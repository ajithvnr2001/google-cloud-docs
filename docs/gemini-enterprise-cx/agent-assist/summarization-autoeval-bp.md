---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-bp/
title: Summarization automatic evaluation \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:32.899266+00:00
---

# Summarization automatic evaluation  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-bp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Summarization automatic evaluation Stay organized with collections  Save and categorize content based on your preferences. 

Summarization automatic evaluation (autoevaluation) is critical for moving away from manual spreadsheet-based QA and toward automated scalable validation of summarization models. This feature provides the empirical evidence needed to upsell model versions or validate custom prompt changes.

Before autoevaluation, validating a summarization model required humans to read transcripts and grade summaries manually, which was a slow, expensive, and subjective process. Summarization autoevaluation improves summarization model validation in the following ways:

  * **Scale:** Evaluates hundreds of conversations in about 20 to 30 minutes.
  * **Consistency:** LLM-based judges score accuracy, adherence, and completeness.
  * **Comparison:** Provides side-by-side evidence that Model A performs better than Model B.



## Before you begin

  * To run an evaluation, you need a summarization generator (the model configuration) and a dataset (the conversations).
  * If you want to use a Customer Experience Insights dataset but you haven't created one, go to the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects). If you have raw transcript files, convert them into the supported format for upload.



### The two data sources

You have the following two options to ingest conversation data. 

**Source type** |  **Best for...** |  **How it works**  
---|---|---  
**Agent Assist Storage** |  Live/Production traffic  |  You select a date range and a sample size. Summarization autoevaluation randomly samples from actual traffic stored in your system.   
**Conversational Insights Dataset** |  Testing specific scenarios  |  You select a curated dataset created in Customer Experience Insights. This is best for golden sets or specific test cases.   
  
## Step 1: Create a generator

  1. Navigate to **Evaluations** and click **New Evaluation**.
  2. Enter the following details: 
     * **Display Name** : Use a naming convention that includes the model version and date.
     * **Feature** : Select **Summarization**.
     * **Generator** : Select the specific generator you want to test.



## Step 2: Create a conversation dataset

Select one of the following summary data sources.

  * **Generate new summaries for all conversations** : Recommended for testing new model versions.
  * **Generate only missing summaries from the dataset** : Recommended when not all conversation transcripts have corresponding summaries based on the generator selected in the previous step.
  * **Use existing summaries from the dataset. Do not generate summaries** : Recommended for grading what was already produced without regeneration or comparing the performance of different summarization generators.



## Step 3: Choose a Cloud Storage resource

Choose a Cloud Storage folder in a bucket to store your result. 

While the [Agent Assist console](https://agentassist.cloud.google.com/) shows high-level results, export the detailed row-by-row data as a CSV. This is the source of truth for deep-dive troubleshooting.

## Step 4: Interpret the metrics

After the run is complete, you see a scorecard with scores for each [evaluation metric](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-metrics).

### Drill down

You can click any specific conversation row to see the following details:

  * The transcript with the raw dialogue
  * The summary candidates
  * A summarization autoevaluation explanation of a specific score



## Step 5: Use comparison mode

You can select two distinct evaluation runs and compare them. Compare evaluation models for the same dataset to ensure you are comparing against the same information. If you change the dataset between runs, the comparison is invalid. Always verify the Dataset ID matches in the metadata.

Follow these steps to see evidence for upgrading your summarization model to the newest version.

  1. Run evaluation A using your current model.
  2. Run evaluation B on the same dataset using the newest model.
  3. Select both evaluations in the list and click **Compare**.



The Agent Assist console highlights the higher scores.

## Troubleshooting tips and best practices

  * **Upload your own raw text files for evaluation.** First create a [Customer Experience Insights dataset](https://docs.cloud.google.com/contact-center/insights/docs/datasets).
  * **The console shows the Concise Situation section, but summary text lists it second.** The sidebar order might not perfectly match the text generation order. Rely on the text content and the CSV export for the definitive structure.
  * **About automated scores.** They're trusworthy, but verify. The autoevaluation model is calibrated to emulate human interaction, but edge cases exist. Always use the Cloud Storage CSV export to audit a small sample manually to build trust in the automated score.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
