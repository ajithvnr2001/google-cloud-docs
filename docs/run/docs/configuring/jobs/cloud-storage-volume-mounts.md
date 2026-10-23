---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts/
title: Configure Cloud Storage volume mounts for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:37.963301+00:00
---

# Configure Cloud Storage volume mounts for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure Cloud Storage volume mounts for jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to mount a Cloud Storage bucket as a storage volume, using Cloud Run volume mounts.

Mounting the bucket as a volume in Cloud Run presents the bucket content as files in the container file system. After you mount the bucket as a volume, you access the bucket as if it were a directory on your local file system, using your programming language's file system operations and libraries instead of using Google API Client Libraries.

You can mount your volume as read-only and you can also specify mount options for your volume.

**Important:** You don't need to install Cloud Storage FUSE in your container or modify the container in any way to use this feature.

## Memory requirements

Cloud Storage volume mounts use the Cloud Run [container memory](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits) for the following activities: 

  * For all Cloud Storage FUSE caching, Cloud Run uses the stat cache setting with a [Time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) of 60 seconds by default. The default maximum size of the stat cache is 32 MB, the default maximum size of the type cache is 4 MiB.

  * When reading from Cloud Storage, Cloud Storage FUSE makes API calls to read an object directly, without downloading the whole file to a local directory. Cloud Storage FUSE establishes a TCP connection, and reads back the entire Cloud Storage object, or just portions of the file you specify in your application or the operating system through an offset. When reading, Cloud Storage FUSE also consumes memory other than stat and type caches, such as a 1 MiB array for every file it reads, and for `goroutines`.

  * When writing to Cloud Storage, Cloud Storage FUSE supports `streaming-writes`, a write path, by default. Cloud Storage FUSE uploads data directly to Cloud Storage without fully staging the file. Each file you open for streaming writes consumes approximately 64 MiB of memory during the upload process. This reduces both latency and disk space usage, making it particularly beneficial for large, sequential writes.


**Note:** For background information on caching, see the Cloud Storage FUSE [Read/Write](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md) page.

## Limitations

Since Cloud Run uses [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) for this volume mount, there are a few things to keep in mind when mounting a Cloud Storage bucket as a volume:

  * Cloud Storage FUSE does not provide concurrency control for multiple writes (file locking) to the same file. When multiple writes try to replace a file, the last write wins and all previous writes are lost.
  * Cloud Storage FUSE is not a fully POSIX-compliant file system. For more details, refer to the [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse).



### Disallowed paths

Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, or `/sys`, or on their subdirectories.

## Before you begin

You need a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to mount as the volume.

For optimal read/write performance to Cloud Storage, see Optimizing Cloud Storage FUSE network bandwidth performance.

### Required roles

To get the permissions that you need to configure Cloud Storage volume mounts, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



To get the permissions that your [service identity](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity) needs to access the file and Cloud Storage bucket, ask your administrator to grant the service identity the [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) role. If the service identity needs to also perform write operations in a bucket, grant the [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) role instead.

For more details on Cloud Storage roles and permissions, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Mount a Cloud Storage volume

You can mount multiple buckets at different mount paths. You can also mount a volume to more than one container using the same or different mount paths across containers. 

If you are using multiple containers, first specify the volumes, then specify the volume mounts for each container. 

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. Click the **Volumes** tab.

  5. Click **Mount volume**.

  6. Select **Cloud Storage bucket** as the volume type.

  7. Configure the volume by doing the following:

     1. In the **Mount path** field, enter the path where you want to mount the volume.
     2. Browse and select the Cloud Storage bucket or a specific directory to be used for the volume. Optionally, create a new bucket.
     3. If you want to make the bucket read-only, select the **Read-only** checkbox.
     4. Optional: Expand **Mount options** to specify mount options.
     5. Click **Save**.
  8. Click **Create** or **Update**.




###  gcloud 

**Note:** We show the `gcloud run jobs update` command but you can also use the `gcloud run jobs deploy` command with the same parameters as shown.

  * To add a volume mount:
        
        gcloud run jobs update JOB \
          --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,readonly=READ_ONLY

