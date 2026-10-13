---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ThreatPreventionProfile
title: Class ThreatPreventionProfile (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:48.175040+00:00
---

# Class ThreatPreventionProfile (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ThreatPreventionProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ThreatPreventionProfile (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    ThreatPreventionProfile(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ThreatPreventionProfile defines an action for specific threat signatures or severity levels.

## Attributes  
  
---  
**Name** | **Description**  
`severity_overrides` |  `MutableSequence[[google.cloud.network_security_v1alpha1.types.SeverityOverride](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.SeverityOverride)]`   
Optional. Configuration for overriding threats actions by severity match.   
`threat_overrides` |  `MutableSequence[[google.cloud.network_security_v1alpha1.types.ThreatOverride](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ThreatOverride)]`   
Optional. Configuration for overriding threats actions by threat_id match. If a threat is matched both by configuration provided in severity_overrides and threat_overrides, the threat_overrides action is applied.   
`antivirus_overrides` |  `MutableSequence[[google.cloud.network_security_v1alpha1.types.AntivirusOverride](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AntivirusOverride)]`   
Optional. Configuration for overriding antivirus actions per protocol.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
