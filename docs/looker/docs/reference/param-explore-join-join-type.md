---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-join-type/
title: join_type \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:46.300136+00:00
---

# join_type  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-join-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  join_type Stay organized with collections  Save and categorize content based on your preferences. 

`join_type` should be avoided as of Looker 3.10; use [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) instead.

## Definition

`join_type` lets you describe a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) as having a one-to-one relationship.

Join relationships that are _not_ one-to-one can create inaccurate results when aggregate functions are used. Since Looker [measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) are in fact aggregate functions, only measures of `type: count` (as `COUNT DISTINCT`) are brought from joined views into the Explore. Consider this example:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

-

In this situation, when a user works with the `order` Explore, they will see all the dimensions and measures from `order`. They will also see all the dimensions from `customer`, but will only see the measures of `type: count` from `customer`. Looker works this way so that repeated rows, which can occur in many-to-one and one-to-many joins, don't inflate values in functions such as `SUM`. This document is discussed in more detail in [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) Community post.

`order` to `customer` is a many-to-one relationship. If it was a one-to-one relationship instead, you could use `join_type` to force the non-count measures from `customer` to be included.

## Examples

Declare the join of `person` to `dna` as having a one-to-one relationship:
    
    
    explore: person {
      join: dna {
        sql_on: ${person.dna_id} = ${dna.id} ;;
        relationship: one_to_one
      }
    }
    

-

## Common challenges

### `join_type` shouldn't be used unless the join is actually one-to-one

Many users are tempted to use `join_type: one_to_one`, even if the join is many-to-one or one-to-many, solely to expose all measures in an Explore. We strongly suggest you don't do this, because — in certain situations — measures won't give you accurate results. Rows are often repeated in many-to-one or one-to-many joins, causing double counting and similar errors. The Community post [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) explains this issue in more detail.

## Things to know

### You can expose measures from joined views without using `join_type`

In some cases, you might carefully consider the situation and decide that it is safe to add a non-count measure from a joined view to an Explore. There is a method to accomplish this. Suppose we have an Explore like this:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

-

In the `customer` view we have a measure like this:
    
    
    measure: max_age {
      type: max
      sql: ${age} ;;
    }
    

-

In this situation, it is probably safe to expose the maximum customer age as a measure in the `order` Explore. To achieve this, you would add a new measure to the `order` view, like this:
    
    
    measure: max_customer_age {
      type: max
      sql: ${customer.age} ;;
    }
    

-

This method does not protect you from errors in and of itself. You must carefully consider if the interaction between the measure and your join will create inaccurate results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
