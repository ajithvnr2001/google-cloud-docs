---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing/
title: Train large-scale machine learning models on GKE with Multi-Tier Checkpointing \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:59.215993+00:00
---

# Train large-scale machine learning models on GKE with Multi-Tier Checkpointing  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Train large-scale machine learning models on GKE with Multi-Tier Checkpointing Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use Multi-Tier Checkpointing to reliably store and manage checkpoints during your machine learning model training on GKE. Checkpoint storage and management is crucial for _large-scale_ training jobs, defined as those utilizing over thousands of nodes. Interruptions to these large-scale jobs are frequent (potentially hourly) and recovery from them can be slow.

## Benefits

Using Multi-Tier Checkpointing provides the following benefits:

  * Fully orchestrated checkpoint data management, including backups, replication, and automatic restoration for the following workloads: 
    * [JAX training runs using Orbax for state management](https://cloud.google.com/blog/products/compute/unlock-faster-workload-start-time-using-orbax-on-jax) running on TPUs.
    * PyTorch workloads on GPUs.
  * Quick recovery of training jobs from a checkpoint stored in the local node. You can also recover using checkpoints stored in another node in the training cluster.
  * Quick restoration of training jobs from a checkpoint stored on a Cloud Storage backup in worst-case scenarios, where there are no in-cluster checkpoints.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets), if you don't have one for your project. Make sure you enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), otherwise backups will fail.



### Requirements

Multi-Tier Checkpointing requires GKE cluster version 1.32.4-gke.1415000 or later.

### Limitations

  * Autopilot clusters aren't supported.



## Configure GKE nodes for using Multi-Tier Checkpointing

This sections covers how to configure GKE nodes on new and existing clusters.

