---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/easy-vista/
title: EasyVista \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:25.993702+00:00
---

# EasyVista  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/easy-vista/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# EasyVista

**Important:** This integration refers to the EasyVista IT Service Management (ITSM) platform.

This document describes how to integrate EasyVista with Google Security Operations.

## Configure EasyVista integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://try.easyvista.com/api/v1/ | Yes | EasyVista API root to connect to.  
Account ID | String | N/A | Yes | EasyVista Account ID.  
Username | String | N/A | Yes | EasyVista username to use for connection.  
Password | Password | N/A | Yes | EasyVista password to use for connection.  
Verify SSL | Checkbox | Checked | No | Specify if the certificate validation should be enabled to check if certificate configured for API root is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the EasyVista instance with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "HREF": "https://try.easyvista.com/api/v1/70047/requests?max_rows=1",
        "record_count": "1",
        "total_record_count": "13015",
        "records": [
            {
                "HREF": "https://try.easyvista.com/api/v1/70047/requests/000002",
                "COMMENT": {
                    "HREF": "https://try.easyvista.com/api/v1/70047/requests/000002/comment"
                },
                "MAX_RESOLUTION_DATE_UT": "2010-11-19T19:00:00.000-05:00",
                "REQUEST_ID": "28452",
                "RFC_NUMBER": "000002",
                "SUBMIT_DATE_UT": "2011-11-17T19:00:00.000-05:00",
                "CATALOG_REQUEST": {
                    "CODE": "",
                    "CATALOG_REQUEST_PATH": "Incidents/Applications/Functional Domain/Exodata",
                    "HREF": "https://try.easyvista.com/api/v1/70047/catalog-requests/4816",
                    "SD_CATALOG_ID": "4816",
                    "TITLE_EN": "Exodata"
                },
                "STATUS": {
                    "STATUS_EN": "Closed",
                    "STATUS_GUID": "{C3D9DFA7-7A21-46C2-B3A3-8BC50C9FF4F3}",
                    "HREF": "https://try.easyvista.com/api/v1/70047/status/8",
                    "STATUS_ID": "8"
                },
                "RECIPIENT": {
                    "BEGIN_OF_CONTRACT": "1986-03-19",
                    "CELLULAR_NUMBER": "790-933-579",
                    "DEPARTMENT_PATH": "Sales/Direct/Services",
                    "E_MAIL": "abuxtehude@evtry.com",
                    "EMPLOYEE_ID": "10334",
                    "LAST_NAME": "Buxtehude, Andrew",
                    "LOCATION_PATH": "Europe/France/Marseille/Bldg 1/Floor 02/244",
                    "PHONE_NUMBER": "+33155859446"
                },
                "REQUESTOR": {
                    "BEGIN_OF_CONTRACT": "1986-03-19",
                    "CELLULAR_NUMBER": "790-933-579",
                    "DEPARTMENT_PATH": "Sales/Direct/Services",
                    "E_MAIL": "abuxtehude@evtry.com",
                    "EMPLOYEE_ID": "10334",
                    "LAST_NAME": "Buxtehude, Andrew",
                    "LOCATION_PATH": "Europe/France/Marseille/Bldg 1/Floor 02/244",
                    "PHONE_NUMBER": "+33155859446"
                },
                "LOCATION": {
                    "CITY": "",
                    "LOCATION_CODE": "",
                    "LOCATION_EN": "244",
                    "LOCATION_PATH": "Europe/France/Marseille/Bldg 1/Floor 02/244",
                    "HREF": "https://try.easyvista.com/api/v1/70047/locations/1610",
                    "LOCATION_ID": "1610"
                },
                "DEPARTMENT": {
                    "DEPARTMENT_CODE": "",
                    "DEPARTMENT_EN": "Services",
                    "DEPARTMENT_PATH": "Sales/Direct/Services",
                    "HREF": "https://try.easyvista.com/api/v1/70047/departments/37",
                    "DEPARTMENT_ID": "37",
                    "DEPARTMENT_LABEL": ""
                },
                "KNOWNERROR": {
                    "KNOWNERROR_PATH": "",
                    "KNOWN_PROBLEMS_ID": "",
                    "KP_NUMBER": "",
                    "QUESTION_EN": ""
                }
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully connected to the EasyVista instance with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
****_If not successful:_ Print "Failed to connect to the EasyVista instance! Error is {0}".format(exception.stacktrace) | General  
  
### Get EasyVista Ticket

#### Description

Get information on specific EasyVista ticket. Note: action is not working on Google SecOps entities, ticket identifier (rfc_number) should be provided.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket Identifier | String | N/A | Yes | EasyVista ticket identifier to get info for, eg S201001_000001.  
  
#### Playbook Use Cases Examples

Get information on the EasyVista ticket that is connected to the alert processed in Google SecOps.

#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

"General" response (https://try.easyvista.com/api/v1/70047/requests/ I200716_000001) - please note that below are example responses for getting description, comment, attachments and actions of the ticket.
    
    
    {
        "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
        "ANALYTICAL_CHARGE_PATH": "",
        "ANALYTICAL_CHARGE_ID": "",
        "ASSET_ID": "",
        "AVAILABLE_FIELD_1": "",
        "AVAILABLE_FIELD_2": "",
        "AVAILABLE_FIELD_3": "",
        "AVAILABLE_FIELD_4": "",
        "AVAILABLE_FIELD_5": "",
        "AVAILABLE_FIELD_6": "",
        "BUDGET_EFFECTIVE": "",
        "BUDGET_ID": "",
        "BUDGET_PLANNED": "",
        "CAN_BE_DUPLICATED": "0",
        "CI_ID": "",
        "CLICK_2_GET_INSTALL_RESULT": "",
        "COMMENT": {
            "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/comment"
        },
        "CONTINUITY_PLAN_ID": "",
        "COST_CENTER_ID": "",
        "CREATION_DATE_UT": "2020-07-16T04:00:24.000-04:00",
        "DELAY": "3840",
        "DEPARTMENT_PATH": "IT",
        "DEPARTMENT_ID": "100",
        "DESCRIPTION": {
            "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/description"
        },
        "DYNAMIC_DETAILS": {
            "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/dynamic_details"
        },
        "E_COST": "100.00",
        "E_DELAY": "",
        "E_SENTIMENT_ANALYSIS": "",
        "EFFECTIVE_CHANGE_DATE_END": "",
        "EFFECTIVE_CHANGE_DATE_START": "",
        "END_DATE_UT": "2020-07-28T23:13:54.000-04:00",
        "ESTIMATED_NET_PRICE": "",
        "ESTIMATED_PERCENT_COMPLETE": "",
        "EXPECTED_DATE_UT": "",
        "EXPECTED_DURATION": "",
        "EXPECTED_END_DATE_UT": "",
        "EXPECTED_START_DATE_UT": "",
        "EXTERNAL_REFERENCE": "",
        "FIRST_CALL_RESOLUTION": "0",
        "HOUR_PER_DAY": "",
        "IMPACT_ID": "3",
        "IMPUTATION_DATE": "",
        "INITIAL_SD_CATALOG_PATH": "",
        "INITIAL_SD_CATALOG_ID": "",
        "IS_FINANCIAL_COMPTED": "0",
        "IS_MAJOR_INCIDENT": "",
        "IS_TEMPLATE": "0",
        "KBASE_ID": "",
        "KNOWN_PROBLEMS_PATH": "",
        "KNOWN_PROBLEMS_ID": "",
        "LAST_DONE_BY_ID": "18376",
        "LAST_GROUP_ID": "12",
        "LAST_UPDATE": "2020-07-28T23:14:40.697-04:00",
        "LOCATION_PATH": "North America/USA/New York",
        "LOCATION_ID": "9762",
        "MARK_1": "",
        "MARK_2": "",
        "MAX_RESOLUTION_DATE_UT": "2020-07-16T17:00:00.000-04:00",
        "MS_PROJECT_IMPORT_VALIDATION_WAITING": "0",
        "NET_PRICE": "",
        "NET_PRICE_CUR_ID": "",
        "NEWS_ID": "",
        "NOT_DEDUCED_CALL": "",
        "ORDER_ID": "",
        "ORDER_NET_PRICE": "",
        "ORIGIN_TOOL_ID": "1",
        "OWNER_ID": "",
        "OWNING_GROUP_ID": "",
        "PARENT_REQUEST_ID": "",
        "PLANNED_CHANGE_DATE_END": "",
        "PLANNED_CHANGE_DATE_START": "",
        "PM_STATUS_ID": "",
        "PROJECT_ID": "",
        "PROJECT_NAME": "",
        "PROJECT_START_DATE_UT": "",
        "QTY": "",
        "RECIPIENT_ID": "18376",
        "RELEASE_ID": "",
        "RENTAL_NET_PRICE": "",
        "RENTAL_NET_PRICE_CUR_ID": "",
        "REQUALIFICATION_PROCESSING": "0",
        "REQUEST_ID": "42837",
        "REQUEST_ORIGIN_ID": "3",
        "REQUEST_PROJECT_ID": "",
        "REQUESTED_CHANGE_DATE_END": "",
        "REQUESTED_CHANGE_DATE_START": "",
        "REQUESTOR_FEEDBACK": "",
        "REQUESTOR_ID": "18376",
        "REQUESTOR_IP_ADDRESS": "",
        "REQUESTOR_PHONE": "+41798248341",
        "REQUIRED_DOWNTIME": "",
        "RFC_NUMBER": "I200716_000001",
        "RISK_AMOUNT": "",
        "RISK_DESCRIPTION": {
            "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/risk_description"
        },
        "RISK_LEVEL_ID": "",
        "ROOT_CAUSE_ID": "69",
        "SD_CATALOG_PATH": "Incidents/Equipment/Router",
        "SD_CATALOG_ID": "4606",
        "SEVERITY_ID": "40",
        "SLA_ID": "1",
        "STATUS_ID": "2",
        "SUBMIT_DATE_UT": "2020-07-16T04:00:24.000-04:00",
        "SUBMITTED_BY": "18376",
        "SYSTEM_AFFECTED": {
            "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/system_affected"
        },
        "SYSTEM_ID": "",
        "TIME_USED_TO_DELIVER_FEEDBACK": "",
        "TIME_USED_TO_SOLVE_REQUEST": "4320",
        "TITLE": "",
        "URGENCY_ID": "1",
        "VALIDATION_LEVEL_REQUIRED": "",
        "WAVE_ID_TARGET": "",
        "CATALOG_REQUEST": {
            "CODE": "46",
            "CATALOG_REQUEST_PATH": "Incidents/Equipment/Router",
            "HREF": "https://try.easyvista.com/api/v1/70047/catalog-requests/4606",
            "SD_CATALOG_ID": "4606",
            "TITLE_EN": "Router"
        },
        "STATUS": {
            "STATUS_EN": "Solved",
            "STATUS_GUID": "{DC97DD1D-0F35-4153-B0E1-0F2E0155365D}",
            "HREF": "https://try.easyvista.com/api/v1/70047/status/2",
            "STATUS_ID": "2"
        },
        "RECIPIENT": {
            "BEGIN_OF_CONTRACT": "",
            "CELLULAR_NUMBER": "+36666667776",
            "DEPARTMENT_PATH": "IT",
            "E_MAIL": "admin@evtry.com",
            "EMPLOYEE_ID": "18376",
            "LAST_NAME": "William",
            "LOCATION_PATH": "North America/USA/New York",
            "PHONE_NUMBER": "+41798248341"
        },
        "REQUESTOR": {
            "BEGIN_OF_CONTRACT": "",
            "CELLULAR_NUMBER": "+36666667776",
            "DEPARTMENT_PATH": "IT",
            "E_MAIL": "admin@evtry.com",
            "EMPLOYEE_ID": "18376",
            "LAST_NAME": "William",
            "LOCATION_PATH": "North America/USA/New York",
            "PHONE_NUMBER": "+41798248341"
        },
        "LOCATION": {
            "CITY": "",
            "LOCATION_CODE": "",
            "LOCATION_EN": "New York",
            "LOCATION_PATH": "North America/USA/New York",
            "HREF": "https://try.easyvista.com/api/v1/70047/locations/9762",
            "LOCATION_ID": "9762"
        },
        "DEPARTMENT": {
            "DEPARTMENT_CODE": "",
            "DEPARTMENT_EN": "IT",
            "DEPARTMENT_PATH": "IT",
            "HREF": "https://try.easyvista.com/api/v1/70047/departments/100",
            "DEPARTMENT_ID": "100",
            "DEPARTMENT_LABEL": ""
        },
        "KNOWNERROR": {
            "KNOWNERROR_PATH": "",
            "KNOWN_PROBLEMS_ID": "",
            "KP_NUMBER": "",
            "QUESTION_EN": ""
        }
    }
    

Description:
    
    
    {
        "COMMENT": "Here, your description",
        "PARENT_HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
        "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/comment"
    }
    

Comment:
    
    
    {
        "DESCRIPTION": "REST API Update - This is a test comment 3, is it replacing old one?\r\nthis is solved",
        "PARENT_HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
        "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/description"
    }
    

Attachment:
    
    
    {
        "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001/documents",
        "PARENT_HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
        "Documents": [
            {
                "HREF": "https://try.easyvista.com/autoconnect_mail.php?field1=5C0F051E5B0F056B1E31&field2=&field3=&docpath=70047/Documents/40000_ff73bce22220ac5b8ce10cefd876a5c8a2b09fec&docname=testfile.txt",
                "PARENT_HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
                "DOCUMENT_ID": "40000_ff73bce22220ac5b8ce10cefd876a5c8a2b09fec&docname=testfile.txt",
                "DDL_HREF": "https://try.easyvista.com/api/v1/70047/documents/40000_ff73bce22220ac5b8ce10cefd876a5c8a2b09fec&docname=testfile.txt"
            },
            {
                "HREF": "https://try.easyvista.com/autoconnect_mail.php?field1=5C0F051E5B0F056B1E3C&field2=&field3=&docpath=70047/Documents/40000_284466a573e227bb632d977f3c4a399016d94fe6&docname=testfile2.txt",
                "PARENT_HREF": "https://try.easyvista.com/api/v1/70047/requests/I200716_000001",
                "DOCUMENT_ID": "40000_284466a573e227bb632d977f3c4a399016d94fe6&docname=testfile2.txt",
                "DDL_HREF": "https://try.easyvista.com/api/v1/70047/documents/40000_284466a573e227bb632d977f3c4a399016d94fe6&docname=testfile2.txt"
            }
        ]
    }
    

Actions:
    
    
    {
        "HREF": "https://try.easyvista.com/api/v1/70047/actions?search=REQUEST.RFC_NUMBER:I200904_000001",
        "record_count": "6",
        "total_record_count": "6",
        "records": [
            {
                "HREF": "https://try.easyvista.com/api/v1/70047/actions/79439",
                "ACTION_ID": "79439",
                "ACTION_LABEL_EN": "Analysis & Resolution",
                "ACTION_NUMBER": "0",
                "DONE_BY_ID": "",
                "EXPECTED_START_DATE_UT": "",
                "LOCATION": {
                    "CITY": "",
                    "LOCATION_CODE": "",
                    "LOCATION_EN": "-",
                    "LOCATION_PATH": "",
                    "HREF": "https://try.easyvista.com/api/v1/70047/locations/6",
                    "LOCATION_ID": "6"
                },
                "DONE_BY": {
                    "BEGIN_OF_CONTRACT": "",
                    "CELLULAR_NUMBER": "",
                    "DEPARTMENT_PATH": "",
                    "E_MAIL": "",
                    "EMPLOYEE_ID": "",
                    "LAST_NAME": "",
                    "LOCATION_PATH": "",
                    "PHONE_NUMBER": ""
                },
                "REQUEST": {
                    "MAX_RESOLUTION_DATE_UT": "2020-09-04T17:00:00.000-04:00",
                    "REQUEST_ID": "42845",
                    "HREF": "https://try.easyvista.com/api/v1/70047/requests/I200904_000001",
                    "RFC_NUMBER": "I200904_000001",
                    "SUBMIT_DATE_UT": "2020-09-04T03:07:26.000-04:00"
                }
            }]
    }
    

##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully returned EasyVista information for the ticket {0}".format(ticket_id)****_If is_success=False, for example_**,** _wrong ticket id was provided, didn't get the results:_ Print "Failed to get EasyVista information for the ticket {0}! Error is {1}".format(ticket_id,exception.stacktrace)  
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
Table | **Table Name:** "EasyVista ticket {0} information:".format(ticket_id) **Table Columns:** Parameter, Value`HREF``DESCRIPTION``COMMENT``CREATION_DATE_UT``END_DATE_UT``LAST_UPDATE``DEPARTMENT_PATH``DEPARTMENT_ID``CATALOG_REQUEST.CATALOG_REQUEST_PATH``STATUS.STATUS_EN``RECIPIENT.E_MAIL``REQUESTOR.E_MAIL``LOCATION.LOCATION_EN``LOCATION.LOCATION_PATH``ATTACHMENTS - attachments names CSV list (docname)``Actions - action names CSV list (ACTION_LABEL_EN)` | General  
  
### Add Comment to Ticket

#### Description

Add a comment to the EasyVista ticket. Note: action is not working on Google SecOps entities, action input parameters should be provided.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket Identifier | String | N/A | Yes | EasyVista ticket identifier to get info for.  
Comment | String | N/A | Yes | Comment to add to EasyVista ticket.  
  
#### Playbook Use Cases Examples

Add a comment to the EasyVista ticket as a part of the investigation.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully added a comment to the EasyVista ticket {0}".format(ticket_id)****_If is_success=False, for example_**,** _wrong ticket id was provided, didn't get the results:_ Print "Failed to add a comment to the EasyVista ticket {0}! Error is {1}".format(ticket_id,exception.stacktrace)  
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print print "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
### Wait for the Ticket Update

#### Description

Action pauses the playbook execution and periodically connects to EasyVista until timeout and checks if the specified ticket got an update. Action also can monitor specific field for the update, once that field is updated - action completes and fetches back the updated ticket information.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket Identifier | String | N/A | Yes | EasyVista ticket identifier to get info for.  
Field To Monitor | DDL  | Possible values: Status Comment Attachments Actions | No | EasyVista ticket field to monitor for the update.  
  
#### Playbook Use Cases Examples

Wait in the Google SecOps playbook while some process will be completed and logged in Easyvista.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully got a an update for ticket {0}".format(ticket_id).****_If is_success=False, for example_**,** _wrong ticket id was provided, didn't get the results:_ Print "Failed to get an update for ticket {0}! Error is {1}".format(ticket_id,exception.stacktrace)  
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print print "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
Table | **Table Name:** "EasyVista ticket {0} information:".format(ticket_id)`HREF``DESCRIPTION``COMMENT``CREATION_DATE_UT``END_DATE_UT``LAST_UPDATE``DEPARTMENT_PATH``DEPARTMENT_ID``CATALOG_REQUEST.CATALOG_REQUEST_PATH``STATUS.STATUS_EN``RECIPIENT.E_MAIL``REQUESTOR.E_MAIL``LOCATION.LOCATION_EN``LOCATION.LOCATION_PATH``ATTACHMENTS - attachments names CSV list (docname)``Actions - action names CSV list (ACTION_LABEL_EN)` | General  
  
### Close EasyVista Ticket

#### Description

Close the EasyVista ticket based on the provided parameters. Note: action is not working on Google SecOps entities, ticket identifier (rfc_number) should be provided.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket Identifier | String | N/A | Yes | EasyVista ticket identifier, eg S201001_000001.  
Comment | String | N/A | No | The comment explaining the closing of the ticket.  
Actions Close Date | String | N/A | No | Closing date of open actions associated with the ticket and the anticipated closure action.The date should be in the following format: MM/DD/YYYY HH:MM:SS.If the wrong format is provided, action will use current DateTime as a close date.  
Delete ongoing actions? | Checkbox | Unchecked | No | Specify whether to delete the ticket ongoing actions on ticket closing.  
  
#### Playbook Use Cases Examples

Close the EasyVista ticket that is connected to the alert been processed.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type (Entity / General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (server returned status 201, is_success=true):_ Print "Successfully closed EasyVista ticket {0}".format(EasyVista_ticket)****_If successful, but wrong date is provided (server returned status 201, is_success=true):_ Print "Wrong date format is provided, EasyVista ticket {0} closed with current date time.".format(EasyVista_ticket)  
****_If is_success=False, for example wrong ticket id was provided, server returned error:_ Print "Failed to close EasyVista ticket {0}! Error is {1}".format(EasyVista_ticket,exception.stacktrace)**The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print print "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
