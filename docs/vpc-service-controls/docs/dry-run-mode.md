---
url: https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode/
title: Dry run mode for service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:50.022465+00:00
---

# Dry run mode for service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Dry run mode for service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

When using VPC Service Controls, it can be difficult to determine the impact to your environment when a service perimeter is created or modified. With dry run mode, you can better understand the effect of enabling VPC Service Controls and changes to perimeters in existing environments.

In the dry run mode, requests that violate the perimeter policy are not denied, only logged. You can use the dry run mode to test perimeter configuration and to monitor usage of services without preventing access to resources. The common use cases include the following:

  * Determining the impact that changes to existing service perimeters will have.

  * Previewing the impact that new service perimeters will have.

  * Monitoring requests to protected services that originate from outside a service perimeter. For example, seeing where requests to a given service are coming from, or to identify unexpected service usage in your organization.

  * In your development environments, creating an analogous perimeter architecture to your production environment. This allows you to identify and mitigate any issues that will be caused by your service perimeters before pushing changes to your production environment.




Service perimeters can exist using dry run mode exclusively. You can also have service perimeters that use a hybrid of enforced and dry run modes.

## Benefits of dry run mode

Using dry run mode, you can create new service perimeters or change multiple existing perimeters with no impact to an existing environment. Requests that violate the new perimeter configuration are not blocked. You can also understand the impact of the perimeter in an environment where not all services being used are integrated with VPC Service Controls.

