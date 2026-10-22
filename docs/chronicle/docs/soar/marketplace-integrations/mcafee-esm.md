---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm/
title: McAfee ESM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:57.956237+00:00
---

# McAfee ESM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee ESM

This document provides guidance on how to integrate McAfee ESM with Google SecOps.

## Integration use cases

Ingest alarms or correlations into Google Security Operations
    The integration allows you to ingest information from McAfee ESM into Google SecOps. Particularly, to ingest alarms and correlations that later can be triaged within the SOAR platform. This can be achieved with the McAfee ESM Connector for alarm ingestion and McAfee ESM Correlations Connector for correlation ingestion.
Perform drill down to get more context about the Security Incident
    The integration supports multiple actions that allows you to execute custom queries (Get Similar Events, Send Advanced Query, Send Query To ESM, Send Entity Query To ESM) and fetch events information. There is also the [Get Similar Events](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#get-similar-events) action which queries events related to the IP addresses, Hostnames and Users in the Google SecOps alert.
Keep track of IOCs with watchlists
    The integration supports adding and removing items from watchlists. This allows you to constantly update a watchlist with suspicious IP Addresses or Hashes.

## Network

API access from Google SecOps to McAfee ESM: Allow traffic over port 443 (HTTPS) (or as configured in your environment).

## Session Management

McAfee ESM has a global parameter that limits the number of sessions per user. In Google SecOps, there is a full mechanism for session management, so that the integration uses the same session across the whole integration. Session values are stored enсrypted in the `McAfee_ESM_Action_Sessions_*.json` and `McAffee_ESM_Connector_Sessions_*.json` DB entry.

Recommendations:

  * Have one user for actions and one user for connectors.
  * At least two sessions should be available per user.



These recommendations are needed for the integration to be stable.

## Integration compatibility

Product name | Version | Deployment | Notes  
---|---|---|---  
McAfee ESM | 11.1-11.5 | On-premises | The integration was tested with the 11.1-11.5 product versions and the API that is used in the integration wasn't modified. If the API wasn't updated in the newer versions, the integration will still work.  
  
## Configure McAfeeESM integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration configuration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
API Root | Sring | https://{ip}/rs/ | Yes | API root for the instance.  
Username | String | N/A | Yes | Username of the instance.  
Password | Password | N/A | Yes | Password for the instance.  
Product Version | String | 11.5 | Yes | Product version. Possible values: 11.1-11.5  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the McAfee ESM server is valid.  
  
## Actions

### Add Values to Watchlist

#### Action description

Add values to a watchlist in McAfee ESM.

**Note:** McAfee ESM will allow values of the invalid type to be passed, for example, API will not raise error adding hash to the IP watchlist. Pay attention to the input.

#### Action usage

Use this action to update the watchlist with new values. For example, if you have a watchlist for malicious hashes, you can use this action to keep the watchlist up-to-date.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Watchlist Name | String | N/A | Yes | Specify the name of the watchlist that needs to be updated.  
Values to Add | CSV | N/A | Yes | Specify a comma-separated list of values that need to be added to a watchlist.  
  
#### Action entity scope

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success=true):_ "Successfully added value to the watchlist." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials or no connection to the server is reported:_ "Error executing action "Add Values To Watchlist". Reason: {0}".format(error.Stacktrace) _If errors are reported in the response:_ "Error executing action "Add Values To Watchlist". Reason: {message}. | General  
  
### Get Similar Events

#### Action description

Get events related to the entities in McAfee ESM. Supported entities: Hostname, IP Address, User.

**Note:** The action is running as async, adjust the script timeout value in Google SecOps IDE for action as needed.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Hours Back | String | 1 | Yes | Specify how many hours backwards to search.  
IPS ID | String | 144115188075855872/8 | No | Specify the IP SID for the search.  
Result Limit | String | 50 | No | Specify the number of results to return. The maximum parameter value: 200 per entity.  
  
#### Action entity scope

This action runs on the following entities:

  * IP Address
  * Hostname
  * User



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult":
            [{
                "Alert.DstPort": "0",
                "Rule.msg": "User Logon",
                "Alert.IPSIDAlertID": "144115188075855872|383521",
                "Action.Name": "success",
                "Alert.SrcIP": "1.1.1.1",
                "Alert.LastTime": "05/28/2019 14:18:10",
                "Alert.Protocol": "n/a",
                "Alert.SrcPort": "0",
                "Alert.DstIP": "1.1.1.1"
            }, {
                "Alert.DstPort": "0",
                "Rule.msg": "User Logon",
                "Alert.IPSIDAlertID": "144115188075855872|383519",
                "Action.Name": "success",
                "Alert.SrcIP": "1.1.1.1",
                "Alert.LastTime": "05/28/2019 14:16:16",
                "Alert.Protocol": "n/a",
                "Alert.SrcPort": "0",
                "Alert.DstIP": "1.1.1.1"
            }],
            "Entity": "1.1.1.1"
        }
    ]
    

##### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
Alert.DstPort | Returns if it exists in JSON result  
Rule.msg | Returns if it exists in JSON result  
Alert.IPSIDAlertID | Returns if it exists in JSON result  
Alert.SrcIP | Returns if it exists in JSON result  
Alert.LastTime | Returns if it exists in JSON result  
Alert.Protocol | Returns if it exists in JSON result  
Alert.SrcPort | Returns if it exists in JSON result  
Alert.DstIP | Returns if it exists in JSON result  
  
