---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/deploy/
title: Setup overview \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:09.824806+00:00
---

# Setup overview  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/deploy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Setup overview

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies to Cloud Service Mesh with the load balancing APIs. We strong recommend that you deploy with the service routing APIs instead. Start by reading [](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview) rather than this document.

The documentation that you need for deploying Cloud Service Mesh with the load balancing APIs depends on the following:

  * Whether you are using Cloud Service Mesh with or without Envoy proxies
  * Whether you are using Compute Engine virtual machine (VM) instances or Google Kubernetes Engine (GKE) Pods



This guide tells you where to start with the documentation.

If you are deploying with the GKE Gateway API, read [Prepare to set up with the GKE Gateway API](https://docs.cloud.google.com/service-mesh/legacy/gateway/prepare-gateway).

## Deploy Cloud Service Mesh with Envoy on Compute Engine VMs

  1. Start by reading [Prepare to set up Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-for-envoy-setup).
  2. If you are using Compute Engine VMs with automatic Envoy deployment, read these documents: 
     * [Set up Compute Engine VMs with automatic Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms-auto)
     * [Options for Compute Engine VM setup with automatic Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-vms-options)
  3. If you are using Compute Engine VMs with manual Envoy deployment, read [Set up Compute Engine VMs with manual Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms).



## Deploy Cloud Service Mesh with Envoy on GKE Pods

  1. Start by reading [Prepare to set up Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-for-envoy-setup).
  2. If you are using GKE Pods with automatic Envoy injection, read these documents: 
     * [Set up GKE Pods with automatic Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto)
     * [Options for GKE Pod setup with automatic Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-gke-options)
  3. If you are using GKE Pods with manual Envoy injection, read [Set up GKE Pods with manual Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods).
  4. To configure authentication and authorization for services deployed with Cloud Service Mesh and Envoy proxies, read [Set up Cloud Service Mesh service security with Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-envoy-setup).



## Deploy Cloud Service Mesh with proxyless gRPC applications

  1. Start by reading [Prepare to set up Cloud Service Mesh with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-proxyless-grpc).
  2. If you are using Compute Engine VMs, read [Cloud Service Mesh setup with Compute Engine VMs and proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gce).
  3. If you are using GKE Pods, read [Cloud Service Mesh setup with GKE and proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke).
  4. To configure a security service for a proxyless gRPC service mesh, read [Set up Cloud Service Mesh service security with proxyless gRPC](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
