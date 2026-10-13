---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata/
title: Method: threatCollections.fetchEntityMetadata \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:23.478367+00:00
---

# Method: threatCollections.fetchEntityMetadata  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: threatCollections.fetchEntityMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ThreatCollectionEntityMetadata
    * JSON representation
  * ThreatCollectionEntityMetadataReference
    * JSON representation



**Full name** : projects.locations.instances.threatCollections.fetchEntityMetadata

Gets a list of entity metadata for a threat collection.

### HTTP request

`GET https://{endpoint}/v1alpha/{name}:fetchEntityMetadata`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the ThreatCollection to fetch entity metadata for. Format: projects/{project}/locations/{location}/instances/{instance}/threatCollections/{threatCollection}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The page size for the number of entities to return. Default and maximum size is 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `FetchEntityMetadata` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `FetchEntityMetadata` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response containing a list of entity metadata.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entityMetadata": [
        {
          object ([ThreatCollectionEntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata#ThreatCollectionEntityMetadata))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`entityMetadata[]` |  `object (`[ThreatCollectionEntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata#ThreatCollectionEntityMetadata)`)` Output only. A list of entity risks scores with information typing them to the threat collection. Ordered by entity.risk_score.  
`nextPageToken` |  `string` Output only. A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` Output only. The total number of entities that match the request. The size of the `entityMetadata` returned by pagination may be less than the `totalSize` that matches.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.threatCollections.fetchEntityMetadata`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ThreatCollectionEntityMetadata

Entity metadata for a threat collection.

JSON representation  
---  
      
    
    {
      "entity": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.entities#Entity))
      },
      "references": [
        {
          object ([ThreatCollectionEntityMetadataReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata#ThreatCollectionEntityMetadataReference))
        }
      ]
    }  
  
Fields  
---  
`entity` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.entities#Entity)`)` An Asset or User entity which contains an entity indicator and riskScore data associated with it.  
`references[]` |  `object (`[ThreatCollectionEntityMetadataReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.threatCollections/fetchEntityMetadata#ThreatCollectionEntityMetadataReference)`)` A list of references associated with the entity.  
  
## ThreatCollectionEntityMetadataReference

A link between a threat collection and an Asset or User entity in a threat collection's entity metadata.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "ioc": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Possible reference types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`ioc` |  `string` The resource name of the Ioc associated with the entity. Format: projects/{project}/locations/{location}/instances/{instance}/iocs/{ioc}  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
