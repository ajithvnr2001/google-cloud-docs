---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-access-control/
title: Access control for tenants \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:38.199521+00:00
---

# Access control for tenants  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control for tenants

Identity Platform provides Admin APIs to manage your tenants, users, and authentication tokens. You can leverage [Identity and Access Management](https://docs.cloud.google.com/iam) to prevent unwanted access using these APIs.

## Granting, changing, and revoking access

Follow these steps to grant a user a role on a tenant resource:

  1. Open the Identity Platform Tenants page in the Google Cloud console.  
[Go to the tenants page](https://console.cloud.google.com/customer-identity/tenants)

  2. Select a tenant from the list.

  3. Switch to the **Permissions** tab in the info panel on the right.

![Access control pane](https://docs.cloud.google.com/static/identity-platform/img/multi-tenancy-access-control.png)

  4. Click **Add principal** to grant a user a new role, or use the list to modify or revoke access for an existing user.




To learn more about access control using IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs). To set the access control policy for a resource, use the [`setIamPolicy` method](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/setIamPolicy).

## API permissions

This table lists the role required to call each method in the Identity Platform API. The role should be assigned on the tenant resource.

Service | Method | Role  
---|---|---  
`google.cloud.identitytoolkit.v1.AccountManagementService` | GetOobCode | Editor  
SetAccountInfo | Editor  
UploadAccount | Editor  
DeleteAccount | Editor  
DownloadAccount | Viewer  
GetAccountInfo | Viewer  
QueryUserInfo | Viewer  
`google.cloud.identitytoolkit.v1.AuthenticationService` | SignUp | Editor  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService` | CreateDefaultSupportedIdpConfig | Editor  
CreateInboundSamlConfig | Editor  
CreateOAuthIdpConfig | Editor  
CreateOutboundSamlConfig | Editor  
DeleteDefaultSupportedIdpConfig | Editor  
DeleteInboundSamlConfig | Editor  
DeleteOAuthIdpConfig | Editor  
DeleteOutboundSamlConfig | Editor  
GetDefaultSupportedIdpConfig | Viewer  
GetInboundSamlConfig | Viewer  
GetOAuthIdpConfig | Viewer  
GetOutboundSamlConfig | Viewer  
ListDefaultSupportedIdpConfigs | Viewer  
ListInboundSamlConfigs | Viewer  
ListOAuthIdpConfigs | Viewer  
ListOutboundSamlConfigs | Viewer  
UpdateDefaultSupportedIdpConfig | Editor  
UpdateInboundSamlConfig | Editor  
UpdateOAuthIdpConfig | Editor  
UpdateOutboundSamlConfig | Editor  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService` | CreateTenant | Editor (on the parent project)  
DeleteTenant | Editor  
UpdateTenant | Editor  
GetTenant | Viewer  
ListTenants | Viewer (on the parent project)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
