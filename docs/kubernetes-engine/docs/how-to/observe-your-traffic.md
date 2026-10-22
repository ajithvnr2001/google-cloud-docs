---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic/
title: Observe your traffic using GKE Dataplane V2 observability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:41.472079+00:00
---

# Observe your traffic using GKE Dataplane V2 observability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Observe your traffic using GKE Dataplane V2 observability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to observe your traffic using GKE Dataplane V2 observability. For more information on the benefits and requirements of GKE Dataplane V2 observability, see [About GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability). For information on configuration, see [Set up GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability).

## How to use GKE Dataplane V2 observability

Start by enabling GKE Dataplane V2 metrics with Google Cloud Managed Service for Prometheus. To create custom dashboards and set alerts similar to any of the metrics that you've been monitoring, you can use [Google Cloud Observability](https://cloud.google.com/products/operations) tools such as [Cloud Monitoring Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

You can also configure any third-party dashboard or tooling that uses Prometheus, including Grafana. With your GKE cluster enabled with GKE Dataplane V2 observability, you can inspect traffic with GKE Dataplane V2 observability tools.

### Visualize metrics and Service dependencies

You can visualize Kubernetes traffic metrics and Service Dependencies as follows:

#### View cluster and workload observability metrics

To view GKE Dataplane V2 metrics for your clusters, perform the following steps in the Google Cloud console in the Metrics Explorer:

  1. Go to the **Monitoring Metrics Explorer** page.

  2. Select the **Metric** under the **Query** as either the **Prometheus Target prometheus/pod_flow_egress_flows_count** or **prometheus/pod_flow_ingress_flows_count/counter**.

  3. (Optional) Choose any selected filters based on **Labels**.

  4. (Optional) Save the chart to a custom **Dashboard**.




#### Visualize Service dependencies

Use the Hubble UI to be able to determine the dependencies of the Pod and Services deployed on your cluster at a glance. Visualize the traffic flows including those reaching out to external destinations. Filter by namespaces, Kubernetes labels, and more.

For instructions on how to deploy the Hubble UI, see [How to deploy the Hubble UI binary distribution](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability#how_to_deploy_the_hubble_ui_binary_distribution).

![Hubble-UI](https://docs.cloud.google.com/static/kubernetes-engine/images/hubble-ui.png)

#### Verify traffic flows

The Hubble UI can also be used to view live flows happening on your cluster. Each live flow shows the source and destination services, destination port, Policy verdicts and timestamps.

### Inspect traffic with GKE Dataplane V2 observability tools

You can capture and analyze network traffic using GKE Dataplane V2 observability tools, accessed using a private endpoint. The endpoint is exposed on an internal IP address, which you can access from within the Kubernetes cluster and the VPC within which the cluster resides.

To inspect network traffic metadata, use the following commands:

#### Use the built-in hubble-cli plugin to inspect network traffic
    
    
    alias hubble="kubectl exec -it deployment/hubble-relay -c hubble-cli -n gke-managed-dpv2-observability -- hubble"
    hubble observe
    

This command inspects network traffic for the cluster.

#### Use the built-in hubble-cli plugin to inspect network traffic in follow mode
    
    
    alias hubble="kubectl exec -it deployment/hubble-relay -c hubble-cli -n gke-managed-dpv2-observability -- hubble"
    hubble observe -f
    

This command inspects network traffic metadata in following mode for the cluster:

#### Use the built-in hubble-cli plugin to inspect network traffic in single namespace
    
    
    alias hubble="kubectl exec -it deployment/hubble-relay -c hubble-cli -n gke-managed-dpv2-observability -- hubble"
    hubble observe -n default
    

This command uses the built-in hubble-cli plugin to inspect network traffic for the default namespace in the cluster.

To enable `Hubble Relay` use the `--enable-dataplane-v2-flow-observability` flag.

### Analyze traffic flows

Use the Hubble CLI to observe live traffic flow dumps with the ability to filter with Kubernetes namespaces and more.

![Network inspection CLI](https://docs.cloud.google.com/static/kubernetes-engine/images/Network-sniffing-CLI.png)

## What's next

  * [Configure Metrics Explorer to view GKE Dataplane V2 metrics](https://docs.cloud.google.com/monitoring/charts/metrics-selector)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
