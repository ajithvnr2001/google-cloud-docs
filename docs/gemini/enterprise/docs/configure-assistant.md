---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant/
title: Configure the assistant \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:09:40.341862+00:00
---

# Configure the assistant  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure the assistant Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the assistant's behavior.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations**.

  4. Select the **Assistant** tab.

  5. In the **Additional LLM system instructions** section, select **Customize**.

  6. Enter the additional LLM system instructions.

For example:
         
         Make the summary headings bold
         List the resources as an unordered list
         

  7. In the **Enable web grounding** section, make sure the toggle is switched on and then select one of the following options:

     * **Google search (not Data Residency compliant)** to use the standard Google Search index for grounding.

     * **Enterprise web search (Data Residency compliant)** to use the enterprise-grade and compliant web index.

  8. In the **Default web search state** section, use the toggle to define the default behavior for queries:

     * Switch the toggle on to enable web search by default for new queries.

     * Switch the toggle off to disable web search by default.

**Note:** Users can always change this setting manually for each search.
  9. In the **Enable location context** section, use the toggle switch to enable or disable the feature:

     * Switch the toggle on to allow the Gemini Enterprise app to use location data to improve the quality of responses.

     * Switch the toggle off to disable the use of location context.

![web-settings-location-context](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/enable-web.png)Configure the web setting and location context 
  10. In the **Enable Model Armor** section, follow the instructions to configure **Model Armor** and setup the Model Armor templates. For more information, see the [Configure Model Armor](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor#configure-model-armor-console) page.

  11. In the **Enable Knowledge Catalog** section, use the toggle to turn the Knowledge Catalog integration on or off. This setting is automatically enabled when you attach a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in federated query mode, or you can turn it on or off manually at any time. For more information, see [Connect to Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog).

  12. In the **Banned phrases** section, click add **Add banned phrase** to add a phrase.

  13. In the dialog, enter the banned phrase and choose the match type.

     * **Simple string match** : This is a substring match. For example, if **Hello** is a banned phrase, both **Hello world** and **Helloworld** are rejected.

![phrase_match_type](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/single-string-match.png)Enter the banned phrase and choose the **Single string match** type 
     * **Word boundary string match** : This blocks the phrase as a whole word. For example, if **Hello** is a banned phrase, **Hello world** is rejected, but **Helloworld** is accepted.

![phrase_match_type](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/word-boundary-string-match.png)Enter the banned phrase and choose the **Word boundary string match** type 
**Note:** When you use multiple phrases, the matching logic ensures the query is blocked if any of the configured banned phrases are present in your input.
  14. In the **Chat history retention period** section, select a retention period for assistant chat sessions. You can select 1, 30, 60, 90, 120, or 180 days (the default is 60 days). Chat sessions older than the selected retention period are automatically deleted.

**Important:** The chat age is based on the **creation date.** Inform your users of this because it means that chats, which they might have interacted with as recently as yesterday, disappear without warning when the retention period is reached.
  15. Click **Save and publish**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
