---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_security_alert/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:08.787370+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_security_alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_security_alert`

Get a specific security alert by its ID directly from Chronicle SIEM.

Retrieves a specific alert's details including rule name, creation time, status, and severity.

**Agent Responsibilities:** \- Provide the exact `alert_id`. - Parse the returned JSON to extract relevant details.

**Workflow Integration:** \- Use to get detailed information about a specific alert found via `get_alerts` or referenced in a case. - Essential for alert triage and investigation.

**Use Cases:** \- Investigate the details of a high-severity alert. - Retrieve the full context of an alert for reporting or case creation.

Args: alert_id (str): The unique ID of the alert to retrieve. project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). include_detections (bool): Whether to include non-alerting detections. Defaults to false.

Returns: str: Raw JSON response containing the alert details (as a 'backstory.Collection' object).

Example Usage: get_security_alert( alert_id="de_12345678-1234-1234-1234-1234567890ab", project_id="my-project", customer_id="my-customer", region="us", include_detections=true )

Next Steps: - Update the alert status using `update_security_alert`. - Create a case based on this alert.

The following sample demonstrate how to use `curl` to invoke the `get_security_alert` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_security_alert",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for LegacyGetAlert.

### LegacyGetAlertRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "alertId": string,
      "includeDetections": boolean
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`alertId` |  `string` The unique ID of the alert/collection.  
`includeDetections` |  `boolean` Whether to include non-alerting detections.  
  
## Output Schema

Returns Alert for a given Collection Id. NEXT TAG: 2

### LegacyGetAlertResponse

JSON representation  
---  
      
    
    {
      "alert": {
        object ([Collection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Collection))
      }
    }  
  
Fields  
---  
`alert` |  `object (`[Collection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Collection)`)` Alert as Collection.  
  
### Collection

JSON representation  
---  
      
    
    {
      "id": string,
      "type": enum (CollectionType),
      "idNamespace": enum (Namespace),
      "createdTime": string,
      "lastUpdatedTime": string,
      "timeWindow": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval))
      },
      "collectionElements": [
        {
          object ([Element](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Element))
        }
      ],
      "detection": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
        }
      ],
      "detectionTime": string,
      "investigation": {
        object ([Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Investigation))
      },
      "tags": [
        string
      ],
      "responsePlatformInfo": {
        object ([ResponsePlatformInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.ResponsePlatformInfo))
      },
      "caseName": string,
      "feedbackSummary": {
        object ([Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Feedback))
      },
      "feedbackHistory": [
        {
          object ([Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Feedback))
        }
      ],
      "soarAlert": boolean,
      "soarAlertMetadata": {
        object ([SoarAlertMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.SoarAlertMetadata))
      },
      "dataAccessScope": string,
      "detectionTimingDetails": [
        enum (DetectionTimingDetails)
      ],
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.LatencyMetrics))
      },
      "ruleRunFrequency": enum (RunFrequency)
    }  
  
Fields  
---  
`id` |  `string` Unique ID for the collection. The ID is specific to the type of collection. For example, with rule detections this is the detection ID.  
`type` |  `enum (`CollectionType`)` What the collection represents.  
`idNamespace` |  `enum (`Namespace`)` The ID namespace used for the Collection.  
`createdTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the collection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdatedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the collection was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeWindow` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval)`)` Time interval that the collection represents.  
`collectionElements[]` |  `object (`[Element](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Element)`)` Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.  
`detection[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).  
`detectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp within the time_window related to the time of the collection_elements. For Rule Detections, this timestamp is the end of the the time_window for multi-event rules or the time of the event for single event rules. For late-arriving events that trigger new alerts, the detection_time will be the event time of the event.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`investigation` |  `object (`[Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Investigation)`)` Consolidated investigation details (categorization, status, etc) typically for collections that begin as detection findings and then evolve with analyst action and feedback into investigations around the detection output.  
`tags[]` |  `string` Tags set by UC/DSML/RE for the Finding during creation.  
`responsePlatformInfo` |  `object (`[ResponsePlatformInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.ResponsePlatformInfo)`)` Alert related info of this same alert in customer's SOAR platform.  
`caseName` |  `string` The resource name of the Case that this collection belongs to. Example: projects/{project id}/locations/{region}/chronicle/cases/{internal_case_id}  
`feedbackSummary` |  `object (`[Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Feedback)`)` The current primary analyst feedback. This does not include the history of feedback given, which may be supplied in `feedback`.  
`feedbackHistory[]` |  `object (`[Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Feedback)`)` The history of feedback submitted by analysts for this finding, in descending order by timestamp. This field is limited to the most recent 1000 feedback events. The primary feedback will also be included in this list.  
`soarAlert` |  `boolean` A boolean field indicating that the alert is present in SOAR.  
`soarAlertMetadata` |  `object (`[SoarAlertMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.SoarAlertMetadata)`)` Metadata fields of alerts coming from other SIEM systems via SOAR.  
`dataAccessScope` |  `string` The resource name of the DataAccessScope of this collection.  
`detectionTimingDetails[]` |  `enum (`DetectionTimingDetails`)` Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.LatencyMetrics)`)` The latency metrics for the specific detection. These metrics are calculated from ALL of the events that contribute to the detection, not just the sampled ones.  
`ruleRunFrequency` |  `enum (`RunFrequency`)` The run frequency of the rule when it generated the detection.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Interval

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Element

JSON representation  
---  
      
    
    {
      "association": {
        object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
      },
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Reference))
        }
      ],
      "label": string,
      "referencesSampled": boolean,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.LatencyMetrics))
      }
    }  
  
Fields  
---  
`association` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` Metadata that provides the relevant association for the references in the element. For a detection, this can be the correlated aspect of the references that contributed to the overall detection. For example, may include sub-rule condition, machine learning model metadata, and/or indicators implicated in this component of the detection (using the .about field).  
`references[]` |  `object (`[Reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Reference)`)` References to model primatives including events and entities that share a common association. Even though a reference can have both UDM and entity, a collection of references (of a single element) will only have one type of message in it (either UDM / Entity).  
`label` |  `string` A name that labels the entire references group.  
`referencesSampled` |  `boolean` Copied from the detection event_sample.too_many_event_samples field. If true, the number of references will be capped at the sample limit (set at rule service). This is applicable to both UDM references and Entity references.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.LatencyMetrics)`)` Latency metrics for the specific element. These are calculated from all the contributing events or entities for a single event variable, not just the sampled ones included in references. This is currently only populated for UDM events.  
  
### SecurityResult

JSON representation  
---  
      
    
    {
      "about": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "category": [
        enum (SecurityCategory)
      ],
      "categoryDetails": [
        string
      ],
      "threatName": string,
      "ruleSet": string,
      "ruleSetDisplayName": string,
      "rulesetCategoryDisplayName": string,
      "ruleId": string,
      "ruleName": string,
      "ruleVersion": string,
      "ruleType": string,
      "ruleAuthor": string,
      "ruleLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "alertState": enum (AlertState),
      "detectionFields": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "outcomes": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "variables": {
        string: {
          object ([FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FindingVariable))
        },
        ...
      },
      "summary": string,
      "description": string,
      "action": [
        enum (Action)
      ],
      "actionDetails": string,
      "severity": enum (ProductSeverity),
      "confidence": enum (ProductConfidence),
      "priority": enum (ProductPriority),
      "riskScore": number,
      "confidenceScore": number,
      "analyticsMetadata": [
        {
          object ([AnalyticsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AnalyticsMetadata))
        }
      ],
      "severityDetails": string,
      "confidenceDetails": string,
      "priorityDetails": string,
      "urlBackToProduct": string,
      "threatId": string,
      "threatFeedName": string,
      "threatIdNamespace": enum (Namespace),
      "threatStatus": enum (ThreatStatus),
      "attackDetails": {
        object ([AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AttackDetails))
      },
      "firstDiscoveredTime": string,
      "associations": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Association))
        }
      ],
      "campaigns": [
        string
      ],
      "reports": [
        string
      ],
      "verdict": {
        object ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Verdict))
      },
      "lastUpdatedTime": string,
      "verdictInfo": [
        {
          object ([VerdictInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.VerdictInfo))
        }
      ],
      "threatVerdict": enum (ThreatVerdict),
      "lastDiscoveredTime": string,
      "detectionDepth": string,
      "threatCollections": [
        {
          object ([ThreatCollectionItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ThreatCollectionItem))
        }
      ]
    }  
  
Fields  
---  
`about` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` If the security result is about a specific entity (Noun), add it here. This field is not populated when the SecurityResult appears in a detection.  
`category[]` |  `enum (`SecurityCategory`)` The security category. This field is not populated when the SecurityResult appears in a detection.  
`categoryDetails[]` |  `string` For vendor-specific categories. For web categorization, put type in here such as "gambling" or "porn". This field is not populated when the SecurityResult appears in a detection.  
`threatName` |  `string` A vendor-assigned classification common across multiple customers (for example, "W32/File-A", "Slammer"). This field is not populated when the SecurityResult appears in a detection.  
`ruleSet` |  `string` The curated detection's rule set identifier. (for example, "windows-threats") This is primarily set in rule-generated detections and alerts.  
`ruleSetDisplayName` |  `string` The curated detections rule set display name. This is primarily set in rule-generated detections and alerts.  
`rulesetCategoryDisplayName` |  `string` The curated detection rule set category display name. (for example, if rule_set_display_name is "CDIR SCC Enhanced Exfiltration", the rule_set_category is "Cloud Threats"). This is primarily set in rule-generated detections and alerts.  
`ruleId` |  `string` A vendor-specific ID for a rule, varying by observer type (e.g. "08123", "5d2b44d0-5ef6-40f5-a704-47d61d3babbe").  
`ruleName` |  `string` Name of the security rule (e.g. "BlockInboundToOracle").  
`ruleVersion` |  `string` Version of the security rule. (e.g. "v1.1", "00001", "1604709794", "2020-11-16T23:04:19+00:00"). Note that rule versions are source-dependant and lexical ordering should not be assumed.  
`ruleType` |  `string` The type of security rule.  
`ruleAuthor` |  `string` Author of the security rule. This field is not populated when the SecurityResult appears in a detection.  
`ruleLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` A list of rule labels that can't be captured by the other fields in security result (e.g. "reference : AnotherRule", "contributor : John"). This is primarily set in rule-generated detections and alerts.  
`alertState` |  `enum (`AlertState`)` The alerting types of this security result. This is primarily set for rule-generated detections and alerts.  
`detectionFields[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` An ordered list of values, that represent fields in detections for a security finding. This list represents mapping of names of requested entities to their values (the security result matched variables).For Collection SecurityResults, prefer variables instead.  
`outcomes[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` This item is deprecated!A list of outcomes that represent the results of this security finding. This list represents a mapping of names of the requested outcomes, to a stringified version of their values.This is only populated when the SecurityResult appears in a detection. This is deprecated. Use variables instead.  
`variables` |  `map (key: string, value: object (`[FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FindingVariable)`))` A list of outcomes and match variables that represent the results of this security finding. This list represents a mapping of names of the requested outcomes or match variables, to their values.This is only populated when the SecurityResult appears in a detection.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`summary` |  `string` A short human-readable summary (e.g. "failed login occurred")  
`description` |  `string` A human-readable description (e.g. "user password was wrong"). This can be more detailed than the summary.  
`action[]` |  `enum (`Action`)` Actions taken for this event. This field is not populated when the SecurityResult appears in a detection.  
`actionDetails` |  `string` The detail of the action taken as provided by the vendor. This field is not populated when the SecurityResult appears in a detection.  
`severity` |  `enum (`ProductSeverity`)` The severity of the result.  
`confidence` |  `enum (`ProductConfidence`)` The confidence level of the result as estimated by the product. This field is not populated when the SecurityResult appears in a detection.  
`priority` |  `enum (`ProductPriority`)` The priority of the result. This field is not populated when the SecurityResult appears in a detection.  
`riskScore` |  `number` The risk score of the security result.  
`confidenceScore` |  `number` The confidence score of the security result. This field is not populated when the SecurityResult appears in a detection.  
`analyticsMetadata[]` |  `object (`[AnalyticsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AnalyticsMetadata)`)` Stores metadata about each risk analytic metric the rule uses. This field is not populated when the SecurityResult appears in a detection.  
`severityDetails` |  `string` Vendor-specific severity. This field is not populated when the SecurityResult appears in a detection.  
`confidenceDetails` |  `string` Additional detail with regards to the confidence of a security event as estimated by the product vendor. This field is not populated when the SecurityResult appears in a detection.  
`priorityDetails` |  `string` Vendor-specific information about the security result priority. This field is not populated when the SecurityResult appears in a detection.  
`urlBackToProduct` |  `string` URL that takes the user to the source product console for this event. This field is not populated when the SecurityResult appears in a detection.  
`threatId` |  `string` Vendor-specific ID for a threat. This field is not populated when the SecurityResult appears in a detection.  
`threatFeedName` |  `string` Vendor feed name for a threat indicator feed. This field is not populated when the SecurityResult appears in a detection.  
`threatIdNamespace` |  `enum (`Namespace`)` The attribute threat_id_namespace qualifies threat_id with an id namespace to get an unique id. The attribute threat_id by itself is not unique across Chronicle as it is a vendor specific id. This field is not populated when the SecurityResult appears in a detection.  
`threatStatus` |  `enum (`ThreatStatus`)` Current status of the threat This field is not populated when the SecurityResult appears in a detection.  
`attackDetails` |  `object (`[AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AttackDetails)`)` MITRE ATT&CK details. This field is not populated when the SecurityResult appears in a detection.  
`firstDiscoveredTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First time the IoC threat was discovered in the provider. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`associations[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Association)`)` Associations related to the threat.  
`campaigns[]  
**(deprecated)**` |  `string` This item is deprecated!Campaigns using this IOC threat. This is deprecated. Use threat_collections instead.  
`reports[]  
**(deprecated)**` |  `string` This item is deprecated!Reports that reference this IOC threat. These are the report IDs. This is deprecated. Use threat_collections instead.  
`verdict  
**(deprecated)**` |  `object (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Verdict)`)` This item is deprecated!Verdict about the IoC from the provider. This field is now deprecated. Use VerdictInfo instead.  
`lastUpdatedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the IoC threat was updated in the provider. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictInfo[]` |  `object (`[VerdictInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.VerdictInfo)`)` Verdict information about the IoC from the provider. This field is not populated when the SecurityResult appears in a detection.  
`threatVerdict` |  `enum (`ThreatVerdict`)` GCTI threat verdict on the security result entity. This field is not populated when the SecurityResult appears in a detection.  
`lastDiscoveredTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the IoC was seen in the provider data. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`detectionDepth` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The depth of the detection chain. Applies only to composite detections.  
`threatCollections[]` |  `object (`[ThreatCollectionItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ThreatCollectionItem)`)` GTI collections associated with the security result.  
  
### Noun

JSON representation  
---  
      
    
    {
      "hostname": string,
      "domain": {
        object ([Domain](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Domain))
      },
      "artifact": {
        object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Artifact))
      },
      "urlMetadata": {
        object ([Url](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Url))
      },
      "browser": {
        object ([Browser](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Browser))
      },
      "assetId": string,
      "user": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "userManagementChain": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
        }
      ],
      "group": {
        object ([Group](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Group))
      },
      "process": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process))
      },
      "processAncestors": [
        {
          object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process))
        }
      ],
      "asset": {
        object ([Asset](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Asset))
      },
      "ip": [
        string
      ],
      "natIp": [
        string
      ],
      "port": integer,
      "natPort": integer,
      "mac": [
        string
      ],
      "administrativeDomain": string,
      "namespace": string,
      "url": string,
      "file": {
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.File))
      },
      "email": string,
      "registry": {
        object ([Registry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Registry))
      },
      "application": string,
      "platform": enum (Platform),
      "platformVersion": string,
      "platformPatchLevel": string,
      "cloud": {
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cloud))
      },
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "ipLocation": [
        {
          object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
        }
      ],
      "ipGeoArtifact": [
        {
          object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Artifact))
        }
      ],
      "resource": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource))
      },
      "resourceAncestors": [
        {
          object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource))
        }
      ],
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "objectReference": {
        object ([Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Id))
      },
      "investigation": {
        object ([Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Investigation))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network))
      },
      "securityResult": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
        }
      ]
    }  
  
Fields  
---  
`hostname` |  `string` Client hostname or domain name field. Hostname also doubles as the domain for remote entities. This field can be used as an entity indicator for asset entities.  
`domain` |  `object (`[Domain](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Domain)`)` Information about the domain.  
`artifact` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Artifact)`)` Information about an artifact.  
`urlMetadata` |  `object (`[Url](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Url)`)` Information about the URL.  
`browser` |  `object (`[Browser](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Browser)`)` Information about an entry in the web browser's local history database.  
`assetId` |  `string` The asset ID. This field can be used as an entity indicator for asset entities.  
`user` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Information about the user.  
`userManagementChain[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Information about the user's management chain (reporting hierarchy). Note: user_management_chain is only populated when data is exported to BigQuery since recursive fields (e.g. user.managers) are not supported by BigQuery.  
`group` |  `object (`[Group](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Group)`)` Information about the group.  
`process` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process)`)` Information about the process.  
`processAncestors[]` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process)`)` Information about the process's ancestors ordered from immediate ancestor (parent process) to root. Note: process_ancestors is only populated when data is exported to BigQuery since recursive fields (e.g. process.parent_process) are not supported by BigQuery.  
`asset` |  `object (`[Asset](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Asset)`)` Information about the asset.  
`ip[]` |  `string` A list of IP addresses associated with a network connection. This field can be used as an entity indicator for asset entities.  
`natIp[]` |  `string` A list of NAT translated IP addresses associated with a network connection.  
`port` |  `integer` Source or destination network port number when a specific network connection is described within an event.  
`natPort` |  `integer` NAT external network port number when a specific network connection is described within an event.  
`mac[]` |  `string` List of MAC addresses associated with a device. This field can be used as an entity indicator for asset entities.  
`administrativeDomain` |  `string` Domain which the device belongs to (for example, the Microsoft Windows domain).  
`namespace` |  `string` Namespace which the device belongs to, such as "AD forest". Uses for this field include Microsoft Windows AD forest, the name of subsidiary, or the name of acquisition. This field can be used along with an asset indicator to identify an asset.  
`url` |  `string` The URL.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.File)`)` Information about the file.  
`email` |  `string` Email address. Only filled in for security_result.about  
`registry` |  `object (`[Registry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Registry)`)` Registry information.  
`application` |  `string` The name of an application or service. Some SSO solutions only capture the name of a target application such as "Atlassian" or "Chronicle".  
`platform` |  `enum (`Platform`)` Platform.  
`platformVersion` |  `string` Platform version. For example, "Microsoft Windows 1803".  
`platformPatchLevel` |  `string` Platform patch level. For example, "Build 17134.48"  
`cloud  
**(deprecated)**` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cloud)`)` This item is deprecated!Cloud metadata. Deprecated: cloud should be populated in entity Attribute as generic metadata (e.g. asset.attribute.cloud).  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Physical location. For cloud environments, set the region in location.name.  
`ipLocation[]  
**(deprecated)**` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` This item is deprecated!Deprecated: use ip_geo_artifact.location instead.  
`ipGeoArtifact[]` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Artifact)`)` Enriched geographic information corresponding to an IP address. Specifically, location and network data.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource)`)` Information about the resource (e.g. scheduled task, calendar entry). This field should not be used for files, registry, or processes because these objects are already part of Noun.  
`resourceAncestors[]` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource)`)` Information about the resource's ancestors ordered from immediate ancestor (starting with parent resource).  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` This item is deprecated!Labels are key-value pairs. For example: key = "env", value = "prod". Deprecated: labels should be populated in entity Attribute as generic metadata (e.g. user.attribute.labels).  
`objectReference` |  `object (`[Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Id)`)` Finding to which the Analyst updated the feedback.  
`investigation` |  `object (`[Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Investigation)`)` Analyst feedback/investigation for alerts.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network)`)` Network details, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).  
`securityResult[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` A list of security results.  
  
