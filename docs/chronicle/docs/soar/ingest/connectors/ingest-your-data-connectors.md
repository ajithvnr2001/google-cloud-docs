---
url: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors/
title: Ingest data using SOAR connectors \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:21.535133+00:00
---

# Ingest data using SOAR connectors  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingest data using SOAR connectors

Supported in: 

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The Google Security Operations platform functionality uses connectors to ingest alerts from a variety of data sources into the platform. A connector is an item in an integration package that you can download from the Content Hub. You configure connectors from **SOAR Settings > Ingestion > Connectors**.

Connectors are Python-based applications that pull alerts from third-party products into Google SecOps. Connectors also parse and normalize the raw data (alerts and events) into a Google SecOps format, which is then presented as a case in the case queue.

If you're running a third-party SIEM (a central place for all your alerts), one connector is sufficient. You can also pull data from multiple sources with several connectors. Each connector has a dedicated documentation link for additional help.

## Use case: Set up an email connector

  1. Go to **Content Hub > Integrations**.
  2. Search for and install email integration.
  3. Select settings **Configure default instance** to open the **Email - Configure Instance** dialog.
  4. Complete all required parameters.
  5. Optional: Go to **SOAR Settings > Response > Integrations Setup** to configure the integration to a different, relevant instance (not the default environment).
  6. Go to **SOAR Settings > Ingestion > Connectors**.
  7. Click add **Create New Connector**.
  8. Select the IMAP Email connector and click **Create**.
  9. Complete the required fields. When prompted, click **Save** , and then click **Yes**.
  10. Enable the connector and save it again. This makes it run periodically to pull any new emails according to the configuration.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
