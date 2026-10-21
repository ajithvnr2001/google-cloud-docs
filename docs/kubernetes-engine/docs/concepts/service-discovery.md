---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery/
title: Service discovery and DNS \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:13:54.944153+00:00
---

# Service discovery and DNS  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Service discovery and DNS Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how Google Kubernetes Engine (GKE) implements service discovery and cluster DNS.

## Service discovery

In Kubernetes, service discovery is implemented with automatically generated service names that map to the Service's IP address. Service names follow a [standard specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md): as follows: `my-svc.my-namespace.svc.cluster.local`. Pods can also access external services through their names, such as `example.com`. For more information about how DNS works in Kubernetes, see [DNS for Services and Pods](https://github.com/kubernetes/dns/blob/master/docs/specification.md).

## Cluster DNS in GKE

New Autopilot clusters use Cloud DNS and you can't modify the DNS provider.

For Standard, GKE provides the following cluster DNS options to resolve service names and external names:

  * kube-dns: a cluster add-on that is deployed by default in all GKE clusters.
  * Cloud DNS: a cloud-managed cluster DNS infrastructure that leverages [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) and does not require managing in-cluster DNS servers such as kube-dns.



You can also register your services with Service Directory for GKE.

GKE also provides NodeLocal DNSCache as an optional add-on that can be used with kube-dns or Cloud DNS.

### kube-dns

kube-dns is the default DNS provider for Standard clusters and the only DNS provider for Autopilot clusters running versions earlier than 1.25.9-gke.400 and 1.26.4-gke.500.

kube-dns runs as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) that schedules kube-dns pods to nodes in the cluster.

To learn more about kube-dns, see [About kube-dns for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns).

### Cloud DNS

Cloud DNS is the only DNS provider for Autopilot clusters running version 1.25.9-gke.400 and later, and version 1.26.4-gke.500 and later.

Cloud DNS provides Pod and Service DNS resolution without a cluster-hosted DNS provider like kube-dns. The Cloud DNS controller automatically provisions DNS records for pods and services in Cloud DNS for ClusterIP, headless and external name services.

To learn how to configure Cloud DNS, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).

### NodeLocal DNSCache

NodeLocal DNSCache runs as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) that schedules a DNS cache Pod on every cluster node. This DNS cache improves DNS lookup latency, makes DNS lookup times more consistent, and can reduce the number of DNS queries to kube-dns or Cloud DNS.

To learn how to configure NodeLocal DNSCache, see [Setting up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).

## Service discovery outside a single cluster

You can configure service discovery beyond the scope of a single cluster using one of the following methods.

### Cloud DNS VPC scope

A cluster that uses Cloud DNS for cluster DNS must operate in one of two available modes: GKE cluster scope or Virtual Private Cloud (VPC) scope.

When you configure a cluster in cluster scope, DNS records are only resolvable within the cluster using the schema `<svc>.<ns>.svc.cluster.local`. This is the same behavior as kube-dns.

When you configure a cluster in VPC scope, DNS records for cluster services are resolvable within the entire VPC. This means that clients in the same VPC or connected to the VPC through Cloud VPN or Cloud Interconnect can directly resolve the DNS records for Services in the GKE cluster. You can also configure unique cluster DNS names so that non-GKE clients can resolve DNS records. For example, a non-GKE client could resolve `gke-svc.ns.svc.cluster1` from `gke-svc.ns.svc.cluster2`.

To learn more about VPC scope DNS, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#vpc_scope_dns).

### Multi-cluster Services

Multi-cluster Services provides multi-cluster service discovery and load balancing for GKE that leverages the existing Service object. Multi-cluster Services are discoverable and accessible across any GKE cluster with a single virtual IP address. This is the same behavior as a ClusterIP Service that is accessible in a single cluster.

Multi-cluster Services aggregates service across clusters and makes them addressable as a single multi-cluster DNS record using the schema `<svc>.<ns>.svc.clusterset.local`. This provides a unique name for a given service that is consistent and addressable from any GKE cluster using multi-cluster Services.

To learn more about Multi-cluster Services, see [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services).

### Service Directory for GKE

Service Directory for GKE provides a single view of services across all of your Kubernetes deployments. Service Directory can register both GKE and non-GKE services in a single registry. Service Directory is particularly useful if you want:

  * A single registry for Kubernetes and non-Kubernetes applications to discover each other.
  * A managed service discovery tool.
  * To store metadata about your service that can be accessed by other clients.
  * To set access permissions on a per-service level.



Service Directory services can be resolved via DNS, HTTP, and gRPC. Service Directory is integrated with Cloud DNS, and can populate Cloud DNS records that match services in Service Directory.

To learn more, see [Configuring Service Directory for GKE](https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke).

## `/etc/resolv.conf`

For Pods using [`ClusterFirst` DNS Policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy), the value of `/etc/resolv.conf` depends on which features are enabled on the cluster:

Cloud DNS for GKE | NodeLocal DNSCache | `/etc/resolv.conf` value  
---|---|---  
Enabled | Enabled | `169.254.20.10`  
Enabled | Disabled | `169.254.169.254`  
Disabled | Enabled | kube-dns service IP address  
Disabled | Disabled | kube-dns service IP address  
  
## What's next

  * Learn how to [use Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).
  * Learn more about [kube-dns for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns).
  * Learn how to [set up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).
  * Learn how to [set up a custom kube-dns Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-kube-dns).
  * Learn more about [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
