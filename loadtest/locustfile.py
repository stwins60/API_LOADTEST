from werkzeug.datastructures import Headers
from locust import HttpUser, SequentialTaskSet, task, between
import json
import requests
import logging
import random


logging.basicConfig(level=logging.INFO)
class UserBehavior(SequentialTaskSet):

    def on_start(self):
        with self.client.get("/api/v1/transactions", name="get_transactions", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get transactions")
            else:
                response.success()
                logging.info("Successfully got transactions")

    @task
    def get_transactions_by_id(self):
        for i in range(1,13):
            logging.info("Getting transaction by id: " + str(i))
            with self.client.get("/api/v1/transactions_by_id?id={}".format(i), name="get_transaction_by_id", catch_response=True) as response:
                if response.status_code != 200:
                    response.failure("Failed to get transaction by id")
                else:
                    response.success()
                    logging.info("Successfully got transaction by id")
    

    @task
    def get_transactions_by_type(self):
        types = ["PURCHASE", "REFUND"]
        for i in types:
            type = random.choice(types)
            logging.info("Getting transactions by type: " + type)
            with self.client.get("/api/v1/transactions/transact_type?transact_type={}".format(type), name="get_transactions_by_type", catch_response=True) as response:
                if response.status_code != 200:
                    response.failure("Failed to get transactions by type")
                else:
                    response.success()
                    logging.info("Successfully got transactions by type")
    
    @task
    def add_new_transaction(self):
        params = {
            "id": 14,
            "transType": 'WITHDRAW',
            "transDate": "2021-11-26",
            "transAmount": 150.00
        }
        logging.info("Adding new transaction")
        Headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip'}
        with self.client.post(f"/api/v1/transactions/new", data = json.dumps(params), headers = Headers, name="add_new_transaction", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to add new transaction")
            else:
                response.success()
                logging.info("Successfully added new transaction")


    
    @task
    def delete_transactions_by_id(self):
        RAND = random.randint(1,10)
        logging.info("Deleting transaction by id: " + str(RAND))
        with self.client.delete("/api/v1/transactions/delete?id=1{}".format(RAND), name="delete_transaction_by_id", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to delete transaction by id")
            else:
                response.success()
                logging.info(f"Successfully deleted transaction by id {RAND}")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior: 1}
    wait_time = between(5, 15)
    host = "http://localhost:5000"


