---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure/
title: Azure AD (Entra ID) \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:43.226795+00:00
---

# Azure AD (Entra ID)  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Azure AD (Entra ID)

The Azure AD (Entra ID) connector lets you perform insert, delete, update, and read operations on Azure Active Directory.

## Before you begin

Before using the Azure AD (Entra ID) connector, do the following tasks:

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

  * Before you create an Azure AD (Entra ID) connection, create an application on Azure Portal/Microsoft Entra ID. For more information, see [Quickstart: Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) and [Register a client application in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Azure AD (Entra ID)** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. **Service Account** : Select a service account that has the required roles.
     6. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     7. To use the connection for event subscriptions, select **Enable event subscription**. Selecting this, displays the following options: 
        * **Enable event subscription with entity and actions** : Select this option to use the connection for both event subscription and connector operations (entities and actions).
        * **Enable only event subscription** : Select this option to use the connection only for event subscription. If you select this option, click **Next** , and then configure event subscription.
     8. **Azure Tenant** : The Microsoft Online tenant being used to access data. If not specified, your default tenant is used. 
     9. **Fetch Extension Properties for Users** : Determines whether to fetch [extension properties](https://learn.microsoft.com/en-us/graph/api/resources/extensionproperty?view=graph-rest-1.0). 
     10. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     11. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Azure AD (Entra ID) connection:

        * Azure AD (Authorization Code Grant Type)
        * OAuth 2.0 Client Credentials
        * OAuth 2.0 Client credentials with JWT bearer

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Configure authentication

Enter the details based on the authentication you want to use.

  * **Azure AD (Authorization Code Grant Type)**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client secret** : The client secret used for requesting access tokens.
    * **Secret version** : The version of the client secret.
    * **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent`. 
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.



  * **OAuth 2.0 Client Credentials**
    * **Client ID** : The client id provided by Azure AD (Entra ID) for the app you created.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret version** : The version of the client secret.


  * **OAuth 2.0 Client credentials with JWT bearer**
    * **Private Key** : Secret Manager Secret containing the contents of the private key file in PEM format. The private key must match the public key/certificate.
    * **Private Key Password** : Secret Manager Secret containing the password (paraphrase) of the private key file.
    * **Secret version** : The version of the private key secret.
    * **Client ID** : The client ID used for requesting access tokens.



### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Azure AD (Entra ID) connection.

#### Azure AD (Auth Code Grant Type) connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Azure AD (Entra ID)  
Connector version | 1  
Connection Name | azure-ad-connection  
Enable Cloud Logging | Yes  
Service Account | XXXX@serviceaccount  
Azure Tenant | 9b25e811-f983-4982-82e4-263c1ca48112  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
Azure AD | Yes  
Client Id | XXXX  
Scope | https://graph.microsoft.com/user.read  
Client Secret | XXXX  
Secret version | 1  
Authorization URL | https://login.microsoftonline.com/9bxxxxxxxxx8112/oauth2/v2.0/authorize?prompt=consent  
Before you specify a value for the Scope field, ensure the following: 

  * You must provide `User.Read.All` and `User.Write.All` permissions at the connection level and at the Azure App level.
  * You can add the remaining scopes both at the Azure AD App registration level and also at connection level according to your requirements.
  * Ensure that permissions are added at the application level for both delegated and application permissions. The following scopes are used commonly: `
    * https://graph.microsoft.com/group.readwrite.all
    * https://graph.microsoft.com/groupmember.readwrite.all
    * https://graph.microsoft.com/user.read.all 
    * https://graph.microsoft.com/user.read 
    * https://graph.microsoft.com/directory.readwrite.all
    * https://graph.microsoft.com/RoleManagement.ReadWrite.Directory 
    * https://graph.microsoft.com/directory.accessasuser.all
    * https://graph.microsoft.com/domain.readwrite.all 
    * https://graph.microsoft.com/device.read.all 
    * https://graph.microsoft.com/RoleManagement.Read.Directory
    * https://graph.microsoft.com/organization.Read.all 
    * https://graph.microsoft.com/Application.ReadWrite.all 
    * https://graph.microsoft.com/AuditLog.Read.All 
    * https://graph.microsoft.com/DeviceLocalCredential.Read.All.
`



#### OAuth 2.0 Client Credentials connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Azure AD (Entra ID)  
Connector version | 1  
Connection Name | azure-ad-client-credentials  
Enable Cloud Logging | Yes  
Service Account | XXXX@serviceaccount  
Azure Tenant | 9b25e811-f983-4982-82e4-263c1ca48112  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
OAuth 2.0 - Client credentials with client secret | Yes  
Client Id | XXXX  
Client Secret | XXXX  
Secret version | 1  
  
#### OAuth 2.0 Client credentials with JWT bearer connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Azure AD (Entra ID)  
Connector version | 1  
Connection Name | azure-jwt  
Enable Cloud Logging | Yes  
Service Account | XXXX@serviceaccount  
Azure Tenant | 9b25e811-f983-4982-82e4-263c1ca48112  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
OAuth 2.0 - Client credentials with JWT bearer | Yes  
Private Key | XXXX  
Secret version | 1  
Client Id | XXXX  
When you use the OAuth 2.0 Client credentials with JWT bearer connection type, complete the following tasks: 

  * Create a self signed certificate and download both the private key certificate and public key. For more information, see [Create Self Signed Certificate](https://certificatetools.com/).
  * Upload the public key certificate in the Azure AD application under Certificates & Secrets.
  * In a private key field, pass both the private key certificate value and the public key certificate value in a single secret key. You needn't create separate secrets for the private and public keys.



For information about establishing connectivity using Postman, see [JWT Connectivity Using API](https://learn.microsoft.com/en-us/answers/questions/1388776/how-to-get-access-token-using-certificate-based-au).

## Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in your Azure AD application, you must re-authorize your Azure AD (Entra ID) connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




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




## Configure event subscription

If you have enabled the event subscription, enter the following values in the **Event Subscription Details** section:

  1. Enter the authentication details. 
     1. **Client ID** : The client ID used for requesting access tokens.
     2. **Client secret** : The client secret used for requesting access tokens.
     3. **Secret version:** Select a secret version.
     4. **Client state** : The Secret Manager Secret containing the client state. This is used for [change notifications](https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks?tabs=http) authentication.
  2. **Azure Tenant** : The Microsoft Online tenant being used to access data. If you don't specify a tenant, your default tenant is used. 
  3. Optionally, select **Enable data enrichment** if you want additional information to be appended to the backend system's response. 

The additional information is specific to the entity for which you have configured the event. For more information, see [Data enrichment in event notifications](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#data-enrichment-in-event-notifications). 

**Note:** If you have configured this connection for only event subscription, you can't enable this option. To enable data enrichment, you must configure the connection for both event subscription and connector operations (entities and actions).
  4. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
  5. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
     1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
     2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
  6. If you want to use a proxy to connect to your backend (for event subscription), enter the following details: 
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

**Tip:** To understand how you can use event subscription in your integrations, see [Azure AD trigger](https://docs.cloud.google.com/application-integration/docs/configure-azuread-trigger). 

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

The Azure AD (Entra ID) connector can process 5 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

### AddGroupMember action

This action adds a member to a group.

#### Input parameters of the AddGroupMember action

Parameter name | Data type | Required | Description  
---|---|---|---  
MemberId | String | Yes | The unique identifier of the member.  
GroupId | String | Yes | The unique identifier of the group.  
  
For an example about how to configure this action, see Action examples.

### RemoveGroupMember action

This action removes a member from a group.

#### Input parameters of the RemoveGroupMember action

Parameter name | Data type | Required | Description  
---|---|---|---  
MemberId | String | Yes | The unique identifier of the member.  
GroupId | String | Yes | The unique identifier of the group.  
  
For an example about how to configure this action, see Examples.

### AddGroupMember(Guest Account) action

This action adds a member to a group.

#### Input parameters of the AddGroupMember action

Parameter name | Data type | Required | Description  
---|---|---|---  
MemberId | String | Yes | The unique identifier of the member.  
GroupId | String | Yes | The unique identifier of the group.  
  
For an example about how to configure this action, see Examples.

### RemoveGroupMember (Guest Account) action

This action removes a member from a group

#### Input parameters of the RemoveGroupMember action

Parameter name | Data type | Required | Description  
---|---|---|---  
MemberId | String | Yes | The unique identifier of the member.  
GroupId | String | Yes | The unique identifier of the group.  
  
For an example about how to configure this action, see Examples.

### AddUserApplicationRoleAssignment action

This action adds a user to an Application Role Assignment.

#### Input parameters of the AddUserApplicationRoleAssignment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ResourceId | String | Yes | The unique identifier of the resource.  
AppRoleId | String | Yes | The unique identifier of the app role.  
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### RemoveUserApplicationRoleAssignment action

This action removes a user from an Application Role Assignment.

#### Input parameters of the RemoveUserApplicationRoleAssignment action

Parameter name | Data type | Required | Description  
---|---|---|---  
AppRoleAssignmentId | String | Yes | The unique identifier of the app role assignment.  
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### AddGroupApplicationRoleAssignment action

This action adds a group to an Application Role Assignment./p>

#### Input parameters of the AddGroupApplicationRoleAssignment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ResourceId | String | Yes | The unique identifier of the resource.  
AppRoleId | String | Yes | The unique identifier of the app role.  
GroupId | String | Yes | The unique identifier of the group  
  
For an example about how to configure this action, see Examples.

### RemoveGroupApplicationRoleAssignment action

This action removes a group from an Application Role Assignment.

#### Input parameters of the RemoveGroupApplicationRoleAssignment action

Parameter name | Data type | Required | Description  
---|---|---|---  
AppRoleAssignmentId | String | Yes | The unique identifier of the app role assignment.  
GroupId | String | Yes | The unique identifier of the group.  
  
For an example about how to configure this action, see Examples.

### ActivateDirectoryRole action

This action activates a directory role.

#### Input parameters of the ActivateDirectoryRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
RoleTemplateId | String | Yes | The Id of the directoryRoleTemplate that the role is based on.  
  
For an example about how to configure this action, see Examples.

### VerifyDomain action

This action verifies a domain.

#### Input parameters of the VerifyDomain action

Parameter name | Data type | Required | Description  
---|---|---|---  
Id | String | Yes | The Id of the domain to be verified.  
  
For an example about how to configure this action, see Examples.

### ChangePassword action

This action changes the password of a user.

#### Input parameters of the ChangePassword action

Parameter name | Data type | Required | Description  
---|---|---|---  
NewPassword | String | Yes | The user's new password.  
CurrentPassword | String | Yes | The user's current password.  
  
For an example about how to configure this action, see Examples.

### ResetPassword action

This action resets the password of a user.

#### Input parameters of the ResetPassword action

Parameter name | Data type | Required | Description  
---|---|---|---  
Password | String | Yes | The user-submitted password to reset it to. If left blank, a system-generated password is created.  
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### AssignLicense action

This action assigns a license to a user.

#### Input parameters of the AssignLicense action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserPrincipalName | String | Yes | The Principal Name of the User for which the license needs to be assigned.Don't provide the username with which you have logged in.  
UserId | String | Yes | The Id of the User for which License needs to be assigned. Don't provide the username with which you have logged in.  
AddLicenseSkuId | String | Yes | The unique identifier for the SKU.  
DisabledPlans | String | No | A collection of the comma separated unique identifiers for plans that have been disabled.  
RemoveLicenses | String | No | A collection of comma separated GUIDs that identify the licenses to remove.  
  
For an example about how to configure this action, see Examples.

### RemoveLicense action

This action removes the license assigned to a user.

#### Input parameters of the RemoveLicense action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserPrincipalName | String | Yes | The Principal Name of the User for which License needs to be assigned. Don't provide the username with which you have logged in.  
UserId | String | Yes | The Id of the User for which License needs to be assigned. Don't provide the username with which you have logged in.  
AddLicenseSkuId | String | No | The unique identifier for the SKU.  
DisabledPlans | String | No | A collection of the comma separated unique identifiers for plans that have been disabled.  
RemoveLicenses | String | Yes | A collection of comma separated GUIDs that identify the licenses to remove.  
  
For an example about how to configure this action, see Examples.

### FetchAdditionalUserFields action

This action retrieves mandatory attribute fields.

#### Input parameters of the FetchAdditionalUserFields action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### AddGroupOwner action

This action adds a owner to a group.

#### Input parameters of the AddGroupOwner action

Parameter name | Data type | Required | Description  
---|---|---|---  
GroupId | String | Yes | The unique identifier of the group.  
OwnerId | String | Yes | The unique identifier of the owner.  
  
For an example about how to configure this action, see Examples.

### RemoveGroupOwner action

This action removes a group owner.

#### Input parameters of the RemoveGroupOwner action

Parameter name | Data type | Required | Description  
---|---|---|---  
GroupId | String | Yes | The unique identifier of the group.  
OwnerId | String | Yes | The unique identifier of the owner.  
  
For an example about how to configure this action, see Examples.

### InviteExternalUser action

This action invites an external user to the organization.

#### Input parameters of the InviteExternalUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserEmailAddress | String | Yes | The email address of the user you are inviting.  
RedirectURL | String | Yes | The URL that the user is redirected to after redemption.  
  
For an example about how to configure this action, see Examples.

### AddPhoneAuthenticationMethod action

This action let users perform specific tasks

#### Input parameters of the AddPhoneAuthenticationMethod action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | Yes | The Id of the User to add a phone authentication method.  
PhoneNumber | String | Yes | The phone number of the authentication method.  
PhoneType | String | Yes | The phone type of the authentication method. Possible values are: mobile, alternateMobile, and office.  
  
For an example about how to configure this action, see Examples.

### RemovePhoneAuthenticationMethod action

This action removes the phone authentication method for a user.

#### Input parameters of the RemovePhoneAuthenticationMethod action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | Yes | The Id of the User to remove a phone authentication method. Don't provide the username with which you have logged in.  
Id | String | Yes | The phone method Id corresponding to the phoneType.  
  
For an example about how to configure this action, see Examples.

### UpdatePhoneAuthenticationMethod action

This action updates the phone authentication method for a user.

#### Input parameters of the UpdatePhoneAuthenticationMethod action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | Yes | The Id of the User to update a phone authentication method.  
Id | String | Yes | The phone method Id corresponding to the phoneType.   
PhoneNumber | String | Yes | The phone number of the authentication method.  
  
For an example about how to configure this action, see Examples.

### AddPrivilegedRole action

This action adds a privileged role for a user.

#### Input parameters of the AddPrivilegedRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
PrincipalId | String | Yes | Identifier of the principal that has been granted the role eligibility.  
RoleDefinitionId | String | Yes | Identifier of the unifiedRoleDefinition object that is being assigned to the principal.   
Justification | String | Yes | A message provided by users and administrators.  
ScheduleInfo | String | Yes | The period of the role eligibility.  
  
For an example about how to configure this action, see Examples.

### RemovePrivilegedRole action

This action removes the privileged role for a user.<

#### Input parameters of the RemovePrivilegedRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
PrincipalId | String | Yes | Identifier of the principal that has been granted the role eligibility.  
RoleDefinitionId | String | Yes | Identifier of the unifiedRoleDefinition object that is being removed to the principal.   
Justification | String | Yes | A message provided by users and administrators.  
  
### RetrieveUserPhoto action

This action retrieves a user photo.

#### Input parameters of the RetrieveUserPhoto action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | Id of the file which you want to download.  
FileLocation | String | No | Where to store the file. Specify the full file path and file name.   
Encoding | String | No | The FileData input encoding type.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if FileLocation is not provided.  
  
For an example about how to configure this action, see Examples.

### UpdateUserPhoto action

This action updates a user photo.

#### Input parameters of the UpdateUserPhoto action

Parameter name | Data type | Required | Description  
---|---|---|---  
LocalFile | String | No | Local file location containing the photo to be uploaded. pecify the full file path and file name.  
ContentStream | String | No | The content as InputStream to be uploaded when localpath or folderpath is not specified   
UserId | String | Yes | Id of the user.  
Content | String | Yes | Photo content to be uploaded.  
  
For an example about how to configure this action, see Examples.

### RemoveUserPhoto action

This action removes a user photo.

#### Input parameters of the RemoveUserPhoto action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | Id of the user.  
  
For an example about how to configure this action, see Examples.

### AssignManager action

This action assigns a manager to a particular user.

#### Input parameters of the AssignManager action

Parameter name | Data type | Required | Description  
---|---|---|---  
ObjectId | String | Yes | The unique identifier of the object.  
ObjectName | String | Yes | The directoryObject, user, or organizational contact object to be added.   
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### RemoveManager action

This action removes the manager assigned to a user.

#### Input parameters of the RemoveManager action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | The unique identifier of the user.  
  
For an example about how to configure this action, see Examples.

### RetrieveManagerChain action

This action retrieves a manager of a user.

#### Input parameters of the RetrieveManagerChain action

Parameter name | Data type | Required | Description  
---|---|---|---  
Levels | String | Yes | The number of levels of managers to retrieve. Specify max to return all managers.  
UserId | String | Yes | The Id of the user.  
  
For an example about how to configure this action, see Examples.

### AddProfileCardProperty action

This action adds a new ProfileCardProperty for an organization.

#### Input parameters of the AddProfileCardProperty action

Parameter name | Data type | Required | Description  
---|---|---|---  
DirectoryPropertyName | String | Yes | Identifies a profileCardProperty resource.  
Annotations | String | Yes | Allows an administrator to set a custom display label for the directory property.  
  
For an example about how to configure this action, see Examples.

The following table lists the permissions required to perform the List and Get operations on profilecardproperties:

Permission | Type  
---|---  
People.Read.All | Application  
PeopleSettings.Read.All | Delegated  
PeopleSettings.Read.All | Application  
  
The following table lists the permissions required to perform the Create action on profilecardproperties:

Permission | Type  
---|---  
PeopleSettings.ReadWrite.All | Application  
PeopleSettings.ReadWrite.All | Delegated  
  
### RemoveProfileCardProperty action

This action removes a ProfileCardProperty for an organization.

#### Input parameters of the RemoveProfileCardProperty action

Parameter name | Data type | Required | Description  
---|---|---|---  
DirectoryPropertyName | String | Yes | Identifies a profileCardProperty resource.  
  
For an example about how to configure this action, see Examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - AddGroupMember

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddGroupMember` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MemberId": "5408040c-fb7d-4c36-8b67-3b66e9edaad3",
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100"
           }
           

This action returns confirmation message of the AddGroupMember If the action is successful, the `AddGroupMember` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveGroupMember

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveGroupMember` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MemberId": "5408040c-fb7d-4c36-8b67-3b66e9edaad3",
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100"
           }
           

If the action is successful, the `RemoveGroupMember` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - AddGroupMember(Guest Account)

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddGroupMember` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MemberId": "735fac93-32df-45c9-b6a3-beee95270a6a",
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100"
           }
           

