---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure/
title: SharePoint \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:13.649566+00:00
---

# SharePoint  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SharePoint

The SharePoint connector lets you manage files, folders, and attachments in SharePoint.

## Supported versions

This connector supports Windows SharePoint Services 3.0, Microsoft Office SharePoint Server 2007 and above, and SharePoint Online.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector: 
  * Enable `secretmanager.googleapis.com` (Secret Manager API) and `connectors.googleapis.com` (Connectors API). For more information, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). 



## Create a SharePoint connection

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create connection** page.
  3. In the **Location** section, select a location from the **Region** list and then click **Next**. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

  4. In the **Connection details** section, complete the following: 
     1. Select **SharePoint** from the connector list.
     2. Select a connector version from the **Connector version** list. The SharePoint connector has two versions: V1 and V2.
     3. In the **Connection name** field, enter a name for the connection instance. The connection name can contain lowercase letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. In the **Service account** field, select an account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
     9. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to and click **Next**.

In the **Destination type** field, select a destination type. For example, host address is ` https://<SITE_NAME>.sharepoint.com`.

     * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
     * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+Add destination**.

  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The SharePoint connection supports the following authentication types:

        * **Windows credentials**. Select this if you use on-premise edition of SharePoint.
        * **AzureAD**. Select this if you use online edition of SharePoint.
        * **OAuth 2.0 client credentials with JWT bearer**. Select this if you use OAuth 2.0 client credentials with JWT bearer for authentication.
        * **OAuth 2.0 client credentials with client secret**. Select this if you use OAuth 2.0 client credentials with client secret for authentication.

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. In the **Review** section, review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

The SharePoint connector supports the following authentication types:

#### Windows credentials authentication type

To enable Windows credentials authentication type, you must complete the following steps:

  1. Configure PSC and create an endpoint attachment.
  2. Specify the credentials in Google Cloud.



**Configure PSC and create an endpoint attachment**

  1. Create an [instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) with the IP where SharePoint is hosted.
  2. Create an [internal passthrough network load balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal) and use the instance group that you created as the backend. The TCP internal load balancer must have the global access enabled.
  3. Publish the load balancer in Private Service Connect. After you publish the load balancer, Private Service Connect generates a service attachment.
  4. [Publish the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service) and specify the load balancer that you created.
  5. Use the service attachment to [create an endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment).
  6. After you create the endpoint attachment, create a SharePoint connection with the endpoint attachment IP.

For more information about creating an endpoint attachment, see [Create an endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment).




**Specify the Windows credentials details in Google Cloud**

When you create the connection in Integration Connectors , you must specify the following details:

In the **Authentication** section, select **Windows credentials** as the authentication type and then enter the following details:

  * **Username** : Enter the username.
  * **Password** : Select the password.
  * **Secret version** : Enter the secret version.



**Windows credentials connection type**

The following table lists the sample configuration values for the Windows credentials connection type.

Field name | Details  
---|---  
Region | us-central1  
Connector | SharePoint  
Connector version | 1  
Connection Name | sharepoint-staging-psc  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
host 1 | http://192.0.2.0  
port 1 | 24  
Authentication | Windows credentials  
Username | USER_NAME  
Password | PASSWORD  
Secret version | 1  
  
#### Azure AD authentication type

To enable Azure AD authentication type, you must complete the following steps:

**Security recommendation:** We recommend a single-tenant configuration with minimum permissions for environments with strict security and compliance requirements.

  1. Register your app and obtain the OAuthClientId and OAuthClientSecret.
  2. Specify the credentials in Google Cloud.
  3. Authorize the connection in Google Cloud.
  4. Add the redirect URL to your app.



**Register your app and obtain the OAuthClientId and OAuthClientSecret**

