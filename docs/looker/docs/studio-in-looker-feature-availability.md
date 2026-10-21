---
url: https://docs.cloud.google.com/looker/docs/studio-in-looker-feature-availability/
title: Feature availability in Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:10:26.282850+00:00
---

# Feature availability in Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/studio-in-looker-feature-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Feature availability in Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

You can create a [Looker report](https://docs.cloud.google.com/looker/docs/glossary#report), [connect to data sources](https://docs.cloud.google.com/looker/docs/report-connectors) to visualize your data, and then save the report in Looker's content management system.

Although Looker reports are similar to Data Studio reports, some features and resources may not be available or may behave differently.

The following table indicates the features and functionality that are supported in Looker reports. This table lists only those features that are related to creating, viewing, editing, and sharing Looker reports.

Connect to data sources | Notes  
---|---  
Connect to Google Sheets | This data source is pre-set with [Owner's Credentials](https://docs.cloud.google.com/looker/docs/studio/data-credentials-article).  
Connect to Microsoft Excel |   
Connect to Looker | These data sources have the same limitations as are described in the [Looker connector documentation](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector).  
Connect to BigQuery | This data source is pre-set with [Owner's Credentials](https://docs.cloud.google.com/looker/docs/studio/data-credentials-article).  
Connect to Amazon Redshift |   
Connect to MySQL |   
Connect to PostgreSQL |   
Connect to File Upload |   
[Create an embedded data source](https://docs.cloud.google.com/looker/docs/studio/embedded-data-sources) |   
Add multiple data sources to a single report |   
[Blend](https://docs.cloud.google.com/looker/docs/studio/how-blends-work-in-looker-studio) up to five data sources |   
[Embed reports](https://docs.cloud.google.com/looker/docs/studio/embed-reports) | This feature requires Looker 25.10 or later.  
Perform actions within a report | Notes  
[View the version history of a report](https://docs.cloud.google.com/looker/docs/studio/see-whats-changed-in-reports-and-data-sources) |   
[Download a report as a PDF file](https://docs.cloud.google.com/looker/docs/download-charts-and-reports#download_entire_reports) |   
[Export data from a report chart to a CSV file, a Microsoft Excel file, or Google Sheets](https://docs.cloud.google.com/looker/docs/download-charts-and-reports#download_individual_charts) |   
Perform actions on a report | Notes  
[Save a report to your personal folder, to another user's personal folder, or to the Shared folder](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) |   
[View and open favorite reports from the Looker instance Home page, Favorites page, or Recently Viewed page](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage) |   
[Add or remove a report from the list of favorites](https://docs.cloud.google.com/looker/docs/finding-content#marking_content_as_a_favorite) |   
[Search for a report by report name](https://docs.cloud.google.com/looker/docs/studio-in-looker#from_looker_searcht) | This feature requires Looker 25.4 or later.  
[View a deleted report in the Trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) | This feature requires Looker 25.4 or later.  
[Restore a deleted report from the Trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) | This feature requires Looker 25.4 or later.  
Perform actions on a folder that contains a report | Notes  
[Copy, move, or delete a report from a folder](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) |   
[Add or remove users and groups from a shared folder that contains a report](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels) |   
Perform admin tasks that are related to reports | Notes  
[Manage the connectors that are allowed on a report](https://docs.cloud.google.com/looker/docs/studio-in-looker-connector-controls) | This feature requires Looker 25.4 or later.  
[Monitor user actions in reports alongside actions in Looker with System Activity](https://docs.cloud.google.com/looker/docs/studio-in-looker-system-activity) | This feature requires Looker 25.4 or later.  
[View report activity in a Looker instance's System Activity](https://docs.cloud.google.com/looker/docs/studio-in-looker-system-activity) | This feature requires Looker 25.4 or later.  
[Localization of certain user-interface (UI) text into supported languages](https://docs.cloud.google.com/looker/docs/supported-user-interface-languages) | This feature requires Looker 25.4 or later. It not available for the fr_FR locale.  
[Set the default locale for a Looker instance](https://docs.cloud.google.com/looker/docs/admin-panel-general-localization) | This feature requires Looker 25.4 or later.  
[Set the default number format for a Looker instance](https://docs.cloud.google.com/looker/docs/admin-panel-general-localization) | This feature requires Looker 25.4 or later.  
[Specify the locale for a user or a group](https://docs.cloud.google.com/looker/docs/model-localization#assigning_users_to_a_locale) | This feature requires Looker 25.4 or later.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
