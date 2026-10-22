---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/working-with-entity-delimiters/
title: Configure entity delimiters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:10.155804+00:00
---

# Configure entity delimiters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/working-with-entity-delimiters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure entity delimiters

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

_Entity delimiters_ let you decide for each entity type and data source how to map the incoming entity. You can disable delimiters for incoming entities, map a specific delimiter (up to 64 characters), or use a regular expression instead.

For example, if you have several files separated by commas in a single entity, you can set the delimiter to a comma so the system treats each file as a separate entity.

You can use entity delimiters in two places:

  * On the **Event Configuration > Mapping** page. 
  * On the **Playbook action > Siemplify > Create Entity** page. 



## Event configuration & mapping

The Event Configuration feature lets you assign visual families to events, providing a graphic visualization of their relationships with other actions. This process ensures events are correctly categorized and contain accurate and complete information. For details, see [configure mapping and assign visual families](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/configure-mapping-and-assign-visual-families).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
