---
url: https://docs.cloud.google.com/compute/docs/instances/
title: Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:35.058424+00:00
---

# Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Compute Engine instances. A Compute Engine instance can be either a virtual machine (VM) or bare metal instance that is hosted on Google's infrastructure. You can [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) or [create a group of managed instances (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) by using the Google Cloud console, the Google Cloud CLI, or the Compute Engine API. 

## Introduction

The terms _Compute Engine instance_ , _compute instance_ or _instance_ are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

  * If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
  * Otherwise, an instance is a VM instance. The terms _virtual machine instance_ , _VM instance_ , and _VM_ are synonymous.



Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

Compute Engine instances can run the [public images](https://docs.cloud.google.com/compute/docs/images) for Linux and Windows Server that Google provides as well as private custom images that you can [create](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) or [import from your existing systems](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks). You can also [deploy Docker containers](https://docs.cloud.google.com/compute/docs/containers/deploying-containers), which are automatically launched on instances running the [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) public image.

You can choose the machine properties of your instances, such as the number of virtual CPUs and the amount of memory, by using a set of [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource) or by creating your own [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

## Instances and projects

Each instance belongs to a [Google Cloud console](https://console.cloud.google.com/) project, and a project can have one or more instances. When you create an instance in a project, you specify the zone, operating system, and machine type of that instance. When you delete an instance, it is removed from the project.

## Instances and storage options

By default, each Compute Engine instance has a small boot disk that contains the operating system. You can add more disks to the instance when you create it, and you can add disks to an instance while the instance is running. For more information about disks in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

## Instances and networks

Each network interface of a Compute Engine instance is associated with a subnet of a unique VPC network. For more information about VPCs, see [Network overview](https://docs.cloud.google.com/compute/docs/networking/network-overview) and [VPC quotas](https://docs.cloud.google.com/vpc/docs/quota).

## Instances and containers

Compute Engine instances support a declarative method for launching your applications using [containers](https://cloud.google.com/containers). When creating an instance or an instance template, you can provide a Docker image name and launch configuration. Compute Engine takes care of the rest including supplying an up-to-date [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) image with Docker installed and launching your container when the instance starts. For more information, see [Deploying containers on instances and MIGs](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).

## Tools to manage instances

To create and manage instances, you can use a variety of tools, including the [Google Cloud console](https://console.cloud.google.com/), the [`gcloud`](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest). To configure applications on your instances, [connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) using Secure Shell (SSH) for Linux instances or Remote Desktop Protocol (RDP) for Windows Server instances.

## Managing access to your instances

You can manage access to your instances using one of the following methods:

  * Linux instances: 
    * [Managing instance access using OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access), which allows you to associate SSH keys with your Google Account or Google Workspace account and manage admin or non-admin access to your instance through IAM roles.
    * [Manage your SSH keys in project or instance metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata), which uses public SSH keys stored in Compute Engine metadata to grant access to the instance. You can use SSH keys stored in project metadata to access all instances in a project. You can use SSH keys stored in instance metadata to access individual instances.
    * If you [connect to your instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools) using the Google Cloud CLI or SSH from the console, Compute Engine automatically generates SSH keys for you.
  * Windows Server instances: 
    * [Generate credentials for Windows instances](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials), which associates a password with a Windows user. Windows instances use this information to authenticate access to the instance.



## Accessing your instances

After you configure access to your instances, you can use one of many options to [connect to your Linux instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) or [connect to your Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

## Default time zone for compute instances

Regardless of the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create your instance, the default time for your instance is Coordinated Universal Time (UTC).

## What's next

  * If you are new to Compute Engine, see [Create a Linux instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) to learn how to create an instance using the Google Cloud console.

  * For a more detailed guide to create an instance, see [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  * For more information about the features of Compute Engine instances, see the following:

    * [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource)

    * [Operating system images](https://docs.cloud.google.com/compute/docs/images)

    * [Networking overview for instances](https://docs.cloud.google.com/compute/docs/networking/network-overview)

    * [Choose a deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option)

  * Learn how to [create a MIG from an existing instance](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm).




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
