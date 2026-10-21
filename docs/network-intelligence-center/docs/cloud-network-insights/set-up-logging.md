---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging/
title: Set up logging \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:23.056726+00:00
---

# Set up logging  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Set up logging Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how Cloud Network Insights integrates with AppNeta for alarm generation and how these alarms are sent to Google Cloud for analysis, viewing, and alert policy creation.

Logging and alerting tasks are split between Google Cloud and AppNeta. Cloud Network Insights logging tracks when the metrics collected by Monitoring Points violate thresholds you configure with alarm rules in AppNeta.

Create alarms and alarm rules in AppNeta to generate alarm logs. Alarm logs and event logs are then exported into [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). You can then use [alert policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts) to send alerts and notifications when a network incident occurs.

## Before you begin

You must [deploy a Monitoring Point](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points) before you can create alarm rules.

## Alarms in AppNeta

Alarms and alarm rules are created in AppNeta. Alarms let you know when there's an issue in your network. If a metric you track, such as latency, exceeds a set threshold within a specific interval, that is a violation of the alarm rule. You can choose to trigger an alarm after a single violation or after multiple violations over a set interval.

For example, if latency exceeds 160ms twice within 3 minutes, you can set the alarm to trigger a warning. This alarm is sent to Google Cloud as a log. Once the log arrives in Cloud Logging, you can send an alert on it and notify your team.

For more information about alarms, see [Alarms Overview](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms.html) or [Alarms – Best Practices](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms-best-practices.html) in the AppNeta documentation.

### Create alarm rules in AppNeta

Create alarm rules that define performance thresholds.

  1. Open the Google Cloud console and navigate to **Network Intelligence** > **Cloud Network Insights** > **Alert Policies**.

