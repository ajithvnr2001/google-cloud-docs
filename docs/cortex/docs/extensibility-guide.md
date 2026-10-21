---
url: https://docs.cloud.google.com/cortex/docs/extensibility-guide/
title: Cortex Framework extensibility guide \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:57.747555+00:00
---

# Cortex Framework extensibility guide  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/extensibility-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Cortex Framework extensibility guide

**[Google Cloud Cortex Framework](https://docs.cloud.google.com/cortex/docs/overview)** provides data product accelerators for advanced analytics and AI. This documentation explains how to customize and extend Cortex Framework.

For proper isolation and lifecycle management, custom foundation and data product modules should be packaged within a **[custom namespace](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces)**. This guide covers three major areas of extensibility:

  * **[Data foundation module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation)** : Register custom data modules to define custom compilation behaviors or ingest tables from source systems not supported out-of-the-box (e.g., Salesforce).
  * **[Data product module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product)** : Create new analytical data products with custom logic using local SQLX or JS files.
  * **[Agentic creation of data products](https://docs.cloud.google.com/cortex/docs/extensibility-guide-agentic-data-product-creation)** : Use autonomous AI coding assistant skills (`create-data-product`, `validate-data-product`) to scaffold, develop, verify, and deploy custom data products.

**Note:** You do **not** need to create a custom data foundation module to ingest and transform additional standard or custom tables. You can add such extra tables directly to the table configuration of the standard modules, or configure multiple instances of the existing modules in `config/config.yaml` as described in [Deployment configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration#add-table-to-data-foundation).**Note:** If you would like to add custom code (such as `.sqlx` or `.js` files) directly in your remote Dataform workspace in the Google Cloud console without creating a full data product module in source control, you must place it inside the `definitions/custom/` directory. Otherwise, your custom files will be deleted or overwritten during the next Cortex Framework deployment run (`cortex-deploy`).

## Example scenario

To illustrate an end-to-end example of extending Google Cloud Cortex Framework, this guide provides practical examples using SAP flight scheduling data:

  1. **Namespace definition** : To package and isolate custom modules, a dedicated custom namespace `sap_bookingdatamodel` is introduced. See [Custom namespace setup](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces#custom-namespace-configuration) for details.
  2. **Data foundation extension** : While adding tables typically only requires modifying table settings, this walkthrough demonstrates how to create a custom data foundation module to illustrate packaging and compiler customization. See [Data foundation module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation) for details.
  3. **Custom data product creation** : This data product consumes the `sflight` foundation table, joins it with the standard SAP currency exchange rates table (`tcurr`), and converts the flight pricing from local currency into US dollars (USD). See [Data product module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product) for details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
