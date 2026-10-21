---
url: https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1
title: Package google.cloud.universalledger.v1 \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:04.767989+00:00
---

# Package google.cloud.universalledger.v1  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Package google.cloud.universalledger.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[UniversalLedger](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UniversalLedger)` (interface)
  * `[Account](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Account)` (message)
  * `[AccountIdList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountIdList)` (message)
  * `[AccountManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountManagerDetails)` (message)
  * `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` (enum)
  * `[ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ActivateAccount)` (message)
  * `[AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AddRoles)` (message)
  * `[AmountValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AmountValue)` (message)
  * `[BalanceToSettle](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.BalanceToSettle)` (message)
  * `[BoolList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.BoolList)` (message)
  * `[Burn](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Burn)` (message)
  * `[ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ChangeAccountManager)` (message)
  * `[ClearingHouseDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClearingHouseDetails)` (message)
  * `[ClientTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClientTransaction)` (message)
  * `[ContractDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractDetails)` (message)
  * `[ContractPermission](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractPermission)` (enum)
  * `[ContractTokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractTokenManagerDetails)` (message)
  * `[CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccount)` (message)
  * `[CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccountManager)` (message)
  * `[CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateClearinghouse)` (message)
  * `[CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContract)` (message)
  * `[CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContractTokenManager)` (message)
  * `[CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateCurrencyOperator)` (message)
  * `[CreateSnapshot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateSnapshot)` (message)
  * `[CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateTokenManager)` (message)
  * `[CurrencyOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyOperatorDetails)` (message)
  * `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` (message)
  * `[DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DeactivateAccount)` (message)
  * `[DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DecreaseTokenIssuanceLimit)` (message)
  * `[DictList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DictList)` (message)
  * `[DictValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DictValue)` (message)
  * `[Endpoint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Endpoint)` (message)
  * `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` (message)
  * `[EventDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.EventDetails)` (message)
  * `[EventType](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.EventType)` (enum)
  * `[ExecutionDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ExecutionDetails)` (message)
  * `[Fields](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Fields)` (message)
  * `[GetEndpointRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GetEndpointRequest)` (message)
  * `[GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GrantContractPermissions)` (message)
  * `[IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.IncreaseTokenIssuanceLimit)` (message)
  * `[Int64List](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Int64List)` (message)
  * `[InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.InvokeContractMethod)` (message)
  * `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` (enum)
  * `[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeySlot)` (enum)
  * `[ListEndpointsRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ListEndpointsRequest)` (message)
  * `[ListEndpointsResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ListEndpointsResponse)` (message)
  * `[MerkleTree](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.MerkleTree)` (message)
  * `[Mint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Mint)` (message)
  * `[NoneValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.NoneValue)` (enum)
  * `[PlatformOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.PlatformOperatorDetails)` (message)
  * `[ProofOfInclusion](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion)` (message)
  * `[ProofOfInclusion.MerkleTreeNode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode)` (message)
  * `[QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QualifiedCurrencyValue)` (message)
  * `[QueryAccountRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryAccountRequest)` (message)
  * `[QueryAccountResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryAccountResponse)` (message)
  * `[QueryDataRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryDataRequest)` (message)
  * `[QueryDataResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryDataResponse)` (message)
  * `[QueryTransactionStateRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryTransactionStateRequest)` (message)
  * `[QueryTransactionStateResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryTransactionStateResponse)` (message)
  * `[RedactedField](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RedactedField)` (message)
  * `[RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveRoles)` (message)
  * `[RemoveSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveSigningPublicKey)` (message)
  * `[ReplaceSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ReplaceSigningPublicKey)` (message)
  * `[Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Role)` (enum)
  * `[RoundCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RoundCertificate)` (message)
  * `[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementMode)` (enum)
  * `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest)` (message)
  * `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SignedTransaction)` (message)
  * `[StatusEvent](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.StatusEvent)` (message)
  * `[StringList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.StringList)` (message)
  * `[SubmitOperationalTransactionRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitOperationalTransactionRequest)` (message)
  * `[SubmitOperationalTransactionResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitOperationalTransactionResponse)` (message)
  * `[SubmitTransactionRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionRequest)` (message)
  * `[SubmitTransactionResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionResponse)` (message)
  * `[TokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TokenManagerDetails)` (message)
  * `[TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionAttempt)` (message)
  * `[TransactionAttempt.TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionAttempt.TransactionStatus)` (enum)
  * `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` (message)
  * `[TransactionChain](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionChain)` (message)
  * `[TransactionEffect](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEffect)` (message)
  * `[TransactionEffects](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEffects)` (message)
  * `[TransactionEvent](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEvent)` (message)
  * `[TransactionEvent.EventAttribute](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEvent.EventAttribute)` (message)
  * `[TransactionState](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionState)` (message)
  * `[TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionStatus)` (message)
  * `[Transfer](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Transfer)` (message)
  * `[TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferContractTokenManager)` (message)
  * `[TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferCurrencyOperator)` (message)
  * `[TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferPlatformOperator)` (message)
  * `[UserDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UserDetails)` (message)
  * `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)` (message)



## UniversalLedger

A service for interacting with the Google Cloud Universal Ledger. Endpoints are pre-created and managed by Google and cannot be modified by users. The names of available endpoints will be provided in the public documentation. An endpoint is a regional resource within a Universal Ledger network. Requests sent to an endpoint may be routed to different validators in the given network within the given region.

GetEndpoint  
---  
` rpc GetEndpoint(`[GetEndpointRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GetEndpointRequest)`) returns (`[Endpoint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Endpoint)`) ` Gets the details of a specific endpoint.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEndpoints  
---  
` rpc ListEndpoints(`[ListEndpointsRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ListEndpointsRequest)`) returns (`[ListEndpointsResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ListEndpointsResponse)`) ` Lists all endpoints for a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryAccount  
---  
` rpc QueryAccount(`[QueryAccountRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryAccountRequest)`) returns (`[QueryAccountResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryAccountResponse)`) ` Queries all the information stored about an account in the network. The returned account details may vary between calls, because an endpoint may route requests to different validators within the network and region, and the validators may not be at the same round ID at any given time.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryData  
---  
` rpc QueryData(`[QueryDataRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryDataRequest)`) returns (`[QueryDataResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryDataResponse)`) ` Queries the network for information stored on the ledger, such as accounts and transactions.Access to certain sensitive fields, such as account balances, may be restricted based on the identity of the sender derived from the signature in the request. If the sender lacks permission, sensitive fields will be redacted from the response and reported in the `redacted_fields` field.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryTransactionState  
---  
` rpc QueryTransactionState(`[QueryTransactionStateRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryTransactionStateRequest)`) returns (`[QueryTransactionStateResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QueryTransactionStateResponse)`) ` Queries the state of a transaction. This method can be called for any transaction submitted to the network. The returned transaction details may vary between calls, because an endpoint may route requests to different validators within the network and region, and the validators may not be at the same round ID at any given time.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SubmitOperationalTransaction  
---  
` rpc SubmitOperationalTransaction(`[SubmitOperationalTransactionRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitOperationalTransactionRequest)`) returns (`[SubmitOperationalTransactionResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitOperationalTransactionResponse)`) ` Submits an operational transaction to the network. This method returns only after the transaction has been replicated across a majority of validators in the network, or if the transaction fails.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SubmitTransaction  
---  
` rpc SubmitTransaction(`[SubmitTransactionRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionRequest)`) returns (`[SubmitTransactionResponse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionResponse)`) ` Submits a transaction to the network. The request is first validated for basic correctness. If validation fails, the request will fail immediately. If validation succeeds, this method returns only after the transaction has been replicated across a majority of validators in the network, or until the request fails.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Account

