---
url: https://docs.cloud.google.com/source-repositories/docs/mirroring-a-github-repository/
title: Mirroring a GitHub repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:10.860571+00:00
---

# Mirroring a GitHub repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/mirroring-a-github-repository/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Mirroring a GitHub repository Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to mirror a GitHub repository to Cloud Source Repositories. With this configuration, commits that you push to the GitHub repository are copied, or _mirrored_ , into a repository hosted in Cloud Source Repositories.

Only Bitbucket Cloud and GitHub Cloud repositories can be mirrored to Cloud Source Repositories; self-hosted Bitbucket and GitHub mirroring are not supported.

If you are mirroring your GitHub repository to Cloud Source Repositories to integrate with Cloud Build and do not need any other Cloud Source Repositories features, follow the Cloud Build instructions on [building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github) instead.

## Before you begin

When you mirror a repository, you must provide GitHub authentication credentials. These credentials let Cloud Source Repositories access the contents of the GitHub repository.

If you're using [GitHub organizations](https://help.github.com/articles/about-organizations/), we recommend that you use a [machine user account](https://developer.github.com/v3/guides/managing-deploy-keys/#machine-users) specifically dedicated to automated tasks, such as mirroring a repository. This account must have administrative access to your repository.

## Mirror a GitHub repository

This section shows how to mirror a GitHub repository to Cloud Source Repositories.

**Note:** Make sure you're signed out of GitHub before you mirror a repository. Signing out helps ensure you select the right GitHub account when you connect the GitHub repository to Cloud Source Repositories.

### Create a mirrored repository

In this process, you need your GitHub machine user credentials to grant Google Cloud read access to the GitHub repository.

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Click **Add repository**.

The **Add a repository** page opens.

  3. Select **Connect external repository** and click **Continue**.

The **Connect external repository** page opens.

  4. In the **Project** drop-down list, select the Google Cloud project to which the mirrored repository belongs.

If you don't have a project, you can click **Create project** to [create a project](https://cloud.google.com/source-repositories/docs/creating-an-empty-repository#creating_a_project).

  5. In the **Git provider** drop-down list, select **GitHub**.

  6. Select the checkbox to authorize Cloud Source Repositories to store your credentials.

  7. Click **Connect to GitHub**.

  8. Sign in to GitHub with your machine user credentials.

  9. Click **Authorize GoogleCloudPlatform**.

This option grants Google Cloud read access to all repositories in the GitHub user account.

When authorization finishes, you're returned to the **Connect external repository** page. A list of repositories opens.

  10. From the list of repositories, select the repository you want to mirror.

  11. Click **Connect Selected Repository**.

The main repository page opens. This page contains a list of the repositories for this Google Cloud project, including the new repository you just created.




### Identify GitHub repositories

Cloud Source Repositories makes it clear which of your repositories are mirrors of GitHub repositories:

  * Each GitHub repository is represented with the GitHub logo.
  * The name of the repository has `github_` added to the beginning of its name.



## Force a repository sync

After you set up mirroring, Cloud Source Repositories automatically syncs your repository with the mirrored repository when a user commits a change. Cloud Source Repositories lets you view the last time your mirrored repository was synced and manually force a sync if necessary.

  1. In the Google Cloud console, browse to the mirrored GitHub repository.

  2. Click **Settings** _settings_.

The sync status is displayed.

![Mirrored repository sync status](https://docs.cloud.google.com/static/source-repositories/docs/images/github-sync.png)

  3. To manually force a sync of the repositories, click **Sync from GitHub**.


**Note:** Repositories connected using an older version of the connected repository service may not have these options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
