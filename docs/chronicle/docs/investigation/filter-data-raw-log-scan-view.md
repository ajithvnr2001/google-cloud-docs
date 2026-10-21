---
url: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-raw-log-scan-view/
title: Filter data in raw log search \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:21:33.003124+00:00
---

# Filter data in raw log search  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-raw-log-scan-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filter data in raw log search

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains the available methods for filtering raw logs using the **Search** bar, which you can access on the landing page or the dedicated **Search** page.

Choose one of the following methods:

## Use the `raw=` format

When using the `raw=` format, use these parameters to filter raw logs:

  * `parsed`: Filters logs based on their parsing status.

    * `parsed=true`: Returns only parsed logs.
    * `parsed=false`: Returns only unparsed logs.
  * `log_source=IN["log_source_name1", "log_source_name2"]`: Filters by log type.




### How to find unparsed raw logs

Unparsed logs don't generate UDM records. You can't query them using UDM fields (such as `metadata.log_type = "UNPARSED"`). To search for unparsed logs:

  1. In the Google SecOps console, go to **Investigation** > **SIEM Search**.
  2. In the search box menu, change the search mode from **UDM Search** to **Raw Log Search**.
  3. Select your target time range (for example, **Past 1 hour** or **Past 24 hours**).
  4. Query for unparsed logs using the `parsed = false` filter:
         
         raw = /.+/ parsed = false
         

To target specific feed log types, combine `parsed = false` with `log_source`:
         
         raw = /.+/ parsed = false log_source IN ["CUSTOM_JSON", "OKTA"]
         




## Use the Raw log search prompt (legacy method)

To use the **Raw Log Search** prompt to filter raw logs, do the following:

  1. On the search bar, enter your search string or regular expressions, and then click **Search**.

  2. In the menu, select **Raw Log Search** to display the search options.

  3. Specify the **Start Time** and **End Time** (the default is 1 week) and click **Search**.

The **Raw Log Search** view displays raw data events. You can filter results by `DNS`, `Webproxy`, `EDR`, and `Alert`. Note: These filters don't apply to event types, such as `GENERIC`, `EMAIL`, and `USER`.




You can use regular expressions to search for and match sets of character strings within your security data using Google SecOps. Regular expressions let you narrow your search down using fragments of information, as opposed to using a complete domain name, for example.

The following **Procedural Filtering** options are available in the **Raw Log Search** view:

  * **Product Event Type**

There are known inconsistencies between how events are displayed across views in the SecOps Console legacy **Raw Log Search** page:  
● **Raw Log** view:  
Displays the **Event type** based on the raw `event_log_type` value.  
For example `FILE_COPY`.  
● **UDM event fields** view:  
Displays the `metadata.event_type` field based on the `event_log_type` value.  
For example `FILE_COPY`.  
● **Procedural Filtering** view:  
Displays the **Event type** field based on the `network.application_protocol` value.  
For example `DNS`.  


    * **Log Source**
  * **Network Connection Status**

  * **TLD**




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
