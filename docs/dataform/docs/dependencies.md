---
url: https://docs.cloud.google.com/dataform/docs/dependencies/
title: Set dependencies \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:45.089352+00:00
---

# Set dependencies  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Set dependencies Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to define the relationship between objects in your workflow in Dataform by declaring dependencies.

You can define a dependency relationship between objects of a workflow. In a dependency relationship, the execution of the dependent object depends on the execution of the dependency object. This means that Dataform runs the dependent after the dependency. You define the relationship by declaring dependencies inside the SQLX definition file of the dependent object.

The dependency declarations make up a dependency tree of your workflow that determines the order in which Dataform runs your workflow actions.

You can define the dependency relationship between the following workflow actions:

[Data source declarations](https://docs.cloud.google.com/dataform/docs/declare-source)
    Declarations of BigQuery data sources that let you reference these data sources in Dataform table definitions and SQL operations. You can set a data source declaration as a dependency, but not as a dependent.
[Tables](https://docs.cloud.google.com/dataform/docs/create-tables)
    Tables that you create in Dataform based on the declared data sources or other tables in your workflow. Dataform supports the following table types: table, incremental table, view, and materialized view. You can set a table as a dependency and as a dependent.
[Custom SQL operations](https://docs.cloud.google.com/dataform/docs/custom-sql#create_a_referenceable_output_table)
    SQL statements that Dataform runs in BigQuery as they are, without modification. You can set a custom SQL operation defined in a `type: operations` file as a dependency and as a dependent. To declare a custom SQL operation as a dependency in the `ref` function, you need to [set the `hasOutput` property to `true`](https://docs.cloud.google.com/dataform/docs/custom-sql#create_a_referenceable_output_table) in the custom SQL operation SQLX definition file.
[Assertions](https://docs.cloud.google.com/dataform/docs/assertions)
    Data quality test queries that you can use to test table data. Dataform runs assertions every time it updates your workflow and it alerts you if any assertions fail. You can set an assertion defined in a `type: assertion` file as a dependency and as a dependent by declaring dependencies in the `config` block.

You can define the dependency relationship in the following ways:

  * Declare a dependency by using the Dataform core `ref` function to reference the dependency in a `SELECT` statement.
  * Declare a list of dependencies in the `config` block of a SQLX definition file.



## Before you begin

  1. [Create and initialize a development workspace in your repository](https://docs.cloud.google.com/dataform/docs/create-workspace).
  2. Optional: [Declare a data source](https://docs.cloud.google.com/dataform/docs/declare-source).
  3. Create at least two workflow actions: [tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-table), [assertions](https://docs.cloud.google.com/dataform/docs/assertions), [data source declarations](https://docs.cloud.google.com/dataform/docs/declare-source), or [operations](https://docs.cloud.google.com/dataform/docs/custom-sql).



### Required roles

To get the permissions that you need to declare dependencies for tables, assertions, data source declarations, and custom SQL operations, ask your administrator to grant you the [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) IAM role on workspaces. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Declare a dependency as an argument of the `ref` function

To reference and automatically declare a dependency in a `SELECT` statement, add the dependency as an argument of the `ref` function.

The `ref` function is a Dataform core built-in function that lets you reference and automatically depend on any table, data source declaration, or custom SQL operation with the `hasOutput` property set to `true` in your workflow.

For more information about the `ref` function, see [Dataform core context methods reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#commoncontext).

For more information about using the `ref` function in a table definition, see [About table definitions](https://docs.cloud.google.com/dataform/docs/create-tables#about-table-definitions).

The following code sample shows the `source_data` data source declaration added as an argument of the `ref` function in the `incremental_table.sqlx` SQLX definition file of an incremental table:
    
    
    // filename is incremental_table.sqlx
    
    config { type: "incremental" }
    
    SELECT * FROM ${ref("source_data")}
    

In the preceding code sample, `source_data` is automatically declared a dependency of `incremental_table`.

The following code sample shows `some_table` table definition SQLX file added as an argument of the `ref` function in the `custom_assertion.sqlx` SQLX definition file of an assertion:
    
    
    // filename is custom_assertion.sqlx
    
    config { type: "assertion" }
    
    SELECT
      *
    FROM
      ${ref("some_table")}
    WHERE
      a is null
      or b is null
      or c is null
    

In the preceding code sample, `some_table` is automatically declared a dependency of `custom_assertion`. During execution, Dataform runs `some_table` first, and then runs `custom_assertion` once `some_table` is created.

## Declare dependencies in the `config` block

To declare dependencies that are not referenced in the SQL statement definition of the dependent, but need to be run before the table, assertion, or custom SQL operation, follow these steps:

  1. In your development workspace, in the **Files** pane, expand the `definitions/` directory.
  2. Select the table, assertion, or custom SQL operation SQLX file that you want to edit.
  3. In the `config` block of the file, enter the following code snippet:
         
         dependencies: [ "DEPENDENCY", ]
         

Replace DEPENDENCY with the string target—for example, the filename of the action that you want to add as a dependency. You can enter multiple targets, separated by commas.

  4. Optional: Click **Format**.




The following code sample shows the `some_table` table and `some_assertion` assertion added as dependencies to the `config` block of a table definition file:
    
    
    config { dependencies: [ "some_table", "some_assertion" ] }
    

## Set assertions as dependencies

When workflow action **B** depends on workflow action **A** , which has assertions, the failure of the assertions of action **A** does not block Dataform from executing action **B**. To run action **B** only if the assertions of action **A** pass, you need to set the assertions of action **A** as dependencies of action **B**.

You can set assertions as dependencies of a selected action in the following ways:

Set selected assertions as dependencies
    

You can manually set selected assertions as dependencies by adding them to the `dependencies: [ "" ]` line in the `config` block of the edited action.

For example, if action **B** depends on action **A** , and you want action **B** to depend only on the selected assertions of action **A** , you can add those selected assertions to the `config` block of action **B**.

You can manually set selected assertions as dependencies for all action types except data source declarations.

Set the assertions of a selected dependency action as dependencies
    

You can set the `includeDependentAssertions` parameter to automatically set all the direct assertions of a selected dependency workflow action as dependencies of the edited action. Dataform adds these assertions as dependencies during each compilation of the action to verify that the dependencies are up to date if the assertions of the dependency action change.

For example, if action **C** depends on actions **A** and **B** , but you only want action **C** to depend on the assertions of action **A** , you can edit action **C** and set the `includeDependentAssertions` parameter to automatically set all assertions of action **A** as dependencies of action **C**.

You can set the `includeDependentAssertions` parameter for actions of the following types:

  * `table`
  * `view`
  * `operations`


Set the assertions of all the dependency actions as dependencies
    

You can set the `dependOnDependencyAssertions` parameter to automatically set all the direct assertions from all the dependency actions of the edited action as additional dependencies of the edited action. Dataform adds these assertions as dependencies during each compilation of the action to verify that the dependencies are up to date if the assertions of the dependency action change.

For example, if action **C** depends on actions **A** and **B** , you can edit action **C** and set the `dependOnDependencyAssertions` parameter to automatically set all the assertions of actions **A** and **B** as dependencies of action **C**.

You can set the `dependOnDependencyAssertions` parameter for actions of the following types:

  * `table`
  * `view`
  * `operations`



When you set the `dependOnDependencyAssertions` parameter and the `includeDependentAssertions` parameters in a single file, the `includeDependentAssertions` parameter takes priority. For example, if you set `dependOnDependencyAssertions` to `true`, but you also set `includeDependentAssertions` to `false` for a selected dependency action, Dataform won't add the assertions of that action to the dependencies.

The following code sample shows the `dependOnDependencyAssertions` and `includeDependentAssertions` parameters set in the same table definition file:
    
    
    // filename is tableName.sqlx
    
    config {
    type: "table",
    dependOnDependencyAssertions: true,
    dependencies: [ "actionA", {name: "actionB", includeDependentAssertions: false} ]
    }
    
    SELECT * FROM ${ref("actionC")}
    

In the preceding code sample, Dataform adds all the direct assertions of `actionA` and `actionC` to the dependencies of `tableName` during compilation.

### Set selected assertions as dependencies

To run a workflow action only when selected assertions pass, you can add the selected assertion to the `dependencies: [ "" ]` line in the `config` block of the edited action.

To set a selected assertion as a dependency of a selected workflow action, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.
  2. Select a workflow action SQLX file.
  3. In the `config` block of the action file, enter `dependencies: [ "" ]`.
  4. Inside `dependencies: [ "" ]`, enter the name of the action assertion or the filename of the manual assertion that you want to set as a dependency in one of the following formats: 

### `nonNull`
         
         config {
           type: "ACTION_TYPE",
           dependencies: [ "ACTION_DATASET_NAME_ACTION_NAME_assertions_nonNull"]
         }
         

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * ACTION_DATASET_NAME: the name of the dataset in which the action is defined. The default dataset is [defined in the workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
     * ACTION_NAME: the name of the action in which the assertion is defined.

### `rowConditions`
    
    config {
      type: "ACTION_TYPE",
      dependencies: [ "ACTION_DATASET_NAME_ACTION_NAME_assertions_rowConditions"]
    }
    

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * DATASET_NAME: the name of the dataset in which the action is defined. The default dataset is [defined in the workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
     * ACTION_NAME: the name of the action in which the assertion is defined.

### `uniqueKey`
    
    config {
      type: "ACTION_TYPE",
      dependencies: [ "ACTION_DATASET_NAME_ACTION_NAME_assertions_uniqueKey_INDEX"]
    }
    

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * DATASET_NAME: the name of the dataset in which the table is defined. The default dataset is [defined in the workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
     * ACTION_NAME: the name of the table in which the assertion is defined.
     * INDEX: the index of the array of keys defined in the `uniqueKey` assertion that you want to add as a dependency—for example, `0` or `1`. If only one array of keys is defined in the assertion, the index is `0`.

### `uniqueKeys`
    
    config {
      type: "ACTION_TYPE",
      dependencies: [ "ACTION_DATASET_NAME_ACTION_NAME_assertions_uniqueKeys_INDEX"]
    }
    

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * DATASET_NAME: the name of the dataset in which the table is defined. The default dataset is [defined in the workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
     * ACTION_NAME: the name of the table in which the assertion is defined.
     * INDEX: the index of the array of keys defined in the `uniqueKeys` assertion that you want to add as a dependency—for example, `0` or `1`. If only one array of keys is defined in the assertion, the index is `0`.

### manual assertion
    
    config {
      type: "ACTION_TYPE",
      dependencies: [ "MANUAL_ASSERTION_NAME"]
    }
    

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * MANUAL_ASSERTION_NAME: the name of the manual assertion.

  5. To add another assertion as a dependency to the edited table, repeat Step 4.

  6. Optional: Click **Format**.




The following code sample shows assertions added to table **A** , which is defined in the `dataform` dataset:
    
    
    config {
      type: "table",
      assertions: {
        uniqueKey: ["user_id"],
        nonNull: ["user_id", "customer_id"],
      }
    }
    

The following code sample shows table **A** assertions added as dependencies to table **B** :
    
    
    config {
      type: "table",
      dependencies: [ "dataform_A_assertions_uniqueKey_0",  "dataform_A_assertions_nonNull"]
    }
    

The following code sample shows a manual assertion that's defined in the `manualAssertion.sqlx` file and added as a dependency to a view:
    
    
    config {
      type: "view",
      dependencies: [ "manualAssertion"]
    }
    

The following code sample shows the `manual_assertion` file and the assertions of the `sometable` table added as dependencies to a table:
    
    
    config {
      type: "table",
      dependencies: [ "manual_assertion",  "dataform_sometable_assertions_nonNull" ,  "dataform_sometable_assertions_rowConditions"]
    }
    
    SELECT * FROM ${ref("referenced_table")} LEFT JOIN ...
    

### Set the assertions of a selected action as dependencies

To run a workflow action only when all the direct assertions of a selected dependency action pass, set the `includeDependentAssertions` parameter to `true` in the edited action. Dataform automatically adds the direct assertions of the selected dependency action to the dependencies during compilation. The default value is `false`.

To set all the assertions of a selected dependency action as dependencies, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.
  2. Select a workflow action SQLX file.
  3. In the file, set the `includeDependentAssertions` parameter to `true` in one of the following ways:

### In the `config` block
         
         config {
         type: "ACTION_TYPE",
         dependencies: [{name: "dEPENDENCY_ACTION_NAME", includeDependentAssertions: true}]
         }
         

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * DEPENDENCY_ACTION_NAME: the name of the dependency action with the assertions that you want to set as dependencies of the edited action.

### In the `SELECT` statement
    
    config { type: "ACTION_TYPE" }
    
      SELECT * FROM ${ref({name: "DEPENDENCY_ACTION_NAME", includeDependentAssertions: true})}
    

Replace the following:

     * ACTION_TYPE: the type of workflow action: `table`, `view`, or `operations`.
     * DEPENDENCY_ACTION_NAME: the name of the dependency action with the assertions that you want to set as dependencies of the edited action.

  4. Optional: Click **Format**.




The following code sample shows `tableC`, which depends on `viewA`, `tableB`, and all the assertions of `tableB`:
    
    
    // filename is tableC.sqlx
    
    config {
    type: "table",
    dependencies: ["viewA", {name: "tableB", includeDependentAssertions: true}]
    }
    
    SELECT * FROM ...
    

In the preceding code sample, Dataform automatically adds all the direct assertions of `tableB` as dependencies to `tableC` during compilation.

### Set the assertions of all the dependency actions as dependencies

To run a workflow action only when all the direct assertions of all the dependency actions pass, set the `dependOnDependencyAssertions` parameter to `true` in the edited action. Dataform automatically adds the direct assertions of the dependency actions as dependencies during compilation. The default value is `false`.

When you set the `dependOnDependencyAssertions` parameter and the `includeDependentAssertions` parameters in a single file, the `includeDependentAssertions` parameter takes priority for the dependency action for which it is set.

To set all the assertions of a selected dependency action as dependencies, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.
  2. Select a workflow action SQLX file.
  3. In the file, set the `dependOnDependencyAssertions` parameter to `true` in the following format:
         
         config {
         type: "ACTION_TYPE",
         dependOnDependencyAssertions: true,
         dependencies: [ "dependency1", "dependency2" ]
         }
         

Replace ACTION_TYPE: the type of workflow action. Supported values include `table`, `view`, and `operations`.

  4. Optional: Click **Format**.




The following code sample shows `sometableE`, which depends on `sometableA`, `sometableB`, `sometableC`, `sometableD`, and all the direct assertions of the dependency tables:
    
    
    // filename is sometableE.sqlx
    
    config {
    type: "table",
    dependOnDependencyAssertions: true,
    dependencies: [ "sometableA", "sometableB" ]
    }
    
    SELECT * FROM ${ref("sometableC")}
    SELECT * FROM ${ref("sometableD")}
    

In the preceding code sample, Dataform automatically adds all the direct assertions of `sometableA`, `sometableB`, `sometableC`, and `sometableD` as dependencies to `sometableE` during compilation.

## Reference a table with an overridden table name

  * To reference a table with an overridden table name, in the `ref` function, enter the overridden table name that's set in `name: ""`.



The following code sample references a table with a name overridden to `overridden_name`:
    
    
      SELECT * FROM ${ref("overridden_name")}
    

For more information about overriding table names, see [Override table settings](https://docs.cloud.google.com/dataform/docs/create-tables#override-table-settings).

## What's next

  * To learn how to set assertions as dependencies, see [Test data quality](https://docs.cloud.google.com/dataform/docs/assertions).
  * To learn how to declare a data source, see [Declare a data source](https://docs.cloud.google.com/dataform/docs/declare-source).
  * To learn how to define custom SQL operations, see [Create operations](https://docs.cloud.google.com/dataform/docs/custom-sql).
  * To learn how to reuse code across your workflow with includes, see [Reuse code across a single repository with includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