If the action is successful, the `AddGroupMember` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveGroupMember(Guest Account)

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveGroupMember` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MemberId": "735fac93-32df-45c9-b6a3-beee95270a6a",
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100"
           }
           

If the action is successful, the `RemoveGroupMember` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - AddUserApplicationRoleAssignment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddUserApplicationRoleAssignment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "3558ca6e-2c2e-41d3-a854-bf9249a3c913",
           "ResourceId": "3a914726-ab97-49a0-ab7d-4f742fbc271e",
           "AppRoleId": "820afb79-d975-4da7-8f29-0e2c0cff1217"
           }
           

If the action is successful, the `AddUserApplicationRoleAssignment` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveUserApplicationRoleAssignment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveUserApplicationRoleAssignment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "3558ca6e-2c2e-41d3-a854-bf9249a3c913",
           "AppRoleAssignmentId": "bspYNS4s00GoVL-SSaPJE0xC2--0GxxIu8uS4aeindU"
           }
           

If the action is successful, the `RemoveUserApplicationRoleAssignment` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - AddGroupApplicationRoleAssignment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddGroupApplicationRoleAssignment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ResourceId": "3a914726-ab97-49a0-ab7d-4f742fbc271e",
           "AppRoleId": "820afb79-d975-4da7-8f29-0e2c0cff1217",
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100"
           }
           

If the action is successful, the `AddGroupApplicationRoleAssignment` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveGroupApplicationRoleAssignment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveGroupApplicationRoleAssignment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100",
           "AppRoleAssignmentId": "p3luD3g1tEid3t7Pu3uxAMT7DwI3p29HlrxMuZ143eU"
           }
           

If the action is successful, the `RemoveGroupApplicationRoleAssignment` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - ActivateDirectoryRole

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ActivateDirectoryRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "RoleTemplateId": "f023fd81-a637-4b56-95fd-791ac0226033"
           } 
           

If the action is successful, the `ActivateDirectoryRole` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "id": "c865d9cb-57da-416c-97a3-753e733da678",
      "roleTemplateId": "f023fd81-a637-4b56-95fd-791ac0226033",
      "displayName": "Service Support Administrator",
      "description": "Can read service health information and manage support tickets."
      }]
      




### Example - VerifyDomain

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `VerifyDomain` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Id": "eternalsolarsolutions.com"
           } 
           

If the action is successful, the `VerifyDomain` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - ChangePassword

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ChangePassword` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "NewPassword": "XXX@9876",
           "CurrentPassword": "XXX@123"
           }
           

