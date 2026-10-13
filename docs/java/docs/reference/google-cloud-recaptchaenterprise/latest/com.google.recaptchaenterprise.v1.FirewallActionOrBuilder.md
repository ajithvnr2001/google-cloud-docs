---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallActionOrBuilder
title: Interface FirewallActionOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:39.906807+00:00
---

# Interface FirewallActionOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallActionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FirewallActionOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface FirewallActionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllow()
    
    
    public abstract FirewallAction.AllowAction getAllow()

The user request did not match any policy and should be allowed access to the requested resource.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.AllowAction allow = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.AllowAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.AllowAction)` | The allow.  
  
### getAllowOrBuilder()
    
    
    public abstract FirewallAction.AllowActionOrBuilder getAllowOrBuilder()

The user request did not match any policy and should be allowed access to the requested resource.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.AllowAction allow = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.AllowActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.AllowActionOrBuilder)` |   
  
### getBlock()
    
    
    public abstract FirewallAction.BlockAction getBlock()

This action denies access to a given page. The user gets an HTTP error code.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.BlockAction block = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.BlockAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.BlockAction)` | The block.  
  
### getBlockOrBuilder()
    
    
    public abstract FirewallAction.BlockActionOrBuilder getBlockOrBuilder()

This action denies access to a given page. The user gets an HTTP error code.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.BlockAction block = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.BlockActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.BlockActionOrBuilder)` |   
  
### getFirewallActionOneofCase()
    
    
    public abstract FirewallAction.FirewallActionOneofCase getFirewallActionOneofCase()

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.FirewallActionOneofCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.FirewallActionOneofCase)` |   
  
### getIncludeRecaptchaScript()
    
    
    public abstract FirewallAction.IncludeRecaptchaScriptAction getIncludeRecaptchaScript()

This action injects reCAPTCHA JavaScript code into the HTML page returned by the site backend.

` .google.cloud.recaptchaenterprise.v1.FirewallAction.IncludeRecaptchaScriptAction include_recaptcha_script = 6; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.IncludeRecaptchaScriptAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.IncludeRecaptchaScriptAction)` | The includeRecaptchaScript.  
  
### getIncludeRecaptchaScriptOrBuilder()
    
    
    public abstract FirewallAction.IncludeRecaptchaScriptActionOrBuilder getIncludeRecaptchaScriptOrBuilder()

This action injects reCAPTCHA JavaScript code into the HTML page returned by the site backend.

` .google.cloud.recaptchaenterprise.v1.FirewallAction.IncludeRecaptchaScriptAction include_recaptcha_script = 6; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.IncludeRecaptchaScriptActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.IncludeRecaptchaScriptActionOrBuilder)` |   
  
### getRedirect()
    
    
    public abstract FirewallAction.RedirectAction getRedirect()

This action redirects the request to a reCAPTCHA interstitial to attach a token.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.RedirectAction redirect = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.RedirectAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.RedirectAction)` | The redirect.  
  
### getRedirectOrBuilder()
    
    
    public abstract FirewallAction.RedirectActionOrBuilder getRedirectOrBuilder()

This action redirects the request to a reCAPTCHA interstitial to attach a token.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.RedirectAction redirect = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.RedirectActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.RedirectActionOrBuilder)` |   
  
### getSetHeader()
    
    
    public abstract FirewallAction.SetHeaderAction getSetHeader()

This action sets a custom header but allow the request to continue to the customer backend.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SetHeaderAction set_header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.SetHeaderAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.SetHeaderAction)` | The setHeader.  
  
### getSetHeaderOrBuilder()
    
    
    public abstract FirewallAction.SetHeaderActionOrBuilder getSetHeaderOrBuilder()

This action sets a custom header but allow the request to continue to the customer backend.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SetHeaderAction set_header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.SetHeaderActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.SetHeaderActionOrBuilder)` |   
  
### getSubstitute()
    
    
    public abstract FirewallAction.SubstituteAction getSubstitute()

This action transparently serves a different page to an offending user.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SubstituteAction substitute = 3; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.SubstituteAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.SubstituteAction)` | The substitute.  
  
### getSubstituteOrBuilder()
    
    
    public abstract FirewallAction.SubstituteActionOrBuilder getSubstituteOrBuilder()

This action transparently serves a different page to an offending user.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SubstituteAction substitute = 3; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallAction.SubstituteActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallAction.SubstituteActionOrBuilder)` |   
  
### hasAllow()
    
    
    public abstract boolean hasAllow()

The user request did not match any policy and should be allowed access to the requested resource.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.AllowAction allow = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allow field is set.  
  
### hasBlock()
    
    
    public abstract boolean hasBlock()

This action denies access to a given page. The user gets an HTTP error code.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.BlockAction block = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the block field is set.  
  
### hasIncludeRecaptchaScript()
    
    
    public abstract boolean hasIncludeRecaptchaScript()

This action injects reCAPTCHA JavaScript code into the HTML page returned by the site backend.

` .google.cloud.recaptchaenterprise.v1.FirewallAction.IncludeRecaptchaScriptAction include_recaptcha_script = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the includeRecaptchaScript field is set.  
  
### hasRedirect()
    
    
    public abstract boolean hasRedirect()

This action redirects the request to a reCAPTCHA interstitial to attach a token.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.RedirectAction redirect = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the redirect field is set.  
  
### hasSetHeader()
    
    
    public abstract boolean hasSetHeader()

This action sets a custom header but allow the request to continue to the customer backend.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SetHeaderAction set_header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the setHeader field is set.  
  
### hasSubstitute()
    
    
    public abstract boolean hasSubstitute()

This action transparently serves a different page to an offending user.

`.google.cloud.recaptchaenterprise.v1.FirewallAction.SubstituteAction substitute = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the substitute field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
