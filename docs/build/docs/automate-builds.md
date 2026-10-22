---
url: https://docs.cloud.google.com/build/docs/automate-builds/
title: Quickstart: Automate builds by using Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:26.288010+00:00
---

# Quickstart: Automate builds by using Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automate-builds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Automate builds by using Cloud Build

This page explains how to use Cloud Build to automate builds.

Cloud Build uses **build triggers** to enable CI/CD automations. You can configure triggers to listen for incoming events, such as when a new commit is pushed to a repository or when a pull request is initiated, and then automatically invoke a build when new events come in.

You will create a trigger and configure that trigger to invoke a build anytime you push a change to a GitHub repository.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/home/dashboard?walkthrough_id=cloud_build_automate)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-automate)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-automate)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you've already installed Google Cloud CLI previously, make sure you have the latest available version by running `gcloud components update`.

  16. If you don't have one already, create an account on [GitHub](https://github.com/).

  17. If you have two-factor authentication set up on GitHub, [create a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to use in place of a GitHub password with the command line.




## Required roles

To get the permissions that you need to automate builds by using Cloud Build, ask your administrator to grant you the following IAM roles on the Cloud Build service account: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)
  * [Storage Bucket Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)
  * [Cloud Build Connection Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Fork and clone a sample GitHub repository

You'll need some sample source code to build. In this section, you'll clone an existing source repository containing a Hello World example in Go to your own GitHub user account. 

  1. If you don't have one already, create an account on [GitHub](https://github.com/).

  2. If you have two-factor authentication set up on GitHub, [create a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to use in place of a GitHub password with the command line.

  3. Fork the `cloud-build-samples` repository to your own GitHub account:

     1. Go to the Cloud Build [cloud-build-samples repository](https://github.com/GoogleCloudPlatform/cloud-build-samples).

     2. Click on the **Fork** icon on the top-right corner of the page.

     3. Click on the GitHub user account you want to fork the repository to.

You will automatically be redirected to the page with your forked version of the `cloud-build-samples` repository.

  4. Open a terminal in your local environment.

  5. Clone the forked repository by running the following command, where GITHUB_USERNAME is the username for your GitHub account:
         
         git clone https://github.com/GITHUB_USERNAME/cloud-build-samples.git




## Connect Cloud Build to your repository

To build source code on GitHub using triggers, you must first connect Cloud Build to your GitHub repository. In this section, you'll connect your `cloud-build-samples` repository to Cloud Build. 

  1. In the Google Cloud console navigation menu, click **Cloud Build > Triggers**.

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project and click **Open**. 

  3. Click **Connect repository**.

  4. Under **Select source** , select **GitHub (Cloud Build GitHub App)**.

  5. Click **Continue**.

  6. Authenticate your GitHub account.

  7. In the **Select repository** section, select the username of your **GitHub account**. If your username doesn't appear in the list:

     1. In the **GitHub account** list, click **+Add**.

You will see a pop-up to install the Cloud Build GitHub app.

     2. Click on your GitHub username.

     3. Click **Only certain repositories** to install the Cloud Build GitHub app on certain repositories.

     4. On the drop-down menu, select **GITHUB_USERNAME /cloud-build-samples**, where GITHUB_USERNAME is the username for your GitHub account.

     5. Click **Install**.

You may be asked to enter the password associated with your GitHub account before proceeding.

     6. Following the installation of the Cloud Build GitHub app, you will now be able to see your username in the drop-down menu on the **GitHub account** field. Select your username.

  8. Under **Repository** , select **GITHUB_USERNAME /cloud-build-samples** as your repository.

  9. Click the checkmark to agree to terms and conditions for trigger connection.

  10. Click **Connect**.

  11. Click **Done**.


You will create a trigger in the next section. 

## Create a trigger

  1. Open the **Triggers** page in the Google Cloud console:

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project from the project selector drop-down menu at the top of the page.

  3. Click **Open**.

  4. On the **Triggers** page, click **Create trigger**.

  5. On the **Create trigger** page, enter the following settings:

     * **Name** : Enter `hello-world-trigger` as the name of your trigger.

     * **Event** : Select **Push to a branch** as the repository event to invoke your trigger.

     * **Source** : Select the `cloud-build-samples` repository as your source, which contains your source code and your build config file.

     * **Build Configuration** : Choose **Cloud Build configuration file** as your build config file.

     * **Cloud Build configuration file location** : Specify the path to your Cloud Build configuration file as `quickstart-automate/cloudbuild.yaml`.

  6. Click **Create** to save your build trigger.




## Commit a change

In this section, you will commit a change to your cloned `cloud-build-samples` repository on your own GitHub account.

  1. In your terminal, navigate to the `quickstart-automate` directory:
         
         cd cloud-build-samples/quickstart-automate

  2. Open the `main.go` file and update the line containing "Hello, world!" to "Hello, universe!"
         
         package main
         
           import (
               "fmt"
           )
         
           func main() {
               fmt.Println("Hello, universe!")
           }
           

  3. Review `cloudbuild.yaml`, which is the build configuration file used by Cloud Build. When a build is invoked with a trigger, the build step in this file instructs Cloud Build to use the [ `golang` image from Docker Hub](https://hub.docker.com/_/golang) to build and run the `main.go` file.
         
         steps:
            - name: golang
              script: go run quickstart-automate/main.go
            

  4. Navigate back to the root directory of your repository:
         
         cd ..

  5. Commit your changes to GitHub by running the following commands:
         
         
             git add quickstart-automate/main.go
             git commit -m "update text"
             git push

You may be prompted to enter your credentials when pushing code to your repository. If prompted, enter your username and password or an authentication token.




You have now pushed a change to your repository. Your push will result in an automatic build by your trigger.

## View build details

In this section, you will view the build details associated with your invoked build after committing a change. 

  1. In the Google Cloud console navigation menu, click **Cloud Build > History**.

[Open the Cloud Build page](https://console.cloud.google.com/cloud-build)

  2. Select your project and click **Open**.

You will see the **Build history** page:

![Screenshot of the build history page for automate](https://docs.cloud.google.com/build/images/automate-build-history.png)

  3. In the **Build** column, click the name of a build.

  4. On the **Build details** page, click **Build Artifacts**.

You will see an output similar to the following:

![Screenshot of build artifacts](https://docs.cloud.google.com/build/images/automate-artifacts.png)

  5. To view the build log, click the download icon and view the downloaded file.




You have successfully invoked a Cloud Build build using a trigger and viewed the build details.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console navigation menu, click **Cloud Build > Triggers**.

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project and click **Open**. 

  3. In the `hello-world-trigger` row, click the Actions menu (vertical ellipses) located at the right end of the row.

  4. Select **Delete**.




You have now deleted the trigger associated with your cloned repository.

## What's next

  * Learn how to [create a basic build config file](https://docs.cloud.google.com/cloud-build/docs/configuring-builds/create-basic-configuration).
  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/cloud-build/docs/automating-builds/create-manage-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
