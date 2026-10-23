---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/ldap/configure/
title: LDAP \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:29.468236+00:00
---

# LDAP  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/ldap/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LDAP

The LDAP connector lets you configure a generic LDAP server.

## Supported versions

This connector supports LDAP versions 2 and 3.

## Before you begin

Before using the LDAP connector, do the following tasks:

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
     1. **Connector** : Select **LDAP** from the drop down list of available Connectors.
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
     8. **Base DN** : The base portion of the distinguished name, used for limiting results to specific subtrees. 
     9. **Auth Mechanism** : The authentication mechanism to be used when connecting to the LDAP server. 
     10. **Follow Referrals** : Whether or not to follow LDAP referrals returned by the LDAP server. 
     11. **Friendly GUID** : Whether to return GUID attribute values in a human readable format. 
     12. **Friendly SID** : Whether to return SID attribute values in a human readable format. 
     13. **LDAP Version** : The LDAP version used to connect to and communicate with the server. 
     14. **Scope** : Whether to limit the scope of the search to the whole subtree (BaseDN and all of its descendants), a single level (BaseDN and its direct descendants), or the base object (BaseDN only). 
     15. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     16. Click **NEXT**.
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

The following authentication types are supported by the LDAP connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

## Configure authentication

The LDAP connector supports the basic authentication type. If your destination or LDAP instance is hosted on a VM or is in a private network, [create an endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/connectors/ldap/integration-connectors/docs/network-connectivity-private). For information about how to install and configure LDAP, see [LDAP installation](https://techcommunity.microsoft.com/t5/sql-server-blog/step-by-step-guide-to-setup-ldaps-on-windows-server/ba-p/385362).

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.



### Basic authentication connection type

The following table lists the sample configuration values for the Basic authentication connection type. Field name  | Details   
---|---  
Region  | us-central1   
Connector  | LDAP   
Connector version  | 1   
Connection Name  | google-ldap-basicauth-conn   
Service Account  | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com   
Base DN  | CN=Users,DC=NAME,DC=com   
Auth Mechanism  | SIMPLE   
LDAP Version  | 3   
Scope  | WHOLESUBTREE   
Verbosity Level  | 5   
Minimum number of nodes  | 2   
Maximum number of nodes  | 50   
Username  | USER_NAME   
Password  | PASSWORD   
Secret Version  | 1   
  
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

This section lists all the actions supported by the LDAP connector.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### MoveToDN action

This action moves objects from one DN (distinguished name) to another DN.

#### Input parameters of the MoveToDN action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
DN | String | Yes | The current DN of the object to be moved on the LDAP server. For example, `CN=Google Cloud,OU=Bangalore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com`.  
NewParentDN | String | Yes | The new parent DN of the object. For example, `OU=Mysore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com`.  
  
#### Output parameters of the DownloadFile action

This action returns the status 200 (OK) with a response body indicating the results.

To understand how to configure the `MoveToDN` action, see Action examples.

### GetAttributes action

This action gets all the attribute names and values of a DN.

#### Input parameters of the GetAttributes action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
DN | String | Yes | Distinguished name of the desired LDAP object. If unspecified, the BaseDN from the connection string will be used.  
  
#### Output parameters of the GetAttributes action

This action returns the status 200 (OK) with a response body indicating the results.

To understand how to configure the `GetAttributes` action, see Action examples.

### AddMembersToGroup action

This action adds users to a group.

#### Input parameters of the GetAttributes action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
GroupId | String | Yes | ID of the group to which you want to add the users.  
UserDNs | String | Yes | The UserDNs aggregate or a temporary table that contains the DN of the users to be added to the Group. The value should be the DN of the user record.  
  
#### Output parameters of the AddMembersToGroup action

This action returns the status 200 (OK) with a response body indicating the results.

To understand how to configure the `AddMembersToGroup` action, see Action examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Move an object from one DN to another DN

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveToDN` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "DN": "CN=Google Cloud,OU=Bangalore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com",
         "NewParentDN": "OU=Mysore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com"
         }
           

This example moves an object from one DN to another DN. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": null,
    "result": "[ok]",
    "modified": "true",
    "rss:title": "The movement was successful.",
    "resultcode": "0"
    }]




### Example - Get attributes of a DN

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetAttributes` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "DN": "CN=Bangalore user,OU=Bangalore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com"
         }

