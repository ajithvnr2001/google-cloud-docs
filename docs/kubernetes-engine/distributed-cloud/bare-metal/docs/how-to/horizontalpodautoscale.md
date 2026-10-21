---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/horizontalpodautoscale/
title: Configure horizontal pod autoscaling \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:53.999721+00:00
---

# Configure horizontal pod autoscaling  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/horizontalpodautoscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure horizontal pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up horizontal pod autoscaling for existing stateless workloads running in your cluster. Horizontal pod autoscaling automatically adjusts the number of running Pods (replicas) for an application based on real-time demand, removing Pods when load decreases and adding Pods when load increases. This scaling in and out is crucial for ensuring application availability, efficient resource use, and cost savings by matching capacity precisely to user traffic without manual intervention. As your container workload requirements evolve, pod autoscaling eliminates the need for operators to constantly monitor performance and manually adjust pod counts.

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Scale a deployment

Use the scaling functionality of Kubernetes to appropriately scale the amount of pods running in your deployment.

### Autoscale the pods of a deployment

Kubernetes offers autoscaling to remove the need to manually update your deployment when demand evolves. Complete the following steps to autoscale the pods of your deployment:

  1. To ensure the horizontal pod autoscaler can appropriately measure the CPU percentage, set the [CPU resource request](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-resource-metrics) on your deployment.

  2. Set the horizontal pod autoscaler in your deployment:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
             -n NAMESPACE \
             autoscale deployment DEPLOYMENT_NAME \
             --cpu-percent=CPU_PERCENT \
             --min=MIN_NUMBER_REPLICAS \
             --max=MAX_NUMBER_REPLICAS
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

     * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

     * `DEPLOYMENT_NAME`: the name of the deployment to autoscale.

     * `CPU_PERCENT`: the target average CPU utilization to request, represented as a percentage, over all the pods.

     * `MIN_NUMBER_REPLICAS`: the lower limit for the number of pods the autoscaler can provision.

     * `MAX_NUMBER_REPLICAS`: the upper limit for the number of pods the autoscaler can provision.

  3. Check the current status of the horizontal pod autoscaler:
         
         kubectl get hpa
         

The output is similar to the following:
         
         NAME              REFERENCE                          TARGET    MINPODS   MAXPODS   REPLICAS   AGE
         DEPLOYMENT_NAME   Deployment/DEPLOYMENT_NAME/scale   0% / 50%  1         10        1          18s
         




### Manually scale the pods of a deployment

If you prefer to manually scale a deployment, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        -n NAMESPACE \
        scale deployment DEPLOYMENT_NAME \
        --replicas NUMBER_OF_REPLICAS
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `DEPLOYMENT_NAME`: the name of the deployment in which to autoscale.

  * `DEPLOYMENT_NAME`: the number of replicated `Pod` objects in the deployment.




## Use custom metrics from Prometheus for autoscaling

Horizontal pod autoscaling uses standard resource metrics like CPU and memory utilization by default. Standard metrics work for general scaling, but aren't useful for specialized application loads.

When you use horizontal pod autoscaling with custom metrics from Prometheus, you can scale workloads based on application-specific metrics, like HTTP request rates, queue depth, and processing latency. Your cluster can respond more accurately to real-world demand by leveraging the rich data already collected by your Prometheus monitoring stack.

### Prerequisites for using Prometheus with horizontal pod autoscaling

