---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics/
title: Autoscale Pods by using custom or external metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:54.209208+00:00
---

# Autoscale Pods by using custom or external metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Autoscale Pods by using custom or external metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to fetch and use custom and external metrics to scale Pods horizontally.

To fetch the metrics, you can use a GKE managed metrics adapter. This managed solution is available both for metrics in Cloud Monitoring that can be queried with PromQL, and certain custom Pod metrics that are exposed under an HTTP endpoint in the Prometheus format.

The workload autoscaler can then use this data to scale workloads more efficiently. For example, you can use this feature to monitor queue depth or cache utilization, and then allow the autoscaler to increase or decrease the number of Pods. From the vLLM example, a metric that could be useful to track cache utilization is `vllm:gpu_cache_usage_perc`.

As an alternative to the managed metrics adapter, to autoscale by using any metric, you can fetch the metric by manually configuring a metrics adapter to send metrics to an autoscaler. This workflow involves installing a third-party adapter, such as the [Stackdriver Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter), and configuring permissions. For example, see the [Optimize Pod autoscaling based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics) tutorial.

The rest of this document focuses on the managed metrics adapter.

## Fetch metrics

You can fetch metrics using the managed metrics adapter in the following ways:

  * Custom pod metrics emitted by Pods can be fetched within the cluster. These metrics can be used for autoscaling without needing to transit through a monitoring system like Cloud Monitoring.
  * Custom pod metrics stored in Cloud Monitoring can be fetched by using a PromQL query. Those metrics are emitted by Pods and exported to Cloud Monitoring, typically by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus). Compared to the previous method, this approach lets you use PromQL features such as calculating percentiles, or reading historical values.
  * External metrics can be fetched from Cloud Monitoring by using a PromQL query.



After you fetch the metric, you then reference the metric in a HorizontalPodAutoscaler object. For more information, see the Use the metrics in the horizontal Pod autoscaler section.

For an overview about autoscaling based on metrics, see [About autoscaling workloads based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics).

### Fetch custom metrics within the cluster

