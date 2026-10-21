---
url: https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild/
title: Automate container image rebuilds to synchronize base image updates \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:06.385834+00:00
---

# Automate container image rebuilds to synchronize base image updates  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Automate container image rebuilds to synchronize base image updates Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations lets you [create and use custom images](https://docs.cloud.google.com/workstations/docs/customize-container-images) for your workstations. After a custom image is in use it's useful to automate a rebuild of the custom image in order to pull in fixes and updates available in the base images.

In this tutorial you learn how to build an automated pipeline to help ensure that you include security updates and patches in your custom workstation images.

## Objectives

By following this tutorial, you build an automated pipeline for your base image with these steps:

  1. Create an Artifact Registry repository to store and scan your custom image.
  2. Configure GitHub with Google Cloud to store your image configurations.
  3. Create a Cloud Build trigger to automate creation and deployment of custom images to Artifact Registry.
  4. Configure Cloud Scheduler to initiate builds on a regular basis.
  5. Review the results of the automated processes.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler/pricing)
  * [Container Scanning](https://cloud.google.com/artifact-analysis/pricing)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry, Container Scanning API, Cloud Build, and Cloud Scheduler APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudbuild.googleapis.com,containerregistry.googleapis.com,containerscanning.googleapis.com,artifactregistry.googleapis.com,cloudscheduler.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the `gcloud` CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Artifact Registry, Container Scanning API, Cloud Build, and Cloud Scheduler APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudbuild.googleapis.com,containerregistry.googleapis.com,containerscanning.googleapis.com,artifactregistry.googleapis.com,cloudscheduler.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the `gcloud` CLI, run the following command: 
         
         gcloud init




## Prepare the environment

Before proceeding, be sure that you set the following environment variables.

  1. Set the project ID for the cloud project you plan to use:
         
         PROJECT_ID=$PROJECT_ID
         

  2. Set the GitHub username where you plan to store your repository:
         
         GITHUB_USER=$GITHUB_ID
         

  3. Set the `PROJECT_NUMBER` and `REGION` variables to use through the process:
         
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID \
             --format='value(projectNumber)')
         
         REGION=$REGION
         

In the prior example, replace $REGION with the region name that you plan to use—for example, `us-central1`.

