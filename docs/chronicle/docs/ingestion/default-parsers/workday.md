---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday/
title: Collect Workday HCM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:54.398154+00:00
---

# Collect Workday HCM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Workday HCM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Workday HCM logs to Google Security Operations by setting up a feed using the Third Party API.

The parser extracts Workday HCM user data from JSON-formatted logs. It handles various data transformations, including renaming fields, merging nested objects, parsing dates, and populating UDM fields for user attributes, employment details, and organizational structure.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `WORKDAY` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to Workday with **Security Administrator** or equivalent permissions.

**Caution:** You must enable allowlisting and add the IP ranges for all log types that ingest data from third-party APIs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).

## Configure Workday API authentication

### Create an Integration System User (ISU)

  1. Sign in to Workday with administrative privileges.
  2. In the search bar, type **Create Integration System User** and select the task.
  3. Enter a **Username** (for example, `ISU_SecOps_HCM`).
  4. Set a **Password**.
  5. Set **Session Timeout Minutes** to `0` to prevent the ISU from timing out.
  6. Enable **Do Not Allow UI Sessions** to enhance security by restricting UI logins.
  7. Go to the **Maintain Password Rules** task.
  8. Add the integration system user to the **System Users exempt from password expiration** field.



### Create an integration security group

  1. In the search bar, type **Create Security Group** and select the task.
  2. Locate the **Type of Tenanted Security Group** field, and select **Integration System Security Group (Unconstrained)**.
  3. Provide a **Name** for the security group (for example, `ISG_SecOps_HCM`).
  4. Click **OK**.
  5. Click **Edit** for the newly created security group.
  6. Assign the Integration System User from the previous step to the security group.
  7. Click **Done**.



### Grant domain access to the security group

The Google SecOps feed retrieves data from four Workday REST API endpoints. Each endpoint requires specific Domain Security Policy permissions to be granted to the integration security group.

  1. In the search bar, type **Maintain Permissions for Security Group** and select the task.
  2. Choose the security group you created (for example, `ISG_SecOps_HCM`) from the **Source Security Group** list.
  3. Click **OK**.
  4. Go to **Domain Security Policy Permissions**.
  5. Add **GET** access for each of the following domains:

API Endpoint | Required Domain Security Policies  
---|---  
`/workers` — Worker list, profiles, and current staffing | `Worker Data: Public Worker Reports`, `Worker Data: Current Staffing Information`, `Person Data: Work Contact Information`  
`/workers/{id}/timeOffEntries` — Time off balances | `Worker Data: Time Off (Time Off Balances)`, `Worker Data: Time Off (Time Off Balances Manager View)`  
`/workers/{id}/history` — Worker staffing history | `Worker Data: Current Staffing Information`  
`/supervisoryOrganizations` — Org structure | `Worker Data: Organization Information`  
**Note:** All domains listed above must be granted for the feed to function without errors. Missing permissions for any endpoint will result in `403 Forbidden` responses for that data type, which may cause the feed to report failures.
  6. Click **OK**.

  7. Click **Done** to save changes.




### Activate security policy changes

  1. In the search bar, type **Activate Pending Security Policy Changes** and select the task.
  2. Enter a reason for the change in the comment field (for example, `Granting API access for Google SecOps HCM integration`).
  3. Click **OK**.
  4. Select **Confirm** , then click **OK**.



### Register API client for integrations

  1. In the search bar, type **Register API Client for Integrations** and select it.
  2. Click **Create**.
  3. Provide the following configuration details:

     * **Client Name** : Enter a name (for example, `Google SecOps HCM Client`).
     * **System User** : Select the Integration System User you created (for example, `ISU_SecOps_HCM`).
     * **Scope** : Select the following scopes:

Scope | Required for  
---|---  
**Staffing** | `/workers` and `/workers/{id}/history` endpoints  
**Contact Information** | Work email and phone fields returned by `/workers` (used for UDM correlation)  
**Time Off and Leave** | `/workers/{id}/timeOffEntries` endpoint  
**Organizations and Roles** | `/supervisoryOrganizations` endpoint  
**Tenant Non-Configurable** | Any OAuth 2.0 API client (system-level integration and token rotation)  
**Important:** Selecting only the **Staffing** scope is not sufficient. You must add all of the scopes listed above. Each scope maps to a different set of Workday REST API resources. If you also ingest Workday User Activity or audit logs, add the **System** scope as well.
  4. Click **Save**.

  5. Click **OK**.

  6. Copy and save the **Client ID** and **Client Secret** immediately.

