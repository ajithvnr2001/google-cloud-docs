---
url: https://docs.cloud.google.com/food-ai/console/
title: Food Ordering AI Agent console overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:18.130472+00:00
---

# Food Ordering AI Agent console overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Guides ](https://docs.cloud.google.com/food-ai/concepts)



Send feedback 

#  Food Ordering AI Agent console overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the [Food Ordering AI Agent console](https://foodai.cloud.google.com), a web-based interface that lets you configure, test, and monitor your AI food ordering agents.

## Resource hierarchy in the console

The Food Ordering AI Agent console organizes your ordering environment into a three-tier hierarchy that maps directly to the [Food Ordering AI Agent API resources](https://docs.cloud.google.com/food-ai/concepts#agent_configuration):

  * **Project** : The Google Cloud project where the Food Ordering AI Agent API is enabled and where project-level access controls are managed.
  * **Brand** : The top-level [`Brand`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#brand) resource representing your restaurant brand and shared agent configuration.
  * **Store** : An individual [`Store`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#store) resource representing a physical restaurant location, its store-level overrides, and its associated [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu).



## Key console capabilities

After you select a Google Cloud project and brand in the Food Ordering AI Agent console, you can use the navigation menu to manage and observe your ordering agent across the following areas:

  * **Overview** : Monitor operational health, agent performance, and sales performance metrics across channels, including session volume, containment rate, outcome distribution, and upsell performance.
  * **Order history** : Inspect individual ordering sessions, filter sessions by store, date range, or session outcome, review turn-by-turn transcripts alongside cart updates, and play back session audio.
  * **Agent customization** : Configure brand-wide and store-specific agent behavior, including welcome greetings, voice characteristics, disambiguation rules, and upsell strategies.
  * **Stores and menus** : View and manage store locations, browse ingested menu items, modifier groups, and modifiers, and inspect menu ingestion logs.
  * **Agent preview** : Test ordering flows interactively using voice or text against a selected store and menu configuration before rolling out changes to production.
  * **Evaluation** : Define test datasets and test cases, configure evaluation contexts and assertion matchers, run automated batch simulations, and review execution history.



## Order history

The **Order history** page lets you review completed ordering sessions for a brand, investigate escalations or errors, and analyze how the agent handled customer orders.

### Filter and export sessions

From the session list table, each row displays the order ID, start timestamp, store ID, session duration, outcome label, and automated intervention analysis. You can narrow down sessions and export data using the toolbar controls:

  * **All filters** : Filter sessions by session ID, time range, store ID, outcome label, intervention category, or utterance text.
  * **Export** : Download the filtered session list as a CSV file for offline reporting and analysis.



### Inspect session details

Click any row in the **Order history** table to open the **Order details** panel for that session:

  * **Session summary and outcome** : View the session ID, store metadata, overall outcome classification (such as `SUCCESS` or escalated outcomes), and intervention analysis signals explaining any human intervention or failure reason.
  * **Conversation transcript and audio playback** : Listen to the full session recording or individual turn audio while reading the turn-by-turn customer and agent transcript.
  * **Cart state updates** : Inspect how the customer's cart items and modifiers changed at each turn of the conversation, and compare the agent-submitted order against the final point-of-sale order.



## Stores and menus

The **Stores** and **Menus** pages let you manage your physical restaurant locations, browse the menus associated with each store, inspect modifier hierarchies, and review menu ingestion status.

### Manage store locations

The **Store locations** page lists all stores configured for the brand. The table displays each store's ID, display name, physical address, assigned tags, operational status (such as `Active` or `Disabled`), and the last updated date.

From the **Store locations** page, you can do the following:

  * **Filter and search stores** : Filter stores by status, last updated date range, geographic location (city or state), tags, or store ID. You can also search by store ID, name, or street address.
  * **Perform batch actions** : Select multiple stores using table checkboxes to add tags, deactivate stores, or delete disabled stores in bulk.
  * **Configure store settings** : Click the settings icon for any store to open its **Store settings** page. Here, you can configure store-level details, operating hours, dayparts, and store-level agent customization and upsell overrides.



### Browse menus and item hierarchies

The **Menus** page lists the menu versions ingested for your brand and stores. Each entry shows the menu ID, associated store ID, display name, last updated timestamp, and tags. The current active menu is labeled with a **Latest** badge.

Click **View menu** on any menu entry to open the interactive **Menu navigator** :

  * **Toggle menu view** : Switch between a hierarchical tree view and a list view of menu items, modifiers, and modifier groups in the menu.
  * **Review item and modifier details** : Check item pricing, modifier price adjustments, combo numbers, combo sizes, default quantities, modifier selection constraints (such as minimum and maximum counts), item images, and availability status (such as Out of stock or Unavailable).
  * **Menu comparison** : Select up to two menus across all stores to compare side-by-side, with differences highlighted to show added, removed, or modified entries.



## Agent preview

The **Agent preview** page provides an interactive simulator to test your AI ordering agent before deploying configuration changes to customer-facing channels.

### Set up a test scenario

Before starting a simulated order, define your test scenario parameters on the **Scenario setup** page:

  * **Store** : Select the target store location. The agent loads that store's active menu, pricing, time zone, and store-specific customization overrides.
  * **Daypart** : Choose **Auto** to determine the daypart automatically from the current time, or select a specific daypart (such as Breakfast or Lunch) to test time-restricted menu availability.
  * **Channel** : Choose the simulated ordering channel, such as **Drive-thru** , **Mobile** , **Phone** , or **Web**.
  * **Agent customization and upsell strategy** : Select specific customization profiles or upsell strategies to test how the agent applies brand-wide or experimental behaviors.
  * **Interaction mode** : Select **Voice** to interact through real-time audio using your microphone, or **Text** to test through a chat interface.



### Test conversational ordering

Click **Start order** to launch the interactive simulation session:

  * **Real-time conversation** : In voice mode, speak into your microphone to converse naturally with the agent. The agent provides turn-by-turn speech transcription, audio playback, and interruption ("barge-in") support. In text mode, enter customer utterances in the chat input field.
  * **Interactive suggestions** : Click suggested item and modifier chips in the transcript stream to simulate customer selections with a single click.
  * **Live cart tracking** : Open the **Cart** side panel to observe real-time cart mutations turn by turn. You can view added items, configured modifiers and modifier quantities, itemized prices, and the running order total.
  * **In-session menu reference** : Open the **Menu** side panel during a session to browse available items and base prices alongside the active conversation.
  * **Historical session comparison** : Click **Historical sessions** to jump directly to **Order history** and compare simulated outcomes against real customer interactions.



## Evaluation

The **Evaluation** page lets you build and run automated test suites to validate your ordering agent's conversational behavior, cart accuracy, and business rules before deploying changes to customers.

For more information about using the evaluation framework and APIs, see [Evaluate ordering agents using the evaluation framework](https://docs.cloud.google.com/food-ai/evaluation).

### Manage datasets and test cases

The **Datasets & cases** tab lets you organize and maintain your evaluation test scenarios:

  * **Evaluation datasets** : Group related test cases into named datasets (such as regression suites, menu change suites, or upsell test suites). You can create new datasets, search datasets, and import or export datasets as YAML files.
  * **Evaluation cases** : Manage independent test cases imported from YAML files or converted from production sessions. Cases can exist on their own or be organized into datasets by dragging them into a dataset.
  * **Static text turn cases** : Define predictable, reproducible multi-turn conversations where specific customer text inputs are provided turn by turn.
  * **Dynamic text turn cases** : Specify high-level natural language ordering instructions (for example, ordering a customized combo meal with special dietary requests) and use generative simulation to test how the agent handles varied customer phrasing.
  * **Convert from historical sessions** : From the **Order history** page, you can convert completed customer sessions directly into evaluation cases to reproduce escalations and prevent regressions.



### Configure evaluation contexts and matchers

Evaluation cases rely on contexts to simulate realistic ordering environments and matchers to score agent performance:

  * **Evaluation contexts** : Configure the operating environment for test cases in the **Contexts** tab, including the target store location, active menu, and daypart (such as Breakfast or Lunch).
  * **Order result matchers** : Define expected final cart states in the **Matchers** tab. The evaluation compares the agent's final order against expected items, modifier selections, and item quantities.
  * **Agent utterance string matchers** : Check whether the agent's spoken or text responses contain required keywords, disclaimers, or specific phrasing using substring or regular expression matching.
  * **LLM judgement matchers** : Use LLM-as-a-judge assertions to evaluate qualitative criteria, such as whether the agent greeted the customer politely, clarified ambiguous requests appropriately, or adhered to brand tone guidelines.



### Run evaluations and review history

You can execute evaluation runs on an entire dataset or on individual test cases:

  * **Dataset and case execution** : Click **Run dataset** next to any dataset to execute all contained cases, or select specific cases using checkboxes and click **Run** to test individual scenarios.
  * **Run history** : The **History** tab tracks completed and in-progress evaluation runs, displaying the execution timestamp, dataset name, duration, and overall pass or fail rate.
  * **Inspect run details** : Click any evaluation run to drill into case-by-case results. You can inspect turn-by-turn conversation transcripts, compare expected versus actual cart contents with visual diffs, and review matcher pass and fail explanations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
