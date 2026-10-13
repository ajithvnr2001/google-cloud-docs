---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/update_security_alert/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:18.111268+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/update_security_alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_security_alert`

Update security alert attributes directly in Chronicle SIEM.

Modifies specific fields of an existing security alert (status, severity, verdict, comments) based on its ID.

**Agent Responsibilities:**

  * Provide the `alert_id`.
  * Provide at least one field to update.



**Workflow Integration:**

  * Use to triage alerts (e.g., change status to "CLOSED", add a verdict).
  * Essential for alert lifecycle management.



**Use Cases:**

  * Close an alert after investigation.
  * Mark an alert as a False Positive.
  * Add analyst comments to an alert.
  * Change the severity or priority of an alert.



**Example Usage:**

  * `update_security_alert(alertId="de_12345678...", projectId="...", customerId="...", region="...", status="CLOSED", verdict="false_positive", comment="Determined to be a test event.")`



**Next Steps:**

  * Verify the update using `get_security_alert`.



The following sample demonstrate how to use `curl` to invoke the `update_security_alert` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_security_alert",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for LegacyUpdateAlert.

### LegacyUpdateAlertRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "alertId": string,
      "status": string,
      "severity": string,
      "priority": string,
      "verdict": string,
      "comment": string,
      "rootCause": string,
      "reason": string,
      "caseName": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. Google Cloud project ID.  
`customerId` |  `string` Required. Chronicle customer ID.  
`region` |  `string` Required. Chronicle region (e.g., "us", "europe").  
`alertId` |  `string` The unique ID of the alert to update.  
`status` |  `string` New status. Valid values: "NEW", "ASSIGNED", "IN_PROGRESS", "CLOSED".  
`severity` |  `string` New severity. Valid values: "unspecified", "informational", "low", "medium", "high", "critical".  
`priority` |  `string` New priority. Valid values: "unspecified", "info", "low", "medium", "high", "critical".  
`verdict` |  `string` New verdict. Valid values: "unspecified", "true_positive", "false_positive", "undefined".  
`comment` |  `string` Analyst comment to add.  
`rootCause` |  `string` Root cause of the alert.  
`reason` |  `string` Reason for the status change (e.g., "resolved", "false_positive").  
`caseName` |  `string` Name of the case associated with this alert.  
  
## Output Schema

Collection represents a container of objects (such as events, entity context metadata, detection finding metadata) and state (such as investigation details).

An example use case for Collection is to model a detection and investigation from detection finding metadata to investigative state collected in the course of the investigation. For more complex investigation and response workflows a Collection could represent an incident consisting of multiple child findings or incidents. This can be expanded on to model remediation elements of a full detection and response workflow.

### Collection

JSON representation  
---  
      
    
    {
      "id": string,
      "type": enum ([CollectionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.CollectionType)),
      "idNamespace": enum ([Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)),
      "createdTime": string,
      "lastUpdatedTime": string,
      "timeWindow": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval))
      },
      "collectionElements": [
        {
          object ([Element](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Element))
        }
      ],
      "detection": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
        }
      ],
      "detectionTime": string,
      "investigation": {
        object ([Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Investigation))
      },
      "tags": [
        string
      ],
      "responsePlatformInfo": {
        object ([ResponsePlatformInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.ResponsePlatformInfo))
      },
      "caseName": string,
      "feedbackSummary": {
        object ([Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Feedback))
      },
      "feedbackHistory": [
        {
          object ([Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Feedback))
        }
      ],
      "soarAlert": boolean,
      "soarAlertMetadata": {
        object ([SoarAlertMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.SoarAlertMetadata))
      },
      "dataAccessScope": string,
      "detectionTimingDetails": [
        enum ([DetectionTimingDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.DetectionTimingDetails))
      ],
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.LatencyMetrics))
      },
      "ruleRunFrequency": enum ([RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.RunFrequency)),
      "simulatedEventCount": string,
      "simulatedEventNames": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Unique ID for the collection. The ID is specific to the type of collection. For example, with rule detections this is the detection ID.  
`type` |  `enum (`[CollectionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.CollectionType)`)` What the collection represents.  
`idNamespace` |  `enum (`[Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)`)` The ID namespace used for the Collection.  
`createdTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the collection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdatedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the collection was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeWindow` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval)`)` Time interval that the collection represents.  
`collectionElements[]` |  `object (`[Element](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Element)`)` Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.  
`detection[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).  
`detectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp within the time_window related to the time of the collection_elements. For Rule Detections, this timestamp is the end of the the time_window for multi-event rules or the time of the event for single event rules. For late-arriving events that trigger new alerts, the detection_time will be the event time of the event.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`investigation` |  `object (`[Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Investigation)`)` Consolidated investigation details (categorization, status, etc) typically for collections that begin as detection findings and then evolve with analyst action and feedback into investigations around the detection output.  
`tags[]` |  `string` Tags set by UC/DSML/RE for the Finding during creation.  
`responsePlatformInfo` |  `object (`[ResponsePlatformInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.ResponsePlatformInfo)`)` Alert related info of this same alert in customer's SOAR platform.  
`caseName` |  `string` The resource name of the Case that this collection belongs to. Example: projects/{project id}/locations/{region}/chronicle/cases/{internal_case_id}  
`feedbackSummary` |  `object (`[Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Feedback)`)` The current primary analyst feedback. This does not include the history of feedback given, which may be supplied in `feedback`.  
`feedbackHistory[]` |  `object (`[Feedback](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Feedback)`)` The history of feedback submitted by analysts for this finding, in descending order by timestamp. This field is limited to the most recent 1000 feedback events. The primary feedback will also be included in this list.  
`soarAlert` |  `boolean` A boolean field indicating that the alert is present in SOAR.  
`soarAlertMetadata` |  `object (`[SoarAlertMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.SoarAlertMetadata)`)` Metadata fields of alerts coming from other SIEM systems via SOAR.  
`dataAccessScope` |  `string` The resource name of the DataAccessScope of this collection.  
`detectionTimingDetails[]` |  `enum (`[DetectionTimingDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.DetectionTimingDetails)`)` Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.LatencyMetrics)`)` The latency metrics for the specific detection. These metrics are calculated from ALL of the events that contribute to the detection, not just the sampled ones.  
`ruleRunFrequency` |  `enum (`[RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.RunFrequency)`)` The run frequency of the rule when it generated the detection.  
`simulatedEventCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of simulated events that contributed to this detection. Simulated events are realistic threat sequences (Raw Logs or UDM) programmatically delivered into the production ingestion pipeline to verify the entire detection lifecycle—from identification to action.  
`simulatedEventNames[]` |  `string` The set of all values from event ingestion_labels where SIMULATED is set as the key, for all simulated events that participated in this detection.  
  
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
        object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
      },
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Reference))
        }
      ],
      "label": string,
      "referencesSampled": boolean,
      "latencyMetrics": {
        object ([LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.LatencyMetrics))
      }
    }  
  
Fields  
---  
`association` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` Metadata that provides the relevant association for the references in the element. For a detection, this can be the correlated aspect of the references that contributed to the overall detection. For example, may include sub-rule condition, machine learning model metadata, and/or indicators implicated in this component of the detection (using the .about field).  
`references[]` |  `object (`[Reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Reference)`)` References to model primatives including events and entities that share a common association. Even though a reference can have both UDM and entity, a collection of references (of a single element) will only have one type of message in it (either UDM / Entity).  
`label` |  `string` A name that labels the entire references group.  
`referencesSampled` |  `boolean` Copied from the detection event_sample.too_many_event_samples field. If true, the number of references will be capped at the sample limit (set at rule service). This is applicable to both UDM references and Entity references.  
`latencyMetrics` |  `object (`[LatencyMetrics](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.LatencyMetrics)`)` Latency metrics for the specific element. These are calculated from all the contributing events or entities for a single event variable, not just the sampled ones included in references. This is currently only populated for UDM events.  
  
### SecurityResult

JSON representation  
---  
      
    
    {
      "about": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "category": [
        enum ([SecurityCategory](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityCategory))
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
      "displayName": string,
      "ruleVersion": string,
      "ruleType": string,
      "ruleAuthor": string,
      "ruleLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "alertState": enum ([AlertState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AlertState)),
      "detectionFields": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "outcomes": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "variables": {
        string: {
          object ([FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FindingVariable))
        },
        ...
      },
      "summary": string,
      "description": string,
      "action": [
        enum ([Action](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Action))
      ],
      "actionDetails": string,
      "severity": enum ([ProductSeverity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductSeverity)),
      "confidence": enum ([ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)),
      "priority": enum ([ProductPriority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductPriority)),
      "riskScore": number,
      "confidenceScore": number,
      "analyticsMetadata": [
        {
          object ([AnalyticsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AnalyticsMetadata))
        }
      ],
      "severityDetails": string,
      "confidenceDetails": string,
      "priorityDetails": string,
      "urlBackToProduct": string,
      "threatId": string,
      "threatFeedName": string,
      "threatIdNamespace": enum ([Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)),
      "threatStatus": enum ([ThreatStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatStatus)),
      "attackDetails": {
        object ([AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AttackDetails))
      },
      "firstDiscoveredTime": string,
      "associations": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association))
        }
      ],
      "campaigns": [
        string
      ],
      "reports": [
        string
      ],
      "verdict": {
        object ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict))
      },
      "lastUpdatedTime": string,
      "verdictInfo": [
        {
          object ([VerdictInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictInfo))
        }
      ],
      "threatVerdict": enum ([ThreatVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatVerdict)),
      "lastDiscoveredTime": string,
      "detectionDepth": string,
      "threatCollections": [
        {
          object ([ThreatCollectionItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatCollectionItem))
        }
      ]
    }  
  
Fields  
---  
`about` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` If the security result is about a specific entity (Noun), add it here. This field is not populated when the SecurityResult appears in a detection.  
`category[]` |  `enum (`[SecurityCategory](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityCategory)`)` The security category. This field is not populated when the SecurityResult appears in a detection.  
`categoryDetails[]` |  `string` For vendor-specific categories. For web categorization, put type in here such as "gambling" or "porn". This field is not populated when the SecurityResult appears in a detection.  
`threatName` |  `string` A vendor-assigned classification common across multiple customers (for example, "W32/File-A", "Slammer"). This field is not populated when the SecurityResult appears in a detection.  
`ruleSet` |  `string` The curated detection's rule set identifier. (for example, "windows-threats") This is primarily set in rule-generated detections and alerts.  
`ruleSetDisplayName` |  `string` The curated detections rule set display name. This is primarily set in rule-generated detections and alerts.  
`rulesetCategoryDisplayName` |  `string` The curated detection rule set category display name. (for example, if rule_set_display_name is "CDIR SCC Enhanced Exfiltration", the rule_set_category is "Cloud Threats"). This is primarily set in rule-generated detections and alerts.  
`ruleId` |  `string` A vendor-specific ID for a rule, varying by observer type (e.g. "08123", "5d2b44d0-5ef6-40f5-a704-47d61d3babbe").  
`ruleName` |  `string` Name of the security rule (e.g. "BlockInboundToOracle").  
`displayName` |  `string` The display name of the security result. This is populated from 'name_override' Outcome Variable, if present. Otherwise, this field is not set.  
`ruleVersion` |  `string` Version of the security rule. (e.g. "v1.1", "00001", "1604709794", "2020-11-16T23:04:19+00:00"). Note that rule versions are source-dependent and lexical ordering should not be assumed.  
`ruleType` |  `string` The type of security rule.  
`ruleAuthor` |  `string` Author of the security rule. This field is not populated when the SecurityResult appears in a detection.  
`ruleLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` A list of rule labels that can't be captured by the other fields in security result (e.g. "reference : AnotherRule", "contributor : John"). This is primarily set in rule-generated detections and alerts.  
`alertState` |  `enum (`[AlertState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AlertState)`)` The alerting types of this security result. This is primarily set for rule-generated detections and alerts.  
`detectionFields[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` An ordered list of values, that represent fields in detections for a security finding. This list represents mapping of names of requested entities to their values (the security result matched variables).For Collection SecurityResults, prefer variables instead.  
`outcomes[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` This item is deprecated!A list of outcomes that represent the results of this security finding. This list represents a mapping of names of the requested outcomes, to a stringified version of their values.This is only populated when the SecurityResult appears in a detection. This is deprecated. Use variables instead.  
`variables` |  `map (key: string, value: object (`[FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FindingVariable)`))` A list of outcomes and match variables that represent the results of this security finding. This list represents a mapping of names of the requested outcomes or match variables, to their values.This is only populated when the SecurityResult appears in a detection.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`summary` |  `string` A short human-readable summary (e.g. "failed login occurred")  
`description` |  `string` A human-readable description (e.g. "user password was wrong"). This can be more detailed than the summary.  
`action[]` |  `enum (`[Action](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Action)`)` Actions taken for this event. This field is not populated when the SecurityResult appears in a detection.  
`actionDetails` |  `string` The detail of the action taken as provided by the vendor. This field is not populated when the SecurityResult appears in a detection.  
`severity` |  `enum (`[ProductSeverity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductSeverity)`)` The severity of the result.  
`confidence` |  `enum (`[ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)`)` The confidence level of the result as estimated by the product. This field is not populated when the SecurityResult appears in a detection.  
`priority` |  `enum (`[ProductPriority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductPriority)`)` The priority of the result. This field is not populated when the SecurityResult appears in a detection.  
`riskScore` |  `number` The risk score of the security result.  
`confidenceScore` |  `number` The confidence score of the security result. This field is not populated when the SecurityResult appears in a detection.  
`analyticsMetadata[]` |  `object (`[AnalyticsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AnalyticsMetadata)`)` Stores metadata about each risk analytic metric the rule uses. This field is not populated when the SecurityResult appears in a detection.  
`severityDetails` |  `string` Vendor-specific severity. This field is not populated when the SecurityResult appears in a detection.  
`confidenceDetails` |  `string` Additional detail with regards to the confidence of a security event as estimated by the product vendor. This field is not populated when the SecurityResult appears in a detection.  
`priorityDetails` |  `string` Vendor-specific information about the security result priority. This field is not populated when the SecurityResult appears in a detection.  
`urlBackToProduct` |  `string` URL that takes the user to the source product console for this event. This field is not populated when the SecurityResult appears in a detection.  
`threatId` |  `string` Vendor-specific ID for a threat. This field is not populated when the SecurityResult appears in a detection.  
`threatFeedName` |  `string` Vendor feed name for a threat indicator feed. This field is not populated when the SecurityResult appears in a detection.  
`threatIdNamespace` |  `enum (`[Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)`)` The attribute threat_id_namespace qualifies threat_id with an id namespace to get an unique id. The attribute threat_id by itself is not unique across Google SecOps as it is a vendor specific id. This field is not populated when the SecurityResult appears in a detection.  
`threatStatus` |  `enum (`[ThreatStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatStatus)`)` Current status of the threat This field is not populated when the SecurityResult appears in a detection.  
`attackDetails` |  `object (`[AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AttackDetails)`)` MITRE ATT&CK details. This field is not populated when the SecurityResult appears in a detection.  
`firstDiscoveredTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First time the IoC threat was discovered in the provider. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`associations[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association)`)` Associations related to the threat.  
`campaigns[]  
**(deprecated)**` |  `string` This item is deprecated!Campaigns using this IOC threat. This is deprecated. Use threat_collections instead.  
`reports[]  
**(deprecated)**` |  `string` This item is deprecated!Reports that reference this IOC threat. These are the report IDs. This is deprecated. Use threat_collections instead.  
`verdict  
**(deprecated)**` |  `object (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict)`)` This item is deprecated!Verdict about the IoC from the provider. This field is now deprecated. Use VerdictInfo instead.  
`lastUpdatedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the IoC threat was updated in the provider. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictInfo[]` |  `object (`[VerdictInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictInfo)`)` Verdict information about the IoC from the provider. This field is not populated when the SecurityResult appears in a detection.  
`threatVerdict` |  `enum (`[ThreatVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatVerdict)`)` GCTI threat verdict on the security result entity. This field is not populated when the SecurityResult appears in a detection.  
`lastDiscoveredTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the IoC was seen in the provider data. This field is not populated when the SecurityResult appears in a detection.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`detectionDepth` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The depth of the detection chain. Applies only to composite detections.  
`threatCollections[]` |  `object (`[ThreatCollectionItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatCollectionItem)`)` GTI collections associated with the security result.  
  
### Noun

JSON representation  
---  
      
    
    {
      "hostname": string,
      "domain": {
        object ([Domain](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Domain))
      },
      "artifact": {
        object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Artifact))
      },
      "urlMetadata": {
        object ([Url](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Url))
      },
      "browser": {
        object ([Browser](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Browser))
      },
      "assetId": string,
      "user": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "userManagementChain": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
        }
      ],
      "group": {
        object ([Group](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Group))
      },
      "process": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process))
      },
      "processAncestors": [
        {
          object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process))
        }
      ],
      "asset": {
        object ([Asset](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Asset))
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
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.File))
      },
      "email": string,
      "registry": {
        object ([Registry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Registry))
      },
      "application": string,
      "platform": enum ([Platform](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Platform)),
      "platformVersion": string,
      "platformPatchLevel": string,
      "cloud": {
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cloud))
      },
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "ipLocation": [
        {
          object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
        }
      ],
      "ipGeoArtifact": [
        {
          object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Artifact))
        }
      ],
      "resource": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource))
      },
      "resourceAncestors": [
        {
          object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource))
        }
      ],
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "objectReference": {
        object ([Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Id))
      },
      "investigation": {
        object ([Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Investigation))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network))
      },
      "securityResult": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
        }
      ],
      "ai": {
        object ([Ai](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Ai))
      }
    }  
  
Fields  
---  
`hostname` |  `string` Client hostname or domain name field. Hostname also doubles as the domain for remote entities. This field can be used as an entity indicator for asset entities.  
`domain` |  `object (`[Domain](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Domain)`)` Information about the domain.  
`artifact` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Artifact)`)` Information about an artifact.  
`urlMetadata` |  `object (`[Url](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Url)`)` Information about the URL.  
`browser` |  `object (`[Browser](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Browser)`)` Information about an entry in the web browser's local history database.  
`assetId` |  `string` The asset ID. This field can be used as an entity indicator for asset entities.  
`user` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Information about the user.  
`userManagementChain[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Information about the user's management chain (reporting hierarchy). Note: user_management_chain is only populated when data is exported to BigQuery since recursive fields (e.g. user.managers) are not supported by BigQuery.  
`group` |  `object (`[Group](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Group)`)` Information about the group.  
`process` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process)`)` Information about the process.  
`processAncestors[]` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process)`)` Information about the process's ancestors ordered from immediate ancestor (parent process) to root. Note: process_ancestors is only populated when data is exported to BigQuery since recursive fields (e.g. process.parent_process) are not supported by BigQuery.  
`asset` |  `object (`[Asset](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Asset)`)` Information about the asset.  
`ip[]` |  `string` A list of IP addresses associated with a network connection. This field can be used as an entity indicator for asset entities.  
`natIp[]` |  `string` A list of NAT translated IP addresses associated with a network connection.  
`port` |  `integer` Source or destination network port number when a specific network connection is described within an event.  
`natPort` |  `integer` NAT external network port number when a specific network connection is described within an event.  
`mac[]` |  `string` List of MAC addresses associated with a device. Must be valid MAC addresses (EUI-48) in ASCII. This field can be used as an entity indicator for asset entities.  
`administrativeDomain` |  `string`  
`namespace` |  `string` Namespace which the device belongs to, such as "AD forest". Uses for this field include Microsoft Windows AD forest, the name of subsidiary, or the name of acquisition. This field can be used along with an asset indicator to identify an asset.  
`url` |  `string` The URL.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.File)`)` Information about the file.  
`email` |  `string` Email address. Only filled in for security_result.about  
`registry` |  `object (`[Registry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Registry)`)` Registry information.  
`application` |  `string` The name of an application or service. Some SSO solutions only capture the name of a target application such as "Atlassian" or "SecOps".  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Platform)`)` Platform.  
`platformVersion` |  `string` Platform version. For example, "Microsoft Windows 1803".  
`platformPatchLevel` |  `string` Platform patch level. For example, "Build 17134.48"  
`cloud  
**(deprecated)**` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cloud)`)` This item is deprecated!Cloud metadata. Deprecated: cloud should be populated in entity Attribute as generic metadata (e.g. asset.attribute.cloud).  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Physical location. For cloud environments, set the region in location.name.  
`ipLocation[]  
**(deprecated)**` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` This item is deprecated!Deprecated: use ip_geo_artifact.location instead.  
`ipGeoArtifact[]` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Artifact)`)` Enriched geographic information corresponding to an IP address. Specifically, location and network data.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource)`)` Information about the resource (e.g. scheduled task, calendar entry). This field should not be used for files, registry, or processes because these objects are already part of Noun.  
`resourceAncestors[]` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource)`)` Information about the resource's ancestors ordered from immediate ancestor (starting with parent resource).  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` This item is deprecated!Labels are key-value pairs. For example: key = "env", value = "prod". Deprecated: labels should be populated in entity Attribute as generic metadata (e.g. user.attribute.labels).  
`objectReference` |  `object (`[Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Id)`)` Finding to which the Analyst updated the feedback.  
`investigation` |  `object (`[Investigation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Investigation)`)` Analyst feedback/investigation for alerts.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network)`)` Network details, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).  
`securityResult[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` A list of security results.  
`ai` |  `object (`[Ai](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Ai)`)` An AI system.  
  
### Domain

