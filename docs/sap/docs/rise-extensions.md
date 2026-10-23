---
url: https://docs.cloud.google.com/sap/docs/rise-extensions/
title: Extensions for RISE with SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:43.443927+00:00
---

# Extensions for RISE with SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/rise-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Extensions for RISE with SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use the [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview) to build innovative extensions for your SAP solutions that are running on Google Cloud and managed by SAP under the RISE with SAP program.

The ABAP SDK for Google Cloud provides you client libraries for accessing over 250 Cloud APIs. By abstracting connectivity, security, data serialization, and error handling, the ABAP SDK for Google Cloud enables seamless consumption of Google services from any SAP application. Using Google services to enhance your SAP solutions can help you optimize business process automation, resiliency, cost, and performance, among other factors.

The following image shows how the features of ABAP SDK for Google Cloud let you solve different use cases by integrating your SAP applications with Google Cloud services:

![ABAP SDK for Google Cloud features](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-features.png)

The following sections describe examples of using ABAP SDK for Google Cloud to build extensions for RISE with SAP on Google Cloud.

## Build Agentic GenAI applications for SAP

Agent Platform SDK for ABAP, a component within the ABAP SDK for Google Cloud, provides you the necessary building blocks to build agentic RAG-capable GenAI applications for SAP business processes. These applications can help increase user productivity, reduce errors, improve accuracy, automate repetitive tasks, personalize user experiences, and provide valuable insights from large datasets.

The following image shows a reference architecture for an SAP solution that uses an agentic GenAI application built by using the ABAP SDK for Google Cloud:

![Reference architecture for an Agentic GenAI application for SAP, built using ABAP SDK for Google Cloud](https://docs.cloud.google.com/static/sap/docs/images/rise-agentic-gen-ai-ref-arch.svg)

## Use Cloud Storage as a content repository for SAP

While migrating your SAP solutions to SAP RISE, you can significantly reduce the size of your database by archiving data and attachments to Cloud Storage. For more information, see [Implement Cloud Storage as a content repository for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/implement-gcs-sap-content-repository).

The following image illustrates the usage of Cloud Storage as a content repository for SAP solutions:

![Illustration of using Cloud Storage as a content repository for SAP solutions](https://docs.cloud.google.com/static/sap/docs/images/rise-content-repo.png)

## Replicate data to BigQuery

BigQuery Toolkit for SAP, another component of the ABAP SDK for Google Cloud, enables seamless programmatic integration between SAP ERP system and BigQuery. By using the BigQuery Toolkit for SAP as a plug-in with multiple data extraction frameworks within SAP, you can extract and load data to BigQuery. For more information, see [ BigQuery Toolkit for SAP overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview).

The following image shows how the BigQuery Toolkit for SAP lets you replicate data from SAP solutions to BigQuery:

![Reference architecture for replicating data from SAP solutions to BigQuery by using BigQuery Toolkit for SAP](https://docs.cloud.google.com/static/sap/docs/images/rise-bq-toolkit.png)

## Sample reference architectures

The following are reference architectures that you can use as a guide to build extensions for your SAP solutions by using the ABAP SDK for Google Cloud:

###  [ Business insights in SAP with BigQuery ML ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/business-insights-with-bigquery-ml)

Use BigQuery ML to gain data-driven insights from your SAP environment and accelerate business decisions. 

###  [ Data protection in SAP with the DLP API ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-protection-with-cloud-dlp)

Use the DLP API to protect sensitive enterprise data in SAP. 

###  [ Gemini-powered business rule engine for SAP ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/gemini-powered-business-rule-engine)

Build a business rule engine powered by Large Language Models (LLMs) such as Gemini. 

###  [ Agent Platform Vector Search for intelligent SAP applications ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/vector-search-for-intelligent-sap-applications)

Develop intelligent SAP applications with semantic search capabilities by using the Agent Platform Vector Search. 

###  [ Data ingestion subsystem for RAG-capable generative AI applications ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-ingestion-subsystem-sap)

Design a data ingestion subsystem in SAP to use with RAG-capable generative AI applications. 

###  [ Serving subsystem for RAG-capable generative AI applications ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/serving-subsystem-sap)

Design a serving subsystem in SAP to use with RAG-capable generative AI applications. 

###  [ Send SAP notifications to Google Chat ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/google-chat-apps-for-sap)

Build Chat apps to send SAP information and updates directly in Google Workspace. 

###  [ Interact with SAP workflows from Google Chat ](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/interactive-google-chat-apps-for-sap)

Build interactive Chat apps to take actions on SAP workflows such as approve or reject requests directly from Google Workspace. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
