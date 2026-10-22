---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-settings/
title: Intent settings \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:18.993300+00:00
---

# Intent settings  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Intent settings Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes basic intent settings.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access intent data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.



If you are building an agent using the API instead of the console, see the [Intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents). The API field names are similar to the console field names.

## Priority

You can set a priority for each intent, [which affects how it is matched](https://docs.cloud.google.com/dialogflow/docs/intents-matching#priority).

To set an intent's priority:

  1. Click the colored dot to the left of the intent name.
  2. Select the priority from the drop-down menu.



![Screenshot of changing the intent priority.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-priority.png)

In most cases, using the **Normal** priority is the best option. If there is a potential matching conflict between two intents, it is best to improve the training phrases to address the conflict. If you cannot remove the conflict with training phrases, you can use priorities to provide preference to one of the intents.

If the priority is **Ignore** , the intent is ignored in runtime detect intent requests.

When using the API, priorities are provided as integers. The larger the number, the greater the priority. If the priority is unset or equal to `0`, the value is converted to `500,000`. The following table shows the relationship between integer priorities and the console's named priorities:

Console priority name | Integer priority set by console | Integer priority (p) range that maps to named priority  
---|---|---  
Ignore | -1 | p < 0  
Low | 250,000 | 0 < p ≤ 250,000  
Normal | 500,000 | p = 0 or 250,000 < p ≤ 500,000  
High | 750,000 | 500,000 < p ≤ 750,000  
Highest | 1,000,000 | p > 750,000  
  
## Fulfillment

To enable [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) for an intent:

  1. Scroll down to the **Fulfillment** section.
  2. Toggle **Enable webhook call for this intent** to on.
  3. Click **Save**.



## Disable ML

Intent matching typically involves both [grammar matching and ML matching](https://docs.cloud.google.com/dialogflow/docs/intents-matching#algo). You can configure an intent to disable ML matching and rely on grammar matching alone.

You may need to do this to prevent or reduce over-triggering of intents where it's possible to provide a near-complete set of training phrases.

**Note:** This setting does not enforce exact matching, because grammar matching has some flexibility.

To disable ML matching:

  1. Click the option _more_vert_ button at the top of the intent page.
  2. Select **Disable ML**.



[ Previous arrow_back  Intent matching  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-matching)

[ Next Entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
