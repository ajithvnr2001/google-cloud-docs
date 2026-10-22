---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredevops/configure/
title: Azure DevOps \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:19.074138+00:00
---

# Azure DevOps  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredevops/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Azure DevOps

The Azure DevOps connector lets you perform insert, delete, update, and read operations on Azure DevOps data.

## Supported versions

This connector supports the following Azure DevOps versions.

  * Azure DevOps 2022, 2020, 2019
  * Team Foundation Server 2018



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
     1. **Connector** : Select **Azure DevOps** from the drop down list of available Connectors.
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
     8. **Azure Tenant** : Provide the name or ID of the Azure DevOps tenant.
     9. **Organization** : Provide the name of the organization or collection that uses the Azure DevOps.
     10. **Schema** : Enter the schema, such as information, project.
     11. **Catalog** : Enter the name of the catalog.
     12. **Apply Transformation** : Enter a comma-separated list of transformations.
     13. **Azure DevOps Edition** : Enter the edition of Azure DevOps.
     14. **Azure DevOps Service API** : Enter the Rest API version of Azure DevOps.
     15. **URL** : Provide the URL of the Azure DevOps instance.
     16. **Include Custom Fields** : Select this option to include custom fields in the column listing.
     17. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     18. Click **NEXT**.
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

The following authentication types are supported by the Azure DevOps connection:

     * AzureAD
     * Basic

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **AzureAD**
    * **ClientID** : Enter the client ID for the app you created.
    * **Scopes** : Specify all the scopes separated by comma, such as read, write.
    * **Client Secret** : Enter the secret manager secret containing the client secret for the connected app you created.
    * **Secret Version** : Select the secret version for the secret selected above.
    * **Authorization URL** : Provide the authorization URL of the client.


  * **Basic**
    * **Personal Access Token** : Enter the generated personal access token.
    * **Secret Version** : Select the secret version for the secret entered.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

In Azure DevOps, various data schemas are used to organize and manage different aspects of a project. Each schema focuses on a specific type of data to structure information effectively based on the project needs.

  * Project data model: A schema that defines how project related data, such as items, repositories, pipelines, and teams are organized, linked, and managed within Azure DevOps.
  * Information data model: A schema that defines how documentation, metadata, and communication artifacts are structured, stored, and accessed across Azure DevOps projects.
  * Repository data model: A schema that defines how code repositories, branches, commits, pull requests, and related metadata are organized and managed within Azure DevOps.
  * Analytics data model: A schema that captures and organizes historical and real time data from Azure DevOps for reporting, dashboards, and advanced analytics.
  * All data models: A single connection that provides access to all data models in a single connection.

Field name | Information model | Project model | Repository model | Analytics model | All models | AzureAD connection  
---|---|---|---|---|---|---  
Location| europe-west1| europe-west1| europe-west1| europe-west1| asia-east1| europe-west1  
Connector| Azure DevOps| Azure DevOps| Azure DevOps| Azure DevOps| Azure DevOps| Azure DevOps  
Connector version| 1| 1| 1| 1| 1| 1  
Connection Name| azuredevops-informationmodel| azuredevops-projectmodel| azuredevops-repositorymodel| azuredevops-analyticsmodel| devops| azuredevops-oauth  
Enable Cloud Logging| Yes| Yes| Yes| Yes| Yes| Yes  
Log Level| Debug| Debug| Debug| Debug| Debug| Debug  
Service Account| Your_Project_Number@serviceaccount| Your_Project_Number@serviceaccount| Your_Project_Number@serviceaccount| Your_Project_Number@serviceaccount| Your_Project_Number@serviceaccount| Your_Project_Number@serviceaccount  
Azure Tenant| Tenant_Id| Tenant_Id| Tenant_Id| Tenant_Id| Tenant_Id| Tenant_Id  
Organization| Organization_Name| Organization_Name| Organization_Name| Organization_Name| Organization_Name| Organization_Name  
Schema| Information| Project| Repository__RepositoryId| Analytics| | Project  
Catalog| Devops| Project_ProjectId| Project_ProjectId| Project_ProjectId| | Project_ProjectId  
Azure Dev Ops Edition| AzureDevOps Online| AzureDevOps Online| AzureDevOps Online| AzureDevOps Online| AzureDevOps Online| AzureDevOps Online  
Azure Dev Ops Service API| 6.0| 6.0| 6.0| 6.0| 6.0| 6.0  
Include Custom Fields| Yes| Yes| Yes| Yes| Yes| Yes  
CustomizedDefaultCatalogName| CustomizedDefaultCatalogName=Google| | | | CustomizedDefaultCatalogName=Google|   
Minimum number of nodes| 2| 2| 2| 2| 2| 2  
Maximum number of nodes| 50| 50| 50| 50| 50| 50  
Authentication| Yes| Yes| Yes| Yes| Yes| Yes  
Basic| Yes| Yes| Yes| Yes| Yes|   
API Token| Api Token provided by your app| Api Token provided by your app| Api Token provided by your app| Api Token provided by your app| Api Token provided by your app|   
Secret version| 1| 1| 1| 1| 1| 1  
AzureAD| | | | | | Yes  
Client ID| | | | | | Client_Id  
Client Secret Value| | | | | | Client Secret Value  
Scopes| | | | | | user_impersonation  
Authorization URL| | | | | | https://login.microsoftonline.com/c6f32d0e-6725-4007-81c2-951e853061a6/oauth2/authorize  
  
You can use the following connection properties to manage data fetched from Azure DevOps.

Catalog

This property specifies the name or ID of the project you want to connect to. To obtain a list of project IDs and names, execute a `SELECT` query against the Projects table.

  * To query data for a specific project, set **Catalog** to the project name or its ID in the format Project_projectname.  
If the project name is **dev** with the ID `2ee729d6-804d-4ece-84af-d5befa94abe8`, set **Catalog** to either `Project_dev` or `Project_2ee729d6-804d-4ece-84af-d5befa94abe8`.
  * To query data that is independent of a specific project, set **Catalog** to **Devops**. If the catalog name is **Devops** , you can use any name in place of **Devops**.



