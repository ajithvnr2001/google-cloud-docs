---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository/
title: Quickstart: Create and clone a repository \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:42.791392+00:00
---

# Quickstart: Create and clone a repository  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and clone a repository

Create a repository in Secure Source Manager and clone it to your local machine.

## Before you begin

  1. Create or request access to a Secure Source Manager instance. For more information, see [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to create a repository, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Repository Creator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceRepositoryCreator) (`roles/securesourcemanager.instanceRepositoryCreator`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Creator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoCreator) (`roles/securesourcemanager.repoCreator`) on the instance project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The [Secure Source Manager Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.admin) (`roles/securesourcemanager.admin`) or [IAM basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of Owner (`roles/owner`) on your project also contains permissions to create and clone a repository. You shouldn't grant administrator roles or basic roles in a production environment, but you can grant them in a development or test environment.

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Create a repository

### Web interface

  1. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

     * INSTANCE_ID with the instance name.
     * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION with the instance's region.
  2. Authenticate using your Secure Source Manager credentials if needed.

  3. Click the **\+ Create new repository** icon in the navigation menu.

  4. Fill out the repository details:

     1. **Repository ID** : Enter a name for the repository.

**Note:** Repository IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lowercase letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the repository.
     2. **Description** : Optional: Enter a description of the repository.

**Caution:** Don't put sensitive or identifying data in the description or other similar resource fields. These fields are treated as Service Data in accordance with the Google Cloud [Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).
     3. **Default branch** : Name of the default branch.

  5. **Initialize repository** : Optional: Select this option if you want to initialize the repository and add .gitignore, license, and README files.

  6. **.gitignore** : Optional: Choose which files to **not** track using the drop-down menu templates.

  7. **license** : Optional: Select a common license from the drop-down menu.

  8. Click **Create repository**. 




The repository is created in your Secure Source Manager instance.

When you create a new repository, you are granted the Repo Admin role (`roles/securesourcemanager.repoAdmin`). The new IAM permission might take up to 2 minutes to propagate, so if you get a permissions error when you try to access the repository after creation, wait a few minutes and try again.

Repositories you've created are listed in the Secure Source Manager web interface on the **My repositories** page.

## Set up your credentials

Add the Secure Source Manager authentication helper to your global Git config by running the following command:

###  Linux 
    
    
    git config --global credential.'https://*.*.sourcemanager.dev'.helper gcloud.sh
    

Earlier versions of Git might not support wildcards. To add the authentication helper without wildcards, run the following command:
    
    
    git config --global credential.'https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev'.helper gcloud.sh
    

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
    

## Clone a repository

  1. In the Secure Source Manager web interface, navigate to your repository page.

  2. Copy the HTTPS URL at the top of your repository page.

  3. Clone your repository by running the following command:
         
         git clone REPOSITORY_URL
         

Where `REPOSITORY_URL` is the HTTPS URL displayed at the top of the repository page you want to clone.

Disregard the warning about cloning an empty repository.




## Push to a repository

  1. In a terminal window, change directories into your cloned repository.
         
         cd REPOSITORY_NAME
         

Where `REPOSITORY_NAME` is your repository name.

  2. Create an empty README file:
         
         touch README.md
         

  3. Add the README file to Git and create a commit message:
         
         git add README.md
         git commit -m "initial commit"
         

  4. Push your changes to your remote repository:
         
         git push -u origin main
         

Git pushes the file from the main branch to the origin remote. The output is similar to the following:
         
         Enumerating objects: 3, done.
         Counting objects: 100% (3/3), done.
         Writing objects: 100% (3/3), 211 bytes | 211.00 KiB/s, done.
         Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
         remote: . Processing 1 references
         remote: Processed 1 references in total
         To https://instance-id-123456789012-git.us-central1.sourcemanager.dev/my-project/my-repo.git
         * [new branch]      main -> main
         branch 'main' set up to track 'origin/main'.
         




## View your files in Secure Source Manager

In the Secure Source Manager web interface, click the name of your repository.

Your repository page opens and your `README.md` file is listed in the **< > Code** tab.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure any files you want to keep are available in another location.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Secure Source Manager is running.
  * LOCATION: the region where your instance is located. For information on supported locations, see [Locations](https://cloud.google.com/secure-source-manager/docs/locations).
  * REPOSITORY_ID: the repository ID.



HTTP method and URL: 
    
    
    DELETE https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    "name":"operations/cc3ea26c-9b57-11ed-be0a-2e3b5910efef","metadata":{"@type":"type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata","createTime":"2023-01-23T19:54:49.904779921Z","endTime":"2023-01-23T19:54:50.947030402Z","target":"projects/my-project/locations/us-central1/repositories/my-repo","verb":"delete","apiVersion":"v1"},"done":true,"response":{"@type":"type.googleapis.com/google.protobuf.Empty"}
    ```
    

The response resembles the following:
    
    
    {"name":"operations/cc3ea26c-9b57-11ed-be0a-2e3b5910efef","metadata":{"@type":"type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata","createTime":"2023-01-23T19:54:49.904779921Z","endTime":"2023-01-23T19:54:50.947030402Z","target":"projects/my-project/locations/us-central1/repositories/my-repo","verb":"delete","apiVersion":"v1"},"done":true,"response":{"@type":"type.googleapis.com/google.protobuf.Empty"}
    

## What's next

  * [List and view repositories](https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories) in the Secure Source Manager web interface.
  * Work with [Pull requests and issues in Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
