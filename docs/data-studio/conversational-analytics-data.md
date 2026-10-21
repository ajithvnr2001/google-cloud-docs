---
url: https://docs.cloud.google.com/data-studio/conversational-analytics-data/
title: Converse with Data Studio data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:18.508553+00:00
---

# Converse with Data Studio data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/conversational-analytics-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Converse with Data Studio data Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through navigating to Conversational Analytics in Data Studio and starting and conversations with your data. To learn how to connect to a data source, see the [Set up Conversational Analytics in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-setup) documentation page.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Navigate to Conversational Analytics

You can access Conversational Analytics from Data Studio in the following ways:

  * Navigate directly to [**Conversational Analytics**](https://datastudio.google.com/conversation).
  * Choose ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversational Analytics** from the navigation panel of Data Studio.
  * Choose ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversations** from the **Create** menu of Data Studio if you are in your [Sandbox](https://docs.cloud.google.com/data-studio/sandbox) workspace.
  * If [data agents](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents) have been created for your instance, select data_table **Data source** from the **Create** menu, and then select the ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Chat with my data** option on the **Get started** page.



## About conversations

Sets of questions that you ask about a dataset are organized by conversation. Splitting work into multiple conversations can be useful for organizing lines of inquiry.

The conversation experience differs between [legacy and new Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience). Select the **Legacy** tab or the **New** tab to learn more about the how conversations operate for each experience.

### New

## Start a conversation

All conversations happen with a [data agent](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents) that was built in BigQuery and published to Data Studio. To start a conversation with a data agent, follow these steps:

  1. Navigate to the **Chat with your data** page.
  2. Select the data agent that you'd like to converse with. You can use the **Search agents** bar to narrow down your search if needed.
  3. To start the conversation, enter your question and press return (Mac) or Enter (PC).



To return to the **Chat with your data** page to chat with a different data agent, select **\+ New conversation** from the main navigation.

If you don't have the [appropriate permissions](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents#before-you-begin) to chat with the agent, the agent appears on the **Chat with your data** page, but it is labeled as **Unavailable**. If you select the agent card, Data Studio displays a message that tells you what IAM role or permission you must be granted for the agent's Google Cloud project.

### Legacy

## Start a conversation

To create a new conversation, follow these steps:

  1. Click **\+ Create conversation** within Conversational Analytics.
  2. Select the data source that you want to investigate or the [data agent](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents) that you want to use for your conversation:

     * **Data source** : To start a conversation based on an existing data source, select the **Data source** panel, and then select a data source. To create a new data source, select **Connect to data**.

     * **Data agent** : To start a conversation with an existing data agent, select **Agents** , and then select a data agent. To [create a new data agent](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents#create-and-edit-data-agents-legacy), select **\+ Create agent**.

  3. To start the conversation, enter your question and press return (Mac) or Enter (PC).




You can return to the conversation from the schedule **Recent** section.

## Converse with a Looker data source

**Important:** Looker data sources aren't supported in the [new Conversational Analytics experience](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience).

[Legacy Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience) uses [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode) of content when querying Looker. 

When you converse with your data, the collapsible storage **Data** panel shows the name of the Looker Explore that is being used by the conversation. The storage **Data** panel also provides the following options:

  * open_in_new **View fields** : View the Explore in Looker in a new browser window by clicking open_in_new **View fields**.
  * chat_spark **New conversation** : Start a new conversation with the Looker Explore that the current conversation is using.



### Open in a Looker Explore

To open the query results as an Explore within the connected Looker instance, click explore **Open in Explore** within the query results.

## Converse with BigQuery data

Once you've connected to a BigQuery data source, you can ask questions about your BigQuery data.

When you converse with your data, the collapsible storage **Data** panel shows the name of the BigQuery table that the conversation is using. The storage **Data** panel also provides the following options:

  * open_in_new **View fields** : View the table in BigQuery in a new browser tab.
  * chat_spark **New conversation** : Start a new conversation with the BigQuery data that the current conversation is using.



## Ask questions

You can ask questions to get insights from your data. You can use suggested questions as a starting point for exploring data and building familiarity with Conversational Analytics.

Once you have created a conversation, you can ask questions about the data in the send_spark **Ask a question** field within the conversation.

When you're beginning a new conversation, Conversational Analytics suggests some starting questions to ask. The questions don't need to be in a specific format or use a specific syntax. However, they do need to relate to the data source.

Type your question in natural language into the **Ask a question** field. Select a question mode and click send. After you submit your query, you can cancel the response by clicking stop **Stop response**. Conversational Analytics stops running the query and displays the following message: `The query was cancelled.`

### Select a question mode

When you ask a question, you can select the question mode from a drop-down menu that contains the options **Fast** and **Thinking**. The UI describes **Fast** as being intended for answering quickly and **Thinking** as being intended for solving complex problems. Conversational Analytics defaults to **Thinking** question mode. Conversational Analytics will maintain the same question mode throughout any multi-turn conversations, unless you manually change it.

#### Fast mode

When you ask a question in **Fast** mode, Conversational Analytics attempts to directly map your natural language query to the LookML parameters that are defined in the LookML models that underlie your conversation's Explores. Conversational Analytics is able to respond quickly because it relies on the governed definitions of your LookML, and it doesn't use or display any kind of reasoning.

For example, a query like "What was our total revenue last month?" can be quickly translated into a query that selects the `total_revenue` measure and filters for the previous month.

Select **Fast** mode if your query is asking for specific facts or predefined metrics from your data.

#### Thinking mode

**Thinking** mode is intended for more complex analytical requests that require analysis beyond direct LookML lookups. In this mode, the agent "plans" its approach, deciding which tools to use and how to combine results. This mode allows for solving multi-step problems and performing advanced data science tasks that may not be possible with a single SQL-based query.

Select **Thinking** mode when asking _why_ about your data, when you're comparing trends, or when you're making more complex analytical requests that may require multiple steps. This mode is also especially helpful when testing an agent to understand how it's using the underlying LookML of its data sources.

### How Conversational Analytics processes your questions

Conversational Analytics may rephrase your question after you've submitted a query, and the rephrased question will be displayed in the conversation window following your original question. For example, Conversational Analytics might rephrase the question "What is the mean of user ages?" to "What is the average user age?"

While Conversational Analytics runs your query, you can observe its reasoning and thought process. Conversational Analytics may ask follow-up questions to clarify any ambiguities in the original query. For example, if there are multiple, similarly named fields, Conversational Analytics may ask you to clarify which field is most appropriate to use in processing your query.

### Multi-turn conversations

Conversational Analytics will take previous questions and answers into account as you continue the conversation. You can take previous answers and build on them by further refining results or changing the visualization type.

**Important:** You can only reference previous questions in answers from the active conversation. You cannot reference previous questions and answers from other conversations.

For more guidance on creating questions, see Limitations on questions.

### Use generated charts in reports

You can generate chart visualizations by asking questions in natural language. While you can't directly add a chart to a Data Studio report, you can manually recreate the visualization in your report.

To manually recreate a chart, follow these steps:

  1. Within your conversation, locate the chart that you want to add to a report.
  2. Identify the chart's details, including the chart type, dimensions, metrics, filters, sorting, and styling.
  3. Open the target Data Studio report.
  4. [Add a new chart component to the report](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report#add_a_chart_to_a_report).
  5. Configure the new chart component to match the data source and settings of the chart in your conversation.



## Manage queries within a conversation

When you converse with data, you can manage the conversation by stopping an active query response while it is running or by deleting the most recent question and its response.

### Stop a query response

To stop running a query after you've sent a message, click stop **Stop response**. Conversational Analytics stops running the query and displays the following message: `The query was cancelled.`

### Delete the most recent question

To delete the most recent question and its response, follow these steps:

  1. Hold your cursor over the most recent question, and then click delete **Delete message**.
  2. In the **Permanently delete message?** dialog, click **Delete** to permanently delete the question and its response.



## Understand query results and calculations

When you ask questions about your data in Conversational Analytics, the response might include a visualization, a data table, or other details, depending on your specific query and the connected data.

In addition to this query response, Conversational Analytics provides the following options for understanding query results and calculations:

  * Details about how your query was interpreted
  * Details about how the answer was calculated
  * If available, the option to view additional insights about the response



### Determine how your query was interpreted

To see how Conversational Analytics reasoned through your query, expand the **Show reasoning** option. To hide its reasoning, click **Hide reasoning**.

Conversational Analytics analyzes each query and thinks about how to respond, using the key words from your query to infer the relevant dimensions, metrics, and other parameters from the conversation's associated datasets and interpreting from your query what aggregations may need to be performed. When you expand **Show reasoning** , Conversational Analytics displays a plain text explanation of the steps that it took to interpret your query. The explanation also includes the duration that Conversational Analytics thought about the query.

Following its reasoning, Conversational Analytics generates a response, which may include a request for clarification about your query.

### Determine how an answer was calculated

To see how Conversational Analytics arrived at an answer or created a visualization, click keyboard_arrow_down **How was this calculated?** within the query results.

When you click **How was this calculated?** , Conversational Analytics displays the following tabs:

  * **Code** : Displays the SQL query that was run to generate the result. If you [connect Conversational Analytics to a BigQuery table](https://docs.cloud.google.com/data-studio/conversational-analytics-setup#connect-to-bigquery-data), the **Code** tab shows the generated BigQuery SQL.

**Note:** If you have enabled the [Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter) by turning on the **Advanced analytics** option for Conversational Analytics, then the **Code** tab displays the additional generated Python code for any advanced queries.
  * **Text** : Provides a plain text explanation of the steps that Conversational Analytics took to arrive at the given answer. This explanation includes the raw field names that were used, the calculations that were done, the filters that were applied, the sort order, and other details.




### Get additional insights

When Conversational Analytics is able to provide additional data insights about a response, an **Insights** keyboard_arrow_down button will appear. Click **Insights** keyboard_arrow_down to see additional information about your query. **Insights** only analyzes the data that was returned by your prompt and won't run additional queries to fetch additional data. **Insights** can be a useful source for ideas for follow-up questions to continue the conversation.

The following is an example of some insights that might be returned by the prompt "How many users are in each state?":

  * A general summary of high and low data volume areas. For example: 
    * "California, Texas, and Ohio are key states for business operations based on the data provided."
    * "England and specific regions in China, namely Anhui and Guangdong, show significant business activity."
    * "Some states, including Mie, Akita, and Iwate, have minimal presence based on the data."
  * An assessment of the variability of the dataset. For example, "The data indicates varying operational scales across different locations."



![](https://docs.cloud.google.com/static/data-studio/images/ca-insights.png)

## Manage conversations

You can change the name of conversations, delete conversations, or restore them from the trash folder.

### Name a conversation

Conversational Analytics automatically generates a conversation title that is based on your first question and response. To change the generated name, follow these steps:

  1. Click the title at the top of the conversation page.
  2. Enter a new conversation name.
  3. To save your changes, click elsewhere on the page, or press return (Mac) or Enter (PC).



### Delete a conversation

To move a conversation to the trash, open the conversation and click delete **Move to trash**.

**Note:** Conversations that remain in the trash for more than 30 days are automatically deleted.

### Restore or permanently delete a conversation

To restore or permanently delete a conversation from the trash, follow these steps:

  1. Within Conversational Analytics, select delete **Trash** in the left navigation panel to view the list of conversations that have been moved to the trash.
  2. In the **Trash** section, click the name of the conversation that you want to restore or permanently delete.
  3. In the **Are you sure?** dialog, select one of the following options: 
     * **Cancel** : Cancels the action.
     * **Restore** : Restores the conversation. The conversation can be accessed from the schedule **Recent** section of the left navigation menu within Conversational Analytics.
     * **Delete forever** : Permanently deletes the conversation.



### Search conversations

To search for a specific conversation by title, follow these steps:

  1. In the **Search Conversational Analytics** search bar, enter your search query. As you type, a list of conversations with titles that match your search query will appear.
  2. Select a conversation from the search results to open that conversation.



## Known limitations

Conversational Analytics has the following known limitations:

  * Limitations on visualizations
  * Limitations on data sources
  * Limitations on questions



### Limitations on visualizations

Conversational Analytics leverages [Vega-lite](https://vega.github.io/vega-lite) for conversation chart generation. The following Vega chart types are fully supported:

  * Line chart (one or more series)
  * Area chart
  * Bar chart (horizontal, vertical, stacked)
  * Scatter plot (one or more groups)
  * Pie chart



The following Vega chart types are supported, but you may encounter unexpected behavior when rendering them:

  * Maps
  * Heatmaps
  * Charts with tooltips



Chart types that exist outside the Vega catalog are not supported. Any charts that are not specified in this section are considered unsupported.

### Limitations on data sources

  * For Looker data sources, the following limitations apply: 
    * Conversational Analytics cannot set the value of a filter-only that is defined using the LookML [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) parameter.
    * Conversational Analytics can return a maximum of 5,000 rows per query.
  * For BigQuery data sources, the following limitations apply: 
    * You can converse with only one BigQuery table at a time. To converse with a different BigQuery table or with a data agent that uses a different BigQuery table, start a new conversation.
    * Conversational Analytics doesn't support BigQuery's [Flexible Column Names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names) feature.
  * Conversational Analytics doesn't work well with data sources that have [field editing in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) disabled because this setting prevents Conversational Analytics from creating calculated fields.



### Limitations on questions

Conversational Analytics supports questions that can be answered by a single visualization, for example:

  * Metric trends over time
  * Breakdown or distribution of a metric by dimension
  * Unique values for one or more dimensions
  * Single metric values
  * The top dimension values by metric



Conversational Analytics doesn't yet support questions that can only be answered with the following types of complicated visualizations:

  * Prediction and forecasting
  * Advanced statistical analysis, including correlation and anomaly detection



More [advanced questions](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter#suggested-questions), such as forecasting, can be answered when the Code Interpreter is enabled.

## Sample conversation

The following sample conversation shows how a user can interact with Conversational Analytics in a natural, back-and-forth way. In this example, the user asks the following question: "Can you plot monthly sales of hot drinks versus smoothies for 2023, and highlight the top selling month for each type of drink?" Conversational Analytics responds by generating a line graph that displays the monthly sales of hot drinks and smoothies for 2023, highlighting July as the month with the highest sales for both categories.

![Conversational Analytics chat that includes a line graph of monthly sales of hot drinks and smoothies in 2023, with July highlighted.](https://docs.cloud.google.com/static/data-studio/images/ca-example-filled.png)![Conversational Analytics chat that includes a line graph of monthly sales of hot drinks and smoothies in 2023, with July highlighted.](https://docs.cloud.google.com/static/data-studio/images/ca-example-filled.png)s 

As this sample conversation illustrates, Conversational Analytics interprets natural language requests, including multi-part questions that use common terms like "sales" and "hot drinks," without requiring users to specify exact database field names (like `Total monthly drink sales`) or define filter conditions (like `type of beverage = hot`). Conversational Analytics describes its key findings, explains its reasoning, and provides an answer that includes text and, where appropriate, a chart. To encourage deeper analysis, Conversational Analytics may also suggest follow-up questions.

## Related resources

  * **[Conversational Analytics overview](https://docs.cloud.google.com/data-studio/conversational-analytics-overview)** : The landing page for Conversational Analytics contains setup requirements, known limitations, supported question types, and more.

  * **[Create and converse with data agents](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents)** : With data agents, you can customize the AI-powered data querying agent by providing context and instructions that are specific to your data, which helps Conversational Analytics generate more accurate and contextually relevant responses.

  * **[Enable advanced analytics with the Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter)** : The Code Interpreter within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the Code Interpreter's use of Python enables more complex analysis and visualizations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
