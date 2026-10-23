---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/overview/
title: Overview of the ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:51.105901+00:00
---

# Overview of the ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Overview of the ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

With the ABAP SDK for Google Cloud, you can integrate Google Cloud services directly into your SAP applications by using your preferred programming language, [ABAP](https://training.sap.com/content/abap-programming-training). You can access the full range of Google Cloud APIs through the ABAP client libraries that the SDK provides.

Beyond basic connectivity, the SDK offers the following:

  * Solutions and accelerators for using Google Cloud's AI and machine learning capabilities.
  * Built-in implementations for connectivity, security, data serialization, and error handling, so that you can focus on building your business logic.
  * A code wizard that generates boilerplate code to help you get started quickly, which helps to both reduce the code that you need to write and shorten development time.



The following diagram shows the key features, solutions, accelerators, and common use cases of ABAP SDK for Google Cloud. The next section describes the use cases in greater detail.

![ABAP SDK for Google Cloud features](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-features.png)

## Use cases

With the ABAP SDK for Google Cloud, you can build business applications by using Google Cloud's AI and machine learning capabilities. The following are some common use cases:

Build ABAP-based AI agents
    By integrating with [Agent Platform](https://docs.cloud.google.com/vertex-ai) through the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview), you can create ABAP-based AI agents that operate directly within your SAP systems. These agents can automate complex processes, make proactive decisions, and learn from data to automate tasks across SAP modules like finance, supply chain, HR, and sales.
Ingest data to BigQuery
    By using the [BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview), you can ingest your SAP data into [BigQuery](https://docs.cloud.google.com/bigquery). You can then transfer large datasets and run reports from your SAP environment.
Make real-time business decisions with BigQuery AI and ML
    By using the ABAP SDK for Google Cloud, you can use the [AI and ML capabilities of BigQuery](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) from SAP. You can load data from SAP into BigQuery, create and train ML models, and then serve predictions and insights back into your SAP applications in real time. This enables data-driven decision-making within SAP processes.
Manage content with AI
    By using [Cloud Storage](https://docs.cloud.google.com/storage) as a scalable [content repository for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/implement-gcs-sap-content-repository), the ABAP SDK for Google Cloud provides AI-infused content management for documents attached to business objects and archived business data. Here's what you can do: 

  * **Manage and analyze documents** : Store and manage documents attached to business objects in Cloud Storage. Then, use the [BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview) with Gemini to analyze this data, generate embeddings, and perform vector searches to intelligently categorize and retrieve information.
  * **Archive and gain insights from business data** : Archive business data to Cloud Storage. Then, use the [BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview) with Gemini to analyze patterns, identify trends, and derive insights from this large dataset for data-driven decision-making.


Automate business processes by using Document AI
    By integrating [Document AI](https://docs.cloud.google.com/document-ai) with SAP through the ABAP SDK for Google Cloud, you can automate tasks like invoice processing, purchase order handling, and other document-heavy workflows. Document AI extracts, classifies, and processes unstructured data from documents, reducing manual effort and errors.
Integrate systems using event-driven architectures
    By using the [Business Eventing Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview), you can facilitate real-time integration between SAP and Google Cloud services like [Pub/Sub](https://docs.cloud.google.com/pubsub). This capability enables event-driven architectures, which let your SAP systems react to business events, exchange data in real time, and trigger automated actions.
Secure SAP systems and applications
    You can integrate with [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) to securely store, retrieve, and transmit sensitive SAP data, ensuring security and compliance. 

These are a few examples of business use cases. With support for all Google Cloud APIs, the ABAP SDK for Google Cloud gives you the tools to build enterprise solutions on the ABAP platform.

## ABAP SDK for Google Cloud editions

ABAP SDK for Google Cloud provides you with options to use the SDK across on-premises, on Google Cloud, on any other cloud, S/4HANA Cloud Private Edition, S/4HANA Cloud Public Edition, and other cloud ABAP apps.

  * SAP BTP edition: Use this edition in SAP S/4HANA Cloud Private Edition, SAP S/4HANA Cloud Public Edition, and other cloud ABAP apps. The SAP BTP edition of the SDK provides integration with more than 70 Google Cloud APIs.
  * On-premises or any cloud edition: Use this edition in SAP S/4HANA, SAP ERP Central Component (ECC), and SAP S/4HANA Cloud Private Edition. The on-premises or any cloud edition of the SDK provides integration with more than 290 Google Cloud APIs.



The following diagram shows the two editions of ABAP SDK for Google Cloud and where you can install each.

![ABAP SDK for Google Cloud editions](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-editions.png)

You can choose the SDK edition that suits your ABAP runtime environment.

### SAP BTP edition

You install the SAP BTP edition of ABAP SDK for Google Cloud in the [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview).

This edition lets you build extensions and integrations using SAP's [side-by-side extension](https://learning.sap.com/learning-journeys/develop-advanced-extensions-with-sap-cloud-sdk/exploring-side-by-side-extensibility_f2f6f71d-d50c-4a48-b0f9-f5a87f717aa1) recommendation.

The SAP BTP edition of ABAP SDK for Google Cloud offers a dedicated tool, Agent Platform SDK for ABAP, for interacting with Google Cloud's [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) platform. For information about Agent Platform SDK for ABAP, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview).

For additions and enhancements to the SAP BTP edition of ABAP SDK for Google Cloud, see [What's new with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new).

### On-premises or any cloud edition

You install the on-premises or any cloud edition of ABAP SDK for Google Cloud on your SAP host system on Compute Engine, any cloud virtual machines, RISE with S/4HANA Cloud Private edition, or on-premises instances.

This edition lets you build in-app extensions and integrations directly in your SAP application.

For additions and enhancements to the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new).

## Solutions and accelerators

The on-premises or any cloud edition of ABAP SDK for Google Cloud offers the following solutions and accelerators:

  * **Agent Platform SDK for ABAP** : Interact with Google Cloud's [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform). For more information, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview).

  * **BigQuery AI and ML SDK for ABAP** : Use the AI and ML capabilities of [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) in your ABAP applications and ABAP-based AI agents. Specifically, you can use these capabilities to do the following:

    * Use Gemini to analyze your enterprise data in BigQuery.
    * Generate and manage embeddings for enterprise data in BigQuery to make BigQuery your vector database.
    * Perform vector search on your enterprise data in BigQuery for similarity search or for Retrieval-Augmented Generation (RAG).

For more information, see [BigQuery AI and ML SDK for ABAP overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview).

  * **BigQuery Toolkit for SAP** : Replicate data from your SAP tables to [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), without [SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US). For more information, see [Overview of the BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview).

  * **Business Eventing Toolkit for SAP** : Integrate SAP with Google Cloud and other business systems through its event-driven architecture. To ensure event standardization, the toolkit provides built-in modules for encoding your SAP events into the industry-standard [CloudEvents specification](https://cloudevents.io/). You can then publish these standardized events to prebuilt targets for Google Cloud services such as Pub/Sub, Cloud Run functions, Firebase Cloud Messaging (FCM), and Integration Connectors. For more information, see [Business Eventing Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview).

  * **Cloud Storage as a content repository for SAP** : Implement [Cloud Storage](https://docs.cloud.google.com/storage) as a content repository for SAP. Cloud Storage can handle your SAP-related data storage needs for storing various file types such as PDFs and images, and for archiving business data. For more information, see [Implement Cloud Storage as a content repository for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/implement-gcs-sap-content-repository).




## Reference architectures

Explore the reference architectures to see examples of how you can use the ABAP SDK for Google Cloud in your SAP application landscape. You can use the SDK to integrate with [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) for AI and machine learning capabilities, and other Google Cloud services such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), and [Cloud Storage](https://docs.cloud.google.com/storage/docs/overview). For more information, see [Reference architectures for the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/overview).

## Google Cloud community

You can discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

## Community resources

To help you get the most out of the ABAP SDK for Google Cloud, you can explore the following community resources:

  * **OpenAPI Generator for ABAP SDK for Google Cloud** : Lets you integrate your custom or private APIs that are hosted on Google Cloud into your SAP applications, by generating the ABAP classes that are compatible with ABAP SDK for Google Cloud. For more information, see [OpenAPI Generator for ABAP SDK for Google Cloud](https://github.com/GoogleCloudPlatform/openapi-generator-for-abap-sdk?tab=readme-ov-file).



## What's next

  * For information about the SAP BTP edition of ABAP SDK for Google Cloud, see [SAP BTP edition of ABAP SDK for Google Cloud guides](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/all-guides).

  * For information about the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [On-premises or any cloud edition of ABAP SDK for Google Cloud guides](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/all-guides).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
