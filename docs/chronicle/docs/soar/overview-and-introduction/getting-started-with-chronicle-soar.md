---
url: https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/getting-started-with-chronicle-soar/
title: Get started with Google Security Operations SOAR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:00:57.109519+00:00
---

# Get started with Google Security Operations SOAR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/getting-started-with-chronicle-soar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with Google Security Operations SOAR 

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

To begin working in the Google SecOps SOAR platform, you must first understand the core concepts, which form the foundation of our documentation. 

## Connectors

_Connectors_ are the data ingestion points for **alerts** into Google SecOps SOAR. Their primary goal is to translate raw security data from third-party tools into normalized Google SecOps SOAR data. The connector gets alerts (or equivalent data) from third party tools, which is then forwarded to the Data Processing layer. 

**Note:** Google SecOps SOAR provides out-of-the-box connectors for popular security systems and includes a Python SDK for developing new custom connectors.

## Cases, alerts, and events 

  * **Case** : The top-level container, composed of one or more alerts ingested from various sources using the connectors.
  * **Alert** : A security notification containing one or more security events.
  * **Entities** : After ingestion, the platform analyzes these events, and their indicators (IOCs, destinations, artifacts) are extracted and translated into dynamic objects called entities.



_Entities_ are dynamic objects that represent extracted points of interest (Indicators of Compromise [IoC], user accounts, IP addresses) from an alert.

Entities are key because they enable:

  * Automatic history tracking.
  * Grouping of related alerts without manual intervention.
  * Hunting for malicious activity based on relationships.



### Entity creation (mapping and modeling)

In order to visually illustrate the entities and their connection in the platform, there is a configuration process of the ontology that involves mapping and modeling. During this process, you select the visual representation of alerts and the entities that should be extracted from it. 

Google SecOps SOAR provides basic ontology rules for most popular SIEM products out-of-the-box. For details, see [Ontology overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview). 

## Create entities in Google SecOps SOAR

The process of mapping and modeling defines how entities are created and visually connected within a case (ontology). This process occurs once when a new alert type is first ingested: 

  * It defines the visual representation of alerts and which entities should be extracted.
  * It sets entity properties, such as whether an entity is internal or external (based on configuration) or malicious (based on playbook results).



Google SecOps SOAR provides basic ontology rules out-of-the-box for most popular SIEM products.

For details about mapping and modeling, see [Create entities (mapping and modeling)](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling).

Using _mapping and modeling_ , you can define the properties of an entity, such as whether it's internal or external, or if it's considered _malicious_. An entity's _internal_ or _external_ status is determined by the platform's settings. Its malicious status is decided by the product running within the playbook. The purpose of mapping and modeling is to specify key details like the data's _source_ , _timestamp_ , and _type_. 

The mapping and modeling occurs once when data is first ingested. After that, the system applies the relevant rules to every new, incoming case. 

## Playbooks

A _Playbook_ is an automation process that can be triggered by a predefined condition. For example, you can trigger a playbook for each alert that contains the product name "Mail": When triggered, the playbook attaches to each alert ingested into Google SecOps SOAR from this product. 

It also executes a series of actions based on a defined tree of conditions (flows):

  * Actions are configured to run manually or automatically on the scope of the alert's entities.
  * Actions run in a defined order until a final resolution is reached for the triggering alert.



For example, you can configure the **VirusTotal - Scan URL** action to run automatically only on a specific entity type, such as URL entities.

## Environments

_Environments_ are logical containers used to achieve data segregation.

  * Administrators can define different environments and assign platform users to one or more of them.
  * Users can only see cases and related information from the environments to which they are assigned.
  * Some user roles have access to **all environments** , granting them full access to all current and future data within the platform.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
