---
url: https://docs.cloud.google.com/source-repositories/docs/mirroring-a-bitbucket-repository/
title: Mirroring a Bitbucket repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:07.969542+00:00
---

# Mirroring a Bitbucket repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/mirroring-a-bitbucket-repository/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Mirroring a Bitbucket repository Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to mirror a Bitbucket repository to Cloud Source Repositories. With this configuration, commits that you push to the Bitbucket repository are copied, or _mirrored_ , into a repository hosted in Cloud Source Repositories.

Only Bitbucket Cloud and GitHub Cloud repositories can be mirrorred to Cloud Source Repositories; self-hosted Bitbucket and GitHub mirroring are not supported.

If you are mirroring your Bitbucket repository to Cloud Source Repositories to integrate with Cloud Build and do not need any other Cloud Source Repositories features, follow the Cloud Build instructions on [building repositories from Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-cloud) instead.

## Before you begin

When you mirror a repository, you must provide Bitbucket authentication credentials. These credentials let Cloud Source Repositories access the contents of the Bitbucket repository.

It is recommended that you [create a Bitbucket account](https://guides.co/g/bitbucket-101/11151) that is specifically dedicated to automated tasks, such as mirroring a repository. This account must have administrative access to your repository.

## Mirror a Bitbucket repository

This section shows how to mirror a Bitbucket repository to Cloud Source Repositories.

**Note:** Make sure you're signed out of Bitbucket before you mirror a repository. Signing out helps ensure you select the right Bitbucket account when you connect the Bitbucket repository to Cloud Source Repositories.

### Create a mirrored repository

In this process, you need your Bitbucket machine user credentials to grant Google Cloud read access to the Bitbucket repository.

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Click **Add repository**.

The **Add a repository** page opens.

  3. Select **Connect external repository** and click **Continue**.

The **Connect external repository** page opens.

  4. In the **Project** drop-down list, select the Google Cloud project to which the mirrored repository belongs.

If you don't have a project, you can click **Create project** to [create a project](https://cloud.google.com/source-repositories/docs/creating-an-empty-repository#creating_a_project).

  5. In the **Git provider** drop-down list, select **Bitbucket**.

  6. Select the checkbox to authorize Cloud Source Repositories to store your credentials.

  7. Click **Connect to Bitbucket**.

  8. Sign in to Bitbucket with your machine user credentials.

  9. Click **Authorize GoogleCloudPlatform**.

This option grants Google Cloud read access to your repository.

When authorization finishes, you're returned to the **Connect external repository** page. A list of repositories opens.

  10. In the **Bitbucket Repository URL** field, enter your repository URL using the following format:
         
         https://bitbucket.org/repositories/BITBUCKET_ORGANIZATION/BITBUCKET_REPOSITORY

  11. Click **Connect Selected Repository**.

The main repository page opens. This page contains a list of the repositories for this Google Cloud project, including the new repository you just created.




### Identify Bitbucket repositories

Cloud Source Repositories makes it clear which of your repositories are mirrors of Bitbucket repositories:

  * Each Bitbucket repository is represented with the Bitbucket logo.
  * The name of the repository has `bitbucket_` added to the beginning of its name.



## Upgrade a Bitbucket connection

If you mirrored a Bitbucket repository by using an earlier Google Cloud console interface, Cloud Source Repositories prompts you to upgrade when you access your mirrored repository in the current Google Cloud console. Until the upgrade is completed, these prompts occur each time you access the repository.

You must have the Source Repository Administrator role to upgrade the connection. Upgrading the connection doesn't change the mirroring behavior of the Bitbucket repository.

**Note:** Make sure you are signed out of Bitbucket before you upgrade the connection. This helps ensure you can select the right account when you connect the repository to Cloud Source Repositories.

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Navigate to the mirrored Bitbucket repository.

  3. When prompted, click **Upgrade Credentials** to upgrade your connection.




## Force a repository sync

After you set up mirroring, Cloud Source Repositories automatically syncs your repository with the mirrored repository when a user commits a change. Cloud Source Repositories lets you to view the last time your mirrored repository was synced and manually force a sync if necessary.

  1. In the Google Cloud console, browse to the mirrored Bitbucket repository.

  2. Click **Settings** _settings_.

The sync status is displayed.

![Mirrored repository sync status](https://docs.cloud.google.com/static/source-repositories/docs/images/bitbucket-sync.png)

  3. To manually force a sync of the repositories, click **Sync from Bitbucket**.


**Note:** Repositories connected using an older version of the connected repository service may not have these options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