Schema

This property specifies the schema to use, available schemas depend on the repository specified. To obtain a list of repository IDs and names, execute a `SELECT` query against the **Repositories** table.

  * If you set **Catalog** and **Schema** to `INFORMATION` in the connection configuration, you will only have access to the Information Data Model schema. Other project catalogs or schemas will not be exposed.
  * If **Catalog** is set to a project catalog, you can set **Schema** to one of the following: `Analytics`, `Project`, or one of the repository schemas. Once you select the appropriate schema, you can query data within a specific repository.  
To query data from a repository with the ID `3ee729d6-804d-4ece-84af-d5befa94abe8`, set **Catalog** to `Repository_3ee729d6-804d-4ece-84af-d5befa94abe8`.



To create an application on Azure Portal/MS Entra and utilise all the parameters of the created application at Azure AD Connection level, see [Quickstart: Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) and [Register a client application in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).

## System limitations

The Azure DevOps connector can process a maximum of 6 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Azure DevOps connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section lists the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) supported by the connector. To understand how to configure the actions, see Action examples.

### CreateWorkItem action

This action creates a work item.

#### Input parameters of the CreateWorkItem action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
Type | String | Yes | The type of the work item to create.  
From | String | No | The from path for the copy or move operation.  
Op | String | Yes | The patch operation that modifies the work item, such as add, copy, move, remove, replace, or test.  
Path | String | Yes | The path for the operation.  
Value | String | Yes | The value for the operation.  
  
For example on how to configure the `CreateWorkItem` action, see Examples.

### UpdateWorkItem action

#### Input parameters of the UpdateWorkItem action

This action updates a work item.

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
WorkItemId | String | Yes | The ID of the work item.  
From | String | No | The from path for the copy or move operation.  
Op | String | Yes | The patch operation that modifies the work item, such as add, copy, move, remove, replace, or test.  
Path | String | Yes | The path for the operation.  
Value | String | Yes | The value for the operation.  
  
For example on how to configure the `UpdateWorkItem` action, see Examples.

### GetPullRequestCommits action

This action gets the commits for the specified pull request.

#### Input parameters of the GetPullRequestCommits action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID or name of the repository. If the ProjectId is not set, you must set the RepositoryId.  
PullRequestId | String | Yes | The ID of the pull request.  
  
#### Output parameters of the GetPullRequestCommits action

For example on how to configure the `GetPullRequestCommits` action, see Examples.

### PushChanges action

This action pushes changes to a repository in your Azure DevOps instance.

#### Input parameters of the PushChanges action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID or name of the repository. If the ProjectId is not set, you must set the RepositoryId.  
BranchRefName | String | Yes | The name of git branch.  
OldObjectId | String | Yes | The current object ID of the branch.  
CommitComment | String | Yes | Specifies the comment included in the commit.  
ChangesAggregate | String | Yes | An aggregate object that contains details of each change in the commit.  
  
For example on how to configure the `PushChanges` action, see Examples.

### DownloadReleaseLogs action

This action downloads logs for the specific release.

#### Input parameters of the DownloadReleaseLogs action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
ReleaseId | Integer | Yes | The ID of the release.  
FileLocation | String | No | The location of the file.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, and BASE64. The default value is BASE64.  
FileStream | String | No | An instance of an output stream where file data is written. Only used if FileLocation is not provided.  
  
For example on how to configure the `DownloadReleaseLogs` action, see Examples.

### DownloadTestAttachment action

This action downloads a test result/run attachment.

#### Input parameters of the DownloadTestAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
ResultId | Integer | No | The ID of the test result.  
RunId | Integer | Yes | The ID of the test run.  
AttachmentId | String | No | The ID of the attachment.  
FileLocation | String | No | The location of the file.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, and BASE64. The default value is BASE64.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if FileLocation is not provided.  
  
For example on how to configure the `DownloadTestAttachment` action, see Examples.

### SetProjectProperties action

This action can create, update, and delete team project properties.

#### Input parameters of the SetProjectProperties action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
From | String | No | The from path for the move or copy operation.  
Op | String | Yes | The patch operation that modifies the project properties, such as add, copy, move, remove, replace, or test.  
Path | String | Yes | The path for the operation.  
Value | String | Yes | The value for the operation.  
  
For example on how to configure the `SetProjectProperties` action, see Examples.

### DeleteTestCase action

This action deletes the test case.

#### Input parameters of the DeleteTestCase action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
TestcaseId | Integer | Yes | The ID of the test case.  
  
For example on how to configure the `DeleteTestCase` action, see Examples.

### RunPipeline action

This action runs a pipeline with the specified configuration.

#### Input parameters of the RunPipeline action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
PipelineId | Integer | Yes | The ID of the pipeline.  
PipelineVersion | Integer | No | The version of the pipeline to run.  
Resources | String | Yes | The resources the run requires.  
Variables | String | No | The list of variables and values for use during pipeline execution.  
StagesToSkip | String | No | The array of stage names to skip.  
TemplateParameters | String | No | A key-value map of parameters used during pipeline execution.  
  
For example on how to configure the `RunPipeline` action, see Examples.

### CreatePullRequest action

This action creates a pull request with the specified configuration.

#### Input parameters of the CreatePullRequest action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID of the repository.  
Title | String | Yes | Title of the pull request.  
Description | String | No | The description of the pull request.  
SourceRefName | String | Yes | The name of the source branch of the pull request.  
TargetRefName | String | Yes | The name of the target branch of the pull request.  
CompletionOptions | String | No | Options which affect how the pull request will be merged when it is completed.  
IsDraft | Boolean | No | Draft / WIP pull request.  
Labels | String | No | The labels associated with the pull request.  
MergeOptions | String | No | Options used when the pull request merge runs.  
Reviewers | String | No | A list of reviewers on the pull request.  
WorkItemRefs | String | No | Any work item references associated with this pull request.  
  
For example on how to configure the `CreatePullRequest` action, see Examples.

### UpdatePullRequest action

This action updates a pull request with the specified configuration.

