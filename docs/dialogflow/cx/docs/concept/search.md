---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/search/
title: Search \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:33.860531+00:00
---

# Search  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/search/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Search Stay organized with collections  Save and categorize content based on your preferences. 

The search feature lets you search, filter, and access the core resources within an agent. You can filter your search results by the following resources:

  * Flows
  * Pages
  * Intents
  * Entity types
  * Route groups
  * Webhooks
  * Generators



To search for a resource:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

  2. Choose your GCP project.

  3. Select your agent.

  4. Click the search icon _search_ in the top menu bar.

  5. In the search bar, enter the keyword for the resource you are searching for. You can search for a resource by one of its properties, such as ID, display name, text response, conditional response, or custom payload. Optionally, you can filter the results by type of resource from the dropdown menu.

As you type, a dropdown menu provides a limited number of results. Click on a result to go to the editing panel of that resource.

     * You can also click **Search references** for a result to display all resources that reference the resource you're searching for. For example, if enter the keyword `store` and click **Search references** for the `store.location` intent in the results menu, the search results show all resources that reference the `store.location` intent.
  6. Press the `Enter` key or click the search icon _search_ to view the full list of search results.




For more granular filter options, click the **Show search options** _expand_more_ dropdown menu in the search bar.

  1. Select a type of resource to filter by.

  2. Under **Reference Filters** , select the **AND** or **OR** matching rule.

  3. Add one or more rules to search for resources by other resources they reference, or by their properties. For example, to search for all pages with the trigger intent `store.hours`, and where the display name contains `store`:

     1. For the first rule, select **Intent** from the dropdown menu and enter `store.hours` in the text box.

     2. Click **Add Rule (AND)**.

     3. For the second rule, select **Display Name** from the dropdown menu and enter `store` in the text box.

  4. Click **Search**.




[ Previous arrow_back  Speech model migration for phone_call Q2 2024  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024)

[ Next Integrations  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
