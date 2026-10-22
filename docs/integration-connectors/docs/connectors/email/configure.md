---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/email/configure/
title: Email \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:58.791976+00:00
---

# Email  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/email/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Email

The Email connector lets you perform insert, delete, update, and read operations on IMAP database.

## Before you begin

**Note:**

  * The email connector supports only username and password authentication for the mail servers. Therefore, you can't create a connection to a mail server that requires a different authentication, such as OAuth 2.0.
  * Starting May 30, 2022, Google no longer supports the use of third-party applications or devices which ask you to sign in to your Google account using only your username and password. Hence, you can't connect to Gmail by using the email connector.



Before using the Email connector, do the following tasks:

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

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Email** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. (Optional) **Description:** Enter a description for the connection.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. **Protocol** : The type of email server to connect to. Valid values are `IMAP` and `POP`. 
     8. **Verbosity Level** : This field determines the amount of detail that you want to include in the log file. Valid values range from 1 to 5. A higher verbosity level logs all the communication details including the request, response, and SSL certificates. 
     9. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
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
     11. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     12. Click **Next**.
  5. In the **Destinations** section, enter details of the name or address of the mail server that you want to connect to. The server supports both IMAP or POP protocols. 
     1. **Destination Type** : Select a **Destination Type**. For example, enter the host address and the port number. For example, host address is `outlook.office365.com` and port is `993`. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

  6. If you want to send email, add the SMTP server details in the **SMTPServer** section by clicking **+Add destination**. Then, do the following: 
     * Enter the host address and the port number. For example, host address is `smtp-mail.outlook.com` and port is `587`.
  7. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Email connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details. 
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The user of the Email account used to authenticate.
    * **Password** : Secret Manager Secret containing the password of the email account used to authenticate.



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

The Email connector can process 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### MoveEmails action

#### Input parameters of the MoveEmails action

Parameter name | Data type | Required | Description  
---|---|---|---  
Description | String | Yes | The mailbox where the message will be moved.  
Mailbox | String | Yes | The mailbox where the message is currently located.  
Id | String | Yes | This inputs indicates the set of messages to operate on. It may consist of a single message id, a range of messages specified by two message numbers separated by ':' (e.g. '1:5'), and/or individual message numbers separated by ',' (e.g. '1:5,7,10').  
  
For example on how to configure the `MoveEmails` action, see Action examples.

### SendMailMessages action

#### Input parameters of the SendMailMessages action

