---
url: https://docs.cloud.google.com/gemini/enterprise/docs/concepts/
title: Gemini Enterprise concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:00.159387+00:00
---

# Gemini Enterprise concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/concepts/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Gemini Enterprise concepts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the concepts related to Gemini Enterprise.

![Gemini Enterprise home screen.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-enterprise-overview.png)

Gemini Enterprise consists of several key concepts that work together to provide a powerful search and action platform. These concepts include data sources, data stores, apps, assistants, actions, agents, skills, analytics, and observability.

Concept | Description  
---|---  
  
###### Data sources

| You can connect Google and third-party data sources to Gemini Enterprise and store the data in dedicated data stores. To connect your data sources, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).   
  
###### Data stores

| Each data source supports a set of entity types. For example, Jira Cloud has entities such as issues, attachments, comments, and worklogs, which are unique to the data source. Gemini Enterprise creates a separate data store for each entity. Therefore, when you create a data store using the Google Cloud console, you get a collection of data stores representing these ingested data entities. To learn about Gemini Enterprise data stores, see [Introduction to connectors and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores).  
  
###### Apps

| A Gemini Enterprise app provides search results, actions, and agents to your end users. The term _app_ can be used interchangeably with the term _engine_ in the context of APIs. An app must be connected to a data store in order to use the data from it to serve search results, answers, or actions.   
  
Apps have a many-to-many relationship with data stores. When multiple data stores are connected to a single app, this is referred to as _blended search_. For information about connecting a search app to more than one data store, see [About blended search](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores#blended).   
  
To learn more about creating an app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).   
  
###### Assistant

|  The in-app chat box, known as the assistant, is grounded with the content in your data stores and adheres to defined security, privacy, and compliance safeguards.   
  
The assistant performs multiple functions, including: 

  * Generating answers to queries and follow-up questions.
  * Grounding answers in your enterprise data with citations (with optional grounding based on external public website data).
  * Analyzing and summarizing uploaded content, such as PDFs and images, and answering follow-up questions about them.
  * Generating images based on text prompts.
  * Creating reports with streamed research during the creation process.

To learn about using the assistant, see [Use the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat).   
  
###### Actions

|  Actions enable Gemini Enterprise to move beyond data access and perform direct tasks within your data sources. For example, if your app connects to Google Calendar and Jira Cloud data sources, you can instruct Gemini Enterprise to create Google Calendar events or edit Jira Cloud issues.   
  
While basic data stores focus on search and retrieval, enabled actions allow Gemini Enterprise to create or update records in real time. You can enable actions during data store creation or later. For information on how to enable and manage actions after data store creation, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions).   
  
###### Agents

|  Agents are applications built to accomplish specific objectives. By connecting to your enterprise data and utilizing a range of tools, these agents can automate multi-step processes, analyze information, and generate new content. In Gemini Enterprise, you can find prebuilt agents in the [Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) or use [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder) to create your own custom agents.   
  
###### Skills

|  Skills provide reusable instructions and standardized prompts that customize how the assistant completes specific tasks. Users can create, save, and share custom skills across their team without writing code. For more information, see [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills).   
  
###### Analytics

|  Analytics gives you insight into the usage trends, search quality, and end-user engagement of your app. The console provides an interactive dashboard experience powered by Looker. For more information, see [View and export analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics).   
  
###### Observability

|  Observability provides real-time telemetry and monitoring across your enterprise search and agent workflows. You can inspect end-to-end execution request traces, trace spans, and usage audit logs to diagnose latency, monitor agent step execution, and analyze system activity.   
  
To learn about configuring observability, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).   
  
To inspect execution telemetry, see [Access traces and spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans) and [Access usage audit logs](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
