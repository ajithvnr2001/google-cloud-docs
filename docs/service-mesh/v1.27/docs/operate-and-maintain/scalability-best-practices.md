---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-best-practices/
title: Scaling best practices for Cloud Service Mesh on GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:47.653433+00:00
---

# Scaling best practices for Cloud Service Mesh on GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-best-practices/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scaling best practices for Cloud Service Mesh on GKE

This guide describes best practices for resolving scaling issues for managed [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview) architectures on Google Kubernetes Engine. The primary goal of these recommendations is to ensure optimal performance, reliability, and resource utilization for your microservices applications as they grow.

To understand the limitations on scalability, refer to [Cloud Service Mesh scalability limits](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits)

**Note:** Many of these techniques can be applied to other deployments of Cloud Service Mesh as well, such as in-cluster deployments on Google Distributed Cloud.

The scalability of Cloud Service Mesh on GKE depends on the efficient operation of its two main components, the data plane and the control plane. This document mainly focuses on scaling the data plane.

## Identifying control plane versus data plane scaling issues

In Cloud Service Mesh, scaling issues can occur in either the control plane or the data plane. Here's how you can identify which type of scaling issue you're facing:

### Symptoms of control plane scaling issues

**Slow service discovery:** New services or endpoints take a long time to be discovered and become available.

**Configuration delays:** Changes to traffic management rules or security policies take a long time to propagate.

**Increased latency in control plane operations:** Operations like creating, updating, or deleting Cloud Service Mesh resources become slow or unresponsive.

**Errors related to Traffic Director:** You might observe errors in Cloud Service Mesh logs or control plane metrics indicating issues with connectivity, resource exhaustion, or API throttling.

**Scope of impact:** Control plane issues typically affect the entire mesh, causing widespread performance degradation.

### Symptoms of data plane scaling issues

**Increased latency in service-to-service communication:** Requests to an in-mesh service experiences higher latency or timeouts, but there is not elevated CPU/memory usage in the service's containers.

**High CPU or memory usage in Envoy proxies:** High CPU or memory usage may indicate that the proxies are struggling to handle the traffic load.

**Localized impact:** Data plane issues typically affect specific services or workloads, depending on the traffic patterns and resource utilization of the Envoy proxies.

## Scaling the data plane

To scale the data plane, try the following techniques:

  * Configure horizontal pod autoscaling (HPA)
  * Optimize envoy proxy configuration
  * Monitor and fine tune



### Configure Horizontal Pod Autoscaling (HPA) for workloads