If the action is successful, the `ChangePassword` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - ResetPassword

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ResetPassword` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Password": "XXX@9876",
           "UserId": "3558ca6e-2c2e-41d3-a854-bf9249a3c913"
           }
           

If the action is successful, the `ResetPassword` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - AssignLicense

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignLicense` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserID": "3558ca6e-2c2e-41d3-a854-bf9249a3c913",
           "UserPrincipalName": "Gcp_test@z8474.onmicrosoft.com",
           "AddLicenseSkuId": "6ec92958-3cc1-49db-95bd-bc6b3798df71"
           }
           

If the action is successful, the `AssignLicense` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveLicense

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignLicense` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserID": "3558ca6e-2c2e-41d3-a854-bf9249a3c913",
           "UserPrincipalName": "Gcp_test@z8474.onmicrosoft.com",
           "RemoveLicenses": "6ec92958-3cc1-49db-95bd-bc6b3798df71"
           }
           

If the action is successful, the `RemoveLicense` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - FetchAdditionalUserFields

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `FetchAdditionalUserFields` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "9630c9d7-cf15-4406-8d21-598e41a058cc"
           } 
           

If the action is successful, the `FetchAdditionalUserFields` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
        "id": "9630c9d7-cf15-4406-8d21-598e41a058cc",
        "deleteddatetime": null,
        "accountenabled": "true",
        "agegroup": null,
        "businessphones": "",
        "city": null,
        "companyname": null,
        "consentprovidedforminor": null,
        "country": null,
        "createddatetime": "2024-04-12T10:24:42Z",
        "creationtype": null,
        "department": null,
        "displayname": "Azure_AD_Test",
        "employeehiredate": null,
        "employeeid": null,
        "employeeleavedatetime": null,
        "employeetype": null,
        "externaluserstate": null,
        "externaluserstatechangedatetime": null,
        "faxnumber": null,
        "givenname": null,
        "imaddresses": "",
        "isresourceaccount": null,
        "jobtitle": null,
        "lastpasswordchangedatetime": "2024-05-14T05:07:15Z",
        "legalagegroupclassification": null,
        "mail": null,
        "mailnickname": "Azure_AD_Test",
        "mobilephone": null,
        "officelocation": null,
        "onpremisesdistinguishedname": null,
        "onpremisesdomainname": null,
        "onpremisesimmutableid": null,
        "onpremiseslastsyncdatetime": null,
        "onpremisessamaccountname": null,
        "onpremisessecurityidentifier": null,
        "onpremisessyncenabled": null,
        "onpremisesuserprincipalname": null,
        "othermails": "",
        "passwordpolicies": null,
        "postalcode": null,
        "preferreddatalocation": null,
        "preferredlanguage": null,
        "proxyaddresses": "",
        "securityidentifier": "S-1-12-1-2519779799-1141296917-2388205965-3428360257",
        "showinaddresslist": null,
        "signinsessionsvalidfromdatetime": "2024-05-14T05:07:15Z",
        "state": null,
        "streetaddress": null,
        "surname": null,
        "usagelocation": "IN",
        "userprincipalname": "Azure_AD_Test@z8474.onmicrosoft.com",
        "usertype": "Member",
        "aboutme": null,
        "birthday": "0001-01-01T08:00:00Z",
        "hiredate": "0001-01-01T08:00:00Z",
        "interests": "",
        "mysite": null,
        "pastprojects": "",
        "preferredname": "",
        "responsibilities": "",
        "schools": "",
        "skills": "",
        "assignedlicenses": "",
        "assignedplans": "[\r\n  {\r\n    \"assignedDateTime\": \"2024-05-16T10:17:45Z\",\r\n    \"capabilityStatus\": \"Deleted\",\r\n    \"service\": \"DynamicsNAV\",\r\n    \"servicePlanId\": \"3f2afeed-6fb5-4bf9-998f-f2912133aead\"\r\n  }\r\n]",
      "authorizationinfo_certificateuserids": "",
      "identities": "[\r\n  {\r\n    \"signInType\": \"userPrincipalName\",\r\n    \"issuer\": \"z8474.onmicrosoft.com\",\r\n    \"issuerAssignedId\": \"Azure_AD_Test@z8474.onmicrosoft.com\"\r\n  }\r\n]",
      "licenseassignmentstates": "",
      "onpremisesextensionattributes_extensionattribute1": null,
      "onpremisesextensionattributes_extensionattribute2": null,
      "onpremisesextensionattributes_extensionattribute3": null,
      "onpremisesextensionattributes_extensionattribute4": null,
      "onpremisesextensionattributes_extensionattribute5": null,
      "onpremisesextensionattributes_extensionattribute6": null,
      "onpremisesextensionattributes_extensionattribute7": null,
      "onpremisesextensionattributes_extensionattribute8": null,
      "onpremisesextensionattributes_extensionattribute9": null,
      "onpremisesextensionattributes_extensionattribute10": null,
      "onpremisesextensionattributes_extensionattribute11": null,
      "onpremisesextensionattributes_extensionattribute12": null,
      "onpremisesextensionattributes_extensionattribute13": null,
      "onpremisesextensionattributes_extensionattribute14": null,
      "onpremisesextensionattributes_extensionattribute15": null,
      "onpremisesprovisioningerrors": "",
      "provisionedplans": "",
      "serviceprovisioningerrors": "",
      "customsecurityattributes": "{\r\n  \"ConnectorTesting\": {\r\n    \"@odata.type\": \"#microsoft.graph.customSecurityAttributeValue\",\r\n    \"FavouriteSport\": \"cricket\",\r\n    \"FavouriteMovie\": \"3 idiots\"\r\n  }\r\n}",
      "signinactivity_lastsignindatetime": "2024-05-14T07:04:51Z",
      "signinactivity_lastsigninrequestid": "ed35b322-d0d9-4fcb-8e71-f9ee7e065e00",
      "signinactivity_lastnoninteractivesignindatetime": "2024-05-15T09:00:02Z",
      "signinactivity_lastnoninteractivesigninrequestid": "0d4ce88b-710a-440f-a612-f590954d6800",
      "signinactivity_lastsuccessfulsignindatetime": "2024-05-15T06:45:42Z",
      "signinactivity_lastsuccessfulsigninrequestid": "64643e9d-3468-4e4d-b7c3-8bd316956600"
      }  
      


**Note:**

  * By default, the entity retrieves the mandatory attributes coming from the Azure AD OData endpoint.
  * For any custom attribute, the `FetchAdditionalUserFields` stored procedure takes userID as an input and provides entire attributes as a part of result. 



### Example - AddGroupOwner

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddGroupOwner` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100",
           "OwnerId": "9630c9d7-cf15-4406-8d21-598e41a058cc"
           }
           

