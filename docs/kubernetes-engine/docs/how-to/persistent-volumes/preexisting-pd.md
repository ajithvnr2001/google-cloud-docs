---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd/
title: Using pre-existing persistent disks as PersistentVolumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:43.031441+00:00
---

# Using pre-existing persistent disks as PersistentVolumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Using pre-existing persistent disks as PersistentVolumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can create a [PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) from a pre-existing persistent disk that contains data and attach it to a Pod in your Google Kubernetes Engine (GKE) cluster. This capability is useful for integrating existing data volumes into your Kubernetes workloads or migrating data into GKE. By using this approach, you can run your applications with their necessary data in your selected environment, simplifying data management.

## Overview

There are two common scenarios which use a pre-existing persistent disk.

  * Manually creating a PersistentVolumeClaim and a PersistentVolume, binding them together, and referring to the PersistentVolumeClaim in a Pod specification.
  * Use a StatefulSet to automatically generate PersistentVolumeClaims which are bound to manually generated PersistentVolumes corresponding to a series of pre-existing persistent disks.



The examples in this page use existing [Compute Engine persistent disks](https://docs.cloud.google.com/compute/docs/disks).

While `ext4` is the default filesystem type, you can use a pre-existing persistent disk with the `xfs` filesystem instead as long as your [node image supports it](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#storage_driver_support). To use an `xfs` disk, change `spec.csi.fsType` to `xfs` in the PersistentVolume manifest.

Windows does not support the `ext4` filesystem type. You must use the `NTFS` filesystem for Windows Server node pools. To use an `NTFS` disk, change `spec.csi.fsType` to `NTFS` in the PersistentVolume manifest.

**Note:** If the filesystem type for the persistent disk you use doesn't match the `fsType` you specify in the PersistentVolume manifest, pods you create that consume the volumes will not start, and you will see errors in the Pod description. Similarly, Persistent Disk CSI volumes only support a single partition. Volumes created outside of GKE with multiple partitions cannot be used with this technique.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have existing persistent disks. To provision a disk, see [Provisioning regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd#manual-provisioning).
  * Ensure that your cluster uses the [Compute Engine persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).



## Using a PersistentVolumeClaim bound to the PersistentVolume

For a container to access your pre-existing persistent disk, you'll need to do the following:

  1. Provision the existing persistent disk as a PersistentVolume.
  2. Bind the PersistentVolume to a PersistentVolumeClaim.
  3. Give the containers in the Pod access to the PersistentVolume.



### Create the PersistentVolume and PersistentVolumeClaim

There are several ways to bind a PersistentVolumeClaim to a specific PersistentVolume. For example, the following YAML manifest creates a new PersistentVolume and PersistentVolumeClaim, and then binds the volume to the claim using the `claimRef` defined on the PersistentVolume.

To bind a PersistentVolume to a PersistentVolumeClaim, the `storageClassName` of the two resources must match, as well as `capacity`, `accessModes`, and `volumeMode`. You can omit the `storageClassName`, but you must specify `""` to prevent Kubernetes from using the default StorageClass.

The `storageClassName` does not need to refer to an existing StorageClass object. If all you need is to bind the claim to a volume, you can use any name you want. However, if you need extra functionality configured by a StorageClass, like volume resizing, then `storageClassName` must refer to an existing StorageClass object.

For more details, see the [Kubernetes documentation on PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

**Note:** The persistent disk must be in the same [zone](https://docs.cloud.google.com/compute/docs/regions-zones) as the cluster nodes.

  1. Save the following YAML manifest:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: PV_NAME
         spec:
           storageClassName: "STORAGE_CLASS_NAME"
           capacity:
             storage: DISK_SIZE
           accessModes:
             - ReadWriteOnce
           claimRef:
             name: PV_CLAIM_NAME
             namespace: default
           csi:
             driver: pd.csi.storage.gke.io
             volumeHandle: DISK_ID
             fsType: FS_TYPE
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           namespace: default
           name: PV_CLAIM_NAME
         spec:
           storageClassName: "STORAGE_CLASS_NAME"
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: DISK_SIZE
         

Replace the following:

     * `PV_NAME`: the name of your new PersistentVolume.
     * `STORAGE_CLASS_NAME`: the name of your new StorageClass.
     * `DISK_SIZE`: the size of your pre-existing persistent disk. For example, `500G`.
     * `PV_CLAIM_NAME`: the name of your new PersistentVolumeClaim.
     * `DISK_ID`: the identifier of your pre-existing persistent disk. The format is `projects/{project_id}/zones/{zone_name}/disks/{disk_name}` for [Zonal persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#pd-zones), or `projects/{project_id}/regions/{region_name}/disks/{disk_name}` for [Regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#regional_persistent_disks).
     * `FS_TYPE`: the filesystem type. You can leave this as the default (`ext4`), or use `xfs`. If your clusters use a Windows Server node pool, you must change this to `NTFS`.
  2. To apply the configuration and create the PersistentVolume and PersistentVolumeClaim resources, run the following command:
         
         kubectl apply -f FILE_PATH
         

Replace `FILE_PATH` with the path to the YAML file.




### Use the PersistentVolume in a Pod

After you create and bind the PersistentVolume and PersistentVolumeClaim, you can give a Pod's containers access to the volume by specifying values in the `volumeMounts` field.

The following YAML configuration creates a new Pod and a container running an `nginx` image, and then mounts the PersistentVolume on the Pod:
    
    
    kind: Pod
    apiVersion: v1
    metadata:
      name: POD_NAME
    spec:
      **volumes :
        - name: VOLUME_NAME
          persistentVolumeClaim:
            claimName: PV_CLAIM_NAME**
      containers:
        - name: CONTAINER_NAME
          image: nginx
          ports:
            - containerPort: 80
              name: "http-server"
          **volumeMounts :
            - mountPath: "/usr/share/nginx/html"
              name: VOLUME_NAME**
    

Replace the following:

  * `POD_NAME`: the name of your new Pod.
  * `VOLUME_NAME`: the name of the volume.
  * `PV_CLAIM_NAME`: the name of the PersistentVolumeClaim you created in the previous step.
  * `CONTAINER_NAME`: the name of your new container.



Apply the configuration:
    
    
    kubectl apply -f FILE_PATH
    

Replace `FILE_PATH` with the path to the YAML file.

To verify that the volume was mounted, run the following command:
    
    
    kubectl describe pods POD_NAME
    

In the output, check that the PersistentVolumeClaim was mounted:
    
    
    ...
    Volumes:
      VOLUME_NAME:
        Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
        ClaimName:  PV_CLAIM_NAME
        ReadOnly:   false
    Events:
      Type    Reason                  Age   From                     Message
      ----    ------                  ----  ----                     -------
      Normal  Scheduled               29s   default-scheduler        Successfully assigned default/POD_NAME to gke-cluster-1-default-pool-d5cde866-o4g4
      Normal  SuccessfulAttachVolume  21s   attachdetach-controller  AttachVolume.Attach succeeded for volume "PV_NAME"
      Normal  Pulling                 19s   kubelet                  Pulling image "nginx"
      Normal  Pulled                  19s   kubelet                  Successfully pulled image "nginx"
      Normal  Created                 18s   kubelet                  Created container CONTAINER_NAME
      Normal  Started                 18s   kubelet                  Started container CONTAINER_NAME
    

## Using a pre-existing disk in a StatefulSet

You can use pre-existing Compute Engine persistent disks in a [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) using PersistentVolumes. The StatefulSet automatically generates a PersistentVolumeClaim for each replica. You can predict the names of the generated PersistentVolumeClaims and bind them to the PersistentVolumes using `claimRef`.

In the following example, you take two pre-existing persistent disks, create PersistentVolumes to use the disks, and then mount the volumes on a StatefulSet with two replicas in the default namespace.

  1. Decide on a name for your new StatefulSet, a name for your PersistentVolumeClaim template, and the number of replicas in the StatefulSet.
  2. Work out the names of the automatically generated PersistentVolumeClaims. The StatefulSet uses the following format for PersistentVolumeClaim names:
         
         PVC_TEMPLATE_NAME-STATEFULSET_NAME-REPLICA_INDEX
         

Replace the following:

     * `PVC_TEMPLATE_NAME`: the name of your new PersistentVolumeClaim template.
     * `STATEFULSET_NAME`: the name of your new StatefulSet.
     * `REPLICA_INDEX`: the index of the StatefulSet's replica. For this example, use `0` and `1`.
  3. Create the PersistentVolumes. You must create a PersistentVolume for each replica in the StatefulSet.

     1. Save the following YAML manifest:
            
            apiVersion: v1
            kind: PersistentVolume
            metadata:
              name: pv-ss-demo-0
            spec:
              storageClassName: "STORAGE_CLASS_NAME"
              capacity:
                storage: DISK1_SIZE
              accessModes:
                - ReadWriteOnce
              claimRef:
                namespace: default
                name: PVC_TEMPLATE_NAME-STATEFULSET_NAME-0
              csi:
                driver: pd.csi.storage.gke.io
                volumeHandle: DISK1_ID
                fsType: FS_TYPE
             ---
            apiVersion: v1
            kind: PersistentVolume
            metadata:
              name: pv-ss-demo-1
            spec:
              storageClassName: "STORAGE_CLASS_NAME"
              capacity:
                storage: DISK2_SIZE
              accessModes:
                - ReadWriteOnce
              claimRef:
                namespace: default
                name: PVC_TEMPLATE_NAME-STATEFULSET_NAME-1
              csi:
                driver: pd.csi.storage.gke.io
                volumeHandle: DISK2_ID
                fsType: FS_TYPE
            

Replace the following:

        * `DISK1_SIZE and DISK2_SIZE`: the sizes of your pre-existing persistent disks.
        * `DISK1_ID and DISK2_ID`: the identifiers of your pre-existing persistent disks.
        * `PVC_TEMPLATE_NAME-STATEFULSET_NAME-0 and PVC_TEMPLATE_NAME-STATEFULSET_NAME-1`: the names of the automatically generated PersistentVolumeClaims in the format defined in the previous step.
        * `STORAGE_CLASS_NAME`: the name of your StorageClass.
     2. Apply the configuration:
            
            kubectl apply -f FILE_PATH
            

Replace `FILE_PATH` with the path to the YAML file.

  4. [Create a StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps#creating_a_statefulset) using the values you chose in step 1. Ensure that the storage you specify in the `volumeClaimTemplates` is less than or equal to the total capacity of your PersistentVolumes.

     1. Save the following YAML manifest:
            
            apiVersion: apps/v1
            kind: StatefulSet
            metadata:
              name: STATEFULSET_NAME
            spec:
              selector:
                matchLabels:
                  app: nginx
              serviceName: "nginx"
              replicas: 2
              template:
                metadata:
                  labels:
                    app: nginx
                spec:
                  terminationGracePeriodSeconds: 10
                  containers:
                  - name: nginx
                    image: nginx:latest
                    ports:
                    - containerPort: 80
                      name: web
                    volumeMounts:
                    - name: PVC_TEMPLATE_NAME
                      mountPath: /usr/share/nginx/html
              volumeClaimTemplates:
              - metadata:
                  name: PVC_TEMPLATE_NAME
                spec:
                  accessModes: [ "ReadWriteOnce" ]
                  storageClassName: "STORAGE_CLASS_NAME"
                  resources:
                    requests:
                      storage: 100Gi
            

Replace the following:

        * `STATEFULSET_NAME`: the name of your new StatefulSet.
        * `PVC_TEMPLATE_NAME`: the name of your new PersistentVolumeClaim template.
        * `STORAGE_CLASS_NAME`: the name of your StorageClass.
**Note:** Make sure that your StatefulSet name and PersistentVolumeClaim name match the values you decided in step 1.
     2. Apply the configuration:
            
            kubectl apply -f FILE_PATH
            

Replace `FILE_PATH` with the path to the YAML file.




## What's next

  * [Learn how to deploy a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
