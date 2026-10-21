---
url: https://docs.cloud.google.com/source-repositories/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:37.845670+00:00
---

# Troubleshooting  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/troubleshooting/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Support ](https://docs.cloud.google.com/source-repositories/docs/support)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page describes tips, troubleshooting, and known issues that you might find helpful if you run into problems using Cloud Source Repositories.

## Search results don't match expectations

It can take several hours for a newly added repository or large commit to be indexed for search. Try again after a few hours. If no changes have been made in the last 24 hours or if this issue persists for over 24 hours, please contact [support](https://docs.cloud.google.com/support).

## Users are unable to perform actions such as viewing or creating repositories

Cloud Source Repositories uses Identity and Access Management to grant permissions to users. If a user cannot perform a specific action, such as create a new repository, check to ensure they have the correct IAM permissions. To learn more about these permissions, see [Configuring Access to Repositories](https://docs.cloud.google.com/source-repositories/docs/configure-access-control).

For example, if a user has the `source.repos.read` permission to a repository, but does not have the `source.repos.list` permission on the project, the user cannot see the repository in the Repository view.

You can resolve this issue by granting the `source.repos.list` permission to the user on the project. Alternatively, the user can also access the repository through a direct hyperlink; however, the user can't search the repository without being granted the `source.repos.list` permission on the project.

## Cannot find newly-added project

If you just created a project, it can take a few minutes for the project information to update. Wait 10 minutes and refresh your browser. If the problem persists, please contact [support](https://docs.cloud.google.com/support).

## Contents of deleted repositories still visible

It can take a few minutes for deleted content to get removed from the user interface. Refreshing your browser should resolve this issue.

## Cannot locate commits

Cloud Source Repositories only displays the most recent commits during searches. To find older commits, use the [History panel](https://docs.cloud.google.com/source-repositories/docs/viewing-commit-changes#using_the_change_history_panel).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