This example gets the attribute of the specified DN. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "AttributeName": "_op",
        "AttributeValue": "ldapadoGetAttributes"
      }, {
        "AttributeName": "usncreated",
        "AttributeValue": "36006"
      }, {
        "AttributeName": "countrycode",
        "AttributeValue": "0"
      }, {
        "AttributeName": "badpwdcount",
        "AttributeValue": "0"
      }, {
        "AttributeName": "dn",
        "AttributeValue": ""
      }, {
        "AttributeName": "dn",
        "AttributeValue": "CN=Bangalore user,OU=Bangalore,OU=India,OU=Domain_Users,DC=test-ldap,DC=com"
      }, {
        "AttributeName": "whenchanged",
        "AttributeValue": "20230913125155.0Z"
      }, {
        "AttributeName": "objectclass",
        "AttributeValue": "top"
      }, {
        "AttributeName": "objectclass",
        "AttributeValue": "person"
      }, {
        "AttributeName": "objectclass",
        "AttributeValue": "organizationalPerson"
      }, {
        "AttributeName": "objectclass",
        "AttributeValue": "user"
      }, {
        "AttributeName": "primarygroupid",
        "AttributeValue": "513"
      }, {
        "AttributeName": "givenname",
        "AttributeValue": "Bangalore"
      }, {
        "AttributeName": "dscorepropagationdata",
        "AttributeValue": "16010101000001.0Z"
      }, {
        "AttributeName": "sn",
        "AttributeValue": "user"
      }, {
        "AttributeName": "useraccountcontrol",
        "AttributeValue": "512"
      }, {
        "AttributeName": "cn",
        "AttributeValue": "Bangalore user"
      }, {
        "AttributeName": "codepage",
        "AttributeValue": "0"
      }, {
        "AttributeName": "accountexpires",
        "AttributeValue": "9223372036854775807"
      }, {
        "AttributeName": "userprincipalname",
        "AttributeValue": "user-1@test-l
      }]  
      




### Example - Add users to a group

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddMembersToGroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "GroupId": "1|CN=Cert Publishers,CN=Users,DC=test-ldap,DC=com",
         "UserDNs": "[{\"DN\":\"CN=Google AI,CN=Users,DC=test-ldap,DC=com;CN=Guest,CN=Users,DC=test-ldap,DC=com\"}]"
         }

This example adds a user DN to the group with ID `1|CN=Cert Publishers,CN=Users,DC=test-ldap,DC=com`. If the action is successful, your connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Success": "True"
      }]




## Entity operation examples

### Example - List users

This example lists all the users in the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. Optionally, you can filter the result set. To filter the result set, in the **Task Input** section of the **Connectors** task, set the **filterClause** as per your requirement. 

For example, setting the filter clause to `Id='1|CN=admin,CN=Users,DC=test-ldap,DC=com'`, lists only those records whose Id matches this criteria.




### Example - Get a user record

This example gets a user detail from the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1|CN=admin,CN=Users,DC=test-ldap,DC=com` in the **Default Value** field. 

Here, `1|CN=admin,CN=Users,DC=test-ldap,DC=com` is one of the primary key values of the `User` entity.




### Example - Create a user record

This example creates a user record in the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RDN": "CN=MPATAI",
         "ObjectClass": "top;person;organizationalPerson;user"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": "1|CN=MPATAI,CN=Users,DC=test-ldap,DC=com"
         }




### Example - Update a ticket

This example updates the specified user record in the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
                 "PostalCode": "560040"
               }
               

  5. Click **entityId** , and then enter `1|CN=admin,CN=Users,DC=test-ldap,DC=com` in the **Default Value** field. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `1|CN=admin,CN=Users,DC=test-ldap,DC=com`.

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         {
         "Id": "1|CN=admin,CN=Users,DC=test-ldap,DC=com"
         }
               




### Example - Delete a user record

This example deletes a user record from the `User` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `User` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `1|CN=admin,CN=Users,DC=test-ldap,DC=com` in the **Default Value** field. 
  5. Alternately, if `User` entity has composite primary keys, instead of specifying the **entityId** , you can set the **filterClause**. For example, `Id='1|CN=admin,CN=Users,DC=test-ldap,DC=com' and DN='CN=admin,CN=Users,DC=test-ldap,DC=com'`.



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
base_dn | STRING | True | The base portion of the distinguished name, used for limiting results to specific subtrees.   
auth_mechanism | ENUM | True | The authentication mechanism to be used when connecting to the LDAP server. Supported values are: SIMPLE, DIGESTMD5, NEGOTIATE  
follow_referrals | BOOLEAN | False | Whether or not to follow LDAP referrals returned by the LDAP server.   
friendly_guid | BOOLEAN | False | Whether to return GUID attribute values in a human readable format.   
friendly_sid | BOOLEAN | False | Whether to return SID attribute values in a human readable format.   
ldapversion | ENUM | True | The LDAP version used to connect to and communicate with the server. Supported values are: 2, 3  
scope | ENUM | True | Whether to limit the scope of the search to the whole subtree (BaseDN and all of its descendants), a single level (BaseDN and its direct descendants), or the base object (BaseDN only). Supported values are: WHOLESUBTREE, SINGLELEVEL, BASEOBJECT  
  
## Use the LDAP connection in an integration

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
