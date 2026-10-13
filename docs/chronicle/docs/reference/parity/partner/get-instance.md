---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/get-instance/
title: GetInstance APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:27.562341+00:00
---

# GetInstance APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/get-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetInstance APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`GetCustomer`**) to the modern Chronicle API ([**`GetInstance`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/get)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/getcustomer` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `GetInstance` is hosted outside `TenantService` (under `InstanceService`) and targets resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`). Partners cannot call `GetInstance` using their own credentials to access tenant data. For a partner to retrieve tenant instance metadata, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.viewer` or `chronicle.googleapis.com/instances.get`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using their own credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`GetCustomer`) | Modern Chronicle API (`GetInstance`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Endpoint URI** | `/v1/partner/customer/getcustomer` | `/v1/{name=projects/*/locations/*/instances/*}`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/instances.get`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers retrieved customer information by supplying the alphanumeric `customer_code` as a query parameter. In the modern Chronicle API, callers retrieve instance properties using the canonical Google Cloud resource name path.

Legacy field (`GetCustomerRequest`) | Modern field (`GetInstanceRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** In the legacy API, callers queried customer details using an alphanumeric customer code (`customer_code`). In the modern API, instances are addressed by their canonical resource name: `projects/{project}/locations/{location}/instances/{instance}`.  
  
* * *

## Response payload field-by-field parity

The legacy endpoint returned customer details in a `Customer` message, while the modern Chronicle API returns the comprehensive `Instance` resource schema.

Legacy field (`Customer` message) | Modern field (`Instance` message) | Field type | Parity and migration notes  
---|---|---|---  
`id` / `customer_id` | `name` | `string` | **Parity mapped:** In the legacy API, the customer was identified by a UUID string (`id`) and raw binary identifier (`customer_id`). In the modern API, the instance is identified by its canonical Google Cloud resource name: `projects/{project}/locations/{location}/instances/{instance}`. The unique instance identifier is the final segment of this path.  
`customer_code` | `customer_code` | `string` | **Direct 1:1 parity:** Both fields represent the customer's alphanumeric acronym/code identifier.  
`customer_name` | `display_name` | `string` | **Parity mapped:** Renamed to `display_name`. User-visible display name of the customer or instance organization.  
`customer_subdomains` | `frontend_path_configs[].frontend_path` | `repeated string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, structured:** In the legacy API, `customer_subdomains` listed the subdomains used to access Backstory (`<subdomain>.backstory.chronicle.security`). In the modern API, this is structured under `frontend_path_configs`, where each entry maps a `frontend_path` to its corresponding workforce pool provider. In addition, the fully qualified URLs are returned in `secops_urls`.  
`provider_id` | `frontend_path_configs[].workforce_pool_provider_id` | `string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, structured:** In the legacy API, `provider_id` was a standalone workforce pool provider ID. In the modern API, it is configured within each `FrontendPathConfig` entry as `workforce_pool_provider_id` (format: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}`).  
`gcp_project_number` | `name` _(parent project)_ | `uint64` $\rightarrow$ `string` | **Parity mapped (resource hierarchy):** In the legacy API, the bound project number was returned as an integer. In the modern API, the project context is embedded directly within the parental hierarchy of the resource name (`projects/{project}`).  
`retention_duration` | `entitlement.data_retention_duration` | `string` $\rightarrow$ `RetentionDuration` (enum) | **Parity mapped, structured:** Legacy API returned a string representation of retention duration (for example, `"1 year"`). In the modern API, retention duration is returned as a typed enum under `entitlement.data_retention_duration` (`ONE_YEAR`, `SIX_MONTHS`, `EIGHTEEN_MONTHS`, `TWO_YEARS`, `THREE_YEARS`, `FOUR_YEARS`, `FIVE_YEARS`, etc.).  
`compliance_certifications` | `compliance_requirements.compliance_certifications` | `repeated ComplianceCertification` (enum) | **Parity mapped, structured:** Mapped under `compliance_requirements`. Supports standard certifications (`FEDRAMP_MODERATE`, `HIPAA`, `PCI_DSS`) as well as extended certifications (`FEDRAMP_HIGH`, `IL4`, `IL5`, `CHRONICLE_CMEK_V1`, `DRZ_ADVANCED`, and regional data boundaries).  
`auth_version` | — | `AuthVersion` (enum) | **Retired / Restructured:** In the legacy API, authentication was tracked by numbered versions (`AUTH_VERSION_1` to `AUTH_VERSION_4`). In the modern Chronicle architecture, authentication is governed per-tenant using `auth_method` or configured at the instance level using `frontend_path_configs`.  
`sso_config` | — | `SSOConfig` | **Retired:** In the legacy API, SAML SSO was tracked using uploaded raw IdP metadata XML bytes. In the modern Chronicle API, SSO is managed natively using standard Workforce Identity Federation or Cloud Identity configurations.  
`credentials` | — | `repeated Credential` | **Retired:** Legacy API returned provisioned API keys and tokens for Backstory, Ingestion, BigQuery, and Forwarder APIs. Modern Chronicle API access is governed by standard Google Cloud IAM roles and OAuth 2.0 service account credentials.  
`forwarders` | — | `repeated string` | **Decoupled:** Forwarders are managed independently using dedicated Forwarder Management APIs (`/forwarders`), such as `ListForwarders`.  
`looker_detail` | — | `LookerDetail` | **Decoupled:** Embedded Looker slot details are managed automatically by Google SecOps platform infrastructure.  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the instance (`ACTIVE`, `SOFT_DELETED`, `SOFT_DELETE_INITIATED`, `UNDELETE_INITIATED`).  
— | `wipeout_status` | `WipeoutState` (enum) | **New field:** Granular status of instance deletion or wipeout workflow (`DELETE_REQUESTED`, `SOFT_DELETE_IN_PROGRESS`, `SOFT_DELETE_COMPLETED`, `WIPED_OUT`, etc.).  
— | `create_time` | `google.protobuf.Timestamp` | **New field:** Timestamp indicating when the instance was created.  
— | `delete_time` | `google.protobuf.Timestamp` | **New field:** Timestamp indicating when the instance was soft-deleted.  
— | `purge_time` | `google.protobuf.Timestamp` | **New field:** Earliest timestamp when a soft-deleted instance will be permanently removed.  
— | `secops_urls` | `repeated string` | **New field:** Fully qualified HTTPS URLs for navigating to the Google SecOps instance (format: `https://{frontend_path}.backstory.chronicle.security`).  
— | `instance_config` | `InstanceConfig` (message) | **New field:** Feature toggle configurations representing enabled capabilities, such as `secops_ui_enabled`, `data_rbac_enabled`, `triage_agent_enabled`, and `sts_migration_enrolled`.  
— | `entitlement` | `Entitlement` (message) | **New field:** Comprehensive licensing and subscription metadata, including `package_tier`, `billing_account_id`, `service_start_time`, `service_end_time`, `data_volume`, and DRE alignment status.  
  
