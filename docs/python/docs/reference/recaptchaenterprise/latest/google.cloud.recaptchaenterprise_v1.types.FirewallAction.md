---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction
title: Class FirewallAction (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:56.031602+00:00
---

# Class FirewallAction (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FirewallAction (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    FirewallAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An individual action. Each action represents what to do if a policy matches.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`allow` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.AllowAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.AllowAction)`   
The user request did not match any policy and should be allowed access to the requested resource. This field is a member of `oneof`_ `firewall_action_oneof`.   
`block` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.BlockAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.BlockAction)`   
This action denies access to a given page. The user gets an HTTP error code. This field is a member of `oneof`_ `firewall_action_oneof`.   
`include_recaptcha_script` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.IncludeRecaptchaScriptAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.IncludeRecaptchaScriptAction)`   
This action injects reCAPTCHA JavaScript code into the HTML page returned by the site backend. This field is a member of `oneof`_ `firewall_action_oneof`.   
`redirect` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.RedirectAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.RedirectAction)`   
This action redirects the request to a reCAPTCHA interstitial to attach a token. This field is a member of `oneof`_ `firewall_action_oneof`.   
`substitute` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.SubstituteAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.SubstituteAction)`   
This action transparently serves a different page to an offending user. This field is a member of `oneof`_ `firewall_action_oneof`.   
`set_header` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallAction.SetHeaderAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction.SetHeaderAction)`   
This action sets a custom header but allow the request to continue to the customer backend. This field is a member of `oneof`_ `firewall_action_oneof`.   
  
## Classes 

### AllowAction
    
    
    AllowAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An allow action continues processing a request unimpeded.

### BlockAction
    
    
    BlockAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A block action serves an HTTP error code a prevents the request from hitting the backend.

### IncludeRecaptchaScriptAction
    
    
    IncludeRecaptchaScriptAction(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

An include reCAPTCHA script action involves injecting reCAPTCHA JavaScript code into the HTML returned by the site backend. This reCAPTCHA script is tasked with collecting user signals on the requested web page, issuing tokens as a cookie within the site domain, and enabling their utilization in subsequent page requests.

### RedirectAction
    
    
    RedirectAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A redirect action returns a 307 (temporary redirect) response, pointing the user to a reCAPTCHA interstitial page to attach a token.

### SetHeaderAction
    
    
    SetHeaderAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A set header action sets a header and forwards the request to the backend. This can be used to trigger custom protection implemented on the backend.

### SubstituteAction
    
    
    SubstituteAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A substitute action transparently serves a different page than the one requested.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
