---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events/
title: Troubleshoot OOM events \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:05:39.816120+00:00
---

# Troubleshoot OOM events  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot OOM events Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If your Google Kubernetes Engine (GKE) apps are experiencing unexpected container terminations, instability, or `CrashLoopBackOff` errors, it might be due to Out of Memory (OOM) events. OOM events occur when a container or node runs out of memory, causing the Linux OOM Killer to terminate processes to reclaim resources.

Use this page to identify whether an OOM event occurred at the container level or the node level, and apply effective mitigation strategies to prevent a recurrence.

This information is important for Application developers who need to ensure that their applications are configured with appropriate memory requests and limits and are free of memory leaks. It's also important for Platform admins and operators who monitor node resource utilization and ensure that the cluster has adequate memory capacity to support the deployed workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Common causes of OOM events

OOM events typically occur during load or traffic spikes, where app memory usage surges and reaches the memory limit configured for the container.

The following scenarios can cause an OOM event:

  * **Insufficient memory limit** : the `resources.limits.memory` setting in the manifest of the Pod is too low for the app's typical or peak memory demands.
  * **Undefined memory requests or limits** : if both `resources.limits.memory` and `resources.requests.memory` aren't defined, the container's memory usage is unbounded.
  * **High or spiky load** : sudden, extreme spikes in load can overwhelm a system's resources, including memory, even if limits are usually adequate.
  * **Memory leak** : the app might have a code defect that causes it to fail to release memory properly.



OOM events can initiate a cascading failure, because fewer containers remain to handle the traffic, increasing the load on the remaining containers. These containers might then also be terminated.

## How Kubernetes handles OOM events

The Linux OOM Killer handles every OOM event. The OOM Killer is a kernel process that activates when the system is critically low on memory. Its purpose is to prevent a total system crash by strategically terminating processes to free up resources. The kernel uses a scoring system to select which process to stop, aiming to preserve system stability and minimize data loss.

In a Kubernetes environment, the OOM Killer operates at two different scopes: the control group (cgroup), which affects one container; and the system, which affects the entire node.

### Container-level OOM kill

A container-level OOM kill occurs when a container attempts to exceed its predefined memory limit. Kubernetes assigns each container to a specific cgroup with a hard memory limit. When a container's memory usage reaches this limit, the kernel first tries to reclaim memory within that cgroup. If the kernel cannot reclaim enough memory by using this process, the cgroup OOM Killer is invoked. It terminates processes within that specific cgroup to enforce the resource boundary.

When the main process in a container is terminated this way, Kubernetes observes the event and marks the container's status as `OOMKilled`. The Pod's configured `restartPolicy` then dictates the outcome:

  * `Always` or `OnFailure`: the container is restarted.
  * `Never`: the container isn't restarted and remains in a terminated state.



By isolating the failure to the offending container, the OOM Killer prevents a single faulty Pod from crashing the entire node.

#### How cgroup version affects OOM Killer behavior

OOM kill behavior can differ significantly between cgroup versions. If you're not sure which cgroup version you use, [check the cgroup mode of cluster nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#check-cgroup-mode).

  * In `cgroup v1`, an OOM event within a container's memory cgroup can lead to unpredictable behavior. The OOM Killer might terminate any process within that cgroup, including child processes that are not the container's main process (PID 1).

This behavior presents a significant challenge for Kubernetes. Because Kubernetes primarily monitors the health of the main container process, it remains unaware of these "partial" OOM kills. The main container process might continue to run, even if critical child processes have been terminated. This behavior can result in subtle app failures that aren't immediately visible to Kubernetes or to operators, but are still visible in the node's system journal (`journalctl`).

  * `cgroup v2` offers more predictable OOM Killer behavior.

To help guarantee workload integrity in a cgroup v2 environment, the OOM killer prevents partial kills and ensures one of two outcomes: either _all tasks_ belonging to that cgroup and its descendants are terminated (making the failure visible to Kubernetes), or when the workload has no tasks using too much memory, the workload is left untouched and it continues to run without unexpected internal process terminations.

For scenarios where you want the `cgroup v1` behavior of terminating a single process, the kubelet provides the `singleProcessOOMKill` flag for `cgroup v2`. This flag gives you more granular control, enabling the termination of individual processes during an OOM event, rather than the entire cgroup.




### System-level OOM kill

A system-level OOM kill is a more serious event that occurs when the entire node, not just a single container, runs out of available memory. This event can happen if the combined memory usage of all processes (including all Pods and system daemons) exceeds the node's capacity.

When this node runs out of memory, the global OOM Killer assesses all processes on the node and terminates a process to reclaim memory for the entire system. The selected process is usually one that is short-lived and uses a large amount of memory.

To prevent severe OOM situations, Kubernetes uses [node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) to manage node resources. This process involves evicting less critical Pods from a node when resources, such as memory or disk space, become critically low. A system-level OOM kill indicates that this eviction process couldn't free up memory fast enough to prevent the issue.

If the OOM Killer terminates a container's process, the effect is usually identical to a cgroup-triggered kill: the container is marked `OOMKilled` and restarted based on its policy. However, if a critical system process is killed (which is rare), the node itself could become unstable.

## Investigate OOM events

