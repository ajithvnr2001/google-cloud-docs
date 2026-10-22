---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/splunk/
title: Integrate Splunk with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:43.197977+00:00
---

# Integrate Splunk with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/splunk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Splunk with Google SecOps 

This document provides guidance on how to integrate Splunk with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Splunk.zip).

## Before you begin

Before you integrate Splunk with Google SecOps, determine the appropriate ingestion method for your deployment architecture and verify that your environment satisfies all required dependencies, network paths, and access permissions.

Google SecOps supports two ingestion methods:

  * **Push-based ingestion**: Splunk evaluates alerts locally and pushes events directly to Google SecOps using the TA-Siemplify add-on and alert trigger actions. No connector configuration is required in Google SecOps.

  * **Pull-based ingestion**: Google SecOps connectors periodically query Splunk REST API endpoints to retrieve alerts, SPL search results, or Splunk ES Notable Events.




### Push-based ingestion

Push-based ingestion requires direct outbound HTTPS connectivity from Splunk to Google SecOps, as well as specific add-on configurations on your Splunk Search Heads.

Verify the following requirements before configuring push-based ingestion:

  1. Download and install the **TA-Siemplify** package from [Splunkbase](https://splunkbase.splunk.com/app/5010/) onto all target Splunk Search Heads. In distributed environments, deploy the add-on across your Search Head Cluster using the Splunk Deployer or Deployment Server.

  2. Verify that a compatible version of **Splunk Common Information Model (Splunk_SA_CIM)** is installed on the Search Head to support modular alerts and logging.

  3. Ensure that your Splunk Search Heads have outbound network access over HTTPS (TCP port 443) to your Google SecOps instance URL.

  4. Verify that you have an account in Google SecOps with administrative permissions to generate API keys (**Settings > Advanced > API**). Ensure the generated API key is assigned a role with alert and case creation permissions.

  5. If you plan to ingest raw events from transforming searches (such as searches using `stats`, `chart`, or `timechart`), ensure that `dispatch.buckets = 1` is configured in `savedsearches.conf` on your Search Heads.




### Pull-based ingestion

Pull-based ingestion, playbook actions, and synchronization jobs require Google SecOps (or a remote agent) to establish inbound administrative connections to Splunk.

Verify the following requirements before configuring pull connectors, actions, or jobs:

  1. **Network connectivity** : Verify network line-of-sight from Google SecOps (or your remote agent) to the Splunk management REST API port (default: `8089/TCP`).

  2. **Custom CA certificate** : If your Splunk instance uses a private or internal CA certificate, verify that you are running Splunk integration version 26.0 or higher in Google SecOps.

  3. **Authentication** : Obtain valid Splunk user credentials (username and password) or generate a Splunk Bearer Token (to enable this authentication method on the Splunk platform, this requires token authentication).

  4. **Splunk role capabilities** : Ensure that the authenticating Splunk account holds a role with the following capabilities:

     * `search`
     * `schedule_search`
     * `edit_tcp` _(Required only if using theSubmit Event action)_
     * `edit_notable_events` _(Required only if using theUpdate Notable Events action or Splunk ES synchronization jobs)_
  5. **Data store and lookup permissions** : Verify that the authenticating account has access to the relevant Splunk data stores for your chosen components:

     * **Splunk pull connector** : Read permissions to the `siemplify_alerts` lookup table (populated when `TA-Siemplify` is installed and configured in Pull mode).
     * **Splunk query connector and actions** : 
       * Search permissions on target event indexes _(doesn't require`TA-Siemplify`)_.
       * Write and input permissions on the target index if using the Submit Event action.
     * **Splunk ES - notable events connector and jobs** : An active **Splunk Enterprise Security (ES)** installation, read permissions to the `notable` index, and access to the `get_notable_index` macro _(doesn't require`TA-Siemplify`)_.



### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | {SCHEMA}://{IP}:{PORT} | Yes | Address of the Splunk Server.  
Username | String | N/A | No | The email address of the user which should be used to connect to Splunk.  
Password | Password | N/A | No | The password of the according user.  
API Token | Password | N/A | No | Splunk API Token. API token has priority over other authentication methods, when this field is not empty.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Splunk connection requires an SSL verification (unchecked by default).  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Host Events

Get events related to hosts in Splunk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event Per Host Limit | Integer | 100 | Yes | Specify how many events to return per host.  
Results From | String | -24h | Yes | Specify the start time for the events.  
Results To | String | now | Yes | Specify the end time for the events.  
Result fields | CSV | N/A | No | Specify a comma-separated list of fields that need to be returned.  
Index | String | N/A | No | Specify what index should be used, when searching for events related to the host. If nothing is provided, action will not use index.  
Host Key | String | host | No | Specify what key should be used to get information about host events. Default: host.  
  
#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "app": "SA-AccessProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087674",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:58.404 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-AccessProtection;Access - Default Account Usage - Rule\", search_type=\"\", user=\"admin\", app=\"SA-AccessProtection\", savedsearch_name=\"Access - Default Account Usage - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=0, dispatch_time=1612179969, run_time=51348.242, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtQWNjZXNzUHJvdGVjdGlvbg__RMD509c859ea7b9951b8_at_1612179932_61.40533\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "0",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".404",
        "_time": "2021-02-02T04:01:58.404+02:00"
    },
    {
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087731",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "127.0.0.1 - admin [02/Feb/2021:04:01:58.172 +0200] \"POST /servicesNS/nobody/SA-AccessProtection/saved/searches/Access%20-%20Default%20Account%20Usage%20-%20Rule/notify?trigger.condition_state=1 HTTP/1.1\" 200 1985 - - - 3ms",
        "_serial": "1",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "splunkd_access",
        "_subsecond": ".172",
        "_time": "2021-02-02T04:01:58.172+02:00"
    },
    {
        "app": "SA-EndpointProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087653",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:57.804 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-EndpointProtection;Endpoint - Should Timesync Host Not Syncing - Rule\", search_type=\"\", user=\"admin\", app=\"SA-EndpointProtection\", savedsearch_name=\"Endpoint - Should Timesync Host Not Syncing - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=300, dispatch_time=1612179970, run_time=51347.420, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtRW5kcG9pbnRQcm90ZWN0aW9u__RMD5ef3c08822811b7cd_at_1612179932_62.25751\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "2",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".804",
        "_time": "2021-02-02T04:01:57.804+02:00"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If successful and results are available:** "Successfully returned events for the following hosts in Splunk: \n {0}".format(entity.identifier)  
******If successful and results are not available for some:** "No events were found for the following hosts in Splunk:\n {0}".format(entity.identifier)  
******If successful and results are not available for all:** "No events were found for the provided hosts in Splunk"******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get Host Events". Reason: {0}''.format(error.Stacktrace)******If 400:** "Error executing action "Get Host Events". Reason: {0}''.format(messages/text) | General  
Case Wall Table | **Name:** {Entity.identifier} Events**Columns:** Based on the results. |   
  
### Ping

Test connectivity to Splunk with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the Splunk server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the Splunk server! Error is {0}".format(exception.stacktrace) | General  
  
### Splunk Csv Viewer

**Deprecated:** This action creates a CSV table based on the raw results.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Results | string | N/A | Yes | Raw results.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
### SplunkQuery

Execute a query in Splunk.

**Important:** Exclude any quotes that are part of the query string.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Search Mode | DDL | Smart _Possible values:_

  * Verbose
  * Smart
  * Fast

| No | Specify the mode for executing search.  
Query | String |  | Yes | Specify the query that needs to be executed. Example: index="_internal"  
Results count limit | Integer | 100 | No | Specify how many results to return.   
Note: this parameter appends the "head" key word to the provided query. Default is 100.  
Results from | String | -24h | No | Specify the start time for the query. Default: -24h  
Results to | String | now | No | Specify the end time for the query. Default: now.  
Result fields | CSV |  | No | Specify a comma-separated list of fields that need to be returned.   
Note: this parameter appends "fields" key word to the provided query.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [{
        "app": "SA-AccessProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087674",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:58.404 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-AccessProtection;Access - Default Account Usage - Rule\", search_type=\"\", user=\"admin\", app=\"SA-AccessProtection\", savedsearch_name=\"Access - Default Account Usage - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=0, dispatch_time=1612179969, run_time=51348.242, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtQWNjZXNzUHJvdGVjdGlvbg__RMD509c859ea7b9951b8_at_1612179932_61.40533\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "0",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".404",
        "_time": "2021-02-02T04:01:58.404+02:00"
    },
    {
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087731",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "127.0.0.1 - admin [02/Feb/2021:04:01:58.172 +0200] \"POST /servicesNS/nobody/SA-AccessProtection/saved/searches/Access%20-%20Default%20Account%20Usage%20-%20Rule/notify?trigger.condition_state=1 HTTP/1.1\" 200 1985 - - - 3ms",
        "_serial": "1",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "splunkd_access",
        "_subsecond": ".172",
        "_time": "2021-02-02T04:01:58.172+02:00"
    },
    {
        "app": "SA-EndpointProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087653",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:57.804 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-EndpointProtection;Endpoint - Should Timesync Host Not Syncing - Rule\", search_type=\"\", user=\"admin\", app=\"SA-EndpointProtection\", savedsearch_name=\"Endpoint - Should Timesync Host Not Syncing - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=300, dispatch_time=1612179970, run_time=51347.420, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtRW5kcG9pbnRQcm90ZWN0aW9u__RMD5ef3c08822811b7cd_at_1612179932_62.25751\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "2",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".804",
        "_time": "2021-02-02T04:01:57.804+02:00"
    }]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If successful and results are available:** "Successfully returned results for the query "{0}" in Splunk".format(query)  
**If successful and results are not available:** "No results were found for the query "{0}" in Splunk".format(query)  
******Async message:** "Waiting for query {0} to finish execution.".format(query name)  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "SplunkQuery". Reason: {0}''.format(error.Stacktrace)******If 400:** "Error executing action "SplunkQuery". Reason: {0}''.format(messages/text) | General  
Case Wall Table | **Name:** Splunk Query Results**Columns -** Based on the results. | General  
  
### Submit Event

Submit event to Splunk.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Index | String | main | Yes | Specify the index, where the event should be created.  
Event | String | N/A | Yes | Specify the raw event that needs to be submitted.  
Host | String | N/A | No | Specify the host that is related to the event.  
Source | String | N/A | No | Specify the source of the event. Example: www.  
Sourcetype | String | N/A | No | Specify the source type of the event. Example: web_event  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "index": "default",
        "bytes": 70,
        "host": "dogo",
        "source": "www",
        "sourcetype": "web_event"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If successful:** "Successfully added a new event to index "{0}" in Splunk.".format(index)  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Submit Event". Reason: {0}''.format(error.Stacktrace)******If 400:** "Error executing action "Submit Event". Reason: {0}''.format(messages/text) | General  
  
### Update Notable Events

Update notable events in Splunk ES.

**Warning:** This action is only supported for Splunk ES.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Notable Event IDs | CSV | N/A | Yes | Specify IDs of notable events. Example: 1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7@@notable@@cb87390ae72763679d3f6f8f097ebe2b,1D234D5B-1531-2D2B-BB94-41C439BE12B7@@notable@@cb87390ae72763679d3f6f8f097ebe2b  
Status | DDL | Select OnePossible values:Select OneUnassignedNewIn ProgressPendingResolvedClosed | Yes | Specify the new status for notable events.  
Urgency | DDL | Select OnePossible values:Select OneCriticalHighMediumLowInformational | Yes | Specify the new urgency for the notable event.  
New Owner | String | N/A | Yes | Specify the new owner of the notable event.  
Comment | String | N/A | Yes | Specify the comment for the notable event.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful and data is available (is_success=true)_ print "Successfully updated {0} notable events in Splunk.".format(count(notable_events))___If fail to update (status_code=400, is_success=false):_ print "Action wasn't able to update notable events. Reason:{0}".format(string_from_response)  
**The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Update Notable Events". Reason: {0}''.format(error.Stacktrace) | General  
  
### Execute Entity Query

Execute an entity query in Splunk.

**Note:** this action prepares the "Where" clause based on the entities. Check documentation for additional information.

#### How to work with action parameters?

This action gives an ability to quickly retrieve information related to entities. For example, it's possible to solve the use case, where you want to see the amount of events of the endpoints affected by the provided hashes without any complicated query building. In order to solve this problem in the Splunk you would need to prepare the following query: `index="main" | where (device_ip="10.0.0.1" or device_ip="10.12.12.12") and (hash="bad_hash_1" or hash="bad_hash_2")` In order to create the same query using "Execute Entity Query" action, you need to fill out the action parameters in the following way:

Query | index="main"  
---|---  
IP Entity Key | device_ip  
File Hash Entity Key | hash  
Cross Entity Operator | AND  
  
All of the other fields can be left empty.

If the use case is to see how many endpoints were affected by the provided hashes, then the configuration of the "Execute Entity Query" will have the following look.

Query | index="main"  
---|---  
File Hash Entity Key | hash  
  
"Cross Entity Operator" in this situation won't have an impact, because it only affects the query, when multiple "Entity Keys" are provided.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Search Mode | DDL | Smart

_Possible values:_
  * Verbose
  * Smart
  * Fast

| No | Specify the mode for executing search.  
Query | String |  | Yes | Specify the query that needs to be executed without the "Where" clause. Example: index="_internal"  
Results count limit | Integer | 100 | No | Specify how many results to return. Note: this parameter appends the "head" key word to the provided query. Default is 100.  
Results from | String | -24h | No | Specify the start time for the query. Default: -24h  
Results to | String | now | No | Specify the end time for the query. Default: now.  
Result fields | CSV | N/A | No | Specify a comma-separated list of fields that need to be returned.   
Note: this parameter appends "fields" key word to the provided query.  
IP Entity Key | String | N/A | No | Specify what key should be used with IP entities. Please refer to the action documentation for details.  
Hostname Entity Key | String | N/A | No | Specify what key should be used with Hostname entities, when preparing the . Please refer to the action documentation for details.  
File Hash Entity Key | String | N/A | No | Specify what key should be used with File Hash entities. Please refer to the action documentation for details.  
User Entity Key | String | N/A | No | Specify what key should be used with User entities. Please refer to the action documentation for details.  
URL Entity Key | String | N/A | No | Specify what key should be used with URL entities. Please refer to the action documentation for details.  
Email Address Entity Key | String | N/A | No | Specify what key should be used with Email Address entities. Please refer to the action documentation for details.  
Stop If Not Enough Entities | Checkbox | Checked | Yes | If enabled, action will not start execution, unless all of the entity types are available for the specified ".. Entity Keys". Example: if "IP Entity Key" and "File Hash Entity Key" are specified, but in the scope there are no file hashes then if this parameter is enabled, action will not execute the query.  
Cross Entity Operator | DDL | ORPossible Values:ORAND | Yes | Specify what should be the logical operator used between different entity types.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * User
  * Hash
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [{
        "app": "SA-AccessProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087674",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:58.404 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-AccessProtection;Access - Default Account Usage - Rule\", search_type=\"\", user=\"admin\", app=\"SA-AccessProtection\", savedsearch_name=\"Access - Default Account Usage - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=0, dispatch_time=1612179969, run_time=51348.242, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtQWNjZXNzUHJvdGVjdGlvbg__RMD509c859ea7b9951b8_at_1612179932_61.40533\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "0",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".404",
        "_time": "2021-02-02T04:01:58.404+02:00"
    },
    {
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087731",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "127.0.0.1 - admin [02/Feb/2021:04:01:58.172 +0200] \"POST /servicesNS/nobody/SA-AccessProtection/saved/searches/Access%20-%20Default%20Account%20Usage%20-%20Rule/notify?trigger.condition_state=1 HTTP/1.1\" 200 1985 - - - 3ms",
        "_serial": "1",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "splunkd_access",
        "_subsecond": ".172",
        "_time": "2021-02-02T04:01:58.172+02:00"
    },
    {
        "app": "SA-EndpointProtection",
        "_bkt": "_internal~425~1A082D7B-D5A1-4A2B-BB94-41C439BE3EB7",
        "_cd": "425:9087653",
        "_indextime": "1612231318",
        "_kv": "1",
        "_raw": "02-02-2021 04:01:57.804 +0200 INFO  SavedSplunker - savedsearch_id=\"nobody;SA-EndpointProtection;Endpoint - Should Timesync Host Not Syncing - Rule\", search_type=\"\", user=\"admin\", app=\"SA-EndpointProtection\", savedsearch_name=\"Endpoint - Should Timesync Host Not Syncing - Rule\", priority=default, status=success, digest_mode=1, scheduled_time=1612179932, window_time=300, dispatch_time=1612179970, run_time=51347.420, result_count=0, alert_actions=\"\", sid=\"rt_scheduler__admin_U0EtRW5kcG9pbnRQcm90ZWN0aW9u__RMD5ef3c08822811b7cd_at_1612179932_62.25751\", suppressed=1, thread_id=\"AlertNotifierWorker-0\", workload_pool=\"\"",
        "_serial": "2",
        "_si": [
            "splunk",
            "_internal"
        ],
        "_sourcetype": "scheduler",
        "_subsecond": ".804",
        "_time": "2021-02-02T04:01:57.804+02:00"
    }]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If successful and results are available:** "Successfully returned results for the query "{0}" in Splunk".format(query)  
**If successful and results are not available:** "No results were found for the query "{0}" in Splunk".format(query)  
******Async message:** "Waiting for query {0} to finish execution.".format(query name)  
******If "Stop If Not Enough Entities" is enabled and not enough entity types are available for the provided "Entity Keys" (is_success=false):** Action wasn't able to build the query, because not enough entity types were supplied for the specified ".. Entity Keys". Please disable "Stop If Not Enough Entities" parameter or provide at least one entity for each specified ".. Entity Key".  
******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Execute Entity Query". Reason: {0}''.format(error.Stacktrace)******If 400:** "Error executing action "Execute Entity Query". Reason: {0}''.format(messages/text) | General  
Case Wall Table | **Name:** Splunk Query Results**Columns:** Based on the results. | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Splunk Query Connector

The connector sends queries that are a part of the dynamic list (`whitelist`), retrieves results, and builds a case based on the retrieved results.

#### Sample Splunk queries to view the logs

  1. Queries should be entered as the dynamic list (`whitelist`) rules.

  2. Search queries with multiple filters should use space as a delimiter between search filters—for example, `index=cim_modactions sourcetype=modular_alerts:risk`.

  3. Using multiple dynamic list (`whitelist`) rules rather than entering multiple space-delimited search filters into the same rule results in a separate search executed for every added rule.

     * `index=cim_modactions`
     * `sourcetype=modular_alerts:send_data_to_siemplify`
     * `index=_internal sourcetype=splunkd`
     * `component=sendmodalert`
     * `action=send_data_to_siemplify`
     * `index=_internal source=/opt/splunk/var/log/splunk/send_data_to_siemplify_modalert.log`



#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | **Required** Input the source field name to retrieve the `Product Field` name. Default value is `device_product`.  
`Event Field Name` | **Required** Enter the source field name to retrieve the `Event Field` name. Default value is `app`.  
`API Root` | **Required** API root of the Splunk instance.Default value is `https://`IP`:8089`.  
`Username` | **Required** Username of the Splunk account.  
`Password` | **Required** Password of the Splunk account.  
`API Token` | _Optional_ Splunk API token.If this field has any value, the API token has priority over other authentication methods.  
`Verify SSL` | **Required** If checked, verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Unchecked by default.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored.  
`Rule Generator Field` | **Required** The name of the field used to map the rule generator value.  
`Alert Name Field Name` | **Required** Alert name.  
`Events Count Limit Per Query` | _Optional_ Max amount of events to fetch per query.  
`Max Day Backwards` | _Optional_ Amount of days from where to fetch events.  
`Aggregate Events Query` | _Optional_ If enabled, the connector will combine all events under one alert.Disabled by default.  
`PythonProcessTimeout (Seconds)` | **Required** Timeout limit for the python process running the current script. Default value is 60 seconds.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Password` | _Optional_ Proxy password to authenticate with.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
  
#### Connector rules

The connector supports proxy.

### Splunk Pull Connector

Pull alerts and events from Splunk into Google SecOps.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | **Required** Input the source field name to retrieve the `Product Field` name. Default value is `device_product`.  
`Event Field Name` | **Required** Enter the source field name to retrieve the `Event Field` name. Default value is `name`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the result environment is `"" `. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`PythonProcessTimeout (Seconds)` | **Required** Timeout limit for the python process running the current script. Default value is 60 seconds.  
`Server Address` | **Required** IP address of the Splunk API server.  
`Port` | **Required** Port of the Splunk instance. Default value is `8089`.  
`Username` | **Required** Username of the Splunk account.  
`Password` | **Required** Password of the Splunk account.  
`Time Frame` | _Optional_ Timeframe for fetching the alerts. Default value is 1 hour.Examples: If the value is set to 1 minute, the connector fetches alerts starting from 1 minute ago.If the value is set to 3 hours, the connector fetches alerts starting from 3 hours ago.If the value is set to 1 day or week, the connector fetches alerts starting from 1 day (24 hours) or 1 week ago, respectively.  
`Alerts Count Limit` | _Optional_ Number of alerts returned by the connector per 1 iteration. Default value is 100.  
`Use SSL` | _Optional_ Check to enable the SSL or TLS connection. Unchecked by default.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Password` | _Optional_ Proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxy.

### Splunk ES - Notable Events Connector

Ingest notable events from Splunk ES.

**Note:** This connector only works with Splunk ES.

#### Define case priority

The case priority is defined by the `Urgency` parameter in the notable event. Only this parameter is taken into consideration when ingesting the notable event into Google SecOps.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | **Required** Input the source field name to retrieve the `Product Field` name. Default value is `Product Name`.  
`Event Field Name` | **Required** Enter the source field name to retrieve the `Event Field` name. Default value is `index`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | **Required** Timeout limit for the python process running the current script. Default value is 180 seconds.  
`Server Address` | **Required** Server address of the Splunk instance. Default value is `https://:8089`.  
`Username` | _Optional_ Username of the Splunk account.  
`Password` | _Optional_ Password of the Splunk account.  
`API Token` | **Required** Splunk API token. If this field has any value, the API token has priority over other authentication methods.  
`Lowest Urgency To Fetch` | **Required** Lowest urgency used to fetch notable events.Possible values are: 

  * `Informational`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

Default value is `Medium`.   
`Fetch Max Hours Backwards` | _Optional_ Amount of hours from where to fetch notable events. Default value is 1 hour.  
`Only Drilldown Events` | _Optional_ If enabled, the connector attempts to fetch drilldown events without fetching base events. This parameter requires the `Fetch Base Events ` option enabled. Disabled by default.  
`Padding Time` | _Optional_ Amount of hours that will be used as a padding. If no value is provided, this parameter isn't applicable. Max value is 12 hours.  
`Max Notable Events To Fetch` | _Optional_ Number of notable events to process per one connector iteration. Default value is 10.  
`Use whitelist as a blacklist` | **Required** If enabled, the dynamic list is used as a blocklist. Disabled by default.  
`Verify SSL` | **Required** If checked, verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Unchecked by default.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Password` | _Optional_ Proxy password to authenticate with.  
`Query Filter` | _Optional_ Additional query filter sent to Splunk to get notable events.Value provided here is appended to the **WHERE** query clause.  
`Extract Base Events` | _Optional_ If enabled, the connector extracts base events related to the notable event using information about the job. In other case, the connector creates a Google SecOps event based on the notable event.If this parameter is set to `True` but the connector can't work with jobs, the connector uses information about notable events as a fallback mechanism. Enabled by default.  
`Multivalue Fields` | _Optional_ A comma-separated list of fields containing multiple entities. For example, if a field contains two hostnames, the notable event is split into two Google SecOps events to map entities correctly.   
`Notable Event Data Along Base Event` | _Optional_ If enabled, the connector adds Google SecOps events based on the notable event in addition to base events.Disabled by default.   
`Rule Generator Field Name` | _Optional_ The name of the field used to map the rule generator value.Only information about the notable event itself is used for mapping, events are disregarded. If invalid value is provided, the connector sets the field to the `rule_name` value.  
`Alert Name Source` | _Optional_ Source for the alert name.Possible values are:

  * `Search Name`
  * `Rule Name`

Default value is `Search Name`.  
`Alert Start Time Field` | _Optional_ A field from the Splunk Notable Event to use as the alert's `start_time`. If the field is empty, invalid, or cannot be parsed as a timestamp, the connector falls back to the default behavior using the `_time` field.  
  
#### How to use the `Query Filter` parameter

If there is a need to narrow down notable events based on the specific parameters, use the `Query Filter` parameter. The value provided in this parameter is appended to the **WHERE** clause of the query sent to get notable events.

The example of the sent query is as follows: 
    
    
    (`get_notable_index` OR `get_sequenced_index`) | eval `get_event_id_meval`,
    rule_id=event_id | tags outputfield=tag | `mvappend_field(tag,orig_tag)` |
    `notable_xref_lookup` | `get_correlations` | `get_current_status` | `get_owner`
    | `get_urgency` | typer | where (urgency="medium" AND urgency="low") AND
    (status_label="Unassigned" OR status_label="New")  | tail 50 | fields *
    

For example, if `Query Filter = isTesting = True`, then the query appears as follows:
    
    
    search (`get_notable_index` OR `get_sequenced_index`) | eval epoch=_time | eval
    `get_event_id_meval`,rule_id=event_id | tags outputfield=tag |
    `mvappend_field(tag,orig_tag)` | `notable_xref_lookup` | `get_correlations` |
    `get_current_status` | `get_owner` | `get_urgency` | typer | where
    (urgency!="informational" AND urgency!="low" **AND isTesting = "True"**) |
    fields *
    

#### Connector rules

The Splunk ES connector uses dynamic list and blocklist (`whitelist` and `blacklist`). The connector uses the `search_name` field from the event to compare against the dynamic list.

#### Connector event
    
    
    [{
        "indicator": "2012/06/29_21:50", 
        "tlp": "TLP:RED", 
        "itype": "mal_url", 
        "severity": "very-high", 
        "classification": "public", 
        "detail": "", 
        "confidence": 50, 
        "actor": "", 
        "feed_name": "import", 
        "source": "admin", 
        "feed_site_netloc": "localhost", 
        "campaign": "", 
        "type": "url", 
        "id": "anomali:indicator-578a9be5-0e03-4ec0-940d-4b1842f40fd0", 
        "date_last": "2020-07-15 08:12:07 AM",
    "Url": "indicator"
      },{
        "indicator": "2010/12/19_16:35", 
        "tlp": "TLP:RED", 
        "itype": "mal_url", 
        "severity": "very-high", 
        "classification": "public", 
        "detail": "", 
        "confidence": 50, 
        "actor": "", 
        "feed_name": "import", 
        "source": "admin", 
        "feed_site_netloc": "localhost", 
        "campaign": "", 
        "type": "url", 
        "id": "anomali:indicator-52cadd07-330a-45fd-962f-32e22d36a89a", 
        "date_last": "2020-07-15 08:12:07 AM"
      }]
    

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Sync Splunk ES Closed Events

Synchronizes closed Splunk ES notable events and Google SecOps alerts.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | https://`IP`:8089 | Yes | Server address of the Splunk instance.  
Username | String | N/A | No | Username of the Splunk account.  
Password | Password | N/A | No | Password of the Splunk account.  
API Token | Password | N/A | Yes | Splunk API token. API token has priority over other authentication methods, when this field is not empty.  
Max Hours Backwards | Integer | 24 | Yes | Specify how many hours backwards to synchronize statuses. Default: 24 hours.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Splunk server is valid.  
  
### Sync Splunk ES Comments

This job will synchronize comments in Splunk ES events and Google SecOps cases.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | https://`IP`:8089 | Yes | Server address of the Splunk instance.  
Username | String | N/A | No | Username of the Splunk account.  
Password | Password | N/A | No | Password of the Splunk account.  
API Token | Password | N/A | Yes | Splunk API token. API token has priority over other authentication methods, when this field is not empty.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Splunk server is valid.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
