---
url: https://docs.cloud.google.com/dataform/docs/javascript-in-dataform/
title: Use JavaScript in Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:41.636952+00:00
---

# Use JavaScript in Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/javascript-in-dataform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Use JavaScript in Dataform Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand how you can use JavaScript to develop workflows in Dataform. This document also shows you how to use JavaScript to create workflow actions and how to create JavaScript includes to reuse code in Dataform. 

[Dataform core](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference) lets you create workflow actions with SQLX and JavaScript. While optional, using JavaScript along with SQLX to create similar elements repeatedly in your workflow. For example, with JavaScript you can create a view of each table in your workflow with certain user IDs removed. You can also develop workflow actions exclusively with JavaScript.

## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).




Additionally, you must be familiar with [JavaScript syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and the following JavaScript concepts:

  * Variables
  * Arrays
  * Conditional statements
  * For loops
  * Maps
  * Functions
  * Objects
  * Exporting and importing modules



### Required roles

To get the permissions that you need to develop a workflow with JavaScript and reuse code with JavaScript includes, ask your administrator to grant you the [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) IAM role on workspaces. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add JavaScript code to a SQLX file

You can add JavaScript code to a SQLX file in two ways: inline or inside a JavaScript block.

You can use a JavaScript block to define functions or constants in a SQLX file. You can use inline JavaScript to dynamically modify a SQLX or SQL query.

The following code sample shows the `self` Dataform core built-in JavaScript function added inline to the `post_operations` block in a SQLX file:
    
    
    config {type: "table"}
    
    SELECT * FROM ...
    
    post_operations {
      GRANT `roles/bigquery.dataViewer`
      ON
      TABLE ${self()}
      TO "group:allusers@example.com", "user:otheruser@example.com"
    }
    

The following code sample shows a constant defined in a JavaScript block and used inline inside a query in a SQLX file:
    
    
    js {
      const columnName = "foo";
    }
    
    SELECT 1 AS ${columnName} FROM "..."
    

## Reuse code across a single SQLX file with JavaScript encapsulation

You can reuse JavaScript code to streamline development in Dataform. To reuse JavaScript constants and functions across a single SQLX file, you can encapsulate them in a JavaScript block. To reuse JavaScript code across a single Dataform repository, you can create includes. To reuse JavaScript code across multiple Dataform repositories, you can create or import a package.

To create repetitive parts of SQL code that you can reuse within a single SQLX file, you can encapsulate functions and constants in a JavaScript block. You can reuse code defined in a JavaScript block only inside the SQLX file where the block is defined. For more information, see [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core).

The following code sample shows a constant and function defined in a JavaScript block and used inline inside a query in a SQLX file:
    
    
    js {
     const foo = 1;
     function bar(number){
         return number+1;
     }
    }
    
    select
     ${foo} as one,
     ${bar(foo)} as two
    

## Reuse code across a single repository with includes

Includes are JavaScript constants or functions global to your repository. You define includes in the `includes` directory of your repository. You can then reuse them across your repository in JavaScript and SQLX files.

The following code sample shows the definition of the `launch_date` constant in the `includes/constants.js` file:
    
    
    // filename is includes/constants.js
    const launch_date = "11.11.2011";
    module.exports = { launch_date };
    

The following code sample shows the `launch_date` constant referenced in a table definition query in a SQLX file:
    
    
    config {type: "table"}
    
    SELECT * FROM source_table WHERE date > ${constants.launch_date}
    

### Create a JavaScript file for includes

To create a new JavaScript file in the `includes/` directory, follow these steps:

  1. In the **Files** pane, next to `includes/`, click more_vert **More**.

  2. Click **Create file**.

  3. In the **Create new file** pane, do the following:

     1. In the **Add a file path** field, after `includes/`, enter the name of the file followed by `.js`. For example, `includes/constants.js`.

Filenames can only include numbers, letters, hyphens, and underscores.

     2. Click **Create file**.




### Create a JavaScript constant

To create a constant that you can reuse across your project, follow these steps:

  1. Go to your development workspace.

  2. In the **Files** pane, expand `includes/`.

  3. Create or select a JavaScript file with the `.js` extension.

  4. In the file, enter the following code snippet:
         
         const CONSTANT_NAME = CONSTANT_VALUE;
          module.exports = { CONSTANT_NAME };
         

Replace the following:

     * CONSTANT_NAME: the name of your constant
     * CONSTANT_VALUE: the value of your constant
  5. Optional: Click **Format**.




The following code sample defines the `PROJECT_ID` constant in the `includes/constants.js` file:
    
    
      // filename is includes/constants.js
      const PROJECT_ID = "my_project_name";
      module.exports = { PROJECT_ID };
    

The following code sample references the `PROJECT_ID` constant in a table definition query in a SQLX file:
    
    
      config { type: "table" }
      SELECT * FROM ${constants.PROJECT_ID}.my_schema_name.my_table_name
    

The following code sample shows the previous Dataform core table definition query compiled into SQL:
    
    
      SELECT * FROM my_project_name.my_schema_name.my_table_name
    

### Create a custom JavaScript function

To create a custom JavaScript function that you can reuse across your project, follow these steps:

  1. Go to your development workspace.

  2. In the **Files** pane, expand `includes/`.

  3. Create or select a JavaScript file with the `.js` extension.

  4. In the file, write your custom JavaScript function.

  5. In the file, enter the following code snippet:
         
         module.exports = { FUNCTION_NAME }
         

Replace `FUNCTION_NAME` with the name of your function.

  6. Optional: Click **Format**.




The following code sample shows a custom JavaScript function that is called `renderScript` and stored in the `includes/functions.js` file. The function generates a SQL script:
    
    
      function renderScript(table, dimensions, metrics) {
        return `
            select
            ${dimensions.map(field => `${field} as ${field}`).join(",")},
            ${metrics.map(field => `sum(${field}) as ${field}`).join(",\n")}
            from ${table}
            group by ${dimensions.map((field, i) => `${i + 1}`).join(", ")}
          `;
      }
    
      module.exports = { renderScript };
    

The following code sample shows the use of the custom `renderScript` JavaScript function in a Dataform core table definition query:
    
    
      config {
          type: "table",
          tags: ["advanced", "hourly"],
          disabled: true
      }
    
      ${functions.renderScript(ref("source_table"),
                                    ["country", "device_type"],
                                    ["revenue", "pageviews", "sessions"]
                                    )}
    

The following code sample shows the previous Dataform core table definition query compiled into SQL:
    
    
      select
        country as country,
        device_type as device_type,
        sum(revenue) as revenue,
        sum(pageviews) as pageviews,
        sum(sessions) as sessions
    
      from "dataform"."source_table"
    
      group by 1, 2
    

### Reference an include in a SQLX file

You can reference any include function or constant inside a SQLX file. The syntax for referencing includes depends on the location of the include file. A top-level includes file is located directly in the `includes/` directory. A nested includes file is located in a subdirectory of `includes/`.

#### Reference a top-level include in a SQLX file

  * To reference a top-level include function or constant in a Dataform core query, enter the include definition filename without the `.js` extension followed by the name of the exported object.



The following code sample references the `firstDate` constant, defined in the `includes/constants.js` file, in a table definition SQLX file:
    
    
      config {type: "table"}
      select * from source_table where date > ${constants.firstDate}
    

#### Reference a nested include in a SQLX file

To reference includes located in subdirectories of `definitions`, import includes by using the JavaScript `require` function and a `js {}` block.

To reference a nested include with the `require` JavaScript function, follow these steps:

  1. Go to your development workspace.

  2. In the **Files** pane, expand `definitions/`.

  3. Select a SQLX file.

  4. In the `config` block, enter the following code snippet:
         
         js {
            var { VARIABLE_NAME } = require("SUBDIRECTORY_INCLUDE");
          }
         

Replace the following:

     * VARIABLE_NAME: the name of the constant or function that you want to import
     * SUBDIRECTORY_INCLUDE: the path of the nested `includes` file
  5. Optional: Click **Format**.




The following code sample references the `firstDate` constant, defined in the nested `includes/allConstants/constants.js` file, in a table definition SQLX file:
    
    
      config {type: "table"}
      js {
        var { firstDate } = require("includes/allConstants/constants");
      }
      select * from source_table where date > ${firstDate}
    

#### Use a JavaScript include function with the Dataform core `ref` function

To use a JavaScript include function with the Dataform core `ref` function, you need to pass `ref` as an argument of the JavaScript include function inside a SQLX file.

The following code sample shows the `includes/script_builder.js` file with the `renderScript` JavaScript function that aggregates metrics by using `SUM` and groups them by dimension:
    
    
    function renderScript(table, dimensions, metrics) {
      return `
          SELECT
          ${dimensions.map((field) => `${field} AS ${field}`).join(",\\n")},
          ${metrics.map((field) => `SUM(${field}) AS ${field}`).join(",\\n")}
          FROM ${table}
          GROUP BY ${dimensions.map((field, i) => `${i + 1}`).join(", ")}
        `;
    }
    module.exports = { renderScript };
    

The following code sample shows the `renderScript` JavaScript function used in the `definitions/stats_per_country_and_device.sqlx` file with the Dataform core `ref` function passed as an argument:
    
    
    ${script_builder.renderScript(
      ref("source_table"),
      ["country", "device_type"],
      ["revenue", "pageviews", "sessions"])}
    

The following code sample shows the `definitions/stats_per_country_and_device.sqlx` query compiled to SQL:
    
    
    SELECT country AS country,
           device_type AS device_type,
           SUM(revenue) AS revenue,
           SUM(pageviews) AS pageviews,
           SUM(sessions) AS sessions
    FROM my_schema.source_table
    GROUP BY 1, 2
    

For more information about the Dataform core `ref` function, see [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core).

## Reuse code across multiple repositories with packages

Packages are collections of JavaScript code that you can import and use across multiple Dataform repositories to streamline workflow development.

You can [create your own custom package](https://docs.cloud.google.com/dataform/docs/create-package) in Dataform or use one of the open-source Dataform packages, available on the [GitHub open-source Dataform page](https://github.com/dataform-co).

To be able to use the contents of a package in Dataform, you need to install the package in your Dataform repository, and then import it to the individual JavaScript or SQLX file in which you want to use the package. For more information, see [Install a package](https://docs.cloud.google.com/dataform/docs/use-packages#install-package).

To be able to install a private NPM package in a Dataform repository, you need to [authenticate the package](https://docs.cloud.google.com/dataform/docs/use-packages#authenticate-private-package).

## Create workflows exclusively with JavaScript

This section shows you how to use JavaScript to create workflow actions in Dataform. You might want to use JavaScript instead of Dataform core to create similar elements repeatedly in your workflow.

As an alternative to developing workflows in SQLX, or SQLX combined with JavaScript, you can create workflow actions in `.js` files by using only JavaScript. You can create multiple workflow actions within one JavaScript file with Dataform global methods and arbitrary JavaScript ES5 code, such as loops and constants. Each of the Dataform global JavaScript methods contain properties you can use to configure the created objects.

You can create the following workflow actions by using only JavaScript in Dataform:

  * Data source declarations
  * Tables
  * Manual assertions
  * Custom SQL operations



With JavaScript, you can create similar actions repeatedly in your workflow. For example, you can create a view of each table in your workflow with certain user IDs removed.

The following JavaScript code sample lets you create a view of each table where the value of the `user_id` field does not correspond to one of the values in the `blocked_user_ids` list:
    
    
      const tableNames = ["user_events", "user_settings", "user_logs"];
    
      tableNames.forEach(tableName => {
        publish(tableName + "_blocked_removed").query(
          ctx => `
            SELECT * FROM ${ctx.ref(tableName)}
            WHERE user_id NOT IN (
              SELECT user_id
              FROM ${ctx.ref("blocked_user_ids")}
            )`
        );
      });
    

This code sample creates three views named `user_events_blocked_removed`, `user_settings_blocked_removed`, and `user_logs_blocked_removed` that don't contain any of the blocked user IDs.

You can create multiple actions within one JavaScript file with Dataform global methods and arbitrary JavaScript ES5 code, such as loops and constants.

You can define the following actions with JavaScript in Dataform:

  * Tables
  * Data source declarations
  * Assertions
  * Custom SQL operations



### Create a JavaScript file

Store JavaScript files for definitions and data source declarations in the `definitions/` directory. To create a new JavaScript file in the `definitions/` directory, follow these steps:

  1. In the **Files** pane, next to `definitions/`, click more_vert **More**.

  2. Click **Create file**.

  3. In the **Create new file** pane, do the following:

     1. In the **Add a file path** field, after `definitions/`, enter the name of the file followed by `.js`. For example, `definitions/definitions.js`.

Filenames can only include numbers, letters, hyphens, and underscores.

     2. Click **Create file**.




### Set workflow action properties with JavaScript

You can use the following Dataform global methods to create SQL workflow actions with Dataform:

  * [`declare`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#declare). Used to declare a data source.
  * [`publish`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#publish). Used to define a table.
  * [`assert`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#assert). Used to create an assertion.
  * [`operate`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#operate). Used to define a custom SQL operation.



Each of the global methods contain properties you can use to configure the created object. For more information on global methods and their properties, see the [Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference).

In the `publish()` method that creates a table, you can set table properties by passing them as the second method argument.

To pass table properties as the second argument of `publish()`, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, add table properties to the `publish()` method in the following format:
         
         method("first_method_argument", {
            property1: "property1_value",
            property2: "property2_value",
            property3: "property3_value",
          });
         

  4. Optional: Click **Format**.




The following code sample shows how to set properties to the `publish()` method by passing the properties as a second argument of the method:
    
    
      publish("table1", {
        type: "table",
        dependencies: ["other_table"],
        description: {
          "Value is 1"
        }
      }).query(ctx => "SELECT 1 AS test");
    

### Reference includes in a JavaScript file

You can reference any includes function, macro, or constant inside a JavaScript file. For more information on includes in Dataform, see the Reuse code across a single repository with includes section of this document.

The syntax for referencing includes inside a JavaScript file depends on the location of the include file. Dataform stores such files in the includes directory.

#### Reference top-level includes

  * To reference a top-level includes file, reference the filename when declaring your variables.



The following code sample references the `serviceName` and `serviceId` variables from the `includes/service.js` file:
    
    
      const {serviceName, serviceId} = service;
    

#### Reference nested includes

To reference a nested includes file, enter the filename in the JavaScript require function.

The following code sample references the `serviceName` and `serviceId` variables from the `includes/allServices/service.js` file:
    
    
      const {serviceName, serviceId} = require("includes/allServices/service.js");
    

### Use Dataform query functions in JavaScript methods

Dataform provides a number of built-in functions that you can use inside queries, such as `ref` and `self`. For more information on Dataform built-in functions, see the [Dataform API reference](https://docs.cloud.google.com/dataform/reference/rest).

To use a built-in query function in a JavaScript method, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, enter a global Dataform JavaScript method.

  4. In the method, enter a contextable `ctx` argument.

  5. Optional: If you are using JavaScript template strings, wrap the contextable argument in backticks ````.

  6. In the contextable argument, enter the query function with its parameter as a context object.

  7. Optional: Click **Format**.




The following code sample shows the `ref` query function wrapped inside a contextable argument of the publish method:
    
    
      publish("example").query(ctx => `SELECT * FROM ${ctx.ref("other_table")}`);
    

### Declare a workflow data source with JavaScript

You can declare multiple data sources in one JavaScript declaration file with the Dataform declare JavaScript method. For more information on the declare method, see the [Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference). For more information on data sources in Dataform, see [Declare a data source](https://docs.cloud.google.com/dataform/docs/declare-source).

To declare a data source in a JavaScript file, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, enter the following code snippet:
         
         declare({
            database: "DATABASE_PROJECT_ID",
            schema: "BIGQUERY_SCHEMA",
            name: "RELATION_NAME",
          });
         

Replace the following:

     * `DATABASE_PROJECT_ID`: the project ID of the project which contains the data source
     * `BIGQUERY_SCHEMA`: the BigQuery dataset in which the external relation exists
     * `RELATION_NAME`: the name of the relation that you can later use to reference the data source in Dataform
  4. To declare another data source in the same file, add an extra `declare` block to the file.

  5. Optional: Click **Format**.




### Define a table with JavaScript

You can create a table with the Dataform JavaScript `publish` method. For more information on the publish method, see the [Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference).

You can define the following table types:

  * Table
  * Incremental table
  * View



For more information on defining tables in Dataform, see [Create tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).

To define a table in a JavaScript file, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, enter the following code snippet:
         
         publish("TABLE_NAME").query(ctx => "SELECT_QUERY");
         

Replace the following:

     * `TABLE_NAME`: the name of the table
     * `SELECT_QUERY`: a SQL SELECT statement defining the table
  4. To set the table type, add table dependencies, and add table description, set object properties of the `publish` method.

  5. To define another table in the same file, repeat step 3 and step 4.

  6. Optional: Click **Format**.




### Define manual assertions with JavaScript

You can create manual SQL assertions in a JavaScript file with the Dataform assert JavaScript method. For more information on the assert method, see the [Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference).

A manual assertion SQL query must return zero rows. If the query returns rows when run, the assertion fails. You can create multiple assertions in one JavaScript file.

For more information on assertions in Dataform, see [Test data quality](https://docs.cloud.google.com/dataform/docs/assertions).

To create a manual assertion in a JavaScript file, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, enter the following code snippet:
         
         assert("ASSERTION_NAME").query(ctx => "CUSTOM_ASSERTION_QUERY");
         

Replace the following:

     * `ASSERTION_NAME`: the name for your custom assertion
     * `CUSTOM_ASSERTION_QUERY`: your SQL assertion query
  4. To create another assertion in the same file, repeat step 3.

  5. Optional: Click **Format**.




The following code sample shows a JavaScript assertion that asserts that no value in `source_table` is `NULL`:
    
    
      assert("assertion1").query(ctx => "SELECT * FROM source_table WHERE value IS NULL");
    

### Define custom SQL operations with JavaScript

You can define custom SQL operations in a JavaScript file with the Dataform operate JavaScript method. For more information on custom SQL operations in Dataform, see [Create operations](https://docs.cloud.google.com/dataform/docs/custom-sql).

To define a custom SQL operation with JavaScript, follow these steps:

  1. In your development workspace, in the **Files** pane, expand `definitions/`.

  2. Select a JavaScript file.

  3. In the file, enter the following code snippet:
         
         operate("OPERATION_NAME").queries(ctx => "CUSTOM_SQL_QUERY");
         

Replace the following:

     * `OPERATION_NAME`: the name for the custom operation
     * `CUSTOM_SQL_QUERY`: your custom SQL query
  4. To define another custom SQL operation in the same file, repeat step 3.

  5. Optional: Click **Format**.




The following code sample shows a custom SQL operation in a JavaScript file that inserts a single new row into `some_table` and sets `test_column` of the new row to `2`:
    
    
      operate("operation1").queries("INSERT INTO some_table (test_column) VALUES (2)");
    

## What's next

  * To learn how to create a package, see [Create a package](https://docs.cloud.google.com/dataform/docs/use-packages#create-package).
  * To learn how to install a package, see [Install a package](https://docs.cloud.google.com/dataform/docs/use-packages#install-package).
  * To learn how to authenticate a private package, see [Authenticate a private package](https://docs.cloud.google.com/dataform/docs/use-packages#authenticate-private-package).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
