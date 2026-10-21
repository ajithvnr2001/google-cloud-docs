---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/pubsub/
title: Integrate Pub/Sub with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:14:36.223302+00:00
---

# Integrate Pub/Sub with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Pub/Sub with Google SecOps

This document explains how to integrate Pub/Sub with Google Security Operations.

## Use cases

The **Pub/Sub** integration supports the following use cases:

  * **Automated alert ingestion** : Continuously retrieve security logs, alerts, and telemetry published to Pub/Sub topics to ingest them into Google SecOps as cases.

  * **Centralized security orchestration** : Consolidate security events routing through Pub/Sub from cloud and third-party systems to trigger automated response playbooks.




## Before you begin

Before you configure the **Pub/Sub** integration in Google SecOps, complete the following prerequisite steps:

  1. Create a service account.

  2. Grant the necessary Identity and Access Management roles to your service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description, and click **Done**. Note the service account's **Email address**.




### Grant IAM roles

Granting permissions lets the integration view and pull messages from your subscriptions. To assign the standard role, complete the following steps:

  1. In the Google Cloud console, go to **IAM**.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account and click **Edit principal** (edit).

  3. Click **Add another role** and select **Pub/Sub Viewer** (`roles/pubsub.viewer`).

  4. Click **Save**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach because it uses short-lived access tokens using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Pub/Sub** integration and enter your service account email in **Workload Identity Email**.

  3. Click **Save > Test**. The test is expected to fail.

  4. Click close_small next to the **Test** button and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into **New principals** and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

Authenticating with a Workload Identity requires a `Quota Project ID` to track API usage and billing. 

  1. In the Google Cloud console, go to **IAM** for the project used as the quota project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Find your service account and click **Edit principal** (edit).

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
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you're authenticating using a Workload Identity. If configured, you must also provide a `Quota Project ID` and `Service Account JSON File Content` is ignored.  
`Service Account JSON File Content` | Optional. The full content of the service account key JSON file. Configure this parameter for service account key authentication.  
`Quota Project ID` | Optional. The project ID used for API usage and billing. This parameter is required when using Workload Identity authentication. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Project ID` | Optional. The project ID to target in Pub/Sub. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Verify SSL` | Required. Validates the SSL certificate for the connection to the server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the Ping action to test the connectivity to Pub/Sub.

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
`Successfully connected to the Pub/Sub server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Pub/Sub server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Pub/Sub – Messages Connector

In Google SecOps platform, the **Pub/Sub – Messages Connector** is called _PubSub – Messages Connector_.

Use the **Pub/Sub – Messages Connector** to retrieve messages from Pub/Sub.

#### JSON severity mapping

To map the alert severity, you need to specify which field the **Pub/Sub – Messages Connector** uses to get the value for severity in the `Severity Mapping JSON` parameter. The connector response can contain value types, such as `integer`, `float`, and `string`.

The **Pub/Sub – Messages Connector** reads the `integer` and `float` values and maps them according to the Google SecOps settings. The following table shows the mapping of the `integer` values to severity in Google SecOps:

Integer value | Mapped severity  
---|---  
`100` | `Critical`  
From `80` to `100` | `High`  
From `60` to `80` | `Medium`  
From `40` to `60` | `Low`  
Less than `40` | `Informational`  
  
If the response contains the `string` value, the **Pub/Sub – Messages Connector** requires additional configuration.

Initially, the default value appears as follows:
    
    
    {
        "Default": 60
    }
    

If the values that are required for mapping are located in the `event_severity` JSON key, the values can be as follows:

  * `"Malicious"`
  * `"Benign"`
  * `"Unknown"`



To parse the `event_severity` JSON key values and ensure that the JSON object has a correct format, configure the `Severity Mapping JSON` parameter as follows:
    
    
    {
        "event_severity": {
            "Malicious": 100,
            "Unknown": 60,
            "Benign": -1
        },
        "Default": 50
    }
    

The `"Default"` value is required.

In a case when there are multiple matches for the same JSON object, the **Pub/Sub – Messages Connector** prioritizes the first JSON object key.

To work with fields that contain `integer` or `float` values, configure the key and an empty string in the `Severity Mapping JSON` parameter:
    
    
    {
      "Default":"60",
      "integer_field": "",
      "float_field": ""
    }
    

#### Connector inputs

The **Pub/Sub – Messages Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `Product Name`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `event_type`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to the default environment.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process running the current script.The default value is `60`.  
`Service Account JSON File Content` | _Optional_ The content of the service account key JSON file. You can configure this parameter or the `Workload Identity Email` parameter.To configure this parameter, provide the full content of the service account key JSON file that you downloaded when creating a service account.For the **Pub/Sub – Messages Connector** , authenticating with the service account key JSON file has priority over the Workload Identity Federation.  
`Workload Identity Email` | _Optional_ The client email address of your service account. You can configure this parameter or the `Service Account JSON File Content` parameter.To impersonate service accounts with the Workload Identity Federation, grant the [`Service Account Token Creator`](https://docs.cloud.google.com/iam/docs/service-account-permissions#%0A%20%20%20%20token-creator-role) role to your service account.  
`Project ID` | _Optional_ The project ID to use in the connector.  
`Quota Project ID` | _Optional_ The Google Cloud project ID which you use for Google Cloud APIs and billing. This parameter requires you to grant the `Service Usage Consumer` role to your service account. For more information about the IAM roles, see [Access Control with IAM](https://docs.cloud.google.com/service-usage/docs/access-control#roles). The integration attaches this parameter value to all API requests.  
`Subscription ID` | _Required_ The Pub/Sub subscription ID.  
`Case Name Template` | _Optional_ A custom case name.When you configure this parameter, the connector adds a new key called `custom_case_name` to the Google SecOps event. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]` For placeholders, the connector uses the first Google SecOps event. The connector only handles keys containing the string value. To configure this parameter, specify event fields without prefixes.  
`Alert Name Template` | _Required_ A custom alert name. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys containing the string value. If you don't provide any value or use an invalid template, the connector uses a fallback value in the following format: `CONNECTOR_NAME - Alert`. To configure this parameter, specify event fields without prefixes.  
`Rule Generator Template` | _Required_ A custom rule generator. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys containing the string value. If you don't provide any value or use an invalid template, the connector uses a fallback value in the following format: `CONNECTOR_NAME - Rule Generator`. To configure this parameter, specify event fields without prefixes.  
`Timestamp Field` | _Required_ The name of the field to define the Google SecOps alert timestamp.If the timestamp doesn't use the Unix epoch time format, define the timestamp format in the `Timestamp Format` parameter.The default value is `message_publishTime`.  
`Timestamp Format` | _Optional_ The message timestamp format.The connector requires the timestamp to correctly process the message. If the timestamp doesn't use the Unix epoch time format and you don't configure a timestamp format, the connector fails.The default value is `%Y-%m-%dT%H:%M:%S.%fZ`.  
`Severity Mapping JSON` | _Required_ The JSON object that defines how the connector extracts the severity level from the message.The default value is as follows:
    
    
        {
          "Default": "60"
        }
        

