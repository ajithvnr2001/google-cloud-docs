---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling/
title: Scale container resource requests and limits \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:25.393658+00:00
---

# Scale container resource requests and limits  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scale container resource requests and limits Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

To prevent abrupt Pod termination under node pressure, improve application stability, and ensure cost-efficient resource allocation, optimize [CPU requests](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/) and [memory requests](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/) for containers in a Google Kubernetes Engine (GKE) cluster. [Vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) automatically adjusts these container resource requests and limits based on historical usage and real-time demand.

You can manage container resources manually through the Google Cloud console, analyze recommendations using a `VerticalPodAutoscaler` object, or configure automatic scaling with [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).

## Before you begin

**Note:** Vertical Pod autoscaling is compatible only with workloads managed by a controller, such as Deployments, StatefulSets, ReplicaSets, and ReplicationControllers. You can't use vertical Pod autoscaling with standalone Pods.

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Analyze resource requests

The Vertical Pod Autoscaler automatically analyzes your containers and provides suggested resource requests. You can view these resource requests using the Google Cloud console, Cloud Monitoring, or Google Cloud CLI.

**Caution:** In some cases, when you access the vertical Pod autoscaling recommendations, GKE initializes the Vertical Pod Autoscaler controller. This might cause a control plane re-creation.

### Console

To view suggested resource requests in the Google Cloud console, you must have an existing workload deployed that is at least 24 hours old. Some suggestions might not be available or relevant for certain workloads, such as those created within the last 24 hours, standalone Pods, and apps written in Java.

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the workload you want to scale.

  3. Click _list_ **Actions > Scale > Edit resource requests**.

The Analyze resource utilization data section shows historic usage data that the Vertical Pod Autoscaler controller analyzed to create the suggested resource requests in the Adjust resource requests and limits section.




###  Cloud Monitoring 

To view suggested resource requests in Cloud Monitoring, you must have an existing workload deployed.

  1. Go to the **Metrics Explorer** page in the Google Cloud console.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Click **Configuration**.

  3. Expand the **Select a Metric** menu.

  4. In the **Resource** menu, select **Kubernetes Scale**.

  5. In the **Metric category** menu, select **Autoscaler**.

  6. In the **Metric** menu, select **Recommended per replicate request bytes** and **Recommended per replica request core**.

  7. Click **Apply**.




###  gcloud CLI 

To view suggested resource requests, you must create a `VerticalPodAutoscaler` object and a Deployment.

  1. For Standard clusters, enable vertical Pod autoscaling for your cluster. For Autopilot clusters, vertical Pod autoscaling is enabled by default.
         
         gcloud container clusters update CLUSTER_NAME --enable-vertical-pod-autoscaling
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. Save the following manifest as `my-rec-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-rec-deployment
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: my-rec-deployment
           template:
             metadata:
               labels:
                 app: my-rec-deployment
             spec:
               containers:
               - name: my-rec-container
                 image: nginx
         

This manifest describes a `Deployment` that does not have CPU or memory requests. The `containers.name` value of `my-rec-deployment` specifies that all Pods in the Deployment belong to the `VerticalPodAutoscaler`.

  3. Apply the manifest to the cluster:
         
         kubectl create -f my-rec-deployment.yaml
         

  4. Save the following manifest as `my-rec-vpa.yaml`:
         
         apiVersion: autoscaling.k8s.io/v1
         kind: VerticalPodAutoscaler
         metadata:
           name: my-rec-vpa
         spec:
           targetRef:
             apiVersion: "apps/v1"
             kind:       Deployment
             name:       my-rec-deployment
           updatePolicy:
             updateMode: "Off"
         

This manifest describes a `VerticalPodAutoscaler`. The `updateMode` value of `Off` means that when Pods are created, the Vertical Pod Autoscaler controller analyzes the CPU and memory needs of the containers and records those recommendations in the `status` field of the resource. The Vertical Pod Autoscaler controller does not automatically update the resource requests for running containers.

  5. Apply the manifest to the cluster:
         
         kubectl create -f my-rec-vpa.yaml
         

  6. After some time, view the `VerticalPodAutoscaler`:
         
         kubectl get vpa my-rec-vpa --output yaml
         

The output is similar to the following:
         
         ...
           recommendation:
             containerRecommendations:
             - containerName: my-rec-container
               lowerBound:
                 cpu: 25m
                 memory: 262144k
               target:
                 cpu: 25m
                 memory: 262144k
               upperBound:
                 cpu: 7931m
                 memory: 8291500k
         ...
         

This output shows recommendations for CPU and memory requests.




## Set Pod resource requests manually

You can set Pod resource requests manually using the Google Cloud console or kubectl. Use the following best practices for setting your container resource requests and limits:

  * **Memory** : Set the same amount of memory for the request and limit.
  * **CPU** : For the request, specify the minimum CPU needed to ensure correct operation, according to your own SLOs. Set an unbounded CPU limit.

**Caution:** Applying vertical Pod autoscaling recommendations causes workload disruptions.

### Console

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the workload you want to scale.

  3. Click _list_ **Actions > Scale > Edit resource requests**.

     1. The **Adjust resource requests and limits** section shows the current CPU and memory requests for each container as well as suggested CPU and memory requests.
  4. Click **Apply Latest Suggestions** to view suggested requests for each container.

  5. Click **Save Changes**.

  6. Click **Confirm**.




### kubectl

### Vertically scale your workload with minimal disruption

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Starting in [Kubernetes version 1.33](https://opensource.googleblog.com/2025/05/kubernetes-1.33-available-on-gke.html), you can use the [`kubectl patch`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#patch) command to vertically scale your workload by updating the resources that are assigned to a container, without re-creating the Pod. For more information, including limitations, see the [Kubernetes documentation for resizing CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources).

To use the `kubectl patch` command, specify the updated resource request under the `--patch` flag. For example, to scale `my-app` to 800 mCPUs, run the following command:
    
    
    kubectl patch pod my-app --subresource resize --patch \
      '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"800m"}, "limits":{"cpu":"800m"}}}]}}'
    

### Vertically scale your workload

To set resource requests for a Pod, set the requests.cpu and memory.cpu values in your Deployment manifest. In this example, you manually modify the Deployment created in Analyze resource requests with suggested resource requests.

  1. Save the following example manifest as `my-adjusted-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-rec-deployment
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: my-rec-deployment
           template:
             metadata:
               labels:
                 app: my-rec-deployment
             spec:
               containers:
               - name: my-rec-container
                 image: nginx
                 resources:
                   requests:
                     cpu: 25m
                     memory: 256Mi
         

