---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview/
title: Ontology overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:22.308205+00:00
---

# Ontology overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ontology overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The Google Security Operations ontology uses a formal specification that provides a shareable and reusable knowledgeable representation of alerts and events. The ontology lets Google SecOps build entities from events and define relationships between them. This process lets you see the full picture and explore potential threats on the [Explore](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/explore-entities-and-alerts-investigation) page. Once entities have been defined using the ontology, you can run actions on them based on their role in the attack or event. 

**Note:** Most integrations include a pre-configured ontology that provides a ready-made structure you can adapt or extend to meet your needs, instead of creating the entire structure manually. 

## View the Ontology status

Go to **Settings > Ontology > Ontology Status** to see the following information: 

  * **Number of product types** : The number of products that Google SecOps captures from your environment. This number changes as more products are added to your environments.
  * **Number of event types** : The number of events that Google SecOps captures.
  * **Number of events assigned to default families** : The number of events that Google SecOps has automatically assigned. You can reassign an event (at any time) by locating the default value in the **Family Name** column and click  settings  **Configure**.



You can export selected ontology status rows as a ZIP file containing a JSON file. You can also import ontology status rows. Be sure to import a ZIP file that contains a JSON file with the ontology details.

## Set up model families

After you've established an initial data connection, you'll need to do the following:

  1. Complete the following procedures to ensure that the data is ingested into the Google SecOps data model.
  2. Map and model new events and alerts according to your requirements.



To set up a model family, follow these high-level steps:

  1. Define the family: click **Settings > Ontology > Visual Families**.
  2. Assign the family to the Event (or Product/Source) from either the [Alerts events](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/deciding-what-events-to-configure) tab or the [Ontology status](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview#ontology-status) page, click **Event Configuration > Visualization**.



## Map data fields

To map data fields, follow these high-level steps:

  1. On the **Case Management** or **Explore** page, correct any missing or incorrect field information.
  2. Check if this can be solved by attaching a new Visual Family; otherwise, edit and configure the rules that make up both the family and the general system fields on the [Event Configuration > Mapping page.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/configure-mapping-and-assign-visual-families)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
