---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/advanced-load-balancing-overview/
title: Advanced load balancing overview \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:44.261943+00:00
---

# Advanced load balancing overview  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/advanced-load-balancing-overview/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advanced load balancing overview

_Advanced load balancing_ consists of features that let you fine-tune global load balancing and traffic distribution to best meet your availability, performance, and cost-efficiency goals. This document is intended for users who have at least an intermediate understanding of Cloud Service Mesh and load balancing concepts.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

To implement advanced load balancing, you create a _service load balancing policy_ (`serviceLbPolicies` resource), which contains values that influence the selection of a backend. You then attach the service load balancing policy to a backend service. The service load balancing policy specifies the algorithm used to determine how traffic is balanced to the backends.

You can choose from the following algorithm options for advanced load balancing:

  * Waterfall by region (default algorithm).
  * Spray to region.
  * Spray to world.
  * Waterfall by zone.



The following additional options are available:

  * Designate preferred backends. Cloud Service Mesh sends traffic to those MIGs or NEGs before it sends traffic to other backends.
  * Set up automatic capacity draining.
  * Customize failover behavior.



Before you configure any of the advanced load balancing options, we recommend that you review documentation for the [backend service resource](https://docs.cloud.google.com/load-balancing/docs/backend-service).

## How Cloud Service Mesh routes and load balances traffic

The following diagram shows how Cloud Service Mesh decides to route traffic.

[ ![How Cloud Service Mesh makes load balancing decisions](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/advanced-lb-decisions.svg)](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/advanced-lb-decisions.svg) How Cloud Service Mesh makes load balancing decisions (click to enlarge)

First, Cloud Service Mesh chooses a backend services, based on request characteristics and based on routing rules in the `Route` resource or URL map, depending on which API your deployment uses.

Second, Cloud Service Mesh chooses a backend MIG or NEG that is associated with the backend service, based on client location, the location, health, and capacity of the MIG or NEG, and information in the service load balancing policy associated with the backend service.

Lastly, Cloud Service Mesh chooses an instance or endpoint within the MIG or NEG. This choice is based on information in the locality load balancing policy in the backend services.

## Supported and unsupported backends

The following backend types are supported for advanced load balancing:

  * Unmanaged instance groups
  * Managed instance groups (MIGs)
  * Zonal network endpoint groups (GCE_VM_IP_PORT NEGs)
  * Hybrid connectivity network endpoint groups (NON_GCP_PRIVATE_IP_PORT NEG)



The following backend types are not supported for advanced load balancing:

  * Regional managed instance groups
  * Internet network endpoint groups (INTERNET_FQDN_PORT NEGs)



## Use cases

The following sections describe how each algorithm works and which to choose for your particular business needs.

### Balance traffic across backends in a region

The default load balancing algorithm, waterfall by region, distributes traffic evenly across all MIGs or NEGs in zones in a region. We recommend that you use the default algorithm unless you have special requirements.

With waterfall by region, backends receive traffic in proportion to their capacity, which provides backend overload protection. Traffic is sent across zone boundaries when necessary to keep the backends evenly loaded within the region. Even if the zone local to the client has remaining capacity, there is cross-zone traffic. Each client's requests can be spread across multiple zonal MIGs or NEGs in the region, which helps to keep the load on the MIGs or NEGs uniform when the traffic load from the clients is not uniform.

### Increase resiliency by spreading traffic from a client across zones

The default waterfall by region algorithm tries to balance capacity usage across multiple zonal MIGs or NEGs. However, under that algorithm requests originating from a single client are not consistently sent to all zones, and requests from a single client are typically routed to MIGs or NEGs in a single zone.

Use the spray to region algorithm when you want clients to spread their requests to all MIGs or NEGs in a region, which reduces the risk of overloading MIGs or NEGs in a single zone when there is a rapid, localized increase in traffic volume.

With the spray to region algorithm, if you have two zones, A and B, and there is a traffic spike at zone B, the traffic is be split among the two zones. With the default algorithm, a spike in zone B could trigger an overload in zone before Cloud Service Mesh is able to respond to the change.

Note that when you use the spray to region algorithm, traffic for each client is always spread out among the backend zones in a region. This results in consistently higher cross zone traffic even when there is remaining capacity in the local zone, and can result in a larger affected area for the traffic from Cloud Service Mesh, if two Cloud Service Mesh clients are sending traffic to the same zones.

### Spread traffic from your client across all backends in multiple regions

As discussed in the previous sections, the spray to region algorithm spreads traffic from each client to all zones in a region. For services that have MIGs or NEGs in multiple regions, Cloud Service Mesh still optimizes overall latency by sending traffic to the closest region.

If you prefer a larger spread radius, use the spray to world algorithm. With this algorithm, clients spread their requests to all MIGs or NEGs in the world across multiple regions.

It's important to note that with this algorithm, all traffic is spread to all backends globally. A defective query might damage all backends in your deployments. The algorithm also results in more cross-region traffic, which might increase request latency and create additional costs.

### Minimize cross-zonal traffic

You can optimize overall latency and reduce cross-zone traffic by using the waterfall by zone setting. When multiple MIGs or NEGs are configured in a zone, client traffic is routed to the closest MIG or NEG in the zone, up to its capacity, before sending traffic to the next MIG or NEG in the zone until all MIG or NEG capacity in the zone is used. Only then is traffic spilled to the next-closest zone.

With this algorithm, you can minimize unnecessary cross-zone traffic. Overall latency might be slightly improved because the closest local backends are preferred. However, this might also create uneven traffic across the MIGs or NEGs within a region.

## Comparison of the load balancing algorithms

The following table provides a detailed comparison of the four Cloud Service Mesh load balancing algorithms.

**Behavior** | **Waterfall by region** | **Spray to region** | **Spray to world** | **Waterfall by zone**  
---|---|---|---|---  
Uniform capacity usage within a region in stable state | Yes | Yes | Yes | No  
Uniform capacity usage across multiple regions in stable state | No | No | Yes | No  
Uniform traffic split within a region in stable state | No | Yes | Yes | No  
Cross-zone traffic | Yes. This algorithm will distribute traffic evenly across zones in a region while optimizing network latency. Traffic may be sent across zones if needed. | Yes | Yes | Yes, traffic will fill up the nearest zone to its capacity. Then it will go to the next zone.   
Sensitivity to local zone traffic spikes | Average; depending on how much traffic is already shifted to balance across zones. | Lower; as single zone spikes will be spread across all zones in the region. | Lower; as single zone spikes will be spread across all regions. | Higher; as single zone spikes are more likely to be served entirely by a single zone until Cloud Service Mesh is able to react.  
  
## Additional advanced load balancing options

The following sections discuss options for modifying Cloud Service Mesh load balancing.

### Preferred backends

You can configure load balancing so that a group of backends of a backend service is designated as preferred. These backends are completely used before subsequent requests are routing to the remaining backends. Cloud Service Mesh distributes client traffic to the preferred backends first, minimizing request latencies for your clients.

Any traffic exceeding the configured capacity of the preferred backends is routed to non-preferred backends. The load balancing algorithm distributes traffic among the non-preferred backends.

One use case is overflow to Google Cloud, where you specify on-premises compute resources, represented by a hybrid connectivity NEG, to be fully used before requests are routed to autoscaled Google Cloud backend MIGs or NEGs. This configuration can minimize Google Cloud compute consumption and still have the resiliency to gradually spill or failover to Google Cloud when necessary.

### Automatic capacity draining

When a backend is unhealthy, it is usually desirable to exclude it as quickly as possible from load balancing decisions. Excluding the backend prevents requests from being sent to the unhealthy backend. In addition traffic is balanced among healthy backends to prevent backend overloading and optimize overall latency.

This option is similar to setting the [capacityscalar](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler) to zero. It asks Cloud Service Mesh to scale down backend capacity to zero automatically when a backend has less than 25% of its individual instances or endpoints passing health checks. With this option, unhealthy backends are removed from global load balancing.

When the auto drained backends are healthy again, they are undrained if at least 35% of the endpoints or instances are healthy for 60 seconds. Cloud Service Mesh does not drain more than 50% of the endpoints in a backend service, regardless of the backend health status.

One use case is that you can use auto capacity draining with preferred backends. If a backend MIG or NEG is preferred and many of the endpoints in it are unhealthy, this setting protects the remaining endpoints in the MIG or NEG by shifting traffic away from the MIG or NEG.

### Customize failover behavior

Cloud Service Mesh typically sends traffic to backends by taking several factors into account. In a steady state, Cloud Service Mesh sends traffic to backends that are selected based on the algorithms discussed previously. The selected backends are considered optimal in terms of latency and capacity utilization. They are called _primary_ backends.

Cloud Service Mesh also keeps track of backends to use when the primary backends are unhealthy and unable to receive traffic. These backends are called _failover_ backends. They are usually nearby backends that have some capacity remaining.

When a backend is unhealthy, Cloud Service Mesh tries to avoid sending traffic to it and instead shifts traffic to healthy backends.

The `serviceLbPolicy` resource includes a field, `failoverHealthThreshold`, whose value can be customized to control failover behavior. The threshold value that you set determines when traffic is shifted from primary backends to failover backends.

When some endpoints in the primary backend are unhealthy, Cloud Service Mesh does not necessarily shift traffic immediately. Instead, Cloud Service Mesh might shift traffic to healthy endpoints in the primary backend, to try to stabilize traffic.

If too many endpoints in the backend are unhealthy, the remaining endpoints are not able to handle additional traffic. In this case, the failure threshold is used to decide whether or not failover is triggered. Cloud Service Mesh tolerates unhealthiness up to the threshold, then shifts a portion of traffic away from the primary backends to the failover backends.

The failover health threshold is a percentage value. The value that you set determines when Cloud Service Mesh directs traffic to the failover backends. You can set the value to an integer between 1 and 99. The default value for Cloud Service Mesh is 70 with Envoy and 50 for proxyless gRPC. A larger value starts traffic failover sooner than a smaller value.

## Troubleshooting

Traffic distribution patterns can change based on how you set up the new `serviceLbPolicy` with the backend service.

To debug traffic issues, use the existing monitoring systems to examine how traffic flows to your backends. Additional Cloud Service Mesh and network metrics can help you understand how load balancing decisions are made. This section offers general troubleshooting and mitigation suggestions.

Overall, Cloud Service Mesh tries to assign traffic to keep backends running under their configured capacity. Keep in mind that this is not guaranteed. You can review [documentation for the backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity) for more details.

Then traffic is assigned based on the algorithm you use. For example, with the algorithm of WATERFALL_BY_ZONE, Cloud Service Mesh tries to keep traffic to the nearest zone. If you check the network metrics, you see Cloud Service Mesh prefers a backend with the smallest RTT latency when sending requests to optimize the overall RTT latency.

The following sections describe issues that you might see with the service load balancing policy and preferred backend settings.

### Traffic is being sent to more distant MIGs or NEGs before closer ones

This is the intended behavior when preferred backends are configured with more distant MIGs or NEGs. If you don't want this behavior, change the values in the preferred backends field.

### Traffic is not being sent to MIGs or NEGs that have many unhealthy endpoints

This is the intended behavior when the MIGs or NEGs are drained because an `autoCapacityDrain` is configured. With this setting, MIGs or NEGs with a lot of unhealthy endpoints will be removed from load balancing decisions and thus would be avoided. If this behavior is undesired, you can disable the `autoCapacityDrain` setting. But note that this means traffic may be sent to MIGs or NEGs with a lot of unhealthy endpoints and thus the requests may fail with errors.

### Traffic is not being sent to some MIGs or NEGs when some MIGs or NEGs are preferred

This is the intended behavior if MIGs or NEGs configured as preferred have not yet reached capacity.

When preferred backends are configured and they have not reached their capacity limit, traffic won't be sent to other MIGs or NEGs. The preferred MIGs or NEGs will be assigned first based on the RTT latency to these backends.

If you prefer to have traffic sent elsewhere, you can either configure their backend service without preferred backends or with more conservative capacity estimates for the preferred MIGs or NEGs.

### Traffic is being sent to too many distinct MIGs or NEGs from a single source

This is the intended behavior if spray-to-region or spray-to-world is used. However, you might experience issues with wider distribution of your traffic. For example, cache hit rates might be reduced as backends see traffic from a wider selection of clients. In this case, consider using other algorithms, such as waterfall by region.

### Traffic is being sent to a remote cluster when backend health changes

When `failoverHealthThreshold` is set to a high value, this is the intended behavior. If you want traffic to stay in the primary backends when there are transient health changes, set `failoverHealthThreshold` to a lower value.

### Healthy endpoints are overloaded when some endpoints are unhealthy

When `failoverHealthThreshold` is set to a low value, this is the intended behavior. When some endpoints are unhealthy, traffic for these unhealthy endpoints might be spread among the remaining endpoints in the same MIG or NEG. If you want the failover behavior to be triggered early, set `failoverHealthThreshold` to a higher value.

## Limitations and considerations

The following are limitations and considerations that you should be aware of when you configure advanced load balancing.

### Waterfall-by-zone

  * During transparent maintenance events, it is possible that traffic will be temporarily balanced outside of the local zone.

  * Expect cases where some MIGs or NEGs are at capacity, while other MIGs or NEGs in the same region are underutilized.

  * If the source of traffic to your service is in the same zone as its endpoints, you see reduced cross zone traffic.

  * A zone might be mapped to different clusters of internal physical hardware within Google data centers; for example, because of zone virtualization. In this case, VMs in the same zone may not be loaded evenly. In general, overall latency will be optimized.




### Spray-to-region

  * If the endpoints in one MIG or NEG go down, the consequences are typically spread out across a larger set of clients; in other words, a larger number of mesh clients might be affected, but less severely.

  * As the clients send requests to all the MIGs or NEGs in the region, in some cases, this might increase the amount of cross-zone traffic.

  * The number of connections opened to endpoints can increase, causing increased resource usage.




### Preferred backends

  * The MIGs or NEGs configured as preferred backends might be far away from the clients and might cause higher average latency for clients. This can happen even if there are other MIGs or NEGs which could serve the clients with lower latency.

  * Global load balancing algorithms (waterfall by region, spray-to-region, waterfall-by-zone) don't apply to MIGs or NEGs configured as preferred backends.




### Auto capacity drain

  * The minimum number of MIGs that are never drained is different from the value set when configured using `serviceLbPolicies`.

  * By default, the minimum number of MIGs that are never drained is 1.

  * If `serviceLbPolicies` is set, the minimum percentage of MIGs or NEGs that are never drained is 50%. Under both the configurations, a MIG or NEG is marked as unhealthy if less than 25% of instances or endpoints in the MIG or NEG are healthy.

  * For a MIG or NEG to undrain after a drain, at least 35% of instances or endpoints must be healthy. This is needed to make sure that a MIG or NEG does not vacillate between drain and undrained states.

  * The same restrictions for capacity scaler for backends that don't use a balancing mode also apply here.




## What's next

  * For setup instructions, see [Set up advanced load balancing](https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/set-up-advanced-load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
