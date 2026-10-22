---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-security-command-center/
title: Integrate Security Command Center with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:45.377590+00:00
---

# Integrate Security Command Center with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-security-command-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Security Command Center with Google SecOps

This document explains how to integrate Security Command Center with Google Security Operations.

**Important:** In the Google SecOps platform, the Security Command Center integration is called _Google Security Command Center_.

## Before you begin

Before you configure the **Security Command Center** integration in Google SecOps, complete the following prerequisite steps:

  1. Create a custom Identity and Access Management role with the necessary permissions.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store any secrets.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity isn't available in your environment.




### Create and configure an IAM role

To create and configure a custom role for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role** to create a custom role with permissions required for the integration.

  3. Enter a **Title** , **Description** , and unique **ID**.

  4. Set the **Role Launch Stage** to `General Availability`.

  5. Add the following permissions to the created role:

     * `securitycenter.assets.list`
     * `securitycenter.findings.list`
     * `securitycenter.findings.setMute`
     * `securitycenter.findings.setState`
     * `serviceusage.services.use` (required for API usage and quota attribution)
  6. Click **Create**. 




### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**.

  3. Provide a name and description and click **Create and continue**.

  4. In the **Grant this service account access to project** step, add the custom role you created.

  5. Click **Done** to finish creating the account. The email address of this service account is used during the authentication configuration process.




### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store or rotate long-lived secrets.

#### Identify the unique instance identity

To use Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This is the final step that allows the instance to securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the integration you're configuring, and enter your service account email in the `Workload Identity Email` field.

  3. Enter a valid project ID in the `Quota Project ID` field.

  4. Click **Save > Test**. The test is expected to fail. 

  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

When authenticating with a Workload Identity, you must specify a `Quota Project ID` in the integration settings to track API usage and billing. 

To authorize this, you must grant your service account the following role on the designated quota project:

  1. In the Google Cloud console, go to **IAM & Admin > IAM** and select your project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account in the list of principals and click **edit(Edit principal)** for that account.

  3. Click **Add another role** and select **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Choose this method or the Workload Identity method to authenticate the integration. Use the JSON key method only if Workload Identity isn't available in your environment, as Workload Identity is the recommended and more secure approach. This method relies on a static, long-lived secret key file that requires manual management and rotation.

Use the following procedure to generate the JSON key file required to authenticate the integration:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key > Create new key**.

  4. Select `JSON` as the key type and click **Create**. The JSON file downloads to your computer.

  5. Copy the entire content of this file and paste it into `User's service account` during integration configuration.




## Integration parameters

The **Security Command Center** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root of the Security Command Center instance.  
`Organization ID` | Optional. The ID of the Google Cloud organization to use for scoping the Security Command Center integration queries.  
`Project ID` | Optional. The Google Cloud project ID used to scope the Security Command Center instance queries.  
`Quota Project ID` | Optional. The Google Cloud project ID used for API usage and billing purposes. This parameter is mandatory if you are authenticating using a Workload Identity.  
`User's Service Account` | Optional. The full content of the service account key JSON file. Only configure this parameter if you are authenticating using a JSON key.  
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you are authenticating using a Workload Identity. If you configure this parameter, you must also configure `Quota Project ID`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Security Command Center server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Finding Details

Use the **Get Finding Details** action to retrieve details about a finding in Security Command Center.

This action doesn't run on Google SecOps entities. 

**Important:** For SCC Enterprise customers, only enable playbooks within the **SCC Enterprise - Cloud Orchestration & Remediation** use case package. Enabling playbooks from the basic package in an SCC Enterprise environment leads to errors.

