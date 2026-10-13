---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/shopify/configure/
title: Shopify \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:51.027246+00:00
---

# Shopify  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/shopify/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Shopify

The Shopify connector lets you perform insert, delete, update, and read operations on Shopify.

## Supported versions

This connector models the [Shopify Admin APIs](https://shopify.dev/docs/api/admin) as a relational database.

## Before you begin

Before using the Shopify connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Shopify** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **Max Points Per Call** : Specifies how many points a call will cost. 
     9. **Schema** : Specify the Shopify server version to connect with. When the `Schema` field is set to `GraphQL`, all entities are treated as read-only Views. To perform Create, Update, or Delete operations, you must set the `Schema` field to `REST`. 
     10. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
        * **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
          * **Basic** : Basic HTTP authentication.
          * **Digest** : Digest HTTP authentication.
        * **Proxy User** : A user name to be used to authenticate with the proxy server. 
        * **Proxy Password** : The Secret manager secret of the user's password. 
        * **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. The following authentication types are supported: 
          * **Auto** : Default setting. If the URL is an HTTPS URL, then the Tunnel option is used. If the URL is an HTTP URL, then the NEVER option is used.
          * **Always** : The connection is always SSL enabled.
          * **Never** : The connection is not SSL enabled.
          * **Tunnel** : The connection is through a tunneling proxy. The proxy server opens a connection to the remote host and traffic flows back and forth through the proxy.
        * In the **Proxy Server** section, enter details of the proxy server. 
          1. Click **\+ Add destination**.
          2. Select a **Destination Type**. 
             * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish a private connection to your backend system, do the following:

               * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
               * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
     11. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     12. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, specify the **Access Token** details.
* Click **NEXT**.
* **Review** : Review your connection and authentication details.
* Click **Create**.

### Create access token and API credentials

  1. Sign in to the Shopify account.
  2. In the Shopify developer portal, click **Settings**.
  3. Select **Apps and sales channels > Develop apps**.
  4. Click **Create an app**.
  5. In the dialog that appears, enter the name of your app and click **Create**.
  6. In the **Overview** page, click **Configure Admin API scopes** and select the access permissions for your app.
  7. Select the permissions required for your specific integration.

> **Note on Permissions:** Shopify scopes are modular. You should only enable the scopes that match the data your integration needs to access. For example: 
>      * **Orders & Fulfillment:** `read_orders`, `write_orders`, `read_fulfillments`.
>      * **Inventory & Products:** `read_products`, `read_inventory`.
>      * **Customer Data:** `read_customers`.

**Minimum Scopes:** If you are unsure which specific actions you will be performing, we recommend starting with `read_products` and `read_orders`.

**(Optional)** If you want to ensure all features of this integration work without permission errors, you may select the following comprehensive list:  


     * `read_assigned_fulfillment_orders`
     * `write_assigned_fulfillment_orders`
     * `read_content`
     * `write_content`
     * `read_customers`
     * `write_customers`
     * `read_draft_orders`
     * `write_draft_orders`
     * `read_fulfillments`
     * `write_fulfillments`
     * `read_gift_cards`
     * `write_gift_cards`
     * `read_inventory`
     * `write_inventory`
     * `read_marketing_events`
     * `write_marketing_events`
     * `read_orders`
     * `write_orders`
     * `read_price_rules`
     * `write_price_rules`
     * `read_product_listings`
     * `write_product_listings`
     * `read_products`
     * `write_products`
     * `read_reports`
     * `write_reports`
     * `read_script_tags`
     * `write_script_tags`
     * `read_shopify_payments_payouts`
     * `read_themes`
     * `write_themes`
  8. Click **Save**.
  9. In the **API Credentials** page, select **Install app**.
  10. In the dialog that appears, click **Install**.
  11. In the **API Credentials** page, select **Reveal token once** and copy the **Admin API access token**.
  12. **Secure your credentials:** Create a secret in your **GCP Secret Manager** to store the **Admin API access token**. Note the secret's resource path for verification.
  13. **Admin Verification:** For connectors utilizing tenant projects, Admins can verify the `access_token` versioning in the Configuration Map using the following JSON: 
         
         { "config_variables": { "schema": "REST" }, "destination_configs": { "shop_url": "https://YOUR_STORE.myshopify.com" }, "auth_config": { "access_token": "projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION" } } 




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

## Entity operation examples

### Example - List all products

This example lists all the records in the `Products` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Products` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get customer details

This example gets the details of the specified customer from the `Customers` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Enter the entity ID of the customer whose details you want to fetch. 

In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `365009521884E12` in the **Default Value** field.

You can also use the **filterClause** field to perform Get and Delete operations.




### Example - Delete an order record

This example deletes the specified order from the `Order` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Order` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Enter the entity ID of the order that you want to delete. 

In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `475009571483E15` in the **Default Value** field.




### Example - Add a customer

This example adds the specified customer to the `Customer` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FirstName": "Test",
         "LastName": "Customer5"
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 6448083206296
         }