#### Input parameters of the UpdatePullRequest action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID of the repository.  
PullRequestId | String | Yes | The ID of the pull request.  
Title | String | No | Title of the pull request.  
Description | String | No | The description of the pull request.  
Status | String | No | Status of the pull request.  
TargetRefName | String | No | The name of the target branch of the pull request. Only available when the PR retargeting feature is enabled.  
CompletionOptions | String | No | Options which affect how the pull request will be merged when it is completed.  
MergeOptions | String | No | Options used when the pull request merge runs.  
AutoCompleteSetById | String | No | ID of the user who enabled autocomplete.  
  
For example on how to configure the `UpdatePullRequest` action, see Examples.

### GetPullRequestCommits action

This action gets the commits for the specified pull request with the specified configuration.

#### Input parameters of the GetPullRequestCommits action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID of the repository.  
PullRequestId | String | Yes | ID of the pull request.  
  
For example on how to configure the `GetPullRequestCommits` action, see Examples.

### AddBuildTag action

This action adds a tag to a build.

#### Input parameters of the AddBuildTag action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
BuildId | String | Yes | The ID of the build.  
Tag | String | Yes | The tag to add to the build.  
  
For example on how to configure the `AddBuildTag` action, see Examples.

### DeleteBuildTag action

This action deletes a tag from a build.

#### Input parameters of the DeleteBuildTag action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
BuildId | String | Yes | The ID of the build.  
Tag | String | Yes | The tag to remove from the build.  
  
For example on how to configure the `DeleteBuildTag` action, see Examples.

### DownloadBuildReports action

This action downloads build reports.

#### Input parameters of the DownloadBuildReports action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
BuildId | Integer | Yes | The ID of the build.  
FileLocation | String | No | The location of the file.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, and BASE64. The default value is BASE64.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if FileLocation is not provided.  
  
For example on how to configure the `DownloadBuildReports` action, see Examples.

### DownloadBuildLogs action

This action downloads build logs.

#### Input parameters of the DownloadBuildLogs action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | Yes | The ID of the Azure DevOps project.  
BuildId | Integer | Yes | ID of the build.  
LogId | Integer | Yes | The ID of the log.  
StartLine | Integer | No | The starting line of the build.  
EndLine | Integer | No | The endinf line of the build.  
FileLocation | String | No | The location of the file.  
Encoding | String | No | The FileData input encoding type. The allowed values are NONE, and BASE64. The default value is BASE64.  
FileStream | String | No | An instance of an output stream where file data is written to. Only used if FileLocation is not provided.  
  
For example on how to configure the `DownloadBuildLogs` action, see Examples.

### UpdateUser action

This action updates a user details.

#### Input parameters of the UpdateUser action

Parameter name | Data type | Required | Description  
---|---|---|---  
UserId | String | Yes | The ID of the user.  
From | String | No | The from path for the move or copy operation.  
Op | String | Yes | The patch operation that modifies the user, such as add, copy, move, remove, replace, or test.  
Path | String | No | The path for the operation.  
Value | String | No | The value for the operation.  
  
For example on how to configure the `UpdateUser` action, see Examples.

### CloneTestPlan action

This action clones a test plan.

#### Input parameters of the CloneTestPlan action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | No | The ID of the Azure DevOps project.  
DeepClone | Boolean | No | Clones all the associated test cases as well.  
CloneRequirements | Boolean | No | If set to true, the requirements are cloned. The default value is false.  
CopyAllSuites | Boolean | No | Copies all suites from a source plan.  
CopyAncestorHierarchy | Boolean | No | Copy ancestor hierarchy.  
DestinationWorkItemType | String | No | Name of the workitem type of the clone.  
OverrideParameters | String | No | Key-value pairs where each key's value is overridden by the specified value.   
RelatedLinkComment | String | No | Adds a comment to the cloned test plan.  
DestinationPlanAreaPath | String | No | Area of the test plan.  
DestinationPlanBuildId | String | No | Build to be tested.  
DestinationPlanDescription | String | No | The description of the test plan.  
DestinationPlanEndDate | String | No | The end date for the test plan.  
DestinationPlanIteration | String | No | The iteration path of the test plan.  
DestinationPlanName | String | Yes | The name of the test plan.  
DestinationPlanOwnerId | String | No | The User ID of the owner of the test plan.  
DestinationPlanProject | String | No | The destination's project name.  
DestinationPlanStartDate | String | No | the start date for the test plan.  
DestinationPlanState | String | No | The state of the test plan.  
DestinationPlanSync | Boolean | No | Specifies how duplicate tests across suites in a test plan must behave.  
SourceTestPlanId | Integer | Yes | The ID of the source test plan.  
SourceTestPlanSuiteId | Integer | No | A comma-separated list of Test Suite IDs to clone inside source test plan.  
  
For example on how to configure the `CloneTestPlan` action, see Examples.

### CloneTestSuite action

This action clones test suite details.

#### Input parameters of the CloneTestSuite action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | No | The ID of the Azure DevOps project.  
DeepClone | Boolean | No | Clones all the associated test cases.  
CloneRequirements | Boolean | No | If set to true, the requirements are cloned. The default value is false.  
CopyAllSuites | Boolean | No | Copies all suites from a source plan.  
CopyAncestorHierarchy | Boolean | No | Copies ancestor hierarchy.  
DestinationWorkItemType | String | No | The name of the workitem type for the clone.  
OverrideParameters | String | No | Key-value pairs where each key's value is overridden by the specified value.  
RelatedLinkComment | String | No | Adds a comment to the cloned test suite.  
DestinationTestSuiteId | Integer | Yes | The ID of the destination test suite.  
DestinationProjectName | String | No | The project name at destination.  
SourceTestSuiteId | Integer | Yes | The ID of the source test suite.  
  
For example on how to configure the `CloneTestSuite` action, see Examples.

### CloneTestCase action

This action clones test case details.