Use **Horizontal Pod Autoscaling (HPA)** to dynamically scale workloads with additional pods based on resource utilization. Consider the following when configuring HPA:

  * Use the `--horizontal-pod-autoscaler-sync-period` parameter to `[kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)` to adjust the polling rate of the HPA controller. The default polling rate is 15 seconds and you might consider setting this lower if you expect quicker traffic spikes. To learn more about when to use HPA with GKE, see [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).

  * The default scaling behavior can result in a large number of pods being deployed (or terminated) at once, which can cause a spike in resource usage. Consider using [scaling policies](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-policies) to limit the rate at which pods can be deployed.

  * Use [EXIT_ON_ZERO_ACTIVE_CONNECTIONS](https://istio.io/latest/docs/reference/commands/pilot-agent/#envvars) to avoid dropping connections during scaledown.




For more details on HPA, see [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) in the Kubernetes documentation.

### Optimize Envoy Proxy Configuration

To optimize Envoy proxy configuration, consider the following recommendations:

  * Resource limits
  * Scope service dependencies



#### Resource limits

You can define [resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for Envoy sidecars in your Pod specifications. This prevents resource contention and ensures consistent performance.

You can also configure default resource limits for all Envoy proxies in your mesh [using resource annotations](https://istio.io/latest/docs/reference/config/annotations/#SidecarProxyCPULimit).

The optimal resource limits for your Envoy proxies depend on factors, such as traffic volume, workload complexity, and GKE node resources. Continually monitor and fine tune your service mesh to ensure optimal performance.

**Important Consideration:**

  * **Quality of Service (QoS):** Setting both requests and limits ensures your Envoy proxies have a predictable quality of service.



#### Scope service dependencies

Consider trimming your mesh's dependency graph by [declaring all your dependencies through the Sidecar API](https://docs.cloud.google.com/service-mesh/v1.27/docs/security/egress-gateway-gke-tutorial#using_the_sidecar_resource_to_restrict_the_scope_of_sidecar_proxy_configuration). This limits the size and complexity of configuration sent to a given workload, which is critical for larger meshes.

As an example, the following is the traffic graph for the online boutique sample application.

![Online Boutique sample application traffic graph tree with many leaves](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/online-boutique-traffic-graph.png)

Many of these services are leafs in the graph, and as such don't need to have egress information for any of the other services in the mesh. You can apply a Sidecar resource limiting the scope of the sidecar configuration for these leaf services as shown in the following example.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: Sidecar
    metadata:
      name: leafservices
      namespace: default
    spec:
      workloadSelector:
        labels:
          app: cartservice
          app: shippingservice
          app: productcatalogservice
          app: paymentservice
          app: emailservice
          app: currencyservice
      egress:
      -   hosts:
        -   "~/*"
    

See [Online Boutique sample application](https://docs.cloud.google.com/service-mesh/v1.27/docs/onlineboutique-install-kpt) for details on how to deploy this sample application.

Another benefit to sidecar scoping is reducing unnecessary DNS queries. Scoping service dependencies ensure that an Envoy sidecar only makes DNS queries for services that it will actually communicate with instead of every cluster in the service mesh.

For any large-scale deployments facing issues with large config sizes in their sidecars, scoping service dependencies is _strongly_ recommended for mesh scalability.

To limit the configuration scope for all workloads within a single namespace, create one Sidecar resource in that namespace. This instructs all Envoy proxies within that namespace to only receive configuration for services in its own namespace.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: Sidecar
    metadata:
      name: sidecar
      namespace: my-app
    spec:
      egress:
      -   hosts:
        -   "my-app/*"
    

You can apply default behavior for every namespace in your mesh by applying a single Sidecar resource to the root namespace, typically istio-system.

The following Sidecar restricts the egress traffic of every sidecar in the mesh to services located within its own namespace.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: Sidecar
    metadata:
      name: sidear
      namespace: istio-system
    spec:
      egress:
      -   hosts:
        -   "./*"
    

Note that Cloud Service Mesh imposes a [limit](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits#Istio-Sidecar-Resources) on the total number of Sidecar resources that can be created within a single mesh. Due to this constraint, creating namespace-level Sidecar is the recommended practice.

### Monitor and fine-tune

After setting initial resource limits, it's crucial to monitor your Envoy proxies to ensure they are performing optimally. Use [GKE dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards) to monitor CPU and memory usage and adjust resource limits as needed.

To determine if an Envoy proxy requires increased resource limits, monitor its resource consumption under typical and peak traffic conditions. Here's what to look for:

  * **High CPU Usage:** If Envoy's CPU usage consistently approaches or exceeds its limit, it may be struggling to process requests, leading to increased latency or dropped requests. Consider increasing the CPU limit.

You may be inclined to scale using horizontal scaling in this case, but if the sidecar proxy consistently isn't able to process the requests as quickly as the application container, adjusting CPU limits may produce the best results.

  * **High Memory Usage:** If Envoy's memory usage approaches or exceeds its limit, it may start dropping connections or experience out-of-memory (OOM) errors. Increase the memory limit to prevent these issues.

  * **Error Logs:** Examine Envoy's logs for errors related to resource exhaustion, such as _upstream connect error_ or _disconnect or reset before headers_ or _too many open files_ errors. These errors may indicate that the proxy needs more resources. See [scaling troubleshooting docs](https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-scaling) for other errors related to scaling issues.

  * **Performance Metrics:** Monitor key performance metrics like request latency, error rates, and throughput. If you notice performance degradation correlated with high resource utilization, increasing limits might be necessary.




By actively setting and monitoring resource limits for your data plane proxies, you can ensure that your service mesh scales efficiently on GKE.

## Scaling the control plane

This section describes settings to adjust for scaling your control plane.

### Discovery selectors

Discovery selectors is a field in the MeshConfig that lets you specify the set of namespaces that control planes consider when computing configuration updates for sidecars.

By default, Cloud Service Mesh watches all namespaces in the cluster. This can be a bottleneck for large clusters that don't need to watch all resources.

Use `discoverySelectors` to reduce the computational load on the control plane by limiting the number of Kubernetes resources (such as services, pods, and endpoints) that are watched and processed.

When using the `TRAFFIC_DIRECTOR` control plane implementation, Cloud Service Mesh only creates Google Cloud resources, such as Backend Services and Network Endpoint Groups, for Kubernetes resources in namespaces specified in `discoverySelectors`.

For more information, see [Discovery selectors](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-discovery_selectors) in the Istio documentation.

**Note:** Cloud Service Mesh always watches the MeshConfig resource in the `istio-system` namespace; therefore, you must include the `istio-system` namespace in your `discoverySelectors`.

## Building in resilience

You can adjust the following settings to build resilience into your service mesh:

  * Outlier detection
  * Retries
  * Timeouts
  * Monitor and fine-tune



### Outlier detection

Outlier detection monitors hosts in an upstream service and removes them from the load balancing pool upon reaching some error threshold.

  * **Key Configuration:**
    * `outlierDetection`: Settings controlling eviction of unhealthy hosts from the load balancing pool.
  * **Benefits:** Maintains a healthy set of hosts in the load balancing pool.



For more information, see [Outlier Detection](https://istio.io/latest/docs/reference/config/networking/destination-rule/#OutlierDetection) in the Istio documentation.

### Retries

Mitigate transient errors by automatically retrying failed requests.

  * **Key Configuration:**
    * `attempts`: Number of retry attempts.
    * `perTryTimeout`: Timeout per retry attempt. Set this shorter than your overall timeout. It determines how long you'll wait for each individual retry attempt.
    * `retryBudget`: Maximum concurrent retries.
  * **Benefits:** Higher success rates for requests, reduced impact of intermittent failures.



**Factors to Consider:**

  * **Idempotency:** Ensure that the operation being retried is idempotent, which means that it can be repeated without unintended side effects.
  * **Max Retries:** Limit the number of retries (e.g., max 3 retries) to avoid infinite loops.
  * **Circuit Breaking:** Integrate retries with circuit breakers to prevent retries when a service is consistently failing.



For more information, see [Retries](https://istio.io/latest/docs/concepts/traffic-management/#retries) in the Istio documentation.

### Timeouts

Use timeouts to define maximum time allowed for request processing.

  * **Key Configuration:**
    * `timeout`: Request timeout for a specific service.
    * `idleTimeout`: Time a connection can remain idle before closure.
  * **Benefits:** Improved system responsiveness, prevention of resource leaks, hardening against malicious traffic.



**Factors to Consider:**

  * **Network Latency:** Account for the expected round-trip time (RTT) between services. Leave some buffer for unexpected delays.
  * **Service Dependency Graph:** For chained requests, ensure that the timeout of a calling service is shorter than the cumulative timeout of its dependencies to avoid cascading failures.
  * **Types of Operations:** Long-running tasks may need significantly longer timeouts than data retrievals.
  * **Error Handling:** Timeouts should trigger appropriate error handling logic (e.g., retry, fallback, circuit breaking).



For more information, see [Timeouts](https://istio.io/latest/docs/concepts/traffic-management/#timeouts) in the Istio documentation.

### Monitor and fine-tune

Consider starting with the default settings for timeouts, outlier detection and retries and then gradually adjusting them based on your specific service requirements and observed traffic patterns. For example, look at real-world data on how long your services typically take to respond. Then adjust timeouts to match the specific characteristics of each service or endpoint.

## Telemetry

Use telemetry to continually monitor your service mesh and adjust its configuration to optimize performance and reliability.

  * **Metrics:** Use comprehensive metrics, specifically, request volumes, latency, and error rates. Integrate with [Cloud Monitoring](https://docs.cloud.google.com/monitoring) for visualization and alerting.
  * **Distributed Tracing:** Enable distributed tracing integration with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) to gain deep insights into request flows across your services.
  * **Logging:** Configure [access logging](https://docs.cloud.google.com/service-mesh/v1.27/docs/observability/accessing-logs) to capture detailed information about requests and responses.



## Additional Reading

  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs).
  * For general site reliability engineering (SRE) guidance on scalability, see the [Handling Overload](https://sre.google/sre-book/handling-overload/), and [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) chapters in the Google SRE book.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
