---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/stripe/configure/
title: Stripe \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:56.484962+00:00
---

# Stripe  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/stripe/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stripe

The Stripe connector lets you perform insert, delete, update, and read operations on Stripe dataset.

## Before you begin

Before using the Stripe connector, do the following tasks:

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

  * For information about creating a Stripe account, see [Create Stripe Account](https://hevodata.com/learn/stripe-dashboards/#b1) or [Create an account and learn how to start using Stripe.](https://docs.stripe.com/get-started)



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create New** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Stripe** from the drop down list of available Connectors.
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
     8. **Account Id** : The ID of the Account that you want to use. 
     9. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 

The Stripe connection supports the `API Key` type authentication. Select the Secret Manager secret for the API key from the **API Key** drop-down, and then select the corresponding secret version.

  6. Click **Next**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Stripe connection.

#### Live API Key connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Stripe  
Connector version | 1  
Connection Name | stripe-connection  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Account Id | ACCOUNT_ID  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Live APIKey | LIVE_API_KEY  
Secret version | 1  
  
For information about the Live API key, see [Live API Key](https://docs.stripe.com/keys).

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

## System limitations

The Stripe connector can process 6 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Stripe connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### ConfirmPaymentIntent action

This action confirms the payment intent.

#### Input parameters of the ConfirmPaymentIntent action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
PaymentIntentId | String | Yes | The PaymentIntent Id.  
  
For example on how to configure the `ConfirmPaymentIntent` action, see Action examples.

### CapturePaymentIntent action

This action captures the payment intent.

#### Input parameters of the CapturePaymentIntent action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
PaymentIntentId | String | Yes | The PaymentIntent Id.  
  
For example on how to configure the `ConfirmPaymentIntent` action, see Action examples.

### CancelPaymentIntent action

This action cancels the payment intent.

#### Input parameters of the CancelPaymentIntent action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
PaymentIntentId | String | Yes | The PaymentIntent Id.  
  
For example on how to configure the `CancelPaymentIntent` action, see Action examples.

### AttachPaymentMethodToCustomer action

This action attaches a PaymentMethod object to a customer.

#### Input parameters of the AttachPaymentMethodToCustomer action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
PaymentMethodId | String | Yes | The PaymentMethod Id.  
CustomerId | String | Yes | The Id of the customer to which to attach the PaymentMethod.  
  
For example on how to configure the `AttachPaymentMethodToCustomer` action, see Action examples.

### DetachPaymentMethodFromCustomer action

This action detaches a PaymentMethod object from a customer. After a PaymentMethod is detached, you can't re-attach it to the customer.

#### Input parameters of the DetachPaymentMethodFromCustomer action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
PaymentMethodId | String | Yes | The PaymentMethod Id.  
  
For example on how to configure the `DetachPaymentMethodFromCustomer` action, see Action examples.

### FinalizeInvoice action

This action finalizes the draft Invoice.

#### Input parameters of the Finalize Invoice action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
InvoiceId | String | Yes | The QuoInvoicete Id.  
  
For example on how to configure the `FinalizeInvoice` action, see Action examples.

### FinalizeQuote action

This action finalizes the drafted quote.

#### Input parameters of the FinalizeQuote action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
SouQuoteIdrcePath | String | Yes | The Quote Id.  
  
For example on how to configure the `FinalizeQuote` action, see Action examples.

###  AcceptQuote action

This action accepts the quote and generates an invoice for the accepted quote.

#### Input parameters of the AcceptQuote action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
QuoteId | String | Yes | The Quote Id.  
  
For example on how to configure the `AcceptQuote` action, see Action examples.

### CancelQuote action

This action cancels the drafted quote.

#### Input parameters of the CancelQuote action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
QuoteId | String | Yes | The Quote Id.  
  
For example on how to configure the `CancelQuote` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Confirm payment intent

This example shows how to confirm the intent of the specified payment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ConfirmPaymentIntent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ReturnUrl": "http://google.com/",
         "PaymentIntentId": "pi_3OggwFANHgX3SHp71AVrNtT3"
         }

If the action is successful, the `ConfirmPaymentIntent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "id": "pi_3OggwFANHgX3SHp71AVrNtT3",
    "object": "payment_intent",
    "amount": "33000",
    "amount_capturable": "0",
    "amount_received": "33000",
    "canceled_at": null,
    "cancellation_reason": null,
    "capture_method": "automatic",
    "client_secret": "pi_3OggwFANHgX3SHp71AVrNtT3_secret_YEfjrYL5uHQZrGCx66cJbedlA",
    "confirmation_method": "automatic",
    "created": "1707196279",
    "currency": "usd",
    "invoice": null,
    "last_payment_error": null,
    "latest_charge": "ch_3OggwFANHgX3SHp71uYScRAw",
    "level3": null,
    "livemode": "false",
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": "pm_1Oggu6ANHgX3SHp7zaRNKNVL",
    "payment_method_configuration_details": null,
    "payment_method_options.card.installments": null,
    "review": null,
    "setup_future_usage": null,
    "statement_descriptor_suffix": null,
    "status": "succeeded",
    "transfer_data": null,
    "transfer_group": null
    }]




### Example - Capture payment intent

This example shows how to capture the intent of the specified payment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CapturePaymentIntent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PaymentIntentId": "pi_3Ogh4sANHgX3SHp72YB0YotA"
         }

If the action is successful, the `CapturePaymentIntent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "id": "pi_3Ogh4sANHgX3SHp72YB0YotA",
    "object": "payment_intent",
    "amount": "33000",
    "amount_capturable": "0",
    "amount_received": "33000",
    "canceled_at": null,
    "cancellation_reason": null,
    "capture_method": "manual",
    "client_secret": "pi_3Ogh4sANHgX3SHp72YB0YotA_secret_jgqc0olEAOTcurQSDeQThJa3X",
    "confirmation_method": "automatic",
    "created": "1707196814",
    "currency": "usd",
    "customer": "cus_Okyi4e7t7BImUL",
    "description": null,
    "invoice": null,
    "last_payment_error": null,
    "latest_charge": "ch_3Ogh4sANHgX3SHp72uGBS7g4",
    "level3": null,
    "livemode": "false",
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": "pm_1Ogh4FANHgX3SHp7GBJJvfGR",
    "payment_method_configuration_details": null,
    "payment_method_options.card.installments": null,
    "payment_method_types": null,
    "processing": null,
    "receipt_email": null,
    "review": null,
    "statement_descriptor_suffix": null,
    "status": "succeeded",
    "transfer_data": null,
    "transfer_group": null
    }]




