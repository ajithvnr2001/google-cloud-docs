---
url: https://docs.cloud.google.com/data-studio/upgrade-content-pro/
title: Upgrade Data Studio content to Data Studio Pro \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:39.266250+00:00
---

# Upgrade Data Studio content to Data Studio Pro  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/upgrade-content-pro/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Upgrade Data Studio content to Data Studio Pro Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for users and administrators whose organization has already [subscribed to Data Studio Pro](https://docs.cloud.google.com/data-studio/newsletter).

Upgrading your existing Data Studio reports to Data Studio Pro unlocks enterprise collaboration features for your team. You can upgrade content that was created by using the no-cost version of Data Studio to Data Studio Pro by following user or administrator workflows.

## User upgrades

Google recommends user upgrades for small deployments, such as individual team subscriptions or limited trials of Data Studio Pro. In a user upgrade, individual users in an organization choose the content that they want to upgrade and use the Data Studio Pro user interface to move their reports or data sources into either a team workspace or their personal **Sandbox**. After the upgrade, users can immediately use Data Studio Pro features.

Learn how to [move assets into folders in team workspaces](https://docs.cloud.google.com/data-studio/organize-assets-with-folders-in-team-workspaces#manage-assets-in-folders).

## Administrator upgrades

For large or enterprise deployments, Google recommends that an administrator lead the upgrade. In an administrator-led content move, a Google Workspace administrator in an organization sets a default Google Cloud project for Data Studio Pro. If users have a Pro subscription that's associated with that project, their content will be moved into their individual **Sandbox** locations under that project.

Learn how to [set a default Data Studio Pro project](https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro). Additionally, administrators can [prevent users from creating new Data Studio Pro departmental subscriptions](https://docs.cloud.google.com/data-studio/consolidate-multiple-pro-subscriptions#prevent-users-from-creating-new-pro-departmental-subscriptions).

**Note:** When users have a Data Studio Pro subscription that's associated with a default Pro project, they no longer have an **Owned by me** location. All new content that a user creates must be stored either in their **Sandbox** or in a [team workspace](https://docs.cloud.google.com/data-studio/about-team-workspaces).

## Additional notes about upgrading content to Data Studio Pro

Regardless of the upgrade method that you choose, the following information applies:

  * Upgrading existing content doesn't change that content's URL. Links to content continue to work as they did before the upgrade. People who already have view or edit permissions on the content won't lose access. There is no downtime during the upgrade.
  * Moving content won't disrupt access to the content. Users still have access to their reports and data sources during the move.
  * Users might gain access to the content as a result of permissions that are inherited through the IAM hierarchy. For example, if a user has the Data Studio Asset Viewer role in the Data Studio Pro project, they can view the upgraded content even if it isn't explicitly shared with them. Similarly, generic roles like Project Owner or Project Editor also grant access to the Data Studio Pro content.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