JSON representation  
---  
      
    
    {
      "name": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence))
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
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "admin": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "tech": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "billing": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "zone": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
      },
      "whoisRecordRawText": string,
      "registryDataRawText": string,
      "ianaRegistrarId": integer,
      "privateRegistration": boolean,
      "categories": [
        string
      ],
      "favicon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon))
      },
      "jarm": string,
      "lastDnsRecords": [
        {
          object ([DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DNSRecord))
        }
      ],
      "lastDnsRecordsTime": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SSLCertificate))
      },
      "lastHttpsCertificateTime": string,
      "popularityRanks": [
        {
          object ([PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PopularityRank))
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
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence)`)` The prevalence of the domain within the customer's environment.  
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
`status` |  `string` Domain status. See <https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en> for meanings of possible values  
`registrant` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Parsed contact information for the registrant of the domain.  
`admin` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Parsed contact information for the administrative contact for the domain.  
`tech` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Parsed contact information for the technical contact for the domain  
`billing` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Parsed contact information for the billing contact of the domain.  
`zone` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Parsed contact information for the zone.  
`whoisRecordRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` WHOIS raw text.A base64-encoded string.  
`registryDataRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Registry Data raw text.A base64-encoded string.  
`ianaRegistrarId` |  `integer` IANA Registrar ID. See <https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml>  
`privateRegistration` |  `boolean` Indicates whether the domain appears to be using a private registration service to mask the owner's contact information.  
`categories[]` |  `string` Categories assign to the domain as retrieved from VirusTotal.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon)`)` Includes difference hash and MD5 hash of the domain's favicon.  
`jarm` |  `string` Domain's JARM hash.  
`lastDnsRecords[]` |  `object (`[DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DNSRecord)`)` Domain's DNS records from the last scan.  
`lastDnsRecordsTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date when the DNS records list was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SSLCertificate)`)` SSL certificate object retrieved last time the domain was analyzed.  
`lastHttpsCertificateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the certificate was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`popularityRanks[]` |  `object (`[PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PopularityRank)`)` Domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc  
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
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute))
      },
      "firstSeenTime": string,
      "accountType": enum ([AccountType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AccountType)),
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
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "managers": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
        }
      ],
      "hireDate": string,
      "terminationDate": string,
      "timeOff": [
        {
          object ([TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TimeOff))
        }
      ],
      "lastLoginTime": string,
      "lastPasswordChangeTime": string,
      "passwordExpirationTime": string,
      "accountExpirationTime": string,
      "accountLockoutTime": string,
      "lastBadPasswordAttemptTime": string,
      "userAuthenticationStatus": enum ([AuthenticationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthenticationStatus)),
      "roleName": string,
      "roleDescription": string,
      "userRole": enum ([Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Role_1))
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
`personalAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Personal address of the user.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute)`)` Generic entity metadata attributes of the user.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountType` |  `enum (`[AccountType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AccountType)`)` Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: <https://attack.mitre.org/techniques/T1078/>  
`groupid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the group that the user belongs to. Deprecated in favor of the repeated group_identifiers field.  
`groupIdentifiers[]` |  `string` Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).  
`windowsSid` |  `string` The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.  
`emailAddresses[]` |  `string` Email addresses of the user. This field can be used as an entity indicator for user entities.  
`employeeId` |  `string` Human capital management identifier. This field can be used as an entity indicator for user entities.  
`title` |  `string` User job title.  
`companyName` |  `string` User job company name.  
`department[]` |  `string` User job department  
`officeAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` User job office location.  
`managers[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` User job manager(s).  
`hireDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment hire date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`terminationDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment termination date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeOff[]` |  `object (`[TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TimeOff)`)` User time off leaves from active work.  
`lastLoginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last login timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastPasswordChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last password change timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`passwordExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User password expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountLockoutTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account lockout timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBadPasswordAttemptTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last bad password attempt timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userAuthenticationStatus` |  `enum (`[AuthenticationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthenticationStatus)`)` System authentication status for user.  
`roleName  
**(deprecated)**` |  `string` This item is deprecated!System role name for user. Deprecated: use attribute.roles.  
`roleDescription  
**(deprecated)**` |  `string` This item is deprecated!System role description for user. Deprecated: use attribute.roles.  
`userRole  
**(deprecated)**` |  `enum (`[Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Role_1)`)` This item is deprecated!System role for user. Deprecated: use attribute.roles.  
  
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
        object ([LatLng](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.LatLng))
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
`regionCoordinates` |  `object (`[LatLng](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.LatLng)`)` Coordinates for the associated region. See <https://cloud.google.com/vision/docs/reference/rest/v1/LatLng> for a description of the fields.  
  
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
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cloud))
      },
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Permission))
        }
      ],
      "roles": [
        {
          object ([Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Role))
        }
      ],
      "creationTime": string,
      "lastUpdateTime": string
    }  
  
Fields  
---  
`cloud` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cloud)`)` Cloud metadata attributes such as project ID, account ID, or organizational hierarchy.  
`labels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` Set of labels for the entity. Should only be used for product labels (for example, Google Cloud resource labels or Azure AD sensitivity labels. Should not be used for arbitrary key-value mappings.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Permission)`)` System permissions for IAM entity (human principal, service account, group).  
`roles[]` |  `object (`[Role](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Role)`)` System IAM roles to be assumed by resources to use the role's permissions for access control.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was created or provisioned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Cloud

JSON representation  
---  
      
    
    {
      "environment": enum ([CloudEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CloudEnvironment)),
      "vpc": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource))
      },
      "project": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource))
      },
      "availabilityZone": string
    }  
  
Fields  
---  
`environment` |  `enum (`[CloudEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CloudEnvironment)`)` The Cloud environment.  
`vpc  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource)`)` This item is deprecated!The cloud environment VPC. Deprecated.  
`project  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Resource)`)` This item is deprecated!The cloud environment project information. Deprecated: Use Resource.resource_ancestors  
`availabilityZone` |  `string` The cloud environment availability zone (different from region which is location.name).  
  
### Resource

JSON representation  
---  
      
    
    {
      "type": string,
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceType)),
      "resourceSubtype": string,
      "id": string,
      "name": string,
      "parent": string,
      "productObjectId": string,
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute))
      },
      "scheduledTask": {
        object ([ScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledTask))
      },
      "scheduledCronTask": {
        object ([ScheduledCronTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledCronTask))
      },
      "scheduledAnacronTask": {
        object ([ScheduledAnacronTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledAnacronTask))
      },
      "windowsScheduledTask": {
        object ([WindowsScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WindowsScheduledTask))
      },
      "volume": {
        object ([Volume](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Volume))
      },
      "service": {
        object ([Service](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Service))
      }
    }  
  
Fields  
---  
`type  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use resource_type instead.  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceType)`)` Resource type.  
`resourceSubtype` |  `string` Resource sub-type (e.g. "BigQuery", "Bigtable").  
`id  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use resource.name or resource.product_object_id.  
`name` |  `string` The full name of the resource. For example, Google Cloud: //cloudresourcemanager.googleapis.com/projects/wombat-123, and AWS: arn:aws:iam::123456789012:user/johndoe.  
`parent  
**(deprecated)**` |  `string` This item is deprecated!The parent of the resource. For a database table, the parent is the database. For a storage object, the bucket name. Deprecated: use resource_ancestors.name.  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (a GUID, OID, or similar) This field can be used as an entity indicator for a Resource entity.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute)`)` Generic entity metadata attributes of the resource.  
`scheduledTask  
**(deprecated)**` |  `object (`[ScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledTask)`)` This item is deprecated!DEPRECATED: use windows_scheduled_task for Windows scheduled tasks or scheduled_cron_task for cron jobs. Information about a scheduled task associated with the resource.  
`scheduledCronTask` |  `object (`[ScheduledCronTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledCronTask)`)` Information about a scheduled cron task associated with the resource.  
`scheduledAnacronTask` |  `object (`[ScheduledAnacronTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ScheduledAnacronTask)`)` Information about a scheduled anacron task associated with the resource.  
`windowsScheduledTask` |  `object (`[WindowsScheduledTask](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WindowsScheduledTask)`)` Information about a Windows scheduled task associated with the resource.  
`volume` |  `object (`[Volume](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Volume)`)` Information about a storage volume associated with the resource.  
`service` |  `object (`[Service](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Service)`)` Information about a Windows service associated with the resource.  
  
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
`author` |  `string` The account name that authored or last modified the scheduled task.  
  
### ScheduledCronTask

JSON representation  
---  
      
    
    {
      "minute": string,
      "hour": string,
      "monthDay": string,
      "month": string,
      "weekDay": string,
      "comment": string,
      "author": string,
      "event": string,
      "path": string
    }  
  
Fields  
---  
`minute` |  `string` Crontab minute field. Value is an integer between 0 and 59 and can also be a range or list of values (e.g., "0-59", "0-59/5", "0,15,30,45") and it // can also be an asterisk (*) to indicate first-last minutes. For more information on the format, see <https://www.linux.org/docs/man5/crontab.html>  
`hour` |  `string` Crontab hour field. Value is an integer between 0 and 23, a range or list of values (e.g., "0-6", "*/2", "1,2"), or an asterisk (*) to indicate first-last hours.  
`monthDay` |  `string` Crontab day of month field. Value is an integer between 1 and 31, a range or list of values (e.g., "1-7", "1-31/7", "1,15"), or an asterisk (*) to indicate first-last days of month.  
`month` |  `string` Crontab month field. Value is an integer between 1 and 12 or a 3-letter name (e.g., "Jan"), a range or list of values (e.g., "1-3", "*/2", "1,6"), or an asterisk (*) to indicate first-last months.  
`weekDay` |  `string` Crontab day of week field. Value is an integer between 0 and 7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a range or list of values (e.g., "1-5", "0,6"), or an asterisk (*) to indicate first-last days of week.  
`comment` |  `string` A comment or description for the task.  
`author` |  `string` The author or creator of the task.  
`event` |  `string` Crontab special string or event (e.g., "@reboot", "@daily").  
`path` |  `string` The PATH environment variable defined in the crontab file.  
  
### ScheduledAnacronTask

JSON representation  
---  
      
    
    {
      "period": string,
      "delayMinutes": string,
      "jobId": string,
      "path": string,
      "sourceLine": string
    }  
  
Fields  
---  
`period` |  `string` Anacrontab period field. Value is an integer in days, or a string like "@daily", "@weekly", or "@monthly".  
`delayMinutes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The delay in minutes before the job is run.  
`jobId` |  `string` The unique identifier of the job.  
`path` |  `string` The PATH environment variable defined in the anacrontab file.  
`sourceLine` |  `string` The original source line from the anacrontab file.  
  
### WindowsScheduledTask

JSON representation  
---  
      
    
    {
      "author": string,
      "virtualPath": string,
      "exitCode": integer,
      "state": enum ([TaskState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskState)),
      "logonType": enum ([TaskLogonType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskLogonType)),
      "taskActions": [
        {
          object ([TaskAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskAction))
        }
      ],
      "taskTriggers": [
        {
          object ([TaskTrigger](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskTrigger))
        }
      ]
    }  
  
Fields  
---  
`author` |  `string` The account name that authored or last modified the scheduled task.  
`virtualPath` |  `string` The task's path in the Task Scheduler library.  
`exitCode` |  `integer` The result which was returned the last time the registered task was run.  
`state` |  `enum (`[TaskState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskState)`)` The operation state of the task.  
`logonType` |  `enum (`[TaskLogonType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskLogonType)`)` The logon type of the task.  
`taskActions[]` |  `object (`[TaskAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskAction)`)` The actions of the scheduled task.  
`taskTriggers[]` |  `object (`[TaskTrigger](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TaskTrigger)`)` The triggers of the scheduled task.  
  
### TaskAction

JSON representation  
---  
      
    
    {
      "actionType": enum ([ActionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ActionType)),
      "execArguments": [
        string
      ],
      "execWorkingDirectory": string,
      "comClassId": string,
      "comData": string
    }  
  
Fields  
---  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ActionType)`)` The action type of the task.  
`execArguments[]` |  `string` The arguments of the task. This field is only populated if the task action type is EXEC.  
`execWorkingDirectory` |  `string` The executable working directory of the task. This field is only populated if the task action type is EXEC.  
`comClassId` |  `string` The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.  
`comData` |  `string` The data of the task. This field is only populated if the task action type is COM_HANDLER.  
  
### TaskTrigger

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "duration": string,
      "interval": string,
      "triggerType": enum ([TriggerType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TriggerType))
    }  
  
Fields  
---  
`enabled` |  `boolean` Indicates whether the task trigger is enabled.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of the task trigger repetition.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`interval` |  `string` The interval between each repetition of the task. The format for this string is `P<days>DT<hours>H<minutes>M<seconds>S` (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and "PT20M" is 20 minutes). The maximum time allowed is 31 days, and the minimum time allowed is 1 minute.  
`triggerType` |  `enum (`[TriggerType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TriggerType)`)` The trigger frequency of the task.  
  
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
      "serviceType": enum ([ServiceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ServiceType)),
      "serviceTypes": [
        enum ([ServiceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ServiceType))
      ],
      "startupType": enum ([StartupType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StartupType)),
      "state": enum ([State](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.State))
    }  
  
Fields  
---  
`displayName` |  `string` The user-friendly display name of the service.  
`serviceType  
**(deprecated)**` |  `enum (`[ServiceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ServiceType)`)` This item is deprecated!Deprecated: use service_types instead. The type of service.  
`serviceTypes[]` |  `enum (`[ServiceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ServiceType)`)` The list of service types.  
`startupType` |  `enum (`[StartupType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StartupType)`)` The startup type of the service.  
`state` |  `enum (`[State](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.State)`)` The status of the service.  
  
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
      "type": enum ([PermissionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PermissionType))
    }  
  
Fields  
---  
`name` |  `string` Name of the permission (e.g. chronicle.analyst.updateRule).  
`description` |  `string` Description of the permission (e.g. 'Ability to update detect rules').  
`type` |  `enum (`[PermissionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PermissionType)`)` Type of the permission.  
  
### Role

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type))
    }  
  
Fields  
---  
`name` |  `string` System role name for user.  
`description` |  `string` System role description for user.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type)`)` System role type for well known roles.  
  
### TimeOff

JSON representation  
---  
      
    
    {
      "interval": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval))
      },
      "description": string
    }  
  
Fields  
---  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval)`)` Interval duration of the leave.  
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
  
### SSLCertificate

JSON representation  
---  
      
    
    {
      "certSignature": {
        object ([CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CertSignature))
      },
      "extension": {
        object ([Extension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Extension))
      },
      "certExtensions": {
        object
      },
      "firstSeenTime": string,
      "issuer": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Subject))
      },
      "ec": {
        object ([EC](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EC))
      },
      "serialNumber": string,
      "signatureAlgorithm": string,
      "size": string,
      "subject": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Subject))
      },
      "thumbprint": string,
      "thumbprintSha256": string,
      "validity": {
        object ([Validity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Validity))
      },
      "version": string,
      "publicKey": {
        object ([PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PublicKey))
      }
    }  
  
Fields  
---  
`certSignature` |  `object (`[CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CertSignature)`)` Certificate's signature and algorithm.  
`extension  
**(deprecated)**` |  `object (`[Extension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Extension)`)` This item is deprecated!(DEPRECATED) certificate's extension.  
`certExtensions` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Certificate's extensions.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date the certificate was first retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issuer` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Subject)`)` Certificate's issuer data.  
`ec` |  `object (`[EC](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EC)`)` EC public key information.  
`serialNumber` |  `string` Certificate's serial number hexdump.  
`signatureAlgorithm` |  `string` Algorithm used for the signature (for example, "sha1RSA").  
`size` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Certificate content length.  
`subject` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Subject)`)` Certificate's subject data.  
`thumbprint` |  `string` Certificate's content SHA1 hash.  
`thumbprintSha256` |  `string` Certificate's content SHA256 hash.  
`validity` |  `object (`[Validity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Validity)`)` Certificate's validity period.  
`version` |  `string` Certificate version (typically "V1", "V2" or "V3").  
`publicKey` |  `object (`[PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PublicKey)`)` Public key information.  
  
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
        object ([AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthorityKeyId))
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
`authorityKeyId` |  `object (`[AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthorityKeyId)`)` Identifies the public key to be used to verify the signature on this certificate or CRL.  
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
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
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
        object ([RSA](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RSA))
      }
    }  
  
Fields  
---  
`algorithm` |  `string` Any of "RSA", "DSA" or "EC". Indicates the algorithm used to generate the certificate.  
`rsa` |  `object (`[RSA](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RSA)`)` RSA public key information.  
  
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
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network))
      },
      "asOwner": string,
      "asn": string,
      "jarm": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SSLCertificate))
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
          object ([Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tunnels))
        }
      ],
      "anonymous": boolean,
      "artifactClient": {
        object ([ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ArtifactClient))
      },
      "risks": [
        string
      ]
    }  
  
Fields  
---  
`ip` |  `string` IP address of the artifact. This field can be used as an entity indicator for an external destination IP entity.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence)`)` The prevalence of the artifact within the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First seen timestamp of the IP in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last seen timestamp of the IP address in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Location of the Artifact's IP address.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network)`)` Network information related to the Artifact's IP address.  
`asOwner` |  `string` Owner of the Autonomous System to which the IP address belongs.  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Autonomous System Number to which the IP address belongs.  
`jarm` |  `string` The JARM hash for the IP address. (<https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a)>.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SSLCertificate)`)` SSL certificate information about the IP address.  
`lastHttpsCertificateDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Most recent date for the certificate in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`regionalInternetRegistry` |  `string` RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).  
`tags[]` |  `string` Identification attributes  
`whois` |  `string` WHOIS information as returned from the pertinent WHOIS server.  
`whoisDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date of the last update of the WHOIS record in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tunnels[]` |  `object (`[Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tunnels)`)` VPN tunnels.  
`anonymous` |  `boolean` Whether the VPN tunnels are configured for anonymous browsing or not.  
`artifactClient` |  `object (`[ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ArtifactClient)`)` Entity or software accessing or utilizing network resources.  
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
      "direction": enum ([Direction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Direction)),
      "ipProtocol": enum ([IpProtocol](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IpProtocol)),
      "ipv6": boolean,
      "applicationProtocol": enum ([ApplicationProtocol](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ApplicationProtocol)),
      "ftp": {
        object ([Ftp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Ftp))
      },
      "email": {
        object ([Email](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Email))
      },
      "dns": {
        object ([Dns](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Dns))
      },
      "dhcp": {
        object ([Dhcp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Dhcp))
      },
      "http": {
        object ([Http](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Http))
      },
      "tls": {
        object ([Tls](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tls))
      },
      "smtp": {
        object ([Smtp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Smtp))
      },
      "asn": string,
      "dnsDomain": string,
      "carrierName": string,
      "organizationName": string,
      "ipSubnetRange": string,
      "isProxy": boolean,
      "proxyInfo": {
        object ([ProxyInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProxyInfo))
      },
      "connectionState": enum ([ConnectionState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ConnectionState))
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
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Direction)`)` The direction of network traffic.  
`ipProtocol` |  `enum (`[IpProtocol](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IpProtocol)`)` The IP protocol.  
`ipv6` |  `boolean` True if IPv6 is used.  
`applicationProtocol` |  `enum (`[ApplicationProtocol](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ApplicationProtocol)`)` The application protocol.  
`ftp` |  `object (`[Ftp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Ftp)`)` FTP info.  
`email` |  `object (`[Email](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Email)`)` Email info for the sender/recipient.  
`dns` |  `object (`[Dns](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Dns)`)` DNS info.  
`dhcp` |  `object (`[Dhcp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Dhcp)`)` DHCP info.  
`http` |  `object (`[Http](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Http)`)` HTTP info.  
`tls` |  `object (`[Tls](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tls)`)` TLS info.  
`smtp` |  `object (`[Smtp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Smtp)`)` SMTP info. Store fields specific to SMTP not covered by Email.  
`asn` |  `string` Autonomous system number.  
`dnsDomain` |  `string` DNS domain name.  
`carrierName` |  `string` Carrier identification.  
`organizationName` |  `string` Organization name (e.g Google).  
`ipSubnetRange` |  `string` Associated human-readable IP subnet range (e.g. 10.1.2.0/24).  
`isProxy` |  `boolean` Whether the IP address is a known proxy.  
`proxyInfo` |  `object (`[ProxyInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProxyInfo)`)` Proxy information. Only set if is_proxy is true.  
`connectionState` |  `enum (`[ConnectionState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ConnectionState)`)` The state of the network connection.  
  
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
`bounceAddress` |  `string` The envelope from address. <https://en.wikipedia.org/wiki/Bounce_address>  
  
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
          object ([Question](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Question))
        }
      ],
      "answers": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord))
        }
      ],
      "authority": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord))
        }
      ],
      "additional": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord))
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
`questions[]` |  `object (`[Question](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Question)`)` A list of domain protocol message questions.  
`answers[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord)`)` A list of answers to the domain name query.  
`authority[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord)`)` A list of domain name servers which verified the answers to the domain name queries.  
`additional[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceRecord)`)` A list of additional domain name servers that can be used to verify the answer to the domain.  
  
### Question

JSON representation  
---  
      
    
    {
      "name": string,
      "type": integer,
      "class": integer,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence))
      }
    }  
  
Fields  
---  
`name` |  `string` The domain name.  
`type` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the type of the query.  
`class` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The code specifying the class of the query.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence)`)` The prevalence of the domain within the customer's environment.  
  
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
      "opcode": enum ([OpCode](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OpCode)),
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
          object ([Option](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Option))
        }
      ],
      "type": enum ([MessageType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.MessageType)),
      "leaseTimeSeconds": integer,
      "clientHostname": string,
      "clientIdentifier": string,
      "requestedAddress": string,
      "clientIdentifierString": string
    }  
  
