---
url: https://docs.cloud.google.com/looker/docs/troubleshooting-looker-reports/
title: Troubleshooting Looker report errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:51:15.220709+00:00
---

# Troubleshooting Looker report errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/troubleshooting-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Troubleshooting Looker report errors Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

If you encounter issues while using Looker reports, refer to the following table for potential solutions. If you encounter an unexpected error that isn't listed in the following table, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).

**Error message** | **Possible cause** | **Possible solution**  
---|---|---  
Can't save report. The selected folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to save a report to a folder that is too deeply nested.  | Choose a folder that is 5 or fewer levels deep.   
Can't save a report to a folder with custom access. Select a folder without custom access.  | You are trying to save a report to a [folder with a custom list of users](https://docs.cloud.google.com/looker/docs/organizing-spaces).  | Select a folder that doesn't provide access to a custom list of users.   
There was a problem saving the report(s).  | An unexpected error occurred while saving the report or reports.  | Try saving the report or reports again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't move a report to a folder with custom access. Select a folder without custom access.  | You are trying to move a report to a [folder with a custom list of users](https://docs.cloud.google.com/looker/docs/organizing-spaces).  | Select a folder that doesn't provide access to a custom list of users.   
Can't move a report to the same folder.  | You are trying to move a report to the folder that it's already in.  | Choose a different destination folder.   
Can't move `_number_` out of `_total_` reports.  | Some reports couldn't be moved because an error occurred.  | Try moving the reports again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
There was a problem moving the report(s).  | An unexpected error occurred while moving the report or reports.  | Try moving the report or reports again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't copy report. The selected folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to copy a report to a folder that is too deeply nested.  | Choose a folder that is 5 or fewer levels deep.   
Can't copy a report to a folder with custom access. Select a folder without custom access.  | You are trying to copy a report to a [folder with a custom list of users](https://docs.cloud.google.com/looker/docs/organizing-spaces).  | Select a folder that doesn't provide access to a custom list of users.   
Can't copy `_number_` out of `_total_` reports.  | Some reports couldn't be copied because an error occurred.  | Try copying the reports again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't copy `_number_` out of `_total_` reports. `_number_` of these reports have a restricted datasource. Contact your admin for more details.  | Some reports couldn't be copied because a report datasource was unavailable.  | This error will occur if a connector that provides a datasource to the report has been disabled. Request that your Looker admin [enable the connector](https://docs.cloud.google.com/looker/docs/report-connectors).   
There was a problem copying the report(s).  | An unexpected error occurred while copying the report or reports.  | Try copying the report or reports again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
There was a problem renaming the report.  | An unexpected error occurred while renaming the report.  | Try renaming the report again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't add report to favorites.  | An error occurred while adding the report to your favorites.  | Try adding the report to your favorites again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't remove report from favorites.  | An error occurred while removing the report from your favorites.  | Try removing the report from your favorites again. If the issue persists, contact [Looker Support](https://console.cloud.google.com/support/?_ga=2.251036998.-1700953642.1728501588).   
Can't move folder. The selected folder contains reports and the destination folder is more than 5 levels deep. Choose a folder that's 5 or fewer levels deep.  | You are trying to move a folder to a destination that is too deeply nested.  | Choose a destination folder that is 5 or fewer levels deep.   
Can't move folder. The selected folder contains reports and the destination folder has custom access. Select a folder without custom access.  | You are trying to move a folder to a [destination folder with a custom list of users](https://docs.cloud.google.com/looker/docs/organizing-spaces).  | Select a destination folder that doesn't provide access to a custom list of users.   
Can't add user(s). Users must also have access to the parent folder.  | You are trying to add a user to a subfolder, but the user doesn't have access to the parent folder.  | Confirm that the user has [access to the parent folder ](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels)before adding them to the subfolder.   
Can't set custom access to this folder. A folder that contains reports can only inherit access permissions from the top-level folder. Grant the users or groups access to the top-level folder and try again.  | You are trying to specify a custom list of users or groups for a folder that contains reports.  | Grant the users or groups access to the appropriate top-level folder, such as the **Shared** **folders** folder.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
