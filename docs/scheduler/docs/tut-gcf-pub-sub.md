---
url: https://docs.cloud.google.com/scheduler/docs/tut-gcf-pub-sub/
title: Schedule an event-driven Cloud Run function \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:58.353953+00:00
---

# Schedule an event-driven Cloud Run function  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/tut-gcf-pub-sub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Schedule an event-driven Cloud Run function Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to trigger an event-driven Cloud Run function using Cloud Scheduler and by targeting a Pub/Sub topic. Use an event-driven function when your function should be triggered directly in response to events within your Google Cloud project, such as messages on a Pub/Sub topic or changes in a Cloud Storage bucket.

Note that you can also [schedule an HTTP function](https://docs.cloud.google.com/scheduler/docs/tut-gcf-http) by targeting your function's HTTP endpoint. Use an HTTP function when you need your function to have a URL endpoint and respond to HTTP requests, such as for webhooks. For more information, see [Types of Cloud Run functions](https://docs.cloud.google.com/functions/docs/writing#function-types).

Scheduling the execution of a Cloud Run function is a common use case for Cloud Scheduler. In this tutorial, you will:

  1. Create a simple Cloud Run function that subscribes to a Pub/Sub topic.
  2. Create a Cloud Scheduler job that publishes a message to the Pub/Sub topic.
  3. Run the Cloud Scheduler job.
  4. Verify that the Cloud Run function was triggered by the Cloud Scheduler job. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run functions](https://docs.cloud.google.com/functions)
  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build, Cloud Functions, Cloud Run Admin, Cloud Scheduler, Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,cloudfunctions.googleapis.com,run.googleapis.com,cloudscheduler.googleapis.com,eventarc.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Cloud Run > Cloud Run Invoker** role to the service account. 

To grant the role, find the **Select a role** list, then select **Cloud Run > Cloud Run Invoker**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Build, Cloud Functions, Cloud Run Admin, Cloud Scheduler, Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,cloudfunctions.googleapis.com,run.googleapis.com,cloudscheduler.googleapis.com,eventarc.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Cloud Run > Cloud Run Invoker** role to the service account. 

To grant the role, find the **Select a role** list, then select **Cloud Run > Cloud Run Invoker**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Note that you must grant the Cloud Run Invoker role because in [Cloud Run functions (2nd gen)](https://docs.cloud.google.com/functions/docs/2nd-gen/2nd-gen-differences), invocation permissions are available by managing the underlying Cloud Run service.

  10. By default, Cloud Run functions uses the automatically created [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for its runtime service account. You can use this service account to try out this tutorial. However, depending on your organization policy configuration, the default service account might not automatically be granted the Editor role on your project. If that is the case, you must [grant the service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) the following roles: 
     1. Artifact Registry Writer (`roles/artifactregistry.writer`)
     2. Logs Writer (`roles/logging.logWriter`)
     3. Storage Object Viewer (`roles/storage.objectViewer`)



## Create an event-driven Cloud Run function

Create an event-driven function that is triggered directly in response to events within your Google Cloud project; in this case, a message published to a Pub/Sub topic.

  1. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  2. Click add_box **Create function**.

  3. In the **Basics** section, do the following:

     1. In the **Environment** list, select **2nd gen**.
     2. Enter a name for your function.
     3. In the **Region** list, select a region.
  4. In the **Trigger** section, do the following:

     1. In the **Trigger type** list, select **Cloud Pub/Sub**.
     2. In the **Cloud Pub/Sub topic** list, select an existing topic or to create a new topic, click **Create a topic**. Note the topic's name as you will need it in a subsequent step.
     3. Click **More options**.

The **Eventarc trigger** panel opens.

  5. In the **Eventarc trigger** panel, do the following:

     1. If you are prompted to allow the Pub/Sub service to create the identity tokens it needs to invoke the function, click **Grant**.
     2. In the **Service account** list, select the service account you previously created.
     3. Accept the other defaults.
     4. Click **Save trigger**.

The **Eventarc trigger** panel closes.

  6. Accept the other defaults and click **Next**.

  7. Don't modify the default runtime language and sample code. The code does not use any cloud services and does not need additional permissions enabled. Click **Deploy**.




## Create a Cloud Scheduler job

Create a Cloud Scheduler job with a Pub/Sub target.

  1. In the Google Cloud console, go to the **Cloud Scheduler** page.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Click Click add_box **Create job**.

  3. Enter a name for your job.

  4. In the **Region** list, select a region.

  5. Specify the **frequency** for your job, using a unix-cron format:
         
         30 16 * * 7
         

For more information, see [Cron job format and time zone](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

  6. In the **Timezone** list, select a time zone.

  7. Click **Continue**.

  8. In the **Target type** list, select **Pub/Sub**.

  9. Select the Pub/Sub topic you created earlier.

  10. In the **Message body** field, enter a string to be sent to your Pub/Sub target topic. For example: "Hello world!"

  11. Click **Create**.




You have created a cron job that sends a message to your Pub/Sub topic at 16:30 on Sundays. Your Cloud Run function is subscribed to that topic.

## Run your Cloud Scheduler job

You can now run the job you created.

  1. In the Google Cloud console, go to the Cloud Scheduler page.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Select the checkbox for the job that you created and click **Force run**.

When it is initially invoked, the first job created in a project can take a few minutes to configure and run.

  3. After the job runs, the **Status of last execution** should indicate `Success`.




## Verify the results in Cloud Run functions

You can verify that your Cloud Run function is successfully triggered and executed by your cron job.

  1. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  2. Click the function name.

The **Function details** page opens and the **Invocations/Second** graph shows your first invocation of the function.

  3. Click the **Logs** tab.

You should see a log entry similar to `Hello, YOUR_STRING!`




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. In the Google Cloud console, go to the **Cloud Scheduler** page.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Select the checkbox next to your job.

  3. Click delete **Delete** and confirm your deletion.

  4. In the Google Cloud console, go to the **Pub/Sub** page.

[Go to Pub/Sub](https://console.cloud.google.com/cloudpubsub)

  5. Select the checkbox next to your topic.

  6. Click delete **Delete** and confirm your deletion.

  7. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  8. Select the checkbox next to your function.

  9. Click delete **Delete** and confirm your deletion.

  10. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  11. Select the checkbox next to the service account you created.

  12. Click delete **Delete** and confirm your deletion.




## What's next

  * [Use Cloud Scheduler to trigger Cloud Run on a schedule](https://docs.cloud.google.com/run/docs/triggering/using-scheduler)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
