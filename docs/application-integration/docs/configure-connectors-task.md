---
url: https://docs.cloud.google.com/application-integration/docs/configure-connectors-task/
title: Connectors task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:44.287909+00:00
---

# Connectors task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-connectors-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connectors task

The **Connectors** task lets you quickly and securely connect to the various Google Cloud services and other business applications from your integration using the out-of-the-box connectors available in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/about-connectors). 

For the list of all the supported connectors for Application Integration, see [Connector reference](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview). **Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

  * Make sure that you have the Connectors Admin (`roles/connectors.admin`) IAM role granted on your Google Cloud project. For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn about the general concepts of [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action).
  * To connect to Google Cloud services and other business applications using a connector, ensure that you have [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration. If your integration does not have user-managed service account configured, then by default the [default service account](https://docs.cloud.google.com/application-integration/docs/access-control#default-service-account) (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used for authentication.
  * Ensure that your service account has the required IAM role. For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).



## Add a Connectors task

To add the Connectors task to your integration, do the following:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 

![image showing connectors task](https://docs.cloud.google.com/static/application-integration/images/apip_browse_connector_task.png)

  5. If you want to configure a new connection, click and place the **Connectors** element in the integration editor. Then, click **Configure connector** to configure the connection. 

![image showing connector task listing](https://docs.cloud.google.com/static/application-integration/images/apip-connector-browse-listing.png)![image showing connector task listing](https://docs.cloud.google.com/static/application-integration/images/apip-connector-browse-listing.png)

  6. If you have an existing connection, click the **Connectors** tab to view the recently created connections. You can also search for a connector, connection, or task by entering the name in the **Search** field. 

![image showing search capability for connectors task](https://docs.cloud.google.com/static/application-integration/images/apip_search_connector_task.png)

  7. Click and place the configured **Connectors** element in the integration editor. For information about how to configure a connector task, see Configure the Connectors task.



## Configure the Connectors task

To configure a **Connectors** task, do the following: **Note:** Configuration details such as authentication will vary depending upon the connection type.

  1. Click the **Connectors** task element on the designer to view the **Connectors** task configuration pane. 

Optionally, click  edit  to rename the task name.

  2. Click **Configure connector**.
  3. You can either select an existing connection in the region or create a new connection. To configure an existing connection, complete the following steps in the **Connectors Task Editor** page. 

The following image shows a sample layout of the **Connectors Task Editor** page. ![image showing Configure connector task dialog](https://docs.cloud.google.com/static/application-integration/images/apip_connector_task.png)![image showing Configure connector task dialog](https://docs.cloud.google.com/static/application-integration/images/apip_connector_task.png)

     1. In the **Select connection** section, select the region of the connection.
     2. Choose an existing connection from the list of available connections in the selected region.
     3. Click **Next**.
     4. From the **Type** list, select **Entities** or **Actions**. 
        * If you select **Entities** , the list of supported entities for the connection is displayed in the **Set entities/actions** section. Select an entity followed by the **Operation** that you want to perform on that entity.
        * If you select **Actions** , the list of supported actions for the connection is displayed in the **Set entities/actions** column. Select an action for the connection.
The supported entities and actions are based on the connector type. For the list of all the supported connectors for Application Integration, see [Connector reference](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview). To view the supported actions and entities for a connector, see the specific connector documentation. 

If the connector supports custom SQL queries, you can select the **Execute custom query** option from the **Actions** list. For information about how to add custom SQL query for your connector, see Action: Execute custom SQL query. 

**Note** : Not all connection types support **Entities** or **Actions**. If a connection type doesn't support any actions or entities, the corresponding **Entities** and **Actions** lists will be empty. For more about entities and actions, see [Entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action).
     5. Click **Done** to complete the connection configuration and close the pane.



### Configure task input and output variables

The **Connectors** task configuration pane displays **Task Input** and **Task Output** [variables](https://docs.cloud.google.com/application-integration/docs/variables-overview) that are automatically generated based on the _Entity and Operation_ or _Action_ selected in the **Configure connector task** dialog. These variables are configurable and are accessible as inputs to the current task, as outputs to subsequent tasks, or as conditionals in the current integration. 

To configure the **Task Input** or **Task Output** variables, click the respective variable to open the **Configure Variable** pane and perform the following steps:

  1. Enter the variable value in the **Default Value** field.
  2. (Optional) Select **Use as an input to integration** or **Use as an output to integration**.
  3. Click **Save**.



For more information about the input and output parameters of the **Connectors** task, see Entity operations.

### Configure authentication override

To enable the connection to accept different backend authentication dynamically during runtime, ensure that in Integration Connectors, you have selected the **Enable Authentication Override** option for your connection.

To configure the authentication override, do the following:

  1. Click the connectors task element on the designer to view the **Connectors** task configuration pane.
  2. Expand the **Task input** section. The **End user credentials** field is set to a `dynamicAuthConfig` variable. 

![End user credentials](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-task-input.png)![End user credentials](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-task-input.png)

Then, do the following:

     1. Click the `dynamicAuthConfig` variable. The **Edit variable** pane appears. 

For overriding the authentication, you must provide the authentication values when you [test the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations). 

![Edit dynamic euc variable](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-edit-variable.png)![Edit dynamic euc variable](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-edit-variable.png)

To do so, follow these steps:

        1. From the **Variable type** list, select **Input to Integration**.
        2. In the **JSON schema options** , you can verify the authentication type configured for the connection. Use this schema to override the authentication value when you [test the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations). 

![Test integration for auth override](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-test-integration.png)![Test integration for auth override](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-test-integration.png)

Alternatively, you can pass the authentication as the HTTP header by selecting the **Use HTTPS Header for Auth Config** checkbox in the **Task input** section of the **Connectors** task configuration pane.

The dynamic authentication header should be in the following JSON format:
    
    {"task1":{"oauth2_auth_code_flow.access_token": "token_value"},"task2":{"oauth2_auth_code_flow.userename": "username_value"}}

In this format, `taskN` corresponds to the Task ID in `integrationVersion`.

![Test integration by passing the authentication as the HTTP header](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-test-integration-http.png)![Test integration by passing authentication as the HTTP header](https://docs.cloud.google.com/static/application-integration/images/dynamic-euc-test-integration-http.png)




## Entity operations and actions

You can perform CRUD (Create, Read, Update, Delete) operations on the entities of a connector. Each of these entity operations has a different set of input and output parameters. The following table lists the input and output parameters for the various entity operations.

Operation name | **Input parameters** | **Output parameters**  
---|---|---  
List | 

  * listEntitiesPageSize
  * listEntitiesPageToken
  * listEntitiesSortByColumns
  * filterClause

| 

  * connectorOutputPayload
  * listEntitiesNextPageToken

  
Get | entityId | connectorOutputPayload  
**Note:** You can use the **Get** operation only to fetch a single record from a table that has a primary key. Alternately, you can use the **List** operation with a filterClause.   
Create | connectorInputPayload | connectorOutputPayload  
Update | 

  * connectorInputPayload
  * entityId
  * filterClause

|  connectorOutputPayload   
Delete | 

  * entityId
  * filterClause

| N/A  
  
### Input parameters

The following table describes the input parameters for the various entity operations.

Parameter name | Data type | Description  
---|---|---  
entityId | String | A unique identifier of the row that you want to access. Normally, the `entityId` is a primary key value of a table or a dataset. If you specify a value for the `entityId` and the table or dataset doesn't have a primary key column, Integration reports a runtime error and the **Connectors** task fails. For example, to get a specific row from a MySQL table, the `entityId` is the primary key value in the table. **Note:** The `entityId` is not mandatory for BigQuery. This field is empty when a BigQuery table doesn't have a primary key.  
connectorInputPayload | JSON | The actual data to be added or updated in an entity. The following example shows the JSON snippet of a row data to be added in a table: 
    
    
    {
    "employee_first_name": "John",
    "employee_emailID": "test-05@test.com"
    }
          

In this example, `employee_first_name` and `employee_emailID` are the column names with the corresponding values `John` and `test-05@test.com`.  
filterClause | String | Restricts the result of the operations based on a condition. For more information about adding a filter clause, see [Add a filter for an operation](https://docs.cloud.google.com/application-integration/docs/connectors-task#filter).   
listEntitiesPageSize | Integer |  Specifies the number of results that should be returned in a page. A page is a logical grouping of the records in a result set. The concept of a page is useful when you are expecting a large number of records in the result set. If the result set is large, the **Connectors** task might fail, as there is a limit on the data size that the **Connectors** task can process. By breaking down the result set into smaller chunks, you can avoid this issue. For example, if you are expecting 1000 records in your result set, you can set the `listEntitiesPageSize` to 100. So when the **Connectors** task runs for the first time, it returns the first 100 records, the next 100 records in the second run and so on.  **Important:**

  * The default page size is 25, and the maximum number of pages supported by the task is 50000.
  * Unless your table or dataset has a primary key, you must set the `listEntitiesSortByColumns` parameter to use `listEntitiesPageToken`. 
  * Use the `listEntitiesPageSize` parameter in conjunction with the `listEntitiesPageToken` parameter to navigate through the pages.

  
listEntitiesPageToken | String | A page identifier (token) that lets you access a specific page. You can get the value of a page token from the `listEntitiesNextPageToken` output parameter. Because each page has a unique token, you have the flexibility to access any page you want in the result set. To understand the usage of this parameter, also read the description of the `listEntitiesNextPageToken` output parameter.  
listEntitiesSortByColumns | String array | The column name by which you want to sort the result set.  **Note:** You can sort the result set only by one column.  
  
### Output parameters

The following table describes the output parameters for the various entity operations.

Parameter name | Data type | Description  
---|---|---  
connectorOutputPayload | JSON | The output of an operation in JSON format.  
listEntitiesNextPageToken | String |  A system generated identifier for a page. You can think of the token as a pointer by which you can access a particular page of the result set. If you have broken down your result set into multiple pages by setting the `listEntitiesPageSize` parameter, you need a mechanism to navigate through the pages. The `listEntitiesNextPageToken` output parameter lets you do exactly that. Every time the **Connectors** task runs, the system generates a token for the next page and sets the `listEntitiesNextPageToken`'s value to the newly generated token. You can then use this token to access the next page in the result set. To access the next page, you must set the `listEntitiesPageToken` input parameter to the next page's token value. For example, consider you have set the `listEntitiesPageSize` parameter to 2. When the **Connectors** task runs for the first time, the `listEntitiesNextPageToken` is set to the `ChoKC2VtcGxveWVlX2lkEgkRAAAAAAAA8D8YDw==` token value. You can then set the `listEntitiesPageToken` input parameter to this token value to fetch the next page in the subsequent run of the **Connectors** task. If your result set has a large number of pages, you can consider using the [While Loop](https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task) task to get the next page and using the [Data Mapping](https://docs.cloud.google.com/application-integration/docs/data-mapping-task) task to automatically assign page token values to the `listEntitiesPageToken` input parameter after each run. Map `listEntitiesNextPageToken` from the last loop iteration to `listEntitiesPageToken` in the `LIST Operation` of the current loop iteration's **Connectors** task. The While Loop task ends when `listEntitiesNextPageToken` is `NULL`, which implies that there are no more pages.  
  
### Filter clause for entity operations

You can restrict the records that are processed by the **Connectors** task using the **Filter clause** variable, which is available as a **Task Input**. For example, in the case of a **delete** operation, you can add a filter clause to delete records with a specific `orderId`. 

A filter clause can be applied only for the following entity operations: 

  * List
  * Delete
  * Update



When you select any of these operations, the **Task Input** section of the **Connectors** task displays the **Filter clause** field automatically.

#### Add a filter clause

To add a filter clause, perform the following steps:

  1. Click the **Connectors** task element on the designer to view the **Connectors** task configuration pane.
  2. Expand the **Task Input** section and click the **filterClause(Connectors)** string variable. 

The **Configure Variable** dialog appears.

  3. Enter the filter clause (following the clause syntax) in the **Default Value** field. 
  4. Click **Save**.



#### Filter clause syntax and examples

A filter clause has the following format:
    
    
    FIELD_NAME CONDITION FILTER_VALUE

#### Examples

  * OwnerId = '0053t000007941XAAQ'

  * PoNumber < 2345

  * OrderNumber = 00110 AND StatusCode = 'Draft'

  * TotalAmount > 2500

  * ShippingPostalCode = 94043 OR ShippingPostalCode = 77002


**Important:** In the filter clause, specify string values within single quotes ( ' ) or double quotes ( " ), depending on the database you are using. For example, MySQL accepts both single and double quotes, whereas BigQuery accepts only single quotes. 

#### Use of variables in filter clause

You can't directly use an integration variable in a filter clause. If you want to use an integration variable, you must first configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task#configure-the-data-mapping-task) to create a mapping between the integration variable and the filter clause. 

The following table shows a sample mapping between an integration variable and the `filterClause(Connectors)` variable:

Input | Output | `PRIMARY_KEY_ID = ' .CONCAT(INTEGRATION_VARIABLE) .CONCAT(')` | `filterClause(Connectors)`  
---|---  
Where `**PRIMARY_KEY_ID = '**` is entered as a **Value** in the input row. 

* * *

### Action: Execute custom SQL query

To create a custom query, follow these steps: 

  1. Follow the detailed instructions to [ add a connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).
  2. When you [configure the connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-the-connectors-task), in the type of action you want to perform, select **Actions**.
  3. In the **Action** list, select **Execute custom query** , and then click **Done**. 

![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)

  4. Expand the **Task input** section, and then do the following: 
     1. In the **Timeout after** field, enter the number of seconds to wait till the query executes. 

Default value: `180` seconds.

     2. In the **Maximum number of rows** field, enter the maximum number of rows to be returned from the database.

Default value: `25`.

     3. To update the custom query, click **Edit Custom Script**. The **Script editor** dialog opens. 

![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)

     4. In the **Script editor** dialog, enter the SQL query and click **Save**. 

You can use a question mark (?) in a SQL statement to represent a single parameter that must be specified in the query parameters list. For example, the following SQL query selects all rows from the `Employees` table that matches the values specified for the `LastName` column: 
            
            SELECT * FROM Employees where LastName=?

**Note:** Data manipulation language (DML) and data definition language (DDL) statements are supported.
     5. If you've used question marks in your SQL query, you must add the parameter by clicking **\+ Add Parameter Name** for each question mark. While executing the integration, these parameters replace the question marks (?) in the SQL query sequentially. For example, if you have added three question marks (?), then you must add three parameters in order of sequence. 

![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)

To add query parameters, do the following:

        1. From the **Type** list, select the data type of the parameter.
        2. In the **Value** field, enter the value of the parameter.
        3. To add multiple parameters, click **\+ Add Query Parameter**.

The **Execute custom query** action does not support array variables.




### Schema refresh

All entities and actions have an associated schema. For example, an action schema includes parameter details such as parameter names and their corresponding data types. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To view the updated schema in your existing connector tasks, follow these steps: 

  1. In Integration Connectors, open the **Connection details** page of the connection, and then click **Refresh connection schema**.
  2. In Application Integration, you must reconfigure your existing connector task for the same connection.



## Inline connection creation

You can use the **Connectors task** to directly create a new connection in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/about-connectors). 

### Before you begin

  * [Add a Connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task)



### Create new connection

To create a new connection from Application Integration, perform the following steps:

  1. Click the **Connectors** task element on the designer to view the **Connectors** task configuration pane. 
  2. Click **Configure connector**. 

The **Connectors Task Editor** page appears.

  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: **Note:** The following instructions are the generic steps to create a connection. While the majority of the steps remain the same for all connection types, a few additional steps or details related to authentication might vary. 

We recommend that you also view the respective connection type documentation in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors).

     1. In the **Location** step, choose the location for the connection. 
        1. Click **Region** and select a location from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** step, provide details about the connection: 
        1. **Connector:** Select the type of connector that you want to create from the drop-down list. For information about the list of supported connectors, see [All Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors).
        2. **Connector version:** Choose an available version of the selected Connector type from the drop-down list. 
        3. **Connection Name:** Enter a name for the Connection instance. **Note:** Connection names must meet the following criteria: 
           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 63 characters.
        4. (Optional) Enter a **Description** for the connection instance.
        5. (Optional) Check **Enable Cloud Logging** to store the log data for the connection instance.
        6. **Service Account** : Select a service account that has the required roles.
        7. (Optional) Click **Advanced settings** to configure the connection node settings. 

For more information, see the respective connection documentation in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors). 

        8. (Optional) Click **\+ ADD LABEL** to add a label to the connection in the form of a key/value pair.
        9. Click **Next**.
     3. In the **Authentication** step, provide the authentication details for the connection. 
        1. The **Authentication** methods populated during this step are based on the type of connection being created. 

Different connection types use different authentication methods. For more information, see the **Configure authentication** section of the respective connection documentation in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors). 

        2. Click **Next**.
     4. **Review** : Review your connection and authentication details.
     5. Click **Create**.



* * *

## Best practices

  * For information about the usage limits that apply to the **Connectors** task, see [Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 
  * For information about how to troubleshoot a failed **Connectors** task, see [Use logs to troubleshoot and trace connector failures](https://docs.cloud.google.com/application-integration/docs/viewing-logs#use-logs-to-troubleshoot-and-trace-connector-failures).



## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Pricing

The Cloud Pub/Sub trigger and Salesforce trigger don't require you to create a [connector](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors). However, if you use the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) to connect to Pub/Sub or Salesforce, then you are billed for the connector usage. For information about pricing, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/docs/pricing).

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
