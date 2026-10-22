---
url: https://docs.cloud.google.com/capacity-planner/docs/capacity-assist/
title: Plan capacity with Capacity Assist \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:06.689762+00:00
---

# Plan capacity with Capacity Assist  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/capacity-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Plan capacity with Capacity Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

This document describes how you can use AI-powered assistance through Gemini in Capacity Planner to help you better understand and manage your resource usage and plan capacity. It is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

Capacity Assist lets you use natural-language prompts to do the following:

  * Analyze historical usage patterns across regions and resources.

  * Forecast capacity needs and identify quota risks early.

  * Simulate growth events to plan future capacity.

  * Get fast answers to your Capacity Planner questions.




Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for capacity planners, platform administrators, cloud architects, and FinOps operators. You don't need prior experience with Capacity Planner to use Capacity Assist. To learn more about Capacity Planner, see the [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview).

## Before you begin

  1. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/gemini/docs/cloud-assist/set-up-gemini).

  2. In the Google Cloud console, on the project selector page, select the Google Cloud project that Gemini Cloud Assist is set up for:

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) for your Google Cloud project.




### Required roles

To get the permissions that you need to use Capacity Assist in Capacity Planner, ask your administrator to grant you the following IAM roles on the project, folder, or organization: 

  * To view capacity and usage in Capacity Planner: [Capacity Planner Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use Capacity Assist in Capacity Planner. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use Capacity Assist in Capacity Planner:

  * To view the forecasted usage of your resources: `capacityplanner.forecasts.list` on the project, folder, or organization 
  * To view the usage of your resources: `capacityplanner.usageHistories.list` on the project, folder, or organization 
  * To summarize the usage of your resources: `capacityplanner.usageHistories.summarize` on the project, folder, or organization 
  * To view quotas: 
    * `serviceusage.quotas.get` on the project
    * `serviceusage.services.get` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Analyze your capacity and usage

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To enter prompts in Capacity Assist, follow these steps:

  1. In the Google Cloud console, go to the **Capacity Planner** page. Capacity Assist includes information about the current Google Cloud console page and project when generating a response to your prompt.

[Go to Capacity Planner](https://console.cloud.google.com/capacity)

  2. Click spark **Ask Capacity Assist**.

The **Capacity Assist** panel appears.

  3. In the **Capacity Assist** panel, enter a natural language prompt about your capacity and resource usage. For example, you might enter the following:
         
         Based on my max usage forecast for the next 3 months, in which regions am I predicted to run out of quota for N2 VMs?

  4. Click send **Send prompt**.

Capacity Assist generates a response and recommendations based on your historical usage, forecasts, and quotas.


**Tip:** To improve the quality of responses, include specific resource types, regions, or time frames in the prompt. For example, `Based on my max usage forecast for the next 3 months, in which regions am I predicted to run out of quota for N2 VMs?`.

### Examples of capacity planning prompts

The following table provides examples of prompts that you can use with Capacity Assist:

Prompt | Type of response  
---|---  
"Analyze historical usage patterns for N2 VMs across all regions for the past 30 days." | Summarizes historical consumption patterns across regions and resource types.  
"Which regions have the highest growth rate for GPU consumption?" | Identifies regions with significant consumption increases and summarizes regional trends over time.  
"Assess my quota risks across the project for all resource types." | Evaluates rolling peak usage against allocated quota across regions, outputting predicted breach dates, estimated shortfalls, and actionable links.  
"Based on my max usage forecast for the next 3 months, in which regions am I predicted to run out of quota for N2 VMs?" | Compares maximum usage forecasts with quotas by region, highlighting predicted quota breaches.  
"I plan to scale up by 20% for my workload in this project. Provide a summary of my capacity usage and help me identify potential quota risks and a path forward." | Simulates growth impact on current usage and identifies potential quota risks and recommended paths forward.  
"I am planning a product launch for Project-Alpha that will increase my current traffic by 40% starting November 1. Do I have enough coverage, or do I need to create a capacity request?" | Overlays simulated traffic increase onto baseline peak usage, checks unreserved eligible quota and active capacity requests, and calculates any uncovered capacity gap.  
"What are the main use cases for Capacity Planner?" | Provides an overview of Capacity Planner capabilities, explaining how to analyze historical usage trends, evaluate quota risks, and simulate growth events.  
  
## Limitations

Before using Capacity Assist, consider the following limitations:

  * **Availability guarantees** : Recommendations and forecasts provided by Capacity Assist don't guarantee capacity availability unless backed by an approved [future reservation](https://docs.cloud.google.com/capacity-planner/docs/create-future-reservations).

  * **Scope of analysis** : Capacity Assist can't analyze any resources that you don't have permission to view in Capacity Planner.




## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Cloud Assist panel](https://docs.cloud.google.com/gemini/docs/cloud-assist-pane).
  * Learn [how Gemini products in Google Cloud use your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Read the [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview).
  * Learn how to [view usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
