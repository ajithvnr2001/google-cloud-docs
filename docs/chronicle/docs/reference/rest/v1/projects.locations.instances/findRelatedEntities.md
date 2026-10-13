---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findRelatedEntities/
title: Method: instances.findRelatedEntities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:20.213506+00:00
---

# Method: instances.findRelatedEntities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findRelatedEntities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.findRelatedEntities Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * DomainType



**Full name** : projects.locations.instances.findRelatedEntities

Finds all the entities associated with provided entity. The API returns a maximum of 100 entities.

### HTTP request

`GET https://{endpoint}/v1/{instance}:findRelatedEntities`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance to find related entities for. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Query parameters

Parameters  
---  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. Time range to search related entities for [inclusive start time, exclusive end time).  
`entityTypes[]` |  `enum (`[EntityType](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/EntityType)`)` Optional. Entity types to filter related entities by. If unspecified, will return all related entities for the given entity.  
`domainType` |  `enum (`[DomainType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findRelatedEntities#DomainType)`)` Optional. The domain type to retrieve. This is taken into account when the entity type is specified as "DOMAIN_NAME".  
`excludeFirstLastSeen` |  `boolean` Optional. If true, then the related entities will not have first/last seen info and reduce latency of endpoint.  
`includeAllUdmEventTypesForFirstLastSeen` |  `boolean` Optional. If true, it includes all types of events we show in UDM Search to calculate the first and last seen time of an entity.  
`limit` |  `integer` Optional. The maximum number of Entities to return. The service may return fewer than this value. If unspecified, at most 100 entities will be returned. The maximum value is 100; values above 100 will be coerced to 100. This field replaces the deprecated `pageSize` field.  
Identifier to find the entity. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityId` |  `string` ID of the entity.  
`fieldAndValue` |  `object (`[FieldAndValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldAndValue)`)` Field path and value to identify entity.  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

Response message for finding related entities.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "relatedEntities": [
        {
          object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity))
        }
      ],
      "hasMoreEntities": boolean,
      "resultTimeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval))
      }
    }  
  
Fields  
---  
`relatedEntities[]` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity)`)` List of related entities.  
`hasMoreEntities` |  `boolean` Indicates if there are more relatedEntities available but were not returned due to the `pageSize`.  
`resultTimeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Time range of related entities  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.entities.findRelatedEntities`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## DomainType

Domain Type.

Enums  
---  
`DOMAIN_TYPE_UNSPECIFIED` | Unspecified.  
`DOMAIN_TYPE_SIBLING` | Sibling domain.  
`DOMAIN_TYPE_SUBDOMAIN` | Subdomain.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
