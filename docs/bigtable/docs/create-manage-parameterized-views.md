---
url: https://docs.cloud.google.com/bigtable/docs/create-manage-parameterized-views/
title: Create and manage parameterized views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:22.426203+00:00
---

# Create and manage parameterized views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-manage-parameterized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage parameterized views

You can create a parameterized view from a logical view in Bigtable and then perform operations on parameterized views.

Before you read this page, familiarize yourself with [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

## Before you begin

If you plan to use the Google Cloud CLI, follow these steps:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 



### Required roles

To get the permissions that you need to create and manage parameterized views, ask your administrator to grant you the Bigtable Admin (`roles/bigtable.admin`) role on the instance.

Alternatively, you can ask for the following permissions at the instance level:

  * Create: `bigtable.logicalViews.create`
  * Update: `bigtable.logicalViews.update`
  * Delete: `bigtable.logicalViews.delete`
  * List: `bigtable.logicalViews.list`



To create a parameterized view, you must also have at least the `bigtable.tables.readRows` permission on the source table.

## Create a parameterized view

A parameterized view is a virtual table defined by a SQL `SELECT` statement that can include the `VIEW_PARAMETERS()` function.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. From the list, select an instance.

  3. In the navigation pane, click **Bigtable Studio**.

  4. Open a new tab by clicking add **New tab menu** , and then select **Editor**.

  5. In the query editor, write your SQL query. The query definition must call the `VIEW_PARAMETERS()` function to specify one or more view parameters. For example:
         
         SELECT *
         FROM TABLE_ID
         WHERE STARTS_WITH(_key, CAST(VIEW_PARAMETERS('PARAM_NAME') AS BYTES))
         

Replace the following:

     * `TABLE_ID`: the ID of the source table.
     * `PARAM_NAME`: the name of the view parameter, enclosed in single quotes, to pass as an argument to the `VIEW_PARAMETERS()` function. This defines the parameter name, not its runtime value. You supply the runtime value when you query the parameterized view.

If the query is valid SQL, then a **Valid** message appears.

  6. Optional: To format your statement in SQL style, click **Format**.

  7. Click **Save** , and then select **Save as logical view**.

  8. In the **Save your logical view** dialog, enter a name for the view, and then click **Save**.

The view appears in the **Explorer** pane, in the **Logical Views** list, with a variable_add parameterized view icon.

For more information about using the query editor, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).




###  gcloud 

