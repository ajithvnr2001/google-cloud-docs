---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility/
title: View cluster autoscaler events and metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:03.251643+00:00
---

# View cluster autoscaler events and metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  View cluster autoscaler events and metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides information about visibility events and metrics emitted by [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) in Google Kubernetes Engine (GKE). By analyzing these logs and metrics, you can gain insights into how cluster autoscaler manages your cluster's scaling, track node provisioning trends, and understand the reasons behind its decisions.

You can use the following information to observe the cluster autoscaler:

  * **Visibility event logs** : event logs in Cloud Logging that provide detailed information about specific scaling actions, such as `scaleUp`, `scaleDown`, and `noScaleUp` decisions. The events described in this guide are separate from the Kubernetes events produced by the cluster autoscaler.
  * **Cloud Monitoring metrics** : aggregate time-series metrics that provide high-level trends on node provisioning attempts, failures, and pending Pods across ComputeClasses.



## Requirements

To see autoscaler events, you must enable [Cloud Logging](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing) in your cluster. The events won't be produced if Logging is disabled.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster. If you need one, [create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



## Viewing events

The visibility events for the cluster autoscaler are stored in a Cloud Logging log, in the same project as where your GKE cluster is located. You can also view these events from the notifications in the Google Kubernetes Engine page in Google Cloud console.

#### Viewing visibility event logs

To view the logs, perform the following:

  1. In the Google Cloud console, go to the **Kubernetes Clusters** page.

