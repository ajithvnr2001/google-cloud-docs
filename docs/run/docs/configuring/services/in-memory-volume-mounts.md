---
url: https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts/
title: Configure in-memory volume mounts for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:53.725615+00:00
---

# Configure in-memory volume mounts for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure in-memory volume mounts for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a dedicated in-memory volume you can use for file reads and writes using Cloud Run volume mounts. Note that this feature differs from the built-in [in-memory file system](https://docs.cloud.google.com/run/docs/container-contract#filesystem) provided by Cloud Run.

When you mount the in-memory volume in Cloud Run, the in-memory volume shows up as files in the container file system. After you mount the in-memory volume, you access it as if it were a directory on your local file system, using your programming language's file system operations and libraries.

You can use in-memory volumes to do the following:

  * Limit the size of the in-memory volume. When you limit the size of a volume, writes to a full volume will fail, which is preferable to having Cloud Run terminate instances due to the volume consuming too much memory.

* Share an in-memory volume between different containers in one Cloud Run instance. When Cloud Run scales out to multiple instances of a service, each instance will have its own in-memory volume shared by all the containers on that instance. This volume is available to all the containers when Cloud Run scales out to handle traffic. 

## Behavior

When creating an in-memory volume, we recommend specifying a size limit. If the volume reaches its size limit, further writes will fail with an out-of-memory error. Your instance can handle this error and keep running.

Note that the size limit is just a limit: it does not allocate additional space for your in-memory volume. Rather, your in-memory volume consumes the memory you configured for your containers. If you deploy multiple containers, the memory used by each write to the volume counts as memory usage for the container that wrote the data.

If you don't specify a size limit, it is automatically set to half of the total size of all the containers in your service. For example, `emptyDir` volume size = [Memory (Container A) + Memory (Container B) + Memory (Container N)]/2. This default behavior can result in the size limit of the in-memory volume being higher than the memory allocated for some of your containers. This can lead to unexpected crashes if a single container exceeds its own allocated memory while trying to write more data to the volume, even though the volume size limit has not been reached.

Although setting a size limit is optional, we recommend setting one to protect your containers from running out of memory and crashing.

## Disallowed paths

Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, and `/sys`, or on their subdirectories.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure an in-memory volume

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it. 

After you configure an in-memory volume for your Cloud Run service, an empty volume is created for every Cloud Run instance that is started, and the volume exists as long as that instance is running. When the instance stops running, the data in the volume is permanently deleted.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu, and click **Deploy container** to configure a new service. If you are configuring an existing service, click the service, then click the **Containers** tab.

  3. If you are configuring a new service, fill out the initial service settings page, then click **Containers, Networking, Security** to expand the service configuration page, then click **Volumes**.

  4. Click **Mount volume**.

  5. Click **In-memory** as the volume type.

  6. In the **Mount path** field, enter the path where you want to mount the volume.

  7. Optional: Enter the **Size limit** and **Memory unit** to specify the memory limit you want to assign to the volume. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) specified for your containers. Data stored in this volume consumes memory reserved by the container that wrote the data.

  8. Click **Save**.

  9. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

  * To mount a volume:
        
        gcloud run services update SERVICE \
          --add-volume mount-path=MOUNT_PATH,type=in-memory,size-limit=SIZE_LIMIT

Replace the following:

    * SERVICE: the name of your service.
    * MOUNT_PATH: the relative path within the container file system where you want to mount this volume—for example, `/mnt/my-volume`.
    * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi), for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits) specified for your containers.
  * If you are using multiple containers, first specify the volumes, then specify the volume mounts for each container:
        
        gcloud run services update SERVICE \
          --add-volume=name= VOLUME_NAME,type=in-memory,size-limit=SIZE_LIMIT \
          --container=CONTAINER_1 \
          --add-volume-mount=volume= VOLUME_NAME,mount-path=MOUNT_PATH \
          --container==CONTAINER_2 \
          --add-volume-mount=volume= VOLUME_NAME,mount-path=MOUNT_PATH2




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Configure the `volumeMounts` and `volumes` attributes as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: **SERVICE_NAME**
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
                 emptyDir:
                   sizeLimit: SIZE_LIMIT
                   medium: Memory

Replace the following:

     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * `MOUNT_PATH`: the relative path within the container file system where you want to mount this volume—for example, `/mnt/my-volume`.
     * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi), for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) specified for your containers.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
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

  * SERVICE_NAME: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
  * MOUNT_PATH: the relative path within the container file system where you want to mount this volume—for example, `/mnt/my-volume`.
  * SIZE_LIMIT: the memory limit you want to assign to the volume, in MiB or GiB (specified as Mi or Gi), for example, `500Mi`. This limit must be less than the [total memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) specified for your containers.



### Compose

To specify in-memory volume mounts in your `compose.yaml` file, use the Google-specific extension `x-google-cloudrun:volume-type: in-memory`.
    
    
      services:
        web:
          image: IMAGE
          volumes:
            - VOLUME_NAME:MOUNT_PATH
      volumes:
        VOLUME_NAME:
          x-google-cloudrun:
            volume-type: in-memory

Replace the following:

  * IMAGE: the URL of your container image.
  * VOLUME_NAME: the name of the in-memory volume.
  * MOUNT_PATH: the path where you want to mount the volume—for example, `/mnt/my-volume`.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

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

To clear all volumes and volume mounts from your single-container service, run the following command:
    
    
    gcloud run services update SERVICE \
        --clear-volumes \
        --clear-volume-mounts

If you have multiple containers, follow the sidecars CLI conventions to clear volumes and volume mounts: 
    
    
    gcloud run services update SERVICE \
        --container=container1 \
        --clear-volumes \
        --clear-volume-mounts \
        --container=container2 \
        --clear-volumes \
        --clear-volume-mounts

### Remove individual volumes and volume mounts

In order to remove a volume, you must also remove all volume mounts using that volume.

To remove individual volumes or volume mounts, use the `remove-volume` and `remove-volume-mount` flags:
    
    
    gcloud run services update SERVICE \
        --remove-volume VOLUME_NAME \
        --container=container1 \
        --remove-volume-mount MOUNT_PATH \
        --container=container2 \
        --remove-volume-mount MOUNT_PATH

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
