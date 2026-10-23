---
url: https://docs.cloud.google.com/source-repositories/docs/adding-repositories-as-remotes/
title: Adding a repository as a remote \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:33.274496+00:00
---

# Adding a repository as a remote  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/adding-repositories-as-remotes/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Adding a repository as a remote Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Source Repositories to add a Google Cloud repository as a remote to a local Git repository.

**Note:** You can add only private repositories as remotes.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Install [Git](http://git-scm.com/).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Add the repository as a remote

  1. Change your current working directory to the directory that contains your local Git repository:
         
         cd [REPO_DIRECTORY]
         

Where `[REPO_DIRECTORY]` is the path to your repository.

  2. On Linux or macOS, run the credential helper script:

###  Linux or macOS 
         
         git config --global credential.'https://source.developers.google.com'.helper gcloud.sh
         

###  Windows 
         
         git config --global credential.https://source.developers.google.com.helper gcloud.cmd
         

Credential helper scripts provide the information that Git needs to connect securely to Cloud Source Repositories using your Google Account credentials. You don't need to perform any additional configuration steps (for example, uploading `ssh` keys) to establish this secure connection.

**Note:** The Google Cloud CLI must be in your `$PATH` for the credential helper scripts to work. If you cannot use the Google Cloud CLI, you can manually generate static credentials. For example, if you're on a build server, you might not have access to the gcloud CLI. For more information, see Generating static credentials in this topic.
  3. Create the repository in Cloud Source Repositories:
         
         gcloud source repos create [REPO_NAME]
         

Where `[REPO_NAME]` is the name for your Google Cloud repository.

  4. Add a repository as a remote:
         
         git remote add google \
         https://source.developers.google.com/p/[PROJECT_ID]/r/[REPO_NAME]
         

Where:

     * `[PROJECT_ID]` is your Google Cloud project ID.
     * `[REPO_NAME]` is the name of your Google Cloud repository.



## Use the repository as a remote

Google Cloud repositories are fully featured Git repositories. You can use the standard set of Git commands to interact with these repositories, including `push`, `pull`, `clone`, and `log`.

### Push to a Google Cloud repository

To push from your local Git repository to a Google Cloud repository, enter this command:
    
    
    git push google master
    

### Pull from a Google Cloud repository

To pull from a Google Cloud repository to your local Git repository, enter this command:
    
    
    git pull google master
    

### View the commit history of a Google Cloud repository

To view the commit history, enter this command:
    
    
    git log google/master
    

## Generate static credentials

In some cases, you might not have access to the gcloud CLI. For example, you might work on a build server that doesn't have access to these tools. In these situations, you can manually generate static credentials.

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Hold the pointer over the repository you want to clone.

  3. Click **Clone** _add_box_.

A dialog with authentication options opens.

  4. Click the **Manually generated credentials** tab and follow the instructions to clone your repository.




## What's next

  * After you have pushed source files to Cloud Source Repositories, you can view repository files from within the Google Cloud console.

  * [Learn how to use the source browser](https://docs.cloud.google.com/source-repositories/docs/using-source-browser).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
