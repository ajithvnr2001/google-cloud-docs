---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig/
title: TenantProjectConfig \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:42.392239+00:00
---

# TenantProjectConfig  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  TenantProjectConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TenantProjectPolicy
    * JSON representation
  * PolicyBinding
    * JSON representation
  * BillingConfig
    * JSON representation
  * ServiceAccountConfig
    * JSON representation



This structure defines a tenant project to be added to the specified tenancy unit and its initial configuration and properties. A project lien is created for the tenant project to prevent the tenant project from being deleted accidentally. The lien is deleted as part of tenant project removal.

JSON representation  
---  
      
    
    {
      "folder": string,
      "tenantProjectPolicy": {
        object ([TenantProjectPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#TenantProjectPolicy))
      },
      "labels": {
        string: string,
        ...
      },
      "services": [
        string
      ],
      "billingConfig": {
        object ([BillingConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#BillingConfig))
      },
      "serviceAccountConfig": {
        object ([ServiceAccountConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#ServiceAccountConfig))
      }
    }  
  
Fields  
---  
`folder` |  `string` Folder where project in this tenancy unit must be located This folder must have been previously created with the required permissions for the caller to create and configure a project in it. Valid folder resource names have the format `folders/{folder_number}` (for example, `folders/123456`).  
`tenantProjectPolicy` |  `object (`[TenantProjectPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#TenantProjectPolicy)`)` Describes ownership and policies for the new tenant project. Required.  
`labels` |  `map (key: string, value: string)` Labels that are applied to this project.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`services[]` |  `string` Google Cloud API names of services that are activated on this project during provisioning. If any of these services can't be activated, the request fails. For example: 'compute.googleapis.com','cloudfunctions.googleapis.com'  
`billingConfig` |  `object (`[BillingConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#BillingConfig)`)` Billing account properties. The billing account must be specified.  
`serviceAccountConfig` |  `object (`[ServiceAccountConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#ServiceAccountConfig)`)` Configuration for the IAM service account on the tenant project.  
  
## TenantProjectPolicy

Describes policy settings that need to be applied to a newly created tenant project.

JSON representation  
---  
      
    
    {
      "policyBindings": [
        {
          object ([PolicyBinding](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#PolicyBinding))
        }
      ]
    }  
  
Fields  
---  
`policyBindings[]` |  `object (`[PolicyBinding](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig#PolicyBinding)`)` Policy bindings to be applied to the tenant project, in addition to the 'roles/owner' role granted to the Service Consumer Management service account. At least one binding must have the role `roles/owner`. Among the list of members for `roles/owner`, at least one of them must be either the `user` or `group` type.  
  
## PolicyBinding

Translates to IAM Policy bindings (without auditing at this level)

JSON representation  
---  
      
    
    {
      "role": string,
      "members": [
        string
      ]
    }  
  
Fields  
---  
`role` |  `string` Role. (<https://cloud.google.com/iam/docs/understanding-roles>) For example, `roles/viewer`, `roles/editor`, or `roles/owner`.  
`members[]` |  `string` Uses the same format as in IAM policy. `member` must include both a prefix and ID. For example, `user:{emailId}`, `serviceAccount:{emailId}`, `group:{emailId}`.  
  
## BillingConfig

Describes the billing configuration for a new tenant project.

JSON representation  
---  
      
    
    {
      "billingAccount": string
    }  
  
Fields  
---  
`billingAccount` |  `string` Name of the billing account. For example `billingAccounts/012345-567890-ABCDEF`.  
  
## ServiceAccountConfig

Describes the service account configuration for the tenant project.

JSON representation  
---  
      
    
    {
      "accountId": string,
      "tenantProjectRoles": [
        string
      ]
    }  
  
Fields  
---  
`accountId` |  `string` ID of the IAM service account to be created in tenant project. The email format of the service account is "@.iam.gserviceaccount.com". This account ID must be unique within tenant project and service producers have to guarantee it. The ID must be 6-30 characters long, and match the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])`.  
`tenantProjectRoles[]` |  `string` Roles for the associated service account for the tenant project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
