---
url: https://docs.cloud.google.com/source-repositories/docs/cloning-repositories/
title: Cloning a repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:42.674037+00:00
---

# Cloning a repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/cloning-repositories/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Cloning a repository Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to clone the contents of a repository from Cloud Source Repositories to your local machine.

## Before you begin

The following is required to clone the contents of a repository:

  * You must have [authentication on your local system](https://docs.cloud.google.com/source-repositories/docs/authentication).

The steps to clone a repository vary depending on your authentication type (SSH, Google Cloud CLI, or manually generated credentials).

  * You must have [a repository in Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository).

  * You must have [permissions to interact with the repository](https://docs.cloud.google.com/source-repositories/docs/configure-access-control).

  * The repository to be cloned cannot have a restricted name such as `All-Users` or `All-Projects`.




## Clone using SSH

If you're not using manually generated credentials or the gcloud CLI, you can clone a repository by using SSH.

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Hold your pointer over the repository you want to clone.

  3. Click **Clone** add_box.

A dialog with authentication options opens.

  4. Click the **SSH authentication** tab and follow the instructions to clone your repository.




###  gcloud 

  1. Ensure that you're [authenticated with SSH](https://docs.cloud.google.com/source-repositories/docs/authentication#ssh) on your local machine.

  2. On your local system, use your Google Cloud username and the fully qualified SSH path to your repository to clone your repository:
         
         git clone ssh://[EMAIL]@source.developers.google.com:2022/p/[PROJECT_ID]/r/[REPO_NAME]
         

Where:

     * `[EMAIL]` is your Google Cloud username.
     * `[PROJECT_ID]` is the ID of the Google Cloud project where the repository is located.
     * `[REPO_NAME]` is the name of the repository.

For example:
    
    git clone ssh://user@gmail.com@source.developers.google.com:2022/p/example-project/r/test-repo
    




The first time you connect to Cloud Source Repositories by using SSH, you're asked to confirm the SSH key fingerprints for the remote host. The hostname for the repository service is `source.developers.google.com`. The fingerprints are:
    
    
    none
    SHA256:AGvEpqYNMqsRNIviwyk4J4HM0lEylomDBKOWZsBn434
    MD5:74:84:6c:08:d5:b5:54:68:19:da:2a:8e:4c:5b:d3:0d
    

## Clone using the gcloud CLI

If you're not using SSH or manually generated credentials, you can clone a repository by using the gcloud CLI.

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Hold your pointer over the repository you want to clone.

  3. Click **Clone** add_box.

A dialog with authentication options opens.

  4. Click the **Google Cloud SDK** tab and follow the instructions to clone your repository.




###  gcloud 

  1. Ensure that [the gcloud CLI is installed](https://docs.cloud.google.com/source-repositories/docs/authentication#authenticate-using-the-cloud-sdk) on your local system.

  2. In a terminal window, provide your authentication credentials:
         
         gcloud init
         

  3. Clone your repository:
         
         gcloud source repos clone [REPO_NAME] --project=[PROJECT_NAME]
         

Where:

     * `[REPO_NAME]` is the name of your repository.
     * `[PROJECT_NAME]` is the name of your Google Cloud project.

For example:
    
    gcloud source repos clone test-repo --project=example-project
    




## Clone using manually generated credentials

If you're not using SSH or the gcloud CLI, you can clone a repository by using manually generated credentials.

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Hold your pointer over the repository you want to clone.

  3. Click **Clone** add_box.

A dialog with authentication options opens.

  4. Click the **Manually generated credentials** tab and follow the instructions to clone your repository.




###  gcloud 

  1. Ensure that you have [generated and stored your Git credentials](https://docs.cloud.google.com/source-repositories/docs/authentication#manually-generated-credentials).

  2. In a terminal window, enter the following command:
         
         git clone https://source.developers.google.com/p/[PROJECT_NAME]/r/[REPO_NAME]
         

Where:

     * `[PROJECT_NAME]` is the name of your project.
     * `[REPO_NAME]` is the name of your repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
