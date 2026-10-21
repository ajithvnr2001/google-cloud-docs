---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots/
title: Restore a workload from a Pod snapshot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:12.559108+00:00
---

# Restore a workload from a Pod snapshot  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Restore a workload from a Pod snapshot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Learn how to restore a workload from a saved Pod snapshot, manage your existing snapshots, and disable Google Kubernetes Engine (GKE) Pod snapshots.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Make sure you have prepared your environment and triggered a snapshot of your workload. For more information, see the following: 
    * [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare)
    * [Trigger a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger)



## Manage snapshots

When you create a Pod snapshot, a PodSnapshot custom resource is created to store the Pod's state at that time. The `status` field of this resource indicates if the snapshot operation succeeded and if the snapshot is available for restores.

To view all PodSnapshot resources in a namespace, run the following command:
    
    
    kubectl get podsnapshots.podsnapshot.gke.io --namespace NAMESPACE
    

The output resembles the following:
    
    
    NAME                                   STATUS                  POLICY           AGE
    de334898-1e7a-4cdb-9f2e-7cc2181c29e4   AllSnapshotsAvailable   example-policy   47h
    

## Restore a workload from a snapshot

To restore your workload from the latest snapshot, you can delete the existing Pod after a snapshot is taken, and then re-deploy the Pod. Alternatively, you can deploy a new Pod with an identical specification. GKE automatically restores the Pod from the matching snapshot.

The following steps show how a Pod is restored from a matching snapshot by deleting and re-deploying the Pod:

  1. Delete the Pod:
         
         kubectl delete -f POD_NAME.yaml
         

Replace `POD_NAME` with the name of your Pod, for example `my-app`.

  2. Re-apply the Pod:
         
         kubectl apply -f POD_NAME.yaml
         

  3. View the logs to confirm snapshot restore:
         
         kubectl logs my-app --namespace NAMESPACE
         

The output depends on how you've configured your application. In the [example Python application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger#trigger-snapshot-workload), the logs show `GKE Pod Snapshot: restore` when a restore operation occurs.




## Restore from a specific snapshot

By default, GKE restores workloads from the most recent PodSnapshot resource that matches the Pod. When a snapshot is taken, GKE auto-generates a unique name (UUID) for the PodSnapshot resource, which you can view by running `kubectl get podsnapshots.podsnapshot.gke.io --namespace NAMESPACE`.

To restore a workload from an older or specific PodSnapshot resource, add the `podsnapshot.gke.io/ps-name` annotation to your workload Pod specification, specifying the name of the PodSnapshot resource to use for restoring the workload:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-app
      namespace: NAMESPACE
      labels:
        app: my-app
      annotations:
        podsnapshot.gke.io/ps-name: "POD_SNAPSHOT_NAME"
    spec:
      serviceAccountName: KSA_NAME
      runtimeClassName: gvisor
      containers:
      ...
    

Replace the following:

  * `POD_SNAPSHOT_NAME`: the name of the snapshot that you want to restore from. You can get snapshot names by running the `kubectl get podsnapshots.podsnapshot.gke.io --namespace NAMESPACE` command.
  * `NAMESPACE`: the namespace for your Pod.
  * `KSA_NAME`: the name of your KSA.



For GKE to use the specified snapshot for restore, the PodSnapshot resource status condition must be `Ready` and exist in the same namespace as the Pod. If the PodSnapshot isn't `Ready` or doesn't exist in the same namespace as the Pod, the workload performs a cold start instead of restoring from a snapshot.

## Snapshot matching and compatibility

When GKE restores a Pod from a snapshot, it must determine which snapshot is compatible. Compatibility is determined by rules such as the selection order, match criteria (based on the `whole-pod` versus `rootfs-only` scope), and grouping rules matching.

For a detailed reference on matching requirements, compatibility criteria, and the spec fields that influence compatibility, see [Pod snapshot matching and compatibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots#snapshot-matching).

## Disable snapshots

Removing the PodSnapshotPolicy CRD prevents Pods from being snapshotted and restored. Running Pods are unaffected by the resource deletion. However, if you delete the policy while a Pod is being saved or restored, the Pod might enter a failed state.

To disable snapshotting and restoration for new Pods governed by a policy, delete the `PodSnapshotPolicy` by running the following command:
    
    
    kubectl delete podsnapshotpolicies.podsnapshot.gke.io SNAPSHOT_POLICY --namespace=NAMESPACE
    

Replace SNAPSHOT_POLICY with the name of the `PodSnapshotPolicy` that you want to delete, for example `example-pod-snapshot-policy`.

You can also delete a specific PodSnapshot resource so that Pods are no longer restored from that specific snapshot. Deleting the PodSnapshot resource also removes the files stored in Cloud Storage.

To prevent a specific snapshot from being used for future restorations, delete the PodSnapshot object by running the following command:
    
    
    kubectl delete podsnapshots.podsnapshot.gke.io POD_SNAPSHOT_NAME --namespace=NAMESPACE
    

Replace `POD_SNAPSHOT_NAME` with the name of the snapshot that you want to delete, for example `example-podsnapshot`.

## What's next

Learn how to [Troubleshoot Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/pod-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
