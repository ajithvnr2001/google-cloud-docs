---
url: https://docs.cloud.google.com/data-studio/how-to-add-more-than-10-andor-filters-to-a-chart/
title: How to add more than 10 AND/OR filters to a chart \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:09.257174+00:00
---

# How to add more than 10 AND/OR filters to a chart  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/how-to-add-more-than-10-andor-filters-to-a-chart/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  How to add more than 10 AND/OR filters to a chart Stay organized with collections  Save and categorize content based on your preferences. 

**Tip:** To get the most from this page, you should be familiar with the following concepts: 

  * [Create, edit, and manage filters](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties)
  * [Add, edit, and troubleshoot calculated fields](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields)
  * [About controls](https://docs.cloud.google.com/data-studio/about-controls)
  * [Advanced filter controls](https://docs.cloud.google.com/data-studio/advanced-filter-control)



When [creating a filter on a chart](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties), you can add `AND/OR` conditions. However, once you've added more than 10 `OR` conditions, you cannot add any more `OR` clauses unless you create a new `AND` condition.

![](https://docs.cloud.google.com/static/data-studio/images/10-or-fields.png)

There are a few ways to work around this limitation:

  * Update the filter conditions to another type
  * Move the filter conditions into a new field



One way to work around this limit is to change your filter conditions to a more inclusive filter type.

For example, if you want a field to match 11 possible values, you can use the `IN` filter type and list each of those values.

As another example, consider a field with product names. You want to create a filter that returns all products that start with the 12 letters A-L. You can achieve this with a RegExp Match type filter by using the appropriate [regular expression syntax](https://docs.cloud.google.com/data-studio/regular-expressions). In this example, the syntax would be the following: `REGEXP_MATCH(field, "^[A-L].*")`

Another workaround is to move the conditions into a separate calculated field and filter on that new field. Calculated fields don't have the same limit on the number of logical conditions that can be included.

For example, if you have 11 different fields, and you want to create a filter that checks if any of them contains a specific error string.

You can create a new field that has the 11 `OR` conditions that you'd need to check this condition. The formula would look like this example:
    
    
    CONTAINS_TEXT(log_field_1, "error")
    OR
    CONTAINS_TEXT(log_field_2, "error")
    OR
    CONTAINS_TEXT(log_field_3, "error")
    OR
    CONTAINS_TEXT(log_field_4, "error")
    OR
    CONTAINS_TEXT(log_field_5, "error")
    OR
    CONTAINS_TEXT(log_field_6, "error")
    OR
    CONTAINS_TEXT(log_field_7, "error")
    OR
    CONTAINS_TEXT(log_field_8, "error")
    OR
    CONTAINS_TEXT(log_field_9, "error")
    OR
    CONTAINS_TEXT(log_field_10, "error")
    OR
    CONTAINS_TEXT(log_field_11, "error")
    

This formula field will create a Boolean field type, which evaluates to `True` OR `False`.

Finally, create a filter that filters on this new field being `True`.

![](https://docs.cloud.google.com/static/data-studio/images/filter-field-11-ors.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
