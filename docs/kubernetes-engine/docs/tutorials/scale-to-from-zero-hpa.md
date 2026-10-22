---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa/
title: Scale GKE workloads to and from zero using HPA \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:52.704403+00:00
---

# Scale GKE workloads to and from zero using HPA  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scale GKE workloads to and from zero using HPA Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to optimize resource utilization in Google Kubernetes Engine (GKE) by configuring workloads to automatically scale to zero replicas when idle, and scale back up as demand increases. This approach integrates the [horizontal Pod autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) with GKE's managed autoscaling infrastructure to manage scaling based on external metrics.

Configure your deployment to scale to zero by setting the value of the `minReplicas` field to `0` and defining a metric with the `External` or `Object` type within your HPA manifest. GKE monitors these metrics through the [AutoscalingMetric](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics) custom resource, which helps ensure efficient resource management for your applications.

With this configuration, you don't need to use third-party metrics adapters, such as KEDA, to scale GKE workloads. This solution manages metric ingestion and scaling recommendations directly in the GKE control plane, reducing cluster management overhead.

In this tutorial, you deploy an example asynchronous worker application that processes messages from a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) queue. You configure a horizontal Pod autoscaler to monitor the queue depth (`pubsub.googleapis.com:num_undelivered_messages`) using an `AutoscalingMetric` custom resource:

  * **When messages arrive in the subscription:** GKE scales up worker Pods to process the queue.
  * **When the queue is empty:** GKE automatically scales the worker Deployment down to zero replicas.



This tutorial is for Application developers, Platform admins and operators, and DevOps who want to optimize resource usage in GKE by scaling workloads to zero when they are idle.

## Considerations

