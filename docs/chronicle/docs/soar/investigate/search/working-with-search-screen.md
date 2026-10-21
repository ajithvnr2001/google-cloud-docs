---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen/
title: Search cases and entities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:48:58.728464+00:00
---

# Search cases and entities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Search cases and entities

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The **SOAR Search** function helps you quickly locate specific cases or entities in Google Security Operations. Google SecOps maintains detailed records of all cases and entities across your environment, enabling quick access to relevant investigation data.  
  
It supports both free-text and field-based searches across all data indexed within the past year, including case metadata, alerts, events, ports, and case timelines. You can search for either cases or entities.  
  
You can also search for cases using the SIEM search functionality. For more information, see [Search cases and case history](https://docs.cloud.google.com/chronicle/docs/investigation/search-and-search-case-history). 

## Explore the SOAR Search options

You can search for either cases or entities from the **SOAR Search** interface, using filters to refine results and take action on individual or multiple cases.

### Search cases

By default, the menu next to the main search bar is set to search for cases. Each result includes details, such as associated alerts, entities, insights, and case wall activity.

To search cases, follow these steps:

  1. Go to **Investigation > SOAR Search**.
  2. Enter your search criteria: 
     * **Free-text search** : In the main search bar, enter keywords or phrases related to the case. 
     * **Field-based search** : Use the available field filters to refine your search by specific criteria, such as: 
       * **CaseIds**
       * **TicketIds**
       * **Ports**
       * **AlertName**
  3. Select the appropriate timeframe using the date picker next to the search bar.
  4. Click a case to view more details, generate reports, or perform actions.

**Note:** Simulated case IDs aren't displayed by default. 

####  Examples of case searches 

  * Query by **caseids:180,181** to return specific case data. Click an ID to reach the **Case Details** screen. 
  * Query by **Ports:663,770** : to return all alerts that include these ports.  

  * Query by **Entity:10.210.1.13** to return all cases that have this IP address `10.210.1.13` as an entity.  

  * Query by **AlertName:IRC Connections** to return all cases with a matching alert name.  




## Search entities

Each entity in the search results includes the entity type, risk level, location, environment, and case count. An entity may be associated with multiple cases.

To search entities, follow these steps:

  1. Go to **Investigation > SOAR Search**.
  2. In the menu next to the search bar, select **Entities**. 
  3. Enter your search criteria: 
     * **Free-text search** : in the main search bar, enter keywords or phrases related to the entity. 
     * **Field-based search** : use the available field filters to refine your search by specific criteria, such as **Contains** or **Equals**
  4. Click an entity in the results to view context, related cases, and the entity log.



#### Examples of searching by entities

  * When you search by **Entities** , you can use free-text search. For example, a free-text search for **Chronicle** returns all entities containing that word. The search results show key details about each entity, including: Risk, Location, Environment, and case count.
  * Click the individual entity to go to the **Entity Details** page for more information. 



## Use filters to refine search results

Filters let you narrow your search results by selecting specific attributes.

To use filters, Click **Apply** to update your results or **Clear** to reset the filters to their default values.

### Search for cases filters

When searching for cases, you can filter by:

  * **Status** : Select the **Open** and **Closed** options as required. This selection returns open, closed, or both types of cases. 
  * **Environment** : Filters by specific environments. 
  * **Tags** : Filters by tags assigned to cases. 
  * **Assigned Users** : Select the required system users to whom the cases are assigned. 
  * **Category Outcomes** : Filters by the outcomes assigned to cases. 
  * **Ports** : Filters by source and destination ports involved in cases. 
  * **Products** : Filters by the integrated products. 
  * **Case Source** : Filters by the source of the cases. 
  * **Case Stage** : Filters by case stages according to SOC methodology. 
  * **Alert Types** : Filters by alert types associated with the cases. 
  * **Priorities** : Filters by required priorities assigned to the cases. 
  * **Importance** : Filters to show cases marked as important (`True`) or not (`False`). 
  * **Is Incident** : Filters to show cases marked as incidents (`True`) or not (`False`). 



### Search for entities filters

If searching for entities, you can filter results based on the following criteria:

  * **Networks** : Filters by the required organizational networks of the entities. 
  * **Environments** : Filters by the required environments related to the entities. 
  * **Type** : Filters by the type of entity. 
  * **Is Suspicious** : Filters to show cases flagged as suspicious (`True`) or not (`False`). 
  * **Is Internal** : Filters to show internal or external entities (`True`) or not (`False`). 
  * **Is Enriched** : Filters to show entities enriched by system (`True`) or not (`False`). 



## Perform actions on cases

You can perform single or bulk actions on selected cases directly from the search results.

  1. In the search results, select the checkbox next to one or more cases.
  2. Click  lists  **Menu** and choose an action: 
     * **Export to CSV** : downloads selected case data as a CSV file. 
     * **Close case** : closes selected open cases. 
     * **Reopen case** : reopens selected closed cases. 
     * **Change priority** : modifies the priority of selected open cases. 
     * **Assign case** : reassigns selected open cases to another user. 
     * **Add tag** : adds tags to selected open cases. 
     * **Merge cases** : merges selected cases into a parent case. 
     * **Change stage** : updates the current stage of selected cases. 



  


**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
