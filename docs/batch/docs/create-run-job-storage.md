---
url: https://docs.cloud.google.com/batch/docs/create-run-job-storage/
title: Create and run a job that uses storage volumes \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:31:02.276259+00:00
---

# Create and run a job that uses storage volumes  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run a job that uses storage volumes Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create and run a Batch job that uses one or more external storage volumes. External storage options include new or existing persistent disk, new local SSDs, existing Cloud Storage buckets, and an existing network file system (NFS) such as a Filestore file share.

Regardless of whether you add external storage volumes, each Compute Engine VM for a job has a boot disk, which provides storage for the job's operating system (OS) image and instructions. For information about configuring the boot disk for a job, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview) instead.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * Create a job that uses a Cloud Storage bucket: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the bucket 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create a job that uses storage volumes

Optionally, a job can use one or more of each of the following types of external storage volumes. For more information about all of the types of storage volumes and the differences and restrictions for each, see the documentation for [Compute Engine VM storage options](https://docs.cloud.google.com/compute/docs/disks).

  * **[persistent disk](https://docs.cloud.google.com/compute/docs/disks#pdspecs)** : zonal or regional, persistent block storage
  * **[local SSD](https://docs.cloud.google.com/compute/docs/disks#localssds)** : high-performance, transient block storage
  * **[Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets)** : affordable object storage
  * **[network file system (NFS)](https://en.wikipedia.org/wiki/Network_File_System)** : distributed file system that follows Network File System protocol—for example, a [Filestore file share](https://docs.cloud.google.com/filestore/docs/create-instance-gcloud), which is a high-performance NFS hosted on Google Cloud



You can allow a job to use each storage volume by including it in your job's definition and specifying its [mount path (`mountPath`)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#volume) in your runnables. To learn how to create a job that uses storage volumes, see one or more of the following sections:

  * Use a persistent disk
  * Use a local SSD
  * Use a Cloud Storage bucket
  * Use a network file system



### Use a persistent disk

A job that uses persistent disks has the following restrictions:

  * **All persistent disks** : Review the [restrictions for all persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs).

  * **New versus existing persistent disks** : Each persistent disk in a job can be either new (defined in and created with the job) or existing (already created in your project and specified in the job). To use a persistent disk, it needs to be [formatted and mounted](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) to the job's VMs, which must be in the same location as the persistent disk. Batch mounts any persistent disks that you include in a job and formats any new persistent disks, but you must format and unmount any existing persistent disks that you want a job to use.

The supported [location options](https://docs.cloud.google.com/batch/docs/locations), [format options](https://manpages.ubuntu.com/manpages/xenial/man8/mkfs.ext4.8.html), and [mount options](https://www.google.com/url?sa=D&q=https%3A%2F%2Fman7.org%2Flinux%2Fman-pages%2Fman8%2Fmount.8.html%23COMMAND-LINE_OPTIONS) vary between new and existing persistent disks as described in the following table:

| New persistent disks | Existing persistent disks  
---|---|---  
Format options | The persistent disk is **automatically formatted with an[`ext4` file system](https://en.wikipedia.org/wiki/Ext4)**. | **You must[format the persistent disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) to use an [`ext4` file system](https://en.wikipedia.org/wiki/Ext4)** before using it for a job.  
Mount options | **All options** are supported. | **All options except writing** are supported. This is due to restrictions of [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms). **You must[detatch the persistent disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk)** from any VMs that it is attached to before using it for a job.  
Location options | You can only create **zonal persistent disks**. You can select **any location** for your job. The persistent disks get created in the zone your project runs in. | You can select **zonal and regional persistent disks**.   
To use a disk, the Compute Engine resources for a job must be created **only in locations that contain all of the job's persistent disks**. For example, for a zonal persistent disk, the job's location must be the disk's zone; for a regional persistent disk, the job's location must be either the disk's region or, if specifying zones, one or both of the specific zones where the regional persistent disk is located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).  
  * **Instance templates** : If you want to [use a VM instance template while creating this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), you must attach any persistent disks for this job in the instance template. Otherwise, if you don't want to use an instance template, you must attach any persistent disks directly in the job definition.




You can create a job that uses a persistent disk using the Google Cloud console, gcloud CLI, Batch API, C++, Go, Java, Node.js, or Python.

### Console

**Important:** The Google Cloud console supports existing zonal persistent disks only. To create a job that uses any new or regional persistent disks, use the gcloud CLI or Batch API.

Using the Google Cloud console, the following example creates a job that runs a script to read a file from an existing zonal persistent disk that is located in the `us-central1-a` zone. The example script assumes that the job has an existing zonal persistent disk that contains a text file named `example.txt` in the root directory.

#### Optional: Create an example zonal persistent disk

If you want to create a zonal persistent disk that you can use to run the example script, do the following before creating your job:

  1. Attach a new, blank persistent named `example-disk` to a Linux VM in the `us-central1-a` zone and then run commands on the VM to format and mount the disk. For instructions, see [Add a persistent disk to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).

Don't disconnect from the VM yet.

  2. To create `example.txt` on the persistent disk, run the following commands on the VM:

     1. To change the current working directory to the root directory of the persistent disk, type the following command:
            
            cd VM_MOUNT_PATH
            

Replace VM_MOUNT_PATH with the path to the directory where the persistent disk was mounted to this VM in the previous step—for example, `/mnt/disks/example-disk`.

     2. Press `Enter`.

     3. To create and define a file named `example.txt`, type the following command:
            
            cat > example.txt
            

     4. Press `Enter`.

     5. Type the contents of the file. For example, type `Hello world!`.

     6. To save the file, press `Ctrl+D` (or `Command+D` on macOS).

When you're done, you can disconnect from the VM.

  3. Detach the persistent disk from the VM.

     * If you don't need the VM anymore, you can [delete the VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance), which automatically detatches the persistent disk.

     * Otherwise, detach the persistent disk. For instructions, see [Detaching and reattaching boot disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) and detach the `example-disk` persistent disk instead of the VM's boot disk.




#### Create a job that uses the existing zonal persistent disk

To create a job that uses existing zonal persistent disks using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-disk-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, to run a script that prints the contents of a file that is named `example.txt` and located in the root directory of the persistent disk that this job uses, do the following:

           1. Select the **Script** checkbox. A field appears.

           2. In the field, enter the following script:
                  
                  echo "Here is the content of the example.txt file in the persistent disk."
                  cat MOUNT_PATH/example.txt
                  

Replace MOUNT_PATH with the path to where you plan to mount the persistent disk to the VMs for this job—for example, `/mnt/disks/example-disk`.

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job.

For example, enter `1` (default).

        3. In the **Parallelism** field, enter the number of tasks to run concurrently.

For example, enter `1` (default).

  4. Configure the **Resource specifications** page:

     1. In the left pane, click **Resource specifications**. The **Resource specifications** page opens.

     2. Select the [location](https://docs.cloud.google.com/batch/docs/locations) for this job. To use an existing zonal persistent disk, a job's VMs must be located in the same zone.

        1. In the **Region** field, select a region.

For example, to use the example zonal persistent disk, select **`us-central1 (Iowa)`** (default).

        2. In the **Zone** field, select a zone.

For example, select **`us-central1-a (Iowa)`**.

  5. Configure the **Additional configurations** page:

     1. In the left pane, click **Additional configurations**. The **Additional configurations** page opens.

     2. For each existing zonal persistent disk that you want to mount to this job, do the following:

        1. In the **Storage volume** section, click **Add new volume**. The **New volume** window appears.

        2. In the **New volume** window, do the following:

           1. In the **Volume type** section, select **Persistent disk** (default).

           2. In the **Disk** list, select an existing zonal persistent disk that you want to mount to this job. The disk must be located in the same zone as this job.

For example, select the existing zonal persistent disk that you prepared, which is located in the `us-central1-a` zone and contains the file `example.txt`.

           3. Optional: If you want to rename this zonal persistent disk, do the following:

              1. Select **Customize the device name**.

              2. In the **Device name** field, enter the new name for your disk.

           4. In the **Mount path** field, enter the mount path (MOUNT_PATH) for this persistent disk:

For example, enter the following:
                  
                  /mnt/disks/EXISTING_PERSISTENT_DISK_NAME
                  

Replace EXISTING_PERSISTENT_DISK_NAME with the name of the disk. If you renamed the zonal persistent disk, use the new name.

For example, replace EXISTING_PERSISTENT_DISK_NAME with `example-disk`.

           5. Click **Done**.

  6. Optional: Configure the [other fields for this job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

  7. Optional: To review the job configuration, in the left pane, click **Preview**.

  8. Click **Create**.




The **Job details** page displays the job that you created.

### gcloud

Using the gcloud CLI, the following example creates a job that attaches and mounts an existing persistent disk and a new persistent disk. The job has 3 tasks that each run a script to create a file in the new persistent disk named `output_task_TASK_INDEX.txt` where TASK_INDEX is the index of each task: 0, 1, and 2.

To create a job that uses persistent disks using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). In the job's JSON configuration file, specify the persistent disks in the `instances` field and mount the persistent disk in the `volumes` field.

  1. Create a JSON file.

     * If you are not using an instance template for this job, create a JSON file with the following contents:
           
           {
               "allocationPolicy": {
                   "instances": [
                       {
                           "policy": {
                               "disks": [
                                   {
                                       "deviceName": "EXISTING_PERSISTENT_DISK_NAME",
                                       "existingDisk": "projects/PROJECT_ID/EXISTING_PERSISTENT_DISK_LOCATION/disks/EXISTING_PERSISTENT_DISK_NAME"
                                   },
                                   {
                                       "newDisk": {
                                           "sizeGb": NEW_PERSISTENT_DISK_SIZE,
                                           "type": "NEW_PERSISTENT_DISK_TYPE"
                                       },
                                       "deviceName": "NEW_PERSISTENT_DISK_NAME"
                                   }
                               ]
                           }
                       }
                   ],
                   "location": {
                       "allowedLocations": [
                           "EXISTING_PERSISTENT_DISK_LOCATION"
                       ]
                   }
               },
               "taskGroups": [
                   {
                       "taskSpec": {
                           "runnables": [
                               {
                                   "script": {
                                       "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/disks/NEW_PERSISTENT_DISK_NAME/output_task_${BATCH_TASK_INDEX}.txt"
                                   }
                               }
                           ],
                           "volumes": [
                               {
                                   "deviceName": "NEW_PERSISTENT_DISK_NAME",
                                   "mountPath": "/mnt/disks/NEW_PERSISTENT_DISK_NAME",
                                   "mountOptions": "rw,async"
                               },
                               {
           
                                   "deviceName": "EXISTING_PERSISTENT_DISK_NAME",
                                   "mountPath": "/mnt/disks/EXISTING_PERSISTENT_DISK_NAME"
                               }
                           ]
                       },
                       "taskCount":3
                   }
               ],
               "logsPolicy": {
                   "destination": "CLOUD_LOGGING"
               }
           }
           

Replace the following:

       * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
       * `EXISTING_PERSISTENT_DISK_NAME`: the name of an existing persistent disk.
       * `EXISTING_PERSISTENT_DISK_LOCATION`: the location of an existing persistent disk. For each existing zonal persistent disk, the job's location must be the disk's zone; for each existing regional persistent disk, the job's location must be either the disk's region or, if specifying zones, one or both of the specific zones where the regional persistent disk is located. Learn more about the [`allowedLocations` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#locationpolicy).

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

         * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
         * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

       * `NEW_PERSISTENT_DISK_SIZE`: the size of the new persistent disk in GB. The [allowed sizes](https://docs.cloud.google.com/compute/docs/disks#introduction) depend on the type of persistent disk, but the minimum is often 10 GB (`10`) and the maximum is often 64 TB (`64000`).

       * `NEW_PERSISTENT_DISK_TYPE`: the [disk type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the new persistent disk, either `pd-standard`, `pd-balanced`, `pd-ssd`, or `pd-extreme`. The default disk type for non-boot persistent disks is `pd-standard`.

       * `NEW_PERSISTENT_DISK_NAME`: the name of the new persistent disk.

     * If you are [using a VM instance template for this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), create a JSON file as shown previously, except replace the [`instances` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#allocationpolicy) with the following:
           
           "instances": [
               {
                   "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
               }
           ],
           

where `INSTANCE_TEMPLATE_NAME` is the name of the instance template for this job. For a job that uses persistent disks, this instance template must define and attach the persistent disks that you want the job to use. For this example, the template must define and attach a new persistent disk named `NEW_PERSISTENT_DISK_NAME` and and attach an existing persistent disk named `EXISTING_PERSISTENT_DISK_NAME`.

  2. Run the following command:
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Using the Batch API, the following example creates a job that attaches and mounts an existing persistent disk and a new persistent disk. The job has 3 tasks that each run a script to create a file in the new persistent disk named `output_task_TASK_INDEX.txt` where TASK_INDEX is the index of each task: 0, 1, and 2.

To create a job that uses persistent disks using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create). In the request, specify the persistent disks in the `instances` field and mount the persistent disk in the `volumes` field.

  * If you are not using an instance template for this job, make the following request:
        
        POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
        
        {
            "allocationPolicy": {
                "instances": [
                    {
                        "policy": {
                            "disks": [
                                {
                                    "deviceName": "EXISTING_PERSISTENT_DISK_NAME",
                                    "existingDisk": "projects/PROJECT_ID/EXISTING_PERSISTENT_DISK_LOCATION/disks/EXISTING_PERSISTENT_DISK_NAME"
                                },
                                {
                                    "newDisk": {
                                        "sizeGb": NEW_PERSISTENT_DISK_SIZE,
                                        "type": "NEW_PERSISTENT_DISK_TYPE"
                                    },
                                    "deviceName": "NEW_PERSISTENT_DISK_NAME"
                                }
                            ]
                        }
                    }
                ],
                "location": {
                    "allowedLocations": [
                        "EXISTING_PERSISTENT_DISK_LOCATION"
                    ]
                }
            },
            "taskGroups": [
                {
                    "taskSpec": {
                        "runnables": [
                            {
                                "script": {
                                    "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/disks/NEW_PERSISTENT_DISK_NAME/output_task_${BATCH_TASK_INDEX}.txt"
                                }
                            }
                        ],
                        "volumes": [
                            {
                                "deviceName": "NEW_PERSISTENT_DISK_NAME",
                                "mountPath": "/mnt/disks/NEW_PERSISTENT_DISK_NAME",
                                "mountOptions": "rw,async"
                            },
                            {
        
                                "deviceName": "EXISTING_PERSISTENT_DISK_NAME",
                                "mountPath": "/mnt/disks/EXISTING_PERSISTENT_DISK_NAME"
                            }
                        ]
                    },
                    "taskCount":3
                }
            ],
            "logsPolicy": {
                "destination": "CLOUD_LOGGING"
            }
        }
        

Replace the following:

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
    * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
    * `JOB_NAME`: the name of the job.
    * `EXISTING_PERSISTENT_DISK_NAME`: the name of an existing persistent disk.
    * `EXISTING_PERSISTENT_DISK_LOCATION`: the location of an existing persistent disk. For each existing zonal persistent disk, the job's location must be the disk's zone; for each existing regional persistent disk, the job's location must be either the disk's region or, if specifying zones, one or both of the specific zones where the regional persistent disk is located. Learn more about the [`allowedLocations` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#locationpolicy).

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

      * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
      * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

    * `NEW_PERSISTENT_DISK_SIZE`: the size of the new persistent disk in GB. The [allowed sizes](https://docs.cloud.google.com/compute/docs/disks#introduction) depend on the type of persistent disk, but the minimum is often 10 GB (`10`) and the maximum is often 64 TB (`64000`).

    * `NEW_PERSISTENT_DISK_TYPE`: the [disk type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the new persistent disk, either `pd-standard`, `pd-balanced`, `pd-ssd`, or `pd-extreme`. The default disk type for non-boot persistent disks is `pd-standard`.

    * `NEW_PERSISTENT_DISK_NAME`: the name of the new persistent disk.

  * If you are [using a VM instance template for this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), create a JSON file as shown previously, except replace the [`instances` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#allocationpolicy) with the following:
        
        "instances": [
            {
                "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
            }
        ],
        ...
        

Where `INSTANCE_TEMPLATE_NAME` is the name of the instance template for this job. For a job that uses persistent disks, this instance template must define and attach the persistent disks that you want the job to use. For this example, the template must define and attach a new persistent disk named `NEW_PERSISTENT_DISK_NAME` and and attach an existing persistent disk named `EXISTING_PERSISTENT_DISK_NAME`.




###  C++ 

**Note:** If this is your first time creating a job that uses a persistent disk, it's recommended to review the API section first.

To create a Batch job that uses new or existing persistent disks using the [Cloud Client Libraries for C++](https://docs.cloud.google.com/cpp/docs/reference/batch/latest), use the [`CreateJob` function](https://docs.cloud.google.com/cpp/docs/reference/batch/latest/classgoogle_1_1cloud_1_1batch__v1_1_1BatchServiceClient#classgoogle_1_1cloud_1_1batch__v1_1_1BatchServiceClient_1abd924423a2a3e6aca655605a578661de) and include the following:

  * To attach persistent disks to the VMs for a job, include one of the following: 
    * If you are not using a VM instance template for this job, use the `set_remote_path` method.
    * If you are using a VM instance template for this job, use the `set_instance_template` method.
  * To mount the persistent disks to the job, use the `volumes` field with the `deviceName` and `mountPath` fields. For new persistent disks, also use the `mountOptions` field to enable writing.



For a code sample of a similar use case, see Use a Cloud Storage bucket.

###  Go 

**Note:** If this is your first time creating a job that uses a persistent disk, it's recommended to review the API section first.

To create a Batch job that uses new or existing persistent disks using the [Cloud Client Libraries for Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1), use the [`CreateJob` function](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1#cloud_google_com_go_batch_apiv1_Client_CreateJob) and include the following:

  * To attach persistent disks to the VMs for a job, include one of the following: 
    * If you are not using a VM instance template for this job, include the [`AllocationPolicy_AttachedDisk` type](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb#cloud_google_com_go_batch_apiv1_batchpb_AllocationPolicy_AttachedDisk).
    * If you are using a VM instance template for this job, include the [`AllocationPolicy_InstancePolicyOrTemplate_InstanceTemplate` type](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb#cloud_google_com_go_batch_apiv1_batchpb_AllocationPolicy_InstancePolicyOrTemplate_InstanceTemplate).
  * To mount the persistent disks to the job, use the [`Volume` type](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb#cloud_google_com_go_batch_apiv1_batchpb_Volume) with the [`Volume_DeviceName` type](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb#cloud_google_com_go_batch_apiv1_batchpb_Volume_DeviceName) and `MountPath` field. For new persistent disks, also use the `MountOptions` field to enable writing.


    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job with persistent disk
    func createJobWithPD(w io.Writer, projectID, jobName, pdName string) error {
    	// jobName := job-name
    	// pdName := disk-name
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("batchClient error: %w", err)
    	}
    	defer batchClient.Close()
    
    	runn := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Script_{
    			Script: &batchpb.Runnable_Script{
    				Command: &batchpb.Runnable_Script_Text{
    					Text: "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}",
    				},
    			},
    		},
    	}
    	volume := &batchpb.Volume{
    		MountPath: fmt.Sprintf("/mnt/disks/%v", pdName),
    		Source: &batchpb.Volume_DeviceName{
    			DeviceName: pdName,
    		},
    	}
    
    	// The disk type of the new persistent disk, either pd-standard,
    	// pd-balanced, pd-ssd, or pd-extreme. For Batch jobs, the default is pd-balanced
    	disk := &batchpb.AllocationPolicy_Disk{
    		Type:   "pd-balanced",
    		SizeGb: 10,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		ComputeResource: &batchpb.ComputeResource{
    			// CpuMilli is milliseconds per cpu-second. This means the task requires 1 CPU.
    			CpuMilli:  1000,
    			MemoryMib: 16,
    		},
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    		Runnables:     []*batchpb.Runnable{runn},
    		Volumes:       []*batchpb.Volume{volume},
    	}
    
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	labels := map[string]string{"env": "testing", "type": "container"}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// Read more about local disks here: https://cloud.google.com/compute/docs/disks/persistent-disks
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					MachineType: "n1-standard-1",
    					Disks: []*batchpb.AllocationPolicy_AttachedDisk{
    						{
    							Attached: &batchpb.AllocationPolicy_AttachedDisk_NewDisk{
    								NewDisk: disk,
    							},
    							DeviceName: pdName,
    						},
    					},
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	job := &batchpb.Job{
    		Name:             jobName,
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           labels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	request := &batchpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, "us-central1"),
    		JobId:  jobName,
    		Job:    job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, request)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    	return nil
    }
    

###  Java 

**Note:** If this is your first time creating a job that uses a persistent disk, it's recommended to review the API section first.

To create a Batch job that uses new or existing persistent disks using the [Cloud Client Libraries for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview), use the [`CreateJobRequest` class](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest) and include the following:

  * To attach persistent disks to the VMs for a job, include one of the following: 
    * If you are not using a VM instance template for this job, include the [`setDisks` method](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_Builder_setDisks_int_com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk_).
    * If you are using a VM instance template for this job, include the [`setInstanceTemplate` method](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setInstanceTemplate_java_lang_String_).
  * To mount the persistent disks to the job, use the [`Volume` class](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume) with the [`setDeviceName` method](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder#com_google_cloud_batch_v1_Volume_Builder_setDeviceName_java_lang_String_) and [`setMountPath` method](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_). For new persistent disks, also use the [`setMountOptions` method](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder#com_google_cloud_batch_v1_Volume_Builder_setMountOptions_int_java_lang_String_) to enable writing.



For example, use the following code sample:
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[LocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html);
    import com.google.common.collect.Lists;
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreatePersistentDiskJob {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
        // The size of the new persistent disk in GB.
        // The allowed sizes depend on the type of persistent disk,
        // but the minimum is often 10 GB (10) and the maximum is often 64 TB (64000).
        int diskSize = 10;
        // The name of the new persistent disk.
        String newPersistentDiskName = "DISK-NAME";
        // The name of an existing persistent disk.
        String existingPersistentDiskName = "EXISTING-DISK-NAME";
        // The location of an existing persistent disk. For more info :
        // https://cloud.google.com/batch/docs/create-run-job-storage#gcloud
        String location = "regions/us-central1";
        // The disk type of the new persistent disk, either pd-standard,
        // pd-balanced, pd-ssd, or pd-extreme. For Batch jobs, the default is pd-balanced.
        String newDiskType = "pd-balanced";
    
        createPersistentDiskJob(projectId, region, jobName, newPersistentDiskName,
                diskSize, existingPersistentDiskName, location, newDiskType);
      }
    
      // Creates a job that attaches and mounts an existing persistent disk and a new persistent disk
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createPersistentDiskJob(String projectId, String region, String jobName,
                                                String newPersistentDiskName, int diskSize,
                                                String existingPersistentDiskName,
                                                String location, String newDiskType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
          // Define what will be done as part of the job.
          String text = "echo Hello world from task ${BATCH_TASK_INDEX}. "
                  + ">> /mnt/disks/NEW_PERSISTENT_DISK_NAME/output_task_${BATCH_TASK_INDEX}.txt";
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(text)
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .addAllVolumes(volumes(newPersistentDiskName, existingPersistentDiskName))
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(3)
              .[setParallelism](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setParallelism_long_)(1)
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          // Policies are used to define the type of virtual machines the tasks will run on.
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) policy = [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder()
                  .[addAllDisks](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_Builder_addAllDisks_java_lang_Iterable___extends_com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk__)(attachedDisks(newPersistentDiskName, diskSize, newDiskType,
                      projectId, location, existingPersistentDiskName))
                  .build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances(
                      [InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder()
                          .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(policy))
                      .setLocation([LocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy.html).newBuilder().[addAllowedLocations](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_LocationPolicy_Builder_addAllowedLocations_java_lang_String_)(location))
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  // We use Cloud Logging as it's an out-of-the-box option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING))
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    
      // Creates link to existing disk and creates configuration for new disk
      private static Iterable<AttachedDisk> attachedDisks(String newPersistentDiskName, int diskSize,
                                                          String newDiskType, String projectId,
                                                          String existingPersistentDiskLocation,
                                                          String existingPersistentDiskName) {
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html) newDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html).newBuilder()
                .setDeviceName(newPersistentDiskName)
                .[setNewDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk_Builder_setNewDisk_com_google_cloud_batch_v1_AllocationPolicy_Disk_)([Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.html).newBuilder().[setSizeGb](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_Disk_Builder_setSizeGb_long_)(diskSize).setType(newDiskType))
                .build();
    
        String diskPath = String.format("projects/%s/%s/disks/%s", projectId,
                existingPersistentDiskLocation, existingPersistentDiskName);
    
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html) existingDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html).newBuilder()
                .setDeviceName(existingPersistentDiskName)
                .[setExistingDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk_Builder_setExistingDisk_java_lang_String_)(diskPath)
                .build();
    
        return Lists.newArrayList(existingDisk, newDisk);
      }
    
      // Describes a volume and parameters for it to be mounted to a VM.
      private static Iterable<Volume> volumes(String newPersistentDiskName,
                                              String existingPersistentDiskName) {
        [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) newVolume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
                .setDeviceName(newPersistentDiskName)
                .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/disks/" + newPersistentDiskName)
                .[addMountOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_addMountOptions_java_lang_String_)("rw")
                .[addMountOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_addMountOptions_java_lang_String_)("async")
                .build();
    
        [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) existingVolume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
                .setDeviceName(existingPersistentDiskName)
                .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/disks/" + existingPersistentDiskName)
                .build();
    
        return Lists.newArrayList(newVolume, existingVolume);
      }
    }

###  Node.js 

**Note:** If this is your first time creating a job that uses a persistent disk, it's recommended to review the API section first.

To create a Batch job that uses new or existing persistent disks using the [Cloud Client Libraries for Node.js](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest), use the [`createJob` method](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/v1.batchserviceclient#_google_cloud_batch_v1_BatchServiceClient_createJob_member_1_) and include the following:

  * To attach persistent disks to the VMs for a job, include one of the following: 
    * If you are not using a VM instance template for this job, include the [`AllocationPolicy.AttachedDisk` class](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.allocationpolicy.attacheddisk).
    * If you are using a VM instance template for this job, include the [`instanceTemplate` property](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.allocationpolicy.instancepolicyortemplate).
  * To mount the persistent disks to the job, use the [`Volume` class](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.volume) with the [`deviceName` property](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.volume#_google_cloud_batch_protos_google_cloud_batch_v1_Volume_deviceName_member) and [`mountPath` property](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.volume#_google_cloud_batch_protos_google_cloud_batch_v1_Volume_mountPath_member). For new persistent disks, also use the [`mountOptions` property](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.volume#_google_cloud_batch_protos_google_cloud_batch_v1_Volume_mountOptions_member) to enable writing.


    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-create-persistent-disk-job';
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of an existing persistent disk.
    const existingPersistentDiskName = 'existing-persistent-disk-name';
    // The name of the new persistent disk.
    const newPersistentDiskName = 'new-persistent-disk-name';
    // The size of the new persistent disk in GB.
    // The allowed sizes depend on the type of persistent disk,
    // but the minimum is often 10 GB (10) and the maximum is often 64 TB (64000).
    const diskSize = 10;
    // The location of an existing persistent disk. For more info :
    // https://cloud.google.com/batch/docs/create-run-job-storage#gcloud
    const location = 'regions/us-central1';
    // The disk type of the new persistent disk, either pd-standard,
    // pd-balanced, pd-ssd, or pd-extreme. For Batch jobs, the default is pd-balanced.
    const newDiskType = 'pd-balanced';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: [
          '-c',
          'echo Hello world! This is task ${BATCH_TASK_INDEX}.' +
            '>> /mnt/disks/NEW_PERSISTENT_DISK_NAME/output_task_${BATCH_TASK_INDEX}.txt',
        ],
      }),
    });
    
    // Define volumes and their parameters to be mounted to a VM.
    const newVolume = new batch.Volume({
      deviceName: newPersistentDiskName,
      mountPath: `/mnt/disks/${newPersistentDiskName}`,
      mountOptions: ['rw', 'async'],
    });
    
    const existingVolume = new batch.Volume({
      deviceName: existingPersistentDiskName,
      mountPath: `/mnt/disks/${existingPersistentDiskName}`,
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      volumes: [newVolume, existingVolume],
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    const newDisk = new batch.AllocationPolicy.Disk({
      type: newDiskType,
      sizeGb: diskSize,
    });
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // Read more about local disks here: https://cloud.google.com/compute/docs/disks/persistent-disks
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      disks: [
        // Create configuration for new disk
        new batch.AllocationPolicy.AttachedDisk({
          deviceName: newPersistentDiskName,
          newDisk,
        }),
        // Create link to existing disk
        new batch.AllocationPolicy.AttachedDisk({
          existingDisk: `projects/${projectId}/${location}/disks/${existingPersistentDiskName}`,
          deviceName: existingPersistentDiskName,
        }),
      ],
    });
    
    const locationPolicy = new batch.AllocationPolicy.LocationPolicy({
      allowedLocations: [location],
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      instances: [{policy: instancePolicy}],
      location: locationPolicy,
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      labels: {env: 'testing', type: 'script'},
      allocationPolicy,
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchPersistentDiskJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchPersistentDiskJob();

###  Python 

**Note:** If this is your first time creating a job that uses a persistent disk, it's recommended to review the API section first.

To create a Batch job that uses new or existing persistent disks using the [Cloud Client Libraries for Python](https://docs.cloud.google.com/python/docs/reference/batch/latest), use the [`CreateJob` function](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1#cloud_google_com_go_batch_apiv1_Client_CreateJob) and include the following:

  * To attach persistent disks to the VMs for a job, include one of the following: 
    * If you are not using a VM instance template for this job, include the [`AttachedDisk` class](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.AttachedDisk).
    * If you are using a VM instance template for this job, include the [`instance_template` attribute](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate).
  * To mount the persistent disks to the job, use the [`Volume` class](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume) with the `device_name` attribute and `mount_path` attribute. For new persistent disks, also use the `mount_options` attribute to enable writing.



For example, use the following code sample:
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_with_pd_job(
        project_id: str,
        region: str,
        job_name: str,
        disk_name: str,
        zone: str,
        existing_disk_name=None,
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances with mounted persistent disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            disk_name: name of the disk to be mounted for your Job.
            existing_disk_name(optional): existing disk name, which you want to attach to a job
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = (
            "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/disks/"
            + disk_name
            + "/output_task_${BATCH_TASK_INDEX}.txt"
        )
        task.runnables = [runnable]
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        volume = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
        volume.device_name = disk_name
        volume.mount_path = f"/mnt/disks/{disk_name}"
        task.volumes = [volume]
    
        if existing_disk_name:
            volume2 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
            volume2.device_name = existing_disk_name
            volume2.mount_path = f"/mnt/disks/{existing_disk_name}"
            task.volumes.append(volume2)
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        disk = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[Disk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Disk.html)()
        # The disk type of the new persistent disk, either pd-standard,
        # pd-balanced, pd-ssd, or pd-extreme. For Batch jobs, the default is pd-balanced
        disk.type_ = "pd-balanced"
        disk.size_gb = 10
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # Read more about local disks here: https://cloud.google.com/compute/docs/disks/persistent-disks
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "n1-standard-1"
    
        attached_disk = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.AttachedDisk.html)()
        attached_disk.new_disk = disk
        attached_disk.device_name = disk_name
        policy.disks = [attached_disk]
    
        if existing_disk_name:
            attached_disk2 = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.AttachedDisk.html)()
            attached_disk2.existing_disk = (
                f"projects/{project_id}/zones/{zone}/disks/{existing_disk_name}"
            )
            attached_disk2.device_name = existing_disk_name
            policy.disks.append(attached_disk2)
    
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
    
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        location = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[LocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.LocationPolicy.html)()
        location.allowed_locations = [f"zones/{zone}"]
        allocation_policy.location = location
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script"}
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### Use a local SSD

A job that uses local SSDs has the following restrictions:

  * **All local SSDs** Review the [restrictions for all local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds).
  * **Instance templates** If you want to [specify a VM instance template while creating this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), you must attach any persistent disks for this job in the instance template. Otherwise, if you don't want to use an instance template you must attach any persistent disks directly in the job definition.



You can create a job that uses a local SSD using the gcloud CLI, Batch API, Java, or Python. The following example describes how to create a job that creates, attaches, and mounts a local SSD. The job also has 3 tasks that each run a script to create a file in the local SSD named `output_task_TASK_INDEX.txt` where `TASK_INDEX` is the index of each task: `0`, `1`, and `2`.

### gcloud

To create a job that uses local SSDs using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). In the job's JSON configuration file, create and attach the local SSDs in the `instances` field and mount the local SSDs in the `volumes` field.

  1. Create a JSON file.

     * If you are not using an instance template for this job, create a JSON file with the following contents:
           
           {
               "allocationPolicy": {
                   "instances": [
                       {
                           "policy": {
                               "machineType": MACHINE_TYPE,
                               "disks": [
                                   {
                                       "newDisk": {
                                           "sizeGb": LOCAL_SSD_SIZE,
                                           "type": "local-ssd"
                                       },
                                       "deviceName": "LOCAL_SSD_NAME"
                                   }
                               ]
                           }
                       }
                   ]
               },
               "taskGroups": [
                   {
                       "taskSpec": {
                           "runnables": [
                               {
                                   "script": {
                                       "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/disks/LOCAL_SSD_NAME/output_task_${BATCH_TASK_INDEX}.txt"
                                   }
                               }
                           ],
                           "volumes": [
                               {
                                   "deviceName": "LOCAL_SSD_NAME",
                                   "mountPath": "/mnt/disks/LOCAL_SSD_NAME",
                                   "mountOptions": "rw,async"
                               }
                           ]
                       },
                       "taskCount":3
                   }
               ],
               "logsPolicy": {
                   "destination": "CLOUD_LOGGING"
               }
           }
           

Replace the following:

       * `MACHINE_TYPE`: the machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), of the job's VMs. The [allowed number of local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) depends on the machine type for your job's VMs.
       * `LOCAL_SSD_NAME`: the name of a local SSD created for this job.
       * `LOCAL_SSD_SIZE`: the size of all the local SSDs in GB. Each local SSD is 375 GB, so this value must be a multiple of `375` GB. For example, for 2 local SSDs, set this value to `750` GB.
     * If you are [using a VM instance template for this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), create a JSON file as shown previously, except replace the [`instances` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#allocationpolicy) with the following:
           
           "instances": [
               {
                   "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
               }
           ],
           

where `INSTANCE_TEMPLATE_NAME` is the name of the instance template for this job. For a job that uses local SSDs, this instance template must define and attach the local SSDs that you want the job to use. For this example, the template must define and attach a local SSD named `LOCAL_SSD_NAME`.

  2. Run the following command:
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



### API

To create a job that uses local SSDs using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create). In the request, create and attach the local SSDs in the `instances` field and mount the local SSDs in the `volumes` field.

  * If you are not using an instance template for this job, make the following request:
        
        POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
        
        {
            "allocationPolicy": {
                "instances": [
                    {
                        "policy": {
                            "machineType": MACHINE_TYPE,
                            "disks": [
                                {
                                    "newDisk": {
                                        "sizeGb": LOCAL_SSD_SIZE,
                                        "type": "local-ssd"
                                    },
                                    "deviceName": "LOCAL_SSD_NAME"
                                }
                            ]
                        }
                    }
                ]
            },
            "taskGroups": [
                {
                    "taskSpec": {
                        "runnables": [
                            {
                                "script": {
                                    "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/disks/LOCAL_SSD_NAME/output_task_${BATCH_TASK_INDEX}.txt"
                                }
                            }
                        ],
                        "volumes": [
                            {
                                "deviceName": "LOCAL_SSD_NAME",
                                "mountPath": "/mnt/disks/LOCAL_SSD_NAME",
                                "mountOptions": "rw,async"
                            }
                        ]
                    },
                    "taskCount":3
                }
            ],
            "logsPolicy": {
                "destination": "CLOUD_LOGGING"
            }
        }
        

Replace the following:

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
    * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
    * `JOB_NAME`: the name of the job.
    * `MACHINE_TYPE`: the machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), of the job's VMs. The [allowed number of local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) depends on the machine type for your job's VMs.
    * `LOCAL_SSD_NAME`: the name of a local SSD created for this job.
    * `LOCAL_SSD_SIZE`: the size of all the local SSDs in GB. Each local SSD is 375 GB, so this value must be a multiple of `375` GB. For example, for 2 local SSDs, set this value to `750` GB.
  * If you are [using a VM instance template for this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), create a JSON file as shown previously, except replace the [`instances` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#allocationpolicy) with the following:
        
        "instances": [
            {
                "instanceTemplate": "INSTANCE_TEMPLATE_NAME"
            }
        ],
        ...
        

Where `INSTANCE_TEMPLATE_NAME` is the name of the instance template for this job. For a job that uses local SSDs, this instance template must define and attach the local SSDs that you want the job to use. For this example, the template must define and attach a local SSD named `LOCAL_SSD_NAME`.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job with local SSD
    // Note: local SSD does not guarantee Local SSD data persistence.
    // More details here: https://cloud.google.com/compute/docs/disks/local-ssd#data_persistence
    func createJobWithSSD(w io.Writer, projectID, jobName, ssdName string) error {
    	// jobName := job-name
    	// ssdName := disk-name
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("batchClient error: %w", err)
    	}
    	defer batchClient.Close()
    
    	runn := &batchpb.Runnable{
    		Executable: &batchpb.Runnable_Script_{
    			Script: &batchpb.Runnable_Script{
    				Command: &batchpb.Runnable_Script_Text{
    					Text: "echo Hello world from script 1 for task ${BATCH_TASK_INDEX}",
    				},
    			},
    		},
    	}
    	volume := &batchpb.Volume{
    		MountPath: fmt.Sprintf("/mnt/disks/%v", ssdName),
    		Source: &batchpb.Volume_DeviceName{
    			DeviceName: ssdName,
    		},
    	}
    
    	// The size of all the local SSDs in GB. Each local SSD is 375 GB,
    	// so this value must be a multiple of 375 GB.
    	// For example, for 2 local SSDs, set this value to 750 GB.
    	disk := &batchpb.AllocationPolicy_Disk{
    		Type:   "local-ssd",
    		SizeGb: 375,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		ComputeResource: &batchpb.ComputeResource{
    			// CpuMilli is milliseconds per cpu-second. This means the task requires 1 CPU.
    			CpuMilli:  1000,
    			MemoryMib: 16,
    		},
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    		Runnables:     []*batchpb.Runnable{runn},
    		Volumes:       []*batchpb.Volume{volume},
    	}
    
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	labels := map[string]string{"env": "testing", "type": "container"}
    
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					// The allowed number of local SSDs depends on the machine type for your job's VMs.
    					// In this case, we tell the system to use "n1-standard-1" machine type, which require to attach local ssd manually.
    					// Read more about local disks here: https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options
    					MachineType: "n1-standard-1",
    					Disks: []*batchpb.AllocationPolicy_AttachedDisk{
    						{
    							Attached: &batchpb.AllocationPolicy_AttachedDisk_NewDisk{
    								NewDisk: disk,
    							},
    							DeviceName: ssdName,
    						},
    					},
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	job := &batchpb.Job{
    		Name:             jobName,
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           labels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	request := &batchpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, "us-central1"),
    		JobId:  jobName,
    		Job:    job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, request)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateLocalSsdJob {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
        // The name of a local SSD created for this job.
        String localSsdName = "SSD-NAME";
        // The machine type, which can be predefined or custom, of the job's VMs.
        // The allowed number of local SSDs depends on the machine type
        // for your job's VMs are listed on: https://cloud.google.com/compute/docs/disks#localssds
        String machineType = "c3d-standard-8-lssd";
        // The size of all the local SSDs in GB. Each local SSD is 375 GB,
        // so this value must be a multiple of 375 GB.
        // For example, for 2 local SSDs, set this value to 750 GB.
        int ssdSize = 375;
    
        createLocalSsdJob(projectId, region, jobName, localSsdName, ssdSize, machineType);
      }
    
      // Create a job that uses local SSDs
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createLocalSsdJob(String projectId, String region, String jobName,
                                          String localSsdName, int ssdSize, String machineType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                      + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) volume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
              .setDeviceName(localSsdName)
              .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/disks/" + localSsdName)
              .[addMountOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_addMountOptions_java_lang_String_)("rw")
              .[addMountOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_addMountOptions_java_lang_String_)("async")
              .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
              // Jobs can be divided into tasks. In this case, we have only one task.
              .addVolumes(volume)
              .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
              .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
              .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
              .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(3)
              .[setParallelism](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setParallelism_long_)(1)
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) policy = [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder()
              .setMachineType(machineType)
              .[addDisks](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_Builder_addDisks_com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk_)([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.html).newBuilder()
                  .setDeviceName(localSsdName)
                  // For example, local SSD uses type "local-ssd".
                  // Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd"
                  // or "pd-standard".
                  .[setNewDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_AttachedDisk_Builder_setNewDisk_com_google_cloud_batch_v1_AllocationPolicy_Disk_)([Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.html).newBuilder().[setSizeGb](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_Disk_Builder_setSizeGb_long_)(ssdSize).setType("local-ssd")))
              .build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances(
                      [InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder()
                          .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(policy)
                          .build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING))
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-local-ssd-job';
    // The name of a local SSD created for this job.
    const localSsdName = 'ssd-name';
    // The machine type, which can be predefined or custom, of the job's VMs.
    // The allowed number of local SSDs depends on the machine type
    // for your job's VMs are listed on: https://cloud.google.com/compute/docs/disks#localssds
    const machineType = 'c3d-standard-8-lssd';
    // The size of all the local SSDs in GB. Each local SSD is 375 GB,
    // so this value must be a multiple of 375 GB.
    // For example, for 2 local SSDs, set this value to 750 GB.
    const ssdSize = 375;
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: [
          '-c',
          'echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.',
        ],
      }),
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType,
      disks: [
        new batch.AllocationPolicy.AttachedDisk({
          deviceName: localSsdName,
          // For example, local SSD uses type "local-ssd".
          // Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd"
          // or "pd-standard".
          newDisk: new batch.AllocationPolicy.AttachedDisk({
            type: 'local-ssd',
            sizeGb: ssdSize,
          }),
        }),
      ],
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      instances: [{policy: instancePolicy}],
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      labels: {env: 'testing', type: 'script'},
      allocationPolicy,
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchGPUJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchGPUJob();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_local_ssd_job(
        project_id: str, region: str, job_name: str, ssd_name: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances with mounted local SSD.
        Note: local SSD does not guarantee Local SSD data persistence.
        More details here: https://cloud.google.com/compute/docs/disks/local-ssd#data_persistence
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            ssd_name: name of the local ssd to be mounted for your Job.
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
        task.runnables = [runnable]
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        volume = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
        volume.device_name = ssd_name
        volume.mount_path = f"/mnt/disks/{ssd_name}"
        task.volumes = [volume]
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        disk = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[Disk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Disk.html)()
        disk.type_ = "local-ssd"
        # The size of all the local SSDs in GB. Each local SSD is 375 GB,
        # so this value must be a multiple of 375 GB.
        # For example, for 2 local SSDs, set this value to 750 GB.
        disk.size_gb = 375
        assert disk.size_gb % 375 == 0
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # The allowed number of local SSDs depends on the machine type for your job's VMs.
        # In this case, we tell the system to use "n1-standard-1" machine type, which require to attach local ssd manually.
        # Read more about local disks here: https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "n1-standard-1"
    
        attached_disk = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.AttachedDisk.html)()
        attached_disk.new_disk = disk
        attached_disk.device_name = ssd_name
        policy.disks = [attached_disk]
    
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
    
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### Use a Cloud Storage bucket

To create a job that uses an existing Cloud Storage bucket, select one of the following methods:

  * Recommended: Mount a bucket directly to your job's VMs by specifying the bucket in the job's definition, as shown in this section. When the job runs, the bucket is automatically mounted to the VMs for your job using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).
  * Create a job with tasks that directly access a Cloud Storage bucket by using the gcloud CLI or client libraries for the Cloud Storage API. To learn how to access a Cloud Storage bucket directly from a VM, see the Compute Engine documentation for [Writing and reading data from Cloud Storage buckets](https://docs.cloud.google.com/compute/docs/disks#writetobucket).



Before you create a job that uses a bucket, create a bucket or identify an existing bucket. For more information, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) and [List buckets](https://docs.cloud.google.com/storage/docs/listing-buckets).

You can create a job that uses a Cloud Storage bucket using the Google Cloud console, gcloud CLI, Batch API, C++, Go, Java, Node.js, or Python.

The following example describes how to create a job that mounts a Cloud Storage bucket. The job also has 3 tasks that each run a script to create a file in the bucket named `output_task_TASK_INDEX.txt` where `TASK_INDEX` is the index of each task: `0`, `1`, and `2`.

### Console

To create a job that uses a Cloud Storage bucket using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-bucket-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, do the following:

           1. Select the **Script** checkbox. A field appears.

           2. In the field, enter the following script:
                  
                  echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt
                  

Replace MOUNT_PATH with the mount path that this job's runnables use to access an existing Cloud Storage bucket. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this bucket with a directory named `my-bucket`, set the mount path to `/mnt/disks/my-bucket`.

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job.

For example, enter `3`.

        3. In the **Parallelism** field, enter the number of tasks to run concurrently.

For example, enter `1` (default).

  4. Configure the **Additional configurations** page:

     1. In the left pane, click **Additional configurations**. The **Additional configurations** page opens.

     2. For each Cloud Storage bucket that you want to mount to this job, do the following:

        1. In the **Storage volume** section, click **Add new volume**. The **New volume** window appears.

        2. In the **New volume** window, do the following:

           1. In the **Volume type** section, select **Cloud Storage bucket**.

           2. In the **Storage Bucket name** field, enter the name of an existing bucket.

For example, enter the bucket you specified in this job's runnable.

           3. In the **Mount path** field, enter the mount path of the bucket (MOUNT_PATH), which you specified in the runnable.

           4. Click **Done**.

  5. Optional: Configure the [other fields for this job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

  6. Optional: To review the job configuration, in the left pane, click **Preview**.

  7. Click **Create**.




The **Job details** page displays the job that you created.

###  gcloud 

To create a job that uses a Cloud Storage bucket using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). In the job's JSON configuration file, mount the bucket in the `volumes` field.

For example, to create a job that outputs files to a Cloud Storage:

  1. Create a JSON file with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt"
                                 }
                             }
                         ],
                         "volumes": [
                             {
                                 "gcs": {
                                     "remotePath": "BUCKET_PATH"
                                 },
                                 "mountPath": "MOUNT_PATH"
                             }
                         ]
                     },
                     "taskCount": 3
                 }
             ],
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `BUCKET_PATH`: the path of the bucket directory that you want this job to access, which must start with the name of the bucket. For example, for a bucket named `BUCKET_NAME`, the path `BUCKET_NAME` represents the root directory of the bucket and the path `BUCKET_NAME/subdirectory` represents the `subdirectory` subdirectory.
     * `MOUNT_PATH`: the mount path that the job's runnables use to access this bucket. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this bucket with a directory named `my-bucket`, set the mount path to `/mnt/disks/my-bucket`.
  2. Run the following command:
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



###  API 

To create a job that uses a Cloud Storage bucket using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and mount the bucket in the `volumes` field.
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt"
                            }
                        }
                    ],
                    "volumes": [
                        {
                            "gcs": {
                                "remotePath": "BUCKET_PATH"
                            },
                            "mountPath": "MOUNT_PATH"
                        }
                    ]
                },
                "taskCount": 3
            }
        ],
        "logsPolicy": {
                "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.
  * `BUCKET_PATH`: the path of the bucket directory that you want this job to access, which must start with the name of the bucket. For example, for a bucket named `BUCKET_NAME`, the path `BUCKET_NAME` represents the root directory of the bucket and the path `BUCKET_NAME/subdirectory` represents the `subdirectory` subdirectory.
  * `MOUNT_PATH`: the mount path that the job's runnables use to access this bucket. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this bucket with a directory named `my-bucket`, set the mount path to `/mnt/disks/my-bucket`.



###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id, std::string const& bucket_name) {
        // Initialize the request; start with the fields that depend on the sample
        // input.
        google::cloud::batch::v1::CreateJobRequest request;
        request.set_parent("projects/" + project_id + "/locations/" + location_id);
        request.set_job_id(job_id);
        // Most of the job description is fixed in this example; use a string to
        // initialize it, and then override the GCS remote path.
        auto constexpr kText = R"pb(
          task_groups {
            task_count: 4
            task_spec {
              compute_resource { cpu_milli: 500 memory_mib: 16 }
              max_retry_count: 2
              max_run_duration { seconds: 3600 }
              runnables {
                script {
                  text: "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt"
                }
              }
              volumes { mount_path: "/mnt/share" }
            }
          }
          allocation_policy {
            instances {
              policy { machine_type: "e2-standard-4" provisioning_model: STANDARD }
            }
          }
          labels { key: "env" value: "testing" }
          labels { key: "type" value: "script" }
          logs_policy { destination: CLOUD_LOGGING }
        )pb";
        auto* job = request.mutable_job();
        if (!google::protobuf::TextFormat::ParseFromString(kText, job)) {
          throw std::runtime_error("Error parsing Job description");
        }
        job->mutable_task_groups(0)
            ->mutable_task_spec()
            ->mutable_volumes(0)
            ->mutable_gcs()
            ->set_remote_path(bucket_name);
        // Create a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.CreateJob(request);
        if (!response) throw std::move(response).status();
        std::cout << "Job : " << response->DebugString() << "\n";
      }

