---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshoot-networking/
title: Troubleshoot GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:26.798352+00:00
---

# Troubleshoot GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshoot-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot GKE networking Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page lists troubleshooting pages for common issues you might encounter when using Google Kubernetes Engine (GKE) networking. This page is for Admins and architects, Security specialists, Networking specialists, or Storage specialists who troubleshoot GKE configurations. To learn more about GKE roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Topic | Description  
---|---  
[Cluster connectivity](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/connectivity-issues-in-cluster) | Troubleshoot network connectivity, including issues with Pod network connectivity.  
[IP address management in VPC clusters](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vpc-clusters) | Troubleshoot managing IP addresses in VPC-native clusters, including issues with subnet exhaustion and default SNAT.  
[Kube-dns in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns) | Learn to identify the source of kube-dns issues by investigating things like the `/etc/resolv.conf` file and network policies. Also learn how to resolve common issues like intermittent DNS timeouts.  
[Cloud DNS in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns) | Learn to identify the source of Cloud DNS issues in GKE by doing things like verifying basic settings and investigating logs. Also learn how to resolve errors such as API rate limits or insufficient quota.  
[Cluster network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-isolation) | Troubleshoot cluster network isolation, including issues with cluster creation, control plane access, VPC Network Peering, and connectivity to public resources.  
[Load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing) | Troubleshoot load balancing, including issues with BackendConfig, Ingress security policies, 500 series errors with NEGs, and internal Ingress.  
[Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops) | Troubleshoot `MultiClusterIngress` and `MultiClusterService` resources, including issues with VIPs, 502 responses, and config cluster migration.  
[Cloud NAT packet loss from a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-nat-packet-loss) | Troubleshoot packet loss from Cloud NAT in clusters with private nodes, including how to use Cloud Logging and Cloud Monitoring to identify the cause of packet loss.  
  
## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for advice about how to contact Cloud Customer Care, use community resources, and use the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers) to open bugs or feature requests.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
