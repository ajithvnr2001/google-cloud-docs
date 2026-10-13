---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1Beta1/latest/Google.Cloud.BigQuery.DataPolicies.V1Beta1.DataMaskingPolicy.Types.PredefinedExpression
title: BigQuery Data Policy v1beta1 API - Enum DataMaskingPolicy.Types.PredefinedExpression (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:05.381558+00:00
---

# BigQuery Data Policy v1beta1 API - Enum DataMaskingPolicy.Types.PredefinedExpression (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1Beta1/latest/Google.Cloud.BigQuery.DataPolicies.V1Beta1.DataMaskingPolicy.Types.PredefinedExpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Data Policy v1beta1 API - Enum DataMaskingPolicy.Types.PredefinedExpression (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1Beta1/latest/Google.Cloud.BigQuery.DataPolicies.V1Beta1.DataMaskingPolicy.Types.PredefinedExpression)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1Beta1/1.0.0-beta04/Google.Cloud.BigQuery.DataPolicies.V1Beta1.DataMaskingPolicy.Types.PredefinedExpression)


    
    
    public enum DataMaskingPolicy.Types.PredefinedExpression

Reference documentation and code samples for the BigQuery Data Policy v1beta1 API enum DataMaskingPolicy.Types.PredefinedExpression.

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.

## Namespace

[Google.Cloud.BigQuery.DataPolicies.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1Beta1/latest/Google.Cloud.BigQuery.DataPolicies.V1Beta1)

## Assembly

Google.Cloud.BigQuery.DataPolicies.V1Beta1.dll

## Fields   
  
---  
**Name** | **Description**  
`AlwaysNull` | Masking expression to replace data with NULLs.  
`DefaultMaskingValue` | Masking expression to replace data with their default masking values. The default masking values for each type listed as below:

  * STRING: ""
  * BYTES: b''
  * INTEGER: 0
  * FLOAT: 0.0
  * NUMERIC: 0
  * BOOLEAN: FALSE
  * TIMESTAMP: 0001-01-01 00:00:00 UTC
  * DATE: 0001-01-01
  * TIME: 00:00:00
  * DATETIME: 0001-01-01T00:00:00
  * GEOGRAPHY: POINT(0 0)
  * BIGNUMERIC: 0
  * ARRAY: []
  * STRUCT: NOT_APPLICABLE
  * JSON: NULL

  
`Sha256` | Masking expression to replace data with SHA-256 hash.  
`Unspecified` | Default, unspecified predefined expression. No masking will take place since no expression is specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
