---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements
title: REST Resource: projects.locations.entitlements \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:44.977834+00:00
---

# REST Resource: projects.locations.entitlements  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.entitlements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Entitlement
    * JSON representation
  * CloudAccountDetails
    * JSON representation
  * State
  * Methods



## Resource: Entitlement

Details of the Entitlement resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "cloudAccountDetails": {
        object ([CloudAccountDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements#CloudAccountDetails))
      },
      "entitlementId": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Entitlement resource with the format: projects/{project}/locations/{region}/entitlements/{entitlement}  
`cloudAccountDetails` |  `object (`[CloudAccountDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements#CloudAccountDetails)`)` Details of the OCI Cloud Account.  
`entitlementId` |  `string` Output only. Google Cloud Marketplace order ID (aka entitlement ID)  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements#State)`)` Output only. Entitlement State.  
  
## CloudAccountDetails

Details of the OCI Cloud Account.

JSON representation  
---  
      
    
    {
      "cloudAccount": string,
      "cloudAccountHomeRegion": string,
      "linkExistingAccountUri": string,
      "accountCreationUri": string
    }  
  
Fields  
---  
`cloudAccount` |  `string` Output only. OCI account name.  
`cloudAccountHomeRegion` |  `string` Output only. OCI account home region.  
`linkExistingAccountUri` |  `string` Output only. URL to link an existing account.  
`accountCreationUri` |  `string` Output only. URL to create a new account and link.  
  
## State

The various lifecycle states of the subscription.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`ACCOUNT_NOT_LINKED` | Account not linked.  
`ACCOUNT_NOT_ACTIVE` | Account is linked but not active.  
`ACTIVE` | Entitlement and Account are active.  
`ACCOUNT_SUSPENDED` | Account is suspended.  
`NOT_APPROVED_IN_PRIVATE_MARKETPLACE` | Entitlement is not approved in private marketplace.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements/list)`

|  Lists the entitlements in a given project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
