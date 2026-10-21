---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/disable-macsec/
title: Disable MACsec \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:15.729646+00:00
---

# Disable MACsec  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/disable-macsec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Disable MACsec Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to disable MACsec for Cloud Interconnect.

You can disable MACsec, which can be useful when troubleshooting your connection.

**Important:** When you disable MACsec on your Cloud Interconnect connection, the connection temporarily experiences packet loss. To avoid disruption to your connectivity, verify that there is no traffic on your Cloud Interconnect VLAN attachments before disabling MACsec for Cloud Interconnect.

## Disable MACsec for Cloud Interconnect

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to modify.

  3. On the **MACsec** tab, click **Disable**.

In the confirmation dialog, read the message, and then click **Confirm** to confirm that you want to disable MACsec, or **Cancel** to cancel.




###  gcloud 

To disable MACsec for Cloud Interconnect, run the following command:
    
    
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --no-enabled
    

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

## Verify MACsec configuration

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to view.

  3. The **Link circuit info** section displays the following information:

     * **Google circuit ID:** the name of the link circuit.

     * **Link state:** the LACP member link's physical state displays a check_circle **Check** and **Active** to indicate that the LACP member link is up.

     * **MACsec key name:** the field is empty when MACsec is disabled.

     * **Receiving optical power:** a check_circle**check** indicates an acceptable connection. The optical light level that the physical interface detects from the remote transmitter is displayed in [dBm](https://en.wikipedia.org/wiki/DBm).

     * **Transmitting optical power:** a check_circle**check** indicates an acceptable connection and the optical light level that the physical interface is transmitting to the remote receiver is displayed in dBm.

  4. **MACsec configuration** displays **Disabled** to indicate that MACsec encryption is disabled on the link.




###  gcloud 

To verify your Cloud Interconnect MACsec configuration, run the following command:
    
    
    gcloud compute interconnects describe INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following:
    
    
    adminEnabled: true
    availableFeatures:
    - IF_MACSEC
    circuitInfos:
    - customerDemarcId: fake-peer-demarc-0
      googleCircuitId: LOOP-0
      googleDemarcId: fake-local-demarc-0
    creationTimestamp: '2021-10-05T03:39:33.888-07:00'
    customerName: Fake Company
    description: something important
    googleReferenceId: '123456789'
    id: '12345678987654321'
    interconnectAttachments:
    - https://www.googleapis.com/compute/v1/projects/my-project1/regions/us-central1/interconnectAttachments/interconnect-123456-987654321-0
    interconnectType: IT_PRIVATE
    kind: compute#interconnect
    labelFingerprint: 12H17262736_
    linkType: LINK_TYPE_ETHERNET_10G_LR
    location: https://www.googleapis.com/compute/v1/projects/my-project1/global/interconnectLocations/cbf-zone2-65012
    macsec:
      failOpen: false
      preSharedKeys:
      - name: key1
        startTime: 2023-07-01T21:00:01.000Z
    macsecEnabled: false
    name: INTERCONNECT_CONNECTION_NAME
    operationalStatus: OS_ACTIVE
    provisionedLinkCount: 1
    requestedFeatures:
    - IF_MACSEC
    requestedLinkCount: 1
    selfLink: https://www.googleapis.com/compute/v1/projects/my-project1/global/interconnects/INTERCONNECT_CONNECTION_NAME
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/my-project1/global/interconnects/12345678987654321
    state: ACTIVE
    

The following items specify the MACsec connections's configuration:

  * **`macsec.failOpen`:** the connection's behavior if Cloud Interconnect can't establish an MKA session with your router. The value is either of the following:

    * **`false`:** if an MKA session can't be established, then Cloud Interconnect drops all traffic.

    * **`true`:** if an MKA session can't be established, then Cloud Interconnect passes unencrypted traffic.

  * **`macsec.preSharedKeys.name`:** the list of all pre-shared keys configured for Cloud Interconnect on this link.

  * **`macsec.preSharedKeys.startTime`:** when the current pre-shared key became valid. All keys have infinite validity.

  * **`macsecEnabled`:** MACsec status for Cloud Interconnect on this link. The value is either of the following:

    * **`false`:** MACsec for Cloud Interconnect is off.

    * **`true`:** MACsec for Cloud Interconnect is on.




This command doesn't display MACsec operational status.

## What's next?

  * [View MACsec status](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status)
  * [Rotate MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
