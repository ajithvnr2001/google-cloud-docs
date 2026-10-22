---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets/
title: Bring your own IP addresses with external subnets \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:45.580130+00:00
---

# Bring your own IP addresses with external subnets  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Bring your own IP addresses with external subnets Stay organized with collections  Save and categorize content based on your preferences. 

Manage IP resources in your organization's Data Network Segment to support external networking requirements. To ensure that external services like egress network address translation (NAT) and external load balancers have enough IP addresses to connect to networks outside your organization, you must add external subnets.

If the Data Network Segment IP addresses are used up, reach out to your infrastructure operator (IO) to scale up your IP addresses.

For an overview of subnets and their concepts, see [Subnets and IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview).

This document is for platform administrators and application operators who are responsible for managing network traffic for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To get the permission that you need to create subnets, ask your Organization IAM Admin to grant you the Subnet Org Admin (`subnet-org-admin`) IAM role. This role is not bound to a namespace.

## Create a leaf subnet for an individual service

To allocate a single IP address for your service, you must create a leaf subnet. This leaf subnet must have the field value `type: Leaf` and must reside in the same project namespace as your external service.

Your leaf subnet must be configured with a `prefixLength` value of `32`, because it's intended to allocate a single IP address. The `parentReference` value references a previously allocated subnet.

  * In a terminal window, create the leaf subnet in the management API server:
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f - <<EOF
        apiVersion: ipam.gdc.goog/v1
        kind: Subnet
        metadata:
          labels:
            ipam.gdc.goog/allocation-preference: default
            ipam.gdc.goog/network-segment: data
          name: SUBNET_NAME
          namespace: PROJECT_NAMESPACE
        spec:
          ipv4Request:
            prefixLength: 32
          parentReference:
            name: PARENT_SUBNET
            namespace: platform
          type: Leaf
        EOF
        

Replace the following:

    * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of your management API server. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).
    * `SUBNET_NAME`: the name for the leaf subnet.
    * `PROJECT_NAMESPACE`: the project namespace corresponding to your project where your services are located.
    * `PARENT_SUBNET`: the name of the parent subnet that this leaf subnet will source its IP address from.



Your individual IP address is now available for use by your external service. For more information about how to configure the IP address for your service, see the corresponding service documentation, such as [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service).

## What's next

  * [Subnets and IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview)
  * [Networking overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview)
  * [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
