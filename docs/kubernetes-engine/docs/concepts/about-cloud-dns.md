---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-cloud-dns/
title: About Cloud DNS for GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:04.142724+00:00
---

# About Cloud DNS for GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-cloud-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About Cloud DNS for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document helps you decide whether Cloud DNS for GKE is the right DNS solution for your cluster. You can use Cloud DNS to handle Pod and Service DNS resolution as an alternative to cluster-hosted DNS providers like `kube-dns`.

For Autopilot clusters, Cloud DNS is already the default DNS provider. For Standard clusters, you can switch from `kube-dns` to Cloud DNS.

This document is for GKE users, including Developers and Admins and architects. To learn more about common roles and example tasks in Google Cloud, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This document assumes that you are familiar with the following concepts:

  * [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/).
  * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).
  * [About service discovery](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-service-discovery).



## How Cloud DNS for GKE works

When you use Cloud DNS as the DNS provider for GKE, Cloud DNS provides Pod and Service DNS resolution without requiring a cluster-hosted DNS provider. DNS records for Pods and Services are automatically provisioned in Cloud DNS for cluster IP address, headless, and external name Services.

Cloud DNS supports the full Kubernetes DNS specification and provides resolution for A, AAAA, SRV, and PTR records for Services within a GKE cluster. PTR records are implemented by using response policy rules. Using Cloud DNS as the DNS provider for GKE offers the following benefits over cluster-hosted DNS:

  * **Reduced overhead** : removes the need to manage cluster-hosted DNS servers. Cloud DNS requires no manual scaling, monitoring, or managing of DNS instances because it is a fully managed service.
  * **High scalability and performance** : resolves queries locally for each GKE node to provide low-latency and highly scalable DNS resolution. For optimal performance, especially in large-scale clusters, consider enabling NodeLocal DNSCache, which provides an additional caching layer on the node.
  * **Integration with Google Cloud Observability** : enables DNS monitoring and logging. For more information, see [Enabling and disabling logging for private managed zones](https://docs.cloud.google.com/dns/docs/monitoring#logging).



## Architecture

When Cloud DNS is the DNS provider for GKE, a controller runs as a GKE-managed Pod. This Pod runs on the control plane nodes of your cluster and syncs the cluster DNS records into a managed private DNS zone.

The following diagram shows how the Cloud DNS control plane and data plane resolve cluster names:

![A Pod requests the IP address of a service using Cloud DNS.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-cloud-dns-architecture.svg)Resolving cluster names using Cloud DNS

In the diagram, the Service backend selects the running backend Pods. The clouddns-controller creates a DNS record for the Service backend.

The Pod frontend sends a DNS request to resolve the IP address of the Service named backend to the Compute Engine local metadata server at 169.254.169.254. The metadata server runs locally on the node, sending cache misses to Cloud DNS.

Cloud DNS resolves the Service name to different IP addresses based on the type of Kubernetes Service. For `ClusterIP` Services, Cloud DNS resolves the Service name to its virtual IP address; for headless Services, it resolves the Service name to the list of endpoint IP addresses.

After the Pod frontend resolves the IP address, the Pod can send traffic to the Service backend and any Pods behind the Service.

**Note:** On GKE versions 1.19 and later, `kube-dns` continues to run on new and existing GKE clusters that have Cloud DNS enabled. You can disable `kube-dns` by scaling the `kube-dns` Deployment and autoscaler to zero.

## DNS scopes

Cloud DNS has the following [DNS scopes](https://docs.cloud.google.com/dns/docs/scopes). A cluster cannot operate in multiple modes simultaneously.

  * [**GKE cluster scope**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#cluster_scope_dns): DNS records are resolvable only within the cluster, which is the same behavior as `kube-dns`. Only nodes that run in the GKE cluster can resolve Service names. By default, clusters have DNS names that end in `*.cluster.local`. These DNS names are visible only within the cluster, and don't overlap or conflict with `*.cluster.local` DNS names for other GKE clusters in the same project. **This mode is the default mode**. 
    * [**Cloud DNS additive VPC scope**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#additive_vpc_scope_dns): the Cloud DNS additive VPC scope is an optional feature that extends the GKE cluster scope to make headless Services resolvable from other resources in the VPC, such as Compute Engine VMs or on-premises clients that are connected by using Cloud VPN or Cloud Interconnect. This mode is an additional mode that's enabled alongside cluster scope. You can [enable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#additive_vpc_scope_dns) or [disable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#disable-additive-vpc-scope) this mode in your cluster without impacting DNS uptime or cluster scope capabilities.
  * [**VPC scope**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#vpc_scope_dns): DNS records are resolvable within the entire VPC. Compute Engine VMs and on-premises clients can connect by using Cloud Interconnect or Cloud VPN, and can directly resolve GKE Service names. You must set a [unique custom domain](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#enable_scope_dns_in_an_existing_cluster) for each cluster, which means that all Service and Pod DNS records are unique within the VPC. This mode reduces communication friction between GKE and non-GKE resources.



The following table lists the differences between DNS scopes:

Feature | GKE cluster scope | Cloud DNS additive VPC scope | VPC scope  
---|---|---|---  
**Scope of DNS visibility** | Only within the GKE cluster | Cluster-only, with headless Services resolvable across the VPC network | Entire VPC network  
**Headless Service resolution** | Resolvable within the cluster | Resolvable within the cluster by using the `cluster.local` domain, and across the VPC by using the cluster suffix | Resolvable within the cluster and across the VPC by using the cluster suffix  
**Unique domain requirement** | No; uses the default `*.cluster.local` domain | Yes, you must set a unique custom domain | Yes, you must set a unique custom domain  
**Setup configuration** | Default, no extra steps | Optional upon cluster creation  
Can be enabled or disabled at any time | Must be configured during cluster creation  
  
## Cloud DNS resources

When you use Cloud DNS as your DNS provider for your GKE cluster, the Cloud DNS controller creates resources in Cloud DNS for your project. The resources that GKE creates depends on the Cloud DNS scope.

Scope | Forward lookup zone | Reverse lookup zone  
---|---|---  
Cluster scope | 1 [private zone](https://docs.cloud.google.com/dns/docs/key-terms#dns-private-zones) per cluster per Compute Engine zone (in the region)  | 1 [response policy zone](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) per cluster per Compute Engine zone (in the region)   
Cloud DNS additive VPC scope | 1 [private zone](https://docs.cloud.google.com/dns/docs/key-terms#dns-private-zones) per cluster per Compute Engine zone (in the region) per cluster (global zone)   
1 [VPC-scoped private zone](https://docs.cloud.google.com/dns/docs/key-terms#dns-private-zones) per cluster (global zone)  | 1 [response policy zone](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) per cluster per Compute Engine zone (in the region) per cluster (global zone)   
1 [VPC-scoped response policy zone](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) per cluster (global zone)   
VPC scope | 1 [private zone](https://docs.cloud.google.com/dns/docs/key-terms#dns-private-zones) per cluster (global zone)  | 1 [response policy zone](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) per cluster (global zone)   
  
The naming convention used for these Cloud DNS resources is the following:

Scope | Forward lookup zone | Reverse lookup zone  
---|---|---  
Cluster scope | `gke-CLUSTER_NAME-CLUSTER_HASH-dns` | `gke-CLUSTER_NAME-CLUSTER_HASH-rp`  
Cloud DNS additive VPC scope | `gke-CLUSTER_NAME-CLUSTER_HASH-dns` for cluster-scoped zones   
`gke-CLUSTER_NAME-CLUSTER_HASH-dns-vpc` for VPC-scoped zones  | `gke-CLUSTER_NAME-CLUSTER_HASH-rp` for cluster-scoped zones   
`gke-NETWORK_NAME_HASH-rp` for VPC-scoped zones  
VPC scope | `gke-CLUSTER_NAME-CLUSTER_HASH-dns` | `gke-NETWORK_NAME_HASH-rp`  
  
In addition to the zones that are mentioned in the previous table, the Cloud DNS controller creates the following zones in your project, depending on your configuration:

Custom DNS configuration | Zone type | Zone naming convention  
---|---|---  
Stub domain | Forwarding (global zone) | `gke-CLUSTER_NAME-CLUSTER_HASH-DOMAIN_NAME_HASH`  
Custom upstream name servers | Forwarding (global zone) | `gke-CLUSTER_NAME-CLUSTER_HASH-upstream`  
  
For more information about how to create custom stub domains or custom upstream name servers, see [Adding custom resolvers for stub domains](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns#customize-kube-dns).

### Managed zones and forwarding zones

For clusters that use **cluster scope** to serve internal DNS traffic, the Cloud DNS controller creates a [managed DNS zone](https://docs.cloud.google.com/dns/docs/zones/zones-overview) in each Compute Engine zone of the region that the cluster belongs to.

For example, if you deploy a cluster in the `us-central1-c` zone, the Cloud DNS controller creates a managed zone in `us-central1-a`, `us-central1-b`, `us-central1-c`, and `us-central1-f`.

For each DNS `stubDomain`, the Cloud DNS controller creates one forwarding zone.

The Cloud DNS processes each DNS upstream using one managed zone with the `.` DNS name.

## Quotas

Cloud DNS uses quotas to limit the number of resources that GKE can create for DNS entries. [Quotas and limits for Cloud DNS](https://docs.cloud.google.com/dns/quotas) might be different from the limitations of `kube-dns` for your project.

The following default quotas are applied to each managed zone in your project when you use Cloud DNS for GKE:

Kubernetes DNS resource | Corresponding Cloud DNS resource | Quota  
---|---|---  
Number of DNS records | Max bytes per managed zone | 2,000,000 (50 MB max for a managed zone)  
Number of Pods per headless Service (IPv4 or IPv6) | Number of records per resource record set | GKE 1.24 to 1.25: 1,000 (both IPv4 or IPv6)  
GKE 1.26 and later: 3,500 for IPv4; 2,000 for IPv6  
Number of GKE clusters in a project | Number of response policies per project | 100  
Number of PTR records per cluster | Number of rules per response policy | 100,000  
**Note:** For VPC scope, the same limits apply to the managed zone That's used for the entire VPC. These quotas apply to the set of clusters that use the Cloud DNS VPC scope and run in the same VPC.

## Resource limits

The Kubernetes resources that you create per cluster contribute to [Cloud DNS resource limits](https://docs.cloud.google.com/dns/quotas#resource_limits), as described in the following table:

Limit | Contribution to limit  
---|---  
Resource record sets per managed zone | Number of services plus number of headless service endpoints with valid hostnames, per cluster.  
Records per resource record set | Number of endpoints per headless service. Does not impact other service types.  
Number of rules per response policy | For cluster scope, number of services plus number of headless service endpoints with valid hostnames per cluster. For VPC scope, number of services plus number of headless endpoints with hostnames from all clusters in the VPC.   
  
For more informatione about how DNS records are created for Kubernetes, see [Kubernetes DNS-Based Service Discovery](https://github.com/kubernetes/dns/blob/master/docs/specification.md).

## More than one cluster per service project

Starting in GKE versions 1.22.3-gke.700 and 1.21.6-gke.1500, you can create clusters in multiple service projects that reference a VPC in the same host project.

## Support custom stub domains and upstream name servers

Cloud DNS for GKE supports custom stub domains and upstream name servers that are configured by using kube-dns ConfigMap. This support is available only for GKE Standard clusters.

Cloud DNS translates `stubDomains` and `upstreamNameservers` values into Cloud DNS forwarding zones.

**Note:** The custom DNS configuration applies to both nodes and Pods in the cluster. This behavior is different from `kube-dns`, where the custom DNS configuration applies only to Pods.

## Specification extensions

To improve service discovery and compatibility with various clients and systems, you can use additions on top of the general [Kubernetes DNS specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md).

### Named ports

This section explains how named ports affect the DNS records that are created by Cloud DNS for your Kubernetes cluster. Kubernetes defines a minimum set of required DNS records, but Cloud DNS might create additional records for its own operation and to support various Kubernetes features. The following tables illustrate the minimum number of record sets you can expect, where "`E`" represents the number of endpoints, and "`P`" represents the number of ports. Cloud DNS might create additional records.

IP stack type | Service type | Record sets  
---|---|---  
Single stack | ClusterIP | $$2+P$$  
Headless | $$2+P+2E$$  
Dual stack | ClusterIP | $$3+P$$  
Headless | $$3+P+3E$$  
See [Single and dual stack services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#single-stack_and_dual-stack_services) for more information about single and dual stack services.

## Additional DNS records created by Cloud DNS

Cloud DNS might create additional DNS records beyond the minimum number of record sets. These records serve various purposes, including the following:

  * **SRV records** : for service discovery, Cloud DNS often creates SRV records. These records provide information about the service's port and protocol.
  * **AAAA records (for dual stack)** : in dual-stack configurations that use both IPv4 and IPv6, Cloud DNS creates both A records (for IPv4) and AAAA records (for IPv6) for each endpoint.
  * **Internal records** : Cloud DNS might create internal records for its own management and optimization. These records are typically not directly relevant to users.
  * **LoadBalancer Services** : for services of type `LoadBalancer`, Cloud DNS creates records that are associated with the external load balancer IP address.
  * **Headless Services** : headless services have a distinct DNS configuration. Each Pod gets its own DNS record, which lets clients connect directly to the Pods. This approach is why the port number is not multiplied in the headless Service record calculation.

**Example** : Consider a Service that's called `my-http-server` and that's in the `backend` namespace. This Service exposes two ports, 80 and 8080, for a deployment with three Pods. Therefore, E = 3 and P = 2. | IP stack type | Service type | Record sets  
---|---|---  
Single stack | ClusterIP | $$2+2$$  
Headless | $$2+2+2*3$$  
Dual stack | ClusterIP | $$3+2$$  
Headless | $$3+2+3*3$$  
  
In addition to these minimum records, Cloud DNS might create SRV records and, in the case of dual-stack networking, AAAA records. If `my-http-server` is a LoadBalancer type Service, additional records for the load balancer IP are created. Note: Cloud DNS adds supplementary DNS records as needed. The specific records that are created depend on factors like the Service type and configuration.

## Known issues

This section describes common issues you might encounter when you use Cloud DNS with GKE, along with potential workarounds.

### Terraform tries to re-create Autopilot cluster due to a `dns_config` change

If you use `terraform-provider-google` or `terraform-provider-google-beta`, you might experience an issue where Terraform tries to re-create an Autopilot cluster. This error occurs because newly created Autopilot clusters that run versions 1.25.9-gke.400, 1.26.4-gke.500, or 1.27.1-gke.400 or later use Cloud DNS as a DNS provider instead of `kube-dns`.

This issue is [resolved](https://github.com/GoogleCloudPlatform/magic-modules/pull/8654) in version 4.80.0 of the Terraform provider of Google Cloud.

If you cannot update the version of `terraform-provider-google` or `terraform-provider-google-beta`, you can add the `lifecycle.ignore_changes` setting to the resource to help ensure that `google_container_cluster` ignores changes to `dns_config`:
    
    
      lifecycle {
        ignore_changes = [
          dns_config,
        ]
      }
    

### DNS resolution fails after migrating from `kube-dns` to Cloud DNS with NodeLocal DNSCache enabled

This section describes a known issue for GKE clusters that are in Cloud DNS, and that have enabled NodeLocal DNSCache in the cluster scope.

When NodeLocal DNSCache is enabled on the cluster and you migrate from `kube-dns` to Cloud DNS, your cluster might experience intermittent resolution errors.

If you use `kube-dns` with NodeLocal DNSCache enabled on the cluster, NodeLocal DNSCache is configured to listen on both addresses: the NodeLocal DNSCache address and the `kube-dns` address.

To check the status of NodeLocal DNSCache, run the following command:
    
    
    kubectl get cm -n kube-system node-local-dns -o json | jq .data.Corefile -r | grep bind
    

The output is similar to the following:
    
    
        bind 169.254.20.10 x.x.x.10
        bind 169.254.20.10 x.x.x.10
    
    

If GKE Dataplane V2 is enabled on the cluster and the cluster uses `kube-dns`, NodeLocal DNSCache runs in an isolated network and is configured to listen on all Pod IP addresses (0.0.0.0). The output is similar to the following:
    
    
        bind 0.0.0.0
        bind 0.0.0.0
    
    

After the cluster is updated to Cloud DNS, the NodeLocal DNSCache configuration is changed. To check the NodeLocal DNSCache configuration, run the following command:
    
    
    kubectl get cm -n kube-system node-local-dns -o json | jq .data.Corefile -r | grep bind
    

The output is similar to the following:
    
    
        bind 169.254.20.10
        bind 169.254.20.10
    

The following workflow explains the entries in the `resolv.conf` file both before and after migration and node re-creation:

#### Before migration

  * Pods have the `resolv.conf` file configured to the `kube-dns` IP address (for example, `x.x.x.10`).
  * NodeLocal DNSCache Pods intercept DNS requests from Pods and listen on the following: 
    * (DPv1) both addresses (bind 169.254.20.10 x.x.x.10).
    * (DPv2) all Pod IP addresses (bind 0.0.0.0).
  * NodeLocal DNSCache works as a cache and minimal load is put on `kube-dns` Pods.



#### After migration

  * After the control plane is updated to use Cloud DNS, the Pods still have the `resolv.conf` file configured to the `kube-dns` IP address (for example, `x.x.x.10`). Pods retain this `resolv.conf` configuration until their node is re-created. When Cloud DNS with NodeLocal DNSCache is enabled, Pods must be configured to use `169.254.20.10` as the name server, but this change applies only to Pods on nodes that were created or re-created after the migration to Cloud DNS.
  * NodeLocal DNSCache Pods listen on the NodeLocal DNSCache address only (bind 169.254.20.10). Requests don't go to NodeLocal DNSCache Pods.
  * All requests from Pods are directly sent to `kube-dns` Pods. This setup generates high traffic on the Pods.



#### After node re-creation or node pool upgrade

  * Pods have the `resolv.conf` file configured to use the NodeLocal DNSCache IP address (169.254.20.10).
  * NodeLocal DNSCache Pods listen on the NodeLocal DNSCache address only (bind 169.254.20.10) and receive DNS requests from Pods on this IP address.



When node pools use the `kube-dns` IP address in the `resolv.conf` file before the node pool is re-created, an increase in DNS query traffic also increases traffic on the `kube-dns` Pods. This increase can cause intermittent failure of DNS requests. To minimize errors, you must plan this migration during downtime periods.

## What's next

  * [Configure Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).
  * [Use NodeLocal DNSCache in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).
  * [Troubleshoot GKE DNS](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
