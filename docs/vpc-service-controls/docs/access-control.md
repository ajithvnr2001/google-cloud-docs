---
url: https://docs.cloud.google.com/vpc-service-controls/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:38.076965+00:00
---

# Access control with IAM  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles required to configure VPC Service Controls.

## Required roles

The following table lists the permissions and roles required to create and list access policies:

Action | Required permissions and roles  
---|---  
Create an organization-level access policy or scoped policies |  Permission: `accesscontextmanager.policies.create` Role that provides the permission: Access Context Manager Editor role (`roles/accesscontextmanager.policyEditor`)   
List an organization-level access policy or scoped policies |  Permission: `accesscontextmanager.policies.list` Roles that provides the permission: 

  * Access Context Manager Editor role (`roles/accesscontextmanager.policyEditor`)
  * Access Context Manager Reader role (`roles/accesscontextmanager.policyReader`)

  
  
You can only create, list, or delegate [scoped policies](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies) if you have those permissions at the organization level. After you create a scoped policy, you can grant permission to manage the policy by adding IAM bindings on the scoped policy.

Permissions granted at the organization-level apply to all access policies, including the organization-level policy and any scoped policies.

**Note:** Any Access Context Manager permissions granted on folders or projects have no effect on scoped policies as permissions can only be granted at the organization-level or on individual policies. The access control for scoped policies is independent of the projects or folders in their scopes.

The following predefined IAM roles provide the necessary permissions to view or configure service perimeters and access levels:

  * Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)
  * Access Context Manager Editor (`roles/accesscontextmanager.policyEditor`)
  * Access Context Manager Reader (`roles/accesscontextmanager.policyReader`)



To grant one of these roles, use [the Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or run one of the following commands in the gcloud CLI. Replace `ORGANIZATION_ID` with the ID of your Google Cloud organization.

### Grant Manager Admin role to allow read-write access
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="user:example@customer.org" \
        --role="roles/accesscontextmanager.policyAdmin"

### Grant Manager Editor role to allow read-write access
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="user:example@customer.org" \
        --role="roles/accesscontextmanager.policyEditor"

### Grant Manager Reader role to allow read-only access
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="user:example@customer.org" \
        --role="roles/accesscontextmanager.policyReader"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
