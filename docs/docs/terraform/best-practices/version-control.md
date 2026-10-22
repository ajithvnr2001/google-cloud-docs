---
url: https://docs.cloud.google.com/docs/terraform/best-practices/version-control/
title: Best practices for version control \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:45.257399+00:00
---

# Best practices for version control  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/best-practices/version-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Best practices for version control Stay organized with collections  Save and categorize content based on your preferences. 

This document provides version control best practices to consider when using Terraform for Google Cloud.

As with other forms of code, store infrastructure code in version control to preserve history and allow easy rollbacks.

This guide is not an introduction to Terraform. For an introduction to using Terraform with Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Use a default branching strategy

For all repositories that contain Terraform code, use the following strategy by default:

  * The `main` branch is the primary development branch and represents the latest approved code. The `main` branch is [protected](https://docs.gitlab.com/ee/user/project/protected_branches.html).
  * Development happens on feature and bug-fix branches that branch off of the `main` branch. 
    * Name feature branches `feature/$feature_name`.
    * Name bug-fix branches `fix/$bugfix_name`.
  * When a feature or bug fix is complete, merge it back into the `main` branch with a pull request.
  * To prevent merge conflicts, rebase branches before merging them.



## Use environment branches for root configurations

For repositories that include root configurations that are directly deployed to Google Cloud, a safe rollout strategy is required. We recommend having a separate _branch_ for each environment. Thus, changes to the Terraform configuration can be promoted by [merging changes between the different branches](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code).

![Separate branch for each environment](https://docs.cloud.google.com/docs/terraform/images/folders-branches-environments.svg)

## Allow broad visibility

Make Terraform source code and repositories broadly visible and accessible across engineering organizations, to infrastructure owners (for example, SREs) and infrastructure stakeholders (for example, developers). This ensures that infrastructure stakeholders can have a better understanding of the infrastructure that they depend on.

Encourage infrastructure stakeholders to submit merge requests as part of the change request process.

## Never commit secrets

Never commit secrets to source control, including in Terraform configuration. Instead, upload them to a system like [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) and reference them by using data sources.

Keep in mind that such sensitive values might still end up in the state file and might also be exposed as outputs.

## Organize repositories based on team boundaries

Although you can use separate directories to manage logical boundaries between resources, organizational boundaries and logistics determine _repository_ structure. In general, use the design principle that configurations with different approval and management requirements are separated into different source control repositories. To illustrate this principle, these are some possible repository configurations:

  * **One central repository** : In this model, all Terraform code is centrally managed by a single platform team. This model works best when there is a dedicated infrastructure team responsible for all cloud management and approves any changes requested by other teams.

  * **Team repositories:** In this model, each team is responsible for their own Terraform repository where they manage everything related to the infrastructure they own. For example, the security team might have a repository where all security controls are managed, and application teams each have their own Terraform repository to deploy and manage their application.

Organizing repositories along team boundaries is the best structure for most enterprise scenarios.

  * **Decoupled repositories** : In this model, each _logical_ Terraform component is split into its own repository. For example, networking might have a dedicated repository, and there might be a separate project factory repository for project creation and management. This works best in highly decentralized environments where responsibilities frequently shift between teams.




### Sample repository structure

You can combine these principles to split Terraform configuration across different repository types:

  * Foundational
  * Application and team-specific



#### Foundational repository

A _foundational_ repository that contains major central components, such as folders or org IAM. This repository can be managed by the central cloud team.

  * In this repository, include a directory for each major component (for example, folders, networks, and so on).
  * In the component directories, include a separate folder for each environment (reflecting the directory structure guidance mentioned earlier).



![Foundational repository structure](https://docs.cloud.google.com/docs/terraform/images/repo-1-foundations.svg)

#### Application and team-specific repositories

Deploy _application and team-specific_ repositories separately for each team to manage their unique application-specific Terraform configuration.

![Application and team-specific repository structure](https://docs.cloud.google.com/docs/terraform/images/repo-n-application-platform-team-specific.svg)

## What's next

  * Learn about [best practices for Terraform operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations).
  * Learn about [best practices for using Terraform securely](https://docs.cloud.google.com/docs/terraform/best-practices/security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
