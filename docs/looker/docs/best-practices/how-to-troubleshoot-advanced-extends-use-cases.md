---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-advanced-extends-use-cases/
title: Troubleshooting an example of an advanced extends use case \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:18:50.284026+00:00
---

# Troubleshooting an example of an advanced extends use case  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-advanced-extends-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting an example of an advanced extends use case Stay organized with collections  Save and categorize content based on your preferences. 

> _This page covers an advanced topic and assumes a solid knowledge of LookML on the part of the reader._

[Extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) is a valuable LookML feature that allows you to maintain DRY (don't repeat yourself) LookML code. In Looker, [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends), [views](https://docs.cloud.google.com/looker/docs/reference/param-view-extends), and [LookML dashboards](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#extending_a_lookml_dashboard) can all be extended with the `extends` parameter within a model file, such as in the following example: 
    
    
    explore: orders {
      view_name: orders
      join: users {
        type: left_outer
        sql_on: %{orders.user_id} = ${users.id} ;;
        relationship: many_to_one
      }
    }
    
    explore: transactions {
      extends: [orders]
    }
    

In this example, the `extends` parameter is used within the definition of the `transactions` Explore to extend the `orders` Explore. 

This page refers to the object that is being extended as the _base_ object, and the object that is doing the extending is referred to as the _extending_ object. 

Extending a LookML object is a fairly straightforward process, as detailed on the [Reusing code with extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#details_of_extend_functionality) documentation page. However, there are some advanced use cases that can cause LookML reference errors and unwanted object duplication. This page provides an example of how extending an Explore based on a view that extends another view can result in LookML reference errors, as well as tips that can help eliminate such issues. 

## Use case: Extending an Explore based on an extending view

Suppose you want to extend the `events` Explore, and you want the view that the extending Explore is based on to use fields from a view that extends the base `events` view. In this example, the `events_extended` Explore extends the `extends` Explore, as shown in the following example LookML: 
    
    
    explore: events {
      view_name: events
      join: users {
        type: left_outer
        sql_on: ${events.user_id} = ${users.id} ;;
        relationship: many_to_one
      }
    }
    
    explore: events_extended {
      extends: [events]
      join: orders {
        sql_on: ${events_extended.test_id} = ${orders.id} ;;
        relationship: many_to_one
      }
    

In this example, the `users` view is joined to the base `events` Explore, while the `orders` view is joined to the extending Explore, `events_extended`. However, the join defined in the base `events` Explore references `events.user_id`, which is a field from the base `events` view. Meanwhile, the join defined in the extending `events_extended` Explore references the field `events_extended.test_id`, where `events_extended` is the name of an extending view based on the `events` view. The `test_id` field that is referenced in the join in the `events_extended` Explore definition is defined in the extending `events_extended` view as follows: 
    
    
    include: "events.view.lkml"
    view: events_extended {
      extends: [events]
    
      dimension: test_id {}
    

Because the join defined in the `events_extended` Explore references the name of the extending view, `events_extended`, the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) displays an [`inaccessible view`](https://docs.cloud.google.com/looker/docs/error-catalog#inaccessible_view_\(?\)._\(?\)_is_not_accessible_in_explore_\(?\)._check_for_missing_joins_in_explore_\(?\).) error. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-lookml-validation-error-2214.png)

To address this, you can add the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter to the LookML for the extending Explore and set its value to the name of the extending view, `events_extended`. The `from` parameter aliases the original table name in the generated SQL, as `FROM schema.name AS alias`. 

> _This is the only recommended use case for applying the`from` parameter at the Explore level._

To pull from the extending view (`events_extended`) without breaking the join references from the base Explore (`events`), you can add a `from` parameter that maps to the extending view: 
    
    
    explore: events_extended {
      extends: [events]
      from: events_extended
      join: orders {
        relationship: many_to_one
        sql_on: ${events.test_id} = ${orders.id} ;;
      }
    }
    

In this example, applying the LookML `from: events_extended` to the LookML for the extending Explore lets you continue referencing the base view (`events`) in the extending Explore, while redirecting those references to pull from the extending version of that view (`events_extended`). 

With the use of the `from` parameter, you can continue to reference the base view name `events` in the join prefixes, but these references will pull from the extending view `events_extended`, which contains all the fields in `events`, plus the new `test_id` field. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
