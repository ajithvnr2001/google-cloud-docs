---
url: https://docs.cloud.google.com/secure-source-manager/docs/overview/
title: Secure Source Manager overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:06.629372+00:00
---

# Secure Source Manager overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Secure Source Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Secure Source Manager is a regionally deployed, single-tenant managed source code repository hosted on Google Cloud. 

## Instances and repositories

Secure Source Manager instances are deployed to an available Google Cloud region and are accessible through their instance URIs. Repositories are created in the Secure Source Manager instance by using the web interface, or the Secure Source Manager API.

Separate roles and permissions are available for instances and repositories. See [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) for information on all Secure Source Manager roles and permissions.

## Git actions

Repositories support all [Git SCM](https://git-scm.com/) client commands and have built-in pull requests and issue tracking. Both HTTPS and SSH authentication are supported.

For more information on SSH authentication, see [SSH authentication](https://docs.cloud.google.com/secure-source-manager/docs/ssh-keys).

To get started using Git source code with Secure Source Manager, see [Use Git SCM](https://docs.cloud.google.com/secure-source-manager/docs/use-git).

## Issues and pull requests

You can create issues and pull requests in the Secure Source Manager web interface. You can add reviewers, labels, milestones, assignees, and due dates to your pull requests. You can open an issue on a specific branch or tag, and add labels, milestones, and assignees to the issue. For more information on issues and pull requests, see [Work with issues and pull requests](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests).

## Notifications

Secure Source Manager can send you notifications for events in pull requests and issues in which you're participating or for repositories you're watching.

For more information on notifications, read the [Notifications overview](https://docs.cloud.google.com/secure-source-manager/docs/notifications-overview) or get started with notifications by following the instructions in [Set up notifications](https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications).

## Developer Connect integration

You can connect Secure Source Manager to [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview) to unify repository connections across Google Cloud services. Connecting to Developer Connect lets you use its Git proxy feature for secure access to your Secure Source Manager repositories. This enables features like [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for Secure Source Manager repositories, letting you fetch code from Secure Source Manager without exposing your instance to the public internet.

The Developer Connect Git proxy only supports read operations such as `git clone`. `git push` operations are not supported with Git proxy.

For information on connecting Secure Source Manager to Developer Connect, see [Configure Developer Connect for Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager). For more information on using Git proxy, see [Configure and use Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).

## Connect to other services

You can invoke builds automatically using the following methods:

  * Create a Secure Source Manager [triggers file](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema) to connect to Cloud Build.
  * Use [Secure Source Manager webhooks](https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview) to connect to Jenkins or other services.



For information on connecting to Cloud Build, see [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).

For information on connecting to Jenkins, see [Connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins).

## Protect branches

When enabled, protected branches block commits based on configurable rules. You can configure multiple branch protection rules for different sets of branches.

The following branch protection options are configurable:

  * Specify a single branch to apply the branch protection rule to, or apply the branch protection rule to all branches.
  * Require pull requests before merging into protected branches.
  * Set the required number of reviewers and approvers before a pull request can be merged into a protected branch.
  * Block merging a pull request if new commits are added after approvals are granted.
  * Require comments to be resolved before merging into a protected branch.
  * Require a linear Git history.
  * Require successful build status checks before merging a pull request into a protected branch.



For more information on protecting branches in Secure Source Manager, see [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).

## Encrypt data

By default, Google Cloud automatically [encrypts data when it is at rest](https://cloud.google.com/security/encryption-at-rest/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK) for creating a Secure Source Manager instance.

When you enable CMEK, data at rest in the instance is encrypted using a key that you manage within Cloud Key Management Service. You can control access to the CMEK key using Identity and Access Management. If you temporarily disable or permanently destroy the CMEK key, data encrypted with that key cannot be accessed. For more information on creating Secure Source Manager instances using CMEK, see [Customer-managed encryption keys](https://docs.cloud.google.com/secure-source-manager/docs/cmek).

## Security compliance

Secure Source Manager is in compliance with the following certifications:

  * [FedRAMP High compliant](https://cloud.google.com/security/compliance/fedramp)

  * [HIPAA compliant](https://cloud.google.com/security/compliance/hipaa)




## Configure a private Secure Source Manager instance in a VPC Service Controls perimeter

You can use Secure Source Manager in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter in order to guard against data exfiltration. For more information, see [Configure Secure Source Manager in a VPC Service Controls perimeter](https://docs.cloud.google.com/secure-source-manager/docs/configure-service-perimeter).

## What's next

  * [Enable the Secure Source Manager API](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable).
  * [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  * [Create and clone a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository).
  * Read about [Software supply chain security](https://cloud.google.com/software-supply-chain-security/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
