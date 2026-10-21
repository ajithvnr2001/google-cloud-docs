---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure/
title: ServiceNow \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:29.115601+00:00
---

# ServiceNow  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ServiceNow

The ServiceNow connector lets you perform insert, delete, update, and read operations on ServiceNow database.

## Before you begin

Before using the ServiceNow connector, do the following tasks:

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

  * Provide access to the following tables in your ServiceNow instance:

    * sys_db_object
    * sys_dictionary
    * sys_glide_object

This permission is required for the connector to connect to your data. To provide the access, do the following steps:

    1. In your ServiceNow application, go to **System Security > Access Controls (ACL)**.
    2. Select **New** to create an access control object.
    3. For **Type** , select **record**.
    4. For **Operation** , select **read**.
    5. For **Name** , select **Table [sys_db_object]** in the first drop-down and **\--None--** in the second drop-down.
    6. In the **Requires role** section, double-click the **Insert a new row....** text box, and then search for and select your desired role.
    7. Click **Submit** to create the ACL object.
    8. Assign the role which has the created ACL to the authenticating user. To do this, go to **User Administration > Users > Select authenticating user > Roles > Edit... > **. and, then add your role from your collection.
  * Get the ServiceNow instance URL, username, and password.




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
     1. **Connector** : Select **Servicenow** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
        * For connectors that [support event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#enable-event-subscriptions-in-connections), the connection names cannot begin with the "goog" prefix. 
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
        * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
        * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
     8. **Include System Tables** : Select this option to retrieve system tables that store security data and metadata. Only admin-role users have access to these tables.
     9. **Filter Tables** : Specify the tables as a comma-separated list. Use this field to filter the tables that you want the connection to retrieve instead of retrieving all the tables.
     10. **Display Value** : Specify whether the connection must retrieve the display value, actual value, or both the values from the database.

Note: If you decide to set this connection property to "true", then all the returned fields will be of type "String" due to Servicenow API limitations.

        * **TRUE** : Returns display values for all fields.
        * **FALSE** : Returns actual values from the database.
        * **ALL** : Returns both actual and display values.
     11. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     12. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     13. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Servicenow connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* If you have enabled event subscription, the **Event Subscription Details** section appears on the connection creation page. To understand how to configure event subscription details, see Configure event subscription.
* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The ServiceNow username to use for the connection.
    * **Password** : Secret Manager secret containing the password associated with the ServiceNow username.



### Configure event subscription [](https://cloud.google.com/products/#product-launch-stages)

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  * **Authentication Token** : (Optional) Select the Secret Manager secret of your authentication token, and the corresponding secret version from the **Secret Version** drop-down.
  * **HMAC Algorithm** : Select the HMAC algorithm for encrypting the response payload.
  * **HMAC Secret Key** : If you have selected a **HMAC Algorithm** , select the Secret Manager secret of the HMAC key, and the corresponding secret version from the **Secret Version** drop-down.
  * **Enable private connectivity** : Select this option to listen to events securely via a private connection.
  * Enter the following dead-letter configuration: 
    * **Dead-letter project ID:** : The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
    * **Dead-letter topic** : The Pub/Sub topic where you want to write the details of the unprocessed event.



#### Post connection creation steps

To complete the event subscription configuration, you must register the webhook URL with your ServiceNow application. Therefore, after the connection creation is successful, perform the following additional steps:

  1. Go the connection details page of the newly created connection, and copy the webhook URL for event subscription.
  2. Log in to your ServiceNow application and do the following: 
     1. In the **All > Business Rules > When to run** page, select the operation for which you want to listen.
     2. Click the **Advanced** tab. This opens a script editor.
     3. Enter a JavaScript that sends a request to the callback URL. The request contains the payload that is triggered whenever any of the enabled operation occurs. A sample JavaScript is as follows: 

### Template
            
            (function executeRule(current, previous /*null when async*/ ) {
            var request = new sn_ws.RESTMessageV2();
            request.setEndpoint('WEBHOOK_URL'); // here you must the listener url where you want send the event payload
            
            request.setHttpMethod('POST');
            
            var authToken = "AUTHENTICATION_TOKEN"
            request.setRequestHeader("authorization", authToken);
            request.setRequestHeader("Accept", "application/json");
            request.setRequestHeader('Content-Type', 'application/json');
            
            request.setRequestBody("{\"eventType\":\"" +
            "EVENT_TYPE" + CUSTOM_FIELDS "\"}");
            
            var data = request.getRequestBody();
            var secretKey = "SECRET_KEY";
            
            var signature = SncAuthentication.encode(data, secretKey, "ENCRYPTION_ALGORITHM");
            request.setRequestHeader("hmacauthorization",signature);
            var response = request.execute();
            
            })(current, previous);

Replace the following: 

        * WEBHOOK_URL: Webhook URL for event subscription that you would have got from the connection details page of Integration Connectors.
        * AUTHENTICATION_TOKEN: The actual text for authentication token that you have configured for the connection.
        * EVENT_TYPE: The actual text for event type that you have configured in the [ServiceNow trigger](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger).
        * CUSTOM_FIELDS: The request body must always have the `eventType` field. In addition to this field, you can add other fields based on your requirement.
        * SECRET_KEY: The actual text for secret key that you have configured for the connection.
        * ENCRYPTION_ALGORITHM: Should be any one of the following values: 
          * HmacSHA224
          * HmacSHA256
          * HmacSHA384
          * HmacSHA512

The algorithm should be same algorithm that you have configured for the connection.

### Example
    
    (function executeRule(current, previous /*null when async*/ ) {
    var request = new sn_ws.RESTMessageV2();
    request.setEndpoint('https://webhook.site/bb37937e-24ea-19b3-9dcd-84eca77f60eg'); // here you must the listener url where you want send the event payload
    
    request.setHttpMethod('POST');
    
    var authToken = "YWRtaW46ZkVpNypxVzhCL3VY"
    request.setRequestHeader("authorization", authToken);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader('Content-Type', 'application/json');
    
    request.setRequestBody("{\"caller_id\":\"" +
    current.caller_id + "\",\"eventType\":\"" +
    "service_now_event_type_1" + "\",\"company\":\"" +
    current.company + "\",\"number\":\"" +
    current.number + "\",\"description\":\"" +
    current.description + "\",\"FirstName\":\"" +
    current.u_firstname + "\",\"LastName\":\"" +
    current.u_lastname + "\",\"status\":\"" +
    current.u_status + "\",\"Element\":\"" +
    current.getElement() + "\",\"category\":\"" +
    current.category + "\",\"opened_at\":\"" +
    current.opened_at + "\",\"opened_by\":\"" +
    current.opened_by + "\",\"location\":\"" +
    current.location + "\",\"salesforceId\":\"" +
    current.u_salesforceid + "\"}"); //fields you want
    
    var data = request.getRequestBody();
    var secretKey = "YWRtaW46ZkVpNypxVzhCL3VY";
    
    // var MAC_ALG_4 = "HmacSHA384";
    var MAC_ALG_3 = "HmacSHA256";
    // var MAC_ALG_5 = "HmacSHA512";
    // var MAC_ALG_2 = "HmacSHA224";
    
    var signature = SncAuthentication.encode(data, secretKey, MAC_ALG_3);
    request.setRequestHeader("hmacauthorization",signature);
    var response = request.execute();
    
    })(current, previous);


**Tip:** To understand how you can use event subscription in your integrations, see [ServiceNow trigger](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger). 

## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### Basic authentication connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Servicenow  
Connector version | 1  
Connection Name | google-cloud-servicenow-conn  
Service Account | Your_Project_Number@serviceaccount  
Display Values | True  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
host 1 | https://Your-domainname.com  
Username | User_name  
Password | Password  
Secret version | 1  
  
## Connection configuration samples

This section lists the sample values for the various fields that you configure for creating the ServiceNow connection.

### ServiceNow web connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | ServiceNow  
Connector version | 1  
Connection Name | gcp-servicenow-conn  
Service Account | SERVICE_ACCOUNT_NAME@serviceaccount  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
host 1 | https://host_name.com  
Username | username  
Password | password  
Secret version | 1  
  
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

## Actions

This section lists all the actions supported by the Servicenow connection.

### UploadAttachment action

This action Upload a file as an attachment to a specified record.

#### Input parameters of the UploadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
Content | String | No | String Content to upload as file.  
ContentBytes | String | No | Bytes content to upload as file.  
HasBytes | Boolean | No | Whether to upload content as bytes.  
TableName | String | No | Name of the table to attach the file to.  
TableSysId | String | No | Sys_id of the record in the table specified by TableName that you want to attach the file to.  
  
#### Output parameters of the UploadAttachment action

This action returns set of parameters from the uploaded entity

For example on how to configure the `UploadAttachment` action, see Examples.

### DownloadAttachment action

This action Download a file attachment from a specific record.

#### Input parameters of the DownloadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
SysId | String | Yes | Sys_id of the attachment file.  
HasBytes | Boolean | No | Whether to download content as bytes.  
  
#### Output parameters of the DownloadAttachment action

This action returns whether download is True or false through Success Parameter and if True, outputs the Content of DownloadAttachment

For example on how to configure the `DownloadAttachment` action, see Examples.

## Examples

This section describes how to perform some of the entity operations and actions in this connector.

### Example - Upload an attachment for an incident

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Content": "File is uploaded",
           "TableName": "Incident",
           "TableSysId": "018f4057473ae5104593a6b5316d4357"
         }

