---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling/
title: Troubleshoot horizontal Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:55:12.148359+00:00
---

# Troubleshoot horizontal Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot horizontal Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When horizontal Pod autoscaling doesn't function as expected in Google Kubernetes Engine (GKE), your workloads might not scale correctly. This issue can prevent applications from handling load, which can cause performance issues or outages. You might see Pods not increasing despite high CPU, metric values showing as `<unknown>` in your HorizontalPodAutoscaler status, or scaling operations not occurring at all.

Use this document to diagnose and resolve common issues with horizontal Pod autoscaling, ranging from initial misconfigurations in your HorizontalPodAutoscaler objects to more complex failures within the metrics pipeline. By following these troubleshooting steps, you can help ensure that your applications scale efficiently and reliably based on demand, making effective use of the HorizontalPodAutoscaler resource.

This information is important for Application developers who configure HorizontalPodAutoscaler objects and need to make sure their applications scale correctly. It also helps Platform admins and operators troubleshoot issues with the metrics pipeline or cluster configuration that affect all autoscaled workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

  * Make sure you use HorizontalPodAutoscaler objects with scalable workloads, such as Deployments and StatefulSets. You can't use horizontal Pod autoscaling with workloads that can't scale, for example, DaemonSets.
  * To get the permissions that you need to troubleshoot horizontal Pod autoscaling in GKE, which includes inspecting HorizontalPodAutoscaler objects and viewing cluster logs, ask your administrator to grant you the following IAM roles on your project: 

    * Inspect GKE resources: [GKE Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.viewer) (`roles/container.viewer`) 
    * View cluster logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Configure the `kubectl` command-line tool to communicate with your GKE cluster:
        
        gcloud container clusters get-credentials CLUSTER_NAME \
            --location LOCATION \
            --project PROJECT_ID
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster.
    * `PROJECT_ID`: your Google Cloud project ID.



## Diagnose HorizontalPodAutoscaler issues

To diagnose issues with a HorizontalPodAutoscaler, inspect the status and configuration using `kubectl` commands or the Google Cloud console.

### Describe the HorizontalPodAutoscaler

To view real-time calculations and recent scaling decisions, use the `kubectl describe hpa` command:
    
    
    kubectl describe hpa HPA_NAME -n NAMESPACE_NAME
    

Replace the following:

  * `HPA_NAME`: the name of your HorizontalPodAutoscaler object.
  * `NAMESPACE_NAME`: the namespace of your HorizontalPodAutoscaler object.



The output is similar to the following:
    
    
    Name:                                                  php-apache-hpa
    Namespace:                                             default
    Reference:                                             Deployment/php-apache
    Metrics: ( current / target )
      resource cpu on pods (as a percentage of request):   1% (1m) / 50%
    Min replicas:                                          1
    Max replicas:                                          10
    Conditions:
      Type            Status  Reason              Message
      ----            ------  ------              -------
      AbleToScale     True    ReadyForNewScale    recommended size matches current size
      ScalingActive   True    ValidMetricFound    the HorizontalPodAutoscaler was able to successfully calculate a replica count
    Events:
      Type     Reason              Age   From                       Message
      ----     ------              ----  ----                       -------
      Normal   SuccessfulRescale   39m   horizontal-pod-autoscaler  New size: 4; reason: cpu resource utilization...
      Normal   SuccessfulRescale   26m   horizontal-pod-autoscaler  New size: 1; reason: cpu resource utilization...
    

In the output, the following three sections help you diagnose the issue:

  * **`Metrics`** : displays current metric values compared to their targets. An `<unknown>` metric value indicates that the HorizontalPodAutoscaler hasn't fetched the metric or that the metrics pipeline is broken.
  * **`Conditions`** : shows whether the HorizontalPodAutoscaler can fetch metrics (`AbleToScale`) and perform scaling calculations (`ScalingActive`). A `False` status in any of these conditions indicates a failure.
  * **`Events`** : logs recent scaling actions, warnings, and errors from the HorizontalPodAutoscaler controller. It's often the first place to find specific error messages or reasons, such as `FailedGetScale` or `FailedGetResourceMetric`.



### Check your HorizontalPodAutoscaler manifest

The YAML manifest of your HorizontalPodAutoscaler object lets you view information about its configuration and its current state.

To view the YAML manifest, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Object Browser** page.

