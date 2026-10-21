---
url: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-user-view/
title: Filter data in User view \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:39:54.047689+00:00
---

# Filter data in User view  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-user-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filter data in User view

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations User view lets you better understand how users within an enterprise might be impacted by security events. By focusing on the behavior of individual users, security administrators can search for activity indicating an account compromise or other security concern.

  1. To open User view, enter the username or email address of a user within your enterprise in the search field.

**Note:** If the user is present within your Google SecOps account, that user is displayed as a result.
  2. Click **SEARCH** to pivot to User view.

  3. Select the user from the **USERS** menu. User view is displayed.

  4. Click the right arrow in the Detections column in the left navigation panel.

  5. Click the ![Filter icon](https://docs.cloud.google.com/chronicle/images/filtering-icon-c.png) icon in the top right corner of the Google SecOps user interface to open the **Procedural Filtering** menu.

The following Procedural Filtering options are available in User view:

     * AUTH TYPE
     * EVENT TYPE
     * LOG SOURCE
     * OUTCOME
     * PRINCIPAL LOCATION
     * TARGET APPLICATION



## Summary of Visual elements in the view

Google Security Operations includes the following user interface elements to help you investigate any issues that might be present within your enterprise:

**Element** | **Description**  
---|---  
Time slider | The time slider allows you to adjust the time period under examination. You can adjust the slider to view between one minute and one day of events. Available only in: Asset view, IP Address view, Domain view, Hash view, User view, Rules Dashboard, Rules Editor.  
Prevalence | Prevalence measures the number of assets within your enterprise that have connected to a specific domain over the past seven days. Available only in: Asset view, IP Address view, Domain view, Hash view.  
**Right Navigation Panel**  
Expand all | Expands all the collapsed items.  
Collapse all | Collapses all the expanded items.  
Reset | Displays the default view and includes _All_ (there are exceptions).  
Show all | Includes all the items.  
Hide all | Excludes all the items.  
Include | Includes the excluded items. Hovering over the icon provides a preview in green.  
Exclude | Filters out the selected item. Hovering over the icon provides a preview in orange.  
Exclude others | FIlters out the other items except the selected item.  
**Left Navigation Panel**  
Expand all | Expands all the collapsed items.  
Collapse all | Collapses all the expanded items.  
Wrap text | Wraps text to the next line when it gets to the right margin, otherwise the text is displayed on one line only.  
Unwrap text | Unwrap text expands the text in one line only.  
Actions  | Download as CSV - Download the information in CSV format.  
Search rows | Provides an option to enter a keyword to search each row.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
