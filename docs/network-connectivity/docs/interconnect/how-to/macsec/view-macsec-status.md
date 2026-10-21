---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status/
title: View MACsec status \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:16.716551+00:00
---

# View MACsec status  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View MACsec status Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the status of your MACsec for Cloud Interconnect circuits.

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Cloud Interconnect connection that you want to view.

  3. The **Link circuit info** section displays the following information:

     1. **Google circuit ID:** the name of the link circuit.

     2. **Link state:** the link's physical state, one of the following:

        * check_circle**Active** to indicate that the LACP member link is up.

        * error**LACP Detatched** to indicate that the LACP member link is down.

     3. **MACsec key name:** the link's MACsec status and the MACsec key used to secure the connection. The status displays one of the following:

        * check_circle: MACsec is operationally up and the link is encrypted.

        * warning: MACsec is operationally down and the link is unencrypted.

     4. **Receiving optical power:** a status indicator and the optical light level that the physical interface detects from the remote transmitter in [dBm](https://en.wikipedia.org/wiki/DBm).

     5. **Transmitting optical power:** a status indicator and the optical light level that the physical interface is transmitting to the remote receiver in dBm.

     6. **Google demarc ID:** the Google-assigned unique ID for the link circuit.

  4. Click the **MACsec** tab. The **MACsec configuration** displays one of the following for your MACsec configuration:

     1. **Enabled, fail open:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link operates without encryption.

     2. **Enabled, fail closed:** MACsec encryption is enabled on the link. If MACsec encryption isn't established between both ends, then the link fails.

     3. **Disabled:** MACsec encryption is disabled on the link.




###  gcloud 

To view the status of your circuits, use the following command:
    
    
    gcloud compute interconnects get-diagnostics INTERCONNECT_CONNECTION_NAME
    

Replace `INTERCONNECT_CONNECTION_NAME` with the name of your Cloud Interconnect connection.

The output is similar to the following; look for the `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_UP`, the `circuitId` `lacpStatus` `state` set to `ACTIVE`, and the `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`:
    
    
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
          operational: true
        operationalStatus: LINK_OPERATIONAL_STATUS_UP
        receivingOpticalPower:
          state: OK
          value: -2.49
        transmittingOpticalPower:
          state: OK
          value: -0.88
      macAddress: 00:11:22:33:44:55
    

In this example, MACsec is enabled and operational on the circuit.

The following items indicate a circuit's status:

  * `bundleOperationalStatus`: the circuit bundle's status, which is one of the following:

    * `BUNDLE_OPERATIONAL_STATUS_UP`: the circuit bundle is up.

    * `BUNDLE_OPERATIONAL_STATUS_DOWN`: the circuit bundle is down.

  * `links.lacpStatus.state`: the circuit's link aggregation control protocol (LACP) state, which is one of the following:

    * `ACTIVE`: LACP is active.

    * `DETACHED`: LACP is inactive.

  * `links.macsec.CKN`: the connectivity association key name (CKN) that MACsec for Cloud Interconnect is actively using for this connection.

You can use `gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME` to display all the keys configured for your Cloud Interconnect connection. For more information, see [Get MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys).

If you have more than one key configured, then the key with the latest start time is selected as the active key. Google's edge routers reject any new MACsec sessions that attempt to use the older keys.

  * `links.macsec.operational`: the MACsec status of the circuits, which is one of the following:

    * `true`: MACsec is operational on this circuit.

    * `false`: MACsec is not operational on this circuit.

  * `links.operationalStatus`: the MACsec status of the link, which is one of the following:

    * `LINK_OPERATIONAL_STATUS_UP`: the Cloud Interconnect connection is operationally up.

    * `LINK_OPERATIONAL_STATUS_DOWN`: the Cloud Interconnect connection is operationally down.




The following sections demonstrate examples of MACsec for Cloud Interconnect states and how they look in the output for the Google Cloud CLI and the Google Cloud console.

## MACsec enabled and operational

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Cloud Interconnect connection that you want to view. The following items indicate that MACsec is enabled and operational. The links are passing traffic:

     * **Link state:** displays check_circle**Active** for all links.

     * **MACsec key name:** displays check_circle for all links. The MACsec key name is listed after each connection.

  3. Click the **MACsec** tab. The following items indicate that MACsec is configured and operational:

     * **MACsec configuration:** displays one of **Enabled, fail opened** or **Enabled, fail closed**.

     * **Pre-shared keys:** displays **Active, in use** for at least one key's **Key status**.




###  gcloud 

The output is similar to the following; look for the `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_UP`, the `circuitId` `lacpStatus` `state` set to `ACTIVE`, and the `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`:
    
    
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
          operational: true
        operationalStatus: LINK_OPERATIONAL_STATUS_UP
        receivingOpticalPower:
          state: OK
          value: -2.49
        transmittingOpticalPower:
          state: OK
          value: -0.88
      macAddress: 00:11:22:33:44:55
    

In the example, the following items indicate that MACsec is enabled and operational. The link is passing traffic:

  * `bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP`
  * `links.lacpStatus.state: ACTIVE`
  * `links.macsec.ckn: 0101010189abcdef...0123456789abcdef`
  * `links.macsec.operational: true`
  * `links.operationalStatus: LINK_OPERATIONAL_STATUS_UP`



## MACsec enabled, not operational, and fail-open off

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Cloud Interconnect connection that you want to view. The following items indicate that MACsec is disabled and non-operational. The links are not passing traffic:

     * **Link state:** displays error**LACP Detached** for all links.

     * **MACsec key name:** displays warning for all links. The MACsec key name is listed after each connection.

  3. Click the **MACsec** tab. The following items indicate that MACsec is configured and not operational:

     * **MACsec configuration:** displays **Down**.

     * **Pre-shared keys:** displays **Active, in use** for at least one key's **Key status**.




###  gcloud 

The output is similar to the following; look for the `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_DOWN`, the `circuitId` `lacpStatus` `state` set to `DETACHED`, and the `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`::
    
    
      bundleAggregationType: BUNDLE_AGGREGATION_TYPE_LACP
      bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_DOWN
      links:
      - circuitId: LOOP-0
        googleDemarc: fake-local-demarc-0
        lacpStatus:
          googleSystemId: '00:11:22:33:44:55'
          neighborSystemId: '55:44:33:22:11:00'
          state: DETACHED
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
    

In the example, **links.macsec** indicates that MACsec is enabled. The following items indicate that MACsec is not operational and that the link is not passing traffic:

  * `bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_DOWN`
  * `links.lacpStatus.state: DETACHED`
  * `links.macsec.ckn: 0101010189abcdef...0123456789abcdef`
  * `links.macsec.operational: false`
  * `links.operationalStatus: LINK_OPERATIONAL_STATUS_UP`



In this case, Google can't establish a MACsec session. Therefore `links.macsec.operational` is `false`. Because MACsec is a lower-level Layer 2 security protocol, all packets for higher-level protocols are dropped, including LACP. This results in `bundleOperationalStatus` being set to `BUNDLE_OPERATIONAL_STATUS_DOWN` and `links.lacpStatus.state` being set to `DETACHED`.

However, MACsec doesn't affect the status of the physical link; therefore, `links.operationalStatus` remains `LINK_OPERATIONAL_STATUS_UP` when MACsec is down as long as the physical layer is operational.

## MACsec enabled, not all links operational, and fail-open off

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Cloud Interconnect connection that you want to view. The following items indicate that MACsec is enabled, not all links are operational, and that some links are passing traffic:

     * **Link state:** displays error**LACP Detached** for one or more links, and check_circle**Active** for at least one link.

     * **MACsec key name:** displays warning**MACsec on this link is down** for one or more links, and check_circle**MACsec on this link is up** for at least one link. The MACsec key name is listed after each connection.

  3. Click the **MACsec** tab. The following items indicate that MACsec is configured and not operational:

     * **MACsec configuration:** displays **Enabled, fail closed**.

     * **Pre-shared keys:** displays **Active, in use** for at least one key's **Key status**.




###  gcloud 

The output is similar to the following; look for `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_UP`, `circuitId lacpStatus state` set to `ACTIVE`, `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`, `circuitId lacpStatus state` set to `DETACHED`, and `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`:
    
    
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
          operational: true
        operationalStatus: LINK_OPERATIONAL_STATUS_UP
        receivingOpticalPower:
          state: OK
          value: -2.49
        transmittingOpticalPower:
          state: OK
          value: -0.88
      - circuitId: LOOP-1
        googleDemarc: fake-local-demarc-1
        lacpStatus:
          googleSystemId: '00:11:22:33:44:66'
          neighborSystemId: '66:44:33:22:11:00'
          state: DETACHED
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
    

In the example, the following items indicate that MACsec is enabled and operational. The circuit is passing traffic, but only on one of the two links displayed:

  * `bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP`
  * `links.circuitId: LOOP-0:`
    * `links.lacpStatus.state: ACTIVE`
    * `links.macsec.ckn: 0101010189abcdef...0123456789abcdef`
    * `links.macsec.operational: true`
    * `links.operationalStatus: LINK_OPERATIONAL_STATUS_UP`
  * `links.circuitId: LOOP-1:`
    * `links.lacpStatus.state: DETACHED`
    * `links.macsec.ckn: 0101010189abcdef...0123456789abcdef`
    * `links.macsec.operational: false`
    * `links.operationalStatus: LINK_OPERATIONAL_STATUS_UP`



In this case, `bundleOperationalStatus` is `BUNDLE_OPERATIONAL_STATUS_UP`. Notice that `links.circuitId: LOOP-0` displays that `links.lacpStatus.state` is `ACTIVE` and `links.macsec.operational` is `true`. The first link is functioning as expected and is passing traffic.

However, notice that `links.circuitId: LOOP-1` displays that `links.lacpStatus.state` is `DETACHED` and `links.macsec.operational` is `false`. The second link is not functioning as expected and is not passing traffic.

However, MACsec doesn't affect the status of either physical link; therefore, both links display `links.operationalStatus` as `LINK_OPERATIONAL_STATUS_UP`. This state remains even when MACsec is down for one of the links, as long as the physical layer is operational.

## MACsec enabled, not operational, and fail-open on

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Cloud Interconnect connection that you want to view. The following items indicate that MACsec is enabled and non-operational. The links are passing traffic:

     * **Link state:** displays check_circle **Active** for all links.

     * **MACsec key name:** displays a warning**Warning** for all links. The MACsec key name is listed after each connection.

  3. Click the **MACsec** tab. The following items indicate that MACsec is configured and not operational:

     * **MACsec configuration:** displays **Enabled, fail opened**.

     * **Pre-shared keys:** displays **Active** for at least one key's **Key status**.




###  gcloud 

The output is similar to the following:
    
    
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

  * `links.macsec` values indicate that MACsec is enabled.
  * `bundleOperationalStatus` displays `BUNDLE_OPERATIONAL_STATUS_UP`, which indicates that the Cloud Interconnect connection is operational.
  * `macsec.operational` displays `false`, which indicates that MACsec isn't operational.



To verify that the Cloud Interconnect connection is set to fail-open, run the following command:
    
    
    gcloud compute interconnects describe INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following for a link set to fail-open; look for the `macsec` section where `macsecEnabled` is set to `true`:
    
    
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
      failOpen: true
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
    

## MACsec disabled

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.



[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  1. Select the Cloud Interconnect connection that you want to view. The following items indicate that MACsec is disabled. The links aren't passing traffic:

     * **Link state:** displays check_circle **Active** for all links.

     * **MACsec key name:** displays a empty text and no status for all links.

  2. Click the **MACsec** tab. The following items indicate that MACsec is configured and not operational:

     * **MACsec configuration:** displays **Disabled**.

     * **Pre-shared keys:** displays **Active** for at least one key's **Key status**.




###  gcloud 

The output is similar to the following; look for the `bundleOperationalStatus` set to `BUNDLE_OPERATIONAL_STATUS_UP`, the `circuitId` `lacpStatus` `state` set to `ACTIVE`, and the `operationalStatus` set to `LINK_OPERATIONAL_STATUS_UP`:
    
    
      bundleAggregationType: BUNDLE_AGGREGATION_TYPE_STATIC
      bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP
      links:
      - circuitId: LOOP-0
        googleDemarc: fake-local-demarc-0
        lacpStatus:
          googleSystemId: '00:11:22:33:44:55'
          neighborSystemId: '55:44:33:22:11:00'
          state: ACTIVE
        operationalStatus: LINK_OPERATIONAL_STATUS_UP
        receivingOpticalPower:
          state: OK
          value: -2.49
        transmittingOpticalPower:
          state: OK
          value: -0.88
      macAddress: 00:11:22:33:44:55
    

In the example, the fact that `links.macsec` is missing from the output indicates that MACsec is disabled and not operational. The link is passing unencrypted traffic.

Because MACsec is disabled, both `links.macsec.ckn` and `links.macsec.operational` don't display a value.

## What's next?

  * [Rotate MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys)
  * [Disable MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/disable-macsec)
  * [Get MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
