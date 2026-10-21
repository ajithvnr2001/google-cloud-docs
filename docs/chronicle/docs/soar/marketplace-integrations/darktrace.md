---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/darktrace/
title: Darktrace \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:45.682328+00:00
---

# Darktrace  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/darktrace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Darktrace

This document describes how to integrate Darktrace with Google Security Operations.

## Configure Darktrace integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{{api root}} | Yes | Darktrace API root  
API Token | String | N/A | Yes | Darktrace API token  
API Private Token | Password | N/A | Yes | Darktrace API private token  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Darktrace server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

  1. Perform enrichment actions
  2. Perform ingestion of the model breaches
  3. Perform triaging action (Update Model Breach Status)



## Actions

### Add Comment To Model Breach

Add a comment to model breach in Darktrace.

#### Parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Model Breach ID | String | N/A | Yes | Specify the ID of the model breach to which you want to add a comment.  
Comment | String | N/A | Yes | Specify the comment for the model breach.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "jsonrpc": "2.0",
        "id": "string",
        "result": {
            "status": "done"
        }
    }
    

##### Case Wall

Result Type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If returned information (is_success=true):_ "Successfully added a comment to the alert with ID {id} in Darktrace." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Comment To Model Breach". Reason: {0}''.format(error.Stacktrace)" _If alert is not found:_ "Add Comment To Model Breach". Reason: model breach with ID {model breach id} wasn't found in Darktrace. Please check the spelling." | General  
  
### Execute Custom Search

Execute custom search in Darktrace.

#### Parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query that needs to be executed.  
Time Frame | DDL | Last Hour Possible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Alert Time Till Now
  * 5 Minutes Around Alert Time
  * 30 Minutes Around Alert Time
  * 1 Hour Around Alert Time
  * Custom

| No | Specify a timeframe for the results. If "Custom" is selected, you also need to provide the "Start Time" parameter. If "Alert Time Till Now" is selected, the action uses start time of the alert as start time for the search and end time is current time. If "30 Minutes Around Alert Time" is selected, the action searches the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened. Same idea applies to the "1 Hour Around Alert Time" and "5 Minutes Around Alert Time" values.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Format: ISO 8601  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

The JSON result can be empty.
    
    
    "hits": [
                {
                    "_index": "logstash-vmprobe-2022.03.11",
                    "_type": "doc",
                    "_id": "AX95xiUpb8-BQBTWRSyh",
                    "_score": null,
                    "_source": {
                        "@fields": {
                            "certificate_not_valid_before": 1635062830,
                            "source_port": 10002,
                            "certificate_issuer": "CN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE",
                            "certificate_sig_alg": "sha256WithRSAEncryption",
                            "certificate_not_valid_after": 1669362596,
                            "fid": "FGxEJX3qjVRTz4JDai01",
                            "certificate_key_length": 2048,
                            "certificate_key_type": "rsa",
                            "san_dns": [
                                "*.checkpoint.com",
                                "checkpoint.com"
                            ],
                            "epochdate": 1647015490.107213,
                            "certificate_key_alg": "rsaEncryption",
                            "certificate_subject": "CN=*.checkpoint.com",
                            "source_ip": "203.0.113.1",
                            "certificate_exponent": "65537",
                            "dest_port": 443,
                            "dest_ip": "198.51.100.255",
                            "uid": "CFrBBX1QNkXIXb5QI301",
                            "certificate_version": 3,
                            "certificate_serial": "7796FB90CCBDA12C831F6DB5",
                            "basic_constraints_ca": false
                        },
                        "@type": "x509",
                        "@timestamp": "2022-03-11T16:18:10",
                        "@message": "1647015490.1072\tCFrBBX1QNkXIXb5QI301\t203.0.113.1\t10002\t203.0.113.1\t443\t-\t-\t1635062830\tCN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE\tsha256WithRSAEncryption\t1669362596\tFGxEJX3qjVRTz4JDai01\t2048\trsa\t[*.checkpoint.com,checkpoint.com]\trsaEncryption\tCN=*.checkpoint.com\t65537\t3\t7796FB90CCBDA12C831F6DB5\tfalse",
                        "@darktrace_probe": "1"
                    },
                    "sort": [
                        1647015490000
                    ]
                }
            ]
    
    

##### Case Wall