### Example - Cancel payment intent

This example shows how to cancel the intent of the specified payment.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelPaymentIntent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PaymentIntentId": "pi_3Ogh7HANHgX3SHp738skMdSQ"
         }

If the action is successful, the `CancelPaymentIntent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "id": "pi_3Ogh7HANHgX3SHp738skMdSQ",
    "object": "payment_intent",
    "amount": "33000",
    "amount_capturable": "0",
    "amount_received": "0",
    "canceled_at": "1707197160",
    "cancellation_reason": null,
    "capture_method": "manual",
    "client_secret": "pi_3Ogh7HANHgX3SHp738skMdSQ_secret_NqQsBexbdyk19ETdMnpQXF19j",
    "confirmation_method": "automatic",
    "created": "1707196963",
    "currency": "usd",
    "customer": "cus_Okyi4e7t7BImUL",
    "description": null,
    "invoice": null,
    "last_payment_error": null,
    "latest_charge": "ch_3Ogh7HANHgX3SHp73LJMZiy5",
    "level3": null,
    "livemode": "false",
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": "pm_1Ogh75ANHgX3SHp79MNT6IHs",
    "payment_method_configuration_details": null,
    "receipt_email": null,
    "review": null,
    "setup_future_usage": null,
    "shipping": null,
    "status": "canceled",
    "transfer_data": null,
    "transfer_group": null
    }]




### Example - Attach payment method to a customer

This example shows how to attach a payment method to the specified customer.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AttachPaymentMethodToCustomer` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PaymentMethodId": "pm_1OYm2nANHgX3SHp7ihGfm5U8",
         "CustomerId": "cus_PNX7n9xMDsMPH4"
         }

If the action is successful, the `AttachPaymentMethodToCustomer` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Detach payment method from a customer

