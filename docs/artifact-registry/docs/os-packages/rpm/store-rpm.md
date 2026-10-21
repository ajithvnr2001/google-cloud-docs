---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/store-rpm/
title: Quickstart: Store RPM packages in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:17.930746+00:00
---

# Quickstart: Store RPM packages in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/store-rpm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store RPM packages in Artifact Registry

This quickstart shows you how to set up a private Artifact Registry Yum repository, add an RPM package to the repository, and install the package on a Compute Engine VM running the CentOS 7 operating system. To learn how to configure Yum repositories that use DNF, see [Configuring VMs to install RPM packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure).

To learn more about managing RPM packages, see [Working with RPM packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm).

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

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/os-packages/rpm/store-rpm)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/os-packages/rpm/store-rpm)




## Required roles

To get the permissions that you need to create and manage Artifact Registry Yum package repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

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

     3. Specify `quickstart-yum-repo` as the repository name.

     4. Select **Yum** as the format.

     5. Under **Location Type** , select **Region** and then choose the location `us-west1`.

     6. Click **Create**.

The repository is added to the repository list.

###  gcloud 

     1. In Cloud Shell, run the following command to create a new Yum repository in the current project named `quickstart-yum-repo` in the location `us-west1`.
            
            gcloud artifacts repositories create quickstart-yum-repo \
                --repository-format=yum \
                --location=us-west1 \
                --description="Yum repository"
            

     2. Run the following command to verify that your repository was created:
            
            gcloud artifacts repositories list
            




You can now add a package to the repository.

## Add a package to the repository

You can upload a package to a repository using the Google Cloud CLI, or you can import a package that is stored in Cloud Storage. If you build packages using Cloud Build, the build can store the packages in Cloud Storage for you to import. 

For this quickstart, you upload a sample file using the `gcloud artifacts yum upload` command.

  1. In Cloud Shell, download the nano text editor with the command:
         
         sudo yum install --downloaddir=. --downloadonly nano
         

Yum downloads the latest version of the package that is available from your configured CentOS repositories.
         
         Loaded plugins: fastestmirror
         Loading mirror speeds from cached hostfile
          * base: mirror.dal.nexril.net
          * epel: ord.mirror.rackspace.com
          * extras: centos.mirror.lstn.net
          * updates: ftpmirror.your.org
         Resolving Dependencies
         --> Running transaction check
         ---> Package nano.x86_64 0:2.3.1-10.el7 will be installed
         --> Finished Dependency Resolution
         
         Dependencies Resolved
         
         ================================================================================
          Package        Arch             Version                   Repository      Size
         ================================================================================
         Installing:
          nano           x86_64           2.3.1-10.el7              base           440 k
         
         Transaction Summary
         ================================================================================
         Install  1 Package
         
         Total download size: 440 k
         Installed size: 1.6 M
         Background downloading packages, then exiting:
         nano-2.3.1-10.el7.x86_64.rpm                               | 440 kB   00:00
         exiting because "Download Only" specified
         

Run `ls` to get the filename of package. The filename is similar to `nano-2.3.1-10.el7.x86_64.rpm`.

  2. To simplify `gcloud` commands, set the default repository to `quickstart-yum-repo` and the default location to `us-west1`. After the values are set, you do not need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the command:
         
         gcloud config set artifacts/repository quickstart-yum-repo
         

To set the location, run the command:
         
         gcloud config set artifacts/location us-west1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.

  3. Run the `gcloud artifacts yum upload` to upload the package to the repository:
         
         gcloud artifacts yum upload quickstart-yum-repo \
             --source=FILE_NAME
         

Replace `FILE_NAME` with the path to the nano package.




## View the package in the repository

Verify that your package was added to the repository.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the **quickstart-yum-repo** repository.

The **Packages** page lists the packages in the repository.




###  gcloud 

To list the packages in the `quickstart-yum-repo` repository, run the command:
    
    
     gcloud artifacts packages list
    

To view versions for a package in `quickstart-yum-repo`, run the command:
    
    
    gcloud artifacts versions list --package=nano
    

## Create a VM

Create a new Compute Engine VM where you'll install the sample package.

In Cloud Shell, run the following command to create a VM instance named `quickstart-yum-vm`.
    
    
    gcloud compute instances create quickstart-yum-vm \
        --image-family=centos-7 \
        --image-project=centos-cloud \
        --scopes=cloud-platform
    

By default, the VM does not have the required [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) for working with the repository. The `--scopes` flag sets the access scope for the VM to `cloud-platform`.

## Configure the package manager

To install a package on the VM, add the repository you created to the Yum file that defines package repositories.

**Note:** The VM you created in this quickstart uses an OS image built by Google, which is pre-configured with some settings for accessing Artifact Registry repositories. If you want to configure a VM that uses an OS image that isn't built by Google or a VM outside of Google Cloud, see the full [VM configuration instructions](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure).

  1. Go to the VM instances page.

[Open the VM instances page](https://console.cloud.google.com/compute/instances)

  2. In the row with your VM, click **SSH**. A new window opens with a terminal session on the VM.

  3. Update Yum:
         
         sudo yum makecache
         

  4. Install the Yum credential helper on the VM to enable Yum to perform authentication, using the following command:
         
         sudo yum install yum-plugin-artifact-registry
         

  5. Configure your VM to access Artifact Registry} packages using the following command:
         
         sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOF
         [yum-quickstart]
         name=My Repository
         baseurl=https://us-west1-yum.pkg.dev/projects/PROJECT/quickstart-yum-repo
         enabled=1
         repo_gpgcheck=0
         gpgcheck=0
         EOF
         

Replace PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




## Install the package

Install the package that you added to the repository.

  1. Update the list of available packages:
         
         sudo yum makecache
         

  2. Install the package in your repository.
         
         sudo yum --enablerepo=yum-quickstart install nano
         

Enter `y` when prompted.

The returned installation information looks like the following example:
         
         Loaded plugins: fastestmirror
         Loading mirror speeds from cached hostfile
          * base: mirrors.cmich.edu
          * epel: ord.mirror.rackspace.com
          * extras: mirror.team-cymru.com
          * updates: mirror.us-midwest-1.nexcess.net
         quickstart-yum-repo                                      | 1.3 kB     00:00
         Resolving Dependencies
         --> Running transaction check
         ---> Package nano.x86_64 0:2.3.1-10.el7 will be installed
         --> Finished Dependency Resolution
         
         Dependencies Resolved
         
         ================================================================================
          Package        Arch             Version                   Repository      Size
         ================================================================================
         Installing:
          nano           x86_64           2.3.1-10.el7              base           440 k
         
         Transaction Summary
         ================================================================================
         Install  1 Package
         
         Total size: 440 k
         Installed size: 1.6 M
         Is this ok [y/d/N]: y
         Downloading packages:
         Running transaction check
         Running transaction test
         Transaction test succeeded
         Running transaction
           Installing : nano-2.3.1-10.el7.x86_64                                     1/1
           Verifying  : nano-2.3.1-10.el7.x86_64                                     1/1
         
         Installed:
           nano.x86_64 0:2.3.1-10.el7
         
         Complete!
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any packages you want to keep are available in another location.

To delete the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the **quickstart-yum-repo** repository.

  3. Click **Delete**.




###  gcloud 

  1. To delete the `quickstart-yum-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-yum-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




To delete the VM you created, run the following command:
    
    
    gcloud compute instances delete quickstart-yum-vm
    

## What's next

  * [Learn about working with RPM packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm).
  * Read about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