* * *

## Key differences

  * **Google Cloud resource model integration:**
    * In the legacy API, customers were retrieved using a flat `customer_code` parameter. In the modern API, instances are addressed using canonical Google Cloud resource paths: `projects/{project}/locations/{location}/instances/{instance}`.
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used global partner tokens or API keys to retrieve details for any customer code.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `GetInstance` is part of `InstanceService` and targets the tenant's project resource (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`), partners cannot use their own project credentials alone to view tenant instance details.
    * To manage or view a tenant's instance, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.viewer` or custom role with `chronicle.googleapis.com/instances.get`) to the partner's authentication principal (such as a service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`), which are managed in the partner's project using partner credentials.
  * **Consolidated identity federation and frontend routing:**
    * Rather than managing separate lists of subdomains, standalone provider IDs, and raw SAML XML (`sso_config`), modern instances configure `frontend_path_configs`, which explicitly associate each frontend path with its corresponding Workforce Identity Federation provider.
  * **Decoupled resource management:**
    * Forwarders (`forwarders`) and embedded Looker slots (`looker_detail`) are separated from instance metadata. Forwarders are queried and managed through modern Forwarder Management APIs (`/forwarders`), and analytics slots are managed platform-natively.
  * **Comprehensive lifecycle and entitlement visibility:**
    * The modern `Instance` resource provides deep operational transparency with explicit lifecycle states (`state`, `wipeout_status`), deletion retention timestamps (`delete_time`, `purge_time`), feature flags (`instance_config`), and commercial subscription entitlements (`entitlement`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
