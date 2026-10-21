---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ironport/
title: IronPort \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:06.357626+00:00
---

# IronPort  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ironport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IronPort

This document provides guidance on how to integrate IronPort with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/IronPort.zip).

## Product Permission

The AsyncOS API is a role-based system. The scope of API queries is defined by the role of the user. Cisco Content Security Management appliance users with the following roles can access the AsyncOS API:

  * Administrator
  * Operator
  * Technician
  * Read-Only Operator
  * Guest
  * Web Administrator
  * Web Policy Administrator
  * URL Filtering Administrator
  * Email Administrator
  * Help Desk User

**Note:** For Google Security Operations IronPort Integration, an account with at least Read-Only Operator role should be used.

## Configure IronPort integration in Google SecOps

### Configure IronPort integration with a CA certificate

You can verify your connection with a CA certificate file if needed.

Before you start, ensure you have the following:

  * The CA certificate file
  * The latest IronPort integration version



To configure the integration with a CA certificate, complete the following steps:

  1. Parse your CA certificate file into a Base64 String.
  2. Open the integration configuration parameters page.
  3. Insert the string in the **CA Certificate File** field.
  4. To test that the integration is successfully configured, select the **Verify SSL** checkbox and click **Test**.



### Configure IronPort integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
IronPort Server Address | String | x.x.x.x | Yes | IronPort Server Address to connect to.  
IronPort AsyncOS API Port | String | 6443 | True | IronPort AsyncOS API Port to connect to.  
Ironport SSH Port | String | 22 | Yes | IronPort SSH Port to connect to.  
Username | String | N/A | Yes | IronPort account to use with integration.  
Passphrase (password) | Password | N/A | Yes | Password for the account.  
CA Certificate File - parsed into Base64 String | String | N/A | No | N/A  
Use SSL | Checkbox | Checked | No | Specify if HTTPS should be used to connect to AsyncOS API.  
Verify SSL | Checkbox | Unchecked | No | Specify if the certificate validation should be enabled (will check if the certificate configured for AsyncOS API is valid).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Get all Recipients by Sender

#### Description

Get a list of recipients who received emails from a given sender.

**Note:** for action to work, please make sure that message tracking is enabled in IronPort, along with AsyncOS API.**Note:** Note that "Search Emails for Last X days/hours" value should be set accordingly to the amount of emails processed by target IronPort instance, if big enough value will be provided action can time out.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Sender | String | N/A | Yes | The sender email address to filter by.  
Search Emails for Last X | Integer | 7 | Yes | Specify a time frame for which to search for emails. Note that this value should be set accordingly to the amount of emails processed by IronPort, if big enough value will be provided action can time out.  
Set Search Email Period in | DDL | Days | Yes | Specify if search emails should by done with the period of days or hours.  
Max Recipients to Return | Integer | 20 | Yes | Specify how many recipients the action should return.  
Page Size | Integer | 100 | Yes | Specify the page size for the action to use when searching for emails.  
  
#### Playbook Use Cases Examples

Search for email recipients based on the sender's email provided in the action.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    ​{
        "attributes": {
            "direction": "",
            "hostName": "",
            "senderGroup": "N/A",
            "sender": "reporting@smtp.inside-ironport.local",
            "replyTo": "N/A",
            "timestamp": "20 May 2020 01:00:04 (GMT +00:00)",
            "serialNumber": "42225C72BFBA18A2257D-C143F31DFB78",
            "mid": [
                229
            ],
            "senderIp": "N/A",
            "icid": 0,
            "messageStatus": {
                "229": "Delivered"
            },
            "mailPolicy": [],
            "isCompleteData": "N/A",
            "verdictChart": {
                "229": "00000000"
            },
            "senderDomain": "N/A",
            "recipient": [
                "test.user1@inside-ironport.local"
            ],
            "sbrs": "N/A",
            "subject": "IronPort Report: Outgoing Mail Daily Report (smtp.inside-ironport.local)"
        }
    }
    

### Get all Recipients by Subject

#### Description

Get a list of recipients that received an email with the same subject.

**Note:** for action to work, please make sure that message tracking is enabled in IronPort, along with AsyncOS API.**Note:** Note that "Search Emails for Last X days/hours" value should be set accordingly to the amount of emails processed by target IronPort instance, if big enough value will be provided action can time out.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Subject | String | N/A | Yes | The subject to filter by.  
Search Emails for Last X | Integer | 7 | Yes | Specify a time frame for which to search for emails.Note that this value should be set accordingly to the amount of emails processed by IronPort, if big enough value will be provided action can time out.  
  
