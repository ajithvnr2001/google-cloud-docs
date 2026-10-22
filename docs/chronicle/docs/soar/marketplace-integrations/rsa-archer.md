---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-archer/
title: RSA Archer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:34.527601+00:00
---

# RSA Archer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-archer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RSA Archer

This document provides guidance on how to integrate RSA Archer with Google SecOps.

## Configure RSA Archer integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory  
---|---|---|---  
API Root | String | http://x.x.x.x/rsaarcher | Yes  
Instance Name | String | N/A | Yes  
Username | String | N/A | Yes  
Password | Password | N/A | Yes  
Verify SSL | Checkbox | Checked | Yes  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Create Incident

#### Description

Create a new incident. In the Create an Incident dialog, analysts can create an incident from selected events in the events view. The incident is then available to incident responders working in respond.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Application Name | String | Incidents | No | Specify an application name for the incident. Default: Incidents.  
Custom Mapping File | String | N/A | No | Specify an absolute path to the file that contains all of the required mapping. If "Remote File" is enabled, then provide a URL that contains the mapping file. Please refer to action documentation for the additional information.  
Custom Fields | String | N/A | No | Specify a JSON object of fields that need to be used, when creating an incident . Example: {"Category": "Malware"}  
Remote File | Checkbox | N/A |  | If enabled, action will treat value provided in "Custom Mapping File" as a URL and try to fetch a file from it.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
content_id | N/A | N/A  
  
##### Structure of the Mapping File

In order to work with a mapping file you need to use the proper format. Currently, mapping allows you to define cross-reference field entries.

The structure of the file is the following:
    
    
        {
        "type_9": {
            "{Cross-reference field name}": {
                "{Cross-reference field value}": "{content id of the cross-reference field value}",
                "{Cross-reference field value 2}": "{content id of the cross-reference field value 2}"
            }
        }
    }
    
    

