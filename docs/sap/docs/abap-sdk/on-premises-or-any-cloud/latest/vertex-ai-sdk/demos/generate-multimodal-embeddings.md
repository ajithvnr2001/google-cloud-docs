---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-embeddings/
title: Demo: Generate multimodal embeddings \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:21.736551+00:00
---

# Demo: Generate multimodal embeddings  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Demo: Generate multimodal embeddings Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/demos/generate-multimodal-embeddings)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/generate-multimodal-embeddings)



This demo shows you how to generate multimodal embeddings by passing multimodal input, such as text and an image to an embedding model, by using the Agent Platform SDK for ABAP.

**Note:** Demo programs are available only with the on-premises or any cloud edition of ABAP SDK for Google Cloud. They are not available with the SAP BTP edition of ABAP SDK for Google Cloud. 

## Before you begin

Before you run this demo, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters). For generating embeddings, only the following parameters are required: `Client Key`, `Model Key`, `Model ID`, `Google Cloud Region Location` and `Publisher`.



## Generate multimodal embeddings

To generate multimodal embeddings, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Go to **ABAP SDK for Google Cloud > Demos**.

  3. Open **Demo: Invoke multimodal Embedding models**

  4. Select **Generate multimodal embeddings**.

  5. In the **Client key** field, enter the client key for authentication.

  6. In the **Model key** field, enter the model key, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

  7. In the **Dimensions** field, enter the number of dimensions for the output embeddings, such as `1408`. For multimodal embeddings, the available dimensions are: `128`, `256`, `512`, and `1408`.

  8. Specify values for the following fields as appropriate:

     * **GCS URI of image** : To add an image to your request, specify the URI of the image stored in a Cloud Storage bucket.
     * **Upload image** : To add an image to your request, upload the image from your local system.
     * **GCS URI of video** : To add a video to your request, specify the URI of the video stored in a Cloud Storage bucket.

You can either specify the URI of a file from Cloud Storage or upload a file from your local system.

  9. In the **Enter text** field, provide your input text.

  10. Run the program. The **Response from LLM** area shows the generated embeddings.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
