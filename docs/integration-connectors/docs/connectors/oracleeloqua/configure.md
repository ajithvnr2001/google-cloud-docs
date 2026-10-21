---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/oracleeloqua/configure/
title: Oracle Eloqua \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:26.136692+00:00
---

# Oracle Eloqua  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/oracleeloqua/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Oracle Eloqua

The Oracle Eloqua connector lets you perform read, insert, update, and delete operations on Oracle Eloqua data.

## Supported Versions

The following is the minimum supported version for this connector: Oracle Eloqua 10-24C (Standard).

## Before you begin

Before using the Oracle Eloqua connector, do the following tasks:

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

  2. Click **\+ Create New** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Oracle Eloqua** from the drop down list of available Connectors.
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
     8. **Company** : Specify the company's unique identifier. This field is used to authenticate to the Eloqua servers. 
     9. **Bulk Polling Interval** : Specify the time interval between bulk API requests. The default value is 200 ms. 
     10. **Bulk Query Timeout** : Specify the time in minutes to wait for a bulk query response. The default value is 25 minutes. 
     11. **Data Retention Duration** : Specify the time duration in hours to store bulk data on the server. You can specify values from 1 hour to 2 weeks. The default value is 24 hours. 
     12. **Display Column Name** : Specify the display name for columns when using the Oracle Eloqua Bulk API. You can specify an empty string, `internal`, or `statement`. 
     13. **Map Data Cards Case Sensitive Match** : Specify whether to use case sensitive match in data card mapping. 
     14. **Map Data Cards Relationship** : Enter a comma-separated list of the relationships between the custom object tables and the entity tables. 
     15. **Retry Count** : Specify the maximum number of times to retry a Bulk API request that fails due to an HTTP 500 status code (Internal Server Error). 
     16. **Retry Interval** : Specify the time interval between attempts to retry a Bulk API request that failed with an HTTP 500 status code (Internal Server Error). 
     17. **Use Bulk API** : Specify whether to use the bulk API to retrieve data. 
     18. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     19. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Oracle Eloqua connection:

     * User Password
     * OAuth 2.0 Authorization code/li>

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **User Password**
    * **Username** : The username to authenticate the connection.
    * **Password** : Secret Manager Secret containing the password associated with the username.
    * **Secret Version** : Secret version for the secret selected above.


  * **OAuth 2.0 Authorization code**
    * **Client ID** : The client id provided by connector for the app you created.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret Version** : Secret version for the secret selected above.
    * **Authorize URL** : Authorization URL generated when creating a client in the Oracle Eloqua instance.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### Username and password connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Oracle Eloqua  
Connector version | 1  
Connection Name | oracle-eloqua-googlecloud  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Company | AltostratLtd  
Username | USERNAME  
Password | PASSWORD  
Secret Version | 1  
  
### OAuth 2.0 connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Oracle Eloqua  
Connector version | 1  
Connection Name | oracle-eloqua-googlecloud-oauth  
Description | oracle-eloqua-googlecloud-oauth  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Company | AltostratLtd  
Client ID | CLIENT_ID  
Scopes | full  
Client Secret | CLIENT_SECRET  
Secret Version | 4  
  
## System limitations

The Oracle Eloqua connector can process a maximum of 12 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Oracle Eloqua connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List all AccountGroup

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AccountGroup` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



You can perform the List operation on the following entities as well:

Event, User, and Campaign

### Example - Get an AccountGroup

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AccountGroup` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to the entity of the AccountGroup. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1` in the **Input Value** field and choose the EntityId as Local variable. 



You can perform the Get operation on the following entities as well: Email and User.

### Example - Delete an AccountGroup

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AccountGroup` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to the entity of the AccountGroup. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `8` in the **Input Value** field and choose the EntityId as Local variable. 



You can perform the Delete operation on the Email entity as well.

### Example - Create a Campaign

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Campaign` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "AltostratCampaign1.11",
           "BudgetedCost": 100000
         }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "ID": 9
         }
         




### Example - Create an Event

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Event from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "Marketing Experience GCP2.2",
           "Description": "Modern Marketing Experience brings together Modern Marketers from around the globe",
           "EmailAddressFieldId": "-2"
         }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "16"
         }
         




### Example - Update a Campaign

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Campaign` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to the entity of the Campaign. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `5` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "AltostratCamp9",
           "BudgetedCost": 100
         }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
      "ID": 5
    }
    




### Example - Update an Email

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Email` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to entity of the Email. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `59` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "My Googlecloud email updated",
           "EmailGroupId": 1,
           "HtmlContent_Type": "RawHtmlContent",
           "IsPlainTextEditable": false,
           "IsTracked": false,
           "PlainText": "\r\n",
           "BouncebackEmail": "AltostratLtd@s119222.m.en25.com",
           "ReplyToEmail": "newclient@en25.com",
           "ReplyToName": "AltostratLtd",
           "SenderEmail": "newclient@en25.com",
           "SenderName": "AltostratLtd",
           "SenderPlainTextOnly": null,
           "Subject": "New subject line",
           "Description": null,
           "FolderId": 42,
           "EmailHeaderId": 1,
           "EmailFooterId": 1,
           "Permissions": "Retrieve,SetSecurity,Delete,Update,Activate",
           "AccessedAt": null,
           "CurrentStatus": "Draft",
           "Depth": "complete"
         }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    {
      "ID": 59
    }
    




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
