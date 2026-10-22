---
url: https://docs.cloud.google.com/data-agent-kit/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:25.526449+00:00
---

# Troubleshoot  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the visible errors captured and surfaced by the Data Agent Kit IDE extension. These errors are typically shown as **Notifications** (pop-ups) or as **Status Bar Warnings** in the IDE. Use this guide to identify and resolve issues.

If you're not able to identify the source of an issue after reviewing the possible error listed here, try signing out and signing back in.

## Authentication and gcloud CLI errors

These errors impact the foundational connectivity of the extension.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
Status bar shows a `$(warning)` icon next to your account name. | The logged-in extension account differs from the active gcloud CLI account. | Run `gcloud auth login` and `gcloud auth application-default login` with the same account used to sign into Google Cloud.  
Status bar shows a `$(warning)` icon. | Extension settings such as project ID, region, or billing project ID don't match gcloud CLI settings. | Click the warning icon in the project status bar to synchronize settings between the extension and the gcloud CLI. Alternatively, manually update the configurations in either tool to ensure they match.  
`Cannot sync Google Cloud CLI to Extension Settings: CLI identity does not match extension account` or `Cannot sync Extension Settings to Google Cloud CLI: CLI identity does not match extension account` | Attempting to sync settings while accounts are inconsistent. | Align accounts between the gcloud CLI and the extension. Ensure that they are using the same user account, project, region, and billing project.  
`Cannot sync settings: Google Cloud CLI is not installed.` | Attempting to sync settings while the gcloud CLI isn't installed. | Install the gcloud CLI.  
  
## Explorer and API fetching errors

The following are general errors encountered when browsing cloud resources in the Google Cloud Data Agent Kit menu tree.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Failed to load ${itemKind}: ${error.message}` | The server can't authorize your request (`HTTP 403 Forbidden` status code), the server can't find the resources (`HTTP 404 Not Found` status code), or the API isn't enabled. | Verify Identity and Access Management (IAM) permissions; ensure the relevant API, such as BigQuery, is enabled in settings.  
`No Google Cloud project selected.` | A feature was triggered without an active project. | Use the project picker in the status bar to select a project.  
  
## BigQuery and Dataform errors

The following errors are specific to SQL transformations and Dataform project management.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Dataform CLI is not installed. Dataform features will not work.` | The `Dataform` npm package is not installed globally. | Click **Install Dataform CLI** in the dialog to automate installation.  
`Failed to compile project in folder...: ${stderr}` | Syntax errors in `.sqlx` files or invalid `workflow_settings.yaml`. | Check the Dataform `Compiled Query` view for specific syntax errors.  
`Failed to run Dataform project: ${message}` | BigQuery job execution failure. | Review the BigQuery job history for detailed execution logs.  
  
## Managed Service for Apache Spark and Spark errors

The following errors are related to cluster management and Spark execution.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Error starting/stopping/restarting cluster ${name}: ${message}` | Insufficient IAM permissions or cluster in transition. | Ensure you have the `roles/dataproc.editor` role; check if the cluster status is already **UPDATING**.  
`Error: No cluster name found.` | Internal reference error in the tree view. | Refresh the **Spark Resource Explorer** view.  
`Failed to redirect to Spark UI: ${message}` | Cluster is stopped or Component Gateway is disabled. | Start the cluster and ensure Component Gateway is enabled in the cluster configuration.  
`Failed to load [clusters/jobs/sessions/session templates]: [message]` | API error | Refresh the **Spark Resource Explorer** view.  
`Failed to start Jupyter process / Pip install failed.` | Local Jupyter server startup failed or installation of required packages failed. | Open a new Spark Notebook with the remote kernel.  
`No sample notebooks found for the selected kernel type.` | Sample notebooks for the selected kernel type (local or remote) are not available. | Not applicable  
`This system does not have Windows Long Path support enabled. Please enable long paths and restart your IDE to work with Spark Notebooks on remote kernels. [Learn More](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later)` | This is specifically for Windows users when long paths are not enabled on your machine. | Enable long paths by referring to the link in the notification.  
`google-cloud-jupyter-config and jupyter_server are required to connect to remote kernels on Managed Service for Apache Spark. Install them?` | This comes up when the user tries to use a remote kernel for the first time. | Install dependencies by clicking the notification and selecting **Yes** in the confirmation dialog.  
`Requires package installation` | Shown in the kernel picker description next to **Remote Kernel** if Jupyter dependencies are missing. | Install dependencies by clicking the notification and selecting **Yes** in the confirmation dialog.  
`Install dependencies for remote Spark kernels. Require google-cloud-jupyter-config and jupyter_server` | Shown in the kernel picker description when user runs an existing notebook on **Remote Kernel** | Install dependencies by clicking the notification and selecting **Yes** in the confirmation dialog.  
  
## Cloud Storage errors

The following errors are surfaced while managing buckets and objects.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`A folder with the name... already exists.` | Naming collision in the bucket. | Choose a unique folder name.  
`Upload/Download failed: ${message}` | Permission denied or network timeout. | Verify `Storage Object Admin` or `Creator` roles.  
`Failed to create bucket: ${message}` | Name already taken globally or invalid characters. | Follow [Cloud Storage bucket naming rules](https://cloud.google.com/storage/docs/naming-buckets).  
  
## Generic interface errors

These errors indicate UI-level failures.

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`No workspace folder open.` | User is in **No Folder** mode in the IDE. | Open a folder using `File > Open Folder`.  
`No active notebook editor found.` | You are running Spark or SQL commands without an open notebook. | Open a `.ipynb` or `.sql` file.  
`Cannot insert item: unsupported resource type.` | Attempting to drag-and-drop a resource that has NoSQL string representation. | Only tables, views, and columns can be inserted into editors.  
  
## Database errors

The following errors are returned when querying Google Cloud databases.

### AlloyDB

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`postgresql error: role "[USER_EMAIL]" does not exist` | The user logged into the extension has not been added as an IAM user to the instance. | See [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) to add the user as an IAM user.  
`postgresql error: permission denied for table [TABLE_NAME]` | The IAM user does not have permission for the object. | See [Grant appropriate database permissions to IAM users](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#grant-privileges) to grant permission to the IAM user for the object.  
  
### Cloud SQL for MySQL

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Invalid request: Some of your SQL statements failed to execute. Details: Error 1045 (28000): Access denied for user '[USER]'@'localhost' (using password: YES).` | 

  * For IAM database authentication: The user logged into the extension has not been added as an IAM user to the instance.
  * For built-in database authentication: The selected regional secret or secret version in Secret Manager does not match the database user's password.

