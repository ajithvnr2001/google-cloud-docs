---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/avaya/
title: Avaya \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:59.282562+00:00
---

# Avaya  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/avaya/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Avaya Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

Dialogflow integrates with the [Avaya](https://www.avaya.com/) telecommunications provider. 

## Setup

To create a telephony integration with this system: 

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Select your agent. 
  3. Click **Integrations** in the left sidebar menu. 
  4. Enable the **Avaya** integration. 
  5. You are redirected to Avaya. Provide the configuration information requested by Avaya. 
  6. You are redirected back to the Dialogflow console, and the integration is now enabled for your agent. 



For more information on this integration, see the [Avaya documentation](https://downloads.avaya.com/css/P8/documents/101066647). 

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

The [pricing](https://cloud.google.com/products/conversational-agents/pricing) and [quotas](https://docs.cloud.google.com/dialogflow/quotas) for this integration are applied as audio input and output. 

## Language support

If your Dialogflow agent's default language is not English, you must configure the language with Avaya's system. Avaya's [InboundXML](https://docs.avayacloud.com/aspx/inboundxml#overview) configuration has a [Gather](https://docs.avayacloud.com/aspx/inboundxml#gather) element. Set the `language` attribute of this element to your Dialogflow agent's default language. The list of language codes supported by Avaya is provided in the documentation for `Gather`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
