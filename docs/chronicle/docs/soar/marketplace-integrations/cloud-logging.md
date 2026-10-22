---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-logging/
title: Integrate Logging with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:02.204907+00:00
---

# Integrate Logging with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Logging with Google SecOps

This document explains how to integrate Cloud Logging with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for Logging is called _Cloud Logging_.

## Use cases

The **Logging** integration uses Google SecOps capabilities to support the following use cases:

  * **Forensic log retrieval** : Run advanced queries to find specific security events across your Google Cloud environment during an investigation.

  * **Automated threat hunting** : Use playbooks to periodically query logs for known indicators of compromise (IoCs) or suspicious patterns.




## Before you begin

Before you configure the **Logging** integration in Google SecOps, complete the following prerequisite steps:

  1. Create a service account and grant it the necessary roles.

  2. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens through service account impersonation, so you don't need to store secrets.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity authentication isn't available in your environment.




### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name (for example, "SecOps Logging Integration") and description, and click **Create and continue**.

  4. In the **Grant this service account access to project** step, add the **Logs Viewer** (`roles/logging.viewer`) role.

  5. Click **Done**. The email address of this service account is used during configuration.




### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Using a Workload Identity is the recommended approach because it uses

short-lived, temporary access tokens using service account impersonation.

#### Identify the unique instance identity

Granting your Google SecOps instance permission to impersonate your service account is the final step to secure access.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Search for and select the **Cloud Logging** integration and enter your service account email in **Workload Identity Email**.

  3. Enter a valid project ID in **Quota Project ID**.

  4. Click **Save > Test**. The test is expected to fail. 

  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Authorizing the retrieved unique identity enables service account impersonation, letting the platform act on your behalf without static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

Authenticating with a Workload Identity requires a `Quota Project ID` to track API usage and billing. 

  1. In the Google Cloud console, go to **IAM & Admin > IAM** and select the project used for the Quota Project ID.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account and click **Edit principal**.

  3. Click **Add another role** and select **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Static, long-lived secret key files require manual management. This method should only be used if Workload Identity credentials aren't available.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** as the key type and click **Create**. 

  4. Copy the entire content of the downloaded file and paste it into `User's Service Account` during configuration.




## Integration parameters

The **Logging** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Optional. The base URL for the Cloud Logging API (for example, `https://logging.googleapis.com`).  
`User's Service Account` | Optional. The full content of the service account key JSON file. Only use this parameter if you're authenticating using a JSON key.  
`Workload Identity Email` | Optional. The client email address of your service account. Only use this parameter if you're authenticating using Workload Identity credentials.  
`Project ID` | Optional. The project ID to use in the integration. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Quota Project ID` | Optional. The project ID used for API usage and billing. This parameter is mandatory when authenticating using Workload Identity credentials.  
`Organization ID` | Optional. The organization ID used to scope queries.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Logging server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Execute Query

Use the **Execute Query** action to execute custom queries in Logging.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Execute Query** action requires the following parameters:

Parameter | Description  
---|---  
`Project ID` | _Optional_ The project ID to use in the integration. If you don't set a value for this parameter, the integration retrieves the project ID from your Google Cloud service account.  
`Organization ID` | _Optional_ The organization ID to use in the integration. If you don't set a value for this parameter, the integration retrieves the project ID from your Google Cloud service account.  
`Query` | _Required_ A query to find the logs.  
`Time Frame` | _Optional_ A period to retrieve the results from.If you select `Custom`, also configure the `Start Time` parameter.The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | _Optional_ The start time to retrieve results. This parameter is required if you selected the `Custom` option for the `Time Frame` parameter.To configure this parameter, use the ISO 8601 format.  
`End Time` | _Optional_ The end time to retrieve results. If you don't set a value for this parameter and select the `Custom` option for the `Time Frame` parameter, the action uses the current time as the end time.To configure this parameter, use the ISO 8601 format.  
`Max Results To Return` | _Optional_ The maximum number of results to return. The default value is 50.  
  
#### Action outputs

The **Execute Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Execute Query** action:
    
    
    [{
        "protoPayload": {
            "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
            "authenticationInfo": {
                "principalEmail": "system:clouddns"
            },
            "authorizationInfo": [
                {
                    "granted": true,
                    "permission": "io.k8s.coordination.v1.leases.update",
                    "resource": "coordination.k8s.io/v1/namespaces/kube-system/leases/clouddns-lock"
                }
            ],
            "methodName": "io.k8s.coordination.v1.leases.update",
            "requestMetadata": {
                "callerIp": "192.0.2.6",
                "callerSuppliedUserAgent": "clouddns-leader-election"
            },
            "resourceName": "coordination.k8s.io/v1/namespaces/kube-system/leases/clouddns-lock",
            "serviceName": "k8s.io",
            "status": {
                "code": 0
            }
        },
        "insertId": "ID",
        "resource": {
            "type": "k8s_cluster",
            "labels": {
                "cluster_name": "CLUSTER_NAME",
                "project_id": "PROJECT_ID",
                "location": "us-central1"
            }
        },
        "timestamp": "2024-09-18T09:46:38.647428Z",
        "labels": {
            "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"system:clouddns\" of ClusterRole \"system:clouddns-role\" to User \"system:clouddns\"",
            "authorization.k8s.io/decision": "allow"
        },
        "logName": "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity",
        "operation": {
            "id": "ID",
            "producer": "k8s.io",
            "first": true,
            "last": true
        },
        "receiveTimestamp": "2024-09-18T09:46:39.063264993Z"
    }]
    

##### Output messages

The **Execute Query** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Cloud Logging.` `No results were found for the provided query.` | The action succeeded.  
`Error executing action "Execute Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Logging.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Cloud Logging server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Cloud Logging server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
