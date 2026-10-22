---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-identity/
title: Integrate Cloud Identity with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:00.974019+00:00
---

# Integrate Cloud Identity with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Cloud Identity with Google SecOps 

This document explains how to integrate Cloud Identity with Google Security Operations.

## Use cases

The **Cloud Identity** integration uses Google SecOps capabilities to support the following use cases:

  * **Manage access controls** : Create and update IAM configurations directly from an investigative playbook.
  * **Audit policy definitions** : List information about available policies to track access mutations.
  * **Maintain detector list attributes** : Append entities and indicators to specific detector URL lists for monitoring.



## Before you begin

Before you configure the **Cloud Identity** integration in the Google SecOps platform, verify that you have configured your environment using the following steps:

  1. Create a service account.
  2. Delegate domain-wide authority to your service account
  3. Enable the required APIs for your project.
  4. Choose and configure one of the following authentication methods: 
     * **Option 1:JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity isn't available in your environment.
     * **Option 2:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store any secrets.



### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your project.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**.

  3. Provide a name and description and click **Done** to create the account.




### Delegate domain-wide authority to your service account

  1. From your domain's Google Admin console, go to **menu Main menu > Security > Access and data control > API controls**.
  2. In the **Domain wide delegation** pane, select **Manage Domain Wide Delegation**.
  3. Click **Add new**.
  4. In the **Client ID** field, enter the client ID obtained from the Create a service account section.
  5. In the **OAuth Scopes** field, enter the following comma-delimited list of the scopes required for your application:
         
         https://www.googleapis.com/auth/cloud-platform,
         https://www.googleapis.com/auth/cloud-identity.policies,
         https://www.googleapis.com/auth/admin.directory.orgunit
         

  6. Click **Authorize**.




The service account is now authorized to access data across your domain using the specified scopes.

### Enable the required APIs for your project

  1. In the Google Cloud console, go to **APIs & Services**.

[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)

  2. Click **Enable APIs and Services**.

  3. Search for and enable the following APIs for your project:

     * **Admin SDK API** (`admin.googleapis.com`)
     * **Cloud Identity API** (`cloudidentity.googleapis.com`)



### Configure a JSON key

You can authenticate the integration using either a static JSON key file or Workload Identity Federation. To maximize your environment security, use the Workload Identity method. Use the JSON key method only if Workload Identity isn't supported in your infrastructure, as static keys require manual rotation and increase credential exposure risks.

To generate the JSON key file required to authenticate the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key**.

  4. Select **Create new key**.

  5. For the key type, select **JSON** and click **Create**. The JSON file downloads to your computer.

  6. Copy the entire content of this file and paste it into `User's Service Account JSON` during integration configuration.




#### Configure Cloud Identity permissions

Use the following procedure to define the administrative privileges the integration requires to manage organizational resources:

  1. In the Google Admin console, go to **Account > Admin Roles**.
  2. Click **Create new role**.
  3. Provide a name for the new custom role and click **Continue**.
  4. On the **Select Privileges** page, go to the **Admin API** privileges section.
  5. Under **Admin API privileges** , select the following privileges: 
     * `Organization Units`
     * `Users`
     * `Groups`
  6. Click **Continue**.
  7. To create a new custom role, click **Create Role**.



##### Assign the custom role to a user

Use the following procedure to assign the role to a user account, authorizing the integration to perform actions on your behalf:

  1. To create a new user, go to **Directory > Users** page.
  2. Add a new user that is associated with the service account.
  3. Open settings for the newly created user. The user account tab opens.
  4. Click **Admin roles and privileges**.
  5. Click edit **Edit**.
  6. Select the custom role you created.
  7. For the selected role, switch the toggle to **Assigned**.



### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, minimizing long-lived secret credential exposure risks.

#### Identify the unique instance identity

To use Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This step allows the instance to securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.
  2. Select the integration you're configuring, and enter your service account email in the `Workload Identity Email` field.
  3. Enter the email you want the integration to impersonate in the `Delegated Email` field.
  4. Click **Save > Test**. The test is expected to fail. 
  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).

**Note:** It may take a few minutes after completing this step for the test to pass.



## Integration parameters

The **Cloud Identity** integration requires the following parameters:

Parameter | Description  
---|---  
`Service Account JSON File Content` | Optional. The content of the service account key JSON file. You can configure either this parameter or **Workload Identity Email**. To use this method, paste the entire JSON string from the key file downloaded during service account creation.  
`Workload Identity Email` | Optional. The client email address of your service account. You can configure either this parameter or **Service Account JSON File Content**. To use this method for service account impersonation, you must grant the Service Account Token Creator role to your Google SecOps instance identity on your service account.  
`Delegated Email` | Required. The email address that the integration uses to perform actions. Ensure this account has the appropriate delegated permissions within your environment to execute the required integration tasks.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Cloud Identity server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Cloud Identity.