Fields  
---  
`opcode` |  `enum (`[OpCode](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OpCode)`)` The BOOTP op code.  
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
`options[]` |  `object (`[Option](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Option)`)` List of DHCP options.  
`type` |  `enum (`[MessageType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.MessageType)`)` DHCP message type.  
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
        object ([UserAgentProto](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UserAgentProto))
      }
    }  
  
Fields  
---  
`method` |  `string` The HTTP request method (e.g. "GET", "POST", "PATCH", "DELETE").  
`referralUrl` |  `string` The URL for the HTTP referer.  
`userAgent` |  `string` The User-Agent request header which includes the application type, operating system, software vendor or software version of the requesting software user agent.  
`responseCode` |  `integer` The response status code, for example 200, 302, 404, or 500.  
`parsedUserAgent` |  `object (`[UserAgentProto](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UserAgentProto)`)` The parsed user_agent string.  
  
### UserAgentProto

JSON representation  
---  
      
    
    {
      "family": enum ([Family](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Family)),
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
      "osType": enum ([OSType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OSType)),
      "osVariantType": enum ([OSVariantType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OSVariantType)),
      "browserType": enum ([BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserType)),
      "browserVariantType": enum ([BrowserVariantType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserVariantType)),
      "annotation": [
        {
          object ([Annotation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Annotation))
        }
      ]
    }  
  
Fields  
---  
`family` |  `enum (`[Family](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Family)`)` User agent family captures the type of browser/app at a high-level e.g. MSIE, Gecko, Safari etc..  
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
`osType` |  `enum (`[OSType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OSType)`)` The OS type of the device in enum format.  
`osVariantType` |  `enum (`[OSVariantType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OSVariantType)`)` The OS variant of the device in enum format.  
`browserType` |  `enum (`[BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserType)`)` The browser type of the device in enum format.  
`browserVariantType` |  `enum (`[BrowserVariantType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserVariantType)`)` The browser variant type of the device in enum format.  
`annotation[]` |  `object (`[Annotation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Annotation)`)`  
  
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
        object ([Client](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Client))
      },
      "server": {
        object ([Server](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Server))
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
`client` |  `object (`[Client](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Client)`)` Certificate information for the client certificate.  
`server` |  `object (`[Server](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Server)`)` Certificate information for the server certificate.  
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
        object ([Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Certificate))
      },
      "ja3": string,
      "serverName": string,
      "supportedCiphers": [
        string
      ],
      "ja4": string
    }  
  
Fields  
---  
`certificate` |  `object (`[Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Certificate)`)` Client certificate.  
`ja3` |  `string` JA3 hash from the TLS ClientHello, as a hex-encoded string.  
`serverName` |  `string` Host name of the server, that the client is connecting to.  
`supportedCiphers[]` |  `string` Ciphers supported by the client during client hello.  
`ja4` |  `string` JA4 hash from the TLS ClientHello, as a hex-encoded string.  
  
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
        object ([Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Certificate))
      },
      "ja3s": string,
      "ja4s": string
    }  
  
Fields  
---  
`certificate` |  `object (`[Certificate](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Certificate)`)` Server certificate.  
`ja3s` |  `string` JA3 hash from the TLS ServerHello, as a hex-encoded string.  
`ja4s` |  `string` JA4 hash from the TLS ServerHello, as a hex-encoded string.  
  
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
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon))
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
          object ([Tracker](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tracker))
        }
      ]
    }  
  
Fields  
---  
`url` |  `string` URL.  
`categories[]` |  `string` Categorisation done by VirusTotal partners.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon)`)` Difference hash and MD5 hash of the URL's.  
`htmlMeta` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Meta tags (only for URLs downloading HTML).  
`lastFinalUrl` |  `string` If the original URL redirects, where does it end.  
`lastHttpResponseCode` |  `integer` HTTP response code of the last response.  
`lastHttpResponseContentLength` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Length in bytes of the content received.  
`lastHttpResponseContentSha256` |  `string` URL response body's SHA256 hash.  
`lastHttpResponseCookies` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Website's cookies.  
`lastHttpResponseHeaders` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Headers and values of the last HTTP response.  
`tags[]` |  `string` Tags.  
`title` |  `string` Webpage title.  
`trackers[]` |  `object (`[Tracker](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tracker)`)` Trackers found in the URL in a historical manner.  
  
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
      "browserType": enum ([BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserType_1)),
      "browserVersion": string,
      "firstVisitTime": string,
      "lastVisitTime": string,
      "profile": string,
      "typed": boolean,
      "visitType": enum ([UrlVisitType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UrlVisitType)),
      "hidden": boolean,
      "requestOriginUri": string,
      "visitCount": string,
      "visitCountCriteria": string,
      "indexedContent": string,
      "firstBookmarkedTime": string,
      "cookies": [
        {
          object ([Cookie](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cookie))
        }
      ],
      "typedCount": string,
      "visitSource": enum ([VisitSource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VisitSource))
    }  
  
Fields  
---  
`browserType` |  `enum (`[BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BrowserType_1)`)` The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).  
`browserVersion` |  `string` The browser version.  
`firstVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the initial visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the most recent visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`profile` |  `string` The browser profile associated with the history entry.  
`typed` |  `boolean` A boolean value indicating if the URL was typed by the user.  
`visitType` |  `enum (`[UrlVisitType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UrlVisitType)`)` Describes the type of navigation or visit (e.g., direct, redirect, etc.).  
`hidden` |  `boolean` A boolean value indicating if the history entry is hidden.  
`requestOriginUri` |  `string` Indicates the URI from which the current visit originated.  
`visitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of times the Url has been visited.  
`visitCountCriteria` |  `string` Describes the criteria used to calculate the visit_count.  
`indexedContent` |  `string` Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.  
`firstBookmarkedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the first time the URL was bookmarked.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cookies[]` |  `object (`[Cookie](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Cookie)`)` Information about the cookies.  
`typedCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the URL was visited with this specific visit type and visit source.  
`visitSource` |  `enum (`[VisitSource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VisitSource)`)` The source of the visit.  
  
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
      "sameSite": enum ([CookieSameSite](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CookieSameSite)),
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
`sameSite` |  `enum (`[CookieSameSite](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.CookieSameSite)`)` Affects cross-site request behavior.  
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
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute))
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
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute)`)` Generic entity metadata attributes of the group.  
`emailAddresses[]` |  `string` Email addresses of the group.  
`windowsSid` |  `string` Microsoft Windows SID of the group.  
  
### Process

JSON representation  
---  
      
    
    {
      "pid": string,
      "parentPid": string,
      "parentProcess": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process))
      },
      "file": {
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.File))
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
      "tokenElevationType": enum ([TokenElevationType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TokenElevationType)),
      "productSpecificParentProcessId": string,
      "ipv6": boolean,
      "kernelDuration": string,
      "userDuration": string,
      "realDuration": string,
      "state": enum ([State](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.State_1))
    }  
  
Fields  
---  
`pid` |  `string` The process ID. This field can be used as an entity indicator for process entities.  
`parentPid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the parent process. Deprecated: use parent_process.pid instead.  
`parentProcess` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Process)`)` Information about the parent process.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.File)`)` Information about the file in use by the process.  
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
`tokenElevationType` |  `enum (`[TokenElevationType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.TokenElevationType)`)` The elevation type of the process on Microsoft Windows. This type determines whether any privileges are removed when you enable User Account Control (UAC).  
`productSpecificParentProcessId  
**(deprecated)**` |  `string` This item is deprecated!A product-specific ID for the parent process. Please use  `parent_process.product_specific_process_id` instead.  
`ipv6` |  `boolean` Whether the process is an IPv6 process.  
`kernelDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The kernel time spent in the process.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`userDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The user time spent in the process.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`realDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The real time spent in the process. This is the sum of the kernel and user time.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.State_1)`)` The state of the process.  
  
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
        object ([FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadata))
      },
      "securityResult": {
        object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
      },
      "peFile": {
        object ([FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataPE))
      },
      "ssdeep": string,
      "vhash": string,
      "ahash": string,
      "authentihash": string,
      "symhash": string,
      "prefetchFileMetadata": {
        object ([PrefetchFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PrefetchFileMetadata))
      },
      "fileType": enum ([FileType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileType)),
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
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence))
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
        object ([ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ExifInfo))
      },
      "signatureInfo": {
        object ([SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SignatureInfo))
      },
      "pdfInfo": {
        object ([PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PDFInfo))
      },
      "firstSubmissionTime": string,
      "lastSubmissionTime": string,
      "mainIcon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon))
      },
      "ntfs": {
        object ([NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.NtfsFileMetadata))
      },
      "appCompatCache": {
        object ([AppCompatMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AppCompatMetadata))
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
**(deprecated)**` |  `object (`[FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadata)`)` This item is deprecated!Metadata associated with the file. Deprecate FileMetadata in favor of using fields in File.  
`securityResult` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` Google Cloud Threat Intelligence (GCTI) security result for the file including threat context and detection metadata.  
`peFile` |  `object (`[FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataPE)`)` Metadata about the Portable Executable (PE) file.  
`ssdeep` |  `string` Ssdeep of the file  
`vhash` |  `string` Vhash of the file.  
`ahash  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. Use authentihash instead.  
`authentihash` |  `string` Authentihash of the file.  
`symhash` |  `string` SymHash of the file. Used for Mach-O (e.g. MacOS) binaries, to identify similar files based on their symbol table.  
`prefetchFileMetadata` |  `object (`[PrefetchFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PrefetchFileMetadata)`)` Metadata about the prefetch file.  
`fileType` |  `enum (`[FileType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileType)`)` FileType field.  
`capabilitiesTags[]` |  `string` Capabilities tags.  
`names[]` |  `string` Names fields.  
`tags[]` |  `string` Tags for the file.  
`lastModificationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastAccessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was accessed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Prevalence)`)` Prevalence of the file hash in the customer's environment.  
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
`exifInfo` |  `object (`[ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ExifInfo)`)` Exif metadata from different file formats extracted by exiftool.  
`signatureInfo` |  `object (`[SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SignatureInfo)`)` File signature information extracted from different tools.  
`pdfInfo` |  `object (`[PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PDFInfo)`)` Information about the PDF file structure.  
`firstSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mainIcon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Favicon)`)` Icon's relevant hashes.  
`ntfs` |  `object (`[NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.NtfsFileMetadata)`)` NTFS metadata.  
`appCompatCache` |  `object (`[AppCompatMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AppCompatMetadata)`)` Windows AppCompatCache (Application Compatibility) metadata.  
  
### FileMetadata

JSON representation  
---  
      
    
    {
      "pe": {
        object ([PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PeFileMetadata))
      }
    }  
  
Fields  
---  
`pe  
**(deprecated)**` |  `object (`[PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PeFileMetadata)`)` This item is deprecated!Metadata for Microsoft Windows PE files. Deprecate PeFileMetadata in favor of single File proto.  
  
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
          object ([FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSection))
        }
      ],
      "imports": [
        {
          object ([FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataImports))
        }
      ],
      "resource": [
        {
          object ([FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataPeResourceInfo))
        }
      ],
      "resourcesTypeCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringToInt64MapEntry))
        }
      ],
      "resourcesLanguageCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringToInt64MapEntry))
        }
      ],
      "resourcesTypeCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "resourcesLanguageCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "signatureInfo": {
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSignatureInfo))
      }
    }  
  
Fields  
---  
`imphash` |  `string` Imphash of the file.  
`entryPoint` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.pe-entry-point.  
`entryPointExiftool` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.exiftool.EntryPoint.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.pe-timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`compilationExiftoolTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.exiftool.TimeStamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`section[]` |  `object (`[FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSection)`)` FilemetadataSection fields.  
`imports[]` |  `object (`[FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataImports)`)` FilemetadataImports fields.  
`resource[]` |  `object (`[FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataPeResourceInfo)`)` FilemetadataPeResourceInfo fields.  
`resourcesTypeCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resources_type_count_str.  
`resourcesLanguageCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resources_language_count_str.  
`resourcesTypeCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5  
`resourcesLanguageCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10  
`signatureInfo  
**(deprecated)**` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSignatureInfo)`)` This item is deprecated!FilemetadataSignatureInfo field. deprecated, user File.signature_info instead.  
  
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
`languageCode` |  `string` Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification.  
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
          object ([SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SignerInfo))
        }
      ],
      "x509": [
        {
          object ([X509](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.X509))
        }
      ]
    }  
  
Fields  
---  
`verificationMessage` |  `string` Status of the certificate. Valid values are "Signed", "Unsigned" or a description of the certificate anomaly, if found.  
`verified` |  `boolean` True if verification_message == "Signed"  
`signer[]  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use signers field.  
`signers[]` |  `object (`[SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SignerInfo)`)` File metadata signer information. The order of the signers matters. Each element is a higher level authority, being the last the root authority.  
`x509[]` |  `object (`[X509](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.X509)`)` List of certificates.  
  
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
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSignatureInfo))
      },
      "codesign": {
        object ([FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataCodesign))
      }
    }  
  
Fields  
---  
`sigcheck` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataSignatureInfo)`)` Signature information extracted from the sigcheck tool.  
`codesign` |  `object (`[FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FileMetadataCodesign)`)` Signature information extracted from the codesign utility.  
  
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
          object ([UsnJournal](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UsnJournal))
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
`usnJournal[]` |  `object (`[UsnJournal](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UsnJournal)`)` NTFS USN journal.  
  
### UsnJournal

JSON representation  
---  
      
    
    {
      "attributesFlag": string,
      "attributes": enum ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute_1)),
      "fileAttributes": [
        enum ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute_1))
      ],
      "allocated": boolean,
      "reason": enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason)),
      "reasons": [
        enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason))
      ]
    }  
  
Fields  
---  
`attributesFlag` |  `string` File attributes flags from the USN record (e.g., "0x20").  
`attributes  
**(deprecated)**` |  `enum (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute_1)`)` This item is deprecated!Deprecated: Use file_attributes instead. File attributes from the USN record.  
`fileAttributes[]` |  `enum (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute_1)`)` File attributes from the USN record.  
`allocated` |  `boolean` Indicates whether the file is allocated in the Master File Table (MFT).  
`reason  
**(deprecated)**` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason)`)` This item is deprecated!Deprecated: Use reasons instead. Human-readable string describing the reason for the USN journal entry. (e.g., "USN_REASON_FILE_CREATE").  
`reasons[]` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason)`)` Human-readable string describing the reasons for the USN journal entry (e.g., "USN_REASON_FILE_CREATE").  
  
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
          object ([Hardware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Hardware))
        }
      ],
      "platformSoftware": {
        object ([PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PlatformSoftware))
      },
      "software": [
        {
          object ([Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Software))
        }
      ],
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "category": string,
      "type": enum ([AssetType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssetType)),
      "networkDomain": string,
      "creationTime": string,
      "firstDiscoverTime": string,
      "lastDiscoverTime": string,
      "systemLastUpdateTime": string,
      "lastBootTime": string,
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "deploymentStatus": enum ([DeploymentStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DeploymentStatus)),
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerability))
        }
      ],
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute))
      },
      "wmiPersistenceItem": {
        object ([WmiPersistenceItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WmiPersistenceItem))
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
`hardware[]` |  `object (`[Hardware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Hardware)`)` The asset hardware specifications.  
`platformSoftware` |  `object (`[PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.PlatformSoftware)`)` The asset operating system platform software.  
`software[]` |  `object (`[Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Software)`)` The asset software details.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Location of the asset.  
`category` |  `string` The category of the asset (e.g. "End User Asset", "Workstation", "Server").  
`type` |  `enum (`[AssetType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssetType)`)` The type of the asset (e.g. workstation or laptop or server).  
`networkDomain` |  `string` The network domain of the asset (e.g. "corp.acme.com")  
`creationTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Time the asset was created or provisioned. Deprecate: creation_time should be populated in Attribute as generic metadata.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`firstDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was first discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`systemLastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset system or OS was last updated. For all other operations that are not system updates (such as resizing a VM), use Attribute.last_update_time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBootTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last boot started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` This item is deprecated!Metadata labels for the asset. Deprecated: labels should be populated in Attribute as generic metadata.  
`deploymentStatus` |  `enum (`[DeploymentStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DeploymentStatus)`)` The deployment status of the asset for device lifecycle purposes.  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerability)`)` Vulnerabilities discovered on asset.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Attribute)`)` Generic entity metadata attributes of the asset.  
`wmiPersistenceItem` |  `object (`[WmiPersistenceItem](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WmiPersistenceItem)`)` Information about a WMI persistence item.  
  
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
`ram` |  `string` Amount of the hardware random access memory (RAM) in Mb.  
  
### PlatformSoftware

JSON representation  
---  
      
    
    {
      "platform": enum ([Platform](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Platform)),
      "platformVersion": string,
      "platformPatchLevel": string
    }  
  
Fields  
---  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Platform)`)` The platform operating system.  
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
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Permission))
        }
      ],
      "description": string,
      "vendorName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the software.  
`version` |  `string` The version of the software.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Permission)`)` System permissions granted to the software. For example, "android.permission.WRITE_EXTERNAL_STORAGE"  
`description` |  `string` The description of the software.  
`vendorName` |  `string` The name of the software vendor.  
  
### Vulnerability

JSON representation  
---  
      
    
    {
      "about": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "name": string,
      "description": string,
      "vendor": string,
      "scanStartTime": string,
      "scanEndTime": string,
      "firstFound": string,
      "lastFound": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Severity)),
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
`about` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` If the vulnerability is about a specific noun (e.g. executable), then add it here.  
`name` |  `string` Name of the vulnerability (e.g. "Unsupported OS Version detected").  
`description` |  `string` Description of the vulnerability.  
`vendor` |  `string` Vendor of scan that discovered vulnerability.  
`scanStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If the vulnerability was discovered during an asset scan, then this field should be populated with the time the scan started. This field can be left unset if the start time is not available or not applicable.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scanEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If the vulnerability was discovered during an asset scan, then this field should be populated with the time the scan ended. This field can be left unset if the end time is not available or not applicable.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`firstFound` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Products that maintain a history of vuln scans should populate first_found with the time that a scan first detected the vulnerability on this asset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastFound` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Products that maintain a history of vuln scans should populate last_found with the time that a scan last detected the vulnerability on this asset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Severity)`)` The severity of the vulnerability.  
`severityDetails` |  `string` Vendor-specific severity  
`cvssBaseScore` |  `number` CVSS Base Score in the range of 0.0 to 10.0. Useful for sorting.  
`cvssVector` |  `string` Vector of CVSS properties (e.g. "AV:L/AC:H/Au:N/C:N/I:P/A:C") Can be linked to via: <https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator>  
`cvssVersion` |  `string` Version of CVSS Vector/Score.  
`cveId` |  `string` Common Vulnerabilities and Exposures Id. <https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures> <https://cve.mitre.org/about/faqs.html#what_is_cve_id>  
`cveDescription` |  `string` Common Vulnerabilities and Exposures Description. <https://cve.mitre.org/about/faqs.html#what_is_cve_record>  
`vendorVulnerabilityId` |  `string` Vendor specific vulnerability id (e.g. Microsoft security bulletin id).  
`vendorKnowledgeBaseArticleId` |  `string` Vendor specific knowledge base article (e.g. "KBXXXXXX" from Microsoft). <https://en.wikipedia.org/wiki/Microsoft_Knowledge_Base> <https://access.redhat.com/knowledgebase>  
  
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
      "registryValueType": enum ([Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type_2)),
      "registryValueBinaryData": string
    }  
  
Fields  
---  
`registryKey` |  `string` Registry key associated with an application or system component (e.g., HKEY_, HKCU\Environment...).  
`registryValueName` |  `string` Name of the registry value associated with an application or system component (e.g. TEMP).  
`registryValueData` |  `string` Data associated with a registry value (e.g. %USERPROFILE%\Local Settings\Temp).  
`registryValueType` |  `enum (`[Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type_2)`)` Type of the registry value.  
`registryValueBinaryData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Binary data associated with a registry value. This field is only populated if the registry value type is BINARY. This field is not populated for other registry value types.A base64-encoded string.  
  
### Id

JSON representation  
---  
      
    
    {
      "namespace": enum ([Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)),
      "id": string,
      "stringId": string
    }  
  
Fields  
---  
`namespace` |  `enum (`[Namespace](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Namespace)`)` Namespace the id belongs to.  
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
      "verdict": enum ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict_1))
      // End of list of possible types for union field _verdict.
    
      // Union field _reputation can be only one of the following:
      "reputation": enum ([Reputation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reputation))
      // End of list of possible types for union field _reputation.
    
      // Union field _severity_score can be only one of the following:
      "severityScore": integer
      // End of list of possible types for union field _severity_score.
    
      // Union field _status can be only one of the following:
      "status": enum ([Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Status))
      // End of list of possible types for union field _status.
    
      // Union field _priority can be only one of the following:
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority))
      // End of list of possible types for union field _priority.
    
      // Union field _root_cause can be only one of the following:
      "rootCause": string
      // End of list of possible types for union field _root_cause.
    
      // Union field _reason can be only one of the following:
      "reason": enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason_1))
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
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict_1)`)` Describes reason a finding investigation was resolved.  
Union field `_reputation`.`_reputation` can be only one of the following:  
`reputation` |  `enum (`[Reputation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reputation)`)` Describes whether a finding was useful or not-useful.  
Union field `_severity_score`.`_severity_score` can be only one of the following:  
`severityScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Severity score for a finding set by an analyst.  
Union field `_status`.`_status` can be only one of the following:  
`status` |  `enum (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Status)`)` Describes the workflow status of a finding.  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority)`)` Priority of the Alert or Finding set by analyst.  
Union field `_root_cause`.`_root_cause` can be only one of the following:  
`rootCause` |  `string` Root cause of the Alert or Finding set by analyst.  
Union field `_reason`.`_reason` can be only one of the following:  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason_1)`)` Reason for closing the Case or Alert.  
Union field `_risk_score`.`_risk_score` can be only one of the following:  
`riskScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Risk score for a finding set by an analyst.  
Union field `_id`.`_id` can be only one of the following:  
`id` |  `string` Identifier for the investigation  
  
### Ai

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "sessionId": string,
      "type": enum ([AiType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AiType)),
      "software": [
        {
          object ([Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Software))
        }
      ],
      "owners": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User))
        }
      ],
      "displayName": string
    }  
  
Fields  
---  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the system (a GUID, OID, or similar). This field can be used as an entity indicator for an AI entity.  
`sessionId` |  `string` An ID which uniquely identifies one "session" of interaction with the AI system. For example, an alert triage agent might use the ID of an alert being investigated to trace the activities of multiple sub-systems.  
`type` |  `enum (`[AiType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AiType)`)` The type of the AI entity.  
`software[]` |  `object (`[Software](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Software)`)` Information about the vendor, version, name, etc. of the software that the AI system runs. An AI system can make use of multiple software packages or applications - for example, a Python script may run in a Notebook and use one or more particular LLM versions.  
`owners[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.User)`)` Information about the owner of the AI system.  
`displayName` |  `string` User-visible name of the AI system or agent. Example: "Workspace Assistant"  
  
### VariablesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FindingVariable))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[FindingVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.FindingVariable)`)`  
  
### FindingVariable

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type_1)),
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
        object ([BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BoolSequence))
      },
      "bytesSeq": {
        object ([BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BytesSequence))
      },
      "doubleSeq": {
        object ([DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DoubleSequence))
      },
      "int64Seq": {
        object ([Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Int64Sequence))
      },
      "uint64Seq": {
        object ([Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Uint64Sequence))
      },
      "stringSeq": {
        object ([StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringSequence))
      }
      // End of list of possible types for union field typed_value.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Type_1)`)` The type of the variable.  
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
`boolSeq` |  `object (`[BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BoolSequence)`)` The value in boolsequence format.  
`bytesSeq` |  `object (`[BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BytesSequence)`)` The value in bytessequence format.  
`doubleSeq` |  `object (`[DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DoubleSequence)`)` The value in doublesequence format.  
`int64Seq` |  `object (`[Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Int64Sequence)`)` The value in int64sequence format.  
`uint64Seq` |  `object (`[Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Uint64Sequence)`)` The value in uint64sequence format.  
`stringSeq` |  `object (`[StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringSequence)`)` The value in stringsequence format.  
  
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
          object ([Tactic](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tactic))
        }
      ],
      "techniques": [
        {
          object ([Technique](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Technique))
        }
      ]
    }  
  
Fields  
---  
`version` |  `string` ATT&CK version (e.g. 12.1).  
`tactics[]` |  `object (`[Tactic](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tactic)`)` Tactics employed.  
`techniques[]` |  `object (`[Technique](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Technique)`)` Techniques employed.  
  
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
      "type": enum ([AssociationType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssociationType)),
      "name": string,
      "description": string,
      "role": string,
      "sourceCountry": string,
      "alias": [
        {
          object ([AssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssociationAlias))
        }
      ],
      "firstReferenceTime": string,
      "lastReferenceTime": string,
      "industriesAffected": [
        string
      ],
      "associatedActors": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association))
        }
      ],
      "regionCode": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "sponsorRegion": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
      },
      "targetedRegions": [
        {
          object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location))
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
`type` |  `enum (`[AssociationType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssociationType)`)` Signifies the type of association.  
`name` |  `string` Name of the threat actor/malware.  
`description` |  `string` Human readable description about the association.  
`role` |  `string` Role of the malware. Not applicable for threat actor.  
`sourceCountry  
**(deprecated)**` |  `string` This item is deprecated!Name of the country the threat originated from.  
`alias[]` |  `object (`[AssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AssociationAlias)`)` Different aliases of the threat actor given by different sources.  
`firstReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`industriesAffected[]` |  `string` List of industries the threat actor affects.  
`associatedActors[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association)`)` List of associated threat actors for a malware. Not applicable for threat actors.  
`regionCode` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Name of the country, the threat is originating from.  
`sponsorRegion` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Sponsor region of the threat actor.  
`targetedRegions[]` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Location)`)` Targeted regions.  
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
        object ([ProviderMLVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProviderMLVerdict))
      },
      "analystVerdict": {
        object ([AnalystVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AnalystVerdict))
      }
    }  
  
Fields  
---  
`sourceCount` |  `integer` Number of sources from which intelligence was extracted.  
`responseCount` |  `integer` Total response count across all sources.  
`neighbourInfluence` |  `string` Describes the neighbour influence of the verdict.  
`verdict` |  `object (`[ProviderMLVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProviderMLVerdict)`)` ML Verdict provided by sources like Mandiant.  
`analystVerdict` |  `object (`[AnalystVerdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AnalystVerdict)`)` Human analyst verdict provided by sources like Mandiant.  
  
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
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source))
        }
      ],
      "thirdPartySources": [
        {
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source))
        }
      ]
    }  
  
Fields  
---  
`sourceProvider` |  `string` Source provider giving the ML verdict.  
`benignCount` |  `integer` Count of responses where this IoC was marked benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked malicious.  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`mandiantSources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source)`)` List of mandiant sources from which the verdict was generated.  
`thirdPartySources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source)`)` List of third-party sources from which the verdict was generated.  
  
### Source

JSON representation  
---  
      
    
    {
      "name": string,
      "benignCount": integer,
      "maliciousCount": integer,
      "quality": enum ([ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)),
      "responseCount": integer,
      "sourceCount": integer,
      "threatIntelligenceSources": [
        {
          object ([Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Name of the IoC source.  
`benignCount` |  `integer` Count of responses where this IoC was marked benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked malicious.  
`quality` |  `enum (`[ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)`)` Quality of the IoC mapping extracted from the source.  
`responseCount` |  `integer` Total response count from this source.  
`sourceCount` |  `integer` Number of sources from which intelligence was extracted.  
`threatIntelligenceSources[]` |  `object (`[Source](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Source)`)` Different threat intelligence sources from which IoC info was extracted.  
  
### AnalystVerdict

JSON representation  
---  
      
    
    {
      "confidenceScore": integer,
      "verdictTime": string,
      "verdictResponse": enum ([VerdictResponse](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictResponse))
    }  
  
Fields  
---  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`verdictTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp at which the verdict was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictResponse` |  `enum (`[VerdictResponse](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictResponse)`)` Details of the verdict.  
  
### VerdictInfo

JSON representation  
---  
      
    
    {
      "sourceCount": integer,
      "responseCount": integer,
      "neighbourInfluence": string,
      "verdictType": enum ([VerdictType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictType)),
      "sourceProvider": string,
      "benignCount": integer,
      "maliciousCount": integer,
      "confidenceScore": integer,
      "iocStats": [
        {
          object ([IoCStats](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IoCStats))
        }
      ],
      "verdictTime": string,
      "verdictResponse": enum ([VerdictResponse](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictResponse)),
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
`verdictType` |  `enum (`[VerdictType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictType)`)` Type of verdict.  
`sourceProvider` |  `string` Source provider giving the machine learning verdict.  
`benignCount` |  `integer` Count of responses where this IoC was marked as benign.  
`maliciousCount` |  `integer` Count of responses where this IoC was marked as malicious.  
`confidenceScore` |  `integer` Confidence score of the verdict.  
`iocStats[]` |  `object (`[IoCStats](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IoCStats)`)` List of IoCStats from which the verdict was generated.  
`verdictTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the verdict was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdictResponse` |  `enum (`[VerdictResponse](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.VerdictResponse)`)` Details about the verdict.  
`globalCustomerCount` |  `integer` Global customer count over the last 30 days  
`globalHitsCount` |  `integer` Global hit count over the last 30 days.  
`pwn` |  `boolean` Whether one or more Mandiant incident response customers had this indicator in their environment.  
`categoryDetails` |  `string` Tags related to the verdict.  
`pwnFirstTaggedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp of the first time a pwn was associated to this entity.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### IoCStats

JSON representation  
---  
      
    
    {
      "iocStatsType": enum ([IoCStatsType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IoCStatsType)),
      "firstLevelSource": string,
      "secondLevelSource": string,
      "benignCount": integer,
      "quality": enum ([ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)),
      "maliciousCount": integer,
      "responseCount": integer,
      "sourceCount": integer
    }  
  
Fields  
---  
`iocStatsType` |  `enum (`[IoCStatsType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.IoCStatsType)`)` Describes the source of the IoCStat.  
`firstLevelSource` |  `string` Name of first level IoC source, for example Mandiant or a third-party.  
`secondLevelSource` |  `string` Name of the second-level IoC source, for example Crowdsourced Threat Analysis or Knowledge Graph.  
`benignCount` |  `integer` Count of responses where the IoC was identified as benign.  
`quality` |  `enum (`[ProductConfidence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ProductConfidence)`)` Level of confidence in the IoC mapping extracted from the source.  
`maliciousCount` |  `integer` Count of responses where the IoC was identified as malicious.  
`responseCount` |  `integer` Total number of response from the source.  
`sourceCount` |  `integer` Number of sources from which information was extracted.  
  
### ThreatCollectionItem

JSON representation  
---  
      
    
    {
      "id": string,
      "type": enum ([ThreatCollectionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatCollectionType)),
      "altNames": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` The ID of the threat collection.  
`type` |  `enum (`[ThreatCollectionType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ThreatCollectionType)`)` The type of threat collection, for example, "campaign".  
`altNames[]` |  `string` The name of the threat collection.  
  
### Reference

JSON representation  
---  
      
    
    {
      "event": {
        object ([UDM](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UDM))
      },
      "entity": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Entity))
      },
      "joinedDataTableRows": [
        {
          object ([DataTableRowInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.DataTableRowInfo))
        }
      ],
      "graphEnrichment": {
        object ([EntityGraphEnrichment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.EntityGraphEnrichment))
      },
      "id": {
        object ([Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Id))
      },
      "logBatchToken": string
    }  
  
Fields  
---  
`event` |  `object (`[UDM](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UDM)`)` Only one of event or entity will be populated for a single reference. Start one-of Event being referenced.  
`entity` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Entity)`)` Entity being referenced. In cases where the entity graph is overridden by data table, this will represent the original entity. End one-of  
`joinedDataTableRows[]` |  `object (`[DataTableRowInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.DataTableRowInfo)`)` The data table rows joined with the event.  
`graphEnrichment` |  `object (`[EntityGraphEnrichment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.EntityGraphEnrichment)`)` The entity graph enrichment details. Only set when the reference is an Entity which has been overridden by a data table or appended from a data table.  
`id` |  `object (`[Id](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Id)`)` Id being referenced. This field will also be populated for both event and entity with the event id. For detections, only this field will be populated.  
`logBatchToken` |  `string` The log batch token of the event being referenced. This field is used to fetch the raw log associated with the event in some legacy systems. This field is only populated for events/entities.  
  
### UDM

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Metadata))
      },
      "additional": {
        object
      },
      "principal": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "src": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "target": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "intermediary": [
        {
          object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
        }
      ],
      "observer": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "about": [
        {
          object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
        }
      ],
      "securityResult": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
        }
      ],
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network))
      },
      "extensions": {
        object ([Extensions](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Extensions))
      },
      "extracted": {
        object
      },
    
      // Union field _grouped can be only one of the following:
      "grouped": {
        object ([GroupedFields](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.GroupedFields))
      }
      // End of list of possible types for union field _grouped.
    }  
  
Fields  
---  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Metadata)`)` Event metadata such as timestamp, source product, etc.  
`additional` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Any important vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model.  
`principal` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents the acting entity that originates the activity described in the event. The principal must include at least one machine detail (hostname, MACs, IPs, port, product-specific identifiers like an EDR asset ID) or user detail (for example, username), and optionally include process details. It must NOT include any of the following fields: email, files, registry keys or values.  
`src` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents a source entity being acted upon by the participant along with the device or process context for the source object (the machine where the source object resides). For example, if user U copies file A on machine X to file B on machine Y, both file A and machine X would be specified in the src portion of the UDM event.  
`target` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents a target entity being referenced by the event or an object on the target entity. For example, in a firewall connection from device A to device B, A is described as the principal and B is described as the target. For a process injection by process C into target process D, process C is described as the principal and process D is described as the target.  
`intermediary[]` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents details on one or more intermediate entities processing activity described in the event. This includes device details about a proxy server or SMTP relay server. If an active event (that has a principal and possibly target) passes through any intermediaries, they're added here. Intermediaries can impact the overall action, for example blocking or modifying an ongoing request. A rule of thumb here is that 'principal', 'target', and description of the initial action should be the same regardless of the intermediary or its action. A successful network connection from A->B should look the same in principal/target/intermediary as one blocked by firewall C: principal: A, target: B (intermediary: C).  
`observer` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner), which is not a direct intermediary, but which observes and reports on the event in question.  
`about[]` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Represents entities referenced by the event that are not otherwise described in principal, src, target, intermediary or observer. For example, it could be used to track email file attachments, domains/URLs/IPs embedded within an email body, and DLLs that are loaded during a PROCESS_LAUNCH event.  
`securityResult[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` A list of security results.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Network)`)` All network details go here, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).  
`extensions` |  `object (`[Extensions](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Extensions)`)` All other first-class, event-specific metadata goes in this message. Do not place protocol metadata in Extensions; put it in Network.  
`extracted` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Flattened fields extracted from the log.  
Union field `_grouped`.`_grouped` can be only one of the following:  
`grouped` |  `object (`[GroupedFields](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.GroupedFields)`)` Related UDM fields that are grouped together.  
  
### Metadata

JSON representation  
---  
      
    
    {
      "id": string,
      "productLogId": string,
      "eventTimestamp": string,
      "eventTimestampAttributes": [
        enum ([EventTimestampAttribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EventTimestampAttribute))
      ],
      "collectedTimestamp": string,
      "ingestedTimestamp": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EventType)),
      "vendorName": string,
      "productName": string,
      "productVersion": string,
      "productEventType": string,
      "productDeploymentId": string,
      "description": string,
      "urlBackToProduct": string,
      "ingestionLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "tags": {
        object ([Tags](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tags))
      },
      "enrichmentState": enum ([EnrichmentState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EnrichmentState)),
      "logType": string,
      "baseLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessLabels))
      },
      "enrichmentLabels": {
        object ([DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessLabels))
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
`eventTimestampAttributes[]` |  `enum (`[EventTimestampAttribute](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EventTimestampAttribute)`)` Attributes associated with event_timestamp. This field is used to distinguish between different types of timestamps that can be used to represent the event_timestamp.  
`collectedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was collected by the vendor's local collection infrastructure.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ingestedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The GMT timestamp when the event was ingested (received) by Google SecOps.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EventType)`)` The event type. If an event has multiple possible types, this specifies the most specific type.  
`vendorName` |  `string` The name of the product vendor.  
`productName` |  `string` The name of the product.  
`productVersion` |  `string` The version of the product.  
`productEventType` |  `string` A short, descriptive, human-readable, product-specific event name or type (e.g. "Scanned X", "User account created", "process_start").  
`productDeploymentId` |  `string` The deployment identifier assigned by the vendor for a product deployment.  
`description` |  `string` A human-readable unparsable description of the event.  
`urlBackToProduct` |  `string` A URL that takes the user to the source product console for this event.  
`ingestionLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` User-configured ingestion metadata labels.  
`tags` |  `object (`[Tags](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Tags)`)` Tags added by Google SecOps after an event is parsed. It is an error to populate this field from within a parser.  
`enrichmentState` |  `enum (`[EnrichmentState](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EnrichmentState)`)` The enrichment state.  
`logType` |  `string` The string value of log type.  
`baseLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessLabels)`)` Data access labels on the base event.  
`enrichmentLabels` |  `object (`[DataAccessLabels](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessLabels)`)` Data access labels from all the contextual events used to enrich the base event.  
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
          object ([DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessIngestionLabel))
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
`ingestionKvLabels[]` |  `object (`[DataAccessIngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DataAccessIngestionLabel)`)` All the ingestion labels (key/value pairs).  
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
        object ([Authentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Authentication))
      },
      "vulns": {
        object ([Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerabilities))
      },
      "entityRisk": {
        object ([EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EntityRisk))
      },
      "linuxUtmp": {
        object ([LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.LinuxUtmp))
      },
      "windowsEventLog": {
        object ([WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WindowsEventLog))
      },
      "resourceUsage": {
        object ([ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceUsage))
      },
      "systemEventDetails": {
        object ([SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SystemEventDetails))
      },
      "outlookMetadata": {
        object ([OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OutlookMetadata))
      },
      "srum": {
        object ([Srum](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Srum))
      },
      "userAssist": {
        object ([UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UserAssist))
      }
    }  
  
Fields  
---  
`auth` |  `object (`[Authentication](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Authentication)`)` An authentication extension.  
`vulns` |  `object (`[Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerabilities)`)` A vulnerability extension.  
`entityRisk` |  `object (`[EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EntityRisk)`)` An entity risk change extension.  
`linuxUtmp` |  `object (`[LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.LinuxUtmp)`)` A Linux Utmp extension. This captures details specific to Linux Utmp events, which record login and logout sessions on a Linux system.  
`windowsEventLog` |  `object (`[WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.WindowsEventLog)`)` A Windows Event Log extension. This captures details specific to Windows Event Log events, providing structured information from various Windows logs.  
`resourceUsage` |  `object (`[ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.ResourceUsage)`)` A resource usage extension. This captures details about what entity, for example, a process or user, is using a specific resource.  
`systemEventDetails` |  `object (`[SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SystemEventDetails)`)` A system event details extension. This captures additional details for system-level events, such as message type, sender image ID, and subsystem.  
`outlookMetadata` |  `object (`[OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.OutlookMetadata)`)` A Microsoft Outlook metadata extension. This includes metadata related to Outlook items, such as comments, templates, and security flags.  
`srum` |  `object (`[Srum](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Srum)`)` A SRUM extension. This captures details specific to Windows System Resource Usage Monitor (SRUM) events, providing insights into application resource consumption.  
`userAssist` |  `object (`[UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.UserAssist)`)` A UserAssist extension. This captures details specific to Windows User Assist events, which track application usage and execution.  
  
### Authentication

JSON representation  
---  
      
    
    {
      "type": enum ([AuthType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthType)),
      "mechanism": [
        enum ([Mechanism](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Mechanism))
      ],
      "authDetails": string,
      "outcome": enum ([Outcome](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Outcome))
    }  
  
Fields  
---  
`type` |  `enum (`[AuthType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.AuthType)`)` The type of authentication.  
`mechanism[]` |  `enum (`[Mechanism](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Mechanism)`)` The authentication mechanism.  
`authDetails` |  `string` The vendor defined details of the authentication.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Outcome)`)` The outcome of the authentication event.  
  
### Vulnerabilities

JSON representation  
---  
      
    
    {
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerability))
        }
      ]
    }  
  
Fields  
---  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Vulnerability)`)` A list of vulnerabilities.  
  
### EntityRisk

JSON representation  
---  
      
    
    {
      "riskVersion": string,
      "riskWindow": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval))
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
        object ([RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RiskDelta))
      }
      // End of list of possible types for union field _risk_delta.
    
      // Union field _raw_risk_delta can be only one of the following:
      "rawRiskDelta": {
        object ([RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RiskDelta))
      }
      // End of list of possible types for union field _raw_risk_delta.
    }  
  
Fields  
---  
`riskVersion` |  `string` Version of the risk score calculation algorithm.  
`riskWindow` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval)`)` Time window used when computing the risk score for an entity, for example 24 hours or 7 days.  
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
`riskDelta` |  `object (`[RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RiskDelta)`)` Represents the change in risk score for an entity between the end of the previous time window and the end of the current time window.  
Union field `_raw_risk_delta`.`_raw_risk_delta` can be only one of the following:  
`rawRiskDelta` |  `object (`[RiskDelta](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RiskDelta)`)` Represents the change in raw risk score for an entity between the end of the previous time window and the end of the current time window.  
  
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
      "recordType": enum ([RecordType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RecordType))
    }  
  
Fields  
---  
`recordType` |  `enum (`[RecordType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.RecordType)`)` The activity record type.  
  
### WindowsEventLog

JSON representation  
---  
      
    
    {
      "channel": enum ([Channel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Channel)),
      "eventId": string,
      "activityId": string
    }  
  
Fields  
---  
`channel` |  `enum (`[Channel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Channel)`)` The channel of the event.  
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
  
### GroupedFields

JSON representation  
---  
      
    
    {
      "ip": [
        string
      ],
      "domain": [
        string
      ],
      "hostname": [
        string
      ],
      "user": [
        string
      ],
      "email": [
        string
      ],
      "filePath": [
        string
      ],
      "hash": [
        string
      ],
      "processId": [
        string
      ]
    }  
  
Fields  
---  
`ip[]` |  `string` IP addresses.  
`domain[]` |  `string` Domains.  
`hostname[]` |  `string` Hostnames.  
`user[]` |  `string` Users.  
`email[]` |  `string` Emails.  
`filePath[]` |  `string` File paths.  
`hash[]` |  `string` File Hashes.  
`processId[]` |  `string` Process Identifiers.  
  
### Entity

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([EntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityMetadata))
      },
      "entity": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "relations": [
        {
          object ([Relation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Relation))
        }
      ],
      "additional": {
        object
      },
      "metric": {
        object ([Metric](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Metric))
      },
    
      // Union field _risk_score can be only one of the following:
      "riskScore": {
        object ([EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EntityRisk))
      }
      // End of list of possible types for union field _risk_score.
    }  
  
