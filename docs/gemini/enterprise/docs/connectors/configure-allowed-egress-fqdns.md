---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns/
title: Configure allowed egress fully qualified domain names for data stores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:27.034439+00:00
---

# Configure allowed egress fully qualified domain names for data stores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure allowed egress fully qualified domain names for data stores Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.

The **Restrict egress domains for data connectors** managed organization policy constraint lets you specify which fully qualified domain names (FQDNs) are permitted when adding a data store in Gemini Enterprise. The domains you need to add typically include the domain names extracted from the instance URL, authorization URL, and token URL provided when provisioning a data store. For example, if the authorization URL is `https://api.cymbal.com/oauth/authorize`, you only need to allowlist `api.cymbal.com`.

## Before you begin

  * Ensure you have the **Organization Policy Administrator** role (`roles/orgpolicy.policyAdmin`).

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization.
  * Understand the policy enforcement dependencies and interactions. See [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview).




## Configure the constraint

To configure the allowed egress FQDNs, follow these steps:

  1. In the Google Cloud console, go to the **Organization Policies** page.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the project selector, choose the organization or project where you want to change policy enforcement.

  3. In the **Filter** field, enter `discoveryengine.managed.allowedEgressFqdns` or `Restrict egress domains for data connectors`.

  4. To open the policy details page, click the policy name.

  5. Click **Manage Policy**.

  6. Select **Override parent's policy**.

  7. Set **Enforcement** to **On**.

  8. Next to the `allowedEgressFqdns` parameter, click **Edit**.

  9. Change the **Value Type** to **User-defined**.

  10. Click **Add item** , and then enter each required fully qualified domain name (FQDN). Add only the domain (such as `api.cymbal.com`), not the full URL. Repeat this step to add all required domains based on your data store type:

**Note:** If your endpoints are hosted on different domains, add every domain to the list of permitted domains. Omitting required domains blocks outbound requests during OAuth sign-in, token exchange, and data syncs, causing connection and authentication checks to fail.Data store type | Required domains  
---|---  
**Custom MCP data stores** |  Add the domain of the **MCP server URL** , **authorization URL** , and **token URL**.   
For example, for an MCP server URL of `https://api.cymbal.com/mcp` with authorization and token URLs on `auth.cymbal.com`, add both `api.cymbal.com` and `auth.cymbal.com`.   
**All other data stores** |  Add the domain of the **instance URL** , **authorization URL** , and **token URL**.   
For example, if your authorization URL is `https://auth.cymbal.com/oauth/authorize`, add `auth.cymbal.com`.   
  11. Optional. To enforce the managed constraint on projects where VPCSC isn't enabled, click **Edit** next to the `enforcedProjects` parameter and add the project numbers.

  12. Click **Set Policy**.




## Verify the policy change

After you apply the new configuration, verify that the policy status is updated.

Verify the policy by attempting to create a data store. If the configuration is correct, you can create the data store without an `Operation denied by org policy` error related to `discoveryengine.managed.allowedEgressFqdns`.

## What's next

  * To connect your data sources, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
