---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/okta/configure/
title: Okta \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:43.256352+00:00
---

# Okta  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/okta/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Okta

You can use the Okta connector to create, read, update, and delete user, group, role, and app records, along with assigning or unassigning users or groups to roles and applications.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.




## Create an Okta connection

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. Select **Okta** from the **Connector** list.
     2. Select a connector version from the **Connector version** list. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
  5. Optionally, enter a **Description** for the connection instance.
  6. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
  7. **Service Account** : Select a service account that has the required roles.
  8. (Optional) Configure the **Connection node settings**.
     * **Minimum number of nodes** : Enter the minimum number of connection nodes.
     * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
  9. **Domain** : Enter an Okta domain to connect to the Okta instance.
  10. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
  11. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Okta connection:

     * OAuth 2.0 - Authorization code
     * OAuth 2.0 Client credentials with JWT bearer

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - Authorization code**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client secret** : The client secret used for requesting access tokens.
    * **Authorization URL** : The authorization URL generated when creating client.

For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.



  * **OAuth 2.0 - Client credentials with JWT bearer**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Private Key** : Secret Manager Secret containing the contents of the private key file in PEM format. The private key must match the public key/certificate.



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

If you are using `Authorization code` authentication type and have made any configuration changes, you must re-authorize your Okta connection. To re-authorize a connection, perform the following steps:

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

The Okta connector can process a maximum of one transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Okta connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section lists the actions supported by the Okta connector. To understand how to configure the actions, see Action examples.

### ReactivateUser action

This action reactivates a user.

#### Input parameters of the ReactivateUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
  
For example on how to configure the `ReactivateUser` action, see ActivateUser Example.

### ActivateUser action

This action activates a user.

#### Input parameters of the ActivateUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
  
For example on how to configure the `ActivateUser` action, see ActivateUser Example.

### DeactivateUser action

This action deactivates a user.

#### Input parameters of the DeactivateUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
  
For example on how to configure the `DeactivateUser` action, see DeactivateUser Example.

### Assignusertogroup action

This action assigns a user to a group.

#### Input parameters of the Assignusertogroup action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
GroupID | String | True | The ID of the Group.  
  
For example on how to configure the `Assignusertogroup` action, see Assignusertogroup Example.

### UnassignUsertoRole action

This action unassigns a user from a role.

#### Input parameters of the UnassignUsertoRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
RoleAssignmentId | String | True | The ID of the Role.  
  
For example on how to configure the `UnassignUsertoRole` action, see UnassignUsertoRole Example.

### AssignUsertoRole action

This action assigns a user to a role.

#### Input parameters of the AssignUsertoRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
RoleId | String | True | The ID of the Role.  
  
For example on how to configure the `AssignUsertoRole` action, see AssignUsertoRole Example.

### AssignUsertoApp action

This action assigns a user to an app.

#### Input parameters of the AssignUsertoApp action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
AppId | String | True | The ID of the App.  
  
For example on how to configure the `AssignUsertoApp` action, see AssignUsertoApp Example.

### UnassignUsertoGroup action

This action unassigns a user from a group.

#### Input parameters of the UnassignUsertoGroup action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
GroupID | String | True | The ID of the Group.  
  
For example on how to configure the `UnassignUsertoGroup` action, see UnassignUsertoGroup Example.

### UnassignUsertoApp action

This action unassigns a user from an App.

#### Input parameters of the UnassignUsertoApp action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserID | String | True | The ID of the user.  
AppID | String | True | The ID of the App.  
  
For example on how to configure the `UnassignUsertoApp` action, see UnassignUsertoApp Example.

### Assigngrouptoapp action

This action assigns a group to an app.

#### Input parameters of the Assigngrouptoapp action

Parameter name | Data type | Required | Description  
---|---|---|---  
GroupId | String | True | The ID of the Group.  
AppID | String | True | The ID of the App.  
  
For example on how to configure the `Assigngrouptoapp` action, see Assigngrouptoapp Example.

### AssignGrouptoRole action

This action assigns a group to a role.

#### Input parameters of the AssignGrouptoRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
GroupId | String | True | The ID of the Group  
RoleId | String | True | The ID of the Role  
TypeId | String | True | The ID of the Type  
  
For example on how to configure the `AssignGrouptoRole` action, see AssignGrouptoRole Example.

### UnassignGrouptoApp action

This action unassigns a group from an app.

