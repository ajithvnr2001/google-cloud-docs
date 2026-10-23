---
url: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-observability/
title: Resolving observability and telemetry issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:47.549700+00:00
---

# Resolving observability and telemetry issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-observability/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving observability and telemetry issues in Cloud Service Mesh

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/docs/getting-support).

In Cloud Service Mesh telemetry, the Envoy proxies call the Google Cloud Observability APIs periodically to report telemetry data. The type of the API call determines its frequency:

  * **Logging** : every ~10 seconds
  * **Metrics** : every ~1 minute
  * **Edges (Context API/Topology view)** : incremental reports every ~1 minute, with full reports every ~10 minutes.
  * **Traces** : determined by the sampling frequency you configure (typically, one out of every 100 requests).

**Important:** Full telemetry might be delayed 1-2 minutes while clusters start.

The telemetry dashboards gather data from both Confluence and Google Cloud Observability to display the various service-focused dashboards.

## Verify that there is at most one Istio telemetry API configuration

This section only applies to managed Traffic Director control plane.

**Note:** In the rapid and regular channels, Cloud Service Mesh with a managed Traffic Director control plane supports multiple telemetry API configurations. Telemetry APIs are supported at the root namespace (default: `istio-system`, or as mentioned in the meshconfig), namespace level, and selector specific. Priority is highest for selector and lowest for root level. In other channels, only a single cluster-wide telemetry API configuration is supported, specifically, a single Istio telemetry API CR in the root namespace.

If you already have an existing Istio telemetry API CR, to preserve your previous customization settings in your existing Istio telemetry CR, you must include them within your new Istio telemetry API CR.

To list the telemetry API configurations, run the following command. Verify that there is at most one Istio telemetry API configuration.
    
    
    kubectl -n istio-system get telemetry

## Services dashboard is missing a service

The dashboard only displays HTTP(S)/gRPC services. If your service should be in the list, verify that Cloud Service Mesh telemetry identifies it as an HTTP service.