Represents the state of an account on the ledger.

Fields  
---  
`sequence_number` |  `int64` Output only. The sequence number of this account. This number increments with each transaction sent by this account.  
`public_key` |  `bytes` Output only. The primary public key associated with this account, used for signature verification.  
`round_id` |  `int64` Output only. The ID of the execution round (similar to block "height") at which the account information provided is accurate.  
`comment` |  `string` Output only. The account comment stored when this account was created.  
Union field `account_details`. Specific details based on the type of account. `account_details` can be only one of the following:  
`user_details` |  `[UserDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UserDetails)` Output only. Details for a standard user account.  
`account_manager_details` |  `[AccountManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountManagerDetails)` Output only. Details for an account manager account.  
`token_manager_details` |  `[TokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TokenManagerDetails)` Output only. Details for a token manager account.  
`contract_token_manager_details` |  `[ContractTokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractTokenManagerDetails)` Output only. Details for a contract token manager account.  
`contract_details` |  `[ContractDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractDetails)` Output only. Details for a smart contract account.  
`clearinghouse_details` |  `[ClearingHouseDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClearingHouseDetails)` Output only. Details for a clearinghouse account.  
`currency_operator_details` |  `[CurrencyOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyOperatorDetails)` Output only. Details for a currency operator account.  
`platform_operator_details` |  `[PlatformOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.PlatformOperatorDetails)` Output only. Details for a platform operator account.  
  
## AccountIdList

A list of account IDs.

Fields  
---  
`values[]` |  `string` Optional. The account ID values.  
  
## AccountManagerDetails

Details specific to an Account Manager.

Fields  
---  
`token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `token_manager_id` instead. The default token manager for accounts created by this account manager.  
`num_accounts` |  `int32` Output only. The number of accounts created by this account manager.  
`token_manager_id` |  `string` Output only. The ID of the default token manager for accounts created by this account manager.  
  
## AccountStatus

The status of an account.

Enums  
---  
`ACCOUNT_STATUS_UNSPECIFIED` | Invalid status.  
`ACCOUNT_STATUS_ACTIVE` | Active state where the account can conduct the operations allowed by its roles.  
`ACCOUNT_STATUS_INACTIVE` | Inactive state where all transactions on the account are forbidden. The manager of the account can still send account management transactions.  
  
## ActivateAccount

Marks an account as `ACCOUNT_STATUS_ACTIVE`. The sender must be the account manager of the account to activate.

The account owner can resume normal operations permitted by the roles on the account.

Fields  
---  
`account  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[account_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ActivateAccount.FIELDS.string.google.cloud.universalledger.v1.ActivateAccount.account_id)` instead. The ID of the account to be activated.  
`account_id` |  `string` Optional. The ID of the account to be activated. One of `account` or `account_id` must be specified. The value is limited to 60 characters.  
  
## AddRoles

Adds the specified roles to the account. The sender must be the account manager of the account to modify.

Fields  
---  
`account  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[account_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AddRoles.FIELDS.string.google.cloud.universalledger.v1.AddRoles.account_id)` instead. The ID of the account to be modified.  
`account_id` |  `string` Optional. The ID of the account to be modified. One of `account` or `account_id` must be specified. The value is limited to 60 characters.  
`roles[]` |  `[Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Role)` Required. The roles to be added.  
  
## AmountValue

Represents a denominated amount in a currency.

Fields  
---  
`currency` |  `[QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QualifiedCurrencyValue)` Required. The currency of the amount.  
`amount_value` |  `int64` Required. The number of minor units of the currency.  
  
## BalanceToSettle

A balance to settle between two token managers.

Fields  
---  
`balance_payer  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `balance_payer_id` instead. The account which owes the balance to be settled.  
`balance_payer_id` |  `string` Output only. The ID of the account which owes the balance to be settled.  
`balance_receiver  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `balance_receiver_id` instead. The account which is owed the balance to be settled.  
`balance_receiver_id` |  `string` Output only. The ID of the account which is owed the balance to be settled.  
`balance` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The balance to settle. Must be positive.  
  
## BoolList

A list of booleans.

Fields  
---  
`values[]` |  `bool` Optional. The boolean values.  
  
## Burn

Burns currency tokens. The sender must be a token manager and the account supplying the tokens to burn must additionally sign the transaction.

The expected flow is that the token manager will have its designated burn account which customers would transfer the tokens to before they are burnt. Alternatively, the customers could directly sign the transaction in which case it would act as an atomic "transfer-and-burn" transaction.

Fields  
---  
`burn_amount` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. The amount to burn.  
`payer  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[payer_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Burn.FIELDS.string.google.cloud.universalledger.v1.Burn.payer_id)` instead. The account supplying the tokens to burn. The account must have the `ROLE_PAYER` enabled on it.  
`payer_id` |  `string` Optional. The ID of the account supplying the tokens to burn. The payer account must have the `ROLE_PAYER` enabled on it. One of `payer` or `payer_id` must be specified.  
  
## ChangeAccountManager

Transfers the responsibility of managing a particular account to another manager. The sender must be the current account manager of the account and, to provide consent, the new manager must also sign this transaction.

Fields  
---  
`account  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[account_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ChangeAccountManager.FIELDS.string.google.cloud.universalledger.v1.ChangeAccountManager.account_id)` instead. The ID of the account whose manager is to be changed.  
`account_id` |  `string` Optional. The ID of the account whose manager is to be changed. One of `account` or `account_id` must be specified. The value is limited to 60 characters.  
`next_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[next_manager_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ChangeAccountManager.FIELDS.string.google.cloud.universalledger.v1.ChangeAccountManager.next_manager_id)` instead. The ID of the new proposed account manager. Validation requires that the new manager has also signed this transaction.  
`next_manager_id` |  `string` Optional. The ID of the new proposed account manager. Validation requires that the new manager has also signed this transaction. One of `next_manager` or `next_manager_id` must be specified. The value is limited to 60 characters.  
  
## ClearingHouseDetails

Details specific to a Clearinghouse.

Fields  
---  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Output only. The status of this account.  
`balances[]` |  `[BalanceToSettle](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.BalanceToSettle)` Output only. The balances that this clearinghouse is currently tracking for settlement.  
`settlement_mode` |  `[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementMode)` Output only. The settlement mode of this clearinghouse.  
  
## ClientTransaction

Represents a transaction initiated by a client.

Fields  
---  
`source  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. The transaction sender. Deprecated: Use `[sender_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClientTransaction.FIELDS.string.google.cloud.universalledger.v1.ClientTransaction.sender_id)` instead.  
`sender_id` |  `string` Optional. The ID of the account that is sending this transaction. One of `source` or `sender_id` must be set.  
`signatories[]  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Accounts that, in addition to the sender, have signed this transaction. Deprecated: Use `[other_signatory_ids](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClientTransaction.FIELDS.repeated.string.google.cloud.universalledger.v1.ClientTransaction.other_signatory_ids)` instead.  
`other_signatory_ids[]` |  `string` Optional. The IDs of accounts that, in addition to the sender, have signed this transaction.  
`sequence_number` |  `int64` Required. A unique, monotonically increasing number, starting from 0.This number must be increased by one for each transaction previously submitted to the network by the same transaction sender.Note this does not include any transaction units that may have been submitted as part of a chain, which must not set a sequence number. But it does include the sender of the transaction chain itself.  
`chained_unit` |  `bool` Must be set to true if this client transaction is part of a transaction chain. Otherwise, it must be set to false.This is necessary to prevent a signed transaction intended to be part of a chain from being submitted on its own.  
Union field `kind`. The client transaction-specific message. `kind` can be only one of the following:  
`app  
**(deprecated)**` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` This item is deprecated!Optional. Deprecated: Use one of the message specific fields instead. A client transaction-specific message. Should be any one of:

  * `[TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferPlatformOperator)`
  * `[CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateCurrencyOperator)`
  * `[TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferCurrencyOperator)`
  * `[CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccountManager)`
  * `[CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateTokenManager)`
  * `[CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateClearinghouse)`
  * `[IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.IncreaseTokenIssuanceLimit)`
  * `[DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DecreaseTokenIssuanceLimit)`
  * `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest)`
  * `[Mint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Mint)`
  * `[Burn](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Burn)`
  * `[CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccount)`
  * `[DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DeactivateAccount)`
  * `[ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ActivateAccount)`
  * `[AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AddRoles)`
  * `[RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveRoles)`
  * `[ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ChangeAccountManager)`
  * `[Transfer](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Transfer)`
  * `[CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContract)`
  * `[GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GrantContractPermissions)`
  * `[InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.InvokeContractMethod)`
  * `[CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContractTokenManager)`
  * `[TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferContractTokenManager)`

  
