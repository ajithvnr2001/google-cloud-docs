---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/saphybrisc4c/configure/
title: SAP Hybris C4C \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:58.688189+00:00
---

# SAP Hybris C4C  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/saphybrisc4c/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP Hybris C4C

The SAP Hybris C4C connector lets you perform insert, delete, update, and read operations on SAP Hybris data.

## Supported versions

This connector supports Version 1.0 of SAP Cloud API.

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
     1. **Connector** : Select **SAP Hybris C4C** from the drop down list of available Connectors.
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
     7. **Tenant** : The SAP Cloud instance to which to establish the connection.
     8. **Use Client Side Paging** : To enable client-side paging in the ADO.NET provider for SAP Cloud, enable this option.
     9. **Use Custom Service** : To enable custom SAP Cloud OData service, enable this option.
     10. **User Defined Views** : Specify the file path to the JSON configuration file that contains your custom views.
     11. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     12. (Optional) To configure a proxy server for the connection, select **Use proxy** and enter the proxy details.
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
     13. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     14. Click **NEXT**.
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

The following authentication types are supported by the SAP Hybris C4C connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Enter the username to authenticate to SAP Cloud.
    * **Password** : Specify the secret manager secret that contains the password associated with the SAP Cloud account.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### Username and password connection type

Field name | Details  
---|---  
Location | asia-east1  
Connector | SAP Hybris C4C  
Connector version | 1  
Connection Name | sap-hybris-c4c-c4codataapi-conn  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Tenant | my335480.crm.ondemand.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Host Address | https://192.0.2.0  
Authentication | User Password  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
  
## System limitations

The SAP Hybris C4C connector can process a maximum of 4 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the SAP Hybris C4C connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the leads from the leads collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select LeadCollection from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** to filter records based on any column. You must pass the value for the filter clause within single quotes.



### Example - Get a lead from the leads collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select LeadCollection from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to "C1A464ABFE7D1EEFACB0E27B8F791046" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"C1A464ABFE7D1EEFACB0E27B8F791046"` in the **Input Value** field and choose the EntityId as the local variable.

Pass the value for the Entity ID directly, such as,"C1A464ABFE7D1EEFACB0E27B8F791046", which is the unique primary key value. If the entity has two composite keys, use the filter clause and pass the value, such as, ObjectID ='C1A464ABFE7D1EEFACB0E27B8F791046'




### Example - Delete a lead from the leads collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select LeadCollection from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to "C1A464ABFE7D1EEFACB0E27B8F791046s" which is the key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"C1A464ABFE7D1EEFACB0E27B8F791046"` in the **Input Value** field and choose the EntityId as the local variable. 

If entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to `ObjectID ='C1A464ABFE7D1EEFACB0E27B8F791046'`.




### Example - Create a lead in the leads collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `LeadCollection` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Googlecloud_Testing", "AccountPartyID": "8000000070" }
         

If the integration is successful, the `LeadCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAF8D279CA432116F" }
         




### Example - Create an opportunity in the oppurtunities collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select OpportunityCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Charlie", "ProspectPartyID": "1", "MainEmployeeResponsiblePartyID": "TESTUPDATEXYZ" }
         

If the integration is successful, the `OpportunityCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A6F0AD1ACA91B5" }
         




### Example - Create a customer order in the item collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CustomerOrderItemCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Description": "This is Customer Order Collection", "ParentObjectID": "D3542BF960751EEFADE1140D7614A0C7", "ProductID": "128" }
         

If the integration is successful, the `CustomerOrderItemCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFB1C28BC1781A71FE" }
         




### Example - Create a contract in the contract collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ContractCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Contract Collection AK" }
         

If the integration is successful, the `ContractCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAFF6ED3FF1EE119E" }
         




### Example - Create a sales quote in the sales quote collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SalesQuoteCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Charlie Cruz" }
         

If the integration is successful, the `SalesQuoteCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAE8A044BF41C112F" }
         




### Example - Create an individual customer in the customers collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select IndividualCustomerCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "RoleCode": "BUP002", "FirstName": "Charlie", "LastName": "Cruz" }
         

If the integration is successful, the `IndividualCustomerCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A0ECAD1B1691B5" }
         




