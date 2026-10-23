---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/
title: Feature deprecation: Classic VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:20.466108+00:00
---

# Feature deprecation: Classic VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/vpn/resources)



Send feedback 

#  Feature deprecation: Classic VPN Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud's [Terms of Service (section 7)](https://cloud.google.com/terms/) define the deprecation policy that applies to Cloud VPN. The [deprecation policy](https://cloud.google.com/terms/deprecation) only applies to the features or services listed therein.

After a Cloud VPN feature has been officially deprecated, the feature continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the feature or service will be scheduled for limited support.

The following table lists current Cloud VPN feature deprecations and their schedules.

Feature (status) | Deprecation date | Details  
---|---|---  
Classic VPN | March 31, 2022 | 

  * You can't create Classic VPN tunnels that use dynamic routing (BGP) that is managed by a Cloud Router for connections outside of Google Cloud. 
  * You can continue to create Classic VPN tunnels that use dynamic routing if the Classic VPN connects to VPN gateway software running inside a Compute Engine virtual machine (VM) instance. This configuration is still supported. 

  
Classic VPN | August 1, 2025 | 

  * You can't create Classic VPN tunnels that use dynamic routing (BGP). This is universally applicable regardless of the gateway the tunnel connects to. This includes connections to VPN gateway software running inside a Compute Engine VM instance or connections outside of Google Cloud.  Existing Classic VPN tunnels with BGP configurations are no longer supported. Tunnels that are in use will continue to function, but without an availability SLA. 
  * If you delete a Classic VPN tunnel that was configured with BGP, you can't recreate it with BGP functionality. However, you can still route traffic through your existing Classic VPN tunnels, unless you make changes that require you to switch to HA VPN, which is now the only option for BGP connectivity in Cloud VPN. 

For more information, see [Classic VPN dynamic routing deprecation](https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/classic-vpn-deprecation).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
