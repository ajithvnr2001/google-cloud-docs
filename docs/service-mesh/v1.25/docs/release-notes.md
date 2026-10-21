---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/release-notes/
title: Cloud Service Mesh version 1.25 release notes \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:06:54.536666+00:00
---

# Cloud Service Mesh version 1.25 release notes  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/release-notes/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Resources ](https://docs.cloud.google.com/service-mesh/v1.25/docs/release-notes)



Send feedback 

#  Cloud Service Mesh version 1.25 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for each version of Cloud Service Mesh. 

You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/servicemesh-release-notes.xml) directly. 

## November 18, 2025

Managed Cloud Service Mesh

The following rollouts have completed for managed Cloud Service Mesh:

  * 1.21.6-asm.4 has rolled out to the rapid release channel.
  * 1.20.8-asm.56 has rolled out to the regular release channel.
  * 1.19.10-asm.52 has rolled out to the stable release channel.
  * CNI and MDPC version 1.20.8-asm.56 has rolled out to all release channels.



While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

## October 28, 2025

1.25.x

**1.25.5-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade). Cloud Service Mesh v1.25.5-asm.9 uses Envoy v1.33.12.

1.26.x

**1.26.5-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh v1.26.5-asm.1 uses Envoy v1.34.10.

1.27.x

**1.27.2-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.27.2-asm.1 uses Envoy v1.35.6.

## October 27, 2025

Managed Cloud Service Mesh

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.4 is rolling out to the rapid release channel.
  * 1.20.8-asm.56 is rolling out to the regular release channel.
  * 1.19.10-asm.52 is rolling out to the stable release channel.



CNI/managed data plane controller version 1.20.8-asm.56 is rolling out to all release channels.

These patches contain fixes for the following CVEs:

**1.21.6-asm.4**

