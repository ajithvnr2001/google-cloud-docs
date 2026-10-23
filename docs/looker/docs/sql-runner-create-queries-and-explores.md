---
url: https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores/
title: Using SQL Runner to create queries and Explores \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:51.076340+00:00
---

# Using SQL Runner to create queries and Explores  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using SQL Runner to create queries and Explores Stay organized with collections  Save and categorize content based on your preferences. 

SQL Runner provides a way to directly access your database and leverage that access in a variety of ways. Using SQL Runner, you can easily navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML Project as a derived table, and perform other useful tasks.

This page describes how to run queries in SQL Runner, create ad hoc Explores, and how to use SQL Runner to debug queries. See these other documentation pages for information on:

  * [SQL Runner basics](https://docs.cloud.google.com/looker/docs/sql-runner-basics)
  * [Using SQL Runner to create derived tables](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables)
  * [Managing database functions with SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db)



## Running queries in SQL Runner

To run a query on your database, you can write the SQL query from scratch, use an Explore to create the query, or run a query against a LookML model. You can also use the history to rerun a previous query.

### Writing a SQL query from scratch

You can use SQL Runner to write and run your own SQL queries against your database. Looker passes your query to your database just as you have written it, so be sure that the syntax of your SQL query is valid for your database dialect. For example, each dialect has slightly different SQL functions with specific parameters that should be passed to the function.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-write-2220.png)

  1. Enter a SQL query in the field below the **Query** bar.
  2. Optionally, select a table name or field from the field list to include it in your query at the cursor location.
  3. Select **Run** to run the query against your database.
  4. View the results in the **Results** area. SQL Runner will load up to 5,000 rows of the query's result set. For SQL dialects that support [streaming](https://docs.cloud.google.com/looker/docs/downloading#streaming_query_results), you can download the results to see the entire result set.

**Note:** Some SQL programs will let you run multiple queries in a series. However, you can only run one query at a time in SQL Runner. SQL Runner also has a 65,535 character limit on queries, which includes whitespace.

After running a query, you can [add the query to a project](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables#adding_a_sql_runner_query_to_a_lookml_project), [get the LookML for a derived table](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables#get_derived_table_lookml), or share the query.

You can also use SQL Runner to play with new queries or test existing queries. SQL Runner error highlighting helps test and debug queries.

### Using an Explore to create a SQL query

You also can use an Explore to create a query, and then get the SQL command for that query to use in SQL Runner:

![](https://docs.cloud.google.com/static/looker/docs/images/develop-sql-runner-write-explore-2412.png)

  1. From an Explore, select the **SQL** tab from the **Data** bar.
  2. The SQL query will appear under the **Data** bar.
  3. Select **Open in SQL Runner** or **Explain in SQL Runner** to open the query in SQL Runner.



Once a query is added to the field below the **Query** bar, you can select **Run** to query the database. Alternatively, you can edit the query and then run the new query.

**Note:** Database connection access in Looker is model-driven. A user's ability to see and use a database connection in both Explores and SQL Runner is determined by the LookML models that their assigned [roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) grant them access to. If a user's role grants them access to a model set that uses a broader-permission connection, that connection automatically appears as an available option in SQL Runner.

Because of this model-driven behavior, it's not possible to hide a connection from SQL Runner while keeping it available for Explores for the same user if that user's role grants them access to both. As a workaround, implement separate roles for users who require only restricted SQL Runner access and don't need access to Explores that are built on the broader-permission connection, or instruct users to manually select the restricted connection in SQL Runner.

### Creating visualizations with SQL Runner

If your Looker admin has enabled the [**SQL Runner Vis**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#sql_runner_vis) Labs feature, you can create visualizations directly in SQL Runner.

**Note:** This feature is not supported for [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-overview).

With **SQL Runner Vis** enabled, the SQL Runner panels are reorganized. The visualization panel appears at the top, the results panel is in the middle, and the query panel appears at the bottom.

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-vis-create-query-2120.png)

  1. After a SQL query is created and run, you can open the **Visualization** tab to view the visualization and choose a visualization type, [just as you would do on the Explore page](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type).
  2. You can edit the visualization by using the **Settings** menu.
  3. You can share visualizations that were created with SQL Runner by sharing the URL. Any customizations that you make by using the visualization's **Settings** menu will be saved and the link won't change.



There are some things to keep in mind about how SQL Runner visualizations work:

  * The results table and visualization interpret any numeric field as a measure.
  * The full field name is always used in the results table and visualization. Therefore, the **Show Full Field Name** option in the **Settings** menu is inactive.
  * To use custom fields, table calculations, pivots, column totals, and subtotals, [explore from your SQL Runner query](https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores#exploring_from_sql_runner_query_results).
  * Static map (regions) visualizations are not supported by SQL Runner visualizations, however maps that use latitude and longitude data (map and static map (points) visualizations) are supported.
  * Timeline visualizations are not supported by SQL Runner visualizations.



#### Pivoting dimensions

You can edit the query results to [pivot](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) by one or more dimensions in SQL Runner visualizations. To pivot a field:

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-72-pivot-steps.png)

  1. Select a column's gear menu in the **Results** area to expose column options.
  2. Select **Pivot Column**.



The pivoted results display in the SQL Runner visualization.

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-vis-pivot-72.png)

**Note:** The results in the **Results** area don't appear pivoted.

To **unpivot** results, select the pivoted column's gear menu and select **Unpivot Column**.

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-unpivot-column-72.png)