[Go to Kubernetes Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the name of your cluster to view its **Cluster Details** page.

  3. On the **Cluster Details** page, click the **Logs** tab.

  4. On the **Logs** tab, click the **Autoscaler Logs** tab to view the logs.

  5. (Optional) To apply more advanced filters to narrow the results, click the button with the arrow on the right side of the page to view the logs in Logs Explorer.




#### Viewing visibility event notifications

To view the visibility event notifications on the Google Kubernetes Engine page, perform the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Check the **Notifications** column for specific clusters to find notifications related to scaling.

  3. Click the notification for detailed information, recommended actions, and to access the logs for this event.




## Monitor pending Pod status with Cloud Monitoring

Available on GKE version 1.37 and later, in addition to visibility events, the GKE cluster autoscaler exports the `kubernetes.io/autoscaler/cluster_pending_pods_per_ccc` real-time metric to Cloud Monitoring. This metric provides a count of Pods in the `Pending` state, as seen and processed by the cluster autoscaler, and is available for the `k8s_entity` monitored resource type.

This metric is particularly useful for understanding the demand for different ComputeClasses.

### Key labels

The metric includes the following key labels:

  * `resource.labels.entity_type`: The entity type, which is always `ComputeClass` for this metric.
  * `resource.labels.entity_name`: The name of the ComputeClass the Pods are requesting. Empty ("") for Pods without a specific ComputeClass.
  * `metric.labels.reason`: The current stage of the Pod in the cluster autoscaler's view (`unprocessed`, `provisioning_in_progress`, `unable_to_provision`, `no_action_taken`).
  * `metric.labels.type`: The type of Pod (`system_pod` or `user_pod`).



### Example use cases

The following examples show how to query this metric with PromQL:

  * **Track scale-up demand per ComputeClass:**
        
        sum by (entity_name) (
          kubernetes_io:autoscaler_cluster_pending_pods_per_ccc{
            monitored_resource="k8s_entity",
            entity_type="ComputeClass",
            type="user_pod"
          }
        )
        

This query shows the total pending user Pods for each ComputeClass, indicating where the current scaling demand lies.

  * **Monitor blocked scale-ups:**
        
        sum by (entity_name, type) (
          kubernetes_io:autoscaler_cluster_pending_pods_per_ccc{
            monitored_resource="k8s_entity",
            entity_type="ComputeClass",
            reason="unable_to_provision"
          }
        )
        

This query helps quickly identify if any ComputeClasses are experiencing issues where the cluster autoscaler can't provision nodes. 




By analyzing this metric, you can gain insights into the cluster autoscaler's backlog and its ability to provision nodes for different workload types defined by your ComputeClasses. For troubleshooting specific ComputeClass scheduling issues, see [Troubleshoot ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass#analyze-ca-metric).

## Monitor node provisioning

Available on GKE version 1.37 and later, the following Cloud Monitoring metrics provide visibility into cluster autoscaler's node provisioning activities, broken down by ComputeClasses. These metrics use the `k8s_entity` monitored resource type. In this resource type, the value of the `resource.labels.entity_type` label is `ComputeClass`, and the value of the `resource.labels.entity_name` label is the name of the ComputeClass that defines the node group being provisioned. An empty string ("") for the `resource.labels.entity_name` label indicates that the node group being provisioned is not associated with any specific ComputeClass.

### Use metrics and logs together

To monitor and diagnose potential issues with the cluster autoscaler, you can use a combination of metrics and logs to do tasks like the following:

  * **Identify trends and set alerts with metrics** : use Cloud Monitoring metrics to monitor aggregate provisioning health, visualize trends over time, and configure alerting policies (such as alerts on spikes in provisioning failures or quota exhaustion).
  * **Investigate root causes with logs** : failed scale-up attempts also generate visibility log entries (such as `noScaleUp` or `eventResult` events) in Cloud Logging. When metrics indicate a spike in failures during a time window, inspect the corresponding logs to view the specific Pods, target node pools, and detailed error messages.



### Monitor node provisioning attempts

The `kubernetes.io/autoscaler/cluster_node_provisioning_attempts_count_per_ccc` metric tracks how often the autoscaler tries to add nodes to a node group defined by a specific ComputeClass. An empty string (`""`) for the `resource.labels.entity_name` label indicates that the provisioning activity is not associated with any specific ComputeClass.

**Important:** Because of the asynchronous nature of provisioning, don't subtract failures from attempts to determine successes in real time. Instead, compare trends over a window (for example, 10m).

The following PromQL example tracks scale-up activity per ComputeClass:
    
    
    sum by (entity_name) (
      increase(
        kubernetes_io:autoscaler_cluster_node_provisioning_attempts_count_per_ccc{
          monitored_resource="k8s_entity",
          entity_type="ComputeClass"
        }[5m]
      )
    )
    

### Monitor node provisioning failures

The `kubernetes.io/autoscaler/cluster_node_provisioning_failed_attempts_count_per_ccc` metric provides a count of failed scale-up attempts. Use this metric to identify infrastructure bottlenecks or misconfigurations.

Important labels for this metric include the following:

  * `resource.labels.entity_name`: the name of the ComputeClass defining the node group for which provisioning failed. The value is empty ("") if the node group is not defined by a specific ComputeClass.
  * `metric.labels.reason`: the string code representing the failure reason.



The following PromQL example identifies top failure reasons per ComputeClass:
    
    
    sum by (reason, entity_name) (
      increase(
        kubernetes_io:autoscaler_cluster_node_provisioning_failed_attempts_count_per_ccc{
          monitored_resource="k8s_entity",
          entity_type="ComputeClass"
        }[1h]
      )
    )
    

#### Failure reasons (`metric.labels.reason`)

The `metric.labels.reason` label on the `kubernetes.io/autoscaler/cluster_node_provisioning_failed_attempts_count_per_ccc` metric provides a string code indicating the cause of the node provisioning failure. For a detailed explanation of each reason, and potential corrective actions, see the [Interpret failure reasons](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass#interpreting-failure-reasons) troubleshooting guide.

## Types of events

All logged events are in the JSON format and can be found in the **jsonPayload** field of a log entry. All timestamps in the events are UNIX second timestamps.

Here's a summary of the types of events emitted by the cluster autoscaler:

Event type | Description  
---|---  
`status` | Occurs periodically and describes the size of all autoscaled node pools and the target size of all autoscaled node pools as observed by the cluster autoscaler.  
`scaleUp` | Occurs when cluster autoscaler scales the cluster up.  
`scaleDown` | Occurs when cluster autoscaler scales the cluster down.  
`eventResult` | Occurs when a scaleUp or a scaleDown event completes successfully or unsuccessfully.  
`nodePoolCreated` | Occurs when cluster autoscaler with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) enabled creates a new node pool.  
`nodePoolDeleted` | Occurs when cluster autoscaler with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) enabled deletes a node pool.  
`noScaleUp` | Occurs when there are unschedulable Pods in the cluster, and cluster autoscaler cannot scale the cluster up to accommodate the Pods.  
`noScaleDown` | Occurs when there are nodes that are blocked from being deleted by cluster autoscaler.  
  
