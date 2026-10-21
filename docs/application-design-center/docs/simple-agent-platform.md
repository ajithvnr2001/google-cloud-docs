---
url: https://docs.cloud.google.com/application-design-center/docs/simple-agent-platform/
title: Simple Agent Platform template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:35:12.877821+00:00
---

# Simple Agent Platform template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/simple-agent-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Simple Agent Platform template Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Deploy a self-contained agent to Gemini Enterprise Agent Platform to provide scalability, AI safety, and content moderation.

This guide helps you understand the _Simple Agent Platform_ application template. You can use this template to quickly deploy your agent, along with safety settings, as an application on Google Cloud.

For example, you might implement this template to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Internal HR policy bot | An organization needs a secure HR assistant to answer employee questions while protecting sensitive data and maintaining professional language. | Sensitive data protection prevents PII leaks, while safety filters maintain professional tone. The serverless runtime scales to handle demand.  
Secure coding assistant | A development firm needs an AI tool to explain code snippets while preventing jailbreak attempts and malicious prompt injection. | Model Armor blocks adversarial attacks and jailbreaks, while enforcement policies sever connections when malicious payloads are detected.  
Multilingual public transit guide | A transit authority needs a multilingual assistant for tourists that strictly filters offensive content across all supported languages. | Multilanguage detection applies safety filters to all queries. A managed identity limits the agent's access to transit-related data.  
  
## Architecture

The following image shows the template components and connections:

![The Agent Runtime and Model Armor components connected in the canvas.](https://docs.cloud.google.com/static/application-design-center/images/agent-runtime-model-armor.png)

The template consists of the following components:

  * [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent): hosts the agent logic in a managed serverless environment. The environment can scale up to 3 instances to maintain performance. System performance is captured for monitoring and debugging.

  * [Model Armor Template](https://docs.cloud.google.com/model-armor/overview): inspects the model's input and output to block sensitive data leaks, jailbreak attempts, or toxic content. Use the `model_armor_template_MODEL_ARMOR_TEMPLATE_ID` variable in your agent code to apply safety policies to agent inputs and outputs.




## What's next

  * To learn how to duplicate and customize templates, see [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Plan your AI application strategy by [choosing your agentic architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
