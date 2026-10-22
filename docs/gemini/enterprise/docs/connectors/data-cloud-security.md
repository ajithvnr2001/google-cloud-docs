---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/
title: Secure Data Cloud connectors \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:40.864134+00:00
---

# Secure Data Cloud connectors  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Secure Data Cloud connectors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the security and compliance controls supported by [Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud) in Gemini Enterprise and explains how to configure organization policies when your project is protected by a VPC Service Controls perimeter.

## Supported security and compliance controls

Data Cloud connectors support the following enterprise security and compliance controls in Gemini Enterprise:

  * **Data residency (DRZ)** : When you use federated query mode, your customer data remains where it's already stored and isn't moved. The connector queries your data in place and returns the results to the agent in the location of your Gemini Enterprise app. If write actions are enabled, the agent can also modify data in place within the underlying data source, subject to the user's Identity and Access Management permissions. Gemini Enterprise supports data residency in the `us` and `eu` multi-regions. For more information, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
  * **Customer-managed encryption keys (CMEK)** : When you use federated query mode, your underlying data remains in the connected data source, where you can configure CMEK directly in that service. In Gemini Enterprise, you can use encryption keys managed in Cloud Key Management Service to protect data at rest, including query results returned to the agent and stored in conversations, connector configurations, and end-user credentials. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).
  * **VPC Service Controls** : You can protect your Gemini Enterprise apps and Data Cloud connectors within a VPC Service Controls service perimeter to help mitigate data exfiltration risks. When VPC Service Controls is enabled, you must also allow the Data Cloud connector IDs in your organization policies as described in Allow Data Cloud connectors in organization policies. For general perimeter setup instructions, see [Use VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).



## Allow Data Cloud connectors in organization policies

If your project is protected by a VPC Service Controls perimeter, or is explicitly included in the `enforcedProjects` parameter of an organization policy, Gemini Enterprise enforces the Google-managed `constraints/discoveryengine.managed.allowedDataSources` organization policy constraint. This constraint blocks data store creation unless the connector's internal identifier is explicitly listed in the policy's `allowedDataSources` parameter.

To allow Data Cloud connectors, add the corresponding connector identifier to the `allowedDataSources` parameter:

  * `bigquery_mcp`: Allows the BigQuery federated data connector.
  * `spanner`: Allows the Spanner federated data connector.
  * `cloudsql`: Allows the Cloud SQL federated data connector.
  * `alloydb`: Allows the AlloyDB for PostgreSQL federated data connector.

**Note:** First-party API connectors communicate directly over internal Google APIs, so their endpoints are automatically permitted when the connector is allowed in `allowedDataSources`. You don't need to add domain names to the `discoveryengine.managed.allowedEgressFqdns` constraint.

For more information about managed constraints and step-by-step instructions for configuring organization policies in the Google Cloud console, see the following resources:

  * [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview)
  * [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources)
  * [Configure allowed egress FQDNs](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
