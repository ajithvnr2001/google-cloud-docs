---
url: https://docs.cloud.google.com/data-studio/transfer-ownership/
title: Transfer ownership \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:57.858637+00:00
---

# Transfer ownership  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/transfer-ownership/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Transfer ownership Stay organized with collections  Save and categorize content based on your preferences. 

When team members change roles or leave your organization, you can transfer ownership of your Data Studio reports and data sources to another user. Reassigning ownership helps your team maintain uninterrupted access to critical dashboards and analytics assets.

## Transfer ownership of no-cost Data Studio assets

When you create a report or data source in the no-cost version of Data Studio, you own that asset. You can transfer ownership of your Data Studio assets to any user with a Google Account by using the **Manage access** options in the sharing dialog.

### Before you begin

Before you can make someone else the owner of an asset, you must first [share that asset with the new intended owner](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports). You can assign the intended owner either the **Editor** or **Viewer** role.

You can share a reusable data source only when you are editing it directly, not when editing the data source from within a report.

Once the new owner is assigned, you won't be able to transfer ownership again, even back to yourself. So be sure to that you select the correct user's address in the following steps.

### How to change ownership

To make someone else the owner of a Data Studio asset, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. View or edit the asset that you want to share.
  3. Click person_add **Share** to open the **Share with people and groups** dialog.
  4. Click the role drop-down next to the person to whom you want to transfer ownership, and then click **Make owner**.
  5. Click **Yes** to confirm the transfer. It may take a few minutes for the transfer to complete.



### After you transfer ownership

Once the ownership transfer is completed, you'll still be able to edit the asset, unless the new owner removes your access.

### Transfer a data source

When you transfer ownership of a data source, the data credentials remain intact. This ensures that data sources that use Owner's credentials will continue to provide data to reports as they did before the transfer. The new owner can change the credentials to use their credentials by reconnecting the data source.

You can manually [revoke your credentials](https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources) after the transfer. The new owner will need to reconnect the data source to use their own credentials to access data.

## Transfer ownership of Data Studio Pro assets

Data Studio Pro content belongs to an organization rather than to an individual user. To avoid Data Studio Pro content becoming inaccessible when team members leave your organization, we recommend using [Team Workspaces](https://docs.cloud.google.com/data-studio/team-workspaces).

When someone leaves your organization, Google Workspace and Cloud Identity administrators can transfer that user's Data Studio reports and data sources to another user in your organization to ensure that you don't lose access to important information. [Learn more in Google Workspace Admin Help.](https://support.google.com/a/answer/33314)

For more information about how to remove users from a Pro subscription, see [Edit a Pro subscription](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription).

## Limits of ownership transfer

Transferring ownership of Data Studio assets is subject to the following limits:

### File upload data sources

You can't transfer ownership of [CSV file upload data sources](https://docs.cloud.google.com/data-studio/upload-csv-files) to another user. File upload data sources must be recreated by the new owner.

### Transfer limits for Google Workspace and Cloud Identity organizations

You can transfer ownership only within your domain. For Google Workspace and Cloud Identity users, this means transferring ownership to another person in your organization. For standard (non-Google Workspace/Cloud Identity) users, this means transferring ownership to another standard user.

For users of the no-cost version of Data Studio, assets belonging to deleted users are **permanently deleted after 20 days**. To avoid losing data, if a user account has been deleted without transferring Data Studio assets, you must transfer ownership of these assets **within 20 days** of the user's deletion by following these steps:

  1. As a Google Workspace administrator, [restore the deleted user account](https://support.google.com/a/answer/1397578).
  2. After verifying that the user's account and data have been restored, initiate the [user deletion process](https://knowledge.workspace.google.com/admin/users/delete-or-remove-a-user-from-your-organization) in the Google Workspace Admin console.
  3. When you're prompted to transfer the user's data, in the **Data in other apps** section, follow these steps: 
     1. Select **Transfer**.
     2. Enter the new owner's email address.
     3. Select **Data Studio**.
     4. (Optionally) Select **Include assets that are not shared with anyone**.

**Warning:** All data not transferred within 20 days will be deleted.

## Related resources

  * [Edit the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection)
  * [Team workspaces for Data Studio Pro](https://docs.cloud.google.com/data-studio/team-workspaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