##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported for one entity (is_success=true):_ "Successfully retrieved events for the following entities in McAfee ESM: {entities}" _If there is no data for one entity (is_success=true):_ "Action wasn't able to retrieve events for the following entities in McAfee ESM: {entities}." _If there is no data for all entities (is_success=false):_ "No events were found for the provided entities in McAfee ESM." _Asynchronous message:_ "Waiting for the query to finish for {pending entities}." **The action should fail and stop a playbook execution:** _If a critical error is reported:_ "Error executing action "Get Similar Events". Reason: {0}".format(error.Stacktrace) _If the action ran int a timeout:_ "Error executing action "Get Similar Events". Reason: action initiated the query but ran into a timeout during data retrieval. Please increase the timeout in the IDE and try again." | General  
Case Wall Table | All fields from the response. | Entity  
  
### Ping

#### Action description

Test connectivity to McAfee ESM with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Action configuration parameters

This action doesn't have mandatory input parameters.

#### Action entity scope

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the McAfee ESM server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the McAfee ESM server! Error is {0}".format(exception.stacktrace) | General  
  
### Remove Values From Watchlist

#### Action description

Remove values from a watchlist in McAfee ESM.

#### Action usage

Use this action to remove certain values from the watchlist. For example, if you have a watchlist for malicious hashes and you discovered that one of the hashes is benign, you can remove it from the watchlist.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Watchlist Name | String | N/A | Yes | Specify the name of the watchlist that needs to be updated.  
Values to Remove | CSV | N/A | Yes | Specify a comma-separated list of values that need to be removed from a watchlist.  
  
#### Action entity scope

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    N/A
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success=true):_ "Successfully added value to the watchlist." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials or no connection to the server is reported: "Error executing action "Remove Values From Watchlist". Reason: {0}".format(error.Stacktrace)_ _If errors are reported in the response:_ "Error executing action "Remove Values From Watchlist". Reason: {message}." | General  
  
### Send Advanced Query to ESM

#### Action description

Send an advanced query to ESM.

**Note:** The action is running as async, adjust the script timeout value in Google SecOps IDE for action as needed.

#### Action usage

This is an advanced action that gives you the full flexibility to execute any query in McAfee ESM. This action takes the full query payload as input. The action returns a maximum of 200 records regardless of what is provided in the payload.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Query Payload | String | N/A | Yes | Specify the JSON object that would need to be executed. The action returns a maximum of 200 results.  
  
##### Create a query payload

To create a query payload, complete the following steps:

  1. Log in to the **McAfee ESM UI** and open **Developer Tools** in your browser.
  2. Go to the **Network** tab.
  3. Click **Add Tab** and add a new view.
  4. Click **Add Widget**.
  5. In the **Widget Configuration** dialog, enter the widget title and select the query that you want to execute.

![Widget Configuration dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-advanced-query-widget-configuration.png)

  6. In **Developer Tools** , you will see the `runningQuery` API request.

  7. Go to the **Payload** tab and click **View Source**.

  8. Copy the payload and paste it into the **Query Payload** parameter field.

![Example payload value](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-advanced-query-payload.png)




#### Action entity scope

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "Rule.msg": "* Latest Kubernetes 1.18 beta is now available for your laptop, NUC, cloud",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Starting Message of the Day...",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Started Message of the Day.",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "https://xxxxxxxx.run/",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "* Multipass 1.1 adds proxy support for developers behind enterprise",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "sudo snap install microk8s --channel=1.18/beta --classic",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Starting Daily apt upgrade and clean activities...",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Started Daily apt upgrade and clean activities.",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "firewalls. Rapid prototyping for cloud operations just got easier.",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "instance or Raspberry Pi, with automatic updates to the final GA release.",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Data Center : Telmetry Posting",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Send Password Expiry Notification",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Data Center: Telemetry Notifier to Collect Data",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Update successful",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Update successful",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "8198-software protection platform service",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "1003-software protection platform service",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "The Time Provider NtpClient is Currently Receiving Valid Time Data",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Time service now synchronizing system time",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "1",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "autorefresh.go:397: auto-refresh: all snaps are up-to-date",
            "COUNT(*)": "2",
            "SUM(Alert.EventCount)": "2",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "storehelpers.go:436: cannot refresh: snap has no updates available: \\\"amazon-ssm-agent\\\", \\\"core\\\"",
            "COUNT(*)": "2",
            "SUM(Alert.EventCount)": "2",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "The Windows Security Center Service could not start Windows Defender",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "2",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "A user's local group membership was enumerated",
            "COUNT(*)": "2",
            "SUM(Alert.EventCount)": "2","Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "The System Time Has Changed",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "3",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "The system time was changed.",
            "COUNT(*)": "1",
            "SUM(Alert.EventCount)": "3",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "User Logon",
            "COUNT(*)": "4",
            "SUM(Alert.EventCount)": "4",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "16384-software protection platform service",
            "COUNT(*)": "7",
            "SUM(Alert.EventCount)": "7",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "16394-software protection platform service",
            "COUNT(*)": "7",
            "SUM(Alert.EventCount)": "7",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Linux crond Session opened",
            "COUNT(*)": "10",
            "SUM(Alert.EventCount)": "10",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Linux crond Session closed",
            "COUNT(*)": "10",
            "SUM(Alert.EventCount)": "10",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Linux cron Scheduled Command Executed",
            "COUNT(*)": "10",
            "SUM(Alert.EventCount)": "10",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "DHCPACK of xx.x.x.xxx from xx.x.x.x",
            "COUNT(*)": "19",
            "SUM(Alert.EventCount)": "19",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Linux dhclient Renewal",
            "COUNT(*)": "19",
            "SUM(Alert.EventCount)": "19",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Linux DHCP Client Request",
            "COUNT(*)": "19",
            "SUM(Alert.EventCount)": "19",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Special Privileges Assigned",
            "COUNT(*)": "28",
            "SUM(Alert.EventCount)": "28",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Special privileges assigned to new logon.",
            "COUNT(*)": "21",
            "SUM(Alert.EventCount)": "30",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "An account was successfully logged on",
            "COUNT(*)": "21",
            "SUM(Alert.EventCount)": "30",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Endpoint Security Firewall Property Translator",
            "COUNT(*)": "40",
            "SUM(Alert.EventCount)": "40",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Retrieve broker health information",
            "COUNT(*)": "41",
            "SUM(Alert.EventCount)": "41",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "5379-microsoft-windows-security-auditing",
            "COUNT(*)": "10",
            "SUM(Alert.EventCount)": "90",
            "Alert.DSIDSigID": "12345-2223334445"
        },{
            "Rule.msg": "Returns a list of DXL Registered Services",
            "COUNT(*)": "43",
            "SUM(Alert.EventCount)": "164",
            "Alert.DSIDSigID": "12345-2223334445"
        }
    ]
    