The following sections help you detect and confirm an OOM event, starting with the simplest Kubernetes tools and moving to more detailed log analysis.

**Note:** Don't rely solely on memory utilization metrics from monitoring tools. These metrics are collected at intervals and often miss the rapid spike that triggers an OOM kill.

### Check the Pod status for visible OOM events

The first step in confirming an OOM event is to check if Kubernetes observed the OOM event. Kubernetes observes the event when the container's main process is killed, which is standard behavior in `cgroup v2` environments.

  * Inspect the Pod's status:
        
        kubectl describe pod POD_NAME
        

Replace `POD_NAME` with the name of the Pod that you want to investigate.

If a visible OOM event occurred, the output is similar to the following:
        
        ...
          Last State:     Terminated
            Reason:       OOMKilled
            Exit Code:    137
            Started:      Tue, 13 May 2025 19:05:28 +0000
            Finished:     Tue, 13 May 2025 19:05:30 +0000
        ...
        




If you see `OOMKilled` in the `Reason` field, you have confirmed the event. An `Exit Code` of `137` also indicates an OOM kill. If the `Reason` field has a different value, or the Pod is still running despite app errors, proceed to the next section for further investigation.

### Search logs for invisible OOM events

An OOM kill is "invisible" to Kubernetes if a child process is killed but the main container process continues to run (a common scenario in `cgroup v1` environments). You must search the node's logs to find evidence of these events.

To find invisible OOM kills, use Logs Explorer:

  1. In the Google Cloud console, go to Logs Explorer.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter one of the following queries:

     * If you already have a Pod that you think experienced an OOM event, query that specific Pod:
           
           resource.type="k8s_node"
           jsonPayload.MESSAGE:(("POD_NAME" AND "ContainerDied") OR "TaskOOM event")
           resource.labels.cluster_name="CLUSTER_NAME"
           

Replace the following:

       * `POD_NAME`: the name of the Pod that you want to query.
       * `CLUSTER_NAME`: the name of the cluster to which the Pod belongs.
     * To discover which Pods or nodes experienced an OOM event, query all GKE workloads:
           
           resource.type="k8s_node"
           jsonPayload.MESSAGE:("ContainerDied" OR "TaskOOM event")
           resource.labels.cluster_name="CLUSTER_NAME"
           

  3. Click **Run query**.

  4. In the output, locate OOM events by searching for log entries containing the string `TaskOOM`.

  5. Optional: if you searched for OOM events for all GKE workloads and want to identify the specific Pod that experienced the OOM events, complete the following steps:

     1. For each event, make a note of the container ID that's associated with it.
     2. Identify container stoppages by looking for log entries containing the string `ContainerDied`, and that occurred shortly after the OOM events. Match the container ID from the OOM event to the corresponding `ContainerDied` line.

**Note:** `ContainerDied` lines without a corresponding `TaskOOM` line (sharing the same container ID) indicate that the container terminated for reasons other than OOMs. You can rule out OOM as a cause for these containers and investigate alternative possibilities. For example, the container could have crashed due to a bug such as an unhandled exception or the failure of a container liveness probe. In those cases, Kubernetes restarts the container, resulting in a `ContainerDied` event.
     3. After you match the `container IDs`, the `ContainerDied` line typically includes the Pod name associated with the failed container. This Pod was affected by the OOM event.




### Use journalctl for real-time information

If you need to perform real-time analysis of your system, use `journalctl` commands.

  1. Connect to the node by using SSH:
         
         gcloud compute ssh NODE_NAME --location ZONE
         

Replace the following:

     * `NODE_NAME`: the name of the node that you want to examine.
     * `ZONE`: the Compute Engine zone to which your node belongs.
  2. In the shell, explore the kernel messages from the node's system journal:
         
         journalctl -k
         

  3. Analyze the output to distinguish the event type:

     * **Container-level kill** : the log entry contains terms like `memory cgroup`, `mem_cgroup`, or `memcg`, which indicate that a cgroup limit was enforced.
     * **System-level kill** : the log entry is a general message like `Out of memory: Killed process...` without mentioning a cgroup.



## Resolve OOM events

To resolve an OOM event, try the following solutions:

  * **Increase memory limits** : this is the most direct solution. Edit the Pod manifest to provide a higher `resources.limits.memory` value that accommodates the app's peak usage. For more information about setting limits, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the Kubernetes documentation.
  * **Add or adjust memory requests** : in the manifest of the Pod, verify that the `resources.requests.memory` field is set to a realistic value for typical usage. This setting helps Kubernetes schedule the Pod onto a node with sufficient memory.
  * **Horizontally scale the workload** : to distribute traffic load and reduce the memory pressure on any single Pod, [increase the number of replicas](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#scaling_an_application). To have Kubernetes proactively scale the workload, consider [enabling horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * **Vertically scale the nodes** : if many Pods on a node are near their limits, the node itself might be too small. To increase the size of the nodes, [migrate your workloads to a node pool with more memory](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes). To have Kubernetes proactively scale the nodes, consider enabling [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).
  * **Optimize your app** : review your app to identify and resolve memory leaks and optimize code that consumes large amounts of memory during traffic spikes.
  * **Delete problematic workloads** : as a last resort for non-critical workloads, delete the Pod to immediately relieve pressure on the cluster.



## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
