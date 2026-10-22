---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing/
title: Sequence the rollout of cluster upgrades with custom stages \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:41.428911+00:00
---

# Sequence the rollout of cluster upgrades with custom stages  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Sequence the rollout of cluster upgrades with custom stages Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Rollout sequencing with custom stageskeyboard_arrow_down

  * [ Rollout sequencing with custom stages ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing)
  * [ Fleet-based rollout sequencing ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing)



This document shows you how to manage Google Kubernetes Engine (GKE) cluster upgrades that use rollout sequencing with custom stages. You create a rollout sequence by using groups of clusters organized into [fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) and optionally, subsets of clusters from those fleets. You can choose how much [soak testing](https://en.wikipedia.org/wiki/Soak_testing) time you want after cluster upgrades are complete in a group (maximum 30 days). You can include both Autopilot and Standard clusters. For more information about how this feature works, see [About rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing). 

If you manage rollouts across multiple fleets, we recommend that you use a dedicated project to host your `RolloutSequence` object. This project acts as the parent and coordinator for the rollouts across the sequence. This project is typically not part of the sequence; that is, the project doesn't contain fleets or clusters which are part of the sequence.

## Before you begin

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * Ensure that you have existing Autopilot or Standard clusters. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * Optional: If you don't already have a dedicated Google Cloud project to host your `RolloutSequence` configuration, create one by using the Google Cloud console or another method. You can only create one `RolloutSequence` object per project.
  * Ensure that you have enabled the [required APIs for fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#enable_apis). These APIs must be enabled in your fleet host projects to create any type of rollout sequence. For your rollout sequence host project, enable the `gkehub.googleapis.com` API.
  * For Terraform instructions, ensure that you use the following version or later of the [`google`](https://registry.terraform.io/providers/hashicorp/google/latest) Terraform provider, depending on the actions that you want to take:

    * **Version 7.39.0 or later** is required for the following actions: 
      * Create a rollout sequence
      * Modify a rollout sequence
      * Choose what types of upgrades GKE performs in a rollout sequence
      * Ignore clusters in a rollout sequence
    * **Version 7.42.0 or later** is required for the following action: 
      * Roll out a specific version to a rollout sequence



### Required roles

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To create or modify a rollout sequence, you must have the Fleet Editor IAM role (`roles/gkehub.editor`) on each fleet host project in the rollout sequence and your rollout sequence host project, even if those projects are in multiple organizations. This role provides the following permissions:

  * `gkehub.rolloutsequences.create`
  * `gkehub.rolloutsequences.get`
  * `gkehub.rolloutsequences.list`
  * `gkehub.rolloutsequences.update`
  * `gkehub.rolloutsequences.delete`
  * `gkehub.fleet.update`



These permissions let you create, access, and modify a `RolloutSequence` object, and use fleets in the rollout sequence.

If you need to register or unregister clusters to a fleet, you need all of the following permissions:

  * [Cluster registration permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_cluster_registration_permissions) in your fleet host projects.
  * [Cluster admin permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_cluster_admin_permissions) for any GKE clusters to be registered.
  * [Cross-project cluster registration permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) for any GKE clusters to be registered to a fleet in a different project.



You can create rollout sequences using fleets hosted in projects in one or more organizations, if you have the necessary permissions for those projects.

For more information about the least-privileged IAM roles required for different tasks, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

## Configure a rollout sequence

To create a rollout sequence, your clusters must be organized into groups of fleets. You can also create granular stages that can target specific subsets of clusters within a fleet by using Kubernetes labels. For guidance on how to organize your clusters, see the [Community bank example](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#example). After you organize the clusters into groups and optionally label them, you create a rollout sequence by defining the ordered list of stages and the soak time for each group.

### Organize clusters into fleets

In a rollout sequence, we recommend enrolling all clusters in the same release channel. If the clusters are not enrolled in the same channel, GKE selects a version from the most conservative channel in the sequence. For example, if clusters are enrolled in both the Stable and Regular channels, GKE chooses the version from the Stable channel. We also recommend that all clusters run the same minor version in order to be eligible for the same auto-upgrade target version.

If you have already organized your clusters into fleets, you can skip the following steps and proceed to the Create subsets of clusters section.

  1. Group your clusters into fleets. You can organize your clusters by deployment environments such as Testing, Staging, and Production (recommended).
  2. [Register each cluster with a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster_on) based on your chosen grouping.



### Create subsets of clusters (optional)

To make a stage in your rollout sequence target specific clusters, you must label those clusters.

For example, to test a new version on a small subset of clusters before a full rollout, you might apply a `canary` label to those clusters. To add the `canary` label with value `true` to a cluster using the Google Cloud CLI, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --update-labels=canary=true
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `CONTROL_PLANE_LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.



The `--update-labels=canary=true` flag instructs GKE to apply the `canary` label to the cluster .

**Warning:** Updating labels on a cluster overwrites any existing labels on the cluster. If the cluster has existing labels that you want to keep, you must include those labels along with any new labels that you want to add when you update the cluster.

For more information about adding a label to a cluster, see [Add or update labels for existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#adding_or_updating_labels_for_existing_clusters).

### Create a rollout sequence with custom stages

A rollout sequence with custom stages defines the order of upgrades by declaratively defining the stages. With the gcloud CLI, you use a YAML file, and with Terraform, you add a resource block to your configuration. In performing the steps described in this section, you create a `RolloutSequence`.

To ensure that the sequence captures all clusters, each fleet must include a catch-all stage (a stage without a label selector). This catch-all stage captures all remaining clusters that GKE didn't select in earlier stages. If you assign a single cluster to multiple stages within one `RolloutSequence`, to resolve conflicts, GKE implicitly assigns the cluster only to the earliest stage.

The following example configurations creates three stages:

  * The first stage targets all clusters in the `dev` fleet. After the upgrade is complete, there is a soak time of 7 days (`7d`).
  * The second stage targets clusters in the `prod` fleet that have the label `canary=true`. After the upgrade is complete, there is a soak time of 7 days (`7d`).
  * The third stage targets the remaining clusters in the `prod` fleet. After the upgrade is complete, there is a soak time of 7 days (`7d`).




### gcloud

  1. Save the following manifest as `rollout-sequence.yaml`:
         
         - stage:
           fleet-projects:
           - projects/dev
           soak-duration: 7d
         - stage:
           fleet-projects:
           - projects/prod
           soak-duration: 7d
           label-selector: resource.labels.canary=='true'
         - stage:
           fleet-projects:
           - projects/prod
           soak-duration: 7d
         

Note the following:

     * `stage`: includes one or more fleets, or a subset of clusters within those fleets. Clusters in earlier stages must be fully upgraded and soaked before the sequence proceeds to the next stage. However, if a cluster has not finished upgrading 30 days after the upgrade process begins, GKE begins the soaking period.
     * `fleet-projects`: a list of fleets from which to select clusters for this stage. A fleet is identified by the project where the fleet is hosted. This project can be a different project from the project where clusters live, if the fleet contains cross-project memberships. The format to specify a fleet project is `projects/PROJECT_ID`.
     * `label-selector` (optional): selects a subset of clusters from the specified fleets. This field uses the [Common Expression Language (CEL)](https://cel.dev/) syntax and must begin with `resource.labels`.
     * `soak-duration`: the time to wait after upgrading all clusters in a preceding stage before proceeding to the next stage. Expressed in seconds, minutes, hours, and days.
  2. To create the rollout sequence that you defined in the `rollout-sequence.yaml` manifest, run the following command:
         
         gcloud container fleet rolloutsequences create ROLLOUT_SEQUENCE_NAME \
             --display-name=DISPLAY_NAME \
             --stage-config=rollout-sequence.yaml
         

Replace the following:

     * `ROLLOUT_SEQUENCE_NAME`: an immutable identifier that conforms to the [RFC-1034](https://datatracker.ietf.org/doc/html/rfc1034) specifications, for example, `test-rollout-sequence`.
     * `DISPLAY_NAME`: a human-readable string for your rollout sequence.



### Terraform

This section shows you how to create a rollout sequence with custom stages using Terraform. You can also use this resource to update the sequence. For more information, see the reference documentation for [`google_gke_hub_rollout_sequence`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_rollout_sequence).

  1. Add the following block to your Terraform configuration to create a rollout sequence resource:
         
         resource "google_gke_hub_rollout_sequence" "rollout_sequence" {
           rollout_sequence_id = "ROLLOUT_SEQUENCE_NAME"
           display_name        = "DISPLAY_NAME"
           stages {
             fleet_projects = ["projects/dev"]
             soak_duration  = "7d"
           }
           stages {
             fleet_projects = ["projects/prod"]
             cluster_selector {
               label_selector = "resource.labels.canary=='true'"
             }
             soak_duration  = "7d"
           }
           stages {
             fleet_projects = ["projects/prod"]
             soak_duration  = "7d"
           }
         }
         

Replace the following:

     * `ROLLOUT_SEQUENCE_NAME`: an immutable identifier that conforms to the [RFC-1034](https://datatracker.ietf.org/doc/html/rfc1034) specifications, for example, `test-rollout-sequence`.
     * `DISPLAY_NAME`: a human-readable string for your rollout sequence.



## Roll out a specific version

You can roll out a specific version to your rollout sequence. For more information, see [Rolling out a specific version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rolling-out-specific-version).

You can roll out a version to either the control planes or nodes of the clusters in your rollout sequence. You can independently select which versions to roll out to the control planes or nodes.

GKE can only roll out one version at a time in a stage to the control plane or nodes, respectively. If you have an existing rollout that is running in the first stage of the rollout sequence, GKE does the following, depending on whether you manage your rollout sequence with the gcloud CLI or Terraform:

  * **gcloud CLI** : when you run the command, an interactive prompt asks whether you want to cancel the existing rollout to create the rollout to the version that you specified. If you answer affirmatively, GKE cancels the existing rollout and creates a new rollout. If not, GKE keeps the existing rollout and doesn't create a new one as you originally requested in the command.
  * **Terraform** : when you update your Terraform configuration as described in the next section, GKE cancels the existing rollout if the rollout is running in the first stage.



### Roll out a version to the control planes in a rollout sequence

### gcloud

Run the following command:
    
    
    gcloud container fleet rolloutsequences upgrade ROLLOUT_SEQUENCE_NAME \
        --control-plane-version="CONTROL_PLANE_VERSION"
    

Replace the following:

  * `ROLLOUT_SEQUENCE_NAME`: the name of the rollout sequence.
  * `CONTROL_PLANE_VERSION`: the version to roll out. You can choose a specific version, such as `1.34.7-gke.1055000`, or use a version alias. For more information, see [Specifying cluster version](https://docs.cloud.google.com/kubernetes-engine/versioning#specifying_cluster_version).



### Terraform

If you use Terraform to manage your rollout sequence, you can roll out a specific version by adding to the block that you used to create the rollout sequence.

Add the following field to the block. You can add the field anywhere except between the `stages` blocks, which need to be consecutive:
    
    
    min_control_plane_version = "CONTROL_PLANE_VERSION"
    

Replace `CONTROL_PLANE_VERSION` with the version to roll out. You can choose a specific version, such as `1.34.7-gke.1055000`, or use a version alias. For more information, see [Specifying cluster version](https://docs.cloud.google.com/kubernetes-engine/versioning#specifying_cluster_version).

If you've already used this field to roll out a control plane version, the field remains in the block. Replace the previous version rolled out with the `CONTROL_PLANE_VERSION` you want to roll out this time.

### Roll out a version to the nodes in a rollout sequence

### gcloud

Run the following command:
    
    
    gcloud container fleet rolloutsequences upgrade ROLLOUT_SEQUENCE_NAME \
        --node-version="NODE_VERSION"
    

Replace the following:

  * `ROLLOUT_SEQUENCE_NAME`: the name of the rollout sequence.
  * `NODE_VERSION`: the version to roll out, for example, `1.34.7-gke.1055000`.



### Terraform

If you use Terraform to manage your rollout sequence, you can roll out a specific version by adding to the block that you used to create the rollout sequence.

Add the following field to the block. You can add the field anywhere except between the `stages` blocks, which need to be consecutive:
    
    
    min_node_version = "NODE_VERSION"
    

Replace `NODE_VERSION` with the version to roll out, for example, `1.34.7-gke.1055000`. If you've already used this field to roll out a node version, the field remains in the block. Replace the previous version rolled out with the `NODE_VERSION` you want to roll out this time.

## Check the status of a rollout

After you configure a rollout sequence, the system automatically creates `Rollout` objects to manage upgrades. You can observe and track the progress of these objects using Google Cloud CLI commands.

### List rollouts

To list all active and historical rollouts in your rollout sequence host project, run the following command:
    
    
    gcloud container fleet rollouts list --project=HOST_PROJECT_ID
    

Replace `HOST_PROJECT_ID` with the ID of your rollout sequence host project.

You can omit the `--project=HOST_PROJECT_ID` flag if you are already in the project where your rollout sequence is hosted.

The output is similar to the following:
    
    
    NAME                                              STATE      CREATE_TIME
    05eb251e4f19269e23-node-1-33-5-gke-1201000-t7mqd  COMPLETED  2025-10-30T20:07:46
    05eb251e4f19269e23-kcp-1-33-5-gke-1201000-djwst   COMPLETED  2025-10-30T18:07:06
    05eb251e4f19269e23-node-1-33-5-gke-1125000-6bxvu  COMPLETED  2025-10-23T17:46:54
    05eb251e4f19269e23-kcp-1-33-5-gke-1125000-2f6ct   RUNNING    2025-10-23T16:41:33
    

In the preceding output, rollout names that contain `kcp` refer to control plane upgrades, and names that contain `node` refer to node upgrades. The segment of the rollout name after `kcp` or `node` is derived from the GKE version.

### Describe a rollout

To get detailed information about a particular rollout, including the target version, state, and which clusters have been upgraded, use the `describe` command with the rollout ID that you obtained from the preceding command:
    
    
    gcloud container fleet rollouts describe ROLLOUT_ID \
      --project=HOST_PROJECT_ID
    

Replace the following:

  * `ROLLOUT_ID`: the rollout ID that you obtained when you listed the rollouts.
  * `HOST_PROJECT_ID`: the project ID where your rollout sequence is hosted.



For example:
    
    
    gcloud container fleet rollouts describe 927e9a989930cf3b55-kcp-1-32-4-gke-1106006 \
      --project=my-hostfleet
    

The output is similar to the following:
    
    
    createTime: '2025-05-26T11:47:29.909959672Z'
    membershipStates:
      projects/dev-project-id/locations/us-central1/memberships/c-1:
        lastUpdateTime: '2025-05-26T12:20:55.601542481Z'
        targets:
        - cluster:   projects/dev-project-id/locations/us-central1/clusters/c-1
          operation: //container.googleapis.com/v1/projects/dev-project-id/locations/us-central1/operations/operation-1234567890-abcdefg-hijklm-nopqrst
          state: SUCCEEDED
        stageAssignment: 1
      projects/dev-project-id/locations/us-central1/memberships/c-2:
        lastUpdateTime: '2025-05-26T12:22:57.151203493Z'
        targets:
        - cluster:   projects/dev-project-id/locations/us-central1/clusters/c-2
          operation: //container.googleapis.com/v1/projects/dev-project-id/locations/us-central1/operations/operation-987654321-ghijkl-mno-pqr-stu-vwxyz
          state: SUCCEEDED
        stageAssignment: 1
      projects/prod-project-id/locations/us-central1/memberships/c-1:
        lastUpdateTime: '2025-05-26T13:03:34.134308942Z'
        targets:
        - cluster: projects/prod-project-id/locations/us-central1/clusters/c-1
          operation: //container.googleapis.com/v1/projects/prod-project-id/locations/us-central1/operations/operation-567891234-efghij-klm-nopq-rstu-vwxyz
          state: SUCCEEDED
        stageAssignment: 2
      projects/prod-project-id/locations/us-central1/memberships/c-2:
        lastUpdateTime: '2025-05-26T13:06:34.025261641Z'
        targets:
        - cluster: projects/prod-project-id/locations/us-central1/clusters/c-1
          operation: //container.googleapis.com/v1/projects/prod-project-id/locations/us-central1/operations/operation-765432198-01a7b896-67c2-523-6fjjh4-icmdydh
          state: SUCCEEDED
        stageAssignment: 2
    name: projects/user-hostfleet/locations/global/rollouts/05eb251e4f19269e23-kcp-1-32-4-gke-1106006
    rolloutSequence: projects/project-id/locations/global/rolloutSequences/my-sequence
    state: COMPLETED
    updateTime: '2025-07-22T07:36:51.052691989Z'
    versionUpgrade:
      desiredVersion: 1.32.4-gke.1106006
      type: TYPE_CONTROL_PLANE
    stages:
    - state: COMPLETED
      endTime: '2025-05-26T12:22:28.828506491Z'
      stageNumber: 1
      startTime: '2025-05-26T11:48:28.772658427Z'
      soakDuration: 600s
    - state: COMPLETED
      endTime: '2025-05-26T13:06:20.026390832Z'
      stageNumber: 2
      startTime: '2025-05-26T12:32:38.419372153Z'
      soakDuration: 600s
    

### Status information for a rollout

When you describe a rollout, the `stages` and `membershipStates` fields of the output provide the progress status of each stage and cluster within that stage, respectively.

The following table lists the potential statuses of a stage:

Status | Description  
---|---  
`PENDING` | The upgrade has not yet started for this stage.  
`RUNNING` | The upgrade is in progress for this stage. If you have configured a maintenance window for the clusters in the stage, GKE waits for the window to open before upgrading the clusters.  
`SOAKING` | All clusters in this stage have completed their upgrades, and the stage is in its configured soaking period.  
`FORCED_SOAKING` | The upgrade took more than the maximum upgrade time (30 days), and therefore GKE force-started the soaking phase. The upgrade still continues on any remaining clusters.  
`COMPLETED` | The stage has finished soaking, and the rollout proceeds to the next stage.  
  
The following table lists the potential statuses of a cluster within a sequence:

Status | Description  
---|---  
`PENDING` | The upgrade is pending on this cluster.  
`INELIGIBLE` | This cluster is ineligible for the upgrade, possibly due to a version discrepancy. The reason for ineligibility is provided in the output.  
`RUNNING` | The upgrade is in progress on this cluster.  
`SUCCEEDED` | The upgrade has successfully completed on this cluster.  
`FAILED` | The upgrade has failed on this cluster. Failed targets are retried indefinitely while their stage is active (in a `RUNNING` or `FORCED_SOAKING` state).  
  
## Manage a rollout

You can manage an individual rollout by using the instructions provided in the following sections. For more information about managing a rollout and the corresponding actions that you can take, see [Managing a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#managing-a-rollout).

For managing an entire rollout sequence, and not only one specific rollout, see the following section, Manage a rollout sequence.

### Pause a rollout

You can pause an active rollout. For more information about this action, see [Pausing a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#pausing-rollout).

To pause a rollout, run the following command:
    
    
    gcloud container fleet rollouts pause ROLLOUT_ID
    

Replace `ROLLOUT_ID` with the ID of the rollout that you want to pause. To get the rollout IDs for the rollouts in your rollout sequence, see List rollouts.

### Resume a rollout

You can resume a paused rollout that's been paused for less than 90 days. For more information about this action, see [Resuming a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#resuming-rollout).

To resume a paused rollout, run the following command:
    
    
    gcloud container fleet rollouts resume ROLLOUT_ID
    

Replace `ROLLOUT_ID` with the ID of the rollout that you want to resume. To get the rollout IDs for the rollouts in your rollout sequence, see List rollouts.

### Cancel a rollout

You can cancel a rollout, including both rollouts that are active or have been paused. You can't cancel [rollouts for mandatory automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rollouts-mandatory-auto-upgrades). For more information about canceling rollouts, see [Canceling a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#canceling-rollout).

To cancel a rollout, run the following command:
    
    
    gcloud container fleet rollouts cancel ROLLOUT_ID
    

Replace `ROLLOUT_ID` with the ID of the rollout that you want to cancel. To get the rollout IDs for the rollouts in your rollout sequence, see List rollouts.

### Complete a rollout stage

You can complete a rollout stage if you're ready for upgrades to proceed to the next stage. For more information about this action, see [Completing a rollout stage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#completing-rollout-stage).

To complete a rollout stage, run the following command:
    
    
    gcloud container fleet rollouts force-complete-stage ROLLOUT_ID \
        --stage=STAGE
    

Replace the following:

  * `ROLLOUT_ID`: the ID of the rollout where you want to complete a stage. To get the rollout IDs for the rollouts in your rollout sequence, see List rollouts.
  * `STAGE`: the stage that you want to complete now. For example, if you want to complete the second stage, enter `2`. The stage must be running or soaking to use this command.



### Ignore a cluster in a rollout sequence for a specific rollout

You can have GKE ignore a cluster in a rollout sequence if you don't want the cluster to be upgraded as part of an active rollout. However, this action removes the cluster from the rollout sequence for active and future rollouts, not only active rollouts.

To perform this action to prevent a cluster from being upgraded in an active rollout, see Ignore a cluster in a rollout sequence.

## Manage a rollout sequence

You can control automatic cluster upgrades with rollout sequencing in several ways, as explained in the following sections.

If you want to manage one rollout from a rollout sequence instead of the entire rollout sequence and all its rollouts, see Manage a rollout.

### List your rollout sequence

To list the rollout sequence in your host project, run the following command:
    
    
    gcloud container fleet rolloutsequences list --project=HOST_PROJECT_ID
    

Replace `HOST_PROJECT_ID` with the ID of your rollout sequence host project.

### Describe a rollout sequence

To see the details of a specific rollout sequence, run the following command:
    
    
    gcloud container fleet rolloutsequences describe ROLLOUT_SEQUENCE_NAME \
      --project=HOST_PROJECT_ID
    

Replace the following:

  * `ROLLOUT_SEQUENCE_NAME`: the name of the rollout sequence.
  * `HOST_PROJECT_ID`: the ID of your rollout sequence host project.



The output is similar to the following:
    
    
    createTime: '2025-10-23T16:40:16.403871189Z'
    displayName: my-display-name
    name: projects/HOST_PROJECT_ID/locations/global/rolloutSequences/ROLLOUT_SEQUENCE_NAME
    stages:
    - clusterSelector:
        labelSelector: resource.labels.canary=='true'
      fleetProjects:
      - projects/FLEET_PROJECT_ID
      soakDuration: 600s
    - fleetProjects:
      - projects/FLEET_PROJECT_ID
      soakDuration: 300s
    uid: 5c5b2ac8-9d76-45f9-92ca-5e6bd3fbcaef
    updateTime: '2025-10-23T17:11:57.285678399Z'
    

### Choose what types of upgrades GKE performs in a rollout sequence

By default, GKE performs all types of cluster upgrades in a rollout sequence. You can restrict the scope of cluster upgrades in a rollout sequence to perform only specific types of upgrades. For information, see [Choosing what types of upgrades GKE performs in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#what-type-of-upgrades-scope).

To designate what types of upgrades you want GKE to perform in a rollout sequence, follow these instructions, depending on how you manage your rollout sequence:

### gcloud

Run the following command:
    
    
    gcloud container fleet rolloutsequences update ROLLOUT_SEQUENCE_NAME \
        --auto-rollout-scope=TYPES_OF_UPGRADES
    

Replace the following:

  * `ROLLOUT_SEQUENCE_NAME`: the name of the rollout sequence.
  * `TYPES_OF_UPGRADES`: the list of upgrades to perform, which can be the following:

    * `all`: the default, GKE performs all types of cluster upgrades in the rollout sequence.
    * `none`: GKE doesn't perform any cluster upgrades in the rollout sequence, except for [rollouts for mandatory automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rollouts-mandatory-auto-upgrades).
    * One or more of the following; if plural, put the values in a comma-separated list with no spaces:

      * `control-plane-patch`: GKE performs [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) to later patch versions.
      * `control-plane-minor`: GKE performs [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) to later minor versions.
      * `nodes-patch`: GKE performs [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades) to later patch versions.
      * `nodes-minor`: GKE performs [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades) to later minor versions.

For example, if you want only patch versions to roll out in the rollout sequence, specify the `control-plane-patch,nodes-patch` configuration.




### Terraform

If you use Terraform to manage your rollout sequence, you can designate what types of upgrades you want GKE to perform in that rollout sequence by adding to the block that you used to create the rollout sequence.

Add the following field to the block. You can add the field anywhere except between the `stages` blocks, which need to be consecutive:
    
    
    auto_upgrade_config {
      rollout_creation_scope {
        upgrade_types = [
          UPGRADE_TYPES
        ]
      }
    }
    

Replace `UPGRADE_TYPES` with the list of upgrades to perform, which can be one or more of the following (each in quotation marks):

  * `"CONTROL_PLANE_PATCH"`: GKE performs [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) to later patch versions.
  * `"CONTROL_PLANE_MINOR"`: GKE performs [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) to later minor versions.
  * `"NODE_PATCH"`: GKE performs [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades) to later patch versions.
  * `"NODE_MINOR"`: GKE performs [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades) to later minor versions.



For example, if you want only patch versions to roll out in the rollout sequence, specify the `upgrade_types = ["CONTROL_PLANE_PATCH", "NODE_PATCH"]` configuration.

If you set `upgrade_types = []`, GKE doesn't perform any cluster upgrades in the rollout sequence, except for [rollouts for mandatory automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rollouts-mandatory-auto-upgrades).

To revert to the default behavior where GKE performs all types of cluster upgrades in the rollout sequence, specify the `upgrade_types = ["CONTROL_PLANE_PATCH", "CONTROL_PLANE_MINOR", "NODE_PATCH", "NODE_MINOR"]` configuration. Or, remove the `auto_upgrade_config` block from your Terraform configuration.

### Modify a rollout sequence

**Caution:** Some modifications of an existing rollout sequence can cause GKE to cancel existing rollouts. For more information, see [Modifying a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#modifying-rollout-sequence).

You can modify an existing rollout sequence after you've created it. Modify your rollout sequence with the following instructions, depending on how you're managing your rollout sequence.

### gcloud

If you use the gcloud CLI to manage your rollout sequence, you can edit the YAML configuration file where you defined the sequence. For example, you can update the soak time for a stage or update the stage to change the order of upgrades. After you edit the file, apply the changes.

For example, if you defined the original rollout sequence in a file named `rollout-sequence.yaml`, edit the file as required. Then, run the following command:
    
    
    gcloud container fleet rolloutsequences update test-rollout-sequence \
      --display-name="My Updated Rollout Sequence" \
      --stage-config=rollout-sequence.yaml
    

### Terraform

If you use Terraform to manage your rollout sequence, modify the rollout sequence by modifying the block that you used to create the rollout sequence.

### Create a cluster that matches the target version of a rollout stage

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a GKE cluster running the target version for a stage in your rollout sequence, specify the `upgrade-target` alias with the `--cluster-version` flag, register the cluster to the fleet, and apply matching cluster labels at creation time (if the stage uses a label selector). If no rollout is active or completed for the sequence, the `upgrade-target` alias resolves to the [auto-upgrade target](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target) for the cluster's release channel.

To create a cluster with the `upgrade-target` alias, run one of the following commands:

### Autopilot
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --fleet-project=FLEET_HOST_PROJECT_ID \
        --labels=STAGE_KEY=STAGE_VALUE \
        --cluster-version=upgrade-target \
        --release-channel=CHANNEL
    

### Standard
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --fleet-project=FLEET_HOST_PROJECT_ID \
        --labels=STAGE_KEY=STAGE_VALUE \
        --cluster-version=upgrade-target \
        --release-channel=CHANNEL
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster. For Autopilot clusters, specify a region.
  * `FLEET_HOST_PROJECT_ID`: the project ID of the fleet host project referenced by the rollout sequence. The `--fleet-project` flag is required if the cluster is in a different project than the fleet host project. If the cluster is in the same project, you can specify `--enable-fleet` instead of `--fleet-project=FLEET_HOST_PROJECT_ID`.
  * `STAGE_KEY=STAGE_VALUE`: the label key and value matching your stage's label selector. Omit the `--labels` flag if the stage doesn't use a label selector.
  * `CHANNEL`: the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) used by the rollout sequence (such as `regular` or `stable`).



### Ignore a cluster in a rollout sequence

You can have GKE ignore a cluster in a rollout sequence. You can ignore one or more clusters in a rollout sequence. For more information, see [Ignoring a cluster in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#ignoring-cluster-rollout-stage).

To have GKE ignore a cluster in a rollout sequence, do the following steps:

  1. [Add a label](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#adding_or_updating_labels_for_existing_clusters) to the cluster that you want GKE to ignore, or use an existing label. You can have GKE ignore, for example, either a label such as `status`, or ignore a label when it has a specific value, such as `status=quarantine`.
  2. Set the rollout sequence to ignore clusters with this label. To do this, perform the following steps, depending on how you manage your rollout sequence:

### gcloud

Run the following command:
         
         gcloud container fleet rolloutsequences update ROLLOUT_SEQUENCE_NAME \
             --ignored-clusters-selector="resource.labels.LABEL_TO_IGNORE"
         

Replace the following:

     * `ROLLOUT_SEQUENCE_NAME`: the name of the rollout sequence.
     * `LABEL_TO_IGNORE`: the name of the label for clusters that GKE should ignore for the rollout sequence.

### Terraform

If you use Terraform to manage your rollout sequence, add the following field to the block that you used to created the rollout sequence. You can add the field anywhere except between the `stages` blocks, which need to be consecutive:
    
    ignored_clusters_selector {
      label_selector = "resource.labels.LABEL_TO_IGNORE"
    }
    

Replace `LABEL_TO_IGNORE` with the name of the label for clusters that GKE should ignore for the rollout sequence.




These instructions configure GKE to ignore one type of label in the rollout sequence. If you want to ignore multiple labels or create more complex expressions for how to ignore clusters with specific labels, you can pass values to this field by using the [CEL](https://cel.dev/) expression syntax. All labels must use the `resource.labels.` prefix.

#### Add a cluster back to a rollout sequence

If you followed the instructions in the previous section for GKE to ignore a cluster in a rollout sequence, you can undo this action. If you want GKE to not ignore clusters anymore, remove the ignore selector with the following instructions, depending on how you manage your rollout sequence:

### gcloud

Run the following command:
    
    
    gcloud container fleet rolloutsequences update ROLLOUT_SEQUENCE_NAME \
        --clear-ignored-clusters-selector
    

Replace `ROLLOUT_SEQUENCE_NAME` with the name of the rollout sequence.

This command resets the ignore selector so that GKE won't ignore any clusters in the sequence.

### Terraform

If you use Terraform to manage your rollout sequence, remove the `ignored_clusters_selector` block from the block that you used to created the rollout sequence.

Or, if you want GKE to not ignore a specific cluster, [remove the labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#removing_cluster_labels) from the cluster.

### Delete a rollout sequence

To delete a rollout sequence, run the following command:
    
    
    gcloud container fleet rolloutsequences delete ROLLOUT_SEQUENCE_NAME \
      --project=HOST_PROJECT_ID
    

Replace the following:

  * `ROLLOUT_SEQUENCE_NAME` with the name of the rollout sequence.
  * `HOST_PROJECT_ID` with the ID of your rollout sequence host project.



When you delete a rollout sequence, any rollouts that are in progress for that sequence are cancelled. The clusters that were part of the sequence revert to the default auto-upgrade behavior for their enrolled release channel.

## Migrate an existing rollout sequence to use custom stages

If you use the [fleet-based version of rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing), you can migrate to a sequence that uses custom stages by creating a new `RolloutSequence` that references your existing fleets. Note that this version of rollout sequencing doesn't have Google Cloud console support.

To migrate your rollout sequence, complete the following steps:

  1. Optionally, before you migrate the sequence, make a copy of your current rollout sequence configuration. To make a copy of the configuration, do one of the following:

     * **gcloud CLI** : run the command to [check the status of a fleet-based rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#command-status). Save the output of the command.
     * **Terraform** : save the Terraform configuration.

We recommend that you don't delete your fleet-based rollout sequence, to make it easier to revert to the earlier version of rollout sequencing, if necessary. You don't need to delete the fleet-based rollout sequence for the rollout sequence with custom stages to work, because GKE adheres only to the rollout sequence with custom stages when both exist.

  2. Create a dedicated Google Cloud project to host your rollout sequence. This project is typically not part of the sequence; that is, the project doesn't contain fleets or clusters which are part of the sequence.

  3. If you want the rollout sequence to include specific clusters within a fleet, add labels to those clusters. This step is optional.

  4. Follow the instructions in Create a rollout sequence with custom stages.

For example, the following manifest, which is named `rollout-sequence-migrate.yaml`, references the existing fleets in a previous rollout sequence. This manifest describes three stages, including a `canary` stage in the `prod` fleet:
         
         - stage:
           fleet-projects:
           - projects/dev
           soak-duration: 604800s
         - stage:
           fleet-projects:
           - projects/prod
           soak-duration: 604800s
           label-selector: canary=true
         - stage:
           fleet-projects:
           - projects/prod
           soak-duration: 604800s
         




Immediately after you define a new `RolloutSequence` for your fleets, GKE begins upgrading the fleets according to the new sequence, and removes the previous configuration.

## Migrate a rollout sequence with custom stages to the previous rollout sequence

This section describes how to revert from rollout sequencing with custom stages back to the fleet-based rollout sequencing model. This process involves deleting the new `RolloutSequence` and restoring your original fleet-based configuration.

### Prevent out-of-order upgrade during migration

To avoid unintended or out-of-order upgrades while you are reconfiguring your sequence, [apply a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) to your production clusters. This step temporarily pauses all automatic upgrades on those clusters. For example, you can configure a maintenance exclusion of type `no upgrades` on your production clusters.

### Delete the rollout sequence

Delete the `RolloutSequence` object that manages your clusters. This deletion disengages the custom stages feature.

To delete the `RolloutSequence`, run the following command:
    
    
    gcloud container fleet rolloutsequences delete ROLLOUT_SEQUENCE_NAME
    

Replace `ROLLOUT_SEQUENCE_NAME` with the name of your rollout sequence.

### Restore your earlier rollout sequence configuration (without custom stages)

After you delete the `RolloutSequence`, you can restore your original fleet-based configuration. This process involves re-creating the `clusterupgrade` features with their original parameters, including the `upstreamFleet` links and soak times for each fleet in your sequence. For more information, see [Create a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#create-rollout-sequence).

### Remove the maintenance exclusions

After you restore your original fleet-based rollout sequencing configuration, [remove the maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#remove-exclusions) you applied in the first step in this section. GKE resumes the automatic upgrades, now governed by your restored fleet-based sequence.

## What's Next

  * Learn more about [cluster upgrades with rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
