---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bfd-interop/
title: Use third-party router configurations for BFD \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:51.851240+00:00
---

# Use third-party router configurations for BFD  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bfd-interop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use third-party router configurations for BFD

This page provides examples of third-party router configurations that support [Bidirectional Forwarding Detection (BFD) for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd).

## Arista EOS

To configure BFD on an Arista EOS, use the following command (the values shown are examples):
    
    
    int NAME
      bfd interval 1000 min_rx 1000 multiplier 5
    
    router bgp 65201
      neighbor 169.254.88.81 bfd
      neighbor 169.254.149.193 bfd
    

For additional Arista BFD configuration settings and examples, see [Section 37.2: BFD Configuration](https://www.arista.com/en/um-eos/eos-section-37-2-bfd-configuration#ww1114266) in the Arista documentation.

## Cisco ASA

For Cisco ASA configuration examples, see [Bidirectional Forwarding Detection Routing](https://www.cisco.com/c/en/us/td/docs/security/asa/asa96/configuration/general/asa-96-general-config/route-bfd.html) in the Cisco documentation. The BGP configuration is identical to the IOS/IOS-XE configuration later in this document.

## Cisco ASR

To see BFD status, use the following command at the top level of the Cisco AS configuration:
    
    
    show bfd neighbors 169.254.44.6 details
    

To configure BFD on a Cisco ASR, use the following command (the values shown are examples):
    
    
    int NAME
      bfd interval 1000 min_rx 1000 multiplier 5
    
    router bgp 65001
      neighbor 169.254.3.6 fall-over bfd single-hop
      neighbor 169.254.4.6 fall-over bfd single-hop
      neighbor 169.254.33.6 fall-over bfd single-hop
      neighbor 169.254.44.6 fall-over bfd single-hop
    

For additional Cisco IOS/IOS-XE BFD configuration settings and examples, see [BGP Support for BFD](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_bgp/configuration/xe-16/irg-xe-16-book/bgp-support-for-bfd.html) in the Cisco documentation.

## Cisco IOS-XR

For Cisco IOS-XR configuration examples, see [Implementing BFD](https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/26xx/routing/configuration/guide/b-routing-cg-asr9000-26xx/implementing-bfd.html) in the Cisco documentation.

## Fortigate

For Fortigate BFD configuration examples, see [Technical Note : FortiGate BFD implementation and examples (Bidirectional Forwarding Detection for OSPF and BGP)](https://kb.fortinet.com/kb/documentLink.do?externalID=FD30260).

## Juniper JunOS

To configure BFD on the Juniper JunOS with BGP, use the following command (the values shown are examples):
    
    
      protocols {
        bgp {
          group bfdtest-cr-2 {
            bfd-liveness-detection {
              minimum-interval 1000;
            }
            neighbor 192.163.6.4;
            neighbor 192.168.40.4;
            }
          }
        }
    

For additional Juniper BFD configuration settings and examples, see [Example: Configure BFD for BGP](https://www.juniper.net/documentation/en_US/junos/topics/topic-map/bgp-bfd.html) in the Juniper documentation.

## What's next

  * To configure BFD on a BGP session or peer router, see [Configure BFD for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

  * To modify BFD settings on a BGP session, see [Update or disable BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd).

  * For help with BFD diagnostic messages, session states, and status messages, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
