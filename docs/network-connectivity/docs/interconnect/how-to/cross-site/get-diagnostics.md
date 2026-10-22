---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/get-diagnostics/
title: Get diagnostics \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:41.650629+00:00
---

# Get diagnostics  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/get-diagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Get diagnostics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Interconnect diagnostics let you troubleshoot your Cross-Site Interconnect connections during provisioning and after activation.

The diagnostics provide you detailed technical information about the Google Cloud Cross-Site Interconnect connections on demand.

## Diagnostics during outages

In the event of a [global outage](https://status.cloud.google.com/), don't use the diagnostics results from your Cross-Site Interconnect connection to make decisions about where to redirect your network traffic. A Cross-Site Interconnect connection is a global resource. A global outage can prevent the diagnostics for Cloud Interconnect from functioning properly.

## Diagnostics during provisioning

Viewing diagnostics provides you with the information required to troubleshoot and fix problems in your on-premises router configuration, which can be helpful if your Cross-Site Interconnect connection fails to progress through the provisioning process.

The diagnostics results contain different data depending on what stage in the provisioning process your Cross-Site Interconnect connection is in. The major and minor steps are listed in the next section. This diagnostic information provides you with possible next steps to take to help ensure that the provisioning process progresses without further issues.

Use the command output reference to interpret diagnostic command results or the information provided in the Google Cloud console.

### Provisioning stages

The Cross-Site Interconnect connection provisioning process occurs in the following stages. You must meet the requirements in stage 1 before you can move on to stage 2:

  * **Stage 1, circuit connection**

    * The optical power state is `OK` for each link in the connection.
  * **Stage 2, production configuration**

    * The optical power state is `OK` for each link in the connection.
    * A temporary IP address is assigned to the untagged bundle interface. Google Cloud verifies connectivity through a ping. The test IP address is removed when the activation process is complete.



## Use diagnostics

To see diagnostics information for the Cross-Site Interconnect connection, follow these steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.get`
  * `compute.interconnects.use`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Physical connections** tab, select the name of a Cross-Site Interconnect connection.

  3. Diagnostics information is in the following locations on the connection details page:

     * For warnings or errors, see the **Status** field.
     * For the provisioned capacity of the Cross-Site Interconnect, see the **Provisioned capacity** field.
     * For additional details, such as link status and light levels, see the **Link circuit info** section.
     * For details such as the effective capacity of the connection or status of its wire groups, see the **Wire groups** section.



###  gcloud 

Use the [`gcloud compute interconnects get-diagnostics` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/get-diagnostics):
    
    
    gcloud compute interconnects get-diagnostics NAME \
        --project=PROJECT_ID
    

Replace the following:

  * `NAME`: the name of the Cross-Site Interconnect connection in your project
  * `PROJECT_ID`: the ID of the Google Cloud project



###  API 

Use the [`interconnects.getDiagnostics` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/getDiagnostics):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/interconnects/NAME/getDiagnostics
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `NAME`: the name of the Cross-Site Interconnect connection in your project



If this command succeeds, it returns `InterconnectDiagnostics` output. To interpret the output, see the command output reference later in this document.

## Command output reference

The definitions for the output parameters for the `gcloud` commands and the [`interconnects.getDiagnostics`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/getDiagnostics) API are listed in the following table.

**Note:** If you want to trigger warnings for the value of the transmitting and receiving optical power in your on-premises routers, you can take a known good optical value, give it a 10% margin, and trigger warnings relative to that value. In general, a `-7dBm` warning and a `-11dBm` alarm are good optical value estimates for most links.Output parameter | Description  
---|---  
`macAddress` | Describes the MAC address of the Cross-Site Interconnect connection bundle on the Google Cloud side.  
`links[]` | Describes the status for each link on the Cross-Site Interconnect connection.  
`links[].circuitId` | Lists the Google-assigned unique ID for this circuit, as assigned during circuit turn-up.  
`links[].googleDemarc` | Describes the Google-assigned demarc, as assigned at circuit turn-up and provided by Google to the customer in the LOA.  
`links[].macsec` | The link's MACsec state. This field is omitted if you don't have MACsec enabled.  
`links[].macsec.ckn` | The connectivity association key name (CKN) in use. This field is omitted if you don't have MACsec enabled.  
`links[].macsec.operational` | The link's MACsec state. This field is omitted if you don't have MACsec enabled. The following are the possible values:

  * `TRUE:` MACsec is operational on the link.
  * `FALSE:` MACsec isn't operational on the link.

  
`links[].operationalState` | The operational state of this Cross-Site Interconnect link. This field is omitted if you don't have MACsec enabled. The following are the possible fixed values:

  * `LINK_OPERATIONAL_STATUS_UP:` The link is operational.
  * `LINK_OPERATIONAL_STATUS_DOWN:` The link isn't operational.

The link's operational state isn't affected by the link's MACsec state.  
`links[].receivingOpticalPower` | Describes the current value and status for the received light level.  
`links[].receivingOpticalPower.value` | Lists the current value of the received light level, in dBm.  
`links[].receivingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the receiving transceiver. The following are the possible fixed values:

  * `OK:` The value has not crossed a warning threshold.
  * `LOW_WARNING:` The value has crossed below the low warning threshold.
  * `HIGH_WARNING:` The value has crossed above the high warning threshold.
  * `LOW_ALARM:` The value has crossed below the low alarm threshold.
  * `HIGH_ALARM:` The value has crossed above the high alarm threshold.

  
`links[].transmittingOpticalPower` | The current value and status for the transmit light level.  
`links[].transmittingOpticalPower.value` | The current value of the transmitting light level, in [dBm](https://wikipedia.org/wiki/DBm).  
`links[].transmittingOpticalPower.state` | The status of the current value when compared to the warning and alarm levels for the transmitting transceiver:

  * `OK:` The value has not crossed a warning threshold.
  * `LOW_WARNING:` The value has crossed below the low warning threshold.
  * `HIGH_WARNING:` The value has crossed above the high warning threshold.
  * `LOW_ALARM:` The value has crossed below the low alarm threshold.
  * `HIGH_ALARM:` The value has crossed above the high alarm threshold.

  
`links[].lacpStatus` | The LACP information for the single link.  
`links[].lacpStatus.state` | 

  * `DETACHED:` The link is not configured within the bundle.

  
  
## What's next

  * To create a Cross-Site Interconnect connection, see the [Cross-Site Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
