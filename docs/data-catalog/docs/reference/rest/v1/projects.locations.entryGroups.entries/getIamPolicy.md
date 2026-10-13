---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/getIamPolicy/
title: Method: projects.locations.entryGroups.entries.getIamPolicy \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:37.488126+00:00
---

# Method: projects.locations.entryGroups.entries.getIamPolicy  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/getIamPolicy/

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.entryGroups.entries.getIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Data Catalog is deprecated. Please use Dataplex Universal Catalog instead.

Gets the access control policy for a resource.

May return:

  * A`NOT_FOUND` error if the resource doesn't exist or you don't have the permission to view it.
  * An empty policy if the resource exists but doesn't have a set policy.



Supported resources are:

  * Tag templates
  * Entry groups



Note: This method doesn't get policies from Google Cloud Platform resources ingested into Data Catalog.

To call this method, you must have the following Google IAM permissions:

  * `datacatalog.tagTemplates.getIamPolicy` to get policies on tag templates.
  * `datacatalog.entryGroups.getIamPolicy` to get policies on entry groups.



### HTTP request

`POST https://datacatalog.googleapis.com/v1/{resource}:getIamPolicy`

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. It takes the form `projects/{project}/locations/{location}/entryGroups/{entrygroup}/entries/{entries}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "options": {
        object ([GetPolicyOptions](https://docs.cloud.google.com/data-catalog/docs/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions))
      }
    }  
  
Fields  
---  
`options` |  `object (`[GetPolicyOptions](https://docs.cloud.google.com/data-catalog/docs/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions)`)` OPTIONAL: A `GetPolicyOptions` object for specifying options to `entries.getIamPolicy`.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/data-catalog/docs/reference/rest/Shared.Types/Policy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
