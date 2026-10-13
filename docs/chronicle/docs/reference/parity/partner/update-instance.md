---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance/
title: UpdateInstance (Auth version) APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:08.439384+00:00
---

# UpdateInstance (Auth version) APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateInstance (Auth version) APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`SetAuthVersion`**) to the modern Chronicle API ([**`UpdateInstance`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/patch)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/setauthversion` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `UpdateInstance` is hosted outside `TenantService` (under `InstanceService`) and targets resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`). Partners cannot directly call `UpdateInstance` using their own credentials to update tenant instance configurations. For a partner to update these resources, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.admin` or `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`SetAuthVersion`) | Modern Chronicle API (`UpdateInstance`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Endpoint URI** | `/v1/partner/customer/setauthversion` | `/v1alpha/{instance.name=projects/*/locations/*/instances/*}`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/instances.update`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers updated the authentication version using a dedicated RPC (`SetAuthVersion`) by specifying the customer code. In the modern Chronicle API, updates are performed using a standard RESTful `PATCH` method with a `google.protobuf.FieldMask` targeting the canonical instance resource path.

Legacy field (`SetAuthVersionRequest`) | Modern field (`UpdateInstanceRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `instance.name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the customer was addressed globally using `customer_code`. In the modern API, the instance is targeted via its canonical resource name: `projects/{project}/locations/{location}/instances/{instance}`.  
`auth_version` | `instance.instance_config` / identity configurations | `AuthVersion` (enum) $\rightarrow$ `Message` | **Architectural evolution:** Legacy `auth_version` values (`AUTH_VERSION_1` to `AUTH_VERSION_4`) tracked historical login routing models (such as GAIA B2B authentication). In the modern Chronicle architecture, authentication federation is configured directly using Workforce Identity Federation or Cloud Identity (via `frontend_path_configs` or tenant-level `auth_method`). Instance configuration updates targeting feature flags or migration settings (such as `instance_config.data_rbac_enabled` or `instance_config.sts_migration_enrolled`) are applied via `PATCH` using `update_mask`.  
— | `update_mask` | `google.protobuf.FieldMask` | **New field (partial update semantics):** A comma-separated list of fully qualified field paths indicating which fields to update (for example, `instance_config.data_rbac_enabled`).  
  
* * *

## Response payload field-by-field parity

The legacy endpoint returned only the updated authentication version enum, while the modern Chronicle API returns the complete updated `Instance` resource.

Legacy field (`SetAuthVersionResponse`) | Modern field (`Instance` response message) | Field type | Parity and migration notes  
---|---|---|---  
`auth_version` | `instance_config` / `frontend_path_configs` | `AuthVersion` (enum) $\rightarrow$ `Message` | **Restructured:** Rather than returning an isolated authentication version enum, the modern API returns the full modified `Instance` resource containing the updated `instance_config` flags and identity configurations.  
— | `name` | `string` | **New field:** Canonical resource name of the updated instance (`projects/{project}/locations/{location}/instances/{instance}`).  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the instance (`ACTIVE`, `SOFT_DELETED`, etc.).  
— | `display_name` | `string` | **New field:** Display name of the instance.  
— | `customer_code` | `string` | **New field:** Unique alphanumeric customer acronym/code.  
— | `secops_urls` | `repeated string` | **New field:** Fully qualified HTTPS URLs for navigating to the Google SecOps instance.  
— | `compliance_requirements` | `ComplianceRequirements` | **New field:** Active compliance certification requirements for the instance.  
— | `entitlement` | `Entitlement` | **New field:** Subscription licensing and entitlement details.  
  
* * *

## Key differences

  * **PATCH vs. POST partial update semantics:**
    * The legacy `SetAuthVersion` method was a specialized `POST` call that overwrote an isolated authentication version enum.
    * The modern `UpdateInstance` method uses standard HTTP `PATCH` semantics with a `google.protobuf.FieldMask`, enabling precise, partial updates to instance configuration flags without impacting unmasked fields.
  * **Identity architecture modernization:**
    * Legacy numbered auth versions (`AUTH_VERSION_1` through `AUTH_VERSION_4`) were used to track transitions between internal authentication backends.
    * Modern Chronicle instances natively integrate with Workforce Identity Federation and Cloud Identity via `frontend_path_configs` and tenant-level configurations, eliminating legacy numbered version management.
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used global partner tokens or API keys to update configurations across customer codes.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `UpdateInstance` is hosted under `InstanceService` and targets the tenant's project resource (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`), partners cannot use their own project credentials alone to modify tenant instance data.
    * To update tenant instances, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.admin` or custom role with `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`, `UpdateTenant`), which are managed in the partner's project using partner credentials.
  * **Exhaustive resource response:**
    * The legacy response returned only a confirmation of `auth_version`. The modern API returns the complete `Instance` resource, providing full operational visibility into active configuration parameters and lifecycle states.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
