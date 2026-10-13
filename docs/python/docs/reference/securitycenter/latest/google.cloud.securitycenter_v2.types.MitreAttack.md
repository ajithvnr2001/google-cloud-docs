---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack
title: Class MitreAttack (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:23.019098+00:00
---

# Class MitreAttack (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MitreAttack (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    MitreAttack(mapping=None, *, ignore_unknown_fields=False, **kwargs)

MITRE ATT&CK tactics and techniques related to this finding. See: <https://attack.mitre.org>

## Attributes  
  
---  
**Name** | **Description**  
`primary_tactic` |  `[google.cloud.securitycenter_v2.types.MitreAttack.Tactic](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack.Tactic)`   
The MITRE ATT&CK tactic most closely represented by this finding, if any.   
`primary_techniques` |  `MutableSequence[[google.cloud.securitycenter_v2.types.MitreAttack.Technique](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack.Technique)]`   
The MITRE ATT&CK technique most closely represented by this finding, if any. primary_techniques is a repeated field because there are multiple levels of MITRE ATT&CK techniques. If the technique most closely represented by this finding is a sub-technique (e.g. `SCANNING_IP_BLOCKS`), both the sub-technique and its parent technique(s) will be listed (e.g. `SCANNING_IP_BLOCKS`, `ACTIVE_SCANNING`).   
`additional_tactics` |  `MutableSequence[[google.cloud.securitycenter_v2.types.MitreAttack.Tactic](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack.Tactic)]`   
Additional MITRE ATT&CK tactics related to this finding, if any.   
`additional_techniques` |  `MutableSequence[[google.cloud.securitycenter_v2.types.MitreAttack.Technique](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MitreAttack.Technique)]`   
Additional MITRE ATT&CK techniques related to this finding, if any, along with any of their respective parent techniques.   
`version` |  `str`   
The MITRE ATT&CK version referenced by the above fields. E.g. "8".   
  
## Classes 

### Tactic
    
    
    Tactic(value)

MITRE ATT&CK tactics that can be referenced by SCC findings. See: <https://attack.mitre.org/tactics/enterprise/>

### Technique
    
    
    Technique(value)

MITRE ATT&CK techniques that can be referenced by Security Command Center findings. See: <https://attack.mitre.org/techniques/enterprise/>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