You can analyze the [VPC Service Controls logs](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#identifying_blocked_requests) for denials, change the configuration to fix potential issues, and then enforce the new security posture.

If issues with the perimeter configuration cannot be resolved, you can choose to keep your perimeter's dry run configuration and monitor the logs for unexpected denials that may indicate an exfiltration attempt. Requests to the perimeter are not denied, however.

## Dry run mode concepts

Dry run mode operates as a second evaluation pass of the perimeter configuration. By default, the enforced mode configuration for all service perimeters is _inherited_ into the dry run mode configuration, where the configuration can be modified or deleted without impacting the operation of the service perimeter.

Because dry run mode inherits the enforced mode configuration, at each step both configurations must be valid. In particular, a project can only be in one perimeter in the enforced configuration and one perimeter in the dry run configuration. As a result, changes that span multiple perimeters, such as moving a project between perimeters, must be sequenced in the proper order.

Dry run mode only logs a request if it meets both the following criteria:

  * The request is _not_ already denied by the perimeter's dry run or enforced configuration.

  * The request violates the perimeter's dry run configuration.




For example, if identical dry run and enforced mode configurations restrict a Cloud Storage bucket, the enforced mode blocks and logs any request to the Cloud Storage bucket. The dry run mode only logs the differences in violations compared to the enforced mode.

In the audit logs of a dry run mode policy check, the `metadata.dryRun` field's value in the audit log is set to `True`. For more information, see [Audit log record content](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging#audit_log_record_content).

You can also create perimeters that have _only_ a dry run configuration. This allows you to simulate the impact of a new enforced perimeter in your environment.

To evaluate the dry run configuration of a service perimeter, set the `useExplicitDryRunSpec` field in the service perimeter configuration to `True`. For more information, see [`accessPolicies.servicePerimeters`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters).

**Note:** The usage of perimeter resources, ingress rules, and egress rules in the dry run mode also contributes to the overall quota utilization of the access policy limits. For more information, see [Quotas and limits](https://docs.cloud.google.com/vpc-service-controls/quotas).

### Policy semantics

The following section describes the policy relationship between enforced and dry run mode, and what order enforcement is resolved in.

#### Unique membership constraint

A Google Cloud project can be included only in one enforced configuration and one dry run configuration. However, the enforced and dry run configurations do not need to be for the same perimeter. This allows you to test the impact of moving a project from one perimeter to another without compromising the security currently applied to the project.

##### Example

Project `corp-storage` is currently protected by the enforced configuration of perimeter PA. You want to test the impact of moving `corp-storage` to perimeter PB.

The dry run configuration for PA hasn't been modified yet. Because the dry run configuration is unmodified, it inherits `corp-storage` from the enforced configuration.

To test the impact, you first remove `corp-storage` from the dry run configuration for PA and add the project to the dry run configuration for PB. You have to remove `corp-storage` from the dry run configuration for PA first because projects can only exist in one dry run configuration at a time.

When you are satisfied that migrating `corp-storage` from PA to PB will not have adverse effects on your security posture, you decide to enforce the changes.

There are two ways to enforce the changes to perimeters PA and PB:

  * You [can manually remove](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#enforce-configuration) `corp-storage` from the enforced configuration for PA and add the project to the enforced configuration for PB. Because `corp-storage` can only be in a single enforced configuration at a time, you need to perform the steps in this order.

_-or-_

  * You can use [the `gcloud` command-line tool](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#enforce-all) or [the Access Context Manager API](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#commit) to enforce _all_ dry run configurations. This operation applies to all modified dry run configurations for your perimeters, so you would want to coordinate the operation with anyone else in your organization who has modified dry run configurations for your perimeters. Because the dry run configuration for PA already excludes `corp-storage`, no additional steps are required.




#### The enforced configuration of a perimeter is executed first

Only requests that are _allowed_ by the enforced configuration of a perimeter but _denied_ by the dry run configuration are logged as dry run policy violations. Requests that are denied by the enforced configuration but would be allowed by the dry run configuration are not logged.

#### Access levels do not have a dry run mode equivalent

While you can create a dry run configuration for a perimeter, access levels do not have a dry run configuration. In practice, this means if you want to test how a change to an access level would affect your dry run configuration, you must:

  1. Create an access level that reflects the changes you want to make to an existing access level.

  2. Apply the new access level to the dry run configuration for the perimeter.




#### Dry run mode does not have a negative impact on security

Changes to a dry run configuration for a perimeter, such as adding new projects or access levels to a perimeter, or changing what services are protected or accessible to networks inside the perimeter, have no impact on the actual enforcement of a perimeter.

For example, assume you have a project that belongs to service perimeter PA. If the project is added to the dry run configuration of another perimeter, the actual security applied to the project does not change. The project continues to be protected by the enforced configuration of perimeter PA, as expected.

### Dry run actions and configuration statuses

Using the dry run feature, you can:

  * Create a perimeter with only a dry run configuration

  * Update an existing perimeter's dry run configuration

  * Move a new project into an existing perimeter

  * Move a project from one perimeter to another

  * Delete a perimeter's dry run configuration




Based on the action taken in dry run mode, a perimeter can be in one of the following configuration statuses:

**Inherited from enforced:** Default state for enforced perimeters. In this state, any changes to the perimeter's enforced configuration are also applied to the dry run configuration.

**Modified:** The dry run configuration for a perimeter has been viewed or changed, and then saved. In this state, changes to the enforced configuration of a perimeter are not applied to the dry run configuration.

**New:** The perimeter has only a dry run configuration. Even if changes are made to the dry run configuration, until this perimeter has an enforced configuration, the status remains **New**.

**Deleted** : The dry run configuration for the perimeter has been deleted. This status remains until you create a new dry run configuration for the perimeter or undo the action. In this state, changes to the enforced configuration of a perimeter are not applied to the dry run configuration.

## Limitations of dry run mode

Dry run mode only applies to perimeters. It does not help understand the impact of restricting Google Cloud API access to the [restricted or private VIP](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity). We recommend ensuring that all services that you want to use are available on the restricted VIP before you configure the `restricted.googleapis.com` domain.

If you're unsure whether the APIs you're using in an existing environment are supported by the restricted VIP, we recommend using the private VIP. You can still enforce perimeter security for supported services. However, if you use the private VIP, entities within your network will have access to unsecured services (services that are not supported by VPC Service Controls), such as the consumer versions of Gmail and Drive. Because the private VIP allows services that aren't supported by VPC Service Controls, it is possible for compromised code, malware, or a malicious user within your network to exfiltrate data using those unsecured services.

## What's next?

  * [Create a perimeter in dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters)

  * Learn to [manage your dry run configurations](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations)

  * Review [the `gcloud` command-line tool commands](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run) for dry run mode




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