To register your app and obtain the OAuthClientId and OAuthClientSecret for your app, do the following:

  1. Log in to the [Azure Portal](https://portal.azure.com/).
  2. In **Azure services** , select **App registrations** and then **New registration**.
  3. Enter an application name and select **Accounts in this organizational directory only** (single-tenant). By default, multi-tenant is selected.
  4. Click **Register**.
  5. After creating the app, navigate to the **Certificates & secrets** page.
  6. Create a client secret for the application, and save the client secret value.
  7. Navigate to the **API permissions** page.
  8. Click **Add a permission**.
  9. In the **Request API permissions** dialog, select the API, type, and permissions from the following table to perform operations in the application.

For the connection to be active, you must grant `Sites.Read.All` permission for the **Microsoft Graph** API.

#### Minimum required permissions (Recommended)

For most SharePoint connector operations, grant only the following Microsoft Graph Application permissions:

Permission | Required for  
---|---  
`Sites.Read.All` | Reading SharePoint sites and site metadata  
`Files.Read.All` | Reading documents and files stored in SharePoint  
`User.Read.All` | Resolving user metadata and ownership information  
**Note:** These are the minimum required Microsoft Graph application permissions for most standard SharePoint connector operations. Granting only these permissions follows the principle of least privilege and we recommend this for most use cases. 

#### Optional and advanced permissions

The following permissions are required only if your integration needs advanced operations such as file uploads, updates, or administrative actions.

Grant these permissions only if your use case explicitly requires them.

API | Permissions name | Type | When to use  
---|---|---|---  
Microsoft Graph | `ConsentRequest.Read.All` | `Application/ Delegated` | To view administrative consent requests.  
Microsoft Graph | `ConsentRequest.ReadWrite.All` | `Application/ Delegated` | To manage administrative consent requests.  
Microsoft Graph | `DelegatedAdminRelationship.Read.All` | `Application/ Delegated` | To view delegated admin relationships.  
Microsoft Graph | `DelegatedAdminRelationship.ReadWrite.All` | `Application/ Delegated` | To manage delegated admin relationships.  
Microsoft Graph | `DelegatedPermissionGrant.Read.All` | `Application/ Delegated` | To view delegated permission grants.  
Microsoft Graph | `DelegatedPermissionGrant.ReadWrite.All` | `Application/ Delegated` | To manage delegated permission grants.  
Microsoft Graph | `Files.ReadWrite.All` | `Application/ Delegated` | To upload, edit, or delete files.  
Microsoft Graph | `Sites.FullControl.All` | `Application/ Delegated` | To grant full administrative control over all sites.  
Microsoft Graph | `Sites.Manage.All` | `Application/ Delegated` | To manage lists, libraries, and site settings.  
Microsoft Graph | `Sites.ReadWrite.All` | `Application/ Delegated` | To create, update, or delete site content.  
Microsoft Graph | `Sites.Selected` | `Application/ Delegated` | To limit access to specific site collections only.  
Microsoft Graph | `TermStore.Read.All` | `Application/ Delegated` | To read taxonomies and managed metadata.  
Microsoft Graph | `TermStore.ReadWrite.All` | `Application/ Delegated` | To manage taxonomies and managed metadata.  
Microsoft Graph | `User.Export.All` | `Application/ Delegated` | To export user data for compliance or backup.  
Microsoft Graph | `User.Read` | `Delegated` | To sign in and read the profile of the logged-in user.  
Microsoft Graph | `User.ReadWrite.All` | `Application/ Delegated` | To update user profiles or directory info.  
SharePoint | `EnterpriseResource.Read` | `Delegated` | To read Project Server enterprise resources.  
SharePoint | `EnterpriseResource.Write` | `Delegated` | To manage Project Server enterprise resources.  
SharePoint | `Project.Read` | `Delegated` | To read SharePoint Project data.  
SharePoint | `Project.Write` | `Delegated` | To create or update SharePoint Project data.  
SharePoint | `ProjectWebApp.FullControl` | `Delegated` | To grant full administrative access to Project Web App.  
SharePoint | `ProjectWebAppReporting.Read` | `Delegated` | To read Project Web App reporting data.  
SharePoint | `TaskStatus.Submit` | `Delegated` | To submit project task status updates.  
  10. Save your changes.
  11. If you have selected to use permissions that require admin consent, you can grant them from the current tenant on the **API Permissions** page.
  12. To add the scope, go to the **Expose an API** section and add `AllSites.Manage, Sites.FullControl.All` scopes and select who can control (Admins and users).
  13. Click **Save**.



**Specify the credentials in Google Cloud**

When you create the connection in Integration Connectors , you must specify the following details:

In the **Authentication** section, select **AzureAD** as the authentication type and then enter the following details:

  * **Client ID** : Enter the client ID that is used for requesting access tokens.
  * **Scopes** : Enter a comma-separated list of desired scopes. For example, `Sites.FullControl.All`
  * **Client secret** : Enter the secret that contains the client secret for the connected app that you created.
  * **Secret version** : Secret version for the secret selected above.
  * **Authorization URL** : The authorization URL that you generate when you create an OAuth client. Enter the URL in the following format: `https://login.microsoftonline.com/TENANT_IDENTIFIER/oauth2/v2.0/authorize?prompt=consent`. For example, `https://login.microsoftonline.com/9byyyyyyyyy8112/oauth2/v2.0/authorize?prompt=consent`. 



**Authorize the connection in Google Cloud**

  1. In the [Connections page](https://console.cloud.google.com//connectors/connections), locate the newly created connection. 

The **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application. For more information, see Add the redirect URL to your app.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




**Add the redirect URL to your app**

  1. In the Azure portal, click **Azure services > App registrations**.
  2. Click on your App name.
  3. Click add redirect URI.
  4. Click **Add a platform**.
  5. In the **Web** dialog, paste the redirect URI that you copied when you authorized the connection in Google Cloud.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Azure AD connection type**

The following table lists the sample configuration values for the Azure AD connection type:

Field name | Details  
---|---  
Region | us-central1  
Connector | SharePoint  
Connector version | 1  
Connection Name | sharepoint-google-cloud-con  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50   
Destination Type  | Host address   
host 1  | http://z8**.sharepoint.com   
Authentication  | AzureAD   
Client Id  | CLIENT_ID   
Scopes  | Sites.FullControl.All   
Client secret  | CLIENT_SECRET   
Secret Version  | 1   
Authorization URL  | https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize?prompt=consent   
  
#### OAuth 2.0 - client credentials with JWT bearer authentication type

To enable OAuth 2.0 - client credentials with JWT bearer authentication type, you must complete the following steps:

  1. Create a certificate.
  2. Upload the certificate to Azure portal.
  3. Obtain a private key.
  4. Complete the setup.
  5. Specify the OAuth 2.0 JWT bearer credentials in Google Cloud.



**Create a certificate**

  1. Create an empty folder on your computer.
  2. Create a text file in the folder.
  3. Copy the PowerShell script from the [ Granting access via Azure AD App-Only page ](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread) and paste it into the text file.
  4. Rename the text file to the following name: `Create-SelfSignedCertificate.ps1`.
  5. Run Windows PowerShell in the folder.
  6. Go to the directory which contains the text file.
  7. Copy the following command: ` .\Create-SelfSignedCertificate.ps1 -CommonName "CERTIFICATE_NAME" -StartDate 2022-09-25 -EndDate 2023-10-25`

Enter a unique name for CERTIFICATE_NAME. Change the StartDate to the current date and the EndDate to a date of your choice.

  8. Paste the copied command with your changes to Windows PowerShell and then press Enter. 

Windows PowerShell prompts to Enter the password to protect the Private Key. Make sure to save the password for later use.

Windows PowerShell creates two files: `MyCertificate.pfx` and `MyCertificate.cer`.




**Upload the certificate to Azure portal**

  1. Sign in to Azure Portal and register a new application by specifying the following details: 
     * **Name** : enter a name for the application.
     * **Supported account types** : select **Accounts in this organizational directory only (Account name only - Single tenant)**.
  2. Go to **API Permissions > Add permission > Request API permissions > SharePoint**.
  3. Select **Application permissions** and then add your required permissions.
  4. Select **Grant admin consent** and then select **Yes**.
  5. After creating the app, navigate to the **Certificates & Secrets** section.
  6. Select **Upload Certificate** and then upload your CER certificate from your computer. After the upload finishes, select **Add**. 

Don't add client secrets in the app as it interferes with the certificate-based authentication flow.

  7. Go to Manifest, find KeyCredentials and then copy the customKeyIdentifier as the Thumbprint. You will use this later. You've now registered the app and linked the certificate.



**Obtain a private key**

You can obtain a private key by converting the PFX file to a PEM file using OpenSSL.

  1. From the command prompt, go to the folder with your PFX file and run the following command: `openssl pkcs12 -in MyCertificate.pfx -out MyCertificate.pem -nodes`
  2. Enter the PFX password which you used in the certificate creation process.
  3. Open the PEM file in a text editor and copy the entire text, which is your private key.



**Complete the setup**

  1. Copy the Client ID and Tenant ID from the newly registered app in the Azure portal.
  2. Sign in with SharePoint List Service Principal authentication with the following credentials:
     * Client ID
     * Tenant ID
     * Private key
     * Thumbprint (private key password)



**Specify the OAuth 2.0 JWT bearer credentials in Google Cloud**

When you create the connection in Integration Connectors , you must specify the following details: 

In the **Authentication** section, select **OAuth 2.0 client credentials with JWT bearer** as the authentication type and then enter the following details:

  * In the **Client ID** field, enter the client ID that is used for requesting access tokens. This is the consumer key that Azure generates when you register the app in the Azure portal. 
  * In the **Private key** field, select the Secret Manager secret containing the contents of the private key file in PEM format. The private key should match the public key/certificate provided to Connector. 
  * In the **Secret version** field, select the version for the secret selected above.
  * In the **Private key password** field, select the secret manager secret containing the password (paraphrase) of the private key file. Use the same password that you set to protect the private key when you created the certificate.
  * In the **Secret version** field, select the version for the secret selected above.
  * In the **Azure Tenant** field, enter the Microsoft online tenant being used to access data.
  * For single-tenant Azure AD registration, you must specify the **Azure Tenant ID** in the **Azure Tenant** field of the connection. If this field is missing or incorrect, the connection fails with a `java.sql.SQLException: Invalid connection string syntax.` error. To resolve this error, verify that the **Azure Tenant** field contains the correct Azure Tenant ID for your single-tenant application.



**JWT Bearer Certificate connection type**

The following table lists the sample configuration values for the OAuth 2.0 JWT Bearer Certificate connection type.

Field name | Details  
---|---  
Region | europe-west1  
Connector | SharePoint  
Connector version | 1  
Connection name | sharepoint-jwt-certificate  
Service account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination type | Host address  
host 1 | http://z8**.sharepoint.com  
port 1 | ****  
Authentication | OAuth 2.0-Client credentials with JWT bearer  
OAuth client ID | CLIENT_ID  
Private key | KEY  
Secret version | 1  
Private key password | PASSWORD  
Secret version | 1  
Azure tenant | AZURE_TENANT_ID  
  
#### OAuth 2.0 - client secret connection type

**Warning: Deprecated Authentication Method**

This authentication method requires Azure Access Control Service (ACS) and the `appinv.aspx` page. Microsoft no longer supports this method for new tenants and plans to retire it completely in **April 2026**. For more information, see [Retirement of SharePoint Add-in appregnew and appinv pages](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/retirement-announcement-for-azure-acs).

You should instead configure authentication using one of the following supported methods:

  * Azure AD authentication type
  * OAuth 2.0 – Client credentials with JWT bearer



These methods use Microsoft Graph, and we recommend them as secure authentication mechanisms for SharePoint Online.

To enable the OAuth 2.0 client secret connection type, you must complete the following steps:

  1. [Register the add-in](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure#register-add-in).
  2. [Grant permissions to the add-in](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure#grant-permissions).
  3. [Specify the OAuth 2.0 client credentials in Google Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure#specify-client-secret)
  4. [Re-authorization for authorization code](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure#re-auth)



**Register the add-in**

  1. Navigate to the **Register Add-In** page using the following URL: ` https://<SITE_NAME>.SharePoint.com/_layouts/15/appregnew.aspx`.
  2. In the **App information** section, generate the client ID and client secret.
  3. Specify values for Title, App domain, and redirect URI.
  4. Click **Create**. SharePoint then registers the add-in, and the SharePoint App displays the created information.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Grant permissions to the add-in**

  1. Navigate to the SharePoint site using the following URL: `https://<SITE_NAME>-admin.sharepoint.com/_layouts/15/appinv.aspx`. You are redirected to the **Grant Permission** page.
  2. In the **App ID** field, enter the client ID which you generated earlier, and click **Lookup**. The values for Title, App Domain, and Redirect URL are populated.
  3. Enter the following permission request in XML format: 

For more information about elements of permission request XML, see [AppPermissionRequests element (AppPermissionManifest)](https://learn.microsoft.com/en-us/sharepoint/dev/schema/apppermissionrequests-element-appdefinition-complextypesharepoint-add-in-manifes).
         
         <AppPermissionRequests AllowAppOnlyPolicy="true">
               <AppPermissionRequest Scope="http://sharepoint.com/content/tenant" Right="FullControl"/>
               </AppPermissionRequests>
                 

For more information about permission request scopes, see [Add-in permissions in SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/add-in-permissions-in-sharepoint).

  4. Click **Create**. The Sharepoint App displays a permission consent dialog.
  5. Click **Trust it**.



**Specify the OAuth 2.0 client credentials in Google Cloud**

When you create the connection in Integration Connectors, you must specify the following details:

In the **Authentication** section, select **OAuth 2.0 client credentials with client secret** as the authentication type and then enter the following details:

  * In the **Client ID** field, enter the client ID provided by connector for the app you created. 
  * In the **Client Secret** field, select the Secret Manager secret containing the client secret for the connected app you created. 
  * In the **Secret version** field, select the version of the client secret.



**Re-authorization for authorization code**

If you use the `Authorization code` authentication type and have made any configuration changes in your SharePoint application, you must re-authorize your SharePoint connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




**Client credential connection type**

The following table lists the sample configuration values for the OAuth 2.0 client credentials connection type.

Field name | Details  
---|---  
Region | europe-west1  
Connector | SharePoint  
Connector version  | 1  
Connection name | sharepoint-client-credentials  
Service account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination type | Host address  
host 1 | http://z8**.sharepoint.com  
port 1 | ****  
Authentication | OAuth 2.0-Client credentials with client secret  
Client ID | CLIENT_ID  
Client secret | CLIENT_SECRET  
Secret version | 1  
  
## Use the SharePoint connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

### Actions

This section lists some of the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### Version 1

Actions supported in version 1

AddAttachments, CheckInDocument, CheckOutDocument, CopyDocument, CreateFolder, DeleteAttachment, DiscardCheckOutDocument, DownloadAttachments, DownloadDocument, MoveAttachmentOrDocument, and UploadDocument.

### Version 2

Actions supported in version 2

AddAttachments, AddLists, CheckInDocument, CheckInFile, CheckPermission, CheckOutDocument, CopyDocument, CreateFolder, DeleteAttachment, DeleteDocument, DeleteLists, DiscardCheckOutDocument, DownloadAttachments, DownloadDocument, MoveAttachmentOrDocument, and UploadDocument.

### DeleteAttachment action

This action deletes an attachment.

#### Input parameters of the DeleteAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ListTitle | String | Yes | The title of the list item.  
ItemId | String | Yes | The ID of the list item.  
FileName | String | Yes | The name of the file to delete in the document library.  
  
For an example about how to configure the `DeleteAttachment` action, see Examples.

### AddLists action

This action adds a list in the document library.

#### Input parameters of the AddLists action

Parameter name | Data type | Required | Description  
---|---|---|---  
Template | String | No | The name of the template used.  
Description | String | No | A description of the list.  
Name | String | No | The name of the list to be added in the document library.  
  
For an example about how to configure the `AddLists` action, see Examples.

### DeleteDocument action

This action deletes the document from the library.

#### Input parameters of the DeleteDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
Library | String | Yes | The name of the document library where the file is stored.  
Path | String | Yes | The relative path of the document.  
  
For an example about how to configure the `DeleteDocument` action, see Examples.

### CheckPermission action

This action checks the permissions of a user or group on a list or list item.

#### Input parameters of the CheckPermission action

Parameter name | Data type | Required | Description  
---|---|---|---  
ListName | String | No | The title of the list.  
Principal | String | No | The login name of the user  
ItemId | String | No | The ID of the list item.  
  
For an example about how to configure the `CheckPermission` action, see Examples.

### DeleteLists action

This action deletes a list in the document library.

#### Input parameters of the DeleteLists action

Parameter name | Data type | Required | Description  
---|---|---|---  
Name | String | No | The name of the list to delete in the document library.  
  
For an example about how to configure the `DeleteLists` action, see Examples.

### CheckInFile action

This action checks in the file or document.

#### Input parameters of the CheckInFile action

Parameter name | Data type | Required | Description  
---|---|---|---  
RelativeURL | String | Yes | The relative URL of the folder.  
DocumentName | String | Yes | The name of the file.  
Comment | String | Yes | A comment for check-in.  
  
For an example about how to configure the `CheckInFile` action, see Examples.

### CheckOutDocument action

This action checks out the file or document.

#### Input parameters of the CheckOutDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
RelativeURL | String | Yes | The relative URL of the folder.  
DocumentName | String | Yes | The name of the file.  
  
For an example about how to configure the `CheckOutDocument` action, see Examples.

### CheckInDocument action

This action lets you check in a document.

#### Input parameters of the CheckInDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
RelativeURL | String | Yes | The relative URL of the folder.  
DocumentName | String | Yes | The name of the file.  
Comment | String | No | A comment for check-in.  
  
For an example about how to configure the `CheckInDocument` action, see Examples.

### DiscardCheckOutDocument action

This action lets you undo a file check out.

#### Input parameters of the DiscardCheckOutDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
RelativeURL | String | Yes | The relative URL of the folder.  
DocumentName | String | Yes | The name of the file.  
  
For an example about how to configure the `DiscardCheckOutDocument` action, see Examples.

### CopyDocument action

This action lets you copy a file from one location to another location.

#### Input parameters of the CopyDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
SourceFileRelativeUrl | String | Yes | The relative URL of the source file.  
DestFileRelativeUrl | String | Yes | The relative URL of the destination file.  
  
For an example about how to configure the `CopyDocument` action, see Examples.

### UploadDocument action

This action lets you upload a file.

#### Input parameters of the UploadDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
FileName | String | Yes | Name of the file to be uploaded.  
RelativeUrl | String | Yes | The relative URL of the folder.  
Content | String | No | Content to upload as a file.  
ContentBytes | String | No | Base64-encoded content of the file. Use this to upload binary data.  
HasBytes | Boolean | No | This parameter specifies whether the content to upload is binary. The default value is `false`.  
  
For an example about how to configure the `UploadDocument` action, see Examples.

### DownloadDocument action

This action lets you download a file.

#### Input parameters of the DownloadDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | The URL of the document. It can be either a full URL or a relative URL.  
Library | String | Yes | The name of the library.  
HasBytes | Boolean | No | This parameter specifies whether the content should be downloaded as bytes. The default value is `false`.  
  
For an example about how to configure the `DownloadDocument` action, see Examples.

### MoveAttachmentOrDocument action

This action lets you move a file from one folder to another folder.

#### Input parameters of the MoveAttachmentOrDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
SourceFileURL | String | Yes | The URL of the source file to move.  
DestinationFolderURL | String | Yes | The URL of the destination folder.  
  
For an example about how to configure the `MoveAttachmentOrDocument` action, see Examples.

### CreateFolder action

This action lets you create a folder.

#### Input parameters of the CreateFolder action

Parameter name | Data type | Required | Description  
---|---|---|---  
RelativeURL | String | Yes | The relative URL of the folder.  
FolderName | String | Yes | The name of the folder to create.  
  
For an example about how to configure the `CreateFolder` action, see Examples.

### AddAttachments action

This action lets you add an attachment.

#### Input parameters of the AddAttachments action

Parameter name | Data type | Required | Description  
---|---|---|---  
ListTitle | String | Yes | The name of the attachment list.  
FileName | String | Yes | The name of the attachment file.  
ItemId | String | Yes | The ID of the attachment to add.  
Content | String | Yes | Content of the attachment.  
ContentBytes | String | No |  Base64-encoded content of the file. Use this to upload binary data.   
HasBytes | Boolean | No | This parameter specifies whether the content to upload is binary. The default value is `false`.  
  
For an example about how to configure the `AddAttachments` action, see Examples.

### DownloadAttachments action

This action lets you download attachments.

#### Input parameters of the DownloadAttachments action

Parameter name | Data type | Required | Description  
---|---|---|---  
RemoteFile | String | Yes | The URL of the file.  
HasBytes | Boolean | No | This parameter specifies whether the content to download is binary. The default value is `false`.  
  
For an example about how to configure the `DownloadAttachments` action, see Examples.

### Action examples

This section describes how to perform some of the actions in this connector.

### Example - Delete an attachment

This example deletes the specified file.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ListTitle": "My lists",
         "ItemId": "1",
         "FileName": "sitepages.txt"
         }

If the action is successful, the `DeleteAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Check in a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CheckInFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "RelativeURL": "/Shared Documents/TestFolder",
           "DocumentName": "Document.docx",
           "Comment": "Comment test with more than 1 word"
         }
         

If the action is successful, the `CheckInFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]
    




### Example - Add a list to a library

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddLists` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Template": "DocumentLibrary",
           "Description": "testdata_from_gcpcloud",
           "Name": "TestList1757601118898"
         }
         

If the action is successful, the `AddLists` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]
    




### Example - Delete a document

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Library": "Shared Documents",
           "Path": "/Shared Documents/TestFolder/Document.docx"
         }
         

If the action is successful, the `DeleteDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]
    




### Example - Check permissions on a list

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CheckPermission` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "ListName": "TestList",
           "ItemId": "1",
           "Principal": "ACLSITE1 Owners"
         }
         

If the action is successful, the `CheckPermission` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]
    




### Example - Delete a list

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteLists` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "TestList1757601118898"
         }
         

If the action is successful, the `DeleteLists` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]
    




### Example - Check in a document

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CheckInDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RelativeURL": "/Shared Documents/TestFolder",
         "DocumentName": "Document.txt",
         "Comment": "Comment test"
         }

If the action is successful, the `CheckInDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Check out a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CheckOutDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RelativeURL": "/Shared Documents/TestFolder",
         "DocumentName": "Document.txt"
         }

If the action is successful, the `CheckOutDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Discard a check out

This example reverts a file check out.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DiscardCheckOutDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RelativeURL": "/Shared Documents/TestFolder",
         "DocumentName": "Document.docx"
         }