Result Type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If found at least one result (is_success = true):_ "Successfully returned results for the query "{query}" in Darktrace. _If no results are found (is_success=true):_ "No results were found for the query "{query}" in Darktrace." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Execute Custom Search". Reason: {0}''.format(error.Stacktrace) _If an error is reported:_ "Error executing action "Execute Custom Search". Reason: {0}''.format(error) | General  
  
#### Description

Enrich entities using information from Darktrace. Supported entities: IP, Hostname, MacAddress, URL.

**Note:** This action extracts the domain part out of the URL entities.

#### Parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Fetch Connection Data | Checkbox | Checked | No | If enabled, the action returns additional information about connections related to the internal endpoints of Darktrace.  
Max Hours Backwards | Integer | 24 | No | Specify the number of hours back that the action needs to fetch connection data.  
Create Endpoint Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing information about the internal endpoints of Darktrace.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON Result - Result for Endpoints
    
    
    {
        "id": 93,
        "macaddress": "ab:cd:ef:01:23",
        "vendor": "Example, Inc.",
        "ip": "198.51.100.1",
        "ips": [
            {
                "ip": "198.51.100.1",
                "timems": 1617174000000,
                "time": "2021-03-31 07:00:00",
                "sid": 5
            }
        ],
        "did": 93,
        "sid": 5,
        "hostname": "example",
        "time": 1614183727000,
        "endtime": 1617175508000,
        "os": "Windows NT kernel",
        "typename": "server",
        "typelabel": "Server"
    }
    