`operational` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Optional. An operational transaction message. Note this can only be sent by the platform operator. Should be any one of:

  * `[CreateSnapshot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateSnapshot)`

  
`transfer_platform_operator_transaction` |  `[TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferPlatformOperator)` Optional. Message for transferring the platform operator role to a new account.  
`create_currency_operator_transaction` |  `[CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateCurrencyOperator)` Optional. Message for creating a new currency operator.  
`transfer_currency_operator_transaction` |  `[TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferCurrencyOperator)` Optional. Message for transferring the currency operator role to a new account.  
`create_clearinghouse_transaction` |  `[CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateClearinghouse)` Optional. Message for creating a new clearinghouse.  
`create_account_manager_transaction` |  `[CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccountManager)` Optional. Message for creating a new account manager.  
`create_token_manager_transaction` |  `[CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateTokenManager)` Optional. Message for creating a new token manager associated to the currency of the operator sending the request.  
`increase_token_issuance_limit_transaction` |  `[IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.IncreaseTokenIssuanceLimit)` Optional. Notifies the network that the target account has deposited reserve funds and increases its token issuance limit.  
`decrease_token_issuance_limit_transaction` |  `[DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DecreaseTokenIssuanceLimit)` Optional. Notifies the network that the target account wishes to withdraw reserve funds and decreases its token issuance limit.  
`settlement_request_transaction` |  `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest)` Optional. Message for initiating a settlement operation.  
`mint_transaction` |  `[Mint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Mint)` Optional. Message for minting currency tokens and transferring them to an account.  
`burn_transaction` |  `[Burn](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Burn)` Optional. Message for burning currency tokens from an account.  
`create_account_transaction` |  `[CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccount)` Optional. Message for creating a new user account.  
`deactivate_account_transaction` |  `[DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DeactivateAccount)` Optional. Message for deactivating a user account.  
`activate_account_transaction` |  `[ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ActivateAccount)` Optional. Message for activating a user account.  
`add_roles_transaction` |  `[AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AddRoles)` Optional. Message for adding roles to an account.  
`remove_roles_transaction` |  `[RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveRoles)` Optional. Message for removing roles from an account.  
`change_account_manager_transaction` |  `[ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ChangeAccountManager)` Optional. Message for changing the account manager of an account.  
`transfer_transaction` |  `[Transfer](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Transfer)` Optional. Message for transferring tokens from one user account to another.  
`create_contract_transaction` |  `[CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContract)` Optional. Message for creating a new contract on the ledger.  
`grant_contract_permissions_transaction` |  `[GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GrantContractPermissions)` Optional. Message for granting permissions to a contract.  
`invoke_contract_method_transaction` |  `[InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.InvokeContractMethod)` Optional. Message for invoking the execution of a contract method.  
`create_contract_token_manager_transaction` |  `[CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContractTokenManager)` Optional. Message for creating a new token manager associated to the currency of the operator sending the request.  
`transfer_contract_token_manager_transaction` |  `[TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferContractTokenManager)` Optional. Message for transferring the token manager role for a currency from one account to another.  
`remove_signing_public_key_transaction` |  `[RemoveSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveSigningPublicKey)` Optional. Message for removing an account signing key.  
`replace_signing_public_key_transaction` |  `[ReplaceSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ReplaceSigningPublicKey)` Optional. Message for replacing an account signing key.  
`chain` |  `[TransactionChain](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionChain)` Optional. Message for a transaction chain including multiple transaction units to execute in sequence.  
  
## ContractDetails

Details specific to a Smart Contract.

Fields  
---  
`owner  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `owner_id` instead. The owner of the contract.  
`owner_id` |  `string` Output only. The ID of the owner of the contract.  
`code` |  `bytes` Output only. The serialized contract code.  
`contract_fields` |  `[Fields](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Fields)` Output only. The contract fields (field name -> value) for this contract.  
`currency_balances` |  `map<string, `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)`>` Output only. The currency balances held by the contract (currency operator -> balance).  
  
## ContractPermission

The set of permissions that can be granted to a contract. More values are expected to be added in the future.

Enums  
---  
`CONTRACT_PERMISSION_UNSPECIFIED` | Invalid permission.  
`CONTRACT_PERMISSION_STORAGE` | Allows a contract to read and write into storage owned by the account who granted the permission. The contract can only read and write the properties that it has previously written.Note this does not allow the contract to read or write data managed by other contracts; nor does it allow the contract to directly update other account properties (for example, the balance of the account in its native currency).  
  
## ContractTokenManagerDetails

Details specific to a Contract Token Manager.

Fields  
---  
`issuance_limit` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The amount of tokens this contract token manager is allowed to provide backing for.Since contract token managers cannot increase or decrease their issuance limit, this should equal the `issued_tokens`.  
`issued_tokens` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The amount of tokens this contract token manager is providing backing for (that is, its total liability).This equals to the sum of all balances held in contracts for its currency, plus its net position in the settlement matrix.  
`previous_contract_token_manager_id` |  `string` Output only. The account ID of the previous contract token manager for this currency. This forms an audit trail that can be traversed to discover all previous managers. If this is the first contract token manager for the currency, this will be empty.  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Output only. The status of this account.  
  
## CreateAccount

Creates a new user account. The sender must be an account manager.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the account owner. Note that this is _not_ the public key of the sender. This is the public key of the _new_ account owner and it will be stored on the ledger. It will be used to validate the signature of the transactions emanating from the created account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`roles[]` |  `[Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Role)` Optional. The list of roles to grant to this account.  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Optional. The status of the account to be created. By default, the account status of a newly created account will be `ACCOUNT_STATUS_ACTIVE`.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[token_manager_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccount.FIELDS.string.google.cloud.universalledger.v1.CreateAccount.token_manager_id)` instead. The token manager for this account. This field is optional and if not supplied, the default token manager associated to the account manager (that is, the sender of this transaction) will be used.  
`token_manager_id` |  `string` Optional. The ID of the token manager for this account. This field is optional and if not supplied, the default token manager associated to the account manager (that is, the sender of this transaction) will be used. The value is limited to 60 characters.  
  