### Status event

A `status` event is emitted periodically, and describes the actual size of all autoscaled node pools and the target size of all autoscaled node pools as observed by cluster autoscaler.

#### Example

The following log sample shows a `status` event:
    
    
    {
      "status": {
        "autoscaledNodesCount": 4,
        "autoscaledNodesTarget": 4,
        "measureTime": "1582898536"
      }
    }
    

### ScaleUp event

A `scaleUp` event is emitted when the cluster autoscaler scales the cluster up. The autoscaler increases the size of the cluster's node pools by scaling up the underlying [Managed Instance Groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) for the node pools. To learn more about how scale up works, see [How does scale up work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-up-work) in the Kubernetes Cluster Autoscaler FAQ.

The event contains information on which MIGs were scaled up, by how many nodes, and which unschedulable Pods triggered the event.

**Note:** The fact that the Pods listed in this event triggered scaling up does not mean that the Pods end up being scheduled on the new nodes.

The list of triggering Pods is truncated to 50 arbitrary entries. The actual number of triggering Pods can be found in the `triggeringPodsTotalCount` field.

#### Example

The following log sample shows a `scaleUp` event:
    
    
    {
      "decision": {
        "decideTime": "1582124907",
        "eventId": "ed5cb16d-b06f-457c-a46d-f75dcca1f1ee",
        "scaleUp": {
          "increasedMigs": [
            {
              "mig": {
                "name": "test-cluster-default-pool-a0c72690-grp",
                "nodepool": "default-pool",
                "zone": "us-central1-c"
              },
              "requestedNodes": 1
            }
          ],
          "triggeringPods": [
            {
              "controller": {
                "apiVersion": "apps/v1",
                "kind": "ReplicaSet",
                "name": "test-85958b848b"
              },
              "name": "test-85958b848b-ptc7n",
              "namespace": "default"
            }
          ],
          "triggeringPodsTotalCount": 1
        }
      }
    }
    

### ScaleDown event

A `scaleDown` event is emitted when cluster autoscaler scales the cluster down. To learn more about how scale down works, see [How does scale down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work) in the Kubernetes Cluster Autoscaler FAQ.

The `cpuRatio` and `memRatio` fields describe the CPU and memory utilization of the node, as a percentage. This utilization is a sum of Pod requests divided by node allocatable, not real utilization.

The list of evicted Pods is truncated to 50 arbitrary entries. The actual number of evicted Pods can be found in the `evictedPodsTotalCount` field.

Use the following query to verify if the cluster autoscaler scaled down the nodes:
    
    
    resource.type="k8s_cluster" \
    resource.labels.location=COMPUTE_REGION \
    resource.labels.cluster_name=CLUSTER_NAME \
    log_id("container.googleapis.com/cluster-autoscaler-visibility") \
    ( "decision" NOT "noDecisionStatus" )
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.

  * `COMPUTE_REGION`: the cluster's Compute Engine region, such as `us-central1`.




#### Example

The following log sample shows a `scaleDown` event:
    
    
    {
      "decision": {
        "decideTime": "1580594665",
        "eventId": "340dac18-8152-46ff-b79a-747f70854c81",
        "scaleDown": {
          "nodesToBeRemoved": [
            {
              "evictedPods": [
                {
                  "controller": {
                    "apiVersion": "apps/v1",
                    "kind": "ReplicaSet",
                    "name": "kube-dns-5c44c7b6b6"
                  },
                  "name": "kube-dns-5c44c7b6b6-xvpbk"
                }
              ],
              "evictedPodsTotalCount": 1,
              "node": {
                "cpuRatio": 23,
                "memRatio": 5,
                "mig": {
                  "name": "test-cluster-default-pool-c47ef39f-grp",
                  "nodepool": "default-pool",
                  "zone": "us-central1-f"
                },
                "name": "test-cluster-default-pool-c47ef39f-p395"
              }
            }
          ]
        }
      }
    }
    

You can also view the `scale-down` event on the nodes with no workload running (typically only system pods created by DaemonSets).

