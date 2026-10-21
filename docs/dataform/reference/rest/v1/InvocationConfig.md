---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig/
title: InvocationConfig \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:40.422130+00:00
---

# InvocationConfig  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  InvocationConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EndUserAuthenticationConfig
    * JSON representation
  * QueryPriority



Includes various configuration options for a workflow invocation. If both `includedTargets` and `includedTags` are unset, all actions will be included.

JSON representation  
---  
      
    
    {
      "includedTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target))
        }
      ],
      "includedTags": [
        string
      ],
      "transitiveDependenciesIncluded": boolean,
      "transitiveDependentsIncluded": boolean,
      "fullyRefreshIncrementalTablesEnabled": boolean,
      "serviceAccount": string,
      "endUserAuthConfig": {
        object ([EndUserAuthenticationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig#EndUserAuthenticationConfig))
      },
      "queryPriority": enum ([QueryPriority](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig#QueryPriority))
    }  
  
Fields  
---  
`includedTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1/Target)`)` Optional. The set of action identifiers to include.  
`includedTags[]` |  `string` Optional. The set of tags to include.  
`transitiveDependenciesIncluded` |  `boolean` Optional. When set to true, transitive dependencies of included actions will be executed.  
`transitiveDependentsIncluded` |  `boolean` Optional. When set to true, transitive dependents of included actions will be executed.  
`fullyRefreshIncrementalTablesEnabled` |  `boolean` Optional. When set to true, any incremental tables will be fully refreshed.  
`serviceAccount` |  `string` Optional. The service account to run workflow invocations under.  
`endUserAuthConfig` |  `object (`[EndUserAuthenticationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig#EndUserAuthenticationConfig)`)` Optional. Configuration for end user authentication. Do not set if `serviceAccount` is used.  
`queryPriority` |  `enum (`[QueryPriority](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig#QueryPriority)`)` Optional. Specifies the priority for query execution in BigQuery. More information can be found at <https://cloud.google.com/bigquery/docs/running-queries#queries>.  
  
## EndUserAuthenticationConfig

Includes configuration options for end user authentication.

JSON representation  
---  
      
    
    {
      "userEmail": string,
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/OAuthConfig))
      }
    }  
  
Fields  
---  
`userEmail` |  `string` Output only. Email address of the user to run workflow invocations under.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/OAuthConfig)`)` Optional. OAuth configuration for end user authentication.  
  
## QueryPriority

Types of priority for query execution in BigQuery.

Enums  
---  
`QUERY_PRIORITY_UNSPECIFIED` | Default value. This value is unused.  
`INTERACTIVE` | Query will be executed in BigQuery with interactive priority. More information can be found at <https://cloud.google.com/bigquery/docs/running-queries#queries>.  
`BATCH` | Query will be executed in BigQuery with batch priority. More information can be found at <https://cloud.google.com/bigquery/docs/running-queries#batchqueries>.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