If the action is successful, the `DiscardCheckOutDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Copy a file to a different location

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CopyDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "SourceFileRelativeUrl": "/Shared Documents/Document.docx",
         "DestFileRelativeUrl": "/Shared Documents/TestFolder/Document123.docx"
         }

If the action is successful, the `CopyDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Upload a text file to a specified location

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileName": "test.txt",
         "RelativeUrl": "/Shared Documents/TestFolder",
         "Content": "abcd"
         }

If the action is successful, the `UploadDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Upload a binary file to a specified location

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "FileName": "test.txt",
         "RelativeUrl": "/Shared Documents/TestFolder",
         "ContentBytes": "SGVsbG8gd29ybGQK",
         "HasBytes": "true"
         }

If the action is successful, the `UploadDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Status": "Success"
    }]




### Example - Download a file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/TestFolder/test.txt",
         "Library": "Shared Documents"
         }

If the action is successful, the `DownloadDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "Content": "Test File",
    }]




### Example - Download a binary file

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/TestFolder/test1.png",
         "Library": "Shared Documents"
         "HasBytes": "true"  
         }

If the action is successful, the `DownloadDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "ContentBytes": "VGVzdCBGaWxl",
    }]

**Note:** The downloaded content will be a Base64 encoded string.


### Example - Download a file from a specific site

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "RemoteFile": "	http://z8**.sharepoint.com/sites/SharepointGCS/Docs/SharpointGCS.docx",
           "Library": "Docs",
           "HasBytes": true
         }
         

