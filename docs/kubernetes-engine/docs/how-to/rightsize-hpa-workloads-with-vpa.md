---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa/
title: Rightsize HPA workloads with VPA \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:09.363938+00:00
---

# Rightsize HPA workloads with VPA  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Rightsize HPA workloads with VPA Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to use HPA rightsizing with the Vertical Pod Autoscaler (VPA) and the Horizontal Pod Autoscaler (HPA) to automatically optimize container CPU requests and limits while scaling workload replicas in Google Kubernetes Engine (GKE).

Traditionally, using the [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) (HPA) and [Vertical Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) (VPA) together on the same metric, such as CPU, creates scaling conflicts. This conflict occurs because when VPA sets Pod CPU requests, it alters the usage baseline that HPA sets, which can lead to unexpected scaling behavior and over-provisioning.

HPA rightsizing with VPA enables both autoscalers to operate cooperatively on the same workload. HPA continues to handle short-term traffic spikes by scaling the number of Pod replicas. Meanwhile, VPA uses rightsizing logic to consider the workload's aggregated historical resource demand over time. It factors in your HPA configuration (such as minimum replicas, maximum replicas, and target CPU utilization) to adjust container CPU requests so that the workload remains cost-effective during low traffic and resilient during high demand.

## Resource handling and scale limits

When configuring HPA rightsizing, consider the following requirements and limitations:

  * Rightsizing calculations apply only to CPU. If you include memory in your VPA configuration, VPA resizes memory requests and limits by using standard VPA logic.
  * You can configure HPA rightsizing for up to 60,000 total containers across all workloads in a single cluster.
  * A single VerticalPodAutoscaler can target up to 1,000 containers.
  * VPA generates recommendations for, and applies updates on, only container-level resource requests and limits (`spec.containers[].resources`). Vertical Pod autoscaling doesn't support [Pod-level resource specifications](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#pod-level-resource-specification) (`spec.resources`).



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Google Kubernetes Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Google Kubernetes Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin, roles/container.developer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. Verify that your cluster runs GKE version `1.36.3-gke.1630000` or later.
  16. Verify that vertical Pod autoscaling is enabled on your cluster. Vertical Pod autoscaling is enabled by default on Autopilot clusters. To create a new Autopilot cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#create_an_autopilot_cluster).

If you are using a Standard cluster, enable vertical Pod autoscaling by running one of the following commands:

     * To create a new Standard cluster with vertical Pod autoscaling enabled, run the following command: 
           
           gcloud container clusters create CLUSTER_NAME \
                   --enable-vertical-pod-autoscaling \
                   --location=LOCATION
               

     * To enable vertical Pod autoscaling on an existing Standard cluster, run the following command: 
           
           gcloud container clusters update CLUSTER_NAME \
                   --enable-vertical-pod-autoscaling \
                   --location=LOCATION
               

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the Compute Engine region or zone of your cluster, for example `us-central1-a`.



## Deploy a workload with HPA and VPA rightsizing

To configure HPA rightsizing with VPA, you deploy your workload, create a HorizontalPodAutoscaler targeting CPU utilization, and configure a VerticalPodAutoscaler with the rightsizing policy annotation.

To give the vertical Pod autoscaler time to gather usage data and build accurate recommendations without modifying running Pods, use a phased deployment approach:

  1. Deploy your workload and configure HPA.
  2. Deploy the VerticalPodAutoscaler with the `updateMode` field set to `"Off"` to observe recommendations. You can skip this step for new workloads or workloads that aren't production-critical.
  3. After several days of observation, update the `updateMode` field to `"InPlaceOrRecreate"` or `"Recreate"` to enable automated rightsizing. VPA generates initial recommendations within a few minutes, but observing for at least 24 hours to several days lets VPA capture full traffic cycles.



