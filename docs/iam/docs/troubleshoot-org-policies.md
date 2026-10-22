---
url: https://docs.cloud.google.com/iam/docs/troubleshoot-org-policies/
title: Troubleshoot organization policy errors for service accounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:00.943797+00:00
---

# Troubleshoot organization policy errors for service accounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/troubleshoot-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Troubleshoot organization policy errors for service accounts Stay organized with collections  Save and categorize content based on your preferences. 

The Organization Policy Service has several predefined and managed constraints that can affect service accounts in your organization. This page helps you understand what errors those organization policies generate, and the steps that you can take to resolve those errors.

## Required roles

To get the permissions that you need to troubleshoot organization policy issues, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Troubleshoot disabled service account key creation

If the `iam.disableServiceAccountKeyCreation` constraint is enforced for your organization, then you can't create keys for any service accounts in your organization. For more information about this constraint, see [Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation).

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

### Key creation error

If you try to create a service account key, but the action is blocked by the `iam.disableServiceAccountKeyCreation` constraint, you get the following error message:

### Console

In the Google Cloud console, a dialog appears with the heading **Service account key creation is disabled**. The dialog states that the `iam.disableServiceAccountKeyCreation` constraint is enforced on your organization.

### gcloud
    
    
    ERROR: (gcloud.iam.service-accounts.keys.create) FAILED_PRECONDITION: Key
    creation is not allowed on this service account.
    - '@type': type.googleapis.com/google.rpc.PreconditionFailure
      violations:
      - description: Key creation is not allowed on this service account.
        subject: projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com?configvalue=SERVICE_ACCOUNT_ID%40PROJECT_ID.iam.gserviceaccount.com
        type: constraints/iam.disableServiceAccountKeyCreation
    

### REST
    
    
    {
      "error": {
        "code": 400,
        "message": "Key creation is not allowed on this service account.",
        "status": "FAILED_PRECONDITION",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
            "violations": [
              {
                "type": "constraints/iam.disableServiceAccountKeyCreation",
                "subject": "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com?configvalue=SERVICE_ACCOUNT_ID%40PROJECT_ID.iam.gserviceaccount.com",
                "description": "Key creation is not allowed on this service account."
              }
            ]
          }
        ]
      }
    }
    

### Recommended resolution for service account key creation error

If an organization policy prevents you from creating a service account key, we recommend that you do the following:

  1. Assess whether a service account key is needed.

We don't recommend using service account keys for authentication. This is because service account keys can become a security risk if they're not managed properly, increasing your vulnerability to threats like credential leakage, privilege escalation, information disclosure, and non-repudiation.

In most cases, you should use a [more secure alternative](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) to authenticate instead of using a service account key.

  2. If a service account key is needed for your use case, disable the `iam.disableServiceAccountKeyCreation` constraint for your project.




To disable the organization policy constraint, either turn off enforcement for the constraint, or exempt your project from enforcement:

  * To turn off enforcement for the constraint for your entire organization, do the following:

    1. Ensure that you have the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. This role is only available to grant on organizations, and doesn't appear in the role list for projects.

To learn how to grant roles at the organization level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

    2. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

    3. In the project selector, select the organization that you want to disable the `iam.disableServiceAccountKeyCreation` constraint for.

    4. In the **Filter** field, enter `iam.disableServiceAccountKeyCreation`. Then, in the policy list, click **Disable service account key creation**.

    5. Click **Manage policy**.

    6. In the **Policy source** section, ensure that **Override parent's policy** is selected.

    7. Under **Enforcement** , turn off enforcement for this organization policy constraint.

    8. Click **Set policy**.

  * To exempt your project from enforcement, do the following:

    1. Ensure that you have the Tag Administrator role (`roles/resourcemanager.tagAdmin`) and the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. To learn how to grant roles at the organization level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    2. At the organization level, create a tag key and tag value that you will use to define whether a resource should be exempt from the organization policy. We recommend creating a tag with the key `disableServiceAccountKeyCreation` and the values `enforced` and `not_enforced`. 

To learn how to create tag keys and tag values, see [Creating and defining a new tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating). 

    3. Attach the `disableServiceAccountKeyCreation` tag to the organization and set its value to `enforced`. All resources in the organization inherit this tag value, unless it's overwritten with a different tag value. 

To learn how to attach tags to resources, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching). 

    4. For each service account that you want to exempt from the organization policy, attach the `disableServiceAccountKeyCreation` tag and set its value to `not_enforced`. Setting a tag value for a service account in this way overrides the tag value inherited from the organization. 
    5. [Create or update the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) that prevents the creation of service account keys so that it doesn't enforce the constraint for exempt resources. This policy should have the following rules: 

       * Configure the `iam.disableServiceAccountKeyCreation` constraint to not be enforced on any resources with the `disableServiceAccountKeyCreation: not_enforced` tag. The condition in this rule should look like the following: 
             
             "resource.matchTag('ORGANIZATION_ID/disableServiceAccountKeyCreation', 'not_enforced')"
             

       * Configure the `iam.disableServiceAccountKeyCreation` constraint to be enforced on all other resources. 




