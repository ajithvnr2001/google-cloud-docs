---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-logs/
title: View fleet logs \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:27.648017+00:00
---

# View fleet logs  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  View fleet logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and view logs for fleets. With fleet logging, multiple logs are aggregated and scoped together, enabling you to analyze the health of your applications in one consolidated view. This page is intended for:

  * Platform administrators who want to enable fleet logging and view logs in all namespaces.
  * Service operators who want to view logs in the specific namespaces to which they have access.



## Overview

Fleet logs let you view logs at the entire fleet level, or for specific team scopes. Scopes are a team-management feature that let you define subsets of fleet logs and other resources on a per-team basis, with each scope associated with one or more fleet member clusters. For more information on scopes, see [Manage teams for your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management).

You can view two types of fleet logs:

  * Default logs: All Kubernetes logs (except [Audit logs](https://docs.cloud.google.com/logging/docs/audit)) that don't belong to any specific fleet scope with the following [resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types):

    * `k8s_container`
    * `k8s_pod`
    * `k8s_node`
    * `k8s_cluster`
    * `k8s_control_plane_components`
  * Fleet scope logs: Container and Pod logs for applications owned by a team deployed in a specific [fleet scope](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management#fleet_team_management_overview) with multiple fleet-level namespaces.




Viewing fleet scope logs is optional. If you don't want to set up team management, you can still use fleet logging to view default logs.

Logs can be routed to different [log buckets](https://docs.cloud.google.com/logging/docs/routing/overview#buckets) in the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) with different views for access control. The default retention period of a log bucket is 30 days. You can configure this period if needed.

There are two modes supported for log routing where fleets contain clusters from multiple projects ([cross-project registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#before_you_begin)):

  * **`MOVE`** : All logs are moved to the fleet host project. If a cluster in the fleet belongs to a different project, their logs are _not_ retained in the original Google Cloud project.

  * **`COPY`** : All logs are sent to the fleet host project. If a cluster in the fleet belongs to a different project, their logs are also retained in the original Google Cloud project.




## Before you begin

  1. If you have already manually created Cloud Logging [buckets](https://docs.cloud.google.com/logging/docs/buckets#create_bucket), [sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#creating_sink), and [set exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions), ensure that the names you have assigned these objects don't conflict with the fleet logging naming restrictions. If there is a naming conflict, [contact Support](https://docs.cloud.google.com/stackdriver/docs/getting-support) before proceeding.

  2. Ensure that the clusters whose logs you want to view have been [registered to your chosen fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation).

  3. If you don't have it installed already, install the Google Cloud CLI following the [installation instructions](https://docs.cloud.google.com/sdk/install). You need version 424.0.0 or higher to view your fleet logs.

  4. Ensure that your fleet host project has all the required APIs enabled, including the Anthos API:
         
         gcloud services enable --project=FLEET_HOST_PROJECT_ID  \
         gkehub.googleapis.com \
         container.googleapis.com \
         connectgateway.googleapis.com \
         cloudresourcemanager.googleapis.com \
         iam.googleapis.com \
         anthos.googleapis.com
         

where:

     * FLEET_HOST_PROJECT_ID is the project ID of your fleet host project. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



## Prepare scopes, namespaces and workloads

If you want to view fleet scope logs, you will need to create a fleet scope and a fleet namespace, in addition to preparing workloads for log collection.

Before you continue, set the default project for the Google Cloud CLI by running the following command:
    
    
    gcloud config set project FLEET_HOST_PROJECT_ID
    

### Create scopes and namespaces

If you want to view logs at the scope level, and haven't already set up scopes, follow the instructions in [Manage teams for your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management) to create scopes, add clusters to scopes, and set up fleet namespaces.

### Prepare workloads

To view log data from your applications, you will need to deploy your workloads in a cluster to the fleet namespace configured in the preceding step. This step is applicable whether you choose to view default logs, fleet scope logs, or both. Here is an example to configure your workload:
    
    
      apiVersion: v1
      kind: Pod
      metadata:
        name: fleet-example-pod
        namespace: NAMESPACE_NAME
      spec:
        containers:
        - name: count
          image: ubuntu:14.04
          args: [bash, -c,
               'for ((i = 0; ; i++)); do echo "$i: $(date)"; sleep 1; done']
    

After deploying the resource, you may see an error if the fleet namespace failed to create for some reason. In this case, run the following command to create the namespace again, and rerun the workload deployment command:
    
    
      kubectl create namespace NAMESPACE_NAME
      

**Note:** Any changes made to the scope, clusters that belong to a scope, or namespace might take a few minutes to apply.

## Enable fleet logging

This section describes how to enable the fleet logging feature and grant team access to view logs.

### gcloud

  * You can enable fleet logging using the Google Cloud CLI by specifying the configuration fields for the feature in a JSON or YAML file. Here is a example of a configuration for fleet logging in JSON format:
        
        {
          "loggingConfig": {
              "defaultConfig": {
                  "mode": "COPY"
              },
              "fleetScopeLogsConfig": {
                  "mode": "MOVE"
              }
          }
        }
        




To view all the fields you can configure for this feature, see the API reference.

When the `defaultConfig` or `fleetScopeLogsConfig` fields are enabled with the `COPY` or `MOVE` modes, as shown in the preceding example, a log sink is created with the prefix `fleet-o11y-`. This log sink is created under the Google Cloud project to route target logs from the cluster project to the fleet host project.

When `fleetScopeLogsConfig` is enabled, a log bucket with name `fleet-o11y-scope-$SCOPE_NAME` is also created in the `global` [region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) under the fleet host project, if it doesn't exist already. Note that you can't change the bucket's region.

**Note:** Cloud Logging has a limit of 100 buckets per Google Cloud project. This limit includes buckets that are [pending deletion](https://docs.cloud.google.com/logging/docs/buckets#deleting-logs-bucket). If you observe the number of buckets is approaching the limit, you can [contact Support](https://docs.cloud.google.com/stackdriver/docs/getting-support) to request changes to the quota.

In this example, default logs will be sent to the fleet host project and retained in the original Google Cloud project, while fleet scope logs will be sent to the fleet host project, and not retained in the Google Cloud project.

  * Add your chosen configuration to a JSON file, and update the fleet:
        
        gcloud container fleet fleetobservability update \
                --logging-config=JSON_FILE
        




Replace JSON_FILE with the name of your filename.

### Terraform

  * The fleet observability feature is enabled by default. If this is your first time using Terraform to manage the fleet observability feature, import the feature into Terraform by running the following command:


    
    
    terraform import google_gke_hub_feature.feature projects/FLEET_HOST_PROJECT_ID/locations/global/features/fleetobservability
    

  * You can enable fleet logging with Terraform using a [Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine).



For example, you can add the following block to your Terraform configuration:
    
    
      resource "google_gke_hub_feature" "feature" {
        name = "fleetobservability"
        location = "global"
        spec {
          fleetobservability {
            logging_config {
              default_config {
                mode = "COPY"
              }
              fleet_scope_logs_config {
                mode = "MOVE"
              }
            }
          }
        }
      }
    

When the `default_config` or `fleet_scope_logs_config` fields are enabled with the `COPY` or `MOVE` modes, as shown in the preceding example, a log sink is created with the prefix `fleet-o11y-`. This log sink is created under the Google Cloud project to route target logs from the cluster project to the fleet host project.

When `fleet_scope_logs_config` is enabled, a log bucket with name `fleet-o11y-scope-$SCOPE_NAME` is also created under the fleet host project, if it doesn't exist already.

**Note:** Cloud Logging has a limit of 100 buckets per Google Cloud project. This limit includes buckets that are [pending deletion](https://docs.cloud.google.com/logging/docs/buckets#deleting-logs-bucket). If you observe the number of buckets is approaching the limit, you can [contact Support](https://docs.cloud.google.com/stackdriver/docs/getting-support) to request changes to the quota.

In this example, default logs will be sent to the fleet host project and retained in the original Google Cloud project, while fleet scope logs will be sent to the fleet host project, and not retained in the Google Cloud project.

Verify that the feature spec is updated:
    
    
       gcloud container fleet fleetobservability describe
      

The output shows the `fleetobservability` spec updated with the configuration, as in the following example:
    
    
    createTime: '2022-09-30T16:05:02.222568564Z'
    membershipStates:
      projects/123456/locations/us-central1/memberships/cluster-1:
        state:
          code: OK
          description: Fleet monitoring enabled.
          updateTime: '2023-04-03T20:22:51.436047872Z'
    name:
    projects/123456/locations/global/features/fleetobservability
    resourceState:
      state: ACTIVE
    spec:
      **fleetobservability:
        loggingConfig:
          defaultConfig:
            mode: COPY
          fleetScopeLogsConfig:
            mode: MOVE**
    state:
      state: {}
    updateTime: '2023-04-03T20:38:17.719596966Z'
    

Any changes made to the `fleetobservability` spec might take a few minutes to apply.

### Set up cross-project logging permissions

This section is only required if you are registering a cluster to a fleet in a different project (also known as [cross-project registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#before_you_begin)). In order to route logs from cluster projects to the fleet host project, you must grant the role `roles/logging.bucketWriter` to the logging service account from each cluster project.

  1. To obtain the service account credentials from sinks in cluster projects, run the following command:
         
         FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
         FLEET_HOST_PROJECT_NUMBER=$(gcloud projects describe "${FLEET_HOST_PROJECT_ID}" --format "value(projectNumber)")
         gcloud logging sinks --project=GKE_PROJECT_ID describe fleet-o11y-${FLEET_HOST_PROJECT_NUMBER}-default
         

If the command returns an error that the log sink cannot be found, try re-running the command after a minute or two. You can view the service account in the `writerIdentity` field of the sink description as shown in the following example:
         
         createTime: '2023-04-06T02:26:54.716195307Z'
         destination:
         logging.googleapis.com/projects/123456/locations/global/buckets/_Default
         filter: xxx
         name: fleet-o11y-default
         updateTime: '2023-04-06T19:03:51.598668462Z'
         **writerIdentity:
         serviceAccount:service-123456@gcp-sa-logging.iam.gserviceaccount.com**
         

  2. Grant the role of `roles/logging.bucketWriter` to the service account retrieved:
         
         gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
             --member "SERVICE_ACCOUNT" \
             --role "roles/logging.bucketWriter"
         

where:

     * SERVICE_ACCOUNT is the name of the service account retrieved from the preceding step. For example:
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:service-123456@gcp-sa-logging.iam.gserviceaccount.com" \
        --role "roles/logging.bucketWriter"
    




### Grant team access to logs

The section describes how to grant access to users to view container logs and Pod logs.

  1. Get the IAM policy for the fleet project, and write it to a local file in JSON format:
         
         gcloud projects get-iam-policy FLEET_HOST_PROJECT_ID --format json > output.json
         

  2. Add an IAM condition that lets the user account view data from the log bucket you created. Here is an example to view container logs and Pod logs:
         
         {
           "bindings": [
             {
               "members": [
                 "user:USER_ACCOUNT_EMAIL"
               ],
               "role": "roles/logging.viewAccessor",
               "condition": {
                   "title": "Bucket reader condition example",
                   "description": "Grants logging.viewAccessor role to user USER_ACCOUNT_EMAIL for the fleet-o11y-scope-SCOPE_NAME-k8s_container and fleet-o11y-scope-SCOPE_NAME-k8s_pod log view.",
                   "expression":
                     "resource.name == \"projects/FLEET_HOST_PROJECT_ID/locations/global/buckets/fleet-o11y-scope-SCOPE_NAME/views/fleet-o11y-scope-SCOPE_NAME-k8s_container\" || resource.name == \"projects/FLEET_HOST_PROJECT_ID/locations/global/buckets/fleet-o11y-scope-SCOPE_NAME/views/fleet-o11y-scope-SCOPE_NAME-k8s_pod\""
               }
             }
           ],
         }
         

  3. Update the IAM policy:
         
         gcloud projects set-iam-policy FLEET_HOST_PROJECT_ID output.json
         




For more options about granting access, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

## View fleet logs

Platform administrators have access to view all logs in all namespaces.

### Default logs

To view all default logs in the `_Default` bucket in your fleet host project, fill in the variables in the following URL, copy and paste it to your browser:
    
    
    https://console.cloud.google.com/logs/query;query=;storageScope=storage,projects%2FFLEET_HOST_PROJECT_ID%2Flocations%2Fglobal%2Fbuckets%2F_Default%2Fviews%2F_Default?jsmode=O&mods=pan_ng2&project=FLEET_HOST_PROJECT_ID
    

### Fleet scope container logs and Pod logs

Service operators can view logs in the namespaces to which they have access. To view logs for all namespaces in a specific fleet scope, complete the following steps:

  1. With your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project) selected, go to the **Teams** section in the Google Cloud console.

[Go to Teams](https://console.cloud.google.com/kubernetes/teams/)

  2. Click the team scope whose logs you want to view, and click the **Logs** tab.

  3. Select **Container Logs** or **Pod logs** to filter the logs view.




To view logs for a specific namespace in your scope:

  1. In the **Teams** page, with your team scope selected, click the **Namespaces** tab.
  2. Click the namespace whose logs you want to view, and click the **Logs** tab.
  3. Select either **Container Logs** or **Pod logs** to filter the logs view.



Alternatively, to view container logs, fill in the variables in the following URL, copy and paste it to your browser:
    
    
    https://console.cloud.google.com/logs/query;query=;storageScope=storage,projects%2FFLEET_HOST_PROJECT_ID%2Flocations%2Fglobal%2Fbuckets%2Ffleet-o11y-scope-SCOPE_NAME%2Fviews%2Ffleet-o11y-scope-SCOPE_NAME-k8s_container?jsmode=O&mods=pan_ng2&project=FLEET_HOST_PROJECT_ID
    

To view Pod logs in a specific fleet scope, fill in the variables in the following URL, copy and paste it to your browser:
    
    
    https://console.cloud.google.com/logs/query;query=;storageScope=storage,projects%2FFLEET_HOST_PROJECT_ID%2Flocations%2Fglobal%2Fbuckets%2Ffleet-o11y-scope-SCOPE_NAME%2Fviews%2Ffleet-o11y-scope-SCOPE_NAME-k8s_pod?jsmode=O&mods=pan_ng2&project=FLEET_HOST_PROJECT_ID
    

See [Logs Explorer interface](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-viewer-interface) for more information on how to analyze log data.

## Disable fleet logging

To disable the fleet logging feature, complete the following steps:

### gcloud

  1. Save the following configuration to a file named `disable_logging_config.json`:
         
         {
           "loggingConfig": {}
         }
         

  2. Update the `fleetobservability` feature spec:
         
         gcloud container fleet fleetobservability update \
                 --logging-config=disable_logging_config.json
         




### Terraform

In your Terraform configuration, update all modes for log routing to `MODE_UNSPECIFIED`. Here is an example:
    
    
      resource "google_gke_hub_feature" "feature" {
        name = "fleetobservability"
        location = "global"
        spec {
          fleetobservability {
            logging_config {
              default_config {
                mode = "MODE_UNSPECIFIED"
              }
              fleet_scope_logs_config {
                mode = "MODE_UNSPECIFIED"
              }
            }
          }
        }
      }
    

Verify that the feature spec is updated:
    
    
       gcloud container fleet fleetobservability describe
      

The output shows the `fleetobservability` spec updated with your configuration:
    
    
      createTime: '2022-09-30T16:05:02.222568564Z'
      membershipStates:
        projects/123456/locations/global/memberships/cluster-1:
          state:
            code: OK
            description: Fleet monitoring enabled.
            updateTime: '2023-04-03T20:22:51.436047872Z'
      name:
      projects/123456/locations/global/features/fleetobservability
      resourceState:
        state: ACTIVE
      spec:
        **fleetobservability:
          loggingConfig: {}**
      state:
        state: {}
      updateTime: '2023-04-03T20:38:17.719596966Z'
      

Any changes made to the `fleetobservability` spec might take a few minutes to apply.

After disabling fleet logging, log sinks and exclusion filters will be removed from your projects. However, all log buckets created for the scope, and log views created under the log bucket will be preserved. To delete the log bucket in your fleet host project, see [Delete a bucket](https://docs.cloud.google.com/logging/docs/buckets#deleting-logs-bucket).

## Update retention period for log buckets

The default retention period of a log bucket is 30 days. To update this period, run the following command:
    
    
    gcloud logging buckets update fleet-o11y-scope-SCOPE_NAME --location=global --retention-days=RETENTION_DAYS
    

where:

  * SCOPE_NAME is the name of the fleet scope.

  * RETENTION_DAYS is the number of days of the new retention period. For more options on configuring log buckets, see [Manage buckets](https://docs.cloud.google.com/logging/docs/buckets#manage_buckets).




If you extend a bucket's retention period, then the retention rules apply going forward and not retroactively. Logs can't be recovered after the applicable retention period ends.

## API reference

This section provides information on the possible fields you can add to your `fleetobservability` object.

### fleetobservability

`fleetobservability` defines the fleet observability configuration.

Field | Description | Schema | Optional  
---|---|---|---  
loggingConfig | Specified if the fleet logging feature is enabled for the entire fleet. If unspecified, the fleet logging feature is disabled for the entire fleet. | loggingConfig | True  
  
### loggingConfig

`loggingConfig` defines the configuration of fleet logging features in fleet observability.

Field | Description | Schema | Optional  
---|---|---|---  
defaultConfig | Sets the log routing behavior for default logs in the fleet. | routingConfig | True  
fleetScopeLogsConfig | Sets the log routing behavior for fleet scope logs. | routingConfig | True  
  
### routingConfig

`routingConfig` defines the configuration of the log routing mode in the fleet logging feature.

Field | Description | Schema | Optional  
---|---|---|---  
mode | Specified to enable logs routing, and unspecified or MODE_UNSPECIFIED to disable logs routing. If set to COPY, logs will be copied to the destination project. If set to MOVE, logs will be moved to the destination project. | String; One of: MOVE, COPY and MODE_UNSPECIFIED | True  
  
## Naming restrictions

When fleet observability is enabled, the fleet observability controller reserves the following names for the logs objects it creates. To avoid unwanted or unexpected behavior, you should avoid using these names when you create your own [log buckets](https://docs.cloud.google.com/logging/docs/buckets#create_bucket), [sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#creating_sink), and [set exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

Feature enabled | Object created | Name used by fleet observability  
---|---|---  
`defaultConfig` | Sink | `fleet-o11y-FLEET_PROJECT_NUMBER-default`  
Exclusion filter. | `fleet-o11y-FLEET_PROJECT_NUMBER-default-exclusion`. This name is reserved under the `_Default` sink of the cluster project.  
`fleetScopeLogsConfig` | Log bucket | `fleet-o11y-scope-SCOPE_NAME`  
  
  * Logs view for container logs in the bucket

| `fleet-o11y-scope-SCOPE_NAME-k8s_container`


  
* Logs view for Pod logs in the bucket
| `fleet-o11y-scope-SCOPE_NAME-k8s_pod`  
Sink | `fleet-o11y-FLEET_PROJECT_NUMBER-scope-SCOPE_NAME`  
Exclusion filter | `fleet-o11y-FLEET_PROJECT_NUMBER-scope-exclusion`  
  
## Troubleshooting

This section describes how to resolve fleet logging related issues.

### Email notification about sink configuration error

If you received an email with the title `[ACTION REQUIRED] Cloud Logging sink configuration error in <Your GCP Project>`, then the service account of your log sink does not have permission to write logs to the destination of the sink. To resolve this, follow the steps in Cross-project logging permissions.

### Unknown error message from Cloud Logging UI

If you see the following error in the Cloud Logging UI, double-check that the `project_id` and `scope` variables entered in the URL are correct.
    
    
    Error: There is an unknown error while executing this operation.
    

### Membership not found error

You might see the following error:
    
    
    ERROR: (gcloud.alpha.container.fleet.memberships.bindings.create) NOT_FOUND: Resource 'parent resource not found for projects/...' was not found
    

Ensure that you have [registered the cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#before_you_begin) to a fleet.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
