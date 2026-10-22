---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure/
title: Salesforce \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:41.072222+00:00
---

# Salesforce  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Salesforce

The Salesforce connector lets you perform insert, delete, update, and read operations on Salesforce data.

## Supported versions

The connector requires the Web Services API. The Web Services API is supported natively by Salesforce Enterprise, Unlimited, and Developer editions. The Web Services API may be enabled on Professional Edition at an additional cost by contacting Salesforce. The connector defaults to version 56.0 of the Salesforce API.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the following IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector: 
    * `roles/secretmanager.viewer`
    * `roles/secretmanager.secretAccessor`

If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. 

  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector.




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create connection** page.
  3. In the **Location** section, select a location from the **Region** list and then click **Next**. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

  4. In the **Connection Details** section, complete the following: 
     1. Select **Salesforce** from the connector list.
     2. Select a connector version from the **Connector version** list.
     3. In the **Connection name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. In the **Service account** field, select an account that has the required roles.
     7. (Optional) Configure the **Connection node settings**.
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

     8. (Optional) To configure a proxy server for the connection, select **Use proxy** and enter the proxy details.
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
     9. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to and click **Next**.

In the **Destination Type** field, select the desired type.

     * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
     * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Salesforce connection:

        * OAuth 2.0 - Auth Code
        * OAuth 2.0 - JWT bearer
        * OAuth 2.0 - Client credentials
        * Username and password

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. Review your connection and authentication details, and then click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - Authorization Code**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** : A comma-separated list of desired scopes.
    * **Client secret** : The client secret used for requesting access tokens.
    * **Secret version** : The version of the client secret.
    * **Authorization URL** : The authorization URL generated when creating the client.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your external application, you must re-authorize your Salesforce connection. To understand how to re-authorize, see Re-authorization for Authorization code. 
  * **OAUTH 2.0 - JWT bearer**
    * **Connected App Consumer Key** : The consumer key provided by Salesforce for the connected app you created.
    * **Username** : The username associated with the connected app you created.
    * **Private key** : Secret Manager Secret containing the contents of the private key file. The private key must match the public key/certificate provided to Salesforce.
    * **Secret version** : The version of the private key.

