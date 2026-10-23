---
url: https://docs.cloud.google.com/source-repositories/docs/csr-ssm-migration-guide/
title: Migrate to Secure Source Manager \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:51.942732+00:00
---

# Migrate to Secure Source Manager  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/csr-ssm-migration-guide/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Migrate to Secure Source Manager Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to migrate a Git repository, including all its information, from Google's Cloud Source Repositories (CSR) to Secure Source Manager (SSM). This migration uses standard Git commands to clone and push repository data.

## Prerequisites

Before you begin the migration, make sure you meet the following prerequisites:

  * **Permissions** : The user or service accounts must have the following permissions to perform the migration: 
    * `source.repos.get`, which is available in the `roles/source.reader` role, on the source CSR repository
    * `securesourcemanager.instances.access`, which is available in the `roles/securesourcemanager.instanceAccessor` role, and `securesourcemanager.repositories.fetch`, which is available in the `roles/securesourcemanager.repoWriter` role, on the target SSM instance and repository. If you are creating new repositories, see [Create a repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).
  * **Git Client** : You need a computer with the Git command-line tool installed.
  * **Google Cloud SDK** : To authenticate when using HTTPS, you must install version 395.0.0 or later on the same computer where you installed the Git tool. If you don't have the Google Cloud SDK, you must connect to both CSR and SSM using SSH keys.
  * **SSM Instance** : Make sure you can access the SSM instance from your computer. If your instance is configured using Private Service Connect, see [Access a private instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance#access-private-instance) for access details.
  * **Local Storage** : You need enough local disk space to temporarily store clones of the repositories you are migrating.



## Migration Steps

The migration process involves cloning the complete repository from CSR to your local computer and then pushing the clone to the SSM repository.

### Determine access principal and method for CSR, SSM repositories

You can connect to CSR using HTTP or SSH transports when you authenticate as a user principal, or through HTTP when you authenticate as a service account. You can connect and authenticate with SSM using HTTP or SSH transports, as a user or service account principal.

You don't need to use the same transport or principal across CSR and SSM. Determine the principal and transport you will use for each platform. For more information on impersonating service accounts, see [Service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation#gcloud).

### Ensure CSR Repository is Read-Only

This migration guide doesn't use automatic mirroring or synchronization. Therefore, make sure no one writes to the CSR repository during or after the migration. Update IAM permissions so no user has a role other than `roles/source.reader` on the repository. Alternatively, coordinate with your users to halt all commits during the migration.

### Create Secure Source Manager Repository

You can skip this step if an administrator has already created the repository for you.

To create an empty repository in your SSM instance, follow the guide to [create a new repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository). Make sure that:

  * If using the UI, don't select **Initialize Repository** , because this creates a non-empty repository.
  * If using Google Cloud CLI, don't set the `--gitignores`, `--readme`, and `--licenses` flags, because this creates a non-empty repository.
  * If using the API, don't set the `gitignores`, `license`, and `readme` fields of the `InitialConfig`, because this creates a non-empty repository.



### Validate SSM Repository Settings

Verify that the repository is empty by checking the UI or by cloning the repository and running `git show-ref`. The output is empty if the repository is empty.

Make sure there are no active branch protection rules by checking the UI or by using the API. There should be no rules, or all rules should be disabled to prevent blocking the migration.

### Ensure local and remote disk space

Before cloning the CSR repository, find its total size. Run `gcloud source repos describe <var>CSR_REPO_NAME</var>`. This command shows the total number of bytes in the repository. To assess available disk space on a Linux system, run `df .` to see the number of bytes available in the current directory.

SSM has a default limit of 100 GB of storage per instance. Verify that the CSR repository will fit before you clone it.

### Clone the CSR Repository

Clone the full repository history from CSR to your local computer.

  1. Go to the local directory where you want to temporarily store the repository.
  2. Clone the repository: `sh git clone <var>CSR_REPO_URL</var> --mirror`



This command creates a bare clone, which is optimized for pushing the entire repository contents to another remote. You'll notice that the directory only contains files like `config` and `HEAD`, instead of your repository contents. This is expected; all the repository content has been cloned and is present in the `objects` directory and others, but there is no working copy.

### Add the Secure Source Manager Repository as a New Remote

Run the following command:
    
    
    git remote add ssm <var>SSM_REPOSITORY_URL</var>
    

### Push the Full Repository to Secure Source Manager

Push all branches, tags, and references from the local clone to the SSM remote:
    
    
    git push --mirror ssm
    

## Validation

After the push operation is complete, clone the SSM repository into a different directory. Then, compare the CSR and SSM copies of the repository:

  * **Number of branches** : Run `git branch -r` in each repository and verify that the number of branches is the same. On Linux or macOS systems, piping the command to `wc -l` counts lines of output.
  * **Number of tags** : Run `git tag` in each repository and verify that the number of tags is the same. On Linux or macOS systems, piping the command to `wc -l` counts lines of output.
  * **HEAD commit** : Run `git rev-parse HEAD` in each repository, and verify that the commit hash is equal.
  * **Commit count** : Run `git rev-list --all --count` in each repository, and verify that the number of commits is the same.



## Cleanup

  * If you impersonated a service account during the migration, then run `gcloud config set account` to reset your credentials.
  * If you disabled branch protection rules, then re-enable **Branch Protection Rules** on the SSM repository.
  * Remove bare copies of the CSR repository from the computer you used for the migration.
  * Delete the original CSR repository.



## What's next

  * [Secure Source Manager overview](https://docs.cloud.google.com/secure-source-manager/docs/overview)
  * [Create an instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
