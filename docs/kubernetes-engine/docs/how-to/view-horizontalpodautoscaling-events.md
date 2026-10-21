---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events/
title: Collect horizontal Pod autoscaler event logs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:56.821927+00:00
---

# Collect horizontal Pod autoscaler event logs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect horizontal Pod autoscaler event logs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides information about decision events emitted by the [horizontal Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) in Google Kubernetes Engine (GKE). By analyzing these events, you can both gain insights into how the horizontal Pod autoscaler controller manages your workload scaling and understand the decision-making process behind its actions.

The horizontal Pod autoscaler emits decision events, which are stored as log entries in Cloud Logging.

## Before you begin

Make sure to complete the following prerequisites:

### Select or create a project

You can use an existing project, or create a new one for this tutorial.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Enable the APIs

Enable the GKE, and Cloud Logging APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,logging.googleapis.com)

### Set up Cloud Shell

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run `gcloud` and `kubectl` commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line tool.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

A Cloud Shell session opens inside a frame lower on the console.

Before you run commands in this tutorial, make sure that your default project is set to the project ID where you want to deploy the sample app. If it's not already set, run the following command in the Cloud Shell:
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

### Required roles and permissions

To get the permissions that you need to enable log generation, and to access and process logs, ask your administrator to grant you the following IAM roles on the project: 

  * To enable horizontal Pod autoscaler event logging in your cluster: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 
  * To access logs and to use Logs Explorer and Observability Analytics: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Requirements

  * Your GKE cluster must be running version `1.31.5-gke.1090000` or later, or `1.32.1-gke.1260000` or later.
  * Enable Cloud Logging in your GKE cluster. The [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing) applies.
  * Ensure you have a [horizontal Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) that you want to monitor. Ensure that the horizontal Pod autoscaler fields don't include sensitive data.



### Costs

[Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing) applies when you enable Cloud Logging and collect horizontal Pod autoscaler decision logs.

## Enable horizontal Pod autoscaler decision events

**Caution:** Existing clusters might have specific logging components already configured. When you update an existing cluster using the Google Cloud CLI, or an API call, you must include the existing logging configuration in your update request to avoid overwriting the existing configurations.**Note:** If you choose to send logs to Cloud Logging, you must send system logs. Make sure to enable the system logs component when you enable logs from additional sources, such as `KCP_HPA`.

### gcloud

To create a new cluster with the `KCP_HPA` decision logs enabled, run the following command: 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--logging =SYSTEM,KCP_HPA**
    

To enable the `KCP_HPA` decision logs on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--logging =SYSTEM,KCP_HPA**
    

