---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-cmdb/
title: Collect ServiceNow CMDB data \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:10:44.172600+00:00
---

# Collect ServiceNow CMDB data  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-cmdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ServiceNow CMDB data

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect ServiceNow CMDB data by setting up a Google Security Operations feed using the Third party API.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to ServiceNow instance with admin console access
  * ServiceNow user account with `cmdb_read` role (minimum requirement for read access)
  * REST API enabled in your ServiceNow instance (enabled by default)

**Caution:** You must enable allowlisting and add the IP ranges for all log types that ingest data from third-party APIs. For more information, see [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists).

## Configure IP allowlisting

Before creating the feed, you must allowlist Google SecOps IP ranges in your ServiceNow firewall or network settings.

### Get Google SecOps IP ranges

  * Fetch IP ranges from the [Google IP address ranges JSON file](https://www.gstatic.com/ipranges/goog.json).



### Add IP ranges to ServiceNow

**Note:** IP Address Access Control requires the IP Range Based Authentication plugin [com.snc.ipauthenticator] to be activated in your ServiceNow instance.

  1. Sign in to your **ServiceNow instance** as an administrator.
  2. Go to **All > System Security > IP Address Access Control**.
  3. Click **New**.
  4. Provide the following configuration details: 
     * **Type** : Select **Allow**.
     * **IP Address** : Enter oneGoogle SecOps IP range in CIDR notation (for example, `192.0.2.0/24`).
     * **Name** : Enter a descriptive name (for example, `GGoogle SecOps IP Range 1`).
     * **Active** : Select the checkbox to enable the rule.
  5. Click **Submit**.
  6. Repeat steps 3-5 for each additional Google SecOps IP range.

**Note:** If IP Address Access Control is not activated, go to **All > System Definition > Plugins**, search for "IP Range Based Authentication", and click **Activate/Upgrade**.

## Configure ServiceNow API access

To enable Google SecOps to pull CMDB data, you need to create a ServiceNow user with appropriate permissions.

### Create dedicated integration user (recommended)

  1. Sign in to the **ServiceNow Admin Console**.
  2. Go to **All > User Administration > Users**.
  3. Click **New**.
  4. Provide the following configuration details: 
     * **User ID** : Enter a descriptive username (for example, `google_secops_integration`).
     * **First name** : Enter `Google`.
     * **Last name** : Enter `SecOps Integration`.
     * **Email** : Enter a valid email address for notifications.
     * **Password** : Click **Set Password** and create a strong password.
     * **Active** : Select the checkbox.
     * **Web service access only** : Select the checkbox (recommended for API-only access).
  5. Click **Submit**.



### Assign required permissions

  1. After creating the user, open the user record.
  2. Go to the **Roles** section.
  3. Click **Edit**.
  4. In the **Collection** list, search for and add the following role: 
     * **cmdb_read** : Provides read access to CMDB tables.
  5. Click **Save**.

**Note:** The `cmdb_read` role grants read access to all CMDB configuration item (CI) tables. If you need write access for other integrations, you may also assign the `itil` role, but this is not required for Google SecOps ingestion.

### Record API credentials

After creating the user, record the following credentials:

  * **Username** : The User ID you created (for example, `google_secops_integration`)
  * **Password** : The password you set for the user
  * **API Hostname** : Your ServiceNow instance FQDN (for example, `myinstance.servicenow.com`) 
    * Do not include `https://` or any paths.
    * Do not include trailing slash.
  * **Table Name** : The CMDB table to query (for example, `cmdb_ci`, `cmdb_ci_server`, `cmdb_ci_computer`)

**Important:** Copy and save these credentials securely. You will need them when configuring the Google SecOps feed.

## Understanding ServiceNow CMDB tables

The ServiceNow CMDB is organized in a hierarchical structure of tables. The most common tables for asset data ingestion include:

Table Name | Description | Use Case  
---|---|---  
`cmdb_ci` | Base Configuration Item table (parent of all CI tables) | All configuration items  
`cmdb_ci_server` | Server configuration items | Physical and virtual servers  
`cmdb_ci_computer` | Computer configuration items | Workstations, laptops, desktops  
`cmdb_ci_linux_server` | Linux server configuration items | Linux servers specifically  
`cmdb_ci_win_server` | Windows server configuration items | Windows servers specifically  
`cmdb_ci_vm_instance` | Virtual machine instances | Virtual machines  
`cmdb_ci_network_adapter` | Network adapters | Network interface cards  
`cmdb_ci_ip_address` | IP addresses | IP address records  
`cmdb_ci_service` | Business services | Service catalog items  
`cmdb_ci_appl` | Applications | Application configuration items  
**Note:** Querying the base `cmdb_ci` table will return all configuration items across all child tables. To retrieve specific types of CIs (for example, only servers), use the appropriate child table.

## Verify REST API access

Before creating the feed, verify that your ServiceNow API credentials work correctly.

### Test using REST API Explorer (optional)

  1. Sign in to your **ServiceNow instance** as the integration user.
  2. Go to **All > System Web Services > REST > REST API Explorer**.
  3. Select **Table API** from the namespace drop-down.
  4. Select **Retrieve records from a table (GET)**.
  5. In **Path Parameters** , enter the table name (for example, `cmdb_ci`).
  6. Click **Send**.
  7. Verify that the response status is **200 OK** and records are returned.



### Test using curl (optional)

  * Alternatively, test the API using curl:
        
        curl "https://your-instance.service-now.com/api/now/table/cmdb_ci?sysparm_limit=10" \
        --request GET \
        --header "Accept: application/json" \
        --user 'your-username':'your-password'
        

    * Replace: 
      * `your-instance.service-now.com`: Your ServiceNow instance hostname
      * `your-username`: Your integration user username
      * `your-password`: Your integration user password



A successful response will return JSON data with configuration items.

## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ServiceNow CMDB - All CIs` or `ServiceNow CMDB - Servers`).
  5. Select **Third party API** as the **Source type**.
  6. Select **ServiceNow CMDB** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Username** : Enter the ServiceNow user ID (for example, `google_secops_integration`).
     * **Secret** : Enter the ServiceNow user password. Important: This is a sensitive field. The password is encrypted and cannot be viewed after saving.
     * **API Hostname** : Enter the fully qualified domain name of your ServiceNow instance. 
       * **Example:** `myinstance.servicenow.com`
       * **Do not include:**
         * Protocol (`https://`)
         * Paths (`/api/now/table/`)
         * Trailing slash
     * **Regional instances:** If your ServiceNow instance is in a specific region, use the correct hostname format: 
       * Standard: `instance.service-now.com`
       * European Union: `instance.service-now.eu`
       * Other regions: Verify with your ServiceNow administrator
     * **Table Name** : Enter the ServiceNow CMDB table to query. 
       * **Examples:**
         * `cmdb_ci` (all configuration items)
         * `cmdb_ci_server` (all servers)
         * `cmdb_ci_computer` (workstations and computers)
         * `cmdb_ci_linux_server` (Linux servers only)
         * `cmdb_ci_win_server` (Windows servers only) Note: The table name is case-sensitive and must match exactly. You can query only one table per feed. To ingest multiple tables, create separate feeds for each table.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve CMDB records from the ServiceNow instance. The initial sync may take several minutes depending on the number of records in the table.

## Ingesting multiple CMDB tables

To ingest data from multiple CMDB tables, create separate feeds for each table:

  1. Create the first feed using the steps above (for example, for `cmdb_ci_server`).
  2. Click **Add New Feed** to create additional feeds.
  3. Use the same ServiceNow credentials but specify different table names.



**Example configuration:**

Feed Name | Table Name | Purpose  
---|---|---  
ServiceNow CMDB - Servers | `cmdb_ci_server` | All server CIs  
ServiceNow CMDB - Computers | `cmdb_ci_computer` | Workstation CIs  
ServiceNow CMDB - Network Adapters | `cmdb_ci_network_adapter` | Network interface CIs  
ServiceNow CMDB - Applications | `cmdb_ci_appl` | Application CIs  
**Note:** Each feed polls the ServiceNow API independently. Consider the API rate limits and polling frequency when creating multiple feeds.

## Required API permissions

The integration user requires the following ServiceNow permissions:

Permission/Role | Access Level | Purpose  
---|---|---  
**cmdb_read** | Read | Retrieve CMDB configuration item data  
  
**Additional roles (optional):**

  * **itil** : Required if you need write access to create or update CIs (not required for Google SecOps ingestion)
  * **rest_api_explorer** : Useful for testing API access during setup

**Note:** Using least-privilege access. Only read permissions are required; write permissions are not needed for log ingestion.

## UDM mapping table

ServiceNow Field | UDM Mapping | Logic  
---|---|---  
`name` | `entity.asset.hostname` | Primary hostname of the asset  
`ip_address` | `entity.asset.ip` | Primary IP address of the asset  
`mac_address` | `entity.asset.mac` | MAC address of the asset  
`serial_number` | `entity.asset.hardware.serial_number` | Hardware serial number  
`asset_tag` | `entity.asset.asset_id` | Asset tag or identifier  
`sys_class_name` | `entity.asset.asset_type` | CI class (server, computer, etc.)  
`os` | `entity.asset.platform_software.platform` | Operating system  
`sys_created_on` | `entity.asset.first_seen_time` | Asset creation timestamp  
`sys_updated_on` | `entity.asset.last_seen_time` | Last update timestamp  
`location` | `entity.asset.location.name` | Physical location  
`company` | `entity.asset.attribute.labels.value` | Owning company/organization  
`event.idm.entity.entity.metadata.entity_type` | `USER` | Mapped from changelog  
`calendar_integration", "u_ldap_source", "u_show_popup", "source", "building", "web_service_access_only", "notification", "enable_multifactor_authn", "sso_source", "sys_domain.display_value", "sys_domain.link", "u_itil_license_type", and "u_assets_validated` | `entity.entity.asset.attribute.labels` | Mapped from changelog  
`last_login_time` | `entity.relation.entity.user.last_login_time` | Mapped from changelog  
`x_bmgr_support_ent_bomgar_username", "vip", "zip", "time_format", "active", "gender", "failed_attempts", "federated_id", "internal_integration_user", "u_business_line", "department.link", "introduction", "preferred_language", "manager.link", "photo", "avatar", "time_zone", "schedule", and "correlation_id` | `entity.relation.entity.user.attribute.labels` | Mapped from changelog  
`street` | `entity.relation.entity.user.personal_address.name` | Mapped from changelog  
`department.display_value` | `entity.relation.entity.user.department` | Mapped from changelog  
`u_office` | `entity.relation.entity.user.company_name` | Mapped from changelog  
`title` | `entity.relation.entity.user.title` | Mapped from changelog  
`first_name` | `entity.relation.entity.user.first_name` | Mapped from changelog  
`last_name` | `entity.relation.entity.user.last_name` | Mapped from changelog  
`middle_name` | `entity.relation.entity.user.middle_name` | Mapped from changelog  
`manager.display_value` | `entity.relation.entity.user.managers.user_display_name` | Mapped from changelog  
`sys_domain_path", "transaction_log", "cost_center", "sys_mod_count", and "sys_tags` | `entity.entity.labels` | Mapped from changelog  
`employee_number", "phone", "home_phone", and "mobile_phone` | `entity.relation.entity.user.phone_numbers` | Mapped from changelog  
`city` | `entity.relation.entity.user.personal_address.city` | Mapped from changelog  
`state` | `entity.relation.entity.user.personal_address.state` | Mapped from changelog  
`country` | `entity.location.country_or_region` | Mapped from changelog  
`u_site_code` | `entity.location.city` | Mapped from changelog  
`u_region` | `entity_labels` | Mapped from changelog  
`location.display_value` | `entity.labels` | Mapped from changelog  
`location.link` | `entity.labels` | Mapped from changelog  
`email` | `_relation.entity.user.email_addresses` | Mapped from changelog  
`sys_id` | `entity.asset.product_object_id` | Mapped from changelog  
`u_sima_bs_activation_date", "attestation_status", "u_oracle_asm_lun_size", "u_app_resource_jndi_name", "is_encrypted", "monitor", "operational_status", "u_updated_ci", "u_cluster_node", "firewall_status", "skip_sync", "u_excluded", "u_data_classification", "u_sla_report", "u_restriction", "u_rack_slot", "u_account_aztech_oe.link", "u_account_aztech_oedisplay_value", "u_organisational_entity.link", "u_organisational_entity.display_value", "assignment_group.link", "assignment_group.display_value", "cost_center.link", "cost_center.display_value", "u_service_instance", "u_local_oe_cost_center", "managed_by", "u_mode_of_operation", "install_status", and "u_provider_tag` | `entity.labels` | Mapped from changelog  
`u_build_user` | `entity.user.email_addresses` | Mapped from changelog  
`metadata.entity_type` | `ASSET` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-cmdb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
