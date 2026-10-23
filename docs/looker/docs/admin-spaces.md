---
url: https://docs.cloud.google.com/looker/docs/admin-spaces/
title: Deleted and unused content for admins \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:02.121376+00:00
---

# Deleted and unused content for admins  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-spaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Deleted and unused content for admins Stay organized with collections  Save and categorize content based on your preferences. 

Looker offers admins several folders for managing unused and unwanted content. The **Unused content** and **Trash** folders are located under the **Folders** item in the [main navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).

You should periodically go through these folders to delete content that isn't needed.

## Unused content

The **Unused content** folder lists dashboards and Looks that haven't been viewed within the past 90 days, or within a time range that you can specify.

To learn more about managing content in the **Unused content** folder, see the [Managing unused content](https://docs.cloud.google.com/looker/docs/manage-unused-content) page.

## Trash

**Note:** Only Looker admins can see the **Trash** folder.

The **Trash** folder shows you any dashboards or Looks that were deleted by users (these dashboards and Looks are also called "soft-deleted"). You can select any number of dashboards and Looks, and then choose what to do with them — permanently delete them or restore them. You can also sort the thumbnails by using the **Sort by** drop-down menu in the top right of each section.

To restore or permanently delete content, follow these steps:

  1. Select the dashboards and Looks that you want to restore or permanently delete: 
     * Select all dashboards or all Looks in the **Dashboards** or **Looks** section of the list using the **Select All** button and then the **Select all x Looks** or **All x dashboards** option that appears.
     * Select individual dashboards or Looks by using the checkbox in the same row.
  2. Click the **Restore** button to move the selected content back to folders. Or click the **Delete** button to _permanently_ delete the content. Deleting content here cannot be undone.



Alternatively, to delete **all** Looks and dashboards from the list, click the **Delete All** button at the top of the page. Any schedules or alerts that are affiliated with a dashboard or Look will also be deleted. The alert or schedule owner will see immediately that the name of the dashboard has been deleted for the alert on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) or for the schedule on [**Schedules You've Created** user page](https://docs.cloud.google.com/looker/docs/user-schedules) in Looker. After the next time the alert or schedule query runs, its status will show as **Disabled**.

**Tip:** You can also use the Looker API to permanently delete [Looks](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/delete_look), [dashboards](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/delete_dashboard), and [entire folders](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Folder/delete_folder).

If you restore a dashboard or a Look, it will return to the folder that it was deleted from, _if_ that folder still exists. Otherwise, the content will be saved to the folder of the admin who restores the content.

Content in the **Trash** folder does not expire and will remain until you restore or permanently delete it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
