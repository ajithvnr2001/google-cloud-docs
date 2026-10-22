---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec/
title: Troubleshoot MACsec \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:49.525489+00:00
---

# Troubleshoot MACsec  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Troubleshoot MACsec Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot MACsec for Cloud Interconnect.

## Cloud Interconnect displays an error when I attempt to create a new key

If you have an existing MACsec key without a start time and you attempt to create a new key, Cloud Interconnect displays an error. To resolve the error, [update the existing key's start time](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys#optional-update-existing-key-start-time).

## MACsec is operationally down on my Cloud Interconnect connection

You successfully enabled MACsec on your Cloud Interconnect connection and on your on-premises router, but the MACsec session displays that it is operationally down on your Cloud Interconnect connection links. The issue could be caused by one of the following:

  * The active keys on your on-premises router and Google's edge routers don't match.
  * A MACsec protocol mismatch exists between your on-premises router and Google's edge router.



To resolve the MACsec state, do the following:

  1. To verify that MACsec is enabled on your Cloud Interconnect connection, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the Cloud Interconnect connection that you want to view.

     3. On the **MACsec** tab, verify that **MACsec** **configuration** displays one of the following:

        * **Enabled, fail open:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link operates without encryption.

        * **Enabled, fail closed:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link fails.

###  gcloud 
    
    gcloud compute interconnects describe INTERCONNECT_CONNECTION_NAME
    

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

The output is similar to the following. Verify that `macsecEnabled: true` is displayed:
    
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
    

  2. To check the Cloud Interconnect port status, MACsec operational state, and the active key name, use one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the Cloud Interconnect connection that you want to view.

     3. In **Link circuit info** , verify that **Link state** displays check_circle**Active** for all links.

     4. Verify that **MACsec key name** displays a key name for all links, and that each key name displays check_circle**MACsec on this link is up** or warning**MACsec on this link is down**.

###  gcloud 
    
    gcloud compute interconnects get-diagnostics INTERCONNECT_CONNECTION_NAME \
        --project=PROJECT_NAME
    

Replace `PROJECT_NAME` with the name of your Google Cloud project.

The output is similar to the following. Verify that `links.lacpStatus.state` displays `ACTIVE`, that `links.macsec.ckn` displays a value, and that `links.operationalStatus` displays `LINK_OPERATIONAL_STATUS_UP`:
    
    bundleAggregationType: BUNDLE_AGGREGATION_TYPE_STATIC
    bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP
    links:
    - circuitId: LOOP-0
      googleDemarc: fake-local-demarc-0
      lacpStatus:
        googleSystemId: '00:11:22:33:44:55'
        neighborSystemId: '55:44:33:22:11:00'
        state: ACTIVE
      macsec:
        ckn: 0101010189abcdef...0123456789abcdef
        operational: false
      operationalStatus: LINK_OPERATIONAL_STATUS_UP
      receivingOpticalPower:
        state: OK
        value: -2.49
      transmittingOpticalPower:
        state: OK
        value: -0.88
    macAddress: 00:11:22:33:44:55
    

If there isn't a value displayed for `links.macsec.ckn`, then contact Google Cloud Support for help.

  3. To verify the active key's CAK and CKN values, and the key's start time, select one of the following options:

###  Console 

     1. On the **MACsec** tab, go to the **Pre-shared keys** section, and then click **View** beside the active key. If a CKN value isn't displayed, contact Google Cloud support for help.

     2. In the **Pre-shared keys** section, verify that the start time listed for the active key matches the start time on your on-premises router. Do one of the following:

        * If the values don't match, refer to your router's manual to update the values on your router, and then verify whether a MACsec session can be established.

        * If the values match but the MACsec session is still operationally down on the link, then continue to the next step.

###  gcloud 

     1. Run the `gcloud compute interconnects get-diagnostics` command to display the active key's CKN value.

If you have more than one key configured, then the key with the latest start time that isn't in the future is selected as the active key. Google's edge routers reject any new MACsec sessions that attempt to use old keys.

     2. Get the MACsec configuration and then note the CAK value and the key's start time that correspond to the previously displayed CKN value:
            
            gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
            

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

The output is similar to the following; look for the `ckn`:
            
            preSharedKeys:
            - name: key1
              ckn: 0101010189abcdef...0123456789abcdef
              cak: 0123456789abcdef...0123456789abcdef
              startTime: 2023-07-01T12:12:12Z
            - name: key2
              ckn: 0202020289abcdef...0123456789abcdef
              cak: 0123456789abcdef...0123456789abcdef
              startTime: 2023-08-01T12:12:12Z
            

     3. Verify that the active CKN, CAK, and start times on your on-premises router match the values that MACsec for Cloud Interconnect displays. Do one of the following:

        * If the values don't match, refer to your router's manual to update the values on your router, and then verify whether a MACsec session can be established.

        * If the values match but the MACsec session is still operationally down on the link, then continue to the next step.

  4. View metrics to determine whether packets are dropping on the ingress or egress of the Cloud Interconnect connection. For information about viewing metrics, see [Monitor connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring).

To determine next steps, do the following:

     * If `network/interconnect/link/macsec/received_errors_count` is incrementing, then the packets are dropping at the ingress Cloud Interconnect connection due to errors. This indicates that a protocol mismatch exists between your on-premises router and Google's edge routers. Check your on-premises router's logs to troubleshoot.

     * If any of the following counters are incrementing, then contact Google Cloud Support for further assistance:

       * `network/interconnect/link/macsec/received_dropped_packets_count`
       * `network/interconnect/link/macsec/send_errors_count`
       * `network/interconnect/link/macsec/send_dropped_packets_count`
     * If none of the following counters are incrementing, then it indicates that packets are dropping at the egress of your on-premises router. Check your on-premises router's logs to troubleshoot.

       * `network/interconnect/receive_errors_count`
       * `network/interconnect/received_unicast_packets_count`
       * `network/interconnect/link/macsec/received_control_packets_count`
       * `network/interconnect/link/macsec/received_data_packets_count`
       * `network/interconnect/link/macsec/received_errors_count`
       * `network/interconnect/link/macsec/received_dropped_packets_count`



## MACsec is operational and is experiencing packet loss

You successfully enabled MACsec for Cloud Interconnect and MACsec is operationally up, but you are experiencing packet loss.

If your MACsec connection is operational but the Cloud Interconnect's Link Aggregation Control Protocol (LACP) status is `Detached`, verify that Secure Channel Identifier (SCI) is enabled on your on-premises router. For more information, see [Configure your on-premises router](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/set-up-macsec#configure-your-on-premises-router).

View metrics to determine if packets are dropping on the ingress or egress of the Cloud Interconnect connection. For information about viewing metrics, see [Monitor connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring). If the Cloud Interconnect connection does not show any packet errors or loss, then proceed to checking the MACsec routers:

  * If `network/interconnect/link/macsec/received_errors_count` is incrementing, then the packets are dropping at the ingress Cloud Interconnect connection due to errors. This indicates that a protocol mismatch exists between your on-premises router and Google's edge routers. Check your on-premises router's logs to troubleshoot.

  * If any of the following counters are incrementing, then contact Google Cloud Support for further assistance:

    * `network/interconnect/link/macsec/received_dropped_packets_count`
    * `network/interconnect/link/macsec/send_errors_count`
    * `network/interconnect/link/macsec/send_dropped_packets_count`
  * If none of the following counters are incrementing, then it indicates that packets are dropping at the egress of your on-premises router. Check your on-premises router's logs to troubleshoot.

    * `network/interconnect/receive_errors_count`
    * `network/interconnect/received_unicast_packets_count`
    * `network/interconnect/link/macsec/received_control_packets_count`
    * `network/interconnect/link/macsec/received_data_packets_count`
    * `network/interconnect/link/macsec/received_errors_count`
    * `network/interconnect/link/macsec/received_dropped_packets_count`



## Troubleshoot MACsec issues while fail-open behavior is enabled

If you enable MACsec for Cloud Interconnect with fail-open behavior, then your Cloud Interconnect connection continues forwarding traffic even if a MACsec session can't be successfully established. We strongly recommend that you avoid using fail-open behavior on production Cloud Interconnect connections to avoid transmitting packets as clear text.

To determine the configuration and state your MACsec connection, do the following:

  1. To verify the state of your Cloud Interconnect connection, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the Cloud Interconnect connection that you want to view.

     3. On the **MACsec** tab, verify that **MACsec configuration** displays **Enabled, fail open**.

###  gcloud 
    
    gcloud compute interconnects describe INTERCONNECT_CONNECTION_NAME
    

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

The output is similar to the following; look for `macsec failOpen` set to `true` and `macsecEnabled` set to `true`:
    
    availableFeatures:
    - IF_MACSEC
    adminEnabled: true
    circuitInfos:
    - customerDemarcId: fake-peer-demarc-0
      googleCircuitId: LOOP-0
      googleDemarcId: fake-local-demarc-0
    creationTimestamp: '2021-10-05T03:39:33.888-07:00'
    customerName: Fake Customer
    description: <something>
    googleReferenceId: '123456789'
    id: '12345678987654321'
    interconnectAttachments:
    - https://www.googleapis.com/compute/prod/projects/my-project1/regions/us-central1/interconnectAttachments/interconnect-123456-123456789-0
    interconnectType: IT_PRIVATE
    kind: compute#interconnect
    labelFingerprint: 42WmSpB8rSM=
    linkType: LINK_TYPE_ETHERNET_10G_LR
    location: https://www.googleapis.com/compute/prod/projects/my-project1/global/interconnectLocations/cbf-zone2-65012
    macsec:
      failOpen: true
      preSharedKeys:
      - name: key3
        startTime: '2023-07-01T21:00:01.000Z'
    macsecEnabled: true
    name: INTERCONNECT_CONNECTION_NAME
    operationalStatus: OS_ACTIVE
    provisionedLinkCount: 1
    requestedFeatures:
    - IF_MACSEC
    requestedLinkCount: 1
    selfLink: https://www.googleapis.com/compute/prod/projects/my-project1/global/interconnects/INTERCONNECT_CONNECTION_NAME
    selfLinkWithId: https://www.googleapis.com/compute/prod/projects/my-project1/global/interconnects/INTERCONNECT_CONNECTION_NAME/12345678987654321
    state: ACTIVE
    

In this example, `macsec.failopen` displays `true` and `macsecEnabled` displays `true`.

  2. To check the Cloud Interconnect connection's port status, MACsec operational state, and the active key name, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the Cloud Interconnect connection that you want to view.

     3. In **Link circuit info** , verify that **Link state** displays check_circle**Active** for all links.

     4. Verify that **MACsec key name** displays a key name for all links, and that each key name displays check_circle**MACsec on this link is up** or warning**MACsec on this link is down**.

###  gcloud 
    
    gcloud compute interconnects get-diagnostics INTERCONNECT_CONNECTION_NAME \
        --project=PROJECT_NAME
    

Replace `PROJECT_NAME` with the name of your Google Cloud project.

The output is similar to the following; look for the `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_UP`, the `state` set to `ACTIVE`, and the `macsec` `ckn` `operational` set to `false`:
    
    bundleAggregationType: BUNDLE_AGGREGATION_TYPE_LACP
      bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP
      links:
      - circuitId: LOOP-0
        googleDemarc: fake-local-demarc-0
        lacpStatus:
          googleSystemId: '00:11:22:33:44:55'
          neighborSystemId: '55:44:33:22:11:00'
          state: ACTIVE
        macsec:
          ckn: 0101010189abcdef...0123456789abcdef
          operational: false
        operationalStatus: LINK_OPERATIONAL_STATUS_UP
        receivingOpticalPower:
          state: OK
          value: -2.49
        transmittingOpticalPower:
          state: OK
          value: -0.88
      macAddress: 00:11:22:33:44:55
    

In this example:

     * `bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP` indicates that the bundle is operationally up.
     * `links.lacpStatus.state: ACTIVE` indicates that the LACP member link is up.
     * `links.macsec.operational: false` indicates that MACsec is operationally down.

In this case, because fail-open behavior is enabled, the LACP control packets are not dropped.

If there isn't a value displayed for `links.macsec.ckn`, then contact Google Cloud Support for help.

The `gcloud compute interconnects get-diagnostics` command displays the active key's CKN value. If you have more than one key configured, then the key with the latest start time is selected as the active key. Google's edge routers reject any new MACsec sessions that attempt to use the older keys.

  3. To get the MACsec configuration, and then note the CAK value and the key's start time that correspond to the previously displayed CKN value, select one of the following options:

###  Console 

     1. On the **MACsec** tab, go to the **Pre-shared keys** section, and then click **View** beside the active key. If the key's CAK and CKN values aren't displayed, contact Google Cloud support for help.

     2. In the **Pre-shared keys** section, verify that the start time listed for the active key matches the start times on your on-premises router.

###  gcloud 

     1. Run the following command:
            
            gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
            

The output is similar to the following; look for the `preSharedKeys` `name` `ckn`:
            
            preSharedKeys:
            - name: key1
              ckn: 0101010189abcdef...0123456789abcdef
              cak: 0123456789abcdef...0123456789abcdef
              startTime: 2023-07-01T12:12:12Z
            - name: key2
              ckn: 0202020289abcdef...0123456789abcdef
              cak: 0123456789abcdef...0123456789abcdef
              startTime: 2023-08-01T12:12:12Z
            

     2. Verify that the active CKN, CAK, and start times on your on-premises router match the values that MACsec for Cloud Interconnect displays.

     3. Do one of the following:

        * If the values don't match, refer to your router's manual to update the values on your router, and then verify if a MACsec can be established now.

        * If the values match but the MACsec session is still operationally down on the link, then continue to the next step.

  4. View metrics to observe packet counters for your Cloud Interconnect connection. For more information about viewing metrics, see [Monitor connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring).

When MACsec fail-open behavior is enabled, the following counters increment:

     * `network/interconnect/sent_unicast_packets_count`
     * `network/interconnect/received_unicast_packets_count`

When MACsec fail-open behavior is enabled, the following counters don't increment:

     * `network/interconnect/link/macsec/received_control_packets_count`
     * `network/interconnect/link/macsec/received_data_packets_count`
     * `network/interconnect/link/macsec/sent_control_packets_count`
     * `network/interconnect/link/macsec/sent_data_packets_count`

To determine next steps, do the following:

     * If `network/interconnect/link/macsec/received_errors_count` is incrementing, then the packets are dropping at the ingress Cloud Interconnect connection due to errors. This indicates that a protocol mismatch exists between your on-premises router and Google's edge routers. Check your on-premises router's logs to troubleshoot.

     * If any of the following counters are incrementing, then contact Google Cloud Support for further assistance:

       * `network/interconnect/link/macsec/received_dropped_packets_count`
       * `network/interconnect/link/macsec/send_errors_count`
       * `network/interconnect/link/macsec/send_dropped_packets_count`
     * If none of the following counters are incrementing, then it can indicate that packets are dropping at the egress of your on-premises router. Check your on-premises router's logs to troubleshoot.

       * `network/interconnect/receive_errors_count`
       * `network/interconnect/received_unicast_packets_count`
       * `network/interconnect/link/macsec/received_errors_count`
       * `network/interconnect/link/macsec/received_dropped_packets_count`



## What's next?

  * [Rotate MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys)
  * [View MACsec status](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status)
  * [Modify fail-open behavior](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/modify-fail-open-behavior)
  * [Get MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
