---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/netskope/
title: Netskope \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:31.324960+00:00
---

# Netskope  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/netskope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Netskope

This guide describes how to integrate Netskope with Google Security Operations (Google SecOps).

## Use cases

Integrating Netskope with Google SecOps can help you solve the following use cases:

  * **Phishing URL investigation and blocking:** upon receiving a phishing URL alert, use the Google SecOps capabilities to query the Netskope cloud security platform for information about the URL reputation and categorization. If URL is confirmed as malicious, Netskope can automatically block the URL across your organization network.

  * **Malware analysis and containment:** use the Google SecOps capabilities to submit a malware sample to Netskope for dynamic analysis. Based on the analysis results, Netskope can then enforce policies to quarantine infected devices or block further communication with malicious command-and-control servers.

  * **Compromised account remediation:** use the Google SecOps capabilities to identify suspicious login attempts or activities and enforce actions, such as password resets, multi-factor authentication challenges, or account suspension.

  * **Vulnerability scanning and patching:** use the Google SecOps capabilities to receive alerts about vulnerabilities detected in cloud applications.

  * **Incident response automation:** use the Google SecOps capabilities to gather contextual information about the incident, such as user activity, network traffic, and data access logs and automate incident response tasks, such as isolating affected systems, blocking malicious traffic, and notifying relevant stakeholders.

  * **Threat intelligence enrichment:** use the Google SecOps capabilities to integrate with Netskope threat intelligence feeds and enrich security alerts with additional context.




## Before you begin

Before you configure the Netskope integration in Google SecOps, you must acquire specific credentials from your Netskope tenant. This integration supports two authentication methods, depending on the API version your actions use.