This manifest describes a Deployment that has two Pods. Each Pod has one container that requests 25 milliCPU and 256 MiB of memory.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f my-adjusted-deployment.yaml
         




## Set Pod resource requests automatically

Vertical Pod autoscaling uses the `VerticalPodAutoscaler` object to automatically set resource requests on Pods when the `updateMode` is `Auto`. You can configure a `VerticalPodAutoscaler` using the gcloud CLI or the Google Cloud console.

**Caution:** Enabling or disabling vertical Pod autoscaling can cause workload disruptions by re-creating Pods.

### Console

To set resource requests automatically, you must have a cluster with the vertical Pod autoscaling feature enabled. Autopilot clusters have the vertical Pod autoscaling feature enabled by default.

## Enable Vertical Pod Autoscaling

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Details** tab.

  4. In the **Automation** section, click _edit_ **Edit** for the **Vertical Pod Autoscaling** option.

  5. Select the **Enable Vertical Pod Autoscaling** checkbox.

  6. Click **Save changes**.




## Configure Vertical Pod Autoscaling

  1. Go to the **Workloads** page in Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment that you want to configure vertical Pod autoscaling for.

  3. Click _list_ **Actions > Edit autoscaling**.

  4. Under the _Vertical Pod Autoscaling section_ , click **Select and configure**.

  5. Under _Update mode_ , choose an autoscaling mode:

     * **Auto mode** : Vertical Pod autoscaling updates CPU and memory requests during the life of a Pod.
     * **Initial mode** : Vertical Pod autoscaling assigns resource requests only at Pod creation and never changes them later.
  6. (Optional) Set container policies. This option lets you ensure that the recommendation is never set to greater or lower than a specified resource request.

     1. Click **Add Policy**.
     2. Select the container to add a policy, or choose a default policy to apply to all containers that don't have a policy.
     3. Select **Auto** for **Scaling mode**.
     4. In **Controlled resources** , select which resources you want to autoscale the container on.
     5. Click **Add Rule** to set one or more minimum or maximum ranges for the container's resource requests: 
        * **Min. allowed Memory** : the minimum amount of memory that the container should always have, in MiB.
        * **Min. allowed CPU** : the minimum amount of CPU that the container should always have, in mCPU.
        * **Max allowed Memory** : the maximum amount of memory that the container should always have, in MiB.
        * **Max allowed CPU** : the maximum amount of CPU that the container should always have, in mCPU.
  7. Click **Submit**.




