---
url: https://docs.cloud.google.com/bigquery/docs/play-transformation/
title: Google Play report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:06.777642+00:00
---

# Google Play report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/play-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Play report transformation

When your Google Play reports are transferred to BigQuery, the reports are transformed into the following BigQuery tables and views.

When you view the tables and views in BigQuery, the value for suffix is the table suffix you configured when you created the transfer.

Google Play report | BigQuery table | BigQuery view  
---|---|---  
**Detailed Reports** |  |   
**_Reviews_** |  |   
[Reviews](https://support.google.com/googleplay/android-developer/answer/6135870#reviews) | p_Reviews_suffix | Reviews_suffix  
**_Financial Reports_** |  |   
[Estimated Sales](https://support.google.com/googleplay/android-developer/answer/6135870#financial) | p_Sales_suffix | Sales_suffix  
[Earnings](https://support.google.com/googleplay/android-developer/answer/6135870#financial) | p_Earnings_suffix | Earnings_suffix  
[Korean Play balance funded](https://support.google.com/googleplay/android-developer/answer/6135870#financial) | p_Korean_Play_balance_funded_suffix | Korean_Play_balance_funded_suffix  
**Aggregated Reports** |  |   
**_Statistics_** |  |   
[Installs](https://support.google.com/googleplay/android-developer/answer/6135870#statistics) | p_Installs_app_version_suffix  
p_Installs_carrier_suffix  
p_Installs_country_suffix  
p_Installs_device_suffix  
p_Installs_language_suffix  
p_Installs_os_version_suffix | Installs_app_version_suffix  
Installs_carrier_suffix  
Installs_country_suffix  
Installs_device_suffix  
Installs_language_suffix  
Installs_os_version_suffix  
[Crashes](https://support.google.com/googleplay/android-developer/answer/6135870#statistics) | p_Crashes_app_version_suffix  
p_Crashes_device_suffix  
p_Crashes_os_version_suffix | Crashes_app_version_suffix  
Crashes_device_suffix  
Crashes_os_version_suffix  
[Ratings](https://support.google.com/googleplay/android-developer/answer/6135870#statistics) | p_Ratings_app_version_suffix  
p_Ratings_carrier_suffix  
p_Ratings_country_suffix  
p_Ratings_device_suffix  
p_Ratings_language_suffix  
p_Ratings_os_version_suffix | Ratings_app_version_suffix  
Ratings_carrier_suffix  
Ratings_country_suffix  
Ratings_device_suffix  
Ratings_language_suffix  
Ratings_os_version_suffix  
[Subscribers](https://support.google.com/googleplay/android-developer/answer/6135870#statistics) | p_Stats_Subscribers_country_suffix  
p_Stats_Subscribers_device_suffix | Stats_Subscribers_country_suffix  
Stats_Subscribers_device_suffix  
**_User Acquisition_** |  |   
[Store Performance](https://support.google.com/googleplay/android-developer/answer/6135870#acquisition) | p_Store_Performance_country_suffix  
p_Store_Performance_traffic_source_suffix  
| Store_Performance_country_suffix  
Store_Performance_traffic_source_suffix  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
