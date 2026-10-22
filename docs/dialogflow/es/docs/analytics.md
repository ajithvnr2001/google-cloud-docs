---
url: https://docs.cloud.google.com/dialogflow/es/docs/analytics/
title: Analytics \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:03.715210+00:00
---

# Analytics  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Analytics Stay organized with collections  Save and categorize content based on your preferences. 

The Dialogflow Console provides an analytics page that shows various agent request and response data statistics. This data helps you assess how your agent is being used in production and may be used to improve your agent.

You can select from multiple data views and filter by time range. The statistics shown on all charts are computed hourly. For most views, only successful request data for the V2 API are included.

## Open the analytics page

To open the analytics page:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Click **Analytics** in the left sidebar menu.
  4. Choose the **New** tab at the top of the page to select the new user interface described in this guide. You can also go back to the **Legacy** UI if you prefer that.



## Common metrics

The following common metrics are displayed on multiple chart types:

  * **Interactions** : For most views, _interactions_ include detect intent request counts via direct API calls and indirect calls via integrations (except for Google Assistant).
  * **Sessions** : _Sessions_ are determined by the session ID provided to interactions. You must create unique session IDs for this metric to be meaningful. For each hour on the x-axis, the _sessions_ metric shows a count of active sessions during that hour. If a session crosses an hour boundary, it will be counted for each hour it is active. Therefore, the sum of all hourly session values on a chart may be larger than the total number of actual sessions during the entire time period.
  * **Exit %** : The percentage of sessions that ended with an intent during the selected time range.



## Views

There are multiple views that you can select on the analytics page. Each view differs by the type of data, the data filter, or the chart type. The following subsections describe each view.

### Overall view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-overall.png)

This view charts session and interaction counts for all requests.

### Status codes view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-status-codes.png)

This view charts interaction counts for all requests by status code. This includes all V2 API requests, whether successful or not. Hovering your mouse over a data point shows a popup with individual status code counts at that point. For example:

  * **OK**
  * **PERMISSION_DENIED**
  * **INTERNAL**
  * **DEADLINE EXCEEDED**



### Integrations view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-integrations.png)

This view charts session and interaction counts for all requests (except Google Assistant) by [integration type](https://docs.cloud.google.com/dialogflow/docs/integrations). Hovering your mouse over a data point shows a popup with integration-specific counts at that point. API calls are shown as "api".

### Webhook view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-webhook.png)

This view charts session and interaction counts for all requests by number of requests with and without [webhook calls](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook). Hovering your mouse over a data point shows a popup with individual counts at that point:

  * **Webhook called**
  * **Webhook not called**



### Languages view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-language.png)

This view charts session and interaction counts for all requests by [language](https://docs.cloud.google.com/dialogflow/docs/agents-multilingual). Hovering your mouse over a data point shows a popup with language-specific counts at that point.

### Knowledge view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-knowledge.png)

This view charts session and interaction counts for [knowledge request](https://docs.cloud.google.com/dialogflow/docs/knowledge-connectors) by knowledge result data. Hovering your mouse over a data point shows a popup with individual counts at that point:

  * **Knowledge had result**
  * **Knowledge was used**
  * **Knowledge had primary result**



### Sentiment view

This view charts session and interaction counts for sentiment requests by sentiment result data. Hovering your mouse over a data point shows a popup with individual counts at that point.

### Speech view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-speech.png)

This view charts session and interaction counts for speech requests by speech-to-text and text-to-speech. Hovering your mouse over a data point shows a popup with individual counts at that point:

  * **Speech to text**
  * **Text to speech**



### Intents view

This view shows a table of common metric values for all requests by intent.

### Intent path view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-intent-path.png)

This view graphs _intent nodes_ with connecting _intent path lines_. Each intent in your agent has one node. Each intent path line shows a frequency value for how often one intent follows another intent in sessions for the selected time period. The **session start** node has intent path lines to the initial intent matches. Each intent node has a frequency value inside its node box that shows how often the intent ended a session for the selected time period. For example, consider that you have three intents: **A** , **B** , and **C** :

  * If **A** is always the first intent matched in a session, the chart will show a 100% intent path line from **session start** to **A**.
  * If **B** is matched 30% of the time that **A** was matched in the previous interaction in the session, the chart will show a 30% intent path line from **A** to **B**.
  * If **C** is matched 70% of the time that **A** was matched in the previous interaction in the session, the chart will show a 70% intent path line from **A** to **C**.
  * If 40% of sessions end by matching **C** , the **C** intent node box will contain a 40% value.



Hovering your mouse over an intent node shows a popup with metrics for the intent:

  * **Sessions start with this intent** : The count and percentage of sessions that started with this intent.
  * **Interactions matched this intent** : The count and percentage of interactions that matched this intent.
  * **Sessions end with this intent** : The count and percentage of sessions that ended with this intent.



Hovering your mouse over an intent path value or session start node also shows additional information.

### Session path view

![Screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/analytics-session-path.png)

Similar to the intent path view, this view graphs _intent nodes_ with connecting _intent path lines_. However, the intent path lines in this view show the frequencies as found in _complete paths_ taken by common sessions for the agent. One intent node may appear multiple times if it is matched in multiple paths or multiple times in a single path. You can interact with this chart by clicking intent nodes to expand them.

Hovering your mouse over an intent node shows a popup with metrics for the intent:

  * **Sessions followed this path prefix** : The count and percentage of sessions that followed the path up to the intent node.
  * **Ended at this point** : The percentage of sessions that ended on the path up to the intent node.



## Additional data from Stackdriver

In addition to the data provided by the analytics page, you can query for other types of data using Stackdriver. See:

  * [`tag_consumed_api`](https://cloud.google.com/monitoring/api/resources#tag_consumed_api)
  * [Creating a Dashboard with Stackdriver SLI Monitoring Metrics](https://medium.com/google-cloud/creating-a-dashboard-with-stackdriver-sli-monitoring-metrics-eaf6d19386de)



## Limitations

The following limitations apply:

  * [Google Assistant integration](https://docs.cloud.google.com/dialogflow/es/docs/integrations/aog) data is not supported.
  * It can take up to a day for data to appear in analytics.



[ Previous arrow_back  Agent validation  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-validation)

[ Next API interactions  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/api-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
