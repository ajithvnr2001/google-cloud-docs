---
url: https://docs.cloud.google.com/iap/docs/agent-overview/
title: IAP for agents overview \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:55.386023+00:00
---

# IAP for agents overview  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/agent-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  IAP for agents overview Stay organized with collections  Save and categorize content based on your preferences. 

Agents require secure, governed access to a vast array of tools and services. In Gemini Enterprise Agent Platform, security administrators can govern inline, agent-to-anywhere access by using [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).

You can grant Identity and Access Management (IAM) privileges to _source agents_ , which are agents that access Agent Gateway. You grant access by binding [IAM allow and deny policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview) on Agent Registry service instances. Agent Gateway services include MCP servers, _destination agents_ , and endpoints. When granting IAM roles to agents, Agent Registry services are also known as _resources_.

Agent Gateway uses Identity-Aware Proxy (IAP) to enforce IAM allow and deny policies.

To learn more about how IAP uses IAM for policy enforcement in Gemini Enterprise Agent Platform, see [Policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview) in the Agent Platform documentation.

## What's next

  * [Read about Agent Gateway and IAP in Gemini Enterprise Agent Platform.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
  * [Understand how IAP enforces policies in Gemini Enterprise Agent Platform.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview)
  * [Manage an IAP policy in Gemini Enterprise Agent Platform.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/assign-identity-iam)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