For more information about severity mapping, see JSON severity mapping.  
`Unique ID Field` | _Optional_ The name of the field to confirm that the message is unique. You can use the reserved keyword `pubsub_message_id` to extract the native Pub/Sub message ID. If you don't set a value or the field is not found, the connector generates a SHA-256 hash and uses it as an identifier for the message.  
`Max Messages To Fetch` | _Required_ The maximum number of messages to process for every connector iteration.The default value is `100`.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Selected by default.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to Pub/Sub is valid.Selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The **Pub/Sub – Messages Connector** supports proxies.

##### Connector events

The following example shows the JSON output of a Google SecOps event that the **Pub/Sub – Messages Connector** generates:
    
    
    {
       "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/soar_connector_toxic_notifications_config",
       "finding": {
           "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
           "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
           "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/global/firewalls/FIREWALL_ID",
           "state": "ACTIVE",
           "category": "OPEN_NETBIOS_PORT",
           "externalUri": "https://console.cloud.google.com/networking/firewalls/details/default-allow-rdp?project\u003dPROJECT_ID",
           "sourceProperties": {
               "Recommendation": "Restrict the firewall rules at: https://console.cloud.google.com/networking/firewalls/details/default-allow-rdp?project\u003dPROJECT_ID",
               "ExceptionInstructions": "Add the security mark \"allow_open_netbios_port\" to the asset with a value of \"true\" to prevent this finding from being activated again.",
               "Explanation": "Firewall rules that allow connections from all IP addresses on TCP ports 137-139 or UDP ports 137-139 may expose NetBIOS services to attackers.",
               "ScannerName": "FIREWALL_SCANNER",
               "ResourcePath": [
                   "projects/PROJECT_ID/",
                   "folders/FOLDER_ID/",
                   "folders/FOLDER_ID/",
                   "organizations/ORGANIZATION_ID/"
               ],
               "ExposedService": "NetBIOS",
               "OpenPorts": {
                   "TCP": [
                       137.0,
                       138.0,
                       139.0
                   ],
                   "UDP": [
                       137.0,
                       138.0,
                       139.0
                   ]
               },
               "compliance_standards": {
                   "iso": [
                       {
                           "ids": [
                               "A.13.1.1"
                           ]
                       }
                   ],
                   "pci": [
                       {
                           "ids": [
                               "1.2.1"
                           ]
                       }
                   ],
                   "nist": [
                       {
                           "ids": [
                               "SC-7"
                           ]
                       }
                   ]
               },
               "ReactivationCount": 4.0
           },
           "securityMarks": {
               "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks",
               "marks": {
                   "peter": "e2e1"
               }
           },
           "eventTime": "2024-08-30T14:44:37.973090Z",
           "createTime": "2024-06-24T07:08:54.777Z",
           "propertyDataTypes": {
               "ResourcePath": {
                   "listValues": {
                       "propertyDataTypes": [
                           {
                               "primitiveDataType": "STRING"
                           }
                       ]
                   }
               },
               "ReactivationCount": {
                   "primitiveDataType": "NUMBER"
               },
               "Explanation": {
                   "primitiveDataType": "STRING"
               },
               "ExposedService": {
                   "primitiveDataType": "STRING"
               },
               "ScannerName": {
                   "primitiveDataType": "STRING"
               }
           }
       }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
