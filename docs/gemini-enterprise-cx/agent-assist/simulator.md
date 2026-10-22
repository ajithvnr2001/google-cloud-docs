---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator/
title: Use the Agent Assist simulator \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:43.721348+00:00
---

# Use the Agent Assist simulator  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Use the Agent Assist simulator Stay organized with collections  Save and categorize content based on your preferences. 

The [Agent Assist Console](https://agentassist.cloud.google.com) includes a simulator that allows you to preview your model performance before you implement it. The simulator can be used with any Agent Assist feature. This tutorial walks you through the steps required to run the Agent Assist simulator.

## Before you begin

  1. You must create a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) before you can use the simulator.



## Test a conversation profile's performance

1.Navigate to the [Agent Assist Console](https://agentassist.cloud.google.com) and click on the **Conversation profiles** menu option on the left side of the page:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa19.png)

  1. The conversation profiles page displays a list of your conversation profiles. To use the simulator, click on the three vertical dots to the far right of the conversation profile that you want to test and click **Use simulator**.

  2. The window that appears provides you with input boxes for both customer and agent responses. You can test conversation profiles by inputting text and evaluating the resulting suggestions. If your conversation profile is configured to suggest both replies and articles, you can choose to enable either feature or all simultaneously by clicking the **Options** button at the top right of the simulator page and making a selection.

  3. Test your model by inputting text. The following example is testing a conversation profile configured for Article Suggestion. As the conversation progresses, articles are suggested on the right side of the screen and timestamped to match the message that triggered the suggestion:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa15.png)

  4. In the case of Smart Reply models, suggested human agent responses are surfaced in bubbles under the **Agent** text bar. Only responses that have been [allowlisted](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training#model_allowlist_management) will be suggested. You can select an agent response by clicking on one of the bubbles.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa16.png)

As the conversation progresses, the suggested replies are continuously updated:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa17.png)

  5. Results are a function of both the conversation profile and model parameters. To change your results, make changes to the conversation profile and/or the model and its associated allowlist.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
