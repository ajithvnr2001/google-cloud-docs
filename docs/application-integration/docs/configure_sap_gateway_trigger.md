---
url: https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger/
title: SAP Gateway trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:39.104871+00:00
---

# SAP Gateway trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP Gateway trigger

The **SAP Gateway trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) SAP Gateway connector lets you perform insert, delete, update, and read operations on SAP Gateway data.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

  * If you plan to create or configure a new connection for the **SAP Gateway trigger** , make sure that you have the following IAM role on the project: 
    * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Grant the following IAM roles to the service account that you want to use for the **SAP Gateway trigger** : 
    * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## Add the SAP Gateway trigger

To add a **SAP Gateway trigger** to your integration, perform the following steps: 

    1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

    2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

    3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

       1. Enter a name and description in the **Create Integration** pane.
       2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
       3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
       4. Click **Create**.

The newly created integration opens in the _integration editor_. 

    4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
    5. Click and place the **SAP Gateway trigger** element in the integration editor.

To configure the **SAP Gateway trigger** , you can either use an existing SAP Gateway connection available in Integration Connectors, or create a new SAP Gateway connection using the inline connection creation option.

## Configure SAP Gateway trigger using an existing connection

The **SAP Gateway trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a SAP Gateway connection with event subscription enabled to configure the trigger. 

For information about how to configure a **SAP Gateway trigger** using a new SAP Gateway connection, see Configure SAP Gateway trigger using a new connection

To configure a **SAP Gateway trigger** using an existing SAP Gateway connection, perform the following steps:

    1. Click the **SAP Gateway trigger** element in the integration editor to open the trigger configuration pane.
    2. Click **Configure trigger**.
    3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
       1. **Region:** Select the region of your SAP Gateway connection.
       2. **Connection:** Select the SAP Gateway connection that you want to use. 

Application Integration only displays those SAP Gateway connections that are active and have an event subscription enabled. 

       3. Enter the event type field name. This field identifies the type of event associated with the incoming event request. 
              
              {
                  "event_type": "user.created",
                  ...
                  // other request fields
                  ...
                  }

       4. **Service Account** : Select a service account with the required IAM roles for the SAP Gateway trigger.
    4. Click **Done** to complete the trigger configuration and close the page.

## Configure SAP Gateway trigger using a new connection

    1. Click the **SAP Gateway trigger** element in the integration editor to open the trigger configuration pane.
    2. Click **Configure trigger**.
    3. Skip the **Region** field.
    4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
    5. In the **Connection Details** section, complete the following: 
       1. **Connector** : Select **SAP Gateway** from the drop down list of available Connectors.
       2. **Connector version** : Select the Connector version from the drop down list of available versions. 
       3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

          * Connection names can use letters, numbers, or hyphens.
          * Letters must be lower-case.
          * Connection names must begin with a letter and end with a letter or number.
          * Connection names cannot exceed 49 characters.
          * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
       4. Optionally, enter a **Description** for the connection instance.
       5. **Service Account** : Select a service account that has the required roles.
       6. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
          * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
          * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
       7. **Namespace** : Specify the service namespace you want to retrieve data from. This is required if the service is not specified in the URL. 
       8. **Service** : Specify the service you want to retrieve data from. This is required if the service is not specified in the URL. 
       9. **CustomUrlParams:** Specify custom query string parameters that are included with the HTTP request. The parameters must be encoded as a query string in the following format: `field1=value1&field2=value2`. The values in the query string must be URL encoded. 
       10. **Data Format** : The data format to retrieve data in. Select either XML or JSON. 
       11. **Use Display Names** : Boolean determining whether or not to use SAP labels. 
       12. Optionally, configure the **Connection node settings** : 

          * **Minimum number of nodes** : Enter the minimum number of connection nodes.
          * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
       13. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
       14. Click **NEXT**.
    6. In the **Destinations** section, set the URL of your SAP Gateway environment or to the full URL of the OData service. For example format; `${ENVIRONMENT_URL}/sap/opu/odata/${NAMESPACE}/${SERVICE}/` and sample URL is `https://sapes5.sapdevcenter.com/sap/opu/odata/IWBEP/GWSAMPLE_BASIC/`. Add any additional properties using the **CustomUrlParams** property. 
       1. **Destination Type** : Select a **Destination Type**. 
          * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
          * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.



If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

* Click **NEXT**.
* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the SAP Gateway connection:

     * Username and password
     * Anonymous
     * OAuth 2.0 auth code flow
     * SAP BTP (OAuth 2.0 - client credentials)

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.


  * **Anonymous**

