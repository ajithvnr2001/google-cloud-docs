---
url: https://docs.cloud.google.com/data-studio/delete-a-data-source/
title: Delete a data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:26.108115+00:00
---

# Delete a data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/delete-a-data-source/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Delete a data source Stay organized with collections  Save and categorize content based on your preferences. 

In Data Studio, you can remove, delete, and restore data sources to manage your reports and maintain data integrity. Removing a data source disconnects it from your reports, while deleting a reusable data source permanently removes it from Data Studio.

## Remove a data source from a report

If embedded and reusable data sources are no longer needed, you can remove them from your reports by following these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **Resource** ![and then](https://docs.cloud.google.com/static/data-studio/images/and-then-2019-11-26.png)**Manage added data sources**.
  3. Locate the data source in the list.
  4. To the right, click **REMOVE** ![Remove.](https://docs.cloud.google.com/static/data-studio/images/deletegoogblue2x48dp-2020-09-22.png).



## Effects of removing a data source

When you remove a data source from a report, note the following effects:

  * Any report components that use the data source display a "Configuration incomplete" error. To fix this error, add a new data source to the component.
  * Removing a reusable data source from a report doesn't affect other reports that use that data source and doesn't move the data source to the Trash.
  * Removing an embedded data source disconnects it from the report but doesn't permanently delete the data source. Data Studio permanently deletes embedded data sources only when you permanently delete the parent report. To permanently delete an embedded data source without deleting the report, you can [convert the embedded data source to a reusable data source](https://docs.cloud.google.com/data-studio/embedded-data-sources#delete-an-embedded-data-source) and then delete it.



## Move reusable data sources to the Trash

You can remove one data source or multiple data sources at once.

Moving a data source to the Trash also removes the data source from any reports that use it.

### Move a single reusable data source to the Trash

**Caution:** If you move a data source to the trash and that data source is connected to one or more reports, Data Studio won't display a warning. Data Studio will label the data source as `(Unknown)` in these reports. Use the [**Manage Added Reports**](https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources) option to see the reports that use a given data source before you remove that data source.

To remove a reusable data source from the home page list, follow these steps to move it to the Trash:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the [DATA SOURCES](https://datastudio.google.com/navigation/datasources) tab.
  3. Locate the data source that you want to remove.
  4. Hover over the data source name. Then, on the right, click **More options** ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png).
  5. Click **Remove** ![Remove.](https://docs.cloud.google.com/static/data-studio/images/deletegrey6002x48dp-2020-09-22.png).



### Move multiple reusable data sources to the Trash

To remove multiple reusable data sources from the home page list at once, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Locate the data sources that you want to remove.
  3. To select multiple adjacent data sources, hold down the Shift key and click the data sources. To select multiple non-adjacent data sources, hold down the Ctrl key (PC) or the command key (Mac) and click the data sources.
  4. Click **Trash selected items** ![Remove.](https://docs.cloud.google.com/static/data-studio/images/deletegrey6002x48dp-2020-09-22.png).
  5. In the **Move items to the trash?** dialog, click **Confirm** to move the data sources to the Trash.



### Permanently delete a reusable data source

Data sources in the Trash remain undeleted unless you permanently delete them. You need to own the data source to delete it.

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the [DATA SOURCES](https://datastudio.google.com/navigation/datasources) tab.
  3. On the left, select **TRASH**.
  4. Locate the data source that you want to delete, and then click **Options** ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png).
  5. Click **Delete forever** ![Remove.](https://docs.cloud.google.com/static/data-studio/images/deletegrey6002x48dp-2020-09-22.png).

**Warning:** You can't undo this action. 

## Restore a reusable data source

You can restore items that are in the Trash. Restoring a reusable data source adds it back to any reports to which it had been previously added. To restore a reusable data source, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the [DATA SOURCES](https://datastudio.google.com/navigation/datasources) tab.
  3. On the left, select **TRASH**.
  4. Locate the data source that you want to restore, and then click the options menu ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png).
  5. Click **Restore** ![Restore.](https://docs.cloud.google.com/static/data-studio/images/restoregrey6002x48dp-2020-09-22.png).



### Version history and deleted data sources

You can't use version history to restore any data sources that have been permanently deleted.

## Related resources

  * [Delete a report](https://docs.cloud.google.com/data-studio/delete-a-report)
  * [Manage added reports and data sources](https://docs.cloud.google.com/data-studio/manage-added-reports-and-data-sources)
  * [Version history](https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources)
  * [Embedded data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
