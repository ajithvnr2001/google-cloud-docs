---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/list-tenants/
title: ListTenants APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:00.509033+00:00
---

# ListTenants APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/list-tenants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListTenants APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`ListCustomersOfPartner`**) to the modern Chronicle API ([**`ListTenants`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants/list)).

> [!NOTE] Unlike instance-level APIs that target resources in tenant projects, `TenantService` methods (such as `ListTenants`, `CreateTenant`, and `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`). Partners call these directly using their own IAM credentials authorized for their partner project. In contrast, managing tenant resources using `InstanceService` or `ForwarderService` requires cross-project IAM delegation granted by the tenant.

## Protocol and mapping overview

Feature | Legacy API (`ListCustomersOfPartner`) | Modern Chronicle API (`ListTenants`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Endpoint URI** | `/v1/partner/customer/listcustomers` | `/v1alpha/{parent=projects/*/locations/*/instances/*}/tenants`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/tenants.list`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers retrieved customers of a partner without providing a resource hierarchy path (the partner was inferred from the authorization token). In the modern Chronicle API, list operations are explicitly scoped to the parental instance resource hierarchy using standard Google Cloud pagination parameters.

Legacy field (`ListCustomersOfPartnerRequest`) | Modern field (`ListTenantsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the partner context was inferred implicitly from the caller's auth token. In the modern API, callers must explicitly provide the parent instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Maximum number of items to return per page. In the legacy API, default and maximum page size was up to 10,000. In the modern API, the default page size is 10 and maximum is 100.  
`page_token` | `page_token` | `string` | **Parity mapped:** Pagination continuation token received from a previous list response to fetch the next page of results.  
  
* * *

## Response payload field-by-field parity

Both endpoints return a paginated collection of customer or tenant organizations.

Legacy field (`ListCustomersOfPartnerResponse`) | Modern field (`ListTenantsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`customers` | `tenants` | `repeated Customer` $\rightarrow$ `repeated Tenant` | **Parity mapped:** The collection of customer/tenant records. Each entry maps from the legacy `Customer` message schema to the modern `Tenant` resource schema (see the detailed resource parity table below).  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Token to retrieve the next page of results. In the legacy API, pagination was noted as unsupported. In the modern API, standard AIP-158 pagination is fully supported.  
  
### Customer-to-Tenant resource schema parity

Each record in the returned list maps between the legacy `Customer` schema and the modern `Tenant` schema as follows:

Legacy field (`Customer` message) | Modern field (`Tenant` message) | Field type | Parity and migration notes  
---|---|---|---  
`id` / `customer_id` | `name` | `string` | **Parity mapped:** In the legacy API, the customer was identified by a UUID string (`id`) and raw binary identifier (`customer_id`). In the modern API, the tenant is identified by its canonical Google Cloud resource name: `projects/{project}/locations/{location}/instances/{instance}/tenants/{tenant_id}`.  
`customer_name` | `display_name` | `string` | **Parity mapped:** User-visible display name of the tenant organization.  
`customer_code` | `customer_code` | `string` | **Parity mapped:** Alphanumeric customer identifier code.  
`customer_subdomains` | `frontend_path_configs[].frontend_path` | `repeated string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, consolidated:** In the legacy API, `customer_subdomains` specified subdomains used to access Backstory (`<subdomain>.backstory.chronicle.security`). In the modern API, this is structured under `frontend_path_configs`, where each entry maps a `frontend_path` to its corresponding workforce pool provider.  
`provider_id` | `frontend_path_configs[].workforce_pool_provider_id` | `string` $\rightarrow$ `repeated FrontendPathConfig` | **Parity mapped, structured:** In the legacy API, `provider_id` was a standalone workforce pool provider ID. In the modern API, it is configured within each `FrontendPathConfig` entry as `workforce_pool_provider_id` (format: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}`).  
`gcp_project_number` | `tenant_gcp_project` | `uint64` $\rightarrow$ `string` | **Parity mapped:** Bound Google Cloud project path (`projects/{project_id}` or `projects/{project_number}`).  
`retention_duration` | `retention_duration` | `string` $\rightarrow$ `RetentionDuration` (enum) | **Parity mapped:** Contractually agreed data retention period. Legacy string values map to typed enum values (`ONE_YEAR`, `SIX_MONTHS`, `EIGHTEEN_MONTHS`, `TWO_YEARS`, `THREE_YEARS`, `FOUR_YEARS`, etc.).  
`auth_version` | `auth_method` | `AuthVersion` $\rightarrow$ `AuthMethod` (enum) | **Restructured:** In the legacy API, authentication was selected using `auth_version` (`AUTH_VERSION_1` to `AUTH_VERSION_4`). In the modern API, authentication is configured using the `auth_method` enum (`WORKFORCE_IDENTITY_FEDERATION` or `CLOUD_IDENTITY`).  
`sso_config` | — | `SSOConfig` | **Retired:** In the legacy API, SAML SSO was tracked via uploaded raw IdP metadata XML bytes. In the modern Chronicle API, identity federation is managed natively using Workforce Identity Federation or Cloud Identity.  
`credentials` | — | `repeated Credential` | **Retired:** Legacy API returned provisioned API keys and tokens. Modern access control is governed by standard Google Cloud IAM roles and service accounts.  
`forwarders` | — | `repeated string` | **Decoupled:** Forwarders are managed independently using modern Forwarder Management APIs (`/forwarders`).  
`looker_detail` | — | `LookerDetail` | **Decoupled:** Embedded Looker slot details are managed automatically by Google SecOps platform infrastructure.  
`compliance_certifications` | — | `repeated ComplianceCertification` | **Restructured:** In the modern architecture, compliance certifications are configured at the parent instance level (`compliance_requirements`) rather than per individual tenant.  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the tenant (`ACTIVE`, `CREATING`, `DELETING`, etc.).  
— | `billing_account` | `string` | **New field:** The Cloud Billing account resource path associated with the customer contract (format: `billingAccounts/{billing_account_id}`).  
— | `provisioning_flow` | `ProvisioningFlow` (enum) | **New field:** Identifies the provisioning workflow executed (`BACKSTORY_API_PARITY` or `TENANT_ATTRIBUTION`).  
  
* * *

## Key differences

  * **Google Cloud resource hierarchy scoping:**
    * The legacy `ListCustomersOfPartner` implicitly inferred the partner scope from authentication tokens.
    * Modern `ListTenants` requires explicit parental scoping via `projects/{project}/locations/{location}/instances/{instance}` in the request URL.
  * **Standard AIP-158 pagination:**
    * While the legacy API defined pagination fields (`page_size`, `page_token`), server-side pagination was largely unpopulated. The modern API strictly implements standard Google Cloud AIP-158 pagination with default page sizes of 10 and max page sizes of 100.
  * **Authorization modernization:**
    * Legacy partner tokens and API keys are replaced by standard Google Cloud IAM authorization checks (`chronicle.googleapis.com/tenants.list`) evaluated against the partner's parent instance resource in the partner project. Unlike instance-level APIs targeting tenant projects, partners do not require cross-project delegation from tenants to list their own tenants.
  * **Modernized tenant schema:**
    * Returned tenant records modernize authentication (`auth_method`), frontend path routing (`frontend_path_configs`), and billing linkage (`billing_account`), while separating client credentials and forwarders into dedicated subsystems.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