### gcloud

To set resource requests automatically, you must use a cluster that has the vertical Pod autoscaling feature enabled. Autopilot clusters have the feature enabled by default.

  1. For Standard clusters, enable vertical Pod autoscaling for your cluster:
         
         gcloud container clusters update CLUSTER_NAME --enable-vertical-pod-autoscaling
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. Save the following manifest as `my-auto-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-auto-deployment
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: my-auto-deployment
           template:
             metadata:
               labels:
                 app: my-auto-deployment
             spec:
               containers:
               - name: my-container
                 image: registry.k8s.io/ubuntu-slim:0.14
                 resources:
                   requests:
                     cpu: 100m
                     memory: 50Mi
                 command: ["/bin/sh"]
                 args: ["-c", "while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done"]
         

This manifest describes a Deployment that has two Pods. Each Pod has one container that requests 100 milliCPU and 50 MiB of memory.

If you create a manifest to match specific details in your own project, then ensure that you don't include sensitive data in the vertical Pod autoscaler fields.

  3. Apply the manifest to the cluster:
         
         kubectl create -f my-auto-deployment.yaml
         

  4. (Optional) Configure `resizePolicy` for in-place updates.

If you plan to use `InPlaceOrRecreate` mode, you can explicitly define how containers should handle resource changes in your Deployment manifest.

Add the `resizePolicy` field to your container spec:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-auto-deployment
         spec:
           ...
           template:
             ...
             spec:
               containers:
               - name: my-container
                 image: registry.k8s.io/ubuntu-slim:0.14
                 **resizePolicy :
                 - resourceName: cpu
                   restartPolicy: NotRequired
                 - resourceName: memory
                   restartPolicy: RestartContainer**
                 resources:
                   requests:
                     cpu: 100m
                     memory: 50Mi
                 ...
         

In this example, CPU resizing is permitted without restarting the container whereas a container restart is required for memory resizes.

  5. List the running Pods:
         
         kubectl get pods
         

The output shows the names of the Pods in `my-deployment`:
         
         NAME                            READY     STATUS             RESTARTS   AGE
         my-auto-deployment-cbcdd49fb-d6bf9   1/1       Running            0          8s
         my-auto-deployment-cbcdd49fb-th288   1/1       Running            0          8s
         

  6. Save the following manifest as `my-vpa.yaml`:
         
         apiVersion: autoscaling.k8s.io/v1
         kind: VerticalPodAutoscaler
         metadata:
           name: my-vpa
         spec:
           targetRef:
             apiVersion: "apps/v1"
             kind:       Deployment
             name:       my-auto-deployment
           updatePolicy:
             updateMode: "Recreate"
         

This manifest describes a `VerticalPodAutoscaler` with the following properties:

     * `targetRef.name`: specifies that any Pod that is controlled by a Deployment named `my-deployment` belongs to this `VerticalPodAutoscaler`.
     * `updateMode: "Recreate"`: specifies that the Vertical Pod Autoscaler controller can delete a Pod, adjust the CPU and memory requests, and then start a new Pod. This is the default behavior if no mode is specified (also referred to as `Auto` mode). You can also change the update mode to one of the following values: 
       * `updateMode: "Initial"`: vertical Pod autoscaling assigns resource requests only at Pod creation time.
       * `updateMode: "InPlaceOrRecreate"` ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): vertical Pod autoscaling attempts to update resources without re-creating the Pod, falling back on re-creation if necessary. This works best when your workloads are configured with `resizePolicy: NotRequired`.
  7. Apply the manifest to the cluster:
         
         kubectl create -f my-vpa.yaml
         

  8. Wait a few minutes, and view the running Pods again:
         
         kubectl get pods
         

The output shows that the Pod names have changed:
         
         NAME                                 READY     STATUS             RESTARTS   AGE
         my-auto-deployment-89dc45f48-5bzqp   1/1       Running            0          8s
         my-auto-deployment-89dc45f48-scm66   1/1       Running            0          8s
         

If the Pod names have not changed, wait a bit longer, and then view the running Pods again.




## Set minimum and maximum resource values

You can set minimum and maximum constraints for the recommendations generated by vertical Pod autoscaling.

###  console 

  1. Go to the **Workloads** page in Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to configure.

  3. Click _list_ **Actions > Autoscale > Vertical pod autoscaling**.

  4. Click _expand_more_ **Add Policy**.

  5. Select the container you want to configure.

  6. Click **Add Rule**.

  7. Enter values for **Min. allowed** and **Max allowed** for CPU and Memory.

  8. Click **Done**.

  9. Click **Save**.




###  gcloud 

To set minimum and maximum resource constraints, include the `resourcePolicy` section in your `VerticalPodAutoscaler` manifest.

  1. Save the following manifest as `my-constrained-vpa.yaml`:
         
         apiVersion: autoscaling.k8s.io/v1
         kind: VerticalPodAutoscaler
         metadata:
           name: my-constrained-vpa
         spec:
           targetRef:
             apiVersion: "apps/v1"
             kind:       Deployment
             name:       my-auto-deployment
           updatePolicy:
             updateMode: "Auto"
           resourcePolicy:
             containerPolicies:
             - containerName: my-container
               minAllowed:
                 cpu: 100m
                 memory: 50Mi
               maxAllowed:
                 cpu: 1000m
                 memory: 1024Mi
         

This configuration helps to ensure that the recommendation for `my-container` won't be lower than 100 mCPU/50 MiB or higher than 1000 mCPU/1024 MiB.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f my-constrained-vpa.yaml
         




## View information about a Vertical Pod Autoscaler

To view details about a Vertical Pod Autoscaler, do the following:

  1. Get detailed information about one of your running Pods:
         
         kubectl get pod POD_NAME --output yaml
         

Replace `POD_NAME` with the name of one of your Pods that you retrieved in the previous step.

The output is similar to the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           annotations:
             vpaUpdates: 'Pod resources updated by my-vpa: container 0: cpu capped to node capacity, memory capped to node capacity, cpu request, memory request'
         ...
         spec:
           containers:
           ...
             resources:
               requests:
                 cpu: 510m
                 memory: 262144k
             ...
         

This output shows that the Vertical Pod Autoscaler controller has a memory request of 262144k and a CPU request of 510 milliCPU.

  2. Get detailed information about the `VerticalPodAutoscaler`:
         
         kubectl get vpa my-vpa --output yaml
         

The output is similar to the following:
         
         ...
           recommendation:
             containerRecommendations:
             - containerName: my-container
               lowerBound:
                 cpu: 536m
                 memory: 262144k
               target:
                 cpu: 587m
                 memory: 262144k
               upperBound:
                 cpu: 27854m
                 memory: "545693548"
         

This output shows recommendations for CPU and memory requests and includes the following properties:

     * `target`: specifies that for the container to run optimally, it should request 587 milliCPU and 26,2144 kilobytes of memory.
     * `lowerBound` and `upperBound`: vertical Pod autoscaling uses these properties to decide whether to delete a Pod and replace it with a new Pod. If a Pod has requests less than the lower bound or greater than the upper bound, the Vertical Pod Autoscaler deletes the Pod and replaces it with a Pod that meets the target attribute.
  3. Check for resize events. If you are using `InPlaceOrRecreate` mode, you can verify if an update happened in-place by checking the events for your Pods:
         
         kubectl get events --field-selector involvedObject.kind=Pod
         

Look for `ResizeCompleted` events, which indicate a successful in-place update:
         
         Reason            Message
         ------            -------
         ResizeCompleted   Pod resize completed: {"containers":[...]}
         




## Opt out specific containers

You can opt out specific containers from vertical Pod autoscaling using the gcloud CLI or the Google Cloud console.

### Console

To opt out specific containers from vertical Pod autoscaling, you must have a cluster with the vertical Pod autoscaling feature enabled. Autopilot clusters have the vertical Pod autoscaling feature enabled by default.

## Enable Vertical Pod Autoscaling

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Details** tab.

  4. In the **Automation** section, click _edit_ **Edit** for the **Vertical Pod Autoscaling** option.

  5. Select the **Enable Vertical Pod Autoscaling** checkbox.

  6. Click **Save changes**.




## Configure Vertical Pod Autoscaling

  1. Go to the **Workloads** page in Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to configure vertical Pod autoscaling for.

  3. Click _list_ **Actions > Edit autoscaling**.

  4. Under the _Vertical Pod Autoscaling section_ , click **Select and configure**.

  5. Under _Update mode_ , choose an autoscaling mode:

     * **Auto mode** : Vertical Pod autoscaling updates CPU and memory requests during the life of a Pod.
     * **Initial mode** : Vertical Pod autoscaling assigns resource requests only at Pod creation and never changes them later.
  6. Click _expand_more_ **Add Policy**.

  7. Select the container you want to opt out.

  8. For **Scaling mode** , select **Off**.

  9. Click **Submit**.




### gcloud

To opt out specific containers from vertical Pod autoscaling, perform the following steps:

  1. Save the following manifest as `my-opt-vpa.yaml`:
         
         apiVersion: autoscaling.k8s.io/v1
         kind: VerticalPodAutoscaler
         metadata:
           name: my-opt-vpa
         spec:
           targetRef:
             apiVersion: "apps/v1"
             kind:       Deployment
             name:       my-opt-deployment
           updatePolicy:
             updateMode: "Recreate"
           resourcePolicy:
             containerPolicies:
             - containerName: my-opt-sidecar
               mode: "Off"
         

This manifest describes a `VerticalPodAutoscaler`. The `mode: "Off"` value turns off recommendations for the container `my-opt-sidecar`.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f my-opt-vpa.yaml
         

  3. Save the following manifest as `my-opt-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-opt-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: my-opt-deployment
           template:
             metadata:
               labels:
                 app: my-opt-deployment
             spec:
               containers:
               - name: my-opt-container
                 image: nginx
               - name: my-opt-sidecar
                 image: busybox
                 command: ["sh","-c","while true; do echo Doing sidecar stuff!; sleep 60; done"]
         

  4. Apply the manifest to the cluster:
         
         kubectl apply -f my-opt-deployment.yaml
         

  5. After some time, view the Vertical Pod Autoscaler:
         
         kubectl get vpa my-opt-vpa --output yaml
         

