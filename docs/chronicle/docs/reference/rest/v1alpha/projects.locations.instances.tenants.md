---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants
title: REST Resource: projects.locations.instances.tenants \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:28.223608+00:00
---

# REST Resource: projects.locations.instances.tenants  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.tenants Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Tenant
    * JSON representation
  * AuthMethod
  * ProvisioningFlow
  * Methods



## Resource: Tenant

Tenant represents a tenant of a partner.

JSON representation  
---  
      
    
    {
      "name": string,
      "tenantGcpProject": string,
      "state": enum ([State](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/State)),
      "displayName": string,
      "customerCode": string,
      "retentionDuration": enum ([RetentionDuration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RetentionDuration)),
      "authMethod": enum ([AuthMethod](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants#AuthMethod)),
      "frontendPathConfigs": [
        {
          object ([FrontendPathConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FrontendPathConfig))
        }
      ],
      "provisioningFlow": enum ([ProvisioningFlow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants#ProvisioningFlow)),
      "billingAccount": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of this tenant. Format: projects/{project}/locations/{location}/instances/{instance}/tenants/{tenantId}  
`tenantGcpProject` |  `string` Required. Project name of the tenant's BYOP project. Format: projects/{projectId} or projects/{projectNumber}  
`state` |  `enum (`[State](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/State)`)` Output only. The state of the Tenant.  
`displayName` |  `string` Required. The display name of the tenant.  
`customerCode` |  `string` Required. Customer code associated with the tenant.  
`retentionDuration` |  `enum (`[RetentionDuration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RetentionDuration)`)` Required. Customer's contractually agreed data retention duration.  
`authMethod` |  `enum (`[AuthMethod](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants#AuthMethod)`)` Required. Auth Method used by tenant  
`frontendPathConfigs[]` |  `object (`[FrontendPathConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/FrontendPathConfig)`)` Required. Configuration for the tenant's frontend paths.  
`provisioningFlow` |  `enum (`[ProvisioningFlow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants#ProvisioningFlow)`)` Optional. The provisioning flow of the tenant.  
`billingAccount` |  `string` Required. The billing account ID of the customer.  
  
## AuthMethod

Auth Method of the Tenant.

Enums  
---  
`AUTH_METHOD_UNSPECIFIED` | The default value.  
`WORKFORCE_IDENTITY_FEDERATION` | Workforce Identity Federation  
`CLOUD_IDENTITY` | Cloud Identity  
  
## ProvisioningFlow

Provisioning flow.

Enums  
---  
`PROVISIONING_FLOW_UNSPECIFIED` | Unspecified provisioning flow.  
`BACKSTORY_API_PARITY` | Provisioning flow triggered to have parity with Backstory API.  
`TENANT_ATTRIBUTION` | Provisioning flow triggered with tenant attribution.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants/create)`

|  Provisions a new tenant under the specified partner/MSSP parent resource.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants/list)`

|  Allow partners to list their tenants.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.tenants/patch)`

|  UpdateTenant allows partners to update their tenants.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
