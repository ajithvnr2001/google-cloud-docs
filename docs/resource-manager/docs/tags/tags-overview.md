---
url: https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview/
title: Tags overview \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:13.039231+00:00
---

# Tags overview  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Tags overview Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) is a way to organize your resources into a tree structure. This hierarchy helps you manage resources at scale, but it models only a few business dimensions, including organization structure, regions, workload types, and cost centers. The hierarchy lacks the flexibility to layer multiple business dimensions together.

Tags provide a way to create annotations for resources, and in some cases conditionally allow or deny policies based on whether a resource has a specific tag. You can use tags and conditional enforcement of policies for fine-grained control across your resource hierarchy.

## Tags and labels

Labels are a separate way to create annotations for resources. The following table lists some of the differences between tags and labels:

| Tags | Labels  
---|---|---  
**Resource structure** | Tag keys, tag values, and tag bindings are all discrete resources | Not a resource in itself, but metadata for resources  
**Definition** | Defined at the organization or project level | Defined by each resource  
**Access control** | Management and attachment of tags requires [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions) | Attachment of labels requires [IAM roles](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#permissions), which vary based on the service resource  
**Prerequisite for attachment** | The tag key and tag value must be defined before a tag can be attached to a resource | No prerequisites for attachment  
**Inheritance** | Tag bindings are inherited by children of the resource in the Google Cloud hierarchy | Not inherited by children of the resource  
**Deletion requirements** | Tags can't be deleted unless no tag bindings for that tag exist | Can be removed from a resource at any time  
**Naming requirements** | Requirements for [tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values) and [tag keys](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) | Requirements for [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)  
**Key-value name length** | 256 characters maximum | 63 characters maximum  
**Allow and deny policy support** | Tags can be referenced by [allow policy conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) and [deny policy conditions](https://docs.cloud.google.com/iam/docs/deny-overview#denial-conditions) | No allow and deny policy support  
**Organization policy support** | Tags on some resources can be referenced by [organization policy conditional constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) | No organization policy support  
**Cloud Billing integration** | Perform chargebacks, audits, and other cost allocation analysis, export [Cloud Billing cost data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) | Filter resources by label in Cloud Billing, export [Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/bq-examples)  
  
For more information about labels, see [Creating and managing labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

**Caution:** Existing labels and [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) continue to be supported for the purposes of extensibility and automation.

## Semantic tags

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A semantic tag is a key-value pair that provides meaningful metadata for your resources with strong, standardized semantics backed by OpenTelemetry (OTel) conventions.

You can use semantic tags with App Hub resources. When you set attributes on services and workloads in App Hub, App Hub automatically replicates them as read-only system semantic tags on the direct underlying resources.

System semantic tags are read-only. You can't edit or remove these system tags directly by using Tags API or the Google Cloud console. Tag management occurs within App Hub.

### App Hub replicated semantic tags

If you use App Hub, the _Environment_ and _Criticality_ attributes set on your services or workloads are automatically replicated as read-only system semantic tags under the dedicated namespace `google:AppHub`.

Supported system tags include:

  * `google:AppHub/environment`: values derived from App Hub, for example `PRODUCTION` or `STAGING`.
  * `google:AppHub/criticality`: values derived from App Hub, for example `MISSION_CRITICAL` or `HIGH`.



Surfacing App Hub context as system tags ensures that downstream services, such as the Google Cloud console consume authoritative metadata to enforce governance and security policies without the risks associated with manual configuration.

For more information about managing semantic tags, see [View and manage semantic tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#view_and_manage_semantic_tags).

### The Semantic Catalog

The Semantic Catalog provides a list of available semantics and their mapping to OpenTelemetry (OTel) backed attributes. You can browse this catalog in the Google Cloud console or view details using APIs.

For more information about accessing the catalog, see [View the Semantic Catalog](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#view_semantic_catalog).

Semantics key | OTel attribute key | Semantics value | OTel attribute value  
---|---|---|---  
`ENVIRONMENT` | `deployment.environment.name` | `PRODUCTION` | `production`  
|  | `STAGING` | `staging`  
|  | `TEST` | `test`  
|  | `DEVELOPMENT` | `development`  
`CRITICALITY` | `service.criticality` | `MISSION_CRITICAL` | `critical`  
|  | `HIGH` | `high`  
|  | `MEDIUM` | `medium`  
|  | `LOW` | `low`  
  
### Limitations of semantic tags

Semantic tags have the following limitations:

  * **Custom bindings** : You can't directly bind `ENVIRONMENT` or `CRITICALITY` semantic tags to resources or Resource Manager nodes (projects, folders, or organizations) through Tags API.
  * **User-defined semantics** : Promoting your existing tags to semantic tags isn't supported.
  * **Direct resources only** : Synchronization applies only to _direct_ resources registered in App Hub. It doesn't propagate to nested or indirect resources within a service or workload (for example, individual VMs in a MIG).



## Creating tags

Tags are structured as a key-value pair. A tag key resource can be created under your organization or project resources, and tag values are resources that are attached to a key—for example, a tag key `environment` with values `production` and `development`.

## Tag administration

Administrators can control the usage of tags by restricting who can create, update, delete, and attach tags to resources. They can select an individual tag to make edits, such as to add or remove values, and update the description. This allows for fine-grained control of your tags.

Tags optionally have a description that is displayed when information about the tag is retrieved. The description helps users who attach the tag to the resource understand the tag's purpose.

In a parent project or organization, each tag key must be unique. This ensures that each tag value, when bound to a resource, creates a unique pairing with its tag key.

## Policies and tags

You can use tags and IAM conditions together to:

  * [Conditionally grant IAM roles](https://docs.cloud.google.com/iam/docs/conditions-overview)
  * [Conditionally deny IAM permissions](https://docs.cloud.google.com/iam/docs/deny-overview)



After you create a tag value, you can bind the tag value to resources. You can then create [IAM policies with conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) that identify resources based on whether a tag key has been bound to the resource. For information about using tags and IAM conditions, see [Tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control).

## Impact of tag changes

If you use tags to conditionally grant or deny access or to [scope organization policies](https://docs.cloud.google.com/organization-policy/scope-policies), then binding or unbinding a tag from a resource can change the impact of these policies.

For example, suppose you have a group of developers who need to manage Compute Engine instances, but only those used for development:

  1. **Tag definitions** : You have a tag key `123456789012/env` with values `dev` and `prod`.
  2. **Conditional access** : You grant the **Compute Instance Admin** role (`roles/compute.instanceAdmin`) to the developer group. You add a condition to the role binding that allows access only if the resource has the tag `env: dev`.
  3. **Effects of changes** : 
     * **Binding tags** : You attach the tag `env: dev` to an instance. The conditional role binding now grants developers access to manage the instance.
     * **Unbinding tags** : Later, the same instance is promoted to production. You unbind the `env: dev` tag and bind the `env: prod` tag. The conditional role binding no longer grants developers access to manage this instance.



In general, tag changes take effect within 2 minutes. However, changes can potentially take up to 7 minutes to fully propagate across the system. This propagation delay applies to how quickly access is granted or revoked, or how quickly an organization policy takes effect after a tag binding or unbinding.

## Enforcement of mandatory tags using organization policies

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce mandatory tags on resources by using a custom organization policy. When you enforce mandatory tags, you can only create resources that comply with your organization's tagging policies; that is, resources are bound with the tag values for the mandatory tag keys specified in the policy. For more information, see [Set up a custom constraint to enforce tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#create_custom_constraint_tags). 

Enforcement of mandatory tags is supported for the following resource types:

  * Resource Manager projects and folders
  * Filestore instances
  * AlloyDB for PostgreSQL cluster and backup resources
  * Workflows workflow
  * Compute Engine resources: 
    * Instances
    * Disks
    * External Vpn Gateways
    * Vpn Gateways
    * Target Vpn Gateways
    * Vpn Tunnels
    * Interconnects
    * Interconnect Attachments
    * Backend Services
    * Regional Backend Services
    * Backend Buckets
  * VPC resources: 
    * Networks
    * Subnetworks
    * Firewall rules
    * Routes



## Tag inheritance

When a tag value is attached to a resource, by default, all descendants of the resource inherit the same tag value. You can override an inherited tag value on a descendant resource. To override an inherited tag value, bind a different tag value to the descendant resource. The different tag value must use the same tag key as the inherited tag value.

For example, suppose that you apply the tag `environment: development` to a folder, and the folder has two child folders named `team-a` and `team-b`. You can also apply a different tag, `environment: test`, to the `team-b` folder. As a result, projects and other resources in the `team-a` folder inherit the tag `environment: development`, and projects and other resources in the `team-b` folder inherit the tag `environment: test`:

![Resource hierarchy with tags](https://docs.cloud.google.com/static/resource-manager/img/tags-resource-hierarchy.svg)

![Resource hierarchy with tags](https://docs.cloud.google.com/static/resource-manager/img/tags-resource-hierarchy.svg)

If you remove the `environment: test` tag from the `team-b` folder, then that folder and its resources inherit the tag `environment: development`.

All of the tags that are both attached to and inherited by a resource are collectively called the _effective tags_. The effective tags for a resource are a combination of the tags directly attached to it, as well as all tags attached to all of the resource's ancestors throughout the hierarchy.

When using tags with IAM conditions, we recommend that you create a safe default tag value for each tag key used by your IAM conditions. Apply the safe default tag value by binding that tag value to your organization so that it is inherited by all resources within the organization. Only change the tag value by explicitly overriding inherited bindings on relevant resources.

For example, suppose you have an IAM condition that depends on the tag value `on` for the `enforcement` tag key, and the tag key also has an `off` tag value. Bind the tag value `enforcement: off` to the organization to create a safe default that's inherited by all resources within the organization. Only bind the tag value `enforcement: on` to selected resources within the organization.

You can then write policies that address the `enforcement` tag key, with conditions that affect a resource if it is `enforcement: on` or `enforcement: off`, and a safe case if it is `enforcement: default`. If the `enforcement` tag key is ever removed from a resource, the resource can then inherit the tag value for `enforcement` from its parent resource. If no parent resource has the `enforcement` tag key, the resource inherits `enforcement: default` from the organization resource.

Using a safe default tag can help, but to prevent unintended behaviors, we recommend that you review the tags and policies with conditions in place before moving your resources or removing tags.

## Deleting tag keys and values

Before you can delete a tag value, you must delete all resource bindings that use the tag value.

### Protecting tag values from deletion

You can create an additional layer of protection for your tag values by attaching a tag hold to a tag value. A tag hold, like a tag binding, prevents a user from deleting the tag value.

Some resources automatically create a tag hold on each tag value attached to the resource. This tag hold must be removed before you can delete the tag value.

## What's next

  * For more information about how to use tags, read the [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) page.
  * For information about using tags with Compute Engine, see [Manage tags for resources](https://docs.cloud.google.com/compute/docs/tag-resources).
  * For information about using secure tags for firewall policies, see [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
