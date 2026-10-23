---
url: https://docs.cloud.google.com/vpc/docs/about-flow-logs-records/
title: About VPC Flow Logs records \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:37.564557+00:00
---

# About VPC Flow Logs records  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-flow-logs-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About VPC Flow Logs records

This page describes the VPC Flow Logs record format, including which base and metadata fields are available. It also explains how you can use log filtering so that only logs that match certain criteria are generated.

## Record format

Log records contain base fields, which are the core fields of every log record, and metadata fields that add additional information. Metadata fields may be omitted to save storage costs.

Some log fields are in a multi-field format, with more than one piece of data in a given field. For example, the `connection` field is of the `IpConnection` format, which contains the source and destination IP address and port, plus the protocol, in a single field. These multi-field fields are described below the record format table.

The values for metadata fields aren't based on the data plane path; they are approximations and might be missing or incorrect. Unlike metadata fields, the values for base fields are taken directly from packet headers.

Field | Field format | Field type: base or optional metadata  
---|---|---  
connection |  IpConnection   
Connection details describing the flow, including the 5-tuple and NAT IP address where applicable  | Base  
reporter |  string   
The side that reported the flow: 

  * For VMs and serverless endpoints, the reporter can be `SRC` or `DEST`.
  * For gateways such as VLAN attachments for Cloud Interconnect and Cloud VPN tunnels, the reporter can be `SRC_GATEWAY` or `DEST_GATEWAY`.

| Base  
connection_direction |  string   
Direction of the TCP connection relative to the reporter. Populated for VMs and serverless endpoints when [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) is enabled and an outbound `SYN` or `SYN-ACK` packet is observed during the aggregation interval. For connections that span multiple aggregation intervals, this field is populated only for the interval where the `SYN` or `SYN-ACK` is captured. Can be one of the following:

  * `EGRESS`: the reporter initiated a TCP connection by sending a `SYN` packet (`reporter` is `SRC`).
  * `INGRESS`: the reporter responded to an inbound `SYN` packet by sending a `SYN-ACK` packet (`reporter` is `DEST`).

| Base  
round_trip_time |  Latencies   
RTT in milliseconds with sub-millisecond precision as measured during the aggregation interval. This field is populated for TCP (for VMs and serverless endpoints) and Falcon traffic: 

  * For TCP traffic, the measured latency is the time elapsed between sending a SEQ and receiving a corresponding ACK.
  * For Falcon traffic, the latency is the hardware-measured RTT.

Not populated:

  * When [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) records a connection event without sampled data packets
  * For dropped traffic (`disposition=DROPPED`)

| Base  
rtt_msec |  int64   
Round-trip time (RTT) in milliseconds as measured during the aggregation interval. This field is populated as follows: 

  * Measured only for TCP traffic
  * Populated for VMs and serverless endpoints
  * Not populated: 
    * For VLAN attachments and Cloud VPN tunnels
    * When [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) records a connection event without sampled data packets
    * For dropped traffic (`disposition=DROPPED`)

The measured RTT is the time elapsed between sending a SEQ and receiving a corresponding ACK. | Base  
bytes_sent |  int64   
Estimated number of user payload bytes sent from the source to the destination.1 For packets with no user payload, the value is zero.2 Not populated for dropped traffic (`disposition=DROPPED`) or when [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) records a connection event without sampled data packets.  | Base  
packets_sent |  int64   
Estimated number of packets sent from the source to the destination.1 Not populated for dropped traffic (`disposition=DROPPED`) or when [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) records a connection event without sampled data packets.  | Base  
start_time |  string   
Timestamp (RFC 3339 date string format) of the first observed packet during the aggregated time interval.  | Base  
end_time |  string   
Timestamp (RFC 3339 date string format) of the last observed packet during the aggregated time interval.  | Base  
disposition |  string   
Populated only for log records that capture packet drops. This field is set to `DROPPED`.  | Base  
drop_reason |  string   
Populated only for log records with `disposition=DROPPED`. For more information, see Packet drop annotations and Packet drop reasons.  | Base  
bytes_dropped |  int64   
Estimated number of user payload bytes dropped from the source to the destination. Populated only for log records with `disposition=DROPPED`.  | Base  
packets_dropped |  int64   
Estimated number of packets dropped from the source to the destination. Populated only for log records with `disposition=DROPPED`.  | Base  
throughput_inclusion |  string   
Populated only for log records with `disposition=DROPPED`. Indicates whether the dropped traffic is included (`INCLUDED`) or excluded (`EXCLUDED`) from the `bytes_sent` and `packets_sent` fields that are reported for the flow by the same reporter.  | Base  
Source and destination metadata fields  
src_gateway |  GatewayDetails   
If the source of the flow is an on-premises or other cloud endpoint that is connected to Google Cloud through a gateway such as a VLAN attachment for Cloud Interconnect or a Cloud VPN tunnel and either of the following conditions is met, this field is populated with gateway details: 

  * The source gateway is the reporter of the flow.
  * The destination of the flow is the reporter, and either of the following is true: 
    * The source gateway is in the same project as the destination of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
