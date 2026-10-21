---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ironscales/
title: IRONSCALES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:11.730460+00:00
---

# IRONSCALES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ironscales/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IRONSCALES

This document provides guidance on how to integrate IRONSCALES with Google SecOps.

## Use Cases

  1. Classify Incident
  2. Incident Details
  3. Mitigation Impersonation Details
  4. Mitigation Incidents Details
  5. Mitigations Per Mailbox
  6. Configure AWS GuardDuty Integration on Google Security Operations



## Configure IRONSCALES integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://members.ironscales.com/ | Yes | API Root of the IRONSCALES instance.  
API Token | String | N/A | Yes | API token of IRONSCALES.  
Company ID | String | N/A | Yes | Specify the company ID to use in IRONSCALES.  
Is Partner | Checkbox | Unchecked | Yes | Specify whether Company ID from above is a partner ID as well.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the IRONSCALES server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to IRONSCALES with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** print "Successfully connected to the IRONSCALES server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** print "Failed to connect to the IRONSCALES server! Error is {0}".format(exception.stacktrace) | General  
  
### Classify Incident

#### Description

Change incidents classification

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **DDL Values** | **Is Mandatory** | **Description**  
---|---|---|---|---|---  
Incidents IDs | String | N/A |  | Yes | Specify IDs of incidents to classify.  
New Classification | DDL | Attack | AttackFalse positiveSpam | Yes | Specify the new classification for these incidents. Note: For Phishing Attack classification enter "Attack", for False positive: "False Positive", for spam: "Spam".  
Classifying User Email | User | N/A |  | Yes | Specify which user is performing the classification by providing his mail address. Note: This email address should be recognized by IRONSCALES.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:****For found incident IDs:** print "Successfully classified incidents to {new_classification}. Incident IDs: {Ids_list}."****  
**For not found incident IDs -** print "Couldn't classify the following incident IDs: {Ids_list}."  
******The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Classify Incident". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Incident Details

#### Description

Get full incident details from IRONSCALES

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Incidents IDs | String | N/A | Yes | Specify IDs of incidents to fetch details for.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "company_id": "3911",
        "company_name": "SIEMPLIFY",
        "incident_id": "753277",
        "classification": "Attack",
        "first_reported_by": "בונד ג'יימס",
        "first_reported_date": "2020-06-17T15:49:56.755Z",
        "affected_mailbox_count": 2,
        "sender_reputation": "medium",
        "banner_displayed": null,
        "sender_email": "demo@ironscales.com",
        "reply_to": null,
        "spf_result": null,
        "sender_is_internal": false,
        "themis_proba": null,
        "themis_verdict": "Insufficient Data",
        "mail_server": {
            "host": "AM6PR02MB4184.eurprd02.prod.outlook.com",
            "ip": "2603:10a6:20b:51::26"
        },
        "federation": {
            "companies_affected": 2,
            "companies_marked_phishing": 2,
            "companies_marked_spam": 0,
            "companies_marked_fp": 0,
            "companies_unclassified": 0,
            "phishing_ratio": 1.0
        },
        "reports": [
            {
                "name": "בונד ג'יימס",
                "email": "james.bond@siemplifycyarx.onmicrosoft.com",
                "subject": "FW: Carey Hart",
                "sender_email": "demo@ironscales.com",
                "mail_server": {
                    "host": "AM6PR02MB4184.eurprd02.prod.outlook.com",
                    "ip": "2603:10a6:20b:51::26"
                },
                "headers": [
                    {
                        "name": "Received",
                        "value": "from DB7PR05MB5787.eurprd05.prod.outlook.com (2603:10a6:20b:b2::22) by AM6PR05MB5957.eurprd05.prod.outlook.com with HTTPS via AM6PR08CA0010.EURPRD08.PROD.OUTLOOK.COM; Wed, 17 Jun 2020 15:44:55 +0000"
                    },
                    {
                        "name": "Received",
                        "value": "from AM5PR0601CA0039.eurprd06.prod.outlook.com (2603:10a6:203:68::25) by DB7PR05MB5787.eurprd05.prod.outlook.com (2603:10a6:10:86::14) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.3088.18; Wed, 17 Jun 2020 15:44:54 +0000"
                    }
                ]
            }
        ],
        "links": [
            {
                "url": "https://en.wikipedia.org/wiki/Carey_Hart#cite_note-Gale-1",
                "name": "[1]"
            },
            {
                "url": "https://en.wikipedia.org/wiki/Americans",
                "name": "American"
            }
        ],
        "attachments": []
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**If successful:****For successful incident IDs:** print "Successfully fetched incidents details from IRONSCALES. incident IDs: {IDS_list}."****  
**For not found incident IDs:** print "Action wasn't able to fetch incident details for incident IDs: {IDs_list} Reason : incidents IDs weren't found."  
******The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Get Incident Details" : {0}''.format(error.Stacktrace) | General  
  
