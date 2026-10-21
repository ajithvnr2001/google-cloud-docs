---
url: https://docs.cloud.google.com/vpc/docs/about-traffic-flows/
title: About traffic flows \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:12.334832+00:00
---

# About traffic flows  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-traffic-flows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About traffic flows

This page describes how VPC Flow Logs reports logs for common traffic flows. See the following sections for examples:

  * VM flows, GKE flows, Serverless flows, and Hybrid connectivity flows describe flows within Google Cloud and flows between Google Cloud and resources outside of Google Cloud. Examples for flows between different Google Cloud projects assume VPC Flow Logs is configured at the project level.
  * Flows between VPC networks in different projects describes how cross-project flows are annotated when VPC Flow Logs is configured at the organization level.



## VM flows

The following sections provide examples of how VPC Flow Logs annotates traffic flows from and to virtual machine (VM) instances.

### VM-to-VM flows in the same VPC network

[ ![VM flows within a VPC network.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-1.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-1.svg) VM flows within a VPC network (click to enlarge).

For VM-to-VM flows in the same VPC network, flow logs are reported from both requesting and responding VMs, as long as both VMs are in subnets that have VPC Flow Logs enabled. In this example, VM `10.10.0.2` sends a request with 1,224 bytes to VM `10.50.0.2`, which is also in a subnet that has logging enabled. In turn, `10.50.0.2` responds to the request with a reply containing 5,342 bytes. Both the request and reply are recorded from both the requesting and responding VMs.

As reported by requesting VM (10.10.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.50.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.50.0.2 | 10.10.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
As reported by responding VM (10.50.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.50.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.50.0.2 | 10.10.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
  
### VM-to-external IP address flows

[ ![VM-to-external IP address flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/vms-to-internet-flows.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/vms-to-internet-flows.svg) VM-to-external IP address flows (click to enlarge).

For flows that traverse the internet between a VM that's in a VPC network and an endpoint with an external IP address, flow logs are reported from the VM that's in the VPC network only:

  * For egress flows, the logs are reported from the VPC network VM that is the source of the traffic.
  * For ingress flows, the logs are reported from the VPC network VM that is the destination of the traffic.



In this example, VM `10.10.0.2` exchanges packets over the internet with an endpoint that has the external IP address `203.0.113.5`. The outbound traffic of 1,224 bytes sent from `10.10.0.2` to `203.0.113.5` is reported from the source VM, `10.10.0.2`. The inbound traffic of 5,342 bytes sent from `203.0.113.5` to `10.10.0.2` is reported from the destination of the traffic, VM `10.10.0.2`.

request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
---|---|---|---|---  
request | 10.10.0.2 | 203.0.113.5 | 1,224 |  src_instance.*  
src_vpc.*  
dest_location.*  
internet_routing_details.*   
reply | 203.0.113.5 | 10.10.0.2 | 5,342 |  src_location.*  
dest_instance.*  
dest_vpc.*   
  
### VM-to-VM flows for Shared VPC

[ ![Shared VPC flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-3.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-3.svg) Shared VPC flows (click to enlarge).

For VM-to-VM flows for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you can enable VPC Flow Logs for the subnet in the host project. For example, subnet `10.10.0.0/20` belongs to a Shared VPC network defined in a host project. You can see flow logs from VMs belonging to this subnet, including ones created by service projects. In this example, the service projects are called "web server", "recommendation", "database".

For VM-to-VM flows, if both VMs are in the same project, or in the case of a shared network, the same host project, annotations for project ID and the like are provided for the other endpoint in the connection. If the other VM is in a different project, then annotations for the other VM are not provided.

The following table shows a flow as reported by either `10.10.0.10` or `10.10.0.20`.

  * `src_vpc.project_id` and `dest_vpc.project_id` are for the host project because the VPC subnet belongs to the host project.
  * `src_instance.project_id` and `dest_instance.project_id` are for the service projects because the instances belong to the service projects.

connection  
.src_ip  |  src_instance  
.project_id  |  src_vpc  
.project_id  |  connection  
.dest_ip  |  dest_instance  
.project_id  |  dest_vpc  
.project_id   
---|---|---|---|---|---  
10.10.0.10 | web server | host_project | 10.10.0.20 | recommendation | host_project  
  
Service projects don't own the Shared VPC network and don't have access to the flow logs of the Shared VPC network.

### VM-to-VM flows for VPC Network Peering

[ ![VPC Network Peering flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-4.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-4.svg) VPC Network Peering flows (click to enlarge).

Unless both VMs are in the same Google Cloud project, VM-to-VM flows for [peered VPC networks](https://docs.cloud.google.com/vpc/docs/vpc-peering) are reported in the same way as for external endpoints—project and other annotation information for the other VM are not provided. If both VMs are in the same project, even if in different networks, then project and other annotation information is provided for the other VM as well.

In this example, the subnets of VM `10.10.0.2` in project analytics-prod and VM `10.50.0.2` in project webserver-test are connected through VPC Network Peering. If VPC Flow Logs is enabled in project analytics-prod, the traffic (1,224 bytes) sent from `10.10.0.2` to `10.50.0.2` is reported from VM `10.10.0.2`, which is the source of the flow. The traffic (5,342 bytes) sent from `10.50.0.2` to `10.10.0.2` is also reported from VM `10.10.0.2`, which is the destination of the flow.

In this example, VPC Flow Logs is not turned on in project webserver-test, so no logs are recorded by VM `10.50.0.2`.

reporter | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
---|---|---|---|---  
source | 10.10.0.2 | 10.50.0.2 | 1,224 |  src_instance.*  
src_vpc.*   
destination | 10.50.0.2 | 10.10.0.2 | 5,342 |  dest_instance.*  
dest_vpc.*   
  
### VM flows through Private Service Connect

For network configurations with Private Service Connect, VPC Flow Logs annotates the following flows:

  * Flows between Private Service Connect consumers (through [endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints)) and published services
  * Flows from and to Private Service Connect [interfaces](https://docs.cloud.google.com/vpc/docs/private-service-connect#interfaces)



The following example describes how VPC Flow Logs annotates log records for flows between Private Service Connect consumers and published services.

[ ![VM flows through Private Service Connect.](https://docs.cloud.google.com/static/vpc/images/flow-logs/psc-consumer-to-producer.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/psc-consumer-to-producer.svg) Flows between consumer and producer VMs (click to enlarge).

Traffic flows to Private Service Connect published services are reported from both consumer and producer VMs as long as both VMs are in subnets that have VPC Flow Logs enabled.

In this example, the consumer VM, `10.10.0.2`, sends a request with 1,224 bytes to the Private Service Connect endpoint, `10.10.0.3`. In the producer VPC network, the source IP address of the request is translated to an IP address in the service attachment subnet, which, in this example, is `10.40.0.2`. The destination IP address of the request is translated to the IP address of the internal passthrough Network Load Balancer, `10.50.0.3`. The request then reaches the backend VM, `10.50.0.2`. In turn, `10.50.0.2` responds to the request with a reply containing 5,342 bytes.

Both the request and the reply are recorded from both the requesting and responding VMs. The log records from the consumer VM are available in the consumer project, and the log records from the producer VM are available in the producer project.

As reported by consumer VM (10.10.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.10.0.3 | 1,224 |  src_instance.*  
src_vpc.*  
psc.reporter  
psc.psc_endpoint.*  
psc.psc_attachment.*   
reply | 10.10.0.3 | 10.10.0.2 | 5,342 |  dest_instance.*  
dest_vpc.*  
psc.reporter  
psc.psc_endpoint.*  
psc.psc_attachment.*   
As reported by producer VM (10.50.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.40.0.2 | 10.50.0.3 | 1,224 |  dest_instance.*  
dest_vpc.*  
psc.reporter  
psc.consumer_connection.*  
psc.psc_endpoint.*  
psc.psc_attachment.*   
reply | 10.50.0.3 | 10.40.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
psc.reporter  
psc.consumer_connection.*  
psc.psc_endpoint.*  
psc.psc_attachment.*   
  
### VM-to-Google API flows

For VM traffic to Google APIs through the VM's external IP address, Private Google Access, or a Private Service Connect endpoint, VPC Flow Logs annotates log records with Google API information.

The following example describes how VPC Flow Logs annotates log records for a VM accessing a global Google API through a Private Service Connect endpoint.

[ ![VM flows to Google APIs through Private Service Connect.](https://docs.cloud.google.com/static/vpc/images/flow-logs/vm-psc-to-google-api.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/vm-psc-to-google-api.svg) VM flows to Google APIs through Private Service Connect (click to enlarge).

Traffic flows to a Google API are reported by consumer VMs, as long as the VM is in a subnet that has VPC Flow Logs enabled. In this example, the consumer VM, `10.10.0.2`, sends a request with 1,224 bytes to the Private Service Connect endpoint, `10.10.110.10`. The request is forwarded to the appropriate Google service, for example, Cloud Storage. In turn, Cloud Storage responds to the request with a reply containing 5,342 bytes. Both the request and the reply are recorded from the requesting VM.

As reported by consumer VM (10.10.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.10.110.10 | 1,224 |  src_instance.*  
src_vpc.*  
dest_google_service.*  
psc.reporter  
psc.psc_endpoint.*  
  
reply | 10.10.110.10 | 10.10.0.2 | 5,342 |  src_google_service.*  
dest_instance.*  
dest_vpc.*  
psc.reporter  
psc.psc_endpoint.*   
  
### VM flows through Cloud Load Balancing

VPC Flow Logs annotates traffic sent through a passthrough Network Load Balancer, proxy Network Load Balancer, or an Application Load Balancer. The following examples assume that these load balancers are configured as internal load balancers.

#### VM-to-VM flows through an internal passthrough Network Load Balancer

[ ![Internal passthrough Network Load Balancer flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-5.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-5.svg) Internal passthrough Network Load Balancer flows (click to enlarge).

When you add a VM to the backend service for an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal), Google Cloud adds the IP address of the load balancer to the local routing table of the VM. This allows the VM to accept request packets with destinations set to the IP address of the load balancer. When the VM replies, it sends its response directly; however, the source IP address for the response packets is set to the IP address of the load balancer, not the VM being load balanced.

VM-to-VM flows sent through an internal passthrough Network Load Balancer are reported from both source and destination.

As reported by client VM (192.168.1.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 192.168.1.2 | 10.240.0.200 | 1,224 |  src_instance.*  
src_vpc.*  
load_balancing.forwarding_rule_project_id  
load_balancing.reporter  
load_balancing.type  
load_balancing.scheme  
load_balancing.forwarding_rule_name  
load_balancing.backend_service_name  
load_balancing.vpc.*   
reply | 10.240.0.200 | 192.168.1.2 | 5,342 |  dest_instance.*  
dest_vpc.*  
load_balancing.forwarding_rule_project_id  
load_balancing.reporter  
load_balancing.type  
load_balancing.scheme  
load_balancing.forwarding_rule_name  
load_balancing.backend_service_name  
load_balancing.vpc.*   
As reported by backend VM (10.240.0.3)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 192.168.1.2 | 10.240.0.200 | 1,224 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*  
load_balancing.* (all fields except url_map_name)   
reply | 10.240.0.200 | 192.168.1.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*  
load_balancing.* (all fields except url_map_name)   
  
In the request that the load balancer distributes to the backend VM, the source IP address is set to the IP address of the client VM. This means that the backend VM can supply `src_instance` and `dest_instance` information about the client VM. However, unlike the backend VM, the client VM can't add `src_instance` and `dest_instance` information about the backend VM to its report because it sends the request to and receives the response from the IP address of the load balancer, not the backend VM.

#### VM flows through an internal proxy Network Load Balancer or internal Application Load Balancer

Traffic flows through an [internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) or [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) are reported by client VMs, as long as the client VM is in a subnet that has VPC Flow Logs enabled. For example, a client VM with the IP address `10.10.0.2` sends a request with 1,224 bytes to the load balancer endpoint, `10.10.0.3`. The request then reaches a backend. In turn, the backend responds to the request with a reply containing 5,342 bytes. Both the request and the reply are recorded on the client VM. The logs from the client VM are available in the Google Cloud project that the VM belongs to.

As reported by client VM (10.10.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.10.0.3 | 1,224 |  src_instance.*  
src_vpc.*  
load_balancing.forwarding_rule_project_id  
load_balancing.reporter  
load_balancing.type  
load_balancing.scheme  
load_balancing.url_map_name (for Application Load Balancer)  
load_balancing.forwarding_rule_name  
load_balancing.vpc.*   
reply | 10.10.0.3 | 10.10.0.2 | 5,342 |  dest_instance.*  
dest_vpc.*  
load_balancing.forwarding_rule_project_id  
load_balancing.reporter  
load_balancing.type  
load_balancing.scheme  
load_balancing.url_map_name (for Application Load Balancer)  
load_balancing.forwarding_rule_name  
load_balancing.vpc.*   
  
## GKE flows

The following sections provide examples of how VPC Flow Logs annotates GKE traffic from and to Pods.

### Pod to ClusterIP flow

[ ![Pod to cluster IP flow.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-6.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-6.svg) Pod to cluster IP flow (click to enlarge).

In this example, traffic is sent from client Pod (`10.4.0.2`) to `cluster-service` (`10.0.32.2:80`). The destination is resolved to the selected server Pod IP address (`10.4.0.3`) on the target port (`8080`).

On node edges, the flow is sampled twice with the translated IP address and port. For both sampling points, we will identify that the destination Pod is backing service `cluster-service` on port `8080`, and annotate the record with the Service details as well as the Pod details. In case the traffic is routed to a Pod on the same node, the traffic doesn't leave the node and is not sampled at all.

In this example, the following records are found.

reporter | connection.src_ip | connection.dst_ip | bytes_sent | Annotations  
---|---|---|---|---  
SRC | 10.4.0.2 | 10.4.0.3 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
src_gke_details.pod.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
DEST | 10.4.0.2 | 10.4.0.3 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
src_gke_details.pod.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
  
### GKE external LoadBalancer flows

[ ![External load balancer flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-7.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-7.svg) External load balancer flows (click to enlarge).

Traffic from an external IP address to a GKE service (`35.35.35.35`) is routed to a node in the cluster—`10.0.12.2` in this example—for routing. By default, regional external passthrough Network Load Balancers distribute traffic across all nodes in the cluster, even those not running a relevant Pod. Traffic might take extra hops to get to the relevant Pod. For more information, see [Networking outside the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#outside-cluster).

The traffic is then routed from the node (`10.0.12.2`) to the selected server Pod (`10.4.0.2`). Both hops are logged because all node edges are sampled. In case the traffic is routed to a Pod on the same node—`10.4.0.3` in this example—the second hop wouldn't be logged because it doesn't leave the node. The second hop is logged by both nodes' sampling points. For the first hop, we identify the Service based on the load balancer IP and Service port (`80`). For the second hop, we identify that the destination Pod is backing the Service on the target port (`8080`).

In this example, the following records are found.

reporter | connection.src_ip | connection.dst_ip | bytes_sent | Annotations  
---|---|---|---|---  
DEST | 203.0.113.1 | 35.35.35.35 | 1,224 |  src_location.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.service.*   
SRC | 10.0.12.2 | 10.4.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
DEST | 10.0.12.2 | 10.4.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
  
### GKE Ingress flows

[ ![Ingress flows.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-8.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-8.svg) Ingress flows (click to enlarge).

A connection from an external IP address to an Ingress destination is terminated at the Cloud Load Balancing service. The connection is mapped to a NodePort Service according to the URL. To serve the request, the load balancer (`130.211.0.1`) connects to one of the cluster nodes (`10.0.12.2`) for routing using the service's NodePort. By default, when creating an Ingress object, the GKE Ingress controller configures an HTTP(S) load balancer that distributes traffic across all nodes in the cluster, even those not running a relevant Pod. Traffic might take extra hops to get to the relevant Pod. For more information, see [Networking outside the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#outside-cluster). The traffic is then routed from the node (`10.0.12.2`) to the selected server Pod (`10.4.0.2`).

Both hops are logged because all node edges are sampled. For the first hop, we identify the Service based on the Service's NodePort (`60000`). For the second hop, we identify that the destination Pod is backing the Service on the target port (`8080`). The second hop is logged by both nodes' sampling points. However, in a case where the traffic is routed to a Pod on the same node (`10.4.0.3`), the second hop is not logged because the traffic didn't leave the node.

In this example, the following records are found.

reporter | connection.src_ip | connection.dst_ip | bytes_sent | Annotations  
---|---|---|---|---  
DEST | 130.211.0.1 | 10.0.12.2 | 1,224 |  dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.service.*   
SRC | 10.0.12.2 | 10.4.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
DEST | 10.0.12.2 | 10.4.0.2 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
  
### GKE Ingress flows using container-native load balancing

[ ![Ingress flows using container-native load balancing.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-9.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-9.svg) Ingress flows using container-native load balancing (click to enlarge).

Requests from an external IP address to an Ingress destination that is using [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing) are terminated at the load balancer. In this type of Ingress, Pods are [core objects for load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing#benefits). A request is then sent from the load balancer (`130.211.0.1`) directly to a selected Pod (`10.4.0.2`). We identify that the destination Pod is backing the Service on the target port (8080).

In this example, the following record is found.

reporter | connection.src_ip | connection.dst_ip | bytes_sent | Annotations  
---|---|---|---|---  
DEST | 130.211.0.1 | 10.4.0.2 | 1,224 |  dest_instance.*  
dest_vpc.*  
dest_gke_details.cluster.*  
dest_gke_details.pod.*  
dest_gke_details.service.*   
  
### Pod to external flows

[ ![Pod to external flow.](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-10.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/flow-logs-10.svg) Pod to external flow (click to enlarge).

Traffic from a Pod (`10.4.0.3`) to an external IP (`203.0.113.1`) is modified by IP masquerading so that the packets are sent from the node IP (`10.0.12.2`) instead of the Pod IP address. By default, the GKE cluster is configured to masquerade traffic to external destinations. For more information, see [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

In order to view Pod annotations for this traffic, you can configure the masquerade agent not to masquerade Pod IP addresses. In such a case, to allow traffic to the internet, you can configure Cloud NAT, which processes the Pod IP addresses. For more information about Cloud NAT with GKE, review [GKE interaction](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE).

In this example, the following record is found.

reporter | connection.src_ip | connection.dst_ip | bytes_sent | Annotations  
---|---|---|---|---  
SRC | 10.0.12.2 | 203.0.113.1 | 1,224 |  src_instance.*  
src_vpc.*  
src_gke_details.cluster.*  
dest_location.*  
internet_routing_details.*   
  
## Serverless flows

For serverless traffic, VPC Flow Logs annotates flows that are sent through Cloud Run or App Engine endpoints configured with Direct VPC egress. For more information, see [ServerlessDetails field format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#serverless-details).

### Serverless-to-VM flows in the same VPC network

For serverless-to-VM flows in the same VPC network, flow logs are reported from both requesting and responding resources, as long as both resources are in subnets that have VPC Flow Logs enabled.

In this example, Cloud Run or App Engine endpoint `10.10.0.2` sends a request with 1,224 bytes to VM `10.50.0.2`. In turn, `10.50.0.2` responds to the request with a reply containing 5,342 bytes. Both the request and reply are recorded from both the requesting endpoint and responding VM.

As reported by requesting Cloud Run or App Engine endpoint (10.10.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.50.0.2 | 1,224 |  src_serverless_details.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.50.0.2 | 10.10.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_serverless_details.*  
dest_vpc.*   
As reported by responding VM (10.50.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.10.0.2 | 10.50.0.2 | 1,224 |  src_serverless_details.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.50.0.2 | 10.10.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_serverless_details.*  
dest_vpc.*   
  
## Hybrid connectivity flows

For hybrid connectivity through VLAN attachments for Cloud Interconnect and Cloud VPN tunnels, VPC Flow Logs annotates the following flows:

  * Flows between VM instances, including instances used as GKE nodes, and on-premises endpoints
  * Flows between Google services and on-premises endpoints
  * Transit flows between on-premises endpoints



The following example describes how VPC Flow Logs annotates flows between a VM instance in a VPC network and an on-premises endpoint. The network is connected to the endpoint through a VLAN attachment for Cloud Interconnect.

[ ![VM flows to on-premises networks.](https://docs.cloud.google.com/static/vpc/images/flow-logs/vms-to-on-premises-flows.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/vms-to-on-premises-flows.svg) VM-to-on-premises flows (click to enlarge).

For flows between a VM that's in a VPC network and an on-premises endpoint with an internal IP address, flow logs are reported from Google Cloud only. The following resources report flow logs:

  * **The VM**. Reports flow logs if the subnet that the VM is connected to has VPC Flow Logs enabled.
  * **The gateway that connects the VPC network to the on-premises endpoint**. Reports flow logs if the gateway (in this example, the VLAN attachment) has VPC Flow Logs enabled.



In the preceding diagram, the on-premises endpoint `10.30.0.2` sends a request with 1,224 bytes to the VM `10.0.0.2` in the VPC network. In turn, the VM `10.0.0.2` responds to the request with a reply containing 5,243 bytes. Both the request and the reply are recorded from both the VLAN attachment and the VM.

As reported by VLAN attachment  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.30.0.2 | 10.0.0.2 | 1,224 |  src_gateway.*  
dest_instance.*  
dest_vpc.*   
reply | 10.0.0.2 | 10.30.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_gateway.*   
As reported by VM (10.0.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.30.0.2 | 10.0.0.2 | 1,224 |  src_gateway.*  
dest_instance.*  
dest_vpc.*   
reply | 10.0.0.2 | 10.30.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_gateway.*   
  
## Flows between VPC networks in different projects

If VPC Flow Logs is configured for an organization and [cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project) are enabled (default), traffic flows between VPC networks in different projects are annotated in the same way as traffic flows between VPC networks in the same project; log records for these flows provide information about both sides of the connection.

If cross-project annotations are disabled, log records provide information only about the reporter of the traffic flow.

### Cross-project annotations enabled

The following example describes how VPC Flow Logs annotates log records for VM-to-VM flows between projects when cross-project annotations are enabled. Cross-project annotations are available for traffic flows through Shared VPC, VPC Network Peering, and Network Connectivity Center.

[ ![VM-to-VM flows in an organization.](https://docs.cloud.google.com/static/vpc/images/flow-logs/cross-project-annotations.svg)](https://docs.cloud.google.com/static/vpc/images/flow-logs/cross-project-annotations.svg) VM-to-VM flows in an organization (click to enlarge).

VM 10.0.0.2 sends a request with 1,224 bytes to VM 10.0.0.1.2. In turn, VM 10.0.0.1.2 responds to the request with a reply containing 5,342 bytes. Both the request and reply are recorded from both the requesting and responding VMs.

As reported by requesting VM (10.0.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.0.0.2 | 10.0.1.2 | 1,224 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.0.1.2 | 10.0.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
As reported by responding VM (10.0.1.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.0.0.2 | 10.0.1.2 | 1,224 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
reply | 10.0.1.2 | 10.0.0.2 | 5,342 |  src_instance.*  
src_vpc.*  
dest_instance.*  
dest_vpc.*   
  
### Cross-project annotations disabled

The following example describes how VPC Flow Logs annotates log records for VM-to-VM flows between projects when cross-project annotations are disabled.

VM 10.0.0.2 sends a request with 1,224 bytes to VM 10.0.0.1.2. In turn, VM 10.0.0.1.2 responds to the request with a reply containing 5,342 bytes. Both the request and reply are recorded from both the requesting and responding VMs. However, information about the other VM isn't provided.

As reported by requesting VM (10.0.0.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.0.0.2 | 10.0.1.2 | 1,224 |  src_instance.*  
src_vpc.*   
reply | 10.0.1.2 | 10.0.0.2 | 5,342 |  dest_instance.*  
dest_vpc.*   
As reported by responding VM (10.0.1.2)  
---  
request-reply | connection.src_ip | connection.dest_ip | bytes_sent | Annotations  
request | 10.0.0.2 | 10.0.1.2 | 1,224 |  dest_instance.*  
dest_vpc.*   
reply | 10.0.1.2 | 10.0.0.2 | 5,342 |  src_instance.*  
src_vpc.*   
  
## What's next

  * [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs)
  * [Access flow logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
