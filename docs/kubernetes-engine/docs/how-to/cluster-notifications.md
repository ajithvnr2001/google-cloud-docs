---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications/
title: Receive cluster notifications through Pub/Sub \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:33.329114+00:00
---

# Receive cluster notifications through Pub/Sub  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Receive cluster notifications through Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to use Pub/Sub to receive notifications about your Google Kubernetes Engine (GKE) clusters.

GKE, by default, routes these notifications to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). You can use all the capabilities of Cloud Logging, including [querying and viewing logs](https://docs.cloud.google.com/logging/docs/log-analytics), and [configuring log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). To find these logs in Cloud Logging, see [Viewing cluster notifications in Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).

## Overview

When certain events occur that are relevant to your GKE clusters, such as important scheduled upgrades or available security bulletins, GKE publishes notifications about those events as messages to Pub/Sub topics that you configure. You can receive these notifications on a Pub/Sub subscription, [integrate with third-party services](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack), and filter for the notification types you want to receive.

To learn more about the benefits of cluster notifications, how notifications work, and why filtering is important, refer to [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications). You can configure cluster notifications in new and existing Standard clusters, and by updating existing Autopilot clusters. You can't use Pub/Sub to receive notifications about [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#creating_a_topic). You can create a topic in your cluster's project, or a different project in your organization.

  * Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).




### Permissions for cross-project cluster notifications

To use a Pub/Sub topic from a different project than your cluster, grant the following roles from your topic project to the `service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com` service account in your cluster project:

  * [Pub/Sub Viewer](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.viewer)
  * [Pub/Sub Publisher](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher)



## Enable cluster notifications on an existing cluster

You can enable GKE cluster notifications on an existing cluster using the Google Cloud CLI or the Google Cloud console.

You can choose to create one topic for all clusters, or create multiple topics for groups of clusters.

### gcloud

To enable cluster notifications on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --notification-config=pubsub=ENABLED,pubsub-topic=projects/TOPIC_PROJECT_ID/topics/TOPIC_NAME,filter=NOTIFICATION_TYPE
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `TOPIC_PROJECT_ID`: the Google Cloud project ID of the project of your Pub/Sub topic. If your topic project is different from your cluster project, ensure that you've granted the required permissions. For more information, see Permissions for cross-project cluster notifications.
  * `TOPIC_NAME`: the name of your Pub/Sub topic.
  * `NOTIFICATION_TYPE`: a pipe (|) delimited list of the notification types you want to receive. For example, `filter="UpgradeEvent|SecurityBulletinEvent"` only sends `UpgradeEvent` and `SecurityBulletinEvent` notifications, ignoring all other types.

**Note:** If you do not specify values for `filter`, you will receive all notifications that are applicable to your cluster configuration.



### Console

To enable cluster notifications on an existing cluster, perform the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. In the **Automation** section, next to **Notifications** , click edit **Edit notifications**.

  4. In the **Edit notifications** dialog, select the **Enable notifications** checkbox.

  5. From the drop-down list, select the Pub/Sub topic you created.

  6. To filter notifications, select the **Filter notification types** checkbox, and then select the notification types you want to receive.

**Note:** If you do not select notification types to filter, you will receive all applicable notifications.
  7. Click **Save changes**.




After enabling notifications, choose the [type of subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) for your topic.

## Filter cluster notifications

You can filter notifications by [notification type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#notification-types) to ensure that you receive notifications that you want.

You can choose to filter notifications using the following methods:

  * **GKE** : Specify values for `filter` in the `--notification-config` flag, as shown in the previous examples for enabling cluster notifications.
  * **Pub/Sub** : Configure your Pub/Sub subscription to [filter messages](https://docs.cloud.google.com/pubsub/docs/filtering) when you create a subscription.

**Note:** We recommend that you filter using GKE. Filtering in GKE lets you modify the filters at any time and eliminates the [undelivered message cost](https://cloud.google.com/pubsub/pricing#filtered_messages) associated with Pub/Sub filters. To learn more about the differences between the filtering options, see [Filtering notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#filtering).

### Modify existing filters in GKE

To modify your existing GKE cluster notification filters, follow the instructions in Enable notifications on an existing cluster and specify the new notification types to filter in the `gcloud` command or select the new types in the Google Cloud console.

### Disable filters in GKE

You can disable your GKE notification filters and receive all notification types applicable to your cluster using the gcloud CLI or the Google Cloud console.

### gcloud

To disable filters using the gcloud CLI, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --notification-config=pubsub=ENABLED,pubsub-topic=projects/TOPIC_PROJECT_ID/topics/TOPIC_NAME
    

### Console

To disable filters using the Google Cloud console, perform the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. In the **Automation** section, next to **Notifications** , click edit **Edit notifications**.

  4. In the **Edit notifications** dialog, clear the **Filter notification types** checkbox.

  5. Click **Save changes**.




## Verify setup for cluster notifications

On Autopilot mode, you can verify cluster notifications as follows:

  1. [Start a control plane upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp).
  2. Wait for GKE to automatically upgrade your nodes to the new version. The time taken might vary based on configured maintenance windows and exclusions.
  3. After GKE upgrades your nodes, [check your Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/pull).



On Standard mode, you can verify cluster notifications as follows:

  1. [Upgrade a specific node pool to a new version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes). If you don't want to change the GKE version on your nodes, you can upgrade to the same version currently on the nodes.

**Caution:** Manually upgrading a Standard node pool ignores your configured [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) and might cause disruptions to running workloads.
  2. After GKE upgrades your nodes, [check your Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/pull).




You can only manually verify setup for the `UpgradeEvent` notification type. If your filters are configured to ignore this type, you won't see a message.

## Disable cluster notifications

You can disable cluster notifications using the gcloud CLI or the Google Cloud console.

### gcloud

To disable notifications using the gcloud CLI, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --notification-config=pubsub=DISABLED
    

### Console

To disable notifications using the Google Cloud console, perform the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. In the **Automation** section, next to **Notifications** , click edit **Edit notifications**.

  4. In the **Edit notifications** dialog, clear the **Enable notifications** checkbox.

  5. Click **Save changes**.




Optionally, [delete the Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#deleting_a_topic) you created for notifications.

## What's next

  * Learn more about [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).
  * Learn about [configuring Pub/Sub notifications](https://docs.cloud.google.com/pubsub/docs/filtering).
  * Learn how to [configure cluster notifications for third-party services](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack).
  * Learn how to [configure clusters to receive notifications via email](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-email).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