This action doesn't run on Google SecOps entities.

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
`Successfully connected to the Cloud Identity server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Cloud Identity server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Entity To Detector URL List

Use the **Add Entity To Detector URL List** action to add entities to the Cloud Identity Policy detection list.

This action runs on the following Google SecOps entities:

  * **URL**
  * **Domain**



#### Action inputs

The **Add Entity To Detector URL List** action requires the following parameters:

Parameter | Description  
---|---  
`Detector Policy ID` | Required. The unique identifier of the detector policy to update.  
`URL` | Optional. A comma-separated list of URLs to add to the detector list.  
`Domain` | Optional. A comma-separated list of domains to add to the detector list.  
  
#### Action outputs

The **Add Entity To Detector URL List** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Entity To Detector URL List** action:
    
    
    {
     "type": "ADMIN",
     "customer": "customers/<CUSTOMER_ID>",
     "policyQuery": {
       "query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))",
       "orgUnit": "orgUnits/<ORG_UNIT_ID>"
     },
     "setting": {
       "type": "settings/detector.url_list",
       "value": {
         "displayName": "test_url_list_detector",
         "description": "test_url_list_detector desc",
         "urlList": {
           "urls": [
             "[http://example.com](http://example.com)",
             "example.org",
             "bad_entity.com"
           ]
         }
       }
     }
    }
    

##### Output messages

The **Add Entity To Detector URL List** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully blocked the following URLs using Cloud Identity: ENTITY_IDENTIFIER` | The action succeeded.  
`Error executing action "Add Entity To Detector URL List". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Entity To Detector URL List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Create Policy

Use the **Create Policy** action to create a new policy entry within Cloud Identity.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Create Policy** action requires the following parameters:

Parameter | Description  
---|---  
`Policy Entry` | Required. The JSON object representing the configuration of the policy entry to add.  
  
##### Example policy configurations

The following example configurations demonstrate how to structure the `Policy Entry` parameter:

**Example 1: URL List Detector**
    
    
    {
      "type": "ADMIN",
      "customer": "customers/<CUSTOMER_ID>",
      "policyQuery": {
        "orgUnit": "orgUnits/<ORG_UNIT_ID>",
        "sortOrder": 1
      },
      "setting": {
        "type": "settings/detector.url_list",
        "value": {
          "displayName": "BlockUrlDetector",
          "description": "Blocked urls for security reasons",
          "urlList": {
            "urls": [
              "www.medium.com",
              "medium.com",
              "wikipedia.org"
            ]
          }
        }
      }
    }
    

**Example 2: DLP Rule**
    
    
    {
      "type": "ADMIN",
      "customer": "customers/<CUSTOMER_ID>",
      "policyQuery": {
        "query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))",
        "orgUnit": "orgUnits/<ORG_UNIT_ID>",
        "sortOrder": 1
      },
      "setting": {
        "type": "settings/rule.dlp",
        "value": {
          "display_name": "TestRule",
          "description": "GoogleSecOps URL Blocklist Rule. Keeps state of blocked URLs. Manual modification is not advised",
          "triggers": [
            "google.workspace.chrome.url.v1.navigation"
          ],
          "condition": {
            "contentCondition": "url.matches_url_list('policies/<DETECTOR_POLICY_ID>')"
          },
          "action": {
            "chromeAction": {
              "blockContent": {
                "actionParams": {
                  "customEndUserMessage": {
                    "unsafeHtmlMessageBody": "(EQ)🚫 BlockedAccess denied."
                  }
                }
              }
            }
          },
          "state": "ACTIVE"
        }
      }
    }
    

#### Action outputs

The **Create Policy** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Policy** action:
    
    
    {
      "type": "ADMIN",
      "customer": "customers/<CUSTOMER_ID>",
      "policyQuery": {
        "query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))",
        "orgUnit": "orgUnits/<ORG_UNIT_ID>"
      },
      "setting": {
        "type": "settings/rule.dlp",
        "value": {
          "display_name": "test_create_rule",
          "triggers": [
            "google.workspace.chrome.file.v1.download"
          ],
          "state": "ACTIVE",
          "action": {
            "chromeAction": {
              "warnUser": {}
            }
          }
        }
      }
    }
    

##### Output messages

The **Create Policy** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added a new policy in Cloud Identity.` | The action succeeded.  
`Error executing action "Create Policy". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Policy** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Policies

Use the **List Policies** action to retrieve a list of existing policies from Cloud Identity.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Policies** action requires the following parameters:

Parameter | Description  
---|---  
`Organization Unit Name` | Required. The name of the organizational unit from which to list policies.  
`Policy Type Filter` | Optional. The type of policy used to filter the list. Possible values: `Admin`, `System`, or `Both`. Default value is `Both`.  
`Settings Type Filter` | Optional. The regular expression pattern used to filter policies by their settings type. This filter is applied directly to the API request.  
`Settings Display Name Filter` | Optional. A comma-separated list of display names used to filter policy settings.  
`Max Results To Return` | Optional. The maximum number of results to return for the action run. Default value is `50`. Maximum value is `100`.  
  
#### Action outputs

The **List Policies** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Policies** action:
    
    
    [
      {
        "name": "policies/123",
        "customer": "customers/123",
        "type": "ADMIN",
        "policy_query": {
          "query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('12345'))",
          "orgUnit": "orgUnits/12345",
          "sortOrder": 1
        },
        "setting": {
          "type": "settings/rule.dlp",
          "value": {
            "display_name": "Test DLP Rule"
          }
        }
      }
    ]
    

##### Output messages

The **List Policies** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed policies based on the provided criteria in Cloud Identity.` `No policies found based on the provided criteria in Cloud Identity.` | The action succeeded.  
`Error executing action "List Policies". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Policies** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
