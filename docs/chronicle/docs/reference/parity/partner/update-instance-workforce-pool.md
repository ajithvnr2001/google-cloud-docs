---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-workforce-pool/
title: UpdateInstance (Workforce pool) APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:10.411080+00:00
---

# UpdateInstance (Workforce pool) APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-workforce-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateInstance (Workforce pool) APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`SetWorkforcePoolProvider`**) to the modern Chronicle API ([**`UpdateInstance`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/patch)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/setworkforcepoolprovider` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `UpdateInstance` and `Subdomain` APIs are hosted outside `TenantService` (under `InstanceService` and `SubdomainService`) and target resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}/...`). Partners cannot directly call these APIs using their own credentials to update identity or workforce pool provider configurations on tenant instances. For a partner to manage these resources, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.admin`, `chronicle.googleapis.com/instances.update`, or `chronicle.googleapis.com/subdomains.create`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`SetWorkforcePoolProvider`) | Modern Chronicle API (`UpdateInstance`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Endpoint URI** | `/v1/partner/customer/setworkforcepoolprovider` | `/v1alpha/{instance.name=projects/*/locations/*/instances/*}`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/instances.update`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers updated a customer's Workforce Identity Federation provider for a given subdomain using `SetWorkforcePoolProvider`. In the modern Chronicle API, workforce identity configurations are associated with subdomains (frontend paths).

At the instance level, `frontend_path_configs` is an `OUTPUT_ONLY` property on the `Instance` message (`Instance.frontend_path_configs[].workforce_pool_provider_id`). To provision, update, or remove workforce pool provider associations, callers manage first-class `Subdomain` resources using `CreateSubdomain` or `DeleteSubdomain` (`projects/*/locations/*/instances/*/subdomains/*`). When inspecting the instance via `UpdateInstance` or `GetInstance`, `frontend_path_configs` provides read-only visibility into the configured mappings.

Legacy field (`SetWorkforcePoolProviderRequest`) | Modern field (`UpdateInstanceRequest` / `Subdomain`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `instance.name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the target customer was identified globally by `customer_code`. In the modern API, the parent instance is identified by its canonical path: `projects/{project}/locations/{location}/instances/{instance}`.  
`customer_subdomain` | `Subdomain.name` / `frontend_path` | `string` | **Sub-resource model (`OUTPUT_ONLY` on `Instance`):** In the legacy API, `customer_subdomain` specified the custom subdomain prefix. On the modern `Instance` resource, this appears in `frontend_path_configs[].frontend_path` as an `OUTPUT_ONLY` field. Write operations are managed via the `Subdomain` resource (`projects/{project}/locations/{location}/instances/{instance}/subdomains/{subdomain}`).  
`provider_id` | `Subdomain.workforce_pool_provider` | `string` | **Resource reference mapping (`OUTPUT_ONLY` on `Instance`):** In the legacy API, `provider_id` was a bare identifier string. On the modern `Instance` resource, this is reflected in `frontend_path_configs[].workforce_pool_provider_id` (`OUTPUT_ONLY`). In the modern `Subdomain` API, this is specified as a full canonical resource name: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}`.  
— | `update_mask` | `google.protobuf.FieldMask` | **New field (partial update semantics):** A comma-separated list of field paths indicating which fields to update. Because `frontend_path_configs` is `OUTPUT_ONLY` on the `Instance` resource, mutations to workforce identity associations are executed via the `Subdomain` sub-resource methods rather than `update_mask`.  
  
* * *

## Response payload field-by-field parity

The legacy endpoint returned only the updated provider ID string, while the modern Chronicle API returns the complete updated `Instance` resource.

Legacy field (`SetWorkforcePoolProviderResponse`) | Modern field (`Instance` response message) | Field type | Parity and migration notes  
---|---|---|---  
`provider_id` | `frontend_path_configs[].workforce_pool_provider_id` | `repeated FrontendPathConfig` | **Restructured:** The modern API returns the complete `Instance` resource. Configured workforce pool providers are listed inside the `frontend_path_configs` array alongside their respective `frontend_path`. In the `Subdomain` API, `workforce_pool_provider` is returned directly on the `Subdomain` resource.  
— | `name` | `string` | **New field:** Canonical resource name of the updated instance (`projects/{project}/locations/{location}/instances/{instance}`).  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the instance (`ACTIVE`, `CREATING`, `SOFT_DELETED`, etc.).  
— | `display_name` | `string` | **New field:** Display name of the instance.  
— | `customer_code` | `string` | **New field:** Unique alphanumeric customer acronym/code.  
— | `secops_urls` | `repeated string` | **New field:** Fully qualified HTTPS URLs for navigating to the Google SecOps instance.  
— | `instance_config` | `InstanceConfig` | **New field:** Active feature toggle configurations for the instance.  
— | `compliance_requirements` | `ComplianceRequirements` | **New field:** Active compliance certification requirements for the instance.  
— | `entitlement` | `Entitlement` | **New field:** Subscription licensing and entitlement details.  
  
* * *

## Key differences

  * **First-class`Subdomain` resources vs. legacy RPC:**
    * In the legacy Backstory Partner API, `SetWorkforcePoolProvider` was a dedicated RPC on `CustomerService` that accepted `(customer_code, customer_subdomain, provider_id)`.
    * In the modern Chronicle API, subdomains and their associated identity providers are modeled as first-class child resources (`Subdomain`). Callers manage them using `CreateSubdomain`, `GetSubdomain`, `ListSubdomains`, and `DeleteSubdomain` under `projects/{project}/locations/{location}/instances/{instance}/subdomains/*`.
  * **Instance`OUTPUT_ONLY` aggregation:**
    * While `Subdomain` manages individual domain mappings, the `Instance` resource aggregates all configured subdomains and providers in the read-only `frontend_path_configs` list (`frontend_path` and `workforce_pool_provider_id`).
    * Consequently, `UpdateInstance` cannot mutate `frontend_path_configs` directly; mutations are performed via the subdomain lifecycle APIs.
  * **Canonical Workforce Identity Federation resource format:**
    * In the legacy API, callers passed a simple short `provider_id`.
    * In modern Chronicle, providers follow standard Google Cloud IAM resource paths: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}`.
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used global partner tokens or API keys to configure workforce pool providers and subdomains across customer codes.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `UpdateInstance` and `Subdomain` APIs are hosted under `InstanceService` and `SubdomainService` targeting the tenant's project resources (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}/...`), partners cannot use their own project credentials alone to modify workforce pool or subdomain configurations.
    * To manage workforce identity configurations for a tenant instance, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.admin` or custom roles with `chronicle.googleapis.com/instances.update` and `chronicle.googleapis.com/subdomains.create`) to the partner's authentication principal (service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`, `UpdateTenant`), which are managed in the partner's project using partner credentials.
  * **Exhaustive resource response:**
    * The legacy response returned only `{ "provider_id": "..." }`. The modern API returns the complete `Instance` resource (or `Subdomain` resource), providing full operational visibility into active configurations, endpoints, and statuses.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
