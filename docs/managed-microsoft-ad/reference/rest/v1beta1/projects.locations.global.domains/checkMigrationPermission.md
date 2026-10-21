---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission/
title: Method: domains.checkMigrationPermission \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:12:25.891608+00:00
---

# Method: domains.checkMigrationPermission  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.checkMigrationPermission Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * State
  * OnPremDomainSIDDetails
    * JSON representation
  * SIDFilteringState
  * Try it!



**Full name** : projects.locations.global.domains.checkMigrationPermission

domains.checkMigrationPermission API gets the current state of DomainMigration

### HTTP request

`POST https://managedidentities.googleapis.com/v1beta1/{domain=projects/*/locations/global/domains/*}:checkMigrationPermission`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`domain` |  `string` Required. The domain resource name using the form: `projects/{projectId}/locations/global/domains/{domainName}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `domain`:

  * `managedidentities.domains.checkMigrationPermission`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

CheckMigrationPermissionResponse is the response message for domains.checkMigrationPermission method.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#State)),
      "onpremDomains": [
        {
          object ([OnPremDomainSIDDetails](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#OnPremDomainSIDDetails))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#State)`)` The state of DomainMigration.  
`onpremDomains[]` |  `object (`[OnPremDomainSIDDetails](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#OnPremDomainSIDDetails)`)` The state of SID filtering of all the domains which has trust established.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## State

State of DomainMigration Permissions.

Enums  
---  
`STATE_UNSPECIFIED` | DomainMigration is in unspecified state.  
`DISABLED` | Domain Migration is Disabled.  
`ENABLED` | Domain Migration is Enabled.  
`NEEDS_MAINTENANCE` | Domain Migration is not in valid state.  
  
## OnPremDomainSIDDetails

OnPremDomainDetails is the message which contains details of on-prem domain which is trusted and needs to be migrated.

JSON representation  
---  
      
    
    {
      "name": string,
      "sidFilteringState": enum ([SIDFilteringState](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#SIDFilteringState))
    }  
  
Fields  
---  
`name` |  `string` FQDN of the on-prem domain being migrated.  
`sidFilteringState` |  `enum (`[SIDFilteringState](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission#SIDFilteringState)`)` Current SID filtering state.  
  
## SIDFilteringState

State of SIDFiltering Permissions.

Enums  
---  
`SID_FILTERING_STATE_UNSPECIFIED` | SID Filtering is in unspecified state.  
`ENABLED` | SID Filtering is Enabled.  
`DISABLED` | SID Filtering is Disabled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
