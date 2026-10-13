---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/observability-proxyless-grpc/
title: Observability for proxyless gRPC \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:49.158892+00:00
---

# Observability for proxyless gRPC  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/observability-proxyless-grpc/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability for proxyless gRPC

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Service Mesh Observability for proxyless gRPC builds on top of the [existing gRPC OpenTelemetry plugin](https://github.com/grpc/proposal/blob/master/A66-otel-stats.md), records metrics (latency, message sizes, etc.) for all gRPC channels and servers that are Cloud Service Mesh-enabled, and provides additional attributes that show topological mesh information for Cloud Service Mesh traffic. A gRPC channel is considered to be Cloud Service Mesh enabled if it gets configuration from the Cloud Service Mesh control plane, while all gRPC servers are considered Cloud Service Mesh enabled.

## Mesh Attributes

The following mesh attributes are available on metrics.

Local Environment Labels:

  * `csm.mesh_id`
    * The mesh ID.
  * Other local environment attributes are obtained from the [OpenTelemetry Resource](https://opentelemetry.io/docs/languages/js/resources/). 
    * [Managed Service for Prometheus (GMP)](https://cloud.google.com/managed-prometheus) can be set up to use Google infrastructure to store metrics. If using this, resource attributes that describe the application's local environment are automatically added in as a [MonitoredResource](https://cloud.google.com/monitoring/api/resources#tag_prometheus_target).
    * If using non-Google infrastructure for exporting and storing metrics, the collection pipeline should add in attributes on the metrics that describe the environment that the application is running on.



Remote Environment Labels:

  * `csm.remote_workload_type`
    * The type of the remote peer. ("gcp_kubernetes_engine" for GKE).
  * Based on the type of the peer, additional attributes would be present. 
    * For a peer running on GKE -
    * `csm.remote_workload_project_id`
      * The identifier of the project associated with this resource, such as "my-project".
    * `csm.remote_workload_location` *The physical location of the cluster that contains the container.
    * `csm.remote_workload_cluster_name`
      * The cluster where the container is running. 
    * `csm.remote_workload_namespace_name`
      * `The namespace where the container is running.`
    * `csm.remote_workload_name`
      * The name of the remote workload. This should be the name of the object that contains the Pod definition (for example, a Deployment, ReplicaSet, or just the Pod name for a bare Pod).



Service Labels: Information about the backend service (xDS cluster) that the RPC is being routed to. Note that this is only available if the backend service has been configured through the Gateway API.

  * `csm.service_name`
    * The service name.
  * `csm.service_namespace_name`
    * The service namespace name.



The term remote_workload refers to the peer, that is, for clients, the server Pod that is the target of an RPC is the remote workload, whereas for servers, the client Pod that initiated the RPC is the remote workload.

Note that these attributes won't be available on `grpc.client.attempt.started` and `grpc.server.call.started` since all topological mesh information is not available at the collection point of these metrics.

**Note:** `grpc.client.call.duration` is not available as a metric. `grpc.client.attempt.duration` and `grpc.server.call.duration` metrics are available.

## Observability setup instructions

This section explains how to enable Cloud Service Mesh Observability for proxyless gRPC on a service mesh setup.

### C++

Observability support is only available through the Bazel build system. The target `grpcpp_csm_observability` needs to be [added as a dependency](https://github.com/grpc/grpc/blob/4958cb95ce067a623c6909bea595ea4111eed12e/examples/cpp/csm/BUILD#L23).

### Required code changes

The following code needs to be added to your gRPC clients and servers in order to make use of Cloud Service Mesh observability.
    
    
    #include <grpcpp/ext/csm_observability.h>
    
    int main() {
      // …
      auto observability = grpc::CsmObservabilityBuilder()
                              .SetMeterProvider(std::move(meter_provider))
                              .BuildAndRegister();
      assert(observability.ok());
      // …
    }
    

Before any gRPC operations, including creating a channel, server, or credentials, use the CsmObservabilityBuilder API to register a plugin. The following sample shows how to set up Cloud Service Mesh Observability with a Prometheus exporter.
    
    
      opentelemetry::exporter::metrics::PrometheusExporterOptions opts;
      opts.url = "0.0.0.0:9464";
      auto prometheus_exporter =
          opentelemetry::exporter::metrics::PrometheusExporterFactory::Create(opts);
      auto meter_provider =
          std::make_shared<opentelemetry::sdk::metrics::MeterProvider>();
      meter_provider->AddMetricReader(std::move(prometheus_exporter));
      auto observability = grpc:::CsmObservabilityBuilder()
                              .SetMeterProvider(std::move(meter_provider))
                              .BuildAndRegister();
    

The `SetMeterProvider()` API on `CsmObservabilityBuilder()` allows users to set a [MeterProvider](https://opentelemetry.io/docs/specs/otel/metrics/sdk/) object that can be configured with exporters.

### Java

To enable Cloud Service Mesh Observability for Java gRPC applications, perform the following steps:

  1. Ensure project includes the `grpc-gcp-csm-observability` artifact. Use gRPC version 1.65.0 or later.

  2. Within `main()` method, initialize Cloud Service Mesh Observability by providing a configured OpenTelemetry SDK instance with a `MeterProvider` to collect and export metrics. 

Before you perform any gRPC operations like setting up a channel or server, make sure to use the `CsmObservability.Builder()` API to register OpenTelemetry SDK. 

Once the CsmObservability instance is created, invoking `registerGlobal()` on the instance enables Cloud Service Mesh Observability for all Cloud Service Mesh channels and servers.

The following example demonstrates how to set up Cloud Service Mesh Observability using a Prometheus exporter.



    
    
    import io.grpc.gcp.csm.observability.CsmObservability;
    ...
    
    public static void main(String[] args) {
        ...
    
        int prometheusPort = 9464;
    
        SdkMeterProvider sdkMeterProvider = SdkMeterProvider.builder()
            .registerMetricReader(
                PrometheusHttpServer.builder().setPort(prometheusPort).build())
            .build();
    
        OpenTelemetrySdk openTelemetrySdk = OpenTelemetrySdk.builder()
            .setMeterProvider(sdkMeterProvider)
            .build();
    
        CsmObservability observability = new CsmObservability.Builder()
            .sdk(openTelemetrySdk)
            .build();
        observability.registerGlobal();
    
        // ... (continue with channel and server configuration)
    }
    

### Go

Before any gRPC operations, including creating a ClientConn or Server, or credentials, configure Cloud Service Mesh Observability globally with a `MeterProvider`. The following sample shows how to set up Cloud Service Mesh Observability. After setting Cloud Service MeshObservability up, any Cloud Service Mesh Channels and all servers will pick up an OpenTelemetry stats plugin configured with provided options and with additional Cloud Service Mesh Labels. Non Cloud Service Mesh Channels will get an OpenTelemetry stats plugin without Cloud Service Mesh Labels.
    
    
      import (
      "context"
    
      "google.golang.org/grpc/stats/opentelemetry"
      "google.golang.org/grpc/stats/opentelemetry/csm"
    
      "go.opentelemetry.io/otel/sdk/metric"
    )
    
    func main() {
      reader := metric.NewManualReader()
      provider := metric.NewMeterProvider(metric.WithReader(reader))
      opts := opentelemetry.Options{
        MetricsOptions: opentelemetry.MetricsOptions{
            MeterProvider: provider,
        },
      }
      cleanup := csm.EnableObservability(context.Background(), opts)
      defer cleanup()
      // Any created ClientConns and servers will be configured with an
      // OpenTelemetry stats plugin configured with provided options.
    
    }
    

### Python

The following gRPC dependencies are required for Cloud Service Mesh Observability:
    
    
    grpcio>=1.65.0
    grpcio-observability>=1.65.0
    grpcio-csm-observability>=1.65.0
    

Before any gRPC operations, including creating a channel, server, or credentials, use the CsmOpenTelemetryPlugin API to create and register a plugin:
    
    
    import grpc_csm_observability
    
    # ...
    csm_plugin = grpc_csm_observability.CsmOpenTelemetryPlugin(
        meter_provider=[your_meter_provider],
    )
    csm_plugin.register_global()
    
    # Create server or client 
    

After all gRPC operations, use the following code to deregister and clean up resources:
    
    
    csm_plugin.deregister_global()
    

The following sample shows how to set up Cloud Service Mesh Observability with a Prometheus exporter:
    
    
    import grpc_csm_observability
    from opentelemetry.exporter.prometheus import PrometheusMetricReader
    from prometheus_client import start_http_server
    
    start_http_server(port=9464, addr="0.0.0.0")
    reader = PrometheusMetricReader()
    meter_provider = MeterProvider(metric_readers=[reader])
    csm_plugin = CsmOpenTelemetryPlugin(
        meter_provider=meter_provider,
    )
    csm_plugin.register_global()
    
    # Clean up after use
    
    csm_plugin.deregister_global()
    

In the previous sample, you can scrape `localhost:9464/metrics` to get the metrics reported by Cloud Service Mesh Observability.

Note that for the mesh attributes added onto the gRPC metrics to work, both the client and server binaries need to be set up with CsmObservability.

If using non-Google infrastructure for exporting and storing metrics, the collection pipeline should add in attributes on the metrics that describe the environment that the application is running on. This along with the mesh attributes described previously can be utilized to get a view of the traffic running on the mesh.

## Spec changes

Cloud Service Mesh Observability determines the mesh topological information through environment variables that need to be added to the container's env, both for clients and servers. This information is made available to peers for metrics reporting through Cloud Service Mesh Observability.
    
    
    spec:
      containers:
      - image: IMAGE_NAME
        name: CONTAINER_NAME
        env:
        - name: GRPC_XDS_BOOTSTRAP
          value: "/tmp/grpc-xds/td-grpc-bootstrap.json" #created by td-grpc-bootstrap
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: NAMESPACE_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
         - name: CSM_WORKLOAD_NAME
           value: CSM_WORKLOAD_NAME
         - name: CONTAINER_NAME
           value: CONTAINER_NAME
         - name: OTEL_RESOURCE_ATTRIBUTES
           value: k8s.pod.name=$(POD_NAME),k8s.namespace.name=$(NAMESPACE_NAME),k8s.container.name=CONTAINER_NAME
    

Replacing the following:

  * IMAGE_NAME with the name of the image.
  * CONTAINER_NAME with the name of the container.
  * CSM_WORKLOAD_NAME with the workload name, for example the deployment name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
