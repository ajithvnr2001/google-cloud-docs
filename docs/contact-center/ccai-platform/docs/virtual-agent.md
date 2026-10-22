---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent/
title: About virtual agents \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:43.044686+00:00
---

# About virtual agents  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  About virtual agents Stay organized with collections  Save and categorize content based on your preferences. 

Virtual agents use generative artificial intelligence (Generative AI) and natural language processing to handle support cases. Contact Center AI Platform (CCAI Platform) virtual agents are based on [Dialogflow](https://docs.cloud.google.com/dialogflow/docs) or [Gemini Enterprise for Customer Experience](https://docs.cloud.google.com/customer-engagement-ai). You can use virtual agents as your first line of customer support or you can configure them to handle support requests with limited to no human agent intervention.

You can use virtual agents in the following ways:

  * Configure multiple virtual agents that focus on specific issues and assign them to specific queues.

  * Assign a virtual agent to answer incoming calls or chats, or use existing routing options at the queue level.

  * Let your human agents receive escalations from virtual agents.




## End-user experience

Sessions can be passed seamlessly from a virtual agent to a human agent. If a virtual agent reaches the limit of its knowledge or if it experiences a technical issue, it can automatically escalate the session and display a message to the end-user. The session is placed in a queue where it can be handled by a human agent.

**Note:** Google recommends assigning a human agent to the same queue as a virtual agent. This provides an additional escalation path in case there's a failure escalating to a different queue.

### Chats

Except for the virtual agent's configurable name and avatar, there is no noticeable difference between a virtual agent and a human agent in the end-user's user interface.

You can add a **Skip to Human Agent** button to the chat interface, which lets end-users skip the virtual agent and connect directly with a human agent. You can also configure user segments in your CRM to have specific groups of end-users (for example, VIPs) bypass the virtual agent automatically.

### Calls

Virtual agents for calls use pre-programmed voice prompts and responses to interact with your end users. They can also use Generative AI to support complex conversations. You can build flows to escalate end-users to human agents or to prevent escalations. You can use your own voice talent to supply audio recordings or use a generated voice from text that you supply.

## Agent experience

The agent experience changes only slightly. Human agents can see that a session was escalated from a virtual agent in the CRM and the agent adapter. For chats, human agents can see a conversation with a virtual agent in the chat adapter.

Human and virtual agents can transfer calls or chats to queues and to each other. Queues attended by virtual agents are labeled to inform human agents.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
