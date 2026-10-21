---
url: https://docs.cloud.google.com/data-studio/report-publishing/
title: Report publishing \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:24:20.377922+00:00
---

# Report publishing  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/report-publishing/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Report publishing Stay organized with collections  Save and categorize content based on your preferences. 

Report publishing lets you control when viewers see the changes you make to a report. By default, viewers see changes in real-time. Report publishing lets editors work on a draft version of a report while viewers see the published version. When you're ready to let viewers see the new version, you can then publish it.

## Turn on report publishing for a report

To turn on report publishing for a report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **File > Publishing settings**.
  3. Turn on **report publishing**.



To let viewers see changes to the report as you make them, turn this option off.

## Publish changes

To publish a draft version, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the upper right, click **Publish**.
  3. In the confirmation dialog, click **Publish.**



## Switch between draft and published reports in view mode

Viewers can only see the published report. Report editors can see either the draft report or the published report in view mode.

To switch between draft and published reports, follow these steps:

  1. View the report.
  2. In the upper left, next to the report name, click the selector, then select the version you want to view.



![A user selects the Published option from the version button drop-down menu next to the report title, with the text Published version in the button.](https://docs.cloud.google.com/static/data-studio/images/view-draft-2021-02-22.png)

## How report publishing works

When you turn on report publishing, Data Studio publishes the current version of that report. Report editors can then work on the draft version until it's time to publish a new version. While you're editing the report, viewers only see the published version.

### Publishing and version history

Version history for manually published reports has 2 current versions: the current published version, and the current draft version. Anyone editing the report works on the current draft version.

You can use [version history](https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources) to publish or restore previous versions of the report:

  * When you **publish a previous version,** report viewers will see that version of the report. The current draft version won't change.

  * When you **restore a previous version** , that becomes the new draft version. The published version of your report doesn't change.




### Data source changes and report publishing

When report publishing is turned on, the following changes to the fields in an **embedded data source** won't appear to viewers until you publish the report:

  * Field name changes
  * Calculated field formula changes
  * Hiding or showing fields

**Important:** Similar edits to **reusable data sources** will appear in both the draft and published versions.

#### Other data source changes that bypass report publishing

In addition, if you make any of the following changes to a data source of either type, the effects will be visible in the published report:

#### Revoke data source credentials

Revoking the credentials on a data source used in the published version of the report will cause charts using that data source to show a "failed to get data" error in the published version.

#### Remove a data source from the report

Removing a data source used in the published version of the report will cause charts using that data source to show an "unknown data source" error in the published version.

#### Moving a data source to the Trash

Moving a data source used in the published version of the report to the Trash or deleting it forever will cause charts using that data source will return a "dataset configuration error" in the published version.

## Copy a report with report publishing turned on

The results of copying a report with report publishing turned on depends on your access to the report.

**For editors:**

  * The copy contains both the draft and published version. Report publishing remains on in the copy.



**For viewers:**

  * The copy only contains the published version of the report. The copy uses automatic publishing.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
