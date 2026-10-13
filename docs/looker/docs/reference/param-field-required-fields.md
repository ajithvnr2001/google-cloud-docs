---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-required-fields/
title: required_fields \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:37.702455+00:00
---

# required_fields  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-required-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  required_fields Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure: field_name {
        required_fields: [field_name, field_name, …]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `required_fields` |  Possible Field Types Dimension, Measure Accepts A square-bracketed list of dimensions and/or measures  
---|---  
  
## Definition

The `required_fields` parameter lets you pull additional fields into a query when a user chooses a specific field. In this example, when the user chooses the **Linked Name** dimension, the `url` field is also pulled into the query:
    
    
    dimension: linked_name {
      sql: ${name} ;;
      html: <a href="{{ row['websites.url'] }}" target="_new">{{ value }}</a> ;;
      required_fields: [url]
    }
    

Although the required fields are added to the query, _they do not display to the user_. If the required fields change the aggregation of the query, it can be confusing for the user.

The LookML example that shows `url` as the required field will likely work because there will likely be the same number of unique website names and website URLs. However, if the data listed several URLs for the same website name (such as naming both `google.com` and `google.com/news` as **Google**), then there could be multiple rows that have the same name but different underlying URLs. Looker typically collapses identical names into one row, but it won't do so in this case because Looker is acting as if the `url` field was also added.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
