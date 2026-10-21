---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/saparibaprocurement/configure/
title: SAP Ariba Procurement \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:27.994655+00:00
---

# SAP Ariba Procurement  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/saparibaprocurement/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP Ariba Procurement

The SAP Ariba Procurement connector lets you perform insert, update, and read operations on the SAP Ariba Procurement data.

## Supported versions

This connector supports SAP Ariba Procurement REST APIs.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector 
  * Enable `secretmanager.googleapis.com` (Secret Manager API) and `connectors.googleapis.com` (Connectors API). For more information, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). 



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, complete the following: 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **SAP Ariba Procurement** from the list of available connectors.
     2. **Connector version** : Select the connector version from the list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. **Description** : Enter a description for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. **ANID** : Specify your SAP Ariba network ID.
     8. **API Key** : Enter the OAuth application key for authentication.
     9. **Realm** : Enter the SAP Ariba realm for the connection.
     10. **API** : Enter the SAP Ariba API to retrieve data from.
     11. **Data Center** : Enter the geographic location where your account's data is hosted.
     12. **Environment** : Enter the SAP Ariba environment you want to connect to.
     13. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     14. **\+ ADD LABEL** : click this to add a label to the connection in the form of a key/value pair.
     15. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the SAP Ariba Procurement connection:

        * OAuth 2.0 - client credentials

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - client credentials**
    * **Client ID** : Enter the client ID for the application you created.
    * **Client Secret** : Enter the secret manager secret containing the client secret for the connected app you created.
    * **Secret version** : Select the secret version for the **client secret**.
    * **Enable Authentication Override** : Enable this for authentication override.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - client credentials connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | SAP Ariba Procurement  
Connector version | 1  
Connection Name | gcp-sapariba-procurement-po-supplier  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Log Level | Debug  
ANID | AN11234322444-T   
API Key | gaTawAf8m3gtAs8gPyUbU9Be1eLXbvFq   
Realm | 745628447-T  
API | PurchaseOrdersSupplierAPI-V1   
Data Center | US  
Environment | TEST  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Client credentials  
Client ID | 4c71c4d4-d7e9-494e-807f-9dead41abc6f   
Client Secret | projects/617888503870/secrets/AribaProcurement/versions/10   
Secret version | 10  
  
## System limitations

The SAP Ariba Procurement connector can process a maximum of 3 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the SAP Ariba Procurement connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the connectors task.

  * To understand how to create and use the connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the connectors task in Application Integration, see [connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section shows how to perform some of the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### CreateChildElementSchema action

This action creates a schema file for an array of documents in the view template.

#### Input parameters of the CreateChildElementSchema action

Parameter name | Type | Accepts output streams | Description  
---|---|---|---  
ViewTemplateName | String | False | The name of an existing view template.  
ChildElement | String | False | A child element or array of documents in the view template in dot notation, such as `LineItems.SplitAccountings`.  
TableName | String | False | The name for the new table, such as `View_LineItems_SplitAccountings`.  
FileName | String | False | The file name for the generated schema. This can be a relative path or an absolute path to the desired save location.  
FileStream | String | True | An instance of an output stream where file data is written to.  
  
For an example about how to configure the `CreateChildElementSchema` action, see Examples.

### CreateSchema action

Creates a schema file for the specified table or view.

#### Input parameters of the CreateSchema action

Parameter name | Type | Accepts output streams | Description  
---|---|---|---  
TableName | String | False | The name for the new table.  
FileName | String | False |  The file name for the generated schema. This can be a relative path or an absolute path to the desired save location.  
FileStream | String | False | An instance of an output stream where file data is written to.  
  
For an example about how to configure the `CreateSchema` action, see Examples.

## Action examples

This section shows how to perform some of the action examples in this connector.

### Example - Create a child element schema

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateChildElementSchema` action, and then click **Done**.
  3. In the **Task Input** section of the **connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ViewTemplateName": "InvoiceReconciliation_SAP_createdRange",
           "ChildElement": "Payments",
           "TableName": "View_LineItems_SplitAccountings"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "FileData": "",
        "Result": "success"
      }
    ]
    




### Example - Create a schema

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateSchema` action, and then click **Done**.
  3. In the **Task Input** section of the **connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "TableName": "Views"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "FileData": "",
        "Result": "success"
      }
    ]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the orders

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Orders` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a filterClause. You can use the filterClause to filter records based on the columns.




### Example - List all the line items

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `LineItems` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **connectors** task, you can set the **filterClause** as per the customer requirement.



### Example - Get an order details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Orders` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entityId to "DO240" which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"DO240"` in the **Input Value** field and choose the entityId as local variable.

You should pass the value for entityId directly, such as "DO240". Here, "DO240" is the unique primary key value.

If passing a single entityId throws an error due to the presence of two composite keys, you can use the filterClause to pass the value, such as `DocumentNumber='DO240'`.




### Example - Get a line item details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `LineItems` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the filterClause to `LineNumber='1' AND DocumentNumber='DO240'` which are the composite keys to be passed. To set the filterClause, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"LineNumber='1' AND DocumentNumber='DO240'"` in the **Input Value** field and choose the filterClause as local variable.



### Example - Create a view

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Views` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId, connectorInputPayload, or filterClause as local variable. 
         
         {
           "ViewTemplateName": "TestView1754629881645",
           "Status": "published",
           "FilterExpressions": "[{\"name\":\"ExampleFilter\",\"field\":\"UniqueName\",\"op\":\"IN\",\"defaultValue\":[\"P011\"]}]",
           "DocumentType": "DirectOrder",
           "SelectAttributes": "[\"SubmitDate\"]"
         }
         

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Success": true
         }
         




### Example - Update a view

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Views` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field. 
         
         {
           "Status": "published"
         }
         

  5. Set the entityId in Data Mapper to the ID of the Views. To set the entityId, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId, connectorInputPayload, or filterClause as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `TestView = '1754629881645'`. 

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
         }
         

An empty JSON object `{}`in the response indicates that the update operation was successful.




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
