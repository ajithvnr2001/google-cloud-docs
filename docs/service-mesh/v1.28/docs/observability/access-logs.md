---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/access-logs/
title: Request proxy logs \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:29.200214+00:00
---

# Request proxy logs  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/access-logs/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request proxy logs

Cloud Service Mesh supports two different types of access logs in Cloud Logging: Traffic logs (also known as Google Cloud Observability access logs) and Envoy access logs. This page shows you how to enable, disable, view, and interpret these logs. Note that traffic logs are enabled by default.

## Enabling and disabling access logs

### Managed Traffic Director

**Note:** In the rapid and regular channels, Cloud Service Mesh with a managed Traffic Director control plane supports multiple telemetry API configurations. Telemetry APIs are supported at the root namespace (default: `istio-system`, or as mentioned in the meshconfig), namespace level, and selector specific. Priority is highest for selector and lowest for root level. In other channels, only a single cluster-wide telemetry API configuration is supported, specifically, a single Istio telemetry API CR in the root namespace.

If you already have an existing Istio telemetry API CR, to preserve your previous customization settings in your existing Istio telemetry CR, you must include them within your new Istio telemetry API CR.

### Envoy access logs

Run the following command to enable Envoy access logs and disable traffic logs:
    
    
    cat <<EOF | kubectl apply -n istio-system -f -
    apiVersion: telemetry.istio.io/v1alpha1
    kind: Telemetry
    metadata:
      name: enable-envoy-disable-sd
      namespace: istio-system
    spec:
      accessLogging:
      - providers:
          - name: envoy
      - providers:
          - name: stackdriver
        disabled: true
    EOF
    

Note that the provider name for traffic log is `stackdriver`.

### Traffic logs

By default, traffic logs are enabled and Envoy access logs are disabled. If you previously enabled Envoy access logs and want to enable traffic logs and disable Envoy access logs, run the following command:
    
    
    cat <<EOF | kubectl apply -n istio-system -f -
    apiVersion: telemetry.istio.io/v1alpha1
    kind: Telemetry
    metadata:
      name: disable-envoy-enable-sd
      namespace: istio-system
    spec:
      accessLogging:
      - providers:
          - name: envoy
        disabled: true
      - providers:
          - name: stackdriver
    EOF
    

### Both

  * To enable both Envoy access logs and traffic logs, run the following command:
        
        cat <<EOF | kubectl apply -n istio-system -f -
        apiVersion: telemetry.istio.io/v1alpha1
        kind: Telemetry
        metadata:
          name: enable-envoy-and-sd-access-log
          namespace: istio-system
        spec:
          accessLogging:
          - providers:
              - name: envoy
              - name: stackdriver
        EOF
        

  * To disable both Envoy access logs and traffic logs, run the following command:
        
        cat <<EOF | kubectl apply -n istio-system -f -
        apiVersion: telemetry.istio.io/v1alpha1
        kind: Telemetry
        metadata:
          name: disable-envoy-and-sd
          namespace: istio-system
        spec:
          accessLogging:
          - providers:
              - name: envoy
            disabled: true
          - providers:
              - name: stackdriver
            disabled: true
        EOF
        




### Selector-specific access logs

In the rapid and regular channels, to enable access logging for only a specific workload, you first need to disable it at the mesh-wide level by applying a Telemetry Configuration in the root namespace (since traffic logging is enabled by default). Then, you apply a separate configuration with a selector to enable it just for that workload.
    
    
    # 1. Disable mesh-wide access logging
    cat <<EOF | kubectl apply -n istio-system -f -
    apiVersion: telemetry.istio.io/v1alpha1
    kind: Telemetry
    metadata:
      name: disable-mesh-wide-telemetry
      namespace: istio-system
    spec:
      accessLogging:
      - providers:
        - name: stackdriver
        disabled: true
    EOF
    
    # 2. Enable access logging for a specific workload
    cat <<EOF | kubectl apply -n NAMESPACE -f -
    apiVersion: telemetry.istio.io/v1alpha1
    kind: Telemetry
    metadata:
      name: workload-specific-telemetry
      namespace: NAMESPACE
    spec:
      selector:
        matchLabels:
          app: YOUR_APP_LABEL
      accessLogging:
      - providers:
        - name: stackdriver
    EOF
    