| 

  * For IAM database authentication: See [Add an individual IAM user or service account to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user).
  * For built-in database authentication: Verify the user and regional secret in the query settings, or see [Configure the database user](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#configure-db-user) in the Cloud SQL Data API documentation.

  
`Invalid request: Some of your SQL statements failed to execute. Details: Error 1044 (42000): Access denied for user '[USER]'@'%' to database '[DB_NAME]'.` | The database user does not have permission to access the database. | See [Grant database privileges to an individual IAM user or service account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#grant-db-privileges) or [Configure the database user](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#configure-db-user) to grant privileges for the database.  
`Invalid request: Failed to access secret '[SECRET_VERSION]': generic::PERMISSION_DENIED: Permission 'secretmanager.versions.access' denied for resource '[SECRET_VERSION]' (or it may not exist).` | The account logged into the extension does not have permission to access the regional secret version in Secret Manager, or the secret version doesn't exist. | Verify that the regional secret and secret version selected in the query settings exist. Then grant the `Secret Manager Secret Accessor` (`roles/secretmanager.secretAccessor`) role to your account. See [Required roles or permissions](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#required-roles-permissions) in the Cloud SQL Data API documentation.  
`Invalid request: Secret fetched from Secret Manager is empty` | The selected regional secret version doesn't contain a password. | Add a new secret version that contains the database user's password, and then select it in the query settings.  
`Invalid request: The instance doesn't allow using ExecuteSql to access this instance. You can allow it by patching the instance with {settings: { dataApiAccess: "ALLOW_DATA_API" }}` | Data API access is not enabled. | Enable Data API access from the query settings or see [Execute SQL statements using the Cloud SQL Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) to enable it from the Google Cloud console or gcloud CLI.  
`Invalid request: IAM authentication is not enabled for the instance [PROJECT_ID]:[INSTANCE_NAME]` | The IAM authentication flag is not enabled. | Enable the IAM authentication flag from the query settings or see [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication) to enable it from the Google Cloud console or gcloud CLI.  
  
### Cloud SQL for PostgreSQL

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Invalid request: The instance doesn't allow using ExecuteSql to access this instance. You can allow it by patching the instance with {settings: { dataApiAccess: "ALLOW_DATA_API" }}` | Data API access is not enabled. | Enable Data API access from the query settings or see [Execute SQL statements using the Cloud SQL Data API](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance) to enable it from the Google Cloud console or gcloud CLI.  
`Invalid request: IAM authentication is not enabled for the instance [PROJECT_ID]:[INSTANCE_NAME]` | The IAM authentication flag is not enabled. | Enable the IAM authentication flag from the query settings or see [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) to enable it from the Google Cloud console or gcloud CLI.  
`Invalid request: Some of your SQL statements failed to execute. Details: pq: password authentication failed for user "[USER]".` | 

  * For IAM database authentication: The user logged into the extension has not been added as an IAM user to the instance.
  * For built-in database authentication: The selected regional secret or secret version in Secret Manager does not match the database user's password.

| 

  * For IAM database authentication: See [Add an individual IAM user or service account to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).
  * For built-in database authentication: Verify the user and regional secret in the query settings, or see [Configure the database user](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user) in the Cloud SQL Data API documentation.

  
`Invalid request: Failed to access secret '[SECRET_VERSION]': generic::PERMISSION_DENIED: Permission 'secretmanager.versions.access' denied for resource '[SECRET_VERSION]' (or it may not exist).` | The account logged into the extension does not have permission to access the regional secret version in Secret Manager, or the secret version doesn't exist. | Verify that the regional secret and secret version selected in the query settings exist. Then grant the `Secret Manager Secret Accessor` (`roles/secretmanager.secretAccessor`) role to your account. See [Required roles or permissions](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#required-roles-permissions) in the Cloud SQL Data API documentation.  
`Invalid request: Secret fetched from Secret Manager is empty` | The selected regional secret version doesn't contain a password. | Add a new secret version that contains the database user's password, and then select it in the query settings.  
`Execution failed. All statements are aborted. Details: pq: permission denied for table [TABLE_NAME]` | The database user does not have permission to access the object. | See [Manage users with IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users) or [Configure the database user](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user) to grant privileges for the database.  
  
### Spanner

**Error message** | **Possible cause** | **Remediation**  
---|---|---  
`Result set too large. Result sets larger than 10.00M can only be yielded through the streaming API.` | Result sizes larger than 10.00 MiB are not supported. | See [`executeSql`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql).  
  
## What's next

  * [Build data engineering pipelines](https://docs.cloud.google.com/data-agent-kit/build-pipelines)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