To create a parameterized view, use the [`gcloud bigtable logical-views create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/create) command.
    
    
    gcloud bigtable logical-views create VIEW \
      --instance=INSTANCE \
      --query="SELECT * FROM TABLE_ID WHERE STARTS_WITH(_key, CAST(VIEW_PARAMETERS('PARAM_NAME') AS BYTES))"
    

Replace the following:

  * `VIEW`: an ID up to 128 characters long for the new parameterized view. The ID must be unique among table IDs and view IDs in the instance.
  * `INSTANCE`: the ID of the instance in which to create the parameterized view.
  * `TABLE_ID`: the ID of the source table.
  * `PARAM_NAME`: the name of the view parameter, enclosed in single quotes, to pass as an argument to the `VIEW_PARAMETERS()` function. This defines the parameter name, not its runtime value. You supply the runtime value when you query the parameterized view.



Optional:

  * To protect the parameterized view from deletion, append the command with the `--deletion-protection` flag. If you don't apply this setting, then the view can be deleted. You can also explicitly allow view deletion by appending `--no-deletion-protection`. For more information, see the Update a parameterized view section of this document.



## Create a parameterized view with a structured row key

If your table uses a structured row key, then you can filter on a specific segment of the row key. For more information, see [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas).

For example, if a row key in a purchase history table stores the user, timestamp of the purchase date, and order ID, delimited by a `#` symbol, you can specify the row schema as follows:
    
    
    field {
        field_name: "user_id"
        type: { bytesType { encoding { raw {} } } }
      }
      field {
        field_name: "reversed_timestamp"
        type: { timestampType { encoding { unixMicrosInt64 { encoding: {           orderedCodeBytes: {} } } } } }
      }
      field {
        field_name: "order_id"
        type: { stringType { encoding { utf8Bytes {} } } }
      }
      encoding {
        delimitedBytes { delimiter "#" }
      }
    

You can then create a view that filters on the user ID field:

###  Console 

  1. In Bigtable Studio, open the query editor and enter the SQL query that filters on the row key segment:
         
         SELECT *
         FROM TABLE_ID
         WHERE user_id = CAST(VIEW_PARAMETERS('user_id') AS BYTES)
         

Replace `TABLE_ID` with the ID of the source table.

  2. Click **Save** , and then select **Save as logical view**.

  3. In the **Save your logical view** dialog, enter a name for the view, and then click **Save**.

The view appears in the **Explorer** pane, in the **Logical Views** list, with a variable_add parameterized view icon.




###  gcloud 

To create a parameterized view with a structured row key, use the [`gcloud bigtable logical-views create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/create) command.
    
    
    gcloud bigtable logical-views create VIEW \
        --instance=INSTANCE \
        --query="SELECT * FROM TABLE_ID WHERE user_id = CAST(VIEW_PARAMETERS('user_id') AS BYTES)"
    

Replace the following:

  * `VIEW`: an ID of up to 128 characters for the new parameterized view. The ID must be unique among table IDs and view IDs in the instance.
  * `INSTANCE`: the ID of the instance in which to create the parameterized view.
  * `TABLE_ID`: the ID of the source table.



## Update a parameterized view

You update a parameterized view in the same way that you [update a logical view](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views#update).

## Delete a parameterized view

You delete a parameterized view in the same way that you [delete a logical view](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views#delete).

## View information about parameterized views

You view a list of parameterized views in the same way that you [view a list of logical views for an instance](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views#list).

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. From the list, select an instance.

  3. In the navigation pane, click **Bigtable Studio**.

  4. In the **Explorer** pane, expand **Logical Views**.

Parameterized views appear in the list with a variable_add parameterized view icon that distinguishes them from standard logical views.

  5. If the instance has more than 10 views, then click **Show more** to load the next 10.




###  gcloud 

To see a list of logical views for an instance, use the [`gcloud bigtable logical-views list`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/list) command.
    
    
    gcloud bigtable logical-views list --instance=INSTANCE
    

Replace `INSTANCE` with the instance ID.

## Query parameterized views

You query parameterized views similarly to regular tables, but you provide the `view_parameters` map in the request.

**Note:** For each view parameter in your request, you must specify the data type. Only values of the `STRING` type are supported. If a parameter represents a different data type in your view's SQL definition, you must pass the parameter value as a string and cast it to the correct type in the SQL definition—for example, `CAST(VIEW_PARAMETERS('PARAM_NAME') AS INT64)`.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. From the list, select an instance.

  3. In the navigation pane, click **Bigtable Studio**.

  4. In the **Explorer** pane, expand **Logical Views**.

  5. Next to the parameterized view that you want to query, click the more_vert **View actions** menu, and then click **Query view**.

A **Parameters** pane opens with the view parameter names prepopulated.

  6. In **View parameters** , enter the runtime values for each required parameter in the **Value** fields.

Parameter values are passed as strings. If a parameter in your view definition is cast to another type (such as an integer or bytes), enter the raw string value.

  7. Optional: To add more parameters, click **Add parameter** , and then enter the parameter name and value. Parameter names must be unique within view parameters.

  8. Click **Save**.

  9. In the query editor, click **Run**.

The results of your query appear in the **Results** table.

If you run the query without providing required view parameters, then an error message appears in the results section with an **Edit parameters** button. Click **Edit parameters** to open the **Parameters** pane and enter the missing parameter values.




Parameter values are configured for each query editor tab. If you navigate away from Bigtable Studio during your session and return, then your open tabs, queries, results, and configured parameters are preserved.

###  Java 

The following example shows how to query a parameterized view named `purchase_history_pv`, which filters data based on a user ID:
    
    
    // Assumes 'purchase_history_pv' was created with the definition:
    // SELECT * FROM purchases WHERE user_id = CAST(VIEW_PARAMETERS('user_id') AS BYTES)
    
    String query = "SELECT customer_info[email], order_details[status], order_info[items] from purchase_history_pv";
    PreparedStatement preparedStatement = dataClient.prepareStatement(query);
    BoundStatement boundStatement = preparedStatement.bind().build();
    
    // The user ID is now passed out-of-band in a view parameters map.
    Map<String, Value> viewParameters = new HashMap<>();
    viewParameters.put("user_id", Value.newBuilder().setType(stringType()).setStringValue(userId).build());
    
    // Execute the query, passing the view parameters using a proto field in the request.
    ResultSet rs = dataClient.executeQuery(
        boundStatement,
        viewParameters
    );
    

This prevents the user from being able to see or manipulate the `user_id` parameter within the query itself, providing a clean logical separation.

## What's next

  * [Use parameterized views in agentic applications](https://docs.cloud.google.com/bigtable/docs/use-pvs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
