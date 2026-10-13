---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/quick-prototyping-with-gemini/
title: Quick prototyping with Gemini \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:37.771348+00:00
---

# Quick prototyping with Gemini  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/quick-prototyping-with-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Quick prototyping with Gemini Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/quick-prototyping-with-gemini)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/quick-prototyping-with-gemini)



Google's [Generative Language API](https://ai.google.dev/api/all-methods#generative-language-api) enables seamless prototyping using the Gemini models. It lets you test and explore the capabilities of Gemini models without needing to set up complex infrastructure or manage model deployment. Google's browser based prototyping tool [Google AI Studio](https://ai.google.dev/aistudio) uses the Generative Language API to enable browser-based prototyping with generative models.

With Agent Platform SDK for ABAP, you can use the Generative Language API—Gemini API to start your prototyping journey, directly from within your ABAP environment. You need an API key generated from Google AI Studio to access the Gemini models. You need to generate this API key only once.

## Generate an API key

The API key that you generate from Google AI Studio provides a convenient way to authenticate to the Gemini API.

To generate an API key, perform the following steps:

  1. In Google AI Studio, open the **API keys** page.

[Get an API key](https://aistudio.google.com/app/apikey)

  2. Click **Create API key**.

  3. If populated, then read and acknowledge the legal notice, and then click **Continue**.

  4. If populated, then read and acknowledge the safety setting reminder.

  5. In the **Create API key** dialog, select one of the following options, as appropriate:

     * **Create API key in new project**
     * **Create API key in existing project**
  6. Copy your key string and keep it secure. You need this API key to configure authentication to the Gemini API.

  7. Copy the project number of the Google Cloud project where the API key is generated. You need this in a later step.




## Set up authentication

To authenticate to Gemini API by using an API key, use one of the following methods:

  * Authenticate by using an API key stored in SAP SSF
  * Authenticate by using an API key through a custom authentication class



### Authenticate by using an API key stored in SAP SSF

To keep your API key secure, you can store the generated API key in SAP SSF and configure a client key with the SSF authentication class. You can use this client key to access the Gemini API. For more information, see:

  * [Store the API key in SSF](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#ssf-store-api-key)
  * [Configure a client key](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#ssf-configure-client-key)



### Authenticate by using an API key through a custom authentication class

Alternatively, you can create a custom authentication class to keep your API key and configure a client key with the custom authentication class.

  1. In your SAP system, create a `Z` class by implementing the interface `/GOOG/IF_AUTH` that is shipped with the ABAP SDK for Google Cloud:

     1. In SAP GUI, execute the transaction code `SE24`.
     2. In the **Object type** field, type a name such as `Z_TEST_GEMINI_API`, and then click **Create**.
     3. Make sure that the **Object type** is **Class** , and then click **OK**.
     4. In the **Description** field, provide a description of the class such as `Class for authentication to Google AI Studio`, and then save the class as a **Local Object** or in a **Transport Request**.
     5. Open the **Interfaces** tab, add the interface `/GOOG/IF_AUTH`, and then press enter.
     6. Open the **Methods** tab. Methods of the interface `/GOOG/IF_AUTH` are automatically implemented into the `Z` class.
     7. Double-click the method `/GOOG/IF_AUTH~GET_ACCESS_TOKEN`.
     8. In the method `/GOOG/IF_AUTH~GET_ACCESS_TOKEN`, add the following code:
            
            ev_auth_type = /goog/if_auth=>c_auth_type_apik_ssf.
            cv_token = 'API_KEY'.
            GET TIME STAMP FIELD ev_logtime.
            

Replace `API_KEY` with the API key that you generated in Google AI Studio.

**Note:** Remember to use your API keys securely. Don't share them or embed them in code the public can view. To learn about the best practices for securing your API key, see [Keep your API key secure](https://ai.google.dev/gemini-api/docs/api-key#security).
     9. Activate your `Z` class.

  2. In the SAP system, create a client key configuration:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

     3. Click **New Entries**.

     4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration, such as `TEST_GEMINI_API`.  
**Google Cloud Service Account Name** | Leave this field blank.  
**Google Cloud Scope** | Leave this field blank.  
**Google Cloud Project Identifier** | Specify the project number of the Google Cloud project where the API key is stored.   
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the `Z` class that you created in the preceding step, such as `Z_TEST_GEMINI_API`.  
**Token Caching** | Leave this field blank.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Leave this field blank.  
**Authorization Parameter 2** | Leave this field blank.  
     5. Save the new entry.

  3. Make a note of the client key. You use this client key for authentication.




## Run sample code

You can explore the Gemini API capabilities by using the AI Studio demo shipped with the Agent Platform SDK for ABAP.

To run the AI Studio demo, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Go to **ABAP SDK for Google Cloud > Demos**.

  3. Open **Agent Platform SDK: Demo: Prototyping with Generative Language API**.

  4. In the **Client key** field, enter the client key that you've created in the Set up authentication section.

  5. In the **Model ID** field, enter the ID of the LLM model that you want to use, such as `gemini-2.5-flash`. For information about the available models, see [Model variants](https://ai.google.dev/gemini-api/docs/models/gemini#model-variations).

  6. Optionally, provide the following generation parameters as appropriate:

     * **Max output tokens**
     * **Response Mime type**
     * **Temperature**
     * **TopK**
     * **TopP**

For information about these model generation parameters, see [Experiment with parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values).

  7. In the **Enter system instructions** field, provide a [system instruction](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions).

  8. In the **Enter prompt** field, provide your input [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

  9. Run the program. The **Response from LLM** area shows the generated output.




## Prototype AI use cases using ABAP

You can build prototype SAP applications using the `/GOOG/CL_GENERATIVELANGUAGE_V1` and `/GOOG/CL_GENERATIVELANG_V1BETA` classes shipped with the SDK. You can invoke these classes from your ABAP environment using the client Key that you've created in the Set up authentication section.

## What's next

  * Learn how to [install and configure the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap).
  * Explore the built-in [Generative AI demo programs for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/demos-overview).
  * Learn about [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/vertex-ai-for-sap-overview).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