### Domain

JSON representation  
---  
      
    
    {
      "name": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "registrar": string,
      "contactEmail": string,
      "whoisServer": string,
      "nameServer": [
        string
      ],
      "creationTime": string,
      "updateTime": string,
      "expirationTime": string,
      "auditUpdateTime": string,
      "status": string,
      "registrant": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "admin": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "tech": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "billing": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "zone": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
      },
      "whoisRecordRawText": string,
      "registryDataRawText": string,
      "ianaRegistrarId": integer,
      "privateRegistration": boolean,
      "categories": [
        string
      ],
      "favicon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon))
      },
      "jarm": string,
      "lastDnsRecords": [
        {
          object ([DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DNSRecord))
        }
      ],
      "lastDnsRecordsTime": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SSLCertificate))
      },
      "lastHttpsCertificateTime": string,
      "popularityRanks": [
        {
          object ([PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PopularityRank))
        }
      ],
      "tags": [
        string
      ],
      "whoisTime": string
    }  
  
Fields  
---  
`name` |  `string` The domain name. This field can be used as an entity indicator for Domain entities.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence)`)` The prevalence of the domain within the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First seen timestamp of the domain in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last seen timestamp of the domain in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`registrar` |  `string` Registrar name . FOr example, "Wild West Domains, Inc. (R120-LROR)", "GoDaddy.com, LLC", or "PDR LTD. D/B/A PUBLICDOMAINREGISTRY.COM".  
`contactEmail` |  `string` Contact email address.  
`whoisServer` |  `string` Whois server name.  
`nameServer[]` |  `string` Repeated list of name servers.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Domain creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last updated time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Expiration time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`auditUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Audit updated time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `string` Domain status. See [](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en)<https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en> for meanings of possible values  
`registrant` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Parsed contact information for the registrant of the domain.  
`admin` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Parsed contact information for the administrative contact for the domain.  
`tech` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Parsed contact information for the technical contact for the domain  
`billing` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Parsed contact information for the billing contact of the domain.  
`zone` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` Parsed contact information for the zone.  
`whoisRecordRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` WHOIS raw text.A base64-encoded string.  
`registryDataRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Registry Data raw text.A base64-encoded string.  
`ianaRegistrarId` |  `integer` IANA Registrar ID. See [](https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml)<https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml>  
`privateRegistration` |  `boolean` Indicates whether the domain appears to be using a private registration service to mask the owner's contact information.  
`categories[]` |  `string` Categories assign to the domain as retrieved from VirusTotal.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon)`)` Includes difference hash and MD5 hash of the domain's favicon.  
`jarm` |  `string` Domain's JARM hash.  
`lastDnsRecords[]` |  `object (`[DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DNSRecord)`)` Domain's DNS records from the last scan.  
`lastDnsRecordsTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date when the DNS records list was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SSLCertificate)`)` SSL certificate object retrieved last time the domain was analyzed.  
`lastHttpsCertificateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the certificate was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`popularityRanks[]` |  `object (`[PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PopularityRank)`)` Domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc  
`tags[]` |  `string` List of representative attributes.  
`whoisTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date of the last update of the WHOIS record.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Prevalence

JSON representation  
---  
      
    
    {
      "rollingMax": integer,
      "dayCount": integer,
      "rollingMaxSubDomains": integer,
      "dayMax": integer,
      "dayMaxSubDomains": integer
    }  
  
Fields  
---  
`rollingMax` |  `integer` The maximum number of assets per day accessing the resource over the trailing day_count days.  
`dayCount` |  `integer` The number of days over which rolling_max is calculated.  
`rollingMaxSubDomains` |  `integer` The maximum number of assets per day accessing the domain along with sub-domains over the trailing day_count days. This field is only valid for domains.  
`dayMax` |  `integer` The max prevalence score in a day interval window.  
`dayMaxSubDomains` |  `integer` The max prevalence score in a day interval window across sub-domains. This field is only valid for domains.  
  
### User

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "userid": string,
      "userDisplayName": string,
      "firstName": string,
      "middleName": string,
      "lastName": string,
      "phoneNumbers": [
        string
      ],
      "personalAddress": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute))
      },
      "firstSeenTime": string,
      "accountType": enum (AccountType),
      "groupid": string,
      "groupIdentifiers": [
        string
      ],
      "windowsSid": string,
      "emailAddresses": [
        string
      ],
      "employeeId": string,
      "title": string,
      "companyName": string,
      "department": [
        string
      ],
      "officeAddress": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "managers": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User))
        }
      ],
      "hireDate": string,
      "terminationDate": string,
      "timeOff": [
        {
          object ([TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.TimeOff))
        }
      ],
      "lastLoginTime": string,
      "lastPasswordChangeTime": string,
      "passwordExpirationTime": string,
      "accountExpirationTime": string,
      "accountLockoutTime": string,
      "lastBadPasswordAttemptTime": string,
      "userAuthenticationStatus": enum (AuthenticationStatus),
      "roleName": string,
      "roleDescription": string,
      "userRole": enum (Role)
    }  
  
Fields  
---  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (e.g. a GUID, LDAP, OID, or similar). This field can be used as an entity indicator for user entities.  
`userid` |  `string` The ID of the user. This field can be used as an entity indicator for user entities.  
`userDisplayName` |  `string` The display name of the user (e.g. "John Locke").  
`firstName` |  `string` First name of the user (e.g. "John").  
`middleName` |  `string` Middle name of the user.  
`lastName` |  `string` Last name of the user (e.g. "Locke").  
`phoneNumbers[]` |  `string` Phone numbers for the user.  
`personalAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Personal address of the user.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute)`)` Generic entity metadata attributes of the user.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountType` |  `enum (`AccountType`)` Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: [](https://attack.mitre.org/techniques/T1078/)<https://attack.mitre.org/techniques/T1078/>  
`groupid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the group that the user belongs to. Deprecated in favor of the repeated group_identifiers field.  
`groupIdentifiers[]` |  `string` Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).  
`windowsSid` |  `string` The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.  
`emailAddresses[]` |  `string` Email addresses of the user. This field can be used as an entity indicator for user entities.  
`employeeId` |  `string` Human capital management identifier. This field can be used as an entity indicator for user entities.  
`title` |  `string` User job title.  
`companyName` |  `string` User job company name.  
`department[]` |  `string` User job department  
`officeAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` User job office location.  
`managers[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.User)`)` User job manager(s).  
`hireDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment hire date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`terminationDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment termination date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeOff[]` |  `object (`[TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.TimeOff)`)` User time off leaves from active work.  
`lastLoginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last login timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastPasswordChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last password change timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`passwordExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User password expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountLockoutTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account lockout timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBadPasswordAttemptTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last bad password attempt timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userAuthenticationStatus` |  `enum (`AuthenticationStatus`)` System authentication status for user.  
`roleName  
**(deprecated)**` |  `string` This item is deprecated!System role name for user. Deprecated: use attribute.roles.  
`roleDescription  
**(deprecated)**` |  `string` This item is deprecated!System role description for user. Deprecated: use attribute.roles.  
`userRole  
**(deprecated)**` |  `enum (`Role`)` This item is deprecated!System role for user. Deprecated: use attribute.roles.  
  
### Location

JSON representation  
---  
      
    
    {
      "city": string,
      "state": string,
      "countryOrRegion": string,
      "name": string,
      "deskName": string,
      "floorName": string,
      "regionLatitude": number,
      "regionLongitude": number,
      "regionCoordinates": {
        object ([LatLng](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.LatLng))
      }
    }  
  
Fields  
---  
`city` |  `string` The city.  
`state` |  `string` The state.  
`countryOrRegion` |  `string` The country or region.  
`name` |  `string` Custom location name (e.g. building or site name like "London Office"). For cloud environments, this is the region (e.g. "us-west2").  
`deskName` |  `string` Desk name or individual location, typically for an employee in an office. (e.g. "IN-BLR-BCPC-11-1121D").  
`floorName` |  `string` Floor name, number or a combination of the two for a building. (e.g. "1-A").  
`regionLatitude  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: use region_coordinates.  
`regionLongitude  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: use region_coordinates.  
`regionCoordinates` |  `object (`[LatLng](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.LatLng)`)` Coordinates for the associated region. See [](https://cloud.google.com/vision/docs/reference/rest/v1/LatLng)<https://cloud.google.com/vision/docs/reference/rest/v1/LatLng> for a description of the fields.  
  
### LatLng

JSON representation  
---  
      
    
    {
      "latitude": number,
      "longitude": number
    }  
  
Fields  
---  
`latitude` |  `number` The latitude in degrees. It must be in the range [-90.0, +90.0].  
`longitude` |  `number` The longitude in degrees. It must be in the range [-180.0, +180.0].  
  
### Attribute

JSON representation  
---  
      
    
    {
      "cloud": {
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cloud))
      },
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Permission))
        }
      ],
      "roles": [
        {
          object ([Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Role))
        }
      ],
      "creationTime": string,
      "lastUpdateTime": string
    }  
  
Fields  
---  
`cloud` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cloud)`)` Cloud metadata attributes such as project ID, account ID, or organizational hierarchy.  
`labels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` Set of labels for the entity. Should only be used for product labels (for example, Google Cloud resource labels or Azure AD sensitivity labels. Should not be used for arbitrary key-value mappings.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Permission)`)` System permissions for IAM entity (human principal, service account, group).  
`roles[]` |  `object (`[Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Role)`)` System IAM roles to be assumed by resources to use the role's permissions for access control.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was created or provisioned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Cloud

JSON representation  
---  
      
    
    {
      "environment": enum (CloudEnvironment),
      "vpc": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource))
      },
      "project": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource))
      },
      "availabilityZone": string
    }  
  
Fields  
---  
`environment` |  `enum (`CloudEnvironment`)` The Cloud environment.  
`vpc  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource)`)` This item is deprecated!The cloud environment VPC. Deprecated.  
`project  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Resource)`)` This item is deprecated!The cloud environment project information. Deprecated: Use Resource.resource_ancestors  
`availabilityZone` |  `string` The cloud environment availability zone (different from region which is location.name).  
  
### Resource

JSON representation  
---  
      
    
    {
      "type": string,
      "resourceType": enum (ResourceType),
      "resourceSubtype": string,
      "id": string,
      "name": string,
      "parent": string,
      "productObjectId": string,
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute))
      },
      "scheduledTask": {
        object ([ScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ScheduledTask))
      },
      "volume": {
        object ([Volume](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Volume))
      },
      "service": {
        object ([Service](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Service))
      }
    }  
  
Fields  
---  
`type  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use resource_type instead.  
`resourceType` |  `enum (`ResourceType`)` Resource type.  
`resourceSubtype` |  `string` Resource sub-type (e.g. "BigQuery", "Bigtable").  
`id  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use resource.name or resource.product_object_id.  
`name` |  `string` The full name of the resource. For example, Google Cloud: //cloudresourcemanager.googleapis.com/projects/wombat-123, and AWS: arn:aws:iam::123456789012:user/johndoe.  
`parent  
**(deprecated)**` |  `string` This item is deprecated!The parent of the resource. For a database table, the parent is the database. For a storage object, the bucket name. Deprecated: use resource_ancestors.name.  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (a GUID, OID, or similar) This field can be used as an entity indicator for a Resource entity.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute)`)` Generic entity metadata attributes of the resource.  
`scheduledTask` |  `object (`[ScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ScheduledTask)`)` Information about a scheduled task associated with the resource.  
`volume` |  `object (`[Volume](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Volume)`)` Information about a storage volume associated with the resource.  
`service` |  `object (`[Service](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Service)`)` Information about a Windows service associated with the resource.  
  
### ScheduledTask

JSON representation  
---  
      
    
    {
      "minute": integer,
      "hour": integer,
      "monthDay": integer,
      "month": integer,
      "weekDay": integer,
      "comment": string,
      "author": string
    }  
  
Fields  
---  
`minute` |  `integer` The minute of the hour (0-59).  
`hour` |  `integer` The hour of the day (0-23).  
`monthDay` |  `integer` The day of the month (1-31).  
`month` |  `integer` The month of the year (1-12).  
`weekDay` |  `integer` The day of the week (0-6, Sunday=0).  
`comment` |  `string` A comment or description for the task.  
`author` |  `string` The author or creator of the task.  
  
### Volume

JSON representation  
---  
      
    
    {
      "fileSystem": string,
      "mountPoint": string,
      "devicePath": string,
      "isMounted": boolean,
      "isReadOnly": boolean,
      "name": string
    }  
  
Fields  
---  
`fileSystem` |  `string` The name of the file system on the volume (e.g., "NTFS", "FAT32").  
`mountPoint` |  `string` The path where the volume is mounted (e.g., "C:", "/mnt/data").  
`devicePath` |  `string` The system path to the device (e.g., "\\.\HarddiskVolume1", "/dev/sda1").  
`isMounted` |  `boolean` Indicates whether the volume is currently mounted.  
`isReadOnly` |  `boolean` Indicates whether the volume is mounted as read-only.  
`name` |  `string` The user-assigned label or name for the volume.  
  
### Service

JSON representation  
---  
      
    
    {
      "displayName": string,
      "serviceType": enum (ServiceType),
      "startupType": enum (StartupType),
      "state": enum (State)
    }  
  
Fields  
---  
`displayName` |  `string` The user-friendly display name of the service.  
`serviceType` |  `enum (`ServiceType`)` The type of service.  
`startupType` |  `enum (`StartupType`)` The startup type of the service.  
`state` |  `enum (`State`)` Output only. The status of the service.  
  
### Label

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "source": string,
      "rbacEnabled": boolean
    }  
  
Fields  
---  
`key` |  `string` The key.  
`value` |  `string` The value.  
`source` |  `string` Where the label is derived from.  
`rbacEnabled` |  `boolean` Indicates whether this label can be used for Data RBAC  
  
### Permission

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum (PermissionType)
    }  
  
Fields  
---  
`name` |  `string` Name of the permission (e.g. chronicle.analyst.updateRule).  
`description` |  `string` Description of the permission (e.g. 'Ability to update detect rules').  
`type` |  `enum (`PermissionType`)` Type of the permission.  
  
### Role

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum (Type)
    }  
  
Fields  
---  
`name` |  `string` System role name for user.  
`description` |  `string` System role description for user.  
`type` |  `enum (`Type`)` System role type for well known roles.  
  
