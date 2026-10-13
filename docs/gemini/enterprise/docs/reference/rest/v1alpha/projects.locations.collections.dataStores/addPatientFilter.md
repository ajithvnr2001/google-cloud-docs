---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores/addPatientFilter/
title: Method: projects.locations.collections.dataStores.addPatientFilter \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:21.225959+00:00
---

# Method: projects.locations.collections.dataStores.addPatientFilter  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores/addPatientFilter/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.addPatientFilter Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Adds a group of patient IDs as a patient filter for the data store. Patient filters are empty by default when a data store is created, and are stored in a separate table. The data store must first be created, and must be a healthcare data store. The filter group must be a FHIR resource name of type Group, and the filter will be constructed from the direct members of the group which are Patient resources.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{dataStore=projects/*/locations/*/collections/*/dataStores/*}:addPatientFilter`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`dataStore` |  `string` Required. Full resource name of `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#DataStore)`, such as `projects/{project}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}`.If the caller does not have permission to access the `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#DataStore)`, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.If the requested `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#DataStore)` does not exist, a NOT_FOUND error is returned. If the requested `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#DataStore)` already has a patient filter, an ALREADY_EXISTS error will be returned.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filterGroups": [
        string
      ]
    }  
  
Fields  
---  
`filterGroups[]` |  `string` Required. Names of the Group resources to use as a basis for the patient filter, in format `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/fhirStores/{fhir_store_id}/fhir/Group/{groupId}`. if the caller does not have permission to access the FHIR store, regardless of whether it exists, PERMISSION_DENIED error is returned. If the discovery engine service account does not have permission to access the FHIR store, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the group is not found at the location, a RESOURCE_NOT_FOUND error will be returned. The filter group must be a FHIR resource name of type Group, and the filter will be constructed from the direct members of the group which are Patient resources.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