Parameter name | Data type | Required | Description  
---|---|---|---  
BCC | String | No | The semicolon-separated list of names and email addresses of the BCCed recipients.  
Priority | String | No | Priority of the mail message.  
Sensitivity | String | No | Sensitivity of the mail message.  
Attachment | String | Yes | Semicolon-separated list of the attachment file names (with path if reading from a file) included in the message.  
MessageBody | String | Yes | The message body.  
AttachmentData | String | Yes | Semicolon-separated list of the base-64-encoded attachment data included in the message. (You must still specify the filename in Attachments.  
InlineImage | String | Yes | Semicolon-separated list of the inline image identifiers (cids) to be included in the message.  
DeliveryNotification | String | No | Email address to send a delivery notification to.  
InlineImageData | String | Yes | Semicolon-separated list of the base-64-encoded image data to be included in the message.  
CC | String | No | The semicolon-separated list of names and email addresses of the CCed recipients.  
InlineImageContent | String | No | The content as InputStream to be uploaded.  
From | String | No | The email address of the sender.  
To | String | No | The semicolon-separated list of names and email addresses of the recipients.  
Subject | String | Yes | The subject of the mail message.  
AttachmentContent | String | No | The content as InputStream to be uploaded.  
Charset | String | No | The character set to use in the message.  
ReadReceipt | String | No | Email address to send a read receipt to.  
IsHTML | String | No | Whether the email is HTML or plain text.  
Importance | String | No | Importance of the mail message.  
  
For example on how to configure the `SendMailMessages` action, see Action examples.

### SetLabels action

#### Input parameters of the SetLabels action

Parameter name | Data type | Required | Description  
---|---|---|---  
OperationType | String | Yes | This indicates weather the specified labels should be added,removed or replace existing labels list.  
Mailbox | String | Yes | The Gmail mailbox where the message is located.  
Id | String | Yes | This inputs indicates the set of messages to operate on. It may consist of a single message id, a range of messages specified by two message numbers separated by ':' (e.g. '1:5'), and/or individual message numbers separated by ',' (e.g. '1:5,7,10').  
Label | String | Yes | List of labels to be set to the message specified by the MessageSet property. This input should be set to a comma separate list of labels.  
  
For example on how to configure the `SetLabels` action, see Action examples.

### SetFlag action

#### Input parameters of the SetFlag action

Parameter name | Data type | Required | Description  
---|---|---|---  
OperationType | String | Yes | This indicates weather the specified flags should be added,removed or replace existing flags list.  
Mailbox | String | Yes | The mailbox where the message is located.  
Id | String | Yes | This inputs indicates the set of messages to operate on. It may consist of a single message id, a range of messages specified by two message numbers separated by ':' (e.g. '1:5'), and/or individual message numbers separated by ',' (e.g. '1:5,7,10').  
Flags | String | Yes | Sets the specified flags to the message specified by message set. (e.g., Seen, Deleted, Draft,flagged). Flags should be specified as comma separated list(e.g. Seen,Deleted,flagged)  
  
For example on how to configure the `SetFlag` action, see Action examples.

## Examples

## Action examples

### Example - Move an email

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveEmails` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Destination": "Inbox",
         "Mailbox": "Archive",
         "Id": "1"
         }

If the action is successful, the `MoveEmails` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "rss:title": "Message(s) moved successfully."
    }] 




### Example - Send an email

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "MessageBody": "This mail is generated by using action sendmailmessage for outlook server.",
         "To": "test97@gmail.com",
         "Subject": "Outlook SMTP\n server."
         }

If the action is successful, the `SendMailMessages` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
     "MessageId": "4797386f18288a7441c5317a459b8340e857@outlook.com"
    }]




### Example - Send mail with attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "MessageBody": "This mail is generated by using action sendmailmessage for outlook server.",
         "To": "test97@gmail.com",
         "Subject": "Outlook SMTP PDF Mail.",
         "Attachment": "Testing.pdf",
         "AttachmentData": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBvYmoKPDwvTGVuz1xj6j3/gb09Wma83/dLbs7L9N03T/dHh6ArlrRiZdCU98lR5A3h9FD
         ...[too long to view on UI. Please download the log to view the full content.]
         }    

If the action is successful, the `SendMailMessages` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "MessageId": "1e96993a6053845c65ee44e6b4153d585e@outlook.com"
    }]




### Example - Set labels

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetLabels` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Labels": "GoogleCloud_Testing",
         "OperationType": "ADD",
         "Mailbox": "Inbox",
         "Id": "1"
         }

If the action is successful, the `SetLabels` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "rss:title": "Message labels set correctly."
    }]




### Example - Set flag

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetFlag` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Mailbox": "Sent",
         "Id": "1",
         "Flags": "Draft",
         "OperationType": "ADD"
         }

If the action is successful, the `SetFlag` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "rss:title": "Message flags set correctly."
    }]




### Example - Set flag to particular mail

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetFlag` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Mailbox": "Sent",
         "Id": "1",
         "Flags": "Flagged",
         "OperationType": "ADD"
         }

If the action is successful, the `SetFlag` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "true",
    "rss:title": "Message flags set correctly."
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all emails

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Inbox` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 



### Example - Get a single email

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Inbox` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1` in the **Default Value** field. 

Here, `1` is a unique record ID in the `Inbox` entity.




### Example - Delete an email

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Inbox` from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `1` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
protocol | STRING | True | The type of email server to connect to.   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Email connection in an integration

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
