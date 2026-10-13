---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations/importIntegrationDependency/
title: Method: integrations.importIntegrationDependency \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:45.782789+00:00
---

# Method: integrations.importIntegrationDependency  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations/importIntegrationDependency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: integrations.importIntegrationDependency Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.integrations.importIntegrationDependency

Uploads a raw dependency file (e.g., a wheel file or binary) to an existing custom integration. Useful for air-gapped environments or proprietary libraries.

### HTTP request

  * Upload URI, for media upload requests:  
`POST https://{endpoint}/upload/v1/{name}:uploadDependency`
  * Metadata URI, for metadata-only requests:  
`POST https://{endpoint}/v1/{name}:uploadDependency`



Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The unique name of the integration. Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dependency": string,
      "media": {
        object ([Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media))
      },
      "mediaInfo": {
        object ([MediaRequestInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaRequestInfo))
      }
    }  
  
Fields  
---  
`dependency` |  `string` Required. The dependency name to upload, limited to a maximum length of 255 chars. This is the name of the dependency that will be in the integration. For example, if the integration has a dependency named "mysql", then the dependency would be "mysql".  
`media` |  `object (`[Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media)`)` Information representing the imported data  
`mediaInfo` |  `object (`[MediaRequestInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaRequestInfo)`)` Metadata about the media upload request.  
  
### Response body

Response message for importing an integration dependency.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mediaInfo": {
        object ([MediaResponseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo))
      }
    }  
  
Fields  
---  
`mediaInfo` |  `object (`[MediaResponseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo)`)` Info about a media upload request from Scotty.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.integrations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