##### Case wall

Result type | Value/Description | Text  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code (is_success=true):_ "Successfully retrieved data for the provided query in McAfee ESM." _If there is no data for one entity (is_success=true):_ "No data was found for the provided query in McAfee ESM." _Asynchronous message:_ "Waiting for the query to finish…" **The action should fail and stop a playbook execution:** _If a critical error is reported:_ "Error executing action "Send Advanced Query to ESM". Reason: {0}".format(error.Stacktrace) _If the 400 or 500 status code is reported:_ "Error executing action "Send Advanced Query to ESM". Reason: {0}";.format(response) _If the action ran into a timeout:_ "Error executing action "Send Advanced Query to ESM". Reason: action initiated the query but ran into a timeout during data retrieval. Please increase the timeout in the IDE and try again." | General  
Case Wall Table | All fields from the response. | General  
  
### Send Query to ESM

#### Action description

Send a query to ESM.

**Note:** The action is running as async, adjust the script timeout value in Google SecOps IDE for action as needed.

#### Action usage

Use this action to perform additional drilling on the Google SecOps alert. You can fetch events, assets and flow information.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Time Range | Drop-down list | LAST_24_HOURS Possible Values:

  * LAST_MINUTE
  * LAST_10_MINUTES
  * LAST_30_MINUTES
  * LAST_HOUR
  * CURRENT_DAY
  * PREVIOUS_DAY
  * LAST_2_DAYS
  * LAST_3_DAYS
  * CURRENT_WEEK
  * PREVIOUS_WEEK
  * CURRENT_MONT
  * PREVIOUS_MONT
  * CURRENT_QUARTER
  * PREVIOUS_QUARTER
  * CURRENT_YEAR
  * PREVIOUS_YEAR

| Yes | Specify a time frame for the results. If `Custom` is selected, you also need to set the **Start Time** parameter.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if `Custom` is selected for the **Time Frame** parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results. Format: ISO 8601. If nothing is provided and `Custom` is selected for the **Time Frame** parameter then this parameter uses current time.  
Filter Field Name | String | N/A | Yes | Specify the field name that will be used for filtering.  
Filter Operator | Drop-down list | EQUALS Possible Values:

  * IN
  * NOT_IN
  * GREATER_OR_EQUALS_THAN
  * LESS_OR_EQUALS_THAN
  * DOES_NOT_EQUAL
  * EQUALS
  * CONTAINS
  * DOES_NOT_CONTAIN
| Yes | Specify the operator that should be used in the filter. 
  
Filter Values | String | N/A | Yes | Specify a comma-separated list of values that will be used in the filter.  
Fields To Fetch | CSV | N/A | No | Specify a comma-separated list of fields that should be returned. If nothing is provided, the action uses the predefined fields.  
Sort Field | String | N/A | No | Specify what parameter should be used for sorting. This parameter expects the field in the format {table}.{key name}. If the parameter is provided in another format, the action will skip it. Example: Alert.LastTime  
Sort Order | Drop-down list | ASC Possible values:

  * ASC
  * DESC

| No | Specify the order of sorting.  
Query Type | Drop-down list | EVENT Possible values:

  * EVENT
  * FLOW
  * ASSET

| Yes | Specify what needs to be queried.  
Max Results To Return | Integer | 50 | Yes | Specify the number of results to return. The default parameter value: 50. The maximum parameter value: 200.  
  
##### Work with the Time Range parameter

The **Time Range** parameter specifies the time frame to be used when executing the query. The action supports a lot of predefined values that you can select. You also can set a custom time range.

To set the custom time range, you need to set the **Time Range** parameter to `Custom` and provide an ISO 8601 value for the **Start Time** parameter. By default the **End Time** parameter points to the current time.

##### Specify fields for the Filter Field Name, Fields To Fetch, and Sort Field parameters