### Example - Create a record in DiscountCode

This example creates a new record in the `DiscountCode` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DiscountCode` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PriceRuleId": 1.394097291568E12,
         "Code": "FREESHIP2025798"
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 1.97836790828E13,
         "PriceRuleId": null
         }




### Example - Create a record in Pricerule

This example creates a new record in the `Pricerule` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pricerule` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Id": 7.13459564696E11,
         "AllocationMethod": "each",
         "CustomerSelection": "all",
         "TargetType": "line_item",
         "UsageLimit": 100.0,
         "Title": "DP_PriceRule"
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 197836790834,
         "PriceRuleId": null
         }




### Example - Create a record in ProductVariant

This example creates a new record in the `ProductVariant` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ProductVariant` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Id": 1070325065,
         "ProductId": 7652181016728,
         "ImageId": null,
         "Price": 1,
         "CompareAtPrice": null,
         "Title": "Yellow",
         "Barcode": null,
         "FulfillmentService": "manual",
         "InventoryManagement": "shopify",
         "InventoryPolicy": "deny",
         "InventoryQuantity": 1070325069,
         "Option1": "Yellow",
         "Option2": null,
         "Option3": null,
         "Position": 5,
         "Sku": "",
         "Taxable": true
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 42711984373912
         }




### Example - Create a record in Order

This example creates a new order in the `Order` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Order` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Currency": "USD",
           "Email": "john.doe@example.com",
           "LineAggregate": "[{\"variant_id\": 34601695641752, \"quantity\": 1, \"price\": \"50.00\"}]",
           "FinancialStatus": "paid"
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "OrderId": 39121984427137
         }




### Example - Create a record in Refund

This example creates a refund in the `Refund` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refund` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "OrderId": 2650438107288,
           "OrderTransactionAggregate": "[{\"amount\": \"15.00\", \"kind\": \"refund\", \"status\": \"success\"}]"
         }

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "OrderId": 2650438107288
         }




### Example - Update customer details

This example updates the details of the specified customer in the `Customer` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FirstName": "Test",
         "LastName": "Customer2"
         }

  5. Enter the entity ID of the customer that you want to delete. 

In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `648400653532` in the **Default Value** field.

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `648400653532`.

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 648400653532
         }




### Example - Update a record in ProductVariant

This example updates a record in the `ProductVariant` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ProductVariant` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ProductId": 7.652181016728E12,
         "ImageId": null,
         "Price": 200.0,
         "CompareAtPrice": null,
         "Title": "Yellow Updated",
         "Barcode": null,
         "FulfillmentService": "manual",
         "InventoryManagement": "shopify",
         "InventoryQuantity": 1.070325069E9,
         "Option1": "Yellow new",
         "Option2": null,
         "Option3": null,
         "Position": 5.0,
         "Sku": "",
         "Taxable": true
         }

  5. Specify the entity ID of the record to update. 

To set the entity ID, click **entityId** and then enter `34601602744472` in the **Default Value** field.

Running this example, returns a response similar to the following in your connector task's `connectorOutputPayload` output variable:
         
         {
         "Id": 2484258073471
         }




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
max_points_per_call | STRING | False | Specifies how many points a call will cost.   
schema_v23 | ENUM | False | Specify the Shopify server version to connect with. Supported values are: REST-2023-04, REST-2023-07, GRAPHQL-2023-04, GRAPHQL-2023-07  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Shopify connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
