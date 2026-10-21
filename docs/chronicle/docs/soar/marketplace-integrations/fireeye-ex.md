---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-ex/
title: FireEye EX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:25.372191+00:00
---

# FireEye EX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-ex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye EX

**Important:** FireEye and McAfee Enterprise merged and became Trellix. FireEye EX was renamed to Trellix Email Security - Server Edition.

This document describes how to integrate FireEye EX with Google Security Operations.

## Product Use Cases

  1. Ingest Trellix Email Security - Server Edition alerts to use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform enrichment actions - get data from Trellix Email Security - Server Edition to enrich data in Google SecOps Alerts.
  3. Perform active actions - release/delete email using Trellix Email Security - Server Edition agent from Google SecOps.



## Configure FireEye EX integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://<address>:\<port> | Yes | API root of Trellix Email Security - Server Edition server.  
Username | String | N/A | Yes | Username of the Trellix Email Security - Server Edition account.  
Password | Password | N/A | Yes | The password of the Trellix Email Security - Server Edition account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Trellix Email Security - Server Edition server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Trellix Email Security - Server Edition with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### List Quarantined Emails

#### Description

List quarantined emails.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Start Time | String | N/A | No | If specified, only emails that were created after start time will be returned. If Start Time and End Time are not specified, action returns quarantined emails from the last 24 hours. Format: YYYY-MM-DD'T'HH:MM:SS.SSS-HHMM  
End Time | String | N/A | No | If specified, only emails that were created before end time will be returned. If Start Time and End Time are not specified, action returns quarantined emails from the last 24 hours. Format: YYYY-MM-DD'T'HH:MM:SS.SSS-HHMM  
  
Sender Filter | String | N/A | No | If specified, returns all of the quarantined emails only from this sender.  
Subject Filter | String | N/A | No | If specified, returns all of the quarantined emails only with this subject.  
Max Email to Return | String | N/A | No | Specify how many emails to return. Limit is 10000. This is Trellix Email Security - Server Edition limitation.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "completed_at": "2020-06-09T08:21:17",
            "email_uuid": "9de3a94f-5ef6-46c7-b6d3-7d4f8c964925",
            "quarantine_path": "/data/email-analysis/quarantine2/2020-06-09/08/49h33n3HZczxNgc",
            "subject": "qwe",
            "message_id": "ec7d161d-c0f5-7e32-8f53-468393ccc9b6@fex2-lab.local",
            "from": "xxxx.xxxxx@xxxx-xxx.xxxxx",
            "queue_id": "49h33n3HZczxNgc"
        },
        {
            "completed_at": "2020-06-09T08:21:42",
            "email_uuid": "58800022-51f7-4b07-b6b1-c5d88434283f",
            "quarantine_path": "/data/email-analysis/quarantine2/2020-06-09/08/49h34G5TVczxNgg",
            "subject": "rew",
            "message_id": "625607a6-a99d-004a-4ad6-69c3ec795168@fex2-lab.local",
            "from": "xxxx.xxxxx@xxxx-xxx.xxxxx",
            "queue_id": "49h34G5TVczxNgg"
        }
    ]
    

### Release Quarantined Email

#### Description

Releases quarantined email.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be released.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Delete Quarantined Email

#### Description

Delete the quarantined email.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be deleted.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Download Quarantined Email

#### Description

Download quarantined email.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be downloaded.  
Download Path | String | N/A | No | Specify where the action should save the files. If nothing is specified, action will not save the file on the disk.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Download Alert Artifacts

#### Description

Download alert artifacts.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Alert UUID | String | N/A | Yes | Specify the alert UUID from where we need to download artifacts.  
Download Path | String | N/A | No | Specify where the action should save the files. If nothing is specified, action will not save the file on the disk.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
## Connectors

### FireEye EX - Alerts Connector

#### Configure FireEye EX - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:x | Yes | API root of Trellix Email Security - Server Edition server.  
Username | String | N/A | Yes | Username of the Trellix Email Security - Server Edition account.  
Password | Password |  | Yes | Password of the Trellix Email Security - Server Edition account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts. Max supported value is 48. This is the Trellix Email Security - Server Edition limitation.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the SonicWall server is valid.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
