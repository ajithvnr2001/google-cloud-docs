---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github/
title: Collect GitHub audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:50.407056+00:00
---

# Collect GitHub audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect GitHub audit logs

**Parser Version:** 23.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest GitHub audit logs to Google Security Operations. You can configure ingestion using one of the following methods:

  * **Google Cloud Storage V2** (recommended): Stream audit logs from GitHub Enterprise Cloud directly to a GCS bucket, then ingest into Google SecOps.
  * **Webhook** : Configure GitHub to push event payloads directly to a Google SecOps webhook endpoint in real time.



GitHub is a cloud-based platform for version control and collaboration that lets developers store and manage code, track changes, and collaborate on software projects. GitHub Enterprise Cloud provides enterprise-grade security features, including audit log streaming for compliance and security monitoring.

## Before you begin

  * Ensure that you have the following prerequisites:

  * A Google SecOps instance

  * A GitHub Enterprise Cloud account with enterprise owner permissions (for GCS streaming) or organization owner permissions (for webhooks)




**For the GCS method, you also need:**

  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create service accounts and manage IAM policies



**For the Webhook method, you also need:**

  * Access to Google Cloud Console (for API key creation)
  * Repository admin or organization owner permissions in GitHub



## Option 1: Configure ingestion using Google Cloud Storage V2 (Recommended)

### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `github-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create a service account for GitHub audit log streaming

GitHub requires a Google Cloud service account with a JSON key to authenticate and write audit logs to your GCS bucket.

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter a descriptive name (for example, `github-audit-streaming`)
     * **Service account description** : Enter `Service account for GitHub Enterprise Cloud audit log streaming to GCS`
  4. Click **Create and Continue**.
  5. Click **Done**.

**Note:** Do not grant any project-level roles at this step. You will grant bucket-level permissions in the next step.



### Grant the service account write access to the GCS bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `github-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `github-audit-streaming@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Creator**
  6. Click **Save**.



### Create a JSON key for the service account

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click the service account (for example, `github-audit-streaming`).
  3. Go to the **Keys** tab.
  4. Click **Add Key > Create new key**.
  5. Select **JSON** as the key type.
  6. Click **Create**.
  7. A JSON key file is downloaded to your computer. Save this file securely.

**Note:** The JSON key file contains credentials that allow write access to your GCS bucket. Store it securely and do not commit it to version control.



### Configure GitHub Enterprise Cloud audit log streaming to GCS

  1. Sign in to **GitHub Enterprise Cloud** as an enterprise owner.
  2. In the top-right corner, click your profile photo, then click **Enterprise settings** (or click **Enterprises** then click the enterprise you want to view).
  3. At the top of the page, click **Settings**.
  4. Under **Settings** , click **Audit log**.
  5. Under **Audit log** , click **Log streaming**.
  6. Select the **Configure stream** drop-down menu and click **Google Cloud Storage**.
  7. Provide the following configuration details: 
     * **Bucket** : Enter the name of the GCS bucket (for example, `github-audit-logs`)
     * **JSON Credentials** : Paste the entire contents of the service account JSON key file
  8. Click **Check endpoint** to verify that GitHub can connect and write to the Google Cloud Storage bucket.
  9. After you have successfully verified the endpoint, click **Save**.

**Note:** GitHub Enterprise Cloud will now continuously stream audit events as compressed JSON files to your GCS bucket in the format `YYYY/MM/HH/MM/<uuid>.json.gz`. This process is automatic and does not require additional configuration.



### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

#### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `GitHub audit logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GitHub** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://github-audit-logs/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click the bucket name (`github-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : 
       * **Storage Object Viewer** (`roles/storage.objectViewer`)
       * Grant one of the following roles depending on the **Source deletion option** selected: 
         * If **Never** is selected: **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`)
         * If **Delete transferred files** or **Delete transferred files and empty directories** is selected: **Storage Legacy Bucket Writer** (`roles/storage.legacyBucketWriter`)
  6. Click **Save**.



## Option 2: Configure ingestion using Webhook

### Create webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `GitHub webhook events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **GitHub** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` if GitHub sends multiple events per request, or leave empty for single-event payloads
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. Copy and save the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create Google Cloud API key

  * Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.



#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** drop-down, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



### Construct the webhook URL

  * Combine the Google SecOps endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

    * **Example:**
          
          https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
          




### Configure GitHub organization webhook

  1. Sign in to **GitHub** and navigate to your organization.
  2. Click **Settings**.
  3. In the left sidebar, click **Webhooks**.
  4. Click **Add webhook**.
  5. Provide the following configuration details: 
     * **Payload URL** : Paste the complete webhook URL constructed in the previous step (endpoint URL with API key and secret key appended as query parameters)
     * **Content type** : Select **application/json**
     * **Secret** : Leave empty (authentication is handled through the URL parameters)
  6. Under **Which events would you like to trigger this webhook?** : 
     1. Select **Let me select individual events**.
     2. Select the events you want to send to Google SecOps. Recommended events for security monitoring include: 
        * **Branch or tag creation**
        * **Branch or tag deletion**
        * **Collaborator add, remove, or changed**
        * **Deploy keys**
        * **Deployments**
        * **Forks**
        * **Member**
        * **Memberships**
        * **Organizations**
        * **Pull requests**
        * **Pull request reviews**
        * **Pushes**
        * **Releases**
        * **Repositories**
        * **Secret scanning alerts**
        * **Security advisories**
        * **Teams**
        * **Visibility changes**
  7. Select the **Active** checkbox to enable the webhook.
  8. Click **Add webhook**.
  9. GitHub sends a test `ping` event. Verify the webhook shows a green checkmark indicating successful delivery.

**Note:** To configure webhooks at the repository level instead of the organization level, navigate to the repository **Settings > Webhooks** and follow the same steps.



## Event types

The following table lists the event types and the conditions for the event types:

event_type | Conditions  
---|---  
`NETWORK_CONNECTION` | `[has_target] == "true" && [has_principal] == "true"`  
`PROCESS_LAUNCH` | `[has_principal] == "true" && [has_target_process] == "true"`  
`STATUS_UPDATE` | `[has_principal] == "true"`  
`USER_LOGIN` | `[raw][message] =~ "Authentication success" or [message] =~ "Authentication success" && ([has_target]== "true"` || `[has_target_user] == "true")`  
`USER_RESOURCE_CREATION` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["personal_access_token.create" ,"repository_vulnerability_alert.create"]`  
`USER_RESOURCE_DELETION` | `[has_target_resource] == "true" && [has_principal_user] == "true" && [action] in ["hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]`  
`USER_RESOURCE_DELETION` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]`  
`USER_RESOURCE_UPDATE_CONTENT` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "pull_request.merge" , "hook.events_changed"]`  
`USER_RESOURCE_UPDATE_PERMISSIONS` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["repo.update_actions_secret","protected_branch.update_pull_request_reviews_enforcement_level", "org.update_member" ,"protected_branch.update_admin_enforced" ,"protected_branch.update_required_status_checks_enforcement_level","org.integration_manager_removed" ,"repo.update_member", "repo.add_member"]`  
`USER_UNCATEGORIZED` | `[has_principal_userid] == "true"`  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`invitee` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`inviter` | `event.idm.read_only_udm.src.user.userid` | Mapped from changelog  
`pull_request.user.login` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`pull_request.user.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`sender.login` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`sender.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`sender.node_id` | `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`sender.url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`repository.custom_properties.criticality` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`host.name` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`logData.Level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`logData.Level` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`logData.Method` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`logData.IdentityName` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`logData.IPAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`logData.IdentityName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`logData.Username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`logData.HostId` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`logData.ServiceHost` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`logData.TenantId` | `event.idm.read_only_udm.metadata.product_deployment_id` | Mapped from changelog  
`logData.AuthenticationMechanism` | `event.idm.read_only_udm.extensions.auth.auth_details` | Mapped from changelog  
`logData.HttpRequestHost` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`logData.HttpRequestHost` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`logData.HttpRemotePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`logData.Command` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`logData.HttpRequestMethod` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`logData.ResponseCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`logData.Status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logData.PersistentSessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`logData.ActivityId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`logData.HttpRequestProtocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`logData.HttpRequestProtocol` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`logData.UserAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`logData.UserAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`logData.Referrer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`logData.Application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`logData.UriStem` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`logData.CUID` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`logData` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadGraphExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadGraphExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadTokenExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AadTokenExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ActivityStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AfdRefInfo` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AnonymousIdentifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationHash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Area` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthorizationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`BlobStorageExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`BlobStorageExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CPUCycles` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CPUExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CPUTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CommandHash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CommandIdentifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ConcurrencySemaphoreTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ContextId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ControllerTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CurrentAuthenticationSessionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DelayTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`E2EID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ElapsedTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExceptionMessage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExceptionType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExecutionTimeThreshold` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Feature` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`FinalSqlCommandExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HostStartTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HostType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HttpRequestTransferEncoding` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HttpResponseArrProxyTarget` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HttpResponseCacheControl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HttpResponseContentEncoding` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HttpUriQuery` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IsExceptionExpected` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Layer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LogicalReads` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Message` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`MethodInformationTimeout` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OrchestrationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ParentHostId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Path` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PendingAuthenticationSessionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PhysicalReads` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PostControllerTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PreControllerTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PreciseTimeStamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProcessName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProviderId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`QueueTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RedisExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RedisExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RelatedActivityId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ServiceBusExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ServiceBusExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlReadOnlyExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlReadOnlyExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlRetryExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SqlRetryExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`StartTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SupportsPublicAccess` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TSTUs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TableStorageExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TableStorageExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ThrottleReason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TimeToFirstPage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TraceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Tracepoint` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UniqueIdentifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Uri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UserDefined` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VSID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VssClientExecutionCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VssClientExecutionTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.email` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`invitation.created_at` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`invitation.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`invitation.invitation_teams_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`invitation.role` | `event.idm.read_only_udm.target.user.attribute.roles` | Mapped from changelog  
`invitation.inviter.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`invitation.inviter.login` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`invitation.inviter.html_url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`invitation.login` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`invitation.inviter.url` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`invitation.inviter.avatar_url` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`invitation.inviter.type` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`organization.url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.invitation_source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.team_count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.node_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.failed_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.failed_reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.avatar_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.events_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.followers_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.following_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.gists_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.gravatar_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.node_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.organizations_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.received_events_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.repos_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.site_admin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.starred_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.subscriptions_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`invitation.inviter.user_view_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commit_message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`sender.type` | `event.idm.read_only_udm.src.user.title` | Mapped from changelog  
`sha` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`target_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`avatar_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`context` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commit_node_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commit_committer_name` | `event.id.read_only_udm.additional.fields` | Mapped from changelog  
`state` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`commit_committer_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commit_committer_email` | `event.idm.read_only_udm.principal.email` | Mapped from changelog  
`commit_tree_sha` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`comment_count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`commit_url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`comments_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commit_user_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`commit_user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`principal.assetid` | `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`sender_login` | `event.idm.read_only_udm.src.user.user_display_name` | Mapped from changelog  
`sender_id` | `event.idm.read_only_udm.src.user.product_object_id` | Mapped from changelog  
`sender_assetid` | `event.idm.read_only_udm.src.asset_id` | Mapped from changelog  
`sender_url` | `event.idm.read_only_udm.src.url` | Mapped from changelog  
`alert.created_at` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.html_url` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.locations_url` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.multi_repo` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.number` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.publicly_leaked` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.push_protection_bypassed` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.secret_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.secret_type_display_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.updated_at` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.validity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`repository_selection", "user_programmatic_access_name", and "permissions_added.*` | `additional.fields` | Mapped from changelog  
`external_identity_nameid` | `principal.user.userid` | Mapped from changelog  
`actor_id` | `principal.user.userid` | Mapped from changelog  
`new_repo_permission", "user", and "actor` | `additional.fields` | Mapped from changelog  
`secret_type_display_name` | `additional.fields` | Mapped from changelog  
`user_id` | `target.user.userid` | Mapped from changelog  
`push_protection_bypass_reason` | `security_result.detection_fields` | Mapped from changelog  
`actor` | `principal.resource.attribute.labels` | Mapped from changelog  
`pull_request_url` | `target.url` | Mapped from changelog  
`pull_request_title", "pull_request_id" ,and "previous_visibility` | `additional.fields` | Mapped from changelog  
`explanation` | `additional.fields` | Mapped from changelog  
`invitee_email" and "email` | `additional.fields` | Mapped from changelog  
`required_status_checks_enforcement_level", "events_were" and "old_permission` | `additional.fields` | Mapped from changelog  
`name", "manager", "pull_request_reviews_enforcement_level", "hook_id", "events", "config_was", "key", "fingerprint", "permission", and "title` | `additional.fields` | Mapped from changelog  
`security_result.action` | `ALLOW` | Mapped from changelog  
`security_result.action` | `BLOCK` | Mapped from changelog  
`user` | `target.user.user_display_name` | Mapped from changelog  
`referrer` | `network.http.referral_url` | Mapped from changelog  
`user_session_id` | `network.session_id` | Mapped from changelog  
`ip` | `principal.ip` | Mapped from changelog  
`from` | `additional.fields` | Mapped from changelog  
`request_category` | `additional.fields` | Mapped from changelog  
`device_cookie` | `additional.fields` | Mapped from changelog  
`operation_type` | `additional.fields` | Mapped from changelog  
`category_type` | `additional.fields` | Mapped from changelog  
`note` | `additional.fields` | Mapped from changelog  
`read` | `additional.fields` | Mapped from changelog  
`pre_perform_allocation_count` | `additional.fields` | Mapped from changelog  
`backend` | `additional.fields` | Mapped from changelog  
`queue` | `additional.fields` | Mapped from changelog  
`class` | `additional.fields` | Mapped from changelog  
`success` | `additional.fields` | Mapped from changelog  
`controller_action` | `security_result.detection_fields` | Mapped from changelog  
`two_factor` | `security_result.detection_fields` | Mapped from changelog  
`user_agent` | `network.http.user_agent` | Mapped from changelog  
`request_method` | `network.http.method` | Mapped from changelog  
`application_name` | `target.application` | Mapped from changelog  
`status_code` | `network.http.response_code` | Mapped from changelog  
`url_path` | `target.url` | Mapped from changelog  
`user_id` | `target.userid` | Mapped from changelog  
`transport_protocol_name` | `network.application_protocol` | Mapped from changelog  
`raw.now` | `metadata.event_timestamp` | Mapped from changelog  
`raw.ip` | `principal.ip` | Mapped from changelog  
`raw.request_id` | `metadata.product_log_id` | Mapped from changelog  
`raw.repo` | `target.url` | Mapped from changelog  
`raw.action` | `security_result.summary` | Mapped from changelog  
`raw.protocol` | `network.application_protocol` | Mapped from changelog  
`raw.message` | `metadata.description` | Mapped from changelog  
`raw.at` | `security_result.action` | Mapped from changelog  
`raw.login` | `target.user_display_name` | Mapped from changelog  
`raw.user_id` | `target.userid` | Mapped from changelog  
`raw.failure_reason", "raw.failure_type", "raw.raw_login" and "raw.from` | `additional.fields` | Mapped from changelog  
`workflow_run.id` | `target.resource.attribute.labels` | Mapped from changelog  
`workflow_run.event` | `additional.fields` | Mapped from changelog  
`workflow_run.actor.login` | `principal.user.userid` | Mapped from changelog  
`workflow_run.head_branch` | `security_result.about.labels` | Mapped from changelog  
`workflow_run.head_sha` | `target.file.sha256` | Mapped from changelog  
`enterprise.name` | `additional.fields` | Mapped from changelog  
`workflow.name` | `security_result.about.labels` | Mapped from changelog  
`workflow_run.workflow_id` | `security_result.about.labels` | Mapped from changelog  
`external_identity_nameid` | `target.user.email_addresses` | Mapped from changelog  
`external_identity_nameid` | `target.user.userid` | Mapped from changelog  
`config.url` | `target.url` | Mapped from changelog  
Log field | UDM mapping | Remarks  
---|---|---  
`above_lock_quota` | `additional.fields` |   
`above_warn_quota` | `additional.fields` |   
`ac_ms` | `additional.fields` |   
`accept` | `additional.fields` |   
`action` | `metadata.product_event_type` | For JSON logs.  
`action` | `security_result.summary` | For syslog logs.  
`active` | `target.resource.attribute.labels` |   
`active_job_id` | `additional.fields` |   
`actor` | `principal.user.userid` |   
`actor_id` | `principal.user.attribute.labels.value` |   
`actor_ip` | `principal.ip` |   
`actor_is_agent` | `additional.fields` |   
`actor_is_bot` | `principal.user.attribute.labels` |   
`actor_location.country_code` | `principal.location.country_or_region` |   
`actor_session` | `additional.fields` |   
`additional_list` | `additional.fields` |   
`additional_string` | `additional.fields` |   
`after` | `additional.fields` |   
`alert_id` | `security_result.detection_fields` |   
`alert_number` | `security_result.detection_fields` |   
`alert_numbers` | `additional.fields` |   
`allow_deletions_enforcement_level` | `additional.fields` |   
`allow_force_pushes_enforcement_level` | `additional.fields` |   
`allow_private_repository_forking` | `additional.fields` |   
`application_name` | `target.application` |   
`aqueduct_job_id` | `additional.fields` |   
`auth_tries` | `additional.fields` |   
`babeld` | `additional.fields` |   
`banner` | `additional.fields` |   
`before` | `additional.fields` |   
`best_cipher` | `additional.fields` |   
`best_kex` | `additional.fields` |   
`best_mac` | `additional.fields` |   
`best_sigtype` | `additional.fields` |   
`Body` | `security_result.description` |   
`branch` | `target.resource.attribute.labels` |   
`branches` | `target.resource.attribute.labels` |   
`business` | `additional.fields` |   
`business_id` | `additional.fields` |   
`cactive` | `additional.fields` |   
`calling_workflow_refs` | `target.resource.attribute.labels` |   
`calling_workflow_shas` | `target.resource.attribute.labels` |   
`changes.body.from` | `additional.fields` |   
`charset` | `additional.fields` |   
`check_run.app` | `additional.fields` |   
`check_run.app.events` | `additional.fields` |   
`check_run.app.owner` | `additional.fields` |   
`check_run.check_suite.app.client_id` | `additional.fields` |   
`check_run.check_suite.app.created_at` | `additional.fields` |   
`check_run.check_suite.app.description` | `additional.fields` |   
`check_run.check_suite.app.events` | `additional.fields` |   
`check_run.check_suite.app.external_url` | `additional.fields` |   
`check_run.check_suite.app.html_url` | `additional.fields` |   
`check_run.check_suite.app.id` | `additional.fields` |   
`check_run.check_suite.app.name` | `additional.fields` |   
`check_run.check_suite.app.node_id` | `additional.fields` |   
`check_run.check_suite.app.slug` | `additional.fields` |   
`check_run.check_suite.app.updated_at` | `additional.fields` |   
`check_run.check_suite.conclusion` | `additional.fields` |   
`check_run.check_suite.id` | `additional.fields` |   
`check_run.check_suite.url` | `additional.fields` |   
`check_run.completed_at` | `additional.fields` |   
`check_run.conclusion` | `additional.fields` |   
`check_run.output` | `additional.fields` |   
`check_run.started_at` | `additional.fields` |   
`check_suite` (all its subfields) | `additional.fields` |   
`check_suite.app` (all its subfields) | `additional.fields` |   
`check_suite.app.events` | `additional.fields` |   
`check_suite.app.owner` (all its subfields) | `additional.fields` |   
`check_suite.head_commit` (all its subfields) | `additional.fields` |   
`cid` | `additional.fields` |   
`cipher` | `network.tls.cipher` |   
`client_id` | `principal.user.attribute.labels` |   
`cloning` | `additional.fields` |   
`code` | `additional.fields` |   
`CodeNamespace` | `additional.fields` |   
`comment` (all its subfields) | `additional.fields` |   
`comment.performed_via_github_app` (all its subfields) | `additional.fields` |   
`comment.performed_via_github_app.events` | `additional.fields` |   
`comment.reactions` (all its subfields) | `additional.fields` |   
`commit.author` | `principal.resource.attribute.labels` |   
`commit.commit.author.date` | `additional.fields` |   
`commit.commit.author.email` | `additional.fields` |   
`commit.commit.author.name` | `additional.fields` |   
`commit.commit.tree.url` | `additional.fields` |   
`commit.commit.verification` | `additional.fields` |   
`commit.committer` | `additional.fields` |   
`commit.parents` | `additional.fields` |   
`commit.sha` | `additional.fields` |   
`commit.url` | `additional.fields` |   
`commit_oid` | `additional.fields` |   
`committer_date` | `additional.fields` |   
`completed_at` | `vulns.vulnerabilities.scan_end_time` |   
`config.content_typt` | `target.resource.attribute.labels` |   
`config.insecure_ssl` | `target.resource.attribute.labels` |   
`config.secret` | `target.resource.attribute.labels` |   
`config.url` | `target.url` |   
`considers.site.admin` | `additional.fields` |   
`content_type` | `target.file.mime_type` |   
`cr` | `additional.fields` |   
`create_protected` | `additional.fields` |   
`created_at` | `metadata.event_timestamp` | The value is converted from UNIX milliseconds to a timestamp.  
`credential` | `detection_fields` |   
`ctotal` | `additional.fields` |   
`data._document_id` | `metadata.product_log_id` |   
`data.active_job_id` | `additional.fields` |   
`data.aqueduct_job_id` | `additional.fields` |   
`data.business` | `target.administrative_domain` |   
`data.business_id` | `additional.fields` |   
`data.cancelled_at` | `extensions.vulns.vulnerabilities.scan_end_time` | The value is converted from ISO8601 format to a timestamp.  
`data.category_type` | `security_result.category_details` |   
`data.dn` | `additional.fields` |   
`data.email` | `target.user.email_addresses` |   
`data.entry_found` | `additional.fields` |   
`data.event` | `target.resource.attribute.labels` |   
`data.events` | `security_result.about.labels.value` |   
`data.head_branch` | `target.resource.attribute.labels` |   
`data.head_sha` | `target.file.sha256` |   
`data.hook_id` | `target.resource.product_object_id` |   
`data.job` | `target.application` |   
`data.operation_type` | `additional.fields` |   
`data.started_at` | `extensions.vulns.vulnerabilities.scan_start_time` | The value is converted from ISO8601 format to a timestamp.  
`data.team` | `target.group.group_display_name` |   
`data.trigger_id` | `target.resource.attribute.labels` |   
`data.uid` | `additional.fields` |   
`data.workflow_id` | `target.resource.attribute.labels` |   
`data.workflow_run_id` | `target.resource.attribute.labels` |   
`default_new_repo_branch` | `additional.fields` |   
`default_repo_visibility` | `additional.fields` |   
`default_repository_permission` | `additional.fields` |   
`degraded` | `additional.fields` |   
`dependency_scope` | `additional.fields` |   
`deployment.environment` | `additional.fields` |   
`disable_members_can_create_repositories` | `additional.fields` |   
`disable_members_can_delete_repositories` | `additional.fields` |   
`disable_user_org_creation` | `additional.fields` |   
`disk_info` | `additional.fields` |   
`disk_py_file` | `additional.fields` |   
`dismiss_stale_reviews_on_push` | `additional.fields` |   
`dotcom_contributions` | `additional.fields` |   
`dotcom_user_license_usage_upload` | `additional.fields` |   
`duration_ms` | `additional.fields` |   
`ecosystem` | `additional.fields` |   
`enforcement_level` | `additional.fields` |   
`enterprise` | `principal.resource.attribute.labels` |   
`enterprise.name` | `additional.fields.value.string_value` |   
`environment_name` | `target.resource.attribute.labels` |   
`error` | `additional.fields` |   
`external_id` | `additional.fields` |   
`external_identity_nameid` | `target.user.email_addresses` | If the value is an email address, it is added to the `target.user.email_addresses` array.  
`external_identity_nameid` | `target.user.userid` |   
`external_identity_username` | `additional.fields` | Mapped to `additional.fields` when it is not populated in `target.user.user_display_name`.  
`external_identity_username` | `target.user.user_display_name` | Mapped when it is populated in `target.user.user_display_name`.  
`features` | `additional.fields` |   
`filtered` | `additional.fields` |   
`filtered_request_body.query` | `additional.fields` |   
`fluentbit_pod_name` | `additional.fields` |   
`fp_sha256` | `additional.fields` |   
`frontend` | `additional.fields` |   
`frontend_pid` | `intermediary.process.pid` |   
`frontend_ppid` | `intermediary.process.parent_process.pid` |   
`fs_host` | `target.hostname` |   
`fsc_ms` | `additional.fields` |   
`fully_qualified_domain_name` | `additional.fields` |   
`gh.sdk.name` | `additional.fields` |   
`gh.sdk.version` | `additional.fields` |   
`gh.timerd.timer.name` | `additional.fields` |   
`ghsa_id` | `additional.fields` |   
`git.maxobjectsize` | `additional.fields` |   
`git_dir_safe` | `target.resource.attribute.labels` |   
`github_event_after` | `target.resource.attribute.labels` |   
`github_event_before` | `target.resource.attribute.labels` |   
`github_event_compare` | `target.resource.attribute.labels` |   
`github_event_created` | `target.resource.attribute.labels` |   
`github_event_deleted` | `target.resource.attribute.labels` |   
`github_event_forced` | `target.resource.attribute.labels` |   
`github_event_head_commit_author_email` | `target.resource.attribute.labels` |   
`github_event_head_commit_author_name` | `target.resource.attribute.labels` |   
`github_event_head_commit_author_username` | `target.resource.attribute.labels` |   
`github_event_head_commit_committer_email` | `target.resource.attribute.labels` |   
`github_event_head_commit_committer_name` | `target.resource.attribute.labels` |   
`github_event_head_commit_committer_username` | `target.resource.attribute.labels` |   
`github_event_head_commit_distinct` | `target.resource.attribute.labels` |   
`github_event_head_commit_msg1` | `target.resource.attribute.labels` |   
`github_event_head_commit_timestamp` | `target.resource.attribute.labels` |   
`github_event_pusher_email` | `target.resource.attribute.labels` |   
`github_event_pusher_name` | `target.resource.attribute.labels` |   
`github_event_ref` | `target.resource.attribute.labels` |   
`github_event_repository_has_projects` | `target.resource.attributes.labels` |   
`github_event_repository_master_branch` | `target.resource.attribute.labels` |   
`github_event_repository_organization` | `target.resource.attribute.labels` |   
`github_event_repository_owner_name` | `target.resource.attribute.labels` |   
`github_event_repository_stargazers` | `target.resource.attribute.labels` |   
`github_event_workflow_job_completed_at` | `target.resource.attributes.labels` |   
`gpv` | `additional.fields` |   
`handler_code` | `additional.fields` |   
`hashed_token` | `network.session_id` |   
`head_branch` | `target.resource.attribute.labels` |   
`head_sha` | `target.file.sha256` |   
`healthy` | `additional.fields` |   
`hmac` | `additional.fields` |   
`hook_id` | `target.resource.attribute.labels` |   
`host.name` | `principal.user.attribute.labels` |   
`http_version` | `network.application_protocol_version` |   
`id` | `metadata.product_log_id` |   
`ignore_approvals_from_contributors` | `additional.fields` |   
`imode` | `additional.fields` |   
`imperfect` | `additional.fields` |   
`InstrumentationScope` | `additional.fields` |   
`integration_id` | `additional.fields` |   
`intel.flat` | `additional.fields` |   
`is_hosted_runner` | `target.resource.attribute.labels` |   
`issue` (all its subfields) | `additional.fields` |   
`issue.pull_request` (all its subfields) | `additional.fields` |   
`job_name` | `target.resource.attribute.labels.value` |   
`job_workflow_ref` | `target.resource.attribute.labels.value` |   
`job_workflow_sha` | `target.resource.attribute.labels.value` |   
`kafka_cluster` | `additional.fields` |   
`kex` | `additional.fields` |   
`keytype` | `additional.fields` |   
`kubernetes.container_image` | `principal.resource.attribute.labels` |   
`kubernetes.container_name` | `principal.resource.attribute.labels` |   
`kubernetes.host` | `principal.resource.attribute.labels` |   
`kubernetes.labels.app` | `principal.resource.attribute.labels` |   
`kubernetes.labels.chart` | `principal.resource.attribute.labels` |   
`kubernetes.labels.component` | `principal.resource.attribute.labels` |   
`kubernetes.labels.heritage` | `principal.resource.attribute.labels` |   
`kubernetes.labels.pod-template-hash` | `principal.resource.attribute.labels` |   
`kubernetes.labels.release` | `principal.resource.attribute.labels` |   
`kubernetes.labels.system` | `principal.resource.attribute.labels` |   
`kubernetes.namespace_name` | `principal.resource.attribute.labels` |   
`kubernetes.pod_ip` | `principal.ip`,   
`principal.asset.ip` |   
`kubernetes.pod_name` | `principal.resource.attribute.labels` |   
`last_state_change_at` | `additional.fields` |   
`last_state_change_reason` | `additional.fields` |   
`lat` | `principal.location.region_coordinates.latitude` |   
`ldap.debug_logging_enabled` | `additional.fields` |   
`level` | `security_result.severity` |   
`lfs_auth_scope` | `additional.fields` |   
`lfs_deploy_key_header` | `additional.fields` |   
`lfs_verify_reason` | `additional.fields` |   
`linear_history_requirement_enforcement_level` | `additional.fields` |   
`lock_allows_fetch_and_merge` | `additional.fields` |   
`lock_branch_enforcement_level` | `additional.fields` |   
`log_level` | `security_result.severity` |   
`log_source` | `additional.fields` |   
`log_source_file` | `target.file.full_path` |   
`logData.Count` | `additional.fields` |   
`logData.Metrics.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`logType` | `additional.fields` |   
`lon` | `principal.location.region_coordinates.longitude` |   
`loop` | `additional.fields` |   
`matched_policies` | `security_result.detection_fields` |   
`member` | `target.user.attribute.labels` |   
`merge_queue_enforcement_level` | `additional.fields` |   
`method` | `additional.fields` |   
`multi_repo` | `security_result.detection_fields` |   
`mysql_component` | `additional.fields` |   
`mysql_warning_code` | `additional.fields` |   
`name` | `target.resource.attribute.labels` |   
`non_integer_id` | `additional.fields` |   
`ns` | `additional.fields` |   
`number` | `additional.fields` |   
`oauth_application` | `principal.application` |   
`oauth_application_id` | `principal.resource.attribute.labels` |   
`oauth_party` | `additional.fields` |   
`offset` | `additional.fields` |   
`old_permissions` | `additional.fields` |   
`old_repo_permissions` | `additional.fields` |   
`org` | `target.administrative_domain` |   
`org_id` | `additional.fields.value.string_value` |   
`organization.url` | `additional.fields` |   
`original_user_agent` | `additional.fields` |   
`overridden_codes` | `additional.fields` |   
`owner` | `principal.user.user_display_name` |   
`owner_id` | `principal.user.userid` |   
`package` | `additional.fields` |   
`package_name` | `target.application` |   
`parent` | `additional.fields` |   
`parent_installation_id` | `additional.fields` |   
`partition` | `additional.fields` |   
`path_info` | `additional.fields` | This is the mapping when the path is already getting mapped to `target.file.full_path`.  
`path_info` | `target.file.full_path` | This is the mapping when the path isn't already getting mapped to `target.file.full_path`.  
`pgroup` | `additional.fields` |   
`pk_ms` | `additional.fields` |   
`prin_ip` | `principal.ip`,   
`principal.asset.ip` |   
`prin_port` | `principal.port` |   
`prin_usr` | `principal.user.userid` |   
`pro_pid` | `target.process.pid` |   
`probe_fail` | `additional.fields` |   
`probe_ok` | `additional.fields` |   
`programmatic_access_type` | `additional.fields.value.string_value` |   
`pubkey_creator_id` | `additional.fields` |   
`pubkey_creator_login` | `additional.fields` |   
`pubkey_fingerprint` | `additional.fields` |   
`pubkey_id` | `additional.fields` |   
`pubkey_verifier_id` | `additional.fields` |   
`pubkey_verifier_login` | `additional.fields` |   
`public_repo` | `additional.fields.value.string_value` |   
`public_repo` | `target.location.name` |   
`publicly_leaked` | `security_result.detection_fields` |   
`pull_request.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request._links.comments.href` | `additional.fields` |   
`pull_request._links.commits.href` | `additional.fields` |   
`pull_request._links.html.href` | `additional.fields` |   
`pull_request._links.issue.href` | `additional.fields` |   
`pull_request._links.review_comment.href` | `additional.fields` |   
`pull_request._links.review_comments.href` | `additional.fields` |   
`pull_request._links.self.href` | `additional.fields` |   
`pull_request._links.statuses.href` | `additional.fields` |   
`pull_request.base.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.base.repo.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.base.repo.owner.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.head.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.head.owner.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.head.repo.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.head.user.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.requested_reviewers.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.requested_teams.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`pull_request.user.` (and all its subfields except `login`) | `principal.user.attribute.labels` |   
`pull_request.user.login` | `principal.user.user_display_name` |   
`pull_request_id` | `target.resource.attribute.labels` |   
`pull_request_title` | `target.resource.attribute.labels` |   
`query_string` | `additional.fields.value.string_value` |   
`queue_duration` | `additional.fields` |   
`quotas_enabled` | `additional.fields` |   
`rate_limit` | `additional.fields` |   
`rate_limit_family` | `additional.fields` |   
`rate_limit_key` | `additional.fields` |   
`rate_limit_remaining` | `additional.fields.value.string_value` |   
`rate_limit_reset` | `additional.fields` |   
`rate_limit_used` | `additional.fields` |   
`raw.at` | `additional.fields` |   
`raw.hashed_token` | `network.session_id` |   
`raw.token_type` | `additional.fields` |   
`raw.url` | `target.url` |   
`raw.user_agent` | `network.http.user_agent`,   
`network.http.parsed_user_agent` |   
`raw_login` | `additional.fields` |   
`read_only` | `additional.fields` |   
`readonly` | `additional.fields` |   
`reasons` | `additional.fields` |   
`ref` | `target.resource.attribute.labels` |   
`replicas` | `additional.fields` |   
`repo` | `target.resource.name` |   
`repo_id` | `additional.fields.value.string_value` |   
`repo_owner_login` | `target.resource.attribute.labels` |   
`repo_owner_type` | `target.resource.attribute.labels` |   
`repo_public` | `additional.fields` |   
`repository` | `target.resource.attribute.labels` |   
`repository.archive_url` | `target.resource.attribute.labels` |   
`repository.assignees_url` | `target.resource.attribute.labels` |   
`repository.blobs_url` | `target.resource.attribute.labels` |   
`repository.branches_url` | `target.resource.attribute.labels` |   
`repository.clone_url` | `target.resource.attribute.labels` |   
`repository.collaborators_url` | `target.resource.attribute.labels` |   
`repository.comments_url` | `target.resource.attribute.labels` |   
`repository.commits_url` | `target.resource.attribute.labels` |   
`repository.compare_url` | `target.resource.attribute.labels` |   
`repository.contents_url` | `target.resource.attribute.labels` |   
`repository.contributors_url` | `target.resource.attribute.labels` |   
`repository.created_at` | `target.resource.attribute.labels` |   
`repository.custom_properties.` (and all its subfields) | `target.resource.attribute.labels` |   
`repository.deployments_url` | `target.resource.attribute.labels` |   
`repository.downloads_url` | `target.resource.attribute.labels` |   
`repository.events_url` | `target.resource.attribute.labels` |   
`repository.fork` | `target.resource.attribute.labels` |   
`repository.forks_url` | `target.resource.attribute.labels` |   
`repository.full_name` | `target.resource.attribute.labels` |   
`repository.git_commits_url` | `target.resource.attribute.labels` |   
`repository.git_refs_url` | `target.resource.attribute.labels` |   
`repository.git_tags_url` | `target.resource.attribute.labels` |   
`repository.git_url` | `target.resource.attribute.labels` |   
`repository.homepage` | `target.resource.attributes.labels` |   
`repository.hooks_url` | `target.resource.attribute.labels` |   
`repository.html_url` | `target.resource.attribute.labels` |   
`repository.id` | `target.resource.attribute.labels` |   
`repository.issue_comment_url` | `target.resource.attribute.labels` |   
`repository.issue_events_url` | `target.resource.attribute.labels` |   
`repository.issues_url` | `target.resource.attribute.labels` |   
`repository.keys_url` | `target.resource.attribute.labels` |   
`repository.labels_url` | `target.resource.attribute.labels` |   
`repository.languages_url` | `target.resource.attribute.labels` |   
`repository.license` | `target.resource.attributes.labels` |   
`repository.merges_url` | `target.resource.attribute.labels` |   
`repository.milestones_url` | `target.resource.attribute.labels` |   
`repository.mirror_url` | `target.resource.attributes.labels` |   
`repository.name` | `target.resource.attribute.labels` |   
`repository.node_id` | `target.resource.attribute.labels` |   
`repository.notifications_url` | `target.resource.attribute.labels` |   
`repository.open_issues_count` | `target.resource.attribute.labels` |   
`repository.owner.avatar_url` | `target.resource.attribute.labels` |   
`repository.owner.events_url` | `target.resource.attribute.labels` |   
`repository.owner.followers_url` | `target.resource.attribute.labels` |   
`repository.owner.following_url` | `target.resource.attribute.labels` |   
`repository.owner.gists_url` | `target.resource.attribute.labels` |   
`repository.owner.gravatar_id` | `target.resource.attribute.labels` |   
`repository.owner.html_url` | `target.resource.attribute.labels` |   
`repository.owner.id` | `target.resource.attribute.labels` |   
`repository.owner.node_id` | `target.resource.attribute.labels` |   
`repository.owner.organizations_url` | `target.resource.attribute.labels` |   
`repository.owner.received_events_url` | `target.resource.attribute.labels` |   
`repository.owner.repos_url` | `target.resource.attribute.labels` |   
`repository.owner.site_admin` | `target.resource.attribute.labels` |   
`repository.owner.starred_url` | `target.resource.attribute.labels` |   
`repository.owner.subscriptions_url` | `target.resource.attribute.labels` |   
`repository.owner.type` | `target.resource.attribute.labels` |   
`repository.owner.url` | `target.resource.attribute.labels` |   
`repository.owner.user_view_type` | `target.resource.attribute.labels` |   
`repository.private` | `target.resource.attribute.labels` |   
`repository.pulls_url` | `target.resource.attribute.labels` |   
`repository.pushed_at` | `target.resource.attribute.labels` |   
`repository.releases_url` | `target.resource.attribute.labels` |   
`repository.size` | `target.resource.attribute.labels` |   
`repository.ssh_url` | `target.resource.attribute.labels` |   
`repository.stargazers_url` | `target.resource.attribute.labels` |   
`repository.statuses_url` | `target.resource.attribute.labels` |   
`repository.subscribers_url` | `target.resource.attribute.labels` |   
`repository.subscription_url` | `target.resource.attribute.labels` |   
`repository.svn_url` | `target.resource.attribute.labels` |   
`repository.tags_url` | `target.resource.attribute.labels` |   
`repository.teams_url` | `target.resource.attribute.labels` |   
`repository.topics` | `target.resource.attributes.labels` |   
`repository.trees_url` | `target.resource.attribute.labels` |   
`repository.updated_at` | `target.resource.attribute.labels` |   
`repository.url` | `target.resource.attribute.labels` |   
`repository.visibility` | `target.resource.attribute.labels` |   
`repository_public` | `target.resource.attribute.labels` |   
`req_content_type` | `target.file.mime_type` |   
`request_access_security_header` | `security_result.detection_fields` |   
`request_auth` | `additional.fields` |   
`request_body` | `additional.fields.value.string_value` |   
`request_duration` | `additional.fields` |   
`request_host` | `principal.ip`,   
`principal.asset.ip` | When an IP address is present, the mapping is to `principal.ip` (keeping the existing mapping of `principal.hostname`).  
`request_method` | `network.http.method` | The value is converted to uppercase.  
`requested_reviewers.*` | `additional.fields` | The star (*) denotes that this includes all subfields.  
`require_code_owner_review` | `additional.fields` |   
`require_last_push_approval` | `additional.fields` |   
`required_approving_review_count` | `additional.fields` |   
`required_deployments_enforcement_level` | `additional.fields` |   
`required_review_thread_resolution_enforcement_level` | `additional.fields` |   
`rerun_type` | `additional.fields` |   
`res_type` | `target.resource.resource_subtype` |   
`response_time` | `additional.fields` |   
`review_id` | `target.resource.attributes.labels` |   
`route` | `additional.fields.value.string_value` |   
`rpc.jsonrpc.error_code` | `network.http.response_code` |   
`rpc.jsonrpc.error_message` | `security_result.summary` |   
`rule_suite_id` | `security_result.rule_id` |   
`run_attempt` | `additional.fields` |   
`run_number` | `additional.fields` |   
`runner_labels` | `target.resource.attribute.labels` |   
`runner_owner_type` | `target.resource.attribute.labels` |   
`runner_tenant_id` | `target.resource.attribute.labels` |   
`s3_tag` | `additional.fields` |   
`secret_type` | `security_result.detection_fields` |   
`secret_types` | `security_result.detection_fields` |   
`secrets_passed` | `security_result.detection_fields` |   
`sender.id` | `src.user.product_object_id` |   
`sender.login` | `src.user.user_display_name` |   
`sender.node_id` | `src.asset_id` |   
`sender.type` | `src.user.title` |   
`sender.url` | `src.url` |   
`service` | `target.resource.name` |   
`service.version` | `additional.fields` |   
`serviceName` | `target.resource.name` |   
`severity` (if high) | `security_result.severity` |   
`SeverityText` | `security_result.severity` |   
`shallow` | `additional.fields` |   
`sign_in_verification_method` | `security_result.detection_fields` |   
`signature_requirement_enforcement_level` | `additional.fields` |   
`sigtype` | `additional.fields` |   
`source` | `src.resource.name` |   
`spec` | `additional.fields` |   
`sr` | `additional.fields` |   
`ss` | `additional.fields` |   
`started_at` | `vulns.vulnerabilities.scan_start_time` |   
`stateless` | `additional.fields` |   
`status_code` | `network.http.response_code` |   
`strict_required_status_checks_policy` | `additional.fields` |   
`subject.business.id` | `target.resource.attribute.labels` |   
`subject.owner.id` | `additional.fields` |   
`subject.owning_organization.id` | `principal.group.product_object_id` |   
`subject.repository.id` | `target.resource.product_object_id` |   
`subject.repository.internal` | `target.resource.attribute.labels` |   
`subject.repository.owner.id` | `additional.fields` |   
`subject.repository.public` | `target.resource.attribute.labels` |   
`subject.repository.writable` | `target.resource.attribute.labels` |   
`subject.type` | `target.resource.attribute.labels` |   
`synthetic_status` | `additional.fields` |   
`tar_application` | `target.application` |   
`telemetry.sdk.name` | `additional.fields` |   
`tenant_id` | `target.resource.attribute.labels` |   
`tid` | `additional.fields` |   
`time` | `metadata.event_timestamp` |   
`time_duration_ms` | `additional.fields` |   
`time_zone` | `additional.fields` |   
`timestamp` | `metadata.event_timestamp` |   
`tls_version` | `network.tls.version` |   
`token_id` | `additional.fields.value.string_value` |   
`token_scopes` | `additional.fields.value.string_value` |   
`topic` | `additional.fields` |   
`total` | `additional.fields` |   
`transport_protocol` | `additional.fields` |   
`transport_protocol_name` | `network.application_protocol` | The value is converted to uppercase.  
`ts` | `metadata.event_timestamp` | When `process_type` is `github_production`.  
`TTY` | `additional.fields` |   
`twirp_method` | `additional.fields` |   
`twirp_package` | `additional.fields` |   
`twirp_service` | `additional.fields` |   
`twirp_status` | `network.http.response_code` |   
`two_factor_type` | `security_result.detection_fields` |   
`type` | `additional.fields` |   
`unavailable` | `additional.fields` |   
`updated_at` | `metadata.collected_timestamp` |   
`url_path` | `target.url` |   
`usage_metrics` | `additional.fields` |   
`user` | `target.user.userid` |   
`user.id` | `target.user.attr.labels` | When `actor.id` is present.  
`user.id` | `target.user.userid` | When `actor.id` isn't present.  
`user_agent` | `network.http.parsed_user_agent` | The value is parsed.  
`user_agent` | `network.http.user_agent` |   
`user_id` | `target.user.userid` |   
`user_operator_mode` | `additional.fields` |   
`user_programmatic_access_id` | `additional.fields` |   
`user_renaming_enabled` | `additional.fields` |   
`user_spammy` | `additional.fields` |   
`version` | `metadata.product_version` | This mapping includes JSON logs.  
`visibility` | `additional.fields` |   
`vk_ms` | `additional.fields` |   
`vulnerability_id` | `additional.fields` |   
`vulnerable_version_range_id` | `additional.fields` |   
`workflow` | `target.resource.attributes.labels` |   
`workflow.name` | `target.resource.attribute.labels` |   
`workflow_id` | `target.resource.attribute.labels` |   
`workflow_job.head_branch` | `security_result.detection_fields` |   
`workflow_job.name` | `target.resource.attributes.labels` |   
`workflow_job.workflow_name` | `security_result.detection_fields` |   
`workflow_run.actor.` (and all its subfields except for the `login` field, included in every subfield) | `principal.user.attribute.labels` |   
`workflow_run.actor.login` | `principal.user.userid` |   
`workflow_run.artifacts_url` | `target.resource.attributes.labels` |   
`workflow_run.cancel_url` | `target.resource.attributes.labels` |   
`workflow_run.check_suite_id` | `additional.fields` |   
`workflow_run.check_suite_node_id` | `additional.fields` |   
`workflow_run.check_suite_url` | `target.resource.attributes.labels` |   
`workflow_run.conclusion` | `target.resource.attribute.labels` |   
`workflow_run.created_at` | `metadata.event_timestamp` |   
`workflow_run.display_title` | `target.resource.attribute.labels` |   
`workflow_run.event` | `additional.fields.value.string_value` |   
`workflow_run.event` | `target.resource.attribute.labels` |   
`workflow_run.head_branch` | `target.resource.attribute.labels` |   
`workflow_run.head_commit` | `target.resource.attributes.labels` |   
`workflow_run.head_repository` | `additional.fields` |   
`workflow_run.head_sha` | `target.file.sha256` |   
`workflow_run.html_url` | `target.resource.attribute.labels` |   
`workflow_run.id` | `target.resource.attribute.labels.value` |   
`workflow_run.jobs_url` | `target.resource.attributes.labels` |   
`workflow_run.logs_url` | `target.resource.attributes.labels` |   
`workflow_run.name` | `target.resource.name` |   
`workflow_run.node_id` | `target.resource.product_object_id` |   
`workflow_run.path` | `target.resource.attribute.labels` |   
`workflow_run.previous_attempt_url` | `target.resource.attributes.labels` |   
`workflow_run.pull_requests` | `about.resource.attribute.labels` |   
`workflow_run.repository` | `additional.fields` |   
`workflow_run.rerun_url` | `target.resource.attributes.labels` |   
`workflow_run.run_attempt` | `target.resource.attribute.labels` |   
`workflow_run.run_number` | `target.resource.attribute.labels` |   
`workflow_run.run_started_at` | `target.resource.attribute.labels` |   
`workflow_run.status` | `security_result.description` |   
`workflow_run.triggering_actor` | `additional.fields` |   
`workflow_run.updated_at` | `metadata.collected_timestamp` |   
`workflow_run.url` | `target.url` |   
`workflow_run.workflow_id` | `security_result.about.labels.value` |   
`workflow_run.workflow_id` | `target.resource.attribute.labels` |   
`workflow_run.workflow_url` | `target.resource.attributes.labels` |   
  
## Release deltas reference

On January 8, 2026, Google SecOps released a new version of the GitHub parser, which includes significant changes.

### Log-field mapping delta

The following table lists the mapping delta for GitHub log-to-UDM fields exposed prior to January 8, 2026 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping  
---|---|---  
`action` (for JSON logs) | `metadata.product_event_type, security_result.summary,security_result.detection_fields` | `metadata.product_event_type`  
`action` (for syslog logs) | `additional.fields, security_result.summary` | `security_result.summary`  
`business` | `additional.fields, target.user.company_name` | `additional.fields`  
`business_id` | `target.resource.attribute.labels` | `additional.fields`  
`data.email` | `target.email` | `target.user.email_addresses`  
`data.event` | `security_result.about.labels` | `target.resource.attribute.labels`  
`data.head_branch` | `security_result.about.labels` | `target.resource.attribute.labels`  
`data.hook_id` | `target.resource.attribute.labels` | `target.resource.product_object_id`  
`data.team` | `target.user.group_identifiers` | `target.group.group_display_name`  
`data.trigger_id` | `security_result.about.labels` | `target.resource.attribute.labels`  
`data.workflow_id` | `security_result.about.labels` | `target.resource.attribute.labels`  
`data.workflow_run_id` | `security_result.about.labels` | `target.resource.attribute.labels`  
`hashed_token` | `additional.fields` | `network.session_id`  
`hook_id` (for JSON logs) | `additional.fields` | `target.resource.attribute.labels`  
`name` | `additional.fields` | `target.resource.attribute.labels`  
`oauth_application_id` | `additional.fields` | `principal.resource.attribute.labels`  
`pull_request_id` | `additional.fields` | `target.resource.attribute.labels`  
`pull_request_title` | `additional.fields` | `target.resource.attribute.labels`  
`repository.archive_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.assignees_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.blobs_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.branches_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.clone_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.collaborators_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.comments_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.commits_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.compare_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.contents_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.contributors_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.created_at` | `additional.fields` | `target.resource.attribute.labels`  
`repository.deployments_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.downloads_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.events_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.fork` | `additional.fields` | `target.resource.attribute.labels`  
`repository.forks_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.full_name` | `additional.fields` | `target.resource.attribute.labels`  
`repository.git_commits_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.git_refs_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.git_tags_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.git_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.hooks_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.html_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.id` | `additional` | `target.resource.attribute.labels`  
`repository.issue_comment_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.issue_events_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.issues_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.keys_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.labels_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.languages_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.merges_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.milestones_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.name` | `additional.fields` | `target.resource.attribute.labels`  
`repository.node_id` | `additional.fields` | `target.resource.attribute.labels`  
`repository.notifications_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.avatar_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.events_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.followers_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.following_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.gists_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.gravatar_id` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.html_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.id` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.node_id` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.organizations_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.received_events_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.repos_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.site_admin` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.starred_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.subscriptions_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.type` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.owner.user_view_type` | `additional.fields` | `target.resource.attribute.labels`  
`repository.private` | `additional.fields` | `target.resource.attribute.labels`  
`repository.pulls_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.pushed_at` | `additional.fields` | `target.resource.attribute.labels`  
`repository.releases_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.size` | `additional.fields` | `target.resource.attribute.labels`  
`repository.ssh_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.stargazers_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.statuses_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.subscribers_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.subscription_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.svn_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.tags_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.teams_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.trees_url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.updated_at` | `additional.fields` | `target.resource.attribute.labels`  
`repository.url` | `additional.fields` | `target.resource.attribute.labels`  
`repository.visibility` | `additional.fields` | `target.resource.attribute.labels`  
`repository_public` | `additional.fields` | `target.resource.attribute.labels`  
`res_type` | `target.resource.type` | `target.resource.resource_subtype`  
`sender.id` | `src.user.product_object_id, additional.fields` | `src.user.product_object_id`  
`sender.login` | `additional.fields, src.user.user_display_name` | `src.user.user_display_name`  
`sender.node_id` | `src.asset_id, additional.fields` | `src.asset_id`  
`sender.type` | `src.user.title, additional.fields` | `src.user.title`  
`sender.url` | `src.url, additional.fields` | `src.url`  
`workflow.name` | `security_result.about.labels` | `target.resource.attribute.labels`  
`workflow_job.head_branch` | `security_result.about.labels` | `security_result.detection_fields`  
`workflow_job.workflow_name` | `security_result.about.labels` | `security_result.detection_fields`  
`workflow_run.event` | `additional.fields` | `target.resource.attribute.labels`  
`workflow_run.head_branch` | `security_result.about.labels` | `target.resource.attribute.labels`  
`workflow_run.workflow_id` | `security_result.about.labels` | `target.resource.attribute.labels`  
  
