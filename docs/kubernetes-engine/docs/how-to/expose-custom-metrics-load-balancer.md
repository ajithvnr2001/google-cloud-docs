---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-load-balancer/
title: Expose custom metrics for load balancers \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:07.565640+00:00
---

# Expose custom metrics for load balancers  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Expose custom metrics for load balancers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to send one or more metrics from a Pod or workload to your load balancer.

These metrics come from the service or application that you are running. For example, see the [metrics exposed](https://docs.vllm.ai/en/latest/design/metrics.html?h=v0+metrics#metrics) by the [vLLM Engine](https://docs.vllm.ai/en/latest/index.html).

The load balancer can then use this data with [utilization-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb) to balance workloads more efficiently. For example, you can use this feature to monitor the regions with heavier workload use, and then allow the load balancer to redirect traffic towards the region with the more available resources. From the vLLM example, a metric that could be useful to track utilization is [`vllm:gpu_cache_usage_perc`](https://docs.vllm.ai/en/latest/design/metrics.html?h=v0+metrics#v0-metrics).

## Requirements

Requirements for the Pods are the following:

  * GKE 1.35.1-gke.1396000 or later.
  * [Gateways API is enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway).
  * Using [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) with the performance profile.



Requirements for the metrics are the following.

  * Metrics must be accessible on an HTTP endpoint under the Pods that are being load balanced by your Gateway. The default endpoint path is `/metrics`.
  * Metrics must be formatted according to the [Prometheus standard](https://prometheus.io/).
  * Load-balancers have restrictions on metric names. For example, the name can't exceed 64 characters. For the full list of restrictions, see the details about the field `backends[].customMetrics[].name` in the [API reference for `BackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

If your service's metric does not comply with these restrictions, you can rename it using the `exportName` field.

  * Only gauge metrics between 0 and 1 are supported, with 1 representing utilization of 100%.

  * Label names in Pod label selectors must not contain special characters. Only a-z letters (lowercase or uppercase), numbers, hyphen, and underscore are supported.

  * Maximum of 20 unique metrics can be exposed per cluster. Other services have their own limits. For example, see the [limits and requirements for load balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics#metrics-limits-requirements). Note that a cluster is able to use more than one load balancer.




## GKE Utilization-Based Balancing (UBB) based on custom metrics

You can use GKE Utilization-Based Balancing (UBB) to let the load balancer distribute traffic based on the utilization of your backend Pods. Instead of relying on a generic metric like CPU, you can configure UBB to use custom metrics that are more relevant to your application's performance.

When you use UBB with custom metrics in GKE, the following limitations apply:

  * **Gateway API only:** you can only use UBB with custom metrics with Services that you expose using the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). GKE uses the GKE Gateway controller to interact with the Gateway API. The Service and Ingress APIs don't support UBB with custom metrics. The custom metrics must originate from the Pods that are members of the Services.
  * **No Cloud Service Mesh:** you can't use UBB with custom metrics with Cloud Service Mesh.
  * **Unsupported load balancers:** you can't use UBB with custom metrics with External Passthrough Network Load Balancers and External proxy Network Load Balancer.



## Expose metrics for load balancing

  1. Choose a metric to expose. You can choose any metric that your server exposes, and that also meets the requirements listed in the previous section. This example uses a custom metric named `queue_depth_util`.

  2. Add the following custom resource, replacing details that are specific to your metric and Pod:
         
         apiVersion: autoscaling.gke.io/v1beta1
         kind: AutoscalingMetric
         metadata:
           name: NAME
           namespace: NAMESPACE
         spec:
           metrics:
           - pod:
               selector:
                 matchLabels:
                   APP_LABEL_NAME: APP_LABEL_VALUE
               containers:
               - endpoint:
                   port: METRIC_PORT
                   path: METRIC_PATH
                 metrics:
                 - gauge:
                   name: METRIC
                   prometheusMetricName: METRIC_PROMETHEUS_NAME
                   loadBalancing:
                     enabled: true
         

Replace the following to match your workload:

     * `NAME`: the name of the AutoscalingMetric object.
     * `NAMESPACE`: the namespace that the Pods are in.
     * `APP_LABEL_NAME` and `APP_LABEL_VALUE`: the label name and value matching the Pods that emit the metric.
     * `METRIC_PORT`: the port number.
     * `METRIC_PATH`: the path to the metric. Verify the path used by your service or application; this path is often `/metrics`.
     * `METRIC`: the name of the metric that you are exposing. The name must match the regular expression `^[a-z]([a-z0-9_-]*[a-z0-9])?`, and have a length of no more than 63 characters. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, underscores, lowercase letters, or digits, except the last character, which must be a letter or a digit.
     * Optional: `METRIC_PROMETHEUS_NAME`: the Prometheus metric name as exposed by the Pod. You can use this field to rename the metric, for example because the metric name exposed by the Pod does not comply with the name restrictions set by the load balancer.

For the full list of restrictions, see the details about the field `backends[].customMetrics[].name` in the [API reference for `BackendService`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

  3. Apply the manifest using the following command:
         
         kubectl apply -f FILE_NAME.yaml
         

Replace `FILE_NAME` with the name of the YAML file.

When you have added the custom resource, the metric is pushed to the autoscaling API. The metric is read every few seconds and sent to the load balancer.

  4. To use this signal for load balancing purposes, provide a `GCPBackendPolicy`. For example:
         
         kind: GCPBackendPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: my-backend-policy
         spec:
           targetRef:
             group: ""
             kind: Service
             name: store-v1
           default:
             balancingMode: CUSTOM_METRICS
             customMetrics:
             -   name: gke.named_metrics.queue_depth_util
                 dryRun: false
         




Note that metrics reported by Prometheus follows a different naming standard. When the metrics are reported for load balancing, the GKE Metrics Agent internally prefixes them with `gke.named_metrics.` to comply with the BackendService API requirement.

To expose a second metric, follow the same steps to create another custom resource.

Now that you have exposed the metrics to the load balancer, you can configure the load balancer to use these metrics. For details, see [Configure the load balancer to use custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics#configure-lb).

For more information about working with the load balancer, see [Configure utilization-based load balancing for GKE Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb).

## Troubleshoot metrics that are exposed to the load balancer

To verify that the metrics are exposed to the load balancer correctly, you can do the following:

  * Verify the logs in the GKE Metrics Agent. If an error occurred when trying to expose the metrics, then the logs might have signaled that there is an error. For more information about how to look for errors, see [Troubleshooting system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics).
  * You can use the load balancer in dry run mode to look at all of the metrics that it receives. To learn more about testing the metrics using the `dryRun` flag, see [Configure the load balancer to use custom metrics](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics#configure-lb).



## What's next

  * For more details about utilization-based load balancing, see [About utilization-based load balancers for GKE Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb).
  * Learn how to [Configure utilization-based load balancing for GKE Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