dest_gateway |  GatewayDetails   
If the destination of the flow is an on-premises or other cloud endpoint that is connected to Google Cloud through a gateway such as a VLAN attachment for Cloud Interconnect or a Cloud VPN tunnel and either of the following conditions is met, this field is populated with gateway details: 

  * The destination gateway is the reporter of the flow.
  * The source of the flow is the reporter, and either of the following is true: 
    * The destination gateway is in the same project as the source of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
src_gke_details |  GkeDetails   
If the source of the flow is a Google Kubernetes Engine (GKE) endpoint, this field is populated with GKE endpoint details.  | Metadata  
dest_gke_details |  GkeDetails   
If the destination of the flow is a GKE endpoint, this field is populated with GKE endpoint details.  | Metadata  
src_google_service |  GoogleServiceDetails   
If the source of the flow is a Google service, this field is populated with service details.  | Metadata  
dest_google_service |  GoogleServiceDetails   
If the destination of the flow is a Google service, this field is populated with service details.  | Metadata  
src_instance |  InstanceDetails   
If the source of the flow is a VM located in a VPC network and either of the following conditions is met, this field is populated with VM instance details: 

  * The source VM is the reporter of the flow.
  * The destination of the flow is the reporter, and either of the following is true: 
    * The source VM, or the VPC network that the source VM is attached to, is in the same project as the destination of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
dest_instance |  InstanceDetails   
If the destination of the flow is a VM located in a VPC network and either of the following conditions is met, this field is populated with VM instance details. 

  * The destination VM is the reporter of the flow.
  * The source of the flow is the reporter, and either of the following is true: 
    * The destination VM, or the VPC network that the destination VM is attached to, is in the same project as the source of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
src_location |  GeographicDetails   
If the source of the flow is a public IP address outside of the VPC network, this field is populated with available location metadata.  | Metadata  
dest_location |  GeographicDetails   
If the destination of the flow is a public IP address outside of the VPC network, this field is populated with available location metadata.  | Metadata  
src_serverless_details |  ServerlessDetails   
If the source of the flow is a serverless endpoint such as a Cloud Run or App Engine resource configured with Direct VPC egress, this field is populated with serverless metadata.  | Metadata  
dest_serverless_details |  ServerlessDetails   
If the destination of the flow is a serverless endpoint such as a Cloud Run or App Engine resource configured with Direct VPC egress, this field is populated with serverless metadata.  | Metadata  
src_psc_interface |  PrivateServiceConnectInterfaceDetails   
If the source of the flow is a Private Service Connect interface, this field is populated with Private Service Connect interface details and is reported in the consumer project, by both the source and destination.  | Metadata  
dest_psc_interface |  PrivateServiceConnectInterfaceDetails   
If the destination of the flow is a Private Service Connect interface, this field is populated with Private Service Connect interface details and is reported in the consumer project, by both the source and destination.  | Metadata  
src_vpc |  VpcDetails   
If the source of the flow is a VM or serverless endpoint located in a VPC network and either of the following conditions is met, this field is populated with VPC network details: 

  * The source resource is the reporter of the flow.
  * The destination of the flow is the reporter, and either of the following is true: 
    * The source resource, or the VPC network that the source resource is attached to, is in the same project as the destination of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
dest_vpc |  VpcDetails   
If the destination of the flow is a VM or serverless endpoint located in a VPC network and either of the following conditions is met, this field is populated with VPC network details: 

  * The destination resource is the reporter of the flow.
  * The source of the flow is the reporter, and either of the following is true: 
    * The destination resource, or the VPC network that the destination resource is attached to, is in the same project as the source of the flow.
    * VPC Flow Logs is configured at the organization level, and cross-project annotations aren't disabled.3

