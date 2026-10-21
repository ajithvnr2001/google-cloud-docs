---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search/
title: Method: organizations.search \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:34.699237+00:00
---

# Method: organizations.search  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: organizations.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Searches organization resources that are visible to the user and satisfy the specified filter. This method returns organizations in an unspecified order. New organizations do not necessarily appear at the end of the results, and may take a small amount of time to appear.

Search will only return organizations on which the user has the permission `resourcemanager.organizations.get` or has super admin privileges.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/organizations:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of organizations to return in the response. The server can return fewer organizations than requested. If unspecified, server picks an appropriate default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `organizations.search` that indicates from where listing should continue.  
`query` |  `string` Optional. An optional query string used to filter the Organizations to return in the response. Query rules are case-insensitive.
    
    
    | Field            | Description                                |
    |------------------|--------------------------------------------|
    | directoryCustomerId, owner.directoryCustomerId | Filters by directory
    customer id. |
    | domain           | Filters by domain.                         |
    

Organizations may be queried by `directoryCustomerId` or by `domain`, where the domain is a G Suite domain, for example:

  * Query `directorycustomerid:123456789` returns Organization resources with `owner.directory_customer_id` equal to `123456789`.
  * Query `domain:google.com` returns Organization resources corresponding to the domain `google.com`.

  
  
### Request body

The request body must be empty.

### Response body

The response returned from the `organizations.search` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "organizations": [
        {
          object ([Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`organizations[]` |  `object (`[Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization)`)` The list of Organizations that matched the search query, possibly paginated.  
`nextPageToken` |  `string` A pagination token to be used to retrieve the next page of results. If the result is too large to fit within the page size specified in the request, this field will be set with a token that can be used to fetch the next page of results. If this field is empty, it indicates that this response contains the last page of results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloudplatformorganizations`
  * `https://www.googleapis.com/auth/cloudplatformorganizations.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
