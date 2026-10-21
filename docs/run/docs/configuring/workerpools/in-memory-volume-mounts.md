---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/in-memory-volume-mounts/
title: Configure in-memory volume mounts for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:02.146201+00:00
---

# Configure in-memory volume mounts for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/in-memory-volume-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure in-memory volume mounts for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a dedicated in-memory volume you can use for file reads and writes using Cloud Run volume mounts. Note that this feature differs from the built-in [in-memory file system](https://docs.cloud.google.com/run/docs/container-contract#filesystem) provided by Cloud Run.

When you mount the in-memory volume in Cloud Run, the in-memory volume shows up as files in the container file system. After you mount the in-memory volume, you access it as if it were a directory on your local file system, using your programming language's file system operations and libraries.

You can use in-memory volumes to do the following:

  * Limit the size of the in-memory volume. When you limit the size of a volume, writes to a full volume will fail, which is preferable to having Cloud Run terminate instances due to the volume consuming too much memory.

* Share an in-memory volume between different containers in one Cloud Run instance. When Cloud Run scales out to multiple instances of a worker pool, each worker pool will have its own in-memory volume shared by all the containers on that worker pool. This volume is available to all the containers when Cloud Run scales out to handle traffic. 

## Behavior

When creating an in-memory volume, we recommend specifying a size limit. If the volume reaches its size limit, further writes will fail with an out-of-memory error. Your instance can handle this error and keep running.

Note that the size limit is just a limit: it does not allocate additional space for your in-memory volume. Rather, your in-memory volume consumes the memory you configured for your containers. If you deploy multiple containers, the memory used by each write to the volume counts as memory usage for the container that wrote the data.

If you don't specify a size limit, it is automatically set to half of the total size of all the containers in your worker pool. For example, `emptyDir` volume size = [Memory (Container A) + Memory (Container B) + Memory (Container N)]/2. This default behavior can result in the size limit of the in-memory volume being higher than the memory allocated for some of your containers. This can lead to unexpected crashes if a single container exceeds its own allocated memory while trying to write more data to the volume, even though the volume size limit has not been reached.

Although setting a size limit is optional, we recommend setting one to protect your containers from running out of memory and crashing.

## Disallowed paths

Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, and `/sys`, or on their subdirectories.

## Required roles

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure an in-memory volume

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it. 

After you configure an in-memory volume for your Cloud Run worker pool, an empty volume is created for every Cloud Run instance that is started, and the volume exists as long as that instance is running. When the instance stops running, the data in the volume is permanently deleted.

Configure an in-memory volume mount using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Volumes** tab.

  4. Click **Mount volume**.

  5. Click **In-memory** as the volume type.

  6. Configure the volume by doing the following:

     1. In the **Mount path** field, enter the path where you want to mount the volume.
     2. In the **Volume name** field, enter name of the volume.
     3. Optional: Enter the **Size limit** and **Memory unit** to specify the memory limit you want to assign to the volume. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits) specified for your containers. Data stored in this volume consumes memory reserved by the container that wrote the data.
     4. Click **Save**.
  7. Click **Create** or **Deploy**.




###  gcloud 

  * To mount a volume:
        
        gcloud run worker-pools update WORKER_POOL \
          --add-volume mount-path=MOUNT_PATH,type=in-memory,size-limit=SIZE_LIMIT

Replace the following:

    * WORKER_POOL: the name of your worker pool.
    * MOUNT_PATH: the relative path within the container file system where you want to mount this volume, for example, `/mnt/my-volume`.
    * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi)—for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits) specified for your containers.
  * If you are using multiple containers, first specify the volumes, then specify the volume mounts for each container:
        
        gcloud run worker-pools update WORKER_POOL \
          --add-volume=name=VOLUME_NAME,type=in-memory,size-limit=SIZE_LIMIT \
          --container=CONTAINER_1 \
          --add-volume-mount=volume=VOLUME_NAME,mount-path=MOUNT_PATH \
          --container=CONTAINER_2 \
          --add-volume-mount volume=VOLUME_NAME,mount-path=MOUNT_PATH2




### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - name: CONTAINER_NAME
                 image: IMAGE_URL
                 volumeMounts:
                 - name: VOLUME_NAME
                   mountPath: MOUNT_PATH
               volumes:
               - name: VOLUME_NAME
                 emptyDir:
                   medium: Memory
                   sizeLimit: SIZE_LIMIT

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER_NAME: the name of the container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.
     * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi), for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits) specified for your containers.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To specify a single container, volume, and volume mount:
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
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
          empty_dir {
            medium = "MEMORY"
            size_limit = "SIZE_LIMIT"
          }
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of your Cloud Run worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
  * MOUNT_PATH: the relative path within the container file system where you want to mount this volume—for example, `/mnt/my-volume`.
  * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi)—for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits) specified for your containers.



To specify multiple containers, volumes, and volume mounts:
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
          volume_mounts {
            name = "VOLUME_NAME"
            mount_path = "MOUNT_PATH"
          }
        }
        containers {
          image = "IMAGE_URL_2"
          volume_mounts {
            name = "VOLUME_NAME_2"
            mount_path = "MOUNT_PATH_2"
          }
        }
        volumes {
          name = "VOLUME_NAME"
          empty_dir {
            medium = "MEMORY"
            size_limit = "SIZE_LIMIT"
          }
        }
        volumes {
          name = "VOLUME_NAME_2"
          empty_dir {
            medium = "MEMORY"
            size_limit = "SIZE_LIMIT_2"
          }
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of your Cloud Run worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * IMAGE_URL, IMAGE_URL_2: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * VOLUME_NAME, VOLUME_NAME_2: any name you want for your volume. This value is used to map the volume to the volume mount.
  * MOUNT_PATH, MOUNT_PATH_2: the relative path within the container file system where you want to mount this volume—for example, `/mnt/my-volume`.
  * SIZE_LIMIT, SIZE_LIMIT_2: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi)—for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits) specified for your containers.



## View environment variable configuration for the worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. Click the **Containers** tab to display worker pool container configuration.




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

## Clear and remove volumes and volume mounts

You can clear all volumes and mounts or you can remove individual volumes and volume mounts.

### Clear all volumes and volume mounts

To clear all volumes and volume mounts from your single-container worker pool, run the following command:
    
    
    gcloud run worker-pools update WORKER_POOL \
        --clear-volumes \
        --clear-volume-mounts

If you have multiple containers, follow the sidecars CLI conventions to clear volumes and volume mounts: 
    
    
    gcloud run worker-pools update WORKER_POOL \
        --container=container1 \
        --clear-volumes \
        --clear-volume-mounts \
        --container=container2 \
        --clear-volumes \
        --clear-volume-mounts

### Remove individual volumes and volume mounts

In order to remove a volume, you must also remove all volume mounts using that volume.

To remove individual volumes or volume mounts, use the `remove-volume` and `remove-volume-mount` flags:
    
    
    gcloud run worker-pools update WORKER_POOL \
        --remove-volume VOLUME_NAME \
        --container=container1 \
        --remove-volume-mount MOUNT_PATH \
        --container=container2 \
        --remove-volume-mount MOUNT_PATH

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
