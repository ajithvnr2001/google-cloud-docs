---
url: https://docs.cloud.google.com/compute/docs/instance-templates/
title: Instance templates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:46.992333+00:00
---

# Instance templates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Instance templates Stay organized with collections  Save and categorize content based on your preferences. 

This document describes what an instance template is, when to use an instance template, and what a deterministic instance template is. It also provides a comparison between regional and global instance templates.

An instance template is a convenient way to save a virtual machine (VM) instance's configuration that includes machine type, boot disk image, labels, startup script, and other VM properties.

You can use an instance template to do the following:

  * Create [individual VMs](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).

  * Create VMs in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

  * Create [reservations for VMs](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).




To learn how to create an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## When to use instance templates

Use instance templates any time you want to quickly create VMs or reservations for VMs based off of a pre-existing VM property. If you want to create a group of identical VMs (a MIG), then you must create the MIG using an instance template.

## How to update instance templates

Instance templates are designed to create VMs with identical configurations. You can't update instance templates after they're created. Instead, do one of the following:

  * Create a new instance template as follows:

    * [Create an instance template based on an existing VM](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance).

    * [Create an instance template based on an existing template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-template).

  * [Create VMs while overriding the instance template's properties](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template#creating_a_vm_instance_from_an_instance_template_with_overrides).




## Use deterministic instance templates to ensure identical VMs

Deterministic instance templates make explicitly clear the type of third-party services or apps to install on your VMs. This helps to ensure that your instance template always creates VMs with an identical configuration. For example, if your template has a startup script that fetches an app, you can specify the version of the app that you want in your template's startup script.

For more information, see [Deterministic instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates).

## Regional and global instance templates

Instance templates are available both as [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) and [global resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#globalresources). Unless you need to reuse an instance template across multiple regions, Google recommends using regional instance templates over global instance templates.

The following table provides a comparison between regional and global instance templates:

| Regional instance template | Global instance template  
---|---|---  
**Scope** | You can use the template only in the template's region. | You can use the template in any region.  
**Reliability** | Hardware errors are isolated to the template's region. | Hardware errors can impact any region where the template is used.  
**Use case** | 

  * Reduce cross-region dependency.
  * Achieve data residency in a region. For example, to meet compliance requirements on the physical location of the data.

| Reuse your global instance template to create VMs, MIGs, and reservations across multiple regions.  
  
### Use of zonal or regional resources in instance templates

In an instance template, you might specify zonal resources, which restricts the use of that template to the zone where that resource resides. Similarly, if you specify a regional resource in a global instance template, the template is restricted to that region. For example, if you include a read-only Persistent Disk from `us-central1-a` in your instance template, you can't use that template in any other zone because that specific Persistent Disk exists only in zone `us-central1-a`.

For more information about zonal resources, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

## How to specify instance templates

When creating resources that are based on an instance template, depending on the interface that you're using, you might need to specify the full or partial URL of the instance template—for example:

  * Full URL: `https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/instanceTemplates/1234567890`
  * Partial URL: `projects/example-project/regions/us-central1/instanceTemplates/1234567890`



You can specify either the ID or the name of the instance template. Google recommends that you specify the ID because, unlike names, instance template IDs can't be reused. This approach helps to ensure that the resources that you create from the template have the properties that you intend.

To view the template ID of an instance, see [Get information about an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template).

## Pricing

There is no additional charge for using instance templates. You are charged for the resources that you create based on the templates.

For Compute Engine pricing information, see [Pricing](https://cloud.google.com/compute/all-pricing). 

## What's next

  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) from scratch, based on an existing instance, or based on an existing instance template.

  * Use an instance template to [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).

  * Use an instance template to [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) or [update an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

  * Use an instance template to [create a reservation for VMs](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