#### Input parameters of the UnassignGrouptoApp action

Parameter name | Data type | Required | Description  
---|---|---|---  
Group | String | True | The ID of the GroupId  
AppID | String | True | The ID of the App  
  
For example on how to configure the `UnassignGrouptoApp` action, see UnassignGrouptoApp Example.

### UnassignGrouptoRole action

This action unassigns a group from a role.

#### Input parameters of the UnassignGrouptoRole action

Parameter name | Data type | Required | Description  
---|---|---|---  
Group | String | True | The ID of the GroupId  
AppID | String | True | The ID of the AppId  
  
For example on how to configure the `UnassignGrouptoRole` action, see UnassignGrouptoRole Example.

### SuspendUser action

This action suspends a user.

#### Input parameters of the SuspendUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
Group | String | True | The ID of the GroupId.  
AppID | String | True | The ID of the AppId.  
  
For example on how to configure the `SuspendUser` action, see SuspendUser Example.

### UnsuspendUser action

This action unsuspends a user.

#### Input parameters of the UnsuspendUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
Group | String | True | The ID of the GroupId.  
AppID | String | True | The ID of the AppId.  
  
For example on how to configure the `UnsuspendUser` action, see UnsuspendUser Example.

## Action examples

### Example - Reactivate a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ReactivateUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ulgqf2s4Zs5Ohge5d7"
         }
         

If the action is successful, the `ReactivateUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    { 
        "Status": "Success",
        "ActivationToken": "PKeQTJMUW9vg0wyh8czA",
        "ActivationUrl": "https://dev-99779501.okta.com/tokens/PKeQTJMUW9vg0wyh8czA/verify" 
    }
    




### Example - Activate a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ActivateUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ulgqf2s4Zs5Ohge5d7"
         }
         
         

If the action is successful, the `ActivateUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    { 
      "Status": "Success",
        "activationurl": null,
        "activationtoken": null
    }
    




### Example - Deactivate a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeactivateUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ulgqf2s4Zs5Ohge5d7"
         }
         

If the action is successful, the `DeactivateUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    { 
     "Status": "Success",
    "activationurl": null,
    "activationtoken": null 
    } 
    
    




### Example - Assign a user to a group

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Assignusertogroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ulgqf2s4Zs5Ohge5d7",
             "GroupId": "7463874b834938475d"
         }
         

If the action is successful, the `Assignusertogroup` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
     "Status": "Success",
    }
    




### Example - Unassign a user from a role

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnassignUsertoRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ukxucmpl25SNLP65d7",
             "RoleAssignmentId": "irblawnjpom1bLBcJ5d7"
         }
         

If the action is successful, the `UnassignUsertoRole` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
     "Status": "Success",
    }
    




### Example - Assign a user to a role

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignUsertoRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "UserId": "00ukxucmpl25SNLP65d7",
         "RoleId": "cr0l2n9ay0pCCxLgG5d7",
         "ResourceSet": "iaml81kep6zefR4Oq5d7",
         "Type": "CUSTOM"
         }
         

If the action is successful, the `AssignUsertoRole` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
     "Status": "Success",
        "Id": "irblawfe99RsUfILD5d7",
        "Label": "UserCreatorByabhishkePostman",
        "Type": "CUSTOM", 
        "Created": "2024-11-21 07:33:05.0",
        "LastUpdated": "2024-11-21 07:33:05.0",
        "AssignmentStatus": "ACTIVE",
        "AssignmentType": "USER",
        "resource-set": "iaml81kep6zefR4Oq5d7",
        "role": "cr0l2n9ay0pCCxLgG5d7",
        "_links_role_href": "https://dev-99779501-admin.okta.com/api/v1/iam/roles/cr0l2n9ay0pCCxLgG5d7",
        "_links_resource-set_href": "https://dev-99779501.okta.com/api/v1/iam/resource-sets/iaml81kep6zefR4Oq5d7",
        "_links_permissions_href": "https://dev-99779501-admin.okta.com/api/v1/iam/roles/cr0l2n9ay0pCCxLgG5d7/permissions",
        "_links_member_href": "https://dev-99779501.okta.com/api/v1/iam/resource-sets/iaml81kep6zefR4Oq5d7/bindings/cr0l2n9ay0pCCxLgG5d7/members/irblawfe99RsUfILD5d7",
        "_links_assignee_href": "https://dev-99779501.okta.com/api/v1/users/00ukxucmpl25SNLP65d7"
    
    }
    




### Example - Assign a user to an app

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignUsertoApp` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ukxucmpl25SNLP65d7",
             "AppId": "0oakn3j0bfGPR1Esk5d7"
         }
         

