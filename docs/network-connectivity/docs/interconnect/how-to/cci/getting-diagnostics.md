---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/getting-diagnostics/
title: Get diagnostics \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:10.669890+00:00
---

# Get diagnostics  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/getting-diagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Get diagnostics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Interconnect diagnostics let you troubleshoot your Cross-Cloud Interconnect connections during provisioning and after activation. The diagnostics provide you with current, detailed technical information about the Google Cloud side of your Cross-Cloud Interconnect connection.

## Diagnostics during outages

Diagnostic results might not be available during a [global outage](https://status.cloud.google.com/) because the Cross-Cloud Interconnect connection information is provided as a global resource. A global outage might affect the diagnostics for Cross-Cloud Interconnect from being fetched. However, these global outages don't necessarily reflect the functional state of the interconnects or attachments.

## Diagnostics during provisioning

Diagnostics contain different data depending on the stage of the provisioning process. Your connection must meet the requirements of each stage before it can move on to the next one.

The stages are as follows:

  * **Stage 1 - Circuit connection:**

    * The optical power state is `OK`.
    * bundleOperationalStatus is `Down`.
  * **Stage 2 - Circuit qualification (multiple links):**

    * The optical power state is `OK`.
    * bundleOperationalStatus is `Down`.
  * **Stage 3 - Production configuration:**

    * The optical power state is `OK`.
    * bundleOperationalStatus is `Up`.



## Use diagnostics

To interpret information that you get from the Google Cloud console, the Google Cloud CLI, or the API, see the Command output reference section.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.get`
  * `compute.interconnects.use`



**Roles**

  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the name of your Cross-Cloud Interconnect connection.

  3. Review the following fields:

     * For warnings or errors, see the **Status** field in the upper-left corner of the page.
     * For the provisioned capacity of the Cloud Interconnect connection, see the **Provisioned capacity** field.
     * If you suspect issues with the Cloud Interconnect connection, see the **VLAN attachments** section for information such as the effective capacity of the connection or the number of down links.
     * For additional details, such as light levels, see the **Link circuit info** section.



###  gcloud 

Use the [`gcloud compute interconnects get-diagnostics` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/get-diagnostics):
    
    
    gcloud compute interconnects get-diagnostics NAME \
        --project=PROJECT_ID
    

Replace the following:

  * `NAME`: the name of the connection
  * `PROJECT_ID`: the ID of the Google Cloud project



The command output should look similar to the following:
    
    
    result:
    bundleAggregationType: BUNDLE_AGGREGATION_TYPE_LACP
    bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP
    links:
    - circuitId: GCP-00112
    googleDemarc: MARKL:MMR A/ 4th floor Cab 04.105.004.704 FP 4 Port 3 Fibers 77,78
      -LC
    lacpStatus:
      googleSystemId: 9c:e1:76:7a:40:de
      neighborSystemId: ec:ce:13:e2:99:07
      state: ACTIVE
    operationalStatus: LINK_OPERATIONAL_STATUS_UP
    receivingOpticalPower:
      state: OK
      value: -2.94
    transmittingOpticalPower:
      state: OK
      value: -1.66
    macAddress: 9c:e1:76:7a:40:e3
    

###  API 

Use the [`interconnects.getDiagnostics` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/getDiagnostics):
    
    
     GET https://compute.googleapis.com/compute/projects/PROJECT_ID/global/interconnects/NAME/getDiagnostics
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `NAME`: the name of your connection



If this command succeeds, it returns `InterconnectDiagnostics` output in the following format.
    
    
    {
    "result": {
    "macAddress": "9c:e1:76:7a:40:e3",
    "links": [
      {
        "circuitId": "GCP-00112",
        "googleDemarc": "MARKL:MMR A/ 4th floor Cab 04.105.004.704 FP 4 Port 3 Fibers 77,78 -LC",
        "receivingOpticalPower": {
          "value": -2.97,
          "state": "OK"
        },
        "transmittingOpticalPower": {
          "value": -1.67,
          "state": "OK"
        },
        "lacpStatus": {
          "state": "ACTIVE",
          "googleSystemId": "9c:e1:76:7a:40:de",
          "neighborSystemId": "ec:ce:13:e2:99:07"
        },
        "operationalStatus": "LINK_OPERATIONAL_STATUS_UP"
      }
    ],
    "bundleOperationalStatus": "BUNDLE_OPERATIONAL_STATUS_UP",
    "bundleAggregationType": "BUNDLE_AGGREGATION_TYPE_LACP"
    }
    }
    

## Command output reference

To interpret diagnostics output, see the following table.

**Note:** If you want to trigger warnings for the value of the transmitting and receiving optical power in your on-premises routers, you can take a known good optical value, give it a 10% margin, and create alerts relative to that value. In general, a `-7dBm` warning and a `-11dBm` alarm are good optical value estimates for most links.Output parameter | Description  
---|---  
`macAddress` | Describes the MAC address of the Cloud Interconnect connection bundle on the Google Cloud side.  
`arpCache` | Describes individual neighbors seen by the Cloud Router in the ARP cache for the Cloud Interconnect connection. This is empty when the connection is not bundled.  
`arpCache[].macAddress` | Lists the MAC address of this ARP neighbor.  
`arpCache[].ipAddress` | Lists the IP address of this ARP neighbor.  
`links[]` | Describes the status for each link on the Cloud Interconnect connection.  
`links[].circuitId` | Lists the Google-assigned unique ID for this circuit, as assigned during circuit turn-up.  
`links[].googleDemarc` | Describes the Google-assigned demarc, as assigned at circuit turn-up.  
`links[].receivingOpticalPower` | Describes the current value and status for the received light level.  
`links[].receivingOpticalPower.value` | Lists the current value of the received light level, in dBm.  
`links[].receivingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the receiving transceiver. The following are the possible fixed values:

  * **OK:** The value has not crossed a warning threshold.
  * **LOW_WARNING:** The value has crossed below the low warning threshold.
  * **HIGH_WARNING:** The value has crossed above the high warning threshold.
  * **LOW_ALARM:** The value has crossed below the low alarm threshold.
  * **HIGH_ALARM:** The value has crossed above the high alarm threshold.

  
`links[].transmittingOpticalPower` | The current value and status for the transmit light level.  
`links[].transmittingOpticalPower.value` | The current value of the transmitting light level, in [dBm](https://wikipedia.org/wiki/DBm).  
`links[].transmittingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the transmitting transceiver. The following are the possible fixed values:

  * **OK:** The value has not crossed a warning threshold.
  * **LOW_WARNING:** The value has crossed below the low warning threshold.
  * **HIGH_WARNING:** The value has crossed above the high warning threshold.
  * **LOW_ALARM:** The value has crossed below the low alarm threshold.
  * **HIGH_ALARM:** The value has crossed above the high alarm threshold.

  
`links[].lacpStatus` | The LACP information for the single link.  
`links[].lacpStatus.state` | 

  * **ACTIVE:** The link is configured and active within the bundle.
  * **DETACHED:** The link is not configured within the bundle; this state is used when the `bundleAggregationType` is `STATIC`.

  
`links[].lacpStatus.googleSystemId` | The system ID of the port on the Google Cloud side of the LACP exchange.  
`links[].lacpStatus.neighborSystemId` | The system ID of the port on the remote cloud side of the LACP exchange.  
`links[].arpCache[]` | A list of `InterconnectDiagnostics.ARPEntry` objects, describing the ARP neighbor entries seen on this link. This is empty if the link is bundled.  
`links[].arpCache[].macAddress` | The MAC address of this ARP neighbor on this link.  
`links[].arpCache[].ipAddress` | The IP address of this ARP neighbor on this link.  
  
## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
