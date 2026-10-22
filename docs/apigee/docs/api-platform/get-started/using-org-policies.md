---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies/
title: Using organization policy constraints in Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:35.716464+00:00
---

# Using organization policy constraints in Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using organization policy constraints in Apigee Stay organized with collections  Save and categorize content based on your preferences. 

This page describes using [ organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) with Apigee. 

Not every feature in Apigee utilizes CMEK for encryption of sensitive data. To ensure that data that requires encryption with CMEK doesn't unknowingly use features that aren't CMEK protected, those features will be disabled for CMEK-constrained projects until they are compliant. Only new usages of the features will be disabled (creating new resources or enabling an add-on). Features and resources that are already in use will remain available and editable, but not protected. 

Eval orgs creation are blocked by both the [ gcloud alpha apigee organizations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision) API and the [ eval provisioning wizard](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs). When trying to view the eval provisioning wizard, you will see the message: **Apigee evaluation is not available**. 

For more information on the features that are disabled for CMEK-constrained projects, see [ Organization policy constraints](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts#organization-policy-constraints).

## Terms

The following terms are used in this topic:

Term | Definition  
---|---  
CMEK | Customer-managed encryption key. See [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) for a detailed description.  
organization policy constraints | A constraint is a particular type of restriction against a Google Cloud service or a list of Google Cloud services. With regards to CMEK, there are [ two relevant constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints): 

  * `constraints/gcp.restrictNonCmekServices`
  * `constraints/gcp.restrictCmekCryptoKeyProjects`

  
Enforcement | A guarantee that Apigee's backend systems will adhere to a project's constraint (CMEK constraints in this case)   
Pre-validation | UI behaviors that guide you in selecting valid configurations in Apigee in accordance with CMEK org policies and do not expose features which are not compliant   
Resources | Apigee resources such as [ organizations](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure) and [ instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances)  
  
## How to restrict non-CMEK services

This section describes how to restrict non-CMEK services.

  1. Meet the prerequisites.
  2. [ Select your Project](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/wizard-select-project) in the Google Cloud console.
  3. Create a new organization policy constraint.
  4. Provision Apigee.



### Prerequisites

You must:

  * Have the [ Organization policy administrator role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles). To get the permissions that you need to manage organization policies, ask your administrator to grant you the [ Organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Have the prerequisites described in [ Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). 
  * Use a paid organization (Subscription or Pay-as-you-go).
  * Use [ data residency.](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts)



### Open project 

  1. In the Google Cloud console, go to the **Dashboard** page.

[Go to Dashboard](https://console.cloud.google.com/home/dashboard)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 



### Create an organization policy constraint

Organization policies are defined by the values set for each constraint. They are either configured at the level of this resource, inherited from the parent resource, or set to the Google-managed default behavior. In this case, you will be creating a constraint that requires CMEK and will be applied to the project and all resources that inherit from the project. 

To ensure that customer-managed encryption keys are always used when encrypting your data in Apigee, create the following organization policy constraint: 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 
  3. In the **Filter** box, enter: 
         
         constraints/gcp.restrictNonCmekServices

  4. Click more_vert **More** , **Edit policy**. If **Edit** is disabled, you don't have the required permissions and need to ask your administrator to grant you the [ Organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. See Prerequisites for more information. 
  5. For **Policy source** , select **Override parent's policy**. This resource will have a unique policy. In the next step you will specify how the parent policy rules are handled. 
  6. For **Policy enforcement** , select one of the following: 
     * **Replace**. This option ignores the parent's policy and uses these rules. 
     * **Merge with parent**. This option adds rules in addition to the ones the parent resource has set. 

See [ Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) for an explanation of organization policy inheritance.

  7. Click **Add a rule**.
  8. For **Policy values** , select **Custom**.
  9. For **Policy type** , select **Deny**.
  10. For **Custom values** , enter: 
         
         apigee.googleapis.com

  11. Click **Done**.
  12. Click **Set policy**. The **Policy details** page is displayed.



Once you have configured the policy and selected a project that inherits/uses the policy, you are ready to provision Apigee. Note that Apigee resources that were created before configuring CMEK organization policies will not be guaranteed to be compliant; only new resources that are created after the policy is in place will adhere to the CMEK constraints.

See also:

  * [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [CMEK-specific examples](https://docs.cloud.google.com/kms/docs/cmek-org-policy#configuration-examples)



### Provision Apigee

Provisioning Apigee where you have organization policy constraints consists of the same steps as provisioning Apigee where you don't have organization policy constraints; however, the UI prevents you from making selections that are not supported.

This section describes where the UI guides you on making selections.

  1. In the Google Cloud console, go to the **Apigee** page.

[Go to Apigee](https://console.cloud.google.com/apigee/welcome)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 
  3. On the **Welcome to Apigee API management page** , **Setup using defaults** is disabled since you need to explicitly select CMEKs. Click **Customize your setup**.
  4. **Enable APIs** : Enable required APIs as described in [ Step 1: Enable required APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis). 
  5. **Set up networking** : Set up networking as described in [ Step 2: Set up networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking). 
  6. **Configure hosting and encryption** :

[ User journey D: Customer-managed encryption, with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting#cm-dr) is the only relevant user journey for organization policy constraints that restrict non-CMEK services. 

     1. Click edit **Edit** to open the **Hosting and encryption keys** panel.
     2. In the **Encryption type** section, **Google-managed encryption key** is disabled and **Customer-managed encryption key** is enabled and cannot be disabled.
     3. Click **Next**.
     4. In the **Control Plane** section, **Enable data residency** is enabled and cannot be disabled. 
     5. Continue configuring hosting and encryption as described in step 3.b. of [ User journey D: Customer-managed encryption, with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting#cm-dr). 
  7. **Customize access routing** : Customize access routing as described in [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing). 



## How to restrict CMEK crypto key projects

This section describes how to restrict CMEK crypto key projects.

You can restrict which projects can provide encryption keys through another organization policy constraint: `constraints/gcp.restrictCmekCryptoKeyProjects` With this constraint, you allowlist projects from which encryption keys can be used. 

Anywhere you can select a CMEK, which is currently while provisioning Apigee or creating an Apigee instance, this constraint is enforced. 

If the current project selected in the Google Cloud console is not allowlisted in the `restrictCmekCryptoKeyProjects` constraint, then you will not be able to select any keys from the encryption key select box. Instead, you will need to use a key from a project that is allowlisted. 

### Prerequisites

You must:

  * Have the [ Organization policy administrator role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles). To get the permissions that you need to manage organization policies, ask your administrator to grant you the [ Organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Have the prerequisites described in [ Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). 
  * Use a paid organization (Subscription or Pay-as-you-go)
  * Use [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts)
  * Provision using the Google Cloud console (Subscription or Pay-as-you-go).
  * Know which project contains the keys you want to use.



### Open project

  1. In the Google Cloud console, go to the **Dashboard** page.

[Go to Dashboard](https://console.cloud.google.com/home/dashboard)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 



### Create an organization policy constraint

Organization policies are defined by the values set for each constraint. They are either configured at the level of this resource, inherited from the parent resource, or set to the Google-managed default behavior. In this case, you will be creating a constraint that allows keys only from allowlisted projects. This constraint will be applied to the project and all resources that inherit from the project. 

To ensure that customer-managed encryption keys are used only from specific projects, add them to an allowlist: 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 
  3. In the **Filter** box, enter: 
         
         restrictCmekCryptoKeyProjects

  4. Click more_vert **More** , **Edit policy**. If **Edit** is disabled, you don't have the required permissions and need to ask your administrator to grant you the [ Organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. See Prerequisites for more information. 
  5. For **Policy source** , select **Override parent's policy**. This resource will have a unique policy. In the next step you will specify how the parent policy rules are handled. 
  6. For **Policy enforcement** , select one of the following: 
     * **Replace**. This option ignores the parent's policy and uses these rules. 
     * **Merge with parent**. This option adds rules in addition to the ones the parent resource has set. 

See [ Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) for an explanation of organization policy inheritance.

  7. Click **Add a rule**.
  8. For **Policy values** , select **Custom**.
  9. For **Policy type** , select **Allow**.
  10. For **Custom values** , enter: 
         
         projects/PROJECT_ID

Replace PROJECT_ID with the project ID where the Cloud KMS keys you want to use are located. For example, `my-kms-project`. 

**Tip:**

You can also specify projects directly: `projects/apigee-cmek10`, or that all projects under a folder or organization are allowlisted: `under:organizations/my-org-id`.

See [ Constraints supported by multiple Google Cloud services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-supported-by-multiple-google-cloud-services) for more information.

  11. Click **Done**.
  12. Click **Set policy**. The **Policy details** page is displayed.



Once you have configured the policy and selected a project that inherits/uses the policy, you are ready to provision Apigee. Note that Apigee resources that were created before configuring CMEK organization policies will not be guaranteed to be compliant; only new resources that are created after the policy is in place will adhere to the CMEK constraints.

See also:

  * [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [CMEK-specific examples](https://docs.cloud.google.com/kms/docs/cmek-org-policy#configuration-examples)



### Provision Apigee

Provisioning Apigee where you have organization policy constraints consists of the same steps as provisioning Apigee where you don't have organization policy constraints; however, the UI prevents you from making selections that are not supported.

This section describes where the UI guides you on making selections.

  1. In the Google Cloud console, go to the **Apigee** page.

[Go to Apigee](https://console.cloud.google.com/apigee/welcome)

  2. Select your project in the Google Cloud console drop-down list if it is not already selected. 
  3. On the **Welcome to Apigee API management page** , Click **Customize your setup**.
  4. **Enable APIs** : Enable required APIs as described in [ Step 1: Enable required APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis). 
  5. **Set up networking** : Set up networking as described in [ Step 2: Set up networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking). 
  6. **Configure hosting and encryption** :

[ User journey D: Customer-managed encryption, with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting#cm-dr) is the only relevant user journey for organization policy constraints that restrict non-CMEK services. 

     1. Click edit **Edit** to open the **Hosting and encryption keys** panel.
     2. In the **Encryption type** section, **Google-managaged encryption key** is disabled and **Customer-managed encryption key** is enabled and cannot be disabled.
     3. Click **Next**.
     4. In the **Control Plane** section, **Enable data residency** is enabled and cannot be disabled. 
     5. Continue configuring hosting and encryption as described in step 3.b. of [ User journey D: Customer-managed encryption, with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting#cm-dr). 
  7. **Customize access routing** : Customize access routing as described in [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing). 



### Use a key from an allowlisted project

To use a key from a project that is allowlisted in Apigee, you will need to enter a key manually by its resource ID. Any key you enter manually will also be validated to ensure that its project is valid based on the allowlisted projects in the constraint. 

### How to get a Google Cloud KMS resource ID

See: [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids)

## Troubleshooting

The following table describes some common error conditions that may arise with CMEK and organization policy constraints. 

Error message | Cause | Steps to take  
---|---|---  
`Constraint constraints/gcp.restrictNonCmekServices violated for projects/my-project attempting to create or enable trial org. CMEK is not supported for trial orgs. To use trial orgs, adjust the gcp.restrictNonCmekServices constraint for this project.` | You attempted to provision a trial org where an organization policy constraint exists for the project.  |  CMEK is not supported for trial/eval orgs. You will have to update organization policy constraint `constraints/gcp.restrictNonCmekServices` to remove Apigee from the denied services list to be able to provision a trial org.  
`Constraint constraints/gcp.restrictNonCmekServices violated for projects/my-project attempting to create or enable global org. CMEK is not supported in location 'global', select another location or adjust the code constraint for this project.` |  You attempted to provision a global org where an organization policy constraint exists for the project.  |  CMEK is not supported for global orgs. You will have to update organization policy constraint `constraints/gcp.restrictNonCmekServices` to remove Apigee from denied services list or use a different location to create their orgs.   
`Constraint constraints/gcp.restrictNonCmekServices violated for projects/my-project attempting to create a resource without specifying a KMS CryptoKey. Provide a KMS CryptoKey to use for this resource.` |  You attempted to provision an org where an organization policy constraint exists for the project without specifying a KMS CryptoKey.  |  You have set code in organization policies which requires you to provide a CMEK to encrypt your data. You will have to provide the CMEK key to be able to create an org or instances. If you do not want to have CMEK enforcement, you can update the organization policy constraint `constraints/gcp.restrictNonCmekServices` to remove Apigee from the denied services list.  
`Constraint constraints/gcp.restrictCmekCryptoKeyProjects violated for projects/my-project attempting to use projects/my-project/locations/my-location/keyRings/kr-1/cryptoKeys/ck-1 key. Use a key from a project that is allowed by `the gcp.restrictCmekCryptoKeyProjects` constraint. ` |  You attempted to provision an org where an organization policy constraint exists for the project and specified a KMS CryptoKey that is not allowlisted.  |  You have set `constraints/gcp.restrictCmekCryptoKeyProjects` in organization policies which require you to provide a CMEK key from the allowed projects listed by you. You will have to provide the CMEK key from an allowed project to be able to create an org or instances. Alternatively, you can update the organization policy constraint `constraints/gcp.restrictCmekCryptoKeyProjects` to allow keys from the specific Google Cloud project you want.   
`Constraint constraints/gcp.restrictNonCmekServices violated for projects/my-project attempting to create a portal. Integrated portals do not support the use of CMEK. To use integrated portals, adjust the gcp.restrictNonCmekServices policy constraint.` |  You attempted to create a portal where an organization policy constraint exists for the project.  |  CMEK is not supported for Integrated Portals. You will have to update organization policy constraint `constraints/gcp.restrictNonCmekServices` to remove Apigee from the denied services list to be able to create a new portal.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
