---
url: https://docs.cloud.google.com/compute/docs/naming-resources/
title: Naming resources \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:21.901858+00:00
---

# Naming resources  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/naming-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Naming resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the naming convention for Compute Engine resources.

Resources are the fundamental components that make up a Cloud service or product. For example, resources on Compute Engine include but are not limited to:

  * [Disks](https://docs.cloud.google.com/compute/docs/disks) and [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)
  * [Images and image families](https://docs.cloud.google.com/compute/docs/images)
  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)
  * [Instance groups](https://docs.cloud.google.com/compute/docs/instance-groups)
  * [Machine images](https://docs.cloud.google.com/compute/docs/machine-images)
  * [Node groups](https://docs.cloud.google.com/compute/docs/nodes) and [node templates](https://docs.cloud.google.com/compute/docs/nodes)
  * [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances)



To learn more about resources, see [Global, regional, and zonal resources documentation](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

## Naming convention

When you create a new resource on Compute Engine, you have to provide properties such as a name for the resource.

For resources on Compute Engine, the resource name must meet the following format (unless specified differently in the documentation for creating that resource):

  * Be 1-63 characters in length.
  * Comply with [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt) conventions.
  * Match the regular expression `^[a-z]([-a-z0-9]*[a-z0-9])?`. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits, except the last character, which cannot be a hyphen.



## Name uniqueness

In general, resource names must be unique within a location within a project. For example, an external IP address name must be unique within the region where it resides. However, you can reuse names across locations.

If the `vmDnsSetting` setting for the Compute Engine project resource isn't set to `ZonalOnly` then all VM names must be unique across the project. We _strongly recommend_ using the `vmDnsSetting:ZonalOnly` setting for your projects, not only so you can reuse VM names across zones and regions, but also because it offers higher reliability by isolating failures in the DNS registration to individual zones. For more information, see [Zonal DNS names](https://docs.cloud.google.com/compute/docs/networking/zonal-dns).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
