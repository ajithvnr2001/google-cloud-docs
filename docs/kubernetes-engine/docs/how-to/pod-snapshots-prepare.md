---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare/
title: Prepare for Pod snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:12.471882+00:00
---

# Prepare for Pod snapshots  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Prepare for Pod snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Learn how to enable and configure Google Kubernetes Engine (GKE) Pod snapshots on your cluster and set up Cloud Storage to store the snapshots.

For more information about how Pod snapshots work, see [About Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable Pod snapshots

To enable Pod snapshots, create or update a cluster with the Pod snapshot feature enabled. For Standard clusters, you must also create or update a node pool to run in GKE Sandbox. GKE Sandbox is supported by default with Autopilot clusters.

**Note:** Your cluster must have Workload Identity Federation for GKE enabled. For more information, see [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). Workload Identity Federation for GKE is always enabled in Autopilot clusters.

To enable Pod snapshots on a cluster, complete one of the following procedures, depending on the GKE mode of operation that you want to use:

###  Autopilot 

  * To enable Pod snapshots on a new cluster, run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME \
              --enable-pod-snapshots \
              --location=CONTROL_PLANE_LOCATION \
              --cluster-version=CLUSTER_VERSION
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
    * `CLUSTER_VERSION`: the version of your new cluster, which must be 1.35.3-gke.1234000 or later.
  * To enable Pod snapshots on an existing cluster, complete the following steps:

    1. Upgrade the cluster to version 1.35.3-gke.1234000 or later:
           
           gcloud container clusters upgrade CLUSTER_NAME \
                 --cluster-version=CLUSTER_VERSION \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
       * `CLUSTER_VERSION`: the version of your new cluster, which must be 1.35.3-gke.1234000 or later.
    2. Enable Pod snapshots on your cluster:
           
           gcloud container clusters update CLUSTER_NAME \
                 --enable-pod-snapshots \
                 --location=CONTROL_PLANE_LOCATION
           

Default `whole-pod` scope Pod snapshots don't support E2 machine types. In Autopilot, GKE might default to machine types that don't support Pod snapshots. If you use `whole-pod` scope snapshots, to help ensure that your workloads run on compatible hardware, you should use a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes) to prioritize compatible machine families. File system snapshots (`rootfs-only`) support E2 machine types.




To create and use a custom ComputeClass, complete the following steps:

  1. Save the following manifest as `non-e2-class.yaml`:
         
         apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: non-e2-class
           spec:
             priorities:
             - machineFamily: n2
             - machineFamily: c3
             activeMigration:
               optimizeRulePriority: false
             whenUnsatisfiable: DoNotScaleUp
         

  2. Apply the manifest:
         
         kubectl apply -f non-e2-class.yaml
         

  3. In your Pod specification, reference the ComputeClass by using the `cloud.google.com/compute-class` node selector:
         
         spec:
             nodeSelector:
               cloud.google.com/compute-class: non-e2-class
             ...
         




###  Standard 

  * To enable Pod snapshots on a new cluster, run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
              --enable-pod-snapshots \
              --cluster-version=CLUSTER_VERSION \
              --workload-pool=PROJECT_ID.svc.id.goog \
              --workload-metadata=GKE_METADATA \
              --location=CONTROL_PLANE_LOCATION
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `CLUSTER_VERSION`: the version of your new cluster, which must be 1.35.3-gke.1234000 or later.
    * `PROJECT_ID`: your project ID.
    * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  * To enable Pod snapshots on an existing cluster, complete the following steps:

    1. Upgrade the cluster to version 1.35.3-gke.1234000 or later:
           
           gcloud container clusters upgrade CLUSTER_NAME \
                 --node-pool=NODEPOOL_NAME \
                 --cluster-version=CLUSTER_VERSION \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `NODEPOOL_NAME`: the name of your node pool.
       * `CLUSTER_VERSION`: the version to update your new cluster, which must be 1.35.3-gke.1234000 or later.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
    2. Enable Pod snapshots on your cluster:
           
           gcloud beta container clusters update CLUSTER_NAME \
               --enable-pod-snapshots \
               --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



