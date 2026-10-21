---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare/
title: Prepare for Pod snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:23.506989+00:00
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

Google Kubernetes Engine (GKE) Pod snapshots let you save and restore running Pod states to improve workload startup latency. Before you can capture snapshots of your workloads, you must prepare your cluster and storage environment.

Use this document to learn how to enable and configure Pod snapshots on your cluster and set up Cloud Storage to store the snapshots. For more information about how Pod snapshots work, see [About GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots).

Platform admins and operators and Application developers can use this document to configure clusters, create storage buckets, and set up access permissions for Pod snapshots. For more information about the common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable Pod snapshots

You can enable Pod snapshots on a new or existing cluster. Pod snapshots require GKE Sandbox and [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). Autopilot clusters enable both features by default. For Standard clusters, you must enable Workload Identity Federation for GKE on the cluster and configure a node pool to run in GKE Sandbox.

To enable Pod snapshots on a cluster, follow the steps for the GKE mode of operation that you want to use:

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
  * To enable Pod snapshots on an existing cluster, follow these steps:

    1. Upgrade the cluster to version 1.35.3-gke.1234000 or later:
           
           gcloud container clusters upgrade CLUSTER_NAME \
                 --cluster-version=CLUSTER_VERSION \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CLUSTER_VERSION`: the version to upgrade your cluster to, which must be 1.35.3-gke.1234000 or later.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
    2. Enable Pod snapshots on your cluster:
           
           gcloud container clusters update CLUSTER_NAME \
                 --enable-pod-snapshots \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



Pod snapshots with the default `whole-pod` scope don't support E2 machine types, whereas file system snapshots (`rootfs-only`) do. In Autopilot clusters, GKE might schedule Pods on E2 nodes by default. If you use the `whole-pod` scope, use a [ComputeClass custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes) to help ensure that your workloads run on compatible hardware.

To create and use a ComputeClass custom resource, follow these steps:

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
         

  3. In your Pod specification, reference the ComputeClass custom resource by using the `cloud.google.com/compute-class` node selector:
         
         spec:
             nodeSelector:
               cloud.google.com/compute-class: non-e2-class
             # Multiple lines are omitted here
         




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
  * To enable Pod snapshots on an existing cluster, follow these steps:

    1. Upgrade the cluster to version 1.35.3-gke.1234000 or later:
           
           gcloud container clusters upgrade CLUSTER_NAME \
                 --node-pool=NODE_POOL_NAME \
                 --cluster-version=CLUSTER_VERSION \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `NODE_POOL_NAME`: the name of your node pool.
       * `CLUSTER_VERSION`: the version to upgrade your cluster to, which must be 1.35.3-gke.1234000 or later.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
    2. Enable Pod snapshots on your cluster:
           
           gcloud beta container clusters update CLUSTER_NAME \
                 --enable-pod-snapshots \
                 --location=CONTROL_PLANE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



To run Pods in GKE Sandbox on a Standard cluster, you must create or update a node pool with GKE Sandbox enabled. To update a node pool, use the `--sandbox type=gvisor` flag. To create a node pool with GKE Sandbox enabled, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --node-version=NODE_VERSION \
        --machine-type=MACHINE_TYPE \
        --location=CONTROL_PLANE_LOCATION \
        --image-type=cos_containerd \
        --sandbox type=gvisor
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `NODE_VERSION`: the version to use for the node pool.
  * `MACHINE_TYPE`: the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types) to use for the nodes.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



For more information about GKE Sandbox, see [Harden workload isolation with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enabling-existing).

## Store snapshots

GKE stores Pod snapshots in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets). Each snapshot contains the application memory and, optionally, the GPU state of the Pod. To authenticate to Cloud Storage, Pod snapshots use the Pod's ServiceAccount object, which requires [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

Pod snapshots require the following bucket configurations:

  * **[Hierarchical namespaces](https://docs.cloud.google.com/storage/docs/hns-overview)** : you must enable hierarchical namespaces to support higher read and write queries per second. Hierarchical namespaces also require that you enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
  * **[Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete)** : because Pod snapshots use [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads), disable data protection features like soft delete. If you leave these features enabled, then soft deletions of the temporary objects can increase your storage bill significantly.
  * **[Location](https://docs.cloud.google.com/storage/docs/locations)** : the Cloud Storage bucket location must be in the same location as the GKE cluster because transferring snapshots across different regions might affect performance.



To create a bucket with the required configurations, run the following command:
    
    
    gcloud storage buckets create gs://BUCKET_NAME \
        --uniform-bucket-level-access \
        --enable-hierarchical-namespace \
        --soft-delete-duration=0d \
        --location=LOCATION
    

Replace the following:

  * `BUCKET_NAME`: the name of your bucket.
  * `LOCATION`: the location of your bucket.



For a complete list of options for bucket creation, see [Flags](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#FLAGS) in the documentation for the `buckets create` command.

## Grant workloads access to the Cloud Storage bucket

By default, GKE doesn't have access to Cloud Storage. To read and write Pod snapshots, you must grant an IAM role that contains the corresponding permissions to the Kubernetes ServiceAccount object that your workload Pods use, or enable multi-tenancy using short-lived tokens.

### Grant roles to specific Kubernetes ServiceAccount objects

To grant roles to specific Kubernetes ServiceAccount objects, follow these steps:

  1. To communicate with your cluster by using `kubectl` commands, get credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  2. For each Pod, follow these steps:

     1. Create a ServiceAccount object:
            
            kubectl create serviceaccount SERVICEACCOUNT_NAME \
                --namespace=NAMESPACE
            

Replace the following:

        * `SERVICEACCOUNT_NAME`: the name of your ServiceAccount object.
        * `NAMESPACE`: the namespace for your Pods.
     2. To let the ServiceAccount object read bucket metadata, grant it the [Storage Bucket Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`):
            
            gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/SERVICEACCOUNT_NAME" \
                --role="roles/storage.bucketViewer"
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
        * `NAMESPACE`: the namespace for your Pods.
        * `SERVICEACCOUNT_NAME`: the name of your ServiceAccount object.
     3. To let the ServiceAccount object read and write snapshot objects in the bucket, grant it the [Storage Object User role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`):
            
            gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/SERVICEACCOUNT_NAME" \
                --role="roles/storage.objectUser"
            




### Enable multi-tenancy using short-lived tokens

As an alternative to granting permissions to individual ServiceAccount objects, you can enable multi-tenancy with short-lived, scope-restricted tokens. This approach helps to avoid the propagation delay associated with manual IAM bindings. Instead of granting permissions to each ServiceAccount object, you perform a one-time grant of the [Storage Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the snapshot storage bucket to the GKE node service account. The node service account then creates short-lived tokens on demand for specific paths.

Enabling tokens with Pod snapshots requires GKE version 1.35.3-gke.1737000 or later.

To enable multi-tenancy, follow these steps:

  1. To grant the node service account permission to use the bucket, run the following command:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com" \
             --role="roles/storage.admin"
         

Replace the following:

     * `BUCKET_NAME`: the name of your bucket.
     * `PROJECT_NUMBER`: your project number.
  2. When you configure storage for snapshots, set the value of the `tokenSource` field to `federatedP4SA`.




## Grant the Pod snapshot controller access to the Cloud Storage bucket

To let the Pod snapshot controller delete snapshots inside the Cloud Storage bucket, you must grant the [Storage Object User role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) to the GKE service agent on the project. To grant the role, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
        --role="roles/storage.objectUser" \
        --condition="expression=resource.name.startsWith(\"projects/_/buckets/BUCKET_NAME\"),title=restrict_to_bucket,description=Restricts access to one bucket only"
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `PROJECT_NUMBER`: your project number.
  * `BUCKET_NAME`: the name of your bucket.



## Optional: Create managed folders for the Cloud Storage bucket

To isolate permissions for snapshots from mutually untrusted Pods, which is useful in multi-tenant use cases, create managed folders. To set up managed folders, follow these steps:

  1. Create a custom IAM role that contains only the necessary permissions for Pod snapshots:
         
         gcloud iam roles create podSnapshotGcsReadWriter \
             --project=PROJECT_ID \
             --permissions="storage.objects.get,storage.objects.create,storage.objects.delete,storage.folders.create"
         

Replace `PROJECT_ID` with your project ID.

  2. Grant the [Storage Bucket Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`) to all ServiceAccount objects in the target namespace. This role lets the ServiceAccount objects read bucket metadata, but doesn't grant them permissions to read or write the objects in the bucket.
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/namespace/NAMESPACE" \
             --role="roles/storage.bucketViewer"
         

