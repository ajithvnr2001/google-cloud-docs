---
url: https://docs.cloud.google.com/chronicle/docs/secops/onboard-chronicle-secops-soar/
title: Onboard Google SecOps platform (SOAR side only) \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:10:38.058303+00:00
---

# Onboard Google SecOps platform (SOAR side only)  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/onboard-chronicle-secops-soar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Onboard Google SecOps platform (SOAR side only)

Supported in:

Google SecOps 

## Before you begin

Google strongly recommends taking the training in the [Google SecOps learning path](https://www.cloudskillsboost.google/journeys/187) first. 

## Set up user groups

You need to create or select a predefined SOC role and a permission group and then map them with the IdP groups received from the SIEM setup. For detailed instructions for each of these tasks, see the following documents: 

  * [Assign roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles)
  * [Assign permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups)
  * [Map users with IdP groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform)



## Set up data ingestion points using connectors or webhooks

Set up connectors or webhooks to ingest alerts into the platform to analyze them. This can also be achieved by downloading an entire use case. For detailed instructions for each of these tasks, see the following documents:  


  * [ Ingest your data using connectors](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors)
  * [ Ingest your data using webhooks](https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook)
  * [ Run a use case from the Content Hub](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases)
  * [Create your own connector](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-connector) (for advanced users)



## Map and model incoming data

You can control how incoming products, events, and entities are mapped and modeled to make sure the right information is captured. You can define this ontology configuration for yourself or choose the default mapping and modeling configuration. For detailed instructions for each of these tasks, see the following documents: 

  * [Ontology overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview)
  * [Create visual families](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/visual-families)
  * [Create entities](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling)



## Create playbooks 

Google Security Operations lets you respond to threats using a sequential set of manual and automated steps called _playbooks_. For more information about playbooks, refer to the following documents: 

  * [ What's on the playbooks screen](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen)
  * [ Create your first automation (playbook)](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen)
  * [Run a use case from the Content Hub](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases)
  * [ Work with Playbook Simulator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-simulator)



## Analyze cases and alerts

Use simulated cases and test alerts to test your configurations and playbooks before going live with them. After alerts are ingested and playbooks have finished running, you can look at the cases and alerts to see what needs to be done next, including triage or remediation steps. For detailed instructions for each of these tasks, see the following documents:   


  * [Cases overview](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview)
  * [Simulate a case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/simulate-cases)
  * [Perform manual actions](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action)
  * [Explore alerts](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-overview-tab)
  * [Entity Explorer page](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/navigating-the-entity-explorer-screen)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
