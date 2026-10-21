---
url: https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/onboard-chronicle-soar/
title: Onboard Google SecOps SOAR platform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:59:38.961813+00:00
---

# Onboard Google SecOps SOAR platform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/onboard-chronicle-soar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Onboard Google SecOps SOAR platform

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

This document provides a comprehensive, step-by-step guide to onboarding and configuring the Google Security Operations SOAR platform. The process is structured to establish user access, secure data ingestion, normalize data, build automation, and prepare for live operations.

## Before you begin

We strongly recommend taking the training in our [Google SIEM and SOAR learning path](https://www.cloudskillsboost.google/journeys/187) first. 

## Set up user access and roles

To get started, you must define a **role** and **permission groups**. If you're an MSSP or you manage a multi-tenant environment, you also need to set up an **environment** and associate it with new users. If required, you can also provision users to sign in using a SAML provider. For detailed instructions for each of these tasks, see the following documents: 

  * [ Manage roles and workloads](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles)
  * [ Manage permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups)
  * [ Add a new environment](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments) (relevant mainly for MSSPs)
  * [Add a new user to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform)
  * [ Authenticate users using SSO (SOAR only)](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication)



## Set up data ingestion points using connectors or webhooks

Configure connectors or webhooks to ingest alerts for analysis. This can also be achieved by downloading an entire Use Case. For detailed instructions for each of these tasks, see the following documents: 

  * [ Ingest data using SOAR connectors](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors)
  * [ Set up a webhook](https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook)
  * [ Run use cases](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases)
  * [ Develop your first email connector](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-connector) (for advanced users)



## Map and model incoming data (ontology)

Control how incoming products, events, and entities are mapped and modeled. This ensures the correct information is captured and visualized. You can define this ontology configuration for yourself or choose the default mapping and modeling configuration. For detailed instructions for each of these tasks, see the following documents: 

  * [ Ontology overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview)
  * [ Map security event relationships with visual families](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/visual-families)
  * [ Create entities (mapping and modeling)](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling)



## Create and test automation (playbooks) 

Build automated responses using playbooks—sequential sets of manual and automated steps that respond to threats. For more information about playbooks, see the following documents: 

  * [Explore the playbooks page](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen)
  * [ Create your first automation](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation)
  * [Run use cases from the Content Hub](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases)
  * [ Work with the Playbook Simulator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-simulator)



## Analyze cases and alerts

Use simulated cases and test alerts to verify configurations. Once live, analyze cases and alerts to determine triage or remediation steps. For detailed instructions for each of these tasks, see the following documents: 

  * [ Cases overview](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview)
  * [ Take actions on a case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/simulate-cases)
  * [ Perform manual actions](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action)
  * [ View alert overview tab](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-overview-tab)
  * [ Navigate the Entity Explorer page](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/navigating-the-entity-explorer-screen)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
