---
url: https://docs.cloud.google.com/batch/docs/create-run-job-gpus/
title: Create and run a job that uses GPUs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:18.909624+00:00
---

# Create and run a job that uses GPUs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run a job that uses GPUs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create and run a job that uses a graphics processing unit (GPU). To learn more about the features and restrictions for GPUs, see [About GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus) in the Compute Engine documentation.

When you create a Batch job, you can optionally use GPUs to accelerate specific workloads. Common use cases for jobs that use GPUs include intensive data processing and artificial intelligence workloads (AI) such as machine learning (ML).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create a job that uses GPUs

To create a job that uses GPUs, do the following:

  1. Plan the requirements for a job that uses GPUs.
  2. Create a job with the requirements and methods that you identified. For examples of how to create a job using the recommended options, see Create an example job that uses GPUs in this document.



### Plan the requirements for a job that uses GPUs

Before creating a job that uses GPUs, plan the job's requirements as explained in the following sections:

  1. Select the GPU machine type and consumption option
  2. Install the GPU drivers
  3. Define compatible VM resources



#### Step 1: Select the GPU machine type and consumption option

A job's requirements vary based on your preferred GPU machine type and consumption option, and the options for each might be interdependent.

To select the GPU machine type and consumption option for your job, complete the following steps:

  1. Identify and select your priority:

     * If you want to prioritize performance and base pricing, then see the Select the GPU machine type section in this document.
     * If you want to prioritize resource availability or discounts, then see the Select the consumption option section in this document.
  2. Make the remaining selection based on what is compatible with your first selection.

     1. To identify the options that are compatible with your first selection, see [Consumption option availability by machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#consumption_option_availability_by_machine_type) in the Compute Engine documentation.

     2. See the remaining section for Select the consumption option or Select the GPU machine type respectively.




##### Select the GPU machine type

To select the GPU machine type for a job and understand its job requirements, complete the following steps:

  1. **Select a GPU machine type:** To review the available _GPU machine types_ (the valid combinations of GPU type, number of GPUs, and machine type (vCPUs and memory)) and their recommended use cases, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) and [Accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation.

  2. **Understand the job requirements for your GPU machine type:** The fields required for a job to specify a GPU machine type vary based on the categories in the following table:

GPU machine types and their job requirements  
---  
**GPUs for accelerator-optimized VMs** : VMs with a machine type from the [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) have a specific type and number of these GPUs automatically attached. | **To use GPUs for accelerator-optimized VMs, we recommend that you specify the machine type.** Each accelerator-optimized machine type supports only a specific type and number of GPUs, so it's functionally equivalent whether you do or don't specify those values in addition to the accelerator-optimized machine type. Specifically, Batch also supports specifying only the type and number of GPUs for accelerator-optimized VMs, but the resulting vCPU and memory options are often very limited. As a result, we recommend that you verify that the available vCPU and memory options are compatible with the job's task requirements.  
**GPUs for N1 VMs** : These GPUs require you to specify the type and amount to attach to each VM and must be attached to VMs with a machine type from the [N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines). | **To use GPUs for N1 VMs, we recommend that you specify at least the type of GPUs and number of GPUs.** Ensure that the combination of values matches one of the valid [GPU options for the N1 machine types](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). The vCPU and memory options for N1 VMs that use any specific type and number GPUs is quite flexible. Unless you create the job using the Google Cloud console, you can let Batch automatically select a machine type that meets the job's task requirements. **Note:** Batch _doesn't_ use GPUs for a job that specifies an N1 machine type but specifies neither a GPU type nor number of GPUs.  



##### Select the consumption option

This section summarizes how to select the consumption option for a job and the job requirements for each option.

**Tip:** For a job that uses GPUs, we recommend that most users select the consumption option as follows: 

  * Unless one of the following conditions is true, use Flex-start VMs (preferred, if it meets your requirements) or on-demand.
  * If your job requires very high assurance of resource availability or if you have any unused reservations that you can't delete, then use calendar-mode reservations (preferred, if it meets your requirements) or reservations.
  * If your workload is very fault-tolerant, then you might be able to reduce costs by trying to use Spot VMs.



The available consumption options for Batch and their job requirements are explained in the following table. This table lists the consumption options based on their use cases: from roughly highest to lowest obtainability. Ensure that the consumption option that you select also meets your requirements for pricing, run time, and machine type support. For more information about choosing a consumption option, also see [Improve resource obtainability](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview), the [Compute Engine documentation for provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), and the [AI Hypercomputer documentation for consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

Consumption options and their job requirements  
---  
**Reservations**

  * **Use case** : We recommend reservations for jobs if you want a very high level of assurance of resource availability and can't use calendar-mode reservations, or if you already have existing reservations that might be unused.
  * **Details** : After a reservation is created, it incurs the costs of the specified VMs at the same price as running the VMs until you delete the reservation. VMs that are consuming a reservation don't incur separate costs, but reservations incur costs regardless of consumption.Learn more about [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) in the Compute Engine documentation.

| **Batch uses reservations for jobs that can consume unused reserved VMs.** For more information about the job requirements for consuming reservations, see the [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) page.  
**Calendar-mode reservations**

  * **Use case** : We recommend calendar-mode reservations for jobs if you want to use a GPU machine type that supports calendar-mode reservations and need a very high level of assurance of resource availability for at least 1 day and up to 90 days.
  * **Details** : Before creating a job, you must request or identify a calendar-mode reservation that you can consume. If Compute Engine fulfills a future reservation request in calendar mode, the auto-created calendar-mode reservation incurs the same cost as running the specified VMs for the entire reservation period at [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing), which offers discounts of up to 53% off of on-demand pricing. After you identify an auto-created calendar-mode reservation that you can use, creating a job that consumes a calendar-mode reservation is very similar to creating a job that consumes a reservation.Learn more about [calendar-mode reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview) in the Compute Engine documentation.

| **Batch uses calendar-mode reservations for jobs that do all of the following:**

  * **Set the`provisioningModel` field to `RESERVATION_BOUND`.**
  * **Specifically target a calendar-mode reservation.** For more information about the job requirements for consuming reservations, see the [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) page.
**Tip:** Although you can run the job in any of the [locations that offer your GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table\)), using the [recommended zones for Dynamic Workload Scheduler](https://docs.cloud.google.com/batch/docs/locations#recommended-zones-dws) increases the likelihood that your request is approved. 
  
**Flex-start VMs**

  * **Use case** : We recommend Flex-start VMs if your job can withstand best-effort obtainability in exchange for discounted pricing and up to 7 days to finish running. Compared to on-demand and Spot VMs, Flex-start VMs can make it easier for you to simultaneously access many GPU resources. For example, Flex-start VMs can be helpful for job scheduling by mitigating delays or issues that are caused by [resource unavailability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability).
  * **Details** : If a request to create a job that uses Flex-start VMs is fulfilled, the VMs are charged at [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing), which offers discounts of up to 53% off of on-demand pricing.Learn more about [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig) in the Compute Engine documentation.

| **Batch uses Flex-start VMs for jobs that do all of the following:**

  * **Set the`provisioningModel` field to `FLEX_START`.**
  * **Block reservations.** Specifically, the job must set the `reservation` field to `NO_RESERVATION`. For more information, see [Create and run a job that can't consume reserved VMs](https://docs.cloud.google.com/batch/docs/create-run-job-reservation#create-run-job-block-reservation).
**Tip:** Although you can run the job in any of the [locations that offer your GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table\)), using the [recommended zones for Dynamic Workload Scheduler](https://docs.cloud.google.com/batch/docs/locations#recommended-zones-dws) increases the likelihood that your request is approved. 
  
**On-demand**

  * **Use case** : We recommend on-demand for most other jobs by default.1
  * **Details** : On-demand is usually the default way to access Compute Engine VMs. On-demand lets you access resources (if available) when requested. The resources are deleted until either the job finishes or the [run time limit](https://docs.cloud.google.com/batch/quotas#max-job-duration) is reached.

| **Batch uses on-demand for most other jobs by default. If you want to ensure that a job uses on-demand, do all of the following:** 1

  * **Set the`provisioningModel` field to `STANDARD`.**
  * **Block reservations.** To prevent a job from automatically consuming using compatible reservations, set the `reservation` field to `NO_RESERVATION`. For more information, see [Create and run a job that can't consume reserved VMs](https://docs.cloud.google.com/batch/docs/create-run-job-reservation#create-run-job-block-reservation).

1**Exception: For jobs that use the A3 machine series, the default behavior is unique, and we recommend that you don't use on-demand and don't leave the`provisioningModel` field undefined; instead, use the job requirements for Flex-start VMs.** Using on-demand is not recommended for the A3 machine series due to low resource availability. Consequently, if a job uses the A3 machine series, blocks reservations, and has the `provisioningModel` field either undefined or set to `STANDARD`, the default consumption option is unique: The behavior is similar to Flex-start VMs, which limits the run time to 7 days; however, it's not recommended because these jobs _don't_ receive discounts from Dynamic Workload Scheduler pricing. If your job with A3 VMs can tolerate a run time limit of 7 days, we recommend that you use Flex-start VMs instead of on-demand. Otherwise, you can't ensure that jobs with A3 VMs use on-demand unless you set `provisioningModel` to `STANDARD` and manually verify that the job can't consume reservations, without setting the `reservation` field to `NO_RESERVATION`.  
**Spot VMs**

  * **Use case** : We recommend that you use Spot VMs to reduce costs for [fault-tolerant workloads](https://docs.cloud.google.com/batch/docs/automate-task-retries). **Important:** Spot VMs have limited availability. To prevent resource availability errors, [view resource availability](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability) before you create your job. If you keep encountering errors because resources are unavailable, then use a different consumption option.
  * **Details** : If a request to create a job that uses Spot VMs is fulfilled, the VMs are charged at [Spot VMs pricing](https://cloud.google.com/spot-vms/pricing), which can change often and might provide the largest discount, up to 91% off of on-demand pricing. However, Spot VMs might not always be available and can be preempted at any time. Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) in the Compute Engine documentation and [recommendations for jobs with Spot VMs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview#spot-vms-recommendations).

| **Batch uses Spot VMs for jobs that do all of the following:**

  * **Set the`provisioningModel` field to `SPOT`.**
  * (Optional) **Block reservations.** You can't use Spot VMs with reservations. Specifically, the job can optionally set the `reservation` field to `NO_RESERVATION`. For more information, see [Create and run a job that can't consume reserved VMs](https://docs.cloud.google.com/batch/docs/create-run-job-reservation#create-run-job-block-reservation).

  
  
#### Step 2: Install the GPU drivers

To use GPUs for a job, you must install the GPU drivers. To install GPU drivers, select one of the following methods:

  * **Install GPU drivers automatically (recommended if possible):** As shown in the examples, to let Batch fetch the required GPU drivers from a third-party location and install them on your behalf, set the `installGpuDrivers` field for the job to `true`. This method is recommended if your job does not require you to install drivers manually.

Optionally, if you need to specify which version of the GPU driver that Batch installs, also set the [`driverVersion` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Accelerator.FIELDS.driver_version).

  * **Install GPU drivers manually:** This method is required if any of the following are true:

**Important:** Due to a known issue, you might also need to install drivers manually for jobs that specify some Compute Engine images. For more information, see [Jobs with GPUs and VM OS images with outdated kernels fail only when automatically installing drivers](https://docs.cloud.google.com/batch/docs/known-issues#jobs-with-GPUs-image-outdated-kernel-fail-automatically-install-drivers).
    * A job uses both script and container runnables and does not have [internet access](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs). For more information about the access a job has, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview).
    * A job uses a custom VM image. To learn more about VM OS images and which VM OS images you can use, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).

To manually install the required GPU drivers, the following method is recommended:

    1. Create a custom VM image that includes the GPU drivers.

       1. To install GPU drivers, run an installation script based on the OS that you want to use:

          * [GPU drivers for Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-gpus#install)
          * [GPU drivers for other OSes](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#installation_scripts)
       2. If your job has any container runnables and does not use Container-Optimized OS, you must also install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

    2. When you create and submit a job that uses GPUs, [specify the custom VM image](https://docs.cloud.google.com/batch/docs/specify-vm-os-image) that includes the GPU drivers, and set the [`installGpuDrivers` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate) for the job to `false` (default).




#### Step 3: Define compatible VM resources

To learn about the requirements and options for defining the VM resources for a job, see [Job resources](https://docs.cloud.google.com/batch/docs/create-run-job#resources).

In summary, you must do all of the following when defining the VM resources for a job that uses GPUs:

  * Ensure that the GPU machine type is available in the location of your job's VMs.

To learn where GPU machine types are available, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) in the Compute Engine documentation.

  * If you specify the job's machine type, ensure that machine type has enough vCPUs and memory for the job's task requirements. Specifying the job's machine type is required whenever you create a job using the Google Cloud console and is recommended whenever you are creating a job that uses GPUs for accelerator-optimized VMs.

  * Ensure you define the VM resources for a job using a valid method:

    * **Define VM resources directly by using the`instances[].policy` field (recommended if possible).** This method is shown in the examples.
    * **Define VM resources through a template by using the`instances[].instanceTemplate` field.** This method is required to manually install GPU drivers through a custom image. For more information, see [Define job resources using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template).



### Create an example job that uses GPUs

The following sections explain how to create an example job for each consumption option. Specifically, the example jobs use the recommended options: all install GPU drivers automatically, and all directly define VM resources.

Consumption option | Example job instructions  
---|---  
_Reservations_ or _calendar-mode reservations_ |  [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation)  
_Flex-start VMs_ |  Use GPUs and Flex-start VMs  
_On-demand_ or _Spot VMs_ |  Select one of the following options based on your GPU machine type:

  * Use GPUs for accelerator-optimized VMs
  * Use GPUs for N1 VMs

  
  
#### Use GPUs and Flex-start VMs

You can create a job that uses GPUs for A3 VMs through Dynamic Workload Scheduler using gcloud CLI or Batch API.

### gcloud

  1. Create a JSON file that installs GPU drivers, specifies a GPU machine type that supports Flex-start VMs, blocks reservations, and runs in a location that supports the GPU machine type.

For example, to create a basic script job that uses Flex-start VMs and GPUs for accelerator-optimized VMs, create a JSON file with the following contents.

**Tip:** If you want to use Flex-start VMs and GPUs for N1 VMs, update the following JSON file to use the `accelerators` field instead of (or in addition to) the `machineType` field as demonstrated in Use GPUs for N1 VMs.
         
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
                         "installGpuDrivers": INSTALL_GPU_DRIVERS,
                         "policy": {
                             "provisioningModel":"FLEX_START",
                             "machineType": "MACHINE_TYPE",
                             "reservation": "NO_RESERVATION"
                         }
                     }
                 ],
                 "location": {
                     "allowedLocations": [
                         "ALLOWED_LOCATIONS"
                     ]
                 }
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

     * `MACHINE_TYPE`: a GPU machine type that supports Flex-start VMs. For more information, see [Consumption option availability by machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#consumption_option_availability_by_machine_type) in the Compute Engine documentation.

     * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

       * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
       * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

       * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
       * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that installs GPU drivers, specifies a GPU machine type that supports Flex-start VMs, blocks reservations, and runs in a location that supports the GPU machine type.

For example, to create a basic script job that uses Flex-start VMs and GPUs for accelerator-optimized VMs, make the following request:

**Tip:** If you want to use Flex-start VMs and GPUs for N1 VMs, update the following JSON file to use the `accelerators` field instead of (or in addition to) the `machineType` field as demonstrated in Use GPUs for N1 VMs.
    
    
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
                    "installGpuDrivers": INSTALL_GPU_DRIVERS,
                    "policy": {
                        "provisioningModel":"FLEX_START",
                        "machineType": "MACHINE_TYPE",
                        "reservation": "NO_RESERVATION"
                    }
                }
            ],
            "location": {
                "allowedLocations": [
                    "ALLOWED_LOCATIONS"
                ]
            }
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

  * `MACHINE_TYPE`: a GPU machine type that supports Flex-start VMs. For more information, see [Consumption option availability by machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#consumption_option_availability_by_machine_type) in the Compute Engine documentation.

  * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

    * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
    * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
    * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).




#### Use GPUs for accelerator-optimized VMs

You can create a job that uses GPUs for accelerator-optimized VMs using the Google Cloud console, gcloud CLI, Batch API, Java, Node.js, or Python.

### Console

**Important:** The Google Cloud console only supports automatically installing the default version of GPU drivers. To install other versions of GPU drivers or manually install GPU drivers, use a different method to create the job.

To create a job that uses GPUs by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-gpu-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, to create a basic script job, do the following:

           1. Select the **Script** checkbox. A field appears.

           2. In the field, enter the following script:
                  
                  echo Hello world from task ${BATCH_TASK_INDEX}.
                  

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job.

For example, enter `3`.

        3. Optional: In the **Parallelism** field, enter the number of tasks to run concurrently.

For example, enter `1` (default).

  4. Configure the **Resource specifications** page:

     1. In the left pane, click **Resource specifications**. The **Resource specifications** page opens.

     2. In the **VM provisioning model** section, select one of the following options for the consumption option for this job's VMs:

        * If your job can withstand preemption and you want discounted Spot VMs, select **Spot**.

        * Otherwise, to use on-demand VMs, select **Standard** (default).

     3. Select the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.

        1. In the **Region** field, select a region.

        2. In the **Zone** field, do one of the following:

           * If you want to restrict this job to run in a specific zone only, select a zone.

           * Otherwise, select **any** (default).

**Important:** Ensure that you specify only [locations that offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job.
     4. Select the GPU machine type for this job's VMs:

        1. In the machine family options, click **GPUs**.

        2. In the **GPU type** field, select the type of GPUs. Then, in the **Number of GPUs** field, select the number of GPUs for each VM.

If you selected one of the [GPU types for accelerator-optimized VMs](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads), then the **Machine type** field only allows one option for the machine type based on the type and number of GPUs that you selected.

        3. To automatically install GPU drivers, select **GPU driver installation** (default).

     5. Configure the amount of VM resources required for each task:

**Important:** Ensure that the GPU machine type has enough [VM resources for the job's task requirements](https://docs.cloud.google.com/batch/docs/create-run-job#job-vm-resource-requirements).
        1. In the **Cores** field, enter the amount of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms) per task.

For example, enter `1` (default).

        2. In the **Memory** field, enter the amount of RAM in GB per task.

For example, enter `0.5` (default).

     6. Click **Done**.

  5. Optional: Configure the [other fields for this job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

  6. Optional: To review the job configuration, in the left pane, click **Preview**.

  7. Click **Create**.

The **Job details** page displays the job that you created.




### gcloud

  1. Create a JSON file that installs GPU drivers, specifies a machine type from the accelerator-optimized machine family, and runs in a location that has the GPU machine type.

For example, to create a basic script job that uses GPUs for accelerator-optimized VMs, create a JSON file with the following contents:
         
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
                         "installGpuDrivers": INSTALL_GPU_DRIVERS,
                         "policy": {
                             "provisioningModel": "PROVISIONING_MODEL",
                             "machineType": "MACHINE_TYPE",
                             "reservation": "NO_RESERVATION"
                         }
                     }
                 ],
                 "location": {
                     "allowedLocations": [
                         "ALLOWED_LOCATIONS"
                     ]
                 }
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

     * `PROVISIONING_MODEL`: the provisioning model for your consumption option: either `STANDARD` for on-demand or `SPOT` for Spot VMs.

     * `MACHINE_TYPE`: a machine type from the [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).

     * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

       * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
       * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

       * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
       * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that installs GPU drivers, specifies a machine type from the accelerator-optimized machine family, and runs in a location that has the GPU machine type.

For example, to create a basic script job that uses GPUs for accelerator-optimized VMs, make the following request:
    
    
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
                    "installGpuDrivers": INSTALL_GPU_DRIVERS,
                    "policy": {
                        "provisioningModel": "PROVISIONING_MODEL",
                        "machineType": "MACHINE_TYPE",
                        "reservation": "NO_RESERVATION"
                    }
                }
            ],
            "location": {
                "allowedLocations": [
                    "ALLOWED_LOCATIONS"
                ]
            }
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

  * `PROVISIONING_MODEL`: the provisioning model for your consumption option: either `STANDARD` for on-demand or `SPOT` for Spot VMs.

  * `MACHINE_TYPE`: a machine type from the [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).

  * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

    * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
    * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
    * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).




###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.html);
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
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateGpuJob {
    
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
        // Optional. When set to true, Batch fetches the drivers required for the GPU type
        // that you specify in the policy field from a third-party location,
        // and Batch installs them on your behalf. If you set this field to false (default),
        // you need to install GPU drivers manually to use any GPUs for this job.
        boolean installGpuDrivers = false;
        // Accelerator-optimized machine types are available to Batch jobs. See the list
        // of available types on: https://cloud.google.com/compute/docs/accelerator-optimized-machines
        String machineType = "g2-standard-4";
    
        createGpuJob(projectId, region, jobName, installGpuDrivers, machineType);
      }
    
      // Create a job that uses GPUs
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createGpuJob(String projectId, String region, String jobName,
                                      boolean installGpuDrivers, String machineType)
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
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                      // Jobs can be divided into tasks. In this case, we have only one task.
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
    
          // Policies are used to define on what kind of virtual machines the tasks will run.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().setMachineType(machineType).build();  
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances(
                      [InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder()
                          .setInstallGpuDrivers(installGpuDrivers)
                          .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy)
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
    const jobName = 'batch-gpu-job';
    // The GPU type. You can view a list of the available GPU types
    // by using the `gcloud compute accelerator-types list` command.
    const gpuType = 'nvidia-l4';
    // The number of GPUs of the specified type.
    const gpuCount = 1;
    // Optional. When set to true, Batch fetches the drivers required for the GPU type
    // that you specify in the policy field from a third-party location,
    // and Batch installs them on your behalf. If you set this field to false (default),
    // you need to install GPU drivers manually to use any GPUs for this job.
    const installGpuDrivers = false;
    // Accelerator-optimized machine types are available to Batch jobs. See the list
    // of available types on: https://cloud.google.com/compute/docs/accelerator-optimized-machines
    const machineType = 'g2-standard-4';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
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
    // In this case, we tell the system to use "g2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType,
      // Accelerator describes Compute Engine accelerators to be attached to the VM
      accelerators: [
        new batch.AllocationPolicy.Accelerator({
          type: gpuType,
          count: gpuCount,
          installGpuDrivers,
        }),
      ],
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      instances: [{installGpuDrivers, policy: instancePolicy}],
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
    
    
    from google.cloud import batch_v1
    
    
    def create_gpu_job(project_id: str, region: str, job_name: str) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances on GPU machines.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
    
        Returns:
            A job object representing the job created.
        """
        client = batch_v1.BatchServiceClient()
    
        # Define what will be done as part of the job.
        task = batch_v1.TaskSpec()
        runnable = batch_v1.Runnable()
        runnable.script = batch_v1.Runnable.Script()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
        # You can also run a script from a file. Just remember, that needs to be a script that's
        # already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
        # exclusive.
        # runnable.script.path = '/tmp/test.sh'
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = batch_v1.ComputeResource()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = batch_v1.TaskGroup()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "g2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = batch_v1.AllocationPolicy.InstancePolicy()
        policy.machine_type = "g2-standard-4"
    
        instances = batch_v1.AllocationPolicy.InstancePolicyOrTemplate()
        instances.policy = policy
        instances.install_gpu_drivers = True
        allocation_policy = batch_v1.AllocationPolicy()
        allocation_policy.instances = [instances]
    
        job = batch_v1.Job()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = batch_v1.LogsPolicy()
        job.logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING
    
        create_request = batch_v1.CreateJobRequest()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.create_job(create_request)
    
    

#### Use GPUs for N1 VMs

You can create a job that uses GPUs for N1 VMs using the Google Cloud console, gcloud CLI, Batch API, Java, Node.js, or Python.

### Console

**Important:** The Google Cloud console only supports automatically installing the default version of GPU drivers. To install other versions of GPU drivers or manually install GPU drivers, use a different method to create the job.

To create a job that uses GPUs by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-gpu-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, to create a basic script job, do the following:

           1. Select the **Script** checkbox. A field appears.

           2. In the field, enter the following script:
                  
                  echo Hello world from task ${BATCH_TASK_INDEX}.
                  

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job.

For example, enter `3`.

        3. Optional: In the **Parallelism** field, enter the number of tasks to run concurrently.

For example, enter `1` (default).

  4. Configure the **Resource specifications** page:

     1. In the left pane, click **Resource specifications**. The **Resource specifications** page opens.

     2. In the **VM provisioning model** section, select one of the following options for the consumption option for this job's VMs:

        * If your job can withstand preemption and you want discounted Spot VMs, select **Spot**.

        * Otherwise, to use on-demand VMs, select **Standard** (default).

     3. Select the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.

        1. In the **Region** field, select a region.

        2. In the **Zone** field, do one of the following:

           * If you want to restrict this job to run in a specific zone only, select a zone.

           * Otherwise, select **any** (default).

**Important:** Ensure that you specify only [locations that offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job.
     4. Select the GPU machine type for this job's VMs:

        1. In the machine family options, click **GPUs**.

        2. In the **GPU type** field, select the type of GPUs.

If you selected one of the [GPU types for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads), then the **Series** field is set to **N1**.

        3. In the **Number of GPUs** field, select the number of GPUs for each VM.

        4. In the **Machine type** field, select the machine type.

        5. To automatically install GPU drivers, select **GPU driver installation** (default).

     5. Configure the amount of VM resources required for each task:

**Important:** Ensure that the GPU machine type has enough [VM resources for the job's task requirements](https://docs.cloud.google.com/batch/docs/create-run-job#job-vm-resource-requirements).
        1. In the **Cores** field, enter the amount of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms) per task.

For example, enter `1` (default).

        2. In the **Memory** field, enter the amount of RAM in GB per task.

For example, enter `0.5` (default).

     6. Click **Done**.

  5. Optional: Configure the [other fields for this job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).

  6. Optional: To review the job configuration, in the left pane, click **Preview**.

  7. Click **Create**.

The **Job details** page displays the job that you created.




### gcloud

  1. Create a JSON file that installs GPU drivers, defines the [`type` and `count` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Accelerator) of the `accelerators[]` field, and runs in a location that has the GPU machine type.

For example, to create a basic script job that uses GPUs for N1 VMs and lets Batch select the exact N1 machine type, create a JSON file with the following contents:
         
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
                         "installGpuDrivers": INSTALL_GPU_DRIVERS,
                         "policy": {
                             "provisioningModel": "PROVISIONING_MODEL",
                             "reservation": "NO_RESERVATION",
                             "accelerators": [
                                 {
                                     "type": "GPU_TYPE",
                                     "count": GPU_COUNT
                                 }
                             ]
                         }
                     }
                 ],
                 "location": {
                     "allowedLocations": [
                         "ALLOWED_LOCATIONS"
                     ]
                 }
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

Replace the following:

     * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

     * `PROVISIONING_MODEL`: the provisioning model for your consumption option: either `STANDARD` for on-demand or `SPOT` for Spot VMs.

     * `GPU_TYPE`: the [GPU](https://docs.cloud.google.com/compute/docs/gpus) type. You can view a list of the available GPU types by using the [`gcloud compute accelerator-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list). Only use this field for GPUs for N1 VMs.

     * `GPU_COUNT`: the number of GPUs of the specified type. For more information about the valid options, see the [GPU machine types for the N1 machine series](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). Only use this field for GPUs for N1 VMs.

     * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

       * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
       * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

       * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
       * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that installs GPU drivers, defines the [`type` and `count` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Accelerator) of the `accelerators[]` field, and uses a location that has the GPU machine type.

For example, to create a basic script job that uses GPUs for N1 VMs and lets Batch select the exact N1 machine type, make the following request:
    
    
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
                    "installGpuDrivers": INSTALL_GPU_DRIVERS,
                    "policy": {
                        "provisioningModel": "PROVISIONING_MODEL",
                        "reservation": "NO_RESERVATION",
                        "accelerators": [
                            {
                                "type": "GPU_TYPE",
                                "count": GPU_COUNT
                            }
                        ]
                    }
                }
            ],
            "location": {
                "allowedLocations": [
                    "ALLOWED_LOCATIONS"
                ]
            }
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `INSTALL_GPU_DRIVERS`: whether or not to automatically install GPU drivers. When set to `true`, Batch fetches the drivers required for the GPU type that you specify in the [`policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) from a third-party location, and Batch installs them on your behalf. If you set this field to `false` (default), you need to install GPU drivers manually to use any GPUs for this job.

  * `PROVISIONING_MODEL`: the provisioning model for your consumption option: either `STANDARD` for on-demand or `SPOT` for Spot VMs.

  * `GPU_TYPE`: the [GPU](https://docs.cloud.google.com/compute/docs/gpus) type. You can view a list of the available GPU types by using the [`gcloud compute accelerator-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list). Only use this field for GPUs for N1 VMs.

  * `GPU_COUNT`: the number of GPUs of the specified type. For more information about the valid options, see [GPU machine types for N1 machine series](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). Only use this field for GPUs for N1 VMs.

  * `ALLOWED_LOCATIONS`: the allowed locations for the job. Ensure that the location for the job's Compute Engine resources [offer the GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones) that you want for this job by using one of the following options:

    * By default, if you omit the `allowedLocations[]` field, a job runs on Compute Engine resources that are created in the job's location (`LOCATION`) region.
    * Optionally, if you include the [`allowedLocations[]` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LocationPolicy.FIELDS.allowed_locations), then the job is only allowed to run on Compute Engine resources that are created in the specified locations.

**Important:** The `allowedLocations[]` field no longer supports locating Compute Engine resources outside of the job's location. To avoid failures, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location by the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.
    * For all other projects, the changes are starting on _July 31, 2026_.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).




###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.html);
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
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateGpuJobN1 {
    
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
        // Optional. When set to true, Batch fetches the drivers required for the GPU type
        // that you specify in the policy field from a third-party location,
        // and Batch installs them on your behalf. If you set this field to false (default),
        // you need to install GPU drivers manually to use any GPUs for this job.
        boolean installGpuDrivers = false;
        // The GPU type. You can view a list of the available GPU types
        // by using the `gcloud compute accelerator-types list` command.
        String gpuType = "nvidia-tesla-t4";
        // The number of GPUs of the specified type.
        int gpuCount = 2;
    
        createGpuJob(projectId, region, jobName, installGpuDrivers, gpuType, gpuCount);
      }
    
      // Create a job that uses GPUs
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createGpuJob(String projectId, String region, String jobName,
                                      boolean installGpuDrivers, String gpuType, int gpuCount)
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
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                      // Jobs can be divided into tasks. In this case, we have only one task.
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
    
          // Accelerator describes Compute Engine accelerators to be attached to the VM.
          [Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.html) accelerator = [Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.html).newBuilder()
              .setType(gpuType)
              .[setCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_Accelerator_Builder_setCount_long_)(gpuCount)
              .build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances(
                      [InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder()
                          .setInstallGpuDrivers(installGpuDrivers)
                          .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)([InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().[addAccelerators](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_Builder_addAccelerators_com_google_cloud_batch_v1_AllocationPolicy_Accelerator_)(accelerator))
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
    const jobName = 'batch-gpu-job-n1';
    // The GPU type. You can view a list of the available GPU types
    // by using the `gcloud compute accelerator-types list` command.
    const gpuType = 'nvidia-tesla-t4';
    // The number of GPUs of the specified type.
    const gpuCount = 1;
    // Optional. When set to true, Batch fetches the drivers required for the GPU type
    // that you specify in the policy field from a third-party location,
    // and Batch installs them on your behalf. If you set this field to false (default),
    // you need to install GPU drivers manually to use any GPUs for this job.
    const installGpuDrivers = false;
    // Accelerator-optimized machine types are available to Batch jobs. See the list
    // of available types on: https://cloud.google.com/compute/docs/accelerator-optimized-machines
    const machineType = 'n1-standard-16';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
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
    // In this case, we tell the system to use "g2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType,
      // Accelerator describes Compute Engine accelerators to be attached to the VM
      accelerators: [
        new batch.AllocationPolicy.Accelerator({
          type: gpuType,
          count: gpuCount,
          installGpuDrivers,
        }),
      ],
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      instances: [{installGpuDrivers, policy: instancePolicy}],
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
    
    async function callCreateBatchGPUJobN1() {
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
    
    await callCreateBatchGPUJobN1();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_gpu_job(
        project_id: str, region: str, zone: str, job_name: str
    ) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances on GPU machines.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            zone: name of the zone you want to use to run the job. Important in regard to GPUs availability.
                GPUs availability can be found here: https://cloud.google.com/compute/docs/gpus/gpu-regions-zones
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
    
        Returns:
            A job object representing the job created.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
        # You can also run a script from a file. Just remember, that needs to be a script that's
        # already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
        # exclusive.
        # runnable.script.path = '/tmp/test.sh'
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "n1-standard-16"
    
        accelerator = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[Accelerator](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Accelerator.html)()
        # Note: not every accelerator is compatible with instance type
        # Read more here: https://cloud.google.com/compute/docs/gpus#t4-gpus
        accelerator.type_ = "nvidia-tesla-t4"
        accelerator.count = 1
    
        policy.accelerators = [accelerator]
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        instances.install_gpu_drivers = True
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        location = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[LocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.LocationPolicy.html)()
        location.allowed_locations = ["zones/us-central1-b"]
        allocation_policy.location = location
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
