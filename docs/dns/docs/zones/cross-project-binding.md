---
url: https://docs.cloud.google.com/dns/docs/zones/cross-project-binding/
title: Create a zone with cross-project binding \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:44.234383+00:00
---

# Create a zone with cross-project binding  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/cross-project-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a zone with cross-project binding Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions about how to create a zone with cross-project binding enabled. For detailed background information, see [Cross-project binding](https://docs.cloud.google.com/dns/docs/zones/zones-overview#cross-project_binding).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.networks.bindPrivateDNSZone` on the project that owns the VPC network 
  * `dns.managedZones.create` on the project that owns the DNS zone 



**Roles**

  * `roles/dns.admin`



## Limitations

  * Your projects need to be in the same organization.
  * You cannot associate a zone to a VPC network in a project outside the organization.



## Set up cross-project binding

You can create a managed private zone that can be bound to a network that is owned by a different project within the same organization. Instead of specifying the network in the _same_ project, specify the URL of the network in _another_ project under the same organization.

Example: Suppose that you have two projects, _project A_ and _project B_. The VPC network is in _project A_. To make sure that all the VMs in that VPC network are able to resolve the DNS zones in _project B_ , follow these steps.

  1. To get the network URL, use the [`gcloud compute networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe) in _project A_ :
         
         gcloud compute networks describe NETWORK_NAME
         

Replace `NETWORK_NAME` with the name of the VPC network in _project A_.

Your output lists the network URL as `SelfLink`, which is the URL that you need. The output looks similar to the following:
         
         autoCreateSubnetworks: true
         creationTimestamp: '2021-08-11T14:07:16.454-07:00'
         description: Default network for the project
         id: '2485375699124847339'
         kind: compute#network
         name: default
         routingConfig:
          routingMode: REGIONAL
         selfLink: https://www.googleapis.com/compute/v1/projects/project-a/global/networks/default
         subnetworks:
         

  2. Create a private zone by running the [`dns managed-zones create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) in _project B_ , where you want to create or manage the DNS zone:
         
         gcloud dns managed-zones create NAME \
          --dns-name=DNS_SUFFIX \
          --description="Cross Project Binding" \
          --visibility=private \
          --networks=VPC_NETWORK
         

Replace the following:

     * `NAME`: a name for your zone
     * `DNS_SUFFIX`: the DNS suffix for your zone, such as `example.private`
     * `VPC_NETWORK`: the shared VPC URL that is authorized to query the zone from _project A_ , such as https://www.googleapis.com/compute/v1/projects/project-a/global/networks/default.

This creates a private zone in _project B_ where you want to create and manage the DNS zone. Your output is similar to the following:
    
    Created
    [https://dns.googleapis.com/dns/v1/projects/project-b/managedZones/my-zone].
    




## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
