---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini/
title: Design AI infrastructure with Compute Advisor \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:46.014629+00:00
---

# Design AI infrastructure with Compute Advisor  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Design AI infrastructure with Compute Advisor Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to plan and design your GPU instances or cluster by prompting the Compute Advisor, an AI-powered interface that is powered by Gemini. To learn more about the components that you must configure before or when you create a cluster, see [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview). 

Compute Advisor helps you evaluate hardware options, estimate deployment costs, and view recommended configurations for your clusters. To tailor its recommendations, Compute Advisor evaluates your Google Cloud project by checking your quota limits, existing reservations, [committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview), [default region and zone](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region), and any [resource location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). By using Compute Advisor to help with your planning, you can reach an optimal configuration for your workload before you create or modify a cluster. 

## Limitations

When you prompt Compute Advisor in the Google Cloud console, you can't directly create, modify, or delete resources.

## Before you begin

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication.

### Required roles

To get the permissions that you need to access and prompt Gemini, ask your administrator to grant you the [Cluster Director Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to access and prompt Gemini. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to access and prompt Gemini:

  * To view a list of clusters: `hypercomputecluster.clusters.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access Compute Advisor in the Google Cloud console

To access Compute Advisor in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Compute Advisor** page.

[Go to Compute Advisor](https://console.cloud.google.com/compute/advisor)

  2. When the page is ready, you can view the following:

![Interface elements of the Compute Advisor page.](https://docs.cloud.google.com/static/cluster-director/images/gemini-ui.png)

The UI elements that are displayed in the preceding screenshot are the following:

     * **Conversation history side panel** : shows your recent chats. You can interact with this panel as follows:

       * To start a new conversation, click **New chat**.

       * To resume a recent conversation, in the **Recent chats** section, click the conversation.

       * To view a list of all your conversations, click **View all**. On the **My history** page, you can view the details of a past conversation and resume it, or delete conversations if you no longer need them.

     * **Quick-action prompt cards** : a set of cards that each contain a sample prompt. If you click a card, then the Google Cloud console automatically populates the prompt box with the sample prompt.

     * **Prompt box** : this field lets you enter and submit prompts. To submit a prompt, click **Submit prompt**. 




## Prompt Compute Advisor

After you submit a prompt, Compute Advisor starts to generate a response. A pane appears and Google Cloud console displays the response to your prompt in the pane, as shown in the following screenshot:

![Generated recommendation response in the Compute Advisor pane.](https://docs.cloud.google.com/static/cluster-director/images/gemini-ui-prompt.png)

Based on your prompt, the response pane includes the following elements:

**Caution:** Generative AI can make mistakes. Before taking any actions on a resource that Compute Advisor recommends you to create, modify, or delete, validate all recommendations and configurations.

  * **Contextual grounding** : Compute Advisor automatically evaluates your project context to deliver highly tailored recommendations, including quota limits, existing reservations, CUDs, your default region and zone, and any resource location constraints.

  * **Interactive code snippets** : Compute Advisor generates gcloud commands, REST API methods, or Terraform resources. You can copy and paste these code snippets or run them in Cloud Shell.

  * **Visual canvas** : Compute Advisor organizes recommendations into structured tables and side-by-side comparisons. This view helps you evaluate product features and architectural approaches. It also provides an implementation plan for your use case.




The following sections outline the best practices for writing prompts, and example prompts that you can use before you create or modify a cluster. 

### Best practices for prompts

To get the most accurate and actionable recommendations from Compute Advisor, we recommend that you structure your prompts in the same way that you would do a code block. This approach guides the generative AI by using clear parameter declarations, role definitions, specific instructions, and explicit output formats.

When you prompt Compute Advisor, consider the following best practices:

  * **Focus on design and planning** : we recommend that you don't prompt Compute Advisor for troubleshooting cluster errors. To resolve these errors, see instead [Troubleshoot creating, updating, and deleting compute instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation). 

  * **Specify a persona or role** : declare a target role or persona, such as an IT administrator, AI researcher, or platform engineer, for Compute Advisor to adopt. This approach guides the tone, depth, and expertise level of the resulting recommendations.

  * **Provide explicit, numbered instructions** : break your objective down into concrete, step-by-step questions or tasks. This approach structures the Compute Advisor's reasoning process and helps ensure that Compute Advisor addresses all of your requirements.

  * **Define a specific output format** : explicitly state how you want the recommendation to be formatted, such as a walkthrough explanation, a Markdown comparison table, or a ready-to-use gcloud code block.

  * **Leverage automatic context grounding** : you don't need to include your default region or zone, available quotas, CUDs, or resource location constraints into your prompt. Compute Advisor can access this information in your Google Cloud project.

  * **Iteratively refine your designs** : you can modify or expand the response that Compute Advisor generated by sending new prompts. For example, you can ask the assistant to add networking recommendations to your deployment plan or modify the storage requirements without starting a new conversation.




### Example prompts

The following are examples of prompts that you can use to help you design and optimize your cluster:

  * **Cluster topology and placement strategy** : to determine the optimal deployment model and placement policy for a high-performance AI workload, use a prompt like the following:
        
        Act as an AI researcher. I need to design a GPU cluster topology in
        Cluster Director to train a foundation large language model that
        maximizes ML goodput and secures accelerator capacity. Please provide the
        following:
        
        1. A comparison of clustered GPU machine series across available regions.
        2. An explanation of how compact placement policies and workload policies
           reduce network latency and boost goodput.
        3. The optimal configuration for future reservations in
           AI Hypercomputer to secure capacity for this workload.
        
        Format the comparison as a Markdown table, and provide the deployment steps
        as a ready-to-use gcloud code block.
        

  * **Provisioning model and cost optimization** : to evaluate provisioning models and reduce batch processing costs, use a prompt like the following:
        
        Act as an IT administrator. I need to select the most cost-effective
        consumption option to run large fault-tolerant AI batch jobs on clusters in
        Cluster Director without data loss. Please provide the following:
        
        1. A cost and availability comparison of Flex-start VMs against
           Spot VMs for AI workloads.
        
        2. An explanation of how atomic allocation in Flex-start VMs
           provisions all accelerator nodes at the exact same time.
        
        3. A cluster configuration with checkpoint storage to save model state
           before Compute Engine reclaims a Spot VM.
        
        Format the comparison as a Markdown table, and provide the configuration
        steps to complete in the Google Cloud console.
        




## What's next

  * To review how to obtain capacity and quota in AI Hypercomputer, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).

  * To compare accelerator options and select the right GPU series, see [Choose between general GPUs and clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).

  * To select tools and create your cluster, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