Set Search Email Period in | DDL | Days | Yes | Specify if search emails should be done with the period of days or hours.  
Max Recipients to Return | Integer | 20 | Yes | Specify how many recipients the action should return.  
Page Size | Integer | 100 | Yes | Specify the page size for the action to use when searching for emails.  
  
#### Playbook Use Cases Examples

Search for email information in IronPort when emails have Unicode in the subject.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
recipients | N/A | N/A  
  
##### JSON Result
    
    
    {
        "attributes": {
            "direction": "",
            "hostName": "",
            "senderGroup": "N/A",
            "sender": "reporting@smtp.inside-ironport.local",
            "replyTo": "N/A",
            "timestamp": "20 May 2020 01:00:04 (GMT +00:00)",
            "serialNumber": "42225C72BFBA18A2257D-C143F31DFB78",
            "mid": [
                229
            ],
            "senderIp": "N/A",
            "icid": 0,
            "messageStatus": {
                "229": "Delivered"
            },
            "mailPolicy": [],
            "isCompleteData": "N/A",
            "verdictChart": {
                "229": "00000000"
            },
            "senderDomain": "N/A",
            "recipient": [
                "test.user1@inside-ironport.local"
            ],
            "sbrs": "N/A"
    }
    

### Get Report

#### Description

Fetch specific IronPort report information.

**Note:** Mail_sender_ip_hostname_detail and mail_incoming_ip_hostname_detail reports work based on Google SecOps IP or Host entities; mail_users_detail works on Google SecOps User entity (with email address). Other reports are working without Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Report Type  
| Drop Down List | Default Value: None | Yes | The type of report to fetch. **Note:** mail_sender_ip_hostname_detail and mail_incoming_ip_hostname_detail reports work based on Google SecOps IP or Host entities; mail_users_detail works on Google SecOps User entity (with email address). Other reports are working without Google SecOps entities.  
Search Reports Data for Last X Days | Integer | 7 | Yes | Specify a time frame in days for which to search for reports data. By default is set to last 7 days.  
Max Records to Return | Integer | 20 | Yes | Specify how many records the action should return.  
  
#### Playbook Use Cases Examples

Get reporting information from the IronPort server for analysis of alert in Google SecOps.

#### Run On

  1. IP or HOST - mail_sender_ip_hostname_detail and mail_incoming_ip_hostname_detail reports
  2. USER - mail_users_detail report
  3. NONE - other report types are working without Google SecOps entities.



#### Action Results

##### Entity Enrichment

Entity enrichment should work as in existing action - if report returned data for specific Google SecOps entity, use returned data for enrichment.

See the existing action code for reference.

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "meta": {
            "totalCount": -1
        },
        "data": {
            "type": "mail_sender_ip_hostname_detail",
            "resultSet": {
                "time_intervals": [
                    {
                        "end_timestamp": 1590969599.0,
                        "counter_values": [
                            {
                                "counter_values": [
                                    0,
                                    0,
                                    0,
                                    0,
                                    8,
                                    8,
                                    0,
                                    0
                                ],
                                "ip_domain": "172.30.203.100",
                                "key": "irp-d1-dc01.inside-ironport.local"
                            }
                        ],
                        "begin_timestamp": 1588291200.0,
                        "end_time": "2020-05-31T23:59:00.000Z",
                        "begin_time": "2020-05-01T00:00:00.000Z"
                    },
                    {
                        "end_timestamp": 1593561599.0,
                        "counter_values": [
                            {
                                "counter_values": [
                                    0,
                                    0,
                                    6,
                                    0,
                                    5,
                                    11,
                                    6,
                                    0
                                ],
                                "ip_domain": "172.30.203.100",
                                "key": "irp-d1-dc01.inside-ironport.local"
                            }
                        ],
                        "begin_timestamp": 1590969600.0,
                        "end_time": "2020-06-30T23:59:00.000Z",
                        "begin_time": "2020-06-01T00:00:00.000Z"
                    }
                ],
                "counter_names": [
                    "detected_virus",
                    "detected_spam",
                    "threat_content_filter",
                    "total_dlp_incidents",
                    "total_clean_recipients",
                    "total_recipients_processed",
                    "total_threat_recipients",
                    "detected_amp"
                ]
            }
        }
    }
    

### Ping

#### Description

Test connectivity to the IronPort server with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
