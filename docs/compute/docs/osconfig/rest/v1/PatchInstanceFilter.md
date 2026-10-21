---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter/
title: PatchInstanceFilter \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:56.791353+00:00
---

# PatchInstanceFilter  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter/

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
          object ([GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter#GroupLabel))
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
`groupLabels[]` |  `object (`[GroupLabel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter#GroupLabel)`)` Targets VM instances matching ANY of these GroupLabels. This allows targeting of disparate groups of VM instances.  
`zones[]` |  `string` Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.  
`instances[]` |  `string` Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`  
`instanceNamePrefixes[]` |  `string` Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".  
  
## GroupLabel

Targets a group of VM instances by using their [assigned labels](https://cloud.google.com/compute/docs/labeling-resources). Labels are key-value pairs. A `GroupLabel` is a combination of labels that is used to target VMs for a patch job.

For example, a patch job can target VMs that have the following `GroupLabel`: `{"env":"test", "app":"web"}`. This means that the patch job is applied to VMs that have both the labels `env=test` and `app=web`.

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
