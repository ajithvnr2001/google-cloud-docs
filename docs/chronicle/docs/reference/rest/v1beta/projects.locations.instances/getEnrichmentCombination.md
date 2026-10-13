---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination/
title: Method: instances.getEnrichmentCombination \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:44.064211+00:00
---

# Method: instances.getEnrichmentCombination  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.getEnrichmentCombination Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * EnrichmentCombinationRecord
    * JSON representation
  * EnrichmentType
  * EnrichmentSource
    * JSON representation
  * ExternalEnrichmentSource



**Full name** : projects.locations.instances.getEnrichmentCombination

Get the EnrichmentCombination.

### HTTP request

`GET https://{endpoint}/v1beta/{name}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the enrichment combination to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/enrichmentCombination  
  
### Request body

The request body must be empty.

### Response body

EnrichmentCombination resource represents the combination of enrichment. It is a singleton resource that contains all the enrichment combination records.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "enrichmentCombinationRecords": [
        {
          object ([EnrichmentCombinationRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentCombinationRecord))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the enrichment combination. Format: projects/{project}/locations/{location}/instances/{instance}/enrichmentCombination  
`enrichmentCombinationRecords[]` |  `object (`[EnrichmentCombinationRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentCombinationRecord)`)` Output only. All the enrichment combination records.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.enrichmentCombination.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## EnrichmentCombinationRecord

EnrichmentCombinationRecord represents a record of enrichment combination.

JSON representation  
---  
      
    
    {
      "enrichmentType": enum ([EnrichmentType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentType)),
      "enrichmentTargetLogType": string,
      "enrichmentSource": {
        object ([EnrichmentSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentSource))
      }
    }  
  
Fields  
---  
`enrichmentType` |  `enum (`[EnrichmentType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentType)`)` Required. The type of enrichment.  
`enrichmentTargetLogType` |  `string` Required. The log type of an event that is enriched. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{logType}  
`enrichmentSource` |  `object (`[EnrichmentSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#EnrichmentSource)`)` The enrichment source that an enrichment is from. For source that comes from external and does not have a log type, for example, `GEO_IP_SERVICE`, the `ExternalEnrichmentSource` field should be set.  
  
## EnrichmentType

The type of enrichment. It can be expanded to include more types in the future.

Enums  
---  
`ENRICHMENT_TYPE_UNSPECIFIED` | Unspecified.  
`ALL_ENRICHMENT_TYPES` | ALL enrichment types.  
`ASSET_ENRICHMENT` | Asset enrichment.  
`USER_ENRICHMENT` | User enrichment.  
`PROCESS_ENRICHMENT` | Process enrichment.  
`GOOGLE_THREAT_INTEL_ENRICHMENT` | Google Threat Intel enrichment.  
`GEO_IP_ENRICHMENT` | GeoIP enrichment.  
  
## EnrichmentSource

The enrichment source that an enrichment is from. For source that comes from external and does not have a log type, for example, `GEO_IP_SERVICE`, the `ExternalEnrichmentSource` field should be set.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "logType": string,
      "externalEnrichmentSource": enum ([ExternalEnrichmentSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#ExternalEnrichmentSource))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The source of an enrichment can be either a log type or an external enrichment source that does not have a log type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`logType` |  `string` Required. Raw LogType of an enrichment source. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{logType}  
`externalEnrichmentSource` |  `enum (`[ExternalEnrichmentSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination#ExternalEnrichmentSource)`)` Required. Represents an enrichment source from external that does not have a log type. For example, GEO_IP_SERVICE for enrichment from the GeoIP service.  
End of mutually exclusive fields.  
  
## ExternalEnrichmentSource

The external enrichment sources that do not have a log type associated with it.

Enums  
---  
`EXTERNAL_ENRICHMENT_SOURCE_UNSPECIFIED` | Unspecified.  
`GEO_IP_SERVICE` | GeoIP service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