Fields  
---  
`metadata` |  `object (`[EntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityMetadata)`)` Entity metadata such as timestamp, product, etc.  
`entity` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Noun in the UDM event that this entity represents.  
`relations[]` |  `object (`[Relation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Relation)`)` One or more relationships between the entity (a) and other entities, including the relationship type and related entity.  
`additional` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Important entity data that cannot be adequately represented within the formal sections of the Entity.  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Metric)`)` Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC.  
Union field `_risk_score`.`_risk_score` can be only one of the following:  
`riskScore` |  `object (`[EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.EntityRisk)`)` Stores information related to the entity's risk score.  
  
### EntityMetadata

JSON representation  
---  
      
    
    {
      "productEntityId": string,
      "collectedTimestamp": string,
      "creationTimestamp": string,
      "interval": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval))
      },
      "vendorName": string,
      "productName": string,
      "feed": string,
      "productVersion": string,
      "entityType": enum ([EntityType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityType)),
      "description": string,
      "threat": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult))
        }
      ],
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.SourceType)),
      "sourceLabels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label))
        }
      ],
      "eventMetadata": {
        object ([Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Metadata))
      },
      "structuredFields": {
        object
      },
      "extracted": {
        object
      },
      "atiPrioritization": {
        object ([AtiPrioritization](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.AtiPrioritization))
      }
    }  
  
Fields  
---  
`productEntityId` |  `string` A vendor-specific identifier that uniquely identifies the entity (e.g. a GUID, LDAP, OID, or similar).  
`collectedTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` GMT timestamp when the entity information was collected by the vendor's local collection infrastructure.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creationTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` GMT timestamp when the entity described by the product_entity_id was created on the system where data was collected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval)`)` Valid existence time range for the version of the entity represented by this entity data.  
`vendorName` |  `string` Vendor name of the product that produced the entity information.  
`productName` |  `string` Product name that produced the entity information.  
`feed` |  `string` Vendor feed name for a threat indicator feed.  
`productVersion` |  `string` Version of the product that produced the entity information.  
`entityType` |  `enum (`[EntityType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityType)`)` Entity type. If an entity has multiple possible types, this specifies the most specific type.  
`description` |  `string` Human-readable description of the entity.  
`threat[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.SecurityResult)`)` Metadata provided by a threat intelligence feed that identified the entity as malicious.  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.SourceType)`)` The source of the entity.  
`sourceLabels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Label)`)` Entity source metadata labels.  
`eventMetadata` |  `object (`[Metadata](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Metadata)`)` Metadata field from the event.  
`structuredFields  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Structured fields extracted from the log.  
`extracted` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Flattened fields extracted from the log.  
`atiPrioritization` |  `object (`[AtiPrioritization](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.AtiPrioritization)`)` Prioritization factors used by ATI curated rules.  
  
### AtiPrioritization

JSON representation  
---  
      
    
    {
      "gtiVerdict": integer,
      "gtiSeverity": integer,
      "gtiThreatScore": integer,
      "mandiantAnalystConfidence": integer,
      "gtiUpdateTime": string,
      "activeIr": boolean,
      "activeIrFirstTaggedTime": string,
      "globalCustomerCount": string,
      "globalHitCount": string,
      "exclusive": boolean,
      "osint": boolean,
      "scanner": boolean,
      "reviewed": boolean,
      "attributedMalware": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association))
        }
      ],
      "attributedThreatActors": [
        {
          object ([Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association))
        }
      ]
    }  
  
Fields  
---  
`gtiVerdict` |  `integer` The confidence score from the GTI verdict source.  
`gtiSeverity` |  `integer` The confidence score from the GTI severity source.  
`gtiThreatScore` |  `integer` The confidence score from the GTI threat score source.  
`mandiantAnalystConfidence` |  `integer` The confidence score from "Mandiant Analyst Intel" source.  
`gtiUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the latest update for GTI verdict, severity, or threat score.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`activeIr` |  `boolean` Whether one or more Mandiant incident response customers had this indicator in their environment.  
`activeIrFirstTaggedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp of the first time an active IR was applied to this entity.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`globalCustomerCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Global customer count over the last 30 days  
`globalHitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Global hit count over the last 30 days  
`exclusive` |  `boolean` Whether the indicator is being used by a maximum of one threat actor.  
`osint` |  `boolean` Whether the indicator details are available in open source.  
`scanner` |  `boolean` Whether the indicator is a scanner.  
`reviewed` |  `boolean` Whether the indicator verdict has passed review.  
`attributedMalware[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association)`)` Malware families associated with this indicator.  
`attributedThreatActors[]` |  `object (`[Association](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Association)`)` Threat actors associated with this indicator.  
  
### Relation

JSON representation  
---  
      
    
    {
      "entity": {
        object ([Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun))
      },
      "entityType": enum ([EntityType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityType)),
      "relationship": enum ([Relationship](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Relationship)),
      "direction": enum ([Directionality](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Directionality)),
      "uid": string,
      "entityLabel": enum ([EntityLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityLabel))
    }  
  
Fields  
---  
`entity` |  `object (`[Noun](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Noun)`)` Entity (b) that the primary entity (a) is related to.  
`entityType` |  `enum (`[EntityType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityType)`)` Type of the related entity (b) in this relationship.  
`relationship` |  `enum (`[Relationship](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Relationship)`)` Type of relationship.  
`direction` |  `enum (`[Directionality](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Directionality)`)` Directionality of relationship between primary entity (a) and the related entity (b).  
`uid` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` UID of the relationship.A base64-encoded string.  
`entityLabel` |  `enum (`[EntityLabel](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.EntityLabel)`)` Label to identify the Noun of the relation.  
  
### Metric

JSON representation  
---  
      
    
    {
      "firstSeen": string,
      "lastSeen": string,
      "sumMeasure": {
        object ([Measure](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Measure))
      },
      "totalEvents": string,
      "metricName": enum ([MetricName](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricName)),
      "dimensions": [
        enum ([Dimension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Dimension))
      ],
      "exportWindow": string,
      "displayName": string,
      "outcomeVariables": [
        {
          object ([MetricVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricVariable))
        }
      ],
      "matchVariables": [
        {
          object ([MetricVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricVariable))
        }
      ],
      "timeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval))
      }
    }  
  
Fields  
---  
`firstSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the first time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the last time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sumMeasure` |  `object (`[Measure](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Measure)`)` Sum of all precomputed measures for the given metric.  
`totalEvents` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of events used to calculate the given precomputed metric.  
`metricName` |  `enum (`[MetricName](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricName)`)` Name of the analytic.  
`dimensions[]` |  `enum (`[Dimension](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.Dimension)`)` All group by clauses used to calculate the metric.  
`exportWindow` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Export window for which the metric was exported.  
`displayName` |  `string` Display name of the custom metric. Google-authored metrics do not have a display name.  
`outcomeVariables[]` |  `object (`[MetricVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricVariable)`)` List of outcome variables used in the custom metric.  
`matchVariables[]` |  `object (`[MetricVariable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.MetricVariable)`)` List of match variables used in the custom metric.  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Interval)`)` Time range for which the custom metric was calculated.  
  
### Measure

JSON representation  
---  
      
    
    {
      "value": number,
      "aggregateFunction": enum ([AggregateFunction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.AggregateFunction))
    }  
  
Fields  
---  
`value` |  `number` Value of the aggregated measure.  
`aggregateFunction` |  `enum (`[AggregateFunction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/summarize_entity#Output.Schema.AggregateFunction)`)` Function used to calculate the aggregated measure.  
  
### MetricVariable

JSON representation  
---  
      
    
    {
      "name": string,
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
        object ([BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BoolSequence))
      },
      "bytesSeq": {
        object ([BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BytesSequence))
      },
      "doubleSeq": {
        object ([DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DoubleSequence))
      },
      "int64Seq": {
        object ([Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Int64Sequence))
      },
      "uint64Seq": {
        object ([Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Uint64Sequence))
      },
      "stringSeq": {
        object ([StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringSequence))
      }
      // End of list of possible types for union field typed_value.
    }  
  
Fields  
---  
`name` |  `string` The name of the variable.  
`sourcePath` |  `string` The UDM field path for the field which this value was derived from. Example: `principal.hostname`  
Union field `typed_value`. The typed value of the variable. `typed_value` can be only one of the following:  
`boolVal` |  `boolean` *  
`bytesVal` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` *A base64-encoded string.  
`doubleVal` |  `number` *  
`int64Val` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` *  
`uint64Val` |  `string` The value in uint64 format.  
`stringVal` |  `string` Enum values are returned as strings.  
`timestampTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` *Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nullVal` |  `boolean` *  
`boolSeq` |  `object (`[BoolSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BoolSequence)`)` *  
`bytesSeq` |  `object (`[BytesSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.BytesSequence)`)` *  
`doubleSeq` |  `object (`[DoubleSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.DoubleSequence)`)` *  
`int64Seq` |  `object (`[Int64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Int64Sequence)`)` *  
`uint64Seq` |  `object (`[Uint64Sequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Uint64Sequence)`)` *  
`stringSeq` |  `object (`[StringSequence](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.StringSequence)`)` *  
  
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
      "enrichmentType": enum ([EnrichmentType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.EnrichmentType)),
      "overriddenEntity": {
        object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Entity))
      }
    }  
  
Fields  
---  
`dataTable` |  `string` The name of the data table.  
`enrichmentType` |  `enum (`[EnrichmentType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.EnrichmentType)`)` The type of enrichment.  
`overriddenEntity` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.Entity)`)` The entity which has only the overridden fields populated. Only populated if the enrichment type is OVERRIDE.  
  
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
      "responsePlatformType": enum ([ResponsePlatformType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.ResponsePlatformType))
    }  
  
Fields  
---  
`alertId` |  `string` Id of the alert in SOAR product.  
`responsePlatformType` |  `enum (`[ResponsePlatformType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.ResponsePlatformType)`)` Type of SOAR product.  
  
### Feedback

JSON representation  
---  
      
    
    {
      "idpUserId": string,
      "createdTime": string,
    
      // Union field _verdict can be only one of the following:
      "verdict": enum ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict_1))
      // End of list of possible types for union field _verdict.
    
      // Union field _reputation can be only one of the following:
      "reputation": enum ([Reputation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reputation))
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
      "status": enum ([Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Status))
      // End of list of possible types for union field _status.
    
      // Union field _priority can be only one of the following:
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority))
      // End of list of possible types for union field _priority.
    
      // Union field _root_cause can be only one of the following:
      "rootCause": string
      // End of list of possible types for union field _root_cause.
    
      // Union field _reason can be only one of the following:
      "reason": enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason_1))
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
      "userType": enum ([UserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.UserType))
      // End of list of possible types for union field _user_type.
    }  
  
