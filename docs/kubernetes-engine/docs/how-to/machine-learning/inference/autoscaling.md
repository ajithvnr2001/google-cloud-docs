---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling/
title: Configure autoscaling for LLM workloads on GPUs with Google Kubernetes Engine (GKE) \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:51.521142+00:00
---

# Configure autoscaling for LLM workloads on GPUs with Google Kubernetes Engine (GKE)  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Configure autoscaling for LLM workloads on GPUs with Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can configure autoscaling for large language model (LLM) workloads running on GPUs within Google Kubernetes Engine (GKE). Autoscaling automatically adjusts resources to manage fluctuating demand, optimize performance, and reduce operational costs. This process involves deploying the Gemma LLM and using the GKE [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) (HPA) to automatically scale pods. The deployment also integrates the [Hugging Face Text Generation Interface](https://huggingface.co/docs/text-generation-inference/en/index) (TGI) serving framework for efficient inference.

To learn more about selecting metrics for autoscaling, see [Best practices for autoscaling LLM workloads with GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Familiarize yourself with the workflow in [Serve Gemma open models using GPUs on GKE with Hugging Face TGI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tgi#deploy-tgi).



## Autoscale using server metrics

You can use the workload-specific performance metrics that are emitted by the TGI inference server to direct autoscaling for your Pods. To learn more about these metrics, see [Server metrics](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#server-metrics).

To set up custom-metric autoscaling with server metrics, follow these steps:

  1. **Export the metrics from the TGI server to Cloud Monitoring**. You use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed), which simplifies deploying and configuring your Prometheus collector. Google Cloud Managed Service for Prometheus is enabled by default in your GKE cluster; you can also [enable it manually](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke).

The following example manifest shows how to set up your [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring) resource definition to direct Google Cloud Managed Service for Prometheus to scrape metrics from your Pods at recurring intervals of 15 seconds:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: gemma-pod-monitoring
         spec:
           selector:
             matchLabels:
               app: gemma-server
           endpoints:
           - port: 8000
             interval: 15s
         

  2. **Install the Custom Metrics Stackdriver Adapter.** This adapter makes the custom metric that you exported to Monitoring visible to the HPA controller. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation.

The following example command shows how to install the adapter:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml
         

  3. **Set up the custom metric-based HPA resource.** Deploy an HPA resource that is based on your preferred custom metric. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation.

Select one of these tabs to see examples of how to configure the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscaler-v2-autoscaling) resource in your manifest:

### Queue size

This example uses the `tgi_queue_size` TGI server metrics, which represents the number of requests in the queue.

To determine the right queue size threshold for HPA, see [Best practices for autoscaling LLM inference workloads with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#queue-threshold).
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: gemma-server
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: tgi-gemma-deployment
           minReplicas: 1
           maxReplicas: 5
           metrics:
           - type: Pods
             pods:
               metric:
                 name: prometheus.googleapis.com|tgi_queue_size|gauge
               target:
                 type: AverageValue
                 averageValue:  $HPA_AVERAGEVALUE_TARGET
         

### Batch size

This example uses the `tgi_batch_size` TGI server metric, which represents the number of requests in the current batch.

To determine the right batch size threshold for HPA, see [Best practices for autoscaling LLM inference workloads with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#batch-threshold).
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: gemma-server
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: tgi-gemma-deployment
           minReplicas: 1
           maxReplicas: 5
           metrics:
           - type: Pods
             pods:
               metric:
                 name: prometheus.googleapis.com|tgi_batch_current_size|gauge
               target:
                 type: AverageValue
                 averageValue:  $HPA_AVERAGEVALUE_TARGET
         




## Autoscale using GPU metrics

You can use the usage and performance metrics emitted by the GPU to direct autoscaling for your Pods. To learn more about these metrics, see [GPU metrics](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#gpu-metrics).

To set up custom-metric autoscaling with GPU metrics, follow these steps:

  1. **Export the GPU metrics to Cloud Monitoring**. If your GKE cluster has [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics) enabled, it automatically sends the GPU utilization metric to Cloud Monitoring through the `container/accelerator/duty_cycle` system metric, every 60 seconds.

     * To learn how to enable GKE system metrics, see [Configure metrics collection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#enable-system-metrics).
     * To set up managed collection, see [Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke) in the Google Cloud Managed Service for Prometheus documentation.
     * For additional techniques to monitor your GPU workload performance in GKE, see the [Run GPUs in GKE Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#monitoring).

The following example manifest shows how to set up your [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring) resource definition to ingest metrics from the [NVIDIA DCGM workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics):
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: nvidia-dcgm-exporter-for-hpa
      namespace: gke-managed-system
      labels:
        app.kubernetes.io/name: nvidia-dcgm-exporter
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: gke-managed-dcgm-exporter
      endpoints:
        - port: metrics
          interval: 15s
          metricRelabeling:
            - action: keep
              sourceLabels: [__name__]
            - action: replace
              sourceLabels: [__name__]
              targetLabel: __name__
              regex: DCGM_FI_DEV_GPU_UTIL
              replacement: dcgm_fi_dev_gpu_util
    

In the code, make sure to change the DCGM metric name to use in HPA to lowercase. This is because there's a [known issue](https://github.com/kubernetes/kubernetes/issues/72996) where HPA doesn't work with uppercase external metric names. For clusters not utilizing a managed DCGM exporter, ensure the HPA's `metadata.namespace` and `spec.selector.matchLabels` identically match the DCGM exporter's configuration.This precise alignment is critical for successful custom metric discovery and querying by the HPA.

  2. **Install the Custom Metrics Stackdriver Adapter.** This adapter makes the custom metric you exported to Monitoring visible to the HPA controller. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation.

The following example command shows how to execute this installation:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml
         

  3. **Set up the custom metric-based HPA resource.** Deploy a HPA resource based on your preferred custom metric. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation.

     * Identify an average value target for HPA to trigger autoscaling. You can do this experimentally; for example, generate increasing load on your server and observe where your GPU utilization peaks. Be mindful of the [HPA tolerance](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details), which defaults to a 0.1 no-action range around the target value to dampen oscillation.
     * We recommend using the [locust-load-inference tool](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) for testing. You can also create a Cloud Monitoring [custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

Select one of these tabs to see an example of how to configure the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscaler-v2-autoscaling) resource in your manifest:

### Duty cycle (GKE system)
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: gemma-hpa
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: tgi-gemma-deployment
      minReplicas: 1
      maxReplicas: 5
      metrics:
      - type: External
        external:
          metric:
            name: kubernetes.io|container|accelerator|duty_cycle
            selector:
              matchLabels:
                resource.labels.container_name: inference-server
                resource.labels.namespace_name: default
          target:
            type: AverageValue
            averageValue:  $HPA_AVERAGEVALUE_TARGET
    

### Duty cycle (DCGM)
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: gemma-hpa
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: tgi-gemma-deployment
      minReplicas: 1
      maxReplicas: 5
      metrics:
      - type: External
        external:
          metric:
            name: prometheus.googleapis.com|dcgm_fi_dev_gpu_util|unknown
            selector:
              matchLabels:
                metric.labels.exported_container: inference-server
                metric.labels.exported_namespace: default
          target:
            type: AverageValue
            averageValue:  $HPA_AVERAGEVALUE_TARGET
    




## What's next

  * Learn how to [autoscale based on custom or external metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics).
  * Learn more about [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) from the open source Kubernetes documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
