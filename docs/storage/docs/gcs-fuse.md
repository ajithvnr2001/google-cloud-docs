---
url: https://docs.cloud.google.com/storage/docs/gcs-fuse/
title: Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:59.890352+00:00
---

# Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/gcs-fuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Cloud Storage FUSE, a [FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace) adapter that lets you mount and access Cloud Storage buckets as local file systems, so applications can read and write objects in your bucket using standard file system semantics.

This documentation reflects the latest version of Cloud Storage FUSE. For details on the latest version, see [Cloud Storage FUSE releases on GitHub](https://github.com/GoogleCloudPlatform/gcsfuse/releases).

Cloud Storage FUSE is an open source product supported by Google. Cloud Storage FUSE uses FUSE and Cloud Storage APIs to transparently expose buckets as locally mounted folders on your file system.

To use Cloud Storage FUSE, you install the Cloud Storage FUSE package on a machine with a compatible operating system such as Linux or Windows Subsystem for Linux, ensure proper Google Cloud authentication and permissions, and then execute the `gcsfuse` command to mount a specific Cloud Storage bucket to a local directory.

Cloud Storage FUSE is integrated with other Google Cloud services. For example, the Cloud Storage FUSE CSI driver lets you use the Google Kubernetes Engine (GKE) API to [consume buckets as volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver), so you can read from and write to Cloud Storage from within your Kubernetes pods. For more information on other integrations, see [Integrations](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#integrations).

## How Cloud Storage FUSE works

Cloud Storage FUSE works by translating object storage names into a directory-like structure, interpreting the slash character (`/`) in object names as a directory separator. Objects with the same common prefix are treated as files in the same directory, allowing applications to interact with the mounted bucket like a file system. Objects can also be organized into a logical file system structure using [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), which lets you organize objects into folders.

Cloud Storage FUSE can be run from anywhere with connectivity to Cloud Storage, including Google Kubernetes Engine, Compute Engine VMs, or on-premises systems.

## Rapid Bucket support

Starting with version 3.7.1, Cloud Storage FUSE supports Rapid Bucket with optimized read path, enabling faster data access and improved performance.

## Cloud Storage FUSE for machine learning

Cloud Storage FUSE is ideal for use cases where Cloud Storage has the right performance and scalability characteristics for an application that requires file system semantics. For example, Cloud Storage FUSE is [useful for machine learning (ML) projects](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#integrations) because it provides a way to store data, models, checkpoints, and logs directly in Cloud Storage. For more information, see [Cloud Storage FUSE for ML workloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#integrations).

Cloud Storage FUSE is a common choice for developers looking to store and access ML training and model data as objects in Cloud Storage. Cloud Storage FUSE provides several benefits for developing ML projects:

  * Cloud Storage FUSE lets you mount Cloud Storage buckets as a local file system so your applications can access training and model data using standard file system semantics. This means that you can avoid the cost of rewriting or refactoring your application's code when using Cloud Storage to store ML data.

  * From training to inference, Cloud Storage FUSE lets you use the built-in high scalability, performance, and [cost effectiveness](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#charges) of Cloud Storage, so you can run your ML workloads at scale.

  * Cloud Storage FUSE lets you start training jobs quickly by providing compute resources with direct access to data in Cloud Storage, so you don't need to download training data to the compute resource.




For more information, see [Frameworks, operating systems, and architectures supported by Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#frameworks-os-architectures).

## Frameworks, operating systems, and architectures

Cloud Storage FUSE has been validated with the following frameworks:

  * TensorFlow V2.x

  * TensorFlow V1.x

  * PyTorch V2.x

  * PyTorch V1.x

  * JAX 0.4.x




Cloud Storage FUSE supports the following operating systems and architectures:

  * Rocky Linux 8.9 or later

  * Ubuntu 18.04 or later

  * Debian 10 or later

  * CentOS 7.9 or later

  * RHEL 7.9 or later

  * SLES 15 or later

  * x86_64

  * ARM64




## Integrations with other Google Cloud products

Cloud Storage FUSE integrates with the following Google Cloud products:

Product | How Cloud Storage FUSE is integrated  
---|---  
[AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs) | Cloud Storage FUSE is recommended for AI and ML use cases because it lets you mount buckets as local file systems and scale your data storage with more cost efficiency than file system services. For more information, see [Storage services](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).  
[Batch](https://docs.cloud.google.com/batch/docs/get-started) | Cloud Storage FUSE lets you mount Cloud Storage buckets as storage volumes when you create and run Batch jobs. You can [specify a bucket in a job's definition](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-bucket), and the bucket gets automatically mounted to the VMs for the job when the job runs.  
[Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) | When you create an environment, Managed Service for Apache Airflow [stores the source code](https://docs.cloud.google.com/composer/docs/concepts/cloud-storage) for your workflows and their dependencies in specific folders in a Cloud Storage bucket. Managed Service for Apache Airflow uses Cloud Storage FUSE to map the folders in the bucket to the Airflow components in the Managed Service for Apache Airflow environment.  
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | Cloud Run lets you mount a Cloud Storage bucket as a volume and presents the bucket content as files in the container file system. To set up volume mounting, see [Mount a Cloud Storage volume](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts#mount-volume).   
[Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) | Cluster Toolkit lets you create or mount a Cloud Storage bucket as a file system. You can specify the bucket in a blueprint YAML file using the [appropriate module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/module-list-overview). The bucket is then automatically created or mounted when the deployment runs.  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-about) | When you use Cloud Storage FUSE to [mount Cloud Storage buckets](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-process-dataflow-fuse) directly onto the worker file system, the [Apache Beam pipeline code](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model) underlying Dataflow can access files in Cloud Storage directly using standard file system semantics. This is particularly helpful when using Dataflow for AI/ML tasks that involve large datasets and software that requires file access.  
[Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers/docs/overview) | To mount Cloud Storage buckets for Deep Learning Containers, you can either use the [Cloud Storage FUSE CSI driver](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver) (recommended) or [install Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install).  
[Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/introduction) | Cloud Storage FUSE comes pre-installed with Deep Learning VM Images.  
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) | The [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) manages the integration of Cloud Storage FUSE with the Kubernetes API to consume Cloud Storage buckets as volumes. You can use the Cloud Storage FUSE CSI driver to mount buckets as file systems on Google Kubernetes Engine nodes.  
[Vertex AI training](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) | You can access data from a Cloud Storage bucket as a [mounted file system](https://docs.cloud.google.com/vertex-ai/docs/training/cloud-storage-file-system) when you perform custom training on Vertex AI. For more information, see [Read and write Cloud Storage files with Cloud Storage FUSE](https://docs.cloud.google.com/vertex-ai/docs/training/code-requirements#fuse).  
[Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/tutorials/jupyter-notebooks) | Vertex AI Workbench instances include a Cloud Storage integration that lets you browse buckets and work with compatible files located in Cloud Storage from within the JupyterLab interface. The Cloud Storage integration lets you access all of the Cloud Storage buckets and files that your instance has access to within the same project as your Vertex AI Workbench instance. To set up the integration, see [Vertex AI Workbench instructions for how to access Cloud Storage buckets and files in JupyterLab](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cloud-storage#access_the_buckets_and_files).  
  
For a list of Google Cloud products that are integrated with Cloud Storage generally, see [Integration with Google Cloud services and tools](https://docs.cloud.google.com/storage/docs/google-integration).

## Caching

Cloud Storage FUSE offers three types of caching to help increase performance and reduce cost: file caching, stat caching, and list caching. For more information about these caches, see [Overview of caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching).

## Directory semantics

Cloud Storage offers buckets with a [flat namespace](https://docs.cloud.google.com/storage/docs/objects#flat-namespace) and buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. By default, Cloud Storage FUSE can infer explicitly-defined directories, also known as [folders](https://docs.cloud.google.com/storage/docs/folders-overview), in buckets with hierarchical namespace enabled but it can't infer implicitly-defined directories in buckets with a flat namespace, including [simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders) and [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders).

_Explicitly defined directories_ are folders that are represented by their own objects in Cloud Storage buckets. _Implicitly defined directories_ are directories that don't have their own corresponding objects in Cloud Storage buckets.

For example, say you mount a bucket named `my-bucket`, which contains an object named `my-directory/my-object.txt`, where `my-directory/` is a simulated folder. When you run `ls` on the bucket mount point, by default, Cloud Storage FUSE cannot access the simulated directory `my-bucket/my-directory/` nor the object `my-object.txt` within it. To enable Cloud Storage FUSE to infer the simulated folder and the object within it, include the [`--implicit-dirs` `gcsfuse` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#implicit-dirs) or the [`implicit-dirs` configuration file field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#implicit-dirs) as part of your `gcsfuse mount` command when mounting a flat namespace bucket.

If you need to store and access your data using a file system, use buckets with hierarchical namespace enabled. To learn how to create such buckets, see [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).

For more information about directory semantics, including how to mount buckets with implicitly-defined directories, see [Files and directories](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#files-and-directories) in the Cloud Storage FUSE GitHub documentation.

## Cloud Storage FUSE retry strategies

By default, failed requests from Cloud Storage FUSE to Cloud Storage are [retried with exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff) up to a specified maximum backoff duration, which has a value of `30s` (30 seconds) by default. Once the backoff duration exceeds the specified maximum duration, the retry continues with the specified maximum duration. You can use the [`--max-retry-sleep` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#max-retry-sleep) or the [`gcs-retries:max-retry-sleep` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#max-retry-sleep) as part of a `gcsfuse mount` call to specify the backoff duration.

### Retry strategy for stalled `GET` or `READ` requests

When you perform a `GET` or `READ` request with Cloud Storage FUSE, a timeout period is applied. If the request exceeds the timeout period, Cloud Storage FUSE cancels the request and retries using an [exponential backoff algorithm](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).

The timeout is dynamic and is based on the 99th percentile latency of past successful or canceled `GET` or `READ` requests, with a 1.5-second minimum. This ensures that only the slowest 1% of requests, those exceeding the 99th percentile historical latency, are retried.

### Retry strategy for stalled uploads

Large file writes are uploaded in chunks. To help reduce tail end write latencies, if a chunk-level write operation stalls or fails, Cloud Storage FUSE attempts a retry after 10 seconds. A maximum of four retry operations are performed for each stalled chunk.

## Cloud Storage FUSE operations associated with Cloud Storage operations

When you perform an operation using Cloud Storage FUSE, you also perform the Cloud Storage operations associated with the Cloud Storage FUSE operation. The following table describes common Cloud Storage FUSE commands and their associated Cloud Storage JSON API operations. You can display information about the Cloud Storage FUSE operations by setting the [`--log-severity` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#log-severity) or the [`logging:severity` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#severity) to `TRACE` in your `gcsfuse` command.

Command | [JSON API Operations](https://docs.cloud.google.com/storage/docs/json_api/v1)  
---|---  
`gcsfuse --log-severity=TRACE example-bucket mp` | Objects.list (to check credentials)  
`cd mp` | n/a  
`ls mp` | Objects.list("")  
`mkdir subdir` | Objects.get("subdir")Objects.get("subdir/")Objects.insert("subdir/")  
`cp ~/local.txt subdir/` | Objects.get("subdir/local.txt")Objects.get("subdir/local.txt/")Objects.insert("subdir/local.txt"), to create an empty objectObjects.insert("subdir/local.txt"), when closing after done writing  
`rm -rf subdir` | Objects.list("subdir")Objects.list("subdir/")Objects.delete("subdir/local.txt")Objects.list("subdir/")Objects.delete("subdir/")  
  
## Metrics

Cloud Storage offers in-depth metrics which can help you optimize Cloud Storage FUSE performance and costs. To learn more about metrics for Cloud Storage FUSE, see [Cloud Storage FUSE Metrics](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics).

## Security

Cloud Storage FUSE applies Google Cloud's standard authentication through [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to identify users or service accounts. Access to the contents within buckets is governed by [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) permissions. Local system permissions secure the mount point itself and any locally cached data.

## Pricing for Cloud Storage FUSE

Cloud Storage FUSE is available free of charge, but the storage, metadata, and network I/O it generates to and from Cloud Storage are charged like any other Cloud Storage interface. In other words, all data transfer and operations performed by Cloud Storage FUSE map to Cloud Storage transfers and operations, and are charged accordingly. For more information on common Cloud Storage FUSE operations and how they map to Cloud Storage operations, see operations mapping.

To avoid surprises, you should estimate how your use of Cloud Storage FUSE translates to Cloud Storage charges. For example, if you are using Cloud Storage FUSE to store log files, you can incur charges quickly if logs are aggressively flushed on hundreds or thousands of machines at the same time.

See [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing) for information on charges such as storage, network usage, and operations.

## Limitations

While Cloud Storage FUSE has a file system interface, it is not like an NFS or CIFS file system on the backend. Additionally, Cloud Storage FUSE is not POSIX compliant. For a POSIX file system product in Google Cloud, see [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) or [Filestore](https://docs.cloud.google.com/filestore).

When using Cloud Storage FUSE, be aware of its limitations and [semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md), which are different than that of POSIX file systems. Cloud Storage FUSE should only be used within its capabilities.

### Limitations and differences from POSIX file systems

The following list describes the limitations of Cloud Storage FUSE:

  * **Metadata** : Cloud Storage FUSE does not transfer object metadata when uploading files to Cloud Storage, with the exception of mtime and symlink targets. This means that you cannot set [object metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) when you upload files using Cloud Storage FUSE. If you need to preserve object metadata, consider uploading files using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage), the [JSON API](https://docs.cloud.google.com/storage/docs/json_api), or the [Google Cloud console](https://docs.cloud.google.com/storage/docs/discover-object-storage-console).
  * **Concurrency** : when you configure multiple mount points to access the same Cloud Storage bucket, and two or more mounts attempt to write to the same Cloud Storage object simultaneously, the first mount to complete the write operation and successfully flush its changes to the object is saved. Other mounts that haven't updated their local file descriptors after the object is modified encounter a `syscall.ESTALE` error when attempting to save their edits due to precondition checks. To ensure that your data is consistently written, we strongly recommend against multiple sources modifying the same object. 

Note that multiple readers can access the same or different objects within a bucket, and multiple writers can modify different objects in the same bucket simultaneously. Concurrent writes to the same Cloud Storage object are supported from the same mount and behave similarly to built-in file systems.

  * **Linking** : Cloud Storage FUSE does not support hard links.
  * **File locking and file patching** : Cloud Storage FUSE does not support file locking or file patching. As such, you shouldn't store version control system repositories in Cloud Storage FUSE mount points, as version control systems rely on file locking and patching. Additionally, you shouldn't use Cloud Storage FUSE as a file replacement.
  * **Semantics** : semantics in Cloud Storage FUSE are different from semantics in a conventional file system. For example, metadata like last access time are not supported, and some metadata operations like directory renaming are not atomic unless you use buckets with [hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/hns-overview). For a list of differences between Cloud Storage FUSE semantics and conventional file system semantics, see [Cloud Storage FUSE semantics](https://github.com/googlecloudplatform/gcsfuse/blob/master/docs/semantics.md) in the Cloud Storage FUSE GitHub documentation. To learn about how Cloud Storage FUSE infers directories in Cloud Storage, see [directory semantics](https://docs.cloud.google.com/storage/docs/gcs-fuse#directory-semantics). 
  * **Workloads that do file patching (or overwrites in place)** : Cloud Storage FUSE can only write whole objects at a time to Cloud Storage and does not provide a mechanism for patching. If you try to patch a file, Cloud Storage FUSE will reupload the entire file. The only exception to this behavior is that you can append content to the end of a file that's 2 MB and larger, where Cloud Storage FUSE will only reupload the appended content.
  * **Access** : authorization for files is governed by Cloud Storage permissions. POSIX-style access control does not work.
  * **Performance** : Cloud Storage FUSE has much higher latency than a local file system, and as such, shouldn't be used as the backend for storing a database. Throughput may be reduced when reading or writing one small file at a time. Using larger files or transferring multiple files at a time will help increase throughput.
  * **Availability** : transient errors can sometimes occur when you use Cloud Storage FUSE to access Cloud Storage. It's recommended that you retry failed operations using [retry strategies](https://docs.cloud.google.com/storage/docs/retry-strategy).
  * **Object versioning** : Cloud Storage FUSE does not formally support usage with buckets that have object versioning enabled. Attempting to use Cloud Storage FUSE with buckets that have object versioning enabled can produce unpredictable behavior.
  * **File transcoding** : 

objects with `content-encoding: gzip` in metadata: Any such object in a Cloud Storage FUSE-mounted directory does not undergo [decompressive transcoding](https://docs.cloud.google.com/storage/docs/transcoding). Instead, the object remains compressed in the same manner that it's stored in the bucket.

For example, a file of 1000 bytes, uploaded to a bucket using the `gcloud storage cp` command with the [`--gzip-local` flag](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp#--gzip-local), might become 60 bytes (the actual compressed size depends on the content and the gzip implementation used by the gcloud CLI) as a Cloud Storage object. If the bucket is mounted using `gcsfuse`, and the corresponding file is listed or read from the mount directory, its size is returned as 60 bytes, and its contents are a compressed version of the original 1000 bytes content.

This is in contrast to a download using `gcloud storage cp gs://bucket/path /local/path` which undergoes decompressive transcoding: in the `gcloud` command, the content is auto-decompressed during the download, and the original, uncompressed content is served.

**Note:** Attempting to use Cloud Storage FUSE to edit or modify objects with `content-encoding: gzip` can produce unpredictable behavior. This is because Cloud Storage FUSE uploads the object content as it is (without compressing it) while retaining `content-encoding: gzip`, and if this content is not properly gzip-compressed, it might fail in being read from the server by other clients, such as the gcloud CLI. This is because other clients employ decompressive transcoding while reading, and it fails for improper gzip content.
  * **Retention policies** : Cloud Storage FUSE does not support writing to buckets with a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock). If you attempt to write to a bucket with a retention policy, your writes will fail. 

Cloud Storage FUSE supports reading objects from buckets with a retention policy, but the bucket must be mounted as `Read-Only` by passing the `-o RO` flag during bucket mounting.

  * **Local storage** : objects that are new or modified are stored in their entirety in a local temporary file until they are closed or synced. When working with large files, make sure you have enough local storage capacity for temporary copies of the files, particularly if you are working with [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances). For more information, see the [Cloud Storage FUSE README overview file](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/README.md#downloading-object-contents) in the Cloud Storage FUSE GitHub documentation.
  * **File handle limits** : the Linux kernel has a default limit of 1,024 open file handles. When using Cloud Storage FUSE as a server to handle multiple concurrent connections, you might exceed this limit. To avoid issues, ensure the number of concurrent connections to a single host remains under the limit, and consider increasing the limit. Scenarios where this is important include using a Cloud Storage FUSE mount to serve web content, host network-attached storage (NAS), or host a file transfer protocol (FTP) server. When serving web content on Cloud Run from a Cloud Storage FUSE mount, the [maximum concurrent requests per instance](https://docs.cloud.google.com/run/docs/about-concurrency) is restricted to less than 1,000. 
  * **`rsync` limitations**: Cloud Storage FUSE's file system latency affects `rsync`, which reads and writes only one file at a time. To transfer multiple files to or from your bucket in parallel, use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage) by running `gcloud storage rsync`. For more information, see the [`rsync` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync). 
  * **List operations limitations** : when you list all the objects in a mounted bucket, for example, by running `ls`, Cloud Storage FUSE calls the [Objects: list API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) on Cloud Storage. The API paginates results, which means that Cloud Storage FUSE might need to issue multiple calls, depending on how many objects are in your bucket, which can make a list operation expensive and slow. 



## Known issues

For a list of known issues in Cloud Storage FUSE, see the [open Cloud Storage FUSE issues](https://github.com/GoogleCloudPlatform/gcsfuse/issues) in GitHub.

## Get support

You can get support, submit general questions, and request new features by using one of [Google Cloud's official support channels](https://docs.cloud.google.com/support-hub). You can also get support by [filing issues in GitHub](https://github.com/GoogleCloudPlatform/gcsfuse/issues).

For solutions to commonly-encountered issues, see [Troubleshooting for production issues](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/troubleshooting.md) in the Cloud Storage FUSE GitHub documentation.

## What's next

  * Learn how to [install the Cloud Storage FUSE CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install).

  * Discover Cloud Storage FUSE by completing a [quickstart](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/quickstart-mount-bucket).

  * Learn how to [mount buckets](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket).

  * Learn how to configure the behavior of Cloud Storage FUSE, using the [`gcsfuse` CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options) or a [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file).

  * Learn how to use [Cloud Storage agent skills](https://docs.cloud.google.com/storage/docs/agents-skills-overview#fuse-skill) to automate mounting and cache configuration with AI coding assistants.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
