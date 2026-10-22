---
url: https://docs.cloud.google.com/build/docs/build-push-docker-image/
title: Quickstart: Build and push a Docker image with Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:22.981782+00:00
---

# Quickstart: Build and push a Docker image with Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/build-push-docker-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build and push a Docker image with Cloud Build

Learn how to get started with Cloud Build by building a Docker image and pushing the image to Artifact Registry. Artifact Registry provides a single location for managing private packages and Docker container images.

You will first build the image using a `Dockerfile`, which is the Docker configuration file, and then build the same image using the Cloud Build configuration file.

**Note:** This quickstart shows you how to build an image with Docker, but Cloud Build supports most build tools and programming languages.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/getting-started?walkthrough_tutorial_id=cloud_build_quickstart)

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

  5. Enable the Cloud Build, Compute Engine and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//docs.cloud.google.com/build/docs/build-push-docker-image)

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

  12. Enable the Cloud Build, Compute Engine and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//docs.cloud.google.com/build/docs/build-push-docker-image)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you've already installed Google Cloud CLI previously, make sure you have the latest available version by running `gcloud components update`.




## Required roles

To get the permissions that you need to build a Docker image and push it to Artifact Registry, ask your administrator to grant you the following IAM roles on the Cloud Build service account: 

  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
  * [Storage Bucket Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)
  * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare source files to build

You'll need some sample source code to package into a container image. In this section, you'll create a shell script and a `Dockerfile`. A `Dockerfile` is a text document that contains instructions for Docker to build an image.

  1. Open a terminal window.

  2. Create a new directory named `quickstart-docker` and navigate into it:
         
         mkdir quickstart-docker
         cd quickstart-docker
         

  3. Create a file named `quickstart.sh` with the following contents:
         
         #!/bin/sh
         echo "Hello, world! The time is $(date)."

  4. Create a file named `Dockerfile` with the following contents:
         
         FROM alpine
         COPY quickstart.sh /
         CMD ["/quickstart.sh"]

  5. In the terminal window, run the following command to make `quickstart.sh` executable:
         
         chmod +x quickstart.sh
         




## Create a Docker repository in Artifact Registry

  1. Use the [`gcloud artifacts repositories create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) command to create a Docker repository named `quickstart-docker-repo` in the location `us-west2` with the description "Docker repository":
         
         gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
             --location=us-west2 --description="Docker repository"
         

  2. Verify that your repository was created:
         
         gcloud artifacts repositories list
         

The list of displayed repositories should include `quickstart-docker-repo`.

Artifact Registry uses a [naming convention](https://docs.cloud.google.com/artifact-registry/docs/docker/names) to identify repositories and images. For example, when you interact with Docker images stored in Artifact Registry in the `us-west2` region, you use `us-west2-docker.pkg.dev` as the registry hostname in your commands.




## Build an image using a Dockerfile

Use the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command to build a Docker image using a `Dockerfile`. You don't require a separate Cloud Build config file.

  1. Get your Google Cloud project ID by running the following command:
         
         gcloud config get-value project
         

  2. Run the following command from the directory containing `quickstart.sh` and `Dockerfile`:
         
         gcloud builds submit --region=us-west2 --tag us-west2-docker.pkg.dev/PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1
         

**Note:** If your project ID contains a colon, replace the colon with a forward slash.

After the build is complete, the output should be similar to the following:
         
         DONE
         ------------------------------------------------------------------------------------------------------------------------------------
         ID                                    CREATE_TIME                DURATION  SOURCE   IMAGES     STATUS
         545cb89c-f7a4-4652-8f63-579ac974be2e  2020-11-05T18:16:04+00:00  16S       gs://gcb-docs-project_cloudbuild/source/1604600163.528729-b70741b0f2d0449d8635aa22893258fe.tgz  us-west2-docker.pkg.dev/gcb-docs-project/quickstart-docker-repo/quickstart-image:tag1  SUCCESS
         




You've just built a Docker image named `quickstart-image` using a `Dockerfile` and pushed the image to Artifact Registry.

## Build an image using a build config file

In this section you use a Cloud Build config file to build the same Docker image built in the previous steps. The build config file instructs Cloud Build to perform tasks based on your specifications.

  1. In the same directory that contains `quickstart.sh` and the `Dockerfile`, create a file named `cloudbuild.yaml` with the following contents. This file is your build config file. At build time, Cloud Build automatically replaces `$PROJECT_ID` with your project ID.
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           script: |
             docker build -t us-west2-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1 .
           automapSubstitutions: true
         images:
         - 'us-west2-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1'

  2. Start the build by running the following command:
         
         gcloud builds submit --region=us-west2 --config cloudbuild.yaml
         

After the build is complete, the output should be similar to the following:
         
         DONE
          ------------------------------------------------------------------------------------------------------------------------------------
          ID                                    CREATE_TIME                DURATION  SOURCE          IMAGES          STATUS
          046ddd31-3670-4771-9336-8919e7098b11  2020-11-05T18:24:02+00:00  15S       gs://gcb-docs-project_cloudbuild/source/1604600641.576884-8153be22c94d438aa86c78abf11403eb.tgz  us-west2-docker.pkg.dev/gcb-docs-project/quickstart-docker-repo/quickstart-image:tag1  SUCCESS
         




You've just built `quickstart-image` using the build config file and pushed the image to Artifact Registry.

## View build details

  1. Open the Cloud Build page in the Google Cloud console.

[Open the Cloud Build page](https://console.cloud.google.com/cloud-build)

  2. If necessary, select your project and click **Open**.

You will see the **Build history** page:

![Screenshot of the build history page](https://docs.cloud.google.com/build/images/docker-build-history.png)

  3. If necessary, select `us-west2`in the **Region** drop-down menu to view builds in that region.

There will be two builds listed, one for each of the builds you executed in this quickstart.

  4. Click one of the builds.

You will see the **Build details** page.

  5. To view the artifacts of your build, under **Build Summary** , click **Build artifacts**.

You should see output similar to the following:

![Screenshot of build artifacts](https://docs.cloud.google.com/build/images/docker-artifacts.png)

You can download your build log and view your image details in Artifact Registry from this page.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Open the Artifact Registry page in the Google Cloud console.

[Open the Artifact Registry page](https://console.cloud.google.com/artifacts)

  2. Select your project and click **Open**.

  3. Select **quickstart-docker-repo**.

  4. Click **Delete**.




You have now deleted the repository that you created as part of this quickstart.

## What's next

  * Learn how to [run a Docker image](https://docs.cloud.google.com/build/docs/building/build-containers#run_the_docker_image).
  * Learn how to [create a basic build config file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).
  * Learn how to [deploy using Cloud Build](https://docs.cloud.google.com/build/docs/deploy-containerized-application-cloud-run).
  * Learn how to [build Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs).
  * Learn how to [build Java applications](https://docs.cloud.google.com/build/docs/building/build-java).
  * Learn how to [build Go applications](https://docs.cloud.google.com/build/docs/building/build-go). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
