---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu/
title: Configure autoscaling for LLM workloads on TPUs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:38.603326+00:00
---

# Configure autoscaling for LLM workloads on TPUs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Configure autoscaling for LLM workloads on TPUs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Configure autoscaling for your large language model (LLM) workloads on Google Kubernetes Engine (GKE) running on TPUs, using the [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) (HPA) and single-host [JetStream](https://github.com/google/JetStream). This helps you efficiently manage fluctuating LLM inference workloads, optimize resource utilization, and ensure consistent performance for your applications.

HPA automatically adjusts the number of pod replicas based on observed CPU utilization or other custom metrics. JetStream facilitates the deployment of LLMs, enabling effective scaling. For best practices on selecting metrics for autoscaling, see [Best practices for autoscaling LLM workloads with TPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Familiarize yourself with and complete the workflow in [Serve Gemma using TPUs on GKE with JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-tpu-jetstream). Make sure the PROMETHEUS_PORT argument is set in your JetStream deployment manifest.



## Autoscale using metrics

You can use the workload-specific performance metrics that are emitted by the JetStream inference server or TPU performance metrics to direct autoscaling for your Pods.

To set up autoscaling with metrics, follow these steps:

  1. **Export the metrics from the JetStream server to Cloud Monitoring**. You use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed), which simplifies deploying and configuring your Prometheus collector. Google Cloud Managed Service for Prometheus is enabled by default in your GKE cluster; you can also [enable it manually](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke).

The following example manifest shows how to set up your [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring) resource definitions to direct Google Cloud Managed Service for Prometheus to scrape metrics from your Pods at recurring intervals of 15 seconds:

If you need to scrape server metrics, use the following manifest. With server metrics, scrape intervals as frequent as 5 seconds are supported.
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: jetstream-podmonitoring
         spec:
           selector:
             matchLabels:
               app: maxengine-server
           endpoints:
           - interval: 15s
             path: "/"
             port: PROMETHEUS_PORT
           targetLabels:
             metadata:
             - pod
             - container
             - node
         

If you need to scrape TPU metrics, use the following manifest. With system metrics, scrape intervals as frequent as 15 seconds are supported.
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: tpu-metrics-exporter
           namespace: kube-system
           labels:
             k8s-app: tpu-device-plugin
         spec:
           endpoints:
             - port: 2112
               interval: 15s
           selector:
             matchLabels:
               k8s-app: tpu-device-plugin
         

  2. **Install a Metrics Adapter.** This adapter makes the server metrics that you exported to Monitoring visible to the HPA controller. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation.

     * If you want JetStream to scale with individual metrics, use the [Custom Metrics Stackdriver Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter).
     * If you want JetStream to scale with the value of an expression composed of multiple distinct metrics, use the third-party [Prometheus Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter).

### Custom Metrics Stackdriver Adapter

The Custom Metrics Stackdriver Adapter supports querying metrics from Google Cloud Managed Service for Prometheus, starting with [version v0.13.1 of the adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/releases/tag/cm-sd-adapter-v0.13.1).

To install the Custom Metrics Stackdriver Adapter, do the following:

     1. Set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) in your cluster.

     2. Install the Custom Metrics Stackdriver Adapter in your cluster.
            
            kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml
            

     3. If you have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled on your Kubernetes cluster and you use Workload Identity Federation for GKE, you must also grant the Monitoring Viewer role to the service account the adapter runs under. Replace `PROJECT_ID` with your project ID.
    
    export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format 'get(projectNumber)')
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
      --role roles/monitoring.viewer \
      --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/custom-metrics/sa/custom-metrics-stackdriver-adapter
    

### Prometheus Adapter

