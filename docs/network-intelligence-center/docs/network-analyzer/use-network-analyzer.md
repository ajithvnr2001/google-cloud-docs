---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-network-analyzer/
title: Use Network Analyzer \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:29.241527+00:00
---

# Use Network Analyzer  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-network-analyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Use Network Analyzer Stay organized with collections  Save and categorize content based on your preferences. 

You can use Network Analyzer to view insight details, view categories of insights, query historical data, update the status of an insight, and rerun the analysis as needed.

## View insight details

The initial view of the Network Analyzer shows the **Summary** tab, with all insights visible by default. To view specific network insights, click the different category tabs.

###  Console 

  1. In the Google Cloud console, go to the **Network Analyzer** page.

[Go to Network Analyzer](https://console.cloud.google.com/net-intelligence/network-analyzer)

On the Network Analyzer page, you can see all the insights listed.

  2. To view the details of an insight, click **View** in the insight details column of any insight.



## Query historical data

By default, the **Network Analyzer** page shows the current active insights. You can query historical data based on the first reported time.

###  Console 

  1. In the Google Cloud console, go to the **Network Analyzer** page.

[Go to Network Analyzer](https://console.cloud.google.com/net-intelligence/network-analyzer)

  2. To query historical data, select a custom time range from the upper-right corner.



If you select a historical time range, the insights reported from that time range are displayed. Even if an insight currently exists in your project, if the **First report time** is outside the specified time range, such insight is not displayed.

## Dismiss an active insight

If you think that an active insight is an expected configuration or if the insight is not useful, you can dismiss the insight. An example of an expected configuration is a static route shadowing a dynamic route.

By default, only **Active** insights are shown on the Network Analyzer page. To view the dismissed insights, you can remove the filter of insight status.

The **Network insights** table lists all the insights and displays the status of each insight in the **Status** column.

###  Console 

  1. In the Google Cloud console, go to the **Network Analyzer** page.

[Go to Network Analyzer](https://console.cloud.google.com/net-intelligence/network-analyzer)

     * To dismiss an active insight, update the insight status from **Active** to **Dismissed** in the **Status** column.
     * On the insight details page, click **Dismiss** to change the status of the insight.
  2. Modify the status of an insight by changing the status back to **Active**.



## Update or rerun the insight

On the **Network Analyzer** page, the information displayed is precalculated. You can view when the analysis was run by checking the **Last run time**.

To view newly calculated insights after making a configuration change:

  * Wait for 10-20 minutes for the updated information to display.
  * Verify if the **Last run time** is after the time you made the configuration change.
  * Regenerate insights by clicking **Update**.



When you click **Update** , Network Analyzer performs the analysis again. When the analysis is generated, the updated analysis details are displayed. The **last run time** indicates whether the page is showing the updated insights or old details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
