---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning/
title: Create clones of persistent volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:44.603455+00:00
---

# Create clones of persistent volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create clones of persistent volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to use Kubernetes volume cloning to clone [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in your Google Kubernetes Engine (GKE) clusters.

## Overview

A clone is a new independent volume that is a duplicate of an existing Kubernetes volume. A clone is similar to a [volume snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) in that it's a copy of a volume at a specific point in time. However, rather than creating a snapshot object from the source volume, volume cloning provisions the clone with all the data from the source volume.

## Requirements

To use volume cloning on GKE, you must meet the following requirements:

  * The source PersistentVolumeClaim must be in the same namespace as the destination PersistentVolumeClaim.
  * Use a CSI driver that supports volume cloning. The in-tree persistent disk driver does not support volume cloning. 
    * The [Compute Engine persistent disk CSI Driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) version 1.4.0 and later supports volume cloning, and is installed by default on new Linux clusters running GKE version 1.22 or later. You can also [enable the Compute Engine persistent disk CSI Driver on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster).



To verify the Compute Engine persistent disk CSI Driver version, run the following command in the gcloud CLI:
    
    
    kubectl describe daemonsets pdcsi-node --namespace=kube-system | grep "gke.gcr.io/gcp-compute-persistent-disk-csi-driver"
    

If the output shows a version earlier than `1.4.0`, [manually upgrade your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp) to get the latest version.

## Limitations

  * Both volumes must use the same [volume mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-mode). By default, GKE sets the VolumeMode to `ext4`.
  * All [restrictions for creating a disk clone from an existing disk](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#restrictions) on Compute Engine also apply to GKE.
  * You can create a regional disk clone from a zonal disk, but you should be aware of the [restrictions of this approach](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#restrictions_2). 
  * Cloning must be done in a compatible zone. Use [allowedTopologies](https://kubernetes.io/docs/concepts/storage/storage-classes/#allowed-topologies) to restrict the topology of provisioned volumes to specific zones. Alternatively, [nodeSelectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) or [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) can be used to constrain a Pod so that it is restricted to run on particular node that runs in a compatible zone. 
    * For zonal to zonal cloning, the clone zone must match the source disk zone.
    * For zonal to regional cloning, one of the replica zones of the clone must match the zone of the source disk.



## Using volume cloning

To provision a volume clone, you add a reference to an existing PersistentVolumeClaim in the same namespace to the `dataSource` field of a new PersistentVolumeClaim. The following exercise shows you how to provision a source volume with data, create a volume clone, and consume the clone.

### Create a source volume

To create a source volume, follow the instructions in [Using the Compute Engine persistent disk CSI Driver for Linux clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#using_the_for_linux_clusters) to create a StorageClass, a PersistentVolumeClaim, and a Pod to consume the new volume. You'll use the PersistentVolumeClaim that you create as the source for the volume clone.

### Add a test file to the source volume

Add a test file to the source volume. You can look for this test file in the volume clone to verify that cloning was successful.

  1. Create a test file in a Pod:
         
         kubectl exec POD_NAME \
             -- sh -c 'echo "Hello World!" > /var/lib/www/html/hello.txt'
         

Replace `POD_NAME` with the name of a Pod that consumes the source volume. For example, if you followed the instructions in [Using the Compute Engine persistent disk CSI Driver for Linux clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#using_the_for_linux_clusters), replace `POD_NAME` with `web-server`.

  2. Verify that the file exists:
         
         kubectl exec POD_NAME \
             -- sh -c 'cat /var/lib/www/html/hello.txt'
         

The output is similar to the following:
         
         Hello World!
         




### Clone the source volume

  1. Save the following manifest as `podpvc-clone.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc-clone
         spec:
           dataSource:
             name: PVC_NAME
             kind: PersistentVolumeClaim
           accessModes:
           - ReadWriteOnce
           storageClassName: STORAGE_CLASS_NAME
           resources:
             requests:
               storage: STORAGE
         

Replace the following:

     * `PVC_NAME`: the name of the source PersistentVolumeClaim that you created in Create a source volume.
     * `STORAGE_CLASS_NAME`: the name of the StorageClass to use, which must be the same as the StorageClass of the source PersistentVolumeClaim.
     * `STORAGE`: the amount of storage to request, which must be at least the size of the source PersistentVolumeClaim.
  2. Apply the manifest:
         
         kubectl apply -f podpvc-clone.yaml
         




### Create a Pod that consumes the cloned volume

The following example creates a Pod that consumes the volume clone that you created.

  1. Save the following manifest as `web-server-clone.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: web-server-clone
         spec:
           containers:
            - name: web-server-clone
              image: nginx
              volumeMounts:
                - mountPath: /var/lib/www/html
                  name: mypvc
           volumes:
            - name: mypvc
              persistentVolumeClaim:
                claimName: podpvc-clone
                readOnly: false
         

  2. Apply the manifest:
         
         kubectl apply -f web-server-clone.yaml
         

  3. Verify that the test file exists:
         
         kubectl exec web-server-clone \
             -- sh -c 'cat /var/lib/www/html/hello.txt'
         

The output is similar to the following:
         
         Hello World!
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

  1. Delete the `Pod` objects:
         
         kubectl delete pod POD_NAME web-server-clone
         

  2. Delete the `PersistentVolumeClaim` objects:
         
         kubectl delete pvc podpvc podpvc-clone
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