Replace the following:

     * `BUCKET_NAME`: the name of your bucket.
     * `PROJECT_NUMBER`: your project number.
     * `PROJECT_ID`: your project ID.
     * `NAMESPACE`: the namespace for your Pods.
  3. For each ServiceAccount object that needs to store Pod snapshots, follow these steps:

     1. Create a managed folder for the ServiceAccount object:
            
            gcloud storage managed-folders create gs://BUCKET_NAME/FOLDER_PATH/
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `FOLDER_PATH`: the path for the managed folder (for example, `my-app-snapshots`).
     2. Grant the ServiceAccount object the custom `podSnapshotGcsReadWriter` role on the managed folder:
            
            gcloud storage managed-folders add-iam-policy-binding gs://BUCKET_NAME/FOLDER_PATH/ \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/SERVICEACCOUNT_NAME" \
                --role="projects/PROJECT_ID/roles/podSnapshotGcsReadWriter"
            

Replace the following:

        * `BUCKET_NAME`: the name of your bucket.
        * `FOLDER_PATH`: the path for the managed folder (for example, `my-app-snapshots`).
        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
        * `NAMESPACE`: the namespace for your Pods.
        * `SERVICEACCOUNT_NAME`: the name of your ServiceAccount object.
**Note:** IAM policies can take several minutes to take effect in GKE.



## Configure storage for snapshots

To specify where to store Pod snapshots, create a PodSnapshotStorageConfig custom resource:

  1. Save the following manifest as `example-pod-snapshot-storage-config.yaml`. This example configures GKE to store Pod snapshots in the `FOLDER_PATH/` path inside the Cloud Storage bucket `BUCKET_NAME`:
         
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

Learn how to [trigger a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
