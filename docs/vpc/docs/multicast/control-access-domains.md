---
url: https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains/
title: Control access to multicast domains \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:45.445711+00:00
---

# Control access to multicast domains  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control access to multicast domains

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to control access to multicast domains.

If you configured a multicast domain with the Network Connectivity Center (NCC) star topology, then you can control multicast consumer access by accepting or rejecting the VPC spoke that is associated with a multicast consumer network.

For more information, see [Hub administration overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin) in the NCC documentation.

## Grant users the ability to propose VPC spokes

To grant multicast consumer network administrators the ability to propose VPC spokes to the hub, see [Manage access to create spokes in hubs across projects](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access#manage_access_to_create_spokes_in_hubs_across_projects). You retain full control over which spokes are accepted into the hub. Spokes don't become active until you explicitly accept them.

Multicast consumer network administrators require the ability to propose spokes when they follow the procedure to [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network).

## Review proposed VPC spokes

To review VPC spokes that multicast consumer network administrators have proposed from different projects, see [View proposals pending review](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#view_proposals_pending_review).

## Accept a VPC spoke

To grant a multicast consumer VPC network access to the multicast domain, accept the VPC spoke that is associated with the consumer VPC network. To learn more, see [Accept a spoke proposal](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#accept_a_spoke_proposal).

You can also set up _auto-accept_ projects for [spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#spoke-groups) in a hub. Auto-accept lets you automatically accept into the hub any spokes that are in auto-accept projects, without having to review each spoke proposal.

## Reject a VPC spoke

To revoke a multicast consumer VPC network's access to the multicast domain, reject the VPC spoke that is associated with the multicast consumer VPC network. To learn more, see [Reject a spoke proposal](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#reject-a-spoke-proposal).

Rejecting a VPC spoke associated with a multicast consumer network does the following:

  * The multicast consumer VPC network loses both unicast and multicast connectivity.
  * If there are multicast consumer configurations between the multicast consumer network and any domain that was created by using the NCC hub, then Google Cloud deactivates those multicast consumer resources and assigns them a status of `INACTIVE`. The multicast consumer resources still exist in the multicast consumer project, but they are no longer usable.



If you want to restore access after rejection, you can accept the spoke again, which does the following:

  * Restores unicast connectivity immediately.
  * Lets the multicast consumer network administrator re-establish multicast connectivity after they do the following: 
    * Delete their existing multicast consumer configurations that are marked as `INACTIVE`.
    * Create new multicast consumer configurations (both consumer associations and group consumer activations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
