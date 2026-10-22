---
url: https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging/
title: Interaction logging \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:22.189163+00:00
---

# Interaction logging  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Interaction logging Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You must have an **Owner** role in the agent's Google Cloud project in order to change the interaction logging settings.

Interaction logs, also called conversation logs, capture conversation messages from both end-users and your agent. You can browse and delete this data with the [History](https://docs.cloud.google.com/dialogflow/es/docs/history) and [Training](https://docs.cloud.google.com/dialogflow/es/docs/training) tools.

## Enable and disable interaction logging

**Note:** If you disable interaction logging, the History and Training features will not be available.

Interaction logging is enabled by default for new agents.

To enable or disable interaction logging for your agent, see the logging options in the [agent's general settings](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#general).

## Handling end-user data

User information may reside within your agent's logs stored by Dialogflow. Disabling conversation logs only prevents future data storage and does not delete existing data. Existing data is retained until the agent is deleted or you delete specific conversations from [History](https://docs.cloud.google.com/dialogflow/es/docs/history#delete) or [Training](https://docs.cloud.google.com/dialogflow/es/docs/training#training-view).

If you choose to disable logging performed by Dialogflow, you can still create private logs within your system. If you are calling the Dialogflow API directly, log request and response data within your system. If you are using a Dialogflow integration, enable a webhook for every intent, and log request and response data within your webhook system.

## Data retention

Interaction logging data is retained in Google systems for 400 days before being deleted.

[ Previous arrow_back  Cloud logging  ](https://docs.cloud.google.com/dialogflow/es/docs/logging)

[ Next History  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/history)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