This example shows how to detach a payment method from a customer.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DetachPaymentMethodFromCustomer` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PaymentMethodId": "pm_1OYm2nANHgX3SHp7ihGfm5U8"
         }

If the action is successful, the `DetachPaymentMethodFromCustomer` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Finalize an invoice 

This example shows how to finalize an invoice.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `FinalizeInvoice ` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "InvoiceId": "in_1OhnXRANHgX3SHp73ufStlXy"
         }

If the action is successful, the `Finalize Invoice ` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "id": "in_1OhnXRANHgX3SHp73ufStlXy",
    "object": "invoice",
    "account_country": "US",
    "account_name": "ZBTA_US_SAPDPA_TestAccount",
    "billing_reason": "manual",
    "charge": null,
    "collection_method": "charge_automatically",
    "created": "1707459976",
    "currency": "usd",
    "discounts": null,
    "due_date": null,
    "effective_at": "1707460034",
    "ending_balance": "0",
    "footer": null,
    "lines.data": null,
    "lines.has_more": "false",
    "lines.total_count": "0",
    "livemode": "false",
    "next_payment_attempt": null,
    "number": "F3C0E263-0004",
    "on_behalf_of": null,
    "paid": "true",
    "paid_out_of_band": "false",
    "payment_intent": null,
    }]




### Example - Finalize a quote 

This example shows how to finalize a quote.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `FinalizeQuote` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "QuoteId": "qt_1ObiPfANHgX3SHp7KT7DXaJe"
         }

If the action is successful, the `FinalizeQuote` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




### Example - Accept a quote 

This example shows how to accept a quote.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AcceptQuote` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "QuoteId": "qt_1ObmqKANHgX3SHp7ahHydwav"
         }

If the action is successful, the `AcceptQuote` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "InvoiceId": "in_1Obmr5ANHgX3SHp7HKi6bJDu",
    "Success": "true"
    }]




### Example - Cancel a quote 

This example shows how to cancel a quote.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelQuote` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "QuoteId": "qt_1Obmu3ANHgX3SHp7as57wBLf"
         }

If the action is successful, the `CancelQuote` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all customers

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` List.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a **filterClause**. You can use the **filterClause** to filter records based on the columns.




### Example - Get customer details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `cus_OxHsz0u5bCGWuy` in the **Default Value** field. 

Here, `cus_OxHsz0u5bCGWuy` is a unique record ID in the `Customer` entity.




### Example - Get payment intent details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PaymentIntent` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `pi_3OWzKoANHgX3SHp70nE8QKyn` in the **Default Value** field. 

Here, `pi_3OWzKoANHgX3SHp70nE8QKyn` is a unique record ID in the `PaymentIntent` entity.




### Example - Get balance transaction details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Balance Transaction` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `txn_1OAR1TANHgX3SHp7EeiZ` in the **Default Value** field. 

Here, `txn_1OAR1TANHgX3SHp7EeiZ` is a unique record ID in the `Balance Transaction` entity.




### Example - Get balance account details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Balance(PendingBalance, AvailableBalance)` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `bal_1OhnXRANHgX3SHp73ufS` in the **Default Value** field. 

Here, `bal_1OhnXRANHgX3SHp73ufS` is a unique record ID in the `Balance(PendingBalance, AvailableBalance)` entity.




### Example - Get refund details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refunds` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `re_3OU27zANHgX3SHp73nxqZMF2` in the **Default Value** field. 

Here, `re_3OU27zANHgX3SHp73nxqZMF2` is a unique record ID in the `Refunds` entity.




### Example - Get card details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `card_1O9kUPANHgX3SHp7Q8Hsk35F` in the **Default Value** field. 

Here, `card_1O9kUPANHgX3SHp7Q8Hsk35F` is a unique record ID in the `Cards` entity.




### Example - Get price details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Prices` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `price_1O9nTjANHgX3SHp7Zr552abc` in the **Default Value** field. 

Here, `price_1O9nTjANHgX3SHp7Zr552abc` is a unique record ID in the `Prices` entity.




### Example - Get invoice details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `in_1OA74xANHgX3SHp7YbC6x9R6` in the **Default Value** field. 

Here, `in_1OA74xANHgX3SHp7YbC6x9R6` is a unique record ID in the `Invoices` entity.




### Example - Get invoice item details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `InvoiceItems` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `ii_1OZAfAANHgX3SHp7xsd9o7Qm` in the **Default Value** field. 

Here, `ii_1OZAfAANHgX3SHp7xsd9o7Qm` is a unique record ID in the `InvoiceItems` entity.




### Example - Get quote details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Quotes` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `qt_1Oc2VaANHgX3SHp7PaM9Ph9o` in the **Default Value** field. 

Here, `qt_1Oc2VaANHgX3SHp7PaM9Ph9o` is a unique record ID in the `Quotes` entity.