### Event-type conditions delta

The conditions that determine Google SecOps event types were changed in the January 8, 2026 release.

**Note:** For a list of all the supported event types, see Event types.

The following table lists the event types and the current conditions (that is, the conditions were different prior to the January 8, 2026 release):

event_type | Conditions  
---|---  
`NETWORK_CONNECTION` | `[has_target] == "true" && [has_principal] == "true"`  
`STATUS_UPDATE` | `[has_principal] == "true"`  
`USER_RESOURCE_DELETION` | `[has_target_resource] == "true" && [has_principal_user] == "true" && [action] in ["hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]`  
`USER_RESOURCE_UPDATE_CONTENT` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "pull_request.merge" , "hook.events_changed"]`  
`USER_RESOURCE_UPDATE_PERMISSIONS` | `[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["repo.update_actions_secret","protected_branch.update_pull_request_reviews_enforcement_level", "org.update_member" ,"protected_branch.update_admin_enforced" ,"protected_branch.update_required_status_checks_enforcement_level","org.integration_manager_removed" ,"repo.update_member", "repo.add_member"]`  
  
### Key mapping delta

The following table lists the mapping delta for keys in raw-log fields to keys in UDM fields exposed prior to January 8, 2026 and subsequently (listed in the **Old key** and **Current key** columns respectively):

Key in raw log | Old key | Current key  
---|---|---  
`alert.secret_type_display_name` | `secret_type_display_name` | `alert_secret_type_display_name`  
`enterprise.name` | `Enterprise Name` | `enterprise_name`  
`hook_id` | `Hook Id` | `Hook_Id`  
`invitation.failed_at` | `failed_at` | `invitation_failed_at`  
`invitation.failed_reason` | `failed_reason` | `invitation_failed_reason`  
`invitation.invitation_source` | `invitation_source` | `invitation_invitation_source`  
`raw.failure_reason` | `failure_reason` | `raw_failure_reason`  
`raw.failure_type` | `failure_type` | `raw_failure_type`  
`raw.from` | `from` | `raw_from`  
`workflow_run.event` | `event` | `workflow_run_event`  
`workflow_run.head_branch` | `Head Branch` | `Head_Branch`  
`workflow_run.id` | `workflow_run_id` | `workflow_Run_id`  
`workflow_run.workflow_id` | `Workflow Id` | `Workflow_Id`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