### TimeOff

JSON representation  
---  
      
    
    {
      "interval": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval))
      },
      "description": string
    }  
  
Fields  
---  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval)`)` Interval duration of the leave.  
`description` |  `string` Description of the leave if available (e.g. 'Vacation').  
  
### Favicon

JSON representation  
---  
      
    
    {
      "rawMd5": string,
      "dhash": string
    }  
  
Fields  
---  
`rawMd5` |  `string` Favicon's MD5 hash.  
`dhash` |  `string` Difference hash.  
  
### DNSRecord

JSON representation  
---  
      
    
    {
      "type": string,
      "value": string,
      "ttl": string,
      "priority": string,
      "retry": string,
      "refresh": string,
      "minimum": string,
      "expire": string,
      "serial": string,
      "rname": string
    }  
  
Fields  
---  
`type` |  `string` Type.  
`value` |  `string` Value.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Time to live.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`priority` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Priority.  
`retry` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Retry.  
`refresh` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Refresh.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`minimum` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`expire` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Expire.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`serial` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Serial.  
`rname` |  `string` Rname.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### SSLCertificate

JSON representation  
---  
      
    
    {
      "certSignature": {
        object ([CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.CertSignature))
      },
      "extension": {
        object ([Extension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Extension))
      },
      "certExtensions": {
        object
      },
      "firstSeenTime": string,
      "issuer": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Subject))
      },
      "ec": {
        object ([EC](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EC))
      },
      "serialNumber": string,
      "signatureAlgorithm": string,
      "size": string,
      "subject": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Subject))
      },
      "thumbprint": string,
      "thumbprintSha256": string,
      "validity": {
        object ([Validity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Validity))
      },
      "version": string,
      "publicKey": {
        object ([PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PublicKey))
      }
    }  
  
Fields  
---  
`certSignature` |  `object (`[CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.CertSignature)`)` Certificate's signature and algorithm.  
`extension  
**(deprecated)**` |  `object (`[Extension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Extension)`)` This item is deprecated!(DEPRECATED) certificate's extension.  
`certExtensions` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Certificate's extensions.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date the certificate was first retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issuer` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Subject)`)` Certificate's issuer data.  
`ec` |  `object (`[EC](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EC)`)` EC public key information.  
`serialNumber` |  `string` Certificate's serial number hexdump.  
`signatureAlgorithm` |  `string` Algorithm used for the signature (for example, "sha1RSA").  
`size` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Certificate content length.  
`subject` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Subject)`)` Certificate's subject data.  
`thumbprint` |  `string` Certificate's content SHA1 hash.  
`thumbprintSha256` |  `string` Certificate's content SHA256 hash.  
`validity` |  `object (`[Validity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Validity)`)` Certificate's validity period.  
`version` |  `string` Certificate version (typically "V1", "V2" or "V3").  
`publicKey` |  `object (`[PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PublicKey)`)` Public key information.  
  
### CertSignature

JSON representation  
---  
      
    
    {
      "signature": string,
      "signatureAlgorithm": string
    }  
  
Fields  
---  
`signature` |  `string` Signature.  
`signatureAlgorithm` |  `string` Algorithm.  
  
### Extension

JSON representation  
---  
      
    
    {
      "ca": boolean,
      "subjectKeyId": string,
      "authorityKeyId": {
        object ([AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AuthorityKeyId))
      },
      "keyUsage": string,
      "caInfoAccess": string,
      "crlDistributionPoints": string,
      "extendedKeyUsage": string,
      "subjectAlternativeName": string,
      "certificatePolicies": string,
      "netscapeCertComment": string,
      "certTemplateNameDc": string,
      "netscapeCertificate": boolean,
      "peLogotype": boolean,
      "oldAuthorityKeyId": boolean
    }  
  
Fields  
---  
`ca` |  `boolean` Whether the subject acts as a certificate authority (CA) or not.  
`subjectKeyId` |  `string` Identifies the public key being certified.  
`authorityKeyId` |  `object (`[AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AuthorityKeyId)`)` Identifies the public key to be used to verify the signature on this certificate or CRL.  
`keyUsage` |  `string` The purpose for which the certified public key is used.  
`caInfoAccess` |  `string` Authority information access locations are URLs that are added to a certificate in its authority information access extension.  
`crlDistributionPoints` |  `string` CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.  
`extendedKeyUsage` |  `string` One or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.  
`subjectAlternativeName` |  `string` Contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.  
`certificatePolicies` |  `string` Different certificate policies will relate to different applications which may use the certified key.  
`netscapeCertComment` |  `string` Used to include free-form text comments inside certificates.  
`certTemplateNameDc` |  `string` BMP data value "DomainController". See MS Q291010.  
`netscapeCertificate` |  `boolean` Identify whether the certificate subject is an SSL client, an SSL server, or a CA.  
`peLogotype` |  `boolean` Whether the certificate includes a logotype.  
`oldAuthorityKeyId` |  `boolean` Whether the certificate has an old authority key identifier extension.  
  
### AuthorityKeyId

JSON representation  
---  
      
    
    {
      "keyid": string,
      "serialNumber": string
    }  
  
Fields  
---  
`keyid` |  `string` Key hexdump.  
`serialNumber` |  `string` Serial number hexdump.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a null value.  
`numberValue` |  `number` Represents a double value.  
`stringValue` |  `string` Represents a string value.  
`boolValue` |  `boolean` Represents a boolean value.  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a structured value.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a repeated `Value`.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### Subject

JSON representation  
---  
      
    
    {
      "countryName": string,
      "commonName": string,
      "locality": string,
      "organization": string,
      "organizationalUnit": string,
      "stateOrProvinceName": string
    }  
  
Fields  
---  
`countryName` |  `string` C: Country name.  
`commonName` |  `string` CN: CommonName.  
`locality` |  `string` L: Locality.  
`organization` |  `string` O: Organization.  
`organizationalUnit` |  `string` OU: OrganizationalUnit.  
`stateOrProvinceName` |  `string` ST: StateOrProvinceName.  
  
### EC

JSON representation  
---  
      
    
    {
      "oid": string,
      "pub": string
    }  
  
Fields  
---  
`oid` |  `string` Curve name.  
`pub` |  `string` Public key hexdump.  
  
### Validity

JSON representation  
---  
      
    
    {
      "expiryTime": string,
      "issueTime": string
    }  
  
Fields  
---  
`expiryTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Expiry date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issueTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Issue date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### PublicKey

JSON representation  
---  
      
    
    {
      "algorithm": string,
      "rsa": {
        object ([RSA](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RSA))
      }
    }  
  
Fields  
---  
`algorithm` |  `string` Any of "RSA", "DSA" or "EC". Indicates the algorithm used to generate the certificate.  
`rsa` |  `object (`[RSA](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RSA)`)` RSA public key information.  
  
### RSA

JSON representation  
---  
      
    
    {
      "keySize": string,
      "modulus": string,
      "exponent": string
    }  
  
Fields  
---  
`keySize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Key size.  
`modulus` |  `string` Key modulus hexdump.  
`exponent` |  `string` Key exponent hexdump.  
  
### PopularityRank

JSON representation  
---  
      
    
    {
      "giver": string,
      "rank": string,
      "ingestionTime": string
    }  
  
Fields  
---  
`giver` |  `string` Name of the rank serial number hexdump.  
`rank` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Rank position.  
`ingestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the rank was ingested.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Artifact

JSON representation  
---  
      
    
    {
      "ip": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network))
      },
      "asOwner": string,
      "asn": string,
      "jarm": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SSLCertificate))
      },
      "lastHttpsCertificateDate": string,
      "regionalInternetRegistry": string,
      "tags": [
        string
      ],
      "whois": string,
      "whoisDate": string,
      "tunnels": [
        {
          object ([Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tunnels))
        }
      ],
      "anonymous": boolean,
      "artifactClient": {
        object ([ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ArtifactClient))
      },
      "risks": [
        string
      ]
    }  
  
Fields  
---  
`ip` |  `string` IP address of the artifact. This field can be used as an entity indicator for an external destination IP entity.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence)`)` The prevalence of the artifact within the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First seen timestamp of the IP in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last seen timestamp of the IP address in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Location of the Artifact's IP address.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network)`)` Network information related to the Artifact's IP address.  
`asOwner` |  `string` Owner of the Autonomous System to which the IP address belongs.  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Autonomous System Number to which the IP address belongs.  
`jarm` |  `string` The JARM hash for the IP address. (<https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a)>.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SSLCertificate)`)` SSL certificate information about the IP address.  
`lastHttpsCertificateDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Most recent date for the certificate in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`regionalInternetRegistry` |  `string` RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).  
`tags[]` |  `string` Identification attributes  
`whois` |  `string` WHOIS information as returned from the pertinent WHOIS server.  
`whoisDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date of the last update of the WHOIS record in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tunnels[]` |  `object (`[Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tunnels)`)` VPN tunnels.  
`anonymous` |  `boolean` Whether the VPN tunnels are configured for anonymous browsing or not.  
`artifactClient` |  `object (`[ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ArtifactClient)`)` Entity or software accessing or utilizing network resources.  
`risks[]` |  `string` This field lists potential risks associated with the network activity.  
  
### Network

JSON representation  
---  
      
    
    {
      "sentBytes": string,
      "receivedBytes": string,
      "totalBytes": string,
      "sentPackets": string,
      "receivedPackets": string,
      "sessionDuration": string,
      "sessionId": string,
      "parentSessionId": string,
      "applicationProtocolVersion": string,
      "communityId": string,
      "direction": enum (Direction),
      "ipProtocol": enum (IpProtocol),
      "applicationProtocol": enum (ApplicationProtocol),
      "ftp": {
        object ([Ftp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Ftp))
      },
      "email": {
        object ([Email](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Email))
      },
      "dns": {
        object ([Dns](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Dns))
      },
      "dhcp": {
        object ([Dhcp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Dhcp))
      },
      "http": {
        object ([Http](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Http))
      },
      "tls": {
        object ([Tls](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tls))
      },
      "smtp": {
        object ([Smtp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Smtp))
      },
      "asn": string,
      "dnsDomain": string,
      "carrierName": string,
      "organizationName": string,
      "ipSubnetRange": string,
      "isProxy": boolean,
      "proxyInfo": {
        object ([ProxyInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ProxyInfo))
      },
      "connectionState": enum (ConnectionState)
    }  
  
Fields  
---  
`sentBytes` |  `string` The number of bytes sent.  
`receivedBytes` |  `string` The number of bytes received.  
`totalBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of total bytes.  
`sentPackets` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of packets sent.  
`receivedPackets` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of packets received.  
`sessionDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of the session as the number of seconds and nanoseconds. For seconds, network.session_duration.seconds, the type is a 64-bit integer. For nanoseconds, network.session_duration.nanos, the type is a 32-bit integer.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`sessionId` |  `string` The ID of the network session.  
`parentSessionId` |  `string` The ID of the parent network session.  
`applicationProtocolVersion` |  `string` The version of the application protocol. e.g. "1.1, 2.0"  
`communityId` |  `string` Community ID network flow value.  
`direction` |  `enum (`Direction`)` The direction of network traffic.  
`ipProtocol` |  `enum (`IpProtocol`)` The IP protocol.  
`applicationProtocol` |  `enum (`ApplicationProtocol`)` The application protocol.  
`ftp` |  `object (`[Ftp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Ftp)`)` FTP info.  
`email` |  `object (`[Email](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Email)`)` Email info for the sender/recipient.  
`dns` |  `object (`[Dns](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Dns)`)` DNS info.  
`dhcp` |  `object (`[Dhcp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Dhcp)`)` DHCP info.  
`http` |  `object (`[Http](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Http)`)` HTTP info.  
`tls` |  `object (`[Tls](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tls)`)` TLS info.  
`smtp` |  `object (`[Smtp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Smtp)`)` SMTP info. Store fields specific to SMTP not covered by Email.  
`asn` |  `string` Autonomous system number.  
`dnsDomain` |  `string` DNS domain name.  
`carrierName` |  `string` Carrier identification.  
`organizationName` |  `string` Organization name (e.g Google).  
`ipSubnetRange` |  `string` Associated human-readable IP subnet range (e.g. 10.1.2.0/24).  
`isProxy` |  `boolean` Whether the IP address is a known proxy.  
`proxyInfo` |  `object (`[ProxyInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ProxyInfo)`)` Proxy information. Only set if is_proxy is true.  
`connectionState` |  `enum (`ConnectionState`)` Output only. The state of the network connection.  
  
### Ftp

JSON representation  
---  
      
    
    {
      "command": string
    }  
  
Fields  
---  
`command` |  `string` The FTP command.  
  
### Email

JSON representation  
---  
      
    
    {
      "from": string,
      "replyTo": string,
      "to": [
        string
      ],
      "cc": [
        string
      ],
      "bcc": [
        string
      ],
      "mailId": string,
      "subject": [
        string
      ],
      "bounceAddress": string
    }  
  
Fields  
---  
`from` |  `string` The 'from' address.  
`replyTo` |  `string` The 'reply to' address.  
`to[]` |  `string` A list of 'to' addresses.  
`cc[]` |  `string` A list of 'cc' addresses.  
`bcc[]` |  `string` A list of 'bcc' addresses.  
`mailId` |  `string` The mail (or message) ID.  
`subject[]` |  `string` The subject line(s) of the email.  
`bounceAddress` |  `string` The envelope from address. [](https://en.wikipedia.org/wiki/Bounce_address)<https://en.wikipedia.org/wiki/Bounce_address>  
  
### Dns

JSON representation  
---  
      
    
    {
      "id": integer,
      "response": boolean,
      "opcode": integer,
      "authoritative": boolean,
      "truncated": boolean,
      "recursionDesired": boolean,
      "recursionAvailable": boolean,
      "responseCode": integer,
      "questions": [
        {
          object ([Question](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Question))
        }
      ],
      "answers": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord))
        }
      ],
      "authority": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord))
        }
      ],
      "additional": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord))
        }
      ]
    }  
  
Fields  
---  
`id` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` DNS query id.  
`response` |  `boolean` Set to true if the event is a DNS response. See QR field from RFC1035.  
`opcode` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The DNS OpCode used to specify the type of DNS query (for example, QUERY, IQUERY, or STATUS).  
`authoritative` |  `boolean` Other DNS header flags. See RFC1035, section 4.1.1.  
`truncated` |  `boolean` Whether the DNS response was truncated.  
`recursionDesired` |  `boolean` Whether a recursive DNS lookup is desired.  
`recursionAvailable` |  `boolean` Whether a recursive DNS lookup is available.  
`responseCode` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Response code. See RCODE from RFC1035.  
`questions[]` |  `object (`[Question](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Question)`)` A list of domain protocol message questions.  
`answers[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord)`)` A list of answers to the domain name query.  
`authority[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord)`)` A list of domain name servers which verified the answers to the domain name queries.  
`additional[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ResourceRecord)`)` A list of additional domain name servers that can be used to verify the answer to the domain.  
  
### Question

JSON representation  
---  
      
    
    {
      "name": string,
      "type": integer,
      "class": integer,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence))
      }
    }  
  
Fields  
---  
`name` |  `string` The domain name.  
`type` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the type of the query.  
`class` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the class of the query.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence)`)` The prevalence of the domain within the customer's environment.  
  
### ResourceRecord

JSON representation  
---  
      
    
    {
      "name": string,
      "type": integer,
      "class": integer,
      "ttl": integer,
      "data": string,
      "binaryData": string
    }  
  