The output shows recommendations for CPU and memory requests:
         
         ...
           recommendation:
             containerRecommendations:
             - containerName: my-opt-container
         ...
         

In this output, there are only recommendations for one container. There are no recommendations for `my-opt-sidecar`.

The Vertical Pod Autoscaler never updates resources on opted out containers. If you wait a few minutes, the Pod re-creates but only one container has updated resource requests.




## Identify workloads without resource requests or limits

You might want to identify workloads without configured resource requests and limits because GKE recommends setting resource requests and limits for all workloads as a [best practice](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#set_appropriate_resource_requests_and_limits) to avoid abrupt Pod termination under node resource pressure and improve accuracy of cost allocation. Defining [BestEffort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#besteffort) Pods or Pods with [Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable) memory might lead to reliability issues when a node experiences [memory pressure](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#node-conditions). Use the following best practices for setting your container resource requests and limits:

  * **Memory** : Set the same amount of memory for the request and limit.
  * **CPU** : For the request, specify the minimum CPU needed to ensure correct operation, according to your own SLOs. Set an unbounded CPU limit.



GKE generates insights and recommendations for workloads running without resource requests and limits.

The following table describes the resource configuration scenarios that GKE detects and the criteria for each scenario.

Insight subtype | Missing settings scenario | Details  
---|---|---  
`REQUEST_OR_LIMIT_NOT_SET` |  No configured memory request and limit. (`MEMORY_REQUEST_AND_LIMIT_NOT_SET`)  |  Pods are running without memory requests and limits set for their containers. GKE cannot throttle memory usage and might abruptly terminate such Pods if a node experiences memory pressure, which might cause reliability issues.   
`REQUEST_OR_LIMIT_NOT_SET` |  No configured memory limits. (`MEMORY_LIMIT_NOT_SET`)  |  Pods are running without memory limits set for their containers. GKE cannot throttle memory usage and might abruptly terminate such Pods if a node experiences memory pressure and the Pods' memory usage exceeds requests, which might cause reliability issues. You should set the same amount of memory for requests and limits to avoid Pods using more memory than requested.   
`REQUEST_OR_LIMIT_NOT_SET` |  No configured CPU request and limit. (`CPU_REQUEST_AND_LIMIT_NOT_SET`)  |  Pods are running without CPU requests and limits set for containers. This increases the chances of node resource exhaustion, makes Pods more likely to be throttled when node CPU utilization is close to its limit, and might cause performance issues.   
  
For more information about these insights, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

## Manually check resource requests and limits

You might want to manually review which resource requests and limits are missing and need to be specified for a given workload so that you can update the configuration as recommended.

To review or update resource requests and limits configuration for a specified workload, do the following:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the workload you want to inspect.

  3. Click _list_ **Actions > Scale > Edit resource requests**.

     1. The **Adjust resource requests and limits** section shows the current CPU and memory requests for each container.



## What's next

  * Learn more about [Vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).
  * Learn how to [troubleshoot vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vertical-pod-autoscaling).
  * Learn [best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#vertical_pod_autoscaler).
  * Learn how to [optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).
  * Learn how to [accelerate application startup with CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