For detailed guidance on locating these settings in the Netskope platform, see the [Netskope Knowledge Portal](https://docs.netskope.com/).

### REST API V1 (legacy)

This method is required for actions that use the V1 API. To use this method you must acquire an API token (also referred to as the API key). See the Netskope [REST API v1 Overview](https://docs.netskope.com/en/rest-api-v1-overview/) for instructions on generating a token.

### REST API V2 (OAuth 2.0)

This method is required for actions that exclusively use the V2 API (**List Alerts** , **List Events** , **Add Entities To URL List** , and **Deploy URL List Changes**) and for actions where the `Use V2 API` parameter is selected.

To authenticate using the V2 API, you must acquire the following credentials from your Netskope tenant (configured under **Settings > Tools > REST API v2** or through a service account under **Settings > Administration > Administrators & Roles** for tenants using RBAC v3):

  * **Client ID** : Generated when you create a new OAuth 2.0 client or service account.
  * **Client secret** : Generated with the client ID.



Refer to the Netskope [REST API V2 Overview](https://docs.netskope.com/en/rest-api-v2-overview-312207/) and [Administrators RBAC V3](https://docs.netskope.com/en/administrators-rbac-v3) documentation for instructions on setting up an OAuth 2.0 client and assigning roles.

#### Required REST API V2 endpoints and scopes

When configuring your OAuth 2.0 client or RBAC v3 service account role in Netskope, grant the minimum required scopes (permissions) for the actions you plan to run:

Action | Required REST API V2 endpoint | Required scope (privilege)  
---|---|---  
**Ping** (when using V2 API)  
**List Alerts** | `/api/v2/events/data/alert` | `Read`  
**List Events** | 

  * `/api/v2/events/data/page`
  * `/api/v2/events/data/application`
  * `/api/v2/events/data/audit`
  * `/api/v2/events/data/infrastructure`

If you don't specify the `Type` parameter in this action, grant `Read` access to all four endpoints. | `Read`  
**List Clients** (when `Use V2 API` is enabled) | `/api/v2/events/datasearch/clientstatus` | `Read`  
**List Quarantined Files** (when `Use V2 API` is enabled) | `/api/v2/casbapi/incidents/quarantine` | `Read`  
**Download File** (when `Use V2 API` is enabled) | 

  * `/api/v2/casbapi/incidents/quarantine`
  * `/api/v2/casbapi/apps/{app}/instances/{instance}/files/{file_id}/content`

| `Read`  
**Allow File** (when `Use V2 API` is enabled) | `/api/v2/casbapi/incidents/quarantine/{file_id}/restore` | `Read+Write`  
**Block File** (when `Use V2 API` is enabled) | `/api/v2/casbapi/incidents/quarantine/{file_id}/block` | `Read+Write`  
**Add Entities To URL List** | 

  * `/api/v2/policy/urllist` (`Read`)
  * `/api/v2/policy/urllist/{id}/append` (`Read+Write`)
  * `/api/v2/policy/urllist/deploy` (`Read+Write`, is required when `Deploy URL List Changes` is enabled)

| `Read+Write`  
**Deploy URL List Changes** | `/api/v2/policy/urllist/deploy` | `Read+Write`  
  
### Network settings

To configure the network settings for the integration, refer to the following table:

Function | Default port | Direction | Protocol  
---|---|---|---  
API | 443 | Outbound | HTTPS  
  
## Integrate Netskope with Google SecOps

The Netskope integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | Required. The API root of the Netskope instance.  
`Api Key` | Optional. The API token value obtained from the Netskope console used to authenticate against actions using the V1 API.  
`Client ID` | Optional. The client ID used for V2 API (OAuth 2.0) authentication. This parameter is required for actions using the V2 API.  
`Client Secret` | Optional. The client secret used for V2 API (OAuth 2.0) authentication. This parameter is required for actions using the V2 API.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Netskope server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Entities To URL List

**Important:** This action uses the Netskope V2 API. Ensure `Client ID` and `Client Secret` are configured in the integration settings.

Use the **Add Entities To URL List** action to append new URLs, domains, or IP addresses to an existing Netskope URL list.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `IP Address`
  * `URL`

#### Action inputs




The **Netskope** action requires the following parameters:

Parameter | Description  
---|---  
`URL List Name` | Required. The name of the existing Netskope URL list to update (such as `Allowed URLs`).  
`Entries` | Optional. A comma-separated list of URLs, domains, or IP addresses to add to the list. The action also automatically processes `URL`, `Domain`, and `IP Address` entities attached to the case.  
`Deploy URL List Changes` | Optional. If selected, the action triggers a global deployment of all pending changes across every URL list in the tenant (not just the list being updated).  
  
#### Action outputs

The **Netskope** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Netskope** action:
    
    
    {
      "added_entities": [
        "https://aistudio.google.com/prompts",
        "https://docs.google.com/"
      ],
      "failed_entities": [
        "not_real_url",
        10500
      ],
      "url_list_name": "Allowed URL List",
      "modify_by": "SOAR_API2",
      "modify_time": "2026-02-26T15:28:07.000Z",
      "pending": 1
    }
    

##### Output messages

The **Netskope** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following entities to the URL_LIST_NAME list in Netskope: ADDED_ENTITIES. Changes are pending deployment.` `Action wasn't able to add the following entities to the URL_LIST_NAME list in Netskope: ENTITIES.` `None of the provided entities were added to the URL List URL_LIST_NAME in Netskope.` | The action succeeded.  
`Error executing action. Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Netskope** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Allow File

Use the **Allow File** action to allow a quarantined file.

This action runs on all Google SecOps entities.

#### Action inputs

The **Allow File** action requires the following parameters:

Parameter | Description  
---|---  
`File ID` | _Required_ The ID of the file to allow.  
`Quarantine Profile ID` | _Optional_ The ID of the quarantine profile that is associated with the file. **Note:** This parameter is mandatory for V1 API.   
`Use V2 API` | _Optional_ If selected, the action uses the Netskope V2 API endpoint instead of V1. This requires valid V2 API credentials. This parameter requires OAuth 2.0 support. Ensure a valid `Client ID` and `Client Secret` are configured in the integration settings.  
  
#### Action outputs

The **Allow File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Allow File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Block File

Use the **Block File** action to block a quarantined file.

This action runs on all Google SecOps entities.

#### Action inputs

The **Block File** action requires the following parameters:

Parameter | Description  
---|---  
`File ID` | _Required_ The ID of the file to block in Netskope.  
`Quarantine Profile ID` | _Optional_ The ID of the quarantine profile that is associated with the file. **Note:** This parameter is mandatory for V1 API.   
`Use V2 API` | _Optional_ If selected, the action uses the Netskope V2 API endpoint instead of V1. This requires valid V2 API credentials. This parameter requires OAuth 2.0 support. Ensure a valid `Client ID` and `Client Secret` are configured in the integration settings.  
  
#### Action outputs

The **Block File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Block File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Deploy URL List Changes

**Important:** This action uses the Netskope V2 API. Ensure `Client ID` and `Client Secret` are configured in the integration settings.

Use the **Deploy URL List Changes** action to push pending configurations to the active policy engine, ensuring that any staged updates are applied and enforced for URL Lists.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Deploy URL List Changes** action provides the following outputs:

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

The **Deploy URL List Changes** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deployed pending Netskope policy changes.` | The action succeeded.  
`Error executing action. Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Deploy URL List Changes** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Download File

Use the **Download File** action to download a quarantined file.

This action runs on the Google SecOps `IP Address` entity.

#### Action inputs

The **Download File** action requires the following parameters:

Parameter | Description  
---|---  
`File ID` | _Required_ The ID of the file to download from quarantine.  
`Quarantine Profile ID` | _Optional_ The ID of the quarantine profile that is associated with the file. **Note:** This parameter is mandatory for V1 API.   
`Use V2 API` | _Optional_ If selected, the action uses the Netskope V2 API endpoint instead of V1. This requires valid V2 API credentials. Enabling this parameter introduces the following requirements and changes:

  * **Authentication** : Requires OAuth 2.0 support. Ensure a valid `Client ID` and `Client Secret` are configured in the integration settings.
  * **Storage logic** : Enabling this parameter switches the source from **Classic Storage** to **NextGen Storage**.

  
  
#### Action outputs

The **Download File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Download File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Alerts

**Important:** This action uses the Netskope V2 API. Make sure valid `Client ID` and `Client Secret` credentials are configured in the integration settings.

Use the **List Alerts** action to list alerts.

This action runs on all Google SecOps entities.

#### Action inputs

The **List Alerts** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | _Optional_ A query to filter the cloud application events in the alerts database.  
`Type` | _Optional_ A type of alerts to filter by.The possible values are as follows:

  * `Anomaly`
  * `Compromised Credential`
  * `Policy`
  * `Legal Hold`
  * `Malsite`
  * `Malware`
  * `DLP`
  * `Watchlist`
  * `Quarantine`
  * `Remediation`

  
`Time Period` | _Optional_ The time period in milliseconds prior to now to search for alerts.The possible values are `3600`, `86400`, `604800`, and `2592000`.  
`Start Time` | _Optional_ A start time to filter alerts with timestamps greater than the specified Unix epoch time.Use this parameter only if you didn't set the `Time Period` parameter.  
`End Time` | _Optional_ An end time to filter alerts with timestamps less than the specified Unix epoch time.Use this parameter only if you didn't set the `Time Period` parameter.  
`Is Acknowledged` | _Optional_ If selected, the integration filters for acknowledged alerts.Not selected by default.  
`Limit` | _Optional_ The number of the results to return. The default value is `100`.  
  
#### Action outputs

The **List Alerts** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Alerts** action:
    
    
    [
        {
            "dstip": "192.0.2.1",
            "app": "Amazon Web Services",
            "profile_id": "ID",
            "device": "iPad",
            "shared_credential_user": "example@example.com",
            "app_session_id": 2961859388,
            "dst_location": "Ashburn",
            "dst_region": "Virginia",
            "policy": "Copy prohibited",
            "page_id": 380765822,
            "object_type": "File",
            "dst_latitude": 39.0481,
            "timestamp": 1548603047,
            "src_region": "California",
            "from_user": "user@example.com",
            "src_location": "San Luis Obispo",
            "traffic_type": "CloudApp",
            "appcategory": "IaaS/PaaS",
            "src_latitude": 35.2635,
            "count": 2,
            "type": "anomaly",
            "risk_level_id": 2,
            "activity": "Upload",
            "userip": "203.0.113.1",
            "src_longitude": -120.6509,
            "browser": "Safari",
            "alert_type": "anomaly",
            "event_type": "user_shared_credentials",
            "_insertion_epoch_timestamp": 1548601562,
            "site": "Amazon Web Services",
            "id": 3561,
            "category": "IaaS/PaaS",
            "orig_ty": "nspolicy",
            "dst_country": "US",
            "src_zipcode": "93401",
            "cci": 94,
            "ur_normalized": "user@example.com",
            "object": "quarterly_report.pdf",
            "organization_unit": "",
            "acked": "false",
            "dst_longitude": -77.4728,
            "alert": "yes",
            "user": "user@example.com",
            "userkey": "user@example.com",
            "srcip": "7198.51.100.1",
            "org": "example.com",
            "src_country": "US",
            "bin_timestamp": 1548633600,
            "dst_zipcode": "20149",
            "url": "http://aws.amazon.com/",
            "sv": "unknown",
            "ccl": "excellent",
            "alert_name": "user_shared_credentials",
            "risk_level": "high",
            "_mladc": ["ur"],
            "threshold_time": 86400,
            "_id": "cadee4a8488b3e139b084134",
            "os": "iOS 6"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **List Alerts** action:

Script result name | Value  
---|---  
`alerts` | `ALERT_LIST`  
  
### List Clients

Use the **List Clients** action to list clients.

This action runs on all Google SecOps entities.

#### Action inputs

The **List Clients** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | _Optional_ Filters the clients retrieved from the database.  
`Limit` | _Optional_ Limits the number of clients returned by the action. The default value is `25`.  
`Use V2 API` | _Optional_ If selected, the action uses the Netskope V2 API endpoint instead of V1. This requires valid V2 API credentials. This parameter requires OAuth 2.0 support. Ensure a valid `Client ID` and `Client Secret` are configured in the integration settings.  
  
#### Action outputs

The **List Clients** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **List Clients** action:
    
    
    [
           {
             "client_install_time": 1532040251,
             "users":
            [
                {
                    "heartbeat_status_since": 1532040385,
                    "user_added_time": 1532040167,
                    "last_event":
                    {
                        "status": "Enabled",
                        "timestamp": 1548578307,
                        "event": "Tunnel Up",
                        "actor": "System"
                    },
                    "device_classification_status": "Not Configured",
                    "username": "user@example.com",
                    "user_source": "Manual",
                    "userkey": "K00fuSXl8yMIqgdg",
                    "_id": "ID",
                    "heartbeat_status": "Active"
                }],
            "last_event":
            {
                "status": "Enabled",
                "timestamp": 1548578307,
                "event": "Tunnel Up",
                "actor": "System"
            },
            "host_info":
            {
                "device_model": "VMware Virtual Platform",
                "os": "Windows",
                "hostname": "HOSTNAME",
                "device_make": "VMware, Inc.",
                "os_version": "10.0"
            },
            "client_version": "1.1.1.1",
            "_id": "ID",
            "device_id": "DEVICE_ID"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **List Clients** action:

Script result name | Value  
---|---  
`clients` | `CLIENT_LIST`  
  
### List Events

**Important:** This action uses the Netskope V2 API. Make sure valid `Client ID` and `Client Secret` credentials are configured in the integration settings.

Use the **List Events** action to list events.

This action runs on all Google SecOps entities.

#### Action inputs

The **List Events** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | _Optional_ A query to filter the cloud application events in the events database.  
`Type` | _Optional_ A type of alerts to filter by.The possible values are as follows:

  * `page`
  * `application`
  * `audit`
  * `infrastructure`

  
`Time Period` | _Optional_ The time period in milliseconds prior to now to search for events.The possible values are as follows: `3600`, `86400`, `604800`, and `2592000`.  
`Start Time` | _Optional_ A start time to filter events with timestamps greater than the specified Unix epoch time.Use this parameter only if you didn't set the `Time Period` parameter.  
`End Time` | _Optional_ An end time to filter events with timestamps less than the specified Unix epoch time.Use this parameter only if you didn't set the `Time Period` parameter.  
`Limit` | _Optional_ The number of the results to return. The default value is `100`.  
  
#### Action outputs

The **List Events** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **List Events** action:
    
    
        {
            "dstip": "192.0.2.64",
            "browser_session_id": 1066949788113471080,
            "srcip": "198.51.100.36",
            "app_session_id": 4502249472406092569,
            "os_version": "WindowsServer2016",
            "dst_region": "Virginia",
            "numbytes": 37480,
            "req_cnt": 18,
            "server_bytes": 8994,
            "page_id": 0,
            "page_duration": 867,
            "page_endtime": 1548577530,
            "dst_latitude": 39.0481,
            "timestamp": 1548576663,
            "src_region": "Oregon",
            "src_location": "Boardman",
            "ur_normalized": "user@example.com",
            "appcategory": "",
            "src_latitude": 45.8491,
            "count": 1,
            "bypass_traffic": "no",
            "type": "page",
            "userip": "203.0.113.253",
            "src_longitude": -119.7143,
            "page": "WebBackground",
            "browser": "",
            "domain": "WebBackground",
            "dst_location": "Ashburn",
            "_insertion_epoch_timestamp": 1548577621,
            "site": "WebBackground",
            "access_method": "Client",
            "browser_version": "",
            "category": "",
            "client_bytes": 28486,
            "user_generated": "no",
            "hostname": "IP-C0A84AC",
            "dst_country": "US",
            "resp_cnt": 18,
            "src_zipcode": "97818",
            "traffic_type": "Web",
            "http_transaction_count": 18,
            "organization_unit": "example.com/Users",
            "page_starttime": 1548576663,
            "dst_longitude": -77.4728,
            "user": "user@example.com",
            "userkey": "user@example.com",
            "device": "WindowsDevice",
            "src_country": "US",
            "dst_zipcode": "20149",
            "url": "WebBackground",
            "sv": "",
            "ccl": "unknown",
            "useragent": "RestSharp/192.0.2.0",
            "_id": "ID",
            "os": "WindowsServer2016"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **List Events** action:

Script result name | Value  
---|---  
`events` | `EVENT_LIST`  
  
### List Quarantined Files

Use the **List Quarantined Files** action to list quarantined files.

This action runs on all Google SecOps entities.

#### Action inputs

The **List Quarantined Files** action requires the following parameters:

Parameter | Description  
---|---  
`Start Time` | _Optional_ A start time to restrict events with the timestamps greater than the value of this parameter in the Unix format.  
`End Time` | _Optional_ An end time to restrict events with the timestamps less than the value of this parameter in the Unix format.  
`Use V2 API` | _Optional_ If selected, the action uses the Netskope V2 API endpoint instead of V1. This requires valid V2 API credentials. This parameter requires OAuth 2.0 support. Ensure a valid `Client ID` and `Client Secret` are configured in the integration settings.  
  
#### Action outputs

The **List Quarantined Files** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **List Quarantined Files** action:

Script result name | Value  
---|---  
`files` | `FILE_LIST`  
  
### Ping

Use the **Ping** action to test the connectivity to Netskope.

This action runs on all Google SecOps entities.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