### Configure nodes on a new cluster

  1. Create a cluster with Multi-Tier Checkpointing, the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver), and [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled. If you use TPU slices for your machine learning workload, you'll need to [adjust the cluster creation command](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#prepare-standard-node-pool) to include the configuration for a TPU slice node pool.
         
         gcloud container clusters create CLUSTER_NAME \
             --addons=HighScaleCheckpointing,GcsFuseCsiDriver  \
             --node-locations=NODE_LOCATION \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --cluster-version=CLUSTER_VERSION
             --location=CLUSTER_LOCATION \
             --machine-type=MACHINE_TYPE \
             --num-nodes=NUM_NODES
         

Replace the following values:

     * `CLUSTER_NAME`: the name of the cluster.
     * `NODE_LOCATION`: the zone for your cluster nodes. This is where your TPU capacity lives.
     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_VERSION`: the version of your cluster. 1.32.4-gke.1415000 is the minimum supported version.
     * `CLUSTER_LOCATION`: the region that you want to create your cluster in.
     * `MACHINE_TYPE`: the machine type used for nodes that run components like the JobSet controller and the multi-tier checkpointing controller. For large-scale training, we recommend using at least `e2-standard-4` machines. You won't use this machine type for model training; instead, you'll create separate node pools for that purpose, often utilizing accelerator-optimized VM families.
     * `NUM_NODES`: the number of nodes to be created in each of the cluster's zones.



### Configure nodes on an existing cluster

To use Multi-Tier Checkpointing with an existing cluster, enable it together with the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver), and [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) with the following commands. Your existing cluster version needs to be later than 1.32.3-gke.1170000.

  1. Enable Workload Identity Federation for GKE:
         
         gcloud container clusters update CLUSTER_NAME \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --location=CLUSTER_LOCATION
         

Replace the following values:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_LOCATION`: the region of the cluster.
  2. Enable Multi-Tier Checkpointing and the Cloud Storage FUSE CSI driver:
         
         gcloud container clusters update CLUSTER_NAME \
             --update-addons=HighScaleCheckpointing=ENABLED,GcsFuseCsiDriver=ENABLED \
             --location=CLUSTER_LOCATION
         




## Configure permissions to use Multi-Tier Checkpointing

This section covers how to configure permissions to use Multi-Tier Checkpointing.

### Grant access to Cloud Storage buckets

The ephemeral volumes used by the Multi-Tier Checkpointing CSI driver must use existing Cloud Storage buckets.

To store checkpoints in a Cloud Storage bucket, Multi-Tier Checkpointing needs access to the bucket. Grant the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket to the [Kubernetes service account](https://kubernetes.io/docs/concepts/security/service-accounts/) for Multi-Tier Checkpointing.
    
    
    gcloud storage buckets add-iam-policy-binding gs://GCS_BUCKET \
        --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gke-managed-checkpointing/sa/gke-checkpointing-multitier-node" \
        --role "roles/storage.objectUser"
    

Replace the following values:

  * `GCS_BUCKET`: the name of the [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets) that you'll transfer data from.
  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. To find this value, refer to [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



### (Optional) Grant Compute Engine default service account access

If your Compute Engine instances need read access to the Cloud Storage bucket, grant the Storage Object Viewer (`roles/storage.objectViewer`) IAM role to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
    
    
    gcloud storage buckets add-iam-policy-binding gs://GCS_BUCKET \
        --member serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --role roles/storage.objectViewer
    

## Deploy the JobSet controller

The [JobSet controller](https://jobset.sigs.k8s.io/docs/overview/) is responsible for managing the batch jobs that run your model training on GKE, and its resource allocation is adjusted to handle the workload efficiently. Make sure that your training job launcher deploys and uses JobSet.

To increase the memory request to 1 Gi, the memory limit to 2 Gi, and the CPU request to 1 for the manager container in your JobSet deployment, run the following patch command:
    
    
    kubectl patch -n jobset-system deploy jobset-controller-manager --type json \
        --patch '[{"op": "add", "path": "/spec/template/spec/containers/0/resources", "value": {"limits": {"memory": "2Gi"}, "requests": {"cpu": "1", "memory": "1Gi"}}}]'
    

## Initialize the Multi-Tier Checkpointing CSI driver

This section describes how to initialize the Multi-Tier Checkpointing CSI driver on nodes where your workloads will run. The CSI driver is responsible for handling the storage and management of checkpoints during your model training process.

### Create a CheckpointConfiguration

A CheckpointConfiguration is a Kubernetes [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) that specifies properties for deploying the Multi-Tier Checkpointing CSI driver. This resource is cluster-scoped.

  1. Create the following `checkpoint.yaml` manifest.
         
         apiVersion: checkpointing.gke.io/v1
         kind: CheckpointConfiguration
         metadata:
           name: MTC_CONFIG_NAME-configuration
         spec:
             cloudStorageBucketName: GCS_BUCKET
             nodeSelector:
                 node.kubernetes.io/instance-type: MACHINE_TYPE
             tolerations:
             - key: TOLERATION_KEY
                 operator: Exists
                 effect: NoSchedule
             inMemoryVolumeSize: IN_MEMORY_VOLUME_SIZE
             gcsFuseMountOptions:
             - implicit-dirs
             - metadata-cache:negative-ttl-secs:0
             - metadata-cache:ttl-secs:-1
             - metadata-cache:stat-cache-max-size-mb:-1
             - metadata-cache:type-cache-max-size-mb:-1
             - file-system:kernel-list-cache-ttl-secs:0
             - read_ahead_kb=1024
             - write:enable-streaming-writes:true
         

Replace the following:

     * MTC_CONFIG_NAME: the name of your CheckpointConfiguration. This name is global for the cluster and is not job-specific.
     * GCS_BUCKET: the name of the Cloud Storage bucket where you'll store checkpoint data. Use the bucket that you set up in the Set up a Cloud Storage bucket with permissions step.
     * MACHINE_TYPE: the machine type for the corresponding accelerators. The value can be one of the following:

       * [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p): `ct5p-hightpu-4t`
       * [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e#v5e-types-for-serving): `ct5e-hightpu-4t`
       * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e#configurations): `ct6e-standard-4t`
       * Ironwood (TPU7x): `tpu7x-standard-4t`
       * NVIDIA H100 80GB GPUs (A3 series): 
         * [A3 High](https://docs.cloud.google.com/compute/docs/gpus#a3-high): `a3-highgpu-8g`
         * [A3 Mega](https://docs.cloud.google.com/compute/docs/gpus#a3-mega): `a3-megagpu-8g`
         * [A3 Ultra](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus): `a3-ultragpu-8g`

For more information on running distributed workloads on GPUs with GKE, see [Running multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi). For TPUs, see [Create the TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#create_node_pool).

     * TOLERATION_KEY: this field allows the CSI driver to be scheduled on nodes with matching [taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/). For more information about how taints work on different accelerator types, see these pages:

       * [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#how_tpus_work)
       * [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#taint)
     * IN_MEMORY_VOLUME_SIZE: the size for the in-memory checkpointing cache. Specify the quantity and unit (for example, 200 Gi).This value should be:

       * The local checkpoint size for TPUs multiplied by 2.2
       * The local checkpoint size for GPUs with a single peer multiplied by 6.6.
  2. Apply the manifest:
         
         kubectl apply -f checkpoint.yaml
         

  3. Check that the CSI driver is running:
         
         kubectl get pod -n gke-managed-checkpointing
         

The output should be similar to the following. There will be multiple entries, one per accelerated node.
         
         NAME                                                          READY   STATUS    RESTARTS   AGE
         multitier-driver-e2b033a7-a4e7-496a-87a3-ffd7fcc2e57b-2d4fz   5/5     Running   0          114s
         




### Uninstall the Multi-Tier Checkpointing CSI driver

If you want to undeploy the Multi-Tier Checkpointing CSI driver, delete the `CheckpointConfiguration` resource. The Multi-Tier Checkpointing controller removes the CSI driver from the nodes. This removes the RAM disks and frees up memory for other workloads. For example:
    
    
    kubectl delete -f checkpoint.yaml
    

## Manage data retention and garbage collection for Cloud Storage backups

You're responsible for implementing retention policies for the Cloud Storage backups of checkpoints. Multi-Tier Checkpointing only writes checkpoint backups to Cloud Storage and never modifies or deletes them.

Many open source tools can handle retention and garbage collection, including the following:

  * [`backup-warden`](https://github.com/charles-001/backup-warden)
  * [`logrotate`](https://linux.die.net/man/8/logrotate)



The following example uses `backup-warden` where the `backup` directory is mounted to a backup location that uses Cloud Storage FUSE:
    
    
    # Add --delete option to actually delete the backups, as is it only shows what would be deleted (dry-run)
    backup-warden -p backup \
        --hourly 24 \
        --daily 7 \
        --weekly 5 \
        --monthly always \
        --yearly always \
        --prefer-recent
    

### Update the workload JobSet manifest

Update the JobSet manifest for your job to include the large-scale checkpoint volume. The details depend on your workload.

For example, to extend the sample JobSet from [Deploy TPU Multislices in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#run_workload), do the following steps:

  1. Add the following lines to the `jax-tpu` container.
         
         volumeMounts:
         - name: checkpoint
           mountPath: CHECKPOINT_DIR
         

Replace CHECKPOINT_DIR with the path to your checkpoint directory. This is the location where the `replicator.yaml` is generated and Multi-Tier Checkpointing performs the checkpoint save operation. For more information, see Integrate Multi-Tier Checkpointing in your application.

  2. Add the following lines to the `spec.template.spec` field of the Job specification.
         
         volumes:
         - name: checkpoint
           csi:
             driver: multitier-checkpoint.csi.storage.gke.io
         




## Integrate Multi-Tier Checkpointing in your application

To share information about checkpoint locations and replication readiness, modify your application to use the following protocol to communicate with Multi-Tier Checkpointing.

The following frameworks and libraries already implement this integration:

  1. **[MaxText](https://github.com/AI-Hypercomputer/maxtext) (using [Orbax](https://github.com/google/orbax))**: MaxText has built-in support for Multi-Tier Checkpointing (MTC). For more information, see the [MaxText MTC documentation](https://maxtext.readthedocs.io/en/latest/guides/checkpointing_solutions/multi_tier_checkpointing.html).
  2. **[Any model using Orbax](https://github.com/google/orbax)** : The integration consists of two main components: the **[MTC initialization module](https://github.com/google/orbax/blob/28854db47c6d004061e2a8235c48e93f51a0bbd9/checkpoint/orbax/checkpoint/experimental/emergency/multi_tier_checkpointing/initialization.py#L73)** for initial setup (for an example, see [MaxText](https://github.com/AI-Hypercomputer/maxtext/blob/a6a5f32f63045ae1b09a65e7feee1d35dd4fbc36/src/MaxText/max_utils.py#L188)), and the **[Replicator Checkpoint Manager](https://github.com/google/orbax/blob/28854db47c6d004061e2a8235c48e93f51a0bbd9/checkpoint/orbax/checkpoint/experimental/emergency/replicator_checkpoint_manager.py#L114)** for saving and restoring checkpoints from a local RAM disk (for an example, see [MaxText](https://github.com/AI-Hypercomputer/maxtext/blob/a6a5f32f63045ae1b09a65e7feee1d35dd4fbc36/src/MaxText/train_utils.py#L39)).
  3. **[PyTorch reference example](https://github.com/AI-Hypercomputer/gpu-recipes/tree/main/training/a3mega/llama3-1-70b/nemo-pretraining-gke-resiliency)** : This example is available for workloads using NeMo with PyTorch.



### Startup

This section describes the initial steps the application needs to interact with Multi-Tier Checkpointing.

The _Replicator_ is a core component of Multi-Tier Checkpointing, running on every node as part of the CSI driver. The Replicator manages checkpoint replication across storage tiers, from the local RAM disk to peer nodes and to external storage like Cloud Storage.

The `replicator.yaml` file acts as a dynamic control plane between your ML training job (framework code) and the Replicator component. Your ML application programmatically generates this file on the local volume (RAMDisk), which is accessible by both the training job and the Replicator service. This manifest allows the ML framework to provide runtime configuration and lifecycle management instructions to the Replicator, distinct from static infrastructure parameters ( for example, Cloud Storage upload frequency) defined during backend setup.

For a concrete example of this interaction, see:

  * The [MaxText project](https://github.com/AI-Hypercomputer/maxtext), which utilizes this architecture for JAX on Cloud TPU.
  * The [PyTorch reference example](https://github.com/AI-Hypercomputer/gpu-recipes/tree/main/training/a3mega/llama3-1-70b/nemo-pretraining-gke-resiliency), which utilizes this architecture with PyTorch and NVIDIA NeMO on GPUs.



Your application should do the following steps during startup:

  1. Wait until the `replicator.yaml` file is absent, which indicates that the Replicator is ready to be configured by your application. The `replicator.yaml` file is generated in the CHECKPOINT_DIR location you configured in the Update the workload JobSet manifest section.

When the model training job is first created, the `replicator.yaml` file won't exist and your application can proceed immediately. However, if the job was restarted (for example, due to a failure or manual intervention), the system might still be processing the previous job instance, and the `replicator.yaml` from that instance might still be present on the local volume.

  2. You application or ML job creates the `replicator.yaml` file with the configuration similar to the following.

### Orbax
         
         job-name: orbax
         framework: orbax
         assume-data-parallelism: 3
         node-rank: 0
         nodes: 32
         peer-ranks: [1, 16] or peers-per-node: 2
         backup-interval-minutes: 30
         

### PyTorch
         
         job-name: nemo
         framework: pytorch.distributed
         node-rank: 0
         nodes: 32
         peer-ranks: [1, 16] or peers-per-node: 2
         backup-interval-minutes: 30
         

This example configuration has the following fields:

     * `name`: the name of the training job.
     * `framework`: the ML framework being used by the training job.
     * `node-rank`: the unique identifier of the current node within the distributed training job. This represents the node rank of the node creating this file. Each node participating in the run will have its own rank.
     * `nodes`: the total number of nodes participating in the distributed training job. This value comes from the Pod's metadata. The ML training job can also view this value.
     * `peer-ranks` or `peers-per-node`: two alternative ways to specify the replication topology. Only one of these two parameters should be present. 
       * `peer-ranks`: explicit ranks of peer nodes to which the current node's checkpoint data should be replicated. This gives fine-grained control over which specific nodes serve as replication partners.
       * `peers-per-node`: the number of peer nodes per node that the Replicator should automatically select for replication.
     * `backup-interval-minutes`: the frequency, in minutes, at which checkpoints are backed up to Cloud Storage. We recommend that you set this value to 30 minutes or more.
  3. Wait until the new `replicator.yaml` file is deleted by the system. This signals that the replicator has re-started and performed cleanup. This step lets you avoid any stale or temporary files on the local volume when your application performs the steps in the next section.




### Restore from the last known good (LKG) checkpoint

  1. After the replicator is initialized, Multi-Tier Checkpointing creates one symbolic link per TPU or GPU worker. These symbolic links are created in the same mounted local volume as `replicator.yaml` file, where the job saves checkpoints.

The symbolic links have the form `<job-name>-s{step}-n<node-rank>-w<worker-index>.restore`.

  2. Restore each worker from the corresponding `.restore` file. For an example, see the Orbax replicated checkpoint manager example in the next section.




By default, the LKG checkpoint is the most recent complete checkpoint that Multi-Tier Checkpointing can find. In-cluster checkpoints (on the local RAM disk and on peer nodes) are preferred, and Cloud Storage backups are used only when no complete in-cluster checkpoint exists. To override this selection, see Restore from a specific backup.

### Restore from a specific backup

You can restore a job from a specific Cloud Storage backup instead of the LKG checkpoint—for example, to roll back training to an earlier state. Before the job starts, do the following steps:

  1. Find the backup to restore from. Multi-Tier Checkpointing writes backups to the bucket that you configured in the CheckpointConfiguration, in a directory named after the job. Each backup is a subdirectory named after the UTC time when the backup was taken, in the format `YYYY-MM-DD_HH-MM`:
         
         gcloud storage ls gs://GCS_PATH/JOB_NAME/
         

Replace the following:

     * GCS_PATH: the Cloud Storage path where Multi-Tier Checkpointing writes backups. This value is the bucket that you specified in the `cloudStorageBucketName` field of the CheckpointConfiguration, including any directory within the bucket.
     * JOB_NAME: the name of the training job, as specified in the `job-name` field of the `replicator.yaml` file.
  2. In the job directory in the bucket, create a file named `restore.version`. The file must contain only the name of the backup directory, for example:
         
         echo "BACKUP_NAME" | gcloud storage cp - gs://GCS_PATH/JOB_NAME/restore.version
         

Replace BACKUP_NAME with the name of the backup directory— for example, `2025-06-30_14-30`.

  3. Start the job.




When the `restore.version` file is present, Multi-Tier Checkpointing behaves as follows:

  * All nodes restore from the specified backup. In-cluster checkpoints are ignored, even if they are more recent than the backup.
  * The `restore.version` file is deleted automatically after the job saves its first checkpoint after the restore. The override applies only once: if the job restarts later, it restores from the LKG checkpoint as usual.
  * If the specified backup doesn't exist or is incomplete, the job starts without a checkpoint. Multi-Tier Checkpointing doesn't fall back to in-cluster checkpoints or to other backups.



### Save the checkpoint

Your application performs these steps multiple times while the training job progresses. The save operations happen in the CHECKPOINT_DIR location you configured in the Update the workload JobSet manifest.

### Orbax

[Create Orbax checkpoints](https://orbax.readthedocs.io/en/latest/guides/checkpoint/orbax_checkpoint_101.html). The directory is named with the step number. The replicator detects the newly created checkpoint diretcory, performs replication or backup as needed, and cleans up automatically.

For more information about how to use the Orbax replicator checkpoint manager, see the [MaxText `checkpointing` file](https://github.com/AI-Hypercomputer/maxtext/blob/8706c206f30bb77d62fc97d4c991e57cc74842cc/MaxText/checkpointing.py#L116-L135). For an example of replicator service interaction, see the [MaxText `max_utils` file](https://github.com/AI-Hypercomputer/maxtext/blob/0fb6b666b77199fe86bc5fc4829d443d3bb2fc22/MaxText/max_utils.py#L326-L365).

### PyTorch

Use `InClusterLocalCheckpointIO` as a custom `pytorch_lightning.CheckpointIO` to enable correct distributed checkpointing with local storage. The following example command enables multi-tier checkpointing using a reference implementation built on the NVIDIA NeMo framework:
    
    
    torchrun train.py <other_train_flags> \
        --local-ckpt-dir=CHECKPOINT_DIR \
        --local-ckpt-interval=20 \
        --job-name=JOB_NAME \
        --enable-high-scale-ckpt
    

Replace the following:

  * `CHECKPOINT_DIR`: the path to your checkpoint directory.
  * `JOB_NAME`: the name of your training job workload.



## Cluster upgrades

For cluster upgrades, you can delete and re-create your `CheckpointConfiguration` object either before or after the upgrade. This action is required because the node checkpointing driver daemonset, deployed dynamically by this object, won't upgrade automatically.

If you specifically want to keep the daemonset specification the same, you don't need to do anything.

## Troubleshoot

This section provides troubleshooting guidance to resolve issues with Multi-Tier Checkpointing. For general storage troubleshooting, see [Troubleshooting Cloud Storage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage).

### Multi-Tier Checkpointing not enabled

The following error indicates that Multi-Tier Checkpointing is not enabled on your cluster:
    
    
    error: unable to recognize "checkpoint.yaml": no matches for kind "CheckpointConfiguration" in version "checkpointing.gke.io/v1"
    

You might encounter this error after running `kubectl apply -f checkpoint.yaml` in the Create a CheckpointConfiguration step.

To resolve this issue, check if you have enabled Multi-Tier Checkpointing on your cluster with the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --project PROJECT_ID
        --location CLUSTER_LOCATION
    

If Multi-Tier Checkpointing enabled, the output should be similar to the following:
    
    
    addonsConfig:
      gcePersistentDiskCsiDriverConfig:
        enabled: true
      gcsFuseCsiDriverConfig:
        enabled: true
      **highScaleCheckpointingConfig:
        enabled: true**
      kubernetesDashboard:
        disabled: true
      networkPolicyConfig:
        disabled: true
    

If Multi-Tier Checkpointing is not enabled, [update your cluster to enable Multi-Tier Checkpointing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing#existing-cluster).

### Multi-Tier Checkpointing CSI driver unable to mount volumes

You might encounter this issue if the CSI driver is unable to mount the Cloud Storage volume. There might be multiple lines similar to this.
    
    
    kubectl get pod -n gke-managed-checkpointing
    NAME                                                          READY   STATUS     RESTARTS   AGE
    multitier-driver-14694e4d-774f-4104-8bba-f0bd82fd7557-5vxr9   0/5     Init:0/1   0          6m32s
    

To resolve this issue, check the CSI driver Pod events, as shown in the following example:
    
    
    kubectl describe pod multitier-driver-14694e4d-774f-4104-8bba-f0bd82fd7557-5vxr9 -n gke-managed-checkpointing
    
    Events:
      Type     Reason       Age                 From               Message
      ----     ------       ----                ----               -------
      Normal   Scheduled    17m                 default-scheduler  Successfully assigned gke-managed-checkpointing/multitier-driver-14694e4d-774f-4104-8bba-f0bd82fd7557-5vxr9 to gke-my-cluster-default-pool-353c773f-6d8q
      Warning  FailedMount  82s (x16 over 17m)  kubelet            MountVolume.SetUp failed for volume "gcs" : rpc error: code = PermissionDenied desc = failed to get GCS bucket "checkpointing-test-bucket": googleapi: Error 403: Caller does not have storage.objects.list access to the Google Cloud Storage bucket. Permission 'storage.objects.list' denied on resource (or it may not exist)., forbidden
    

If the issue occurs because of Cloud Storage bucket `PermissionDenied` error, as shown in the example, you can resolve the problem by correctly setting up permissions.

## What's next

  * [Learn more about deploying TPU Multislice on Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice).
  * [Learn how to optimize the Cloud Storage FUSE CSI Driver for Google Kubernetes Engine for performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).
  * [Explore Orbax checkpointing options](https://orbax.readthedocs.io/en/latest/api_reference/checkpoint.options.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
