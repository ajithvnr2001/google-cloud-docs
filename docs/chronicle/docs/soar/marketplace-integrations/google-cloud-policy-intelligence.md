---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-policy-intelligence/
title: Integrate Policy Intelligence with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:00:22.283512+00:00
---

# Integrate Policy Intelligence with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-policy-intelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Policy Intelligence with Google SecOps

This document explains how to integrate Policy Intelligence with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for Policy Intelligence is called _Google Cloud Policy Intelligence_.

## Use cases

The **Policy Intelligence** integration supports the following use cases:

  * **Identify dormant service accounts** : Automatically identify service accounts that haven't authenticated within a specific timeframe to facilitate the cleanup of unused identities and reduce the attack surface.

  * **Investigate identity compromise** : Retrieve the last authentication time for a service account during an incident investigation to determine if the account was active during a suspected breach window.

  * **Automate compliance auditing** : Compile service account authentication metadata into digestible reports to satisfy regulatory requirements for monitoring identity access and usage.




## Endpoints

The integration interacts with the single `activities:query` endpoint within the Policy Intelligence API using different parameters for different actions. The following is an example of an endpoint for the integration:
    
    
    [https://policyintelligence.googleapis.com/v1/projects/](https://policyintelligence.googleapis.com/v1/projects/)PROJECT_ID/locations/global/activityTypes/serviceAccountLastAuthentication/activities:query
    

## Before you begin

Before you configure the **Policy Intelligence** integration in Google SecOps, complete the following prerequisite steps:

  1. Create and configure a custom Identity and Access Management role.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Create and configure the IAM role

To provide the integration with the necessary permissions, create a custom role in your project:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **add Create custom role**.

  3. Provide a **Title** (for example, `SecOps Policy Intelligence Analyst`), **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Add the following permission to the role:

     * `policyanalyzer.serviceAccountLastAuthenticationActivities.query`
  6. Click **Create**.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description and click **Create and continue**.

  4. In the **Grant this service account access to project** step, assign the custom role you created.

  5. Click **Done**. Take note of the service account's **Email address**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach as it uses short-lived access tokens using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Policy Intelligence** integration and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click the close_small button next to **Test** and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

Authenticating with Workload Identity requires a `Quota Project ID` to track API usage and billing. 

  1. In the Google Cloud console, go to **IAM** for the project used as the quota project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account and click **Edit principal** (edit).

  3. Click **Add another role** and select **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Only use this method if Workload Identity authentication is unavailable.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The browser downloads the JSON file to your computer.




## Integration parameters

The **Pub/Sub** integration requires the following parameters:

Parameter | Description  
---|---  
`Service Account JSON File Content` | Optional. The full content of the service account key JSON file. Configure this parameter for service account key authentication.  
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you're authenticating using a Workload Identity. If configured, you must also provide a `Quota Project ID` and `Service Account JSON File Content` is ignored.  
`Project ID` | Optional. The project ID to target in Pub/Sub. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Quota Project ID` | Optional. The project ID used for API usage and billing. This parameter is required when using Workload Identity authentication. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Verify SSL` | Required. Validates the SSL certificate for the connection to the server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the Ping action to test connectivity to Policy Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The Ping action provides the following outputs:

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

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Cloud Policy Intelligence server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Google Cloud Policy Intelligence server!` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Service Account Activity

Use the Search Service Account Activity action to search for an activity related to service accounts in Policy Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The Search Service Account Activity action requires the following parameters:

Parameters | Description  
---|---  
`Project ID` | _Optional_ The name of the project to search for the service account activities in.If you provide no value, the action extracts the project ID from the integration configuration.  
`Service Account Resource Name` | _Required_ A comma-separated list which contains the resource names of the service accounts used to retrieve activities.  
`Max Activities To Return` | _Required_ The number of activities to return for a service account. The maximum number is 1000.By default, the action returns 50 activities.  
  
#### Action outputs

The Search Service Account Activity action provides the following outputs:

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

The following example describes the JSON result output received when using the Search Service Account Activity action:
    
    
    [
      {
        "Entity": "//iam.googleapis.com/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT@ENTITY_ID",
        "EntityResult": [
          {
            "fullResourceName": "//iam.googleapis.com/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT@ENTITY_ID",
            "activityType": "serviceAccountLastAuthentication",
            "observationPeriod": {
              "startTime": "2023-05-23T07:00:00Z",
              "endTime": "2023-08-20T07:00:00Z"
            },
            "activity": {
              "lastAuthenticatedTime": "2023-08-20T07:00:00Z",
              "serviceAccount": {
                "serviceAccountId": "SERVICE_ACCOUNT_ID",
                "projectNumber": "PROJECT_NUMBER",
                "fullResourceName": "//iam.googleapis.com/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT@ENTITY_ID"
              }
            }
          }
        ]
      }
    ]
    

##### Output messages

On a Case Wall, the Search Service Account Activity action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found activity for the following service accounts in Google Cloud Policy Intelligence: SERVICE_ACCOUNTS` `No activity was found for the following service accounts in Google Cloud Policy Intelligence: SERVICE_ACCOUNTS` `No activity was found for the provided service accounts in Google Cloud Policy Intelligence` | Action succeeded.  
`Error executing action "Search Service Account Activity". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Search Service Account Activity action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
