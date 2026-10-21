---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/modify-fail-open-behavior/
title: Modify fail-open behavior \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:15.779649+00:00
---

# Modify fail-open behavior  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/modify-fail-open-behavior/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify fail-open behavior Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to modify MACsec for Cloud Interconnect fail-open behavior.

You can choose to enable MACsec for Cloud Interconnect with fail-open behavior. Fail-open means that if Google's edge routers can't establish a MACsec key agreement (MKA) session with your router, then the Cloud Interconnect connection remains operational with unencrypted traffic. The default setting drops all traffic if an MKA session can't be established with your router.

You can change MACsec fail-over behavior only by using the Google Cloud CLI.

**Warning:** To avoid unintentionally passing unencrypted traffic, we recommend that you use the default setting for production traffic, and use fail-open behavior only for testing and troubleshooting.

## Enable fail-open behavior

Verify that there is no traffic on your Cloud Interconnect connection before enabling MACsec for Cloud Interconnect with fail-open behavior.

**Important:** When you enable fail-open behavior on your Cloud Interconnect connection, you must temporarily disable MACsec on your Cloud Interconnect connection. The connection temporarily experiences packet loss as a result. To avoid disruption to your network, verify that there is no traffic on your Cloud Interconnect VLAN attachments before disabling MACsec for Cloud Interconnect. For more information, see [Disable or enable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans).

###  gcloud 

Run the following commands:
    
    
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --no-enabled \
        --fail-open
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --enabled
    

## Disable fail-open behavior

If you have fail-open behavior enabled for MACsec for Cloud Interconnect, you can choose to later disable fail-open behavior. After fail-open behavior is disabled, if Google's edge routers can't establish a MACsec key agreement (MKA) session with your router, then the connection drops all traffic.

**Important:** When you disable fail-open behavior on your Cloud Interconnect connection, you must temporarily disable MACsec on your Cloud Interconnect connection. The connection temporarily experiences packet loss as a result. To avoid disruption to your network, verify that there is no traffic on your Cloud Interconnect VLAN attachments before disabling MACsec for Cloud Interconnect. For more information, see [Disable or enable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans).

###  gcloud 

Run the following commands:
    
    
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --no-enabled \
        --no-fail-open
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --enabled
    

## What's next?

  * [Troubleshoot MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
