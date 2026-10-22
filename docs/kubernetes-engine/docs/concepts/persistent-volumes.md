---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes/
title: GKE persistent volumes & provisioning \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:46.193236+00:00
---

# GKE persistent volumes & provisioning  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE persistent volumes & provisioning Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of Persistent Volumes (PVs), Persistent Volume Claims (PVCs), and Storage Classes in Google Kubernetes Engine (GKE). It focuses on storage backed by [Compute Engine persistent disks](https://docs.cloud.google.com/compute/docs/disks).

You learn how to effectively create, manage, and troubleshoot persistent storage within your GKE clusters to help ensure data security, high availability, and optimal performance.

This page is for Storage specialists who create and allocate storage and configure and manage data security, protection, and access and permissions. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## PersistentVolumes

`PersistentVolume` resources are used to manage durable storage in a cluster. In GKE, a `PersistentVolume` is typically backed by a persistent disk.

You can use other storage solutions like NFS instead. [Filestore](https://docs.cloud.google.com/filestore/docs) is a NFS solution on Google Cloud. To learn how to set up a Filestore instance as an NFS PV solution for your GKE clusters, see [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver) in the Filestore documentation.

The `PersistentVolume` lifecycle is managed by Kubernetes. A `PersistentVolume` can be dynamically provisioned; you don't have to manually create and delete the backing storage.

`PersistentVolume` resources are cluster resources that exist independently of [Pods](https://kubernetes.io/docs/concepts/workloads/pods). This means that the disk and data represented by a `PersistentVolume` continue to exist as the cluster changes and as Pods are deleted and recreated. `PersistentVolume` resources can be provisioned dynamically through `PersistentVolumeClaims`, or they can be explicitly created by a cluster administrator.

**Caution:** Using the [`[fsGroup]` setting](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems) with large `PersistentVolumes` can cause mounts to fail. For more information, see [Troubleshooting Volume mount failures](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-storage#mounting_a_volume_stops_responding_due_to_the_fsgroup_setting).

To learn more about `PersistentVolume` resources, refer to the [Kubernetes Persistent Volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) and the [Persistent Volumes API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/).

## PersistentVolumeClaims

A `PersistentVolumeClaim` is a request for and claim to a `PersistentVolume` resource. `PersistentVolumeClaim` objects request a specific size, access mode, and [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/) for the `PersistentVolume`. If a `PersistentVolume` that satisfies the request exists or can be provisioned, the `PersistentVolumeClaim` is bound to that `PersistentVolume`.

Pods use claims as volumes. The cluster inspects the claim to find the bound volume and mounts that volume for the Pod.

Portability is another advantage of using `PersistentVolumes` and `PersistentVolumeClaims`. You can use the same [Pod specification](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates) across different clusters and environments because `PersistentVolume` is an interface to the actual backing storage.

## StorageClasses

Volume implementations such as [Compute Engine persistent disk Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) are configured through [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/) resources.

GKE creates a default `StorageClass` for you which uses the balanced persistent disk type (ext4). The default `StorageClass` is used when a `PersistentVolumeClaim` doesn't specify a `StorageClassName`. You can replace the provided default `StorageClass` with your own. For instructions, see [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/).

You can create your own `StorageClass` resources to describe different classes of storage. For example, classes might map to quality-of-service levels, or to backup policies. This concept is sometimes called "profiles" in other storage systems.

If you are using a [cluster with Windows node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows), you must create a `StorageClass` and specify a `StorageClassName` in the `PersistentVolumeClaim` because the default fstype (ext4) is not supported with Windows. If you are using a Compute Engine persistent disk, you must use NTFS as the file storage type.

When defining a `StorageClass`, you must list a provisioner. On GKE, we recommend that you use one of the following provisioners:

  * [Compute Engine persistent disk CSI](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver)
  * [Kubernetes Filestore CSI](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)

**Note:** Support for provisioners other than those listed is not covered by [Cloud Customer Care](https://cloud.google.com/support/docs), except for the open source [SMB CSI Driver for Kubernetes](https://github.com/kubernetes-csi/csi-driver-smb), which is provided on a best effort basis. Third party support for other provisioners might also be available.

## Dynamically provision PersistentVolumes

Most of the time, you don't need to directly configure `PersistentVolume` objects or create Compute Engine persistent disks. Instead, you can create a `PersistentVolumeClaim` and Kubernetes automatically provisions a persistent disk for you.

The following manifest describes a request for a disk with 30 gibibytes (GiB) of storage whose access mode allows it to be mounted as read-write by a single node. It also creates a Pod that consumes the `PersistentVolumeClaim` as a volume.
    
    
    # pvc-pod-demo.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: pvc-demo
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
      storageClassName: standard-rwo
    ---
    kind: Pod
    apiVersion: v1
    metadata:
      name: pod-demo
    spec:
      volumes:
        - name: pvc-demo-vol
          persistentVolumeClaim:
           claimName: pvc-demo
      containers:
        - name: pod-demo
          image: nginx
          resources:
            limits:
              cpu: 10m
              memory: 80Mi
            requests:
              cpu: 10m
              memory: 80Mi
          ports:
            - containerPort: 80
              name: "http-server"
          volumeMounts:
            - mountPath: "/usr/share/nginx/html"
              name: pvc-demo-vol
    

When you create this `PersistentVolumeClaim` object with `kubectl apply -f pvc-pod-demo.yaml`, Kubernetes dynamically creates a corresponding `PersistentVolume` object.

Because the storage class `standard-rwo` uses volume binding mode `WaitForFirstConsumer`, the `PersistentVolume` won't be created until a Pod is scheduled to consume the volume.

The following example shows the `PersistentVolume` created.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      annotations:
        pv.kubernetes.io/provisioned-by: pd.csi.storage.gke.io
      finalizers:
      - kubernetes.io/pv-protection
      - external-attacher/pd-csi-storage-gke-io
      name: pvc-c9a44c07-cffa-4cd8-b92b-15bac9a9b984
      uid: d52af557-edf5-4f96-8e89-42a3008209e6
    spec:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 30Gi
      claimRef:
        apiVersion: v1
        kind: PersistentVolumeClaim
        name: pvc-demo
        namespace: default
        uid: c9a44c07-cffa-4cd8-b92b-15bac9a9b984
      csi:
        driver: pd.csi.storage.gke.io
        csi.storage.k8s.io/fstype: ext4
        volumeAttributes:
          storage.kubernetes.io/csiProvisionerIdentity: 1660085000920-8081-pd.csi.storage.gke.io
        volumeHandle: projects/xxx/zones/us-central1-c/disks/pvc-c9a44c07-cffa-4cd8-b92b-15bac9a9b984
      nodeAffinity:
        required:
          nodeSelectorTerms:
          - matchExpressions:
            - key: topology.gke.io/zone
              operator: In
              values:
              - us-central1-c
      persistentVolumeReclaimPolicy: Delete
      storageClassName: standard-rwo
      volumeMode: Filesystem
    status:
      phase: Bound
    

Assuming that you haven't replaced the storage class `standard-rwo`, this `PersistentVolume` is backed by a new, empty Compute Engine persistent disk.

**Note:** Modifying the `topology.kubernetes.io/zone` label during the lifetime of a PersistentVolume can result in mount failures.

## Delete persistent storage

During dynamic provisioning, you can control whether your persistent storage is deleted when a `PersistentVolumeClaim` (PVC) is deleted. To do this, you set the `reclaimPolicy` field in your `StorageClass` configuration to either `Delete` or `Retain`.

  * **`reclaimPolicy: Delete`** : This is the default policy. When the PVC is deleted, the `PersistentVolume` (PV) object and the underlying disk (such as a Compute Engine persistent disk) are automatically deleted. Use this policy for temporary workloads or for compliance requirements where data must be cleaned up after a job is complete.

  * **`reclaimPolicy: Retain`** : If you set this policy, the PV and the underlying disk are not deleted when you delete the PVC. The PV status changes to **`Released`**. The data is preserved, but the volume cannot be used by a new PVC until an administrator manually reclaims it.




### Manually managing retained volumes

When a `PersistentVolume` has a `Released` status, you must manually decide what to do with the underlying data and disk.

  * **To permanently delete the storage** : You must delete both the Kubernetes `PersistentVolume` resource and the underlying Compute Engine disk.

    1. Delete the `PersistentVolume`: `bash kubectl delete pv <your-pv-name>`
    2. Find the name of the underlying disk by describing the YAML configuration file for the PV and looking for the `volumeHandle` or a similar field.
    3. Delete the Compute Engine persistent disk: `bash gcloud compute disks delete <your-disk-name> --zone=<your-zone>`
  * **To reuse the volume** : Reclaiming a volume with a `Released` status for use by another PVC is an advanced task that involves manually cleaning the disk data and editing the `PersistentVolume` object to make it `Available` again. For more information about the detailed procedure, see the official Kubernetes documentation on [Reclaiming a PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaiming).




To prevent or mitigate data loss, we also recommend enabling [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) and scheduling [regular backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#gcloud) of your GKE cluster.

### Troubleshooting unexpected disk deletion

If you observe that your underlying persistent disks are being deleted when you don't expect them to be, the most common cause is a `reclaimPolicy` field that's set to `Delete` in the `StorageClass` configuration used by your `PersistentVolumeClaim`.

To diagnose this issue, complete the following steps:

  1. Check the `StorageClass` of your PVC: `bash kubectl get pvc <your-pvc-name> -o jsonpath='{.spec.storageClassName}'`

  2. Inspect the `reclaimPolicy` field: `bash kubectl get sc <your-storageclass-name> -o yaml`

  3. **Align the policy with your intent** :

     * If the policy is `Delete` and your application requires data to persist, you must update your application to use a `StorageClass` configuration that sets the policy to `Retain`.
     * If the policy is `Delete` and your application is ephemeral or subject to compliance rules requiring data cleanup, then the configuration is correct and working as intended.



For more information, see the Kubernetes documentation about [Reclaiming](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaiming).

### Manage persistent storage during cluster deletion

When a GKE cluster is deleted, GKE retains `PersistentVolume` resources with either the `Delete` or `Retain` reclaim policy.

To remove `PersistentVolume` resources when you delete a cluster, you can manually delete the namespace of `PersistentVolumeClaim` resources, which will trigger deletion for `PersistentVolume` objects with the `Delete` policy. Alternatively, you can delete individual `PersistentVolumeClaim` resources. However, GKE doesn't wait before these deletion activities are complete before starting to delete the cluster. So, if you delete a namespace then immediately delete the cluster, `PersistentVolume` resources with `Delete` policies might not be deleted.

After cluster deletion, you can view remaining `PersistentVolume` resources in the Google Cloud console.

To view any unused resources, such as unused `PersistentVolume` resources, you can [view recommendations for idle resources](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations).

## Access modes

`PersistentVolume` resources support the following [access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes):

  * **ReadWriteOnce:** The volume can be mounted as read-write by a single node.
  * **ReadOnlyMany:** The volume can be mounted read-only by many nodes.
  * **ReadWriteMany:** The volume can be mounted as read-write by many nodes. `PersistentVolume` resources that are backed by Compute Engine persistent disks don't support this access mode.
  * **ReadWriteOncePod:** The volume can be mounted as read-write by a single Pod only.



### Using Compute Engine persistent disks as ReadOnlyMany

ReadWriteOnce is the most common use case for persistent disks and works as the default access mode for most applications. Compute Engine persistent disks also support ReadOnlyMany mode so that many applications or many replicas of the same application can consume the same disk at the same time. An example use case is serving static content across multiple replicas.

**Note:** You can't attach persistent disks in write mode on multiple nodes at the same time. See Deployments versus StatefulSets.

For instructions, refer to [Use persistent disks with multiple readers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/readonlymany-disks).

## Use pre-existing persistent disks as PersistentVolumes

Dynamically provisioned `PersistentVolume` resources are empty when they are created. If you have an existing Compute Engine persistent disk populated with data, you can introduce it to your cluster by manually creating a corresponding `PersistentVolume` resource. The persistent disk must be in the same [zone](https://docs.cloud.google.com/compute/docs/regions-zones) as the cluster nodes.

Refer to this [example of how to create a Persistent Volume backed by a pre-existing persistent disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd).

**Note:** Mounting a persistent disk from a different Google Cloud project to a Pod in your current Google Cloud project is not supported.

## Deployments versus StatefulSets

You can use a `PersistentVolumeClaim` or `VolumeClaim` templates in higher level controllers such as [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) or [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) respectively.

Deployments are designed for [_stateless applications_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps) so all replicas of a Deployment share the same `PersistentVolumeClaim`. Since the replica Pods created are identical to each other, only volumes with the ReadWriteMany mode can work in this setting.

Even Deployments with one replica using ReadWriteOnce volume are not recommended. This is because the default Deployment strategy creates a second Pod before bringing down the first Pod on a recreate. The Deployment may fail in deadlock as the second Pod can't start because the ReadWriteOnce volume is already in use, and the first Pod won't be removed because the second Pod has not yet started. Instead, use a StatefulSet with ReadWriteOnce volumes.

StatefulSets are the recommended method of deploying stateful applications that require a unique volume per replica. By using StatefulSets with PersistentVolumeClaim templates, you can have applications that can scale up automatically with unique PersistentVolumesClaims associated to each replica Pod.

## Regional persistent disks

[Regional persistent disks](https://docs.cloud.google.com/compute/docs/disks#repds) are multi-zonal resources that replicate data between two zones in the same region, and can be used similarly to zonal persistent disks. In the event of a zonal outage or if cluster nodes in one zone become unschedulable, Kubernetes can failover workloads using the volume to the other zone. You can use regional persistent disks to build highly available solutions for stateful workloads on GKE. You must ensure that both the primary and failover zones are configured with enough resource capacity to run the workload.

Regional SSD persistent disks are an option for applications such as databases that require both high availability and high performance. For more details, see [Block storage performance comparison](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison).

As with zonal persistent disks, regional persistent disks can be dynamically provisioned as needed or manually provisioned in advance by the cluster administrator. To learn how to add regional persistent disks, see [Provisioning regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd).

## Zones in persistent disks

[Zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs) are zonal resources and regional persistent disks are multi-zonal resources. When you [add persistent storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps#requesting_persistent_storage_in_a_statefulset) to your cluster, unless a zone is specified, GKE assigns the disk to a single zone. GKE chooses the zone at random. Once a persistent disk is provisioned, any Pods referencing the disk are scheduled to the same zone as the persistent disk. However, Pods or Deployments don't inherently recognize the zone of pre-existing persistent disks. To ensure Pods are scheduled correctly with pre-existing persistent disks, use [zonal placement methods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology#zonal-placement-methods) like [nodeAffinity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology#nodeaffinity-placement) in your Pod or Deployment specifications to target the appropriate zones.

## Volume binding mode WaitForFirstConsumer

If you dynamically provision a persistent disk in your cluster, we recommend you set the `WaitForFirstConsumer` [volume binding mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode) on your StorageClass. This setting instructs Kubernetes to provision a persistent disk in the same zone that the Pod gets scheduled to. It respects Pod scheduling constraints such as [anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) and node selectors. Anti-affinity on zones allows StatefulSet Pods to be spread across zones along with the corresponding disks.

Following is an example `StorageClass` for provisioning zonal persistent disks that sets `WaitForFirstConsumer`:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: slow
    provisioner: pd.csi.storage.gke.io
    parameters:
      type: pd-balanced
      csi.storage.k8s.io/fstype: ext4
    **volumeBindingMode : WaitForFirstConsumer**
    

For an example using regional persistent disks, see [Provisioning regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd).

## What's next

  * [Learn about StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset), the recommended method of deploying stateful applications.
  * [Learn how to deploy a stateful application using a StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).
  * [Learn to use persistent disks in a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/persistent-disk).
  * [Learn how to create a disk that can be read from multiple nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/readonlymany-disks).
  * [Learn how to create persistent disks backed by SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/ssd-pd).
  * [Learn how to provision regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
