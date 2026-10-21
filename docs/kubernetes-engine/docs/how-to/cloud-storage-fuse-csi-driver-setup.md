---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup/
title: Set up the Cloud Storage FUSE CSI driver for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:07.585262+00:00
---

# Set up the Cloud Storage FUSE CSI driver for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Set up the Cloud Storage FUSE CSI driver for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to set up the Cloud Storage FUSE CSI driver to access Cloud Storage buckets from Google Kubernetes Engine (GKE). 

With the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver), your GKE workloads can access Cloud Storage buckets as a local file system. The CSI driver integrates Cloud Storage with GKE, and simplifies how your containerized applications interact with large datasets stored in buckets. The CSI driver provides a standard interface for GKE storage. In this document, you prepare your environment and connect your GKE clusters to Cloud Storage buckets by using the Cloud Storage FUSE CSI driver.

This document is for developers, administrators, and storage specialists who integrate GKE workloads with object storage. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Create the Cloud Storage bucket

If you have not already done so, [create your Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets). You will mount these buckets as volumes in your GKE cluster. To improve performance, set the [Location type](https://docs.cloud.google.com/storage/docs/locations) to **Region** , and select a region that matches your GKE cluster.

**Tip:** Your Cloud Storage buckets and GKE clusters can be in different Google Cloud projects, or in the same project.

## Enable the Cloud Storage FUSE CSI driver

Follow these steps, depending on whether you are using GKE Autopilot or Standard clusters. We recommend that you use an Autopilot cluster for a fully managed Kubernetes experience. To choose the mode that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

The Cloud Storage FUSE CSI driver is enabled by default for Autopilot clusters. You can skip to Configure access to Cloud Storage buckets.

### Standard

If your Standard cluster has Cloud Storage FUSE CSI driver enabled, skip to Configure access to Cloud Storage buckets.

The Cloud Storage FUSE CSI driver is not enabled by default in Standard clusters. To create a Standard cluster with the Cloud Storage FUSE CSI driver enabled, you can use the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --addons GcsFuseCsiDriver \
        --cluster-version=VERSION \
        --location=LOCATION \
        --workload-pool=PROJECT_ID.svc.id.goog
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `VERSION`: the GKE version number. You must select 1.24 or later.
  * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  * `PROJECT_ID`: your project ID.



To enable the driver on an existing Standard cluster, use the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --update-addons GcsFuseCsiDriver=ENABLED \
        --location=LOCATION
    

To verify that the Cloud Storage FUSE CSI driver is enabled on your cluster, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID \
        --format="value(addonsConfig.gcsFuseCsiDriverConfig.enabled)"
    

## Configure access to Cloud Storage buckets

The Cloud Storage FUSE CSI driver uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) so that you can set fine grained permissions on how your GKE Pods can access data stored in Cloud Storage.

