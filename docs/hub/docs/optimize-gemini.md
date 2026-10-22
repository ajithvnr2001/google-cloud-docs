---
url: https://docs.cloud.google.com/hub/docs/optimize-gemini/
title: Optimize costs with Gemini assistance \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:59.578946+00:00
---

# Optimize costs with Gemini assistance  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/optimize-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  Optimize costs with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use Gemini for Google Cloud, an AI-powered collaborator, to help you to optimize costs.

For information about viewing data on the Optimization page in Cloud Hub, see [View resource costs and utilization](https://docs.cloud.google.com/hub/docs/optimize).

Gemini Cloud Assist can help you to:

  * Learn insights about recent cost and utilization changes.
  * Get cost or utilization data for a specific application or project.
  * For supported resource costs, get an explanation for cost changes.



This document is for developers and platform administrators. If you manage billing accounts or budgets in Cloud Billing, see the [Cloud Billing cost optimization documentation](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) for information about using FinOps Hub and Gemini Cloud Assist in Cloud Billing.

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

  1. [Set up Cloud Hub](https://docs.cloud.google.com/hub/docs/setup-cloud-hub).

  2. [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).


**Note:** Cloud Hub only supports applications in a folder configured for application management. It doesn't support applications in a [host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

The Cloud Hub Operator role contains most of the required permissions to view data on the Optimization page, including permissions to view Cloud Monitoring data, Cloud Logging data, App Hub application data, Cloud Asset Inventory resource data, and Active Assist recommendations.

To get the permissions that you need to view data in Cloud Hub, ask your administrator to grant you the following IAM roles on the project or management project (for [app-enabled folders](https://docs.cloud.google.com/hub/docs/app-project-views)): 

  * View most data in Cloud Hub: [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) 
  * Use Gemini Cloud Assist chat: [Gemini Cloud Assist User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Making changes based on your analysis of costs might require additional permissions or coordination with a member of your organization who has the required permissions.

## View Gemini generated insights

Gemini Cloud Assist insights about recent changes can help you to quickly get a sense of the overall cost and utilization in your project or application.

  1. Open the **Optimization** page.

[Go to Optimization](https://console.cloud.google.com/cloud-hub/optimization)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

  3. Expand the **Insights generated by Gemini** section. Gemini Cloud Assist summarizes cost changes and resource usage that might have contributed to the cost change.

The following example shows a 78.6% increase in costs compared to the previous 7 days primarily driven by heavy query usage in BigQuery and a sustained spike in a Compute Engine instance.

![ ](https://docs.cloud.google.com/hub/images/cho-insights.png)

  4. To ask a question about the insights, click **Ask a follow up question**. The **Cloud Assist** panel opens.

  5. Enter a prompt. For examples of questions you can ask, see Prompt examples.




## Learn about costs in Gemini Cloud Assist chat

You can start a cost analysis directly from Gemini Cloud Assist chat:

  1. In the Google Cloud console, go to any page—for example, the **Optimization** page.

[Go to Optimization](https://console.cloud.google.com/cloud-hub/optimization)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

  3. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**. The **Cloud Assist** panel opens.

  4. Enter a prompt. For examples of questions you can ask, see Prompt examples.




## Prompt guidelines and examples

In Gemini Cloud Assist chat, you can get assistance by using natural language _prompts_ (questions or statements).

Gemini Cloud Assist uses data from the App Optimize API for cost-related questions about utilization, the same API that provides data for the Cloud Hub Optimization page.

For details about cost and utilization data that the App Optimize API provides to Gemini Cloud Assist, see [About resource costs](https://docs.cloud.google.com/hub/docs/optimization-data#cost-data).

### Prompt guidelines

Use the following information to help you write your prompts:

  * **Dates** \- You can specify date ranges, such as `2025-10-1 to 2025-10-31`. 
    * If you don't specify a date range, the default date range is the previous 7 days.
    * Prompts for data from the previous week set the date range to the last Monday to Sunday period.
    * Prompts for data from the previous month set the date range to the last calendar month.
  * **Applications** \- For App Hub applications, you must specify the application name in your prompt, even if you are viewing a page in Google Cloud console that is showing data for an application. The application name is the unique identifier for the application, such as `web-store`. If you use the display name for the application, such as "Web store", Gemini Cloud Assist might parse your prompt incorrectly.
  * If you ask about multiple projects or applications in a single chat session, include the project ID or application name in follow-up questions so that the context is clear. If you don't specify a project in your prompt, Gemini Cloud Assist uses the project you selected in the project picker.
  * **Cost analysis data** : Gemini Cloud Assist can suggest explanations for cost changes based on resource usage or Cloud Billing SKU usage for [supported resources](https://docs.cloud.google.com/hub/docs/optimization-data#resource-costs).



### Prompt examples

This section provides examples of prompts for analyzing costs.

#### Get cost and utilization data

The following example prompts show general questions about cost and utilization:

**Prompt** | **Type of response**  
---|---  
"How much did I spend on this project last month?"  | A summary of costs in the last calendar month for the selected project.   
"How much did my GKE cluster `my-cluster-id` cost me last month?"  | A summary of costs for the cluster `my-cluster-id` in the last calendar month.   
"Show me my costs in us-central1."  | A summary of resource costs in the selected project in the region `us-central1` over the last 7 days.   
"What were the least cost efficient resources last month for my app `my-favourite-app`?"  | A list of the least cost efficient resources in the application `my-favourite-app` in the last month.   
"What are my most overprovisioned resources that are costing me the most?"  | A list of the most overprovisioned resources in the selected project in the last 7 days.   
  
#### Analyze cost changes

For [supported resources](https://docs.cloud.google.com/hub/docs/optimization-data#resource-costs), Gemini Cloud Assist can use resource-level costs, SKU data, and operational data such as logs and metrics to provide an explanation for cost changes.

For example, you can use these prompts to get additional information about cost changes:

  * "Compare my costs between 2026-02-01 and 2026-03-01"
  * "Why did my costs go up in the last 5 days?"
  * "Why is the cost change so large today?"
  * "Can you explain why prod-cluster cost more this week?"



As Gemini Cloud Assist generates a response, the research process is displayed in the chat panel. You can hide this information by clicking **Hide process**.

When the research process is done, Gemini Cloud Assist provides its response. To view details about the research for the response, click **View research**.

The following example prompt asks about an increase in project costs in the past month.
    
    
    Why did my costs increase this month?
    

In this example, Gemini Cloud Assist analyzed the cost trend in May and June 2026. Based on Cloud Billing data, it identified an increase in costs for the Cross-Regional Proxy Instance Charge SKU in Cloud Load Balancing. It then analyzed resource usage and audit logs to determine that the source of these increased costs was 20 new forwarding rules that were created on May 21, 2026.

![Example prompt response and research details](https://docs.cloud.google.com/hub/images/cho-chat-example.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
