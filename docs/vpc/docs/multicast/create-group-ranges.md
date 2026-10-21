---
url: https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges/
title: Create multicast group ranges \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.972205+00:00
---

# Create multicast group ranges  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create multicast group ranges

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the steps that a multicast administrator must follow to create multicast group ranges.

For an overview of the configuration process for Cloud Multicast, see [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).

## Before you begin

A multicast group range must be associated with a specific multicast domain. Before you create a multicast group range, follow the steps to [create a multicast domain](https://docs.cloud.google.com/vpc/docs/multicast/create-domains).

## Create a multicast group range

This section describes how to create a multicast group range in a domain. You can repeat these steps to create multiple group ranges in a given domain.

### Create a group range

Associate a multicast group IP address range with the multicast domain.

###  gcloud 

  1. Reserve an internal range in the multicast administrator VPC network that contains the multicast group IP addresses that you want to use. To reserve an internal range, use the [`network-connectivity internal-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create).
         
         gcloud network-connectivity internal-ranges create INTERNAL_RANGE_NAME \
            --network=ADMIN_NETWORK \
            --ip-cidr-range=CIDR_RANGE
         

Replace the following values:

     * `INTERNAL_RANGE_NAME`: a name for the internal range to reserve
     * `ADMIN_NETWORK`: the name of the multicast administrator network
     * `CIDR_RANGE`: the CIDR range to reserve

The CIDR range that you specify must be a class D address (such as `224.0.0.0` \- `239.255.255.255`). Additionally, the total number of IP addresses in one or more multicast group ranges associated with the same domain can't exceed your quota for [Multicast groups per domain](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_groups_per_domain).

Fore more information about creating internal ranges, see [Create and use internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges).

  2. Create a multicast group range by using the internal range that you reserved. To create a multicast group range, use [`network-services multicast-group-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/create).
         
         gcloud network-services multicast-group-ranges create GROUP_RANGE_NAME \
            --multicast-domain="projects/ADMIN_PROJECT/locations/global/multicastDomains/DOMAIN_NAME" \
            --reserved-internal-range="projects/ADMIN_PROJECT/locations/global/internalRanges/INTERNAL_RANGE_NAME" \
            --location=global \
            [--require-explicit-accept ] \
            [--consumer-accept-list=CONSUMER_ACCEPT_LIST] \
            [--distribution-scope=DISTRIBUTION_SCOPE] \
            [--enable-logging | --no-enable-logging]
         

Replace the following values:

     * `GROUP_RANGE_NAME`: a name for the multicast group range
     * `DOMAIN_NAME`: the name of the multicast domain that you created previously
     * `ADMIN_PROJECT`: the ID of the multicast administrator project
     * `INTERNAL_RANGE_NAME`: the name of the internal range that you reserved previously
     * Specify the following properties for multicast traffic, group membership, and logging.

Except for the traffic distribution scope, you can [update each property](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#group-range) as needed at a later point in time.

       * `--require-explicit-accept`: determines which projects can use the multicast group range if the multicast consumer accept list is empty. This configuration determines whether a multicast consumer project can [Activate a multicast consumer VPC network for the group range](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#activate-consumer). 
         * To deny all projects, include this flag. A project can only use the group range if you add it to the multicast consumer accept list.
         * (Default) To allow all projects, exclude this flag. Any project that has access to the multicast domain can use the group range. In the Network Connectivity Center (NCC) star topology, you grant a project access to the domain by accepting it to the hub.
       * `CONSUMER_ACCEPT_LIST`: if you specified `--require-explicit-accept`, then you can enter list of multicast consumer projects that can use this multicast group range. If a multicast consumer project isn't in the accept list, then the project can't create multicast consumer configurations using this group range.

You can specify up to 100 projects by the project ID or name.

       * `DISTRIBUTION_SCOPE`: determines the location scope of multicast traffic. You can't update this property later.

         * To allow this range to send multicast traffic only within a zone, set this flag to `intra-zone`.
         * (Default) To allow this range to send multicast traffic across zones, set this flag to `intra-region`.
       * `--[no-]enable-logging`: determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled.

         * To enable logging, use `--enable-logging`.
         * (Default) To disable logging, use `--no-enable-logging`.



###  API 

  1. Reserve an internal range in the multicast administrator VPC network that contains the multicast group IP addresses that you want to use. To reserve an internal range, use the [`internalRanges.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/create).
         
         POST https://networkconnectivity.googleapis.com/v1/projects/ADMIN_PROJECT/locations/global/internalRanges?internalRangeId=INTERNAL_RANGE_NAME
         {
           "network": "projects/ADMIN_PROJECT/global/networks/ADMIN_NETWORK",
           "ipCidrRange": "CIDR_RANGE"
         }
         

Replace the following values:

     * `INTERNAL_RANGE_NAME`: a name for the internal range to reserve
     * `ADMIN_PROJECT`: the ID of the multicast administrator project
     * `ADMIN_NETWORK`: the name of the multicast administrator network
     * `CIDR_RANGE`: the CIDR range to reserve

The CIDR range that you specify must be a class D address (such as `224.0.0.0` \- `239.255.255.255`). Additionally, the total number of IP addresses in one or more multicast group ranges associated with the same domain can't exceed your quota for [Multicast groups per domain](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_groups_per_domain).

Fore more information about creating internal ranges, see [Create and use internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges).

  2. Create a multicast group range by using the internal range that you reserved. To create a multicast group range, use [`multicastGroupRanges.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/create).
         
         POST https://networkservices.googleapis.com/v1/projects/ADMIN_PROJECT/locations/global/multicastGroupRanges?multicastGroupRangeId=GROUP_RANGE_NAME
         {
           "multicastDomain": "projects/ADMIN_PROJECT/locations/global/multicastDomains/DOMAIN_NAME",
           "reservedInternalRange": "projects/ADMIN_PROJECT/locations/global/internalRanges/INTERNAL_RANGE_NAME",
           "requireExplicitAccept": "REQUIRE_EXPLICIT_ACCEPT",
           "consumerAcceptList": [
               "CONSUMER_ACCEPT_LIST"
           ],
           "distributionScope": "DISTRIBUTION_SCOPE",
           "logConfig": {
               "enabled": "LOGGING_ENABLED"
          }
         }
         

Replace the following values:

     * `GROUP_RANGE_NAME`: a name for the multicast group range
     * `ADMIN_PROJECT`: the ID of the multicast administrator project
     * `DOMAIN_NAME`: the name of the multicast domain that you created previously
     * `INTERNAL_RANGE_NAME`: the name of the internal range that you reserved previously

To specify properties for multicast traffic, group membership, and logging, include the following fields in request body. Except for the traffic distribution scope, you can [update each property](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#group-range) as needed at a later point in time.

     * `REQUIRE_EXPLICIT_ACCEPT`: determines which projects can use the multicast group range if `consumerAcceptList` is empty. This configuration determines whether a multicast consumer project can [Activate a multicast consumer VPC network for the group range](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#activate-consumer). 
       * To deny all projects, set to `true`. A project can only use the group range if you add it to `consumerAcceptList`.
       * (Default) To allow all projects, set to `false`. Any project that has access to the multicast domain can use the group range. In the NCC star topology, you grant a project access to the domain by accepting it to the hub.
     * `CONSUMER_ACCEPT_LIST`: if you set `requireExplicitAccept` to `true`, then you can enter list of multicast consumer projects that can use this multicast group range.

If a multicast consumer project isn't in the accept list, then the project can't create multicast consumer configurations using this group range.

You can specify up to 100 projects by the project ID or name. Use the following format: `"consumerAcceptList": ["project-1", "project-2"]`.

     * `DISTRIBUTION_SCOPE`: determines the location scope of multicast traffic. You can't update this property later.

       * To allow this range to send multicast traffic only within a zone, set to `INTRA_ZONE`.
       * (Default) To allow this range to send multicast traffic across zones, set to `INTRA_REGION`.
     * `LOGGING_ENABLED`: determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled.

       * To enable logging, set to `true`.
       * (Default) To disable logging, set to `false`.



### Activate the group range

Activate the group range in each zone where multicast producers or consumers need to use the associated group IP addresses.

If you don't activate a group range in a given zone, the associated group IP addresses can't be used to send or receive multicast traffic in the zone.

###  gcloud 

To activate a multicast group range, use the [`network-services multicast-group-range-activations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-range-activations/create).
    
    
      gcloud network-services multicast-group-range-activations create GROUP_RANGE_ACTIVATION_NAME \
         --multicast-domain-activation="projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME" \
         --multicast-group-range="projects/ADMIN_PROJECT/locations/global/multicastGroupRanges/GROUP_RANGE_NAME" \
         --location=ZONE \
         [--enable-logging | --no-enable-logging]
    

Replace the following values:

  * `GROUP_RANGE_ACTIVATION_NAME`: a name for the multicast group range activation
  * `ADMIN_PROJECT`: the project ID of the multicast administrator
  * `ZONE`: the zone in which to activate the group range. This must be a zone in which you previously activated the domain.
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that you created previously in this zone
  * `GROUP_RANGE_NAME`: the name of the group range that you created previously
  * `--[no-]enable-logging`: optional, determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled. Configuring this flag on a zonal group range activation overrides the setting for the global group range. 
    * To enable logging, use `--enable-logging`.
    * (Default) To disable logging, use `--no-enable-logging`.



###  API 

To activate a multicast group range, use the [`multicastGroupRangeActivations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/create).
    
    
    POST https://networkservices.googleapis.com/v1/projects/ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations?multicastGroupRangeActivationId=GROUP_RANGE_ACTIVATION_NAME
    {
        "multicastDomainActivation": "projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME",
        "multicastGroupRange": "projects/ADMIN_PROJECT/locations/global/multicastGroupRanges/GROUP_RANGE_NAME",
        "logConfig": {
              "enabled": "LOGGING_ENABLED"
        }
    }
    

Replace the following values:

  * `GROUP_RANGE_ACTIVATION_NAME`: a name for the multicast group range activation
  * `ADMIN_PROJECT`: the project ID of the multicast administrator
  * `ZONE`: the zone in which to activate the group range. This must be a zone in which you previously activated the domain.
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that you created previously in this zone
  * `GROUP_RANGE_NAME`: the name of the group range that you created previously
  * `LOGGING_ENABLED`: determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled. Configuring logging on a zonal group range activation overrides the setting for the global group range. 
    * To enable logging, set to `true`.
    * (Default) To disable logging, set to `false`.



## What's next

  * To view the multicast group range configurations that you created, see [View multicast group range configurations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-group-range-configs).
  * [Update multicast group range configurations](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#group-range)
  * [Enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
