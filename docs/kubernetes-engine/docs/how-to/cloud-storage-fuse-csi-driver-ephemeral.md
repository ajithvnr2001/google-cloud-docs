---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral/
title: Mount Cloud Storage buckets as CSI ephemeral volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:04.658451+00:00
---

# Mount Cloud Storage buckets as CSI ephemeral volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Mount Cloud Storage buckets as CSI ephemeral volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to use [CSI ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes) backed by your Cloud Storage buckets to automatically manage storage resources for your Kubernetes [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) or [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) on Google Kubernetes Engine (GKE). CSI ephemeral volumes are tied to the Pod or Job lifecycle, and you don't need to manually handle PersistentVolume and PersistentVolumeClaim objects.

This guide is for Platform admins and operators who want to simplify storage management for their GKE applications.

Before reading this page, ensure you're familiar with CSI ephemeral volumes, Kubernetes Pods and Jobs, and Cloud Storage buckets.

If you are already familiar with PersistentVolumes and want consistency with your existing deployments that rely on this resource type, see [Mount Cloud Storage buckets as persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv).

## Before you begin

Make sure you have completed these prerequisites:

  * Understand the [requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#requirements) and [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#limitations) of the Cloud Storage FUSE CSI driver.
  * [Create the Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#create-bucket)
  * [Enable the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#enable)
  * [Configure access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication)



## How CSI ephemeral storage for Cloud Storage buckets work

CSI ephemeral volumes simplify storage management for your applications on GKE. You define CSI ephemeral volumes directly within your Pod or Job specification. Using CSI ephemeral volumes eliminates the need for separate PersistentVolume and PersistentVolumeClaim objects.

Using a CSI ephemeral volume involves these operations:

  1. **Storage definition** : You specify the storage in your Pod or Job's YAML file, including the CSI driver to use and any required parameters. For Cloud Storage FUSE CSI driver, you specify the bucket name and other relevant details.

Optionally, you can fine-tune the performance of your CSI driver by using the [file caching](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#file-caching) feature. File caching can boost GKE app performance by caching frequently accessed Cloud Storage files on a faster disk.

Additionally, you can use the [parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#parallel-download) feature to accelerate reading large files from Cloud Storage for multi-threaded downloads. You can use this feature to improve model load times, especially for reads of over 1 GB in size.

**Tip:** For additional ways to fine-tune the performance of your CSI driver, see [Optimize performance for the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).
  2. **Driver invocation** : When you create the Pod or Job, GKE detects the ephemeral volume request and calls the Cloud Storage FUSE CSI driver.

  3. **Volume mount and attachment** : The CSI driver mounts the CSI ephemeral volume (which points to the underlying Cloud Storage bucket) and makes it available to the Pod or Job, making it accessible to your application. To fine-tune how buckets are mounted in the file system, you can use [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options). You can also use [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#volume-attributes) to configure specific behavior of the Cloud Storage FUSE CSI driver.

  4. **Lifecycle management** : The ephemeral volume exists for the lifetime of the Pod or Job. When the Pod is deleted or the Job completes, the CSI driver automatically handles cleanup, and unmounting the volume.


**Note:** When using CSI ephemeral volumes, you are still responsible for creating the buckets before use and for deleting the buckets.

## Attach the CSI ephemeral volume

Follow these instructions, depending on whether you want to attach the CSI ephemeral volume to a Pod or Job.

### Pod

To attach the CSI ephemeral volume in a Pod, follow these steps:

  1. Create a Pod YAML manifest with the following specification:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-example-ephemeral **  namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true" **
         spec:
           terminationGracePeriodSeconds: 60
           containers:
           - image: busybox
             name: busybox
             command: ["sleep"]
             args: ["infinity"] **    volumeMounts:
             - name: gcs-fuse-csi-ephemeral
               mountPath: /data
               readOnly: true
           serviceAccountName: KSA_NAME
           volumes:
           - name: gcs-fuse-csi-ephemeral
             csi:
               driver: gcsfuse.csi.storage.gke.io
               readOnly: true
               volumeAttributes:
                 bucketName: BUCKET_NAME
                 mountOptions: "implicit-dirs" **
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * KSA_NAME: the name of the Kubernetes ServiceAccount you specified when [configuring access to the Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

The example manifest shows these required settings:

     * `metadata.annotations`: the annotation `gke-gcsfuse/volumes: "true"` is required. See [Configure the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar) for optional annotations.
     * `spec.volumes[n].csi.driver`: use `gcsfuse.csi.storage.gke.io` as the CSI driver name.

Optionally, you can adjust these variables:

     * `spec.terminationGracePeriodSeconds`: By default, this is set to 30. If you need to write large files to the Cloud Storage bucket, increase this value to make sure that Cloud Storage FUSE has enough time to flush the data after your application exits. To learn more, see [Kubernetes best practices: terminating with grace](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace).
     * `spec.volumes[n].csi.volumeAttributes.mountOptions`: Pass [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options) to Cloud Storage FUSE. Specify the flags in one string separated by commas, without spaces.
     * `spec.volumes[n].csi.volumeAttributes`: Pass additional [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#volume-attributes) to Cloud Storage FUSE.
     * `spec.volumes[n].csi.readOnly`: Specify true if all the volume mounts are read-only.
     * `spec.containers[n].volumeMounts[m].readOnly`: Specify true if only a specific volume mount is read-only.
  2. Run the following command to apply the manifest to your cluster:
         
         kubectl apply -f FILE_PATH
         

Replace FILE_PATH with the path to your YAML file.




### Pod (file caching)

To attach the CSI ephemeral volume with file caching in a Pod, follow these steps:

  1. Create a cluster or node pool with [Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#ephemeral), by following the steps in [Create a cluster or node pool with Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#create).

**Note:** If you want to fine tune the storage type of the file cache (for example, if you are using a TPU VM and want to use RAM for faster processing), see [Select the storage for backing your file cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#select-storage-for-file-cache).
  2. Create a Pod YAML manifest with the following specification:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-file-cache-example **  namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true"
             gke-gcsfuse/ephemeral-storage-limit: "50Gi" **
         spec:
           nodeSelector:
             cloud.google.com/gke-ephemeral-storage-local-ssd: "true"
           restartPolicy: Never
           initContainers:
           - name: data-loader
             image: gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
             resources:
               limits:
                 cpu: 500m
                 memory: 1Gi
               requests:
                 cpu: 500m
                 memory: 1Gi
             command:
               - "/bin/sh"
               - "-c"
               - |
                 mkdir -p /test_files
                 for i in $(seq 1 1000); do dd if=/dev/zero of=/test_files/file_$i.txt bs=1024 count=64; done
                 gcloud storage cp /test_files gs://BUCKET_NAME --recursive
           containers:
           - name: data-validator
             image: busybox
             resources:
               limits:
                 cpu: 500m
                 memory: 512Mi
               requests:
                 cpu: 500m
                 memory: 512Mi
             command:
               - "/bin/sh"
               - "-c"
               - |
                 echo "first read with cache miss"
                 time cat /data/test_files/file_* > /dev/null
         
                 echo "second read from local cache"
                 time cat /data/test_files/file_* > /dev/null **    volumeMounts:
             - name: gcs-fuse-csi-ephemeral
               mountPath: /data
           serviceAccountName: KSA_NAME
           volumes:
           - name: gcs-fuse-csi-ephemeral
             csi:
               driver: gcsfuse.csi.storage.gke.io
               volumeAttributes:
                 bucketName: BUCKET_NAME
                 mountOptions: "implicit-dirs,file-cache:max-size-mb:-1"**
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * KSA_NAME: the name of the Kubernetes ServiceAccount you specified when configuring access to the Cloud Storage buckets.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

In the example manifest, the init container data-loader generates 1,000 files with size of 64 KiB, and uploads the files to a Cloud Storage bucket. The main container `data-validator` reads all the files from the bucket twice, and logs the duration.

  3. Run the following command to apply the manifest to your cluster:
         
         kubectl apply -f FILE_PATH
         

Replace FILE_PATH with the path to your YAML file.

  4. To view the log output, run the following command:
         
         kubectl logs -n NAMESPACE gcs-fuse-csi-file-cache-example -c data-validator
         

Replace NAMESPACE with the namespace of your workload.

The output should look similar to the following:
         
         first read with cache miss
         real    0m 54.68s
         ...
         second read from local cache
         real    0m 0.38s
         ...
         

The output shows that the second read with local cache is much faster than the first read with a cache miss.




### Pod (parallel download)

To attach the CSI ephemeral volume with parallel download in a Pod, follow these steps:

  1. Create a Pod YAML manifest with the following specification:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-example-ephemeral 
           namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true"
             gke-gcsfuse/ephemeral-storage-limit: "50Gi" 
         spec:
           containers:
           ...
           volumes:
           - name: gcs-fuse-csi-ephemeral **    csi:
               driver: gcsfuse.csi.storage.gke.io
               volumeAttributes:
                 bucketName: BUCKET_NAME
                 mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:max-size-mb:-1"
                 fileCacheCapacity: "-1"**
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.
  2. Run the following command to apply the manifest to your cluster:
         
         kubectl apply -f FILE_PATH
         

Replace FILE_PATH with the path to your YAML file.




### Job

To attach the CSI ephemeral volume in a Job, follow these steps:

  1. Create a Job YAML manifest with the following specification:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: gcs-fuse-csi-job-example **  namespace: NAMESPACE **
         spec:
           template:
             metadata: **      annotations:
                 gke-gcsfuse/volumes: "true"
             spec:
               serviceAccountName: KSA_NAME **
               containers:
               - name: writer
                 image: busybox
                 command:
                   - "/bin/sh"
                   - "-c"
                   - touch /data/test && echo $(date) >> /data/test && sleep 10
                 volumeMounts:
                 - name: gcs-fuse-csi-ephemeral
                   mountPath: /data
               - name: reader
                 image: busybox
                 command:
                   - "/bin/sh"
                   - "-c"
                   - sleep 10 && cat /data/test **        volumeMounts:
                 - name: gcs-fuse-csi-ephemeral
                   mountPath: /data
                   readOnly: true
               volumes:
               - name: gcs-fuse-csi-ephemeral
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: BUCKET_NAME
               restartPolicy: Never **
           backoffLimit: 1
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you deploy your Pod.
     * KSA_NAME: the name of the Kubernetes ServiceAccount you specified when configuring access to the Cloud Storage buckets.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

The example manifest shows these required settings:

     * `metadata.annotations`: the annotation `gke-gcsfuse/volumes: "true"` is required. See [Configure the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar) for optional annotations.
     * `spec.volumes[n].csi.drive`r: use `gcsfuse.csi.storage.gke.io` as the CSI driver name.

Optionally, you can adjust these variables:

     * `spec.volumes[n].csi.volumeAttributes.mountOptions`: Pass [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options) to Cloud Storage FUSE. Specify the flags in one string separated by commas, without spaces.
     * `spec.volumes[n].csi.volumeAttributes`: Pass additional [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#volume-attributes) to Cloud Storage FUSE.
     * `spec.volumes[n].csi.readOnly`: Specify true if all the volume mounts are read-only.
     * `spec.containers[n].volumeMounts[m].readOnly`: Specify true if only a specific volume mount is read-only.
  2. Run the following command to apply the manifest to your cluster:
         
         kubectl apply -f FILE_PATH
         

Replace `FILE_PATH` with the path to your YAML file.




## Mount the same Cloud Storage bucket with different CSI ephemeral volumes

You can optionally use multiple CSI ephemeral volumes that are backed by the same Cloud Storage bucket. To do so, attach two or more volumes that reference the same bucket name at different mount paths. An example use case could be mounting different CSI ephemeral volumes with different mount options to the same Pod, where each ephemeral volume refers to the same Cloud Storage bucket. The following is a sample Pod manifest using this feature:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: gcs-fuse-csi-job-example
      namespace: NAMESPACE
    spec:
      template:
        metadata:
          annotations:
            gke-gcsfuse/volumes: "true"
        spec:
          serviceAccountName: KSA_NAME
          containers:
          - name: writer
            image: busybox
            command:
              - "/bin/sh"
              - "-c"
              - touch /data/test && echo $(date) >> /data/test && sleep 10
            volumeMounts: **        - name: gcs-fuse-csi-ephemeral
              mountPath: /data
            volumeMounts:
            - name: gcs-fuse-csi-ephemeral-with-mo
              mountPath: /data2
          volumes:
          - name: gcs-fuse-csi-ephemeral
            csi:
              driver: gcsfuse.csi.storage.gke.io
              volumeAttributes:
                bucketName: BUCKET_NAME
          - name: gcs-fuse-csi-ephemeral-with-mo
            csi:
              driver: gcsfuse.csi.storage.gke.io
              volumeAttributes:
                bucketName: BUCKET_NAME
                mountOptions: "implicit-dirs"**
          restartPolicy: Never
      backoffLimit: 1
    

## Troubleshoot issues

For more information about troubleshooting the Cloud Storage FUSE CSI driver, see the [troubleshooting guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md) in the GitHub project documentation.

## What's next

  * [Learn how to optimize performance for the Cloud Storage FUSE CSI driver.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf)
  * [Explore additional samples for using the CSI driver on GitHub](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/examples/README.md).
  * [Learn more about Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
