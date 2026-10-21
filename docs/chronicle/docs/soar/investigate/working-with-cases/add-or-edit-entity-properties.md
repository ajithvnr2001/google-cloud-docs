---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-or-edit-entity-properties/
title: Manage entity properties \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:27:24.296728+00:00
---

# Manage entity properties  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-or-edit-entity-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage entity properties

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how you can add or edit entity enrichment properties directly from investigation pages as part of your case investigation in Google Security Operations to work more efficiently during case analysis. You can add up to 100 entity properties to a single entity. 

**Note:** To add or edit entity properties, ensure the appropriate permissions are granted in the corresponding module in **Settings**. For more information, see [Working with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups). 

## Entity properties

Entities are key components in Google SecOps cases, representing objects involved in security events. Understanding their properties is crucial for effective investigation.

Entities and artifacts differ in several ways:

  * **Icon:** Entities have black icons with a blue stroke, while artifacts have green icons.
  * **Occurrence:** The same entity typically appears at most twice in the same event (as a source and a destination). There is no limit on the number of artifacts of the same type in an alert.
  * **Scope:** Entities can be internal (inside the organization's network) or external. Artifacts are always internal.



For definitions of standard entity properties, see [SOARInvolvedEntities](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard#soar-involved-entities).

You can manage properties by adding new ones, editing existing values, or adding entities to alerts. For more information, see:

  * Add an entity property
  * Edit an entity property
  * Add new or existing entities



## Add or edit entity properties across pages

Add or edit an entity enrichment property on the following pages:

  * **Investigation** : In the case view, click **Explore** to open the **Investigation** page. 
  * **Entity Explorer** : In the case view, click the **Entity Highlights** widget and select the relevant entity. 
  * **Cases (Entities Highlights)** : In the case view, click an entity in the **Entity Highlights** widget and then click **View more** to open a side drawer with entity properties. 
  * **Cases (Entities Graph)** : In the case view, click the **Entities Graph** widget and then click **Entity**. A side drawer opens with entity properties. 



### Add an entity property

As part of the investigation, include other entity keys to enrich your case investigation. Identify the kind of malware being used to better understand the threat. This example shows how to create a new entity property called `Malware_family`. 

To add an entity property, follow these steps:

  1. Go to the **Cases** queue.
  2. Select the **Virus Found or Security Risk Found** case, and click **Explore** to open the **Investigation** page.
  3. Click add **Add**.
  4. Enter `Malware_family` as the **Key** and `Trojan.Generic` as the **Value**.
  5. Click **Save** to add the new entity property.



The new enrichment provides an additional layer of understanding during your case investigation.

### Edit an entity property

This example follows a use case where a file is marked as suspicious with low confidence in a case related to a potential malware threat. After running a TI enrichment block and investigation, you're confident that the file is malicious and want to update the `confidence_level` from **Low** to **High**. 

To edit an entity property, follow these steps:

  1. Go to the **Cases** page.
  2. Go to the **Virus Found or security risk found** case, and click **Explore** to open the **Investigation** page.
  3. Click tag **File Hash Entity** on the **Investigation** page.
  4. Hold the pointer over the **confidence_level** value in the side drawer.
  5. Click more_vert **More** and select **View or edit property**.
  6. In the **View or Edit Entity Property** dialog, change the value of **Confidence_level** from **Low** to **High** to highlight the potential risk of the hash entity. You can also select a display format to control how the data appears in the side drawer. **Note:** The display format affects only how the value is shown in the UI. It doesn't change the underlying data. 
  7. Click **Save**.



The confidence level of the entity is updated and reflected in the side drawer.

**Note:** You can't change entity properties, such as `isAttacker`, `isVulnerable`, and `isPivot` to **false** once it's set to **true**. 

## Add new or existing entities

To add new or existing entities, follow these steps:

  1. Click more_vert **Alert Options** and select **Add Entity**.
  2. In the **Add entities to alert** dialog, select an entity from either **Add existing entities** or **Add new entity**.
  3. Enter an identifier and click add **Add** > **Apply**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
