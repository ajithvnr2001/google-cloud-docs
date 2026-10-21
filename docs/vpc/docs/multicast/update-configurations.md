---
url: https://docs.cloud.google.com/vpc/docs/multicast/update-configurations/
title: Update multicast configurations \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.098704+00:00
---

# Update multicast configurations  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/update-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update multicast configurations

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to update existing multicast configurations for Cloud Multicast.

The procedures on this page assume that the corresponding configurations have been created as described in the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).

For information about deleting multicast configurations, see [Delete multicast configurations](https://docs.cloud.google.com/vpc/docs/multicast/delete-resources).

## Update multicast domain configurations

You can update existing multicast domain configurations in the following ways:

  * To control access to a multicast domain, see [Control access to multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains).

If you configured a multicast domain with the Network Connectivity Center (NCC) star topology, then you can control multicast consumer access by accepting or rejecting the VPC spoke that is associated with a multicast VPC consumer network.

  * To resize the infrastructure for your domain, see [Update multicast domain parameters](https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters).

You can resize the infrastructure for your domain by updating the traffic parameters of existing zonal multicast domain activations.

  * To activate an existing multicast domain in a new zone, see [Activate a multicast domain](https://docs.cloud.google.com/vpc/docs/multicast/create-domains#activate-domain).

Activate the domain in the new zone where multicast producers or consumers need to send or receive multicast traffic. When you activate a domain in a zone, Google Cloud provisions multicast infrastructure for your domain in that zone. Ensure that you also activate a [Activate a multicast group range](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges#activate_the_group_range) in the new zone.




## Update multicast group range configurations

You can update existing multicast group range configurations in the following ways:

  * To update which multicast consumer projects can use a multicast group range, see [Control access to multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/control-access-group-ranges).

  * To configure group membership event logging, see [Enable logging for a multicast group range](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs#enable-group).

You can configure logging on both the global multicast group range and a zonal multicast group range activation. Enabling logging lets you view logs for all multicast consumers of the group range.

  * To activate an existing multicast group range in a new zone, see [Activate a multicast group range](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges#activate_the_group_range).

Activate the group range in the new zone where multicast producers or consumers need to use the associated group IP addresses.

  * To add a new multicast group range to an existing domain, see [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges).




The distribution scope property of an existing multicast group range (`intra-zone` or `intra-region`) can't be updated.

## Update multicast producer configurations

You can update existing multicast producer configurations in the following ways:

  * To enable a VPC network to produce multicast traffic for a domain in a new zone, see [Add a multicast producer VPC network to a domain](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#create-producer).

Create a producer association between your VPC network and the domain in the new zone. Ensure that you also activate your network for a corresponding group range as described in the following list item.

  * To enable a VPC network to produce multicast traffic for a new group range, or for an existing group range in a new zone, see [Activate a multicast producer VPC network for a group range](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#activate-producer). Complete this procedure for each new multicast group range and zone in which you want to produce multicast traffic.

  * To create new multicast producers in an existing multicast producer VPC network, see the following:

    * For information about choosing a machine type, see [Machine considerations for multicast producer and consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).
    * For information about creating instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



## Update multicast consumer configurations

You can update existing multicast consumer configurations in the following ways:

  * To enable a VPC network to consume multicast traffic for a domain in a new zone, see [Add a multicast consumer VPC network to a domain](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#add-consumer).

Create a consumer association between your VPC network and the domain in the new zone. Ensure that you also activate the network for a corresponding group range as described in the following list item.

  * To enable a VPC network to consume multicast traffic for a new group range, or for an existing group range in a new zone, see [Activate a multicast consumer VPC network for a group range](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#activate-consumer). Complete this procedure for each new multicast group range and zone for which you want to consume multicast traffic.

  * To configure group membership event logging, see [Enable logging for a multicast group consumer activation](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs#enable-consumer).

You configure logging on the multicast group consumer activation. Enabling logging lets you view logs for multicast consumers in a specific multicast consumer VPC network and for a specific group range.

  * To create new multicast consumers in an existing multicast consumer VPC network, or to configure existing instances as multicast consumers, see the following:

    * For information about choosing a machine type, see [Machine considerations for multicast producer and consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).
    * For information about creating and configuring multicast consumer instances, see [Configure multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
