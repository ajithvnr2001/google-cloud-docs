---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/square/configure/
title: Square \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:56.600051+00:00
---

# Square  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/square/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Square

The Square connector lets you perform insert, delete, update, and read actions on the Square data.

## Supported versions

This connector supports Square version 1.0.

## Before you begin

Before using the Square connector, do the following tasks:

  * In your Google Cloud project: 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

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
     1. **Connector** : Select **Square** from the list of available connectors.
     2. **Connector version** : Select the connector version from the list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lowercase.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. **Description** : Enter a description for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. **Schema** : Specify the schema for the connection, such as v1 or v2.
     8. **Use Sandbox** : Specify whether to use the sandbox environment for the connection.
     9. **Location Id** : Specify the location ID for the connection.
     10. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     11. **\+ ADD LABEL** Click this to add a label to the connection in the form of a key/value pair.
     12. Click **NEXT**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Square connection:

        * OAuth 2.0 - Authorization Code
        * Personal Access Token

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - Authorization Code**
    * **Client ID** : Enter the client ID to use for the connection.
    * **Scopes** : Enter a comma-separated list of desired scopes.
    * **Client Secret** : Enter the client secret to use for the Square connection.
    * **Secret version** : Select the secret version for the secret selected above.
    * **Authorization URL** : Enter the authorization URL that was generated while creating the client.
    * **Enable Authentication Override** : Specify whether to enable override authentication for the connection.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

  * **Personal Access Token**
    * **Personal Access Token** : Enter the personal access token to use for the connection.
    * **Secret version** : Select the secret version for the secret selected above.
    * **Enable Authentication Override** : Specify whether to enable override authentication for the connection.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - Authorization code connection type

Fieldname | Details  
---|---  
Location | us-central1  
Connector | Square  
Connector version | 1  
Connection Name | square-oauth-ai   
Enable Cloud Logging | true  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Schema | v2  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization Code  
Client Id | CLIENT_ID  
Scopes | BANK_ACCOUNTS_READ, CASH_DRAWER_READ, CUSTOMERS_READ, CUSTOMERS_WRITE, DEVICE_CREDENTIAL_MANAGEMENT, EMPLOYEES_READ, EMPLOYEES_WRITE, INVENTORY_READ, INVENTORY_WRITE, ITEMS_READ, ITEMS_WRITE, LOYALTY_READ, LOYALTY_WRITE, MERCHANT_PROFILE_READ, ORDERS_READ, ORDERS_WRITE, PAYMENTS_READ, PAYMENTS_WRITE, PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS, PAYMENTS_WRITE_IN_PERSON, SETTLEMENTS_READ, TIMECARDS_READ, TIMECARDS_WRITE, TIMECARDS_SETTINGS_READ, TIMECARDS_SETTINGS_WRITE, APPOINTMENTS_READ, APPOINTMENTS_WRITE, APPOINTMENTS_BUSINESS_SETTINGS_READ, INVOICES_READ, INVOICES_WRITE, SUBSCRIPTIONS_READ, SUBSCRIPTIONS_WRITE, DISPUTES_READ, DISPUTES_WRITE, GIFTCARDS_READ, GIFTCARDS_WRITE, ONLINE_STORE_SNIPPETS_WRITE, ONLINE_STORE_SNIPPETS_READ, ONLINE_STORE_SITE_READ, PAYMENTS_WRITE_SHARED_ONFILE, APPOINTMENTS_ALL_READ, APPOINTMENTS_ALL_WRITE, MERCHANT_PROFILE_WRITE, VENDOR_READ, VENDOR_WRITE, PAYOUTS_READ, DEVICES_READ   
Client Secret | CLIENT_SECRET  
Secret version | 1  
Authorization URL | https://connect.squareup.com/oauth2/authorize  
  
### Personal access token connection type

Fieldname | Details  
---|---  
Location | asia-east1  
Connector | Square  
Connector version | 1  
Connection Name | square-pat-prod-conn   
Enable Cloud Logging | true  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Schema | v2  
Use Sandbox | true  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Personal Access Token  
Personal Access Token | PERSONAL_ACCESS_TOKEN  
Secret version | 1  
  
## System limitations

The Square connector can process a maximum of 16 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Square connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section shows how to perform some of the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### CancelPayment action

This action cancels a payment.

#### Input parameters of the CancelPayment action

Parameter name | Data type | Required | Description  
---|---|---|---  
PaymentId | String | True | The ID of the payment to cancel.  
  
For an example about how to configure the `CancelPayment` action, see Examples.

### CompletePayment action

This action completes a payment.

#### Input parameters of the CompletePayment action

Parameter name | Data type | Required | Description  
---|---|---|---  
PaymentId | String | True | The ID of the payment to complete.  
  
