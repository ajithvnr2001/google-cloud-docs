---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base/
title: Create a knowledge base \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:28.913507+00:00
---

# Create a knowledge base  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Create a knowledge base Stay organized with collections  Save and categorize content based on your preferences. 

The Agent Assist [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion) and [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq) features follow a conversation between a human agent and an end-user and provide the human agent with relevant document suggestions. Both features make suggestions based on _knowledge bases_ , collections of documents that you upload to Agent Assist. These documents are called _knowledge documents_ and can be either articles (for use with Article Suggestion) or FAQ documents (for use with FAQ Assist). See the [knowledge documents documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents) for best practices information and the [data overview page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/data) for more details on the types of data that can be uploaded to Agent Assist. This tutorial walks you through the steps required to create a knowledge base and add documents to it using the Agent Assist Console.

## Before you begin

  1. Follow the [Dialogflow setup](https://cloud.google.com/dialogflow/es/docs/quick/setup?hl=en) instructions to enable Dialogflow on a Google Cloud Platform project.
  2. We recommend that you read the Agent Assist [basics page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics) before starting this tutorial.
  3. If you are creating a knowledge base for use with [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion), make sure that your knowledge documents are in one of two formats: 
     * A public URL.
     * A file stored in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  4. If you are creating a knowledge base for use with [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq), make sure that your FAQ documents are in one of three formats:

     * A public URL.
     * A `csv` file saved in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
     * The contents of a `csv` file.

If your FAQ document is in `.csv` format, it must contain two columns. FAQ questions must be listed in the first column, and the answers to each question must be listed in the second column. Each FAQ question and its associated answer is called an **FAQ pair**. Make sure that the `.csv` file does not contain a header row.




## Create a knowledge base

  1. Navigate to the [Agent Assist](https://agentassist.cloud.google.com)

Console. Select your Google Cloud project, then click the **Data** menu option on the far left margin of the page. The **Data** menu displays all of your data. There are two tabs, one each for **conversation datasets** and **knowledge bases**.

  2. Click **knowledge bases** , then the **+Create new** button at the top of the knowledge bases page.

  3. In the menu that pops up enter a name for the knowledge base and choose a language.

  4. You will see a list (currently empty) of all documents that are part of this knowledge base. To add a document, click **+Create New**.

  5. Under **choose a knowledge type** select **FAQ** if you're uploading FAQ documents for use with [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq), or **article suggestion** if you're uploading articles for use with [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion).

  6. Under **choose a file source** , choose the location of the document you're adding. See the [before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base#before_you_begin) section for details on supported locations and file formats.

  7. Click **Create** to add the document.

**Note:** When you use the Agent Assist Console you must add documents to a knowledge base one at a time. If you want to upload a large number of documents, we recommend that you use the [Agent Assist API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion). We recommend that each knowledge base contain at least 50 documents.



## What's next

[Create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) using the Agent Assist Console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
