---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/oraclesalescloud/configure/
title: Oracle Sales Cloud \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:29.979610+00:00
---

# Oracle Sales Cloud  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/oraclesalescloud/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Oracle Sales Cloud

The Oracle Sales Cloud connector lets you perform insert, delete, update, and read operations on Oracle Sales Cloud data.

## Supported versions

The following is the minimum supported version for this connector: Oracle Sales Cloud 24D (11.13.24.10.0)

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.




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
     1. **Connector** : Select **Oracle Sales Cloud** from the drop down list of available Connectors.
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
     8. **Expand Fields** : The field parameter filters the resource attributes. When running SELECT * queries, if this field is set to true, only the specified attributes are returned. 
     9. **Include Custom Objects** : Specifies whether custom objects are dynamically retrieved. If this property is set to false, custom tables will not be displayed. 
     10. **Connection Timeout** : Specifies the connection timeout in seconds. 
     11. **Generate Schema Files** : Specifies when to generate and save the schemas. You can choose one of the following options: 
        * **Never** : Never generates schema files.
        * **OnUse** : Generates the schema file when a table is referenced for the first time and the schema file doesn't exist.
        * **OnStart** : Generates the schema file for tables that don't have a schema file when the connection is created.
        * **OnCreate** : Generates the schema file when a CREATE TABLE SQL query is run.
  5. (Optional) To configure a proxy server for the connection, select **Use proxy** and enter the proxy details.
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
  6. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
  7. Click **NEXT**.


* In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 

  1. **Destination Type** : Select a **Destination Type**. 
     * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
     * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.



* Click **NEXT**.
* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Oracle Sales Cloud connection:

     * Username and password

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.
    * **Secret version** : Secret version for the secret selected above.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

Field name | Details  
---|---  
Location | europe-west1  
Connector | Oracle Sales Cloud  
Connector version | 1  
Connection Name | oracle-sales-new  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
host1 | https://iaaptz.fa.ocs.oraclecloud.com//td>  
Username | OracleSalesCloudUser  
Password | PASSWORD  
Secret Version | 1  
  
## System limitations

The Oracle Sales Cloud connector can process a maximum of 10 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Oracle Sales Cloud connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section provides examples of how to perform the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List all opportunities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Opportunities` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.

You must use the List operation with filter clause in entities where more than one key is required to retrieve a single record.




### Example - Get contacts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Contacts. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `3046` in the **Input Value** field and choose the EntityId as Local variable.

You must use the Get operation with filter clause in entities where more than one key is required to retrieve a single record.




### Example - Delete opportunities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Opportunities` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to Delete Opportunities. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `203002` in the **Input Value** field and choose the EntityId as Local variable. 

You must use the Delete operation with filter clause in entities where more than one key is required to retrieve a single record.




### Example - Create contacts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "FirstName": "Googlecloud2", "LastName": "TestCreate3" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "PartyNumber": "807006" }
         




### Example - Create contact addresses

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ContactAddresses from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "City": "CreatingAddGooglecloud", "State": "France", "Country": "FR", "Address1": "Googlecloud Contact Address 1", "PartyNumber": "3046" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "AddressNumber": "411001", "PartyNumber": "3046" }
         




### Example - Create accounts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Accounts from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "OrganizationName": "Test Account7Googlecloud", "AddressLine1": "E-City", "City": "Paris", "Country": "FR" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "PartyNumber": "804006" }
         




### Example - Create opportunities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Opportunities from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "Name": "OpportunityGooglecloud1" } 

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "OptyNumber": "203001" }
         




### Example - Create activity assignee

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ActivityAssignee` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "ActivityId": 300000010836710, "AssigneeId": 300000001962681, "ActivityNumber": "212380" }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ActivityAssigneeId": 300000014424799 }
         




### Example - Create activity contact

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ActivityContact` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "ActivityNumber": "212544", "ContactId": 100000001886382 }

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ActivityContactId": 300000014968493 }
         




### Example - Update opportunities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Opportunities` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the EntityID to Opportunities. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `5` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "Name": "Updated Googlecloud Opportunity again" }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    { "OptyNumber": "150364" }
    




### Example - Update accounts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the EntityID to Accounts. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `804006` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "OrganizationName": "updated Test Account7Googlecloud" }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    { "PartyNumber": "804006" }
    




### Example - Update activities

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Activities` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the EntityID to Activities. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `201001` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "ActivityFunctionCode": "APPOINTMENT", "ActivityStartDate": "2025-05-27 07:10:23", "ActivityEndDate": "2025-05-27 08:10:23" }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    { "ActivityNumber": "201001" }
    




### Example - Update contacts

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Contacts` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the EntityID to Contacts. To set the EntityID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `59` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         { "FirstName": "GooglecloudUpdated2", "LastName": "Testlatency3" }
         

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
    
    { "PartyNumber": "807004" }
    




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
expand_fields | BOOLEAN | False | Determines whether the driver will leave the fields URL parameter blank when doing SELECT * queries.   
include_custom_objects | BOOLEAN | False | Specifies whether custom objects must be dynamically retrieved or not. Custom tables will not be displayed unless this property is set to true.   
generate_schema_files | ENUM | False | Indicates the user preference as to when schemas should be generated and saved. Supported values are: Never, OnUse, OnStart, OnCreate  
proxy_enabled | BOOLEAN | False | Specifies whether to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
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