### Example - Get account details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `acct_1OZBcsQbE7mBlkdN` in the **Default Value** field. 

Here, `acct_1OZBcsQbE7mBlkdN` is a unique record ID in the `Accounts` entity.




### Example - Create a payment intent (Entity Operation)

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PaymentIntent` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PaymentMethod": "pm_1OXN5YANHgX3SHp7Q5Y0rb39",
           "Currency": "usd",
           "Amount": 1500.0
         }
         

If the integration is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "pi_3OXN69ANHgX3SHp70tgsxkuR"
         }
         




### Example - Update payment method details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PaymentMethods` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Card": {
             "ExpMonth": 12,
             "ExpYear": 2027
           }
         }
         

  5. Click **entityId** , and then enter `pm_1OXN5YANHgX3SHp7Q5Y0rb39` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` variable will contain:
         
         {
           "Id": "pm_1OXN5YANHgX3SHp7Q5Y0rb39"
         }
         




### Example - Update bank account details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Bank Accounts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "AccountHolderName": "Jane Doe"
         }
         

  5. Click **entityId** , and then enter `ba_1O9kUPANHgX3SHp7` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` variable will contain:
         
         {
           "Id": "ba_1O9kUPANHgX3SHp7"
         }
         




### Example - Update refund details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refunds` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Metadata": {
             "Reason": "Customer request"
           }
         }
         

  5. Click **entityId** , and then enter `re_3OU27zANHgX3SHp73nxqZMF2` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` variable will contain:
         
         {
           "Id": "re_3OU27zANHgX3SHp73nxqZMF2"
         }
         




### Example - Delete a card

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Click **entityId** and then enter `card_1O9kUPANHgX3SHp7Q8Hsk35F` in the **Default Value** field. 

Instead of specifying the **entityId** , you can set the **filterClause** to `id='card_1O9kUPANHgX3SHp7Q8Hsk35F'`.




### Example - Delete an invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Click **entityId** and then enter `in_1OA74xANHgX3SHp7YbC6x9R6` in the **Default Value** field. 

Instead of specifying the **entityId** , you can set the **filterClause** to `id='in_1OA74xANHgX3SHp7YbC6x9R6'`.




### Example - Delete an invoice item

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `InvoiceItems` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Click **entityId** and then enter `ii_1OZAfAANHgX3SHp7xsd9o7Qm` in the **Default Value** field. 

Instead of specifying the **entityId** , you can set the **filterClause** to `id='ii_1OZAfAANHgX3SHp7xsd9o7Qm'`.




### Example - Delete a quote

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Quotes` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Click **entityId** and then enter `qt_1Oc2VaANHgX3SHp7PaM9Ph9o` in the **Default Value** field. 

Instead of specifying the **entityId** , you can set the **filterClause** to `id='qt_1Oc2VaANHgX3SHp7PaM9Ph9o'`.




### Example - Get customer details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `cus_OxHsz0u5bCGWuy` in the **Default Value** field. 

Here, `cus_OxHsz0u5bCGWuy` is a unique record ID in the `Customer` entity.




### Example - Create a customer

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "abc"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "cus_OxIqiMh1W335rE"
         }
         
         




### Example - Create a refund

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refunds` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Charge": "ch_3OU27zANHgX3SHp73HqiDsh3",
           "Amount": 10.0
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "re_3OU27zANHgX3SHp73nxqZMF2"
         }
         




### Example - Create a card

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "CustomerId": "cus_OmptWC2kb2264y",
           "Token": "tok_1O9kUPANHgX3SHp7WcrPumVI"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "card_1O9kUPANHgX3SHp7Q8Hsk35F",
           "CustomerId": "cus_OmptWC2kb2264y"
         }
         




### Example - Create a price

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Prices` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Currency": "usd",
           "Product": "prod_OlNe53LwNydXSx",
           "UnitAmount": 1200.0
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "price_1OAR1TANHgX3SHp7EeiZTW9h"
         }
         




### Example - Create an invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "CustomerId": "cus_OhvXm2EI9bsFyN"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "in_1OXR9gANHgX3SHp7wHdnEe7U"
         }
         




### Example - Create an invoice item

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `InvoiceItems` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Customer": "cus_OksFS6F8HS7o5O",
           "Currency": "usd",
           "Amount": 1000.0
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "ii_1OZAfAANHgX3SHp7xsd9o7Qm"
         }
         




