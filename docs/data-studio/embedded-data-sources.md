---
url: https://docs.cloud.google.com/data-studio/embedded-data-sources/
title: Embedded data sources \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:21.451552+00:00
---

# Embedded data sources  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/embedded-data-sources/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Embedded data sources Stay organized with collections  Save and categorize content based on your preferences. 

In Data Studio, new data sources that you create while editing a report are embedded directly in that report. Embedded data sources move with the report when you share or copy it, allowing editors to manage data connections together without managing separate assets. You can also convert embedded data sources to standalone, reusable data sources.

## Embedded versus reusable data sources

Data sources can be either _embedded_ or _reusable._ Reports can include both embedded and reusable data sources.

**Data sources that you create while editing a report are embedded** in the report. To edit an embedded data source, you do so within that report. Embedded data sources make collaborating on reports and data sources easier. Anyone who can edit the report can also edit the data source as well as modify its connection. When you share or copy the report, any embedded data sources are shared or copied as well.

**Data sources that you create from the home page are reusable**. You can reuse these data sources in different reports. Reusable data sources let you create and share a consistent data model across your organization. Only people with whom you share the reusable data source can edit it. Only the owner of the data source's credentials can modify the connection.

### Benefits of embedded data sources

When you share or copy a report, all its embedded data sources are shared or copied along with it. You don't need to share the data sources separately. Having your data sources embedded in the report reduces the number of assets you need to manage, since all your data sources can be contained by a single report.

> #### Data governance and embedded data sources
> 
> While embedded data sources simplify collaboration, they can also let viewers access potentially sensitive data and metadata. If you are concerned about strictly controlling access to data and metadata, consider either hiding or removing unused fields from the embedded data source or using reusable data sources in your reports.
> 
> [Learn more about data governance in Data Studio](https://docs.cloud.google.com/data-studio/data-governance-in-an-overview).

## How to tell if a data source is embedded or reusable

If you can see the data source in the Data Sources list on the home page, then it's reusable.

While editing a report, in the menu, click **Resources > Manage added data sources**. You'll see the type displayed in the first column.

![The Data sources panel displays the Name and Type \(Reusable, Embedded, etc.\)  of data sources for a report.](https://docs.cloud.google.com/static/data-studio/images/data-source-types-2020-08-12.png)

## Edit an embedded data source

Anyone who can edit a report can [edit its embedded data sources](https://docs.cloud.google.com/data-studio/edit-a-data-source).

## Share reports that contain embedded data sources

The type of data source makes no difference when you share a report with view access. Whether they are embedded or reusable, [data credentials](https://docs.cloud.google.com/data-studio/data-credentials) control who can view the data in the report.

When you share a report with edit access, those people with whom you share can use any embedded data source you've added to modify the report. Report editors can also [modify the embedded data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).

## Convert an embedded data source to a reusable data source

**Important:** You must own the data credentials for an embedded data source in order to make it reusable.

Making an embedded data source reusable lets you manage the data source as a separate asset. By default, editors of the current report will be able to edit the new reusable data source, but you can turn off that option during the copy process.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menu, click **Resources > Manage added data sources**.
  3. Locate the embedded data source, and then, on the right, click **Make reusable**.

**Note:** It's not possible to convert an existing reusable data source into an embedded data source.

## Copy a report with an embedded data source

When you copy a report with embedded data sources, the copy includes those data sources. Copying a report doesn't copy reusable data sources that were added to the report.

If an embedded data source uses Owner's credentials but the person who copies the report is not the owner of those credentials, that data source isn't copied. Charts in the copy that are based on that data source will show an error asking you to fix the missing data source.

> You can copy an embedded data source within a report:
> 
>   1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
>   2. In the menu, select **Resources > Manage added data sources.**
>   3. Locate the data source, then click **Copy.**
> 


## Delete an embedded data source

When you remove an embedded data source from a report, Data Studio disconnects the data source from the report. Removing an embedded data source doesn't permanently delete it.

After removal, embedded data sources stay with the report so that earlier versions in version history and undo actions continue to work. Data Studio permanently deletes embedded data sources only when you permanently delete the parent report.

You can't delete an individual embedded data source directly from a report; however, you can permanently delete an embedded data source if you convert it to a reusable data source first.

### Permanently delete an embedded data source for data compliance

If your organization has data retention or compliance requirements that require you to permanently delete an embedded data source without deleting the report, follow these steps to convert the data source to a reusable data source and then delete it.

**Note:** You must own the data credentials for an embedded data source in order to make it reusable. Making an embedded data source reusable is permanent and can't be undone.

#### Delete a data source from the current version of the report

If the data source is still added to the report, follow these steps to delete the data source:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menu, click **Resource > Manage added data sources**.
  3. Find the embedded data source, and then click **Make reusable**.
  4. In the confirmation dialog that appears, click **Make reusable**.
  5. In the **Manage added data sources** panel, click **Remove**.
  6. In the confirmation dialog that appears, click **Remove data source**.
  7. Click **Close**.
  8. Open the [Data Studio home page](https://datastudio.google.com).
  9. On the **Data Sources** tab, find the data source, click the three-dot menu, and then click **Remove**.
  10. Open the Trash, find the data source, click the **three-dot menu** , and then click **Delete forever**.
  11. In the confirmation dialog that appears, click **Delete forever** again.



#### Delete a data source that was removed from a previous version of the report

If you've already removed the data source from the current version of the report, follow these steps to delete the data source:

**Tip:** To help you identify the current version of your report, you can name it by selecting **File > Version history > Name current version** before proceeding with these steps. For example, name the version "Latest" or "Current".

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **File > Version history > See version history**.
  3. Select an earlier version of the report where the data source is still added, and then click **Restore this version**.
  4. In the confirmation dialog that appears, click **Restore**.
  5. In the menu, click **Resource > Manage added data sources**.
  6. Find the embedded data source, and then click **Make reusable**.
  7. In the confirmation dialog that appears, click **Make reusable**.
  8. In the **Manage added data sources** panel, click **Remove**.
  9. In the confirmation dialog that appears, click **Remove data source**.
  10. Click **Close**.
  11. **Important:** To restore the report to its original state, select **File > Version history > See version history** again.
  12. Select the latest version of the report, and then click **Restore this version**.
  13. Open the [Data Studio home page](https://datastudio.google.com).
  14. On the **Data Sources** tab, find the data source, click the three-dot menu and then click **Remove**.
  15. Open the Trash, find the data source, click the **three-dot menu** , and then click **Delete forever**.
  16. In the confirmation dialog that appears, click **Remove data source**.



## Version history and embedded data sources

Version history for embedded data source is included in the report's version history. To restore a previous version of your embedded data source:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **File > See version history**.
  3. Select an earlier version of the report, and then click **Restore this version**.



## Field editing in reports

Report editors can always modify field definitions in charts that connect to embedded data sources. The **Field Editing in Reports** option, which lets data source owners manage field editing in reports, is available only for reusable data sources.

[Learn more about editing fields in your reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
