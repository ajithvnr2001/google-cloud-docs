---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade/
title: Upgrading Apigee hybrid to version 1.16 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:53.210641+00:00
---

# Upgrading Apigee hybrid to version 1.16  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.16 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/upgrade.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/upgrade.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/upgrade.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/upgrade.html)



This procedure covers upgrading from Apigee hybrid version 1.15.x to Apigee hybrid version 1.16.11 and from previous releases of hybrid 1.16.x to version 1.16.11. 

Use the same procedures for minor version upgrades (for example version 1.15 to 1.16) and for patch release upgrades (for example 1.16.0 to 1.16.11). 

If you are upgrading from Apigee hybrid version 1.14 or older, you must first upgrade to hybrid version 1.15 before upgrading to version 1.16.11. See the instructions for [Upgrading Apigee hybrid to version 1.15](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade). 

## Changes from Apigee hybrid v1.15

Please note the following changes: 

  * **Seccomp profiles** : Starting in [version 1.16](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1160), Apigee hybrid now offers the capability to apply Seccomp Profiles to your runtime components, significantly enhancing the security posture of your deployment. This feature allows Apigee administrators and security teams to restrict the system calls a containerized process can make to the host's kernel. By limiting a container to only the necessary syscalls, you can: 
    * Enhance Security: Mitigate the risk of container breakouts and privilege escalation.
    * Enforce Least Privilege: Ensure components only have access to the exact system calls required for their operation.
    * Meet Compliance: Provide a critical control for meeting stringent security compliance requirements.
For more information, see [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles). 
  * **UDCA in Apigee hybrid removal** : In Apigee hybrid [version 1.16](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1160), the Unified Data Collection Agent (UDCA) component has been removed. The responsibilities of sending analytics, trace, and deployment status data to the Apigee control plane are now handled using a [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) based data pipeline. Using the Pub/Sub based data pipeline has been the default data collection mechanism since Apigee hybrid [version 1.14.0](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1140). 
  * **`apigee-guardrails` service account**: In v1.16.0, Apigee Hybrid introduces an `apigee-guardrails` Google IAM service account. This is used by the `apigee-operator` chart during installation to check that all needed APIs are enabled in your project. 

