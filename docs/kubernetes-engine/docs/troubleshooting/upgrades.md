---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades/
title: Troubleshoot cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:42:58.078026+00:00
---

# Troubleshoot cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If your Google Kubernetes Engine (GKE) control plane or node pool upgrade fails, gets stuck, or causes unexpected workload behavior, you might need to troubleshoot the process. Keeping your control plane and node pools up-to-date is essential for security and performance, and resolving any issues helps ensure that your environment remains stable.

To resolve common upgrade issues, a good first step is to monitor the cluster upgrade process. You can then find advice on resolving your issue:

  * Node pool upgrades taking longer than usual.
  * Incomplete node pool upgrades.
  * Unexpected auto-upgrade behavior.
  * Failed upgrades with specific error messages.
  * Issues after a completed upgrade.
  * Version compatibility issues.



This information is important for Platform admins and operators who want to diagnose the root causes of stuck or failed upgrades, manage maintenance policies, and resolve version incompatibilities. Application developers can find guidance on resolving post-upgrade workload issues and understand how workload configurations, such as `PodDisruptionBudgets`, can affect upgrade duration. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Monitor the cluster upgrade process

To resolve upgrade issues more effectively, start by understanding what happened during the upgrade process. GKE provides several tools that give you visibility into this process.

In the Google Cloud console, the upgrade dashboard offers a project-wide view of all ongoing cluster upgrades, a timeline of recent events, and warnings about potential blockers like active maintenance exclusions or upcoming version deprecations. For command-line or automated checks, you can use the `gcloud container operations list` command to get the status of specific upgrade operations. For more information, see [Get visibility into cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist).

For a more detailed investigation, Cloud Logging is your primary source of information. GKE records detailed information about control plane and node pool upgrade processes within Cloud Logging. This includes high-level audit logs that track the main upgrade operations, as well as more granular logs such as Kubernetes Events and logs from node components, which can show you more information about specific errors.