#### Input parameters of the CloneTestCase action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | No | The ID of the Azure DevOps project.  
IncludeAttachments | Boolean | No | Includes attachments of a test case if set to true, the default value is set to false.  
IncludeLinks | Boolean | No | If set to true, the links are included. The default value is false.  
RelatedLinkComment | String | No | To add a comment to the cloned test case.  
DestinationTestPlanId | Integer | Yes | The ID of the destination test plan.  
DestinationTestSuiteId | Integer | Yes | The ID of the destination test suite.  
SourceTestPlanId | Integer | Yes | The ID of the source test plan.  
SourceTestSuiteId | Integer | Yes | The ID of the source test suite.  
TestCaseId | Integer | Yes | A comma-separated list of test case IDs to clone.  
  
For example on how to configure the `CloneTestCase` action, see Examples.

### DeletePullRequestAttachment action

This action deletes pull request attachment details.

#### Input parameters of the DeletePullRequestAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
ProjectId | String | No | The ID of the Azure DevOps project.  
RepositoryId | String | Yes | The ID of the repository.  
PullRequestId | Integer | Yes | The ID of the pull request.  
FileName | String | Yes | The name of the attachment.  
  
For example on how to configure the `DeletePullRequestAttachment` action, see Examples.

## Action examples

### Example - Create a work item

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateWorkItem` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "Type": "Bug", "Value": "Googlecloud_Testing_Bug_M", "Op": "add", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Path": "/fields/System.Title" }
         

If the action is successful, the `CreateWorkItem` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
    "Success": "True"
    }]
    




To create various entities such as a Task, Epic, User Story, Test Case, Feature, and Issue, you only need to modify the value of the "Type" field in the input payload.  
To set a Type to Epic, you can set `"Type": "Epic"`. Similarly, you can change the value to "Type": "Task", "Type": "User Story", "Type": "Test Case", "Type": "Feature", or "Type": "Issue" to create the respective entity.

### Example - Update a work item

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateWorkItem` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "WorkItemId": "35", "Value": "Update Workitem", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Op": "replace", "Path": "/fields/System.Title" }
         

If the action is successful, the `UpdateWorkItem` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "True"
    }]
    




### Example - Get a pull request of a commit

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetPullRequestCommits` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "PullRequestId": "2", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6" }
         

If the action is successful, the `GetPullRequestCommits` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "CommitId": "7299b6623d7d146751d8cf280af301f9a345ff05", "AuthorName": "jeffersonloveshi.k", "AuthorEmail": "jeffersonloveshiking@gmail.com", "AuthoredDate": "2024-08-12 11:25:23.0", "CommitterName": "lakshminarayana.k", "CommitterEmail": "jeffersonloveshiking@gmail.com", "CommittedDate": "2024-08-12 11:25:23.0", "Comment": "Added sample.txt", "CommentTruncated": null, "Url": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/e848b49e-704f-4df3-94ce-4f23176715b6/commits/7299b6623d7d146751d8cf280af301f9a345ff05" } ]
    




### Example - Push changes to a repository

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `PushChanges` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "RepositoryId": "89f79340-8659-4927-9d9f-e8836c19af55", "BranchRefName": "refs/heads/US_Googlecloud_Push1", "OldObjectId": "4d66aafb75efda2bbdda7a2b609b152b1b715b7e", "CommitComment": "Googlecloud PUSH Changes", "ChangesAggregate": "{\n \"changeType\": \"edit\",\n \"item\": {\n \"path\": \"/tasks.md\"\n },\n \"newContent\": {\n \"content\": \"# Tasks\\n\\n* Item 1\\n* Item 2\",\n \"contentType\": \"rawtext\"\n }\n }" }
         

If the action is successful, the `PushChanges` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "NewObjectId": "949e4710336bc5bdc779ca6b334e029c2f50a029", "CommitId": "949e4710336bc5bdc779ca6b334e029c2f50a029", "CommitTreeId": "7e7394dcfc5b4d4cf2c8c21d70a96fe34f8eaf3e", "AuthorName": "Charlie Cruz", "AuthorEmail": "baklavainthebalkans@gmail.onmicrosoft.com", "AuthoredDate": "2024-11-19 07:04:42.0", "CommitterName": "Charlie Cruz", "CommitterEmail": "baklavainthebalkans@gmail.onmicrosoft.com", "CommittedDate": "2024-11-19 07:04:42.0", "CommitUrl": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/89f79340-8659-4927-9d9f-e8836c19af55/commits/949e4710336bc5bdc779ca6b334e029c2f50a029", "RepositoryId": "89f79340-8659-4927-9d9f-e8836c19af55", "RepositoryName": "refs/heads/US_Googlecloud_Push1", "PushId": "193", "PushDate": "2024-11-19T07:04:42.5793751Z", "PushURL": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/89f79340-8659-4927-9d9f-e8836c19af55/pushes/193" } ]
    




### Example - Download the logs of a release

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadReleaseLogs` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "ReleaseId": 2 }
         

If the action is successful, the `DownloadReleaseLogs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "FileData": "{Base64encodedvalue}]
    




### Example - Download a test result/run attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadTestAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RunId": 50, "AttachmentId": "2" }
         

If the action is successful, the `DownloadTestAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "FileData": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAIAAABvFaqvAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABlSURBVDhP7cxBCsAgDERR739pG/CnGJI0FopQ8O2cjNP6R85QbeNQU7wT1dkijaQ3vkZoWElaoTeJojW01cYh0jwfgiFBV/lEjOZtacijN/nLkOBHhIaVDgn+Wdycp6FXzlCl9wt0Y0cAzHo/zgAAAABJRU5ErkJggg==" } ]
    




### Example - Set a project properties

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SetProjectProperties` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Op": "add", "Path": "/Alias", "Value": "Google CLoud Properties" }
         

If the action is successful, the `SetProjectProperties` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success" } ]
    




### Example - Delete a test case

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteTestCase` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "TestCaseId": 22255, "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc" }
         

If the action is successful, the `DeleteTestCase` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success" } ]
    




### Example - Run a pipeline for a project

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `RunPipeline` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "PipelineId": 7, "Resources": "{\n \"repositories\": {\n \"self\": {\n \"refName\": \"refs/heads/main\" // Specify the branch or tag\n }\n }\n }" }
         