f the action is successful, the `AddGroupOwner` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemoveGroupOwner

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveGroupOwner` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "GroupId": "0f6e79a7-3578-48b4-9dde-decfbb7bb100",
           "OwnerId": "9630c9d7-cf15-4406-8d21-598e41a058cc"
           }
           

If the action is successful, the `RemoveGroupOwner` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - InviteExternalUser

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `InviteExternalUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserEmailAddress": "taleprajyot97@gmail.com",
           "RedirectURL": "https://www.example.com"
           }
           

This action returns confirmation message of the InviteExternalUser If the action is successful, the `InviteExternalUser` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True",
      "Id": "70905aef-361f-4cb1-8d04-41f9e377ebd3",
      "ReedemURL": "https://login.microsoftonline.com/redeem?rd=https%3a%2f%2finvitations.microsoft.com%2fredeem%2f%3ftenant%3d9b25e811-f983-4982-82e4-263c1ca48112%26user%3d70905aef-361f-4cb1-8d04-41f9e377ebd3%26ticket%3dx5aOZc%25252bE9XslKcOdb101qLnoe2V%25252b8%25252beeFlNhYA5WvTg%25253d%26ver%3d2.0",
      "InvitedUserId": "d5eeb199-a544-4985-b726-e3073751050c"
      }]
      




