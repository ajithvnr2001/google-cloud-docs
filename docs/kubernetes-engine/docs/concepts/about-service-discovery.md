---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-service-discovery/
title: About service discovery \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:04.052705+00:00
---

# About service discovery  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-service-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About service discovery Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how service discovery in Google Kubernetes Engine (GKE) simplifies application management and how to extend service discovery beyond a single cluster by using Cloud DNS scopes, Multi-cluster Services (MCS), and Service Directory.

This document is for GKE users, Developers, and Admins and architects. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before you read this document, make sure you understand the following concepts:

  * [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/).
  * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).
  * [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview).



## Overview

Service discovery is a mechanism that lets services and applications find and communicate with each other dynamically without hardcoding IP addresses or endpoint configurations. Service discovery helps ensure that applications always have access to up-to-date Pod IP addresses, even when Pods are rescheduled or new Pods are added. GKE offers several ways to implement service discovery, including `kube-dns`, custom `kube-dns` deployments, and Cloud DNS. You can further optimize DNS performance with `NodeLocal DNSCache`.

### Benefits of service discovery

Service discovery provides the following benefits:

  * **Simplified application management** : service discovery eliminates the need to hardcode IP addresses in your application configurations. Applications communicate by using logical Service names, which automatically resolve to the correct Pod IP addresses. This approach simplifies configuration, especially in dynamic environments where Pod IP addresses might change due to scaling or rescheduling.
  * **Simplified scaling and resilience** : service discovery simplifies scaling by decoupling service consumers from Pod IP addresses, which change frequently. While your application scales, or if Pods fail and are replaced, Kubernetes automatically updates which Pods are available to receive traffic for a given Service. Service discovery helps ensure that requests to the stable Service name are directed only to healthy Pods, which lets your application scale or recover from failures without manual intervention or client reconfiguration.
  * **High availability** : GKE uses load balancing together with service discovery to help ensure high availability and improve responsiveness for your applications, even under heavy loads.



### Load balancing with service discovery

GKE helps ensure high availability for your applications by combining different levels of load balancing with service discovery.

  * **Internal Services** : for services that are accessible only within the cluster, GKE's dataplane (`kube-proxy` or `Cilium`) acts as a load balancer. It distributes incoming traffic evenly across multiple healthy Pods, preventing overload and helping to ensure high availability.
  * **External Services** : for services that need to be accessible from outside the cluster, GKE provisions Google Cloud Load Balancers. These load balancers include external Google Cloud Load Balancers for public internet access and internal Google Cloud Load Balancers for access within your Virtual Private Cloud network. These load balancers distribute traffic across the nodes in your cluster. The dataplane on each node then further routes the traffic to the appropriate Pods.



In both internal and external scenarios, service discovery continuously updates the list of available Pods for each Service. This continuous updating helps ensure that both the dataplane (for internal services) and the Google Cloud load balancers (for external services) direct traffic only to healthy instances.

## Use cases for service discovery

The following are common use cases for service discovery:

  * **Microservice architecture** : in a microservice architecture, applications often consist of many smaller, independent services that need to interact. Service discovery enables these applications to find each other and exchange information, even while the cluster scales.
  * **Enable zero-downtime deployments and improve resilience** : Service discovery facilitates zero-downtime updates for applications, including controlled rollouts and canary deployments. It automates the discovery of new service versions and shifts traffic to them, which helps reduce downtime during deployment and ensure a smooth transition for users. Service discovery also enhances resilience. When a Pod fails in GKE, a new one is deployed, and Service discovery registers the new Pod and redirects traffic to it, which helps minimize application downtime.



## How service discovery works

In GKE, applications often consist of multiple Pods that need to find and communicate with each other. Service discovery provides this capability by using the Domain Name System (DNS). Similar to how you use DNS to find websites on the internet, Pods in a GKE cluster use DNS to locate and connect with services by using their Service names. This approach lets Pods interact effectively, regardless of where they are running in the cluster, and allows applications to communicate by using consistent service names rather than unstable IP addresses.

## How Pods perform DNS resolution

Pods in a GKE cluster resolve DNS names for Services and other Pods by using a combination of automatically generated DNS records and their local DNS configuration.

