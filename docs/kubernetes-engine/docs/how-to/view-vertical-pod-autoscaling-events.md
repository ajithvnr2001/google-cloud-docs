---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events/
title: Collect vertical Pod autoscaler event logs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:38.887199+00:00
---

# Collect vertical Pod autoscaler event logs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect vertical Pod autoscaler event logs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides information about decision events emitted by the [vertical Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) in Google Kubernetes Engine (GKE). By analyzing these events, you can both gain insights into how the vertical Pod autoscaler controller manages your workload scaling and understand the decision-making process behind its actions.

The vertical Pod autoscaler emits decision events, which are stored as log entries in Cloud Logging.

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

  * To enable vertical Pod autoscaler event logging in your cluster: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 
  * To access logs and to use Logs Explorer and Observability Analytics: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Requirements

  * Your GKE cluster must be running version `1.36.0-gke.1601000` or later.
  * Enable Cloud Logging in your GKE cluster.
  * Ensure you have a [vertical Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) that you want to monitor. Ensure that the vertical Pod autoscaler fields don't include sensitive data.



### Costs

[Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing) applies when you enable Cloud Logging and collect vertical Pod autoscaler decision logs.

## Enable vertical Pod autoscaler decision logs

**Caution:** Existing clusters might have specific logging components already configured. When you update an existing cluster using the Google Cloud CLI, or an API call, you must include the existing logging configuration in your update request to avoid overwriting the existing configurations.**Note:** If you choose to send logs to Cloud Logging, you must send system logs. Make sure to enable the system logs component when you enable logs from additional sources, such as `KCP_VPA`.

The commands in the following sections enable exporting the logs generated by `KCP_VPA` and save the logs at the `logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fvpa-controller"` destination within Cloud Logging.

### Enable logs on a new cluster