### Example - AddPhoneAuthenticationMethod

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddPhoneAuthenticationMethod` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PhoneType": "mobile",
           "UserID": "93e42f0d-74d7-445b-b15a-dd6ceb013d81",
           "PhoneNumber": "+91 9898989890"
           }
           

If the action is successful, the `AddPhoneAuthenticationMethod` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RemovePhoneAuthenticationMethod

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemovePhoneAuthenticationMethod` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PhoneType": "mobile",
           "UserID": "93e42f0d-74d7-445b-b15a-dd6ceb013d81",
           "PhoneNumber": "+91 9898989890"
           }
           

If the action is successful, the `RemovePhoneAuthenticationMethod` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - UpdatePhoneAuthenticationMethod

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdatePhoneAuthenticationMethod` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "securityComplianceNotificationPhones": "9899999999",
           "securityComplianceNotificationMails": "abc@gmail.com"
           }
           

If the action is successful, the `UpdatePhoneAuthenticationMethod` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - AddPrivilegedRole

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddPrivilegedRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PrincipalId": "8cbe82b6-0dd5-4f10-bf67-82bf88ac6cb8",
           "RoleDefinitionId": "729827e3-9c14-49f7-bb1b-9608f156bbb8",
           "Justification": "Add Privileged Role",
           "ScheduleInfo": "{\n\"StartDateTime\" : \"2022-09-09T21:31:27.91Z\",\n\"Expiration\"    : {\n\"Type\"        : \"Eligible\"}\n}"
           }
           

If the action is successful, the `AddPrivilegedRole` task's `connectorOutputPayload` response parameter has a value similar to the following:ç 
    
    [{
      "Success": "True"
      }]
      




### Example - RemovePrivilegedRole

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemovePrivilegedRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "PrincipalId": "8cbe82b6-0dd5-4f10-bf67-82bf88ac6cb8",
           "RoleDefinitionId": "729827e3-9c14-49f7-bb1b-9608f156bbb8",
           "Justification": "Removing Privileage Role"
           }
           

If the action is successful, the `RemovePrivilegedRole` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Success": "True"
      }]
      




### Example - RetrieveUserPhoto

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RetrieveUserPhoto` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "8e22c728-c523-436b-8f46-3b21cc1b5f80"
           } 
           

