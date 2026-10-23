---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger/
title: Trigger a Pod snapshot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:05.504467+00:00
---

# Trigger a Pod snapshot  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Trigger a Pod snapshot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

To reduce startup latency for Google Kubernetes Engine (GKE) workloads, you can take a snapshot of a running Pod and restore new Pods from it. This document shows you how to create a Pod snapshot policy and trigger a snapshot, either from your workload or manually. For more information about how Pod snapshots work, see [About GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots).

Platform admins and operators and Application developers can use this document to configure snapshot policies and trigger snapshots. For more information about the common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Complete the prerequisites and enable Pod snapshots on your cluster. For more information about preparing your cluster and storage, see [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare).



## Create a snapshot policy

To enable snapshots for a Pod, create a PodSnapshotPolicy custom resource with a selector that matches the Pod's labels:

  1. Save the following manifest as `example-pod-snapshot-policy.yaml`. This example creates a policy that applies to Pods with the `app: my-app` label. The policy uses the `example-pod-snapshot-storage-config` PodSnapshotStorageConfig custom resource, which you created in [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare), to define the snapshot storage location:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotPolicy
         metadata:
           name: example-pod-snapshot-policy
           namespace: NAMESPACE
         spec:
           storageConfigName: example-pod-snapshot-storage-config
           selector:
             matchLabels:
               app: my-app
           triggerConfig:
             type: TRIGGER_TYPE
             postCheckpoint: resume
         

Replace the following:

     * `NAMESPACE`: the namespace for your Pods. Use the same namespace that you granted Cloud Storage access to in [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare).
     * `TRIGGER_TYPE`: the type of trigger. Supported values are `workload` for workload-based triggers or `manual` for on-demand snapshots.

In this example, the `postCheckpoint: resume` setting keeps the Pod running after GKE takes the snapshot.

