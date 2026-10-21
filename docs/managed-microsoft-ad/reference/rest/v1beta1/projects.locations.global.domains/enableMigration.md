---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/enableMigration/
title: Method: domains.enableMigration \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:20.343613+00:00
---

# Method: domains.enableMigration  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/enableMigration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: domains.enableMigration Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * OnPremDomainDetails
    * JSON representation
  * Try it!



**Full name** : projects.locations.global.domains.enableMigration

Enable Domain Migration

### HTTP request

`POST https://managedidentities.googleapis.com/v1beta1/{domain=projects/*/locations/global/domains/*}:enableMigration`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`domain` |  `string` Required. The domain resource name using the form: `projects/{projectId}/locations/global/domains/{domainName}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `domain`:

  * `managedidentities.domains.enableMigration`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "migratingDomains": [
        {
          object ([OnPremDomainDetails](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/enableMigration#OnPremDomainDetails))
        }
      ]
    }  
  
Fields  
---  
`migratingDomains[]` |  `object (`[OnPremDomainDetails](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/enableMigration#OnPremDomainDetails)`)` Required. List of the on-prem domains to be migrated.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## OnPremDomainDetails

OnPremDomainDetails is the message which contains details of on-prem domain which is trusted and needs to be migrated.

JSON representation  
---  
      
    
    {
      "domainName": string,
      "disableSidFiltering": boolean
    }  
  
Fields  
---  
`domainName` |  `string` Required. FQDN of the on-prem domain being migrated.  
`disableSidFiltering` |  `boolean` Optional. Option to disable SID filtering.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
