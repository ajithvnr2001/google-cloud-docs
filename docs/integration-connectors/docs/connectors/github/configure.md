---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/github/configure/
title: GitHub \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:50.074375+00:00
---

# GitHub  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/github/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GitHub

The GitHub connector lets you perform insert, delete, update, and read operations on GitHub data.

## Before you begin

Before using the GitHub connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

  * In GitHub, based on your requirement, complete the following tasks: 
    * [Create a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
    * [Create new repositories](https://docs.GitHub.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
    * [Create new organizations](https://docs.GitHub.com/en/enterprise-server@3.11/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).
    * [Create projects](https://docs.GitHub.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project).
    * [Create an OAuth app](https://docs.GitHub.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app).
    * [Create a GitHub app](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps).
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

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
       1. **Connector** : Select **GitHub** from the drop down list of available Connectors.
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
       7. Optionally, specify **OwnerLogin** : A unique login name belonging either to a user or an organization.
       8. Optionally, specify **Schema** : Use schema to restrict the dynamically retrieved schemas to a specific project or repository schema. To retrieve all the schemas, don't specify any value in this field. For information about supported schemas, see Schemas and scopes
       9. Optionally, configure the **Connection node settings** : 

          * **Minimum number of nodes** : Enter the minimum number of connection nodes.
          * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
       10. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
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
       11. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
       12. Click **NEXT**.
    5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
       1. **Destination Type** : Select a **Destination Type**. 
          * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
          * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.



If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

* Click **NEXT**.
* In the **Authentication** section, enter the authentication details. 

To understand how to configure these authentication types, see Configure authentication.

* Click **NEXT**.
* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Client ID** : The client ID used for requesting access tokens.
  * **Scopes** : A comma-separated list of desired scopes.
  * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - authorization code connection type

Field name | Details  
---|---  
Location | europe-west1  
Connector | GitHub  
Connector version | 1  
Connection Name | GitHub-connector  
Enable Cloud Logging | No  
Service Account | Your_Project_Number@serviceaccount  
OwnerLogin | souvikg-Your_Owner_Login  
Schema |   
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Client ID | ClientID  
Scopes | repo repo:status repo_deployment  
Client Secret | Client secret  
Secret Version | 1  
  
### GitHub schemas and scopes

The GitHub connector supports the following schemas: 

  * Information schema: This schema contains tables that contain licensing information and high-level overviews of the projects and repositories associated with the authenticated account. Only one information schema exists. To retrieve the information schema, specify the following in the schema field: Information
  * Repository schema: The connector supports schema for each repository in the authenticated user or organization's account. Use the following format to specify a repository schema: Repository_.
  * Project schema: The connector supports schema for each project in the authenticated user or organization's account. Use the following format to specify a project schema: Project_



For more information about scopes, see [GitHub Scopes](https://docs.GitHub.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps). 

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

The GitHub connector can process 2 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Action

This section lists the action supported by the GitHub connector. To understand how to configure the action, see Action examples.

### UpdatePullRequestBranch action

This action updates the pull request branch.

#### Input parameters of the UpdatePullRequestBranch action

Name | Type | Description  
---|---|---  
PullRequestId | string | The Node ID of the pull request.  
ExpectedHeadOid | string | The head ref oid for the upstream branch.  
UpdateMethod | string | The update branch method to use. The default is 'MERGE'. The allowed values are MERGE and REBASE.  
  
#### Output parameters of the AppsDeployStatus action

This action returns the status 200 (OK) and updates pull request branch.

For example on how to configure the `UpdatePullRequestBranch` action, see Examples.

### MergePullRequest action

This action merges pull request.

#### Input parameters of the MergePullRequest action

Name | Type | Description  
---|---|---  
PullRequestId | string | The Node ID of the pull request to be merged.  
ExpectedHeadOid | string | OID that the pull request head ref must match to allow merge; if omitted, no check is performed.  
CommitHeadline | string | Commit headline to use for the merge commit; if omitted, a default message is used.  
CommitBody | string | Commit body to use for the merge commit; if omitted, a default message is used.  
MergeMethod | string | The merge method to use. The default is 'MERGE'. The allowed values are MERGE, SQUASH, and REBASE.  
AuthorEmail | string | The email address to associate with this merge.  
  
#### Output parameters of the MergePullRequest action

This action returns the status 200 (OK) and merges pull request.

For example on how to configure the `MergePullRequest` action, see Examples.

### DownloadFile action

This action downloads a file from the repository.

#### Input parameters of the DownloadFile action

Name | Type | Required | Description  
---|---|---|---  
Path | String | False | The path of the file in the repository.  
Branch | String | False | The branch name in the repository from which the file is downloaded. The default value is main branch.  
LocalPath | String | False | The local path where the file is saved after download.  
OutputStream | Binary | True | An instance of an output stream to which the file data is written. The output stream is used only if the LocalPath is not provided.  
  
For example on how to configure the `DownloadFile` action, see Examples.

### UploadFile action

This action uploads a file to the repository.

#### Input parameters of the UploadFile action

Name | Type | Required | Description  
---|---|---|---  
Path | String | False | The path of the file in the repository.  
Branch | String | False | The branch name in the repository to upload the file. The default value is main branch.  
CommitMessage | String | False | The message that describes the changes made during the file upload.  
SHA | String | False | The hash of the file that is used to verify and update existing files in the repository.  
CommitterName | String | False | The user who commits the file. The default value is the authenticated user.  
CommitterEmail | String | False | The email address of the user who commits the file. The default value is the authenticated user.  
AuthorName | String | False | The name of the author who uploads the file. The default value is the committer's name or the authenticated user.  
AuthorEmail | String | False | The email address of the author who uploads file. The default value is the committer's email or the authenticated user's email.  
LocalPath | String | False | The local path where the file is saved after download.  
InputStream | Binary | True | An input stream instance used to read the file data. This is used only if LocalPath is not specified.  
FileData | String | False | The Base64-encoded string representing the file's content. This is used only if LocalPath and InputStream are not specified.  
  
For example on how to configure the `UploadFile` action, see Examples.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - UpdatePullRequestBranch

This example retrieves the deployment statuses of the application.

  1. In the `Configure connector task` dialog, click `Action`.
  2. Select the `UpdatePullRequestBranch` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "PullRequestId": "PR_kwDOLywhW8537gcA"
               } 
           

If the action is successful, the `UpdatePullRequestBranch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
        "pullrequestid": "PR_kwDOLywhW8537gcA"
           } 
      




### Example - MergePullRequest

This example merges a pull request.

  1. In the `Configure connector task` dialog, click `Action`.
  2. Select the `MergePullRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "PullRequestId": "PR_kwDOLywhW8537gcA",
             "CommitHeadline": "Google MERGE",
             "CommitBody": "This is Google Merge"
               }
           

If the action is successful, the `MergePullRequest` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
        "pullrequestid": "PR_kwDOLywhW8537gcA"
            } 
      




### Example - Download a file from the repository

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Repository": "Google_GitHub_Testing",
             "Path": "Test_Document.txt"
               }
           

If the action is successful, the `DownloadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
          "Success": true,
          "Details": null,
          "FileData": "SGkgR29vZ2xlIEhvdyBSIHlvdT8KCkknbSBmaW5l"
        }
      




### Example - Upload a file to the repository

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UploadFile` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
             "Path": "Sample.txt",
             "Repository": "Google_GitHub_Testing",
             "AuthorName": "Cruz",
             "FileData": "dXBsb2FkIGR0YWEgaW50byB0aGlzIGZpbGUgZnJvbSBHQ1A=",
             "CommitMessage": "TestCommitFrom GCPcloud",
             "CommitterEmail": "Charlie@altrostrat.com",
             "CommitterName": "Charlie",
             "AuthorEmail": "cruz@altrostrat.com"
               }
           

If the action is successful, the `UploadFile` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
          "Success": false,
          "Details": "Invalid request.\n\n\"sha\" wasn't supplied. ",
          "CommitSHA": null,
          "FileSHA": null
        }
      




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all Branches

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Branches` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your requirement.



### Example - List all Commits

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Commits` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your requirement.



