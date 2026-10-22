---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure/
title: Create and configure a Google Drive connection \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:11.224332+00:00
---

# Create and configure a Google Drive connection  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Create and configure a Google Drive connection

The page describes how to create and configure a Google Drive connection in Integration Connectors. For more information about the Google Drive connector, see [Google Drive connector overview](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview).

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM role to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.




## Create a Google Drive connection

To create a Google Drive connection, do the following:

  1. In the Google Cloud console, go to the **Integration Connectors** > **Connections** page. 

[Go to Connections](https://console.cloud.google.com/connectors/connections)

  2. Click add_box **Create Connection**. 

The **Create Connection** page appears.

  3. In the **Location** section: 
     1. Click **Region** and then select a location for your connection. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, provide the following details: 
     1. **Connector** : select **Google Drive**.
     2. **Connector version** : select the version of the connector that you want to use. 

The connector version you select depends on the Google Drive API version that you want to use. For more information, see [Google Drive connection versions](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview#gsc-connector-versions). 

     3. **Connection Name** : enter a name for the connection. **Important:** The connection name must be unique within the selected region. The connection name must adhere to the following rules: 
        * The name must contain lower-case letters, numbers, or hyphens.
        * The name must begin with a letter and end with a letter or number.
        * The name must not exceed 49 characters.
     4. **Description** : (Optional) enter a description for the connection.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select the service account that you want to use for the connection. Ensure that the service account has the relevant IAM roles and permissions required.
     7. **Supports All Drives** : Select this checkbox to enable access to shared drives. This option is available only for the Google Drive v2.
     8. **Connection node settings** : (Optional) configure the connection node settings.
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. Click **Next**.
  5. In the **Authentication** section, select and configure the authentication type for the connection: 

### Service Account

Select this option if your application runs on a Google Cloud Virtual Machine and should use the VM's attached service account for authentication.

To use this authentication type, you must have a service account with the relevant IAM roles and permissions required for authentication.

For information about creating a service account, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). For information about granting roles to a service account, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Sample connection details for service account authentication type

Field name | Details  
---|---  
Location | us-central1  
Connector | Google Drive  
Connector version | 2  
Connection Name | googledrive-ws-gcpaccount  
Enable Cloud Logging | Yes  
Service Account | 123456789012-compute@developer.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Service Account Authentication  
  
### OAuth 2.0 - JWT Bearer

To configure the Oauth 2.0 JWT Bearer authentication type, do the following:

     1. [Create a service account JSON key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and download the JSON key file. This key file is used as the JWT certificate for the connection.
  6. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create-a-secret) to store the JSON key file or the JWT certificate.
  7. Provide the secret details when you create the connection in Integration Connectors: 
     * **JWT Cert** : choose the secret containing the JWT certificate.
     * **Secret version** : select the secret version for the secret selected.
     * **JWT Subject** : (Optional) enter the JWT subject to use for the connection. This is used as the `sub` field in the JWT token.



#### Sample connection details for OAuth 2.0 - JWT Bearer authentication type

Field name | Details  
---|---  
Location | us-central1  
Connector | Google Drive  
Connector version | 2  
Connection Name | googledrivejwt  
Enable Cloud Logging | Yes  
Service Account | 123456789012-compute@developer.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - JWT Bearer  
JWT Cert | 
    
    
    {
      "type": "service_account",
      "project_id": "sm****-****-******",
      "private_key_id": "0b***************************",
      "private_key": "-----BEGIN PRIVATE KEY-----\nO********************************************=\n-----END PRIVATE KEY-----\n",
      "client_email": "go**********************************8",
      "client_id": "10**********************",
      "auth_uri": "https:***********************",
      "token_uri": "https:************************",
      "auth_provider_x509_cert_url": "https:*********************",
      "client_x509_cert_url": "https:****************************************************",
      "universe_domain": "go********"
    }  
  
Secret version | 2  
  
### Oauth 2.0 Authorization Code

Use this method if your application requires end-user interaction through a browser-based login.

To configure the Oauth 2.0 Authorization Code authentication type, do the following:

  1. [Create OAuth 2.0 credentials](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred) for your web application. This process creates a client ID and the client secret JSON file.
  2. [Identify access scopes](https://developers.google.com/identity/protocols/oauth2/web-server#identify-access-scopes) that you want to grant to your application.
  3. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create-a-secret) to store the OAuth 2.0 credentials (`client_secret.json`).
  4. Provide the client ID, scopes, secret details when you create the connection in Integration Connectors: 
     * **Client ID** : enter the client ID created for your web application.
     * **Scopes** : enter a comma-separated list of desired scopes.
     * **Client Secret** : choose the secret containing the OAuth 2.0 credentials.
     * **Secret version** : select the secret version for the secret selected.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

#### Sample connection details for Oauth 2.0 Authorization Code authentication type

Field name | Details  
---|---  
Location | europe-west1  
Connector | Google Drive  
Connector version | 2  
Connection Name | googledrive-wsconn-code  
Enable Cloud Logging | Yes  
Service Account | 123456789012-compute@developer.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code  
Client ID | CLIENT_ID  
Scopes | https://www.googleapis.com/auth/drive, https://www.googleapis.com/auth/drive.readonly, https://www.googleapis.com/auth/drive.file, https://www.googleapis.com/auth/drive.appdata, https://www.googleapis.com/auth/drive.appfolder, https://www.googleapis.com/auth/drive.install, https://www.googleapis.com/auth/drive.metadata, https://www.googleapis.com/auth/drive.metadata.readonly, https://www.googleapis.com/auth/drive.activity, https://www.googleapis.com/auth/drive.activity.readonly, https://www.googleapis.com/auth/drive.apps.readonly, https://www.googleapis.com/auth/drive.scripts, and https://www.googleapis.com/auth/drive.meet.readonly  
Client Secret | CLIENT_SECRET  
Secret version | 2  
* **Enable authentication override** : (Optional) select this checkbox to enable the connection to accept a different authentication dynamically during runtime.
* Click **Next**.
* In the **Review** section, review your connection and authentication details. You can always click on any of the previous sections to make any changes if required.
* Click **Create**. 

Integration Connectors starts creating the connection for the provided configuration. This process takes a few minutes to complete. After the connection is created, you are redirected to the **Connections** page. 

## Use the Google Drive connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



For the list of supported entities and operations, see [Supported entities and operations](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview#supported_entities_and_operations). For information about the supported connector-specific actions, see [Supported actions](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/overview#supported_actions). 

### Use case examples in Application Integration

The following examples demonstrate how to use the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task) in Application Integration to perform operations using your configured Google Drive connection. 

#### Example - List all the files

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

The value for `filterClause` should be always passed within the single quotes (') in this format.

You can use the `filterClause` for filtering our certain set of records based on any columns.




#### Example - Get a file details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entityId to "1wsHFAusizqFe5O2" which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"1wsHFAusizqFe5O2"` in the **Input Value** field and choose the entityId as Local variable.

The value for `entityId` must be passed directly, such as "1wsHFAusizqFe5O2". Here, "1wsHFAusizqFe5O2" is the unique primary key value, which is passed.




#### Example - Delete a file

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entityId to "1nLrFkDM8nOehXwW8XEpc2UZDBrq_ku-L" which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"1nLrFkDM8nOehXwW8XEpc2UZDBrq_ku-L"` in the **Input Value** field and choose the entityId as Local variable.

If the entity has two composite business or primary keys, instead of specifying the entityId, you can also set the filterClause to id='1nLrFkDM8nOehXwW8XEpc2UZDBrq_ku-L'.




#### Example - Create a file

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload as Local variable.
    
    { "FileData": " ",
      "Name": "creategcpshareddrivedocxfile.docx", 
      "MIMEType": "application/vnd.google-apps.document",
      "Encoding": "BASE64"}
    

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    { "Id": "1C48uLda6lyeakx2hOUdwnib-qtFOAhlpR_Ja2AmPvTU"}
    




#### Example - Create a shared drive

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Drives` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload as Local variable.
    
    {"Name": "SharedDrive7"}
    

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {"Id": "0AN6y5wEvVrmPUk9PVA"}
    




#### Example - Create a permission for a file, folder or shared drive

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Permissions` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload as Local variable.
    
    {"ResourceId": "1PErCmc9MmnYzcslo49DeIIN1-ACs3W4L",
      "Role": "COMMENTER",
      "Type": "USER",
      "EmailAddress": "charlie@altostrat.com"}
    

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    { "PermissionId": "10596783046483894074",
      "ResourceId": "1PErCmc9MmnYzcslo49DeIIN1-ACs3W4L"}
    




#### Example - Update a file details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Files` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload/filterClause as Local variable. 
         
         {"Name": "New Updated file"}
         

  5. Set the entityId of the file. To set the entityId, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload/filterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to 1IY5YhQN-LRgR3IxKlheqXM83sJP3DMFm.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
    
    {"Id": "1IY5YhQN-LRgR3IxKlheqXM83sJP3DMFm">}




#### Example - Update a permission for a file, folder or shared drive

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Permissions` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload/filterClause as Local variable.
    
    (PermissionId='10596783046483894074' and ResourceId='0AKfRSSy6kZbfUk9PVA')
    { "Role": "READER"}
    

  5. Set the entityId of the permission. To set the entityId, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the entityId/connectorInputPayload/filterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `PermissionId='10596783046483894074' and ResourceId='0AKfRSSy6kZbfUk9PVA'`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"PermissionId": "10596783046483894074",
           "ResourceId": "0AKfRSSy6kZbfUk9PVA"}
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
