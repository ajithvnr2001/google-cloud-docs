---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout/
title: PatchRollout \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:51.358275+00:00
---

# PatchRollout  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  PatchRollout Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Mode
  * FixedOrPercent
    * JSON representation



Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout#Mode)),
      "disruptionBudget": {
        object ([FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout#FixedOrPercent))
      }
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout#Mode)`)` Mode of the patch rollout.  
`disruptionBudget` |  `object (`[FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchRollout#FixedOrPercent)`)` The maximum number (or percentage) of VMs per zone to disrupt at any given moment. The number of VMs calculated from multiplying the percentage by the total number of VMs in a zone is rounded up.During patching, a VM is considered disrupted from the time the agent is notified to begin until patching has completed. This disruption time includes the time to complete reboot and any post-patch steps.A VM contributes to the disruption budget if its patching operation fails either when applying the patches, running pre or post patch steps, or if it fails to respond with a success notification before timing out. VMs that are not running or do not have an active agent do not count toward this disruption budget.For zone-by-zone rollouts, if the disruption budget in a zone is exceeded, the patch job stops, because continuing to the next zone requires completion of the patch process in the previous zone.For example, if the disruption budget has a fixed value of `10`, and 8 VMs fail to patch in the current zone, the patch job continues to patch 2 VMs at a time until the zone is completed. When that zone is completed successfully, patching begins with 10 VMs at a time in the next zone. If 10 VMs in the next zone fail to patch, the patch job stops.  
  
## Mode

Type of the rollout.

Enums  
---  
`MODE_UNSPECIFIED` | Mode must be specified.  
`ZONE_BY_ZONE` | Patches are applied one zone at a time. The patch job begins in the region with the lowest number of targeted VMs. Within the region, patching begins in the zone with the lowest number of targeted VMs. If multiple regions (or zones within a region) have the same number of targeted VMs, a tie-breaker is achieved by sorting the regions or zones in alphabetical order.  
`CONCURRENT_ZONES` | Patches are applied to VMs in all zones at the same time.  
  
## FixedOrPercent

Message encapsulating a value that can be either absolute ("fixed") or relative ("percent") to a value.

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "fixed": integer,
      "percent": integer
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`. Type of the value. `mode` can be only one of the following:  
`fixed` |  `integer` Specifies a fixed value.  
`percent` |  `integer` Specifies the relative value defined as a percentage, which will be multiplied by a reference value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