For an example about how to configure the `CompletePayment` action, see Examples.

### CancelPaymentByIdempotencyKey action

This action cancels a payment using its idempotency key.

#### Input parameters of the CancelPaymentByIdempotencyKey action

Parameter name | Data type | Required | Description  
---|---|---|---  
IdempotencyKey | String | True | The idempotency key used to identify the payment to cancel.  
  
For an example about how to configure the `CancelPaymentByIdempotencyKey` action, see Examples.

### CancelInvoice action

This action cancels an invoice.

#### Input parameters of the CancelInvoice action

Parameter name | Data type | Required | Description  
---|---|---|---  
InvoiceId | String | True | The ID of the invoice to cancel.  
InvoiceVersion | String | True | The version of the invoice to cancel.  
  
For an example about how to configure the `CancelInvoice` action, see Examples.

### PublishInvoice action

This action publishes an invoice.

#### Input parameters of the PublishInvoice action

Parameter name | Data type | Required | Description  
---|---|---|---  
InvoiceId | String | True | The ID of the invoice to publish.  
InvoiceVersion | Int32 | True | The version of the invoice to publish. This must match the current version of the invoice; otherwise, the request is rejected.  
  
For an example about how to configure the `PublishInvoice` action, see Examples.

### DeleteInvoiceAttachment action

This action deletes an invoice attachment.

#### Input parameters of the DeleteInvoiceAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
InvoiceId | String | True | The ID of the invoice that contains the attachment to delete.  
AttachmentId | String | True | The ID of the attachment to delete.  
  
For an example about how to configure the `DeleteInvoiceAttachment` action, see Examples.

### CancelSubscriptions action

This action cancels a subscription.

#### Input parameters of the CancelSubscriptions action

Parameter name | Data type | Required | Description  
---|---|---|---  
Id | String | True | The ID of the subscription to cancel.  
  
For an example about how to configure the `CancelSubscriptions` action, see Examples.

## Action examples

This section shows how to perform some of the action examples in this connector.

### Example - Cancel a payment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelPayment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PaymentId": "P7eOGiuAYV8CfcLxSXHuUsedBRMZY"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": true
      }
    ]
    




### Example - Complete a payment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CompletePayment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PaymentId": "JiZRuypGuu4B7OOoPhL3kYg9YZaZY"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true
    }] 
    




### Example - Cancel a payment using an idempotency key

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelPaymentByIdempotencyKey` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "IdempotencyKey": "8b3e387b-a4d8-480c-a871-1c5fdcfd82cd"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true
    }]
    




### Example - Cancel an invoice

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelInvoice` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "InvoiceId": "inv:0-ChCdONOpvkOxnZ64VuiDwLQ4EPgO",
         "InvoiceVersion": "2"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "invoice_id": "inv:0-ChCdONOpvkOxnZ64VuiDwLQ4EPgO",
        "invoice_version": "3",
        "invoice_location_id": "LSHW80WV4KB06",
        "invoice_order_id": "dfChzstnmPfPGdEIFQ6ulRFdOf4F",
        "invoice_payment_requests_uid": "28ff79b1-16de-4c82-bb88-3f4e02be68c5",
        "invoice_payment_requests_request_type": "BALANCE",
        "invoice_payment_requests_due_date": "2025-11-26",
        "invoice_payment_requests_tipping_enabled": "true",
        "invoice_payment_requests_computed_amount_money_amount": "60",
        "invoice_payment_requests_computed_amount_money_currency": "USD",
        "invoice_payment_requests_total_completed_amount_money_amount": "0",
        "invoice_payment_requests_total_completed_amount_money_currency": "USD",
        "invoice_payment_requests_reminders_uid": "ae64a254-d516-4014-aea2-5fee42ec7457",
        "invoice_payment_requests_reminders_relative_scheduled_days": "1",
        "invoice_payment_requests_reminders_message": "Your invoice is almost due",
        "invoice_payment_requests_reminders_status": "NOT_APPLICABLE",
        "invoice_payment_requests_automatic_payment_source": "NONE",
        "invoice_primary_recipient_customer_id": "5BH2SYXX0G87A7NBYZKKJJTDVG",
        "invoice_primary_recipient_given_name": "Postman",
        "invoice_primary_recipient_family_name": "Test",
        "invoice_primary_recipient_email_address": "Charlie.Cruz@altostrat.com",
        "invoice_primary_recipient_phone_number": "1-212-555-4240",
        "invoice_primary_recipient_company_name": "Square",
        "invoice_primary_recipient_address_address_line_1": "500 Electric Ave",
        "invoice_primary_recipient_address_address_line_2": "Suite 600",
        "invoice_primary_recipient_address_locality": "New York",
        "invoice_primary_recipient_address_administrative_district_level_1": "NY",
        "invoice_primary_recipient_address_postal_code": "10003",
        "invoice_primary_recipient_address_country": "US",
        "invoice_invoice_number": "00000001",
        "invoice_title": "Invoice Update",
        "invoice_description": "Updating invoice",
        "invoice_public_url": "https://app.squareupsandbox.com/pay-invoice/invtmp:8779596a-2c13-4cf0-ab21-05eb6a1d03ef",
        "invoice_status": "CANCELED",
        "invoice_timezone": "UTC",
        "invoice_created_at": "2025-06-11T09:19:10Z",
        "invoice_updated_at": "2025-06-11T09:57:24Z",
        "invoice_accepted_payment_methods_card": "true",
        "invoice_accepted_payment_methods_square_gift_card": "true",
        "invoice_accepted_payment_methods_bank_account": "true",
        "invoice_accepted_payment_methods_buy_now_pay_later": "true",
        "invoice_accepted_payment_methods_cash_app_pay": "true",
        "invoice_delivery_method": "EMAIL",
        "invoice_store_payment_method_enabled": "true",
        "success": true
      }
    ]
    




