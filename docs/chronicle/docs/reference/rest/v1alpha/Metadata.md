---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata/
title: Metadata \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:44.531252+00:00
---

# Metadata  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Metadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EventTimestampAttribute
  * Tags
    * JSON representation
  * EnrichmentState
  * DataAccessLabels
    * JSON representation
  * DataAccessIngestionLabel
    * JSON representation



General information associated with a UDM event.

JSON representation  
---  
      
    
    {
      "id": string,
      "productLogId": string,
      "eventTimestamp": string,
      "eventTimestampAttributes": [
        enum ([EventTimestampAttribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#EventTimestampAttribute))
      ],
      "collectedTimestamp": string,
      "ingestedTimestamp": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/EventType)),
      "vendorName": string,
      "productName": string,
      "productVersion": string,
      "productEventType": string,
      "productDeploymentId": string,
      "description": string,
      "urlBackToProduct": string,
      "ingestionLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "tags": {
        object ([Tags](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#Tags))
      },
      "enrichmentState": enum ([EnrichmentState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#EnrichmentState)),
      "logType": string,
      "baseLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessLabels))
      },
      "enrichmentLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessLabels))
      },
      "structuredFields": {
        object
      },
      "parserVersion": string
    }  
  
Fields  
---  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` ID of the UDM event. Can be used for raw and normalized event retrieval.A base64-encoded string.  
`productLogId` |  `string` A vendor-specific event identifier to uniquely identify the event (e.g. a GUID).  
`eventTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eventTimestampAttributes[]` |  `enum (`[EventTimestampAttribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#EventTimestampAttribute)`)` Attributes associated with eventTimestamp. This field is used to distinguish between different types of timestamps that can be used to represent the eventTimestamp.  
`collectedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was collected by the vendor's local collection infrastructure.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ingestedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was ingested (received) by Chronicle.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/EventType)`)` The event type. If an event has multiple possible types, this specifies the most specific type.  
`vendorName` |  `string` The name of the product vendor.  
`productName` |  `string` The name of the product.  
`productVersion` |  `string` The version of the product.  
`productEventType` |  `string` A short, descriptive, human-readable, product-specific event name or type (e.g. "Scanned X", "User account created", "process_start").  
`productDeploymentId` |  `string` The deployment identifier assigned by the vendor for a product deployment.  
`description` |  `string` A human-readable unparsable description of the event.  
`urlBackToProduct` |  `string` A URL that takes the user to the source product console for this event.  
`ingestionLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` User-configured ingestion metadata labels.  
`tags` |  `object (`[Tags](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#Tags)`)` Tags added by Chronicle after an event is parsed. It is an error to populate this field from within a parser.  
`enrichmentState` |  `enum (`[EnrichmentState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#EnrichmentState)`)` The enrichment state.  
`logType` |  `string` The string value of log type.  
`baseLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessLabels)`)` Data access labels on the base event.  
`enrichmentLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessLabels)`)` Data access labels from all the contextual events used to enrich the base event.  
`structuredFields  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Flattened fields extracted from the log.  
`parserVersion` |  `string` The version of the parser that generated this UDM event.  
  
## EventTimestampAttribute

Enum representing the type of timestamp that the eventTimestamp field represents.

Enums  
---  
`EVENT_TIMESTAMP_ATTRIBUTE_UNSPECIFIED` | Default event timestamp attribute.  
`FILE_LAST_ACCESS_TIME` | Deprecated. Use LAST_ACCESSED instead.This item is deprecated!  
`FILE_LAST_MODIFIED_TIME` | Deprecated. Use LAST_MODIFIED instead.This item is deprecated!  
`FILE_METADATA_LAST_CHANGE_TIME` | Deprecated. Use METADATA_LAST_CHANGED instead.This item is deprecated!  
`FILE_CREATION_TIME` | Deprecated. Use CREATED instead.This item is deprecated!  
`COLLECTED_TIME` | Deprecated. Use COLLECTED instead.This item is deprecated!  
`COLLECTED` | The time when the event was collected by the vendor's local collection infrastructure.  
`ACCESSED` | The time when the file was accessed.  
`CHANGED` | The time when the file was changed.  
`CREATED` | The time when the file was first created.  
`FILE_NAME_ACCESSED` | The time when the file name was accessed.  
`FILE_NAME_CHANGED` | The time when the file name was changed.  
`FILE_NAME_CREATED` | The time when the file name was created.  
`FILE_NAME_LAST_ACCESSED` | The time when the file name was last accessed.  
`FILE_NAME_LAST_MODIFIED` | The time when the file name was last modified.  
`FILE_NAME_METADATA_LAST_CHANGED` | The time when the file name metadata was last changed.  
`FILE_NAME_MODIFIED` | The time when the file name was modified.  
`LAST_ACCESSED` | The time when the file was last accessed.  
`LAST_MODIFIED` | The time when the file was last modified.  
`METADATA_LAST_CHANGED` | The time when the file metadata was last changed.  
`MODIFIED` | The time when the file was modified.  
`ADDED` | Added Timestamp.  
`BACKED_UP` | Backed Up Timestamp.  
`LAST_CONNECTED` | Last Connected timestamp.  
`DELETED` | Deleted Timestamp.  
`ENDED` | Ended Timestamp.  
`EXITED` | Exited Timestamp.  
`EXPIRED` | Expired Timestamp.  
`FIRST_ACCESSED` | First Accessed Timestamp.  
`APPEARED` | Appeared Timestamp.  
`INSTALLED` | Installed Timestamp.  
`LAST_ACTIVE` | Last Active Timestamp.  
`LAST_LOGGED_IN` | Last Login Timestamp.  
`LAST_LOGIN_ATTEMPT` | Last Login Attempt Timestamp.  
`LAST_PASSWORD_SET` | Last Password Set Timestamp.  
`LAST_PRINTED` | Last Printed Timestamp.  
`LAST_RESUMED` | Last Resumed Timestamp.  
`LAST_EXECUTED` | Last Executed Timestamp.  
`LAST_SEEN` | Last Seen Timestamp.  
`LAST_SHUTDOWN` | Last Shutdown Timestamp.  
`LAST_UPDATED` | Last Updated Timestamp.  
`LAST_USED` | Last Used Timestamp.  
`LAST_VISITED` | Last Visited Timestamp.  
`LINKED` | Linked Timestamp.  
`METADATA_MODIFIED` | Metadata Modified Timestamp.  
`CONTENT_MODIFIED` | Modified Timestamp.  
`PURCHASED` | Purchased Timestamp.  
`RECORDED` | Recorded Timestamp.  
`REQUEST_RECEIVED` | Request Received Timestamp.  
`RESPONSE_SENT` | Response Sent Timestamp.  
`SCHEDULED_TO_END` | Scheduled to End Timestamp.  
`SCHEDULED_TO_START` | Scheduled to Start Timestamp.  
`SENT` | Sent Timestamp.  
`STARTED` | Started Timestamp.  
`UPDATED` | Updated Timestamp.  
`VALIDATED` | Validated Timestamp.  
`MOST_RECENT_RUN` | Most Recent Run Timestamp.  
`NEXT_RUN` | Next Run Timestamp.  
`VISITED` | Visited Timestamp.  
`TARGET_CREATED` | Target Created Timestamp.  
`VOLUME_CREATED` | Volume Created Timestamp.  
`POST_CHECKED` | Post Checked Timestamp.  
`SYNCHRONIZED` | Synchronized Timestamp.  
`ITEM_CREATED` | Item Created Timestamp.  
`ITEM_MODIFIED` | Item Modified Timestamp.  
`DOCUMENT_LAST_SAVED` | Document Last Saved Timestamp.  
`LAST_REGISTERED` | Last Registered Timestamp.  
`LAUNCHED` | Launched Timestamp.  
  
## Tags

Tags are event metadata which is set by examining event contents post-parsing. For example, a UDM event may be assigned a tenantId based on certain customer-defined parameters.

JSON representation  
---  
      
    
    {
      "tenantId": [
        string
      ],
      "dataTapConfigName": [
        string
      ]
    }  
  
Fields  
---  
`tenantId[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A list of subtenant ids that this event belongs to.A base64-encoded string.  
`dataTapConfigName[]` |  `string` A list of sink name values defined in DataTap configurations.  
  
## EnrichmentState

An enrichment state.

Enums  
---  
`ENRICHMENT_STATE_UNSPECIFIED` | Unspecified.  
`ENRICHED` | The event has been enriched by Chronicle.  
`UNENRICHED` | The event has not been enriched by Chronicle.  
  
## DataAccessLabels

JSON representation  
---  
      
    
    {
      "logTypes": [
        string
      ],
      "ingestionLabels": [
        string
      ],
      "namespaces": [
        string
      ],
      "customLabels": [
        string
      ],
      "ingestionKvLabels": [
        {
          object ([DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessIngestionLabel))
        }
      ],
      "allowScopedAccess": boolean
    }  
  
Fields  
---  
`logTypes[]` |  `string` All the LogType labels.  
`ingestionLabels[]  
**(deprecated)**` |  `string` This item is deprecated!All the ingestion labels.  
`namespaces[]` |  `string` All the namespaces.  
`customLabels[]` |  `string` All the complex labels (UDM search syntax based).  
`ingestionKvLabels[]` |  `object (`[DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Metadata#DataAccessIngestionLabel)`)` All the ingestion labels (key/value pairs).  
`allowScopedAccess` |  `boolean` Are the labels ready for scoped access  
  
## DataAccessIngestionLabel

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` The key.  
`value` |  `string` The value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
