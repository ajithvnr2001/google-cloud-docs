---
url: https://docs.cloud.google.com/chronicle/docs/reference/migrate-from-legacy-api-to-chronicle-api/
title: Migrate from legacy SIEM API to Chronicle API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:01.574476+00:00
---

# Migrate from legacy SIEM API to Chronicle API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/migrate-from-legacy-api-to-chronicle-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from legacy SIEM API to Chronicle API

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** Legacy APIs can have a security and performance impact. The legacy SIEM APIs—[Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#backstory_api) (including [Customer Management API](https://docs.cloud.google.com/chronicle/docs/reference/customer-management-api)) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#ingestion_api)—will be deprecated and fully non-functional by July 20, 2027. Continued use of these APIs can lead to performance issues or unexpected behavior within the product. You must migrate all legacy API programmatic calls to the modern [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#chronicle_api) immediately to ensure platform stability, security, and performance.

This document helps you manage applications that call any of the legacy SIEM APIs ([Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#backstory_api) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#ingestion_api)). It describes the steps you must follow to set up programmatic access and update any references from the legacy SIEM API endpoints to the modern [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) endpoints.

For a quick overview of the migration process, watch the embedded video.

The Chronicle API surface introduces several improvements designed to streamline your development process and align with Google Cloud API standards for improved reliability, security, performance, and stronger integration with Cloud Audit Logs, Cloud Monitoring, Cloud Identity, and Identity and Access Management (IAM). It also addresses many of the limitations and complexities of the legacy APIs.

## What is changing

All programmatic requests to legacy [Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#backstory_api) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#ingestion_api) endpoints must transition to the modern [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest). If your organization uses custom integrations, automation scripts, or third-party tools that make calls to these legacy endpoints, you must update those workloads to use modern endpoints and authentication flows before July 20, 2027. In addition, if your organization uses Google Security Operations SOAR, you must update your SOAR integrations and connectors (such as the Google Chronicle integration) to use the Chronicle API. For details, see Migrate SOAR integrations.

## What isn't changing

Actions performed directly in the Google Security Operations user interface (UI) already invoke the modern [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest). If your organization only interacts with Google SecOps through the UI, or if your integrations already call [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) endpoints, you aren't required to take any action.

## Key changes and enhancements

The following table highlights the major differences between the legacy SIEM API and the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest):

Feature area | Legacy SIEM API | Chronicle API | Details  
---|---|---|---  
Credential management | Manual process involving Google representatives | Self-service management of service accounts, credentials, and IAM permissions | Self-service credential and IAM management simplify onboarding and remove dependence on manual support requests.  
Compliance standards | Limited support | Built-in support for Data Residency controls, VPC Service Controls, Access Transparency, CMEK, and FedRAMP | Modern built-in infrastructure controls meet industry compliance and regulatory standards.  
Logging and auditing | Legacy audit streams | Cloud Audit Logs integrated into your Google Cloud project | Direct integration provides centralized audit trails and monitoring.  
Authentication | API token and service account credentials | OAuth 2.0 with support for modern authentication methods, including Workload Identity and service accounts as described in [Authentication for Google Cloud APIs and services](https://docs.cloud.google.com/docs/authentication) | These modern authentication methods provide enhanced security and standardize the credential flow.  
Data models and API design | Flat, proprietary structures | Resource-oriented design, RESTful architecture, and standardized naming following [AIPs](https://google.aip.dev/) | This modern design improves data consistency, makes the API more intuitive, and simplifies object manipulation.  
Endpoint naming | Inconsistent | RESTful and standardized | Consistent naming makes the API more intuitive and easier to integrate.  
Ecosystem | Very limited | Integration with MCP, Terraform, client libraries, and SDKs | Broad compatibility with modern cloud tooling and automation frameworks.  
Partner authorization | Partner token or API key used directly across customer codes | Cross-project IAM delegation for tenant resources; partner-scoped TenantService methods | TenantService methods run in the partner project. All other tenant APIs require cross-project IAM delegation granted by the tenant in the tenant project.  
  
### Partner authorization

For multi-tenant partner workflows, authorization in the Chronicle API depends on resource ownership. The project that hosts a resource determines which credentials and IAM permissions a partner needs. Scoping tenant operations to tenant-delegated credentials aligns with the core security principle that partners shouldn't be able to access, retrieve, or modify tenant data without explicit permission granted by the tenant. The following table compares partner authorization in the legacy Backstory API and the Chronicle API:

API | Methods | Resource scope | Authorization  
---|---|---|---  
Legacy Backstory API | `/v1/partner/customer/*` endpoints | All of the partner's customer codes | Partners call these endpoints directly with their own partner tokens or API keys.  
Chronicle API: `TenantService` | `CreateTenant`, `ListTenants`, and `UpdateTenant` | Partner's instance: `projects/{partner_project}/locations/{location}/instances/{partner_instance}/tenants/*` | Partners call these methods directly with their own service accounts or credentials that have `chronicle.googleapis.com/tenants.*` permissions in the partner project.  
Chronicle API: other services, such as `InstanceService` and `ForwarderService` | `GetInstance`, `UpdateInstance`, `GenerateForwarderFiles`, and other tenant-scoped methods | Tenant's instance: `projects/{tenant_project}/locations/{location}/instances/{tenant_instance}/...` | Partner credentials alone can't access or modify tenant data. The tenant administrator must grant IAM roles, such as `roles/chronicle.admin`, `roles/chronicle.viewer`, or a custom role, to the partner's service account or Workload Identity Federation principal in the tenant's Google Cloud project.  
  
## Deprecation schedule

The legacy SIEM API is scheduled to be shut down on July 20, 2027. We recommend completing your migration before this date to avoid any service interruptions:

  * Starting **October 26, 2026** , you can no longer call legacy APIs ([Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#backstory_api) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#ingestion_api)) from new instances.
  * By **July 20, 2027** , you must migrate all existing instances to the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest), as the legacy APIs will no longer be available.



## Before you begin

Before migrating to the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest), make sure you complete the following:

**Note:** If you use a Managed Instance, your Managed Security Service Provider (MSSP) might have completed some of these steps for you.

  * **Deploy on modern SIEM infrastructure:** Make sure the instance is deployed on your or your MSSP partner's Google Cloud project using the modern SIEM infrastructure. For detailed instructions, see [SIEM migration overview](https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra).
  * **Enable the Chronicle API:** In the Google Cloud console, navigate to the project hosting your instance and enable the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) (`chronicle.googleapis.com`). For details, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).
  * **Identify SOAR integrations:** If your environment connects Google SecOps SOAR to Google Security Operations SIEM, verify your existing connectors. For details, see Migrate SOAR integrations.



## Migrate SOAR integrations

If your organization connects Google SecOps SOAR to Google SecOps SIEM, you must migrate your SOAR integrations and connectors (such as the Google Chronicle integration) to use the Chronicle API.

For detailed instructions about upgrading the Google Chronicle integration and connectors to use the Chronicle API—including locating your environment's Chronicle API root and configuring authentication credentials—see [Migration from Backstory API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle#migration_from_backstory_api_to_chronicle_api).

## Migrate to the Chronicle API

Migrate your custom scripts and integrations from the legacy APIs to the Chronicle API by completing the following steps:

  1. **Audit API usage:** Identify all custom scripts and integrations in your environment that invoke legacy endpoints.
  2. **Set up authentication and authorization:** Configure your environment to authenticate and authorize requests to the Chronicle API.
  3. **Map endpoints and update URLs:** Replace legacy endpoints with their modern regional equivalents.
  4. **Update API logic:** Adjust your request payloads and response handling to match the modern API's data models.
  5. **Test your integration:** Validate the changes in a staging environment before deploying to production.



### Audit API usage

Audit your environment to identify custom scripts or integrations invoking `backstory.googleapis.com` or `malachiteingestion-pa.googleapis.com`. You can identify these integrations by reviewing your codebase, automation scripts, and third-party tools. If your organization also uses Google SecOps SOAR, see Migrate SOAR integrations.

### Set up authentication and authorization

Configure your environment to authenticate and authorize requests to the Chronicle API:

  1. **Choose an authentication method:** Choose how your workloads authenticate to the Chronicle API using one of the listed methods. We recommend using [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) for better security, as it avoids managing and storing long-lived service account keys. For advanced authentication scenarios (such as service account impersonation), see [Authenticate to the Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/authentication). 
     * **Workload Identity Federation (recommended):** Set up [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) to allow workloads running outside of Google Cloud to authenticate using external identities.
     * **Service Accounts:** If you must use service accounts, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) in your Google Cloud project and [generate and download a private key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) in JSON format. Keep this key secure.
  2. **Grant IAM permissions:** Grant the required IAM permissions to the identity (either the service account or the external identity principal) used for authentication. See [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table) to find the specific IAM permissions required for the modern endpoints replacing your legacy calls. 
     * **Custom role (recommended):** [Create a custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) with the required permissions, and [grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) the custom role to the service account or the external identity principal.
     * **Predefined role:** [Grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) a [Google SecOps predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle) to the service account or the external identity principal. This will likely grant more access than needed for a specific automation.
     * **Multi-tenant partner delegation:** If you are an MSSP or partner managing tenant resources outside `TenantService` (such as `GetInstance`, `UpdateInstance`, or `GenerateForwarderFiles`), the tenant administrator must explicitly grant your service account or Workload Identity Federation principal, the required IAM roles in the tenant's Google Cloud project.
  3. **Set the credentials environment variable:** Configure your runtime environment to use the credentials with Application Default Credentials (ADC) by setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. This variable should point to either the downloaded service account key JSON file or the [Workload Identity Federation credential configuration file](https://docs.cloud.google.com/iam/docs/authenticate-with-auth-libraries#authenticate-standard). The [Google Cloud client libraries](https://docs.cloud.google.com/chronicle/docs/libraries) automatically detect this variable to authenticate requests:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
         

  4. **Update OAuth scopes:** Update the scope string if your legacy integration scripts explicitly requested OAuth scopes for token generation. The legacy scope doesn't grant access to the modern API surface:

     * **Legacy Backstory scope:** `https://www.googleapis.com/auth/chronicle-backstory`
     * **Chronicle scope:** `https://www.googleapis.com/auth/chronicle` (or the broader `https://www.googleapis.com/auth/cloud-platform` scope).



### Map endpoints and update URLs

Familiarize yourself with the Chronicle API surface, map your legacy calls, and update the service endpoints in your application.

#### Review reference documentation

Familiarize yourself with the comprehensive documentation for the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest).

#### Map endpoints to the Chronicle API

Identify the corresponding modern endpoints for each of the legacy API calls your application makes. Similarly, map your existing data models to the modern structures, accounting for any schema changes or additional fields. For details across all SIEM endpoints, see [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table). If your workflow also interacts with SOAR endpoints, see the [SOAR API endpoint mapping table](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/endpoint-mapping-table).

#### Update the service endpoint

Update the base URL of your API calls to point to the correct regional service endpoint. The [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) is a regional service, so you must call the regional service endpoint that matches the location of your Google SecOps instance.

All modern endpoints use a consistent prefix, making the final endpoint address predictable. The following example shows the modern endpoint URL structure:
    
    
    [api_version]/projects/[project_id]/locations/[location]/instances/[instance_id]/...
    

This structure makes the final address to the endpoint as follows:
    
    
    https://[service_endpoint]/[api_version]/projects/[project_id]/locations/[location]/instances/[instance_id]/...
    

Where:

  * `service_endpoint`: A regional service address.
  * `api_version`: The API version to query. Can be `v1alpha`, `v1beta`, or `v1`.
  * `project_id`: Your project ID (same project as you defined for your IAM permissions).
  * `location`: The location of your project (region); same as the regional endpoints.
  * `instance_id`: Your Google SecOps SIEM customer ID.



Regional addresses:

  * africa-south1: `https://africa-south1-chronicle.googleapis.com` or `https://chronicle.africa-south1.rep.googleapis.com`
  * asia-northeast1: `https://asia-northeast1-chronicle.googleapis.com` or `https://chronicle.asia-northeast1.rep.googleapis.com`
  * asia-south1: `https://asia-south1-chronicle.googleapis.com` or `https://chronicle.asia-south1.rep.googleapis.com`
  * asia-southeast1: `https://asia-southeast1-chronicle.googleapis.com` or `https://chronicle.asia-southeast1.rep.googleapis.com`
  * asia-southeast2: `https://asia-southeast2-chronicle.googleapis.com` or `https://chronicle.asia-southeast2.rep.googleapis.com`
  * australia-southeast1: `https://australia-southeast1-chronicle.googleapis.com` or `https://chronicle.australia-southeast1.rep.googleapis.com`
  * europe-west12: `https://europe-west12-chronicle.googleapis.com` or `https://chronicle.europe-west12.rep.googleapis.com`
  * europe-west2: `https://europe-west2-chronicle.googleapis.com` or `https://chronicle.europe-west2.rep.googleapis.com`
  * europe-west3: `https://europe-west3-chronicle.googleapis.com` or `https://chronicle.europe-west3.rep.googleapis.com`
  * europe-west6: `https://europe-west6-chronicle.googleapis.com` or `https://chronicle.europe-west6.rep.googleapis.com`
  * europe-west9: `https://europe-west9-chronicle.googleapis.com` or `https://chronicle.europe-west9.rep.googleapis.com`
  * me-central1: `https://me-central1-chronicle.googleapis.com` or `https://chronicle.me-central1.rep.googleapis.com`
  * me-central2: `https://me-central2-chronicle.googleapis.com` or `https://chronicle.me-central2.rep.googleapis.com`
  * me-west1: `https://me-west1-chronicle.googleapis.com` or `https://chronicle.me-west1.rep.googleapis.com`
  * northamerica-northeast2: `https://northamerica-northeast2-chronicle.googleapis.com` or `https://chronicle.northamerica-northeast2.rep.googleapis.com`
  * southamerica-east1: `https://southamerica-east1-chronicle.googleapis.com` or `https://chronicle.southamerica-east1.rep.googleapis.com`
  * United States (`us`): `https://us-chronicle.googleapis.com` or `https://chronicle.us.rep.googleapis.com`
  * Europe (`eu`): `https://eu-chronicle.googleapis.com` or `https://chronicle.eu.rep.googleapis.com`



For a comprehensive list of all supported endpoints, see the official reference in the Chronicle API [Service endpoint](https://docs.cloud.google.com/chronicle/docs/reference/rest#service-endpoint) documentation.

For example, to list all detection rules for an instance in the `us` location, send the following request:
    
    
    GET
      https://us-chronicle.googleapis.com/v1alpha/projects/my-project-name-or-id/locations/us/instances/408bfb7b-5746-4a50-885a-50a323023529/rules
    

Similarly, to query SOAR resources such as Cases using the regional endpoint (`rep`) alias, send the following request:
    
    
    GET
      https://chronicle.us.rep.googleapis.com/v1alpha/projects/my-project-name-or-id/locations/us/instances/408bfb7b-5746-4a50-885a-50a323023529/cases
    

### Update API logic

Review the [Chronicle API REST reference](https://docs.cloud.google.com/chronicle/docs/reference/rest) to identify and implement changes to field names and data structures in your application. While some legacy endpoints might remain similar, you must update your integrations to match the latest data models and endpoint structures.

#### Use Google Cloud client libraries

Simplify your integration to automatically handle authentication, token refreshing, and transport details. We recommend using the official Google Cloud client libraries for doing so. Chronicle API support is available across eight programming languages, including Python, Go, Java, Node.js, and C#. For installation and usage details, see [Client libraries and SDK](https://docs.cloud.google.com/chronicle/docs/libraries).

### Test your integration

Test your updated application in a staging environment before deploying to production:

  1. **Create a test plan:** Define test cases that cover all migrated functionalities.
  2. **Execute tests:** Run automated and manual tests to confirm accuracy and validity.
  3. **Monitor performance:** Assess the performance of your application with the modern API.



## Troubleshoot

This section describes how to resolve common errors you might encounter during the migration.

### HTTP 403 Forbidden or PERMISSION_DENIED

If your API calls return an `HTTP 403 Forbidden` or `PERMISSION_DENIED` error, verify the following:

  * **Authentication method and principal:** Ensure you are using the correct credentials. 
    * If using Workload Identity Federation, verify that the external identity principal matches the principal bound to the IAM roles in your project.
    * If using a service account, verify that the correct service account is being used and that it hasn't been disabled. Don't use legacy service accounts (often containing `bk` or `malachite-cx` in their email address) for modern Chronicle API endpoints.
  * **IAM roles:** Check that the service account or external identity principal has been granted the required predefined or custom IAM roles (such as `Chronicle API Viewer` or `Chronicle API Editor`) in your Google Cloud project. For granular endpoint permissions, see [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table).



### HTTP 401 Unauthorized or UNAUTHENTICATED

If your API calls fail with `HTTP 401 Unauthorized` or `UNAUTHENTICATED`, check the following:

  * **OAuth scopes:** Verify that your custom scripts are requesting the modern scope: `https://www.googleapis.com/auth/chronicle` (or the broader `https://www.googleapis.com/auth/cloud-platform` scope). The legacy scope (`https://www.googleapis.com/auth/chronicle-backstory`) doesn't grant access to the modern Chronicle API.
  * **Environment variable:** Confirm that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set and points to the correct JSON key file or Workload Identity Federation configuration file in your runtime environment.



### HTTP 404 Not Found or regional mismatches

If your API calls return an `HTTP 404 Not Found` or fail to connect, check your regional endpoints:

  * **Regional endpoint:** The Chronicle API is a regional service. Verify that you are calling the endpoint that matches the region of your Google SecOps instance (for example, `https://europe-west3-chronicle.googleapis.com` for an instance in Frankfurt). Sending requests to a different region will result in errors. For a full list of regional addresses, see Update the service endpoint or the official [Service endpoint reference](https://docs.cloud.google.com/chronicle/docs/reference/rest#service-endpoint).



## What's next

  * [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table)
  * [Authenticate to the Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/authentication)
  * [Chronicle API REST reference](https://docs.cloud.google.com/chronicle/docs/reference/rest)
  * [Client libraries and SDK](https://docs.cloud.google.com/chronicle/docs/libraries)
  * [Chronicle API ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods)
  * [Upgrade Google Chronicle integration in SOAR](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle#migration_from_backstory_api_to_chronicle_api)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
