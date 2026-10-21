---
url: https://docs.cloud.google.com/secure-source-manager/docs/use-git/
title: Use Git source code management \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:51.467976+00:00
---

# Use Git source code management  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/use-git/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Use Git source code management Stay organized with collections  Save and categorize content based on your preferences. 

Secure Source Manager supports all [Git SCM](https://git-scm.com/) client commands and has built in pull requests and issue tracking. Both HTTPS and [SSH authentication](https://docs.cloud.google.com/secure-source-manager/docs/ssh-keys) are supported.

## Required roles

To get the permissions that you need to use Git to interact with a Secure Source Manager repository, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * To clone a repository: [Secure Source Manager Repo Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`) on the repository 
  * To push to a repository: [Secure Source Manager Repo Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the repository 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Install Git and Google Cloud CLI

  1. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

  2. If you are prompted to **Choose a credential helper** by the Git installer, select **None (Do not use a credential helper)**.

  3. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  4. The gcloud CLI version `395.0.0` or later is required to use Git with HTTPS. To check your gcloud CLI version run the following command:
         
         gcloud --version
         

  5. To update the gcloud CLI run the following command.
         
         gcloud components update
         

  6. After updating, run `gcloud init` to [initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).

See the gcloud CLI documentation on [updating components](https://docs.cloud.google.com/sdk/docs/components#updating_components) for more information.




## Set up your credentials

If you authenticate to Secure Source Manager using a third-party identity provider and Workforce Identity Federation, you don't need to complete this section—instead, you must create a workforce identity pool login configuration.

Add the Secure Source Manager authentication helper to your global Git config by running the following command:

###  Linux 
    
    
    git config --global credential.'https://*.*.sourcemanager.dev'.helper gcloud.sh
    

Earlier versions of Git might not support wildcards. To add the authentication helper without wildcards, run the following command:
    
    
    git config --global credential.'https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev'.helper gcloud.sh
    

Replace the following:

  * `INSTANCE_ID` with the name of your Secure Source Manager instance.
  * `PROJECT_NUMBER` with your project number. For help finding your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `LOCATION` with the instance's region. For more information on regions, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).



###  Windows
    
    
    git config --global credential.https://*.*.sourcemanager.dev.helper gcloud.cmd
    

Earlier versions of Git might not support wildcards. To add the authentication helper without wildcards, run the following command:
    
    
    git config --global credential.https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev.helper gcloud.cmd
    

Replace the following:

  * `INSTANCE_ID` with the name of your Secure Source Manager instance.
  * `PROJECT_NUMBER` with your project number. For help finding your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `LOCATION` with the instance's region. For more information on regions, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).



The authentication helper uses the gcloud CLI to fetch your Google Cloud credentials when using Git commands with Secure Source Manager.

To re-authenticate after the initial credential setup, run the following gcloud CLI command:
    
    
    gcloud auth login
    

**Note:** some systems might try to store credentials fetched by authentication helpers by adding a line to your Git config similar to `*credential*.helper=store`. Since the Secure Source Manager credentials are short lived, this will cause authentication errors. To fix this issue, remove the line from your global, system, or local repository Git config file.

## Authenticate from a Compute Engine VM using a service account

You can authenticate from a Compute Engine virtual machine (VM) by using an attached service account.

### Configure the VM and service account

If you use the Compute Engine default service account, create your VM with the required OAuth scopes:
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --scopes=openid,https://www.googleapis.com/auth/userinfo.profile,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * `VM_NAME`: the name for your VM.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the zone for your VM.



If you use a custom service account, create the service account and then create the VM.

  1. Create a service account:
         
         gcloud iam service-accounts create SA_NAME --project=PROJECT_ID
         

Replace `SA_NAME` with a name for the service account.

  2. Grant permission to use the service account. To create a VM with a service account, you need the [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) on the service account. Grant this role to the principal creating the VM:
         
         gcloud iam service-accounts add-iam-policy-binding SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --member="user:USER_EMAIL" \
             --role="roles/iam.serviceAccountUser"
         

Replace `USER_EMAIL` with the email of the user creating the VM.

  3. Create the VM:
         
         gcloud compute instances create VM_NAME \
             --project=PROJECT_ID \
             --zone=ZONE \
             --scopes=openid,https://www.googleapis.com/auth/userinfo.profile,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform \
             --service-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com
         




### Grant IAM roles to the service account

Grant the service account access to the Secure Source Manager instance and repository:

  1. Grant instance access:
         
         SA_EMAIL=$(gcloud compute instances describe VM_NAME --project=PROJECT_ID --zone=ZONE --format="get(serviceAccounts[0].email)")
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:$SA_EMAIL" \
             --role=roles/securesourcemanager.instanceAccessor
         

  2. Grant repository read access.

To grant read access to a specific repository, run the following command:
         
         gcloud ssm repos add-iam-policy-binding REPOSITORY_ID \
             --instance=INSTANCE_ID \
             --location=LOCATION \
             --member="serviceAccount:$SA_EMAIL" \
             --role=roles/securesourcemanager.repoReader
         

Replace the following:

     * `REPOSITORY_ID`: The repository ID.
     * `INSTANCE_ID`: The Secure Source Manager instance ID.
     * `LOCATION`: The region of the Secure Source Manager instance.

To grant write access, use the role `roles/securesourcemanager.repoWriter`.

Granting access at the repository level is recommended to follow the principle of least privilege. If you need to grant access to all repositories in a project, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).




IAM permissions can take a few minutes to propagate.

### Configure Git on the VM

  1. Connect to the VM using SSH:
         
         gcloud compute ssh VM_NAME --project=PROJECT_ID --zone=ZONE
         

  2. On the VM, install Git:
         
         sudo apt-get install git
         

  3. On the VM, configure the Git credential helper as described in Set up your credentials. For example, on Linux:
         
         git config --global credential.'https://*.*.sourcemanager.dev'.helper gcloud.sh
         




After you configure the credential helper, Git uses the Application Default Credentials from the VM's service account to authenticate to Secure Source Manager. You can now clone a repository. You must use the HTTPS repository URL to authenticate with Application Default Credentials.

## Create a workforce identity pool login configuration

You don't need to complete this section unless you're using Workforce Identity Federation to authenticate to Secure Source Manager with a third-party identity provider.

To authenticate with your workforce identity pool credentials to your Secure Source Manager instance using gcloud CLI commands or Git commands, you must create a login configuration with your workforce identity pool.

To create a workforce identity pool login configuration, follow the instructions in [Obtain short-lived tokens for Workforce Identity Federation](https://docs.cloud.google.com/sdk/docs/authenticate#federated-user-identities) to create a browser-based sign-in with the gcloud CLI.

After you have authenticated, you can use Git commands to interact with your Secure Source Manager instance. You must re-authenticate when the **session duration** for your workforce identity pool expires.

## Clone a repository

Clone a repository by running the following command:
    
    
    git clone REPOSITORY_URL
    

Where `REPOSITORY_URL` is the HTTPS or SSH URL displayed at the top of the repository page you want to clone.

## Clone with Developer Connect

You can clone repositories using the Developer Connect Git proxy if you have linked your Secure Source Manager repository in Developer Connect. Cloning with Developer Connect uses IAM to authenticate and authorize repository access.

### Before you begin

  1. Follow the instructions to [create a connection to a Secure Source Manager repository](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager) in Developer Connect.
  2. Ensure Git proxy is enabled on your Developer Connect connection. See [Configure and use Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy) for instructions on enabling Git proxy.
  3. Grant principals that need to clone using the proxy URI the `roles/developerconnect.gitProxyReader` role on the `GitRepositoryLink` resource in Developer Connect. See [Developer Connect access control with IAM](https://docs.cloud.google.com/developer-connect/docs/access-control) for instructions on granting roles.



### Set up credentials for Developer Connect

Add the Developer Connect authentication helper to your global Git config by running the following command:

###  Linux 
    
    
    git config --global credential.'https://*.developerconnect.dev'.helper gcloud.sh
    

###  Windows 
    
    
    git config --global credential.https://*.developerconnect.dev.helper gcloud.cmd
    

### Clone using the proxy URI

To clone a repository using the Developer Connect proxy URI, run the following command:
    
    
    git clone https://REGION-git.developerconnect.dev/v1/projects/PROJECT_ID/locations/REGION/connections/CONNECTION_ID/gitRepositoryLinks/LINK_ID
    

Replace the following:

  * `REGION`: The region of your Developer Connect resources.
  * `PROJECT_ID`: The Project ID of your Developer Connect resources.
  * `CONNECTION_ID`: The ID of your Developer Connect connection.
  * `LINK_ID`: The ID of your Developer Connect `GitRepositoryLink` resource.



For instructions on viewing your `GitRepositoryLink` resource details, see [gcloud developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links). You can use `list` or `describe` subcommands to view link details.

**Note:** Pushing to Secure Source Manager repositories using the Developer Connect Git proxy URI is not supported. This is to prevent writes using the Developer Connect service account identity. To push changes, use HTTPS or SSH instead.

## Push an existing repository to Secure Source Manager

You must [create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository) to act as a remote before you can push to it.

To push your existing Git repository to an empty Secure Source Manager repository you need to add the Secure Source Manager repository as a remote and push to it.

  1. To set the Secure Source Manager repository as a remote run the following command:
         
         git remote add origin REPOSITORY_URL
         

Where `REPOSITORY_URL` is the HTTPS or SSH URL displayed at the top of the repository page.

  2. To push to the repository run the following command:
         
         git push -u origin main
         




For more information on Git source code management, read the [Git documentation](https://git-scm.com/doc).

## What's next

  * Learn more about [Git source code management](https://git-scm.com/)
  * [List and view repositories](https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