Replace the following:

    * JOB: the name of your job.
    * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
    * BUCKET_NAME: the name of your Cloud Storage bucket.
    * READ_ONLY: `true` to make the volume read-only, or `false` to allow writes.
  * If you are using multiple containers, first specify your volume(s), then specify the volume mount(s) for each container:
        
        gcloud run jobs update JOB \
          --add-volume name=VOLUME_NAME,type=cloud-storage,bucket=BUCKET_NAME \
          --container CONTAINER_1 \
          --add-volume-mount volume=VOLUME_NAME,mount-path=MOUNT_PATH \
          --container CONTAINER_2 \
          --add-volume-mount volume=VOLUME_NAME,mount-path=MOUNT_PATH2




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the MOUNT_PATH, VOLUME_NAME, BUCKET_NAME and IS_READ_ONLY as needed.
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: **JOB_NAME**
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/execution-environment: gen2
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     volumeMounts:
                     - mountPath: MOUNT_PATH
                       name: VOLUME_NAME
                   volumes:
                   - name: VOLUME_NAME
                     csi:
                       driver: gcsfuse.run.googleapis.com
                       readOnly: IS_READ_ONLY
                       volumeAttributes:
                         bucketName: BUCKET_NAME

Replace the following:

     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.
     * BUCKET_NAME: the name of the Cloud Storage bucket.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
      resource "google_cloud_run_v2_job" "default" {
        name     = "JOB_NAME"
        location = "REGION"
    
        template {
          template {
            containers {
              image = "IMAGE_URL"
              volume_mounts {
                name = "VOLUME_NAME"
                mount_path = "MOUNT_PATH"
              }
            }
    
          volumes {
            name = "VOLUME_NAME"
            gcs {
              bucket = google_storage_bucket.default.name
              read_only = IS_READ_ONLY
            }
          }
        }
      }
    }
    
      resource "google_storage_bucket" "default" {
        name     = "BUCKET_NAME"
        location = "REGION"
      }
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
  * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.
  * BUCKET_NAME: the name of the Cloud Storage bucket.



## Reading and writing to a volume

If you use the Cloud Run volume mount feature, you access a mounted volume using the same libraries in your programming language that you use to read and write files on your local file system.

This is especially useful if you're using an existing container that expects data to be stored on the local file system and uses regular file system operations to access it.

The following snippets assume a volume mount with a `mountPath` set to `/mnt/my-volume`.

### Nodejs

Use the File System module to create a new file or append to an existing file in the volume, `/mnt/my-volume`: 
    
    
    var fs = require('fs');
    fs.appendFileSync('/mnt/my-volume/sample-logfile.txt', 'Hello logs!', { flag: 'a+' });

### Python

Write to a file kept in the volume, `/mnt/my-volume`: 
    
    
    f = open("/mnt/my-volume/sample-logfile.txt", "a")

### Go

Use the `os` package to create a new file kept in the volume, `/mnt/my-volume`: 
    
    
    f, err := os.Create("/mnt/my-volume/sample-logfile.txt")

### Java

Use the `Java.io.File` class to create a log file in the volume, `/mnt/my-volume`: 
    
    
    import java.io.File;
    File f = new File("/mnt/my-volume/sample-logfile.txt");

## Volume configuration using mount options

You can optionally use mount options to configure various properties of your volume mount. The available mount options allow you to configure cache settings, mount a specific directory, enable debug logging, and other behaviors.

### Specify mount options

You can specify mount options using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform. The mount options are separated by semicolons (`;`) in Google Cloud CLI and are separated by commas in YAML, as shown in the following tabs: 

### Console

To specify mount options for an existing volume:

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Click the job, then click **View and edit job configuration**.

  3. Click the **Volumes** tab.

     1. Click **Edit volume mount**.
     2. Expand **Mount options**.
     3. Configure mount options by updating the appropriate fields or by adding mount options manually.
     4. Click **Save**.
  4. Click **Deploy**.




###  gcloud 

To add a volume and mount it with mount options:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="OPTION_1=VALUE_1;OPTION_N=VALUE_N"

Replace the following:

  * JOB: the name of your job.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.
  * BUCKET_NAME: the name of your Cloud Storage bucket.
  * OPTION_1: the first mount option. Note that you can specify as many mount options as you need, with each mount option and value pair separated by a semicolon.
  * VALUE_1: the setting you want for the first mount option.
  * OPTION_N: the next mount option.
  * VALUE_N: the setting for the next mount option.



### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update as needed. 
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: **JOB_NAME**
         spec:
           metadata:
           template:
             metadata:
               annotations:
                 run.googleapis.com/execution-environment: gen2
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     volumeMounts:
                     - mountPath: MOUNT_PATH
                       name: VOLUME_NAME
                   volumes:
                   - name: VOLUME_NAME
                     csi:
                       driver: gcsfuse.run.googleapis.com
                       readOnly: IS_READ_ONLY
                       volumeAttributes:
                         bucketName: BUCKET_NAME
                         mountOptions: OPTION_1=VALUE_1,OPTION_N=VALUE_N

Replace the following:

     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * OPTION_1: the first mount option. Note that you can specify as many mount options as you need, with each mount option and value pair separated by a comma.
     * VALUE_1: the setting you want for the first mount option.
     * OPTION_N: the next mount option.
     * VALUE_N: the setting for the next mount option.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "IMAGE_URL"
            volume_mounts {
              name = "VOLUME_NAME"
              mount_path = "MOUNT_PATH"
            }
          }
    
          volumes {
            name = "VOLUME_NAME"
            gcs {
              bucket = google_storage_bucket.default.name
              read_only = IS_READ_ONLY
              mount_options = ["OPTION_1=VALUE_1", "OPTION_N=VALUE_N", "OPTION_O"]
            }
          }
        }
      }
    }
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run service.
  * REGION: the Google Cloud region.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
  * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.
  * BUCKET_NAME: the name of the Cloud Storage bucket.
  * OPTION_1: the first mount option. Note that you can specify as many mount options as you need, with each mount option and value pair separated by a comma.
  * VALUE_1: the setting you want for the first mount option.
  * OPTION_N: the second mount option, if applicable.
  * VALUE_N: the setting for the second mount option.
  * OPTION_O: the third mount option, if applicable. Some mount options don't have a value.



### Commonly used mount options

Mount options are commonly used to:

  * Configure cache settings
  * Mount only a specific directory from the Cloud Storage bucket
  * Configure the ownership of the volume (`uid`, `gid`)
  * Turn off implicit directories
  * Specify debug logging levels.



#### Configure caching settings