If the action is successful, the `RunPipeline` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [ { "State": "inProgress", "RunId": "16", "RunName": "20241113.2", "RunHref": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/pipelines/7/runs/16", "CreatedDate": "2024-11-13 12:07:38.9237296" } ]
    




### Example - Update a pull request

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdatePullRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6", "PullRequestId": "26", "Description": "updated pull req", "Title": "Googlecloud M pull request" }
         

If the action is successful, the `UpdatePullRequest` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "PullRequestId": 26 } ]
    




### Example - Create a pull request

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreatePullRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6", "Title": "Googlecloud M pull request", "SourceRefName": "refs/heads/Test_Branch", "TargetRefName": "refs/heads/main" }
         

If the action is successful, the `CreatePullRequest` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "PullRequestId": 26 } ]
    




### Example - Get a pull request commit

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `GetPullRequestCommits` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "PullRequestId": "23", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6" }
         

If the action is successful, the `GetPullRequestCommits` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "CommitId": "ebb720c5b93c52341cb86ccfb42258bb562a8406", "AuthorName": "dani.dana", "AuthorEmail": "baklavainthebalkans@gmail.com", "AuthoredDate": "2024-11-26 11:24:19.0", "CommitterName": "dani.dana", "CommitterEmail": "baklavainthebalkans@gmail.com", "CommittedDate": "2024-11-26 11:24:19.0", "Comment": "Updated sample.txt", "CommentTruncated": null, "Url": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/e848b49e-704f-4df3-94ce-4f23176715b6/commits/ebb720c5b93c52341cb86ccfb42258bb562a8406" }, { "CommitId": "353f74b48ada83111449b922f4660a338e058989", "AuthorName": "dani.dana", "AuthorEmail": "baklavainthebalkans@gmail.com", "AuthoredDate": "2024-11-26 11:23:01.0", "CommitterName": "dani.dana", "CommitterEmail": "baklavainthebalkans@gmail.com", "CommittedDate": "2024-11-26 11:23:01.0", "Comment": "Updated bcd", "CommentTruncated": null, "Url": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/e848b49e-704f-4df3-94ce-4f23176715b6/commits/353f74b48ada83111449b922f4660a338e058989" }, { "CommitId": "50a74dee46f8bcad4637d730994144f944c7d589", "AuthorName": "dani.dana", "AuthorEmail": "baklavainthebalkans@gmail.com", "AuthoredDate": "2024-11-26 11:21:59.0", "CommitterName": "dani.dana", "CommitterEmail": "baklavainthebalkans@gmail.com", "CommittedDate": "2024-11-26 11:21:59.0", "Comment": "Added bcd", "CommentTruncated": null, "Url": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/e848b49e-704f-4df3-94ce-4f23176715b6/commits/50a74dee46f8bcad4637d730994144f944c7d589" }, { "CommitId": "9813f562b0548144006f773314704db274c757c4", "AuthorName": "Alex amal", "AuthorEmail": "cloudysanfrancisco@gmail.com", "AuthoredDate": "2024-11-26 11:19:29.0", "CommitterName": "Alex amal", "CommitterEmail": "cloudysanfrancisco@gmail.com", "CommittedDate": "2024-11-26 11:19:29.0", "Comment": "hello", "CommentTruncated": null, "Url": "https://dev.azure.com/charliecruz/64058663-6419-4b11-8ef0-2ebf985949bc/_apis/git/repositories/e848b49e-704f-4df3-94ce-4f23176715b6/commits/9813f562b0548144006f773314704db274c757c4" } ]
    




### Example - Add a build tag

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AddBuildTag` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc","BuildId": "14","Tag": "AddGooglecloud_Tag" }
         

If the action is successful, the `AddBuildTag` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{ "Status": "Success" }]
    




### Example - Delete a build tag

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteBuildTag` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc","BuildId": "14","Tag": "AddGooglecloud_Tag"}
         

If the action is successful, the `DeleteBuildTag` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{ "Status": "Success" }] 
    




### Example - Download a build report

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadBuildReports` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "BuildId": 16 }
         

If the action is successful, the `DownloadBuildReports` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "FileData": "Base64-format data" } ]
    




### Example - Download build logs

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadBuildLogs` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "BuildId": 16, "LogId": 1, "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc" }
         

If the action is successful, the `DownloadBuildLogs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success", "FileData": "Base64-format data" } ]
    




### Example - Update a user

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateUser` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "UserId": "088a8c28-1b83-4538-9c74-b7ca97eb4ef2", "Op": "add", "Path": "/projectEntitlements/50fac9d4-37aa-4a13-a81a-887d12be7b9f", "Value": "{ \"projectRef\": {\n \"id\": \"50fac9d4-37aa-4a13-a81a-887d12be7b9f\",\n \"name\": \"Postman_Testing_Project\"\n }, \n \"group\": {\n \"groupType\": \"projectContributor\"\n }}" }
         

If the action is successful, the `Update User` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "Status": "Success" } ]
    




