---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances/runOnDemand/
title: Method: connectorInstances.runOnDemand \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:26.398154+00:00
---

# Method: connectorInstances.runOnDemand  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances/runOnDemand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: connectorInstances.runOnDemand Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SampleCase
    * JSON representation



**Full name** : projects.locations.instances.integrations.connectors.connectorInstances.runOnDemand

Triggers an immediate, single execution of the connector. Use this method for testing configuration changes or manually force-starting a data ingestion cycle.

### HTTP request

`POST https://{endpoint}/v1alpha/{name}:runOnDemand`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The connector instance identifier (from route) Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/connectors/{connector}/connectorInstances/{connectorInstance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "connectorInstance": {
        object ([ConnectorInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstance))
      }
    }  
  
Fields  
---  
`connectorInstance` |  `object (`[ConnectorInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances#ConnectorInstance)`)` Required. The connector instance with values from FE.  
  
### Response body

Response for connectorInstances.runOnDemand.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "debugOutput": string,
      "success": boolean,
      "sampleCases": [
        {
          object ([SampleCase](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances/runOnDemand#SampleCase))
        }
      ]
    }  
  
Fields  
---  
`debugOutput` |  `string` Output only. The execution debug output message  
`success` |  `boolean` Output only. True if the execution was successful, false if not.  
`sampleCases[]` |  `object (`[SampleCase](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.connectors.connectorInstances/runOnDemand#SampleCase)`)` Output only. The alerts that were produced by the connector run. Could also be an empty list when no alerts were produced by the connector.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.connectorInstances.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SampleCase

Sample case.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "productName": string,
      "startTime": string,
      "endTime": string,
      "eventCount": string,
      "fullCaseInfoAsJson": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The display name of the sample case  
`productName` |  `string` Output only. The product name of the alert  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The start time of the sample case  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The end time of the sample case  
`eventCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of events in the alert  
`fullCaseInfoAsJson` |  `string` Output only. The sample case full info represented as json  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
