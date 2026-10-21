---
url: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-hash-view/
title: Filter data in Hash view \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:04:16.278820+00:00
---

# Filter data in Hash view  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-hash-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filter data in Hash view

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Hash view lets you search and investigate files based on their hash value.

## Open Hash view

You can open Hash view the following ways:

  * Search for the file hash directly
  * Pivot to Hash view when viewing a process- or file-based event in Asset view



### Search for the file hash directly

To open Hash view directly:

  1. Enter the hash value in the Google Security Operations search field. Click **Search**.

  2. Select the hash value from the **Hashes** menu. Hash view is displayed.




### Navigate to Hash view from Asset view

You can also navigate to Hash view while investigating an asset in Asset view.

  1. Search for an asset and view it in Asset view. Asset view is displayed.

  2. From the **Timeline** tab to the left, scroll to any event tied to a process or file modification, such as PROCESS_LAUNCH.

**Note:** If you are not able to locate PROCESS_LAUNCH in the Event column, change the start-date on the top left corner to a few days previous to the present date. Also, slide the Time slider on the top right corner to 1 Day. Doing this will refresh the Timeline panel and display the other required events.
  3. Expand the file to view details and investigate.

  4. You can open Hash view for the file by clicking the hash value in Asset view. Hash view is displayed.




## Filter options in Hash view

The following Procedural Filtering options are available in Hash view:

  * ASSETS
  * EVENT TYPE
  * LOG SOURCE
  * PID
  * PROCESS NAME



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
