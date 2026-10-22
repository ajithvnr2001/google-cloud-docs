---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/arcsight-logger/
title: Integrate ArcSight Logger with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:42.544939+00:00
---

# Integrate ArcSight Logger with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/arcsight-logger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate ArcSight Logger with Google SecOps 

This document explains how to integrate ArcSight Logger with Google Security Operations (Google SecOps).

## Integration parameters

For detailed instructions on how to configure an integration in Google Security Operations, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server Address | String | https://<host>:<port> | Yes | The server address of the ArcSight Logger instance.  
Username | String | N/A | Yes | Username of the ArcSight Logger account.  
Password | Password | N/A | Yes | The password of the ArcSight Logger account.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verify the SSL certificate for the connection to the ArcSight Logger server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

Test connectivity to ArcSight Logger with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

The action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:** _If no errors and returned data:_ "Successfully connected to the ArcSight Logger with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If an error is reported:_ "Error executing action "Ping". Reason: {0}''.format(error.Stacktrace) | General  
  
### Send Query

Send a query to get information about related events from ArcSight Logger event log manager.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Query | String | "" | Yes | Specify the query to send to ArcSight Logger event search.  
Max Events to Return | Integer | 100 | No | Specify the amount of events to return. Limit is 10000. This is ArcSight Logger limitation.  
Time Frame | String | 1h | No | Specify the timeframe which will be used to fetch events. Possible values:  
1m - 1 minute ago 1h - 1 hour ago 1d - 1 day ago Note: You can't combine different values, like 1d2h30m.  
Fields to Fetch | Comma Separated Values | None | No | Specify what fields to fetch from ArcSight Logger. If nothing is specified, then all of the available fields will be returned.  
Include Raw Event Data | Checkbox | Checked | No | If enabled, raw event data is included in the response.  
Local Search Only | Checkbox | Unchecked | No | Indicates that ArcSight Logger event search is local only, and does not include ArcSight Logger peers. Set to false if you want to include peers in the event search.  
Discover fields | Checkbox | Checked | No | Indicates that the ArcSight Logger search should try to discover fields in the events found.  
Sort | String | ascending | No | Specify what sorting method to use. Possible values: ascending descending  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "fields": [
          {
              "name": "_rowId",
              "type": "string",
              "alias": "_rowId"
          },
          {
              "name": "_raw",
              "type": "string",
              "alias": "_raw"
          },
          {
              "name": "Event Time",
              "type": "date",
              "alias": "Event Time"
          },
          {
              "name": "Logger",
              "type": "string",
              "alias": "Logger"
          },
          {
              "name": "Device",
              "type": "string",
              "alias": "Device"
          },
          {
              "name": "Receipt Time",
              "type": "date",
              "alias": "Receipt Time"
          },
          {
              "name": "deviceReceiptTime",
              "type": "date",
              "alias": "deviceReceiptTime"
          },
          {
              "name": "deviceCustomString2",
              "type": "string",
              "alias": "deviceCustomString2"
          },
          {
              "name": "destinationAddress",
              "type": "string",
              "alias": "destinationAddress"
          },
          {
              "name": "deviceCustomNumber3Label",
              "type": "string",
              "alias": "deviceCustomNumber3Label"
          },
          {
              "name": "globalEventId",
              "type": "number",
              "alias": "globalEventId"
          },
          {
              "name": "deviceVersion",
              "type": "string",
              "alias": "deviceVersion"
          },
          {
              "name": "name",
              "type": "string",
              "alias": "name"
          },
          {
              "name": "deviceAddress",
              "type": "string",
              "alias": "deviceAddress"
          },
          {
              "name": "deviceVendor",
              "type": "string",
              "alias": "deviceVendor"
          },
          {
              "name": "Version",
              "type": "string",
              "alias": "Version"
          },
          {
              "name": "deviceCustomNumber1Label",
              "type": "string",
              "alias": "deviceCustomNumber1Label"
          },
          {
              "name": "deviceEventCategory",
              "type": "string",
              "alias": "deviceEventCategory"
          },
          {
              "name": "endTime",
              "type": "date",
              "alias": "endTime"
          },
          {
              "name": "fileName",
              "type": "string",
              "alias": "fileName"
          },
          {
              "name": "deviceCustomNumber2",
              "type": "number",
              "alias": "deviceCustomNumber2"
          },
          {
              "name": "deviceCustomNumber1",
              "type": "number",
              "alias": "deviceCustomNumber1"
          },
          {
              "name": "baseEventCount",
              "type": "number",
              "alias": "baseEventCount"
          },
          {
              "name": "startTime",
              "type": "date",
              "alias": "startTime"
          },
          {
              "name": "deviceCustomNumber3",
              "type": "number",
              "alias": "deviceCustomNumber3"
          },
          {
              "name": "agentSeverity",
              "type": "string",
              "alias": "agentSeverity"
          },
          {
              "name": "fsize",
              "type": "string",
              "alias": "fsize"
          },
          {
              "name": "deviceProduct",
              "type": "string",
              "alias": "deviceProduct"
          },
          {
              "name": "deviceEventClassId",
              "type": "string",
              "alias": "deviceEventClassId"
          },
          {
              "name": "deviceCustomNumber2Label",
              "type": "string",
              "alias": "deviceCustomNumber2Label"
          },
          {
              "name": "deviceCustomString2Label",
              "type": "string",
              "alias": "deviceCustomString2Label"
          },
          {
              "name": "fileType",
              "type": "string",
              "alias": "fileType"
          }
      ],
      "results": [
          [
              "4BFEFD-86@Local",
              "CEF:0|ArcSight|Logger|7.0.0.8280.0|storagegroup:100|Storage Group Space Used|1| cat=/Monitor/StorageGroup/Space/Used cn1=15 cn1Label=Percent Used cn2=180 cn2Label=retention period (days) cn3=2048 cn3Label=used (MB) cs2=CurrentValue cs2Label=timeframe dst=10.0.2.185 dvc=10.0.2.185 end=1585661238546 fileType=storageGroup fname=Default Storage Group fsize=13 geid=0 rt=1585661238546",
              1585661238546,
              "Local",
              "Logger",
              1585661364960,
              1585661238546,
              "CurrentValue",
              "10.0.2.185",
              "used (MB)",
              0,
              "7.0.0.8280.0",
              "Storage Group Space Used",
              "10.0.2.185",
              "ArcSight",
              "0",
              "Percent Used",
              "/Monitor/StorageGroup/Space/Used",
              1585661238546,
              "Default Storage Group",
              180,
              15,
              1,
              1585661238546,
              2048,
              "1",
              "13",
              "Logger",
              "storagegroup:100",
              "retention period (days)",
              "timeframe",
              "storageGroup"
          ],
          [
              "4BFEFD-87@Local",
              "CEF:0|ArcSight|Logger|7.0.0.8280.0|storagegroup:100|Storage Group Space Used|1| cat=/Monitor/StorageGroup/Space/Used cn1=33 cn1Label=Percent Used cn2=365 cn2Label=retention period (days) cn3=1024 cn3Label=used (MB) cs2=CurrentValue cs2Label=timeframe dst=10.0.2.185 dvc=10.0.2.185 end=1585661238546 fileType=storageGroup fname=Internal Event Storage Group fsize=3 geid=0 rt=1585661238546",
              1585661238546,
              "Local",
              "Logger",
              1585661364960,
              1585661238546,
              "CurrentValue",
              "10.0.2.185",
              "used (MB)",
              0,
              "7.0.0.8280.0",
              "Storage Group Space Used",
              "10.0.2.185",
              "ArcSight",
              "0",
              "Percent Used",
              "/Monitor/StorageGroup/Space/Used",
              1585661238546,
              "Internal Event Storage Group",
              365,
              33,
              1,
              1585661238546,
              1024,
              "1",
              "3",
              "Logger",
              "storagegroup:100",
              "retention period (days)",
              "timeframe",
              "storageGroup"
          ]
      ]
    }
    

##### Case Wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:** >_If status is set to "completed" and hit is greater than zero:_ "Successfully returned events for query "{0}" from the ArcSight Logger".format(query) _If status is set "completed" and hit is set to 0: (is_success == false):_ "Events were not found for query "{0}" in ArcSight Logger".format(query). >_If status the status is set to error:_ "Unable to execute query "{0}" in ArcSight Logger".format(query). _If status code is 409 in the first request:_ "Unable to execute query "{0}" in ArcSight Logger. Reason: {1}".format(query, errors/message from first response)" _Async output message:_ "Starting processing query {0} in ArcSight Logger".format(query) **The action should fail and stop a playbook execution:** _If a fatal error (wrong credentials, connection error, action crashes) is reported:_ "Error executing action "Send Query". Reason: {0}''.format(error.Stacktrace) | General  
Table | **Table name:** {Query} **Columns:** all of the available columns from the response. Look into the Action behavior section for more details.  | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