Use the following query to see the event logs:
    
    
    resource.type="k8s_cluster" \
    resource.labels.project_id=PROJECT_ID \
    resource.labels.location=COMPUTE_REGION \
    resource.labels.cluster_name=CLUSTER_NAME \
    severity>=DEFAULT \
    logName="projects/PROJECT_ID/logs/events" \
    ("Scale-down: removing empty node")
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `CLUSTER_NAME`: the name of the cluster.

  * `COMPUTE_REGION`: the cluster's Compute Engine region, such as `us-central1`.




### EventResult event

An `eventResult` event is emitted when a scaleUp or a scaleDown event completes successfully or unsuccessfully. This event contains a list of event IDs (from the `eventId` field in scaleUp or scaleDown events), along with error messages. An empty error message indicates the event completed successfully. A list of eventResult events are aggregated in the `results` field.

To diagnose errors, consult the ScaleUp errors and ScaleDown errors sections.

#### Example

The following log sample shows an `eventResult` event:
    
    
    {
      "resultInfo": {
        "measureTime": "1582878896",
        "results": [
          {
            "eventId": "2fca91cd-7345-47fc-9770-838e05e28b17"
          },
          {
            "errorMsg": {
              "messageId": "scale.down.error.failed.to.delete.node.min.size.reached",
              "parameters": [
                "test-cluster-default-pool-5c90f485-nk80"
              ]
            },
            "eventId": "ea2e964c-49b8-4cd7-8fa9-fefb0827f9a6"
          }
        ]
      }
    }
    

### NodePoolCreated event

A `nodePoolCreated` event is emitted when cluster autoscaler with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) enabled creates a new node pool. This event contains the name of the created node pool and a list of its underlying [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups). If the node pool was created because of a scaleUp event, the `eventId` of the corresponding scaleUp event is included in the `triggeringScaleUpId` field.

#### Example

The following log sample shows a `nodePoolCreated` event:
    
    
    {
      "decision": {
        "decideTime": "1585838544",
        "eventId": "822d272c-f4f3-44cf-9326-9cad79c58718",
        "nodePoolCreated": {
          "nodePools": [
            {
              "migs": [
                {
                  "name": "test-cluster-nap-n1-standard--b4fcc348-grp",
                  "nodepool": "nap-n1-standard-1-1kwag2qv",
                  "zone": "us-central1-f"
                },
                {
                  "name": "test-cluster-nap-n1-standard--jfla8215-grp",
                  "nodepool": "nap-n1-standard-1-1kwag2qv",
                  "zone": "us-central1-c"
                }
              ],
              "name": "nap-n1-standard-1-1kwag2qv"
            }
          ],
          "triggeringScaleUpId": "d25e0e6e-25e3-4755-98eb-49b38e54a728"
        }
      }
    }
    

### NodePoolDeleted event

A `nodePoolDeleted` event is emitted when cluster autoscaler with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) enabled deletes a node pool.

#### Example

The following log sample shows a `nodePoolDeleted` event:
    
    
    {
      "decision": {
        "decideTime": "1585830461",
        "eventId": "68b0d1c7-b684-4542-bc19-f030922fb820",
        "nodePoolDeleted": {
          "nodePoolNames": [
            "nap-n1-highcpu-8-ydj4ewil"
          ]
        }
      }
    }
    

### NoScaleUp event

A `noScaleUp` event is periodically emitted when there are unschedulable Pods in the cluster and cluster autoscaler cannot scale the cluster up to accommodate the Pods.

  * noScaleUp events are best-effort, that is, these events don't cover all possible reasons for why cluster autoscaler cannot scale up.
  * noScaleUp events are throttled to limit the produced log volume. Each persisting reason is only emitted every couple of minutes.
  * All the reasons can be arbitrarily split across multiple events. For example, there is no guarantee that all rejected MIG reasons for a single Pod group will appear in the same event.
  * The list of unhandled Pod groups is truncated to 50 arbitrary entries. The actual number of unhandled Pod groups can be found in the `unhandledPodGroupsTotalCount` field.



#### Reason fields

