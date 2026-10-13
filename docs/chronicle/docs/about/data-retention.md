---
url: https://docs.cloud.google.com/chronicle/docs/about/data-retention/
title: Configure SIEM data retention \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:48.030859+00:00
---

# Configure SIEM data retention  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/about/data-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure SIEM data retention

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

By default, Google retains 12 months of your data in your Google Security Operations account. You can extend the retention period for up to five years as part of your Purchase Order. The retention period applies to all of the data in your Google SecOps instance. For example, you can't modify the data retention policy for a specific log type.

**Important:** You cannot delete log data manually in Google SecOps.

Google uses an automated system to remove historical data based on the following:

  * **Raw logs** : Retention is determined by the ingestion timestamp (when the log arrived in the system).
  * **UDM events** : Retention is determined by the UDM event time (the timestamp within the normalized data structure).

**Note:** It may be possible to see extended events at the margins of the retention period. For example, if a detection includes component events marginally older than the retention period.

## View your data retention start date in Google SecOps

The **Data Retention** page is a read-only section within the SIEM settings that shows the date when data retention began for your account. 

To view your data retention start date, follow these steps:

  * In the navigation bar, select **SIEM Settings** > **Data Retention**. The **Data Retention** page displays the retention start date in _yyyy-mm-dd_ format.



To learn about where data in the Google SecOps account is stored, see [SecOps service locations](https://cloud.google.com/terms/secops/data-residency).

For more information, see [Google SecOps pricing](https://cloud.google.com/security/products/security-operations#pricing).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
