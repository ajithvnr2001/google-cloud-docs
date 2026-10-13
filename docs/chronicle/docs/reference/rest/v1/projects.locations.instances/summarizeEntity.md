---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity/
title: Method: instances.summarizeEntity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:27.310491+00:00
---

# Method: instances.summarizeEntity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.summarizeEntity Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * PrevalenceSnapshot
    * JSON representation
  * AssetRiskMetadata
    * JSON representation
  * MetadataAndProperties
    * JSON representation
  * FileHashProperties
    * JSON representation
  * QueryState
  * WidgetMetadata
    * JSON representation



**Full name** : projects.locations.instances.summarizeEntity

Returns all entity data over specified time. The API returns a maximum of 1000 entities.

### HTTP request

`GET https://{endpoint}/v1/{instance}:summarizeEntity`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance to summarize an entity for. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Query parameters

Parameters  
---  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. Time range to retrieve the summary for [Inclusive start time, exclusive end time).  
`returnPrevalence` |  `boolean` Optional. Whether to return prevelance data for the entity.  
`prevalenceInput` |  `object (`[FieldAndValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldAndValue)`)` Optional. Entity to use in order to compute combined prevalences. `returnPrevalence` needs to be set in order to compute prevalence.  
`returnAlerts` |  `boolean` Optional. Whether to return alertCounts for the entity.  
`includeAllUdmEventTypesForFirstLastSeen` |  `boolean` Optional. If true, it includes all types of events we show in UDM Search to calculate the first and last seen time of an entity.  
Identifier options to find the entity snapshots. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityId` |  `string` ID of the entity indicator to list entity summary snapshots for.  
`fieldAndValue` |  `object (`[FieldAndValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldAndValue)`)` A set of fields which characterize the entity indicator to return entity summary snapshots for. This can use either an enumerated type or infer the type from a UDM path.  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

Response message to retrieve summarized data for an entity.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity))
        }
      ],
      "alertCounts": [
        {
          object ([AlertCountByRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertCountByRule))
        }
      ],
      "hasMoreAlerts": boolean,
      "timeline": {
        object ([Timeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Timeline))
      },
      "prevalenceResult": [
        {
          object ([PrevalenceSnapshot](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#PrevalenceSnapshot))
        }
      ],
      "tpdPrevalenceResult": [
        {
          object ([PrevalenceSnapshot](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#PrevalenceSnapshot))
        }
      ],
      "assetPrevalenceTimes": [
        string
      ],
      "assetRiskMetadata": [
        {
          object ([AssetRiskMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#AssetRiskMetadata))
        }
      ],
      "fileMetadataAndProperties": {
        object ([MetadataAndProperties](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#MetadataAndProperties))
      },
      "widgetMetadata": {
        object ([WidgetMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#WidgetMetadata))
      },
      "topLevelDomain": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity))
      }
    }  
  
Fields  
---  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity)`)` A list of entities. Each "entity" is a snapshot of data about the requested entity indicator for a particular time range.  
`alertCounts[]` |  `object (`[AlertCountByRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertCountByRule)`)` Rule display names with an alert count for each rule that has alerts that match the requested entity indicator. This will only be populated if returnAlerts is true in the request.  
`hasMoreAlerts` |  `boolean` Indicates if there are more alerts than the limit (1000 currently).  
`timeline` |  `object (`[Timeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Timeline)`)` Data representing the number of alerts associated with the entity indicator within the requested time range, bucketed by time ranges. This will only be populated if returnAlerts is true in the request.  
`prevalenceResult[]` |  `object (`[PrevalenceSnapshot](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#PrevalenceSnapshot)`)` Prevalence statistics for the requested indicator.  
`tpdPrevalenceResult[]` |  `object (`[PrevalenceSnapshot](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#PrevalenceSnapshot)`)` If the entity was a domain with a different top private domain, this will contain statistics for the top private domain.  
`assetPrevalenceTimes[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamps at which the asset was queried for the entity being summarized.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assetRiskMetadata[]` |  `object (`[AssetRiskMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#AssetRiskMetadata)`)` Vendor-defined risk metadata for an asset entity. This will only be populated if the requested entity indicator is for an asset entity (internal IP, hostname, MAC, etc.)  
`fileMetadataAndProperties` |  `object (`[MetadataAndProperties](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#MetadataAndProperties)`)` File hash metadata and properties. This data will be only be populated if the requested entity indicator is for a file entity (MD5, SHA1, SHA256 file hash).  
`widgetMetadata` |  `object (`[WidgetMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#WidgetMetadata)`)` Widget metadata for the VirusTotal VT Augment widget. This is included for entity indicators that are supported by VirusTotal including file hash (MD5, SHA1, SHA256), IP, and Domain.  
`topLevelDomain` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity)`)` Data describing the Top level domain entity for the requested indicator.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.entities.summarize`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## PrevalenceSnapshot

Prevalence statistics for an artifact at a particular point of time.

JSON representation  
---  
      
    
    {
      "prevalenceTime": string,
      "count": integer
    }  
  
Fields  
---  
`prevalenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp that the prevalence statistic represents.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`count` |  `integer` The prevalence count for the indicator at the prevalenceTime.  
  
## AssetRiskMetadata

Arbitrary vendor-defined risk metadata about an asset entity.

JSON representation  
---  
      
    
    {
      "sourceProduct": string,
      "uploadTime": string,
      "risks": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`sourceProduct` |  `string` Source product that produces the risk metadata for the asset.  
`uploadTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp of the event that uploaded this metadata version.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`risks` |  `map (key: string, value: string)` Map from a risk's name to its description.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## MetadataAndProperties

Data about a file hash entity.

JSON representation  
---  
      
    
    {
      "metadata": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Label))
        }
      ],
      "properties": [
        {
          object ([FileHashProperties](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#FileHashProperties))
        }
      ],
      "specialDescriptions": [
        string
      ],
      "queryState": enum ([QueryState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#QueryState))
    }  
  
Fields  
---  
`metadata[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Label)`)` File hash's metadata include file type and file size information.  
`properties[]` |  `object (`[FileHashProperties](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#FileHashProperties)`)` Properties include PE properties (for windows file only) and signer details.  
`specialDescriptions[]` |  `string` Special descriptions for risks of some well-known file types, e.g., micsoroft office documents.  
`queryState` |  `enum (`[QueryState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity#QueryState)`)` Output only. File hash query state.  
  
## FileHashProperties

File hash properties.

JSON representation  
---  
      
    
    {
      "title": string,
      "properties": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Label))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Title of properties: for example, "PE Properties".  
`properties[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Label)`)` Repeated field of properties  
  
## QueryState

File hash query state.

Enums  
---  
`QUERY_STATE_UNSPECIFIED` | Unspecified state for file hash query.  
`QUERY_STATE_OK_HAS_RESULT` | Query is successful and has result.  
`QUERY_STATE_OK_HAS_NO_RESULT` | Query is successful but has no result.  
`QUERY_STATE_ERROR` | Query is unsuccessful.  
  
## WidgetMetadata

VirusTotal widget metadata.

JSON representation  
---  
      
    
    {
      "uri": string,
      "detections": integer,
      "total": integer
    }  
  
Fields  
---  
`uri` |  `string` Widget rendering URL for the VirusTotal VT Augment widget. See <https://docs.virustotal.com/reference/widgeturl>  
`detections` |  `integer` Number of scanners which flagged this content.  
`total` |  `integer` Total number of scanners.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
