---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-install/
title: Plan an installation \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:07.567598+00:00
---

# Plan an installation  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-install/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Plan an installation

This page provides information to help you plan a new installation of Cloud Service Mesh.

**Note:** If you need to install Cloud Service Mesh from a private or custom container registry, see [Install Cloud Service Mesh from a custom container registry](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/enable-optional-features#use_a_custom_overlay_for_custom_registry).

## Customize the control plane

The features that Cloud Service Mesh supports differ between platforms. We recommend that you review the [Supported features](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-features) to learn which features are supported on your platform. Some features are enabled by default, and others you can optionally enable by creating an `IstioOperator` [overlay file](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#overlay_file). When you run `asmcli install`, you can customize the control plane by specifying the [`--custom_overlay`](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/reference) option with the overlay file. As a best practice, we recommend that you save the overlay files in your version control system.

The [`anthos-service-mesh`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.19/asm/istio/options) package in GitHub contains many overlay files. These files contain common customizations to the default configuration. You can use these files as they are, or you can make additional changes to them as needed. Some of the files are required to [enable optional Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/all-install-options). The `anthos-service-mesh` package is downloaded when you run `asmcli` to [validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#validate_project_and_cluster).

When you install Cloud Service Mesh using `asmcli install`, you can specify one or more overlay files with the `--option` or `--custom_overlay`. If you don't need to make any changes to the files in the `anthos-service-mesh` repository, you can use `--option`, and the script fetches the file from GitHub for you. Otherwise, you can make changes to the overlay file, and then use the `--custom_overlay` option to pass it to the `asmcli`.

## Choose a Certificate Authority

Depending on your use case, platform, and control plane type ([in-cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-features#certificate_authority_ca_support) or [managed](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp#certificate_authority_ca_support)), you can choose one of the following as the certificate authority (CA) for issuing [mutual TLS (mTLS)](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/security-overview#mutual_tls) certificates:

  * [Cloud Service Mesh certificate authority](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/security-overview#features)
  * [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [Istio CA](https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/)



This section provides high-level information about each of these CA options and their use cases.

### Mesh CA

Unless you require a custom CA, we recommend that you use Cloud Service Mesh certificate authority for the following reasons:

  * Cloud Service Mesh certificate authority is a highly reliable and scalable service that is optimized for dynamically scaled workloads.
  * With Cloud Service Mesh certificate authority, Google manages the security and availability of the CA backend.
  * Cloud Service Mesh certificate authority lets you rely on a single root of trust across clusters.



Certificates from Cloud Service Mesh certificate authority include the following data about your application's services:

  * The Google Cloud project ID
  * The GKE namespace
  * The GKE service account name

**Important:** The certificates issued by Mesh CA should only be used to enable secure service-to-service communication within your service mesh, and not be used for any other purpose. These certificates are sent whenever services attempt to communicate with each other using mutual TLS. Make sure that you don't inadvertently expose confidential information by using these certificates when communicating outside your service mesh.

### CA Service

**Platform note:** CA Service is only supported on the following platforms: GKE clusters on Google Cloud, Google Distributed Cloud, and Distributed Cloud. If you run `asmcli install` and specify `--ca gcp_cas` on other platforms, the installation appears successful, but your workloads will fail to start. 

In addition to [Mesh CA](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/security-overview#features), you can configure Cloud Service Mesh to use [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). This guide provides you an opportunity to integrate with CA Service, which is recommended for the following use cases:

  * If you need different certificate authorities to sign workload certificates on different clusters.
  * If you want to use `istiod` Custom CA plugin certificates.
  * If you need to back your signing keys in a [managed HSM](https://docs.cloud.google.com/kms/docs/hsm).
  * If you are in a highly regulated industry and are subject to compliance.
  * If you want to chain up your Cloud Service Mesh CA to a custom enterprise root certificate to sign workload certificates.



The cost of Mesh CA is included in the [Cloud Service Mesh pricing](https://cloud.google.com/service-mesh/pricing). The CA Service isn't included in the base Cloud Service Mesh price and is [charged separately](https://cloud.google.com/certificate-authority-service/pricing). Additionally, CA Service comes with an [explicit SLA](https://cloud.google.com/certificate-authority-service/sla), but the Mesh CA does not.

For this integration, all workloads in Cloud Service Mesh are granted [IAM roles](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles):

  * `privateca.workloadCertificateRequester`
  * `privateca.auditor`
  * `privateca.template` (_required if using a[certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template)_)



### Istio CA

We recommend that you use Istio CA if you meet the following criteria:

  * Your mesh already uses Istio CA and you do not require the benefits enabled by Cloud Service Mesh certificate authority or CA Service.
  * You require a custom root CA.
  * You have off-Google Cloud workloads where a Google Cloud-managed CA service is not acceptable.



## Prepare gateway configuration

Cloud Service Mesh gives you the option to deploy and manage gateways as part of your service mesh. A gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateways are Envoy proxies that provide you with fine-grained control over traffic entering and leaving the mesh.

`asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. For more information, see [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/v1.19/docs/gateways).

## What's next?

  * [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
