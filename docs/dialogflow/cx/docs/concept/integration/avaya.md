---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/avaya/
title: Avaya \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:02.732777+00:00
---

# Avaya  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/avaya/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Avaya Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

Dialogflow CX integrates with the [Avaya](https://www.avaya.com/) telecommunications provider.

## Setup

To create a telephony integration with this system:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Telephony Integrations** in the **Integrations** section of the **Manage** tab.
  6. Click the **Connect** button for the Avaya integration.
  7. You are redirected to Avaya. Provide the configuration information requested by Avaya.
  8. You are redirected back to the Dialogflow CX console, and the integration is now enabled for your agent.



For more information on this integration, see the [Avaya documentation](https://developers.avayacloud.com).

## Supported countries

This integration supports phone numbers in the following countries:

**Note:** Some countries might have unique requirements that Avaya will guide you through. 

  * Argentina
  * Austria
  * Australia
  * Bahrain
  * Belgium
  * Brazil
  * Bulgaria
  * Canada
  * Chile
  * China
  * Colombia
  * Croatia
  * Cyprus
  * Czech Republic
  * Denmark
  * Dominican Republic
  * El Salvador
  * Finland
  * France
  * Georgia
  * Germany
  * Greece
  * Hong Kong
  * Hungary
  * India
  * Ireland
  * Israel
  * Italy
  * Japan
  * South Korea
  * Latvia
  * Lithuania
  * Luxembourg
  * Malaysia
  * Malta
  * Mexico
  * Netherlands
  * New Zealand
  * Norway
  * Panama
  * Peru
  * Poland
  * Portugal
  * Puerto Rico
  * Romania
  * Singapore
  * Slovakia
  * Slovenia
  * South Africa
  * Spain
  * Sweden
  * Switzerland
  * Turkey
  * United Kingdom
  * United States



## Pricing and quotas

The [pricing](https://cloud.google.com/products/conversational-agents/pricing) and [quotas](https://docs.cloud.google.com/dialogflow/quotas) for this integration are applied as a voice session.

## Language support

If your agent's default language isn't English, you must configure the language with Avaya's system. Avaya's [InboundXML](https://docs.avayacloud.com/aspx/inboundxml#overview) configuration has a [Gather](https://docs.avayacloud.com/aspx/inboundxml#gather) element. Set the `language` attribute of this element to your agent's default language. The list of language codes supported by Avaya is provided in the documentation for `Gather`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