If the action is successful, the `RetrieveUserPhoto` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
        "Status": "Success",
        "FileData": "77+9UE5HDQoaCgAAAA1JSERSAAADUgAAAjYIBgAAAFo077+977+9AAAAAXNSR0IA77+977+9HO+/vQAAAARnQU1BAADvv73vv70L77+9YQUAAAAJcEhZcwAADu+/vQAADu+/vQHvv71v77+9ZAAA77+977+9SURBVHhe77+977+9ZXwcV9K+LWlmZCbvv71O77+977+977+9ZO+/vcmG77+9Ge+/vThmZmZm77+9OO+/vcmG77+977+9MTMzM++/vS0z77+977+977+9eu+/ve+/vXTvv71o77+9KAvvv73vv73vv71w77+9DjRO77+977+9Vl3vv70677+9KWsrR2zvv71zEe+/ve+/vUTvv73vv717KGrvv709EO+/ve+/vWjvv71RG01777+977+9Me+/ve+/vWjvv73vv719OmJLyqfZuu+/vRHvv71ZK++/vQ7Uj9iJ77+977+9du+/vUXEslrvv73vv73vv70uzbzvv70pFu+/vUrvv709Yl4P77+9eu+/vSDvv73vv71n77+977+977+9Gu+/ve+/vV3vv71sP2Vm77+977+9be+/vWbvv707RmxV77+9VFvvv70u77+9Fu+/ve+/vdqi77+9aTbvv71N77+977+9Re+/ve+/vWPvv70tYe+/vRXvv73vv70677+9bu+/vTRbS++/ve+/ve+/vWxkP1vvv71FbWt377+977+9LdW277+977+977+977+977+9ae+/ve+/vXvvv73vv73vv70Z77+9Xe+/vSLvv73vv70X77+977+9E++/vT1ob1/vv71+ae+/ve+/vWx3by1P77+9XT3vv71sL++/ve+/ve+/vWbvv73vv73vv71m77+9F+e0s2vvv712dErvv73vv73vv73vv73vv73vv71p77+977+9Le+/vW/vv73vv71oZ0vvv73vv70577+9R3tb77+92b7vv70R77+977+9KmIHKQ/vv73vv73agdapdu+/vU3vv73vv73vv73vv73vv71zXe+/ve+/ve+/ve+/ve+/vRTvv70777+977+977+96pqK77+9LO+/vXN077+9PO+/ve+/ve+/vVp2f++/vdOgNO+/ve+/veyBlO+/ve+/vQdQ77+9cO+/vTc477+9bBDvv71S77+977+977+977+9Zu+/ve+/vW8I77+977+977+9ZQ8paFnvv70LWnxwYe+/ve+/vVEWNBvvv71O77+977+9eQMKW++/vV8x77+977+9FO+/vd6k77+977+9LmHvv70eRS3erQBiG++/vXXvv71DzLI577+9LO+/vT3vv73vv71077+9Ze+/ve+/ve+/vTcebe+/vWbvv73vv71E77+9UEPvv71r77+9NMus77+9Zu+/ve+/vUVsXe+/ve+/ve+/ve+/ve+/vWZr77+9c29qRG0177+9VdWi77+977+9eu+/ve+/ve+/vUlfTe+/ve+/vW/vv73NujVTbX3vv73vv73vv73vv70V77+9He+/ve+/vXUj77+977+9AdeeMe+/ve+/ve+/ve+/ve+/ve+/vQHvv73vv70Y77+9aFcj77+9Y2Pvv700Zjtpb2vvv73vv73vv73vv73ZmHvXnHvvv70Y77+904Lvv73vv70y77+977+9EO+/ve+/vRjvv73vv71077+9dDvbs++/ve+/vXsX4bqU77+9Wu+/vVsH77+977+977+977+9P1vvv73vv70y77+9fO+/ve+/vV8pZd6rJe+/vXvvv70cy6Yef++/ve+/vWXvv71U1LJf77+9Wg3vv73vv71j1otF77+9NO+/ve+/vQTvv73vv70A77+9SO+/vWZHD++/vQ3vv71ta++/ve+/ve+/veO+rmDvv73vv73vv71c77+9cD1+77+9Hu+/ve+/vSpG77+977+9Y++/ve+/vWfvv73vv73vv70zMXvvv73vv73vv73
      ...[too long to view on UI. Please use the API to view the full content.]
      