## CreateAccountManager

Creates a new account manager. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new account manager. Note that this is _not_ the public key of the operator. This public key will be associated with the account manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the account manager's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`default_token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[default_token_manager_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateAccountManager.FIELDS.string.google.cloud.universalledger.v1.CreateAccountManager.default_token_manager_id)` instead. The default token manager for the accounts that will be created by this manager.  
`default_token_manager_id` |  `string` Optional. The ID of the default token manager for the accounts that will be created by this manager. The value is limited to 60 characters.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## CreateClearinghouse

Creates a new clearinghouse. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new clearinghouse. Note that this is _not_ the public key of the operator. This public key will be associated with the clearinghouse and stored on the ledger. It will be used to validate signature of the transactions emanating from the clearinghouse's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`settlement_mode` |  `[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementMode)` Required. The settlement mode for this clearinghouse. Required. Considered public information.  
  
## CreateContract

Stores a contract on the ledger.

Fields  
---  
`contract_bytes` |  `bytes` Serialised contract bytes.  
`arguments  
**(deprecated)**` |  `map<string, `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)`>` This item is deprecated!Optional. Immutable. Deprecated: Use `[init_arguments](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateContract.FIELDS.repeated.google.cloud.universalledger.v1.CreateContract.InitArgumentsEntry.google.cloud.universalledger.v1.CreateContract.init_arguments)` instead. Arguments for the `__init__` method.  
`init_arguments` |  `map<string, `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)`>` Optional. Immutable. Contains arguments for the `__init__` method.  
`contract_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the contract. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## CreateContractTokenManager

Creates a new contract token manager associated with the currency of the operator sending the request. The sender must be a currency operator. The newly created contract token manager is active by default. If the contract token manager has to be replaced, the TransferContractTokenManager transaction should be sent instead. If another contract token manager associated with the same currency exists, this transaction will fail.

Unlike regular token managers, contract token managers are not allowed to execute transactions such as mint or burn. They can, however, participate in settlement operations.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new contract token manager. Note that this is _not_ the public key of the operator. This public key will be associated with the contract token manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the contract token manager's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
  
## CreateCurrencyOperator

Creates a new currency operator. The sender must be the platform operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

This transaction must introduce a new currency into the system. If the specified currency already exists, this transaction will fail. If the currency operator has to be replaced, the TransferCurrencyOperator transaction should be sent instead.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new currency operator. This public key will be associated with the currency operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the operator's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`currency  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Use `[currency_code](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CreateCurrencyOperator.FIELDS.string.google.cloud.universalledger.v1.CreateCurrencyOperator.currency_code)` instead. The fiat currency associated with this operator, represented as a 3-capital-letter ISO 4217 code. Considered public information.  
`currency_code` |  `string` Optional. The fiat currency associated with this operator, represented as a 3-capital-letter ISO 4217 code. Considered public information.  
  
## CreateSnapshot

This type has no fields.

Triggers the creation of a snapshot of the network. The sender must be the platform operator.

## CreateTokenManager

Creates a new token manager associated to the currency of the operator sending the request. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new token manager. Note that this is _not_ the public key of the operator. This public key will be associated with the token manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the token manager's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## CurrencyOperatorDetails

Details specific to a Currency Operator.

Fields  
---  
`currency  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated: Use `currency_code` instead. The currency associated with this account, represented by the 3-letter ISO 4217 code.  
`currency_code` |  `string` Output only. The ID of the currency associated with this account, represented by the 3-letter ISO 4217 code.  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Output only. The status of this account.  
`previous_entity_id  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `previous_currency_operator_id` instead. The previous currency operator which transferred ownership of the currency operator role to this account. If this is the first currency operator for the currency, this will be empty.  
`previous_currency_operator_id` |  `string` Output only. The ID of the previous currency operator which transferred ownership of the currency operator role to this account. If this is the first currency operator for the currency, this will be empty.  
`platform_operator_entity_id  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `platform_operator_id` instead. The platform operator which created this currency operator.  
`platform_operator_id` |  `string` Output only. The ID of the platform operator which created this currency operator.  
`contract_token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `contract_token_manager_id` instead. The contract token manager associated with this currency operator.  
`contract_token_manager_id` |  `string` Output only. The ID of the contract token manager associated with this currency operator.  
`clearinghouse_id` |  `string` Output only. The ID of the clearinghouse associated with this currency operator.  
  
## CurrencyValue

Represents an amount of currency (i.e. money). Note that the denominated currency is not included in this message. The relevant currency is decided by the account that sends the transaction. Each account has a unique immutable currency associated to it.

Fields  
---  
`value` |  `int64` Required. The number of minor units of the currency.This smallest valid denomination is referred to as "minor units" and is specified in [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). As an example, for USD, the value will be the number of cents and for GBP it will be the number of pence. For the Japanese Yen which does not have a minor unit, it will be the number of Yen.  
  
## DeactivateAccount

Marks an account as `ACCOUNT_STATUS_INACTIVE`. The sender must be the account manager of the account to deactivate.

This implies that the account owner will not be able to make any transactions on the account regardless of the roles.

Fields  
---  
`account  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[account_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DeactivateAccount.FIELDS.string.google.cloud.universalledger.v1.DeactivateAccount.account_id)` instead. The ID of the account to be deactivated.  
`account_id` |  `string` Optional. The ID of the account to be deactivated. One of `account` or `account_id` must be specified. The value is limited to 60 characters.  
  
## DecreaseTokenIssuanceLimit

Notifies the network that the target account wishes to withdraw reserve funds and decreases its token issuance limit. The sender must be a clearinghouse account.

Note that this transaction must be successfully finalized _before_ the reserve funds can be withdrawn. This is necessary because it is possible for the transaction to fail (for example, if the minted amount is already above the requested reduced limit).

Fields  
---  
`token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[token_manager_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DecreaseTokenIssuanceLimit.FIELDS.string.google.cloud.universalledger.v1.DecreaseTokenIssuanceLimit.token_manager_id)` instead. The ID of the institutional account whose mint limit is to be lowered. This account must be a token manager for the transaction to be valid.  
`token_manager_id` |  `string` Optional. The ID of the institutional account whose mint limit is to be lowered. This account must be a token manager for the transaction to be valid. One of `token_manager_id` (preferred) or `token_manager` (deprecated) must be specified.  
`amount` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. The amount by which to lower the limit. The amount must be positive. The transaction will fail if the reduced limit will fall below the currently issued tokens.  
  
## DictList

A list of dictionaries.

Fields  
---  
`values[]` |  `[DictValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DictValue)` Optional. The DictValue values. All nested dicts must have the same concrete type.  
  
## DictValue

Indices map key to value. For example, `keys[0]` key maps to `values[0]`.

Fields  
---  
Union field `keys`. Each key can be exactly one kind. `keys` can be only one of the following:  
`bool_keys` |  `[BoolList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.BoolList)` Optional. A list of boolean keys.  
`string_keys` |  `[StringList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.StringList)` Optional. A list of string keys.  
`int64_keys` |  `[Int64List](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Int64List)` Optional. A list of int64 keys.  
`account_id_keys` |  `[AccountIdList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountIdList)` Optional. A list of account ID keys.  
Union field `values`. Each value can be exactly one kind. `values` can be only one of the following:  
`bool_values` |  `[BoolList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.BoolList)` Optional. A list of boolean values.  
`string_values` |  `[StringList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.StringList)` Optional. A list of string values.  
`int64_values` |  `[Int64List](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Int64List)` Optional. A list of int64 values.  
`dict_values` |  `[DictList](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DictList)` Optional. Values are a list of nested dictionaries.  
  
