---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-gemini/
title: Accelerate diagnosis with Gemini Cloud Assist \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:22.608910+00:00
---

# Accelerate diagnosis with Gemini Cloud Assist  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Accelerate diagnosis with Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Troubleshooting complex Google Kubernetes Engine (GKE) issues can be time-consuming, even with standard tools. Deciphering cryptic error messages or identifying subtle patterns in logs and metrics often requires deep expertise.

Use this page to see how Gemini Cloud Assist accelerates the diagnosis of complex problems by analyzing error messages, recommending solutions, and performing automated investigations to help you find the root cause faster.

This information is important for Platform admins and operators seeking to quickly understand and resolve cluster or node-level issues, for Application developers needing to debug application errors and interpret complex stack traces, and for Security specialists looking to use AI-powered analysis to identify potential security-related anomalies or misconfigurations. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Access Gemini Cloud Assist

To access Gemini Cloud Assist, complete the following steps:

  1. In the Google Cloud console, go to any page.
  2. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens. You can click example prompts if they are displayed, or you can enter a prompt in the **Enter a prompt** field.




## Explore example prompts

To help you understand how Gemini Cloud Assist can help you, here are some example prompts:

**Theme** | **Scenario** | **Example prompt** | **How Gemini Cloud Assist can help**  
---|---|---|---  
Confusing error message | A Pod has the `CrashLoopBackoff` status, but the error message is hard to understand. | What does this GKE Pod error mean and what are common causes: `panic: runtime error: invalid memory address or nil pointer dereference`? | Gemini Cloud Assist analyzes the message and explains it in clear terms. It also offers potential causes and solutions.  
Performance issues | Your team notices high latency for an app that runs in GKE. | My `api-gateway` service in the `prod` GKE cluster is experiencing high latency. What metrics should I check first, and can you suggest some common GKE-related causes for this? | Gemini Cloud Assist suggests key metrics to examine, explores potential issues (for example, resource constraints, or network congestion), and recommends tools and techniques for further investigation.  
Node issues | A GKE node is stuck with a status of `NotReady`. | One of my GKE nodes (`node-xyz`) is showing a `NotReady` status. What are the typical steps to troubleshoot this? | Gemini Cloud Assist provides a step-by-step investigation plan, explaining concepts like node auto-repair and suggesting relevant `kubectl` commands.  
Understanding GKE | You're unsure about a specific GKE feature or how to implement a best practice. | What are the best practices for securing a GKE cluster? Is there any way I can learn more? | Gemini Cloud Assist provides clear explanations of GKE best practices. Click **Show related content** to see links to official documentation.  
  
For more information, see the following resources:

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



## Use Gemini Cloud Assist Investigations

In addition to interactive chat, Gemini Cloud Assist can perform more automated, in-depth analysis through [Gemini Cloud Assist Investigations](https://docs.cloud.google.com/cloud-assist/investigations). This feature is integrated directly into workflows like Logs Explorer, and is a powerful root-cause analysis tool.

When you initiate an investigation from an error or a specific resource, Gemini Cloud Assist analyzes logs, configurations, and metrics. It uses this data to produce ranked observations and hypotheses about probable root causes, and then provides you with recommended next steps. If you have a [support package](https://cloud.google.com/support), you can also transfer the investigation results to a Google Cloud support case, providing additional context that can help resolve your case faster.

## What's next

  * Read [Put it all together: Example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example) (the next page in this series).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
