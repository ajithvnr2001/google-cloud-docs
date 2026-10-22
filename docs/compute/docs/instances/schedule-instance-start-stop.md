---
url: https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop/
title: Scheduling a VM instance to start and stop \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:51.793115+00:00
---

# Scheduling a VM instance to start and stop  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Scheduling a VM instance to start and stop Stay organized with collections  Save and categorize content based on your preferences. 

Instance schedules let you [start and stop virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) automatically. To use instance schedules, create a resource policy detailing the start and stop behavior, and then attach the policy to one or more VM instances.

Using instance schedules to automate deployment of your VM instances can help you optimize costs and manage VM instances more efficiently. You can use instance schedules for both recurring and one-off workloads. For example, use instance schedules to only run VM instances during working hours or to provide capacity for a onetime event.

To learn about other options for automatically scheduling VMs, see the following pages:

  * [Scale based on schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules): If you run your workload on a managed instance group (MIG), you can use scaling schedules to schedule the required number of virtual machine (VM) instances for recurring or onetime events.

  * [Limit the run time of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime): If you don't want to create resource policies, you can directly configure a VM to be automatically stopped or deleted when it reaches a specific time or duration.




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




## Required roles

To use instance schedules, you need to grant the required Identity and Access Management (IAM) roles to the following principals:

  * The [Compute Engine Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) for your project. This is needed for the instance schedule to run on a VM.

If you revoke these permissions after creating instance schedules, your instance schedules might stop working without notice. To verify if your instance schedules run successfully, you should regularly check the [audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging).

  * The user account or service account that creates, manages, or uses the instance schedule.




### Compute Engine Service Agent required roles

To ensure that the Compute Engine Service Agent has the necessary permissions to run instance schedule, ask your administrator to grant the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role to the Compute Engine Service Agent on the project. **Important:** You must grant this role to the Compute Engine Service Agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to run instance schedule. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to run instance schedule:

  * `compute.instances.start`
  * `compute.instances.stop`



Your administrator might also be able to give the Compute Engine Service Agent these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### User or service account required roles

To ensure that you or your service account has the necessary permissions to create and manage instance schedules, ask your administrator to grant the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role to you or your service account on your project or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage instance schedules. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage instance schedules:

  * Create an instance schedule: `compute.resourcePolicies.create`
  * List an instance schedule: `compute.resourcePolicies.list`
  * Describe an instance schedule: `compute.resourcePolicies.get`
  * Delete an instance schedule: `compute.resourcePolicies.delete`
  * Attach an instance schedule to a new VM: 
    * `compute.instances.create`
    * `compute.resourcePolicies.use`
    * `compute.instances.addResourcePolicies`
  * Attach an instance schedule to an existing VM: 
    * `compute.resourcePolicies.use`
    * `compute.instances.addResourcePolicies`
  * Remove an instance schedule from a VM: 
    * `compute.resourcePolicies.use`
    * `compute.instances.removeResourcePolicies`



Your administrator might also be able to give you or your service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * You can only attach an instance schedule to VM instances that are located in the same region as the instance schedule.
  * You can't use instance schedules to stop an instance that has Local SSD disks.
  * Each VM instance can only follow one instance schedule, but you can attach each instance schedule to up to 1,000 VM instances.
  * Instance schedules don't provide capacity guarantees, so if the resources required for a scheduled VM instance are not available at the scheduled time, your VM instance might not start when scheduled. Although you can [reserve VM instances](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) before starting them to obtain a high level of assurance that your capacity is available when needed, reservations can't be automatically scheduled.
  * Instance schedules only start and stop VM instances at the specified times, but you can manually start and stop VM instances at any time. For example, suppose you have a schedule that starts daily at 8 AM and stops daily at 5 PM. If you attach that schedule to a stopped VM instance at 4 PM, that VM instance does not start until 8 AM the next day unless you manually start the VM instance before then.
  * Scheduled VM instances might take up to 15 minutes past the scheduled time to begin a start or stop operation. If you need VM instances to start or stop at a specific time, schedule the operation 15 minutes earlier than needed, and schedule each operation at least 15 minutes apart.
  * The scheduler might fail if there is a gap of less than 15 minutes between the start and stop operations. This is because the stop operation might occur before the start operation, preventing the start operation from happening.
  * Each instance schedule lets you have up to one start operation and up to one stop operation per hour.
  * To modify an instance's schedule, use a patch operation on the Instance Schedule policy.