## Troubleshoot disabled service account creation

If the `iam.disableServiceAccountCreation` constraint is enforced for your organization, then you can't create service accounts in any projects in your organization. For more information about this constraint, see [Disable service account creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation).

### Service account creation error

If you try to create a service account, but the action is blocked by the `iam.disableServiceAccountCreation` constraint, you get the following error message:

### Console

In the Google Cloud console, a dialog appears with the heading **Service account creation failed**. The dialog states, **The attempted action failed, please try again**.

### gcloud
    
    
    ERROR: (gcloud.iam.service-accounts.create) FAILED_PRECONDITION: Service account
    creation is not allowed on this project.
    - '@type': type.googleapis.com/google.rpc.PreconditionFailure
      violations:
      - description: Service account creation is not allowed on this project.
        subject: projects/PROJECT_ID/serviceAccounts/?configvalue=
        type: constraints/iam.disableServiceAccountCreation
    

### REST
    
    
    {
      "error": {
        "code": 400,
        "message": "Service account creation is not allowed on this project.",
        "status": "FAILED_PRECONDITION",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
            "violations": [
              {
                "type": "constraints/iam.disableServiceAccountCreation",
                "subject": "projects/PROJECT_ID/serviceAccounts/?configvalue=",
                "description": "Service account creation is not allowed on this project."
              }
            ]
          }
        ]
      }
    }
    

### Recommended resolution for service account creation error

If an organization policy prevents you from creating a service account, we recommend that you do the following:

  1. Assess whether a service account is needed.

Review [Choose when to use service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#choose-when-to-use) to confirm that a service account is needed for your use case.

  2. If a service account is needed for your use case, disable the `iam.disableServiceAccountCreation` constraint for your project.




To disable the organization policy constraint, either turn off enforcement for the constraint, or exempt your project from enforcement:

  * To turn off enforcement for the constraint for your entire organization, do the following:

    1. Ensure that you have the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. This role is only available to grant on organizations, and doesn't appear in the role list for projects.

To learn how to grant roles at the organization level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

    2. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

    3. In the project selector, select the organization that you want to disable the `iam.disableServiceAccountCreation` constraint for.

    4. In the **Filter** field, enter `iam.disableServiceAccountCreation`. Then, in the policy list, click **Disable service account creation**.

    5. Click **Manage policy**.

    6. In the **Policy source** section, ensure that **Override parent's policy** is selected.

    7. Under **Enforcement** , turn off enforcement for this organization policy constraint.

    8. Click **Set policy**.

  * To exempt your project from enforcement, do the following:

    1. Ensure that you have the Tag Administrator role (`roles/resourcemanager.tagAdmin`) and the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. To learn how to grant roles at the organization level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    2. At the organization level, create a tag key and tag value that you will use to define whether a resource should be exempt from the organization policy. We recommend creating a tag with the key `disableServiceAccountCreation` and the values `enforced` and `not_enforced`. 

To learn how to create tag keys and tag values, see [Creating and defining a new tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating). 

    3. Attach the `disableServiceAccountCreation` tag to the organization and set its value to `enforced`. All resources in the organization inherit this tag value, unless it's overwritten with a different tag value. 

To learn how to attach tags to resources, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching). 

    4. For each project or folder that you want to exempt from the organization policy, attach the `disableServiceAccountCreation` tag and set its value to `not_enforced`. Setting a tag value for a project or folder in this way overrides the tag value inherited from the organization. 
    5. [Create or update the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) that prevents the creation of service accounts so that it doesn't enforce the constraint for exempt resources. This policy should have the following rules: 

       * Configure the `iam.disableServiceAccountCreation` constraint to not be enforced on any resources with the `disableServiceAccountCreation: not_enforced` tag. The condition in this rule should look like the following: 
             
             "resource.matchTag('ORGANIZATION_ID/disableServiceAccountCreation', 'not_enforced')"
             

       * Configure the `iam.disableServiceAccountCreation` constraint to be enforced on all other resources. 



## Troubleshoot granting roles to default service accounts

Default service accounts are created automatically when you use certain Google Cloud services. They have the following identifiers:

  * App Engine service default service account: `PROJECT_ID@appspot.gserviceaccount.com`
  * Compute Engine default service account: `PROJECT_NUMBER-compute@developer.gserviceaccount.com`



All default service accounts are automatically granted the Editor role (`roles/editor`) when they're created, unless that behavior is disabled by an organization policy. There are two organization policy constraints that prevent the Editor role from being granted to the default service accounts:

  * `iam.automaticIamGrantsForDefaultServiceAccounts`: A predefined constraint that prevents the default service accounts from being granted roles automatically. This constraint doesn't prevent you from later granting the Editor role to default service accounts.
  * `constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts`: A managed constraint that prevents the Editor and Owner (`roles/owner`) roles from ever being granted to the default service accounts.



### Granting basic roles to service accounts error