#### Changing the field type

When displaying your query's results and visualization, SQL Runner automatically interprets any numeric field as a measure and any non-numeric field as a dimension. You can override the default field type and convert a dimension to a measure – or vice versa – by following these steps:

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-vis-change-field-type-72.png)

  1. Select a column's gear menu in the **Results** area to expose column options.
  2. Select **Convert to Dimension** or **Convert to Measure** to change the field type.



The visualization will display the new field type.

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-change-field-type-vis-72.png)

### Running a query against a LookML model

You can use SQL Runner to write and run SQL queries against a LookML model, instead of directly against your database. When constructing your query against a model, you can use [LookML substitution operators](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\)), such as `${view_name.field_name}` or `${view_name.SQL_TABLE_NAME}`. This can save time when constructing a query to troubleshoot a derived table, for example.

Looker resolves any LookML substitutions and then passes your query to your database, so the query should be in valid SQL for your database dialect. For example, each dialect has slightly different SQL functions with specific parameters that should be passed to the function.

To run a query against your LookML model in SQL Runner:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-query-model-512.png)

  1. Select the **Model** tab.
  2. Select the model that you want to query.
  3. In the text box under the **Data** bar, enter your SQL query by using LookML fields.
  4. Optionally, select a view in the view list to include the view in your query at the cursor location.
  5. To see the list of fields in a view, select the view in the **Views** section. Optionally, you can select a field in the field list to include it in your query at the cursor location.
  6. In the **Prepared SQL Query** area, you can view the resulting SQL query that is built after any LookML substitutions have been translated to SQL.
  7. Select **Run** to run the query against your model.
  8. View the results in the **Results** area. SQL Runner loads up to 5,000 rows of the query's result set. For SQL dialects that support streaming, you can download the results to see the entire result set.



You can use SQL Runner to play with new queries, test existing queries, or open a new Explore from the results. SQL Runner error highlighting helps test and debug queries.

When you have a query that you like, you can share the query and even [add the query to a LookML project](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables#adding_a_sql_runner_query_to_a_lookml_project).

#### Viewing a field's LookML from SQL Runner

From the field list in the **Model** tab, you can also see the LookML for a field. Hold your pointer over the field in the field list, and select the Looker icon to the right of the field name.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-goto-lookml-512.png)

Looker opens up the LookML IDE, and loads the file where the field is defined.

### SQL Runner history

You can also see a recent history of all queries you have run in SQL Runner.

To see your history, select the **History** tab at the top of the navigation pane. SQL Runner displays all the queries that were run on the database connection. Red indicates a query that did not run because an error occurred.

Select a query in the history to populate that query into SQL Runner, and then select **Run** to rerun the query.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-history-512.png)

### Sorting your query

