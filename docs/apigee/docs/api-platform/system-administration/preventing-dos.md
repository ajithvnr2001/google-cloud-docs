---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/preventing-dos/
title: Preventing DoS attacks \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:34.213286+00:00
---

# Preventing DoS attacks  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/preventing-dos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Preventing DoS attacks Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A Denial of Service (DoS) attack is an attempt to render your service or application unavailable to your end users. With Distributed Denial of Service (DDoS) attacks, the attackers use multiple resources (often a large number of compromised hosts/instances) to orchestrate large scale attacks against targets.

The Apigee architecture creates a peering connection between two networks: a Google-managed tenant project (the _Apigee VPC_) and a customer-managed project (the _Customer VPC_). To mitigate or prevent DoS attacks on these networks, be sure to follow the [Best Practices for DDoS Protection and Mitigation on Google Cloud Platform](https://docs.cloud.google.com/static/files/GCPDDoSprotection-04122016.pdf) (PDF).

If you expose your APIs externally, you can be vulnerable to DoS attacks. To mitigate this, Cloud Load Balancing includes some built-in protections, including:

  * **Protection by Google Frontend infrastructure:** With Cloud Load Balancing, the Google frontend infrastructure terminates user traffic and automatically scales to absorb certain types of attacks (such as SYN floods) before they reach your Compute Engine instances.
  * **Anycast-based Load Balancing:** Cloud Load Balancing enables a single anycast IP to front-end Apigee instances in all regions. Traffic is directed to the closest backend; in the event of a DDoS attack, GCLB increases the surface area to absorb the attack by moving traffic to instances with available capacity in any region where backends are deployed.



In addition to Cloud Load Balancing, you can add Google Cloud Armor to protect your API endpoints against DoS and web attacks. Cloud Armor provides benefits such as:

  * **IP-based and geo-based access control:** Filter your incoming traffic based on IPv4 and IPv6 addresses or address ranges (CIDRs). Enforce geography-based access controls to allow or deny traffic based on source geo using Google's geoIP mapping.
  * **Support for hybrid and multi-cloud deployments:** Help defend applications from DDoS or web attacks and enforce Layer 7 security policies whether your application is deployed on Google Cloud or in a hybrid or multi-cloud architecture.
  * **Visibility and monitoring:** Easily monitor all of the metrics associated with your security policies in the Cloud Monitoring dashboard. You can also view suspicious application traffic patterns from Cloud Armor directly in the Security Command Center dashboard.
  * **Pre-configured WAF rules:** Out-of-the-box rules from the ModSecurity Core Rule Set to help defend against attacks like cross-site scripting (XSS) and SQL injection. RFI, LFI, and RCE rules are also available in beta. Learn more in our WAF rules guide.
  * **Named IP Lists:** Allow or deny traffic through a Cloud Armor security policy based on a curated Named IP List (beta).



For more information, see [Google Cloud Armor](https://docs.cloud.google.com/armor).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[ VPC]: Virtual Private Cloud