If the action is successful, the `AssignUsertoApp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
        "Status": "Success",
        "Id": "00ukxucmpl25SNLP65d7",
        "Created": "2024-11-21 07:08:40.0",
        "LastUpdated": "2024-11-21 07:08:45.0",
        "Scope": "USER",
        "AssignmentStatus": "ACTIVE",
        "externalid": null, 
        "statuschanged": "2024-11-21T07:08:40.000Z",
        "passwordchanged": null,
        "syncstate": "DISABLED",
        "credentials_username": "baklavainthebalkans@gmail.com",
        "profile_street_address": null,
        "profile_country": null, 
        "profile_website": null,
        "profile_zoneinfo": "America/Los_Angeles",
        "profile_birthdate": null,
        "profile_gender": null,
        "profile_formatted": null,
        "profile_profile": null,
        "profile_locality": null,
        "profile_given_name": "Baklavainthe",
        "profile_middle_name": null,
        le_phone_number": null,
        "profile_region": null,
        "profile_postal_code": null,
        "profile_family_name": "Balkans",
        "profile_email": "baklavainthebalkans@gmail.com",
        "_links_app_href": "https://dev-99779501.okta.com/api/v1/apps/0oakn3j0bfGPR1Esk5d7", 
        "_links_user_href": "https://dev-99779501.okta.com/api/v1/users/00ukxucmpl25SNLP65d7"
    
    }
    




### Example - Unassign a user from a group

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnassignUsertoGroup` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ukxucmpl25SNLP65d7",
             "GroupId": "0oakn3j0bfGPR1Esk5d7"
         }
         

If the action is successful, the `UnassignUsertoGroup` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




### Example - Unassign a user from an app

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnassignUsertoApp` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "UserId": "00ukxucmpl25SNLP65d7",
             "AppId": "0oakn3j0bfGPR1Esk5d7"
         }
         
         

If the action is successful, the `UnassignUsertoApp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




### Example - Assign a group to an app

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `Assigngrouptoapp` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
            "GroupId": "00gl5wovm8GuLr8vg5d7",
             "AppId": "0oakn3j0bfGPR1Esk5d7"
         }
         

If the action is successful, the `Assigngrouptoapp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success",
    "Id": "00gl5wovm8GuLr8vg5d7",
    "LastUpdated": "2024-11-21 08:42:53.0",
    "Priority": 0,
    "_links_app_href": "https://dev-99779501.okta.com/api/v1/apps/0oakn3j0bfGPR1Esk5d7",
    "_links_self_href": "https://dev-99779501.okta.com/api/v1/apps/0oakn3j0bfGPR1Esk5d7/groups/00gl5wovm8GuLr8vg5d7", "_links_group_href": "https://dev-99779501.okta.com/api/v1/groups/00gl5wovm8GuLr8vg5d7"
    }
    




### Example - Assign a group to a role

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AssignGrouptoRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "GroupId": "00gl9xqojqXq0TJgS5d7",
         "RoleId": "cr0l5tqddvkDtcfPl5d7",
         "Type": "CUSTOM", "ResourceSet": "iaml81kep6zefR4Oq5d7"
         }
         

If the action is successful, the `AssignGrouptoRole` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success",
    "Id": "irbla1k8uy8XxDDFF5d7",
    "Label": "ReadAdmin_Altostrat",
    "Type": "CUSTOM",
    "Created": "2024-11-20 12:28:33.0",
    "LastUpdated": "2024-11-20 12:28:33.0",
    "AssignmentStatus": "ACTIVE",
    "AssignmentType": "GROUP",
    "resource-set": "iaml81kep6zefR4Oq5d7",
    "role": "cr0l5tqddvkDtcfPl5d7",
    "_links_role_href": "https://dev-99779501-admin.okta.com/api/v1/iam/roles/cr0l5tqddvkDtcfPl5d7",
    "_links_resource-set_href": "https://dev-99779501.okta.com/api/v1/iam/resource-sets/iaml81kep6zefR4Oq5d7", "_links_permissions_href": "https://dev-99779501-admin.okta.com/api/v1/iam/roles/cr0l5tqddvkDtcfPl5d7/permissions", "_links_member_href": "https://dev-99779501.okta.com/api/v1/iam/resource-sets/iaml81kep6zefR4Oq5d7/bindings/cr0l5tqddvkDtcfPl5d7/members/irbla1k8uy8XxDDFF5d7", "_links_assignee_href": "https://dev-99779501.okta.com/api/v1/groups/00gl9xqojqXq0TJgS5d7"
    }
    




### Example - Unassign a group from an app

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnassignGrouptoApp` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
          "GroupId": "00gl5wovm8GuLr8vg5d7",
          "AppId": "0oakn3j0bfGPR1Esk5d7" 
         }
         

