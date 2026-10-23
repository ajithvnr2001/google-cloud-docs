---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure/
title: Jira Cloud \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:29.550999+00:00
---

# Jira Cloud  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Jira Cloud

The Jira Cloud connector lets you perform insert, delete, update, and read operations on Jira data which is modeled as a database.

## Supported versions

The Jira Cloud connector uses version 2 and 3 of the JIRA Cloud REST API. These are managed internally and you don't have to do any extra configurations.

## Before you begin

Before using the Jira Cloud connector, do the following tasks:

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
     1. **Connector** : Select **Jira Cloud** from the drop down list of available Connectors.
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
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
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
     11. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * **Host address** : Specify the hostname or IP address of the destination. **Note:** If you are specifying a hostname, you must specify the URL along with the protocol (HTTP or HTTPS).

If you want to establish private connection to your backend, do the following:

          * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
          * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.

To enter additional destinations, click **+ADD DESTINATION**.

     2. Click **NEXT**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Jira Cloud connection:

        * Username and password 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  7. If you have enabled the event subscription, the **Event Subscription Details** section appears on the connection creation page. To understand how to configure event subscription details, see Configure event subscription.
  8. **Review** : Review your connection and authentication details.
  9. Click **Create**.



### Configure event subscription

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  1. Select a **Destination Type**. 
     * **Host address** : Enter the registration URL of your backend system in the **host** field.
  2. Enter the authentication details. 
     1. **Username** : Enter the username.
     2. **API Token** : Select the Secret Manager secret containing the API token.
     3. **Secret Version** : Select the secret version.
  3. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
  4. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
     1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
     2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
  5. If you want to use a proxy to connect to your backend (for event subscription), enter the following details: 
     1. **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. Select any of the following authentication types: 
        * **Always** : The connection is always SSL enabled for event subscription.
        * **Never** : The connection is not SSL enabled for event subscription.
     2. **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
        * **Basic** : Basic HTTP authentication.
     3. **Proxy User** : Enter the user name to be used to authenticate with the proxy server.
     4. **Proxy Password** : Select the Secret Manager secret of the user's password.
     5. **Secret version** : Select the secret version. 
     6. In the **Proxy Server** section, enter details of the proxy server. 
        1. Click **\+ Add destination** , and then select the **Destination Type** as **Host address**.
        2. Enter the proxy server's hostname or IP address, and the proxy server's port number.

**Tip:** To understand how you can use event subscription in your integrations, see [Jira Cloud trigger](https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger). 

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The Jira Cloud username to use for the connection.
    * **API Token** : The password for the username will be an API token. Select the Secret Manager Secret containing the API Token associated with the Jira Cloud username. 
  * **OAuth 2.0 - Authorization code**
    * **Client ID:** Client ID as provided by your external application.
    * **Scopes:** Permission scopes. The `offline_access` and `read:jira-user` scopes are required to create a connection. To understand how the scopes work and to view all the available scopes for Jira Cloud, see [Scopes](https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/). 
    * **Client secret:** Select the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). You should have created the Secret Manager secret prior configuring this authorization.
    * **Secret version:** Secret Manager secret version for client secret.
    * **Cloud ID** : Specify the Cloud ID of the Atlassian site. For information about how to get the Cloud ID, see [Cloud ID](https://developer.atlassian.com/cloud/forms/rest/intro/#using-basic-auth).

For the `Authorization code` authentication type, after creating the connection, you should perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your Jira Cloud application, you must re-authorize your Jira Cloud connection. To understand how to re-authorize, see Re-authorization for Authorization code. 


### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

  1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).




## Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in your Jira Cloud application, you must re-authorize your Jira Cloud connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




## System limitations

The Jira Cloud connector can process a maximum of 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Entity operation examples

This section shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List Issues

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Issues from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a filterClause, such as, CreatorEmail = 'cruz@altostrat.com'. You can use the filterClause to filter records based on the columns.

In some entities only List operation can not fetch data. In such entities, you can use filetClause.




### Example - Get Issues

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Issues from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. Set the entity ID to 10000 which is the Key ID to be passed for Issues. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `10000` in the **Default Value** field.

The value for Entity ID must be passed directly, such as, 10000. Here, 10000 is the unique primary key value. The Get operation can be performed only on entities with unique primary key.




### Example - Delete Issues

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Issues from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. Set the entity ID to 10000 which is the Key to be passed.. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `10000` in the **Default Value** field.

The Delete operation can be performed only on entities with unique primary key.




### Example - Create IssueTypes

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select IssueTypes from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "task123456",
           "Description": "New description is added."
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "10041"
         }
         




### Example - Create Issues

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Issues from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "IssueTypeName": "Subtask", 
             "ProjectName": "kanban4", 
             "Summary": "Summary Added", 
             "ParentKey": "KN-6" 
           }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 10071.0
         }
         




### Example - Create Sprints

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Sprints from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "PROJ Sprint GCPcloud",
           "State": "future",
           "Goal": null,
           "OriginBoardId": 2.0,
           "StartDate": "2023-06-27 07:06:08",
           "EndDate": "2023-07-27 07:06:08"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 23.0
         }
         




### Example - Create Comments

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Comments from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "IssueId": 10001.0,
           "Body": "Adding comments to above ID by editing it"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": 10023.0,
           "IssueId": null
         }
         




### Example - Create Users

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Users from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "GroupName": null,
           "DisplayName": "Charlie",
           "EmailAddress": "charlie@altostrat.com",
           "Active": true,
           "TimeZone": null,
           "Locale": "en_US",
           "AccountType": "atlassian"
         }
         

If the integration is successful, the connectors task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "AccountId": "557058:0a04612c-746d-4d47-a909-71ba797fe228"
         }
         




### Example - Create Worklogs

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Worklogs from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "IssueKey": "GJCT-1",
           "Started": "2023-06-10 08:08:08",
           "TimeSpent": "2000"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "41718",
           "IssueId": 10000.0
         }
         




### Example - Update IssueTypes

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select IssueTypes from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "NEW_TASK",
           "Description": "New Description"
         }
         

  5. Set the entity ID to the entity of the IssueTypes. To set the entity ID, click **entityId** and then enter `10038` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "10038"
         }
         




### Example - Update Issues

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Issues from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "AssigneeAccountId": "61d572aa7c6f9800705289a1",
           "AssigneeName": "Charlie c"
         }
         

  5. Set the entity ID to the entity of the Issues. To set the entity ID, click **entityId** and then enter `10024` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "AssigneeDisplayName": "Charlie Cruz"
         }
         




### Example - Update Sprints

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Sprints from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "PROJ Sprint GCP_Updated",
           "State": "future",
           "StartDate": "2023-06-27 07:06:08",
           "EndDate": "2023-07-27 07:06:08"
         } 
         

  5. Set the entity ID to the entity of the Sprints. To set the entity ID, click **entityId** and then enter ` 2 ` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         }
         




### Example - Update Comments

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Comments from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "PROJ Sprint GCPcloud_Updated",
           "State": "future",
           "StartDate": "2023-06-27 07:06:08",
           "EndDate": "2023-07-27 07:06:08"
         } 
         

  5. Set the entity ID to the entity of the Comments. To set the entity ID, click **entityId** and then enter `2` in the **Default Value** field. 

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         }
         




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
  
## Use the Jira Cloud connection in an integration

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
