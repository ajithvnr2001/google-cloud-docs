---
url: https://docs.cloud.google.com/looker/docs/download-charts-and-reports/
title: Download Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:06:40.960383+00:00
---

# Download Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/download-charts-and-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Download Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

This page guides you through the components of downloading Looker reports. You can download individual charts in CSV or Excel format and entire reports in PDF format. Read the following sections to learn about these concepts:

  * Requirements
  * Things to know about downloading charts and reports
  * Download individual charts
  * Download entire reports



## Requirements

To download charts and reports, users must have either the [Looker **Admin** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) or the following content and data access:

  * One of the following types of access to the folder in which a report is saved: 
    * View
    * Manage Access, Edit
    * The [`download_with_limit` or `download_without_limit` permission](https://docs.cloud.google.com/looker/docs/overview-of-studio-in-looker-permissions)
  * Access to the underlying [LookML model](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets), if a chart or report includes a Looker data source



For more information about content access and permissions, see [Controlling user content access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_user_content_access) and [How content access and permissions interact](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#how_content_access_and_permissions_interact).

If you want to change the access level settings for a folder, see [Viewing and managing folder access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels).

## Things to know about downloading charts and reports

There are several things to know about downloading charts and reports in Looker:

  * Individual charts can be downloaded only in CSV or Excel style formats.
  * Entire reports can be downloaded only in PDF format.
  * The limit for data downloads for users, including those with the `download_without_limit` permission, is 5,000 rows.
  * When a report link is included in a downloaded PDF, users will be directed to that specific report within Looker. Users _must_ have access to the folder in which the report is saved to view the report in Looker.
  * If a user is not granted the required permissions, they won't see the option to download content.
  * If a user does not have the required model access to Looker data on a report, that data won't be included in downloads.



## Download individual charts

To download content from an individual chart in CSV or Excel format, follow these steps:

  1. Open the report that contains the data that you want to download.
  2. Click the chart's more_vert three-dot menu.
  3. Click **Export** to open the **Export data** dialog.
  4. In the **Export data** dialog, enter a name for the download in the **Name** field.
  5. Choose an option in the **Export as** section. The options include the following:

     * CSV
     * CSV (Excel)
     * Google Sheets

**Important:** Users will see the **Google Sheets** export option only if they are logged in to the instance with the Google OAuth authentication method.
  6. Click the check_box **Keep value formatting** checkbox to carry over the value format settings from the chart to the exported file.

  7. Click **Export** to export the file, or click **Cancel** to close the dialog.




## Download entire reports

To download an entire report as a PDF, follow these steps:

  1. Open the report that contains the data that you want to download.
  2. Click group_add **Share** in the report banner.
  3. Click download **Download** to open the **Download as PDF** dialog.
  4. Click the check_box checkboxes to enable or disable the following export settings:

     * **Ignore custom background color** : Select this option to override any background color settings on the report.
     * **Add a link back to the report** : Select this option to include a link to the report in Looker. See the Things to know about downloading charts and reports section on this page for more information about including links in downloads.
     * **Password protect report** : Select this option to set a password for the PDF file.
**Note:** The name of the report will be the name of the PDF file.
  5. Click **Download** to download the PDF, or click **Cancel** to close the dialog.


**Note:** If a report contains data from a Looker data source, and you do _not_ not have the required model access to the Looker data on the report, you will see a note in the **Download as PDF** dialog that those visualizations will be excluded from the PDF.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
