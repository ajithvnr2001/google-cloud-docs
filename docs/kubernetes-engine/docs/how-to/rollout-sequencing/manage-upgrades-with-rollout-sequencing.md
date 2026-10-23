---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing/
title: Sequence the rollout of cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:33.085464+00:00
---

# Sequence the rollout of cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Sequence the rollout of cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Rollout sequencingkeyboard_arrow_down

  * [ Rollout sequencing with custom stages ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing)
  * [ Fleet-based rollout sequencing ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing)



This document shows you how to manage GKE cluster upgrades with rollout sequencing. To learn more about how this feature works, see [About cluster upgrades with rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing).

**Best practice** : 

Use [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rs-custom-stages) if you're configuring an environment for the first time.

## Before you begin

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * Ensure that you have existing Autopilot or Standard clusters. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * Ensure that you have enabled the [required APIs for fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#enable_apis). These APIs must be enabled in your fleet host projects to create any type of rollout sequence.
  * For Terraform instructions, ensure that you use the version 5.13.0 or later of the [`google`](https://registry.terraform.io/providers/hashicorp/google/latest) provider.



### Required roles

To create or modify a rollout sequence, you need to be granted the `roles/gkehub.editor` IAM role on each project in the rollout sequence. The [Fleet Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (formerly GKE Hub Editor) role provides the `gkehub.features.create` and `gkehub.fleet.update` permissions, which are needed to access and modify fleet-related resources between projects. This role provides the necessary permissions to define the upgrade strategy, access and modify relevant resources, and initiate and manage the rollout process.

If you need to register or unregister clusters to a fleet, you need all of the following permissions:

  * [Cluster registration permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_cluster_registration_permissions), in your fleet host projects.
  * [Cluster admin permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_cluster_admin_permissions) for any GKE clusters to be registered.
  * [Cross-project cluster registration permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) for any GKE clusters to be registered to a fleet in a different project.



For more information about the least-privileged IAM roles required for different tasks, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

## Configure a rollout sequence

This document explains how to create a rollout sequence using groups of clusters organized by [fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

You can create a sequence of up to five groups of clusters and you can choose the [soak testing](https://en.wikipedia.org/wiki/Soak_testing) time that you want after cluster upgrades are complete in a group (maximum 30 days). You can include both Autopilot and Standard clusters.

To create a rollout sequence, your clusters must be organized into groups of fleets. For guidance on how to organize your clusters, see [the community bank example](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#example). After you organize clusters into groups, you create a rollout sequence by defining the upstream group relationships and each group's soak time. Upstream, in a rollout sequence, refers to the previous group, and downstream refers to the next group.

### Organize your clusters into groups

In a rollout sequence, all clusters in all groups must be enrolled in the same release channel and be on the same minor version. If these requirements are not met and there are version discrepancies between clusters, this can cause issues with the version rollout. For more information, see [Fleet-based rollout eligibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#rollout-eligibility).

If you have already organized your clusters into fleets, you can skip the following steps and proceed to Create a rollout sequence.

  1. Group your clusters into fleets. You can organize your clusters by deployment environments such as Testing, Staging, and Production, as shown in the [example fleet-based rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing#fleet-based-sequence).

  2. [Register each cluster with a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster) based on your chosen grouping.




### Create a rollout sequence

A rollout sequence is organized as a [linked list](https://en.wikipedia.org/wiki/Linked_list) with up to five elements.

When you create a rollout sequence, you set the following properties for each fleet of clusters:

  * **Upstream group:** The upstream fleet, which qualifies new versions for the downstream group. You don't set an upstream group for the first group in a sequence.
  * **Soak time:** The soak time for a group is the time between when upgrades complete (or rollout has taken 30 days) and when upgrades can begin on the downstream group. To learn more, see [How version qualification works in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#version-qualification).




### Console

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Rollout Sequencing** page in the Google Cloud console.

[Go to Rollout Sequencing](https://console.cloud.google.com/kubernetes/upgrades)

  2. Click **Create rollout sequence**.

  3. In the **Create a rollout sequence** pane, select the first two fleets in the sequence:

     1. In the **Fleet 1** section, select the first fleet in the sequence.
     2. In the **Soak time for upstream fleet** section, set the soak time for the first fleet using the **Days** , **Hours** , and **Minutes** fields.
     3. In the **Fleet 2** section, select the second fleet in the sequence.
     4. Click **Create**.
  4. Optional: If you want to have three or more fleets in this rollout sequence, do the following additional steps:

     1. In the **Rollout graph** , click the element for the second fleet.
     2. Click add **Add downstream fleet**.
     3. In the **Soak time for upstream fleet** section, set the soak time for the second fleet using the **Days** , **Hours** , and **Minutes** fields.
     4. In the **Next fleet in the sequence** section, select the third fleet in the sequence.
     5. Click **Save**.
     6. Repeat the previous steps if you want to add a fourth or fifth fleet.



### gcloud

The following instructions use the `gcloud container fleet clusterupgrade update` command, however you can set the same properties with the `gcloud container fleet clusterupgrade create` command.

For each of the following commands, replace `SOAK_TIME` with the soak time for the fleet you are updating.

Create a rollout sequence:

  1. Set the soak time for the first fleet in the sequence:
         
         gcloud container fleet clusterupgrade update \
             --default-upgrade-soaking=SOAK_TIME \
             --project=FIRST_FLEET_PROJECT_ID
         

Replace `FIRST_FLEET_PROJECT_ID` with the project ID of the fleet host project.

  2. Set the upstream fleet and the soak time for the second fleet in the sequence:
         
         gcloud container fleet clusterupgrade update \
             --upstream-fleet=FIRST_FLEET_PROJECT_ID \
             --default-upgrade-soaking=SOAK_TIME \
             --project=SECOND_FLEET_PROJECT_ID
         

Replace `FIRST_FLEET_PROJECT_ID` with the project ID of the first fleet's host project, and `SECOND_FLEET_PROJECT_ID` with the project ID of the fleet host project.

  3. Optional: If you want to have more than two fleets in a rollout sequence, set the upstream fleet for the next fleets in the sequence.

The following command sets the upstream fleet for the third fleet in the sequence. If you'd like to add a fourth or fifth fleet, repeat this step, following the same pattern to replace the variables with the project IDs for the respective fleet hosts projects (previous fleet and next fleet).

**Note:** You must set a soak time for each fleet, including the last fleet in a rollout sequence.

Set the upstream fleet for the next fleet in the sequence:
         
         gcloud container fleet clusterupgrade update \
             --upstream-fleet=SECOND_FLEET_PROJECT_ID \
             --default-upgrade-soaking=SOAK_TIME \
             --project=THIRD_FLEET_PROJECT_ID
         

Replace `SECOND_FLEET_PROJECT_ID` with the project ID of the second fleet's host project, and `THIRD_FLEET_PROJECT_ID` with the project ID of the fleet host project.




### Terraform

This section shows you how to create a fleet-based sequence using Terraform. You can also use this resource to update the sequence. To learn more, see the reference documentation for [`google_gke_hub_feature`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature).

For each of the following commands, replace `SOAK_TIME` with the soak time for the fleet you are updating.

Create a rollout sequence:

  1. Add the following block to your Terraform configuration to set the soak time for the first fleet in the sequence:
         
         resource "google_gke_hub_feature" "feature" {
           name = "clusterupgrade"
           location = "global"
           spec {
             clusterupgrade {
               upstream_fleets = []
               post_conditions {
                 soaking = "SOAK_TIME"
               }
             }
           }
           project = "FIRST_FLEET_PROJECT_ID"
         }
         

Replace `FIRST_FLEET_PROJECT_ID` with the project ID of the fleet host project.

  2. Add the following block to your Terraform configuration to set the upstream fleet and the soak time for the second fleet in the sequence:
         
         resource "google_gke_hub_feature" "feature" {
           name = "clusterupgrade"
           location = "global"
           spec {
             clusterupgrade {
               upstream_fleets = ["FIRST_FLEET_PROJECT_ID"]
               post_conditions {
                 soaking = "SOAK_TIME"
               }
             }
           }
           project = "SECOND_FLEET_PROJECT_ID"
         }
         

Replace `FIRST_FLEET_PROJECT_ID` with the project ID of the first fleet's host project, and `SECOND_FLEET_PROJECT_ID` with the project ID of the fleet host project.

  3. Optional: If you want to have three fleets in a rollout sequence, add the following block to your Terraform configuration to set the upstream fleet for the fleet in the sequence:
         
         resource "google_gke_hub_feature" "feature" {
           name = "clusterupgrade"
           location = "global"
           spec {
             clusterupgrade {
               upstream_fleets = ["SECOND_FLEET_PROJECT_ID"]
               post_conditions {
                 soaking = "SOAK_TIME"
               }
             }
           }
           project = "THIRD_FLEET_PROJECT_ID"
         }
         

Replace `SECOND_FLEET_PROJECT_ID` with the project ID of the second fleet's host project, and `THIRD_FLEET_PROJECT_ID` with the project ID of the fleet host project.

Repeat this step if you want to add a fourth or fifth fleet.




## Check status of a rollout sequence

You can check the status of a rollout sequence with either of the following methods:

  * Monitor a visual representation of a rollout sequence in the Google Cloud console (Preview).
  * Use the gcloud CLI or [GKE Hub API](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.clusterupgrade.v1) to check the status of a rollout sequence.



To view a rollout sequence with either of the preceding methods, ensure that you have the `roles/gkehub.viewer` IAM role for each fleet host project, especially if the sequence includes fleets in different projects. If you don't have the required permissions for a project, you get an error when you check the status of the sequence.

### Monitor a rollout sequence in the Google Cloud console

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Rollout Sequencing** page in the Google Cloud console.

[Go to Rollout Sequencing](https://console.cloud.google.com/kubernetes/upgrades)

  2. View the sequence in the section **Monitor your rollout sequence**. If you don't see a rollout sequence, switch to a different rollout sequence, or create a rollout sequence if you haven't already done so.




#### How to use the console to monitor a rollout sequence

On this page, you can view the rollout sequence associated with your project's fleet. You can do the following to see the progress of a rollout sequence:

  * View the entire rollout sequence, or see the statuses of individual fleets and clusters within those fleets, as well as the soak time between fleets. You can also view the sequence where there is no active upgrade, if you want to check the configuration of the sequence.
  * Filter by upgrade type (control plane or node upgrade) and specific version (for example, 1.31.6-gke.500).



You can visually monitor your entire rollout sequence while GKE upgrades all the clusters in the sequence, qualifying a new version across environments before upgrading your production environment clusters. While monitoring, you can manage a rollout sequence with the gcloud CLI, making any changes as needed.

#### Switch to a different rollout sequence

This page shows the rollout sequence if the active project in the Google Cloud console is a fleet host project for a fleet that is enrolled in a rollout sequence.

If you want to view a different rollout sequence, select a fleet host project associated with a different rollout sequence from the project picker at the top of the page.

### Use the gcloud CLI

You can check the status of a rollout sequence, a fleet in the sequence, or individual clusters within a fleet.

  * To check the status of a fleet-based rollout sequence, run the following command:
        
        gcloud container fleet clusterupgrade describe \
            --show-linked-cluster-upgrade --project=FLEET_PROJECT_ID
        

Replace `FLEET_PROJECT_ID` with the project ID of the host project for any fleet in the sequence. See the reference [`gcloud container fleet clusterupgrade describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/describe) for a complete list of flags.

  * To check the status of only one fleet in the sequence, in the preceding command, replace the `--show-linked-cluster-upgrade` flag with the `--show-cluster-upgrade` flag.

  * To check the status of individual clusters within a fleet, run the following command in the fleet host project and see the `membershipStates` section:
        
        gcloud container fleet features describe clusterupgrade
        




The following section describes the status information in the resulting output.

### Status information for a rollout sequence

When you check the status of a version rollout, you can see the progress of each group and cluster within that group.

See the following table for the potential statuses of a cluster or group:

Status | For a single cluster | For a fleet  
---|---|---  
INELIGIBLE | This cluster is ineligible for this upgrade | One or more clusters in this group are ineligible for this upgrade.  
PENDING | The upgrade is pending on the cluster or some of its Standard node pools or groups of nodes in an Autopilot cluster. | The upgrade hasn't started on any of the clusters in the group.  
IN_PROGRESS | The upgrade is in progress on the cluster. | The upgrade has started on at least one cluster but hasn't finished on all clusters.  
SOAKING | The upgrade has finished on the cluster and hasn't finished soaking. | The upgrade has finished on all clusters and hasn't finished soaking.  
FORCED_SOAKING | The upgrade took more than the maximum upgrade time (30 days) and therefore we forced it to enter the soaking phase. The upgrade can still continue in the cluster. | The upgrade took more than the maximum upgrade time (30 days) and therefore we forced it to enter the soaking phase. The upgrade can still continue in the clusters.  
COMPLETE | The upgrade is treated as "done", meaning that the upgrade has finished soaking on this cluster. | The upgrade is treated as "done" and ready to be consumed by the downstream group, meaning that the upgrade has finished soaking.  
  
In the output of these commands, the`clusterUpgrade(s).spec` and `clusterUpgrade(s).state` attributes contain additional information about the cluster upgrade such as soaking time, cluster upgrade overrides, and upgrade status.

## Manage a rollout sequence

You can control automatic cluster upgrades with rollout sequencing in several ways, explained in the following sections.

### Change the soak time for a group

You can change the default soak time for a group or change the soak time for when that group upgrades to a specific version. The maximum is 30 days.

#### Update the default soak time

You can update the default soak time in the Google Cloud console (Preview) or with the gcloud CLI.

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Rollout Sequencing** page in the Google Cloud console.

[Go to Rollout Sequencing](https://console.cloud.google.com/kubernetes/upgrades)

  2. View the sequence in the section **Monitor your rollout sequence**. If you don't see a rollout sequence, switch to a different rollout sequence, or create a rollout sequence if you haven't already done so.

  3. In the **Rollout graph** , click the **Soak time** element after the element of the fleet where you want to update the soak time.

  4. Click edit **Edit soak time**.

  5. In the section **Set a new soak time** , enter a new soak time using the **Days** , **Hours** , and **Minutes** fields.

  6. To save the settings, click **Save**.




### gcloud

To change the default soak time for a group, use the gcloud CLI commands from the instructions to Create a rollout sequence, omitting the flags to set the upstream group.

#### Override the default soak time

You can change the soak time for a specific version rollout to be different than the default soak time for the group. For example, if you have already qualified a new version and are ready for upgrades to begin in the next group, you can set the soak time to zero. You can also use it if you want more time than the default soaking time to qualify a specific version.

As the soak time is set on a per-group basis, if you want to override the soak time for other groups in this sequence, update them using this same command with the fleet name replaced.

For the instructions in this section, replace the following variables:

  * `SOAK_TIME`: the soak time to use other than the default (for example, "0d" if you want to skip the soak time for one version rollout).
  * `UPGRADE_NAME`: the type of upgrade, either `k8s_control_plane` for control plane upgrades or `k8s_node` for node upgrades.
  * `VERSION`: the GKE version where you want to override the default soak time after the version (for example, 1.25.2-gke.400) has been rolled out to this group.




### gcloud

Run the following command in the host project of the fleet where you want to override the soak time used for the version rollout of a specific version.
    
    
    gcloud container fleet clusterupgrade update
        --add-upgrade-soaking-override=SOAK_TIME \
        --upgrade-selector=name=UPGRADE_NAME,version=VERSION
    

### Terraform

Add the following `gke_upgrades_overrides` block to your Terraform configuration within the [`clusterupgrade` block](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#example-usage---gkehub-feature-clusterupgrade) to override the soak time used for the version rollout of a specific version:
    
    
    gke_upgrade_overrides {
        upgrade {
          name = "UPGRADE_NAME"
          version = "VERSION"
        }
        post_conditions {
          soaking = "SOAK_TIME"
        }
      }
    

### Update the groups in a rollout sequence

You can update an existing rollout sequence to add, remove, or change the order of groups in the sequence. To make these changes, update the associations between groups.

You can perform these steps in the Google Cloud console (Preview) or with the gcloud CLI.

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Rollout Sequencing** page in the Google Cloud console.

[Go to Rollout Sequencing](https://console.cloud.google.com/kubernetes/upgrades)

  2. View the sequence in the section **Monitor your rollout sequence**. If you don't see a rollout sequence, switch to a different rollout sequence, or create a rollout sequence if you haven't already done so.

  3. In the **Rollout graph** , click the elements for the existing fleets in the sequence. After you click those elements, you can do some of the following actions to make the changes:

     * Click add **Add downstream fleet**.
     * Click add **Add upstream fleet**.
     * Click delete **Remove fleet**.



You can do actions such as the following:

  * Add another fleet to the end of the rollout sequence by adding a downstream fleet to the last fleet in the sequence.
  * Add another fleet to the start of the rollout sequence by adding an upstream fleet to the first fleet in the sequence.
  * Change the order of the fleets in the rollout sequence by removing fleets, then adding the fleets back with a different upstream or downstream fleet.
  * Remove the first fleet in the rollout sequence.
  * Remove the last fleet in the rollout sequence.
  * Remove the middle fleet in the rollout sequence, after removing the first or last fleet in the sequence.



### gcloud

To add or change upstream fleets, use the `gcloud container fleet clusterupgrade update` command with the `--upstream-fleet` flag. To remove an upstream fleet, use the `--reset-upstream-fleet` flag .

You can do actions such as the following:

  * Add another fleet to the start of the rollout sequence by adding an upstream fleet to the first fleet in the sequence.
  * Change the order of the fleets in the rollout sequence by changing the upstream fleet associations.
  * Remove the first fleet in the rollout sequence by removing the upstream fleet of the second fleet.



### Delay the completion of group's version rollout

If you need to temporarily prevent a group from completing the rollout of a new version to its clusters, you can add a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to any of the clusters that have not been upgraded to the target version. This can pause a group from proceeding to its soak time or downstream group for up to 30 days. After 30 days, the group will begin soaking.

You can also change the soak time for that group to 30 days to maximize how long the rollout sequence waits before proceeding to the next group.

If you need to further delay upgrades beginning for the next group, you can use maintenance exclusions for the clusters in the next group.

## Delete a sequence

To delete a sequence, you remove the upstream associations for each of the groups, except for the first group. The first group doesn't have an upstream group.

You can perform these steps in the Google Cloud console (Preview) or with the gcloud CLI.

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Rollout Sequencing** page in the Google Cloud console.

[Go to Rollout Sequencing](https://console.cloud.google.com/kubernetes/upgrades)

  2. View the sequence in the section **Monitor your rollout sequence**. If you don't see a rollout sequence, switch to a different rollout sequence, or create a rollout sequence if you haven't already done so.

  3. In the **Rollout graph** , click the element for the last fleet.

  4. Click delete **Remove fleet**.

  5. To remove the fleet, click **Remove**.

  6. Repeat the previous three steps until only the first fleet remains.

**Success:** After you delete the remaining connection between the fleets, the **Rollout graph** continues to show one fleet without any connections. If this is the state, you've successfully deleted the rollout sequence.



### gcloud

Run the following command in the fleet host project of each of the fleets in the rollout sequence, excluding the first fleet:
    
    
    gcloud container fleet clusterupgrade update --reset-upstream-fleet
    

## Troubleshooting

### Troubleshoot rollout eligibility

If all clusters in a rollout sequence don't have the same upgrade target, GKE might not be able to proceed with cluster upgrades. Automatic upgrades cannot proceed if an upstream group does not qualify one upgrade target to pass to the downstream group. Automatic upgrades also cannot proceed if clusters in the upstream group qualify an invalid upgrade target for clusters in the downstream group.

To check if your rollout sequence has any rollout eligibility issues, check the status of the rollout sequence. If a group is ineligible, follow the instructions to see the status of individual clusters in a group.

To immediately advance cluster upgrades, remove any clusters with an `INELIGIBLE` status following the instructions to Advance partially eligible rollouts.

#### Fix eligibility in a group

In a group, if a cluster is ineligible because it is on an earlier version (for example, most of the clusters in the group are being upgraded from 1.23 to 1.24 and a cluster is on version 1.22), you can manually upgrade the cluster to 1.24 to resolve the version discrepancy.

In a group, GKE ignores clusters on later versions than the auto-upgrade target. These clusters don't prevent upgrades from proceeding to the downstream group.

#### Fix eligibility between groups

Between groups, if there is a mismatch in upgrade targets where the downstream group is on a newer version (for example, the upstream group upgraded from 1.23 to 1.24 and the clusters in the downstream group are on 1.25), you can manually upgrade the clusters in the upstream group to 1.25 to ensure that upgrades proceed.

Between groups, if there is a mismatch in upgrade targets where the downstream group is on an earlier version (for example, the upstream group upgraded from 1.24 to 1.25 and the clusters in the downstream group are on 1.23), you can manually upgrade the clusters in the downstream group to 1.24 or 1.25 to ensure that upgrades proceed. If GKE upgraded the upstream group to any version for which the downstream group is eligible, GKE upgrades the clusters in the downstream group to that upgrade target. In this situation, you don't need to manually upgrade the clusters to unblock the sequence. For more information, see [The upstream group qualified multiple upgrade targets for the downstream group](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing#multiple-versions-qualified).

### Advance partially eligible rollouts

If cluster upgrades in a group won't finish because of issues with [rollout eligibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing#rollout-eligibility) (for example, version discrepancies within a group), you can remove clusters that are ineligible for the group's upgrade target from a group to complete the version rollout and begin the soak time or move on to the next group in the rollout sequence. You can also remove a cluster from a group for other reasons, for example if this cluster's usage is no longer related to the other clusters in the group.

Follow the instructions to [unregister a cluster from a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister#unregister).

After you have removed all clusters which are preventing a group's version rollout from being completed, the group's version rollout will complete. Confirm this by following the instructions to Check the status of a version rollout.

## What's next

  * [About cluster upgrades with rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
