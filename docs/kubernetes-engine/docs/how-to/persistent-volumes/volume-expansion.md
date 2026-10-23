---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion/
title: Using volume expansion \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:24.261916+00:00
---

# Using volume expansion  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Using volume expansion Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In Google Kubernetes Engine (GKE) version 1.24 or later, you can use the Kubernetes volume expansion feature to change a persistent volume's capacity after its creation.

For more information on volume expansion, see the open source [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims).

## Prerequisites

Volume expansion has the following prerequisites:

  * If the volume you want to resize is managed by a CSI Driver: 
    * Ensure the GKE cluster version is 1.16 or later. If the cluster has Windows node pools, ensure the GKE cluster version is 1.18 or later. If you are using the managed [GKE Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), the cluster version must be 1.21 or later. If you are using the Managed Lustre CSI driver, the cluster version must be `1.35.0-gke.2331000` or later.
    * Check your storage vendor's documentation to verify your CSI driver supports volume expansion. The Compute Engine Persistent Disk CSI driver, the Filestore CSI driver, and the Managed Lustre CSI driver support volume expansion.
  * If the volume you want to resize is managed by an in-tree volume plugin: 
    * Ensure the GKE cluster version is 1.11 or greater. While GKE cluster versions 1.11-1.14 support expansion of volumes managed by in-tree plugins, they require all Pods using the volume to be terminated and recreated to complete volume expansion.
    * Check your storage vendor's documentation to verify your in-tree volume plugin supports volume expansion (the Compute Engine Persistent Disk in-tree plugin does).
  * You can't use volume expansion when using [`ReadOnlyMany` access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).



## Using volume expansion

**Note:** To avoid errors using volume expansion, ensure that you complete the steps in this section in the right sequence.

To use volume expansion, perform the following tasks:

  1. Add `allowVolumeExpansion: true` to your StorageClass, if your StorageClass doesn't already have the field. For example:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: standard
         provisioner: my.driver
         ...
         **allowVolumeExpansion : true**
         

  2. Request a change in volume capacity by editing your PersistentVolumeClaim's `spec.resources.requests.storage` field.
         
         kubectl edit pvc pvc-name
         

For example, you could change the following PVC from having a 30 gibibyte (GiB) disk to having a 40 GiB disk.

Before editing:
         
         # pvc-demo.yaml
          apiVersion: v1
          kind: PersistentVolumeClaim
          metadata:
            name: pvc-demo
          spec:
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                **storage : 30Gi**
         

After editing:
         
         # pvc-demo.yaml
          apiVersion: v1
          kind: PersistentVolumeClaim
          metadata:
            name: pvc-demo
          spec:
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                **storage : 40Gi**
         

  3. Verify the change by viewing PVC. To view your PVC, run the following command:
         
         kubectl get pvc pvc-name -o yaml
         

Eventually, you should see the new volume in the `status.capacity` field. For example:
         
         ...
         spec:
           accessModes:
           - ReadWriteOnce
           resources:
             requests:
               storage: 40Gi
           storageClassName: standard
           volumeMode: Filesystem
           volumeName: pvc-078b7484-cc8d-4077-9bcb-2c17d8d4550c
         status:
           accessModes:
           - ReadWriteOnce
           **capacity :
             storage: 40Gi**
         ...
         


**Note:** Don't edit the capacity of the PersistentVolume object directly. If you edit the capacity of a PersistentVolume, and then change the size of the corresponding PersistentVolumeClaim to the same value, volume expansion won't happen. Kubernetes will assume that the backing volume was manually resized, and that no expansion is required.

If the capacity of a PersistentVolume is modified directly, this could lead the container file system to be incorrect. To fix these issues, see [troubleshoot volume expansion changes](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-storage#volume_expansion_changes_not_reflecting_in_the_container_filesystem).

## Managing volume expansions in StatefulSets

If you need to increase the size of volumes used by Pods within a [StatefulSet](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#creating-a-statefulset) in Kubernetes, you should adjust the `spec.resources.requests.storage` field of the PersistentVolumeClaims (PVCs) associated with the Pods. Attempting to modify the `volumeClaimTemplates` field directly in the StatefulSet object will cause an error.

Additionally, if you increase the replica count of the StatefulSet, it will still create PVCs of the original size. To permanently change the size of the volumes provisioned for the Pods managed by the StatefulSet, you must delete and recreate the StatefulSet object with the updated size that's specified in the `volumeClaimTemplates` field.

You can perform the following steps in order to keep the original Pods up and running while adjusting the StatefulSet to provision future replicas with the new volume size.

  1. Save the existing StatefulSet to a file:
         
         kubectl get StatefulSet statefulset-name -o yaml > sts-backup.yaml
         

  2. For each PersistentVolumeClaim in the StatefulSet, open the `PersistentVolumeClaim` object in a text editor:
         
         kubectl edit pvc PVC_NAME
         

  3. Update the `spec.resources.requests.storage` field to the new volume size, like in the following example:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
         # lines omitted for clarity
         spec:
           resources:
             requests:
               storage: 14Gi
         # lines omitted for clarity
         

For details, see [Expanding Persistent Volumes Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims).

  4. Save your edits and close the text editor. Wait for Kubernetes to update the PersistentVolumeClaim with your changes.

  5. Remove the StatefulSet object from the cluster while keeping the Pods running as standalone Pods:
         
         kubectl delete sts statefulset-name --cascade=orphan
         

  6. Edit the new volume storage size in the locally saved `sts-backup.yaml` file, specifically the value of `spec.volumeClaimTemplates.spec.resources.requests.storage`

  7. Recreate the StatefulSet back in the cluster:
         
         kubectl apply -f sts-backup.yaml
         




## What's next

  * Learn more about [volumes](https://kubernetes.io/docs/concepts/storage/volumes/).
  * Learn more about [Resizing Persistent Volumes using Kubernetes](https://kubernetes.io/blog/2018/07/12/resizing-persistent-volumes-using-kubernetes/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