For a complete list of the fields that you can configure, see the [PodSnapshotPolicy specification](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/podsnapshot#podsnapshotpolicy).

  2. Apply the manifest:
         
         kubectl apply -f example-pod-snapshot-policy.yaml
         




## Configure additional Pod snapshot policy settings

Your PodSnapshotPolicy custom resource also supports optional settings beyond the required selector, storage configuration, and trigger. These additional settings control what each snapshot captures, how long GKE keeps snapshots, and how GKE groups snapshots for restores:

  * **Snapshot scope** : to specify which parts of the Pod state to capture in the snapshot, configure the `spec.snapshotScope` field. Supported values are `whole-pod` (default) and `rootfs-only`. The `whole-pod` scope captures the entire Pod, including application state, memory, and file systems. The `rootfs-only` scope captures only the container root file system. The `rootfs-only` scope requires GKE version 1.35.3-gke.1031000 or later.

  * **Automatic cleanup** : to automatically clean up old PodSnapshot custom resources, configure a retention policy by using the `spec.retentionConfig` field. You can specify a duration by using the `lastAccessTimeout` field—for example, `7d`. After this duration elapses, GKE deletes the snapshot.

  * **Snapshot grouping** : to isolate snapshots taken in similar environments but in different contexts, specify grouping labels in the `spec.snapshotGroupingRules` field. For example, in a multi-tenant scenario where the base Pod is the same for all users, you can isolate the snapshots by user or group. During a restore, GKE selects a snapshot only from the same label group. For more information about how this grouping affects compatibility matching during restoration, see [Grouping rules matching](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots#grouping-rules-matching).




You can configure the snapshot scope, retention, and grouping settings independently. The following example shows all three settings in a PodSnapshotPolicy custom resource:
    
    
    # Multiple lines are omitted here
    spec:
      snapshotScope: rootfs-only
      retentionConfig:
        lastAccessTimeout: 7d
      snapshotGroupingRules:
        groupByLabelValue:
          labels: ["tenant", "environment"]
          groupRetentionPolicy:
            maxSnapshotCountPerGroup: 5
    

For a complete list of the fields that you can configure, see the [PodSnapshotPolicy specification](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/podsnapshot#podsnapshotpolicy).

## Optimize snapshot size

Larger snapshots take longer to save and restore. Before you trigger a snapshot, reduce its size by deleting any temporary files or application state that your application doesn't need after GKE restores the Pod from the snapshot.

With the default `whole-pod` snapshot scope, GKE Sandbox captures the entire state of all containers, including the following:

  * Application state, such as memory and registers
  * Changes to the root file system and `tmpfs` mounts (including `emptyDir` volumes)
  * Kernel state, such as open file descriptors, threads, and sockets



Optimizing snapshot size is particularly important for workloads like large language models (LLMs). LLM servers often download model weights into local storage (`rootfs` or `tmpfs`) before loading them into the GPU. When you take a snapshot, GKE Sandbox saves both the GPU state and the model weight files. In this scenario, if the model is 100 GB, then the resulting snapshot is approximately 200 GB (100 GB of model files, plus 100 GB representing the GPU state). After the application loads the model weights into the GPU, it often doesn't need the files on the file system to run. By deleting these model files before you trigger the snapshot, you can reduce the snapshot size by half and restore the application with significantly lower latency.

## Trigger a snapshot

Choose one of the following methods to trigger a snapshot:

  * **Workload trigger** : use this method when you can modify your application to signal that it's ready for a snapshot—for example, after initialization completes. This method is best for improving the startup latency of horizontally scaling workloads. A workload trigger runs only once in a workload cycle.

  * **Manual trigger** : use this method when you can't modify your application to signal readiness, or when you want on-demand snapshots of a specific Pod. You can create a manual trigger as many times as you need.




### Trigger a snapshot from a workload

To trigger a snapshot from within your application code, configure your application to send a signal when it's ready for a snapshot. To signal readiness, write the value `1` to the `/proc/gvisor/checkpoint` file—for example, by running the `echo 1 > /proc/gvisor/checkpoint` command. The write operation starts the snapshot process asynchronously and returns immediately. Reading from the same file descriptor blocks the reading process until the snapshot or restore operation completes and the workload is ready to resume.

Before you trigger a snapshot from a workload, make sure that a snapshot policy selects the Pod. The value of the `triggerConfig.type` field in that policy must be set to `workload`.

The exact usage varies depending on your application, but the following example shows a snapshot trigger for a Python application. To trigger a snapshot from this example workload, follow these steps:

  1. Save the following manifest as `my-app.yaml`. In this example, the `app: my-app` label matches the selector in the example snapshot policy, and the `runtimeClassName: gvisor` setting runs the Pod in GKE Sandbox:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-app
           namespace: NAMESPACE
           labels:
             app: my-app
         spec:
           serviceAccountName: SERVICEACCOUNT_NAME
           runtimeClassName: gvisor
           containers:
           - name: my-container
             image: python:3.10-slim
             command: ["python3", "-c"]
             args:
               - |
                 import time
                 def trigger_snapshot():
                   try:
                     with open("/proc/gvisor/checkpoint", "r+") as f:
                       f.write("1")
                       res = f.read().rstrip()
                       print(f"GKE Pod Snapshot: {res}")
                   except FileNotFoundError:
                     print("GKE Pod Snapshot file does not exist -- "
                           "Pod Snapshots is disabled")
                     return
                 i = 0
                 while True:
                   print(f"Count: {i}", flush=True)
                   if (i == 20): # Simulate readiness at the 20th count
                     trigger_snapshot()
                   i += 1
                   time.sleep(1)
             resources:
               limits:
                 cpu: "500m"
                 memory: "512Mi"
               requests:
                 cpu: "250m"
                 memory: "256Mi"
         

Replace the following:

     * `NAMESPACE`: the namespace for your Pods.
     * `SERVICEACCOUNT_NAME`: the name of the ServiceAccount object that you granted Cloud Storage access to in [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare).
  2. Deploy the application:
         
         kubectl apply -f my-app.yaml
         

After the application starts and signals that it's ready, GKE Sandbox takes the snapshot. To confirm that the snapshot succeeded, see Verify snapshots.




### Trigger a snapshot manually

Before you manually trigger a snapshot, make sure that the target Pod is running and that a snapshot policy selects the Pod. The value of the `triggerConfig.type` field in that policy must be set to `manual`.

To manually trigger an on-demand snapshot for a specific Pod, create a PodSnapshotManualTrigger custom resource by following these steps:

  1. Save the following manifest as `example-manual-trigger.yaml`. This example triggers a snapshot for a Pod named `my-pod`:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotManualTrigger
         metadata:
           name: example-manual-trigger
           namespace: NAMESPACE
         spec:
           targetPod: my-pod
         

Replace `NAMESPACE` with the namespace for your Pods.

  2. Apply the manifest:
         
         kubectl apply -f example-manual-trigger.yaml
         

  3. To confirm that the snapshot triggered successfully, check the `status` section of the PodSnapshotManualTrigger custom resource:
         
         kubectl get podsnapshotmanualtriggers.podsnapshot.gke.io \
             example-manual-trigger \
             --namespace NAMESPACE -o yaml
         

Replace `NAMESPACE` with the namespace for your Pods.

If the trigger succeeded, then the `status.conditions` field shows that the checkpoint completed and the `status.snapshotCreated` field shows the name of the created PodSnapshot custom resource.




## Verify snapshots

To confirm that GKE took a snapshot, check the event history for `GKEPodSnapshotting` events:
    
    
    kubectl get events \
        -o custom-columns=NAME:involvedObject.name,CREATIONTIME:.metadata.creationTimestamp,REASON:.reason,MESSAGE:.message \
        --namespace NAMESPACE \
        --field-selector involvedObject.name=POD_NAME,reason=GKEPodSnapshotting
    

Replace the following:

  * `NAMESPACE`: the namespace for your Pods.
  * `POD_NAME`: the name of your Pod.



The output is similar to the following:
    
    
    NAME                                    CREATIONTIME           REASON               MESSAGE
    default/5b449f9c7c-bd7pc                2025-11-05T16:25:11Z   GKEPodSnapshotting   Successfully checkpointed the pod to PodSnapshot
    

The `MESSAGE` column shows `Successfully checkpointed the pod to PodSnapshot`, which confirms that GKE saved the Pod state to a PodSnapshot custom resource. To view and manage your PodSnapshot custom resources, see [Manage snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots#manage-snapshots).

## What's next

  * [Restore a workload from a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots)
  * [Troubleshoot Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/pod-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