To run Pods in GKE Sandbox on a Standard cluster, create or update a node pool with gVisor enabled. To update a node pool, use the `--sandbox type=gvisor` flag. To create a node pool with gVisor enabled, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
      --cluster=CLUSTER_NAME \
      --node-version=NODE_VERSION \
      --machine-type=MACHINE_TYPE \
      --location=CONTROL_PLANE_LOCATION \
      --image-type=cos_containerd \
      **--sandbox type=gvisor**
    

Replace the following variables:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `NODE_VERSION`: the version to use for the node pool.
  * `MACHINE_TYPE`: the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types) to use for the nodes.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



For more information about using gVisor, see [Isolate your workloads using GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enabling-existing).

## Store snapshots

Pod snapshots are stored in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets), which contains the memory and (optionally) GPU state. Pod snapshots require [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to enable and use the Pod's service account to authenticate to Cloud Storage.

Pod snapshots require the following configuration for the bucket:

  * [Hierarchical namespaces](https://docs.cloud.google.com/storage/docs/hns-overview): these must be enabled to allow for higher read and write queries per second. Hierarchical namespaces also require that [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled.
  * [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete): because Pod snapshots use [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads), you should disable data protection features like soft delete. If these features are left enabled, soft deletions of the temporary objects can increase your storage bill significantly.
  * [Location](https://docs.cloud.google.com/storage/docs/locations): the Cloud Storage bucket location must be the same location as the GKE cluster because performance might be impacted if snapshots are transferred across different regions.



To create both the required bucket and permissions, complete the following steps:

  1. Create a Cloud Storage bucket. The following command creates a bucket with the required configuration:
         
         gcloud storage buckets create "gs://BUCKET_NAME" \
            --uniform-bucket-level-access \
            --enable-hierarchical-namespace \
            --soft-delete-duration=0d \
            --location="LOCATION"
         

Replace the following:

     * `BUCKET_NAME`: the name of your bucket.
     * `LOCATION`: the location of your bucket.

For a complete list of options for bucket creation, see [`buckets create` options](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#FLAGS).




## Grant workloads access to the Cloud Storage bucket

By default, GKE doesn't have access to Cloud Storage. To read and write snapshot files, you must grant an IAM role that contains the corresponding permissions to the Kubernetes ServiceAccount (KSA) used by your workload Pods, or grant short-lived tokens.

### Grant roles to specific Kubernetes ServiceAccounts

  1. Get credentials so that you can communicate with your cluster with `kubectl` commands:
         
         gcloud container clusters get-credentials "CLUSTER_NAME"
         

  2. For each Pod, complete the following steps:

     1. Create a KSA for each Pod:
            
            kubectl create serviceaccount "KSA_NAME" \
                --namespace "NAMESPACE"
            

Replace the following:

        * `KSA_NAME`: the name of your KSA.
        * `NAMESPACE`: the namespace for your Pods.
     2. Grant the KSA permission to access the bucket:
            
            gcloud storage buckets add-iam-policy-binding "gs://BUCKET_NAME" \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
                --role="roles/storage.bucketViewer"
            
            
            gcloud storage buckets add-iam-policy-binding "gs://BUCKET_NAME" \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
                --role="roles/storage.objectUser"
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
        * `NAMESPACE`: the namespace for your Pods.
        * `KSA_NAME`: the name of your KSA.



### Enable multi-tenancy using short-lived tokens

As an alternative to granting permissions to individual KSAs, you can enable multi-tenancy with short-lived, scope-restricted tokens. This approach helps to avoid the propagation delay associated with manual IAM bindings. Instead of granting permissions to each KSA, you perform a one-time grant of the `roles/storage.admin` role on the snapshot storage bucket to the GKE node service account. The node service account then creates short-lived tokens on-demand for specific paths.

Enabling tokens with Pod snapshots requires GKE version 1.35.3-gke.1737000 or later.

To enable multi-tenancy, complete the following steps:

  1. To grant the node service account permission to access the bucket, run the following command:
         
         gcloud storage buckets add-iam-policy-binding "gs://BUCKET_NAME" \
             --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com" \
             --role="roles/storage.admin"
         

  2. When you configure storage for snapshots, set the value of the `tokenSource` field to `federatedP4SA`.




## Grant the Pod snapshot controller access to the Cloud Storage bucket

To allow the Pod snapshot controller to delete snapshots inside the Cloud Storage bucket, the GKE Service agent needs to be granted the Storage Object User (`roles/storage.objectUser`) role on the project. Grant the `roles/storage.objectUser` role by running the following command:
    
    
    gcloud projects add-iam-policy-binding "PROJECT_ID" \
      --member="serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
      --role="roles/storage.objectUser" \
      --condition="expression=resource.name.startsWith(\"projects/_/buckets/BUCKET_NAME\"),title=restrict_to_bucket,description=Restricts access to one bucket only"
    

Replace the following:

  * `PROJECT_NUMBER`: your project number.
  * `PROJECT_ID`: your project ID.
  * `BUCKET_NAME`: the name of your bucket.



## (Optional) Create managed folders for the Cloud Storage bucket

Creating folders lets you isolate permissions for snapshots from mutually untrusted Pods, which is useful in multi-tenant use cases. To set up managed folders, complete the following steps:

  1. Create a custom IAM role that contains only the necessary permissions for Pod snapshots:
         
         gcloud iam roles create podSnapshotGcsReadWriter \
             --project="PROJECT_ID" \
             --permissions="storage.objects.get,storage.objects.create,storage.objects.delete,storage.folders.create"
         

  2. Grant the `roles/storage.bucketViewer` role to all KSAs in the target namespace. This role lets KSAs read bucket metadata, but does not grant read or write permissions to objects in the bucket.
         
         gcloud storage buckets add-iam-policy-binding "gs://BUCKET_NAME" \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/namespace/NAMESPACE" \
             --role="roles/storage.bucketViewer"
         

Replace the following:

     * `BUCKET_NAME`: the name of your bucket.
     * `PROJECT_NUMBER`: your project number.
     * `PROJECT_ID`: your project ID.
     * `NAMESPACE`: the namespace for your Pods.
  3. For each KSA that needs to store Pod snapshots, complete the following steps:

     1. Create a managed folder for the KSA:
            
            gcloud storage managed-folders create "gs://BUCKET_NAME/FOLDER_PATH/"
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `FOLDER_PATH`: the path for the managed folder, for example `my-app-snapshots`.
     2. Grant the KSA the custom `podSnapshotGcsReadWriter` role on the managed folder:
            
            gcloud storage managed-folders add-iam-policy-binding "gs://BUCKET_NAME/FOLDER_PATH/" \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
                --role="projects/PROJECT_ID/roles/podSnapshotGcsReadWriter"
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `FOLDER_PATH`: the path for the managed folder, for example `my-app-snapshots`.
        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
        * `NAMESPACE`: the namespace for your Pods.
        * `KSA_NAME`: the name of your KSA.
**Note:** IAM policies can take several minutes to populate in GKE.



## Configure storage for snapshots

To specify where to store snapshot files, create a PodSnapshotStorageConfig resource.

  1. The following example configures GKE to store Pod snapshots in the `FOLDER_PATH/` path inside the Cloud Storage bucket BUCKET_NAME. Save the following manifest as `example-pod-snapshot-storage-config`:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotStorageConfig
         metadata:
           name: example-pod-snapshot-storage-config
         spec:
           snapshotStorageConfig:
             gcs:
               bucket: "BUCKET_NAME"
               path: "FOLDER_PATH"
               tokenSource: "TOKEN_SOURCE"
         

Replace the following:

     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `FOLDER_PATH`: the path for the Cloud Storage managed folder.
     * `TOKEN_SOURCE`: the identity provider for access. Use `podKSA` (default) or `federatedP4SA` for multi-tenancy.
  2. Apply the manifest:
         
         kubectl apply -f example-pod-snapshot-storage-config.yaml
         




## What's next

  * Learn how to [trigger a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
