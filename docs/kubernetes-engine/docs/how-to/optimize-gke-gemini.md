---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-gke-gemini/
title: Fine-tune GKE services with Gemini assistance \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:43.204951+00:00
---

# Fine-tune GKE services with Gemini assistance  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-gke-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Fine-tune GKE services with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how you can fine-tune your Google Kubernetes Engine (GKE) deployments to optimize performance and reliability by using [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview), an AI-powered collaborator for Google Cloud. Gemini assistance can include recommendations, code generation, and troubleshooting.

Among many other benefits, Gemini Cloud Assist can help you achieve the following:

  * **Reduce costs** : identify idle resources, rightsize your deployments, and optimize autoscaling configurations to minimize unnecessary spending.
  * **Improve reliability and stability** : proactively identify potential issues, like version skew or missing Pod Disruption Budgets, to prevent downtime and ensure application resilience.
  * **Optimize AI/ML Workloads** : get help with deploying, managing, and optimizing AI/ML workloads on GKE.
  * **Simplify troubleshooting** : quickly analyze logs and pinpoint the root cause of errors, saving time and effort.



This page is for existing GKE users, and Operators and Developers who provision and configure cloud resources and deploy apps and services. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Costs

  * **Gemini** : While in Preview, there is no cost for using Gemini Cloud Assist.

  * **GKE** : There are no additional costs for using Gemini Cloud Assist in GKE.




## Before you begin

To begin using Gemini with GKE, complete the following prerequisites.

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Ask your [Identity and account admins](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins-identity) to grant you the necessary permissions to access and modify your GKE resources.
  * Follow the instructions provided in the [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini) guide to enable Gemini Cloud Assist in your project or folder, with specific Identity and Access Management (IAM) roles granted to your [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).



This guide assumes that you have a GKE cluster and, preferably some deployments running.

## Ask Gemini Cloud Assist

You can invoke Gemini Cloud Assist from the Google Cloud console. Gemini Cloud Assist lets you use natural language prompts to get help with tasks quickly and efficiently.

