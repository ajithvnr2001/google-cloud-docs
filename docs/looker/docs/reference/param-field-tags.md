---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-tags/
title: tags (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:25.109113+00:00
---

# tags (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  tags (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `tags` parameter that is part of a field.
> 
> `tags` can also be used as part of an Explore, described on the [`tags` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-tags) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        tags : ["string1","string2", ...]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `tags` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts Square brackets containing a comma-separated list of strings  
---|---  
  
## Definition

The `tags` parameter lets you add text strings to a field. These strings are not used by the Looker model but can be passed to other applications using:

  * Integrated services enabled on the [**Action** panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions). Some services require one or more fields containing certain types of data, such as a phone number. Use the `tags` parameter to identify those fields that can be used by a service.
  * [API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model). For API calls, `tags` can be useful for providing arbitrary metadata about a field to an outside application.



## Examples

Adds two text tags, "Important Data" and "Customer Data", to the `customer_count_distinct` measure.
    
    
    measure: customer_count_distinct {
      tags: ["Important Data", "Customer Data"]
      type: count_distinct
      sql: ${customer.id} ;;
    }
    

## Using `tags` with integrated services

Some integrated services in the [Action panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) require that you identify a specific field in your LookML model using the `tags` parameter. This will be a field or fields that provide identifying data to that service.

For example, the **Twilio Send Message** service sends a message to phone numbers. It requires a query that includes a phone number field, and that you identify the phone number field in LookML using `tags: ["phone"]`. Looker uses the `tags` parameter to identify which field in the query contains phone numbers that should be sent to Twilio. Your LookML for the phone number field could look like this:
    
    
    measure: phone {
      tags: ["phone"]
      type: string
      sql: ${TABLE}.phone ;;
    }
    

Some integrated services can be called from a row in an Explore, a dashboard tile, or a Look. In this case, Looker marks the tagged field with three dots to indicate that there is a drop-down list. Select the three dots to see the actions available for that link:

![](https://docs.cloud.google.com/static/looker/docs/images/admin-actions-send-row-54.png)

Other integrated services can be used when [delivering Looker content](https://docs.cloud.google.com/looker/docs/scheduling) to various destinations. If a query's results contain the required tagged fields for an enabled service, then the **Where should this data go?** field of the Scheduler displays the service and the required field. Looker also displays the service as a destination if the service does not require a tagged field.

For more information about the integrated services that are available in the Looker Action Hub, see the [Admin settings — Actions](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#list_of_integrated_services) section of the **Actions** page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
