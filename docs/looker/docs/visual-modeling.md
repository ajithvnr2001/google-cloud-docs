---
url: https://docs.cloud.google.com/looker/docs/visual-modeling/
title: Using the visual modeling canvas \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:20.030320+00:00
---

# Using the visual modeling canvas  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/visual-modeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the visual modeling canvas Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue or if you have feedback during the Public Preview of the visual modeling canvas, report it to [visual_modeling_looker@google.com](mailto:visual_modeling_looker@google.com).

The visual modeling canvas in Looker lets you connect to BigQuery data sources so that you can build and edit LookML data models by using an interactive, drag-and-drop canvas. With the visual modeling canvas, you can visually join tables, define dimensions and measures, preview query results in real time, and publish Explores without writing LookML code.

![The visual modeling canvas](https://docs.cloud.google.com/static/looker/docs/images/visual-model-2614.png)

## Canvas components

The visual modeling canvas includes the following workspace components and navigation tabs:

  * **Sources** database: A searchable sidebar that displays available database datasets, tables, and views on the active connection
  * **Visual canvas** graph_4: The main workspace where you drag tables, arrange table nodes, and define join relationships
  * **LookML code** code: A panel that displays the generated LookML code that's behind your visual model
  * **Data preview** table_chart: A collapsible bottom panel that shows a real-time query preview (`LIMIT 100`) of the joined dataset
  * **Field editor** edit_attributes: A panel for adding, renaming, and customizing dimensions and measures



## Before you begin

To use the visual modeling canvas, you must have the following:

  * A Looker instance running Looker 26.14 or later, that's configured by a Looker admin to [enable self-service Explores](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore)
  * A BigQuery database connection that's configured with the following settings: 
    * Configured with the **All projects** scope in the [**Databases** tab](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#databases_tab) of the **Connections** page
    * Configured for [authentication with OAuth](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#authentication_with_oauth)
  * A Looker user account with the [`create_self_service_from_table`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_self_service_from_table) permission
  * A Google Account with the following IAM roles for the target BigQuery tables: 
    * [`bigquery.jobUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
    * [`bigquery.dataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)



## Creating a visual model

The following sections provide the steps for creating a new data model by using the visual modeling canvas:

  1. Connect to your database
  2. Add tables to the canvas
  3. Define relationships and joins
  4. Add and configure measures and dimensions
  5. Preview your data in real time
  6. View the LookML for your model
  7. Publish your model to an Explore



### Connect to your database

To connect to your database, follow these steps:

  1. In Looker, click the **Create** button in the main navigation.
  2. Select **Data source**.
  3. In the **Create data source** dialog, select the **Connect to Database** tab.
  4. Choose a database connection from the **BigQuery Connection** drop-down menu.
  5. Specify your project: 
     * Select **Select from list** to choose from available projects on the connection.
     * Select **Enter manually** to type the project ID directly.
  6. Specify whether to include all tables or select specific tables: 
     * Select **Include all datasets and tables in this selected project** to begin with an empty canvas. From the empty canvas, you can add tables from your sources list.
     * Select **Choose a specific table** to specify a single dataset and table to add to the canvas. The visual modeling canvas will open to the field editor and load the fields from your selected table. You can click **Visual canvas** graph_4 from the navigation bar to see the table in the canvas. You can add other tables from your sources list.
  7. Click **Continue** to open the visual modeling canvas.



### Add tables to the canvas

To add tables to the canvas to begin modeling your data, follow these steps:

  1. In the **Sources** database sidebar, browse or search for the datasets, tables, or views that you want to model.
  2. Drag each table from the sidebar onto the canvas.
  3. Reposition table nodes on the canvas to organize your data model layout.



When you drag a table onto the canvas, the visual modeling canvas represents it as a _table node_. The canvas displays the table name and its BigQuery project and dataset ID. The first table added to the canvas is labeled **Base view**.

### Define relationships and joins

When you add more than one table to the canvas, the visual modeling canvas scans for matching column names (for example, `order_id` in `orders` and `order_items`) and automatically proposes a join connection line between the tables.

To modify or create relationships between tables in your database, follow these steps:

  1. Click the join connection line between two table nodes to open the **Join Configuration** panel. Configure the join in the **Join Configuration** panel: 
     * **Join Type** : Select the join type (**Left Outer** , **Inner** , or **Full Outer**). By default, Looker uses a Left Outer join.
     * **Relationship (Cardinality)** : Select the relationship type (**One-to-One** , **One-to-Many** , **Many-to-One** , or **Many-to-Many**).
     * **Join clause** : Review the automatically suggested join keys, or add custom join conditions. You can specify multiple join conditions (such as `orders.id = order_items.order_id AND orders.date = order_items.date`).
  2. **Resolve Join Errors** : If a join creates an invalid SQL path or circular reference, the connection line turns red with an explanatory tooltip. Adjust the join keys or relationship cardinality to resolve the error.
  3. If you have changed the join settings, click **Apply** to apply your changes to the join.



### Add and configure measures and dimensions

The visual modeling canvas automatically sets up dimensions and measures for your tables, and lets you add custom calculations. By default, the visual modeling canvas creates a measure of type `count` or `sum` for numeric fields, while retaining fields with names containing `ID`, `Key`, or `Code` as numeric dimensions. When you define a **One-to-Many** relationship, the visual modeling canvas automatically applies symmetric aggregation logic to prevent fan-out and duplicate value calculation errors.

You can't delete a generated field; you can only hide it, either by selecting **Hide** from the field's gear menu in the field editor, or by clicking the field's **Edit** edit icon and selecting the **Hide this field from Explores and visualizations** checkbox.

To view the fields for a table, select the table node in the canvas and then click **Edit fields**.

From the field editor, you can perform the following tasks:

  * Edit a dimension
  * Edit a measure
  * Create a custom dimension
  * Create a custom measure



#### Edit a dimension

To edit an existing dimension, follow these steps:

  1. From the visual modeling canvas, select a table node in the canvas and then click **Edit fields** to open the field editor.
  2. In the field editor, click the **Dimensions** tab.
  3. Find the dimension that you want to edit and click the field's **Edit** edit icon to open the **Edit dimension** dialog.
  4. Update any of the following fields (the **Data type** field is read-only): 
     * **Format** : Select a formatting option from the drop-down menu.
     * **Name** : Edit the name that's used to identify the dimension in LookML and expressions.
     * **Label** : Edit the label that appears in Explores and visualizations.
     * **\+ Add description** : Click this option to enter or edit an optional description for the dimension.
     * **Hide this field from Explores and visualizations** : Select or clear this checkbox to hide or display the dimension.
  5. Click **Save**.



#### Edit a measure

To edit an existing measure, follow these steps:

  1. From the visual modeling canvas, select a table node in the canvas and then click **Edit fields** to open the field editor.
  2. In the field editor, click the **Measures** tab.
  3. Find the measure that you want to edit and click the field's **Edit** edit icon to open the **Edit measure** dialog.
  4. Update any of the following fields:

**Note:** For count measures, you can edit only **Label** , **Format** , **Description** , and **Hide this field from Explores and visualizations**.
     * **Field to measure** : Select the field that you want to aggregate from the drop-down menu.
     * **Measure type** : Select the aggregation type (such as **Sum** , **Count** , **Average** , **Min** , or **Max**) from the drop-down menu.
     * **Label** : Edit the label that appears in Explores and visualizations.
     * **Filters tab** : Under **Narrow results** , select a field from the **Filter name** drop-down menu and specify a **Filter value**. Use the **+** and **-** buttons to add or remove filter conditions.
     * **Field details tab** : Select a formatting option from the **Format** drop-down menu and enter an optional **Description** (up to 255 characters).
     * **Hide this field from Explores and visualizations** : Select or clear this checkbox to hide or display the measure.
  5. Click **Save**.




#### Create a custom dimension

To create a custom dimension by using a Looker expression, follow these steps:

  1. From the visual modeling canvas, select a table node in the canvas and then click **Edit fields** to open the field editor.
  2. From the field editor in the visual modeling canvas, click **Add dimension** to open the **Create dimension** dialog.
  3. In the expression editor box, enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) that defines the dimension, or click **Help me write an expression with Gemini** to generate an expression.
  4. Select a formatting option from the **Format** drop-down menu.
  5. Enter a **Name** and a **Label** for the dimension.
  6. Optionally, click **\+ Add description** to enter or edit a description for the dimension.
  7. Optionally, select the **Hide this field from Explores and visualizations** checkbox to hide the dimension.
  8. Click **Save**.



#### Create a custom measure

To create a custom measure, follow these steps:

  1. From the visual modeling canvas, select a table node in the canvas and then click **Edit fields** to open the field editor.
  2. In the field editor, click the **Measures** tab and then click **Add measure** to open the **Create measure** dialog.
  3. Select the field that you want to aggregate from the **Field to measure** drop-down menu.
  4. In the **Measure type** drop-down, select the type of aggregation that you want to perform on the **Field to measure** field.
  5. Enter a **Label** for the measure.
  6. Configure optional filter conditions or formatting details: 
     * **Filters tab** : Under **Narrow results** , select a field from the **Filter name** drop-down menu and specify a **Filter value**. Use the **+** and **-** buttons to add or remove filter conditions.
     * **Field details tab** : Select a formatting option from the **Format** drop-down menu and enter an optional **Description** (up to 255 characters).
  7. Optionally, select the **Hide this field from Explores and visualizations** checkbox to hide the measure.
  8. Click **Save**.



### Preview your data in real time

Follow these steps to verify the data output of your model:

  1. In the visual modeling canvas, click the **Data preview** tab table_chart from the navigation bar.
  2. Click a table in the canvas to select fields from that table.
  3. In the data preview pane, click the **Preview columns** drop-down menu.
  4. From the drop-down menu, select the fields from the table that you want to query, and then click **Preview**.

The visual modeling canvas will query your database and show the query results in a table in the data preview pane.

  5. Inspect the data to ensure that no unintended row fan-out or dropped records occur. 

  6. Update the joins or fields as necessary, and then click **Refresh schema** in the data preview pane to update the table.




### View the LookML

Click the **LookML code** tab code to inspect the generated LookML for your model. The LookML for visual models is read-only. If you want to edit fields and joins, use the visual modeling canvas.

### Publish your model to an Explore

To save your model, click the **Explore data** button in the visual modeling canvas. 

Looker generates the underlying LookML model files and saves the canvas layout coordinates. Your model is now published and ready to query.

## Accessing visual models

Published visual models appear in the Looker navigation under **Explore** in the **Self-service Explores** section.

To query a visual model, follow these steps:

  1. In Looker, click **Explore** in the main navigation.
  2. Under **Self-service Explores** , select your model's Explore name.
  3. Select dimensions and measures from the field picker, add filters, and run queries to create visualizations and dashboard tiles.



## Editing an existing visual model

To modify an existing model that's created with the visual modeling canvas, follow these steps:

  1. In Looker, click **Explore** in the main navigation menu.
  2. Under **Self-service Explores** , open the Explore for the model that you want to edit.
  3. Select **Edit Model** from the Explore's field picker to open the visual modeling canvas. If you're using the classic Explore experience, select **Edit Model** from the Explore's gear menu.
  4. Make your changes in the visual modeling canvas (such as adding tables, updating join clauses, or creating new measures).
  5. Click **Explore data** to update the model.

**Note:** If multiple users edit the same visual model, the most recently saved version is persisted.

## Deleting a visual model

To delete a visual model, follow these steps:

  1. In Looker, click **Explore** in the main navigation menu.
  2. Under **Self-service Explores** , open the Explore for the model that you want to edit.
  3. Select **Edit Model** from the Explore's field picker to open the visual modeling canvas. If you're using the classic Explore experience, select **Edit Model** from the Explore's gear menu.
  4. From the visual modeling canvas, select **Delete** from the three-dot menu.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