If the `iam.automaticIamGrantsForDefaultServiceAccounts` constraint or the `constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` constraint is enforced for your project, then workloads in your project that use the default service accounts might encounter insufficient permission errors. To learn which roles to grant to a default service account, see Recommended resolution for granting roles to default service accounts.

The `iam.automaticIamGrantsForDefaultServiceAccounts` constraint doesn't cause errors on its own. However, because of this constraint, it's possible that a workload that uses the default service account won't have the permissions that it needs.

Additionally, if the `constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` constraint is enforced for your project, then you'll see an error message like the following if you try to grant the Owner or Editor role to a default service account:

### Console

In the Google Cloud console, a dialog appears with the heading **IAM policy updated failed**. The dialog states that the changes you are trying to make to your IAM policy have been restricted by your organization policy administrator, then lists the constraints blocking the updated. The constraints listed includes the `customConstraints/custom.cantGrantProjectIamAdmin` constraint.

### gcloud
    
    
    ERROR: (gcloud.projects.set-iam-policy) FAILED_PRECONDITION: Operation denied by
    org policy on resource 'RESOURCE_ID':
    ["constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts":
    "When this constraint is enforced, it prevents anyone from granting the Editor
    role (roles/editor) or the Owner role (roles/owner) to the Compute Engine and
    App Engine default service accounts, at any time. To learn more about default
    service accounts, see
    https://cloud.google.com/iam/help/service-accounts/default. Enforcing this
    constraint prevents the default service accounts from automatically being
    granted the Editor role (roles/editor). This might cause permission issues for
    services that use these service accounts. To learn which roles to grant to each
    service account, see
    https://cloud.google.com/iam/help/service-accounts/troubleshoot-roles-default."].
    

### REST
    
    
    {
      "error": {
        "code": 400,
        "message": "Operation denied by org policy on resource
        'RESOURCE_ID':
        [\"constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts\":
        \"When this constraint is enforced, it prevents anyone from granting the
        Editor role (roles/editor) or the Owner role (roles/owner) to the Compute
        Engine and App Engine default service accounts, at any time. To learn more
        about default service accounts, see
        https://cloud.google.com/iam/help/service-accounts/default.\n Enforcing this
        constraint prevents the default service accounts from automatically being
        granted the Editor role (roles/editor). This might cause permission issues
        for services that use these service accounts. To learn which roles to grant
        to each service account, see
        https://cloud.google.com/iam/help/service-accounts/troubleshoot-roles-default.\"].",
        "status": "FAILED_PRECONDITION",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "CUSTOM_ORG_POLICY_VIOLATION",
            "domain": "googleapis.com",
            "metadata": {
              "customConstraints": "constraints/iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts",
              "resource": "projects/PROJECT_ID"
            }
          }
        ]
      }
    }
    

### Recommended resolution for granting roles to default service accounts

If an organization policy prevents you from granting the Editor or Owner role to a default service account, then you should find a less permissive role to grant to the service account. The role that the service account needs depends on the service you're using and the tasks you want to accomplish.

**Note:** We don't recommend disabling the organization policy. The Editor and Owner roles are basic roles, and shouldn't be used in production environments. However, if you decide to disable the organization policy, follow the instructions for [editing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

Review the following table to determine which role to grant to which default service account, depending on the service you're using:

Service | Default service account | Role to grant  
---|---|---  
App Engine |  App Engine default service account (`PROJECT_ID@appspot.gserviceaccount.com`)  |  Cloud Build Account role (`roles/cloudbuild.builds.builder`)   
Compute Engine |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  The roles that the default service account needs depend on the task that you want to accomplish. To figure out which roles are required, review the documentation for the task that you want to accomplish, or review [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).  When deciding which role to grant, follow the best practices described on the [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) page in the Compute Engine documentation.   
Cloud Build |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  Cloud Build Service Account role (`roles/cloudbuild.builds.builder`)   
Cloud Deploy |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  To see which roles to grant to this service account, find the Cloud Deploy quickstart that corresponds with your use case, then grant the roles described in that quickstart. For a list of Cloud Deploy quickstarts, see [Quickstarts](https://docs.cloud.google.com/deploy/docs/quickstarts) in the Cloud Deploy documentation.   
Cloud Run functions and Cloud Functions |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  To deploy functions: Cloud Build Account role (`roles/cloudbuild.builds.builder`) For more information, see [Custom service account for Cloud Build](https://docs.cloud.google.com/functions/1stgendocs/securing/build-custom-sa).   
Cloud Run |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  The roles that the default service account needs depend on the task that you want to accomplish. To figure out which roles are required, review the documentation for the task that you want to accomplish, or review [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).  For details about Cloud Run roles, see [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) in the Cloud Run documentation.   
Google Kubernetes Engine |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  Kubernetes Engine Default Node Service Account role (`roles/container.defaultNodeServiceAccount`) For more information, see [Use least privilege IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).   
Workflows |  Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`)  |  The roles that the default service account needs depend on the task that you want to accomplish. To figure out which roles are required, review the documentation for the task that you want to accomplish, or review [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).  Follow the best practices described on the [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication#default-sa) page in the Workflows documentation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
