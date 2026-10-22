---
url: https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs/
title: Limit the run time of VMs in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:01.876145+00:00
---

# Limit the run time of VMs in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Limit the run time of VMs in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to automatically terminate virtual machines (VMs) in a managed instance group (MIG) by specifying a time limit for the VMs. It also describes how time limit works for VMs in a MIG.

You can optimize temporary workloads by specifying a time limit for the VMs in a MIG. When a VM reaches its time limit, the MIG automatically terminates (deletes) that VM. Limiting the run time of VMs in a MIG by a time limit helps to minimize costs and free up quota.

To learn about specifying a time limit for a standalone VM, see [Limit the run time of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime). If you want a MIG to automatically add or delete VMs based on your workloads, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

## Before you begin

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




## Limit the run time of VMs in a MIG

You can limit the run time of VMs in a MIG by specifying a time limit in the [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) used for the MIG. When the MIG creates VMs based on the template, the time limit is applied to each VM.

You can specify one of two types of time limits:

  * Time limit as a run duration
  * Time limit as a termination time



To specify a time limit for the VMs in a MIG, follow these steps:

  1. Create an instance template with a run duration for VMs or with a termination time for VMs.

  2. Use the instance template to [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) or [update an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).




### Limitations

  * You must comply with the [restrictions for limiting the run time of standalone VMs](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#restrictions).

  * When you create an instance template to specify a time limit for VMs in a MIG, the following limitations apply:

    * You can only set the termination action to `DELETE`.

    * You can only use the instance template if it specifies the [standard or flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  * You can't limit the run time of VMs in a regional MIG if the MIG specifies both of the following:

    * `EVEN` target distribution shape

    * [Proactive instance redistribution enabled](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution)




### Create an instance template with a run duration for VMs

To automatically terminate VMs in a MIG after they run for a certain duration, set a maximum run duration (`maxRunDuration`) in the instance template.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. Select the **Location** as follows:

     * If you want to use the instance template across regions, choose **Global**.
     * If you want to reduce cross-region dependency, choose **Regional**.
  4. If you chose regional, then select the **Region** where you want to create your instance template.

  5. In the **Availability policies** section, expand **VM provisioning model advanced settings**.

  6. Select the **Set a time limit for the VM** checkbox.

  7. In the **Time limit type** field, select **By hours** (default) to specify the time limit as a duration. In the next field, enter the duration in hours.

  8. In the **On VM termination** list, select **Delete**.

  9. For the other fields, either accept the default values or modify them as required.

  10. Click **Create**.




###  gcloud 

Use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). To automatically delete VMs after a specific duration, include the `--max-run-duration` flag and set the`--instance-termination-action` flag to `DELETE` as follows:
    
    
      gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
          --max-run-duration=DURATION \
          --instance-termination-action=DELETE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `DURATION`: the duration you want the VMs to run. The MIG automatically deletes the VM after the specified duration.

Format the duration as the number of days, hours, minutes, and seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for a duration of 30 minutes, or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).




###  Terraform 

