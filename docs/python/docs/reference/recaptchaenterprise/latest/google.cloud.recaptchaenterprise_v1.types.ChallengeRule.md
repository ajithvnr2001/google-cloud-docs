---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRule
title: Class ChallengeRule (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:54.724996+00:00
---

# Class ChallengeRule (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ChallengeRule (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    ChallengeRule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A rule to configure the behavior of reCAPTCHA for conditionally presenting a challenge.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`condition` |  `str`   
Optional. A CEL condition that must be met for this rule to apply. If unspecified, the rule applies unconditionally. The following fields can be referenced in the condition: \- `score` \- `user_ip_address` \- `user_asn` \- `user_agent` \- `verified_bots.name` \- `verified_bots.bot_type` Examples: \- `score <>` \- `user_ip_address == "123.45.67.89"` \- `user_agent.contains("Chrome")` \- `score < 0.5="" &&="" user_ip_address="=">`  
`no_challenge` |  `[google.cloud.recaptchaenterprise_v1.types.ChallengeRule.NoChallengeOutcome](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRule.NoChallengeOutcome)`   
Do not present a challenge to the user. This field is a member of `oneof`_ `outcome`.   
`challenge` |  `[google.cloud.recaptchaenterprise_v1.types.ChallengeRule.ChallengeOutcome](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRule.ChallengeOutcome)`   
Present a challenge to the user. This field is a member of `oneof`_ `outcome`.   
  
## Classes 

### ChallengeOutcome
    
    
    ChallengeOutcome(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An outcome that indicates that a challenge of a specified difficulty should be presented to the user.

### NoChallengeOutcome
    
    
    NoChallengeOutcome(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An outcome that indicates that no challenge should be presented to the user.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