### Example - Create a corporate account in the account collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CorporateAccountCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Charlie S", "RoleCode": "CRM000" }
         

If the integration is successful, the `CorporateAccountCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0901EC0786A51A9" }
         




### Example - Create a partner in the partners collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PartnerCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "HouseNumber": "B-5", "Name": "Charlie", "CountryCode": "US", "City": "Muzzfanagar", "StateCode": "AZ", "POBoxPostalCode": "12345", "StreetPostalCode": "56789", "POBox": "MS" }
         

If the integration is successful, the `PartnerCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFB1CCA349FF68B204" }
         




### Example - Create a competitor in the competitors collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select CompetitorCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         { "Name": "Charlie Cruz", "Phone": "1213446464" }
         

If the integration is successful, the `CompetitorCollection` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAE82734673233121" }
         




### Example - Create a business transaction document in the reference collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select OpportunityBusinessTransactionDocumentReferenceCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
           "ParentObjectID": "07D09F6BEB401EEFB683B9BFCBD63CA1",
           "OpportunityID": "11",
           "ID": "17",
           "TypeCode": "30",
           "BusinessTransactionDocumentRelationshipRoleCode": "2"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAE8A044BF41C112F" }
         




### Example - Create an attachment in the oppurtunities collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select OpportunityAttachmentFolderCollection from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as the local variable. 
         
         {
           "ParentObjectID": "0B7E0B7275361EEFB59B682026F83C0B",
           "TypeCode": "10001",
           "Name": "AttachMs.csv",
           "MimeType": "text/csv",
           "Binary": "c2FtcGxlIHRleHQgaW5zZXJ0"
         }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "ObjectID": "C1A464ABFE7D1EEFAE8A044BF41C112F" }
         

You can add files such as .png, .jpeg, .csv, .jpg, .pdf, .docx, .xlsx, .ppt, and .gif by changing its mime type and binary.




### Example - Update a lead in the leads collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select LeadCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Charlie Cruz" }
         

  5. Set the entity ID in Data Mapper to the entity of the LeadCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB0A54EA52EF251B5'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A54EA52EF251B5" }
         




### Example - Update an opportunity in theopportunities collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select OpportunityCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Charlie Cruz", "ProspectPartyID": "1", "MainEmployeeResponsiblePartyID": "TESTUPDATEXYZ" }
         

  5. Set the entity ID in Data Mapper to the entity of the OpportunityCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB0A6F0AD1ACA91B5'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A6F0AD1ACA91B5" }
         




### Example - Update a sales quote in sales quote collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SalesQuoteCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Charlie Cruz" }
         

  5. Set the entity ID in Data Mapper to the entity of the SalesQuoteCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFAE8A044BF41C112F'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFAE8A044BF41C112F" }
         




### Example - Update a contract in the contracts collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ContractCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Updated Contract Collection" }
         

  5. Set the entity ID in Data Mapper to the entity of the ContractCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFAE8A044BF41C112F'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFAFF6ED3FF1EE119E" }
         




### Example - Update an individual customer in the customers collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select IndividualCustomerCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Email": "baklavainthebalkans@gmail.com", "Mobile": "7037251086" }
         

  5. Set the entity ID in Data Mapper to the entity of the IndividualCustomerCollection. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB0A0ECAD1B1691B5'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A0ECAD1B1691B5" }
         




### Example - Update a survey in the surveys collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select SurveyCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Updated survey from MS" }
         

  5. Set the entity ID in Data Mapper to the entity of the SurveyCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB0EFB26D09DF91D4'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0EFB26D09DF91D4" }
         




### Example - Update a partner in the partners collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select PartnerCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "City": "Paris" }
         

  5. Set the entity ID in Data Mapper to the entity of the PartnerCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB1CCA349FF68B204'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB1CCA349FF68B204" }
         




### Example - Update a service ticket in the service requests collection

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select ServiceRequestCollection from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 
         
         { "Name": "Charlie Cruz 3" }
         

  5. Set the entity ID in Data Mapper to the entity of the ServiceRequestCollection To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as the local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id ='C1A464ABFE7D1EEFB0A358A79B9DD1B5'`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         { "ObjectID": "C1A464ABFE7D1EEFB0A358A79B9DD1B5" }
         




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