A table's sort order is indicated by an upward or a downward arrow next to the sorted field name, depending on whether the results are in ascending or descending order. You can sort by multiple columns by holding down the Shift key and then selecting the column headers in the order that you want them sorted. A field's sort order is also indicated by a number that distinguishes its sort-by order as compared to other fields, by an arrow next to the field name that shows the sorting direction (ascending or descending), and by a pop-up that appears when you hold your pointer over a field name.

For more information and examples, see the [Sorting data](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data) section of the **Exploring data in Looker** documentation page.

### Sharing queries

You can share a query in SQL Runner with another user who has SQL Runner access. To share a query, copy the URL in the address bar of your browser.

### Downloading results

Once you have run your SQL query, you can download the results in a variety of formats.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-download-512.png)

  1. Write a query in the **SQL Query** box. (You do not need to run the query in SQL Runner at this point.)
  2. Select **Download** from the gear menu in the upper right.
  3. Select the file format of the download (text file, CSV, JSON, etc.).
  4. Select **Open in Browser** to see the results in a new browser window, or select **Download** to download the results to a file on your computer.

**Note:** When you select either **Open in Browser** or **Download** , Looker will rerun the query and then perform the download.



For SQL dialects that support streaming, the SQL Runner **Download** option will download the entire result set. For SQL dialects that do not support streaming, the SQL Runner **Download** option will download only the rows of the query that are shown in the **Results** section (up to 5,000 rows).

### Copying column values

You can copy column values from the **Results** section in SQL Runner. Select a column's gear menu to copy the values to your clipboard. From there you can paste the column values into a text file, an Excel spreadsheet, or another location.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-copy-values-512.png)

