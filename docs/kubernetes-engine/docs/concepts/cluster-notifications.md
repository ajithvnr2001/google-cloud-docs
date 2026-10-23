---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications/
title: Cluster notifications \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:49.601464+00:00
---

# Cluster notifications  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Cluster notifications Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how Google Kubernetes Engine (GKE) publishes cluster notifications to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) by default (and optionally to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview)) when specific events occur in your GKE clusters. These notifications have information about events relevant to your cluster configuration, such as scheduled, available, or ongoing upgrades, security bulletins, and end of support dates. To find these logs in Cloud Logging, see Viewing cluster notifications in Cloud Logging.

GKE also publishes notifications about those events as messages to Pub/Sub topics that you configure. You can receive these notifications on a Pub/Sub subscription, [integrate with third-party services](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack), and filter for the notification types you want to receive. For more information about how to set up cluster notifications with Pub/Sub, see [Receive cluster notifications through Pub/Sub](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).

In addition to cluster notifications, GKE also provides notifications for [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing) exclusively to Cloud Logging.

## Benefits

Cluster notifications provide the following benefits:

  * You are notified when [security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins) that are specific to your clusters are issued, which provides you with accurate risk and impact information.
  * You are notified when there is a new GKE version available for your cluster, allowing you to better plan for testing and qualifications, and to help ensure a smooth and predictable upgrade process. Previously, you had to check the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) or the [GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ServerConfig) to discover when a new GKE version was released.
  * You are notified when either GKE or a user initiates [cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades), and when the upgrade operation finishes, providing you with more visibility into the background operations of your cluster.
  * You are notified when your cluster is running a GKE minor version that is at or near the end of support.
  * You can choose whether to use Cloud Logging or Pub/Sub:

    * Cluster notifications are sent to Cloud Logging by default. You can use all the capabilities of Cloud Logging, including [querying and viewing logs](https://docs.cloud.google.com/logging/docs/log-analytics), and [configuring log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).
    * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) is highly extensible, giving you flexibility in how you process incoming notifications. For example, you could integrate with [Slack](https://slack.com) to forward notifications to a Slack channel, or initiate [Cloud Run functions](https://docs.cloud.google.com/functions) to run custom processes. When custom processes are required (for example, orchestrating a staging to production workflow to test and certify an upgrade), you can use the notification to auto-trigger these workflows.



Rollout sequencing notifications notify you about the following:

  * The progression of a rollout in a rollout sequence with custom stages. The notifications keeps you informed regarding the status of a rollout, so that you can monitor the performance of your clusters and workloads, and take action, if necessary.
  * If a rollout sequence with custom stages is misconfigured, meaning that you need to fix it.



## Types of upgrade notifications

GKE sends the following cluster notification types:

  * `SecurityBulletinEvent`
  * `UpgradeAvailableEvent`
  * `UpgradeEvent`
  * `UpgradeInfoEvent`, which includes the following types of events:

    * Scheduled cluster upgrades ([Preview](https://cloud.google.com/products#product-launch-stages))
    * Upgrade operation is complete
    * Minor version at or near the end of support
    * New patch versions change to new Container-Optimized OS milestone during extended support
    * Disruptive events during a node pool upgrade



If you view cluster notifications in Cloud Logging, you can use the capabilities of Cloud Logging to filter the logs. If you use Pub/Sub, you can filter the notifications you receive so that you're notified only for relevant events.

GKE sends the following rollout sequence notification types for rollout sequencing with custom stages:

  * `RolloutEvent`
  * `RolloutSequenceEvent`



### SecurityBulletinEvent

When GKE issues a security bulletin that directly correlates to your cluster configuration or version, GKE sends a [`SecurityBulletinEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/SecurityBulletinEvent) notification, providing you with information about the vulnerability, the impact, and, if applicable, actions you can take.

**Key Point:** GKE does not send a notification if your cluster is not affected by the vulnerability. Also, GKE waits to send a bulletin notification until a patch has rolled out in your cluster region or zone so that you can act when you receive the notification. You might receive two notifications for the same bulletin if the vulnerability affects both the control plane and nodes.

### UpgradeAvailableEvent

When a new version becomes available on a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), GKE sends an [`UpgradeAvailableEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeAvailableEvent) notification to clusters on that release channel to inform the clusters that a new version is now available. This notification provides one week of advance notice for patch versions and at least 2-4 weeks for minor versions (depending on the channel). For more information, refer to [What versions are available in a channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel).

**Note:** GKE does not send a notification when the default version changes in a release channel.

For clusters not on a release channel, GKE sends `UpgradeAvailableEvent` notifications for all new versions that the clusters can upgrade to, including patches on the current minor version and the next minor version.

**Note:** Clusters and node pools that aren't on a release channel and have [auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) enabled might upgrade shortly after receiving an `UpgradeAvailableEvent` notification, because there is no guarantee of advance notice for clusters outside release channels.

If you use Windows Server node pools, Windows version information is sent as part of the `UpgradeAvailableEvent` notification.

**Note:** Windows Server version information being included in `UpgradeAvailableEvent` notifications is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### UpgradeEvent

When you or GKE initiates an upgrade, GKE sends an [`UpgradeEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeEvent) notification, telling you that an upgrade has begun. Ideally, you should use the `UpgradeAvailableEvent` notification type to be aware of the upcoming upgrade so that you can either upgrade in advance or take necessary measures to prepare, such as setting up [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions).

The `UpgradeEvent` notification is sent at the start of the upgrade operation. The operation ID is passed in the message.

For [two-step control plane minor upgrades with rollback safety](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#two-step-cp-upgrade), GKE sends this notification when the _binary upgrade_ starts, and when the _emulated version upgrade_ starts. For more information about what key details GKE provides, see What's included in the notification for two-step upgrades.

### UpgradeInfoEvent

GKE sends an [`UpgradeInfoEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeInfoEvent) notification for different types of events, which are outlined in the next sections.

For more information about filtering for a specific type of `UpgradeInfoEvent`, see Filter `UpgradeInfoEvent` cluster notifications.

#### Scheduled cluster upgrades

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When GKE schedules a cluster upgrade, GKE sends you a notification between 72 hours and 96 hours in advance. For more information about how to enable scheduled cluster upgrades, see [Get notified about scheduled cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-notified-scheduled-upgrades).

#### Upgrade operation is complete

When GKE finishes the operation to automatically or manually upgrade a cluster's control plane or nodes, GKE sends a notification to inform you that the operation is complete. The operation completes with one of the following states:

  * `SUCCEEDED`: GKE successfully upgraded the control plane or nodes.
  * `FAILED`: GKE failed to upgrade the control plane or nodes.
  * `CANCELED`: GKE canceled the upgrade operation for technical or business reasons, or you [canceled the upgrade operation](https://docs.cloud.google.com/sdk/gcloud/reference/container/operations/cancel).



Use the notification to confirm the success of an upgrade operation.

##### What's included in the notification for two-step upgrades

For [two-step control plane minor upgrades with rollback safety](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#two-step-cp-upgrade), GKE sends this notification once after the _binary upgrade_ completes, which is when the soak time starts, and again, after the _emulated version upgrade_ completes. These notifications include information such as the following, where applicable based on the status of the two-step upgrade:

  * The initial version
  * The target version
  * The initial emulated version
  * The target emulated version



#### Minor version at or near the end of support

When your cluster runs a GKE minor version that is near the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support) or [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support), or has reached either of those milestones, GKE sends notifications that you must upgrade your cluster control plane or nodes to the next supported minor version. Running a supported minor version ensures that you continue receiving security patches, bug fixes, and support. GKE sends one notification 30 days before the end of support, and one notification at the end of support, if your cluster still runs the minor version.

GKE sends cluster-level notifications, although multiple components of your cluster might be affected, and your cluster can run different minor versions at the same time. If the minor version is reaching the end of standard support and you need time to prepare for an upgrade to a supported version, you can [switch to the Extended release channel to get long-term support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended). Otherwise, GKE schedules [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support). These notifications help ensure that you're prepared for the enforcement of these end of support policies.

A notification includes the following details:

  * The cluster that is affected.
  * The current version that is at or near the end of support.
  * The end of support date.



For more details about the timeline of support for GKE minor versions, see the [GKE minor version lifecycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle).

#### New patch versions change to new Container-Optimized OS milestone during extended support

When your cluster is enrolled in the Extended channel during the extended support period, and the Container-Optimized OS milestone that's used by the GKE minor version reaches the end of support before the minor version, GKE sends out a cluster notification. GKE sends this notification when the first patch version to use the new milestone becomes available in the Extended channel.

This notification includes the following details:

  * The cluster that is affected.
  * The patch version which uses the new milestone.
  * The existing and new milestones.
  * How GKE pauses automatic patch upgrades for the nodes.



The patch version which uses the new milestone eventually becomes the patch auto-upgrade target for the cluster, and node auto-upgrades are paused. Cluster administrators must decide which of the following next steps to take:

  * Manually upgrade the cluster nodes to the next patch version which uses the next Container-Optimized OS milestone.
  * Manually upgrade the cluster to the next minor version.
  * Forgo patch upgrades until GKE upgrades the cluster to the next minor version towards the end of extended support.



To learn more, see [The Container-Optimized OS milestone reaches the end of support before the minor version end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#eos-before-minor-version).

#### Disruptive events during a node pool upgrade

When a node pool experiences certain types of disruptive events during a node pool upgrade, GKE sends a notification to inform you about this event.

GKE sends out a cluster notification for the following types of disruptive events:

  * The node drain is blocked by the [Pod Disruption Budget (PDB)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).
  * The PDB timeout is reached and the Pods will be force deleted despite the PDB violation.



This notification includes the following details:

  * The node that is affected by this disruption event.
  * The Pods that are affected by this disruption event.
  * The operation that triggered the node drain.
  * The PDB timeout before the Pods were force deleted.



### RolloutEvent

GKE sends notifications when the following events occur for the rollout of a GKE version in a rollout sequence with custom stages:

  * `ROLLOUT_CREATED`: a new rollout has been created.
  * `ROLLOUT_STAGE_TRANSITION`: a stage in the rollout has transitioned to a new state.
  * `ROLLOUT_BLOCKED`: the rollout is blocked because a control plane or node pool is ineligible for upgrade.
  * `ROLLOUT_AUTO_PAUSED`: the rollout has been automatically paused by GKE.
  * `ROLLOUT_AUTO_RESUMED`: the rollout has been automatically resumed after being paused.
  * `ROLLOUT_CANCELLATION_WARNING`: the rollout has been paused for too long and will be canceled automatically in seven days if it is not resumed.
  * `ROLLOUT_AUTO_CANCELLED`: the rollout has been automatically cancelled by GKE.
  * `ROLLOUT_COMPLETED`: the rollout has completed successfully.



### RolloutSequenceEvent

GKE sends notifications for the following situations for a rollout sequence with custom stages:

  * `SEQUENCE_MISCONFIGURED`: the rollout sequence is misconfigured, meaning that GKE can't perform upgrades in the sequence with its current configuration.
  * `SEQUENCE_DEACTIVATION_WARNING`: a warning that GKE will deactivate the rollout sequence if the misconfiguration isn't fixed.



## Viewing cluster notifications in Cloud Logging

The following instructions work for both cluster notifications and rollout sequencing notifications.

To view logs for GKE clusters, see [Accessing your logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#accessing_your_logs).

To opt out of storing these logs, you can configure an [exclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

View logs in Cloud Logging with the following filter to see all types of cluster notifications:
    
    
    logName=projects/PROJECT_ID/logs/container.googleapis.com%2Fnotifications
    

Replace `PROJECT_ID` with your Google Cloud project ID.

View logs with the following filter to see a specific cluster notification type, such as `UpgradeEvent`:
    
    
    jsonPayload.@type=type.googleapis.com/google.container.v1beta1.NOTIFICATION_TYPE
    

Replace `NOTIFICATION_TYPE` with the cluster notification type for whichever logs you want to see.

### Filter `UpgradeInfoEvent` cluster notifications

View logs with the following filter to see a specific `UpgradeInfoEvent`, such as the notification for where an upgrade operation is complete:
    
    
    jsonPayload.@type=type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent
    jsonPayload.eventType=EVENT_TYPE
    

Replace `EVENT_TYPE` with one of the following:

  * **Upgrade operation is complete**: `UPGRADE_LIFECYCLE`
  * **Minor version at or near the end of support**: `END_OF_SUPPORT`
  * **New patch versions change to new Container-Optimized OS milestone during extended support**: `COS_MILESTONE_VERSION_UPDATE`
  * **Disruptive events during a node pool upgrade**: `DISRUPTION_EVENT`
  * **Scheduled cluster upgrades**: `UPGRADE_LIFECYCLE`



## Filtering notifications to Pub/Sub

You can filter cluster notifications to ensure that you receive only the notifications that you want in Pub/Sub. You can apply filtering for notifications to Pub/Sub in one of the following ways:

  * Filtering notifications in GKE.
  * Filtering notifications in Pub/Sub.



To view and filter notifications in Cloud Logging, see Viewing cluster notifications in Cloud Logging.

**Note:** Filtering notifications in GKE is strongly recommended over filtering in Pub/Sub because of the ease-of-use and because you are billed only for the notifications you receive.

### Filtering notifications to Pub/Sub in GKE

You can set up filtering to Pub/Sub for one or more available notification types when enabling cluster notifications by specifying values for `filter` in the `--notification-config` flag. `filter` takes a pipe ( | ) delimited list of the notification types you want to receive.

For example, specifying `filter="UpgradeEvent|SecurityBulletinEvent"` tells GKE to only send notifications for `UpgradeEvent` and `SecurityBulletinEvent` notification types.

Filtering notifications using `filter` has benefits such as the following:

  * Easier to use, because you filter on the notification type without using a specific syntax.
  * Notifications you filter out are never sent to Pub/Sub, so you aren't charged fees for undelivered messages.
  * You can edit the filter configuration at any time.



For instructions on filtering notifications in GKE, see [Receive cluster notifications through Pub/Sub](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications#filter-notifications).

Filtering notifications in GKE doesn't affect which logs appear in Cloud Logging.

### Filtering notifications in Pub/Sub

Pub/Sub supports filtering messages in your subscription using a filtering syntax. When you use this method, GKE delivers all notification types to your Pub/Sub topic. Pub/Sub filters messages based on your subscription configuration and delivers the messages you want to receive.

For example, you could filter for `UpgradeEvent` and `UpgradeAvailableEvent` notifications using the following syntax in your subscription:
    
    
    attributes.type_url = "type.googleapis.com/google.container.v1beta1.UpgradeEvent" OR "type.googleapis.com/google.container.v1beta1.UpgradeAvailableEvent"
    

You are still [charged for undelivered messages](https://cloud.google.com/pubsub/pricing#filtered_messages) filtered by your subscription. You also **cannot** modify the filters after you've configured the subscription. However, the filtering syntax is more extensible than filtering in GKE.

To learn more about filtering your Pub/Sub subscription, see [Filtering messages](https://docs.cloud.google.com/pubsub/docs/filtering).

## Alerting on cluster notifications in Cloud Logging

You can configure log-based alerts to receive notifications when specific cluster events occur. The following section provides a basic example of setting up a log-based alert, but you can find other examples in the [monitoring dashboard samples repository](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/alerts/google-gke).

### Create a log-based alert

To create an alert for a specific notification type, complete the following steps. The following steps use `UpgradeEvent` as an example.

  1. In the Google Cloud console, go to the [Logs Explorer](https://console.cloud.google.com/logs/query).

  2. In the **Query** field, enter the following query to filter for your chosen notification type:
         
         resource.type="RESOURCE_TYPE"
         log_id("container.googleapis.com/notifications")
         jsonPayload.@type="type.googleapis.com/google.container.v1beta1.NOTIFICATION_TYPE"
         

Replace the following:

     * `RESOURCE_TYPE`: the resource type that you want to filter on, for example `gke_cluster` OR `gke_nodepool`, or a combination.
     * `NOTIFICATION_TYPE`: The cluster notification type that you want to alert on, such as `UpgradeEvent`.

Some notification types require additional filtering. For example, if you want to filter for a specific type of `UpgradeInfoEvent`, add the `jsonPayload.eventType` filter to your query. The following example query filters for `UpgradeInfoEvent` where the event type is `UPGRADE_LIFECYCLE`:
    
    resource.type="RESOURCE_TYPE"
    log_id("container.googleapis.com/notifications")
    jsonPayload.@type="type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent"
    jsonPayload.eventType="UPGRADE_LIFECYCLE"
    

For more information on filtering `UpgradeInfoEvent`, see Filter `UpgradeInfoEvent` cluster notifications.

  3. Under the **Actions** menu, click **Create log alert**.

  4. On the **Alert details** page, provide a name for your alert policy and then click **Next**.

In the **Define log entries to alert on** section, your query is pre-populated.

  5. In the **Extract log labels** section, click **Add a label**. Extracting log labels helps make your notifications more informative. For example, for an `UpgradeEvent`, you can include the current and target versions of an upgrade by adding the following labels:

     * **CurrentVersion** : `jsonPayload.currentVersion`
     * **TargetVersion** : `jsonPayload.targetVersion`
  6. Click **Next**.

  7. Configure the notification frequency and autoclose duration, and then click **Next**.

  8. In the **Who should be notified?** section, select the [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) where you want to receive the alerts and then click **Save**.




After you configure the alert, notifications for an `UpgradeEvent` include the `CurrentVersion` and `TargetVersion` labels, providing valuable context directly in the notification.

## Consuming Pub/Sub messages

Pub/Sub messages contain two fields: `data` (string) and `attributes` (string-to-string map).

For GKE notifications, the `data` field contains human-readable information. The `attributes` field has generic notification information like the notification type, your project ID, cluster name, and cluster location. The `attributes.payload` field is a JSON-parsable string that contains specific notification information, such as the details of a security bulletin.

Notifications always contain the following attributes:

Attribute | Description | Example  
---|---|---  
`project_id` | The project number that owns the cluster. | `123456789`  
`cluster_location` | The location of the cluster. | `us-central1-c`  
`cluster_name` | The name of the cluster. | `example-cluster`  
`type_url` | The type of notification. | `type.googleapis.com/google.container.v1beta1.UpgradeEvent`  
`payload` | A JSON-parsable string carrying notification-specific information.  | 
    
    
    { "resourceType":"MASTER",
      "operation":"operation-1595889094437-87b7254a",
      "operationStartTime":"2020-07-27T22:31:34.437652293Z",
      "currentVersion":"1.15.12-gke.2",
      "targetVersion":"1.15.12-gke.9"}  
  
GKE will always send `beta` notification types. However, you can parse the payload to display the corresponding GA notification type if it is available.

### Sample cluster notification messages

In addition to the text in the `data` field, each message that GKE sends to Cloud Logging or Pub/Sub has specific values in the `attributes.type_url` and `attributes.payload` fields. The following tables show you examples of the information you might receive for each notification type:

#### SecurityBulletinEvent

The output is similar to the following for a [`SecurityBulletinEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/SecurityBulletinEvent) message:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.SecurityBulletinEvent`  
`payload` | 
    
    
    {    "resourceTypeAffected":"RESOURCE_TYPE_CONTROLPLANE",
             "bulletinId":"GCP-2021-001",
             "cveIds":[
                "CVE-2021-3156"
             ],
             "severity":"Medium",
             "briefDescription":"A vulnerability was recently discovered in the Linux utility sudo, described in CVE-2021-3156, that may allow an attacker with unprivileged local shell access on a system with sudo installed to escalate their privileges to root on the system.",
             "affectedSupportedMinors":["1.18", "1.19"],
             "patchedVersions":["1.18.9-gke.1900", "1.19.9-gke.1900"],
             "suggestedUpgradeTarget":"1.19.9-gke.1900",
             "bulletinUri":"https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2021-001"
          }
            
  
#### UpgradeAvailableEvent

The output is similar to the following for an [`UpgradeAvailableEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeAvailableEvent) message:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.UpgradeAvailableEvent`  
`payload` | 
    
    
    { "version":"1.17.15-gke.800",
      "resourceType":"MASTER",
      "releaseChannel":{"channel":"RAPID"},
      "windowsVersions": [
        {
          "imageType": "WINDOWS_SAC",
          "osVersion": "10.0.18363.1198",
          "supportEndDate": {
            "day": 10,
            "month": 5,
            "year": 2022
          }
        },
        {
          "imageType": "WINDOWS_LTSC",
          "osVersion": "10.0.17763.1577",
          "supportEndDate": {
            "day": 9,
            "month": 1,
            "year": 2024
          }
        }
      ]
    }
    
            
  
#### UpgradeEvent

The output is similar to the following for an [`UpgradeEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeEvent) message:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.UpgradeEvent`  
`payload` | 
    
    
    { "resourceType":"MASTER",
      "operation":"operation-1595889094437-87b7254a",
      "operationStartTime":"2020-07-27T22:31:34.437652293Z",
      "currentVersion":"1.15.12-gke.2",
      "targetVersion":"1.15.12-gke.9"}
            
  
This output represents a notification for a one-step control plane upgrade. Two-step upgrades include different information in the notification. For more information about the different types of control plane upgrades, see [Upgrading the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster).

#### UpgradeInfoEvent

The output is similar to the following for an [`UpgradeInfoEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeInfoEvent) message for when an upgrade operation completes, such as this example for a node pool upgrade:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent`  
`payload` | 
    
    
    { "currentVersion":"1.31.1-gke.1846000",
      "endTime":"2024-11-06T17:12:54.111640650Z",
      "operation":"operation-1730912205658-de2f88a8-6290-4718-b2c1-fb19611060b8",
      "resource":"projects/PROJECT_ID/locations/CLUSTER_LOCATION/clusters/CLUSTER_NAME/nodePools/NODE_POOL_NAME",
      "resourceType":"NODE_POOL"
      "startTime":"2024-11-06T16:56:45.658321844Z",
      "state":"**SUCCEEDED** ",
      "targetVersion":"1.31.1-gke.2105000"}
            
  
This output is distinct from notifications for control plane upgrades, when the messages are for a minor version at or near the end of support, when new patch versions change to new Container-Optimized OS milestone during extended support, or for disruptive events during a node pool upgrade.

##### Scheduled cluster upgrade notification

When a cluster upgrade is scheduled and scheduled upgrade notifications are enabled, GKE sends an output [`UpgradeInfoEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeInfoEvent) message similar to the following for a scheduled control plane upgrade:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent`  
`payload` | 
    
    
    {
      "insertId": "[...]",
      "jsonPayload": {
        "description": "Your cluster control plane will be upgraded to 1.32.9-gke.1239000 after 2025-12-13 12:46 UTC",
        "startTime": "2025-12-13T12:46:37.380970854Z",
        "targetVersion": "1.32.9-gke.1239000",
        "@type": "type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent",
        "currentVersion": "1.31.14-gke.1081000",
        "eventType": "UPGRADE_LIFECYCLE",
        "state": "SCHEDULED",
        "resourceType": "MASTER"
      },
      "resource": {
        "type": "gke_cluster",
        "labels": {
          "cluster_name": "CLUSTER_NAME",
          "location": "LOCATION",
          "project_id": "PROJECT_ID"
        }
      },
      "timestamp": "2025-12-10T12:46:37.989407414Z",
      "severity": "NOTICE",
      "logName": "projects/PROJECT_ID/logs/container.googleapis.com%2Fnotifications",
      "receiveTimestamp": "2025-12-10T12:46:38.007312354Z"
    }
            
  
GKE sends an output message similar to the following for scheduled node upgrades:

Attributes  
---  
`type_url` | `type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent`  
`payload` | 
    
    
    {
      "insertId": "[...]",
      "jsonPayload": {
        "description": "Your cluster node pools will be upgraded to 1.32.9-gke.1239000 (or latest target patch) after 2025-12-13 12:46 UTC: NODE_POOL_1, NODE_POOL_2, [...] and 23 more.",
        "startTime": "2025-12-13T12:46:37.380970854Z",
        "targetVersion": "1.32.9-gke.1239000",
        "@type": "type.googleapis.com/google.container.v1beta1.UpgradeInfoEvent",
        "currentVersion": "1.31.14-gke.1081000",
        "eventType": "UPGRADE_LIFECYCLE",
        "state": "SCHEDULED",
        "resource": "projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/nodePools/NODE_POOL_1",
        "resourceType": "NODE_POOL"
      },
      "resource": {
        "type": "gke_nodepool",
        "labels": {
          "cluster_name": "CLUSTER_NAME",
          "location": "LOCATION",
          "nodepool_name": "NODE_POOL_NAME",
          "project_id": "PROJECT_ID"
        }
      },
      "timestamp": "2025-12-10T12:46:37.989407414Z",
      "severity": "NOTICE",
      "logName": "projects/PROJECT_ID/logs/container.googleapis.com%2Fnotifications",
      "receiveTimestamp": "2025-12-10T12:46:38.007312354Z"
    }
            
  
For scheduled node upgrades, which are grouped by auto-upgrade target, GKE alphabetically lists up to 10 node pools—providing detailed information only for the first node pool. If more than 10 node pools are scheduled, GKE displays a count of the remaining unlisted pools (such as 33 total upgrades in this example).

## What's next

  * Learn how to [receive cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).
  * Learn how to [send cluster notifications to Slack](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack).
  * Learn about [cluster upgrades for GKE Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * Read the overview on [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
