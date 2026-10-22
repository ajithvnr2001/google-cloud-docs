---
url: https://docs.cloud.google.com/batch/docs/create-run-job-custom-boot-disks/
title: Create and run a job that uses custom boot disks \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:59.956908+00:00
---

# Create and run a job that uses custom boot disks  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-custom-boot-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run a job that uses custom boot disks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to customize the persistent disks used to boot each virtual machine (VM) instance that a job runs on.

Specifically, you can customize the size, type, and/or the VM operating system (OS) image for a boot disk. If you only want to customize the VM OS image, see [Specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image) instead.

To learn more about boot disks and when to configure boot disks, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create and run a job that uses a custom boot disk

Specify a custom boot disk when you are creating a job by selecting one of the following methods:

  * **Use a Compute Engine instance template that specifies a _pre-existing_ custom boot disk.** If you want to use a VM instance template while creating this job or use a pre-existing custom boot disk, complete the following steps:

    1. Create or identify a custom boot disk.

For boot disk requirements for Batch, see this document and see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview). For instructions on how to create a boot disk, see [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) in the Compute Engine documentation.

    2. Create or identify a VM instance template that includes this custom boot disk.

For instructions on how to create a VM instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) in the Compute Engine documentation.

    3. Create and run a job that includes this VM instance template.

For instructions on how to create and run the job, see [Define job resources using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template).

  * **Use the boot disk field to specify a _new_ custom boot disk.** As the following instructions explain, you can define a new custom boot disk by using the [boot disk (`bootDisk`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) when you create and run a job using the gcloud CLI or Batch API.

Specifically, you can customize the boot disk by configuring the [VM OS image (`image`), persistent disk type (`type`), and/or size (`sizeGb`) subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Disk). Batch sets a default value for any of these subfields that you choose to omit.




### gcloud

  1. Create a JSON file that specifies your job's configuration details. To specify a new custom boot disk for the job's VMs, include the [`bootDisk` field and subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy).

For example, to create a basic script job that uses a new custom boot disk, create a JSON file with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello world from task ${BATCH_TASK_INDEX}."
                                 }
                             }
                         ]
                     },
                     "taskCount": 3,
                     "parallelism": 1
                 }
             ],
             "allocationPolicy": {
               "instances": [
                 {
                   "policy": {
                     "bootDisk": {
                       "image": "VM_OS_IMAGE_URI",
                       "type": "BOOT_DISK_TYPE",
                       "sizeGb": BOOT_DISK_SIZE
                     }
                   }
                 }
               ]
             },
             "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

Replace the following:

     * `VM_OS_IMAGE_URI`: a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the VM OS image. Use one of the following options:

       * **Specify a Batch OS prefix.** To use the latest image of a specific Batch OS, use the following format:
             
             BATCH_OS_PREFIX
             

Replace `BATCH_OS_PREFIX` with one of the [Batch VM OS image prefixes](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#batch-VM-OS-image-prefixes)—for example, `batch-debian` is the prefix for the Batch Debian OS.

       * **Specify an image family.** To use the latest image from a specific image family, use the following format:
             
             projects/IMAGE_PROJECT_ID/global/images/family/IMAGE_FAMILY
             

Replace the following:

         * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, for all Batch images, specify `batch-custom-image`.
         * `IMAGE_FAMILY`: the image family, which includes one or more specific images and represents the type and [major version](https://en.wikipedia.org/wiki/Software_versioning) of the OS. For example, to see all the VM OS image families from Batch, [view a list of VM OS images](https://docs.cloud.google.com/batch/docs/view-os-images).
       * **Specify an image version.** To use a specific version of a VM OS image, use the following format:
             
             projects/IMAGE_PROJECT_ID/global/images/IMAGE_NAME
             

Replace the following:

         * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, for all Batch images, specify `batch-custom-image`.
         * `IMAGE_NAME`: the image name, which represents a specific version of a VM OS image. For example, to see all the VM OS image versions from Batch, [view a list of VM OS images](https://docs.cloud.google.com/batch/docs/view-os-images).
     * `BOOT_DISK_TYPE`: the [disk type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, either `pd-standard`, `pd-balanced`, `pd-ssd`, or `pd-extreme`. The default disk type for boot disks is `pd-balanced`.

     * `BOOT_DISK_SIZE`: the size of the new persistent boot disk in GB. This value must comply with all the [boot disk size requirements](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#boot-disk-size-requirements).

  2. To create the job, run the following [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name for this job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.
     * `JSON_CONFIGURATION_FILE`: the path to the JSON file with the job's configuration details.



### API

To create a job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify your job's configuration details. To specify the VM OS image for the job, include the [`bootDisk` field and subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy). For example, to create a basic script job that uses a new custom boot disk, make the following `POST` request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello world from task ${BATCH_TASK_INDEX}."
                            }
                        }
                    ]
                },
                "taskCount": 3,
                "parallelism": 1
            }
        ],
        "allocationPolicy": {
          "instances": [
            {
              "policy": {
                "bootDisk": {
                  "image": "VM_OS_IMAGE_URI",
                  "type": "BOOT_DISK_TYPE",
                  "sizeGb": BOOT_DISK_SIZE
                }
              }
            }
          ]
        },
        "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `VM_OS_IMAGE_URI`: a [relative resource name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the VM OS image. Use one of the following options:

    * **Specify a Batch OS prefix.** To use the latest image of a specific Batch OS, use the following format:
          
          BATCH_OS_PREFIX
          

Replace `BATCH_OS_PREFIX` with one of the [Batch VM OS image prefixes](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#batch-VM-OS-image-prefixes)—for example, `batch-debian` is the prefix for the Batch Debian OS.

    * **Specify an image family.** To use the latest image from a specific image family, use the following format:
          
          projects/IMAGE_PROJECT_ID/global/images/family/IMAGE_FAMILY
          

Replace the following:

      * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, for all Batch images, specify `batch-custom-image`.
      * `IMAGE_FAMILY`: the image family, which includes one or more specific images and represents the type and [major version](https://en.wikipedia.org/wiki/Software_versioning) of the OS. For example, to see all the VM OS image families from Batch, [view a list of VM OS images](https://docs.cloud.google.com/batch/docs/view-os-images).
    * **Specify an image version.** To use a specific version of a VM OS image, use the following format:
          
          projects/IMAGE_PROJECT_ID/global/images/IMAGE_NAME
          

Replace the following:

      * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, for all Batch images, specify `batch-custom-image`.
      * `IMAGE_NAME`: the image name, which represents a specific version of a VM OS image. For example, to see all the VM OS image versions from Batch, [view a list of VM OS images](https://docs.cloud.google.com/batch/docs/view-os-images).
  * `BOOT_DISK_TYPE`: the [disk type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, either `pd-standard`, `pd-balanced`, `pd-ssd`, or `pd-extreme`. The default disk type for boot disks is `pd-balanced`.

  * `BOOT_DISK_SIZE`: the size of the new persistent boot disk in GB. This value must comply with all the [boot disk size requirements](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#boot-disk-size-requirements).




## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn more about [boot disks and VM OS images](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).
  * Learn more about [creating a job](https://docs.cloud.google.com/batch/docs/create-run-job).
  * Learn how to [view jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
