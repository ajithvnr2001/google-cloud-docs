---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ca-service-desk-manager/
title: CA Service Desk Manager \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:01.848081+00:00
---

# CA Service Desk Manager  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ca-service-desk-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CA Service Desk Manager

This document describes how to integrate CA Service Desk Manager with Google Security Operations.

## Configure CA Service Desk Manager integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | N/A | Yes | Address of the CA Service Desk Manager instance.  
Username | String | N/A | Yes | The email address of the user which should be used to connect to CA Service Desk Manager.  
Password | Password | N/A | Yes | The password of the according user.  
Ticket Fields | String | customer.combo_name, category.sym,status.sym, priority.sym,active, log_agent.combo_name, assignee.combo_name, group.combo_name, affected_service.name, severity.sym,urgency.sym, impact.sym,problem.ref_num, resolution_code.sym, call_back_date, change.chg_ref_num, caused_by_chg.chg_ref_num, external_system_ticket, resolution_method.sym, symptom_code.sym, requested_by.combo_name, persistent_id, summary,description, open_date,last_mod_dt, resolve_date,close_date, ref_num | Yes | Ticket fields of the CA Service Desk Manager integration.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add Comment

#### Description

Add comment to a CA Service Desk incident. Adding comments will add text in the tickets, and provide a way for you to include notes in the ticket.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Incident's ref num. Example: 338  
Comment | String | N/A | Yes | Comment to add to an incident.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
### Assign Incident to User

#### Description

Assign an incident to a specific user.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Incident number.  
Username | String | N/A | Yes | Username to assign the incident to.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
### Assign to Group

#### Description

Assign an incident to a particular group.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Incident number.  
Group | String | N/A | Yes | Group to assign the incident to.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ticket_id | N/A | N/A  
  
### Change Ticket Status

#### Description

Change CA Desk Manager ticket status.

#### How to change ticket status

  1. View the ticket.
  2. From the Ticket Detail window, select **Activities** , then **Update Status** (a Status Change Request window will open).
  3. Use the drop-down under **New Status** to choose from the list of provided statuses. (If you want to save the comments entered in the field of description, you MUST switch from one state to another).
  4. Click the **Save** button to save your changes and return to the ticket. The activity is added to the **Activities** Tab.



#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Incident number.  
Status | String | N/A | Yes | Incident status to change. Example: Closed.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
### Close Ticket

#### Description

Close an incident in CA Service Desk manager. Once the issue has been resolved, update the status field to "Resolved". If there is no additional action on the ticket after two business days, the ticket will automatically change its status to closed. Once the ticket is in a closed state, a customer survey will be delivered (if applicable).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Incident number.  
Close Reason | String | N/A | Yes | The description which can be used in the close activity log.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
### Create Ticket

#### Description

Create new ticket in CA Service Desk. Fetch data from CSV files located in a specific folder, and convert this data to alerts in the Google SecOps system.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Summary | String | N/A | Yes | Incident's summary text.  
Description | String | N/A | Yes | Incident's description text.  
Category Name | String | N/A | Yes | Incident's area name. Example: Software.  
Group Name | String | N/A | Yes | Group name. Example: Test.  
Username | String | N/A | Yes | User name.  
Custom Fields | JSON | N/A | No | Specify a JSON object containing all of the needed fields and values. The structure is the following:` { "field":"value" } ` If the same field is provided in the "Custom Fields" parameter and other parameters, the "Custom Fields" parameter value has priority.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ticket_id | N/A | N/A  
  
### Ping

#### Description

Verifies that the user has a connection to CA Service Desk Manager via the user's device.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
### Search Tickets

#### Description

Search tickets in CA Desk Manager by field.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | No | Incident ID to filter by.  
Summary | String | N/A | No | Summary content to filter by.  
Description | String | N/A | No | Description content to filter by.  
Status | String | N/A | No | Filter by status. Example: Open.  
Days Backwards | String | N/A | No | Get results from 'x' days backwards. Example: 5.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "severity.sym": "None",
            "resolution_code.sym": "None",
            "group.combo_name": "None",
            "resolve_date": "None",
            "caused_by_chg.chg_ref_num": "None",
            "log_agent.combo_name": "TEST",
            "requested_by.combo_name": "None",
            "resolution_method.sym": "None",
            "problem.ref_num":"None",
            "change.chg_ref_num": "None",
            "affected_service.name": "None",
            "priority.sym": "3",
            "customer.combo_name": "TEST",
            "call_back_date": "None",
            "assignee.combo_name": "AnalystUserOther",
            "status": "OP",
            "urgency.sym": "3-Quickly",
            "impact.sym": "3-Single Group",
            "description": "lalal",
            "symptom_code.sym": "None",
            "external_system_ticket": "None",
            "last_mod_dt": "1547368725",
            "active": "1",
            "open_date": "1517743983",
            "category.sym": "None",
            "status.sym": "Open",
            "persistent_id": "cr:400767",
            "summary": "lala",
            "close_date": "None"
        }
    ]
    

### Sync Ticket History

#### Description

Fetch and attach the entire ticket history to an alert.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment Type Field | String | N/A | No | Ticket type. Example: type.sym.  
Analyst Name Field | String | N/A | No | Analyst Name. Example: analyst.combo_name.  
TimeStamp Field | String | N/A | No | Time field. Example: time_stamap.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "time_stamp": "1546944096",
            "analyst.combo_name": "Analyst",
            "type.sym": "Log Comment",
            "description": "Tests Comments."
        }
    ]
    

### Wait for Status Change

#### Description