To specify fields for the Filter **Field Name** , **Fields To Fetch** , and **Sort Field** parameters, complete the following steps:

  1. Log in to the **McAfee ESM UI** and open **Developer Tools** in your browser.
  2. Go to the **Network** tab.
  3. Click **Add Tab** and add a new view.
  4. Click **Add Widget**.
  5. In the **Widget Configuration** dialog:

     * in the **Fields** section, select all the fields that interest you.
     * enter a custom title and set **Query Source** to `Events`. For assets, select `Assets`, and for flows, select `Flows`.

![Widget Configuration dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-advanced-query-widget-configuration.png)

  6. Once you've selected all the fields you need, click **Create**.

  7. In **Developer Tools** , you will see the `runningQuery` request. Get details about this request and go to the **Request** section. There you will see a list of all the API names for the fields that you have provided.

![Request details](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-query-runningquery.png)




##### Known issues

  * The McAfee ESM API that is used by the action to send query (`qryExecuteDetail`) has unexpected behaviors in scenarios, where a key of unsupported type (FLOAT keys) are used with the `GREATER_OR_EQUALS_THAN` or `LESS_OR_EQUALS_THAN` operators. Validate the types of the fields that are used.
  * It has been observed that some key combinations return no results even though the filter did not return a McAfee API error.

**Note:** If you encounter any of the listed known issues, we recommend to use the [Send Advanced Query To ESM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#send-advanced-query-to-esm) action instead.

#### Action entity scope

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "Rule.msg": "McAfee EDB database server state change alert",
            "Alert.AvgSeverity": "25",
            "Alert.SrcIP": "::",
            "Alert.EventCount": "1",
            "Alert.LastTime": "02/12/2019 20:45:45",
            "Alert.Protocol": "n/a",
            "Action.Name": "informational",
            "Alert.IPSIDAlertID": "144115188075855872|1",
            "Alert.DstIP": "10.0.0.10"
        }
    ]
    

##### Case wall

Result type | Value/Description | Text  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code (is_success=true):_ "Successfully retrieved data for the provided query in McAfee ESM." _If there is no data for one entity (is_success=true):_ "No data was found for the provided query in McAfee ESM." _Asynchronous message:_ "Waiting for the query to finish…" **The action should fail and stop a playbook execution:** _If a critical error is reported:_ "Error executing action "Send Query to ESM". Reason: {0}".format(error.Stacktrace) _If the 400 or 500 status code is reported:_ "Error executing action "Send Query to ESM". Reason: {0}".format(response) _If the action ran into a timeout:_ "Error executing action "Send Query to ESM". Reason: action initiated the query but ran into a timeout during data retrieval. Please increase the timeout in the IDE and try again." | General  
Case Wall Table | All fields from the response. | General  
  
### Send Entity Query To ESM

#### Action description

Send a query to ESM based on entities. Supported entities: IP Address, Hostname.

**Note:** The action is running as async, adjust the script timeout value in Google SecOps IDE for action as needed.

#### Action usage

