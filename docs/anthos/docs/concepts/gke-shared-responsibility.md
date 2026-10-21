---
url: https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility/
title: GKE shared responsibility \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:06.732342+00:00
---

# GKE shared responsibility  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  GKE shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains the shared security responsibilities for both Google and Google Cloud customers. Running a business-critical application on Google Kubernetes Engine (GKE) requires multiple parties to have different responsibilities. Although this document is not an exhaustive list, this document can help you understand your responsibilities.

This document is for Security specialists who define, govern and implement policies and procedures to protect an organization's data from unauthorized access. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

### Google's responsibilities

  * Protecting the underlying infrastructure, including hardware, firmware, kernel, OS, storage, network, and more. This includes [encrypting data at rest by default](https://docs.cloud.google.com/docs/security/encryption/default-encryption), providing [additional customer-managed disk encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek), [encrypting data in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit), using [custom-designed hardware](https://docs.cloud.google.com/docs/security/titan-hardware-chip), laying [private network cables](https://cloud.google.com/about/locations/#network-tab), protecting data centers from physical access, protecting the bootloader and kernel against modification using [Shielded Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes), and following secure software development practices.
  * [Hardening](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security) and [patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching) the nodes' operating system, such as Container-Optimized OS or Ubuntu. GKE promptly makes any patches to these images available. If you have auto-upgrade enabled, or are using a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), these updates are automatically deployed. This is the OS layer underneath your container—it's not the same as the operating system running in your containers.
  * Building and operating threat detection for container-specific threats into the kernel with [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) (priced separately with Security Command Center).
  * Hardening and [patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching) Kubernetes node components. All GKE managed components are upgraded automatically when you upgrade GKE node versions. This includes: 
    * [vTPM-backed trusted bootstrap mechanism for issuing kubelet TLS certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) and auto-rotation of the certificates
    * Hardened kubelet configuration [following CIS benchmarks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks)
    * GKE metadata server for [Workload identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
    * GKE's native [Container Network Interface plugin and Calico for NetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
    * GKE Kubernetes storage integrations such as the [CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver)
    * GKE [logging and monitoring agents](https://docs.cloud.google.com/stackdriver/docs/solutions/gke)
  * Hardening and [patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching) the control plane. The control plane includes the control plane VM, API server, scheduler, controller manager, [cluster CA, TLS certificate issuance and rotation, root-of-trust key material](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-trust), IAM authenticator and authorizer, audit logging configuration, etcd, and various other controllers. All of your control plane components run on Google-operated Compute Engine instances. These instances are single tenant, meaning each instance runs the control plane and its components for only one customer.
  * Provide Google Cloud integrations for Connect, Identity and Access Management, Cloud Audit Logs, Google Cloud Observability, Cloud Key Management Service, Security Command Center, and others.
  * Restrict and log Google administrative access to customer clusters for contractual support purposes with [Access Transparency](https://cloud.google.com/access-transparency).



### Customer's responsibilities

  * Maintain your workloads, including your application code, build files, container images, data, Role-based access control (RBAC)/IAM policy, and containers and pods that you are running.
  * [Rotate your clusters credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#overview).
  * Keep Standard node pools enrolled in [automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades).
  * In the following situations, manually upgrade your clusters and node pools to remediate vulnerabilities within your organization's patching timelines: 
    * Auto-upgrades are postponed because of factors like maintenance policies.
    * You need to apply a patch before it becomes available in your selected release channel. For more information, see [Run patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).
  * Monitor the cluster and applications and respond to any alerts and incidents using technologies such as the [security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) and [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs).
  * Provide Google with environmental details when requested for troubleshooting purposes.
  * Ensure Logging and Monitoring are enabled on clusters. _If you don't enable Logging and Monitoring, and if support personnel can't access those logs, support is available on a best-effort basis_.



## What's next

  * Read the GKE [Security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