Be aware of these considerations when using `prometheus-adapter` to scale using Google Cloud Managed Service for Prometheus:

     * Route queries through the Prometheus frontend UI proxy, just like when [querying Google Cloud Managed Service for Prometheus using the Prometheus API or UI](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui). This frontend is installed in a later step.
     * By default, the [`prometheus-url`](https://github.com/kubernetes-sigs/prometheus-adapter/blob/7bdb7f14b922298df2de392d5450205467b32404/deploy/manifests/deployment.yaml#L34) argument of the `prometheus-adapter` Deployment is set to `--prometheus-url=http://frontend.default.svc:9090/`, where `default` is the namespace where you deployed the frontend. If you deployed the frontend in another namespace, configure this argument accordingly.
     * In the `.seriesQuery` field of the rules config, you can't use a regular expression (regex) matcher on a metric name. Instead, fully specify metric names.

As data can take slightly longer to be available within Google Cloud Managed Service for Prometheus compared to upstream Prometheus, configuring overly eager autoscaling logic can cause unwanted behavior. Although there is no guarantee on data freshness, data is typically available to query 3-7 seconds after it is sent to Google Cloud Managed Service for Prometheus, excluding any network latency.

All queries issued by `prometheus-adapter` are global in scope. This means that if you have applications in two namespaces that emit identically named metrics, an HPA configuration using that metric scales using data from both applications. To avoid scaling using incorrect data, always use `namespace` or `cluster` filters in your PromQL.

To set up an example HPA configuration using `prometheus-adapter` and managed collection, follow these steps:

     1. Set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) in your cluster.
     2. Deploy the [Prometheus frontend UI proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#promui-deploy) in your cluster. Create the following manifest named `prometheus-frontend.yaml`:
            
            apiVersion: apps/v1
              kind: Deployment
              metadata:
                name: frontend
              spec:
                replicas: 2
                selector:
                  matchLabels:
                    app: frontend
                template:
                  metadata:
                    labels:
                      app: frontend
                  spec:
                    automountServiceAccountToken: true
                    affinity:
                      nodeAffinity:
                        requiredDuringSchedulingIgnoredDuringExecution:
                          nodeSelectorTerms:
                          - matchExpressions:
                            - key: kubernetes.io/arch
                              operator: In
                              values:
                              - arm64
                              - amd64
                            - key: kubernetes.io/os
                              operator: In
                              values:
                              - linux
                    containers:
                    - name: frontend
                      image: gke.gcr.io/prometheus-engine/frontend:v0.8.0-gke.4
                      args:
                      - "--web.listen-address=:9090"
                      - "--query.project-id=PROJECT_ID"
                      ports:
                      - name: web
                        containerPort: 9090
                      readinessProbe:
                        httpGet:
                          path: /-/ready
                          port: web
                      securityContext:
                        allowPrivilegeEscalation: false
                        capabilities:
                          drop:
                          - all
                        privileged: false
                        runAsGroup: 1000
                        runAsNonRoot: true
                        runAsUser: 1000
                      livenessProbe:
                        httpGet:
                          path: /-/healthy
                          port: web
              ---
              apiVersion: v1
              kind: Service
              metadata:
                name: prometheus
              spec:
                clusterIP: None
                selector:
                  app: frontend
                ports:
                - name: web
                  port: 9090
            

Then, apply the manifest:
            
            kubectl apply -f prometheus-frontend.yaml
            

     3. Ensure `prometheus-adapter` is installed in your cluster by installing the `prometheus-community/prometheus-adapter` helm chart. Create the following `values.yaml` file:
            
            rules:
              default: false
              external:
              - seriesQuery: 'jetstream_prefill_backlog_size'
                resources:
                  template: <<.Resource>>
                name:
                  matches: ""
                  as: "jetstream_prefill_backlog_size"
                metricsQuery: avg(<<.Series>>{<<.LabelMatchers>>,cluster="CLUSTER_NAME"})
              - seriesQuery: 'jetstream_slots_used_percentage'
                resources:
                  template: <<.Resource>>
                name:
                  matches: ""
                  as: "jetstream_slots_used_percentage"
                metricsQuery: avg(<<.Series>>{<<.LabelMatchers>>,cluster="CLUSTER_NAME"})
              - seriesQuery: 'memory_used'
                resources:
                  template: <<.Resource>>
                name:
                  matches: ""
                  as: "memory_used_percentage"
                metricsQuery: avg(memory_used{cluster="CLUSTER_NAME",exported_namespace="default",container="jetstream-http"}) / avg(memory_total{cluster="CLUSTER_NAME",exported_namespace="default",container="jetstream-http"})
            

Then, use this file as the values file for deploying your helm chart:
            
            helm repo add prometheus-community https://prometheus-community.github.io/helm-charts && helm repo update && helm install example-release prometheus-community/prometheus-adapter -f values.yaml
            

If you use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity), you also need to [configure and authorize a service account](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#gmp-wli-svcacct) by running the following commands:

     1. Create a Kubernetes ServiceAccount:
            
            kubectl create sa prom-frontend-sa
            

     2. Grant the Kubernetes ServiceAccount the Monitoring Viewer role (`roles/monitoring.viewer`) on the project:
            
            export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format 'get(projectNumber)')
            gcloud projects add-iam-policy-binding projects/PROJECT_ID \
              --role=roles/monitoring.viewer \
              --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/default/sa/prom-frontend-sa \
              --condition=None
            