Use this action to perform additional drilling on the Google SecOps alert around the entities. You can fetch events, assets, and flow information. Unlike the [Send Query To ESM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#send-query-to-esm) action, this action also adds an entity filter as a part of the query.

#### Action configuration parameters

Use the following parameters to configure the action:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
IP Address Entity Key | String | Alert.SrcIP | Yes | Specify the key that will is with the IP Address entity during filtering. If an invalid key is provided, the action still returns results, but they are unexpected. |   
Hostname Entity Key | String | N/A | Yes | Specify the key that is used with the Hostname entity during filtering. If an invalid key is provided, the action still returns results, but they are unexpected.  
Time Range | Drop-down list | LAST_HOUR Possible values:

  * LAST_MINUTE
  * LAST_10_MINUTES
  * LAST_30_MINUTES
  * LAST_HOUR
  * CURRENT_DAY
  * PREVIOUS_DAY
  * LAST_2_DAYS
  * LAST_3_DAYS
  * CURRENT_WEEK
  * PREVIOUS_WEEK
  * CURRENT_MONTH
  * PREVIOUS_MONTH
  * CURRENT_QUARTER
  * PREVIOUS_QUARTER
  * CURRENT_YEAR
  * PREVIOUS_YEAR
  * CUSTOM

| Yes | Specify a time frame for the results. If `Custom` is selected, you also need to provide the **Start Time** parameter.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if `Custom` is selected for the **Time Frame** parameter. Format: ISO 8601 | End Time | String | N/A | No | Specify the end time for the results. Format: ISO 8601. If nothing is provided and `Custom` is selected for the **Time Frame** parameter then this parameter uses current time.  
Filter Field Name | String | N/A | Yes | Specify the field name that will be used for filtering.  
Filter Operator | Drop-down list | EQUALS Possible Values:

  * IN
  * NOT_IN
  * GREATER_OR_EQUALS_THAN
  * LESS_OR_EQUALS_THAN
  * DOES_NOT_EQUAL
  * EQUALS
  * CONTAINS
  * DOES_NOT_CONTAIN
| Yes | Specify the operator that should be used in the filter. 
  
Filter Values | String | N/A | Yes | Specify a comma-separated list of values that will be used in the filter.  
Fields To Fetch | CSV | N/A | No | Specify a comma-separated list of fields that should be returned. If nothing is provided, the action uses the predefined fields.  
Sort Field | String | N/A | No | Specify what parameter should be used for sorting. This parameter expects the field in the format {table}.{key name}. If the parameter is provided in another format, the action will skip it. Example: Alert.LastTime  
Sort Order | Drop-down list | ASC Possible values:

  * ASC
  * DESC

| No | Specify the order of sorting.  
Max Results To Return | Integer | 50 | Yes | Specify the number of results to return. The default parameter value: 50. The maximum parameter value: 200.  
  
##### Work with the Time Range parameter

The **Time Range** parameter specifies the time frame to be used when executing the query. The action supports a lot of predefined values that you can select. You also can set a custom time range.

To set the custom time range, you need to set the **Time Range** parameter to `Custom` and provide an ISO 8601 value for the **Start Time** parameter. By default the **End Time** parameter points to the current time.

##### Specify fields for the Filter Field Name, Fields To Fetch, and Sort Field parameters

To specify fields for the **Filter Field Name** , **Fields To Fetch** , and **Sort Field** parameters, complete the following steps:

  1. Log in to the **McAfee ESM UI** and open **Developer Tools** in your browser.
  2. Go to the **Network** tab.
  3. Click **Add Tab** and add a new view.
  4. Click **Add Widget**.
  5. In the **Widget Configuration** dialog:

     * in the **Fields** section, select all the fields that interest you.
     * enter a custom title and set **Query Source** to `Events`. For assets, select `Assets`, and for flows, select `Flows`.

![Widget Configuration dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-advanced-query-widget-configuration.png)

  6. Once you've selected all the fields you need, click **Create**.

  7. In **Developer Tools** , you will see the `runningQuery` request. Get details about this request and go to the **Request** section. There you will see a list of all the API names for the fields that you have provided.

![Request details](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-send-query-runningquery.png)




##### Work with the IP Address Entity Key and Hostname Entity Key parameters

The **IP Address Entity Key** and **Hostname Entity Key** parameters define the key that is used in the filter. For example, if the **IP Address Entity Key** parameter is set to `Alert.SrcIP`, the action creates an IP address filter using the `Alert.SrcIP` key. Depending on your use case, you can modify the key that is used.

##### Known issues

  * The McAfee ESM API that is used by the action to send query (`qryExecuteDetail`) has unexpected behaviors in scenarios, where a key of unsupported type (FLOAT keys) are used with the `GREATER_OR_EQUALS_THAN` or `LESS_OR_EQUALS_THAN` operators. Validate the types of the fields that are used.
  * It has been observed that some key combinations return no results even though the filter did not return a McAfee API error.

**Note:** If you encounter any of the listed known issues, we recommend to use the [Send Advanced Query To ESM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#send-advanced-query-to-esm) action instead.

#### Action entity scope

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "Rule.msg": "McAfee EDB database server state change alert",
            "Alert.AvgSeverity": "25",
            "Alert.SrcIP": "::",
            "Alert.EventCount": "1",
            "Alert.LastTime": "02/12/2019 20:45:45",
            "Alert.Protocol": "n/a",
            "Action.Name": "informational",
            "Alert.IPSIDAlertID": "144115188075855872|1",
            "Alert.DstIP": "10.0.0.10"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported(is_success=true):_ "Successfully retrieved data for the following entities in McAfee ESM: {entity.identifier}" _If there is no data for all entities:_ "No data was found in McAfee ESM for the following entities: {entity.id}." _If the 400 or 500 status code is reported for a specific entity:_ "Queries weren't executed in McAfee ESM for the following entities: {entity.id}. Please check the configuration." _If there is no data for all entities (is_success=true):_ "No data was found for the provided entities in McAfee ESM" _Asynchronous message:_ "Waiting for the entity to finish processing..." **The action should fail and stop a playbook execution:** _If a critical error is reported:_ "Error executing action "Send Entity Query To ESM". Reason: {0}''.format(error.Stacktrace)." _If the 400 or 500 status code is reported for all entities:_ "Error executing action "Send Entity Query To ESM". Reason: {response}' _If the action ran into a timeout:_ "Error executing action "Send Entity Query To ESM". Reason: action initiated the query but ran into a timeout during data retrieval for the following entities: {entity.identifier}. Please increase the timeout in the IDE and try again. Note: If you retry the action will send another message." | General  
Case Wall Table | All fields from response. | Entity  
  
## Connectors

### Connectors upgrade - integration version: 34.0

The connectors have been revamped in the 34.0 integration version. They have been optimized to be less prone to bugs and easier to maintain. Also new features have been added.

If you want to upgrade the connector to the 34.0 version, we recommend you to get familiar with the connector configuration parameters first. The connector upgrade doesn't affect playbooks.

### McAfeeESM Connector

#### Connector description

Pull information about alarms from McAfee ESM.

**Note:** The Dynamic List filter works with the **alarmName** parameter.

#### Connector usage

Use the connector to ingest correlations and related events into Google SecOps. In this connector one Google SecOps alert is represented by one Correlation event.

Google SecOps events are created based on data from the following objects:

  * **Alarm Data**
  * **Correlation Event Data:** correlation is a trigger event created from correlation rules
  * **Source Event Data:** base events that caused a correlation or alarm



Example of the Google SecOps event based on Alarm Data:

![Google SecOps event based on Alarm Data](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-esm-connector-alarm-based-event.png)

Example of the Google SecOps event based on Correlation or Source Event Data:

![Google SecOps event based on Correlation or Source Event Data](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-esm-connector-correlation-based-event.png)

Each Google SecOps event contains raw information from the API along with additional keys that were added to make mapping easier. To distinguish the different types of Google SecOps events, there is a custom `data_type` key. This key can contain the following values:

  * Alarm
  * Correlation Event
  * Source Event



#### Custom type fields in Google SecOps events

McAfee ESM Correlation/Source events can include custom fields that raw API representation is not suitable for mapping purposes.

Example of the raw custom type data:
    
    
      "customTypes": [
          {
              "fieldId": 1,
              "fieldName": "AppID",
              "definedFieldNumber": 1,
              "unformattedValue": "374385694492",
     "formatedValue": "WIN"
          },
          {
              "fieldId": 7,
              "fieldName": "UserIDSrc",
              "definedFieldNumber": 7,
              "unformattedValue": "22018731010750406",
              "formatedValue": "NGCP"
          },
          {
              "fieldId": 4259842,
              "fieldName": "Message_Text",
              "definedFieldNumber": 9,
              "unformattedValue": "11049395522927265911",
              "formatedValue": "User Log In succeeded"
          }
      ]
    

In the Google SecOps event, the same fields are represented in the following way:
    
    
    {
      "{fieldName}": "{formatedValue}",
      "AppID": "WIN",
      "UserIDSrc": "NGCP",
      "Message_Text": "formatedValue",
      "customTypeFields": {
        "{fieldName}": "{formatedValue}",
        "AppID": "WIN",
        "UserIDSrc": "NGCP",
        "Message_Text": "formatedValue"
      }
    }
    

We recommended to use placeholders with the `customTypeFields` key as the placeholder values correctly represent the custom field. The custom fields that are represented at the level above may contain misleading information. If a key with the same name existed before the custom field was added, then the data from the original key is used as you can't have duplicate keys in the JSON file.

#### Configure the connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

#### Connector configuration parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Product Field Name | String | data_type | Yes | The field name used to determine the device product.  
Event Field Name | String | alarmName | Yes | The field name used to determine the event name (sub-type).  
API Root | String | https://{ipaddress}/rs/ | Yes | The API Root of the McAfee ESM instance. Format: https://{ip address}/rs/  
Password | Secret | N/A | Yes | Password of the McAfee ESM account.  
PythonProccessTimeout | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
Product Version | String | N/A | Yes | Version of Mcafee ESM. Possible values: 11.1, 11.2, 11.3, 11.4, 11.5.  
Username | String | N/A | Yes | Username of the McAfee ESM account.  
Disable Overflow | Checkbox | Unchecked | No | If enabled, the connector will disable the overflow mechanism. For more information about this parameter, see [ Work with the Disable Overflow and Disable Overflow For Alarms parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#alarms-disable-overflow).  
Disable Overflow For Alarms | CSV | N/A | No | A comma-separated list of alarm names for which the connector will ignore overflow. This parameter requires the **Disable Overflow** parameter to be enabled. For more information about this parameter, see [ Work with the Disable Overflow and Disable Overflow For Alarms parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#alarms-disable-overflow).  
Environment Field Name | String | srcZone | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | :* | No | A regex pattern to run on the value found in the Environment Field Name field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Ingest 0 Source Event Alarms | Checkbox | Checked | No | If enabled, the connector ingests alarms that have 0 source events. The connector will wait the time that is provided in the **Padding Time** parameter. For more information about this parameter, see [ Work with the Ingest 0 Source Event Alarms parameter](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#ingest-0-source-event-alarms).  
Lowest Severity To Fetch | Integer | 0 | No | The lowest severity that needs to be used to fetch alarms. Possible values are in range from 0 to 100. If nothing is specified, the connector ingests alarms with all types of severity.  
Max Alarms To Fetch | Integer | 100 | No | The number of alarms to process per one connector iteration. The default parameter value : 20.  
Max Hours Backwards | Integer | 1 | No | The number of hours from when to fetch alarms.  
Padding Time | Integer | 1 | No | The number of hours that the connector uses for padding. This parameter describes how long the connector waits to ingest the alarm with 0 source events, if the **Ingest 0 Source Event Alarms** parameter is disabled. The maximum parameter value: 6 hours.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Rule Generator Field Name | String | alarmName | No | Name of the field that is used in the rule generator. The connector uses `alarmName`, if the value is not available and this parameter is only applied to the values that come from source events.  
Secondary Device Product Field | String | N/A | No | Fallback product field name.  
Time Format | String | %m/%d/%Y %H:%M:%S | No | Time format that is used to read the timestamp provided in McAfee ESM. If nothing is provided or an invalid time format is provided, then the connector will not perform the transformation. For more information about this parameter, see [ Work with the Time Zone and Time Format parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#alarms-time-zone-format).  
Time Zone | String | N/A | No | Time zone of the source event. This parameter is needed to transform the timestamp into the format that reflects UTC+0 time. This parameter is ignored, if an invalid values are provided in the **Time Format** parameter or nothing is provided there. For more information about this parameter, see [ Work with the Time Zone and Time Format parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#alarms-time-zone-format).  
Use dynamic list as a blocklist | Checkbox | Unchecked | No | If enabled, the dynamic list is used as a blocklist.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the McAfee ESM server is valid.  
  
##### Work with the Ingest 0 Source Event Alarms parameter

In McAfee ESM, it's possible to have correlations with 0 events, which means that the Google SecOps alert contains only one Google SecOps event based on the correlation information. It's not recommended to ingest correlations with 0 source events as the context will be lost.

If the **Ingest 0 Source Event Alarms** parameter is enabled, the connector ingests all correlations into the Google SecOps system, even if there are 0 related events. If this parameter is disabled, the connector waits until at least one source event appears in McAfee ESM. The waiting time is defined by the **Padding Period** parameter.

The **Padding Period** parameter specifies the number of hours back (maximum value is 6) that the connector fetches data in each iteration. For example, if the **Padding Period** parameter is set to `2`, the connector always fetches data 2 hours back and starts handling data from that point in time. Logically, the **Padding Time** represents the number of hours the connector waits for the event to occur so it can ingest it.

There is an exception for two alarm types:

  * Device Health
  * EPS Rate Exceeded



These alarms come from the default McAfee ESM configuration and they will never have any events related to them. The connector always ingests them regardless of the **Ingest 0 Source Event Alarms** configuration parameter setting.

##### Work with the Time Zone and Time Format parameters

Sometimes time and time zones at the McAfee ESM server level can be configured using different formats. This can create some challenges, because, for example, the McAfee ESM API doesn't return information about the time zone. By default, the connector treats the timestamp that comes from the API as UTC. This can mess up time in the Google SecOps alerts and events as localization settings are applied.

For example, the raw API returned a timestamp in UTC+8. The connector ingested the alarm and then the localization was also set to UTC+8. In this situation, the Google SecOps alert timestamp is from the future.

To overcome this challenge, use the **Time Zone** parameter. This parameter defines requirements for getting the timestamp in the UTC format. If Mcafee ESM returns a timestamp in the UTC+8 format, you need to set the **Time Zone** connector parameter to `-8`.

In Google SecOps events, there are 3 new keys added:

  * the `utc_firstTime` and `utc_lastTime` keys for the event based on the Correlation/Source event data.
  * the `utc_triggeredDate` key for the event based on the Alarm data.



![Example of added key](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-esm-connector-time-zone-format.png)

##### Work with the Disable Overflow and Disable Overflow For Alarm Names parameters

Sometimes McAfee ESM can be very noisy and create a lot of correlation events. In Google SecOps, there is an overflow mechanism to prevent creating too many Google SecOps alerts in a short period of time.

This mechanism might be harmful, if you believe that all alarms are meaningful and need to be triaged. **We don't recommend disabling the overflow mechanism**. However, if required, you can use the **Disable Overflow** and **Disable Overflow For Alarm Names** parameters for this purpose.

The preferred solution is to use the **Disable Overflow For Alarm Names** parameter as it allows you to provide specific alarm names that should ignore overflow rules instead of disabling overflow for all alarms.

### McAfeeESM Correlations Connector

#### Connector description

Pull information about сorrelations from McAfee ESM.

**Note:** The dynamic list filter works with the **ruleName** parameter.

#### Connector usage

Use the connector to ingest correlations and related events into Google SecOps. In this connector one Google SecOps alert is represented by one Correlation event.

Google SecOps events are created based on data from the following objects:

  * **Correlation Event Data:** correlation is a trigger event created from correlation rules
  * **Source Event Data:** base events that caused a correlation



Example of the Google SecOps event based on Correlation or Source Event Data:

![Google SecOps event based on Correlation or Source Event Data](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-esm-correlations-connector-correlations-based-event.png)

Each Google SecOps event contains raw information from the API along with additional keys that were added to make mapping easier. To distinguish the different types of Google SecOps events, there is a custom `data_type` key. This key can contain the following values:

  * Correlation Event
  * Source Event



#### Custom type fields in Google SecOps events

McAfee ESM Correlation/Source events can include custom fields that raw API representation is not suitable for mapping purposes.

Example of the raw custom type data:
    
    
      "customTypes": [
          {
              "fieldId": 1,
              "fieldName": "AppID",
              "definedFieldNumber": 1,
              "unformattedValue": "374385694492",
              "formatedValue": "WIN"
          },
          {
              "fieldId": 7,
              "fieldName": "UserIDSrc",
              "definedFieldNumber": 7,
              "unformattedValue": "22018731010750406",
              "formatedValue": "NGCP"
          },
          {
              "fieldId": 4259842,
              "fieldName": "Message_Text",
              "definedFieldNumber": 9,
              "unformattedValue": "11049395522927265911",
              "formatedValue": "User Log In succeeded"
          }
      ]
    

In the Google SecOps event, the same fields are represented in the following way:
    
    
    {
      "{fieldName}": "{formatedValue}",
      "AppID": "WIN",
      "UserIDSrc": "NGCP",
      "Message_Text": "formatedValue",
      "customTypeFields": {
        "{fieldName}": "{formatedValue}",
        "AppID": "WIN",
        "UserIDSrc": "NGCP",
        "Message_Text": "formatedValue"
      }
    }
    

We recommended to use placeholders with the `customTypeFields` key as the placeholder values correctly represent the custom field. The custom fields that are represented at the level above may contain misleading information. If a key with the same name existed before the custom field was added, then the data from the original key is used as you can't have duplicate keys in the JSON file.

#### Configure the connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Product Field Name | String | data_type | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | sigId | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | srcZone | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | :* | No | A regex pattern to run on the value found in the Environment Field Name field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
PythonProcessTimeout | String | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{ipaddress}/rs/ | Yes | The API Root of the McAfee ESM instance. Format: https://{ip address}/rs/  
Username | String | N/A | No | Username of the McAfee ESM account.  
Password | Secret | N/A | No | Password of the McAfee ESM account.  
Product Version | String | N/A | Yes | Version of McAfee ESM. Possible values: 11.1, 11.2, 11.3, 11.4, 11.5.  
Lowest Average Severity To Fetch | Integer | 0 | No | The lowest average severity that needs to be used to fetch correlations. Possible values are in range from 0 to 100. If nothing is specified, the connector ingests correlations with all types of severity.  
Ingest 0 Source Event Correlations | Checkbox | Unchecked | No | If enabled, the connector ingests correlations that have 0 source events. This parameter can impact the values that come from the **Product Field Name** , **Event Field Name** , and **Rule Generator Field Name** parameters. If disabled, the connector waits for the time that is specified in the **Padding Time** parameter. For more information about this parameter, see [ Work with the Ingest 0 Source Event Correlations parameter](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#ingest-0-source-event-correlation).  
Padding Time | Integer | 1 | No | The number of hours that the connector uses for padding. This parameter describes how long the connector will wait to ingest the correlation with 0 source events, if the Ingest 0 Source Event Correlations parameter is disabled. The maximum parameter value: 6 hours.  
Max Hours Backwards | Integer | 1 | No | The number of hours from when to fetch alarms.  
Max Correlations To Fetch | Integer | 20 | No | The number of alarms to process per one connector iteration. The default parameter value: 20.  
IPSIDs Filter |  | N/A | No | Comma-separated list of IPSIDs that is used to fetch data. If nothing is provided, the connector uses default IPSID.  
SIGIDs Filter | CSV | N/A | No | Comma-separated list of signature IDs that are used during ingestion. If nothing is provided, the connector ingests correlations from all rules.  
Use dynamic list as a blocklist | Checkbox | Unchecked | No | If enabled, the dynamic list is used as a blocklist.  
Time Format | String | %m/%d/%Y %H:%M:%S | No | Time format that is used to read the timestamp provided in McAfee ESM. If nothing is provided or an invalid time format is provided, then the connector does not perform the transformation. For more information about this parameter, see [ Work with the Time Zone and Time Format parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#correlation-time-zone-format).  
Time Zone | String | N/A | No | Time zone of the source event. This parameter is needed to transform the timestamp into the format that reflects UTC+0 time. This parameter is ignored, if an invalid values are provided in the **Time Format** parameter or nothing is provided there. For more information about this parameter, see [ Work with the Time Zone and Time Format parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#correlation-time-zone-format).  
Rule Generator Field Name | String | app | No | Name of the field that is used in the rule generator. The action uses `ruleName`, if an invalid value is provided.  
Secondary Device Product Field | String | N/A | No | Fallback product field name.  
Disable Overflow | Checkbox | Unchecked | No | If enabled, the connector disables the overflow mechanism. For more information about this parameter, see [ Work with the Disable Overflow and Disable Overflow For SigIDs](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#correlation-disable-overflow) parameters.  
Disable Overflow For SigIDs | CSV | N/A | No | A comma-separated list of signature IDs for which connector ignores overflow. This parameter requires the **Disable Overflow** parameter to be enabled. For more information about this parameter, see [ Work with the Disable Overflow and Disable Overflow For SigIDs](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-esm#correlation-disable-overflow) parameters.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the McAfee ESM server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
##### Work with the Ingest 0 Source Event Correlations parameter

In McAfee ESM, it's possible to have correlations with 0 events, which means that the Google SecOps alert contains only one Google SecOps event based on the correlation information. It's not recommended to ingest correlations with 0 source events as the context will be lost.

If the **Ingest 0 Source Event Correlations** parameter is enabled, the connector ingests all correlations into the Google SecOps system, even if there are 0 related events. If this parameter is disabled, the connector waits until at least one source event appears in McAfee ESM. The waiting time is defined by the **Padding Period** parameter.

The **Padding Period** parameter specifies the number of hours back (maximum value is `6`) that the connector fetches data in each iteration. For example, if the **Padding Period** parameter is set to `2`, the connector always fetches data 2 hours back and starts handling data from that point in time. Logically, the Padding Time represents the number of hours the connector waits for the event to occur so it can ingest it.

##### Work with the Time Zone and Time Format parameters

Sometimes time and time zones at the McAfee ESM server level can be configured using different formats. This can create some challenges, because, for example, the McAfee ESM API doesn't return information about the time zone. By default, the connector treats the timestamp that comes from the API as UTC. This can mess up time in the Google SecOps alerts and events as localization settings are applied.

For example, the raw API returned a timestamp in UTC+8. The connector ingested the alarm and then the localization was also set to UTC+8. In this situation, the Google SecOps alert timestamp is from the future.

To overcome this challenge, use the **Time Zone** parameter. This parameter defines requirements for getting the timestamp in the UTC format. If Mcafee ESM returns a timestamp in the UTC+8 format, you need to set the **Time Zone** connector parameter to `-8`.

In Google SecOps events, there are 2 new keys added: the `utc_firstTime` and u`tc_lastTime` keys for the event based on the Correlation/Source event data.

##### Work with the Disable Overflow and Disable Overflow For SigIDs parameters

Sometimes McAfee ESM can be very noisy and create a lot of correlation events. In Google SecOps, there is an overflow mechanism to prevent creating too many Google SecOps alerts in a short period of time.

This mechanism might be harmful, if you believe that all alarms are meaningful and need to be triaged. **We don't recommend disabling the overflow mechanism.** However, if required, you can use the **Disable Overflow** and **Disable Overflow For SigIDs** parameters for this purpose.

The preferred solution is to use the **Disable Overflow For SigIDs** parameter as it allows you to provide specific signature IDs that should ignore overflow rules instead of disabling overflow for all correlations.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
