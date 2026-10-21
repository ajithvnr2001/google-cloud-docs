---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps/
title: Scaling an application \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:17.254117+00:00
---

# Scaling an application  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scaling an application Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) lets you scale [deployed applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) to respond to traffic fluctuations and optimize cluster resource utilization. By adjusting application capacity, you can maintain availability during peak demand while reducing compute costs when demand drops.

In GKE, each application _replica_ runs as a Kubernetes Pod that encapsulates your application's containers. You can scale applications using two methods:

  * [Horizontal scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler): Increase or decrease the number of workload replicas.
  * [Vertical scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler): Adjust the CPU and memory resources available to existing replicas in-place.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Inspecting an application

Before scaling your application, you should inspect the application and ensure that it is healthy.

To see all applications deployed to your cluster, run the following command:
    
    
    kubectl get CONTROLLER
    

Substitute `CONTROLLER` for `deployments`, `statefulsets`, or another controller object type.

For example, if you run `kubectl get deployments` and you have created only one Deployment, the command's output should look similar to the following:
    
    
    NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
    my-app                 1/1        1           1        10m
    

The output of this command is similar for all objects, but may appear slightly different. For Deployments, the output has five columns:

  * `NAME` lists the names of the Deployments in the cluster.
  * `READY` displays the number of running replicas that are ready, formatted as _ready replicas_ / _desired replicas_. You define the desired state when you create the Deployment.
  * `UP-TO-DATE` displays the number of replicas that have been updated to achieve
  * `AVAILABLE` displays how many replicas of the application are available to your users.
  * `AGE` displays the amount of time that the application has been running in the cluster.



In this example, there is only one Deployment, `my-app`, which has only one replica because its desired state is one replica. You define the desired state at the time of creation, and you can change it at any time by scaling the application.

## Inspecting StatefulSets

Before scaling a StatefulSet, you should inspect it by running the following command:
    
    
    kubectl describe statefulset my-app
    

In the output of this command, check the **Pods Status** field. If the `Failed` value is greater than `0`, scaling might fail.

If a StatefulSet appears to be unhealthy, perform the following:

  1. Get a list of pods, and see which pods are unhealthy:
         
         kubectl get pods
         

  2. Remove the unhealthy pod:
         
         kubectl delete pod POD_NAME
         




Attempting to scale a StatefulSet while it is unhealthy may cause it to become unavailable.

## Scaling an application

The following sections describe each method you can use to scale an application. The `kubectl scale` method is the fastest way to scale. However, you may prefer another method in some situations, like when updating configuration files or when performing in-place modifications.

### kubectl scale

The [`kubectl scale`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale) command lets your instantaneously change the number of replicas you want to run your application.

To use `kubectl scale`, you specify the new number of replicas by setting the `--replicas` flag. For example, to scale `my-app` to four replicas, run the following command, substituting `CONTROLLER` for `deployment`, `statefulset`, or another controller object type:
    
    
    kubectl scale CONTROLLER my-app --replicas 4
    

If successful, this command's output should be similar to `deployment "my-app" scaled`.

Next, run:
    
    
    kubectl get CONTROLLER my-app
    

The output should look similar to the following:
    
    
    NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
    my-app                4/4         4            4       15m
    

**Note:** It may take several minutes for scaling to complete.

