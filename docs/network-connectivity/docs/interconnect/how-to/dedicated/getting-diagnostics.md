---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics/
title: Get diagnostics \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:07.478271+00:00
---

# Get diagnostics  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Get diagnostics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Interconnect diagnostics let you troubleshoot your Dedicated Interconnect connections during provisioning and after activation.

The diagnostics provide you current, detailed technical information about the Google Cloud side of the Dedicated Interconnect connections on demand.

## Diagnostics during outages

In the event of a [global outage](https://status.cloud.google.com/), don't use the diagnostics results from your Dedicated Interconnect connection to make decisions about where to redirect your network traffic.

Unlike a VLAN attachment, which is regional, a Dedicated Interconnect connection is a global resource. A global outage can prevent the diagnostics for Cloud Interconnect from functioning properly.

## Diagnostics during provisioning

Viewing diagnostics provides you with the information required to troubleshoot and fix problems in your on-premises router configuration, which can be helpful if your Dedicated Interconnect connection fails to progress through the provisioning process.

The diagnostics results contain different data depending on what stage in the provisioning process your Dedicated Interconnect connection is in. The major and minor steps are listed in the next section. This diagnostic information provides you with possible next steps to take so that the provisioning process progresses without further issues.

Use the command output reference to interpret diagnostic command results or the information provided in the Google Cloud console.

### Provisioning stages

The Dedicated Interconnect connection provisioning process occurs in multiple stages. You must meet the following requirements in each stage before you can move on to the next one:

  * **Stage 1 - Circuit Connection:**

    * The optical power state is `OK` for each link in the connection.
  * **Stage 2 - Circuit Qualification (only for connections that have multiple links):**

    * The optical power state is `OK` for each link in the connection.
    * Each link is assigned a temporary IP address. The address is used to qualify each link individually through a ping test.
    * Address Resolution Protocol (ARP) entries are present.
  * **Stage 3 - Production Configuration:**

    * The optical power state is `OK` for each link in the connection.
    * All links in the connection are configured in an LACP bundle.
    * A temporary IP address is assigned to the untagged bundle interface. Google Cloud verifies connectivity through a ping. The test IP address is removed when the activation process is complete.
    * ARP entries are present.



## Use diagnostics

To see diagnostics information for the Dedicated Interconnect connection, follow these steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.get`
  * `compute.interconnects.use`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the name of a Dedicated Interconnect connection.

  3. Diagnostics information is in the following locations on the connection details page:

     * For warnings or errors, see the **Status** field.
     * For the provisioned capacity of the Dedicated Interconnect, see the **Provisioned capacity** field.
     * If you suspect issues with the Dedicated Interconnect connection, see the **VLAN attachments** section for information such as the effective capacity of the connection or the number of down links.
     * For additional details, such as light levels, see the **Link circuit info** section.



###  gcloud 

Use the `gcloud compute interconnects get-diagnostics` command:
    
    
    gcloud compute interconnects get-diagnostics NAME
        --project=PROJECT_ID
    

Replace the following:

  * `NAME`: the name of the Dedicated Interconnect connection in your project
  * `PROJECT_ID`: the ID of the Google Cloud project



The output is similar to the following:
    
    
    macAddress: "00:11:22:33:44:55"
    arpCache:
      macAddress: "55:44:33:22:11:00"
      ipAddress: "1.2.3.4"
    links:
      - circuitId: "circuit-id-1"
        receivingOpticalPower:
          value: 0.4
          state: OK
        lacpStatus:
          state: ACTIVE
          googleSystemId: "00:11:22:33:44:55"
          neighborSystemId: "55:44:33:22:11:00"
         macsec:
          ckn: 0101010189abcdef...0123456789abcdef
          operational: true
      - circuitId: "circuit-id-2"
        receivingOpticalPower:
          value: 0.4
          state: OK
        lacpStatus:
          state: DETACHED
        macsec:
          ckn: 0101010189abcdef...0123456789abcdef
          operational: false
        arpCache:
          macAddress: "01:23:45:67:89:0a"
          ipAddress: "2.3.4.5"
    

###  API 

Use the [`interconnects.getDiagnostics` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/getDiagnostics):
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/global/interconnects/NAME/getDiagnostics
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `NAME`: the name of the Dedicated Interconnect connection in your project



If this command succeeds, it returns `InterconnectDiagnostics` output in the following format. To interpret the output, see the command output reference.
    
    
    {
      "macAddress": "00:11:22:33:44:55",
      "arpCache": [
        {
          "macAddress": "55:44:33:22:11:00",
          "ipAddress": "1.2.3.4"
        }
      ],
      "links": [
        {
          "circuitId": "circuit-id",
          "receivingOpticalPower": {
            "value": 0.4,
            "state": OK,
          },
          "lacpStatus": {
            "state": ACTIVE,
            "googleSystemId": "00:11:22:33:44:55",
            "neighborSystemId": "55:44:33:22:11:00"
          }
        },
        {
          "circuitId": "circuit-id",
          "receivingOpticalPower": {
            "value": 0.4,
            "state": OK,
          },
          "lacpStatus": {
            "state": DETACHED
          },
          "arpCache": [
            {
              "macAddress": "01:23:45:67:89:0a",
              "ipAddress": "2.3.4.5"
            }
          ]
        }
      ]
    }
    

### Use diagnostics from connection groups

You can also get aggregated diagnostics from all of the Cloud Interconnect connections in a connection group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectGroups.get`
  * `cloudasset.assets.listComputeInterconnect`
  * `cloudasset.assets.listComputeInterconnectAttachment`
  * `cloudasset.assets.listComputeNetworks`
  * `cloudasset.assets.listComputeRouters`
  * `cloudasset.assets.listComputeVpnGateways`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Interconnect Group Analyzer (`roles/compute.interconnectGroupAnalyzer`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. In the **Interconnect groups** table, select the name of a Dedicated Interconnect connection group.

  3. Diagnostics information is in the following locations on the group details page:

     * Near the top of the page, you can view the group's status and description.
     * Under the status and description, you can view how many of your connections are up, your intended SLA, and whether you are eligible for your intended SLA.
     * If there is a blocker preventing your connection group from meeting the requirements of your intended SLA, those blockers appear in the **SLA eligibility blockers** field under the previous section.
     * The table at the bottom of the page displays details about each connection in your connection group.



###  gcloud 

Use the `gcloud compute interconnects groups get-operational-status` command, replacing `NAME` with the name of the Dedicated Interconnect connection you want to check:
    
    
    gcloud compute interconnects groups get-operational-status NAME
    

### Use diagnostics from VLAN attachment groups

You can get aggregated diagnostics from all of the VLAN attachments in a VLAN attachment group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectAttachmentGroups.get`
  * `compute.routers.get`
  * `cloudasset.assets.listComputeInterconnect`
  * `cloudasset.assets.listComputeInterconnectAttachment`
  * `cloudasset.assets.listComputeNetworks`
  * `cloudasset.assets.listComputeRouters`
  * `cloudasset.assets.listComputeVpnGateways`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Interconnect Attachment Group Analyzer (`roles/compute.interconnectAttachmentGroupAnalyzer`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment group that you want to edit.

  3. Diagnostics information is in the following locations on the group details page:

     * Near the top of the page, you can view the group's status and description.
     * Under the status and description, you can view how many of your VLAN attachments are up, your intended SLA, and whether you are eligible for your intended SLA.
     * If there is a blocker preventing your VLAN attachment group from meeting the requirements of your intended SLA, those blockers appear in the **SLA eligibility blockers** field under the previous section.
     * The table at the bottom of the page displays details about each VLAN attachment in your VLAN attachment group.



###  gcloud 

Use the `gcloud compute interconnects attachments groups get-operational-status` command:
    
    
    gcloud compute interconnects attachments groups get-operational-status NAME
    

Replace the following:

  * `NAME`: the name of the VLAN attachment group in your project



The output is similar to the following:
    
    
    result:
    attachmentStatuses:
    - adminEnabled: true
      attachment: https://www.googleapis.com/compute/v1/projects/equinix-gci-testing/regions/us-west2/interconnectAttachments/byohsm-lab-sfo-attachment3
      isActive: ACTIVE
      status: CONNECTION_UP
    - adminEnabled: true
      attachment: https://www.googleapis.com/compute/v1/projects/equinix-gci-testing/regions/us-west2/interconnectAttachments/ccsw03-sfo05-z1-a1
      isActive: ACTIVE
      status: CONNECTION_UP
    configured:
      availabilitySla:
        effectiveSla: PRODUCTION_NON_CRITICAL
    groupStatus: FULLY_UP
    intent:
      availabilitySla: PRODUCTION_NON_CRITICAL
    operational:
      availabilitySla:
        effectiveSla: PRODUCTION_NON_CRITICAL
    

## Command output reference

The definitions for the output parameters for the Google Cloud CLI commands and the [`interconnects.getDiagnostics`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/getDiagnostics) API are listed in the following table.

**Note:** If you want to trigger warnings for the value of the transmitting and receiving optical power in your on-premises routers, you can take a known good optical value, give it a 10% margin, and trigger warnings relative to that value. In general, a `-7dBm` warning and a `-11dBm` alarm are good optical value estimates for most links.Output parameter | Description  
---|---  
`macAddress` | Describes the MAC address of the Dedicated Interconnect connection bundle on the Google Cloud side.  
`arpCache` | Describes individual neighbors seen by the Cloud Router in the ARP cache for the Dedicated Interconnect connection. This is empty when the connection isn't bundled.  
`arpCache[].macAddress` | Lists the MAC address of this ARP neighbor.  
`arpCache[].ipAddress` | Lists the IP address of this ARP neighbor.  
`links[]` | Describes the status for each link on the Dedicated Interconnect connection.  
`links[].circuitId` | Lists the Google-assigned unique ID for this circuit, as assigned during circuit turn-up.  
`links[].googleDemarc` | Describes the Google-assigned demarc, as assigned at circuit turn-up and provided by Google to the customer in the LOA.  
`links[].macsec` | The link's MACsec state. This field is omitted if you don't have MACsec enabled.  
`links[].macsec.ckn` | The connectivity association key name (CKN) in use. This field is omitted if you don't have MACsec enabled.  
`links[].macsec.operational` | The link's MACsec state. This field is omitted if you don't have MACsec enabled. The following are the possible values:

  * **TRUE:** MACsec is operational on the link.
  * **FALSE:** MACsec isn't operational on the link.

  
`links[].operationalState` | The operational state of this Dedicated Interconnect link. This field is omitted if you don't have MACsec enabled. The following are the possible fixed values:

  * **LINK_OPERATIONAL_STATUS_UP:** The link is operational.
  * **LINK_OPERATIONAL_STATUS_DOWN:** The link isn't operational.

The link's operational state isn't affected by the link's MACsec state.  
`links[].receivingOpticalPower` | Describes the current value and status for the received light level.  
`links[].receivingOpticalPower.value` | Lists the current value of the received light level, in [dBm](https://wikipedia.org/wiki/DBm).  
`links[].receivingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the receiving transceiver:

  * **OK:** The value has not crossed a warning threshold.
  * **LOW_WARNING:** The value has crossed below the low warning threshold.
  * **HIGH_WARNING:** The value has crossed above the high warning threshold.
  * **LOW_ALARM:** The value has crossed below the low alarm threshold.
  * **HIGH_ALARM:** The value has crossed above the high alarm threshold.

  
`links[].transmittingOpticalPower` | The current value and status for the transmit light level.  
`links[].transmittingOpticalPower.value` | The current value of the transmitting light level, in dBm.  
`links[].transmittingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the transmitting transceiver. The following are the possible fixed values:

  * **OK:** The value has not crossed a warning threshold.
  * **LOW_WARNING:** The value has crossed below the low warning threshold.
  * **HIGH_WARNING:** The value has crossed above the high warning threshold.
  * **LOW_ALARM:** The value has crossed below the low alarm threshold.
  * **HIGH_ALARM:** The value has crossed above the high alarm threshold.

  
`links[].lacpStatus` | The LACP information for the single link.  
`links[].lacpStatus.state` | 

  * **ACTIVE:** The link is configured and active within the bundle.
  * **DETACHED:** The link isn't configured within the bundle.

  
`links[].lacpStatus.googleSystemId` | The system ID of the port on the Google Cloud side of the LACP exchange.  
`links[].lacpStatus.neighborSystemId` | The system ID of the port on the customer's side of the LACP exchange.  
`links[].arpCache[]` | A list of `InterconnectDiagnostics.ARPEntry` objects, describing the ARP neighbor entries seen on this link. This is empty if the link is bundled.  
`links[].arpCache[].macAddress` | The MAC address of this ARP neighbor on this link.  
`links[].arpCache[].ipAddress` | The IP address of this ARP neighbor on this link.  
  
## What's next

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