If the action is successful, the `DownloadDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [
      {
        "Success": "True",
        "ContentBytes": "UEsDBAoAAAAAAAAAIQD/////TwEAAE8BAAAQAAAAW3RyYXNoXS8wMDAwLmRhdP////nFmjQeC1QbGmk9o7n0xjiLgudAMOrYQBpOZdZp5/OrWkWbudVPccasL5uVSKun3URrHAxow7iMUm2WSi7nlGy2Mr+sjJxQSrYFcFtDQyo/QSutWhbNcAODEWh14mklzxCS9C5CW3Fmwme/gMKGjGoXlSVyvtDoB+u0A6XtA8bkWTnPNHSvxcepoAKIdsR96imCvxe4MxOWqHWnQkLDyjNMOMrrQeMDF7nOMCCvPlVn5Vd6KlDYnHlW1zLOcQf6WmKl2xN4Z8WBXZfkrJZqPv6yNdWyp8ADRmgTdRSqDkPpQqzvqWj3qpdiRZqSwyBRtfr2kHBumkTNjSi6drBMFMxZEgrktw6ZxuEXcx3v16cXd6k5JVO3kOXMg/HFnH"
      }
    ]
    

To download a file from a specific site, you must provide the complete address of the remote file.




### Example - Move an attachment to a different location

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `MoveAttachmentOrDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "SourceFileURL": "/Shared Documents/test.txt",
         "DestinationFolderURL": "/Shared Documents/TestFolder"
         }

