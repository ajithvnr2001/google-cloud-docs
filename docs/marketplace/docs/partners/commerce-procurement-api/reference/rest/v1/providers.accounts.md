---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts
title: REST Resource: providers.accounts \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:09.133601+00:00
---

# REST Resource: providers.accounts  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: providers.accounts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Account
    * JSON representation
  * AccountState
  * Approval
    * JSON representation
  * State
  * Methods



## Resource: Account

Represents an account that was established by the customer on the service provider's system.

JSON representation  
---  
      
    
    {
      "name": string,
      "updateTime": string,
      "createTime": string,
      "provider": string,
      "state": enum ([AccountState](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#AccountState)),
      "inputProperties": {
        object
      },
      "approvals": [
        {
          object ([Approval](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Approval))
        }
      ],
      "resellerParentBillingAccount": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the account. Account names have the form `accounts/{account_id}`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`provider` |  `string` Output only. The identifier of the service provider that this account was created against. Each service provider is assigned a unique provider value when they onboard with Cloud Commerce platform.  
`state` |  `enum (`[AccountState](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#AccountState)`)` Output only. The state of the account. This is used to decide whether the customer is in good standing with the provider and is able to make purchases. An account might not be able to make a purchase if the billing account is suspended, for example.  
`inputProperties  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Output only. The custom properties that were collected from the user to create this account.  
`approvals[]` |  `object (`[Approval](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Approval)`)` Output only. The approvals for this account. These approvals are used to track actions that are permitted or have been completed by a customer within the context of the provider. This might include a sign up flow or a provisioning step, for example, that the provider can admit to having happened.  
`resellerParentBillingAccount` |  `string` Output only. The reseller parent billing account of the account's corresponding billing account, applicable only when the corresponding billing account is a subaccount of a reseller.Included in responses only for view: ACCOUNT_VIEW_FULL.Format: billingAccounts/{billing_account_id}  
  
## AccountState

AccountState indicates the current status of the account.

Enums  
---  
`ACCOUNT_STATE_UNSPECIFIED` | Default state of the account. It's only set to this value when the account is first created and has not been initialized.  
`ACCOUNT_ACTIVATION_REQUESTED` | The customer has requested the creation of the account resource, and the provider notification message is dispatched.This state has been deprecated, as accounts now immediately transition to `[AccountState.ACCOUNT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#AccountState.ENUM_VALUES.ACCOUNT_ACTIVE)`.  
`ACCOUNT_ACTIVE` | The account is active and ready for use.The next possible states are: - Account getting deleted: After the user invokes delete from another API.  
  
## Approval

An approval for some action on an account.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#State)),
      "reason": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the approval.  
`state` |  `enum (`[State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#State)`)` Output only. The state of the approval.  
`reason` |  `string` Output only. An explanation for the state of the approval.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The last update timestamp of the approval.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The current status of an approval.

Enums  
---  
`STATE_UNSPECIFIED` | Sentinel value; do not use.  
`PENDING` | The approval is pending response from the provider.The approval state can transition to `[Account.Approval.State.APPROVED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#State.ENUM_VALUES.APPROVED)` or `[Account.Approval.State.REJECTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#State.ENUM_VALUES.REJECTED)`.  
`APPROVED` | The approval has been granted by the provider.  
`REJECTED` | The approval has been rejected by the provider.A provider may choose to approve a previously rejected approval, so is it possible to transition to `[Account.Approval.State.APPROVED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#State.ENUM_VALUES.APPROVED)`.  
  
## Methods  
  
---  
  
### `[approve](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/approve)`

|  Grants an approval on an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`.  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/get)`

|  Gets a requested `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)` resource.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/list)`

|  Lists `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`s that the provider has access to.  
  
### `[reject](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/reject)`

|  Rejects an approval on an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`.  
  
### `[reset](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/reset)`

|  Resets an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)` and cancels all associated `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`s.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-18 UTC."],[],[]] 
