---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview/
title: Overview of managed policy constraints \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:03.017004+00:00
---

# Overview of managed policy constraints  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview of managed policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.

This page provides an overview of managed organization policy constraints and their interactions.

## Policy enforcement dependencies

The enforcement of managed organization policy constraints for data stores depends on several factors: the type of data source you are configuring, whether your project is protected with VPC Service Controls, and whether your project is included in the `enforcedProjects` parameter.

Related policy or service | Description  
---|---  
**[Restrict allowed data sources for data connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources)** |  If you allow a data source, such as Google Drive or Gmail, in the **Restrict allowed data sources for data connectors** managed organization policy constraint, then the constraint automatically permits connections to its well-known FQDNs. This permission means you don't need to define these domains in the **Restrict egress domains for data connectors** managed policy constraint.  
  
For projects where the policy is enforced (VPCSC-enabled projects or projects listed in `enforcedProjects`), you must use the **Restrict egress domains for data connectors** policy to explicitly allow the necessary FQDNs for third-party data sources where FQDNs aren't automatically allowed.   
**[Restrict egress domains for data connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns)** |  For projects where the policy is enforced (VPCSC-enabled projects or projects listed in `enforcedProjects`), This managed organization policy constraint lets you specify which fully qualified domain names (FQDNs) are permitted when adding a data store.   
**[Override the organization policy for Custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores)** |  This managed organization policy constraint controls whether Custom Model Context Protocol (MCP) data sources can be used.  
  
Before you can create a Custom MCP data store, you must turn off the `Disable custom MCP server connector for Gemini Enterprise` managed constraint to enable Custom MCP.   
**VPC Service Controls** |  VPC Service Controls perimeters can protect your project. For more information, see [Use VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).   
  
Enforcement of this constraint also depends on whether your project is protected by a VPC Service Controls (VPCSC) perimeter. For more information, see VPCSC interaction and enforcement.   
  
### VPCSC interaction and enforcement

The enforcement behavior of this constraint depends on your project's VPCSC state and whether it's included in the organization policy constraint's `enforcedProjects` parameter, as summarized in the following table:

VPCSC state | Project included in `enforcedProjects` | `allowedEgressFqdns` enforcement | `allowedDataSources` enforcement  
---|---|---|---  
Enabled | Yes |  Provisioning is **blocked** if the required domains aren't listed.  |  Provisioning is **blocked** if the data source isn't listed.   
Enabled | No |  Provisioning is **blocked** if the required domains aren't listed.  |  Provisioning is **blocked** if the data source isn't listed.   
Not enabled | Yes |  Provisioning is **blocked** if the required domains aren't listed.  |  Provisioning is **blocked** if the data source isn't listed.   
Not enabled | No |  Provisioning is **allowed** even if domains aren't listed.  |  Provisioning is **allowed** even if data source isn't listed.   
  
## Example scenarios

To understand how these policies interact, consider the following examples.

### Allow Google Drive with VPCSC protection

You want to let users create a Google Drive data store.

Setup  
---  
The project is protected by a VPC Service Controls perimeter, and the VPCSC state is **Enabled**.  
Requirement  
To create the data store, you must add `google_drive` to the **Restrict allowed data sources for data connectors** policy.  
Why  
The system allows the connection and automatically permits the well-known FQDNs for Google Drive. You don't need to update the **Restrict egress domains for data connectors** policy.  
  
### Allowing a Custom MCP Server with VPCSC protection

You want to allow users to create a Custom MCP data store that connects to `api.cymbal.com`.

Setup  
---  
The project is protected by a VPC Service Controls perimeter (VPCSC state: **Enabled**).  
Requirement  
To create the data store and allow it to connect to `api.cymbal.com`, you must: 

  1. Turn off the **Disable custom MCP server connector for Gemini Enterprise** managed constraint.
  2. Add `custom_mcp` to the **Restrict allowed data sources for data connectors** policy.
  3. Add `api.cymbal.com` to the **Restrict egress domains for data connectors** policy.

  
Why  
When VPC Service Controls is enabled, policies are enforced automatically. Custom MCP requires that you explicitly allow FQDNs.  
  
### Third-party data source (Jira) without VPCSC protection

An organization wants to allow users to create a data store for a third-party data source, Jira, in a project that is not subject to enforcement.

Setup  
---  
The project is not protected by a VPC Service Controls perimeter and is not listed in `enforcedProjects`.  
Requirement  
No updates are required for the organization policies.  
Why  
Because standard enforcement is disabled, you don't need to explicitly allow the data source or its FQDNs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
