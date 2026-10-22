---
url: https://docs.cloud.google.com/artifact-registry/docs/conda/store-conda/
title: Quickstart: Store Conda packages in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:48.749340+00:00
---

# Quickstart: Store Conda packages in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/conda/store-conda/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Conda packages in Artifact Registry

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This quickstart shows you how to set up a private Artifact Registry Conda repository and then upload a package to that repository.

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

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/conda/store-conda)

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

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/conda/store-conda)

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

  10. To use the Conda CLI within your Google Cloud environment, install one of the following Conda package managers: 
     * [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
     * [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
     * [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
     * [Miniforge](https://conda-forge.org/download/)



## Launch Cloud Shell

In this quickstart, you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Conda. The gcloud CLI provides the primary command-line interface for Google Cloud.

Launch Cloud Shell:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. On the Google Cloud console toolbar, click **Activate Cloud Shell**.




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

## Configure authentication

A Conda _channel_ is the address to a location where one or more Conda packages are stored. Before you can install packages in your Conda environment, you must add the channel for that package to your Conda configuration file.

To allow the Conda CLI to call Artifact Registry directly, you must authenticate your Conda channel in Google Cloud by doing the following:

  1. In the gcloud CLI, run the following command to store the identity of an `oauth` token in a TOKEN variable:
         
         export TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
         

  2. Add your Conda repository as a channel in your Conda configuration file:

### Conda
         
         conda config --add channels \
         https://$TOKEN@LOCATION-conda.pkg.dev/PROJECT/REPOSITORY
         

### Miniforge
         
         conda config --add channels \
         https://$TOKEN@LOCATION-conda.pkg.dev/PROJECT/REPOSITORY
         

### Mamba
         
         mamba config --add channels \
         https://$TOKEN@LOCATION-conda.pkg.dev/PROJECT/REPOSITORY
         

### Micromamba
         
         micromamba config --add channels \
         https://$TOKEN@LOCATION-conda.pkg.dev/PROJECT/REPOSITORY
         

**Note:** The `add` command adds your channel to the beginning of the channel list in your configuration file. To add the channel to the end of the list, use `--append` instead.

Where:

     * TOKEN stores the value of the `oauth` token generated by running `oauth2accesstoken:$(gcloud auth print-access-token)`.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     * PROJECT is the ID of the project containing the repository.
     * REPOSITORY is the ID of the repository.



**Refresh an expired`oauth` token**

An `oauth` token expires after one hour. To re-authenticate your channel with a new token, do the following:

  1. Remove your channel from your configuration file:

### Conda
         
         conda config --remove channels CHANNEL_NAME
         

### Miniforge
         
         conda config --remove channels CHANNEL_NAME
         

### Mamba
         
         mamba config --remove channels CHANNEL_NAME
         

### Micromamba
         
         micromamba config --remove channels CHANNEL_NAME
         

  2. Follow the previous step that described creating a new `oauth` token.

  3. Add your Conda repository back to your Conda configuration file, using your new token value.




## Create a repository

Create the repository for your package.

  1. Run the following command to create a new Conda repository in the current project named `quickstart-conda-repo` in the location `us-west1`.
         
         gcloud artifacts repositories create quickstart-conda-repo \
             --repository-format=conda \
             --location=us-west1 \
             --description="Conda repository"
         

  2. Run the following command to verify that your repository was created:
         
         gcloud artifacts repositories list
         

  3. To simplify `gcloud` commands, set the default repository to `quickstart-conda-repo` and the default location to `us-west1`. After the values are set, you don't need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the following command:
         
         gcloud config set artifacts/repository quickstart-conda-repo
         

To set the location, run the following command:
         
         gcloud config set artifacts/location us-west1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.




## Upload the package to the repository

To upload a package to your repository, run the following command:
    
    
    gcloud artifacts files upload \
        --source=PACKAGE_NAME \
        --repository=REPO_NAME\
        --project=PROJECT \
        --location=LOCATION
    

Where:

  * REPO_NAME is the ID of the repository.
  * PROJECT is the ID of the project containing the repository.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.



To upload multiple packages at one time:
    
    
    gcloud artifacts files upload \
        --source-directory="DIRECTORY" \
        --repository="REPO_NAME"\
        --project="PROJECT" \
        --location="LOCATION"
    

Where:

  * DIRECTORY is the address of a local folder containing your Conda packages.



## View the package in the repository

To verify that your package was added, list the packages in the `quickstart-conda-repo` repository.

Run the following command:
    
    
    gcloud artifacts packages list --repository=quickstart-conda-repo
    

To view versions for a package, run the following command:
    
    
    gcloud artifacts versions list --package=PACKAGE_NAME
    

To view the files for a package version, run the following command:
    
    
    gcloud artifacts files list --package=PACKAGE_NAME --version=VERSION
    

## Install the package

To install the package that you just added to your Artifact Registry repository, run the following command:

### Conda
    
    
    conda install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Miniforge
    
    
    conda install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Mamba
    
    
    mamba install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Micromamba
    
    
    micromamba install -n ENVIRONMENT_NAME PACKAGE_NAME
    

Where:

  * ENVIRONMENT_NAME is the name of your Conda environment.
  * PACKAGE_NAME is the name of the package to install in your repository.



## Troubleshooting

See [Troubleshooting for Conda packages](https://docs.cloud.google.com/artifact-registry/docs/conda/troubleshooting) for more information.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any packages you want to keep are available in another location.

  1. To delete the `quickstart-conda-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-conda-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




## What's next

  * [Learn more about configuring authentication](https://docs.cloud.google.com/artifact-registry/docs/conda/authentication).
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories).
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/conda/manage-packages).
  * Read our resources about [DevOps](https://docs.cloud.google.com/devops) and explore our [research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