Before enabling the feature, the following conditions must be met:

  * Existing Prometheus server: A Prometheus server must already be deployed and network-accessible from within the cluster (the HPA controller doesn't manage the Prometheus instance itself). For more information, see [How to deploy and configure the Prometheus Operator in Kubernetes](https://grafana.com/blog/how-to-monitor-kubernetes-clusters-with-the-prometheus-operator/).

  * Administrative permissions: You must have the necessary permissions to modify the Cluster custom resource.

  * No API conflicts: A preflight check verifies that no other component has already registered an APIService for `custom.metrics.k8s.io`. If a conflict exists, the adapter can't be enabled.




### Enable and configure Prometheus

The process involves defining metric rules and updating the cluster configuration:

  1. Create one or more metric rule ConfigMaps.

Define the PromQL-based rules for your custom metrics in one or more ConfigMaps within the target cluster namespace. The controller watches these ConfigMaps, merges them, and automatically applies them to the adapter.

For more information about defining rules, see [Metrics Discovery and Presentation Configuration](https://github.com/kubernetes-sigs/prometheus-adapter/blob/master/docs/config.md) in [kubernetes-sigs/prometheus-adapter](https://github.com/kubernetes-sigs/prometheus-adapter).

The following sample shows a ConfigMap with rules defined for `http_requests_per_second` in the `data` field:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: my-app-rules
           namespace: <cluster-namespace>
         data:
           config.yaml: |
             rules:
             - seriesQuery: 'http_requests_total'
               resources:
                 overrides:
                   namespace_name: {resource: "namespace"}
                   pod_name: {resource: "pod"}
               name:
                 matches: "^(.*)_total$"
                 as: "${1}_per_second"
               metricsQuery: 'sum(rate(<<.Series>>{<<.LabelMatchers>>}[5m])) by (<<.GroupBy>>)'
         

  2. If your Prometheus server requires authentication, such as mutual transport layer security (mTLS), create a Kubernetes Secret in the kubeconfig format containing the necessary credentials.

The following example shows a Secret that supports basic authentication:
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: prometheus-auth-secret
           namespace: <cluster-namespace>
           annotations:**    baremetal.cluster.gke.io/mark-source: "true"**
         type: Opaque
         stringData:
           config: authentication-credentials
         

  3. Update the Cluster custom resource:

     1. Add the `preview.baremetal.cluster.gke.io/metrics-adapter: "true"` annotation to the `metadata` for the Cluster custom resource.

     2. Add the [`spec.metricsAdapter`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/horizontalpodautoscale/) section to define the Prometheus URL and reference your rule ConfigMaps.
            
            apiVersion: baremetal.cluster.gke.io/v1
            kind: Cluster
            metadata:
              name: <cluster-name>
              namespace: <cluster-namespace>**  annotations:
                preview.baremetal.cluster.gke.io/metrics-adapter: "true"**
            spec:
              # ... other existing cluster configurations ...**  metricsAdapter:
                prometheus:
                  url: "http://prometheus-k8s.monitoring.svc.cluster.local:9090"
                  orgID: "production-environment"
                  auth:
                    configSecretRef:
                      name: prometheus-auth-secret
                      key: config # This is the key within the Secret's 'data' field
                rules:
                  configMapKeyRefs:
                    - name: my-app-rules
                      key: config.yaml** # This is the key within the ConfigMap's 'data' field
                    # - name: base-system-rules
                    #   key: config.yaml
            

If your Prometheus instance doesn't require authentication, you can omit the `metricsAdapter.prometheus.auth` section from the Cluster spec.

  4. Apply the updated Cluster custom resource.

The controller automatically deploys the Prometheus Adapter into the `kube-system` namespace.

  5. Use the custom metrics in for horizontal pod autoscaling by creating a HorizontalPodAutoscaler resource that targets the custom metrics defined in the ConfigMaps `rules` fields.

The ConfigMap sample from an earlier step defined a `http_requests_per_second` custom metric. To use this metric, the HorizontalPodAutoscaler resource should look similar to the following example:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: <name>
           namespace: <namespace>
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: <workload-name>
           minReplicas: 1
           maxReplicas: 10
           metrics:
           - type: Pods
             pods:
               metric:
                 name: http_requests_per_second
               target:
                 type: AverageValue
                 averageValue: 10
         




### Disable Prometheus

To disable the use of Prometheus with horizontal pod autoscaling, remove the `spec.metricsAdapter` section from the Cluster custom resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
