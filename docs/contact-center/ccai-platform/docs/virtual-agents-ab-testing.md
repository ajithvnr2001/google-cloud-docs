---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-ab-testing/
title: CCAI Platform conversational agent A/B testing \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:22.251439+00:00
---

# CCAI Platform conversational agent A/B testing  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-ab-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CCAI Platform conversational agent A/B testing Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to configure A/B testing of conversational agents using CCAI Platform.

## Why A/B test virtual agents?

A/B testing (or split testing) is a powerful methodology for optimizing the performance of conversational AI. Instead of relying on intuition when updating a flow, you can let real-time data guide your decisions.

Core benefits include the following:

  * **Risk mitigation:** Test a new "Agent B" with a small percentage of traffic (for example, 10%) before a full rollout to ensure that it doesn't negatively impact containment rates.
  * **Performance comparison:** Compare specific KPIs such as Intent Matching Accuracy, Task Completion Rate, and Customer Sentiment across different versions.
  * **Iterative refinement:** Experiment with different prompts, personas, or LLM-backed generators to find the most effective way to resolve user queries.



## Configure testing

This section explains how to configure CCAI Platform to support A/B testing for the capabilities of an agent. This applies to both voice agents and digital channels such as mobile and web.

### Prepare your virtual agents

Before configuring the telephony or routing, ensure you have two separate virtual agent targets ready in your environment. Refer to the documentation for configuring virtual agents. You will likely need two separate conversational profiles. The actual conversational agents could be separate agents or they could be the same agent with a different environments.

  * **Agent A (control):** Your existing, stable virtual agent.

  * **Agent B (variant):** The agent containing the new features, prompts, or logic changes that you want to test.




### Create dedicated CCAI Platform queues

In the CCAI Platform portal, you need to establish a hierarchy of queues to manage the traffic flow. This will depend on whether you are using voice or digital channels. Refer to the documentation for further details on creating queues.

  1. **Create queue A:** Navigate to Queue Management. Create a new queue named Queue_A_Test. Assign virtual agent A as the primary handler for this queue.

  2. **Create queue B:** Create a second queue named Queue_B_Test. Assign virtual agent B as the primary handler for this queue.

  3. **Create parent (entry) queue:** Create a queue named Main_Entry_Point. This queue won't have a virtual agent assigned directly; it will act as the "traffic splitter."




## Implement routing logic

To distribute traffic, you must configure the routing rules in the Main_Entry_Point queue. This will leverage the automatic redirection feature to specify the routing groups. Each routing group will include the routing to the relative queue. The percentage allocation will also be associated with the specific routing group. Refer to the documentation for further details on configuring the routing rules.

### Define the traffic split

You will use a percentage-based distribution rule. This lets you control exactly how much volume each agent receives.

**Component** | Logic | Goal  
---|---|---  
**Trigger** | All incoming calls or chats to `Main_Entry_Point`. | Catch all traffic.  
**Action 1** | Route **X** % of traffic to `Queue_A_Test`. | Establish the control group.  
**Action 2** | Route Remaining % of traffic to `Queue_B_Test`. | Establish the test group.  
  
### Configuration workflow

  1. Open the **Automatic Redirection** configuration for your `Main_Entry_Point` queue.
  2. Add a **group**.
  3. Select the **redirection selection** of Queue.
  4. Select the queue that should be associated with this routing group A.
  5. Select **Percentage Split**.
  6. Select **Add**.
  7. Add a **group**.
  8. Select the **redirection selection** of Queue.
  9. Select the queue that should be associated with this routing group B.
  10. Select **Percentage Split**.
  11. Select **Add**.
  12. Define your ratio (for example, 50/50 for a balanced test, or 90/10 for a canary release).
  13. Save the configuration.



## Monitor and analyze

When the traffic is flowing, use the CCaaS Analytics Dashboard to compare the performance.

  * Filter reports by `Queue_A_Test` versus `Queue_B_Test`.
  * Look for statistical significance in **Average Handle Time (AHT)** and **Transfer Rate to Human Agent**.
  * Look at the conversational agent analytics to look for any additional details that would indicate a positive or negative impact to performance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
