---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction/
title: ClientTransaction \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:06.134601+00:00
---

# ClientTransaction  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  ClientTransaction Stay organized with collections  Save and categorize content based on your preferences. 

Represents a transaction initiated by a client.

JSON representation  
---  
      
    
    {
      "source": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "senderId": string,
      "signatories": [
        {
          object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
        }
      ],
      "otherSignatoryIds": [
        string
      ],
      "sequenceNumber": string,
      "chainedUnit": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "app": {
        "@type": string,
        field1: ...,
        ...
      },
      "operational": {
        "@type": string,
        field1: ...,
        ...
      },
      "transferPlatformOperatorTransaction": {
        object ([TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferPlatformOperator))
      },
      "createCurrencyOperatorTransaction": {
        object ([CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateCurrencyOperator))
      },
      "transferCurrencyOperatorTransaction": {
        object ([TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferCurrencyOperator))
      },
      "createClearinghouseTransaction": {
        object ([CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateClearinghouse))
      },
      "createAccountManagerTransaction": {
        object ([CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccountManager))
      },
      "createTokenManagerTransaction": {
        object ([CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateTokenManager))
      },
      "increaseTokenIssuanceLimitTransaction": {
        object ([IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#IncreaseTokenIssuanceLimit))
      },
      "decreaseTokenIssuanceLimitTransaction": {
        object ([DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DecreaseTokenIssuanceLimit))
      },
      "settlementRequestTransaction": {
        object ([SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest))
      },
      "mintTransaction": {
        object ([Mint](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Mint))
      },
      "burnTransaction": {
        object ([Burn](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn))
      },
      "createAccountTransaction": {
        object ([CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccount))
      },
      "deactivateAccountTransaction": {
        object ([DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DeactivateAccount))
      },
      "activateAccountTransaction": {
        object ([ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ActivateAccount))
      },
      "addRolesTransaction": {
        object ([AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles))
      },
      "removeRolesTransaction": {
        object ([RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveRoles))
      },
      "changeAccountManagerTransaction": {
        object ([ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager))
      },
      "transferTransaction": {
        object ([Transfer](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Transfer))
      },
      "createContractTransaction": {
        object ([CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContract))
      },
      "grantContractPermissionsTransaction": {
        object ([GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#GrantContractPermissions))
      },
      "invokeContractMethodTransaction": {
        object ([InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#InvokeContractMethod))
      },
      "createContractTokenManagerTransaction": {
        object ([CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContractTokenManager))
      },
      "transferContractTokenManagerTransaction": {
        object ([TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferContractTokenManager))
      },
      "removeSigningPublicKeyTransaction": {
        object ([RemoveSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveSigningPublicKey))
      },
      "replaceSigningPublicKeyTransaction": {
        object ([ReplaceSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#ReplaceSigningPublicKey))
      },
      "chain": {
        object ([TransactionChain](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransactionChain))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`source  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. The transaction sender. Deprecated: Use `[senderId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#FIELDS.sender_id)` instead.  
`senderId` |  `string` Optional. The ID of the account that is sending this transaction. One of `source` or `senderId` must be set.  
`signatories[]  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Accounts that, in addition to the sender, have signed this transaction. Deprecated: Use `[otherSignatoryIds](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#FIELDS.other_signatory_ids)` instead.  
`otherSignatoryIds[]` |  `string` Optional. The IDs of accounts that, in addition to the sender, have signed this transaction.  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. A unique, monotonically increasing number, starting from 0.This number must be increased by one for each transaction previously submitted to the network by the same transaction sender.Note this does not include any transaction units that may have been submitted as part of a chain, which must not set a sequence number. But it does include the sender of the transaction chain itself.  
`chainedUnit` |  `boolean` Must be set to true if this client transaction is part of a transaction chain. Otherwise, it must be set to false.This is necessary to prevent a signed transaction intended to be part of a chain from being submitted on its own.  
The client transaction-specific message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`app  
**(deprecated)**` |  `object` This item is deprecated!Optional. Deprecated: Use one of the message specific fields instead. A client transaction-specific message. Should be any one of:

  * `[TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferPlatformOperator)`
  * `[CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateCurrencyOperator)`
  * `[TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferCurrencyOperator)`
  * `[CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccountManager)`
  * `[CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateTokenManager)`
  * `[CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateClearinghouse)`
  * `[IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#IncreaseTokenIssuanceLimit)`
  * `[DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DecreaseTokenIssuanceLimit)`
  * `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest)`
  * `[Mint](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Mint)`
  * `[Burn](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn)`
  * `[CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccount)`
  * `[DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DeactivateAccount)`
  * `[ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ActivateAccount)`
  * `[AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles)`
  * `[RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveRoles)`
  * `[ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager)`
  * `[Transfer](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Transfer)`
  * `[CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContract)`
  * `[GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#GrantContractPermissions)`
  * `[InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#InvokeContractMethod)`
  * `[CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContractTokenManager)`
  * `[TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferContractTokenManager)`

An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`operational` |  `object` Optional. An operational transaction message. Note this can only be sent by the platform operator. Should be any one of:

  * `[CreateSnapshot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/CreateSnapshot)`

An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`transferPlatformOperatorTransaction` |  `object (`[TransferPlatformOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferPlatformOperator)`)` Optional. Message for transferring the platform operator role to a new account.  
`createCurrencyOperatorTransaction` |  `object (`[CreateCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateCurrencyOperator)`)` Optional. Message for creating a new currency operator.  
`transferCurrencyOperatorTransaction` |  `object (`[TransferCurrencyOperator](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferCurrencyOperator)`)` Optional. Message for transferring the currency operator role to a new account.  
`createClearinghouseTransaction` |  `object (`[CreateClearinghouse](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateClearinghouse)`)` Optional. Message for creating a new clearinghouse.  
`createAccountManagerTransaction` |  `object (`[CreateAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccountManager)`)` Optional. Message for creating a new account manager.  
`createTokenManagerTransaction` |  `object (`[CreateTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateTokenManager)`)` Optional. Message for creating a new token manager associated to the currency of the operator sending the request.  
`increaseTokenIssuanceLimitTransaction` |  `object (`[IncreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#IncreaseTokenIssuanceLimit)`)` Optional. Notifies the network that the target account has deposited reserve funds and increases its token issuance limit.  
`decreaseTokenIssuanceLimitTransaction` |  `object (`[DecreaseTokenIssuanceLimit](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DecreaseTokenIssuanceLimit)`)` Optional. Notifies the network that the target account wishes to withdraw reserve funds and decreases its token issuance limit.  
`settlementRequestTransaction` |  `object (`[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest)`)` Optional. Message for initiating a settlement operation.  
`mintTransaction` |  `object (`[Mint](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Mint)`)` Optional. Message for minting currency tokens and transferring them to an account.  
`burnTransaction` |  `object (`[Burn](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn)`)` Optional. Message for burning currency tokens from an account.  
`createAccountTransaction` |  `object (`[CreateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccount)`)` Optional. Message for creating a new user account.  
`deactivateAccountTransaction` |  `object (`[DeactivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DeactivateAccount)`)` Optional. Message for deactivating a user account.  
`activateAccountTransaction` |  `object (`[ActivateAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ActivateAccount)`)` Optional. Message for activating a user account.  
`addRolesTransaction` |  `object (`[AddRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles)`)` Optional. Message for adding roles to an account.  
`removeRolesTransaction` |  `object (`[RemoveRoles](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveRoles)`)` Optional. Message for removing roles from an account.  
`changeAccountManagerTransaction` |  `object (`[ChangeAccountManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager)`)` Optional. Message for changing the account manager of an account.  
`transferTransaction` |  `object (`[Transfer](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Transfer)`)` Optional. Message for transferring tokens from one user account to another.  
`createContractTransaction` |  `object (`[CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContract)`)` Optional. Message for creating a new contract on the ledger.  
`grantContractPermissionsTransaction` |  `object (`[GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#GrantContractPermissions)`)` Optional. Message for granting permissions to a contract.  
`invokeContractMethodTransaction` |  `object (`[InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#InvokeContractMethod)`)` Optional. Message for invoking the execution of a contract method.  
`createContractTokenManagerTransaction` |  `object (`[CreateContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContractTokenManager)`)` Optional. Message for creating a new token manager associated to the currency of the operator sending the request.  
`transferContractTokenManagerTransaction` |  `object (`[TransferContractTokenManager](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferContractTokenManager)`)` Optional. Message for transferring the token manager role for a currency from one account to another.  
`removeSigningPublicKeyTransaction` |  `object (`[RemoveSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveSigningPublicKey)`)` Optional. Message for removing an account signing key.  
`replaceSigningPublicKeyTransaction` |  `object (`[ReplaceSigningPublicKey](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#ReplaceSigningPublicKey)`)` Optional. Message for replacing an account signing key.  
`chain` |  `object (`[TransactionChain](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransactionChain)`)` Optional. Message for a transaction chain including multiple transaction units to execute in sequence.  
End of mutually exclusive fields.  
  
## TransferPlatformOperator

Transfers the ownership of the platform operator to a new account. The sender must be the current platform operator.

If the transaction is successful, deactivates the current platform operator, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "accountComment": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new platform operator. This public key will be associated with the platform operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the platform operator's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## CreateCurrencyOperator

Creates a new currency operator. The sender must be the platform operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

This transaction must introduce a new currency into the system. If the specified currency already exists, this transaction will fail. If the currency operator has to be replaced, the TransferCurrencyOperator transaction should be sent instead.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "accountComment": string,
      "currency": string,
      "currencyCode": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new currency operator. This public key will be associated with the currency operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the operator's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`currency  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Use `[currencyCode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateCurrencyOperator.FIELDS.currency_code)` instead. The fiat currency associated with this operator, represented as a 3-capital-letter ISO 4217 code. Considered public information.  
`currencyCode` |  `string` Optional. The fiat currency associated with this operator, represented as a 3-capital-letter ISO 4217 code. Considered public information.  
  
## TransferCurrencyOperator

Transfers the ownership of the given currency operator to a new account. The sender must be the platform operator.

If the transaction is successful, deactivates the given currency operator, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "accountComment": string,
      "currencyOperator": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "currencyOperatorId": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new currency operator. This public key will be associated with the currency operator and stored on the ledger. It will be used to validate the signature of the transactions emanating from the currency operator's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`currencyOperator  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[currencyOperatorId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#TransferCurrencyOperator.FIELDS.currency_operator_id)` instead. The currency operator to be replaced. Must be active.  
`currencyOperatorId` |  `string` Optional. The ID of the currency operator to be replaced. Must be active. One of `currencyOperator` or `currencyOperatorId` must be specified. The value is limited to 60 characters.  
  
## CreateClearinghouse

Creates a new clearinghouse. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "accountComment": string,
      "settlementMode": enum ([SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#SettlementMode))
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new clearinghouse. Note that this is _not_ the public key of the operator. This public key will be associated with the clearinghouse and stored on the ledger. It will be used to validate signature of the transactions emanating from the clearinghouse's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`settlementMode` |  `enum (`[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#SettlementMode)`)` Required. The settlement mode for this clearinghouse. Required. Considered public information.  
  
## CreateAccountManager

Creates a new account manager. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "defaultTokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "defaultTokenManagerId": string,
      "accountComment": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new account manager. Note that this is _not_ the public key of the operator. This public key will be associated with the account manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the account manager's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`defaultTokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[defaultTokenManagerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccountManager.FIELDS.default_token_manager_id)` instead. The default token manager for the accounts that will be created by this manager.  
`defaultTokenManagerId` |  `string` Optional. The ID of the default token manager for the accounts that will be created by this manager. The value is limited to 60 characters.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## CreateTokenManager

Creates a new token manager associated to the currency of the operator sending the request. The sender must be a currency operator.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "accountComment": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new token manager. Note that this is _not_ the public key of the operator. This public key will be associated with the token manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the token manager's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## IncreaseTokenIssuanceLimit

Transactions for token issuance and minting. Notifies the network that the target account has deposited reserve funds and increases its token issuance limit. The sender must be a clearinghouse account.

JSON representation  
---  
      
    
    {
      "tokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "tokenManagerId": string,
      "amount": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`tokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[tokenManagerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#IncreaseTokenIssuanceLimit.FIELDS.token_manager_id)` instead. The ID of the institutional account whose mint limit is to be raised. This account must be a token manager for the transaction to be valid.  
`tokenManagerId` |  `string` Optional. The ID of the institutional account whose mint limit is to be raised. This account must be a token manager for the transaction to be valid. One of `tokenManager` or `tokenManagerId` must be specified.  
`amount` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. The amount by which to raise the limit. The amount must be positive.  
  
## DecreaseTokenIssuanceLimit

Notifies the network that the target account wishes to withdraw reserve funds and decreases its token issuance limit. The sender must be a clearinghouse account.

Note that this transaction must be successfully finalized _before_ the reserve funds can be withdrawn. This is necessary because it is possible for the transaction to fail (for example, if the minted amount is already above the requested reduced limit).

JSON representation  
---  
      
    
    {
      "tokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "tokenManagerId": string,
      "amount": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`tokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[tokenManagerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DecreaseTokenIssuanceLimit.FIELDS.token_manager_id)` instead. The ID of the institutional account whose mint limit is to be lowered. This account must be a token manager for the transaction to be valid.  
`tokenManagerId` |  `string` Optional. The ID of the institutional account whose mint limit is to be lowered. This account must be a token manager for the transaction to be valid. One of `tokenManagerId` (preferred) or `tokenManager` (deprecated) must be specified.  
`amount` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. The amount by which to lower the limit. The amount must be positive. The transaction will fail if the reduced limit will fall below the currently issued tokens.  
  
## SettlementRequest

Initiates a settlement operation between two token managers. The sender must be a clearinghouse account.

In the deferred `[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#SettlementMode)` where the clearinghouse has custody of the token manager funds, this is the only transaction that needs to be sent to execute a settlement between the two token managers.

JSON representation  
---  
      
    
    {
      "payer": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "payerId": string,
      "beneficiary": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "beneficiaryId": string,
      "balance": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "roundId": string
    }  
  
Fields  
---  
`payer  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Immutable. Deprecated: Use `[payerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest.FIELDS.payer_id)` instead. The account ID of the party that needs to make the fund transfer.  
`payerId` |  `string` Optional. Immutable. The account ID of the party that needs to make the fund transfer. One of `payer` or `payerId` must be specified.  
`beneficiary  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Immutable. Deprecated: Use `[beneficiaryId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest.FIELDS.beneficiary_id)` instead. The account ID of the party that needs to be paid.  
`beneficiaryId` |  `string` Optional. Immutable. The account ID of the party that will receive the funds. One of `beneficiary` or `beneficiaryId` must be specified.  
`balance` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. Immutable. The balance of issued tokens that need to be transferred by the `payer` account to the `beneficiary` account on the ledger.  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Immutable. The round ID at which this settlement amount was computed.  
  
## Mint

Mints currency tokens and transfers them to a specified account. The sender must be a token manager.

JSON representation  
---  
      
    
    {
      "mintAmount": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "beneficiary": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "beneficiaryId": string
    }  
  
Fields  
---  
`mintAmount` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. The amount to mint. The amount must be such that the total tokens minted by the token manager do not exceed the mint limit. If the amount is higher than that, the transaction must be rejected  
`beneficiary  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[beneficiaryId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Mint.FIELDS.beneficiary_id)` instead. The account to which the minted amount should be transferred. The beneficiary account must have the `ROLE_RECEIVER` enabled on it.  
`beneficiaryId` |  `string` Optional. The ID of the account to which the minted amount should be transferred. The receiving account must have the `ROLE_RECEIVER` enabled on it. One of `beneficiary` or `beneficiaryId` must be specified.  
  
## CreateAccount

Creates a new user account. The sender must be an account manager.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)),
      "roles": [
        enum ([Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role))
      ],
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)),
      "accountComment": string,
      "tokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "tokenManagerId": string
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the account owner. Note that this is _not_ the public key of the sender. This is the public key of the _new_ account owner and it will be stored on the ledger. It will be used to validate the signature of the transactions emanating from the created account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
`roles[]` |  `enum (`[Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role)`)` Optional. The list of roles to grant to this account.  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Optional. The status of the account to be created. By default, the account status of a newly created account will be `ACCOUNT_STATUS_ACTIVE`.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`tokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[tokenManagerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateAccount.FIELDS.token_manager_id)` instead. The token manager for this account. This field is optional and if not supplied, the default token manager associated to the account manager (that is, the sender of this transaction) will be used.  
`tokenManagerId` |  `string` Optional. The ID of the token manager for this account. This field is optional and if not supplied, the default token manager associated to the account manager (that is, the sender of this transaction) will be used. The value is limited to 60 characters.  
  
## DeactivateAccount

Marks an account as `ACCOUNT_STATUS_INACTIVE`. The sender must be the account manager of the account to deactivate.

This implies that the account owner will not be able to make any transactions on the account regardless of the roles.

JSON representation  
---  
      
    
    {
      "account": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "accountId": string
    }  
  
Fields  
---  
`account  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[accountId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#DeactivateAccount.FIELDS.account_id)` instead. The ID of the account to be deactivated.  
`accountId` |  `string` Optional. The ID of the account to be deactivated. One of `account` or `accountId` must be specified. The value is limited to 60 characters.  
  
## RemoveRoles

Removes the specified roles from the account. The sender must be the account manager of the account to modify.

JSON representation  
---  
      
    
    {
      "account": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "accountId": string,
      "roles": [
        enum ([Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role))
      ]
    }  
  
Fields  
---  
`account  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[accountId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#RemoveRoles.FIELDS.account_id)` instead. The ID of the account to be modified.  
`accountId` |  `string` Optional. The ID of the account to be modified. One of `account` or `accountId` must be specified. The value is limited to 60 characters.  
`roles[]` |  `enum (`[Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role)`)` Required. The roles to be removed.  
  
## Transfer

Transfers tokens from one user account to another. The sender must be a regular user account, as opposed to a privileged account like a token manager or an account manager.

Additionally, the transaction sender must have the `ROLE_PAYER` enabled on it, while the receiver must have the `ROLE_RECEIVER` enabled on it.

JSON representation  
---  
      
    
    {
      "beneficiary": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "beneficiaryId": string,
      "amount": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`beneficiary  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[beneficiaryId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#Transfer.FIELDS.beneficiary_id)` instead. The account that receives the tokens.  
`beneficiaryId` |  `string` Optional. The ID of the account that receives the tokens. One of `beneficiary` or `beneficiaryId` must be specified.  
`amount` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. The amount to transfer. The amount must be positive.  
  
## CreateContract

Stores a contract on the ledger.

JSON representation  
---  
      
    
    {
      "contractBytes": string,
      "arguments": {
        string: {
          object ([Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value))
        },
        ...
      },
      "initArguments": {
        string: {
          object ([Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value))
        },
        ...
      },
      "contractComment": string
    }  
  
Fields  
---  
`contractBytes` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Serialised contract bytes.A base64-encoded string.  
`arguments  
**(deprecated)**` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value)`))` This item is deprecated!Optional. Immutable. Deprecated: Use `[initArguments](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#CreateContract.FIELDS.init_arguments)` instead. Arguments for the `__init__` method.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`initArguments` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value)`))` Optional. Immutable. Contains arguments for the `__init__` method.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`contractComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the contract. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
  
## GrantContractPermissions

Grants permissions to the contract by the transaction sender. If `delegateContractId` is specified, the permissions and corresponding storage are granted exclusively to the `delegateContractId` contract, not the sender.

Note that there is no support for revoking permissions.

JSON representation  
---  
      
    
    {
      "contract": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "contractId": string,
      "permissions": [
        enum ([ContractPermission](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ContractPermission))
      ],
      "delegateContractId": string
    }  
  
Fields  
---  
`contract  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[contractId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#GrantContractPermissions.FIELDS.contract_id)` instead. ID of the contract to which permissions are being granted.  
`contractId` |  `string` Optional. The ID of the contract to which permissions are being granted. One of `contract` or `contractId` must be specified.  
`permissions[]` |  `enum (`[ContractPermission](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ContractPermission)`)` The permissions to be granted.  
`delegateContractId` |  `string` Optional. The contract ID for which permissions are being granted. The transaction sender must be the owner of this contract.  
  
## InvokeContractMethod

Invokes the execution of a contract method.

JSON representation  
---  
      
    
    {
      "contract": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "contractId": string,
      "methodName": string,
      "arguments": {
        string: {
          object ([Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value))
        },
        ...
      },
      "methodArguments": {
        string: {
          object ([Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value))
        },
        ...
      },
      "payment": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`contract  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[contractId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#InvokeContractMethod.FIELDS.contract_id)` instead. ID of the contract to run.  
`contractId` |  `string` Optional. The ID of the contract to run. One of `contract` or `contractId` must be specified.  
`methodName` |  `string` Name of the method to run.  
`arguments  
**(deprecated)**` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value)`))` This item is deprecated!Optional. Immutable. Deprecated: Use `[methodArguments](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#InvokeContractMethod.FIELDS.method_arguments)` instead. Arguments for the method.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`methodArguments` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value)`))` Optional. Immutable. Contains arguments to pass to the method.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`payment` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` The amount to be paid. Must be greater than zero when invoking payable methods; and zero for non-payable ones.  
  
## CreateContractTokenManager

Creates a new contract token manager associated with the currency of the operator sending the request. The sender must be a currency operator. The newly created contract token manager is active by default. If the contract token manager has to be replaced, the TransferContractTokenManager transaction should be sent instead. If another contract token manager associated with the same currency exists, this transaction will fail.

Unlike regular token managers, contract token managers are not allowed to execute transactions such as mint or burn. They can, however, participate in settlement operations.

If the transaction is successful, the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "accountComment": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat))
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new contract token manager. Note that this is _not_ the public key of the operator. This public key will be associated with the contract token manager and stored on the ledger. It will be used to validate the signature of the transactions emanating from the contract token manager's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
  
## TransferContractTokenManager

Transfers the ownership of the contract token manager to a new account. The sender must be the current currency operator for the currency.

If the transaction is successful, deactivates the current contract token manager for the currency, and the ID of the newly created account is returned as an event in the `[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)` of the finalized transaction.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "accountComment": string,
      "keyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat))
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key of the new contract token manager. Note that this is _not_ the public key of the operator. This is the public key of the _new_ contract token manager and it will be stored on the ledger. It will be used to validate the signature of the transactions emanating from the contract token manager's account.The format of the public key is defined by the `keyFormat` field. Considered public information.A base64-encoded string.  
`accountComment` |  `string` Optional. Immutable. An opaque comment field that is not interpreted by the system but stored on the ledger in the account. Considered public information. Maximum length is 128 characters. May be left empty. Once created, the field is immutable.  
`keyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Optional. Immutable. The key format of the public key. If not specified, defaults to a binary serialized keyset in [Tink wire format](https://developers.google.com/tink/wire-format#keyset_serialization). Considered public information.  
  
## RemoveSigningPublicKey

Removes the account signing key from the specified slot. The other slot must not be empty, and must hold the key used to sign the `ClientTransaction`.

JSON representation  
---  
      
    
    {
      "keySlot": enum ([KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot))
    }  
  
Fields  
---  
`keySlot` |  `enum (`[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)`)` Required. The key slot we're removing the key from. If this is already empty, the transaction will fail.  
  
## ReplaceSigningPublicKey

Replaces the account signing key in the specified slot. The other slot must not be empty, and must hold the key used to sign the `ClientTransaction`.

JSON representation  
---  
      
    
    {
      "keySlot": enum ([KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)),
      "newPublicKey": string,
      "newKeyFormat": enum ([KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat))
    }  
  
Fields  
---  
`keySlot` |  `enum (`[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)`)` Required. The key slot we're replacing the key in.  
`newPublicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The new public key, which will replace the public key in the specified slot.The format of the public key is defined by the newKeyFormat field. Considered public information.A base64-encoded string.  
`newKeyFormat` |  `enum (`[KeyFormat](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeyFormat)`)` Required. The key format of the new public key. See the definition of KeyFormat for a list of supported formats. Considered public information.  
  
## TransactionChain

A transaction chain including multiple transaction units to execute in sequence.

The units will be executed sequentially, in the order they are listed. If all of the units succeed, their cumulative effects will be committed atomically to the world state. Otherwise, if any of them fails, the whole chain will be failed and none of its effects will be applied.

JSON representation  
---  
      
    
    {
      "units": [
        string
      ]
    }  
  
Fields  
---  
`units[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The individual units of the chain. Each unit must be a serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction)`.Note that the serialized bytes are required in order to determine the bytes to be signed for the chain itself.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
