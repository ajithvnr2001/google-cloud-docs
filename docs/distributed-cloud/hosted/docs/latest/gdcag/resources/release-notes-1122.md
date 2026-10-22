---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1122/
title: Google Distributed Cloud air-gapped 1.12.2 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:22.286158+00:00
---

# Google Distributed Cloud air-gapped 1.12.2 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1122/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.12.2 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## April 5, 2024

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.12.2 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Security

Updated Rocky Linux OS image version to 20240306 to apply the latest security patches and important updates. The following security vulnerabilities are fixed: 

  * [CVE-2023-28486](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28486)
  * [CVE-2023-28487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28487)
  * [CVE-2023-42465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42465)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2018-1099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1099)



* * *

Security

Fixed a vulnerability with Microsoft Visual Studio Code in Operations Suite Infrastructure (OI) by updating Microsoft Visual Studio Code to version 1.86.2.

* * *

Security

Fixed multiple vulnerabilities with Google Chrome in Operations Suite Infrastructure (OI) by updating to version 122.0.6261.69.

* * *

Security

Fixed the vulnerabilities related to the prebuilt Ubuntu OS.

* * *

Security

Updated the `gcr.io/distroless/libc` base image to digest `sha256:4f834e207f2721977094aeec4c9daee7032c5daec2083c0be97760f4306e4f88` to apply the latest security patches and important updates.

* * *

Issue

**Cluster management** :

  * User clusters with Kubernetes version 1.27.x might have node pools that fail to initialize. 
  * The required IPv4 PodCIDR is not available. 



**File and block storage** :

  * When upgrading from 1.11.1 to 1.12.2, the `file-netapp-trident` subcomponent rollout might fail. 



**Firewall** :

  * `bm-system-machine-init` is failing on the first node. Default IDPS firewall policies don't support the organization custom IPs for the Direct Connect (DX) Interconnect. 



**Hardware security module (HSM)** :

  * A rotatable secret for hardware security modules is in an unknown state. 



**Lower networking** :

  * Network switches preloaded with version lower than 9.3.10 may fail to bootstrap. 
  * Some connections to the `org-admin` node time out. 



**Networking** :

  * GDC fails to create switch ACLs from traffic policies during the initial bootstrapping process. 



**NTP server** :

  * The Node OS has unsynchronized time. 



**Object storage** :

  * Object storage buckets might not be ready after root org upgrade. 



**Monitoring** :

  * [Configuring the ServiceNow webhook](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/install-30/sn-webhooks) results in Lifecycle Management (LCM) re-reconciling and reverting the changes made to the `ConfigMap` object `mon-alertmanager-servicenow-webhook-backend` and the `Secret` object `mon-alertmanager-servicenow-webhook-backend` in the `mon-system` namespace. 
  * The `mon-common` subcomponent doesn't deploy the Istio Telemetry object on the `mon-system` namespace. 
  * The metrics storage class is incorrectly defined in the configuration. 
  * The `mon-prober-backend-prometheus-config` ConfigMap gets reset to include no probe jobs, and alert `MON-A0001` is triggered. 



**Physical servers** :

  * A `NodePool` has a server in unknown state during creation. 
  * The node firmware upgrade fails on an org. 



**System artifact registry** :

  * The job service pod is not ready. 



**Ticketing system** :

  * The ticketing system knowledge base sync fails. 
  * The ticketing system has no healthy upstream. 



**Vertex AI** :

  * The `MonitoringTarget` shows a `Not Ready` status when user clusters are being created, causing pre-trained APIs to continually show an `Enabling` state in the user interface. 



**Virtual machines** :

  * The importer pods are failing or stuck. 
  * Virtual machine disks might take a long time to provision. 
  * VMRuntime might not be ready due to network-controller-manager installation failure. 



**Upgrade** :

**Upgrade** :

  * The `unet-nodenetworkpolicy-infra` subcomponent fails during upgrade. 
  * System cluster fails during upgrade from 1.11.x to 1.12.2. 
  * The `file-observability` subcomponent fails on the `org-1-system-cluster` when upgrading from 1.11.x to 1.12.2. 
  * The `HSMupgrade` fails when upgrading from 1.11.x to 1.12.2. 
  * Loki pods are stuck in a terminating state for more than 1.5 hours when upgrading from 1.11.x to 1.12.2. 
  * SSH for a VM with management IP and the cilium logs fails when upgrading from 1.11.x to 1.12.2. 
  * The object storage upgrade shows an error during the postflight or preflight check. 
  * The `mz-etcd` subcomponent updates `spec.deployTarget` and `spec.Namespace` causing the upgrade from 1.11.x to 1.12.x to fail. 
  * An NTP `OSPolicy` failure blocks all other `OSPolicies` from running. 



* * *

Fixed

**Cluster management** :

  * Fixed the issue with the namespace deletion operation getting stuck in the `Terminating` state when deleting a user cluster.



**Logging** :

  * Fixed the issue with Loki instances not collecting audit logs and operational logs.
  * Fixed the issue with `ValidatingWebhookConfiguration`, `MutatingWebhookConfiguration`, and `MonitoringRule` resources deployed by the Log component failing to upgrade from 1.11.x to 1.12.x. 
  * Fixed the issue with Kubernetes API server logs not being forwarded to an external SIEM destination when [enabling logs export](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/export-logs-external). 



**Monitoring** :

  * Fixed the issue with the Cortex bucket deletion failure when upgrading from 1.11.x to 1.12.2.



**NTP server** : 

  * Fixed an issue with the NTP relay server pod crash looping.




**Physical servers** :

  * Fixed the issue where servers were stuck in the `Inspecting` phase during bootstrap.



**Upgrade** :

  * Fixed the issue when OS in-place node upgrade might stop responding.
  * Fixed the issue with user cluster upgrades being blocked due to a reconciling error.



**Volume backup and restore** :

  * Fixed the issue that prevented volume backups from resolving org buckets.



* * *

Change

**Add-on Manager** : 

  * The Google Distributed Cloud version is updated to 1.28.300-gke.131 to apply the latest security patches and important updates. 

See the [Google Distributed Cloud 1.28.300-gke.131 release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver-1#release_128300-gke131) for details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