#### Considerations

  * Commits is the name of the entity. You must pass the value for filter clause using single quotes ('), such as City='Redwood City'. Where City is the column name and Redwood city is the value.
  * You can make use of the filter clause to filter records based on columns. For example, if there are 20 records with `name = demo16975280986860` then we can filter records with column Address='Redwood City' and region='us-east1'.



You can perform the List operation on the following entities:

CommitComments, Forks, IssueComments, Issue, IssueAssignees, AssignableUser,Labels, Milestones, PullRequestReviews, PullRequests, PullRequestComments, ReleaseAssets, Releases, Watcher, Users, Repositories, Collaborators, OrganizationTeams, OrganizationsMannequins, OrganizationMember, Organization, Licenses, LicensePermission, LicenseLimitation, LicenseConditions, Projects, and PullRequestReviewRequests

### Example - Get a Branches record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Branches` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Here, the entity ID is set to 4. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `4` in the **Default Value** field.



### Example - Get a Repositories record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Repositories` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to 4 which is the Key to be passed. To set the entity ID, in the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `4` in the **Default Value** field.

In some cases passing a single Entity ID can cause an error because of two composite keys. In such cases, use the filter clause with the necessary columns.

For views, the Get operation doesn't work because views don't have primary keys. Instead, you can use the List operation with filters on views, which functions similarly to the Get operation.




You can perform the Get operation on the following entities:

CommitComments, Commits, IssueAssignees, Labels, Milestones, PullRequestReviews, PullRequests, PullRequestComments, ReleaseAssets, Release, Topics, Users, Collaborators, Organizations, and Licenses

### Example - Create an Issues record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Issues` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Title": "Google_Cloud_GitHub_Issues_Create",
           "Body": "Please check hence raising the Feature Request for the same."
              }
         

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "I_kwDOLywhW86Sd-xF"
              } 
         




