---
url: https://docs.cloud.google.com/gemini/docs/codeassist/monitor-gemini-code-assist/
title: Monitor Gemini Code Assist usage \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:12.347455+00:00
---

# Monitor Gemini Code Assist usage  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/monitor-gemini-code-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Monitor Gemini Code Assist usage Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) usage in your organization.

Gemini Code Assist automatically collects and stores [metrics](https://docs.cloud.google.com/monitoring/docs/collect-metrics-overview#gc-metrics) in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). You can use the data visualization and analysis tools in Cloud Monitoring to help you answer important questions, such as how many daily active users in your organization are using Gemini Code Assist. This dashboard is automatically available when you enable and use Gemini Code Assist, and includes some of the most important metrics, which lets you quickly view aggregated usage data.

## Limitations

Gemini Code Assist metrics data recording is limited to user interactions with Gemini Code Assist within the IDE.

## Before you begin

To get the permissions that you need to view metric data by using the Google Cloud console, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Additionally, users must have the [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.userrole) (`roles/geminicloudassist.user`) role on your project to collect their usage metrics and send the data to the dashboard.

## Available metrics

The following tables list metrics available for Gemini Code Assist. All metrics are reported under the `cloudaicompanion.googleapis.com/Instance` resource type.

### General active user metrics

These metrics track the number of users shown a response from a Gemini Code Assist service over different time frames.

Metric | Name  
---|---  
`code_assist/hourly_active_user_count` | Hourly active user count  
`code_assist/daily_active_users` | Daily active users  
`code_assist/weekly_active_user_count` | Weekly active user count  
`code_assist/twenty_eight_day_active_users` | 28-day active users  
  
### Code suggestion and interaction metrics

These metrics count the number of Gemini Code Assist code responses shown to and accepted by users in the IDE or with the Gemini CLI.

Metric | Name  
---|---  
`code_assist/code_suggestions_count` | Code suggestions count  
`code_assist/code_suggestions_accepted_count` | Code suggestions accepted count  
`code_assist/code_lines_accepted_count` | Code lines accepted count  
`code_assist/chat_conversation_count` | Chat conversations  
`code_assist/chat_responses_count` | Chat response count  
`code_assist/chat_responses_accepted_count` | Chat responses accepted count  
  
### Platform and usage metrics

These metrics track usage at the platform level, including API calls and tokens used.

Metric | Name  
---|---  
`code_assist/used_tokens_count` | Used tokens count  
`code_assist/api_calls_count` | API calls count  
  
### Token and quota metrics

These metrics track model token consumption and overage usage for your organization:

Metric | Name  
---|---  
`usage/token_count` | Total tokens (Input, Output, and Cached)  
  
## View Gemini Code Assist metrics in your project

To view aggregated metrics for Gemini Code Assist, do the following:

  1. Go to the **Gemini Code Assist Overview** page.

[Go to Gemini Code Assist Overview](https://console.cloud.google.com/gemini-code-assist/overview)

  2. Click **Metrics** in the left navigation menu.




## What's next

  * Learn how to view [Gemini Code Assist logs](https://docs.cloud.google.com/gemini/docs/log-gemini).
  * Learn how to [monitor services and resources on Google Cloud](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