For more information, see [Create Salesforce Connection using JWT](https://www.googlecloudcommunity.com/gc/Integration-Services/Application-Integration-Create-Salesforce-Connection-using-JWT/m-p/511566#M69).

  * **OAuth 2.0 - Client credentials**
    * **Client ID** : The client ID for the app you created.
    * **Client secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Secret version** : The version of the client secret.
  * **Username and password**
    * **Username** : The Salesforce username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the Salesforce username.
    * **Security token** : Secret Manager Secret containing case-sensitive alphanumeric code provided by Salesforce for the user.
    * **Secret version** : The version of the Secret Manager Secret.

**Note:** If you are using OAuth authentication, you must install the connected app in your Salesforce account after creating the connection. For details, see Install the OAuth connected app.

### Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

#### Username and password connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | salesforce  
Connector version | 1  
Connection Name | google-cloud-salesforce-conn  
Enable Cloud Logging | Yes  
Log Level | Error  
Service Account | SERVICEACCOUNT_NAME@developer.gserviceaccount.com  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
Host 1 | https://login.salesforce.com.  
Username | USERNAME  
Password | PASSWORD  
Secret version | 1  
Security Token | zrph####53HCM6D1ZdW####  
Secret version | 1  
  
**Note** : You can pass the following URL as the hostname, which is the default host address: `https://login.salesforce.com`. You must use a different host address if your organization uses a custom login endpoint.

### Re-authorization for Authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in your backend Salesforce application, you must re-authorize your Salesforce connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




### Install the OAuth 2.0 connected app

As part of a security enhancement, Salesforce now requires all connected apps using OAuth 2.0 authentication to be installed. This applies to both new and existing connections. This change means your existing connection might stop working unless the connected app is installed in Salesforce. Navigate to the **Connected Apps OAuth Usage** page in your Salesforce account and install the app. For more information, see [Connected App Usage Restrictions Change](https://help.salesforce.com/s/articleView?id=005132365&type=1).

## Use the Salesforce connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



### Actions

This connector lets you perform insert, delete, update, and read operations on Salesforce data. To execute custom SQL queries, the connector provides the **Execute custom query** action.

To create a custom query, follow these steps: 

  1. Follow the detailed instructions to [ add a connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).
  2. When you [configure the connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-the-connectors-task), in the type of action you want to perform, select **Actions**.
  3. In the **Action** list, select **Execute custom query** , and then click **Done**. 

![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)

  4. Expand the **Task input** section, and then do the following: 
     1. In the **Timeout after** field, enter the number of seconds to wait till the query executes. 

Default value: `180` seconds.

     2. In the **Maximum number of rows** field, enter the maximum number of rows to be returned from the database.

Default value: `25`.

     3. To update the custom query, click **Edit Custom Script**. The **Script editor** dialog opens. 

![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)

     4. In the **Script editor** dialog, enter the SQL query and click **Save**. 

You can use a question mark (?) in a SQL statement to represent a single parameter that must be specified in the query parameters list. For example, the following SQL query selects all rows from the `Employees` table that matches the values specified for the `LastName` column: 
            
            SELECT * FROM Employees where LastName=?

**Note:** Data manipulation language (DML) and data definition language (DDL) statements are supported.
     5. If you've used question marks in your SQL query, you must add the parameter by clicking **\+ Add Parameter Name** for each question mark. While executing the integration, these parameters replace the question marks (?) in the SQL query sequentially. For example, if you have added three question marks (?), then you must add three parameters in order of sequence. 

![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)

To add query parameters, do the following:

        1. From the **Type** list, select the data type of the parameter.
        2. In the **Value** field, enter the value of the parameter.
        3. To add multiple parameters, click **\+ Add Query Parameter**.

The **Execute custom query** action does not support array variables.




The Salesforce connector doesn't support parameterized values for the OFFSET clause, and it can't be dynamically replaced using query parameters. However, query parameters are supported in the WHERE clause.

This section lists the actions supported by the Salesforce connector. To understand how to configure the actions, see Action examples.

#### CreateJobv2 action

Use this action to create a Job.

#### Input parameters of the CreateJobV2 action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ObjectName | String | Yes | The name of the object to be used for the job, such as Account, Campaign, Event, etc.  
Query | String | No | The query to be performed.  
Action | String | Yes | Type of action to use in the job. Valid values are 'insert', 'delete', 'update', 'upsert' or 'query'.  
ExternalIdColumn | String | No | The external ID field in the object being updated. This is required for upsert operations. The field values must also exist in CSV job data.  
ColumnDelimiter | String | No | The column delimiter used for CSV job data. The default value is COMMA. Valid values are 'BACKQUOTE','CARET','COMMA', 'PIPE', 'SEMICOLON', and 'TAB'.  
LineEnding | String | No | The line ending used for CSV job data, marking the end of a data row. The default is LF. Valid values are 'LF' and 'CRLF'.  
MultiPartRequest | Boolean | No | Enable this feature only if the data in the CSV file does not exceed 20,000 characters. You must also specify the path of your CSV file.  
CSVFilePath | String | No | Specifies the path of your CSV File.  
  
For example on how to configure the `CreateJobV2` action, see Examples.

#### UploadJobDataV2 action

Use this action to upload a Job file in CSV format to Salesforce.

#### Input parameters of the UploadJobDataV2 action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ContentUrl | String | No | The URL to use for 'Upload Job Data' requests for this job. Only valid if the job is in Open state.  
CSVFilePath | String | No | Specify the path of your CSV File.  
Content | String | Yes | The CSV file content as an InputStream. To be provided only if CSVFilePath is empty.  
  
For example on how to configure the `UploadJobDataV2` action, see Examples.

#### CreateBatch action

This action creates a Salesforce batch.

#### Input parameters of the CreateBatch action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | Id of the job the batch is being added to.  
Aggregate | String | True | The aggregate of objects being added. Specifies the query to use if performing a batch query.  
ContentType | String | True | The content type for the job. Following are the valid values: CSV, XML, ZIP_CSV, and ZIP_XML. Set the value to CSV if you perform a batch query. The default value is XML.  
  
#### Output parameters of the CreateBatch action

For example on how to configure the `CreateBatch` action, see Examples.

#### CreateJob action

This action adds a Salesforce object entry.

#### Input parameters of the CreateJob action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ObjectName | String | True | Name of the object to be used for the job  
Action | String | True | Type of action to use in the job.  
  
#### Output parameters of the CreateJob action

For example on how to configure the `CreateJob` action, see Examples.

####  GetBatch action

This action gets information about a Salesforce batch.

#### Input parameters of the GetBatch action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | Id of the job the batch is associated with.  
BatchId | String | True | Id of the batch being retrieved.  
  
#### Output parameters of the GetBatch action

For example on how to configure the `GetBatch` action, see Examples.

#### GetJob action

This action gets information about a Salesforce job.

#### Input parameters of the GetJob action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | Id of the job being retrieved.  
  
#### Output parameters of the GetJob action

For example on how to configure the `GetJob` action, see Examples.

#### UploadAttachment action

This action uploads an attachment and associates it with an entity in Salesforce.

#### Input parameters of the UploadAttachment action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
ObjectId | String | True | The Id of the object to associate the uploaded document with.  
FileName | String | True | The name for the attachment.  
Base64Data | String | True | The string of data to be used as content for the file.  
  
To upload Salesforce files to Google Cloud Storage use binary streaming.

For example on how to configure the `UploadAttachment` action, see Examples.

#### GetBatchResults action

This action gets the results of a Salesforce batch.

#### Input parameters of the GetBatchResults action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
JobId | String | True | Id of the job the batch is associated with.  
BatchId | String | True | Id of the batch being retrieved.  
ContentType | String | True | The content type for the job.  
  
#### Output parameters of the GetBatchResults action

For example on how to configure the `GetBatchResults` action, see Examples.

#### DownloadContentDocument action

This action downloads document from Salesforce.

#### Input parameters of the DownloadContentDocument action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
Id | String | True | The ID of the document to download.  
Title | String | False | The title of the document to download.  
LocalPath | String | True | The local path to save the downloaded file. If not provided, the file content is returned in memory.  
Encoding | String | False | The encoding of the downloaded file. The valid values are `NONE` and `BASE64`. Default value is `BASE64`.  
FileStream | String | False | The Output stream used when `LocalPath` is not provided. It enables in-memory or streaming use cases.  
  
#### Output parameters of the DownloadContentDocument action

Parameter Name | Data Type | Description  
---|---|---  
FileId | String | The ID of the downloaded file.  
Success | String | This parameter indicates whether the download was successful.  
FileName | String | The name of the downloaded file.  
FullPath | String | The full path of the downloaded file.  
FileData | String | The file data of the downloaded file.  
FailureMessage | String | The failure message for the failed downloaded file.  
  
The Salesforce connector does not enforce a maximum file download size. For `JSON` or `Base64` payloads, keep files under 40 MB to avoid payload expansion, memory limits, or timeouts.

For example on how to configure the `DownloadContentDocument` action, see Examples.

### Action examples

#### Example - CreateJobV2

This example creates a Job.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateJobV2` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then you must enter a value similar to the following in the `Default Value` field: 
         
         {
           "ObjectName": "Contact",
           "Action": "insert"
          }

If the action is successful, the `CREATEJOBV2` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "ID": "750dM000005HjdnQAC",
      "State": "Open",
      "JobType": null,
      "ContentUrl": "services/data/v43.0/jobs/ingest/750dM000005HjdnQAC/batches",
      "ContentType": "CSV",
      "CreatedDate": "2024-08-07T09:16:16.000+0000",
      "CreatedById": "005dM0000061WSFQA2",
      "ConcurrencyMode": "Parallel",
      "SystemModStamp": "2024-08-07T09:16:16.000+0000"
      }] 




#### Example - UploadJobDataV2

This example uploads a Job file to Salesforce.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadJobDataV2` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Content":   "FirstName,LastName,Email,MobilePhone,External_Id__c\\nGinelle,Merioth,gmerioth0@example.com,851-555-8435,4d13cac0-2c11-48e9-891d-49ee9508a6c7\\nDalli,Tumilson,dtumilson1@example.com,881-555-6742,38bcb24b-247f-498b-9502-c98995a1e04b\\nRobbin,Purveys,rpurveys2@example.com,732-555-6909,35d96c7a-3856-4809-8c49-35ddb9fa7dd9\\nLothaire,Ivanchenkov,livanchenkov3@example.com,144-555-1959,75f63f26-6f4a-406f-a9f4-807f4a8a7b51",
           "ContentUrl": "services/data/v43.0/jobs/ingest/750dM000005HjdnQAC/batches"
          }

If the action is successful, the `UploadJobDataV2` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "Uploaded": "true"
      }]




