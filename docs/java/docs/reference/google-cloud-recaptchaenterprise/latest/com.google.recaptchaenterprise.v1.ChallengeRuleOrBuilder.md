---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRuleOrBuilder
title: Interface ChallengeRuleOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:35.583259+00:00
---

# Interface ChallengeRuleOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRuleOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ChallengeRuleOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface ChallengeRuleOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChallenge()
    
    
    public abstract ChallengeRule.ChallengeOutcome getChallenge()

Present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.ChallengeOutcome challenge = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ChallengeRule.ChallengeOutcome](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRule.ChallengeOutcome)` | The challenge.  
  
### getChallengeOrBuilder()
    
    
    public abstract ChallengeRule.ChallengeOutcomeOrBuilder getChallengeOrBuilder()

Present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.ChallengeOutcome challenge = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ChallengeRule.ChallengeOutcomeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRule.ChallengeOutcomeOrBuilder)` |   
  
### getCondition()
    
    
    public abstract String getCondition()

Optional. A CEL condition that must be met for this rule to apply. If unspecified, the rule applies unconditionally. The following fields can be referenced in the condition:

  * `score`
  * `user_ip_address`
  * `user_asn`
  * `user_agent`
  * `verified_bots.name`
  * `verified_bots.bot_type`

Examples:

  * `score < 0.5`
  * `user_ip_address == "123.45.67.89"`
  * `user_agent.contains("Chrome")`
  * `score < 0.5 && user_ip_address == "123.45.67.89"`



`string condition = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The condition.  
  
### getConditionBytes()
    
    
    public abstract ByteString getConditionBytes()

Optional. A CEL condition that must be met for this rule to apply. If unspecified, the rule applies unconditionally. The following fields can be referenced in the condition:

  * `score`
  * `user_ip_address`
  * `user_asn`
  * `user_agent`
  * `verified_bots.name`
  * `verified_bots.bot_type`

Examples:

  * `score < 0.5`
  * `user_ip_address == "123.45.67.89"`
  * `user_agent.contains("Chrome")`
  * `score < 0.5 && user_ip_address == "123.45.67.89"`



`string condition = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for condition.  
  
### getNoChallenge()
    
    
    public abstract ChallengeRule.NoChallengeOutcome getNoChallenge()

Do not present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.NoChallengeOutcome no_challenge = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ChallengeRule.NoChallengeOutcome](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRule.NoChallengeOutcome)` | The noChallenge.  
  
### getNoChallengeOrBuilder()
    
    
    public abstract ChallengeRule.NoChallengeOutcomeOrBuilder getNoChallengeOrBuilder()

Do not present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.NoChallengeOutcome no_challenge = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ChallengeRule.NoChallengeOutcomeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRule.NoChallengeOutcomeOrBuilder)` |   
  
### getOutcomeCase()
    
    
    public abstract ChallengeRule.OutcomeCase getOutcomeCase()

**Returns**  
---  
**Type** | **Description**  
`[ChallengeRule.OutcomeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ChallengeRule.OutcomeCase)` |   
  
### hasChallenge()
    
    
    public abstract boolean hasChallenge()

Present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.ChallengeOutcome challenge = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the challenge field is set.  
  
### hasNoChallenge()
    
    
    public abstract boolean hasNoChallenge()

Do not present a challenge to the user.

`.google.cloud.recaptchaenterprise.v1.ChallengeRule.NoChallengeOutcome no_challenge = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the noChallenge field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