**Important:** The Client Secret is displayed only once. If you lose it, you must regenerate a new one.



### Generate OAuth 2.0 refresh token

  1. In the search bar, type **Manage Refresh Tokens for Integrations** and select it.
  2. Click **Generate New Refresh Token**.
  3. In the **Workday Account** field, search for and select the Integration System User (for example, `ISU_SecOps_HCM`).
  4. Select the API client you created and click **OK**.
  5. Copy and save the **Refresh Token**.



### Get API endpoint URLs

  1. In the search bar, type **View API Clients** and select it.
  2. Under **API Clients for Integrations** , locate the client you created (for example, `Google SecOps HCM Client`).
  3. Copy and save the following details:

     * **Token Endpoint** : The URL to obtain an access token (for example, `https://wd2-impl-services1.workday.com/ccx/oauth2/YOUR_TENANT/token`).
     * **Workday REST API Endpoint** : The base URL for API calls (for example, `https://wd2-impl-services1.workday.com/ccx/api/v1/YOUR_TENANT`).
**Note:** The hostname varies by Workday environment (for example, `wd2-impl-services1.workday.com`, `wd3-services1.workday.com`, `wd5-services1.workday.com`). Use the exact URLs provided by Workday.



### Generate OAuth access token

Use `curl` or a similar HTTP client to send a POST request to the Token Endpoint:
    
    
    curl -X POST "https://HOSTNAME/ccx/oauth2/TENANT/token" \
        -d "grant_type=refresh_token" \
        -d "client_id=YOUR_CLIENT_ID" \
        -d "client_secret=YOUR_CLIENT_SECRET" \
        -d "refresh_token=YOUR_REFRESH_TOKEN"
    

This returns an access token (for example, `"access_token": "abcd1234"`). Copy and save the access token.

### Verify API access

Before configuring the feed, verify that the ISU has the required permissions for the key endpoints. Replace the variables with your actual values:
    
    
    TOKEN="your-access-token"
    HOST="your-workday-host"
    TENANT="your-tenant"
    
    # Test 1: Workers (should return worker list)
    curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $TOKEN" \
        "https://$HOST/ccx/api/v1/$TENANT/workers?limit=1"
    
    # Test 2: Time off entries (replace WORKER_ID with an ID from Test 1)
    curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $TOKEN" \
        "https://$HOST/ccx/api/v1/$TENANT/workers/WORKER_ID/timeOffEntries"
    
    # Test 3: Worker history (replace WORKER_ID with an ID from Test 1)
    curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $TOKEN" \
        "https://$HOST/ccx/api/v1/$TENANT/workers/WORKER_ID/history"
    
    # Test 4: Supervisory organizations
    curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $TOKEN" \
        "https://$HOST/ccx/api/v1/$TENANT/supervisoryOrganizations"
    

Each test should return HTTP status `200`. If any endpoint returns `403`, see the Troubleshooting section below.

## Configure a feed in Google SecOps to ingest Workday HCM data

### Set up the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Workday HCM`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Workday** as the **Log type**.
  7. Click **Next**.



### Configure feed parameters

Specify values for the following input parameters:

  * **API Hostname** : The fully qualified domain name of your Workday REST API endpoint (for example, `wd2-impl-services1.workday.com`).

**Note:** Do not include the `https://` prefix or the API path. Enter only the hostname.
  * **Tenant** : The last path element of your Workday REST API endpoint that identifies your Workday instance.

  * **Access token** : The OAuth access token generated in the previous section.




**Advanced Options:**

  * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
  * **Ingestion labels** : The label to be applied to the events from this feed.


  1. Click **Next**.
  2. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Troubleshooting

### 403 Forbidden on specific endpoints

