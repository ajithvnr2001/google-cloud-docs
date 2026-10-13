---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.AccessRulesOptions
title: Class AccessRulesOptions (0.4.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:21.729506+00:00
---

# Class AccessRulesOptions (0.4.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.AccessRulesOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccessRulesOptions (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.4.2  0.3.0  0.2.0  0.1.2 
    
    
    AccessRulesOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

IP-based access rules for the Managed Lustre instance. These options define the root user squash configuration.

## Attributes  
  
---  
**Name** | **Description**  
`access_rules` |  `MutableSequence[[google.cloud.lustre_v1.types.AccessRulesOptions.AccessRule](https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.AccessRulesOptions.AccessRule)]`   
Optional. The access rules for the instance.   
`default_squash_mode` |  `[google.cloud.lustre_v1.types.AccessRulesOptions.SquashMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.AccessRulesOptions.SquashMode)`   
Required. The squash mode for the default access rule.   
`default_squash_uid` |  `int`   
Optional. The user squash UID for the default access rule. This user squash UID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no UID squash).   
`default_squash_gid` |  `int`   
Optional. The user squash GID for the default access rule. This user squash GID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no GID squash).   
  
## Classes 

### AccessRule
    
    
    AccessRule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A single policy group with IP-based access rules for the Managed Lustre instance.

### SquashMode
    
    
    SquashMode(value)

Squash mode for an access rule.
    
    
        If set inside an
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.AccessRule">AccessRule</xref>,
        root users matching the `ip_ranges][AccessRule.ip_ranges]`
        are not squashed.
    
        If set as the
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_mode">default_squash_mode</xref>,
        root squash is disabled for this instance.
    
        If the default squash mode is `NO_SQUASH`, do not set the
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_uid">default_squash_uid</xref>
        or
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_gid">default_squash_gid</xref>,
        or an `invalid argument` error is returned.
    ROOT_SQUASH (2):
        Root user squash is enabled.
    
        Not supported inside an
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.AccessRule">AccessRule</xref>.
    
        If set as the
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_mode">default_squash_mode</xref>,
        root users not matching any of the
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.access_rules">access_rules</xref>
        are squashed to the
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_uid">default_squash_uid</xref>
        and
        <xref uid="google.cloud.lustre.v1.AccessRulesOptions.default_squash_gid">default_squash_gid</xref>.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