Before configuring workloads to scale to zero, review the following considerations:

  * Scaling workloads to and from zero using HPA requires GKE cluster control plane and nodes to run version 1.37 or later in both new and upgraded existing clusters. If you use an existing cluster, verify its version or [upgrade your cluster or its nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to version 1.37 or later.
  * Your HPA manifest must use the `apiVersion: autoscaling/v2` configuration to support the `minReplicas: 0` setting and external metrics.
  * Before [downgrading node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes) to a version earlier than 1.37, update any HPA manifests configured to scale to and from zero by setting the `minReplicas` field to `1` or greater. Versions earlier than 1.37 don't support the `minReplicas: 0` setting, which can cause workloads to remain stuck at zero replicas.
  * You must configure at least one `External` or `Object` metric (such as a queue depth) in your horizontal Pod autoscaler. GKE cannot collect CPU or memory (`Resource`) metrics when a workload has zero Pods, so resource metrics alone cannot trigger scaling up from zero.
  * The AutoscalingMetric, HorizontalPodAutoscaler, and target Deployment must reside in the same Kubernetes namespace.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  7. Enable the GKE and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com pubsub.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  13. Enable the GKE and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com pubsub.googleapis.com




### Required roles

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [GKE Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`)
  * [Pub/Sub Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up your environment

For simplicity, the commands in this tutorial create all resources (the GKE cluster, and the Pub/Sub topic and subscription) within a single Google Cloud project (`PROJECT_ID`).

To set up your environment, follow these steps:

  1. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format 'get(projectNumber)')
         export LOCATION=LOCATION
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `LOCATION`: the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to create your GKE cluster, such as `us-central1`. For Autopilot clusters, specify a region.
**Note:** These environment variables are used throughout this tutorial. If you open a new shell session or disconnect, run these commands again to set the variables.
  2. Create a GKE cluster running version 1.37 or later with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enabled. We recommend that you use an Autopilot cluster for a fully managed Kubernetes experience and to maximize cost savings when workloads scale to zero. To choose the mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode):

### Autopilot

Create an Autopilot cluster:
         
         gcloud container clusters create-auto scale-to-zero \
             --project=${PROJECT_ID} \
             --location=${LOCATION}
         

Workload Identity Federation for GKE is enabled by default on Autopilot clusters.

### Standard

Create a Standard cluster with Workload Identity Federation for GKE enabled:
         
         gcloud container clusters create scale-to-zero \
             --project=${PROJECT_ID} \
             --location=${LOCATION} \
             --workload-pool=${PROJECT_ID}.svc.id.goog
         

  3. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials scale-to-zero \
             --project=${PROJECT_ID} \
             --location=${LOCATION}
         




### Create Pub/Sub resources

This tutorial uses Pub/Sub queue depth as an example external metric source.

To create a Pub/Sub topic and subscription, follow these steps:

  1. Create a Pub/Sub topic:
         
         gcloud pubsub topics create my-worker-topic \
             --project=${PROJECT_ID}
         

  2. Create a subscription attached to the topic:
         
         gcloud pubsub subscriptions create my-worker-subscription \
             --topic=my-worker-topic \
             --project=${PROJECT_ID}
         




### Set up Workload Identity Federation for GKE

Configure Workload Identity Federation for GKE to allow your worker application to authenticate with Google Cloud APIs and consume messages from Pub/Sub.

GKE automatically handles authentication with Cloud Monitoring for AutoscalingMetric resources in the same project. To learn more about defining metrics for autoscaling, see [Fetch custom or external metrics from Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics#define-custom-metrics-promql).

To configure Workload Identity Federation for GKE for your worker workload, follow these steps:

  1. Create a Kubernetes service account for your worker application in the `default` namespace:
         
         kubectl create serviceaccount async-worker-sa \
             --namespace default
         

  2. Grant the `roles/pubsub.subscriber` role to the Kubernetes service account so the application can receive messages from your Pub/Sub subscription:
         
         gcloud projects add-iam-policy-binding projects/${PROJECT_ID} \
             --role=roles/pubsub.subscriber \
             --member=principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/async-worker-sa
         




For more information, see [Configure applications to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).

### Create the example Deployment

Before you can create an HPA object, you must create the workload it will monitor.

To create the example Deployment, follow these steps:

  1. Save the following manifest as `async-worker.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: async-worker
           namespace: default
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: async-worker
           template:
             metadata:
               labels:
                 app: async-worker
             spec:
               containers:
               - name: async-worker
                 image: nginx:latest
                 ports:
                 - containerPort: 80
                 resources:
                   limits:
                     memory: 100Mi
                   requests:
                     cpu: 50m
                     memory: 100Mi
         

  2. Apply the `async-worker.yaml` Deployment:
         
         kubectl apply -f async-worker.yaml
         




## Configure a workload to scale to and from zero

In this section, you configure the `async-worker` Deployment to scale down to zero when the Pub/Sub queue is empty, and scale back up as new messages arrive.

### Create the AutoscalingMetric resource

To define the external signal monitored by GKE, create the AutoscalingMetric custom resource. In the following example manifest, the metric queries Cloud Monitoring for the number of undelivered Pub/Sub messages on the `my-worker-subscription` subscription.

To create the AutoscalingMetric resource, follow these steps:

  1. Save the following manifest as the `pubsub-metric.yaml` file:
         
         apiVersion: autoscaling.gke.io/v1beta1
         kind: AutoscalingMetric
         metadata:
           name: pubsub-queue-depth
           namespace: default
         spec:
           metrics:
           - promql:
               name: pubsub-undelivered
               query: >
                   {
                     "pubsub.googleapis.com/subscription/num_undelivered_messages",
                     subscription_id="my-worker-subscription"
                   }
         

  2. Apply the `pubsub-metric.yaml` manifest:
         
         kubectl apply -f pubsub-metric.yaml
         

  3. Verify the metric status and retrieve the metric identifier:
         
         kubectl describe autoscalingmetric pubsub-queue-depth
         

In the `Status` section of the output, verify that no errors are listed and note the `Hpa Name` value that's in the `autoscaling.gke.io|CUSTOM_RESOURCE_NAME|METRIC_NAME` format. You'll reference this external metric identifier when you create the HorizontalPodAutoscaler object in the next section. If the `Status` section reports configuration errors or metrics are not retrieved as expected, see [Troubleshoot metrics that are fetched for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics#troubleshoot).




### Configure the horizontal Pod autoscaler

To configure autoscaling behavior, create a HorizontalPodAutoscaler resource targeting the Deployment.

To configure the horizontal Pod autoscaler, follow these steps:

  1. Save the following manifest as the `worker-hpa.yaml` file:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: async-worker-hpa
           namespace: default
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: async-worker
           minReplicas: 0
           maxReplicas: 20
           metrics:
           - type: External
             external:
               metric:
                 name: autoscaling.gke.io|pubsub-queue-depth|pubsub-undelivered
               target:
                 type: AverageValue
                 averageValue: "10"
         

This manifest configures the following key fields:

     * `minReplicas: 0`: enables scale-to-zero by allowing the controller to scale the Deployment down to `0` replicas when demand drops to zero.
     * `type: External`: configures an external metric source so the HPA can trigger scale-up when the workload has zero Pods.
     * `name: autoscaling.gke.io|pubsub-queue-depth|pubsub-undelivered`: maps the HPA directly to the AutoscalingMetric resource created in the previous step by using the `autoscaling.gke.io|CUSTOM_RESOURCE_NAME|METRIC_NAME` identifier format.
  2. Apply the `worker-hpa.yaml` manifest:
         
         kubectl apply -f worker-hpa.yaml
         




## Verify zero-scale behavior and conditions

When all messages in the Pub/Sub subscription are processed, the horizontal Pod autoscaler evaluates the zero demand and scales the Deployment down to `0` replicas.

To verify that the horizontal Pod autoscaler actuated the zero state, inspect the status conditions of the `async-worker-hpa` resource by running the following command:
    
    
    kubectl describe hpa async-worker-hpa
    

The output is similar to the following:
    
    
    Name:             async-worker-hpa
    Namespace:        default
    Reference:        Deployment/async-worker
    Metrics:          ( current / target )
      "autoscaling.gke.io|pubsub-queue-depth|pubsub-undelivered" (external metric):  0 / 10
    Min replicas:     0
    Max replicas:     20
    Deployment pods:  0 current / 0 desired
    Conditions:
      Type            Status  Reason               Message
      ----            ------  ------               -------
      AbleToScale     True    SucceededGetScale    the HPA controller was able to get the target's current scale
      ScalingActive   True    ValidMetricFound     the HPA was able to successfully calculate a replica count from external metric
      ScaledToZero    True    ScaledToZero         the HPA has scaled the target resource to 0 replicas due to zero metric demand
    

### Understand the `ScaledToZero` condition

The `ScaledToZero` condition indicates whether the horizontal Pod autoscaler has scaled the workload to zero replicas:

  * **`ScaledToZero: True` (`Reason: ScaledToZero`)**: indicates that the HPA controller successfully scaled your workload to `0` replicas because external metric demand dropped to zero. The HPA remains active (`ScalingActive: True`) and continuously polls GKE to detect when workload demand increases.
  * **`ScaledToZero: False`** : indicates that the workload has scaled up to one or more replicas.



If you manually scale a Deployment to zero replicas, for example, with the `kubectl scale --replicas=0` command, the HPA pauses autoscaling (`ScalingActive: False`) to prevent conflicting changes. To resume autoscaling, scale the deployment back to one or more replicas (`kubectl scale deployment async-worker --replicas=1`).

For troubleshooting scenarios where workloads fail to scale to zero or fail to scale up from zero, see [Troubleshoot scaling GKE workloads to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling#troubleshoot-scale-to-from-zero-hpa). If the horizontal Pod autoscaler reports missing or invalid external metrics, see [Troubleshoot metrics that are fetched for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics#troubleshoot).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, follow these steps:

  1. Delete the GKE cluster:
         
         gcloud container clusters delete scale-to-zero \
             --project=${PROJECT_ID} \
             --location=${LOCATION}
         

  2. Delete the Pub/Sub subscription and topic:
         
         gcloud pubsub subscriptions delete my-worker-subscription \
             --project=${PROJECT_ID}
         gcloud pubsub topics delete my-worker-topic \
             --project=${PROJECT_ID}
         




## What's next

  * Learn how to mitigate cold-start latency by using [GKE Capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).
  * Learn how to [diagnose scaling issues when scaling to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling#troubleshoot-scale-to-from-zero-hpa).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