**Note:** Refer to the [Cloud Storage FUSE caching documentation](https://docs.cloud.google.com/storage/docs/gcsfuse-cache) for more information on cache options.

You can change the caching settings for your volume by setting the caching-related mount options. The following table lists the settings, along with the default Cloud Run values:

Cache setting | Description | Default  
---|---|---  
`cache-dir` | The in-memory volume name to use as the underlying directory to persist files from your Cloud Storage bucket in the format `cr-volume:{volume name}`. For example, if you have an in-memory volume named `in-memory-1` that you want to use as the cache directory, specify `cr-volume:in-memory-1`. For instructions on setting up in-memory volumes, see [Configure in-memory volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts). When you enable these features, Cloud Run changes the resource accounting of the Cloud Storage FUSE process and counts this towards the container memory limits. To increase the container memory limit, see [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits#configure-services). |   
`file-cache-download-chunk-size-mb` | Specifies the size of each read request in MiB that each goroutine makes to Cloud Storage when downloading the object into the file cache. | 200  
`file-cache-enable-parallel-downloads` | Accelerates reads of large files by using the file cache directory as a prefetch buffer using multiple workers to download multiple parts of a file in parallel. | true  
`file-cache-max-parallel-downloads` | The maximum number of goroutines that can be spawned at any given time across all the download jobs of files. | Twice the number of CPU cores on your machine or 16, whichever is higher.  
`file-cache-parallel-downloads-per-file` | The number of concurrent download requests per file. | 16  
`file-cache-cache-file-for-range-read` | Determines whether the full object should be downloaded asynchronously and stored in the Cloud Storage FUSE cache directory when the first read is completed from a non-zero offset. | false  
`stat-cache-max-size-mb` | Maximum size in mebibytes (MiB) that the stat cache can use. The stat cache is always entirely kept in memory, impacting memory consumption. Specify a value of `32` if your workload involves up to 20,000 files. If your workload uses more than 20,000 files, increase the size by values of `10` for every additional 6,000 files, where the stat cache uses an average of 1,500 bytes per file.  
  
To let the stat cache use as much memory as needed, specify a value of `-1`. To disable the stat cache, specify a value of `0`. | 32  
`type-cache-max-size-mb` | The maximum size in MiB per directory that the type cache can use. The type cache is always entirely kept in memory, impacting memory consumption.  
  
Specify a value of `4` if the maximum number of files within a single directory from the bucket you're mounting contains 20,000 files or less. If the maximum number of files within a single directory that you're mounting contains more than 20,000 files, increase the value by `1` for every 5,000 files, which is an average of around 200 bytes per file.  
  
To let the type cache use as much memory as needed, specify a value of `-1`.  
  
To disable the type cache, specify a value of `0`. | 4  
  
The following Google Cloud CLI command sets the `metadata-cache-ttl-secs` to 120 seconds and increases the stat and type cache capacity to `52` and `7` MiB, respectively:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="metadata-cache-ttl-secs=120;stat-cache-max-size-mb=52;type-cache-max-size-mb=7"

Replace the following:

  * JOB: the name of your job.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.
  * BUCKET_NAME: the name of your Cloud Storage bucket.



#### Enable debug logging

By default, Cloud Storage FUSE logs events that have `Info` or higher. You can change the logging settings using any of the following log-severity levels, listed in order from lowest to highest:

  * `trace`
  * `debug`
  * `info`
  * `warning`
  * `error`
  * To turn off all logging, specify the value `off`.



When you specify a severity level, Cloud Storage FUSE generates logs for events that have a severity level equal to or higher than the specified severity. For example, when you specify the `warning` level, Cloud Storage FUSE generates logs for warnings and errors.

Setting log severity to levels higher than `info` can impact performance and generate a large amount of logging data, so we recommend doing this only as needed. For compatibility with cloud logging, the log format is `text` format, and `json` format is not supported.

The following command line turns on debug logging:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="log-severity=debug"

Replace the following:

  * JOB with the name of your job.
  * BUCKET_NAME with the name of your Cloud Storage bucket.
  * MOUNT_PATH with the relative path where you are mounting the volume—for example, `/cache`.



#### Disable implicit directories

To make Cloud Storage appear more like a standard file system, Cloud Run enables implicit directories by default when mounting a Cloud Storage bucket. You can turn implicit directories off using the `implicit-dirs` mount option. Disabling implicit directories can improve performance and cost, but comes with compatibility tradeoffs.

The implicit directories feature enables Cloud Run to recognize pre-existing Cloud Storage files whose filenames mimic a directory structure, such as `/mydir/myfile.txt`. If you disable implicit directories, Cloud Run won't be able to list or read such files.

Turning off implicit directories reduces the number of requests to Cloud Storage, which might improve your application performance and cost. Read the Cloud Storage FUSE [Files and directories](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#files-and-directories) documentation to learn more.

The following command line disables implicit directories:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="implicit-dirs=false"

Replace the following:

  * JOB: the name of your job.
  * BUCKET_NAME: the name of your Cloud Storage bucket.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.



#### Mount a specific directory inside your Cloud Storage bucket

By default, Cloud Run mounts the entire Cloud Storage bucket, which gives Cloud Run jobs access to all its contents. In some cases you might want to mount only a specific directory. For example, in the case where the bucket contains a large number of files, mounting a specific directory can improve performance.

You can also implement this for isolation purposes where you need different jobs to have access to different directories in the storage bucket.

The following command line specifies the directory to mount:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="only-dir=images"

Replace the following:

  * JOB: the name of your job.
  * BUCKET_NAME: the name of your Cloud Storage bucket.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.



#### Set the volume `UID` and `GID`

Use the `uid` and `gid` mount options to change the User Identifier and Group Identifier for the volume. This is useful if you want to set ownership of the file to a specific user or group matching the identity of one or multiple running containers. By default, volumes are owned by root.

The following command line sets `uid` and `gid`:
    
    
    gcloud run jobs update JOB \
        --add-volume mount-path=MOUNT_PATH,type=cloud-storage,bucket=BUCKET_NAME,mount-options="uid=UID;gid=GID"

Replace the following:

  * JOB: the name of your job.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/cache`.
  * BUCKET_NAME: the name of your Cloud Storage bucket.
  * UID: user ID to mount the volume as.
  * GID: group ID to mount the volume as.



### Set other mount options

The following is the complete list of all of the mount options supported by Cloud Run.

**Directory**

  * `implicit-dirs`
  * `only-dir`
  * `rename-dir-limit`



**Debug**

  * `debug_fuse_errors`
  * `debug_fuse`
  * `debug_gcs`
  * `debug-invariants`
  * `debug_mutex`



**Cache**

  * `stat-cache-capacity`
  * `stat-cache-ttl`
  * `type-cache-ttl`
  * `enable-nonexistent-type-cache`



**Permissions**

  * `uid`
  * `gid`
  * `file-mode`
  * `dir-mode`



**Other**

  * `billing-project`
  * `client-protocol`
  * `experimental-enable-json-read`
  * `experimental-opentelemetry-collector-address`
  * `http-client-timeout`
  * `limit-bytes-per-sec`
  * `limit-ops-per-sec`
  * `max-conns-per-host`
  * `max-idle-conns-per-host`
  * `max-retry-sleep`
  * `-o`
  * `retry-multiplier`
  * `sequential-read-size-mb`
  * `stackdriver-export-interval`



For detailed descriptions of these options, see [Cloud Storage FUSE command line mount options](https://docs.cloud.google.com/storage/docs/gcsfuse-cli#options). The Cloud Storage FUSE page lists all available FUSE options, some of which are not supported by Cloud Run.

## View volume mounts settings

You can view current volume mount settings using the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job you are interested in to open the _Job details_ page.

  3. Click **View and edit job configuration**.

  4. Click the **Volumes** tab.

  5. Locate the volumes and details.




###  gcloud 

  1. Use the following command:
         
         gcloud run jobs describe JOB_NAME

  2. Locate the volume mounts setting in the returned configuration.




## Optimize Cloud Storage FUSE network bandwidth performance

For better read and write performance, connect your Cloud Run job to a VPC network using Direct VPC and route all outbound traffic through your VPC network. You can do this using any of the following options:

  * Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access), making sure to set the `vpc-egress` parameter to `all-traffic`.
  * Use one of the options described in the networking best practices page, in the section [Internal traffic to a Google API](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#internal-vpc-throughput).



## Container startup time and Cloud Storage FUSE mounts

Using Cloud Storage FUSE can slightly increase your Cloud Run container cold start time because Cloud Run starts the volume mount prior to starting the container(s). Your container will start only if Cloud Storage FUSE is successfully mounted.

Note that Cloud Storage FUSE successfully mounts a volume only after establishing a connection to Cloud Storage. Any networking delays can have an impact on container startup time. Correspondingly, if the connection attempt fails, Cloud Storage FUSE will fail to mount and the Cloud Run job will fail to start. Also, if Cloud Storage FUSE takes longer than 30 seconds to mount, the Cloud Run job will fail to start because Cloud Run has a total timeout of 30 seconds to perform all mounts.

## Cloud Storage FUSE performance characteristics

If you define two volumes, each pointing to a different bucket, two Cloud Storage FUSE processes will be started. The mounts and processes occur in parallel.

Operations using Cloud Storage FUSE are impacted by network bandwidth because Cloud Storage FUSE communicates with Cloud Storage using the Cloud Storage API. Some operations such as listing the contents of a bucket can be slow if the network bandwidth is low. Similarly, reading a large file can take time as this is also limited by network bandwidth.

When you write to a bucket, Cloud Storage FUSE fully stages the object in memory. This means that writing large files is limited by the amount of memory available to the container instance (the maximum container memory limit is 32 GiB).

The write is flushed to the bucket only when you perform a `close` or an `fsync`: the full object is then uploaded to the bucket. The only exception to an object being entirely re-uploaded to the bucket is in the case of a file with appended content when the file is 2 MiB or more.

For more information, see the following resources:

  * [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse#expandable-1)
  * [Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/gcsfuse-performance)
  * [Cloud Storage FUSE semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md)



## Clear and remove volumes and volume mounts

You can clear all volumes and mounts or you can remove individual volumes and volume mounts.

### Clear all volumes and volume mounts

To clear all volumes and volume mounts from your single-container job, run the following command:
    
    
    gcloud run jobs update JOB \
        --clear-volumes \
        --clear-volume-mounts

If you have multiple containers, follow the sidecars CLI conventions to clear volumes and volume mounts: 
    
    
    gcloud run jobs update JOB \
        --clear-volumes \
        --clear-volume-mounts \
        --container=container1 \
        --clear-volumes \
        --clear-volume-mounts \
        --container=container2 \
        --clear-volumes \
        --clear-volume-mounts

### Remove individual volumes and volume mounts

In order to remove a volume, you must also remove all volume mounts using that volume.

To remove individual volumes or volume mounts, use the `remove-volume` and `remove-volume-mount` flags:
    
    
    gcloud run jobs update JOB \
        --remove-volume VOLUME_NAME
        --container=container1 \
        --remove-volume-mount MOUNT_PATH \
        --container=container2 \
        --remove-volume-mount MOUNT_PATH

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
