---
url: https://docs.cloud.google.com/resource-manager/docs/handle-special-cases/
title: Handle special cases \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:28.324285+00:00
---

# Handle special cases  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/handle-special-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Handle special cases Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to handle special cases when you migrate projects. Before you migrate a project, ensure that you have the required Identity and Access Management (IAM) [permissions](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-roles) on the project, its parent resource, and the destination resource.

## Migrate projects that aren't associated with an organization resource

You can migrate a project that was created with no associated organization resource into the hierarchy of an organization resource. However, you can't reverse this process. To revert a project to **No organization** , contact Cloud Customer Care for assistance.

To migrate a project that isn't associated with an organization resource, you must have the `roles/resourcemanager.projectIamAdmin` role on the project. You must also have the `roles/resourcemanager.projectCreator` role on the destination organization resource.

If you don't have the `resourcemanager.organizations.get` permission on the parent organization resource, your projects might not appear as expected under the organization in the Google Cloud console. This can make it seem like the project isn't associated with an organization resource. For more information, see [Restricting project visibility for users](https://docs.cloud.google.com/resource-manager/docs/access-control-org#restricting_visibility).

To determine whether the project is associated with an organization resource, do the following:

###  gcloud 

Run the following command:
    
    
    gcloud projects describe PROJECT_ID
    

Replace PROJECT_ID with the ID of the project you want to migrate.

If the **parent** resource is _not_ displayed in the output, it confirms that the project isn't associated with an organization resource.

If the **parent** resource (folder or organization resource) is displayed in the output, it confirms that the project is associated with an organization resource.

**Note:** Reverting a project to **No organization** requires business justification.

The process of migrating a project not associated with an organization resource is similar to the process for migrating a project between organization resources, but doesn't require all the steps in the migration plan. To migrate a project into an organization resource, follow these steps:

  1. Verify the impact on this project of the [policies it will inherit](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan#plan_policy).

  2. Create a [dedicated import folder](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan#import_export_folders) in the destination organization resource, if required.

  3. Assign Identity and Access Management permissions for the **project** and the **destination parent** resource as detailed in [Assign permissions](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-roles).

  4. Determine if you need to change the [billing account](https://docs.cloud.google.com/resource-manager/docs/perform-migration#migrating_existing_billing_accounts).




Then, you can perform the migration using one of the following methods:

###  Console 

  1. Open the **IAM & Admin > Settings** page in the Google Cloud console. 

[Open the Settings page](https://console.cloud.google.com/projectselector/iam-admin/settings)

  2. Select your project (one with **No organization**) using the project picker.

  3. At the top of the **Settings** page, click **Migrate**.

  4. In the dialog that appears, select the organization resource you want to migrate your project to, and then click **Migrate**.




###  gcloud 

To migrate a project into an organization resource, run the following command:
    
    
    gcloud beta projects move PROJECT_ID \
        --organization ORGANIZATION_ID
    

Replace the following:

  * PROJECT_ID: the ID of the project to migrate
  * ORGANIZATION_ID: the ID of the destination organization resource



###  API 

Using the Resource Manager API, you can migrate a project into the organization resource by setting its `parent` field to the organization resource ID of the organization resource.

To migrate a project into the organization resource:

  * Get the `project` object using the `projects.get()` method.
  * Set its `parent` field to the organization resource ID of the organization resource.
  * Update the `project` object using the `projects.update()` method.



You can't change the `parent` field after you set it.

The following code snippet demonstrates these steps:
    
    
        project = crm.projects().get(projectId=flags.projectId).execute()
        project['parent'] = {
            'type': 'organization',
            'id': flags.organizationId
        }
    

If [Cloud OS Login API](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) is enabled in your source project, assign the `roles/compute.osLoginExternalUser` role to any principals that have access to that project.

## Shared VPC

**Note:** Due to propagation delay, it might take up to two minutes for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) service projects to be migrated after their host project. You might encounter an error during this time. If this happens, retry the migration.

You can migrate Shared VPC projects under certain conditions. First, a user with the `roles/orgpolicy.policyAdmin` role in the source organization resource must set an organization policy containing the `constraints/resourcemanager.allowEnabledServicesForExport` constraint on the parent of the project to be exported. This constraint should list `SHARED_VPC` as an **allowed_value**.

You don't need to disable Shared VPC before migration. However, you must migrate the Shared VPC host project first, followed by all of its service projects. We recommend that you match the firewall rules between the source and target organization resources to minimize potential issues and avoid downtime. We don't guarantee the health of your network if you leave service projects in the source organization resource while migrating others.

If you migrate the host project, you can move it back to the source organization resource. There's no exact deadline for how long the host and service projects can be in different organizations. However, once you begin migrating service projects, you must migrate all of them before you can migrate the host project again.

## Custom IAM roles

[Custom Identity and Access Management roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) provide granular control of access to resources at the organization resource level, but they're only valid in the organization resource where they're created. If you migrate a project that contains an allow policy binding to an organization-level custom IAM role, the migration fails. The error explains that the role doesn't exist in the destination organization resource.

To list all custom IAM roles in your organization resource, run the following command:
    
    
    gcloud iam roles list --organization ORGANIZATION_ID
    

Replace ORGANIZATION_ID with the ID of the organization resource. For more information, see [Get your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

To get information about a custom Identity and Access Management role in your organization resource, run the following command:
    
    
    gcloud iam roles describe --organization ORGANIZATION_ID \
        ROLE_ID
    

Replace the following:

  * ORGANIZATION_ID: the ID of the organization resource
  * ROLE_ID: the name of the role to describe



To work around this error, create equivalent project-level custom roles for each inherited organization-level custom role. Then, remove the IAM role bindings that reference the organization-level custom roles.

After you migrate the project, you can update the allow policies to use the organization-level custom roles in the destination organization resource.

For more information, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Bucket Lock

[Cloud Storage Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) lets you configure a data retention policy on a Cloud Storage bucket. This policy governs how long objects must be retained. The bucket lock is protected using a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) to prevent accidental project deletion.

The retention policy and lien are kept with the project during migration. The lien doesn't prevent you from migrating the project.

## VPC Service Controls security perimeters

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) mitigates data exfiltration risks by setting up a project-based security perimeter around Google Cloud services. You can't migrate a project protected by a VPC Service Controls security perimeter.

To remove a project from a security perimeter, see [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters). It might take several hours or up to a day for you to migrate a project after you remove it from a service perimeter.

## Context-Aware Access policies for service accounts

[Context-Aware Access](https://docs.cloud.google.com/access-context-manager/docs/securing-console-and-apis) lets users define access policies on Google Cloud resources for service accounts based on context attributes like network, location, and time. You cannot migrate a project that has at least one Context-Aware Access policy for service accounts.

To delete a Context-Aware Access policy for service accounts, see [Managing access bindings](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings).

Note the following timing considerations when creating or deleting policies:

  * **Policy creation:** A newly created Context-Aware Access policy might not block migrations immediately. This propagation delay can last for up to 24 hours after the policy is created.
  * **Policy deletion:** After all of the Context-Aware Access policies are removed from a project, it can take several hours before you can migrate the project.



## Dedicated Interconnect

We recommend migrating projects with Dedicated Interconnect objects and projects with VLAN attachments together. Projects with these objects continue to function after migration between organization resources. However, you can't create new VLAN attachments between organization resources while they're split.

Configuration changes made to a split project might not propagate across organization resources. We recommend that you don't leave projects split for long.

## Partner Interconnect

There aren't any special considerations for migrating projects with Partner Interconnect. There are no special considerations needed when migrating projects with Partner Interconnect.

## Management Project

[Management project](https://docs.cloud.google.com/resource-manager/docs/manage-applications#management-project) is a Google Cloud project in the app-enabled folder that acts as a central repository for all your application-centric metadata. Each app-enabled folder contains only one management project. The management project provides the infrastructure for application libraries and APIs, including billing, quotas, and access control. You cannot migrate a Management Project.

## Cross-project service accounts

When you migrate a [cross-project service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project), the following cases apply:

  * If you migrate a project with a cross-project service account attached, the service account continues to function in the destination organization resource. This applies even if an organization policy [restricts the domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).
  * If you migrate a project that owns a cross-project service account used by another project, the service account continues to function. However, you can't use it on resources that have a domain restriction organization policy applied that restricts them to the source organization resource domain.



For example, assume `project-A` in `organizations/12345678901` has `serviceAccount-1` attached. `project-B` and `project-C` in the same organization also use `serviceAccount-1`.

`project-C` has an organization policy that only allows the `organizations/12345678901` domain.

If you add `serviceAccount-1` to the IAM binding for `project-C` before you migrate `project-A` to `organizations/45678901234`, the service account functions.

If you migrate `project-A` to `organizations/45678901234` and then try to add `serviceAccount-1` to the IAM binding for `project-C`, the binding fails because it violates the domain restriction.

## Support cases

If you migrate a project with an open support case, notify Cloud Customer Care after the migration. You can't view those support cases until Cloud Customer Care updates the metadata to the new organization resource.

## OAuth consent screen

If your project uses an [Internal OAuth consent screen](https://support.google.com/cloud/answer/10311615), only destination organization resource members can authorize requests after migration. This change can take up to 24 hours to take effect. Until then, source organization resource members can still authorize requests.

To ensure source members don't lose access, consider creating new users in the destination organization resource or updating the OAuth consent screen configuration:

  1. Update the OAuth consent screen to be external instead of internal.

  2. If the app uses [sensitive data](https://support.google.com/cloud/answer/9110914#sensitive-scopes), apply for [app verification](https://support.google.com/cloud/answer/9110914#ver-prep) for sensitive or restricted scopes. Otherwise, users will see an [unverified app screen](https://support.google.com/cloud/answer/7454865).




## Cloud OS Login API

If [Cloud OS Login API](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) is enabled in your source project, assign the `roles/compute.osLoginExternalUser` role to any principals that have access to that project. This ensures that these principals don't lose access in the destination organization resource.

**Warning:** Cloud OS Login API POSIX profiles are scoped to an organization resource. When you migrate a project, POSIX profiles for users aren't migrated and they lose access. To restore access, you must repopulate the POSIX profiles in the destination organization resource, for example by re-importing SSH keys. 

## Shared reservations of virtual machine (VM) instances

In a shared reservation, the project that created the reservation (_owner project_) or any projects it's shared with (_consumer project_) can consume the reservation by creating VM instances. You can only share a reservation with projects in the same organization as the owner project.

When you migrate an owner or consumer project, the following happens:

  * If you migrate the owner project, Compute Engine deletes any reservation created by that project. Running VM instances aren't affected.
  * If you migrate a consumer project, it stops consuming resources from any shared reservation in the previous organization.



For more information, see [How shared reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

## Attaching service accounts to resources

For most Google Cloud services, you need the `iam.serviceAccounts.actAs` permission to attach a service account to a resource. However, some services historically allowed this without explicit impersonation permissions. This is documented in [Requiring permission to attach service accounts to resources](https://docs.cloud.google.com/iam/docs/service-accounts-actas).

If your source organization resource has this legacy behavior but the destination doesn't, grant the `roles/iam.serviceAccountUser` role to users who attach these service accounts. For more information about permissions, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).

To check if your organization resource has the legacy behavior:

  1. In the Google Cloud console, go to the **Organization policies** page:

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the resource selector, choose the organization resource that you want to check.

  3. In the filter box, enter `constraints/appengine.enforceServiceAccountActAsCheck`.

  4. If the policy appears, the organization resource has the legacy behavior.

  5. Repeat steps 3 and 4 for each of the following constraints:

     * `appengine.enforceServiceAccountActAsCheck`
     * `dataflow.enforceComputeDefaultServiceAccountCheck`
     * `dataproc.enforceComputeDefaultServiceAccountCheck`
     * `composer.enforceServiceAccountActAsCheck`



If any of these constraints appear, your organization resource uses the legacy behavior. If both organization resources use the legacy behavior, no action is required, but consider enforcing the policy to prevent unintended impersonation.

## Migrating projects with BigQuery sharing

If you migrate a project that uses BigQuery sharing to another organization resource, you might encounter errors. To resolve them, [contact Cloud Customer Care](https://docs.cloud.google.com/bigquery/docs/support).

If the data exchange resource from the previous organization isn't visible in the Sharing administrator page of the new organization, use the BigQuery sharing API to update a field (for example, `description`) to trigger a cache refresh.

Use the [`projects.locations.dataExchanges.patch` method](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges/patch).
    
    
    PATCH https://analyticshub.googleapis.com/v1/projects/ \
        PROJECT_ID/locations/LOCATION/ \
        dataExchanges/DATA_EXCHANGE_ID \
        ?update_mask=UPDATE_DX_FIELD \
        -d { UPDATE_DX_FIELD:UPDATE_DX_VALUE }
    

Replace the following:

  * PROJECT_ID: the unique identifier of the project
  * LOCATION: the location of the data exchange
  * DATA_EXCHANGE_ID: the ID of the data exchange
  * UPDATE_DX_FIELD: the field to update, such as `description`
  * UPDATE_DX_VALUE: the updated value



## Backup and DR Service

Disable Backup and DR before you migrate projects to a different organization resource. Factor in the outage risk when the service is disabled. Re-enable Backup and DR after the migration is complete.

## Workload Identity Federation

[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) lets you grant on-premises or multi-cloud workloads access to Google Cloud resources. Workload Identity Federation pools are project-scoped resources.

When you migrate a project, the workload identity pools and their providers configured within that project are migrated with the project. No additional action is required to maintain access for workloads using these pools.

## Tags

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are key-value pairs attached to resources. Tags created at the organization level aren't migrated.

If your project uses organization-level tags for policy bindings or constraints, you must recreate the tag keys and values in the destination organization resource and re-attach them to the migrated projects.

## Migrating projects with inherited Privileged Access Manager grants

Before you migrate a project, we recommend that you [revoke](https://docs.cloud.google.com/iam/docs/pam-revoke-grants) any active scoped grants on that project. A scoped grant is created on an inherited entitlement from a folder or organization and then scoped to a child project.

When you migrate a project with an active scoped grant, the IAM policy moves to the new organization, but the grant managing it remains in the previous organization. The Privileged Access Manager service agent loses permission to modify the IAM policy in the new organization. Consequently, any revoke or withdraw operations on that grant fail, and the requester retains access until the grant expires.

**Note:** Even after a project has been migrated to a new organization, a user with IAM Admin access on the project can directly remove access using the IAM Admin console.

## What's next

  * [Perform the migration](https://docs.cloud.google.com/resource-manager/docs/perform-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
