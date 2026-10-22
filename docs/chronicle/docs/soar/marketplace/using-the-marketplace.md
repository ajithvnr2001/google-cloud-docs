---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace/
title: Use the Content Hub for SOAR standalone \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:30.669405+00:00
---

# Use the Content Hub for SOAR standalone  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Content Hub for SOAR standalone 

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** If you're a Google SecOps unified customer, see [Content Hub overview](https://docs.cloud.google.com/chronicle/docs/secops/content_hub). 

The Content Hub acts as the customer's toolbox, holding a wide range of utilities and options to choose from, including the following:

**Integrations** : Integrations to third-party applications and custom integrations that you've built in the IDE. 

**Use Cases** : Prebuilt playbook workflows you can integrate into the platform and use to optimize your Google Security Operations installation. They include predefined use cases from Google SecOps and customer-uploaded use cases to test drive Google SecOps functionality or incorporate into your own use cases. 

**Power Ups** : Tools created by Google SecOps that enhance your ability to automate processes for playbooks.

## Content types

There are four types of content in the Content Hub:

  * **Google** : Content that has been developed, maintained & verified by Google SecOps. This category includes both new and updated content items.
  * **Partner** : Content that has been developed and maintained by the Partner. These may carry a **Verified** badge if they pass Google's automated quality and validation checks.
  * **Community** : Content that has been developed and maintained by Community users. These may carry a **Verified** badge if they pass Google's automated quality and validation checks.
  * **Custom** : Content that you created and which is only displayed on your own Content Hub. This content is private to your instance and is not verified by Google SecOps.



### Filter integrations

You can filter the integrations according to integration type or by status.

###  Configure integrations 

For more information on installing and configuring an integration, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations). For more information about configuring an integration on several instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances). For more information on integrations, see [Response integrations](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations).

If an integration update introduces issues, you can revert to the previously installed version. For more information, see [Roll back response integration version](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback).

### Ontology override

When you install or upgrade an integration, an on-screen dialog offers you the following two options:

  * **Override (replace mapping)** : This action completely replaces the existing ontology mapping rules. All existing mappings (source, product, event type) are overwritten by the corresponding rules defined in the new integration. This includes the deletion of any custom modifications you may have previously made.

  * **Retain (keep existing mapping)** : This action preserves the existing mapping in its entirety. Use this action if you've implemented significant custom changes to the ontology to meet specific instance requirements.




We recommend exporting the existing ontology mapping rules for each specific integration as a backup, before initiating an override. For more information about ontology, see [Ontology status](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/viewing-model-family-and-field-mapping).

## Use cases

Use cases provide an end-to-end solution that significantly shortens your time to value by providing predefined solutions to specific SOC challenges. They demonstrate how Google SecOps experts or community users approach common security problems.

Each use case contains relevant items, such as integrations and playbooks, to simulate an entire workflow from end-to-end. After you download one of these use cases, you can choose to simulate it in the **Cases** page. Optionally, you can configure the connector and edit the playbook of a predefined use case and run it on your organization's live data.

## Power Ups

_Power Ups_ are built-in actions provided by Google SecOps, designed to enhance your existing playbooks. These actions require no special configuration as they're inherently included within the Google SecOps platform. For specific technical details and usage examples of each available action, click **Read More** within the platform documentation.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
