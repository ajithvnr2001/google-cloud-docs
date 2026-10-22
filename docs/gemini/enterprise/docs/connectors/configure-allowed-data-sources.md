---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources/
title: Configure allowed data sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:16.615212+00:00
---

# Configure allowed data sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure allowed data sources Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.

The `discoveryengine.managed.allowedDataSources` managed organization policy constraint, also known as **Restrict allowed data sources for data connectors** , lets you control which external data sources (such as Jira, Box, or Confluence) are permitted when adding a data store in Gemini Enterprise.

## Before you begin

  * Ensure you have the **Organization Policy Administrator** role (`roles/orgpolicy.policyAdmin`).

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization.
  * Understand the policy enforcement dependencies and interactions. See [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview).




## Configure the constraint

To configure the allowed data sources, follow these steps:

  1. In the Google Cloud console, go to the **Organization Policies** page.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the project selector, choose the organization or project where you want to change policy enforcement.

  3. In the **Filter** field, enter `discoveryengine.managed.allowedDataSources` or `Restrict allowed data sources for data connectors`.

  4. Click the policy name to open its details.

  5. Click **Manage Policy**.

  6. Select **Override parent's policy**.

  7. Set **Enforcement** to **On**.

  8. Edit the `allowedDataSources` parameter:

     1. Click edit next to `allowedDataSources`.
     2. Set **Value Type** to **User-defined**.
     3. Add values, such as `jira`, `box`, or `custom_mcp`. For a complete list, see Supported Data Sources.
  9. **Optional** : To enforce this policy on specific projects not in VPCSC, update the `enforcedProjects` parameter and add the project names in the format `projects/<project_name>/`.

  10. Click **Set Policy**.




### Supported data sources

For the canonical list of supported `dataSource` values that you can add to the `allowedDataSources` parameter, see the tables in [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source#sources-by-launch-stage). Use the values from the **Value for`allowedDataSources`** column exactly as they appear.

## Verify the policy change

Verify the policy by attempting to create a data store. If the configuration is correct, you can create the data store without an `Operation denied by org policy` error related to `discoveryengine.managed.allowedDataSources`.

## What's next

  * To connect your data sources, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).

  * To create custom organization policies with fine-grained rules for your data connectors or data stores, see [Manage resources with custom organization policies](https://docs.cloud.google.com/gemini/enterprise/docs/org-policy-custom-constraints).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
