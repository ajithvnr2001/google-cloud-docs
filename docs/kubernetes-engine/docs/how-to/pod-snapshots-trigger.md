---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger/
title: Trigger a Pod snapshot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:12.692313+00:00
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

Learn how to create snapshot policies and trigger a Pod snapshot of your running workloads on Google Kubernetes Engine (GKE).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Make sure you have completed the prerequisites and enabled Pod snapshots on your cluster. For more information, see [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare).



## Create a snapshot policy

To enable snapshots for a Pod, create a PodSnapshotPolicy resource with a selector that matches the Pod's labels.

  1. The following example creates a policy that applies to Pods with the `app: my-app` label and uses the `example-pod-snapshot-storage-config` storage configuration. Save the following manifest as `example-pod-snapshot-policy.yaml`:
         
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

     * `TRIGGER_TYPE`: the type of trigger. Supported values are `workload` for workload-based triggers or `manual` for on-demand snapshots.
     * `NAMESPACE`: the namespace for your Pods.

For a complete list of all fields you can configure, see the [PodSnapshotPolicy CustomResourceDefinition (CRD) documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/podsnapshot#podsnapshotpolicy).

  2. Apply the manifest:
         
         kubectl apply -f example-pod-snapshot-policy.yaml
         




## Configure additional Pod snapshot policies

You can configure additional policies in your PodSnapshotPolicy, such as the following:

  * **Snapshot scope** : to specify which parts of the Pod state to capture in the snapshot, configure the `spec.snapshotScope` field. Supported values are `whole-pod` (default) to checkpoint the entire Pod including application state, memory, and file systems, or `rootfs-only` to checkpoint only the container root file system. The `rootfs-only` scope requires GKE version 1.35.3-gke.1031000 or later.

  * **Automatic clean-up** : to automatically clean up old Pod snapshot resources, configure a retention policy by using the `spec.retentionConfig` field. You can specify a duration by using the `lastAccessTimeout` field (for example, `7d`), after which time, the snapshot is deleted.

  * **Organize snapshots** : you can group snapshots logically to differentiate among snapshots that were taken in similar environments, but in different contexts. For example, in a multi-tenant scenario where the base Pod is the same for all users, you could isolate the snapshots by user or group. To isolate snapshots, specify grouping labels in the policy by using the `snapshotGroupingRules` field. When a Pod is restored, it only matches against snapshots within the same label group. For more information about how this grouping affects compatibility matching during restoration, see [Grouping rules matching](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots#snapshot-matching).




The following example shows how to configure both the retention and grouping settings in your PodSnapshotPolicy. These settings can be set independently:
    
    
    # ... other fields omitted
    spec:
      snapshotScope: rootfs-only
      retentionConfig:
        lastAccessTimeout: 7d
      snapshotGroupingRules:
        groupByLabelValue:
          labels: ["tenant", "environment"]
          groupRetentionPolicy:
            maxSnapshotCountPerGroup: 5
    

For a complete list of all fields you can configure, see the [PodSnapshotPolicy reference documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/podsnapshot#podsnapshotpolicy).

## Optimize snapshot size

When a Pod snapshot is triggered, gVisor captures the entire state of all containers, including:

  * Application state, such as memory and registers
  * Changes to the root file system and `tmpfs` (including `emptyDir` volumes)
  * Kernel state, such as open file descriptors, threads, and sockets



The size of the snapshot is determined by these factors. Larger snapshots take longer to save and restore. To optimize performance, before triggering a snapshot, you should clean up any application state or files that aren't required after the Pod is restored from the snapshot.

Optimizing snapshot size is particularly important for workloads like large language models (LLMs). LLM servers often download model weights into local storage (`rootfs` or `tmpfs`) before loading them into the GPU. When a snapshot is taken, both the GPU state and the model weight files are saved. In this scenario, if the model is 100 GB, the resulting snapshot is roughly 200 GB (100 GB of model files, plus 100 GB representing the GPU state). After the model weights are loaded into the GPU, the files on the file system are often not needed for the application to run. By deleting these model files before you trigger the snapshot, you can reduce the snapshot size by half and restore the application with significantly lower latency.

## Trigger a snapshot

You can trigger a snapshot from within a workload when the application is ready, or you can manually trigger an on-demand snapshot for a specific Pod.

### Trigger a snapshot from a workload

To trigger a snapshot from within your application code, configure your application to send a signal when it's ready for a snapshot. To signal readiness, write `1` to the `/proc/gvisor/checkpoint` file, for example `echo 1 > /proc/gvisor/checkpoint`. The write operation starts the snapshot process asynchronously and returns immediately. Reading from the same file descriptor will block the reading process until both the snapshot and restore is complete and the workload is ready to resume.

The exact usage will vary depending on your application, but the following example shows a snapshot trigger for a Python application. To trigger a snapshot from this example workload, complete the following steps:

  1. Save the following manifest as `my-app.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-app
           namespace: NAMESPACE
           labels:
             app: my-app
         spec:
           serviceAccountName: KSA_NAME
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
                     print("GKE Pod Snapshot file does not exist -- Pod Snapshots is disabled")
                     return
                 i = 0
                 while True:
                   print(f"Count: {i}", flush=True)
                   if (i == 20): #simulate the application being ready to snapshot at 20th count
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
     * `KSA_NAME`: the name of your KSA.
  2. Deploy the application:
         
         kubectl apply -f my-app.yaml
         




### Trigger a snapshot manually

To manually trigger an on-demand snapshot for a specific Pod, create a PodSnapshotManualTrigger resource.

  1. The following example triggers a snapshot for a Pod named `my-pod`. Save the following manifest as `example-manual-trigger.yaml`:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotManualTrigger
         metadata:
           name: example-manual-trigger
           namespace: NAMESPACE
         spec:
           targetPod: my-pod
         

Replace `NAMESPACE` with the namespace of your Pod.

**Note:** The snapshot policy that selects this Pod must have the trigger type set to `manual`.
  2. Apply the manifest:
         
         kubectl apply -f example-manual-trigger.yaml
         




To confirm if the snapshot was triggered successfully, check the `status` field of the PodSnapshotManualTrigger resource:
    
    
    kubectl get podsnapshotmanualtriggers.podsnapshot.gke.io example-manual-trigger -n NAMESPACE -o yaml
    

The `status` field indicates if triggering the snapshot succeeded or failed.

## Verify snapshots

You can confirm that a snapshot was taken by checking the event history for `GKEPodSnapshotting` events:
    
    
    kubectl get events -o \
    custom-columns=NAME:involvedObject.name,CREATIONTIME:.metadata.creationTimestamp,REASON:.reason,MESSAGE:.message \
    --namespace NAMESPACE \
    --field-selector involvedObject.name=POD_NAME,reason=GKEPodSnapshotting
    

Replace the following:

  * `POD_NAME`: the name of your Pod, for example `my-app` or `my-pod`.
  * `NAMESPACE`: the namespace for your Pods.



The output resembles the following:
    
    
    NAME                                    CREATIONTIME           REASON               MESSAGE
    default/5b449f9c7c-bd7pc                2025-11-05T16:25:11Z   GKEPodSnapshotting   Successfully checkpointed the pod to PodSnapshot
    

## What's next

Learn how to [restore a workload from a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
