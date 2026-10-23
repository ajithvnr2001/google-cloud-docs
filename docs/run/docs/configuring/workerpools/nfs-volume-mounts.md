---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/nfs-volume-mounts/
title: Configure NFS volume mounts for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:22.507328+00:00
---

# Configure NFS volume mounts for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/nfs-volume-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure NFS volume mounts for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to mount an NFS file share as a volume in Cloud Run. You can use any NFS server, including your own NFS server hosted on-premises, or on a Compute Engine VM. If you don't already have an NFS server, we recommend [Filestore](https://cloud.google.com/filestore), which is a fully managed NFS offering from Google Cloud.

Mounting the NFS file share as a volume in Cloud Run presents the file share as files in the container file system. After you mount the file share as a volume, you access it as if it were a directory on your local file system, using your programming language's file system operations and libraries.

## Limitations

  * Cloud Run does not support NFS locking. NFS volumes are automatically mounted in no-lock mode.
  * Disallowed paths: Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, or `/sys`, or on their subdirectories.



## Before you begin

To mount an NFS server as a volume in Cloud Run, make sure you have the following:

  * A [VPC Network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) where your NFS server or Filestore instance is running.
  * An NFS server running in a VPC network, with your Cloud Run worker pool connected to that VPC network. If you don't already have an NFS server, create one by [creating a Filestore instance](https://docs.cloud.google.com/filestore/docs/create-instance-console).
  * Your Cloud Run worker pool is attached to the VPC network where your NFS server is running. For best performance, use [Direct VPC](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) rather than VPC Connectors.
  * If you're using an existing project, make sure that your VPC Firewall configuration allows Cloud Run to reach your NFS server. (If you're starting from a new project, this is true by default.) If you're using Filestore as your NFS server, follow the Filestore documentation to create a [Firewall egress rule](https://docs.cloud.google.com/filestore/docs/configuring-firewall#linux_1) to enable Cloud Run to reach Filestore.
  * Set the permissions on your remote NFS file share to allow access for the container's user. By default, Filestore provides read access to all users but restricts write access to the root user (`uid 0`). If your container requires write access and does not run as the root user, you must use a connected client (running as root) to modify the share permissions. For example, you can use the `chown` command to change the ownership of the files or directories to the specific user ID your container runs as.



### Required roles

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Mount an NFS volume

You can mount multiple NFS servers, Filestore instances, or other volume types at different mount paths.

If you are using multiple containers, first specify the volume(s), then specify the volume mount(s) for each container.

Configure an NFS volume mount using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Volumes** tab.

  4. Click **Mount volume**.

  5. Click **NFS** as the volume type.

  6. Configure the volume by doing the following:

     1. In the **Mount path** field, enter the path where you want to mount the volume.
     2. In the **NFS server** field, enter the domain name or location (in the form `IP_ADDRESS`) of the NFS file share.
     3. In the **Path** field, enter the path to the NFS server directory that you want to mount.
     4. Click **Save**.
  7. Click **Create** or **Deploy**.




###  gcloud 

  * To add a volume mount:
        
        gcloud run worker-pools update WORKER_POOL \
        --add-volume mount-path=MOUNT_PATH,type=nfs,location=IP_ADDRESS:NFS_PATH,readonly=READ_ONLY

Replace the following:

    * WORKER_POOL: the name of your worker pool.
    * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.
    * IP_ADDRESS: the location of the NFS file share.
    * NFS_PATH: the path to the NFS file share starting with a forward slash—for example `/example-directory`.
    * READ_ONLY: `true` to make the volume read-only, or `false` to allow writes.
  * If you are using multiple containers, first specify the volumes, then specify the volume mounts for each container:
        
        gcloud run worker-pools update WORKER_POOL \
          --add-volume name=VOLUME_NAME,type=nfs,location=IP_ADDRESS:NFS_PATH \
          --container=CONTAINER_1 \
          --add-volume-mount volume=VOLUME_NAME,mount-path=MOUNT_PATH \
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
                 nfs:
                   server: IP_ADDRESS
                   path: NFS_PATH
                   readOnly: IS_READ_ONLY

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER_NAME: the name of the container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * VOLUME_NAME: any name you want for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
     * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
     * IP_ADDRESS: the address of the NFS file share.
     * NFS_PATH: the path to the NFS file share starting with a forward slash—for example, `/example-directory`.
     * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
          volume_mounts {
            name       = "VOLUME_NAME"
            mount_path = "MOUNT_PATH"
          }
        }
        vpc_access {
          network_interfaces {
            network    = "default"
            subnetwork = "default"
          }
        }
    
        volumes {
          name = "VOLUME_NAME"
          nfs {
            server    = google_filestore_instance.default.networks[0].ip_addresses[0]
            path      = "NFS_PATH"
            read_only = "IS_READ_ONLY"
          }
        }
      }
    }
    
    resource "google_filestore_instance" "default" {
      name     = "cloudrun-worker-pool"
      location = "REGION"
      tier     = "BASIC_HDD"
    
      file_shares {
        capacity_gb = 1024
        name        = "share1"
      }
    
      networks {
        network = "default"
        modes   = ["MODE_IPV4"]
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * VOLUME_NAME: the name for your volume. The VOLUME_NAME value is used to map the volume to the volume mount.
  * MOUNT_PATH: the relative path where you are mounting the volume—for example, `/mnt/my-volume`.
  * NFS_PATH: the path to the NFS file share.
  * IS_READ_ONLY: `True` to make the volume read-only, or `False` to allow writes.



## View environment variable configuration for the worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. Click the **Containers** tab to display worker pool container configuration.




### Troubleshooting NFS

If you experience problems, check the following:

  * Your Cloud Run worker pool is connected to the VPC network that the NFS server is on.
  * There are no firewall rules preventing Cloud Run from reaching the NFS server.
  * If your container needs to write data, ensure the NFS share permissions are configured to allow writes from your container's user.



## Container startup time and NFS volume mounts

Using NFS volume mounts can slightly increase your Cloud Run container cold start time because the volume mount is started prior to starting the container(s). Your container will start only if NFS is successfully mounted.

Note that NFS successfully mounts a volume only after establishing a connection to the server and fetching a file handle. If Cloud Run fails to establish a connection to the server, the Cloud Run worker pool will fail to start.

Also, any networking delays can have an impact on container startup time since Cloud Run has a total 30-second timeout for all mounts. If NFS takes longer than 30 seconds to mount, then Cloud Run worker pool will fail to start.

## NFS performance characteristics

If you create more than one NFS volume, all volumes are mounted in parallel.

Because NFS is a network file system, it is subject to bandwidth limits and access to the file system can be impacted by limited bandwidth.

When you write to your NFS volume, the write is stored in Cloud Run memory until the data is flushed. Data is flushed in the following circumstances:

  * Your application flushes file data explicitly using sync(2), msync(2), or fsync(3).
  * Your application closes a file with close(2).
  * Memory pressure forces reclamation of system memory resources.



For more information, see the [Linux documentation on NFS](https://linux.die.net/man/5/nfs).

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
