---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation/
title: Case manipulation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:27.152900+00:00
---

# Case manipulation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Case manipulation 

This section focuses on SDK functions that help manipulate a case's state and data. 

Name  |  Siemplify  |  SiemplifyAction  |  Description   
---|---|---|---  
close_case  |  N/A  |  [close_case](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#close-case-siemplify-action) |  Closes the current case with the selected close reason and given comment   
add_comment  |  [add_comment](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#add-comment-siemplify) |  [add_comment](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#add-comment-siemplify-action) |  Adds a comment to the current case's case wall   
close_alert  |  N/A  |  [close_alert](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#close-alert-siemplify-action) |  Closes the current alert with the selected close reason and given comment   
raise_incident  |  [raise_incident](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#raise-incident-siemplify) |  [raise_incident](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#raise-incident-siemplify-action) |  Changes the current case into an incident   
assign_case  |  [assign_case](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#assign-case-siemplify) |  [assign_case](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#assign-case-siemplify-action) |  Assigns the current case to the selected analyst or group   
add_entity_to_case  |  [add_entity_to_case](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#add-entity-to-case-siemplify) |  [add_entity_to_case](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#add-entity-to-case-siemplify-action) |  Creates a new entity in the case   
add_attachment  |  [add_attachment](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#add-attachment-siemplify-action) |  [add_attachment](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#add-attachment-siemplify-action) |  Adds attachment to the case.   
  
##  Case metadata 

This section focuses on SDK functions that manipulate case index and help maintain the system. Functions in this section are used to produce better search mechanism, KPIs and filters. 

###  Methods 

Name  |  Siemplify  |  SiemplifyAction  |  Description   
---|---|---|---  
add_tag  |  N/A  |  [add_tag](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#add-tag-siemplify-action) |  Adds a new tag to the current case   
change_case_stage  |  N/A  |  [change_case_stage](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#change-case-stage-siemplify-action) |  Sets the current case's stage to a specific stage   
change_case_priority  |  [change_case_priority](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#change-case-priority-siemplify) |  [change_case_priority](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#change-case-priority-siemplify-action) |  Sets the current case's priority to a specific value   
mark_case_as_important  |  [mark_case_as_important](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#important-case-siemplify) |  [mark_case_as_important](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#important-case-siemplify-action}) |  Marks the current case with the 'importance triangle' sign   
  
##  Data retrieval 

Name  |  Siemplify  |  SiemplifyAction  |  Description   
---|---|---|---  
get_case_comments  |  [get_case_comments](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module#get-case-comms-siemplify) |  [get_case_comments](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#get-case-comms-siemplify-action) |  Retrieve comments on the case   
get_alerts_ticket_ids_from_cases_closed_since_timestamp  |  N/A  |  [get_alerts_ticket_ids_from_cases_closed_since_timestamp](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#get-alert-tids-siemplify-action) |    
  
get_similar_cases  |  N/A  |  [get_similar_cases](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module#get-similar-cases-siemplify-action) |  Retrieve similar cases in the system   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
