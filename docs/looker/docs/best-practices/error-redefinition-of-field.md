---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-redefinition-of-field/
title: Error: Redefinition of field \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:38.587683+00:00
---

# Error: Redefinition of field  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-redefinition-of-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Redefinition of field Stay organized with collections  Save and categorize content based on your preferences. 

The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#running_validation) and [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) let you detect and resolve the `Redefinition of field 'view_name.field_name'` error in your LookML project. By inspecting your view and Explore join definitions, including joins aliased with the `from` parameter, you can locate and rename duplicate dimensions, measures, or joins.

## Common causes of Error: Redefinition of field 

The error `Redefinition of field 'view_name.field_name'` appears under **LookML Errors** in the **Project Health Panel** after you run the LookML Validator, and means that Looker has identified two fields with exactly the same combination of view and field names. 

There are several common causes of the error: 

  * You have accidentally named two fields with the same name in the same view. This could be:
    * Two dimensions with the same name
    * Two measures with the same name
    * One dimension and one measure with the same name
  * You copied and pasted a field in a view and forgot to change the name.
  * You joined a view to your Explore a second time but forgot to give the join a different name.
  * You used the LookML generator to create your LookML project and created duplicate fields. 

For example, you use the LookmL generator and your data table has a column named `count`. In this case, Looker will create a dimension named `count`, which references the column in your table. By default, Looker will also create a measure named `count` (which is the only default measure that Looker creates). Since the two fields are both named `count`, the error occurs. 




The next section of this page will help you identify the view in your LookML project that is the source of the error. 

## Finding the view mentioned in the error

Keep in mind that the view name that is mentioned in the error will be [the view name as it is defined in the `explore` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) where the view is joined. 

For the typical case, the view name is easy to understand. For example, you could have the following join: 
    
    
    join: address
    foreign_key: order.billing_id
    

In this example, the view name that is mentioned in the error is `address`, as specified in the `join` parameter. 

### Finding the source view when a view name is aliased in a join

If you are using an alias to change the way a view name is displayed in a join, the alias name will be mentioned in the error message. For example, suppose you have a join using the [`from` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from). The `from` parameter lets you give the join a different name than the underlying view, which is useful when you want to join the same view a second time. 
    
    
    join: billing_address
    from: address
    foreign_key: order.billing_id
    

In this example, the view name that is mentioned in the error from the LookML view file will be `billing_address` and not `address`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
