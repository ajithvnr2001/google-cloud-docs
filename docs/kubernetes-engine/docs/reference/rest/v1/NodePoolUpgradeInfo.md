---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo/
title: NodePoolUpgradeInfo \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:22.836568+00:00
---

# NodePoolUpgradeInfo  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  NodePoolUpgradeInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AutoUpgradeStatus
  * AutoUpgradePausedReason
  * CustomImageInfo
    * JSON representation



NodePoolUpgradeInfo contains the upgrade information of a node pool.

JSON representation  
---  
      
    
    {
      "autoUpgradeStatus": [
        enum ([AutoUpgradeStatus](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#AutoUpgradeStatus))
      ],
      "pausedReason": [
        enum ([AutoUpgradePausedReason](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#AutoUpgradePausedReason))
      ],
      "upgradeDetails": [
        {
          object ([UpgradeDetails](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeDetails))
        }
      ],
      "customImageInfo": {
        object ([CustomImageInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#CustomImageInfo))
      },
      "minorTargetVersion": string,
      "patchTargetVersion": string,
      "endOfStandardSupportTimestamp": string,
      "endOfExtendedSupportTimestamp": string
    }  
  
Fields  
---  
`autoUpgradeStatus[]` |  `enum (`[AutoUpgradeStatus](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#AutoUpgradeStatus)`)` The auto upgrade status.  
`pausedReason[]` |  `enum (`[AutoUpgradePausedReason](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#AutoUpgradePausedReason)`)` The auto upgrade paused reason.  
`upgradeDetails[]` |  `object (`[UpgradeDetails](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeDetails)`)` The list of past auto upgrades.  
`customImageInfo` |  `object (`[CustomImageInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolUpgradeInfo#CustomImageInfo)`)` Output only. Upgrade info for the node pool specific to the usage of custom images.  
`minorTargetVersion` |  `string` minorTargetVersion indicates the target version for minor upgrade.  
`patchTargetVersion` |  `string` patchTargetVersion indicates the target version for patch upgrade.  
`endOfStandardSupportTimestamp` |  `string` The node pool's current minor version's end of standard support timestamp.  
`endOfExtendedSupportTimestamp` |  `string` The node pool's current minor version's end of extended support timestamp.  
  
## AutoUpgradeStatus

AutoUpgradeStatus indicates the status of auto upgrade.

Enums  
---  
`UNKNOWN` | UNKNOWN indicates an unknown status.  
`ACTIVE` | ACTIVE indicates an active status.  
`MINOR_UPGRADE_PAUSED` | MINOR_UPGRADE_PAUSED indicates the minor version upgrade is paused.  
`UPGRADE_PAUSED` | UPGRADE_PAUSED indicates the upgrade is paused.  
  
## AutoUpgradePausedReason

AutoUpgradePausedReason indicates the reason for auto upgrade paused status.

Enums  
---  
`AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED` | AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED indicates an unspecified reason.  
`MAINTENANCE_WINDOW` | MAINTENANCE_WINDOW indicates the cluster is outside customer maintenance window.  
`MAINTENANCE_EXCLUSION_NO_UPGRADES` | MAINTENANCE_EXCLUSION_NO_UPGRADES indicates the cluster is in a maintenance exclusion with scope NO_UPGRADES.  
`MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES` | MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES indicates the cluster is in a maintenance exclusion with scope NO_MINOR_UPGRADES.  
`SYSTEM_CONFIG` | SYSTEM_CONFIG indicates the cluster upgrade is paused by system config.  
  
## CustomImageInfo

Contains the custom image info for a node pool.

JSON representation  
---  
      
    
    {
      "upgradeMessage": string
    }  
  
Fields  
---  
`upgradeMessage` |  `string` Output only. The human-readable upgrade message for the custom image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