### Service DNS names

When you create a Kubernetes Service, GKE automatically assigns a DNS name to it. This name follows a predictable format, which any Pod in the cluster can use to access the Service:

`<service-name>.<namespace>.svc.cluster.local`

The default cluster domain is `cluster.local`, but you can customize the domain when you create the cluster. For example, a Service that's named `my-web-app` in the default namespace would have the DNS name `my-web-app.default.svc.cluster.local`.

### The role of `/etc/resolv.conf`

To resolve these DNS names, Pods rely on their `/etc/resolv.conf` file. This configuration file tells the Pod which name server to send its DNS queries. The IP address of the name server listed in this file depends on the specific DNS features that are enabled on your GKE cluster. The following table outlines which name server IP a Pod uses, based on your configuration:

Cloud DNS for GKE | NodeLocal DNSCache | `/etc/resolv.conf` name server value  
---|---|---  
Enabled | Enabled | `169.254.20.10`  
Enabled | Disabled | `169.254.169.254`  
Disabled | Enabled | `kube-dns` Service IP address  
Disabled | Disabled | `kube-dns` Service IP address  
  
This configuration helps ensure that DNS queries from the Pod are directed to the correct component:

  * **NodeLocal DNSCache** : provides fast, local lookups on the node.
  * **Metadata server IP (`169.254.169.254`)**: is used when Cloud DNS for GKE is enabled without NodeLocal DNSCache. DNS queries are directed to this IP address, which Cloud DNS uses to intercept and handle DNS requests.
  * **`kube-dns` Service IP address**: is used for standard in-cluster resolution when Cloud DNS for GKE is disabled.



### DNS architecture in GKE

GKE provides a flexible architecture for service discovery, Primarily by using DNS. The following components work together to resolve DNS queries within your cluster:

  * **`kube-dns`** : the default in-cluster DNS provider for GKE Standard clusters. It runs as a managed deployment of Pods in the `kube-system` namespace and monitors the Kubernetes API for new Services to create the necessary DNS records.
  * **Cloud DNS** : Google Cloud's fully managed DNS service. It offers a highly scalable and reliable alternative to `kube-dns` and is the default DNS provider for GKE Autopilot clusters.
  * **`NodeLocal DNSCache`** : a GKE add-on that improves DNS lookup performance. It runs a DNS cache on each node in your cluster, working with either `kube-dns` or Cloud DNS to serve DNS queries locally, which reduces latency and the load on the cluster's central DNS provider. For GKE Autopilot clusters, `NodeLocal DNSCache` is enabled by default and cannot be overridden.
  * **Custom`kube-dns` Deployment**: a Deployment that lets you deploy and manage your own instance of `kube-dns`, which provides more control over `kube-dns` configuration and resources.



#### Choose your DNS provider

The following table summarizes the DNS providers available in GKE, including their features and when to choose each one:

Provider | Features | When to choose  
---|---|---  
`kube-dns` | In-cluster DNS resolution for Services and Pods. | All clusters with standard networking needs. The new version of `kube-dns` is suitable for both small and large-scale clusters.  
Cloud DNS | Advanced DNS features (private zones, traffic steering, global load balancing), and integration with other Google Cloud services. | Exposing services externally, multi-cluster environments, or for clusters with high DNS query rates (QPS).  
Custom `kube-dns` Deployment | Additional control over configuration, resource allocation, and the potential to use alternative DNS providers. | Large-scale clusters or specific DNS needs that require more aggressive scaling or fine-grained control over resource allocation.  
  
## Service discovery outside a single cluster

You can extend service discovery beyond a single GKE cluster By using the following methods:

### Cloud DNS scope

Clusters that use Cloud DNS for cluster DNS can operate in one of three available scopes:

  * **Cluster scope** : this is the default behavior for Cloud DNS. In this mode, Cloud DNS functions equivalently to `kube-dns` by providing DNS resolution exclusively for resources that are within the cluster. DNS records are resolvable only from within the cluster, and they adhere to the standard Kubernetes Service schema: `<svc>.<ns>.svc.cluster.local`.
  * **Additive VPC scope** : this optional feature extends the cluster scope by making headless Services resolvable from other resources within the same VPC network, such as Compute Engine VMs or on-premises clients that connect by using Cloud VPN or Cloud Interconnect.
  * **VPC scope** : with this configuration, DNS records for cluster Services are resolvable within the entire VPC network. This approach means that any client that's in the same VPC or is connected to it (through Cloud VPN or Cloud Interconnect) can directly resolve Service names.



