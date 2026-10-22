---
url: https://docs.cloud.google.com/batch/docs/create-run-job-reservation/
title: Ensure resource availability using VM reservations \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:31.018045+00:00
---

# Ensure resource availability using VM reservations  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Ensure resource availability using VM reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create jobs that run on reserved resources and how to block jobs from consuming reservations.

_Reservations_ are a feature of Compute Engine. A reservation provides a very high level of assurance in obtaining capacity for one or more VMs with the specified hardware configuration. A reservation for a VM incurs the costs of that VM from when you create and until you delete the reservation. But, while you are consuming that VM, the total cost is equivalent to a VM without a reservation.

Generally, reservations are useful when capacity availability is critically important or to prevent errors for obtaining resources. For Batch specifically, consider using dedicated reservations to help minimize job scheduling time, or attempt to use existing reservations while they're not being used. If you have underused reservations—such as reservations required for [committed-use discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)—you can configure jobs to attempt to consume them while they're not being used to try to help optimize your incurred costs. Alternatively, if you want to prioritize resource availability for other workloads in your project, you can explicitly block a job from consuming reservations.

To learn more about reservations, see the [Compute Engine documentation for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview). To learn more about choosing which obtainability features to use for your workload, see [Improve resource obtainability](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. Make sure you have the permissions to [create a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) or [view an existing reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view) that you want a job's VMs to consume as needed. 
  3. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Restrictions

In addition to the [general restrictions for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions), Batch also has the following restrictions:

  * A job's VMs can't consume reservations if either specify a [compact placement policy](https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy).
  * If you create a job using the Google Cloud console, its VMs automatically consume matching reservations. To consume a specific reservation or block VMs from consuming reservations, you must define the `reservation` field when you create a job by using the gcloud CLI or Batch API instead.



## Requirements

This section summarizes the requirements for a job's VMs to consume a reservation. For more information about all the requirements, see the [general requirements for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) in the Compute Engine documentation and the procedure for planning your configuration later in this document.

  * For a job's VMs to be generally capable of consuming a reservation, all the following conditions must be met:

    * The job and reservation must specify VM properties that exactly match.

    * You must comply with all the restrictions in this document and all the other general requirements for reservations.

  * For each of a job's VMs to successfully consume a reservation, the reservation must have unused capacity available during the VM's run time.

A reservation's unused capacity is the difference between its VM count and the number of VMs currently consuming it. VMs attempt to consume reservations whenever you have unused reservation capacity. So, a VM can start consuming a reservation when the VM is created or later in its run time. A VM doesn't stop consuming a reservation until the VM stops running or the reservation is deleted.

Depending on your total unused reservation capacity, none, some, or all of a job's VMs might consume reservations, and the amount of reserved VMs might vary throughout the job's run time.




## Create and run a job that can consume reserved VMs

  1. **Plan your configuration.** To make sure your job and reservation are compatible, complete the following steps. 

If you want to consume a reservation that already exists, you must create a job with a corresponding configuration. Otherwise, if you plan to create a new reservation, select the configuration options that you prefer. 

     1. **Determine the reservation properties.** Due to the restrictions, the share type must be _single-project_ , which is the default option for a reservation. Determine the values that you want to use for the following reservation properties:

        * Consumption type*
        * VM count†

*The reservation's [consumption type](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) (_specifically targeted_ or _automatically consumed_) determines which VMs can consume the reservation.

†The [VM count](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#vm-count) represents total capacity of a reservation. When deciding this value, consider [the job's number of VMs](https://docs.cloud.google.com/batch/docs/create-run-job#vms-per-job).

     2. **Determine the VM properties for the job and reservation.** Due to the restrictions, neither the job nor the reservation can specify a compact placement policy, which is the default option for both reservations and jobs. Determine the values that you want to use for the following VM properties, which must match _exactly_ for the reservation and the job: 

        * Project
        * Zone*
        * Machine type†
        * Minimum CPU platform† (if any‡)
        * GPU type and count† (if any‡)
        * Local SSD type and count† (if any‡)
        * Reservation affinity†#

*The job VM's must be located in the same zone as the reserved VMs. If using the `allowedLocations[]` field, you must include this zone in the job's `allowedLocations[]` field. Otherwise, if omitting the `allowedLocations[]` field, you must set the job's location to the region that contains this zone.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

        * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
        * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

†The job must define all these properties using either the `policy` subfields or [a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template). A job can't specify a combination of `policy` subfields and a template.

‡ An optional field can't be defined for one resource and omitted from the other. Define or omit the optional field for both the reservation and the job. If the job specifies a VM instance template, this also applies to the fields of the specified template.

#The reservation's consumption type determines the reservation affinity required for the job's VMs, which you must specify in the job as follows:

        * If the job is using a VM instance template, the template needs to [configure the reservation affinity as explained in the reservations documentation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).
        * If the job isn't using a template and the reservation is specifically targeted, specify the name of the reservation in the job's `reservation` field.
        * Otherwise, if the job isn't using a template and the reservation is automatically consumed, omit the job's `reservation` field.

  2. **Prepare the reservation.** If you haven't already, [create the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) that you want the job's VMs to consume. Make sure the reservation has the properties you planned.

  3. **Create and run the job.** You can create and run a job that consumes VMs from the prepared reservation by using the gcloud CLI or Batch API:

**Important:** Due to a known issue, jobs that consume reserved VMs might be incorrectly delayed or prevented from running. To workaround this issue, add a label with the name `goog-batch-skip-quota-check` and value `true` to the [job-level `labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#resource:-job). For more information, see [Known issues](https://docs.cloud.google.com/batch/docs/known-issues#underestimated-reservations-quota).

### gcloud

     1. Create a JSON file that specifies the job's configuration details that sets the [VM instance resource (`instances[]`) subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate) to exactly match the VM properties of a reservation.

For example, to create a basic script job that consumes VMs from a reservation, create a JSON file with the following contents.
            
            {
              "taskGroups": [
                {
                  "taskSpec": {
                    "runnables": [
                      {
                        "script": {
                          "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                        }
                      }
                    ]
                  },
                  "taskCount": 3
                }
              ],
              "allocationPolicy": {
                "instances": [
                  {
                    VM_RESOURCES
                  }
                ],
              },
              "logsPolicy": {
                "destination": "CLOUD_LOGGING"
              }
            }
            

Replace `VM_RESOURCES` with the VM resources that match the reservation that you want to the job to consume by specifying the `instances[]` subfields that you planned in the previous steps.

For example, start from the following value for `VM_RESOURCES`:
            
            "installGpuDrivers": INSTALL_GPU_DRIVERS,
            "policy": {
              "machineType": "MACHINE_TYPE",
              "minCpuPlatform": "MIN_CPU_PLATFORM",
              "provisioningModel": "PROVISIONING_MODEL",
              "accelerators": [
                {
                  "type": "GPU_TYPE",
                  "count": GPU_COUNT
                }
              ],
              "disks": [
                {
                  "newDisk": {
                    "sizeGb": LOCAL_SSD_SIZE,
                    "type": "local-ssd"
                  },
                  "deviceName": "LOCAL_SSD_NAME"
                }
              ],
              "reservation": "SPECIFIC_RESERVATION_URL"
            }
            

Before using this value, update it based on all the following questions:

        1. Do you want to use an instance template?

           * **Yes:** Replace the `policy` field with the `instanceTemplate` field and specify an existing VM instance template that matches the reservation. For example, see the instructions for [using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template#create-job-instance-template) and verify the `properties` fields of the instance template by reviewing the remaining questions in this document. If the reservation uses GPUs or local SSDs, then you also need to [configure the `installGpuDrivers` field](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#install-gpu-drivers) and [configure the `volumes[]` field for local SSDs](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-local-ssd) respectively. Then, submit the job.

           * **No:** Replace `MACHINE_TYPE` with the same machine type as the reservation.

        2. Does the reservation include a minimum CPU platform?

           * **Yes:** Replace `MIN_CPU_PLATFORM` with the same minimum CPU platform.

           * **No:** Remove the `minCpuPlatform` field.

        3. Does the reservation include GPUs?

           * **Yes:** Complete the following steps.

             1. Replace `INSTALL_GPU_DRIVERS` and specify any additional fields that are required to install GPU drivers for this job. For instructions, see [Install GPU drivers](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#install-gpu-drivers).
             2. Replace `PROVISIONING_MODEL` based on your [consumption option](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#select-provisioning-method): either `STANDARD` (default) for reservations or `RESERVATION_BOUND` for calendar-mode reservations.
             3. Update the `accelerators[]` field based on your GPU machine type:

                * If you are using an accelerator-optimized machine type, remove the `accelerators[]` field.
                * Otherwise, if you are using an N1 accelerator-optimized machine type, replace `GPU_TYPE`, and `GPU_COUNT` to match the reservation.
           * **No:** Remove the `installGpuDrivers` field, the `provisioningModel` field, and the `accelerators[]` field.

        4. Does the reservation include local SSDs?

           * **Yes:** Replace `LOCAL_SSD_SIZE` and `LOCAL_SSD_NAME` to match the reservation, and mount the local SSDs by adding the [`volumes[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.volumes) to the job. For example, see the code sample for [using local SSDs](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-local-ssd).

           * **No:** Remove the `disks[]` field.

        5. Does the reservation use the specifically targeted consumption type?

**Tip:** If you set `PROVISIONING_MODEL` to `RESERVATION_BOUND`, the answer is yes. Otherwise, if you set `PROVISIONING_MODEL` to `STANDARD`, then view the reservation to check. For more information, see [Consume a specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation) in the Compute Engine documentation.
           * **Yes:** Replace `SPECIFIC_RESERVATION_URL` with the following:
                 
                 projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME
                 

Replace the following:

             * `RESERVATION_OWNER_PROJECT_ID` with the project ID of the project where the reservation exists.

             * `RESERVATION_NAME` with the name of the reservation.

**Tip:** If the reservation was created in the current project, you can specify only RESERVATION_NAME instead.
           * **No:** Remove the `reservation` field.

For example, suppose you're using an automatically consumed reservation for `n2-standard-32` VMs that doesn't specify any minimum CPU platform, GPUs, or local SSDs. Additionally, you don't want to specify a VM instance template. In that case, you must replace `VM_RESOURCES` with the following value:
    
    "policy": {
      "machineType": "n2-standard-32"
    }
    

     2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
            
            gcloud batch jobs submit JOB_NAME \
              --location LOCATION \
              --config JSON_CONFIGURATION_FILE
            

Replace the following:

        * `JOB_NAME`: the name of the job.

        * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job. To consume a reservation, the job's Compute Engine resources must be created in the same zone as the reservation.

        * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.

### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that sets the [VM instance resource (`instances[]`) subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate) to exactly match the VM properties of a reservation.

For example, to create a basic script job that consumes VMs from a reservation, make the following request:
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            VM_RESOURCES
          }
        ],
      },
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

     * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job. To consume a reservation, the job's Compute Engine resources must be created in the same zone as the reservation.

     * `JOB_NAME`: the name of the job.

     * `VM_RESOURCES`: the VM resources that match the reservation that you want to the job to consume by specifying the `instances[]` subfields that you planned in the previous steps.

