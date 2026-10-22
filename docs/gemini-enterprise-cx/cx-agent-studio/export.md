---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export/
title: Export and import \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:03.239973+00:00
---

# Export and import  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Export and import Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export and import agent applications and individual tools.

## Agent export and import

You can export and import agent applications:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project. The list of agent applications for your project are shown.
  3. Click the context menu for your application, then select import or export.



### Environment file

When you export an agent application, a file named `environment.json` is included in the root directory of the downloaded archive. This file helps you manage environment-specific settings for your application, such as Cloud Storage buckets, service endpoints, and data store URIs.

Utilizing this file for exports and imports has the following advantages:

  * **Improved Portability:** Transfer agent applications between different projects or environments (for example, development to production) by modifying a single file.
  * **Centralized Configuration:** All key external dependencies are listed in one place, simplifying management and providing a clear overview.
  * **Reduced Errors:** Minimizes the risk of mistakes compared to manually editing settings across multiple resource files.
  * **Automation-Friendly:** The JSON format lets you to programmatically update configurations using scripts as part of a CI/CD pipeline.



To update environment-specific settings:

  1. **Export:** Download the exported agent application and extract it.
  2. **Modify:** Open the `environment.json` file located in the root directory. Modify the values for the dependencies to match your target environment's settings.
  3. **Import:** Compress the entire directory, including the modified `environment.json` file, into a new zip archive. Import this new archive into the target environment. The system applies the updated values from `environment.json`.



#### Environment file details

The `environment.json` file acts as a central manifest for external dependencies that might change between different environments (for example, development, testing, and production).

When you export an agent application, the system identifies environment-specific fields within the application's resources. Instead of hardcoding these values, the system extracts them and places them in the `environment.json` file. The values are organized by the resource type and name. In the original resource manifest files, these extracted values are replaced with a placeholder variable, `$env_var`.

When you import the agent application, the system reads the `environment.json` file. It finds the `$env_var` placeholders in the resource manifests and substitutes them with the corresponding values from the `environment.json` file. This process configures the application for the new environment.

The following fields are managed in the `environment.json` file:

  * `ApiKeyConfig.key_name`
  * `ApiKeyConfig.api_key_secret_version`
  * `AudioRecordingConfig.gcs_bucket`
  * `BoostSpecs.data_stores`
  * `ConnectorTool.connection`
  * `DataStore.name`
  * `EngineSource.engine`
  * `FileSearchTool.file_corpus`
  * `OAuthConfig.client_secret_version`
  * `OAuthConfig.token_endpoint`
  * `OpenApiToolset.url` (Automatically extracted from `OpenApiToolset.open_api_schema`)
  * `ServiceAccountAuthConfig.service_account`
  * `VertexAiRagRetrievalTool.RagResource.rag_corpus`
  * `VertexAiRagRetrievalTool.RagResource.rag_file_ids`



## Tool export and import

You can export and import individual tools. This functionality provides two new options in the Tool panel: **Import** and **Export**.

  * **Export:** Download the tool's content as a JSON file to your local machine or to Cloud Storage.
  * **Import:** Use local JSON files or JSON files stored in Cloud Storage to create new tools or update existing tools.



### Export a tool

To export a tool:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com), and select your project and agent.
  2. Open the **Tool** panel.
  3. Click the context menu for the tool you want to export.
  4. Select **Export**.
  5. In the dialog, choose one of the following options: 
     * **Download:** Saves the JSON file to your local machine.
     * **Cloud Storage:** Saves the JSON file to a specified Cloud Storage URI.



### Import a tool

There are two workflows for importing a tool:

#### Import to overwrite

Use this option to modify an existing tool. The imported JSON file must correspond to the same tool type as the current tool.

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com), and select your project and agent.
  2. Open the **Tool** panel.
  3. Click the context menu for the tool you want to update.
  4. Select **Import to overwrite**.
  5. In the dialog, choose one of the following options: 
     * **Upload JSON:** Select a JSON file from your local machine.
     * **Cloud Storage:** Enter the URI of a JSON file in Cloud Storage.



#### Import as new

Use this option to create a new tool.

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com), and select your project and agent.
  2. Open the **Create Tool** panel.
  3. Select **Import as new**.
  4. In the dialog, choose one of the following options: 
     * **Upload JSON:** Select a JSON file from your local machine.
     * **Cloud Storage:** Enter the URI of a JSON file in Cloud Storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