#### Example - CreateBatch

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateBatch` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
         "JobId": "750dL000007EipxQAC",
         "Aggregate": "\n    Walter\n    White\n  \n  \n    Rob\n    Brown\n  \n",
         "ContentType": "XML"
         }

If the action is successful, the `CreateBatch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "ID": "751dL000003ziC5QAI",
      "JobID": "750dL000007EipxQAC",
      "ApexProcessingTime": "0",
      "ApiActiveProcessingTime": "0",
      "CreatedDate": "2024-09-03T04:48:53.000Z",
      "NumberRecordsFailed": "0",
      "NumberRecordsProcessed": "0",
      "State": "Queued",
      "StateMessage": null,
      "SystemModstamp": "2024-09-03T04:48:53.000Z",
      "TotalProcessingTime": "0"
    }]




#### Example - CreateJob

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateJob` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "ObjectName": "Campaign",
           "Action": "insert"
         }

If the action is successful, the `CreateJob` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "ID": "750dL000007GgD7QAK",
      "JobID": "750dL000007GgD7QAK",
      "ObjectName": "Campaign",
      "Operation": "insert",
      "ApiVersion": "56.0",
      "ApexProcessingTime": "0",
      "ApiActiveProcessingTime": "0",
      "AssignmentRuleId": null,
      "ConcurrencyMode": "Parallel",
      "ContentType": "XML",
      "CreatedById": "005dL000007CalFQAS",
      "CreatedDate": "2024-09-03T05:31:41.000Z",
      "ExternalIdFieldName": null,
      "NumberBatchesCompleted": "0",
      "NumberBatchesQueued": "0",
      "NumberBatchesFailed": "0",
      "NumberBatchesInProgress": "0",
      "NumberBatchesTotal": "0",
      "NumberRecordsFailed": "0",
      "NumberRecordsProcessed": "0",
      "NumberRetries": "0",
      "State": "Open",
      "SystemModStamp": "2024-09-03T05:31:41.000Z",
      "TotalProcessingTime": "0"
    }]




#### Example - GetBatch

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetBatch` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "BatchId": "751dL000003yKlJQAU",
           "JobId": "750dL000007EipxQAC"
         }

