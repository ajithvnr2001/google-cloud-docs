---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management/
title: Gateway traffic management \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:24.220716+00:00
---

# Gateway traffic management  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Gateway traffic management Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how Gateway traffic management works.

This page is intended for Developers, Operators, and Networking specialists who want to deploy and manage traffic using the Gateway API.

## Overview

Google Kubernetes Engine (GKE) networking is built upon [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). With Cloud Load Balancing, a single anycast IP address delivers global traffic management. [Google's traffic management](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb#how_https_load_balancing_works) provides global and regional load balancing, autoscaling, and capacity management to provide equalized, stable, and low latency traffic distribution. Using the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api), GKE users can utilize Google's global traffic management control in a declarative and Kubernetes-native manner.

To try traffic spillover between clusters, see [Deploying capacity-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#capacity-load-balancing). To try traffic-based autoscaling, see [Autoscaling based on load balancer traffic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#autoscale-traffic).

## Traffic management

Load balancing, autoscaling, and capacity management are the foundations of a traffic management system. They operate together to equalize and stabilize system load.

  * **Load balancing** distributes traffic across backend Pods according to location, health, and different load balancing algorithms.
  * **Autoscaling** scales workload replicas to create more capacity to absorb more traffic.
  * **Capacity management** monitors the utilization of Services so that traffic can overflow to backends with capacity rather than impacting application availability or performance.



These capabilities can be combined in different ways depending on your goals. For example:

  * If you want to take advantage of low-cost [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), you might want to optimize for evenly distributing traffic across Spot VMs at the cost of latency. Using load balancing and capacity management, GKE would overflow traffic between regions based on capacity so that Spot VMs are fully utilized wherever they are available.

  * If you want to optimize user latency at the cost of over-provisioning, you could deploy GKE clusters in many regions and increase capacity dynamically wherever load increases. Using load balancing and autoscaling GKE would autoscale the number of Pods when traffic spikes so that traffic does not have to overflow over to other regions. Regions would grow in capacity so that they are able to fully handle load as close as possible to users.




The following diagram shows load balancing, autoscaling, and capacity management operating together:

![Load balancing, autoscaling and capacity management diagram](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-overview.svg)

In the diagram, the workload in the `gke-us` cluster has failed. Load balancing and health checking drains active connections and redirects traffic to the next closest cluster. The workload in `gke-asia` receives more traffic than it has capacity for, so it sheds load to `gke-eu`. The `gke-eu` receives more load than typical because of events in `gke-us` and `gke-asia` and so `gke-eu` autoscales to increase its traffic capacity.

To learn more about how Cloud Load Balancing handles traffic management, see [global capacity management](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb).

### Traffic management capabilities and Service Extensions

Gateway, HTTPRoute, Service, and Policy resources provide the controls to manage traffic in GKE. The [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) is the control plane that monitors these resources.

GKE Gateway Service Extensions customize and extend traffic management in GKE. Extensions inject custom logic for advanced traffic control.

The following traffic management capabilities are available when deploying Services in GKE:

  * **Service capacity** : specifying the amount of traffic capacity that a Service can receive before Pods autoscale or traffic overflows to other available clusters
  * **Traffic-based autoscaling** : autoscaling Pods within a Service based on HTTP requests received per second
  * **Multi-cluster load balancing** : load balancing to Services hosted across multiple GKE clusters or multiple regions
  * **Traffic splitting** : explicit, weight-based traffic distribution across backends
  * **Session affinity (GCPTrafficDistributionPolicy)** : pinning sessions by using cookies, headers, or client IP addresses to optimize stateful application performance
  * **Cross-Origin Resource Sharing (CORS)** : allowing and helping to secure cross-origin requests
  * **Edge caching** : caching content with Cloud CDN to improve end-user latency and reduce origin load for GKE-hosted applications
  * **Custom traffic management with Service Extensions** : extending traffic management by injecting custom logic for advanced control, such as: 
    * Modifying headers and payloads for HTTP requests and responses
    * Implementing custom routing logic to control traffic flow
    * Integrating with external services for functions like authorization

**Note:** Support for Service Extensions is in [Preview](https://cloud.google.com/products#product-launch-stages) stage.

### Traffic management support

The available traffic management capabilities depend on the GatewayClass that you deploy. For a complete list of feature support, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities). The following table summarizes GatewayClass support for traffic management:

GatewayClass | Service capacity | Traffic autoscaling | Multi-cluster load balancing | Traffic splitting1 | Session affinity (GCPTrafficDistributionPolicy) | CORS | Edge caching  
---|---|---|---|---|---|---|---  
`gke-l7-global-external-managed` |  |  |  |  |  |  |   
`gke-l7-regional-external-managed` |  |  |  |  |  |  |   
`gke-l7-rilb` |  |  |  |  |  |  |   
`gke-l7-gxlb` |  |  |  |  |  |  |   
`gke-l7-global-external-managed-mc` |  |  |  |  |  |  |   
`gke-l7-regional-external-managed-mc` |  |  |  |  |  |  |   
`gke-l7-cross-regional-internal-managed-mc` |  |  |  |  |  |  |   
`gke-l7-rilb-mc` |  |  |  |  |  |  |   
`gke-l7-gxlb-mc` |  |  |  |  |  |  |   
  
1 Traffic splitting is supported with single-cluster Gateways in GA. 

### Traffic management with custom metrics-based load balancing

Google Cloud Application Load Balancers distribute traffic based on custom metrics. These metrics might include GPU utilization load or other application-specific utilization signals. Custom metrics provide a more accurate view of workload performance. Your application reports these metrics by using the Open Request Cost Aggregation (ORCA) standard. For more information, see [Custom metrics for Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics).

In GKE, you can integrate this advanced traffic management capability through the GKE Gateway API. The API is useful for workloads with variable resource usage, such as generative AI inference. You can set up custom traffic behavior by configuring the following policies:

  * **GCPBackendPolicy** : enables precise control over how backend services of a load balancer distribute traffic to their backends for backend selection. This policy includes specific fields that let you configure various load balancing modes, like the use of custom metrics. To configure backend selection with GCPBackendPolicy, see [Configure backend selection using GCPBackendPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure-backend-selection).

  * **GCPTrafficDistributionPolicy** : configures session affinity and load balancing algorithms for endpoint selection within a backend for endpoint-level routing. You can configure persistent session stickiness (`STRONG_COOKIE_AFFINITY`, `HTTP_COOKIE`, `GENERATED_COOKIE`, `HEADER_FIELD`, `CLIENT_IP`) and stable load balancing algorithms like `RING_HASH`. When you select `WEIGHTED_ROUND_ROBIN`, the load balancer uses weights derived from reported metrics, including custom metrics, to distribute traffic to individual instances or endpoints. To configure endpoint-level routing and session affinity, see [Configure endpoint-level routing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure-endpoint-routing) and [Configure session affinity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#session_affinity).




#### Location-based policies

You can apply these location-based policies to specific Google Cloud zones or regions by using a location specifier. Location specifiers useful for canary deployments, phased rollouts, or testing policy changes in isolated regions. For more information, see [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).

#### Monitor custom metrics for GKE backends

The global external Application Load Balancers and internal Application Load Balancers provide logging and monitoring capabilities that allow you to observe custom metrics reported by your GKE backends for granular traffic insights. For more information, see [global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring).

You can use the GKE metric labels to query custom metrics per GKE service, cluster, and namespace.

To view the custom metrics reported by your GKE backends, go to **Cloud Monitoring** and view the custom metrics under the `network.googleapis.com/loadbalancer/backend/` monitored resource. You can use GKE-specific labels to query and filter these metrics.

The metrics available include:

  * `/error_rate`: errors served by each backend group per second.
  * `/lb_custom_metric`: current utilization by each backend group, based on your defined custom metrics.
  * `/fullness`: current fullness (load or capacity) by each backend group, which load balancers use for routing decisions.
  * `/rate`: requests received by each backend group per second.



GKE-specific labels that enhance monitoring for these metrics include `gke_service_name`, `gke_namespace`, and `gke_cluster`. You can use these labels to explore metric data per GKE service, namespace, and cluster. Note that these GKE labels are only populated if the `backend_type` is `ZONAL_NETWORK_ENDPOINT_GROUP`.

The following table lists GKE-specific labels:

Label | Type | Description  
---|---|---  
`gke_service_name` | Metric Label or System Label | GKE resource's service name, if one exists. This field is only populated if `backend_type` is `ZONAL_NETWORK_ENDPOINT_GROUP`. For other backend types, this label has null entry.  
`gke_namespace` | Metric Label or System Label | GKE resource's namespace, if one exists. This field is only populated if `backend_type` is `ZONAL_NETWORK_ENDPOINT_GROUP`. For other backend types, this label has null entry.  
`gke_cluster` | Metric Label or System Label | GKE cluster name of the resource, if one exists. This field is only be populated if `backend_type` is `ZONAL_NETWORK_ENDPOINT_GROUP`. For other backend types, this label has null entry.  
  
global external Application Load Balancers log entries contain information useful for monitoring and debugging your HTTP(S) traffic.

### Global, regional, and zonal load balancing

Service capacity, location, and health all determine how much traffic the load balancer sends to a given backend. Load balancing decisions are made at the following levels, starting with global for global load balancers and regional for regional load balancers:

  * **Global** : traffic is sent to the closest Google Cloud region to the client that has healthy backends with capacity. As long as the region has capacity, it receives all of its closest traffic. If a region does not have capacity, excess traffic overflows to the next closest region with capacity. To learn more, see global load balancing.
  * **Regional** : traffic is sent by the load balancer to a specific region. The traffic is load balanced across zones in proportion to the zone's available serving capacity. To learn more, see regional load balancing.
  * **Zonal** : after traffic is determined for a specific zone, the load balancer distributes traffic evenly across backends within that zone. Existing TCP connections and session persistence settings are preserved, so that future requests go to the same backends, as long as the backend Pod is healthy. To learn more, see zonal load balancing.



#### Global load balancing and traffic overflow

To try the following concepts in your own cluster, see [Capacity-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#capacity-load-balancing).

Under normal conditions, traffic is sent to the closest backend to the client. Traffic terminates at the closest Google point of presence (PoP) to the client and then traverses the Google backbone until it reaches the closest backend, as determined by network latency. When the backends in a region don't have remaining capacity, traffic overflows to the next closest cluster with healthy backends that have capacity. If more than 50% of backend Pods within a zone are unhealthy, then traffic gradually fails over to other zones or regions, independent of the configured capacity.

Traffic overflow only occurs under the following conditions:

  * You are using a [multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).
  * You have the same Service deployed across multiple clusters, served by the multi-cluster Gateway.
  * You have Service capacities configured such that traffic exceeds service capacities in one cluster, but not others.



The following diagram demonstrates how global load balancing works with traffic overflow:

![Global load balancing with traffic overflow](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-overflow-1.svg)

In the diagram:

  * A multi-cluster Gateway provides global internet load balancing for the `store` Service. The service is deployed across two GKE clusters, one in `us-west1` and another in `europe-west1`. Each cluster is running 2 replicas.
  * Each Service is configured with `max-rate-per-endpoint="10"`, which means that each Service has a total capacity 2 replicas * 10 RPS = 20 RPS in each cluster.
  * Google PoPs in North America receive 6 RPS. All traffic is sent to the nearest healthy backend with capacity, the GKE cluster in `us-west1`.
  * European PoPs receive 30 cumulative RPS. The closest backends are in `europe-west1`, but they only have 20 RPS of capacity. Because the backends in `us-west1` have excess capacity, 10 RPS overflows to `us-west1` so that it receives 16 RPS in total and distributes 8 RPS to each pod.

**Note:** If you are using single-cluster Gateways, a Service of type `LoadBalancer`, or Ingress resources, then this global load balancing example does not apply since these resources only load balance to a single cluster within a single region. Multi-cluster Gateways are recommended if you have global load balancing requirements.

#### Preventing traffic overflow

Traffic overflow helps prevent exceeding application capacity that can impact performance or availability.

However, you might not want to overflow traffic. Latency-sensitive applications, for example, might not benefit from traffic overflow to a much more distant backend.

You can use any of following methods to prevent traffic overflow:

  * Use only single-cluster Gateways which can host Services in only a single cluster.

  * Even if using multi-cluster Gateways, replicas of an application deployed across multiple clusters can be deployed as separate Services. From the perspective of the Gateway, this enables multi-cluster load balancing, but does not aggregate all endpoints of a Service between clusters.

  * Set Service capacities at a high enough level that traffic capacity is never realistically exceeded unless absolutely necessary.




#### Load balancing within a region

Within a region, traffic is distributed across zones according to the available capacities of the backends. This is not using overflow, but rather load balancing in direct proportion to the Service capacities in each zone. Any individual flow or session is always sent to a single, consistent backend Pod and is not split.

The following diagram shows how traffic is distributed within a region:

![Traffic distributed within a region](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-overflow-2.svg)

In the diagram:

  * A Service is deployed in a regional GKE cluster. The Service has 4 Pods which are deployed unevenly across zones. 3 Pods are in zone A, 1 Pod is in zone B, and 0 Pods are in zone C.
  * The Service is configured with `maxRatePerEndpoint=10`. Zone A has 30 RPS of total capacity, zone B has 10 RPS of total capacity, and zone C has 0 RPS of total capacity, because it has no Pods.
  * The Gateway receives a total of 16 RPS of traffic from different clients. This traffic is distributed across zones in proportion to the remaining capacity in each zone.
  * Traffic flow from any individual source or client is consistently load balanced to a single backend Pod according to the session persistence settings. The distribution of traffic splits across different source traffic flows so that any individual flows are never split. As a result, a minimum amount of source or client diversity is required to granularly distribute traffic across backends.



For example, if the incoming traffic spikes from 16 RPS to 60 RPS, either of the following scenarios would occur:

  * If using single-cluster Gateways, then there are no other clusters or regions for this traffic to overflow to. Traffic continues to be distributed according to the relative zonal capacities, even if incoming traffic exceeds the total capacity. As a result, zone A receives 45 RPS and zone B receives 15 RPS.
  * If using multi-cluster Gateways with Services distributed across multiple clusters, then traffic can overflow to other clusters and other regions as described in Global load balancing and traffic overflow. Zone A receives 30 RPS, zone B receives 10 RPS, and 20 RPS overflows to another cluster.

**Note:** Cloud Load Balancing does not automatically drop traffic when backends are over-capacity. Traffic overflows to any available backends that have capacity. If all backends are over-capacity, then the overflow traffic is distributed across all backends in proportion to their total capacities. This exceeds the total Service capacity.

#### Load balancing within a zone

Once traffic has been sent to a zone, it is distributed evenly across all the backends within that zone. HTTP sessions are persistent depending on the session affinity setting. Unless the backend becomes unavailable, existing TCP connections never move to a different backend. This means that long-lived connections continue going to the same backend Pod even if new connections overflow because of limited capacity. The load balancer prioritizes maintaining existing connections over new ones.

Although standard load balancing distributes traffic evenly across backends, the `RING_HASH` algorithm provides consistent mapping of requests to specific Pods. `RING_HASH` minimizes request reshuffling when Pods are added or removed, making it a more stable option for stateful workloads sensitive to cache misses. You can optionally configure `minimumHashRingSize` to tune the hash ring size; a larger ring size can help ensure a more even spread of requests across backends, particularly in larger clusters.

## Service capacity

With service capacity, you can define a Requests per Second (RPS) value per Pod in a Service. This value represents the maximum RPS per-Pod on average that a Service can receive. This value is configurable on Services and is used to determine traffic-based autoscaling and capacity-based load balancing.

### Requirements

Service capacity has the following requirements and limitations:

  * Only supported with the GatewayClass resources and Ingress types defined in Traffic management support.
  * Only impacts load balancing if you are using traffic-based autoscaling or multi-cluster Gateways. If you are not using these capabilities, Service capacity has no effect on network traffic.



### Configure Service capacity

### Single-cluster Gateways

Ensure your GKE cluster is running the version 1.31.1-gke.2008000 or later. Earlier versions can use the `networking.gke.io/max-rate-per-endpoint` annotation as described in the _Multi-cluster Gateways_ tab.

To use single-cluster Gateways to configure Service capacity, create a Service and an associated GCPBackendPolicy. Use the following manifest to create a Service:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: store
    spec:
      ports:
      - port: 8080
        targetPort: 8080
        name: http
      selector:
        app: store
      type: ClusterIP
    

Configure the GCPBackendPolicy object using the `maxRatePerEndpoint` field with a maximum RPS. Use the following manifest to configure the GCPBackendPolicy object:
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: store
    spec:
      default:
        maxRatePerEndpoint: RATE_PER_SECOND
      targetRef:
        group: ""
        kind: Service
        name: store
    

### Multi-cluster Gateways

To use multi-cluster Gateways to configure Service capacity, create a Service using the `networking.gke.io/max-rate-per-endpoint` annotation. Use the following manifest to create a Service with a maximum RPS:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: store
      annotations:
        networking.gke.io/max-rate-per-endpoint: "RATE_PER_SECOND"
    spec:
      ports:
      - port: 8080
        targetPort: 8080
        name: http
      selector:
        app: store
      type: ClusterIP
    

Replace `RATE_PER_SECOND` with the maximum HTTP/HTTPS requests per second that a single Pod in this Service should receive.

The `maxRatePerEndpoint` value creates a dynamic capacity for a Service based on the number of Pods in the Service. The total Service capacity value is calculated by multiplying the `maxRatePerEndpoint` value with the number of replicas, as described in the following formula:
    
    
    Total Service capacity = maxRatePerEndpoint * number of replicas
    

If an autoscaler scales up the number of Pods within a Service, then the Service's total capacity is computed accordingly. If a Service is scaled down to zero Pods, then it has zero capacity and does not receive any traffic from the load balancer.

**Note:** Service capacity configuration using the `maxRatePerEndpoint` field in the GCPBackendPolicy only applies to the traffic ingressing through a supported Gateway. It does not influence the capacity-based load balancing for the type `ClusterIP` within the cluster, or for the Services of type `LoadBalancer`.

### Service capacity and standalone NEGs

Service capacity can also be configured when using [standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg), however it does not use the `maxRatePerEndpoint` setting. When using standalone NEGs, the `maxRatePerEndpoint` is configured manually when adding the NEG to a Backend Service resource. Using the [`gcloud compute backend-services add-backend`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) command, the `--max-rate-per-endpoint` flag can configure capacity for each NEG individually.

This can be useful for any of the following workflows:

  * When deploying internal and external load balancers manually using standalone NEGs
  * When deploying [Cloud Service Mesh on GKE using standalone NEGs](https://docs.cloud.google.com/service-mesh/docs/set-up-gke-pods-auto#deploying_a_kubernetes_service_for_testing)



There is no functional difference when configuring service capacity with standalone NEGs. Both traffic autoscaling and traffic spillover are supported.

### Determine your Service's capacity

Determining the value for `maxRatePerEndpoint` requires an understanding of your applications performance characteristics and your load balancing goals. The following strategies can help you define your application performance characteristics:

  * Observe your application in both test and production environments when configured without Service capacity.
  * Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to create a correlation between traffic requests and your performance service level objectives (SLOs).

  * Use [load balancer metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics), such as `https` or `request_count` to map RPS levels.

  * Define what your performance SLOs are for your application. They might be one or more of the following, depending on what you consider "bad" or "unstable" performance. All of the following can be gathered from Cloud Monitoring load balancer metrics:

    * Response error codes
    * Response or total latency
    * Backend unhealthiness or downtime
  * Observe your application under traffic load in both test and production environments. In test environments, stress your application under increasing request load so you can see how the different performance metrics are impacted as traffic increases. In production environments, observe realistic traffic patterns levels.




### Default Service capacity

All Services attached to GKE resources have a default Service capacity configured even if it isn't explicitly configured. To learn more, see Default service capacity.

The following table describes the default capacities:

Load balancing resource type | Default `maxRatePerEndpoint`  
---|---  
Ingress (internal and external) | 1 RPS  
Gateway (all GatewayClasses) | 100,000,000 RPS  
MultiClusterIngress | 100,000,000 RPS  
  
## Traffic-based autoscaling

Traffic-based autoscaling is a capability of GKE that natively integrates traffic signals from load balancers to autoscale Pods. Traffic-based autoscaling is only supported for single-cluster Gateways.

To use traffic-based autoscaling, see [Autoscaling based on load balancer traffic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#autoscale-traffic).

Traffic-based autoscaling provides the following benefits:

  * Applications which are not strictly CPU or memory bound might have capacity limits which are not reflected in their CPU or memory usage.
  * Traffic, or requests per second (RPS) is an easier metric to understand in some cases because it is more aligned with app usage and business metrics such as page views or daily active users (DAUs).
  * Traffic is a leading indicator that represents instantaneous demand compared with CPU or memory which are lagging indicators.
  * The combination of CPU, memory, and traffic autoscaling metrics provides a holistic way of autoscaling applications that uses multiple dimensions to ensure that capacity is appropriately provisioned.



The following diagram demonstrates how traffic-based autoscaling works:

![Traffic-based autoscaling](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-autoscale-1.svg)

In the diagram:

  * The Service owner configures Service capacity and a target utilization for the Deployment.
  * The Gateway receives traffic from clients going to the `store` Service. The Gateway sends utilization telemetry to the GKE Pod Autoscaler. Utilization is equal to the actual traffic received by an individual Pod divided by the Pod's configured capacity.
  * The GKE Pod Autoscaler scales Pods up or down according to the configured target utilization.



### Autoscaling behavior

The following diagram shows how traffic-based autoscaling works on an application receiving 10 RPS through the load balancer:

![Traffic-based autoscaling with 10 RPS](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-autoscale-2.svg)

In the diagram, the service owner has configured the capacity of the store Service to 10 RPS, which means that each Pod can receive a maximum of 10 RPS. The HorizontalPodAutoscaler is configured with `averageValue` is set to `70`, which means that the target utilization is 70% of 10 RPS per Pod.

The autoscaler attempts to scale replicas to achieve the following equation:
    
    
    replicas = ceiling[ current traffic / ( averageValue * maxRatePerEndpoint) ]
    

In the diagram, this equation computes to:
    
    
    ceiling[ 10 rps / (0.7 * 10 rps) ] = ceiling[ 1.4 ] = 2 replicas
    

10 RPS of traffic results in 2 replicas. Each replica receives 5 RPS, which is under the target utilization of 7 RPS.

**Note:** Changes in traffic levels or traffic spikes can cause the autoscaler to approximate the target replicas equation. In steady-state conditions, the amount of replicas approach the target but it might not always be exact, especially with fluctuating traffic.

## Traffic splitting

Traffic splitting uses an explicit ratio, called a **weight** , that defines the proportion of HTTP requests that are sent to a Service. HTTPRoute resources let you configure weights on a list of Services. The relative weights between Services define the split of traffic between them. This is useful for splitting traffic during rollouts, canarying changes, or for emergencies.

**Warning:** Weighted traffic splitting takes precedence over session affinity. If you use both features simultaneously, client requests might be routed to different backend Pods based on the weights, even if session affinity is enabled.

The following diagram describes an example traffic splitting configuration:

![Traffic splitting configuration](https://docs.cloud.google.com/static/kubernetes-engine/images/traffic-split.svg)

In the diagram:

  * The Service owner configures two services for a single route, with a rule splitting traffic 90% to `store-v1` and 10% to `store-v2`.
  * The Gateway receives traffic from clients going to the URL of the store application and traffic is split according to the configured rule. 90% of traffic routes to `store-v1` and 10% routes to `store-v2`.



Traffic splitting is supported between Services in the same cluster and also between Services in different clusters. The two types of traffic splitting supported are as follows:

  * **Traffic splitting between Services** : this approach is used for splitting traffic for application version rollouts. Using the traffic splitting example, you would have two separate Deployments, `store-v1` and `store-v2`, which each have their own Service, `store-v1` and `store-v2`. Weights are configured between the two Services to gradually shift traffic until `store-v2` is fully rolled out.

**Note:** The `gke-l7-gxlb` GatewayClass does not support traffic splitting.
  * **Traffic splitting between ServiceImports** : this approach is used for shifting traffic to or from specific clusters for maintenance, migration, or emergencies. ServiceImports represent multi-cluster Services and enable traffic splitting between different Services on different clusters. The exercise [Blue-green, multi-cluster routing with Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#blue-green) demonstrates splitting traffic across clusters.

**Note:** The `gke-l7-gxlb-mc` GatewayClass does not support traffic splitting.



### Weight versus capacity

Weights and capacities both control how much traffic is sent to different Services. While they have similar effects, they operate differently and have different use cases. They can and should be used together, though for different purposes.

#### Weight

Weight is an **explicit** control of traffic. It defines the exact proportions of traffic, independent of incoming traffic and backend utilization. In the traffic splitting example, if `store-v2` was over-capacity, or if all of its replicas failed, 10% of the traffic would still be allocated to `store-v2`, potentially causing traffic to be dropped. That is because weight does not change the proportion of traffic based on utilization or health.

Weight is best suited for the following use cases:

  * Shifting traffic between different versions of a service for rollouts.
  * Manually onboarding services using explicit traffic splits.
  * Shifting traffic away from a set of backends for emergency or maintenance purposes.



#### Capacity

Capacity is an **implicit** control of traffic. It defines the proportions of traffic indirectly as they depend on the amount of incoming traffic, backend utilization, and the source location of traffic. Capacity is an inherent property of a Service and is typically updated much less frequently.

Capacity is best suited for the following use cases:

  * Preventing backend over-utilization during traffic spikes.
  * Controlling the rate of autoscaling with respect to traffic.



Configuring Service capacity to overflow traffic may not always be a behavior that you want. Consider the global load balancing example. Service capacity protects backends from over-utilization by overflowing traffic, but this might result in extra latency for the requests that have overflowed, since those requests are traveling to a more remote region.

If your application is not very sensitive to overutilization then you might want to configure a very high Service capacity so that traffic is unlikely to ever overflow to another region. If your application's availability or latency is sensitive to overutilization, then overflowing traffic to other clusters or regions may be better than absorbing excess traffic on over-utilized backends. To learn more about how to configure Service capacity for your application, see Determine your Service's capacity.

## Session affinity

Session affinity (also known as "sticky sessions") ensures that requests from a specific client are consistently routed to the same backend Pod. This is a performance optimization for stateful applications that benefit from local caching. Examples include ecommerce shopping carts or gaming sessions, where maintaining user session data on a specific Pod is essential.

GKE Gateway supports all session affinity types available on Google Cloud Application Load Balancer instances by using the GCPTrafficDistributionPolicy resource: `STRONG_COOKIE_AFFINITY` (stateful session persistence), `HTTP_COOKIE`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `CLIENT_IP`.

To configure session affinity we recommend using GCPTrafficDistributionPolicy, which is the default method. However, you can use GCPBackendPolicy in existing configurations for the `CLIENT_IP` and `GENERATED_COOKIE` session affinity types. If both policies target the same Service, GCPTrafficDistributionPolicy takes precedence. You can also configure stable load balancing algorithms, such as `RING_HASH`, using GCPTrafficDistributionPolicy.

**Note:** Weighted traffic splitting takes precedence over session affinity. If an incoming request matches a route rule with traffic weights, the load balancer picks the backend Service first, which might override the session affinity stickiness for that request.

## What's next

  * Learn about [deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Read an overview of [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).
  * Learn about the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn how to [configure Gateway resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).
  * Learn about [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