Fields  
---  
`idpUserId` |  `string` Required.  
`createdTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `_verdict`.`_verdict` can be only one of the following:  
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Verdict_1)`)`  
Union field `_reputation`.`_reputation` can be only one of the following:  
`reputation` |  `enum (`[Reputation](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reputation)`)`  
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
`status` |  `enum (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Status)`)` Optional.  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority)`)` Optional.  
Union field `_root_cause`.`_root_cause` can be only one of the following:  
`rootCause` |  `string` Optional.  
Union field `_reason`.`_reason` can be only one of the following:  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/generate_synthetic_events#Output.Schema.Reason_1)`)` Optional.  
Union field `_severity_display`.`_severity_display` can be only one of the following:  
`severityDisplay` |  `string` Optional.  
Union field `_priority_display`.`_priority_display` can be only one of the following:  
`priorityDisplay` |  `string` Optional.  
Union field `_triage_agent_investigation_id`.`_triage_agent_investigation_id` can be only one of the following:  
`triageAgentInvestigationId` |  `string` Optional.  
Union field `_user_type`.`_user_type` can be only one of the following:  
`userType` |  `enum (`[UserType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_security_alerts#Output.Schema.UserType)`)`  
  
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
  
### CollectionType

The type of the collection which will indicate which other fields are relevant. For example, detection finding collections will populate the detection field. Findings that evolve into investigations will populate the investigation field.

Enums  
---  
`COLLECTION_TYPE_UNSPECIFIED` | An unspecified collection type.  
`TELEMETRY_ALERT` | An alert reported in customer telemetry.  
`GCTI_FINDING` | A finding from the Uppercase team.  
`UPPERCASE_ALERT` |   
`RULE_DETECTION` | A detection found by applying a rule.  
`MACHINE_INTELLIGENCE_ALERT` | An alert generated by Chronicle machine learning models.  
`SOAR_ALERT` | An alert coming from other SIEMs via Chronicle SOAR.  
  
### Namespace

Extracted Namespace Component

Enums  
---  
`NORMALIZED_TELEMETRY` | Ingested and Normalized telemetry events  
`RAW_TELEMETRY` | Ingested Raw telemetry  
`RULE_DETECTIONS` | Chronicle Rules engine  
`UPPERCASE` | Uppercase  
`MACHINE_INTELLIGENCE` | DSML - Machine Intelligence  
`SECURITY_COMMAND_CENTER` | A normalized telemetry event from Google Security Command Center.  
`UNSPECIFIED` | Unspecified Namespace  
`SOAR_ALERT` | An alert coming from other SIEMs via Chronicle SOAR.  
`VIRUS_TOTAL` | VirusTotal.  
  
### CloudEnvironment

The service provider environment.

Enums  
---  
`UNSPECIFIED_CLOUD_ENVIRONMENT` | Default.  
`GOOGLE_CLOUD_PLATFORM` | Google Cloud Platform.  
`AMAZON_WEB_SERVICES` | Amazon Web Services.  
`MICROSOFT_AZURE` | Microsoft Azure.  
  
### ResourceType

The type of resource.

Enums  
---  
`UNSPECIFIED` | Default type.  
`MUTEX` | Mutex.  
`TASK` | Task.  
`PIPE` | Named pipe.  
`DEVICE` | Device.  
`FIREWALL_RULE` | Firewall rule.  
`MAILBOX_FOLDER` | Mailbox folder.  
`VPC_NETWORK` | VPC Network.  
`VIRTUAL_MACHINE` | Virtual machine.  
`STORAGE_BUCKET` | Storage bucket.  
`STORAGE_OBJECT` | Storage object.  
`DATABASE` | Database.  
`TABLE` | Data table.  
`CLOUD_PROJECT` | Cloud project.  
`CLOUD_ORGANIZATION` | Cloud organization.  
`SERVICE_ACCOUNT` | Service account.  
`ACCESS_POLICY` | Access policy.  
`CLUSTER` | Cluster.  
`SETTING` | Settings.  
`DATASET` | Dataset.  
`BACKEND_SERVICE` | Endpoint that receive traffic from a load balancer or proxy.  
`POD` | Pod, which is a collection of containers. Often used in Kubernetes.  
`CONTAINER` | Container.  
`FUNCTION` | Cloud function.  
`RUNTIME` | Runtime.  
`IP_ADDRESS` | IP address.  
`DISK` | Disk.  
`VOLUME` | Volume.  
`IMAGE` | Machine image.  
`SNAPSHOT` | Snapshot.  
`REPOSITORY` | Repository.  
`CREDENTIAL` | Credential, e.g. access keys, ssh keys, tokens, certificates.  
`LOAD_BALANCER` | Load balancer.  
`GATEWAY` | Gateway.  
`SUBNET` | Subnet.  
`USER` | User.  
`SERVICE` | Service.  
  
### TaskState

Enum representing the operation state of the task.

Enums  
---  
`TASK_STATE_UNSPECIFIED` | The state of the task is unknown or not specified.  
`DISABLED` | The task is registered but is disabled and no instances of the task are queued or running. The task cannot be run until it is enabled.  
`QUEUED` | Instances of the task are queued.  
`ACTIVE` | The task is ready to be executed, but no instances are queued or running.  
`RUNNING` | One or more instances of the task are running.  
  
### TaskLogonType

Enum representing the logon type of the task.

Enums  
---  
`TASK_LOGON_TYPE_UNSPECIFIED` | The logon method is not specified. Used for non-NT credentials.  
`PASSWORD` | Use a password for logging on the user. The password must be supplied at registration time.  
`S4U` | Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.  
`INTERACTIVE_TOKEN` | User must already be logged on. The task will be run only in an existing interactive session.  
`GROUP` | Logon with group credentials.  
`SERVICE_ACCOUNT` | Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.  
`INTERACTIVE_TOKEN_OR_PASSWORD` | First use the interactive token. If the user is not logged on (no interactive token is available), the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK_LOGON_PASSWORD.  
  
### ActionType

Enum representing the action type of the task.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | The action type is not specified.  
`EXEC` | This action performs a command-line operation. For example, the action can run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.  
`COM_HANDLER` | This action fires a handler. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.  
`SEND_EMAIL` | This action sends an email message. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.  
`SHOW_MESSAGE` | This action shows a message box. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.  
  
### TriggerType

Enum representing the trigger type of the task. For more details, see <https://learn.microsoft.com/en-us/windows/win32/api/taskschd/ne-taskschd-task_trigger_type2>.

Enums  
---  
`TRIGGER_TYPE_UNSPECIFIED` | The trigger frequency is not specified.  
`EVENT` | Triggers the task when a specific event occurs.  
`TIME` | Triggers the task at a specific time of day.  
`DAILY` | Triggers the task on a daily schedule. For example, the task starts at a specific time every day, every other day, or every third day.  
`WEEKLY` | Triggers the task on a weekly schedule. For example, the task starts at 8:00 AM on a specific day every week or other week.  
`MONTHLY` | Triggers the task on a monthly schedule. For example, the task starts on specific days of specific months.  
`MONTHLYDOW` | Triggers the task on a monthly day-of-week schedule. For example, the task starts on a specific days of the week, weeks of the month, and months of the year.  
`IDLE` | Triggers the task when the computer goes into an idle state.  
`REGISTRATION` | Triggers the task when the task is registered.  
`BOOT` | Triggers the task when the computer boots.  
`LOGON` | Triggers the task when a specific user logs on.  
`SESSION_STATE_CHANGE` | Triggers the task when a specific user session state changes.  
`CUSTOM_TRIGGER01` | Custom trigger 01.  
  
### ServiceType

The type of service.

Enums  
---  
`SERVICE_TYPE_UNSPECIFIED` | Default service type.  
`KERNEL_DRIVER` | A kernel driver.  
`FILE_SYSTEM_DRIVER` | A file system driver.  
`WIN32_OWN_PROCESS` | A process that is owned by the service. This is a Windows-specific service type.  
`WIN32_SHARE_PROCESS` | A process that is shared by the service. This is a Windows-specific service type.  
`ADAPTER` | An adapter. This is a Windows-specific service type.  
`RECOGNIZER_DRIVER` | A recognizer driver. This is a Windows-specific service type.  
`INTERACTIVE_PROCESS` | An interactive process. This is a Windows-specific service type.  
  
### StartupType

How the service is started.

Enums  
---  
`STARTUP_TYPE_UNSPECIFIED` | Default startup type.  
`AUTOMATIC` | The service is started automatically.  
`MANUAL` | The service is started manually by a user.  
`DISABLED` | The service is disabled and will not start automatically.  
  
### State

The current status of the service.

Enums  
---  
`STATE_UNSPECIFIED` | Default service status.  
`RUNNING` | The service is running.  
`STOPPED` | The service is stopped. This is a Windows-specific service status.  
`PAUSED` | The service is paused. This is a Windows-specific service status.  
`COMPLETED` | The service is completed.  
`START_PENDING` | The service is starting.  
`STOP_PENDING` | The service is stopping.  
`PAUSE_PENDING` | The service is pausing.  
`CONTINUE_PENDING` | The service is continuing.  
  
### PermissionType

High level categorizations of permission type.

Enums  
---  
`UNKNOWN_PERMISSION_TYPE` | Default permission type.  
`ADMIN_WRITE` | Administrator write permission.  
`ADMIN_READ` | Administrator read permission.  
`DATA_WRITE` | Data resource access write permission.  
`DATA_READ` | Data resource access read permission.  
  
### Type

Well-known system roles.

Enums  
---  
`TYPE_UNSPECIFIED` | Default user role.  
`ADMINISTRATOR` | Product administrator with elevated privileges.  
`SERVICE_ACCOUNT` | System service account for automated privilege access.  
  
### AccountType

User Account Type.

Enums  
---  
`ACCOUNT_TYPE_UNSPECIFIED` | Default user account type.  
`DOMAIN_ACCOUNT_TYPE` | A human account part of some domain in directory services.  
`LOCAL_ACCOUNT_TYPE` | A local machine account.  
`CLOUD_ACCOUNT_TYPE` | A SaaS service account type (such as Slack or GitHub).  
`SERVICE_ACCOUNT_TYPE` | A non-human account for data access.  
`DEFAULT_ACCOUNT_TYPE` | A system built in default account.  
  
### AuthenticationStatus

Authentication status, can be used to describe the status of authentication for a user or particular credential.

Enums  
---  
`UNKNOWN_AUTHENTICATION_STATUS` | The default authentication status.  
`ACTIVE` | The authentication method is in active state.  
`SUSPENDED` | The authentication method is in suspended/disabled state.  
`NO_ACTIVE_CREDENTIALS` | The authentication method has no active credentials.  
`DELETED` | The authentication method has been deleted.  
  
### Role

User system roles.

Enums  
---  
`UNKNOWN_ROLE` | Default user role.  
`ADMINISTRATOR` | Product administrator with elevated privileges.  
`SERVICE_ACCOUNT` | System service account for automated privilege access. Deprecated: not a role, instead set User.account_type.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Direction

A network traffic direction.

Enums  
---  
`UNKNOWN_DIRECTION` | The default direction.  
`INBOUND` | An inbound request.  
`OUTBOUND` | An outbound request.  
`BROADCAST` | A broadcast.  
  
### IpProtocol

An IP protocol.

Enums  
---  
`UNKNOWN_IP_PROTOCOL` | The default protocol.  
`EIGRP` | Enhanced Interior Gateway Routing  
`ESP` | Encapsulating Security Payload  
`ETHERIP` | Ethernet-within-IP Encapsulation  
`GRE` | Generic Routing Encapsulation  
`ICMP` | ICMP.  
`ICMP6` | ICMPv6  
`IGMP` | IGMP  
`IP6IN4` | IPv6 Encapsulation  
`PIM` | Protocol Independent Multicast  
`SCTP` | Stream Control Transmission Protocol  
`TCP` | TCP.  
`UDP` | UDP.  
`VRRP` | Virtual Router Redundancy Protocol  
  
### ApplicationProtocol

A network application protocol.

Enums  
---  
`UNKNOWN_APPLICATION_PROTOCOL` | The default application protocol.  
`AFP` | Apple Filing Protocol.  
`AMQP` | Advanced Message Queuing Protocol.  
`APPC` | Advanced Program-to-Program Communication.  
`ATOM` | Publishing Protocol.  
`BEEP` | Block Extensible Exchange Protocol.  
`BITCOIN` | Crypto currency protocol.  
`BIT_TORRENT` | Peer-to-peer file sharing.  
`CFDP` | Coherent File Distribution Protocol.  
`CIP` | Common Industrial Protocol.  
`COAP` | Constrained Application Protocol.  
`COTP` | Connection Oriented Transport Protocol.  
`DCERPC` | DCE/RPC.  
`DDS` | Data Distribution Service.  
`DEVICE_NET` | Automation industry protocol.  
`DHCP` | DHCP.  
`DICOM` | Digital Imaging and Communications in Medicine Protocol.  
`DNP3` | Distributed Network Protocol 3 (DNP3)  
`DNS` | DNS.  
`ENRP` | Endpoint Handlespace Redundancy Protocol.  
`E_DONKEY` | Classic file sharing protocol.  
`FAST_TRACK` | Filesharing peer-to-peer protocol.  
`FINGER` | User Information Protocol.  
`FREENET` | Censorship resistant peer-to-peer network.  
`FTAM` | File Transfer Access and Management.  
`FTP` | File Transfer Protocol.  
`GOOSE` | GOOSE Protocol.  
`GOPHER` | Gopher protocol.  
`GRPC` | gRPC Remote Procedure Call.  
`H323` | Packet-based multimedia communications system.  
`HL7` | Health Level Seven.  
`HTTP` | HTTP.  
`HTTPS` | HTTPS.  
`IEC104` | IEC 60870-5-104 (IEC 104) Protocol.  
`IMAP` | Internet Message Access Protocol.  
`IRCP` | Internet Relay Chat Protocol.  
`KADEMLIA` | Peer-to-peer hashtables.  
`KRB5` | Kerberos 5.  
`LDAP` | Lightweight Directory Access Protocol.  
`LPD` | Line Printer Daemon Protocol.  
`MIME` | Multipurpose Internet Mail Extensions and Secure MIME.  
`MMS` | Multimedia Messaging Service.  
`MODBUS` | Serial communications protocol.  
`MQTT` | Message Queuing Telemetry Transport.  
`NETCONF` | Network Configuration.  
`NFS` | Network File System.  
`NIS` | Network Information Service.  
`NNTP` | Network News Transfer Protocol.  
`NTCIP` | National Transportation Communications for Intelligent Transportation System.  
`NTP` | Network Time Protocol.  
`OSCAR` | AOL Instant Messenger Protocol.  
`PNRP` | Peer Name Resolution Protocol.  
`POP3` | Post Office Protocol version 3.  
`PTP` | Precision Time Protocol.  
`QUIC` | QUIC.  
`RDP` | Remote Desktop Protocol.  
`RELP` | Reliable Event Logging Protocol.  
`RIP` | Routing Information Protocol.  
`RLOGIN` | Remote Login in UNIX Systems.  
`RPC` | Remote Procedure Call.  
`RTMP` | Real Time Messaging Protocol.  
`RTP` | Real-time Transport Protocol.  
`RTPS` | Real Time Publish Subscribe.  
`RTSP` | Real Time Streaming Protocol.  
`SAP` | Session Announcement Protocol.  
`SDP` | Session Description Protocol.  
`SFTP` | Secure File Transfer Protocol.  
`SIP` | Session Initiation Protocol.  
`SLP` | Service Location Protocol.  
`SMB` | Server Message Block.  
`SMTP` | Simple Mail Transfer Protocol.  
`SNMP` | Simple Network Management Protocol.  
`SNTP` | Simple Network Time Protocol.  
`SSH` | Secure Shell.  
`SSMS` | Secure SMS Messaging Protocol.  
`STYX` | Styx/9P - Plan 9 from Bell Labs distributed file system protocol.  
`SV` | Sampled Values Protocol.  
`TCAP` | Transaction Capabilities Application Part.  
`TDS` | Tabular Data Stream.  
`TELNET` | Virtual Terminal Protocol.  
`TOR` | Anonymity network.  
`TSP` | Time Stamp Protocol.  
`VTP` | Virtual Terminal Protocol.  
`WEB_DAV` | Web Distributed Authoring and Versioning.  
`WHOIS` | Remote Directory Access Protocol.  
`X400` | Message Handling Service Protocol.  
`X500` | Directory Access Protocol (DAP).  
`XMPP` | Extensible Messaging and Presence Protocol.  
  
### OpCode

BOOTP op code. See RFC951, section 3.

Enums  
---  
`UNKNOWN_OPCODE` | Default opcode.  
`BOOTREQUEST` | Request.  
`BOOTREPLY` | Reply.  
  
### MessageType

DHCP message type. See RFC2131, section 3.1.

Enums  
---  
`UNKNOWN_MESSAGE_TYPE` | Default message type.  
`DISCOVER` | DHCPDISCOVER.  
`OFFER` | DHCPOFFER.  
`REQUEST` | DHCPREQUEST.  
`DECLINE` | DHCPDECLINE.  
`ACK` | DHCPACK.  
`NAK` | DHCPNAK.  
`RELEASE` | DHCPRELEASE.  
`INFORM` | DHCPINFORM.  
`WIN_DELETED` | Microsoft Windows DHCP "lease deleted".  
`WIN_EXPIRED` | Microsoft Windows DHCP "lease expired".  
  
### Family

LINT.IfChange

Enums  
---  
`USER_DEFINED` | Used to represent new families supported by user-defined parsers  
`MSIE` | Desktop user agent families  
`GECKO` |   
`APPLEWEBKIT` | WebKit based browsers e.g. Safari  
`OPERA` |   
`KHTML` | e.g. Konqueror  
`OTHER` | Mobile and non-browser user agent families UA's w/o enough data to fit into a family  
`APPLE` | Apple apps e.g. YouTube on iPhone  
`BLACKBERRY` |   
`DOCOMO` |   
`GOOGLE` | Google Earth, Sketchup, UpdateChecker etc...  
`OPENWAVE` | UP.Browser  
`POLARIS` |   
`OBIGO` |   
`TELECA` |   
`MICROSOFT` | Windows Media Player, RSS platform etc...  
`NOKIA` |   
`NETFRONT` |   
`SEMC` | Sony Ericsson Mobile Communications  
`SMIT` |   
`KOREAN` | SKT, LGT  
`CLIENT_HINTS` | Constructed from UA-CH instead of UserAgent string.  
  
### OSType

Enums  
---  
`OS_TYPE_UNKNOWN` |   
`OS_TYPE_ANDROID` |   
`OS_TYPE_IOS` |   
`OS_TYPE_WINDOWS` |   
`OS_TYPE_LINUX` |   
`OS_TYPE_MAC_OS` |   
`OS_TYPE_CHROME_OS` |   
`OS_TYPE_KAIOS` |   
`OS_TYPE_ROKU_OS` |   
`OS_TYPE_TIZEN` |   
`OS_TYPE_VIZIO` |   
`OS_TYPE_PLAYSTATION` |   
`OS_TYPE_APPLETV_OS` |   
`OS_TYPE_CHROMECAST` |   
`OS_TYPE_XBOX_OS` |   
`OS_TYPE_VIDAA_OS` |   
`OS_TYPE_DARWIN_OS` |   
`OS_TYPE_OPENTV_OS` |   
  
### OSVariantType

Enums  
---  
`OS_VARIANT_TYPE_UNKNOWN` |   
`OS_VARIANT_TYPE_FIRE_OS` |   
`OS_VARIANT_TYPE_IPHONE_OS` |   
`OS_VARIANT_TYPE_IPAD_OS` |   
  
### BrowserType

Enums  
---  
`BROWSER_TYPE_UNKNOWN` |   
`BROWSER_TYPE_CHROME` |   
`BROWSER_TYPE_FIREFOX` |   
`BROWSER_TYPE_SAFARI` |   
`BROWSER_TYPE_OPERA` |   
`BROWSER_TYPE_IE` |   
`BROWSER_TYPE_EDGE` |   
`BROWSER_TYPE_EDGIUM` |   
`BROWSER_TYPE_UC` |   
`BROWSER_TYPE_SAMSUNG` |   
`BROWSER_TYPE_YANDEX` |   
`BROWSER_TYPE_COCCOC` |   
`BROWSER_TYPE_NETFRONT` |   
`BROWSER_TYPE_ANDROIDWEBKIT` |   
`BROWSER_TYPE_CONJURE` |   
  
### BrowserVariantType

Enums  
---  
`BROWSER_VARIANT_TYPE_UNKNOWN` |   
`BROWSER_VARIANT_TYPE_BRAVE` | Brave browser is a fork of Chromium.  
  
### ConnectionState

The state of a network connection.

Enums  
---  
`CONNECTION_STATE_UNSPECIFIED` | The default connection state.  
`LISTENING` | The port is listening for incoming connections.  
`ESTABLISHED` | A connection has been established.  
`TIME_WAIT` | The connection is waiting for a timeout.  
`CLOSE_WAIT` | The connection is waiting for a connection termination request from the local application.  
`CLOSED` | The connection is closed.  
`SYN_SENT` | A connection request has been sent.  
`SYN_RECEIVED` | A connection request has been received.  
`FIN_WAIT1` | The connection is waiting for a connection termination request from the remote host.  
`FIN_WAIT2` | The connection is waiting for a connection termination request from the local application.  
`LAST_ACK` | The connection is waiting for an acknowledgment of the final connection termination request.  
  
### BrowserType

The name of the browser.

Enums  
---  
`BROWSER_TYPE_UNSPECIFIED` | Default value.  
`CHROME` | Chrome.  
`FIREFOX` | Firefox.  
`SAFARI` | Safari.  
`INTERNET_EXPLORER` | Internet Explorer.  
`EDGE` | Edge.  
`OPERA` | Opera.  
  
### UrlVisitType

The type of visit to a URL.

Enums  
---  
`URL_VISIT_TYPE_UNSPECIFIED` | Default value.  
`LINK` | The user clicked a link.  
`TYPED` | The user typed a URL.  
`AUTO_BOOKMARK` | The user bookmarked the URL.  
`AUTO_SUBFRAME` | Loaded in a nested subframe by the parent frame.  
`MANUAL_SUBFRAME` | Loaded in a nested subframe by the user.  
`GENERATED` | The user clicked on auto generated link in browser address bar.  
`AUTO_TOPLEVEL` | The page was loaded through command line or is the starting page.  
`FORM_SUBMIT` | The user submitted a form.  
`RELOAD` | The user reloaded the page.  
`KEYWORD` | The Url was generated by a keyword search configured by user.  
`KEYWORD_GENERATED` | Corresponds to a visit generated by a keyword search.  
`REDIRECT` | The user was redirected to the URL.  
  
### CookieSameSite

The SameSite attribute of a cookie.

Enums  
---  
`COOKIE_SAME_SITE_UNSPECIFIED` | Default value.  
`STRICT` | Corresponds to SameSite=Strict.  
`LAX` | Corresponds to SameSite=Lax.  
`NONE` | Corresponds to SameSite=None.  
  
### VisitSource

The source of the visit.

Enums  
---  
`VISIT_SOURCE_UNSPECIFIED` | Default value.  
`SYNCED` | The visit was synced from another device.  
`BROWSER` | The visit was from a browser.  
`EXTENSION` | The visit was from an extension.  
`IMPORTED` | The visit was imported from another browser application.  
  
### FileType

The file type, for example Microsoft Windows executable.

Enums  
---  
`FILE_TYPE_UNSPECIFIED` | File type is UNSPECIFIED.  
`FILE_TYPE_PE_EXE` | File type is PE_EXE.  
`FILE_TYPE_PE_DLL` | Although DLLs are actually portable executables, this value enables the file type to be identified separately. File type is PE_DLL.  
`FILE_TYPE_MSI` | File type is MSI.  
`FILE_TYPE_NE_EXE` | File type is NE_EXE.  
`FILE_TYPE_NE_DLL` | File type is NE_DLL.  
`FILE_TYPE_DOS_EXE` | File type is DOS_EXE.  
`FILE_TYPE_DOS_COM` | File type is DOS_COM.  
`FILE_TYPE_COFF` | File type is COFF.  
`FILE_TYPE_ELF` | File type is ELF.  
`FILE_TYPE_LINUX_KERNEL` | File type is LINUX_KERNEL.  
`FILE_TYPE_RPM` | File type is RPM.  
`FILE_TYPE_LINUX` | File type is LINUX.  
`FILE_TYPE_MACH_O` | File type is MACH_O.  
`FILE_TYPE_JAVA_BYTECODE` | File type is JAVA_BYTECODE.  
`FILE_TYPE_DMG` | File type is DMG.  
`FILE_TYPE_DEB` | File type is DEB.  
`FILE_TYPE_PKG` | File type is PKG.  
`FILE_TYPE_PYC` | File type is PYC.  
`FILE_TYPE_LNK` | File type is LNK.  
`FILE_TYPE_DESKTOP_ENTRY` | File type is DESKTOP_ENTRY.  
`FILE_TYPE_JPEG` | File type is JPEG.  
`FILE_TYPE_TIFF` | File type is TIFF.  
`FILE_TYPE_GIF` | File type is GIF.  
`FILE_TYPE_PNG` | File type is PNG.  
`FILE_TYPE_BMP` | File type is BMP.  
`FILE_TYPE_GIMP` | File type is GIMP.  
`FILE_TYPE_IN_DESIGN` | File type is Adobe InDesign.  
`FILE_TYPE_PSD` | File type is PSD. Adobe Photoshop.  
`FILE_TYPE_TARGA` | File type is TARGA.  
`FILE_TYPE_XWD` | File type is XWD.  
`FILE_TYPE_DIB` | File type is DIB.  
`FILE_TYPE_JNG` | File type is JNG.  
`FILE_TYPE_ICO` | File type is ICO.  
`FILE_TYPE_FPX` | File type is FPX.  
`FILE_TYPE_EPS` | File type is EPS.  
`FILE_TYPE_SVG` | File type is SVG.  
`FILE_TYPE_EMF` | File type is EMF.  
`FILE_TYPE_WEBP` | File type is WEBP.  
`FILE_TYPE_DWG` | File type is DWG.  
`FILE_TYPE_DXF` | File type is DXF.  
`FILE_TYPE_THREEDS` | File type is 3DS.  
`FILE_TYPE_OGG` | File type is OGG.  
`FILE_TYPE_FLC` | File type is FLC.  
`FILE_TYPE_FLI` | File type is FLI.  
`FILE_TYPE_MP3` | File type is MP3.  
`FILE_TYPE_FLAC` | File type is FLAC.  
`FILE_TYPE_WAV` | File type is WAV.  
`FILE_TYPE_MIDI` | File type is MIDI.  
`FILE_TYPE_AVI` | File type is AVI.  
`FILE_TYPE_MPEG` | File type is MPEG.  
`FILE_TYPE_QUICKTIME` | File type is QUICKTIME.  
`FILE_TYPE_ASF` | File type is ASF.  
`FILE_TYPE_DIVX` | File type is DIVX.  
`FILE_TYPE_FLV` | File type is FLV.  
`FILE_TYPE_WMA` | File type is WMA.  
`FILE_TYPE_WMV` | File type is WMV.  
`FILE_TYPE_RM` | File type is RM. RealMedia type.  
`FILE_TYPE_MOV` | File type is MOV.  
`FILE_TYPE_MP4` | File type is MP4.  
`FILE_TYPE_T3GP` | File type is T3GP.  
`FILE_TYPE_WEBM` | File type is WEBM.  
`FILE_TYPE_MKV` | File type is MKV.  
`FILE_TYPE_PDF` | File type is PDF.  
`FILE_TYPE_PS` | File type is PS.  
`FILE_TYPE_DOC` | File type is DOC.  
`FILE_TYPE_DOCX` | File type is DOCX.  
`FILE_TYPE_PPT` | File type is PPT.  
`FILE_TYPE_PPTX` | File type is PPTX.  
`FILE_TYPE_XLS` | File type is XLS.  
`FILE_TYPE_XLSX` | File type is XLSX.  
`FILE_TYPE_RTF` | File type is RTF.  
`FILE_TYPE_PPSX` | File type is PPSX.  
`FILE_TYPE_ODP` | File type is ODP.  
`FILE_TYPE_ODS` | File type is ODS.  
`FILE_TYPE_ODT` | File type is ODT.  
`FILE_TYPE_HWP` | File type is HWP.  
`FILE_TYPE_GUL` | File type is GUL.  
`FILE_TYPE_ODF` | File type is ODF.  
`FILE_TYPE_ODG` | File type is ODG.  
`FILE_TYPE_ONE_NOTE` | File type is ONE_NOTE.  
`FILE_TYPE_OOXML` | File type is OOXML.  
`FILE_TYPE_SLK` | File type is SLK.  
`FILE_TYPE_EBOOK` | File type is EBOOK.  
`FILE_TYPE_LATEX` | File type is LATEX.  
`FILE_TYPE_TTF` | File type is TTF.  
`FILE_TYPE_EOT` | File type is EOT.  
`FILE_TYPE_WOFF` | File type is WOFF.  
`FILE_TYPE_CHM` | File type is CHM.  
`FILE_TYPE_ZIP` | File type is ZIP.  
`FILE_TYPE_GZIP` | File type is GZIP.  
`FILE_TYPE_BZIP` | File type is BZIP.  
`FILE_TYPE_RZIP` | File type is RZIP.  
`FILE_TYPE_DZIP` | File type is DZIP.  
`FILE_TYPE_SEVENZIP` | File type is SEVENZIP.  
`FILE_TYPE_CAB` | File type is CAB.  
`FILE_TYPE_JAR` | File type is JAR.  
`FILE_TYPE_RAR` | File type is RAR.  
`FILE_TYPE_MSCOMPRESS` | File type is MSCOMPRESS.  
`FILE_TYPE_ACE` | File type is ACE.  
`FILE_TYPE_ARC` | File type is ARC.  
`FILE_TYPE_ARJ` | File type is ARJ.  
`FILE_TYPE_ASD` | File type is ASD.  
`FILE_TYPE_BLACKHOLE` | File type is BLACKHOLE.  
`FILE_TYPE_KGB` | File type is KGB.  
`FILE_TYPE_ZLIB` | File type is ZLIB.  
`FILE_TYPE_TAR` | File type is TAR.  
`FILE_TYPE_ZST` | File type is ZST.  
`FILE_TYPE_LZFSE` | File type is LZFSE.  
`FILE_TYPE_PYTHON_WHL` | File type is PYTHON_WHL.  
`FILE_TYPE_PYTHON_PKG` | File type is PYTHON_PKG.  
`FILE_TYPE_MSIX` | File type is MSIX, new Windows app package format.  
`FILE_TYPE_TEXT` | File type is TEXT.  
`FILE_TYPE_SCRIPT` | File type is SCRIPT.  
`FILE_TYPE_PHP` | File type is PHP.  
`FILE_TYPE_PYTHON` | File type is PYTHON.  
`FILE_TYPE_PERL` | File type is PERL.  
`FILE_TYPE_RUBY` | File type is RUBY.  
`FILE_TYPE_C` | File type is C.  
`FILE_TYPE_CPP` | File type is CPP.  
`FILE_TYPE_JAVA` | File type is JAVA.  
`FILE_TYPE_SHELLSCRIPT` | File type is SHELLSCRIPT.  
`FILE_TYPE_PASCAL` | File type is PASCAL.  
`FILE_TYPE_AWK` | File type is AWK.  
`FILE_TYPE_DYALOG` | File type is DYALOG.  
`FILE_TYPE_FORTRAN` | File type is FORTRAN.  
`FILE_TYPE_JAVASCRIPT` | File type is JAVASCRIPT.  
`FILE_TYPE_POWERSHELL` | File type is POWERSHELL.  
`FILE_TYPE_VBA` | File type is VBA.  
`FILE_TYPE_M4` | File type is M4.  
`FILE_TYPE_OBJETIVEC` | File type is OBJETIVEC.  
`FILE_TYPE_JMOD` | File type is JMOD.  
`FILE_TYPE_MAKEFILE` | File type is MAKEFILE.  
`FILE_TYPE_INI` | File type is INI.  
`FILE_TYPE_CLJ` | File type is CLJ.  
`FILE_TYPE_PDB` | File type is PDB.  
`FILE_TYPE_SQL` | File type is SQL.  
`FILE_TYPE_NEKO` | File type is NEKO.  
`FILE_TYPE_WER` | File type is WER.  
`FILE_TYPE_GOLANG` | File type is GOLANG.  
`FILE_TYPE_M3U` | File type is M3U.  
`FILE_TYPE_BAT` | File type is BAT, Windows .bat/.cmd (old files are tagged as SHELLSCRIPT).  
`FILE_TYPE_MSC` | File type is MSC, Microsoft Management Console (MMC).  
`FILE_TYPE_RDP` | File type is RDP, Microsoft Remote Desktop Protocol (RDP) file.  
`FILE_TYPE_SYMBIAN` | File type is SYMBIAN.  
`FILE_TYPE_PALMOS` | File type is PALMOS.  
`FILE_TYPE_WINCE` | File type is WINCE.  
`FILE_TYPE_ANDROID` | File type is ANDROID.  
`FILE_TYPE_IPHONE` | File type is IPHONE.  
`FILE_TYPE_HTML` | File type is HTML.  
`FILE_TYPE_XML` | File type is XML.  
`FILE_TYPE_SWF` | File type is SWF.  
`FILE_TYPE_FLA` | File type is FLA.  
`FILE_TYPE_COOKIE` | File type is COOKIE.  
`FILE_TYPE_TORRENT` | File type is TORRENT.  
`FILE_TYPE_EMAIL_TYPE` | File type is EMAIL_TYPE.  
`FILE_TYPE_OUTLOOK` | File type is OUTLOOK.  
`FILE_TYPE_SGML` | File type is SGML.  
`FILE_TYPE_JSON` | File type is JSON.  
`FILE_TYPE_CSV` | File type is CSV.  
`FILE_TYPE_HTA` | File type is HTA (HTML Application).  
`FILE_TYPE_INTERNET_SHORTCUT` | File type is MSHTML .url.  
`FILE_TYPE_CAP` | File type is CAP.  
`FILE_TYPE_ISOIMAGE` | File type is ISOIMAGE.  
`FILE_TYPE_SQUASHFS` | File type is SQUASHFS.  
`FILE_TYPE_VHD` | File type is VHD.  
`FILE_TYPE_APPLE` | File type is APPLE.  
`FILE_TYPE_MACINTOSH` | File type is MACINTOSH.  
`FILE_TYPE_APPLESINGLE` | File type is APPLESINGLE.  
`FILE_TYPE_APPLEDOUBLE` | File type is APPLEDOUBLE.  
`FILE_TYPE_MACINTOSH_HFS` | File type is MACINTOSH_HFS.  
`FILE_TYPE_APPLE_PLIST` | File type is APPLE_PLIST.  
`FILE_TYPE_MACINTOSH_LIB` | File type is MACINTOSH_LIB.  
`FILE_TYPE_APPLESCRIPT` | File type is APPLESCRIPT.  
`FILE_TYPE_APPLESCRIPT_COMPILED` | File type is APPLESCRIPT_COMPILED .  
`FILE_TYPE_CRX` | File type is CRX.  
`FILE_TYPE_XPI` | File type is XPI.  
`FILE_TYPE_ROM` | File type is ROM.  
`FILE_TYPE_IPS` | File type is IPS.  
`FILE_TYPE_PEM` | File type is PEM.  
`FILE_TYPE_PGP` | File type is PGP.  
`FILE_TYPE_CRT` | File type is CRT.  
  
### Attribute

File attributes from the USN record (e.g., "READ_ONLY, HIDDEN"). See <https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants> for more information about the attributes.

Enums  
---  
`ATTRIBUTE_UNSPECIFIED` | Unspecified attribute.  
`READ_ONLY` | A file that is read-only.  
`HIDDEN` | The file or directory is hidden.  
`SYSTEM` | A file or directory that the operating system uses.  
`ARCHIVE` | Archive file or directory.  
`COMPRESSED` | A file or directory that is compressed.  
`ENCRYPTED` | A file or directory that is encrypted.  
`DIRECTORY` | The handle that identifies the directory.  
`DEVICE` | Reserved for system use.  
`NORMAL` | A file that does not have other attributes set.  
`TEMPORARY` | A file that is being used for temporary storage.  
`SPARSE_FILE` | A file that is a sparse file.  
`REPARSE_POINT` | A file or directory that has an associated reparse point.  
`OFFLINE` | The data of a file is not available immediately.  
`NOT_CONTENT_INDEXED` | The file or directory is not to be indexed.  
`NON_CONTENT_INDEXED` | Deprecated: Use NOT_CONTENT_INDEXED instead.  
`INTEGRITY_STREAM` | The directory or user data stream is configured with integrity.  
`VIRTUAL` | Reserved for system use.  
`NO_SCRUB_DATA` | The user data stream not to be read by the background data integrity scanner.  
`EA` | A file or directory with extended attributes.  
`PINNED` | The file or directory should be kept fully present locally.  
`UNPINNED` | The file or directory should not be kept fully present locally.  
`RECALL_ON_OPEN` | The file or directory has no physical representation on the local system.  
`RECALL_ON_DATA_ACCESS` | The file or directory is not fully present locally.  
  
### Reason

The reason for the USN journal entry.

Enums  
---  
`REASON_UNSPECIFIED` | Unspecified reason.  
`DATA_OVERWRITE` | Data overwrite reason.  
`DATA_EXTEND` | Data extend reason.  
`DATA_TRUNCATION` | Data truncation reason.  
`NAMED_DATA_OVERWRITE` | Named data overwrite reason.  
`NAMED_DATA_EXTEND` | Named data extend reason.  
`NAMED_DATA_TRUNCATION` | Named data truncation reason.  
`FILE_CREATE` | File create reason.  
`FILE_DELETE` | File delete reason.  
`EA_CHANGE` | EA change reason.  
`SECURITY_CHANGE` | Security change reason.  
`RENAME_OLD_NAME` | Rename old name reason.  
`RENAME_NEW_NAME` | Rename new name reason.  
`INDEXABLE_CHANGE` | Indexable change reason.  
`BASIC_INFO_CHANGE` | Basic info change reason.  
`HARD_LINK_CHANGE` | Hard link change reason.  
`COMPRESSION_CHANGE` | Compression change reason.  
`ENCRYPTION_CHANGE` | Encryption change reason.  
`OBJECT_ID_CHANGE` | Object ID change reason.  
`REPARSE_POINT_CHANGE` | Reparse point change reason.  
`STREAM_CHANGE` | Stream change reason.  
`TRANSACTED_CHANGE` | Transacted change reason.  
`CLOSE` | Close reason.  
  
### TokenElevationType

The elevation type of the process's token. See <https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_elevation_type>

Enums  
---  
`UNKNOWN` | An undetermined token type.  
`TYPE_1` | A full token with no privileges removed or groups disabled.  
`TYPE_2` | An elevated token with no privileges removed or groups disabled. Used when running as administrator.  
`TYPE_3` | A limited token with administrative privileges removed and administrative groups disabled.  
  
### State

The state of the process. See <https://psutil.readthedocs.io/en/stable/#process-status-constants>.

Enums  
---  
`STATE_UNSPECIFIED` | Undetermined state.  
`RUNNING` | Process is running or runnable.  
`SLEEPING` | Process is waiting for an event.  
`DISK_SLEEP` | Process is in uninterruptible sleep, typically I/O.  
`STOPPED` | Process is stopped.  
`TRACING_STOP` | Process is stopped by debugger.  
`ZOMBIE` | Process is terminated but not reaped by parent.  
`DEAD` | Process is terminated.  
`WAKE_KILL` | Process is woken to be killed.  
`WAKING` | Process is waking from sleep.  
`PARKED` | Linux specific: process is parked.  
`IDLE` | Linux, macOS, and FreeBSD specific: process is idle.  
`LOCKED` | FreeBSD specific: process is locked.  
`WAITING` | FreeBSD specific: process is waiting.  
`SUSPENDED` | NetBSD specific: process is suspended.  
  
### Platform

Operating system platform.

Enums  
---  
`UNKNOWN_PLATFORM` | Default value.  
`WINDOWS` | Microsoft Windows.  
`MAC` | macOS.  
`LINUX` | Linux.  
`GCP` | Deprecated: see cloud.environment.  
`AWS` | Deprecated: see cloud.environment.  
`AZURE` | Deprecated: see cloud.environment.  
`IOS` | IOS  
`ANDROID` | Android  
`CHROME_OS` | Chrome OS  
  
### AssetType

The role type of the asset.

Enums  
---  
`ROLE_UNSPECIFIED` | Unspecified asset role.  
`WORKSTATION` | A workstation or desktop.  
`LAPTOP` | A laptop computer.  
`IOT` | An IOT asset.  
`NETWORK_ATTACHED_STORAGE` | A network attached storage device.  
`PRINTER` | A printer.  
`SCANNER` | A scanner.  
`SERVER` | A server.  
`TAPE_LIBRARY` | A tape library device.  
`MOBILE` | A mobile device such as a mobile phone or PDA.  
  
### DeploymentStatus

Deployment status states.

Enums  
---  
`DEPLOYMENT_STATUS_UNSPECIFIED` | Unspecified deployment status.  
`ACTIVE` | Asset is active, functional and deployed.  
`PENDING_DECOMISSION` | Asset is pending decommission and no longer deployed.  
`DECOMISSIONED` | Asset is decommissioned.  
  
### Severity

Severity of the vulnerability.

Enums  
---  
`UNKNOWN_SEVERITY` | The default severity level.  
`LOW` | Low severity.  
`MEDIUM` | Medium severity.  
`HIGH` | High severity.  
`CRITICAL` | Critical severity.  
  
### Type

Type of the registry value. These values are based on the Windows Registry value types: <https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types>

Enums  
---  
`TYPE_UNSPECIFIED` | Default registry value type used when the type is unknown.  
`NONE` | The registry value is not set and only the key exists.  
`SZ` | A null-terminated string.  
`EXPAND_SZ` | A null-terminated string that contains unexpanded references to environment variables  
`BINARY` | Binary data in any form.  
`DWORD` | A 32-bit number.  
`DWORD_LITTLE_ENDIAN` | A 32-bit number in little-endian format.  
`DWORD_BIG_ENDIAN` | A 32-bit number in big-endian format.  
`LINK` | A null-terminated Unicode string that contains the target path of a symbolic link.  
`MULTI_SZ` | A sequence of null-terminated strings, terminated by an empty string  
`RESOURCE_LIST` | A device driver resource list.  
`QWORD` | A 64-bit number.  
`QWORD_LITTLE_ENDIAN` | A 64-bit number in little-endian format.  
  
### Verdict

Categorization options for the validity of a finding (for example, whether it reflects an actual security incident).

Enums  
---  
`VERDICT_UNSPECIFIED` | An unspecified verdict.  
`TRUE_POSITIVE` | A categorization of the finding as a "true positive".  
`FALSE_POSITIVE` | A categorization of the finding as a "false positive".  
  
### Reputation

Categorization options for the usefulness of a finding.

Enums  
---  
`REPUTATION_UNSPECIFIED` | An unspecified reputation.  
`USEFUL` | A categorization of the finding as useful.  
`NOT_USEFUL` | A categorization of the finding as not useful.  
  
### Status

Describes status of a finding.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified finding status.  
`NEW` | New finding.  
`REVIEWED` | When a finding has feedback.  
`CLOSED` | When an analyst closes an finding.  
`OPEN` | Open. Used to indicate that a Case / Alert is open.  
  
### Priority

Priority that is assigned to a Case or Alert.

Enums  
---  
`PRIORITY_UNSPECIFIED` | Default priority level.  
`PRIORITY_INFO` | Informational priority.  
`PRIORITY_LOW` | Low priority.  
`PRIORITY_MEDIUM` | Medium priority.  
`PRIORITY_HIGH` | High priority.  
`PRIORITY_CRITICAL` | Critical priority.  
  
### Reason

Reason for closing an Alert or Case in the SOAR product.

Enums  
---  
`REASON_UNSPECIFIED` | Default reason.  
`REASON_NOT_MALICIOUS` | Case or Alert not malicious.  
`REASON_MALICIOUS` | Case or Alert is malicious.  
`REASON_MAINTENANCE` | Case or Alert is under maintenance.  
  
### AiType

The type of the AI system.

Enums  
---  
`AI_TYPE_UNSPECIFIED` | Default value.  
`MODEL` | A foundational or fine-tuned language, vision, or multi-modal model. For example, the Gemini multi-modal LLM.  
`AGENT` | An autonomous agent that uses one or more models or tools to perform tasks. Example: A SOAR agent that investigates security incidents.  
`TOOL` | A specific capability or tool exposed by an AI system. Example: An MCP server or a specific function exposed by an agent.  
  
### SecurityCategory

SecurityCategory is used to standardize security categories across products so one event is not categorized as "malware" and another as a "virus".

Enums  
---  
`UNKNOWN_CATEGORY` | The default category.  
`SOFTWARE_MALICIOUS` | Malware, spyware, rootkit.  
`SOFTWARE_SUSPICIOUS` | Below the conviction threshold; probably bad.  
`SOFTWARE_PUA` | Potentially Unwanted App (such as adware).  
`NETWORK_MALICIOUS` | Includes C&C or network exploit.  
`NETWORK_SUSPICIOUS` | Suspicious activity, such as potential reverse tunnel.  
`NETWORK_CATEGORIZED_CONTENT` | Non-security related: URL has category like gambling or porn.  
`NETWORK_DENIAL_OF_SERVICE` | DoS, DDoS.  
`NETWORK_RECON` | Port scan detected by an IDS, probing of web app.  
`NETWORK_COMMAND_AND_CONTROL` | If we know this is a C&C channel.  
`ACL_VIOLATION` | Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc.  
`AUTH_VIOLATION` | Authentication failed (e.g. bad password or bad 2-factor authentication).  
`EXPLOIT` | Exploit: For all manner of exploits including attempted overflows, bad protocol encodings, ROP, SQL injection, etc. For both network and host- based exploits.  
`DATA_EXFILTRATION` | DLP: Sensitive data transmission, copy to thumb drive.  
`DATA_AT_REST` | DLP: Sensitive data found at rest in a scan.  
`DATA_DESTRUCTION` | Attempt to destroy/delete data.  
`TOR_EXIT_NODE` | TOR Exit Nodes.  
`MAIL_SPAM` | Spam email, message, etc.  
`MAIL_PHISHING` | Phishing email, chat messages, etc.  
`MAIL_SPOOFING` | Spoofed source email address, etc.  
`POLICY_VIOLATION` | Security-related policy violation (e.g. firewall/proxy/HIPS rule violated, NAC block action).  
`SOCIAL_ENGINEERING` | Threats which manipulate to break normal security procedures.  
`PHISHING` | Phishing pages, pops, https phishing etc.  
  
### AlertState

The type of alerting set up for a security result.

Enums  
---  
`UNSPECIFIED` | The security result type is not known.  
`NOT_ALERTING` | The security result is not an alert.  
`ALERTING` | The security result is an alert.  
  
### Type

Type options for Finding variables.

Enums  
---  
`TYPE_UNSPECIFIED` | An unspecified variable type.  
`MATCH` | A variable coming from the match conditions.  
`OUTCOME` | A variable representing significant data that was found in the detection logic.  
  
### Action

Enum representing different possible actions taken by the product that created the event. Google SecOps classifies: - ALLOW and ALLOW_WITH_MODIFICATION actions as "successful". - BLOCK, QUARANTINE, FAIL, and CHALLENGE actions as "failed". This includes all corresponding metrics (for example, AUTH_ATTEMPTS_FAIL, FILE_EXECUTIONS_FAIL, RESOURCE_READ_FAIL, and so on). - UNKNOWN_ACTION actions as neither "successful" nor "failed", because, for example, logs might not provide information whether a login event occurred but some kind of "unknown" error was issued nonetheless.

Enums  
---  
`UNKNOWN_ACTION` | The default action.  
`ALLOW` | Allowed.  
`BLOCK` | Blocked.  
`ALLOW_WITH_MODIFICATION` | Strip, modify something (e.g. File or email was disinfected or rewritten and still forwarded).  
`QUARANTINE` | Put somewhere for later analysis (does NOT imply block).  
`FAIL` | Failed (e.g. the event was allowed but failed).  
`CHALLENGE` | Challenged (e.g. the user was challenged by a Captcha, 2FA).  
  
### ProductSeverity

Defined by the product

Enums  
---  
`UNKNOWN_SEVERITY` | The default severity level.  
`INFORMATIONAL` | Info severity.  
`ERROR` | An error.  
`NONE` | No malicious result.  
`LOW` | Low-severity malicious result.  
`MEDIUM` | Medium-severity malicious result.  
`HIGH` | High-severity malicious result.  
`CRITICAL` | Critical-severity malicious result.  
  
### ProductConfidence

A level of confidence in the result.

Enums  
---  
`UNKNOWN_CONFIDENCE` | The default confidence level.  
`LOW_CONFIDENCE` | Low confidence.  
`MEDIUM_CONFIDENCE` | Medium confidence.  
`HIGH_CONFIDENCE` | High confidence.  
  
### ProductPriority

A product priority level.

Enums  
---  
`UNKNOWN_PRIORITY` | Default priority level.  
`LOW_PRIORITY` | Low priority.  
`MEDIUM_PRIORITY` | Medium priority.  
`HIGH_PRIORITY` | High priority.  
  
### ThreatStatus

Vendor-specific information about the status of a threat (ITW).

Enums  
---  
`THREAT_STATUS_UNSPECIFIED` | Default threat status  
`ACTIVE` | Active threat.  
`CLEARED` | Cleared threat.  
`FALSE_POSITIVE` | False positive.  
  
### AssociationType

Represents different possible Association types. Can be threat or malware. Used to represent Mandiant threat intelligence.

Enums  
---  
`ASSOCIATION_TYPE_UNSPECIFIED` | The default Association Type.  
`THREAT_ACTOR` | Association type Threat actor.  
`MALWARE` | Association type Malware.  
`SOFTWARE_TOOLKIT` | Association type Software toolkit.  
  
### VerdictResponse

Represents different verdict types. Used to represent Mandiant threat intelligence.

Enums  
---  
`VERDICT_RESPONSE_UNSPECIFIED` | The default verdict response type.  
`MALICIOUS` | VerdictResponse resulted a threat as malicious.  
`BENIGN` | VerdictResponse resulted a threat as benign.  
  
### VerdictType

Category of the verdict.

Enums  
---  
`VERDICT_TYPE_UNSPECIFIED` | Verdict category not specified.  
`PROVIDER_ML_VERDICT` | MLVerdict result provided from threat providers, like Mandiant. These fields are used to model Mandiant sources.  
`ANALYST_VERDICT` | Verdict provided by the human analyst. These fields are used to model Mandiant sources.  
  
### IoCStatsType

Type of IoCStat based on source.

Enums  
---  
`UNSPECIFIED_IOC_STATS_TYPE` | IoCStat source is unidentified.  
`MANDIANT_SOURCES` | IoCStat is from a Mandiant Source.  
`THIRD_PARTY_SOURCES` | IoCStat is from a third-party source.  
`THREAT_INTELLIGENCE_IOC_STATS` | IoCStat is from a threat intelligence feed.  
  
### ThreatVerdict

GCTI threat verdict levels.

Enums  
---  
`THREAT_VERDICT_UNSPECIFIED` | Unspecified threat verdict level.  
`UNDETECTED` | Undetected threat verdict level.  
`SUSPICIOUS` | Suspicious threat verdict level.  
`MALICIOUS` | Malicious threat verdict level.  
  
### ThreatCollectionType

Different Types of threat collections currently supported.

Enums  
---  
`THREAT_COLLECTION_TYPE_UNSPECIFIED` | Threat collection type is unspecified.  
`CAMPAIGN` | Threat collection type is campaign.  
`REPORT` | Threat collection type is report.  
`OPERATION` | Threat collection type is operation.  
  
### EventTimestampAttribute

Enum representing the type of timestamp that the event_timestamp field represents.

Enums  
---  
`EVENT_TIMESTAMP_ATTRIBUTE_UNSPECIFIED` | Default event timestamp attribute.  
`FILE_LAST_ACCESS_TIME` | Deprecated. Use LAST_ACCESSED instead.  
`FILE_LAST_MODIFIED_TIME` | Deprecated. Use LAST_MODIFIED instead.  
`FILE_METADATA_LAST_CHANGE_TIME` | Deprecated. Use METADATA_LAST_CHANGED instead.  
`FILE_CREATION_TIME` | Deprecated. Use CREATED instead.  
`COLLECTED_TIME` | Deprecated. Use COLLECTED instead.  
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
`FIRST_VISITED` | First Visited Timestamp.  
`FIRST_SEEN` | First Seen Timestamp.  
`DOWNLOADED` | Downloaded Timestamp.  
  
### EventType

An event type. Choose event type not based on the product that generated the event but the one that logged the event itself. So, for example, an antivirus (AV) scanning email on a client would generate an SMTP_PROXY event, not an AV event. A DLP device scanning a web upload would generate an HTTP_PROXY event and not a DLP or process activity event. Note: In the case of a HTTP_PROXY event, you might also include process details if this occurred on an endpoint. That would be optional, but there are a certain set of required fields and banned fields due to its status as an HTTP_PROXY event.

Enums  
---  
`EVENTTYPE_UNSPECIFIED` | Default event type  
`PROCESS_UNCATEGORIZED` | Activity related to a process which does not match any other event types.  
`PROCESS_LAUNCH` | Process launch.  
`PROCESS_INJECTION` | Process injecting into another process.  
`PROCESS_PRIVILEGE_ESCALATION` | Process privilege escalation.  
`PROCESS_TERMINATION` | Process termination.  
`PROCESS_OPEN` | Process being opened.  
`PROCESS_MODULE_LOAD` | Process loading a module.  
`REGISTRY_UNCATEGORIZED` | Registry event which does not match any of the other event types.  
`REGISTRY_CREATION` | Registry creation.  
`REGISTRY_MODIFICATION` | Registry modification.  
`REGISTRY_DELETION` | Registry deletion.  
`SETTING_UNCATEGORIZED` | Settings-related event which does not match any of the other event types.  
`SETTING_CREATION` | Setting creation.  
`SETTING_MODIFICATION` | Setting modification.  
`SETTING_DELETION` | Setting deletion.  
`MUTEX_UNCATEGORIZED` | Any mutex event other than creation.  
`MUTEX_CREATION` | Mutex creation.  
`FILE_UNCATEGORIZED` | File event which does not match any of the other event types.  
`FILE_CREATION` | File created.  
`FILE_DELETION` | File deleted.  
`FILE_MODIFICATION` | File modified.  
`FILE_READ` | File read.  
`FILE_COPY` | File copied. Used for file copies, for example, to a thumb drive.  
`FILE_OPEN` | File opened.  
`FILE_MOVE` | File moved or renamed.  
`FILE_SYNC` | File synced (for example, Google Drive, Dropbox, backup).  
`USER_UNCATEGORIZED` | User activity which does not match any of the other event types.  
`USER_LOGIN` | User login.  
`USER_LOGOUT` | User logout.  
`USER_CREATION` | User creation.  
`USER_CHANGE_PASSWORD` | User password change event.  
`USER_CHANGE_PERMISSIONS` | Change in user permissions.  
`USER_STATS` | Deprecated. Used to update user info for an LDAP dump.  
`USER_BADGE_IN` | User physically badging into a location.  
`USER_DELETION` | User deletion.  
`USER_RESOURCE_CREATION` | User creating a virtual resource. This is equivalent to RESOURCE_CREATION.  
`USER_RESOURCE_UPDATE_CONTENT` | User updating content of a virtual resource. This is equivalent to RESOURCE_WRITTEN.  
`USER_RESOURCE_UPDATE_PERMISSIONS` | User updating permissions of a virtual resource. This is equivalent to RESOURCE_PERMISSIONS_CHANGE.  
`USER_COMMUNICATION` | User initiating communication through a medium (for example, video).  
`USER_RESOURCE_ACCESS` | User accessing a virtual resource. This is equivalent to RESOURCE_READ.  
`USER_RESOURCE_DELETION` | User deleting a virtual resource. This is equivalent to RESOURCE_DELETION.  
`GROUP_UNCATEGORIZED` | A group activity that does not fall into one of the other event types.  
`GROUP_CREATION` | A group creation.  
`GROUP_DELETION` | A group deletion.  
`GROUP_MODIFICATION` | A group modification.  
`EMAIL_UNCATEGORIZED` | Email messages  
`EMAIL_TRANSACTION` | An email transaction.  
`EMAIL_URL_CLICK` | Deprecated: use NETWORK_HTTP instead. An email URL click event.  
`NETWORK_UNCATEGORIZED` | A network event that does not fit into one of the other event types.  
`NETWORK_FLOW` | Aggregated flow stats like netflow.  
`NETWORK_CONNECTION` | Network connection details like from a FW.  
`NETWORK_FTP` | FTP telemetry.  
`NETWORK_DHCP` | DHCP payload.  
`NETWORK_DNS` | DNS payload.  
`NETWORK_HTTP` | HTTP telemetry.  
`NETWORK_SMTP` | SMTP telemetry.  
`STATUS_UNCATEGORIZED` | A status message that does not fit into one of the other event types.  
`STATUS_HEARTBEAT` | Heartbeat indicating product is alive.  
`STATUS_STARTUP` | An agent startup.  
`STATUS_SHUTDOWN` | An agent shutdown.  
`STATUS_UPDATE` | A software or fingerprint update.  
`SCAN_UNCATEGORIZED` | Scan item that does not fit into one of the other event types.  
`SCAN_FILE` | A file scan.  
`SCAN_PROCESS_BEHAVIORS` | Scan process behaviors. Please use SCAN_PROCESS instead.  
`SCAN_PROCESS` | Scan process.  
`SCAN_HOST` | Scan results from scanning an entire host device for threats/sensitive documents.  
`SCAN_VULN_HOST` | Vulnerability scan logs about host vulnerabilities (e.g., out of date software) and network vulnerabilities (e.g., unprotected service detected via a network scan).  
`SCAN_VULN_NETWORK` | Vulnerability scan logs about network vulnerabilities.  
`SCAN_NETWORK` | Scan network for suspicious activity  
`SCHEDULED_TASK_UNCATEGORIZED` | Scheduled task event that does not fall into one of the other event types.  
`SCHEDULED_TASK_CREATION` | Scheduled task creation.  
`SCHEDULED_TASK_DELETION` | Scheduled task deletion.  
`SCHEDULED_TASK_ENABLE` | Scheduled task being enabled.  
`SCHEDULED_TASK_DISABLE` | Scheduled task being disabled.  
`SCHEDULED_TASK_MODIFICATION` | Scheduled task being modified.  
`SYSTEM_AUDIT_LOG_UNCATEGORIZED` | A system audit log event that is not a wipe.  
`SYSTEM_AUDIT_LOG_WIPE` | A system audit log wipe.  
`SERVICE_UNSPECIFIED` | Service event that does not fit into one of the other event types.  
`SERVICE_CREATION` | A service creation.  
`SERVICE_DELETION` | A service deletion.  
`SERVICE_START` | A service start.  
`SERVICE_STOP` | A service stop.  
`SERVICE_MODIFICATION` | A service modification.  
`GENERIC_EVENT` | Operating system events that are not described by any of the other event types. Might include uncategorized Microsoft Windows event logs.  
`RESOURCE_CREATION` | The resource was created/provisioned. This is equivalent to USER_RESOURCE_CREATION.  
`RESOURCE_DELETION` | The resource was deleted/deprovisioned. This is equivalent to USER_RESOURCE_DELETION.  
`RESOURCE_PERMISSIONS_CHANGE` | The resource had it's permissions or ACLs updated. This is equivalent to USER_RESOURCE_UPDATE_PERMISSIONS.  
`RESOURCE_READ` | The resource was read. This is equivalent to USER_RESOURCE_ACCESS.  
`RESOURCE_WRITTEN` | The resource was written to. This is equivalent to USER_RESOURCE_UPDATE_CONTENT.  
`DEVICE_FIRMWARE_UPDATE` | Firmware update.  
`DEVICE_CONFIG_UPDATE` | Configuration update.  
`DEVICE_PROGRAM_UPLOAD` | A program or application uploaded to a device.  
`DEVICE_PROGRAM_DOWNLOAD` | A program or application downloaded to a device.  
`ANALYST_UPDATE_VERDICT` | Analyst update about the Verdict (such as true positive, false positive, or disregard) of a finding.  
`ANALYST_UPDATE_REPUTATION` | Analyst update about the Reputation (such as useful or not useful) of a finding.  
`ANALYST_UPDATE_SEVERITY_SCORE` | Analyst update about the Severity score (0-100) of a finding.  
`ANALYST_UPDATE_STATUS` | Analyst update about the finding status.  
`ANALYST_ADD_COMMENT` | Analyst addition of a comment for a finding.  
`ANALYST_UPDATE_PRIORITY` | Analyst update about the priority (such as low, medium, or high) for a finding.  
`ANALYST_UPDATE_ROOT_CAUSE` | Analyst update about the root cause for a finding.  
`ANALYST_UPDATE_REASON` | Analyst update about the reason (such as malicious or not malicious) for a finding.  
`ANALYST_UPDATE_RISK_SCORE` | Analyst update about the risk score (0-100) of a finding.  
`ENTITY_RISK_CHANGE` | An update to an entity risk score. This event type is restricted to events published by Google Security Operations Risk Analytics.  
`TRIAGE_AGENT_UPDATE_INVESTIGATION` | Triage Agent has investigated the finding.  
  
### EnrichmentState

An enrichment state.

Enums  
---  
`ENRICHMENT_STATE_UNSPECIFIED` | Unspecified.  
`ENRICHED` | The event has been enriched by Google SecOps.  
`UNENRICHED` | The event has not been enriched by Google SecOps.  
  
### AuthType

Type of system the authentication event is associated with.

Enums  
---  
`AUTHTYPE_UNSPECIFIED` | The default type.  
`MACHINE` | A machine authentication.  
`SSO` | An SSO authentication.  
`VPN` | A VPN authentication.  
`PHYSICAL` | A Physical authentication (e.g. "Badge reader").  
`TACACS` | A TACACS family protocol for networked systems authentication (e.g. TACACS, TACACS+).  
  
### Mechanism

Mechanism(s) used to authenticate.

Enums  
---  
`MECHANISM_UNSPECIFIED` | The default mechanism.  
`USERNAME_PASSWORD` | Username + password authentication.  
`OTP` | OTP authentication.  
`HARDWARE_KEY` | Hardware key authentication.  
`LOCAL` | Local authentication.  
`REMOTE` | Remote authentication.  
`REMOTE_INTERACTIVE` | RDP, Terminal Services, or VNC.  
`MECHANISM_OTHER` | Some other mechanism that is not defined here.  
`BADGE_READER` | Badge reader authentication  
`NETWORK` | Network authentication.  
`BATCH` | Batch authentication.  
`SERVICE` | Service authentication  
`UNLOCK` | Direct human-interactive unlock authentication.  
`NETWORK_CLEAR_TEXT` | Network clear text authentication.  
`NEW_CREDENTIALS` | Authentication with new credentials.  
`INTERACTIVE` | Interactive authentication.  
`CACHED_INTERACTIVE` | Interactive authentication using cached credentials.  
`CACHED_REMOTE_INTERACTIVE` | Cached Remote Interactive authentication using cached credentials.  
`CACHED_UNLOCK` | Cached Remote Interactive authentication using cached credentials.  
`BIOMETRIC` | Biometric device such as a fingerprint reader.  
`WEARABLE` | Wearable such as an Apple Watch.  
  
### Outcome

The outcome of the authentication event.

Enums  
---  
`OUTCOME_UNSPECIFIED` | The default outcome.  
`SUCCESS` | The authentication was successful.  
`FAILURE` | The authentication failed.  
  
### RecordType

The type of activity record from the Utmp file.

Enums  
---  
`RECORD_TYPE_UNSPECIFIED` | The default record type.  
`RUN_LVL` | Run-level change.  
`BOOT_TIME` | System boot time.  
`NEW_TIME` | New time after system clock change.  
`OLD_TIME` | Old time before system clock change.  
`INIT_PROCESS` | Process spawned by init.  
`LOGIN_PROCESS` | Login process.  
`USER_PROCESS` | Normal user process (logged-in session).  
`DEAD_PROCESS` | Terminated process (session ended).  
`ACCOUNTING` | Accounting message.  
  
### Channel

The channel specifies the source or category of the event.

Enums  
---  
`CHANNEL_UNSPECIFIED` | Default channel.  
`SECURITY` | The security channel.  
`SYSTEM` | The system channel.  
`APPLICATION` | The application channel.  
`SETUP` | The setup channel.  
`FORWARDED_EVENTS` | The forwarded events channel.  
`OTHER` | The other channel.  
  
### EntityType

Describes the type of entity. An unknown event type.

Enums  
---  
`UNKNOWN_ENTITYTYPE` | @hide_from_doc  
`ASSET` | An asset, such as workstation, laptop, phone, virtual machine, etc.  
`USER` | User.  
`GROUP` | Group.  
`RESOURCE` | Resource.  
`IP_ADDRESS` | An external IP address. The request should include IOC intel threat metadata for each entity to be ingested.  
`CIDR_BLOCK` | A CIDR block.  
`FILE` | A file.  
`DOMAIN_NAME` | A domain.  
`URL` | A url.  
`MUTEX` | A mutex.  
`METRIC` | A metric.  
`AI` | An AI system (Model, agent, tool, etc.)  
  
### SourceType

Describes the source of an entity.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Default source type  
`ENTITY_CONTEXT` | Entities ingested from customers (e.g. AD_CONTEXT, DLP_CONTEXT)  
`DERIVED_CONTEXT` | Entities derived from customer data such as prevalence, artifact first/last seen, or asset/user first seen stats.  
`GLOBAL_CONTEXT` | Global contextual entities such as WHOIS or Safe Browsing.  
  
### Relationship

Type of relationship between the primary entity (a) and related entity (b).

Enums  
---  
`RELATIONSHIP_UNSPECIFIED` | Default value  
`OWNS` | Related entity is owned by the primary entity (e.g. user owns device asset).  
`ADMINISTERS` | Related entity is administered by the primary entity (e.g. user administers a group).  
`MEMBER` | Primary entity is a member of the related entity (e.g. user is a member of a group).  
`EXECUTES` | Primary entity may have executed the related entity.  
`DOWNLOADED_FROM` | Primary entity may have been downloaded from the related entity.  
`CONTACTS` | Primary entity contacts the related entity.  
  
### Directionality

Describes the relationship model as directed or undirected.

Enums  
---  
`DIRECTIONALITY_UNSPECIFIED` | Default value.  
`BIDIRECTIONAL` | Modeled in both directions. Primary entity (a) to related entity (b) and related entity (b) to primary entity (a).  
`UNIDIRECTIONAL` | Modeled in a single direction. Primary entity (a) to related entity (b).  
  
### EntityLabel

Entity label of the relation.

Enums  
---  
`ENTITY_LABEL_UNSPECIFIED` | Default value.  
`PRINCIPAL` | The Noun represents a principal type object.  
`TARGET` | The Noun represents a target type object.  
`OBSERVER` | The Noun represents an observer type object.  
`SRC` | The Noun represents src type object.  
`NETWORK` | The Noun represents a network type object.  
`SECURITY_RESULT` | The Noun represents a SecurityResult object.  
`INTERMEDIARY` | The Noun represents an intermediary type object.  
  
### AggregateFunction

Mathematic function used to calculate the value.

Enums  
---  
`AGGREGATE_FUNCTION_UNSPECIFIED` | Default value.  
`MIN` | Minimum.  
`MAX` | Maximum.  
`COUNT` | Count.  
`SUM` | Sum.  
`AVG` | Average.  
`STDDEV` | Standard Deviation.  
  
### MetricName

The name of the precomputed analytic.

Enums  
---  
`METRIC_NAME_UNSPECIFIED` | Default  
`NETWORK_BYTES_INBOUND` | Total received network bytes.  
`NETWORK_BYTES_OUTBOUND` | Total network sent bytes.  
`NETWORK_BYTES_TOTAL` | Total network sent bytes and received bytes.  
`AUTH_ATTEMPTS_SUCCESS` | Successful authentication attempts.  
`AUTH_ATTEMPTS_FAIL` | Failed authentication attempts.  
`AUTH_ATTEMPTS_TOTAL` | Total authentication attempts.  
`DNS_BYTES_OUTBOUND` | Total number of sent bytes for DNS events.  
`NETWORK_FLOWS_INBOUND` | Total number of events having non-null received bytes.  
`NETWORK_FLOWS_OUTBOUND` | Total number of events having non-null sent bytes.  
`NETWORK_FLOWS_TOTAL` | Total events having non-null sent or received bytes.  
`DNS_QUERIES_SUCCESS` | DNS query success count - Number of events with response_code = 0.  
`DNS_QUERIES_FAIL` | Number of events with response_code != 0.  
`DNS_QUERIES_TOTAL` | Total number of DNS queries made.  
`FILE_EXECUTIONS_SUCCESS` | Number of successful file executions.  
`FILE_EXECUTIONS_FAIL` | Number of failed file executions.  
`FILE_EXECUTIONS_TOTAL` | Total number file executions.  
`HTTP_QUERIES_SUCCESS` | Number of successful HTTP queries.  
`HTTP_QUERIES_FAIL` | Number of failed HTTP queries.  
`HTTP_QUERIES_TOTAL` | Total number of HTTP queries.  
`WORKSPACE_EMAILS_SENT_TOTAL` | Total number of emails sent in Google Workspace.  
`WORKSPACE_TOTAL_DOWNLOAD_ACTIONS` | Total number of download actions in Google Workspace.  
`WORKSPACE_TOTAL_CHANGE_ACTIONS` | Total number of change actions in Google Workspace.  
`WORKSPACE_AUTH_ATTEMPTS_TOTAL` | Total number of authentication attempts in Google Workspace.  
`WORKSPACE_NETWORK_BYTES_OUTBOUND` | Number of outbound network bytes (total sent) in Google Workspace.  
`WORKSPACE_NETWORK_BYTES_TOTAL` | Total number of network bytes (both sent and received) in Google Workspace.  
`ALERT_EVENT_NAME_COUNT` | Track number of alerts fired by EDR/SENTINEL/MICROSOFT_GRAPH.  
`RESOURCE_CREATION_TOTAL` | Analytic tracking successful resource creations.  
`RESOURCE_CREATION_SUCCESS` | Analytic tracking successful resource creations.  
`RESOURCE_READ_SUCCESS` | Analytic tracking successful resource reads.  
`RESOURCE_READ_FAIL` | Analytic tracking failed resource reads.  
`RESOURCE_DELETION_SUCCESS` | Analytic tracking successful resource deletions.  
`RESOURCE_CREATION_FAIL` | Analytic tracking failed resource creations.  
`RESOURCE_DELETION_FAIL` | Analytic tracking failed resource deletions.  
`RESOURCE_DELETION_TOTAL` | Analytic tracking total resource deletions.  
`RESOURCE_READ_TOTAL` | Analytic tracking total resource reads.  
`RESOURCE_WRITTEN_FAIL` | Analytic tracking failed resource writes.  
`RESOURCE_WRITTEN_SUCCESS` | Analytic tracking successful resource writes.  
`RESOURCE_WRITTEN_TOTAL` | Analytic tracking total resource writes.  
`UDM_DATA_PRESENCE_SUMMARY` | UDM data summary tracking unique values of dimensions.  
  
### Dimension

Describes field used as the dimension when grouping data to calculate the aggregate metric.

Enums  
---  
`DIMENSION_UNSPECIFIED` | Default  
`PRINCIPAL_DEVICE` | Principal Device  
`TARGET_USER` | Target User  
`TARGET_DEVICE` | Target Device  
`PRINCIPAL_USER` | Principal User  
`TARGET_IP` | Target IP  
`PRINCIPAL_FILE_HASH` | Principal File Hash  
`PRINCIPAL_COUNTRY` | Principal Country  
`SECURITY_CATEGORY` | Security Category  
`NETWORK_ASN` | Network ASN  
`CLIENT_CERTIFICATE_HASH` | Client Certificate Hash  
`DNS_QUERY_TYPE` | DNS Query Type  
`DNS_DOMAIN` | DNS Domain  
`HTTP_USER_AGENT` | HTTP User Agent  
`EVENT_TYPE` | Event Type  
`PRODUCT_NAME` | Product Name  
`PRODUCT_EVENT_TYPE` | Product Event Type  
`PARENT_FOLDER_PATH` | Parent Folder Path  
`TARGET_RESOURCE_NAME` | Target resource Name  
`PRINCIPAL_APPLICATION` | Principal Application.  
`TARGET_APPLICATION` | Target Application.  
`EMAIL_TO_ADDRESS` | Email To Address.  
`EMAIL_FROM_ADDRESS` | Email From Address.  
`MAIL_ID` | Mail Id.  
`PRINCIPAL_IP` | Principal IP.  
`SECURITY_ACTION` | Security Action.  
`SECURITY_RULE_ID` | Security Rule Id.  
`TARGET_NETWORK_ORGANIZATION_NAME` | Target Network Organization name.  
`PRINCIPAL_NETWORK_ORGANIZATION_NAME` | Principal Network Organization name.  
`PRINCIPAL_PROCESS_FILE_PATH` | Principal Process File Path.  
`PRINCIPAL_PROCESS_FILE_HASH` | Principal Process File SHA256 Hash.  
`SECURITY_RESULT_RULE_NAME` | Security Result rule name.  
`TARGET_RESOURCE_LABEL_KEY` | Target Resource label key.  
`VENDOR_NAME` | Vendor name.  
`TARGET_RESOURCE_TYPE` | Target Resource type.  
`TARGET_LOCATION_NAME` | Target Location name.  
`LOG_TYPE` | Log type.  
`TARGET_HOSTNAME` | Target Hostname.  
  
### EnrichmentType

Type of enrichment.

Enums  
---  
`ENRICHMENT_TYPE_UNSPECIFIED` | Enrichment type is unspecified.  
`APPEND` | The data table was appended to the entity graph.  
`OVERRIDE` | The entity graph was overridden by the data table.  
  
### ResponsePlatformType

Available response platforms.

Enums  
---  
`RESPONSE_PLATFORM_TYPE_UNSPECIFIED` | Response platform not specified.  
`RESPONSE_PLATFORM_TYPE_SIEMPLIFY` | Siemplify  
  
### UserType

Enums  
---  
`USER_TYPE_UNSPECIFIED` |   
`ANALYST` |   
`TRIAGE_AGENT` |   
  
### DetectionTimingDetails

Detection timing details for the collection.

Enums  
---  
`DETECTION_TIMING_DETAILS_UNSPECIFIED` | Detection timing details are unspecified.  
`DETECTION_TIMING_DETAILS_REPROCESSING` | Detection is generated by a reprocessing run.  
`DETECTION_TIMING_DETAILS_RETROHUNT` | Detection is generated by a retrohunt run.  
  
### RunFrequency

Run frequencies used by rule executions.

Enums  
---  
`RUN_FREQUENCY_UNSPECIFIED` | Unspecified run frequency.  
`RUN_FREQUENCY_REALTIME` | Real-time run frequency.  
`RUN_FREQUENCY_HOURLY` | Executes once an hour.  
`RUN_FREQUENCY_DAILY` | Executes once a day.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
