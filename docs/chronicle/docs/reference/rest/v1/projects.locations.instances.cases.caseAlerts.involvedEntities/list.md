---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/list/
title: Method: involvedEntities.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:23.181774+00:00
---

# Method: involvedEntities.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: involvedEntities.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseAlerts.involvedEntities.list

Lists all InvolvedEntities associated with a specific case and alert.

### HTTP request

`GET https://{endpoint}/v1/{parent}/involvedEntities`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list InvolvedEntities for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}/involvedEntities  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of InvolvedEntities to return. The service may return fewer than this value. If unspecified, at most 50 InvolvedEntities will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `involvedEntities.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter to apply to the list of InvolvedEntities. Supported filter fields: * `entityType`: Filter by the type. * `id`: Filter by the id. * `suspicious`: Filter by the suspicious flag. * `internal`: Filter by the internal flag. * `threatSource`: Filter by the threat source. * `operatingSystem`: Filter by the operating system. * `networkTitle`: Filter by the network title. * `networkPriority`: Filter by the network priority. * `attacker`: Filter by the attacker flag. * `pivot`: Filter by the pivot flag. * `environment`: Filter by the environment. * `manuallyCreated`: Filter by the manually created flag. * `additionalProperties`: Filter by the additional properties. * `entityUri`: Filter by the source system uri. * `enriched`: Filter by the enriched flag. * `artifact`: Filter by the artifact flag. * `vulnerable`: Filter by the vulnerable flag. * `fields`: Filter by the fields. Example: `filter="displayName='some_name'"`  
`orderBy` |  `string` Optional. Configures ordering of InvolvedEntities in the response. If not specified, InvolvedEntities are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. Supported sort fields: * `entityType` * `id` * `suspicious` * `internal` * `threatSource` * `operatingSystem` * `networkTitle` * `networkPriority` * `attacker` * `pivot` * `environment` * `manuallyCreated` * `additionalProperties` * `entityUri` * `enriched` * `artifact` * `vulnerable` * `fields` example: "entityType desc, suspicious"  
`distinctBy` |  `string` Optional. Configures distinct by fields for the response. example: "type, identifier"  
  
### Request body

The request body must be empty.

### Response body

Response message for involvedEntities.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "involvedEntities": [
        {
          object ([InvolvedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#InvolvedEntity))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`involvedEntities[]` |  `object (`[InvolvedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#InvolvedEntity)`)` The list of InvolvedEntities.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of InvolvedEntities.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.involvedEntities.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