## Managing instance schedules

Create, list, describe, and delete instance schedules using the Google Cloud console, Google Cloud CLI, or Compute Engine API.

### Creating an instance schedule

Create an instance schedule that describes when your VM instances should automatically start or stop. The instance schedule that you create is a resource policy, which you can use by attaching or removing it from VM instances.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page.

**Note:** If you don't see this option, [create a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) first.
  3. Click date_range **Create schedule**. The **Create a schedule** pane opens.

  4. Enter a **Name**.

  5. In the **Region** drop-down menu, select the location for this instance schedule.

  6. Define when the instance schedule starts and stops any attached VM instances. If you need VM instances to start or stop at a specific time, schedule the operation 15 minutes earlier than needed. Make sure each start and stop operation are at least 15 minutes apart.

Use either the default **Start time** , **Stop time** , and **Frequency** fields or, if you want to configure a more complex schedule, use cron expressions.

     * Default fields:

       1. Enter a **Start time** , a **Stop time** , or both. 
          * In the **Start time** field, type or click access_time to select the time to start VM instances.
          * In the **Stop time** field, type or click access_time to select the time to stop VM instances.
       2. In the **Frequency** drop-down menu at the bottom of the pane, select how often the **Start time** and **Stop time** repeat.
     * Cron expressions:

       1. To enable cron expressions, click the **Use CRON expression** toggle at the top of the pane.
       2. Enter a **Start CRON expression** , **Stop CRON expression** , or both. 
          * In the **Start CRON expression** field, enter a cron expression that describes when to start VM instances.
          * In the **Stop CRON expression** field, enter a cron expression that describes when to stop VM instances.
  7. In the **Time zone** drop-down menu, select the time zone for the **Start time** and **Stop time**.

  8. Optional: In the **Initiate date** field, type or click date_range to select the date and time when you want this instance schedule to begin. If omitted, the schedule is effective immediately.

  9. Optional: In the **End date** field, type or click date_range to select the date and time when you want this instance schedule to end. If omitted, the schedule is effective indefinitely.

  10. Click **Submit**.




###  gcloud 

To create an instance schedule using the gcloud CLI, use the [`gcloud compute resource-policies create instance-schedule` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/instance-schedule):
    
    
    gcloud compute resource-policies create instance-schedule SCHEDULE_NAME \
        --region=REGION \
        [--vm-start-schedule='START-OPERATION_SCHEDULE'] \
        [--vm-stop-schedule='STOP-OPERATION_SCHEDULE'] \
        [--timezone=TIME_ZONE] \
        [--initiation-date=INITIATION_DATE] \
        [--end-date=END_DATE]
    

Replace the following:

  * SCHEDULE_NAME: the name of the new instance schedule.
  * REGION: the region where the VM instances that you want to attach to this instance schedule are located.
  * Specify at least one of the following: 
    * START-OPERATION_SCHEDULE: a schedule that describes when the attached VM instances are started, formatted as a cron expression. If you need VM instances to start at a specific time, schedule the operation 15 minutes earlier than needed. For more information, see start-operation schedule.
    * STOP-OPERATION_SCHEDULE: a schedule that describes when the attached VM instances are stopped, formatted as a cron expression. If you need VM instances to stop at a specific time, schedule the operation 15 minutes earlier than needed. For more information, see stop-operation schedule.
  * TIME_ZONE: Optional: the location-based IANA time zone for this instance schedule. If omitted, the default value `UTC` is used. For more information, see time zone.
  * INITIATION_DATE: Optional: the first date that instance schedule is effective, formatted as an RFC 3339 timestamp. If omitted, the schedule is effective immediately. For more information, see initiation date.
  * END_DATE: Optional: the last date that instance schedule is effective, formatted as an RFC 3339 timestamp. If omitted, the schedule is effective indefinitely. For more information, see end date.



###  REST 