### kubectl patch

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Starting in [Kubernetes version 1.33](https://opensource.googleblog.com/2025/05/kubernetes-1.33-available-on-gke.html), you can use the [`kubectl patch`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#patch) command to vertically scale your workload by updating the resources that are assigned to a container, without recreating the Pod. For more information, including limitations, see the [Kubernetes documentation for resizing CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources).

To use the `kubectl patch` command, specify the updated resource request under the `--patch` flag. For example, to scale `my-app` to 800 mCPUs, run the following command:
    
    
    kubectl patch pod my-app --subresource resize --patch \
      '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"800m"}, "limits":{"cpu":"800m"}}}]}}'
    

### kubectl apply

You can use [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) to apply a new configuration file to an existing controller object. `kubectl apply` is useful for making multiple changes to a resource, and may be useful for users who prefer to manage their resources in configuration files.

To scale using `kubectl apply`, the configuration file you supply should include a new number of replicas in the `replicas` field of the object's specification.

The following is an updated version of the configuration file for the example `my-app` object. The example shows a Deployment, so if you use another type of controller, such as a StatefulSet, change the `kind` accordingly. This example works best on a cluster with at least three Nodes.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: app
      template:
        metadata:
          labels:
            app: app
        spec:
          containers:
          - name: my-container
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0
    

In this file, the value of the `replicas` field is `3`. When this configuration file is applied, the object `my-app` scales to three replicas.

To apply an updated configuration file, run the following command:
    
    
    kubectl apply -f config.yaml
    

Next, run:
    
    
    kubectl get CONTROLLER my-app
    

The output should look similar to the following:
    
    
    NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
    my-app                3/3         3            3       15m
    

### Console

To scale a workload in the Google Cloud console, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the workload you want to scale.

  3. Click _list_ **Actions > Scale > Edit replicas**.

  4. Enter the new number of **Replicas** for the workload.

  5. Click **Scale**.




You can view metrics related to scaling by clicking the **Scaling** tab.

## Autoscaling Deployments

You can autoscale Deployments based on CPU utilization of Pods using `kubectl autoscale` or from the GKE Workloads menu in the Google Cloud console.

### kubectl autoscale

[`kubectl autoscale`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale) creates a `HorizontalPodAutoscaler` (or HPA) object that targets a specified resource (called the _scale target_) and scales it as needed. The HPA periodically adjusts the number of replicas of the scale target to match the average CPU utilization that you specify.

**Note:** Your object's Pod template can include a `resources` field that specifies a CPU utilization request for each Pod. To learn more about making resource requests for Pods and containers, refer to [Managing resources for containers](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/).

When you use `kubectl autoscale`, you specify a maximum and minimum number of replicas for your application, as well as a CPU utilization target. For example, to set the maximum number of replicas to six and the minimum to four, with a CPU utilization target of 50% utilization, run the following command:
    
    
    kubectl autoscale deployment my-app --max 6 --min 4 --cpu-percent 50
    

In this command, the `--max` flag is required. The `--cpu-percent` flag is the target CPU utilization over all the Pods. This command _does not_ immediately scale the Deployment to six replicas, unless there is already a systemic demand.

After running `kubectl autoscale`, the `HorizontalPodAutoscaler` object is created and targets the application. When there is a change in load, the object increases or decreases the application's replicas.

**Note:** The maximum number of replicas is limited by the cluster's resources. If the cluster has a static number of available nodes, the cluster might run out of resources and prevent some replicated Pods from running. To learn about scaling your cluster, refer to [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-container-cluster) and [Cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

To get a list of the `HorizontalPodAutoscaler` objects in your cluster, run:
    
    
    kubectl get hpa
    

To see a specific `HorizontalPodAutoscaler` object in your cluster, run:
    
    
    kubectl get hpa HPA_NAME
    

Replace `HPA_NAME` with the name of your `HorizontalPodAutoscaler` object.

To see the `HorizontalPodAutoscaler` configuration:
    
    
    kubectl get hpa HPA_NAME -o yaml
    

The output of this command is similar to the following:
    
    
    apiVersion: autoscaling/v1
    kind: HorizontalPodAutoscaler
    metadata:
      creationTimestamp: ...
      name: HPA_NAME
      namespace: default
      resourceVersion: "664"
      selfLink: ...
      uid: ...
    spec:
      maxReplicas: 10
      minReplicas: 1
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: HPA_NAME
      targetCPUUtilizationPercentage: 50
    status:
      currentReplicas: 0
      desiredReplicas: 0
    

In this example output, the `targetCPUUtilizationPercentage` field holds the `50` percentage value passed in from the `kubectl autoscale` example.

To see a detailed description of a specific `HorizontalPodAutoscaler` object in the cluster:
    
    
    kubectl describe hpa HPA_NAME
    

You can modify the `HorizontalPodAutoscaler` by applying a new configuration file with `kubectl apply`, using `kubectl edit`, or using `kubectl patch`.

To delete a `HorizontalPodAutoscaler` object:
    
    
    kubectl delete hpa HPA_NAME
    

### Console

To autoscale a Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the Deployment you want to autoscale.

  3. Click _list_ **Actions > Edit autoscaling**.

  4. Under the _Horizontal Pod Autoscaling section_ , enter the **Maximum number of replicas** and, optionally, the **Minimum number of replicas** for the Deployment.

  5. (Optional) Under **Autoscaling metrics** , select and configure metrics.

  6. Click **Submit**.




You can view metrics related to scaling by clicking the **Scaling** tab.

### Autoscaling with custom or external metrics

In addition to scaling based on resources such as CPU and memory, you can also [scale based on custom or external metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics). This includes metrics stored in Cloud Monitoring, but in certain cases, can also bypass an external monitoring system.

**Note:** Cloud Monitoring is a Google Cloud service separate from GKE. To use scaling based on custom metrics, you need to associate a paid Google Cloud Observability service account with your Google Cloud console project. For more information, refer to the [Google Cloud Observability for GKE documentation](https://docs.cloud.google.com/stackdriver/docs/solutions/gke).

## What's next

  * [Accelerate application startup using CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).
  * [Scale container resource requests and limits (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling).
  * [Configuring horizontal Pod autoscaling (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
