---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-location/
title: Localized languages in the agent adapter \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:37.919297+00:00
---

# Localized languages in the agent adapter  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-location/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Localized languages in the agent adapter Stay organized with collections  Save and categorize content based on your preferences. 

Agents can choose from a list of supported languages using the CCAI Platform portal and localized Adapters.

Administrators can assign the default agent adapters language based on their location. Locations are managed by an administrator, and each location has an assigned language. Users can override their location-based language setting using the agent adapter.

**Note:** If your CCAI Platform portal had locations entered previously, you will need to re-select locations after this feature is enabled.

## User interface components

  * Localized user interface components:

    * The agent will see all call and chat adapter controls in the language set or selected, including call flows, confirmation and error messages, agent statistics and more.
  * Not localized:

    * Queue names are not translated and will appear as they are set up in **Settings** > **Queue** for each language.

    * The incoming or outgoing call or chat session won't be translated or impacted in any way.


**Note:** See [Supported Languages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Customizing_Languages__Recordings____Messages/index.md#UUID-f1750720-b4af-9115-3a1d-c2bde09dd13b) for the full list of agent and consumer facing supported languages.

## Configure location and language

_Admin role required for configuration_

### Add a new location

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Scroll to **Localization** and click **Manage Location Setting.**

  3. Click **Add Location.**

  4. Enter the **Location** name.

  5. Select a **Language.**

  6. Click **Save.**




### Assign a language or location to agents

Agents and users are able to be assigned to a specific location. The Location dictates the default Language of the user.

#### Bulk update multiple users

To update the location for a list of users, use the [Importing Users](https://docs.cloud.google.com/contact-center/ccai-platform/Agent___Team_Configuration/index.md#UUID-d322c3ca-0001-a762-d50a-01d22822805a) process. Capitalization and spelling must match exactly for a successful import.

#### Assign locations to individual users

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams**.

  2. Navigate to the user you would like to add a location for.

  3. Click the **edit** icon next to the user's name.

  4. Select one of the pre-configured locations from the **Location** drop-down.

  5. Click **Update** to save.




## Agent adapter

The following details the specifics pertaining to the agent adapter itself.

### Set language

**Note:** The option to switch language only shows up in the **CRM adapter**. If you are accessing the adapter using the CCAI Platform portal that option won't be displayed.

  1. In the Agent Adapter **in your CRM** , click the **profile icon**.

  2. Click the language drop-down and select a language.

  3. The Agent Adapter now displays in the language selected.




### Localized adapter examples

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