### Example - Clone a test plan

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CloneTestPlan` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "CloneRequirements": true, "CopyAllSuites": true, "RelatedLinkComment": "Cloned from existing test plan googlecloud", "DestinationPlanName": "TestPlan 2", "DestinationPlanAreaPath": "GCPTesting_New_Project", "DestinationPlanIteration": "GCPTesting_New_Project", "DestinationPlanProject": "GCPTesting_New_Project", "SourceTestPlanId": 1, "CopyAncestorHierarchy": true }
         

If the action is successful, the `CloneTestPlan` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "CloneOperationId": null, "CloneOperationState": "queued", "sourcetestplan_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "sourcetestplan_project_name": "GCPTesting_New_Project", "sourcetestplan_project_state": "unchanged", "sourcetestplan_project_visibility": "unchanged", "sourcetestplan_project_lastupdatetime": "0001-01-01T00:00:00", "sourcetestplan_id": "1", "sourcetestplan_name": "Test Plan 1", "destinationtestplan_id": "15", "destinationtestplan_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "destinationtestplan_project_name": "GCPTesting_New_Project", "destinationtestplan_project_state": "unchanged", "destinationtestplan_project_visibility": "unchanged", "destinationtestplan_project_lastupdatetime": "0001-01-01T00:00:00", "destinationtestplan_updateddate": "2025-01-07T14:02:31.247Z", "destinationtestplan_updatedby_displayname": "Charlie Cruz", "destinationtestplan_updatedby_url": "https://spsprodcin1.vssps.visualstudio.com/A0f5fd5e8-7721-4842-b504-2a8ddb8efeb0/_apis/Identities/df102a0c-59d2-6d69-aecd-556086d6d8d6", "destinationtestplan_updatedby__links_avatar_href": "https://dev.azure.com/sunitavenkata2024/_apis/GraphProfile/MemberAvatars/msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_updatedby_id": "df102a0c-59d2-6d69-aecd-556086d6d8d6", "destinationtestplan_updatedby_uniquename": "sunitavenkata2024@outlook.com", "destinationtestplan_updatedby_imageurl": "https://dev.azure.com/sunitavenkata2024/_apis/GraphProfile/MemberAvatars/msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_updatedby_descriptor": "msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_rootsuite_id": "16", "destinationtestplan_rootsuite_name": "TestPlan 2", "destinationtestplan__links__self_href": "https://dev.azure.com/sunitavenkata2024/GCPTesting_New_Project/_apis/testplan/Plans/15", "destinationtestplan__links_clienturl_href": "mtms://dev.azure.com:443/sunitavenkata2024/p:GCPTesting_New_Project/Testing/testplan/connect?id=15", "destinationtestplan__links_rootsuite_href": "https://dev.azure.com/sunitavenkata2024/GCPTesting_New_Project/_apis/testplan/Plans/15/Suites/16", "destinationtestplan_revision": "1", "destinationtestplan_name": "TestPlan 2", "destinationtestplan_areapath": "GCPTesting_New_Project", "destinationtestplan_startdate": "2025-01-07T14:02:31.0878913Z", "destinationtestplan_enddate": "2025-01-14T14:02:31.0878913Z", "destinationtestplan_iteration": "GCPTesting_New_Project", "destinationtestplan_owner_displayname": "sunita m V", "destinationtestplan_owner_url": "https://spsprodcin1.vssps.visualstudio.com/A0f5fd5e8-7721-4842-b504-2a8ddb8efeb0/_apis/Identities/df102a0c-59d2-6d69-aecd-556086d6d8d6", "destinationtestplan_owner__links_avatar_href": "https://dev.azure.com/sunitavenkata2024/_apis/GraphProfile/MemberAvatars/msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_owner_id": "df102a0c-59d2-6d69-aecd-556086d6d8d6", "destinationtestplan_owner_uniquename": "sunitavenkata2024@outlook.com", "destinationtestplan_owner_imageurl": "https://dev.azure.com/sunitavenkata2024/_apis/GraphProfile/MemberAvatars/msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_owner_descriptor": "msa.ZGYxMDJhMGMtNTlkMi03ZDY5LWFlY2QtNTU2MDg2ZDZkOGQ2", "destinationtestplan_state": "Active", "destinationtestplan_testoutcomesettings_syncoutcomeacrosssuites": "false", "cloneoptions_relatedlinkcomment": "Cloned from existing test plan gcp", "cloneoptions_copyallsuites": "true", "cloneoptions_copyancestorhierarchy": "true", "cloneoptions_clonerequirements": "true", "cloneoperationresponse_state": "queued", "cloneoperationresponse_links__self_href": "https://dev.azure.com/sunitavenkata2024/GCPTesting_New_Project/_apis/testplan/Plans/CloneOperation/0" } ]
    




### Example - Clone a test suite

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CloneTestSuite` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "SourceTestSuiteId": 18, "CopyAllSuites": true, "CopyAncestorHierarchy": true, "DestinationTestSuiteId": 2 }
         

If the action is successful, the `CloneTestSuite` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [ { "CloneOperationId": 2, "CloneOperationState": "queued", "sourcetestsuite_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "sourcetestsuite_project_name": "GCPTesting_New_Project", "sourcetestsuite_project_state": "unchanged", "sourcetestsuite_project_visibility": "unchanged", "sourcetestsuite_project_lastupdatetime": "0001-01-01T00:00:00", "sourcetestsuite_id": "18", "sourcetestsuite_name": "Test Plan 3", "destinationtestsuite_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "destinationtestsuite_project_name": "GCPTesting_New_Project", "destinationtestsuite_project_state": "unchanged", "destinationtestsuite_project_visibility": "unchanged", "destinationtestsuite_project_lastupdatetime": "0001-01-01T00:00:00", "destinationtestsuite_id": "2", "destinationtestsuite_name": "Test Plan 1", "cloneoptions_copyallsuites": "true", "cloneoptions_copyancestorhierarchy": "true", "cloneoptions_clonerequirements": "false", "cloneoperationresponse_opid": "2", "cloneoperationresponse_state": "queued", "cloneoperationresponse_links__self_href": "https://dev.azure.com/sunitavenkata2024/GCPTesting_New_Project/_apis/testplan/Suites/CloneOperation/2" } ]
    