Custom metrics come from the service or application that you are running. For one example of exposed metrics, see the [metrics that are exposed](https://docs.vllm.ai/en/latest/design/metrics.html?h=v0+metrics#metrics) by the [vLLM Engine](https://docs.vllm.ai/en/latest/index.html).

#### Requirements

Requirements for the Pods are the following:

  * GKE 1.37.0-gke.3100000 and later. This feature is also available in [preview](https://docs.cloud.google.com/products#product-launch-stages) for GKE versions 1.36.4-gke.1247000 and later.
  * Use [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) with the performance profile.



Requirements for the metrics are the following:

  * The metrics must be emitted by Pods in the workload being autoscaled.
  * Metrics must be accessible on an HTTP endpoint. The endpoint path is by default `/metrics`.
  * Metrics must be formatted according to the [Prometheus standard](https://prometheus.io/).
  * Only gauge metrics are supported.
  * By default, a maximum of 50 unique metrics can be exposed per node. If you need to expose more metrics, you can [request a higher amount of additional memory](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics#confirm_metrics_agent_has_sufficient_memory).
  * If you are using the [preview](https://docs.cloud.google.com/products#product-launch-stages) version of this feature, in GKE version 1.36.4-gke.1247000 to version 1.37.0-gke.3100000, then the following additional requirements apply: 
    * Label names in Pod label selectors must not contain special characters. Only a-z letters (lowercase or uppercase), numbers, hyphens, and underscores are supported.
    * When you use filtering based on metrics labels, the label key must match the regular expression `^[a-zA-Z_][a-zA-Z0-9_]*` (start with a letter or an underscore, and only contain letters, numbers, or underscores).
    * A maximum of 20 unique metrics can be exposed per cluster.



#### Define the metric

  1. Choose a metric to expose. You can choose any metric that your workload exposes, and that also meets the requirements listed in the previous section.

If your workload exposes multiple metrics with the same name but different labels, add a label filter to help ensure only one is selected.

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
                     name: METRIC_NAME
                     prometheusMetricName: METRIC_PROMETHEUS_NAME
         

Replace the following to match your workload:

     * `NAME`: the name of the AutoscalingMetric object.
     * `NAMESPACE`: the namespace that the Pods are in.
     * `APP_LABEL_NAME` and `APP_LABEL_VALUE`: the label name and value matching the Pods that emit the metric.
     * `METRIC_PORT`: the port number.
     * `METRIC_PATH`: the path to the metric. Verify the path used by your service or application; this path is often `/metrics`.
     * `METRIC_NAME`: the name of the metric that you are exposing. The name must match the regular expression `^[a-z]([-a-z0-9]*[a-z0-9])?`, and have a length of no more than 63 characters. This expression means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits. However, the last character cannot be a hyphen.
     * Optional: `METRIC_PROMETHEUS_NAME`: the Prometheus metric name as exposed by the Pod. You can use this field to rename the metric, for example, because the metric name exposed by the Pod does not comply with the name restrictions set by the autoscaler.

For more information about name restrictions, see the [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#limitations) for horizontal Pod autoscaling. You can also filter metrics using metric labels.

  3. Apply the manifest by using the following command:
         
         kubectl apply -f FILE_NAME_AUTOSCALING_METRIC.yaml
         

Replace `FILE_NAME_AUTOSCALING_METRIC` with the name of the YAML file.

  4. Verify the metric definition and retrieve the metric name to use for the HorizontalPodAutoscaler object:

     1. Run the `kubectl describe` command for the AutoscalingMetric custom resource:
            
            kubectl describe autoscalingmetric NAME -n NAMESPACE
            

Replace the following:

        * `NAME`: the name of the AutoscalingMetric object.
        * `NAMESPACE`: the namespace of the AutoscalingMetric object.
     2. Look at the `Status` field. If no errors are listed, then the object is valid.

     3. Copy the name in the `HPA Name` field. This is the name you add to the HorizontalPodAutoscaler object. This name has the following format: `autoscaling.gke.io|NAME|METRIC_NAME`.




The metric is now defined in the AutoscalingMetric object. To autoscale with this metric, you need to reference it in a HorizontalPodAutoscaler object. For more information, see the Use the metrics in the HorizontalPodAutoscaler object section.

When you add the custom resource, the metric is pushed to the autoscaling API. The metric is read every few seconds and sent to the workload autoscaler.

#### Filtering metrics using metric labels

Filtering metrics using metric labels is available on GKE 1.36.0-gke.1759000 or later.

The metrics emitted by your workloads often include labels. Labels are key-value pairs that let you add dimensions to a value. For example, a metric counting the number of requests to a HTTP endpoint sliced by method and environment could use labels to specify this context. This example could look like the following:
    
    
    http_requests_total{method="GET", env="prod"} 11111
    http_requests_total{method="PUT", env="staging"} 22222
    

You can use label filters to help ensure that your metric specification exactly matches one metric. For example, to select only the first metric in the preceding example, use the following specification for the AutoscalingMetric `gauge` metric:
    
    
    apiVersion: autoscaling.gke.io/v1beta1
    kind: AutoscalingMetric
    metadata:
      name: filter-sample
    spec:
      # Several lines are omitted here.
          metrics:
          - gauge:
              name: http_requests_total
              filter:
                matchLabels:
                  method: GET
                  env: prod
    

The keys of the `matchLabels` key-value pairs must match the regular expression `^[a-zA-Z_][a-zA-Z0-9_]*`: that is, start with a letter or an underscore, and only contain letters, numbers, or underscores.

### Fetch custom or external metrics from Cloud Monitoring

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can fetch metrics from Cloud Monitoring to scale your workloads. GKE supports fetching two types of metrics from Cloud Monitoring:

  * **Custom metrics** : use this type to apply PromQL features, such as calculating percentiles or reading historical values, to the metrics emitted by your cluster workloads.
  * **External metrics** : use this type to scale based on an entity outside of the cluster, such as the number of pending messages on a Pub/Sub subscription.



Otherwise, fetch custom metrics from the cluster.

#### Requirements

  * GKE version 1.36.2-gke.2771000 or later.
  * Metrics must be stored in Cloud Monitoring. For example, you can use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).
  * A maximum of 100 metrics is supported per cluster. This limit is the combined total for both custom and external metrics.
  * The metrics in Cloud Monitoring must be in the same Google Cloud project as the cluster that is being autoscaled.



#### Define the metric

You use a YAML file to define the metrics, including the specific PromQL query.

**Note:** To conserve cluster resources, the autoscaling metrics adapter runs with zero replicas by default. When you apply an AutoscalingMetric object that includes a PromQL query, the adapter scales to one replica.

Choose one of the following configurations, depending on whether you are fetching a _custom metric_ or an _external metric_ :

  1. Create an AutoscalingMetric object and define the metric to fetch.

###  Custom metric (Pods) 
         
         apiVersion: autoscaling.gke.io/v1beta1
         kind: AutoscalingMetric
         metadata:
           name: NAME
           namespace: NAMESPACE
         spec:
           metrics:
             - promql:
                 name: METRIC_NAME
                 query: PROMQL_QUERY
                 type: Pods # Specifies that the metric is associated with Pods.
                 # metricLabels are optional, default to the labels used by Google
                 # Cloud Managed Service for Prometheus. The defaults are used
                 # below.
                 metricLabels:
                   podName: "pod"
                   namespace: "namespace"
                   clusterName: "cluster"
                   location: "location"
                   projectId: "project_id"
         

Replace the following:

     * `NAME`: the name of the AutoscalingMetric object.
     * `NAMESPACE`: the namespace of the AutoscalingMetric object, which must match the namespace of the workload you want to scale.
     * `METRIC_NAME`: the name of the metric that the HorizontalPodAutoscaler object uses.
     * `PROMQL_QUERY`: the PromQL query that queries the metric. The PromQL query must return a vector with one entry per Pod in the autoscaled resource—for example, one entry per Pod in a Deployment.

You can define more than one metric in a single AutoscalingMetric manifest by adding additional `promql` entries to the `metrics` array.

In this manifest, the following applies:

     * The `type: Pods` field indicates that the metrics are emitted by Pods.
     * Optional: The `metricLabels` fields are the label names in the PromQL query result that list the resource details (such as the Pod name, namespace, or cluster information). The custom metric emitted by a Pod must include a label matching the `podName` field, specifying which Pod the metric is associated with. This label is configured automatically when you send metrics to Cloud Monitoring using Google Cloud Managed Service for Prometheus.

If these fields are not specified in the AutoscalingMetric object, then the following default values are used to find the information in the label. These default values are the same label names that are configured by Google Cloud Managed Service for Prometheus:

       * `podName: "pod"`
       * `namespace: "namespace"`
       * `clusterName: "cluster"`
       * `location: "location"`
       * `projectId: "project_id"`

###  External metric 
    
    apiVersion: autoscaling.gke.io/v1beta1
    kind: AutoscalingMetric
    metadata:
      name: NAME
      namespace: NAMESPACE
    spec:
      metrics:
        - promql:
            name: METRIC_NAME
            query: PROMQL_QUERY
            type: External  # Optional, default is 'External'
    

Replace the following:

     * `NAME`: the name of the AutoscalingMetric object.
     * `NAMESPACE`: the namespace of the AutoscalingMetric object, which must match the namespace of the workload you want to scale.
     * `METRIC_NAME`: the name of the metric that the HPA uses.
     * `PROMQL_QUERY`: the PromQL query that queries the metric. The PromQL query must return a scalar value, or a vector with a unique entry.
**Note:** You can define more than one metric in a single AutoscalingMetric manifest by adding additional `promql` entries to the `metrics` array.

  2. Verify the PromQL queries in Cloud Monitoring to ensure that they return the expected metrics. It's easier to verify the queries as you set them up than it is to troubleshoot unexpected behaviors later.

To verify the queries, see the following section: Verify PromQL queries.

  3. Apply the AutoscalingMetric manifest to the cluster:
         
         kubectl apply -f MANIFEST_FILE.yaml
         

Replace `MANIFEST_FILE` with the name of the YAML file.

  4. Verify the metric definition and retrieve the metric name to use for the HorizontalPodAutoscaler object:

     1. Run the `kubectl describe` command for the AutoscalingMetric custom resource:
            
            kubectl describe autoscalingmetric NAME -n NAMESPACE
            

Replace the following:

        * `NAME`: the name of the AutoscalingMetric object.
        * `NAMESPACE`: the namespace of the AutoscalingMetric object.
     2. Look at the `Status` field. If no errors are listed, then the object is valid.

     3. Copy the name in the `HPA Name` field. This is the name you add to the HorizontalPodAutoscaler object. This name has the following format: `autoscaling.gke.io|NAME|METRIC_NAME`.




The metric is now defined in the AutoscalingMetric object. To autoscale with this metric, you need to reference it in a HorizontalPodAutoscaler object. For more information, see the Use the metrics in the HorizontalPodAutoscaler object section.

## Use the metrics in the HorizontalPodAutoscaler object

  1. Create a HorizontalPodAutoscaler object. The HorizontalPodAutoscaler metric type must match the value of the `type` field defined in the AutoscalingMetric custom resource. Choose one of the following configurations depending on your metric type:

**Option 1: External metric**
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: HPA_NAME
           namespace: NAMESPACE
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: DEPLOYMENT_NAME
           minReplicas: MIN_REPLICAS
           maxReplicas: MAX_REPLICAS
           metrics:
             **- type: External
               external:
                 metric:
                   name: autoscaling.gke.io|NAME|METRIC_NAME
                 target:
                   type: AverageValue
                   averageValue: AVERAGE_VALUE**
         

**Option 2: Pods metric**
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: HPA_NAME
           namespace: NAMESPACE
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: DEPLOYMENT_NAME
           minReplicas: MIN_REPLICAS
           maxReplicas: MAX_REPLICAS
           metrics:
             **- type: Pods
               pods:
                 metric:
                   name: autoscaling.gke.io|NAME|METRIC_NAME
                 target:
                   type: AverageValue  # This is the only supported target type
                   averageValue: AVERAGE_VALUE**
         

Replace the following:

     * `HPA_NAME`: the name of the HorizontalPodAutoscaler object.
     * `NAMESPACE`: the namespace of the HorizontalPodAutoscaler object, which must match the namespace of the workload and the AutoscalingMetric resource.
     * `DEPLOYMENT_NAME`: the name of the workload Deployment you want to scale.
     * `MIN_REPLICAS`: the minimum number of running Pods.
     * `MAX_REPLICAS`: the maximum number of running Pods.
     * `NAME`: the name of the AutoscalingMetric custom resource you created.
     * `METRIC_NAME`: the name of the metric defined in the AutoscalingMetric resource.
     * `AVERAGE_VALUE`: the target metric value at which the autoscaler scales the workload.

When you are creating your own HorizontalPodAutoscaler object, note the following:

     * The AutoscalingMetric, Deployment, and HorizontalPodAutoscaler objects must be in the same namespace.
     * The preceding example uses the `type: AverageValue` field-value pair. Note that `type: Value` is also supported for external metrics.
     * The preceding example uses a Deployment object only as an example. You can also autoscale any object supported by HorizontalPodAutoscaler objects, such as a ReplicaSet object.
  2. Apply the HorizontalPodAutoscaler manifest:
         
         kubectl apply -f HPA_MANIFEST_FILE.yaml
         

Replace `HPA_MANIFEST_FILE` with the name of the YAML file.




## Troubleshoot metrics that are fetched for autoscaling

To troubleshoot issues with fetching metrics, you can review the logs or the status of the AutoscalingMetric custom resource.

### Autoscaling metrics adapter has zero replicas

When you inspect the `autoscaling-metrics-adapter` deployment in `kube-system`, you might notice that it has zero replicas.

By default, the adapter runs with zero replicas to conserve cluster resources. This is expected behavior. The deployment only scales up to one replica when an AutoscalingMetric custom resource that requires PromQL processing exists in the cluster.

If you configured an AutoscalingMetric object with a PromQL query but the adapter has not scaled up, verify that the object is successfully created in the cluster.

### Review the logs

To find issues with the controller responsible for getting metrics from Cloud Monitoring, you can review its logs.

You can view the logs in the Google Cloud console:

  1. Go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         resource.type="k8s_container"
         resource.labels.namespace_name="kube-system"
         resource.labels.container_name="autoscaling-metrics-adapter"
         




Alternatively, to view the logs by using `kubectl`, run the following command:
    
    
    kubectl logs deployment.apps/autoscaling-metrics-adapter -n kube-system
    

### Review the AutoscalingMetric status

You can review the status of the AutoscalingMetric custom resource to look for configuration errors.

  1. Inspect the AutoscalingMetric custom resource:
         
         kubectl describe autoscalingmetric NAME -n NAMESPACE
         

Replace the following:

     * `NAME`: the name of the AutoscalingMetric custom resource you created.
     * `NAMESPACE`: the namespace of the custom resource.
  2. For details about configured metrics, look at the `Status` field. These details include any warnings about configuration errors and the exact name of the metric as it should appear in the HorizontalPodAutoscaler object.

The following is an example of a valid status:
         
         Name:         sample-metric
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  autoscaling.gke.io/v1beta1
         Kind:         AutoscalingMetric
         Metadata:
           Creation Timestamp:  2026-08-10T14:41:58Z
           Generation:          1
           Resource Version:    1786372918604351020
           UID:                 c3f012a9-8f25-4399-ac91-12ae8f4426d7
         Spec:
           Metrics:
             Promql:
               Name:   pubsub_unacked
               Query:  sum(pubsub_subscription_num_undelivered_messages)
               Type:   External
         Status:
           Metric Statuses:
             Hpa Name:  autoscaling.gke.io|sample-metric|pubsub_unacked
             Name:      pubsub_unacked
         Events:        <none>
         

The following is an example of a status with a configuration error:
         
         Name:         bad-metric
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  autoscaling.gke.io/v1beta1
         Kind:         AutoscalingMetric
         Metadata:
           Creation Timestamp:  2026-08-10T14:42:40Z
           Generation:          1
           Resource Version:    1786372960414079010
           UID:                 a47d3ed4-f6f2-4c2c-9341-0de4e9752c3c
         Spec:
           Metrics:
             Promql:
               Name:   duplicate_metric
               Query:  sum(up)
               Type:   External
             Promql:
               Name:   duplicate_metric
               Query:  avg(up)
               Type:   External
         Status:
           Metric Statuses:
             **Errors:
               Multiple metrics defined with the same name.**
             Name:  duplicate_metric
         Events:    <none>
         




### Verify PromQL queries

If you fetch metrics from Cloud Monitoring by using a PromQL query, then an issue with the query can cause errors in retrieving the metric, or cause an unexpected value to be retrieved. For example, if you expect a percentage to be returned as a value from 1 to 100, but receive a value from 0 to 1 instead, then the resulting autoscaling behaves unexpectedly.

You can test the PromQL queries in Cloud Monitoring to verify that they return the expected metrics.

To verify the queries, do the following:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. At the top of the **Query builder** pane, select the **PromQL** tab.

  3. In the query editor, enter the PromQL query you want to test.

  4. Click **Run Query** to view the metrics on the chart.




## What's next

  * For an overview about autoscaling based on metrics, see [About autoscaling workloads based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics).
  * To autoscale using metrics that can't be defined with a PromQL query, see [Optimize Pod autoscaling based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