| Metadata  
Other metadata fields  
internet_routing_details |  InternetRoutingDetails   
If the flow is between Google Cloud and the internet, this field is populated with routing details. Available only for egress flows.  | Metadata  
load_balancing |  LoadBalancingDetails   
If the flow passes through a load balancer in one of the following configurations, this field is populated with Cloud Load Balancing details: 

  * The reporter of the flow is the client of the load balancer, and the load balancer type is `APPLICATION_LOAD_BALANCER`, `PROXY_NETWORK_LOAD_BALANCER`, `PASSTHROUGH_NETWORK_LOAD_BALANCER`, or `PROTOCOL_FORWARDING`.
  * The reporter of the flow is the backend of the load balancer, and the load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER` or `PROTOCOL_FORWARDING`.

| Metadata  
nat_gateway_details |  NatGatewayDetails   
If the reporter of the flow is `SRC` in a subnet where a Cloud NAT gateway performs network address translation, this field is populated with Cloud NAT gateway details.  | Metadata  
network_service |  NetworkServiceDetails   
If the Differentiated Services Code Point (DSCP) header is set, this field is populated with network service details.  | Metadata  
psc |  PrivateServiceConnectDetails   
If the flow is associated with a Private Service Connect connection—including a connection propagated through Network Connectivity Center—and either of the following conditions is met, this field is populated with Private Service Connect details: 

  * The reporter of the flow is a consumer and uses a Private Service Connect endpoint that targets a published service or global Google APIs. 
  * The reporter of the flow is a producer and uses an internal passthrough Network Load Balancer or internal protocol forwarding. 

| Metadata  
rdma_traffic_type |  string   
Type of RDMA traffic. Populated for GPU-to-GPU traffic between VMs. Can be `GPUDirect-TCPXO`, `Falcon`, or `RoCE`.  | Metadata  
  
1 Estimated total based on sampled packets. For best accuracy, aggregate logs across longer time periods or multiple resources. For more information about accuracy and sampling, see [VPC Flow Logs: Understanding byte and packet counts](https://services.google.com/fh/files/misc/vpc_flow_logs_understanding_byte_and_packet_counts.pdf) and [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 

2 For Falcon traffic, the bytes sent value is calculated differently for the source and destination: 

  * If the source VM is the reporter, the reported bytes value is the sum of the user payload bytes and packet header bytes sent. This value is always greater than zero, even for packets containing no user payload.
  * If the destination VM is the reporter, the reported bytes value is the user payload bytes received and forwarded to the application layer. For packets with no user payload, the bytes value is zero.



3 If VPC Flow Logs is configured at the organization level, by default, log records for cross-project flows include details about both sides of the flow. Cross-project annotations are available for flows through Shared VPC, VPC Network Peering, and Network Connectivity Center. For more information, see Cross-project annotations. 

### GatewayDetails field format

Field | Type | Description  
---|---|---  
project_id | string | Google Cloud project ID of the gateway  
location | string | Region of the gateway  
name | string | Name of the gateway  
type | string |  Type of the gateway. Can be `INTERCONNECT_ATTACHMENT` or `VPN_TUNNEL`.   
vpc | VpcDetails |  VPC network details of the gateway   
interconnect_name | string |  If the type of the gateway is `INTERCONNECT_ATTACHMENT`, this field is populated with the name of the Cloud Interconnect connection on which the VLAN attachment is configured.   
interconnect_project_number | int64 |  If the type of the gateway is `INTERCONNECT_ATTACHMENT`, this field is populated with the Google Cloud project number of the Cloud Interconnect connection on which the VLAN attachment is configured.   
  
### GeographicDetails field format

Field | Type | Description  
---|---|---  
asn | int32 |  The ASN of the external network to which this endpoint belongs   
city | string | City for external endpoints  
continent | string | Continent for external endpoints  
country | string |  Country for external endpoints, represented as [ ISO 3166-1 Alpha-3](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country codes   
region | string | Region for external endpoints  
  
### GkeDetails field format

Field | Type | Description  
---|---|---  
cluster |  ClusterDetails | GKE cluster metadata  
pod |  PodDetails |  GKE Pod metadata, populated when the source or destination of the traffic is a Pod   
service |  ServiceDetails |  GKE Service metadata, populated in Service endpoints only. The record contains up to two Services. If there are more than two relevant Services, this field contains a single Service with a special `MANY_SERVICES` marker.   
  
#### ClusterDetails field format

Field | Type | Description  
---|---|---  
cluster_location | string |  Location of the cluster. This can be a zone or a region depending if the cluster is zonal or regional.   
cluster_name | string | GKE cluster name.  
  
#### PodDetails field format

Field | Type | Description  
---|---|---  
pod_name | string | Name of the Pod  
pod_namespace | string | Namespace of the Pod  
workload | WorkloadDetails | Metadata about the top-level workload resource that controls the Pod  
  
##### WorkloadDetails field format

Field | Type | Description  
---|---|---  
workload_name | string | Name of the top-level workload controller  
workload_type | string |  Type of the top-level workload controller. Can be `DEPLOYMENT`, `REPLICA_SET`, `STATEFUL_SET`, `DAEMON_SET`, `JOB`, `CRON_JOB`, or `REPLICATION_CONTROLLER`.   
  
#### ServiceDetails field format

Field | Type | Description  
---|---|---  
service_name | string |  Name of the Service. If there are more than two relevant Services, the field is set to a special `MANY_SERVICES` marker.   
service_namespace | string | Namespace of the Service  
  
Example:

If there are two services, the Service field looks like this:
    
    
    service: [
     0: {
      service_name: "my-lb-service"
      service_namespace: "default"
     }
     1: {
      service_name: "my-lb-service2"
      service_namespace: "default"
     }
    ]
    

If there are more than two services, the Service field looks like this:
    
    
    service: [
     0: {
      service_name: "MANY_SERVICES"
     }
    ]
    

### GoogleServiceDetails field format

Field | Type | Description  
---|---|---  
type | string | Type of service: `GOOGLE_API` or `GOOGLE_VPC_HOSTED_SERVICE`.

  * `GOOGLE_API`: this type is used for the following Google APIs and services: 
    * [Google APIs that are accessed from VMs with external IP addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip)
    * [Google APIs that are accessed through Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) or [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid)
    * [Global Google APIs that are accessed through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints)
  * `GOOGLE_VPC_HOSTED_SERVICE`: this type is used for VPC-hosted services such as the following: 
    * Google services that are accessed through public IP connectivity—for example, [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-ip)
    * [Google services that are published through Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#google-services)
    * [Google services that are published through private services access](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services)

  
service_name | string | Name of the service. For example, `pubsub.googleapis.com`. Limitations:

  * The service name might be missing for requests to Google APIs that take longer than 60 seconds to complete.
  * If a VM or gateway uses the same 5-tuple to connect to multiple services, the log record contains the name of only one of the services, selected randomly.

  
connectivity | string | Access method. For the `GOOGLE_API` type, the connectivity field can be one of the following:

  * `PUBLIC_IP`, if the API is accessed from a VM with an external IP address
  * `PRIVATE_GOOGLE_ACCESS` or `DIRECT_CONNECTIVITY`, if the API is accessed through Private Google Access
  * `PRIVATE_SERVICE_CONNECT_FOR_GOOGLE_APIS`, if the API is accessed through Private Service Connect endpoints

For the `GOOGLE_VPC_HOSTED_SERVICE` type, the connectivity field can be one of the following:

  * `PUBLIC_IP`, if the service is accessed through public IP connectivity
  * `PRIVATE_SERVICES_ACCESS`, if the service is accessed through private services access
  * `PRIVATE_SERVICE_CONNECT_ENDPOINT` or `PRIVATE_SERVICE_CONNECT_INTERFACE`, if the service is accessed through Private Service Connect

  
private_domain | string | Private domain or Private Service Connect API bundle. The private_domain field can be one of the following:

  * For the `PRIVATE_GOOGLE_ACCESS` access method: `private.googleapis.com` or `restricted.googleapis.com`
  * For the `DIRECT_CONNECTIVITY` access method: `restricted.googleapis.com`
  * For the `PRIVATE_SERVICE_CONNECT_FOR_GOOGLE_APIS` access method: `all-apis` or `vpc-sc`

  
  
### InstanceDetails field format

Field | Type | Description  
---|---|---  
project_id | string | ID of the Google Cloud project that contains the VM resource  
region | string | Region of the VM  
vm_name | string | Instance name of the VM  
zone | string | Zone of the VM  
managed_instance_group | InstanceGroupDetails |  If the VM is part of a managed instance group, this field is populated with instance group details.   
  
#### InstanceGroupDetails field format

Field | Type | Description  
---|---|---  
name | string | Name of the instance group  
region | string | If the instance group is regional, this field is populated with the region of the instance group.  
zone | string | If the instance group is zonal, this field is populated with the zone of the instance group.  
  
### InternetRoutingDetails field format

Field | Type | Description  
---|---|---  
egress_as_path | AsPath | List of relevant AS paths. If there are multiple AS paths available to the flow, the field might contain more than one AS path.  
  
#### AsPath field format

Field | Type | Description  
---|---|---  
as_details | AsDetails | List of AS details for all systems in the AS path. The list starts from the first AS that is external to Google Cloud's network and ends with the AS to which the remote IP address belongs.  
  
#### AsDetails field format

Field | Type | Description  
---|---|---  
asn | uint32 | The autonomous system number (ASN) of the AS  
  
### IpConnection field format

Field | Type | Description  
---|---|---  
src_ip | string | Source IP address. Populated for all flows.  
dest_ip | string | Destination IP address. Populated for all flows.  
src_port | int32 | Source port: 

  * Populated for TCP and UDP flows
  * Not populated for ICMP, ESP, GRE, and RDMA flows

  
dest_port | int32 | Destination port: 

  * Populated for TCP and UDP flows
  * Not populated for ICMP, ESP, GRE, and RDMA flows

  
nat_ip | string | IP address used by the Cloud NAT gateway (if configured). Populated only if the reporter is `SRC`.  
nat_port | int32 | Port assigned by the Cloud NAT gateway (if configured). Populated only if the reporter is `SRC`.  
protocol | int32 | The IANA protocol number: 

  * Populated for TCP, UDP, ICMP, ESP, and GRE flows
  * Not populated for RDMA flows

  
  
### Latencies field format

Field | Type | Description  
---|---|---  
median_msec | double | The median latency in milliseconds as measured during the aggregation interval.  
  
### LoadBalancingDetails field format

Field | Type | Description  
---|---|---  
forwarding_rule_project_id | string | Google Cloud project ID of the forwarding rule  
reporter | string | Cloud Load Balancing reporter. Can be either `CLIENT` or `BACKEND`. 

  * If the reporter of the flow is the client of the load balancer, this field is set to `CLIENT`.
  * If the reporter of the flow is the backend of the load balancer, this field is set to `BACKEND`.

  
type | string | Load balancer type. Can be `APPLICATION_LOAD_BALANCER`, `PROXY_NETWORK_LOAD_BALANCER`, `PASSTHROUGH_NETWORK_LOAD_BALANCER`, or `PROTOCOL_FORWARDING`.  
scheme | string | Load balancer scheme. Can be `EXTERNAL_MANAGED`, `INTERNAL_MANAGED`, `EXTERNAL`, `INTERNAL`, or `INTERNAL_SELF_MANAGED`.  
url_map_name | string | Name of the URL map. Populated if the type of the load balancer is `APPLICATION_LOAD_BALANCER`.  
forwarding_rule_name | string | Name of the forwarding rule  
backend_service_name | string | Name of the backend service. Populated if the reporter is `BACKEND` and load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER`. If the backend group type is `TARGET_POOL`, this field isn't populated.  
backend_service_project_id | string | Project ID of the backend service. Populated if the reporter is `BACKEND` and the load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER`. If the backend group type is `TARGET_POOL`, this field isn't populated.  
backend_group_name | string | Name of the backend group. Populated if the reporter is `BACKEND` and load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER`.  
backend_group_type | string | Type of the backend group. Can be `INSTANCE_GROUP`, `NETWORK_ENDPOINT_GROUP`, or `TARGET_POOL`. Populated if the reporter is `BACKEND` and the load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER`.  
backend_group_location | string | Location of the backend group. Can be a zone or a region depending on whether the scope of the backend group is zonal or regional. Populated if the reporter is `BACKEND` and the load balancer type is `PASSTHROUGH_NETWORK_LOAD_BALANCER`. If the backend group type is `TARGET_POOL`, this field isn't populated.  
vpc | VpcDetails |  VPC network details of the load balancer   
  
### NatGatewayDetails field format

Field | Type | Description  
---|---|---  
gateway_name | string | Name of the Cloud NAT gateway  
router_name | string | Name of the Cloud Router that is associated with the Cloud NAT gateway  
project_id | string | Google Cloud project ID of the Cloud NAT gateway and Cloud Router  
region | string | Region of the Cloud NAT gateway and Cloud Router  
type | string | Type of Cloud NAT: `PUBLIC` or `PRIVATE`  
  
### NetworkServiceDetails field format

Field | Type | Description  
---|---|---  
dscp | int32 | If the Differentiated Services field is present in packet headers, this field is populated with the DSCP value.  
  
### Packet drop reasons

The following table describes the supported values of the `drop_reason` field when reported by `SRC` or `SRC_GATEWAY`.

Drop reason | Description  
---|---  
`FIREWALL_DENY` | Outbound traffic was dropped because an egress firewall rule was evaluated and its action was `deny`.  **Recommendation** : If you want to allow this traffic, adjust your firewall rules.   
`NAT_ENDPOINT_INDEPENDENT_CONFLICT` | Outbound traffic was dropped because an endpoint-independent mapping conflict occurred. **Recommendation:** Review the following Cloud NAT documentation:

  * [Simultaneous port reuse and endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-reuse-endpoints)
  * [Packets dropped with reason: endpoint independence conflict](https://docs.cloud.google.com/nat/docs/troubleshooting#endpoint-independent-conflict)

  
`NAT_OUT_OF_CONNECTIONS` | Outbound traffic was dropped because the NAT connection tracking table reached its maximum capacity. **Recommendation** : Review [NAT connection limits per VM](https://docs.cloud.google.com/nat/quota#considerations) and [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).   
`NAT_OUT_OF_PORTS` | Outbound traffic was dropped because the Cloud NAT gateway ran out of NAT 2-tuples (ports) to assign to VMs. Consequently, the VM network interface was unable to send packets using the gateway.  **Recommendation** : Make sure that your NAT IP address and ports-per-VM allocations are sufficient. For more information, see [IP addresses and ports](https://docs.cloud.google.com/nat/docs/ports-and-addresses).  
`NO_MATCHING_ROUTE` | Outbound traffic was dropped because there was no matching route for the destination. **Recommendation** : Review routes in your VPC network by [using the Effective Routes section](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) of the Google Cloud console. You can also create and run [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).   
`QUEUE_OVERFLOW` | Outbound traffic was dropped because the host's packet processing software exceeded its CPU capacity. **Recommendation** : If drops are persistent, consider using VMs with [higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) (Tier_1) or spreading traffic across more VMs.  
`SPOOFED_SOURCE` | Outbound traffic was dropped because the packet's source wasn't associated with the VM network interface and IP forwarding is turned off.  **Recommendation** : To send packets with arbitrary sources from a VM network interface to destinations routable within a VPC network, you must [enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) for the VM.   
`TOO_MANY_CONNECTIONS` | Outbound traffic was dropped because the host's packet processing software couldn't accommodate the flow rate. **Recommendation** : Consider using a different machine series designed for larger numbers of connections or distributing your workload across more VMs.  
  
The following table describes the supported values of the `drop_reason` field when reported by `DEST` or `DEST_GATEWAY`.

Drop reason | Description  
---|---  
`EARLY_DROPS_FULL_FAIR_QUEUE` | Inbound traffic was dropped because the host's packet processing software enforced resource fairness. This behavior typically affects only the 1st generation [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology).  **Recommendation** : If drops are persistent, consider migrating to a newer or more performant machine series.  
`FIREWALL_DENY` | Inbound traffic was dropped because an ingress firewall rule was evaluated and its action was `deny`.  **Recommendation** : If you want to allow this traffic, adjust your firewall rules.  
`INVALID_L4_CHECKSUM_INTERNET` | Inbound traffic was dropped because a checksum mismatch was detected. The packets were sent from a source outside of the VPC network to a destination external IP address that is associated with the VM reporter. For more information, see [Ingress to destinations outside of a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-in-dest-e). **Recommendation** : If drops are persistent, investigate the health of the source or network path.  
`INVALID_L4_CHECKSUM_INTERNAL` | Inbound traffic was dropped because a checksum mismatch was detected. The packets were routed within the VPC network to a destination IP address associated with the VM reporter. For more information, see [Ingress to destinations routable within a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-in-dest-i). **Recommendation** : If drops are persistent, investigate the health of the source or network path.  
`PSC_NAT_OUT_OF_CONNECTIONS` | Inbound traffic was dropped because the Private Service Connect endpoint reached the [maximum number of simultaneous connections for the consumer](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections). **Recommendation** : Ask the consumer to reduce the rate of new connections to this Private Service Connect endpoint or ask the consumer to distribute connections to this Private Service Connect endpoint by using more client VMs.   
`PSC_NAT_OUT_OF_PORTS` | Inbound traffic from a Private Service Connect consumer was dropped because Private Service Connect NAT port exhaustion occurred. **Recommendation** : Review your [NAT subnet sizing](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets).  
`QUEUE_OVERFLOW` | Inbound traffic was dropped because the host's packet processing software exceeded its CPU capacity. **Recommendation** : If drops are persistent, consider using VMs with [higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) (Tier_1) or spreading traffic across more VMs.  
`TOO_MANY_CONNECTIONS` | Inbound traffic was dropped because the host's packet processing software couldn't accommodate the flow rate. **Recommendation** : If the high flow rate is due to high connection concurrency or turnover at the VM level, consider reducing the rate of new connections to the VM.  
  
### PrivateServiceConnectDetails field format

Field | Type | Description  
---|---|---  
reporter | string | Private Service Connect reporter. Can be either `CONSUMER` or `PRODUCER`.  
consumer_connection | IpConnection |  The pre-NAT 5-tuple that describes the flow from the consumer's perspective. Populated if the reporter is `PRODUCER`.   
psc_endpoint | PrivateServiceConnectEndpointDetails |  Consumer endpoint details   
psc_attachment | PrivateServiceConnectAttachmentDetails |  Producer service attachment details   
  
#### PrivateServiceConnectEndpointDetails field format

Field | Type | Description  
---|---|---  
name | string |  Name of the Private Service Connect endpoint. Populated only if `target_service_type` is `PUBLISHED_SERVICE`.   
project_id | string | Google Cloud project ID of the endpoint.  
region | string | Region of the endpoint. Not populated if the target service type is `GLOBAL_GOOGLE_APIS`.  
psc_connection_id | string | Private Service Connect connection ID  
target_service_type | string | Target service type. Can be either `GLOBAL_GOOGLE_APIS` or `PUBLISHED_SERVICE`.  
vpc | VpcDetails |  VPC network details of the endpoint. If the reporter is `PRODUCER`, the `subnetwork_name` and `subnetwork_region` fields aren't populated.   
  
#### PrivateServiceConnectAttachmentDetails field format

Field | Type | Description  
---|---|---  
name | string |  Name of the service attachment   
project_id | string | Google Cloud project ID of the service attachment  
region | string | Region of the service attachment  
vpc | VpcDetails |  VPC network details of the service attachment   
  
### PrivateServiceConnectInterfaceDetails field format

Field | Type | Description  
---|---|---  
network_attachment | NetworkAttachmentDetails | Metadata for the consumer's network attachment  
producer | ProducerDetails |  Metadata for the producer that initiated the connection   
  
#### NetworkAttachmentDetails field format

Field | Type | Description  
---|---|---  
name | string | Name of the network attachment  
project_id | string | Google Cloud project ID of the network attachment  
region | string | Region of the network attachment  
  
#### ProducerDetails field format

Field | Type | Description  
---|---|---  
project_id | string |  Google Cloud project ID of the producer. Populated only if the `service_class_id` field isn't available.   
region | string | Region of the producer VM  
service_class_id | string | ID of the producer's service class (if available)  
zone | string | Zone of the producer VM  
  
### ServerlessDetails field format

Field | Type | Description  
---|---|---  
project_id | string | ID of the Google Cloud project that contains the Cloud Run or App Engine resource. In a Shared VPC configuration, the project ID is usually the ID of the service project.  
region | string | Region of the Cloud Run or App Engine resource  
One of the following:

  * cloud_run_service_details
  * cloud_run_job_details
  * cloud_run_worker_pool_details
  * app_engine_service_details

| One of the following:

  * CloudRunServiceDetails
  * CloudRunJobDetails
  * CloudRunWorkerPoolDetails
  * AppEngineServiceDetails

| Name of the Cloud Run or App Engine resource  
  
#### CloudRunServiceDetails field format

Field | Type | Description  
---|---|---  
service_name | string | Name of the Cloud Run service  
  
#### CloudRunJobDetails field format

Field | Type | Description  
---|---|---  
job_name | string | Name of the Cloud Run job  
  
#### CloudRunWorkerPoolDetails field format

Field | Type | Description  
---|---|---  
worker_pool_name | string | Name of the Cloud Run worker pool  
  
#### AppEngineServiceDetails field format

Field | Type | Description  
---|---|---  
service_name | string | Name of the App Engine service  
  
### VpcDetails field format

Field | Type | Description  
---|---|---  
project_id | string | ID of the Google Cloud project that contains the VPC. In a Shared VPC configuration, the project ID is the ID of the host project.  
subnetwork_name | string |  Name of the subnet, if applicable   
subnetwork_region | string | Region of the subnet, if applicable  
vpc_name | string | Name of the network  
  
## Metadata annotations

Log records contain base fields and metadata fields. The Record format section lists which fields are type metadata and which are type base. All base fields are always included. You can customize which metadata fields you keep.

  * If you select all metadata, all metadata fields in the VPC Flow Logs record format are included in the flow logs. When new metadata fields are added to the record format, the flow logs automatically include the new fields.

  * If you select no metadata, this omits all metadata fields.

  * If you select custom metadata, you can specify the metadata fields that you want to include by the parent field, such as `src_vpc`, or by their full names, such as `src_vpc.project_id`

When new metadata fields are added to the record format, they're excluded from the flow logs unless they're within a parent field that you have specified to include.

    * If you specify custom metadata using parent fields, when new metadata fields are added to the record format within that parent field, the flow logs will automatically include the new fields.

    * If you specify custom metadata using the full name of the field, new metadata fields that are added to the parent field are excluded from the flow logs.




For information about how to customize metadata fields, see [Enable VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs) or [Update VPC Flow Logs configuration](https://docs.cloud.google.com/vpc/docs/using-flow-logs#update-flow-logs).

### Cross-project annotations

If VPC Flow Logs is [enabled at the organization level](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization), flows through Shared VPC, VPC Network Peering, and Network Connectivity Center are annotated with cross-project annotations. Cross-project annotations are enabled by default. You can optionally disable these annotations.

  * If cross-project annotations are enabled, log records for flows between resources in different projects [include information about both sides of the flow](https://docs.cloud.google.com/vpc/docs/about-traffic-flows#cross-project-logging).
  * If cross-project annotations are disabled, log records include information only about the reporter of the flow.



If VPC Flow Logs is enabled at the project level, flows between resources in different projects aren't annotated with cross-project annotations.

### GKE annotations

Flows that have an endpoint in a GKE Cluster can be annotated with GKE metadata annotations, which can include details of the Cluster, Pod, and Service of the endpoint.

#### GKE Service annotations

Traffic sent to a ClusterIP, NodePort, or LoadBalancer can receive Service annotations. If sent to a NodePort or LoadBalancer, the flow receives the Service annotation on both hops of the connection.

Traffic sent directly to a Pod's Service port is annotated with a Service annotation on the destination endpoint.

Traffic sent to a Pod's Service port where the Pod is backing more than one Service on the same Service port is annotated with multiple Services on the destination endpoint. This is limited to two Services. If there are more than that, the endpoint will be annotated with a special `MANY_SERVICES` marker.

#### Pod annotations on internet traffic

Traffic between a Pod and the internet doesn't receive Pod annotations by default. VPC Flow Logs can't add Pod annotations because, for packets to the internet, the masquerade agent translates the Pod IP address to the node IP address before VPC Flow Logs sees the packet.

Because of the masquerade, Pod annotations are only visible if the destinations are within either [the default non-masquerade destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests) or in a [custom `nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#specify-non-masq-cidrs). If you include internet destinations in a custom `nonMasqueradeCIDRs` list, you need to provide a way for the internal Pod IP addresses to be translated before they are delivered to the internet. For both private and non-private clusters, you can use Cloud NAT. See [GKE interaction](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE) for more details.

