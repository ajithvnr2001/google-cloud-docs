---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-ui-config/
title: UpdateInstance (UI config) APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:11.814443+00:00
---

# UpdateInstance (UI config) APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-ui-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateInstance (UI config) APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`SetUIState`**) to the modern Chronicle API ([**`UpdateInstance`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/patch)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/setuistate:state` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `UpdateInstance` is hosted outside `TenantService` (under `InstanceService`) and targets resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`). Partners cannot directly call `UpdateInstance` using their own credentials to update UI state or feature configurations on tenant instances. For a partner to update these resources, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.admin` or `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`SetUIState`) | Modern Chronicle API (`UpdateInstance`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Endpoint URI** | `/v1/partner/customer/setuistate:state` | `/v1alpha/{instance.name=projects/*/locations/*/instances/*}`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/instances.update`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers enabled or disabled user interface access using a dedicated RPC (`SetUIState`) specifying the customer code and a boolean flag (`state`). In the modern Chronicle API, UI accessibility is configured via the nested boolean feature flag `instance_config.secops_ui_enabled` on the `Instance` resource using a standard RESTful `PATCH` request with a `google.protobuf.FieldMask`.

Legacy field (`SetUIStateRequest`) | Modern field (`UpdateInstanceRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `instance.name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the target customer was identified globally by `customer_code`. In the modern API, the update targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`state` | `instance.instance_config.secops_ui_enabled` | `bool` | **Parity mapped:** Directly controls whether the user interface is accessible. Setting `state = true` in the legacy request corresponds to setting `secops_ui_enabled = true` in `instance.instance_config`. Setting `false` disables web UI access while API ingestion and search capabilities remain functional.  
— | `update_mask` | `google.protobuf.FieldMask` | **New field (partial update semantics):** A comma-separated list of field paths indicating which fields to update (for example, `instance_config.secops_ui_enabled` or `instance_config`).  
  
* * *

## Response payload field-by-field parity

The legacy endpoint returned only a boolean confirmation (`state`), while the modern Chronicle API returns the complete updated `Instance` resource.

Legacy field (`SetUIStateResponse`) | Modern field (`Instance` response message) | Field type | Parity and migration notes  
---|---|---|---  
`state` | `instance_config.secops_ui_enabled` | `bool` | **Restructured:** The modern response returns the complete updated state of the `Instance` resource containing the `instance_config.secops_ui_enabled` flag rather than an isolated boolean wrapper message.  
— | `name` | `string` | **New field:** Canonical resource name of the updated instance (`projects/{project}/locations/{location}/instances/{instance}`).  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the instance (`ACTIVE`, `CREATING`, `SOFT_DELETED`, etc.). Note that in the modern API, `state` denotes the instance lifecycle state, distinct from the UI access flag (`secops_ui_enabled`).  
— | `display_name` | `string` | **New field:** Display name of the instance.  
— | `customer_code` | `string` | **New field:** Unique alphanumeric customer acronym/code.  
— | `secops_urls` | `repeated string` | **New field:** Fully qualified HTTPS URLs for navigating to the Google SecOps instance.  
— | `instance_config` | `InstanceConfig` | **New field:** Complete feature flag configurations for the instance, including `data_rbac_enabled`, `triage_agent_enabled`, and `sts_migration_enrolled` alongside `secops_ui_enabled`.  
— | `compliance_requirements` | `ComplianceRequirements` | **New field:** Active compliance certification requirements for the instance.  
— | `entitlement` | `Entitlement` | **New field:** Subscription licensing and entitlement details.  
  
* * *

## Key differences

  * **PATCH vs. POST partial update semantics:**
    * The legacy `SetUIState` method used a custom verb action `POST` endpoint (`/v1/partner/customer/setuistate:state`) that passed the customer code and state in the body.
    * The modern `UpdateInstance` method uses standard HTTP `PATCH` semantics with a `google.protobuf.FieldMask` (such as `update_mask=instance_config.secops_ui_enabled`), ensuring atomic, safe partial updates that do not interfere with other instance properties.
  * **Disambiguation of "state":**
    * In the legacy API, the boolean field was ambiguously named `state` across both request and response messages to represent web UI enablement.
    * In the modern Chronicle API, the UI toggle is explicitly named `secops_ui_enabled` within the `instance_config` sub-message, whereas `state` on `Instance` is strictly reserved for the instance lifecycle state enum (`ACTIVE`, `SOFT_DELETED`, etc.).
  * **Consolidated feature flags in`instance_config`:**
    * Instead of isolated endpoints for individual toggles, the modern Chronicle API unifies UI accessibility with other tenant-level capability switches (such as `data_rbac_enabled` and `triage_agent_enabled`) under `Instance.instance_config`.
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used global partner tokens or API keys to toggle UI accessibility across customer codes.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `UpdateInstance` is hosted under `InstanceService` and targets the tenant's project resource (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`), partners cannot use their own project credentials alone to configure UI enablement or feature toggles on a tenant's instance.
    * To configure UI accessibility for a tenant instance, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.admin` or custom role with `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`, `UpdateTenant`), which are managed in the partner's project using partner credentials.
  * **Exhaustive resource response:**
    * The legacy response returned only `{ "state": true }`. The modern API returns the complete `Instance` resource, providing immediate visibility into web URLs (`secops_urls`), licensing entitlements, and overall instance health.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