To create a new cluster with the `KCP_VPA` decision logs enabled, run the following command.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        **--logging =SYSTEM,KCP_VPA**
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster you want to create or update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [compute regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster.



### Enable logs on an existing cluster

To enable the `KCP_VPA` decision logs on an existing cluster, do the following:

  1. Review the existing configuration of the cluster. If the cluster has specific logging components already configured, then decide if you want to add to or overwrite the existing logging configuration.

  2. To enable the vertical Pod autoscaler decision logs, run the following command. If you are adding to an existing configuration, then add the existing logging configuration to the command as well.
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             **--logging =SYSTEM,KCP_VPA**
         

Replace the following:

     * `CLUSTER_NAME`: name of the cluster you want to create or update.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `LOCATION`: [compute regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster.



## Verify that logging is enabled

To verify that the `KCP_VPA` decision logs are enabled on a cluster, retrieve the updated logging configuration of the cluster and review the list of logs. To do so, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=loggingConfig \
        --format='csv[delimiter=",",no-heading](componentConfig.enableComponents)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the [compute regions or zones](https://docs.cloud.google.com/compute/docs/regions-zones) for your cluster.



When `KCP_VPA` decision logs are enabled on a cluster, the output is similar to the following:
    
    
    SYSTEM_COMPONENTS,APISERVER,CONTROLLER_MANAGER,SCHEDULER,KCP_VPA
    

## View vertical Pod autoscaler logs in the Logs Explorer

You can monitor the behavior of the vertical Pod autoscaler in the Logs Explorer. To view vertical Pod autoscaler logs, complete the following steps:

  1. Go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select **All log names** , and search the log names for `vpa-controller`.

The logs explorer displays all vertical Pod autoscaler logs, including logs from all clusters that enabled vertical Pod autoscaler logs in the project.

  3. You can filter the logs by using the cluster name or workload name. For example, to list events from a specific workload in a cluster, specify the cluster name and workload name by using the following query:
         
         resource.labels.cluster_name="CLUSTER_NAME" AND
         jsonPayload.target.name="WORKLOAD_NAME"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `WORKLOAD_NAME`: the name of the workload.



## Disable vertical Pod autoscaling decision logs

**Caution:** Existing clusters might have specific logging components already configured. When you update an existing cluster using the Google Cloud CLI, or an API call, you must include the existing logging configuration in your update request to avoid overwriting the existing configurations.**Note:** System logs are necessary for troubleshooting and support. If you disable System logs, GKE customer support is offered on a best-effort basis and might require additional effort from your engineering team.

  1. To disable the `KCP_VPA` decision logs on an existing cluster, run the following command:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --logging=SYSTEM
         

  2. Verify that the `KCP_VPA` decision logs are disabled. To do so, run the following command:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --flatten=loggingConfig \
             --format='csv[delimiter=",",no-heading](componentConfig.enableComponents)'
         

When `KCP_VPA` decision logs are disabled on a cluster, the output is similar to the following:
         
         SYSTEM_COMPONENTS,APISERVER,CONTROLLER_MANAGER,SCHEDULER
         




## Types of logs

The decision events for the vertical Pod autoscaler are stored in Cloud Logging, at the `logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fvpa-controller"` location that's in the `_Default bucket` in the same project as your GKE cluster. All logged events are in the `JSON` format and can be found in the `jsonPayload` field of a log entry.

The type and frequency of logs generated depend on the [vertical Pod autoscaling mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#vpa-modes) configured for your workload. There are four types of VPA logs, categorized by the operation they perform:

  * **Update recommendation** : each vertical Pod autoscaler generates one new update recommendation log every minute.
  * **Evict Pod** : each vertical Pod autoscaler generates one evict Pod log for each Pod when the vertical Pod autoscaler decides to resize in `Recreate` mode.
  * **Apply recommendation on eviction** : each vertical Pod autoscaler generates one apply recommendation log for each Pod when the vertical Pod autoscaler decides to resize in `Recreate` mode.
  * **Apply recommendation in place** : each vertical Pod autoscaler generates one apply recommendation in place log for each Pod when the vertical Pod autoscaler decides to resize in `InPlaceOrRecreate` mode.



The types of logs that the controller can emit depends on the mode of the vertical Pod autoscaler. The following table lists the logs that can be emitted for each mode.

Vertical Pod autoscaler mode | Types of logs that can be emitted  
---|---  
`Auto` (deprecated) or `Recreate` | 

  * Update recommendation
  * Evict Pod
  * Apply recommendation on eviction

  
`InPlaceOrRecreate` | 

  * Update recommendation
  * Apply recommendation in place
  * Evict Pod (this type of log is possible when `In-place` resize fails)
  * Apply recommendation on eviction (this type of log is possible when `In-place` resize fails)

  
  
For a vertical Pod autoscaler with `InPlaceOrRecreate` mode, when `In-place resize` fails, the autoscaler has the same behavior as the `Recreate` mode.

### Update recommendation

An update recommendation log can be produced with the following vertical Pod autoscaler modes: `Auto` (deprecated), `Recreate`, and `InPlaceOrRecreate`.

The `jsonPayload` of this decision log includes the following fields:

Field | Description  
---|---  
`vpaName` | The name of the VPA.  
`vpaNamespace` | The namespace of the VPA.  
`target` | The workload that this VPA is targeting. 

  * `name`: the name of the workload.
  * `kind`: the kind of workload.
  * `apiVersion`: the API version of the workload.

  
`operation` | The operation that is running. The value is one of the following: 

  * `UPDATE_RECOMMENDATION`
  * `EVICT_POD`
  * `APPLY_RECOMMENDATION_IN_PLACE`
  * `APPLY_RECOMMENDATION_ON_EVICTION`

  
`state` | State of the operation. The value is one of the following: 

  * `SUCCEEDED`
  * `SKIPPED`
  * `FAILED`

  
`reason` | The reason explains why the operation is skipped or failed. For operation `APPLY_RECOMMENDATION_IN_PLACE` and `APPLY_RECOMMENDATION_ON_EVICTION` success case, it clarifies that the applied recommendation could be different from the raw recommendation in operation `UPDATE_RECOMMENDATION` due to modifications applied (such as capping or autopilot resource ratio).  
`recommendedResources` | The raw recommendation. This is exactly the same as the `Status.Recommendation` field in the VPA object. 

  * `containerName`: the name of the container this recommendation is for.
  * `target`: the actual recommendation that might be applied.
  * `lowerBound`: the lower bound of the recommendation.
  * `upperBound`: the upper bound of the recommendation.
  * `uncappedTarget`: the recommendation before capping by lower or upper bound.

  
`confidence` | Confidence of the recommendation. This field exists when the state is `succeeded`. The value is one of the following: 

  * `LOW`: the VPA has processed less than 10 metric samples.
  * `HIGH`: the VPA has processed 10 or more metric samples.

  
  
Example update recommendation log:
    
    
    {
     "insertId": "ehz6w9d304v4zttg",
     "jsonPayload": {
       "state": "SUCCEEDED",
       "instance": {
         "vm_name": "my-unique-vm-identifier",
         "zone": "us-central1-c"
       },
       "recommendedResources": [
         {
           "lowerBound": {
             "memory": "5Mi",
             "cpu": "5m"
           },
           "containerName": "nginx",
           "uncappedTarget": {
             "memory": "5Mi",
             "cpu": "1m"
           },
           "upperBound": {
             "memory": "5Mi",
             "cpu": "5m"
           },
           "target": {
             "memory": "5Mi",
             "cpu": "5m"
           }
         }
       ],
       "operation": "UPDATE_RECOMMENDATION",
       "target": {
         "name": "my-workload",
         "kind": "Deployment",
         "apiVersion": "apps/v1"
       },
       "vpaNamespace": "default",
       "vpaName": "my-vpa"
     },
     "resource": {
       "type": "k8s_control_plane_component",
       "labels": {
         "component_location": "us-central1-c",
         "project_id": "my-project",
         "cluster_name": "my-cluster",
         "location": "us-central1-c",
         "component_name": "vpa-controller"
       }
     },
     "timestamp": "2026-01-22T19:28:16.069635605Z",
     "severity": "INFO",
     "labels": {
       "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
     },
     "logName": "projects/my-project/logs/container.googleapis.com%2Fvpa-controller",
     "sourceLocation": {
       "file": "vpa_event_logger.go",
       "line": "23"
     },
     "receiveTimestamp": "2026-01-22T19:28:17.750678359Z"
    }
    

### Evict Pod

An evict Pod log is available with VPA mode `Auto` (deprecated) and `Recreate`. This log type is also possible with VPA mode `InPlaceOrRecreate` if the `In-place resize` operation fails.

The `jsonPayload` of this decision log includes the following fields:

Field | Description  
---|---  
`vpaName` | The name of the VPA.  
`vpaNamespace` | The namespace of the VPA.  
`target` | The workload that this VPA is targeting. 

  * `name`: the name of the workload.
  * `kind`: the kind of workload.
  * `apiVersion`: the API version of the workload.

  
`operation` | The operation that is running. The value is one of the following: 

  * `UPDATE_RECOMMENDATION`
  * `EVICT_POD`
  * `APPLY_RECOMMENDATION_IN_PLACE`
  * `APPLY_RECOMMENDATION_ON_EVICTION`

  
`state` | The state of the operation. The value is one of the following: 

  * `SUCCEEDED`
  * `SKIPPED`
  * `FAILED`

  
`reason` | The reason explains why the operation is skipped or failed. For operation `APPLY_RECOMMENDATION_IN_PLACE` and `APPLY_RECOMMENDATION_ON_EVICTION` success case, the reason clarifies that the applied recommendation could be different from the raw recommendation in operation `UPDATE_RECOMMENDATION` due to modifications applied (such as capping or autopilot resource ratio).  
`pod` | The name of the Pod.   
  
Example evict Pod log:
    
    
    {
     "insertId": "8x278gc4f75oowf4",
     "jsonPayload": {
       "target": {
         "kind": "Deployment",
         "apiVersion": "apps/v1",
         "name": "my-deployment"
       },
       "operation": "EVICT_POD",
       "vpaName": "my-vpa",
       "pod": "my-deployment-856ff7966-gr4rh",
       "state": "SUCCEEDED",
       "vpaNamespace": "default",
       "instance": {
         "vm_name": "my-unique-vm-identifier",
         "zone": "us-central1-c"
       }
     },
     "resource": {
       "type": "k8s_control_plane_component",
       "labels": {
         "component_name": "vpa-controller",
         "cluster_name": "my-cluster",
         "component_location": "us-central1-c",
         "location": "us-central1-c",
         "project_id": "my-project"
       }
     },
     "timestamp": "2026-01-22T19:26:25.283067078Z",
     "severity": "INFO",
     "labels": {
       "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
     },
     "logName": "projects/my-project/logs/container.googleapis.com%2Fvpa-controller",
     "sourceLocation": {
       "file": "vpa_event_logger.go",
       "line": "23"
     },
     "receiveTimestamp": "2026-01-22T19:26:27.766941073Z"
    }
    

### Apply recommendation on eviction

An apply recommendation on eviction log is available with VPA mode `Auto` (deprecated) and `Recreate`. This log type is also possible with VPA mode `InPlaceOrRecreate` if `In-place resize` fails.

The `jsonPayload` of this decision log includes the following fields:

Field | Description  
---|---  
`vpaName` | The name of the VPA.  
`vpaNamespace` | The namespace of the VPA.  
`target` | The workload that this VPA is targeting. 

  * `name`: the name of the workload.
  * `kind`: the kind of workload.
  * `apiVersion`: the API version of the workload.

  
`operation` | The operation that is running. The value is one of the following: 

  * `UPDATE_RECOMMENDATION`
  * `EVICT_POD`
  * `APPLY_RECOMMENDATION_IN_PLACE`
  * `APPLY_RECOMMENDATION_ON_EVICTION`

  
`state` | State of the operation. The value is one of the following: 

  * `SUCCEEDED`
  * `SKIPPED`
  * `FAILED`

  
`reason` | The reason explains why the operation is skipped or failed. For operation `APPLY_RECOMMENDATION_IN_PLACE` and `APPLY_RECOMMENDATION_ON_EVICTION` success case, it clarifies that the applied recommendation could be different from the raw recommendation in operation `UPDATE_RECOMMENDATION` due to modifications applied (such as capping or autopilot resource ratio).  
`pod` | The name of the Pod.   
`appliedResources` | The resources applied to the Pod. 

  * `containerName`: the name of the container.
  * `requests`: the resource requests applied. 
    * `cpu`: the CPU applied.
    * `memory`: the memory applied.
  * `limits`: the resource limits applied. 
    * `cpu`: the CPU applied.
    * `memory`: the memory applied.

  
`confidence` | The confidence of the recommendation. This field exists when the state is `succeeded`. The value is one of the following: 

  * `LOW`: the VPA has processed less than 10 metric samples.
  * `HIGH`: the VPA has processed 10 or more metric samples.

  
  
Example apply recommendation on eviction log:
    
    
    {
     "insertId": "366tcmgdkq94eppg",
     "jsonPayload": {
       "appliedResources": [
         {
           "containerName": "my-container",
           "requests": {
             "memory": "15Mi",
             "cpu": "15m"
           }
         }
       ],
       "vpaName": "my-vpa",
       "vpaNamespace": "default",
       "instance": {
         "zone": "us-central1-c",
         "vm_name": "my-unique-vm-identifier"
       },
       "pod": "my-deployment-856ff7966-%",
       "state": "SUCCEEDED",
       "target": {
         "name": "my-deployment",
         "kind": "Deployment",
         "apiVersion": "apps/v1"
       },
       "operation": "APPLY_RECOMMENDATION_ON_EVICTION"
     },
     "resource": {
       "type": "k8s_control_plane_component",
       "labels": {
         "location": "us-central1-c",
         "component_location": "us-central1-c",
         "cluster_name": "my-cluster",
         "component_name": "vpa-controller",
         "project_id": "my-project"
       }
     },
     "timestamp": "2026-01-22T19:26:25.344313199Z",
     "severity": "INFO",
     "labels": {
       "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
     },
     "logName": "projects/my-project/logs/container.googleapis.com%2Fvpa-controller",
     "sourceLocation": {
       "file": "vpa_event_logger.go",
       "line": "23"
     },
     "receiveTimestamp": "2026-01-22T19:26:32.744122156Z"
    }
    

### Apply recommendation in place

An apply recommendation in place log is available with VPA mode `InPlaceOrRecreate`.

The `jsonPayload` of this decision log includes the following fields:

Field | Description  
---|---  
`vpaName` | The name of the VPA.  
`vpaNamespace` | The namespace of the VPA.  
`target` | The workload that this VPA is targeting. 

  * `name`: the name of the workload.
  * `kind`: the kind of workload.
  * `apiVersion`: the API version of the workload.

  
`operation` | The operation that is running. The value is one of the following: 

  * `UPDATE_RECOMMENDATION`
  * `EVICT_POD`
  * `APPLY_RECOMMENDATION_IN_PLACE`
  * `APPLY_RECOMMENDATION_ON_EVICTION`

  
`state` | The state of the operation. The value is one of the following: 

  * `SUCCEEDED`
  * `SKIPPED`
  * `FAILED`

  
`reason` | The reason explains why the operation is skipped or failed. For operation `APPLY_RECOMMENDATION_IN_PLACE` and `APPLY_RECOMMENDATION_ON_EVICTION` success case, the reason clarifies that the applied recommendation could be different from the raw recommendation in operation `UPDATE_RECOMMENDATION` due to modifications applied (such as capping or autopilot resource ratio).  
`pod` | The name of the Pod.   
`appliedResources` | The resources applied to the Pod. 

  * `containerName`: the name of the container.
  * `requests`: the resource requests applied. 
    * `cpu`: the CPU applied.
    * `memory`: the memory applied.
  * `limits`: the resource limits applied. 
    * `cpu`: the CPU applied.
    * `memory`: the memory applied.

  
`confidence` | The confidence of the recommendation. This field exists when the state is `succeeded`. The value is one of the following: 

  * `LOW`: the VPA has processed less than 10 metric samples.
  * `HIGH`: the VPA has processed 10 or more metric samples.

  
  
Example apply recommendation in place log:
    
    
    {
     "insertId": "suzfuepgyiwap7hb",
     "jsonPayload": {
       "pod": "my-deployment-cdc7fd7b4-grxlk",
       "vpaNamespace": "default",
       "state": "SUCCEEDED",
       "target": {
         "name": "my-deployment",
         "apiVersion": "apps/v1",
         "kind": "Deployment"
       },
       "operation": "APPLY_RECOMMENDATION_IN_PLACE",
       "appliedResources": [
         {
           "containerName": "my-container",
           "limits": {
             "cpu": "10m",
             "memory": "10Mi"
           },
           "requests": {
             "cpu": "5m",
             "memory": "5Mi"
           }
         }
       ],
       "instance": {
         "zone": "us-central1-c",
         "vm_name": "my-unique-vm-identifier"
       },
       "vpaName": "my-vpa"
     },
     "resource": {
       "type": "k8s_control_plane_component",
       "labels": {
         "project_id": "my-project",
         "component_location": "us-central1-c",
         "cluster_name": "my-cluster",
         "location": "us-central1-c",
         "component_name": "vpa-controller"
       }
     },
     "timestamp": "2026-01-22T19:26:25.214095375Z",
     "severity": "INFO",
     "labels": {
       "compute.googleapis.com/resource_name": "my-unique-vm-identifier"
     },
     "logName": "projects/my-project/logs/container.googleapis.com%2Fvpa-controller",
     "sourceLocation": {
       "file": "vpa_event_logger.go",
       "line": "23"
     },
     "receiveTimestamp": "2026-01-22T19:26:27.766941073Z"
    }
    

## Troubleshooting

This section describes issues and resolution steps related to vertical Pod autoscaler events.

### No events

If you don't see any vertical Pod autoscaler decision events, make sure you have done all of the following:

  * You have enabled Cloud Logging for the cluster.
  * You have enabled the `KCP_VPA` logs for the cluster.
  * You have deployed at least one correctly configured `vpa` object to your cluster.



To view your `vpa` object configuration, run the following command:
    
    
    kubectl describe vpa $VPA_NAME
    

If you still don't see any `KCP_VPA` logs, reach out to [Google Cloud Support](https://docs.cloud.google.com/support).

## What's next

  * See [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).
  * Understand your [GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#understanding_your_logs).
  * Learn how to find specific GKE logs using [sample queries](https://docs.cloud.google.com/logging/docs/view/query-library#kubernetes-filters).
  * Learn more about [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
