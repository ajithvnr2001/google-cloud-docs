---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/store-apt/
title: Quickstart: Store Apt packages in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:17.594377+00:00
---

# Quickstart: Store Apt packages in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/store-apt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Apt packages in Artifact Registry

This quickstart shows you how to set up a private Artifact Registry Apt repository, add a Debian package to the repository, and install the package on a Compute Engine VM running a Debian-based operating system.

To learn more about managing Debian packages, see [Working with Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian).

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

  5. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/os-packages/debian/store-apt)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/os-packages/debian/store-apt)




## Required roles

To get the permissions that you need to create and manage Artifact Registry Apt package repositories, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * Create a virtual machine (VM) in Compute Engine: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Launch Cloud Shell

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The gcloud CLI provides the primary command-line interface for Google Cloud.

Launch Cloud Shell:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. In the Google Cloud console, click **Activate Cloud Shell** ![Activate Cloud Shell button](https://docs.cloud.google.com/static/artifact-registry/docs/images/cloud-shell.png).




A Cloud Shell session opens inside a frame lower on the console. You'll use this shell to run the `gcloud` commands to create a VM and a repository. 

## Create a repository

Create the repository for your artifacts.

  1. Create the repository:

###  Console 

     1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

     2. Click **Create Repository**.

     3. Specify `quickstart-apt-repo` as the repository name.

     4. Select **Apt** as the format.

     5. Under **Location Type** , select **Region** and then choose the location `us-west1`.

     6. Click **Create**.

The repository is added to the repository list.

###  gcloud 

     1. In Cloud Shell, run the following command to create a new Apt repository in the current project named `quickstart-apt-repo` in the location `us-west1`.
            
            gcloud artifacts repositories create quickstart-apt-repo \
                --repository-format=apt \
                --location=us-west1 \
                --description="Apt repository"
            

     2. Run the following command to verify that your repository was created:
            
            gcloud artifacts repositories list
            




You can now add a package to the repository. Cloud Shell uses a Google-built Ubuntu image, not Debian. To manage Debian packages in the repository, you will use a VM that uses a Debian OS image.

## Create a VM

Create a new Compute Engine VM where you'll install the sample package.

In Cloud Shell, run the following command to create a VM instance named `quickstart-apt-vm`:
    
    
    gcloud compute instances create quickstart-apt-vm \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --scopes=cloud-platform
    

By default, the VM does not have the required [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) for working with the repository. The `--scopes` flag sets the access scope for the VM to `cloud-platform`.

**Note:** The VM you created in this quickstart uses a Debian OS image built by Google, which is pre-configured with some settings for accessing Artifact Registry repositories. If you want to configure a Compute Engine VM that uses a Google-built Ubuntu image, a VM that uses an OS image that isn't built by Google, or a VM outside of Google Cloud, there are additional configuration steps. For details, see the full [VM configuration instructions](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

  1. Go to the VM instances page.

[Open the VM instances page](https://console.cloud.google.com/compute/instances)

  2. In the row with your VM, click **SSH**. A new window opens with a terminal session on the VM.




## Add a package to the repository

You can upload a package to a repository using the Google Cloud CLI, or you can import a package that is stored in Cloud Storage. If you build packages using Cloud Build, the build can store the packages in Cloud Storage for you to import. 

For this quickstart, you upload a sample file using the `gcloud artifacts apt upload` command.

  1. Run `gcloud init` to initialize the Google Cloud CLI on your VM.

  2. Update Apt:
         
         sudo apt update
         

  3. Download the curl package with the command:
         
         apt download curl
         

Apt downloads the latest version of the package that is available from your configured Apt repositories.
         
         Get:1 file:/etc/apt/mirrors/debian.list Mirrorlist [30 B]
         Get:2 https://deb.debian.org/debian bookworm/main amd64 curl amd64 7.88.1-10+deb12u14 [316 kB]
         Fetched 316 kB in 0s (3078 kB/s)
         

Run `ls` to get the filename of the curl package. The filename is similar to `curl_7.88.1-10+deb12u14_amd64.deb`.

  4. To simplify `gcloud` commands, set the default repository to `quickstart-apt-repo` and the default location to `us-west1`. After the values are set, you don't need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the command:
         
         gcloud config set artifacts/repository quickstart-apt-repo
         

To set the location, run the command:
         
         gcloud config set artifacts/location us-west1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.

  5. Run the `gcloud artifacts apt upload` to upload the package to the repository:
         
         gcloud artifacts apt upload quickstart-apt-repo \
             --source=FILE_NAME
         

Replace `FILE_NAME` with the path to the curl package.




## View the package in the repository

Verify that your package was added to the repository.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the **quickstart-apt-repo** repository.

The **Packages** page lists the packages in the repository.




###  gcloud 

To list the packages in the `quickstart-apt-repo` repository, run the command:
    
    
     gcloud artifacts packages list
    

To view versions for a package in `quickstart-apt-repo`, run the command:
    
    
    gcloud artifacts versions list --package=apt-dpkg-ref
    

## Configure the package manager

To install a package on the VM, add the repository you created to the Apt configuration file that defines package repositories.

  1. Install the Apt credential helper on the VM to enable Apt to perform authentication:
         
         sudo apt install apt-transport-artifact-registry
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb ar+https://us-west1-apt.pkg.dev/projects/PROJECT quickstart-apt-repo main' | sudo tee -a  /etc/apt/sources.list.d/artifact-registry.list
         

Replace PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




## Install the package

Install the package that you added to the repository.

  1. Update the list of available packages:
         
         sudo apt update
         

  2. Install the package from your repository.
         
         sudo apt install curl/quickstart-apt-repo
         

The returned installation information looks like the following example:
         
         Reading package lists... Done
         Building dependency tree... Done
         Reading state information... Done
         Selected version '7.88.1-10+deb12u14' (quickstart-apt-repo:quickstart-apt-repo, Debian:12.12/oldstable [amd64]) for 'curl'
         The following additional packages will be installed:
           libcurl3-gnutls libcurl4
         The following packages will be upgraded:
           curl libcurl3-gnutls libcurl4
         3 upgraded, 0 newly installed, 0 to remove and 77 not upgraded.
         Need to get 1093 kB of archives.
         After this operation, 0 B of additional disk space will be used.
         Do you want to continue? [Y/n] y
         Get:1 file:/etc/apt/mirrors/debian.list Mirrorlist [30 B]
         Get:2 https://deb.debian.org/debian bookworm/main amd64 libcurl4 amd64 7.88.1-10+deb12u14 [392 kB]
         Get:3 https://deb.debian.org/debian bookworm/main amd64 libcurl3-gnutls amd64 7.88.1-10+deb12u14 [386 kB]
         Get:4 ar+https://us-west1-apt.pkg.dev/projects/PROJECT quickstart-apt-repo/main amd64 curl amd64 7.88.1-10+deb12u14 [316 kB]
         Fetched 1093 kB in 1s (947 kB/s)
         Reading changelogs... Done
         (Reading database ... 72080 files and directories currently installed.)
         Preparing to unpack .../curl_7.88.1-10+deb12u14_amd64.deb ...
         Unpacking curl (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
         Preparing to unpack .../libcurl4_7.88.1-10+deb12u14_amd64.deb ...
         Unpacking libcurl4:amd64 (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
         Preparing to unpack .../libcurl3-gnutls_7.88.1-10+deb12u14_amd64.deb ...
         Unpacking libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) over (7.88.1-10+deb12u12) ...
         Setting up libcurl3-gnutls:amd64 (7.88.1-10+deb12u14) ...
         Setting up libcurl4:amd64 (7.88.1-10+deb12u14) ...
         Setting up curl (7.88.1-10+deb12u14) ...
         Processing triggers for man-db (2.11.2-2) ...
         Processing triggers for libc-bin (2.36-9+deb12u10) ...
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any packages you want to keep are available in another location.

To delete the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the **quickstart-apt-repo** repository.

  3. Click **Delete**.




###  gcloud 

  1. To delete the `quickstart-apt-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-apt-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




To delete the VM you created, run the following command:
    
    
    gcloud compute instances delete quickstart-apt-vm
    

## What's next

  * [Learn about working with Deb packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian).
  * Read about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