For more information, see the [SCC playbooks overview](https://docs.cloud.google.com/security-command-center/docs/playbooks-overview).

#### Action inputs

The **Get Finding Details** action requires the following parameters:

Parameter | Description  
---|---  
`Finding Name` |  Required. The full resource names of the findings to return details, in the format `organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID`. This parameter accepts multiple values as a comma-separated list.  
  
#### Action outputs

The **Get Finding Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Finding Details** action can return the following table:

Table title: **Finding Details**

Table columns:

  * **Category**
  * **State**
  * **Severity**
  * **Type**



##### JSON result

The following example shows the JSON result output received when using the **Get Finding Details** action:
    
    
    {
       {
          "finding_name": "organizations/ORGANIZATION_ID/sources/2678067631293752869/findings/hvX6WwbvFyBGqPbEs9WH9m",
          "finding": {
            "name": "organizations/ORGANIZATION_ID/sources/2678067631293752869/findings/hvX6WwbvFyBGqPbEs9WH9m",
            "parent": "organizations/ORGANIZATION_ID/sources/2678067631293752869",
            "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "state": "ACTIVE",
            "category": "Discovery: Service Account Self-Investigation",
            "sourceProperties": {
              "sourceId": {
                "projectNumber": "PROJECT_ID",
                "customerOrganizationNumber": "ORGANIZATION_ID"
              },
              "detectionCategory": {
                "technique": "discovery",
                "indicator": "audit_log",
                "ruleName": "iam_anomalous_behavior",
                "subRuleName": "service_account_gets_own_iam_policy"
              },
              "detectionPriority": "LOW",
              "affectedResources": [
                {
                  "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID"
                }
              ],
              "evidence": [
                {
                  "sourceLogId": {
                    "projectId": "PROJECT_ID",
                    "resourceContainer": "projects/PROJECT_ID",
                    "timestamp": {
                      "seconds": "1622678907",
                      "nanos": 448368000
                    },
                    "insertId": "ID"
                  }
                }
              ],
              "properties": {
                "serviceAccountGetsOwnIamPolicy": {
                  "principalEmail": "prisma-cloud-serv@PROJECT_ID.iam.gserviceaccount.com",
                  "projectId": "PROJECT_ID",
                  "callerIp": "192.0.2.41",
                  "callerUserAgent": "Redlock/GC-MDC/resource-manager/PROJECT_ID Google-API-Java-Client HTTP-Java-Client/1.34.0 (gzip),gzip(gfe)",
                  "rawUserAgent": "Redlock/GC-MDC/resource-manager/PROJECT_ID Google-API-Java-Client HTTP-Java-Client/1.34.0 (gzip),gzip(gfe)"
                }
              },
              "contextUris": {
                "mitreUri": {
                  "displayName": "Permission Groups Discovery: Cloud Groups",
                  "url": "https://attack.mitre.org/techniques/ID/003/"
                },
                "cloudLoggingQueryUri": [
                  {
                    "displayName": "Cloud Logging Query Link",
                    "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222021-06-03T00:08:27.448368Z%22%0AinsertId%3D%22ID%22%0Aresource.labels.project_id%3D%22PROJECT_ID%22?project=PROJECT_ID"
                  }
                ]
              }
            },
            "securityMarks": {
              "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
            },
            "eventTime": "2021-06-03T00:08:27.448Z",
            "createTime": "2021-06-03T00:08:31.074Z",
            "severity": "LOW",
            "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
            "mute": "UNDEFINED",
            "findingClass": "THREAT",
            "mitreAttack": {
              "primaryTactic": "DISCOVERY",
              "primaryTechniques": [
                "PERMISSION_GROUPS_DISCOVERY",
                "CLOUD_GROUPS"
              ]
            }
          },
          "resource": {
            "name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "projectName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "projectDisplayName": "PROJECT_ID",
            "parentName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
            "parentDisplayName": "example.net",
            "type": "google.cloud.resourcemanager.Project",
            "displayName": "PROJECT_ID"
          }
        }
    }
    

##### Output messages

The **Get Finding Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following findings in Security Command Center: FINDING_NAMES.` `Action wasn't able to find the following findings in Security Command Center: FINDING_NAMES. ` `None of the provided findings were found in Security Command Center.` | The action succeeded.  
`Error executing action "Get Finding Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Finding Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Asset Vulnerabilities

Use the **List Asset Vulnerabilities** action to list vulnerabilities related to entities in Security Command Center.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Asset Vulnerabilities** action requires the following parameters:

Parameter | Description  
---|---  
`Asset Resource Names` | Required. A comma-separated list of the unique identifiers (full resource names) for the assets to retrieve data about.  
`Timeframe` | Optional. The timeframe to search for the vulnerabilities or misconfigurations. The possible values are as follows:

  * `Last Week`
  * `Last Month`
  * `Last Year`
  * `All Time`

The default value is `All Time`.  
`Record Types` | Optional. The type of record to return. The possible values are as follows:

  * `Vulnerabilities + Misconfigurations`
  * `Vulnerabilities`
  * `Misconfigurations`

The default value is `Vulnerabilities + Misconfigurations`.   
`Output Type` | Optional. The type of output to return in the JSON result for every asset. The possible values are as follows:

  * `Statistics`
  * `Data`
  * `Statistics + Data`

The default value is `Statistics`.  
`Max Records To Return` | Optional. The maximum number of records to return for every record type. The default value is `100`.  
  
#### Action outputs

The **List Asset Vulnerabilities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Asset Vulnerabilities** action can return the following tables:

Table title: **ASSET_ID Vulnerabilities**

Table columns:

  * **Category**
  * **Description**
  * **Severity**
  * **Event Time**
  * **CVE**



Table title: **ASSET_ID Misconfigurations**

Table columns:

  * **Category**
  * **Description**
  * **Severity**
  * **Event Time**
  * **Recommendation**



##### JSON result

The following example shows the JSON result output received when using the **List Asset Vulnerabilities** action:
    
    
    {
       ."siemplify_asset_display_name":[1] [2]  ""
    "vulnerabilities": {
            "statistics": {
                "critical": 1,
                "high": 1,
                "medium": 1,
                "low": 1,
                "undefined": 1
            },
            "data": [
                {
                    "category": "CATEGORY"
                    "description": "DESCRIPTION"
                    "cve_id": "CVE_ID"
                    "event_time": "EVENT_TIME"
                    "related_references": "RELATED_REFERENCES"
                    "severity": "SEVERITY"
                }
            ]
        },
        "misconfigurations": {
            "statistics": {
                "critical": 1,
                "high": 1,
                "medium": 1,
                "low": 1,
                "undefined": 1
            },
            "data": [
                {
                    "category": "CATEGORY"
                    "description": "DESCRIPTION"
                    "recommendation": "RECOMMENDATION"
                    "event_time": "EVENT_TIME"
                    "severity": "SEVERITY"
                }
            ]
        },
    }
    

##### Output messages

The **List Asset Vulnerabilities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related vulnerabilities and misconfigurations to the following entities in Security Command Center: ASSET_IDS.` `No vulnerabilities and misconfigurations were found to the following entities in Security Command Center: ASSET_IDS.` `No vulnerabilities and misconfigurations were found for the provided assets in Security Command Center.` | The action succeeded.  
`Error executing action "List Asset Vulnerabilities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Asset Vulnerabilities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Security Command Center.

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

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Security Command Center server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Security Command Center server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update Finding

Use the **Update Finding** action to update an existing finding in Security Command Center.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Finding** action requires the following parameters:

Parameter | Description  
---|---  
`Finding Name` | Required. The full resource names of the findings to return details, in the format `organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID`. This parameter accepts multiple values as a comma-separated list.  
`Mute Status` | Optional. The mute status of the finding. The possible values are as follows:

  * `Mute`
  * `Unmute`

  
`State Status` | Optional. The state of the finding. The possible values are as follows:

  * `Active`
  * `Inactive`

  
  
#### Action outputs

The **Update Finding** action provides the following outputs:

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

The **Update Finding** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the following findings in Security Command Center: FINDING_NAMES ` `Action wasn't able to find the following findings in Security Command Center: FINDING_NAMES ` `None of the provided findings were found in Security Command Center.` | The action succeeded.  
`Error executing action "Update Finding". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Finding** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Security Command Center - Findings Connector

Use the **Security Command Center - Findings Connector** to retrieve information about findings from Security Command Center.

This connector supports filtering findings by category using the dynamic list.

**Note:** This connector supports proxies.

#### Connector inputs

The **Security Command Center - Findings Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype).  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`API Root` | Required. The API root of the Security Command Center instance.  
`Organization ID` | Optional. The ID of the Google Cloud organization to use  
`Project ID` | Optional. The Google Cloud project ID to use.  
`Quota Project ID` | Optional. The Google Cloud project ID to use.  
`Location ID` | Optional. The ID of the location to use. The default value is `global`.  
`User's Service Account` | Required. The full content of the service account key JSON file. Only use this parameter if you are authenticating using a JSON key.  
`Workload Identity Email` | Optional. The client email address of your service account. Only use this parameter if you are authenticating using a Workload Identity. If you configure this parameter, you must also configure `Quota Project ID`.  
`Finding Class Filter` | Optional. A comma-separated list of the types of security findings to include when ingesting data from the source. The possible values are as follows:

  * `Threat`
  * `Vulnerability`
  * `Misconfiguration`
  * `SCC_Error`
  * `Observation`
  * `Toxic Combination`
  * `Chokepoint`

If no value is provided, findings from all classes are ingested.  
`Lowest Severity To Fetch` | Optional. The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`
  * `Critical`

If a finding with an undefined severity is assigned the `Fallback Severity` level, that finding is exempt from filtering by this parameter. If no value is provided, all severity types are ingested.  
`Fallback Severity` | Optional. The severity level to assign to any ingested security finding without a defined or recognizable severity rating from the source. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`
  * `Critical`

The default value is `Medium`.  
`Max Hours Backwards` | Optional. The number of hours prior to now to retrieve findings. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The maximum value is `24`. The default value is `1`.  
`Max Findings To Fetch` | Optional. The number of findings to process in every connector iteration. The maximum value is `1000`. The default value is `100`.  
`Use dynamic list as a blacklist` | Required.If selected, the connector uses the dynamic list as a blocklist. Disabled by default.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the Security Command Center server. Disabled by default.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The proxy username to authenticate with.  
`Proxy Password` | Optional. The proxy password to authenticate with.  
`PythonProcessTime` | Required.The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
