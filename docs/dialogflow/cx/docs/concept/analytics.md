---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics/
title: Analytics \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:53.540991+00:00
---

# Analytics  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Analytics Stay organized with collections  Save and categorize content based on your preferences. 

The Dialogflow CX console provides an analytics panel that shows various views for tracking agent performance data. You can track escalations, pages with many no-matches, and webhooks with many failures. You can also filter each view by date range, and all statistics are computed hourly.

Using these analytics views, you can understand your agent performance through different conversation paths and take corrective action to improve performance.

## Limitations

For large agents, analytics data takes time to load.

## Enable conversation history

The analytics tool uses data from conversation history. It lets you enable or disable logging with the [Conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general) agent setting.

## Open the analytics panel

To open the analytics panel:

  1. Go to the [Dialogflow CX console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Analytics**.
  6. Access [Legacy Analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics-legacy) using the link near the top.



## Conversation outcomes

This view shows the counts of certain conversation outcomes as a time series chart.

The following table shows the metrics:

X | Item  
---|---  
End Interaction | The number of conversations that were abandoned.  
Live Agent Handoff | The number of conversations where human escalation was requested.  
Other | A fail-safe category in case the conversation was not handed to the live agent and did not reach the `END SESSION` page. For example, if a user says "Hi" and immediately closes the conversation, the conversation is categorized under `Other`.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-conversation-outcomes.png)

## Intent escalations

This view shows a table of intents with the highest number of human escalations. It also shows an escalation trend for a selected intent as a time series chart. If you have labeled certain intents as [head intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#head), you can restrict the view to these intents only.

The following table shows the metrics:

X | Item  
---|---  
Sessions | The total number of sessions in which the intent appeared.  
Escalation rate | Percentage of sessions that requested human escalation.  
Turns | The number of conversational turns in which the intent was detected. A single conversation can have multiple matches for one intent.  
Head intent escalated | Percentage of escalation requests for sessions where the intent was the final head intent.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-intent-escalations.png)

## Troubleshooting

The troubleshooting section contains multiple views that help you debug common issues with flows and pages.

### Missing transitions

This view lists pages where an existing intent could have matched but didn't due to missing routes.

The following table shows the metrics:

X | Item  
---|---  
Intent name | The name of the intent that would have matched if it were in scope.  
Turns | The number of conversational turns that should have matched the intent.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-missing-transitions.png)

### Pages with no-matches

This view lists pages in tabular form sorted by no-match rates.

The following table shows the metrics:

X | Item  
---|---  
No match rate | Percentage of total conversation turns that resulted in a no-match for the page.  
No match turns | The total number of conversation turns that resulted in a no-match for the page.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-pages-no-matches.png)

### Pages with no responses

This view lists pages that resulted in no agent response.

The following table shows the metrics:

X | Item  
---|---  
Empty responses | The number of interactions on the page with no agent response.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-pages-no-responses.png)

## Webhook errors

This view provides webhook errors in tabular form.

You can organize the list by:

  * **Name:** Organized by webhook name.
  * **Tag:** Organized by webhook tags.



The following table shows the metrics:

X | Item  
---|---  
Calls | The number of webhook invocations.  
Failures | The number of webhook failures excluding timeouts.  
Timeout rate | Percentage of webhook invocations that timed out.  
Average latency | Average latency of the webhook invocation.  
  
![Screenshot of analytics view](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/analytics-new-webhook-errors.png)

[ Previous arrow_back  Answer feedback  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback)

[ Next Legacy Analytics  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics-legacy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
