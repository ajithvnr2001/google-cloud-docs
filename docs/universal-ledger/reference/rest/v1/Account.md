---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account/
title: Account \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:35:11.852580+00:00
---

# Account  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Account Stay organized with collections  Save and categorize content based on your preferences. 

Represents the state of an account on the ledger.

JSON representation  
---  
      
    
    {
      "sequenceNumber": string,
      "publicKey": string,
      "roundId": string,
      "comment": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userDetails": {
        object ([UserDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#UserDetails))
      },
      "accountManagerDetails": {
        object ([AccountManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountManagerDetails))
      },
      "tokenManagerDetails": {
        object ([TokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#TokenManagerDetails))
      },
      "contractTokenManagerDetails": {
        object ([ContractTokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ContractTokenManagerDetails))
      },
      "contractDetails": {
        object ([ContractDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ContractDetails))
      },
      "clearinghouseDetails": {
        object ([ClearingHouseDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ClearingHouseDetails))
      },
      "currencyOperatorDetails": {
        object ([CurrencyOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyOperatorDetails))
      },
      "platformOperatorDetails": {
        object ([PlatformOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#PlatformOperatorDetails))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The sequence number of this account. This number increments with each transaction sent by this account.  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The primary public key associated with this account, used for signature verification.A base64-encoded string.  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The ID of the execution round (similar to block "height") at which the account information provided is accurate.  
`comment` |  `string` Output only. The account comment stored when this account was created.  
Specific details based on the type of account. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userDetails` |  `object (`[UserDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#UserDetails)`)` Output only. Details for a standard user account.  
`accountManagerDetails` |  `object (`[AccountManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountManagerDetails)`)` Output only. Details for an account manager account.  
`tokenManagerDetails` |  `object (`[TokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#TokenManagerDetails)`)` Output only. Details for a token manager account.  
`contractTokenManagerDetails` |  `object (`[ContractTokenManagerDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ContractTokenManagerDetails)`)` Output only. Details for a contract token manager account.  
`contractDetails` |  `object (`[ContractDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ContractDetails)`)` Output only. Details for a smart contract account.  
`clearinghouseDetails` |  `object (`[ClearingHouseDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#ClearingHouseDetails)`)` Output only. Details for a clearinghouse account.  
`currencyOperatorDetails` |  `object (`[CurrencyOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyOperatorDetails)`)` Output only. Details for a currency operator account.  
`platformOperatorDetails` |  `object (`[PlatformOperatorDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#PlatformOperatorDetails)`)` Output only. Details for a platform operator account.  
End of mutually exclusive fields.  
  
## UserDetails

Details specific to a User account.

JSON representation  
---  
      
    
    {
      "accountManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "accountManagerId": string,
      "tokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "tokenManagerId": string,
      "roles": [
        enum ([Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role))
      ],
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)),
      "balance": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "accountFields": {
        string: {
          object ([Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields))
        },
        ...
      },
      "contractAccountFields": {
        string: {
          object ([Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields))
        },
        ...
      }
    }  
  
Fields  
---  
`accountManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `accountManagerId` instead. The account manager for this user.  
`accountManagerId` |  `string` Output only. The ID of the account manager for this user.  
`tokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `tokenManagerId` instead. The token manager for this user.  
`tokenManagerId` |  `string` Output only. The ID of the token manager for this user.  
`roles[]` |  `enum (`[Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role)`)` Output only. The list of roles granted to this account.  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Output only. The status of this account.  
`balance` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The token balance of this user account.  
`accountFields  
**(deprecated)**` |  `map (key: string, value: object (`[Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields)`))` This item is deprecated!Output only. Deprecated: Use `contractAccountFields` instead. The contract account fields (contract ID -> fields) for this user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`contractAccountFields` |  `map (key: string, value: object (`[Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields)`))` Output only. The contract account fields (contract ID -> fields) for this user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Entity

An entity in the Universal Ledger network. All accounts are attached to an entity. The entity ID, also often referred to as the account ID, is unique and immutable across the network.

JSON representation  
---  
      
    
    {
      "id": string
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID assigned to the entity. This is assigned by the network on account creation.  
  
## Role

The regular set of roles.

Enums  
---  
`ROLE_UNSPECIFIED` | Invalid role.  
`ROLE_PAYER` | The role that allows an account to initiate a payment transaction.  
`ROLE_RECEIVER` | The role that allows an account to receive payments.  
`ROLE_CONTRACT_CREATOR` | The role that allows an account to deploy contracts.  
`ROLE_CONTRACT_PARTICIPANT` | The role that allows an account to interact with deployed contracts.  
  
## AccountStatus

The status of an account.

Enums  
---  
`ACCOUNT_STATUS_UNSPECIFIED` | Invalid status.  
`ACCOUNT_STATUS_ACTIVE` | Active state where the account can conduct the operations allowed by its roles.  
`ACCOUNT_STATUS_INACTIVE` | Inactive state where all transactions on the account are forbidden. The manager of the account can still send account management transactions.  
  
## CurrencyValue

Represents an amount of currency (i.e. money). Note that the denominated currency is not included in this message. The relevant currency is decided by the account that sends the transaction. Each account has a unique immutable currency associated to it.

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The number of minor units of the currency.This smallest valid denomination is referred to as "minor units" and is specified in [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). As an example, for USD, the value will be the number of cents and for GBP it will be the number of pence. For the Japanese Yen which does not have a minor unit, it will be the number of Yen.  
  
## Fields

A map of fields (field name -> value) from a contract used to represent contract fields or account fields.

JSON representation  
---  
      
    
    {
      "fields": {
        string: {
          object ([Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value))
        },
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Value)`))` Output only. The map of field names to their values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Value

A concrete value of some type.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "noneValue": enum ([NoneValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#NoneValue)),
      "boolValue": boolean,
      "int64Value": string,
      "stringValue": string,
      "accountId": string,
      "dictValue": {
        object ([DictValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictValue))
      },
      "qualifiedCurrencyValue": {
        object ([QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#QualifiedCurrencyValue))
      },
      "amountValue": {
        object ([AmountValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AmountValue))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The actual value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`noneValue` |  `enum (`[NoneValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#NoneValue)`)` Optional. Represents a None value.  
`boolValue` |  `boolean` Optional. A boolean value.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. An int64 value.  
`stringValue` |  `string` Optional. A string value.  
`accountId` |  `string` Optional. An account ID.  
`dictValue` |  `object (`[DictValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictValue)`)` Optional. A dictionary value.  
`qualifiedCurrencyValue` |  `object (`[QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#QualifiedCurrencyValue)`)` Optional. A qualified currency value.  
`amountValue` |  `object (`[AmountValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AmountValue)`)` Optional. An amount value.  
End of mutually exclusive fields.  
  
## NoneValue

A singleton enumeration to represent the None value.

Enums  
---  
`NONE_VALUE_UNSPECIFIED` | The None value.  
  
## DictValue

Indices map key to value. For example, `keys[0]` key maps to `values[0]`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "boolKeys": {
        object ([BoolList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BoolList))
      },
      "stringKeys": {
        object ([StringList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#StringList))
      },
      "int64Keys": {
        object ([Int64List](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Int64List))
      },
      "accountIdKeys": {
        object ([AccountIdList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountIdList))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "boolValues": {
        object ([BoolList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BoolList))
      },
      "stringValues": {
        object ([StringList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#StringList))
      },
      "int64Values": {
        object ([Int64List](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Int64List))
      },
      "dictValues": {
        object ([DictList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictList))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Each key can be exactly one kind. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`boolKeys` |  `object (`[BoolList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BoolList)`)` Optional. A list of boolean keys.  
`stringKeys` |  `object (`[StringList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#StringList)`)` Optional. A list of string keys.  
`int64Keys` |  `object (`[Int64List](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Int64List)`)` Optional. A list of int64 keys.  
`accountIdKeys` |  `object (`[AccountIdList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountIdList)`)` Optional. A list of account ID keys.  
End of mutually exclusive fields.  
Each value can be exactly one kind. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`boolValues` |  `object (`[BoolList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BoolList)`)` Optional. A list of boolean values.  
`stringValues` |  `object (`[StringList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#StringList)`)` Optional. A list of string values.  
`int64Values` |  `object (`[Int64List](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Int64List)`)` Optional. A list of int64 values.  
`dictValues` |  `object (`[DictList](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictList)`)` Optional. Values are a list of nested dictionaries.  
End of mutually exclusive fields.  
  
## BoolList

A list of booleans.

JSON representation  
---  
      
    
    {
      "values": [
        boolean
      ]
    }  
  
Fields  
---  
`values[]` |  `boolean` Optional. The boolean values.  
  
## StringList

A list of strings.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Optional. The string values.  
  
## Int64List

A list of int64s.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The int64 values.  
  
## AccountIdList

A list of account IDs.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Optional. The account ID values.  
  
## DictList

A list of dictionaries.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([DictValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictValue))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[DictValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#DictValue)`)` Optional. The DictValue values. All nested dicts must have the same concrete type.  
  
## QualifiedCurrencyValue

Represents a currency on the ledger, which is qualified by its Currency Operator.

JSON representation  
---  
      
    
    {
      "operatorId": string
    }  
  
Fields  
---  
`operatorId` |  `string` Required. The Currency Operator ID administering the currency.  
  
## AmountValue

Represents a denominated amount in a currency.

JSON representation  
---  
      
    
    {
      "currency": {
        object ([QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#QualifiedCurrencyValue))
      },
      "amountValue": string
    }  
  
Fields  
---  
`currency` |  `object (`[QualifiedCurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#QualifiedCurrencyValue)`)` Required. The currency of the amount.  
`amountValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The number of minor units of the currency.  
  
## AccountManagerDetails

Details specific to an Account Manager.

JSON representation  
---  
      
    
    {
      "tokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "numAccounts": integer,
      "tokenManagerId": string
    }  
  
Fields  
---  
`tokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `tokenManagerId` instead. The default token manager for accounts created by this account manager.  
`numAccounts` |  `integer` Output only. The number of accounts created by this account manager.  
`tokenManagerId` |  `string` Output only. The ID of the default token manager for accounts created by this account manager.  
  
## TokenManagerDetails

Details specific to a Token Manager.

JSON representation  
---  
      
    
    {
      "issuanceLimit": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "issuedTokens": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`issuanceLimit` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The amount of tokens this token manager is allowed to mint.  
`issuedTokens` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The amount of tokens minted by this token manager. This number will increase when minting and decrease when burning.  
  
## ContractTokenManagerDetails

Details specific to a Contract Token Manager.

JSON representation  
---  
      
    
    {
      "issuanceLimit": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "issuedTokens": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "previousContractTokenManagerId": string,
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus))
    }  
  
Fields  
---  
`issuanceLimit` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The amount of tokens this contract token manager is allowed to provide backing for.Since contract token managers cannot increase or decrease their issuance limit, this should equal the `issuedTokens`.  
`issuedTokens` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The amount of tokens this contract token manager is providing backing for (that is, its total liability).This equals to the sum of all balances held in contracts for its currency, plus its net position in the settlement matrix.  
`previousContractTokenManagerId` |  `string` Output only. The account ID of the previous contract token manager for this currency. This forms an audit trail that can be traversed to discover all previous managers. If this is the first contract token manager for the currency, this will be empty.  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Output only. The status of this account.  
  
## ContractDetails

Details specific to a Smart Contract.

JSON representation  
---  
      
    
    {
      "owner": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "ownerId": string,
      "code": string,
      "contractFields": {
        object ([Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields))
      },
      "currencyBalances": {
        string: {
          object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
        },
        ...
      }
    }  
  
Fields  
---  
`owner  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `ownerId` instead. The owner of the contract.  
`ownerId` |  `string` Output only. The ID of the owner of the contract.  
`code` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The serialized contract code.A base64-encoded string.  
`contractFields` |  `object (`[Fields](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Fields)`)` Output only. The contract fields (field name -> value) for this contract.  
`currencyBalances` |  `map (key: string, value: object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`))` Output only. The currency balances held by the contract (currency operator -> balance).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ClearingHouseDetails

Details specific to a Clearinghouse.

JSON representation  
---  
      
    
    {
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)),
      "balances": [
        {
          object ([BalanceToSettle](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BalanceToSettle))
        }
      ],
      "settlementMode": enum ([SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#SettlementMode))
    }  
  
Fields  
---  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Output only. The status of this account.  
`balances[]` |  `object (`[BalanceToSettle](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#BalanceToSettle)`)` Output only. The balances that this clearinghouse is currently tracking for settlement.  
`settlementMode` |  `enum (`[SettlementMode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#SettlementMode)`)` Output only. The settlement mode of this clearinghouse.  
  
## BalanceToSettle

A balance to settle between two token managers.

JSON representation  
---  
      
    
    {
      "balancePayer": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "balancePayerId": string,
      "balanceReceiver": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "balanceReceiverId": string,
      "balance": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      }
    }  
  
Fields  
---  
`balancePayer  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `balancePayerId` instead. The account which owes the balance to be settled.  
`balancePayerId` |  `string` Output only. The ID of the account which owes the balance to be settled.  
`balanceReceiver  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `balanceReceiverId` instead. The account which is owed the balance to be settled.  
`balanceReceiverId` |  `string` Output only. The ID of the account which is owed the balance to be settled.  
`balance` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Output only. The balance to settle. Must be positive.  
  
## SettlementMode

The settlement mode for a clearinghouse.

Enums  
---  
`SETTLEMENT_MODE_UNSPECIFIED` | The settlement mode is unspecified. This value is invalid and should not be used.  
`SETTLEMENT_MODE_DEFERRED` | The clearinghouse is responsible for tracking the ownership of the off-ledger funds, and periodically issuing `[SettlementRequest](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction#SettlementRequest)` transactions to maintain the corresponding balances on the ledger in sync.  
`SETTLEMENT_MODE_INSTANT` | The clearinghouse maintains a single pool of funds and the ledger acts as the golden source for the allocation of those funds between the token managers. This settlement mode can also be described as "instant gross settlement."  
  
## CurrencyOperatorDetails

Details specific to a Currency Operator.

JSON representation  
---  
      
    
    {
      "currency": string,
      "currencyCode": string,
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)),
      "previousEntityId": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "previousCurrencyOperatorId": string,
      "platformOperatorEntityId": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "platformOperatorId": string,
      "contractTokenManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "contractTokenManagerId": string,
      "clearinghouseId": string
    }  
  
Fields  
---  
`currency  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated: Use `currencyCode` instead. The currency associated with this account, represented by the 3-letter ISO 4217 code.  
`currencyCode` |  `string` Output only. The ID of the currency associated with this account, represented by the 3-letter ISO 4217 code.  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Output only. The status of this account.  
`previousEntityId  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `previousCurrencyOperatorId` instead. The previous currency operator which transferred ownership of the currency operator role to this account. If this is the first currency operator for the currency, this will be empty.  
`previousCurrencyOperatorId` |  `string` Output only. The ID of the previous currency operator which transferred ownership of the currency operator role to this account. If this is the first currency operator for the currency, this will be empty.  
`platformOperatorEntityId  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `platformOperatorId` instead. The platform operator which created this currency operator.  
`platformOperatorId` |  `string` Output only. The ID of the platform operator which created this currency operator.  
`contractTokenManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `contractTokenManagerId` instead. The contract token manager associated with this currency operator.  
`contractTokenManagerId` |  `string` Output only. The ID of the contract token manager associated with this currency operator.  
`clearinghouseId` |  `string` Output only. The ID of the clearinghouse associated with this currency operator.  
  
## PlatformOperatorDetails

Details specific to a Platform Operator.

JSON representation  
---  
      
    
    {
      "accountStatus": enum ([AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)),
      "previousEntityId": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "previousPlatformOperatorId": string
    }  
  
Fields  
---  
`accountStatus` |  `enum (`[AccountStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#AccountStatus)`)` Output only. The status of this account.  
`previousEntityId  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Output only. Deprecated: Use `previousPlatformOperatorId` instead. The previous platform operator which transferred ownership of the platform operator role to this account. If this is the first platform operator, this will be empty.  
`previousPlatformOperatorId` |  `string` Output only. The ID of the previous platform operator which transferred ownership of the platform operator role to this account. If this is the first platform operator, this will be empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