[Go to Alert Policies](https://console.cloud.google.com/net-intelligence/cloud-network-insights/alert-policies)

  2. Click **Create Alarm Rules** to open the **Alarm Rule Edit** page in AppNeta.

  3. Define rules specifying metrics, thresholds, violation strategies, and severity. You can use or customize default rules.




After an alarm is triggered, the alarm log is sent to Cloud Logging. After the log is sent to Google Cloud, you can navigate to Cloud Network Insights and [set your alert policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts).

For more information about creating alarm rules, see [Alarm Rules](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms-rules.html) in the AppNeta documentation.

## View logs in Google Cloud

Cloud Network Insights exports detailed logs in Cloud Logging to help you analyze and troubleshoot network performance and significant events. You can access these logs using the Logs Explorer.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Create queries to alert on relevant information.




Cloud Network Insights logs use one of the following for `logName`:

  * Alarm logs - `networkmanagement.googleapis.com/insights_alarm`
  * Event logs - `networkmanagement.googleapis.com/insights_event`



For more information, see [Build and save queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries).

## Pricing

All Cloud Network Insights logs are written to Cloud Logging. There is no separate charge from Cloud Network Insights for this service. However, these logs can result in additional storage costs depending on the size of the logs that are written and stored.

For information about Cloud Logging pricing, see [Pricing for Google Cloud Observability: Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing).

## Log details

While the specific details for each log type are contained within the `jsonPayload` field, several other standard LogEntry fields are crucial for querying and understanding the logs.

### Alarm logs

  * **Log Name** : `networkmanagement.googleapis.com/insights_alarm`
  * **Triggered** : Generated when the conditions of an alarm rule are met.
  * **Resource Labels** : Describes the monitored resource associated with the log. This includes the following: 
    * `type` \- The type of resource, can be one of the following: 
      * `networkmanagement.googleapis.com/NetworkMonitoringProvider`
      * `networkmanagement.googleapis.com/MonitoringPoint`
      * `networkmanagement.googleapis.com/NetworkPath`
    * `labels` \- Key-value pairs identifying the specific resource instance, such as `resource_container` (project ID), `location`, `network_monitoring_provider_id`, and `path_id` or `monitoring_point_id`.
  * **Key JSON Fields** : Alarm logs provide information about triggered alarms.
  * **Severity Mapping** : Severity is recorded differently between AppNeta and Google Cloud. **AppNeta severity** | **Google Cloud log severity**  
---|---  
Critical | CRITICAL  
Major | ERROR  
Minor | WARNING  
Warning | NOTICE  



### Alarm log fields

The `jsonPayload` of an alarm log contains the following fields.

**Field** | **Type** | **Description**  
---|---|---  
`alarm_id` | string | The unique identifier for the alarm in AppNeta.  
`alarm_severity` | enum | The severity of the alarm. Can be `CRITICAL`, `MAJOR`, `MINOR`, or `WARNING`.  
`alarm_type` | enum | The type of the alarm. The `QUALITY_OF_SERVICE` type is supported.  
`cleared_reason` | string | The reason why the alarm was cleared. Generated only when `state` = "CLEARED" (omitted or null otherwise). Common string values include `alarm-rule-no-longer-violated`, `stale`, `rule-deleted`, and `duplicate`.  
`cleared_time` | timestamp | The time the alarm was cleared. This will be empty if the alarm log has the state `RAISED` or `UPDATED`.  
`description` | string | A human-readable description of the alarm.  
`first_violation_time` | timestamp | The time the alarm condition was first violated.  
`item` | object | The entity associated with the alarm. See Common Item Structures for details.  
`noise_conditions` | array of strings | Identifies which noise filter conditions flagged this alarm for the given rule and item pair. Alarms are evaluated against both a 24-hour frequency threshold and a short-term burst window. Can contain either one or both of the following values:

  * `frequent-detection`: Triggered when alarm occurrences on the same item reach the 24-hour threshold (default: 5 alarms).
  * `burst-detection`: Triggered when multiple alarms occur within the configured time window (default: more than 1 alarm per 60 minutes).

Returns an empty array or is omitted entirely if the alarm is not considered noisy.  
`provider_link` | string | A hyperlink to the alarm in the AppNeta UI.  
`raised_time` | timestamp | The time the alarm was raised.  
`receiveTimestamp` | string | The time the alarm was created in Google Cloud.  
`rule` | string | The name of the alarm rule that triggered the alarm.  
`state` | enum | The state of the alarm. Can be `RAISED`, `UPDATED` (the alarm details have been updated in AppNeta but not yet cleared), or `CLEARED`.  
`timestamp` | string | The time the alarm was created in AppNeta.  
  
### Event logs

  * **Log Name** : `networkmanagement.googleapis.com/insights_event`
  * **Trigger** : Generated when a structural change occurs (for example, `Route Change`, `MTU Change`, or `Monitoring Point Offline`).
  * **Severity** : Always `INFO`.
  * Key JSON Fields: Event logs provide information about triggered events.



### Event log fields

The `jsonPayload` of an event log contains the following fields.

**Field** | **Type** | **Description**  
---|---|---  
`event_detail` | object | Details specific to the event type. This can be `route_change_event`, `mtu_change_event`, `qos_change_event`, or `forwarding_loss_clear_event`. An empty object will be returned for events that have no further details. See  Event detail fields for details.  
`event_id` | string | The unique identifier for this event.  
`event_type` | enum | The type of event. Can be `MONITORING_POINT_OFFLINE`, `MONITORING_POINT_ONLINE`, `ROUTE_CHANGE`, `MTU_CHANGE`, `QOS_CHANGE`, or `FORWARDING_LOSS_CLEAR`.  
`item` | object | The entity associated with the event. See Common item structures for details.  
`receiveTimestamp` | string | The time the event was created in Google Cloud.  
`timestamp` | string | The time the event was created in AppNeta.  
  
### Event detail fields

The `event_detail` object contains details specific to the event type. Depending on the `event_type`, it contains one of the following nested objects:

  * `mtu_change_event`
  * `qos_change_event`
  * `forwarding_loss_clear_event`
  * `route_change_event`



An empty object is returned for events with no further details.

#### MTU change event (`mtu_change_event`)

This object captures details whenever the MTU size is modified.

Field | Type | Description  
---|---|---  
`new_mtu` | int32 | The newly measured MTU.  
`previous_mtu` | int32 | The previous MTU, if there was one (omitted on startup).  
`mtu_exceeded` | hop object | Hop containing details (such as the IP address) of the node reporting the packet-too-big error. See Hop for more details.  
  
#### QoS change event (`qos_change_event`)

This object reports QoS remapping on all detected paths.

Field | Type | Description  
---|---|---  
`configured_qos` | int32 | The QoS configured in the job settings.  
`remapped_qos` | int32 | Altered QoS detected on the path.  
`ip_address` | string | The IP address of the hop where the QoS change was detected, if known.  
  
#### Forwarding loss clear event (`forwarding_loss_clear_event`)

This object reports that sustained packet loss beginning at a specific network hop (forwarding loss) has cleared and normal forwarding has resumed. This event captures when normal forwarding resumes and the initial suspected timestamp. The onset of forwarding loss is monitored using AppNeta alarms.

Field | Type | Description  
---|---|---  
`protocol` | string | The monitoring protocol (such as `TCP`, `UDP`, and `ICMP`).  
`first_hop` | hop object | The first hop where forwarding loss started. See  Hop for more details.  
`initial_loss_suspected_time` | timestamp | The time when forwarding loss was initially suspected.  
  
#### Route change event (`route_change_event`)

The object captures differences in hop count or sequence of known IP addresses between consecutive traceroutes.

Field | Type | Description  
---|---|---  
`previous_route_change_time` | timestamp | The timestamp of the traceroute that first detected the previous route.  
`protocol` | string | The protocol used for the traceroute (such as `TCP`, `UDP`, and `ICMP`).  
`hop_count` | int32 | The total number of hops in the route.  
`target_ip` | string | The target IP address of the traceroute.  
`route_changes` | array of objects | An array of all detected changes. Each object contains a `route_change_type` string and a `details` object. See Route change details.  
  
### Route change details

The `details` object inside the `route_changes` array depends on the `route_change_type`:

  * **`incomplete_route`** or **`complete_route`**
    * `terminal_hop` (hop object): The last hop successfully reached (or final hop if complete).
    * `terminal_network` (network object): The network information for the terminal hop.
  * **`route_loop`**
    * `first_hop` (hop object): The first hop in the detected route loop.
    * `last_hop` (hop object): The last hop in the detected route loop.
    * `loop_span` (int32): The number of hops involved in the loop.
  * **`target_ip_change`**
    * `previous_target_ip` (string): The target IP address observed in the previous traceroute.
    * `new_target_ip` (string): The current target IP address.
  * **`sequence_change`**
    * `last_common_hop` (hop object): The last common hop between the previous and current traceroutes.
    * `previous_next_hop` (hop object): The previous next-hop device in the sequence.
    * `new_next_hop` (hop object): The new next-hop device in the sequence.
    * `previous_hop_count` (int32): Total number of hops in the previous traceroute.
    * `hop_count` (int32): Total number of hops in the current traceroute.
  * **`network_change`**
    * `previous_asns` (array of int32): Sequence of ASN Network for the path.
    * `new_asns` (array of int32): The new sequence of ASN Network for the path.
  * **`isp_change`**
    * `previous_isp` (network object): The ISP observed in the previous traceroute.
    * `new_isp` (network object): The current ISP observed.



### Common sub-objects

Hop and network objects are returned for multiple fields.

#### Hop

Hop objects describe a specific network hop.

Field | Type | Description  
---|---|---  
`hop_number` | int32 | The hop number in the traceroute.  
`ip_address` | string | The IP address of the hop.  
`hostname` | string | The hostname resolved for the hop's IP address.  
  
#### Network

A network object describes the network where an action occurred.

Field | Type | Description  
---|---|---  
`asn` | int32 | The Autonomous System Number (ASN) of the network.  
`display_name` | string | The name of the network (such as ISP name or organization name).  
  
### Common item structures

The item field within the `jsonPayload` of both Alarm and Event logs contains details about the associated entity. The structure depends on the item type.

#### NetworkPathItem

**Field** | **Type** | **Description**  
---|---|---  
`destination` | string | The destination IP address or hostname.  
`destination_monitoring_point` | MonitoringPointItem | Details of the destination MonitoringPointItem (for MonitoringPoint-to-MonitoringPoint paths only).  
`display_name` | string | The user-defined display name of the Network Path.  
`monitoring_policy_display_name` | string | The display name of the monitoring policy.  
`monitoring_policy_id` | string | The ID of the monitoring policy.  
`network_protocol` | string | The network protocol used, such as `TCP`, `UDP`, or `ICMP`.  
`provider_tags` | array of objects | Tags defined in AppNeta for the path.  
`source_monitoring_point` | MonitoringPointItem | Details of the source MonitoringPointItem.  
  
#### WebPathItem

**Field** | **Type** | **Description**  
---|---|---  
`destination` | string | The destination URL.  
`display_name` | string | The user-defined display name of the Web Path.  
`monitoring_policy_display_name` | string | The display name of the monitoring policy.  
`monitoring_policy_id` | string | The ID of the monitoring policy.  
`provider_tags` | array | Tags defined in the provider for the path.  
`source_monitoring_point` | object | Details of the source MonitoringPoint.  
  
#### MonitoringPointItem

**Field** | **Type** | **Description**  
---|---|---  
`display_name` | string | The user-defined display name of the Monitoring Point.  
`host` | object | Details of the Monitoring Point's host.  
`id` | string | The unique identifier of the Monitoring Point.  
`provider_tags` | array | Tags defined in the provider for the Monitoring Point.  
  
#### MonitoringPointHost

**Field** | **Type** | **Description**  
---|---|---  
`cloud_instance_id` | string | The instance ID from the cloud provider.  
`cloud_project_id` | string | The Google Cloud project ID.  
`cloud_provider` | string | Cloud Provider such as `GCP`, `AWS`, or `AZURE`.  
`cloud_region` | string | The cloud region of the endpoint, for example, `us-central1`.  
`cloud_virtual_network_ids` | array of strings | User-visible cloud virtual network IDs.  
`cloud_zone` | string | The cloud zone of the endpoint, for example, `us-central1-a`.  
`labels` | map | User-defined labels configured on the VM instance.  
`os` | string | The operating system of the Monitoring Point's host.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
