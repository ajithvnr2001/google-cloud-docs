---
url: https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger/
title: Cloud Scheduler trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:37.751739+00:00
---

# Cloud Scheduler trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Scheduler trigger

The **Cloud Scheduler trigger** lets you schedule your integration executions for defined time periods or regular intervals across multiple regions. 

**Cloud Scheduler triggers** leverage the [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) services to provide a fully managed enterprise-grade cron job scheduler within Application Integration. Using this trigger, you can now manage all your cron jobs created within your integration, both from the Application Integration UI, and the [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) dashboard. Additionally, the **Cloud Scheduler trigger** also lets you deploy cross-region cron jobs to schedule your integration executions. 

For example, if you have provisioned your integration in `us-central1`, you can use the **Cloud Scheduler trigger** to deploy a cron job in `asia-east1` (or any of the supported Google Cloud [regions](https://cloud.google.com/about/locations) for [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview)) to call your integration's endpoint at `us-central1`. 

**Important:** Separate charges will be applicable for use of the [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) services in your integration. You will incur charges based on the number of cron jobs created using the **Cloud Scheduler trigger** in Application Integration. For more information about the Cloud Scheduler charges, see [Cloud Scheduler pricing](https://docs.cloud.google.com/scheduler/pricing). 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Cloud Scheduler trigger** : 

  1. Enable the **Cloud Scheduler API** (`cloudscheduler.googleapis.com`). 

[Enable Cloud Scheduler API](https://console.cloud.google.com/apis/enableflow?apiid=cloudscheduler.googleapis.com)

  2. Confirm that you have a Google [service account](https://docs.cloud.google.com/iam/docs/service-accounts) with the **Application Integration Invoker** role assigned. If you don't have a service account, you must create a new one, and assign the **Application Integration Invoker** role to it. 

For information about creating and managing service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)

For information about the predefined Application Integration roles, see [Predefined IAM roles](https://docs.cloud.google.com/application-integration/docs/integrations-access-permissions). 




## Add the Cloud Scheduler trigger

To add a **Cloud Scheduler trigger** to your integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Click and place the **Cloud Scheduler trigger** element in the integration editor.



## Configure the Cloud Scheduler trigger

To configure a **Cloud Scheduler trigger** , perform the following steps: 

  1. Click the **Cloud Scheduler trigger** element in the integration editor to open the trigger configuration pane. 

Specify the schedule of the **Cloud Scheduler trigger** using either of the following options: 

     * **Basic** : Use the user interface to configure the cron job schedule.
     * **Advanced** : Use a [unix-cron](https://en.wikipedia.org/wiki/Cron) expression to configure the cron job schedule. 
  2. (For Basic option) Select the **Basic** tab and do the following in the indicated fields: 
     1. **Times:** Select the time intervals at which the integration must run. 
        * **Run at a specific time:** Select this option to run the integration at a specific time.
        * **Repeat by the hour:** Select this option to repeatedly run the integration on an hourly basis.
        * **Repeat by the minute:** Select this option to repeatedly run the integration as per the specified number of minutes
     2. **Days** : Select the days on which the integration must run. You can choose to run the integration every day, or on specific days of the week, or on a specific day of the month.
     3. **Months** : Select the month(s) in which the integration must run. You can choose to run the integration every month, or during specific months.
  3. (For Advanced option) Select the **Advanced** tab and specify the schedule of the cron job using a cron expression. 

The cron expression has five values that must be specified in the following order: 

     1. Minute (0-59)
     2. Hour (0-23)
     3. Day of the month (1-31)
     4. Month, either of the following values: 
        * A number 1-12
        * A three-letter month abbreviation (For example, Jan, Feb, Mar)
     5. Day of week, either of the following values: 
        * A number from 0 - 6 starting with Sunday as 0
        * A three-letter day abbreviation (For example, Mon, Tue, Wed)

For example, to run the integration on the first day of every month, use the `* * 1 * *` cron expression. 

For more information, see [Configure cron job schedules](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules). 

  4. **Region:** Select the region where your Cloud Scheduler job will be deployed. 
  5. **Service account email:** Enter the created Google service account email address. 



### Trigger output

For each **Cloud Scheduler trigger** that is configured and published in your integration version, Application Integration creates a new Cloud Scheduler job in your Google Cloud project. 

A Cloud Scheduler job is created using the following naming convention to avoid any job duplication errors: 
    
    
        INTEGRATION_NAME__VINTEGRATION_VERSION__CLOUD_SCHEDULER_TRIGGER_NUMBER
        

**Example** : `DemoIntegration__V1__1`

### Trigger logs

A **Cloud Scheduler trigger** generates logs at the start and end of each integration execution. You can view the **Cloud Scheduler trigger** logs in the **Cloud Logging Logs Explorer** page: 

  1. In the Google Cloud console, go to the **Cloud Scheduler** page. 

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Locate your Cloud Scheduler job and click **View** in the **Logs** column. 

The **Cloud Logging Logs Explorer** page appears displaying the logs generated by the **Cloud Scheduler trigger**. 




**Note:** Application Integration doesn't store or collect any logs generated by the **Cloud Scheduler trigger**. These logs are stored in your Google Cloud project and can only be viewed from the **Cloud Logging Logs Explorer** page. 

## Edit a Cloud Scheduler trigger

####  Application Integration 

**Warning:** Editing a Cloud Scheduler trigger from Application Integration will overwrite your existing cron job with a new cron job in a new integration version. 

To edit your Cloud Scheduler trigger from Application Integration, do the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the integration that you want to edit.
  4. In the _integration editor_ , click the **Version dropdown** , and select the integration version containing the **Cloud Scheduler trigger** that you want to edit.
  5. [Unpublish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations#unpublish-an-integration) and enable editing If the selected integration version is published (in active state).
  6. Click the **Cloud Scheduler trigger** element in the integration editor to open the trigger configuration pane.
  7. Modify the Cloud Scheduler job configurations as desired.



####  Cloud Scheduler 

You can edit your Cloud Scheduler trigger by modifying the configuration of your Cloud Scheduler job from Cloud Scheduler: 

  1. In the Google Cloud console, go to **Cloud Scheduler**. 

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Select the **Cloud Scheduler** job to edit.
  3. Click **Edit**.
  4. Modify the Cloud Scheduler job configurations as desired. 

**Note:** Editing a Cloud Scheduler job from [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler) does not change the state of the target integration version.

## Pause, Resume, Copy a Cloud Scheduler job

Application Integration does not support pause, resume, and copy operations for a Cloud Scheduler job created using the **Cloud Scheduler trigger**. 

The **Cloud Scheduler trigger** throws an error in the trigger configuration pane if you manually pause the execution of a Cloud Scheduler job from [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler). 

For more information about the **Cloud Scheduler trigger** error messages, see Troubleshoot Cloud Scheduler trigger. For information about pausing and resuming a cron job using Cloud Scheduler, see [Pause or resume a job](https://docs.cloud.google.com/scheduler/docs/creating#pause)

## Delete a Cloud Scheduler job

You can delete a Cloud Scheduler job either from within your integration in Application Integration or from [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview). 

####  Application Integration 

To delete a Cloud Scheduler job from Application Integration, do the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the integration that you want to edit.
  4. In the _integration editor_ , click the **Version dropdown** , and select the integration version containing the **Cloud Scheduler trigger** that you want to delete.
  5. [Unpublish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations#unpublish-an-integration) the selected integration version. 

The Cloud Scheduler job for the corresponding integration version is deleted. 




####  Cloud Scheduler 

To delete a Cloud Scheduler job from Cloud Scheduler, do the following steps: 

  1. In the Google Cloud console, go to **Cloud Scheduler**. 

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Select the **Cloud Scheduler** job to delete.
  3. Click **Delete**. 

The Cloud Scheduler job for the corresponding integration version is deleted. 


**Note:**

  * Deleting a Cloud Scheduler job from [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler) does not delete the **Cloud Scheduler trigger** within your integration in Application Integration.
  * The **Cloud Scheduler trigger** in your integration throws an error in the trigger configuration pane if a Cloud Scheduler job is deleted using [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler). For more information about the **Cloud Scheduler trigger** error messages, see Troubleshoot Cloud Scheduler trigger.



## Best practices

As a best practice, unpublish any **Cloud Scheduler triggers** when they are no longer needed. If you leave a redundant **Cloud Scheduler trigger** published, the trigger will continue to invoke the integration automatically, which might cause additional billing charges. 

## Troubleshoot Cloud Scheduler trigger

The following table describes the errors that you might encounter in Cloud Scheduler trigger, and the corresponding causes for the errors. 

Error location | Occurrence of error | Error message | Possible causes | Resolution  
---|---|---|---|---  
Trigger configuration pane **>** Error Message | When the Cloud Scheduler job stops the execution of your integration | ` The configured Cloud Scheduler job CLOUD_SCHEDULER_JOB does not exist. It might be deleted from your Google Cloud project. ` | The Cloud Scheduler job is deleted using [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview). | [Create](https://docs.cloud.google.com/application-integration/docs/integration-versions#create-a-new-version) a new integration version to overwrite your existing Cloud Scheduler job.  
` The configured Cloud Scheduler job CLOUD_SCHEDULER_JOB is PAUSED. You must RESUME the job from your Google Cloud project. ` | The Cloud Scheduler job is paused using [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview).  | [Resume](https://docs.cloud.google.com/scheduler/docs/creating#resume) the Cloud Scheduler job from Cloud Scheduler.  
` The configured Cloud Scheduler job CLOUD_SCHEDULER_JOB is DISABLED due to an internal system error.` | Check the [Trigger logs](https://docs.cloud.google.com/application-integration/docs/configuring-cloud-scheduler-trigger#trigger-logs) to identity the issue. | [Create](https://docs.cloud.google.com/application-integration/docs/integration-versions#create-a-new-version) a new integration version to overwrite your existing Cloud Scheduler job.  
` The configured Cloud Scheduler job CLOUD_SCHEDULER_JOB is in an UPDATE_FAILED state due to a failed [CloudScheduler.UpdateJob operation](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs/patch#google.cloud.scheduler.v1.CloudScheduler.UpdateJob).` | The provided service account does not have the required IAM permissions.  | To recover a job from this state, retry [CloudScheduler.UpdateJob operation](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs/patch#google.cloud.scheduler.v1.CloudScheduler.UpdateJob) until a successful response is received.  
` The last execution of the Cloud Scheduler job CLOUD_SCHEDULER_JOB failed due to CLOUD_SCHEDULER_JOB_ISSUE. Learn more.` | CLOUD_SCHEDULER_JOB_ISSUE | NA  
  
## SLA exclusions

The Cloud Scheduler trigger is dependent on the [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) product. As this dependency is external to the Application Integration, the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions are applicable only when the execution is successfully scheduled for an `active` integration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
