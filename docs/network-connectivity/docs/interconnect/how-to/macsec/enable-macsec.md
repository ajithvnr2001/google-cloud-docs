---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/enable-macsec/
title: Enable MACsec \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:15.672440+00:00
---

# Enable MACsec  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/enable-macsec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Enable MACsec Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable MACsec for Cloud Interconnect.

After you generate pre-shared keys and configure your on-premises router to use them, you need to enable MACsec for Cloud Interconnect. After MACsec for Cloud Interconnect is enabled, you verify that your Cloud Interconnect configuration is correctly configured and is using MACsec to help protect your data.

## Before you begin

If you haven't completed set up, then [set up MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/set-up-macsec) before enabling MACsec for Cloud Interconnect.

**Important:** When you enable MACsec on your Cloud Interconnect connection, the connection temporarily experiences packet loss. To avoid disruption to your connectivity, verify that there is no traffic on your Cloud Interconnect VLAN attachments before enabling MACsec for Cloud Interconnect. For more information, see [Disable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans).

## Enable MACsec for Cloud Interconnect

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to modify.

  3. On the **MACsec** tab, click **Enable**.

A confirmation window is displayed. Read the message, and then click **Confirm** to confirm that you want to enable MACsec, or **Cancel** to cancel.




###  gcloud 

To enable MACsec for Cloud Interconnect with default settings, run the following command:
    
    
    gcloud compute interconnects macsec update INTERCONNECT_CONNECTION_NAME \
        --enabled
    

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

     * **MACsec key name** : displays a check_circle **Check** and the name of the MACsec key name to indicate that MACsec is active on the link.

     * **Receiving optical power:** a check_circle **Check** indicates an acceptable connection. The optical light level that the physical interface detects from the remote transmitter is displayed in [dBm](https://en.wikipedia.org/wiki/DBm).

     * **Transmitting optical power:** a check_circle **Check** indicates an acceptable connection and the optical light level that the physical interface is transmitting to the remote receiver is displayed in dBm.

     * **Google demarc ID:** the Google-assigned unique ID for the link circuit.

  4. Click the **MACsec** tab. The **MACsec** **configuration** displays one of the following for your MACsec configuration:

     * **Enabled, fail open:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link operates without encryption.

     * **Enabled, fail closed:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link fails.




###  gcloud 

Run the following command:
    
    
    gcloud compute interconnects describe INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following 10 GB Cloud Interconnect example; look for `availableFeatures` set to `IF_MACSEC` and the `macsec` section:
    
    
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
    macsecEnabled: true
    name: INTERCONNECT_CONNECTION_NAME
    operationalStatus: OS_ACTIVE
    provisionedLinkCount: 1
    requestedFeatures:
    - IF_MACSEC
    requestedLinkCount: 1
    selfLink: https://www.googleapis.com/compute/v1/projects/my-project1/global/interconnects/INTERCONNECT_CONNECTION_NAME
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/my-project1/global/interconnects/12345678987654321
    state: ACTIVE
    

The following items specify the Cloud Interconnect connection's MACsec configuration:

  * **`availableFeatures`:** MACsec capability on the Cloud Interconnect connection. This parameter is shown only for 10 GB Cloud Interconnect connections, because all 100 GB and 400 GB Cloud Interconnect connections are MACsec capable by default.

  * **`macsec.failOpen`:** the connection's behavior if Cloud Interconnect can't establish an MKA session with your router. The value is either of the following:

    * **`false`:** if an MKA session can't be established, then Cloud Interconnect drops all traffic.

    * **`true`:** if an MKA session can't be established, then Cloud Interconnect passes unencrypted traffic.

  * **`macsec.preSharedKeys.name`:** the list of all pre-shared keys configured for Cloud Interconnect on this link.

  * **`macsec.preSharedKeys.startTime`:** the start time that the current pre-shared key is considered valid. All keys have infinite validity.

  * **`macsecEnabled`:** MACsec status for Cloud Interconnect on this link. The value is either of the following:

    * **`false`:** MACsec for Cloud Interconnect is off.
    * **`true`:** MACsec for Cloud Interconnect is on.



This command doesn't display MACsec operational status.

## Enable MACsec on your on-premises router

Refer to your router vendor's documentation to enable MACsec on your on-premises router.

## Undrain your Cloud Interconnect connection

If you previously drained your Cloud Interconnect connection, [enable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/enable-vlan-attachments).

## What's next?

  * [Troubleshoot MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec)
  * [View MACsec status](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status)
  * [Disable MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/disable-macsec)
  * [Get MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys)
  * [Rotate MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
