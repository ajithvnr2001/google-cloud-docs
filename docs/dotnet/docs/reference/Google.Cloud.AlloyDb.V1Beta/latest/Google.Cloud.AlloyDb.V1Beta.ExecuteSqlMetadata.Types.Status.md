---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlMetadata.Types.Status
title: AlloyDB v1beta API - Enum ExecuteSqlMetadata.Types.Status (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:16.126806+00:00
---

# AlloyDB v1beta API - Enum ExecuteSqlMetadata.Types.Status (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlMetadata.Types.Status

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Enum ExecuteSqlMetadata.Types.Status (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public enum ExecuteSqlMetadata.Types.Status

Reference documentation and code samples for the AlloyDB v1beta API enum ExecuteSqlMetadata.Types.Status.

Status contains all valid Status a SQL execution can end up in.

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`Error` | Error during SQL execution. Atleast 1 SQL statement execution resulted in a error. Side effects of other statements are rolled back. The "message" field will contain human readable error given by Postgres of the first bad SQL statement. SQL execution errors don't constitute API errors as defined in <https://google.aip.dev/193> but will be returned as part of this message.  
`Ok` | No error during SQL execution i.e. All SQL statements ran to completion. The "message" will be empty.  
`Partial` | Same as OK, except indicates that only partial results were returned. The "message" field will contain details on why results were truncated.  
`Unspecified` | The status is unknown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