## Records for dropped traffic

VPC Flow Logs generates log records for dropped traffic. Log records for dropped traffic are generated separately from standard log records. Packet drops are aggregated by flow and drop reason. Within an aggregation interval, packet drops with the same reason are consolidated into a single log record; separate log records are generated for each unique drop reason.

Egress drops are reported by the source (`SRC` or `SRC_GATEWAY`), and ingress drops are reported by the destination (`DEST` or `DEST_GATEWAY`). When VPC Flow Logs is enabled for both the source and destination, the following behavior applies:

  * **Egress drops**. If a drop occurs on the source side, both a standard log record and a log record that includes the drop reason are generated for the source. No log record is generated for the destination because the traffic was never delivered to the destination.
  * **Ingress drops**. If a drop occurs on the destination side, log records are generated for both the source and destination. For the source, VPC Flow Logs generates a standard log record, and for the destination, it generates only a log record that includes the drop reason.



Log records for dropped traffic include the `disposition`, `drop_reason`, `bytes_dropped`, `packets_dropped`, and `throughput_inclusion` fields.

For a list of tracked packet drop reasons, see Packet drop reasons.

## Log filtering

When you enable VPC Flow Logs, you can set a filter based on both base and metadata fields that only preserves logs that match the filter. All other logs are discarded before being written to Logging.

