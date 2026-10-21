---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview/
title: BGP route policies overview \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:20.916691+00:00
---

# BGP route policies overview  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BGP route policies overview

This guide is an overview to Cloud Router Border Gateway Protocol (BGP) route policies.

BGP route policies let you set rules to filter BGP routes or modify BGP route attributes. You can apply BGP route policies to both learned and advertised routes. You use the Common Expression Language (CEL) to define the BGP route policies to apply to your BGP routes.

You can apply BGP route policies to learned routes or advertised routes on Cloud Router for BGP sessions. BGP route policies are separate from policy-based routes.

Policy-based routes are applied to Virtual Private Cloud networks by assigning a next-hop route that is based on a per-example source address, which might be unrelated to the destination address. For more information, see [Policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes).

**Note:** BGP route policies are not supported for [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes). BGP route policies are only supported for routes learned directly from the BGP peer.

We recommend using BGP route policies within a test environment to verify your configuration prior to rolling your configuration out to your production environment.

## What are BGP route policies?

BGP route policies are defined as an ordered list of terms. Each term is evaluated in the order that you specify, and include both a condition and a corresponding action for when a route matches that term. A particular BGP route policy can be applied only in one direction, either inbound for learned routes, or outbound for advertised routes, but not both simultaneously. However, BGP route policies can be applied to multiple BGP peers on Cloud Router.

You can create named sets for BGP route policies for either communities or for BGP prefixes. Each named set can be referenced by any number of the policies that are defined on the same Cloud Router. Named sets are unique to each Cloud Router and are used to group together expressions of one type, allowing them to be managed or referenced as a single entity.

## BGP route policies use cases

You can use BGP route policies to control which BGP routes are accepted, rejected, or modified before the BGP routes are advertised to other BGP peers or imported to the VPC routing table.

The following are example use cases for BGP route policies:

  * **Modifying the best-preferred BGP route** : You can use BGP route policies to modify the best-preferred BGP route, which is helpful for influencing the path that traffic takes through a network. For example, you can use BGP route policies to help ensure that BGP routes from a particular peer are preferred over other BGP routes by changing the value of the BGP MED attribute.

  * **Filtering unwanted BGP routes** : You can use BGP route policies to filter unwanted learned routes, or to avoid advertising particular routes to BGP peers. This is useful to prevent routing loops or routes that send traffic through undesirable paths. For example, you can use BGP route policies to filter prefixes within a subnet.

  * **Meeting traffic engineering goals** : You can use BGP route policies to meet specific traffic engineering goals. To influence traffic distribution, prepend one or more values to a route's AS-PATH. For example, for a prefix `192.168.2.0/24`, Cloud Router learns the prefix from two peers but learns different AS-PATH values from each peer. So `peer1` might provide an AS-PATH value of `[1010]` and `peer2` might provide an AS-PATH value of `[2020]`. With BGP route policies, you can choose to add one or more values to the front of the AS-PATH value.




## How BGP route policies are applied

You apply BGP route policies to BGP configurations on a Cloud Router. Each BGP peer has zero or more route import and export policies applied to it. Import route policies apply to learned routes, and export route policies apply to advertised routes.

The following diagram shows route import policies for learned routes, and route export policies for advertised routes:

[ ![BGP import policy and export policy directions.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-policy-import-export.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-policy-import-export.svg) BGP import policy and export policy directions (click to enlarge).

The following describes the general rules that Cloud Router follows when applying BGP route policies:

  * BGP route policies are evaluated in the order that you list.

  * Terms in each BGP route policy are evaluated in the order of specified priority.

  * Terms can modify BGP routes. A subsequent term can modify a BGP route made by a previous term.

  * Evaluation ends when a BGP route is accepted or dropped. BGP routes are accepted if all policies and terms are evaluated and the route isn't dropped.

  * Terms aren't evaluated twice for a route in a single exercise of a BGP route policy.




BGP route policy evaluation defaults to fail open. In other words, routes that aren't explicitly dropped are accepted during BGP route policy evaluation. You can't change this behavior directly, but you can create a "drop all" policy that you apply to your last peering, in effect creating a fail closed BGP route policy.

The following diagram shows how a set of applied policies for a route is evaluated:

[ ![BGP route policy processing.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-policy-process.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/route-policy-process.svg) BGP route policy processing (click to enlarge).

## BGP communities and Cloud Router

A community value is a 32-bit field divided into two 16-bit sections. Conventionally, the first 16-bits of the value encode the autonomous system (AS) number of the network originating the community, but Cloud Router doesn't enforce this convention. The second 16-bits of the value encode a unique number assigned by the originating AS.

BGP route policies can match and act on standard BGP communities attributes. BGP route policies can't match or modify the extended communities attributes.

The Cloud Router route selection process doesn't use the BGP communities attribute on prefixes. For example, it doesn't honor the `NO_EXPORT` or the `NO_ADVERTISE` BGP communities.

After BGP route policies are imported, Cloud Router drops BGP communities from learned routes, which means that Cloud Router doesn't re-advertise communities—that is, Cloud Router treats communities as a non-transitive attribute. BGP communities can only be used to influence Cloud Router ingress match policies. You can add, remove, or replace BGP communities on advertised routes to influence what your peer router does.

Because Cloud Router doesn't recognize well-known communities, you must use literal values for BGP well-known communities, such as `65535:65281` for `NO_EXPORT` or `65535:65282` for `NO_ADVERTISE`.

## Relationships between BGP route policy resources

Each Cloud Router maintains its own list of BGP peers, BGP route policies, and BGP named sets. BGP peers that belong to a Cloud Router resource can reference BGP route policies by name if those policies are defined on the Cloud Router. Similarly, the BGP route policies that belong to a Cloud Router resource can reference BGP named sets by name if those named sets are defined on the Cloud Router.

You can create, modify, and delete BGP route policies as long as the parent Cloud Router exists.

## Interactions with other Cloud Router features

The following sections describe how BGP route policies interact with other Cloud Router features.

Custom advertised routes
    Export BGP route policies can drop or modify [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) before they're advertised to BGP peers. BGP route policies can't match or modify custom learned routes.
Prefix limits
    

The limit of prefixes that Cloud Router accepts from a peer is 5000. If a peer advertises more than 5000 prefixes, Cloud Router resets the BGP session.

The prefix limit is applied to learned routes before BGP route policies are applied, so using BGP route policies doesn't change this behavior.

Subnets
    

Export BGP route policies can filter or modify [Virtual Private Cloud subnets](https://docs.cloud.google.com/vpc/docs/subnets) subnet routes before they're advertised to BGP peers.

Transit routes
    

BGP route policies can modify transit routes.

Cloud Router doesn't honor the behavior of the `NO_EXPORT` and `NO_ADVERTISED` BGP communities.

## What's next

  * [Create BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-policies)
  * [Create named sets](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-named-sets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
