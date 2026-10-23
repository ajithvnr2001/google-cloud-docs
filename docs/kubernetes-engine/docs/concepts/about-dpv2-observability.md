---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability/
title: About GKE Dataplane V2 observability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:53.102939+00:00
---

# About GKE Dataplane V2 observability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About GKE Dataplane V2 observability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

GKE Dataplane V2 observability provides GKE Dataplane V2 metrics and insights into workloads on GKE clusters on Google Cloud. With GKE Dataplane V2 observability, starting with GKE versions **1.28** or later, you can:

  * Capture, observe, and alert on network metrics using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) and [Cloud Monitoring ](https://docs.cloud.google.com/monitoring) with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
  * Understand traffic flows for a particular Service in a cluster
  * Understand and identify issues with the network health of a Kubernetes workload
  * Verify [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)



GKE Dataplane V2 observability offers the following troubleshooting tools:

  * A Kubernetes cluster Network Topology
  * A Kubernetes Network Policy verdict table with live traffic flows and connection information
  * Command-line tooling for troubleshooting Kubernetes traffic flows



### GKE Dataplane V2 metrics

GKE Dataplane V2 metrics provide traffic flow information for the following:

  * **Traffic flows:** insights about how GKE handles flows between Pods and Services.
  * **Network policy enforcement:** information about how GKE enforces Kubernetes Network Policies.

**Note:** Observability draws insights from Layer 3 and Layer 4 network data. This aligns with GKE's Network Policies, which also function at Layer 3 and Layer 4.



You can use GKE Dataplane V2 metrics to monitor and troubleshoot Kubernetes workloads using the following tools:

  * **Google Cloud Managed Service for Prometheus** to view and analyze your GKE Dataplane V2 metrics. You can modify the Google Cloud Managed Service for Prometheus configuration to add or remove the metrics of your choice for Google Cloud Managed Service for Prometheus ingestion.
  * **Cloud Monitoring Metrics Explorer** to view Pod-level traffic flow details.
  * **Cloud Monitoring** to explore and use any metric. For example, you can create alerts that trigger when GKE Dataplane V2 metrics exceed certain thresholds.
  * **Self-managed Grafana** to visualize metrics collected by Google Cloud Managed Service for Prometheus.



When you enable Google Cloud Managed Service for Prometheus:

  * GKE creates a `PodMonitoring` resource
  * GKE exposes the metrics endpoint



To consume metrics with Google Cloud Managed Service for Prometheus and to be able to create a `PodMonitoring` resource, you must enable Google Cloud Managed Service for Prometheus on the cluster. If you don't enable Google Cloud Managed Service for Prometheus, GKE exposes the metrics endpoint but does not create a `PodMonitoring` resource.

When you enable GKE Dataplane V2 metrics for a cluster, Google Cloud Managed Service for Prometheus ingests the following GKE Dataplane V2 metrics:

GKE Dataplane V2 Metric | Type | Description  
---|---|---  
`prometheus.googleapis.com/pod_flow_egress_flows_count/counter` | cumulative  | Total number of flows from a Pod.   
`prometheus.googleapis.com/pod_flow_ingress_flows_count/counter` | cumulative  | Total number of flows to a Pod.   
  
Enabling GKE Dataplane V2 metrics opens the metrics port on each Kubernetes node.

Additional metrics are also available, including from the open source observability platform [Hubble](https://docs.cilium.io/en/v1.13/observability/metrics/#hubble). By default, Google Cloud Managed Service for Prometheus doesn't ingest these additional metrics but you can configure Google Cloud Managed Service for Prometheus to collect them. To collect these metrics, [configure a `PodMonitoring` custom resource (CR)](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring).

The following table describes additional Hubble metrics:

Hubble metric  | Type  | Description   
---|---|---  
`hubble_flows_processed_total` | cumulative  | Total number of flows processed.   
`hubble_drop_total` | cumulative  | Total number of flows dropped.   
`hubble_port_distribution_total` | cumulative  | Total number of flows processed aggregated by port number.   
`hubble_tcp_flags_total` | cumulative  | Total number of flows processed with given TCP flags set.   
`hubble_icmp_total` | cumulative  | Total number of ICMP flows processed.   
  
To collect these additional metrics, you need to create a `PodMonitoring` resource in your cluster.

For example, to create a `PodMonitoring` resource that collects all the available Hubble metrics, complete the following steps:

  1. Save the following manifest as `pod-monitoring.yaml`:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: hubble-metrics
           namespace: kube-system
           # The resource is created in the `kube-system` namespace because the Cilium pods that emit the metrics reside in that namespace
         spec:
           selector:
             matchLabels:
               k8s-app: cilium
           endpoints:
           - port: 9965
             interval: 30s
             path: /metrics
             metricRelabeling:
             - action: keep
               sourceLabels: [__name__]
               regex: (hubble_flows_processed_total|hubble_drop_total|hubble_port_distribution_total|hubble_tcp_flags_total|hubble_icmp_total)
         

  2. Apply the manifest to your cluster by running the following command:
         
         kubectl apply -f pod-monitoring.yaml
         

After applying this configuration, the additional Hubble metrics are available in Google Cloud Managed Service for Prometheus.




### GKE Dataplane V2 observability tools

GKE Dataplane V2 observability provides a Managed Hubble solution with network observability and security insights for Kubernetes workloads deployed with GKE Dataplane V2.

When enabled, GKE Dataplane V2 observability deploys the following components to your cluster:

  * **Hubble Relay:** a service that collects network telemetry data about your Pods from each node.

  * **Hubble CLI:** a command-line interface tool providing live traffic information within the cluster.




You can deploy the following component after you enable GKE Dataplane V2 observability to your cluster:

  * **Hubble UI:** a web-based tool that you can use to view and analyze the network telemetry data that is collected by Hubble Relay. You must enable GKE Dataplane V2 observability to deploy Hubble UI.



## How GKE Dataplane V2 metrics and observability works

GKE Dataplane V2 observability uses the following components and tools to collect metrics and provide insights into your network traffic:

  * GKE Dataplane V2: GKE Dataplane V2 metrics and observability use GKE Dataplane V2 datapath based on [eBPF](https://ebpf.io/what-is-ebpf/) to collect metrics about traffic flows and network policy enforcement for a Pod based on a given workload.

  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus): GKE Dataplane V2 metrics configures the Google Cloud Managed Service for Prometheus agent to ingest aggregated metrics to Google Cloud Managed Service for Prometheus, a scalable monitoring solution that can ingest and store large amounts of data that also lets you build on the [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/solutions/gke).

  * [Hubble](https://github.com/cilium/hubble): GKE Dataplane V2 observability uses Hubble, an open source observability project. Hubble enables network observability and security insights for Kubernetes workloads deployed with an eBPF Dataplane.

Hubble flow events occur when:

    * A network connection is first established

    * A TCP flag is first seen, which indicates the state of the TCP connection

    * A packet is transmitted after at least five seconds have passed since the last flow event

**Hubble metrics:** counts the number of flow events in a Kubernetes cluster that you can use to identify which Pods are communicating with each other.

**Note:** Hubble flow metrics don't count the amount of data or number of packets transmitted.
  * **Enabling metrics and observability:** You can enable GKE Dataplane V2 and observability independent of each other. To enable the Network topology visualization in the open source Hubble UI, you must [enable GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability#configure-gke-dpv2-observability-tools).

  * **Autopilot clusters:**

    * Metrics are enabled by default

    * Observability tools are disabled by default

    * You must create the Cluster`PodMonitoring` resource to gather metrics in the Google Cloud Managed Service for Prometheus

  * **Standard clusters:**

    * Metrics are disabled by default

    * Observability tools are disabled by default

    * If you have Google Cloud Managed Service for Prometheus enabled, a `PodMonitoring` resource is created automatically

    * A `PodMonitoring` resource is marked as **ensure exists**. You can stop sending metrics to Google Cloud Managed Service for Prometheus by editing the `PodMonitoring` resource to disable all metrics




### GKE Dataplane V2 observability endpoints

GKE Dataplane V2 observability components expose the following two observability endpoints:

  * **Metrics endpoint:** an HTTP endpoint that exposes traffic metrics in Prometheus format. The `anetd` Pod exposes the metrics endpoint on each cluster node on port 9965.

  * **Flows port:** a gRPC endpoint. The `hubble-relay` Pod exposes the flows port endpoint as a Kubernetes `ClusterIP` Service on port 443. The `hubble-relay` Pod is the backend for the Kubernetes `ClusterIP` Service and all requests to the Kubernetes `ClusterIP` Service are forwarded to the `hubble-relay` Pod. You can access the flow port using Hubble CLI or the Hubble UI.




## Limitations

  * GKE Dataplane V2 observability has a cluster-wide limit of 5000 nodes.
  * GKE Dataplane V2 metrics and observability only work in clusters on Google Cloud with [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) enabled.
  * Given that the metrics are flow-based, they don't provide an accurate representation of the amount of data transmitted in a network flow.
  * When Dataplane V2 metrics are enabled, the `anetd` Pod memory might continuously increase due to Hubble metrics collection. This is expected behavior as metrics are stored in memory until the Pod is restarted.



## What's next

  * Learn how to [set up GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability).
  * Learn how to [observe your traffic using GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic).
  * Learn how to [use GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).
  * Learn how to [use Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