### Example - Create a quote

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Quotes` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "CustomerId": "cus_POGecLC3f3hwk2"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "qt_1OZU92ANHgX3SHp75zJzMSvC"
         }
         




### Example - Create an account

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Type": "standard"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "acct_1OZBcsQbE7mBlkdN"
         }
         




### Example - Create a payment intent

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PaymentIntent` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "PaymentMethod": "pm_1OXN5YANHgX3SHp7Q5Y0rb39",
         "Currency": "usd",
         "Amount": 1500.0
         }
         

If the integration is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Id": "pi_3OXN69ANHgX3SHp70tgsxkuR"
         }




### Example - Update customer details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "Charlie"
         }

  5. Click **entityId** , and then enter `cus_OxHsz0u5bCGWuy` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": "cus_OxHsz0u5bCGWuy"
         }




### Example - Update a payment intent

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PaymentIntent` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "Payment Intent"
         }
         

  5. Set the entityId to pi_3OWzKoANHgX3SHp70nE8QKyn. To set the entityId, click **entityId** , and then enter `pi_3OWzKoANHgX3SHp70nE8QKyn` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'pi_3OWzKoANHgX3SHp70nE8QKyn'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "pi_3OWzKoANHgX3SHp70nE8QKyn"
         }
         




### Example - Update card details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Cards` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "AddressCountry": "US",
           "Id": "card_1O9kUPANHgX3SHp7Q8Hsk35F",
           "CustomerId": "cus_OmptWC2kb2264y"
         }
         

  5. Set the filterClause to `CustomerId = 'cus_OmptWC2kb2264y'` and `Id = 'card_1O9kUPANHgX3SHp7Q8Hsk35F'`. To set the filterClause, click **filterClause** and then enter `CustomerId = 'cus_OmptWC2kb2264y' and Id = 'card_1O9kUPANHgX3SHp7Q8Hsk35F'` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "result": [{
             "Id": "card_1O9kUPANHgX3SHp7Q8Hsk35F",
             "CustomerId": "cus_OmptWC2kb2264y"
           }]
         } 
         




### Example - Update price details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Prices` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Nickname": "Price Update"
         }
         

  5. Set the entityId to price_1O9nTjANHgX3SHp7Zr552abc. To set the entityId, click **entityId** and then enter `price_1O9nTjANHgX3SHp7Zr552abc` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'price_1O9nTjANHgX3SHp7Zr552abc'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
          "Id": "price_1O9nTjANHgX3SHp7Zr552abc"
         }
         




### Example - Update an invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Description": "Invoice for car"
         }
         

  5. Set the entityId to in_1OA74xANHgX3SHp7YbC6x9R6. To set the entityId, click **entityId** and then enter `in_1OA74xANHgX3SHp7YbC6x9R6` in the **Default Value** field. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'in_1OA74xANHgX3SHp7YbC6x9R6'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "in_1OA74xANHgX3SHp7YbC6x9R6"
         }
         




### Example - Update an invoice item

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `InvoiceItems` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Quantity": 3.0
         }
         

  5. Set the entityId to ii_1OZAfAANHgX3SHp7xsd9o7Qm. To set the entityId, click **entityId** and then enter `ii_1OZAfAANHgX3SHp7xsd9o7Qm` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "ii_1OZAfAANHgX3SHp7xsd9o7Qm"
         }
         




### Example - Update a quote

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Quotes` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "CustomerId": "cus_PQuEGGfutajbAs"
         }
         

  5. Set the entityId to qt_1Oc2VaANHgX3SHp7PaM9Ph9o. To set the entityId, click **entityId** and then enter `qt_1Oc2VaANHgX3SHp7PaM9Ph9o` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "qt_1Oc2VaANHgX3SHp7PaM9Ph9o"
         }
         




### Example - Update account details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "BusinessProfileName": "StagingName"
         }
         

  5. Set the entityId to acct_1OZBcsQbE7mBlkdN. To set the entityId, click **entityId** and then enter `acct_1OZBcsQbE7mBlkdN` in the **Default Value** field. 

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "acct_1OZBcsQbE7mBlkdN"
         }
         




### Example - Delete a customer

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customer` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Click **entityId** and then enter `cus_OxIqiMh1W335rE` in the **Default Value** field. 

If entity has two composite business or primary keys, instead of specifying the **entityId** , you can set the **filterClause** to `id='cus_OxIqiMh1W335rE'`.




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
account_id | STRING | False | The ID of the Account that you want to use.   
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
  
## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