If you want to use anonymous login, select **Not Available**.

    * **API Key** : The API key of the currently authenticated user.


  * **OAuth 2.0 auth code flow**
    * **Client ID** : Enter the client ID obtained from the API client page.
    * **Scopes** : Enter a comma-separated list of desired scopes.
    * **Client Secret** : Enter the client secret obtained from the API client page.
    * **Secret version** : Enter the secret version for the **Client Secret** selected.
    * **Authorization URL** : Enter the authorization URL generated when you create an OAuth client in your SAP Gateway instance.
    * **Enable Authentication Override** : Select to enable the connection to accept a different authentication dynamically during runtime.


  * **SAP BTP (OAuth 2.0 - client credentials)**
    * **Client ID** : Enter the client ID obtained from the API client page.
    * **Client Secret** : Enter the client secret obtained from the API client page.
    * **Secret version** : Enter the secret version for the secret selected above.
    * **OAuthAccessTokenURL** : Enter the URL of the OAuth access token.
    * **Destination Name** : Enter the name of the SAP BTP destination.
    * **Destination URL** : Enter the destination URL of the SAP BTP.
    * **Enable Authentication Override** : Select this option to enable the connection to accept a different authentication dynamically during runtime.



### Configure event subscription

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  1. Select any one of the following authentication types for the event listener. **Note:** Before you configure authentication, ensure that you have the event listener endpoint, which is available to you after you create the connection. To view the endpoint, go to the [All connections](https://console.cloud.google.com/connectors/connections) page, and then click the connection that you wan to view. The endpoint is displayed in the **Connection Details** section.
     * [Google Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt). If you enable this option, follow the steps in [Authenticate by using JSON Web Tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt#configure-google-auth) to configure the authentication for ABAP SDK. Also, ensure that the service account has [roles/connectors.listener](https://cloud.google.com/iam/docs/roles-permissions/connectors) role whose access token is used for authentication.
     * [API Key Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys). If you select this option, you must have created an API key, and then saved the key as a Secret Manager secret. For more information, see [Create an API key](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#ssf-create-api-key).
  2. Enter the event type field name. This field identifies the type of event associated with the incoming event request. 
         
         {
         "event_type": "user.created",
         ...
         // other request fields
         ...
         }

  3. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
  4. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
     1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
     2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.

**Tip:** To understand how you can use event subscription in your integrations, see [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger). 

## Configure authentication in SAP

Configure the authentication in SAP by following the instructions in the [Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication) guide. 

## Validate the trigger

To validate the trigger, you can create an ABAP program. The following is a sample ABAP program that you can use as a reference. The `ls_event_payload` field changes based on your requirements:
    
    
    *&---------------------------------------------------------------------*
    *& Report ZR_TEST_INT_CONNECTOR
    *&---------------------------------------------------------------------*
    *&
    *&---------------------------------------------------------------------*
    REPORT zr_test_int_connector.
    PARAMETERS: p_auth TYPE char1 RADIOBUTTON GROUP rbg1 USER-COMMAND uc DEFAULT 'X',
     p_apik TYPE char1 RADIOBUTTON GROUP rbg1.
    DATA:
     lv_p_projects_id TYPE string,
     lv_p_locations_id TYPE string,
     lv_p_connections_id TYPE string,
     ls_input TYPE /goog/cl_connectors_v1=>ty_103.
    TYPES: BEGIN OF event_payload,
     event_type TYPE string,
     event_id TYPE string,
     name TYPE string,
     org_id TYPE string,
     END OF event_payload.
    DATA: ls_event_payload TYPE event_payload.
    ls_event_payload = VALUE #(
     event_type = 'create-entity'
     event_id = '1'
     name = 'demo-org'
     org_id = 'SAP'
     ).
    TRY.
     IF p_Auth = abap_true.
     DATA(lv_client_key) = 'IC_DEMO_GOOGLE_AUTH'.
     lv_p_connections_id = 'conn-event-triggers-from-sap-gateway'.
     ELSE.
     lv_client_key = 'IC_DEMO_GOOGLE_APIK'.
     lv_p_connections_id = 'conn-event-triggers-from-sap-gateway-apik'.
     ENDIF.
    * Open HTTP Connection
     DATA(lo_client) = NEW /goog/cl_connectors_v1( iv_key_name = CONV #( lv_client_key ) ).
    * Populate relevant parameters
     lv_p_projects_id = lo_client->gv_project_id.
     lv_p_locations_id = 'us-central1'.
     GET REFERENCE OF ls_event_payload INTO ls_input-payload .
    * Call API method: connectors.projects.locations.connections.listenEvent
     CALL METHOD lo_client->listen_event_connections
     EXPORTING
    
    
    iv_p_projects_id = lv_p_projects_id
     iv_p_locations_id = lv_p_locations_id
     iv_p_connections_id = lv_p_connections_id
     is_input = ls_input
     IMPORTING
    * es_raw =
     es_output = DATA(ls_output)
     ev_ret_code = DATA(lv_ret_code)
     ev_err_text = DATA(lv_err_text)
     es_err_resp = DATA(ls_err_resp).
     IF lo_client->is_success( lv_ret_code ).
     MESSAGE 'Success' TYPE 'S'.
     ELSE.
     MESSAGE lv_err_text TYPE 'E'.
     ENDIF.
    * Close HTTP Connection
     lo_client->close( ).
     CATCH /goog/cx_sdk INTO DATA(lo_exception).
     MESSAGE lo_exception->get_text( ) TYPE 'E'.
    ENDTRY.
    

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
