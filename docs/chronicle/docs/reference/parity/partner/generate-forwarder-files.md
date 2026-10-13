---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/generate-forwarder-files/
title: GenerateForwarderFiles APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:21.781500+00:00
---

# GenerateForwarderFiles APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/partner/generate-forwarder-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GenerateForwarderFiles APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory Partner API (**`GetForwarderConfigs`**) to the modern Chronicle API ([**`GenerateForwarderFiles`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.forwarders/generateForwarderFiles)).

> [!IMPORTANT] **Cross-project IAM delegation requirement:** In legacy Backstory, partners could use their own partner tokens or API keys to call `/v1/partner/customer/getforwarderconfigs` directly across all their customer codes.
> 
> In the modern Chronicle Dataplane API, `GenerateForwarderFiles` is hosted outside `TenantService` (under `ForwarderService`) and targets resources in the tenant's Google Cloud project (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}/forwarders/{forwarder}`). Partners cannot call `GenerateForwarderFiles` using their own credentials to generate forwarder configurations for a tenant. For a partner to generate forwarder files, the tenant must explicitly grant the required IAM role or permission (such as `roles/chronicle.admin` or `chronicle.googleapis.com/forwarders.generate`) to the partner's authentication principal (such as the partner's service account or Workload Identity Federation principal) in the tenant's Google Cloud project.
> 
> In contrast, `TenantService` methods (`CreateTenant`, `ListTenants`, `UpdateTenant`) are hosted within `TenantService` and scoped to the partner's own instance (`projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*`), allowing partners to call them directly using their own credentials on the partner project.

## Protocol and mapping overview

Feature | Legacy API (`GetForwarderConfigs`) | Modern Chronicle API (`GenerateForwarderFiles`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner access token or legacy API keys | `chronicle.googleapis.com/forwarders.generate`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers retrieved forwarder configurations for all forwarders belonging to a customer by providing the global `customer_code`. In the modern Chronicle API, forwarders are first-class Google Cloud resources, and configuration files are generated individually by targeting the specific forwarder resource name path.

Legacy field (`GetForwarderConfigsRequest`) | Modern field (`GenerateForwarderFilesRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_code` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** In the legacy API, forwarder configs were requested at the customer level using `customer_code`. In the modern API, forwarders are individual child resources under an instance. Callers must target a specific forwarder resource path: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}`. Forwarder resource names can be discovered using the modern `ListForwarders` API.  
  
* * *

## Response payload field-by-field parity

The legacy API returned a `Forwarder` response containing an array of raw binary configs partitioned by target OS platform. The modern Chronicle API returns a `GenerateForwarderFilesResponse` with separated, cross-platform configuration and authentication credential file payloads.

Legacy field (`Forwarder` response) | Modern field (`GenerateForwarderFilesResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`id` | `name` _(in request path)_ | `string` | **Parity mapped (resource identity):** In the legacy API, the forwarder identifier was returned in the response body (`id`). In the modern API, the forwarder identity is defined by the request resource path (`.../forwarders/{forwarder}`) rather than repeated in the response.  
`forwarder_configs[].platform` | — _(platform-agnostic)_ | `Platform` (enum) | **Unified architecture:** In the legacy API, separate configurations were generated for `WINDOWS` (1) and `LINUX` (2). The modern Chronicle forwarder architecture uses a unified, cross-platform collector agent where platform abstraction is handled automatically without platform-specific configurations.  
`forwarder_configs[].config` | `config` | `bytes` $\rightarrow$ `string` | **Parity mapped:** In the legacy API, configuration settings were returned as raw bytes. In the modern API, the forwarder runtime configuration file content is returned as a formatted UTF-8 string containing all collector and ingestion settings.  
— | `auth` | `string` | **New field (credential separation):** Returns the authentication credentials file content (such as client credentials or service account tokens) required by the forwarder to authenticate and transmit data to Google SecOps. Separating configuration (`config`) from credentials (`auth`) enables secure storage and rotation of credentials independently of collector configurations.  
  
* * *

## Key differences

  * **Resource-level granularity vs. customer-wide bundle:**
    * The legacy `GetForwarderConfigs` returned configurations for all forwarders associated with a customer code.
    * Modern `GenerateForwarderFiles` operates on a specific forwarder resource (`projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}`). Callers use `ListForwarders` to enumerate all forwarders under an instance before generating files.
  * **Separation of configuration and authentication:**
    * The legacy API bundled all settings and credentials together into platform-specific binary blobs (`config`).
    * The modern API strictly separates operational configuration (`config`) from sensitive credentials (`auth`), simplifying deployment workflows and credential rotation without modifying collector configuration settings.
  * **Unified cross-platform collector agent:**
    * Legacy clients had to specify or parse operating system variants (`Platform.WINDOWS` versus `Platform.LINUX`).
    * The modern Chronicle forwarder uses a unified configuration model that is platform-independent.
  * **Authorization modernization and cross-project delegation:**
    * In the legacy Backstory Partner API, partners used their own partner tokens or API keys to retrieve forwarder configurations across customer codes.
    * In the modern Chronicle API, access is governed strictly by Google Cloud IAM. Because `GenerateForwarderFiles` is part of `ForwarderService` and targets the tenant's forwarder resource (`projects/{tenant_project}/locations/{location}/instances/{tenant_instance}/forwarders/{forwarder}`), partners cannot use their own project credentials alone to generate tenant forwarder configurations.
    * To generate forwarder files for a tenant instance, the tenant must explicitly configure cross-project IAM delegation by granting the required role (such as `roles/chronicle.admin` or custom role with `chronicle.googleapis.com/forwarders.generate`) to the partner's authentication principal (service account or Workload Identity Federation principal) in the tenant's Google Cloud project. This contrasts with `TenantService` methods (`ListTenants`, `CreateTenant`), which are managed in the partner's project using partner credentials.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
