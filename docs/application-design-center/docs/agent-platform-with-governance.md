---
url: https://docs.cloud.google.com/application-design-center/docs/agent-platform-with-governance/
title: Agent Platform with governance template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:36.842750+00:00
---

# Agent Platform with governance template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/agent-platform-with-governance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Agent Platform with governance template Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1). This feature provides capabilities to govern and secure AI Agents, so the "Agentic AI Services" Service Specific Terms apply. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).

This template uses Agent Gateway, which is in Private Preview. To request access to use Agent Gateway with Agent Runtime, see the [access request page](https://forms.gle/ZLNYKUDW7j2B4a8K7).

Deploy your agent to Gemini Enterprise Agent Platform to consistently apply security, governance, and observability settings for your agents. Connect your agent to an MCP server that supports data retrieval and analysis tasks that align with your governance policies.

This guide helps you understand the _Agent Platform with governance_ application template. You can use this template to quickly deploy your agent, along with its infrastructure and policies, as an application on Google Cloud.

For example, you might implement this template to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Governed data analyst for sensitive financial datasets | A financial services firm needs to use internal datasets to generate reports for analysts. They need to detect personally identifiable information (PII) and detect attempts to bypass internal data access rules. | The agent discovers and queries the financial database using a standardized protocol. Only the agent's specific identity can access the BigQuery tool. A final safety layer automatically blocks sensitive data and malicious prompts.  
Regional customer support agent with regional data residency | A global retail brand needs a customer support agent in a specific region to comply with data residency laws. The agent must be isolated so that its traffic only flows through specific, audited regional endpoints. | Regional gateways enforce data residency by pinning traffic to specific locations. Authorization policies provide a zero-trust posture, while all ingress and egress are funneled through regional modules to provide a comprehensive audit trail.  
Automated content moderator for community forums | A media company needs to scan user-submitted comments and flag them for removal. The company needs to separate moderation logic from safety policy. | Authorization extensions separate moderation logic from the safety configuration, while Model Armor identifies toxic content. The agent scales automatically on a managed runtime and uses the registry service to interact securely with the dataset.  
  
## Architecture

The following image shows the template components and connections:

![The agent platform application in the design canvas. The application includes ingress, request processing, data retrieval, and egress components.](https://docs.cloud.google.com/static/application-design-center/images/agent-platform-template.png)

The template components are organized in the following layers:

### Agent logic execution

  * [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent): hosts the agent logic in a managed serverless environment.



### Traffic management

  * [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview): a regional proxy that manages incoming traffic and directs requests into the agent environment. The egress component controls how and where the agent sends data or calls external APIs.

  * [Authorization Policy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview): Helps ensure that requestors have permission for requested actions. The following authorization policies are configured in this template:

    * Inbound requests.
    * Outbound requests.
    * Content validation.
  * [Authorization Service Extensions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization): provides a programmable hook to inject custom authorization logic into incoming and outgoing traffic flow.

  * [Model Armor Template](https://docs.cloud.google.com/model-armor/overview): inspects the model's input and output to block sensitive data leaks, jailbreak attempts, or toxic content.




### Data source connection

  * [Agent Registry service](https://docs.cloud.google.com/agent-registry/overview): a centralized catalog that lets you manage, version, and discover tools and services.

  * [Agent Registry MCP server](https://docs.cloud.google.com/agent-registry/register-mcp-servers): helps the agent discover and interact with Google Cloud data sources (BigQuery) using a standardized protocol.

  * [Identity-Aware Proxy (IAP) Agent Registry MCP server](https://docs.cloud.google.com/iap/docs/concepts-overview): connects the Agent Runtime identity to the MCP server.

  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction): an example dataset and table used by the agent for data retrieval or analysis. This template demonstrates how you can apply governance policies to your agent's interactions with data sources through an MCP server.




## What's next

  * To learn how to duplicate and customize templates, see [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Plan your AI application strategy by [choosing your agentic architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
