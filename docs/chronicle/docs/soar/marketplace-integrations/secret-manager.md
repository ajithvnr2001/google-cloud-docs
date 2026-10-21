---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/secret-manager/
title: Integrate Secret Manager with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:04.317647+00:00
---

# Integrate Secret Manager with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Secret Manager with Google SecOps 

This document explains how to integrate Secret Manager with Google Security Operations.

## Use cases

The **Secret Manager** integration uses Google SecOps capabilities to support the following use cases:

  * **Centralize credential management** : Eliminate hard-coded application credentials embedded in your Google SecOps configuration files and scripts by centrally storing, auditing, and managing them within Google Cloud.
  * **Synchronize parameters** : Automate configuration management using a background sync job to fetch entries from Google Cloud Secret Manager and update integration instances, connectors, and jobs.



## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have configured your environment using the following steps:

  1. Create a service account.
  2. Enable the required APIs for your project.
  3. Choose and configure one of the following authentication methods: 
     * **Option 1:JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity isn't available in your environment.
     * **Option 2:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store any secrets.



### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your project.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**.

  3. Provide a name and description and click **Done** to create the account.

  4. Grant the required IAM permissions to the service account depending on your chosen authentication method:

     * For service account key authentication, grant the following roles: 
       * **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`), _allows the integration to access secret payloads_.
       * **Secret Manager Viewer** (`roles/secretmanager.viewer`), *provides the `secretmanager.secrets.list` permission required for the **Ping** action to test connectivity*.
     * For Workload Identity authentication: 
       * Grant the target service account being impersonated both the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) and **Secret Manager Viewer** (`roles/secretmanager.viewer`) roles.
       * Ensure your runtime environment identity has the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) role.



### Enable the required APIs for your project

  1. In the Google Cloud console, go to **APIs & Services**.

[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)

  2. Click **Enable APIs and Services**.

  3. Search for and enable the [**Secret Manager API**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/%60secretmanager.googleapis.com%60) for your project.




### Configure a JSON key

You can authenticate the integration using either a static JSON key file or a Workload Identity. To maximize your environment security, use the Workload Identity method. Use the JSON key method only if Workload Identities aren't supported in your infrastructure, as static keys require manual rotation and increase credential exposure risks.

To generate the JSON key file required to authenticate the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key**.

  4. Select **Create new key**.

  5. For the key type, select **JSON** and click **Create**. The JSON file downloads to your computer.

  6. Copy the entire content of this file and paste it into `Service Account JSON` during integration configuration.




#### Configure Secret Manager permissions

Use the following procedure to grant the administrative privileges that the integration requires to access secret materials and validate connectivity within your Google Cloud project:

  1. In the Google Cloud console, go to **IAM & Admin > IAM**.
  2. Locate the service account you created from the principals list and click edit **Edit principal**.
  3. Click **Add another role**.
  4. In the role selection field, search for and select the following roles: 
     * [**Secret Manager Secret Accessor**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/%60roles/secretmanager.secretAccessor%60)
     * [**Secret Manager Viewer**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/%60roles/secretmanager.viewer%60).
  5. Click **Save**.

**Note:** The **Secret Manager Viewer** (`roles/secretmanager.viewer`) role provides the `secretmanager.secrets.list` permission required for the **Ping** action (connection test) to succeed. If your organization uses custom IAM roles, ensure that both `secretmanager.versions.access` and `secretmanager.secrets.list` permissions are assigned.

### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, minimizing long-lived secret credential exposure risks.

#### Identify the unique instance identity

To use Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This step allows the instance to securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the integration you're configuring, and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).

**Note:** It may take a few minutes after completing this step for the test to pass.



## Integration parameters

The **Secret Manager** integration requires the following configuration parameters:

Parameter | Description  
---|---  
`Service Account JSON` | Optional. The content of the service account key JSON file used to authenticate with Secret Manager. You can configure either this parameter or **Workload Identity Email**.  
`Project ID` | Optional. The Google Cloud Project ID where your secrets are stored. If no value is provided, the integration attempts to infer this from `Service Account JSON` if present, though explicitly specifying it is recommended.  
`Workload Identity Email` | Optional. The service account email address to impersonate when authenticating using Workload Identity (Application Default Credentials). Use this configuration instead of `Service Account JSON` when the Google SecOps platform or remote agent runs inside Google Cloud with Workload Identity enabled.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when establishing a connection to Secret Manager. Enabled by default (`True`).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to validate connectivity and verify configuration parameters against the target Secret Manager instance.

This action is primarily used for immediate connection testing from the integration configuration page in the Content Hub and does not execute on individual Google Cloud entities.

**Note:** Connection testing requires the `secretmanager.secrets.list` permission (provided by the **Secret Manager Viewer** role). If this permission is missing, the action fails.

#### Action inputs

There are no input parameters required for this action.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Secret Manager server with the provided connection parameters!` | The action succeeded and credentials are valid.  
`Failed to connect to Secret Manager! Error is ERROR_REASON` | The action failed. Check your authentication credentials, Project ID configuration, IAM permissions, or network connectivity. Verify that the service account has the `secretmanager.secrets.list` permission (such as using the **Secret Manager Viewer** role).  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
* * *

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Sync Integration Credentials Job

Use the **Secret Manager - Sync Integration Credentials Job** to systematically synchronize configuration parameters from Secret Manager entries to automatically update your platform integration instances, connectors, and background job configurations.

This background sync task operates globally and does not execute on individual entities.

#### Job behavior

The job parses a structured configuration object to query secret definitions, handling two version reference styles:

  * **Implied Notation** : Format as `projects/<project_id>/secrets/<secret_name>`. The sync task dynamically resolves and retrieves the latest active version from Secret Manager during processing.
  * **Explicit Notation** : Format as `projects/<project_id>/secrets/<secret_name>/versions/<version_id>`. The sync task retrieves that exact pinned version entry, even if its state is marked as inactive in Google Cloud.



Each targeted secret path inside Secret Manager must contain a valid JSON object string that maps parameter keys directly to their respective credential values.

##### Example Credential Mapping configuration
    
    
    {
        "integration_instances": {
            "AzureActiveDirectory_1": {
                "Client ID": "projects/154371241292/secrets/AzureActiveDirectory"
            }
        },
        "connectors": {
            "Crowdstrike - Alerts Connector": {
                "Client Secret": "projects/154371241292/secrets/CrowdstrikeConnectorSecret",
                "Client ID": "projects/154371241292/secrets/CrowdstrikeConnectorID"
            },
            "Microsoft Graph Mail Connector": {
                "Client Secret": "projects/154371241292/secrets/GraphConnectorSecret",
                "Client ID": "projects/154371241292/secrets/GraphConnectorID/versions/3"
            }
        },
        "jobs": {
            "Sync Incidents": {
                "API Root": "projects/154371241292/secrets/API_Root/versions/2"
            }
        }
    }
    

#### Job inputs

The **Sync Integration Credentials Job** requires the following configuration parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment context in which to query target configurations. Default value is `Default Environment`. For setups targeting Shared Environments, provide `*`.  
`Credential Mapping` | Required. A valid JSON string structuring the target locations where integration instances, connectors, and jobs map to their explicit Secret Manager resource coordinates.  
`Service Account JSON` | Optional. The service account key JSON content dedicated to authorizing this background sync job.  
`Project ID` | Optional. The default Google Cloud Project ID scope hosting the target resources.  
`Workload Identity Email` | Optional. The application default credentials service account email to impersonate if running inside Google Cloud infrastructures with active Workload Identity.  
`Verify SSL` | Required. Validates SSL certificate endpoints during sync tasks. Enabled by default (`True`).  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
