---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-descriptions/
title: Predefined role descriptions for AOs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:41.994233+00:00
---

# Predefined role descriptions for AOs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-descriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Predefined role descriptions for AOs Stay organized with collections  Save and categorize content based on your preferences. 

## Application Operator roles

An Application Operator (AO) is a member of the development team within the Platform Administrator (PA) organization. AOs interact with project-level resources. You can assign the following predefined roles to team members:

  * **Project IAM Admin:** Manages the IAM allow policies of projects.
  * **AI OCR Developer** : Access the Optical Character Recognition service to detect text in images.
  * **AI Speech Developer** : Access the Speech-to-Text service to recognize speech and transcribe audio.
  * **AI Translation Developer** : Access the Vertex AI Translation service to translate text.
  * **Artifact Management Admin** : Has admin access to resources in all Harbor projects in the project namespace.
  * **Artifact Management Editor** : Has read and write access to resources in all Harbor projects in the project namespace.
  * **Certificate Authority Service Admin** : Has access to manage certificate authorities and certificate requests in their project.
  * **Certificate Service Admin** : Has access to manage certificates and certificate issuers in their project.
  * **Dashboard Editor** : Has read and write access on `Dashboard` custom resources.
  * **Dashboard Viewer** : Has read-only access on `Dashboard` custom resources.
  * **Harbor Instance Admin** : Has full access to manage Harbor instances in a project.
  * **Harbor Instance Viewer** : Has read-only access to view Harbor instances in a project.
  * **Harbor Project Creator** : Has access to manage Harbor instance projects.
  * **K8s Network Policy Admin** : Manages network policies in Kubernetes clusters.
  * **LoggingRule Creator** : Creates `LoggingRule` custom resources in the project namespace.
  * **LoggingRule Editor** : Edits `LoggingRule` custom resources in the project namespace.
  * **LoggingRule Viewer** : Views `LoggingRule` custom resources in the project namespace.
  * **LoggingTarget Creator** : Creates `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget Editor** : Edits `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget Viewer** : Views `LoggingTarget` custom resources in the project namespace.
  * **Load Balancer Admin** : has read and write permissions on all load balancer resources in project namespace.
  * **MonitoringRule Editor** : Has read and write access to `MonitoringRule` resources.
  * **MonitoringRule Viewer** : Has read-only access to `MonitoringRule` custom resources.
  * **MonitoringTarget Editor** : Has read and write access to `MonitoringTarget` custom resources.
  * **MonitoringTarget Viewer** : Has read-only access to `MonitoringTarget` custom resources.
  * **NAT Viewer** : Has read-only access to deployments in Kubernetes clusters.
  * **Namespace Admin** : Manages all resources within the project namespace.
  * **ObservabilityPipeline Editor** : Has read and write access on `ObservabilityPipeine` custom resources.
  * **ObservabilityPipeline Viewer** : Has read-only access on `ObservabilityPipeline` custom resources.
  * **Project Bucket Admin** : Manages the storage buckets and objects within buckets.
  * **Project Bucket Object Admin** : Has read-only access on buckets within a project, and read-write access on the objects in those buckets.
  * **Project Bucket Object Viewer** : Has read-only access on buckets within a project and the objects in those buckets.
  * **Project Cortex Alertmanager Editor** : Grants permissions to edit the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Alertmanager Viewer** : Grants permissions to access the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Prometheus Viewer** : Grants permissions to access the Cortex Prometheus instance in the project namespace.
  * **Project Grafana Viewer** : Accesses the Grafana instance in the project namespace of the fleet admin cluster.
  * **Project NetworkPolicy Admin:** Manages the project network policies in the project namespace.
  * **Project Viewer:** Has read-only access to all resources within project namespaces.
  * **Project VirtualMachine Admin** : Manages VMs in the project namespace.
  * **Project VirtualMachine Image Admin** : Manages VM images in the project namespace.
  * **Secret Admin** : Manages Kubernetes secrets in projects.
  * **Secret Viewer** : Views Kubernetes secrets in projects.
  * **Service Configuration Admin** : Has read and write access to service configurations within a project namespace.
  * **Service Configuration Viewer** : Has read access to service configurations within a project namespace.
  * **Volume Replication Admin** : Manages volume replication resources.
  * **Workbench Notebooks Admin** : Get read and write access to all notebook resources within a project namespace.
  * **Workbench Notebooks Viewer** : Get read-only access to all notebook resources within a project namespace and view the Vertex AI Workbench user interface.
  * **Workload Viewer** : Has read access to workloads in a project.



## Common roles

The following predefined common roles apply to all authenticated users:

  * **AI Platform Viewer** : Grants permissions to view pre-trained services.
  * **DNS Suffix Viewer** : Accesses the domain name service (DNS) suffix config map.
  * **Flow Log Admin** : Has read and write access to all Flow Log resources.
  * **Flow Log Viewer** : Has read-only access to all Flow Log resources.
  * **Project Discovery Viewer** : Has read access for all authenticated users to the project view.
  * **Public Image Viewer** : Has read access for all authenticated users on the public VM images in the namespace `vm-images`.
  * **System Artifact Registry anthos-creds secret Monitor** : Has read-only access to secrets in the `anthos-creds` namespace.
  * **System Artifact Registry gpc-system secret Monitor** : Has read-only access to secrets in the `gpc-system` namespace.
  * **System Artifact Registry harbor-system secret Monitor** : Has read-only access to secrets in the `harbor-system` namespace.
  * **Virtual Machine Type Viewer** : Has read access to cluster-scoped virtual machine types.
  * **VM Type Viewer** : Has read access to the predefined virtual machine types on the admin clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
