---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/exportMetadata/
title: Method: projects.locations.instances.backtestResults.exportMetadata \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:32.933408+00:00
---

# Method: projects.locations.instances.backtestResults.exportMetadata  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/exportMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Reference ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest)



Send feedback 

#  Method: projects.locations.instances.backtestResults.exportMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Export governance information for a BacktestResult resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results).

### HTTP request

`POST https://financialservices.googleapis.com/v1/{backtestResult=projects/*/locations/*/instances/*/backtestResults/*}:exportMetadata`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`backtestResult` |  `string` Required. The resource name of the BacktestResult. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `backtestResult`:

  * `financialservices.v1backtests.exportMetadata`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "structuredMetadataDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#BigQueryDestination))
      }
    }  
  
Fields  
---  
`structuredMetadataDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#BigQueryDestination)`)` Required. BigQuery output where the metadata will be written.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `backtestResult` resource:

  * `financialservices.v1backtests.exportMetadata`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
