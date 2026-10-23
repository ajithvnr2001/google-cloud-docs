---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new/
title: What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:51.209793+00:00
---

# What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document lists additions and enhancements to the on-premises or any cloud edition of ABAP SDK for Google Cloud. For more information about the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Quickstarts for on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart).

For information about the steps to update the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Update the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update).

To explore the reference architectures that demonstrate how to integrate Google Cloud services within your SAP application landscape by using the ABAP SDK for Google Cloud, see [Reference architectures for the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/overview).

For additions and enhancements to the SAP BTP edition of ABAP SDK for Google Cloud, see [What's new with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new).

To view all of the announcements from SAP on Google Cloud, see [Release notes](https://docs.cloud.google.com/sap/docs/release-notes).

You can discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

## Version 1.14

Version 1.14 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following enhancement:

  * **Enhanced signature verification for Cloud Storage content repository** : When you use [Cloud Storage as a content repository for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/implement-gcs-sap-content-repository), your SAP system can successfully authenticate and retrieve documents from Cloud Storage without encountering an `HTTP 401 Unauthorized (ICS:3009)` signature verification error. This version applies the [SAP Note 2520326: URL corrupted when proxy configuration is in place](https://me.sap.com/notes/2520326/E) to help ensure reliable communication, particularly in environments where an outbound network proxy is configured between the SAP system and the internet.

  * **Cleanup of unreferenced node from the SPRO configuration menu** : This version removes an unreferenced node from the SPRO configuration menu that displayed `Node text not found` in the SDK version 1.13. If you are updating the SDK from version 1.13, you must import the deletion transport request to clear this unreferenced node. For information about how to do so, see [Troubleshooting the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting#dangling-spro-node). If you are updating the SDK from version 1.12 or earlier, or performing a new installation, these instructions don't apply to you.




## Version 1.13

Version 1.13 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features and enhancements:

  * **Thought signatures in function calling** : For latest Gemini 3.1 Pro models, the SDK handles the mandatory [`thoughtSignature`](https://ai.google.dev/gemini-api/docs/thought-signatures) required for function calling. This ensures reliable function calls across multiple cycles. To use this feature, [update your SDK](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update) to the latest version. For more information, see [Thought signatures in function calling](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-function-calling#thought-signatures-function-calling).

  * **Enhanced thinking configuration** : To improve the quality of model responses for complex reasoning tasks, you've more control over the model's "thinking" process for Gemini models. You can optimize your calls to Gemini by specifying the intensity of the thinking model's reasoning by setting a [thinking level](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#budget). For more information, see [Set thinking configuration for the model](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models#set-thinking-config).

  * **Support for the Parameter Manager API** : To separate configuration from your ABAP code and manage parameters centrally, this version of the SDK provides an ABAP client library for the [Parameter Manager API v1](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest). An extension to the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) service, [Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) provides a centralized storage and a single source of truth to store, access, and manage the lifecycle of all configuration parameters related to your workload deployments.

  * **Fix for`recordstamp` in BigQuery Toolkit for SAP**: This version fixes an issue with the `recordstamp` field when multiple records with the same primary key are replicated to BigQuery by using the BigQuery Toolkit for SAP. In such cases, the toolkit sets the `recordstamp` for records in the ascending order of the internal table, with up to microsecond precision.




## Version 1.12

Version 1.12 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **Support for Gemma models** : You can enhance your ABAP development by integrating [Gemma models](https://ai.google.dev/gemma/docs), a family of lightweight, state-of-the-art open models from Google. You access this feature through the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk-overview). For more information, see [Invoke the Gemma models](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemma-models).

  * **Control randomness of model's output** : For applications that require predictable and consistent outputs, you can control the randomness of Gemini's responses by setting the [seed parameter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#seed). For more information, see [Control randomness of model's output](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models#control-randomness-model-output).

  * **Get insight into Gemini's reasoning** : To gain deeper insight into the model's decision-making process, you can set [thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking) configuration to include the model's internal "thoughts" in its response. You can also specify the maximum number of tokens the model can use for this internal thought process to manage response size and complexity. For more information, see [Set thinking configuration for the model](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models#set-thinking-config).




## Version 1.11

Version 1.11 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **Support for Anthropic Claude models on Agent Platform** : You can enhance your ABAP development by integrating with [Anthropic Claude models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude) on Agent Platform. You can access this feature through the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk-overview). For more information, see [Invoke Anthropic Claude models](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-claude-models).

  * **Support for the Model Armor API** : For secure, private, and compliant use of AI, this version of the SDK provides a client stub for the [Model Armor API](https://docs.cloud.google.com/security-command-center/docs/reference/model-armor/rest). [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) is a fully managed Google Cloud service that screens LLM prompts and responses for various security and safety risks. This helps you enhance the security and safety of your ABAP-based AI agents, protecting your ABAP applications that use generative AI from common LLM security and safety risks.

  * **WIF authentication validation** : For WIF authentication to Google Cloud, you can validate the authentication configuration to verify its readiness. For more information, see [Validate authentication configuration](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#validate-auth-config).

  * **Default OAuth scope for JWT-based authentication** : For JWT-based authentication, this version of the SDK automatically populates the default OAuth scope for the [IAM Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest) calls. This improvement simplifies your configuration, as you no longer need to explicitly specify the default OAuth scope. For more information, see [Specify access settings in the client key table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt#jwt-specify-access-settings).

  * **Fixes to the BigQuery Toolkit for SAP CSV file upload** : This version of the SDK fixes the issue that was preventing you from uploading your updated BigQuery field map CSV files to the [BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview). For more information about how to use a CSV file to edit the BigQuery field map, see [Edit the BigQuery field map in a CSV file](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#edit-fields-in-csv).




## Version 1.10

Version 1.10 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **BigQuery AI and ML SDK for ABAP** : The BigQuery AI and ML SDK for ABAP lets you use the [AI and ML capabilities of BigQuery](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) in your ABAP applications and **ABAP-based AI agents**. The SDK offers the following capabilities from your ABAP environment:

    * Use Gemini to analyze your enterprise data in BigQuery.
    * Generate and manage embeddings for enterprise data in BigQuery to make BigQuery as your low-cost vector database.
    * Perform vector search on your enterprise data in BigQuery for similarity search or to [RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation) your model.

For more information, see [BigQuery AI and ML SDK for ABAP overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview).

  * **Business Eventing Toolkit for SAP** : The Business Eventing Toolkit for SAP lets you integrate SAP with Google Cloud and other business systems through its event-driven architecture, requiring minimal configuration. This approach leads to faster integration cycles and reduced development effort associated with manual integration methods. To ensure event standardization, the toolkit provides built-in modules that let you encode your SAP events into the industry-standard [CloudEvents specification](https://cloudevents.io/). You can then publish these standardized events to prebuilt targets for Google Cloud services such as [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Cloud Run functions](https://docs.cloud.google.com/functions), [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging), and [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview). For more information, see [Business Eventing Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview).

  * **Cloud Storage as a content repository for SAP** : For your SAP landscape, you can implement [Cloud Storage](https://docs.cloud.google.com/storage) as a scalable and cost-effective content repository for storing various file types such as PDFs and images, and for archiving business data. With unstructured SAP data in Cloud Storage, you can unlock the potential of your data for **enterprise AI agents** built using the Google AI services such as [Gemini Enterprise](https://cloud.google.com/products/agentspace) and [Agent Development Kit (ADK)](https://google.github.io/adk-docs). For more information, see [Implement Cloud Storage as a content repository for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/implement-gcs-sap-content-repository).

  * **Expanded support for more Google Cloud APIs** : To support your evolving needs as ABAP developers for integrating with the entire breadth of Google Cloud services and for advanced cloud adoption in SAP use cases, the ABAP SDK for Google Cloud supports more than 294 Google Cloud APIs. For information about the ABAP client libraries for all supported APIs, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/overview).

  * **Support for automatic function chaining in Agent Platform SDK for ABAP** : To handle complex interactions with Large Language Models (LLMs) in your ABAP applications and **ABAP-based AI agents** , you can use automatic function chaining. When auto-invocation of SAP function modules is enabled, if an LLM determines that multiple function modules or agents are needed to answer a prompt, then the Agent Platform SDK for ABAP automatically calls those function modules or agents in a sequence suggested by the model. Automatic function chaining lets you **orchestrate other AI agents** and perform **agent hand-offs** directly from your ABAP-based agents. For more information, see [Automatic function chaining](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-function-calling#automatic-function-chaining).

  * **Support for multi-turn conversation in Agent Platform SDK for ABAP** : To build **ABAP-based AI conversational agents** , you can use multi-turn conversations with Gemini models from your ABAP applications. The SDK lets you pass conversation history as input with each Gemini invocation, ensuring that the responses you receive are contextually relevant to the ongoing conversation. For more information, see [Add content history](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models#add-content-history). To build an ABAP-based conversation agent, see the [GitHub sample solution](https://github.com/GoogleCloudPlatform/sap-genai-samples/blob/main/README.md#gemini-powered-conversation-agent).

  * **Support for controlled content generation by using Gemini 2.0 in Agent Platform SDK for ABAP** : The Agent Platform SDK for ABAP supports [controlled generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output#googlegenaisdk_ctrlgen_with_enum_schema-python_vertex_ai_sdk) with Gemini 2.0, which helps you ensure that a model's generated output adheres to a specific schema for consistently formatted responses. For more information, see [Set response schema](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models#set-response-schema).

  * **Integrating with multi-agent systems deployed on Agent Runtime** : You can call **multi-agent systems** , built using the open-source [Agent Development Kit (ADK)](https://google.github.io/adk-docs), from your SAP systems by using the on-premises or any cloud edition of ABAP SDK for Google Cloud. For details about how to do so, see the quickstart guide [Call AI agents from ABAP environment](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-call-vertex-ai-agent).




## Version 1.9

Version 1.9 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **BigQuery Toolkit for SAP** : The BigQuery Toolkit for SAP lets you programmatically replicate data from your SAP tables to [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), without [SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US). For more information, see [Overview of the BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview).

  * **Support for more Google Cloud APIs** : From version 1.9, Google Cloud has enriched the developer experience by introducing ABAP client libraries for additional Google Cloud APIs into the SDK, including the [Firestore](https://docs.cloud.google.com/firestore/docs/reference/rest) and [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/reference/fcm/rest) APIs. The SDK also provides demo programs for these APIs. For information about the ABAP client libraries, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/overview).

  * **Enhancement to authentication by using Workload Identity Federation** : For streamlined authentication for SAP workloads that run on Google Cloud, you can set up Workload Identity Federation authentication to use VM metadata server as an Identity Provider (IdP). For more information, see [Workload Identity Federation with VM metadata](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#wif_with_vm_metadata).

  * **Enhancements to SAP function calling with Gemini** : [SAP function calling with Gemini](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-function-calling) supports the following:

    * You can declare functions without input parameters, which can serve as fallbacks for your user prompts. For more information, see [Add function declaration](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-function-calling#add_function_declaration).
    * You can get the name of the Gemini selected function (from among the declared functions) along with the Gemini suggested parameter values for the selected function. You can use this information to validate, track, and log Gemini actions as per your enterprise's security information and event management guidelines. For more information, see [Get the selected function name and parameter values](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-function-calling#get_the_selected_function_name_and_parameter_values).
  * **Support for Cards V2 interface for the Google Chat API** : You can create interactive cards for Google Chat apps by using the [Cards V2](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards) interface with the [Google Chat API v1](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_chat_v1).

  * **Fixed an issue with the Embeddings Invoker module** : The Embeddings Invoker module of the SDK generates image embeddings according to the provided input dimensions. This fixes an issue where embeddings were always generated in dimension 1408, irrespective of the input.




## Version 1.8

Version 1.8 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **Agent Platform SDK for ABAP** : The Agent Platform SDK for ABAP offers seamless interaction with [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform), making Google Cloud's Agent Platform capabilities more accessible from your ABAP environment. To learn about how you can unlock the power of AI in your ABAP programs, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview) and [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/vertex-ai-for-sap-overview).



## Version 1.7

Version 1.7 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **Support for more Google Cloud APIs** : From version 1.7, Google Cloud has enriched the developer experience by introducing ABAP client libraries for more than 20 additional Google Cloud APIs into the SDK, including the following key APIs:

    * [Apigee API v1](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest): Integrate your ABAP applications with Apigee, Google Cloud's API management platform. With Apigee API, you can manage and monitor Google Cloud APIs for better performance, security, and developer experience.
    * [Cloud Run Admin API v2](https://docs.cloud.google.com/run/docs/reference/rest): Streamline the deployment and management of serverless ABAP applications on Cloud Run. Cloud Run offers flexibility and scalability for modern application architectures, making it easier to manage and scale your applications.
    * [Discovery Engine API](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest): Empower your ABAP applications with intelligent search capabilities to show relevant products, articles, or documents based on user queries. With Discovery Engine API, you can improve information discovery and take advantage of the power of [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) to create conversational AI agents that can seamlessly interact with your SAP systems.
    * [Dialogflow API v3](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1-overview): Build conversational interfaces and chatbots into ABAP applications using the natural language processing capabilities of Dialogflow. With Dialogflow API, you can enhance customer support, automate processes, and provide personalized interactions.
    * [Google Forms API v1](https://developers.google.com/forms/api/reference/rest): Create, read, or update Google Forms programmatically from ABAP applications. With Forms API, you can automate surveys, collect customer feedback, or gather data for analysis.
    * [Google Slides API v1](https://developers.google.com/slides/api/reference/rest): Enable ABAP applications to generate or manipulate presentations programmatically. With Slides API, you can automate report generation, data visualization, or content creation workflows.
    * [Identity and Access Management (IAM) API v2](https://docs.cloud.google.com/iam/docs/reference/rest): Build your ABAP applications to manage authentication and authorization seamlessly. With IAM API v2, you can apply enhanced security and fine-grained control over user permissions and access to Google Cloud resources.
    * [Storage Transfer Service API v1](https://docs.cloud.google.com/storage-transfer/docs/reference/rest): Simplify the migration of large datasets from on-premises storage or other cloud providers into Cloud Storage. With Storage Transfer Service API, you can optimize data transfer workflows for your ABAP applications.
    * [Gemini Enterprise Agent Platform `v1beta1`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest): Use enhanced [Retrieval-Augmented Generation (RAG)](https://cloud.google.com/use-cases/retrieval-augmented-generation) corpus management features for efficient use of custom knowledge bases. With Gemini Enterprise Agent Platform v1beta1, you can take advantage of predictive analytics, intelligent automation, data-driven decision-making, and improved tools for indexing or retrieving information from large document collections.

The SDK provides ABAP client libraries for more than 75 Google Cloud APIs. For information about the client libraries, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/reference/latest/overview).

  * **Authentication improvements for Cloud Run functions** : You can use dedicated service accounts for authentication to invoke Cloud Run functions from the ABAP SDK. Depending on the environment where your SAP system is hosted, you can access 1st gen and 2nd gen Cloud Run functions by using JWT, Workload Identity Federation, or Google authentication. For more information, see [Authentication to invoke Cloud Run functions](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions).

  * **Enhanced control for Workflows API** : For [Workflows API](https://docs.cloud.google.com/workflows/docs/overview), the ABAP client library includes the [`sendHttpCallback`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.callbacks/sendHttpCallback) method that offers more ways to manage your workflows. For more information, see [Class /GOOG/CL_WORKFLOWS_V1](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_workflows_v1).

  * **Role Finder utility** : The Role Finder utility, integrated within the SDK, lets you conveniently identify the IAM roles associated with various Google Cloud APIs. For more information, see [Find IAM roles for Google Cloud APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#iam-role-finder).

  * **Enhanced API client stub** : When you're writing code in the ABAP editor, you can view the description of each field of an ABAP type. This feature helps you to quickly understand the purpose of each field in the [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer#client_stub) class.

  * **Fixed an issue with resumable uploads:** For resumable uploads to Cloud Storage and Google Drive, the issue that occurred due to unknown file size has been fixed.




## Version 1.6

Version 1.6 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **API related enhancements** : The SDK offers enhancements to the ABAP client libraries for the following Google Cloud APIs:

    * **Gemini Enterprise Agent Platform** : You can use the enhanced ABAP client library for Agent Platform API to build applications using generative AI capabilities of multi-modal LLMs, such as Gemini. For more information, see [Introduction to Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

    * **Integration Connectors** : You can use the ABAP client library for Integration Connectors API to build seamless integrations with various data sources such as Salesforce, Workday, and ServiceNow. For the list of supported data sources, see [All Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors).

By using [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) in Integration Connectors along with [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview), you can create useful integrations to address your business needs. For information about how to configure Application Integration triggers on SAP ERP data and SAP Gateway data, see [SAP ERP trigger](https://docs.cloud.google.com/application-integration/docs/configure-sap-erp-trigger) and [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger), respectively.

    * **Google Drive** : You can use the enhanced ABAP client library for Drive API to upload file data. The SDK provides methods for uploads, multipart uploads, and resumable uploads. For information about file data upload to Drive , see [Upload file data](https://developers.google.com/drive/api/guides/manage-uploads).

    * **Cloud Logging** : You can use the ABAP client library for Logging API to send application logs to Logging. With Logging, you can view all your logs in one place for troubleshooting and monitoring.

For information about the ABAP client libraries, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/reference/latest/overview).

  * **Authentication using Workload Identity Federation** : For SAP systems hosted outside Google Cloud, you can authenticate to Google Cloud using tokens through Workload Identity Federation. With Workload Identity Federation, you can grant on-premises or multicloud SAP workloads access to Google Cloud resources without using a service account key. For more information, see [Authenticate using tokens through Workload Identity Federation](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/authentication#externally_hosted_use_wif).

  * **Custom IMG transaction** : To manage ABAP SDK for Google Cloud configurations, the SDK provides a custom IMG transaction `/GOOG/SDK_IMG`. If you use SAP products such as SAP CRM or SAP BW, which don't have the Implementation Guide (IMG), then you can use the custom IMG transaction `/GOOG/SDK_IMG` to configure the SDK.

  * **Custom JSON transformations** : The SDK now offers greater control over data exchanged with API stubs through custom JSON transformations. While the default behavior uses the SAP-provided class `/UI2/CL_JSON` for serialization and deserialization, you can implement custom logic for these tasks using a BADI (Business Add-In) included with the SDK. For more information, see [Serialization and deserialization of API request and response](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#serialization_deserialization_of_api_request_and_response).

  * **Codelabs for ABAP SDK for Google Cloud** : Codelabs for ABAP SDK for Google Cloud provide tutorials to help you learn how to use Google services through the SDK. To access the codelabs for ABAP SDK for Google Cloud, see [Codelabs](https://codelabs.developers.google.com/?text=ABAP%20SDK).

  * **Web-based code wizard** : Without the need of installing ABAP SDK for Google Cloud, the web-based code wizard lets you generate sample code for all the public methods of the API client stubs provided by the SDK. To use the web-based code wizard, see [Code wizard for ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/code-wizard).




## Version 1.5

Version 1.5 of the on-premises or any cloud edition of ABAP SDK for Google Cloud introduces the following features:

  * **Support for more Google APIs:** The SDK offers new ABAP client libraries that allow developers to build and deploy ML and AI-driven solutions with [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs), integrate with [Google Workspace](https://developers.google.com/workspace) solutions like Gmail and Sheets, and get real-world location insights from [Google Maps Platform](https://mapsplatform.google.com/).

For a complete list of supported services, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/reference/v1.5/overview).

  * **Support for authentication with OAuth 2.0 client credentials:** The SDK provides a new authentication class for authenticating with Google Cloud APIs using OAuth 2.0 client credentials.

For more information, see [Authenticate to Google Cloud APIs using OAuth 2.0 client credentials](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/authentication#oauth_with_client_credentials).




## Version 1.1 to 1.4 (Not available)

Version 1.1 to 1.4 of the on-premises or any cloud edition of ABAP SDK for Google Cloud are not available.

## Version 1.0

Version 1.0 of the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/install-config#sdk_overview) provides ABAP client libraries for the following Google Cloud APIs:

  * [Address Validation](https://developers.google.com/maps/documentation/address-validation/overview) API v1
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) API v1
  * [Cloud Translation](https://docs.cloud.google.com/translate/docs/overview) API v2, v3
  * [Document AI](https://docs.cloud.google.com/document-ai/docs/overview) API v1
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) API v1
  * [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) API v1



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