Fields  
---  
`name` |  `string` The name of the owner of the resource record.  
`type` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the type of the resource record.  
`class` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the class of the resource record.  
`ttl` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The time interval for which the resource record can be cached before the source of the information should again be queried.  
`data` |  `string` The payload or response to the DNS question for all responses encoded in UTF-8 format  
`binaryData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw bytes of any non-UTF8 strings that might be included as part of a DNS response.A base64-encoded string.  
  
### Dhcp

JSON representation  
---  
      
    
    {
      "opcode": enum (OpCode),
      "htype": integer,
      "hlen": integer,
      "hops": integer,
      "transactionId": integer,
      "seconds": integer,
      "flags": integer,
      "ciaddr": string,
      "yiaddr": string,
      "siaddr": string,
      "giaddr": string,
      "chaddr": string,
      "sname": string,
      "file": string,
      "options": [
        {
          object ([Option](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Option))
        }
      ],
      "type": enum (MessageType),
      "leaseTimeSeconds": integer,
      "clientHostname": string,
      "clientIdentifier": string,
      "requestedAddress": string,
      "clientIdentifierString": string
    }  
  
Fields  
---  
`opcode` |  `enum (`OpCode`)` The BOOTP op code.  
`htype` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Hardware address type.  
`hlen` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Hardware address length.  
`hops` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Hardware ops.  
`transactionId` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Transaction ID.  
`seconds` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Seconds elapsed since client began address acquisition/renewal process.  
`flags` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Flags.  
`ciaddr` |  `string` Client IP address (ciaddr).  
`yiaddr` |  `string` Your IP address (yiaddr).  
`siaddr` |  `string` IP address of the next bootstrap server.  
`giaddr` |  `string` Relay agent IP address (giaddr).  
`chaddr` |  `string` Client hardware address (chaddr).  
`sname` |  `string` Server name that the client wishes to boot from.  
`file` |  `string` Boot image filename.  
`options[]` |  `object (`[Option](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Option)`)` List of DHCP options.  
`type` |  `enum (`MessageType`)` DHCP message type.  
`leaseTimeSeconds` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Lease time in seconds. See RFC2132, section 9.2.  
`clientHostname` |  `string` Client hostname. See RFC2132, section 3.14.  
`clientIdentifier` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Client identifier. See RFC2132, section 9.14. Note: Make sure to update the client_identifier_string field as well if you update this field.A base64-encoded string.  
`requestedAddress` |  `string` Requested IP address. See RFC2132, section 9.1.  
`clientIdentifierString` |  `string` Client identifier as string. See RFC2132, section 9.14. This field holds the string value of the client_identifier.  
  
### Option

JSON representation  
---  
      
    
    {
      "code": integer,
      "data": string
    }  
  
Fields  
---  
`code` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Code. See RFC1533.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Data.A base64-encoded string.  
  
### Http

JSON representation  
---  
      
    
    {
      "method": string,
      "referralUrl": string,
      "userAgent": string,
      "responseCode": integer,
      "parsedUserAgent": {
        object ([UserAgentProto](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.UserAgentProto))
      }
    }  
  
Fields  
---  
`method` |  `string` The HTTP request method (e.g. "GET", "POST", "PATCH", "DELETE").  
`referralUrl` |  `string` The URL for the HTTP referer.  
`userAgent` |  `string` The User-Agent request header which includes the application type, operating system, software vendor or software version of the requesting software user agent.  
`responseCode` |  `integer` The response status code, for example 200, 302, 404, or 500.  
`parsedUserAgent` |  `object (`[UserAgentProto](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.UserAgentProto)`)` The parsed user_agent string.  
  
### UserAgentProto

JSON representation  
---  
      
    
    {
      "family": enum (Family),
      "subFamily": string,
      "platform": string,
      "device": string,
      "deviceVersion": string,
      "carrier": string,
      "security": string,
      "locale": string,
      "os": string,
      "osVariant": string,
      "browser": string,
      "browserVersion": string,
      "browserEngineVersion": string,
      "googleToolbarVersion": string,
      "javaProfile": string,
      "javaProfileVersion": string,
      "javaConfiguration": string,
      "javaConfigurationVersion": string,
      "messaging": string,
      "messagingVersion": string,
      "annotation": [
        {
          object ([Annotation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Annotation))
        }
      ]
    }  
  
Fields  
---  
`family` |  `enum (`Family`)` User agent family captures the type of browser/app at a high-level e.g. MSIE, Gecko, Safari etc..  
`subFamily` |  `string` Sub-family identifies individual regexps when a family has more than 1. This is used to generate the right UA string from a protobuf. Examples in the AppleWebKit family: Chrome and Safari. Can also be an arbitrary identifier.  
`platform` |  `string` The platform describes the environment in which the browser or app runs. For desktop user agents, Platform is a string describing the OS family e.g. Windows, Macintosh, Linux. For mobile user agents, Platform either describes the OS family (if available) or the hardware maker. e.g. Linux, or HTC, LG, Palm.  
`device` |  `string` (Usually) Mobile specific: name of hardware device, may or may not contain the full model name. e.g. iPhone, Palm750, SPH-M800. Reduced to "K" for Android devices with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`deviceVersion` |  `string` (Usually) Mobile specific: version of hardware device Unavailable with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`carrier` |  `string` Mobile specific: name of mobile carrier  
`security` |  `string` Security level reported by user agent, either U, I or N. Unavailable with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`locale` |  `string` Locale in which the browser is running as country code and optionally language pair. Unavailable with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`os` |  `string` Full name of the operating system e.g. "Darwin/9.7.0", "Android 1.5", "Windows 98" Version is reduced, and other data might also be missing, for reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`osVariant` |  `string` Extra qualifier for the OS e.g. "(i386)", "Build/CUPCAKE", "PalmSource/Palm-D061" Unavailable with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`browser` |  `string` Product brand within the family: Firefox, Netscape, Camino etc.. Or Earth, Windows-Media-Player etc.. for non-browser user agents.  
`browserVersion` |  `string` Minor and lower versions unavailable with reduced User-Agent and no client hints (<https://www.chromium.org/updates/ua-reduction/)>.  
`browserEngineVersion` |  `string` Version of the rendering engine e.g. "8.01" for "Opera/8.01"  
`googleToolbarVersion` |  `string` Version number of GoogleToolbar, if installed. Applies only to MSIE and Firefox at this time.  
`javaProfile` |  `string` Mobile specific: e.g. Profile/MIDP-2.0  
`javaProfileVersion` |  `string`  
`javaConfiguration` |  `string` Mobile specific: e.g. Configuration/CLDC-1.1  
`javaConfigurationVersion` |  `string`  
`messaging` |  `string` Mobile specific: e.g. MMP/2.0  
`messagingVersion` |  `string`  
`annotation[]` |  `object (`[Annotation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Annotation)`)`  
  
### Annotation

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tls

JSON representation  
---  
      
    
    {
      "client": {
        object ([Client](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Client))
      },
      "server": {
        object ([Server](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Server))
      },
      "cipher": string,
      "curve": string,
      "version": string,
      "versionProtocol": string,
      "established": boolean,
      "nextProtocol": string,
      "resumed": boolean
    }  
  
Fields  
---  
`client` |  `object (`[Client](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Client)`)` Certificate information for the client certificate.  
`server` |  `object (`[Server](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Server)`)` Certificate information for the server certificate.  
`cipher` |  `string` Cipher used during the connection.  
`curve` |  `string` Elliptical curve used for a given cipher.  
`version` |  `string` TLS version.  
`versionProtocol` |  `string` Protocol.  
`established` |  `boolean` Indicates whether the TLS negotiation was successful.  
`nextProtocol` |  `string` Protocol to be used for tunnel.  
`resumed` |  `boolean` Indicates whether the TLS connection was resumed from a previous TLS negotiation.  
  
### Client

JSON representation  
---  
      
    
    {
      "certificate": {
        object ([Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Certificate))
      },
      "ja3": string,
      "serverName": string,
      "supportedCiphers": [
        string
      ]
    }  
  
Fields  
---  
`certificate` |  `object (`[Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Certificate)`)` Client certificate.  
`ja3` |  `string` JA3 hash from the TLS ClientHello, as a hex-encoded string.  
`serverName` |  `string` Host name of the server, that the client is connecting to.  
`supportedCiphers[]` |  `string` Ciphers supported by the client during client hello.  
  
### Certificate

JSON representation  
---  
      
    
    {
      "version": string,
      "serial": string,
      "subject": string,
      "issuer": string,
      "md5": string,
      "sha1": string,
      "sha256": string,
      "notBefore": string,
      "notAfter": string
    }  
  
Fields  
---  
`version` |  `string` Certificate version.  
`serial` |  `string` Certificate serial number.  
`subject` |  `string` Subject of the certificate.  
`issuer` |  `string` Issuer of the certificate.  
`md5` |  `string` The MD5 hash of the certificate, as a hex-encoded string.  
`sha1` |  `string` The SHA1 hash of the certificate, as a hex-encoded string.  
`sha256` |  `string` The SHA256 hash of the certificate, as a hex-encoded string.  
`notBefore` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Indicates when the certificate is first valid.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`notAfter` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Indicates when the certificate is no longer valid.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Server

JSON representation  
---  
      
    
    {
      "certificate": {
        object ([Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Certificate))
      },
      "ja3s": string
    }  
  
Fields  
---  
`certificate` |  `object (`[Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Certificate)`)` Server certificate.  
`ja3s` |  `string` JA3 hash from the TLS ServerHello, as a hex-encoded string.  
  
### Smtp

JSON representation  
---  
      
    
    {
      "helo": string,
      "mailFrom": string,
      "rcptTo": [
        string
      ],
      "serverResponse": [
        string
      ],
      "messagePath": string,
      "isWebmail": boolean,
      "isTls": boolean
    }  
  
Fields  
---  
`helo` |  `string` The client's 'HELO'/'EHLO' string.  
`mailFrom` |  `string` The client's 'MAIL FROM' string.  
`rcptTo[]` |  `string` The client's 'RCPT TO' string(s).  
`serverResponse[]` |  `string` The server's response(s) to the client.  
`messagePath` |  `string` The message's path (extracted from the headers).  
`isWebmail` |  `boolean` If the message was sent via a webmail client.  
`isTls` |  `boolean` If the connection switched to TLS.  
  
### ProxyInfo

JSON representation  
---  
      
    
    {
      "anonymous": boolean,
      "anonymousVpn": boolean,
      "publicProxy": boolean,
      "torExitNode": boolean,
      "smartDnsProxy": boolean,
      "hostingProvider": boolean,
      "vpnDatacenter": boolean,
      "residentialProxy": boolean,
      "vpnServiceName": string,
      "proxyOverVpn": boolean,
      "relayProxy": boolean
    }  
  
Fields  
---  
`anonymous` |  `boolean` Whether the IP address is anonymous.  
`anonymousVpn` |  `boolean` Whether the IP address is an anonymous VPN.  
`publicProxy` |  `boolean` Whether the IP address is a public proxy.  
`torExitNode` |  `boolean` Whether the IP address is a tor exit node.  
`smartDnsProxy` |  `boolean` Whether the IP address is a smart DNS proxy.  
`hostingProvider` |  `boolean` Whether the IP address is a hosting provider.  
`vpnDatacenter` |  `boolean` Whether the IP address is a VPN datacenter.  
`residentialProxy` |  `boolean` Whether the IP address is a residential proxy.  
`vpnServiceName` |  `string` The name of the VPN service.  
`proxyOverVpn` |  `boolean` Whether the IP address is a proxy over VPN.  
`relayProxy` |  `boolean` Whether the IP address is a relay proxy.  
  
### Tunnels

JSON representation  
---  
      
    
    {
      "provider": string,
      "type": string
    }  
  
Fields  
---  
`provider` |  `string` The provider of the VPN tunnels being used.  
`type` |  `string` The type of the VPN tunnels.  
  
### ArtifactClient

JSON representation  
---  
      
    
    {
      "behaviors": [
        string
      ],
      "proxies": [
        string
      ]
    }  
  
Fields  
---  
`behaviors[]` |  `string` The behaviors of the client accessing the network.  
`proxies[]` |  `string` The type of proxies used by the client.  
  
### Url

JSON representation  
---  
      
    
    {
      "url": string,
      "categories": [
        string
      ],
      "favicon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon))
      },
      "htmlMeta": {
        object
      },
      "lastFinalUrl": string,
      "lastHttpResponseCode": integer,
      "lastHttpResponseContentLength": string,
      "lastHttpResponseContentSha256": string,
      "lastHttpResponseCookies": {
        object
      },
      "lastHttpResponseHeaders": {
        object
      },
      "tags": [
        string
      ],
      "title": string,
      "trackers": [
        {
          object ([Tracker](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tracker))
        }
      ]
    }  
  
Fields  
---  
`url` |  `string` URL.  
`categories[]` |  `string` Categorisation done by VirusTotal partners.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon)`)` Difference hash and MD5 hash of the URL's.  
`htmlMeta` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Meta tags (only for URLs downloading HTML).  
`lastFinalUrl` |  `string` If the original URL redirects, where does it end.  
`lastHttpResponseCode` |  `integer` HTTP response code of the last response.  
`lastHttpResponseContentLength` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Length in bytes of the content received.  
`lastHttpResponseContentSha256` |  `string` URL response body's SHA256 hash.  
`lastHttpResponseCookies` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Website's cookies.  
`lastHttpResponseHeaders` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Headers and values of the last HTTP response.  
`tags[]` |  `string` Tags.  
`title` |  `string` Webpage title.  
`trackers[]` |  `object (`[Tracker](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tracker)`)` Trackers found in the URL in a historical manner.  
  
### Tracker

JSON representation  
---  
      
    
    {
      "tracker": string,
      "id": string,
      "timestamp": string,
      "url": string
    }  
  
Fields  
---  
`tracker` |  `string` Tracker name.  
`id` |  `string` Tracker ID, if available.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Tracker ingestion date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`url` |  `string` Tracker script URL.  
  
### Browser

JSON representation  
---  
      
    
    {
      "browserType": enum (BrowserType),
      "browserVersion": string,
      "firstVisitTime": string,
      "lastVisitTime": string,
      "profile": string,
      "typed": boolean,
      "visitType": enum (UrlVisitType),
      "hidden": boolean,
      "requestOriginUri": string,
      "visitCount": string,
      "visitCountCriteria": string,
      "indexedContent": string,
      "firstBookmarkedTime": string,
      "cookies": [
        {
          object ([Cookie](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cookie))
        }
      ],
      "typedCount": string,
      "visitSource": enum (VisitSource)
    }  
  
Fields  
---  
`browserType` |  `enum (`BrowserType`)` The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).  
`browserVersion` |  `string` The browser version.  
`firstVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the initial visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the most recent visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`profile` |  `string` The browser profile associated with the history entry.  
`typed` |  `boolean` A boolean value indicating if the URL was typed by the user.  
`visitType` |  `enum (`UrlVisitType`)` Describes the type of navigation or visit (e.g., direct, redirect, etc.).  
`hidden` |  `boolean` A boolean value indicating if the history entry is hidden.  
`requestOriginUri` |  `string` Indicates the URI from which the current visit originated.  
`visitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of times the Url has been visited.  
`visitCountCriteria` |  `string` Describes the criteria used to calculate the visit_count.  
`indexedContent` |  `string` Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.  
`firstBookmarkedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the first time the URL was bookmarked.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cookies[]` |  `object (`[Cookie](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Cookie)`)` Information about the cookies.  
`typedCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the URL was visited with this specific visit type and visit source.  
`visitSource` |  `enum (`VisitSource`)` The source of the visit.  
  
### Cookie

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "domain": string,
      "path": string,
      "expirationTime": string,
      "httpOnly": boolean,
      "secure": boolean,
      "maxAge": string,
      "sameSite": enum (CookieSameSite),
      "session": boolean,
      "partitioned": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique name identifying the cookie.  
`value` |  `string` The data stored within the cookie.  
`domain` |  `string` The domain for which the cookie is valid.  
`path` |  `string` The URL path for which the cookie is valid.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The date and time when the cookie will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`httpOnly` |  `boolean` Indicates if the cookie is inaccessible via client-side scripts (e.g., JavaScript).  
`secure` |  `boolean` Indicates if the cookie should only be sent over secure HTTPS connections.  
`maxAge` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum age of the cookie in seconds.  
`sameSite` |  `enum (`CookieSameSite`)` Affects cross-site request behavior.  
`session` |  `boolean` Indicates if the cookie is persistent.  
`partitioned` |  `boolean` Shows if the cookies is stored using partitioned storage.  
  
### Group

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "creationTime": string,
      "groupDisplayName": string,
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute))
      },
      "emailAddresses": [
        string
      ],
      "windowsSid": string
    }  
  