If your Looker admin has enabled the [**SQL Runner Vis**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#sql_runner_vis) Labs feature, you have other options in the column gear menu as well:

  * [Freeze and Unfreeze](https://docs.cloud.google.com/looker/docs/table-options#freeze)
  * [Autosize All Columns](https://docs.cloud.google.com/looker/docs/table-options#autosize_all_columns)
  * [Reset All Column Widths](https://docs.cloud.google.com/looker/docs/table-options#reset_all_column_widths)



You can also manually [move, pin](https://docs.cloud.google.com/looker/docs/table-options#manually_moving_and_pinning_columns) and [resize](https://docs.cloud.google.com/looker/docs/table-options#manually_resizing_columns) columns in the results table.

### Cost estimates for SQL Runner queries

For [BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery), [MySQL](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore), [Amazon RDS for MySQL](https://docs.cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds), [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake), [Amazon Redshift](https://docs.cloud.google.com/looker/docs/db-config-amazon-redshift), [Amazon Aurora](https://docs.cloud.google.com/looker/docs/db-config-amazon-aurora-mysql), [PostgreSQL, Cloud SQL for PostgreSQL, and Microsoft Azure PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql) connections, SQL Runner provides an estimate of the cost of the query. Once you enter the SQL query, SQL Runner will calculate the amount of data that the query will require and display the information near the **Run** button.

> For BigQuery, MySQL, and Amazon RDS for MySQL connections, cost estimates are always enabled. For Snowflake, Amazon Redshift, Amazon Aurora, PostgreSQL, Cloud SQL for PostgreSQL, and Microsoft Azure PostgreSQL database connections, you must enable the [**Cost Estimate**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#cost_estimate) option for the connection. You can enable **Cost Estimate** when you [create the connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#creating_a_new_database_connection). For existing connections, you can [edit the connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#editing_connections) from the [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) page in the **Database** section of Looker's **Admin** panel.

## Creating an ad hoc Explore

From SQL Runner you can get fast insight into the data by creating an ad hoc Explore for a SQL query or database table. You can use the Looker Explore to select fields, add filters, visualize the results, and create SQL queries.

There are two ways to open an ad hoc Explore from SQL Runner:

  * Explore from SQL Runner's query results
  * Explore from SQL Runner's table list



### Exploring from SQL Runner query results

SQL Runner lets you open an Explore from a SQL query. This creates a temporary Explore from the query written in SQL Runner. That lets you test what is returned by the query, as well as visualize the results. This can be used for any query but is especially useful for testing queries you plan to use for derived tables.

**Note:** If your Looker admin has enabled the [**SQL Runner Vis**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#sql_runner_vis) Labs feature, you can create visualizations directly in SQL Runner. This feature is not supported for [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences).

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-explore-a-2120.png)

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-explore-b-2120.png)

  1. Use SQL Runner to create the SQL query that you want to use.
  2. Select **Explore** from the gear menu in the upper right. This takes you to a new Explore, where you can explore the SQL query as if it were a saved table in your model.
  3. You can copy the URL to this Explore for sharing.
  4. To add this query as a derived table in your project directly from here, select **Add View to Project**.



### Creating custom fields while exploring in SQL Runner

If you have access to the [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) feature, you can use custom fields to visualize unmodeled fields in SQL Runner. As described in the previous section, select **Explore** from the gear menu. Then, in the field picker, follow these steps:

  * Select the **Custom Fields** section to open it, and then select **Add** to begin creating a [custom dimension](https://docs.cloud.google.com/looker/docs/custom-fields#creating_a_custom_dimension_using_a_looker_expression), [custom measure](https://docs.cloud.google.com/looker/docs/custom-fields#using_the_custom_fields_section), or [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations). (If you don't have the **Custom Fields** section, you don't have access to create custom fields.)
  * Select a measure's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#three-dot_more_menu) and choose **Filter Measure** to create a [filtered custom measure from an existing measure](https://docs.cloud.google.com/looker/docs/custom-fields#creating_a_filtered_custom_measure_from_another_measure).
  * Select a dimension's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#three-dot_more_menu) and choose a measure type (like sum or count) to create a [custom measure from a dimension](https://docs.cloud.google.com/looker/docs/custom-fields#using_the_dimensions_gear_menu).



### Exploring a table listed in SQL Runner

Use the **Explore Table** option in the **Database** tab to create an ad hoc Explore for any table in the connection. This lets you use Looker on a table before you've modeled it, exploring the table just like a LookML view.

Once you open an Explore for the table, you can decide whether to add the table to your project. You can also use the Explore's **SQL** tab to see the SQL queries that Looker sends to the database, and then use the **Open in SQL Runner** button to bring the query back into SQL Runner.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-explore-table-512.png)

  1. Select the **Database** tab.
  2. In SQL Runner, select the gear for a table and then select **Explore Table**.
  3. Looker generates a temporary model with a view for the table and then displays the Explore.
  4. Looker provides a dimension field for each column in the table. (This is the same way that Looker [generates a model at the start of a project](https://docs.cloud.google.com/looker/docs/generating-a-model).)
  5. Looker automatically includes timeframes for any date fields.
  6. Looker also includes a count measure.

**Note:** When using the **Explore Table** option, there is no LookML file associated with the Explore — it is just an ad hoc view of the table.

## Debugging using SQL Runner

SQL Runner is also a useful tool for checking SQL errors in queries.

### SQL Runner error highlighting

SQL Runner highlights the location of errors in the SQL command and includes the position of the error in the error message:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-error-highlighting-512.png)

The position information provided will vary depending on the database dialect. For example, MySQL provides the line number that contains the error, while Redshift provides the character position of the error. Other database dialects might have one of these or other behaviors.

SQL Runner also highlights the location of the _first_ syntax error in the SQL command by underlining it in red and marking the row with an **x**. Hold the pointer over the **x** to see more information on the error. After you fix that issue, select **Run** to see if there are any more errors in the query.

### Using SQL Runner to check errors in Explores

If you run into SQL syntax errors in an Explore, you can use SQL Runner to determine the location of the error and the type of error, such as spelling mistakes or missing commands.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-open-in-sql-runner-error-620.png)

  1. From the Explore, select the **SQL tab** of the Data bar.
  2. Select **Open in SQL Runner** to open the query in SQL Runner.



This copies the Explore's generated SQL to SQL Runner. As shown in the **SQL Runner error highlighting** section, SQL Runner highlights the location of errors in the SQL command and includes the position of the error in the error message. You can then make changes and re-run the query in SQL Runner until you have corrected the errors.

### Using SQL Runner to check errors in derived tables

For information about using SQL Runner to check SQL errors in [derived tables](https://docs.cloud.google.com/looker/docs/derived-tables), see the [Using SQL Runner to test derived tables](https://discuss.google.dev/t/using-sql-runner-to-test-derived-tables/115142) Looker Community post.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