If the action is successful, the `GetBatch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "ID": "751dL000003yKlJQAU",
      "JobID": "750dL000007EipxQAC",
      "ApexProcessingTime": "0",
      "ApiActiveProcessingTime": "0",
      "CreatedDate": "2024-09-02T11:44:15.000Z",
      "NumberRecordsFailed": "0",
      "NumberRecordsProcessed": "0",
      "State": "Failed",
      "StateMessage": "InvalidBatch : Failed to parse XML. Unexpected XML element 'sObject' found at  START_TAG seen ... @1:9 it should be 'sObjects'",
      "SystemModstamp": "2024-09-02T11:44:15.000Z",
      "TotalProcessingTime": "0"
    }]




#### Example - GetJob

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetJob ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "JobId": "750dL000007EipxQAC"
         } 

If the action is successful, the `GetJob` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "ID": "750dL000007EipxQAC",
      "JobID": "750dL000007EipxQAC",
      "ObjectName": "Campaign",
      "Operation": "insert",
      "ApiVersion": "56.0",
      "ApexProcessingTime": "0",
      "ApiActiveProcessingTime": "0",
      "AssignmentRuleId": null,
      "ConcurrencyMode": "Parallel",
      "ContentType": "XML",
      "CreatedById": "005dL000007CalFQAS",
      "CreatedDate": "2024-09-02T11:17:42.000Z",
      "ExternalIdFieldName": null,
      "NumberBatchesCompleted": "0",
      "NumberBatchesQueued": "0",
      "NumberBatchesFailed": "2",
      "NumberBatchesInProgress": "0",
      "NumberBatchesTotal": "2",
      "NumberRecordsFailed": "0",
      "NumberRecordsProcessed": "0",
      "NumberRetries": "0",
      "State": "Open",
      "SystemModStamp": "2024-09-02T11:17:42.000Z",
      "TotalProcessingTime": "0"
    }]




#### Example - UploadAttachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadAttachment` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "ObjectId": "001dL00000SC6j7QAD",
           "FileName": "My files/salesforce/con.csv",
           "Base64Data": "Y29ubmVjdG9ycyBpcyBiYWNr"
         }

