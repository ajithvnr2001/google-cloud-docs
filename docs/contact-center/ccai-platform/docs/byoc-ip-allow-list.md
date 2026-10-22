---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc-ip-allow-list/
title: BYOC IP allow list \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:25.703684+00:00
---

# BYOC IP allow list  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc-ip-allow-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  BYOC IP allow list Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the Bring Your Own Carrier (BYOC) IP addresses, by carrier, that you can use in your Access Control List (ACL). Google recommends using all appropriate IP ranges to help avoid call failures.

## Media IPs

Media IP addresses are for real-time transmission of audio data during a SIP session. After a call is established using signaling, the voice streams flow between these media IP addresses. Implementing the correct media IP configuration is critical for clear and uninterrupted media exchange with your carrier.

### Telnyx

  * 103.115.244.128/25
  * 185.246.41.128/25



### Vonage

  * 216.147.0.0/18
  * 168.100.64.0/18



### Twilio

  * 168.86.128.0/18



## Signaling IPs

Signaling IP addresses are for controlling and managing SIP sessions. They transmit messages that initiate, modify, and terminate sessions. Proper configuration of signaling IPs is essential for CCAI Platform to correctly communicate call control information with your carrier.

### Telnyx

  * North America (US): 
    * 192.76.120.10
    * 64.16.250.10
  * North America (Canada): 
    * 192.76.120.31
    * 64.16.250.13
  * Europe: 
    * 185.246.41.140
    * 185.246.41.141
  * Australia: 
    * 103.115.244.145
    * 103.115.244.146



### Vonage

  * Global: 
    * 216.147.0.1
    * 216.147.0.2
    * 216.147.1.1
    * 216.147.1.2
    * 216.147.2.1
    * 216.147.2.2
    * 216.147.3.1
    * 216.147.3.2
    * 216.147.4.1
    * 216.147.4.2
    * 216.147.5.1
    * 216.147.5.2



### Twilio

  * North America: 
    * 54.172.60.0/30
    * 54.244.51.0/30
  * South America: 
    * 177.71.206.192/30
  * Europe (Ireland): 
    * 54.171.127.192/30
  * Europe (Germany): 
    * 35.156.191.128/30
  * Asia Pacific (Japan): 
    * 54.65.63.192/30
  * Asia Pacific (Singapore): 
    * 54.169.127.128/30
  * Asia Pacific (Australia): 
    * 54.252.254.64/30



## Ports

The following ports should be permitted for signaling and media:

  * RTP Port Ranges 10,000 to 60,000 UDP (Ephemeral Port Range)
  * Signaling Port Ranges 5060 UDP / 5061 TCP and TLS



## Certificates

The carriers used by CCAI Platform accept any publicly signed certificate.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