If your service remains missing, verify that a [Kubernetes service configuration](https://kubernetes.io/docs/concepts/services-networking/service/) exists in your cluster.

  * Review the list of all Kubernetes services:
        
        kubectl get services --all-namespaces

  * Review the list of Kubernetes services in a specific namespace:
        
        kubectl get services -n YOUR_NAMESPACE




## Missing or incorrect metrics for services

If there are missing or incorrect metrics for services in the Services dashboard, see the following sections for potential resolutions.

### Verify Sidecar proxies exist and have been injected properly

**Note:** You must have access to the cluster to troubleshoot missing or incorrect metrics.

The namespace might not have a label for automatic injection, or manual injection has failed. Confirm that the pods in the namespace have at least two containers and that one of those containers is the istio-proxy container:
    
    
    kubectl -n YOUR_NAMESPACE get pods

### Verify that telemetry configuration exists

To confirm that the Google Cloud Observability filter is configured, gather a configuration dump from each proxy and look for the presence of the Google Cloud Observability filter:
    
    
    kubectl debug --image istio/base --target istio-proxy -it YOUR_POD_NAME -n YOUR_NAMESPACE curl localhost:15000/config_dump

In output of the previous command, look for the Google Cloud Observability filter, which looks like the following:
    
    
    "config": {
        "root_id": "stackdriver_inbound",
        "vm_config": {
            "vm_id": "stackdriver_inbound",
            "runtime": "envoy.wasm.runtime.null",
            "code": {
                "local": {
                    "inline_string": "envoy.wasm.null.stackdriver"
                 }
             }
         },
         "configuration": "{....}"
    }

### Verify that Cloud Service Mesh identifies an HTTP service

Metrics won't show up in the user interface if the service port for the Kubernetes service is not named `http` or any name with an `http-` prefix. Confirm that the service has the proper names for its ports.

### Verify the Cloud Monitoring API is enabled for the project

Confirm that the Cloud Monitoring API is enabled in the APIs & Services dashboard in Google Cloud console, which is the default.

### Verify no errors reporting to the Cloud Monitoring API

In the Google Cloud console API & Services dashboard, open the Traffic By Response Code graph URL:
    
    
    https://console.cloud.google.com/apis/api/monitoring.googleapis.com/metrics?folder=&organizationId=&project=YOUR_PROJECT_ID

If you see error messages, it might be an issue that warrants further investigation. In particular, look for a large number of `429` error messages, which indicates a potential quota issue. See the next section for troubleshooting steps.

### Verify correct quota for the Cloud Monitoring API

In the Google Cloud console, open the `IAM & Admin` menu and verify there is a [Quotas](https://console.cloud.google.com/iam-admin/quotas) option. You can access this page directly using the URL:
    
    
    https://console.cloud.google.com/iam-admin/quotas?project=YOUR_PROJECT_ID

This page shows the full set of quotas for the project, where you can search for `Cloud Monitoring API`.

### Verify no error logs in Envoy proxies

Review the logs for the proxy in question, searching for error message instances:
    
    
    kubectl -n YOUR_NAMESPACE logs YOUR_POD_NAME -c istio-proxy

However, ignore the warning messages like the following, which are normal:
    
    
    [warning][filter] [src/envoy/http/authn/http_filter_factory.cc:83]
    mTLS PERMISSIVE mode is used, connection can be either plaintext or TLS,
    and client cert can be omitted. Please consider to upgrade to mTLS STRICT mode
    for more secure configuration that only allows TLS connection with client cert.
    See https://istio.io/docs/tasks/security/mtls-migration/ [warning][config]
    [bazel-out/k8-opt/bin/external/envoy/source/common/config/_virtual_includes/grpc_stream_lib/common/config/grpc_stream.h:91]
    gRPC config stream closed: 13

### Verify that `metric.mesh_uid` is set correctly

Open [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) and run the following MQL query:
    
    
    fetch istio_canonical_service
    | metric 'istio.io/service/server/request_count'
    | align delta(1m)
    | every 1m
    | group_by [metric.destination_canonical_service_namespace, metric.destination_canonical_service_name, metric.mesh_uid]
    

Verify that all expected services are reporting metrics, and that their `metric.mesh_uid` is in the format `proj-<Cloud Service Mesh fleet project number>`.

**Note:** For multi-project meshes, the project number must be the _fleet_ project, rather than the _host_ project.

If `metric.mesh_uid` has any other value, the Cloud Service Mesh dashboard won't display metrics. `metric.mesh_uid` is set when Cloud Service Mesh is installed on the cluster, so investigate your installation method to see if there's a way to set it to the expected value.

## Missing or incorrect telemetry data for services

By default, Cloud Monitoring and Cloud Logging are enabled in your Google Cloud project when you install Cloud Service Mesh. To report telemetry data, each sidecar proxy that is injected into your service pods calls the Cloud Monitoring API and the Cloud Logging API. After deploying workloads, it takes about one or two minutes for telemetry data to be displayed in the Google Cloud console. Cloud Service Mesh automatically keeps the service dashboards up to date:

  * For metrics, the sidecar proxies call the Cloud Monitoring API approximately every minute.
  * To update the Topology graph, the sidecar proxies send incremental reports approximately every minute and full reports about every ten minutes.
  * For logging, the sidecar proxies call the Cloud Logging API approximately every ten seconds.
  * For tracing, you have to enable Cloud Trace. Traces are reported according to the sampling frequency that you have configured (typically, one out of every 100 requests).



Metrics are displayed only for HTTP services on the Cloud Service Mesh Metrics page. If you don't see any metrics, verify that all the pods in the namespace for your application's services have sidecar proxies injected:
    
    
    kubectl get pod -n YOUR_NAMESPACE --all

In the output, notice that the `READY` column shows two containers for each of your workloads: the primary container and the container for the sidecar proxy.

Additionally, the Services dashboard only displays server metrics, so telemetry data may not appear if the client is not in the mesh or if it is configured to report only client metrics (such as ingress gateways).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
