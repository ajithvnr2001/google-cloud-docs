---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment/
title: Set up Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:08.902572+00:00
---

# Set up Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Set up Cluster Toolkit Stay organized with collections  Save and categorize content based on your preferences. 

Cluster Toolkit is an open-source tool that simplifies deploying high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads on Google Cloud. Cluster Toolkit uses customizable blueprints to provision infrastructure that aligns with Google Cloud best practices, making it extensible for a broad range of use cases.

This guide helps you prepare your Google Cloud environment and install Cluster Toolkit for efficient deployment and management of your cluster environments.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, Filestore, Cloud Storage, Service Usage, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,file.googleapis.com,storage.googleapis.com,serviceusage.googleapis.com,cloudresourcemanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, Filestore, Cloud Storage, Service Usage, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,file.googleapis.com,storage.googleapis.com,serviceusage.googleapis.com,cloudresourcemanager.googleapis.com)




## Overview

To set up Cluster Toolkit, you need to complete the following steps:

  1. Set up your CLI
  2. Set up your project
  3. Install Cluster Toolkit



## Set up your CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

## Set up your project

Before you can deploy your cluster, you need to configure your Google Cloud project. The following sections show you how to set a default project, enable the required service accounts and roles, grant credentials for deployment, and enable OS Login for Compute Engine instance access.

### Set a default project

Set a default project:

Replace `PROJECT_ID` with your project ID.
    
    
    gcloud config set project PROJECT_ID

### Ensure that the default Compute Engine service account is enabled

Cluster Toolkit requires that the default Compute Engine service account is enabled in your project and the Compute Instance Admin (v1) role (`roles/compute.instanceAdmin.v1`) and the Service Account User (`roles/iam.serviceAccountUser`) role are granted to the service account.

However, if you've disabled the default Compute Engine service account and lack the required roles in your project, complete the following steps to enable these settings:

  1. Enable the default Compute Engine service account.
         
         gcloud iam service-accounts enable \
            --project PROJECT_ID \
            PROJECT_NUMBER-compute@developer.gserviceaccount.com
         

  2. Grant the Compute Instance Admin (v1) role (`roles/compute.instanceAdmin.v1`) and the Service Account User (`roles/iam.serviceAccountUser`) to the service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/compute.instanceAdmin.v1
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/iam.serviceAccountUser
         




Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: the automatically generated unique identifier for your project

For more information, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




### Grant user access credentials to Terraform

**Note:** If you are using Cloud Shell, you can skip this step.

Generate cloud credentials associated with your Google Cloud account:
    
    
    gcloud auth application-default login

This grants the Application Default Credentials (ADC) to Terraform.

### Enable OS Login at the project-level

To be able to connect to a compute instance in your cluster by using `ssh`, you must enable OS Login. If OS Login is already enabled at the organization level, you don't need to enable it on your project.
    
    
    gcloud compute project-info add-metadata \
         --metadata enable-oslogin=TRUE

## Install Cluster Toolkit

To install Cluster Toolkit, download the prebuilt binary bundle from the [releases](https://github.com/GoogleCloudPlatform/cluster-toolkit/releases) page. These bundles contain the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster), the [`examples`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples) directory, and the [`community/examples`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/examples) directory.

### Supported platforms

The prebuilt bundles support the following execution environments:

Platform | Support Status | Notes  
---|---|---  
Linux | Yes | Pre-compiled on Debian Bullseye.  
Google Cloud Shell | Yes | Built-in support by using the Linux binary.  
macOS | Yes | Built-in support by using the Mac binary.  
Windows | No | You must build from source.  
  
### Install the prebuilt bundle

To install Cluster Toolkit, you download and extract the prebuilt binary bundle for your platform. Both ZIP and TAR (`.tgz`) archives are available.

  1. Go to the [Cluster Toolkit releases page](https://github.com/GoogleCloudPlatform/cluster-toolkit/releases) on GitHub.

  2. Download the bundle for your platform and architecture. The following bundles are available:

     * `gcluster_bundle_linux_amd64.zip` or `gcluster_bundle_linux_amd64.tgz`
     * `gcluster_bundle_linux_arm64.zip` or `gcluster_bundle_linux_arm64.tgz`
     * `gcluster_bundle_mac_amd64.zip` or `gcluster_bundle_mac_amd64.tgz`
     * `gcluster_bundle_mac_arm64.zip` or `gcluster_bundle_mac_arm64.tgz`

Alternatively, if you are using Cloud Shell or a terminal, download the bundle directly by using `curl`: 
    
    curl -L -O https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/VERSION/BUNDLE_FILENAME

Replace `VERSION` with the release version tag (for example, `v1.89.0`), and replace `BUNDLE_FILENAME` with the filename of the bundle for your platform.

  3. Perform the installation steps for your platform:

###  Linux 

     1. In your terminal, extract the bundle files to a new directory:

        * If you downloaded a ZIP bundle, extract the files by using the `unzip` command:
              
              unzip BUNDLE_FILENAME -d cluster-toolkit

        * If you downloaded a TAR bundle, extract the files by using the `tar` command:
              
              mkdir -p cluster-toolkit
              tar -xzf BUNDLE_FILENAME -C cluster-toolkit

Replace `BUNDLE_FILENAME` with the name of the bundle you downloaded.

     2. Go to the new directory:
            
            cd cluster-toolkit

###  macOS 

     1. In your terminal, extract the bundle files to a new directory:

        * If you downloaded a ZIP bundle, extract the files by using the `unzip` command:
              
              unzip BUNDLE_FILENAME -d cluster-toolkit

        * If you downloaded a TAR bundle, extract the files by using the `tar` command:
              
              mkdir -p cluster-toolkit
              tar -xzf BUNDLE_FILENAME -C cluster-toolkit

Replace `BUNDLE_FILENAME` with the name of the bundle you downloaded.

     2. Go to the new directory:
            
            cd cluster-toolkit

  4. Verify the installation:
         
         ./gcluster --version
         ./gcluster --help
         




## Build from source

If you use a Windows environment, you must build the Cluster Toolkit binary from source.

  1. Clone the Cluster Toolkit GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/cluster-toolkit.git
         

  2. Go to the main working directory:
         
         cd cluster-toolkit/
         

  3. Build the Cluster Toolkit binary:
         
         make
         

  4. Verify that the build was successful:
         
         ./gcluster --version
         




## What's next

  * [Cluster blueprint overview](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint)
  * [Best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices)
  * [Deploy an HPC cluster with Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