To create an instance schedule using the Compute Engine API, make a request using the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies
    {
      "name": "SCHEDULE_NAME",
      "instanceSchedulePolicy": {
        "vmStartSchedule": {
          "schedule": "START-OPERATION_SCHEDULE"
        },
        "vmStopSchedule": {
          "schedule": "STOP-OPERATION_SCHEDULE"
        },
        "timeZone": "TIME_ZONE",
        "startTime":"INITIATION_DATE",
        "expirationTime":"END_DATE"
      }
    }
    

Replace the following:

  * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * REGION: the region where the VM instances that you want to attach to this instance schedule are located.
  * SCHEDULE_NAME: the name of the new instance schedule.
  * START-OPERATION_SCHEDULE or STOP-OPERATION_SCHEDULE: Specify at least one of the following: 
    * START-OPERATION_SCHEDULE: a schedule that describes when the attached VM instances are started, formatted as a cron expression. If you need VM instances to start at a specific time, schedule the operation 15 minutes earlier than needed. For more information, see start-operation schedule.
    * STOP-OPERATION_SCHEDULE: a schedule that describes when the attached VM instances are stopped, formatted as a cron expression. If you need VM instances to stop at a specific time, schedule the operation 15 minutes earlier than needed. For more information, see stop-operation schedule.
  * TIME_ZONE: the location-based IANA time zone for this instance schedule. For more information, see time zone.
  * INITIATION_DATE: Optional: the first date that instance schedule is effective, formatted as an RFC 3339 timestamp. If omitted, the schedule is effective immediately. For more information, see initiation date.
  * END_DATE: Optional: the last date that instance schedule is effective, formatted as an RFC 3339 timestamp. If omitted, the schedule is effective indefinitely. For more information, see end date.



Each instance schedule has the following settings:

start-operation schedule, stop-operation schedule
    

Schedules that describe when the instance schedule starts and stops any attached VM instances. An instance schedule can have one of these schedules or both.

