---
url: https://docs.cloud.google.com/looker/docs/looker-cicd/
title: Creating a multi-tier Looker CI/CD workflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:56.647115+00:00
---

# Creating a multi-tier Looker CI/CD workflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-cicd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a multi-tier Looker CI/CD workflow Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide explains how to implement a multi-tier continuous delivery (CD) deployment pipeline across multiple Looker environments. To configure automated testing and validation within your LookML projects, see [Looker Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration).

Advanced users may want to create a CI/CD workflow in Looker so that they can manage LookML in a formal software development manner. These guides explain how to configure such a setup so that LookML may be developed, QAed, validated, and deployed.

The examples given explain a three-tier system that comprises development, QA, and production. However, you can apply the same principles to a two-tier or four-tier system.

Once enabled, all Looker developers must use the CI/CD workflow.

## Process overview

In this process, developers write LookML in their development environment, using Git pull requests. The pull requests are configured to require that code reviews are completed and that the code is evaluated with automatic processes.

When LookML is ready for testing, it is tagged in Git with a release candidate version number and promoted to QA. When QA approves, the LookML is promoted to production based on a Git tagged version number.

If needed, content like Looks and user-defined dashboards can be migrated between the CI/CD tiers through the use of [Gazer](https://github.com/looker-open-source/gzr).

![Diagram showing the CI/CD workflow.](https://docs.cloud.google.com/static/looker/docs/images/cicd-workflow.png)

## Installation and configuration

Find installation and configuration steps on the [Multi-tier Looker CI/CD installation and configuration](https://docs.cloud.google.com/looker/docs/looker-cicd-installation) page.

## Usage and workflow

Find details for using this setup after installation on the [Multi-tier Looker CI/CD usage and workflow](https://docs.cloud.google.com/looker/docs/looker-cicd-usage) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
