---
url: https://docs.cloud.google.com/looker/docs/best-practices/delete-user-data/
title: How to delete your data from Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:02.527297+00:00
---

# How to delete your data from Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/delete-user-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  How to delete your data from Looker Stay organized with collections  Save and categorize content based on your preferences. 

Your Looker admin can [delete your Looker account](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#deleting-users) at any time. If you request that your account be deleted and then change your mind, be aware that certain content cannot be recovered.

**Note:** Looker accounts are not shared across Looker instances. If you have Looker accounts on multiple Looker instances, contact your Looker admin for each Looker instance to delete your account.

## Step 1: Learn what deleting your Looker account means

When your Looker account is deleted, the following content will be **immediately lost** :

  * Schedules that you have created will be deleted.
  * Schedules that other users created on Looks and dashboards in your personal folder will be deleted.
  * Alerts that you have created will be deleted.
  * Your records in the [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) will be deleted. 
    * Caveat: The filter suggestions for the **User Name** field remain cached until six hours after your account is deleted.



The following content **may be recoverable** if you change your mind later:

  * Looks and dashboards in your personal folder will be moved to the [Trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) folder. If a Looker admin empties the Trash, the content won't be recoverable.



The following content **will be retained** even after your Looker account is deleted:

  * Looks and dashboards that you saved to a Shared folder won't be deleted.
  * Schedules that other users created that list you as a recipient will continue to be sent to you, as long as that user can [schedule content to external recipients](https://docs.cloud.google.com/looker/docs/configuring-deliveries#delivery_permissions_for_destinations).
  * [Boards](https://docs.cloud.google.com/looker/docs/presenting-content) that you created will still exist.



See the [Removing user access](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#removing_user_access) section of the Admin settings - Users page for more information about the effects of disabling or deleting users.

## Step 2: Delete your Looker account

To delete your Looker account, follow these steps:

  1. Contact your Looker admin and request that they [delete your Looker account](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#deleting-users).
  2. If you have accounts on multiple Looker instances, contact the appropriate Looker admin for each Looker instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