The waiting period of the change of the ticket status.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Ticket ID | String | N/A | Yes | Target ticket ID.  
Expected Ticket Status Name | String | N/A | Yes | Expected status.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    {
        "severity.sym": "None",
        "resolution_code.sym": "None",
        "urgency.sym": "3-Quickly",
        "resolve_date": "None",
        "caused_by_chg.chg_ref_num": "None",
        "log_agent.combo_name": "Siemplify",
        "requested_by.combo_name": "None",
        "resolution_method.sym": "None",
        "problem.ref_num": "None",
        "change.chg_ref_num": "None",
        "affected_service.name": "None",
        "priority.sym": "3",
        "customer.combo_name": "Siemplify",
        "call_back_date": "None",
        "assignee.combo_name": "AnalystUserOther",
        "status": "OP",
        "group.combo_name": "None",
        "impact.sym": "3-Single Group",
        "description": "lalal",
        "symptom_code.sym": "None",
        "external_system_ticket": "None",
        "last_mod_dt": "1547368725",
        "active": "1",
        "open_date": "1517743983",
        "category.sym": "None",
        "status.sym": "Open",
        "persistent_id": "cr:400767",
        "summary": "lala",
        "close_date": "None"
    }
    

## Connectors

### CA Service Desk Connector

#### Description

Fetch tickets from CA Desk Manager.

### Configure CA Service Desk Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Environment | DDL | N/A | Yes | Select the required environment. For example, "Customer One".  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection. For example, "every day".  
Product Field Name | String | device_product | Yes | The field name used to determine the device product. For example, device_product  
Event Field Name | String | description | Yes | The field name used to determine the event name (sub-type). For example, "name".  
Script Timeout (Seconds) | Integer | 60 | Yes | The timeout limit (in seconds) for the python process running current script.  
API Root | String | N/A | Yes | Example: http://x.x.x.x:8080  
Username | String | N/A | Yes | Username.  
Password | Password | N/A | Yes | Password.  
Ticket ID Field | String | ref_num | Yes | Incident id field key as it appear at the ticket JSON. Example: ref_num  
Start Time Field | String | open_date | Yes | Represent the key of the start time at the ticket. Example: open_date  
End Time Field | String | last_mod_dt | Yes | Represent the key of the end time at the ticket. Example: last_mod_dt  
Category Default Field | String | category | Yes | Represent the category key at the ticket. Example: category  
Category Fallback Field | String | category.sym | Yes | Example: category.sym  
User ID Field | String | customer.combo_name | Yes | Filter by user. Example: customer.combo_name  
Ticket Fields | String | customer.combo_name, category.sym, status.sym, priority.sym, active, log_agent.combo_name, assignee.combo_name, group.combo_name, affected_service.name, severity.sym, urgency.sym,impact.sym, problem.ref_num, resolution_code.sym, call_back_date, change.chg_ref_num, caused_by_chg.chg_ref_num, external_system_ticket, resolution_method.sym, symptom_code.sym, requested_by.combo_name, persistent_id, summary, description, open_date, last_mod_dt,resolve_date, close_date,ref_num | Yes | Comma-separated. Example: customer.combo_name, category.sym,status.sym, priority.sym,active, log_agent.combo_name, assignee.combo_name, group.combo_name, affected_service.name, severity.sym,urgency.sym, impact.sym,problem.ref_num, resolution_code.sym,call_back_date,change.chg_ref_num, caused_by_chg.chg_ref_num, external_system_ticket, resolution_method.sym, symptom_code.sym, requested_by.combo_name, persistent_id,summary, description,open_date, last_mod_dt,resolve_date, close_date,ref_num  
List of Users to Ignore | String | N/A | No | Comma-separated. Filter incidents by users to ignore.  
Categories List | String | N/A | No | Filter incidents by categories.  
Groups List | String | N/A | No | Filter incidents by groups.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

## Jobs

### CA Close Ticket in CA for Closed Case

#### Description

Sync closure of the tickets at the CA Desk Manager with Google SecOps cases closure.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | http://x.x.x.x: | Yes | N/A  
Username | String | N/A | Yes | N/A  
Password | String | N/A | Yes | N/A  
Group Filter | String | Test | Yes | N/A  
Group Field | String | group.combo_name | Yes | N/A  
Ticket Final Status | String | Closed | Yes | N/A  
Script Name | String | TEST CLOSE | Yes | N/A  
  
### Sync Comments

#### Description

Sync comments from CA Desk Manager to Google SecOps.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | http://x.x.x.x: | Yes | N/A  
Username | String | N/A | Yes | N/A  
Password | String | N/A | Yes | N/A  
Summary Field | String | summery.combo_name | Yes | N/A  
Ticket Fields | String | summery.combo_name, customer.combo_name, category.sym,status.sym, priority.sym,active, log_agent.combo_name, assignee.combo_name, group.combo_name, affected_service.name, severity.sym,urgency.sym, impact.sym,problem.ref_num, resolution_code.sym, call_back_date, change.chg_ref_num, caused_by_chg.chg_ref_num, external_system_ticket, resolution_method.sym, symptom_code.sym, requested_by.combo_name, persistent_id, summary, description, open_date, last_mod_dt, resolve_date, close_date, ref_num | Yes | N/A  
Script Name | String | Test | Yes | N/A  
Ticket Type Field | Checkbox | Checked | No | N/A  
Analyst Type Field | Checkbox | Checked | No | N/A  
Time Stamp Field | Checkbox | Checked | No | N/A  
Timezone String | Checkbox | Checked | No | N/A  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