To make your Cloud Storage buckets accessible by your GKE cluster, authenticate using Workload Identity Federation for GKE with the Cloud Storage bucket that you want to mount in your Pod specification:

  1. If you don't have Workload Identity Federation for GKE enabled, follow [these steps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) to enable it. If you want to use an existing node pool, [manually enable Workload Identity Federation for GKE on your node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#option_2_node_pool_modification) after enabling Workload Identity Federation for GKE on your cluster.
  2. Get credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster that has Workload Identity Federation for GKE enabled.
     * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  3. Create a namespace to use for the [Kubernetes ServiceAccount](https://kubernetes.io/docs/concepts/security/service-accounts/). You can also use the `default` namespace or any existing namespace.
         
         kubectl create namespace NAMESPACE
         

Replace `NAMESPACE` with the name of the Kubernetes namespace for the Kubernetes ServiceAccount.

**Important:** Your workload **must** run in the same namespace.
  4. Create a Kubernetes ServiceAccount for your application to use. You can also use any existing Kubernetes ServiceAccount in any namespace, including the `default` Kubernetes ServiceAccount.
         
         kubectl create serviceaccount KSA_NAME \
             --namespace NAMESPACE
         

Replace `KSA_NAME` with the name of your Kubernetes ServiceAccount.

  5. Grant one of the [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the Kubernetes ServiceAccount. Follow these steps, depending on whether you are granting the Kubernetes ServiceAccount access to a specific Cloud Storage bucket only, or global access to all buckets in the project.

### Specific bucket access
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
             --role "ROLE_NAME"
         

Replace the following:

     * `BUCKET_NAME`: your Cloud Storage bucket name.
     * `PROJECT_NUMBER`: the numerical project number of your GKE cluster. To find your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `PROJECT_ID`: the project ID of your GKE cluster.
     * `NAMESPACE`: the name of the Kubernetes namespace for the Kubernetes ServiceAccount.
     * `KSA_NAME`: the name of your new Kubernetes ServiceAccount.
     * `ROLE_NAME`: the IAM role to assign to your Kubernetes ServiceAccount. 
       * For read-only workloads, use the Storage Object Viewer role (`roles/storage.objectViewer`).
       * For read-write workloads, use the Storage Object User role (`roles/storage.objectUser`).

### Global bucket access
    
    gcloud projects add-iam-policy-binding GCS_PROJECT \
        --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
        --role "ROLE_NAME"
    

Replace the following:

     * `GCS_PROJECT`: the project ID of your Cloud Storage buckets.
     * `PROJECT_NUMBER`: the numerical project number of your GKE cluster. To find your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `PROJECT_ID`: the project ID of your GKE cluster.
     * `NAMESPACE`: the name of the Kubernetes namespace for the Kubernetes ServiceAccount.
     * `KSA_NAME`: the name of your new Kubernetes ServiceAccount.
     * `ROLE_NAME`: the IAM role to assign to your Kubernetes ServiceAccount. 
       * For read-only workloads, use the Storage Object Viewer role (`roles/storage.objectViewer`).
       * For read-write workloads, use the Storage Object User role (`roles/storage.objectUser`).




## Configure access for Pods with host network

For GKE cluster versions earlier than `1.33.3-gke.1226000`, the Cloud Storage FUSE CSI driver does not support Pods running on the [host network](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#hosts-namespaces) (`hostNetwork: true`) due to [restrictions of Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#restrictions). However, for later GKE versions, you can configure secure authentication for `hostNetwork` enabled Pods when you use the Cloud Storage FUSE CSI driver to mount Cloud Storage buckets. The host network support is available only on Standard GKE clusters.

Make sure that your GKE cluster meets the following requirements:

  * Both the control plane and node pools in your Standard GKE cluster must have a version `1.33.3-gke.1226000` or later.
  * [Enable Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) on your cluster.
  * Grant the necessary [IAM permissions](https://docs.cloud.google.com/iam/docs/understanding-roles) to the Kubernetes Service Account that your `hostNetwork`-enabled Pod uses to access your Cloud Storage bucket. For more information, see [Authenticate to Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).



You specify the volume attribute `hostNetworkPodKSA: "true"` in your Pod or PersistentVolume definition to enable your `HostNetwork` Pods to access Cloud Storage volumes. The exact configuration differs based on how you manage the Cloud Storage FUSE sidecar container.

### Managed sidecars

This section applies if GKE automatically injects and manages the Cloud Storage FUSE sidecar container into your Pods. This option is the default and recommended setup for the Cloud Storage FUSE CSI driver.

### Ephemeral volume

The following Pod manifest configures an ephemeral volume for a `HostNetwork` Pod to access a Cloud Storage bucket.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod
      namespace: ns1
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      serviceAccountName: test-ksa-ns1
      hostNetwork: true
      containers:
      - image: busybox
        name: busybox
        command:
          - sleep
          - "3600"
        volumeMounts:
        - name: gcs-fuse-csi-ephemeral
          mountPath: /data
      volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: test-bucket
            hostNetworkPodKSA: "true"
    

### Persistent volume

The following PV manifest configures a PV for a `HostNetwork` Pod to access a Cloud Storage bucket.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: gcp-cloud-storage-csi-pv
    spec:
    accessModes:
    - ReadWriteMany
    capacity:
      storage: 5Gi
    persistentVolumeReclaimPolicy: Retain
    # storageClassName does not need to refer to an existing StorageClass object.
    storageClassName: test-storage-class
    mountOptions:
      - uid=1001
      - gid=3003
    csi:
      driver: gcsfuse.csi.storage.gke.io
      volumeHandle: test-wi-host-network-2
      volumeAttributes:
        hostNetworkPodKSA: "true"
    

### Private sidecars

This section applies if you manually manage the Cloud Storage FUSE sidecar container within your Pods or use a custom sidecar image.

Make sure that your sidecar image is based on Cloud Storage FUSE CSI driver version [v1.17.2 or later](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/tree/v1.17.2).

### Ephemeral volume

The following Pod manifest configures an ephemeral volume for a `HostNetwork` Pod to access a Cloud Storage bucket.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod
      namespace: ns1
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      serviceAccountName: test-ksa-ns1
      hostNetwork: true
      containers:
      - image: busybox
        name: busybox
        command:
          - sleep
          - "3600"
        volumeMounts:
        - name: gcs-fuse-csi-ephemeral
          mountPath: /data
      volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: test-bucket
            hostNetworkPodKSA: "true"
            identityProvider: "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME"
    

In the `identityProvider` field, replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the location of your cluster.
  * `CLUSTER_NAME`: the name of your Standard GKE cluster.



### Persistent volume

The following PV manifest configures a PV for a `HostNetwork` Pod to access a Cloud Storage bucket.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: gcp-cloud-storage-csi-pv
    spec:
    accessModes:
    - ReadWriteMany
    capacity:
      storage: 5Gi
    persistentVolumeReclaimPolicy: Retain
    # storageClassName does not need to refer to an existing StorageClass object.
    storageClassName: test-storage-class
    mountOptions:
      - uid=1001
      - gid=3003
    csi:
      driver: gcsfuse.csi.storage.gke.io
      volumeHandle: test-wi-host-network-2
      volumeAttributes:
        hostNetworkPodKSA: "true"
        identityProvider: "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME"
    

In the `identityProvider` field, replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the location of your cluster.
  * `CLUSTER_NAME`: the name of your Standard GKE cluster.



## What's next

  * [Troubleshoot Cloud Storage FUSE ](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md)
  * [Learn how to mount Cloud Storage buckets by specifying your buckets in-line with the Pod specification.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral)
  * [Learn how to mount Cloud Storage buckets using a PersistentVolume resource.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv)
  * [Learn more about configuring applications to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).
  * [Automatically optimize performance with Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles).
  * [Manually optimize Cloud Storage FUSE for performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
