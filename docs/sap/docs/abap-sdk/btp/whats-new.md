---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new/
title: What's new with the SAP BTP edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:04.228631+00:00
---

# What's new with the SAP BTP edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  What's new with the SAP BTP edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document lists additions and enhancements to the SAP BTP edition of ABAP SDK for Google Cloud.

You install and use the SAP BTP edition of ABAP SDK for Google Cloud in the [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview). For more information about the SAP BTP edition of ABAP SDK for Google Cloud, see [SAP BTP edition of ABAP SDK for Google Cloud guides](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/all-guides).

To explore the reference architectures that demonstrate how to integrate Google Cloud services within your SAP application landscape by using the ABAP SDK for Google Cloud, see [Reference architectures for the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/overview).

For additions and enhancements to the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new).

To view all of the announcements from SAP on Google Cloud, see [Release notes](https://docs.cloud.google.com/sap/docs/release-notes).

You can discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

## Version 1.1

Version 1.1 of the SAP BTP edition of ABAP SDK for Google Cloud introduces the following:

  * **Agent Platform SDK for ABAP** : The Agent Platform SDK for ABAP offers seamless interaction with [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform), making Google Cloud's Agent Platform capabilities more accessible from your BTP environment.

To learn about how you can unlock the power of AI in your ABAP programs, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview) and [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/vertex-ai-for-sap-overview).

  * **Predefined space and template** : The SDK is shipped with the predefined space `/GOOG/SDK_CONFIG_SPACE` and the predefined page `/GOOG/SDK_CONFIG_PAGE`, which simplify its installation.

  * **Invoke Cloud Run functions** : You can invoke Cloud Run functions by using the class [`/GOOG/CL_CLOUDFUNC_INVOKER`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_cloudfunc_invoker).

  * **Support for more Google Cloud APIs** : From version 1.1, Google Cloud has enriched the developer experience by introducing ABAP client libraries for 20 additional Google Cloud APIs into the SDK, including the following key APIs:

    * [Apigee API v1](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest): Integrate your ABAP applications with Apigee, Google Cloud's API management platform. With Apigee API, you can manage and monitor Google Cloud APIs for better performance, security, and developer experience.
    * [Cloud Run Admin API v2](https://docs.cloud.google.com/run/docs/reference/rest): Streamline the deployment and management of serverless ABAP applications on Cloud Run. Cloud Run offers flexibility and scalability for modern application architectures, making it easier to manage and scale your applications.
    * [Discovery Engine API](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest): Empower your ABAP applications with intelligent search capabilities to show relevant products, articles, or documents based on user queries. With Discovery Engine API, you can improve information discovery and take advantage of the power of [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) to create conversational AI agents that can seamlessly interact with your SAP systems.
    * [Dialogflow API v3](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1-overview): Build conversational interfaces and chatbots into ABAP applications using the natural language processing capabilities of Dialogflow. With Dialogflow API, you can enhance customer support, automate processes, and provide personalized interactions.
    * [Google Forms API v1](https://developers.google.com/forms/api/reference/rest): Create, read, or update Google Forms programmatically from ABAP applications. With Forms API, you can automate surveys, collect customer feedback, or gather data for analysis.
    * [Google Slides API v1](https://developers.google.com/slides/api/reference/rest): Enable ABAP applications to generate or manipulate presentations programmatically. With Slides API, you can automate report generation, data visualization, or content creation workflows.
    * [Identity and Access Management (IAM) API v2](https://docs.cloud.google.com/iam/docs/reference/rest): Build your ABAP applications to manage authentication and authorization seamlessly. With IAM API v2, you can apply enhanced security and fine-grained control over user permissions and access to Google Cloud resources.
    * [Storage Transfer Service API v1](https://docs.cloud.google.com/storage-transfer/docs/reference/rest): Simplify the migration of large datasets from your SAP, BTP environment to Cloud Storage. With Storage Transfer Service API, you can optimize data transfer workflows for your ABAP applications.

The SDK provides ABAP client libraries for more than 75 Google Cloud APIs. For information about the client libraries, see [SAP BTP edition of ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview).




## Version 1.0

Version 1.0 of the SAP BTP edition of ABAP SDK for Google Cloud enables developers to use Google Cloud APIs to create innovative solutions in their SAP BTP, ABAP environment. As a developer, you can build and deploy ML and AI-driven solutions with [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs), [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction), [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), and get real-world location insights from [Google Maps Platform](https://mapsplatform.google.com/). For a complete list of supported services, see [SAP BTP edition of ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview).

With the SAP BTP edition of ABAP SDK for Google Cloud, you can build solutions for various scenarios in SAP BTP, such as when you're following SAP's recommendation for [side-by-side extension](https://learning.sap.com/learning-journeys/develop-advanced-extensions-with-sap-cloud-sdk/exploring-side-by-side-extensibility_f2f6f71d-d50c-4a48-b0f9-f5a87f717aa1), [Clean Core](https://www.sap.com/assetdetail/2022/05/d43ce7b7-2b7e-0010-bca6-c68f7e60039b.html), or using S/4HANA Cloud.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
