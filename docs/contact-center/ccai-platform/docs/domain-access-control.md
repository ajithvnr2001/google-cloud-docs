---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/domain-access-control/
title: Domain-based access control \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:36.156829+00:00
---

# Domain-based access control  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/domain-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Domain-based access control Stay organized with collections  Save and categorize content based on your preferences. 

Domain-based access control ensures security while also allowing you to define and control which domains can display the Contact Center AI Platform (CCAI Platform) agent adapter.

## Specify a domain

The format for specifying a domain can be any valid domain name, and can include a wildcard (*) to match an arbitrary number of subdomains. The wildcard must be placed at the beginning of the domain, and it will match any subdomains. Additionally, you have the option to specify a protocol and a port using the syntax `<protocol>://<domain>:<port>`.

The port can be a wildcard, but the protocol cannot be a wildcard. If a protocol is specified, it will match only that protocol and all other protocols won't be able to display the adapter.

For example:

`https://some.example.domain.com` won't match `http://some.example.domain.com` or `mail://some.example.domain.com`.

## Add domains in developer settings

**Note:** Once added it can take up to a minute for changes to the list of domains to take effect.

  1. In the CCAI Platform portal, go to **Developer Settings > Agent Adapter-Domain Based Access Control**.

  2. Enter each domain on a new line. Format is `*.domain`. If no domains are specified, access is granted to all domains.

For example, `*.mycompany.com`.




## CRM specific domains

Use the following domain naming conventions when entering your CRM domain. If you don't include all of these domains for a specific CRM, the Agent Adapter will immediately break.

  * **Salesforce:** `*.visualforce.com` `*.force.com` `*.salesforce.com`

  * **Zendesk:** `*.zdusercontent.com` `*.zendesk.com`

  * **Microsoft Dynamics:** `*.crm.dynamics.com`

  * **Kustomer:** `*.kustomerapp.com`

  * **HubSpot:** `*.hubspot`




## Reload frame on the agent adapter

If the agent adapter is not visible to agents after making administrator configuration changes, the agent must **right click** over the agent adapter and then select the **Reload Frame** operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