Replace `PROJECT_ID` with your project ID.

     3. Configure the `frontend` Deployment to use the `prom-frontend-sa` ServiceAccount:
            
            kubectl set serviceaccount deployment frontend prom-frontend-sa
            

  3. **Set up the metric-based HPA resource.** Deploy an HPA resource that is based on your preferred server metric. For more details, see [Horizontal pod autoscaling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa) in the Google Cloud Managed Service for Prometheus documentation. The specific HPA configuration depends on the type of metric (server or TPU) and which metric adapter is installed.

A few values are required across all HPA configurations and must be set in order to create an HPA resource:

     * MIN_REPLICAS: The minimum number of JetStream pod replicas allowed. If not modifying the JetStream deployment manifest from the [Deploy JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-tpu-jetstream#deploy-jetstream) step, we recommend setting this to 1.
     * MAX_REPLICAS: The maximum number of JetStream pod replicas allowed. The example JetStream deployment requires 8 chips per replica and the node pool contains 16 chips. If you want to keep scale up latency low, set this to 2. Larger values trigger the Cluster Autoscaler to create new nodes in the node pool, thus increasing scale up latency.
     * TARGET: The targeted average for this metric across all JetStream instances. See the [Kubernetes Documentation for Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) for more information about how replica count is determined from this value.

### Custom Metrics Stackdriver Adapter

Custom Metrics Stackdriver Adapter supports scaling your workload with the average value of individual metric queries from Google Cloud Managed Service for Prometheus across all Pods. When using Custom Metrics Stackdriver Adapter, we advise scaling with the `jetstream_prefill_backlog_size` and `jetstream_slots_used_percentage` server metrics and the `memory_used` TPU metric.

To create an HPA manifest for scaling with server metrics, create the following `hpa.yaml` file:
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: jetstream-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: maxengine-server
      minReplicas: MIN_REPLICAS
      maxReplicas: MAX_REPLICAS
      metrics:
      - type: Pods
        pods:
          metric:
            name: prometheus.googleapis.com|jetstream_METRIC|gauge
          target:
            type: AverageValue
            averageValue: TARGET
    

When using the Custom Metrics Stackdriver Adapter with TPU metrics, we recommend only using the `kubernetes.io|node|accelerator|memory_used` metric for scaling. To create an HPA manifest for scaling with this metric, create the following `hpa.yaml` file:
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: jetstream-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: maxengine-server
      minReplicas: MIN_REPLICAS
      maxReplicas: MAX_REPLICAS
      metrics:
      - type: External
        external:
          metric:
            name: prometheus.googleapis.com|memory_used|gauge
            selector:
              matchLabels:
                metric.labels.container: jetstream-http
                metric.labels.exported_namespace: default
          target:
            type: AverageValue
            averageValue: TARGET
    

### Prometheus Adapter

Prometheus Adapter supports scaling your workload with the value of PromQL queries from Google Cloud Managed Service for Prometheus. Earlier, you defined the `jetstream_prefill_backlog_size` and `jetstream_slots_used_percentage` server metrics that represent the average value across all Pods.

To create an HPA manifest for scaling with server metrics, create the following `hpa.yaml` file:
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: jetstream-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: maxengine-server
      minReplicas: MIN_REPLICAS
      maxReplicas: MAX_REPLICAS
      metrics:
      - type: External
        external:
          metric:
            name: jetstream_METRIC
          target:
            type: AverageValue
            averageValue: TARGET
    

To create an HPA manifest for scaling with TPU metrics, we recommend only using the `memory_used_percentage` defined in the prometheus-adapter helm values file. `memory_used_percentage` is the name given to the following PromQL query which reflects the current average memory used across all accelerators:
    
    avg(kubernetes_io:node_accelerator_memory_used{cluster_name="CLUSTER_NAME"}) / avg(kubernetes_io:node_accelerator_memory_total{cluster_name="CLUSTER_NAME"})
    

To create an HPA manifest for scaling with `memory_used_percentage`, create the following `hpa.yaml` file:
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: jetstream-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: maxengine-server
      minReplicas: MIN_REPLICAS
      maxReplicas: MAX_REPLICAS
      metrics:
      - type: External
        external:
          metric:
            name: memory_used_percentage
          target:
            type: AverageValue
            averageValue: TARGET
    




## Scale using multiple metrics

You can also configure scaling based on multiple metrics. To learn about how replica count is determined using multiple metrics, refer to the [Kubernetes documentation on auto-scaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-multiple-metrics). To build this type of HPA manifest, collect all entries from the `spec.metrics` field of each HPA resource into a single HPA resource. The following snippet shows an example of how you can bundle the HPA resources:
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: jetstream-hpa-multiple-metrics
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: maxengine-server
      minReplicas: MIN_REPLICAS
      maxReplicas: MAX_REPLICAS
      metrics:
      - type: Pods
        pods:
          metric:
            name: jetstream_METRIC
          target:
            type: AverageValue
          averageValue: JETSTREAM_METRIC_TARGET
      - type: External
        external:
          metric:
            name: memory_used_percentage
          target:
            type: AverageValue
          averageValue: EXTERNAL_METRIC_TARGET
    

## Monitor and test autoscaling

You can observe how your JetStream workloads scale based on your HPA configuration.

To observe the replica count in real-time, run the following command:
    
    
    kubectl get hpa --watch
    

The output from this command should be similar to the following:
    
    
    NAME            REFERENCE                     TARGETS      MINPODS   MAXPODS   REPLICAS   AGE
    jetstream-hpa   Deployment/maxengine-server   0/10 (avg)   1         2         1          1m
    

To test your HPA's ability to scale, use the following command which sends a burst of 100 requests to the model endpoint. This will exhaust the available decode slots and cause a backlog of requests on the prefill queue, triggering the HPA to increase the size of the model deployment.
    
    
    seq 100 | xargs -P 100 -n 1 curl --request POST --header "Content-type: application/json" -s localhost:8000/generate --data '{ "prompt": "Can you provide a comprehensive and detailed overview of the history and development of artificial intelligence.", "max_tokens": 200 }'
    

**Note:** If you are using a private cluster, you need to [install an internal firewall rule](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#control-plane-firewall) on port `6443` from the control plane to your nodes.

## What's next

  * Learn how to [autoscale based on custom or external metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics).
  * Learn more about [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) from the open source Kubernetes documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
