---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/verticalpodautoscale/
title: Configure vertical Pod autoscaling \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:42.405935+00:00
---

# Configure vertical Pod autoscaling  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/verticalpodautoscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure vertical Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

Vertical Pod autoscaling automates setting CPU and memory resource requests and limits for containers within Kubernetes Pods. Vertical Pod autoscaling analyzes historical and current resource usage to provide recommendations, which it can either display or automatically apply by updating Pods. This feature improves stability and cost efficiency by right-sizing resource allocations.

## Before you begin

Before you configure Vertical Pod Autoscaling, ensure you meet the following prerequisites:

  * You have a running bare metal cluster.
  * You have `kubectl` access to the cluster.
  * Metrics Server is available in the cluster. Bare metal clusters include Metrics Server by default.



## Enable vertical Pod autoscaling

Enable vertical Pod autoscaling on your bare metal cluster by configuring the cluster specification:

  1. Modify the `spec` of the Cluster custom resource to include the `verticalPodAutoscaling` field and specify the `enableUpdater` and `enableMemorySaver` modes:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: cluster1
           namespace: cluster-cluster1
           annotations:
             preview.baremetal.cluster.gke.io/vertical-pod-autoscaler: enable
         spec:
           # ... other cluster spec fields**  verticalPodAutoscaling:
             enableUpdater: true       # Set to true for automated updates
             enableMemorySaver: true   # Set to true to reduce recommender memory usage**
         

  2. If you modified the cluster configuration file, apply the changes using the following command:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.

     * `KUBECONFIG`: the path of your cluster kubeconfig file.




## Create a `VerticalPodAutoscaler` custom resource

After enabling vertical Pod autoscaling on your cluster, define a `VerticalPodAutoscaler` custom resource to target specific workloads:

  1. Define a `VerticalPodAutoscaler` resource in the same namespace as the target workload.

This custom resource specifies which Pods it targets using `targetRef` and any resource policies.
         
         apiVersion: "autoscaling.k8s.io/v1"
         kind: VerticalPodAutoscaler
         metadata:
           name: hamster-vpa
         spec:
           targetRef:
             apiVersion: "apps/v1"
             kind: Deployment
             name: hamster
           resourcePolicy:
             containerPolicies:
               -   containerName: '*'
                 minAllowed:
                   cpu: 100m
                   memory: 50Mi
                 maxAllowed:
                   cpu: 1
                   memory: 500Mi
                 controlledResources: ["cpu", "memory"]
         

  2. Apply the `VerticalPodAutoscaler` manifest using the following command:
         
         kubectl apply -f VPA_MANIFEST \
             --kubeconfig KUBECONFIG
         

Replace the following:

     * `VPA_MANIFEST`: the path of the `VerticalPodAutoscaler` manifest file.

     * `KUBECONFIG`: the path of the cluster kubeconfig file.




## Understand vertical Pod autoscaling modes

Vertical Pod autoscaling operates in different modes that control how it applies resource recommendations.

### Recommendation mode

In recommendation mode, vertical Pod autoscaling installs the recommender component. This component analyzes resource usage and publishes recommended values for CPU and memory requests and limits in the status section of the `VerticalPodAutoscaler` custom resources you create.

To view resource requests and limits recommendations, use the following command:
    
    
    kubectl describe vpa VPA_NAME \
        --kubeconfig KUBECONFIG \
        -n CLUSTER_NAMESPACE
    
    
    
    Replace the following:
    
    *   `VPA_NAME`: the name of the `VerticalPodAutoscaler`
        that's targeting the workloads for which you are considering resource
        adjustments.
    
    *   `KUBECONFIG`: the path of the cluster kubeconfig
        file.
    
    *   `CLUSTER_NAMESPACE`: the name of the cluster that's
        running vertical Pod autoscaling.
    

The response should contain a `Status` section that's similar to the following sample:
    
    
    Status:
      Conditions:
        Last Transition Time:  2025-08-04T23:53:32Z
        Status:                True
        Type:                  RecommendationProvided
      Recommendation:
        Container Recommendations:
          Container Name:  hamster
          Lower Bound:
            Cpu:     100m
            Memory:  262144k
          Target:
            Cpu:     587m
            Memory:  262144k
          Uncapped Target:
            Cpu:     587m
            Memory:  262144k
          Upper Bound:
            Cpu:     1
            Memory:  500Mi
    

