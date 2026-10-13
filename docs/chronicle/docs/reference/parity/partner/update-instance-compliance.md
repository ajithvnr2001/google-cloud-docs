---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-compliance/
title: UpdateInstance (Compliance) APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:09.638537+00:00
---

# UpdateInstance (Compliance) APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/update-instance-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateInstance (Compliance) APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`SetComplianceRequirements`**) to the modern Chronicle API ([**`UpdateInstance`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/patch)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/setcompliancerequirements` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `UpdateInstance` is hosted outside `TenantService` (under `InstanceService`) and targets resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`). Partners cannot directly call `UpdateInstance` using their own credentials to update compliance settings on tenant instances. For a partner to update these resources, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.admin` or `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`SetComplianceRequirements`) | Modern Chronicle API (`UpdateInstance`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Endpoint URI** | `/v1/partner/customer/setcompliancerequirements` | `/v1alpha/{instance.name=projects/*/locations/*/instances/*}`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/instances.update`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers updated compliance certifications using a dedicated RPC (`SetComplianceRequirements`) specifying the customer code and a list of certifications. In the modern Chronicle API, compliance settings are updated as nested properties on the `Instance` resource using a standard RESTful `PATCH` request with a `google.protobuf.FieldMask`.

Legacy field (`SetComplianceRequirementsRequest`) | Modern field (`UpdateInstanceRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `instance.name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the target customer was identified globally by `customer_code`. In the modern API, the update targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`compliance_certifications` | `instance.compliance_requirements.compliance_certifications` | `repeated ComplianceCertification` (enum) | **Parity mapped, expanded:** Maps directly to the repeated enum field nested under `compliance_requirements.compliance_certifications` within the `Instance` message. The legacy API supported 3 certifications (`FEDRAMP_MODERATE = 1`, `HIPAA = 2`, `PCI_DSS = 3`). The modern API supports these same values and adds support for extended compliance regimes (such as `FEDRAMP_HIGH = 4`, `IL4 = 5`, `IL5 = 6`, `CHRONICLE_CMEK_V1 = 7`, `DRZ_ADVANCED = 8`, and geographic data boundaries).  
— | `update_mask` | `google.protobuf.FieldMask` | **New field (partial update semantics):** A comma-separated list of field paths indicating which fields to update (for example, `compliance_requirements` or `compliance_requirements.compliance_certifications`).  
  
* * *

## Response payload field-by-field parity

The legacy endpoint returned only a confirmation list of compliance certifications, while the modern Chronicle API returns the complete updated `Instance` resource schema.

Legacy field (`SetComplianceRequirementsResponse`) | Modern field (`Instance` response message) | Field type | Parity and migration notes  
---|---|---|---  
`compliance_certifications` | `compliance_requirements.compliance_certifications` | `repeated ComplianceCertification` (enum) | **Restructured:** The modern response returns the complete updated state of the `Instance` resource containing the `compliance_requirements` block rather than an isolated enum wrapper list.  
— | `name` | `string` | **New field:** Canonical resource name of the updated instance (`projects/{project}/locations/{location}/instances/{instance}`).  
— | `state` | `State` (enum) | **New field:** Current lifecycle state of the instance (`ACTIVE`, `SOFT_DELETED`, etc.).  
— | `display_name` | `string` | **New field:** Display name of the instance.  
— | `customer_code` | `string` | **New field:** Unique alphanumeric customer acronym/code.  
— | `secops_urls` | `repeated string` | **New field:** Fully qualified HTTPS URLs for navigating to the Google SecOps instance.  
— | `instance_config` | `InstanceConfig` | **New field:** Active feature toggle configurations for the instance.  
— | `entitlement` | `Entitlement` | **New field:** Subscription licensing and entitlement details.  
  
* * *

## Key differences

  * **PATCH vs. POST partial update semantics:**
    * The legacy `SetComplianceRequirements` method was a specialized `POST` call that overwrote compliance certifications for a customer.
    * The modern `UpdateInstance` method uses standard HTTP `PATCH` semantics with a `google.protobuf.FieldMask`, enabling callers to update `compliance_requirements` without affecting other instance properties or feature flags.
  * **Expanded compliance regimes and data boundaries:**
    * The legacy API only recognized three certification types: `FEDRAMP_MODERATE`, `HIPAA`, and `PCI_DSS`.
    * The modern Chronicle API substantially expands this enum to support government impact levels (`FEDRAMP_HIGH`, `IL4`, `IL5`), customer-managed encryption keys (`CHRONICLE_CMEK_V1`), data residency (`DRZ_ADVANCED`), and regional data boundary profiles (e.g. EU, Australia, Canada, Israel, Japan, KSA).
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used global partner tokens or API keys to modify compliance requirements across customer codes.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `UpdateInstance` is hosted under `InstanceService` and targets the tenant's project resource (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}`), partners cannot use their own project credentials alone to modify tenant instance compliance settings.
    * To update compliance requirements on a tenant instance, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.admin` or custom role with `chronicle.googleapis.com/instances.update`) to the partner's authentication principal (service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`, `UpdateTenant`), which are managed in the partner's project using partner credentials.
  * **Exhaustive resource response:**
    * The legacy endpoint returned only a repeated list of compliance certifications. The modern API returns the complete `Instance` resource, providing comprehensive visibility into active configuration parameters and lifecycle status.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