### Deploy the example workload and HPA

  1. Save the following sample Deployment manifest as `sample-app.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: sample-app
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: sample-app
           template:
             metadata:
               labels:
                 app: sample-app
             spec:
               containers:
               - name: sample-app
                 image: nginx
                 resources:
                   requests:
                     cpu: 250m
                     memory: 256Mi
         

  2. Apply the manifest to your cluster by running the following command:
         
         kubectl apply -f sample-app.yaml
         

  3. Save the following HorizontalPodAutoscaler manifest as `sample-app-hpa.yaml`:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: sample-app-hpa
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: sample-app
           minReplicas: 2
           maxReplicas: 10
           metrics:
           -   type: Resource
             resource:
               name: cpu
               target:
                 type: Utilization
                 averageUtilization: 70
         

  4. Apply the HPA manifest to your cluster by running the following command:
         
         kubectl apply -f sample-app-hpa.yaml
         




### Observe recommendations in Off mode

To let the VerticalPodAutoscaler object analyze historical resource demand and generate recommendations without resizing Pods, deploy it in Off mode. You can skip this section for new workloads or workloads that aren't production-critical, and instead deploy the VerticalPodAutoscaler with the `updateMode` field set to `"InPlaceOrRecreate"` or `"Recreate"`.

  1. Save the following manifest as `sample-app-vpa.yaml`:
         
         apiVersion: autoscaling.k8s.io/v1
         kind: VerticalPodAutoscaler
         metadata:
           name: sample-app-vpa
           annotations:
             gke.io/autoscaling-hpa-rightsizing-mode: "gke-hpa-rightsizing-mode-policy"
         spec:
           targetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: sample-app
           updatePolicy:
             updateMode: "Off"
           resourcePolicy:
             containerPolicies:
             - containerName: sample-app
               controlledResources: ["cpu", "memory"]
               minAllowed:
                 cpu: 100m
                 memory: 200Mi
               maxAllowed:
                 cpu: 1000m
                 memory: 1024Mi
         

This manifest configures the following key settings:

     * `metadata.annotations` field: contains `gke.io/autoscaling-hpa-rightsizing-mode: "gke-hpa-rightsizing-mode-policy"` to enable HPA rightsizing.
     * `spec.updatePolicy.updateMode` field: set to `"Off"` to generate recommendations without updating container resource requests.
     * `spec.resourcePolicy.containerPolicies[].controlledResources` field: specifies `"cpu"` (and optionally `"memory"`).
     * `spec.resourcePolicy.containerPolicies[].minAllowed` and `maxAllowed` fields: define boundary constraints to prevent VPA from resizing the container outside your chosen resource limits.
  2. Apply the VPA manifest by running the following command:
         
         kubectl apply -f sample-app-vpa.yaml
         

  3. Let your workload run under typical traffic patterns for several days so that VPA can collect enough metrics to generate high-confidence recommendations. VPA generates initial recommendations within a few minutes of deploying the VerticalPodAutoscaler and refines them as it collects metrics across your workload's traffic cycles.




### Enable automated rightsizing

After observing recommendations and confirming that they fit your application requirements, enable automatic rightsizing.

  1. In `sample-app-vpa.yaml`, update the `spec.updatePolicy.updateMode` field to `"InPlaceOrRecreate"`:
         
         ...other fields omitted for clarity...
         spec:
           updatePolicy:
             updateMode: "InPlaceOrRecreate"
         

The `"InPlaceOrRecreate"` mode updates CPU requests non-disruptively without restarting Pods. If your workload also manages memory and your application runtime requires a restart to apply memory changes, [add `resizePolicy` to your container spec](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-policies) (`restartPolicy: RestartContainer` for memory). Alternatively, set `updateMode: "Recreate"` to recreate Pods on every resource update.

  2. Apply the updated manifest by running the following command:
         
         kubectl apply -f sample-app-vpa.yaml
         




VPA automatically adjusts the CPU requests of your containers to optimal levels based on workload demand, and HPA continues to scale the number of replicas dynamically.

## Configure rightsizing for multi-container workloads

If your workload runs multiple containers in each Pod (such as a primary application container and one or more sidecars), configure the HPA to scale based on the primary container's CPU utilization rather than the total Pod utilization. This configuration helps ensure that HPA and VPA evaluate resource demands by using the same container baseline.

To target a specific container in your HorizontalPodAutoscaler, use the `ContainerResource` metric type in the `autoscaling/v2` API:
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: multi-container-hpa
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: multi-container-app
      minReplicas: 2
      maxReplicas: 10
      metrics:
      -   type: ContainerResource
        containerResource:
          name: cpu
          container: PRIMARY_CONTAINER_NAME
          target:
            type: Utilization
            averageUtilization: 70
    

Replace `PRIMARY_CONTAINER_NAME` with the name of your primary application container.

## Verify recommendations

To inspect the recommendations generated by VPA, run the following command:
    
    
    kubectl describe vpa VPA_NAME
    

Replace `VPA_NAME` with the name of your VerticalPodAutoscaler, for example, `sample-app-vpa`.

The output includes a "Recommendation" section similar to the following:
    
    
    Recommendation:
      Container Recommendations:
        Container Name:  sample-app
        Lower Bound:
          Cpu:     100m
          Memory:  200Mi
        Target:
          Cpu:     350m
          Memory:  256Mi
        Uncapped Target:
          Cpu:     350m
          Memory:  256Mi
        Upper Bound:
          Cpu:     1
          Memory:  1024Mi
    

In this output, look for the following fields:

  * `Target`: the recommended CPU and memory requests that VPA applies when automated updates are enabled.
  * `Lower Bound`: the minimum resource request recommendation calculated by VPA.
  * `Upper Bound`: the maximum resource request recommendation calculated by VPA.
  * `Uncapped Target`: the raw recommendation calculated by VPA before applying `minAllowed` or `maxAllowed` constraints.



For more detailed diagnostic logs, you can view VPA decision logs in Cloud Logging. For instructions, see [View vertical Pod autoscaling events and decision logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events).

## Best practices and considerations

When using HPA rightsizing with VPA, consider the following best practices:

  * If you use continuous delivery tools such as Argo CD, the tool might attempt to revert the resource changes made by VPA back to the manifest values. Some tools support configuring settings that ignore these types of changes, for example Argo CD has the [`ignoreDifferences` attribute](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/).
  * For workloads that experience heavy CPU spikes during initial startup (such as Java applications), you can combine rightsizing with [VPA CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup) to temporarily allocate extra CPU during startup without impacting steady-state rightsizing calculations.
  * To disable HPA rightsizing on a workload, delete the VerticalPodAutoscaler or set the `spec.updatePolicy.updateMode` field to `"Off"`. Don't remove only the `gke.io/autoscaling-hpa-rightsizing-mode` annotation and leave the `updateMode` field set to `"InPlaceOrRecreate"` or `"Recreate"`. Removing only the annotation reverts VPA to standard VPA behavior, which can cause HPA and VPA to compete and create scaling instability.



## What's next

  * Learn more about [Horizontal Pod Autoscaler concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).
  * Learn more about [Vertical Pod Autoscaler concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).
  * Learn how to [view vertical Pod autoscaling events and decision logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
