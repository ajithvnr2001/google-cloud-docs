---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-content/
title: Demo: Generate multimodal content \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:38.109351+00:00
---

# Demo: Generate multimodal content  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Demo: Generate multimodal content Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/demos/generate-multimodal-content)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-content)



This demo shows you how to generate multimodal content by passing multimodal input, such as text and an image to a Gemini model, by using the Agent Platform SDK for ABAP.

**Note:** Demo programs are available only with the on-premises or any cloud edition of ABAP SDK for Google Cloud. They are not available with the SAP BTP edition of ABAP SDK for Google Cloud. 

## Before you begin

Before you run this demo, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



## Generate multimodal content

To generate multimodal content, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Go to **ABAP SDK for Google Cloud > Demos**.

  3. Open **Agent Platform SDK: Demo: Invoke Text and Multimodal Gemini Models**.

  4. Select **Generate multimodal content**.

  5. In the **Client key** field, enter the client key for authentication.

  6. In the **Model key** field, enter the model key, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

  7. Specify values for the following fields as appropriate:

     * **MIME Type** : Specify the IANA standard MIME type of the source data. The default value is `application/pdf`.
     * **GCS URI of file** : To add an image or other media to your request, specify the URI of the file stored in a Cloud Storage bucket.
     * **Upload media** : To add an image or other media to your request, upload the file from your local system.

You can either specify the URI of a file stored in a Cloud Storage bucket or upload a file from your local system.

  8. In the **Enter system instructions** field, provide [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions).

  9. In the **Enter prompt** field, provide your input [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

  10. Run the program. The **Response from LLM** area shows the generated multimodal content.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
