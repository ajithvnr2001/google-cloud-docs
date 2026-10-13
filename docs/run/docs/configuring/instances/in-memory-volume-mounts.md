---
url: https://docs.cloud.google.com/run/docs/configuring/instances/in-memory-volume-mounts/
title: Configure in-memory volume mounts for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:14.365669+00:00
---

# Configure in-memory volume mounts for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/in-memory-volume-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure in-memory volume mounts for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure a dedicated in-memory volume you can use for file reads and writes using Cloud Run volume mounts. Note that this feature differs from the built-in [in-memory file system](https://docs.cloud.google.com/run/docs/container-contract#filesystem) provided by Cloud Run.

When you mount the in-memory volume in Cloud Run, the in-memory volume shows up as files in the container file system. After you mount the in-memory volume, you access it as if it were a directory on your local file system, using your programming language's file system operations and libraries.

You can use in-memory volumes to do the following:

  * Limit the size of the in-memory volume. When you limit the size of a volume, writes to a full volume will fail, which is preferable to having Cloud Run terminate instances due to the volume consuming too much memory.



## Behavior

When creating an in-memory volume, we recommend specifying a size limit. If the volume reaches its size limit, further writes will fail with an out-of-memory error. Your instance can handle this error and keep running.

Note that the size limit is just a limit: it does not allocate additional space for your in-memory volume. Rather, your in-memory volume consumes the memory you configured for your containers. If you deploy multiple containers, the memory used by each write to the volume counts as memory usage for the container that wrote the data.

If you don't specify a size limit, it is automatically set to half of the total size of all the containers in your instance. For example, `emptyDir` volume size = [Memory (Container A) + Memory (Container B) + Memory (Container N)]/2. This default behavior can result in the size limit of the in-memory volume being higher than the memory allocated for some of your containers. This can lead to unexpected crashes if a single container exceeds its own allocated memory while trying to write more data to the volume, even though the volume size limit has not been reached.

Although setting a size limit is optional, we recommend setting one to protect your containers from running out of memory and crashing.

## Disallowed paths

Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, and `/sys`, or on their subdirectories.

## Required roles

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure an in-memory volume

After you configure an in-memory volume for your Cloud Run instance, an empty volume is created for every Cloud Run instance that is started, and the volume exists as long as that instance is running. When the instance stops running, the data in the volume is permanently deleted.

Configure an in-memory volume mount using the Google Cloud CLI or YAML.

###  gcloud 

  * To mount a volume:
        
        gcloud beta run instances update INSTANCE \
          --add-volume mount-path=MOUNT_PATH,type=in-memory,size-limit=SIZE_LIMIT

Replace the following:

    * INSTANCE: the name of your instance.
    * MOUNT_PATH: the relative path within the container file system where you want to mount this volume, for example, `/mnt/my-volume`.
    * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi)—for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/instances/memory-limits) specified for your containers.
  * If you are using multiple containers, first specify the volumes, then [specify the volume mounts](https://docs.cloud.google.com/run/docs/configuring/instances/To%20override%20the%20default%20image%20%60ENTRYPOINT%60%20and%20%60CMD%60%20settings) for each container:
        
        gcloud beta run instances update INSTANCE \
          --add-volume=name=VOLUME_NAME,type=in-memory,size-limit=SIZE_LIMIT \
          --container=CONTAINER_1 \
          --add-volume-mount=volume=VOLUME_NAME,mount-path=MOUNT_PATH \
          --container=CONTAINER_2 \
          --add-volume-mount volume=VOLUME_NAME,mount-path=MOUNT_PATH2




### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
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

     * INSTANCE: the name of your Cloud Run instance.
     * CONTAINER_NAME: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.
     * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi), for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/instances/memory-limits) specified for your containers.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




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

To clear all volumes and volume mounts from your single-container instance, run the following command:
    
    
    gcloud beta run instances update INSTANCE \
        --clear-volumes \
        --clear-volume-mounts

### Remove individual volumes and volume mounts

In order to remove a volume, you must also remove all volume mounts using that volume.

To remove individual volumes or volume mounts, use the `remove-volume` and `remove-volume-mount` flags:
    
    
    gcloud beta run instances update INSTANCE \
        --remove-volume VOLUME_NAME \
        --container=container1 \
        --remove-volume-mount MOUNT_PATH \
        --container=container2 \
        --remove-volume-mount MOUNT_PATH

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
