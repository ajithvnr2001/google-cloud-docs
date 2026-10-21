---
url: https://docs.cloud.google.com/shell/docs/deploy-cloud-run-app/
title: Quickstart: Deploy a Cloud Run service by using Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:33.029218+00:00
---

# Quickstart: Deploy a Cloud Run service by using Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/deploy-cloud-run-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Cloud Run app by using Cloud Shell

Learn how to setup and deploy a sample Hello World application to Cloud Run and view the status of your live service's resources.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://ide.cloud.google.com/?walkthrough_tutorial_url=https%3A%2F%2Fwalkthroughs.googleusercontent.com%2Fcontent%2Fcloud_run_quickstart_index%2Fcloud_run_quickstart_index.md)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

To get the permissions that you need to deploy a Cloud Run app, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant the Cloud Build service account access to your project

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior.

For Cloud Build to build your sources, grant the Cloud Build service account the [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) role on your project:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_EMAIL_ADDRESS \
        --role=roles/run.builder

Replace `PROJECT_ID` with your Google Cloud project ID and `SERVICE_ACCOUNT_EMAIL_ADDRESS` with the email address of the Cloud Build service account. If you're using the Compute Engine default service account as the Cloud Build service account, then use the following format for the service account email address:
    
    
    PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number.

For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Create an application

  1. [Launch the Cloud Shell Editor](https://ide.cloud.google.com).
  2. From the Cloud Code status bar, select **New Application**.
  3. Choose **Cloud Run application** as your preferred application type.
  4. From the list of sample applications (Node.js, Python with Flask and Django frameworks, Java, Go), choose a Hello World app.

For example, choosing `Python (Flask): Hello World` creates a starter Python (Flask) Hello World app.

  5. Select a folder as your application location and then click **Create New Application**.

Cloud Shell Editor loads the application in a new workspace. After the workspace loads, your app is accessible in the explorer view.




## Deploy to Cloud Run

To deploy your application to Cloud Run, follow these steps:

  1. Open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Deploy to Cloud Run** command. This brings up the Cloud Run Deploy UI.
  2. If prompted, authorize Cloud Code to make Google Cloud API calls.
  3. Set your Google Cloud project.
  4. If prompted, enable the Cloud Run API by clicking **Enable APIs**.
  5. In the Deploy to Cloud Run dialog, select a pre-existing service or create a new one.
  6. If you're creating a new service, choose **Cloud Run (fully managed)** under Deployment Platform.
  7. Choose a region to deploy to.
  8. For Authentication, select **Allow unauthenticated invocations** to make this a public service.
  9. After you define your preferred settings, you can click **Deploy**.

Cloud Code builds your image, pushes it to the registry, and deploys your app to Cloud Run. Your service is now live!

  10. View your running service by following the URL displayed in your Cloud Run: Deploy dialog.




## Edit your service

To edit your application, follow these steps:

  1. With the Explorer view, find the `app.py` file that implements the service behavior.
  2. Change the message "It's running!" to a message of your choosing.
  3. After you make this change, choose the **Deploy to Cloud Run** command using the Command Palette.
  4. Check that the service you just created is selected in Service Settings.
  5. Click **Deploy**.
  6. After your application finishes building and deploying, you can refresh your service to see your updated message.



## View logs

You can also view logs from your deployed application with the Log Viewer that comes with Cloud Code.

To view logs, follow these steps:

  1. Click ![Cloud Code icon](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-icon.png)**Cloud Code** and then expand the **Cloud Run** section.
  2. Right-click your Cloud Run service and then click **View logs**.

  3. Refresh your app in the browser, and see the new logs generated by clicking the Logs refresh button.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To delete your project:

  1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

  2. Select the project you created for this quickstart and then click **Delete**.

This shuts down the project and schedules it for deletion.




If you're using a pre-existing project and would like to delete resources you created for this quickstart:

  * **Container image:** While Cloud Run doesn't charge when a service isn't in use, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete your image, open the Artifact Registry page, select the repository that contains your image, select your image, click **Delete** , and then click **Delete**.

[Open the Artifact Registry page](https://console.cloud.google.com/artifacts)

  * **Cloud Run service:** To delete a Cloud Run service, from the Cloud Run page in the Google Cloud console, select the service you'd like to delete, click **Delete** , and then click **Delete**.

[Open the Cloud Run page](https://console.cloud.google.com/run)




## What's next

  * Discover the variety of features that the [Cloud Shell Editor interface](https://docs.cloud.google.com/shell/docs/editor-overview) has to offer.
  * Learn how to [configure Cloud Shell](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell) to customize your experience.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
