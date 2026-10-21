---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores/
title: Override the organization policy for Custom MCP data stores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:48:51.387639+00:00
---

# Override the organization policy for Custom MCP data stores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Override the organization policy for Custom MCP data stores Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.

By default, Gemini Enterprise blocks the creation of Model Context Protocol (MCP) data stores using a managed organization policy constraint. To enable the creation of Custom MCP data stores, an Organization Policy Administrator must override this restriction.

## Before you begin

  * Ensure you have the **Organization Policy Administrator** role (`roles/orgpolicy.policyAdmin`).

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization.
  * Understand the policy enforcement dependencies and interactions. For more information, see [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview).




## Example usage scenarios

To understand how these policies work together, consider an organization that wants to allow users to create a Custom MCP data store that connects to `api.cymbal.com` in a project named `cymbal-project`.

#### The project is VPCSC protected

Setup  
---  
`cymbal-project` is protected by a VPC Service Controls perimeter (VPCSC state: **Enabled**).  
Requirement  
To create the data store and allow it to connect to `api.cymbal.com`, the organization administrator must: 

  1. Turn off the **Disable custom MCP server connector for Gemini Enterprise** managed constraint to enable Custom MCP. 
  2. Add `custom_mcp` to the `allowedDataSources` parameter in the **Restrict allowed data sources for data connectors** policy. For more information, see [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 
  3. Add `api.cymbal.com` to the `allowedEgressFqdns` parameter in the **Restrict egress domains for data connectors** policy. For more information, see [Configure allowed egress FQDNs for data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns). 

  
Why  
Because VPCSC is enabled, policies are enforced automatically.  
  
#### Project not VPCSC protected, but enforced through the policy

Setup  
---  
`cymbal-project` is not in a VPC Service Controls perimeter (VPCSC state: **Not enabled**), but the administrator added it to the `enforcedProjects` parameter in both policies.  
Requirement  
To create the data store and allow it to connect to `api.cymbal.com`, the organization administrator must: 

  1. Turn off the **Disable custom MCP server connector for Gemini Enterprise** managed constraint to enable Custom MCP. 
  2. Add `custom_mcp` to the `allowedDataSources` parameter in the **Restrict allowed data sources for data connectors** policy. For more information, see [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources)
  3. Add `api.cymbal.com` to the `allowedEgressFqdns` parameter in the **Restrict egress domains for data connectors** policy. For more information, see [Configure allowed egress FQDNs for data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns). 

  
Why  
The project is opted-in to enforcement using `enforcedProjects`.  
  
#### The project is not VPCSC protected or enforced through the policy

Setup  
---  
`cymbal-project` is not in a VPC Service Controls perimeter (VPCSC state: **Not enabled**) and is not listed in the `enforcedProjects` parameter for either policy.  
Requirement  
To create the data store and allow it to connect to `api.cymbal.com`, the organization administrator must: 

  1. If the **Disable custom MCP server connector for Gemini Enterprise** managed constraint is enabled, turn it off to enable Custom MCP. 
  2. No updates are needed for the **Restrict allowed data sources for data connectors** policy.
  3. No updates are needed for the **Restrict egress domains for data connectors** policy.

  
Why  
The **Restrict egress domains for data connectors** and **Restrict allowed data sources for data connectors** policies are not enforced on this project.  
  
## Override the constraint

To create a Custom MCP server data store in your Google Cloud project, you must override the existing managed organization policy constraint. Follow these steps:

  1. In the Google Cloud console, go to the **Organization Policies** page.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the project selector, select the project for which you want to change enforcement.

**Important:** Select the specific project for which you want to change enforcement. Setting the policy at the organization level changes enforcement for all projects in the organization.
  3. In the **Filter** field, enter `Disable custom MCP server connector for Gemini Enterprise`.

  4. Click the policy name to navigate to the policy details page.

  5. Click **Manage Policy**.

![The Manage Policy button on the Organization Policies
page.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/custom-mcp-server/custom-mcp-server-manage-policy.png)

  6. Select the option to **Override parent's policy**.

  7. Add a new rule and set the enforcement toggle to **OFF**.

  8. Click **Set Policy**.




## Verify the policy change

After you apply the new configuration, verify that the policy status is updated to **Not enforced**.

The following image shows the Organization Policy Service details page with the policy set to **Not enforced** :

![The Manage Policy details page with the **Disable custom MCP server
connector for Gemini Enterprise** policy set to **Not
enforced**.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/custom-mcp-server/custom-mcp-server-not-enforced.png)

## What's next

  * Create a custom MCP server data store. For more information, see [Set up a custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
