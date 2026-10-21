---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/list/
title: Method: organizations.customConstraints.list \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:41.088196+00:00
---

# Method: organizations.customConstraints.list  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Method: organizations.customConstraints.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Retrieves all of the custom constraints that exist on a particular organization resource.

### HTTP request

`GET https://orgpolicy.googleapis.com/v2/{parent=organizations/*}/customConstraints`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The target Google Cloud resource that parents the set of custom constraints that will be returned from this call. Must be in one of the following forms:

  * `organizations/{organization_id}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `orgpolicy.customConstraints.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Size of the pages to be returned. This is not used, but the server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start using this field.  
  
### Request body

The request body must be empty.

### Response body

The response returned from the `[customConstraints.list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/list#google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints)` method. It will be empty if no custom or managed constraints are set on the organization resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customConstraints": [
        {
          object ([CustomConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#CustomConstraint))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`customConstraints[]` |  `object (`[CustomConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#CustomConstraint)`)` All custom and managed constraints that exist on the organization resource. It will be empty if no custom constraints are set.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start supplying a valid token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/organizationpolicy`
  * `https://www.googleapis.com/auth/organizationpolicy.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
