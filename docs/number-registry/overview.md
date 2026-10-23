---
url: https://docs.cloud.google.com/number-registry/overview/
title: Cloud Number Registry overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:02.524264+00:00
---

# Cloud Number Registry overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Number Registry overview

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Number Registry lets you view, manage, and plan your IP address usage in Google Cloud. When you [set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry), a read-only discovery process imports IP address information for the whole organization, creating a representation of supported IP addresses and ranges. You can use Cloud Number Registry to do the following across the organization:

  * View IP address utilization for discovered ranges or custom ranges.
  * Find available IP address ranges within discovered ranges or custom ranges.
  * Search for IP address resources within a registry book.



## Project designation for Cloud Number Registry

Before you configure Cloud Number Registry, an IAM principal that has been granted the Cloud Number Registry IPAM Admin role at the organization level must designate a project to use for Cloud Number Registry in that organization. You designate a project by [creating an `org-number-registries` resource](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry) that references which project to use for a given organization.

After you configure Cloud Number Registry, the designated project contains IP address range information for the whole organization. To limit access to Cloud Number Registry information, we strongly recommend that you use the following configuration:

  * Create a new project to designate to use for Cloud Number Registry.
  * Configure Identity and Access Management policies so that only principals that need to view all IP address ranges in the organization can access that project.



## Cloud Number Registry IPAM resources

Cloud Number Registry uses the following resources to help you organize your IP address resources.

### IPAM admin scope

To use Cloud Number Registry, you [create an IPAM admin scope](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry) in a project. We strongly recommend that you create a new project that is used only for Cloud Number Registry. For more information, see Limitations.

The project must be part of an [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

Creating an IPAM admin scope starts a discovery process which imports Compute Engine resources in the parent organization of the project to Cloud Number Registry. These imported resources are known as _discovered resources_. The discovery process can take up to 24 hours to complete.

Only one project in a given organization can contain and manage the IPAM admin scope for the organization.

### Registry books

A registry book is a container for IP address management information. When you create an IPAM admin scope, Cloud Number Registry automatically creates a registry book called `default` and imports the discovered resources to it.

You can also [create additional registry books](https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges#create-registry-book) to help you organize your discovered resources. When you create a registry book, you defined a _claimed scope_ — one or more projects that you add to the registry book.

A project can be claimed by only one registry book. When you create a registry book and define the claimed scope, the realms and ranges that are associated with the projects in the claimed scope are added to the new registry book and removed from the default registry book.

You can query registry books for information about IP address usage and free IP address ranges.

### Realms

A realm is a set of managed IP address ranges that represent a network routing domain. IP address ranges that are managed within a realm can't overlap, unless one range is the parent of another shared range.

Cloud Number Registry creates a realm for the following resources as needed:

  * Each discovered [VPC network](https://docs.cloud.google.com/vpc/docs/vpc). The realm names start with `vpc-global`.
  * Google-provisioned external IPv4 and IPv6 addresses and ranges. The realms are named `google-owned-ipv4` and `google-owned-ipv6`.
  * [Bring your own IP addresses (BYOIP)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) public advertised prefixes. The realms are named `byoip-ipv4` and `byoip-ipv6`.



Discovered realms are managed by Cloud Number Registry—you can't modify them. However, you can [create custom realms](https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges#create-realm), which lets you include any ranges in Cloud Number Registry, including ranges that are outside of Google Cloud.

### Discovered ranges

The IP address ranges and IP addresses that Cloud Number Registry discovers are known as _discovered ranges_.

You can't directly update or delete discovered ranges in Cloud Number Registry. To modify a discovered range, you must modify the source Compute Engine resource. Cloud Number Registry reflects any changes that you make to the source resource.

### Custom ranges

[Custom ranges](https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges#create-custom-range) are IP address ranges that you've added to a custom realm. Because custom ranges are user-managed, you can update or delete these ranges from Cloud Number Registry directly.

Updating or deleting custom ranges doesn't affect the source Google Cloud resources.

## Discovered resources

The discovery process for Compute Engine resources creates the following realms as needed to organize the discovered resources:

  * A realm for each VPC network's internal IPv4 resources. The realm name starts with `vpc-global`. This realm contains discovered ranges for the following resources:

    * Subnet primary IPv4 address ranges.
    * Subnet secondary IPv4 address ranges.
    * Ephemeral and static internal IPv4 addresses.

These addresses are displayed as child ranges (`/32`) of the parent discovered range. For example, a regional internal IPv4 address that is assigned to an instance or a forwarding rule is displayed as a child range of the subnet's primary IPv4 address range.

    * Instances that use these IPv4 addresses.

  * A realm for each VPC network's internal IPv6 resources. This realm contains discovered ranges for the following resources:

    * ULA internal IPv6 range for internal IPv6 subnet ranges.
    * Subnet internal IPv6 address ranges.
    * Ephemeral and static internal IPv6 address ranges.

These ranges are displayed as child ranges of the parent discovered range. For example, a regional internal IPv6 address range that is assigned to an instance or a forwarding rule is displayed as a child range of the subnet's internal IPv6 address range.

    * Instances that use these IPv6 address ranges.

  * A realm named `google-owned-ipv4` that contains the following:

    * Ephemeral and static external IPv4 addresses.
    * Instances that use these IPv4 addresses.
    * Instances that use static external IPv4 addresses that come from a BYOIP public delegated prefix. For more information, see Limitations.
  * A realm named `google-owned-ipv6` that contains the following:

    * Subnet external IPv6 address ranges.
    * Static external IPv6 address ranges.
    * Ephemeral IPv6 address ranges that are assigned to resources such as instances and forwarding rules.
    * Instances that use these IPv6 address ranges.
  * A realm named `byoip-ipv4` that contains the following:

    * IPv4 BYOIP public advertised prefixes.
    * IPv4 BYOIP public delegated prefixes.
    * Static external IPv4 addresses that are reserved from a public delegated prefix.
    * Instances that use ephemeral external IPv4 addresses that are created from a public delegated prefix.

If an instance uses a static external IPv4 address that is reserved from a public delegated prefix, the instance is listed in the `google-owned-ipv4` realm instead of the `byoip-ipv4` realm . For more information, see Limitations.

  * A realm named `byoip-ipv6` that contains the following:

    * IPv6 BYOIP public advertised prefixes.
    * IPv6 BYOIP public delegated prefixes.
    * External or internal IPv6 subnet ranges that are created from a public delegated prefix.
    * Ephemeral and static external IPv6 address ranges that are created from a public delegated prefix.
    * Instances that use ephemeral or static IPv6 address ranges that are created from a public delegated prefix.



## Limitations

The following limitations apply to Cloud Number Registry:

  * Cloud Number Registry is configured in the designated project, but contains a read-only representation of IP address range information for the whole organization. To control access to the organization's IP address information, you must control access to the designated project. For more information, see Project designation for Cloud Number Registry.

  * [Internal ranges](https://docs.cloud.google.com/vpc/docs/internal-ranges) aren't discovered.

  * If you use bring your own IP addresses (BYOIP), and have reserved an external IPv4 address from a public delegated prefix, and have assigned that static IP address to an instance, the discovered ranges are split across two realms instead of the same realm:

    * The discovered range for the instance is displayed under the `google-owned-ipv4` realm.
    * The discovered range for the static external IPv4 address is displayed under the public advertised prefix realm.



## What's next

  * [Designate a project to use for Cloud Number Registry](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