Fields  
---  
`productObjectId` |  `string` Product globally unique user object identifier, such as an LDAP Object Identifier.  
`creationTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`groupDisplayName` |  `string` Group display name. e.g. "Finance".  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute)`)` Generic entity metadata attributes of the group.  
`emailAddresses[]` |  `string` Email addresses of the group.  
`windowsSid` |  `string` Microsoft Windows SID of the group.  
  
### Process

JSON representation  
---  
      
    
    {
      "pid": string,
      "parentPid": string,
      "parentProcess": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process))
      },
      "file": {
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.File))
      },
      "commandLine": string,
      "commandLineHistory": [
        string
      ],
      "productSpecificProcessId": string,
      "accessMask": string,
      "integrityLevelRid": string,
      "euid": string,
      "ruid": string,
      "egid": string,
      "rgid": string,
      "pgid": string,
      "sessionLeaderPid": string,
      "tty": string,
      "tokenElevationType": enum (TokenElevationType),
      "productSpecificParentProcessId": string,
      "ipv6": boolean,
      "kernelDuration": string,
      "userDuration": string,
      "realDuration": string
    }  
  
Fields  
---  
`pid` |  `string` The process ID. This field can be used as an entity indicator for process entities.  
`parentPid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the parent process. Deprecated: use parent_process.pid instead.  
`parentProcess` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Process)`)` Information about the parent process.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.File)`)` Information about the file in use by the process.  
`commandLine` |  `string` The command line command that created the process. This field can be used as an entity indicator for process entities.  
`commandLineHistory[]` |  `string` The command line history of the process.  
`productSpecificProcessId` |  `string` A product specific process id.  
`accessMask` |  `string` A bit mask representing the level of access.  
`integrityLevelRid` |  `string` The Microsoft Windows integrity level relative ID (RID) of the process.  
`euid` |  `string` The effective user ID of the process.  
`ruid` |  `string` The real user ID of the process.  
`egid` |  `string` The effective group ID of the process.  
`rgid` |  `string` The real group ID of the process.  
`pgid` |  `string` The identifier that points to the process group ID leader.  
`sessionLeaderPid` |  `string` The process ID of the session leader process.  
`tty` |  `string` The teletype terminal which the command was executed within.  
`tokenElevationType` |  `enum (`TokenElevationType`)` The elevation type of the process on Microsoft Windows. This determines if any privileges are removed when UAC is enabled.  
`productSpecificParentProcessId  
**(deprecated)**` |  `string` This item is deprecated!A product specific id for the parent process. Please use parent_process.product_specific_process_id instead.  
`ipv6` |  `boolean` This is used to determine if the process is an IPv6 process.  
`kernelDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The kernel time spent in the process.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`userDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The user time spent in the process.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`realDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The real time spent in the process. This is the sum of the kernel and user time.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### File

JSON representation  
---  
      
    
    {
      "sha256": string,
      "md5": string,
      "sha1": string,
      "size": string,
      "fullPath": string,
      "mimeType": string,
      "fileMetadata": {
        object ([FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadata))
      },
      "securityResult": {
        object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
      },
      "peFile": {
        object ([FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataPE))
      },
      "ssdeep": string,
      "vhash": string,
      "ahash": string,
      "authentihash": string,
      "symhash": string,
      "prefetchFileMetadata": {
        object ([PrefetchFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PrefetchFileMetadata))
      },
      "fileType": enum (FileType),
      "capabilitiesTags": [
        string
      ],
      "names": [
        string
      ],
      "tags": [
        string
      ],
      "lastModificationTime": string,
      "createTime": string,
      "lastAccessTime": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "statMode": string,
      "statInode": string,
      "statDev": string,
      "statNlink": string,
      "statFlags": integer,
      "lastAnalysisTime": string,
      "embeddedUrls": [
        string
      ],
      "embeddedDomains": [
        string
      ],
      "embeddedIps": [
        string
      ],
      "exifInfo": {
        object ([ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ExifInfo))
      },
      "signatureInfo": {
        object ([SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SignatureInfo))
      },
      "pdfInfo": {
        object ([PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PDFInfo))
      },
      "firstSubmissionTime": string,
      "lastSubmissionTime": string,
      "mainIcon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon))
      },
      "ntfs": {
        object ([NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.NtfsFileMetadata))
      },
      "appCompatCache": {
        object ([AppCompatMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AppCompatMetadata))
      }
    }  
  
Fields  
---  
`sha256` |  `string` The SHA256 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`md5` |  `string` The MD5 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`sha1` |  `string` The SHA1 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`size` |  `string` The size of the file in bytes.  
`fullPath` |  `string` The full path identifying the location of the file on the system. This field can be used as an entity indicator for file entities.  
`mimeType` |  `string` The MIME (Multipurpose Internet Mail Extensions) type of the file, for example "PE", "PDF", or "powershell script".  
`fileMetadata  
**(deprecated)**` |  `object (`[FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadata)`)` This item is deprecated!Metadata associated with the file. Deprecate FileMetadata in favor of using fields in File.  
`securityResult` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` Google Cloud Threat Intelligence (GCTI) security result for the file including threat context and detection metadata.  
`peFile` |  `object (`[FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataPE)`)` Metadata about the Portable Executable (PE) file.  
`ssdeep` |  `string` Ssdeep of the file  
`vhash` |  `string` Vhash of the file.  
`ahash  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. Use authentihash instead.  
`authentihash` |  `string` Authentihash of the file.  
`symhash` |  `string` SymHash of the file. Used for Mach-O (e.g. MacOS) binaries, to identify similar files based on their symbol table.  
`prefetchFileMetadata` |  `object (`[PrefetchFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PrefetchFileMetadata)`)` Metadata about the prefetch file.  
`fileType` |  `enum (`FileType`)` FileType field.  
`capabilitiesTags[]` |  `string` Capabilities tags.  
`names[]` |  `string` Names fields.  
`tags[]` |  `string` Tags for the file.  
`lastModificationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastAccessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was accessed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Prevalence)`)` Prevalence of the file hash in the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was first seen in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was last seen in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`statMode` |  `string` The mode of the file. A bit string indicating the permissions and privileges of the file.  
`statInode` |  `string` The file identifier. Unique identifier of object within a file system.  
`statDev` |  `string` The file system identifier to which the object belongs.  
`statNlink` |  `string` Number of links to file.  
`statFlags` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` User defined flags for file.  
`lastAnalysisTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was last analysed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`embeddedUrls[]` |  `string` Embedded urls found in the file.  
`embeddedDomains[]` |  `string` Embedded domains found in the file.  
`embeddedIps[]` |  `string` Embedded IP addresses found in the file.  
`exifInfo` |  `object (`[ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ExifInfo)`)` Exif metadata from different file formats extracted by exiftool.  
`signatureInfo` |  `object (`[SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SignatureInfo)`)` File signature information extracted from different tools.  
`pdfInfo` |  `object (`[PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PDFInfo)`)` Information about the PDF file structure.  
`firstSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mainIcon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Favicon)`)` Icon's relevant hashes.  
`ntfs` |  `object (`[NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.NtfsFileMetadata)`)` NTFS metadata.  
`appCompatCache` |  `object (`[AppCompatMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AppCompatMetadata)`)` Windows AppCompatCache (Application Compatibility) metadata.  
  
### FileMetadata

JSON representation  
---  
      
    
    {
      "pe": {
        object ([PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PeFileMetadata))
      }
    }  
  
Fields  
---  
`pe  
**(deprecated)**` |  `object (`[PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PeFileMetadata)`)` This item is deprecated!Metadata for Microsoft Windows PE files. Deprecate PeFileMetadata in favor of single File proto.  
  
### PeFileMetadata

JSON representation  
---  
      
    
    {
      "importHash": string
    }  
  
Fields  
---  
`importHash` |  `string` Hash of PE imports.  
  
### FileMetadataPE

JSON representation  
---  
      
    
    {
      "imphash": string,
      "entryPoint": string,
      "entryPointExiftool": string,
      "compilationTime": string,
      "compilationExiftoolTime": string,
      "section": [
        {
          object ([FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSection))
        }
      ],
      "imports": [
        {
          object ([FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataImports))
        }
      ],
      "resource": [
        {
          object ([FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataPeResourceInfo))
        }
      ],
      "resourcesTypeCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringToInt64MapEntry))
        }
      ],
      "resourcesLanguageCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringToInt64MapEntry))
        }
      ],
      "resourcesTypeCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "resourcesLanguageCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "signatureInfo": {
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSignatureInfo))
      }
    }  
  
Fields  
---  
`imphash` |  `string` Imphash of the file.  
`entryPoint` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.pe-entry-point.  
`entryPointExiftool` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.exiftool.EntryPoint.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.pe-timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`compilationExiftoolTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.exiftool.TimeStamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`section[]` |  `object (`[FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSection)`)` FilemetadataSection fields.  
`imports[]` |  `object (`[FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataImports)`)` FilemetadataImports fields.  
`resource[]` |  `object (`[FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataPeResourceInfo)`)` FilemetadataPeResourceInfo fields.  
`resourcesTypeCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resources_type_count_str.  
`resourcesLanguageCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resources_language_count_str.  
`resourcesTypeCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5  
`resourcesLanguageCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10  
`signatureInfo  
**(deprecated)**` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSignatureInfo)`)` This item is deprecated!FilemetadataSignatureInfo field. deprecated, user File.signature_info instead.  
  
### FileMetadataSection

JSON representation  
---  
      
    
    {
      "name": string,
      "entropy": number,
      "rawSizeBytes": string,
      "virtualSizeBytes": string,
      "md5Hex": string
    }  
  
Fields  
---  
`name` |  `string` Name of the section.  
`entropy` |  `number` Entropy of the section.  
`rawSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Raw file size in bytes.  
`virtualSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Virtual file size in bytes.  
`md5Hex` |  `string` MD5 hex of the file.  
  
### FileMetadataImports

JSON representation  
---  
      
    
    {
      "library": string,
      "functions": [
        string
      ]
    }  
  
Fields  
---  
`library` |  `string` Library field.  
`functions[]` |  `string` Function field.  
  
### FileMetadataPeResourceInfo

JSON representation  
---  
      
    
    {
      "sha256Hex": string,
      "filetypeMagic": string,
      "languageCode": string,
      "entropy": number,
      "fileType": string
    }  
  
Fields  
---  
`sha256Hex` |  `string` SHA256_hex field..  
`filetypeMagic` |  `string` Type of resource content, as identified by the magic Python module.  
`languageCode` |  `string` Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification. Examples: | Language | Sublanguage | Field value | | LANG_NEUTRAL | SUBLANG_NEUTRAL | NEUTRAL | | LANG_FRENCH | - | FRENCH | | LANG_ENGLISH | SUBLANG_ENGLISH US | ENGLISH US |  
`entropy` |  `number` Entropy of the resource.  
`fileType` |  `string` File type. Note that this value may not match any of the well-known type identifiers defined in the ResourceType enum.  
  
### StringToInt64MapEntry

JSON representation  
---  
      
    
    {
    
      // Union field _key can be only one of the following:
      "key": string
      // End of list of possible types for union field _key.
    
      // Union field _value can be only one of the following:
      "value": string
      // End of list of possible types for union field _value.
    }  
  
Fields  
---  
Union field `_key`.`_key` can be only one of the following:  
`key` |  `string` Key field.  
Union field `_value`.`_value` can be only one of the following:  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Value field.  
  
### FileMetadataSignatureInfo

JSON representation  
---  
      
    
    {
      "verificationMessage": string,
      "verified": boolean,
      "signer": [
        string
      ],
      "signers": [
        {
          object ([SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SignerInfo))
        }
      ],
      "x509": [
        {
          object ([X509](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.X509))
        }
      ]
    }  
  
Fields  
---  
`verificationMessage` |  `string` Status of the certificate. Valid values are "Signed", "Unsigned" or a description of the certificate anomaly, if found.  
`verified` |  `boolean` True if verification_message == "Signed"  
`signer[]  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use signers field.  
`signers[]` |  `object (`[SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SignerInfo)`)` File metadata signer information. The order of the signers matters. Each element is a higher level authority, being the last the root authority.  
`x509[]` |  `object (`[X509](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.X509)`)` List of certificates.  
  
### SignerInfo

JSON representation  
---  
      
    
    {
    
      // Union field _name can be only one of the following:
      "name": string
      // End of list of possible types for union field _name.
    
      // Union field _status can be only one of the following:
      "status": string
      // End of list of possible types for union field _status.
    
      // Union field _valid_usage can be only one of the following:
      "validUsage": string
      // End of list of possible types for union field _valid_usage.
    
      // Union field _cert_issuer can be only one of the following:
      "certIssuer": string
      // End of list of possible types for union field _cert_issuer.
    }  
  
Fields  
---  
Union field `_name`.`_name` can be only one of the following:  
`name` |  `string` Common name of the signers/certificate. The order of the signers matters. Each element is a higher level authority, the last being the root authority.  
Union field `_status`.`_status` can be only one of the following:  
`status` |  `string` It can say "Valid" or state the problem with the certificate if any (e.g. "This certificate or one of the certificates in the certificate chain is not time valid.").  
Union field `_valid_usage`.`_valid_usage` can be only one of the following:  
`validUsage` |  `string` Indicates which situations the certificate is valid for (e.g. "Code Signing").  
Union field `_cert_issuer`.`_cert_issuer` can be only one of the following:  
`certIssuer` |  `string` Company that issued the certificate.  
  
### X509

JSON representation  
---  
      
    
    {
      "name": string,
      "algorithm": string,
      "thumbprint": string,
      "certIssuer": string,
      "serialNumber": string
    }  
  
Fields  
---  
`name` |  `string` Certificate name.  
`algorithm` |  `string` Certificate algorithm.  
`thumbprint` |  `string` Certificate thumbprint.  
`certIssuer` |  `string` Issuer of the certificate.  
`serialNumber` |  `string` Certificate serial number.  
  
### PrefetchFileMetadata

JSON representation  
---  
      
    
    {
      "runCount": string,
      "prefetchHash": string
    }  
  
Fields  
---  
`runCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the application has been run.  
`prefetchHash` |  `string` A hash of the executable path used to identify the prefetch file.  
  
### ExifInfo

JSON representation  
---  
      
    
    {
      "originalFile": string,
      "product": string,
      "company": string,
      "fileDescription": string,
      "entryPoint": string,
      "compilationTime": string
    }  
  
Fields  
---  
`originalFile` |  `string` original file name.  
`product` |  `string` product name.  
`company` |  `string` company name.  
`fileDescription` |  `string` description of a file.  
`entryPoint` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` entry point.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Compilation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SignatureInfo

JSON representation  
---  
      
    
    {
      "sigcheck": {
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSignatureInfo))
      },
      "codesign": {
        object ([FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataCodesign))
      }
    }  
  
Fields  
---  
`sigcheck` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataSignatureInfo)`)` Signature information extracted from the sigcheck tool.  
`codesign` |  `object (`[FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FileMetadataCodesign)`)` Signature information extracted from the codesign utility.  
  
### FileMetadataCodesign

JSON representation  
---  
      
    
    {
      "id": string,
      "format": string,
      "compilationTime": string,
      "teamId": string
    }  
  
Fields  
---  
`id` |  `string` Code sign identifier.  
`format` |  `string` Code sign format.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Code sign timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`teamId` |  `string` The assigned team identifier of the developer who signed the application.  
  
### PDFInfo

JSON representation  
---  
      
    
    {
      "js": string,
      "javascript": string,
      "launchActionCount": string,
      "objectStreamCount": string,
      "endobjCount": string,
      "header": string,
      "acroform": string,
      "autoaction": string,
      "embeddedFile": string,
      "encrypted": string,
      "flash": string,
      "jbig2Compression": string,
      "objCount": string,
      "endstreamCount": string,
      "pageCount": string,
      "streamCount": string,
      "openaction": string,
      "startxref": string,
      "suspiciousColors": string,
      "trailer": string,
      "xfa": string,
      "xref": string
    }  
  
Fields  
---  
`js` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JS tags found in the PDF file. Should be the same as javascript field in normal scenarios.  
`javascript` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JavaScript tags found in the PDF file. Should be the same as the js field in normal scenarios.  
`launchActionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /Launch tags found in the PDF file.  
`objectStreamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of object streams.  
`endobjCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of object definitions (endobj keyword).  
`header` |  `string` PDF version.  
`acroform` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /AcroForm tags found in the PDF.  
`autoaction` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /AA tags found in the PDF.  
`embeddedFile` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /EmbeddedFile tags found in the PDF.  
`encrypted` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Whether the document is encrypted or not. This is defined by the /Encrypt tag.  
`flash` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /RichMedia tags found in the PDF.  
`jbig2Compression` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JBIG2Decode tags found in the PDF.  
`objCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of objects definitions (obj keyword).  
`endstreamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of defined stream objects (stream keyword).  
`pageCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of pages in the PDF.  
`streamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of defined stream objects (stream keyword).  
`openaction` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /OpenAction tags found in the PDF.  
`startxref` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of startxref keywords in the PDF.  
`suspiciousColors` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of colors expressed with more than 3 bytes (CVE-2009-3459).  
`trailer` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of trailer keywords in the PDF.  
`xfa` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of \XFA tags found in the PDF.  
`xref` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of xref keywords in the PDF.  
  
### NtfsFileMetadata

JSON representation  
---  
      
    
    {
      "changeTime": string,
      "filenameCreateTime": string,
      "filenameModifyTime": string,
      "filenameAccessTime": string,
      "filenameChangeTime": string,
      "usnJournal": [
        {
          object ([UsnJournal](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.UsnJournal))
        }
      ]
    }  
  