The following sections explain how to query these logs by using either Logs Explorer or the gcloud CLI. For more information, see [Check upgrade logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#check-update-log).

### Identify the upgrade operation with audit logs

If you don't know which upgrade operation failed, you can use GKE audit logs. Audit logs track administrative actions and provide an authoritative record of when an upgrade was initiated and its final status. Use the following queries in the Logs Explorer to find the relevant operation.

Event type | Log query  
---|---  
Control plane auto-upgrade | 
    
    
    resource.type="gke_cluster"
    protoPayload.methodName="google.container.internal.ClusterManagerInternal.UpdateClusterInternal"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.metadata.operationType="UPGRADE_MASTER"
    resource.labels.cluster_name="CLUSTER_NAME"
            

Replace `CLUSTER_NAME` with the name of the cluster that you want to investigate. This query shows the target control plane version and the previous control plane version.  
Control plane manual upgrade | 
    
    
    resource.type="gke_cluster"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.response.operationType="UPGRADE_MASTER"
    resource.labels.cluster_name="CLUSTER_NAME"
              
  
Node pool auto-upgrade (target version only) | 
    
    
    resource.type="gke_nodepool"
    protoPayload.methodName="google.container.internal.ClusterManagerInternal.UpdateClusterInternal"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.metadata.operationType="UPGRADE_NODES"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.nodepool_name="NODEPOOL_NAME"
            

Replace `NODEPOOL_NAME` with the name of the node pool that belongs to the cluster.  
Node pool manual upgrade | 
    
    
    resource.type="gke_nodepool"
    protoPayload.methodName="google.container.v1.ClusterManager.UpdateNodePool"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.response.operationType="UPGRADE_NODES"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.nodepool_name="NODEPOOL_NAME"
            

To find the previous node pool version, check the Kubernetes API logs:
    
    
    resource.type="k8s_cluster"
    resource.labels.cluster_name="CLUSTER_NAME"
    protoPayload.methodName="nodes.patch"
              
  
### Find detailed error messages in GKE logs

After the audit log shows you which operation failed and when, you can search for more detailed error messages from GKE components around the same time. These logs can contain the specific reasons for an upgrade failure, such as a misconfigured `PodDisruptionBudget` object.

For example, after finding a failed `UPGRADE_NODES` operation in the audit logs, you can use its timestamp to narrow your search. In Logs Explorer, enter the following query and then use the time-range selector to focus on the time when the failure occurred:
    
    
    resource.type="k8s_node"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.node_name="NODE_NAME"
    severity=ERROR
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `NODE_NAME`: the name of the node within the cluster that you want to check for errors.



### Use the gcloud CLI to view upgrade events

In addition to Logs Explorer, you can use gcloud CLI commands to review upgrade events.

To look for control plane upgrades, run the following command:
    
    
    gcloud container operations list --filter="TYPE=UPGRADE_MASTER"
    

The output is similar to the following:
    
    
    NAME: operation-1748588803271-cfd407a2-bfe7-4b9d-8686-9f1ff33a2a96
    TYPE: UPGRADE_MASTER
    LOCATION: LOCATION
    TARGET: CLUSTER_NAME
    STATUS_MESSAGE:
    STATUS: DONE
    START_TIME: 2025-05-30T07:06:43.271089972Z
    END_TIME: 2025-05-30T07:18:02.639579287Z
    

This output includes the following values:

  * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.
  * `CLUSTER_NAME`: the name of your cluster.



To look for node pool upgrades, run the following command:
    
    
    gcloud container operations list --filter="TYPE=UPGRADE_NODES"
    

The output is similar to the following:
    
    
    NAME: operation-1748588803271-cfd407a2-bfe7-4b9d-8686-9f1ff33a2a96
    TYPE: UPGRADE_NODES
    LOCATION: LOCATION
    TARGET: CLUSTER_NAME
    STATUS_MESSAGE:
    STATUS: DONE
    START_TIME: 2025-05-30T07:06:43.271089972Z
    END_TIME: 2025-05-30T07:18:02.639579287Z
    

### Example: Use logs to troubleshoot control plane upgrades

The following example shows you how to use logs to troubleshoot an unsuccessful control plane upgrade:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, filter for control plane upgrade logs by entering the following query:
         
         resource.type="gke_cluster"
         protoPayload.metadata.operationType=~"(UPDATE_CLUSTER|UPGRADE_MASTER)"
         resource.labels.cluster_name="CLUSTER_NAME"
         

Replace `CLUSTER_NAME` with the name of the cluster that you want to investigate.

  3. Click **Run query**.

  4. Review the log output for the following information:

  5. **Confirm that the upgrade started** : look for recent `UPGRADE_MASTER` events around the time that you initiated the upgrade. The presence of these events confirms that either you or GKE triggered the upgrade process.

     * **Verify the versions** : check the following fields to confirm the previous and target versions:

       * `protoPayload.metadata.previousMasterVersion`: shows the control plane version _before_ the upgrade.
       * `protoPayload.metadata.currentMasterVersion`: shows the version to which GKE attempted to upgrade the control plane.

For example, if you intended to upgrade to version 1.30.1-gke.1234 but accidentally specified 1.30.2-gke.4321 (a newer, potentially incompatible version for your workloads), reviewing these two fields would highlight this discrepancy. Alternatively, if the `currentMasterVersion` field still displays the earlier version after an extended period, this finding indicates that the upgrade failed to apply the new version.

     * **Look for errors** : check for repeated `UPGRADE_MASTER` events or other error messages. If the operation log stops without indicating completion or failure, this finding indicates a problem.




After you identify a specific error or behavior from the logs, you can use that information to find the appropriate solution in this guide.

## Troubleshoot node pool upgrades taking longer than usual

If your node pool upgrade is taking longer than expected, try the following solutions:

  1. Check the value of `terminationGracePeriodSeconds` in the manifest of your Pods. This value defines the maximum time that Kubernetes waits for a Pod to shut down gracefully. A high value (for example, a few minutes) can significantly extend upgrade durations because Kubernetes waits for the full period for each Pod. If this delay is causing issues, consider reducing the value.
  2. Check your `PodDisruptionBudget` objects. When a node is being drained, GKE waits for at most one hour per node to gracefully evict its workloads. If your `PodDisruptionBudget` object is too restrictive, it can prevent a graceful eviction from ever succeeding. In this scenario, GKE uses the entire one-hour grace period to try and drain the node before it finally times out and forces the upgrade to proceed. This delay, when repeated across multiple nodes, is a common cause of a slow overall cluster upgrade. To confirm if a restrictive `PodDisruptionBudget` object is the cause of your slow upgrades, use Logs Explorer:

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

     2. In the query pane, enter the following query:
            
            resource.type=("gke_cluster" OR "k8s_cluster")
            resource.labels.cluster_name="CLUSTER_NAME"
            protoPayload.response.message="Cannot evict pod as it would violate the pod's disruption budget."
            log_id("cloudaudit.googleapis.com/activity")
            

     3. Click **Run query**.

     4. Review the log output. If the `PodDisruptionBudget` object is the cause of your issue, the output is similar to the following:
            
            resourceName: "core/v1/namespaces/istio-system/pods/POD_NAME/eviction"
            
            response: {
              @type: "core.k8s.io/v1.Status"
              apiVersion: "v1"
              code: 429
              details: {
              causes: [
                0: {
                message: "The disruption budget istio-egressgateway needs 1 healthy pods and has 1 currently"
                reason: "DisruptionBudget"
                }
              ]
              }
              kind: "Status"
              message: "Cannot evict pod as it would violate the pod's disruption budget."
              metadata: {
              }
              reason: "TooManyRequests"
              status: "Failure"
            }
            

     5. After you've confirmed that a `PodDisruptionBudget` object is the cause, list all `PodDisruptionBudget` objects and make sure that the settings are appropriate:
            
            kubectl get pdb --all-namespaces
            

The output is similar to the following:
            
            NAMESPACE        NAME          MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
            example-app-one  one_pdb       3               0                 1                     12d
            

In this example, the `PodDisruptionBudget` named `one_pdb` requires a minimum of three available Pods. Because evicting a Pod during the upgrade would leave only two Pods available, the action violates the budget and causes the upgrade to stall.

If your `PodDisruptionBudget` object is working the way you want, you don't need to take any action. If it's not, consider relaxing the `PodDisruptionBudget` settings during the upgrade window.

  3. Check your node affinities. Restrictive rules can slow down upgrades by preventing Pods from being rescheduled onto available nodes if those nodes don't match the required labels. This issue is especially problematic during surge upgrades because node affinities can limit how many nodes can be upgraded simultaneously if nodes with the correct labels don't have enough cluster capacity to host the new Pods.

  4. Check if you use the [short-lived upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start). GKE uses the short-lived upgrade strategy for flex-start nodes and for nodes that use only queued provisioning on clusters running GKE version 1.32.2-gke.1652000 or later. If you use this upgrade strategy, the upgrade operation can take up to seven days.

  5. Check if you use [extended duration Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods) (available for Autopilot clusters). During an upgrade, GKE must drain all Pods from a node before the process can complete. However, during a GKE-initiated upgrade, GKE doesn't evict extended duration Pods for up to seven days. This protection prevents the node from draining. GKE forcibly terminates the Pod only after this period ends, and this significant, multi-day delay for a single node can delay more node upgrades in the Autopilot cluster.

  6. Attached Persistent Volumes can cause an upgrade process to take longer than usual, due to the time it takes to manage the lifecycle of these volumes.

  7. Check the [cluster auto-upgrade status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#status). If the reason is `SYSTEM_CONFIG`, automatic upgrades are temporarily paused for technical or business reasons. If you see this reason, we recommend not performing a manual upgrade unless it's required.




## Troubleshoot incomplete node pool upgrades

Occasionally, GKE can't complete a node pool upgrade, leaving the node pool partially upgraded. There are several reasons that cause incomplete upgrades:

  * [The upgrade was manually cancelled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#cancel).
  * The upgrade failed due to an issue such as new nodes failing to register, IP address exhaustion, or insufficient resource quotas.
  * GKE paused the upgrade. This pause can occur, for example, to prevent an upgrade to a version with known issues or during certain Google-initiated maintenance periods.
  * If you use auto-upgrades, a maintenance window ended before the upgrade could complete. Alternatively, a maintenance exclusion period started before the upgrade could complete. For more information, see [Maintenance window preventing node update completion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#unfinished-node-changes).



When a node pool is partially upgraded, the nodes run on different versions. To resolve this issue and verify that all nodes in the node pool run on the same version, either [resume the upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#resume) or [roll back the upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#rollback).

### How node upgrade strategies work with maintenance windows

The [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) strategy and the [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) strategy interact with maintenance windows differently:

  * **Surge upgrades** : the upgrade operation is paused if it runs beyond the maintenance window. The upgrade is automatically resumed during the next scheduled maintenance window.
  * **Blue-green upgrades** : the upgrade operation continues until completion, even if it exceeds the maintenance window. Blue-green upgrades offer granular control over the upgrade pace with features like batch and node pool soak times, and the additional node pool helps ensure workloads remain operational.



For more information about how specific operations work with maintenance policies, see the **Respects maintenance policies** columns in the tables in [Types of changes to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#types-of-changes).

## Troubleshoot unexpected auto-upgrade behavior

Sometimes, cluster auto-upgrades don't happen the way that you might expect. The following sections help you to resolve the following issues:

  * Clusters fail to upgrade when auto-upgrade is enabled
  * Clusters upgrade automatically when auto-upgrade is not enabled



### Clusters fail to upgrade when node auto-upgrade is enabled

If you haven't disabled node auto-upgrade, but an upgrade doesn't occur, try the following solutions:

  1. If you use a release channel, verify that node auto-upgrades aren't blocked. For clusters enrolled in a release channel, your `maintenancePolicy` is the primary way to control automated upgrades. It can prevent an upgrade from starting or interrupt one that is already in progress. An active maintenance exclusion can block an upgrade completely and the timing of a maintenance window can cause an interruption. Review your `maintenancePolicy` to determine if either of these settings is the cause:
         
         gcloud container clusters describe CLUSTER_NAME \
             --project PROJECT_ID  \
             --location LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster of the node pool to describe.
     * `PROJECT_ID`: the project ID of the cluster.
     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.

The output is similar to the following:
    
    …
    maintenancePolicy:
      maintenanceExclusions:
      - exclusionName: critical-event-q4-2025
        startTime: '2025-12-20T00:00:00Z'
        endTime: '2026-01-05T00:00:00Z'
        scope:
          noUpgrades: true # This exclusion blocks all upgrades
      window:
        dailyMaintenanceWindow:
          startTime: 03:00 # Daily window at 03:00 UTC
    …
    

In the output, review the `maintenancePolicy` section for the following two conditions:

     * **To see if an upgrade is blocked** : look for an active `maintenanceExclusion` with a `NO_MINOR_OR_NODE_UPGRADES` scope. This setting generally prevents GKE from initiating a new upgrade.
     * **To see if an upgrade was interrupted** : check the schedule for your `dailyMaintenanceWindow` or `maintenanceExclusions`. If an upgrade runs beyond the scheduled window, GKE pauses the upgrade, resulting in a partial upgrade. For more information about partial upgrades, see the Troubleshoot incomplete upgrades section.

To resolve these issues, you can wait for an exclusion to end, remove it, or adjust your maintenance windows to allow more time for upgrades to complete.

  2. If you don't use a release channel, verify that auto-upgrade is still enabled for the node pool:
         
         gcloud container node-pools describe NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION
         

Replace `NODE_POOL_NAME` with the name of the node pool to describe.

If node pool auto-upgrades are enabled for this node pool, the output in the `autoUpgrade` field is the following:
         
         management:
           autoUpgrade: true
         

If `autoUpgrade` is set to `false`, or the field isn't present, [enable auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#enable).

  3. The upgrade might not have rolled out to the region or zone where your cluster is located, even if the upgrade was mentioned in the release notes. GKE upgrades are rolled out progressively over multiple days (typically four or more). After the upgrade reaches your region or zone, the upgrade only starts during approved maintenance windows. For example, a rollout could reach your cluster's zone on Day One of the rollout, but the cluster's next maintenance window isn't until Day Seven. In this scenario, GKE won't upgrade the cluster until Day Seven. For more information, see [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).




### Clusters upgrade automatically when auto-upgrade is not enabled

To help maintain the reliability, availability, security, and performance of your GKE environment, GKE might automatically upgrade your clusters, even if you don't use auto-upgrades.

GKE might bypass your maintenance windows, exclusions, or disabled node pool auto-upgrades to perform necessary upgrades for several critical reasons, such as the following:

  * Clusters whose control planes are running a GKE version that has reached its end of support date. To confirm that your cluster is nearing its end of support date, see [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).
  * Nodes within a cluster that are running a GKE version that has reached its end of support date.
  * Clusters that are in a running state, but show no activity for an extended period. For example, GKE might consider a cluster with no API calls, no network traffic, and no active use of subnets to be abandoned.
  * Clusters that exhibit persistent instability that repeatedly cycle through operational states. For example, states that loop from running to degraded, repairing, or suspended and back to running without a resolution.



If you observe an unexpected automatic upgrade and have concerns about the effect that this upgrade might have on your cluster, contact [Cloud Customer Care](https://cloud.google.com/support-hub) for assistance.

## Troubleshoot failed upgrades

When your upgrade fails, GKE produces error messages. The following sections explain the causes and resolutions for the following errors:

  * Error: `kube-apiserver` is unhealthy
  * Error: DeployPatch failed



### Error: `kube-apiserver` is unhealthy

Sometimes, you might see the following error message when you start a manual control plane upgrade of your cluster's GKE version:
    
    
    FAILED: All cluster resources were brought up, but: component
    "KubeApiserverReady" from endpoint "readyz of kube apiserver is not successful"
    is unhealthy.
    

This message appears in the gcloud CLI and in the `gke_cluster` and `gke_nodepool` resource type log entries.

This issue occurs when some user-deployed admission webhooks block system components from creating the permissive RBAC roles that are required to function correctly.

During a control plane upgrade, GKE re-creates the Kubernetes API server (`kube-apiserver`) component. If a webhook blocks the RBAC role for the API server component, the API server won't start and the cluster upgrade won't complete. Even if a webhook is working correctly, it can cause the cluster upgrade to fail because the newly created control plane might be unable to reach the webhook.

Kubernetes [auto-reconciles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#auto-reconciliation) the default system RBAC roles with the default policies in the latest minor version. The default policies for system roles sometimes change in new Kubernetes versions.

To perform this reconciliation, GKE creates or updates the ClusterRoles and ClusterRoleBindings in the cluster. If you have a webhook that intercepts and rejects the create or update requests because of the scope of permissions that the default RBAC policies use, the API server can't function on the new minor version.

To identify the failing webhook, [check your GKE audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#viewing_logs) for RBAC calls with the following information:
    
    
    protoPayload.resourceName="RBAC_RULE"
    protoPayload.authenticationInfo.principalEmail="system:apiserver"
    

In this output, `RBAC_RULE` is the full name of the RBAC role, such as `rbac.authorization.k8s.io/v1/clusterroles/system:controller:horizontal-pod-autoscaler`.

The name of the failing webhook is displayed in the log with the following format:
    
    
    admission webhook WEBHOOK_NAME denied the request
    

To resolve this issue, try the following solutions:

  1. Review your ClusterRoles to ensure that they are not overly restrictive. Your policies shouldn't block GKE's requests to create or update the ClusterRoles with the default `system:` prefix.
  2. Adjust your webhook to not intercept requests for creating and updating system RBAC roles.
  3. Disable the webhook.



### Error: DeployPatch failed

Sometimes, the cluster upgrade operation fails with the following error:
    
    
    DeployPatch failed
    

This error can happen if the Kubernetes control plane remains unhealthy for over 20 minutes.

This error is often transient because the control plane retries the operation until it succeeds. If the upgrade continues to fail with this error, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

## Troubleshoot issues after a completed upgrade

If you encounter unexpected behavior after your upgrade has completed, the following sections offer troubleshooting guidance for the following common problems:

  * Unexpected behavior due to breaking changes
  * Workloads evicted after Standard cluster upgrade
  * Pods stuck in a Pending state
  * Node CPU usage higher than expected



### Unexpected behavior due to breaking changes

If the upgrade completed successfully, but you notice unexpected behavior after an upgrade, check the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for information about bugs and breaking changes related to the version to which the cluster upgraded.

### Workloads evicted after Standard cluster upgrade

Your workloads might be at risk of eviction after a cluster upgrade if all of the following conditions are true:

  * The system workloads require more space when the cluster's control plane is running the new GKE version.
  * Your existing nodes don't have enough resources to run the new system workloads and your existing workloads.
  * Cluster autoscaler is disabled for the cluster.



To resolve this issue, try the following solutions:

  1. [Enable autoscaling for existing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enable_autoscaling).
  2. [Enable node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable).
  3. [Create a new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add).
  4. [Scale up an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool).



### Pods stuck in `Pending` state after configuring Node Allocatable

If you've configured [Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources), a node version upgrade can sometimes cause Pods that had a `Running` state to become stuck in a `Pending` state. This change typically occurs because the upgraded node consumes slightly different system resources, or because Pods that were rescheduled must now fit within Node Allocatable limits on the new or modified nodes, potentially under stricter conditions.

If your Pods have a status of `Pending` after an upgrade, try the following solutions:

  1. Verify that the CPU and memory requests for your Pods don't exceed their peak usage. With GKE reserving CPU and memory for overhead, Pods cannot request these resources. Pods that request more CPU or memory than they use prevent other Pods from requesting these resources, and might leave the cluster underutilized. For more information, see [How Pods with resource requests are scheduled](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#how-pods-with-resource-requests-are-scheduled) in the Kubernetes documentation.
  2. Consider [increasing the size of your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster#increase).
  3. To verify if the upgrade is the cause of this issue, revert the upgrade by [downgrading your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes).
  4. Configure your cluster to [send Kubernetes scheduler metrics to Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics) and view [scheduler metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#scheduler). By monitoring these metrics, you can determine if there are enough resources for the Pods to run.



## Troubleshoot version and compatibility issues

Maintaining supported and compatible versions for all of your cluster's components is essential for stability and performance. The following sections provide guidance about how to identify and resolve versioning and compatibility issues that can affect the upgrade process.

### Check for control plane and node version incompatibility

Version skew between your control plane and nodes can cause cluster instability. The [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew) states that a control plane is only compatible with nodes up to two minor versions earlier. For example, a 1.19 control plane works with 1.19, 1.18, and 1.17 nodes.

If your nodes fall outside this supported window, you risk running into critical compatibility problems. These issues are often API-related; for example, a workload on an older node might use an API version that has been deprecated or removed in the newer control plane. This incompatibility can also lead to more severe failures, like a broken networking path that prevents nodes from registering with the cluster if an incompatible workload disrupts communication.

Periodically, the GKE team performs upgrades of the cluster control plane on your behalf. Control planes are upgraded to newer stable versions of Kubernetes. To ensure your nodes remain compatible with the upgraded control plane, they must also be kept up-to-date. By default, GKE handles this upgrade because a cluster's nodes have [auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades) enabled, and we recommend that you don't disable it. If auto-upgrade is disabled for a cluster's nodes, and you don't manually upgrade them, your control plane eventually becomes incompatible with your nodes.

To confirm if your control plane and node versions are incompatible, check what version of Kubernetes your cluster's control plane and node pools are running:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --project PROJECT_ID  \
        --location LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster of the node pool to describe.
  * `PROJECT_ID`: the project ID of the cluster.
  * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.



The output is similar to the following:
    
    
    …
    currentMasterVersion: 1.32.3-gke.1785003
    …
    currentNodeVersion: 1.26.15-gke.1090000
    …
    

In this example, the control plane version and the node pool version are incompatible.

To resolve this issue, [manually upgrade the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) version to a version that is compatible with the control plane.

If you're concerned about the upgrade process causing disruption to workloads running on the affected nodes, then complete the following steps to migrate your workloads to a new node pool:

  1. [Create a new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add) with a compatible version.
  2. [Cordon](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration) the nodes of the existing node pool.
  3. Optional: update your workloads running on the existing node pool to add a nodeSelector for the label `cloud.google.com/gke-nodepool:NEW_NODE_POOL_NAME`. Replace `NEW_NODE_POOL_NAME` with the name of the new node pool. This action ensures that GKE places those workloads on nodes in the new node pool.
  4. [Drain](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) the existing node pool.
  5. Check that the workloads are running successfully in the new node pool. If they are, you can delete the old node pool. If you notice workload disruptions, reschedule the workloads on the existing nodes by uncordoning the nodes in the existing node pool and draining the new nodes.



### Node CPU usage is higher than expected

You might encounter an issue where some nodes are using more CPU than expected from the running Pods.

This issue can occur if you use manual upgrades and your clusters or nodes haven't been upgraded to run a [supported version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#supported-versions). Review the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) to ensure the versions you use are available and supported.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
