---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/QueryOptions/
title: QueryOptions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:20.673018+00:00
---

# QueryOptions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/QueryOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  QueryOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Query optimizer configuration.

JSON representation  
---  
      
    
    {
      "optimizerVersion": string,
      "optimizerStatisticsPackage": string
    }  
  
Fields  
---  
`optimizerVersion` |  `string` An option to control the selection of optimizer version.This parameter allows individual queries to pick different query optimizer versions.Specifying `latest` as a value instructs Cloud Spanner to use the latest supported query optimizer version. If not specified, Cloud Spanner uses the optimizer version set at the database level options. Any other positive integer (from the list of supported optimizer versions) overrides the default optimizer version for query execution.The list of supported optimizer versions can be queried from `SPANNER_SYS.SUPPORTED_OPTIMIZER_VERSIONS`.Executing a SQL statement with an invalid optimizer version fails with an `INVALID_ARGUMENT` error.See <https://cloud.google.com/spanner/docs/query-optimizer/manage-query-optimizer> for more information on managing the query optimizer.The `optimizerVersion` statement hint has precedence over this setting.  
`optimizerStatisticsPackage` |  `string` An option to control the selection of optimizer statistics package.This parameter allows individual queries to use a different query optimizer statistics package.Specifying `latest` as a value instructs Cloud Spanner to use the latest generated statistics package. If not specified, Cloud Spanner uses the statistics package set at the database level options, or the latest package if the database option isn't set.The statistics package requested by the query has to be exempt from garbage collection. This can be achieved with the following DDL statement:
    
    
    ALTER STATISTICS <package_name> SET OPTIONS (allow_gc=false)
    

The list of available statistics packages can be queried from `INFORMATION_SCHEMA.SPANNER_STATISTICS`.Executing a SQL statement with an invalid optimizer statistics package or with a statistics package that allows garbage collection fails with an `INVALID_ARGUMENT` error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
