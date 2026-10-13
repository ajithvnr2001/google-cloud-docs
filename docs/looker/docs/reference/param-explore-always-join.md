---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join/
title: always_join \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:20.395268+00:00
---

# always_join  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  always_join Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    explore: explore_name {
      always_join: [
        view_name,
        view_name,
        ...
      ]
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `always_join` |  Default Value None Accepts Square brackets containing a comma-separated list of view names Special Rules You must join a view to the `explore` before using it in `always_join`  
---|---  
  
## Definition

`always_join` forces one or more [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) to be included in the SQL that Looker generates, even if the user has not selected a field from that joined view. Multiple joins can be required by using a comma-separated list like `[view_name_a, view_name_b, etc]`.

When Looker generates SQL for a query, it attempts to create the cleanest SQL possible, and will only use the joins that are necessary for the fields a user selects. By using `always_join`, you can force joins to occur no matter what.

`always_join` may be valuable when a join is executed with the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) parameter, and the join is not a `LEFT JOIN`. In such a situation the join may be critical to correctly limiting the rows that are returned.

## Examples

Make sure that `member` is always joined to `event`, even if the user does not choose a field from `member`. This limits the results to only look at member-generated events:
    
    
    explore: event {
      always_join: [member]
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
        type: inner
      }
    }
    

Make sure that `member` and `payment` are always joined to `event`, even if the user does not choose a field from either of those views. This limits the results to only look at member-generated events where the member has paid already:
    
    
    explore: event {
      always_join: [member, payment]
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
        type: inner
      }
      join: payment {
        sql_on: ${member.payment_id} = ${payment.id} ;;
        type: inner
      }
    }
    

## Common challenges

### A view must be joined to an Explore before it can be referenced in `always_join`

To place a view into `always_join`, make sure that it is joined to the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) where the `always_join` is being used. For example, this will not work:
    
    
    explore: event {
      always_join: [member]
    }
    

Here the `member` view hasn't been joined to `event`, so it isn't available for use in `always_join`.

## Things to know

### Don't apply business logic in joins if possible

The standard Looker approach to joining is to use a `LEFT JOIN` whenever possible. In the previous examples, we avoid a `LEFT JOIN` so that business logic can be applied within the join itself. In one of the examples we created an Explore that included only those events that were associated with members:
    
    
    explore: event {
      always_join: [member]
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
        type: inner
      }
    }
    

The preferred way to execute this in Looker is to use a `LEFT JOIN` to get event data and member data stuck together simply:
    
    
    explore: event {
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
      }
    }
    

Then you could create a dimension that you could set to yes or no, to look only at member events:
    
    
    dimension: is_member_event {
      type: yesno
      sql: ${member.id} IS NOT NULL ;;
    }
    

This approach gives users the flexibility to look at all events, or only member events. You have not forced users to only look at member events via the join.

### When an Explore includes `always_join`, the default value of `full_suggestions` switches to `yes`

When an Explore includes the `always_join` parameter, the default value of [`full_suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions) switches to `yes`. This causes the suggestions query to run using the Explore logic, which means that `always_join` will be applied to narrow the suggestions that come back, limiting the list of suggestions to only the data that the user is intended to have access to.

If you manually set `full_suggestions` to `no`, the filter suggestion query won't run.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-19 UTC."],[],[]] 
