---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap/
title: Install and configure the BigQuery AI and ML SDK for ABAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:48.674861+00:00
---

# Install and configure the BigQuery AI and ML SDK for ABAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the BigQuery AI and ML SDK for ABAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap)



This document describes how to install and configure the BigQuery AI and ML SDK for ABAP on SAP host system on Compute Engine, any cloud virtual machines, RISE with S/4HANA Cloud Private edition, or on-premise instances.

## Installation

When you install the latest version of the on-premises or any cloud edition of ABAP SDK for Google Cloud, the BigQuery AI and ML SDK for ABAP is installed for you. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

If you're using version 1.9 or earlier of the on-premises or any cloud edition of ABAP SDK for Google Cloud, then update your SDK to the latest version to get the BigQuery AI and ML SDK for ABAP. For more information, see [Update ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update).

## Enable Google Cloud APIs

To create remote connections in BigQuery for Gemini and embeddings models, enable the BigQuery Connection API in your Google Cloud project.

[BigQuery Connection API](https://console.cloud.google.com/project/_/apis/library/bigqueryconnection.googleapis.com)

To invoke Gemini and Agent Platform embeddings models, enable the Agent Platform API in your project before you register BigQuery ML models with the Model Registry.

[Agent Platform API](https://console.cloud.google.com/project/_/apis/library/aiplatform.googleapis.com)

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

## Authentication

When you set up authentication to access Google Cloud APIs in your on-premises or any cloud edition of ABAP SDK for Google Cloud, the BigQuery AI and ML SDK for ABAP utilizes the same authentication method to access relevant APIs. For information about how to set up authentication in the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

### Grant IAM permissions

Ensure that the dedicated service account for API access that you've configured for authentication has access to the BigQuery and Agent Platform resources.

## Supported regions

BigQuery ML is supported in the same regions as BigQuery. For more information, see [BigQuery ML models locations](https://docs.cloud.google.com/bigquery/docs/locations#bqml-loc).

## Get support

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
