---
url: https://docs.cloud.google.com/code/docs/intellij/deploy-cloud-run-app/
title: Quickstart: Deploy a Cloud Run service with Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:34.129826+00:00
---

# Quickstart: Deploy a Cloud Run service with Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/deploy-cloud-run-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Cloud Run service with Cloud Code for IntelliJ

This page shows you how to get started with Cloud Code.

You'll set up a Hello World service that runs on Cloud Run using a sample application, deploy your service to Cloud Run, and view the status of your live service's resources.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  8. Install [Git](https://git-scm.com/downloads) so that Cloud Code can perform Git operations, like cloning a sample.
  9. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/intellij/install#installing) if you haven't already.



## Creating a service

Cloud Code comes with a collection of [code sample](https://github.com/GoogleCloudPlatform/cloud-code-samples#readme) templates to get you started quickly. To create a new service using an existing sample:

  1. In your IDE, open **File** > **New Project** and then select **Cloud Code: Cloud Run**.
  2. Select the programming language for your sample application and then click **Next**. ![Creating a service from a list of existing sample apps](https://docs.cloud.google.com/static/code/docs/intellij/images/cccr-new-app.png)
  3. Name your project and then click **Finish**.

Cloud Code clones the sample application, opens your newly created project for use, and creates the necessary Cloud Run run configurations.

  4. If you chose a Java sample application, when prompted, click **Load Maven project**.

![Maven build scripts found notification - choose Load Maven Project, Skip, or Help](https://docs.cloud.google.com/static/code/docs/intellij/images/mavensync.png)




You can now run your Hello World service. Cloud Code watches your file system for changes so that you can edit and rerun your service in near real time.

## Deploying your service to Cloud Run

To deploy your service, follow these steps:

  1. Choose the automatically created run configuration, **Cloud Run: Deploy** , from the Run/Debug configurations selector in the Navigation bar.
  2. Click ![run action icon](https://docs.cloud.google.com/static/code/docs/intellij/images/run-action-icon.png)**Run**. This brings up the Edit configuration window.
  3. Set your Google Cloud project ID.
  4. Choose a region for your deployment platform.

This quickstart uses the default platform option, **Cloud Run (fully managed)** , as the Deployment Platform.

  5. Click **Run**.

  6. View your running service by following the URL displayed in the **output window**.

  7. You can also view the status of your service (metrics, revision details, and more) by following the logs URL displayed in the output window.

![Viewing the status of your service in the Google Cloud console](https://docs.cloud.google.com/static/code/docs/intellij/images/cccr-view-logs.png)




## Viewing resource status

To view the status of your running service's resources, follow these steps:

  1. Navigate to the Cloud Run Explorer. It can be accessed from the sidebar panel on the right.

![Cloud Run explorer tab highlighted on the right hand-side panel](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-run-explorer.png)

  2. To display a service or revision's properties, click the service or revision in the explorer.

![Cloud Run explorer open with a service selected and its properties displayed below](https://docs.cloud.google.com/static/code/docs/intellij/images/service-properties.png)

  3. To view a revision's logs, right-click the revision and then click **View Cloud Logs**.

![Right-click a revision to view its logs](https://docs.cloud.google.com/static/code/docs/intellij/images/view-service-logs.png)




## Cleaning up

If you created a project for this quickstart, be sure to delete it to avoid unnecessary charges:

  1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

  2. Select the project you created for this quickstart and then click **Delete**.

This shuts down the project and schedules it for deletion.




If you're using a pre-existing project and would like to delete resources you created for this quickstart:

  * **Container image:** While Cloud Run doesn't charge when the service isn't in use, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete your image, follow the steps in [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).
  * **Cloud Run service:** To delete a Cloud Run service, navigate to Cloud Run in the Google Cloud console using the navigation menu. Select the service you'd like to delete and then click **Delete**. 



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

## What's next

  * Add [Google Cloud APIs and client libraries](https://docs.cloud.google.com/code/docs/intellij/client-libraries) to your project.
  * Customize your run configurations with [advanced settings](https://docs.cloud.google.com/code/docs/intellij/deploying-a-cloud-run-app).
  * Try creating and [running a Kubernetes application with Cloud Code](https://docs.cloud.google.com/code/docs/intellij/deploy-kubernetes-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
