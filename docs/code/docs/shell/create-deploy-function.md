---
url: https://docs.cloud.google.com/code/docs/shell/create-deploy-function/
title: Deploy a Cloud Run service by using Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:48.893232+00:00
---

# Deploy a Cloud Run service by using Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/create-deploy-function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Deploy a Cloud Run service by using Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to set up and deploy a sample Hello World application to Cloud Run and view the status of your live service's resources.

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




## Create an application

  1. [Launch the Cloud Shell Editor](https://ide.cloud.google.com).
  2. From the Cloud Code status bar, select **New Application**.
  3. Choose **Cloud Run application** as your preferred application type.
  4. From the list of sample applications, choose a Hello World app. For example, choosing `Python (Flask): Hello World` creates a starter Python (Flask) Hello World app.
  5. Select a folder as your application location and then click **Create New Application**. Cloud Shell Editor loads the application in a new workspace. After the workspace loads, your app is accessible in the explorer view.



## Deploy to Cloud Run

To deploy your application to Cloud Run:

  1. Choose the **Deploy to Cloud Run** command using the command palette (accessible with `Ctrl`/`Cmd`+`Shift`+`P`). This brings up the Cloud Run Deploy UI.
  2. If prompted, authorize Cloud Code to make Google Cloud API calls.
  3. Set your Google Cloud project.
  4. If prompted, enable the Cloud Run API by clicking **Enable APIs**.
  5. In the Deploy to Cloud Run dialog, select a pre-existing service or create a new one.
  6. If you're creating a new service, choose **Cloud Run (fully managed)** under Deployment Platform.
  7. Choose a region to deploy to.
  8. For Authentication, select **Allow unauthenticated invocations** to make this a public service.
  9. After you define your preferred settings, click **Deploy**. Cloud Code builds your image, pushes it to the registry, and deploys your app to Cloud Run. Your service is now live.
  10. View your running service by following the URL displayed in your Cloud Run: Deploy dialog.



## Edit your service

To edit your application:

  1. With the Explorer view, find the `app.py` file that implements the service behavior.
  2. Change the message "It's running!" to a message of your choosing.
  3. After you make this change, choose the **Deploy to Cloud Run** command using the command palette.
  4. Check that the service you created is selected in Service Settings.
  5. Click **Deploy**.
  6. After your application finishes building and deploying, you can refresh your service to see your updated message.



## View logs

You can also view logs from your deployed application with the Log Viewer that comes with Cloud Code.

To view logs:

  1. To open the Cloud Run Explorer, click ![](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-icon.png)**Cloud Code** and then expand the **Cloud Run** section.
  2. Right-click your Cloud Run service and then click **View logs**.
  3. Refresh your app in the browser, and see the new logs generated by clicking the Logs refresh button.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



If you're using a pre-existing project and want to delete the resources you created for this quickstart:

  * **Container image:** While Cloud Run doesn't charge when a service isn't in use, you might still be [charged for storing the container image in Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing). To delete your image, open the Artifact Registry page, select the repository that contains your image, select your image, click **Delete** , and then click **Delete**.   


[Open the Artifact Registry page](https://console.cloud.google.com/artifacts)

  * **Cloud Run service:** To delete a Cloud Run service, from the Cloud Run page in the Google Cloud console, select the service you'd like to delete, click **Delete** , and then click **Delete**. [Open the Cloud Run page](https://console.cloud.google.com/run)



## What's next

  * Discover the features that the [Cloud Shell Editor interface](https://docs.cloud.google.com/shell/docs/editor-overview) offers.
  * Learn how to [configure Cloud Shell](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell) to customize your experience.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
