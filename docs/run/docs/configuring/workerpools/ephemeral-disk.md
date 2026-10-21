---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/ephemeral-disk/
title: Configure an ephemeral disk for Cloud Run worker pools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:23.713675+00:00
---

# Configure an ephemeral disk for Cloud Run worker pools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/ephemeral-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure an ephemeral disk for Cloud Run worker pools Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Use Cloud Run volume mounts to mount an ephemeral disk**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run provides an ephemeral disk volume that persists only for the duration of your instance. This feature lets you specify the amount of disk you need and the location for mounting it. Cloud Run will then allocate that amount of disk to your resource.

Disks are automatically provisioned, pre-formatted to `ext4`, and encrypted with instance-specific keys at startup. Ephemeral disk creates your volume so that any user can read or write to it. Because the storage is ephemeral, all data is permanently deleted when the instance shuts down. This includes shutdowns caused by:

  * Instance crashes 
  * Traffic migration to a new revision 



Disks are dedicated to a specific instance and are not shared across other instances or revisions. You have control over the file system structure with a configurable mount point for each volume.

Before shutting down an instance, Cloud Run sends a `SIGTERM` signal to all the containers in an instance, indicating the start of a 10-second period before the actual shutdown occurs, at which point Cloud Run sends a `SIGKILL` signal. You can use this 10-second window to perform cleanup operations such as doing a final round of copying disk content persistent storage.

## Use cases

You can use ephemeral disk for the following:

  * **Data processing workloads** : When processing large data files in Cloud Run, you typically store the entire file in memory or orchestrate splitting it up into smaller pieces. With ephemeral storage, you won't need to pay for large amounts of memory to make a temporary local copy of your data. You will also be able to process larger data sets.
  * **Caching** : In web serving use cases, caching data on disk rather than fetching from remote storage can optimize your application's latency.



## Storage and instance limits

The following limits apply:

  * **Volume size limit** : each volume must be between `1Gi` and `100Gi`.
  * **Instance storage limit** : each instance is limited to 10 GiB of total space by default. Configuring more than 10 GiB per instance requires requesting a quota increase.
  * **Instance volume limit** : each instance is limited to a maximum of 10 ephemeral disk volumes.
  * **Project limit** : each project starts with a total regional allocation limit of 0 GiB by default. Projects are automatically granted 100 GiB per region the first time a resource with an ephemeral disk is deployed in that region. At runtime, this regional quota is shared across all actively running instances in the region. When deploying a resource, the combined ephemeral disk size per instance multiplied by its maximum number of instances cannot exceed the regional allocation limit. For example, with a 100 GiB regional limit, a resource with a 10 GiB disk can be configured with up to 10 instances. If necessary, request a quota increase.



### Request a quota increase

If you need additional capacity, you must request a quota increase for your Cloud Run worker pool. Use the links provided in the following buttons to request the quota you need.

