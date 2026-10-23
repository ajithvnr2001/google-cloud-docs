---
url: https://docs.cloud.google.com/source-repositories/docs/features/
title: Features \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:42.714523+00:00
---

# Features  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/features/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Features Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Source Repositories provides fully featured, private [Git](https://git-scm.com) repositories hosted on [Google Cloud](https://docs.cloud.google.com/).

You can use Cloud Source Repositories for collaborative, version-controlled development of any app or service, including those that run on [App Engine](https://docs.cloud.google.com/appengine/docs) and [Compute Engine](https://docs.cloud.google.com/compute/docs).

If you're familiar with Git, you can get started quickly with Cloud Source Repositories. For example, you can add Cloud Source Repositories to a local Git repository as a remote, or you can connect it to a hosted repository on GitHub or Bitbucket. From a local repository, you can use the standard set of Git commands to interact with the repository in the cloud, including `push`, `pull`, `clone`, and `log`.

**Caution**

Cloud Source Repositories are intended to store only the source code for your app and not user or personal data. Don't store any Core App Engine Customer Data (as defined in your [License Agreement](https://docs.cloud.google.com/terms/service-terms#26-definitions)) in Cloud Source Repositories. 

## Multiple repositories

You can [create multiple repositories](https://docs.cloud.google.com/source-repositories/docs/setting-up-repositories) for a single Google Cloud project, allowing you to organize the code associated with your cloud project in whatever way works best for you.

## Connected repositories

You can connect an existing [GitHub](https://github.com) or [Bitbucket](https://bitbucket.org/) repository to Cloud Source Repositories. Connected repositories are synchronized with Cloud Source Repositories automatically.

## Editor support

Because repositories in Cloud Source Repositories are Git repositories, you can continue to use the editor of your choice to work on your code. For a more integrated experience, see [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/vcs)

## Source browser

Cloud Source Repositories also provide a [source browser](https://docs.cloud.google.com/source-repositories/docs/using-source-browser) that you can use to view repository files from within the Google Cloud console.

![Source browser](https://docs.cloud.google.com/static/source-repositories/docs/images/view-repository-file.png)

## Automatic logging

Cloud Source Repositories automatically send logs on repository activity to Cloud Logging to help track and troubleshoot data access.

You can use these logs to review recent repository synchronization, repository access by other users, and administrative actions such as creations, deletions, and permission changes. Moreover, you can configure notification settings such that an alert is sent to you when an error is logged during a repository synchronization.

For more information regarding reading and writing log entries in Logging, see this [quickstart](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud). For information about possible billing configurations to manage storage of your logs, see [Logging pricing](https://cloud.google.com/stackdriver/pricing_v2).

## Security key detection

Cloud Source Repositories offer security key detection to block `git push` transactions that contain sensitive information. This feature is designed to improve the security of your source code. Enabling it is a best practice. For more information, see [Detecting security keys](https://docs.cloud.google.com/source-repositories/docs/detecting-security-keys).

## User data

**Caution**

Cloud Source Repositories are intended to store only the source code for your app and not user or personal data. Don't store any Core App Engine Customer Data (as defined in your [License Agreement](https://docs.cloud.google.com/terms/service-terms#26-definitions)) in Cloud Source Repositories. 

## What's next

  * [Learn how to set up a repository.](https://docs.cloud.google.com/source-repositories/docs/setting-up-repositories)
  * [Learn how to add a repository as a remote.](https://docs.cloud.google.com/source-repositories/docs/adding-repositories-as-remotes)
  * [Learn how to connect a repository hosted on GitHub or Bitbucket.](https://docs.cloud.google.com/source-repositories/docs/connecting-hosted-repositories)
  * [Learn how to use the source browser.](https://docs.cloud.google.com/source-repositories/docs/using-source-browser)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
