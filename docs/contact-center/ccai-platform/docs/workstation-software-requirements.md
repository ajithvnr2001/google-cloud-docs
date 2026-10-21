---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/workstation-software-requirements/
title: Workstation and software requirements \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:35.987455+00:00
---

# Workstation and software requirements  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/workstation-software-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Workstation and software requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page contains recommendations for setting up an agent's workstation and software to provide the best possible agent experience.

## Network bandwidth requirements

Adequate bandwidth is critical to ensure high call quality. The contact center local area network or associated virtual local area network should have as much bandwidth capacity as possible. Your agents use your data network for Contact Center AI Platform (CCAI Platform) functions and to interact with your CRM and any other systems you've implemented. Google recommends that you have the bandwidth for 100 Kbps upload and 100 Kbps download per agent dedicated for voice and chat with burstable bandwidth for images and attachments.

The [network test service](https://networktest.twilio.com) will give you an estimation of how many agents your connection can support.

### Virtual Local area network (VLAN)

Agents should be on a separate Virtual Local Area Network (VLAN) from other traffic in your network. By isolating your contact center operations in its own VLAN, you can create traffic shaping rules as well as Quality of Service (QoS) policies that can optimize and prioritize agent network traffic. This can reduce the chances of an end-user or agent experiencing poor call quality.

### Quality of Service (QOS)

Quality of Service (QoS) lets you prioritize certain network application traffic when the network gets congested. This helps reduce packet loss for the prioritized application. Voice traffic (UDP) should be given the highest priority on your network to avoid latency, jitter, and packet loss. On most modern network equipment, you can prioritize traffic through QoS and also set a minimum percentage of total bandwidth for specific types of traffic. Your network administrator can implement this feature for you. All network equipment in your Local Area Network (LAN) through which the prioritized traffic travels must have QoS implemented or you risk losing the prioritization tags.

### Network packet loss

Network packet loss results in poor audio call quality, delays, and garbled speech. We recommend ensuring that your network packet loss is less than 2%, or your agents will likely experience call issues. Even with low packet loss, it is still possible to experience low call quality if your customer has a poor wireless connection.

### Round-trip time (RTT)

Round-trip time (RTT) is the length of time it takes for a telecommunications signal to be sent and for an acknowledgment of that signal to be received. RTT is also known as ping time. RTT should be less than 200 milliseconds. Real-time communications like voice use the User Datagram Protocol (UDP), which is more sensitive to network delay than Transmission Control Protocol (TCP).

### SIP ALG and SPI

If SIP ALG (SIP Application Gateway) or Stateful Packet Inspection is included in the router or firewall, turn off these features for the [Agent adapter IP allow list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list.md).

### Virtual Private Network (VPN)

We strongly recommend avoiding using a VPN, as it will likely affect call quality due to additional overhead. If you need to use a VPN to route traffic, you can exclude the voice traffic by referring to the [Agent adapter IP allow list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list).

## Workstation requirements

This section provides recommendations for agent workstation equipment.

### Software and physical requirements

Agents should use a hard-wired connection because Wi-Fi connectivity cannot guarantee the support adequate voice quality. We recommend that you avoid running network or CPU-intensive applications, such as music streaming or large uploads or downloads, on your agent workstation. These compete for audio bandwidth when using the agent adapter.

Agent computers must have an Intel Core i5 (or equivalent) hardware processor or higher. For a Microsoft Windows computer, the recommended RAM is at least 8 GBs and preferably 16 GB. Mac OS and ChromeOS operating system computers are also supported.

You access CCAI Platform using the web. CCAI Platform supports Chrome, Safari, and Firefox, and we recommend using the latest versions.

### Headsets

The following features and brands of headsets are recommended for CCAI Platform use. Headsets must have a wired connection to the computer.

**Important:** To ensure a stable connection, make sure the headphone ports are clean.

Recommended features:

  * Binaural - Audio in both ears cuts down on background noise

  * Noise-canceling microphone

  * Noise-canceling headset

  * USB connection




Recommended brands of headsets that our customers use:

  * Jabra

  * Logitech

  * Poly

  * Sennheiser




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
