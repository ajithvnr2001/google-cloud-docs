---
url: https://docs.cloud.google.com/dataform/docs/assertions/
title: Test data quality \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:01.395288+00:00
---

# Test data quality  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/assertions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Test data quality Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to test your workflow code with Dataform table assertions and unit tests. 

## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. [Create a table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).




### Required roles

To get the permissions that you need to create assertions and unit tests, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on the workspace
  * To synchronize assertion metadata to Knowledge Catalog: [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project or `@bigquery` entry group 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Test data with assertions

An assertion is a data quality test query that finds rows that violate one or more conditions specified in the query. If the query returns any rows, the assertion fails. Dataform runs assertions every time it updates your workflow and it alerts you if any assertions fail.

Dataform automatically creates views in BigQuery that contain the results of compiled assertion queries. As [configured in your workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings), Dataform creates these views in an assertions schema where you can inspect assertion results.

For example, for the default `dataform_assertions` schema, Dataform creates a view in BigQuery in the following format: `dataform_assertions.assertion_name`.

You can create assertions for all Dataform table types: tables, incremental tables, views, and materialized views.

You can create assertions in the following ways:

  * Add built-in assertions to the config block of a table.

You can add built-in assertions to the `config` block of a table and specify their conditions.

  * Add manual assertions in a separate SQLX file.

You manually write custom assertions in a separate SQLX file for advanced use cases or for datasets not created by Dataform.


**Note:** Dataform assertions are automatically integrated with the [Knowledge Catalog data quality scorecard](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#data-quality-scorecard). During pipeline execution, the results of any Dataform assertions are automatically published to Knowledge Catalog. These results populate the Knowledge Catalog data quality scorecard with a pass or fail status. Each execution overwrites existing data quality scorecards published by prior Dataform runs, but doesn't affect scorecards created by Knowledge Catalog data scans. To check the status of a metadata update, follow the instructions in [Inspect workspace execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#inspect-workspace-execution-logs). To view these results in Knowledge Catalog, follow the instructions in [Search for resources](https://docs.cloud.google.com/dataplex/docs/search-assets#search-data-assets).

### Create built-in assertions

You can add built-in Dataform assertions to the `config` block of a table. Dataform runs these assertions after table creation. After Dataform creates the table, you can see if the assertion passed in the **Workflow execution logs** tab of your workspace.

You can create the following assertions in the `config` block of a table:

  * `nonNull`

This condition asserts that the specified columns are not null across all table rows. This condition is used for columns that can never be null.

The following code sample shows a `nonNull` assertion in the `config` block of a table:



    
    
    config {
      type: "table",
      assertions: {
        nonNull: ["user_id", "customer_id", "email"]
      }
    }
    SELECT ...
    

  * `rowConditions`

This condition asserts that all table rows follow the custom logic you define. Each row condition is a custom SQL expression, and each table row is evaluated against each row condition. The assertion fails if any table row results in `false`.

The following code sample shows a custom `rowConditions` assertion in the `config` block of an incremental table:



    
    
    config {
      type: "incremental",
      assertions: {
        rowConditions: [
          'signup_date is null or signup_date > "2022-08-01"',
          'email like "%@%.%"'
        ]
      }
    }
    SELECT ...
    

  * `uniqueKey`

This condition asserts that, in a specified column, no table rows have the same value.

The following code sample shows a `uniqueKey` assertion in the `config` block of a view:



    
    
    config {
      type: "view",
      assertions: {
        uniqueKey: ["user_id"]
      }
    }
    SELECT ...
    

  * `uniqueKeys`

This condition asserts that, in the specified columns, no table rows have the same value. The assertion fails if there is more than one row in the table with the same values for all the specified columns.

The following code sample shows a `uniqueKeys` assertion in the `config` block of a table:



    
    
    config {
      type: "table",
      assertions: {
        uniqueKeys: [["user_id"], ["signup_date", "customer_id"]]
      }
    }
    SELECT ...
    

#### Add assertions to the `config` block

To add assertions to the config block of a table, follow these steps:

  1. In your development workspace, in the **Files** pane, select a table definition SQLX file.
  2. In the `config` block of the table file, enter `assertions: {}`.
  3. Inside `assertions: {}`, add your assertions.
  4. Optional: Click **Format**.



The following code sample shows the conditions added in the `config` block:
    
    
    config {
      type: "table",
      assertions: {
        uniqueKey: ["user_id"],
        nonNull: ["user_id", "customer_id"],
        rowConditions: [
          'signup_date is null or signup_date > "2019-01-01"',
          'email like "%@%.%"'
        ]
      }
    }
    SELECT ...
    

### Create manual assertions with SQLX

Manual assertions are SQL queries that you write in a dedicated SQLX file. A manual assertion SQL query must return zero rows. If the query returns rows when it's run, the assertion fails.

To add manual assertions in a new SQLX file, follow these steps:

  1. In the **Files** pane, next to `definitions/`, click the ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**More** menu.
  2. Click **Create file**.
  3. In the **Add a file path** field, enter the name of the file followed by `.sqlx`. For example, `definitions/custom_assertion.sqlx`.

Filenames can only include numbers, letters, hyphens, and underscores.

  4. Click **Create file**.

  5. In the **Files** pane, click the new file.

  6. In the file, enter:
         
         config {
           type: "assertion"
         }
         

  7. Below the `config` block, write your SQL query or multiple queries.

  8. Optional: Click **Format**.




The following code sample shows a manual assertion in a SQLX file that asserts that fields **A** , **B** , and `c` are never `NULL` in `sometable`:
    
    
    config { type: "assertion" }
    
    SELECT
      *
    FROM
      ${ref("sometable")}
    WHERE
      a IS NULL
      OR b IS NULL
      OR c IS NULL
    

## Test data quality with unit tests

A unit test is a data quality test, defined in a dedicated `.sqlx` file, that mocks all dependencies of the tested workflow action and provides expected results. You can use unit tests to test Dataform actions against controlled mock inputs to verify if the action code handles edge cases, null values, aggregations, regular expressions, and conditional logic correctly.

Mocks for action dependencies, such as predecessor tables, views, or raw declarations referenced in the `${ref()}` function, are defined in `input` blocks. Each `input` block references a dependency by its name and contains a SQL query that defines the mock rows. This query is typically a series of `SELECT` statements combined with `UNION ALL`. Expected results are SQL queries that represent the results of running the specified inputs over the workflow action SQL statement.

Dataform runs unit tests row by row and compares the actual result of running a workflow action's SQL logic against mock data with an expected result set.

Unit tests resolve to the following states:

  * `SUCCESS`: The test passed. Actual results match the expected results.
  * `FAILURE`: The test failed. Actual results don't match the expected results.



### Limitations

Dataform unit tests are available with the following limitations:

  * Unit tests are available with Dataform core version `3.0.56` and later.
  * The maximum size of input data in a unit test is 100 rows per input.



### Create unit tests

Store `.sqlx` files for unit tests in the `definitions/` directory. To create a new unit test `.sqlx` file in the `definitions/` directory, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository.

  3. Select a development workspace.

  4. In the **Files** pane, next to `definitions/`, click the **More** menu.

  5. Click **Create file**.

  6. In the **Create new file** pane, do the following:

     1. In the **Add a file path** field, after `definitions/`, enter the name of the file followed by `_test.sqlx`. For example, `definitions/customer_spend_test.sqlx`.

Filenames can only include numbers, letters, hyphens, and underscores.

     2. Click **Create file**.

  7. In the test file, add the following `config` block:
         
         config {
           type: "test",
           dataset: "ACTION_NAME"
         }
         

Replace ACTION_NAME with the name of the action that this test validates.

  8. To mock the tested action, add an `input` block for each action dependency, and write a SQL query testing that dependency in the following format:
         
         input "DEPENDENCY_NAME" {
         SELECT ...
         SELECT ...
         }
         

Replace DEPENDENCY_NAME with the name of the tested action dependency that this input mocks.

  9. Below the `input` blocks, write standard SQL queries representing the expected output rows in the following format:
         
         -- Expected Output
         SELECT ...
         SELECT ...
         




The expected output queries should only return the rows and columns that the tested action is supposed to produce given the mock inputs.

The following code sample shows the `customer_spend.sqlx` workflow action:
    
    
    config {
    type: "table",
    name: "customer_spend"
    }
    
    SELECT
      c.customer_id,
      c.name,
      SUM(o.amount) AS total_completed_amount
    FROM
      ${ref("source_customers")} c
      JOIN
      ${ref("source_orders")} o
      ON c.customer_id = o.customer_id
    WHERE
      o.status = 'COMPLETED'
    GROUP BY
      1, 2
    

The following code sample shows the `customer_spend_test.sqlx` unit test that mocks dependencies of the `customer_spend.sqlx` action, and defines expected results for the mocks:
    
    
    config {
      type: "test",
      dataset: "customer_spend"
    }
    
    input "source_customers" {
      SELECT 101 AS customer_id, 'Alice' AS name UNION ALL
      SELECT 102 AS customer_id, 'Bob' AS name UNION ALL
      SELECT 103 AS customer_id, 'Charlie' AS name
    }
    
    input "source_orders" {
      -- Alice has one completed and one pending order
      SELECT 1 AS order_id, 101 AS customer_id, 'COMPLETED' AS status, 100.0 AS amount UNION ALL
      SELECT 2 AS order_id, 101 AS customer_id, 'PENDING' AS status, 50.0 AS amount UNION ALL
      -- Bob has one completed order
      SELECT 3 AS order_id, 102 AS customer_id, 'COMPLETED' AS status, 250.0 AS amount UNION ALL
      -- Charlie has no orders
      SELECT 4 AS order_id, 999 AS customer_id, 'COMPLETED' AS status, 10.0 AS amount
    }
    
    -- Expected Output
    SELECT 101 AS customer_id, 'Alice' AS name, 100.0 AS total_completed_amount UNION ALL
    SELECT 102 AS customer_id, 'Bob' AS name, 250.0 AS total_completed_amount
    

### Run unit tests

To run unit tests, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository.

  3. Select a development workspace.

  4. Click **Start execution** > **Execute actions**.

  5. In the **Execute** panel, in the **Execution mode** section, select **Unit tests**.

  6. Select one of the following options:

     * **Select unit tests** : runs unit tests that you manually select.
     * **Select tagged unit tests** : runs unit tests with a selected tag.
     * **All unit tests** : runs all unit tests in the workspace.
  7. Optional: In the **Execution options** sections, select the **Execute as interactive job with high priority** checkbox to run unit tests immediately, prioritizing execution speed.

If you don't select the **Execute as interactive job with high priority** checkbox, Dataform runs unit tests using batch resources by default, prioritizing compute costs savings.

  8. Click **Start execution**.




###  API 

To run unit tests programmatically, create a workflow invocation by using the [`WorkflowInvocations.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create) method, and set the following unit testing execution parameters in the `invocationConfig` object:

`"executionMode": "UNIT_TESTS_ONLY"`
    This parameter, set to `"UNIT_TESTS_ONLY"`, triggers execution of unit tests defined in the repository.
Optional: `"queryPriority": "INTERACTIVE"`
    When this parameter is set to `"INTERACTIVE"`, Dataform runs queries immediately. If unset, Dataform runs unit tests with the default batch query priority.
Optional: `"includedTargets": []`
    This parameter lets you specify unit tests so that Dataform runs only these tests.
Optional: `"includedTags": []`
    This parameter lets you specify tags so that Dataform runs only the unit tests tagged with those tags.

The following code sample shows the body of a workflow invocation that runs all unit tests defined in the `my-repo` repository with the default batch query priority:
    
    
    {
      "compilationResult": "projects/my-project/locations/us/repositories/my-repo/compilationResults/my-compilation-id",
      "invocationConfig": {
        "executionMode": "UNIT_TESTS_ONLY"
      }
    }
    

The following code sample shows the body of a workflow invocation that runs only the `my-test` unit test with the interactive query priority:
    
    
    {
      "compilationResult": "projects/my-project/locations/us/repositories/my-repo/compilationResults/my-compilation-id",
      "invocationConfig": {
        "executionMode": "UNIT_TESTS_ONLY",
        "queryPriority": "INTERACTIVE",
        "includedTargets": [
          {
            "database": "my-project",
            "schema": "my-dataset",
            "name": "my-test"
          }
        ]
      }
    }
    

The following code sample shows the body of a workflow invocation that runs unit tests in the `my-repo` repository that are tagged with `test-tag-1` or `test-tag-2`:
    
    
    {
      "compilationResult": "projects/my-project/locations/us/repositories/my-repo/compilationResults/my-compilation-id",
      "invocationConfig": {
        "executionMode": "UNIT_TESTS_ONLY",
        "queryPriority": "INTERACTIVE",
        "includedTags": [
          "test-tag-1",
          "test-tag-2"
        ]
      }
    }
    

### Inspect unit test results

You can inspect the differences between the expected and actual scripts of a unit test in the **Compiled graph** or in **Executions**.

###  Compiled graph 

To view the actual and expected scripts of a unit test in the compiled graph of workflow actions, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository.

  3. Select a development workspace.

  4. Optional: To view unit tests linked to the actions they test, instead of viewing them as independent graph nodes, set the `includeTestsInCompiledGraph` setting to `true` in the `workflow_settings.yaml` file:

     1. Select the `workflow_settings.yaml` file.
     2. Add the following code:
    
    includeTestsInCompiledGraph: true
    

  5. Click **Compiled graph**.

  6. In the compiled graph, select a unit test, and then click **Query**.

  7. Compare the **Actual SQL Script** , and the **Expected SQL Script**.




###  Executions 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository.

  3. Select a development workspace.

  4. Click **Executions** , and then click **View details** next to the selected unit test.

  5. Compare the **Actual results query** and the **Expected results query**.




### Best practices for unit tests

Keep mock datasets small
    Keep mock input data under 10 rows for faster compilation and easier debugging.
Specify an explicit row order
    Always add an `ORDER BY` clause to both your action query and your expected output query to ensure deterministic row ordering during evaluation.
Explicitly cast columns in your mock statements
    Explicitly casting columns in your mock statements—for example, by using `CAST(100 AS INT64)`—maintains type strictness and prevents compilation errors.
Include test cases with `NULL` or missing values
    Including test cases with `NULL` or missing values in your input mock queries ensures that your `COALESCE` statements, string operations, and filter criteria safely handle incomplete or null production data.

The following code sample shows a `NULL` test case:
    
    
    input "source_customers" {
      SELECT 101 AS customer_id, 'Alice' AS name UNION ALL
      SELECT 102 AS customer_id, NULL AS name -- Test null handling
    }
    
    

## What's next

  * To learn more about assertion types, see [Dataform API](https://docs.cloud.google.com/dataform/reference/rest).
  * To learn how to define assertions with JavaScript, see [Create workflows exclusively with JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#create-workflows-with-javascript).
  * To learn how to manually run workflows, see [Manually trigger runs](https://docs.cloud.google.com/dataform/docs/trigger-execution).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