For more information about VPC scope DNS, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).

### Multi-cluster Services

Multi-cluster Services (MCS) enables service discovery and traffic management across multiple GKE clusters. MCS lets you build applications that span clusters while maintaining a unified service experience.

MCS leverages DNS-based service discovery to connect Services across clusters. When you create an MCS instance, it generates DNS records in the format of `<svc>.<ns>.svc.clusterset.local`. These records resolve to the IP addresses of the Service's endpoints in each participating cluster.

When a client in one cluster accesses an MCS, requests are routed to the nearest available endpoint in any of the participating clusters. This traffic distribution is managed by `kube-proxy` (or `Cilium` in GKE GKE Dataplane V2) on each node, which helps ensure efficient communication and load balancing across clusters.

### Service Directory for GKE

Service Directory for GKE provides a unified registry for service discovery across your Kubernetes and non-Kubernetes deployments. Service Directory can register both GKE and non- GKE services in a single registry.

Service Directory is particularly useful if you want any of the following:

  * A single registry for Kubernetes and non-Kubernetes applications to discover each other.
  * A managed service discovery tool.
  * The ability to store metadata about your Service that other clients can access.
  * The ability to set access permissions on a per-Service level. Service Directory services can be resolved by using DNS, HTTP, and gRPC. Service Directory is integrated with Cloud DNS, and can populate Cloud DNS records that match services in Service Directory.



For more information, see [Configure Service Directory for GKE](https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke).

## Optimize DNS performance and best practices

To help ensure reliable and efficient service discovery, especially in large-scale or high-traffic clusters, consider the following best practices and optimization strategies.

### Optimize performance with NodeLocal DNSCache

For clusters that have a high density of Pods, or applications that generate a high volume of DNS queries, you can improve DNS lookup speeds by enabling `NodeLocal DNSCache`. `NodeLocal DNSCache` is a GKE add-on that runs a DNS cache on each node in your cluster. When a Pod makes a DNS request, the request goes to the cache that's on the same node. This approach reduces latency and network traffic.

For more information about how to enable and configure this feature, see [Setting up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).

### Scale your DNS provider

If you use `kube-dns` and experience intermittent timeouts, particularly during periods of high traffic, you might need to scale the number of `kube-dns` replicas. The `kube-dns-autoscaler` adjusts the number of replicas based on the number of nodes and cores in the cluster, and its parameters can be tuned to deploy more replicas sooner.

For detailed instructions, see [Set up a custom `kube-dns` Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-kube-dns).

### General best practices

  * **Select the appropriate DNS provider** : choose your DNS provider based on your cluster's needs. Cloud DNS is recommended for high-QPS workloads, multi-cluster environments, and when you need integration with your broader VPC network. The new version of `kube-dns` is suitable for a wide range of clusters, from small to large, that have standard in-cluster service discovery needs.
  * **Avoid Spot VMs or Preemptible VMs for`kube-dns`**: help ensure the stability of your cluster's DNS service by not running critical system components like `kube-dns` on Spot VMs or Preemptible VMs. Unexpected node terminations can lead to DNS resolution issues.
  * **Use clear and descriptive Service names** : adopt consistent and meaningful naming conventions for your Services to make application configurations easier to read and maintain.
  * **Organize with namespaces** : use Kubernetes namespaces to group related services. This approach helps prevent naming conflicts and improves cluster resource organization.
  * **Monitor and validate DNS** : regularly monitor DNS metrics and logs to identify potential issues before they impact your applications. Periodically test DNS resolution from within your Pods to ensure that service discovery is functioning as expected.



## What's next

  * Read an [overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery) of cluster DNS in GKE.
  * Read [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service) for a general overview of how DNS is used in Kubernetes clusters.
  * Learn how to [set up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).
  * Learn how to [set up a custom `kube-dns` Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-kube-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