#### JSON Result - for External Entities (URL)
    
    
    {
        "hostname": "example.com",
        "firsttime": 1614091840000,
        "devices": [
            {
                "did": 90,
                "macaddress": "ab:cd:ef:01:23",
                "vendor": "Example, Inc.",
                "ip": "198.51.100.1",
                "ips": [
                    {
                        "ip": "198.51.100.1",
                        "timems": 1617174000000,
                        "time": "2021-03-31 07:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "example.hostname",
                "firstSeen": 1614183620000,
                "lastSeen": 1617175580000,
                "os": "Windows NT kernel",
                "typename": "desktop",
                "typelabel": "Desktop"
            },
            {
                "did": 98,
                "macaddress": "ab:cd:ef:01:23",
                "vendor": "VMware, Inc.",
                "ip": "198.51.100.2",
                "ips": [
                    {
                        "ip": "198.51.100.2",
                        "timems": 1617174000000,
                        "time": "2021-03-31 07:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "example.hostname",
                "firstSeen": 1614184533000,
                "lastSeen": 1617174510000,
                "os": "Windows NT kernel",
                "typename": "desktop",
                "typelabel": "Desktop"
            },
            {
                "did": 107,
                "macaddress": "ab:cd:ef:01:23",
                "vendor": "Example, Inc.",
                "ip": "198.51.100.3",
                "ips": [
                    {
                        "ip": "198.51.100.3",
                        "timems": 1617159600000,
                        "time": "2021-03-31 03:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "example.hostname",
                "firstSeen": 1616749011000,
                "lastSeen": 1617161974000,
                "os": "Windows NT kernel",
                "typename": "desktop",
                "typelabel": "Desktop"
            }
        ],
        "ips": [
            {
                "ip": "198.51.100.1",
                "firsttime": 1615895887000,
                "lasttime": 1616722320000
            },
            {
                "ip": "198.51.100.2",
                "firsttime": 1616741572000,
                "lasttime": 1617016188000
            },
            {
                "ip": "198.51.100.3",
                "firsttime": 1616722488000,
                "lasttime": 1617163627000
            },
            {
                "ip": "198.51.100.4",
                "firsttime": 1616723208000,
                "lasttime": 1617163387000
            },
            {
                "ip": "198.51.100.5",
                "firsttime": 1616515190000,
                "lasttime": 1616517828000
            },
            {
                "ip": "198.51.100.6",
                "firsttime": 1616715466000,
                "lasttime": 1616721229000
            },
            {
                "ip": "198.51.100.7",
                "firsttime": 1616721408000,
                "lasttime": 1616721949000
            },
            {
                "ip": "198.51.100.8",
                "firsttime": 1614417878000,
                "lasttime": 1616715288000
            },
            {
                "ip": "198.51.100.9",
                "firsttime": 1614374675000,
                "lasttime": 1616517837000
            },
            {
                "ip": "198.51.100.10",
                "firsttime": 1616680696000,
                "lasttime": 1616722129000
            },
            {
                "ip": "198.51.100.11",
                "firsttime": 1615388011000,
                "lasttime": 1616667243000
            },
            {
                "ip": "198.51.100.12",
                "firsttime": 1616516000000,
                "lasttime": 1616516000000
            },
            {
                "ip": "198.51.100.13",
                "firsttime": 1617016021000,
                "lasttime": 1617016021000
            }
        ],
        "locations": [
            {
                "latitude": 37,
                "longitude": -122,
                "country": "United States",
                "city": "Mountain View"
            },
            {
                "latitude": 37,
                "longitude": -97,
                "country": "United States",
                "city": ""
            },
            {
                "latitude": 51,
                "longitude": 0,
                "country": "United Kingdom",
                "city": "London"
            }
        ]
    }
    

#### JSON Result - for External Entities (IP)
    
    
    {
        "ip": "198.51.100.255",
        "firsttime": 1617044992000,
        "country": "India",
        "asn": "Example Ltd.",
        "city": "Kolkata",
        "region": "Asia",
        "name": "",
        "longitude": 88.37,
        "latitude": 22.56,
        "ipage": 1209600,
        "iptime": "2021-03-17 08:15:03",
        "devices": [
            {
                "did": 93,
                "macaddress": "ab:cd:ef:01:23",
                "vendor": "Example, Inc.",
                "ip": "198.51.100.255",
                "ips": [
                    {
                        "ip": "198.51.100.255",
                        "timems": 1617174000000,
                        "time": "2021-03-31 07:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "example.hostname",
                "firstSeen": 1614183727000,
                "lastSeen": 1617175508000,
                "os": "Windows NT kernel",
                "typename": "server",
                "typelabel": "Server"
            }
        ]
    }
    

##### Entity Enrichment for Endpoints

Enrichment Field Name | Logic - When to apply  
---|---  
macaddress | When available in JSON  
id | When available in JSON  
ip | When available in JSON  
did | When available in JSON  
os | When available in JSON  
hostname | When available in JSON  
typelabel | When available in JSON  
devicelabel | When available in JSON  
  
##### Entity Enrichment for External Entities

Enrichment Field Name | Logic - When to apply  
---|---  
ip | When available in JSON  
country | When available in JSON  
asn | When available in JSON  
city | When available in JSON  
region | When available in JSON  
hostname | When available in JSON  
name | When available in JSON  
longitude | When available in JSON  
latitude | When available in JSON  
count_related_devices | When available in JSON  
associated_ips | When available in JSON  
associated_countries | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If enriched some entities (is_success = true):_ "Successfully enriched the following entities using Darktrace:\n".format(entity.identifier) _If didn't enrich some entities (is_success = true):_ "Action wasn't able to enrich the following entities using Darktrace:\n".format(entity.identifier) _If didn't enrich all entities (is_success = false):_ "No entities were enriched". **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Entity Table |  | Entity  
Case Wall Table (External Entity) | **Table Name:** {entity.identifier}: Interacted Devices **Table Column:**

  * MacAddress 
  * Vendor
  * IP 
  * Hostname
  * OS 
  * Type 

| General  
Case Wall Table (Internal Entity) Connection Data is enabled. | **Table Name:** {entity.identifier}: Connection Data  **Table Column:**

  * Type - (can be "External Domain"/"Internal Device")
  * Domain - (externalDomains/domain) I
  * P Address - (devices/ip) 
  * Mac Address - devices/macaddress

| General  
  
### List Endpoint Events

List latest events related to the endpoint in Darktrace. Supported entities: IP, Hostname, MacAddress.

**Note:** Events are returned in the UTC timezone.

#### Parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Event Type | CSV | connection,  
unusualconnection,  
notice | Yes | Specify a comma-separated list of event types that they want to return. Possible values: connection, unusualconnection, newconnection, notice, devicehistory, modelbreach  
Time Frame | DDL | Last Hour Possible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| Yes | Specify a timeframe for the search. If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the search. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Format: ISO 8601  
Max Events To Return | Integer | 50 | No | Specify the number of events to return per event type.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON Result
    
    
    {
        {entity}: {
    "{event_type}": [{`EVENTS`}]
    "{event_type_2}": [{`EVENTS_2`}]}
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for at least one event type (is_success = true):_ "Successfully returned events related to the following endpoints from Darktrace: {entity.identifier}". _If data is not available for one endpoint or endpoint isn't found (is_success=true):_ "Action wasn't able to find any events related to the following endpoints from Darktrace: {entity.identifier}". _If data is not available for all endpoint or all endpoints aren't found (is_success=false):_ "No events were found for the provided endpoints.". **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Endpoint Events". Reason: {0}''.format(error.Stacktrace) _If the "Start Time" parameter is empty and the "Time Frame" parameter is set to "Custom":_ "Error executing action "List Endpoint Events". Reason: "Start Time" should be provided, when "Custom" is selected in "Time Frame" parameter." _If at least one value in the "Event Type" parameter is invalid:_ "Error executing action "List Endpoint Events". Reason: Invalid values was provided in the parameter "Event Type". Possible values: connection, unusualconnection, newconnection, notice, devicehistory, modelbreach." | General  
Case Wall Table(connection type) | **Table Name: {entity.identifier}:** Connection Events**Table Columns:**

  * Direction
  * Source Port
  * Destination Port
  * Protocol
  * Application
  * Time
  * Destination
  * Status

| General  
Case Wall Table(unusualconnection type) | **Table Name: {entity.identifier}:** Unusual Connection Events **Table Columns:**

  * Direction
  * Source Port
  * Destination Port
  * Protocol
  * Application 
  * Time
  * Destination
  * Status
  * Info 

| General  
Case Wall Table (newconnection type) | **Table Name: {entity.identifier}:** New Connection Events **Table Columns:**

  * Direction
  * Source Port
  * Destination Port
  * Protocol
  * Application
  * Time
  * Destination
  * Status
  * Info

| General  
Case Wall Table (notice type) | **Table Name: {entity.identifier}:** Notice Events **Table Columns:**

  * Direction
  * Destination Port
  * Type
  * Time
  * Destination
  * Message 

| General  
Case Wall Table(device history type) | **Table Name: {entity.identifier}:** Device History Events**Table Columns:**

  * Name
  * Value
  * Reason
  * Time

| General  
Case Wall Table (modelbreach type) | **Table Name: {entity,identifier}:** Model Breach Events **Table Columns:**

  * Name
  * State
  * Score
  * Time
  * Active 

| General  
  
### List Similar Devices

List similar devices to the endpoint in Darktrace.

#### Parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Max Devices To Return | Integer | 50 | No | Specify the number of devices to return per entity.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname
  * Mac Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "did": 143,
            "score": 100,
            "macaddress": "00:50:56:a2:1a:08",
            "vendor": "Example, Inc.",
            "ip": "198.51.100.255",
            "ips": [
                {
                    "ip": "198.51.100.255",
                    "timems": 1647273600000,
                    "time": "2022-03-14 16:00:00",
                    "sid": 5
                }
            ],
            "sid": 5,
            "firstSeen": 1640274511000,
            "lastSeen": 1647277180000,
            "typename": "server",
            "typelabel": "Server"
        }
    ]
    

##### Case Wall

Result Type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for at least one event type (is_success = true):_ "Successfully returned similar devices for the following endpoints from Darktrace: {entity.identifier}" _If data is not available for one endpoint or endpoint isn't found (is_success=true):_ print "Action wasn't able to find any similar devices for the following endpoints from Darktrace: {entity.identifier}" _If data is not available for all endpoints or all endpoints aren't found (is_success=false):_ "No similar devices were found for the provided endpoints." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Similar Devices". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** entity.identfier  **Table Columns:**

  * IP Address - ip
  * Mac Address - macaddress
  * Hostname - hostname Type - typename
  * OS - os
  * First Seen - firstSeen
  * Last Seen - lastSeen

| General  
  
### Ping

Test connectivity to Darktrace with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Darktrace server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Darktrace server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Model Breach Status

Update model breach status in Darktrace.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Status | DDL | Acknowledged Possible values:

  * Acknowledged
  * Unacknowledged

| Yes | Specify the status to set for the model breach.  
Model Breach ID | String | N/A | Yes | Specify the ID of the model breach, for which you want to update status.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success = true):_ "Successfully updated status of the model breach "{id}" to "{status}" in Darktrace.". _If status is already applied (is_success=true):_ "Model breach "{id}" already has status "{status}" in Darktrace." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Model Breach Status". Reason: {0}''.format(error.Stacktrace) _If the 404 status code or error is reported:_ "Error executing action "Update Model Breach Status". Reason: model breach "{id}" wasn't found in Darktrace.' | General  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Darktrace — Model Breaches Connector

Pull information about model breaches and their related connection events from Darktrace.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
Product Field Name | **Required** The source field name to retrieve the Product Field name.  
Event Field Name | **Required** The source field used to retrieve the event field name. The default value is `eventType`.  
Environment Field Name | _Optional_ The field that stores the environment name. If the environment field isn't found, the environment is set to the default environment. The default value is `""`.  
Environment Regex Pattern | _Optional_ A regular expression pattern to run on the value in the **Environment Field Name**. The default value `.*` is used to catch all and return the value unchanged. Use this parameter to transform the environment value using regular expression logic. If the pattern or the environment value is null or empty, the default environment is used.  
PythonProcessTimeout | **Required** The timeout limit, in seconds, for the Python process running the current script. The default value is `180`.  
API Root | **Required** The API root of the Darktrace instance.  
API Token | **Required** The Darktrace API token.  
API Private Token | **Required** The Darktrace API private token.  
Verify SSL | _Optional_ When checked, verifies the SSL certificate for the connection to the Darktrace server when enabled. Enabled by default.  
Lowest Model Breach Score To Fetch | _Optional_ The minimum model breach score to fetch. The maximum value is `100`. The default value is `0`.  
Lowest Priority To Fetch | _Optional_ The minimum priority used to fetch model breaches. Provided as an integer. `1`, `2`, `3` \- Informational, `4` \- Suspicious, `5` \- Critical.  
Max Hours Backwards | _Optional_ The amount of hours to fetch the model breaches from. The default value is `1`.  
Max Model Breaches To Fetch | _Optional_ The number of model breaches to process per-connector iteration. The maximum value is `1000`. The default value is `10`.  
Use whitelist as a blacklist | **Required** If checked, the allowlist is used as a blocklist. Checked by default.  
Proxy Server Address | _Optional_ The address of the proxy server to use.  
Proxy Username | _Optional_ The username for proxy authentication.  
Proxy Password | _Optional_ The password for proxy authentication.  
Behavior Visibility | _Optional_ A comma-separated list of behavior visibility values to ingest. Possible values: 
* `Critical`
* `Suspicious`
* `Compliance`
* `Informational`  
Padding Time | _Optional_ The number of hours used as padding. The maximum value is `100`.  
  
#### Connector rules

The connector supports Proxy.

#### Connector events

The Model Breaches connector has two types of events: one is based on model breach and the other on related events.

The example of an event based on model breach is as follows:
    
    
    [
        {
            "creationTime": 1617101902000,
            "commentCount": 0,
            "pbid": 59,
            "time": 1617101836000,
            "model": {
                "then": {
                    "name": "Compliance::ExampleService",
                    "pid": 88,
                    "phid": 809,
                    "uuid": "2eb05e89-f401-4c9c-9324-dc63a504737d",
                    "logic": {
                        "data": [
                            {
                                "cid": 1670,
                                "weight": 2
                            },
                            {
                                "cid": 1669,
                                "weight": 1
                            },
                            {
                                "cid": 1668,
                                "weight": 1
                            },
                            {
                                "cid": 1667,
                                "weight": 1
                            },
                            {
                                "cid": 1666,
                                "weight": 1
                            }
                        ],
                        "targetScore": 2,
                        "type": "weightedComponentList",
                        "version": 1
                    },
                    "throttle": 86400,
                    "sharedEndpoints": false,
                    "actions": {
                        "alert": true,
                        "antigena": {},
                        "breach": true,
                        "model": true,
                        "setPriority": false,
                        "setTag": false,
                        "setType": false
                    },
                    "tags": [],
                    "interval": 3600,
                    "sequenced": false,
                    "active": true,
                    "modified": "2021-02-15 00:50:10",
                    "activeTimes": {
                        "devices": {},
                        "tags": {},
                        "type": "exclusions",
                        "version": 2
                    },
                    "priority": 1,
                    "autoUpdatable": true,
                    "autoUpdate": true,
                    "autoSuppress": true,
                    "description": "A device is making peer-to-peer ExampleService connections. ExampleService is used for large file transfers and while it has legitimate uses, it is commonly associated with the sharing of copyright protected and other unwanted data.\\n\\nAction: Investigate the volumes of data being transferred by the device and its other activities as this is a strong indication of a compliance issue.",
                    "behaviour": "decreasing",
                    "created": {
                        "by": "Unknown"
                    },
                    "edited": {
                        "by": "System"
                    },
                    "version": 19
                },
                "now": {
                    "category" : "Suspicious",
                    "name": "Compliance::ExampleService",
                    "pid": 88,
                    "phid": 809,
                    "uuid": "2eb05e89-f401-4c9c-9324-dc63a504737d",
                    "logic": {
                        "data": [
                            {
                                "cid": 1670,
                                "weight": 2
                            },
                            {
                                "cid": 1669,
                                "weight": 1
                            },
                            {
                                "cid": 1668,
                                "weight": 1
                            },
                            {
                                "cid": 1667,
                                "weight": 1
                            },
                            {
                                "cid": 1666,
                                "weight": 1
                            }
                        ],
                        "targetScore": 2,
                        "type": "weightedComponentList",
                        "version": 1
                    },
                    "throttle": 86400,
                    "sharedEndpoints": false,
                    "actions": {
                        "alert": true,
                        "antigena": {},
                        "breach": true,
                        "model": true,
                        "setPriority": false,
                        "setTag": false,
                        "setType": false
                    },
                    "tags": [],
                    "interval": 3600,
                    "sequenced": false,
                    "active": true,
                    "modified": "2021-02-15 00:50:10",
                    "activeTimes": {
                        "devices": {},
                        "tags": {},
                        "type": "exclusions",
                        "version": 2
                    },
                    "priority": 1,
                    "autoUpdatable": true,
                    "autoUpdate": true,
                    "autoSuppress": true,
                    "description": "A device is making peer-to-peer ExampleService connections. ExampleService is used for large file transfers and while it has legitimate uses, it is commonly associated with the sharing of copyright protected and other unwanted data.\\n\\nAction: Investigate the volumes of data being transferred by the device and its other activities as this is a strong indication of a compliance issue.",
                    "behaviour": "decreasing",
                    "created": {
                        "by": "Unknown"
                    },
                    "edited": {
                        "by": "System"
                    },
                    "message": "Increasing cooldown",
                    "version": 19
                }
            },
            "score": 0.419,
            "device": {
                "did": 98,
                "macaddress": "ab:cd:ef:01:23:45",
                "vendor": "Example, Inc.",
                "ip": "203.0.113.1",
                "ips": [
                    {
                        "ip": "203.0.113.1",
                        "timems": 1617105600000,
                        "time": "2021-03-30 12:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "host2.example.local",
                "firstSeen": 1614184533000,
                "lastSeen": 1617105980000,
                "typename": "desktop",
                "typelabel": "Desktop"
            }
        }
    ]
    
    

The example of an event based on related events is as follows:
    
    
        {
            "time": "2021-03-29 20:19:05",
            "timems": 1617049145655,
            "action": "connection",
            "eventType": "connection",
            "uid": "CfB8nO1tC9APLM7601",
            "sdid": 93,
            "port": 6881,
            "sourcePort": 48663,
            "destinationPort": 6881,
            "info": "An unusual connection compared with similar devices externally on port 6881",
            "direction": "out",
            "applicationprotocol": "Unknown",
            "protocol": "UDP",
            "sourceDevice": {
                "id": 93,
                "did": 93,
                "macaddress": "ab:cd:ef:01:23:45",
                "ip": "203.0.113.1",
                "ips": [
                    {
                        "ip": "203.0.113.1",
                        "timems": 1617102000000,
                        "time": "2021-03-30 11:00:00",
                        "sid": 5
                    }
                ],
                "sid": 5,
                "hostname": "host1",
                "time": "1614183727000",
                "os": "Windows NT kernel",
                "typename": "server",
                "typelabel": "Server"
            },
            "destinationDevice": {
                "longitude": 88.37,
                "latitude": 22.56,
                "city": "Kolkata",
                "country": "India",
                "countrycode": "IN",
                "asn": "Example Ltd.",
                "region": "Asia",
                "ip": "198.51.100.1",
                "ippopularity": "0",
                "connectionippopularity": "0"
            },
            "source": "host1",
            "destination": "198.51.100.1"
        }
    

### Darktrace — AI Incident Events Connector

Pull information about the AI incident events from Darktrace.

**Note:** The dynamic list works with the `title` parameter.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
Product Field Name | **Required** The source field used to retrieve the product field name.  
Event Field Name | **Required** The source field used to retrieve event field name. The default value is `data_type`.  
Environment Field Name | _Optional_ The field that stores the environment name. If this field is missing, the default environment is used. The default value is `""`.  
Environment Regex Pattern | _Optional_ A regular expression applied to the value in the `Environment Field Name` field. The default value is `.*`. Use this pattern to manipulate the environment value. If the pattern or the environment value is null or empty, the default environment is used.  
PythonProcessTimeout | **Required** The timeout (in seconds) for the Python process running the current script. The default value is `180`.  
API Root | **Required** The API root URL of the Darktrace instance.  
API Token | **Required** The Darktrace API token.  
API Private Token | **Required** The Darktrace API private token.  
Verify SSL | _Optional_ When checked, verifies the SSL certificate for the connection to the Darktrace server when enabled. Enabled by default.  
Lowest AI Incident Score To Fetch | **Required** The minimum AI incident score to fetch. The maximum value is `100`. The default value is `0`.  
Max Hours Backwards | _Optional_ The number of hours to look back when fetching model breaches.  The default value is `1`.  
Max AI Incidents To Fetch | _Optional_ The number of AI incidents to process per connector iteration. The maximum value is `100`. The default value is `10`.  
Use dynamic list as a blocklist | _Optional_ When enabled, the dynamic list is used as a blocklist.  
Enabled by default.  
Proxy Server Address | _Optional_ The address of the proxy server to use.  
Proxy Username | _Optional_ The username for proxy authentication.  
Proxy Password | _Optional_ The password for proxy authentication.  
  
#### Connector rules

The connector supports Proxy.

#### Connector events

The AI Incident Events connector has two types of events: one is based on incident and the other on events.

The example of an event based on incident is as follows:
    
    
       {
           "summariser": "FluxingSummary",
           "acknowledged": false,
           "pinned": false,
           "createdAt": 1680472869315,
           "attackPhases": [
               2
           ],
           "mitreTactics": [
               "command-and-control"
           ],
           "title": "Multiple DNS Requests for Algorithmically Generated Domains",
           "id": "7a519f45-7268-45f8-98be-c3c5395aa1d2",
           "children": [
               "7a519f45-7268-45f8-98be-c3c5395aa1d2"
           ],
           "category": "critical",
           "currentGroup": "g7a519f45-7268-45f8-98be-c3c5395aa1d2",
           "groupCategory": "suspicious",
           "groupScore": 12.939280403280277,
           "groupPreviousGroups": [],
           "activityId": "da39a3ee",
           "groupingIds": [
               "b6692ea5"
           ],
           "groupByActivity": false,
           "userTriggered": false,
           "externalTriggered": false,
           "aiaScore": 64.84360067503793,
           "summary": "The device testing label has been detected making large numbers of DNS requests for domains which appear to have been created using a domain generation algorithm (DGA).\n\nThis technique is used by multiple malware families to obfuscate the location of their command and control servers, since active domains can be frequently altered, with their DNS lookups being hidden amongst multiple similar failed queries.\n\nThe security team may therefore wish to investigate the device for further signs of compromise, and remove any infections that may be present.",
           "periods": [
               {
                   "start": 1680472700788,
                   "end": 1680472781120
               }
           ],
           "breachDevices": [
               {
                   "identifier": "testing label",
                   "hostname": "example.example",
                   "ip": "192.0.2.1",
                   "mac": "ab:cd:ef:01:23:45",
                   "subnet": null,
                   "did": 33,
                   "sid": 3
               }
           ],
           "relatedBreaches": [
               {
                   "modelName": "Compromise / Domain Fluxing",
                   "pbid": 10556,
                   "threatScore": 65.0,
                   "timestamp": 1680472731000
               }
           ]
       }
    

The example of an event based on events is as follows:
    
    
                   {
                       "data_type": "Event",
                       "header": "Breaching Device",
                       "device_identifier": "example.example",
                       "device_hostname": "example.example",
                       "device_ip": "192.0.2.1",
                       "device_mac": "ab:cd:ef:01:23:45",
                       "device_subnet": null,
                       "device_did": 19,
                       "device_sid": 3,
                       "createdAt": "1675766657442"
                   }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