Fields  
---  
`changeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS MFT entry changed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute created timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameModifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute modified timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameAccessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute accessed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute changed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`usnJournal[]` |  `object (`[UsnJournal](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.UsnJournal)`)` NTFS USN journal.  
  
### UsnJournal

JSON representation  
---  
      
    
    {
      "attributesFlag": string,
      "attributes": enum (Attribute),
      "fileAttributes": [
        enum (Attribute)
      ],
      "allocated": boolean,
      "reason": enum (Reason)
    }  
  
Fields  
---  
`attributesFlag` |  `string` File attributes flags from the USN record (e.g., "0x20").  
`attributes  
**(deprecated)**` |  `enum (`Attribute`)` This item is deprecated!Deprecated: Use file_attributes instead. File attributes from the USN record.  
`fileAttributes[]` |  `enum (`Attribute`)` File attributes from the USN record.  
`allocated` |  `boolean` Indicates whether the file is allocated in the Master File Table (MFT).  
`reason` |  `enum (`Reason`)` Human-readable string describing the reason for the USN journal entry (e.g., "USN_REASON_FILE_CREATE").  
  
### AppCompatMetadata

JSON representation  
---  
      
    
    {
      "sequence": integer,
      "executed": boolean,
      "controlSet": string
    }  
  
Fields  
---  
`sequence` |  `integer` Indicates the chronological order in which the entry was added to the cache.  
`executed` |  `boolean` Indicates whether the file associated with the entry was executed.  
`controlSet` |  `string` Indicates which registry Control Set the AppCompatCache data belongs to (e.g., "ControlSet001").  
  
### Asset

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "hostname": string,
      "assetId": string,
      "ip": [
        string
      ],
      "mac": [
        string
      ],
      "natIp": [
        string
      ],
      "firstSeenTime": string,
      "hardware": [
        {
          object ([Hardware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Hardware))
        }
      ],
      "platformSoftware": {
        object ([PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PlatformSoftware))
      },
      "software": [
        {
          object ([Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Software))
        }
      ],
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "category": string,
      "type": enum (AssetType),
      "networkDomain": string,
      "creationTime": string,
      "firstDiscoverTime": string,
      "lastDiscoverTime": string,
      "systemLastUpdateTime": string,
      "lastBootTime": string,
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "deploymentStatus": enum (DeploymentStatus),
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Vulnerability))
        }
      ],
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute))
      },
      "wmiPersistenceItem": {
        object ([WmiPersistenceItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.WmiPersistenceItem))
      }
    }  
  
Fields  
---  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (a GUID or similar). This field can be used as an entity indicator for asset entities.  
`hostname` |  `string` Asset hostname or domain name field. This field can be used as an entity indicator for asset entities.  
`assetId` |  `string` The asset ID. Value must contain the ':' character. For example, cs:abcdd23434. This field can be used as an entity indicator for asset entities.  
`ip[]` |  `string` A list of IP addresses associated with an asset. This field can be used as an entity indicator for asset entities.  
`mac[]` |  `string` List of MAC addresses associated with an asset. This field can be used as an entity indicator for asset entities.  
`natIp[]` |  `string` List of NAT IP addresses associated with an asset.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first observed time for an asset. The value is calculated on the basis of the first time the identifier was observed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`hardware[]` |  `object (`[Hardware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Hardware)`)` The asset hardware specifications.  
`platformSoftware` |  `object (`[PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.PlatformSoftware)`)` The asset operating system platform software.  
`software[]` |  `object (`[Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Software)`)` The asset software details.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Location of the asset.  
`category` |  `string` The category of the asset (e.g. "End User Asset", "Workstation", "Server").  
`type` |  `enum (`AssetType`)` The type of the asset (e.g. workstation or laptop or server).  
`networkDomain` |  `string` The network domain of the asset (e.g. "corp.acme.com")  
`creationTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Time the asset was created or provisioned. Deprecate: creation_time should be populated in Attribute as generic metadata.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`firstDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was first discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`systemLastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset system or OS was last updated. For all other operations that are not system updates (such as resizing a VM), use Attribute.last_update_time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBootTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last boot started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` This item is deprecated!Metadata labels for the asset. Deprecated: labels should be populated in Attribute as generic metadata.  
`deploymentStatus` |  `enum (`DeploymentStatus`)` The deployment status of the asset for device lifecycle purposes.  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Vulnerability)`)` Vulnerabilities discovered on asset.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Attribute)`)` Generic entity metadata attributes of the asset.  
`wmiPersistenceItem` |  `object (`[WmiPersistenceItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.WmiPersistenceItem)`)` Information about a WMI persistence item.  
  
### Hardware

JSON representation  
---  
      
    
    {
      "serialNumber": string,
      "manufacturer": string,
      "model": string,
      "cpuPlatform": string,
      "cpuModel": string,
      "cpuClockSpeed": string,
      "cpuMaxClockSpeed": string,
      "cpuNumberCores": string,
      "ram": string
    }  
  
Fields  
---  
`serialNumber` |  `string` Hardware serial number.  
`manufacturer` |  `string` Hardware manufacturer.  
`model` |  `string` Hardware model.  
`cpuPlatform` |  `string` Platform of the hardware CPU (e.g. "Intel Broadwell").  
`cpuModel` |  `string` Model description of the hardware CPU (e.g. "2.8 GHz Quad-Core Intel Core i5").  
`cpuClockSpeed` |  `string` Clock speed of the hardware CPU in MHz.  
`cpuMaxClockSpeed` |  `string` Maximum possible clock speed of the hardware CPU in MHz.  
`cpuNumberCores` |  `string` Number of CPU cores.  
`ram` |  `string` Amount of the hardware ramdom access memory (RAM) in Mb.  
  
### PlatformSoftware

JSON representation  
---  
      
    
    {
      "platform": enum (Platform),
      "platformVersion": string,
      "platformPatchLevel": string
    }  
  
Fields  
---  
`platform` |  `enum (`Platform`)` The platform operating system.  
`platformVersion` |  `string` The platform software version ( e.g. "Microsoft Windows 1803").  
`platformPatchLevel` |  `string` The platform software patch level ( e.g. "Build 17134.48", "SP1").  
  
### Software

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Permission))
        }
      ],
      "description": string,
      "vendorName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the software.  
`version` |  `string` The version of the software.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Permission)`)` System permissions granted to the software. For example, "android.permission.WRITE_EXTERNAL_STORAGE"  
`description` |  `string` The description of the software.  
`vendorName` |  `string` The name of the software vendor.  
  
### Vulnerability

JSON representation  
---  
      
    
    {
      "about": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "name": string,
      "description": string,
      "vendor": string,
      "scanStartTime": string,
      "scanEndTime": string,
      "firstFound": string,
      "lastFound": string,
      "severity": enum (Severity),
      "severityDetails": string,
      "cvssBaseScore": number,
      "cvssVector": string,
      "cvssVersion": string,
      "cveId": string,
      "cveDescription": string,
      "vendorVulnerabilityId": string,
      "vendorKnowledgeBaseArticleId": string
    }  
  
Fields  
---  
`about` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` If the vulnerability is about a specific noun (e.g. executable), then add it here.  
`name` |  `string` Name of the vulnerability (e.g. "Unsupported OS Version detected").  
`description` |  `string` Description of the vulnerability.  
`vendor` |  `string` Vendor of scan that discovered vulnerability.  
`scanStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If the vulnerability was discovered during an asset scan, then this field should be populated with the time the scan started. This field can be left unset if the start time is not available or not applicable.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scanEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If the vulnerability was discovered during an asset scan, then this field should be populated with the time the scan ended. This field can be left unset if the end time is not available or not applicable.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`firstFound` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Products that maintain a history of vuln scans should populate first_found with the time that a scan first detected the vulnerability on this asset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastFound` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Products that maintain a history of vuln scans should populate last_found with the time that a scan last detected the vulnerability on this asset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`severity` |  `enum (`Severity`)` The severity of the vulnerability.  
`severityDetails` |  `string` Vendor-specific severity  
`cvssBaseScore` |  `number` CVSS Base Score in the range of 0.0 to 10.0. Useful for sorting.  
`cvssVector` |  `string` Vector of CVSS properties (e.g. "AV:L/AC:H/Au:N/C:N/I:P/A:C") Can be linked to via: [ ](https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator)<https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator>  
`cvssVersion` |  `string` Version of CVSS Vector/Score.  
`cveId` |  `string` Common Vulnerabilities and Exposures Id. [](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)<https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures> [](https://cve.mitre.org/about/faqs.html#what_is_cve_id)<https://cve.mitre.org/about/faqs.html#what_is_cve_id>  
`cveDescription` |  `string` Common Vulnerabilities and Exposures Description. [](https://cve.mitre.org/about/faqs.html#what_is_cve_record)<https://cve.mitre.org/about/faqs.html#what_is_cve_record>  
`vendorVulnerabilityId` |  `string` Vendor specific vulnerability id (e.g. Microsoft security bulletin id).  
`vendorKnowledgeBaseArticleId` |  `string` Vendor specific knowledge base article (e.g. "KBXXXXXX" from Microsoft). [](https://en.wikipedia.org/wiki/Microsoft_Knowledge_Base)<https://en.wikipedia.org/wiki/Microsoft_Knowledge_Base> [](https://access.redhat.com/knowledgebase)<https://access.redhat.com/knowledgebase>  
  
### WmiPersistenceItem

JSON representation  
---  
      
    
    {
      "caption": string,
      "name": string,
      "settingId": string,
      "derivation": string,
      "propertyCount": string,
      "relPath": string,
      "dynasty": string,
      "wmiSuperClass": string,
      "wmiClass": string,
      "genus": string
    }  
  
Fields  
---  
`caption` |  `string` A brief title or caption for the WMI object.  
`name` |  `string` The name of the WMI object.  
`settingId` |  `string` The identifier for the setting.  
`derivation` |  `string` The base class from which the WMI class is derived (e.g., CIM_Setting).  
`propertyCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of properties in the WMI object.  
`relPath` |  `string` The relative path to the WMI object (e.g., Win32_StartupCommand.Command=''').  
`dynasty` |  `string` The top-level class in the WMI inheritance hierarchy (e.g., CMI_Setting).  
`wmiSuperClass` |  `string` The immediate parent class in the WMI inheritance hierarchy.  
`wmiClass` |  `string` The name of the WMI class.  
`genus` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An integer representing the type or version of the WMI object.  
  
### Registry

JSON representation  
---  
      
    
    {
      "registryKey": string,
      "registryValueName": string,
      "registryValueData": string,
      "registryValueType": enum (Type),
      "registryValueBinaryData": string
    }  
  
Fields  
---  
`registryKey` |  `string` Registry key associated with an application or system component (e.g., HKEY_, HKCU\Environment...).  
`registryValueName` |  `string` Name of the registry value associated with an application or system component (e.g. TEMP).  
`registryValueData` |  `string` Data associated with a registry value (e.g. %USERPROFILE%\Local Settings\Temp).  
`registryValueType` |  `enum (`Type`)` Type of the registry value.  
`registryValueBinaryData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Binary data associated with a registry value. This field is only populated if the registry value type is BINARY. This field is not populated for other registry value types.A base64-encoded string.  
  
### Id

JSON representation  
---  
      
    
    {
      "namespace": enum (Namespace),
      "id": string,
      "stringId": string
    }  
  
Fields  
---  
`namespace` |  `enum (`Namespace`)` Namespace the id belongs to.  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Full raw ID.A base64-encoded string.  
`stringId` |  `string` Some ids are stored as strings that are not able to be translated to bytes, so store these separately. Ex. detection id of the form de_aaaaaaaa-aaaa...  
  
### Investigation

JSON representation  
---  
      
    
    {
      "comments": [
        string
      ],
    
      // Union field _verdict can be only one of the following:
      "verdict": enum (Verdict)
      // End of list of possible types for union field _verdict.
    
      // Union field _reputation can be only one of the following:
      "reputation": enum (Reputation)
      // End of list of possible types for union field _reputation.
    
      // Union field _severity_score can be only one of the following:
      "severityScore": integer
      // End of list of possible types for union field _severity_score.
    
      // Union field _status can be only one of the following:
      "status": enum (Status)
      // End of list of possible types for union field _status.
    
      // Union field _priority can be only one of the following:
      "priority": enum (Priority)
      // End of list of possible types for union field _priority.
    
      // Union field _root_cause can be only one of the following:
      "rootCause": string
      // End of list of possible types for union field _root_cause.
    
      // Union field _reason can be only one of the following:
      "reason": enum (Reason)
      // End of list of possible types for union field _reason.
    
      // Union field _risk_score can be only one of the following:
      "riskScore": integer
      // End of list of possible types for union field _risk_score.
    
      // Union field _id can be only one of the following:
      "id": string
      // End of list of possible types for union field _id.
    }  
  
Fields  
---  
`comments[]` |  `string` Comment added by the Analyst.  
Union field `_verdict`.`_verdict` can be only one of the following:  
`verdict` |  `enum (`Verdict`)` Describes reason a finding investigation was resolved.  
Union field `_reputation`.`_reputation` can be only one of the following:  
`reputation` |  `enum (`Reputation`)` Describes whether a finding was useful or not-useful.  
Union field `_severity_score`.`_severity_score` can be only one of the following:  
`severityScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Severity score for a finding set by an analyst.  
Union field `_status`.`_status` can be only one of the following:  
`status` |  `enum (`Status`)` Describes the workflow status of a finding.  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `enum (`Priority`)` Priority of the Alert or Finding set by analyst.  
Union field `_root_cause`.`_root_cause` can be only one of the following:  
`rootCause` |  `string` Root cause of the Alert or Finding set by analyst.  
Union field `_reason`.`_reason` can be only one of the following:  
`reason` |  `enum (`Reason`)` Reason for closing the Case or Alert.  
Union field `_risk_score`.`_risk_score` can be only one of the following:  
`riskScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Risk score for a finding set by an analyst.  
Union field `_id`.`_id` can be only one of the following:  
`id` |  `string` Identifier for the investigation  
  
### VariablesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FindingVariable))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.FindingVariable)`)`  
  
### FindingVariable

JSON representation  
---  
      
    
    {
      "type": enum (Type),
      "value": string,
      "sourcePath": string,
    
      // Union field typed_value can be only one of the following:
      "boolVal": boolean,
      "bytesVal": string,
      "doubleVal": number,
      "int64Val": string,
      "uint64Val": string,
      "stringVal": string,
      "timestampTime": string,
      "nullVal": boolean,
      "boolSeq": {
        object ([BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.BoolSequence))
      },
      "bytesSeq": {
        object ([BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.BytesSequence))
      },
      "doubleSeq": {
        object ([DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DoubleSequence))
      },
      "int64Seq": {
        object ([Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Int64Sequence))
      },
      "uint64Seq": {
        object ([Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Uint64Sequence))
      },
      "stringSeq": {
        object ([StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringSequence))
      }
      // End of list of possible types for union field typed_value.
    }  
  
Fields  
---  
`type` |  `enum (`Type`)` The type of the variable.  
`value` |  `string` The value in string form.  
`sourcePath` |  `string` The UDM field path for the field which this value was derived from. Example: `principal.user.username`  
Union field `typed_value`. The typed value of the variable. `typed_value` can be only one of the following:  
`boolVal` |  `boolean` The value in boolean format.  
`bytesVal` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The value in bytes format.A base64-encoded string.  
`doubleVal` |  `number` The value in double format.  
`int64Val` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The value in int64 format.  
`uint64Val` |  `string` The value in uint64 format.  
`stringVal` |  `string` The value in string format. Enum values are returned as strings.  
`timestampTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The value in timestamp format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nullVal` |  `boolean` Whether the value is null.  
`boolSeq` |  `object (`[BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.BoolSequence)`)` The value in boolsequence format.  
`bytesSeq` |  `object (`[BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.BytesSequence)`)` The value in bytessequence format.  
`doubleSeq` |  `object (`[DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DoubleSequence)`)` The value in doublesequence format.  
`int64Seq` |  `object (`[Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Int64Sequence)`)` The value in int64sequence format.  
`uint64Seq` |  `object (`[Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Uint64Sequence)`)` The value in uint64sequence format.  
`stringSeq` |  `object (`[StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.StringSequence)`)` The value in stringsequence format.  
  
### BoolSequence

JSON representation  
---  
      
    
    {
      "boolVals": [
        boolean
      ]
    }  
  
Fields  
---  
`boolVals[]` |  `boolean` bool sequence.  
  
### BytesSequence

JSON representation  
---  
      
    
    {
      "bytesVals": [
        string
      ]
    }  
  
Fields  
---  
`bytesVals[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` bytes sequence.A base64-encoded string.  
  
### DoubleSequence

JSON representation  
---  
      
    
    {
      "doubleVals": [
        number
      ]
    }  
  
Fields  
---  
`doubleVals[]` |  `number` double sequence.  
  
### Int64Sequence

JSON representation  
---  
      
    
    {
      "int64Vals": [
        string
      ]
    }  
  
Fields  
---  
`int64Vals[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` int64 sequence.  
  
### Uint64Sequence

JSON representation  
---  
      
    
    {
      "uint64Vals": [
        string
      ]
    }  
  
Fields  
---  
`uint64Vals[]` |  `string` uint64 sequence.  
  
### StringSequence

JSON representation  
---  
      
    
    {
      "stringVals": [
        string
      ]
    }  
  
Fields  
---  
`stringVals[]` |  `string` string sequence.  
  
### AnalyticsMetadata

JSON representation  
---  
      
    
    {
      "analytic": string
    }  
  
Fields  
---  
`analytic` |  `string` Name of the analytic.  
  
### AttackDetails

JSON representation  
---  
      
    
    {
      "version": string,
      "tactics": [
        {
          object ([Tactic](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tactic))
        }
      ],
      "techniques": [
        {
          object ([Technique](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Technique))
        }
      ]
    }  
  
Fields  
---  
`version` |  `string` ATT&CK version (e.g. 12.1).  
`tactics[]` |  `object (`[Tactic](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tactic)`)` Tactics employed.  
`techniques[]` |  `object (`[Technique](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Technique)`)` Techniques employed.  
  
### Tactic

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string
    }  
  
Fields  
---  
`id` |  `string` Tactic ID (e.g. "TA0043").  
`name` |  `string` Tactic Name (e.g. "Reconnaissance")  
  
### Technique

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "subtechniqueId": string,
      "subtechniqueName": string
    }  
  
Fields  
---  
`id` |  `string` Technique ID (e.g. "T1595").  
`name` |  `string` Technique Name (e.g. "Active Scanning").  
`subtechniqueId` |  `string` Subtechnique ID (e.g. "T1595.001").  
`subtechniqueName` |  `string` Subtechnique Name (e.g. "Scanning IP Blocks").  
  
### Association

JSON representation  
---  
      
    
    {
      "id": string,
      "countryCode": [
        string
      ],
      "type": enum (AssociationType),
      "name": string,
      "description": string,
      "role": string,
      "sourceCountry": string,
      "alias": [
        {
          object ([AssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AssociationAlias))
        }
      ],
      "firstReferenceTime": string,
      "lastReferenceTime": string,
      "industriesAffected": [
        string
      ],
      "associatedActors": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Association))
        }
      ],
      "regionCode": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "sponsorRegion": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
      },
      "targetedRegions": [
        {
          object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location))
        }
      ],
      "tags": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Unique association id generated by mandiant.  
