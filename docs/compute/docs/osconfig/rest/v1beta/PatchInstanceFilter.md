---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchInstanceFilter/
title: PatchInstanceFilter \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:34:51.614009+00:00
---

# PatchInstanceFilter  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchInstanceFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  PatchInstanceFilter Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GroupLabel
    * JSON representation



A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones.

JSON representation  
---  
      
    
    {
      "all": boolean,
      "groupLabels": [
        {
          object ([GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchInstanceFilter#GroupLabel))
        }
      ],
      "zones": [
        string
      ],
      "instances": [
        string
      ],
      "instanceNamePrefixes": [
        string
      ]
    }  
  
Fields  
---  
`all` |  `boolean` Target all VM instances in the project. If true, no other criteria is permitted.  
`groupLabels[]` |  `object (`[GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/PatchInstanceFilter#GroupLabel)`)` Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".  
`zones[]` |  `string` Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.  
`instances[]` |  `string` Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`  
`instanceNamePrefixes[]` |  `string` Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".  
  
## GroupLabel

Represents a group of VMs that can be identified as having all these labels, for example "env=prod and app=web".

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Compute Engine instance labels that must be present for a VM instance to be targeted by this filter.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
