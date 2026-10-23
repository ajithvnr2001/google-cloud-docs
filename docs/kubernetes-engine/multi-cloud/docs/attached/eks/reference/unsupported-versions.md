---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/unsupported-versions/
title: Unsupported Kubernetes cluster versions \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:40.086855+00:00
---

# Unsupported Kubernetes cluster versions  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/unsupported-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/api-permissions)



Send feedback 

#  Unsupported Kubernetes cluster versions Stay organized with collections  Save and categorize content based on your preferences. 

The following versions of GKE attached clusters are unsupported.

## Kubernetes 1.32

### 1.32.0-gke.3

  * **Breaking Change:** GKE attached clusters no longer validate that the `anthos.googleapis.com` service is enabled when creating or updating a cluster. Attached clusters are now included in the GKE Standard tier, so this validation is no longer required.

  * **Security Fixes**

    * Fixed [CVE-2025-12817](https://ubuntu.com/security/CVE-2025-12817)
    * Fixed [CVE-2025-12818](https://ubuntu.com/security/CVE-2025-12818)
    * Fixed [CVE-2025-9230](https://ubuntu.com/security/CVE-2025-9230)
    * Fixed [CVE-2025-9232](https://ubuntu.com/security/CVE-2025-9232)



### 1.32.0-gke.2

  * **Security Fixes**
    * Fixed [CVE-2025-32988](https://ubuntu.com/security/CVE-2025-32988)
    * Fixed [CVE-2025-32989](https://ubuntu.com/security/CVE-2025-32989)
    * Fixed [CVE-2025-32990](https://ubuntu.com/security/CVE-2025-32990)
    * Fixed [CVE-2025-3576](https://ubuntu.com/security/CVE-2025-3576)
    * Fixed [CVE-2025-4802](https://ubuntu.com/security/CVE-2025-4802)
    * Fixed [CVE-2025-6395](https://ubuntu.com/security/CVE-2025-6395)
    * Fixed [CVE-2025-8713](https://ubuntu.com/security/CVE-2025-8713)
    * Fixed [CVE-2025-8714](https://ubuntu.com/security/CVE-2025-8714)
    * Fixed [CVE-2025-8715](https://ubuntu.com/security/CVE-2025-8715)



### 1.32.0-gke.1

  * **Feature:** You can now customize Kubernetes labels and tolerations for Google-owned system components on your attached clusters. For more information see: 
    * [Customize system components on AKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/customize-system-components)
    * [Customize system components on EKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/customize-system-components)
    * [Customize system components on CNCF conformant clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/customize-system-components)
  * **Security Fixes**
    * Fixed [CVE-2023-4039](https://ubuntu.com/security/CVE-2023-4039)
    * Fixed [CVE-2024-13176](https://ubuntu.com/security/CVE-2024-13176)
    * Fixed [CVE-2024-26462](https://ubuntu.com/security/CVE-2024-26462)
    * Fixed [CVE-2025-0395](https://ubuntu.com/security/CVE-2025-0395)
    * Fixed [CVE-2025-1390](https://ubuntu.com/security/CVE-2025-1390)
    * Fixed [CVE-2025-24528](https://ubuntu.com/security/CVE-2025-24528)
    * Fixed [CVE-2025-31115](https://ubuntu.com/security/CVE-2025-31115)
    * Fixed [CVE-2025-4207](https://ubuntu.com/security/CVE-2025-4207)



## Kubernetes 1.31

### 1.31.0-gke.5

  * **Security Fixes**
    * Fixed [CVE-2025-32988](https://ubuntu.com/security/CVE-2025-32988)
    * Fixed [CVE-2025-32989](https://ubuntu.com/security/CVE-2025-32989)
    * Fixed [CVE-2025-32990](https://ubuntu.com/security/CVE-2025-32990)
    * Fixed [CVE-2025-3576](https://ubuntu.com/security/CVE-2025-3576)
    * Fixed [CVE-2025-4802](https://ubuntu.com/security/CVE-2025-4802)
    * Fixed [CVE-2025-6395](https://ubuntu.com/security/CVE-2025-6395)
    * Fixed [CVE-2025-8713](https://ubuntu.com/security/CVE-2025-8713)
    * Fixed [CVE-2025-8714](https://ubuntu.com/security/CVE-2025-8714)
    * Fixed [CVE-2025-8715](https://ubuntu.com/security/CVE-2025-8715)



### 1.31.0-gke.4

  * **Feature:** You can now customize Kubernetes labels and tolerations for Google-owned system components on your attached clusters. For more information see: 
    * [Customize system components on AKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/customize-system-components)
    * [Customize system components on EKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/customize-system-components)
    * [Customize system components on CNCF conformant clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/customize-system-components)
  * **Security Fixes**
    * Fixed [CVE-2023-4039](https://ubuntu.com/security/CVE-2023-4039)
    * Fixed [CVE-2024-13176](https://ubuntu.com/security/CVE-2024-13176)
    * Fixed [CVE-2024-26462](https://ubuntu.com/security/CVE-2024-26462)
    * Fixed [CVE-2025-0395](https://ubuntu.com/security/CVE-2025-0395)
    * Fixed [CVE-2025-1390](https://ubuntu.com/security/CVE-2025-1390)
    * Fixed [CVE-2025-24528](https://ubuntu.com/security/CVE-2025-24528)
    * Fixed [CVE-2025-31115](https://ubuntu.com/security/CVE-2025-31115)
    * Fixed [CVE-2025-4207](https://ubuntu.com/security/CVE-2025-4207)



### 1.31.0-gke.3

  * **Security Fixes**

    * Fixed [CVE-2020-13529](https://ubuntu.com/security/CVE-2020-13529)
    * Fixed [CVE-2021-33560](https://ubuntu.com/security/CVE-2021-33560)
    * Fixed [CVE-2022-4899](https://ubuntu.com/security/CVE-2022-4899)
    * Fixed [CVE-2023-5678](https://ubuntu.com/security/CVE-2023-5678)
    * Fixed [CVE-2024-0727](https://ubuntu.com/security/CVE-2024-0727)
    * Fixed [CVE-2024-12133](https://ubuntu.com/security/CVE-2024-12133)
    * Fixed [CVE-2024-12243](https://ubuntu.com/security/CVE-2024-12243)
    * Fixed [CVE-2024-2511](https://ubuntu.com/security/CVE-2024-2511)
    * Fixed [CVE-2024-4741](https://ubuntu.com/security/CVE-2024-4741)
    * Fixed [CVE-2024-5535](https://ubuntu.com/security/CVE-2024-5535)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [CVE-2025-1094](https://ubuntu.com/security/CVE-2025-1094)



### 1.31.0-gke.2

  * **Security Fixes**
    * Fixed [CVE-2024-10976](https://ubuntu.com/security/CVE-2024-10976)
    * Fixed [CVE-2024-10977](https://ubuntu.com/security/CVE-2024-10977)
    * Fixed [CVE-2024-10978](https://ubuntu.com/security/CVE-2024-10978)
    * Fixed [CVE-2024-10979](https://ubuntu.com/security/CVE-2024-10979)



### 1.31.0-gke.1

  * **Breaking Change:** GKE attached clusters validate that the following required services are enabled when creating or updating attached clusters: `anthos.googleapis.com`. For details, see [Google Cloud requirements](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/cluster-prerequisites#requirements).
  * **Feature:** The `gcloud beta container fleet memberships get-credentials` command uses a preview feature of the Connect gateway that lets you run the `kubectl port-forward` command. For more information, see [Limitations](https://cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#limitations) in the Connect gateway documentation.
  * **Feature:** Added the option to disable Cloud Monitoring. In the API, set `cluster.monitoring_config.cloud_monitoring_config.enabled` to `false` to disable Cloud Monitoring. Note that you can't use the Metrics Explorer when Cloud Monitoring is disabled.
  * **Security Fixes**
    * Fixed [CVE-2019-18276](https://ubuntu.com/security/CVE-2019-18276)
    * Fixed [CVE-2020-1751](https://ubuntu.com/security/CVE-2020-1751)
    * Fixed [CVE-2023-39318](https://ubuntu.com/security/CVE-2023-39318)
    * Fixed [CVE-2023-39319](https://ubuntu.com/security/CVE-2023-39319)
    * Fixed [CVE-2023-39323](https://ubuntu.com/security/CVE-2023-39323)
    * Fixed [CVE-2023-39325](https://ubuntu.com/security/CVE-2023-39325)
    * Fixed [CVE-2023-39326](https://ubuntu.com/security/CVE-2023-39326)
    * Fixed [CVE-2023-3978](https://ubuntu.com/security/CVE-2023-3978)
    * Fixed [CVE-2023-40577](https://ubuntu.com/security/CVE-2023-40577)
    * Fixed [CVE-2023-44487](https://ubuntu.com/security/CVE-2023-44487)
    * Fixed [CVE-2023-45142](https://ubuntu.com/security/CVE-2023-45142)
    * Fixed [CVE-2023-45285](https://ubuntu.com/security/CVE-2023-45285)
    * Fixed [CVE-2023-45288](https://ubuntu.com/security/CVE-2023-45288)
    * Fixed [CVE-2023-45918](https://ubuntu.com/security/CVE-2023-45918)
    * Fixed [CVE-2023-48795](https://ubuntu.com/security/CVE-2023-48795)
    * Fixed [CVE-2024-24557](https://ubuntu.com/security/CVE-2024-24557)
    * Fixed [CVE-2024-24786](https://ubuntu.com/security/CVE-2024-24786)
    * Fixed [CVE-2024-24789](https://ubuntu.com/security/CVE-2024-24789)
    * Fixed [CVE-2024-24790](https://ubuntu.com/security/CVE-2024-24790)
    * Fixed [CVE-2024-29018](https://ubuntu.com/security/CVE-2024-29018)
    * Fixed [CVE-2024-33599](https://ubuntu.com/security/CVE-2024-33599)
    * Fixed [CVE-2024-33600](https://ubuntu.com/security/CVE-2024-33600)
    * Fixed [CVE-2024-33601](https://ubuntu.com/security/CVE-2024-33601)
    * Fixed [CVE-2024-33602](https://ubuntu.com/security/CVE-2024-33602)
    * Fixed [CVE-2024-41110](https://ubuntu.com/security/CVE-2024-41110)
    * Fixed [CVE-2024-6104](https://ubuntu.com/security/CVE-2024-6104)
    * Fixed [GHSA-jq35-85cj-fj4p](https://github.com/advisories/GHSA-jq35-85cj-fj4p)
    * Fixed [GHSA-m425-mq94-257g](https://github.com/advisories/GHSA-m425-mq94-257g)



## Kubernetes 1.30

### 1.30.0-gke.7

  * **Feature:** You can now customize Kubernetes labels and tolerations for Google-owned system components on your attached clusters. For more information see: 
    * [Customize system components on AKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/customize-system-components)
    * [Customize system components on EKS clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/customize-system-components)
    * [Customize system components on CNCF conformant clusters](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/customize-system-components)
  * **Security Fixes**
    * Fixed [CVE-2023-4039](https://ubuntu.com/security/CVE-2023-4039)
    * Fixed [CVE-2024-13176](https://ubuntu.com/security/CVE-2024-13176)
    * Fixed [CVE-2024-26462](https://ubuntu.com/security/CVE-2024-26462)
    * Fixed [CVE-2025-0395](https://ubuntu.com/security/CVE-2025-0395)
    * Fixed [CVE-2025-1390](https://ubuntu.com/security/CVE-2025-1390)
    * Fixed [CVE-2025-24528](https://ubuntu.com/security/CVE-2025-24528)
    * Fixed [CVE-2025-31115](https://ubuntu.com/security/CVE-2025-31115)
    * Fixed [CVE-2025-4207](https://ubuntu.com/security/CVE-2025-4207)



### 1.30.0-gke.6

  * **Security Fixes**

    * Fixed [CVE-2020-13529](https://ubuntu.com/security/CVE-2020-13529)
    * Fixed [CVE-2021-33560](https://ubuntu.com/security/CVE-2021-33560)
    * Fixed [CVE-2022-4899](https://ubuntu.com/security/CVE-2022-4899)
    * Fixed [CVE-2023-5678](https://ubuntu.com/security/CVE-2023-5678)
    * Fixed [CVE-2024-0727](https://ubuntu.com/security/CVE-2024-0727)
    * Fixed [CVE-2024-12133](https://ubuntu.com/security/CVE-2024-12133)
    * Fixed [CVE-2024-12243](https://ubuntu.com/security/CVE-2024-12243)
    * Fixed [CVE-2024-2511](https://ubuntu.com/security/CVE-2024-2511)
    * Fixed [CVE-2024-4741](https://ubuntu.com/security/CVE-2024-4741)
    * Fixed [CVE-2024-5535](https://ubuntu.com/security/CVE-2024-5535)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [CVE-2025-1094](https://ubuntu.com/security/CVE-2025-1094)



### 1.30.0-gke.5

  * **Security Fixes**
    * Fixed [CVE-2024-10976](https://ubuntu.com/security/CVE-2024-10976)
    * Fixed [CVE-2024-10977](https://ubuntu.com/security/CVE-2024-10977)
    * Fixed [CVE-2024-10978](https://ubuntu.com/security/CVE-2024-10978)
    * Fixed [CVE-2024-10979](https://ubuntu.com/security/CVE-2024-10979)



### 1.30.0-gke.4

  * **Breaking Change:** GKE attached clusters validate that the following required services are enabled when creating or updating attached clusters: `cloudresourcemanager.googleapis.com`, `monitoring.googleapis.com`. For details, see [Google Cloud requirements](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/cluster-prerequisites#requirements).



### 1.30.0-gke.3

  * **Breaking Change:** GKE attached clusters validate that the following required services are enabled when creating or updating attached clusters: `gkeconnect.googleapis.com`, `gkehub.googleapis.com`, `kubernetesmetadata.googleapis.com`, `logging.googleapis.com`. For details, see [Google Cloud requirements](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/cluster-prerequisites#requirements).
  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-28834](https://ubuntu.com/security/CVE-2024-28834)
    * Fixed [CVE-2024-28835](https://ubuntu.com/security/CVE-2024-28835)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)
    * Fixed [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)



### 1.30.0-gke.2

  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-7348](https://ubuntu.com/security/CVE-2024-7348)



### 1.30.0-gke.1

  * **Security Fixes:**
    * Fixed [CVE-2024-0553](https://ubuntu.com/security/CVE-2024-0553)
    * Fixed [CVE-2024-0567](https://ubuntu.com/security/CVE-2024-0567)
    * Fixed [CVE-2024-37370](https://ubuntu.com/security/CVE-2024-37370)
    * Fixed [CVE-2024-37371](https://ubuntu.com/security/CVE-2024-37371)



## Kubernetes 1.29

### 1.29.0-gke.9

  * **Security Fixes**

    * Fixed [CVE-2020-13529](https://ubuntu.com/security/CVE-2020-13529)
    * Fixed [CVE-2021-33560](https://ubuntu.com/security/CVE-2021-33560)
    * Fixed [CVE-2022-4899](https://ubuntu.com/security/CVE-2022-4899)
    * Fixed [CVE-2023-5678](https://ubuntu.com/security/CVE-2023-5678)
    * Fixed [CVE-2024-0727](https://ubuntu.com/security/CVE-2024-0727)
    * Fixed [CVE-2024-12133](https://ubuntu.com/security/CVE-2024-12133)
    * Fixed [CVE-2024-12243](https://ubuntu.com/security/CVE-2024-12243)
    * Fixed [CVE-2024-2511](https://ubuntu.com/security/CVE-2024-2511)
    * Fixed [CVE-2024-4741](https://ubuntu.com/security/CVE-2024-4741)
    * Fixed [CVE-2024-5535](https://ubuntu.com/security/CVE-2024-5535)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [CVE-2025-1094](https://ubuntu.com/security/CVE-2025-1094)



### 1.29.0-gke.8

  * **Security Fixes**
    * Fixed [CVE-2024-10976](https://ubuntu.com/security/CVE-2024-10976)
    * Fixed [CVE-2024-10977](https://ubuntu.com/security/CVE-2024-10977)
    * Fixed [CVE-2024-10978](https://ubuntu.com/security/CVE-2024-10978)
    * Fixed [CVE-2024-10979](https://ubuntu.com/security/CVE-2024-10979)



### 1.29.0-gke.7

  * **Breaking Change:** GKE attached clusters validate that the following required services are enabled when creating or updating attached clusters: `cloudresourcemanager.googleapis.com`, `monitoring.googleapis.com`. For details, see [Google Cloud requirements](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/cluster-prerequisites#requirements).



### 1.29.0-gke.6

  * **Breaking Change:** GKE attached clusters validate that the following required services are enabled when creating or updating attached clusters: `gkeconnect.googleapis.com`, `gkehub.googleapis.com`, `kubernetesmetadata.googleapis.com`, `logging.googleapis.com`. For details, see [Google Cloud requirements](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/cluster-prerequisites#requirements).
  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-28834](https://ubuntu.com/security/CVE-2024-28834)
    * Fixed [CVE-2024-28835](https://ubuntu.com/security/CVE-2024-28835)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)
    * Fixed [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)



### 1.29.0-gke.5

  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-7348](https://ubuntu.com/security/CVE-2024-7348)



### 1.29.0-gke.4

  * **Security Fixes:**
    * Fixed [CVE-2024-0553](https://ubuntu.com/security/CVE-2024-0553)
    * Fixed [CVE-2024-0567](https://ubuntu.com/security/CVE-2024-0567)
    * Fixed [CVE-2024-37370](https://ubuntu.com/security/CVE-2024-37370)
    * Fixed [CVE-2024-37371](https://ubuntu.com/security/CVE-2024-37371)



### 1.29.0-gke.3

  * **Security Fixes:**
    * Fixed [CVE-2023-5981](https://ubuntu.com/security/CVE-2023-5981)
    * Fixed [CVE-2024-0985](https://ubuntu.com/security/CVE-2024-0985)
    * Fixed [CVE-2024-2961](https://ubuntu.com/security/CVE-2024-2961)
    * Fixed [CVE-2024-33599](https://ubuntu.com/security/CVE-2024-33599)
    * Fixed [CVE-2024-33600](https://ubuntu.com/security/CVE-2024-33600)
    * Fixed [CVE-2024-33601](https://ubuntu.com/security/CVE-2024-33601)
    * Fixed [CVE-2024-33602](https://ubuntu.com/security/CVE-2024-33602)



### 1.29.0-gke.2

  * **Breaking Change:** Starting from Kubernetes 1.29, clusters require outbound HTTPS connectivity to the domain `kubernetesmetadata.googleapis.com`. Please ensure that your proxy server and/or firewall configuration allows this traffic. You also need to enable the Kubernetes Metadata API, which can be enabled in the [Google Cloud console](https://console.cloud.google.com/apis/library/kubernetesmetadata.googleapis.com).

  * **Feature:** Removed the requirement for connectivity to the domain `opsconfigmonitoring.googleapis.com`. This domain was previously required for logging and monitoring but is no longer needed for Kubernetes 1.29 and later. You should remove this domain from your firewall and/or proxy server configuration.

  * **Bug Fix:** Fixed an issue where the Fluentbit agent can become unresponsive and stop ingesting logs into Cloud Logging. Added a mechanism to detect and automatically restart the agent when this occurs.




### 1.29.0-gke.1

  * **Breaking Change:** Starting from Kubernetes 1.29, clusters require outbound HTTPS connectivity to the domain `kubernetesmetadata.googleapis.com`. Please ensure that your proxy server and/or firewall configuration allows this traffic. You also need to enable the Kubernetes Metadata API, which can be enabled in the [Google Cloud console](https://console.cloud.google.com/apis/library/kubernetesmetadata.googleapis.com).

  * **Feature:** Removed the requirement for connectivity to the domain `opsconfigmonitoring.googleapis.com`. This domain was previously required for logging and monitoring but is no longer needed for Kubernetes 1.29 and later. You should remove this domain from your firewall and/or proxy server configuration.

  * **Bug Fix:** Fixed an issue where the Fluentbit agent can become unresponsive and stop ingesting logs into Cloud Logging. Added a mechanism to detect and automatically restart the agent when this occurs.




## Kubernetes 1.28

### 1.28.0-gke.9

  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-28834](https://ubuntu.com/security/CVE-2024-28834)
    * Fixed [CVE-2024-28835](https://ubuntu.com/security/CVE-2024-28835)
    * Fixed [CVE-2024-9143](https://ubuntu.com/security/CVE-2024-9143)
    * Fixed [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)
    * Fixed [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)



### 1.28.0-gke.8

  * **Security Fixes:**
    * Fixed [CVE-2023-47108](https://ubuntu.com/security/CVE-2023-47108)
    * Fixed [CVE-2024-7348](https://ubuntu.com/security/CVE-2024-7348)



### 1.28.0-gke.7

  * **Security Fixes:**
    * Fixed [CVE-2024-0553](https://ubuntu.com/security/CVE-2024-0553)
    * Fixed [CVE-2024-0567](https://ubuntu.com/security/CVE-2024-0567)
    * Fixed [CVE-2024-37370](https://ubuntu.com/security/CVE-2024-37370)
    * Fixed [CVE-2024-37371](https://ubuntu.com/security/CVE-2024-37371)



### 1.28.0-gke.6

  * **Security Fixes:**
    * Fixed [CVE-2023-5981](https://ubuntu.com/security/CVE-2023-5981)
    * Fixed [CVE-2024-0985](https://ubuntu.com/security/CVE-2024-0985)
    * Fixed [CVE-2024-2961](https://ubuntu.com/security/CVE-2024-2961)
    * Fixed [CVE-2024-33599](https://ubuntu.com/security/CVE-2024-33599)
    * Fixed [CVE-2024-33600](https://ubuntu.com/security/CVE-2024-33600)
    * Fixed [CVE-2024-33601](https://ubuntu.com/security/CVE-2024-33601)
    * Fixed [CVE-2024-33602](https://ubuntu.com/security/CVE-2024-33602)



### 1.28.0-gke.5

  * **Security Fixes:**



### 1.28.0-gke.4

  * **Security Fixes:**



### 1.28.0-gke.3

  * **Security Fixes:**
    * Fixed [CVE-2023-39326](https://ubuntu.com/security/CVE-2023-39326).
    * Fixed [CVE-2023-44487](https://ubuntu.com/security/CVE-2023-44487).
    * Fixed [CVE-2023-45142](https://ubuntu.com/security/CVE-2023-45142).
    * Fixed [CVE-2023-45285](https://ubuntu.com/security/CVE-2023-45285).
    * Fixed [CVE-2023-48795](https://ubuntu.com/security/CVE-2023-48795).



### 1.28.0-gke.2

  * **Bug Fix:** Fixed an intermittent authorization failure when using Google Groups.



### 1.28.0-gke.1

  * **Breaking Change:** Starting from 1.28, clusters require outbound HTTPS connectivity to `{GCP_LOCATION}-gkemulticloud.googleapis.com`. Ensure your proxy server and/or firewall allows for this traffic.

  * **Feature:** Removed the need to explicitly add Google IAM bindings for most features.

    1. No longer need to add any bindings for `gke-system/gke-telemetry-agent` when creating a cluster.
    2. No longer need to add any bindings for `gmp-system/collector` or `gmp-system/rule-evaluator` when enabling managed data collection for Google Managed Service for Prometheus.
    3. No longer need to add any bindings for `gke-system/binauthz-agent` when enabling binary authorization.
  * **Bug Fix:** Enhanced Cloud Logging's ingestion of logs from Anthos attached clusters:

    * Fixed an issue in timestamp parsing.
    * Assigned the correct severity level to the `anthos-metadata-agent`'s error logs.



## Kubernetes 1.27

### 1.27.0-gke.9

  * **Security Fixes:**
    * Fixed [CVE-2023-5981](https://ubuntu.com/security/CVE-2023-5981)
    * Fixed [CVE-2024-0985](https://ubuntu.com/security/CVE-2024-0985)
    * Fixed [CVE-2024-2961](https://ubuntu.com/security/CVE-2024-2961)
    * Fixed [CVE-2024-33599](https://ubuntu.com/security/CVE-2024-33599)
    * Fixed [CVE-2024-33600](https://ubuntu.com/security/CVE-2024-33600)
    * Fixed [CVE-2024-33601](https://ubuntu.com/security/CVE-2024-33601)
    * Fixed [CVE-2024-33602](https://ubuntu.com/security/CVE-2024-33602)



### 1.27.0-gke.8

  * **Security Fixes:**



### 1.27.0-gke.7

  * **Security Fixes:**



### 1.27.0-gke.6

  * **Security Fixes:**
    * Fixed [CVE-2023-39323](https://ubuntu.com/security/CVE-2023-39323).
    * Fixed [CVE-2023-39325](https://ubuntu.com/security/CVE-2023-39325).
    * Fixed [CVE-2023-39326](https://ubuntu.com/security/CVE-2023-39326).
    * Fixed [CVE-2023-3978](https://ubuntu.com/security/CVE-2023-3978).
    * Fixed [CVE-2023-44487](https://ubuntu.com/security/CVE-2023-44487).
    * Fixed [CVE-2023-45142](https://ubuntu.com/security/CVE-2023-45142).
    * Fixed [CVE-2023-45285](https://ubuntu.com/security/CVE-2023-45285).
    * Fixed [CVE-2023-48795](https://ubuntu.com/security/CVE-2023-48795).



### 1.27.0-gke.5

  * **Bug Fix:** Fixed an intermittent authorization failure when using Google Groups.



### 1.27.0-gke.4

  * **Bug Fix:** Enhanced Cloud Logging's ingestion of logs from Anthos attached clusters: 
    * Fixed an issue in timestamp parsing.
    * Assigned the correct severity level to the `anthos-metadata-agent`'s error logs.



### 1.27.0-gke.3

  * **Feature:** Added support for attaching any CNCF-conformant Kubernetes cluster, in addition to EKS and AKS clusters. To attach a cluster, specify the distribution type as "generic".
  * **Bug Fix:** Removed deployment of Fluent Bit when logging is disabled.



### 1.27.0-gke.2

  * **Bug Fix:** Fixed a problem where Kubernetes resource metrics might not be successfully scraped from Kubelet for EKS if the node's name did not match the node's hostname.



### 1.27.0-gke.1

  * **Feature:** Added the `authorization.admin_groups` field. This allows users to specify google groups as cluster-admins through the management plane.
  * **Feature:** Added [Binary Authorization](https://cloud.google.com/binary-authorization) support.
  * **Feature:** Enabled gzip compression for `fluent-bit` (a log processor and forwarder) and `gke-metrics-agent` (a metrics collector). `fluent-bit` compresses log data before sending it to Cloud Logging, and `gke-metrics-agent` compresses metrics data before sending the data to Cloud Monitoring. This reduces network bandwidth and costs.
  * **Feature:** Added proxy support for attaching AKS/EKS clusters. For details, see [Connect to your EKS cluster](http://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/connect-to-cluster) and [Connect to your AKS cluster](http://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/connect-to-cluster).

  * **Security Fixes**

    * Fixed [CVE-2021-43565](https://ubuntu.com/security/CVE-2021-43565)
    * Fixed [CVE-2022-21698](https://ubuntu.com/security/CVE-2022-21698)
    * Fixed [CVE-2023-0464](https://ubuntu.com/security/CVE-2023-0464)
    * Fixed [CVE-2023-0465](https://ubuntu.com/security/CVE-2023-0465)
    * Fixed [CVE-2023-0466](https://ubuntu.com/security/CVE-2023-0466)
    * Fixed [CVE-2023-2454](https://ubuntu.com/security/CVE-2023-2454)
    * Fixed [CVE-2023-2455](https://ubuntu.com/security/CVE-2023-2455)
    * Fixed [CVE-2023-2650](https://ubuntu.com/security/CVE-2023-2650)
    * Fixed [CVE-2023-24539](https://ubuntu.com/security/CVE-2023-24539)
    * Fixed [CVE-2023-24540](https://ubuntu.com/security/CVE-2023-24540)
    * Fixed [CVE-2023-29400](https://ubuntu.com/security/CVE-2023-29400)



## Kubernetes 1.26

### 1.26.0-gke.9

  * **Security Fixes:**
    * Fixed [CVE-2023-0464](https://ubuntu.com/security/CVE-2023-0464).
    * Fixed [CVE-2023-0465](https://ubuntu.com/security/CVE-2023-0465).
    * Fixed [CVE-2023-0466](https://ubuntu.com/security/CVE-2023-0466).
    * Fixed [CVE-2023-2454](https://ubuntu.com/security/CVE-2023-2454).
    * Fixed [CVE-2023-2455](https://ubuntu.com/security/CVE-2023-2455).
    * Fixed [CVE-2023-2650](https://ubuntu.com/security/CVE-2023-2650).
    * Fixed [CVE-2023-3446](https://ubuntu.com/security/CVE-2023-3446).
    * Fixed [CVE-2023-36054](https://ubuntu.com/security/CVE-2023-36054).
    * Fixed [CVE-2023-3817](https://ubuntu.com/security/CVE-2023-3817).
    * Fixed [CVE-2023-39318](https://ubuntu.com/security/CVE-2023-39318).
    * Fixed [CVE-2023-39319](https://ubuntu.com/security/CVE-2023-39319).
    * Fixed [CVE-2023-39323](https://ubuntu.com/security/CVE-2023-39323).
    * Fixed [CVE-2023-39325](https://ubuntu.com/security/CVE-2023-39325).
    * Fixed [CVE-2023-39326](https://ubuntu.com/security/CVE-2023-39326).
    * Fixed [CVE-2023-39417](https://ubuntu.com/security/CVE-2023-39417).
    * Fixed [CVE-2023-45285](https://ubuntu.com/security/CVE-2023-45285).
    * Fixed [CVE-2023-4911](https://ubuntu.com/security/CVE-2023-4911).
    * Fixed [CVE-2023-5868](https://ubuntu.com/security/CVE-2023-5868).
    * Fixed [CVE-2023-5869](https://ubuntu.com/security/CVE-2023-5869).
    * Fixed [CVE-2023-5870](https://ubuntu.com/security/CVE-2023-5870).
    * Fixed [CVE-2024-0985](https://ubuntu.com/security/CVE-2024-0985).



### 1.26.0-gke.8

  * **Bug Fix:** Fixed an intermittent authorization failure when using Google Groups.



### 1.26.0-gke.7

  * **Bug Fix:** Enhanced Cloud Logging's ingestion of logs from Anthos attached clusters: 
    * Fixed an issue in timestamp parsing.
    * Assigned the correct severity level to the `anthos-metadata-agent`'s error logs.



### 1.26.0-gke.6

  * **Feature:** Added support for attaching any CNCF-conformant Kubernetes cluster, in addition to EKS and AKS clusters. To attach a cluster, specify the distribution type as "generic".



### 1.26.0-gke.5

  * **Bug Fix:** Fixed a problem where Kubernetes resource metrics might not be successfully scraped from Kubelet for EKS if the node's name did not match the node's hostname.
  * **Security Fixes**
    * Fixed [CVE-2023-24539](https://ubuntu.com/security/CVE-2023-24539)
    * Fixed [CVE-2023-24540](https://ubuntu.com/security/CVE-2023-24540)
    * Fixed [CVE-2023-29400](https://ubuntu.com/security/CVE-2023-29400)



### 1.26.0-gke.4

### 1.26.0-gke.3

  * **Security Fixes**
    * Fixed [CVE-2022-27664](https://ubuntu.com/security/CVE-2022-27664)
    * Fixed [CVE-2022-32149](https://ubuntu.com/security/CVE-2022-32149)
    * Fixed [CVE-2022-41723](https://ubuntu.com/security/CVE-2022-41723)
    * Fixed [CVE-2023-24534](https://ubuntu.com/security/CVE-2023-24534)
    * Fixed [CVE-2023-24536](https://ubuntu.com/security/CVE-2023-24536)
    * Fixed [CVE-2023-24537](https://ubuntu.com/security/CVE-2023-24537)
    * Fixed [CVE-2023-24538](https://ubuntu.com/security/CVE-2023-24538)



### 1.26.0-gke.2

  * **Bug Fixes**
    * Fixed an issue in which the logging agent consumed increasingly high amounts of memory.



### 1.26.0-gke.1

  * **Feature:** Added support for Kubernetes 1.26.

  * **Feature:** Enabled connecting to an Anthos attached cluster as a member of a Google group. For details, see [Connect to your EKS cluster](http://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/connect-to-cluster) and [Connect to your AKS cluster](http://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/connect-to-cluster).

  * **Feature:** Fixed a regression which breaks scraping from authenticated Kubelet port.

  * **Feature:** Added day 2 operations for Anthos attached clusters in the Google Cloud console, allowing you to easily [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/detach-cluster) EKS clusters. From the Google Cloud Console, you can also [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/detach-cluster) AKS clusters.

  * **Feature:** Enabled sending Kubernetes resource metadata to Google Cloud Platform, improving both the user interface and cluster metrics. For the metadata to be ingested properly, customers need to enable the `Config Monitoring for Ops` API. This API can be enabled either in the [Google Cloud Console](https://console.cloud.google.com/apis/api/opsconfigmonitoring.googleapis.com/overview) , or by manually enabling the `opsconfigmonitoring.googleapis.com` API in the [gcloud CLI](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/cluster-prerequisites#requirements). Additionally, customers must follow the steps outlined in the [Authorize Cloud Logging/Monitoring](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster#telemetry-agent-auth) documentation to add the necessary IAM bindings.




## Kubernetes 1.25

### 1.25.0-gke.8

  * **Feature:** Added support for attaching any CNCF-conformant Kubernetes cluster, in addition to EKS and AKS clusters. To attach a cluster, specify the distribution type as "generic".



### 1.25.0-gke.7

  * **Bug Fix:** Fixed a problem where Kubernetes resource metrics might not be successfully scraped from Kubelet for EKS if the node's name did not match the node's hostname.
  * **Security Fixes**
    * Fixed [CVE-2023-24539](https://ubuntu.com/security/CVE-2023-24539)
    * Fixed [CVE-2023-24540](https://ubuntu.com/security/CVE-2023-24540)
    * Fixed [CVE-2023-29400](https://ubuntu.com/security/CVE-2023-29400)



### 1.25.0-gke.6

### 1.25.0-gke.5

  * **Security Fixes**
    * Fixed [CVE-2022-27664](https://ubuntu.com/security/CVE-2022-27664)
    * Fixed [CVE-2022-32149](https://ubuntu.com/security/CVE-2022-32149)
    * Fixed [CVE-2022-41723](https://ubuntu.com/security/CVE-2022-41723)
    * Fixed [CVE-2023-24534](https://ubuntu.com/security/CVE-2023-24534)
    * Fixed [CVE-2023-24536](https://ubuntu.com/security/CVE-2023-24536)
    * Fixed [CVE-2023-24537](https://ubuntu.com/security/CVE-2023-24537)
    * Fixed [CVE-2023-24538](https://ubuntu.com/security/CVE-2023-24538)



### 1.25.0-gke.4

  * **Bug Fixes**
    * Fixed an issue in which the logging agent consumed increasingly high amounts of memory.



### 1.25.0-gke.3

  * **Feature:** Added day 2 operations for Anthos attached clusters in the Google Cloud console, allowing you to easily [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/detach-cluster) EKS clusters. From the Google Cloud Console, you can also [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/detach-cluster) AKS clusters.

  * **Feature:** Enabled sending Kubernetes resource metadata to Google Cloud Platform, improving both the user interface and cluster metrics. For the metadata to be ingested properly, customers need to enable the `Config Monitoring for Ops` API. This API can be enabled either in the [Google Cloud Console](https://console.cloud.google.com/apis/api/opsconfigmonitoring.googleapis.com/overview) , or by manually enabling the `opsconfigmonitoring.googleapis.com` API in the [gcloud CLI](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/cluster-prerequisites#requirements). Additionally, customers must follow the steps outlined in the [Authorize Cloud Logging/Monitoring](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster#telemetry-agent-auth) documentation to add the necessary IAM bindings.

  * **Bug Fix:** Fixed a regression which breaks scraping from authenticated Kubelet port.




### 1.25.0-gke.2

  * **Security Fixes**
    * Fixed [CVE-2021-46848](https://ubuntu.com/security/CVE-2021-46848)
    * Fixed [CVE-2022-42898](https://ubuntu.com/security/CVE-2022-42898)



### 1.25.0-gke.1

  * **Feature:** Added support for Kubernetes 1.25.



## Kubernetes 1.24

### 1.24.0-gke.5

  * **Security Fixes**
    * Fixed [CVE-2022-27664](https://ubuntu.com/security/CVE-2022-27664)
    * Fixed [CVE-2022-32149](https://ubuntu.com/security/CVE-2022-32149)
    * Fixed [CVE-2022-41723](https://ubuntu.com/security/CVE-2022-41723)
    * Fixed [CVE-2023-24534](https://ubuntu.com/security/CVE-2023-24534)
    * Fixed [CVE-2023-24536](https://ubuntu.com/security/CVE-2023-24536)
    * Fixed [CVE-2023-24537](https://ubuntu.com/security/CVE-2023-24537)
    * Fixed [CVE-2023-24538](https://ubuntu.com/security/CVE-2023-24538)



### 1.24.0-gke.4

  * **Bug Fixes**
    * Fixed an issue in which the logging agent consumed increasingly high amounts of memory.



### 1.24.0-gke.3

  * **Feature:** Added day 2 operations for Anthos attached clusters in the Google Cloud console, allowing you to easily [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/detach-cluster) EKS clusters. From the Google Cloud Console, you can also [view](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/view-cluster), [update](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/update-cluster), and [detach](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/detach-cluster) AKS clusters.

  * **Bug Fix:** Fixed a regression which breaks scraping from authenticated Kubelet port.




### 1.24.0-gke.2

  * **Security Fixes**
    * Fixed [CVE-2021-46848](https://ubuntu.com/security/CVE-2021-46848)
    * Fixed [CVE-2022-42898](https://ubuntu.com/security/CVE-2022-42898)



### 1.24.0-gke.1

  * **Feature:** Added support for Kubernetes 1.24.



## Kubernetes 1.23

### 1.23.0-gke.3

  * **Security Fixes**
    * Fixed [CVE-2021-46848](https://ubuntu.com/security/CVE-2021-46848)
    * Fixed [CVE-2022-42898](https://ubuntu.com/security/CVE-2022-42898)



### 1.23.0-gke.2

### 1.23.0-gke.1

  * **Feature:** Added support for Kubernetes 1.23.



## Kubernetes 1.22

### 1.22.0-gke.1

  * **Feature:** Added support for Kubernetes 1.22.



## Kubernetes 1.21

### 1.21.0-gke.1

  * **Feature:** Added support for Kubernetes 1.21.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
