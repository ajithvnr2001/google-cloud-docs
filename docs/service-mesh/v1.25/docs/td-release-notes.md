---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/td-release-notes/
title: Cloud Service Mesh version 1.25 release note archive \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:54:16.655505+00:00
---

# Cloud Service Mesh version 1.25 release note archive  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/td-release-notes/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback 

#  Cloud Service Mesh version 1.25 release note archive Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Traffic Director, now known as Cloud Service Mesh. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/servicemesh-release-notes.xml) directly. 

## November 08, 2023

[Cloud Service Mesh advanced load balancing](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/advanced-load-balancing-overview), which is in Preview, is updated to include failover health threshold configuration.

## July 14, 2023

Read [Envoy Security Bulletin CVE-2023-35945](https://github.com/envoyproxy/envoy/security/advisories/GHSA-jfxv-29pc-x22r) about Envoy security vulnerabilities and update Envoy proxies in your Cloud Service Mesh installation to Envoy release 1.24.9, 1.25.8 or 1.26.3.

## January 11, 2023

gRPC Java releases 1.51.0, 1.51.1, and 1.52.0 have an important bug that can cause them to stop receiving updates from Cloud Service Mesh. We encourage users of gRPC Java to avoid these releases and use the older v1.50.x until patch releases with fixes are available. See the [public gRPC announcement](https://groups.google.com/g/grpc-io/c/roNyXX5pEAU?pli=1) for more information.

## December 16, 2022

A new series of enhancements for handling locality load balancing in proxyless mesh deployments is now available in GA. These enhancements let you do the following:

  * Create and use a list of preferred load-balancing policies. With this feature, if your first preferred policy can't be used by a particular client, gRPC falls back to the next policy on the list.

  * Use a custom load-balancing policy that you created and deployed with gRPC. As part of a related gRPC enhancement, a new set of APIs lets you capture metrics about query cost and server utilization. You can use these APIs to fine-tune your custom policy.




For more information about using these features, see [Locality load balancing](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#custom-lb-config).

**Caution:** This feature is intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration.

## November 23, 2022

Cloud Service Mesh deployment with automatic Envoy injection for GKE Pods currently installs Envoy version v1.24.0.

## November 18, 2022

The [backendServices API reference documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) now reflects that the outlierDetection object supports gRPC clients.

For more information about using the outlier detection feature with proxyless service mesh deployments, see the [Outlier detection section](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#outlier-detection) of the Cloud Service Mesh documentation.

## October 27, 2022

Cloud Service Mesh deployment with automatic Envoy injection for Google Kubernetes Engine Pods currently installs Envoy version 1.20.0.

## September 23, 2022

Cloud Service Mesh now supports outlier detection for proxyless service mesh deployments. Outlier detection lets you identify and temporarily eject unhealthy hosts from the load-balancing pool. gRPC evaluates hosts based on success rate—the frequency with which a host successfully handles requests. When you configure outlier detection through Cloud Service Mesh, you can fine-tune how gRPC assesses hosts and how it handles outliers.

**Note:** The API documentation for the outlierDetection object doesn't yet reflect that gRPC clients can use outlier detection. For the most up-to-date information about using the feature, see the [Outlier detection section](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#outlier-detection) of the Cloud Service Mesh documentation.

## September 19, 2022

The [Cloud Service Mesh service routing APIs](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview) are now in General Availability. The APIs simplify routing and service mesh configuration with new Mesh, Gateway, and Route resources.

## May 18, 2022

[Cloud Service Mesh for GKE now supports using the Kubernetes Gateway APIs](https://docs.cloud.google.com/service-mesh/legacy/gateway/gke-gateway-overview) to create a service mesh.

[Cloud Service Mesh control plane logging and monitoring](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/control-plane-observability) now supports request count by zone, in addition to DS API Connected Streams and request count.

## May 02, 2022

Cloud Service Mesh's [service routing APIs](https://docs.cloud.google.com/service-mesh/v1.25/docs/\(/service-mesh/v1.25/docs/service-routing/service-routing-overview\)) now include [Gateway TLS routing](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-gateway-tls-routing).

## March 14, 2022

A new client_zone label is added to the [Connected Streams](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/control-plane-observability#view_metrics) metric. The new label might introduce a breaking change. The change creates a stream discontinuity, which might have some effect on your monitoring, depending on whether you configured an alert on this metric.

## February 24, 2022

Read [Security Bulletin GCP-2022-008](https://docs.cloud.google.com/support/bulletins#GCP-2022-008) about Envoy security vulnerabilities and update Envoy proxies in your Cloud Service Mesh installation to Envoy release 1.21.1.

## February 15, 2022

[Cloud Service Mesh is now integrated with Service Directory](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-directory-integration). After you register a service with Service Directory, the integration makes services in the service registry available to the applications in your mesh and to gateways configured by Cloud Service Mesh. Your service mesh and self- managed gateways can then send traffic to these services.

## February 04, 2022

Cloud Service Mesh's [new service routing APIs](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview) are available in preview. The new APIs simplify routing and service mesh configuration with new Mesh, Gateway, and Route resources.

Related to this change, ]new options are available for automated Envoy deployment](/service-mesh/legacy/load-balancing-apis/auto-vms-options).

## December 16, 2021

[Cloud Service Mesh authorization policies are generally available for gRPC deployments with Java and Go clients](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-proxyless-setup#configure_service-level_access_with_an_authorization_policy).

## December 13, 2021

Control plane observability is now in Preview. This lets you view logs and metrics for the Cloud Service Mesh control plane. For more information, see [Control plane observability](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/control-plane-observability).

## December 01, 2021

Cloud Service Mesh support for Client Status Discovery Service (CSDS) API is now in General Availability. The CSDS API lets you see which clients are connected to Cloud Service Mesh and to inspect the configuration that Cloud Service Mesh generates for its clients. For more information, see [Understanding client status](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/client-status).

## November 15, 2021

Cloud Service Mesh [service security](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-overview) for GKE is now in General Availability. This provides the following:

  * Authentication and encryption using transport layer security (TLS) and mutual TLS (mTLS) for both Cloud Service Mesh with Envoy and proxyless gRPC applications. Server TLS policies and client TLS policies control whether services need to prove their identities to each other and use encrypted communication channels.

  * Authorization, based on characteristics of the client and the request. Authorization policies control whether a service is permitted to access another service, and which actions are allowed. Authorization is currently available only for Cloud Service Mesh with Envoy.




For more information, see the [service security documentation](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-overview) and setup guides.

## October 21, 2021

Cloud Service Mesh with internet NEGs of the type INTERNET_FQDN_PORT is now in General Availability. For full details, see [Cloud Service Mesh with internet network endpoint groups](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/internet-negs).

## October 20, 2021

[Cloud Service Mesh security service with GKE](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-overview) is now in General Availability for proxyless gRPC services. The changes in this release include:

  * Support for the Certificate Authority Service GA API, using [CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) instead of individual CAs.
  * Promoting the network-services and network-security CLI/APIs to general availability.
  * Security is enabled by default in gRPC libraries and the gRPC PSM bootstrap generator.
  * Cloud Logging enhancements to aid in debugging run-time errors and conflicts. Support for proxyless gRPC and Envoy interoperability with security enabled.
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) support for proxyless gRPC security.
  * Use of the new --enable-mesh-certificates GKE flag.
  * Support for the [GA version](https://docs.cloud.google.com/security.cloud.google.com/v1) of WorkloadCertificateConfig and TrustConfig in GKE.
  * [Wallet example](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/master) upgraded to use PSM security .



## August 30, 2021

Cloud Service Mesh deployed with proxyless gRPC can now use the [advanced traffic management features retry and session affinity](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).

## July 15, 2021

Cloud Service Mesh can now use internet NEGs of the type INTERNET_FQDN_PORT to route traffic to private services that are reachable using hybrid connectivity, including named on-premises, multicloud, and internet services. For full details, see [Cloud Service Mesh with internet network endpoint groups](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/internet-negs).

## June 29, 2021

You can now use VPC Service Controls with Cloud Service Mesh. You can add projects to service perimeters that protect resources and services (like Cloud Service Mesh) from requests that originate outside the perimeter. To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## June 02, 2021

Support for Go is added to [Cloud Service Mesh service security with proxyless gRPC](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-proxyless-setup).

## May 19, 2021

[Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/security-overview) with GKE is now available in Public Preview. This provides the following:

Authentication and encryption using transport layer security (TLS) and mutual TLS (mTLS) for both Cloud Service Mesh with Envoy and proxyless gRPC applications. Server TLS policies and client TLS policies control whether services need to prove their identities to each other and use encrypted communication channels.

Authorization, based on characteristics of the client and the request. Authorization policies control whether a service is permitted to access another service, and which actions are allowed. Authorization is currently available only for Cloud Service Mesh with Envoy.

## May 13, 2021

Fixed an issue where the Services user interface would display a warning if a service had a mix of healthy backend groups (x out of x healthy endpoints) and empty backend groups (0 out of 0 healthy endpoints). Now, services that have a mix of healthy backend groups and empty backend groups are shown as healthy.

## May 07, 2021

gRPC's observability features can now be used with services that use Cloud Service Mesh, including monitoring and tracing metrics that help you solve issues with your deployment. For more details, see [Observability with proxyless gRPC applications](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/observability-proxyless).

Proxyless gRPC applications can now use these advanced traffic management features:

  * Circuit breaking
  * Fault injection
  * Max stream duration



For complete information, see [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).

## April 22, 2021

Fixed an issue that caused unexpected behavior when handling malformed HTTP requests.

## April 13, 2021

Cloud Service Mesh now supports the Client Status Discovery Service (CSDS) API, enabling you to see which clients are connected to Cloud Service Mesh and to inspect the configuration that Cloud Service Mesh generates for its clients. For more information, see [Understanding client status](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/client-status).

## April 12, 2021

[Cloud Service Mesh now supports TCP-based services in GA](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-tcp). This brings service discovery, global load balancing, failover and many other Cloud Service Mesh capabilities to your non-HTTP services. See the [setup guide](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-tcp) to get started and the target proxies documentation for helpful background information.

## March 22, 2021

Cloud Service Mesh support for xDS clients that connect and request configuration using the xDS v3 API is now Generally Available. All guides have been updated to use xDS v3.

## January 21, 2021

Cloud Service Mesh support for xDS clients that connect and request configuration using the xDS v3 API is now in Preview.

## January 05, 2021

Cloud Service Mesh now supports TCP-based services in Preview. This brings service discovery, global load balancing, failover and many other Cloud Service Mesh capabilities to your non-HTTP services. See the [setup guide](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-tcp) to get started and the target proxies documentation for helpful background information.

## November 12, 2020

Cloud Service Mesh now supports multi-environment deployments. The hybrid connectivity network endpoint group (NEG) is in General Availability. The documentation includes [an overview of the feature](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/multi-environment-overview) and a tutorial,[Network edge services for multi-environment (on-premises, multi-cloud) deployments](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/network-edge-services-multi-environment).

## September 29, 2020

[Automated Envoy deployment for Google Compute Engine VMs](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-pods-auto) is now in General Availability.

## September 03, 2020

Cloud Service Mesh can now be set up for GKE Pods with [automatic Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto).

## August 26, 2020

Cloud Service Mesh supports [advanced traffic management features](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-advanced-traffic-management) with proxyless gRPC applications in General Availability. This release includes path- and header-based routing, as well as weight-based traffic splitting.

## July 21, 2020

Cloud Service Mesh supports [proxyless gRPC applications](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/proxyless-overview) in General Availability. In this deployment model, gRPC applications can participate in a service mesh without needing a sidecar proxy.

## July 07, 2020

Cloud Service Mesh now supports [Automated Envoy deployment for Google Compute Engine VMs](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-pods-auto) in Beta.

## May 06, 2020

A new document is added to Cloud Service Mesh: [Ingress traffic for your mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/ingress-traffic).

## April 15, 2020

A new document, [Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/features), is published.

## November 15, 2019

[Cloud Service Mesh traffic management with route rules and traffic policies](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/advanced-traffic-management) is available in General Availability.

## July 08, 2019

[Cloud Service Mesh traffic management with route rules and traffic policies](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/advanced-traffic-management) is available in Beta.

## June 20, 2019

[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview) is available in GA.

## March 15, 2019

[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview) is available in Beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
