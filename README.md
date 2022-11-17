# API_LOADTEST

| Endpoints | Description | Parameter
| ----------- | ----------- |----------- |
| /api/v1/transactions| Get all transactions |
| /api/v1/transactions_by_id    | Get transaction by id | ?id=<transaction_id> |
| /api/v1/transactions/transact_type  | Get transaction by transaction type | ?transact_type=<transact_type>
| /api/v1/transactions/new     | Post new transactions | {"id": int(id),"transType": transType,"transDate": transDate,"transAmount": float(transAmount)} |
| /api/v1/transactions/delete    | Delete transaction by id | ?id=<transaction_id> |

------------------------------------------------------------------------------------
