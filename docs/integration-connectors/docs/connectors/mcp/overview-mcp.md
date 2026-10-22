---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/overview-mcp/
title: MCP connector \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:32.521631+00:00
---

# MCP connector  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/overview-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# MCP connector

The Model Context Protocol (MCP) connector lets you create and configure an MCP connection in Integration Connectors. You can use this connection in your business applications to securely exchange data and perform operations with MCP. 

For the list of supported entities and operations, see Entity operation examples. For information about the supported connector-specific actions, see Actions. 

All connections in Integration Connectors provide a layer of abstraction for the underlying service objects. These objects are exposed as manageable [entities](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action), letting you perform standard [operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) or use connector-specific [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). 

## MCP connector versions

The MCP connector supports two versions:

  * **MCP v1** : Use this connector version to access the MCP v1 API.
  * **MCP v2** : Use this connector version to access the MCP v2 API.



For information about creating a MCP connection, see [Create and configure a MCP connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/configure-mcp). 

## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## Supported entities and operations

The MCP connector supports entities and operations, with the specific ones available depending on the tool connected through MCP. 

### Entity operation examples

This section provides examples of entity operations for different tools.

#### List Jira Issues entity

This example lists all **Issues** in the **Issues** entity using a Jira MCP connection.

  1. In the **Configure Connector Task** window, click **Entities**.
  2. Select **Issues** from the **Entity** list.
  3. Select the **List** operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {
               "operation": "LIST_ENTITIES",
               "connection_name": "projects/YOUR_PROJECT_ID/locations/YOUR_LOCATION/connections/YOUR_JIRA_CONNECTION_NAME",
               "service_name": "projects/YOUR_TENANT_PROJECT_ID/locations/YOUR_LOCATION/namespaces/cloudrun/services/YOUR_RUNTIME_SERVICE",
               "host": "https://YOUR_TENANT_PROJECT_ID-YOUR_LOCATION.us-west1-runtime-connectors-google.com",
               "entity": "Issues",
               "entity_id": "Issues",
               "page_token": ""
             }




#### List all requests

This example lists all **Requests** in the **Requests** entity.

  1. In the **Configure Connector Task** window, click **Entities**.
  2. Select **Requests** from the **Entity** list.
  3. Select the **List** operation, and then click **Done**.



#### Get a user by ID

This example gets the user with **AccountId** as `6035864ce2020c0070b5285b` from the **Users** entity. **`AccountId`** is the primary key for the **Users** entity. To get a specific entity, use the **List** operation with a `filterClause` on the primary key, as the **Get** operation isn't supported for this entity.

  1. In the **Configure Connector Task** window, click **Entities**.
  2. Select **Users** from the **Entity** list. 
  3. Select the **List** operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **filterClause** and then enter `AccountId`=`6035864ce2020c0070b5285b` in the **Default Value** field.



## Actions

The MCP connector provides various actions, with the specific ones available depending on the tool connected through MCP. 

### Action examples

This section describes how to perform some of the actions available through the MCP connector for different tools.

#### Jira actions: Get issues

This example demonstrates how to list Jira issues using an MCP connection configured for Jira.

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the **get_issues** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {
             "issue_ids": ["YOUR_ISSUE_ID_1", "YOUR_ISSUE_ID_2"]
           }




#### Linear actions: List issues

This example demonstrates how to list issues in Linear using an MCP connection configured for Linear.

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the **list_issues** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {
             "limit": 50
           }




#### Sentry Actions: Whoami

This example demonstrates how to get user info from Sentry using an MCP connection configured for Sentry.

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the **whoami** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {
             "name": "example-org"
           }




#### Find organizations

This example demonstrates how to find organizations in Sentry using an MCP connection configured for Sentry.

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the **find_organizations** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {}




#### Intercom Actions: Search conversations

This example demonstrates how to search for conversation details in Intercom using an MCP connection configured for Intercom.

  1. In the **Configure connector task** dialog, click **Actions**.
  2. Select the **search** action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click **connectorInputPayload** and then enter a value similar to the following in the **Default Value** field: 
         
         {
             "query": "object_type:conversations state:open created_at:gt:2024-01-01"
           }




## System limitations

The MCP connector has system limitations that may vary based on the specific tool being connected. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