To create an instance template using Terraform, use the `google_compute_instance_template` resource. To create an instance template that automatically deletes VMs after a specific duration, you must include the [`max_run_duration` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template#max_run_duration) and set the [`instance_termination_action` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template#instance_termination_action) to `DELETE`.

For more information, see the [Terraform documentation for the `google_compute_instance_template` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template).

###  REST 

Use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert). To automatically delete VMs after a specific duration, include the `maxRunDuration` field and set the`instanceTerminationAction` field to `DELETE` as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default",
            "accessConfigs": [
              {
                "name": "external-IP",
                "type": "ONE_TO_ONE_NAT"
              }
            ]
          }
        ],
        "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams":
            {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ]
        "scheduling": {
          "maxRunDuration":
          {
            "seconds": DURATION
          },
          "instanceTerminationAction": "DELETE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in which you want to create the instance template.
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the VMs in the group.
  * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image; for example, `debian-cloud`.
  * `IMAGE` or `IMAGE_FAMILY`: specify one of the following:

    * `IMAGE`: a specific version of the OS image; for example, `debian-10-buster-v20200309`.

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-10`, the latest version in the Debian 10 image family is used.

  * `DURATION`: the duration you want the VMs to run. The MIG automatically deletes the VM after the specified duration.

Format the duration as the number of days, hours, minutes, and seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for a duration of 30 minutes, or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. The minimum duration is 30 seconds (`30s`) and the maximum duration is 120 days (`120d`).




### Create an instance template with a termination time for VMs

To automatically terminate VMs in a MIG at a specific time, set a termination time (`terminationTime`) in the instance template. You can set a date and time at which you want a MIG to terminate the VMs.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. Select the **Location** as follows:

     * If you want to use the instance template across regions, choose **Global**.
     * If you want to reduce cross-region dependency, choose **Regional**.
  4. If you chose regional, then select the **Region** where you want to create your instance template.

  5. In the **Availability policies** section, expand **VM provisioning model advanced settings**.

  6. In the **Time limit type** field, select **By date** to specify the time limit as a time and date. In the next field, click date_range**Select date and time** and select the date, time, and timezone for automatic termination.

  7. In the **On VM termination** list, select **Delete**.

  8. For the other fields, either accept the default values or modify them as required.

  9. Click **Create**.




###  gcloud 

Use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). To automatically delete VMs at a specific time, include the `--termination-time` flag and set the`--instance-termination-action` flag to `DELETE` as follows:
    
    
      gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
          --termination-time=TIME \
          --instance-termination-action=DELETE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `TIME`: the time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
        
        YYYY-MM-DDTHH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: A date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
    * `HH:MM:SS`: A time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
    * `OFFSET`: The time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.



###  REST 

Use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert). To automatically delete VMs at a specific time, include the `terminationTime` field and set the`instanceTerminationAction` field to `DELETE` as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default",
            "accessConfigs": [
              {
                "name": "external-IP",
                "type": "ONE_TO_ONE_NAT"
              }
            ]
          }
        ],
        "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams":
            {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ]
        "scheduling": {
          "terminationTime": TIME,
          "instanceTerminationAction": "DELETE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in which you want to create the instance template.
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the VMs in the group.
  * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image; for example, `debian-cloud`.
  * `IMAGE` or `IMAGE_FAMILY`: specify one of the following:

    * `IMAGE`: a specific version of the OS image; for example, `debian-10-buster-v20200309`.

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-10`, the latest version in the Debian 10 image family is used.

  * `TIME`: The time you want this VM to be automatically terminated. The time you specify must be at least 30 seconds in the future and at most 120 days in the future. Format the time as a [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339):
        
        YYYY-MM-DDTHH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: A date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
    * `HH:MM:SS`: A time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
    * `OFFSET`: The time zone formatted as an offset of Coordinated Universal Time (UTC). For example, to use Pacific Standard Time (PST), which is 8 hours earlier than UTC, specify `-08:00`. Alternatively, to use no offset (UTC+0), specify `Z`.



## View the termination timestamp of VMs in a MIG

To see when Compute Engine will terminate the VMs in a MIG, check their termination timestamps. To know how a MIG calculates the termination timestamp, see the How time limit works for VMs in a MIG section in this document.

To view the termination timestamp, use one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your MIG.

  3. On the **Overview** tab, in the **VM instances** table, look for the **Termination timestamp** column.




###  gcloud 

To view the termination timestamp of VMs in the MIG, use the [`compute instance-groups managed list-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances). To filter the termination timestamps in the output, use the `--format` flag as shown in the following example.

For a zonal MIG, run the following command. For a regional MIG, replace the `--zone=ZONE` flag in the following command with the `--region=REGION` flag.
    
    
    gcloud compute instance-groups managed list-instances MIG_NAME \
        --zone=ZONE \
        --format="table(name, instanceStatus, scheduling.terminationTimestamp)"
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG is located.



The following is a sample output. The `TERMINATION_TIMESTAMP` field shows a value only if that VM has a termination timestamp set.
    
    
    NAME          STATUS   TERMINATION_TIMESTAMP
    new-mig-2-2mr4  RUNNING  2025-06-12T16:09:00.366292Z
    new-mig-2-6b0v  RUNNING
    

###  REST 

To view the termination timestamp of VMs in the MIG, use one of the following methods:

  * For a regional MIG, use the [`regionInstanceGroupManagers.listManagedInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances).
  * For a zonal MIG, use the [`instanceGroupManagers.listManagedInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances).



To filter the termination timestamps, add the `fields` parameter to the request URL. The following example shows a request for a zonal MIG:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/listManagedInstances?fields=managedInstances(name%2Cscheduling)
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: the zone where the MIG is located.
  * `VM_NAME`: the name of the MIG.



The following is a sample response. The `terminationTimestamp` field is shown only if that VM has a termination timestamp set.
    
    
    {
      "managedInstances": [
        {
          "name": "new-mig-2-2mr4",
          "scheduling": {
            "terminationTimestamp": "2025-06-12T16:09:00.366292Z"
          }
        },
        {
          "name": "new-mig-2-6b0v"
        }
      ]
    }
    

## How time limit works for VMs in a MIG

When you specify a time limit for VMs in a MIG, the time at which a MIG will terminate a VM is automatically set in the termination timestamp (`terminationTimestamp`) field of the VM.

Based on the type of time limit that you specify, the termination timestamp of a VM is set as follows:

  * Time limit as a run duration (`maxRunDuration`):

`terminationTimestamp` of a VM = VM's latest creation or start time + `maxRunDuration`

When you specify a duration, the termination timestamp is set relative to the VM's latest creation or start time. If the VM is recreated, restarted, resumed, or replaced, then the termination timestamp is recalculated. The termination timestamp can vary across the VMs in a MIG based on the time that each VM was last created or started. For example, if a VM is repaired, the termination timestamp of the VM is recalculated by adding the duration to the time the VM was recreated during the repair.

  * Time limit as a termination time (`terminationTime`):

`terminationTimestamp` of a VM = `terminationTime`

When you specify a time, the termination timestamp is set to that time, provided the time is in the future. If the termination time has passed, any MIG action that attempts to create, restart, or replace a VM fails with an [error](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors). To resolve such an error, you must create a new instance template with a termination time in the future and apply that template to the MIG. If you want to use the existing template properties in the new template, then [create an instance template based on the existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template).




During a VM refresh, the termination timestamp doesn't change. For example, if you set the [disruption level](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#controlling_the_disruption_level_during_a_rolling_update) for updates to `REFRESH`, then the termination timestamp is retained whenever the MIG updates the VM.

When you [suspend or stop](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig) a VM in a MIG, the termination timestamp is automatically cleared irrespective of the type of time limit. When you resume or start a VM, the termination timestamp is set again based on the type of time limit as explained earlier in this section.

### How autoscaling works when a time limit is set

[Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) lets your MIG automatically add or remove VMs based on increases or decreases in load. When a MIG deletes VMs that have reached their termination timestamps, the MIG creates new VMs to maintain the [recommended size](https://docs.cloud.google.com/compute/docs/autoscaler#recommended_size) by the autoscaler. The new VMs run for the specified time limit. If the autoscaler recommendation is to reduce the number of VMs, then the MIG deletes VMs even before they reach their time limits.

If you've configured [scaling schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules), the VMs run only until the end of a schedule or until a VM reaches its termination timestamp, whichever comes first.

## What's next

  * Learn about the [basic scenarios for creating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * Learn about [applying a new instance template to an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