###  Go 

### Go

For more information, see the [Batch Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job that executes the specified script
    func createScriptJobWithBucket(w io.Writer, projectID, region, jobName, bucketName string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    	// jobName := "some-bucket"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	// Define what will be done as part of the job.
    	command := &batchpb.Runnable_Script_Text{
    		Text: "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt",
    	}
    
    	// Specify the Google Cloud Storage bucket to mount
    	volume := &batchpb.Volume{
    		Source: &batchpb.Volume_Gcs{
    			Gcs: &batchpb.GCS{
    				RemotePath: bucketName,
    			},
    		},
    		MountPath:    "/mnt/share",
    		MountOptions: []string{},
    	}
    
    	// We can specify what resources are requested by each task.
    	resources := &batchpb.ComputeResource{
    		// CpuMilli is milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
    		CpuMilli:  500,
    		MemoryMib: 16,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		Runnables: []*batchpb.Runnable{{
    			Executable: &batchpb.Runnable_Script_{
    				Script: &batchpb.Runnable_Script{Command: command},
    			},
    		}},
    		ComputeResource: resources,
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    		Volumes:       []*batchpb.Volume{volume},
    	}
    
    	// Tasks are grouped inside a job using TaskGroups.
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// In this case, we tell the system to use "e2-standard-4" machine type.
    	// Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					MachineType: "e2-standard-4",
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	jobLabels := map[string]string{"env": "testing", "type": "script"}
    
    	// The job's parent is the region in which the job will run
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    
    	job := batchpb.Job{
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           jobLabels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	req := &batchpb.CreateJobRequest{
    		Parent: parent,
    		JobId:  jobName,
    		Job:    &job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    
    	return nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[GCS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithMountedBucket {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
    
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
    
        // Name of the bucket to be mounted for your Job.
        String bucketName = "BUCKET_NAME";
    
        createScriptJobWithBucket(projectId, region, jobName, bucketName);
      }
    
      // This method shows how to create a sample Batch Job that will run
      // a simple command on Cloud Compute instances.
      public static void createScriptJobWithBucket(String projectId, String region, String jobName,
          String bucketName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world from task ${BATCH_TASK_INDEX}. >> "
                                  + "/mnt/share/output_task_${BATCH_TASK_INDEX}.txt")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) volume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
              .[setGcs](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setGcs_com_google_cloud_batch_v1_GCS_)([GCS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS.html).newBuilder()
                  .setRemotePath(bucketName)
                  .build())
              .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/share")
              .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(500)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .addVolumes(volume)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder().[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  .putLabels("mount", "bucket")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING).build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
        }
      }
    }

###  Node.js 

### Node.js

For more information, see the [Batch Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    /**
     * The region you want to the job to run in. The regions that support Batch are listed here:
     * https://cloud.google.com/batch/docs/get-started#locations
     */
    // const region = 'us-central-1';
    /**
     * The name of the job that will be created.
     * It needs to be unique for each project and region pair.
     */
    // const jobName = 'YOUR_JOB_NAME';
    /**
     * The name of the bucket to be mounted.
     */
    // const bucketName = 'YOUR_BUCKET_NAME';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    // Define what will be done as part of the job.
    const task = new batch.TaskSpec();
    const runnable = new batch.Runnable();
    runnable.script = new batch.Runnable.Script();
    runnable.script.text =
      'echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt';
    // You can also run a script from a file. Just remember, that needs to be a script that's
    // already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
    // exclusive.
    // runnable.script.path = '/tmp/test.sh'
    task.runnables = [runnable];
    
    const gcsBucket = new batch.GCS();
    gcsBucket.remotePath = bucketName;
    const gcsVolume = new batch.Volume();
    gcsVolume.gcs = gcsBucket;
    gcsVolume.mountPath = '/mnt/share';
    task.volumes = [gcsVolume];
    
    // We can specify what resources are requested by each task.
    const resources = new batch.ComputeResource();
    resources.cpuMilli = 2000; // in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    resources.memoryMib = 16;
    task.computeResource = resources;
    
    task.maxRetryCount = 2;
    task.maxRunDuration = {seconds: 3600};
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup();
    group.taskCount = 4;
    group.taskSpec = task;
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const allocationPolicy = new batch.AllocationPolicy();
    const policy = new batch.AllocationPolicy.InstancePolicy();
    policy.machineType = 'e2-standard-4';
    const instances = new batch.AllocationPolicy.InstancePolicyOrTemplate();
    instances.policy = policy;
    allocationPolicy.instances = [instances];
    
    const job = new batch.Job();
    job.name = jobName;
    job.taskGroups = [group];
    job.allocationPolicy = allocationPolicy;
    job.labels = {env: 'testing', type: 'script'};
    // We use Cloud Logging as it's an option available out of the box
    job.logsPolicy = new batch.LogsPolicy();
    job.logsPolicy.destination = batch.LogsPolicy.Destination.CLOUD_LOGGING;
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const response = await batchClient.createJob(request);
      console.log(response);
    }
    
    await callCreateJob();

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_script_job_with_bucket(
        project_id: str, region: str, job_name: str, bucket_name: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
            bucket_name: name of the bucket to be mounted for your Job.
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world from task ${BATCH_TASK_INDEX}. >> /mnt/share/output_task_${BATCH_TASK_INDEX}.txt"
        task.runnables = [runnable]
    
        gcs_bucket = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[GCS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.GCS.html)()
        gcs_bucket.remote_path = bucket_name
        gcs_volume = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
        gcs_volume.gcs = gcs_bucket
        gcs_volume.mount_path = "/mnt/share"
        task.volumes = [gcs_volume]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 500  # in milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
        resources.memory_mib = 16
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy.instances = [instances]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script", "mount": "bucket"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### Use a network file system

You can create a job that uses an existing network file system (NFS), such as a [Filestore file share](https://docs.cloud.google.com/filestore/docs/create-instance-gcloud), using the Google Cloud console, gcloud CLI or Batch API.

Before creating a job that uses a NFS, make sure that your network's firewall is properly configured to allow traffic between your job's VMs and the NFS. For more information, see [Configuring firewall rules for Filestore](https://docs.cloud.google.com/filestore/docs/configuring-firewall).

This following example describes how to create a job that specifies and mounts a NFS. The job also has 3 tasks that each run a script to create a file in the NFS named `output_task_TASK_INDEX.txt` where `TASK_INDEX` is the index of each task: `0`, `1`, and `2`.

### Console

To create a job that uses a NFS using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-nfs-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, do the following:

           1. Select the **Script** checkbox. A field appears.

           2. In the field, enter the following script:
                  
                  echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt
                  

Replace MOUNT_PATH with the mount path that the job's runnable use to access this NFS. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this NFS with a directory named `my-nfs`, set the mount path to `/mnt/disks/my-nfs`.

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job.

For example, enter `3`.

        3. In the **Parallelism** field, enter the number of tasks to run concurrently.

For example, enter `1` (default).

  4. Configure the **Additional configurations** page:

     1. In the left pane, click **Additional configurations**. The **Additional configurations** page opens.

     2. For each Cloud Storage bucket that you want to mount to this job, do the following:

        1. In the **Storage volume** section, click **Add new volume**. The **New volume** window appears.

        2. In the **New volume** window, do the following:

           1. In the **Volume type** section, select **Network file system**.

           2. In the **File server** field, enter the IP address of the server where the NFS you specified in this job's runnable is located.

For example, if your NFS is a Filestore file share, then specify the IP address of the Filestore instance, which you can get by [describing the Filestore instance](https://docs.cloud.google.com/filestore/docs/getting-instance-information).

           3. In the **Remote path** field, enter a path that can access the NFS you specified in the previous step.

The path of the NFS directory must start with a `/` followed by the root directory of the NFS.

           4. In the **Mount path** field, enter the mount path to the NFS (MOUNT_PATH), which you specified in the previous step.

     3. Click **Done**.

  5. Optional: Configure the [other fields for this job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

  6. Optional: To review the job configuration, in the left pane, click **Preview**.

  7. Click **Create**.




The **Job details** page displays the job that you created.

### gcloud

To create a job that uses a NFS using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). In the job's JSON configuration file, mount the NFS in the `volumes` field.

  1. Create a JSON file with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt"
                                 }
                             }
                         ],
                         "volumes": [
                             {
                                 "nfs": {
                                     "server": "NFS_IP_ADDRESS",
                                     "remotePath": "NFS_PATH"
                                 },
                                 "mountPath": "MOUNT_PATH"
                             }
                         ]
                     },
                     "taskCount": 3
                 }
             ],
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `NFS_IP_ADDRESS`: the IP address of the NFS. For example, if your NFS is a Filestore file share, then specify the IP address of the Filestore instance, which you can get by [describing the Filestore instance](https://docs.cloud.google.com/filestore/docs/getting-instance-information).
     * `NFS_PATH`: the path of the NFS directory that you want this job to access, which must start with a `/` followed by the root directory of the NFS. For example, for a Filestore file share named `FILE_SHARE_NAME`, the path `/FILE_SHARE_NAME` represents the root directory of the file share and the path `/FILE_SHARE_NAME/subdirectory` represents the `subdirectory` subdirectory.
     * `MOUNT_PATH`: the mount path that the job's runnables use to access this NFS. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this NFS with a directory named `my-nfs`, set the mount path to `/mnt/disks/my-nfs`.
  2. Run the following command:
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



### API

To create a job that uses a NFS using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and mount the NFS in the `volumes` field.
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
       {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello world from task ${BATCH_TASK_INDEX}. >> MOUNT_PATH/output_task_${BATCH_TASK_INDEX}.txt"
                            }
                        }
                    ],
                    "volumes": [
                        {
                            "nfs": {
                                "server": "NFS_IP_ADDRESS",
                                "remotePath": "NFS_PATH"
                            },
                            "mountPath": "MOUNT_PATH"
                        }
                    ]
                },
                "taskCount": 3
            }
        ],
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.
  * `NFS_IP_ADDRESS`: the IP address of the Network File System. For example, if your NFS is a Filestore file share, then specify the IP address of the Filestore instance, which you can get by [describing the Filestore instance](https://docs.cloud.google.com/filestore/docs/getting-instance-information).
  * `NFS_PATH`: the path of the NFS directory that you want this job to access, which must start with a `/` followed by the root directory of the NFS. For example, for a Filestore file share named `FILE_SHARE_NAME`, the path `/FILE_SHARE_NAME` represents the root directory of the file share and the path `/FILE_SHARE_NAME/subdirectory` represents a subdirectory.
  * `MOUNT_PATH`: the mount path that the job's runnables use to access this NFS. The path must start with `/mnt/disks/` followed by a directory or path that you choose. For example, if you want to represent this NFS with a directory named `my-nfs`, set the mount path to `/mnt/disks/my-nfs`.



###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[NFS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFS.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.cloud.batch.v1.[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateScriptJobWithNfs {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
    
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
    
        // The path of the NFS directory that you want this job to access.
        String nfsPath = "NFS_PATH";
        // The IP address of the Network File System.
        String nfsIpAddress = "NFS_IP_ADDRESS";
    
        createScriptJobWithNfs(projectId, region, jobName, nfsPath, nfsIpAddress);
      }
    
      // This method shows how to create a batch script job that specifies and mounts a NFS.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createScriptJobWithNfs(String projectId, String region, String jobName,
                                                String nfsPath, String nfsIpAddress)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).Script.newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world from task ${BATCH_TASK_INDEX}. >> "
                                  + "/mnt/share/output_task_${BATCH_TASK_INDEX}.txt")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          // Describes a volume and parameters for it to be mounted to a VM.
          [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html) volume = [Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.html).newBuilder()
              .[setNfs](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setNfs_com_google_cloud_batch_v1_NFS_)([NFS](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFS.html).newBuilder()
                  .[setServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFS.Builder.html#com_google_cloud_batch_v1_NFS_Builder_setServer_java_lang_String_)(nfsIpAddress)
                  .setRemotePath(nfsPath)
                  .build())
              .[setMountPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder.html#com_google_cloud_batch_v1_Volume_Builder_setMountPath_java_lang_String_)("/mnt/share")
              .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(500)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .addVolumes(volume)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here:
          // https://cloud.google.com/compute/docs/machine-types
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicy.newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicyOrTemplate.newBuilder()
                          .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  .putLabels("mount", "bucket")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder()
                          .[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING).build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-nfs-job';
    // The path of the NFS directory that you want this job to access.
    const nfsPath = '/your_nfs_path';
    // The IP address of the Network File System.
    const nfsIpAddress = '0.0.0.0';
    // The mount path that the job's tasks use to access the NFS.
    const mountPath = '/mnt/disks';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: [
          '-c',
          'echo Hello world from task ${BATCH_TASK_INDEX}. >> ' +
            '/mnt/share/output_task_${BATCH_TASK_INDEX}.txt',
        ],
      }),
    });
    
    // Define a volume that uses NFS.
    const volume = new batch.Volume({
      nfs: new batch.NFS({
        server: nfsIpAddress,
        remotePath: nfsPath,
      }),
      mountPath,
    });
    
    // Specify what resources are requested by each task.
    const computeResource = new batch.ComputeResource({
      // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
      cpuMilli: 500,
      // In MiB.
      memoryMib: 16,
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      volumes: [volume],
      computeResource,
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType: 'e2-standard-4',
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      instances: [{policy: instancePolicy}],
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      allocationPolicy,
      labels: {env: 'testing', type: 'script'},
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchNfsJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchNfsJob();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_job_with_network_file_system(
        project_id: str,
        region: str,
        job_name: str,
        mount_path: str,
        nfs_ip_address: str,
        nfs_path: str,
    ) -> batch_v1.Job:
        """
        Creates a Batch job with status events that mounts a Network File System (NFS).
        Function mounts an NFS volume using the provided NFS server, IP address and path.
    
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            region (str): name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name (str): the name of the job that will be created.
                It needs to be unique for each project and region pair.
            mount_path (str): The mount path that the job's tasks use to access the NFS.
            nfs_ip_address (str): The IP address of the NFS server (e.g., Filestore instance).
                Documentation on how to create a
                Filestore instance is available here: https://cloud.google.com/filestore/docs/create-instance-gcloud
            nfs_path (str): The path of the NFS directory that the job accesses.
                The path must start with a / followed by the root directory of the NFS.
    
        Returns:
            batch_v1.Job: The created Batch job object containing configuration details.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Create a runnable with a script that writes a message to a file
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = f"echo Hello world from task ${{BATCH_TASK_INDEX}}. >> {mount_path}/output_task_${{BATCH_TASK_INDEX}}.txt"
    
        # Define a volume that uses NFS
        volume = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume.html)()
        volume.nfs = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[NFS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.NFS.html)(server=nfs_ip_address, remote_path=nfs_path)
        volume.mount_path = mount_path
    
        # Create a task specification and assign the runnable and volume to it
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
        task.volumes = [volume]
    
        # Specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Create a task group and assign the task specification to it
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 1
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        # Create the job and assign the task group and allocation policy to it
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        # Create the job request and set the job and job ID
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
