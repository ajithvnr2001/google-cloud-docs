---
url: https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs/
title: View flow logs for multicast \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.067767+00:00
---

# View flow logs for multicast  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View flow logs for multicast

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes support for multicast traffic for Cloud Multicast in VPC Flow Logs.

VPC Flow Logs samples packets in your Virtual Private Cloud (VPC) network to generate flow logs. Flow logs are aggregated by IP connection (5-tuple).

These logs can be used for network monitoring, forensics, security analysis, and expense optimization. For example, multicast producers can use log-based metrics to track packet loss for multicast consumers. For more information, see the [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics) in the Cloud Logging documentation.

For more information, see the [VPC Flow Logs overview](https://docs.cloud.google.com/vpc/docs/flow-logs).

## VPC Flow Logs records for multicast

The following table summarizes the unique information included in VPC Flow Logs records for multicast traffic depending on whether the reporter of the flow is a multicast producer or a multicast consumer.

VPC Flow Logs writes logs to the project of the reporting VPC network as described in [Logs collection](https://docs.cloud.google.com/vpc/docs/flow-logs#logs_collection). Log records for a multicast producer (`SRC`), including per-consumer flow logs, are available in the project that contains the multicast producer VPC network. Log records for a multicast consumer (`DEST`) are available in the project that contains the multicast consumer VPC network.

For a full list of fields in VPC Flow Logs records, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

Flow reporter | Description of logs  
---|---  
Multicast producer |  For multicast producers, VPC Flow Logs generates two sets of flow logs:  


  * Regular flow logs that correspond to the aggregate traffic sent to multicast consumers. These flow logs include information about the corresponding multicast domain and group range so that you can observe throughput from a multicast producer to a group.
  * Per-consumer flow logs that provide observability for individual multicast consumers. These flow logs include information about the corresponding multicast domain and group range, per-consumer latency, and per-consumer packet loss. To help ensure accurate loss and latency measurements, multicast producers must set a unique [IP ID](https://en.wikipedia.org/wiki/IPv4#Identification) per packet.

For details, see Record format for multicast producers.   
Multicast consumer |  VPC Flow Logs records include the following additional information:  


  * Information about the corresponding multicast domain and group range so that you can observe throughput from a multicast group to the multicast consumer.
  * Network packet loss
  * Network latency

For details, see Record format for multicast consumers.  
  
### Record format for multicast producers

This section describes the unique fields and field format differences in VPC Flow Logs records for multicast traffic when the reporter of the flow is a multicast producer.

For a given multicast producer flow, VPC Flow Logs generates up to three flow log records for the same traffic:

  * **A regular log record**. This record corresponds to aggregate traffic to a group and is always generated.
  * **A per-consumer latency log record**. This record is typically always generated. However, in rare cases when 100% packet loss occurs during the [aggregation interval](https://docs.cloud.google.com/vpc/docs/flow-logs#logs_collection), this record isn't generated.
  * **A per-consumer packet loss record**. This record is generated only if packet loss occurs.



For details about the fields in each log record, see the following table.

Field | Field format | Field type: Base or optional metadata  
---|---|---  
log_type |  string   
If the log is a per-consumer log, this field is populated with a value of `PER_MULTICAST_CONSUMER_PRODUCER_LOG`. Otherwise, this field isn't populated.  | Base  
disposition |  string   
Applies to per-consumer logs. If the log represents packet loss, this field is populated with a value of `DROPPED`. Otherwise, this field isn't populated.  | Base  
drop_reason |  string   
Applies to per-consumer logs. If the value of the `disposition` field is `DROPPED`, this field is populated with a value of `LOST_IN_TRANSIT`. Otherwise, this field isn't populated.  | Base  
one_way_network_latencies |  Latencies   
Applies to per-consumer logs. If the `disposition` isn't populated, meaning there is no packet loss, this field is populated with one-way network latency in milliseconds with sub-millisecond precision as measured during the aggregation interval. If not populated, the measurement isn't available.  | Base  
rtt_msec |  Not populated for multicast traffic.  | Base  
round_trip_time |  Not populated for multicast traffic.  | Base  
bytes_sent |  int64   
Populated as follows: 

  * If the `disposition` field isn't populated, this field is the estimated number of user payload bytes sent from the multicast producer to the consumer.
  * If the `disposition` field is populated with a value of `DROPPED`, this field is the estimated number of user payload bytes dropped.

Consider an example in which a multicast producer sends 1000 bytes, but 100 bytes are dropped. In this case, two separate per-consumer logs are generated: one with `bytes_sent: 900`, and one with `bytes_sent: 100`.  | Base  
packets_sent |  int64   
Populated as follows: 

  * If the `disposition` field isn't populated, this field is the estimated number of packets sent from the multicast producer to the consumer.
  * If the `disposition` field is populated with a value of `DROPPED`, this field is the estimated number of packets dropped.

Consider an example in which a multicast producer sends 100 packets, but 10 packets are dropped. In this case, two separate per-consumer logs are generated: one with `packets_sent: 90`, and one with `packets_sent: 10`.  | Base  
Source and destination metadata fields  
dest_multicast_group_range |  MulticastGroupDetails   
If the destination of the flow is a multicast group IP address and reporter of the flow is a multicast producer, then this field is populated with multicast domain and group range details.  | Metadata  
dest_instance |  [InstanceDetails](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#InstanceDetails)   
Populated as follows: 

  * If the multicast producer and consumer are in the same project, or if they are in the same organization but separate projects and [cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project) are enabled, this field is populated with no differences from the regular format.
  * If the multicast producer and consumer are in separate projects and cross-project annotations disabled, this field is populated with alternative consumer identifiers as described in InstanceDetails field format differences.

| Metadata  
dest_vpc |  [VpcDetails](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#VpcDetails)   
Populated as follows: 

  * If the multicast producer and consumer are in the same project, or if they are in the same organization but separate projects and [cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project) are enabled, this field is populated with no differences from the regular format.
  * If the multicast producer and consumer are in separate projects and cross-project annotations disabled, this field is populated with alternative consumer identifiers described in VpcDetails field format differences.

| Metadata  
  
### Record format for multicast consumers

The following table describes the unique fields and field format differences in VPC Flow Logs records for multicast traffic when the reporter of the flow is a multicast consumer.

For a given multicast consumer flow, VPC Flow Logs generates up to two separate flow log records for the same traffic:

  * One log record for successfully delivered packets. This record is generated by default, except in rare cases when 100% network packet loss occurs during the [aggregation interval](https://docs.cloud.google.com/vpc/docs/flow-logs#logs_collection).
  * One log record for dropped packets. This record is generated only if packet loss occurs.



For details about the fields in each log record, see the following table.

Field | Field format | Field type: Base or optional metadata  
---|---|---  
disposition |  string   
If the log represents packet loss, this field is populated with a value of `DROPPED`. Otherwise, this field isn't populated.  | Base  
drop_reason |  string   
If the value of the `disposition` field is `DROPPED`, this field is populated with a value of `LOST_IN_TRANSIT`. Otherwise, this field isn't populated.  | Base  
one_way_network_latencies |  Latencies   
If the `disposition` isn't populated, meaning there is no packet loss, this field is populated with one-way network latency in milliseconds with nanosecond-level precision as measured during the aggregation interval. The latency measurement excludes time consumed by the application. If not populated, the measurement isn't available.  | Base  
rtt_msec |  Not populated for multicast traffic.  | Base  
round_trip_time |  Not populated for multicast traffic.  | Base  
bytes_sent |  int64   
Populated as follows: 

  * If the `disposition` field isn't populated, this field is the number of user payload bytes sent from the multicast producer to the consumer.
  * If the `disposition` field is populated with a value of `DROPPED`, this field is the number of user payload bytes dropped.

Consider an example in which a multicast producer sends 1000 bytes, but 100 bytes are dropped. In this case, two separate logs are generated: one with `bytes_sent: 900`, and one with `bytes_sent: 100`.  | Base  
packets_sent |  int64   
Populated as follows: 

  * If the `disposition` field isn't populated, this field is the number of packets sent from the multicast producer to the consumer.
  * If the `disposition` field is populated with a value of `DROPPED`, this field is the number of packets dropped.

| Base  
Source and destination metadata fields  
src_multicast_group_consumer_activation |  MulticastGroupConsumerActivationDetails   
If the destination of the flow is a multicast group IP address and the reporter of the flow is a multicast consumer, then this field is populated with multicast consumer association and group consumer activation details.  | Metadata  
  
### Field format reference

This section provides a reference for field formats in flow log records.

For a full list of field formats in VPC Flow Logs records, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

#### Latencies field format

Field | Type | Description  
---|---|---  
median_msec | double | The median latency as measured during the aggregation interval.  
  
#### MulticastGroupDetails field format

Field | Type | Description  
---|---|---  
project_id | string | The ID of the multicast administrator project.  
location | string | The zone of the multicast producer.  
name | string | The name of the multicast group range that contains the group IP address that traffic was sent to.  
domain | string | The name of the multicast domain that contains the group range.  
  
#### InstanceDetails field format differences

If the multicast producer and consumer are in separate projects and cross-project annotations are disabled, the following identifiers are used for the destination instance. These fields are populated because the regular string fields `vm_name` and `project_id` aren't available.

Field | Type | Description  
---|---|---  
instance_id | int64 | Integer ID of the instance.  
project_number | int64 | Project number for the instance.  
  
#### VpcDetails field format differences

If the multicast producer and consumer are in separate projects and cross-project annotations are disabled, the following identifiers are used for the destination VPC network. These fields are populated because the regular string fields `vpc_name` or `project_id` aren't available.

Field | Type | Description  
---|---|---  
vpc_id | int64 | Integer ID of the VPC network.  
project_number | int64 | Project number for the VPC network.  
  
#### MulticastGroupConsumerActivationDetails field format

Field | Type | Description  
---|---|---  
project_id | string | The ID of the project that contains the multicast consumer VPC network.  
location | string | The zone of the multicast consumer.  
name | string | The name of the multicast group consumer activation that was created when the multicast consumer VPC network was activated for the group range.  
domain_association | string | The name of the multicast consumer association between the multicast consumer VPC network and the domain.  
  
## View flow logs in Cloud Logging

You can view flow logs in [Cloud Logging](https://docs.cloud.google.com/logging), and you can export logs to any destination that Cloud Logging export supports.

To view flow logs in Cloud Logging, do the following:

  1. If you haven't already, configure VPC Flow Logs. See [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) in the VPC Flow Logs documentation.
  2. Follow the steps to [access flow logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs).



## Analyze traffic flows with Flow Analyzer

Flow Analyzer lets you quickly and efficiently understand your traffic flows without the need to write complex SQL queries. For more information, see the [Flow Analyzer overview](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview).

All of the information in VPC Flow Logs records for multicast is available in Flow Analyzer

Before you begin, review the following limitation: Connectivity Tests doesn't support multicast. In Flow Analyzer, UI options for running Connectivity Tests are disabled where applicable.

To analyze traffic flows, do the following:

  1. If you haven't already, enable Observability Analytics. See [Enable Observability Analytics](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/enable-log-analytics) in the Flow Analyzer documentation.

  2. Follow the steps to [analyze your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows) by building and running queries on your flow logs.

Consider the following when analyzing multicast traffic flows:

     * **Filters** : [Basic filters](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#basic-filters) let you define the scope of a query.

       * Filtering on multicast fields is available through the **Flow Parameters** filter list. For more information, see the following Filter reference for multicast fields.

       * For multicast producers, keep in mind that VPC Flow Logs generates both regular flow logs and per-consumer flow logs. If you want to view aggregate data without double-counting logs, specify `is unknown` for the **Multicast Log Type**. This ensures that only data for regular log records is displayed.

     * **Display options** : After running a query, you can refine your results by using display options.

       * To view throughput data, use the [**Data volume**](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#data-volume) display mode.

       * To view latency data, use the [**Latency**](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#latency) display mode. Ensure that you select **One-way (median)** for the **Metric type**. While round-trip time (RTT) is the default metric type, this data isn't available in multicast flow logs.

       * To view packet loss data, use the [**Packet drops**](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#packet-drops) display mode.




### Filter reference for multicast fields

This section provides a reference for the Flow Analyzer filters that correspond to VPC Flow Logs record fields for multicast traffic.

#### Filters for multicast producer logs

Field in VPC Flow Logs records | Filter in Flow Analyzer | Filter type  
---|---|---  
log_type | Multicast Log Type | Flow parameter  
MulticastGroupDetails  
dest_multicast_group_range.project_id | Multicast Admin Project ID | Flow parameter  
dest_multicast_group_range.location | Multicast Producer Location | Flow parameter  
dest_multicast_group_range.name | Multicast Admin Group Range Name | Flow parameter  
dest_multicast_group_range.domain | Multicast Admin Domain Name | Flow parameter  
InstanceDetails1  
dest_instance.instance_id | GCE instance ID | Destination  
dest_instance.project_number | GCE instance project number | Destination  
VpcDetails1  
dest_vpc.vpc_id | VPC ID | Destination  
dest_vpc.project_number | VPC project number | Destination  
  
1 These alternative destination filters are used only when the multicast producer and consumer are in separate projects and cross-project annotations are disabled as described in Record format for multicast producers.

#### Filters for multicast consumer logs

Field in VPC Flow Logs records | Filter in Flow Analyzer | Filter type  
---|---|---  
MulticastGroupConsumerActivationDetails  
src_multicast_group_consumer_activation.project_id | Multicast Consumer Project ID | Flow parameter  
src_multicast_group_consumer_activation.location | Multicast Consumer Location | Flow parameter  
src_multicast_group_consumer_activation.name | Multicast Consumer Activation Name | Flow parameter  
src_multicast_group_consumer_activation.domain_association | Multicast Consumer Domain Association | Flow parameter  
  
## What's next

  * [Get an overview of Cloud Multicast observability](https://docs.cloud.google.com/vpc/docs/multicast/observability)
  * [View multicast group membership event logs](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs)
  * [Monitor membership metrics for multicast](https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
