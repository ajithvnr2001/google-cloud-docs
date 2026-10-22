---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/pod-snapshots/
title: Troubleshoot Pod snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:20.185011+00:00
---

# Troubleshoot Pod snapshots  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/pod-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot Pod snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to resolve common issues with `GKE` Pod snapshots and its associated resources.

This information is important for the Application developers and Platform admins and operators who use Pod snapshots to checkpoint and restore workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Post-checkpoint mutation risks with PVCs

If your Pod uses a Persistent Volume Claim (PVC), a significant risk occurs during the "checkpoint and resume" workflow: if you configure a workload to resume immediately after a checkpoint (by using the `postCheckpoint: resume` field), the application remains active and can modify the PVC after the checkpoint.

  * **Graceful shutdown issue** : after the checkpoint and resume cycle, when you delete a Pod, Kubernetes initiates a graceful shutdown sequence by sending a `SIGTERM` signal to the main process in the container. Many applications implement graceful shutdown logic during which they might trigger cleanup routines to delete or update temporary files on the PVC.
  * **Restore failure** : if these changes occur on the PVC after the Pod snapshot is taken, the restore procedure will expect the PVC state as it existed at the exact moment of the checkpoint, leading to potential restore failures or data inconsistency.
  * **Recommended mitigation** : if using a PVC is necessary for the workload, don't resume the workload after a checkpoint. Use the configuration `postCheckpoint: stop` in your `PodSnapshotPolicy`. This configuration helps to ensure that the process does not have the opportunity to perform auxiliary writes or state changes after the checkpointing phase completes.



## ConfigMap mounts and directory masking

When integrating configuration data into a container, the mounting method can impact the integrity of a snapshot.

If a ConfigMap is mounted by using a standard volume mount, Kubernetes treats the entire target directory as an external mount. Because external mounts are skipped during snapshots, the entire directory is excluded from the snapshot.

In the following example, any changes in the `/etc/my-app/` directory aren't captured in the snapshot because the entire directory is an external mount:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: my-config
    data:
      config.json: |
        {
          "mode": "local"
        }
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-app
    spec:
      runtimeClassName: gvisor
      containers:
        - name: my-app-container
          image: my-app-image
          volumeMounts:
            - mountPath: /etc/my-app
              name: config-volume
      volumes:
        - name: config-volume
          configMap:
            name: my-config
    

To resolve this issue, use a `subPath`. A `subPath` helps to ensure that only the specific configuration file is treated as an external mount. This configuration targets the exact file, which lets the remaining files and structure within the parent directory remain part of the container's local file system, which is properly captured during the checkpointing process.

The following example shows the `volumeMounts` configuration that uses a `subPath`:
    
    
          volumeMounts:
            - mountPath: /etc/my-app/config.json
              name: config-volume
              subPath: config.json
    

## Implicit anonymous volumes

Certain container images define volumes within their metadata through the `VOLUME` instruction in the Dockerfile. Even if your Pod specification doesn't define a volume, Kubernetes automatically creates an anonymous volume for any path defined as a volume in the base image. For example, the `alpine/git` image defines `/git` as an implicit volume.

These anonymous volumes are treated as external mounts and, like PVCs, are not checkpointed. Check your base images to ensure that critical data is not stored in implicit volumes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