For example, start from the following value for `VM_RESOURCES`:
           
           "installGpuDrivers": INSTALL_GPU_DRIVERS,
           "policy": {
             "machineType": "MACHINE_TYPE",
             "minCpuPlatform": "MIN_CPU_PLATFORM",
             "provisioningModel": "PROVISIONING_MODEL",
             "accelerators": [
               {
                 "type": "GPU_TYPE",
                 "count": GPU_COUNT
               }
             ],
             "disks": [
               {
                 "newDisk": {
                   "sizeGb": LOCAL_SSD_SIZE,
                   "type": "local-ssd"
                 },
                 "deviceName": "LOCAL_SSD_NAME"
               }
             ],
             "reservation": "SPECIFIC_RESERVATION_URL"
           }

Before using this value, update it based on all the following questions:

       1. Do you want to use an instance template?

          * **Yes:** Replace the `policy` field with the `instanceTemplate` field and specify an existing VM instance template that matches the reservation. For example, see the instructions for [using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template#create-job-instance-template) and verify the `properties` fields of the instance template by reviewing the remaining questions in this document. If the reservation uses GPUs or local SSDs, then you also need to [configure the `installGpuDrivers` field](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#install-gpu-drivers) and [configure the `volumes[]` field for local SSDs](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-local-ssd) respectively. Then, submit the job.

          * **No:** Replace `MACHINE_TYPE` with the same machine type as the reservation.

       2. Does the reservation include a minimum CPU platform?

          * **Yes:** Replace `MIN_CPU_PLATFORM` with the same minimum CPU platform.

          * **No:** Remove the `minCpuPlatform` field.

       3. Does the reservation include GPUs?

          * **Yes:** Complete the following steps.

            1. Replace `INSTALL_GPU_DRIVERS` and specify any additional fields that are required to install GPU drivers for this job. For instructions, see [Install GPU drivers](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#install-gpu-drivers).
            2. Replace `PROVISIONING_MODEL` based on your [consumption option](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#select-provisioning-method): either `STANDARD` (default) for reservations or `RESERVATION_BOUND` for calendar-mode reservations.
            3. Update the `accelerators[]` field based on your GPU machine type:

               * If you are using an accelerator-optimized machine type, remove the `accelerators[]` field.
               * Otherwise, if you are using an N1 accelerator-optimized machine type, replace `GPU_TYPE`, and `GPU_COUNT` to match the reservation.
          * **No:** Remove the `installGpuDrivers` field, the `provisioningModel` field, and the `accelerators[]` field.

       4. Does the reservation include local SSDs?

          * **Yes:** Replace `LOCAL_SSD_SIZE` and `LOCAL_SSD_NAME` to match the reservation, and mount the local SSDs by adding the [`volumes[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.volumes) to the job. For example, see the code sample for [using local SSDs](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-local-ssd).

          * **No:** Remove the `disks[]` field.

       5. Does the reservation use the specifically targeted consumption type?

          * **Yes:** Replace `SPECIFIC_RESERVATION_URL` with the following:
                
                projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME
                

Replace the following:

            * `RESERVATION_OWNER_PROJECT_ID` with the project ID of the project where the reservation exists.

            * `RESERVATION_NAME` with the name of the reservation.

**Tip:** If the reservation was created in the current project, you can specify only RESERVATION_NAME instead.
          * **No:** Remove the `reservation` field.

For example, suppose you're using an automatically consumed reservation for `n2-standard-32` VMs that doesn't specify any minimum CPU platform, GPUs, or local SSDs. Additionally, you don't want to specify a VM instance template. In that case, you must replace `VM_RESOURCES` with the following value:
    
    "policy": {
      "machineType": "n2-standard-32"
    }




## Create and run a job that can't consume reserved VMs

To block a job from consuming any reservations, set the [`reservation` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicy.FIELDS.reservation) to `NO_RESERVATION`. For more information about preventing reservation consumption, see [Prevent compute instances from consuming reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption) in the Compute Engine documentation.

You can create and run a job that can't consume any reserved VMs by using the gcloud CLI or Batch API.

### gcloud

  1. Create a JSON file that specifies the job's configuration details and sets the `reservation` field to `NO_RESERVATION`.

For example, to create a basic script job that can't consume reservations, create a JSON file with the following contents:
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "script": {
                       "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                     }
                   }
                 ]
               },
               "taskCount": 3
             }
           ],
           "allocationPolicy": {
             "instances": [
               {
                 "policy": {
                   **"reservation" : "NO_RESERVATION"**
                 }
               }
             ],
           },
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that sets the `reservation` field to `NO_RESERVATION`.

For example, to create a basic script job that can't consume reservations, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            "policy": {
              **"reservation" : "NO_RESERVATION"**
            }
          }
        ],
      },
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.




## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
