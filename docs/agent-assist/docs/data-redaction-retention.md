---
url: https://docs.cloud.google.com/agent-assist/docs/data-redaction-retention/
title: Data redaction and retention \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:38.118754+00:00
---

# Data redaction and retention  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/data-redaction-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Data redaction and retention Stay organized with collections  Save and categorize content based on your preferences. 

Data redaction means masking or removing sensitive information from your data to protect a user's privacy. Redaction is crucial for Google Cloud compliance and maintaining user trust. Data retention policies dictate how long data is stored. A data retention strategy should balance business needs with regulatory requirements. Use security settings to configure data redaction and retention in Agent Assist.

## Security settings

Configure your security settings at the project level. You can configure separate security settings for each project and [location](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region). You must specify the security settings to apply for each conversation profile. If you don't specify any security settings in a conversation profile, Agent Assist doesn't apply any redaction for that conversation profile. The default and maximum retention window is 30 days.

For more information on the settings described in the following table, see the [RPC Security settings reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings).

Security settings | Description  
---|---  
`redaction_strategy` | The strategy used for redaction.  
`redaction_scope` | The data that redaction is applied to.  
`inspect_template` | [DLP](https://docs.cloud.google.com/sensitive-data-protection/docs) inspect template name.  
`deidentify_template` | [DLP](https://docs.cloud.google.com/sensitive-data-protection/docs) deidentify template name.  
`retention_window_days` | Number of days that data is retained. The default retention window in Agent Assist is 30 days.  
  
## Step 1: Create your inspect and deidentify templates

  * **Inspect template** : Defines sensitive data requiring redaction. 
  * **Deidentify template** : Specifies how to mask or remove sensitive data.



Follow these steps to create these templates.

  1. Open the Google Cloud console, and select your project.

[Google Cloud console](https://console.cloud.google.com/)

  2. Enter a search for **Sensitive data protection** , and click the link for the security page.

  3. Click the **Configuration** tab, then enable the **Sensitive Data Protection (DLP)** API, and create a template.




## Step 2: Create security settings

Follow these steps to create security settings.

  1. Open the unified CCAI (Gemini Enterprise for Customer Experience) console and select your project.

[CCAI console](https://ccai.cloud.google.com/projects)

  2. Click **Create Security Settings**.

  3. Enter your security settings configuration, and click **Create**.




## Step 3: Specify security settings

  1. Navigate to the Agent Assist console and select your project.

[Agent Assistconsole](https://agentassist.cloud.google.com)

  2. Click **Conversation profiles** and select a profile.

  3. Navigate to **Security Settings** and select the display name of the template you created.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
