---
url: https://docs.cloud.google.com/source-repositories/docs/detecting-security-keys/
title: Detecting security keys \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:43.843221+00:00
---

# Detecting security keys  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/detecting-security-keys/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Detecting security keys Stay organized with collections  Save and categorize content based on your preferences. 

You should never store security keys in a version-control system. Cloud Source Repositories can help you prevent users from storing security keys in a Google Cloud repository. Cloud Source Repositories can check for the following types of security keys:

  * Google Cloud service account credentials (JSON format)
  * PEM-encoded private keys (including RSA, DSA, and PGP)



This checking feature is available for all repositories at no charge.

## How the security-key checking feature works

When a user executes a `git push` command, the checking feature looks for data that might be a security key. If a match is found, the feature blocks the `git` push and notifies users what was found and where. For example:
    
    
    The push has been rejected because we detect that it contains a private key.
    Please check the following commands and confirm that it's intentional:
    
    git show [COMMIT]
    
    You can use `git rev-list --objects --all` to find the files.
    
    To push these files, please run `git push -o nokeycheck`.
    

**Note:** To help store security keys more securely, consider using [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/store-secrets).

## Before you begin

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## Disable security key detection

To disable security key detection, use the following `gcloud` command:
    
    
        gcloud init
        gcloud source project-configs update --disable-pushblock
    

## Enable security key detection

To enable private key detection, use the following `gcloud` command:
    
    
        gcloud init
        gcloud source project-configs update --enable-pushblock
    

## Override security key detection

To override the security key detection feature, use the following `git` command:
    
    
        git push -o nokeycheck
    

## What's next

After you set up a Google Cloud repository, you might find the following topics helpful:

  * [Controlling access to repositories](https://docs.cloud.google.com/source-repositories/docs/configure-access-control)
  * [Using the source browser](https://docs.cloud.google.com/source-repositories/docs/using-source-browser)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
