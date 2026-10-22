---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar/
title: Configure the Cloud Storage FUSE CSI driver sidecar container for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:17.606205+00:00
---

# Configure the Cloud Storage FUSE CSI driver sidecar container for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure the Cloud Storage FUSE CSI driver sidecar container for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to configure resource settings for the Cloud Storage FUSE CSI driver sidecar container in Google Kubernetes Engine (GKE).

To optimize your application's performance and resource use in GKE, configure specific resource settings for the Cloud Storage FUSE CSI driver sidecar container. By setting up these resources—such as a private image, a custom write buffer, and a custom read cache volume—you can gain more control over how your applications interact with Cloud Storage. These configurations can lead to faster data access, quicker processing times, and potentially reduce overall resource consumption in your GKE clusters.

This document is for developers, administrators, and architects who optimize application performance. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before you begin, familiarize yourself with the following workload and storage concepts:

  * [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver)
  * [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/key-terms#buckets)
  * [Deployments and Kubernetes Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes)



## How the sidecar container works

The Cloud Storage FUSE CSI driver uses a sidecar container to mount Cloud Storage buckets to make them accessible as local file systems to Kubernetes applications. This sidecar container, named `gke-gcsfuse-sidecar`, runs alongside the workload container within the same Pod. When the driver detects the `gke-gcsfuse/volumes: "true"` annotation in a Pod specification, it automatically injects the sidecar container. This sidecar container approach helps to ensure security and manage resources effectively.

The sidecar container handles the complexities of mounting the Cloud Storage buckets and provides file system access to the applications without requiring you to manage the Cloud Storage FUSE runtime directly. You can configure resource limits for the sidecar container using annotations like `gke-gcsfuse/cpu-limit` and `gke-gcsfuse/memory-limit`. The sidecar container model also ensures that the Cloud Storage FUSE instance is tied to the workload lifecycle, preventing it from consuming resources unnecessarily. This means the sidecar container terminates automatically when the workload containers exit, especially in Job workloads or Pods with a `RestartPolicy` of `Never`.

### OSS Istio compatibility

The Cloud Storage FUSE CSI driver's sidecar container and [Istio](https://istio.io/) can coexist and run concurrently in your Pod. However, in GKE version 1.29 and later, you might encounter authentication failures if Cloud Storage FUSE attempts to connect to the metadata server before the Istio proxy is ready. If you encounter these authentication failures, you can resolve this issue by adding `traffic.sidecar.istio.io/excludeOutboundIPRanges: 169.254.169.254/32` to `metadata.annotations` in your Pod specification. This annotation configures Istio to exclude the IP address of the GKE metadata server from redirection.

**Note:** Cloud Service Mesh does not support running with multiple sidecar containers. For more information, see [Cloud Service Mesh Limitations](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#limitations).

## Configure custom write buffer

Cloud Storage FUSE stages writes in a local directory, and then uploads to Cloud Storage on `close` or `fsync` operations.

This section describes how to configure a custom buffer volume for Cloud Storage FUSE write buffering. This scenario might apply if you need to replace the default `emptyDir` volume for Cloud Storage FUSE to stage the files in write operations. This is useful if you need to write files larger than 10 GiB on Autopilot clusters.

You can specify any type of storage supported by the Cloud Storage FUSE CSI driver for file caching, such as a Local SSD, Persistent Disk-based storage, and RAM disk (memory). GKE will use the specified volume for file write buffering. To learn more about these options, see [Select the storage for backing your file cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#select-storage-for-file-cache).

To use a custom buffer volume backed by a Persistent Disk, you must specify a non-zero `fsGroup` in your Pod's securityContext. This step grants the necessary read or write permissions for the volume to the non-root sidecar container. This setting is not required if your PVC [mounts Cloud Storagebuckets as persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv) by using the Cloud Storage FUSE CSI driver.

The following example shows how you can use a predefined PersistentVolumeClaim as the buffer volume:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      securityContext:
        fsGroup: FS_GROUP
      containers:
      ...
      volumes:
      - name: gke-gcsfuse-buffer
        persistentVolumeClaim:
          claimName: BUFFER_VOLUME_PVC
    

Replace the following:

  * FS_GROUP: the fsGroup ID.
  * BUFFER_VOLUME_PVC: the predefined PVC name.



## Configure custom read cache volume

This section describes how to configure a custom cache volume for Cloud Storage FUSE read caching.

This scenario might apply if you need to replace the default `emptyDir` volume for Cloud Storage FUSE to cache the files in read operations. You can specify any type of storage supported by GKE, such as a [PersistentVolumeClaim](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims), and GKE will use the specified volume for file caching. This is useful if you need to cache files larger than 10 GiB on Autopilot clusters.

To use a custom cache volume backed by a Persistent Disk, you must specify a non-zero `fsGroup` in your Pod's securityContext. This step grants the necessary read or write permissions for the volume to the non-root sidecar container. This setting is not required if your PVC [mounts Cloud Storage buckets as persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv) by using the Cloud Storage FUSE CSI driver.

The following example shows how you can use a predefined PersistentVolumeClaim as the cache volume:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      securityContext:
        fsGroup: FS_GROUP
      containers:
      ...
      volumes:
      - name: gke-gcsfuse-cache
        persistentVolumeClaim:
          claimName: CACHE_VOLUME_PVC
    

Replace the following:

  * FS_GROUP: the `fsGroup` ID.
  * CACHE_VOLUME_PVC: the predefined PersistentVolumeClaim name.



## Configure a private image for the sidecar container

This section describes how to use the sidecar container image if you are hosting it in a private container registry. This scenario might apply if you need to use private nodes for security purposes.

To configure and consume the private sidecar container image, follow these steps:

  1. Refer to this [GKE compatibility table](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/releases.md#gke-compatibility) to find a compatible public sidecar container image.
  2. Pull it to your local environment and push it to your private container registry.
  3. In the manifest, specify a container named `gke-gcsfuse-sidecar` with only the image field. GKE will use the specified sidecar container image to prepare for the sidecar container injection.

Here is an example:
         
         apiVersion: v1
         kind: Pod
         metadata:
           annotations:
             gke-gcsfuse/volumes: "true"
         spec:
           containers:
           - name: gke-gcsfuse-sidecar
             image: PRIVATE_REGISTRY/gcs-fuse-csi-driver-sidecar-mounter:PRIVATE_IMAGE_TAG
           - name: main # your main workload container.
         

Replace the following:

     * PRIVATE_REGISTRY: your private container registry. For example, `us-central1-docker.pkg.dev/my-project/my-registry`.
     * PRIVATE_IMAGE_TAG: your private sidecar container image tag. For example, `v1.17.1-gke.1`.



## Configure sidecar container resources

By default, the `gke-gcsfuse-sidecar` container is configured with the following resource requests and limits for Standard and Autopilot clusters:

Requests:

  * 250m CPU
  * 256 MiB memory
  * 5 GiB ephemeral storage



Limits (GKE version `1.29.1-gke.1670000` and later):

  * unlimited cpu
  * unlimited memory
  * unlimited ephemeral storage



Limits (before GKE version `1.29.1-gke.1670000`):

  * 250m CPU
  * 256 MiB memory
  * 5 GiB ephemeral storage



By default, the `gke-gcsfuse-metadata-prefetch` container is configured with the following resource requests and limits for Standard and Autopilot clusters:

Requests:

  * 10m CPU
  * 10 MiB memory
  * 10 MiB ephemeral storage



Limits:

  * 50m CPU
  * 250 MiB memory
  * unlimited ephemeral storage



In Standard and Autopilot clusters, you can overwrite the default values. The way GKE handles container resources depends on your cluster mode of operation:

  * Standard clusters: If one of the request or limit is set and another is unset, the Pods' resource limits and requests will be set as the same. If both request and limits are set, Pods use the exact resource requests and limits that you specify. If you do not set any values, the default resources (described above) are applied directly.
  * Autopilot clusters: If one of the request or limit is set and another is unset, the Pods' resource limits and requests will be set as the same. Refer to [Setting resource limits in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#resource-limits) to understand how resource overrides, and the default resource values set will affects pod behavior.



To overwrite the default values for `gke-gcsfuse-sidecar` container, you can optionally specify the annotation `gke-gcsfuse/[cpu-limit|memory-limit|ephemeral-storage-limit|cpu-request|memory-request|ephemeral-storage-request]` as shown in the following example:

To overwrite the default values for `gke-gcsfuse-metadata-prefetch` container (starting from GKE version `1.32.3-gke.1717000` and later), you can optionally specify the annotation `gke-gcsfuse/[metadata-prefetch-cpu-limit|metadata-prefetch-memory-limit|metadata-prefetch-ephemeral-storage-limit|metadata-prefetch-cpu-request|metadata-prefetch-memory-request|metadata-prefetch-ephemeral-storage-request]` as shown in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        gke-gcsfuse/volumes: "true"
    
        # gke-gcsfuse-sidecar overrides
        gke-gcsfuse/cpu-limit: "10"
        gke-gcsfuse/memory-limit: 10Gi
        gke-gcsfuse/ephemeral-storage-limit: 1Ti
        gke-gcsfuse/cpu-request: 500m
        gke-gcsfuse/memory-request: 1Gi
        gke-gcsfuse/ephemeral-storage-request: 50Gi
    
        # gke-gcsfuse-metadata-prefetch overrides
        gke-gcsfuse/metadata-prefetch-cpu-limit: "10"
        gke-gcsfuse/metadata-prefetch-memory-limit: 10Gi
        gke-gcsfuse/metadata-prefetch-ephemeral-storage-limit: 1Ti
        gke-gcsfuse/metadata-prefetch-cpu-request: 500m
        gke-gcsfuse/metadata-prefetch-memory-request: 1Gi
        gke-gcsfuse/metadata-prefetch-ephemeral-storage-request: 50Gi
    

You can use value `"0"` to unset any resource limits or requests, but note that the `gke-gcsfuse-sidecar` container already has all limits (`cpu-limit`, `memory-limit`, and `ephemeral-storage-limit`) unset, and the `gke-gcsfuse-metadata-prefetch` container already has `ephemeral-storage-limit` unset, so setting these limits to `"0"` on a cluster with GKE version `1.32.3-gke.1717000` or later, would be a no-op.

For example, setting `gke-gcsfuse/metadata-prefetch-memory-limit: "0"`, indicates you want the `gke-gcsfuse-metadata-prefetch` container memory limit unset. This is useful when you cannot decide on the amount of resources the metadata prefetch feature needs for your workloads, and want to let metadata prefetch consume all the available resources on a node.

**Note:** If you use value `"0"` to unset the sidecar container resource limits or requests on Autopilot clusters, the behavior of your pods changes, depends on several factors including if your cluster supports bursting. See [Setting resource limits in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#resource-limits) for details.**Note:** A [`LimitRange`](https://kubernetes.io/docs/concepts/policy/limit-range/) object will also override the default and annotated values.

## (Optional) Analyze performance using Cloud Profiler

You can use [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler) to gain continuous, granular visibility into the resource consumption of your storage-heavy applications. The granular data can help you proactively monitor CPU and memory usage in the Cloud Storage FUSE CSI driver and its sidecar container. The insights you gain from Cloud Profiler data can help you in identifying inefficient code paths, optimizing resource allocation, and troubleshooting complex issues such as memory leaks or unexpected Out of Memory (OOM) events before they impact service stability.

Using Cloud Profiler is optional and is designed for administrators who require detailed performance diagnostics. Cloud Profiler is enabled by default for the node driver. For sidecar containers, it's an opt-in feature that you can manually enable.

### Before you enable Cloud Profiler

To use Cloud Profiler with the Cloud Storage FUSE CSI driver, ensure you're using GKE version 1.36.0-gke.2403000 or later. Before generating profiles, you must enable the Cloud Profiler API and configure the appropriate IAM permissions for the components you want to profile.

#### Enable the API

[ Enable the Cloud Profiler API ](https://console.cloud.google.com/flows/enableapi?apiid=cloudprofiler.googleapis.com)

#### Grant permissions to the node driver

To send profiling data to Cloud Profiler, the node driver requires IAM permissions. Because the node driver runs on the host network by default, it authenticates using the IAM service account associated with the GKE node, instead of using Workload Identity Federation for GKE.

Grant the `roles/cloudprofiler.agent` role to your node's service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/cloudprofiler.agent \
        --member=serviceAccount:NODE_SERVICE_ACCOUNT
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `NODE_SERVICE_ACCOUNT`: the IAM service account used by your GKE nodes. This is typically the default Compute Engine service account, for example, `PROJECT_NUMBER-compute@`, unless your nodes are [configured to use a different service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).



#### Grant permissions to the sidecar container

To send profiling data to Cloud Profiler, the sidecar container and `gcsfuse` process require IAM permissions. These components authenticate using Workload Identity Federation for GKE, which uses the Kubernetes Service Account (KSA) associated with your workload Pod.

Grant the `roles/cloudprofiler.agent` role to the KSA that your Pod uses:
    
    
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
        --role=roles/cloudprofiler.agent \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME \
        --condition=None
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `PROJECT_NUMBER`: the project number of your Google Cloud project.
  * `NAMESPACE`: the name of your Kubernetes namespace.
  * `KSA_NAME`: the name of your Kubernetes Service Account.

**Note:** If your workload Pod uses the host network but does not specify the `hostNetworkPodKSA` volume attribute, you must instead grant the `cloudprofiler.agent` role directly to the underlying Node's service account.

### Enable Cloud Profiler for sidecar workloads

To generate profiles for the sidecar mounter and the underlying `gcsfuse` process, set the `enableCloudProfilerForSidecar` volume attribute to `"true"` in your workload specification. Enabling Cloud Profiler for the sidecar container also automatically enables it for the underlying `gcsfuse` process.

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket:
    
    
    volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: BUCKET_NAME
            enableCloudProfilerForSidecar: "true"
    

### View profiling data

To view your profiling data, go to the [Cloud Profiler page in the Google Cloud console](https://console.cloud.google.com/profiler). Use the **Service name** filter as follows to analyze the component you are investigating:

Component | Service name filter  
---|---  
Node Driver | `gcs-fuse-csi-driver`  
Sidecar Mounter | `gke-gcsfuse-sidecar`  
GCSFuse | `gcsfuse`  
  
Cloud Profiler identifies each instance using the format `POD_NAME_POD_UID`. This ensures that each instance is uniquely identified even if a Pod restarts.

### (Optional) Disable GCSFuse profiling

By default, enabling profiling for the sidecar container also profiles the underlying `gcsfuse` process. You might want to disable `gcsfuse` profiling to reduce resource overhead or focus your analysis solely on the sidecar container's performance.

To disable `gcsfuse` profiling while keeping sidecar profiling enabled, add `enable-cloud-profiler=false` to the `mountOptions` attribute in your volume specification.

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket:
    
    
    volumes:
      - name: gcs-fuse-csi-ephemeral
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: BUCKET_NAME
            enableCloudProfilerForSidecar: "true"
            mountOptions: "enable-cloud-profiler=false"
    

## Configure logging verbosity

By default, the `gke-gcsfuse-sidecar` container generates logs at the `info` and `error` levels. However, for debugging or more detailed analysis, you might need to adjust the logging verbosity. This section outlines how to increase or decrease the logging level.

You can either use [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options) to configure the logging verbosity or use the CSI driver's capability to translate [volume attribute](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr) values into the necessary gcsfuse configuration settings.

In the target Pod manifest, include the following configurations:
    
    
          volumeAttributes:
            bucketName: BUCKET_NAME
            mountOptions: "implicit-dirs"
            gcsfuseLoggingSeverity:  LOGGING_SEVERITY
    

To use the mount options, include the following configuration in the target Pod manifest:
    
    
      mountOptions: "logging:severity:LOGGING_SEVERITY"
    

Replace the following:

  * BUCKET_NAME: your Cloud Storage bucket name.
  * LOGGING_SEVERITY: one of the following values, based on your requirements: 
    * `trace`
    * `debug`
    * `info`
    * `warning`
    * `error`



After the Pod is deployed, the CSI driver initiates gcsfuse with the newly configured logging level.

You can use the following filter to verify if the logging severity is applied:
    
    
    resource.labels.container_name="gke-gcsfuse-sidecar"
    resource.type="k8s_container"
    resource.labels.pod_name="POD_NAME"
    "severity:"
    

## Troubleshoot issues

For more information about troubleshooting the Cloud Storage FUSE CSI driver, see the [troubleshooting guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md) in the GitHub project documentation.

## What's next

  * [Learn how to optimize performance for the Cloud Storage FUSE CSI driver.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf)
  * [Explore additional samples for using the CSI driver on GitHub](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/examples/README.md).
  * [Learn more about Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