Replace the following:

  * `CLUSTER_NAME`: name of the cluster you want to create or update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: [Compute regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster. 



### Terraform

To enable `KCP_HPA` decision logs by using Terraform, update your `google_container_cluster` resource. In the `logging_config` block, add the `KCP_HPA` value to the list for the `enable_components` field: 
    
    
    resource "google_container_cluster" "primary" {
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other configuration ...
    
      logging_config {
        enable_components = ["SYSTEM_COMPONENTS", "KCP_HPA"]
      }
    }
    

Replace the following:

  * `CLUSTER_NAME`: name of the cluster you want to create.
  * `LOCATION`: [Compute region or zone](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster. 



These commands enable exporting the logs generated by `KCP_HPA` and save them at the destination `logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fhpa-controller"` within Cloud Logging.

Retrieve the updated logging configuration of the cluster and review the list of logs to make sure that the `KCP_HPA` log is enabled:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=loggingConfig \
        --format='csv[delimiter=",",no-heading](componentConfig.enableComponents)'
    

The output is similar to the following:
    
    
    SYSTEM_COMPONENTS,APISERVER,CONTROLLER_MANAGER,SCHEDULER,KCP_HPA
    

### View horizontal Pod autoscaler logs in the Google Cloud console

You can monitor the behavior of the horizontal Pod autoscaler in the Google Cloud console. This view provides a convenient way to see the same atomic and final recommendation logs that are available in Cloud Logging, without leaving the context of your workload.

To view horizontal Pod autoscaler logs in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Workloads** page:

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the workload that is being managed by the horizontal Pod autoscaler.

  3. Click the **Scaling** tab.




On this tab, you can find information related to scaling, including resource usage, efficiency data, and logs. The data on this tab can help you identify the most effective configuration for autoscaling your workloads. In the _Logs_ section, you can find the same information from the **Logs** and filter these logs by kind, including "Event", "Final recommendation", and "Atomic recommendation". For more details about the different logs, see Types of Logs.

## Disable horizontal Pod autoscaler decision events

**Caution:** Existing clusters might have specific logging components already configured. When you update an existing cluster using the Google Cloud CLI, or an API call, you must include the existing logging configuration in your update request to avoid overwriting the existing configurations.**Note:** System logs are necessary for troubleshooting and support. If you disable System logs, GKE customer support is offered on a best-effort basis and might require additional effort from your engineering team.

### gcloud

Update a cluster to remove the `KCP_HPA` component from the `--logging` flag: 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--logging =SYSTEM**
    

Replace the following:

  * `CLUSTER_NAME`: name of the cluster you want to create or update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: [Compute regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster. 



### Terraform

To disable `KCP_HPA` decision logs by using Terraform, update your `google_container_cluster` resource. In the `logging_config` block, remove the `KCP_HPA` value from the list for the `enable_components` field: 
    
    
    resource "google_container_cluster" "primary" {
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other configuration ...
    
      logging_config {
        enable_components = ["SYSTEM_COMPONENTS"]
      }
    }
    

Replace the following:

  * `CLUSTER_NAME`: name of the cluster you want to update.
  * `LOCATION`: [Compute region or zone](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster. 



This command disables exporting the logs generated by `KCP_HPA`. You can't retrieve them using the `logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fhpa-controller"` filter within Cloud Logging.

Retrieve the updated logging configuration of the cluster and review the list of logs to make sure that the `KCP_HPA` log is disabled:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=loggingConfig \
        --format='csv[delimiter=",",no-heading](componentConfig.enableComponents)'
    

The output is similar to the following:
    
    
    SYSTEM_COMPONENTS,APISERVER,CONTROLLER_MANAGER,SCHEDULER
    

## Types of Logs

The decision events for the horizontal Pod autoscaler are stored in Cloud Logging, at the `logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fhpa-controller"` location that's in the `_Default` bucket in the same project as your GKE cluster. All logged events are in the `JSON` format and can be found in the `jsonPayload` field of a log entry.

Make sure that you understand the storage needs of the potential log volumes, in addition to any performance or cost implications. The following examples explain how frequently the horizontal Pod autoscaler generates each type of decision event:

  * **Atomic recommendation** : the horizontal Pod autoscaler generates one atomic recommendation event every 15 seconds for each metric being monitored by each HPA object in your cluster. For example, if you have two HPA objects in your cluster and each HPA object monitors three metrics, then _six atomic recommendations_ will be logged every 15 seconds.

  * **Final recommendation** : the horizontal Pod autoscaler generates one final recommendation event every 15 seconds for each HPA object in your cluster. For example, if you have two HPA objects in your cluster, then _two final recommendations_ will be logged every 15 seconds.




In total, with _two HPA objects_ that each monitor _three metrics_ , your `KCP_HPA` log will receive _eight total_ decision event entries _every 15 seconds_.

### Atomic recommendation

An atomic recommendation log describes a recommendation based on an individual metric specified on your horizontal Pod autoscaler.

An atomic log includes the following fields:

Field | Description  
---|---  
`start_time` | Indicates when HPA started to compute a recommendation.  
`hpa` | The name of the HPA object associated with the recommendation.  
`pod_count` | Indicates the number of total Pods associated with the HPA when making the recommendation. This number also includes ready, unready, and ignored Pods.  
`metric` | Provides information about the specification and status of the metric used for the recommendation. The `metric` field contains the following subfields: 

  * `index`: index of the metric in the `Spec metrics` array.
  * `type`: metric type with values from the [MetricSourceType](https://pkg.go.dev/k8s.io/api/autoscaling/v2#MetricSourceType) (for example Resource, External).
  * `spec`: name of the metric and a target set on that metric.
  * `status`: [Status conditions](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#appendix-horizontal-pod-autoscaler-status-conditions) with respect to scalability and scaling limitations.
  * `newest_sample_time`: timestamp of the freshest metric sample.
  * `newest_sample_age_seconds`: age of the most recent sample, measured in seconds, since the recommendation computation began. A negative value signifies that the metrics sample predates the start of the computation.

  
`summary` | The summary field contains information regarding the recommendation result, including the suggested replica number. If a recommendation can't be proposed, an error message is displayed. The `summary` field contains the following subfields: 

  * `dampening`: HPA applies dampening to the recommendation and its direction to try and reduce the magnitude of a potential scale. Dampening can happen in the following ways: 
    * `up`: an up-dampening direction means HPA assumes missing-metrics Pods with 100% usage of the metric.
    * `down`: a down-dampening direction means HPA assumes missing-metrics Pods or unready Pods that consume 0% usage of the metric.
    * `none`: no dampening is applied.
  * `override`: message that provides a reason when the recommendation proposed by HPA is not applied (for example, due to tolerance); or `none` if no override happens.
  * `result`: result of the recommendation. It either proposes a recommended number of replicas or displays an error message if the recommendation can't be computed.

  
  
Example atomic recommendation log:
    
    
    {
      "insertId": "xiu4bty9k5b279wu",
      "jsonPayload": {
        "instance": {
          "vm_name": "my-unique-vm-identifier",
          "zone": "us-central1-a"
        },
        "atomicRecommendation": {
          "startTime": "2025-02-06T20:07:00.573419526Z",
          "hpa": "gke-managed-cim/kube-state-metrics",
          "metric": {
            "newestSampleAgeSeconds": -39.573419526,
            "status": {
              "averageValue": "25849856"
            },
            "newestSampleTime": "2025-02-06T20:06:21Z",
            "type": "Resource",
            "spec": {
              "target": {
                "averageValue": "400Mi"
              },
              "name": "memory"
            }
          },
          "podCount": {
            "ready": 1,
            "total": 1
          },
          "summary": {
            "override": "none",
            "replicas": 1,
            "dampening": "none"
          }
        }
      },
      "resource": {
        "type": "k8s_control_plane_component",
        "labels": {
          "project_id": "my-project-id",
          "cluster_name": "my-cluster",
          "location": "us-central1-a",
          "component_location": "us-central1-a",
          "component_name": "hpa-controller"
        }
      },
      "timestamp": "2025-02-06T20:07:00.593777835Z",
      "severity": "INFO",
      "labels": {
        "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
      },
      "logName": "projects/my-project-id/logs/container.googleapis.com%2Fhpa-controller",
      "sourceLocation": {
        "file": "event_logger.go",
        "line": "61"
      },
      "receiveTimestamp": "2025-02-06T20:07:05.284753647Z"
    }
    

### Final recommendation

A final recommendation log describes a consolidated recommendation proposed by the horizontal Pod autoscaler. The horizontal Pod autoscaler combines all the atomic recommendations from different metrics to create a final recommendation and actuates the final recommendations. Actuation means that the HPA instructs the Deployment to adjust the number of replicas to match the recommended value. If the final recommendation suggests a different number of Pods than the number of running Pods, the horizontal Pod autoscaler triggers a scale-up or scale-down event to adjust the Deployment accordingly.

A final recommendation log includes the following fields:

Field | Description  
---|---  
`start_time` | Indicates when HPA started to compute a recommendation.  
`hpa` | The name of the HPA object associated with the recommendation.  
`target_ref` | Indicates the HPA [ScaleTargetRef](https://pkg.go.dev/k8s.io/api/autoscaling/v2#HorizontalPodAutoscalerSpec) object associated with a recommendation.  
`configured_size` | The last recorded number of replicas before HPA computes and applies this recommendation.  
`top_level_override` | Provides a reason if the recommendation proposed by HPA is not applied (for example, due to tolerance); or `none` if no override happens.  
`top_level_limit` | Provides a reason if the recommendation proposed by HPA needs to be adjusted (for example, due to the number of replicas that are defined by the `MinReplicas` or `MaxReplicas` fields in the HPA specification).  
`leading_metric_index` | The leading metric index in the `Spec metrics` array is the metric whose associated atomic recommendation is used as the final recommendation.  
`normalization` | Provides stabilization and limitation summary as follows, if present: `stabilization`: describes the stabilization state if it was applied. Stabilization is used to restrict the flapping of replica count when the metrics used for scaling keep fluctuating. `stabilization` field consists of the following subfields:

  * `replicas`: replica number after stabilization.
  * `reason`: applied stabilization type — `scaleUp` or `scaleDown`.
  * `stabilization_window`: associated stabilization time period, in seconds.
  * `replicas_before_stabilization`: recommended replica number before stabilization.

`limitation`: describes how scaling limitations are handled if they are applied. This behavior modifies the recommendations proposed by the HPA based on the limitations in place. `limitation` field consists of the following subfields:

  * `replicas`: replica number after limitation.
  * `reason`: reason for not scaling beyond the min or max replica count.
  * `scaling_policy`: the [scaling policy](https://pkg.go.dev/k8s.io/api/autoscaling/v2#HPAScalingPolicy) that's applied.
  * `selectPolicy`: specifies how a policy is selected when scaling in a certain direction. `MaxChange` corresponds to [MaxChangePolicySelect](https://pkg.go.dev/k8s.io/api/autoscaling/v2#ScalingPolicySelect); `MinChange` corresponds to [MinChangePolicySelect](https://pkg.go.dev/k8s.io/api/autoscaling/v2#ScalingPolicySelect). If scaling is disabled, the `selectPolicy` field won't be present.
  * `replicas_before_limitation`: recommended replica number before limitation.

  
`replicas` | Recommended replica number.  
`actuation_error` | An error message associated with the failure, if actuation failed.  
`actuation_time` | Timestamp of the actuation on success.  
`actuation_latency_seconds` | Time that passed, in seconds, from the start of the recommendation computation until the actuation succeeded.  
  
Example final recommendation log:
    
    
    {
      "insertId": "qzyv7alfv1sm19ns",
      "jsonPayload": {
        "finalRecommendation": {
          "actuationTime": "2025-02-06T20:06:57.487786873Z",
          "targetRef": {
            "name": "kube-state-metrics",
            "kind": "StatefulSet",
            "apiVersion": "apps/v1"
          },
          "topLevelLimit": "none",
          "hpa": "gke-managed-cim/kube-state-metrics",
          "topLevelOverride": "noRecommendation",
          "replicas": 1,
          "configuredSize": 1,
          "actuationLatencySeconds": 0.003722451,
          "startTime": "2025-02-06T20:06:57.484064422Z"
        },
        "instance": {
          "vm_name": "my-unique-vm-identifier",
          "zone": "us-central1-a"
        }
      },
      "resource": {
        "type": "k8s_control_plane_component",
        "labels": {
          "cluster_name": "my-cluster",
          "component_location": "us-central1-a",
          "component_name": "hpa-controller",
          "location": "us-central1-a",
          "project_id": "my-project-id"
        }
      },
      "timestamp": "2025-02-06T20:06:57.488193527Z",
      "severity": "INFO",
      "labels": {
        "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
      },
      "logName": "projects/my-project-id/logs/container.googleapis.com%2Fhpa-controller",
      "sourceLocation": {
        "file": "event_logger.go",
        "line": "61"
      },
      "receiveTimestamp": "2025-02-06T20:06:57.844898727Z"
    }
    

## Troubleshooting

This section describes issues and resolution steps related to horizontal Pod Autoscaler events.

### No events

If you don't see any horizontal Pod autoscaler decision events, make sure you have done all of the following:

  * You have enabled Cloud Logging for the cluster.
  * You have enabled the `KCP_HPA` logs for the cluster.
  * You have deployed at least one correctly configured `hpa` object to your cluster.



To view your `hpa` object configuration, run the following command:
    
    
      kubectl describe hpa $HPA_NAME
    

If you still don't see any `KCP_HPA` logs, reach out to [Google Cloud Support](https://docs.cloud.google.com/support).

## What's next

  * See [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).
  * Understand your [GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#understanding_your_logs).
  * Learn how to find specific GKE logs using [sample queries](https://docs.cloud.google.com/logging/docs/view/query-library#kubernetes-filters).
  * Learn more about [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
