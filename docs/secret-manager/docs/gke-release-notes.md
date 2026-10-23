---
url: https://docs.cloud.google.com/secret-manager/docs/gke-release-notes/
title: Secret Manager GKE integration release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:11.023794+00:00
---

# Secret Manager GKE integration release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/gke-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secret-manager/docs/resources)



Send feedback 

#  Secret Manager GKE integration release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Secret Manager integration with Google Kubernetes Engine (GKE), which includes the following components:

  * [**Secret Manager add-on**](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component): A managed GKE add-on that mounts secrets stored in Secret Manager as volumes directly into Kubernetes Pods. The add-on is derived from the open source Kubernetes Secrets Store CSI Driver and the Google Secret Manager provider.
  * [**Kubernetes Secret Sync**](https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets): A controller that automatically synchronizes secrets stored in Secret Manager into native Kubernetes Secret objects.



You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/secret-manager-gke-release-notes.xml) directly. 

## June 25, 2026

Change

### GKE 1.36.0-gke.4447000 and later

GKE version 1.36.0-gke.4447000 and later include the following updates for the Secret Manager integration.

#### Secret Manager add-on

**Changed**

  * Added support to read service account tokens from the CSI `serviceAccountTokenInSecrets` field for compatibility with Kubernetes 1.35 and later.



**Bug fixes**

  * Corrected log formatting when volume target path modification timestamps are absent.



**Security patches**

  * Remediated Go standard library vulnerabilities CVE-2025-68121, CVE-2026-25679, CVE-2026-32281, CVE-2026-32288, and CVE-2026-32289.
  * Remediated OpenTelemetry SDK vulnerability CVE-2026-24051.
  * Remediated network dependency vulnerability GO-2026-4918.
  * Remediated liveness probe vulnerability CVE-2026-33186.



#### Kubernetes Secret Sync

**Security patches**

  * Remediated Go standard library vulnerabilities CVE-2025-68121, CVE-2026-25679, CVE-2026-32281, CVE-2026-32288, and CVE-2026-32289.
  * Remediated OpenTelemetry SDK vulnerability CVE-2026-24051.
  * Remediated network dependency vulnerability GO-2026-4918.



### GKE 1.35.5-gke.1163012 and later

GKE version 1.35.5-gke.1163012 and later include the following updates for the Secret Manager integration.

#### Secret Manager add-on

**Changed**

  * Added support to connect to Secret Manager through an HTTP or HTTPS proxy to allow secret retrieval in environments with strict egress controls.
  * Improved secret Security Health Analytics (SHA) generation logic for auto-rotated volume contents.



**Security patches**

  * Remediated Go standard library vulnerabilities CVE-2025-22874 and CVE-2025-22871.
  * Remediated network dependency vulnerability CVE-2025-22872 (`golang.org/x/net`).



#### Kubernetes Secret Sync

**Changed**

  * Improved error classification in Secret Sync to detect server-side apply conflicts (such as when another controller or user attempts to modify a managed secret) and explicitly report them as user configuration conflicts in the resource status.
  * Reduced log verbosity when you use Fleet Workload Identity to minimize log noise in cluster logs.



**Bug fixes**

  * Updated Secret Sync to automatically recreate synchronized Kubernetes Secrets if they are deleted from the cluster to maintain the synchronization state.



**Security patches**

  * Remediated Go standard library vulnerabilities CVE-2025-22871, CVE-2025-22874, and CVE-2025-68121.
  * Remediated network dependency vulnerability CVE-2025-22872 (`golang.org/x/net`) in the provider.



### GKE 1.34.8-gke.1000000 and later

GKE version 1.34.8-gke.1000000 and later include the following updates for the Secret Manager integration.

#### Secret Manager add-on

**Changed**

  * Reduced log verbosity during Workload Identity token retrieval when `fleetWorkloadIdentity` is enabled to minimize log noise.
  * Added error messages to driver logs when Workload Identity authentication calls fail.



**Security patches**

  * Remediated Go standard library vulnerabilities CVE-2026-33811, CVE-2026-27142, and CVE-2025-61725.



### GKE 1.33.12-gke.1116000 and later

GKE version 1.33.12-gke.1116000 and later include the following updates for the Secret Manager integration.

#### Secret Manager add-on

**Security patches**

  * Remediated network dependency vulnerabilities CVE-2025-22870 and CVE-2024-45338 (`golang.org/x/net`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
