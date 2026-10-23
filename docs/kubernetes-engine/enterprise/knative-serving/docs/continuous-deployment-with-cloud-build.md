---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/continuous-deployment-with-cloud-build/
title: Continuous deployment from Git using Cloud Build \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:29.113413+00:00
---

# Continuous deployment from Git using Cloud Build  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/continuous-deployment-with-cloud-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Continuous deployment from Git using Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Build to automate builds and deployments to Knative serving by using [Cloud Build trigger](https://docs.cloud.google.com/build/docs/running-builds/automate-builds) to automatically build and deploy your code whenever new commits are pushed to a given branch of a Git repository.

When you use a Cloud Build trigger to build containers, the [source repository information is displayed](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions#build-source) in the Google Cloud console for your service after you deploy to Knative serving.

## Before you begin

  * You either have a git repository with a `Dockerfile` or your codebase is written in one of the languages supported by [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview): Go, Node.js, Python, Java or .NET Core. 
  * Enable the Cloud Build and Cloud Source Repositories APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sourcerepo.googleapis.com,cloudbuild.googleapis.com)




## Setting up continuous deployment from the Knative serving user interface

The procedure varies slightly depending on whether you are setting up continuous deployment on a new service or on an existing service. Click the appropriate tab to learn more.

###  New service

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create service**.

  3. Fill the _Service Settings_ with your preferences.

  4. Click **Next**.

  5. Select **Continuously deploy new revisions from a source repository**.

![Set up with Cloud Build](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/create-service-form2-cloudbuild.png)

  6. Click **Set up with Cloud Build**.

  7. Select the provider and the repository.

     * _GitHub_ \- if you are not yet authenticated, click **Authenticate** and follow the instructions. By default, connecting a repository is done via the Cloud Build GitHub app. Alternatively, you can mirror your GitHub repository in Cloud Source Repositories. To do so, click _Advanced option_ and check _Mirror GitHub repository using Cloud Source Repositories_ [Learn more](https://docs.cloud.google.com/build/docs/automating-builds/create-github-app-triggers#different_types_of_github-based_triggers)
     * _Bitbucket_ \- if you are not yet authenticated, click **Authenticate** and follow the instructions.
     * [_Cloud Source Repositories_](https://docs.cloud.google.com/source-repositories/docs)

![Set up Continuous Deployment step 1](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/continuous-deployment-step1.png)

  8. Click **Next**.

  9. Fill the options in Build Configuration step:

     * _Branch_ \- indicates what source should be used when running the trigger. You can put the [regex](https://github.com/google/re2/wiki/Syntax) here. Matched branches are automatically verified: you can see them below the input. Note that if exactly one branch is matched, the trigger will be automatically executed after the creation.
     * _Build Type_

       * If your repository should be built using Docker and it contains a Dockerfile, select **Dockerfile**. **Source location** indicates the location and name of the Dockerfile. This directory will be used as the Docker build context. All paths should be relative to the current directory.

       * Otherwise, select **Google Cloud Buildpacks**. Use **Buildpack context** to specify the directory and **Entrypoint** (optional) to provide the command to start the server. Example: `gunicorn -p :8080 main:app` for Python, `java -jar target/myjar.jar` for Java. Leave it blank to use [default behavior](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs).

![Set up Continuous Deployment step 2](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/continuous-deployment-step2.png)

  10. Click **Save**.

  11. Verify the selected settings.

![Set up Continuous Deployment verification](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/continuous-deployment-settings-selected.png)

  12. Click **Create**.

  13. Note that you are redirected to the _Service Details_ page, where you can track the progress of your Continuous Deployment set up.

  14. Once all steps are completed, note additional options:

     * Edit Continuous Deployment button.
     * Build History.
     * Source details in the [_Revision Details_ section](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions#viewing_revision_details).



### Existing service

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click **Set up Continuous Deployment**.

  4. Select the provider and the repository.

     * _GitHub_ \- if you are not yet authenticated, click **Authenticate** and follow the instructions. By default, connecting a repository is done via the Cloud Build GitHub app. Alternatively, you can mirror your GitHub repository in Cloud Source Repositories. To do so, click _Advanced option_ and check _Mirror GitHub repository using Cloud Source Repositories_ [Learn more](https://docs.cloud.google.com/build/docs/automating-builds/create-github-app-triggers#different_types_of_github-based_triggers)
     * _Bitbucket_ \- if you are not yet authenticated, click **Authenticate** and follow the instructions.
     * [_Cloud Source Repositories_](https://docs.cloud.google.com/source-repositories/docs)

![Set up Continuous Deployment step 1](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/continuous-deployment-step1.png)

  5. Click **Next**.

  6. Fill the options in Build Configuration step:

     * _Branch_ \- indicates what source should be used when running the trigger. You can put the [regex](https://github.com/google/re2/wiki/Syntax) here. Matched branches are automatically verified: you can see them below the input. Note that if exactly one branch is matched, the trigger will be automatically executed after the creation.
     * _Build Type_

       * If your repository should be built using Docker and it contains a Dockerfile, select **Dockerfile**. **Source location** indicates the location and name of the Dockerfile. This directory will be used as the Docker build context. All paths should be relative to the current directory.

       * Otherwise, select **Google Cloud Buildpacks**. Use **Buildpack context** to specify the directory and **Entrypoint** (optional) to provide the command to start the server. Example: `gunicorn -p :8080 main:app` for Python, `java -jar target/myjar.jar` for Java. Leave it blank to use [default behavior](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs).

![Set up Continuous Deployment step 2](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/continuous-deployment-step2.png)

  7. Click **Save**.

  8. The page reloads and displays the progress of the Continuous Deployment setup.

  9. Once all steps are completed, note additional options:

     * Edit Continuous Deployment button.
     * Build History.
     * Source details in the [_Revision Details_ section](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions#viewing_revision_details).



## Setting up continuous deployment manually

Refer to [Setting up continuous deployment manually](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) if you need to use a manual procedure and not the UI.

## Attach existing Cloud Build trigger to Knative serving service.

If you already have an existing Cloud Build trigger, you can attach it to the service and take advantage of Google Cloud console features in the Service Details page: **Edit Continuous Deployment** button and **Build History** chart.

To do so, you have to add a label with gcb-trigger-id as a key and the unique identifier of the Cloud Build trigger as value (not the trigger name). See [instructions](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/labels#set-labels) for setting up the label.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
