---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd/
title: Provisioning regional persistent disks and Hyperdisk Balanced High Availability volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:37.126658+00:00
---

# Provisioning regional persistent disks and Hyperdisk Balanced High Availability volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provisioning regional persistent disks and Hyperdisk Balanced High Availability volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to enable dynamic provisioning of [Hyperdisk Balanced High Availability volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) and [regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#regional_persistent_disks) and how to provision them manually in Google Kubernetes Engine (GKE). For machine type compatibilities, see [Limitations for Regional Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#repd_limitations) and [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support). Generally, you should use Hyperdisk Balanced High Availability volumes for 3rd generation machine series or newer and regional persistent disks in 2nd generation machine series or older. For more information on machine series generation, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology).

For creating end-to-end solutions for high-availability applications with regional persistent disks, see [Increase stateful app availability with Stateful HA Operator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha). This feature does not support Hyperdisk Balanced High Availability volumes.

**Note:** Multi-writer disks can only be consumed in Block volume mode. The application is responsible for managing its own filesystem or other synchronization mechanism on top of the block device. For more information, see [Supported file systems for multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#supported_file_systems_for_multi-writer_mode).

## Hyperdisk Balanced High Availability

This example shows how Hyperdisk Balanced High Availability volumes can be dynamically provisioned as needed or manually provisioned in advance by the cluster administrator.

**Note:** Provisioning Hyperdisk Balanced High Availability volumes is only supported by the [Compute Engine persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) starting from GKE version 1.33.

### Dynamic provisioning

  1. Save the following manifest in a file named `balanced-ha-storage.yaml`.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: balanced-ha-storage
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         # Allow volume expansion.
         allowVolumeExpansion: true
         parameters:
           type: hyperdisk-balanced-high-availability
           # Provisioned throughput in MiB/s.
           provisioned-throughput-on-create: "250Mi"
           # Provisioned IOPS (input/output operations per second).
           provisioned-iops-on-create: "7000"
         allowedTopologies:
         - matchLabelExpressions:
           - key: topology.gke.io/zone
             values:
             - ZONE1
             - ZONE2
         

Replace the following:

     * `ZONE1`, `ZONE2`: the zones within the region where the dynamically provisioned volume will be replicated.
  2. Create the StorageClass:
         
         kubectl create -f hdb-ha-example-class.yaml
         

  3. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ACCESS_MODE
           storageClassName: balanced-ha-storage
           resources:
             requests:
               storage: 20Gi
         

Replace the following:

     * `ACCESS_MODE`: Hyperdisk Balanced High Availability supports `ReadWriteOnce`, `ReadWriteMany` and `ReadWriteOncePod`. For differences and use cases of each access mode, see [Persistent Volume Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
     * If you choose to use `ReadWriteMany`, you also need to add `volumeMode: Block` to the `PersistentVolumeClaim`. This setting prevents data corruption that can happen from multiple Pods writing to the storage simultaneously. The `volumeMode: Block` setting exposes the disk as a raw block device that bypasses file system management by Kubernetes. The following is an example:
    
    kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: podpvc
      spec:
        accessModes:
        - ReadWriteMany
        volumeMode: Block
        storageClassName: balanced-ha-storage
        resources:
          requests:
            storage: 20Gi
      ```
    

  4. Apply the PersistentVolumeClaim that references the StorageClass you created from earlier:
         
         kubectl apply -f pvc-example.yaml
         




### Manual Provisioning

  1. Follow [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk) to create a Hyperdisk Balanced High Availability volume manually.

  2. Save the following PersistentVolume manifest in a file named `pv-example.yaml`. The manifest references the Hyperdisk Balanced High Availability volume you just created:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: pv-demo
         spec:
           capacity:
             storage: 500Gi
           accessModes:
             - ACCESS_MODE
           # ClaimRef links this PersistentVolume to a PersistentVolumeClaim.
           claimRef:
             namespace: default
             name: podpvc
           csi:
             driver: pd.csi.storage.gke.io
             # The unique identifier of the Compute Engine disk resource that backs this volume.
             volumeHandle: projects/PROJECT_ID/regions/REGION/disks/gce-disk-1
           # Node affinity to ensure the Pod is scheduled in a zone where the volume is replicated.
           nodeAffinity:
             required:
               nodeSelectorTerms:
                 - matchExpressions:
                   - key: topology.gke.io/zone
                     operator: In
                     values:
                     - ZONE1
                     - ZONE2
         

Replace the following:

     * `PROJECT_ID`: the project ID of the volume you created.
     * `REGION`: the region of the disk you created. Refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) for the latest regional availability.
     * `ZONE1`, `ZONE2`: the zones within the region where the volume you created is replicated.
     * `ACCESS_MODE`: Hyperdisk Balanced High Availability supports `ReadWriteOnce`, `ReadWriteMany` and `ReadWriteOncePod`. For differences and use cases of each access mode, see [Persistent Volume Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
  3. Create the Persistent Volume that references the Hyperdisk Balanced High Availability volume you created earlier:
         
         kubectl apply -f pv-example.yaml
         

  4. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ACCESS_MODE
           storageClassName: balanced-ha-storage
           resources:
             requests:
               storage: 20Gi
         

Replace the following:

     * `ACCESS_MODE`: Hyperdisk Balanced High Availability supports `ReadWriteOnce`, `ReadWriteMany` and `ReadWriteOncePod`. Must be the same access mode as what is specified in the PersistentVolume from the previous step. For differences and use cases of each access mode, see [Persistent Volume Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
  5. Apply the PersistentVolumeClaim that references the PersistentVolume you created from earlier:
         
         kubectl apply -f pvc-example.yaml
         




### Consuming a multi-writer volume in block mode

In order to use a volume in block mode, you must specify `volumeBlock` instead of `volumeMounts` in the consuming Pod. An example Pod that uses the previously introduced `PersistenVolumeClaim` should look like the following:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: web-server-deployment
      labels:
        app: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx
            # Use volumeDevices instead of volumeMounts to consume the volume as a raw block device.
            volumeDevices:
            # The "mountPath" field specifies the path where the block device is accessible in the container.
            - mountPath: /dev/my-device
              name: mypvc
          volumes:
          - name: mypvc
            persistentVolumeClaim:
              claimName: podpvc
              readOnly: false
    

## Regional persistent disks

As with zonal persistent disks, regional persistent disks can be dynamically provisioned as needed or manually provisioned in advance by the cluster administrator, although dynamic provisioning is recommended. To utilize regional persistent disks of the `pd-standard` type, set the PersistentVolumeClaim's `spec.resources.requests.storage` attribute to a minimum of 200 GiB. If your use case requires a smaller volume, consider using `pd-balanced` or `pd-ssd` instead.

### Dynamic provisioning

To enable dynamic provisioning of regional persistent disks, create a `StorageClass` with the `replication-type` parameter, and specify zone constraints in `allowedTopologies`.

For example, the following manifest describes a `StorageClass` named `regionalpd-storageclass` that uses standard persistent disks and that replicates data to the `europe-west1-b` and `europe-west1-c` zones:
    
    
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    metadata:
      name: regionalpd-storageclass
    provisioner: pd.csi.storage.gke.io
    parameters:
      type: pd-balanced
      # Specifies that the disk should be a regional persistent disk.
      replication-type: regional-pd
    volumeBindingMode: WaitForFirstConsumer
    # Constrains which zones the regional persistent disk can be provisioned in.
    allowedTopologies:
    - matchLabelExpressions:
      - key: topology.gke.io/zone
        values:
        - europe-west1-b
        - europe-west1-c
    

If using a regional cluster, you can leave `allowedTopologies` unspecified. If you do this, when you create a Pod that consumes a `PersistentVolumeClaim` which uses this `StorageClass` a regional persistent disk is provisioned with two zones. One zone is the same as the zone that the Pod is scheduled in. The other zone is randomly picked from the zones available to the cluster.

**Note:** You can omit `allowedTopologies` in your StorageClass only if your node pools have active nodes in at least two different zones. This allows GKE to automatically select the correct primary and secondary zones for your regional persistent disks.

When using a zonal cluster, `allowedTopologies` must be set.

Once the `StorageClass` is created, next create a `PersistentVolumeClaim` object, using the `storageClassName` field to refer to the `StorageClass`. For example, the following manifest creates a `PersistentVolumeClaim` named `regional-pvc` and references the `regionalpd-storageclass`:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: regional-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 500Gi
      storageClassName: regionalpd-storageclass
    

Since the `StorageClass` is configured with `volumeBindingMode: WaitForFirstConsumer`, the `PersistentVolume` is not provisioned until a Pod using the `PersistentVolumeClaim` has been created.

The following manifest is an example Pod using the previously created `PersistentVolumeClaim`:
    
    
    kind: Pod
    apiVersion: v1
    metadata:
      name: task-pv-pod
    spec:
      volumes:
        - name: task-pv-storage
          # This Pod uses the PVC that's associated with the
          # "regionalpd-storageclass" StorageClass.
          persistentVolumeClaim:
            claimName: regional-pvc
      containers:
        - name: task-pv-container
          image: nginx
          ports:
            - containerPort: 80
              name: "http-server"
          # The volume is mounted into the container at the "/usr/share/nginx/html" path.
          volumeMounts:
            - mountPath: "/usr/share/nginx/html"
              name: task-pv-storage
    

### Manual provisioning

First, create a regional persistent disk using the [`gcloud compute disks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) command. The following example creates a disk named `gce-disk-1` replicated to the `europe-west1-b` and `europe-west1-c` zones:
    
    
    gcloud compute disks create gce-disk-1 \
       --size 500Gi \
       --region europe-west1 \
       --replica-zones europe-west1-b,europe-west1-c
    

You can then create a `PersistentVolume` that references the regional persistent disk you just created. In addition to objects in [Using preexisting Persistent Disks as PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd), the `PersistentVolume` for a regional persistent disk should also specify a [`node-affinity`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#node-affinity). If you use a `StorageClass`, it should specify the persistent disk CSI driver.

Here's an example of a `StorageClass` manifest that uses standard persistent disks and that replicates data to the `europe-west1-b` and `europe-west1-c` zones:
    
    
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    metadata:
      name: regionalpd-storageclass
    provisioner: pd.csi.storage.gke.io
    parameters:
      type: pd-balanced
      # Specifies that the disk should be a regional persistent disk.
      replication-type: regional-pd
    volumeBindingMode: WaitForFirstConsumer
    # Constrains which zones the regional persistent disk can be provisioned in.
    allowedTopologies:
    - matchLabelExpressions:
      - key: topology.gke.io/zone
        values:
        - europe-west1-b
        - europe-west1-c
    

Here's an example manifest that creates a `PersistentVolume` named `pv-demo` and references the `regionalpd-storageclass`:
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: pv-demo
    spec:
      # The StorageClass that specifies regional replication.
      storageClassName: "regionalpd-storageclass"
      capacity:
         storage: 500Gi
      accessModes:
         - ReadWriteOnce
      claimRef:
        namespace: default
        name: pv-claim-demo
      csi:
        driver: pd.csi.storage.gke.io
        # The unique identifier for the pre-existing regional disk.
        volumeHandle: projects/PROJECT_ID/regions/europe-west1/disks/gce-disk-1
      # Ensures that Pods are scheduled in zones where the disk is replicated.
      nodeAffinity:
        required:
          nodeSelectorTerms:
            - matchExpressions:
              - key: topology.gke.io/zone
                operator: In
                values:
                   - europe-west1-b
                   - europe-west1-c
    

Note the following for the `PersistentVolume` example:

  * The `volumeHandle` field contains details from the `gcloud compute disks create` call, including your `PROJECT_ID`.
  * The `claimRef.namespace` field must be specified even when it is set to `default`.



## Naming persistent disks

Kubernetes cannot distinguish between zonal and regional persistent disks with the same name. As a workaround, ensure that persistent disks have unique names. This issue does not occur when using dynamically provisioned persistent disks.

## What's next

  * Take a tutorial to learn about [Deploying WordPress on GKE with Persistent Disks and Cloud SQL](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/persistent-disk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
