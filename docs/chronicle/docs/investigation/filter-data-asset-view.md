---
url: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-asset-view/
title: Filter data in Asset view \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:45:21.330504+00:00
---

# Filter data in Asset view  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-asset-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filter data in Asset view

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Asset view lets you to investigate assets within your enterprise and whether or not they have interacted with suspicious domains. You can adjust Asset view to hide benign activity and help highlight the data relevant to an investigation.

Complete the following steps to navigate to Asset view page:

  1. Enter the asset (ending with a known public suffix) or URL you need to investigate in the search bar at the top of the user interface. Click **SEARCH**.

  2. Select the asset from the **ASSETS** drop-down menu. Asset view is displayed.

  3. Click the ![Filtering Icon](https://docs.cloud.google.com/chronicle/images/filtering-icon-c.png) icon in the top right corner of the Google Security Operations user interface. The **Procedural Filtering** menu opens. Procedural Filtering lets you to further filter information pertaining to an asset, including by event type, log source, network connection status, and Top Level Domain (TLD).

The following Procedural Filtering options are available in Asset view:

     * EVENT TYPE
     * LOG SOURCE
     * NETWORK CONNECTION STATUS
     * TLD



## Navigate Asset view

The asset view has the following components.

### Prevalence

Prevalence measures the number of assets within your enterprise connected to a specific domain over the past seven days. More assets connecting to a domain means that the domain has greater prevalence within your enterprise. High prevalence domains, such as google.com, are unlikely to require investigation. You can use the Prevalence slider to filter out the high prevalence domains and focus on the domains which fewer assets across your enterprise have accessed. The minimum Prevalence value is 1, meaning you could focus on the domains which are linked to a single asset within your enterprise. The maximum value varies depending on the number of assets you have within your enterprise.

Google SecOps provides a graphical representation of the historical prevalence of a given FQDN and its TLD. This graph can be used to determine whether the domain has been accessed from within the enterprise before, and can provide an indication of whether the domain is associated with a particular campaign targeting the enterprise. Typically, less prevalent domains, ones that fewer assets have connected to, might represent a greater threat to your enterprise.

### Time slider

The time slider lets you to adjust the time period under examination. You can adjust the slider to view between one minute and one day of events (you can also adjust this using the scroll wheel of your mouse over the Prevalence Graph). Domains that more assets have accessed are displayed as more prevalent in Asset view.

### Timeline tab

Selecting an event in the Timeline tab also highlights the corresponding event in the Gradient Heat Map in green. Alerts are indicated by a red triangle and red text.

### Asset tab

Selecting an asset highlights it in green in the Asset tab and all activity involving that asset is also highlighted in green on the Gradient Heat Map. You can pivot to Asset view by clicking on first accessed or last accessed in the Assets tab.

### TIMELINE Sidebar List

When you search for an asset, activity is returned with a default time window of 2 hours. Hovering over the header categories row displays the sorting control for each column, enabling you to sort alphabetically or by time depending on the category. Adjust the time window using the time slider or by scrolling the mouse wheel while the cursor is over the Prevalence Graph.

### DOMAINS sidebar list

Use this list to see the first lookup of each distinct domain within a given time window. This helps to hide noise caused by assets frequently connecting to domains.

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