## Endpoint

Represents a Universal Ledger endpoint.

Fields  
---  
`name` |  `string` Identifier. The resource name of the endpoint. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
  
## Entity

An entity in the Universal Ledger network. All accounts are attached to an entity. The entity ID, also often referred to as the account ID, is unique and immutable across the network.

Fields  
---  
`id` |  `string` Output only. The ID assigned to the entity. This is assigned by the network on account creation.  
  
## EventDetails

Represents additional details of a status event.

Fields  
---  
Union field `event_details`. The details of the event. `event_details` can be only one of the following:  
`execution_details` |  `[ExecutionDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ExecutionDetails)` Output only. Additional details for an execution event.  
  
## EventType

Represents the type of an event in the processing of a transaction, as observed by the validator that the request was routed to.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | Unknown or unspecified event.  
`EVENT_TYPE_RECEIVED` | The transaction was received by this validator directly from a client.  
`EVENT_TYPE_BROADCASTED` | The transaction was broadcasted by this to other validators.  
`EVENT_TYPE_ORDERED` | The transaction was ordered and scheduled for execution by this validator.  
`EVENT_TYPE_EXECUTION_STARTED` | The execution of the transaction has started.  
`EVENT_TYPE_EXECUTION_COMPLETED` | The execution of the transaction has completed.  
`EVENT_TYPE_FINALIZED` | The transaction has been finalized by this validator.  
  
## ExecutionDetails

Additional details for an execution event.

Fields  
---  
`round_id` |  `int64` Output only. The round ID at which the execution event occurred.  
  
## Fields

A map of fields (field name -> value) from a contract used to represent contract fields or account fields.

Fields  
---  
`fields` |  `map<string, `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)`>` Output only. The map of field names to their values.  
  
## GetEndpointRequest

Request message for GetEndpoint.

Fields  
---  
`name` |  `string` Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
  
## GrantContractPermissions

Grants permissions to the contract by the transaction sender. If `delegate_contract_id` is specified, the permissions and corresponding storage are granted exclusively to the `delegate_contract_id` contract, not the sender.

Note that there is no support for revoking permissions.

Fields  
---  
`contract  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[contract_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.GrantContractPermissions.FIELDS.string.google.cloud.universalledger.v1.GrantContractPermissions.contract_id)` instead. ID of the contract to which permissions are being granted.  
`contract_id` |  `string` Optional. The ID of the contract to which permissions are being granted. One of `contract` or `contract_id` must be specified.  
`permissions[]` |  `[ContractPermission](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ContractPermission)` The permissions to be granted.  
`delegate_contract_id` |  `string` Optional. The contract ID for which permissions are being granted. The transaction sender must be the owner of this contract.  
  
## IncreaseTokenIssuanceLimit

Transactions for token issuance and minting. Notifies the network that the target account has deposited reserve funds and increases its token issuance limit. The sender must be a clearinghouse account.

Fields  
---  
`token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[token_manager_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.IncreaseTokenIssuanceLimit.FIELDS.string.google.cloud.universalledger.v1.IncreaseTokenIssuanceLimit.token_manager_id)` instead. The ID of the institutional account whose mint limit is to be raised. This account must be a token manager for the transaction to be valid.  
`token_manager_id` |  `string` Optional. The ID of the institutional account whose mint limit is to be raised. This account must be a token manager for the transaction to be valid. One of `token_manager` or `token_manager_id` must be specified.  
`amount` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. The amount by which to raise the limit. The amount must be positive.  
  
## Int64List

A list of int64s.

Fields  
---  
`values[]` |  `int64` Optional. The int64 values.  
  
## InvokeContractMethod

Invokes the execution of a contract method.

Fields  
---  
`contract  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[contract_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.InvokeContractMethod.FIELDS.string.google.cloud.universalledger.v1.InvokeContractMethod.contract_id)` instead. ID of the contract to run.  
`contract_id` |  `string` Optional. The ID of the contract to run. One of `contract` or `contract_id` must be specified.  
`method_name` |  `string` Name of the method to run.  
`arguments  
**(deprecated)**` |  `map<string, `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)`>` This item is deprecated!Optional. Immutable. Deprecated: Use `[method_arguments](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.InvokeContractMethod.FIELDS.repeated.google.cloud.universalledger.v1.InvokeContractMethod.MethodArgumentsEntry.google.cloud.universalledger.v1.InvokeContractMethod.method_arguments)` instead. Arguments for the method.  
`method_arguments` |  `map<string, `[Value](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Value)`>` Optional. Immutable. Contains arguments to pass to the method.  
`payment` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` The amount to be paid. Must be greater than zero when invoking payable methods; and zero for non-payable ones.  
  
## KeyFormat

Specifies the format a public key is provided in. New values may be added to this enum in the future.

Enums  
---  
`KEY_FORMAT_UNSPECIFIED` | The key format is unspecified. This value is invalid and should not be used.  
`KEY_FORMAT_TINK_WIRE_FORMAT` | A binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization).  
`KEY_FORMAT_PEM_EC_P256_SHA256` | A PEM-encoded elliptic curve signing key using the P-256 curve with SHA256 digest. Signatures must be provided in DER format.  
  
## KeySlot

An identifier of the slots which can hold keys on an account.

Enums  
---  
`KEY_SLOT_UNSPECIFIED` | The key slot is unspecified.  
`KEY_SLOT_PRIMARY` | The primary key slot.  
`KEY_SLOT_ALTERNATE` | The alternate key slot.  
  
## ListEndpointsRequest

Request message for ListEndpoints.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of endpoints. Format: `projects/{project}/locations/{location}`  
`page_size` |  `int32` Optional. The maximum number of endpoints to return. The service may return fewer than this value. If unspecified, at most 50 endpoints will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEndpoints` call. Provide this to retrieve the subsequent page.  
  
## ListEndpointsResponse

Response message for ListEndpoints.

Fields  
---  
`endpoints[]` |  `[Endpoint](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Endpoint)` The endpoints for the given project and location.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## MerkleTree

A Merkle tree with a cryptographic digest of the root node.

Fields  
---  
`root_hash_hex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The cryptographic digest of the root node. Deprecated: Use `[root_digest_hex](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.MerkleTree.FIELDS.string.google.cloud.universalledger.v1.MerkleTree.root_digest_hex)` instead.  
`root_digest_hex` |  `string` Output only. The hexadecimal representation of the digest of the root node. Format: A 64-character hexadecimal string.  
`num_transactions` |  `int64` Output only. The number of transactions in the tree.  
  
## Mint

Mints currency tokens and transfers them to a specified account. The sender must be a token manager.

Fields  
---  
`mint_amount` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. The amount to mint. The amount must be such that the total tokens minted by the token manager do not exceed the mint limit. If the amount is higher than that, the transaction must be rejected  
`beneficiary  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[beneficiary_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Mint.FIELDS.string.google.cloud.universalledger.v1.Mint.beneficiary_id)` instead. The account to which the minted amount should be transferred. The beneficiary account must have the `ROLE_RECEIVER` enabled on it.  
`beneficiary_id` |  `string` Optional. The ID of the account to which the minted amount should be transferred. The receiving account must have the `ROLE_RECEIVER` enabled on it. One of `beneficiary` or `beneficiary_id` must be specified.  
  
## NoneValue

A singleton enumeration to represent the None value.

Enums  
---  
`NONE_VALUE_UNSPECIFIED` | The None value.  
  
## PlatformOperatorDetails

Details specific to a Platform Operator.

Fields  
---  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Output only. The status of this account.  
`previous_entity_id  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `previous_platform_operator_id` instead. The previous platform operator which transferred ownership of the platform operator role to this account. If this is the first platform operator, this will be empty.  
`previous_platform_operator_id` |  `string` Output only. The ID of the previous platform operator which transferred ownership of the platform operator role to this account. If this is the first platform operator, this will be empty.  
  
