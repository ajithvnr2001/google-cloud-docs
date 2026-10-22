---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/requirements-for-publishing-integration/
title: Publish custom integrations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:15.461077+00:00
---

# Publish custom integrations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/requirements-for-publishing-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish custom integrations

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the requirements for publishing integrations in Google Security Operations SOAR. It lists prerequisites, coding standards, action development guidelines, JSON formatting rules, entity enrichment best practices, and the process for submitting an integration to the Content Hub. Following these requirements helps ensure integrations are reliable, maintainable, and discoverable by other users. 

## Integration requirements

  * **Python 3.7** : Develop all integrations in Python 3.7. 
  * **Integration description** : Include a clear description of the product you're integrating with. 
  * **Icons**
    * **SVG icon** : This icon is applied to all instances of the integration in the platform. 
    * **PNG icon** : This image appears in the Google SecOps Marketplace. 
  * **Integration category** : Define a category to let other users filter your integration in the Google SecOps Marketplace. Select a category from the predefined list in the Google SecOps Marketplace. 
  * **Dependencies** : If your integration requires external libraries, list them in the integration settings. 
  * **Integration Parameters** : Include all parameters needed for a successful connection to the product, along with clear descriptions. 
  * **Manager** : To avoid code duplication, create a manager—a Python file that can be referenced by other scripts in the integration. 
  * **Ping action** : Include a **Ping** action to verify connectivity. The result should return `true` if the connection is successful. This action should be disabled by default; it's not intended for playbook use. 
  * **Linux** : The integration should support CentOS 7 or later. 



## Action requirements

  * **Action description** : Clearly describe what the action does. 
  * **Action structure** : Follow the default Integrated Development Environment (IDE) action template. 
  * **Action parameters** : Define all parameters that are relevant to the action, including descriptions. Match parameter types to the action's requirements. 
  * **Running action on a context of an alert** : Where applicable, design the action to run in the context of an alert. For example, scope the logic to specific entity types (for example, URLs) using `siemplify.target_entities`. For an example, see [Create custom actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action). 
  * **Logging** : Add logs for complex actions, and log all exceptions or errors with the correct severity level ([`info`](https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module#info-script-result), [`warn`](https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module#warn-script-result), [`error`](https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module#error-script-result), and [`exception`](https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module#exception-script-result)). 



## JSON requirements

  * **JSON Result** : For actions that return data, use [`add_result_json`](https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module#add-result-json-script-result) to return a JSON result. 
  * **Add a JSON Example** : Add an example JSON file that you can import into the **Expression Builder** for playbook creation. This recommendation lets JSON result values represent placeholders in a playbook.



## Enrich entities

When enriching entities with data from an integrated product, follow these best practices:

  * **Add an enrichment step** : Include relevant data from the product in the action output.
  * **Use a prefix** : Add a prefix (usually the product name) to enrichment field keys to prevent conflicts. 
    * **Example** : To enrich an entity with a user's first and last name, add `Zoom` as the prefix to the new fields. 
          
          entity_enrichment = {"first_name":"First Name", "last_name":"Last Name"}
          entity_enrichment = add_prefix_to_dict(entity_enrichment, "Zoom")

  * **Update the entity** : Use `entity.additional_properties.update()` to add the enriched data to the entity's properties.
  * **Update the alert** : Use `siemplify.update_entities(enriched_entities)` to add the updated entities to the alert. Click the entity to view the full details.



## Publish the integration

To make your integration available to all Google SecOps Marketplace users, contact [Customer Support](https://docs.cloud.google.com/chronicle/docs/getting-support) to submit it for review by the Marketplace team.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
