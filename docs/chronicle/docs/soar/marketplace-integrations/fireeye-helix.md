---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-helix/
title: FireEye Helix \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:14.763601+00:00
---

# FireEye Helix  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-helix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye Helix

**Important:** FireEye and McAfee Enterprise merged and became Trelix. FireEye Helix was renamed to Trellix Helix.

This document describes how to integrate FireEye Helix with Google Security Operations.

## Use Cases

  1. Ingest Trellix Helix alerts and use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform remediation actions like adding entities to a block list



## Product Permission

Generate a token and use it as a part of a special header for every request.
    
    
    GET /helix/id/hexqsj477/api/v3/appliances/health HTTP/1.1
    Host: helix.eu.fireeye.com
    x-fireeye-api-key: xxxxxxxxxxxxxxxxxxxxx
    

### How to generate API Token

  1. Navigate to **Identity Access Management**.

![Trellix Helix
console](https://docs.cloud.google.com/static/chronicle/images/integrations/fireeye-helix-identity-access-management.png)

  2. Go to **API Keys** and click **Create API Key**.

![API Keys tab in FireEye
Helix](https://docs.cloud.google.com/static/chronicle/images/integrations/fireeye-helix-api-keys.png)

  3. Set "API Key Name", "Expiration Date", "Products" and press "Next".

![Create API Key
pane](https://docs.cloud.google.com/static/chronicle/images/integrations/fireeye-helix-create-api-key.png)

  4. Add the following permissions for integration:

     * tap.alert.suppressions.add
     * tap.alert.suppressions.browse
     * tap.alert.suppressions.edit
     * tap.alert.suppressions.read
     * tap.alerts.browse
     * tap.alerts.edit
     * tap.alerts.read
     * tap.appliances.browse
     * tap.appliances.read
     * tap.archivesearch.add
     * tap.archivesearch.browse
     * tap.assets.browse
     * tap.assets.read
     * tap.lists.add
     * tap.lists.browse
     * tap.lists.edit
     * tap.lists.read
     * tap.search.browse
     * tap.search.regex
  5. Copy API Token.

![API Token
localization](https://docs.cloud.google.com/static/chronicle/images/integrations/fireeye-helix-copy-token.png)




## Configure FireEye HELIX integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://helix.eu.fireeye.com/helix/id/{id}/ | Yes | API Root of the Trellix Helix instance.  
API Token | String | N/A | No | The API token of the FireEye Helix account.  
Client ID | String | N/A | No | Client ID for Trellix IAM OAuth authentication.  
Client Secret | Password | N/A | No | Client Secret for Trellix IAM OAuth authentication.  
Scope | String | xdr.alr.r xdr.org.adm | No | Space separated scopes for Trellix IAM OAuth authentication.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the Trellix Helix server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trellix Helix with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ Print "Successfully connected to the Trellix Helix server with the provided connection parameters!"**The action should fail and stop a playbook execution:**_If critical error, like wrong credentials or lost connectivity:_ Print "Failed to connect to the Trellix Helix server! Error is {0}".format(exception.stacktrace) | General  
  
### Suppress Alert

#### Description

Duration is in minutes. We need to take the current time and add to it the relevant time. The created value will be used in the "endDate" parameter of the request.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | Integer | N/A | Yes | Specify ID of the Alert that needs to be suppressed in Trellix Helix.  
Duration | Integer | N/A | Yes | Specify for how long the Alert should be suppressed in minutes.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully suppressed the alert with ID {ID} for {duration} minutes in Trellix Helix."****_If Alert ID not found:_ Print "Action wasn't able to suppress the alert with ID {ID} for {duration} minutes in Trellix Helix. Reason: Alert with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Suppress Alert". Reason: {0}''.format(error.Stacktrace) | General  
  
### Close Alert

#### Description

Close Alert in Trellix Helix.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | Integer | N/A | Yes | Specify ID of the Alert that needs to be closed in Trellix Helix.  
Revision Note | String | N/A | No | Specify revision note for the alert.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully closed the alert with ID {ID} in Trellix Helix."****_If Alert ID not found:_ Print "Action wasn't able to close the alert with ID {ID} in Trellix Helix. Reason: Alert with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Close Alert". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Note To Alert

#### Description

Add a Note to Alert in Trellix Helix.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | Integer | N/A | Yes | Specify ID of the Alert that needs to be suppressed in Trellix Helix.  
Note | Integer | N/A | Yes | Specify note for the alert.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully added a note to the alert with ID {ID} in Trellix Helix."****_If Alert ID not found:_ Print "Action wasn't able to add a note to the alert with ID {ID} in Trellix Helix. Reason: Alert with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Add Note To Alert". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Lists

#### Description

Return information about Trellix Helix lists.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | No | Specify name filter.  
Short Name | String | N/A | No | Specify short name filter.  
Active | Checkbox | False | No | Specify, whether action should only return active lists.  
Internal | Checkbox | False | No | Specify, whether action should only return internal lists.  
Protected | Checkbox | False | No | Specify, whether action should only return protected lists.  
Sort By | DDL | NamePossible values:NameShort NameCreated At | No | Specify which parameter should be used for sorting results.  
Sort Order | DDL | AscendingPossible values:AscendingDescending | No | Specify the sorting order for the results.  
Max Lists To Return | Integer | 100 | No | Specify how many lists to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "results": [
            {
                "id": 14387,
                "short_name": "siemplify_atest",
                "item_count": 0,
                "types": [],
                "created_by": {
                    "id": "0b48dde7-5c81-4899-978d-793540861a42",
                    "avatar": "https://secure.gravatar.com/avatar/0feb076e8da5a3dff2b62cf8e53525cd",
                    "name": "xxxxxxxx",
                    "username": "xxx.xxxxxx@xxxxxxxxx.xx",
                    "primary_email": "xxx.xxxxxx@xxxxxxxxx.xx"
                },
                "updated_by": {
                    "id": "0b48dde7-5c81-4899-978d-793540861a42",
                    "avatar": "https://secure.gravatar.com/avatar/0feb076e8da5a3dff2b62cf8e53525cd",
                    "name": "xxxxxxxx",
                    "username": "xxx.xxxxxx@xxxxxxxxx.xx",
                    "primary_email": "xxx.xxxxxx@xxxxxxxxx.xx"
                },
                "created_at": "2020-08-11T07:36:24.725168Z",
                "updated_at": "2020-08-11T07:36:24.725168Z",
                "name": "xxxxxxxx xxx",
                "type": "default",
                "description": "",
                "usage": [],
                "is_internal": false,
                "is_protected": false,
                "is_active": true,
                "hash": ""
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully returned lists from Trellix Helix."****_If no lists were found (is_success=false):_ Print "No lists were found that match the set criteria."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Get Lists". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Name:** "Trellix Helix Lists"**Column:**

  * Name (mapped as name)
  * Short Name (mapped as short_name)
  * Created At (mapped as created_at)
  * Item Count (mapped as item_count)
  * Internal (mapped as is_internal)
  * Active (mapped as is_active)
  * Protected (mapped as is_protected)

| General  
  
### Get List Items

#### Description

Return information about Trellix Helix lists items.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
List Short Name | String | N/A | Yes | Specify the short name of the list.  
Value | String | N/A | No | Specify value filter for the items.  
Type | DDL | ALLPossible Values:  
ALLEmailFQDNIPv4IPv6MD5MISCSHA-1 | No | Specify type filter for the items.  
Sort By | DDL | ValuePossible values:ValueTypeRisk | No | Specify which parameter should be used for sorting results.  
Sort Order | DDL | AscendingPossible values:AscendingDescending | No | Specify the sorting order for the results.  
Max Items To Return | Integer | 100 | No | Specify how many items to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "results": [
            {
                "id": 45404223,
                "value": "xxxxxxxxx.xx",
                "type": "misc",
                "risk": "Low",
                "notes": "",
                "list": 4969
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully returned items of the "{short_name}" list from Trellix Helix."****_If no list was found (is_success=false):_ Print "List with short name "{short_name}" was not found in Trellix Helix."_If no items are in the list (is_success=false):_ Print "No items were found in the list with short name "{short_name}" in Trellix Helix."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Get List Items". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Entities To a List

#### Description

Add Google SecOps entities to the Trellix Helix list.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
List Short Name | String | N/A | No | Specify the short name of the list.  
Risk | DDL | MediumPossible values:LowMediumHighCritical | No | Specify the risk of the items.  
Note | String | N/A | No | Specify notes that should be added to the items.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": 45417477,
        "value": "misc/email/fqdn/ipv4/ipv6/md5/shaa1aa",
        "type": "misc",
        "risk": "Critical",
        "notes": "Asd",
        "list": 14387
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities were added (is_success = true):_  
__Print "Successfully added the following entities to Trellix Helix list with short name "{0}": \n {1}".format(List Short Name, entity.identifier list)****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to add the following entities to the Trellix Helix list with short name '{0}' \n: {1}".format(List Short Name, [entity.identifier])_If no entities were added (is_success=false):_ Print "No entities were added to the list with short name "{short_name}" in Trellix Helix."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Add Entities To a List". Reason: {0}''.format(error.Stacktrace) | General  
  
### Index Search

#### Description

Perform index search in Trellix Helix.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query for the search, for example: srcserver=172.30.202.130  
Time Frame | String | N/A | No | Specify the time frame for the search. Only hours and days are supported. This is the Trellix Helix limitation. Examples of the values:  
7h - 7 hours1d - 1 day  
Max Results To Return | Integer | 100 | No | Specify how many results to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     "results": {
            "hits": {
                "hits": [
                    {
                        "_score": 0.0,
                        "_type": "_doc",
                        "_id": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                        "_source": {
                            "dstusagetype": "cdn",
                            "_eventid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "srcisp": "private ip address lan",
                            "meta_uuid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "srcipv4": "x.x.x.x",
                            "alert_version": "x.x.x.x",
                            "cnchost": [
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx"
                            ],
                            "detect_rulenames": [
                                "fireeye nx alert [malware-object]"
                            ],
                            "dstdomain": "xxxxxxxx.xxx",
                            "dstregion": "california",
                            "meta_ts": "2020-08-13T08:34:12.000Z",
                            "dstipv4": "x.x.x.x",
                            "meta_rule": "fireeye_cms_alert-ss-0.1.4",
                            "alert_product": "web mps",
                            "srcmac": "xx:xx:xx:xx:xx:xx",
                            "eventlog": "malware-object",
                            "eventtype": "ips",
                            "dstcountry": "united states of america",
                            "msr_ruleids": [],
                            "meta_alert_deviceid": "867A65B84172",
                            "root-infection": "19",
                            "dstlatitude": 37.775699615478516,
                            "version": "x.x.x.x",
                            "detect_rulematches": [
                                {
                                    "confidence": "high",
                                    "severity": "medium",
                                    "tags": [
                                        "fireeye",
                                        "ids",
                                        "helixcmsrule",
                                        "md-none"
                                    ],
                                    "ruleid": "1.1.2370",
                                    "rulename": "fireeye nx alert [malware-object]",
                                    "revision": 0
                                }
                            ],
                            "msg": "extended",
                            "dstisp": "cloudflare inc.",
                            "dstport": 80,
                            "metaclass": "antivirus",
                            "alerturl": "https://fireeye-cm.xxxxxx.xxxxx/event_stream/events_for_bot?ma_id=166",
                            "md5": "47f9fdc617f8c98a6732be534d8dbe9a",
                            "eventid": "166",
                            "product": "cms",
                            "virus": [
                                "fetestevent",
                                "fe_ml_heuristic"
                            ],
                            "devicename": "fireeye-cm.xxxxxx.xxxxx",
                            "dstlongitude": -122.39520263671875,
                            "explanation": {
                                "malware-detected": {
                                    "malware": [
                                        {
                                            "name": "fetestevent",
                                            "stype": "vm-bot-command",
                                            "sid": "11111112"
                                        },
                                        {
                                            "profile": "win7x64-sp1m",
                                            "http-header": "get /appliance-test/test-infection.exe http/1.1\r\nhost: fedeploycheck.fireeye.com\r\nuser-agent: mozilla/5.0 (windows nt 10.0; win64; x64; rv:79.0) gecko/20100101 firefox/79.0\r\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\naccept-language: en-us,en;q=0.5\r\naccept-encoding: gzip, deflate\r\nconnection: keep-alive\r\nupgrade-insecure-requests: 1\r\n\r\n http/1.1 200 ok\r\ndate: thu, 13 aug 2020 08:34:22 gmt\r\nserver: apache\r\nlast-modified: tue, 17 apr 2012 22:12:28 gmt\r\netag: \"40011-7000-4bde73bf74b00\"\r\naccept-ranges: bytes\r\ncontent-length: 28672\r\ncache-control: max-age=0\r\nexpires: thu, 13 aug 2020 08:34:22 gmt\r\nconnection: close\r\ncontent-type: application/octet-stream",
                                            "submitted-at": "2020-08-13t08:32:15z",
                                            "name": "fe_ml_heuristic",
                                            "downloaded-at": "2020-08-13t08:34:08z",
                                            "md5sum": "47f9fdc617f8c98a6732be534d8dbe9a",
                                            "executed-at": "2020-08-13t08:34:12z",
                                            "application": "windows explorer",
                                            "sha256": "b009f4c1b52cbe6db873fd601b68735a05b0721556eea73690b704f77f04b17e",
                                            "type": "exe",
                                            "original": "test-infection.exe",
                                            "stype": "malware-guard"
                                        }
                                    ]
                                },
                                "cnc-services": {
                                    "cnc-service": [
                                        {
                                            "type": "networkanomaly",
                                            "sname": "fetestevent",
                                            "protocol": "udp",
                                            "port": "53",
                                            "address": "xxx.xxxxxxx.xxx"
                                        },
                                        {
                                            "type": "networkanomaly",
                                            "sname": "fetestevent",
                                            "protocol": "udp",
                                            "port": "53",
                                            "address": "xxx.xxxxxxx.xxx"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "sid": "11111112",
                                            "type": "vmsigmatch",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "type": "networkanomaly",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~::~~get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: mil.fireeye.com::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "sid": "11111112",
                                            "type": "vmsigmatch",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "type": "networkanomaly",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~"
                                        }
                                    ]
                                },
                                "anomaly": "229888",
                                "analysis": "binary"
                            },
                            "vlan": 0,
                            "detect_ruleids": [
                                "1.1.2370"
                            ],
                            "alert": {
                                "ack": "no",
                                "ati-data": "{\"data\": [{\"extracted_from\": \"analysis\", \"observable_type\": \"hash\", \"context_api\": {\"threat_details\": {\"av_classifications\": [{\"first_seen\": \"2020-07-26t06:28:44.000000z\", \"av_vendor\": \"third-party-1\", \"av_product\": \"external products\", \"total_malicious\": 2, \"id\": \"av-results-type--b0ea2863-a6ec-3401-8892-3ccd59c9cbd8\", \"total_scanned\": 70}]}, \"name\": \"not_attributed\", \"sample_metadata\": {\"hashes\": {\"md5\": \"47f9fdc617f8c98a6732be534d8dbe9a\"}, \"mime_type\": \"application/x-dosexec\"}, \"updated_at\": \"2020-08-04 00:15:37.000000z\", \"created_at\": \"2020-08-04 00:15:37.000000z\", \"third_party_context\": {\"av_results\": [{\"product\": \"external products\", \"scanned\": \"2020-07-26t06:28:44.000000z\", \"total_malicious\": 2, \"total_scanned\": 70}]}, \"analysis_conclusion\": \"indeterminate\", \"type\": \"malware-summary\", \"id\": \"malware-summary--1e92bab8-007a-39ec-8c85-0a8859a5793c\"}, \"observable_value\": \"47f9fdc617f8c98a6732be534d8dbe9a\"}]}",
                                "sc-version": "1044.170"
                            },
                            "dstcountrycode": "us",
                            "meta_deviceid": "86F781D434CE",
                            "meta_sensor": "fireeye-nx1500v",
                            "alert_deviceid": "867a65b84172",
                            "class": "fireeye_nx_alert",
                            "severity": "majr",
                            "uuid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "sha256": "b009f4c1b52cbe6db873fd601b68735a05b0721556eea73690b704f77f04b17e",
                            "__metadata__": {
                                "received": "2020-08-13T08:34:37.000Z",
                                "raw_batch_id": "ff9eb053-d43f-43ef-82ec-bf8b8ca169b0",
                                "data_type": "passthrough",
                                "disable_index": false,
                                "dynamic_taxonomy": true,
                                "num_events": 1,
                                "source_type": "json",
                                "target_index": "alerts",
                                "batch_id": "ff9eb053-d43f-43ef-82ec-bf8b8ca169b0",
                                "customer_id": "hexqsj477",
                                "id": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                                "sequence_number": 0
                            },
                            "sensor": "fireeye-nx1500v",
                            "srcport": 52903,
                            "srcserver": "x.x.x.x",
                            "rule": [
                                "vm-bot-command",
                                "malware-guard"
                            ],
                            "srcusagetype": "rsv",
                            "deviceid": "86f781d434ce",
                            "action": "notified",
                            "attackinfo": "get /appliance-test/test-infection.exe http/1.1\r\nhost: fedeploycheck.fireeye.com\r\nuser-agent: mozilla/5.0 (windows nt 10.0; win64; x64; rv:79.0) gecko/20100101 firefox/79.0\r\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\naccept-language: en-us,en;q=0.5\r\naccept-encoding: gzip, deflate\r\nconnection: keep-alive\r\nupgrade-insecure-requests: 1\r\n\r\n http/1.1 200 ok\r\ndate: thu, 13 aug 2020 08:34:22 gmt\r\nserver: apache\r\nlast-modified: tue, 17 apr 2012 22:12:28 gmt\r\netag: \"40011-7000-4bde73bf74b00\"\r\naccept-ranges: bytes\r\ncontent-length: 28672\r\ncache-control: max-age=0\r\nexpires: thu, 13 aug 2020 08:34:22 gmt\r\nconnection: close\r\ncontent-type: application/octet-stream",
                            "dstcity": "san francisco"
                        },
                        "_index": "alerts"
                    }
                ],
                "total": 9,
                "max_score": 0.0
            },
            "_shards": {
                "successful": 27,
                "failed": 0,
                "skipped": 0,
                "total": 27
            },
            "took": 4,
            "timed_out": false,
            "metrics": {
                "load": 0.9833333333333334,
                "regex": false,
                "list": false,
                "aggregation": false,
                "subsearch": false
            },
            "failures": []
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully returned results for the query '{query}' in Trellix Helix."****_If not successfully hits/total=0 (is_success=false):_ Print "No results were found for the query '{query}'."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Index Search". Reason: {0}''.format(error.Stacktrace) | General  
  
### Archive Search

#### Description

Perform archive search in Trellix Helix.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query for the search, for example, srcserver=172.30.202.130  
Time Frame | String | N/A | Yes | Specify the time frame for the search. Only hours and days are supported. This is the Trellix Helix limitation. Examples of the values:  
7h - 7 hours1d - 1 day  
Max Results To Return | Integer | 100 | No | Specify how many results to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "results": {
            "hits": {
                "hits": [
                    {
                        "_score": 0.0,
                        "_type": "_doc",
                        "_id": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                        "_source": {
                            "dstusagetype": "cdn",
                            "_eventid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "srcisp": "private ip address lan",
                            "meta_uuid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "srcipv4": "x.x.x.x",
                            "alert_version": "x.x.x.x",
                            "cnchost": [
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx",
                                "xxx.xxxxxxx.xxx"
                            ],
                            "detect_rulenames": [
                                "fireeye nx alert [malware-object]"
                            ],
                            "dstdomain": "cloudflare.com",
                            "dstregion": "california",
                            "meta_ts": "2020-08-13T08:34:12.000Z",
                            "dstipv4": "172.65.203.203",
                            "meta_rule": "fireeye_cms_alert-ss-0.1.4",
                            "alert_product": "web mps",
                            "srcmac": "x:x:x:x:x:x",
                            "eventlog": "malware-object",
                            "eventtype": "ips",
                            "dstcountry": "united states of america",
                            "msr_ruleids": [],
                            "meta_alert_deviceid": "867A65B84172",
                            "root-infection": "19",
                            "dstlatitude": 37.775699615478516,
                            "version": "9.0.0.916210",
                            "detect_rulematches": [
                                {
                                    "confidence": "high",
                                    "severity": "medium",
                                    "tags": [
                                        "fireeye",
                                        "ids",
                                        "helixcmsrule",
                                        "md-none"
                                    ],
                                    "ruleid": "1.1.2370",
                                    "rulename": "fireeye nx alert [malware-object]",
                                    "revision": 0
                                }
                            ],
                            "msg": "extended",
                            "dstisp": "cloudflare inc.",
                            "dstport": 80,
                            "metaclass": "antivirus",
                            "alerturl": "https://fireeye-cm.xxxxxxxxxx.xxxxx/event_stream/events_for_bot?ma_id=166",
                            "md5": "47f9fdc617f8c98a6732be534d8dbe9a",
                            "eventid": "166",
                            "product": "cms",
                            "virus": [
                                "fetestevent",
                                "fe_ml_heuristic"
                            ],
                            "devicename": "fireeye-cm.xxxxxxxxxx.xxxxx",
                            "dstlongitude": -122.39520263671875,
                            "explanation": {
                                "malware-detected": {
                                    "malware": [
                                        {
                                            "name": "fetestevent",
                                            "stype": "vm-bot-command",
                                            "sid": "11111112"
                                        },
                                        {
                                            "profile": "win7x64-sp1m",
                                            "http-header": "get /appliance-test/test-infection.exe http/1.1\r\nhost: fedeploycheck.fireeye.com\r\nuser-agent: mozilla/5.0 (windows nt 10.0; win64; x64; rv:79.0) gecko/20100101 firefox/79.0\r\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\naccept-language: en-us,en;q=0.5\r\naccept-encoding: gzip, deflate\r\nconnection: keep-alive\r\nupgrade-insecure-requests: 1\r\n\r\n http/1.1 200 ok\r\ndate: thu, 13 aug 2020 08:34:22 gmt\r\nserver: apache\r\nlast-modified: tue, 17 apr 2012 22:12:28 gmt\r\netag: \"40011-7000-4bde73bf74b00\"\r\naccept-ranges: bytes\r\ncontent-length: 28672\r\ncache-control: max-age=0\r\nexpires: thu, 13 aug 2020 08:34:22 gmt\r\nconnection: close\r\ncontent-type: application/octet-stream",
                                            "submitted-at": "2020-08-13t08:32:15z",
                                            "name": "fe_ml_heuristic",
                                            "downloaded-at": "2020-08-13t08:34:08z",
                                            "md5sum": "47f9fdc617f8c98a6732be534d8dbe9a",
                                            "executed-at": "2020-08-13t08:34:12z",
                                            "application": "windows explorer",
                                            "sha256": "b009f4c1b52cbe6db873fd601b68735a05b0721556eea73690b704f77f04b17e",
                                            "type": "exe",
                                            "original": "test-infection.exe",
                                            "stype": "malware-guard"
                                        }
                                    ]
                                },
                                "cnc-services": {
                                    "cnc-service": [
                                        {
                                            "type": "networkanomaly",
                                            "sname": "fetestevent",
                                            "protocol": "udp",
                                            "port": "53",
                                            "address": "xxx.xxxxxxx.xxx"
                                        },
                                        {
                                            "type": "networkanomaly",
                                            "sname": "fetestevent",
                                            "protocol": "udp",
                                            "port": "53",
                                            "address": "xxx.xxxxxxx.xxx"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "sid": "11111112",
                                            "type": "vmsigmatch",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "type": "networkanomaly",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: mil.fireeye.com::~~::~~get /appliance-test/alert.html http/1.1::~~cache-control: no-cache::~~connection: keep-alive::~~pragma: no-cache::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "sid": "11111112",
                                            "type": "vmsigmatch",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~"
                                        },
                                        {
                                            "sname": "fetestevent",
                                            "protocol": "tcp",
                                            "url": "hxxp:///appliance-test/alert.html",
                                            "address": "xxx.xxxxxxx.xxx",
                                            "type": "networkanomaly",
                                            "port": "80",
                                            "channel": "get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: xxx.xxxxxxx.xxx::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~get /appliance-test/alert.html http/1.1::~~user-agent: winhttp example/1.0::~~host: mil.fireeye.com::~~connection: keep-alive::~~cache-control: no-cache::~~pragma: no-cache::~~::~~"
                                        }
                                    ]
                                },
                                "anomaly": "229888",
                                "analysis": "binary"
                            },
                            "vlan": 0,
                            "detect_ruleids": [
                                "1.1.2370"
                            ],
                            "alert": {
                                "ack": "no",
                                "ati-data": "{\"data\": [{\"extracted_from\": \"analysis\", \"observable_type\": \"hash\", \"context_api\": {\"threat_details\": {\"av_classifications\": [{\"first_seen\": \"2020-07-26t06:28:44.000000z\", \"av_vendor\": \"third-party-1\", \"av_product\": \"external products\", \"total_malicious\": 2, \"id\": \"av-results-type--b0ea2863-a6ec-3401-8892-3ccd59c9cbd8\", \"total_scanned\": 70}]}, \"name\": \"not_attributed\", \"sample_metadata\": {\"hashes\": {\"md5\": \"47f9fdc617f8c98a6732be534d8dbe9a\"}, \"mime_type\": \"application/x-dosexec\"}, \"updated_at\": \"2020-08-04 00:15:37.000000z\", \"created_at\": \"2020-08-04 00:15:37.000000z\", \"third_party_context\": {\"av_results\": [{\"product\": \"external products\", \"scanned\": \"2020-07-26t06:28:44.000000z\", \"total_malicious\": 2, \"total_scanned\": 70}]}, \"analysis_conclusion\": \"indeterminate\", \"type\": \"malware-summary\", \"id\": \"malware-summary--1e92bab8-007a-39ec-8c85-0a8859a5793c\"}, \"observable_value\": \"47f9fdc617f8c98a6732be534d8dbe9a\"}]}",
                                "sc-version": "1044.170"
                            },
                            "dstcountrycode": "us",
                            "meta_deviceid": "86F781D434CE",
                            "meta_sensor": "fireeye-nx1500v",
                            "alert_deviceid": "867a65b84172",
                            "class": "fireeye_nx_alert",
                            "severity": "majr",
                            "uuid": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                            "sha256": "b009f4c1b52cbe6db873fd601b68735a05b0721556eea73690b704f77f04b17e",
                            "__metadata__": {
                                "received": "2020-08-13T08:34:37.000Z",
                                "raw_batch_id": "ff9eb053-d43f-43ef-82ec-bf8b8ca169b0",
                                "data_type": "passthrough",
                                "disable_index": false,
                                "dynamic_taxonomy": true,
                                "num_events": 1,
                                "source_type": "json",
                                "target_index": "alerts",
                                "batch_id": "ff9eb053-d43f-43ef-82ec-bf8b8ca169b0",
                                "customer_id": "hexqsj477",
                                "id": "e7afc97f-f3fb-4e1b-9915-a648f00b9c5f",
                                "sequence_number": 0
                            },
                            "sensor": "fireeye-nx1500v",
                            "srcport": 52903,
                            "srcserver": "x.x.x.x",
                            "rule": [
                                "vm-bot-command",
                                "malware-guard"
                            ],
                            "srcusagetype": "rsv",
                            "deviceid": "86f781d434ce",
                            "action": "notified",
                            "attackinfo": "get /appliance-test/test-infection.exe http/1.1\r\nhost: fedeploycheck.fireeye.com\r\nuser-agent: mozilla/5.0 (windows nt 10.0; win64; x64; rv:79.0) gecko/20100101 firefox/79.0\r\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\naccept-language: en-us,en;q=0.5\r\naccept-encoding: gzip, deflate\r\nconnection: keep-alive\r\nupgrade-insecure-requests: 1\r\n\r\n http/1.1 200 ok\r\ndate: thu, 13 aug 2020 08:34:22 gmt\r\nserver: apache\r\nlast-modified: tue, 17 apr 2012 22:12:28 gmt\r\netag: \"40011-7000-4bde73bf74b00\"\r\naccept-ranges: bytes\r\ncontent-length: 28672\r\ncache-control: max-age=0\r\nexpires: thu, 13 aug 2020 08:34:22 gmt\r\nconnection: close\r\ncontent-type: application/octet-stream",
                            "dstcity": "san francisco"
                        },
                        "_index": "alerts"
                    }
                ],
                "total": 9,
                "max_score": 0.0
            },
            "_shards": {
                "successful": 27,
                "failed": 0,
                "skipped": 0,
                "total": 27
            },
            "took": 4,
            "timed_out": false,
            "metrics": {
                "load": 0.9833333333333334,
                "regex": false,
                "list": false,
                "aggregation": false,
                "subsearch": false
            },
            "failures": []
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully returned results for the archive query '{query}' in Trellix Helix."****_If job was paused 3 times (is_success =false):_ Print "No results were found for the archive query '{query}'. Reason: archive search job was paused more than 3 times."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Archive Search". Reason: {0}''.format(error.Stacktrace)___If bad input in the Time Frame parameter:_ print "Error executing action "Archive Search". Reason: Unexpected format is used in the parameter 'Time Frame'. Please check the specified value. ''.format(error.Stacktrace) | General  
  
### Get Alert Details

#### Description

Retrieve information about Alert from Trellix Helix.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | Integer | N/A | Yes | Specify ID of the Alert that needs to be enriched in Trellix Helix.  
Max Notes To Return | Integer | 50 | No | Specify how many associated notes to return.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "alerts": [
            {
                "_assignedAt": null,
                "_assignedTo": null,
                "_createdBy": {
                    "id": "abd5feae-84fc-41e9-be61-336ec358c89a",
                    "avatar": "https://secure.gravatar.com/avatar/8267ad472cbc450380f270ee60d729b5",
                    "name": "System User",
                    "username": "system_user",
                    "primary_email": "xx.xxxxx@fireeye.com"
                },
                "_updatedBy": {
                    "id": "0b48dde7-5c81-4899-978d-793540861a42",
                    "avatar": "https://secure.gravatar.com/avatar/0feb076e8da5a3dff2b62cf8e53525cd",
                    "name": "xxxxxxxxx",
                    "username": "xxx.xxxxxx@xxxxxxx.xxx",
                    "primary_email": "xxx.xxxxxx@xxxxxxx.xxx"
                },
                "alertThreat": "Unknown",
                "alertType": "fireeye_rule",
                "alertTypeDetails": {
                    "source": "fireeye-domain",
                    "detail": {
                        "pid": 3808,
                        "result": "quarantined",
                        "lastmodifiedtime": "2020-08-17T11:18:09.274Z",
                        "processpath": "c:\\knowbe4\\rssimulator\\start.exe",
                        "confidence": "high",
                        "filename": "c:\\knowbe4\\rssimulator\\testfolder\\tests\\9\\1873917892.axp",
                        "hx_alert_id": 504,
                        "accountdomain": "xxxxxxx-xxx",
                        "method": "oas",
                        "username": "xxxxxxxxx",
                        "virus": "generic.mg.4a1aa9b759980343",
                        "agentdomain": "xxxxxx-xxx",
                        "createdtime": "2020-05-24T11:18:08.993Z",
                        "agenthostname": "xxxxxx-xxxxxx",
                        "md5": "4a1aa9b7599803432bfe85056f1dce06",
                        "sha1": "469cf073c0ffcdfd23c28d88a851b885422ab2ce",
                        "bytes": 224888,
                        "agentip": "x.x.x.x",
                        "deviceid": "86b7f11acf8d",
                        "malwaretype": "malware",
                        "lastaccessedtime": "2020-08-17T11:18:09.274Z",
                        "objecttype": "file"
                    },
                    "summary": {
                        "virus": "generic.mg.4a1aa9b759980343",
                        "malwaretype": "malware"
                    }
                },
                "classification": 30,
                "closedState": "Unknown",
                "confidence": "Medium",
                "context": null,
                "createDate": "2020-08-17T11:30:16.863577Z",
                "customer_id": "hexqsj477",
                "description": "FireEye HX detected and quarantined malware on this system using the AV engine.",
                "displayId": 3564,
                "distinguisherKey": "js2asebmwggfxt0ahvu034~,~malware~,~generic.mg.4a1aa9b759980343~,~quarantined",
                "distinguishers": {
                    "virus": "generic.mg.4a1aa9b759980343",
                    "agentid": "js2asebmwggfxt0ahvu034",
                    "result": "quarantined",
                    "malwaretype": "malware"
                },
                "emailedAt": 737654,
                "eventCount": 1,
                "eventsThreshold": 1,
                "firstEventAt": "2020-08-17T11:29:13.124000Z",
                "lastEventAt": "2020-08-17T11:29:13.124000Z",
                "external": [],
                "externalCount": 0,
                "externalId": "",
                "id": "5f3a6a3777e949323809f5af",
                "infoLinks": [],
                "internal": [],
                "internalCount": 0,
                "isThreat": false,
                "isTuned": false,
                "killChain": [
                    "5 - Installation"
                ],
                "lastSyncMs": 1597663799165,
                "message": "FIREEYE HX [Malware Prevented]",
                "notes": [],
                "notesCount": 0,
                "organization": "hexqsj477",
                "originId": "MAP_RULE",
                "queues": [
                    "Default Queue"
                ],
                "revision": 0,
                "revisions": [],
                "revisionNotes": "",
                "risk": "Medium",
                "riskOrder": 2,
                "search": "class=fireeye_hx_alert eventlog=mal result=quarantined NOT srcipv4:$exclusions.global.srcipv4",
                "secondsThreshold": 60,
                "severity": "Medium",
                "sourceRevision": 0,
                "sourceUrl": "",
                "state": "Open",
                "suppressed": true,
                "tags": [
                    "fireeye",
                    "helixhxrule",
                    "malware",
                    "av",
                    "md-info"
                ],
                "threatChangedAt": null,
                "threatType": 50,
                "triggerId": "1.1.2615",
                "triggerRevision": 0,
                "tuningSearch": "",
                "updateDate": "2020-09-13T07:10:25.451790Z"
            }
        ],
        "meta": {
            "count": 1,
            "previous": null,
            "offset": 0,
            "limit": 30,
            "next": null
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_  
__Print "Successfully returned information about the alert with ID {ID} from Trellix Helix."****_If Alert ID not found:_ Print "Action wasn't able to return information about the alert with ID {ID} from Trellix Helix. Reason: Alert with ID {ID} wasn't found."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Get Alert Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall | **Table name:** Notes**Table Columns:**

  * Note (mapped as note)
  * Author (mapped as _author/name)
  * Created At (mapped as createDate)

| General  
  
### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname.

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
FEHelix_risk_score | risk_score | When available in JSON  
FEHelix_last_event_at | last_event_at | When available in JSON  
FEHelix_severity | severity | When available in JSON  
FEHelix_status | asset_status | When available in JSON  
FEHelix_source | source | When available in JSON  
FEHelix_events_count | events_count | When available in JSON  
FEHelix_is_vip_asset | is_vip_asset | When available in JSON  
FEHelix_type | asset_type | When available in JSON  
FEHelix_name | asset_name | When available in JSON  
FEHelix_detections_count | detections | When available in JSON  
FEHelix_uuid | asset_uuid | When available in JSON  
FEHelix_department | asset_department | When available in JSON  
FEHelix_id | id | When available in JSON  
FEHelix_os | properties/os | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "risk_score": 0,
        "last_event_at": null,
        "asset_job_title": null,
        "severity": "Low",
        "cidr_range": null,
        "asset_status": "active",
        "source": "detection",
        "created_at": "2020-09-01T22:27:05.202322+00:00",
        "events_count": 0,
        "is_vip_asset": false,
        "asset_type": "xxxx",
        "asset_name": "xx-xxxx-xxxx",
        "last_activity": "2020-09-01T22:27:05.202322+00:00",
        "detections": 0,
        "asset_uuid": "09aa70c9-f76e-4092-a3a6-040192d24231",
        "location": null,
        "properties": {
            "os": "windows 10 enterprise evaluation"
        },
        "org": "hexqsj477",
        "id": 856440,
        "asset_department": null
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities were enriched (is_success = true):_  
__Print "Successfully enriched the following entities in Trellix Helix: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to enrich the following entities in Trellix Helix\n: {0}".format([entity.identifier])_If no entities were enriched (is_success=false):_ Print "No entities were enriched."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Enrich Endpoint". Reason: {0}''.format(error.Stacktrace) | General  
  
### Enrich User

#### Description

Fetch information about users from Trellix Helix.

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
FEHelix_risk_score | risk_score | When available in JSON  
FEHelix_last_event_at | last_event_at | When available in JSON  
FEHelix_severity | severity | When available in JSON  
FEHelix_status | asset_status | When available in JSON  
FEHelix_source | source | When available in JSON  
FEHelix_events_count | events_count | When available in JSON  
FEHelix_is_vip_asset | is_vip_asset | When available in JSON  
FEHelix_type | asset_type | When available in JSON  
FEHelix_name | asset_name | When available in JSON  
FEHelix_detections_count | detections | When available in JSON  
FEHelix_uuid | asset_uuid | When available in JSON  
FEHelix_department | asset_department | When available in JSON  
FEHelix_id | id | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
                "risk_score": 0,
                "last_event_at": null,
                "asset_job_title": null,
                "severity": "Low",
                "cidr_range": null,
                "asset_status": "active",
                "source": "detection",
                "created_at": "2020-08-25T20:26:17.694104+00:00",
                "events_count": 0,
                "is_vip_asset": false,
                "asset_type": "User",
                "asset_name": "xxxxxxxx",
                "last_activity": "2020-08-25T20:26:17.694104+00:00",
                "detections": 0,
                "asset_uuid": "066c934a-c768-4c4f-adf5-35d03e95fc95",
                "location": null,
                "properties": {},
                "org": "hexqsj477",
                "id": 1174213,
                "asset_department": null
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities were enriched (is_success = true):_  
__Print "Successfully enriched the following entities in Trellix Helix: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to enrich the following entities in Trellix Helix\n: {0}".format([entity.identifier])_If no entities were enriched (is_success=false):_ Print "No entities were enriched."**The action should fail and stop a playbook execution:**_if not successful:_ Print "Error executing action "Enrich User". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connectors

### FireEye Helix - Alerts Connector

#### Description

Pull alerts from Trellix Helix.

#### API Authentication

API Authentication is done through x-fireeye-api-key header, which contains API key.

#### Configure FireEye Helix - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventtype | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://helix.eu.fireeye.com/helix/id/{id} | Yes | API Root of the Trellix Helix instance. Example: https://helix.eu.fireeye.com/helix/id/aaaqsj477  
API Token | String | N/A | No | API Token of the Trellix Helix account.  
Client ID | String | N/A | No | Client ID for Trellix IAM OAuth authentication.  
Client Secret | Password | N/A | No | Client Secret for Trellix IAM OAuth authentication.  
Scope | String | xdr.alr.r xdr.org.adm | No | Space separated scopes for Trellix IAM OAuth authentication.  
Server Timezone | String | N/A | No | Specify which timezone is set on the Trellix Helix server in regards to UTC. For example, +1, -1, etc. If nothing is specified, the connector will use UTC as a default timezone.  
Lowest Risk To Fetch | String | Medium | Yes | Lowest risk that will be used to fetch Alert.. Possible values:  
Low Medium High Critical  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 50 | No | How many alerts to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix Helix server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