## ProofOfInclusion

Certificate of the inclusion of the effects of a transaction in the world state.

Fields  
---  
`transaction_certificate` |  `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` Output only. Certificate of the inclusion of the transaction effects in a specific round.  
`round_certificate` |  `[RoundCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RoundCertificate)` Output only. Certificate of the execution of the round.  
`path_to_round_root[]` |  `[MerkleTreeNode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode)` Output only. Cryptographic proof of inclusion of the transaction effects in the execution round.It is given as a path from a given leaf (a transaction digest) to the root of the execution round. The path is represented as a list of (left child, right child) pairs, and the first pair is the left and right children of the given leaf's parent node. For example, assuming the Merkle tree was built with eight leaf digests `[t0, t1, t2, t3, t4, t5, t6, t7]`, having the following structure:
    
    
           _____root_digest____
          |                    |
       __ h20__             __h21__
      |        |           |       |
     h10     h11          h12     h13
     | |     | |          | |     | |
    t0 t1   t2 t3        t4 t5   t6 t7
    

In here, `path_to_round_root` for `t0` will contain: `[(t0, t1), (h10, h11), (h20, h21)]`.One can consecutively compute SHA-256 digests of each path node to verify that the digest of the path produces the same value as the `round_certificate.merkle_tree.root_digest_hex`. Thus, verifying that the leaf was included in the round's Merkle tree.  
  
## MerkleTreeNode

Represents a node in a Merkle tree path.

Fields  
---  
`left_child_hash_hex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The hexadecimal representation of the digest of the left child of a node. Deprecated: Use `[left_child_digest_hex](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode.FIELDS.string.google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode.left_child_digest_hex)` instead.  
`right_child_hash_hex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The hexadecimal representation of the digest of the right child of a node. Deprecated: Use `[right_child_digest_hex](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode.FIELDS.string.google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNode.right_child_digest_hex)` instead.  
`left_child_digest_hex` |  `string` Output only. The hexadecimal representation of the digest of the left child of a node. Format: A 64-character hexadecimal string.  
`right_child_digest_hex` |  `string` Output only. The hexadecimal representation of the digest of the right child of a node. Format: A 64-character hexadecimal string.  
  
## QualifiedCurrencyValue

Represents a currency on the ledger, which is qualified by its Currency Operator.

Fields  
---  
`operator_id` |  `string` Required. The Currency Operator ID administering the currency.  
  
## QueryAccountRequest

Request message for QueryAccount.

Fields  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
`account_id` |  `string` Required. The account ID to get information about. The value is limited to 60 characters.  
`round_id` |  `int64` Optional. The ID of the execution round (similar to block "height") at which to request data. The returned account information will be accurate for the world state at this execution round. If unspecified, uses the latest finalized round as known by the serving validator. The state at a given round ID is always consistent and canonical.  
  
## QueryAccountResponse

Response message for QueryAccount.

Fields  
---  
`account` |  `[Account](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Account)` The account information, along with the height at which it was obtained.  
  
## QueryDataRequest

Request message for QueryData.

Fields  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
`serialized_signed_query_request` |  `bytes` Required. A protobuf serialized `SignedQueryRequest` to query the Universal Ledger network.  
  
## QueryDataResponse

Response message for QueryData.

Fields  
---  
`redacted_fields[]` |  `[RedactedField](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RedactedField)` Indicates which fields have been redacted from the response due to permission restrictions.  
Union field `kind`. The query-specific result. `kind` can be only one of the following:  
`account` |  `[Account](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Account)` The account information, if the query was for an account.  
`transaction_state` |  `[TransactionState](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionState)` The state of a transaction, if the query was for a transaction.  
  
## QueryTransactionStateRequest

Request message for QueryTransactionState.

Fields  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
`transaction_digest_hex` |  `string` Required. The transaction ID to get the state of.  
  
## QueryTransactionStateResponse

Response message for QueryTransactionState.

Fields  
---  
`transaction_attempts[]` |  `[TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionAttempt)` One entry per each known submission of the transaction to the validator handling the request.  
  
## RedactedField

Information about a redacted field in the response.

Fields  
---  
`redacted_path` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Output only. The fully qualified field paths that were redacted from the payload.  
`reason` |  `string` Output only. A human-readable explanation of why the fields were redacted.  
`reason_code` |  `[Code](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.rpc#google.rpc.Code)` Output only. A machine readable code for why the fields were redacted.  
  
## RemoveRoles

Removes the specified roles from the account. The sender must be the account manager of the account to modify.

Fields  
---  
`account  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[account_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.RemoveRoles.FIELDS.string.google.cloud.universalledger.v1.RemoveRoles.account_id)` instead. The ID of the account to be modified.  
`account_id` |  `string` Optional. The ID of the account to be modified. One of `account` or `account_id` must be specified. The value is limited to 60 characters.  
`roles[]` |  `[Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Role)` Required. The roles to be removed.  
  
## RemoveSigningPublicKey

Removes the account signing key from the specified slot. The other slot must not be empty, and must hold the key used to sign the `ClientTransaction`.

Fields  
---  
`key_slot` |  `[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeySlot)` Required. The key slot we're removing the key from. If this is already empty, the transaction will fail.  
  
## ReplaceSigningPublicKey

Replaces the account signing key in the specified slot. The other slot must not be empty, and must hold the key used to sign the `ClientTransaction`.

