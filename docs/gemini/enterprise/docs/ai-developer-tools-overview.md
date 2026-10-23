---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview/
title: AI developer tools overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:35.064153+00:00
---

# AI developer tools overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  AI developer tools overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

Gemini Enterprise provides AI-powered developer tools designed to accelerate software development and delivery through autonomous agents. With a subscription to the Gemini Enterprise Standard, Plus, or Pay-as-you-go edition and an invoiced Cloud Billing account, users can access the AI developer tools.

## AI developer tools on Gemini Enterprise

AI developer tool | Description  
---|---  
**Google Antigravity** |  An AI-powered development environment designed to help developers build applications using autonomous AI agents.   
  
**Supported tools:** Antigravity app and Antigravity CLI.   
  
To get started, see [Get started with Antigravity](https://antigravity.google/docs/enterprise).   
**Antigravity for IDEs** |  An AI-powered extension for integrated development environments (IDEs) that brings autonomous AI agent capabilities into your developer workflow.   
  
**Supported IDEs:** Visual Studio Code, Visual Studio, JetBrains IDEs (such as IntelliJ IDEA, PyCharm, WebStorm, and GoLand), Zed, and Xcode.   
  
To get started, see [Antigravity IDE extensions](https://antigravity.google/docs/ide/extensions).   
**Android Studio** |  The recommended IDE for professional Android development. Provides AI capabilities that help you build, debug, and scale your Android apps faster.   
  
**Supported tools:** the latest [stable version of Android Studio](https://developer.android.com/studio).   
  
To get started, see [Use Android Studio with Gemini Enterprise](https://developer.android.com/studio/gemini/enterprise).   
  
## Key benefits and use cases

AI developer tools help engineering teams accelerate software delivery and improve code quality through autonomous, multi-step agentic workflows:

Use case | Description  
---|---  
Automated code reviews and quality checks |  Autonomous agents analyze code changes and pull requests to detect bugs, security vulnerabilities, and style violations, offering actionable suggestions and automated fixes before code is merged.   
Accelerated debugging and root-cause analysis |  Agents investigate test failures, build breakages, and runtime errors across large codebases by inspecting logs, tracing stack traces, and proposing validated code corrections.   
End-to-end feature development and refactoring |  Developers can delegate multi-step software engineering tasks—such as implementing new features, refactoring legacy modules, migrating APIs, and generating comprehensive test suites—directly to autonomous AI agents.   
Seamless CLI and IDE integration |  With support for the Antigravity app, the Antigravity CLI, Antigravity for IDEs, and Android Studio, developers can incorporate AI agents into their daily IDE development, terminal workflows, and automated pipelines.   
  
## Before you begin

Before you use AI developer tools, ensure that your organization meets the following requirements:

Requirement | Description  
---|---  
Supported editions |  You must have a paid or free-trial subscription to the Gemini Enterprise Standard or Plus edition, or a paid subscription to the Standard Emerging Market or Pay-as-you-go edition. Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.  
Supported regions |  For more information about regional availability and feature limitations, see [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook](https://docs.cloud.google.com/gemini/enterprise/docs/locations).   
Invoiced billing account |  Your project must have Cloud Billing enabled and use an invoiced account. For more information, see [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).   
Overages |  To check usage limits and how overage charges apply, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages). To enable and configure pay-as-you-go overages when usage exceeds your standard quota, see [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages).   
Required roles |  To access or configure AI developer tools, users must have the appropriate role: 

  * [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`): Required to configure AI developer tools settings and view metrics. 
  * [Gemini Enterprise User](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`): Required to access and use AI developer tools. 

**Note** : The Gemini Enterprise Admin role doesn't grant permissions to access AI developer tools. You must explicitly grant the Gemini Enterprise User role to users who need to access AI developer tools, even if they already have the Gemini Enterprise Admin role.  To prevent users from accessing AI developer tools, you can create a custom role that doesn't include the AI developer tools permissions and assign that custom role instead of the default Gemini Enterprise User role. For more information, see [Create custom roles for AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles).   
  
## Known limitations

The following are known issues and limitations when configuring and using AI developer tools:

Limitation | Description  
---|---  
API enablement before license purchases |  If you purchase new Gemini Enterprise subscriptions before you enable the required APIs, the purchase or provisioning might fail.   
  
To resolve this, enable the required APIs as described in [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#before-you-begin), and then wait approximately five minutes for the change to propagate before you complete your purchase.   
Default policy for accessing files outside working folders |  When you configure AI developer tools for the first time, the **Outside of file access policy** defaults to **Deny** instead of the expected default of **Always ask**. To prompt users before AI agents access files outside their designated working folders, you must explicitly change this policy to **Always ask**.   
Access to Android Studio using a third-party identity provider |  Android Studio doesn't support third-party identity providers. If a third-party identity provider is configured for a specific location in your Gemini Enterprise Google Cloud project, users whose licenses are in that location can't access AI developer tools features in Android Studio.   
  
## Compliance limitations

Antigravity in Gemini Enterprise doesn't support the following compliance certifications and security controls:

  * Access Transparency (AXT)
  * FedRAMP (Moderate and High)
  * Impact Level 4 (IL4) and Impact Level 5 (IL5)
  * International Organization for Standardization (ISO) certifications, including ISO 27001 and ISO 42001
  * International Traffic in Arms Regulations (ITAR)
  * Service Organization Control (SOC) 1, SOC 2, and SOC 3



## What's next

  * Learn how to enable AI developer tools and configure security, compliance, and model availability controls. For more information, see [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).
  * Learn how to view metrics, adoption telemetry, and third-party model token consumption: 
    * [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics)
    * [Track third-party model token usage](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage)
  * Learn how to create custom IAM roles to restrict access to AI developer tools. For more information, see [Create custom roles for AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles).
  * Learn how to turn off AI developer tools for your organization. For more information, see [Turn off AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-turn-off).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