### Example - Clone a test case

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CloneTestCase` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "SourceTestPlanId": 1, "DestinationTestPlanId": 20, "SourceTestSuiteId": 2, "DestinationTestSuiteId": 21, "TestCaseId": 3 }
         

If the action is successful, the `CloneTestCase` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [ { "CloneOperationId": 3, "CloneOperationState": "queued", "sourcetestsuite_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "sourcetestsuite_project_name": "GCPTesting_New_Project", "sourcetestsuite_project_state": "unchanged", "sourcetestsuite_project_visibility": "unchanged", "sourcetestsuite_project_lastupdatetime": "0001-01-01T00:00:00", "sourcetestsuite_testcaseids": "3", "sourcetestsuite_id": "2", "sourcetestsuite_name": "Test Plan 1", "destinationtestsuite_project_id": "ea4270d3-d335-4ef1-b1af-37a7591880cf", "destinationtestsuite_project_name": "GCPTesting_New_Project", "destinationtestsuite_project_state": "unchanged", "destinationtestsuite_project_visibility": "unchanged", "destinationtestsuite_project_lastupdatetime": "0001-01-01T00:00:00", "destinationtestsuite_id": "21", "destinationtestsuite_name": "Test Plan 4", "cloneoptions_includelinks": "false", "cloneoptions_includeattachments": "false", "cloneoperationresponse_opid": "3", "cloneoperationresponse_state": "queued", "cloneoperationresponse_links__self_href": "https://dev.azure.com/sunitavenkata2024/GCPTesting_New_Project/_apis/testplan/Plans/CloneOperation/3" } ]
    




### Example - Delete a pull request attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeletePullRequestAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6", "PullRequestId": 26, "FileName": "Company.jpg" }
         

This action returns confirmation message of the DeletePullRequestAttachment If the action is successful, the `DeletePullRequestAttachment` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [ { "Status": "Success" } ]
    




## Entity operation examples

### Retrieve all dashboards in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Dashboards` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement. Please check the Note section below

The value for **filterClause** should be always passed within the single quotes (') in this format.  
You can use the **filterClause** for filtering our certain set of records based on any columns.




### Example - Retrieve a single dashboard using its ID

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Dashboards` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to "2f671e29-e48f-4d26-8869-859e154b5f20" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"2f671e29-e48f-4d26-8869-859e154b5f20"` in the **Input Value** field and choose the EntityId as Local variable. 

The value for Entity ID should be passed directly, such as "2f671e29-e48f-4d26-8869-859e154b5f20". Here, "2f671e29-e48f-4d26-8869-859e154b5f20" is the unique primary key value, which is passed.

In some cases, passing a single Entity ID may cause an error because the entity has two composite keys. In such cases, you can use the **filterClause** and pass the value, such as id='2f671e29-e48f-4d26-8869-859e154b5f20'.




### Example - Remove a dashboard using its ID

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Dashboards` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the entity ID to "2f671e29-e48f-4d26-8869-859e154b5f20" which is the Key to be passed. To set the entity ID, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"2f671e29-e48f-4d26-8869-859e154b5f20"` in the **Input Value** field and choose the EntityId as Local variable. 

If entity has two composite business or primary keys, instead of specifying the **entityId** , you can set the **filterClause** to ` id='2f671e29-e48f-4d26-8869-859e154b5f20'`.




### Example - Create a new dashboard in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Dashboard` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "TestingGooglecloud09", "TeamId": "9f2e4d3c-ed57-474f-bab1-3de5727e60a1" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "a2402c49-6c17-43a9-bfc4-3701d07bcfee" }
         




### Example - Create a new user entitlement in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Users` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "UserPrincipalName": "jeffersonloveshiking@gmail.com", "UserSubjectKind": "user", "AccessLevelAccountLicenseType": "Stakeholder", "UserOriginId": "e3d3e130-51dc-48c5-a510-cce7a9df63af" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "5e373a81-073d-4d64-a2c5-23d0b6cc287f" }
         




### Example - Create a new query in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Queries` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "New Queries Googlecloud", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "IsFolder": true, "Wiql": "SELECT [System.Id], [System.Title], [System.State] FROM WorkItems WHERE [System.WorkItemType] = 'Bug' AND [System.State] = 'New' ORDER BY [System.ChangedDate] DESC", "ParentQueryId": "df947cf9-dbbe-43bc-93a4-3e4d7287adb8" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "cf4a25e8-d2d2-48b7-a483-dd901c78293b" }
         




### Example - Create a new pipeline in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Pipelines` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Name": "Googlecloud pipeline", "Folder": "\\\\", "ConfigurationPath": "build-deploy.yml", "ConfigurationRepositoryId": "957b9cd1-f7f1-45d4-8665-ed7120021da9", "ConfigurationRepositoryType": "azureReposGit", "ConfigurationType": "yaml" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": 9 }
         




### Example - Create a deployment group in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DeploymentGroups` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "Deployment group 2 Googlecloud" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": 139 }
         




### Example - Create a new test configuration in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestPlan` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "Googlecloud_TestPlan" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": 106 }
         




### Example - Create a test suite in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestSuite` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "Googlecloud_Suite", "PlanId": 106, "SuiteType": "staticTestSuite", "ParentSuiteId": 108, "InheritDefaultConfigurations": false }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": 22264 }
         




### Example - Create a test run in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestRun` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "TestRun_Googlecloud1"}
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": 46 }
         




### Example - Create a new project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Projects` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "project from Googlecloud test 4", "Description": "This is new project", "CapabilitiesVersionControlType": "Git\n", "CapabilitiesProcessTemplateTypeId": "6b724908-ef14-45cf-84f8-768b5384da45" }
         

If the integration is successful, the `Projects` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "c1a8e7f4-9afa-47a8-9862-b56229e134a9" }
         

The ID generated after performing the Create operation on a project is not the actual project ID.  
To retrieve the exact project details, you need to perform the List operation with the project name as a filter condition, such as Name= 'Google Project Integration'.




### Example - Create a team in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Teams` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "M new team"}
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "5285fb98-a1bc-42e1-9668-3c2780061367" }
         




### Example - Create an environment in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Environments` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "Google CLoud Env M", "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Description": "Google Cloud created environment" }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "9" }
         




### Example - Create a new widget in a dashboard

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Widgets` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "Name": "Widget 2", "DashboardId": "6cb82f8d-393c-422e-b4e3-563d5e34fc31", "TeamId": "9f2e4d3c-ed57-474f-bab1-3de5727e60a1", "RowPosition": 4, "ColumnPosition": 4, "RowSpanSize": 1, "ColumnSpanSize": 2, "ContributionId": "ms.vss-dashboards-web.Microsoft.VisualStudioOnline.Dashboards.OtherLinksWidget" }
         

This example demonstrates how to add a Widgets If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "7d049ae2-d995-4b3e-9ebd-662d94a53cc8" }
         




### Example - Add a reviewer to a pull request in a repository

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PullRequestReviewers` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6", "PullRequestId": 22, "Id": "38b14cd8-d8f2-4d79-9204-19adbcb62c81", "Vote": 0 }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "38b14cd8-d8f2-4d79-9204-19adbcb62c81", "PullRequestId": null }
         