Fields  
---  
`key_slot` |  `[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeySlot)` Required. The key slot we're replacing the key in.  
`new_public_key` |  `bytes` Required. The new public key, which will replace the public key in the specified slot.The format of the public key is defined by the new_key_format field. Considered public information.  
`new_key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Required. The key format of the new public key. See the definition of KeyFormat for a list of supported formats. Considered public information.  
  
## Role

The regular set of roles.

Enums  
---  
`ROLE_UNSPECIFIED` | Invalid role.  
`ROLE_PAYER` | The role that allows an account to initiate a payment transaction.  
`ROLE_RECEIVER` | The role that allows an account to receive payments.  
`ROLE_CONTRACT_CREATOR` | The role that allows an account to deploy contracts.  
`ROLE_CONTRACT_PARTICIPANT` | The role that allows an account to interact with deployed contracts.  
  
## RoundCertificate

Certificate of the execution of a round by a specific validator.

Fields  
---  
`round_id` |  `int64` Output only. The ID of the round for which the certificate is for.  
`validator_id` |  `string` Output only. The human readable validator identifier. This is used to look up the public key against which the `validator_signatures` is verified.  
`round_state_checksum_hex` |  `string` Output only. The hex representation of the homomorphic digest over the world state after the effects of this round are applied.  
`round_delta_checksum_hex` |  `string` Output only. The hex representation of the homomorphic digest over the aggregated transaction effects of this round.  
`merkle_tree` |  `[MerkleTree](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.MerkleTree)` Output only. Merkle tree having this round as root node and transaction batches (executed in the round) as the leaves.  
`validator_signatures[]` |  `bytes` Optional. The signature of the validator. This is signed over the digest of the preceding payload of this record.  
`is_finalized` |  `bool` Output only. Boolean to indicate if the round is finalized, i.e., whether a sufficient quorum of validators have certified this round with the same certificate.  
  
## SettlementMode

The settlement mode for a clearinghouse.

Enums  
---  
`SETTLEMENT_MODE_UNSPECIFIED` | The settlement mode is unspecified. This value is invalid and should not be used.  
`SETTLEMENT_MODE_DEFERRED` | The clearinghouse is responsible for tracking the ownership of the off-ledger funds, and periodically issuing `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest)` transactions to maintain the corresponding balances on the ledger in sync.  
`SETTLEMENT_MODE_INSTANT` | The clearinghouse maintains a single pool of funds and the ledger acts as the golden source for the allocation of those funds between the token managers. This settlement mode can also be described as "instant gross settlement."  
  
## SettlementRequest

Initiates a settlement operation between two token managers. The sender must be a clearinghouse account.

In the deferred `[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementMode)` where the clearinghouse has custody of the token manager funds, this is the only transaction that needs to be sent to execute a settlement between the two token managers.

Fields  
---  
`payer  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Immutable. Deprecated: Use `[payer_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest.FIELDS.string.google.cloud.universalledger.v1.SettlementRequest.payer_id)` instead. The account ID of the party that needs to make the fund transfer.  
`payer_id` |  `string` Optional. Immutable. The account ID of the party that needs to make the fund transfer. One of `payer` or `payer_id` must be specified.  
`beneficiary  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Immutable. Deprecated: Use `[beneficiary_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SettlementRequest.FIELDS.string.google.cloud.universalledger.v1.SettlementRequest.beneficiary_id)` instead. The account ID of the party that needs to be paid.  
`beneficiary_id` |  `string` Optional. Immutable. The account ID of the party that will receive the funds. One of `beneficiary` or `beneficiary_id` must be specified.  
`balance` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. Immutable. The balance of issued tokens that need to be transferred by the `payer` account to the `beneficiary` account on the ledger.  
`round_id` |  `int64` Required. Immutable. The round ID at which this settlement amount was computed.  
  
## SignedTransaction

A transaction with attached signatures. To submit a transaction, this message should be serialized and included in a `[SubmitTransactionRequest](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionRequest)`.

Fields  
---  
`serialized_client_transaction` |  `bytes` Required. A serialized `[ClientTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClientTransaction)` with the transaction details.  
`sender_signature` |  `bytes` Required. The signature of the transaction sender.The signature should be computed by signing the `serialized_client_transaction` bytes with their own private key.For a transaction chain, the bytes to be signed are computed as the concatenation of: - A digest of the serialized client transaction of the entire chain. - A digest of the serialized signed transaction of each unit in the chain, in the order they appear in the chain. The digests are computed using SHA-256.  
`sender_signing_key_slot` |  `[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeySlot)` Optional. The key slot of the sender used to sign the transaction. Uses the primary slot of the sender account if not specified.  
`other_signatures[]` |  `bytes` Optional. The signatures of accounts listed as additional transaction signatories. The number and order of these signatures must match the `signatories` field in the `[ClientTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ClientTransaction)`.The bytes to be signed are the same as those for the `sender_signature`, which each signatory should sign with their own private key.The number and identity of additional signatories depends on the particular transaction kind. For a transaction chain, one signature is needed for each account appearing either as the sender or as a signatory of a unit in the chain.  
`other_signing_key_slots[]` |  `[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeySlot)` Optional. The key slots of the accounts listed as additional transaction signatories. If set, the number and order of these key slots must match the `other_signatures` field in the `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SignedTransaction)`. Defaults to the primary slot of each account if not specified.  
  
## StatusEvent

Represents an event in the processing of a transaction as observed by a single validator.

All values reported are from the perspective of the validator handling the request and may differ from the view of other validators.

Fields  
---  
`event_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when the event was recorded by this validator.  
`event_type` |  `[EventType](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.EventType)` Output only. The type of the event.  
`event_details` |  `[EventDetails](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.EventDetails)` Output only. Additional details associated with the event.  
  
## StringList

A list of strings.

Fields  
---  
`values[]` |  `string` Optional. The string values.  
  
## SubmitOperationalTransactionRequest

Request message for SubmitOperationalTransaction.

Fields  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
`serialized_signed_operational_transaction` |  `bytes` Required. A protobuf serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SignedTransaction)` to submit to the ledger. The enclosed client transaction must be an operational transaction, and the sender must be the platform operator. Using a serialized format ensures that all validators compute the same transaction ID as the SHA-256 digest of the serialized bytes.  
  
## SubmitOperationalTransactionResponse

Response message for SubmitOperationalTransaction.

Fields  
---  
`transaction_digest_hex` |  `string` Identifier that uniquely represents the submitted operational transaction. It is the hexadecimal representation of the SHA-256 digest of the `serialized_signed_operational_transaction`. This transaction ID is provided so that a client can track the transaction without needing to implement the hashing logic itself. The identifier can be directly used in subsequent API calls, for example to query the transaction state.  
  
## SubmitTransactionRequest

Request message for SubmitTransaction.

Fields  
---  
`endpoint` |  `string` Required. The endpoint to submit the transaction to. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
`serialized_signed_transaction` |  `bytes` Required. A protobuf serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SignedTransaction)` to submit to the ledger. Using a serialized format ensures that all validators compute the same transaction ID as the SHA-256 digest of the serialized bytes.  
  
## SubmitTransactionResponse

Response message for SubmitTransaction.

Fields  
---  
`transaction_digest_hex` |  `string` Identifier that uniquely represents the submitted transaction. It is the hexadecimal representation of the SHA-256 digest of the `serialized_signed_transaction`. This transaction ID is provided so that a client can track the transaction without needing to implement the hashing logic itself. The identifier can be directly used in subsequent API calls, for example to query the transaction state.  
  
## TokenManagerDetails

Details specific to a Token Manager.

Fields  
---  
`issuance_limit` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The amount of tokens this token manager is allowed to mint.  
`issued_tokens` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The amount of tokens minted by this token manager. This number will increase when minting and decrease when burning.  
  
## TransactionAttempt

The state of an attempted transaction submission.

Fields  
---  
`status` |  `[TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionAttempt.TransactionStatus)` Output only. The current status of the transaction attempt.  
`proof_of_inclusion` |  `[ProofOfInclusion](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.ProofOfInclusion)` Output only. Certificate of the inclusion of the transaction effects in the world state. Only provided if status is `FINALIZED`.  
`status_events[]` |  `[StatusEvent](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.StatusEvent)` Output only. The ordered status events recorded for the transaction attempt.  
  
## TransactionStatus

The status of the transaction attempt.

Enums  
---  
`TRANSACTION_STATUS_UNSPECIFIED` | Unknown or uninitialized state.  
`PENDING` | The transaction is known to this validator, but it is not finalized yet.  
`FINALIZED` | The transaction is finalized. Its effects have been persisted on the blockchain and cannot be reversed.  
  
## TransactionCertificate

Certificate of the execution of a specific transaction in a round.

