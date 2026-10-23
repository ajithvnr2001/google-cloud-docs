---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters/
title: Manage clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:40.018945+00:00
---

# Manage clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manage clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to manage your clusters in Google Kubernetes Engine (GKE). To learn about how clusters work, refer to [Cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## View your clusters

### gcloud

  * To view a specific cluster, run the following command:
        
        gcloud container clusters describe CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * To list all clusters in a project in any region or zone, run the following command:
        
        gcloud container clusters list
        

  * To list clusters located in the specific region or zone, run the following command:
        
        gcloud container clusters list \
            --location=CONTROL_PLANE_LOCATION
        




### Console

To view your clusters, go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

To see more information about a cluster, select the cluster from the list.

## Set a default cluster for `kubectl`

If you have multiple clusters, you can set a default cluster for the `kubectl` command-line tool.

To learn more, refer to [Setting a default cluster for `kubectl` commands](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#default_cluster_kubectl).

## Set a default cluster for `gcloud`

To set a default cluster for `gcloud` commands, run the following command:
    
    
    gcloud config set container/cluster CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your cluster.

## Upgrade clusters

By default, GKE automatically upgrades your clusters. However, you can choose to upgrade your Standard clusters yourself. To learn more, see [Manually upgrading a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

For guidance on upgrading clusters, see [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).

## Add or remove zones in a Standard cluster

The following sections explain how to add or remove cluster zones. All zones must be in the cluster's region.

**Warning:** If you change the cluster zones, nodes are immediately added or removed. Before you remove a zone, ensure that your workloads in that zone are prepared for disruption.

### Change zones for zonal clusters

For existing zonal clusters, you can add or remove zones.

### gcloud

To add or remove zones for a zonal cluster, use the `gcloud container clusters update` command:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location CONTROL_PLANE_LOCATION \
      --node-locations COMPUTE_ZONE1,COMPUTE_ZONE2
    

Replace the following:

  * `CLUSTER_NAME`: the name you choose for the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  * `COMPUTE_ZONE1,COMPUTE_ZONE2,[...]`: the zones in which nodes are created. You can specify as many zones as needed for your cluster. All zones must be in the same region as the cluster's control plane, specified by the `--location` flag. For zonal clusters, `--node-locations` must contain the cluster's primary zone.

**Note:** In `--node-locations`, do not put spaces between the zone names.

For example, `example-cluster` runs in `us-central1-a`. To add two more zones to the cluster, you'd run the following command:
    
    
    gcloud container clusters update example-cluster \
      --location us-central1-a
      --node-locations us-central1-a,us-central1-b,us-central1-c
    

As another example, `example-cluster` runs in `us-central1-a`, `us-central1-b` and `us-central1-c`. If you only want the cluster to run in `us-central1-a` and `us-central1-b`, you'd run the following command:
    
    
    gcloud container clusters update example-cluster \
      --location us-central1-a \
      --node-locations us-central1-a,us-central1-b
    

### Console

To add or remove zones in an existing cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Beside the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. Under the Details tab, for the **Default node zones** field, click _edit_ **Edit node pools**.

  4. Select the desired zones and save your changes.




### Change zones for regional clusters

Currently, it is only possible to change the zones for existing regional clusters using the `gcloud` command.

To add or remove zones for a regional cluster, use the `gcloud container clusters update` command with the `--node-locations` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location CONTROL_PLANE_LOCATION \
      --node-locations COMPUTE_ZONE1,COMPUTE_ZONE2
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  * `COMPUTE_ZONE1`,`COMPUTE_ZONE2,[...]`: the [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) control plane region in which the nodes are created. The zones must be in the same `CONTROL_PLANE_LOCATION` as the cluster's control plane(s), specified by the `--location` flag.

**Note:** In `--node-locations`, do not put spaces between the zones.

For example, `example-cluster` runs in `us-central1-a` and `us-central1-b`. To add `us-central1-c`, you'd run the following command:
    
    
    gcloud container clusters update example-cluster \
      --location us-central1 \
      --node-locations us-central1-a,us-central1-b,us-central1-c
    

As another example, `example-cluster` runs in `us-central1-a`, `us-central1-b` and `us-central1-c`. If you only want the cluster to run in `us-central1-a` and `us-central1-b`, you'd run the following command:
    
    
    gcloud container clusters update example-cluster \
      --location us-central1 \
      --node-locations us-central1-a,us-central1-b
    

## Resize clusters

You can resize a Standard cluster to increase or decrease the number of nodes it has. For example, if you want to stop your cluster from consuming resources without deleting it, you can scale the nodes down to zero. To learn more about resizing, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).

Autopilot clusters are sized automatically based on your Pod specifications, so resizing your cluster isn't something you need to worry about. For example, if you change the number of replicas of your Pod, or the resources it requests, the cluster will be sized up or down appropriately.

If you would like a more efficient way to optimize your clusters, you can also use [Vertical Pod Autoscaling (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler). The autoscaler can recommend values for CPU and memory requests and limits, or it can automatically update the values.

## Delete clusters

When needed, you can delete a cluster. To learn more, see [Deleting a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).

### Prevent cluster deletion by using deny policies

You can use [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to prevent the deletion of certain critical clusters, regardless of which principal attempts the deletion. To target specific clusters in a deny policy, you add a [tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) to those clusters. Then, you use a [denial condition](https://docs.cloud.google.com/iam/docs/deny-overview#denial-conditions) to apply the deny policy only to clusters that have that tag.

To protect a specific cluster from deletion, follow these steps:

  1. [Create and define a tag key](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) to identify protected clusters. For example, you can create a tag key that's named `do_not_delete`.

  2. [Attach the tag key to your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags#attach-tag-cluster).

  3. Create an IAM deny policy by selecting one of the following options:

###  Console 

     1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM Deny](https://console.cloud.google.com/iam-admin/iam/deny)

     2. Click add_box **Create deny policy**. The **Create deny policy** page opens.

     3. In the **ID** field, specify a unique, immutable ID for your deny policy.

     4. In the **New deny rule** section, do the following:

        1. In the **Denied principals** field, specify `principalSet://goog/public:all`, which covers any principal.

        2. In the **Denied permissions** section, in the **Permission 1** drop-down list, find and select the `container.googleapis.com/clusters.delete` permission.

        3. Click add **Add denial condition**. The **Add denial condition** pane opens.

        4. Specify an informative title for the condition, such as `Cluster has the do_not_delete tag`.

        5. In the **Condition builder** tab, from the **Condition type 1** drop-down list, select **Tag**.

        6. In the **Operator** drop-down list, select **Has key**.

        7. In the **Key path** drop-down list, select the tag key that you applied to the cluster, such as `do_not_delete`.

        8. Click **Save**.

     5. Click **Create**.

###  gcloud 

     1. Create a JSON file that contains the following deny policy:
            
            {
              "displayName": "Prevent cluster deletion based on tag",
              "rules": [
                {
                  "description": "Prevent cluster deletion based on tag",
                  "deniedPrincipals": [
                    "principalSet://goog/public:all"
                  ],
                  "deniedPermissions": [
                    "container.googleapis.com/clusters.delete"
                  ],
                  "denialCondition": {
                    "title": "Cluster has the do_not_delete tag",
                    "expression": "resource.hasTagKey('TAG_KEY_NAME')"
                  }
                }
              ]
            }
            

Replace `TAG_KEY_NAME` with the path to the tag key that you created.

     2. Create the deny policy by using the [`gcloud iam policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/create) command:
            
            gcloud iam policies create POLICY_ID \
                --attachment-point=ATTACHMENT_POINT \
                --kind=denypolicies --policy-file=POLICY_FILE
            

Replace the following:

        * `POLICY_ID`: an ID for your deny policy.
        * `ATTACHMENT_POINT`: the organization, folder, or project to attach the deny policy to. For example, if you attach the deny policy to a folder, the policy applies to clusters in any project in that folder. For more information, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).
        * `POLICY_FILE`: the path to the JSON file that you created in the preceding step.




After you create the deny policy, no one can delete a cluster that has the tag key that's specified in the denial condition. Any attempt to delete the cluster fails with a `Permission denied` error message. To allow cluster deletion, you must [detach that tag key from the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags#detach-tag-cluster).

## Add clusters to a fleet

If your organization uses multiple clusters, you can simplify multi-cluster management by adding the clusters to a _fleet_ : a logical grouping of Kubernetes clusters. Creating a fleet helps your organization uplevel management from individual clusters to entire groups of clusters, and lets you use fleet-enabled features such as [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), [ Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview), and [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).

You can add GKE clusters to a fleet by using the Google Cloud console, gcloud CLI, or declaratively using Terraform or Config Connector.

You can learn more about how fleets work in [Fleet management](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview), and about creating fleets in [Create fleets to simplify multi-cluster management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-fleets).

## What's next

  * [Learn about how clusters work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).
  * [Learn about adding and managing your clusters' node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).
  * [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