Name | Envoy Proxy | Envoy Proxy Distroless | Control plane  
---|---|---|---  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | Yes | -  
[CVE-2025-8058 ](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | -  
[CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | -  
[CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | -  
[CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | -  
[CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | -  
[CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | -  
[CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | -  
[CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | -  
[CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | -  
[CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | -  
  
**1.20.8-asm.55**

Name | Envoy Proxy | Envoy Proxy Distroless | Control plane  
---|---|---|---  
[CVE-2023-4813](https://security-tracker.debian.org/tracker/CVE-2023-4813) | - | Yes | -  
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | -  
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | - | Yes | -  
[CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | -  
[CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | -  
[CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | -  
[CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | -  
[CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | -  
[CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | -  
[CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | -  
[CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | -  
[CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | -  
  
**1.19.10-asm.52**

Name | Envoy Proxy | Envoy Proxy Distroless | Control plane  
---|---|---|---  
[CVE-2023-4813](https://security-tracker.debian.org/tracker/CVE-2023-4813) | - | Yes | -  
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | -  
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | - | Yes | -  
[CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | -  
[CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | -  
[CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | -  
[CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | -  
[CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | -  
[CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | -  
[CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | -  
[CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | -  
[CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | -  
  
**CNI & MDPC**

Name | CNI | MDPC  
---|---|---  
[CVE-2024-56406](https://ubuntu.com/security/CVE-2024-56406) | Yes | Yes  
[CVE-2025-1372](https://ubuntu.com/security/CVE-2025-1372) | Yes | Yes  
[CVE-2025-46836](https://ubuntu.com/security/CVE-2025-46836) | Yes | Yes  
[CVE-2025-30258](https://ubuntu.com/security/CVE-2025-30258) | Yes | Yes  
[CVE-2023-4039](https://ubuntu.com/security/CVE-2023-4039) | Yes | Yes  
[CVE-2025-4802](https://ubuntu.com/security/CVE-2025-4802) | Yes | Yes  
[CVE-2025-1377](https://ubuntu.com/security/CVE-2025-1377) | Yes | Yes  
[CVE-2025-4598](https://ubuntu.com/security/CVE-2025-4598) | Yes | Yes  
[CVE-2025-3576](https://ubuntu.com/security/CVE-2025-3576) | Yes | Yes  
  
## October 16, 2025

Managed Cloud Service Mesh

The promotion of [1.21 to the Rapid release channel](https://docs.cloud.google.com/service-mesh/docs/release-notes#May_06_2025) included upstream breaking changes to [ExternalName](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#externalname-support-changes) and [auto-sni](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#default-value-of-the-feature-flag-enable_auto_sni-to-true) when using the `ISTIOD` [implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation). After considering the impact on customers, we have decided to restore the previous behavior from 1.20 and earlier for managed Cloud Service Mesh clusters using the `ISTIOD` implementation to match Rapid clusters using the `TRAFFIC_DIRECTOR` implementation. These changes are rolling out to the Rapid release channel in version 1.21.5-asm.55 or later.

  * If you are using an `ExternalName` service in the Rapid channel without a port description, the `ExternalName` service will not be translated into `Cluster` in the Envoy configuration. If the `ExternalName` service is a destination of `VirtualService` or `ExternalName` service is used with `REGISTRY_ONLY` mode, you must specify the port in the service like in 1.20 and earlier.

  * If you have an external service multiplexing traffic based on SNI but the corresponding `DestinationRule` doesn't have an explicit SNI, you must [set SNI properly](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#explicit_sni_setup).




## October 15, 2025

1.26.x

**1.26.4-asm.7 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.4-asm.7 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.4](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.26.4-asm.7 uses Envoy v1.34.8-dev.

1.26.4-asm.7 includes the fixes for the following CVEs:

CVE | Proxy | Control Plane | CNI | Distroless  
---|---|---|---|---  
[CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963) | Yes | Yes | Yes | -  
[CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058) | Yes | Yes | Yes | Yes  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | - | - | Yes  
  
1.25.x

1.25.5-asm.7 includes the fixes for the following CVEs:

CVE | Proxy | Control Plane | CNI | Distroless  
---|---|---|---|---  
[CVE-2025-6297](https://ubuntu.com/security/CVE-2025-6297) | Yes | Yes | Yes | -  
[CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963) | Yes | Yes | Yes | -  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | - | - | Yes  
[CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058) | Yes | Yes | Yes | Yes  
  
**1.25.5-asm.7 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.5-asm.7 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.5](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.5-asm.7 uses envoy v1.33.10-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

1.27.x

1.27.1-asm.5 includes the fixes for the following CVEs:

CVE | Proxy | Control Plane | CNI | Distroless  
---|---|---|---|---  
[CVE-2025-6297](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6297) | Yes | Yes | Yes | -  
[CVE-2024-10963](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2024-10963) | Yes | Yes | Yes | -  
[CVE-2025-9230](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-9230) | Yes | Yes | Yes | -  
[CVE-2025-8058](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-8058) | Yes | Yes | Yes | Yes  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | \- | - | - | Yes  
  
**1.27.1-asm.5 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.1-asm.5 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.27.1-asm.5 uses Envoy v1.35.4-dev.

1.24.x

In-cluster Cloud Service Mesh 1.24 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

## September 30, 2025

Managed Cloud Service Mesh

You can now configure traffic routing using [Cloud Service Mesh service routing APIs](https://docs.cloud.google.com/service-mesh/docs/configure-cloud-service-mesh-for-cloud-run#service_to_service) between Cloud Run and Cloud Run, Google Kubernetes Engine, and Google Compute Engine services. (GA).

Managed Cloud Service Mesh with a TD control plane in the Rapid release channel will start using proxy images with an [internal envoy version](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#base_images).

All features supported by Managed (TD) control planes are supported by this proxy. To identify which proxy version is used in a cluster, see [Identify the proxy versions used in the cluster](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-proxy#identify_the_proxy_version_used_in_the_cluster).

This release uses the version `csm_istio_proxy_20250611.00_p0`. More details about the proxy version can be found on the [Versions](https://docs.cloud.google.com/service-mesh/versions) page.

## September 29, 2025

Managed Cloud Service Mesh

**CVE** | **CNI** | **MDP Controller**  
---|---|---  
[CVE-2025-4802](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-4802) | Yes  | Yes   
[CVE-2023-29383](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-29383) | Yes  | Yes   
[CVE-2024-56406](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2024-56406) | Yes  | Yes   
[CVE-2023-7008](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-7008) | Yes  | Yes   
[CVE-2025-1377](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-1377) | Yes  | Yes   
[CVE-2023-4039](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-4039) | Yes  | Yes   
[CVE-2025-46836](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-46836) | Yes  | Yes   
[CVE-2023-50495](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-50495) | Yes  | Yes   
[CVE-2025-4598](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-4598) | Yes  | Yes   
[CVE-2025-3576](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-3576) | Yes  | Yes   
[CVE-2025-30258](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-30258) | Yes  | Yes   
[CVE-2017-11164](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-11164) | Yes  | Yes   
[CVE-2022-41409](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-41409) | Yes  | Yes   
[CVE-2025-1372](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-1372) | Yes  | Yes   
[CVE-2022-27943](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-27943) | Yes  | Yes   
[CVE-2022-4899](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-4899) | Yes  | Yes   
[CVE-2023-34969](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-34969) | Yes  | Yes   
[CVE-2023-45918](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-45918) | Yes  | Yes   
  
CNI/managed data plane controller version 1.23.6-asm.15 is rolling out to all release channels.

## September 25, 2025

1.21.x & 1.22.x & 1.23.x & 1.24.x & 1.25.x & 1.26.x & 1.27.x

Support for the following features will end on **March 17, 2027** :

  * [GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
  * [GKE on Azure](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
  * EKS Attached Clusters on AWS
  * Azure Attached Clusters with AKS



Note that there are no changes to the other features of GKE attached clusters or Google Distributed Cloud (software only or air-gapped), 

You must migrate to an alternative service mesh solution or an alternative Istio-based solution using your existing CSM configuration files by March 17, 2027.

## September 23, 2025

1.27.x

**1.27.1-asm.2 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.1-asm.2 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

The following environment variables and annotations are not supported:

  * `ENVOY_STATUS_PORT_ENABLE_PROXY_PROTOCOL`
  * `PILOT_DNS_CARES_UDP_MAX_QUERIES`
  * `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
  * `sidecar.istio.io/bootstrapOverride`



For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.27.1-asm.2 uses Envoy v 1.35.3-dev.

## September 17, 2025

Managed Cloud Service Mesh

The following rollouts have completed for managed Cloud Service Mesh:

  * 1.21.5-asm.55 has rolled out to the rapid release channel.
  * 1.20.8-asm.48 has rolled out to the regular release channel.
  * 1.19.10-asm.48 has rolled out to the stable release channel.



While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

## September 10, 2025

1.25.x

**1.25.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.4](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.4-asm.0 uses envoy v1.33.8-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

1.24.x

**1.24.6-asm.12 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.12 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.12 uses envoy v1.33.8-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

1.24.x & 1.25.x & 1.26.x

These patches address the following CVEs:

CVE  | Proxy  | Control Plane  | CNI  | Distroless   
---|---|---|---|---  
[CVE-2025-32990](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32990) | Yes  | Yes  | Yes  | \-   
[CVE-2025-32988](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32988) | Yes  | Yes  | Yes  | \-   
[CVE-2025-40909](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-40909) | Yes  | Yes  | Yes  | \-   
[CVE-2025-32989](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32989) | Yes  | Yes  | Yes  | \-   
[CVE-2025-47268](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-47268) | Yes  | Yes  | Yes  | \-   
[CVE-2025-5702](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-5702) | Yes  | Yes  | Yes  | \-   
[CVE-2025-6395](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6395) | Yes  | Yes  | Yes  | \-   
[CVE-2025-48964](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-48964) | Yes  | Yes  | Yes  | \-   
  
1.26.x

1.26.4-asm.1 in-cluster Cloud Service Mesh already includes the fixes for these CVEs.

## September 09, 2025

Managed Cloud Service Mesh

The managed Cloud Service Mesh rollouts [previously announced](https://docs.cloud.google.com/service-mesh/docs/release-notes#August_12_2025) address the following vulnerabilities. While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

**1.21.5-asm.55**

Name | Envoy Proxy | Envoy Proxy distroless | Control plane  
---|---|---|---  
[CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | -  
[CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | -  
[CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | -  
[CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | -  
[CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | -  
[CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | -  
[CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | -  
[CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | -  
[CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | -  
[CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | -  
[CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | -  
[CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | -  
[CVE-2025-1372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1372) | Yes | - | -  
[CVE-2025-1377](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1377) | Yes | - | -  
[CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039) | - | Yes | -  
  
**1.20.8-asm.48**

Name | Envoy Proxy | Envoy Proxy distroless | Control plane  
---|---|---|---  
[CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | -  
[CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | -  
[CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | -  
[CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | -  
[CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | -  
[CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | -  
[CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | -  
[CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | -  
[CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | -  
[CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | -  
[CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | -  
[CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | -  
[CVE-2025-1372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1372) | Yes | - | -  
[CVE-2025-1377](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1377) | Yes | - | -  
  
**1.19.10-asm.48**

Name | Envoy Proxy | Envoy Proxy distroless | Control plane  
---|---|---|---  
[CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | -  
[CVE-2025-22872](https://github.com/advisories/GHSA-vvgc-356p-c3xw) | Yes | Yes | Yes  
[CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | -  
[CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | -  
[CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | -  
[CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | -  
[CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | -  
[CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | -  
[CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | -  
[CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | -  
[CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | -  
[CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | -  
[CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | -  
  
## September 02, 2025

1.26.x

**1.26.4-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains a fix for a [use-after-free (UAF) vulnerability in the DNS cache](https://www.cve.org/CVERecord?id=CVE-2025-54588). For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-048).

Only clusters running in-cluster Cloud Service Mesh version 1.26 are affected. If you are running an earlier in-cluster version or managed Cloud Service Mesh, you are not affected and do not need to take any action.

For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

## August 12, 2025

Managed Cloud Service Mesh

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.5-asm.55 is rolling out to the rapid release channel.
  * 1.20.8-asm.48 is rolling out to the regular release channel.
  * 1.19.10-asm.48 is rolling out to the stable release channel.



## July 25, 2025

Managed Cloud Service Mesh

[Advanced load balancing](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/advanced-load-balancing-istio) for managed Cloud Service Mesh (TD) now generally available (GA).

## July 21, 2025

Managed Cloud Service Mesh

Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20250623b_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.35. This change is rolling out to all release channels.

## July 16, 2025

1.25.x

**1.25.3-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.3-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.3](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.3-asm.11 uses envoy v1.33.4-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

1.26.x

**1.26.0-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.0-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.0](https://istio.io/latest/news/releases/1.26.x/announcing-1.26/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

The following environment variables and annotations are not supported:

  * `ENABLE_GATEWAY_API_MANUAL_DEPLOYMENT`
  * `RETRY_IGNORE_PREVIOUS_HOSTS`
  * `ENABLE_CLUSTER_TRUST_BUNDLE_API`
  * `OMIT_EMPTY_VALUES`
  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
  * Referencing ConfigMaps in a DestinationRule with TLS mode set to SIMPLE mode is not supported



The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with the legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.26.0-asm.11 uses Envoy v1.34.2-dev.

1.23.x

In-cluster Cloud Service Mesh 1.23 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

1.24.x

**1.24.6-asm.9 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.9 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.9 uses envoy v1.32.7-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

## July 09, 2025

1.23.x

**1.23.6-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.6-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.6](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.6-asm.11 uses envoy v1.31.9-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.23/docs/upgrade/upgrade).

1.25.x

**1.25.3-asm.8 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.3-asm.8 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.3](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.3-asm.8 uses envoy v1.33.4-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

1.24.x

**1.24.6-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.4 uses envoy v1.32.7-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

## June 09, 2025

Managed Cloud Service Mesh

You can now enforce cluster-local traffic for an individual service, all services in a particular namespace, or globally for all services in the mesh. For more information, see [Keeping traffic in-cluster](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#keeping_traffic_in-cluster).

## June 06, 2025

Managed Cloud Service Mesh

[DNS Proxy feature](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/dns-proxy) is now available in the Rapid release channel. This feature requires sidecar version `1.21.5-asm.39` or later.

This change affects clusters using both the `TRAFFIC_DIRECTOR` and `ISTIOD` control plane implementations.

When using Cloud Service Mesh with Istio APIs, configuring an [unsupported field](https://docs.cloud.google.com/service-mesh/docs/onboarding/unsupported-istio-apis) or value in an Istio Custom Resources will be reflected as an error in the Mesh status API. 

In some cases, the validation webhook will also reject unsupported API usage with an error message indicating the specific unsupported API. For more information, see [Common webhook error messages](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-webhook#common_webhook_error_messages). You can mitigate these issues by amending the Istio Custom Resource to remove the specified unsupported API configuration.

Isolation support to prevent cross-region overflow is now available as a preview feature for `TRAFFIC_DIRECTOR` implementations of Cloud Service Mesh. For more information, see [Isolation for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/isolation).

## May 21, 2025

1.22.x

In-cluster Cloud Service Mesh 1.22 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

1.25.x

**1.25.2-asm.3 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.2-asm.3 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.2](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.2-asm.3 uses envoy v1.33.1-dev..

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

1.23.x

**1.23.6-asm.3 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.6-asm.3 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.6](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.6-asm.3 uses envoy v1.31.6.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.23/docs/upgrade/upgrade).

1.24.x

**1.24.5-asm.3 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.5-asm.3 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.5](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.5-asm.3 uses envoy v1.32.6-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

## May 06, 2025

Managed Cloud Service Mesh

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.5-asm.42 is rolling out to the rapid release channel.
  * 1.20.8-asm.33 is rolling out to the regular release channel.
  * 1.19.10-asm.33 is rolling out to the stable release channel.



A behavioral change regarding [user-provided credentials (private key and certificate) for TLS termination](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gateway-tls-termination) at ingress is now rolling out to the Rapid release channel. Subsequent announcements will appear for additional release channels.

The Kubernetes Secrets denoted by `Gateway.servers.port.tls.credentialName` will be read by each ingress gateway pod directly instead of the Control Plane. This change enhances security because the user-provided secret is read directly by the workloads instead of passing any managed component.

This change is compatible with previous behavior aside from the propagation speed of the updated secrets. Previously, updated secrets would propagate immediately. Now, updated secrets will propagate within 60 minutes. If you need immediate secret rotation, restart the gateway pods. 

Each gateway pod reads Kubernetes secrets, so the number of the gateway pods becomes a scalability factor. We recommend the following maximum number of gateway pods:

  * If the GKE cluster is regional, 1500 or fewer pods
  * If the GKE cluster is zonal or using autopilot, 500 or fewer pods



If this change in behavior doesn't work for you, consider using the [deployment with mounted credentials](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gateway-tls-termination#deployment_without_mounted_credentials).

This change only affects clusters using Traffic Director and version 1.21.5-asm.42 or later.

## April 16, 2025

1.21.x

In-cluster Cloud Service Mesh 1.21 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

Managed Cloud Service Mesh

New troubleshooting tools for your service mesh are now available. You can get detailed error codes for your Istio resources and check the state of your mesh to identify and resolve configuration problems. Learn more about [Resolving configuration issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-configuration) and [Understanding Feature State Conditions](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-with-feature-state-condition).

## April 04, 2025

1.25.x

**1.25.0-asm.8 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.0-asm.8 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.0](https://istio.io/latest/news/releases/1.25.x/announcing-1.25/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

The following environment variables are not supported:

  * PILOT_MX_ADDITIONAL_LABELS
  * PILOT_DNS_CARES_UDP_MAX_QUERIES
  * PILOT_DNS_JITTER_DURATION
  * PILOT_SEND_UNHEALTHY_ENDPOINTS



The following annotations are not supported:

  * networking.istio.io/traffic-distribution
  * istio.io/reroute-virtual-interfaces 



For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.25.0-asm.8 uses Envoy v1.33.1-dev.

There is a [known issue](https://github.com/istio/istio/issues/55787) where all gateway CRs will see a downtime for status updates when upgrading from 1.24.3 to 1.25.x .

## March 27, 2025

1.22.x

**1.22.8-asm.5 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.22.8-asm.5 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.22.8](https://istio.io/latest/news/releases/1.22.x/announcing-1.22.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster). Cloud Service Mesh version 1.22.8-asm.5 uses envoy v1.30.10-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade).

1.21.x

**1.21.5-asm.34 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.21.5-asm.34 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.21.5](https://istio.io/latest/news/releases/1.21.x/announcing-1.21.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-in-cluster). Cloud Service Mesh version 1.21.5-asm.34 uses envoy v1.29.12-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade).

1.24.x

**1.24.3-asm.6 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.3-asm.6 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.3](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.3-asm.6 uses envoy v1.32.4-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

1.23.x

**1.23.5-asm.3 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.5-asm.3 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.5](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.5-asm.3 uses envoy v1.31.6-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.23/docs/upgrade/upgrade).

## March 20, 2025

Managed Cloud Service Mesh & 1.22.x & 1.23.x & 1.24.x

Cloud Service Mesh now supports dual-stack, extending IPv6 capability to both proxy-based Envoy and proxyless gRPC. For more information, see [Configure IPv6 dual-stack for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/configure-dual-stack-ipv6).

You can now use [custom constraints](https://docs.cloud.google.com/service-mesh/docs/service-routing/custom-constraints) with Organization Policy to provide more granular control over specific fields for some networksecurity and networkservices resources.

Managed Cloud Service Mesh

If you use the managed Cloud Service Mesh with the `ISTIOD` control plane implementation, important changes have been made to how and when you'll receive notifications of upcoming modernization. For details, see [Managed control plane modernization](https://docs.cloud.google.com/service-mesh/docs/modernization#notifications-and-scheduling).

## March 12, 2025

Managed Cloud Service Mesh

The rollout of managed Cloud Service Mesh version 1.20 to the rapid channel has completed.

## February 25, 2025

Managed Cloud Service Mesh

Managed Cloud Service Mesh with the Traffic Director control plane now supports [configuring the network topology](https://istio.io/latest/docs/ops/configuration/traffic-management/network-topologies/#configuring-network-topologies) to use `X-Forwarded-For` and `X-Forwarded-Client-Cert` headers by MeshConfig or annotations of workloads.

## February 24, 2025

Managed Cloud Service Mesh

If you're a user of managed Cloud Service Mesh with the `ISTIOD` control plane implementation, you can now fine-tune your control plane modernization. See the [Managed control plane modernization](https://docs.cloud.google.com/service-mesh/docs/modernization) page for details.

## February 19, 2025

Managed Cloud Service Mesh

Managed Cloud Service Mesh 1.20 is **rolling out** to the rapid channel.

## February 03, 2025

Managed Cloud Service Mesh

Managed Cloud Service Mesh starts using Envoy.1.33 for Gateway API on GKE clusters with rapid channel.

A new version of the data plane for Gateway API is now generally available (GA) as a part of managed Cloud Service Mesh for clusters on GKE Rapid channel. The managed data plane helps you to trigger upgrades for data plane proxies. For more information see [Data plan management considerations](https://docs.cloud.google.com/service-mesh/docs/gateway/prepare-gateway) .

## January 16, 2025

1.24.x

**1.24.2-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.2-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.2](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

  * Istio's dual-stack is not supported
  * Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.



For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.24.2-asm.1 uses Envoy v1.32.3.

## January 15, 2025

1.23.x

**1.23.4-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for a bug in envoy config where `opencensus.proto.trace.v1.TraceConfig` has been disabled by default and an issue causing VirtualService header name validation to reject valid header names.

This patch release also contains the fix for a security vulnerability where [an attacker can craft an input to the Parse functions that would be processed non-linearly with respect to its length, resulting in extremely slow parsing](https://github.com/advisories/GHSA-w32m-9786-jp63).

For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.23.4-asm.7 uses Envoy v1.31.5.

1.22.x

**1.22.7-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for a security vulnerability where [an attacker can craft an input to the Parse functions that would be processed non-linearly with respect to its length, resulting in extremely slow parsing](https://github.com/advisories/GHSA-w32m-9786-jp63).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).Cloud Service Mesh version 1.22.7-asm.4 uses envoy v1.30.9.

1.21.x

**1.21.5-asm.21 is now available for in-cluster Cloud Service Mesh.**

This patch release contains a fix for a bug where [mixed case hosts in Gateway and TLS redirect results in stale RDS](https://github.com/istio/istio/issues/49638). 

This patch release also contains the fix for a security vulnerability where [an attacker can craft an input to the Parse functions that would be processed non-linearly with respect to its length, resulting in extremely slow parsing](https://github.com/advisories/GHSA-w32m-9786-jp63).

For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade). Cloud Service Mesh v1.21.5-asm.21 uses Envoy v1.29.12.

## January 10, 2025

Managed Cloud Service Mesh

The CVE fix for [GCP-2024-065](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-065) has rolled out to all channels.

## December 20, 2024

Managed Cloud Service Mesh

[Advanced load balancing](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/advanced-load-balancing-istio) for managed Cloud Service Mesh (TD) is now available in preview.

## December 18, 2024

1.22.x

**1.22.7-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-065](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-065). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade). Cloud Service Mesh v1.22.7-asm.1 uses Envoy v1.30.9.

Managed Cloud Service Mesh

Upgrading the gRPC client may cause excessive streams to Traffic Director. Be cautious and do a gradual upgrade when upgrading to the following versions:

  * gRPC Java 1.67.1
  * gPRC Go 1.66
  * gRPC C++ 1.63



1.23.x

**1.23.4-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-065](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-065). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.23.4-asm.1 uses Envoy v1.31.5.

1.21.x

**1.21.5-asm.17 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-065](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-065). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade). Cloud Service Mesh v1.21.5-asm.17 uses Envoy v1.29.12.

## December 17, 2024

1.23.x

Routing traffic between Cloud Service Mesh workloads and Cloud Run Services is now available in preview. For more information, see the following pages:

  * [Route traffic from Cloud Service Mesh workloads to Cloud Run Services](https://docs.cloud.google.com/service-mesh/docs/route-to-cloud-run)
  * [Route traffic from Cloud Run Services to Cloud Service Mesh workloads on GKE](https://docs.cloud.google.com/service-mesh/docs/route-from-cloud-run)
  * [Migrate Istio ServiceEntry to GCPBackend for Cloud Run](https://docs.cloud.google.com/service-mesh/docs/migrate-istio-serviceentry-gcpbackend)



1.21.x & 1.22.x & 1.23.x

[Single Cluster Gateway for Mesh](https://docs.cloud.google.com/service-mesh/docs/gateway/overview) is now generally available. For more information, see [Prepare to setup the Gateway API for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gateway/prepare-gateway).

## December 10, 2024

1.21.x & Managed Cloud Service Mesh & 1.22.x & 1.23.x

As part of the [Per-cluster entitlement to GKE Enterprise](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/setup/enable-gkee), a GKE cluster needs to have its `cluster_tier` set to `ENTERPRISE` in order for that cluster to be considered GKE Enterprise.

Existing clusters and new clusters can follow [Update an existing cluster's tier](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/setup/enable-gkee#console_2) and [Enroll a new cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/setup/enable-gkee#enroll_a_new_cluster) respectively to make a cluster enterprise.

Clusters created or registered before November 2024 that use GKE Enterprise as part of their fleet membership are automatically enterprise-tier clusters. This is a billing announcement only, Cloud Service Mesh features don't change.

## November 19, 2024

Managed Cloud Service Mesh

The rollout of managed Cloud Service Mesh version 1.19 to all channels has completed.

## November 12, 2024

1.20.x

In-cluster Cloud Service Mesh 1.20 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

**1.20.8-asm.10 is now available for in-cluster Cloud Service Mesh.**

1.20 is no longer supported. While the fix for the bug in the distroless proxy container has been backported to 1.20, you should upgrade to 1.21 or later.

You can now download 1.20.8-asm.10 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.20.8](https://istio.io/latest/news/releases/1.20.x/announcing-1.20.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.20.8-asm.10 uses envoy v1.28.6.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.20/docs/upgrade/upgrade).

1.23.x

**1.23.3-asm.2 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.3-asm.2 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.3](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.3-asm.2 uses envoy v1.31.2.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

1.22.x

**1.22.6-asm.2 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.22.6-asm.2 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.22.6](https://istio.io/latest/news/releases/1.22.x/announcing-1.22.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster). Cloud Service Mesh version 1.22.6-asm.2 uses envoy v1.30.6.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade).

1.20.x & 1.21.x & 1.22.x & 1.23.x

This release fixes a bug in the distroless proxy container. Before this fix, the distroless proxy produced errors similar to the following when deployed in a Kubernetes cluster with in-cluster control plane that did not have Container Network Interface (CNI) installed.
    
    
    xtables resource problem: can't open lock file /run/xtables.lock: No such file or directory
    

This fix applies to the following new versions:

  * 1.20.8-asm.10
  * 1.21.5-asm.12
  * 1.22.6-asm.2
  * 1.23.3-asm.2



1.21.x

**1.21.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.21.5-asm.12 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.21.5](https://istio.io/latest/news/releases/1.21.x/announcing-1.21.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-in-cluster). Cloud Service Mesh version 1.21.5-asm.12 uses envoy v1.29.8.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade).

## November 07, 2024

Managed Cloud Service Mesh

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.19.10-asm.21 is rolling out to the rapid release channel.
  * 1.19.10-asm.21 is rolling out to the regular release channel.
  * 1.19.10-asm.21 is rolling out to the stable release channel.



## November 06, 2024

1.23.x

**1.23.3-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.3-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.3](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.3-asm.1 uses envoy v1.31.2.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade).

Managed Cloud Service Mesh

Patches fixing a bug where the default user for distroless proxy was changed to root will be rolling out to all release channels. As a result of this fix, the default user is changing back to non-root. When you see the release note notifying that this rollout is complete, you must restart each affected workload to make the change effective.

1.21.x

**1.21.5-asm.10 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.21.5-asm.10 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.21.5](https://istio.io/latest/news/releases/1.21.x/announcing-1.21.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.21.5-asm.10 uses envoy v1.29.8.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade).

1.20.x & 1.21.x & 1.22.x

This release fixes a bug in the following versions where the default user for distroless proxy was changed to root; As a result of this fix, the default user is now back to non-root

  * 1.20.8-asm.6
  * 1.20.8-asm.7
  * 1.21.5-asm.5
  * 1.21.5-asm.7
  * 1.22.3-asm.1
  * 1.22.4-asm.0
  * 1.22.5-asm.1



This change may affect some gateway deployments which rely on the root user to expose a privileged port for ingress or egress. To ensure your gateways continue to work correctly, you may need to apply additional security contexts to your deployments. For details, see the [troubleshooting guide](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-proxy#gateway_fails_to_start_with_distroless_proxy_when_a_privileged_port_is_exposed).

1.20.x

**1.20.8-asm.9 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.20.8-asm.9 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.20.8](https://istio.io/latest/news/releases/1.20.x/announcing-1.20.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.20.8-asm.9 uses envoy v1.28.6.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade).

1.22.x

**1.22.6-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.22.6-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.22.6](https://istio.io/latest/news/releases/1.22.x/announcing-1.22.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.22.6-asm.1 uses envoy v1.30.6.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade).

## October 24, 2024

Managed Cloud Service Mesh

The rollout of managed Cloud Service Mesh version 1.19 to the stable channel has completed.

In future releases, managed Cloud Service Mesh will use the [GKE release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to determine the data plane component and Istio API versions. For more information, see [Provision managed Cloud Service Mesh Requirements](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#requirements).

## October 01, 2024

Managed Cloud Service Mesh

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.19.10-asm.19 is rolling out to the rapid release channel.
  * 1.19.10-asm.19 is rolling out to the regular release channel.
  * 1.19.10-asm.19 is rolling out to the stable release channel.



1.19.10-asm.19 contains the fixes for the security vulnerabilities listed in [GCP-2024-052](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052) and uses Envoy v1.27.7.

1.23.x

A known issue with asmcli for 1.23 is now fixed. Customers might have seen the following error when attempting to install in-cluster Cloud Service Mesh 1.23:
    
    
    asmcli: Downloading ASM..
    gzip: stdin: not in gzip format
    tar: Child returned status 1
    tar: Error is not recoverable: exiting now
    

A new version of asmcli with the fix has released.

## September 19, 2024

1.21.x

**1.21.5-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-052](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade). Cloud Service Mesh v1.21.5-asm.7 uses Envoy v1.29.8.

1.20.x

**1.20.8-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-052](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade/upgrade). Cloud Service Mesh v1.20.8-asm.7 uses Envoy v1.28.6.

1.23.x

1.23.2-asm.2 is now available for in-cluster Cloud Service Mesh.

You can now download 1.23.2-asm.2 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.2](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster). 

  * Istio's [deferred cluster creation](https://istio.io/latest/news/releases/1.23.x/announcing-1.23/change-notes/#:%7E:text=Added%20an%20experimental%20feature%20to%20enable%20cluster%20creation) is not supported.

  * Istio's [outlier log path configuration](https://istio.io/latest/news/releases/1.23.x/announcing-1.23/change-notes/#:%7E:text=Added%20outlier%20log%20path%20configuration%20to%20the%20mesh%20proxy%20config) in mesh proxy config is not supported.

  * Istio's [credentialName](https://istio.io/latest/docs/reference/config/networking/destination-rule/#ClientTLSSettings:%7E:text=No-,credentialName,-string) field in the DestinationRule API is not supported.




Cloud Service Mesh 1.23.2-asm.2 uses Envoy v1.31.1.

This release contains the fix for the security vulnerability listed in [GCP-2024-052](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052).

Managed Cloud Service Mesh 1.23 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout.

1.22.x

**1.22.5-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2024-052](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/upgrade/upgrade). Cloud Service Mesh v1.22.5-asm.1 uses Envoy v1.30.5.

## September 17, 2024

1.20.x & 1.21.x & 1.22.x

Cloud Service Mesh with a Traffic Director control plane implementation is [still](https://docs.cloud.google.com/service-mesh/docs/release-notes#July_29_2024) incompatible with [Envoy version v1.31.0](https://www.envoyproxy.io/docs/envoy/latest/version_history/v1.31/v1.31.0).

If you manually control your Envoy version, do not upgrade to v1.31.0 as there is an existing issue with connecting to the Traffic Director API. Instead, upgrade to [Envoy version **1.31.1**](https://www.envoyproxy.io/docs/envoy/latest/version_history/v1.31/v1.31.1) where this issue is fixed, or set [GRPC_DNS_RESOLVER=native](https://github.com/grpc/grpc/blob/master/doc/environment_variables.md) for v1.31.0 as a workaround.

If you do not manually control your Envoy version, you don't have to do anything. Google's data plane management will not select an incompatible version for you.

## August 22, 2024

Managed Cloud Service Mesh

The onboarding path for Managed Cloud Service Mesh with asmcli is deprecated as of August 22, 2024, and support will end in February 2025. This change affects only Google Cloud clusters. Any off-Google Cloud clusters will continue to use asmcli. 

To ensure this transition is as smooth as possible, use the [gcloud](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane) or Cloud Console onboarding paths when creating new clusters before February 2025.

For clusters with existing Cloud Service Mesh deployments, no immediate action is required from you and those deployments remain fully supported.

1.22.x

**1.22.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.22.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.22.4](https://istio.io/latest/news/releases/1.22.x/announcing-1.22.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Cloud Service Mesh 1.22.4-asm.0 uses Envoy v1.30.4.

1.20.x

**1.20.8-asm.6 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.20.8-asm.6 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.20.8](https://istio.io/latest/news/releases/1.20.x/announcing-1.20.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Cloud Service Mesh 1.20.8-asm.6 uses Envoy v1.28.5.

1.21.x

**1.21.5-asm.5 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.21.5-asm.5 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.21.5](https://istio.io/latest/news/releases/1.21.x/announcing-1.21.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Cloud Service Mesh 1.21.5-asm.5 uses Envoy v1.29.7.

## August 07, 2024

Managed Cloud Service Mesh

Configuring Cloud Service Mesh for either proxyless gRPC or Envoy proxy deployments with the Kubernetes [Gateway API](https://gateway-api.sigs.k8s.io/) is now available as a preview feature. For more information see, the [Overview page](https://docs.cloud.google.com/service-mesh/docs/gateway/overview).

## July 29, 2024

1.20.x & 1.21.x & 1.22.x

**Updated August 8, 2024**

Cloud Service Mesh with a Traffic Director control plane implementation is incompatible with [Envoy version v1.31.0](https://github.com/envoyproxy/envoy/releases). 

If you manually control your Envoy version, do not upgrade to this version as there is an existing [issue](https://github.com/grpc/grpc/issues/19954) with connecting to Traffic Director. If you run into issues with v1.31.0, set [`GRPC_DNS_RESOLVER=native`](https://github.com/grpc/grpc/blob/master/doc/environment_variables.md).

If you do not manually control your Envoy version, you don't have to do anything. Google's data plane management will not select this version for you.

## July 25, 2024

1.22.x

**1.22.3-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.22.3-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.22.3](https://istio.io/latest/news/releases/1.22.x/announcing-1.22.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

  * [Path templating](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation) in Authorization Policy is not supported.
  * Istio's Ambient mode is not supported.
  * Kubernetes Gateway API for mesh is not supported. Gateway API for ingress continues to be supported in public preview. For more information, see [Kubernetes Gateway API (preview) supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#kubernetes_gateway_api_preview).



Cloud Service Mesh 1.22.3-asm.1 uses Envoy v1.30.3.

1.22 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout.

## July 08, 2024

1.20.x

**1.20.8-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for an Envoy bug where the [additional cookie attributes are not properly sent to clients](https://github.com/envoyproxy/envoy/releases/tag/v1.30.4). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.20.8-asm.1 uses Envoy v1.28.5.

1.21.x

**1.21.4-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for an Envoy bug where the [additional cookie attributes are not properly sent to clients](https://github.com/envoyproxy/envoy/releases/tag/v1.30.4). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.21.4-asm.5 uses Envoy v1.29.7.

1.19.x

**1.19.10-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for an Envoy bug where the [additional cookie attributes are not properly sent to clients](https://github.com/envoyproxy/envoy/releases/tag/v1.30.4). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.19.10-asm.9 uses Envoy v1.27.7.

## July 01, 2024

Managed Cloud Service Mesh

New fleets that provision managed Cloud Service Mesh in organizations that have existing fleets with the managed `istiod` control plane implementation will receive the Traffic Director control plane implementation by default.

If you received a Service Announcement, or requested an exception from your account team, then your organization's default control plane implementation for new fleets continues to be `istiod`.

## June 27, 2024

1.21.x

**1.21.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for a security vulnerability where the [Datadog tracer does not handle trace headers with unicode characters](https://github.com/envoyproxy/envoy/security/advisories/GHSA-8mq4-c2v5-3h39). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.21.4-asm.0 uses Envoy v1.29.6.

## June 04, 2024

1.21.x

**1.21.3-asm.3 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.21.3-asm.3 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.21.3](https://istio.io/latest/news/releases/1.21.x/announcing-1.21.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Cloud Service Mesh 1.21.3-asm.3 uses Envoy v1.29.5.

This release contains the fixes for the security vulnerabilities listed in [GCP-2024-032](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-032).

1.21 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout.

The following 3 changes break backwards compatibility in 1.21.

  1. The default value of the feature flag `ENABLE_AUTO_SNI` has [changed from false to true](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#default-value-of-the-feature-flag-enable_auto_sni-to-true). To opt out, set the environment variable to `ENABLE_AUTO_SNI=false`.

  2. The default value of the feature flag `VERIFY_CERT_AT_CLIENT` [changed from false to true](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#default-value-of-the-feature-flag-verify_cert_at_client-is-set-to-true). To opt out, set the environment variable to `VERIFY_CERT_AT_CLIENT=false`.

  3. There are additional changes in [external name support](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#externalname-support-changes). To opt out, set the environment variable `ENABLE_EXTERNAL_NAME_ALIAS=false`.




Note that opting out is only possible for in-cluster installations. If you do opt out, you must restore the default values before upgrading to 1.22.

1.20.x

**1.20.7-asm.2 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-032](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-032). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.20.7-asm.2 uses Envoy v1.28.4.

1.18.x

**1.18.7-asm.26 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-032](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-032). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.18.7-asm.26 uses Envoy v1.26.8.

1.19.x

**1.19.10-asm.6 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-032](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-032). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.19.10-asm.6 uses Envoy v1.27.6.

## May 23, 2024

1.18.x & 1.19.x & 1.20.x

If you're using the Istio APIs with the Traffic Director control plane implementation, disabling multi-cluster load balancing is not supported.

Anthos Service Mesh and Traffic Director have converged into a single, unified product: Cloud Service Mesh. Cloud Service Mesh brings together features from both products:

  * A fully managed, global, multi-tenant control plane
  * Managed data plane and telemetry for Google Cloud
  * A choice of APIs 
    * Open APIs, Istio & Gateway for Kubernetes Engine
    * Service Routing APIs for Compute Engine and Kubernetes Engine
  * Support for Kubernetes clusters on-prem and on other public clouds



For more information see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## April 24, 2024

1.19.x

**1.19.10-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-023](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-023). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/upgrade). Anthos Service Mesh v1.19.10-asm.0 uses Envoy v1.27.5.

1.18.x

**1.18.7-asm.21 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-023](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-023). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.18/docs/unified-install/upgrade). Anthos Service Mesh v1.18.7-asm.21 uses Envoy v1.26.8.

1.20.x

**1.20.6-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-022](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-022). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade). Anthos Service Mesh v1.20.6-asm.0 uses Envoy v1.28.3.

## March 15, 2024

Managed Anthos Service Mesh

The rollout of managed Anthos Service Mesh version 1.17 to the stable channel **has completed**.

## March 11, 2024

1.18.x

**1.18.7-asm.11 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.7-asm.11 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.7-asm.11](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.11/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.18/docs/supported-features). Anthos Service Mesh 1.18.7-asm.11 uses Envoy v1.26.7.

1.20.x

**1.20.4-asm.0 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.20.4-asm.0 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.20.4](https://istio.io/latest/news/releases/1.20.x/announcing-1.20.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.20.4-asm.0 uses Envoy v1.28.1.

Managed Anthos Service Mesh

There is a known issue where new installations of Managed Anthos Service Mesh in the rapid channel on GKE Autopilot clusters may fail. For affected versions and mitigation, see the [GKE release note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#March_08_2024).

1.19.x

**1.19.8-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.19.8-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.19.8](https://istio.io/latest/news/releases/1.19.x/announcing-1.19.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-features). Anthos Service Mesh 1.19.8-asm.2 uses Envoy v1.27.3.

## March 04, 2024

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.18 has completed its rollout in the rapid channel. See [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## February 08, 2024

1.17.x

**1.17.8-asm.20 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

While these CVE fixes have been backported to 1.17, you should upgrade to a supported version, 1.18 or later.

Google has ended support for in-cluster Anthos Service Mesh 1.17 following the official policy. Managed Anthos Service Mesh will continue to support 1.17 until 1.18 is promoted to the regular and stable channels. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

1.20.x

**1.20.3-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.20.3-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.20.3](https://istio.io/latest/news/releases/1.20.x/announcing-1.20.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.20.3-asm.4 uses Envoy v1.28.1.

This release contains the fix for the security vulnerability listed in [GCP-2024-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-007). 

After upgrading Anthos Service Mesh to version 1.20.3 for off-Google Cloud clusters, make sure to restart all Pods in order to trigger the re-injection of sidecars. Otherwise, the Anthos Service Mesh metric reports might become inconsistent between the old and new proxies in the cluster.

Managed Anthos Service Mesh 1.20 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

1.19.x

**1.19.7-asm.3 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.18.x

**1.18.7-asm.4 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2024-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

## January 29, 2024

Managed Anthos Service Mesh

In February 2024, Managed Anthos Service Mesh will begin creating new Google Cloud backend resources that relate to upcoming control plane enhancements. These resources will have no impact on your traffic. The resources include but are not limited to the following:

  * HealthChecks
  * Gateways
  * Meshes
  * HTTPRoutes
  * TCPRoutes
  * TLSRoutes
  * TrafficPolicies
  * EndpointPolicies
  * ServerTLSPolicies
  * ClientTLSPolicies
  * HTTPFilters
  * TCPFilters
  * ServiceLbPolicies



Managed Anthos Service Mesh 1.17 **is rolling out** in the stable channel. See [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## January 16, 2024

1.18.x

**1.18.7-asm.0 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.7-asm.0 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.7](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.7/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.18/docs/supported-features). Anthos Service Mesh 1.18.7-asm.0 uses Envoy v1.26.7.

1.19.x

**1.19.6-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.19.6-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.19.6](https://istio.io/latest/news/releases/1.19.x/announcing-1.19.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.19.6-asm.2 uses Envoy v1.27.3.

1.17.x

**1.17.8-asm.12 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.8-asm.12 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.8](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.17/docs/supported-features). Anthos Service Mesh 1.17.8-asm.12 uses Envoy v1.25.12.

## January 11, 2024

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.17 **is rolling out** in the regular channel. See [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## December 12, 2023

1.16.x

Google has ended support for in-cluster Anthos Service Mesh 1.16 following the official policy. Managed Anthos Service Mesh will continue to support 1.16 in the regular and stable channels until 1.17 is promoted to the regular and stable channels. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

Managed Anthos Service Mesh

The `asmcli --channel` option is no longer supported and your managed Anthos Service Mesh release channel is determined based on your cluster's Google Kubernetes Engine (GKE) release channel. However, using the `asmcli --channel` option will not break your configuration. Additionally, selecting a different managed Anthos Service Mesh release channel is no longer supported. If the cluster is using static versioning, then managed Anthos Service Mesh will default to the regular channel. For more information, see [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel).

1.17.x

**1.17.8-asm.8 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.8-asm.8 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.8](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.17/docs/supported-features). Anthos Service Mesh 1.17.8-asm.8 uses Envoy v1.25.12.

1.19.x

**1.19.5-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.19.5-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.19.5](https://istio.io/latest/news/releases/1.19.x/announcing-1.19.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.19.5-asm.4 uses Envoy v1.27.3.

1.18.x

**1.18.6-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.6-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.6](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.18/docs/supported-features). Anthos Service Mesh 1.18.6-asm.2 uses Envoy v1.26.7.

## December 07, 2023

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.18 **is rolling out** in the rapid channel. See [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

**If you use Gateway API Automated Deployment** , note the following breaking change. With Anthos Service Mesh v1.18 rolled out to the rapid channel, upgrading gateways no longer requires restarting the Pods to trigger a re-injection. Instead, gateways are updated, via a rolling restart, when their revision changes. For more information, see [Istio's release note](https://istio.io/latest/news/releases/1.18.x/announcing-1.18/upgrade-notes/#gateway-api-automated-deployment-changes).

## November 27, 2023

Managed Anthos Service Mesh

The rollout of managed Anthos Service Mesh version 1.17 to the rapid channel **has completed**. Additionally, the rollout of managed Anthos Service Mesh version 1.16 to the stable channel **has completed**.

See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

**If you use Gateway API Automated Deployment** , note the following upcoming change. When Anthos Service Mesh v1.18 is rolled out to the rapid channel, upgrading gateways will no longer require restarting the Pods to trigger a re-injection. Instead, gateways will be updated, via a rolling restart, when their revision changes. For more information, see [Istio's release note](https://istio.io/latest/news/releases/1.18.x/announcing-1.18/upgrade-notes/#gateway-api-automated-deployment-changes).

## November 14, 2023

1.18.x

**1.18.5-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.5-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.5](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.18/docs/supported-features). Anthos Service Mesh 1.18.5-asm.2 uses Envoy v1.26.5.

1.17.x

**1.17.8-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.8-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.8](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.17/docs/supported-features). Anthos Service Mesh 1.17.8-asm.4 uses Envoy v1.25.12.

1.19.x

**1.19.3-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.19.3-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.19.3](https://istio.io/latest/news/releases/1.19.x/announcing-1.19.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.19.3-asm.4 uses Envoy v1.27.2.

1.16.x

**1.16.7-asm.14 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.16.7-asm.14 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.16.7](https://istio.io/latest/news/releases/1.16.x/announcing-1.16.7/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.16/docs/supported-features). Anthos Service Mesh 1.16.7-asm.14 uses Envoy v1.24.11.

## October 31, 2023

1.19.x

**1.19.3-asm.0 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.19.3-asm.0 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.19.3](https://istio.io/latest/news/releases/1.19.x/announcing-1.19.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.19.3-asm.0 uses Envoy v1.27.1.

After upgrading Anthos Service Mesh to version 1.19.3 for off-Google Cloud clusters, make sure to restart all Pods in order to trigger the re-injection of sidecars. Otherwise, the Anthos Service Mesh metric reports might become inconsistent between the old and new proxies in the cluster.

Managed Anthos Service Mesh 1.19 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## October 17, 2023

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.17 **is rolling out** in the rapid channel.

Additionally, the rollout of managed Anthos Service Mesh version 1.16 to the regular channel **has completed**.

See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## October 10, 2023

1.17.x

**1.17.7-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-031](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-031) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.17/docs/unified-install/upgrade).

1.18.x

**1.18.4-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-031](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-031) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.16.x

**1.16.7-asm.10 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-031](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-031) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.16/docs/unified-install/upgrade).

## September 06, 2023

1.16.x

**1.16.7-asm.7 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.16.7-asm.7 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.16.7](https://istio.io/latest/news/releases/1.16.x/announcing-1.16.7/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.16/docs/supported-features). Anthos Service Mesh 1.16.7-asm.7 uses Envoy v1.24.9.

1.18.x

**1.18.2-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.2-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.2](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.18.2-asm.4 uses Envoy v1.26.5.

1.17.x

**1.17.5-asm.9 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.5-asm.9 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.5](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.17.5-asm.9 uses Envoy v1.25.8.

## September 05, 2023

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.16 **is rolling out** in the stable channel. See [Managed Anthos Service Mesh release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

Anthos Service Mesh will begin creating [Network Endpoint Groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs) for all services. This rollout will proceed gradually over a period of several months, starting with the rapid channel. You may notice the following annotations on each of your services: `cloud.google.com/neg` and `cloud.google.com/neg-status`.

You can view NEGs with the following command: `gcloud compute network-endpoint-groups list`.

## August 08, 2023

Managed Anthos Service Mesh

The rollout of managed Anthos Service Mesh version 1.15 to the stable channel has completed.

See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## August 03, 2023

1.18.x

**1.18.2-asm.0 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.18.2-asm.0 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.18.2](https://istio.io/latest/news/releases/1.18.x/announcing-1.18.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.18.2-asm.0 uses Envoy v1.26.5.

Managed Anthos Service Mesh 1.18 isn't rolling out to the rapid release channel at this time. You can periodically check this page for announcements regarding rapid channel rollout. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

Anthos Service Mesh now supports setting up a mesh containing multiple Anthos clusters on AWS. For more information, see [Set up a multi-cluster mesh outside Google Cloud](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup).

1.15.x

Google has ended support for in-cluster Anthos Service Mesh 1.15 following the official policy. Managed Anthos Service Mesh will continue to support 1.15 in the stable channel until 1.16 is promoted to the stable channel. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## July 25, 2023

1.16.x

**Updated:** 2023-07-26

**1.16.7-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-021](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-021) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.16/docs/unified-install/upgrade).

1.17.x

**Updated:** 2023-07-26

**1.17.5-asm.0 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-021](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-021) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.15.x

**Updated:** 2023-07-26

**1.15.7-asm.23 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-021](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-021) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.15/docs/unified-install/upgrade).

## July 18, 2023

1.17.x

**1.17.4-asm.2 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-019](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-019) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.16.x

**1.16.6-asm.3 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-019](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-019) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.16/docs/unified-install/upgrade).

1.15.x

**1.15.7-asm.21 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2023-019](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-019) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.15/docs/unified-install/upgrade).

## June 13, 2023

1.17.x

**1.17.3-asm.1 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.3-asm.1 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.3](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.17.3-asm.1 uses Envoy v1.25.7.

1.16.x

**1.16.5-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.16.5-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.16.5](https://istio.io/latest/news/releases/1.16.x/announcing-1.16.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.16/docs/supported-features). Anthos Service Mesh 1.16.5-asm.2 uses Envoy v1.24.8.

1.15.x

**1.15.7-asm.16 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.15.7-asm.16 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.15.7](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.7/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.15/docs/supported-features). Anthos Service Mesh 1.15.7-asm.16 uses Envoy v1.23.7.

## May 24, 2023

Managed Anthos Service Mesh

The following images **are now rolling out** for managed Anthos Service Mesh:

  * The image for 1.16.4-asm.14 is rolling out to the **regular release channel**
  * The image for 1.15.7-asm.14 is rolling out to the **stable release channel**



See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## May 23, 2023

1.16.x

**1.16.4-asm.14 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.16.4-asm.14 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.16.4](https://istio.io/latest/news/releases/1.16.x/announcing-1.16.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.16.4-asm.14 uses Envoy v1.24.8.

## May 08, 2023

Managed Anthos Service Mesh

Three images that contain a fix for FIPS compliance have successfully rolled out for managed Anthos Service Mesh:

  * The image for 1.16.4-asm.8 is in the **rapid release channel**
  * The image for 1.15.7-asm.8 is in the **regular release channel**
  * The image for 1.14.6-asm.16 is in the **stable release channel**



See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## May 05, 2023

Managed Anthos Service Mesh

The managed data plane is enabled on by default in the regular and rapid channels. To disable the managed data plane, follow the steps in [Disable the managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh-asmcli#disable_the_managed_data_plane_optional)

## April 27, 2023

Managed Anthos Service Mesh

Three images for managed Anthos Service Mesh are now rolling out and contain a fix for FIPS compliance:

  * The image for 1.16.4-asm.8 is rolling out in the **rapid release channel**
  * The image for 1.15.7-asm.8 is rolling out in the **regular release channel**
  * The image for 1.14.6-asm.16 is rolling out in the **stable release channel**



See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## April 26, 2023

1.15.x

**1.15.7-asm.8 is now available for in-cluster Anthos Service Mesh.**

Fixes build issues to achieve FIPS compliance. For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.17.x

**1.17.2-asm.8 is now available for in-cluster Anthos Service Mesh.**

Fixes build issues to achieve FIPS compliance. For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.16.x

**1.16.4-asm.8 is now available for in-cluster Anthos Service Mesh.**

Fixes build issues to achieve FIPS compliance. For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.16/docs/unified-install/upgrade).

## April 21, 2023

Managed Anthos Service Mesh

**1.14.6-asm.11 is now available for managed Anthos Service Mesh.**

The image for 1.14.6-asm.11 has rolled out in the stable release channel for managed Anthos Service Mesh. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

**1.15.7-asm.1 is now available for managed Anthos Service Mesh.**

The image for 1.15.7-asm.1 has rolled out in the regular release channel for managed Anthos Service Mesh. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

The Service dashboard now displays telemetry from external mesh services that have a canonical service label in the regular release channel. See [Defining a Canonical Service](https://docs.cloud.google.com/service-mesh/docs/observability/defining-canonical-service) for more information.

1.14.x

In-cluster Anthos Service Mesh 1.14 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## April 18, 2023

Managed Anthos Service Mesh

Enabling `mesh.googleapis.com` automatically enables `trafficdirector.googleapis.com`, `networkservices.googleapis.com`, and `networksecurity.googleapis.com`. These APIs are required for managed Anthos Service Mesh. However, you can safely disable them on a project or fleet that has no managed Anthos Service Mesh clusters.

## April 04, 2023

1.17.x

**1.17.2-asm.1 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.17.2-asm.1 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.17.1](https://istio.io/latest/news/releases/1.17.x/announcing-1.17.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh 1.17.2-asm.1 uses Envoy v1.25.2.

Managed Anthos Service Mesh 1.17 is rolling out to the rapid release channel soon. You can periodically check this page for the announcement of the rollout of managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

The Envoy projects recently disclosed a series of CVEs that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. The fixes for these CVEs are already included in 1.17.2-asm.1. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-002).

Anthos Service Mesh now supports multi-cluster, multi-network meshes on Anthos clusters on Azure. See [Install Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh) for more information.

The `asmcli` flag `--option vm` used by the now deprecated Compute Engine virtual machine feature has been removed.

1.16.x

**1.16.4-asm.2 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2023-002](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-002). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.16/docs/unified-install/upgrade).

1.14.x

**1.14.6-asm.11 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2023-002](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-002) For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.14/docs/unified-install/upgrade).

1.15.x

**1.15.7-asm.1 is now available for in-cluster Anthos Service Mesh.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2023-002](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2023-002). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.15/docs/unified-install/upgrade).

## April 03, 2023

1.14.x & 1.15.x & 1.16.x

Anthos clusters on AWS (previous generation) is deprecated as of April 1, 2023. Therefore, Anthos Service Mesh no longer supports Anthos clusters on AWS (previous generation). For more information, see the [deprecation announcement](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/turndown-announcement).

## March 28, 2023

Managed Anthos Service Mesh

The `control_plane` field in the service mesh fleet feature API (for example, `gcloud container fleet mesh update --control-plane ...`) is deprecated. Instead, use the `management` field. For more information, see [Provision managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).

## March 23, 2023

Managed Anthos Service Mesh & 1.14.x & 1.15.x & 1.16.x

In April 2023, enabling `mesh.googleapis.com` will automatically enable `trafficdirector.googleapis.com`, `networkservices.googleapis.com`, and `networksecurity.googleapis.com`. These APIs will be required for managed Anthos Service Mesh. You will be able to safely disable them on a project or fleet that has no managed Anthos Service Mesh clusters.

1.16.x

Configuring Certificate Authority connectivity through a HTTP CONNECT-based proxy is now generally available (GA). For more information, see [Configure Certificate Authority connectivity through a proxy](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/configure-ca-through-proxy).

## March 21, 2023

1.14.x & 1.15.x & 1.16.x

In Anthos Service Mesh versions 1.9 and earlier, the server-side minimum TLS version for Anthos Service Mesh workloads was 1.0. In Anthos Service Mesh versions 1.10 and later, the server-side minimum TLS version for Anthos Service Mesh workloads is configured to be 1.2 to improve TLS security. For better security, Anthos Service Mesh does not support configuring the minimum workload TLS version to be lower than 1.2.

With Envoy versions 1.22 and later, the default minimal TLS version for servers changed from 1.0 to 1.2. Therefore, for Anthos Service Mesh version 1.14 and later, the default minimum TLS version for gateway servers is 1.2. If you need to configure the minimal TLS version on an Anthos Service Mesh gateway server to be lower than 1.2, then you can configure the [minProtocolVersion parameter](https://docs.cloud.google.com/service-mesh/docs/gateways#configure_gateway_minimum_tls_version).

Anthos clusters on AWS (previous generation) will be deprecated as of April 1, 2023. Therefore, Anthos Service Mesh will not support Anthos clusters on AWS (previous generation) starting April 1, 2023. For more information, see the [deprecation announcement](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/turndown-announcement).

## February 28, 2023

1.14.x

**1.14.6-asm.9 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.14.6-asm.9 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.14.6](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.14/docs/supported-features).

## February 22, 2023

1.15.x

**1.15.5-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.15.5-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.15.5](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## February 21, 2023

1.16.x

**1.16.2-asm.2** is now available for in-cluster Anthos Service Mesh.

You can now download 1.16.2-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.16.2](https://istio.io/latest/news/releases/1.16.x/announcing-1.16.2/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Managed Anthos Service Mesh 1.16 isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

Anthos Service Mesh now supports Mesh CA on all [supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-features#certificate_authority_ca_support).

Anthos Service Mesh now supports multi-cluster meshes on Amazon EKS and Microsoft AKS. See [Install Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh) and [Set up a multi-cluster mesh outside Google Cloud](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup) for more information.

Anthos Service Mesh now supports [Anthos Clusters on Azure](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#azure) as a preview feature.

1.13.x

Anthos Service Mesh 1.13 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## January 30, 2023

1.15.x

**1.15.4-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.15.4-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.15.4](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## January 24, 2023

1.13.x

**1.13.9-asm.10 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.13.9-asm.10 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.13.9](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.9/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## January 19, 2023

1.14.x

**1.14.6-asm.4 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.14.6-asm.4 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.14.6](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.6/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## January 18, 2023

1.15.x

**1.15.4-asm.2 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.15.4-asm.2 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.15.4](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.4/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Managed Anthos Service Mesh

Service mesh cloud gateway is now available as a preview feature for managed Anthos Service Mesh in the rapid release channel. With service mesh cloud gateway, you can configure Anthos Service Mesh ingress gateway with Cloud Load Balancing through the Kubernetes Gateway API. For more information, see [Configure external HTTP(S) Load Balancing for managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh-cloud-gateway).

1.13.x

**1.13.9-asm.9 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.13.9-asm.9 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.13.9](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.9/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## November 21, 2022

1.15.x

**1.15.3-asm.6 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.15.3-asm.6 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.15.3](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.3/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

1.14.x

**1.14.5-asm.8 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.14.5-asm.8 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.14.5](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

1.13.x

**1.13.9-asm.3 is now available for in-cluster Anthos Service Mesh.**

You can now download 1.13.9-asm.3 for in-cluster Anthos Service Mesh. It includes the features of [Istio 1.13.9](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.9/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## November 07, 2022

Managed Anthos Service Mesh

The rollout of version 1.15 for managed Anthos Service Mesh has completed in all regions.

## November 03, 2022

1.15.x

**1.15.3-asm.1 is now available.**

Anthos Service Mesh 1.15.3-asm.1 includes the features of [Istio 1.15.3](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.3/) subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). If you've installed in-cluster 1.15.2, **please update to 1.15.3 right away**. Google will automatically upgrade customers running managed Anthos Service Mesh.

## November 02, 2022

Managed Anthos Service Mesh

[VPC-SC for managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc-ga) is generally available (GA) in the rapid channel.

## November 01, 2022

Managed Anthos Service Mesh

Version 1.15 is now available for managed Anthos Service Mesh and is rolling out to the Rapid Release Channel.

Upon rollout completion, the managed Anthos Service Mesh channels will contain the following versions:

  * Rapid Release Channel - Version 1.15
  * Regular Release Channel - Version 1.14
  * Stable Release Channel - Version 1.13



Note that regions will have mixed availability during the 1.15 rollout. Additionally, stable and regular channel promotion occurs before 1.15 rolls out to rapid channel.

See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

[End-user authentication](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/end-user-auth) is being made available to managed Anthos Service Mesh in the rapid release channel. See the preceding release note for rollout timelines.

## October 25, 2022

1.15.x

**1.15.2-asm.6 is now available.**

Anthos Service Mesh 1.15.2-asm.6 includes the features of [Istio 1.15.2](https://istio.io/latest/news/releases/1.15.x/announcing-1.15.2/) subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Docker images for in-cluster Anthos Service Mesh v1.15 and later support the Arm architecture.

Anthos Service Mesh now supports configuring Mesh CA and Google CA Service connectivity through an HTTPS proxy when direct connectivity from the sidecar-injected workloads is not available (for example, due to firewalls or other restrictive features). See [Configure Certificate Authority connectivity through a proxy](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/configure-ca-through-proxy) for more information.

1.13.x

**1.13.9-asm.1 is now available.**

Anthos Service Mesh 1.13.9-asm.1 includes the features of [Istio 1.13.9](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.9/) subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

1.12.x

Anthos Service Mesh 1.12 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

Managed Anthos Service Mesh

Managed Anthos Service Mesh 1.15 isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of Managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

1.14.x

**1.14.5-asm.3 is now available.**

Anthos Service Mesh 1.14.5-asm.3 includes the features of [Istio 1.14.5](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.5/) subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## October 19, 2022

Managed Anthos Service Mesh

[VPC-SC for managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc) will soon be generally available (GA) in the rapid channel. Older versions of the `istioctl` support tool may not be compatible with the enhanced security checks. To ensure compatibility, download the latest version of `istioctl`.

## October 05, 2022

1.12.x & 1.13.x & 1.14.x

The Istio and Go projects recently disclosed a CVE that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-020).

1.12.x

**1.12.9-asm.3 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-020](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-020). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade).

1.13.x

**1.13.8-asm.3 and 1.13.8-asm.4 are now available.**

These patch releases contain the fixes for the security vulnerabilities listed in [GCP-2022-020](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-020). If your environment uses managed Anthos Service Mesh, then 1.13.8-asm.3 was rolled out to the Regular release channel and you do not need to take additional steps. If your environment uses in-cluster Anthos Service Mesh, then you must upgrade to 1.13.8-asm.4. For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.14.x

**1.14.4-asm.2 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-020](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-020). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

## September 22, 2022

1.13.x

**1.13.8-asm.1 is now available.**

Anthos Service Mesh 1.13.8-asm.1 includes the features of [Istio 1.13.8](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.8/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

1.14.x

**1.14.4-asm.0 is now available.**

Anthos Service Mesh 1.14.4-asm.0 includes the features of [Istio 1.14.4](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.4/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## September 08, 2022

Managed Anthos Service Mesh

Managed Anthos Service Mesh support for GKE Autopilot is now generally available in the Regular and Rapid channels. For more information, see [Configure managed Anthos Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/automatic-management-with-fleet) or [Configure managed Anthos Service Mesh with `asmcli`](https://docs.cloud.google.com/service-mesh/docs/managed/configure-managed-anthos-service-mesh).

## September 07, 2022

Managed Anthos Service Mesh

Automatically configuring managed Anthos Service Mesh using the Fleet Feature API is now generally available in the rapid, regular, and stable release channels. With this feature, Google will automatically configure your control plane, data plane, and multi-cluster endpoint visibility. This is the preferred method to provision managed Anthos Service Mesh on GKE. For more information, see [Configure managed Anthos Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/automatic-management-with-fleet).

The Google-managed data plane is now generally available (GA) as a part of managed Anthos Service Mesh. The managed data plane helps you upgrade data plane proxies automatically. For more information see [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet#managed-data-plane).

## September 01, 2022

1.13.x

**1.13.7-asm.3 is now available.**

This patch release contains a fix for an issue where `istiod` starts up very slowly when connectivity to the Google Cloud metadata service is partially broken. For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.13/docs/unified-install/upgrade).

Anthos Service Mesh 1.13.7-asm.3 includes the features of [Istio 1.13.7](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.7/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## August 18, 2022

1.13.x

**1.13.7-asm.0 is now available.**

Anthos Service Mesh 1.13.7-asm.0 includes the features of [Istio 1.13.7](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.7/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## August 12, 2022

1.14.x

**1.14.3-asm.1 is now available.**

This patch release contains a fix for the known issue with the signatures of the revisions released August 11, 2022.

Anthos Service Mesh 1.14.3-asm.1 includes the features of [Istio 1.14.3](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.3/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## August 11, 2022

1.12.x

**1.12.9-asm.0 is now available.**

Anthos Service Mesh 1.12.9-asm.0 includes the features of [Istio 1.12.9](https://istio.io/latest/news/releases/1.12.x/announcing-1.12.9/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

1.14.x

**1.14.3-asm.0 is now available.**

Anthos Service Mesh 1.14.3-asm.0 includes the features of [Istio 1.14.3](https://istio.io/latest/news/releases/1.14.x/announcing-1.14.3/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## August 01, 2022

1.12.x & 1.13.x & 1.14.x

The Mesh Config API (`meshconfig.googleapis.com`) now enables the [Connect Gateway API](https://docs.cloud.google.com/anthos/multicluster-management/gateway) (`connectgateway.googleapis.com`) and the [GKE Hub API](http://cloud.google.com/anthos/fleet-management/docs/fleet-concepts) (`gkehub.googleapis.com`). This change does not incur any additional cost.

## July 26, 2022

Managed Anthos Service Mesh

Version 1.14 is now available for managed Anthos Service Mesh and is rolling out to the Rapid Release Channel.

The managed Anthos Service Mesh channels are now mapped to the following versions:

  * Rapid Release Channel - Version 1.14
  * Regular Release Channel - Version 1.13
  * Stable Release Channel - Version 1.12



See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## July 20, 2022

1.14.x

**1.14.1-asm.3 is now available.**

Anthos Service Mesh 1.14 includes the features of [Istio 1.14](https://istio.io/latest/news/releases/1.14.x/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Anthos Service Mesh allows you to configure the minimum TLS version for your Istio workloads. See [Configure minimum TLS version for your workloads](https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls#configure_the_minimum_tls_version_for_your_workloads) for more information.

Managed Anthos Service Mesh isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of Managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

1.11.x

Anthos Service Mesh 1.11 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

1.12.x

**1.12.8-asm.2 is now available**.

Anthos Service Mesh 1.12 includes the features of [Istio 1.12.8](https://istio.io/latest/news/releases/1.12.x/announcing-1.12.8/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/v1.12/docs/supported-features).

1.13.x

**1.13.5-asm.1 is now available**.

Anthos Service Mesh 1.13 includes the features of [Istio 1.13.5](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.5/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/v1.13/docs/supported-features).

## June 17, 2022

1.11.x & 1.12.x & 1.13.x

The [Fleet Feature API](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet) (`mesh.googleapis.com`) now enables the [Connect Gateway API](https://docs.cloud.google.com/anthos/multicluster-management/gateway) (`connectgateway.googleapis.com`). This change does not incur any additional cost.

## June 10, 2022

1.12.x

**1.12.7-asm.2 is now available.**

This patch release contains a fix for the known issue with the signatures of the revisions released [June 9, 2022](https://docs.cloud.google.com/service-mesh/docs/release-notes#June_09_2022) as well as the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade).

1.11.x & 1.12.x & 1.13.x

There is a known issues with the signatures of the revisions released [June 9, 2022](https://docs.cloud.google.com/service-mesh/docs/release-notes#June_09_2022). To avoid this issue, upgrade to one of the following versions instead:

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4



1.13.x

**1.13.4-asm.4 is now available.**

This patch release contains a fix for the known issue with the signatures of the revisions released [June 9, 2022](https://docs.cloud.google.com/service-mesh/docs/release-notes#June_09_2022) as well as the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.11.x

**1.11.8-asm.4 is now available.**

This patch release contains a fix for the known issue with the signatures of the revisions released [June 9, 2022](https://docs.cloud.google.com/service-mesh/docs/release-notes#June_09_2022) as well as the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.11/docs/unified-install/upgrade).

## June 09, 2022

1.13.x

**1.13.4-asm.3 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.11.x

**1.11.8-asm.3 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.11/docs/unified-install/upgrade).

1.12.x

**1.12.7-asm.1 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-015](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade).

1.11.x & 1.12.x & 1.13.x

The Istio and Envoy projects recently disclosed a series of CVEs that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-015).

## May 20, 2022

Managed Anthos Service Mesh

Enabling endpoint discovery multi-cluster installations with declarative API is now available as a preview feature in all release channels. For more information, see [Enable endpoint discovery between public clusters with declarative API](https://docs.cloud.google.com/service-mesh/docs/unified-install/gke-install-multi-cluster#endpoint-discovery-declarative-api).

## May 12, 2022

1.13.x

**1.13.2-asm.5 is now available.**

This patch release contains the features of [Istio 1.13.2](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.2/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features). Anthos Service Mesh version 1.13.2-asm.5 uses envoy v1.21.2.

1.11.x

**1.11.8-asm.1 is now available.**

This patch release includes the features of [Istio 1.11.8](https://istio.io/latest/news/releases/1.11.x/announcing-1.11.8/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/v1.11/docs/supported-features). Anthos Service Mesh version 1.11.8-asm.1 uses envoy v1.19.3.

1.12.x

**1.12.6-asm.3 is now available.**

This patch release contains the features of [Istio 1.12.6](https://istio.io/latest/news/releases/1.12.x/announcing-1.12.6/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/v1.12/docs/supported-features). Anthos Service Mesh version 1.12.6-asm.3 uses envoy v1.20.3.

## May 03, 2022

Managed Anthos Service Mesh

In addition to the existing labels, you can now use the "istio-injection" label as an alias. For more information, see [Injection labels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#injection_labels).

Version 1.13 is now available for managed Anthos Service Mesh and is rolling out into the Rapid Release Channel.

Version 1.12 is being promoted to the Regular Release Channel, and version 1.11 is being promoted to the Stable Release Channel.

See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) for more information.

## April 14, 2022

1.13.x

**1.13.2-asm.2 is now available**.

Anthos Service Mesh 1.13 includes the features of [Istio 1.13.2](https://istio.io/latest/news/releases/1.13.x/announcing-1.13.2/) subject to the list of [Anthos Service Mesh Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## March 30, 2022

1.13.x

**1.13.1-asm.1 is now available.**

Anthos Service Mesh 1.13 includes the features of [Istio 1.13](https://istio.io/latest/news/releases/1.13.x/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Managed Anthos Service Mesh isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of Managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

Anthos Service Mesh now supports Google Kubernetes Engine on Google Cloud and On-premise combined in a hybrid mesh as a public preview feature. See [Install Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh) and [Set up a multi-cluster mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup) for more information.

Anthos Service Mesh now supports Google Kubernetes Engine on Google Cloud and Amazon EKS combined in a multi-cloud mesh as a public preview feature. See [Install Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh) and [Set up a multi-cluster mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup) for more information.

Enabled a single Cloud API (`mesh.googleapis.com`), which automatically enables [all required Cloud APIs](https://docs.cloud.google.com/service-mesh/docs/unified-install/project-cluster-setup#required_apis) for Anthos Service Mesh.

In general, the Service dashboards support all current versions of Anthos Service Mesh. Historically, the Anthos Service Mesh release notes attempted to announce each of these dashboard updates. Going forward, the Anthos Service Mesh release notes will no longer explicitly announce dashboard updates but reserve the space for significant new feature announcements.

1.10.x

Anthos Service Mesh 1.10 is no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## March 10, 2022

1.10.x & 1.11.x & 1.12.x

The Istio project recently [disclosed](https://istio.io/latest/news/security) a CVE that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-010).

1.11.x

**1.11.8-asm.0 is now available.**

This patch release contains the fixes for the security vulnerability listed in [GCP-2022-010](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-010). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.12.x

**1.12.5-asm.0 is now available.**

This patch release contains the fixes for the security vulnerability listed in [GCP-2022-010](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-010). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.10.x

**1.10.6-asm.2 is now available.**

This patch release contains the fixes for the security vulnerability listed in [GCP-2022-010](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-010). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

## March 02, 2022

1.12.x

**1.12.4-asm.2 is now available.**

Anthos Service Mesh includes the features of [Istio 1.12](https://istio.io/latest/news/releases/1.12.x) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Anthos Service Mesh now supports [certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template) with the Certificate Authority Service integration. See [Install default features and CA Service](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#install_ca_service) for more information.

## February 22, 2022

1.12.x

**1.12.4-asm.1 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.10.x

**1.10.6-asm.1 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

1.10.x & 1.11.x & 1.12.x

The Istio project recently [disclosed](https://istio.io/latest/news/security) a series of CVEs that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-007).

1.11.x

**1.11.7-asm.1 is now available.**

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2022-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2022-007). For details on upgrading Anthos Service Mesh, refer to [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).

## February 04, 2022

Managed Anthos Service Mesh

Using the [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) feature API to set up [managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh) with automatic control plane management is now available as a preview feature in the rapid, regular, and stable [release channels](https://docs.cloud.google.com/service-mesh/docs/managed/release-channels). For more information, see [Configure managed Anthos Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet).

## January 28, 2022

1.10.x & 1.11.x & 1.12.x

The Anthos Service Mesh dashboard in the Cloud Console now supports cross-project clusters, Anthos on GKE-on-vSphere (on-prem), and Anthos on Bare Metal. For more information, see [Observability overview](https://docs.cloud.google.com/service-mesh/docs/observability-overview).

## January 20, 2022

1.12.x

1.12.2-asm.0 is now available.

This patch release contains the same bug fixes that are in [Istio 1.12.2](https://istio.io/latest/news/releases/1.12.x/announcing-1.12.2/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE using asmcli](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade)
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade#on-premises)



1.10.x

1.10.6-asm.0 is now available.

This patch release contains the same bug fixes that are in [Istio 1.10.6](https://istio.io/latest/news/releases/1.10.x/announcing-1.10.6/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE using the install_asm script](https://docs.cloud.google.com/service-mesh/v1.10/docs/scripted-install/gke-upgrade)
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.10/docs/on-premises-upgrade)



## January 19, 2022

Managed Anthos Service Mesh

Version 1.12 is now available for managed Anthos Service Mesh and is rolling out into the Rapid Release Channel.

Version 1.11 has been promoted to the Regular Release Channel, and version 1.10 has been promoted to the Stable Release Channel.

See [Select a managed Anthos Service Mesh release channel ](https://docs.cloud.google.com/service-mesh/docs/managed/release-channels)for more information.

Managed Anthos Service Mesh now supports deploying a proxy built on the distroless base image. Note that distroless proxy images do not work with managed data plane.

The distroless base image ensures that the proxy image contains the minimal number of packages required to run the proxy. This improves security posture by reducing the overall attack surface of the image and gets cleaner results with CVE scanners. See [Distroless proxy image](https://docs.cloud.google.com/service-mesh/docs/managed/optional-features#distroless_proxy_image) for more information.

Managed Anthos Service Mesh now supports GKE Autopilot in the Regular and Rapid channels. For more information, see [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh).

Managed Anthos Service Mesh control plane now displays its provisioning status in the ControlPlaneRevision API. For more information, see [Verify the control plane has been provisioned](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh#verify_the_control_plane_has_been_provisioned).

## December 16, 2021

1.12.x

**1.12.0-asm.4 is now available.**

Anthos Service Mesh includes the features of [Istio 1.12](https://istio.io/latest/news/releases/1.12.x) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Fixed a compatibility issue in the previous release between GKE 1.22, the Anthos Service Mesh Certificate Authority (Mesh CA), and Certificate Authority Service (CA Service).

1.10.x & 1.11.x & 1.12.x

Anthos Service Mesh now supports Locality Load Balancing and Consistent Hash Load Balancing.

Managed Anthos Service Mesh

Managed Anthos Service Mesh now supports Locality Load Balancing and Consistent Hash Load Balancing in the regular and rapid channels.

## December 14, 2021

1.7.x & 1.8.x & 1.9.x

Anthos Service Mesh 1.7-1.9 are no longer supported. For more information, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

1.9.x

This release note was updated on December 16, 2021. Managed Anthos Service Mesh still supports 1.9 in the Stable Release Channel.

## December 13, 2021

Managed Anthos Service Mesh

Managed Anthos Service Mesh now supports VPC Service Controls (VPC-SC) as a preview feature in the rapid channel. For more information, see [Configure VPC Service Control for Managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc).

1.11.x

**1.11.5-asm.3 is now available.**

Anthos Service Mesh 1.11 includes the features of [Istio 1.11](https://istio.io/latest/news/releases/1.11.x/announcing-1.11.5/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## December 09, 2021

1.12.x

**1.12.0-asm.3 is now available.**

Anthos Service Mesh 1.12 includes the features of [Istio 1.12](https://istio.io/latest/news/releases/1.12.x/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Managed Anthos Service Mesh isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of Managed Anthos Service Mesh to the rapid channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

Anthos Service Mesh now supports [installations](https://docs.cloud.google.com/service-mesh/docs/unified-install/install) and [upgrades](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) on Microsoft Azure Kubernetes Service (AKS) clusters.

Anthos Service Mesh now supports the [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs) integration on on-premises platforms (both Anthos on VMware and bare metal). See [install](https://docs.cloud.google.com/service-mesh/docs/unified-install/install#install_ca_service) and [upgrade](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade#upgrade_default_features_with_ca_service) with default features and CA Service.

Anthos Service Mesh now supports deploying a proxy built on the distroless base image. The distroless base image ensures that the proxy image contains the minimal number of packages required to run the proxy. This improves security posture by reducing the overall attack surface of the image and gets cleaner results with CVE scanners. See [Distroless proxy image](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/enable-optional-features#distroless_proxy_image) for more information.

For unmanaged Anthos Service Mesh installations, the installer will automatically set up the [default tag](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) (the `istio-revision-tag-default` and `istio-default-validator` webhooks). When the default tag exists, it is possible to use the `istio-injection=enabled` namespace label and the `sidecar.istio.io/inject` workload label to enable sidecar injection for that revision.

## November 19, 2021

1.11.x

1.11.4-asm.5 is now available for managed Anthos Service Mesh and is rolling out into the Rapid Release Channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

Managed Anthos Service Mesh now supports [Certificate Authority (CA) Service](https://docs.cloud.google.com/certificate-authority-service/docs). To install managed Anthos Service Mesh with CA Service, see [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/managed-service-mesh).

Managed Anthos Service Mesh now supports [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) as a preview feature in the Rapid Channel. For more information, see [Configure managed Anthos Service Mesh with `asmcli x`](https://docs.cloud.google.com/service-mesh/docs/unified-install/managed-asmcli-experimental#apply_the_google-managed_control_plane_with_asmcli_experimental).

## November 04, 2021

1.11.x

Managed Anthos Service Mesh now supports private GKE clusters with private control plane. This means that all types of [private GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) are supported. For more information, see [Environments](https://docs.cloud.google.com/service-mesh/docs/supported-features-mcp#environments) on the Supported features page.

Managed Anthos Service Mesh now supports Multi-project with shared VPC in the Rapid Release Channel. For more information, see [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/managed-service-mesh).

Version 1.11 is now available for managed Anthos Service Mesh and is rolling out into the Rapid Release Channel. See [Select a managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

## October 06, 2021

1.11.x

**1.11.2-asm.17 is now available.**

Anthos Service Mesh 1.11 includes the features of [Istio 1.11](https://istio.io/latest/news/releases/1.11.x/) subject to the list of Anthos Service Mesh [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Managed Anthos Service Mesh isn't rolling out to the rapid release channel at this time. You can periodically check this page for the announcement of the rollout of Managed Anthos Service Mesh to the rapid channel. See [Select a Managed Anthos Service Mesh release channel](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-service-mesh) for more information.

`asmcli`is generally available for new installations and upgrades of Anthos Service Mesh. You can use `asmcli` to:

  * Install the [Anthos Service Mesh in-cluster control plane](https://docs.cloud.google.com/service-mesh/docs/unified-install/asmcli-overview)

  * [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/managed-service-mesh)

  * [Add Compute Engine virtual machines to Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gke-install-vm)

  * [Set up a multi-cluster mesh on non-private GKE clusters](https://docs.cloud.google.com/service-mesh/docs/unified-install/gke-install-multi-cluster)

  * [Set up a multi-cluster mesh outside Google Cloud](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup)




The in-cluster control plane is supported on the on the following platforms using `asmcli`:

  * GKE clusters in a single project
  * GKE clusters in multiple projects
  * Anthos clusters on VMware
  * Anthos on bare metal
  * Anthos clusters on AWS
  * Amazon EKS



**Note** : Upgrades from Anthos Service Mesh 1.7 on EKS to Anthos Service Mesh 1.11 aren't supported. You will need to set up a new EKS cluster to install Anthos Service Mesh 1.11.

`asmcli` requires clusters to be registered with a fleet. `asmcli` can automatically register a cluster as long as it meets the requirements specified in [fleet requirements](https://docs.cloud.google.com/service-mesh/docs/unified-install/prerequisites#fleet_requirements). `asmcli` does not support automatic fleet registration for GKE 1.22 clusters, which must be registered manually before installation.

Using `install_asm` and `istioctl install` is deprecated and support for these tools for installations and upgrades of Anthos Service Mesh will be removed when Anthos Service Mesh 1.12 is released. Please update your scripts and tools to use `asmcli`. For more information see [Transitioning to asmcli](https://docs.cloud.google.com/service-mesh/docs/unified-install/asmcli-overview#transitioning_to_asmcli).

Anthos Service Mesh uses a proxy that is based on OSS Envoy. The Anthos Service Mesh 1.11 proxy is based on Envoy v1.19.1.

The Anthos Service Mesh integration with [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service) (CA Service) is generally available. You can use CA Service as the certificate authority for signing mutual TLS certificates. See [Configure Anthos Service Mesh to use CA Service for details](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/configure-ca-service).

## September 20, 2021

1.9.x & 1.10.x

1.9.8-asm.6 and 1.10.4-asm.14 are now available.

These patch releases fix a potential memory leak in the control plane.

## September 14, 2021

1.9.x & 1.10.x

1.9.8-asm.3 and 1.10.4-asm.9 are now available. 

These patch releases:

  * Introduced a rate limit to improve control plane availability under load spikes.
  * Fixed a memory leak and proxy count issue in the control plane.



## August 24, 2021

1.10.x

1.10.4-asm.6 is now available.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2021-016](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-016). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE or On-premises](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) using the `asmcli` script.
  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters](https://docs.cloud.google.com/service-mesh/docs/on-premises-upgrade) on VMware



The `asmcli` script is now available in [preview](https://cloud.google.com/products#product-launch-stages). With this script you can install and upgrade Anthos Service Mesh on GKE and On-premises. For more information, see [About the `asmcli`](https://docs.cloud.google.com/service-mesh/docs/unified-install/asmcli-overview).

Anthos Service Mesh for Compute Engine VMs now uses `gcloud` commands and supports Google-managed control planes. For more information, see [Add Compute Engine virtual machines to Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gke-install-vm).

Google-managed data plane is now available in [preview](https://cloud.google.com/products#product-launch-stages) as a part of managed Anthos Service Mesh. Google-managed data plane helps you upgrade data plane proxies automatically. For more information see [Configure managed Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed-service-mesh).

1.7.x & 1.8.x & 1.9.x & 1.10.x

The Istio project recently [disclosed](https://istio.io/latest/news/security) a series of CVEs that can expose Anthos Service Mesh to remotely exploitable vulnerabilities. For more information, see the [security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-016).

Anthos Service Mesh now supports skip-version upgrades for single-project clusters on GKE running versions 1.7 and higher. This means you can now upgrade 1.7 and 1.8 installations directly to 1.10. For more information, see [Upgrading Anthos Service Mesh to the latest version](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade).

1.8.x

1.8.6-asm.8 is now available.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2021-016](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-016). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE or On-premises](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) using the `asmcli` script (preview)
  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.8/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters](https://docs.cloud.google.com/service-mesh/v1.8/docs/gke-on-prem-upgrading) on VMware



1.7.x

1.7.8-asm.10 is now available.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2021-016](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-016). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE or On-premises](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) using the `asmcli` script (preview)
  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.7/docs/scripted-install/gke-asm-onboard-1-7) using the `install_asm` script
  * [Upgrading on Anthos clusters](https://docs.cloud.google.com/service-mesh/v1.7/docs/gke-on-prem-upgrading) on VMware



1.9.x

1.9.8-asm.1 is now available.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2021-016](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-016). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE or On-premises](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade) using the `asmcli` script (preview)
  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.9/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters](https://docs.cloud.google.com/service-mesh/v1.9/docs/on-premises-upgrade) on VMware



## July 28, 2021

1.8.x

1.8.6-asm.7 is now available. This patch release:

  * Fixes a bug that could lead to memory leaks in the proxy.
  * Fixes a bug causing invalid `cipherSuites` in the Gateway configuration that could cause broken traffic.



## July 22, 2021

1.7.x & 1.8.x & 1.9.x & 1.10.x

The 1.x version of [`kpt`](https://kpt.dev/?id=overview) breaks Anthos Service Mesh installations and upgrades. Anthos Service Mesh requires a pre -1.x version of `kpt`. The latest version of the `gcloud` command-line tool includes the 1.x `kpt` that breaks installs and upgrades. 

Make sure that you are running a pre 1.x version of `kpt`:
    
    
    kpt version
    

The output should be similar to the following:
    
    
    0.39.2
    

If you have `kpt` version 1.x or higher, use the `curl` command in [Setting up your environment](https://docs.cloud.google.com/service-mesh/docs/environment-setup) to download the required version for your operating system.

If you are installing or upgrading Anthos Service Mesh using the `install_asm` script, make sure to download the most recent version of the script. The updated version of `install_asm` checks your `kpt` version. If needed, `install_asm` downloads and uses the required `kpt` version. Run `install_asm --version` to make sure you have a version of `install_asm` that has the workaround. You need the following `install_asm` versions or higher:

  * **1.10** : 1.10.2-asm.3+config1 or higher. [Get the latest 1.10 install_asm](https://docs.cloud.google.com/service-mesh/docs/scripted-install/asm-onboarding#downloading_the_script).

  * **1.9** : 1.9.6-asm.2+config1 or higher. [Get the latest 1.9 install_asm](https://docs.cloud.google.com/service-mesh/v1.9/docs/scripted-install/asm-onboarding#downloading_the_script).

  * **1.8** 1.8.6-asm.5+config1 or higher. [Get the latest 1.8 install_asm](https://docs.cloud.google.com/service-mesh/v1.8/docs/scripted-install/asm-onboarding#downloading_the_script).

  * **1.7** Download the required `kpt` version as described above.




## June 30, 2021

1.10.x

1.10.2-asm.3 is now available and includes a fix for the known issue with control plane metric reporting reported on June 25, 2021.

For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters](https://docs.cloud.google.com/service-mesh/docs/on-premises-upgrade) on VMware



Anthos Service Mesh user authentication is now generally available (GA). This feature lets you use existing Identity Providers (IDP) for user authentication and access control to your workloads. For more information, see [Configuring Anthos Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/docs/security/end-user-auth).

## June 29, 2021

1.10.x

There is a breaking change in 1.10 with inbound forwarding that affects applications that bind solely to the `localhost` interface.

For more information, see the [1.10 Istio upgrading notes](https://istio.io//latest/news/releases/1.10.x/announcing-1.10/upgrade-notes/).

## June 25, 2021

1.10.x

There is a known issue in 1.10.2-asm.2 where control plane metric reporting to Cloud Monitoring is not functioning properly and reports excessive error logs in the Istiod container.

## June 24, 2021

1.10.x

1.10.2-asm.2 is now available.

This patch release contains the same bug fixes that are in [Istio 1.10.2](https://istio.io/latest/news/releases/1.10.x/announcing-1.10.2/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos](https://docs.cloud.google.com/service-mesh/docs/on-premises-upgrade) clusters on VMware



Google-managed control plane release channels are available.

Anthos Service Mesh releases updates often, to deliver security updates, fix known issues, and introduce new features. Release channels offer you the ability to balance between stability and the feature set of the Anthos Service Mesh version. Google automatically manages the version and upgrade cadence for each release channel. To learn more, see the following:

  * [1.9x Google-managed control plane](https://docs.cloud.google.com/service-mesh/v1.9/docs/release-channels-managed-control-plane)

  * [1.10x Google-managed control plane](https://docs.cloud.google.com/service-mesh/docs/release-channels-managed-control-plane)




Anthos clusters on-premises support Mesh CA.

New installations of Anthos Service Mesh 1.10x on Anthos clusters on VMWare and bare metal support the Anthos Service Mesh certificate authority (Mesh CA). For details on the installation, see [Installing Anthos Service Mesh on-premises](https://docs.cloud.google.com/service-mesh/docs/on-premises-install).

When you install Anthos Service Mesh on-premises with Mesh CA, this enables [Cloud Monitoring and Cloud Logging](https://docs.cloud.google.com/service-mesh/docs/supported-features#user_interface) by default. Additionally, you can use Cloud Trace (which you [enable separately](https://docs.cloud.google.com/service-mesh/docs/enable-optional-features#trace)) as needed for troubleshooting.

Migrating to Mesh CA from Istio CA with little or no downtime.

Migrating to Anthos Service Mesh certificate authority (Mesh CA) from Istio CA (also known as Citadel) requires migrating the root of trust. Prior to Anthos Service Mesh 1.10, if you wanted to migrate from Istio on to Anthos Service Mesh with Mesh CA, you needed to schedule downtime because Anthos Service Mesh was not able to load multiple root certificates, which interrupted mutual TLS (mTLS) traffic during the migration.

With Anthos Service Mesh 1.10 and higher, you can install a new in-cluster control plane with an option that distributes the Mesh CA root of trust to all proxies. After switching to the new control plane and restarting workloads, all proxies are configured with both the Istio CA and Mesh CA root of trust. Next, you install a new in-cluster control plane that has Mesh CA enabled. As you switch workloads over to the new control plane, mTLS traffic isn't interrupt. For details, see [Migrating to Mesh CA](https://docs.cloud.google.com/service-mesh/docs/ca-migration).

1.8.x & 1.9.x

1.8.6-asm.4 and 1.9.6-asm.1 are now available. This release updates the envoy versions for the following Anthos Service Mesh versions:

  * 1.8.6-asm.2 uses Envoy v1.16.3.
  * 1.9.6-asm.1 uses Envoy v1.17.2.



These patch releases contains a fix for [CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * Anthos Service Mesh 1.8.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.8/docs/scripted-install/gke-upgrade)
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.8/docs/gke-on-prem-upgrading)
  * Anthos Service Mesh 1.9.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.9/docs/scripted-install/gke-upgrade)
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.9/docs/on-premises-upgrade)



The Istio project recently [announced](https://istio.io/latest/news/security/istio-security-2021-007/) a security vulnerability ([CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)) where where credentials specified in the Gateway and DestinationRule credentialName field can be accessed from different namespaces.

For more information, see the [GCP-2021-012 security bulletin](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-012).

## June 15, 2021

1.9.x

Google-managed control plane is now a generally available (GA) feature. This feature lets you move from managing Istiod in your clusters to configuring the control plane as a service. Google will manage the availability, scalability and security of the control plane.

In addition, it offers these new features: 

  * Support for [CNI](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane#apply_the_google-managed_control_plane)
  * Support for private clusters with a [public IP address/endpoint access](https://docs.cloud.google.com/service-mesh/docs/supported-features-mcp#environments) for the control plane
  * Support for private clusters with [Master Authorized Network (MAN)](https://docs.cloud.google.com/service-mesh/docs/supported-features-mcp#environments)



Using the Google-managed control plane also simplifies multi-cluster mesh configuration and reduces the Kubernetes Engine privileges needed to install Anthos Service Mesh. For more information see [Configuring the Google-managed control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane).

## May 19, 2021

1.6.x

Anthos Service Mesh 1.6 is no longer supported. For more information see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## May 17, 2021

1.7.x & 1.8.x & 1.9.x

1.9.5-asm.2, 1.8.6-asm.3, and 1.7.8-asm.8 are now available.

This release fixes the following security vulnerabilities: 

  * [GCP-2021-008](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-008)
  * [GCP-2021-007](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2021-007)



For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade)
  * [Upgrading on-premises](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)



Anthos Service Mesh uses a proxy that is based on OSS Envoy. The Envoy version that the Anthos Service Mesh proxy uses differs by Anthos Service Mesh version, as follows:

  * **1.9.5-asm.2** : [Envoy v1.17.1](https://www.envoyproxy.io/docs/envoy/v1.17.2/version_history/current)
  * **1.8.6-asm.3** : [Envoy v1.16.3](https://www.envoyproxy.io/docs/envoy/v1.17.2/version_history/current)
  * **1.7.8-asm.8** : [Envoy v1.15.4](https://www.envoyproxy.io/docs/envoy/v1.15.4/version_history/current)

**Note:** The rollout of the [Anthos Service Mesh Managed Control Plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane) (available only in 1.9.x versions) will complete in the next few days.

## April 20, 2021

1.9.x

Adding multiple private clusters from different projects into a single Mesh on GKE is now available as a generally available (GA) feature.

1.8.x

Adding multiple private clusters from different projects into a single Mesh on GKE is now available as a public [preview](https://cloud.google.com/products#product-launch-stages) feature.

1.6.x & 1.7.x & 1.8.x & 1.9.x

1.9.3-asm.2, 1.8.5-asm.2, 1.7.8-asm.1, and 1.6.14-asm.2 are now available.

Fixes the security issue, [ISTIO-SECURITY-2021-003](https://istio.io/latest/news/security/istio-security-2021-003), with the same fixes as Istio 1.9.3. These fixes were also backported to the specified Anthos Service Mesh versions.

This release updates the envoy versions for the following Anthos Service Mesh versions:

  * Anthos Service Mesh version 1.9.3-asm.2 uses [envoy v1.17.2](https://www.envoyproxy.io/docs/envoy/v1.17.2/version_history/current).
  * Anthos Service Mesh version 1.8.5-asm.2 uses [envoy v1.16.3](https://www.envoyproxy.io/docs/envoy/v1.16.3/version_history/current).
  * Anthos Service Mesh version 1.7.8-asm.1 uses [envoy v1.15.4](https://www.envoyproxy.io/docs/envoy/v1.15.4/version_history/current).
  * Anthos Service Mesh version 1.6.14-asm.2 uses [envoy v1.14.7](https://www.envoyproxy.io/docs/envoy/v1.14.7/).



For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * Anthos Service Mesh 1.9.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)
  * Anthos Service Mesh 1.8.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.8/docs/scripted-install/gke-upgrade)
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.8/docs/gke-on-prem-upgrading)
  * Anthos Service Mesh 1.7.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.7/docs/scripted-install/gke-asm-onboard-1-7)
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.7/docs/gke-on-prem-upgrading)
  * Anthos Service Mesh 1.6.x 
    * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/v1.6/docs/upgrading-gke)
    * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.6/docs/gke-on-prem-upgrading)



## April 02, 2021

1.9.x

Anthos Service Mesh user authentication is now available as a public [preview](https://cloud.google.com/products#product-launch-stages) feature on installations of 1.9. This feature lets you use existing Identity Providers (IDP) for user authentication and access control to your workloads. For more information, see [Configuring Anthos Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/docs/security/end-user-auth).

1.9.2-asm.1 is now available.

This patch release contains the same bug fixes that are in [Istio 1.9.2](https://istio.io/latest/news/releases/1.9.x/announcing-1.9.2). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)



## March 29, 2021

1.6.x & 1.4.x & 1.5.x

The Anthos Service Mesh Topology (beta) page in Cloud Console won't display properly if [unsupported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features), including versions earlier than Anthos Service Mesh 1.6.8, are installed on your clusters or if you have disabled the Canonical Service controller in clusters in your project.

Note that the Canonical Service controller is enabled by default on version 1.6.8 and higher. If you did not disable the Canonical Service controller on a supported version, no action is required. 

**What should I do?**

  * [Upgrade to Anthos Service Mesh 1.6.8 or higher](https://docs.cloud.google.com/service-mesh/docs/upgrade-path-old-versions).
  * [Enable the Canonical Service controller](https://docs.cloud.google.com/service-mesh/docs/canonical-service-controller-enable-and-disable).



## March 04, 2021

1.9.x

1.9.1-asm.1 is now available. Anthos Service Mesh 1.9 includes the features of [Istio 1.9](https://istio.io/latest/news/releases/1.9.x/announcing-1.9/) subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Anthos Service Mesh for Compute Engine VMs is now available as a public [preview](http://cloud.google.com/products#product-launch-stages) feature. With this new feature you can manage, observe, and secure services running on both Compute Engine Managed Instance Groups and Kubernetes Engine clusters in the same mesh. You can mix and choose the best environment to run your services while enjoying the benefits of Anthos Service Mesh.

This feature also improves security and usability by letting you use Compute Engine service accounts for mTLS authentication to other Compute Engine VMs and Kubernetes Engine Pods. For more information see the [documentation](https://docs.cloud.google.com/service-mesh/docs/gke-install-vm).

Google-managed control plane is now available as a public [preview](http://cloud.google.com/products#product-launch-stages) feature. This feature lets you move from managing `istiod` in your clusters to configuring the control plane as a service. Google will manage the availability, scalability and security of the control plane.

Using the managed control plane also simplifies multi-cluster mesh configuration and reduces the Kubernetes Engine privileges needed to install Anthos Service Mesh. For more information see [Configuring the Google-managed control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane).

1.5.x

Anthos Service Mesh 1.5 is no longer supported. For more information see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features#supported_versions).

## February 23, 2021

1.8.x

1.8.3-asm.2 is now available. 

This patch release contains the same bug fixes that are in [Istio 1.8.3](https://istio.io/latest/news/releases/1.8.x/announcing-1.8.3/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE ](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)



## February 12, 2021

1.6.x

1.6.14-asm.1 is now available.

This patch release contains a fix for [CVE-2021-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3156). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.6/docs/upgrading-gke)
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/v1.6/docs/gke-on-prem-upgrading)



## February 02, 2021

1.8.x

1.8.2-asm.2 is now available. 

This patch release contains the same bug fixes that are in [Istio 1.8.2](https://istio.io/latest/news/releases/1.8.x/announcing-1.8.2/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading on GKE ](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-upgrade) using the `install_asm` script
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)



The `install_asm` script lets you reinstall the same version

You can use the `install_asm` script when you need to reinstall the same Anthos Service Mesh version to change the control plane configuration. For more information, see the following:

  * 1.8: [Reinstalling the same version](https://docs.cloud.google.com/service-mesh/docs/scripted-install/reinstall)

  * 1.7: [Reinstalling the same version](https://docs.cloud.google.com/service-mesh/docs/archive/1.7/docs/scripted-install/gke-asm-onboard-1-7#reinstalling_the_same_version)




## January 20, 2021

1.7.x

1.7.6-asm.1 is now available.

This patch release contains the same bug fixes that are in [Istio 1.7.6](https://istio.io/latest/news/releases/1.7.x/announcing-1.7.6/). For details on upgrading Anthos Service Mesh, refer to the following Anthos Service Mesh upgrade guides:

  * [Upgrading on GKE ](https://docs.cloud.google.com/service-mesh/docs/archive/1.7/docs/scripted-install/gke-asm-onboard-1-7) using the `install_asm` script
  * [Upgrading on Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/archive/1.7/docs/gke-on-prem-upgrading)



## January 12, 2021

1.6.x

1.6.14-asm.0 is now available.

This patch release contains the same bug fixes that are in [Istio 1.6.14](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.14/). For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

  * [Upgrading Anthos Service Mesh on GKE ](https://docs.cloud.google.com/service-mesh/docs/archive/1.6/docs/upgrading-gke)
  * [Upgrading Anthos clusters on VMware](https://docs.cloud.google.com/service-mesh/docs/archive/1.6/docs/gke-on-prem-upgrading)



## December 16, 2020

1.8.x

1.8.1-asm.5 is now available.

New flags for the install_asm script

The `install_asm` script was enhanced to provide you with more granular control over the changes that the script makes on your project and GKE on Google Cloud cluster. For more information, see the [Enablement flags](https://docs.cloud.google.com/service-mesh/docs/scripted-install/reference#enablement_flags) section in the documentation for the script.

Multi-cluster support for GKE on-prem [Beta](https://cloud.google.com/products#product-launch-stages)

Anthos Service Mesh now supports multi-cluster meshes when running on GKE on-prem. For more information, see [Add clusters to Anthos Service Mesh on-prem](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-install-multicluster-vmware).

Third-party add-ons removed from all profiles

The Prometheus, Grafana, and Kiali add-ons were removed from all Anthos Service Mesh profiles. For information on why the add-ons were removed, see [Reworking our Addon Integrations](https://istio.io/latest/blog/2020/addon-rework/). Installation of these third-party add-ons was removed from the 1.8 `IstioOperator` API, which means that they can't be installed with the `istioctl install` command. For information on installing a demo version of the add-ons, see [Integrating with third-party add-ons](https://docs.cloud.google.com/service-mesh/docs/third-party-integrations).

Note that by default, [metrics are still exported to Prometheus](https://docs.cloud.google.com/service-mesh/docs/supported-features#telemetry) in the `asm-multicloud` profile. You can optionally enable metrics export to Prometheus in the `asm-gcp-multiproject` profile.

Anthos Service Mesh 1.8 isn't supported on Anthos attached clusters and GKE on AWS

Anthos Service Mesh 1.8 currently isn't supported on Anthos attached clusters (Microsoft AKS and Amazon EKS) and GKE on AWS (Amazon EC2). Anthos Service Mesh 1.7 and 1.6 are supported for these environments. For more information, see the following guides:

  * Anthos Service Mesh 1.7 
    * [Installing Anthos Service Mesh 1.7 on attached clusters](https://docs.cloud.google.com/service-mesh/docs/archive/1.7/docs/attached-clusters-install)
    * [Installing Anthos Service Mesh 1.7 on GKE on AWS](https://docs.cloud.google.com/service-mesh/docs/archive/1.7/docs/gke-on-aws-install)
  * Anthos Service Mesh 1.6 
    * [Installing Anthos Service Mesh 1.6 on attached clusters](https://docs.cloud.google.com/service-mesh/docs/archive/1.6/docs/attached-clusters-install)
    * [Installing Anthos Service Mesh 1.6 on GKE on AWS](https://docs.cloud.google.com/service-mesh/docs/archive/1.6/docs/gke-on-aws-install)



Reduced permissions required for installation

The permissions required for installation have been scaled back. Testing has shown that the Project Editor role can be replaced with more granular roles. For the complete list, see [Permissions required to install Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/installation-permissions).

## November 12, 2020

1.6.x & 1.7.x

Anthos Service Mesh, Mesh CA and the Anthos Service Mesh dashboards in Google Cloud Console are now available for any GKE customer and do not require the purchase of Anthos. See [pricing](https://cloud.google.com/service-mesh/docs/pricing) for details.

Added a shell script to automate Anthos Service Mesh installation and migration from Istio and the Istio on GKE add-on. For details, see the following guides:

  * 1.6: [Installation and migration on GKE](https://docs.cloud.google.com/service-mesh/docs/archive/1.6/docs/scripted-install/gke-asm-onboard-1-6)

  * 1.7: [Installation, migration, and upgrades on GKE](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-asm-onboard-1-7)




There are slight changes to the behavior of Google Cloud Console for customers who use Anthos Service Mesh without an Anthos subscription. See details [here](https://docs.cloud.google.com/service-mesh/docs/ui-differences).

## November 03, 2020

1.7.x

1.7.3-asm.6 is now available

Anthos Service Mesh 1.7 is compatible with and has the feature set of [Istio 1.7](https://istio.io/latest/news/releases/1.7.x/announcing-1.7/), subject to the list of [Anthos Service Mesh supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Added [revision label support](https://docs.cloud.google.com/service-mesh/docs/proxy-injection) to sidecar injection for greater control over various scenarios, such as canary upgrades and more.

Added support for on-premises secure key management, provided by [Thales Luna HSM 7+ and Hashicorp Vault](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-install-hsm).

Added a shell script to automate Anthos Service Mesh installation and migration from Istio 1.6. See the [installation guide](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-asm-onboard-1-7) for details.

The beta validation tool **asmctl** is retired and the lessons learned are built into the new, streamlined [Anthos Service Mesh install script](https://docs.cloud.google.com/service-mesh/docs/scripted-install/gke-asm-onboard-1-7).

If you use unsupported Istio features in your Anthos Service Mesh deployment, see [Istio upgrade notes](https://istio.io/latest/news/releases/1.7.x/announcing-1.7/upgrade-notes/) for changes that might affect you.

## October 13, 2020

1.4.x

You can now allow an experimental feature to exceed 4GB of memory usage.

1.4.10-asm.19 is now available

## September 29, 2020

1.6.x & 1.4.x & 1.5.x

**1.6.11-asm.1, 1.5.10-asm.2, and 1.4.10-asm.18**

Fixes the security issue, [ISTIO-SECURITY-2020-010](https://istio.io/latest/news/security/istio-security-2020-010), with the same fixes as Istio 1.6.11. These fixes were backported to 1.6.11-asm.1, 1.5.10-asm.2 and 1.4.10-asm.18. For more information, see the [Istio 1.6.11 release notes](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.11/).

For details on upgrading Anthos Service Mesh, refer to the following upgrade guides:

**1.6**

  * [Upgrading Anthos Service Mesh on GKE ](https://docs.cloud.google.com/service-mesh/docs/upgrading-gke)
  * [Upgrading Anthos Service Mesh on premises](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)



**1.5**

  * [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/docs/archive/1.5/docs/upgrading-gke)
  * [Upgrading Anthos Service Mesh on premises](https://docs.cloud.google.com/service-mesh/docs/archive/1.5/docs/gke-on-prem-upgrading)



**1.4**

  * [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/docs/archive/1.4/docs/upgrading-gke-1-4)
  * [Upgrading Anthos Service Mesh on premises](https://docs.cloud.google.com/service-mesh/docs/archive/1.4/docs/gke-on-prem-upgrading-1-4)



## August 27, 2020

1.6.x

**1.6.8-asm.9 is now available**

Adds Citadel CA support for `gcp` profiles.

Adds beta support for joining multiple clusters from [different projects](https://docs.cloud.google.com/service-mesh/docs/gke-install-overview) into a single Anthos Service Mesh on Google Kubernetes Engine.

Fixes an [issue](https://github.com/istio/istio/issues/26435) for enabling trust domain validation at the transport socket level.

## August 14, 2020

1.6.x & 1.5.x

**1.6.8-asm.0 and 1.5.9-asm.0**

Fixes the security issue, [ISTIO-SECURITY-2020-009](https://istio.io/latest/news/security/istio-security-2020-009), with the same fixes as Istio 1.6.8 and Istio 1.5.9. For more information, see the Istio release notes:

  * [Istio 1.6.8 release notes](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.8/)

  * [Istio 1.5.9 release notes](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.9/)




## July 24, 2020

1.6.x

Anthos Service Mesh on GKE on AWS is supported.

For more information, see [Installing Anthos Service Mesh on GKE on AWS](https://docs.cloud.google.com/service-mesh/docs/gke-on-aws-install).

## July 22, 2020

1.6.x

**1.6.5-asm.7, 1.5.8-asm.7, and 1.4.10-asm.15 are now available**

This release provides these features and fixes:

  * Builds Istiod (Pilot), Citadel Agent, Pilot Agent, Galley, and Sidecar Injector with [Go+BoringCrypto](https://go.googlesource.com/go/+/refs/heads/dev.boringcrypto).
  * Builds Istio Proxy (Envoy) with the [\--define boringssl=fips](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/ssl#fips-140-2) option.
  * Ensures the components listed above use FIPS-compliant algorithms.



## July 10, 2020

1.6.x

**1.6.5-asm.1, 1.5.8-asm.0, and 1.4.10-asm.4**

Fixes the security issue, [ISTIO-SECURITY-2020-008](https://istio.io/latest/news/security/istio-security-2020-008), with the same fixes as Istio 1.6.5 and Istio 1.5.8. These fixes were backported to 1.4.10-asm.4. For more information, see the Istio release notes:

  * [Istio 1.6.5](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.5/)

  * [Istio 1.5.8](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.8/)




## June 30, 2020

1.6.x

1.6.4-asm.9 is now available.

ASM 1.6 is compatible with and has the feature set of Istio 1.6 (see [Istio release notes](https://istio.io/latest/news/releases/1.6.x/announcing-1.6/)), subject to the list of [ASM Supported Features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

Upgrade from ASM 1.5 to ASM 1.6 without downtime using a [dual control plane upgrade](https://istio.io/latest/blog/2020/multiple-control-planes/).

In the `asm-multicloud` profile, ASM now installs a complete observability stack (Prometheus, Grafana and Kiali).

Anthos Service Mesh now supports cross-cluster security policies (beta) for your [multi-cluster mesh](https://docs.cloud.google.com/service-mesh/docs/gke-install-multi-cluster) when running on GKE on Google Cloud.

Support for cross-cluster load balancing (beta) for your [multi-cluster mesh](https://docs.cloud.google.com/service-mesh/docs/gke-install-multi-cluster) for GKE on Google Cloud.

The profile to install ASM in GKE has been renamed from `asm` to `asm-gcp`, see [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/docs/upgrading-gke). The profile to install ASM in GKE on-premise clusters has been renamed from `asm-onprem` to `asm-multicloud`, see [Upgrading Anthos Service Mesh on premises](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading).

Users that configure multiple clusters in their mesh can now see unified, multi-cluster views of their services in the Anthos Service Mesh pages in the Cloud Console. Note that multi-cluster support is in Beta and not all UI features are supported in multi-cluster mode.

Anthos Service Mesh now supports multi-cluster meshes (beta) when running on GKE on Google Cloud.

New installation guides: [Installing Anthos Service Mesh on attached clusters](https://docs.cloud.google.com/service-mesh/docs/attached-clusters-install) and [Adding clusters to an Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gke-install-multi-cluster).

ASM 1.6 is supported in a single cluster configuration in Anthos Attached Clusters in the following environments: Amazon Elastic Kubernetes Service (EKS) and Microsoft Azure Kubernetes Service (AKS).

Known Issue: If you upgrade from Istio to ASM 1.6 and have set SLOs on your service metrics, those SLOs might be lost and need to be recreated after the upgrade.

1.4.x & 1.5.x

1.5.7-asm.0 and 1.4.10-asm.3

Fixes the security issue, [ISTIO-SECURITY-2020-007](https://istio.io/latest/news/security/istio-security-2020-007/), with the same fixes as Istio 1.6.4. For information, see the [Istio release notes](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.4/).

**Description**

The vulnerability affects Anthos Service Mesh (ASM) versions 1.4.0 to 1.4.10, 1.5.0 to 1.5.5, and 1.6.4 whether running in Anthos clusters on VMware or on GKE, potentially exposing your application to Denial of Service (DOS) attacks. This vulnerability is referenced in these publicly disclosed Istio security bulletins: 

  * [ISTIO-SECURITY-2020-007](https://istio.io/news/security/istio-security-2020-007/): 
    * CVE-2020-12603 (CVSS score 7.0, High): Envoy through 1.14.1 may consume excessive amounts of memory when proxying HTTP/2 requests or responses with many small (e.g., 1 byte) data frames.
    * CVE-2020-12605 (CVSS score 7.0, High): Envoy through 1.14.1 may consume excessive amounts of memory when processing HTTP/1.1 headers with long field names or requests with long URLs.
    * CVE-2020-8663 (CVSS score 7.0, High): Envoy version 1.14.1 or earlier may exhaust file descriptors and/or memory when accepting too many connections.
    * CVE-2020-12604 (CVSS score 7.0, High): Envoy through 1.14.1 is susceptible to increased memory usage in the case where an HTTP/2 client requests a large payload but does not send enough window updates to consume the entire stream and does not reset the stream. The attacker can cause data associated with many streams to be buffered forever.



**Mitigation**

If you use ASM 1.6.4: * Apply the additional configuration changes specified in [ISTIO-SECURITY-2020-007](https://istio.io/latest/news/security/istio-security-2020-007/) to prevent Denial of Service (DOS) attacks on your mesh.

If you use ASM 1.4.0 to 1.4.10 or 1.5.0 to 1.5.5: * Upgrade your clusters to ASM 1.4.10-asm.3 or ASM 1.5.7-asm.0 as soon as possible and apply the additional configuration changes specified in [ISTIO-SECURITY-2020-007](https://istio.io/latest/news/security/istio-security-2020-007/) to prevent Denial of Service (DOS) attacks on your mesh.

  * See the following documentation for how to upgrade your Anthos Service Mesh.

    * ASM 1.5 for GKE and on-premises, respectively:
    * [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/docs/upgrading-gke)
    * [Upgrading Anthos Service Mesh on-prem](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)

    * ASM 1.4 for GKE and on-premises, respectively:

    * [Upgrading Anthos Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/docs/archive/1.4/docs/upgrading-gke-1-4)

    * [Upgrading Anthos Service Mesh on-prem](https://docs.cloud.google.com/service-mesh/docs/archive/1.4/docs/gke-on-prem-upgrading-1-4)




## June 22, 2020

1.4.x & 1.5.x

**1.5.6-asm.0 and 1.4.10.asm.2**

Contains the same fixes as OSS Istio 1.5.6. Non-critical, minor improvements were also backported to ASM 1.4.10. See [Announcing Istio 1.5.6](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.6/) for more information.

## June 15, 2020

1.5.x

**1.5.5-asm.2**

Fixes a bug in the `istioctl` `HorizontalPodAutoscaling` setting that caused Anthos Service Mesh installations to fail.

## June 11, 2020

1.4.x & 1.5.x

**1.5.5-asm.0 and 1.4.10-asm.1**

Fixes the security issue, CVE-2020-11080, with the same fixes as [OSS Istio 1.5.5](https://istio.io/news/releases/1.5.x/announcing-1.5.5/). The security fixes were backported to ASM 1.4.10.

**Description**

A vulnerability affecting the HTTP/2 library used by Envoy has been fixed and publicly disclosed (c.f. Denial of service: Overly large SETTINGS frames ). 

[CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080): By sending a specially crafted packet, an attacker could cause the CPU to spike at 100%. This could be sent to the ingress gateway or a sidecar.

**Mitigation**

HTTP/2 support could be disabled on the Ingress Gateway as a temporary workaround using the following configuration. HTTP/2 support at ingress can only be disabled if you are not exposing HTTP/2 services that cannot fallback to HTTP/1.1 through ingress. Note that gRPC services cannot fallback to HTTP/1.1.
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: EnvoyFilter
    metadata:
      name: disable-ingress-h2
      namespace: istio-system
    spec:
      workloadSelector:
        labels:
          istio: ingressgateway
      configPatches:
      - applyTo: NETWORK_FILTER # http connection manager is a filter in Envoy
        match:
          context: GATEWAY
          listener:
            filterChain:
              filter:
                name: "envoy.http_connection_manager"
        patch:
          operation: MERGE
          value:
            typed_config:
              "@type": type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager
              codec_type: HTTP1
    

For additional information, see [ISTIO-SECURITY-2020-006](https://istio.io/news/security/istio-security-2020-006).

## May 20, 2020

1.5.x

**1.5.4-asm.2**

1.5.4-asm.2 is now available.

**Security fixes**

1.5.4-asm.2 contains all the same security fixes that are in Anthos Service Mesh 1.4.

**Beta release of the Anthos CLI**

The Anthos CLI simplifies the installation of Anthos Service Mesh. You can use the Anthos CLI to:

  * Create a new cluster that meets the Anthos Service Mesh cluster requirements and install Anthos Service Mesh. See [Installing Anthos Service Mesh on a new cluster using the Anthos CLI](https://service-mesh/docs/gke-anthos-cli-new-cluster).
  * Update an existing cluster with the options that Anthos Service Mesh requires and install Anthos Service Mesh. See [Installing Anthos Service Mesh on an existing cluster using the Anthos CLI](https://service-mesh/docs/gke-anthos-cli-existing-cluster).



**Port change for automatic sidecar injection**

If you are installing Anthos Service Mesh on a private cluster, you must add a firewall rule to open port 15017 if you want to use [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/proxy-injection). In Anthos Service Mesh 1.4, the port used for automatic sidecar injection is 9443.

If you don't add the firewall rule and automatic sidecar injection is enabled, you get an error when you deploy workloads. For details on adding a firewall rule, see [Adding firewall rules for specific use cases](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules).

**The alpha authentication policy is deprecated**

See [Updating to the beta security policies](https://docs.cloud.google.com/service-mesh/docs/security/update-authentication-policies) for more information.

**`IstioOperator` API replaces `IstioControlPlane` API**

The alpha [`IstioControlPlane` API](https://archive.istio.io/v1.4/docs/reference/config/istio.operator.v1alpha12.pb/#IstioControlPlane) has been replaced by the [`IstioOperator` API](https://istio.io/docs/reference/config/istio.operator.v1alpha1/#IstioComponentSetSpec). You must use the `IstioOperator` API in YAML files to enable optional features when you install Anthos Service Mesh.

**Enabling pod security policies no longer needed**

SDS security was improved by merging Node Agent with Pilot Agent as Istio Agent and removing cross-pod UDS, which no longer requires users to deploy Kubernetes pod security policies for UDS connections.

**Istio CNI plugin is supported**

By default Anthos Service Mesh injects an `initContainer`, `istio-init`, in pods deployed in the mesh. The `istio-init` container sets up the pod network traffic redirection to/from the sidecar proxy. This requires the user or service-account deploying pods to the mesh to have sufficient Kubernetes RBAC permissions to deploy containers with the `NET_ADMIN` and `NET_RAW` capabilities. Requiring users to have elevated Kubernetes RBAC permissions is problematic for some organization's security compliance. The Istio Container Network Interface (CNI) plugin is a replacement for the `istio-init` container that performs the same networking functionality but without requiring users to enable elevated Kubernetes RBAC permissions.

The Istio CNI plugin performs the mesh pod traffic redirection in the Kubernetes pod lifecycle's network setup phase, thereby removing the requirement for the `NET_ADMIN` and `NET_RAW` capabilities for users deploying pods into the mesh. The Istio CNI plugin replaces the functionality provided by the `istio-init` container.

## May 12, 2020

1.4.x

1.4.9-asm.1

Fixes the security issue, CVE-2020-10739, with the same fixes as [OSS Istio 1.4.9](https://istio.io/news/releases/1.4.x/announcing-1.4.9/). See [ISTIO-SECURITY-2020-005](https://istio.io/news/security/istio-security-2020-005) for more information.

## April 28, 2020

1.4.x

The Anthos Service Mesh dashboard in the Google Cloud Console is generally available for Anthos Service Mesh installations on Google Kubernetes Engine clusters. For more information, see the [Observability overview](https://docs.cloud.google.com/service-mesh/docs/observability-overview).

## April 01, 2020

1.4.x

1.4.7-asm.0

Contains the same fixes as OSS Istio 1.4.7. See [Announcing Istio 1.4.7](https://istio.io/news/releases/1.4.x/announcing-1.4.7/) for more information.

## March 03, 2020

1.4.x

1.4.6-asm.0

Fixes known security issues with the same fixes as [OSS Istio 1.4.6](https://istio.io/news/releases/1.4.x/announcing-1.4.6/):

  * CVE-2020-8659, CVE-2020-8661, CVE-2020-8664, CVE-2020-8660: [ISTIO-SECURITY-2020-003](https://istio.io/news/security/istio-security-2020-003)



## February 28, 2020

1.4.x

1.4.5-asm.0

Anthos Service Mesh certificate authority (Mesh CA) is generally available for GKE on Cloud.

Mesh CA is a Google managed, highly available and secure service that replaces Citadel for Anthos Service Mesh customers on GKE on Cloud. Mesh CA issues mTLS certificates for workloads running in Anthos Service Mesh.

GKE on premises continues to use Citadel.

The changes to support the [Anthos Service Mesh observability features](https://docs.cloud.google.com/service-mesh/docs/observability), including the topology graph on the Anthos Service Mesh Dashboard are included in 1.4.5-asm-0.

Note that the Anthos Service Mesh Dashboard itself is still in beta.

1.5.x

Prepare for a breaking change coming in Anthos Service Mesh 1.5

**WARNING:** Don't include a [TargetSelector](https://archive.istio.io/v1.5/docs/reference/config/security/istio.authentication.v1alpha1/#TargetSelector) in your authentication polices. Authentication policies that include a `TargetSelector` will not be automatically converted to the new version of the Authentication Policy API that will be released in Anthos Service Mesh 1.5. You will have to migrate these authentication policies manually to the new Authentication Policy API. If you don't remove the `TargetSelector`, the authentication policies might be ignored without warning in Anthos Service Mesh 1.5.

## February 12, 2020

1.4.x

1.4.4-asm.0 

Fixes a [known security issue](https://istio.io/news/security/istio-security-2020-001/) with the same fixes as OSS Istio 1.4.4, as well as improvements from OSS Istio 1.4.3.

## December 20, 2019

1.4.x

Anthos Service Mesh is generally available.

This release features a supported, downloadable installation of Anthos Service Mesh for use in your Anthos clusters on-premises or on Google Kubernetes Engine.

The following features remain in beta:

  * [Service Mesh Dashboard for Google Kubernetes Engine clusters](https://docs.cloud.google.com/service-mesh/docs/access-dashboard)
  * [Observability of your services](https://docs.cloud.google.com/service-mesh/docs/observability)
  * [Anthos Service Mesh certificate authority (Mesh CA)](https://docs.cloud.google.com/service-mesh/docs/overview#security_features)



## October 28, 2019

0.1.x

Anthos Service Mesh certificate authority Beta.

## September 16, 2019

0.1.x

Anthos Service Mesh Beta. * [Service Mesh Dashboard for Google Kubernetes Engine clusters](https://docs.cloud.google.com/service-mesh/docs/access-dashboard) * [Observability of your services](https://docs.cloud.google.com/service-mesh/docs/observability)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