### Example - Publish an invoice

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `PublishInvoice` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "InvoiceId": "inv:0-ChCdONOpvkOxnZ64VuiDwLQ4EPgO",
           "InvoiceVersion": 1
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "invoice_id": "inv:0-ChCdONOpvkOxnZ64VuiDwLQ4EPgO",
        "invoice_version": "2",
        "invoice_location_id": "LSHW80WV4KB06",
        "invoice_order_id": "dfChzstnmPfPGdEIFQ6ulRFdOf4F",
        "invoice_payment_requests_uid": "28ff79b1-16de-4c82-bb88-3f4e02be68c5",
        "invoice_payment_requests_request_type": "BALANCE",
        "invoice_payment_requests_due_date": "2025-11-26",
        "invoice_payment_requests_tipping_enabled": "true",
        "invoice_payment_requests_computed_amount_money_amount": "60",
        "invoice_payment_requests_computed_amount_money_currency": "USD",
        "invoice_payment_requests_total_completed_amount_money_amount": "0",
        "invoice_payment_requests_total_completed_amount_money_currency": "USD",
        "invoice_payment_requests_reminders_uid": "ae64a254-d516-4014-aea2-5fee42ec7457",
        "invoice_payment_requests_reminders_relative_scheduled_days": "1",
        "invoice_payment_requests_reminders_message": "Your invoice is almost due",
        "invoice_payment_requests_reminders_status": "PENDING",
        "invoice_payment_requests_automatic_payment_source": "NONE",
        "invoice_primary_recipient_customer_id": "5BH2SYXX0G87A7NBYZKKJJTDVG",
        "invoice_primary_recipient_given_name": "Postman",
        "invoice_primary_recipient_family_name": "Test",
        "invoice_primary_recipient_email_address": "Charlie.Cruz@altostrat.com",
        "invoice_primary_recipient_phone_number": "1-212-555-4240",
        "invoice_primary_recipient_company_name": "Square",
        "invoice_primary_recipient_address_address_line_1": "500 Electric Ave",
        "invoice_primary_recipient_address_address_line_2": "Suite 600",
        "invoice_primary_recipient_address_locality": "New York",
        "invoice_primary_recipient_address_administrative_district_level_1": "NY",
        "invoice_primary_recipient_address_postal_code": "10003",
        "invoice_primary_recipient_address_country": "US",
        "invoice_invoice_number": "00000001",
        "invoice_title": "Invoice Update",
        "invoice_description": "Updating invoice",
        "invoice_public_url": "https://app.squareupsandbox.com/pay-invoice/invtmp:8779596a-2c13-4cf0-ab21-05eb6a1d03ef",
        "invoice_next_payment_amount_money_amount": "60",
        "invoice_next_payment_amount_money_currency": "USD",
        "invoice_status": "UNPAID",
        "invoice_timezone": "UTC",
        "invoice_created_at": "2025-06-11T09:19:10Z",
        "invoice_updated_at": "2025-06-11T09:52:13Z",
        "invoice_accepted_payment_methods_card": "true",
        "invoice_accepted_payment_methods_square_gift_card": "true",
        "invoice_accepted_payment_methods_bank_account": "true",
        "invoice_accepted_payment_methods_buy_now_pay_later": "true",
        "invoice_accepted_payment_methods_cash_app_pay": "true",
        "invoice_delivery_method": "EMAIL",
        "invoice_store_payment_method_enabled": "true",
        "success": true
      }
    ]
    




