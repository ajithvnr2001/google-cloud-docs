---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logProcessingPipelines/testPipeline/
title: Method: logProcessingPipelines.testPipeline \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:11.448520+00:00
---

# Method: logProcessingPipelines.testPipeline  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logProcessingPipelines/testPipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: logProcessingPipelines.testPipeline Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.logProcessingPipelines.testPipeline

logProcessingPipelines.testPipeline previews processed logs for a given log processing pipeline for a given input sample logs.

### HTTP request

`POST https://{endpoint}/v1alpha/{parent}/logProcessingPipelines:testPipeline`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the pipeline to preview processed logs for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "logProcessingPipeline": {
        object ([LogProcessingPipeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logProcessingPipelines#LogProcessingPipeline))
      },
      "inputLogs": [
        {
          object ([Log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.logs#Log))
        }
      ]
    }  
  
Fields  
---  
`logProcessingPipeline` |  `object (`[LogProcessingPipeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logProcessingPipelines#LogProcessingPipeline)`)` Required. The LogProcessingPipeline to test.  
`inputLogs[]` |  `object (`[Log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.logs#Log)`)` Required. The logs to preview processed logs for. These are the logs that will be sent to the pipeline for processing.  
  
### Response body

Response message for logProcessingPipelines.testPipeline.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "logs": [
        {
          object ([Log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.logs#Log))
        }
      ]
    }  
  
Fields  
---  
`logs[]` |  `object (`[Log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.logs#Log)`)` Resultant, processed logs after execution of log processing pipeline.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.logProcessingPipelines.testPipeline`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
