---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship/
title: relationship \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:25.417784+00:00
---

# relationship  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  relationship Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: view_name {
      join: view_name_2 {
        relationship: one_to_one
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `relationship` |  Default Value `many_to_one` Accepts A relationship (`many_to_one`, `many_to_many`, `one_to_many`, `one_to_one`)   
---|---  
  
## Definition

`relationship` lets you describe the [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) relationship between joined views. It's important to properly define the type of relationship in order for Looker to calculate accurate measures.

To understand the relationship that is being defined, consider this example:
    
    
    explore: order {
      join: user {
        sql_on: ${order.user_id} = ${user.id} ;;
        relationship: many_to_one
      }
      join: user_facts {
        sql_on: ${user.id} = ${user_facts.user_id} ;;
        relationship: one_to_one
      }
    }
    

When a view is joined directly to an Explore, like the `user` view in this example, the relationship is _from_ the Explore _to_ the joined view. We're saying here that there could be _many_ orders for _one_ user.

When a view is joined to an Explore through another view — such as how `user_facts` joins through `user` to `order` in this example — the relationship being defined is _from_ the intermediate view (`user`) _to_ the final view (`user_facts`). In this example we're saying there is _one_ user for _one_ user fact record.

The possible values for `relationship` are described in these sections of this page:

  * `one_to_one`
  * `many_to_one` (default value)
  * `one_to_many`
  * `many_to_many`



### one_to_one

If one row in the Explore can only match one row in the joined view, the relationship is `one_to_one`. For example, a `user` Explore with a `user_facts` joined view would be `one_to_one`, since both tables have one row per user.

> A `one_to_one` relationship requires that there be no null values in the primary keys of the tables. If there are null values in one or both of the primary keys of the tables, the relationship is either `many_to_many` or `many_to_one`.

### many_to_one (default value)

If many rows in the Explore can match one row in the joined view, the relationship is `many_to_one`. For example, an `order` Explore with a `user` joined view would be `many_to_one`, because there may be multiple orders per user.

![](https://docs.cloud.google.com/static/looker/docs/images/relationship-many_to_one.png)

### one_to_many

If one row in the Explore can match many rows in the joined view, the relationship is `one_to_many`. For example, an `order` Explore with an `item` joined view would be `one_to_many`, because one order can contain multiple items..

![](https://docs.cloud.google.com/static/looker/docs/images/relationship-one_to_many.png)

### many_to_many

If many rows in the Explore can match many rows in the joined view, the relationship is `many_to_many`. For example, a `student` Explore with a `class` joined view _could_ be `many_to_many` if a student has multiple classes and a class has multiple students. In practice, `many-to-many` relationships are often avoided in SQL database design, so most models do not have a need for `many_to_many`.

![](https://docs.cloud.google.com/static/looker/docs/images/relationship-many_to_many.png)

## Examples

Declare the `user` to `dna` relationship as `one_to_one`:
    
    
    explore: user {
      join: dna {
        sql_on: ${user.dna_id} = ${dna.id} ;;
        relationship: one_to_one
      }
    }
    

Declare the `order` to `user` relationship as `many_to_one`:
    
    
    explore: order {
      join: user {
        sql_on: ${order.user_id} = ${user.id} ;;
        relationship: many_to_one
      }
    }
    

Declare the `order` to `item` relationship as `one_to_many`:
    
    
    explore: order {
      join: item {
        sql_on: ${order.order_id} = ${item.order_id} ;;
        relationship: one_to_many
      }
    }
    

Declare the `student` to `class` relationship as `many_to_many`:
    
    
    explore: student {
      join: class {
        sql_on: ${student.student_id} = ${class.student_id} ;;
        relationship: many_to_many
      }
    }
    

Declare the `user` to `user_type` relationship as `many_to_one`:
    
    
    explore: order {
      join: user {
        sql_on: ${order.user_id} = ${user.id} ;;
        relationship: many_to_one
      }
      join: user_type {
        sql_on: ${user.type_id} = ${user_type.id} ;;
        relationship: many_to_one
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
