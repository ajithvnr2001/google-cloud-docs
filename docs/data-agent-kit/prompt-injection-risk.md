---
url: https://docs.cloud.google.com/data-agent-kit/prompt-injection-risk/
title: Mitigate indirect prompt injection risks from Google Cloud MCP \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:54.370037+00:00
---

# Mitigate indirect prompt injection risks from Google Cloud MCP  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/prompt-injection-risk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Mitigate indirect prompt injection risks from Google Cloud MCP Stay organized with collections  Save and categorize content based on your preferences. 

Coding agents are often deployed locally on a user's workstation leveraging authority delegated by their controlling user to access data. Generally, coding agents run with all the privileges of the user, but unlike humans are susceptible to prompt injection dictating their actions. This can pose risks to your infrastructure and data that you should consider.

Agents may erroneously interpret data as instructions, sometimes referred to as indirect prompt injection. For instance, a malicious actor may create some malicious prompts, share with a victim directly (e.g., in an email or calendar) or indirectly (e.g., by including them in Cloud Storage or BigQuery) and wait for the agent to act on these malicious prompts.

To help reduce risk, we recommend you consider the following additional guardrails.

  1. Run the agents in a constrained environment when possible. A canonical example is to have users bring up agents only on Cloud Workstations, disabling internet access and without root privileges. We also recommend [configuring VPC-SC](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters) protections on Cloud Workstations.

  2. [Organization Restriction Header](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions) – As an alternative, organizations with network security proxies at the boundary of their corporate network can enable the Organization Restriction Header. When deployed, this will restrict the set of resources accessible from the corporate network to a particular set of Google Cloud Organizations (such as the home organization of the enterprise), blocking agents (and humans) from accessing resources outside of the corporate tenant of Google Cloud. If your organization already uses an egress proxy, [it may support this feature](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/validated-solutions) out of the box.

  3. [Principal Access Boundaries (PAB)](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create) – PABs provide the ability to limit the set of resources that a particular set of identities can access. For coding agents, the agents can either run as their own identity (for example, a service account or the newly available [Agent Identity](https://docs.cloud.google.com/agent-builder/agent-engine/agent-identity) supported by Vertex AI Agent Engine) or using delegated authority from the user. PABs can be enabled to restrict access to only the organization's resources in either case, though applying the limit to human identity will also limit the access of the human.

**Note:** Humans are subject to the same kinds of phishing risks as agents via public data sets, but other security controls in the enterprise may be better suited to manage those risks than they are for agents.
  4. [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls) \- Organizations that include their corporate network within a VPC Service Controls perimeter are already protected from these risks when directly originated from outside of the VPC perimeter. Organizations that are concerned with data exfiltration through Google Cloud, including via agents, may want to consider whether VPC Service Controls makes sense in their environment.

  5. [Model Armor](https://docs.cloud.google.com/model-armor) \- Enable Model Armor to detect and block potential prompt injection attacks from data accessed through Google’s managed MCP servers.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