### Get Mitigation Impersonation Details

#### Description

Get latest company impersonation incidents.

Results are limited to the latest 1000 incidents, a message will appear displaying if the amount of incidents in the period is over this limit.

Please note that the IDs returned here are of impersonation attempts, not incidents or reports, so searching these IDs in other endpoints will not return the expected incidents

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **DDL Values** | **Description**  
---|---|---|---|---|---  
Period | DDL | Last 24 hours | Yes | Last 24 hoursLast 7 daysLast 90 daysLast 180 daysLast 360 daysCurrent year to dateAll time | Specify the time period for which you would like to get mitigation impersonation details for.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "page": null,
        "total_pages": null,
        "incidents": [
            {
                "incidentID": 100694130,
                "mailboxId": 1305177,
                "remediatedTime": "2020-12-08T19:18:17.592631+00:00",
                "mailboxEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "jamesbondtest6@gmail.com",
                "subject": "testing",
                "reportedBy": "IronSights",
                "incidentType": "Display Name Impersonation",
                "resolution": "",
                "remediations": 1
            },
            {
                "incidentID": 100694131,
                "mailboxId": 1305177,
                "remediatedTime": "2020-12-08T19:18:18.024769+00:00",
                "mailboxEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "jamesbondtest6@gmail.com",
                "subject": "testing",
                "reportedBy": "IronSights",
                "incidentType": "Display Name Impersonation",
                "resolution": "",
                "remediations": 1
            },
            {
                "incidentID": 100696686,
                "mailboxId": 1305177,
                "remediatedTime": "2020-12-08T19:25:43.216123+00:00",
                "mailboxEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "jamesbondtest6@gmail.com",
                "subject": "n",
                "reportedBy": "IronSights",
                "incidentType": "Display Name Impersonation",
                "resolution": "",
                "remediations": 1
            }
        ],
        "messages": []
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** print "Successfully fetched details of impersonation mitigations for the +{period}"  
****  
**The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Get Mitigation impersonation details". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Incident Mitigation Details

#### Description

Get latest company mitigation details.