Example. You have an incident application that you want to link to a certain facility application. In that case the mapping file will look like this:
    
    
    {
        "type_9": {
            "Facility": {
                "Business Department": "20202021",
                "Developers": "20011101"
            }
        }
    }
    
      ```
    
    You need to use a mapping file, when actions are not able to automatically
    retrieve content id. In all of the other cases, this step is not needed.
    
    #####  JSON Result
    
    ```json
    {
        "@odata.context": "http://172.30.202.238/RSAarcher/contentapi/Incidents(249459)/$metadata#Incidents/$entity",
        "Incidents_Id": 249459,
        "Additional_Access": [],
        "Additional_Notification_Recipients": [],
        "Address": "<p>Fifth street </p>",
        "Affected_Business_Unit": [],
        "Batch_File_Format": [],
        "Business_Continuity_Plans": [],
        "Business_Impact_Analysis_Archive": [],
        "Category": [
            "Harassment"
        ],
        "Cause": null,
        "City": "Vienna",
        "Corrective_Actions": null,
        "Country": [],
        "Current_Status": [],
        "Customer_Data": [],
        "Customer_Data_Details": null,
        "Data_Encrypted": [],
        "Date_Created": "2020-05-08T12:17:37.187+02:00",
        "DateTime_Closed": null,
        "DateTime_Occurred": "2020-05-06T05:00:00+02:00",
        "DateTime_Reported": "2020-05-08T12:15:00+02:00",
        "Days_Open": 6,
        "Default_Record_Permissions": [
            "IM: Admin",
            "IM: Read Only",
            "BCM: Admin"
        ],
        "Desktop_Policy_Enabled": [],
        "Discovery_Policy_Enabled": [],
        "DLP_Policy": [],
        "DLP_Source_Product": [],
        "Emergency_Notifications": [],
        "Encryption_Details": null,
        "Escalated_Incident_Status": [],
        "Estimated_Hours": 0,
        "Facility": [],
        "Filing_Name": null,
        "From_Date__Time": null,
        "Google_Map": "&lt;a target='_new' href='http://maps.google.com/maps?f=q&ie=UTF8&om=1<p>Fifth street </p>, Vienna, , 5000'>Google Map",
        "Impacted_Information_Assess": [],
        "Incident_Analysis_Q1": [],
        "Incident_Analysis_Q2": [],
        "Incident_Analysis_Q3": [],
        "Incident_Analysis_Q4": [],
        "Incident_Analysis_Q5": [],
        "Incident_Analysis_Q6": [],
        "Incident_Analysis_Q7": [],
        "Incident_Analysis_Q8": [],
        "Incident_Analysis_Score": 0,
        "Incident_Analysis_Severity": [
            "Low"
        ],
        "Incident_Details": "Closed!",
        "Incident_ID": 2,
        "Incident_Manager": [],
        "Incident_Owner": [],
        "Incident_Resolution_Detail": null,
        "Incident_Result": [
            "To Be Determined"
        ],
        "Incident_Status": [
            "Closed"
        ],
        "Incident_Summary": "TEST!!!!",
        "Incident_Trend": [],
        "Individuals_Involved": [],
        "Inherited_From_Third_Party_Profile": [],
        "Inherited_Permissions_Engagement_Stakeho": [],
        "Inherited_Permissions_Supplier_Request_F": [],
        "Inherited_RP": [],
        "Investigations": [],
        "Involved_Third_Parties": [],
        "Is_BSA_Bank_Secrecy_Act_reporting_requir": [
            "No"
        ],
        "Last_Updated": "2020-05-15T12:40:18.987+02:00",
        "Law_Enforcement_Agency": null,
        "Law_Enforcement_Agent": null,
        "Law_Enforcement_Case_No": null,
        "Legal_Involvement": [],
        "Legal_Involvement_Details": null,
        "Loss": 0,
        "Loss_Description": null,
        "Loss_Events": [],
        "Network_Policy_Enabled": [],
        "Notification_Execution": [],
        "Notify_Crisis_Team": [
            " No, do not send an email notification"
        ],
        "Notify_Incident_Owner": [
            "No, do not send an email notification to the incident owner"
        ],
        "Open_TasksActivities": [],
        "Organization_Affected_By_Incident": [],
        "Override_Rejected_Submission": [
            "No"
        ],
        "Policy_Enabled": [],
        "Priority": [
            "High"
        ],
        "Range_Type": [],
        "Recovery_": 0,
        "Recovery_Description": null,
        "Region": [],
        "Related_Incidents": [],
        "Related_Incidents1": [],
        "Reported_to_Police": [],
        "Responder_Hours_Entry": [],
        "Risks": [],
        "Source": [],
        "State": [],
        "Status_Change": [
            "No"
        ],
        "Status_Prior_Value": [],
        "Top_Offending_Users": [],
        "Total_Hours": 0,
        "Workflow_Assignees": [],
        "Workflow_Stage": [],
        "Zip_Code": "5000"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Error Messages:****If invalid key -** "Action wasn't able to create a new incident. Reason: {0} field was not found."format(invalid key)  
  
**If application not found -** "Action wasn't able to create a new incident. Reason: {0} application was not found."format(application)  
  
**If invalid value for type 4 and 9 -** "Action wasn't able to create a new incident. Reason: {0} field contains an invalid value."format(key)****  
**If user not found for type 8 -** "Action wasn't able to create a new incident. Reason: Username {0} was not found."f.ormat(user name) | General  
  
### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Update Incident

#### Description

Update an incident.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Application Name | String | Incidents | No | Specify an application name for the incident. Default: Incidents.  
Custom Mapping File | String | N/A | No | Specify an absolute path to the file that contains all of the required mapping. If "Remote File" is enabled, then provide a URL that contains the mapping file. Please refer to action documentation for the additional information.  
Content ID | String | N/A |  | Content ID of the incident to update.  
Incident Summary | String | N/A |  | The new summary of the incident.  
Incident Details | String | N/A |  | The new details (description) of the incident.  
Incident Owner | String | N/A |  | The new owner of the incident.  
Incident Status | String | N/A |  | The new status of the incident.  
Priority | String | N/A |  | The new priority of the incident.  
Category | String | N/A |  | The new category of the incident.  
Custom Fields | String | N/A | No | Specify a JSON object of fields that need to be updated. Example: {"Category": "Malware"}.  
Remote File | Checkbox | N/A |  | If enabled, action will treat value provided in "Custom Mapping File" as a URL and try to fetch a file from it.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
content_id | N/A | N/A  
  
##### Structure of the Mapping File

In order to work with a mapping file you need to use the proper format. Currently, mapping allows you to define cross-reference field entries.

The structure of the file is the following:
    
    
        {
        "type_9": {
            "{Cross-reference field name}": {
                "{Cross-reference field value}": "{content id of the cross-reference field value}",
                "{Cross-reference field value 2}": "{content id of the cross-reference field value 2}"
            }
        }
    }
    
    

Example. You have an incident application that you want to link to a certain facility application. In that case the mapping file will look like this:
    
    
    {
        "type_9": {
            "Facility": {
                "Business Department": "20202021",
                "Developers": "20011101"
            }
        }
    }
    
    

You need to use a mapping file, when actions are not able to automatically retrieve content id. In all of the other cases, this step is not needed.

##### JSON Result
    
    
    {
        "@odata.context": "http://172.30.202.238/RSAarcher/contentapi/Incidents(249459)/$metadata#Incidents/$entity",
        "Incidents_Id": 249459,
        "Additional_Access": [],
        "Additional_Notification_Recipients": [],
        "Address": "<p>Fifth street </p>",
        "Affected_Business_Unit": [],
        "Batch_File_Format": [],
        "Business_Continuity_Plans": [],
        "Business_Impact_Analysis_Archive": [],
        "Category": [
            "Harassment"
        ],
        "Cause": null,
        "City": "Vienna",
        "Corrective_Actions": null,
        "Country": [],
        "Current_Status": [],
        "Customer_Data": [],
        "Customer_Data_Details": null,
        "Data_Encrypted": [],
        "Date_Created": "2020-05-08T12:17:37.187+02:00",
        "DateTime_Closed": null,
        "DateTime_Occurred": "2020-05-06T05:00:00+02:00",
        "DateTime_Reported": "2020-05-08T12:15:00+02:00",
        "Days_Open": 6,
        "Default_Record_Permissions": [
            "IM: Admin",
            "IM: Read Only",
            "BCM: Admin"
        ],
        "Desktop_Policy_Enabled": [],
        "Discovery_Policy_Enabled": [],
        "DLP_Policy": [],
        "DLP_Source_Product": [],
        "Emergency_Notifications": [],
        "Encryption_Details": null,
        "Escalated_Incident_Status": [],
        "Estimated_Hours": 0,
        "Facility": [],
        "Filing_Name": null,
        "From_Date__Time": null,
        "Google_Map": "&lt;a target='_new' href='http://maps.google.com/maps?f=q&ie=UTF8&om=1<p>Fifth street </p>, Vienna, , 5000'>Google Map",
        "Impacted_Information_Assess": [],
        "Incident_Analysis_Q1": [],
        "Incident_Analysis_Q2": [],
        "Incident_Analysis_Q3": [],
        "Incident_Analysis_Q4": [],
        "Incident_Analysis_Q5": [],
        "Incident_Analysis_Q6": [],
        "Incident_Analysis_Q7": [],
        "Incident_Analysis_Q8": [],
        "Incident_Analysis_Score": 0,
        "Incident_Analysis_Severity": [
            "Low"
        ],
        "Incident_Details": "Closed!",
        "Incident_ID": 2,
        "Incident_Manager": [],
        "Incident_Owner": [],
        "Incident_Resolution_Detail": null,
        "Incident_Result": [
            "To Be Determined"
        ],
        "Incident_Status": [
            "Closed"
        ],
        "Incident_Summary": "TEST!!!!",
        "Incident_Trend": [],
        "Individuals_Involved": [],
        "Inherited_From_Third_Party_Profile": [],
        "Inherited_Permissions_Engagement_Stakeho": [],
        "Inherited_Permissions_Supplier_Request_F": [],
        "Inherited_RP": [],
        "Investigations": [],
        "Involved_Third_Parties": [],
        "Is_BSA_Bank_Secrecy_Act_reporting_requir": [
            "No"
        ],
        "Last_Updated": "2020-05-15T12:40:18.987+02:00",
        "Law_Enforcement_Agency": null,
        "Law_Enforcement_Agent": null,
        "Law_Enforcement_Case_No": null,
        "Legal_Involvement": [],
        "Legal_Involvement_Details": null,
        "Loss": 0,
        "Loss_Description": null,
        "Loss_Events": [],
        "Network_Policy_Enabled": [],
        "Notification_Execution": [],
        "Notify_Crisis_Team": [
            " No, do not send an email notification"
        ],
        "Notify_Incident_Owner": [
            "No, do not send an email notification to the incident owner"
        ],
        "Open_TasksActivities": [],
        "Organization_Affected_By_Incident": [],
        "Override_Rejected_Submission": [
            "No"
        ],
        "Policy_Enabled": [],
        "Priority": [
            "High"
        ],
        "Range_Type": [],
        "Recovery_": 0,
        "Recovery_Description": null,
        "Region": [],
        "Related_Incidents": [],
        "Related_Incidents1": [],
        "Reported_to_Police": [],
        "Responder_Hours_Entry": [],
        "Risks": [],
        "Source": [],
        "State": [],
        "Status_Change": [
            "No"
        ],
        "Status_Prior_Value": [],
        "Top_Offending_Users": [],
        "Total_Hours": 0,
        "Workflow_Assignees": [],
        "Workflow_Stage": [],
        "Zip_Code": "5000"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **Error Messages:****If invalid key -** "Action wasn't able to update the incident. Reason: {0} field was not found."format(invalid key)  
  
**If application not found -** "Action wasn't able to update the incident. Reason: {0} application was not found."format(application)****  
**If invalid value for type 4 and 9 -** "Action wasn't able to update the incident. Reason: {0} field contains an invalid value."format(key)****  
**If user not found for type 8 -** "Action wasn't able to update the incident. Reason: Username {0} was not found."f.ormat(user name) | General  
  
### Get Incident Details

#### Description

Retrieve information about the incident from RSA Archer.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Application Name | String | Incidents | No | Specify an application name for the incident. Default: Incidents.  
Content ID | Integer | N/A | Yes | Specify ID of the content for which you want to retrieve details.  
  
#### Use cases

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "@odata.context": "http://172.30.202.238/RSAarcher/contentapi/Incidents(249459)/$metadata#Incidents/$entity",
        "Incidents_Id": 249459,
        "Additional_Access": [],
        "Additional_Notification_Recipients": [],
        "Address": "<p>Fifth street </p>",
        "Affected_Business_Unit": [],
        "Batch_File_Format": [],
        "Business_Continuity_Plans": [],
        "Business_Impact_Analysis_Archive": [],
        "Category": [
            "Harassment"
        ],
        "Cause": null,
        "City": "Vienna",
        "Corrective_Actions": null,
        "Country": [],
        "Current_Status": [],
        "Customer_Data": [],
        "Customer_Data_Details": null,
        "Data_Encrypted": [],
        "Date_Created": "2020-05-08T12:17:37.187+02:00",
        "DateTime_Closed": null,
        "DateTime_Occurred": "2020-05-06T05:00:00+02:00",
        "DateTime_Reported": "2020-05-08T12:15:00+02:00",
        "Days_Open": 6,
        "Default_Record_Permissions": [
            "IM: Admin",
            "IM: Read Only",
            "BCM: Admin"
        ],
        "Desktop_Policy_Enabled": [],
        "Discovery_Policy_Enabled": [],
        "DLP_Policy": [],
        "DLP_Source_Product": [],
        "Emergency_Notifications": [],
        "Encryption_Details": null,
        "Escalated_Incident_Status": [],
        "Estimated_Hours": 0,
        "Facility": [],
        "Filing_Name": null,
        "From_Date__Time": null,
        "Google_Map": "&lt;a target='_new' href='http://maps.google.com/maps?f=q&ie=UTF8&om<p>Fifth street </p>, Vienna, , 5000'>Google Map",
        "Impacted_Information_Assess": [],
        "Incident_Analysis_Q1": [],
        "Incident_Analysis_Q2": [],
        "Incident_Analysis_Q3": [],
        "Incident_Analysis_Q4": [],
        "Incident_Analysis_Q5": [],
        "Incident_Analysis_Q6": [],
        "Incident_Analysis_Q7": [],
        "Incident_Analysis_Q8": [],
        "Incident_Analysis_Score": 0,
        "Incident_Analysis_Severity": [
            "Low"
        ],
        "Incident_Details": "Closed!",
        "Incident_ID": 2,
        "Incident_Manager": [],
        "Incident_Owner": [],
        "Incident_Resolution_Detail": null,
        "Incident_Result": [
            "To Be Determined"
        ],
        "Incident_Status": [
            "Closed"
        ],
        "Incident_Summary": "TEST!!!!",
        "Incident_Trend": [],
        "Individuals_Involved": [],
        "Inherited_From_Third_Party_Profile": [],
        "Inherited_Permissions_Engagement_Stakeho": [],
        "Inherited_Permissions_Supplier_Request_F": [],
        "Inherited_RP": [],
        "Investigations": [],
        "Involved_Third_Parties": [],
        "Is_BSA_Bank_Secrecy_Act_reporting_requir": [
            "No"
        ],
        "Last_Updated": "2020-05-15T12:40:18.987+02:00",
        "Law_Enforcement_Agency": null,
        "Law_Enforcement_Agent": null,
        "Law_Enforcement_Case_No": null,
        "Legal_Involvement": [],
        "Legal_Involvement_Details": null,
        "Loss": 0,
        "Loss_Description": null,
        "Loss_Events": [],
        "Network_Policy_Enabled": [],
        "Notification_Execution": [],
        "Notify_Crisis_Team": [
            " No, do not send an email notification"
        ],
        "Notify_Incident_Owner": [
            "No, do not send an email notification to the incident owner"
        ],
        "Open_TasksActivities": [],
        "Organization_Affected_By_Incident": [],
        "Override_Rejected_Submission": [
            "No"
        ],
        "Policy_Enabled": [],
        "Priority": [
            "High"
        ],
        "Range_Type": [],
        "Recovery_": 0,
        "Recovery_Description": null,
        "Region": [],
        "Related_Incidents": [],
        "Related_Incidents1": [],
        "Reported_to_Police": [],
        "Responder_Hours_Entry": [],
        "Risks": [],
        "Source": [],
        "State": [],
        "Status_Change": [
            "No"
        ],
        "Status_Prior_Value": [],
        "Top_Offending_Users": [],
        "Total_Hours": 0,
        "Workflow_Assignees": [],
        "Workflow_Stage": [],
        "Zip_Code": "5000"
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful(is_success = true):** print "Successfully returned information about the incident with ID {0} in RSA Archer.".format(content ID)  
******if status code 404 (is_success = false):** print "Action wasn't able to return information about the incident with ID {0} in RSA Archer. Reason: Incident with ID {0} was not found.".format(content id)****  
**The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** print "Error executing action "Get Incident Details". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Incident Journal Entry

#### Description

Add a journal entry to the Security Incident in RSA Archer.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Destination Content ID | String | N/A | True | Specify a content id of the security incident to which you want to add journal entry.  
Text | String | N/A | True | Specify the text for the journal entry.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "Links": [],
        "RequestedObject": {
            "Id": 267754
        },
        "IsSuccessful": true,
        "ValidationMessages": []
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if Successful == true (is_success = true):** "Successfully added new journal entry to the Security Incident {0} in RSA Archer.".format(content_id)******if Successful == false(is_success = false):** "Action wasn't able to add new journal entry to the Security Incident {0} in RSA Archer..format(content_id)******The action should fail and stop a playbook execution:****if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Add Incident Journal Entry". Reason: {0}''.format(error.Stacktrace)******If incident doesn't exist (404 status code):** "Error executing action "Add Incident Journal Entry". Reason: Security Incident {0} was not found''.format(content_id). | General  
  
## Connector

### RSA Archer - Security Incidents Connector

#### Description

Pull Security Incidents from RSA Archer.

### Configure RSA Archer - Security Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | http://x.x.x.x/RSAarcher | Yes | API Root of the RSA Archer instance.  
Instance Name | String | N/A | Yes | Name of the RSA Archer instance.  
Username | String | N/A | Yes | Username of the RSA Archer account.  
Password | Password | N/A | Yes | Password of the RSA Archer account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch security incidents.  
Max Security Incidents To Fetch | Integer | 50 | No | How many security incidents to process per one connector iteration.  
Process Security Alerts | Checkbox | Checked | No | If enabled, action will process Security Alerts related to the Security Incident.  
Process Incident Journal | Checkbox | Checked | No | If enabled, action will process Incident Journal related to the Security Incident.  
Time Format | String | %Y-%m-%d %H:%M:%S | Yes | Specify, what should be the time format for the searching of Security Incidents.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the RSA Archer server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

## Job

### Sync Security Incidents

#### Description

This job will synchronize security incidents in RSA Archer and Google SecOps.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | http://x.x.x.x/RSAarcher | Yes | API Root of the RSA Archer instance.  
Instance Name | String | N/A | Yes | Name of the RSA Archer instance.  
Username | String | N/A | Yes | Username of the RSA Archer account.  
Password | Password | N/A | Yes | Password of the RSA Archer account.  
Sync Fields | CSV | N/A | Yes | Specify a comma-separated list of fields that need to be synced  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the RSA Archer server is valid.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
