---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/storage/
title: Configure Distributed Cloud connected storage \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:17:33.843042+00:00
---

# Configure Distributed Cloud connected storage  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/storage/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Configure Distributed Cloud connected storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure storage for Distributed Cloud connected clusters, including:

  * Rakuten Symcloud Storage
  * Local storage schemas
  * Troubleshooting



## Configure Distributed Cloud connected for Symcloud Storage

Distributed Cloud connected nodes don't expose their local storage directly to your workloads. Instead, Distributed Cloud connected uses [Rakuten Symcloud Storage](https://symphony.rakuten.com/insight/datasheet/symcloud-storage), which is a third-party solution that acts as a local storage abstraction layer that runs on each Distributed Cloud connected node and makes its local storage available to workloads running on all Distributed Cloud connected nodes in a cluster.

[Container Storage Interface](https://github.com/container-storage-interface/spec) (CSI) is an open standard API supported by many major storage vendors that enables Kubernetes to expose arbitrary storage systems to containerized workloads. In Distributed Cloud connected, Symcloud Storage is the supported and managed CSI storage solution. When Symcloud Storage is activated, the required Kubernetes [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/) are configured for you. You can then configure your workloads to use the appropriate storage class.

Symcloud Storage is deployed from Google Cloud Marketplace and is subject to the terms stated therein. Google provides limited support for using Symcloud Storage with Distributed Cloud connected and might engage the third-party provider for assistance. Software updates for Symcloud Storage are included in the Distributed Cloud connected software updates.

This release of Distributed Cloud connected ships with and supports [Symcloud Storage 6.0.0-226](https://docs.robin.io/storage/6.0.0/release_note.html). No other version of Symcloud Storage is supported in this release of Distributed Cloud connected.

### Obtain a Symcloud Storage license

You must obtain a Symcloud Storage license in YAML format from the Google Cloud Marketplace:

[Go to Marketplace](https://console.cloud.google.com/marketplace/product/robinio-public/enterprise-sds-by-rakuten?project=_)

### Prerequisites

Before you begin, complete the following steps:

  1. [Configure logging and monitoring](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/logs-metrics#configure_logging_and_monitoring) for the target Distributed Cloud connected project.
  2. [Create the target Distributed Cloud connected cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#create). You can [monitor the provisioning progress](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#monitor-provisioning).
  3. [Configure your Distributed Cloud networking](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/networking) so that Pods in the target Distributed Cloud connected cluster can reach the Google Cloud data center.
  4. Software-defined storage (SDS) solutions such as Symcloud Storage target unbound `local-block` raw block devices. Distributed Cloud connected expects an SDS solution to be installed at cluster creation when unbound `local-block` devices are available.



### Install Symcloud Storage on a Distributed Cloud connected node

To install Symcloud Storage on a Distributed Cloud connected node, complete the following steps:

  1. Use the following command to apply the Symcloud Storage license to your cluster. Replace `LICENSE_FILE` with the full path and name of the Symcloud Storage license file.
         
         kubectl apply -f LICENSE_FILE -n robin-admin
         

  2. Use the following command to verify the status of the `RobinCluster` service and all the Symcloud Storage nodes:
         
         kubectl describe robinclusters -n robinio
         

The command returns output similar to the following:
         
         [...]
         Status:
         [...]
         Phase:              Ready
         robin_node_status:
         [...]
          Status:           Ready
         [...]
          Status:           Ready
         [...]
          Status:           Ready
         [...]
         

The expected status for the service and nodes is `Ready`.




### Set Symcloud Storage as the default storage class

Use the following command to set Symcloud Storage as the default storage class on your Distributed Cloud connected cluster. Replace `STORAGE_CLASS` with one of the Symcloud Storage classes.
    
    
    kubectl patch storageclass STORAGE_CLASS -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
    

For more information about setting the default storage class, see [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) in the Kubernetes documentation.

### Symcloud Storage classes

This section describe the storage classes that Symcloud Storage can enable on your Distributed Cloud connected cluster. Symcloud Storage on Distributed Cloud connected does not support the `robin-rwx` storage class nor any custom-configured RWX file system mode volumes. For more information on Symcloud Storage classes, see [Using Robin CNS in Kubernetes](https://docs.robin.io/storage/latest/storage.html).

#### `robin` storage class

The `robin` storage class is a basic Read Write-Once (RWO) storage class. The following example illustrates the instantiation of the class:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
        name: robin
        labels:
            app.kubernetes.io/instance: robin
            app.kubernetes.io/managed-by: robin.io
            app.kubernetes.io/name: robin
    provisioner: robin
    reclaimPolicy: Delete
    allowVolumeExpansion: true
    volumeBindingMode: WaitForFirstConsumer
    

**Warning:** Using this single-replica storage class can result in **loss of data** as it doesn't provide redundancy in case of node failure. We strongly recommend that you use a storage class that provides redundancy with at least three replicas.

#### `robin-immediate` storage class

The `robin-immediate` storage class is the same as `robin` except that the persistent volume is created immediately after creating the corresponding persistent volume claim. The following example illustrates the instantiation of the class:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
        name: robin-immediate
        labels:
            app.kubernetes.io/instance: robin
            app.kubernetes.io/managed-by: robin.io
            app.kubernetes.io/name: robin
    provisioner: robin
    reclaimPolicy: Delete
    allowVolumeExpansion: true
    volumeBindingMode: Immediate
    

**Warning:** Using this single-replica storage class can result in **loss of data** as it doesn't provide redundancy in case of node failure. We strongly recommend that you use a storage class that provides redundancy with at least three replicas.

#### `robin-repl-3` storage class

The `robin-repl-3` is an RWO storage class with three replicas that span across multiple Distributed Cloud nodes. The following example illustrates the instantiation of the class:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
        name: robin-repl-3
        labels:
            app.kubernetes.io/instance: robin
            app.kubernetes.io/managed-by: robin.io
            app.kubernetes.io/name: robin
    provisioner: robin
    reclaimPolicy: Delete
    allowVolumeExpansion: true
    volumeBindingMode: WaitForFirstConsumer
    parameters:
        replication: "3"
        faultdomain: host
    

### Configure abstracted Symcloud Storage volumes for workloads

This section provides examples for how to use Symcloud Storage classes to configure abstracted storage for your Distributed Cloud connected workloads. For more details about configuring Symcloud Storage volumes, see [Using Robin CNS in Kubernetes](https://docs.robin.io/storage/latest/storage.html).

#### Configure an `ext4` RWO volume in file system mode

The following example illustrates how to configure a persistent volume claim for an RWO volume in file system mode with the `ext4` file system. Replace `STORAGE_CLASS` with one of the Symcloud Storage classes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: rwo-fs-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
      storageClassName: STORAGE_CLASS
    

#### Configure an RWO volume in block mode

The following example illustrates how to configure a persistent volume claim for an RWO volume in block mode. Replace `STORAGE_CLASS` with one of the Symcloud Storage classes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: rwo-block-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
      storageClassName: STORAGE_CLASS
      volumeMode: Block
    

#### Modify the configuration of an existing volume

The following example illustrates how to modify the configuration of an existing Symcloud Storage LZ4 compressed RWO volume by using annotations. Replace`STORAGE_CLASS` with one of the Symcloud Storage classes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: compressed-rwo-fs-pvc
      annotations:
        robin.io/compression: LZ4
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
      storageClassName: STORAGE_CLASS
    

The following example illustrates how to modify the configuration of an existing Symcloud Storage RWO volume with the `xfs` file system by using annotations. Replace`STORAGE_CLASS` with one of the Symcloud Storage classes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: rwo-xfs-pvc
      annotations:
        robin.io/fstype: xfs
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
      storageClassName: STORAGE_CLASS
    

#### Configure the Symcloud Storage CLI client

Symcloud Storage provides a command-line interface (CLI) client that you can use to manage your Symcloud Storage configuration. To configure the client on your Distributed Cloud connected cluster, complete the following steps:

  1. Get the Symcloud Storage image path used by the `RobinCluster` service instance deployed on your Distributed Cloud connected cluster and set your environment variables as follows:
         
         image_robin=$(kubectl get robincluster -o jsonpath='{.items[].spec.image_robin}')
         image_registry_path=$(kubectl get robincluster -o jsonpath='{.items[].spec.image_registry_path}')
         ROBIN_CNS_IMAGE="$image_registry_path/$image_robin"
         

  2. Create a `robincli` resource with the following contents:
         
         kind: Deployment
         apiVersion: apps/v1
         metadata:
          name: robincli
          namespace: default
          labels:
            name: robincli
         spec:
          replicas: 1
          selector:
            matchLabels:
              name: robincli
          template:
            metadata:
              annotations:
                product: robin
              labels:
                name: robincli
            spec:
              containers:
              - name: robincli
                image: ROBIN_CNS_IMAGE
                workingDir: /root
                command: ["/bin/bash","-c","mkdir -p /root/.robin; ln -s -t /usr/lib/python3.7/site-packages/ /opt/robin/current/python3/site-packages/robincli /opt/robin/current/python3/site-packages/stormgr_def.py /opt/robin/current/python3/site-packages/stormgr_lib.py; /opt/robin/current/bin/robin client add-context robin-master.robinio --set-current; while true; do sleep 10000; done"]
                resources:
                  requests:
                    memory: "10Mi"
                    cpu: "100m"
         

Replace `ROBIN_CNS_IMAGE` with the full repository path and name of the image that you obtained in step 1.

  3. Apply the `robincli` resource onto your Distributed Cloud connected cluster.

  4. Upon initial installation, Symcloud Storage generates a `default-admin-user` secret in the `robinio` namespace with a randomized password. Use the following commands to obtain these logon credentials:

     1. Obtain the username:
            
            kubectl -n robinio get secret default-admin-user -o jsonpath='{.data.username}' | base64 -d
            

     2. Obtain the password:
            
            kubectl -n robinio get secret default-admin-user -o jsonpath='{.data.password}' | base64 -d
            

  5. Log on to the newly created Pod and run the client:
         
         kubectl exec -it robincli -- bash
         




#### Reference the storage class in a StatefulSet

The following example shows how to reference a Symcloud Storage class in a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) workload.

The example assumes that you're using the pre-configured `robin-repl-3` storage class, which provides volumes replicated across three distinct worker nodes for high availability.

When configuring a StatefulSet for high availability, include the following best practices in your configuration:

  * **Headless Service** : A StatefulSet requires a companion Headless Service matching the `serviceName` field. A Headless Service is a service with `clusterIP: None`. This service assigns stable DNS hostnames to each Pod in the set.
  * **Pod anti-affinity** : If you use a replicated storage class like `robin-repl-3`, your data is safely mirrored across multiple worker nodes. However, if Kubernetes schedules all of your application Pods onto the same worker node, a single node outage can take down your application. Configuring Pod anti-affinity ensures your Pods are distributed across separate worker nodes, matching your compute availability to your storage redundancy.



The following example demonstrates a complete configuration that includes the Headless Service (`nginx`) and a StatefulSet configured with Pod anti-affinity referencing the `robin-repl-3` storage class. If your workload storage requirements grow over time, you can dynamically resize the volume by editing the storage request in the PersistentVolumeClaim.

**Note:** Pre-configured Symcloud Storage classes use `volumeBindingMode: WaitForFirstConsumer`, which delays volume provisioning until the Pod is scheduled. Consequently, your PersistentVolumeClaims remain in a `Pending` state, or `waiting for first consumer`, until Pod scheduling completes. This behavior is expected.

### statefulset.yaml
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      ports:
      - port: 80
        name: web
      clusterIP: None
      selector:
        app: nginx
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      serviceName: "nginx"
      replicas: 2
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                  - key: app
                    operator: In
                    values:
                    - nginx
                topologyKey: "kubernetes.io/hostname"
          containers:
          - name: nginx
            image: registry.k8s.io/nginx-slim:0.8
            volumeMounts:
            - name: www
              mountPath: /usr/share/nginx/html
      volumeClaimTemplates: # Reference the storage class in this specification
      - metadata:
          name: www
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 10Gi # Symcloud Storage classes support dynamic volume expansion if more storage is needed
          storageClassName: robin-repl-3 # References the Symcloud storage class

### Limitations of Symcloud Storage

When using Symcloud Storage with Distributed Cloud connected, you can only achieve high availability if your Distributed Cloud connected cluster consists of three or more Distributed Cloud connected nodes.

### Removing nodes that use Symcloud Storage from a cluster

Symcloud Storage volume replicas are stored on worker nodes within your Distributed Cloud connected cluster. If you remove a node from the cluster, the Symcloud Storage volume data stored on that node becomes unavailable. To prevent this, you must do one of the following:

  * If you are tearing down the entire cluster, remove the workloads and their corresponding Symcloud Storage persistent volumes before you tear down the cluster itself.
  * If you are removing specific nodes from the cluster, you must migrate the workload data stored on those nodes before you remove those nodes from the cluster. For instructions, see [Evacuating volumes from a disk](https://docs.robin.io/storage/5.3.4/manage_storage.html#evacuating-volumes-from-a-disk).



## Configure local storage schemas

A storage schema is a logical grouping of one or more partitions. Each partition is a logically independent unit of storage. Partitions are created on your cluster sequentially until physical disk space has been exhausted. Each storage schema has a unique name that identifies it.

To create a new local storage schema for your Distributed Cloud connected cluster, you must request it from Google. Once we test the schema and create it on your cluster, you can then apply it using the `gcloud` CLI.

You cannot modify a schema after it's been applied to a cluster. To change an existing schema, you must request the deletion of the existing schema from Google and then request the creation of a new schema to replace it.

### Define partitions for a local storage schema

Before you can request a local storage schema you must first define the partitions for that schema.

A partition has the following properties:

  * **Size.** You can either specify a partition size in binary bytes, or have it use all remaining space on the local disk.
  * **Type.** You can configure a partition as either a Kubernetes persistent volume (PV) or a Linux local volume on the local disk.
  * **Mode.** You can configure the volume stored in the partition as either a block volume or a file system volume. For persistent volume partitions, the partition's storage class is either `local-block` or `local-disks`, respectively. For local volume partitions, you can specify the bind and mount points for the contained filesystems.



### Request a local storage schema

To request a new local storage schema for your Distributed Cloud connected cluster, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/getting-support) and provide the size, type, mode, and, optionally, mount and bind points for each partition you want to create in the schema.

When we receive your request, we run a series of tests to ensure the robustness of the schema, then create it on your Distributed Cloud connected cluster.

### Default local storage schemas

Distributed Cloud connected ships with the following default local storage schemas:

  * **`default_control_plane_node`**. This schema defines the following partitions:

    * A 100GB local volume partition in file system mode.
    * A persistent volume partition in block mode that occupies the remaining free disk space.
  * **`default_worker_node`**. This schema defines a 410GB persistent volume partition in block mode.




### Apply a local storage schema to a cluster

To apply a local storage schema to your Distributed Cloud connected cluster, do one of the following:

  * To apply a local storage schema to the cluster's control plane nodes, use the `--control-plane-node-storage-schema` flag when creating the cluster. For more information, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#create).

  * To apply a local storage schema to the cluster's worker nodes, use the `--node-storage-schema` when creating a node pool for the cluster. For more information, see [Create a node pool](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/nodepools#create).




Distributed Cloud connected creates the partitions defined in your local storage schema upon successful creation of the cluster or node pool.

### Default static local persistent volumes

Distributed Cloud connected ships with the following types of pre-provisioned default static local PersistentVolumes (PVs):

  * **`anthos-system` (97GiB)**: a pre-provisioned static local volume storage class in file system mode.
  * **`local-shared` (97GiB)**: a pre-provisioned static local volume storage class in file system mode.
  * **`local-disks`** : a pre-provisioned static local volume storage class in file system mode available on single-node deployments for customer workload storage. Unlike `local-shared`, these PVs are backed by dedicated physical partitions and are not logically overcommitted.
  * **`local-block`** : an unbound raw block device partition reserved for workload storage and Symcloud Storage volumes. The size of this partition depends on the underlying hardware storage capacity, consuming the remaining disk space after reserving space for system partitions. Typically, control plane nodes reserve 200 GiB (100 GiB system partition and 100 GiB etcd partition), while worker nodes reserve 100 GiB (for the system partition). The partition layout, slice offsets, and physical device boundaries of these raw block devices are fixed and immutable.



Each node's `local-shared` PVs are not accessible to other nodes in the cluster. Pods running on a node write to separate directories that reside on the same physical disk drive on that node. If you don't use Symcloud Storage, the unbound `local-block` raw block devices remain available on each node.

The `anthos-system` and `local-shared` static PVs are logically overcommitted and backed by the same single physical `~105 GB` system partition file system mounted at `/dev/mapper/shared_lpvs_encrypted` on each node. This architecture provides directory-level isolation for Google-managed system background services, such as logging, monitoring, and networking, without wasting physical disk capacity. These system PVs are over-provisioned to their maximum nominal capacity upfront because static local volume resizing requires data migration and recreating the affected PVs and PVCs.

#### Avoid using `local-shared` PVs for production workloads

Don't use `local-shared` PVs for production workloads. Because these PVs reside on the same physical disk drive as the Distributed Cloud connected system services, any workloads you deploy to use those PVs compete for space with the Distributed Cloud connected system itself.

If the system disk drive runs out of free space, the following happens:

  * Google-managed platform services and monitoring pods crash
  * Kubernetes triggers a hard `DiskPressure` state on the node
  * Kubernetes evicts all pods from the node



To prevent this, only use storage classes offered by Symcloud Storage for production workloads.

## Troubleshooting

If PersistentVolumeClaims remain pending unexpectedly or workloads fail to attach volumes, run the troubleshooting steps listed in this section.

### PersistentVolumeClaims remain pending

If your PersistentVolumeClaims remain in a `Pending` state, check the `volumeBindingMode` of your storage class. Pre-configured Symcloud Storage classes use `volumeBindingMode: WaitForFirstConsumer`, which delays volume provisioning until the Pod referencing the claim is scheduled. Ensure that your workload Pod is successfully scheduled.

If Pod scheduling is complete but the claim remains pending, or if volume attachment fails, verify the health of the Symcloud Storage control plane and node-level daemons.

### Verify control plane health

To verify that the Symcloud Storage control plane is healthy and ready to provision volumes, run the [kubectl describe](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/) command to check the status of the `RobinCluster` custom resource:
    
    
    kubectl describe robinclusters -n robinio
    

In the command output, verify that `Phase` is `Ready`.

### Verify storage daemon health

To verify that all node-level storage daemon Pods are running, run the [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command:
    
    
    kubectl get pods -n robinio
    

In the command output, ensure that all Pods are in the `Running` state. If a workload gets scheduled on a node with a failing storage daemon Pod, volume attachment hangs regardless of the central `RobinCluster` status.

### Contact support

If the Symcloud Storage control plane status is not `Ready` or any storage daemon Pods are not in the `Running` state, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/getting-support). When filing a support ticket, provide the outputs of the troubleshooting commands that you ran.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
