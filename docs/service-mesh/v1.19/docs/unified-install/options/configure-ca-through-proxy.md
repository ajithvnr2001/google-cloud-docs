---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/configure-ca-through-proxy/
title: Configure Certificate Authority connectivity through a proxy \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:27.477469+00:00
---

# Configure Certificate Authority connectivity through a proxy  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/configure-ca-through-proxy/

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

# Configure Certificate Authority connectivity through a proxy

This guide explains how to configure certificate authority (CA) connectivity through a proxy when direct connectivity from the sidecar-injected workloads is not available (for example, due to firewalls or other restrictive features). This configuration is only applicable for Cloud Service Mesh installations that use [Certificate Authority Service](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh#install_ca_service).

**Warning:** This guide only ensures CA connectivity through a proxy. However, note that Telemetry and Observability features (including metrics explorer, Cloud Service Mesh UI) **do not work** when workloads are behind a proxy.

In a typical in-cluster Cloud Service Mesh installation, you deploy sidecars in application pods where direct connectivity to CA services (such as `meshca.googleapis.com` and `privateca.googleapis.com`) is available. In scenarios where a direct connection is not available, you must configure an explicit `CONNECT`-based HTTPS proxy.

## Prerequisites

Before configuring CA connectivity through a proxy, ensure you have:

  * Established network connectivity from all sidecar injected pods to the HTTPS proxy.
  * Granted access for the deployed HTTPS proxy to all Google Cloud services.



## Configure a ProxyConfig custom resource

  1. Configure an [Istio ProxyConfig custom resource (CR)](https://istio.io/latest/docs/reference/config/networking/proxy-config/) to inject into the sidecar proxy to point to the HTTPS proxy. For example:
         
         apiVersion: networking.istio.io/v1beta1
         kind: ProxyConfig
         metadata:
          labels:
           istio.io/rev: <istio-rev>   # To target proxies mapped to a specific control plane if needed.
          name: test-proxy-inject
          namespace: istio-system      # To ensure side-cars injected into all namespaces process this CR
         spec:
          environmentVariables:
           CA_PLUGIN_PROXY_URL: http://<proxy-service>.<proxy-ns>:<proxy-port>
         

where:

     * `CA_PLUGIN_PROXY_URL` is the configuration consumed by sidecars to establish a `CONNECT` handshake with the proxy which then forwards all CA-destined traffic to the relevant endpoint.
     * `proxy-service` is deployed in the `proxy-ns` namespace and listening for `CONNECT` handshakes on `proxy-port` port. The format of this environment variable is similar to the standard `HTTPS_PROXY` environment variable.
  2. Once the Cloud Service Mesh control plane has been installed, apply the appropriate `ProxyConfig` CR (configured in step 1) on the cluster **before** restarting workloads in Cloud Service Mesh-labeled namespaces to ensure that the configuration is correctly injected into the sidecars. This configuration is required for sidecars to get signed workload certificates from the CA, which ensures that the sidecar injected pod can start up.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