If the action is successful, the `MoveAttachmentOrDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Result": "Success"
    }]




### Example - Create a folder in a specific location

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateFolder` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RelativeURL": "/Shared Documents/TestFolder",
         "FolderName": "TestFolder123"
         }

If the action is successful, the `CreateFolder` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Id": "110842b7-2393-4f11-9391-3d75214e9fb8",
    "Status": "Success"
    }]




### Example - Add an attachment to a list

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddAttachments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ListTitle": "My Lists",
         "FileName": "TestAttachment2",
         "Content": "abcd text",
         "ItemId": "1"
         }

If the action is successful, the `AddAttachments` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "RelativeUrl": "/Lists/My lists/Attachments/1/TestAttachment2",
    "Status": "Success"
    }]




### Example - Add a binary attachment to a list

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddAttachments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "ListTitle": "My Lists",
         "FileName": "TestAttachment3",
         "ContentBytes": "VGVzdCBGaWxl",
         "HasBytes": "true",  
         "ItemId": "1"
         }

If the action is successful, the `AddAttachments` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "RelativeUrl": "/Lists/My lists/Attachments/1/TestAttachment3",
    "Status": "Success"
    }]
    




### Example - Download an attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/Shared Documents/Document.txt"
         }

If the action is successful, the `DownloadAttachments` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "Content": "Test File",
    }]




