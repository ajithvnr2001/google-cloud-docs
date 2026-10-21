---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-zpa-audit/
title: Collect Zscaler ZPA Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:39:31.744224+00:00
---

# Collect Zscaler ZPA Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-zpa-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler ZPA Audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export Zscaler ZPA Audit logs by setting up Bindplane agent and how log fields map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Zscaler ZPA Audit and the Bindplane agent configured to send logs to Google Security Operations. Each customer deployment can differ and might be more complex.

The deployment contains the following components:

  * **Zscaler ZPA Audit** : The platform from which you collect logs.

  * **Bindplane agent** : The Bindplane agent fetches logs from Zscaler ZPA Audit and sends logs to Google Security Operations.

  * **Google SecOps** : Retains and analyzes the logs.




An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `ZSCALER_ZPA_AUDIT` label.

## Before you begin

  * Ensure that you are using Zscaler ZPA Audit 2024 or later.
  * Ensure that you have access to Zscaler Private Access console. For more information, see [Secure Private Access (ZPA) Help](https://help.zscaler.com/zpa/getting-started).
  * Ensure that all systems in the deployment architecture are configured with the UTC time zone.



## Configure Log Receiver in Zscaler Private Access

Use the following steps to configure and manage Log Receiver in Zscaler Private Access:

### Add a log receiver

  1. Select **Configuration & Control** > **Private Infrastructure** > **Log Streaming Service** > **Log Receivers** and then click **Add Log Receiver**.
  2. In the **Log Receiver** tab, do the following: 
     1. In the **Name** field, enter the name for the log receiver.
     2. In the **Description** field, enter a description.
     3. In the **Domain or IP Address** field, enter the fully qualified domain name (FQDN) or IP address for the log receiver.
     4. In the **TCP Port** field, enter the TCP port number used by the log receiver.
     5. Select the encryption type in **TLS Encryption** to enable or disable the encryption of the traffic between the App Connector and the log receiver. By default, this setting is disabled.
     6. In the **App Connector groups** list, choose the App Connector groups that can forward logs to the receiver and click **Done**.
     7. Click **Next**.
  3. In the **Log Stream** tab, do the following:

     1. Select a **Log Type** from the menu.
     2. Select a **Log Template** from the menu.
     3. Copy-paste the **Log Stream Content** and add new fields. Ensure the key names match the actual field names.

The following is the default **Log Stream Content** for the Audit log type: 
            
            {"ModifiedTime":%j{modifiedTime:iso8601},"CreationTime":%j{creationTime:iso8601},"ModifiedBy":%d{modifiedBy},"RequestID":%j{requestId},"SessionID":%j{sessionId},"AuditOldValue":%j{auditOldValue},"AuditNewValue":%j{auditNewValue},"AuditOperationType":%j{auditOperationType},"ObjectType":%j{objectType},"ObjectName":%j{objectName},"ObjectID":%d{objectId},"CustomerID":%d{customerId},"User":%j{modifiedByUser},"ClientAuditUpdate":%d{clientAuditUpdate}}\n
            

     4. In the **SAML Attributes** , click **Select IdP** and select the IdP configuration you want to include in the policy.

     5. In the **Application Segments** menu, select the application segments you want to include and click **Done**.

     6. In the **Segment Groups** menu, select the segment groups you want to include and click **Done**.

     7. In the **Client Types** menu, select the client types you want to include and click **Done**.

     8. In the **Session Statuses** menu, select the session status codes you want to exclude and click **Done**.

     9. Click **Next**.

  4. In the **Review** tab, review your log receiver configuration and click **Save**.




**Note:** The `ZSCALER_ZPA_AUDIT` Gold parser only supports JSON log format, therefore make sure to select **JSON** as **Log Template** from the menu while configuring log stream.

### Copy a log Receiver

  1. Select **Control > Private Infrastructure > Log Streaming Service > Log Receivers**.
  2. In the table, locate the log receiver you want to modify and click **Copy**.
  3. In the **Add Log Receiver** window, modify fields as necessary. To learn more about each field, see the procedure in the **Add Log Receiver** section.
  4. Click **Save**.



### Edit a log Receiver

  1. Select **Control > Private Infrastructure > Log Streaming Service > Log Receivers**.
  2. In the table, locate the log receiver you want to modify and click **Edit**.
  3. In the **Edit Log Receiver** window, modify fields as necessary. To learn more about each field, see the procedure in the **Add Log Receiver** section.
  4. Click **Save**.



### Delete a log Receiver

  1. Select **Control > Private Infrastructure > Log Streaming Service > Log Receivers**.
  2. In the table, locate the log receiver you want to modify and click **Delete**.
  3. In the **Confirmation** window, click **Delete**.



## Forward Logs to Google SecOps using Bindplane agent

  1. Install and set up a **Linux Virtual Machine**.
  2. Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see [the Bindplane agent installation and configuration instructions](https://bindplane.com/docs/getting-started/quickstart-guide).



If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zscaler ZPA Audit log formats

The Zscaler ZPA Audit parser supports logs in JSON format.

## Supported Zscaler ZPA Audit sample logs

  * JSON:
        
        {
          "ModifiedTime": "",
          "CreationTime": "2024-06-29T05:06:34.000Z",
          "ModifiedBy": 216193796315021769,
          "RequestID": "ed500dfb-c66d-4ec2-b97e-ec2018c811f4",
          "SessionID": "v2t27ixe6qs21cffpzy6jx1zv",
          "AuditOldValue": "",
          "AuditNewValue": "{\\"loginAttempt\\":\\"2024-06-29 05: 06: 34 UTC\\",\\"remoteIP\\":\\"198.51.100.0\\"}",
          "AuditOperationType": "Sign In",
          "ObjectType": "Authentication",
          "ObjectName": "",
          "ObjectID": 0,
          "CustomerID": dummy_customer_id,
          "User": "abc.xyz.com",
          "ClientAuditUpdate": 0
        }
        




## UDM Mapping Table

### Field mapping reference: ZSCALER_ZPA_AUDIT 

The following table lists the log fields of the `ZSCALER_ZPA_AUDIT` log type and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `Zscaler Private Access`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Zscaler`.  
`CreationTime` | `metadata.event_timestamp` |   
`RequestID` | `metadata.product_log_id` |   
`SessionID` | `network.session_id` |   
`` | `metadata.event_type` | If the `AuditOperationType` log field value is _not_ empty, then if the `AuditOperationType` log field value is equal to `Create`, then the `metadata.event_type` UDM field is set to `RESOURCE_CREATION`.  
  
Else, if the `AuditOperationType` log field value is equal to `Client Session Revoked`, then the `metadata.event_type` UDM field is set to `USER_LOGOUT`.  
  
Else, if the `AuditOperationType` log field value is equal to `Delete`, then the `metadata.event_type` UDM field is set to `RESOURCE_DELETION`.  
  
Else, if the `AuditOperationType` log field value is equal to `Download`, then the `metadata.event_type` UDM field is set to `USER_RESOURCE_ACCESS`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In`, then the `metadata.event_type` UDM field is set to `USER_LOGIN`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In Failure`, then the `metadata.event_type` UDM field is set to `USER_LOGIN`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign Out`, then the `metadata.event_type` UDM field is set to `USER_LOGOUT`.   
  
Else, if the `AuditOperationType` log field value is equal to `Session Time Out`, then the `metadata.event_type` UDM field is set to `USER_LOGOUT`.  
  
Else, if the `AuditOperationType` log field value is equal to `Update`, then the `metadata.event_type` UDM field is set to `USER_RESOURCE_UPDATE_CONTENT`.  
`` | `metadata.product_event_type` | If the `AuditOperationType` log field value is _not_ empty, then if the `AuditOperationType` log field value is equal to `Create`, then the `metadata.product_event_type` UDM field is set to `create`.  
  
Else, if the `AuditOperationType` log field value is equal to `Client Session Revoked`, then the `metadata.product_event_type` UDM field is set to `client session revoked`.  
  
Else, if the `AuditOperationType` log field value is equal to `Delete`, then the `metadata.product_event_type` UDM field is set to `delete`.  
  
Else, if the `AuditOperationType` log field value is equal to `Download`, then the `metadata.product_event_type` UDM field is set to `download`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In`, then the `metadata.product_event_type` UDM field is set to `user_login`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In Failure`, then the `metadata.product_event_type` UDM field is set to `user_login_fail`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign Out`, then the `metadata.product_event_type` UDM field is set to `user_logout`.  
  
Else, if the `AuditOperationType` log field value is equal to `Session Time Out`, then the `metadata.product_event_type` UDM field is set to `session time out`.  
  
Else, if the `AuditOperationType` log field value is equal to `Update`, then the `metadata.product_event_type` UDM field is set to `update`.  
`` | `security_result.action` | If the `AuditOperationType` log field value is _not_ empty, then if the `AuditOperationType` log field value is equal to `Client Session Revoked`, then the `security_result.action` UDM field is set to `BLOCK`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Else, if the `AuditOperationType` log field value is equal to `Sign In Failure`, then the `security_result.action` UDM field is set to `FAIL`.  
`ObjectType` | `target.resource.resource_subtype` |   
`ObjectID` | `target.resource.product_object_id` |   
`ObjectName` | `target.resource.name` |   
`ModifiedTime` | `target.resource.attribute.labels[ModifiedTime]` |   
`ModifiedBy` | `principal.user.userid` | If the `Audit Operation Type` log field value contain one of the following values, then the `ModifiedBy` log field is mapped to the `principal.user.userid` UDM field. 

  * `Create`
  * `Delete`
  * `Update`
  * `Download`

  
`ModifiedBy` | `target.user.userid` | If the `Audit Operation Type` log field value contain one of the following values, then the `ModifiedBy` log field is mapped to the `target.user.userid` UDM field. 

  * `Sign In`
  * `Sign In Failure`
  * `Sign Out`
  * `Client Session Revoked`
  * `Session Time Out`

  
`User` | `principal.user.email_addresses` | If the `Audit Operation Type` log field value contain one of the following values and the `User` log field value matches the regular expression pattern `(^.*@.*$)`, then the `User` log field is mapped to the `principal.user.email_addresses` UDM field. 

  * `Create`
  * `Delete`
  * `Update`
  * `Download`

  
`User` | `principal.user.user_display_name` | If the `Audit Operation Type` log field value contain one of the following values and the `User` log field value _not_ matches the regular expression pattern `(^.*@.*$)`, then the `User` log field is mapped to the `principal.user.user_display_name` UDM field. 

  * `Create`
  * `Delete`
  * `Update`
  * `Download`

  
`User` | `target.user.email_addresses` | If the `Audit Operation Type` log field value contain one of the following values and the `User` log field value matches the regular expression pattern `(^.*@.*$)`, then the `User` log field is mapped to the `target.user.email_addresses` UDM field. 

  * `Sign In`
  * `Sign In Failure`
  * `Sign Out`
  * `Client Session Revoked`
  * `Session Time Out`

  
`User` | `target.user.user_display_name` | If the `Audit Operation Type` log field value contain one of the following values and the `User` log field value _not_ matches the regular expression pattern `(^.*@.*$)`, then the `User` log field is mapped to the `target.user.user_display_name` UDM field. 

  * `Sign In`
  * `Sign In Failure`
  * `Sign Out`
  * `Client Session Revoked`
  * `Session Time Out`

  
`AuditOldValue` | `additional.fields[AuditOldValue]` | Iterate through AuditOldValue object: The `AuditOldValue object key` is mapped to the `additional.fields.key` UDM field and `AuditOldValue object value` is mapped to the `additional.fields.value` UDM field.  
`AuditNewValue` | `additional.fields[AuditNewValue]` | Iterate through AuditNewValue object: The `AuditNewValue object key` is set to the `additional.fields.key` UDM field and `AuditNewValue object value` is mapped to the `additional.fields.value` UDM field.  
`CustomerID` | `metadata.product_deployment_id` |   
`ClientAuditUpdate` | `additional.fields[ClientAuditUpdate]` |   
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-zpa-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