### Example - Delete an invoice attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteInvoiceAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "InvoiceId": "inv:0-ChBGMewfnhndQBmYdpW0sp3uEPgO",
           "AttachmentId": "inva:0-ChBsWWogZxWt0bRCqCdHkJJO"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true
    }]
    




### Example - Cancel a subscription

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CancelSubscriptions` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Id": "40da986b-08e4-45bf-9ba2-d11cf9f589fb"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "Status": "CANCELED"
    
    }]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the payments

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Payments` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** based on your filtering requirements.

You must use single quotes (') to enclose the value for a **filterClause**. You can use the **filterClause** to filter records based on the columns.




### Example - Get payment details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Payments` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the **entityId** to `"bb4756c7-38c0-426b-97aa-03b6443e7f16"` which is the key to be passed.
  5. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"bb4756c7-38c0-426b-97aa-03b6443e7f16"` in the **Input Value** field and choose the **entityId** as local variable.

The value for **entityId** must be passed directly, such as `"bb4756c7-38c0-426b-97aa-03b6443e7f16"`. Here, `"bb4756c7-38c0-426b-97aa-03b6443e7f16"` is the unique primary key value.

If passing a single **entityId** throws an error due to the presence of two composite keys, you can use the **filterClause** to pass the value.




### Example - Delete a payment

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Payments` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the **entityId** to `"62008bbe-effa-4341-9d29-eac7f67b84fe"` which is the key to be passed.
  5. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"62008bbe-effa-4341-9d29-eac7f67b84fe"` in the **Input Value** field and choose the **entityId** as local variable.

If the entity has two composite business or primary keys, instead of specifying the **entityId** , you can also set the **filterClause** to `id='62008bbe-effa-4341-9d29-eac7f67b84fe'`.




### Example - Create a payment

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Payments` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** or **connectorInputPayload** as local variable. 
         
         {
           "ShippingAddressLine1": "Paris",
           "BillingAddressFirstName": "Charlie",
           "SourceId": "cnon:card-nonce-ok",
           "BankName": "Altostrat bank",
           "MoneyAmount": 7,
           "MoneyCurrency": "USD",
           "IdempotencyKey": "ab5c8c43-eaba-474e-935c-268ea3ae453a"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "BY8GnuLixAdrbr93m8nYHDgONxZZY"
         }
         




### Example - Create a refund

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Refunds` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** or **connectorInputPayload** as local variable. 
         
         {
           "PaymentId": "50yXsd0oousMgYUv0372RkIdJnRZY",
           "RefundedMoneyAmount": 72,
           "RefundedMoneyCurrency": "USD"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Success": true
         }
         




### Example - Create a subscription

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Subscriptions` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** or **connectorInputPayload** as local variable. 
         
         {
           "LocationId": "LSHW80WV4KB06",
           "CustomerId": "TE9VCZMC369HVA2RVBCEKTDQ6G",
           "PlanId": "OEVRZUHD5C42W7VQUT22WURN",
           "Ordinal": 0,
           "OrderTemplateId": "d9ZVzcjiHVc2Ugd0bzlE7yZT9g4F"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "40da986b-08e4-45bf-9ba2-d11cf9f589fb"
         }
         




### Example - Create a customer

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Customers` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** or **connectorInputPayload** as local variable. 
         
         {
           "FamilyName": "LastName",
           "GivenName": "FirstName"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "X8883DFR5M4AXGEKRSCFE3F2M9"
         }
         




### Example - Create a gift card

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `GiftCards` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** or **connectorInputPayload** as local variable. 
         
         {
           "Type": "DIGITAL",
           "LocationId": "LSHW80WV4KB06"
         }
         
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "X8883DFR5M4AXGEKRSCFE3F2M0"
         }
         




### Example - Update an invoice

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Invoices` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 
         
         {
           "Title": "Invoice Update",
           "Description": "Update Invoice",
           "Version": 0
         }
         

  5. Set the **entityId** in Data Mapper to the entity of the Invoices.
  6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'inv:0-ChCdONOpvkOxnZ64VuiDwLQ4EPgO'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { }
         




### Example - Update a subscription

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Subscriptions` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 
         
         {
           "Note": "Update Subscription"
         }
         

  5. Set the **entityId** in Data Mapper to the entity of the Subscriptions.
  6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'40da986b-08e4-45bf-9ba2-d11cf9f589fb'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { }
         




### Example - Update payout details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PayOuts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 
         
         {
           "Version": 1,
           "Description": "Update Payout"
         }
         

  5. Set the **entityId** in Data Mapper to the entity of the PayOuts.
  6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the **entityId** , **connectorInputPayload** , or **filterClause** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `'181352d9-94ef-4e86-8bb9-e3759472325f'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { }
         




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