### Managed `istiod`

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

### Envoy access logs

Run the following commands to enable Envoy access logging:

**Warning:** You can overwrite your own changes. If you already have an existing configmap, you must include all previous customization settings within the `mesh:` section to preserve your changes. This ensures no downtime when enabling optional features.

  1. Run the following command to add `accessLogFile: /dev/stdout`:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: v1
         data:
           mesh: |-
             accessLogFile: /dev/stdout
         kind: ConfigMap
         metadata:
           name: istio-release-channel
           namespace: istio-system
         EOF
         

where release-channel is your [release channel](https://docs.cloud.google.com/service-mesh/v1.28/docs/managed/select-a-release-channel) (`asm-managed`, `asm-managed-stable`, or `asm-managed-rapid`).

  2. Run the following command to view the configmap:
         
         kubectl get configmap istio-release-channel -n istio-system -o yaml
         

  3. To verify that access logging is enabled, ensure the `accessLogFile: /dev/stdout` line appears in the `mesh:` section.
         
         ...
         apiVersion: v1
         data:
           mesh: |
             ....
             accessLogFile: /dev/stdout
         ...
         




### Traffic logs

Traffic logs are enabled by default.

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

### Envoy access logs
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        accessLogFile: "/dev/stdout"

For more information, see [Enable Envoy's access logging](https://istio.io/v1.28/docs/tasks/observability/logs/access-log/#enable-envoy-s-access-logging).

### Traffic logs

Traffic logs are enabled by default, **unless Cloud Service Mesh is installed on _Google Distributed Cloud with Istio CA_ (previously known as Citadel)**.

To enable traffic logs on Google Distributed Cloud with Istio CA _when[installing in-cluster Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh)_, use the flag `--option stackdriver`. Alternatively, you can enable traffic logs on Google Distributed Cloud with Istio CA _[after installing in-cluster Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/options/enable-optional-features#stackdriver)_.

## Viewing access logs

### Envoy access logs

### Command line

To view Envoy access logs in the istio-proxy log, run the following command:
    
    
    kubectl logs POD_NAME -n NAMESPACE_NAME -c istio-proxy
    

###  Logs Explorer 

To view Envoy access logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. Navigate to the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the appropriate Google Cloud project.

  3. Run the following query:



    
    
    resource.type="k8s_container" \
    resource.labels.container_name="istio-proxy"
    resource.labels.cluster_name="CLUSTER_NAME" \
    resource.labels.namespace_name="NAMESPACE_NAME" \
    resource.labels.pod_name="POD_NAME"
    

### Traffic logs

To view traffic logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. Navigate to the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the appropriate Google Cloud project.

  3. Run the following query depending on whether you are viewing client or server access logs:

### Server logs
         
         resource.labels.cluster_name="CLUSTER_NAME" logName="projects/PROJECT_NAME/logs/server-accesslog-stackdriver"
         

### Client logs
         
         resource.labels.cluster_name="CLUSTER_NAME" logName="projects/PROJECT_NAME/logs/client-accesslog-stackdriver"
         




To view traffic logs in the Cloud Service Mesh page for a Service during a specified time span, follow these steps:

  1. In Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/kubernetes/services)

  2. Under **Services** , select the name of the Service you want to inspect.

  3. Go to the **Metrics** page.

  4. Specify a time span from the **Time Span** drop-down menu or [set a custom span with the timeline](https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/explore-dashboard#working_with_the_timeline).

  5. Under _filter_list_ **Select a filter option** , click **View traffic logs**.




The traffic log is named as **server-accesslog-stackdriver** and is attached to the corresponding monitored resource ([k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) or [gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)) your service is using. The traffic log contains the following information:

  * HTTP request properties, such as ID, URL, size, latency, and common headers.

  * Source and destination workload information, such as name, namespace, identity, and common labels.

  * If tracing is enabled, trace information, such as sampling, trace ID, and span ID.




An example log entry looks like the following:
    
    
    {
      insertId: "1awb4hug5pos2qi"
      httpRequest: {
        requestMethod: "GET"
        requestUrl: "YOUR-INGRESS/productpage"
        requestSize: "952"
        status: 200
        responseSize: "5875"
        remoteIp: "10.8.0.44:0"
        serverIp: "10.56.4.25:9080"
        latency: "1.587232023s"
        protocol: "http"
      }
      resource: {
        type: "k8s_container"
        labels: {
          location: "us-central1-a"
          project_id: "YOUR-PROJECT"
          pod_name: "productpage-v1-76589d9fdc-ptnt9"
          cluster_name: "YOUR-CLUSTER-NAME"
          container_name: "productpage"
          namespace_name: "default"
        }
      }
      timestamp: "2020-04-28T19:55:21.056759Z"
      severity: "INFO"
      labels: {
        destination_principal: "spiffe://cluster.local/ns/default/sa/bookinfo-productpage"
        response_flag: "-"
        destination_service_host: "productpage.default.svc.cluster.local"
        source_app: "istio-ingressgateway"
        service_authentication_policy: "MUTUAL_TLS"
        source_name: "istio-ingressgateway-5ff85d8dd8-mwplb"
        mesh_uid: "YOUR-MESH-UID"
        request_id: "021ce752-9001-4ac6-b6d6-3b15f5d3632"
        destination_namespace: "default"
        source_principal:  "spiffe://cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account"
        destination_workload: "productpage-v1"
        destination_version: "v1"
        source_namespace: "istio-system"
        source_workload: "istio-ingressgateway"
        destination_name: "productpage-v1-76589d9fdc-ptnt9"
        destination_app: "productpage"
      }
      trace: "projects/YOUR-PROJECT/traces/d4197f59b7a43e3aeff3571bac99d536"
      receiveTimestamp: "2020-04-29T03:07:14.362416217Z"
      spanId: "43226343ca2bb2b1"
      traceSampled: true
      logName: "projects/YOUR-PROJECT/logs/server-accesslog-stackdriver"
      receiveTimestamp: "2020-04-28T19:55:32.185229100Z"
    }

## Interpret Cloud Service Mesh telemetry

The following sections explain how to check the status of your mesh and review the various telemetry that contain helpful details to assist your troubleshooting.

### Interpret control plane metrics

### Managed Traffic Director

Cloud Service Mesh with a managed Traffic Director control plane doesn't support control plane metrics.

### Managed `istiod`

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

Cloud Service Mesh with a managed `istiod` control plane doesn't support the control plane metric inspection in this section.

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

When installing Cloud Service Mesh with the in-cluster control plane, `istiod` exports metrics to Google Cloud Observability for monitoring, by default. `istiod` prefixes these metrics with `istio.io/control` and give insights into the control plane state, such as number of proxies connected to each control plane instance, configuration events, pushes and validations.

Observe or troubleshoot the control plane, using the following steps.

  1. Load a sample dashboard:
         
         git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples && cd monitoring-dashboard-samples/dashboards && git checkout servicemesh

  2. Install the Cloud Service Mesh dashboard:
         
         gcloud monitoring dashboards create --config-from-file=dashboards/servicemesh/anthos-service-mesh-control-plane-monitoring.json

  3. Look for a dashboard named `Istio Control Plane Dashboard` in the list. For more information, see [Viewing the installed dashboard](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates#view-installed-template).




For the full list of metrics available, see [Exported metrics](https://istio.io/v1.28/docs/reference/commands/istioctl/#metrics).

#### Diagnose configuration delays

### Managed Traffic Director

Cloud Service Mesh with a managed Traffic Director control plane doesn't support diagnosing configuration delays.

### Managed `istiod`

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

Cloud Service Mesh with a managed istiod control plane doesn't support diagnosing configuration delays.

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

The following steps explain how to use the `pilot_proxy_convergence_time` metric to diagnose a delay between a configuration change and all proxies converging.

  1. Run a shell command in a pod:
         
         kubectl debug --image istio/base --target istio-proxy -it $(kubectl get pod -l app=pilot -o jsonpath='{.items[0].metadata.name}' -n istio-system) -n istio-system -- curl -s

  2. Access `localhost:15014` and `grep` for `convergence` in metrics:
         
         curl http://localhost:15014/metrics | grep convergence




### Interpret traffic logs

The following information explains how to use the traffic logs to troubleshoot connection problems. Traffic logs are enabled by default.

Cloud Service Mesh exports data into traffic logs that can help you debug the following types of problems:

  * Traffic flow and failures
  * End-to-end request routing



Traffic logs are enabled by default for Cloud Service Mesh installations on Google Kubernetes Engine. You can enable traffic logs by re-running `asmcli install`. Use the same options that you originally installed but omit the custom overlay that disabled Stackdriver.

There are two types of traffic logs:

  * Server access logs give a server-side view of requests. They are located under `server-accesslog-stackdriver`, attached to the `k8s_container` monitored resource. Use the following URL syntax to display server-side access logs:
        
        https://console.cloud.google.com/logs/viewer?advancedFilter=logName="projects/PROJECT_ID/logs/server-accesslog-stackdriver"&project=PROJECT_ID

  * Client access logs give a client-side view of requests. They are located under `client-accesslog-stackdriver`, attached to the `k8s_pod` monitored resource. Use the following URL syntax to display client-side access logs:
        
        https://console.cloud.google.com/logs/viewer?advancedFilter=logName="projects/PROJECT_ID/logs/client-accesslog-stackdriver"&project=PROJECT_ID




Access logs contain the following information:

  * HTTP request properties, such as ID, URL, size, latency, and common headers.
  * Source and destination workload information, such as name, namespace, identity, and common labels.
  * Source and destination canonical service and revision information.
  * If tracing is enabled, the logs contain trace information, such as sampling, trace ID, and span ID.



Traffic logs may contain the following labels:

  * `route_name`
  * `upstream_cluster`
  * `X-Envoy-Original-Path`



This is an example log entry:
    
    
    {
      "insertId": "1j84zg8g68vb62z",
      "httpRequest": {
        "requestMethod": "GET",
        "requestUrl": "http://35.235.89.201:80/productpage",
        "requestSize": "795",
        "status": 200,
        "responseSize": "7005",
        "remoteIp": "10.168.0.26:0",
        "serverIp": "10.36.3.153:9080",
        "latency": "0.229384205s",
        "protocol": "http"
      },
      "resource": {
        "type": "k8s_container",
        "labels": {
          "cluster_name": "istio-e2e22",
          "namespace_name": "istio-bookinfo-1-68819",
          "container_name": "productpage",
          "project_id": "***",
          "location": "us-west2-a",
          "pod_name": "productpage-v1-64794f5db4-8xbtf"
        }
      },
      "timestamp": "2020-08-13T21:37:42.963881Z",
      "severity": "INFO",
      "labels": {
        "protocol": "http",
        "upstream_host": "127.0.0.1:9080",
        "source_canonical_service": "istio-ingressgateway",
        "source_namespace": "istio-system",
        "x-envoy-original-path": "",
        "source_canonical_revision": "latest",
        "connection_id": "32",
        "upstream_cluster": "inbound|9080|http|productpage.istio-bookinfo-1-68819.svc.cluster.local",
        "requested_server_name": "outbound_.9080_._.productpage.istio-bookinfo-1-68819.svc.cluster.local",
        "destination_version": "v1",
        "destination_workload": "productpage-v1",
        "source_workload": "istio-ingressgateway",
        "destination_canonical_revision": "v1",
        "mesh_uid": "cluster.local",
        "source_principal": "spiffe://cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account",
        "x-envoy-original-dst-host": "",
        "service_authentication_policy": "MUTUAL_TLS",
        "destination_principal": "spiffe://cluster.local/ns/istio-bookinfo-1-68819/sa/bookinfo-productpage",
        "response_flag": "-",
        "log_sampled": "false",
        "destination_service_host": "productpage.istio-bookinfo-1-68819.svc.cluster.local",
        "destination_name": "productpage-v1-64794f5db4-8xbtf",
        "destination_canonical_service": "productpage",
        "destination_namespace": "istio-bookinfo-1-68819",
        "source_name": "istio-ingressgateway-6845f6d664-lnfvp",
        "source_app": "istio-ingressgateway",
        "destination_app": "productpage",
        "request_id": "39013650-4e62-9be2-9d25-78682dd27ea4",
        "route_name": "default"
      },
      "logName": "projects/***/logs/server-accesslog-stackdriver",
      "trace": "projects/***t/traces/466d77d15753cb4d7749ba5413b5f70f",
      "receiveTimestamp": "2020-08-13T21:37:48.758673203Z",
      "spanId": "633831cb1fda4fd5",
      "traceSampled": true
    }

You can use this log in various ways:

  * Integrate with Cloud Trace, which is an optional feature in Cloud Service Mesh.
  * Export traffic logs to BigQuery, where you can run queries like selecting all requests take more than 5 seconds.
  * Create log-based metrics.
  * Troubleshoot `404` and `503` errors



#### Troubleshoot `404` and `503` errors

The following example explains how to use this log to troubleshoot when a request fails with a `404` or `503` response code.

  1. In the client access log, search for an entry like the following:
         
         httpRequest: {
         requestMethod: "GET"
         requestUrl: "://IP_ADDRESS/src/Util/PHP/eval-stdin.php"
         requestSize: "2088"
         status: 404
         responseSize: "75"
         remoteIp: "10.168.0.26:34165"
         serverIp: "10.36.3.149:8080"
         latency: "0.000371440s"
         protocol: "http"
         }

  2. Navigate to the labels in the access log entry. Find the `response_flag` field that looks like the following:
         
         response_flag: "NR"

The `NR` value is an acronym for `NoRoute`, which means no route was found for the destination or there was no matching filter chain for a downstream connection. Similarly, you can use the `response_flag` label to troubleshoot `503` errors also.

  3. If you see `503` errors in both the client and server access logs, check that the port names set for each service match the name of the protocol in use between them. For example, if a golang binary client connects to a golang server using HTTP, but the port is named `http2`, the protocol will not auto-negotiate correctly.




For more information, see [response flags](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage#config-access-log-format-response-flags).

### Interpret Envoy access logs

The following steps explain how to use the Envoy access logs to show traffic between both ends of a connection for troubleshooting purposes.

Envoy access logs are useful for diagnosing issues like:

  * Traffic flow and failures
  * End-to-end request routing



Envoy access logs are not enabled by default in Cloud Service Mesh and can be enabled for the clusters in a mesh.

**Note:** Traffic logs (also known as the [Google Cloud Observability](https://docs.cloud.google.com/logging/docs) logs) are the preferred logs for most troubleshooting scenarios. However, if the issue persists, enable Envoy access logs to troubleshoot further.

You can troubleshoot connection or request failures by generating activity in your application that triggers an HTTP request, then inspecting the associated request in the source or destination logs.

If you trigger a request appears and it appears in the source proxy logs, it indicates that `iptables` traffic redirection is working correctly and the Envoy proxy is handling traffic. If you see errors in the logs, generate an Envoy configuration dump and check the Envoy cluster configuration to ensure it is correct. If you see the request but the log has no errors, check the destination proxy logs instead.

If the request appears in the destination proxy logs, it indicates that the mesh itself is working correctly. If you see an error instead, run an Envoy configuration dump and verify the correct values for the traffic port set in the listener configuration.

If the problem persists after performing the previous steps, Envoy might be unable to auto-negotiate the protocol between the sidecar and its application pod. Ensure that the Kubernetes service port name, for example `http-80`, matches the protocol that the application uses.

### Use Logs Explorer to query logs

You can use the [Logs Explorer interface](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to query specific Envoy access logs. For example, to query all requests that have `MULTUAL_TLS` enabled and use protocol `grpc`, append following to the server access logs query:
    
    
    labels.protocol="grpc" labels.service_authentication_policy="MULTUAL_TLS"

### Set an access log policy

### Managed Traffic Director

To configure access logs for Cloud Service Mesh with a managed Traffic Director control plane, see Enabling access logs.

### Managed `istiod`

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

To configure access logs for Cloud Service Mesh with a managed istiod control plane, see Enabling access logs.

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

To set an access log policy for Cloud Service Mesh with the in-cluster control plane:

  1. Create an `IstioOperator` custom overlay file that includes the applicable [`AccessLogPolicyConfig`](https://istio.io/v1.22/docs/reference/config/proxy_extensions/accesslogpolicy/) values for your scenario.

  2. Pass this file to `asmcli` using the `--custom_overlay` option to update the in-cluster control plane configuration. For information on running `asmcli install` with a custom overlay file, see [Install with optional features](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/install-anthos-service-mesh#install_with_optional_features).

**Caution:** If you customized the previous installation, you need the same customizations when you reinstall the control plane to include the file with the `AccessLogPolicyConfig` settings. Omitting an overlay file results in a successful installation; however, your service mesh has a different configuration than you intended because the omitted values are reset back to the defaults when the control plane is redeployed.



### View service or workload-specific information

If you have an issue with a specific service or workload rather than a mesh-wide problem, inspect the individual Envoy proxies and gather relevant information from them. To gather information about a particular workload and its proxies, you can use `pilot-agent`:
    
    
    kubectl exec POD_NAME -n NAMESPACE_NAME -c istio-proxy -- pilot-agent request GET SCOPE

In the example, SCOPE is one of the following:

  * `certs` \- Certificates within the Envoy instance
  * `clusters` \- Clusters with Envoy configured
  * `config_dump` \- Dumps the Envoy configuration
  * `listeners` \- Listeners with Envoy configured
  * `logging` \- View and change logging settings
  * `stats` \- Envoy statistics
  * `stats/prometheus` \- Envoy statistics as Prometheus records

**Note:** `config_dump` and `stats` are the options that are most likely to produce actionable information.

#### View proxy socket states

You can directly examine the state of Envoy proxy sockets by using the following process.

  1. Display a list of established sockets, including sockets in the `TIME_WAIT` state, which can negatively affect scalability if their count is high:
         
         kubectl debug --image istio/base --target istio-proxy -it POD_NAME -n NAMESPACE_NAME -- ss -anopim

  2. Display a summary of socket statistics:
         
         kubectl debug --image istio/base --target istio-proxy -it POD_NAME -n NAMESPACE_NAME -- ss -s




For more information, see [An Introduction to the ss Command](https://www.linux.com/topic/networking/introduction-ss-command/).

#### `istio-proxy` and `istio-init` logs

In addition, retrieve the `istio-proxy` logs and review its contents for any errors that might suggest the cause of the problem:
    
    
    kubectl logs POD_NAME -n NAMESPACE_NAME -c istio-proxy

You can do the same for the `init` container:
    
    
    kubectl logs POD_NAME -n NAMESPACE_NAME -c istio-init

## What's next

  * [Integrate with Cloud Trace](https://docs.cloud.google.com/trace/docs/trace-log-integration). Cloud Trace is an [optional feature](https://docs.cloud.google.com/service-mesh/v1.28/docs/unified-install/options/enable-optional-features#command-line_options_to_enable_optional_features) in Cloud Service Mesh.

  * [Export traffic logs to BigQuery](https://docs.cloud.google.com/logging/docs/export/bigquery).

  * [Create log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
