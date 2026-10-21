---
url: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/
title: Offer AI agents through Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:05.661306+00:00
---

# Offer AI agents through Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Offer AI agents through Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. You can use Google Cloud Marketplace to offer AI agents to your customers through multiple flexible deployment models. Your agents can be built on any framework, use any communication protocol, run on any runtime (Google Cloud or beyond), and be consumed in various forms and surfaces.

## Before you begin

  * If you're new to offering software on Cloud Marketplace, [sign up to become a vendor](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#initiate-onboarding). 
  * To get access to Producer Portal, complete the _Cloud Marketplace Project Info Form_ , provided by the Cloud Marketplace team. 



## Choose how to offer your AI agents

You can publish and offer your AI agents on Cloud Marketplace using any of the following supported product types:

  * **AI Agents as a Service (A2A protocol)** : Offer AI agents that run on Google Cloud, integrate with Gemini Enterprise, and use the Agent2Agent (A2A) protocol to communicate and collaborate with other AI agents. For details, see Offer AI agents using the A2A protocol below.

  * **Software as a Service (SaaS)** : If your AI agent uses a different protocol (not A2A), you can offer it as a SaaS product with integrated billing. Your SaaS agent runs on Google Cloud or other infrastructure, and is billed by Google. To learn how to onboard a SaaS AI agent, see [Offer Software as a Service (SaaS) products](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas).

  * **Kubernetes apps for GKE and GKE Enterprise** : If you provide your AI agent as a containerized application, users can deploy and run it on their own Google Kubernetes Engine (GKE) clusters or their own infrastructure using GKE Enterprise. To learn how to onboard a Kubernetes-based AI agent, see [Offer Kubernetes apps](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes).

  * **Professional Services** : You can offer professional services related to AI agents, such as consulting, deployment, or offering customized AI agents as a service. To learn how to onboard professional services for AI agents, see [Offer professional services](https://docs.cloud.google.com/marketplace/docs/partners/professional-services).




## Offer AI agents using the A2A protocol

If you are offering an AI agent as a service that uses the A2A protocol and integrates with Gemini Enterprise, follow these specific requirements and steps.

AI agents from Cloud Marketplace use the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/topics/what-is-a2a/) to communicate and collaborate with other AI agents. For more information, see the [A2A protocol's documentation](https://a2a-protocol.org/latest/). For each AI agent that you offer through Cloud Marketplace, you must create an _Agent Card_ aligned to the [A2A Agent Card specification](https://a2a-protocol.org/dev/specification/). Your AI agent's Agent Card defines its presence on Cloud Marketplace, detailing its capabilities and facilitating its coordination with other AI agents. Agent Cards exist as JSON files stored in Cloud Storage.

After you've created your AI agent's Agent Card, use Producer Portal to create your AI agent's Cloud Marketplace listing and submit it for review. After you've published your AI agent, customers can get it from Cloud Marketplace and run a command to add it to Gemini Enterprise.

## Requirements for A2A AI agents

  1. All products that you offer through Cloud Marketplace must comply with the Cloud Marketplace listing requirements. If you offer A2A AI agents, they must meet the following additional requirement:
  2. Your A2A AI agents must not include professional services, hardware, or other non-software components that are billed through Cloud Marketplace.
  3. Be customer-ready, secure, and built for enterprise ecosystems.
  4. Be developed and operated in accordance with [Google's AI Principles](https://ai.google/principles).
  5. Be discoverable through primary Google surfaces, such as Gemini Enterprise.
  6. Use [Google foundation or 3rd party models hosted in Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) as a default configuration.
  7. Support multi-agent interoperability through the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/).



## Pricing models for A2A AI agents

You can choose one of the following pricing models for your AI agent:

  * **Free** : Customers only pay for the Google Cloud resources that they use.

  * **Subscription-based pricing** : Customers pay a flat monthly fee for using your AI agent. For partial months, the cost is prorated.

  * **Usage-based pricing** : Customers pay for your AI agent based on measurements that you choose, called _metrics_. If you choose a usage-based pricing model, then your app must measure and report usage information to Google.

  * **Combined pricing** : Customers pay a base subscription fee for using your AI agent, and additional charges based on their usage.




For more information about these pricing models, see [Pricing models for AI agents](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models).

## Overview of onboarding an A2A AI agent

Offering an A2A AI agent through Cloud Marketplace involves the following steps:

  1. Create your AI agent and its Agent Card. For more information about Agent Cards, see [Agent Cards](https://a2a-protocol.org/latest/topics/key-concepts/#agent-cards) in the A2A documentation.

  2. [Add your AI agent in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/add-product). You use Producer Portal to complete the process of onboarding your AI agent to Cloud Marketplace.

  3. [Add your AI agent's Agent Card](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/agent-card) in Producer Portal.

  4. [Add product details](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/product-details) for your AI agent's listing in Producer Portal.

  5. [Add pricing information](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing) for your AI agent in Producer Portal. It might take up to four business days for Google to review your AI agent's pricing model. You can continue integrating your AI agent while Google reviews the pricing model.

  6. [Integrate your AI agent with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/technical-integration). The integration includes modifying the frontend and backend of your software to do the following:

     * Create accounts for users.
     * Link the accounts to their Google accounts.
     * Provide a way for users to sign in using their Google credentials.
  7. [Publish your AI agent to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/publish). To publish your AI agent, you submit various parts of your AI agent's listing for review. The Cloud Marketplace team reviews each submission and works with you to resolve any issues before approving it. When all of your submissions are approved, Google operations begins validation and testing. After validation is complete, you are provided with a `gcloud` command to make your listing publicly visible.




## What's next

  * Review the [A2A Agent Card specification](https://a2a-protocol.org/dev/specification/) as you create your AI agent's Agent Card.
  * Review the available [pricing models for AI agents](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models).
  * [Add your AI agent](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/add-product) to Cloud Marketplace by using Producer Portal.



[ Next Pricing models for AI agents  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
