---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/arcsight/
title: Integrate ArcSight with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:42.715369+00:00
---

# Integrate ArcSight with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/arcsight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate ArcSight with Google SecOps 

This document describes how to integrate ArcSight with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Arcsight.zip).

## Before you begin

Before configuring the ArcSight ESM integration in Google SecOps, verify your environment meets the connection and permission requirements for your connectors, jobs, and actions.

To prepare your environment for integration, complete the following prerequisites:

  1. Verify the base integration requirements to establish network line-of-sight and programmatic authentication.

  2. To ingest security events or correlation cases into Google SecOps, configure connector-specific requirements.

  3. To grant granular privileges for case management and playbook automation, configure job and action-specific requirements.

  4. Review the configuration workflow to understand the provisioning sequence across ArcSight ESM and Google SecOps.




### Base integration requirements

The base integration establishes the core HTTPS connection and authentication session used across all Google SecOps actions, connectors, and jobs.

Configure the following foundational requirements in your environment:

  1. **Network line-of-sight** : Enable HTTPS communication from your Google SecOps instance or Remote Agent to the ArcSight ESM server on the management port (default: `8443/TCP`).

  2. **REST API access** : Verify direct access to the ArcSight ESM REST services located at `https://<esm-host>:8443/www/manager-service/rest/` and `https://<esm-host>:8443/www/core-service/rest/` as described in the [ArcSight ESM REST Web Services API Guide](https://www.microfocus.com/documentation/arcsight/).

  3. **SSL/TLS trust** : Provide a Base64-encoded PEM root and intermediate CA certificate file if your ArcSight ESM deployment uses a private or self-signed certificate authority.

  4. **Service account properties** : Create a dedicated ArcSight service account with user type `Web User` (recommended to avoid consuming an interactive Console seat license) or `Normal User`, and ensure `Login Enabled` is set to active.

For user administration procedures, refer to the "Managing Users" section of the [ArcSight ESM Administrator's Guide](https://www.microfocus.com/documentation/arcsight/).

  5. **Base group membership** : Assign the service user to a dedicated user group (for example, `SecOps_Integration_Group`) to manage all downstream operations privileges, resource ACLs, and event filters centrally.

For group configuration procedures, refer to the "Managing User Groups" section of the [ArcSight ESM Administrator's Guide](https://www.microfocus.com/documentation/arcsight/).




### Connector-specific requirements

Ingestion connectors pull alerts and security events into Google SecOps and require specialized data scoping and operational permissions beyond the base integration.

Configure the prerequisites corresponding to your chosen ingestion connector:

  1. **Event filter assignment** : Assign an event filter (such as `All Events` or a scoped organizational filter) to the integration user group to define the data scope of security events the connectors can retrieve.

For instructions on configuring group-level event filters, refer to the [ArcSight ESM Administrator's Guide](https://www.microfocus.com/documentation/arcsight/).

  2. **ArcSight - Security Events Connector** : Grant `Security Events: Inspect`, `Reports: Inspect`, and `Reports: Execute` operations privileges, and assign `Read` and `Execute` ACL permissions on the specific report resource in ArcSight that exports correlation events

For resource ACL procedures, refer to the "Managing Access Control on Resources" section of the [ArcSight ESM Console User's Guide](https://www.microfocus.com/documentation/arcsight/).

  3. **ArcSight ESM Connector** : Grant `Security Events: Inspect` and `Cases: Inspect` operations privileges, and assign `Read` ACL permissions on the target case folders and correlation resources in accordance with the [ArcSight ESM Console User's Guide](https://www.microfocus.com/documentation/arcsight/).




### Job and action-specific requirements

Scheduled jobs and playbook actions inherit the base integration connection and require granular operations privileges and object-level ACL permissions depending on the specific ArcSight resources they interact with.

Grant privileges and ACLs based on the integration capabilities you're deploying:

  1. **Action enablement** : Playbook actions don't require separate connection configuration in Google SecOps. Granting the required operations privileges and resource ACLs to the service account group in ArcSight immediately enables them for playbook use.

  2. **Close Cases job** : Grant `Cases: Inspect` and `Cases: Edit` operations privileges, and assign `Read` and `Modify` ACL permissions on the target case folders as outlined in the [ArcSight ESM Console User's Guide](https://www.microfocus.com/documentation/arcsight/).

  3. **Active list actions** : Grant `Active Lists: Inspect` and `Active Lists: Edit Content` (or `Active Lists: Edit`) operations privileges, and assign `Read` and `Write` ACL permissions on the specific active lists targeted by your playbook action parameters.

  4. **Case management actions** : Grant `Cases: Inspect` and `Cases: Edit` operations privileges, and assign `Read` and `Modify` ACL permissions on target case folders.

  5. **Query and search actions** : Grant `Query Viewers: Inspect` and `Query Viewers: Execute` operations privileges, and assign `Read` and `Execute` ACL permissions on target query viewers.

  6. **Report actions** : Grant `Reports: Inspect` and `Reports: Execute` operations privileges, and assign `Read` and `Execute` ACL permissions on target reports.




#### Component permission mapping

The following table outlines the minimum required operations privileges and resource ACLs for each integration component type.

Review the following table to understand the permission requirements:

  1. **Base session** : The base integration requires only valid login credentials and default authenticated user rights.

  2. **Ingestion connectors** : Connectors require event filtering rights, event inspection privileges, and read access to reports or cases.

  3. **Jobs and actions** : Playbook actions and sync jobs require functional task privileges and ACL permissions on the specific resources accessed, configured using the [ArcSight ESM Console User's Guide](https://www.microfocus.com/documentation/arcsight/).


Component Type | Component Name | API Service | Required Operations Privileges | Required Resource ACLs  
---|---|---|---|---  
**Base Integration** | Base Connection & Authentication | `LoginService` | Default authenticated user privileges | None  
**Connector** | ArcSight - Security Events Connector | `SecurityEventService`, `ReportService` | `Security Events: Inspect`, `Reports: Inspect`, `Reports: Execute` | `Read` and `Execute` on target report resource  
**Connector** | ArcSight ESM Connector | `SecurityEventService`, `CaseService` | `Security Events: Inspect`, `Cases: Inspect` | `Read` on target case folders and correlation objects  
**Job** | Close Cases Job | `CaseService` | `Cases: Inspect`, `Cases: Edit` | `Read` and `Modify` on target case folders  
**Action** | Active List Actions (Add Entities, Add Entries, Get Entries, Check Value) | `ActiveListService` | `Active Lists: Inspect`, `Active Lists: Edit Content` (or `Active Lists: Edit`) | `Read` and `Write` on target active lists  
**Action** | Change Case Stage Action | `CaseService` | `Cases: Inspect`, `Cases: Edit` | `Read` and `Modify` on target case folders  
**Action** | Query & Search Actions (Get Query Results, Search) | `QueryViewerService`, `SearchService` | `Query Viewers: Inspect`, `Query Viewers: Execute` | `Read` and `Execute` on target query viewers  
**Action** | Get Report Action | `ReportService` | `Reports: Inspect`, `Reports: Execute` | `Read` and `Execute` on target reports  
**Action** | List Resources Action | `ActiveListService`, `CaseService`, `QueryViewerService`, `ReportService` | `Inspect` privilege for each enabled resource type | `Read` on target resource folders  
  
### Configuration workflow

Follow this multi-phase workflow to provision permissions in ArcSight ESM and activate your selected components in Google SecOps.

Complete the configuration steps in the following sequence:

  1. **ArcSight service account and group provisioning** : Create the dedicated service user in ArcSight ESM, create a dedicated user group, assign the service user to the group, and apply an event filter to define data visibility as detailed in the [ArcSight ESM Administrator's Guide](https://www.microfocus.com/documentation/arcsight/).

  2. **Assign privileges and ACLs for chosen components** : Cross-reference your planned connectors, jobs, and actions against the component permission mapping table, grant the corresponding operations privileges to the user group, and assign object-level ACLs (such as `Read/Write` on active lists or `Read/Execute` on reports) on the specific target resource folders in the [ArcSight ESM Console User's Guide](https://www.microfocus.com/documentation/arcsight/).

  3. **Configure in Google SecOps** : Configure the base integration, ingestion connectors, scheduled jobs, and playbook actions in Google SecOps as described in the following sections.




## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the instance you intend to configure the integration for.  
Description | String | N/A | No | Description of the instance.  
API Root | String | `https://{IP}:{PORT}` | Yes | Server address of the ArcSight instance.  
Username | String | N/A | Yes | Username of the ArcSight account.  
Password | Password | N/A | Yes | Password of the ArcSight account.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Entries to Active List

Provides a mechanism to get information from trends outside of, and in addition to, reports. Active lists updated by trends support summary views of information from multiple trends.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Columns | String | N/A | Yes | Example: Message;Username  
Entries | String | N/A | Yes | Example: test1|Me1;Test|Me2  
Active List UUID | String | N/A | Yes | Example: HCN75QGABABCZXCOdT9P51w==  
  
#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
is_succeed | True or False | is_succeed:False  
  
### Change Case Stage

Change a case's stage. Valid stages are INITIAL, QUEUED, CLOSED, FINAL, and FOLLOW_UP.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Case Name | String | N/A | Yes | The name of the case to update.  
Stage | String | N/A | Yes | The stage of the case. Example: CLOSED, INITIAL  
  
#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
### Get Activelist Entries

Retrieve ArcSight active list entries and return csv output.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Active list UUID | String | N/A | Yes | Example: HTcILQWABABCr553ieI0Xmw==  
  
#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
Success_Indicator | N/A | N/A  
  
##### JSON result
    
    
    [
    "12346e4d96f0a72c42015d69aaf0e8ab ,
     file.txt",
     "0e0776034e5e096704cd28cbd40cdbb5 ,
     Test.config"
    ]
    

### Get Query Results

Get query results by query ID. A query can be used as the primary data source for a report, or a trend (based on one query) that can be used as the data source to another query that further refines the initial query result.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Query ID | String | N/A | Yes | The query ID.  
Max Items To Return | Integer | 100 | No | Specify how many items to return in the response.  
  
#### Use Cases

Add limitation for how many results to return.

#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
    [
        {
            "Target User Name": "user",
            "Attacker Address": "192.0.2.1",
            "External ID": "127",
            "Name": "A Kerberos authentication ticket (TGT) was requested.",
            "Target Address": "192.0.2.1"
        },{
            "Target User Name": "user",
            "Attacker Address": "192.0.2.1",
            "External ID": "127",
            "Name": "A Kerberos authentication ticket (TGT) was requested.",
            "Target Address": "192.0.2.1"
        }
    ]
    

### Get Report

Get a report with dynamic fields. A report is an ArcSight resource that binds data from a query or trend to an existing report template. Once ran, the results of a report can be viewed in the ArcSight consoles viewer panel, saved (archived), or exported in a variety of formats. Reports can be scheduled to run at regular intervals and can be ran on-demand as needed.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Report Full Path (URI) | String | N/A | Yes | The relevant report uri.  
Field 2 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 3 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 4 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 6 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 6 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 7 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 8 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 9 | String | N/A | No | The dynamic fields for the query to generate the report.  
Field 10 | String | N/A | No | The dynamic fields for the query to generate the report.  
  
#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
json_report | N/A | N/A  
  
### Is Value in Activelist Column

Check if specific value is in active list .

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Active list UUID | String | N/A | Yes | Active list uuid. Example: cuser.  
Column name | String | N/A | Yes | The name of the column. Example: sourceUserName.  
  
#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
Success_Indicator | N/A | N/A  
  
### Ping

Test Connectivity.

#### Parameters

None.

#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
is_succeed | True or False | is_succeed:False  
  
### Search

You can start a search at the ArcSight Command Center from the console event channel. Event Complete Search looks for the associated attribute, which is stored in several fields (for example, abc). The search for events searches for a value (for example, abc) stored in the field specified (for example, in the field of name only).

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Search Query | String | N/A | Yes | The search query.  
Max Items To Return | Integer | 100 | No | Specify how many items to return in the response.  
  
#### Use Cases

Add limitation for how many results to return.

#### Run on

This action runs on all entities.

#### Action results

This action can provide the following results.

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
    [
        {
            "score": 1.2440307,
            "uuid": "UUID",
            "uri": "/All_Fields/ArcSight_Foundation/Variables_Library/IPv6/Attacker_IPv6_Address",
            "name": "Attacker IPv6 Address"
        }, {
            "score": 1.2440307,
            "uuid": "UUID",
            "uri": "/All_Fields/ArcSight_Foundation/Variables_Library/IPv6/Attacker_IPv6_Address",
            "name": "Attacker IPv6 Address"
        }
    ]
    

## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Arcsight ESM Connector

This guide refers to ArcSight ESM versions 6.9.1 and higher.

#### ESM rule or case forwarding to Google SecOps

**Working with Triggered Rules/Correlations**

You will be required to configure ArcSight ESM to forward the latest correlation objects to Google SecOps while you configure Google SecOps to function on ArcSight ESM as a SIEM provider, and also to provide API access to ArcSight ESM through an authorized user.

This feature allows Google SecOps to retrieve any triggered rules within ArcSight ESM in near real-time and forward them to be translated and contextualized as alerts for cases.

**Data Flow between Google SecOps and ArcSight ESM**

Google SecOps automatically indexes and contextualizes correlations that were forwarded to Google SecOps and were triggered in ArcSight ESM through ArcSight Forwarding Connector module and API access.

#### Connector severity prioritization

The connector assigns severity with the following prioritization values:

  * 1 and 2 - very low
  * 3 and 4 - low
  * 5 and 6 - medium
  * 7 and 8 - high
  * 9 and 10 - critical



#### Connector inputs

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Environment | DDL | N/A | Yes | Select the required environment, for example, **Customer One**. In case that the alert's Environment field is empty, this alert will be injected to this environment.  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection.  
Product Field Name | String | device_product | No | The name of the field where the product name is stored.The default value is `device_product`.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `device_product` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.  
Event Field Name | String | name | No | The field name used to determine the event name (sub-type).  
Script Timeout (seconds) | String | 500 | No | The timeout limit (in seconds) for the python process running the current script.  
Server Address | String | N/A | Yes | `https://{IP}:{PORT}`  
Username | String | N/A | Yes | Username of the ArcSight account.  
Password | Password | N/A | Yes | The password of the ArcSight account.  
Events Count Limit | Integer | 15 | Yes | Enter the maximum number of events to fetch per correlation. Limit the number of events, for example, 10.  
Cases Folder Path | String | `I:\SiemShare\CorrelationSource` | Yes | The location of the case files, such as `I:\SiemShare\CorrelationSource` **Note:** The Cases Folder Path parameter can be changed from one customer to another. Full path. Example: `C:\Desktop\CorrelationSource`  
Alerts Count Limit | Integer | 10 | Yes | The maximum number of alerts to process per connector cycle, for example, 10.  
Environment Field Name | String | event.customerURI | Yes | The name of the field to get the case's environment, for example, event.customerUri.  
Secondary Device Product Field | String | N/A | No | Replace the original product field (from the connector's DeviceProductField with the value from the secondary product field). Example: CustomDeviceString2  
Alert Custom Fields Names | String | N/A | No | Pull custom field values from ArcSight into the alert, such as baseEventCount,agent_address,device_assetId.  
Done files retention days | Integer | 3 | Yes | How many days, to keep each DONE csv file.  
Error files retention days | Integer | 14 | Yes | How many days, to keep each ERROR csv file.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

### ArcSight - Security Events Connector

Pull correlations from ArcSight. This connector is suitable for SaaS deployment of Google SecOps and is the recommended one for production use.

**Note:** Dynamic list works with the _name_ parameter.

This connector requires completing the prerequisite steps.

#### Connector inputs

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | type | Yes | The name of the field where the product name is stored. The default value is `type`.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `type` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.  
Event Field Name | String | name | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | FALSE | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 360 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
API Root | String | `https://{ip}` | Yes | The API root of the ArcSight instance.  
Username | String | N/A | Yes | Username of the ArcSight account.  
Password | Password | N/A | Yes | Password of the ArcSight account.  
Report Name | String | N/A | Yes | Name of the report that will be used to fetch events.  
Fetch Base Events | Checkbox | Checked | Yes | If enabled, connector will also fetch base events.  
Lowest Priority To Fetch | Integer | N/A | No | Lowest priority that will be used to fetch events. Possible values are in range 1 to 10. If nothing is provided, all events will be ingested.  
Max Events To Fetch | Integer | 100 | No | The number of alerts to process per connector iteration. The maximum allowed is 1000.  
Use dynamic list as a blocklist | Checkbox | Checked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If selected, the integration validates the SSL certificate when connecting to the ArcSight server.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Close Cases

The job requires the following parameters:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Server Address | String | 192.0.2.1 | Yes | N/A  
Username | String | N/A | Yes | N/A  
Password | Password | N/A | Yes | N/A  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