### Example - Create a PullRequests record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PullRequests` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "BaseRefName": "main",
           "HeadRefName": "New_Branch",
           "Title": "DEMO_Google_Cloud_PULLRequest",
           "Body": "This is demo Google_Cloud pull"
              }
         

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "PR_kwDOLywhW8537gcA"
               }
         




### Example - Create a Repositories record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Repositories` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "Google_Cloud_DEMO_REPO",
           "OwnerId": "O_kgDOCaxLsg",
           "Visibility": "PUBLIC"
              }
         

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "R_kgDOMhWBEQ"
               } 
         




### Example - Update an Issues record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Issues` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Title": "New_Updated_Google_Cloud_Issue",
           "Body": "Newly Updated from Google_Cloud"
              }
         

  5. Set the value for entityId to I_kwDOLywhW86Sd-xF. To set the value for filterClause, click **entityId** and then enter `I_kwDOLywhW86Sd-xF` in the **Default Value** field. 

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "I_kwDOLywhW86Sd-xF"
              }
         




### Example - Update a PullRequests record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PullRequests` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Title": "Updated_Google_Cloud_PULL",
           "Body": "Update New pull Body"
               }
         

  5. Set the value for entityId to PR_kwDOLywhW8537gcA. To set the value for filterClause, click **entityId** and then enter `PR_kwDOLywhW8537gcA` in the **Default Value** field. 

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "PR_kwDOLywhW8537gcA"
               } 
         




### Example - Update a Repositories record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Repositories` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Name": "Updated_New_Google_Cloud_Repo"
               }
         

  5. Set the value for entityId to R_kgDOMhWBEQ. To set the value for filterClause, click **entityId** and then enter `R_kgDOMhWBEQ` in the **Default Value** field. 

Running this example, returns a response smiliar to the following in the Connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "R_kgDOMhWBEQ"
               }
         




### Example - Delete a PullRequestReviewRequests record

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PullRequestReviewRequests` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the value for filterClause, click **filterClause** and then enter `PullRequestId= 'PR_kwDOLywhW85yNWPa' and RequestedReviewerUserId= 'U_kgDOCebPLA'` in the **Default Value** field.

In this example, PullRequestReviewRequests is name of the table and the value for filterClause should be passed directly.   
Such as, PullRequestId= 'PR_kwDOLywhW85yNWPa' and RequestedReviewerUserId= 'U_kgDOCebPLA'.   
Here, PullRequestId= 'PR_kwDOLywhW85yNWPa' and RequestedReviewerUserId= 'U_kgDOCebPLA' are the unique primary key values that should be passed.




## Connector Versions

We usually create a new version when there is a breaking change.

Current Status: The connector now has two versions (v1 and v2).

### Below are the major changes between v1 and v2 versions:

  1. Removed DatabaseId column from ProjectViews, Projects, OrganizationTeamProjects, and ItemsView across all schemas.
  2. Moved the MergePullRequest stored procedure from the Repository schema to the Information schema.



## Use the GitHub connection in an integration

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