The following fields help to explain why scaling up did not occur:

  * `reason`: Provides a global reason for why cluster autoscaler is prevented from scaling up. Refer to the NoScaleUp top-level reasons section for details.
  * `napFailureReason`: Provides a global reason preventing cluster autoscaler from provisioning additional node pools (for example, node auto-provisioning is disabled). Refer to the NoScaleUp top-level node auto-provisioning reasons section for details.
  * `skippedMigs[].reason`: Provides information about why a particular MIG was skipped. Cluster autoscaler skips some MIGs from consideration for any Pod during a scaling up attempt (for example, because adding another node would exceed cluster-wide [resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#resource_limits)). Refer to the NoScaleUp MIG-level reasons section for details.
  * `unhandledPodGroups`: Contains information about why a particular group of unschedulable Pods does not trigger scaling up. The Pods are grouped by their immediate controller. Pods without a controller are in groups by themselves. Each Pod group contains an arbitrary example Pod and the number of Pods in the group, as well as the following reasons: 
    * `napFailureReasons`: Reasons why cluster autoscaler cannot provision a new node pool to accommodate this Pod group (for example, Pods have affinity constraints). Refer to the NoScaleUp Pod-level node auto-provisioning reasons section for details.
    * `rejectedMigs[].reason`: Per-MIG reasons why cluster autoscaler cannot increase the size of a particular MIG to accommodate this Pod group (for example, the MIG's node is too small for the Pods). Refer to the NoScaleUp MIG-level reasons section for details.



#### Example

The following log sample shows a `noScaleUp` event:
    
    
    {
      "noDecisionStatus": {
        "measureTime": "1582523362",
        "noScaleUp": {
          "skippedMigs": [
            {
              "mig": {
                "name": "test-cluster-nap-n1-highmem-4-fbdca585-grp",
                "nodepool": "nap-n1-highmem-4-1cywzhvf",
                "zone": "us-central1-f"
              },
              "reason": {
                "messageId": "no.scale.up.mig.skipped",
                "parameters": [
                  "max cluster cpu limit reached"
                ]
              }
            }
          ],
          "unhandledPodGroups": [
            {
              "napFailureReasons": [
                {
                  "messageId": "no.scale.up.nap.pod.zonal.resources.exceeded",
                  "parameters": [
                    "us-central1-f"
                  ]
                }
              ],
              "podGroup": {
                "samplePod": {
                  "controller": {
                    "apiVersion": "v1",
                    "kind": "ReplicationController",
                    "name": "memory-reservation2"
                  },
                  "name": "memory-reservation2-6zg8m",
                  "namespace": "autoscaling-1661"
                },
                "totalPodCount": 1
              },
              "rejectedMigs": [
                {
                  "mig": {
                    "name": "test-cluster-default-pool-b1808ff9-grp",
                    "nodepool": "default-pool",
                    "zone": "us-central1-f"
                  },
                  "reason": {
                    "messageId": "no.scale.up.mig.failing.predicate",
                    "parameters": [
                      "NodeResourcesFit",
                      "Insufficient memory"
                    ]
                  }
                }
              ]
            }
          ],
          "unhandledPodGroupsTotalCount": 1
        }
      }
    }
    

### NoScaleDown event

A `noScaleDown` event is periodically emitted when there are nodes which are blocked from being deleted by cluster autoscaler.

  * Nodes that cannot be removed because their utilization is high are not included in noScaleDown events.
  * NoScaleDown events are best effort, that is, these events don't cover all possible reasons for why cluster autoscaler cannot scale down.
  * NoScaleDown events are throttled to limit the produced log volume. Each persisting reason will only be emitted every couple of minutes.
  * The list of nodes is truncated to 50 arbitrary entries. The actual number of nodes can be found in the `nodesTotalCount` field.



#### Reason fields

The following fields help to explain why scaling down did not occur:

  * `reason`: Provides a global reason for why cluster autoscaler is prevented from scaling down (for example, a backoff period after recently scaling up). Refer to the NoScaleDown top-level reasons section for details.
  * `nodes[].reason`: Provides per-node reasons for why cluster autoscaler is prevented from deleting a particular node (for example, there's no place to move the node's Pods to). Refer to the NoScaleDown node-level reasons section for details.



#### Example

The following log sample shows a `noScaleDown` event:
    
    
    {
      "noDecisionStatus": {
        "measureTime": "1582858723",
        "noScaleDown": {
          "nodes": [
            {
              "node": {
                "cpuRatio": 42,
                "mig": {
                  "name": "test-cluster-default-pool-f74c1617-grp",
                  "nodepool": "default-pool",
                  "zone": "us-central1-c"
                },
                "name": "test-cluster-default-pool-f74c1617-fbhk"
              },
              "reason": {
                "messageId": "no.scale.down.node.no.place.to.move.pods"
              }
            }
          ],
          "nodesTotalCount": 1,
          "reason": {
            "messageId": "no.scale.down.in.backoff"
          }
        }
      }
    }
    

## Messages

The events emitted by the cluster autoscaler use parameterized messages to provide explanations for the event. The `parameters` field is available with the `messageId` field, such as in this [example log for a NoScaleUp event](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#example_7).

This section provides descriptions for various `messageId` and its corresponding parameters. However, this section does not contain all possible messages, and may be extended at any time.

**Note:** Visibility events provide a limited view into the behavior of cluster autoscaler. The purpose of the logs is to provide transparency into why cluster autoscaler makes decisions. **The events are not necessarily an indication of system failure.** If the outcome is unexpected, use the following steps to mitigate the root cause.

### ScaleUp errors

You can find event error messages for `scaleUp` events in the corresponding `eventResult` event, in the `resultInfo.results[].errorMsg` field.

When a scale-up operation fails because it exceeds a quota, it is a node creation error that triggers a system backoff period, which can last up to 30 minutes. For more information, see [Backoff periods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#backoff-periods).

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"scale.up.error.out.of.resources"` | Resource errors occur when you try to request new resources in a zone that cannot accommodate your request due to the current unavailability of a Compute Engine resource, such as GPUs or CPUs. | Failing MIG IDs. | Follow the [resource availability troubleshooting steps](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) in the Compute Engine documentation.  
`"scale.up.error.quota.exceeded"` | The scaleUp event failed because some of the MIGs couldn't be increased, due to exceeded Compute Engine quota. | Failing MIG IDs. | Check the **Errors** tab of the MIG in the Google Cloud console to see what quota is being exceeded. After you know which quota is being exceeded, follow the instructions to [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).  
`"scale.up.error.waiting.for.instances.timeout"` | Scale up of managed instance group failed to scale up due to timeout.  | Failing MIG IDs. | If the instances boot but do not register with the control plane, follow the [instance registration troubleshooting steps](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration#find-instance-failed-registration). This message should be transient. If it persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
`"scale.up.error.ip.space.exhausted"` | Can't scale up because instances in some of the managed instance groups ran out of IPs. This means that the cluster doesn't have enough unallocated IP address space to use to add new nodes or Pods. | Failing MIG IDs. | Follow the troubleshooting steps in [Not enough free IP address space for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vpc-clusters#not_enough_space).  
`"scale.up.error.service.account.deleted"` | Can't scale up because the service account was deleted. | Failing MIG IDs. |  Try to [undelete the service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting). If that procedure is unsuccessful, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
### Reasons for a noScaleUp event

A `noScaleUp` event is periodically emitted when there are unschedulable Pods in the cluster and cluster autoscaler cannot scale the cluster up to schedule the Pods. `noScaleUp` events are best-effort, and don't cover all possible cases.

#### NoScaleUp top-level reasons

Top-level reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.reason` field. The message contains a top-level reason for why cluster autoscaler cannot scale the cluster up.

Message | Details | Mitigation  
---|---|---  
`"no.scale.up.in.backoff"` | No scale up because scaling up is in a backoff period (temporarily blocked). This message that can occur during scale up events with a large number of Pods. |  This message should be transient. Check this error after a few minutes. If this message persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
#### NoScaleUp top-level node auto-provisioning reasons

Top-level node auto-provisioning reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.napFailureReason` field. The message contains a top-level reason for why cluster autoscaler cannot provision new node pools.

Message | Details | Mitigation  
---|---|---  
`"no.scale.up.nap.disabled"` |  Node auto provisioning couldn't scale up because node auto provisioning is not enabled at cluster level. If node auto-provisioning is disabled, new nodes won't be automatically provisioned if the pending Pod has requirements that can't be satisfied by any existing node pools. | Review the cluster configuration and consider [enabling node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable).  
  
#### NoScaleUp MIG-level reasons

MIG-level reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.skippedMigs[].reason` and `noDecisionStatus.noScaleUp.unhandledPodGroups[].rejectedMigs[].reason` fields. The message contains a reason why cluster autoscaler can't increase the size of a particular MIG.

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.up.mig.skipped"` | Cannot scale up a MIG because it was skipped during the simulation. | Reasons why the MIG was skipped (for example, missing a Pod requirement). | Review the parameters included in the error message and address why the MIG was skipped.  
`"no.scale.up.mig.failing.predicate"` | Can't scale up a node pool because of a failing scheduling predicate for the pending Pods. |  Name of the failing predicate and reasons why it failed. | Review the Pod requirements, such as [affinity rules](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-respect-node-affinity-when-selecting-node-groups-to-scale-up), taints or tolerations, and resource requirements.  
  
#### NoScaleUp Pod-group-level node auto-provisioning reasons

Pod-group-level node auto-provisioning reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.unhandledPodGroups[].napFailureReasons[]` field. The message contains a reason why cluster autoscaler cannot provision a new node pool to schedule a particular Pod group.

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.up.nap.pod.gpu.no.limit.defined"` | Node auto-provisioning couldn't provision any node group because a pending Pod has a GPU request, but [GPU resource limits are not defined at the cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#gpu_limits). | Requested GPU type. | Review the pending Pod's GPU request, and update the cluster-level node auto-provisioning [configuration for GPU limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#gpu_limits).  
`"no.scale.up.nap.pod.gpu.type.not.supported"` | Node auto-provisioning did not provision any node group for the Pod because it has requests for an unknown GPU type. | Requested GPU type. | Check the pending Pod's configuration for the GPU type to ensure that it matches a [supported GPU type](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads).   
`"no.scale.up.nap.pod.zonal.resources.exceeded"` | Node auto-provisioning did not provision any node group for the Pod in this zone because doing so would either violate the [cluster-wide maximum resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#limits_for_clusters), exceed the available resources in the zone, or there is no machine type that could fit the request. | Name of the considered zone. | Review and update [cluster-wide maximum resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#limits_for_clusters), the Pod resource requests, or the [available zones for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#auto-provisioning_locations).  
`"no.scale.up.nap.pod.zonal.failing.predicates"` | Node auto-provisioning did not provision any node group for the Pod in this zone because of failing predicates. | Name of the considered zone and reasons why predicates failed. | Review the pending Pod's requirements, such as affinity rules, taints, tolerations, or resource requirements.  
  
### ScaleDown errors

You can find error event messages for `scaleDown` events in the corresponding `eventResult` event, in the `resultInfo.results[].errorMsg` field.

Event message | Details | Parameter | Mitigation  
---|---|---|---  
`"scale.down.error.failed.to.mark.to.be.deleted"` | A node couldn't be marked for deletion. | Failing node name. | This message should be transient. If it persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
`"scale.down.error.failed.to.evict.pods"` | Cluster autoscaler can't scale down because some of the Pods couldn't be evicted from a node. | Failing node name. | Review the PodDisruptionBudget for the Pod and make sure the rules allow for eviction of application replicas when acceptable. To learn more, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) in the Kubernetes documentation.  
`"scale.down.error.failed.to.delete.node.min.size.reached"` | Cluster autoscaler can't scale down because a node couldn't be deleted due to the cluster already being at minimal size. | Failing node name. | Review the minimum value set for node pool autoscaling and [adjust the settings](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#resizing_a_node_pool) as necessary. To learn more, see the [Error: Nodes in the cluster have reached minimum size](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#nodes-minimum-size).  
  
### Reasons for a noScaleDown event

A `noScaleDown` event is periodically emitted when there are nodes which are blocked from being deleted by cluster autoscaler. `noScaleDown` events are best-effort, and don't cover all possible cases.

#### NoScaleDown top-level reasons

Top-level reason messages for `noScaleDown` events appear in the `noDecisionStatus.noScaleDown.reason` field. The message contains a top-level reason why cluster autoscaler can't scale the cluster down.

Event message | Details | Mitigation  
---|---|---  
`"no.scale.down.in.backoff"` | Cluster autoscaler can't scale down because scaling down is in a backoff period (temporarily blocked). | This message should be transient, and can occur when there has been a recent scale up event. If the message persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.  
`"no.scale.down.in.progress"` | Cluster autoscaler can't scale down because a previous scale down was still in progress. | This message should be transient, as the Pod will eventually be removed. If this message occurs frequently, review the termination grace period for the Pods blocking scale down. To speed up the resolution, you can also delete the Pod if it's no longer needed.  
  
#### NoScaleDown node-level reasons

Node-level reason messages for `noScaleDown` events appear in the `noDecisionStatus.noScaleDown.nodes[].reason field`. The message contains a reason why cluster autoscaler can't remove a particular node.

Event message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.down.node.scale.down.disabled.annotation"` | Cluster autoscaler can't remove a node from the node pool because the node is annotated with `cluster-autoscaler.kubernetes.io/scale-down-disabled: true`.  | N/A | Cluster autoscaler skips nodes with this annotation without considering their utilization and this message is logged regardless of the node's utilization factor. If you want cluster autoscaler to scale down these nodes, remove the annotation.  
`"no.scale.down.node.node.group.min.size.reached"` |  Cluster autoscaler can't scale down when node group size has exceeded minimum size limit.  This happens because removing nodes would violate the cluster-wide minimal resource limits defined in your node auto-provisioning settings. | N/A | Review the minimum value set for node pool autoscaling. If you want cluster autoscaler to scale down this node, [adjust the minimum value](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#resizing_a_node_pool).  
`"no.scale.down.node.minimal.resource.limits.exceeded"` | Cluster autoscaler can't scale down nodes because it would violate cluster-wide minimal resource limits. These are the resource limits set for node auto-provisioning. | N/A | Review your limits for memory and vCPU and, if you want cluster autoscaler to scale down this node, decrease[ the limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable).  
`"no.scale.down.node.no.place.to.move.pods"` | Cluster autoscaler can't scale down because there's no place to move Pods. | N/A | If you expect that the Pod should be rescheduled, review the scheduling requirements of the Pods on the underutilized node to determine if they can be moved to another node in the cluster. To learn more, see the [Error: No place to move Pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#no-place-to-move-pods).  
`"no.scale.down.node.pod.not.backed.by.controller"` | Pod is blocking scale down because it's not backed by a controller. Specifically, the cluster autoscaler is unable to scale down an underutilized node due to a Pod that lacks a recognized controller. Allowable controllers include ReplicationController, DaemonSet, Job, StatefulSet, or ReplicaSet. | Name of the blocking Pod. | Set the annotation `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` for the Pod or define an acceptable controller.  
`"no.scale.down.node.pod.not.safe.to.evict.annotation"` | A Pod on the node has the `safe-to-evict=false` annotation. | Name of the blocking Pod. | If the Pod can be safely evicted, edit the manifest of the Pod and update the annotation to `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`.  
`"no.scale.down.node.pod.kube.system.unmovable"` | Pod is blocking scale down because it's a non-DaemonSet, non-mirrored, Pod without a PodDisruptionBudget in the `kube-system` namespace. | Name of the blocking Pod. | In GKE versions earlier than 1.32.4-gke.1236000, the cluster autoscaler doesn't remove Pods in the `kube-system` namespace. Starting with version 1.32.4-gke.1236000, the cluster autoscaler considers these Pods for removal after they have been created for one hour. To resolve this issue, either add a PodDisruptionBudget for the `kube-system` Pods or use a combination of node pools taints and tolerations to separate `kube-system` Pods from your application Pods. To learn more, see [Error: kube-system Pod unmoveable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#kube-system-unmoveable).  
`"no.scale.down.node.pod.not.enough.pdb"` | Pod is blocking scale down because it doesn't have enough PodDisruptionBudget. | Name of the blocking Pod. | Review the PodDisruptionBudget for the Pod and consider making it less restrictive. To learn more, see [Error: Not enough PodDisruptionBudget](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#not-enough-pdb).  
`"no.scale.down.node.pod.controller.not.found"` | Pod is blocking scale down because its controller (for example, a Deployment or ReplicaSet) can't be found. | N/A | To determine what actions were taken that left the Pod running after its controller was removed, review the logs. To resolve this issue, manually delete the Pod.  
`"no.scale.down.node.pod.unexpected.error"` | Pod is blocking scale down because of an unexpected error. | N/A | The root cause of this error is unknown. [Contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
## What's next

  * [Learn more about cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * [Learn about how to use node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * [Troubleshoot cluster autoscaler not scaling down](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down).
  * [Troubleshoot cluster autoscaler not scaling up](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up).
  * [Watch a YouTube video about troubleshooting and resolving scaling issues](https://www.youtube.com/watch?v=IdCjKUZah-Q).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