Results are limited to the latest 1000 incidents, a message will appear displaying if the amount of incidents in the period is over this limit.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **DDL Values** | **Description**  
---|---|---|---|---|---  
Period | DDL | Last 24 hours | Yes | Last 24 hoursLast 7 daysLast 90 daysLast 180 daysLast 360 daysCurrent year to dateAll time | Specify the time period for which you would like to get incident mitigation details for.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "messages": [],
        "incidents": [
            {
                "incidentID": 1251713,
                "incidentState": 2,
                "remediatedTime": "2020-12-07T15:22:38.798292+00:00",
                "affectedMailboxCount": 6,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "crazywiz7@abv.bg",
                "subject": "Re: FW: Carey Hart",
                "threatType": "False Positive",
                "detectionType": "User Report",
                "reportedBy": "AI-Powered Incident Response"
            },
            {
                "incidentID": 1251683,
                "incidentState": 7,
                "remediatedTime": "2020-12-07T15:20:18.546309+00:00",
                "affectedMailboxCount": 2,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "crazywiz7@abv.bg",
                "subject": "Re: FW: Carey Hart",
                "threatType": "Spam",
                "detectionType": "User Report",
                "reportedBy": "AI-Powered Incident Response"
            },
            {
                "incidentID": 1257956,
                "incidentState": 1,
                "remediatedTime": "2020-12-08T13:40:50.730184+00:00",
                "affectedMailboxCount": 4,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "senderEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "subject": "Testing",
                "threatType": "Unclassified",
                "detectionType": "User Report",
                "reportedBy": "AI-Powered Incident Response"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** print "Successfully fetched details of incident mitigations for the +{period}"  
******The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Get Incident Mitigation details". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Mitigations Per Mailbox

#### Description

Get details of mitigations per mailbox.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **DDL Values** | **Description**  
---|---|---|---|---|---  
Incident IDs | CSV | N/A | Yes | - | Provide a comma separated list of incident IDs to search for.  
Period | DDL | All Time | No | Last 24 hoursLast 7 daysLast 90 daysLast 180 daysLast 360 daysCurrent year to dateAll time | Specify the time period for which you would like to get mitigations per mailbox for.  
Max Pages to Fetch | Integer | 1 | Yes | - | Specify the maximum number of pages you would like to fetch.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "page": 1,
        "total_pages": 1,
        "mitigations": [
            {
                "incidentID": 1257956,
                "mitigationID": 48919694,
                "incidentState": "False Positive",
                "remediatedTime": null,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "subject": "Testing",
                "senderEmail": "bruce.wayne@abv.bg",
                "senderIP": "2603:10a6:20b:aa::19",
                "reportedBy": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "resolution": "False Positive",
                "spfResult": "fail"
            },
            {
                "incidentID": 1257956,
                "mitigationID": 48919695,
                "incidentState": "False Positive",
                "remediatedTime": null,
                "mailboxId": 1305177,
                "mailboxEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "subject": "Testing",
                "senderEmail": "bruce.wayne@abv.bg",
                "senderIP": "2603:10a6:20b:aa::19",
                "reportedBy": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "resolution": "False Positive",
                "spfResult": "fail"
            },
            {
                "incidentID": 1257956,
                "mitigationID": 48918977,
                "incidentState": "False Positive",
                "remediatedTime": null,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "subject": "Testing",
                "senderEmail": "bruce.wayne@abv.bg",
                "senderIP": "2603:10a6:20b:aa::19",
                "reportedBy": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "resolution": "False Positive",
                "spfResult": "fail"
            },
            {
                "incidentID": 1257956,
                "mitigationID": 48918344,
                "incidentState": "False Positive",
                "remediatedTime": null,
                "mailboxId": 1305171,
                "mailboxEmail": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "subject": "Testing",
                "senderEmail": "james.bond@siemplifycyarx.onmicrosoft.com",
                "senderIP": "2603:10a6:20b:aa::19",
                "reportedBy": "bruce.wayne@siemplifycyarx.onmicrosoft.com",
                "resolution": "False Positive",
                "spfResult": "fail"
            },
            {
                "incidentID": 1264413,
                "mitigationID": 49068886,
                "incidentState": "Attack",
                "remediatedTime": "2020-12-09T16:22:43.096Z",
                "mailboxId": 1960971,
                "mailboxEmail": "emulator@siemplifycyarx.onmicrosoft.com",
                "subject": "[EMULATED - DANGEROUS - 8] Change Of Account In Payroll",
                "senderEmail": "",
                "senderIP": "52.37.31.151",
                "reportedBy": "emulator@siemplifycyarx.onmicrosoft.com",
                "resolution": "Phishing Attack",
                "spfResult": "pass"
            },
            {
                "incidentID": 1264413,
                "mitigationID": 49066007,
                "incidentState": "Attack",
                "remediatedTime": "2020-12-09T16:05:35.650Z",
                "mailboxId": 1960971,
                "mailboxEmail": "emulator@siemplifycyarx.onmicrosoft.com",
                "subject": "[EMULATED - DANGEROUS - 2] Change Of Account In Payroll",
                "senderEmail": "",
                "senderIP": "52.37.31.151",
                "reportedBy": "emulator@siemplifycyarx.onmicrosoft.com",
                "resolution": "Phishing Attack",
                "spfResult": "pass"
            },
            {
                "incidentID": 1264413,
                "mitigationID": 49064037,
                "incidentState": "Attack",
                "remediatedTime": "2020-12-09T15:49:05.567Z",
                "mailboxId": 1960971,
                "mailboxEmail": "emulator@siemplifycyarx.onmicrosoft.com",
                "subject": "[EMULATED - DANGEROUS - 2] Change Of Account In Payroll",
                "senderEmail": "",
                "senderIP": "52.37.31.151",
                "reportedBy": "emulator@siemplifycyarx.onmicrosoft.com",
                "resolution": "Phishing Attack",
                "spfResult": "pass"
            }
        ],
        "messages": []
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully fetched details of incident mitigations per mailbox for the +{period}"  
****  
**If action has more than one iteration (more than one page) :** print "Continuing...fetching incident mitigations per mailbox, page (current_page_number) out of (total_page_number) "  
******The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Get Mitigations Per Mailbox". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
