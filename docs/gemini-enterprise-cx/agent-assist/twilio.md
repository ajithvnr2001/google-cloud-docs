---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio/
title: Twilio integration basics \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:22.996691+00:00
---

# Twilio integration basics  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Twilio integration basics Stay organized with collections  Save and categorize content based on your preferences. 

Surface real-time suggestions for your customer service agents by integrating UI modules with Twilio.

## Before you begin

To integrate UI modules with Twilio Flex, you need access to the following resources:

  * [Agent Assist integrations repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations)
  * Provisioned Twilio [Flex](https://www.twilio.com/docs/flex) instance



## Configure your integration

Follow these steps to configure your integration.

  1. Clone the git repository.
  2. Push the Twilio Flex folder to its own repository so that the GitHub folder is in the root directory.
  3. Create an environment and store the following variables in the settings of the repository to use as part of the GitHub action pipeline: 
     * `TF_ENCRYPTION_KEY`: This can be any string of text.
     * `TWILIO_ACCOUNT_SID`: You can find this on your account dashboard.
     * `TWILIO_API_KEY`: Create an API key in your Twilio console.
     * `TWILIO_API_SECRET`: Obtain the secret when creating the API key.
  4. Click **Actions** > **Deploy Flex** > **Run Workflow**.
  5. Choose your options and click **Run Workflow** again.
  6. After it runs, click **Settings** to open the administrative console and apply your settings, such as conversation profile and endpoint configurations.



## What's next

  * [Deploy Twilio Flex](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio-flex)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