### Example - UpdateUserPhoto

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateUserPhoto` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "9630c9d7-cf15-4406-8d21-598e41a058cc",
           "Content": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAI2CAIAAADVVi6oAAAgAElEQVR4AZy9d3Rc1dX3r3POHVmWrG6ckIQHN0gCCYEkT/IkJA89lARc1Xsf1ZlR78W2iis4BFuybMAFMMW4qctFknu31XvvzTbu0tx9fmufOzMWJe+b97fWXmede2ekBYs/8sm3bJm1uLAry9jJt2jFq9Khl6XDL0vFr0ilr0pHXlMdf52ee5tdXU5b3diAN50IYHdCyYMINh1FIJpCnJmcRCGFQSqBdDNIJzhp5H4Su5FIx5PYYDzrjaVdcaxRS+qjyWWNdFlHL2jZBR27ECNdiqNX41l9HG1MYI0JtCWBtSTSjiTWnSz1pNCuZNKXKvWl0e4U0p/GhtLZcDodz2QjmWw0i42soiOZdDiDDaXToVQ6ms76k2lvEuuKZ71xbCBJ6o+nA7F0IIb260ifhg5p6EAkHdGycS0bjaJjGjYWxSY17IZOmtCQ61p6P0a6HU1vRtPbsfRePH2QQO8lkXtJdDqN4aRTfRbRryaQQ+Ucqs+mshj9GiqvocpLyKU8h0CueMwmPJtCDoE8CtlMn2cxnWsh51pCnrWca8FzzSHPAtZYyqusIdMG0s15hq2cOkdOniUnW8hxVI5V6WPpdDSd1kn3IsndKPZNOL2hZteD6HgAHfSnff6s1ZM1u9NmD9biKTW500Z3qdGDNnmxFi+pyYO2+7BWL9Lmy9q8WbuP1OHHegJZVwDr8qc9gawvkPYF0cEgOhTMhkPYcKhqIIj2BpP+IDoQQkfD2WgEG4mgY5EqPCPodS27FUfvJ5lPpVnJGVaQbS9n28o5c+V1j+rXzYWN8+RN9vCuLWyep99kL2901G+Yo19rAevw33p6vdX9XPM72Wwiiw2l0v5U1p9Ge1Kk1gRaH8dOR7Ayf/alh2qnk7RjhWrbUmnLO6p332DrX6fZr0iZL7KUF1jCn1TaP86K/P2siN9Zhj43R/1b68DfWPv+ysbrlw5uT9g6L7JducjeeZGjy6J5zo/buyxwdF9g77nIwfcJ+9Bfzo34pX3MMw4Jv7LP/K3tpj/b5L9gu/0Fq89fn130zpzyFXNOONuecZ1z0WtOnd+ctiDrjkCbwTDH4Qjrm9qf3on9yd34H02n/Jc+9TFIf1xOX6hPexwyF0Da49NJj00nPXYndt7tuB9N6hyGImx71datfrOueNHTrtKR5axkmVS2fHaN67wLvovq1c+26f7cl/zqZPbye5u99NuC4JMI2B8LFelwIodffg/qtkBzIbTthI5dvHMP7/4cp+dL3vcVH9jPBw/CUDEfKYPRMj5Wzscq+dgRPirOh5dK8VH5d04YKYVR8YOj5TBSir9kpIwPlcJwKQyXwHAJFwNDxfg4VGx6lAcP8YGHA/0H8bH/EO8Tl76DeOk7CP378Z+wfx/v3wf9+6Dva7kXT+jbB31fQe9X0P0V79mH0/0V71LmS979BXR9bjp59xe86wve+Tl07OWdnxtnL+/cCx2fKcM7PoP2T6H9Uy5OaPuEt38C7Z/wtj3Qsou37sZp2cNb9sgte3gzDjTv4U27efNO3vwxb/4Ip0lM807etBMaP4KGHdCwgzd+iO8bP+SNH0KT4aXhfcN2qC/k9dvlum1Qvw3qxGPdNj5joN74WFsw8z3eDW8KeJ34qLYA3xhHrsuH+nxel89r83ndVsPP1hZA7VbAx628Lh8atvLGfF6/Va4v4LVbceryeaPxfWM+NObzhgLegC+VAeXeUIAX/KgA3xu/gL+wYSv+lGmMH+GbpgLT4HdmPP7f780FvHnrw2nZyvHNNpyWfN4i7k3boLmAt4pp2cZbC7npbNnGWwrxo5Z8aM0X39kGbQWG6djK2/OhrYC35z+cjnxow/e8Ix/E8M4C6MjnnQUPp2sb79qGj8rZOeOufPS9E7rF
           ...[too long to view on UI. Please use the API to view the full content.]
           

If the action is successful, the `UpdateUserPhoto` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Status": "Success"
      }]
      




### Example - RemoveUserPhoto

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveUserPhoto` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "9630c9d7-cf15-4406-8d21-598e41a058cc"
           } 
           

If the action is successful, the `RemoveUserPhoto` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Status": "Success"
      }]
      




### Example - AssignManager

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignManager` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "3558ca6e-2c2e-41d3-a854-bf9249a3c913",
           "ObjectId": "8cbe82b6-0dd5-4f10-bf67-82bf88ac6cb8",
           "ObjectName": "users"
           }
           

If the action is successful, the `AssignManager` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Status": "True"
      }]
      




### Example - RemoveManager

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveManager` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "3558ca6e-2c2e-41d3-a854-bf9249a3c913"
           } 
           

If the action is successful, the `RemoveManager` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "Status": "True"
      }]
      




