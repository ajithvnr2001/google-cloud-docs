---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images/
title: Quickstart: Store Docker container images in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:55.562686+00:00
---

# Quickstart: Store Docker container images in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Docker container images in Artifact Registry

Artifact Registry provides a single location for managing private packages and Docker container images.

This quickstart shows you how to:

  * Create a private Docker repository in Artifact Registry
  * Set up authentication
  * Push an image to the repository
  * Pull the image from the repository



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?tutorial=artifact_registry_docker_quickstart)

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

  4. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/docker/quickstart)

  5. Make sure that you have the following role or roles on the project: Artifact Registry Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/docker/quickstart)

  9. Make sure that you have the following role or roles on the project: Artifact Registry Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Required roles

To get the permissions that you need to create and manage Artifact Registry Docker repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Choose a shell

To complete this quickstart, use either Cloud Shell or your local shell.

Cloud Shell
    [Cloud Shell](https://docs.cloud.google.com/shell/docs) is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with Docker and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), the primary command-line interface for Google Cloud.
Local shell
    If you prefer using your local shell, you must install Docker and gcloud CLI in your environment.

### Starting Cloud Shell

To launch Cloud Shell, perform the following steps:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. Click the **Activate Cloud Shell** button: ![ ](https://docs.cloud.google.com/static/artifact-registry/docs/images/cloud-shell.png).




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

### Setting up a local shell

To install gcloud CLI and Docker, perform the following steps:

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). To update an existing installation, run the command `gcloud components update`.

**Note:** On Ubuntu, use the [Debian package](https://docs.cloud.google.com/sdk/docs/install#deb) to install gcloud CLI. The gcloud CLI snap package does not include `kubectl` or extensions to authenticate with Artifact Registry using the gcloud CLI.
  2. Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it is not already installed.

  3. Docker requires privileged access to interact with registries. On Linux or Windows, add the user that you use to run Docker commands to the Docker security group. This step is not required on macOS since [Docker Desktop](https://docker-docs.uclv.cu/docker-for-mac/) runs on a virtual machine as the root user.

### Linux

The Docker security group is called `docker`. To add your username, run the following command:
         
         sudo usermod -a -G docker ${USER}
         

### Windows

The Docker security group is called `docker-users`. To add a user from the Administrator command prompt, run the following command:
         
         net localgroup docker-users DOMAIN\USERNAME /add
         

Where

     * DOMAIN is your Windows domain.
     * USERNAME is your username.

**Note:** The Docker security group has access equivalent to the root or Administrator user. Only add trusted users who require access to Docker. For details about security impacts, see [Docker daemon security](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface).
  4. Log out and log back in for group membership changes to take effect. If you are using a virtual machine, you may need to restart the virtual machine for membership changes to take effect.

  5. To ensure that Docker is running, run the following Docker command, which returns the current time and date:
         
         docker run --rm busybox date
         

The `--rm` flag deletes the container instance on exit.




## Create a Docker repository

Create a Docker repository to store the sample image for this quickstart.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click add **Create Repository**.

  3. Specify `quickstart-docker-repo` as the repository name.

  4. Choose **Docker** as the format and **Standard** as the mode.

  5. Under **Location Type** , select **Region** and then choose the location `us-west1`.

  6. Click **Create**.




The repository is added to the repository list.

###  gcloud 

  1. Run the following command to create a new Docker repository named `quickstart-docker-repo` in the location `us-west1` with the description "Docker repository".
         
         gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
             --location=us-west1 --description="Docker repository" \
             --project=PROJECT
         

Where PROJECT is your Google Cloud project ID.

  2. Run the following command to verify that your repository was created.
         
         gcloud artifacts repositories list \
             --project=PROJECT
         




For more information about Artifact Registry commands, run the command `gcloud artifacts`.

## Configure authentication

Before you can push or pull images, configure Docker to use the Google Cloud CLI to authenticate requests to Artifact Registry.

To set up authentication to Docker repositories in the region `us-west1`, run the following command:
    
    
    gcloud auth configure-docker us-west1-docker.pkg.dev
    

The command updates your Docker configuration. You can now connect with Artifact Registry in your Google Cloud project to push and pull images.

For information about other authentication methods, see [Authentication methods](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication).

## Obtain an image to push

For this quickstart, you will push a sample image named `hello-app`.

Run the following command to pull version 1.0 of the image.
    
    
    docker pull us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

Image paths in Artifact Registry include multiple parts. For this sample image:

  * `us-docker.pkg.dev` is the hostname for container images stored in Artifact Registry Docker repositories, which includes the location of the repository (`us`).
  * `google-samples` is the project ID.
  * `containers` is the repository ID.
  * `/gke/hello-app` is the path to the image in the repository `containers`.



## Add the image to the repository

Before you push the Docker image to Artifact Registry, you must tag it with the repository name.

### Tag the image with a registry name

Tagging the Docker image with a repository name configures the `docker push` command to push the image to a specific location. For this quickstart, the host location is `us-west1-docker.pkg.dev`.

Run the following command to tag the image as `quickstart-image:tag1`:
    
    
    docker tag us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 \
    us-west1-docker.pkg.dev/PROJECT/quickstart-docker-repo/quickstart-image:tag1
    

Where:

  * `us-west1` is the repository location.
  * `us-west1-docker.pkg.dev` is the hostname for the Docker repository you created.
  * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `quickstart-docker-repo` is the ID of the repository you created.
  * `quickstart-image` is the image name you want to use in the repository. The image name can be different than the local image name. For this quickstart you will store the image directly under the repository ID `quickstart-docker-repo`.
  * `tag1` is a tag you're adding to the Docker image. If you didn't specify a tag, Docker will apply the default tag `latest`.



You are now ready to push the image to the repository you created.

### Push the image to Artifact Registry

After you have configured authentication and tagged the local image, you can push the image to the repository that you created.

To push the Docker image, run the following command:
    
    
    docker push us-west1-docker.pkg.dev/PROJECT/quickstart-docker-repo/quickstart-image:tag1
    

Replace PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 

## Pull the image from Artifact Registry

To pull the image from Artifact Registry onto your local machine, run the following command:
    
    
    docker pull us-west1-docker.pkg.dev/PROJECT/quickstart-docker-repo/quickstart-image:tag1
    

Replace PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 
    
    
    latest: Pulling from [PROJECT-ID]/quickstart-image:tag1
    Digest: sha256:70c42...
    Status: Image is up to date for us-west1-docker.pkg.dev/PROJECT/quickstart-docker-repo/quickstart-image:tag1
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any images you want to keep are available in another location.

To delete the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the `quickstart-docker-repo` repository.

  3. Click **Delete**.




###  gcloud 

To delete the `quickstart-docker-repo` repository, run the following command:
    
    
    gcloud artifacts repositories delete quickstart-docker-repo --location=us-west1
    

## What's next

  * [Learn more about working with container images](https://docs.cloud.google.com/artifact-registry/docs/docker).
  * [Learn more about Docker](https://docs.docker.com/get-started/).
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps Research and Assessment (DORA)](https://dora.dev/) research program.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
