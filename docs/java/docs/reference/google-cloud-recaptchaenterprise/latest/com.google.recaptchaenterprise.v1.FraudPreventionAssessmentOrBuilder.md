---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessmentOrBuilder
title: Interface FraudPreventionAssessmentOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:13.742738+00:00
---

# Interface FraudPreventionAssessmentOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FraudPreventionAssessmentOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface FraudPreventionAssessmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBehavioralTrustVerdict()
    
    
    public abstract FraudPreventionAssessment.BehavioralTrustVerdict getBehavioralTrustVerdict()

Output only. Assessment of this transaction for behavioral trust.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.BehavioralTrustVerdict behavioral_trust_verdict = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.BehavioralTrustVerdict](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.BehavioralTrustVerdict)` | The behavioralTrustVerdict.  
  
### getBehavioralTrustVerdictOrBuilder()
    
    
    public abstract FraudPreventionAssessment.BehavioralTrustVerdictOrBuilder getBehavioralTrustVerdictOrBuilder()

Output only. Assessment of this transaction for behavioral trust.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.BehavioralTrustVerdict behavioral_trust_verdict = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.BehavioralTrustVerdictOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.BehavioralTrustVerdictOrBuilder)` |   
  
### getCardTestingVerdict()
    
    
    public abstract FraudPreventionAssessment.CardTestingVerdict getCardTestingVerdict()

Output only. Assessment of this transaction for risk of being part of a card testing attack.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.CardTestingVerdict card_testing_verdict = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.CardTestingVerdict](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.CardTestingVerdict)` | The cardTestingVerdict.  
  
### getCardTestingVerdictOrBuilder()
    
    
    public abstract FraudPreventionAssessment.CardTestingVerdictOrBuilder getCardTestingVerdictOrBuilder()

Output only. Assessment of this transaction for risk of being part of a card testing attack.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.CardTestingVerdict card_testing_verdict = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.CardTestingVerdictOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.CardTestingVerdictOrBuilder)` |   
  
### getRiskReasons(int index)
    
    
    public abstract FraudPreventionAssessment.RiskReason getRiskReasons(int index)

Output only. Reasons why the transaction is probably fraudulent and received a high transaction risk score.

` repeated .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason risk_reasons = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.RiskReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason)` |   
  
### getRiskReasonsCount()
    
    
    public abstract int getRiskReasonsCount()

Output only. Reasons why the transaction is probably fraudulent and received a high transaction risk score.

` repeated .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason risk_reasons = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRiskReasonsList()
    
    
    public abstract List<FraudPreventionAssessment.RiskReason> getRiskReasonsList()

Output only. Reasons why the transaction is probably fraudulent and received a high transaction risk score.

` repeated .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason risk_reasons = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RiskReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason)>` |   
  
### getRiskReasonsOrBuilder(int index)
    
    
    public abstract FraudPreventionAssessment.RiskReasonOrBuilder getRiskReasonsOrBuilder(int index)

Output only. Reasons why the transaction is probably fraudulent and received a high transaction risk score.

` repeated .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason risk_reasons = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.RiskReasonOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReasonOrBuilder)` |   
  
### getRiskReasonsOrBuilderList()
    
    
    public abstract List<? extends FraudPreventionAssessment.RiskReasonOrBuilder> getRiskReasonsOrBuilderList()

Output only. Reasons why the transaction is probably fraudulent and received a high transaction risk score.

` repeated .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason risk_reasons = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReasonOrBuilder>` |   
  
### getStolenInstrumentVerdict()
    
    
    public abstract FraudPreventionAssessment.StolenInstrumentVerdict getStolenInstrumentVerdict()

Output only. Assessment of this transaction for risk of a stolen instrument.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.StolenInstrumentVerdict stolen_instrument_verdict = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.StolenInstrumentVerdict](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.StolenInstrumentVerdict)` | The stolenInstrumentVerdict.  
  
### getStolenInstrumentVerdictOrBuilder()
    
    
    public abstract FraudPreventionAssessment.StolenInstrumentVerdictOrBuilder getStolenInstrumentVerdictOrBuilder()

Output only. Assessment of this transaction for risk of a stolen instrument.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.StolenInstrumentVerdict stolen_instrument_verdict = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment.StolenInstrumentVerdictOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment.StolenInstrumentVerdictOrBuilder)` |   
  
### getTransactionRisk()
    
    
    public abstract float getTransactionRisk()

Output only. Probability of this transaction being fraudulent. Summarizes the combined risk of attack vectors below. Values are from 0.0 (lowest) to 1.0 (highest).

`float transaction_risk = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The transactionRisk.  
  
### hasBehavioralTrustVerdict()
    
    
    public abstract boolean hasBehavioralTrustVerdict()

Output only. Assessment of this transaction for behavioral trust.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.BehavioralTrustVerdict behavioral_trust_verdict = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the behavioralTrustVerdict field is set.  
  
### hasCardTestingVerdict()
    
    
    public abstract boolean hasCardTestingVerdict()

Output only. Assessment of this transaction for risk of being part of a card testing attack.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.CardTestingVerdict card_testing_verdict = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cardTestingVerdict field is set.  
  
### hasStolenInstrumentVerdict()
    
    
    public abstract boolean hasStolenInstrumentVerdict()

Output only. Assessment of this transaction for risk of a stolen instrument.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.StolenInstrumentVerdict stolen_instrument_verdict = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stolenInstrumentVerdict field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
