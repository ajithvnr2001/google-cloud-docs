---
url: https://docs.cloud.google.com/chronicle/docs/agentic-soc/security-tokens/
title: Google SecOps Agentic SOC Security Tokens pricing and billing \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:58.606492+00:00
---

# Google SecOps Agentic SOC Security Tokens pricing and billing  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/agentic-soc/security-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps Agentic SOC Security Tokens pricing and billing

This page describes the billing, metering, and contract framework for agentic consumption within Google Security Operations, introducing the Security Token model. For additional service specific terms, see [SecOps Service Specific Terms](https://cloud.google.com/terms/secops/service-terms).

## What are Google SecOps Security Tokens

Google SecOps uses a single-unit consumption metric called Security Tokens to measure the activity of autonomous Google security agents.

  * **Token-consuming operations** : Tokens are consumed by generally available security agents only. These agents are invoked automatically (for example, auto alert triage) or manually using the web interface, CLI, chat, or Model Context Protocol (MCP).

  * **Non-consuming operations** : Assistive features, such as standard chat panels and automated summaries, along with preview agents, don't consume security tokens.




## Billing and metering models

Security Tokens use a _Commit and Overage_ billing model. The product uses global price list across all supported Google SecOps regions.

### Allocation hierarchy and consumption order

While an agent works, the system evaluates and routes token consumption through available token pools using the following strict hierarchy:

  1. **Complementary and included Token entitlement (Daily):** Provided automatically to Enterprise Plus and Google Unified Security (GUS) deployments. This entitlement is allocated daily, resets at _00:00 US Pacific Time (UTC -7:00)_ , and doesn't roll over. Enterprise tiers don't receive a complimentary daily allotment.

  2. **Paid subscription tokens (annual):** Purchased tokens that apply across any generally available agent. These tokens are valid for a 12-month contract period and don't roll over to subsequent terms or ramp periods.

  3. **Overage:** Triggered automatically only after both the daily complimentary allocation and annual paid subscription balances are completely exhausted within a term or ramp period.




### Included allotment tiers (daily)

Customers with Google SecOps Enterprise Plus and GUS subscriptions receive a daily allotment of complimentary Security Tokens.

The number of complimentary Security Tokens you receive is based on the Annual Contract Value (ACV) of your underlying eligible Google SecOps package:

  
**Token allotment tier** |   
**Google SecOps package annual contract value (ACV)** |   
**Included daily Token allotment**  
---|---|---  
  
**Tier 1** |   
Less than $1,000,000 USD |   
10 million Tokens  
  
**Tier 2** |   
$1,000,000 – $5,000,000 USD |   
20 million Tokens  
  
**Tier 3** |   
Greater than $5,000,000 USD |   
60 million Tokens  
  
## Token allocation

  * For customers provisioned after July 1, 2026, all daily included tokens are allocated to the first tenant.

  * For customers provisioned before July 1, 2026, all daily included tokens are allocated on the tenant with the highest data ingestion per customer. Customers can contact Google Cloud support to request a re-allocation or distributions of free tokens across multiple tenants.




## Purchase Security Tokens

Security Tokens cannot be purchased as a standalone product. They are sold as an add-on SKU to the following Google SecOps subscriptions:

  * Google SecOps Enterprise

  * Google SecOps Enterprise Plus

  * GUS




### Term length and co-termination rules

  * **Term limits:** The maximum individual term length for a token subscription is 12 months.

  * **Multi-year agreements:** Multi-year agreements must use an annualized ramp structure for token allocations. These ramps don't need to strictly match the core Google SecOps ingestion structure. Unused tokens expire at the end of each ramp period and don't roll over.

  * **Co-termination:** The contract end-date for the token SKU cannot exceed the end-date of the primary Google SecOps deployment. Strict co-termination is supported, but not mandatory.

  * **Cloud commitments:** Existing Google Cloud commitments can be applied to the purchase of {google_secops_name_short} Security Tokens. Note that you cannot directly transfer Gemini tokens sourced using Vertex AI or Gemini Enterprise Google SecOps agents to run first-party. However, you can use them for custom, customer-built security agents running independently on Vertex AI.




## Tenant budgets and overage protections

To prevent unexpected overage bills due to misconfigurations or runaway workflows, the platform enforces several programmatic limitations:

  * **Per-tenant activation:** Paid token consumption must be explicitly activated on a per-tenant basis. This prevents test or sandbox environments from accidentally consuming tokens.

  * **Built-in agent limits:** Every GA agent includes built-in consumption limits to stop runaway logic loops or misconfigurations.

  * **Consumption ceilings:** Administrators can configure explicit daily consumption limits for paid tokens using the Google SecOps web interface or the Chronicle API.




## Token consumption metrics and estimates

Security investigations vary depending on log density, time windows, and threat complexity. Token usage for each alert can fluctuate. For example, network-layer hunts or automated deep-dive investigations typically consume more tokens than localized endpoint checks.

Use the following strategies to project and evaluate your token consumption before signing long-term contract commitments:

  * **90-day evaluation period:** New deployments include a 90-day trial window to execute agents and monitor consumption trends using Google SecOps dashboards.

  * **Pre-GA visibility:** Before a preview agent transitions to general availability, you can check its simulated token consumption profile to calculate its future impact.




Customers subscribed to Enterprise, Enterprise Plus, and GUS packages require Security Tokens to operate these agents. Given the non-deterministic nature of Agentic AI, the tokens consumed by a particular agent are calculated upon the successful completion of each agent execution.

The tokens needed depend on the agents you run. Each has their own average token consumption, but the true number comes from your environment.

## Token controls

If you only use the included tokens (for Enterprise Plus and GUS packages), when you run out of entitlement tokens, you won't be able to start new agents. However, any agents that have started run to completion.

If you have paid tokens, you start using them after you have consumed the included tokens. If you run out of this year's purchased tokens, you get an overage, unless you set a limit.

## Agentic AI feature

The following Agentic AI feature is available for use with Google SecOps Security Tokens:

[Triage and Investigation Agent (TIN)](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent)

## Important: Trial period

The official trial period has ended. If you are interested in extending the trial or are a new customer please reach out to your Google SecOps account representative

If your organization purchases a paid subscription to Google SecOps Security Tokens with a start date prior to July 1, 2026, your paid subscription term begins on the date listed on your Order Form. However, consumption of purchased Security Tokens against your paid subscription won't begin until August 31, 2026.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
