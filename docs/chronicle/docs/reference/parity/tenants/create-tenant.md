---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/tenants/create-tenant/
title: CreateTenant APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:11.214287+00:00
---

# CreateTenant APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/tenants/create-tenant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CreateTenant APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`CreateCustomer`**) to the modern Chronicle API ([**`CreateTenant`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants/create)).

## Protocol and mapping overview

Feature | Legacy API (`CreateCustomer`) | Modern Chronicle API (`CreateTenant`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/tenants.create`  
  
* * *

## Request payload field-by-field parity

The legacy call provisioned a new customer organization under a partner. The modern Chronicle API provisions a tenant resource under a parent instance using the `CreateTenantRequest` payload.

Legacy field (`CreateCustomerRequest`) | Modern field (`CreateTenantRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** In the legacy API, the target partner was authenticated globally without a resource hierarchy path. In the modern API, the request scopes tenant creation under the parental instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`customer_name` | `tenant.display_name` | `string` | **Parity mapped:** Renamed from `customer_name` to `display_name`. Represents the human-readable display name of the customer/tenant organization.  
`customer_code` | `tenant.customer_code` | `string` | **Parity mapped:** Alphanumeric customer identifier code (for example, a 3-5 character customer acronym or ID).  
`customer_subdomains` | `tenant.frontend_path_configs[].frontend_path` | `repeated string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, consolidated:** In the legacy API, `customer_subdomains` specified subdomains used to access Backstory (`<subdomain>.backstory.chronicle.security`). In the modern API, this is structured under `frontend_path_configs`, where each entry maps a `frontend_path` to its corresponding workforce pool provider.  
`provider_id` | `tenant.frontend_path_configs[].workforce_pool_provider_id` | `string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, structured:** In the legacy API, `provider_id` was a standalone workforce pool provider ID for BYOID. In the modern API, it is configured within each `FrontendPathConfig` entry as `workforce_pool_provider_id` (format: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}`).  
`gcp_project` | `tenant.tenant_gcp_project` | `string` | **Parity mapped:** Customer's Bring Your Own Project (BYOP) Google Cloud project. In the legacy API, this was passed as a raw project ID string. In the modern API, it must be passed as a canonical resource name: `projects/{project_id}` or `projects/{project_number}`.  
`retention_duration` | `tenant.retention_duration` | `RetentionDuration` (enum) | **Parity mapped:** Customer contract data retention duration. Legacy enum values (`ONE_YEAR = 1`, `SIX_MONTHS = 2`) map directly to modern values (`ONE_YEAR = 1`, `SIX_MONTHS = 3`). The modern API also supports extended durations (`EIGHTEEN_MONTHS`, `TWO_YEARS`, `THREE_YEARS`, `FOUR_YEARS`). Note that `retention_duration` is a required field in `CreateTenant`.  
`auth_version` | `tenant.auth_method` | `AuthVersion` $\rightarrow$ `AuthMethod` (enum) | **Restructured:** In the legacy API, authentication was selected using `auth_version` (`AUTH_VERSION_1` to `AUTH_VERSION_4`). In the modern API, authentication is configured using the `auth_method` enum (`WORKFORCE_IDENTITY_FEDERATION` or `CLOUD_IDENTITY`).  
`sso_config` | — | `bytes` | **Retired:** In the legacy API, SAML SSO was provisioned by uploading raw XML configuration bytes. In the modern Chronicle API, identity federation is managed natively using Workforce Identity Federation or Cloud Identity.  
— | `tenant.billing_account` | `string` | **New required field:** Specifies the Cloud Billing account resource path associated with the customer contract (format: `billingAccounts/{billing_account_id}`).  
— | `tenant.provisioning_flow` | `ProvisioningFlow` (enum) | **New optional field:** Specifies the provisioning flow variant (`BACKSTORY_API_PARITY` for Backstory API parity migration, or `TENANT_ATTRIBUTION` for tenant attribution).  
— | `tenant.name` | `string` | **Read-only / identifier:** The server-assigned canonical resource path for the tenant: `projects/{project}/locations/{location}/instances/{instance}/tenants/{tenant_id}`.  
— | `tenant.state` | `State` (enum) | **Output only:** Current lifecycle state of the tenant (for example, `CREATING`, `ACTIVE`, `DELETING`).  
  
* * *

## Response payload field-by-field parity

Both endpoints return a long-running operation (`google.longrunning.Operation`). The legacy operation resolved to a `Customer` resource containing provisioned credentials and forwarders, while the modern operation returns a `Tenant` resource alongside workflow metadata in `TenantMetadata`.

Legacy field (`Customer` message) | Modern field (`Tenant` message) | Field type | Parity and migration notes  
---|---|---|---  
`id` / `customer_id` | `name` | `string` | **Parity mapped:** In the legacy API, the customer was identified by a UUID string (`id`) and raw binary identifier (`customer_id`). In the modern API, the tenant is identified by its canonical Google Cloud resource name: `projects/{project}/locations/{location}/instances/{instance}/tenants/{tenant_id}`.  
`customer_name` | `display_name` | `string` | **Parity mapped:** User-visible display name of the tenant organization.  
`customer_code` | `customer_code` | `string` | **Parity mapped:** Customer acronym/code identifier.  
`customer_subdomains` | `frontend_path_configs[].frontend_path` | `repeated string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped:** Associated frontend paths for accessing the instance.  
`provider_id` | `frontend_path_configs[].workforce_pool_provider_id` | `string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped:** Associated workforce pool provider IDs.  
`gcp_project_number` | `tenant_gcp_project` | `uint64` $\rightarrow$ `string` | **Parity mapped:** Bound Google Cloud project path (`projects/{project_id}` or `projects/{project_number}`).  
`retention_duration` | `retention_duration` | `string` $\rightarrow$ `RetentionDuration` (enum) | **Parity mapped:** Contractually agreed data retention period.  
`auth_version` | `auth_method` | `AuthVersion` $\rightarrow$ `AuthMethod` (enum) | **Parity mapped:** Active authentication mechanism for the tenant.  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the provisioned tenant (`ACTIVE`, `CREATING`, `DELETING`, etc.).  
— | `billing_account` | `string` | **New field:** The Cloud Billing account resource path tied to the tenant contract.  
— | `provisioning_flow` | `ProvisioningFlow` (enum) | **New field:** Identifies the provisioning workflow executed (`BACKSTORY_API_PARITY` or `TENANT_ATTRIBUTION`).  
`credentials` | — | `repeated Credential` | **Retired:** Legacy API issued client credentials (API keys and tokens). Modern access control is governed by standard Google Cloud IAM roles and service accounts.  
`forwarders` | — | `repeated string` | **Decoupled:** Forwarders are managed independently using modern Forwarder Management APIs (`/forwarders`).  
`sso_config` | — | `SSOConfig` | **Retired:** SSO configuration is managed through standard Workforce Identity Federation configurations.  
`looker_detail` | — | `LookerDetail` | **Decoupled:** Embedded Looker slot details are managed automatically by Google SecOps platform infrastructure.  
`compliance_certifications` | — | `repeated ComplianceCertification` | **Restructured:** In the modern architecture, compliance certifications are configured at the parent instance level (`compliance_requirements`) rather than per individual tenant.  
  
### Long-running operation metadata parity

The modern API populates `google.longrunning.Operation.metadata` with `TenantMetadata`:

Modern field (`TenantMetadata`) | Field type | Description  
---|---|---  
`creation_workflow_status` | `WorkflowState` (enum) | Execution state of the tenant creation workflow (`RUNNING`, `FINISHED`, `ERROR`, `CANCELLED`, `WAITING`, `QUEUED`, `PAUSED`, `SKIPPED`).  
`tenant` | `string` | Canonical resource path of the tenant being created (`projects/{project}/locations/{location}/instances/{instance}/tenants/{tenant_id}`).  
  
* * *

## Key differences

  * **Google Cloud resource model integration:**
    * Tenant creation is scoped under a parent instance resource: `projects/{project}/locations/{location}/instances/{instance}`.
    * Associated projects (`tenant_gcp_project`) and billing accounts (`billing_account`) use standard Google Cloud resource name formats.
  * **Consolidated frontend path and identity provider configs:**
    * Rather than separate lists of subdomains and a standalone provider ID, modern `frontend_path_configs` explicitly pairs each frontend URL path with its corresponding Workforce Identity Pool provider.
  * **Authentication and credential modernization:**
    * Raw SAML XML (`sso_config`) uploads and API-generated legacy credentials (`credentials`) are replaced by standard Workforce Identity Federation / Cloud Identity integration and Cloud IAM service account authorization.
  * **Billing account linkage:**
    * Callers must explicitly specify `billing_account` linked to an active SecOps contract.
  * **Operation polling and status tracking:**
    * Both APIs use long-running operations, but the modern API enriches operation progress with `TenantMetadata` providing granular workflow lifecycle states (`creation_workflow_status`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
