---
url: https://docs.cloud.google.com/developer-connect/docs/git-repo-connections/
title: Git repository connections \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:52.719249+00:00
---

# Git repository connections  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/git-repo-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Git repository connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Git repository connections in Developer Connect. Platform administrators can use this information to learn key concepts and decide when to use this type of connection.

## Introduction

A Git repository connection is type of Developer Connect system connection that lets you create and maintain narrowly scoped connections to Git-based repositories on source code management systems outside of Google Cloud.

Use Git repository connections in situations where the user who created the connection doesn't need to be present when that connection is invoked. For example, when a Git repository is connected to your [Cloud Build](https://docs.cloud.google.com/build/docs/triggers#devcon-triggers) configuration, triggering a build upon a commit to the repository doesn't require you do anything at build time. You just grant your service account permission to use the connection, and the trigger runs upon commit.

With Git repository connections, you can configure bot services in accounts on those SCMs to handle routine tasks like cloning and indexing repositories.

For example, a Gemini Code Assist code customization user can set up a Git repository connection to a GitHub repository so that Gemini Code Assist can clone and index the connected repositories.

When you have a Git repository connection, you can create links for specific repositories. When you create a link, webhooks are enabled for the linked repository. You can also [enable or disable Git proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy#view-update-console) for a linked repository. Proxy is enabled by default when you create a connection using Google Cloud console.

## Use cases

The following table lists the products and use cases that Developer Connect supports, then the SCMs that you can integrate for each use case. The table also includes links to how-to guides showing you the steps to get started with each SCM.

**Product** | **Use case** | **Supported SCMs**  
---|---|---  
**[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/agent-builder/agent-engine/deploy)** | Deploy directly from a repository linked using Developer Connect. | 

  * GitHub
  * GitLab
  * Bitbucket Cloud

  
**[Firebase App Hosting](https://firebase.google.com/docs/app-hosting)** | Create a web app from your GitHub repositories | 

  * GitHub

  
**[Cloud Build triggers](https://docs.cloud.google.com/build/docs/triggers)** | Trigger builds from events in connected repositories | 

  * GitHub
  * GitHub Enterprise Cloud
  * GitHub Enterprise
  * GitLab
  * GitLab Enterprise
  * Bitbucket Cloud
  * Bitbucket Data Center

  
**[App Lifecycle Manager](https://docs.cloud.google.com/saas-runtime/docs/overview)** | Connect to Terraform files stored in external Git repositories | 

  * GitHub
  * GitHub Enterprise Cloud
  * GitHub Enterprise

  
**[Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview)** | Create and share templates to ensure that applications follow organizational standards and to reduce deployment time. | 

  * GitHub

  
**[Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview)** | Get AI-powered coding assistance tailored to your connected repositories | 

  * GitHub
  * GitHub Enterprise Cloud
  * GitHub Enterprise
  * GitHub Enterprise in private networks
  * GitLab
  * GitLab Enterprise (including GitLab Community Edition)
  * GitLab Enterprise in private networks
  * Bitbucket Cloud
  * Bitbucket Data Center
  * Bitbucket Data Center in private networks

  
**[Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code)** | Use a Gemini-powered agent to summarize pull requests and provide in-depth code reviews. | 

  * GitHub

  
  
## Benefits

Developer Connect guides you through authentication, authorization, and networking configuration. In many cases, connections to publicly hosted repositories can be created through prebuilt Google-managed processes and apps.

Developer Connect also lets you manage all of your SCM integrations in one place. You can create, view, and edit all of your repository connections from within Developer Connect.

## Key concepts

Developer Connect handles integrations through _connections_ and _links_.

  * **Connection** : the first step in creating a bridge between Google and a non-Google source code management platform.
  * **Link** : the association with an individual Git repository that you select within a connected source code management platform. You can have multiple links under a given connection.



For example, after setting up a connection between Google and GitLab, you can configure links to multiple repositories within the connected GitLab account.

## What's next

  * [Create a Git repository connection to GitHub](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo).
  * [Create a Git repository connection to GitLab](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab).
  * [Create a Git repository connection to Bitbucket Cloud](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud).
  * [Create a Git repository connection to GitHub Enterprise in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise-private).
  * [Create a Git repository connection to GitLab Enterprise in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise-private).
  * [Create a Git repository connection to Bitbucket Data Center in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-data-center-private).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
