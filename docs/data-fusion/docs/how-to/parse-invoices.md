---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/parse-invoices/
title: Parse invoices \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:11.015352+00:00
---

# Parse invoices  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/parse-invoices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Parse invoices Stay organized with collections  Save and categorize content based on your preferences. 

You can convert invoices into structured data in Cloud Data Fusion using the Invoice Parser plugin, which is powered by Document AI. The structured data gets stored in BigQuery.

## Before you begin

To parse invoices, you need a Cloud Data Fusion instance running in version 6.4.1 or later. For more information, see [Upgrading Cloud Data Fusion instances](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#upgrade-instances).

## Create a processor

  1. In the Google Cloud console, go to the Document AI **Processors** page.

[Go to Processors](https://console.cloud.google.com/ai/document-ai/processors)

  2. [Create a processor](https://docs.cloud.google.com/document-ai/docs/create-processor). Select **Invoice parser** as the type of processor.

![Select Invoice Parser as type of processor](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/parse-invoices/invoice-parser-tile.png)

**Note:** When you create the processor, copy the processor ID for your plugin configurations.



## Configure the invoice parser plugin

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Ensure that the desired instance has been upgraded to version 6.4.1 or later. For earlier versions, [upgrade the instance](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

  3. Click **View instance**. The Cloud Data Fusion UI opens.

  4. Click **Hub**.

  5. Click **GCP** , and then deploy **GCP Plugins**.

  6. Click **DocAI** , and then deploy the **Doc AI Plugins**.

  7. Click the **Invoice Parser Quickstart** > **Create**.

  8. Customize your pipeline by entering the Invoice Parser processor ID, Cloud Storage bucket path, and BigQuery table details.

  9. Deploy and run the pipeline.

![Example pipeline with Invoice Parser plugin](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/parse-invoices/invoice-parser-pipeline-example.png)




Parsed invoices are stored in the output table in BigQuery. Metadata from the invoices is stored in the `Metadata` table and includes parsing status, Cloud Storage path, and upload timestamp of the raw invoice. Records in the output and metadata tables can be joined with the `invoice_uuid` key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