Pods aren't automatically updated in this mode. Use these recommendations to manually update your Pod configurations. This is the default behavior if [`enableUpdater`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#verticalpodautoscaling-enableupdater) isn't set or is `false`.

### Automated update mode

When you set [`enableUpdater`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#verticalpodautoscaling-enableupdater) [`enableUpdater`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#verticalpodautoscaling-enableupdater) to `true`, bare metal lifecycle controllers deploy the vertical Pod autoscaling updater and admission controller components in addition to the recommender. The updater monitors for Pods whose current resource requests deviate significantly from the recommendations.

The update policy in the `VerticalPodAutoscaler` resource specifies how the updater applies the recommendations. By default, the update mode is `Auto`, which dictates that the updater assigns updated resource settings on Pod creation. The following `VerticalPodAutoscaler` sample how you set the update mode to `Initial`:
    
    
    apiVersion: "autoscaling.k8s.io/v1"
    kind: VerticalPodAutoscaler
    metadata:
      name: hamster-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: hamster
      resourcePolicy:**  updatePolicy:
        updateMode: "Initial"**
        ...
    

The updater supports the following five modes:

  * `Auto`: The updater evicts the Pod. The admission controller intercepts the creation request for the new Pod and modifies it to use the recommended CPU and memory values provided by the recommender. Updating resources requires recreating the Pod, which can cause disruptions. Use [Pod Disruption Budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/), which the updater honors, to manage the eviction process. This mode equivalent to `Recreate`.

  * `Recreate`: The updater evicts Pods and assigns recommended resource requests and limits when the Pod is recreated.

  * `InPlaceOrRecreate`(alpha): The updater attempts best-effort in-place updates, but may fall back to recreating the Pod if in-place updates aren't possible. For more information, see the [in-place pod resize](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/) documentation.

  * `Initial`: The updater only assigns resource requests on Pod creation and never changes them later.

  * `Off`: The updater doesn't automatically change the resource requirements of the Pods. The recommendations are calculated and can be inspected in the `VerticalPodAutoscaler` object.




For more information about the `VerticalPodAutoscaler` custom resource, use `kubectl` to retrieve the `verticalpodautoscalercheckpoints.autoscaling.k8s.io` custom resource definition that is installed on the version 1.33.0 or later cluster.

The following sample shows how resource recommendations might appear in the `Status` section for the `hamster` container. The sample also shows an example of a Pod eviction event, which occurs when the updater evicts a Pod prior to automatically assigning the recommended resource configuration to the recreated Pod:
    
    
    Spec:
      Resource Policy:
        Container Policies:
          Container Name:  *
          Controlled Resources:
            cpu
            memory
          Max Allowed:
            Cpu:     1
            Memory:  500Mi
          Min Allowed:
            Cpu:     100m
            Memory:  50Mi
      Target Ref:
        API Version:  apps/v1
        Kind:         Deployment
        Name:         hamster
      Update Policy:
        Update Mode:  Auto
    Status:
      Conditions:
        Last Transition Time:  2025-08-04T23:53:32Z
        Status:                True
        Type:                  RecommendationProvided
      Recommendation:
        Container Recommendations:
          Container Name:  hamster
          Lower Bound:
            Cpu:     100m
            Memory:  262144k
          Target:
            Cpu:     587m
            Memory:  262144k
          Uncapped Target:
            Cpu:     587m
            Memory:  262144k
          Upper Bound:
            Cpu:     1
            Memory:  500Mi
    Events:
      Type    Reason      Age   From         Message
      ----    ------      ----  ----         -------
      Normal  EvictedPod  49s   vpa-updater  VPA Updater evicted Pod hamster-7cb59fb657-lkrk4 to apply resource recommendation.
    

### Memory saver mode

Memory saver mode reduces the memory footprint of the vertical Pod autoscaling recommender component. When you set [`enableMemorySaver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#verticalpodautoscaling-enablememorysaver) to `true`, the recommender only tracks and computes aggregations for Pods that have a matching `VerticalPodAutoscaler` custom resource.

The trade-off is that when you create a new `VerticalPodAutoscaler` custom resource for an existing workload, the recommender takes some time (up to 24 hours) to gather sufficient history to provide accurate recommendations. This mode is `false` by default for most cluster types, but defaults to `true` for edge clusters.

## Use Prometheus as a persistent history provider

By default, the recommender component maintains the resource consumption history of the workloads running on the cluster in memory, and, periodically, saves its state to a `VerticalPodAutoscalerCheckpoint` custom resource in etcd to provide resilience against restarts.

Starting with Google Distributed Cloud version 1.34, you can use your own instance of Prometheus as a persistent history provider for resource consumption data, namely CPU and memory usage metrics. When this integration is enabled, the recommender can query the Prometheus server upon startup or restart to retrieve long-term historical resource usage data for all managed Pods. Retrieving this data allows the recommender to immediately build its internal state with a rich dataset, leading to more informed and accurate recommendations from the start.

Using Prometheus as a persistent history provider offers the following advantages:

  * **Optimizing resource utilization:** generates well-informed and accurate recommendations as soon as it starts so you can optimize cluster resource utilization.

  * **Preventing Out Of Memory (OOM) errors:** Prometheus eliminates the need to store the recommender's internal state in `VerticalPodAutoscalerCheckpoint` custom resources (CRs) making ETCD memory utilization more efficient. When the recommender component restarts, it loses in-memory historical data. When you use Prometheus as a history provider, the recommender fetches historical metrics from Prometheus on restart, which eliminates the need for the `VerticalPodAutoscalerCheckpoint` CR and saves ETCD memory.




You can enable and disable the use of Prometheus as a persistent history provider at any time.

### Prerequisites for using Prometheus with vertical Pod autoscaling

To use your own Prometheus instance as a history provider for vertical Pod autoscaling, you must configure it to scrape the necessary metrics, which involves the following steps:

  1. If needed, deploy the Prometheus Operator in the cluster for which you want to use it as a persistent history provider for vertical Pod autoscaling. For more information, see [How to deploy and configure the Prometheus Operator in Kubernetes](https://grafana.com/blog/how-to-monitor-kubernetes-clusters-with-the-prometheus-operator/).

  2. Configure permissions for scraping metrics.

To allow Prometheus to scrape metrics from cAdvisor using a configuration file, you must grant additional permissions to the service account that the Prometheus server uses. Create or update a `ClusterRole` containing these rules and ensure it's bound to the correct Prometheus service account using a `ClusterRoleBinding`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
            name: prometheus-role
            labels:
               app: prometheus-server
         rules:
            - apiGroups: [""]
              resources:
                - nodes
              verbs:
                - get
                - list
                - watch
            - apiGroups: [""]
              resources:
                - nodes/proxy
                - nodes/metrics
              verbs:
                - get
             ---
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: prometheus-binding
           labels:
             app: prometheus-server
         subjects:
           - kind: ServiceAccount
             name: prometheus-server        # Service account being used by prometheus
             namespace: prometheus          # Service account's namespace
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: prometheus-role            # Name of the ClusterRole created above
         

  3. Update the Prometheus configuration file to scrape the following metrics from cAdvisor:

     * `container_cpu_usage_seconds_total`
     * `container_memory_working_set_bytes`

The following lines define the scrape details for the cAdvisor metrics:
    
    - job_name: 'kubernetes-cadvisor'
      scheme: https
      tls_config:
        ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
      bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      kubernetes_sd_configs:
        - role: node
      relabel_configs:
        - action: labelmap
          regex: __meta_kubernetes_node_label_(.+)
        - target_label: __address__
          replacement: kubernetes.default.svc:443
        - source_labels: [__meta_kubernetes_node_name]
          regex: (.+)
          target_label: __metrics_path__
          replacement: /api/v1/nodes/${1}/proxy/metrics/cadvisor
    
      metric_relabel_configs:
      # Keep only the metrics VPA uses to save disk space
        - source_labels: [__name__]
          regex: (container_cpu_usage_seconds_total|container_memory_working_set_bytes)
          action: keep
    

  4. Update the Prometheus configuration file to scrape the following metric from the `kube-state-metrics` Service:

     * `kube_pod_labels`
     1. Deploy a `kube-state-metrics` Service on your cluster.

**Note:** Although a `kube-state-metrics` Service is installed by default on bare metal clusters, it doesn't expose the needed `kube_pod_labels` metric.

You can use the following Helm commands to install the new Service:
            
            helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
            helm repo update
            

     2. Create a `ksm-values.yaml` file with the following content:
            
            fullnameOverride: vpa-kube-state-metrics
            metricAllowlist:
              - kube_pod_labels
            metricLabelsAllowlist:
              - "pods=[*]"
            

     3. Install a Helm chart based on the values file from the preceding step:
            
            helm install vpa-ksm prometheus-community/kube-state-metrics \
                -f ksm-values.yaml --namespace kube-system
            

     4. Add the following lines to the Prometheus configuration file to scrape the `kube_pod_labels` metric from the installed `kube-state-metrics` Service:
            
            - job_name: 'kube-state-metrics'
              static_configs:
                - targets: ['vpa-kube-state-metrics.kube-system.svc.cluster.local:8080']
              metric_relabel_configs:
                - source_labels: [ __name__ ]
                  regex: 'kube_pod_labels'
                  action: keep
            




### Enable and use Prometheus

Vertical Pod autoscaling supports both basic authentication and bearer token-based authentication for connecting to Prometheus. When using authentication, you need to create a `Secret` containing the necessary credentials in the cluster namespace. The controller forwards this Secret to the target cluster and mounts it as a volume or environment variable in the recommender Pod. You can also use Prometheus without authentication.

To enable and use your own Prometheus instance with vertical Pod autoscaling, you need to configure the `verticalPodAutoscaling` section in your cluster specification with details for connecting to your Prometheus instance.

Here's an example of the configuration in the cluster spec for use with a bearer token:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
      annotations:
        preview.baremetal.cluster.gke.io/vertical-pod-autoscaler: enable
    spec:
      # ... other existing cluster configurations ...
      verticalPodAutoscaling:
        # ... other vertical Pod autoscaling configurations ...
        # Add this new section to configure the vpa to use prometheus using bearer token authentication as history provider**    prometheus:
          url: "http://prometheus.prometheus.monitoring.svc.cluster.local:9090"
          auth:
            bearerTokenAuth:
                name: prom-bearer-creds
                key: bearertoken**
    

To enable Prometheus for use with vertical Pod autoscaling:

  1. Ensure that your Prometheus instance is set up to scrape required metrics as outlined in Prerequisites for using Prometheus with vertical Pod autoscaling.

  2. Update the Cluster custom resource `spec` so that the [`verticalPodAutoscaling.prometheus`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#verticalpodautoscaling-prometheus) field specifies the connection settings for your Prometheus server.

  3. Add the `url` to the `prometheus` section and set it to the fully qualified domain name (FQDN) for connecting to Prometheus from within the cluster:
         
         spec:
           # ... other existing cluster configurations ...
           verticalPodAutoscaling:
             # ... other vpa configurations ...
             # Add this new section to configure the vpa to use prometheus as history provider
             prometheus:
               # Required: The URL of the Prometheus server**      url: "http://prometheus.prometheus.svc.cluster.local:9090"**
         

  4. Specify the connection details:

Vertical Pod autoscaling supports the following three connection methods:

     * No authentication
     * Basic (username, password) authentication
     * Bearer token authentication

###  No authentication 

If your Prometheus instance doesn't require authentication, you're done. The `prometheus` section must include only a `url` field.

###  Basic authentication 

Use the following steps to specify basic authentication for Prometheus:

     1. Create a Secret that contains a username and password in the `stringData` section and the `baremetal.cluster.gke.io/mark-source: "true"` annotation.

The following example shows a Secret that supports basic authentication:
            
            apiVersion: v1
            kind: Secret
            metadata:
              name: prom-basic-creds
              namespace: <cluster-namespace>
              annotations:**    baremetal.cluster.gke.io/mark-source: "true"**
            type: Opaque
            stringData:
              username: admin
              password: pwd
            

The annotation is required to make sure that the source secret and the secret in the target cluster are always in sync. The Secret updates when the source secret is updated.

**Note:** Whenever you rotate credentials, you must update this secret.
     2. Update the `prometheus.auth.basicAuth` section of the cluster spec to reference the username and password from the `data` field in the Secret.

The following example shows a `basicAuth` section that references the username and password in the Secret from the preceding step:
            
            # ... other vpa configurations ...
            prometheus:
              url: "http://prometheus.prometheus.svc.cluster.local:9090"
              auth:**    basicAuth:
                  usernameRef:
                    name: prom-basic-creds
                    key: username
                  passwordRef:
                    name: prom-basic-creds
                    key: password**
            

The username and password must be in the same Secret. The keys must be valid keys from the `data` field of the Secret.

The Prometheus instance should start working as a history provider for the vertical Pod autoscaler when the Cluster custom resource is updated.

###  Bearer token authentication 

Use the following steps to specify bearer token authentication for Prometheus:

     1. Create a Secret that contains a bearer token in the `stringData` section and the `baremetal.cluster.gke.io/mark-source: "true"` annotation.

The following example shows a Secret that supports bearer token authentication:
            
            apiVersion: v1
            kind: Secret
            metadata:
              name: prom-bearer-creds
              namespace: <cluster-namespace>**  annotations:
                baremetal.cluster.gke.io/mark-source: "true"**
            type: Opaque** stringData:
              bearertoken: "SAMPLE_TOKEN"**
            

The annotation is required to make sure that the source secret and the secret in the target cluster are always in sync. The Secret updates when the source secret is updated.

**Note:** Whenever you rotate credentials, you must update this secret.
     2. Update the `prometheus.auth.bearerTokenAuth` section of the cluster spec to reference the bearer token from the `data` field in the Secret.

The following example shows a `bearerTokenAuth` section that references the bearer token in the Secret from the preceding step:
            
            # ... other vertical Pod autoscaling configurations ...
            prometheus:
              url: "http://prometheus.prometheus.svc.cluster.local:9090"
              auth:**    bearerTokenAuth:
                    name: prom-bearer-creds
                    key: bearertoken**
            

The key must be a valid key from the `data` field of the Secret.

The Prometheus instance should start working as a history provider for vertical Pod autoscaling when the Cluster custom resource is updated.




### Disable the use of Prometheus

To disable the use of Prometheus with vertical Pod autoscaling, remove the `prometheus` section from the `verticalPodAutoscaling` section of the Cluster custom resource.

## Disable vertical Pod autoscaling

Disable Vertical Pod Autoscaling by removing its custom resources and configuration from your cluster:

  1. Delete any `VerticalPodAutoscaler` custom resources you have created.

  2. Modify the Cluster custom resource and remove the entire `verticalPodAutoscaling` section from the `spec`.

You can edit the Cluster custom resource directly or modify the cluster configuration file and use `bmctl update`.

  3. Remove the `preview.baremetal.cluster.gke.io/vertical-pod-autoscaler` annotation from the Cluster custom resource.




## Limitations

Consider the following limitations when using Vertical Pod Autoscaling:

  * Vertical Pod autoscaling isn't ready for use with JVM-based workloads due to limited visibility into actual memory usage of the workload.
  * The updater requires a minimum of two Pod replicas for Deployments to replace Pods with revised resource values.
  * The updater doesn't quickly update Pods that are crash-looping due to Out-Of-Memory (OOM) errors.
  * The `InPlaceOrRecreate` update policy for Pods is an alpha feature within vertical Pod autoscaling. It attempts best-effort in-place updates, but may fall back to recreating the Pod if in-place updates aren't possible.



## What's next

  * Explore [Pod Disruption Budgets](https://kubernetes.io/docs/concepts/workloads/pods/pod-disruption-budgets/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