If the action is successful, the `UploadAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "Id": "00PdL000000EJUDUA4"
    }]




#### Example - GetBatchResults

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetBatchResults` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "BatchId": "751dL000004D17FQAS",
           "JobId": "750dL000007XKUhQAO",
           "ContentType": "XML"
         }

If the action is successful, the `GetBatchResults` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "ID": null,
      "Created": "false",
      "Success": "false",
      "Errors_Fields": "LastName",
      "Errors_Message": "Account: bad field names on insert/update call: FirstName, LastName",
      "Errors_StatusCode": "INVALID_FIELD_FOR_INSERT_UPDATE"
    }, {
      "ID": null,
      "Created": "false",
      "Success": "false",
      "Errors_Fields": "LastName",
      "Errors_Message": "Account: bad field names on insert/update call: FirstName, LastName",
      "Errors_StatusCode": "INVALID_FIELD_FOR_INSERT_UPDATE"
    }]




#### Example - DownloadContentDocument

This example downloads a document from Salesforce using the document ID.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadContentDocument` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Id": "069dM00000ABC123QAC",
           "LocalPath": "/tmp/salesforce_docs"
         }

If the action is successful, the `DownloadContentDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "FileId": "069dM00000ABC123QAC",
      "Success": "true",
      "FileName": "Contract.pdf",
      "FullPath": "/tmp/salesforce_docs/Contract.pdf"
    }]




#### Example - DownloadContentDocument (in-memory)

This example downloads a document from Salesforce and stores it in memory.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadContentDocument` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {"Title": "Invoice_Q4_2024" }

If the action is successful, the `DownloadContentDocument` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{"FileId": "069dM00000XYZ789QAC",
      "Success": "true",
      "FileName": "Invoice_Q4_2024.pdf",
      "FileData": "JVBERi0xLjQKJ..."
    }]




### Entity operation examples

This section shows how to perform some of the entity operations in this connector.

#### Example - Create an attachment

Entity create attachment only creates an attachment with no content file in it. In order to add a file we need to perform Upload Attachment action by giving a file context in the input.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Attachment from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "New Attachment",
           "Description": "New created attachment",
           "ParentId": "001dL00000SC6j7QAD",
           "Body": "Body"
         }
         

  5. Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "00PdL000000EJKXUA4"
         }
         




#### Example - Update an attachment

Entity update attachment only updates the attachment name or description. In order to add a file we need to perform Upload Attachment action by giving a file context in the input.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select Attachment from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. Set the entity ID to Update an Attachment. To set the entity ID, in the **Data mapper** section of the **Tasks** , click **EntityID** and then enter `00PdL000000EJKXUA4` in the given field. 
  5. In the **Data mapper** section of the **Task** click `OpenDataMapping` editor and then enter a value similar to the following in the `field:`
         
         {
           "Name": "New Attachment",
           "Description": "New updated attachment",
           "Body": "Body"
         }
         

Alternately, instead of specifying the **entityId** , you can also set the **filterClause** to `00PdL000000EJKXUA4`.

  6. Running this example, returns a response similar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "00PdL000000EJKXUA4"
         } 
         




## System limitations

The Salesforce connector can process a maximum of 28 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

The Salesforce connector doesn't support the `Upsert` entity operation.

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

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