### Example - Create a variable group in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `VariableGroups` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
           "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc",
           "Type": "Vsts",
           "Variables": "{\n    \"SampleVariableName1\": {\n      \"value\": \"SampleValue1\"\n    },\n    \"SampleVariableName2\": {\n      \"value\": \"SampleValue2\"\n    }\n  }",
           "VariableGroupProjectRefs": "[\n    {\n      \"description\": \"SampleDescription\",\n      \"name\": \"Variable Group new test\",\n      \"projectReference\": {\n        \"id\": \"64058663-6419-4b11-8ef0-2ebf985949bc\",\n        \"name\": \"Googlecloud-Demo-Project\"\n      }\n    }\n  ]",
           "Name": "Variable Group new test"
         }

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {"Id": "12"}
         




### Example - Create a new build definition in a repository

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BuildDefinition` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {"Name": "New Build definition from googlecloud test 11","RepositoryType": "TfsGit","ProcessYamlFilename": "data.txt","RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6","Tags": "1"}
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {"Id": "25"}
         




### Example - Create a release in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Releases` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { "ProjectId": "64058663-6419-4b11-8ef0-2ebf985949bc", "Reason": "manual", "Description": "This is a googlecloud release", "ReleaseDefinitionId": 1 }
         

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         { "Id": "13" }
         




### Example - Update a team's name or description in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Teams` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "M new team update" }
         

  5. Set the entity ID in Data Mapper to the entity of the Teams To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `5285fb98-a1bc-42e1-9668-3c2780061367`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "5285fb98-a1bc-42e1-9668-3c2780061367" }
         




### Example - Update a query in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Queries` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Update Queries" }
         

  5. Set the entity ID in Data Mapper to the entity of the Queries To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `81797017-624d-4967-bc85-842a817bff48`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "81797017-624d-4967-bc85-842a817bff48" }
         




### Example - Update a dashboard in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Dashboard` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": " update from googlecloud" }
         

  5. Set the entity ID in Data Mapper to the entity of the Dashboard To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `139`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "139" }
         




### Example - Update a test suite in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestSuite` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "UPdated_Suite", "ParentSuiteId": 108 }
         

  5. Set the entity ID in Data Mapper to the entity of the TestSuite To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `22264`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "22264" }
         




### Example - Update a deployment group in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DeploymentGroups` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Deployment" }
         

  5. Set the entity ID in Data Mapper to the entity of the DeploymentGroups To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `138`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "138" }
         




### Example - Update a test plan in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestPlan` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "TestPlan_Update" }
         

  5. Set the entity ID in Data Mapper to the entity of the TestPlan To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `104`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "104" }
         




### Example - Update a test run in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `TestRuns` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Update Test Run", "Comment": "Google cloud has updated the test run use case." }
         

  5. Set the entity ID in Data Mapper to the entity of the TestRuns To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `46`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "46" }
         




### Example - Update a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Projects` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Projects Update" }
         

  5. Set the entity ID in Data Mapper to the entity of the Projects To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{ "Id": "1677d4b0-eaf6-47c2-88ee-78819b00977d" }`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "1677d4b0-eaf6-47c2-88ee-78819b00977d" }
         




### Example - Update an environment in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Environments` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Environment Update M", "Description": "Update environment " }
         

  5. Set the entity ID in Data Mapper to the entity of the Environments To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{ "Id": "9" }`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": 9 }
         




### Example - Update a variable group in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `VariableGroups` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {
           "VariableGroupProjectRefs": "[\n    {\n      \"description\": \"SampleDescription\",\n      \"name\": \"New VariableGroup googlecloud updated\",\n      \"projectReference\": {\n        \"id\": \"64058663-6419-4b11-8ef0-2ebf985949bc\",\n        \"name\": \"GoogleCloud-Demo-Project\"\n      }\n    }\n  ]",
           "Variables": "{\n    \"SampleVariableName1\": {\n      \"value\": \"SampleValue1\"\n    },\n    \"SampleVariableName2\": {\n      \"value\": \"SampleValue2\"\n    }\n  }",
           "Name": "Variable Group new test updated"
         }
         

  5. Set the entity ID in Data Mapper to the entity of the VariableGroups To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{ "Id": "12" }`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": 12 }
         




### Example - Update a build definition in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `BuildDefinition` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Name": "Build definition update 25","RepositoryId": "e848b49e-704f-4df3-94ce-4f23176715b6","RepositoryType": "TfsGit","ProcessYamlFilename": "data.txt","Revision": 1 }
         

  5. Set the entity ID in Data Mapper to the entity of the BuildDefinition. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{ ProjectId='64058663-6419-4b11-8ef0-2ebf985949bc' and Id='25'}`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": 25 }
         




### Example - Update a pull request reviewer in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `PullRequestReviewers` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         {"isFlagged": true}
         

  5. Set the entity ID in Data Mapper to the entity of the PullRequestReviewers. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{ ProjectId='64058663-6419-4b11-8ef0-2ebf985949bc' and RepositoryId='e848b49e-704f-4df3-94ce-4f23176715b6' and PullRequestId='22' and Id='38b14cd8-d8f2-4d79-9204-19adbcb62c81'}`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         { "Id": "38b14cd8-d8f2-4d79-9204-19adbcb62c81","PullRequestId": null}
         




### Example - Update a release in a project

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Releases` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 
         
         { "Description": "Update Release Description googlecloud","Name": "Update release googlecloud"}
         

  5. Set the entity ID in Data Mapper to the entity of the Releases. To set the entity ID, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload/FilterClause as Local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `{"Id": 13}`.

Running this example, returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {"Id": 13 }
         




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
