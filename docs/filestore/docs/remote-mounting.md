---
url: https://docs.cloud.google.com/filestore/docs/remote-mounting/
title: Mounting file shares on remote clients \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:15.630200+00:00
---

# Mounting file shares on remote clients  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/remote-mounting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Mounting file shares on remote clients Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to mount a Filestore file share on clients in a remote network, such as:

  * Compute Engine VMs on a different project or VPC network.
  * On-premises clients on your local network.



## Establish a VPN connection between the remote network and the VPC network of the Filestore instance

Before you can mount a file share on a remote client, you must establish a VPN connection between the client's network and the VPC network of the Filestore instance.

  1. Create an HA VPN or a Classic VPN. For detailed instructions, see [Creating an HA VPN gateway to a Peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) or [Create a Classic VPN gateway using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).

Ensure that:

     * The subnet ranges of the client and the Filestore instance don't overlap.
     * The IP address of the Filestore instance is advertised as a custom route during BGP configuration.
     * You must use an external or third-party VPN provider.

For details, see [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues#mounting_over_vpn).

  2. Configure the VPN gateway and tunnel on the remote network:

     * For specific configuration guidance for certain VPN devices, see [VPN Interoperability Guides](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides).
     * For general configuration parameters, see [Configuring the Peer VPN Gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).



## Mount the Filestore file share on the remote client

Once the VPN connection is established, you can mount the file share on any client in the remote network using any of the [standard mounting methods](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).

If you use HA VPN or Cloud Interconnect and mount the file share to client VM that's running Linux kernel version 5, set the [`nconnect` mount option](https://man7.org/linux/man-pages/man5/nfs.5.html) to `1`. This setting prevents multiple connections to different Filestore backend nodes and ensures connection to mounted file shares.
    
    
       mount -o nconnect=1
    

## What's next

  * Learn more about creating [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * Learn more about creating [Filestore instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * Learn more about [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
