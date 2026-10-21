---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-uneven-traffic-distribution/
title: Troubleshoot uneven traffic distribution \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:17.769424+00:00
---

# Troubleshoot uneven traffic distribution  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-uneven-traffic-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot uneven traffic distribution Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to resolve issues with uneven traffic distribution to Kubernetes Services.

## Identify symptoms of uneven traffic distribution

Uneven traffic distribution, often referred to as hotspots, occurs when a subset of Pods or nodes handles a disproportionate amount of the total workload while others remain underutilized.

Common symptoms include:

  * **Performance Bottlenecks** : users might experience intermittent timeouts, HTTP 5xx errors, or packet loss on overutilized network connections.
  * **Resource Exhaustion** : specific Pods or nodes show significantly higher CPU or memory utilization than the rest of the fleet.
  * **Traffic Imbalance Patterns** : 
    * **Per-Pod Imbalance** : traffic hits only a small subset of available Pods, even though all Pods are reported as healthy and ready.
    * **Per-Node Imbalance** : one or more nodes receive significantly more packets or requests than others, often seen when using `externalTrafficPolicy: Local` with uneven Pod placement.
    * **Sticky Client Sessions** : all requests from a single high-volume client consistently route to the same backend Pod.



### Diagnosis using Cloud Monitoring

To confirm these symptoms, visualize traffic patterns by using the following metrics:

  * **For Layer 7 (Ingress/Gateway)** : plot `loadbalancing.googleapis.com/backend/request_count` and group by `backend_target` to compare request volumes across different backends.



## Understand common causes of uneven traffic distribution

This section describes common causes of uneven traffic distribution to Kubernetes Services. This imbalance can lead to performance bottlenecks, resource exhaustion on certain Pods, and reduced application availability, with some Pods receiving significantly more traffic than others while some receive very little or none.

### Session affinity causes uneven distribution

The following problem occurs when load balancers with session affinity enabled consistently route requests from the same client to the same backend Pod. If a particular client generates a large volume of traffic, that Pod becomes overloaded, leading to a hotspot where it receives significantly more load than others, while other Pods remain underutilized.

You can configure session affinity in Kubernetes Service objects using the `sessionAffinity` field.

When `sessionAffinity` is set to `ClientIP`, the Service makes sure that all connections originating from the same client IP address are consistently routed to the same backend Pod. This provides true client IP-based session affinity.

When `sessionAffinity` is set to `None` (the default behavior), Layer 4 load balancers typically distribute connections using a hash of various network parameters, such as a 4-tuple (client IP address, destination IP address, destination port, protocol) or a 5-tuple (including source port). While this hashing can provide some connection "stickiness" by consistently routing connections with identical tuple values to the same backend, it doesn't guarantee that all connections from a specific client IP address will always go to the same Pod if other tuple elements change.

For more information, see [Session Affinity](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-affinity).

For GKE Gateway, the `GCPTrafficDistributionPolicy` CRD configures session affinity. For more information, see [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).

For regional external passthrough Network Load Balancers, you can use session affinity to maintain connection stickiness to a specific backend. However, note that session affinity can itself cause uneven distribution if some clients generate more traffic than others.

For more information, see [Session Affinity](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#session_affinity) and [Backend service-based external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

The following example shows a Service manifest with `sessionAffinity: ClientIP`:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      type: LoadBalancer
      sessionAffinity: ClientIP  # This can cause uneven distribution
      ports:
      -   port: 80
        targetPort: 8080
      selector:
        app: my-app
    

### Connection pooling causes uneven distribution

Connection pooling occurs when load balancers reuse existing connections to specific Pods, even if other Pods have available capacity. This behavior can cause an imbalance if some connections are longer-lived or handle significantly more requests than others. This concentrates traffic on certain Pods, similar to session affinity, creating hotspots where those Pods become overloaded while other Pods remain underutilized.

Load balancers implement connection pooling to improve performance by reducing the overhead of establishing new connections. However, if not managed correctly, connection pooling can cause uneven traffic distribution, especially with applications that maintain long-lived connections.

To mitigate uneven distribution caused by connection pooling, implement strategies at the application or client level:

  * **Configure clients to use multiple connections** : instead of relying on a single long-lived connection, configure clients to open and manage a pool of multiple connections to the load balancer. This allows the load balancer to distribute new connection attempts across available backend Pods, improving overall traffic distribution.

  * **Periodically close and reopen connections** : for applications that naturally maintain long-lived connections, configure them or their clients to periodically close and reopen connections. While this incurs a slight overhead of connection re-establishment, it provides the load balancer with new opportunities to distribute subsequent connection attempts to different, less utilized backend Pods. This approach is particularly effective for services where connection termination and re-establishment isn't overly disruptive.

  * **Implement aggressive connection draining** : make sure that your Pods are configured for graceful shutdown and connection draining. When a Pod is gracefully terminated (for example, during a deployment or scale-down), the load balancer should stop sending new connections to it and allow existing connections to complete or drain. This enables traffic to shift to other Pods more smoothly and helps prevent traffic from being concentrated on terminating Pods.




By actively managing connection behavior, you can help load balancers distribute traffic more evenly, even with long-lived connections.

### 5-Tuple hashing causes uneven distribution

This is the default behavior for many Layer 4 load balancers when you don't explicitly configure session affinity. If many connections originate from the same client or use the same port combinations, this results in an uneven distribution.

To resolve imbalances caused by hashing, consider the following:

  * **Use Layer 7 load balancing** : GKE Ingress and Gateway operate at the request level, allowing them to distribute requests from a single client across multiple backend Pods.

  * **Adjust client behavior** : configure clients to use multiple connections or a larger pool of source ports.




### Uneven Pod distribution across nodes causes uneven distribution

This issue arises when Pods aren't evenly distributed across nodes and the load balancer doesn't use container-native load balancing. Nodes with more Pods receive more traffic, which can lead to some nodes being overloaded while others are underutilized.

This issue is especially relevant when you use `externalTrafficPolicy: Local`.

### External traffic policy settings cause uneven distribution

The `externalTrafficPolicy` setting on your Service impacts how traffic routes.

  * **Cluster** : allows the load balancer to distribute traffic to any node in the cluster. Use the `Cluster` setting for the most even distribution across all available nodes and Pods.
  * **Local** : routes traffic only to Pods running on the same node that received the traffic. This can lead to uneven distribution if you don't evenly distribute Pods across nodes.



### Node affinity causes uneven distribution

Using node affinity to restrict Pods to a subset of nodes can cause those nodes to become overloaded, especially if the workload isn't well-balanced across them.

Make sure that your Pods aren't pinned to specific nodes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