When creating instance schedules using the Google Cloud console, you can either select a **Start time** , **Stop time** , and **Frequency** or format each schedule as a [cron expression](https://wikipedia.org/wiki/Cron#CRON_expression). When creating instance schedules using the gcloud CLI or Compute Engine API, you must format each schedule as a cron expression.

The following table defines the fields of a cron expression and the supported values for each field.

Minute | Hour | Day of the month | Month | Day of the week  
---|---|---|---|---  
0-59 | 0-23 | 1-31  
where 29-31 are only effective for relevant months | 1-12 | 0-6 or `SUN-SAT` (Sunday-Saturday)  
where 0=`SUN`, 1=`MON`, … 6=`SAT`  
**Note:** Operation schedules repeat every year unless you specify an initiation date and end date.  In addition to these values, every field in a cron expression can also use the following special characters. Special character | Meaning | Example  
---|---|---  
`*` | any | If the day-of-the-month field, month field, and day-of-the-week field are all set to `*`, the schedule repeats every day.  
`-` | range | If the day-of-the-week field is set to `MON-FRI` (or `1-5`), the schedule repeats every week Monday through Friday.  
`,` | list | If the month field is set to `1-6,8-12`, the schedule repeats every month except July.  
  
When you write a cron expression, consider the following:

  * Whitespace is used to separate the fields of a cron expression. Remember to not add extra whitespace in a field that is using special characters.
  * When you specify both a day of the week and a day of the month (when neither field is set to `*`), the schedule uses the union of these values, not the intersection. For example, the schedule `0 8 1 * MON` starts at 8 AM on every Monday and on the first day of every month. That schedule does _not_ start at 8 AM only on Mondays that are also the first day of the month.


time zone
    

The location-based IANA time zone for the start-operation schedule and stop-operation schedule. The [IANA time zone database](https://wikipedia.org/wiki/Tz_database) defines a [list of available values](https://wikipedia.org/wiki/List_of_tz_database_time_zones). This time zone is used as reference for only the start-operation and stop-operation schedules—it is not used for the initiation date and end date. The time zone is optional when using the gcloud CLI or Compute Engine API. If omitted, the default value `UTC` is used.

Some IANA time zones observe [daylight saving time](https://wikipedia.org/wiki/Daylight_saving_time) (DST), which can impact your instance schedules. The details of DST—such as when DST starts and ends, as well as how much time is skipped and repeated—vary according to each time zone.

**Note:** When DST begins and ends, instance schedules have the following behavior:

  * Operations that are scheduled during the period when DST begins, and time is skipped, are still executed but with an offset. For example, if an operation is scheduled for 2:15 AM but DST skips the 2 AM hour, the operation for that day begins at 3:15 AM instead. This skipped time might cause your VM instances to run for less time than they would have otherwise. If the skipped time causes a start operation and stop operation to be scheduled at the same time, the stop operation is prioritized and the start operation is ignored.
  * Operations that are scheduled during the period when DST ends, and time is repeated, are executed at the first occurrence of that time. This repeated time might cause your VM instances to run for more time than they would have otherwise.


initiation date, end date
    

The timeframe that the instance schedule is effective. Both values are optional. Operations repeat annually unless you specify these values to limit the schedule to a single year.

When creating instance schedules using the Google Cloud console, select a date, time, and time zone using the **Initiate date** and **End date** fields.

When creating instance schedules using the gcloud CLI or Compute Engine API, these values are formatted as an [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp:
    
    
      YYYY-MM-DDTHH:MM:SSOFFSET

Replace the following:

  * YYYY-MM-DD: a date formatted as a 4-digit year, 2-digit month, and 2-digit day of the month separated by hyphens.
  * HH:MM:SS: a time formatted as a 2-digit hour using 24-hour time, 2-digit minute, and 2-digit second separated by colons.
  * OFFSET: the time zone formatted as an offset of Coordinated Universal Time (UTC). For example, Pacific Standard Time (PST), which is 8 hours earlier than UTC, is written as `-08:00`. Alternatively, to use no offset (the UTC time zone), write `Z`.



### Listing instance schedules

List instances schedules to view all existing instance schedules for your project.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page. This displays a list of all the instance schedules for this project.




###  gcloud 

To view a list of all of your resource policies, including instance schedules, using the gcloud CLI, use the [`gcloud compute resource-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list). Optionally, to restrict the results to a specific region, include the `--filter` flag.
    
    
    gcloud compute resource-policies list \
        [--filter="region:(REGION)"]
    

Replace the following:

  * REGION: Optional: the region where the instance schedules that you want to list are located.



###  REST 

To view a list of all your resource policies, including instance schedules, in a specific region using the Compute Engine API, make a request using the [`resourcePolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies
    

Replace the following:

  * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * REGION: the region where the instance schedules that you want to list are located.



### Describing an instance schedule

Describe an instance schedule to view its description, timing, operations, and a list of all of the VM instances that it is attached to.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page. This displays a list of all the instance schedules for this project.

  3. Click the name of the instance schedule that you want to describe. This opens the **Instance schedules details** page for that schedule.




###  gcloud 

To describe an instance schedule using the gcloud CLI, use the [`gcloud compute resource-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/describe):
    
    
    gcloud compute resource-policies describe SCHEDULE_NAME \
        --region=REGION
    

Replace the following:

  * SCHEDULE_NAME: the name of the instance schedule that you want to describe.
  * REGION: the region where the instance schedule is located.



The output is similar to the following:
    
    
    ...
    description: Every Monday to Friday in 2022, start VMs at 8 AM and stop VMs at 5 PM.
    ...
    instanceSchedulePolicy:
     expirationTime: '2022-12-31T23:59:59Z'
     startTime: '2022-01-01T00:00:00Z'
     timeZone: UTC
     vmStartSchedule:
       schedule: 0 8 * * MON-FRI
     vmStopSchedule:
       schedule: 0 17 * * MON-FRI
    ...
    name: example-instance-schedule
    region: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-west1
    resourceStatus:
     instanceSchedulePolicy:
       nextRunStartTime: '2022-01-03T08:00:00Z'
    ...
    status: READY
    

###  REST 

To describe an instance schedule using the Compute Engine API, make a request using the [`resourcePolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies/SCHEDULE_NAME
    

Replace the following:

  * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * REGION: the region where the instance schedule is located.
  * SCHEDULE_NAME: the name of the instance schedule that you want to describe.



The output is similar to the following:
    
    
    {
      ...
      "description": "Every Monday to Friday in 2022, start VMs at 8 AM and stop VMs at 5 PM.",
      "name": "example-instance-schedule",
      "instanceSchedulePolicy": {
        "vmStartSchedule": {
          "schedule": "0 8 * * MON-FRI"
        },
        "vmStopSchedule": {
          "schedule": "0 17 * * MON-FRI"
        },
        "timeZone": "UTC",
        "startTime": "2022-01-01T00:00:00Z",
        "expirationTime": "2022-12-31T23:59:59Z"
      },
      "status": "READY",
      "resourceStatus": {
        "instanceSchedulePolicy": {
          "nextRunStartTime": "2022-01-03T08:00:00Z"
        }
      },
      ...
    }
    

### Deleting an instance schedule

Delete an instance schedule when you no longer need it by removing any attached VM instances and deleting the resource policy.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page. This displays a list of all the instance schedules for this project.

  3. Select the checkboxes for the instance schedules that you want to delete.

  4. Click delete **Delete** at the top of the page. This opens a new dialog to confirm this action.

  5. In the dialog, click **Delete**.




###  gcloud 

  1. If this instance schedule is attached to any VM instances, remove them. 
     1. To check which VM instances this schedule is attached to, describe the instance schedule.
     2. For each VM instance that this schedule is attached to, remove the instance schedule.
  2. To delete an instance schedule using the gcloud CLI, use the [`gcloud compute resource-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/delete):
         
         gcloud compute resource-policies delete SCHEDULE_NAME \
            --region=REGION
         

Replace the following:

     * SCHEDULE_NAME: the name of the instance schedule that you want to delete.
     * REGION: the region where the instance schedule is located.



###  REST 

  1. If this instance schedule is attached to any VM instances, remove them. 
     1. To check which VM instances this schedule is attached to, describe the instance schedule.
     2. For each VM instance that this schedule is attached to, remove the instance schedule.
  2. To delete an instance schedule using the Compute Engine API, make a request using the [`resourcePolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/delete):
         
         DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies/SCHEDULE_NAME
         

Replace the following:

     * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * REGION: the region where the instance schedule is located.
     * SCHEDULE_NAME: the name of the instance schedule that you want to delete.



## Using instance schedules with VM instances

To use an instance schedule, attach it to one or more VM instances that you want to follow that schedule. You can attach an instance schedule to an existing VM instance or while creating a new VM instance. To stop a VM instance from following an attached instance schedule, remove the schedule from that VM instance.

### Attaching an instance schedule while creating a new VM instance

To attach an instance schedule to a new VM instance, you must create the VM instance in the same region as the instance schedule that you use. Learn more about [creating a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  Console 

You cannot attach an instance schedule while creating an instance using the Google Cloud console. To use the Google Cloud console to attach an instance schedule to a new VM instance, [create a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), and then attach a schedule to the VM instance.

###  gcloud 

To attach an instance schedule to a VM instance using the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--resource-policies` flag. For example, to create a VM instance from a public image with an attached instance schedule, use the following command:
    
    
    gcloud compute instances create VM_NAME \
        --resource-policies=SCHEDULE_NAME \
        --zone=ZONE \
        [--image IMAGE | --image-family IMAGE_FAMILY] \
        [--image-project IMAGE_PROJECT]
    

Replace the following:

  * VM_NAME: the name of the VM instance that you want to attach an instance schedule to.
  * SCHEDULE_NAME: the name of the instance schedule that you want to attach.
  * ZONE: the zone where your VM instance is located.
  * Optional: create a VM instance from a public image: 
    * IMAGE or IMAGE_FAMILY: Specify one of the following:
    * IMAGE: the required version of a public image. For example, `--image debian-10-buster-v20200309`.
    * IMAGE_FAMILY: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `--image-family debian-10`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
    * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) containing the image.



###  REST 

To attach an instance schedule to a VM instance using the Compute Engine API, make a request using [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and include the `resourcePolicies` attribute. For example, to create a VM instance from a public image with an attached instance schedule, make the following request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ],
      "resourcePolicies": [
        "https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies/SCHEDULE_NAME"
      ]
    }
    

Replace the following:

  * PROJECT_ID: the ID of the project to create the VM in.
  * ZONE: the zone to create the VM in.
  * MACHINE_TYPE_ZONE: the zone containing the machine type to use for the new VM.
  * MACHINE_TYPE: the machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new VM.
  * VM_NAME: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * Optional: create a VM instance from a public image: 
    * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) containing the image. For example, if you specify `family/debian-10` as the image family, specify `debian-cloud` as the image project.
    * IMAGE or IMAGE_FAMILY: specify one of the following:
    * IMAGE: the required version of a public image. For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`
    * IMAGE_FAMILY: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
  * REGION: the region where the instance schedule is located.
  * SCHEDULE_NAME: the name of the instance schedule that you want to attach.



You can verify if the instance schedule runs successfully by checking the [audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) for the instance schedule resource policy and the attached VM instance. You might need to wait for up to 15 minutes after the scheduled time for each operation.

### Attaching an instance schedule to an existing VM instance

You can attach an instance schedule to any existing VM instance that is located in the same region as the instance schedule.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page. This displays a list of all the instance schedules for this project.

  3. Click the name of the instance schedule that you want to attach. The **Instance schedule details** page opens.

  4. Click **Add instances to schedule**. The **Add instances to schedule** pane opens.

  5. Select the checkbox for each VM instance that you want to attach this schedule to.

  6. Click **Add**.




###  gcloud 

To attach an instance schedule to a VM instance using the gcloud CLI, use the [`gcloud compute instances add-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-resource-policies):
    
    
    gcloud compute instances add-resource-policies VM_NAME \
        --resource-policies=SCHEDULE_NAME \
        --zone=ZONE
    

Replace the following:

  * VM_NAME: the name of the VM instance that you want to attach an instance schedule to.
  * SCHEDULE_NAME: the name of the instance schedule that you want to attach.
  * ZONE: the zone where your VM instance is located.



###  REST 

To attach an instance schedule to a VM instance using the Compute Engine API, make a request using the [`instances.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addResourcePolicies):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances/VM_NAME/addResourcePolicies
    {
      "resourcePolicies": "projects/PROJECT/regions/REGION/resourcePolicies/SCHEDULE_NAME"
    }
    

Replace the following:

  * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * ZONE: the zone where your VM instance is located.
  * VM_NAME: the name of the VM instance that you want to attach an instance schedule to.
  * REGION: the region where the instance schedule is located.
  * SCHEDULE_NAME: the name of the instance schedule that you want to attach.



You can verify if the instance schedule runs successfully by checking the [audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) for the instance schedule resource policy and the attached VM instance. You might need to wait for up to 15 minutes after the scheduled time for each operation.

### Removing an instance schedule from a VM instance

To stop a VM instance from following an instance schedule, remove the instance schedule from the VM instance.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Instance schedules** tab at the top of the page. A list of all the instance schedules for this project is displayed.

  3. Click the name of the instance schedule that you want remove. The **Instance schedule details** page opens.

  4. Under the **Attached Instances** section, select the checkbox for each VM instance that you want to remove from this schedule.

  5. Click delete **Remove instances from schedule**. This opens a new dialog to confirm this action.

  6. In the dialog, click **Remove**.




###  gcloud 

To remove an instance schedule from a VM instance using the gcloud CLI, use the [`gcloud compute instances remove-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies):
    
    
    gcloud compute instances remove-resource-policies VM_NAME \
        --resource-policies=SCHEDULE_NAME \
        --zone=ZONE
    

Replace the following:

  * VM_NAME: the name of the VM instance that you want to remove an instance schedule from.
  * SCHEDULE_NAME: the name of the instance schedule that you want to remove.
  * ZONE: the zone where your VM instance is located.



###  REST 

To remove an instance schedule from a VM instance using the Compute Engine API, make a request using the [`instances.removeResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/removeResourcePolicies):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances/VM_NAME/removeResourcePolicies
    {
      "resourcePolicies": "projects/PROJECT/regions/REGION/resourcePolicies/SCHEDULE_NAME"
    }
    

Replace the following:

  * PROJECT: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * ZONE: the zone where your VM instance is located.
  * VM_NAME: the name of the VM instance that you want to remove an instance schedule from.
  * REGION: the region where the instance schedule is located.
  * SCHEDULE_NAME: the name of the instance schedule that you want to remove.



## What's next

  * Learn about other Compute Engine features for scheduling VMs: 
    * [Limit the runtime of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)
    * [Scale MIGs based on schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
