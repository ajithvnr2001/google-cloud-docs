---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa/
title: Horizontal pod autoscaling (HPA) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:32.045334+00:00
---

# Horizontal pod autoscaling (HPA)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Horizontal pod autoscaling (HPA) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable horizontal pod autoscaling (HPA) for Google Cloud Managed Service for Prometheus. You can enable HPA by doing one of the following:

  * Using [KEDA (Kubernetes Event-driven Autoscaling)](https://keda.sh/), an open-source solution that has graduated from the Cloud Native Computing Foundation.
  * Using the [Custom Metrics Stackdriver Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter) library, developed and supported by Google Cloud.
  * Using the third-party [Prometheus Adapter](https://github.com/kubernetes-sigs/prometheus-adapter/) library.



You can't use the Stackdriver Adapter and the Prometheus Adapter together in the same cluster because their resource definitions overlap, as described in Troubleshooting. We recommend choosing only one solution for HPA.

Alternatively, GKE also provides [built-in support for autoscaling based on metrics in Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics).

## Use KEDA

KEDA (Kubernetes Event-driven Autoscaling) is the most recently released autoscaler that uses Prometheus metrics, and it is becoming a favored solution within the Prometheus community.

To get started, see [the KEDA documentation for integrating with Google Cloud Managed Service for Prometheus](https://keda.sh/docs/scalers/prometheus/#google-managed-service-for-prometheus).

## Use the Custom Metrics Stackdriver Adapter

The Custom Metrics Stackdriver Adapter supports querying metrics from Managed Service for Prometheus starting with [version v0.13.1 of the adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/releases/tag/cm-sd-adapter-v0.13.1).

To set up an example HPA configuration using the Custom Metrics Stackdriver Adapter, do the following:

  1. Set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) in your cluster.
  2. Install Custom Metrics Stackdriver Adapter in your cluster.
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml
         

  3. Deploy an example Prometheus metrics exporter and an HPA resource:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/examples/prometheus-to-sd/custom-metrics-prometheus-sd.yaml
         

This command deploys an exporter application that emits the metric `foo` and an HPA resource. The HPA scales this application up to 5 replicas to achieve the target value for the metric `foo`.

  4. If you use Workload Identity Federation for GKE, you must also grant the Monitoring Viewer role to the service account the adapter runs under. **Skip this step if you do not have[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled on your Kubernetes cluster.**
         
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format 'get(projectNumber)')
         gcloud projects add-iam-policy-binding projects/PROJECT_ID \
           --role roles/monitoring.viewer \
           --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/custom-metrics/sa/custom-metrics-stackdriver-adapter
         

  5. Define a PodMonitoring resource by placing the following configuration in a file named `podmonitoring.yaml`.
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: prom-example
         spec:
           selector:
             matchLabels:
               run: custom-metric-prometheus-sd
           endpoints:
           - port: 8080
             interval: 30s
         

  6. Deploy the new PodMonitoring resource:
         
         kubectl -n default apply -f podmonitoring.yaml
         

Within a couple of minutes, Managed Service for Prometheus processes the metrics scraped from the exporter and stores them in Cloud Monitoring using a long-form name. Prometheus metrics are stored with the following conventions:

     * The prefix `prometheus.googleapis.com`.
     * This suffix is usually one of `gauge`, `counter`, `summary`, or `histogram`, although untyped metrics might have the `unknown` or `unknown:counter` suffix. To verify the suffix, look up the metric in Cloud Monitoring by using Metrics Explorer.
  7. Update the deployed HPA to query the metric from Cloud Monitoring. The metric `foo` is ingested as `prometheus.googleapis.com/foo/gauge`. To make the metric queryable by the deployed HorizontalPodAutoscaler resource, you use the long-form name in the deployed HPA, but you have to modify it by replacing the all forward slashes (`/`) with the pipe character (`|`): `prometheus.googleapis.com|foo|gauge`. For more information, see the [Metrics available from Stackdriver section](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter#metrics-available-from-stackdriver) of the Custom Metrics Stackdriver Adapter repository.

     1. Update the deployed HPA by running the following command:
            
            kubectl edit hpa custom-metric-prometheus-sd
            

     2. Change the value of the `pods.metric.name` field from `foo` to `prometheus.googleapis.com|foo|gauge`. The `spec` section should look like the following:
            
            spec:
               maxReplicas: 5
               metrics:
               - pods:
                   metric:
                     name: prometheus.googleapis.com|foo|gauge
                   target:
                     averageValue: "20"
                     type: AverageValue
                 type: Pods
               minReplicas: 1
            

In this example, the HPA configuration looks for the average value of the metric `prometheus.googleapis.com/foo/gauge` to be `20`. Because the Deployment sets the value of the metric is `40`, the HPA controller increases the number of pods up to the value of the `maxReplicas` (`5`) field to try to reduce the average value of the metric across all pods to `20`.

The HPA query is scoped to the namespace and cluster in which the HPA resource is installed, so identical metrics in other clusters and namespaces don't affect your autoscaling.

  8. To watch the workload scale up, run the following command:
         
         kubectl get hpa custom-metric-prometheus-sd --watch
         

The value of the `REPLICAS` field changes from `1` to `5`.
         
         NAME                          REFERENCE                                TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
         custom-metric-prometheus-sd   Deployment/custom-metric-prometheus-sd   40/20          1         5         **5**          *
         

  9. To scale down the deployment, update the target metric value to be higher than the exported metric value. In this example, the Deployment sets the value of the `prometheus.googleapis.com/foo/gauge` metric to `40`. If you set the target value to a number that is higher than `40`, then the deployment will scale down.

For example, use `kubectl edit` to change the value of the `pods.target.averageValue` field in the HPA configuration from `20` to `100`.
         
         kubectl edit hpa custom-metric-prometheus-sd
         

Modify the spec section to match the following:
         
         spec:
           maxReplicas: 5
           metrics:
           - pods:
               metric:
                 name: prometheus.googleapis.com|foo|gauge
               target:
                 averageValue: "100"
                 type: AverageValue
           type: Pods
           minReplicas: 1
         

  10. To watch the workload scale down, run the following command:
         
         kubectl get hpa custom-metric-prometheus-sd --watch
         

The value of the `REPLICAS` field changes from `5` to `1`. By design, this happens more slowly than when scaling the number of pods up:
         
         NAME                          REFERENCE                                TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
         custom-metric-prometheus-sd   Deployment/custom-metric-prometheus-sd   40/100          1         5         **1**          *
         

  11. To clean up the deployed example, run the following commands:
         
         kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml
         kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/examples/prometheus-to-sd/custom-metrics-prometheus-sd.yaml
         kubectl delete podmonitoring/prom-example
         




For more information, see the [Prometheus example](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter/examples/prometheus-to-sd) in the Custom Metrics Stackdriver Adapter repository, or see [Scaling an application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps).

## Use the Prometheus Adapter

Existing prometheus-adapter configs can be used to autoscale with only a few changes. Configuring prometheus-adapter to scale using Managed Service for Prometheus has two additional restrictions compared to scaling using upstream Prometheus:

  * Queries must be routed through the Prometheus frontend UI proxy, just like when [querying Managed Service for Prometheus using the Prometheus API or UI](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui). For prometheus-adapter, you need to [edit the `prometheus-adapter` Deployment](https://github.com/kubernetes-sigs/prometheus-adapter/blob/7bdb7f14b922298df2de392d5450205467b32404/deploy/manifests/deployment.yaml#L34) to change the `prometheus-url` value as follows:
        
        --prometheus-url=http://frontend.NAMESPACE_NAME.svc:9090/
        

where NAMESPACE_NAME is the namespace where the frontend is deployed.

  * You cannot use a regular expression matcher (`=~` or `!~`) on a metric name in the `.seriesQuery` field of the rules config. Instead you must fully specify metric names. For some workarounds, see [PromQL compatibility](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql-differences#promql-metric-name-match).




As data can take slightly longer to be available within Managed Service for Prometheus compared to upstream Prometheus, configuring overly-eager autoscaling logic might cause unwanted behavior. Although there is no guarantee on data freshness, data is typically available to query 3-7 seconds after it is sent to Managed Service for Prometheus, excluding any network latency.

All queries issued by prometheus-adapter are global in scope. This means that if you have applications in two namespaces that emit identically named metrics, an HPA configuration using that metric scales using data from both applications. We recommend always using `namespace` or `cluster` filters in your PromQL to avoid scaling using incorrect data.

To set up an example HPA configuration using prometheus-adapter and managed collection, use the following steps:

  1. Set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) in your cluster.
  2. Deploy the [Prometheus frontend UI proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#promui-deploy) in your cluster. If you use Workload Identity Federation for GKE, you must also [configure and authorize a service account](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#gmp-wli-svcacct).
  3. Deploy the manifests in the [`examples/hpa/` directory within the prometheus-engine repo](https://github.com/GoogleCloudPlatform/prometheus-engine/tree/main/examples/hpa): 
     * `example-app.yaml`: An example deployment and service that emits metrics.
     * `pod-monitoring.yaml`: A resource that configures scraping the example metrics.
     * `hpa.yaml`: The HPA resource that configures scaling for your workload.
  4. Make sure `prometheus-adapter` is installed in your cluster. This can be done by deploying the [example install manifest](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/91fa0b34ecbb5094986d1739508a050934f7d434/examples/hpa/prometheus-adapter.yaml) to your cluster. This manifest is configured to:

     * Query a [frontend proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#promui-deploy) deployed in the `default` namespace.
     * Issue PromQL to calculate and return the `http_requests_per_second` metric from the example deployment.
**Note:** The `http_requests_per_second` metric won't be available until load is generated against the example application.
  5. Run the following commands, each in a separate terminal session:

     1. Generate HTTP load against the `prometheus-example-app` service: 
            
            kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://prometheus-example-app; done"

     2. Watch the horizontal pod autoscaler: 
            
            kubectl get hpa prometheus-example-app --watch

     3. Watch the workload scale up: 
            
            kubectl get po -lapp.kubernetes.io/name=prometheus-example-app --watch

  6. Stop HTTP load generation by using Ctrl+C and watch the workload scale back down.




## Troubleshooting

Custom Metrics Stackdriver Adapter uses resource definitions with the same names as those in the Prometheus Adapter, [prometheus-adapter](https://github.com/kubernetes-sigs/prometheus-adapter/). This overlap in names means that running more than one adapter in the same cluster [causes errors](https://github.com/kubernetes-sigs/custom-metrics-apiserver/issues/70).

Installing the Prometheus Adapter in a cluster that previously had the Custom Metrics Stackdriver Adapter installed might throw errors such as `FailedGetObjectMetric` due to colliding names. To resolve this, you might have to delete the `v1beta1.external.metrics.k8s.io`, `v1beta1.custom.metrics.k8s.io`, and `v1beta2.custom.metrics.k8s.io` apiservices previously registered by the Custom Metrics Adapter.

Troubleshooting tips:

  * Some Cloud Monitoring system metrics such as [Pub/Sub metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub) are delayed by 60 seconds or more. As Prometheus Adapter executes queries using the current timestamp, querying these metrics using the Prometheus Adapter might incorrectly result in no data. To query delayed metrics, use the [`offset` modifier in PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier) to change your query's time offset by the necessary amount.

  * To verify that the [frontend UI proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#promui-deploy) is working as intended and there are no issues with permissions, run the following command in a terminal:
        
        kubectl -n NAMESPACE_NAME port-forward svc/frontend 9090
        

Next, open another terminal and run the following command:
        
        curl --silent 'localhost:9090/api/v1/series?match%5B%5D=up'
        

When the frontend UI proxy is working properly, the response in the second terminal is similar to the following:
        
        curl --silent 'localhost:9090/api/v1/series?match%5B%5D=up' | jq .
        {
          "status": "success",
          "data": [
             ...
          ]
        }
        

If you receive a 403 error, then then frontend UI proxy isn't properly configured. For information about how to resolve a 403 error, see [configure and authorize a service account](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#gmp-wli-svcacct) guide.

  * To verify that the custom metrics apiserver is available, run the following command:
        
        kubectl get apiservices.apiregistration.k8s.io v1beta1.custom.metrics.k8s.io
        

When the apiserver is available, the response is similar to the following:
        
        $ kubectl get apiservices.apiregistration.k8s.io v1beta1.custom.metrics.k8s.io
        NAME                            SERVICE                         AVAILABLE   AGE
        v1beta1.custom.metrics.k8s.io   monitoring/prometheus-adapter   True        33m
        

  * To verify that your HPA is working as intended, run the following command:
        
        $ kubectl describe hpa prometheus-example-app
        Name:                                  prometheus-example-app
        Namespace:                             default
        Labels:                                
        Annotations:                           
        Reference:                             Deployment/prometheus-example-app
        Metrics:                               ( current / target )
        "http_requests_per_second" on pods:  11500m / 10
        Min replicas:                          1
        Max replicas:                          10
        Deployment pods:                       2 current / 2 desired
        Conditions:
        Type            Status  Reason              Message
        ----            ------  ------              -------
        AbleToScale     True    ReadyForNewScale    recommended size matches current size
        ScalingActive   True    ValidMetricFound    the HPA was able to successfully calculate a replica count from pods metric http_requests_per_second
        ScalingLimited  False   DesiredWithinRange  the desired count is within the acceptable range
        Events:
        Type     Reason               Age                   From                       Message
        ----     ------               ----                  ----                       -------
        Normal   SuccessfulRescale    47s                   horizontal-pod-autoscaler  New size: 2; reason: pods metric http_requests_per_second above target
        

When the response contains a statement like `FailedGetPodsMetric`, then the HPA failing. The following illustrates a response to the `describe` call when the HPA is failing:
        
        $ kubectl describe hpa prometheus-example-app
        Name:                                  prometheus-example-app
        Namespace:                             default
        Reference:                             Deployment/prometheus-example-app
        Metrics:                               ( current / target )
          "http_requests_per_second" on pods:   / 10
        Min replicas:                          1
        Max replicas:                          10
        Deployment pods:                       1 current / 1 desired
        Conditions:
          Type            Status  Reason               Message
          ----            ------  ------               -------
          AbleToScale     True    ReadyForNewScale     recommended size matches current size
          ScalingActive   False   FailedGetPodsMetric  the HPA was unable to compute the replica count: unable to get metric http_requests_per_second: unable to fetch metrics from custom metrics API: the server could not find the metric http_requests_per_second for pods
          ScalingLimited  False   DesiredWithinRange   the desired count is within the acceptable range
        Events:
          Type     Reason               Age                   From                       Message
          ----     ------               ----                  ----                       -------
          Warning  FailedGetPodsMetric  104s (x11 over 16m)   horizontal-pod-autoscaler  unable to get metric http_requests_per_second: unable to fetch metrics from custom metrics API: the server could not find the metric http_requests_per_second for pods
        

When the HPA is failing, make sure you are generating metrics with the `load-generator`. You can check the custom metrics api directly, with the command:
        
        kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/" | jq .
        

A successful output is similar to the following:
        
        $ kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/" | jq .
          {
          "kind": "APIResourceList",
          "apiVersion": "v1",
          "groupVersion": "custom.metrics.k8s.io/v1beta1",
          "resources": [
             {
                "name": "namespaces/http_requests_per_second",
                "singularName": "",
                "namespaced": false,
                "kind": "MetricValueList",
                "verbs": [
                "get"
                ]
             },
             {
                "name": "pods/http_requests_per_second",
                "singularName": "",
                "namespaced": true,
                "kind": "MetricValueList",
                "verbs": [
                "get"
                ]
             }
          ]
          }
        

If there are no metrics, there will be no data under `"resources"` in the output, for example:
        
        kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/" | jq .
        {
        "kind": "APIResourceList",
        "apiVersion": "v1",
        "groupVersion": "custom.metrics.k8s.io/v1beta1",
        "resources": []
        }
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