You can filter on any subset of fields listed in Record format, except for the following fields:

  * `rtt_msec`
  * `bytes_sent`
  * `packets_sent`
  * `start_time`
  * `end_time`
  * `bytes_dropped`
  * `packets_dropped`
  * `throughput_inclusion`



VPC Flow Logs filtering uses CEL, an embedded expression language for attribute-based logic expressions. Filter expressions for VPC Flow Logs have a limit of 2,048 characters. For more information, see Supported CEL logic operators.

For more information about CEL, see the [CEL introduction](https://github.com/google/cel-spec/blob/master/doc/intro.md) and the [language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md). The generation filter feature supports a limited subset of CEL syntax.

To create a VPC Flow Logs configuration that uses log filtering, see [Enable VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs). To configure log filtering for an existing VPC Flow Logs configuration, see [Update VPC Flow Logs configuration](https://docs.cloud.google.com/vpc/docs/using-flow-logs#update-flow-logs). For examples of log filters, see [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples).

### Supported CEL logic operators

Expression | Supported types | Description  
---|---|---  
true, false | boolean | Boolean constants  
x == y x != y | boolean, int, string | Comparison operators Example: connection.protocol == 6  
x && y x || y | boolean | Boolean logic operators Example: connection.protocol == 6 && src_instance.vm_name == "vm_1"  
!x | boolean | Negation  
1, 2.0, 0, ... | int | Constant numeric literals  
x + y | string | String concatenation  
"foo", 'foo', ... | string | Constant string literal  
x.lower() | string | Returns the lowercase value of the string  
x.upper() | string | Returns the uppercase value of the string  
x.contains(y) | string | Returns true if the string contains the specified substring  
x.startsWith(y) | string | Returns true if the string begins with the specified substring  
x.endsWith(y) | string | Returns true if the string ends with the specified substring  
inIpRange(X, Y) | string | Returns true if X is an IP and Y is an IP range that contains X Example: inIpRange("1.2.3.1", "1.2.3.0/24")  
x.containsFieldValue(y) |  x: list   
y: map(string, string)  | Returns true if the list contains an object with fields that match the specified key-value pairs Example: dest_gke_details.service.containsFieldValue({'service_name': 'service1', 'service_namespace': 'namespace1'})  
has(x) |  string  | Returns true if the field is present.  
  
## App Hub labels

For Google Cloud resources that are registered as [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) workloads or services, log records contain [application-specific labels](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-labels#log_labels). VPC Flow Logs includes these labels for traffic that is associated with the following resources:

  * Compute Engine managed instance groups
  * GKE Pods (the `CRON_JOB`, `DAEMON_SET`, `DEPLOYMENT`, and `STATEFUL_SET` workload types)
  * Cloud Run services and jobs configured with Direct VPC egress
  * Forwarding rules



App Hub labels are attached for at most one source resource and one destination resource per log record, where applicable. For forwarding rules, the `CLIENT` and `BACKEND` fields determine whether the forwarding rule is the source or the destination resource.

App Hub labels are distinct from VPC Flow Logs metadata annotations; VPC Flow Logs metadata and log filtering settings aren't applicable to these labels.

## What's next

  * [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs)
  * [Access flow logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