Fields  
---  
`transaction_digest_hex` |  `string` Output only. The ID of the transaction this certificate is for.  
`round_id` |  `int64` Output only. The ID of the execution round at which this transaction was executed in.  
`transaction_effects` |  `[TransactionEffects](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEffects)` Output only. The effects from the transaction execution.  
`events[]` |  `[TransactionEvent](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEvent)` Output only. Events produced by the transaction.  
`transaction_effects_state_checksum_hex` |  `string` Output only. Homomorphic checksum of the effects. A 2048 byte value encoded as a hexadecimal string.  
`certification_results_digest_hex` |  `string` Output only. The cryptographic digest of all the previous fields in sequence. Used to build a Merkle tree for the proof of inclusion.  
  
## TransactionChain

A transaction chain including multiple transaction units to execute in sequence.

The units will be executed sequentially, in the order they are listed. If all of the units succeed, their cumulative effects will be committed atomically to the world state. Otherwise, if any of them fails, the whole chain will be failed and none of its effects will be applied.

Fields  
---  
`units[]` |  `bytes` The individual units of the chain. Each unit must be a serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SignedTransaction)`.Note that the serialized bytes are required in order to determine the bytes to be signed for the chain itself.  
  
## TransactionEffect

Represents an update by some transaction to the world state.

If it has a `delta_val`, it is assumed to be a delta (an integer offset) applied to the previously stored value on a given key. In that case, `new_val` and `old_val` should be empty.

Otherwise, it is assumed to have at least one of `old_val` or `new_val` (or both). An empty `old_val` indicates the value was inserted. An empty `new_val` indicates the value was deleted.

Fields  
---  
`key` |  `bytes` Output only. The key in the world state that was updated.  
`old_val` |  `bytes` Output only. The value of the key before the transaction was executed.  
`new_val` |  `bytes` Output only. The value of the key after the transaction was executed.  
`delta_val` |  `int64` Output only. An integer offset that was applied to the previously stored value.  
  
## TransactionEffects

Effects of the execution of a transaction.

Fields  
---  
`status` |  `[TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionStatus)` Output only. The resulting status of the transaction execution.  
`effects[]  
**(deprecated)**` |  `[TransactionEffect](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEffect)` This item is deprecated!Output only. Deprecated: Query the network state instead to determine any changes to the world state. The effects of the transaction in the world state.  
  
## TransactionEvent

An event produced by a transaction.

Fields  
---  
`type` |  `string` Output only. The type of event. A special event of type `transaction_output` contains the outputs produced by the transaction—for example, the account ID of a newly created account.  
`attributes[]` |  `[EventAttribute](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionEvent.EventAttribute)` Output only. The event attributes as arbitrary key-value pairs.  
  
## EventAttribute

An individual attribute as a key-value pair.

Fields  
---  
`key` |  `string` Output only. The key of the attribute.  
`value` |  `string` Output only. The value of the attribute.  
  
## TransactionState

The state of a transaction.

Fields  
---  
`transaction_attempts[]` |  `[TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionAttempt)` One entry per each known submission of the transaction to the validator handling the request.  
  
## TransactionStatus

Represents the status of a transaction execution.

Fields  
---  
`code` |  `int32` Output only. The status code, a numeric value whose meaning is defined by the corresponding [gRPC status code](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md).  
`message` |  `bytes` Output only. The error message, if any. Set only if code is not `OK`. This is a string encoded as utf-8 bytes. Stored as bytes to prevent any issues with the determinism of the encoding.  
  
## Transfer

Transfers tokens from one user account to another. The sender must be a regular user account, as opposed to a privileged account like a token manager or an account manager.

Additionally, the transaction sender must have the `ROLE_PAYER` enabled on it, while the receiver must have the `ROLE_RECEIVER` enabled on it.

Fields  
---  
`beneficiary  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[beneficiary_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Transfer.FIELDS.string.google.cloud.universalledger.v1.Transfer.beneficiary_id)` instead. The account that receives the tokens.  
`beneficiary_id` |  `string` Optional. The ID of the account that receives the tokens. One of `beneficiary` or `beneficiary_id` must be specified.  
`amount` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Required. The amount to transfer. The amount must be positive.  
  
## TransferContractTokenManager

Transfers the ownership of the contract token manager to a new account. The sender must be the current currency operator for the currency.

If the transaction is successful, deactivates the current contract token manager for the currency, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new contract token manager. Note that this is _not_ the public key of the operator. This is the public key of the _new_ contract token manager and it will be stored on the ledger. It will be used to validate the signature of the transactions emanating from the contract token manager's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
  
## TransferCurrencyOperator

Transfers the ownership of the given currency operator to a new account. The sender must be the platform operator.

If the transaction is successful, deactivates the given currency operator, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new currency operator. This public key will be associated with the currency operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the currency operator's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`currency_operator  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Optional. Deprecated: Use `[currency_operator_id](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransferCurrencyOperator.FIELDS.string.google.cloud.universalledger.v1.TransferCurrencyOperator.currency_operator_id)` instead. The currency operator to be replaced. Must be active.  
`currency_operator_id` |  `string` Optional. The ID of the currency operator to be replaced. Must be active. One of `currency_operator` or `currency_operator_id` must be specified. The value is limited to 60 characters.  
  
## TransferPlatformOperator

Transfers the ownership of the platform operator to a new account. The sender must be the current platform operator.

If the transaction is successful, deactivates the current platform operator, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.TransactionCertificate)` of the finalized transaction.

Fields  
---  
`public_key` |  `bytes` Required. The public key of the new platform operator. This public key will be associated with the platform operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the platform operator's account.The format of the public key is defined by the `key_format` field. Considered public information.  
`key_format` |  `[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.KeyFormat)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`account_comment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## UserDetails

Details specific to a User account.

Fields  
---  
`account_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `account_manager_id` instead. The account manager for this user.  
`account_manager_id` |  `string` Output only. The ID of the account manager for this user.  
`token_manager  
**(deprecated)**` |  `[Entity](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Entity)` This item is deprecated!Output only. Deprecated: Use `token_manager_id` instead. The token manager for this user.  
`token_manager_id` |  `string` Output only. The ID of the token manager for this user.  
`roles[]` |  `[Role](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Role)` Output only. The list of roles granted to this account.  
`account_status` |  `[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AccountStatus)` Output only. The status of this account.  
`balance` |  `[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.CurrencyValue)` Output only. The token balance of this user account.  
`account_fields  
**(deprecated)**` |  `map<string, `[Fields](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Fields)`>` This item is deprecated!Output only. Deprecated: Use `contract_account_fields` instead. The contract account fields (contract ID -> fields) for this user.  
`contract_account_fields` |  `map<string, `[Fields](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.Fields)`>` Output only. The contract account fields (contract ID -> fields) for this user.  
  
## Value

A concrete value of some type.

Fields  
---  
Union field `value`. The actual value. `value` can be only one of the following:  
`none_value` |  `[NoneValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.NoneValue)` Optional. Represents a None value.  
`bool_value` |  `bool` Optional. A boolean value.  
`int64_value` |  `int64` Optional. An int64 value.  
`string_value` |  `string` Optional. A string value.  
`account_id` |  `string` Optional. An account ID.  
`dict_value` |  `[DictValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.DictValue)` Optional. A dictionary value.  
`qualified_currency_value` |  `[QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.QualifiedCurrencyValue)` Optional. A qualified currency value.  
`amount_value` |  `[AmountValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.AmountValue)` Optional. An amount value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