### Example - Download a binary attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "RemoteFile": "/Shared Documents/Document.docx",
         "HasBytes": "true"
         }

If the action is successful, the `DownloadAttachments` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True",
    "ContentBytes": "VGVzdCBGaWxl",
    }]

**Note:** The downloaded content will be a Base64 encoded string.


### Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Version 1

Entities supported in version 1

Files, and My Lists.

### Version 2

Entities supported in version 2

Files, ListItem, My Lists, RoleAssignments, Sharing Links, SitePages, Subsites, and Users.

### Example - List all files

This example lists all the files in the `Files` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). You can also specify multiple filter conditions by using the logic operators.



### Example - List all sharing links of files

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sharing Links` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all sharing links of folders

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sharing Links` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all site pages

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SitePages` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all sub sites

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Subsites` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all my lists

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `My Lists` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all users

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all items

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `ListItem` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - List all the role assignments

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `RoleAssignments` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.



### Example - Get a sharing link of a file

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sharing Links` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the **entityId** to Sharing Links. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1.0` in the **Input Value** field and choose the **entityId** as local variable.



### Example - Get file details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the **entityId** to Files. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `ZETdEU1T_UOBEzbgDmsvcubxvUaXbcJNrrNPM4LqoklbdDZx3Eo0SIWPCsc_L6yI` in the **Input Value** field and choose the **entityId** as local variable.



### Example - Get a sharing link of a folder

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Sharing Links` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the **entityId** to Sharing Links. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `3.0` in the **Input Value** field and choose the **entityId** as local variable.



### Example - Get a list

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `My Lists` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `3` in the **Default Value** field. 

Here, `3` is a primary key value in the `My Lists` entity.




### Example - Create a list

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `My Lists` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "AuthorId": 11.0,
         "BaseName": "3_",
         "Attachments": false,
         "Title": "Created List New"
         }
         

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "ID": 3.0
         }]
         




### Example - Delete a list

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `My Lists` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `2` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).



### Limitations

The following are the limitations of the SharePoint connector: 

  * The update operation for entities `SitePages` and `Events` is not working.
  * The list operation for entities `AllFiles`, `AllPages`, `AllEvents`, `AllLists`, and `Sites` is not working.



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