### Example - RetrieveManagerChain

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RetrieveManagerChain` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "UserId": "8cbe82b6-0dd5-4f10-bf67-82bf88ac6cb8",
           "Levels": "max"
           }
           

If the action is successful, the `RetrieveManagerChain` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
      "id": "8cbe82b6-0dd5-4f10-bf67-82bf88ac6cb8",
      "displayName": "test1",
      "manager": "{\r\n  \"@odata.type\": \"#microsoft.graph.user\",\r\n  \"id\": \"9630c9d7-cf15-4406-8d21-598e41a058cc\",\r\n  \"deletedDateTime\": null,\r\n  \"accountEnabled\": true,\r\n  \"ageGroup\": null,\r\n  \"businessPhones\": [],\r\n  \"city\": null,\r\n  \"companyName\": null,\r\n  \"consentProvidedForMinor\": null,\r\n  \"country\": null,\r\n  \"createdDateTime\": \"2024-04-12T10:24:42Z\",\r\n  \"creationType\": null,\r\n  \"department\": null,\r\n  \"displayName\": \"Azure_AD_Test\",\r\n  \"employeeId\": null,\r\n  \"employeeHireDate\": null,\r\n  \"employeeLeaveDateTime\": null,\r\n  \"employeeType\": null,\r\n  \"externalUserState\": null,\r\n  \"externalUserStateChangeDateTime\": null,\r\n  \"faxNumber\": null,\r\n  \"givenName\": null,\r\n  \"isLicenseReconciliationNeeded\": false,\r\n  \"jobTitle\": null,\r\n  \"legalAgeGroupClassification\": null,\r\n  \"mail\": null,\r\n  \"mailNickname\": \"Azure_AD_Test\",\r\n  \"mobilePhone\": null,\r\n  \"onPremisesDistinguishedName\": null,\r\n  \"onPremisesDomainName\": null,\r\n  \"onPremisesImmutableId\": null,\r\n  \"onPremisesLastSyncDateTime\": null,\r\n  \"onPremisesSecurityIdentifier\": null,\r\n  \"onPremisesSamAccountName\": null,\r\n  \"onPremisesSyncEnabled\": null,\r\n  \"onPremisesUserPrincipalName\": null,\r\n  \"otherMails\": [],\r\n  \"passwordPolicies\": null,\r\n  \"officeLocation\": null,\r\n  \"postalCode\": null,\r\n  \"preferredDataLocation\": null,\r\n  \"preferredLanguage\": null,\r\n  \"proxyAddresses\": [],\r\n  \"refreshTokensValidFromDateTime\": \"2024-05-14T05:07:15Z\",\r\n  \"imAddresses\": [],\r\n  \"isResourceAccount\": null,\r\n  \"showInAddressList\": null,\r\n  \"securityIdentifier\": \"S-1-12-1-2519779799-1141296917-2388205965-3428360257\",\r\n  \"signInSessionsValidFromDateTime\": \"2024-05-14T05:07:15Z\",\r\n  \"state\": null,\r\n  \"streetAddress\": null,\r\n  \"surname\": null,\r\n  \"usageLocat
      ...[too long to view on UI. Please use the API to view the full content.]
      




### Example - AddProfileCardProperty

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddProfileCardProperty` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Annotations": "[{"displayName": "Attributes"}]",
         "DirectoryPropertyName": "CustomAttribute15"
         }

If the action is successful, the `AddProfileCardProperty` task's `connectorOutputPayload` response parameter has a value similar to the following:
    
    [{
    "Status": "True"
    }]




### Example - RemoveProfileCardProperty

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RemoveProfileCardProperty` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "DirectoryPropertyName": "CustomAttribute12"
         } 

If the action is successful, the `RemoveProfileCardProperty` task's `connectorOutputPayload` response parameter has a value similar to the following: 
    
    [{
    "Status": "True"
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List the groups

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Groups from the `Entity` list.
  3. Select the `LIST` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.



You must use single quotes (') to enclose the value for filter clause. You can use the filter clause to filter records based on the columns. 

#### You can also perform LIST operations on the following entities:

  * User
  * GroupMembers
  * Domains
  * RoleAssignments
  * Applications
  * Devices
  * Contacts
  * DirectoryRoleTemplates
  * DirectoryRoles
  * AdministrativeUnits
  * SubscribedSKUs
  * PhoneAuthenticationMethod
  * Organization
  * DeviceLocalCredentials
  * ProfileCardProperties



### Example - Get a single record from the group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Groups from the `Entity` list.
  3. Select the `GET` operation, and then click **Done**.
  4. Set the entity ID to "bb4756c7-38c0-426b-97aa-03b6443e7f16" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"bb4756c7-38c0-426b-97aa-03b6443e7f16"` in the **Input Value** field and choose the EntityId as Local variable. 

**Note:**
* You must pass the Entity ID value directly, such as, "bb4756c7-38c0-426b-97aa-03b6443e7f16". Here "bb4756c7-38c0-426b-97aa-03b6443e7f16" is the unique primary key value.
* If two composite keys are present, then passing a Entity Id might throw an error. In such cases, you can use the filter clause, such as,id='bb4756c7-38c0-426b-97aa-03b6443e7f16'.

#### You can also perform GET operations on the following entities:

  * User
  * GroupMembers
  * Domains
  * RoleAssignments
  * Applications
  * Devices
  * Contacts
  * DirectoryRoleTemplates
  * DirectoryRoles
  * AdministrativeUnits
  * PhoneAuthenticationMethod
  * Organization
  * UserManagers
  * DeviceLocalCredentials



### Example - Delete a record from the group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Groups from the `Entity` list.
  3. Select the `DELETE` operation, and then click **Done**.
  4. Set the entity ID to "62008bbe-effa-4341-9d29-eac7f67b84fe", which is the key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"62008bbe-effa-4341-9d29-eac7f67b84fe"` in the **Input Value** field and choose the EntityId as Local variable. 

If two composite or primary keys are present, then passing a Entity Id might throw an error. In such cases, you can use the filter clause, such as,` id='62008bbe-effa-4341-9d29-eac7f67b84fe'`.




#### You can also perform DELETE operations on the following entities:

* User
* Domains
* Applications
* Devices

### Example - Create a group (Microsoft 365) entity

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Groups from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "securityEnabled": true,
         "displayName": "GoogleGCP",
         "description": "This Group is creating for gcp testing.",
         "mailEnabled": false,
         "mailNickname": "GoogleGCP",
         "groupTypes": "Unified"
         }

This example creates the Groups records. If the integration is successful, the `Groups` task's `connectorOutputPayload` response parameter has a value similar to the following:
         
         {
         "id": "30fc13b3-79b3-4ac5-a3ba-684d4e887ecc"
         } 




### Example - Update a user

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Users from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
         "jobTitle": "Software Engineer"
         }

  5. Set the entity ID in Data Mapper to the entity of the Users. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as a local variable. 

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `7ad59ec3-1c37-4932-be51-7513fe98c3c3`.

This example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
         "id": "7ad59ec3-1c37-4932-be51-7513fe98c3c3"
         } 




## Use the Azure AD (Entra ID) connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



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
