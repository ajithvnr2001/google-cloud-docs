---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/list/
title: Method: organizations.apis.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:21.416526+00:00
---

# Method: organizations.apis.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apis.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the names of all API proxies in an organization. The names returned correspond to the names defined in the configuration files for each API proxy.

If the resource has the `space` attribute set, the response may not return all resources. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/apis`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization in the following format: `organizations/{org}`If the resource has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.proxies.list`

  
  
### Query parameters

Parameters  
---  
`includeRevisions` |  `boolean` Flag that specifies whether to include a list of revisions in the response.  
`includeMetaData` |  `boolean` Flag that specifies whether to include API proxy metadata in the response.  
`space` |  `string` Optional. The space ID to filter the list of proxies (optional). If unspecified, all proxies in the organization will be listed.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "proxies": [
        {
          object ([ApiProxy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis#ApiProxy))
        }
      ]
    }  
  
Fields  
---  
`proxies[]` |  `object (`[ApiProxy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis#ApiProxy)`)`  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