See:

    * [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/guardrails)
    * [About service accounts: `apigee-guardrails`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#apigee-guardrails)
    * [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/create-service-account)
    * [Installation Part 2: Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts)
    * [Installation Part 2: Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication)
  * **Support for cert-manager release 1.18 and 1.19** : Apigee hybrid v1.16 supports cert-manager [release 1.18](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18) and [release 1.19](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19). In cert-manager release 1.18, there is a change to the default value of `Certificate.Spec.PrivateKey.rotationPolicy` that can impact traffic. If you are upgrading from a previous version of Apigee hybrid, and you are uprading to cert-manager release 1.18 or above, follow the Upgrade cert-manager prodedure in this guide. **Note:** This does not affect fresh installations of Apigee hybrid v1.6.



For additional information about features in Hybrid version 1.16, see the [Apigee hybrid v1.16.11 release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v11611).

## Prerequisites

Before upgrading to hybrid version 1.16, make sure your installation meets the following requirements: 

  * If your hybrid installation is running a version older than v1.15, you must upgrade to version 1.15 before upgrading to v1.16. See [Upgrading Apigee hybrid to version 1.15](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade). 
  * Helm version v3.14.2+.
  * `kubectl`: A supported version of `kubectl` appropriate for your Kubernetes platform version. See [Supported platforms and versions: `kubectl`](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#kubectl).
  * cert-manager: A supported version of cert-manager. See [Supported platforms and versions: cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#cert-manager). If needed, you will upgrade cert-manager in the Prepare to upgrade to version 1.16 section below.



##  Before you upgrade to 1.16.11 - limitations and important notes 

  * Apigee hybrid 1.16.11 introduces a new enhanced per-environment proxy limit that lets you deploy more proxies and shared flows in a single environment. See [Limits: API Proxies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#api-proxies) to understand the limits on the number of proxies and shared flows you may deploy per environment. This feature is available only on newly created hybrid organizations, and cannot be applied to upgraded orgs. To use this feature, perform a fresh installation of hybrid 1.16.11, and create a new organization. 

This feature is available exclusively as part of the [2024 subscription plan](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements), and is subject to the entitlements granted under that subscription. See [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits) to learn more about this feature.

  * Upgrading to Apigee hybrid version 1.16 may require downtime.

When upgrading the Apigee controller to version 1.16.11, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends that once you begin the upgrade, you should upgrade all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.15 cannot be used to restore a Hybrid 1.16 instance.

  * Management plane changes do not need to be fully suspended during an upgrade. Any required temporary suspensions to management plane changes are noted in the upgrade instructions below.




##  Upgrading to version 1.16.11 overview 

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade. 
  2. Install hybrid runtime version 1.16.11.



##  Prepare to upgrade to version 1.16 

###  Back up your hybrid installation 

  1. These instructions use the environment variable APIGEE_HELM_CHARTS_HOME for the directory in your file system where you have installed the Helm charts. If needed, change directory into this directory and define the variable with the following command: 

###  Linux 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Mac OS 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Windows 
         
         set APIGEE_HELM_CHARTS_HOME=%CD%
         echo %APIGEE_HELM_CHARTS_HOME%

  2. Make a backup copy of your version 1.15 `$APIGEE_HELM_CHARTS_HOME/` directory. You can use any backup process. For example, you can create a `tar` file of your entire directory with: 
         
         tar -czvf **$APIGEE_HELM_CHARTS_HOME** /../apigee-helm-charts-v1.15-backup.tar.gz **$APIGEE_HELM_CHARTS_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview). 
  4. Make sure that your TLS certificate and key files (`.crt`, `.key`, and/or `.pem`) reside in the `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/` directory. 



###  Upgrade your Kubernetes version 

Check your Kubernetes platform version and if needed, upgrade your Kubernetes platform to a version that is supported by both hybrid 1.15 and hybrid 1.16. Follow your platform's documentation if you need help. 

#### _Click to expand a list of supported platforms_

### Supported versions

| 1.14 | 1.15 | 1.16 | 1.17  
---|---|---|---|---  
GKE on Google Cloud |  1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  |  1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  |  1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  |  1.33.x   
1.34.x   
1.35.x   
1.36.x   
Google Distributed Cloud (software only) on VMware (3) | 1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.33.x   
1.34.x   
1.35.x   
1.36.x   
Google Distributed Cloud (software only) on bare metal | 1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.33.x   
1.34.x   
1.35.x   
1.36.x   
EKS | 1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.33.x   
1.34.x   
1.35.x   
1.36.x   
AKS | 1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.34.x   
1.35.x   
1.36.x   
OpenShift(7) | 4.13   
4.14   
4.15   
4.16   
4.17   
4.18   
4.19(≥ v1.14.4)(11)   
4.20(≥ v1.14.4)(11)   
4.21(≥ v1.14.4)(11)   
4.22(≥ v1.14.4)(11) | 4.16   
4.17   
4.18   
4.19(≥ v1.15.2)(10)   
4.20(≥ v1.15.2)(10)   
4.21(≥ v1.15.2)(10)   
4.22(≥ v1.15.2)(10) | 4.16   
4.18   
4.19   
4.20   
4.21   
4.22  | 4.20   
4.21   
4.22   
Rancher Kubernetes Engine (RKE) |  v1.27.x   
1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  |  v1.28.x   
1.29.x   
1.30.x   
1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.31.x   
1.32.x   
1.33.x   
1.34.x   
1.35.x   
1.36.x  | 1.33.x   
1.34.x   
1.35.x   
1.36.x   
  
### Components

| 1.14 | 1.15 | 1.16 | 1.17  
Cloud Service Mesh |  1.22.x(2) |  1.22.x(2) |  1.22.x(2) |  1.22.x(2)  
JDK |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 17  
cert-manager |  1.15.x(8)  
1.16.x(8)  
1.17.x(8) |  1.16.x(8)  
1.17.x(8) |  1.16.x(8)  
1.17.x(8)  
1.18.x(9)  
1.19.x(9) |  1.17.x(8)  
1.18.x(9)  
1.19.x(9)  
Cassandra |  4.0 |  4.0 |  4.0 |  4.0  
Kubernetes | 1.28.x  
1.29.x  
1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.29.x  
1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.33.x  
1.34.x  
1.35.x  
1.36.x  
kubectl | 1.28.x  
1.29.x  
1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.29.x  
1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.30.x  
1.31.x  
1.32.x  
1.33.x  
1.34.x  
1.35.x  
1.36.x | 1.33.x  
1.34.x  
1.35.x  
1.36.x  
Helm | 3.14.2 through 3.x.x | 3.14.2 through 3.x.x | 3.17.0 through 3.x.x | 3.17.0 through 3.x.x  
Secret Store CSI driver | 1.4.6+ | 1.4.6+ | 1.4.6+ | 1.4.6+  
Vault | 1.17.2 | 1.17.2 | 1.17.2 | 1.19.0+  
**(1) The official EOL dates for Apigee hybrid versions 1.13 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(2) Cloud Service Mesh is automatically installed with Apigee hybrid 1.9 and newer**.  **(3) Vault is not certified on Google Distributed Cloud for VMware. ** **(4) Support available with Apigee hybrid version 1.10.5 and newer**.  **(5) Support available with Apigee hybrid version 1.11.2 and newer**.  **(6) Support available with Apigee hybrid version 1.12.1 and newer**.  **(7) Apigee hybrid is tested and certified on OpenShift using the Kubernetes version bundled with each specific OCP version**.  **(8) Some versions of cert-manager have an issue where the webhook TLS server may fail to automatically renew its CA certificate.** To avoid this, Apigee recommends using: 

  * **Hybrid v1.13![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg) :** use cert-manager version [1.15.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15/#v1155)+. 
  * **Hybrid v1.14:** use cert-manager versions [1.15.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15/#v1155)\+ or [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)+. 
  * **Hybrid v1.15:** use cert-manager versions [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)\+ or [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+. 
  * **Hybrid v1.16:** use cert-manager versions [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)+, [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+, [1.18.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#v1180)\+ or [1.19.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19/#v1190)+. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for cert-manager releases 1.18 and 1.19. 
  * **Hybrid v1.17:** use cert-manager versions [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+, [1.18.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#v1180)\+ or [1.19.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19/#v1190)+. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for cert-manager releases 1.18 and 1.19. 

**(9) cert-manager release 1.18 introduces a change to the default private key rotation policy that may cause traffic interruptions. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for a workaround.** **(10) Support for OpenShift 4.19, 4.20, 4.21, & 4.22 available with Apigee hybrid version 1.15.2 and newer.** **(11) Support for OpenShift 4.19, 4.20, 4.21, & 4.22 available with Apigee hybrid version 1.14.4 and newer.**  
**Note:** Hybrid installations are not currently supported on Autopilot clusters. 

### Unsupported versions

|  1.6 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) |  1.7 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) |  1.8 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.9 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.10 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.11 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.12 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.13 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1)  
---|---|---|---|---|---|---|---|---  
GKE on Google Cloud | 1.19.x  
1.20.x  
1.21.x | 1.20.x   
1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.21.x (≤ 1.8.3)   
1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)  
1.24.x (≥ 1.8.4)  
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x (≥ 1.9.2) | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)(8) | 1.27.x   
1.28.x   
1.29.x   
1.30.x   
Google Distributed Cloud (software only) on VMware (3) | 1.7.x  
1.8.x  
1.9.3+  
1.10.x | 1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3)(≥ 1.7.2)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(≥ 1.7.2) | 1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x   
1.14.x   
1.15.x (K8s v1.26.x)  | 1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x   
1.14.x   
1.15.x (K8s v1.26.x)  | 1.13.x   
1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x   
1.29.x(≥ 1.12.1)(8) | 1.16.x (K8s v1.27.x)   
1.28.x   
1.29.x   
1.30.x   
Google Distributed Cloud (software only) on bare metal | 1.7.x  
1.8.2+  
1.9.3+  
1.10.x | 1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(≥ 1.7.2)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(≥ 1.7.2) | 1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x   
1.14.x   
1.15.x  | 1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x   
1.14.x   
1.15.x  | 1.13.x   
1.14.x (K8s v1.25.x)   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x   
1.29.x(≥ 1.12.1)(8) | 1.16.x (K8s v1.27.x)   
1.28.x   
1.29.x   
1.30.x   
EKS | 1.19.x  
1.20.x  
1.21.x | 1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)  
1.24.x (≥ 1.8.4)  
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x  | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)(8) | 1.27.x   
1.28.x   
1.29.x   
1.30.x   
AKS | 1.19.x  
1.20.x  
1.21.x | 1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)  
1.24.x (≥ 1.8.4)  
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x(≥ 1.9.2) | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)(8) | 1.27.x   
1.28.x   
1.29.x   
1.30.x   
OpenShift(7) | 4.6  
4.7  
4.8 | 4.7   
4.8  | 4.8   
4.9   
4.10  | 4.10   
4.11  | 4.11   
4.12   
4.14(≥ 1.10.5)(6)   
4.15(≥ 1.10.5)(6) | 4.12   
4.13   
4.14   
4.15(≥ 1.11.2)(7)   
4.16(≥ 1.11.2)(7) | 4.12   
4.13   
4.14   
4.15   
4.16(≥ 1.12.1)(8) | 4.12   
4.13   
4.14   
4.15   
4.16   
Rancher Kubernetes Engine (RKE) |  N/A |  N/A |  N/A |  1.3.8 |  v1.26.2+rke2r1   
1.27.x(≥ 1.10.5)(6)   
1.28.x(≥ 1.10.5)(6) |  v1.26.2+rke2r1   
v1.27.x   
1.28.x(≥ 1.11.2)(7)   
1.29.x(≥ 1.11.2)(7) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x(≥ 1.12.1)(8) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x   
1.30.x   
  