`countryCode[]` |  `string` Country from which the threat actor/ malware is originated.  
`type` |  `enum (`AssociationType`)` Signifies the type of association.  
`name` |  `string` Name of the threat actor/malware.  
`description` |  `string` Human readable description about the association.  
`role` |  `string` Role of the malware. Not applicable for threat actor.  
`sourceCountry  
**(deprecated)**` |  `string` This item is deprecated!Name of the country the threat originated from.  
`alias[]` |  `object (`[AssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AssociationAlias)`)` Different aliases of the threat actor given by different sources.  
`firstReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`industriesAffected[]` |  `string` List of industries the threat actor affects.  
`associatedActors[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Association)`)` List of associated threat actors for a malware. Not applicable for threat actors.  
`regionCode` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Name of the country, the threat is originating from.  
`sponsorRegion` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Sponsor region of the threat actor.  
`targetedRegions[]` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Location)`)` Targeted regions.  
`tags[]` |  `string` Tags.  
  
### AssociationAlias

JSON representation  
---  
      
    
    {
      "name": string,
      "company": string
    }  
  
Fields  
---  
`name` |  `string` Name of the alias.  
`company` |  `string` Name of the provider who gave the association's name.  
  
### Verdict

JSON representation  
---  
      
    
    {
      "sourceCount": integer,
      "responseCount": integer,
      "neighbourInfluence": string,
      "verdict": {
        object ([ProviderMLVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ProviderMLVerdict))
      },
      "analystVerdict": {
        object ([AnalystVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AnalystVerdict))
      }
    }  
  
Fields  
---  
`sourceCount` |  `integer` Number of sources from which intelligence was extracted.  
`responseCount` |  `integer` Total response count across all sources.  
`neighbourInfluence` |  `string` Describes the neighbour influence of the verdict.  
`verdict` |  `object (`[ProviderMLVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.ProviderMLVerdict)`)` ML Verdict provided by sources like Mandiant.  
`analystVerdict` |  `object (`[AnalystVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.AnalystVerdict)`)` Human analyst verdict provided by sources like Mandiant.  
  
### ProviderMLVerdict

JSON representation  
---  
      
    
    {
      "sourceProvider": string,
      "benignCount": integer,
      "maliciousCount": integer,
      "confidenceScore": integer,
      "mandiantSources": [
        {
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source))
        }
      ],
      "thirdPartySources": [
        {
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source))
        }
      ]
    }  
  
Fields  
---  
`sourceProvider` |  `string` Source provider giving the ML verdict.  
`benignCount` |  `integer` Count of responses where this IoC was marked benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked malicious.  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`mandiantSources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source)`)` List of mandiant sources from which the verdict was generated.  
`thirdPartySources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source)`)` List of third-party sources from which the verdict was generated.  
  
### Source

JSON representation  
---  
      
    
    {
      "name": string,
      "benignCount": integer,
      "maliciousCount": integer,
      "quality": enum (ProductConfidence),
      "responseCount": integer,
      "sourceCount": integer,
      "threatIntelligenceSources": [
        {
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Name of the IoC source.  
`benignCount` |  `integer` Count of responses where this IoC was marked benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked malicious.  
`quality` |  `enum (`ProductConfidence`)` Quality of the IoC mapping extracted from the source.  
`responseCount` |  `integer` Total response count from this source.  
`sourceCount` |  `integer` Number of sources from which intelligence was extracted.  
`threatIntelligenceSources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Source)`)` Different threat intelligence sources from which IoC info was extracted.  
  
### AnalystVerdict

JSON representation  
---  
      
    
    {
      "confidenceScore": integer,
      "verdictTime": string,
      "verdictResponse": enum (VerdictResponse)
    }  
  
Fields  
---  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`verdictTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp at which the verdict was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictResponse` |  `enum (`VerdictResponse`)` Details of the verdict.  
  
### VerdictInfo

JSON representation  
---  
      
    
    {
      "sourceCount": integer,
      "responseCount": integer,
      "neighbourInfluence": string,
      "verdictType": enum (VerdictType),
      "sourceProvider": string,
      "benignCount": integer,
      "maliciousCount": integer,
      "confidenceScore": integer,
      "iocStats": [
        {
          object ([IoCStats](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.IoCStats))
        }
      ],
      "verdictTime": string,
      "verdictResponse": enum (VerdictResponse),
      "globalCustomerCount": integer,
      "globalHitsCount": integer,
      "pwn": boolean,
      "categoryDetails": string,
      "pwnFirstTaggedTime": string
    }  
  
Fields  
---  
`sourceCount` |  `integer` Number of sources from which intelligence was extracted.  
`responseCount` |  `integer` Total response count across all sources.  
`neighbourInfluence` |  `string` Describes the near neighbor influence of the verdict.  
`verdictType` |  `enum (`VerdictType`)` Type of verdict.  
`sourceProvider` |  `string` Source provider giving the machine learning verdict.  
`benignCount` |  `integer` Count of responses where this IoC was marked as benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked as malicious.  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`iocStats[]` |  `object (`[IoCStats](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.IoCStats)`)` List of IoCStats from which the verdict was generated.  
`verdictTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the verdict was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictResponse` |  `enum (`VerdictResponse`)` Details about the verdict.  
`globalCustomerCount` |  `integer` Global customer count over the last 30 days  
`globalHitsCount` |  `integer` Global hit count over the last 30 days.  
`pwn` |  `boolean` Whether one or more Mandiant incident response customers had this indicator in their environment.  
`categoryDetails` |  `string` Tags related to the verdict.  
`pwnFirstTaggedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp of the first time a pwn was associated to this entity.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### IoCStats

JSON representation  
---  
      
    
    {
      "iocStatsType": enum (IoCStatsType),
      "firstLevelSource": string,
      "secondLevelSource": string,
      "benignCount": integer,
      "quality": enum (ProductConfidence),
      "maliciousCount": integer,
      "responseCount": integer,
      "sourceCount": integer
    }  
  
Fields  
---  
`iocStatsType` |  `enum (`IoCStatsType`)` Describes the source of the IoCStat.  
`firstLevelSource` |  `string` Name of first level IoC source, for example Mandiant or a third-party.  
`secondLevelSource` |  `string` Name of the second-level IoC source, for example Crowdsourced Threat Analysis or Knowledge Graph.  
`benignCount` |  `integer` Count of responses where the IoC was identified as benign.  
`quality` |  `enum (`ProductConfidence`)` Level of confidence in the IoC mapping extracted from the source.  
`maliciousCount` |  `integer` Count of responses where the IoC was identified as malicious.  
`responseCount` |  `integer` Total number of response from the source.  
`sourceCount` |  `integer` Number of sources from which information was extracted.  
  
### ThreatCollectionItem

JSON representation  
---  
      
    
    {
      "id": string,
      "type": enum (ThreatCollectionType),
      "altNames": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` The ID of the threat collection.  
`type` |  `enum (`ThreatCollectionType`)` The type of threat collection (e.g., "campaign").  
`altNames[]` |  `string` The name of the threat collection.  
  
### Reference

JSON representation  
---  
      
    
    {
      "event": {
        object ([UDM](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.UDM))
      },
      "entity": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Entity))
      },
      "joinedDataTableRows": [
        {
          object ([DataTableRowInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.DataTableRowInfo))
        }
      ],
      "graphEnrichment": {
        object ([EntityGraphEnrichment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.EntityGraphEnrichment))
      },
      "id": {
        object ([Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Id))
      },
      "logBatchToken": string
    }  
  
Fields  
---  
`event` |  `object (`[UDM](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.UDM)`)` Only one of event or entity will be populated for a single reference. Start one-of Event being referenced.  
`entity` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Entity)`)` Entity being referenced. In cases where the entity graph is overridden by data table, this will represent the original entity. End one-of  
`joinedDataTableRows[]` |  `object (`[DataTableRowInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.DataTableRowInfo)`)` The data table rows joined with the event.  
`graphEnrichment` |  `object (`[EntityGraphEnrichment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.EntityGraphEnrichment)`)` The entity graph enrichment details. Only set when the reference is an Entity which has been overridden by a data table or appended from a data table.  
`id` |  `object (`[Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Id)`)` Id being referenced. This field will also be populated for both event and entity with the event id. For detections, only this field will be populated.  
`logBatchToken` |  `string` The log batch token of the event being referenced. This field is used to fetch the raw log associated with the event in some legacy systems. This field is only populated for events/entities.  
  
### UDM

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metadata))
      },
      "additional": {
        object
      },
      "principal": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "src": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "target": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "intermediary": [
        {
          object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
        }
      ],
      "observer": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "about": [
        {
          object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
        }
      ],
      "securityResult": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
        }
      ],
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network))
      },
      "extensions": {
        object ([Extensions](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Extensions))
      },
      "extracted": {
        object
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metadata)`)` Event metadata such as timestamp, source product, etc.  
`additional` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Any important vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model.  
`principal` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents the acting entity that originates the activity described in the event. The principal must include at least one machine detail (hostname, MACs, IPs, port, product-specific identifiers like an EDR asset ID) or user detail (for example, username), and optionally include process details. It must NOT include any of the following fields: email, files, registry keys or values.  
`src` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents a source entity being acted upon by the participant along with the device or process context for the source object (the machine where the source object resides). For example, if user U copies file A on machine X to file B on machine Y, both file A and machine X would be specified in the src portion of the UDM event.  
`target` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents a target entity being referenced by the event or an object on the target entity. For example, in a firewall connection from device A to device B, A is described as the principal and B is described as the target. For a process injection by process C into target process D, process C is described as the principal and process D is described as the target.  
`intermediary[]` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents details on one or more intermediate entities processing activity described in the event. This includes device details about a proxy server or SMTP relay server. If an active event (that has a principal and possibly target) passes through any intermediaries, they're added here. Intermediaries can impact the overall action, for example blocking or modifying an ongoing request. A rule of thumb here is that 'principal', 'target', and description of the initial action should be the same regardless of the intermediary or its action. A successful network connection from A->B should look the same in principal/target/intermediary as one blocked by firewall C: principal: A, target: B (intermediary: C).  
`observer` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner), which is not a direct intermediary, but which observes and reports on the event in question.  
`about[]` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Represents entities referenced by the event that are not otherwise described in principal, src, target, intermediary or observer. For example, it could be used to track email file attachments, domains/URLs/IPs embedded within an email body, and DLLs that are loaded during a PROCESS_LAUNCH event.  
`securityResult[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` A list of security results.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Network)`)` All network details go here, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).  
`extensions` |  `object (`[Extensions](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Extensions)`)` All other first-class, event-specific metadata goes in this message. Do not place protocol metadata in Extensions; put it in Network.  
`extracted` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Flattened fields extracted from the log.  
  
### Metadata

JSON representation  
---  
      
    
    {
      "id": string,
      "productLogId": string,
      "eventTimestamp": string,
      "eventTimestampAttributes": [
        enum (EventTimestampAttribute)
      ],
      "collectedTimestamp": string,
      "ingestedTimestamp": string,
      "eventType": enum (EventType),
      "vendorName": string,
      "productName": string,
      "productVersion": string,
      "productEventType": string,
      "productDeploymentId": string,
      "description": string,
      "urlBackToProduct": string,
      "ingestionLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "tags": {
        object ([Tags](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tags))
      },
      "enrichmentState": enum (EnrichmentState),
      "logType": string,
      "baseLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessLabels))
      },
      "enrichmentLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessLabels))
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
`eventTimestampAttributes[]` |  `enum (`EventTimestampAttribute`)` Attributes associated with event_timestamp. This field is used to distinguish between different types of timestamps that can be used to represent the event_timestamp.  
`collectedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was collected by the vendor's local collection infrastructure.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ingestedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was ingested (received) by Chronicle.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eventType` |  `enum (`EventType`)` The event type. If an event has multiple possible types, this specifies the most specific type.  
`vendorName` |  `string` The name of the product vendor.  
`productName` |  `string` The name of the product.  
`productVersion` |  `string` The version of the product.  
`productEventType` |  `string` A short, descriptive, human-readable, product-specific event name or type (e.g. "Scanned X", "User account created", "process_start").  
`productDeploymentId` |  `string` The deployment identifier assigned by the vendor for a product deployment.  
`description` |  `string` A human-readable unparsable description of the event.  
`urlBackToProduct` |  `string` A URL that takes the user to the source product console for this event.  
`ingestionLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` User-configured ingestion metadata labels.  
`tags` |  `object (`[Tags](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Tags)`)` Tags added by Chronicle after an event is parsed. It is an error to populate this field from within a parser.  
`enrichmentState` |  `enum (`EnrichmentState`)` The enrichment state.  
`logType` |  `string` The string value of log type.  
`baseLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessLabels)`)` Data access labels on the base event.  
`enrichmentLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessLabels)`)` Data access labels from all the contextual events used to enrich the base event.  
`structuredFields  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Flattened fields extracted from the log.  
`parserVersion` |  `string` The version of the parser that generated this UDM event.  
  
### Tags

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
  
### DataAccessLabels

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
          object ([DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessIngestionLabel))
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
`ingestionKvLabels[]` |  `object (`[DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.DataAccessIngestionLabel)`)` All the ingestion labels (key/value pairs).  
`allowScopedAccess` |  `boolean` Are the labels ready for scoped access  
  
### DataAccessIngestionLabel

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
  
### Extensions

JSON representation  
---  
      
    
    {
      "auth": {
        object ([Authentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Authentication))
      },
      "vulns": {
        object ([Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Vulnerabilities))
      },
      "entityRisk": {
        object ([EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityRisk))
      },
      "linuxUtmp": {
        object ([LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.LinuxUtmp))
      },
      "windowsEventLog": {
        object ([WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.WindowsEventLog))
      },
      "resourceUsage": {
        object ([ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.ResourceUsage))
      },
      "systemEventDetails": {
        object ([SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.SystemEventDetails))
      },
      "outlookMetadata": {
        object ([OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.OutlookMetadata))
      },
      "srum": {
        object ([Srum](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Srum))
      },
      "userAssist": {
        object ([UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.UserAssist))
      }
    }  
  
Fields  
---  
`auth` |  `object (`[Authentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Authentication)`)` An authentication extension.  
`vulns` |  `object (`[Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Vulnerabilities)`)` A vulnerability extension.  
`entityRisk` |  `object (`[EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityRisk)`)` An entity risk change extension.  
`linuxUtmp` |  `object (`[LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.LinuxUtmp)`)` A Linux Utmp extension. This captures details specific to Linux Utmp events, which record login and logout sessions on a Linux system.  
`windowsEventLog` |  `object (`[WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.WindowsEventLog)`)` A Windows Event Log extension. This captures details specific to Windows Event Log events, providing structured information from various Windows logs.  
`resourceUsage` |  `object (`[ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.ResourceUsage)`)` A resource usage extension. This captures details about what entity (e.g., process, user) is using a specific resource.  
`systemEventDetails` |  `object (`[SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.SystemEventDetails)`)` A system event details extension. This captures additional details for system-level events, such as message type, sender image ID, and subsystem.  
`outlookMetadata` |  `object (`[OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.OutlookMetadata)`)` A Microsoft Outlook specific metadata extension. This includes metadata related to Outlook items, such as comments, templates, and security flags.  
`srum` |  `object (`[Srum](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.Srum)`)` A SRUM extension. This captures details specific to Windows System Resource Usage Monitor (SRUM) events, providing insights into application resource consumption.  
`userAssist` |  `object (`[UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/mcp/udm_search#Output.Schema.UserAssist)`)` A UserAssist extension. This captures details specific to Windows User Assist events, which track application usage and execution.  
  
### Authentication

JSON representation  
---  
      
    
    {
      "type": enum (AuthType),
      "mechanism": [
        enum (Mechanism)
      ],
      "authDetails": string,
      "outcome": enum (Outcome)
    }  
  
Fields  
---  
`type` |  `enum (`AuthType`)` The type of authentication.  
`mechanism[]` |  `enum (`Mechanism`)` The authentication mechanism.  
`authDetails` |  `string` The vendor defined details of the authentication.  
`outcome` |  `enum (`Outcome`)` The outcome of the authentication event.  
  
### Vulnerabilities

JSON representation  
---  
      
    
    {
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Vulnerability))
        }
      ]
    }  
  
Fields  
---  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Vulnerability)`)` A list of vulnerabilities.  
  
### EntityRisk

JSON representation  
---  
      
    
    {
      "riskVersion": string,
      "riskWindow": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval))
      },
      "DEPRECATEDRiskScore": integer,
      "detectionsCount": integer,
      "firstDetectionTime": string,
      "lastDetectionTime": string,
      "riskScore": number,
      "normalizedRiskScore": integer,
      "riskWindowSize": string,
      "lastResetTime": string,
      "detailUri": string,
      "riskWindowHasNewDetections": boolean,
    
      // Union field _risk_delta can be only one of the following:
      "riskDelta": {
        object ([RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RiskDelta))
      }
      // End of list of possible types for union field _risk_delta.
    
      // Union field _raw_risk_delta can be only one of the following:
      "rawRiskDelta": {
        object ([RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RiskDelta))
      }
      // End of list of possible types for union field _raw_risk_delta.
    }  
  
Fields  
---  
`riskVersion` |  `string` Version of the risk score calculation algorithm.  
`riskWindow` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval)`)` Time window used when computing the risk score for an entity, for example 24 hours or 7 days.  
`DEPRECATEDRiskScore  
**(deprecated)**` |  `integer` This item is deprecated!Deprecated risk score.  
`detectionsCount` |  `integer` Number of detections that make up the risk score within the time window.  
`firstDetectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the first detection within the specified time window. This field is empty when there are no detections.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDetectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the last detection within the specified time window. This field is empty when there are no detections.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`riskScore` |  `number` Raw risk score for the entity.  
`normalizedRiskScore` |  `integer` Normalized risk score for the entity. This value is between 0-1000.  
`riskWindowSize` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Risk window duration for the entity.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`lastResetTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp for UEBA risk score reset based deduplication. Used specifically for risk based meta rules.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`detailUri` |  `string` Link to the Google Security Operations UI with information about the entity risk score. If the SecOps instance has multiple frontend paths configured, this will be a relative path that can be used to construct the full URL.  
`riskWindowHasNewDetections` |  `boolean` Whether there are new detections for the risk window.  
Union field `_risk_delta`.`_risk_delta` can be only one of the following:  
`riskDelta` |  `object (`[RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RiskDelta)`)` Represents the change in risk score for an entity between the end of the previous time window and the end of the current time window.  
Union field `_raw_risk_delta`.`_raw_risk_delta` can be only one of the following:  
`rawRiskDelta` |  `object (`[RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.RiskDelta)`)` Represents the change in raw risk score for an entity between the end of the previous time window and the end of the current time window.  
  
### RiskDelta

JSON representation  
---  
      
    
    {
      "previousRangeEndTime": string,
      "riskScoreDelta": integer,
      "previousRiskScore": integer,
      "riskScoreNumericDelta": integer
    }  
  
Fields  
---  
`previousRangeEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End time of the previous time window.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`riskScoreDelta` |  `integer` Difference in the normalized risk score from the previous recorded value.  
`previousRiskScore` |  `integer` Risk score from previous risk window  
`riskScoreNumericDelta` |  `integer` Numeric change between current and previous risk score  
  
