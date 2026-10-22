---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions/
title: Conversational Analytics API: Ask effective questions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:36.181939+00:00
---

# Conversational Analytics API: Ask effective questions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API: Ask effective questions Stay organized with collections  Save and categorize content based on your preferences. 

The Conversational Analytics API is a powerful tool that lets you query your data using natural language. This page provides guidance about how to format effective questions for the ideal output. This page includes best practices for the following actions:

  * Ask general questions
  * Ask multi-part questions for more complex analyses
  * Ask questions with data conditions
  * Ask for data aggregation
  * Ask follow-up questions
  * Ask for formatted results



## Ask general questions

When you ask general questions, be specific and provide context. Instead of broad questions, narrow down the scope by including relevant details, such as dates, specific categories, or numerical filters.

A data agent that uses a Looker data source may ask follow-up questions to clarify any ambiguities in the original query. For example, if there are multiple, similarly-named fields, the data agent may ask you to clarify which field is most appropriate to use in processing your query. These questions will appear in a **Clarification Needed** response.

### Example

**Original question** : "How many invoices are created manually and systematically each year?"

**Refined question** : "Provide a count of invoices created manually and systematically each year. Assuming it takes 15 minutes to create 1 manual invoice, also calculate and provide a summary of the total time taken in hours to process all manual invoices."

**Why this works** : The refined question adds a specific calculation requirement (time spent on manual invoices) and specifies an output format, a summary.

## Ask multi-part questions for more complex analyses

Break down complex questions into multiple parts to help the Conversational Analytics API process each component accurately.

### Example

**Original question** : "What is the average turnaround time in days of cash upon delivery and payment clearing for each receivable type (PHA, co-op rebate, credit card, retail media) and what percentage of these are manual clearings? Assuming we spend 15 minutes for each receivable cleared manually, how much time are we spending on the cash app and clearing for each receivable type each year?"

**Refined question, part 1** : "What is the average turnaround in days each for the receivable type between 2025-05-05 and 2025-06-01?"

**Refined question, part 2** : "What percentage of clearings are manual clearings between 2025-05-05 and 2025-06-01 for each receivable type?"

**Refined question, part 3** : "Assuming we spend 15 minutes for each receivable cleared manually, how much time are we spending on the cash app and clearing for each receivable type each year?"

**Why this works** : Asking the questions separately lets the Conversational Analytics API address each specific metric (average turnaround, percentage of manual clearings, total time spent) with the appropriate filters, for a more accurate result.

## Ask questions with data conditions

When you ask questions with data conditions, clearly state all of the necessary filters and conditions within your question, including exact dates, number limits, and specific categories. Make sure that the Conversational Analytics API applies the correct filters (date ranges, top N results, specific categories, for example).

### Examples

The following questions correctly specify filter criteria:

  * "Show me the invoice date from 2025-05-02 until 2025-06-03 along with the respective average age of outstanding invoices only." This question clearly specifies the date range.

  * "Provide the customer name, sum of outstanding balance, average age, and receivable type for the records that are aged beyond 46 days. Limit the results up to 5 records by outstanding balance." This question specifies the record age, provides a limit, and provides sorting requirements.

  * "Provide the top industries by variance amount in customer receivables balances along with amounts for 2025FP1 versus the prior year end." This question specifies "top industries" and the periods for comparison.




## Ask for data aggregation

When you ask questions to aggregate data, specify the type of aggregation ("sum of outstanding balance," or "average age," for example) and the dimensions that you want to aggregate by ("customer name," "receivable type," or "industry", for example).

### Example

The following question effectively specifies clear requirements for data aggregation:

"Provide the customer name, sum of outstanding balance, average age, and receivable type for the records that are aged beyond 46 days."

## Ask follow-up questions

When you ask a follow-up question, refer to the previously established context, but be explicit about changes or additions. For example, if you want to change a date range, or a limit, clearly state the new parameters.

### Examples

**Original question** : "Provide the customer name, sum of outstanding balance, average age, and receivable type for the records that are aged beyond 46 days. Limit the results up to 5 records by outstanding balance."

**Follow-up question** : "Provide the previous metrics for records aged beyond 90 days and limit up to the top 10 records."

**Why this works** : The follow-up question clearly specifies the changes to the "aged beyond" filter, and the result limit, while referencing the same metrics as the previous question for context.

## Ask for formatted results

When you ask a question that doesn't specify a results format, the Conversational Analytics API determines the format that's best suited to the specific criteria and the key terms that are provided in the question.

You can guide the Conversational Analytics API to provide results in the following formats by including key terms in your question:

  * Table
  * Text
  * Line chart
  * Bar or comparison chart



### Guide the Conversational Analytics API to return results in a table

The following question implies that results should be returned in a table format, because it specifies dimension and metric column names:

"Provide the customer name, sum of outstanding balance, average age, and receivable type for the records that are aged beyond 46 days."

### Guide the Conversational Analytics API to return results as text

Using key terms such as "summary," or asking a question that only requires a straightforward response, guides the Conversational Analytics API to provide results as text.

The following questions imply that results should be returned in a text output:

  * "Calculate and provide a summary on the total time taken in hours for processing all manual invoices."

  * "What is the total time taken to process manual invoices in the past week?"




### Guide the Conversational Analytics API to return results as a line chart

Using key terms such as "trend," "change," or "delta change" in a question guides the Conversational Analytics API to provide results as a line chart.

The following questions imply that results should be returned as a line chart:

  * "What is the monthly trend of ending balances for each industry in the year 2024."

  * "What is a daily delta change in average age of outstanding invoices for day over previous day between 2025-05-02 and 2025-06-03?"




### Guide the Conversational Analytics API to return results as a bar or comparison chart

Using key terms such as "compare" and "variance" guides the Conversational Analytics API to provide results as a bar or comparison chart.

The following question implies that results should be returned as a bar or comparison chart:

"Provide the top industries by variance amount in customer receivables balances along with amounts for 2025FP1, against prior year end."

The results for this question will be returned as a bar chart that displays the variance for each industry.

## Additional resources

For additional troubleshooting tips and answers to frequently asked questions, see the [Frequently asked questions about the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions) page.

For more information about API errors and potential solutions, see the [Troubleshoot Conversational Analytics API errors](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors) guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
