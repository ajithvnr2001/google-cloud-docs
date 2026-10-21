---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dynamic-schema-with-user-attributes/
title: Using user attributes for dynamic schema and table name injection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:36.669069+00:00
---

# Using user attributes for dynamic schema and table name injection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dynamic-schema-with-user-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Using user attributes for dynamic schema and table name injection Stay organized with collections  Save and categorize content based on your preferences. 

Looker's [User Attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) feature can be used to dynamically insert schema and/or table names on a per-user basis. 

The first step is to [create a user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#creating_user_attributes), such as `custom_schema` or `custom_table`, to which you will assign a value for each user. You can assign these values: 

  * Through the UI
  * In [bulk via the API](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/UserAttribute/user_attribute)
  * In the [SSO URL for embedded contexts](https://github.com/looker/looker_embed_sso_examples/blob/master/node_example.js#L31). 



Once you have created the user attribute and assigned the appropriate value for your users, you can add a reference to that attribute in the `sql_table_name` of your view files, via [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference). Following are two examples, one using a custom schema and one a custom table. 

## Example A

Using a `custom_schema`: 
    
    
    view: events {
     sql_table_name: {{ _user_attributes['custom_schema'] }}.events ;;
    
    
    
     dimension: event_id {
       type: number
       primary_key: yes
       sql: ${TABLE}.id ;;
     }
    }
    

## Example B

Using a `custom_table`: 
    
    
    view: events {
      sql_table_name: web_traffic.{{ _user_attributes['custom_event_table_name'] }} ;;
    
    
    
      dimension: event_id {
        type: number
        primary_key: yes
        sql: ${TABLE}.id ;;
     }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