If the feed reports errors or the verification curl commands return `403` for specific endpoints, the Integration System User is missing permissions.

Failing endpoint | Fix  
---|---  
`/workers/{id}/timeOffEntries` | Add **GET** access for `Worker Data: Time Off (Time Off Balances)` and `Worker Data: Time Off (Time Off Balances Manager View)` domains. Add **Time Off and Leave** scope to the API client.  
`/workers/{id}/history` | Add **GET** access for `Worker Data: Historical Staffing Information` domain. Verify the **Staffing** scope is assigned to the API client.  
`/supervisoryOrganizations` | Add **GET** access for `Manage: Supervisory Organization` or `View: Supervisory Organization` domain. Add **Organizations and Roles** scope to the API client.  
  
After making permission changes:

  1. Run **Activate Pending Security Policy Changes** in Workday.
  2. If you added new scopes to the API client, generate a new refresh token via **Manage Refresh Tokens for Integrations** and then generate a new access token.
  3. Update the feed configuration with the new access token if changed.



### Authentication errors

  * **401 Unauthorized** : The access token has expired. Generate a new token using the refresh token and update the feed.
  * **Invalid client** : Verify the Client ID and Client Secret are correct.
  * **Invalid refresh token** : The refresh token may have been revoked. Generate a new one via **Manage Refresh Tokens for Integrations**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`entity_host_name` | `entity.asset.hostname` | Directly mapped  
