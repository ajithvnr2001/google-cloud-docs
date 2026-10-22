---
url: https://docs.cloud.google.com/dialogflow/es/docs/data-logging/
title: Speech data logging \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:56.786019+00:00
---

# Speech data logging  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/data-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Speech data logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

With Dialogflow Essentials, you can opt in to speech data logging to access [enhanced speech models](https://docs.cloud.google.com/dialogflow/es/docs/speech-enhanced-models), which use customer data for speech recognition improvements.

## Limitations

The following limitations apply:

  * This setting is currently only available to users of a paid [edition](https://docs.cloud.google.com/dialogflow/docs/editions).



## Enabling data logging and using enhanced models

**Note:** Before enabling data logging, you need to certify that you have the proper permissions from the data originator(s), and that you haven't entered into a BAA with Google, for HIPAA purposes as an example. See the complete [terms for data logging](https://docs.cloud.google.com/dialogflow/docs/data-logging-terms) for details.

To enable data logging:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent.
  3. Click the settings _settings_ button next to the agent name to edit its settings.
  4. Select the **Speech** tab.
  5. Scroll to the **Improve Speech Recognition Quality** section.
  6. Toggle **Enable enhanced speech models and data logging** on.



To use an enhanced model, you just need to specify a speech model in your API request. If you do not specify a speech model, Dialogflow CX does not use an enhanced model.

## Disabling data logging

You can disable data logging for your project at any time. Review the [terms for data logging](https://docs.cloud.google.com/dialogflow/docs/data-logging-terms) to read about what happens to your data when you disable data logging for a project.

To disable data logging:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent.
  3. Click the settings _settings_ button next to the agent name to edit its settings.
  4. Select the **Speech** tab.
  5. Scroll to the **Improve Speech Recognition Quality** section.
  6. Toggle **Enable enhanced speech models and data logging** off.



[ Previous arrow_back  History  ](https://docs.cloud.google.com/dialogflow/es/docs/history)

[ Next Audit logging  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/audit-logging)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