If the action is successful, the `UnassignGrouptoApp` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




### Example - Unassign a group from a role

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnassignGrouptoRole` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "GroupId": "00gl5wovm8GuLr8vg5d7",
         "RoleAssignmentId": "irbl94sbyit77SGpg5d7"
         }
         

If the action is successful, the `UnassignGrouptoRole` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




### Example - Suspend a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SuspendUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "UserId": "00ulkdsubxO6W6LgJ5d7" 
         }
         

If the action is successful, the `SuspendUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




### Example - Unsuspend a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UnsuspendUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "UserId": "00ulkdsubxO6W6LgJ5d7" 
         }
         

If the action is successful, the `UnsuspendUser` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
    "Status": "Success"
    }
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all users

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Users from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your requirement.

You must use single quotes (') to enclose the value for a filter clause. You can use the filter clause to filter records based on the columns.




### Example - Get a user

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to "20001" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"20001"` in the **Input Value** field and choose the EntityId as Local variable.

You must pass the entity ID directly, such as "20001". Here, "20001" is the unique primary key value, which is passed

You must use filter clause in queries where passing an Entity Id would thrown an error as there will be two composite keys, such as id='20001'




### Example - Delete a user

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to "00ul7l5fdyTdHDfSj5d7" which is the Key to be passed.To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"20001"` in the **Input Value** field and choose the EntityId as Local variable. 

If Entity has two composite Business or primary Keys instead of specifying the **entityId** , you can also set the **filterClause** to `id='00ul7l5fdyTdHDfSj5d7'`.




### Example - Create a user

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "ProfileFirstName": "Test",
             "ProfileLastName": "Test User",
             "ProfileEmail": "Test@gmail.com",
             "ProfileLogin": "Test11@example.com"
         }
         

If the integration is successful, the `Vendor` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": "00ula502hjbwWYsO25d7"
         }
         




### Example - Create a group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Groups` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
             "ProfileDescription": "Googlecloud group",
             "ProfileName": "Goolecloud created grp\n"
         }
         

If the integration is successful, the `APBill` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": "00gl7lb5gniIAOMwA5d7"
         }
         




### Example - Create an app

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Apps` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Label": "Googlecloud generated app",
             "SignOnMode": "AUTO_LOGIN",
             "AutoSubmitToolbar": false,
             "Settings": "{\"signOn\":{\"redirectUrl\":\"https://www.example.com\",\"loginUrl\":\"https://www.example.com\"}}"
         }
         

This example will create the Vendtype. If the integration is successful, the `Vendtype` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": "0oal9vwooxEXXpdjS5d7"
         }
         




### Example - Create a role

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Roles` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Label": "new role2", 
             "Description": "GABA Role1",
             "Permissions": "\"okta.users.read\", \"okta.groups.read\"" 
         }
         

If the integration is successful, the `Customer` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
             "Id": "cr0l824rbiTvtJDoi5d7"
         }
         




### Example - Update a user

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "ProfileFirstName": "ShubhGillL" 
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Users. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `20044`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "Id": "00ul7u8cyobt8SGRK5d7" 
         }
         




### Example - Update a group

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Groups` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "ProfileName": "Updated Googlecloud group"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Groups. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1371`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "Id": "00gl92veg4VSQQb5A5d7"
         }
         




### Example - Update an app

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Apps` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Label": "Googlecloud updated label"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Apps. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Customerid='10100'\n`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "Id": "0oal9vwooxEXXpdjS5d7"
         }
         




### Example - Update a role

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Roles` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
             "Label": "Googlecloud updated label"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the Roles. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `1`.

Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
             "Id": "cr0l7dqeatRuIrn5x5d7"
         }
         




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