[Go to Object Browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. In the **Object Kinds** list, select the **HorizontalPodAutoscaler** checkbox and click **OK**.

  3. Navigate to the **autoscaling** API group, then click the expander arrow for **HorizontalPodAutoscaler**.

  4. Click the name of the HorizontalPodAutoscaler object that you want to inspect.

  5. Review the **YAML** section, which displays the complete configuration of the HorizontalPodAutoscaler object.




### kubectl

Run the following command:
    
    
    kubectl get hpa HPA_NAME -n NAMESPACE_NAME -o yaml
    

Replace the following:

  * `HPA_NAME`: the name of your HorizontalPodAutoscaler object.
  * `NAMESPACE_NAME`: the namespace of your HorizontalPodAutoscaler object.



After you retrieve the manifest, look for these key sections:

  * **`spec` (your configuration)**: 
    * **`scaleTargetRef`** : the workload (such as a Deployment) that the HorizontalPodAutoscaler is configured to scale.
    * **`minReplicas` and `maxReplicas`**: the minimum and maximum replica settings.
    * **`metrics`** : the metrics configured for scaling (for example, CPU utilization or custom metrics).
  * **`status` (the HorizontalPodAutoscaler's live state)**: 
    * **`currentMetrics`** : the most recent metric values that the HorizontalPodAutoscaler has observed.
    * **`currentReplicas` and `desiredReplicas`**: the current number of Pods and the number that the HorizontalPodAutoscaler wants to scale to.
    * **`conditions`** : shows the HorizontalPodAutoscaler's health: 
      * `AbleToScale`: indicates if the HorizontalPodAutoscaler can find its target and metrics.
      * `ScalingActive`: shows if the HorizontalPodAutoscaler is allowed to calculate and perform scaling.
      * `ScalingLimited`: shows if the HorizontalPodAutoscaler wants to scale but is being capped by your `minReplicas` or `maxReplicas` settings.



### View event logs

To gain deeper insight into your HorizontalPodAutoscaler object, use the following types of logs:

  * **View HorizontalPodAutoscaler events in Cloud Logging** : use a log filter to find all HorizontalPodAutoscaler events for a specific cluster. For example:

    1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

    2. In the query pane, enter the following query:
           
           resource.type="k8s_cluster"
           resource.labels.cluster_name="CLUSTER_NAME"
           resource.labels.location="LOCATION"
           logName="projects/PROJECT_ID/logs/events"
           jsonPayload.involvedObject.kind="HorizontalPodAutoscaler"
           

Replace the following:

       * `CLUSTER_NAME`: the name of the cluster that the HorizontalPodAutoscaler belongs to.
       * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster.
       * `PROJECT_ID`: your project ID.
    3. Click **Run query** and review the output.

  * **[View horizontal Pod autoscaling events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events)** : these logs provide structured, human-readable logs explaining how the HorizontalPodAutoscaler computes a recommendation, offering detailed insight into its decision-making process.




## Troubleshoot HorizontalPodAutoscaler configuration errors

The following sections address misconfigurations in the HorizontalPodAutoscaler manifest, such as mistyped fields, invalid metric targets, or conflicting configurations.

### Target workload not found

#### Symptoms

The `Events` section has a condition of `FailedGetScale` with a message similar to the following:
    
    
    the HorizontalPodAutoscaler controller was unable to get the target's current scale: WORKLOAD_TYPE.apps "TARGET_WORKLOAD" not found
    

This output includes the following values:

  * `WORKLOAD_TYPE`: the type of workload, such as `Deployment` or `StatefulSet`.
  * `TARGET_WORKLOAD`: the name of the workload.



#### Cause

The HorizontalPodAutoscaler controller is unable to find the workload (such as a Deployment or StatefulSet) that it's configured to manage. This issue occurs because of a misconfiguration in the `scaleTargetRef` field within the HorizontalPodAutoscaler's manifest. The specified resource might not exist, might have been deleted, or might have a spelling mistake.

#### Resolution

Try the following solutions:

  1. **Verify the`scaleTargetRef` field of the HorizontalPodAutoscaler manifest**: make sure that the values of the `name`, `kind`, and `apiVersion` in the `scaleTargetRef` field exactly match the corresponding metadata of your target workload. If the workload name is incorrect, update the HorizontalPodAutoscaler's `scaleTargetRef` field to point to the correct name.
  2. **Confirm that the workload exists** : verify that the target workload exists in the same namespace as the HorizontalPodAutoscaler. You can check this with a command such as `kubectl get deployment DEPLOYMENT_NAME`. If you intentionally deleted the workload, delete the corresponding HorizontalPodAutoscaler object to clean up your cluster. If you need to re-create the workload, the HorizontalPodAutoscaler automatically finds it after it's available, and the error resolves.
  3. **Check that the HorizontalPodAutoscaler and workload are in the same namespace** : the HorizontalPodAutoscaler and its target workload must be in the same namespace. If you forget to specify a namespace when creating an object with `kubectl` commands, Kubernetes places the object in the `default` namespace. This behavior can cause a mismatch if your HorizontalPodAutoscaler is in the `default` namespace and your workload is in another, or the other way around. Check the namespace for both objects and verify that they match.



After the HorizontalPodAutoscaler successfully locates its target, the condition `AbleToScale` becomes `True`, and the message changes to: `the HorizontalPodAutoscaler controller was able to get the target's current scale`.

### Invalid metrics

#### Symptoms

If the HorizontalPodAutoscaler can't calculate the required replicas due to a configuration problem, its `Events` section shows a reason of `FailedComputeMetricsReplicas` with a message similar to the following:
    
    
    invalid metrics (1 invalid out of 1)
    

#### Cause

This error usually means there's a mismatch between the metric `type` and the `target` that you defined in your HorizontalPodAutoscaler manifest. For example, you might have specified a `type` of `Utilization`, but provided a target value of `averageValue` instead of `averageUtilization`.

#### Resolution

Correct the HorizontalPodAutoscaler manifest so that the value of the `target` field aligns with the metric `type`:

  * If `type` is `Utilization`, the value in the `target` field must be `averageUtilization`.
  * If `type` is `AverageValue`, the value in the `target` field must be `averageValue`.



### Metric label is not allowed

#### Symptoms

You notice the following error:
    
    
    unable to fetch metrics from external metrics API: googleapi: Error 400: Metric label: 'LABEL_NAME' is not allowed
    

In this output, `LABEL_NAME` is the name of the incorrect label.

#### Cause

The HorizontalPodAutoscaler manifest specifies an invalid label key in the `metric.selector.matchLabels` section and Cloud Monitoring doesn't recognize or allow this key for the metric.

#### Resolution

To resolve this issue, do the following:

  1. Identify the disallowed label name from the error message.
  2. Remove or correct this label key in the `metric.selector.matchLabels` section of your HorizontalPodAutoscaler manifest.
  3. Find a valid, filterable label key by consulting [the Cloud Monitoring documentation for that metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp).



### Multiple HorizontalPodAutoscalers target the same workload

#### Symptoms

There is no specific `Condition` or `Reason` within a HorizontalPodAutoscaler's status that directly indicates this conflict. Instead, you might observe the following symptoms:

  * The replica count of the workload can fluctuate unexpectedly.
  * Scaling decisions might not seem to correspond to the metrics defined in any single HorizontalPodAutoscaler.
  * When you view events, you might see alternating or contradictory `SuccessfulRescale` events from different HorizontalPodAutoscaler objects.



#### Cause

This issue occurs because more than one HorizontalPodAutoscaler object within the same namespace specifies the exact same workload in the `spec.scaleTargetRef` field. Each HorizontalPodAutoscaler independently calculates replica counts and attempts to scale the workload based on its own set of metrics and targets. Kubernetes doesn't block this configuration, but it leads to erratic scaling adjustments because the HorizontalPodAutoscalers compete with each other.

#### Resolution

To avoid conflicts, define all scaling metrics in a single HorizontalPodAutoscaler object. Each HorizontalPodAutoscaler calculates scaling needs from its own `spec.metrics` field, so merging them lets the chosen HorizontalPodAutoscaler object consider all factors, such as CPU and requests-per-second, together:

  1. To identify which HorizontalPodAutoscalers target the same workload, get the YAML manifest for each HorizontalPodAutoscaler object. Pay close attention to the `spec.scaleTargetRef` field in the output.
         
         kubectl get hpa -n NAMESPACE_NAME -o yaml
         

Replace `NAMESPACE_NAME` with the namespace of your HorizontalPodAutoscaler object.

Look for any instances where different HorizontalPodAutoscaler resources have the same values for `apiVersion`, `kind`, and `name` within their `scaleTargetRef` field.

  2. Consolidate metrics into a single HorizontalPodAutoscaler object:

     1. Choose one HorizontalPodAutoscaler object to keep. This HorizontalPodAutoscaler will be the one that you modify.
     2. Examine the `spec.metrics` section in the manifest of each of the other HorizontalPodAutoscaler objects that target the same workload.
     3. Copy the metric definitions that you want to keep from the `spec.metrics` sections of the duplicate HorizontalPodAutoscaler objects.
     4. Paste these copied metric definitions into the `spec.metrics` array of the HorizontalPodAutoscaler that you decided to keep.
  3. Apply your changes:
         
         kubectl apply -f MANIFEST_NAME
         

Replace `MANIFEST_NAME` with the name of the HorizontalPodAutoscaler manifest that you decided to keep.

  4. Delete the other HorizontalPodAutoscaler objects that were targeting the same workload:
         
         kubectl delete hpa DUPLICATE_MANIFEST_NAME -n NAMESPACE_NAME
         

Replace `DUPLICATE_MANIFEST_NAME` with the name of the redundant HorizontalPodAutoscaler object that you want to delete.




## Troubleshoot workload and Service errors

The following sections address errors caused by the target workload or its associated Services, rather than the HorizontalPodAutoscaler object itself.

### Missing resource requests for scaling calculation

#### Symptoms

The `ScalingActive` condition is `False` with a `Reason` of `FailedGetResourceMetric`. You typically also see a message similar to the following:
    
    
    the HorizontalPodAutoscaler was unable to compute the replica count
    

#### Cause

The HorizontalPodAutoscaler needs to calculate resource utilization as a percentage to scale the workload, but it can't perform this calculation because at least one container within the Pod specification is missing a `resources.requests` definition for the corresponding resource (`cpu` or `memory`).

#### Resolution

To resolve this issue, update the Pod manifest within your Deployment, StatefulSet, or other controller to include a `resources.requests` field for the resource (`cpu` or `memory`) that the HorizontalPodAutoscaler is trying to scale on for _all_ containers in the Pod. For example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-pod
    # Multiple lines are omitted here
    spec:
      containers:
      - name: example-container
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
    

### Unable to fetch Pod metrics

#### Symptoms

You observe a persistent message similar to the following:
    
    
    unable to fetch pod metrics for pod
    

It's normal to see this message temporarily when the metrics server starts up.

#### Cause

To scale based on resource utilization percentage (such as `cpu` or `memory`), every container within the Pods targeted by the HorizontalPodAutoscaler object must have the `resources.requests` field defined for that specific resource. Otherwise, the HorizontalPodAutoscaler can't perform the calculations that it needs to, and takes no action related to that metric.

#### Resolution

If these error messages persist and you notice that Pods are not scaling for your workload, verify that you have [specified resource requests for each container in your workload](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#per-pod_resources).

### Multiple services select the same target

#### Symptoms

You notice the following error:
    
    
    multiple services selecting the same target of HPA_NAME: SERVICE_NAME
    

This output includes the following values:

  * `HPA_NAME`: the name of the HorizontalPodAutoscaler.
  * `SERVICE_NAME`: the name of a Service.



#### Cause

Traffic-based autoscaling is configured, but more than one Kubernetes Service is targeting the HorizontalPodAutoscaler's `scaleTargetRef` field. Traffic-based autoscaling supports only a one-to-one relationship between the Service and the autoscaled workload.

#### Resolution

To fix this issue, make sure that only one Service's label selector matches your workload's Pods:

  1. Find your workload's Pod labels:
         
         kubectl get deployment HPA_TARGET_DEPLOYMENT \
             -n NAMESPACE \
             -o jsonpath='{.spec.template.metadata.labels}'
         

Replace the following:

     * `HPA_TARGET_DEPLOYMENT`: the name of the Deployment that the HorizontalPodAutoscaler is targeting.
     * `NAMESPACE`: the namespace of the Deployment.

The output is similar to the following:
    
    {"app":"my-app", "env":"prod"}
    

  2. Find all Services that match those labels by reviewing the `spec.selector` field for all Services in the namespace.
         
         kubectl get services -n NAMESPACE -o yaml
         

Identify every Service whose selector matches the labels from the previous step. For example, both `{"app": "my-app"}` and `{"app": "my-app", "env": "prod"}` match the example Pod labels.

  3. Resolve the conflict by choosing one of the following options:

     * Make the intended Service's selector unique by adding a new, unique label to your Deployment's `spec.template.metadata.labels` field. Then, update the _one_ intended Service's `spec.selector` field to include this new label.
     * Make other Service selectors more restrictive by changing the `spec.selector` field of all _other_ conflicting Services so they are more restrictive and no longer match your workload's Pods.
  4. Apply your changes:
         
         kubectl apply -f MANIFEST_NAME
         

Replace `MANIFEST_NAME` with the name of the YAML file containing the updated Service or Deployment manifest.




## Troubleshoot metrics API and data availability

The following sections help you resolve errors that occur when the HorizontalPodAutoscaler tries to communicate with a metrics API or query a metrics backend.

### Troubleshoot custom and external metrics

When your HorizontalPodAutoscaler relies on metrics from sources other than default CPU or memory, issues can occur within the custom or external metrics pipeline. This pipeline consists of the HorizontalPodAutoscaler controller, Kubernetes metrics API server, metrics adapter, and the metric source (for example, Cloud Monitoring or Prometheus) as shown in the following diagram:

![HPA metrics
pipeline showing components: HPA controller, Kubernetes API server, metrics
adapter, and metric source.](https://docs.cloud.google.com/static/kubernetes-engine/images/metrics-pipeline.svg)

#### Symptoms

The most common symptoms of an issue in the metrics pipeline are the following:

  * The metric value shows as `<unknown>`.
  * HorizontalPodAutoscaler events show errors such as `FailedGetExternalMetric` or `FailedGetCustomMetric`.



#### Cause

An issue exists within the custom or external metrics pipeline.

#### Resolution

Use the following steps to help you debug the pipeline:

  1. **Check if the metrics adapter is registered and available** : the metrics adapter must register itself with the main Kubernetes API server to serve metrics. This action is the most direct way to see if the adapter is running and reachable by the API server:
         
         kubectl get apiservice | grep -E 'NAME|metrics.k8s.io'
         

In the output, you should see the `v1beta1.custom.metrics.k8s.io` or `v1beta1.external.metrics.k8s.io` entries and a value of `True` in the `Available` column. For example:
         
         NAME                   SERVICE                      AVAILABLE   AGE
         v1beta1.metrics.k8s.io kube-system/metrics-server   True        18d
         

     * If the value in the `Available` column is `False` or missing, your adapter is likely crashed or misconfigured. Check the adapter's Pod logs in the `kube-system` or `custom-metrics` namespace for errors related to permissions, network connectivity to the metric source, or messages indicating the metric couldn't be found.

     * If the value is `True`, proceed to the next step.

  2. **Query the metrics API directly** : if the adapter is available, bypass the HorizontalPodAutoscaler and ask the Kubernetes API for your metric directly. This command tests the entire pipeline, from the API server to the metrics adapter to the data source.

**Note:** The following commands use the `jq` JSON processor to print the JSON output. If you don't have `jq` installed, you can remove the `| jq .` section of the commands to view the raw JSON response.

To query external metrics, run the following command:
         
         kubectl get --raw "/apis/external.metrics.k8s.io/v1beta1/namespaces/NAMESPACE_NAME/METRIC_NAME" | jq .
         

To query custom Pod metrics, run the following command:
         
         kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/NAMESPACE_NAME/pods/*/METRIC_NAME" | jq .
         

Replace the following:

     * `NAMESPACE_NAME`: the namespace where your Pods are running.
     * `METRIC_NAME`: the name of the custom or external metric that you're trying to query. For example, `requests_per_second` or `queue_depth`.
  3. **Analyze the command output** : the result of the previous commands tells you where the problem is. Choose the scenario that matches your output:

     * **Successful JSON response with a value** : the metrics pipeline is working correctly. The problem is likely a configuration issue in your HorizontalPodAutoscaler manifest. Check for spelling mistakes in the metric name or incorrect `matchLabels`.
     * **`Error: Error from server (Service Unavailable)`** : this error typically indicates a network connectivity problem, which is often a firewall issue in clusters that use network isolation.

       1. Identify the metrics adapter Service. It's usually in the `custom-metrics` or `kube-system` namespace:
              
              kubectl get service -n custom-metrics,kube-system | grep -E 'adapter|metrics'
              

       2. Find the port that the adapter is listening on:
              
              kubectl get service ADAPTER_SERVICE -n ADAPTER_NAMESPACE -o yaml
              

Replace the following:

          * `ADAPTER_SERVICE`: the name of the Kubernetes Service associated with the metrics adapter that you deployed. This Service is the Service that you found in the preceding step. This Service exposes the adapter's functionality to other parts of the cluster, including the Kubernetes API server.
          * `ADAPTER_NAMESPACE`: the namespace where the adapter service resides (for example, `custom-metrics` or `kube-system`).
       3. Find the inbound firewall rules for your cluster's control plane:
              
              gcloud compute firewall-rules list \
                  --filter="name~gke-CLUSTER_NAME-[0-9a-z]*-master"
              

Replace `CLUSTER_NAME` with the name of your cluster.

       4. Add the adapter's `targetPort` to the rule:

**Caution:** The following command replaces the existing allowed ports. To avoid breaking cluster functionality, you must include the existing ports (typically `tcp:443` for the Kubernetes API and `tcp:10250` for the `kubelet` agent) _plus_ the `ADAPTER_PORT`.
          1. Describe the current rule to see existing allowed ports:
                 
                 gcloud compute firewall-rules describe FIREWALL_RULE_NAME
                 

Replace `FIREWALL_RULE_NAME` with the name of the firewall rule that governs network traffic to the control plane of your Kubernetes cluster.

          2. Update the rule to add the adapter port to the list:
                 
                 gcloud compute firewall-rules update FIREWALL_RULE_NAME \
                     --allow tcp:443,tcp:10250,tcp:ADAPTER_PORT
                 

Replace `ADAPTER_PORT` with the network port that the metrics adapter is listening on.

       5. Make sure that Kubernetes Network Policies are not blocking traffic to the metrics adapter Pods:
              
              kubectl get networkpolicy -n custom-metrics,kube-system
              

Review any policies to verify that they allow ingress traffic from the control plane or API server to the `ADAPTER_SERVICE` on the `ADAPTER_PORT`.

     * **An empty list`[]`**: this output means that the adapter is running, but can't retrieve the specific metric, indicating a problem with either the adapter's configuration or the metric source itself.

       * **Adapter Pod issues** : inspect the logs of the metrics adapter Pod or Pods for errors related to API calls, authentication, or metric fetching. To inspect the logs, do the following:

         1. Find the name of the adapter Pod:
                
                kubectl get pods -n ADAPTER_NAMESPACE
                

         2. View its logs:
                
                kubectl logs ADAPTER_POD_NAME \
                    -n ADAPTER_NAMESPACE
                

Replace the following:

            * `ADAPTER_POD_NAME`: the name of the adapter Pod that you identified in the previous step.
            * `ADAPTER_NAMESPACE`: the namespace where the adapter Pod resides (for example, `custom-metrics` or `kube-system`).
       * **No data at the source** : the metric might not exist in the source system. Use a monitoring tool, such as Metrics Explorer, to confirm the metric exists and has the correct name and labels.




### Metric versions not found or adapter unavailable

#### Symptoms

You notice the following error:
    
    
    unable to fetch metrics from custom metrics API: no known available metric versions found
    

#### Cause

This error indicates a communication breakdown within the cluster, not a problem with the metrics source (such as Cloud Monitoring). Common causes include the following:

  * The Kubernetes API server is temporarily unavailable (for example, during a cluster upgrade or control plane repair).
  * The metrics adapter Pods (for example, `custom-metrics-stackdriver-adapter`) are unhealthy, not running, or aren't correctly registered with the API server.



#### Resolution

This issue is often temporary. If it persists, try the following solutions:

  1. **Check the health of the Kubernetes control plane** :

     1. In the Google Cloud console, view your cluster's health and status.

        1. Go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Check the **Status** and **Notifications** columns for your cluster.

     3. Click notifications **Notifications** to look for any ongoing operations such as upgrades or repairs. The API server might be briefly unavailable during these times.

     4. Review Cloud Audit Logs for any errors related to control plane components. For information about how to view these logs, see [GKE audit logging information](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).

  2. **Check the health and logs of the metrics adapter Pods** : make sure that the metrics adapter Pods are in the `Running` status and have no recent restarts:
         
         kubectl get pods -n custom-metrics,kube-system -o wide
         

If a Pod's status is anything other than `Running`, or it has a high restart count, investigate the Pod to find the root cause. For troubleshooting tips, see [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods) in the Kubernetes documentation.

  3. **Verify that the metrics APIs are registered and available** :
         
         kubectl get apiservice | grep metrics.k8s.io
         

If the metrics APIs are healthy, the output is similar to the following:
         
         NAME                            SERVICE                                             AVAILABLE   AGE
         v1beta1.custom.metrics.k8s.io   custom-metrics/custom-metrics-stackdriver-adapter   True        18d
         v1beta1.external.metrics.k8s.io custom-metrics/custom-metrics-stackdriver-adapter   True        18d
         v1beta1.metrics.k8s.io          kube-system/metrics-server                          True        18d
         

If the `AVAILABLE` column has a value of `False`, the `Message` column in the full APIService manifest might provide more details.

You can view the full manifest with the following command:
         
         kubectl get apiservice API_SERVICE_NAME -o yaml
         

Replace `API_SERVICE_NAME` with the name of the APIService object, such as `v1beta1.custom.metrics.k8s.io`.




### Metric query returns no time series

#### Symptoms

You notice the following error:
    
    
    unable to fetch metrics from custom or external metrics API: googleapi: Error
    400: The supplied filter [...] query will not return any time series
    

#### Cause

The query sent to Cloud Monitoring was valid, but it returned no data. This means no data points exist that match your filter (which is different from finding a metric with a value of `0`). The most likely reason for this issue is that the application or workload responsible for generating the custom metric was not writing data to Cloud Monitoring during the time that the errors were reported.

#### Resolution

Try the following solutions:

  1. **Verify configuration** : make sure that the metric names and labels in your HorizontalPodAutoscaler object precisely match those being emitted by the application.
  2. **Check permissions** : confirm the application is correctly configured with the necessary permissions and API endpoints to publish metrics to Cloud Monitoring.
  3. **Confirm application activity** : verify that the application responsible for the metric was operational and attempting to send data to Cloud Monitoring during the time period when the HorizontalPodAutoscaler warnings occurred.
  4. **Investigate for errors** : check the application's logs from the same time period for any explicit errors related to metric emission, such as connection failures, invalid credentials, or formatting issues.



## Troubleshoot healthy but unexpected scaling behaviors

The following sections address scenarios where the HorizontalPodAutoscaler configuration is valid and metrics are available, but scaling actions don't occur as expected.

### HorizontalPodAutoscaler is healthy but doesn't scale

#### Symptoms

The HorizontalPodAutoscaler appears healthy, its conditions report `True`, and it shows no errors in its events. However, it still doesn't take any scaling actions.

#### Cause

Several factors can cause this expected behavior:

  * **Replica limits** : the current number of replicas is already at the boundary set by the `minReplicas` or `maxReplicas` field in the HorizontalPodAutoscaler configuration.
  * **Tolerance window** : Kubernetes uses a default 10% tolerance window to prevent scaling on minor metric fluctuations. Scaling only occurs if the ratio of the current metric to the target metric falls outside the 0.9 to 1.1 range. For example, if the target is 85% CPU and the current usage is 93%, the ratio is approximately 1.094 (93/85≈1.094). Because this value is less than 1.1, the HorizontalPodAutoscaler doesn't scale up.
  * **Unready Pods** : the HorizontalPodAutoscaler includes only Pods with a `Ready` status in its scaling calculations. Pods that are stuck with a `Pending` status or are not becoming `Ready` (due to failing health checks or resource issues) are ignored and can prevent scaling.
  * **Sync period delay** : the HorizontalPodAutoscaler controller checks metrics periodically. A delay of 15-30 seconds between a metric crossing the threshold and the initiation of a scaling action is normal.
  * **New metric latency** : when a HorizontalPodAutoscaler uses a new custom metric for the first time, you might see a one-time latency of several minutes. This delay occurs because the monitoring system (such as Cloud Monitoring) must create the new time series when the first data point is written.
  * **Multiple metrics calculation** : when you configure multiple metrics, the HorizontalPodAutoscaler calculates the required replica count for each metric independently and then chooses the _highest_ calculated value as the final number of replicas. Because of this behavior, your workload scales to meet the demands of the metric with the highest needs. For example, if CPU metrics calculate a need for 9 replicas, but a requests-per-second metric calculates a need for 15, the HorizontalPodAutoscaler scales the Deployment to 15 replicas.



#### Resolution

Try the following solutions:

  * **Replica limits** : check the `minReplicas` and `maxReplicas` values in your HorizontalPodAutoscaler manifest or in the output of the `kubectl describe` command. Adjust these limits if they are preventing necessary scaling.
  * **Tolerance window** : if scaling is required inside the default tolerance, [configure a different tolerance value](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#tolerance). Otherwise, wait for the metric to move outside the 0.9 to 1.1 ratio.
  * **Unready Pods** : investigate why Pods are `Pending` or not `Ready` and resolve the underlying issues (for example, resource constraints, failing readiness probes). For troubleshooting tips, see [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods) in the Kubernetes documentation.
  * **Sync period delay and new metric latency** : these latencies are normal. Wait for the sync period to complete or for the new custom metric time series to be created.
  * **Multiple metrics calculation** : this is the intended behavior. If scale-up is occurring based on one metric (such as requests-per-second), it is correctly overriding another metric's lower calculation (such as CPU).



### HorizontalPodAutoscaler fails to scale down

#### Symptoms

The HorizontalPodAutoscaler successfully scales the workload up, but fails to scale it back down even when metrics such as CPU utilization are low.

#### Cause

This behavior is designed to prevent rapidly scaling up and down or scaling down based on incomplete information. The main reasons are the following:

  * **Using multiple metrics** : the HorizontalPodAutoscaler scales based on the metric requiring the _most_ replicas. If you have multiple metrics, the workload won't scale down unless _all_ metrics indicate that fewer replicas are needed. One metric demanding a high replica count prevents scale-down, even if others are low.
  * **Unavailable metrics** : if any metric becomes unavailable (often showing as `<unknown>`), the HorizontalPodAutoscaler conservatively refuses to scale down the workload. It can't determine if the metric is missing because usage is truly zero or because the metrics pipeline is broken. This issue is common with rate-based custom metrics (for example, `messages_per_second`), which can stop reporting data when there is no activity, causing the HorizontalPodAutoscaler to see the metric as unavailable and halt scale-down operations.
  * **Scale-down delay from scaling policy** : the HorizontalPodAutoscaler's `behavior` field lets you configure scaling policies. The default policy for scaling down includes a stabilization window of 300 seconds (five minutes). During this window, the HorizontalPodAutoscaler won't reduce the replica count, even when metric values have fallen below the target threshold. This window prevents rapid fluctuations, but can make scale-down slower than expected.



#### Resolution

Try the following solutions:

  1. For multiple metrics and unavailable metrics, diagnose the metric that's causing issues:
         
         kubectl describe hpa HPA_NAME -n NAMESPACE_NAME
         

In the output, look in the `Metrics` section for any metric with a status of `<unknown>` and in the `Events` section for warnings such as `FailedGetCustomMetric` or `FailedGetExternalMetric`. For detailed pipeline debugging, see the Troubleshoot custom and external metrics section.

  2. For unavailable metrics, if a metric becomes unavailable during periods of low traffic (common with rate-based metrics), try one of the following solutions:

     * Use gauge-based metrics instead of rate-based ones where possible. A gauge metric, such as the total number of messages in a queue (for example, `subscription` or `num_undelivered_messages`), consistently reports a value, even if that value is `0`, allowing the HorizontalPodAutoscaler to make scaling decisions reliably.
     * Make sure that your metric source reports zero values. If you control the custom metric, configure it to publish a `0` during periods of inactivity instead of sending no data at all.
  3. For scale-down delays from scaling policy, if the default five-minute stabilization window for scale-downs is too long, customize it. Inspect the `spec.behavior.scaleDown` section of your HorizontalPodAutoscaler manifest. You can lower the `stabilizationWindowSeconds` to let the autoscaler scale down more quickly after the metrics drop. For more information about configuring these policies, see [Scaling Policies](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-policies) in the Kubernetes documentation.




## Troubleshoot scaling GKE workloads to and from zero using HPA

This section helps you diagnose issues when configuring workloads to [scale to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa) (`minReplicas: 0`) in GKE 1.37 or later.

### Workload does not scale to zero

If your workload remains at one or more replicas when demand drops to zero, check the following:

  1. **Check`minReplicas`**: ensure that the `minReplicas: 0` field-value pair is set in your HorizontalPodAutoscaler manifest.
  2. **Check metric types** : the HPA cannot scale to zero if it uses only CPU or memory (`Resource`) metrics. You must configure at least one `External` or `Object` metric.
  3. **Check multiple metrics** : the HPA scales based on the metric requiring the highest replica count. If you configure multiple metrics, the workload does not scale to zero unless every monitored metric evaluates to zero.
  4. **Wait for the scale-down stabilization window** : by default, GKE waits for five minutes (`scaleDown.stabilizationWindowSeconds: 300`) of continuous zero demand before scaling from one to zero replicas.
  5. **Check for unavailable metrics** : if the value of any metric shows as `<unknown>`, the HPA pauses scale-down operations to prevent premature downscaling. For more information, see Troubleshoot horizontal Pod autoscaler failing to scale down.



### Workload does not scale up from zero

If your workload remains at zero replicas when demand increases, check the following:

  1. **Inspect the HorizontalPodAutoscaler** : run the `kubectl describe hpa HPA_NAME` command and check the following sections in the output:

     * **Metrics section** : verify that the metric value is greater than zero and does not display the value as `<unknown>`. If the metric is missing or not updating, verify that the external source (such as Pub/Sub) is publishing events and that Cloud Monitoring is receiving them.
     * **Conditions section** : 
       * **Healthy zero-replica state** : verify that the conditions display `AbleToScale: True`, `ScalingActive: True`, and `ScaledToZero: True` (with reason `ScaledToZero`). In this state, GKE automatically scales the workload up when demand increases.
       * **External override detected** : check whether the value of the `ScalingActive` condition is `False` with either the `ScalingDisabledExternalScaleToZero` reason or the `ScalingDisabledReplicaCountZero` reason, which indicates that the workload was manually scaled to zero. For example, the workload was manually scaled with the `kubectl scale` command, which pauses autoscaling to prevent conflicting changes.
     * **Resolution** : to resume automatic scaling, manually scale the Deployment back to one or more replicas:
           
           kubectl scale deployment DEPLOYMENT_NAME --replicas=1
           

  2. **Check for cold-start latency** : if the workload starts slowly, node provisioning might be adding delay. To help ensure standby compute capacity is ready when scaling from zero, consider using [Capacity Buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