### Components

| 1.6 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.7 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.8 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.9 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.10![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.11![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.12![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1) | 1.13 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(1)  
Cloud Service Mesh |  1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg) |  1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(≥ 1.7.2)  
1.14.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.15.x (≥ 1.7.6) |  1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.14.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.15.x  |  1.17.x(2) |  1.17.x(2) |  1.17.x(v1.11.0 - v1.11.1)(2)   
1.18.x(≥ 1.11.2)(7)(2) |  1.18.x(2) |  1.19.x(2)  
JDK |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11  
cert-manager |  1.5.4 |  1.7.x |  1.7.x   
1.8.x   
1.9.x   
1.10.x   
1.11.x  |  1.10.x   
1.11.x |  1.10.x  
1.11.x  
1.12.x  |  1.11.x  
1.12.x  
1.13.x  |  1.11.x  
1.12.x  
1.13.x  |  1.15.x(8)  
1.16.x(8)  
1.17.x(8)  
Cassandra |  3.11 |  3.11 |  3.11 |  3.11 |  3.11 |  3.11 |  4.0 |  4.0  
Kubernetes |  |  |  | 1.23.x  
1.24.x  
1.25.x  
| 1.24.x  
1.25.x  
1.26.x  
| 1.25.x  
1.26.x  
1.27.x  
| 1.26.x  
1.27.x  
1.28.x  
1.29.x | 1.27.x  
1.28.x  
1.29.x  
1.30.x  
kubectl |  |  |  |  | 1.24.x  
1.25.x  
1.26.x | 1.25.x  
1.26.x  
1.27.x | 1.26.x  
1.27.x  
1.28.x  
1.29.x | 1.27.x  
1.28.x  
1.29.x  
1.30.x  
Helm |  |  |  |  | 3.10+ | 3.10+ | 3.14.2 through 3.x.x | 3.14.2 through 3.x.x  
Secret Store CSI driver |  |  |  |  |  | 1.3.4+ | 1.4.1+ | 1.4.6+  
Vault |  |  |  |  |  | 1.13.x | 1.15.2 | 1.15.2  
**(1) The official EOL dates for Apigee hybrid versions 1.13 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(2) Cloud Service Mesh is automatically installed with Apigee hybrid 1.9 and newer**.  **(3) Vault is not certified on Google Distributed Cloud for VMware. ** **(4) Support available with Apigee hybrid version 1.10.5 and newer**.  **(5) Support available with Apigee hybrid version 1.11.2 and newer**.  **(6) Support available with Apigee hybrid version 1.12.1 and newer**.  **(7) Apigee hybrid is tested and certified on OpenShift using the Kubernetes version bundled with each specific OCP version**.  **(8) Some versions of cert-manager have an issue where the webhook TLS server may fail to automatically renew its CA certificate.** To avoid this, Apigee recommends using: 

  * **Hybrid v1.13![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg) :** use cert-manager version [1.15.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15/#v1155)+. 
  * **Hybrid v1.14:** use cert-manager versions [1.15.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15/#v1155)\+ or [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)+. 
  * **Hybrid v1.15:** use cert-manager versions [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)\+ or [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+. 
  * **Hybrid v1.16:** use cert-manager versions [1.16.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)+, [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+, [1.18.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#v1180)\+ or [1.19.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19/#v1190)+. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for cert-manager releases 1.18 and 1.19. 
  * **Hybrid v1.17:** use cert-manager versions [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+, [1.18.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#v1180)\+ or [1.19.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19/#v1190)+. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for cert-manager releases 1.18 and 1.19. 

**(9) cert-manager release 1.18 introduces a change to the default private key rotation policy that may cause traffic interruptions. See [Known Issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046) for a workaround.** **(10) Support for OpenShift 4.19, 4.20, 4.21, & 4.22 available with Apigee hybrid version 1.15.2 and newer.** **(11) Support for OpenShift 4.19, 4.20, 4.21, & 4.22 available with Apigee hybrid version 1.14.4 and newer.**  
**Note:** Hybrid installations are not currently supported on Autopilot clusters. 

### Pull the Apigee Helm charts.

Apigee hybrid charts are hosted in [Google Artifact Registry](https://docs.cloud.google.com/artifact-registry):

`oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts`

Using the `pull` command, copy all of the Apigee hybrid Helm charts to your local storage with the following command: 
    
    
    export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
    export **CHART_VERSION** =1.16.11
    helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-env --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
    helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
    

### Edit `kustomization.yaml` for a custom apigee namespace

If your Apigee namespace is not `apigee`, edit the `apigee-operator/etc/crds/default/kustomization.yaml` file and replace the `namespace` value with your Apigee namespace.
    
    
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    
    namespace: APIGEE_NAMESPACE
    

If you are using `apigee` as your namespace you do not need to edit the file. 

* Install the updated Apigee CRDs: **Note:** From this step onwards, all commands should be run under the chart repo root directory. **Note:** This is the only supported method for installing Apigee CRDs. Do not use `kubectl apply` without `-k`, do not omit `--server-side`. **Note:** This step requires elevated cluster permissions. 

  1. Use the `kubectl` dry-run feature by running the following command:
         
         kubectl apply -k  apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false --dry-run=server
         

  2. After validating with the dry-run command, run the following command:
         
         kubectl apply -k  apigee-operator/etc/crds/default/ \
           --server-side \
           --force-conflicts \
           --validate=false
         

  3. Validate the installation with the `kubectl get crds` command: 
         
         kubectl get crds | grep apigee

Your output should look something like the following:
         
         apigeedatastores.apigee.cloud.google.com                    2024-08-21T14:48:30Z
         apigeedeployments.apigee.cloud.google.com                   2024-08-21T14:48:30Z
         apigeeenvironments.apigee.cloud.google.com                  2024-08-21T14:48:31Z
         apigeeissues.apigee.cloud.google.com                        2024-08-21T14:48:31Z
         apigeeorganizations.apigee.cloud.google.com                 2024-08-21T14:48:32Z
         apigeeredis.apigee.cloud.google.com                         2024-08-21T14:48:33Z
         apigeerouteconfigs.apigee.cloud.google.com                  2024-08-21T14:48:33Z
         apigeeroutes.apigee.cloud.google.com                        2024-08-21T14:48:33Z
         apigeetelemetries.apigee.cloud.google.com                   2024-08-21T14:48:34Z
         cassandradatareplications.apigee.cloud.google.com           2024-08-21T14:48:35Z
         



* Check the labels on the cluster nodes. By default, Apigee schedules data pods on nodes with the label `cloud.google.com/gke-nodepool=apigee-data` and runtime pods are scheduled on nodes with the label `cloud.google.com/gke-nodepool=apigee-runtime`. You can customize your node pool labels in the `overrides.yaml` file. 

For more information, see [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes). 

### Set up the `apigee-guardrails` service account

Starting with hybrid v1.16, the `apigee-guardrails` service account is required to upgrade the `apigee-operator` chart. 

In the following procedure, select the type of service account authentication you are using.

  1. Verify you can execute `create-service-account`. If you have just downloaded the charts the `create-service-account` file might not be in an executable mode. In your APIGEE_HELM_CHARTS_HOME directory run the following command: 
         
         ./apigee-operator/etc/tools/**create-service-account --help**

If your output says `permission denied` you need to make the file executable, for example with `chmod` in Linux, MacOS, or UNIX or in the Windows Explorer or with the `icacls` command in Windows. For example: 
         
         chmod +x ./apigee-operator/etc/tools/**create-service-account**

  2. Create the `apigee-guardrails` service account: 

### Kubernetes Secrets
         
         ./apigee-operator/etc/tools/create-service-account \
           --env prod \
           --profile apigee-guardrails \
           --dir service-accounts

This command creates the `apigee-guardrails` service account and downloads the key to the `service-accounts/` directory.

### JSON files
         
         ./apigee-operator/etc/tools/create-service-account \
           --env prod \
           --profile apigee-guardrails \
           --dir ./apigee-operator/

This command creates the `apigee-guardrails` service account and downloads the key to the `apigee-operator/` chart directory. 

### Vault
         
         ./apigee-operator/etc/tools/create-service-account \
           --env prod \
           --profile apigee-guardrails \
           --dir service-accounts

This command creates the `apigee-guardrails` service account and downloads the key to the `service-accounts/` directory.

### WIF for GKE
         
         ./apigee-operator/etc/tools/create-service-account \
           --env prod \
           --profile apigee-guardrails \
           --dir service-accounts

This command creates the `apigee-guardrails` service account and downloads the key to the `apigee-operator/etc/tools/service-accounts/` directory. You do not need the downloaded key file and can delete it.

### WIF on other platforms
         
         ./apigee-operator/etc/tools/create-service-account \
           --env prod \
           --profile apigee-guardrails \
           --dir service-accounts

This command creates the `apigee-guardrails` service account and downloads the key to the `service-accounts/` directory.

  3. Set up authentication for the `apigee-guardrails` service account: 

### Kubernetes Secrets

Create the Kubernetes secret using the `apigee-guardrails` service account key file in the `service-accounts/` directory:
         
         kubectl create secret generic apigee-guardrails-svc-account \
             --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-guardrails.json" \
             -n $APIGEE_NAMESPACE

Add the following to your `overrides.yaml` file:
         
         guardrails:
           serviceAccountRef: apigee-guardrails-svc-account

### JSON files

Add the following to your `overrides.yaml` file, using the path to the `apigee-guardrails` service account key file in the `apigee-operator/` directory:
         
         guardrails:
           serviceAccountPath: $PROJECT_ID-apigee-guardrails.json

### Vault

     1. Update the Vault secret `secret/data/apigee/orgsakeys` to add a `guardrails` entry with the contents of the `apigee-guardrails` service account key file. 
            
            vault kv patch secret/apigee/orgsakeys guardrails="$(cat ./service-accounts/hybrid115-apigee-guardrails.json)"
            

     2. The Kubernetes service account (KSA) for guardrails is named `apigee-operator-guardrails-sa`. Add the Guardrails KSA to the organization-specific service accounts bound to the `apigee-orgsakeys` role in Vault. 
        1. Get the current list of KSAs bindings: 
               
               vault read auth/kubernetes/role/apigee-orgsakeys
               

The output should be in the following format:
               
               Key                                         Value
               ---                                         -----
               alias_name_source                           serviceaccount_uid
               bound_service_account_names                 BOUND_SERVICE_ACCOUNT_NAMES
               bound_service_account_namespace_selector    n/a
               bound_service_account_namespaces            APIGEE_NAMESPACE

In the output, `BOUND_SERVICE_ACCOUNT_NAMES` is a list of comma-separated service account names. Add `apigee-operator-guardrails-sa` to the list of names. for example (without the newlines added for readability):
               
               apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
               apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
               rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
               assandra-user-setup-myhybridorg-5b044c1,apigee-mart-myhybridorg-5b0
               44c1,apigee-mint-task-scheduler-myhybridorg-5b044c1,apigee-connect-
               agent-myhybridorg-5b044c1,apigee-watcher-myhybridorg-5b044c1,apigee
               -metrics-apigee-telemetry,apigee-open-telemetry,apigee-synchronizer
               -myhybridorg-dev-ee52aca,apigee-runtime-telemetry-collector-apigee-
               telemetry,apigee-logger-apigee-e-myhybrridorg-dev-ee52aca,apigee-sy
               nchronizer-myhybridog-prod-2d0221c,apigee-runtime-myhybridorg-prod-
               2d0221c,**apigee-operator-guardrails-sa**

        2. Update the bindings to the `apigee-orgsakeys` role with the updated list of service account names: 
               
               vault write auth/kubernetes/role/apigee-orgsakeys \
                 bound_service_account_names=UPDATED_BOUND_SERVICE_ACCOUNT_NAMES \
                 bound_service_account_namespaces=APIGEE_NAMESPACE \
                 policies=apigee-orgsakeys-auth \
                 ttl=1m
               

     3. Add "guardrails" to the `SecretProviderClass`
        1. Edit your `spc-org.yaml` file. **Tip:** If you are need to recreate it, use the template in [Storing service account keys in Hashicorp Vault: Create `SecretProviderClass` objects](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault#create-secretproviderclass-objects).
        2. Under `spec.parameters.objects`, add a guardrails entry: 
               
               - objectName: "guardrails"
                       secretPath: ""
                       secretKey: ""

**Tip:** For scripted environments or to automate this change, you can use the command-line YAML processor [`yq`](https://github.com/mikefarah/yq). 

**Command:** To add the "guardrails" entry to `spc-org.yaml` in-place, use the following command:
               
               yq -i '.spec.parameters.objects |= (
                   from_yaml + [
                       {
                           "objectName": "guardrails",
                           "secretPath": "",
                           "secretKey": ""
                       }
                   ] | to_yaml
               )' spc-org.yaml

This command parses the embedded YAML string in the `objects` field, adds the new item to the list, and then writes the result back.

        3. Update your `SecretProviderClass`: 
               
               kubectl -n APIGEE_NAMESPACE apply -f spc-org.yaml
               

### WIF for GKE

**Note:** Although granting Identity and Access Management (IAM) roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Apigee hybrid requires IAM service account impersonation because the hybrid Helm charts (`*.gsa` properties in `overrides.yaml`) and control plane synchronization APIs require IAM service account email addresses.

The Kubernetes service account (KSA) for guardrails is named `apigee-operator-guardrails-sa`. Create the binding for the `apigee-guardrails` Google service account (GSA) with the following command:
    
    gcloud iam service-accounts add-iam-policy-binding apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
        --role roles/iam.workloadIdentityUser \
        --member "serviceAccount:$PROJECT_ID.svc.id.goog[$APIGEE_NAMESPACE/apigee-operator-guardrails-sa]" \
        --project $PROJECT_ID

Add the following to your `overrides.yaml` file:
    
    guardrails:
      gsa: apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com

### WIF on other platforms

The Kubernetes service account (KSA) for guardrails is named `apigee-operator-guardrails-sa`. You need to grant the guardrails KSA access to impersonate the `apigee-guardrails` Google service account (GSA), and configure your overrides to use a credential configuration file.

     1. Grant the KSA access to impersonate the GSA with the following command: 

### Template
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
              --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/system:serviceaccount:APIGEE_NAMESPACE:apigee-operator-guardrails-sa" \
              --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-guardrails@my-project.iam.gserviceaccount.com \
              --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-operator-guardrails-sa" \
              --role=roles/iam.workloadIdentityUser

Where:

        * `PROJECT_ID`: your Google Cloud project ID.
        * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where you created the workload identity pool.
        * `POOL_ID`: the workload identity pool ID.
        * `APIGEE_NAMESPACE`: The namespace where Apigee hybrid is installed.
     2. Create a credential configuration file for the `apigee-guardrails` service account: 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=apigee-guardrails-credential-configuration.json
                

Where `WORKLOAD_PROVIDER_ID` is your workload identity pool provider ID.

     3. Configure `apigee-guardrails` to use Workload Identity Federation with one of the following methods: 

### WIF: secrets

        1. Create a new Kubernetes secret using the credential source file for each credential configuration file. 
               
               kubectl create secret -n APIGEE_NAMESPACE generic guardrails-workload-identity-secret --from-file="client_secret.json=./apigee-guardrails-credential-configuration.json"

        2. Replace the value of `serviceAccountRef` with the new secret: 
               
               guardrails:
                 serviceAccountRef: guardrails-workload-identity-secret

### WIF: files

Move the generated `apigee-guardrails-credential-configuration.json` file to your `apigee-operator/` chart directory.

Add the following to your `overrides.yaml` file:
    
    guardrails:
      serviceAccountPath: apigee-guardrails-credential-configuration.json

### WIF: Vault

Update the service account key for `guardrails` in Vault with the corresponding credential source file: 
    
    SAKEY=$(cat .apigee-guardrails-credential-configuration.json); kubectl -n APIGEE_NAMESPACE exec vault-0 -- vault kv patch secret/apigee/orgsakeys guardrails="$SAKEY"

See [`Storing service account keys in Hashicorp Vault`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault) for more information.




###  Upgrade cert-manager 

**Note:** This procedure is optional if you are using cert-manager 1.16.3 or higher. 

Apigee hybrid v1.16 supports cert-manager releases 1.16 through 1.19. There is a change in cert-manager 1.18 that can cause an issue with your traffic. In cert-manager release 1.18, the default value of `Certificate.Spec.PrivateKey.rotationPolicy` was changed from `Never` to `Always`. For upgraded Apigee hybrid installations, this can cause an issue with your traffic. When upgrading to hybrid v1.16 from an earlier version, you must either edit your `apigee-ca` certificate to compensate for this change or keep your version of cert-manager at release 1.17.x or lower. 

**Note:** This change affects upgrades from earlier versions of Apigee hybrid only and does not affect fresh installations of Apigee hybrid v1.16. 

Before upgrading cert-manager to 1.18 or 1.19, use the following steps procedure to edit your `apigee-ca` certificate to set the value of `Certificate.Spec.PrivateKey.rotationPolicy` to `Never`. 

**Warning:** Performe these steps _before_ upgrading cert-manager. Otherwise, you may trigger a certificate rotation. **Note:** For multi-region deployments, the following change to the `apigee-ca` certificate only needs to be made in the primary region. If there is no `apigee-ca` certificate, skip this procedure for clusters in secondary regions. 

  1. Check the contents of your `apigee-ca` certificate to see if `rotationPolicy` is set: **Tip:** If you are using a custom cert-manager namesspace, replace `cert-manager` with the correct namespace in the following commands.
         
         kubectl get certificate apigee-ca -n cert-manager -o yaml
         

Look for the values under `spec.privateKey` in the output:
         
         ...
         **spec:**
           commonName: apigee-hybrid
           duration: 87600h
           isCA: true
           issuerRef:
             group: cert-manager.io
             kind: ClusterIssuer
             name: apigee-root-certificate-issuer
           **privateKey:**
             algorithm: ECDSA
             **# Note: rotationPolicy would appear here if it is set.**
             size: 256
           secretName: apigee-ca
         ...

  2. If `rotationPolicy` is not set or if it is set to `Always`, edit the `apigee-ca` certificate to set the value of `rotationPolicy` to `Never`: 
     1. Perform a dry run first: 
            
            kubectl patch Certificate \
              --dry-run=server \
              -n cert-manager \
              --type=json \
              -p='[{"op": "replace", "path": "/spec/privateKey/rotationPolicy", "value": "Never"}]' \
              -o=yaml \
              apigee-ca
            

     2. Patch the certificate: 
            
            kubectl patch Certificate \
              -n cert-manager \
              --type=json \
              -p='[{"op": "replace", "path": "/spec/privateKey/rotationPolicy", "value": "Never"}]' \
              -o=yaml \
              apigee-ca
            

  3. Verify that the value of `rotationPolicy` is now set to `Never`: 
         
         kubectl get certificate apigee-ca -n cert-manager -o yaml
         

The output should look similar to the following:
         
         ...
         **spec:**
           commonName: apigee-hybrid
           duration: 87600h
           isCA: true
           issuerRef:
             group: cert-manager.io
             kind: ClusterIssuer
             name: apigee-root-certificate-issuer
           **privateKey:**
             algorithm: ECDSA
             **rotationPolicy: Never**
             size: 256
           secretName: apigee-ca
         ...

  4. Upgrade cert-manager. The following command will download and install cert-manager v1.19.2: 
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.19.2/cert-manager.yaml

See [Supported platforms and versions: cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#cert-manager) for a list of supported versions.




See:

  * [Known issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046)
  * [cert-manager Release 1.18: The default value of `Certificate.Spec.PrivateKey.rotationPolicy` is now `Always`](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#the-default-value-of-certificatespecprivatekeyrotationPolicy-is-now-always)



##  Install the hybrid 1.16.11 runtime 

**Caution:** Do not create new environments during the upgrade process.This upgrade procedure assumes you are using the same namespace and service accounts for the upgraded installation. If you are making any configuration changes, be sure to reflect those changes in your overrides file before installing the Helm charts.**Note:** Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run` at the end of the command. See `helm -h` to list supported commands, options, and usage. 

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Upgrade the Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm upgrade -h` for details.

Dry run:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify Apigee Operator installation:
         
         helm ls -n APIGEE_NAMESPACE
         
         
         NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                   APP VERSION
         operator   apigee   3          2024-08-21 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.16.11   1.16.11
         

Verify it is up and running by checking its availability:
         
         kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
         
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-controller-manager   1/1     1            1           7d20h
         

  3. Upgrade the Apigee datastore: 

Dry run:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify `apigeedatastore` is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeedatastore default
         
         
         NAME      STATE       AGE
         default   running    2d

  4. Upgrade Apigee telemetry: 

Dry run:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
         
         
         NAME               STATE     AGE
         apigee-telemetry   running   2d

  5. Upgrade Apigee Redis: 

Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   2d

  6. Upgrade Apigee ingress manager: 

Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its availability:
         
         kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           2d

  7. Upgrade the Apigee organization: 

Dry run:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking the state of the respective org:
         
         kubectl -n APIGEE_NAMESPACE get apigeeorg
         
         
         NAME                      STATE     AGE
         apigee-my-org-my-env      running   2d

**Note** : If the upgrade command fails with the error `Forbidden: state: releasing`, the existing components are still in releasing status. You can wait for the current update to complete and then retry. Check release status with the following command: 
         
         kubectl get org -n APIGEE_NAMESPACE

  8. Upgrade the environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME.

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

     * ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.
     * ENV_NAME is the name of the environment you are upgrading.
     * OVERRIDES_FILE is your new overrides file for v.1.16.11

Upgrade the chart:
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE
    

Verify it is up and running by checking the state of the respective env:
    
    kubectl -n APIGEE_NAMESPACE get apigeeenv
    
    
    NAME                          STATE       AGE   GATEWAYTYPE
    apigee-my-org-my-env          running     2d

**Note** : If the upgrade command fails with the error `Forbidden: state: releasing`, the existing components are still in releasing status. You can wait for the current update to complete and then retry. Check release status with the following command: 
    
    kubectl get env -n APIGEE_NAMESPACE

  9. Upgrade the environment groups (`virtualhosts`). 
     1. You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each environment group mentioned in the overrides.yaml file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. It is usually ENV_GROUP_NAME.

Upgrade the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE
            

**Note:** ENV_GROUP_RELEASE_NAME must be unique within the `apigee` namespace. 

For example, if you have an _environment_ named `prod` and an _environment group_ named `prod`, set the value of ENV_GROUP_RELEASE_NAME to something unique, like `prod-envgroup`. 

     2. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls environment group-related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2d
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                        STATE     AGE
            apigee-org1-dev-egroup-123abc               running   2d

  10. After you have verified all the installations are upgraded successfully, delete the older `apigee-operator` release from the `apigee-system` namespace. 
     1. Uninstall the old `operator` release: 
            
            helm delete operator -n apigee-system
            

     2. Delete the `apigee-system` namespace: 
            
            kubectl delete namespace apigee-system
            

  11. Upgrade `operator` again in your Apigee namespace to re-install the deleted cluster-scoped resources: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         


**Congratulations!** You have upgraded to Apigee hybrid version 1.16.11. To test your upgrade, call a proxy against the new installation. For an example, see [Part 3, Step 2: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-deploy-proxy) in the Apigee hybrid 1.16 installation guide. 

##  Rolling back to a previous version 

To roll back to the previous version, use the older chart version to roll back the upgrade process in the reverse order. Start with `apigee-virtualhost` and work your way back to `apigee-operator`, and then revert the CRDs. 

**Tip:** If you know the last release version, you can use the `helm rollback` command rather than the `helm upgrade` command described below.

  1. Revert the charts. The following commands assume you are using the charts from the previous version (v1.15.x). 
     1. Run the following command for each environment group:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=ENV_GROUP_NAME \
              -f 1.15_OVERRIDES_FILE
            

     2. Run the following command for each environment:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=ENV_NAME \
              -f 1.15_OVERRIDES_FILE
            

     3. `apigee-org`:
            
            helm upgrade ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

     4. `apigee-ingress-manager`:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

     5. `apigee-redis`:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

     6. `apigee-telemetry`:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

     7. `apigee-datastore`:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

     8. `apigee-operator`:
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f 1.15_OVERRIDES_FILE
            

  2. Revert the CRDs by reinstalling the older CRDs. 
         
         kubectl apply -k apigee-operator/etc/crds/default/ \
           --server-side \
           --force-conflicts \
           --validate=false
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
