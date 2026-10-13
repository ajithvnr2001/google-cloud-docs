---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations/batchGet/
title: Method: iocAssociations.batchGet \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:01.031589+00:00
---

# Method: iocAssociations.batchGet  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations/batchGet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: iocAssociations.batchGet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.iocAssociations.batchGet

Gets a batch (list) of IocAssociations given a list of names and a parent.

### HTTP request

`GET https://{endpoint}/v1beta/{parent}/iocAssociations:batchGet`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent that owns this batch of ioc associations. Format: projects/{project}/locations/{region}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`names[]` |  `string` Required. The names of the IocAssociations to retrieve. A maximum of 1000 IocAssociations can be retrieved in a batch. Format: projects/{project}/locations/{location}/instances/{instance}/iocAssociations/{iocAssociation}  
  
### Request body

The request body must be empty.

### Response body

Response message to get a batch of IocAssociations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "associations": [
        {
          object ([IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation))
        }
      ]
    }  
  
Fields  
---  
`associations[]` |  `object (`[IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation)`)` The list of IocAssociations requested.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.iocAssociations.batchGet`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
