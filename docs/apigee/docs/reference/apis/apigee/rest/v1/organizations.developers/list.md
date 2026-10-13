---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/list/
title: Method: organizations.developers.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:33.843606+00:00
---

# Method: organizations.developers.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all developers in an organization by email address.

By default, the response does not include company developers. Set the `includeCompany` query parameter to `true` to include company developers.

**Note** : A maximum of 1000 developers are returned in the response. You paginate the list of developers returned using the `startKey` and `count` query parameters.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/developers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the Apigee organization. Use the following structure in your request: `organizations/{org}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.developers.list`

  
  
### Query parameters

Parameters  
---  
`expand` |  `boolean` Specifies whether to expand the results. Set to `true` to expand the results. This query parameter is not valid if you use the `count` or `startKey` query parameters.  
`startKey` |  `string` **Note** : Must be used in conjunction with the `count` parameter.Email address of the developer from which to start displaying the list of developers. For example, if the an unfiltered list returns:
    
    
    westley@example.com
    fezzik@example.com
    buttercup@example.com
    

and your `startKey` is `fezzik@example.com`, the list returned will be
    
    
    fezzik@example.com
    buttercup@example.com
      
  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Number of developers to return in the API call. Use with the `startKey` parameter to provide more targeted filtering. The limit is 1000.  
`ids` |  `string` Optional. List of IDs to include, separated by commas.  
`includeCompany` |  `boolean` Flag that specifies whether to include company details in the response.  
`app` |  `string` Optional. List only Developers that are associated with the app. Note that startKey, count are not applicable for this filter criteria.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "developer": [
        {
          object ([Developer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers#Developer))
        }
      ]
    }  
  
Fields  
---  
`developer[]` |  `object (`[Developer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers#Developer)`)` List of developers.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
