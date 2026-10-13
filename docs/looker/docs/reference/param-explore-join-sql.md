---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql/
title: sql (for joins) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:59.617623+00:00
---

# sql (for joins)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  sql (for joins) Stay organized with collections  Save and categorize content based on your preferences. 

`sql` should be avoided as of Looker 3.12.

Use a combination of [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on), [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key), [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type), and/or [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) instead, as described in the Definition section on this page.

> This page refers to the `sql` parameter that is part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join).
> 
> `sql` can also be used as part of a field, as described on the [`sql` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter documentation page.
> 
> `sql` can also be used as part of a derived table, as described on the [`sql` (for derived tables)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table) parameter documentation page.

## Definition

`sql` lets you write the raw SQL that will join a view to an Explore. It is currently used almost exclusively to execute `RIGHT JOIN`, which is not supported by the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) parameter. Otherwise, there are better parameters to use to execute joins.

Previous to Looker 3.10, `sql` was the only method available to execute a join that was not a `LEFT JOIN`. For example, before 3.10 you may have created an `INNER JOIN` between an `event` Explore and a `member` view like this:
    
    
    explore: event {
      join: member {
        sql:
          INNER JOIN member
          ON member.id = event.member_id ;;
      }
    }
    

-

As of Looker 3.10 the join should be executed with [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) or [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) instead, while the type of join should be defined using [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) as follows:
    
    
    # Option 1 Using sql_on
    explore: event {
      join: member {
        sql_on: ${member.id} = ${event.member_id} ;;
        type: inner
      }
    }
    
    # Option 2 Using foreign_key
    explore: event {
      join: member {
        foreign_key: member_id
        type: inner
      }
    }
    

-

The second common use case for `sql` was to join tables from two different database, which is called a "Federated Join". For example, you might have written this LookML:
    
    
    # Model File
    explore: view_1 {
      join: view_2 {
        sql:
          LEFT JOIN other_db.other_schema.view_2 AS view_2
          ON view_1.something = view_2.something ;;
      }
    }
    

-

This can now be achieved by using `sql_table_name` instead, as follows:
    
    
    # Model File
    explore: view_1 {
      join: view_2 {
        sql_on: ${view_1.something} = ${view_2.something} ;;
        type: left_outer
      }
    }
    
    # View File
    view: view_2 {
      sql_table_name: other_db.other_schema.view_2 ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
