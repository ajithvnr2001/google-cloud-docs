---
url: https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime/
title: Limit the run time of a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:25.044428+00:00
---

# Limit the run time of a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Limit the run time of a VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to limit the run time of new or existing virtual machine (VM) instances and how to monitor the run time of those VMs. For managed instance groups (MIGs), see [Limit the run time of a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs) instead.

When limiting the run time of a VM, you can schedule the VM to be automatically _terminated_ (stopped or deleted) when it reaches a specific _time limit_ (duration or time). Use time limits to help optimize temporary workloads—by automatically limiting VM run times, you can help minimize costs and free up quotas.

**Note:** GPU VMs that are configured to be automatically deleted after a predefined run time of 7 days or less can consume either preemptible or standard allocation quotas. This behavior is intended to help you improve the obtainability of allocation quota for temporary-but-uninterrupted workloads. For more information about this behavior, see [GPU VMs and preemptible allocation quotas](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).

To learn how to immediately stop a VM, see [Stop or restart a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance). To learn how to immediately delete a VM, see [Delete a VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

## Before you begin

  * To get the permissions that you need to limit the run time of a VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Restrictions

Limiting the run time of a VM has the following restrictions:

  * The automatic termination action must be either stop or delete. You cannot configure a VM to be automatically suspended when the time limit is reached.

  * The minimum time limit is 30 seconds and the maximum time limit is 120 days.

**Note:** If you want to schedule a VM to stop after more than 120 days, you can use [instance schedules](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop) instead.
  * Automatic termination might take up to 30 seconds longer than the duration or time you specify to begin stopping or deleting the VM.

  * You cannot use time limits with [legacy preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible). Instead, use time limits with [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

  * A VM's local SSD data cannot be preserved when the VM is automatically stopped due to a time limit. For more information, see [Stop a VM with Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance).




## Limit the run time of a new VM

The following sections describe how to configure a time limit while creating a new VM. You can specify the time limit, which is when you want a VM to automatically terminate, as either a duration (`maxRunDuration`) or a time (`terminationTime`).

When deciding the type of time limit for a VM, consider that the VM might be interrupted—for example, by a user request or by a [host event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview). The behavior of a time limit varies based on the type of interruption and the type of time limit:

  * A VM's _termination timestamp_ (`terminationTimestamp`) is a read-only field that represents the planned time for automatic termination and is automatically defined by Compute Engine whenever a VM has a time limit and enters the `RUNNING` state.

  * The termination timestamp is automatically cleared whenever a VM is [stopped or suspended](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview). However, a termination timestamp doesn't change when you [reset or reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance).

  * The termination timestamp is automatically redefined whenever the VM is restarted or resumed based on the type of time limit that you set:

    * If you set a duration for the VM, the termination timestamp is recalculated by adding that duration to the VM's latest start time.
    * If you set a time for the VM, the termination timestamp is set to that time. However, the time must be in the future; otherwise, any requests to create or rerun the VM fail until you update or remove the time.



### Set a duration

A _duration_ represents the total run time that you want for a VM. To create a VM that is automatically terminated after the VM runs for a specific duration, use the Google Cloud console, Google Cloud CLI, Terraform, or Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Availability policies** section, expand **VM provisioning model advanced settings**.

  3. Select the **Set a time limit for the VM** checkbox. The **Time limit type** field appears.

  4. In the **Time limit type** field, select **By hours** (default) to specify the time limit as a duration. In the following field, enter the duration in hours.

  5. In the **On VM termination** list, select what happens when the run time of the VM reaches the specified time limit:

     * To automatically stop the VM, select **Stop** (default).
     * To delete the VM, select **Delete**.
  6. Optional: Specify other VM options. For more information, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  7. To create and start the VM, click **Create**.




###  gcloud 

To create a VM from the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

  * To create a VM that is automatically terminated after a specific duration, you must include the `--max-run-duration` flag.
  * To specify the termination action, include the `--instance-termination-action` flag.
  * Configure the [`--discard-local-ssds-at-termination-timestamp` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--discard-local-ssds-at-termination-timestamp): 
    * If the VM has any local SSDs and the termination action (`TERMINATION_ACTION`) is stop (`STOP`), you must include the `--discard-local-ssds-at-termination-timestamp=true` flag.
    * Otherwise, omit the `--discard-local-ssds-at-termination-timestamp` flag.


    
    
    gcloud compute instances create VM_NAME \
        --max-run-duration=DURATION \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `DURATION`: The duration you want this VM to run before being automatically terminated. Format the duration as the number of days, hours, minutes, and seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for a duration of 30 minutes, or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).
  * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model: 
    * If this is a Spot VM (if the VM uses the `--provisioning-model=SPOT` flag), the `--instance-termination-action=TERMINATION_ACTION` flag is optional. If this flag is omitted, the default termination action is stop.
    * Otherwise (default), the `--instance-termination-action=TERMINATION_ACTION` flag is required.



For more information about other options you can specify when creating a VM, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  Terraform 

To create a VM using Terraform, use the `google_compute_instance` resource.

  * To create a VM that is automatically terminated after a specific duration, you must include the [`max_run_duration` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#max_run_duration).
  * To specify the termination action, include the [`instance_termination_action` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#instance_termination_action). You must include the `instance_termination_action` argument unless you are creating a Spot VM (set the [`provisioning_model` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#provisioning_model) to `SPOT`), which defaults to stop (`STOP`).
  * Configure the [`on_instance_stop_action` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#on_instance_stop_action): 
    * If the VM has any local SSDs and the termination action (`instance_termination_action` argument) is stop (`STOP`), you must set the `on_instance_stop_action` argument to true (`true`).
    * Otherwise, omit the `on_instance_stop_action` argument.



For more information, see the [Terraform documentation for the `google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).

###  REST 

To create a VM from the Compute Engine API, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). You must specify a name, machine type, and boot disk for the VM.

To create a VM that is automatically terminated after a specific duration, you must include the `maxRunDuration` field. To specify the termination action, include the `instanceTerminationAction` field, which is optional for Spot VMs.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ]
      "scheduling":
      {
        "maxRunDuration":
        {
          "seconds": DURATION
        },
        "instanceTerminationAction": "TERMINATION_ACTION"
      },
    }

Replace the following:

  * `PROJECT_ID`: The [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project to create the VM in.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the VM in. The zone must also support the machine type to use for the new VM.
  * `MACHINE_TYPE`: The [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the new VM.
  * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `IMAGE_PROJECT`: The [project containing the image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). For example, if you specify `family/debian-10` as the image, specify `debian-cloud` as the image project.
  * `IMAGE`: The image for the new VM. You can specify either a specific version of a public image or an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). For example, if you specify `family/debian-10` as the image and `debian-cloud` as the image project, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
  * `DURATION`: The duration in seconds that you want this VM to run before being automatically terminated. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).
  * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model: 
    * If this is a Spot VM (if the VM uses the `"provisioningModel": "SPOT"` field), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is optional. If this field is omitted, the default termination action is stop.
    * Otherwise (default), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is required.



For more information about the options you can specify when creating a VM, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Set a time

A _time_ represents the date, time, and timezone when you want a VM to be terminated. To create a VM that is automatically terminated at a specific time, use the Google Cloud console, Google Cloud CLI, or Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Availability policies** section, expand **VM provisioning model advanced settings**.

  3. Select the **Set a time limit for the VM** checkbox. The **Time limit type** field appears.

  4. In the **Time limit type** field, select **By date** to specify the time limit as a time and date. In the following field, click date_range **Select date and time** and select the date, time, and timezone for the time limit.

  5. In the **On VM termination** list, select what happens when the run time of the VM reaches the specified time limit:

     * To automatically stop the VM, select **Stop** (default).
     * To delete the VM, select **Delete**.
  6. Optional: Specify other VM options. For more information, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  7. To create and start the VM, click **Create**.




###  gcloud 

To create a VM from the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

  * To create a VM that is automatically terminated at a specific time, you must include the `--termination-time` flag.
  * To specify the termination action, include the `--instance-termination-action` flag, which is optional for Spot VMs.
  * Configure the [`--discard-local-ssds-at-termination-timestamp` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--discard-local-ssds-at-termination-timestamp): 
    * If the VM has any local SSDs and sets the termination action (`TERMINATION_ACTION`) to stop (`STOP`), you must include the `--discard-local-ssds-at-termination-timestamp=true` flag.
    * Otherwise, omit the `--discard-local-ssds-at-termination-timestamp` flag.


    
    
    gcloud compute instances create VM_NAME \
        --termination-time=TIME \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `TIME`: The time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
        
        YYYY-MM-DDTHH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: A date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
    * `HH:MM:SS`: A time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
    * `OFFSET`: The time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.
  * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model:

    * If this is a Spot VM (if the VM uses the `--provisioning-model=SPOT` flag), the `--instance-termination-action=TERMINATION_ACTION` flag is optional. If this flag is omitted, the default termination action is stop.
    * Otherwise (default), the `--instance-termination-action=TERMINATION_ACTION` flag is required.



For more information about other options you can specify when creating a VM, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  REST 

To create a VM from the Compute Engine API, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). You must specify a name, machine type, and boot disk for the VM.

To create a VM that is automatically terminated at a specific time, you must include the `terminationTime` field. To specify the termination action, include the `instanceTerminationAction` field, which is optional for Spot VMs.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ]
      "scheduling":
      {
        "terminationTime": "TIME",
        "instanceTerminationAction": "TERMINATION_ACTION"
      },
    }

Replace the following:

  * `PROJECT_ID`: The [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project to create the VM in.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the VM in. The zone must also support the machine type to use for the new VM.
  * `MACHINE_TYPE`: The [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the new VM.
  * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `IMAGE_PROJECT`: The [project containing the image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). For example, if you specify `family/debian-10` as the image, specify `debian-cloud` as the image project.
  * `IMAGE`: The image for the new VM. You can specify either a specific version of a public image or an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). For example, if you specify `family/debian-10` as the image and `debian-cloud` as the image project, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
  * `TIME`: The time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
        
        YYYY-MM-DDTHH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: A date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
    * `HH:MM:SS`: A time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
    * `OFFSET`: The time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.
  * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model::

    * If this is a Spot VM (if the VM uses the `"provisioningModel": "SPOT"` field), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is optional. If this field is omitted, the default termination action is stop.
    * Otherwise (default), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is required.



For more information about the options you can specify when creating a VM, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Limit the run time of an existing VM

You can limit the run time of an existing VM by updating the VM's schedule. If you don't already understand how to configure settings for time limits, review the previous sections about how to limit the run time of a new VM first.

You can use the Google Cloud console, Google Cloud CLI, or Compute Engine API to update the VM's scheduling-related properties, as described in this section. This method requires that you first stop your VM, then update its properties, then restart it. Alternatively, if you want to simultaneously update additional VM properties and automatically stop and restart a VM, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties) instead.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM that you want to update.

  3. From the **VM instance details** page, complete the following steps:

     1. If the VM is running, click **Stop** to stop the VM.
     2. To edit the VM, click edit **Edit**.
     3. On the **Edit instance** page, complete the following steps:

        1. In the **Availability policies** section, modify the **Set a time limit for the VM** checkbox and any fields below it as desired.

For more information about how to configure the properties for time limits, see limit the run time of a new VM.

        2. To save your changes, click **Save**.

     4. Optional: If you want to start running the VM now, click **Start**.




###  gcloud 

To update a VM's time limit by using the gcloud CLI, complete the following steps:

  1. If the VM is running, stop the VM by using the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of VM that you want to update.

  2. Update the VM's time limit by using the [`gcloud compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling).
         
         gcloud compute instances set-scheduling VM_NAME \
             --max-run-duration=DURATION \
             --termination-time=TIME \
             --instance-termination-action=TERMINATION_ACTION \
             --discard-local-ssds-at-termination-timestamp=true
         

Configure the following flags:

     * You must omit either the `--max-run-duration` flag or the `--termination-time` flag to set the time limit as either a time or duration, respectively.
     * Include `--instance-termination-action` flag to set the termination action.
     * If the VM has any local SSDs and sets the termination action (`TERMINATION_ACTION`) to stop (`STOP`), you must include the `--discard-local-ssds-at-termination-timestamp=true` flag. Otherwise, omit the `--discard-local-ssds-at-termination-timestamp=true` flag.

Then, replace the following:

     * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM that you want to update.
     * `DURATION`: The duration you want this VM to run before being automatically terminated. Format the duration as the number of days, hours, minutes, and seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for a duration of 30 minutes, or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).
     * `TIME`: The time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
           
           YYYY-MM-DDTHH:MM:SSOFFSET
           

Replace the following:

       * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
       * `HH:MM:SS`: a time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
       * `OFFSET`: the time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.
     * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model:

       * If this is a Spot VM (if the VM uses the `--provisioning-model=SPOT` flag), the `--instance-termination-action=TERMINATION_ACTION` flag is optional. If this flag is omitted, the default termination action is stop.
       * Otherwise (default), the `--instance-termination-action=TERMINATION_ACTION` flag is required.
  3. If you want the VM to start running, start the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM.




###  REST 

To update a VM's time limit by using the Compute Engine API, complete the following steps:

  1. If the VM is running, stop the VM by using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: The [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the VM.
     * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones) that contains the VM.
     * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM that you want to update.
  2. Update the VM's `scheduling` property, including fields for the VM's time limit, by using the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling). Include either the `maxRunDuration` field or the `terminationTime` field to set the time limit as either a duration or time, respectively:

     * To set a _duration_ , use the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
           {
             "maxRunDuration":
             {
               "seconds": DURATION
             },
             "instanceTerminationAction": "TERMINATION_ACTION"
           }
           

     * To set a _time_ , use the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
           {
             "terminationTime": "TIME",
             "instanceTerminationAction": "TERMINATION_ACTION"
           }
           

Replace the following:

     * `PROJECT_ID`: The [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project to create the VM in.
     * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the VM in. The zone must also support the machine type to use for the new VM.
     * `MACHINE_TYPE`: The [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the new VM.
     * `VM_NAME`: The [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
     * `IMAGE_PROJECT`: The [project containing the image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). For example, if you specify `family/debian-10` as the image, specify `debian-cloud` as the image project.
     * `IMAGE`: The image for the new VM. You can specify either a specific version of a public image or an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). For example, if you specify `family/debian-10` as the image and `debian-cloud` as the image project, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
     * `DURATION`: The duration in seconds that you want this VM to run before being automatically terminated. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).
     * `TIME`: The time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
           
           YYYY-MM-DDTHH:MM:SSOFFSET
           

Replace the following:

       * `YYYY-MM-DD`: A date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
       * `HH:MM:SS`: A time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
       * `OFFSET`: The time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.
     * `TERMINATION_ACTION`: The termination action for this VM, which can be either stop (`STOP`) or delete (`DELETE`). Whether this field is required or has a default value varies based on the VM's provisioning model:

       * If this is a Spot VM (if the VM uses the `"provisioningModel": "SPOT"` field), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is optional. If this field is omitted, the default termination action is stop.
       * Otherwise (default), the `"instanceTerminationAction": "TERMINATION_ACTION"` field is required.
  3. If you want the VM to start running, start the VM by using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: the [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the VM.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) that contains the VM.
     * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM.



## Monitor the run time of a VM

You can monitor the run time of a VM that has a time limit by using the following options:

  * To see when a running VM is scheduled to be automatically terminated, view the VM's termination timestamp:

    1. [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).
    2. In the output, view the VM's field for the termination timestamp: 
       * If you are using the Google Cloud console, see the **Max duration** field.
       * If you are using the Google Cloud CLI or Compute Engine API, see the `terminationTimestamp` field.
  * To verify if a VM was automatically terminated, view the VM's operations:

    1. [View VM operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations).
    2. In the output, you can identify VM operations that are caused by a time limit by looking for the following types of operations:

       * `compute.instances.deferredStop` indicates an automatic termination action of stop
       * `compute.instances.deferredDelete` indicates an automatic termination action of delete



## What's next

  * Learn how to further optimize your VMs:

    * If your workloads are fault-tolerant, you can use [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) to get significant discounts and optional dedicated quota.
    * If you want a VM to automatically execute commands before shutting down, you can use [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).
  * Learn about more options for automatically limiting the run times of VMs:

    * [Limit the run time of VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs)
    * [Scheduling a VM to start and stop](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)
    * [Batch](https://docs.cloud.google.com/batch)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
