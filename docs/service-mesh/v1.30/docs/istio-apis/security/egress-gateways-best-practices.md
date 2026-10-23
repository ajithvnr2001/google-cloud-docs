---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/istio-apis/security/egress-gateways-best-practices/
title: Best Practices for using Cloud Service Mesh egress gateways on GKE clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:19.276156+00:00
---

# Best Practices for using Cloud Service Mesh egress gateways on GKE clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/istio-apis/security/egress-gateways-best-practices/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best Practices for using Cloud Service Mesh egress gateways on GKE clusters

This document describes how to use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview) egress gateways and other Google Cloud controls to secure outbound traffic (egress) from workloads deployed on a Google Kubernetes Engine (GKE) cluster. These controls can limit connections to external services based on the identity of the source application, a team's namespace, the destination domain, and other properties of the outgoing requests.

There is a [companion tutorial](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/egress-gateway-gke-tutorial) that you can use as a blueprint for configuring egress controls in your own clusters.

The intended audience for this document includes network, platform, and security engineers who administer GKE clusters used by one or more software delivery teams. The controls described here might be especially useful for organizations that must demonstrate compliance with regulations (for example, [GDPR](https://gdpr.eu/) and [PCI](https://www.pcisecuritystandards.org/)).

## Introduction

The traditional approach to network security is to define security perimeters around a group of applications. Firewalls are used at these perimeters to allow or deny traffic based on source and destination IP addresses, while trusting applications and traffic contained within the perimeter. However, this trust involves risk. A malicious insider, or anyone who compromises the perimeter can move freely inside the network, access and exfiltrate data, attack third-party systems, and interfere with administration systems.

When workloads running on a Kubernetes cluster make egress connections to hosts on the internet, applying traditional IP-based security controls can be complicated because:

  * Pod IP addresses don't adequately represent the identity of the workload making the connection. In a Kubernetes environment, Pod IP addresses are assigned ephemerally and are recycled frequently as Pods come and go.

  * It is often impossible to identify a small and fixed set of IP addresses for particular destination hosts. IP addresses change frequently, vary by region, and can be taken from large ranges or represent caches, proxies, or [CDNs](https://wikipedia.org/wiki/Content_delivery_network).

  * Multiple teams sharing the same multi-tenant cluster, with a shared range of source IPs, might have differing external connectivity requirements.




[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview) is a fully managed service mesh on Google Cloud. A service mesh provides a uniform way to connect, manage, and secure application communication. Service meshes take an application-centric approach and use trusted application identities rather than a network IP focused approach.

You can deploy a service mesh transparently without the need to modify existing application code. Using a service mesh helps to decouple the work of development teams that are responsible for delivering and releasing application features, from the responsibilities of network administrators by providing declarative control of network behavior.

Cloud Service Mesh provides the [option to deploy](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/gateways) standalone forward-proxies, known as egress gateways, at the edge of the mesh. This guide explains how the features of the egress gateway proxy can be combined with Google Cloud features to control, authorize, and observe outbound traffic from workloads deployed to a GKE cluster.

![conceptual components](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/conceptual-components.svg)

## Defense-in-depth architecture

The diagram below shows an architecture that takes a defense-in-depth approach to the fine-grained control of egress traffic for a cluster used by multiple teams. The controls are based both on [Layer 4 (transport)](https://wikipedia.org/wiki/Transport_layer) and [Layer 7 (application)](https://wikipedia.org/wiki/Application_layer) network controls.

![overall architecture](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/overall-architecture.svg)

The architecture uses the following resources and controls:

  * A [private GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept): Nodes on a private GKE cluster only have internal IP addresses and aren't connected to the internet by default.

  * [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE): Cloud NAT allows outbound internet access from the private cluster.

  * [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls): You configure VPC firewall rules to apply Layer 4 (Transport) controls to connections to and from the nodes in the GKE cluster. You can apply VPC firewall rules to VMs based on [service accounts](https://docs.cloud.google.com/vpc/docs/firewalls#serviceaccounts) or [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

  * [GKE node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) with different service accounts: This lets you configure different firewall rules to be applied depending on the node pool a node belongs to.

  * Kubernetes [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/): You create namespaces for each team to provide isolation and delegated administrative control. Network administrators use a dedicated namespace to deploy the egress gateway and to configure routing to external hosts.

  * Kubernetes [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/): Network policies let you apply Layer 4 controls to Pods. Each network policy is [scoped to a namespace](https://docs.cloud.google.com/anthos-config-management/docs/how-to/configs#network-policy-config) and can be more finely scoped to particular Pods in a namespace.

  * An egress gateway: Traffic leaving Pods within the mesh is directed through dedicated egress gateway proxies running on dedicated nodes. You deploy egress gateways with a [horizontal Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) so that the number of replicas scales up and down with traffic.

  * [Authorization policies](https://istio.io/v1.30/docs/reference/config/security/authorization-policy/): You use mesh authorization policies to apply Layer 7 (application) controls to traffic between Pods within the mesh and to traffic leaving the mesh.

  * [Sidecar resources](https://istio.io/v1.30/docs/reference/config/networking/sidecar/): You use Sidecar resources to control the configuration scope of the sidecar proxies running in each workload Pod. You can use the Sidecar resource to configure the namespaces, Pods, and external services that are visible to a workload.

  * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options#pga): This option lets nodes and Pods on the private cluster access Google APIs and pull Docker images from [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview).

  * [GKE Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity): With Workload Identity, you can use [Identity and Access Management](https://docs.cloud.google.com/iam) (IAM) to grant API permissions to specific workloads following [the principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege), without the need to handle secrets.




## Configuring egress controls

If you use the egress gateway to secure egress traffic from your mesh, we recommend that you configure the defense-in-depth controls described in this section.

### Use Private GKE with Cloud NAT

Where security is important, the first requirement of many organizations is to avoid assigning public IP addresses to their workloads. A [private GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) satisfies this requirement. You can configure [VPC Native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) mode on your private cluster so that Pods and services are assigned IP addresses from secondary ranges in the VPC. VPC Native Pod IP addresses are natively routable within the VPC network.

Some workloads might require access to services outside of the VPC network and to the internet. To allow workloads to connect to external hosts without needing them to have public IP addresses, configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE) to provide network address translation (NAT).

Ensure that Cloud NAT is configured so that the egress gateway can make a sufficient number of simultaneous connections to external destinations. You can avoid port exhaustion and problems with connection reuse delays by setting the minimum number of ports per VM appropriately. See the [Cloud NAT address and port overview](https://docs.cloud.google.com/nat/docs/ports-and-addresses) for more details. Increasing the number of egress gateway replicas can help to reduce the chances of [endpoint-independent mapping conflicts](https://docs.cloud.google.com/nat/docs/ports-and-addresses#example-conflict-eim).

### Configure Private Google Access for Google APIs and services

It's likely that your workloads need to have access to Google APIs and services. Use Private Google Access with [Custom DNS zones](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) to allow connectivity from private VPC subnets to Google APIs using a set of four IP addresses. When using these IP addresses there is no need for Pods to have external IP addresses and the traffic never leaves the Google network. You can use `private.googleapis.com` (`199.36.153.8/30`) or `restricted.googleapis.com` (`199.36.153.4/30`), depending on whether you're using [VPC Service Controls](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config).

### Use Workload Identity and IAM to further secure Google APIs and services

Using [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is the recommended way to allow GKE workloads to authenticate with Google APIs and for administrators to apply "least privilege" authorization controls using IAM.

When using Private Google Access, Workload Identity, and IAM, you can safely allow workload Pods to bypass the egress gateway and connect directly to Google APIs and services.

### Use Kubernetes namespaces for administrative control

Namespaces are an organizational resource that are helpful in environments where there are many users, teams, or tenants. They can be thought of as a virtual cluster, and they allow administrative responsibility for groups of Kubernetes resources to be delegated to different administrators.

Namespaces are an important feature for isolation of administrative control. However, they don't, by default, provide node isolation, data plane isolation, or network isolation.

Cloud Service Mesh builds on Kubernetes namespaces by using them as a [unit of tenancy](https://istio.io/v1.30/docs/ops/deployment/deployment-models/#namespace-tenancy) within a service mesh. Mesh authorization policies and sidecar resources can restrict visibility and access based on namespace, identity, and Layer 7 (application) attributes of network traffic.

Likewise, you can use Kubernetes network policies to allow or deny network connections at Layer 4 (transport).

### Run egress gateways on dedicated gateway nodes

Running egress gateways on nodes in a dedicated gateway node pool offers several advantages. The externally facing nodes can use a [hardened configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster), and you can configure VPC firewall rules to prevent workloads from reaching external hosts directly. The node pools can be independently autoscaled using the cluster autoscaler.

To allow separate administrative control of the egress gateway, deploy it to a dedicated `istio-egress` namespace. However, namespaces are a cluster-wide resource and it isn't possible to use them to control which nodes the deployment runs on. For deployment control, use a [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) for the egress gateway deployment so that it runs on nodes that are labeled as members of the gateway node pool.

Ensure that only gateway Pods can run on gateway nodes. Other Pods should be repelled from gateway nodes, otherwise the egress controls could be bypassed. Workloads can be prevented from running on certain nodes by using [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/). You should taint the nodes in the gateway node pool and add a corresponding toleration to the egress gateway deployment.

**Important:** Restrict the toleration of the egress gateway deployment so that workloads cannot be deployed to the gateway nodes. Options for restricting the use of tolerations are described later in this guide.

### Apply VPC firewall rules to specific nodes

You configure service mesh routing to direct egress traffic from the workloads running in the default node pool through the egress gateways running in the gateway node pool. However, the routing configuration of the mesh should not be trusted as a security boundary because there are various ways in which a workload could bypass the mesh proxies.

To prevent application workloads from connecting directly to external hosts, apply restrictive egress firewall rules to the nodes in the default node pool. Apply separate firewall rules to the gateway nodes so that the egress gateway Pods running on them can connect to external hosts.

When creating a [VPC firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls), you specify the ports and protocols that the firewall rule allows or denies and the direction of the traffic to which it applies. Egress rules apply to outgoing traffic and ingress rules apply to incoming traffic. The default for egress is `allow` and the default for ingress is `deny`.

Firewall rules are applied in order based on a priority number which you can specify. Firewall rules are stateful, which means that if specific traffic from a VM is allowed, then return traffic using the same connection is also allowed.

The following diagram shows how separate firewall rules can be applied to nodes in two different node pools based on the service account assigned to a node. In this case, a default `deny all` firewall rule denies egress access for the whole VPC. To avoid overriding default firewall rules that are essential for your cluster to operate, your `deny all` rule should use a low priority such as 65535\. An additive and higher priority egress firewall rule is applied to the gateway nodes to allow them to connect directly to external hosts on ports 80 and 443. The default node pool has no access to external hosts.

![firewall node pool](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/firewall-node-pool.svg)

### Use Kubernetes Network policies as a firewall for Pods and namespaces

Use [Kubernetes network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) to apply an extra layer of security as part of a defense-in-depth strategy. Network policies are scoped to namespaces and operate at Layer 4 (transport). With network policies, you can restrict ingress and egress:

  * Between namespaces
  * To Pods within a namespace
  * To particular ports and IP blocks.



After any network policy selects Pods in a namespace, any connections that are not explicitly allowed are rejected. When multiple network policies are applied, the result is additive and is a union of the policies. The order in which policies are applied doesn't matter.

The companion tutorial includes the following network policy examples:

  * Allow egress connections from the workload namespaces to the `istio-system` and `istio-egress` namespaces. Pods must be able to connect to `control-plane` and the egress gateway.
  * Allow workloads to make DNS queries from the workload namespaces to port 53 in the `kube-system` namespace.
  * Optionally, allow workloads in the same namespace to connect to each other.
  * Optionally, allow egress connections between the namespaces used by different application teams.
  * Allow egress connections from workload namespaces to the VIPs for the Google APIs (exposed by using Private Google Access). Cloud Service Mesh provides a managed CA and exposes it as an API, so the sidecar proxies must be able to connect to it. It's also likely that some workloads need access to Google APIs.
  * Allow egress connections from workload namespaces to the GKE metadata server so that the sidecar proxies and the workloads can make metadata queries and authenticate to Google APIs.



By default, when a sidecar proxy is injected into a workload Pod, `iptables` rules are programmed so that the proxy captures all inbound and outbound TCP traffic. However, as mentioned previously, there are ways for workloads to bypass the proxy. VPC firewall rules prevent direct egress access from the default nodes that run the workloads. You can use Kubernetes network policies to ensure that no direct external egress is possible from workload namespaces and that egress is possible to the `istio-egress` namespace.

If you also control ingress with network policies, then you need to create ingress policies to correspond with your egress policies.

## Service Mesh configuration and security

Workloads running in a service mesh are not identified based on their IP addresses. Cloud Service Mesh assigns a strong and verifiable identity in the form of an [X.509](https://wikipedia.org/wiki/X.509) certificate and key for each workload. Trusted communication between workloads is established using authenticated and encrypted [mutual TLS (mTLS)](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview#mutual_tls) connections.

The use of mTLS authentication with a well-defined identity for each application allows you to use mesh authorization policies for fine-grained control over how workloads can communicate with external services.

Although traffic can leave the mesh directly from the sidecar proxies, if you need extra control we recommend that you route traffic through egress gateways as described in this guide.

### Manage configuration for egress controls in a dedicated namespace

Allow network administrators to centrally manage controls by using a dedicated `istio-egress` namespace for egress-related mesh configuration. As previously recommended, you deploy the egress gateway to the `istio-egress` namespace. You can create and manage service entries, gateways, and authorization policies in this namespace.

### Define external destinations with Service Entries

Configure [Service Entries](https://istio.io/latest/docs/reference/config/networking/service-entry/) to explicitly register external hosts in the mesh's service registry. By default, service entries are visible to all namespaces. Use the [exportTo attribute](https://istio.io/latest/docs/reference/config/networking/service-entry/#ServiceEntry-export_to) to control which namespaces a service entry is visible to. Service Entries determine the outbound routes that are configured in mesh proxies but should not, on their own, be considered a secure control for determining which external hosts workloads can connect to.

### Configure egress gateway behavior with the Gateway resource

Configure the load-balancing behavior of egress gateways using the [Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/) resource. The load balancer can be configured for a particular set of hosts, protocols, and ports and associated with an egress gateway deployment. For example, a gateway might be configured for egress to ports 80 and 443 for any external host.

Cloud Service Mesh enables auto mTLS by default. With auto mTLS, a client sidecar proxy automatically detects if the server has a sidecar. The client sidecar sends mTLS to workloads with sidecars and sends plain text traffic to workloads without sidecars. Even with auto mTLS, traffic sent to the egress gateway from sidecar proxies doesn't automatically use mTLS. To indicate how connections to the egress gateway should be secured, you have to set the TLS mode on the Gateway resource. Whenever possible, use mTLS for connections from sidecar proxies to the egress gateway.

### Configure Virtual Services and Destination Rules to route traffic through the gateway

Use [Virtual Services](https://istio.io/latest/docs/reference/config/networking/virtual-service/) and [Destination Rules](https://istio.io/latest/docs/reference/config/networking/destination-rule/) to configure the routing of traffic from sidecar proxies through the egress gateway to external destinations. Virtual services define rules for matching certain traffic. The matched traffic is then sent to a destination. Destination rules can define subsets (for example, the egress gateway or an external host) and how traffic should be handled when being routed to the destination.

Use a single destination rule for multiple destination hosts to explicitly specify how traffic from sidecar proxies to the gateway should be secured. As explained previously, the preferred method is for workloads to send plain text requests and for the sidecar proxy to originate a mTLS connection to the gateway.

Use a destination rule for each external host to configure the egress gateway to 'upgrade' plain HTTP requests to use a TLS (HTTPS) connection when forwarding to the destination. Upgrading a plain text connection to TLS is often referred to as _TLS origination_.

### Use Authorization Policy to allow or deny traffic at the egress gateway

[AuthorizationPolicy](https://istio.io/latest/docs/reference/config/security/authorization-policy/) is a resource that lets you configure fine-grained access control policy for mesh traffic. You can create policies to allow or deny traffic based on properties of the source, destination, or the traffic itself (for example, the host or headers of an HTTP request).

To allow or deny connections based on the source workload's identity or namespace, the connection to the egress gateway must be authenticated with mTLS. Connections from sidecars to the egress gateway do not automatically use mTLS, so the destination rule for connections to the gateway must explicitly specify the [`ISTIO_MUTUAL` TLS mode](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview#mutual_tls).

To allow or deny requests at the gateway using authorization policies, workloads should send plain HTTP requests to destinations outside of the mesh. The sidecar proxies can then forward the request to the gateway using mTLS and the gateway can originate a secure TLS connection to the external host.

To support the egress requirements of different teams and applications, configure separate "least privilege" authorization policies per namespace or workload. For example, different policies can be applied at the egress gateway by specifying rules based on the namespace of the source workload and attributes of the request as follows:

  * If the source namespace is **team-x** AND the destination host is **example.com** , then **allow** the traffic.

![authorization policies example](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/authz-example.svg)

  * If the source namespace is **team-y** AND the destination host is **httpbin.org** AND the path is **/status/418** then **allow** the traffic.

![authorization policies using httpbin](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/authz-httpbin.svg)




All other requests are denied.

### Configure the egress gateway to originate TLS (HTTPS) connections to the destination

Configure destination rules so that the egress gateway originates TLS (HTTPS) connections to external destinations.

For TLS origination at the egress gateway to work, workloads must send plain HTTP requests. If the workload initiates TLS, the egress gateway wraps TLS on top of the original TLS, and requests to the external service will fail.

Because workloads are sending plain HTTP requests, configure the workload's sidecar proxy to establish an mTLS connection when sending them to the gateway. The egress gateway then terminates the mTLS connection and originates a regular TLS (HTTPS) connection to the destination host.

![TLS origination at egress gateway](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/tls-origination.svg)

This approach has several advantages:

  * You can use an authorization policy to allow or deny traffic based on attributes of the source workload and the requests.

  * Traffic between workload Pods and the egress gateway is encrypted and authenticated (mTLS) and traffic between the egress gateway and the destination is encrypted (TLS/HTTPS).

  * Inside the mesh, sidecar proxies can observe and act upon the properties of HTTP requests (for example, headers), providing additional options for observability and control.

  * Application code can be simplified. There is no need for developers to deal with certificates or HTTPS client libraries and the service mesh can ensure secure communication with standard and up-to-date ciphers.

  * TLS connections that the egress gateway originates to external services can be reused for traffic from many Pods. Connection reuse is more efficient and reduces the risk of connection limits being reached.




### DNS, hostnames, and wildcards

When routing, denying, or allowing traffic based on the destination host, you must have full trust in the integrity of your DNS systems to resolve DNS names to the correct IP address. On Kubernetes Engine clusters, the Kubernetes DNS service handles DNS queries and in turn delegates external queries to the GKE metadata server and [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns). Set the [resolution attribute](https://istio.io/latest/docs/reference/config/networking/service-entry/#ServiceEntry-Resolution) of service entries to DNS when routing to external hosts, so that the sidecar proxies are responsible for making DNS queries.

Cloud Service Mesh can route traffic based on wildcard hosts. The simplest case is a wildcard for hosts that share a common name and are hosted on a common set of servers. For example, if a single set of servers can serve the domains matched by `*.example.com`, then a wildcard host can be used.

A standard egress gateway cannot forward based on more general and arbitrary wildcard hosts (for example `*.com`) due to certain limitations of the Envoy proxy used by Istio. Envoy can only route traffic to predefined hosts, predefined IP addresses, or to the original destination IP address of a request. When using an egress gateway, the original destination IP of the request is lost because it is replaced with the IP of the gateway and the arbitrary destination hosts cannot be preconfigured.

## Administrative enforcement of policies

### Use Kubernetes Role Based Access Control (RBAC)

Only authorized administrators should be able to configure egress controls. Configure [Kubernetes Role Based Access Control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) to avoid unauthorized circumvention of egress controls. Apply RBAC roles so that only network administrators can manage the `istio-egress`,`istio-system,`and`kube-system` namespaces and the following resources:

  * Sidecar
  * ServiceEntry
  * Gateway
  * AuthorizationPolicy
  * NetworkPolicy



### Restricting the use of tolerations

As previously described you can use taints and tolerations to prevent workload Pods from being deployed on gateway nodes. However, by default, there is nothing to prevent workloads from being deployed with a toleration for the gateway nodes and hence allow egress controls to be bypassed. If it is possible to enforce centralized administrative control over deployment pipelines, you can use them to enforce restrictions on the use of certain toleration keys.

Another approach is to use [Kubernetes admission control](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers). Anthos includes a component called [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) which acts as a Kubernetes admission controller and validates that deployments meet the policy constraints that you specify.

## Ensure traffic is logged

It is often necessary to log all traffic that crosses network perimeters. Traffic logging is essential if you must be able to demonstrate compliance with common data protection regulations. Traffic logs are sent directly to [Cloud Logging](https://docs.cloud.google.com/logging) and [can be accessed](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/accessing-logs#accessing_traffic_logs) from the Cloud Service Mesh dashboards in the Google Cloud console. You can filter logs based on various attributes including source/destination, identity, namespace, attributes of the traffic, and latency.

To allow easy debugging with `kubectl`, enable traffic logging to `stdout` when installing Cloud Service Mesh by using the [accessLogFile setting](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/options/enable-optional-features#direct_envoy_to_stdout).

[Audit logs](https://docs.cloud.google.com/service-mesh/v1.30/docs/audit-logging) are sent to Cloud Logging each time Mesh CA creates a certificate for a workload.

## Consider using a separate cluster for egress gateways in multi-cluster meshes

Cloud Service Mesh can be [deployed across more than one GKE cluster](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/gke-install-multi-cluster). Multi-cluster meshes introduce new possibilities for controlling egress traffic and also some limitations.

Instead of deploying the egress gateway to a dedicated node pool, you can deploy the gateway to a separate cluster that does not run regular workloads. Using a separate cluster provides similar isolation between workloads and gateways, while avoiding the need for taints and tolerations. The egress gateway can share the separate cluster with ingress gateways or other central services.

You can use Kubernetes network policies in multi-cluster deployments, but because they operate at Layer 4 (transport), they can't restrict cross-cluster connections based on the destination namespace or Pod.

## What's next

  * Try out the [companion tutorial](https://docs.cloud.google.com/service-mesh/v1.30/docs/istio-apis/security/egress-gateway-gke-tutorial)
  * Consult the [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) hardening guide
  * Learn about managing configuration and policy across all of your infrastructure with [Anthos Configuration Management](https://docs.cloud.google.com/anthos/config-management)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