This example uploads the Content value from Payload as attachment and return the set of Parameters for the entity uploaded . If the action is successful, the `UploadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "SysId": "a667f5d1939be110ff87352d6cba10fc",
    "FileName": "7043426257788756581.connector.txt",
    "TableSysId": "018f4057473ae5104593a6b5316d4357",
    "TableName": "Incident",
    "DownloadLink": "https://gcp.service-now.com/api/now/v1/attachment/a667f5d1939be110ff87352d6cba10fc/file",
    "ContentType": "text/plain",
    "SizeBytes": "16",
    "ChunkSizeBytes": "700000",
    "Compressed": "true",
    "SizeCompressed": "36",
    "SysTags": "",
    "ImageHeight": "",
    "ImageWidth": "",
    "AverageImageColor": "",
    "SysModCount": "0",
    "Hash": "807e96c2942c41ad699d004a9d6a74595c84fab09111d479b6bbe013d5debff6",
    "State": "pending",
    "SysUpdatedBy": "gcp2",
    "SysUpdatedOn": "2023-06-07 07:23:34",
    "SysCreatedBy": "gcp2",
    "SysCreatedOn": "2023-06-07 07:23:34",
    "encryption_context": ""
    }




### Example - Download an attachment of an incident

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "SysId": "440c3995471fe1104593a6b5316d4384"
         }

This example returns whether download is True or false through Success Parameter and if True, outputs the Content of DownloadAttachment. If the action is successful, the `DownloadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True"
    },
    {
    "Content": " A Simple Text File \r\n\r\n\r\n This is a small demonstration .txt file - \r\n just for use in the Virtual Mechanics tutorials. More text. And more \r\n text. And more text. And more text. And more text. \r\n And more text. And more text. And more text. And more text. And more \r\n text. And more text. Boring, zzzzz. And more text. And more text. And \r\n more text. And more text. And more text. And more text. And more text. \r\n And more text. And more text. \r\n And more text. And more text. And more text. And more text. And more \r\n text. And more text. And more text. Even more. Continued on page 2 ...\r\n Simple PDF File 2 \r\n ...continued from page 1. Yet more text. And more text. And more text. \r\n And more text. And more text. And more text. And more text. And more \r\n text. Oh, how boring typing this stuff. But not as boring as watching \r\n paint dry. And more text. And more text. And more text. And more text. \r\n Boring. More, a little more text. The end, and just as well. "
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - GET single record for Entity "Incident"

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Incident from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. Set the entity ID to "0c5f3cece1b12010f877971dea0b1449", which is the key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"0c5f3cece1b12010f877971dea0b1449"` in the **Input Value** field and choose the EntityId as Local variable. 

**Note:**
* The value for the Entity Id must be passed directly, such as "0c5f3cece1b12010f877971dea0b1449". Here "0c5f3cece1b12010f877971dea0b1449" is the unique primary key value.
* There are certain cases, where passing single Entity Id might throw an error due to the presence of two composite keys.
* To fetch the comment field details under the incident entity, mark the display value as true at the connection level.




## System limitations

The ServiceNow connector can process a maximum of 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

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
include_system_tables | BOOLEAN | False | Controls whether to expose the system tables or not.   
filter_tables | STRING | False | Specify the tables you want in a comma-separated list.   
  
## Use the Servicenow connection in an integration

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
