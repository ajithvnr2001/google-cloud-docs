---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/custom-lists/
title: Custom lists \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:52.296116+00:00
---

# Custom lists  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/custom-lists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Custom lists 

**Note:** For Google SecOps customers who have migrated to Google Cloud, use [Data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables) instead. **Note:** Related Methods: [Siemplify.add_entities_to_custom_list](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#entities-cl-siemplify), [Siemplify.any_entity_in_custom_list](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#any-entity-cl-siemplify), [Siemplify.remove_entities_from_custom_list](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#remove-entities-cl-siemplify), [Siemplify.get_existing_custom_list_categories](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#get-cl-categories-siemplify), [Siemplify.is_existing_category](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#is-category-siemplify)

The custom list is a list of objects, that can be saved into DBs, as a shared resource, fetched and queried by each script execution instance.  
The custom list can be edited in the **Settings** page. This section deals with SDK functionalities for custom lists. 

####  Custom List item structure:  
This object is defined in [SiemplifyDataModel](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module)

Param Name  |  Param Type  |  Possible Values   
---|---|---  
identifier  |  string  |  Any identifier whatsoever. Usually this identifier represents a possible entity in future alerts   
category  |  string  |  Category from the Siemplify settings   
environment  |  string  |  Environment name from the Siemplify settings   
  
To create a _CustomList_ object, do the following: 
    
    
        from SiemplifyAction import SiemplifyAction
        from SiemplifyDataModel import CustomList
        custom_list = CustomList(identifier="203.0.113.1", category="AllowListed HOSTs", environment="")
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
