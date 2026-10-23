---
url: https://docs.cloud.google.com/vpc/docs/flow-logs/
title: VPC Flow Logs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:51.600684+00:00
---

# VPC Flow Logs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VPC Flow Logs

VPC Flow Logs samples packets in your Virtual Private Cloud (VPC) network to generate flow logs. Flow logs are aggregated by IP connection (5-tuple). VPC Flow Logs samples the following packets:

  * Packets that are sent from and received by [virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances), including instances used as [Google Kubernetes Engine nodes](https://docs.cloud.google.com/kubernetes-engine/docs)
  * Packets that are sent from and received by [Cloud Run](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) or [App Engine](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) resources configured with Direct VPC egress
  * Packets that are sent through VLAN attachments for [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels



You can view flow logs in [Cloud Logging](https://docs.cloud.google.com/logging), and you can export logs to any destination that Cloud Logging export supports. These logs can be used for network monitoring, forensics, security analysis, and expense optimization. For more information, see Supported configurations.

## Use cases

The following are use cases for VPC Flow Logs.

### Network monitoring

VPC Flow Logs provides you with visibility into network throughput and performance. You can:

  * Monitor the VPC network
  * Perform network diagnosis
  * Filter the flow logs by VMs, serverless endpoints, VLAN attachments, and Cloud VPN tunnels to understand traffic changes
  * Understand traffic growth for capacity forecasting



### Understanding network usage and optimizing network traffic expenses

You can analyze network usage with VPC Flow Logs to optimize network traffic expenses. For example, you can analyze the network flows for the following:

  * Traffic between regions and zones
  * Traffic to specific countries on the internet
  * Traffic to on-premises and other cloud networks
  * Top talkers in the network, including VMs, serverless endpoints, VLAN attachments, and Cloud VPN tunnels



### Network forensics

You can use VPC Flow Logs for network forensics. For example, if an incident occurs, you can examine the following:

  * Which IP addresses have communicated with each other and when
  * Which IPs are compromised by analyzing all the incoming and outgoing network flows



[Learn how Google Cloud users strengthen their cyber defense with VPC Flow Logs](https://www.youtube.com/watch?v=v3lx-rKkM-g).

## Supported configurations

You can enable VPC Flow Logs at the organization and project levels. An organization-level VPC Flow Logs configuration enables flow logs for all subnets, VLAN attachments, and Cloud VPN tunnels in all VPC networks in the organization.

At the project level, you can enable VPC Flow Logs for specific VPC networks, subnets, VLAN attachments, and Cloud VPN tunnels.

Configuration scope | Generates flow logs for these resources | Steps to enable  
---|---|---  
Organization | 

  * All VM instances and Cloud Run or App Engine resources in all subnets in the organization
  * All VLAN attachments in the organization
  * All Cloud VPN tunnels in the organization

| [Enable VPC Flow Logs for an organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization)  
VPC network | 

  * All VM instances and Cloud Run or App Engine resources in all subnets in the VPC network
  * All VLAN attachments in the VPC network
  * All Cloud VPN tunnels in the VPC network

| [Enable VPC Flow Logs for a VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network)  
Subnet | All VM instances and Cloud Run or App Engine resources in a specific subnet | Enable VPC Flow Logs for a subnet:

  * Recommended: [Enable VPC Flow Logs for a subnet (Network Management API)](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management)
  * [Enable VPC Flow Logs for a subnet (Compute Engine API)](https://docs.cloud.google.com/vpc/docs/using-flow-logs#compute-engine)

  
VLAN attachment | A specific VLAN attachment | [Enable VPC Flow Logs for a VLAN attachment](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-vlan-attachment)  
Cloud VPN tunnel | A specific Cloud VPN tunnel | [Enable VPC Flow Logs for a Cloud VPN tunnel](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-vpn-tunnel)  
  
You can use filtering to customize these configuration scopes. For more information, see Log sampling and processing.

## Logs collection

Packets are sampled within an aggregation interval. All packets collected for a given IP connection within the aggregation interval are aggregated into a single flow log entry, as described in Log sampling and processing. This data is then sent to [Logging](https://docs.cloud.google.com/logging/docs) in the Google Cloud project of the VPC network that reported the flow.

Logs are stored in Logging for 30 days by default. If you want to keep logs longer than that, you can either [set a custom retention period](https://docs.cloud.google.com/logging/docs/storage#logs-retention) or [export them](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to a supported destination.

Additionally, you can optionally enable TCP connection logging to capture outbound TCP connection attempts and acknowledged inbound TCP connections for VM instances and serverless endpoints. VPC Flow Logs also generates log records for dropped traffic.

### Log sampling and processing

To generate flow logs, VPC Flow Logs samples packets in your VPC network, including packets that are sent from and received by VMs and serverless endpoints and packets that pass through gateways such as VLAN attachments or Cloud VPN tunnels.

VPC Flow Logs samples packets using a _primary sampling rate_. The primary sampling rate is dynamic and varies depending on the load of the physical host running the reporting resource at the time of sampling. The probability of sampling any single IP connection increases with the volume of packets. You can't control the primary flow log sampling process or adjust the primary sampling rate.

After the flow logs are generated, VPC Flow Logs processes them according to the following procedure:

  1. **Filtering**. You can specify that only logs that match specified criteria are generated. For example, you can filter so that only logs for a particular VM or only logs with a particular metadata value are generated and the rest are discarded. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering).
  2. **Aggregation**. Information for sampled packets is aggregated over a configurable _aggregation interval_ to produce a _flow log entry_.
  3. **Secondary flow log sampling**. This is a second sampling process. Flow log entries are further sampled according to a configurable _secondary sampling rate_ parameter. The secondary sampling is performed on the flow logs generated by the primary flow log sampling process. For example, if the secondary sampling rate is set to 1.0, or 100%, VPC Flow Logs samples 100% of the flow logs generated by the primary flow log sampling.
  4. **Metadata**. If disabled, all metadata annotations are discarded. If you want to keep metadata, you can retain all fields or a specific set of fields. For more information, see [Metadata annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#metadata).
  5. **Write to Logging**. The final log entries are written to Cloud Logging.



VPC Flow Logs doesn't capture every packet. Instead, it estimates total traffic based on the sampled packets, accounting for missed packets. For more information, see [VPC Flow Logs: Understanding byte and packet counts](https://services.google.com/fh/files/misc/vpc_flow_logs_understanding_byte_and_packet_counts.pdf).

Even though Google Cloud doesn't capture every packet, log record captures can be quite large. You can balance your traffic visibility and storage cost needs by adjusting the following aspects of logs collection:

  * **Aggregation interval**. Sampled packets for a time interval are aggregated into a single log entry. This time interval can be 5 seconds (default), 30 seconds, 1 minute, 5 minutes, 10 minutes, or 15 minutes.
  * **Secondary sampling rate**. 
    * For configurations created with the Compute Engine API, 50% of log entries are kept by default. You can set this parameter from `1.0` (100%, all log entries are kept) to `0.0` (0%, no logs are kept).
    * For configurations created with the Network Management API, 100% of log entries are kept by default. You can set this parameter from `1.0` to greater than `0.0`.
  * **Metadata annotations**. By default, flow log entries are annotated with metadata information, such as the names of the source and destination within Google Cloud or the geographic region of external sources and destinations. Metadata annotations can be turned off, or you can specify only certain annotations, to save storage space.
  * **Filtering**. By default, logs are generated for every sampled flow. You can set [filters](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) to generate logs that only match certain criteria.

**Note:** If you need to analyze all packets, you can use [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) and collector instances running third-party software.

### TCP connection logging

Because the primary packet sampling can miss short-lived or low-volume TCP connections, you can optionally enable TCP connection logging for VM instances and serverless endpoints. You can configure TCP connection logging in a VPC Flow Logs configuration for a [subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management) (through the Network Management API), a [VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network), or an [organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization).

TCP connection logging captures all outbound TCP connection attempts and all acknowledged inbound TCP connections:

  * For outbound connections, VPC Flow Logs captures the initial `SYN` packet. The reporter is `SRC`, and the direction is `EGRESS`.
  * For inbound connections, VPC Flow Logs captures the `SYN-ACK` packet that is sent in response to a received `SYN` packet. The reporter is `DEST`, and the direction is `INGRESS`.



Up to 100 connections per vCPU per second (maximum 800 connections per second per VM) are logged. Connections that exceed these limits might not be logged.

TCP connection logging integrates with VPC Flow Logs aggregation as follows:

  * If a connection event occurs and subsequent data packets for the same 5-tuple are captured by the primary packet sampling within the same aggregation interval, VPC Flow Logs merges them into a single log entry.
  * If a connection event occurs but no subsequent data packets are sampled during that aggregation interval, VPC Flow Logs generates a separate log entry for the connection event.
  * The secondary flow log sampling setting applies to log entries for connection events.



You can identify connection events by using the `connection_direction` field. For more information, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

### Dropped traffic

VPC Flow Logs generates log records for dropped traffic. Log records for dropped traffic are generated separately from standard flow log records and records that are generated by TCP connection logging.

For more information, see [Records for dropped traffic](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#packet-drops).

## Specifications

  * VPC Flow Logs introduces no delay or performance penalty when enabled.
  * VPC Flow Logs works with VPC networks, not legacy networks.
  * VPC Flow Logs samples TCP, UDP, ICMP, ESP, GRE, and RDMA flows: 
    * Both inbound and outbound flows are sampled. For RDMA over Converged Ethernet (RoCE), only outbound flows are sampled.
    * Flows can be within Google Cloud or between Google Cloud and other networks.
    * If a flow is captured by sampling, VPC Flow Logs generates a log for the flow. Each flow record includes the information described in the [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format) section.
  * Except for flow log entries that include TCP connection events, flow log entries indicate packet direction, but they don't indicate whether the reporter is the connection initiator.

When TCP connection logging is enabled, flow log entries that include connection events indicate both the packet direction and whether the reporter initiated a connection by sending a `SYN` packet or acknowledged an inbound connection by sending a `SYN-ACK` packet (indicated by the `connection_direction` field).

  * VPC Flow Logs interacts with firewall rules in the following ways:

    * Egress packets are sampled _before_ _egress_ firewall rules. Even if an egress firewall rule denies outbound packets, those packets can be sampled by VPC Flow Logs.
    * Ingress packets are sampled _after_ _ingress_ firewall rules. If an ingress firewall rule denies inbound packets, those packets aren't sampled by VPC Flow Logs.
  * You can use [filters](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) in VPC Flow Logs to generate only certain logs.

  * VPC Flow Logs supports VMs that have multiple network interfaces. In each VPC, you need to enable VPC Flow Logs for each subnet that contains a network interface.

  * To log flows between Pods on the same Google Kubernetes Engine (GKE) node, you must enable [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) for the cluster.

  * VPC Flow Logs isn't supported for subnets with purpose `INTERNAL_HTTPS_LOAD_BALANCER` because these subnets are used as proxy-only subnets and have no VM instances or serverless endpoints.

  * VPC Flow Logs writes logs to the project of the reporting VPC network. For resources in Shared VPC networks, logs are reported in the host project.




## Pricing and billing

VPC Flow Logs pricing is described in [Network Telemetry pricing](https://cloud.google.com/vpc/pricing#network-telemetry).

VPC Flow Logs charges are billed to the Google Cloud project containing the resource that reports flow logs. If VPC Flow Logs is enabled at the organization level, each project is billed separately.

## What's next

  * To learn more about the VPC Flow Logs record format and which metadata annotations are available, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).
  * To see examples of VPC Flow Logs that are collected for various use cases, see [About traffic flows](https://docs.cloud.google.com/vpc/docs/about-traffic-flows).
  * To start reporting flows for a subnet, see [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
