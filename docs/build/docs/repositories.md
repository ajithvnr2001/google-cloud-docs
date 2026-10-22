---
url: https://docs.cloud.google.com/build/docs/repositories/
title: Cloud Build repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:12:00.468996+00:00
---

# Cloud Build repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud Build repositories Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build lets you create and manage connections to source code repositories using the Google Cloud console. You can create and manage connections using Developer Connect or Cloud Build repositories (2nd gen). With Cloud Build repositories (2nd gen), you can additionally configure repositories programmatically without the Google Cloud console and independently without a trigger.

This page provides an overview of Cloud Build repositories (2nd gen) and repositories linked through Developer Connect.

## Connect to source providers using Developer Connect

Developer Connect lets you connect non-Google products or non-Google developer tools to Google Cloud using standardized steps and apps. You can configure Cloud Build to use a repository linked to a Developer Connect connection and then create triggers to build from the linked repositories. You can invoke builds on commits and pull requests.

Developer Connect can by used to connect to the following providers:

  * [GitHub](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo)
  * [GitHub Enterprise](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise)
  * [GitLab](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab)
  * [GitLab Enterprise Edition](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise)
  * [Bitbucket Data Center](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-dc)
  * [Bitbucket Cloud](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud)



For more information about Developer Connect, see the [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

## Connect to providers using Cloud Build repositories (2nd gen)

With Cloud Build repositories (2nd gen), you can create and manage repository connections programmatically. You can set up a single connection for a repository and use Secret Manager secrets from that connection to programmatically set up additional connections across regions and projects. You can also set up connections using Terraform, in addition to the Google Cloud console, `gcloud` command-line tool, and the API. You must create a host connection prior to linking repositories when using Cloud Build repositories (2nd gen).

Cloud Build repositories (2nd gen) can be used with the following providers:

  * [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github)
  * [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise)
  * [GitLab](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab)
  * [GitLab Enterprise Edition](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition)
  * [Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center)
  * [Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud)



You can invoke builds on commits and pull requests. You can also invoke builds [manually](https://docs.cloud.google.com/build/docs/manually-build-code-source-repos), on a [Pub/Sub topic](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events), or on an incoming [webhook event](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events).

**Note:** Cloud Build repositories (1st gen) is superseded by 2nd gen, but is available as a legacy option.

## Repository capabilities

The following table outlines capabilities associated with Cloud Build 2nd gen repositories and with repositories linked through Developer Connect.

**Capabilities** | **Cloud Build repositories (2nd gen)** | **Developer Connect repositories**  
---|---|---  
You can build in response to branch pushes, tag pushes, or pull request events. | Yes | Yes  
You can create a manual trigger | Yes | No  
You can create a Pub/Sub trigger | Yes | No  
You can create a webhook trigger | Yes | No  
You can create a single connection for a repository and use authentication from that connection to set up additional connections | Yes | Yes  
You can connect repositories from GitHub and GitHub Enterprise | Yes | Yes  
You can connect repositories from GitLab and GitLab Enterprise Edition | Yes | Yes  
You can connect repositories from Bitbucket Data Center and Bitbucket Cloud | Yes | Yes  
You can connect repositories from Cloud Source Repositories | No | No  
You can link repositories without creating a host connection | No | No  
You can create repository connections using gcloud | Yes | Yes  
You can create and automate repository connections using Terraform | Yes, except for Bitbucket Data Center and Bitbucket Cloud | No  
Your host connections and link repositories must exist in a particular region | Yes | Yes  
  
**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

## Specifying repositories as dependencies

By default, one of the following is used as the repository for the build:

  * The repository that triggers a build, if you're using a [trigger](https://docs.cloud.google.com/build/docs/triggers)

  * The repository that you specify using `gcloud builds submit`




However, you can [specify repositories explicitly as dependencies](https://docs.cloud.google.com/build/docs/building/manage-dependencies), including the main source code repositories and any others your build depends on.

[Learn more](https://docs.cloud.google.com/build/docs/building/manage-dependencies).

## What's next

  * Find out more about [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview).
  * Learn how to [connect a GitHub host and repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github).
  * Learn how to [connect a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise).
  * Learn how to [connect a GitHub Enterprise repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise).
  * Learn how to [connect a GitLab host](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab).
  * Learn how to [connect a GitLab repository](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab).
  * Learn how to [connect a GitLab Enterprise Edition host](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition).
  * Learn how to [connect a GitLab Enterprise Edition repository](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition).
  * Learn how to [manually build code in source repositories](https://docs.cloud.google.com/build/docs/manually-build-code-source-repos).
  * Learn how to [automate builds in response to webhook events](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events).
  * Learn how to [automate builds in response to Pub/Sub events](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
