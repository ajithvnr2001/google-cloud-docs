---
url: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/elasticsearch-connector-mapping-custom-datetime/
title: Map custom date and time in Elasticsearch \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:29.809863+00:00
---

# Map custom date and time in Elasticsearch  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/elasticsearch-connector-mapping-custom-datetime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map custom date and time in Elasticsearch

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

After you and configure an integration, you must map its fields to Google Security Operations fields to accurately display the information on the platform. More specifically, this document explains how to map a custom date and time for the Elasticsearch connector. 

When you configure the **Elasticsearch** connector, you must _convert_ or map the custom date and time fields, such as _\\_source\\_@timestamps_ , to **startTime** and **endTime** of Google SecOps cases. 

  1. Go to **SOAR Settings > Ontology > Ontology Status**.
  2. Click  settings  **Configure** in the same row as the Elasticsearch connector. 
  3. On the **Event Configuration** page, select **Mapping**. 
  4. Under **System Fields** , select the **StartTime** row and choose **Edit Field** from the menu. 
  5. In the **Map Target Field: StartTime** dialog, set the following fields:
     * **Extracted** : Select **\\_source\\_@timestamp** , which is from the ELK stack. 
     * **Transformation Function** : Select **FROM_CUSTOM_DATETIME**. 
     * **Enter Parameters** : Enter `YYYY-MM-DDTHH:MM:SS:zzzZ`.
  6. In the **Map Target Field: EndTime** dialog, set the following fields: 
     * **Extracted Field** : Select **\\_source\\_@timestamp** , which is from the ELK stack. 
     * **Transformation Function** : Select **FROM_CUSTOM_DATETIME**. 
     * **Enter Parameters** : Enter `YYYY-MM-DDTHH:MM:SS:zzzZ` to generalize the time format.
  7. Click **Save**.



The Elasticsearch timestamp fields are now converted to the standardized time and date fields. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