For more information about available regions, see [Cloud Workstations locations](https://docs.cloud.google.com/workstations/docs/locations).




## Create an Artifact Registry repository

In this tutorial you use Artifact Registry to store and scan your images.

  1. Create a repository with the following command:
         
         gcloud artifacts repositories create custom-images \
               --repository-format=docker \
               --location=$REGION \
               --description="Docker repository"
         

Replace $REGION with the region name that you plan to use.

  2. Configure Docker to use your `gcloud` CLI credentials when accessing Artifact Registry.
         
         gcloud auth configure-docker $REGION-docker.pkg.dev
         

**Note:** Keep in mind that this configuration also enables automated container scanning, which provides vulnerability scanning but has an extra price per scanned image. See [pricing details](https://cloud.google.com/artifact-analysis/pricing).

To turn off Artifact Analysis, run the following command:
         
         gcloud services disable containerscanning.googleapis.com
         




## Configure your GitHub repository

In practice, you keep the Dockerfile for your custom images in a Git repository. The automated process accesses that repository during the build process to pull the relevant configs and Dockerfile.

### Fork the sample repository

To fork a sample repository that provides container definitions, follow these steps:

  1. Click this link to [Create a new fork](https://github.com/GoogleCloudPlatform/software-delivery-workshop/fork). of the `software-delivery-workshop` repository.
  2. If prompted, sign in to GitHub.
  3. Select your GitHub username as the Owner. The Repository name appears as `software-delivery-workshop`.
  4. Click **Create fork** and wait a few seconds for the process to complete.



### Connect Cloud Build to GitHub

Next, connect that repository to Cloud Build using the built-in GitHub connection capability. Click the link to the GitHub repository and follow the instructions describing how to complete the process. You don't need to create the trigger in the last step of the wizard, and you can skip the last steps because you can do that later from the command line.

  * [Connect Cloud Build to the GitHub repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github)



If you use a different Git repository solution, you can also follow the instructions to [connect Cloud Build to GitLab](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab-enterprise-edition) or [Bitbucket](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server).

## Create a Cloud Build trigger

The sample repository contains a container definition and a Cloud Build configuration used to build the container image. In this step you create a Cloud Build trigger that runs the instructions in the `cloudbuild.yaml` file that you can find in the [labs/cloudbuild-scheduled-jobs/code-oss-java](https://github.com/GoogleCloudPlatform/software-delivery-workshop/tree/main/labs/cloudbuild-scheduled-jobs/code-oss-java) folder.
    
    
    gcloud builds triggers create manual \
        --name=custom-image-trigger \
        --repo=$GITHUB_USER/software-delivery-workshop \
        --repo-type=GITHUB \
        --branch=main \
        --build-config=labs/cloudbuild-scheduled-jobs/code-oss-java/cloudbuild.yaml \
        --substitutions=_REGION=$REGION,_AR_REPO_NAME=custom-images,_AR_IMAGE_NAME=code-oss-java,_IMAGE_DIR=labs/cloudbuild-scheduled-jobs/code-oss-java
    
    TRIGGER_ID=$(gcloud builds triggers list \
        --filter=name="custom-image-trigger" --format="value(id)")
    
    

This example configures the following:

  * The `gcloud` CLI command creates a [manual trigger](https://docs.cloud.google.com/build/docs/triggers#manual_triggers) within Cloud Build named `custom-image-trigger` as indicated by the `name` flag on the second line.
  * The next three lines contain flags related to the source GitHub repository: 
    * Path to the repository
    * [Type of the repository](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/manual#--repo-type)
    * Git branch to build
  * The `build-config` flag indicates the path to the Cloud Build file in the Git repository.
  * To make the job dynamic, use the `substitutions` flag. For this job, the command passes in the following variables:

    * Region, `$_REGION`
    * Artifact Registry repository name, `$_AR_REPO_NAME`
    * Container image name, `$_AR_IMAGE_NAME`
    * Location of the Dockerfile to build, `$_IMAGE_DIR`

View the [cloudbuild.yaml](https://github.com/GoogleCloudPlatform/software-delivery-workshop/blob/main/labs/cloudbuild-scheduled-jobs/code-oss-java/cloudbuild.yaml) file to see how these variables are used in the process.

  * After the trigger is created, the unique name of the trigger is retrieved and stored in the `$TRIGGER_ID` environment variable for later use.




## Configure Cloud Scheduler

To help ensure that your images are up to date with the latest updates and patches, use Cloud Scheduler to execute the Cloud Build trigger on a set frequency. For this tutorial, the job runs every day. In practice, set this to a frequency aligned to your organizational needs to help ensure that the latest updates are always included.

  1. Grant a required role to default service account to invoke Cloud Build trigger:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/cloudbuild.builds.editor"
         

  2. Grant a required role to Cloud Build service account to upload images to Artifact Registry:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
             --role="roles/artifactregistry.admin"
         

  3. Create the Cloud Scheduler job with the following command:
         
         gcloud scheduler jobs create http run-build \
             --schedule='0 1 * * *' \
             --uri=https://cloudbuild.googleapis.com/v1/projects/$PROJECT_ID/locations/global/triggers/$TRIGGER_ID:run \
             --location=us-central1 \
             --oauth-service-account-email=$PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --oauth-token-scope=https://www.googleapis.com/auth/cloud-platform
         

  4. The job is set to execute one time every day; however, to test the feature immediately, run the job manually from the Cloud Scheduler:

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

     1. On the Cloud Scheduler page, find the entry you just created called **run-build**.
     2. In the Actions column, click the more_vert**More** options menu for that row.
     3. Click **Force a job run** to test the system manually.
     4. After the command successfully executes, switch to the Cloud Build history page to review the progress:

[Go to Cloud Build History](https://console.cloud.google.com/cloud-build/builds)




## Review the results

Because you enabled the Container Scanning API as part of the setup process, Artifact Registry automatically scans the images for security vulnerabilities.

To review the vulnerabilities:

  1. Open the Artifact Registry Repositories page:

[Go to Artifact Registry Repositories](https://console.cloud.google.com/artifacts)

  2. In the repositories list, click a repository.

  3. Click an image name. Vulnerability totals for each image digest appear in the **Vulnerabilities** column.

![Artifact Registry Repositories page that shows a sample image name](https://docs.cloud.google.com/static/workstations/images/artifact-registry-repositories-sample-page.png)

  4. To view the list of vulnerabilities for an image, click the link in the **Vulnerabilities** column. The vulnerability list shows the [severity](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#severity_levels_for_vulnerabilities), availability of a fix, and the name of the package that contains the vulnerability.

![Artifact Registry Vulnerabilities page that shows a sample list of vulnerabilities](https://docs.cloud.google.com/static/workstations/images/artifact-registry-vulnerabilities-sample-page.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To avoid incurring charges to your Google Cloud account for the resources used on this page, make sure that you remember to delete resources that you no longer need.

To delete a Google Cloud project from the Google Cloud console or from the `gcloud` CLI: 

### Console

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### gcloud

**Caution** : Deleting a project has the following effects: 
    * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
    * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




For more information about deleting other resources, such as workstation clusters, workstation configurations, and workstations, see [Delete resources](https://docs.cloud.google.com/workstations/docs/delete-resources). 

## What's next

  * Review the list of available [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images).
  * [Customize your container images](https://docs.cloud.google.com/workstations/docs/customize-container-images).
  * [Review available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types).
  * [Set up security best practices](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
