---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/per-proxy-config/
title: Configure Envoy bootstrap attributes \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:12.111983+00:00
---

# Configure Envoy bootstrap attributes  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/per-proxy-config/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Envoy bootstrap attributes

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

When the Envoy proxies and gRPC libraries that power your service mesh initialize, they need to connect to Cloud Service Mesh and become Cloud Service Mesh clients. To establish this connection, a client needs to be bootstrapped with configuration information, for example:

  * Where to find Cloud Service Mesh (`trafficdirector.googleapis.com`)
  * The VPC network name for which the client should request configuration
  * Other optional information like whether to enable logging



This document covers how to supply bootstrapping information when using Envoy with Cloud Service Mesh. The method that you use to supply bootstrapping configuration varies depending on how you deploy your services:

  * For Envoy sidecar proxies deployed automatically with VMs, see [Options for VM setup with automated Envoy deployment](https://docs.cloud.google.com/service-mesh/docs/service-routing/auto-vms-options) for the parameter equivalents when you create an instance template.
  * For Envoy sidecar proxies deployed automatically with GKE Pods, add the supported parameters below to the `proxyMetadata` in the sidecar injector's `ConfigMap`. For more information about configuring required attributes, see [Set up Google Kubernetes Engine Pods with automated Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto).
  * For manual Envoy deployments, add the supported parameters below to your proxy's bootstrap node metadata configuration.



Only xDS v3 is supported. If you are using xDS v2, migrate to xDS v3 using the instructions is [Migrate from xDS v2 to xDS v3](https://docs.cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis#migrate_from_xds_v2_to_xds_v3).

## Required bootstrap configuration for manual Envoy deployments

The following table contains all required bootstrap configuration attributes.

Attribute | Value | Description  
---|---|---  
TRAFFICDIRECTOR_NETWORK_NAME | A string. For example: default. | Google Cloud VPC network name for which the configuration is requested (This is the VPC network name referenced in the forwarding rule in the Google Cloud API). With the xDS v3 API, you must provide the network name. Leaving this as an empty value is not recommended. An empty value is not guaranteed to be supported in future releases.   
TRAFFICDIRECTOR_GCP_PROJECT_NUMBER | A string of digits. For example, `123456789`. | The Google Cloud project where Cloud Service Mesh resources are configured. This is the numeric identifier of your project (for example, `111222333444`).  
You can get a list of all your projects with their corresponding project numbers by using the gcloud projects list command or reviewing the **Project info** section of the Google Cloud console. With the xDS v3 API, you must provide the project number.  
  
## Optional bootstrap configuration for manual Envoy deployments

The following table contains all optional bootstrap configuration attributes.

Attribute | Value | Description  
---|---|---  
TRAFFICDIRECTOR_INTERCEPTION_PORT | An integer in the range 0-65535 | A port number for the interception listener. Traffic destined to services configured in Cloud Service Mesh must be redirected to this port. If this value is left empty, the interception listener is not configured by Cloud Service Mesh. If your configuration depends on outbound traffic interception, the absence of the interception listener breaks the flow of traffic. This field is not required for middle proxy use cases where only inbound traffic must be intercepted.   
TRAFFICDIRECTOR_ACCESS_LOG_PATH | A path to the access log file, represented as a string. For example: "/var/log/sidecar/access.log" | The value of this parameter is used for file access log configuration, sent to a proxy by Cloud Service Mesh with other parameters. All incoming and outgoing requests are recorded in this file. For more information, refer to [File access log](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/access_loggers/file/v3/file.proto) documentation of the Envoy proxy.  
TRAFFICDIRECTOR_ENABLE_TRACING | Boolean, represented as a string; for example, `true` | Enables the sidecar proxy to generate distributed tracing information. If set to `true`, [Envoy tracing parameters](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-tracing) are programmed in the sidecar proxy by Cloud Service Mesh, and [generate_request_id](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto) set to "true".  
  
The following is an example in yaml format of how to configure the supported attributes in the node metadata section of the Envoy proxy bootstrap configuration:
    
    
    node:
      metadata:
        TRAFFICDIRECTOR_INTERCEPTION_PORT: "15001"
        TRAFFICDIRECTOR_NETWORK_NAME: "default"
        TRAFFICDIRECTOR_GCP_PROJECT_NUMBER: "111222333444"
        TRAFFICDIRECTOR_ACCESS_LOG_PATH: "/tmp/sidecar/access.log"
        TRAFFICDIRECTOR_ENABLE_TRACING: "true"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
