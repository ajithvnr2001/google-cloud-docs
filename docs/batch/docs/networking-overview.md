---
url: https://docs.cloud.google.com/batch/docs/networking-overview/
title: Batch networking overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:23.766963+00:00
---

# Batch networking overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/networking-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Batch networking overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains networking concepts for Batch, including networking options, when to configure networking, and how networking works.

## Networking options

Networking options control how Batch is connected with other sources, such as the internet and other Google Cloud resources and services.

Batch has the following networking options:

  * Specify the network for a job or use the default network.
  * Use additional networking restrictions: 
    * Block external connections for job runtime environments, either all VMs or specific containers.
    * Protect Batch resources and data by using VPC Service Controls.



For more information about determining which networking options to use for Batch, see When to configure networking in this document. For more information about the networking concepts for each option, see How networking works in this document.

## When to configure networking

Review this section to determine whether to configure networking when using Batch or use the default networking configuration.

You must configure networking for Batch in the following cases:

**Note:** If you aren't sure which of the following organization policies have been enabled for your project or organization, you or an administrator can [view your organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

  * If your project or network uses VPC Service Controls to restrict networking access for Batch, you must configure networking by following the [Use VPC Service Controls with Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls) documentation.
  * If the `compute.vmExternalIpAccess` organization policy constraint requires your project to create VMs without external IP addresses or if your network uses [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), you must [Create jobs that block external access for all VMs](https://docs.cloud.google.com/batch/docs/job-without-external-access).
  * If you cannot or do not want to use the default network, you must [Specify the network for jobs](https://docs.cloud.google.com/batch/docs/specify-job-network).

To determine if you can use the default network for a job, verify the following:

    * The default network exists for your project. New Google Cloud projects automatically include the default network unless the `compute.skipDefaultNetworkCreation` organization policy constraint is enabled.
    * The default network supports any specific networking requirements that you have. Notably, if the default network for your project is modified, you or other users might encounter issues. If you need more information about the default network, see Default networking configuration in this document.



Even if it's not required, you might want to configure networking to improve security for your Batch resources and data. For example, if you want to improve security for jobs that use containers and do not block external access for all VMs, you can optionally [Create jobs that block external access for only one or more containers](https://docs.cloud.google.com/batch/docs/job-without-external-access). Using a non-default network or additional networking restrictions can help you implement [least-privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) principles. For more information about options you can use to configure networking for Batch, see How networking works in this document.

Otherwise, if you don't need or want to configure networking, you can create a job without specifying any networking options to use the default networking configuration.

## How networking works

The following sections explain networking concepts for Batch:

  * Job network
  * Additional networking restrictions
  * Default networking configuration



### Job network

Every job runs on Compute Engine virtual machines (VMs), which must be part of a Google Cloud Virtual Private Cloud (VPC) network and a subnet of that network.

_VPC networks_ connect VMs to other sources, such as the internet and other Google Cloud resources and services. Each network consists of at least one _subnetwork_ , also known as a _subnet_ , which is one or more ranges of [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses) that is associated with a [region](https://docs.cloud.google.com/batch/docs/locations). Each VM has a network interface with an internal IP address and an optional external IP address that are allocated from the subnet. You can configure _VPC firewall rules_ to allow or deny connections for the VMs in a network. Every network has implied firewall rules that block all incoming connections and allow all outgoing connections. Typically, a VPC network can only be used within its project, but if you want to use the same network across multiple projects, you can use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

In summary, every job runs on VMs that each use IP addresses to make connections that are controlled by the firewall rules for the network.

For more information about networking concepts, see [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview) in the Compute Engine documentation and [Virtual Private Cloud (VPC) overview](https://docs.cloud.google.com/vpc/docs/overview) in the VPC documentation.

### Additional networking restrictions

To help improve security, a networking configuration might involve more restrictions than only the firewall rules for its network. For example, your project or organization can use [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints) or other Google Cloud services to restrict networking.

The following sections explain common options to further restrict networking:

  * Block external connections for job runtime environments
  * Restrict networking access for Batch by using VPC Service Controls



#### Block external connections for job runtime environments

You can block external connections directly to and from the runtime environment for a job by using up to one of the following options:

  * **Block external access for all the VMs for a job.** Block external access for a job's VMs to create a job that runs on VMs without external IP addresses. This option is often required for a network or project or optionally used to improve security.

VMs without external IP addresses can only be accessed through their internal IP addresses by another node on the same network, so you need to configure access to these VMs by doing the following:

    * To run a job on VMs without external IP addresses, use [Cloud NAT](https://docs.cloud.google.com/nat/docs/gce-example#create-nat) or [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) to allow access to the domains for the APIs and services that your job uses. For example, all Batch jobs use the Batch and Compute Engine APIs and very often use the Cloud Logging API.

    * If you or other users need to connect to VMs without external IP addresses, see [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip) in the Compute Engine documentation.

  * **Block external access for one or more containers for a job.** If a job uses containers and does not already block external access for all its VMs, you can choose if you want to block external access for each container. This option is optional; it can be used to improve security when you specify the network for a job or when you create a job that uses the default networking configuration.




#### Protect Batch resources and data by using VPC Service Controls

In addition to blocking external access for all the VMs for a job, you can optionally further restrict networking by using VPC Service Controls.

Unlike the other networking options explained in this document, which can restrict networking only for the VMs or containers that run jobs, VPC Service Controls lets you restrict networking access for the resources and data for Google Cloud services—for example, Batch jobs and data.

You can use VPC Service Controls to create perimeters that protect the resources and data of Google Cloud services that you specify. The service perimeter isolates the selected services and resources, blocking connections with Google Cloud services outside the perimeter and any connections from the internet that are not explicitly allowed. For more information, see the [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview#capabilities) documentation and [Use VPC Service Controls with Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls).

### Default networking configuration

When you create a job and don't specify any networking options, the job's VMs use the default network and the subnet for the VM's [location](https://docs.cloud.google.com/batch/docs/locations).

Each project has a default network named `default` unless you delete it or disable this by using the `compute.skipDefaultNetworkCreation` organization policy constraint. The default network is an [auto mode network](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations), so it has one subnet in each region. In addition to the implied firewall rules for every network, the `default` network also has pre-populated firewall rules, which allow access for common use cases. For more information, see [Pre-populated rules in the default network](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) in the VPC documentation.

Consider using the default networking configuration if you don't have any networking requirements for a job and don't want to configure networking. For details about when to use the default networking configuration, see When to configure networking in this document.

## What's next

  * Configure networking for Batch: 
    * [Specify the network for a job](https://docs.cloud.google.com/batch/docs/specify-job-network)
    * [Block external access for a job](https://docs.cloud.google.com/batch/docs/job-without-external-access)
    * [Use VPC Service Controls with Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls)
  * Alternatively, to create a job that uses default networking configuration, see [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job).
  * You can also control access for a job by [using a custom service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
