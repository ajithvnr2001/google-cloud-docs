---
url: https://docs.cloud.google.com/source-repositories/docs/pushing-code-from-a-repository/
title: Pushing code from an existing repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:35.736798+00:00
---

# Pushing code from an existing repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/pushing-code-from-a-repository/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Pushing code from an existing repository Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to push code from an existing repository on your local machine to Cloud Source Repositories.

## Before you begin

You must have a repository in Cloud Source Repositories. To create a repository, see [Creating an empty repository](https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository).

## Push a local repository into Cloud Source Repositories

You can push a local repository to Cloud Source Repositories by using either SSH, the Google Cloud CLI, or manually generated credentials.

###  SSH 

  1. Ensure you have [set up local authentication](https://docs.cloud.google.com/source-repositories/docs/authentication#ssh) with SSH.

  2. Add your local repository as a remote:
         
         git remote add google ssh://[EMAIL]@source.developers.google.com:2022/p/[PROJECT_ID]/r/[REPO_NAME]
         

Where:

     * `[EMAIL]` is your Google Cloud username.
     * `[PROJECT_ID]` is the ID of the Google Cloud project where the repository is located.
     * `[REPO_NAME]` is the name of the repository.

For example:
    
    git remote add google ssh://user@gmail.com@source.developers.google.com:2022/p/example-project/r/test-repo
    

  3. Push your code to Cloud Source Repositories:
         
         git push --all google
         




###  gcloud CLI 

  1. Ensure that [the gcloud CLI is installed](https://docs.cloud.google.com/source-repositories/docs/authentication#authenticate-using-the-cloud-sdk) on your machine.

  2. Open a terminal window.

  3. If you're using Windows, enter the following command:
         
         gcloud init && git config credential.helper gcloud.cmd
         

If you're using Linux or macOS, enter the following command:
         
         gcloud init && git config credential.helper gcloud.sh
         

  4. Add your local repository as a remote:
         
         git remote add google \
         https://source.developers.google.com/p/[PROJECT_NAME]/r/[REPO_NAME]
         

Where:

     * `[PROJECT_NAME]` is the name of your Google Cloud project.
     * `[REPO_NAME]` is the name of your repository.
  5. Push your code to Cloud Source Repositories:
         
         git push --all google
         




###  Manual 

  1. Ensure you have [generated and stored your Git credentials](https://docs.cloud.google.com/source-repositories/docs/authentication#manually-generated-credentials).

  2. Open a terminal window and add your local repository as a remote:
         
         git remote add google \
         https://source.developers.google.com/p/[PROJECT_NAME]/r/[REPO_NAME]
         

Where:

     * `[PROJECT_NAME]` is the name of your Google Cloud project.
     * `[REPO_NAME]` is the name of your repository.
  3. Push your code to Cloud Source Repositories:
         
         git push --all google
         




## Use the repository as a remote

Google Cloud repositories are fully featured Git repositories. You can use the standard set of Git commands to interact with these repositories, including `push`, `pull`, `clone`, and `log`.

### Push to a Google Cloud repository

To push from your local Git repository to a Google Cloud repository, enter the following command:
    
    
    git push google master
    

### Pull from a Google Cloud repository

To pull from a Google Cloud repository to your local Git repository, enter the following command:
    
    
    git pull google master
    

### View the commit history of a Google Cloud repository

To view the commit history, enter the following command:
    
    
    git log google/master
    

## What's next

After you push your local repository to your local machine, you can:

  * [Learn from your code's history](https://docs.cloud.google.com/source-repositories/docs/history-overview).
  * [Search your code](https://docs.cloud.google.com/source-repositories/docs/searching-code).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
