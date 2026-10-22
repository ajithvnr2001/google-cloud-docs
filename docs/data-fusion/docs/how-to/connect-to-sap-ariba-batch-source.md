---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source/
title: Connect to an SAP Ariba batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:15.644973+00:00
---

# Connect to an SAP Ariba batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Connect to an SAP Ariba batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect your data pipeline to an SAP Ariba Source and a BigQuery Sink. You can configure and execute bulk data transfers from Ariba without any coding using the SAP Ariba Batch Source plugin from the Cloud Data Fusion Hub.

The plugin extracts data from the reporting facts provided in the SAP Ariba Source. Each fact corresponds with an SAP Ariba Document Type. Facts are exposed in view templates, which are accessed through the Analytical Reporting API.

For more information, see the [SAP Ariba Batch Source reference](https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference).

## Before you begin

  * [Create an instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance) in Cloud Data Fusion version 6.5.1 or later. If your instance uses an earlier version, [upgrade your Cloud Data Fusion environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

  * An SAP Ariba User must do the following:

    * Create an application and generate the OAuth credentials.
    * Grant access to the Analytical Reporting API in the Ariba developer portal.
  * Retrieve the name of the reporting view template from the SAP Ariba Analytical Reporting - View Management API by sending a `GET` request. See [Identifying Analytical reporting API view templates](https://help.sap.com/docs/ARIBA_APIS/bf0cde439a0142fbbaf511bfac5b594d/8706adc1c4c64fb5944d48283187067e.html#identifying-analytical-reporting-api-view-templates).

  * Optional: To prevent pipeline failures due to rate limits, identify the expected record count. The plugin extracts data from facts and dimensions through the SAP Ariba Analytical Reporting API, where rate limits apply. For more information, see Manage rate limits.




## Deploy and configure the plugin

  1. Deploy the SAP Ariba Batch Source plugin from the SAP tab of the Hub. For more information, see [Deploy a plugin from the Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).

  2. Open the pipeline on the Cloud Data Fusion **Studio** page and select **Data Pipeline - Batch**. The plugin doesn't support real-time pipelines.

  3. In the source menu, click **SAP Ariba**. The SAP Ariba Batch Source node appears in the pipeline.

  4. Go to the node and click **Properties**. An Ariba Properties window opens.

  5. [Configure the properties](https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference#configuration).

  6. Click **Validate** and resolve any errors.

  7. Click close **Close**.




## Optional: Connect the plugin to a BigQuery Sink

  1. On the Cloud Data Fusion **Studio** page, go to the **Sink** menu and click **BigQuery**.

The BigQuery Sink node appears in the pipeline.

  2. Configure the required properties of the sink.

  3. Click **Validate** and resolve any errors.

  4. Click close **Close**.




## Optional: Manage rate limits

To check the records count for a specific date range in SAP Ariba, see [Date-related filters for the Analytical Reporting API](https://help.sap.com/docs/ARIBA_APIS/bf0cde439a0142fbbaf511bfac5b594d/fa729a38b94c4f6b8a4d45aed80699b4.html).

For more information, see [Limits](https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference) for the plugin.

The following table describes ways to troubleshoot issues with rate limits.

Example pipeline | Count of records and required API calls | Remaining daily limit | Troubleshooting  
---|---|---|---  
I want to extract data from one view template for a specific date range.  
1 | 2,020,000 records, 41 calls | -1 of 40 | The required API calls for this date range and record count exceed the daily limit (40). To reduce the number of calls, select a smaller date range to decrease the count of records.   
I want to extract data from multiple view templates for a specific date range.  
1 | 50,001 records, 2 calls | 38 of 40  
2 | 100,000 records, 2 calls | 36 of 40  
3 | 100 records, 1 call | 35 of 40  
4 | 1,000,000 records, 20 calls | 15 of 40  
5 | 500,000 records, 10 calls | 5 of 40  
6 | 500,000 records, 10 calls | -5 of 40 | Pipeline 6 exceeds the limit for API calls. To prevent errors, run the extraction a day later or change the date range.   
  
## What's next

  * Learn more about [Cloud Data Fusion integrations for SAP](https://docs.cloud.google.com/sap/docs/cdf-plugin-for-sap).
  * Refer to the [SAP Ariba Batch Source reference](https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
