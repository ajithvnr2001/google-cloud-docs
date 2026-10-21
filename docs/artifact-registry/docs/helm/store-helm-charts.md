---
url: https://docs.cloud.google.com/artifact-registry/docs/helm/store-helm-charts/
title: Quickstart: Store Helm charts in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:40:41.073824+00:00
---

# Quickstart: Store Helm charts in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/helm/store-helm-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Helm charts in Artifact Registry

[Helm](https://helm.sh/) is the package manager for Kubernetes. Artifact Registry lets you store and manage Helm [charts](https://helm.sh/docs/topics/charts/) in Docker-format repositories to version and deploy Kubernetes resources. In this quickstart, you create a private repository, package and push a sample chart, and deploy a release to a cluster.

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

  5. Enable the Artifact Registry, Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/helm/store-helm-charts)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Artifact Registry, Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/helm/store-helm-charts)




## Required roles

To get the permissions that you need to create and manage Helm charts in Artifact Registry Docker package repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Choose a shell

To complete this quickstart, use either Cloud Shell or your local shell.

Cloud Shell
    [Cloud Shell](https://docs.cloud.google.com/shell/docs) is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with Docker, Helm, and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), the primary command-line interface for Google Cloud.
Local shell
    If you prefer using your local shell, you must install Docker and gcloud CLI in your environment.

### Starting Cloud Shell

To launch Cloud Shell, perform the following steps:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. Click the **Activate Cloud Shell** button: ![ ](https://docs.cloud.google.com/static/artifact-registry/docs/images/cloud-shell.png).

A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

  3. [Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/). In previous versions of Helm, support for charts in OCI format is an experimental feature.

Run `helm version` to verify your version.




### Setting up a local shell

To install gcloud CLI and Helm, perform the following steps:

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). To update an existing installation, run the command `gcloud components update`.

  2. [Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/). In previous versions of Helm, support for charts in OCI format is an experimental feature.

Run `helm version` to verify your version.




## Create a repository

Create a Docker repository to store the sample chart for this quickstart.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify `quickstart-helm-repo` as the repository name.

  4. Choose Docker as the format.

  5. Under **Location Type** , select **Region** and then choose the location `us-west1`.

  6. Click **Create**.




The repository is added to the repository list.

###  gcloud 

  1. Run the following command to create a new Docker repository named `quickstart-helm-repo` in the location `us-west1` with the description "docker repository".
         
         gcloud artifacts repositories create quickstart-helm-repo --repository-format=docker \
         --location=us-west1 --description="Helm repository"
         

  2. Run the following command to verify that your repository was created.
         
         gcloud artifacts repositories list
         




For more information about Artifact Registry commands, run the command `gcloud artifacts`.

## Create a chart

For this quickstart, you will create a sample chart named `hello-chart`.

  1. Change to a directory where you want to create the chart.
  2. Run the following command to create the chart:
         
         helm create hello-chart
         

Helm creates a directory named `hello-chart` with a default set of chart files. One of the files is [Chart.yaml](https://helm.sh/docs/topics/charts/#the-chartyaml-file), which includes information about the chart.

  3. Package the chart an archive.
         
         helm package hello-chart/
         

Helm creates an archive named `hello-chart-0.1.0.tgz` using the chart name and version number in `Chart.yaml`.




## Authenticate with the repository

Before you can push or install images, Helm must authenticate to Artifact Registry.

Helm can use existing registry settings a Docker configuration file. If you haven't already configured Docker for use with Artifact Registry, you can authenticate with an access token for this quickstart.

See [Setting up authentication for Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication) for more information about authentication.

### Authenticate with your Docker configuration

By default, Helm supports registry settings in the Docker configuration file [config.json](https://docs.docker.com/engine/reference/commandline/login/#privileged-user-requirement). Helm finds registry settings in either the default location or the location specified by the [DOCKER_CONFIG](https://docs.docker.com/engine/reference/commandline/cli/#change-the-docker-directory) environment variable.

If you [configured Docker](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication) with a credential helper to authenticate with Artifact Registry, Helm uses your existing configuration for Artifact Registry Docker repositories.

### Authenticate with an access token

To authenticate with an access token:

  1. Obtain an access token as credentials when you authenticate to Artifact Registry with Helm.

### Linux / macOS

Run the following command:
         
         gcloud auth print-access-token | helm registry login -u oauth2accesstoken \
         --password-stdin us-west1-docker.pkg.dev
         

### Windows

Run the following command:
         
         gcloud auth print-access-token
         ya29.8QEQIfY_...
         
         helm registry login -u oauth2accesstoken -p "ya29.8QEQIfY_..." \
         us-west1-docker.pkg.dev/PROJECT-ID/REPOSITORY
         

Where

     * `oauth2accesstoken` is the user name to use when authenticating with an access token.
     * `gcloud auth print-access-token` is the gcloud command to obtain the access token. Your access token is the password for authentication.



Helm is now authenticated with Artifact Registry. You're ready to push the chart to the repository.

## Push the chart to Artifact Registry

After you have created your chart archive and authenticated to the Artifact Registry repository, you can push the chart to the repository.

To push the chart, run the following command:
    
    
    helm push hello-chart-0.1.0.tgz oci://us-west1-docker.pkg.dev/PROJECT/quickstart-helm-repo
    

Replace PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Helm uses values from `Chart.yaml` for the image:

  * The chart name is the image name: `hello-chart`
  * The chart version is the image tag: `0.1.0`



Helm returns output similar to the following example:
    
    
    Login Succeeded
    Pushed: us-west1-docker.pkg.dev/my-project/quickstart-helm-repo/hello-chart:0.1.0
    Digest: sha256:67a72...
    

Run the following command to verify that the chart is now stored in the repository:
    
    
    gcloud artifacts docker images list us-west1-docker.pkg.dev/PROJECT/quickstart-helm-repo
    

The command output looks similar to the following example:
    
    
    Listing items under project my-project, location us-west1, repository quickstart-helm-repo.
    
    IMAGE: us-west1-docker.pkg.dev/my-project/quickstart-helm-repo/hello-chart
    DIGEST: sha256:67a72...
    CREATE_TIME: 2021-11-08T22:59:57
    UPDATE_TIME: 2021-11-08T22:59:57
    

You can now deploy a release using the chart stored in Artifact Registry.

## Deploy the chart

In Helm, a deployed instance of your application is called a _release_. After you have added your repository to the Helm configuration, you can deploy a release of your chart.

  1. Create a cluster named `chart-cluster` for your deployment with the command:
         
         gcloud container clusters create --zone us-west1-a chart-cluster
         

When the cluster is created, the command returns a summary similar to the following example:
         
         kubeconfig entry generated for chart-cluster.
         NAME: chart-cluster
         LOCATION: us-west1-a
         MASTER_VERSION: 1.20.10-gke.1600
         MASTER_IP: 34.66.36.211
         MACHINE_TYPE: e2-medium
         NODE_VERSION: 1.20.10-gke.1600
         NUM_NODES: 3
         STATUS: RUNNING
         

  2. Get the cluster credentials so that `kubectl` can access the cluster:
         
         gcloud container clusters get-credentials --zone us-west1-a chart-cluster
         

  3. Run the following command to deploy a release of `hello-chart` using the locally extracted chart files:
         
         helm install hello-chart oci://us-west1-docker.pkg.dev/PROJECT/quickstart-helm-repo/hello-chart --version 0.1.0
         

The command returns a summary of the deployment:
         
         NAME: hello-chart
         LAST DEPLOYED: Mon Nov  8 23:15:13 2021
         NAMESPACE: default
         STATUS: deployed
         REVISION: 1
         




You have successfully deployed a release using the chart that you created and pushed to Artifact Registry.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the repository you created with the following command:
         
         gcloud artifacts repositories delete quickstart-helm-repo --location=us-west1
         

  2. Delete the cluster you created:
         
         gcloud container clusters delete --zone=us-west1-a chart-cluster
         




## What's next

  * [Learn more about working with charts](https://docs.cloud.google.com/artifact-registry/docs/helm).
  * [Learn more about Helm](https://helm.sh/docs/).
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore our [research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
