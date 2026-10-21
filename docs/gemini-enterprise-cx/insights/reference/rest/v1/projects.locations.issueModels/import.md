---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/import/
title: Method: projects.locations.issueModels.import \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:15.555189+00:00
---

# Method: projects.locations.issueModels.import  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.issueModels.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * GcsSource
    * JSON representation
  * Try it!



Imports an issue model from a Cloud Storage bucket.

### HTTP request

`POST https://{endpoint}/v1/{parent=projects/*/locations/*}/issueModels:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the issue model.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "createNewModel": boolean,
    
      // Union field Source can be only one of the following:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/import#GcsSource))
      }
      // End of list of possible types for union field Source.
    }  
  
Fields  
---  
`createNewModel` |  `boolean` Optional. If set to true, will create an issue model from the imported file with randomly generated IDs for the issue model and corresponding issues. Otherwise, replaces an existing model with the same ID as the file.  
Union field `Source`.`Source` can be only one of the following:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/import#GcsSource)`)` Google Cloud Storage source message.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.issueModels.create`
  * `contactcenterinsights.issueModels.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GcsSource

Google Cloud Storage Object URI to get the issue model file from.

JSON representation  
---  
      
    
    {
      "objectUri": string
    }  
  
Fields  
---  
`objectUri` |  `string` Required. Format: `gs://<bucket-name>/<object-name>`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
