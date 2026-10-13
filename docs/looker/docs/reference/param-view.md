---
url: https://docs.cloud.google.com/looker/docs/reference/param-view/
title: View parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.838392+00:00
---

# View parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  View parameters Stay organized with collections  Save and categorize content based on your preferences. 

A view represents a table of data in Looker, whether that table is built-in to your database or was created using Looker's [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) functionality. Views are typically declared in [view files](https://docs.cloud.google.com/looker/docs/model-and-view-files#view_files), with one view per file.

Within each view are field definitions, each of which typically corresponds to a column in the underlying table or a calculation in Looker. These fields are described in the [field reference](https://docs.cloud.google.com/looker/docs/reference/param-field), [dimension type reference](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types), and [measure type reference](https://docs.cloud.google.com/looker/docs/reference/param-measure-types).

There are also a number of view-level settings, which are described on this page.

## Example usage

Hold your pointer over a parameter name to see a quick description. Click a parameter to visit its reference page. When a parameter can be set to one of several specific options, the default value is listed first.
    
    
    ## STRUCTURAL PARAMETERS
    
    [include](https://docs.cloud.google.com/looker/docs/reference/param-model-include "Adds files to a view"):"filename_or_pattern"
    ## Possibly more include declarations
    
    [test](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Creates a data test to verify your model's logic"): test_name{
      [explore_source](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Specifies the source Explore for the test query"): explore_name {
        # Desired subparameters (described on [test](https://docs.cloud.google.com/looker/docs/reference/param-model-test) page)
      }
      [assert](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Defines a yes/no Looker expression that must result in yes for the test to pass"): assert_statement {
        [expression](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Specifies the yes/no Looker expression to be executed to test your model's logic"):Looker expression ;;
      }
      # Possibly more assert declarations
    }
    ## Possibly more test declarations
    
    [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view "Creates a view"): view_name {
      [extension](https://docs.cloud.google.com/looker/docs/reference/param-view-extension "Specifies that the view requires extension"): required
      [extends](https://docs.cloud.google.com/looker/docs/reference/param-view-extends "Specifies view\(s\) that will be extended by this view"): [view_name, view_name, ...]
    
      ([dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension "Creates a dimension field") | [dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group "Creates several time-based dimensions at the same time") | [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure "Creates a measure field") | [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter "Creates a filter-only field for use in a templated filter")):field_name{
        # Desired field parameters (described on [Field Parameters](https://docs.cloud.google.com/looker/docs/reference/param-field) page)
      }
      # Possibly more field declarations
    
      [set](https://docs.cloud.google.com/looker/docs/reference/param-view-set "Defines a set of dimensions and measures to be used in other parameters"): set_name{
        [fields:](https://docs.cloud.google.com/looker/docs/reference/param-view-set "See set page for more detail")[field_or_set, field_or_set, ...]
      }
      # Possibly more set declarations
    
      [drill_fields](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields "Declares the default list of fields that will be displayed when measures defined in the view are drilled into"): [field_or_set, field_or_set, ...]
    
      # CUSTOM CALENDAR PARAMETERS
    
        [calendar_definition](https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition "Defines the mapping between a custom calendar definition on your database and your custom calendar view in LookML"): {
          Custom calendar mapping parameters ;;
        }
    
      # DISPLAY PARAMETERS
    
      [label](https://docs.cloud.google.com/looker/docs/reference/param-view-label "Specifies how the view name will appear in the field picker"): "desired label"
      [fields_hidden_by_default](https://docs.cloud.google.com/looker/docs/reference/param-view-fields-hidden-by-default "Hides all fields in the view"): yes | no
    
      # FILTER PARAMETERS
    
      [suggestions](https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions "Enables or disables suggestions for all dimensions on this view"): yes | no
    
      # QUERY PARAMETERS
    
      [autogenerate_primary_keys](https://docs.cloud.google.com/looker/docs/reference/param-explore-autogenerate-primary-keys "Enables or disables automatic primary key generation"): yes | no
      [required_access_grants](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants "Specifies which access grants are required for a user to access this view"): [access_grant_name, access_grant_name, ...]
      [sql_table_name](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name "Changes the SQL table on which a view is based"): table_name ;;
      [derived_analytic_model](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model "Define an in-database analytic model managed by Looker"): {
        [sql](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model#sql "Declares the SQL query for a derived analytic model"): analytic_model_definition ;;
      }
      [sql_analytic_model_name](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name "Specify the in-database analytic model on which a view is based"): analytic_model_name ;;
    
      # DERIVED TABLE PARAMETERS
    
      [derived_table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table "Bases a view on a derived table"): {
        [cluster_keys](https://docs.cloud.google.com/looker/docs/reference/param-view-cluster-keys "Specifies that a persistent derived table be clustered by one or more fields in BigQuery and Snowflake"): ["column_name", "column_name", ...]
        [create_process](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process "Specifies an ordered sequence of steps to create a PDT on a database dialect that requires custom DDL commands"): {
          [sql_step](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process "Specifies SQL to be executed as one step of this PDT creation process"):SQL query ;;
        }
        [datagroup_trigger](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger "Specifies the datagroup to use for the PDT rebuilding policy"): datagroup_name
        [distribution](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution "Sets the distribution key of a persistent derived table that is built in Redshift or Aster"): "column_name"
        [distribution_style](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style " Sets the distribution style of a persistent derived table that is built in Redshift"): all | even
        [explore_source](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source "Specifies a native derived table that's based on an Explore"): explore_name {
          # Desired subparameters (described on [explore_source](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) page)
        }
        [increment_key](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key "Specifies the time increment for which fresh data should be queried and appended to an incremental PDT"): "column_name"
        [increment_offset](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset "Specifies of number of previous time periods \(at the increment key granularity\) that are rebuilt to account for late arriving data for an incremental PDT"): N
        [indexes](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes "Sets the indexes of a persistent derived table built in a traditional database \(for example, MySQL, Postgres\) or an interleaved sort key in Redshift"): ["column_name", "column_name", ...]
        [interval_trigger](https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger "Specifies a rebuild schedule for a persistent derived table"): "N (seconds | minutes | hours)"
        [materialized_view](https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view "Creates a materialized view on your database for a derived table"): yes | no
        [partition_keys](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys "Specifies that a persistent derived table be partitioned by one or more fields in Presto, or by a single date/time field in BigQuery"): ["column_name", "column_name", ...]
        [persist_for](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table "Sets the maximum age of a persistent derived table before it is regenerated"): "N (seconds | minutes | hours)"
        [publish_as_db_view](https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view "Creates a stable database view for the PDT to enable querying the table outside of Looker"): yes | no
        [sortkeys](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys "Sets the sort keys of a persistent derived table that is built in Redshift"): ["column_name","column_name", ...]
        [sql](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table "Declares the SQL query for a derived table"): SQL query ;;
        [sql_create](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create "Defines a SQL CREATE statement to create a PDT on a database dialect that requires custom DDL commands"): {
          SQL query ;;
        }
        [sql_trigger_value](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value "Specifies the condition that causes a persistent derived table to be regenerated"): SQL query ;;
        [table_compression](https://docs.cloud.google.com/looker/docs/reference/param-view-table-compression " Specifies the table compression to use for a PDT in Amazon Athena"): GZIP | SNAPPY
        [table_format](https://docs.cloud.google.com/looker/docs/reference/param-view-table-format " Specifies the table format to use for a PDT in Amazon Athena"): PARQUET | ORC | AVRO | JSON | TEXTFILE
      }
    }
    
    ## REFINEMENT PARAMETERS
    view: [+view_name](https://docs.cloud.google.com/looker/docs/lookml-refinements "Adds a refinement to an existing view") {
      [final](https://docs.cloud.google.com/looker/docs/lookml-refinements#final "Indicates that this is the final refinement allowed for the view"): yes
    }
    

## Parameter definitions

Parameter Name | Description  
---|---  
Structural Parameters  
[`drill_fields` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields) | Specifies the default list of fields shown when drilling into measures defined in the view  
[`extends` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-extends) | Specifies view(s) that will be extended by this view  
[`extension` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-extension) | Specifies that the view requires extension and cannot itself be exposed to users  
[`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) | Adds files to a view  
[`test`](https://docs.cloud.google.com/looker/docs/reference/param-model-test) | Creates a data test to verify your model's logic. The project settings include an option to [require data tests](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests). When this is enabled for a project, developers on the project must run data tests before deploying their changes to production. This parameter has `explore_source` and `assert` subparameters.  
[`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) | Defines a set of dimensions and measures to be used in other parameters  
[`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) | Creates a view  
Display Parameters  
[`label` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-label) | Specifies how the view name will appear in the field picker  
[`fields_hidden_by_default`](https://docs.cloud.google.com/looker/docs/reference/param-view-fields-hidden-by-default) |  Added 21.12  When set to `yes`, hides all fields in the view by default. Use the [`hidden: no`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter on a field to display the field.  
Filter Parameters  
[`suggestions` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions) | Enables or disables suggestions for all dimensions on this view  
Query Parameters  
[`autogenerate_primary_keys` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-explore-autogenerate-primary-keys) | Enables or disables automatic primary key generation  
[`required_access_grants` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants) | Limits access to the view to only users whose user attribute values match the access grants  
[`sql_table_name` (for view)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) | Changes the SQL table on which a view is based  
Derived Table Parameters  
[`cluster_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-cluster-keys) | Specifies that a PDT be clustered by one or more fields in BigQuery Support added for `cluster_keys` on Snowflake  
[`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) | Specifies an ordered sequence of steps to create a PDT on a database dialect that requires custom DDL commands. This parameter has the subparameter `sql_step`.   
[`datagroup_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger) | Specifies the datagroup to use for the PDT rebuilding policy  
[`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) | Bases a view on a derived table  
[`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution) | Sets the distribution key of a PDT that is built in Redshift or Aster  
[`distribution_style`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style) | Sets the distribution style of a PDT that is built in Redshift  
[`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) |  Defines a [native derived table](https://docs.cloud.google.com/looker/docs/creating-ndts) that's based on an Explore  
[`increment_key`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key) |  Added 21.4  Makes the derived table into an [incremental PDT](https://docs.cloud.google.com/looker/docs/incremental-pdts). The `increment_key` specifies the time increment for which fresh data should be queried and appended to the PDT.  
[`increment_offset`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset) |  Added 21.4  Used in conjunction with the `increment_key` parameter for [incremental PDTs.](https://docs.cloud.google.com/looker/docs/incremental-pdts) The `increment_offset` specifies the number of previous time periods (at the increment key's granularity) that are rebuilt to account for late arriving data.  
[`interval_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger) |  Added 21.20  The `interval_trigger` specifies a rebuild schedule for a persistent derived table, in the format `"N (seconds | minutes | hours)"`  
[`materialized_view`](https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view) |  Added 21.10  The statement `materialized_view: yes` creates a materialized view on your database for a derived table.  
[`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes) | Sets the indexes of a PDT built in a traditional database (for example, MySQL, Postgres) or an interleaved sort key in Redshift  
[`partition_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys) |  Specifies that a PDT be partitioned by one or more fields in Presto, or by a single date/time field in BigQuery  
[`persist_for` (for derived_table)](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) | Sets the maximum age of a PDT before it is regenerated  
[`publish_as_db_view`](https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view) | The statement `publish_as_db_view: yes` creates a stable database view for the PDT to enable querying the table outside of Looker  
[`sortkeys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys) | Sets the sort keys of a PDT that is built in Redshift  
[`sql` (for derived_table)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table) | Declares the SQL query for a derived table  
[`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create) | Defines a `SQL CREATE` statement to create a PDT on a database dialect that requires custom DDL commands  
[`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value) | Specifies the condition that causes a PDT to be regenerated  
[`table_compression`](https://docs.cloud.google.com/looker/docs/reference/param-view-table-compression) | Specifies the table compression to use for a PDT in Amazon Athena  
[`table_format`](https://docs.cloud.google.com/looker/docs/reference/param-view-table-format) | Specifies the table format to use for a PDT in Amazon Athena  
Refinement Parameters  
[`view: +view_name`](https://docs.cloud.google.com/looker/docs/lookml-refinements) | Adds a plus sign (`+`) in front of an existing view name to add a refinement to the existing view. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information and use cases.  
[`final`](https://docs.cloud.google.com/looker/docs/lookml-refinements#final) | Indicates that the current refinement is the final refinement allowed for the view. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements#final) documentation page for more information and use cases.  
Parameters to Avoid  
[`distkey`](https://docs.cloud.google.com/looker/docs/reference/param-view-distkey) |  Removed 3.26  Replaced by [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution)  
[`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-view-view-label) |  Avoid 4.4  Replaced by [`label`](https://docs.cloud.google.com/looker/docs/reference/param-view-label)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
