---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-preamble/
title: sql_preamble \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.868152+00:00
---

# sql_preamble  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-preamble/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_preamble Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      sql_preamble: SQL STATEMENT  ;;
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `sql_preamble` |  Default Value None Accepts A SQL expression   
---|---  
  
## Definition

The `sql_preamble` parameter specifies a SQL statement that executes before queries in the Explore are run. The primary use for `sql_preamble` is to create user-defined functions (UDFs) on Google BigQuery. Most database dialects let you install UDFs directly on the database server, but Google BigQuery is stateless, so `sql_preamble` provides this functionality.

## Using Liquid in `sql_preamble`

The `sql_preamble` parameter supports Liquid and user attributes, which enables dynamic SQL generation for use cases such as setting session variables, selecting different warehouses or databases, implementing partition pruning in BigQuery, and allowing for flexible data filtering by interacting with the underlying database more directly.

The following Liquid use patterns are supported in the `sql_preamble` parameter: 

  * [`_filters['view_name.field_name']`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#_filters)
  * [`{% date_start date_filter_name %}`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#date_start)
  * [`{% date_end date_filter_name %}`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#date_end)
  * [`{% condition filter_name %} sql_or_lookml_reference {% endcondition %}`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#condition_filter_name)
  * `{% if %} sql_or_lookml_reference {% else %} other_value {% endif %}`
  * [`{% parameter parameter_name %}`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#parameter)
  * [`parameter_name._parameter_value`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#parameter_value)
  * [`_user_attributes['name_of_attribute']`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#user_attributes)
  * [`_localization['localization_key']`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#localization)
  * [`_model._name`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#model)
  * [`_explore._name`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#explore_name)
  * [`_explore._dashboard_url`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#explore_dashboard)
  * [`_query._query_timezone`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#query_timezone)
  * [`view_name._in_query`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#in_query)
  * [`view_name.field_name._in_query`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#view_name_field_name_in_query)
  * [`view_name.field_name._is_selected`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#is_selected)
  * [`view_name.field_name._is_filtered`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#is_filtered)
  * [`_view._name`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#view_name)



The following Liquid use patterns are not supported in `sql_preamble`:

  * `value`
  * `rendered_value`
  * `filterable_value`
  * `link`
  * `linked_value`
  * `_field._name`



## Examples

### Using `sql_preamble` to specify a BigQuery reservation

Specify a [Google BigQuery reservation](https://docs.cloud.google.com/bigquery/docs/reservations-intro#reservations) to use for the Explore's queryies by using the BigQuery [`SET @@reservation`](https://docs.cloud.google.com/bigquery/docs/reservations-assignments#sql_3) SQL statement in the `sql_preamble` parameter:
    
    
    explore: orders {
      sql_preamble:
        SET @@reservation='projects/your-project/locations/your-location/reservations/your-reservation';
    }
    

### Using `sql_preamble` to add a temporary median

Create a user-defined function (UDF) on Google BigQuery that computes a median by using the Google BigQuery `CREATE TEMP FUNCTION` statement, and inserts the median function into the Google BigQuery SQL before each query in the Explore is run.
    
    
    explore: salary {
      sql_preamble:
        CREATE TEMP FUNCTION MEDIAN(a_num ARRAY<FLOAT64>)
        RETURNS FLOAT64 AS ((
           SELECT
              AVG(num)
            FROM (
              SELECT
                row_number() OVER (ORDER BY num) -1 as rn
                , num
              FROM UNNEST(a_num) num
            )
            WHERE
              rn = TRUNC(ARRAY_LENGTH(a_num)/2)
                OR (
                 MOD(ARRAY_LENGTH(a_num), 2) = 0 AND
                  rn = TRUNC(ARRAY_LENGTH(a_num)/2)-1 )
        ));
      ;;
    }
    

### Using Liquid in `sql_preamble` to localize the table name

Use Liquid in `sql_preamble` to create a temporary table that's named based on the user's selected language, so that a single LookML model can adapt to different internal naming conventions:
    
    
    explore: orders {
      sql_preamble: 
        WITH {{ _localization['storage_table_name'] }} AS (select * from users);;
      ...
    }
    

Instead of using a hardcoded name like `mytable` for the temporary table, this code will replace the Liquid variable with the actual string that's defined in the [locale strings file](https://docs.cloud.google.com/looker/docs/model-localization#creating_locale_strings_files) for the key `storage_table_name`. See [Using locale in Liquid variables](https://docs.cloud.google.com/looker/docs/model-localization#using_locale_in_liquid_variables) for more information.

The Looker query that follows the preamble would then reference this dynamically named table. For example, the SQL query would use `FROM {{ _localization['storage_table_name'] }}`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
