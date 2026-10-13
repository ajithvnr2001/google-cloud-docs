---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRuleOrBuilder
title: Interface CustomInfoType.DetectionRule.HotwordRuleOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:44.986066+00:00
---

# Interface CustomInfoType.DetectionRule.HotwordRuleOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRuleOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomInfoType.DetectionRule.HotwordRuleOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.7  3.5.0  3.4.0  3.3.2  3.2.1  3.1.4 
    
    
    public static interface CustomInfoType.DetectionRule.HotwordRuleOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getHotwordRegex()
    
    
    public abstract CustomInfoType.Regex getHotwordRegex()

Regular expression pattern defining what qualifies as a hotword.

`.google.privacy.dlp.v2.CustomInfoType.Regex hotword_regex = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex)` | The hotwordRegex.  
  
### getHotwordRegexOrBuilder()
    
    
    public abstract CustomInfoType.RegexOrBuilder getHotwordRegexOrBuilder()

Regular expression pattern defining what qualifies as a hotword.

`.google.privacy.dlp.v2.CustomInfoType.Regex hotword_regex = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.RegexOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.RegexOrBuilder)` |   
  
### getLikelihoodAdjustment()
    
    
    public abstract CustomInfoType.DetectionRule.LikelihoodAdjustment getLikelihoodAdjustment()

Likelihood adjustment to apply to all matching findings.

` .google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment likelihood_adjustment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.DetectionRule.LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment)` | The likelihoodAdjustment.  
  
### getLikelihoodAdjustmentOrBuilder()
    
    
    public abstract CustomInfoType.DetectionRule.LikelihoodAdjustmentOrBuilder getLikelihoodAdjustmentOrBuilder()

Likelihood adjustment to apply to all matching findings.

` .google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment likelihood_adjustment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.DetectionRule.LikelihoodAdjustmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustmentOrBuilder)` |   
  
### getProximity()
    
    
    public abstract CustomInfoType.DetectionRule.Proximity getProximity()

Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The finding itself will be included in the window, so that hotwords can be used to match substrings of the finding itself. Suppose you want Cloud DLP to promote the likelihood of the phone number regex "\\(\d{3}\\) \d{3}-\d{4}" if the area code is known to be the area code of a company's office. In this case, use the hotword regex "\\(xxx\\)", where "xxx" is the area code in question.

For tabular data, if you want to modify the likelihood of an entire column of findngs, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).

`.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity proximity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.DetectionRule.Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity)` | The proximity.  
  
### getProximityOrBuilder()
    
    
    public abstract CustomInfoType.DetectionRule.ProximityOrBuilder getProximityOrBuilder()

Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The finding itself will be included in the window, so that hotwords can be used to match substrings of the finding itself. Suppose you want Cloud DLP to promote the likelihood of the phone number regex "\\(\d{3}\\) \d{3}-\d{4}" if the area code is known to be the area code of a company's office. In this case, use the hotword regex "\\(xxx\\)", where "xxx" is the area code in question.

For tabular data, if you want to modify the likelihood of an entire column of findngs, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).

`.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity proximity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CustomInfoType.DetectionRule.ProximityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.ProximityOrBuilder)` |   
  
### hasHotwordRegex()
    
    
    public abstract boolean hasHotwordRegex()

Regular expression pattern defining what qualifies as a hotword.

`.google.privacy.dlp.v2.CustomInfoType.Regex hotword_regex = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hotwordRegex field is set.  
  
### hasLikelihoodAdjustment()
    
    
    public abstract boolean hasLikelihoodAdjustment()

Likelihood adjustment to apply to all matching findings.

` .google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment likelihood_adjustment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the likelihoodAdjustment field is set.  
  
### hasProximity()
    
    
    public abstract boolean hasProximity()

Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The finding itself will be included in the window, so that hotwords can be used to match substrings of the finding itself. Suppose you want Cloud DLP to promote the likelihood of the phone number regex "\\(\d{3}\\) \d{3}-\d{4}" if the area code is known to be the area code of a company's office. In this case, use the hotword regex "\\(xxx\\)", where "xxx" is the area code in question.

For tabular data, if you want to modify the likelihood of an entire column of findngs, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).

`.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity proximity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the proximity field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
