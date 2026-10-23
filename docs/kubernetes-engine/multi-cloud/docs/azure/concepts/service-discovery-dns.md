---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/service-discovery-dns/
title: Service discovery and DNS overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:39.721306+00:00
---

# Service discovery and DNS overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/service-discovery-dns/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service discovery and DNS overview

This topic describes how GKE on Azure interacts with Domain Name Services (DNS).

## Service discovery

Service discovery is the process where workloads discover services without knowing the service's IP address. This section describes how GKE on Azure implements service discovery and managed DNS.

Kubernetes automatically generates service names that use the following [specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md):

`service.namespace.svc.cluster.local`

Where:

  * `service`: your service's name
  * `namespace`: your service's Namespace



Workloads also access external services— for example `example.net`— using DNS names. For more information on the behavior of DNS in Kubernetes, see [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

### CoreDNS

GKE on Azure uses [CoreDNS](https://kubernetes.io/blog/2018/07/10/coredns-ga-for-kubernetes-cluster-dns/) to resolve DNS names within clusters. CoreDNS runs as a redundant, scaled [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in the `kube-system` namespace. The CoreDNS deployment has a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) that groups the CoreDNS Pods and gives them a single IP address. The CoreDNS Deployment scales with the cluster's size and usage.

### NodeLocal DNSCache

GKE on Azure uses [NodeLocal DNSCache](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/) to improve DNS lookup performance. NodeLocal DNSCache runs as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) on each node in your cluster. When a Pod makes a DNS request, the request first goes to the DNS cache on the same node. If the cache can't resolve the DNS request, the cache forwards the request to either:

  * CoreDNS for an internal name— for example `foo.bar.svc.cluster.local`



## What's next

  * For an overview of how DNS is used in Kubernetes clusters, see [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