### LinuxUtmp

JSON representation  
---  
      
    
    {
      "recordType": enum (RecordType)
    }  
  
Fields  
---  
`recordType` |  `enum (`RecordType`)` The activity record type.  
  
### WindowsEventLog

JSON representation  
---  
      
    
    {
      "channel": enum (Channel),
      "eventId": string,
      "activityId": string
    }  
  
Fields  
---  
`channel` |  `enum (`Channel`)` The channel of the event.  
`eventId` |  `string` A unique identifier for a specific type of event.  
`activityId` |  `string` A GUID (Globally Unique Identifier) used to link a sequence of related events together.  
  
### ResourceUsage

JSON representation  
---  
      
    
    {
      "usedEntity": string,
      "usedEntityId": string
    }  
  
Fields  
---  
`usedEntity` |  `string` The name of the entity (e.g., process, user) that is using the resource.  
`usedEntityId` |  `string` A numerical identifier for the entity using the resource (e.g., PID, UID).  
  
### SystemEventDetails

JSON representation  
---  
      
    
    {
      "messageType": string,
      "senderImageId": string,
      "subsystem": string
    }  
  
Fields  
---  
`messageType` |  `string` The specific type or category of the message.  
`senderImageId` |  `string` An identifier for the image associated with the sender of the message.  
`subsystem` |  `string` The subsystem or component that generated the event.  
  
### OutlookMetadata

JSON representation  
---  
      
    
    {
      "comment": string,
      "template": string,
      "title": string,
      "securityFlagsCount": integer
    }  
  
Fields  
---  
`comment` |  `string` A user-defined comment or note associated with the Outlook item.  
`template` |  `string` The name of the template file used to create the Outlook item.  
`title` |  `string` The title of the Outlook item.  
`securityFlagsCount` |  `integer` Count of Security-related flags for the message, such as encryption or signing status.  
  
### Srum

JSON representation  
---  
      
    
    {
      "id": string,
      "backgroundBytesRead": string,
      "backgroundBytesWritten": string,
      "backgroundContextSwitches": string,
      "backgroundCycleCount": string,
      "backgroundFlushesCount": string,
      "backgroundReadOperations": string,
      "backgroundWriteOperations": string,
      "interfaceLuid": string
    }  
  
Fields  
---  
`id` |  `string` A unique identifier for the SRUM record or the application/user being monitored.  
`backgroundBytesRead` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of bytes read by the application while running in the background.  
`backgroundBytesWritten` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of bytes written by the application while running in the background.  
`backgroundContextSwitches` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of context switches performed by the application's threads while in the background.  
`backgroundCycleCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.  
`backgroundFlushesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of flush operations performed by the application in the background.  
`backgroundReadOperations` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of read operations performed by the application in the background.  
`backgroundWriteOperations` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of write operations performed by the application in the background.  
`interfaceLuid` |  `string` The Locally Unique Identifier (LUID) for the network interface used for data transfer.  
  
### UserAssist

JSON representation  
---  
      
    
    {
      "applicationFocusCount": string,
      "applicationFocusDuration": string,
      "executionsCount": string,
      "entryIndex": string
    }  
  
Fields  
---  
`applicationFocusCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the application associated with the entry gained focus.  
`applicationFocusDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The total duration the application associated with the entry was in focus.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`executionsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the application associated with the entry has been executed.  
`entryIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The index or identifier of the user assist entry, unique per user.  
  
### Entity

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([EntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityMetadata))
      },
      "entity": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "relations": [
        {
          object ([Relation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Relation))
        }
      ],
      "additional": {
        object
      },
      "metric": {
        object ([Metric](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metric))
      },
    
      // Union field _risk_score can be only one of the following:
      "riskScore": {
        object ([EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityRisk))
      }
      // End of list of possible types for union field _risk_score.
    }  
  
Fields  
---  
`metadata` |  `object (`[EntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityMetadata)`)` Entity metadata such as timestamp, product, etc.  
`entity` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Noun in the UDM event that this entity represents.  
`relations[]` |  `object (`[Relation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Relation)`)` One or more relationships between the entity (a) and other entities, including the relationship type and related entity.  
`additional` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Important entity data that cannot be adequately represented within the formal sections of the Entity.  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metric)`)` Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC.  
Union field `_risk_score`.`_risk_score` can be only one of the following:  
`riskScore` |  `object (`[EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.EntityRisk)`)` Stores information related to the entity's risk score.  
  
### EntityMetadata

JSON representation  
---  
      
    
    {
      "productEntityId": string,
      "collectedTimestamp": string,
      "creationTimestamp": string,
      "interval": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval))
      },
      "vendorName": string,
      "productName": string,
      "feed": string,
      "productVersion": string,
      "entityType": enum (EntityType),
      "description": string,
      "threat": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult))
        }
      ],
      "sourceType": enum (SourceType),
      "sourceLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label))
        }
      ],
      "eventMetadata": {
        object ([Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metadata))
      },
      "structuredFields": {
        object
      },
      "extracted": {
        object
      }
    }  
  
Fields  
---  
`productEntityId` |  `string` A vendor-specific identifier that uniquely identifies the entity (e.g. a GUID, LDAP, OID, or similar).  
`collectedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` GMT timestamp when the entity information was collected by the vendor's local collection infrastructure.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creationTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` GMT timestamp when the entity described by the product_entity_id was created on the system where data was collected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval)`)` Valid existence time range for the version of the entity represented by this entity data.  
`vendorName` |  `string` Vendor name of the product that produced the entity information.  
`productName` |  `string` Product name that produced the entity information.  
`feed` |  `string` Vendor feed name for a threat indicator feed.  
`productVersion` |  `string` Version of the product that produced the entity information.  
`entityType` |  `enum (`EntityType`)` Entity type. If an entity has multiple possible types, this specifies the most specific type.  
`description` |  `string` Human-readable description of the entity.  
`threat[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.SecurityResult)`)` Metadata provided by a threat intelligence feed that identified the entity as malicious.  
`sourceType` |  `enum (`SourceType`)` The source of the entity.  
`sourceLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Label)`)` Entity source metadata labels.  
`eventMetadata` |  `object (`[Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Metadata)`)` Metadata field from the event.  
`structuredFields  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Structured fields extracted from the log.  
`extracted` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Flattened fields extracted from the log.  
  
### Relation

JSON representation  
---  
      
    
    {
      "entity": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun))
      },
      "entityType": enum (EntityType),
      "relationship": enum (Relationship),
      "direction": enum (Directionality),
      "uid": string,
      "entityLabel": enum (EntityLabel)
    }  
  
Fields  
---  
`entity` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Noun)`)` Entity (b) that the primary entity (a) is related to.  
`entityType` |  `enum (`EntityType`)` Type of the related entity (b) in this relationship.  
`relationship` |  `enum (`Relationship`)` Type of relationship.  
`direction` |  `enum (`Directionality`)` Directionality of relationship between primary entity (a) and the related entity (b).  
`uid` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` UID of the relationship.A base64-encoded string.  
`entityLabel` |  `enum (`EntityLabel`)` Label to identify the Noun of the relation.  
  
### Metric

JSON representation  
---  
      
    
    {
      "firstSeen": string,
      "lastSeen": string,
      "sumMeasure": {
        object ([Measure](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Measure))
      },
      "totalEvents": string,
      "metricName": enum (MetricName),
      "dimensions": [
        enum (Dimension)
      ],
      "exportWindow": string
    }  
  
Fields  
---  
`firstSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the first time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time stamp of the last time last time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sumMeasure` |  `object (`[Measure](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Measure)`)` Sum of all precomputed measures for the given metric.  
`totalEvents` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of events used to calculate the given precomputed metric.  
`metricName` |  `enum (`MetricName`)` Name of the analytic.  
`dimensions[]` |  `enum (`Dimension`)` All group by clauses used to calculate the metric.  
`exportWindow` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Export window for which the metric was exported.  
  
### Measure

JSON representation  
---  
      
    
    {
      "value": number,
      "aggregateFunction": enum (AggregateFunction)
    }  
  
Fields  
---  
`value` |  `number` Value of the aggregated measure.  
`aggregateFunction` |  `enum (`AggregateFunction`)` Function used to calculate the aggregated measure.  
  
### DataTableRowInfo

JSON representation  
---  
      
    
    {
      "dataTable": string,
      "row": {
        object
      },
      "rowId": string
    }  
  
Fields  
---  
`dataTable` |  `string` The name of data table.  
`row` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Stores the key value pair for a data table row where the key is the name of the column for the given value.  
`rowId` |  `string` The row id of the data table row.  
  
### EntityGraphEnrichment

JSON representation  
---  
      
    
    {
      "dataTable": string,
      "enrichmentType": enum (EnrichmentType),
      "overriddenEntity": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Entity))
      }
    }  
  
Fields  
---  
`dataTable` |  `string` The name of the data table.  
`enrichmentType` |  `enum (`EnrichmentType`)` The type of enrichment.  
`overriddenEntity` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_security_alerts#Output.Schema.Entity)`)` The entity which has only the overridden fields populated. Only populated if the enrichment type is OVERRIDE.  
  
### LatencyMetrics

JSON representation  
---  
      
    
    {
      "oldestIngestionTime": string,
      "newestIngestionTime": string,
      "oldestEventTime": string,
      "newestEventTime": string,
      "ingestionLatency": string
    }  
  
Fields  
---  
`oldestIngestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The oldest ingestion timestamp from the events used to create the detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`newestIngestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The newest (most recent) ingestion timestamp from the events used to create the detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`oldestEventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The oldest event timestamp from the events used to create the detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`newestEventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The newest (most recent) event timestamp from the events used to create the detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ingestionLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The difference between newest ingestion timestamp and newest event timestamp.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### ResponsePlatformInfo

JSON representation  
---  
      
    
    {
      "alertId": string,
      "responsePlatformType": enum (ResponsePlatformType)
    }  
  
Fields  
---  
`alertId` |  `string` Id of the alert in SOAR product.  
`responsePlatformType` |  `enum (`ResponsePlatformType`)` Type of SOAR product.  
  
### Feedback

JSON representation  
---  
      
    
    {
      "idpUserId": string,
      "createdTime": string,
    
      // Union field _verdict can be only one of the following:
      "verdict": enum (Verdict)
      // End of list of possible types for union field _verdict.
    
      // Union field _reputation can be only one of the following:
      "reputation": enum (Reputation)
      // End of list of possible types for union field _reputation.
    
      // Union field _confidence_score can be only one of the following:
      "confidenceScore": integer
      // End of list of possible types for union field _confidence_score.
    
      // Union field _risk_score can be only one of the following:
      "riskScore": integer
      // End of list of possible types for union field _risk_score.
    
      // Union field _disregarded can be only one of the following:
      "disregarded": boolean
      // End of list of possible types for union field _disregarded.
    
      // Union field _severity can be only one of the following:
      "severity": integer
      // End of list of possible types for union field _severity.
    
      // Union field _comment can be only one of the following:
      "comment": string
      // End of list of possible types for union field _comment.
    
      // Union field _status can be only one of the following:
      "status": enum (Status)
      // End of list of possible types for union field _status.
    
      // Union field _priority can be only one of the following:
      "priority": enum (Priority)
      // End of list of possible types for union field _priority.
    
      // Union field _root_cause can be only one of the following:
      "rootCause": string
      // End of list of possible types for union field _root_cause.
    
      // Union field _reason can be only one of the following:
      "reason": enum (Reason)
      // End of list of possible types for union field _reason.
    
      // Union field _severity_display can be only one of the following:
      "severityDisplay": string
      // End of list of possible types for union field _severity_display.
    
      // Union field _priority_display can be only one of the following:
      "priorityDisplay": string
      // End of list of possible types for union field _priority_display.
    
      // Union field _triage_agent_investigation_id can be only one of the following:
      "triageAgentInvestigationId": string
      // End of list of possible types for union field
      // _triage_agent_investigation_id.
    
      // Union field _user_type can be only one of the following:
      "userType": enum (UserType)
      // End of list of possible types for union field _user_type.
    }  
  
Fields  
---  
`idpUserId` |  `string` Required.  
`createdTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `_verdict`.`_verdict` can be only one of the following:  
`verdict` |  `enum (`Verdict`)`  
Union field `_reputation`.`_reputation` can be only one of the following:  
`reputation` |  `enum (`Reputation`)`  
Union field `_confidence_score`.`_confidence_score` can be only one of the following:  
`confidenceScore` |  `integer`  
Union field `_risk_score`.`_risk_score` can be only one of the following:  
`riskScore` |  `integer`  
Union field `_disregarded`.`_disregarded` can be only one of the following:  
`disregarded` |  `boolean`  
Union field `_severity`.`_severity` can be only one of the following:  
`severity` |  `integer`  
Union field `_comment`.`_comment` can be only one of the following:  
`comment` |  `string` Optional.  
Union field `_status`.`_status` can be only one of the following:  
`status` |  `enum (`Status`)` Optional.  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `enum (`Priority`)` Optional.  
Union field `_root_cause`.`_root_cause` can be only one of the following:  
`rootCause` |  `string` Optional.  
Union field `_reason`.`_reason` can be only one of the following:  
`reason` |  `enum (`Reason`)` Optional.  
Union field `_severity_display`.`_severity_display` can be only one of the following:  
`severityDisplay` |  `string` Optional.  
Union field `_priority_display`.`_priority_display` can be only one of the following:  
`priorityDisplay` |  `string` Optional.  
Union field `_triage_agent_investigation_id`.`_triage_agent_investigation_id` can be only one of the following:  
`triageAgentInvestigationId` |  `string` Optional.  
Union field `_user_type`.`_user_type` can be only one of the following:  
`userType` |  `enum (`UserType`)`  
  
### SoarAlertMetadata

JSON representation  
---  
      
    
    {
      "alertId": string,
      "sourceRule": string,
      "vendor": string,
      "sourceSystem": string,
      "product": string,
      "sourceSystemTicketId": string,
      "sourceSystemUri": string
    }  
  
Fields  
---  
`alertId` |  `string` Alert ID in the source SIEM system.  
`sourceRule` |  `string` Name of the rule triggering the alert in the source SIEM.  
`vendor` |  `string` Name of the vendor.  
`sourceSystem` |  `string` Name of the Source SIEM system.  
`product` |  `string` Name of the product the alert is coming from.  
`sourceSystemTicketId` |  `string` Ticket id for the alert in the source system.  
`sourceSystemUri` |  `string` Url to the source SIEM system.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
