---
url: https://docs.cloud.google.com/docs/overview/
title: Google Cloud overview \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:22.316473+00:00
---

# Google Cloud overview  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Google Cloud overview Stay organized with collections  Save and categorize content based on your preferences. 

This overview is designed to help you understand the overall landscape of Google Cloud. You'll learn about how Google Cloud is structured, how its functionality is provided as services, and the different ways that you can interact with it when designing, creating, and running your applications.

As you explore the rest of this Get started section, you'll learn more about Google Cloud's tooling and resources, and how to get started creating and managing your own applications on Google Cloud.

For general information on cloud computing, see [Advantages and disadvantages of cloud computing](https://cloud.google.com/learn/advantages-of-cloud-computing).

## Universes, regions, and zones

Underlying everything you do with Google Cloud technology are the physical machines that run your workloads and Google Cloud services. These machines live in data centers, and are logically structured into universes, regions, and zones.

At the top of this hierarchy is the _universe_. A universe is a fully self-contained cloud, with its own networking that is separate from the public internet and other universes. Google Cloud is the original universe, with resources in data centers all over the world. There are also other universes, based on the same technology as Google Cloud but with all their resources in a single jurisdiction and running in partner-operated datacenters. These self-contained smaller clouds are created as part of a program called Google Cloud Dedicated and provide strong data and operational sovereignty guarantees for users whose workloads require them.

Within each universe there are geographic _regions_. Google Cloud has regions in Asia, Australia, Europe, Africa, the Middle East, North America, and South America.

Finally, regions are divided into _zones_. Each zone is identified by a name that combines a letter identifier with the name of the region. For example, zone `a` in the East Asia region is named `asia-east1-a`. Zones have high-bandwidth, low-latency network connections to other zones in the same region.

This distribution of resources in a universe into regions and zones provides several benefits, including redundancy in case of failure and reduced latency by locating resources closer to clients. This distribution also introduces some rules about how resources can be used together.

## Global, regional, and zonal resources

Some resources can be accessed by any other resource in their universe, across regions and zones. These _global resources_ include preconfigured disk images, disk snapshots, and networks. Some resources can be accessed only by resources that are located in the same region. These _regional resources_ include static external IP addresses. Other resources can be accessed only by resources that are located in the same zone. These _zonal resources_ include VM instances, their types, and disks.

The following diagram shows the relationship between global scope, regions and zones, and some of their resources:

![A global network can contain region-specific resources such as IP
         addresses and zone-specific resources such as VMs and disks.](https://docs.cloud.google.com/static/docs/images/overview/regions-zones.svg)

The scope of an operation varies depending on what kind of resources you're working with. For example, creating a network is a global operation because a network is a global resource, while reserving an IP address is a regional operation because the address is a regional resource.

As you start to design and optimize your Google Cloud applications, it's important to understand how these regions and zones interact. For example, even if you could, you wouldn't want to attach a disk in one region to a computer in a different region because the latency you'd introduce would make for poor performance. Thankfully, Google Cloud won't let you do that; disks can only be attached to computers in the same zone.

Depending on the level of self-management required for the [computing and hosting service](https://docs.cloud.google.com/docs/overview/cloud-platform-services#computing-hosting) you choose, you might or might not need to think about how and where resources are allocated.

For more information about the geographical distribution of Google Cloud, see [Geography and Regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Accessing resources through services

In cloud computing, what you might be used to thinking of as software and hardware products, become _services_. These services provide access to the underlying resources, letting you add a wide range of functionality—from managed Kubernetes to data storage—to your applications. You can see the list of available Google Cloud services in our [product list](https://cloud.google.com/products/).

When you develop your website or application on Google Cloud, you mix and match these services into combinations that provide the infrastructure you need, and then add your code to enable the scenarios you want to build.

## Projects

Any Google Cloud resources that you allocate and use must belong to a project. You can think of a project as the organizing entity for what you're building. A project is made up of the settings, permissions, and other metadata that describe your applications. Resources within a single project can work together easily, for example by communicating through an internal network, subject to the regions-and-zones rules. A project can't access another project's resources unless you use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

Each Google Cloud project has the following:

  * A project name, which you provide.
  * A project ID, which you can provide or Google Cloud can provide for you.
  * A project number, which Google Cloud provides.



So, for example, the same project might have:

  * The project name **Example Project**
  * The project ID **example-id**
  * The project number **123456789012**



As you work with Google Cloud, you use these identifiers in commands and API calls. For example, you might specify that you want to use the project as your default for the Google Cloud CLI with the following command:
    
    
    gcloud config set project example-id
    

You can create multiple projects and use them to separate your work in whatever way makes sense for you and your organization. For example, you might have one project that can be accessed by all team members and a separate project that can only be accessed by certain team members.

A project serves as a namespace. This means every resource within each project must have a unique name, but you can usually reuse resource names if they are in separate projects. Some resource names must be unique within Google Cloud. Refer to the documentation for the resource for details.

Each project is associated with one billing account. Multiple projects can have their resource usage billed to the same account.

For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

## Interacting with Google Cloud

There are multiple ways to interact with resources and services in Google Cloud, including the following:

  * The [Google Cloud console](https://console.cloud.google.com/) provides a web-based, graphical user interface that you can use to manage your Google Cloud projects and resources.
  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) lets you manage development workflow and Google Cloud resources directly from the command line. For example, you can create a Compute Engine virtual machine (VM) instance by running the `gcloud compute instances create` command in your shell environment. You can choose between installing the Google Cloud CLI on your local machine, or using it in [Cloud Shell](https://docs.cloud.google.com/shell/docs/features), a convenient browser-based shell that you can access from the Google Cloud console and which has many tools pre-installed.
  * Our provided [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) help you to interact with services programmatically in a variety of popular languages. Cloud Client Libraries provide an optimized developer experience by using each supported language's natural conventions and styles. They also reduce the boilerplate code you have to write because they're designed to enable you to work with service metaphors in mind, rather than implementation details or service API concepts.
  * You can use an "infrastructure as code" (IaC) approach by using [Terraform](https://docs.cloud.google.com/docs/terraform) and the Google Cloud Terraform provider.



You can learn more in [Interacting with Google Cloud](https://docs.cloud.google.com/docs/get-started/interact-with-resources).

## Pricing

To learn how to explore and evaluate Google Cloud at no cost, see [Free Google Cloud features and trial offer](https://docs.cloud.google.com/free/docs/free-cloud-features).

To browse pricing details for individual services, see the [price list](https://cloud.google.com/pricing/list).

To estimate your total costs for running a specific workload on Google Cloud, see the [pricing calculator](https://cloud.google.com/products/calculator).

## What's next

  * Visit [Get started with Google Cloud](https://docs.cloud.google.com/docs/get-started) to explore setup paths and resources for IT administrators, security engineers, application developers, and more.
  * Delve deeper into [interacting with Google Cloud](https://docs.cloud.google.com/docs/get-started/interact-with-resources).
  * For administrators of new organizations on Google Cloud, our [Google Cloud Setup](https://docs.cloud.google.com/docs/enterprise/cloud-setup) guided flow helps you build a robust foundation for your organization's workloads that embodies best practices for enterprise infrastructure.



##  Try Google Cloud 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
