---
url: https://docs.cloud.google.com/dialogflow/es/docs/history/
title: History \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:51.522353+00:00
---

# History  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  History Stay organized with collections  Save and categorize content based on your preferences. 

With the History tool, you can browse and delete [interaction logs](https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging) for your agent. These logs are grouped by conversation and are shown in reverse chronological order.

![History tool screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/history.png)

## Open a conversation

To open a conversation:

  1. Open the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent near the top of the left sidebar menu.
  3. Click **History** in the left sidebar menu. If you do not see this option, ensure you have enabled [interaction logs](https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging).
  4. Optionally click **All platforms** to filter by integration platform.
  5. Optionally click **All conversations** to filter by conversations that did not match an intent.
  6. Optionally select a time range filter.
  7. Click a conversation to expand it and show individual messages.



## Delete a conversation

To delete a conversation, open the conversation and click the delete _delete_ button. If you want to delete a specific message within a conversation, you can do this from the [Training view of the Training tool](https://docs.cloud.google.com/dialogflow/es/docs/training#training-view).

## Errors and troubleshooting

Interactions that had issues with intent matching show a warning icon in yellow. To fix issues with intent matching, add training phrases to intents that should have been matched for the conversation.

Interactions that had webhook errors show a warning icon in red. To fix webhook errors, inspect the logs in Cloud logging to determine the cause.

When you click the option _more_vert_ icon for an interaction, you see options for troubleshooting:

  * **View logs in Stackdriver** : This takes you to the associated logs in [Cloud logging](https://docs.cloud.google.com/dialogflow/es/docs/logging). If you have disabled the [**Log interactions to Google Cloud**](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#general) setting, this option will not be available.
  * **Go to intent** : This takes you directly to the intent that was matched. If no intent was matched, this option is not available.
  * **Raw interaction log** : This opens the JSON representation of the interaction request.



[ Previous arrow_back  Interaction logging  ](https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging)

[ Next Speech data logging  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/data-logging)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