Current quota | Quota link  
---|---  
10 GiB per instance | [Request greater quota per instance](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fmax_per_instance_ephemeral_disk_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
100 GiB per project | [Request greater quota per project](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fephemeral_disk_allocation_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
  
For more information on requesting quota increases, see [How to increase quota](https://docs.cloud.google.com/run/quotas#increase).

## Limitations

Ephemeral disk is only available in the second generation execution environment. By default, Cloud Run worker pools use the [second generation execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments). 

### Disallowed paths

Cloud Run does not allow you to mount a volume at `/dev`, `/proc`, or `/sys`, or on their subdirectories.

### Supported regions

Ephemeral disk is available in all [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI. 
  7. Update components: 
         
         gcloud components update

  8. Review the Cloud Run [pricing](https://cloud.google.com/run/pricing) page for CPU, memory, and network egress. The entire size of the provisioned disk and the lifetime of the instance that is using it contribute to your cost. 



### Required roles

To get the permissions that you need to configure an ephemeral disk, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create and mount an ephemeral disk

You can create and mount an ephemeral disk using the Google Cloud console, Google Cloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Containers** tab.

  4. Select the **Ephemeral disk** checkbox.

  5. Specify ephemeral disk size from the menu.

  6. Enter the mount path.

  7. Click **Create** or **Update**.




###  gcloud 

To add a volume and mount it:
    
    
    gcloud beta run worker-pools update WORKERPOOL \
        --add-volume=name=VOLUME_NAME,type=ephemeral-disk,size=SIZE \
        --add-volume-mount=volume=VOLUME_NAME,mount-path=MOUNT_PATH
    

Replace the following:

  * WORKERPOOL: the name of your worker pool.
  * VOLUME_NAME: the name you want to give your volume.
  * SIZE: the disk size—for example, `10Gi`. The size must be between `1Gi` and `100Gi` for `ephemeral-disk` volumes.
  * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.



###  YAML 

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Configure the YAML file:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           labels:
             cloud.googleapis.com/location: REGION
           annotations:
             run.googleapis.com/launch-stage: BETA
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
                   medium: Disk
                   sizeLimit: SIZE
         

Replace the following:

     * WORKER_POOL: the name of your worker pool.
     * REGION: the Google Cloud region.
     * CONTAINER_NAME: the name you want to give your container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
     * VOLUME_NAME: the name you want to give your volume.
     * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.
     * SIZE: the disk size—for example, `10Gi`. The size must be between `1Gi` and `100Gi` for `ephemeral-disk` volumes.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




###  Terraform 

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
      resource "google_cloud_run_v2_worker_pool" "default" {
        name     = "WORKER_POOL"
        location = "REGION"
        deletion_protection = "true"
        launch_stage = "BETA"
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
              medium = "DISK"
              size_limit = "SIZE"
            }
          }
        }
        lifecycle {
          ignore_changes = [
            launch_stage,
          ]
        }
      }
    

Replace the following:

  * WORKER_POOL: the name of your worker pool.
  * REGION: the Google Cloud region.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * VOLUME_NAME: the name you want to give your volume.
  * MOUNT_PATH: the relative path where you are mounting the volume, for example, `/mnt/my-volume`.
  * SIZE: the disk size—for example, `10Gi`. The size must be between `1Gi` and `100Gi` for `ephemeral-disk` volumes.



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

## Best practices

Adhere to the following best practices to effectively manage ephemeral data and optimize storage performance.

### Copy to persistent storage

If you intend to copy the ephemeral disk contents to persistent storage, such as a Cloud Storage bucket, we recommend incrementally copying, rather than relying on the 10-second `SIGTERM` to `SIGKILL` grace period. See [Container runtime contract](https://docs.cloud.google.com/run/docs/container-contract#worker-pool-instance-shutdown) for more information on instance shutdowns. 

Cloud Run can read and write from Cloud Storage without any additional networking setup. To achieve optimal performance, we recommend routing traffic to and from Cloud Storage through a VPC network using Direct VPC.

This method works if you don't need the Cloud Run resource to access the internet. If you do need internet access, either set up Cloud NAT, or see [Internal traffic to a Google API](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#internal-vpc-throughput).

To configure Direct VPC egress with a worker pool, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the menu, and click **Deploy container** to configure a new worker pool. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

  3. If you are configuring a new worker pool, fill out the initial worker pool page, then click **Containers, Networking, Security** to expand the worker pools configuration page.

  4. Click the **Networking** tab.

  5. Select **Connect to a VPC**.

  6. For **Traffic routing** , select one **Route all traffic to the VPC** to send all outbound traffic through the VPC network.

  7. Click **Create** or **Deploy**.

You can now send requests from your Cloud Run worker pool to any resource on the VPC network, as allowed by your firewall rules.

  8. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) on the subnet you connected to.




## Troubleshoot

If you see slow network speeds when downloading a large amount of data to your ephemeral disk, follow the steps to turn on Direct VPC. If Direct VPC is not enabled, you will see slower network transfer speeds. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
