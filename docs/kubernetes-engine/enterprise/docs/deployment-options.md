---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options/
title: GKE deployment options \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:36.454036+00:00
---

# GKE deployment options  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  GKE deployment options Stay organized with collections  Save and categorize content based on your preferences. 

This page shows the Google Cloud features that are available on each of the following environments:

  * [Google Kubernetes Engine (GKE) on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs)
  * Google Distributed Cloud (GKE on-premises): 
    * [On VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem)
    * [On bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest)
    * [Google Distributed Cloud connected deployments](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview)
  * GKE Multi-Cloud: 
    * [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws)
    * [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure)
    * [GKE attached clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached), which are third-party Kubernetes clusters registered to your [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).



This page is for Operators who define IT solutions and system architecture in accordance with company strategy in coordination with key stakeholders. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Enable GKE and related features

This section describes how to enable the features that are described on this page.

### Enable GKE

To enable GKE, enable the GKE API.

[Enable GKE API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

Enabling this API gives you access to the GKE, which includes the following features:

  * [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview)
  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller)
  * [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview)
  * [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs/getting-started)
  * [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet)
  * [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#default-logs-enterprise) and [Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#default-metrics-enterprise) for GKE system components
  * [Security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)
  * [Node to node encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption)
  * [FQDN network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies)



### Enable related products and features

To use the following products and features with GKE, you must enable each of these features individually. For more information, see the following links.

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling)
  * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress)



See the following pricing guides for detailed information about how these products and features are billed.

  * [Cloud Service Mesh](https://cloud.google.com/service-mesh/pricing)
  * [Binary Authorization](https://cloud.google.com/binary-authorization/pricing)
  * [Multi Cluster Ingress](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress)



## Features available on GKE clusters on Google Cloud

To use some features, you must register the cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). You can see which features require fleets in the following table.

A small number of features aren't supported on [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview). These are also shown in the table.

**Feature** | **Available on GKE standard clusters** | **Available on Autopilot clusters** | **Available without fleet membership**  
---|---|---|---  
Config Sync |  |  |   
Policy Controller |  |  |   
Config Controller |  |  |   
Cloud Service Mesh in-cluster |  |  |   
Managed Cloud Service Mesh |  |  |   
Knative serving |  |  |   
Migrate to Containers |  |  |   
GKE Identity Service |  |  |   
Binary Authorization |  |  |   
Multi Cluster Ingress |  |  |   
Cloud Logging and Cloud Monitoring for GKE system components |  |  |   
Advanced security posture and compliance monitoring |  |  |   
Node to node encryption |  |  |   
FQDN network policies |  |  |   
  
## Features available on clusters outside of Google Cloud

The following tables show which key Google Cloud and GKE features are available on clusters outside of Google Cloud.

For more information about which versions of the features are supported on each environment, see the [version support matrix](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support).

### Plugins and load balancers

GKE clusters outside of Google Cloud use a combination of built-in GKE capabilities along with platform-native capabilities.

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
Network plugin |  |  |  |  |  |   
Container storage interface (CSI) & hybrid storage |  |  |  |  |  |   
Bundled L4 load balancer |  |  |  |  |  |   
Platform-native load balancers | N/A | N/A |  |  |  | N/A  
  
### Operations and management

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | GDC (connected)  
---|---|---|---|---|---|---  
[ GKE dashboard in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) |  |  |  |  |  |   
[Connect Gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using) |  |  |  |  |  |   
[Cloud Logging and Cloud Monitoring ](https://docs.cloud.google.com/stackdriver/docs) |  |  |  |  |  |   
[ Prometheus/Grafana](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/concepts/logging-and-monitoring#prometheus_and_grafana) |  |  |  |  |  |   
  
### Security and Identity

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity) |  |  |  |  |  |   
[ Fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) |  |  |  |  |  |   
[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) |  |  |  |  |  |   
[Binary Authorization](https://docs.cloud.google.com/binary-authorization) |  |  |  |  |  |   
  
### Service management

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[ Cloud Service Mesh in-cluster](https://docs.cloud.google.com/service-mesh/docs/unified-install/prerequisites) |  |  |  |  | * |   
[Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh) |  |  |  |  |  |   
[Service dashboards in the Google Cloud console](https://docs.cloud.google.com/service-mesh/docs/observability/explore-dashboard) |  |  |  |  | * |   
[ Cloud Service Mesh certificate authority](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#mesh_ca) |  |  |  |  |  |   
[ Cloud Service Mesh integration with Certificate Authority Service](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#ca_service) |  |  |  |  |  |   
  
***** For the list of attached clusters that Cloud Service Mesh supports, see [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms). 

### Configuration management

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[ Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) |  |  |  |  | * |   
[ Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) |  |  |  |  |  |   
[ Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview) |  |  |  |  |  |   
  
***** To install Policy Controller, AKS clusters must not have the Azure Policy add-on.

### Application deployment

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[ Knative serving](https://docs.cloud.google.com/anthos/run/docs/architecture-overview) |  |  |  |  |  |   
[Google Cloud Marketplace](https://docs.cloud.google.com/marketplace) |  |  |  |  |  |   
  
### Application migration

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs/getting-started) |  |  |  |  |  |   
  
### VM management

**Feature** | **GDC (VMware)** | **GDC (bare metal)** | **GKE on AWS** | **GKE on Azure** | **Attached clusters** | **GDC (connected)**  
---|---|---|---|---|---|---  
[ VM Runtime on Google Distributed Cloud ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/overview) |  |  |  |  |  |   
  
## What's next

  * [Version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support)
  * [Managed Cloud Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp)
  * [In-cluster Cloud Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