To open **Cloud Assist** from a GKE page, follow these steps:

  1. In the Google Cloud console, on the project selector page, select a Google Cloud project where you [enabled Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the Google Cloud console, go to a specific page on the **Kubernetes Engine** console.

For example, go to the **Kubernetes Engine Overview** page.

[Go to Kubernetes Engine Overview](https://console.cloud.google.com/kubernetes/overview)

If you have a question about a specific resource, navigate first to the relevant page. For example, on the [**Clusters**](https://console.cloud.google.com/kubernetes/list/overview) page, Gemini Cloud Assist can advise you about managing your clusters, monitoring your cluster health, and troubleshooting cluster issues. Using Gemini on a specific Google Cloud console page helps provide context for your questions. Gemini can then use this context, along with the overall project you're in, to generate more tailored and accurate assistance.

  3. To open the Gemini Cloud Assist pane, click the spark **Open or close Gemini AI chat** in the toolbar.

  4. If prompted, and you agree to the terms, click **Accept**.

  5. Enter a prompt in the Gemini pane. See an example workflow of using Gemini to troubleshoot in the following section.




For more information about using Gemini in the Google Cloud console, see [Use Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/cloud-assist-pane).

### Example of using Gemini to troubleshoot

Gemini can help you troubleshoot issues in your GKE services.

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Select the workload you want to troubleshoot.

  3. Click the **Logs** tab.

  4. Click the spark **Open or close Gemini AI chat** in the toolbar.

  5. Enter a prompt to describe the issue you are experiencing. For example, "My `accounts-db` database application is experiencing high latency". Gemini might ask for more context, such as the type of database, the scope of impact, such as the operations and users affected by the latency.

  6. Gemini can then provide guidance to analyze the logs yourself, and provide troubleshooting suggestions.

  7. Review and follow the suggestions to resolve the issue.




## Example prompts for Gemini Cloud Assist

This section shows some real-world use cases and suggests the prompts that you can try asking Gemini. The actual responses you receive might be generic, or they might be personalized and actionable based on the unique state of your Google Cloud environment. The responses could include Google Cloud console links for reviewing and managing your Cloud resources, and links to the relevant documentation for further information.

### Reduce costs

The following table describes the prompts you can use to help reduce costs.

**Prompt** | **Type of response**  
---|---  
"How can I save costs on my GKE clusters without sacrificing performance?" | 

  * Recommendations that identify and suggest the removal of underutilized resources, such as idle clusters.
  * Advice about enabling or adjusting autoscaling mechanisms.
  * Suggestions that highlight potential savings through configuration reviews, such as logging retention policies.

  
"I'm looking to upgrade my `my-docker-cluster` GKE cluster. Any recommendations?" | Suggestions to implement specific Kubernetes configurations and best practices, for example:  


  * Defining resource requests and limits for Pods to help ensure predictable resource allocation.
  * Using dedicated namespaces to isolate workloads.
  * Implementing Pod Disruption Budgets to help ensure that a minimum number of Pod replicas are available during voluntary disruptions, like node maintenance or upgrades.
  * Scheduling maintenance windows to manage planned disruptions and minimize unexpected downtime.
  * Enrolling clusters in release channels to manage GKE version upgrades.

  
"I have a large traffic spike coming in a couple of weeks on the `my-docker-cluster` cluster. Any recommendations?" | 

  * Strategies to scale the number of application Pods by using the horizontal Pod autoscaler.
  * Strategies to increase the resources (CPU, memory) per Pod by using the vertical Pod autoscaler.

  
"Which of my GKE workloads don't have HPA enabled?" | The list of workloads that don't have the horizontal Pod autoscaler enabled.  
  
### Improve reliability and stability

The following table describes the prompts you can use to help improve reliability and stability of your GKE workloads.

**Prompt** | **Type of response**  
---|---  
"How can I make my GKE clusters more reliable and prevent downtime?" | 

  * Identifies version skew in the clusters and suggests actions to maintain Kubernetes version compatibility. 
  * Provides recommendations to implement resource isolation.
  * Provides recommendations to configure Pod Disruption Budgets to maintain a minimum number of running Pod replicas during planned maintenance or upgrades.

  
"Show me how I can move my workloads from the `Default` namespace on `my-cluster`." |  Steps to do the following:  


  * Prepare a target cluster.
  * Migrate apps and data to the target cluster.
  * Switch over the services with minimal downtime.

  
"How do I ensure high availability for my running pods?" | 

  * A detailed procedure that specifies a Deployment that uses `podAntiAffinity`, and multiple replicas for redundancy.
  * Suggestions for setting resource requests and limits, and using horizontal Pod autoscaling.

  
  
### Optimizing GKE for AI/ML workloads

The following table describes the prompts you can use to get help with deploying, managing, and optimizing AI/ML workloads on GKE.

**Prompt** | **Type of response**  
---|---  
"What are the recommended node pool configurations for running large-scale distributed TensorFlow training on GKE with GPUs?"  | Recommendations to optimize distributed TensorFlow ML training on GKE can include the following:  


  * Selecting the right GPU and machine types.
  * Enabling autoscaling.
  * Optimizing network connectivity.
  * Leveraging distributed training frameworks.
  * Implementing cost-saving measures.

  
"How do I use GPUs on GKE for training?"  | Overview of the steps and considerations to configure a cluster and workloads to use GPUs.   
"Give me an example of deploying a model serving container on GKE."  | An example with sample code to deploy a model serving container on GKE. The example might incorporate best practices and helps ensures scalability.   
"What metrics should I track to assess the effectiveness of my load balancing setup for inference?"  | The list of metrics—like traffic distribution, latency, error rates, CPU, and memory utilization—to gain insights into the performance and health of the load balancing setup.   
  
### Simplify troubleshooting

The following table describes the prompts you can use to help quickly analyze logs and identify the root cause of errors, saving time and effort.

**Prompt** | **Type of response**  
---|---  
"What's this error about?  
`Readiness probe failed: Get "https://10…./abcd": context deadline exceeded (Client.Timeout exceeded while awaiting headers)`"  | Explains that the kubelet failed to execute the readiness probe for the container within the defined timeout period, and suggests potential causes and troubleshooting actions.   
"Why is my deployment `nettools` crashing with error `ping: socket: Operation not permitted`?"  | Explains that the `ping` command requires the `CAP_NET_RAW` Security Context capability, and that, by default, containers in Kubernetes run with a restricted set of capabilities for security reasons.   
"What does it mean when my pod is unschedulable due to the error `Cannot schedule pods: No preemption victims found for incoming pod.`"  | Explains how Pod scheduling and preemption works in Kubernetes. Lists steps to troubleshoot why no preemption victim was found.   
  
## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/gemini/docs/cloud-assist-pane).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