`location.descriptor` | `entity.location.city` | Directly mapped  
`AU_EFFECTIVE_DATE` | `entity.resource.attribute.labels.value` | Directly mapped  
`COMPANY_EFFECTIVE_DATE` | `entity.resource.attribute.labels.value` | Directly mapped  
`ORIG_HIRE_DT` | `entity.resource.attribute.labels.value` | Directly mapped  
`STATUS_EFFECTIVE_DATE` | `entity.resource.attribute.labels.value` | Directly mapped  
`href` | `entity.url` | Directly mapped  
`CONT_START_DTE` | `entity.user.attribute.labels.value` | Directly mapped  
`EMPL_TYPE` | `entity.user.attribute.labels.value` | Directly mapped  
`EXEC_CD` | `entity.user.attribute.labels.value` | Directly mapped  
`EXEC_DESCR` | `entity.user.attribute.labels.value` | Directly mapped  
`HR_Status` | `entity.user.attribute.labels.value` | Directly mapped  
`Is_Active` | `entity.user.attribute.labels.value` | Directly mapped  
`Is_Manager` | `entity.user.attribute.labels.value` | Directly mapped  
`JOB_CODE` | `entity.user.attribute.labels.value` | Directly mapped  
`ORG_CD` | `entity.user.attribute.labels.value` | Directly mapped  
`ORG_Container` | `entity.user.attribute.labels.value` | Directly mapped  
`ORG_Container_Name` | `entity.user.attribute.labels.value` | Directly mapped  
`PER_Status` | `entity.user.attribute.labels.value` | Directly mapped  
`POSITION_NBR` | `entity.user.attribute.labels.value` | Directly mapped  
`PS_ELID` | `entity.user.attribute.labels.value` | Directly mapped  
`REG_TEMP` | `entity.user.attribute.labels.value` | Directly mapped  
`WB_LOGON_ID` | `entity.user.attribute.labels.value` | Directly mapped  
`ORG_DESCR` | `entity.user.department` | Merged  
`primarySupervisoryOrganization.descriptor` | `entity.user.department` | Merged  
`Email` | `entity.user.email_addresses` | Merged  
`Work_Email` | `entity.user.email_addresses` | Merged  
`primaryWorkEmail` | `entity.user.email_addresses` | Merged  
`EMPLID` | `entity.user.employee_id` | Directly mapped  
`Employee_ID` | `entity.user.employee_id` | Directly mapped  
`First_Name` | `entity.user.first_name` | Directly mapped  
`Legal_Name_First_Name` | `entity.user.first_name` | Directly mapped  
`HIRE_DATE` | `entity.user.hire_date` | Parsed as `RFC 3339`  
`Hire_Date` | `entity.user.hire_date` | Parsed as `RFC 3339`  
`Last_Name` | `entity.user.last_name` | Directly mapped  
`Legal_Name_Last_Name` | `entity.user.last_name` | Directly mapped  
`gopher-supervisor.primaryWorkEmail` | `entity.user.managers.email_addresses` | Merged  
`Reports_To_EMPLID` | `entity.user.managers.employee_id` | Directly mapped  
`gopher-supervisor.id` | `entity.user.managers.product_object_id` | Renamed/mapped  
`Reports_To_Name` | `entity.user.managers.user_display_name` | Directly mapped  
`gopher-supervisor.descriptor` | `entity.user.managers.user_display_name` | Renamed/mapped  
`primaryWorkPhone` | `entity.user.phone_numbers` | Merged  
`Termination_Date` | `entity.user.termination_date` | Parsed as `RFC 3339`  
`timeoff.descriptor` | `entity.user.time_off.description` | Directly mapped  
`timeoff.date` | `entity.user.time_off.interval.start_time` | Parsed as `RFC 3339`  
`HR_JOB_TITLE` | `entity.user.title` | Directly mapped  
`Job_Profile` | `entity.user.title` | Directly mapped  
`businessTitle` | `entity.user.title` | Directly mapped  
`Full_Name` | `entity.user.user_display_name` | Directly mapped  
`descriptor` | `entity.user.user_display_name` | Directly mapped  
`udm_metadata` | `metadata` | Renamed/mapped  
`metadata_entity_type` | `metadata.entity_type` | Directly mapped  
`actual_completed_date_and_time` | `metadata.event_timestamp` | Parsed as `MM/dd/yyyy HH:mm:ss a`  
`body.time` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`requestTime` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`EMPLID` | `metadata.product_entity_id` | Directly mapped  
`Employee_ID` | `metadata.product_entity_id` | Directly mapped  
`id` | `metadata.product_entity_id` | Directly mapped  
`Source_Name` | `metadata.product_name` | Directly mapped  
`userAgent` | `network.http.parsed_user_agent` | Renamed/mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`sessionId` | `network.session_id` | Directly mapped  
`ipAddress` | `principal.ip` | Merged  
`taskId` | `principal.process.pid` | Directly mapped  
`activityAction_label` | `principal.resource.attribute.labels` | Merged  
`body.event.Submitted_By` | `principal.user.userid` | Directly mapped  
`body.event.Response_Message` | `security_result.action_details` | Directly mapped  
`body.event.Messages` | `security_result.description` | Directly mapped  
`actual_start_date_and_time_label` | `security_result.detection_fields` | Merged  
`background_process_is_running_label` | `security_result.detection_fields` | Merged  
`by_person_label` | `security_result.detection_fields` | Merged  
`created_from_trigger_label` | `security_result.detection_fields` | Merged  
`items_processed_label` | `security_result.detection_fields` | Merged  
`percent_complete_label` | `security_result.detection_fields` | Merged  
`processing_time_label` | `security_result.detection_fields` | Merged  
`scheduled_start_date_and_time_label` | `security_result.detection_fields` | Merged  
`sent_on_label` | `security_result.detection_fields` | Merged  
`total_duration_label` | `security_result.detection_fields` | Merged  
`body.event.Integration_Event_Status` | `security_result.summary` | Directly mapped  
`body.event.Integration_System` | `target.application` | Directly mapped  
`target_data.id` | `target.resource.product_object_id` | Directly mapped  
`deviceType` | `target.resource.resource_subtype` | Directly mapped  
`deviceType` | `target.resource.type` | Mapped: `(?i)(Desktop/Laptop/Mobile)` → `DEVICE`  
`user_display_name` | `target.user.user_display_name` | Directly mapped  
`systemAccount` | `target.user.userid` | Directly mapped  
N/A | `entity.resource.attribute.labels.key` | Constant: `COMPANY_EFFECTIVE_DATE`  
N/A | `entity.user.attribute.labels.key` | Constant: `ORG_Container`  
N/A | `metadata.product_name` | Constant: `HCM`  
N/A | `metadata.vendor_name` | Constant: `Workday`  
N/A | `target.resource.type` | Constant: `DEVICE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
