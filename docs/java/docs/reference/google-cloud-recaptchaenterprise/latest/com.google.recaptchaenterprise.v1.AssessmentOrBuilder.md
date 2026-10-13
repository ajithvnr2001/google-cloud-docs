---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentOrBuilder
title: Interface AssessmentOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:34.938407+00:00
---

# Interface AssessmentOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AssessmentOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface AssessmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccountDefenderAssessment()
    
    
    public abstract AccountDefenderAssessment getAccountDefenderAssessment()

Output only. Assessment returned by Account defense when an account identifier is provided.

` .google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment account_defender_assessment = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AccountDefenderAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountDefenderAssessment)` | The accountDefenderAssessment.  
  
### getAccountDefenderAssessmentOrBuilder()
    
    
    public abstract AccountDefenderAssessmentOrBuilder getAccountDefenderAssessmentOrBuilder()

Output only. Assessment returned by Account defense when an account identifier is provided.

` .google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment account_defender_assessment = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AccountDefenderAssessmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountDefenderAssessmentOrBuilder)` |   
  
### getAccountVerification()
    
    
    public abstract AccountVerificationInfo getAccountVerification()

Optional. Account verification information for identity verification. The assessment event must include a token and site key to use this feature.

` .google.cloud.recaptchaenterprise.v1.AccountVerificationInfo account_verification = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AccountVerificationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountVerificationInfo)` | The accountVerification.  
  
### getAccountVerificationOrBuilder()
    
    
    public abstract AccountVerificationInfoOrBuilder getAccountVerificationOrBuilder()

Optional. Account verification information for identity verification. The assessment event must include a token and site key to use this feature.

` .google.cloud.recaptchaenterprise.v1.AccountVerificationInfo account_verification = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AccountVerificationInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountVerificationInfoOrBuilder)` |   
  
### getAssessmentEnvironment()
    
    
    public abstract AssessmentEnvironment getAssessmentEnvironment()

Optional. The environment creating the assessment. This describes your environment (the system invoking CreateAssessment), NOT the environment of your user.

` .google.cloud.recaptchaenterprise.v1.AssessmentEnvironment assessment_environment = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssessmentEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentEnvironment)` | The assessmentEnvironment.  
  
### getAssessmentEnvironmentOrBuilder()
    
    
    public abstract AssessmentEnvironmentOrBuilder getAssessmentEnvironmentOrBuilder()

Optional. The environment creating the assessment. This describes your environment (the system invoking CreateAssessment), NOT the environment of your user.

` .google.cloud.recaptchaenterprise.v1.AssessmentEnvironment assessment_environment = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssessmentEnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentEnvironmentOrBuilder)` |   
  
### getEvent()
    
    
    public abstract Event getEvent()

Optional. The event being assessed.

` .google.cloud.recaptchaenterprise.v1.Event event = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event)` | The event.  
  
### getEventOrBuilder()
    
    
    public abstract EventOrBuilder getEventOrBuilder()

Optional. The event being assessed.

` .google.cloud.recaptchaenterprise.v1.Event event = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EventOrBuilder)` |   
  
### getFirewallPolicyAssessment()
    
    
    public abstract FirewallPolicyAssessment getFirewallPolicyAssessment()

Output only. Assessment returned when firewall policies belonging to the project are evaluated using the field firewall_policy_evaluation.

` .google.cloud.recaptchaenterprise.v1.FirewallPolicyAssessment firewall_policy_assessment = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallPolicyAssessment)` | The firewallPolicyAssessment.  
  
### getFirewallPolicyAssessmentOrBuilder()
    
    
    public abstract FirewallPolicyAssessmentOrBuilder getFirewallPolicyAssessmentOrBuilder()

Output only. Assessment returned when firewall policies belonging to the project are evaluated using the field firewall_policy_evaluation.

` .google.cloud.recaptchaenterprise.v1.FirewallPolicyAssessment firewall_policy_assessment = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssessmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallPolicyAssessmentOrBuilder)` |   
  
### getFraudPreventionAssessment()
    
    
    public abstract FraudPreventionAssessment getFraudPreventionAssessment()

Output only. Assessment returned by Fraud Prevention when TransactionData is provided.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment fraud_prevention_assessment = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessment)` | The fraudPreventionAssessment.  
  
### getFraudPreventionAssessmentOrBuilder()
    
    
    public abstract FraudPreventionAssessmentOrBuilder getFraudPreventionAssessmentOrBuilder()

Output only. Assessment returned by Fraud Prevention when TransactionData is provided.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment fraud_prevention_assessment = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudPreventionAssessmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudPreventionAssessmentOrBuilder)` |   
  
### getFraudSignals()
    
    
    public abstract FraudSignals getFraudSignals()

Output only. Fraud Signals specific to the users involved in a payment transaction.

` .google.cloud.recaptchaenterprise.v1.FraudSignals fraud_signals = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudSignals](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudSignals)` | The fraudSignals.  
  
### getFraudSignalsOrBuilder()
    
    
    public abstract FraudSignalsOrBuilder getFraudSignalsOrBuilder()

Output only. Fraud Signals specific to the users involved in a payment transaction.

` .google.cloud.recaptchaenterprise.v1.FraudSignals fraud_signals = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[FraudSignalsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FraudSignalsOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. Identifier. The resource name for the Assessment in the format `projects/{project}/assessments/{assessment}`.

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Identifier. The resource name for the Assessment in the format `projects/{project}/assessments/{assessment}`.

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPhoneFraudAssessment()
    
    
    public abstract PhoneFraudAssessment getPhoneFraudAssessment()

Output only. Assessment returned when a site key, a token, and a phone number as `user_id` are provided. SMS defense needs to be enabled.

` .google.cloud.recaptchaenterprise.v1.PhoneFraudAssessment phone_fraud_assessment = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PhoneFraudAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PhoneFraudAssessment)` | The phoneFraudAssessment.  
  
### getPhoneFraudAssessmentOrBuilder()
    
    
    public abstract PhoneFraudAssessmentOrBuilder getPhoneFraudAssessmentOrBuilder()

Output only. Assessment returned when a site key, a token, and a phone number as `user_id` are provided. SMS defense needs to be enabled.

` .google.cloud.recaptchaenterprise.v1.PhoneFraudAssessment phone_fraud_assessment = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PhoneFraudAssessmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PhoneFraudAssessmentOrBuilder)` |   
  
### getPolicyEvaluation()
    
    
    public abstract PolicyEvaluation getPolicyEvaluation()

Output only. Provides information about the policy evaluation for this assessment.

` .google.cloud.recaptchaenterprise.v1.PolicyEvaluation policy_evaluation = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PolicyEvaluation)` | The policyEvaluation.  
  
### getPolicyEvaluationOrBuilder()
    
    
    public abstract PolicyEvaluationOrBuilder getPolicyEvaluationOrBuilder()

Output only. Provides information about the policy evaluation for this assessment.

` .google.cloud.recaptchaenterprise.v1.PolicyEvaluation policy_evaluation = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyEvaluationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PolicyEvaluationOrBuilder)` |   
  
### getPrivatePasswordLeakVerification()
    
    
    public abstract PrivatePasswordLeakVerification getPrivatePasswordLeakVerification()

Optional. The private password leak verification field contains the parameters that are used to to check for leaks privately without sharing user credentials.

` .google.cloud.recaptchaenterprise.v1.PrivatePasswordLeakVerification private_password_leak_verification = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification)` | The privatePasswordLeakVerification.  
  
### getPrivatePasswordLeakVerificationOrBuilder()
    
    
    public abstract PrivatePasswordLeakVerificationOrBuilder getPrivatePasswordLeakVerificationOrBuilder()

Optional. The private password leak verification field contains the parameters that are used to to check for leaks privately without sharing user credentials.

` .google.cloud.recaptchaenterprise.v1.PrivatePasswordLeakVerification private_password_leak_verification = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivatePasswordLeakVerificationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerificationOrBuilder)` |   
  
### getRiskAnalysis()
    
    
    public abstract RiskAnalysis getRiskAnalysis()

Output only. The risk analysis result for the event being assessed.

` .google.cloud.recaptchaenterprise.v1.RiskAnalysis risk_analysis = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[RiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis)` | The riskAnalysis.  
  
### getRiskAnalysisOrBuilder()
    
    
    public abstract RiskAnalysisOrBuilder getRiskAnalysisOrBuilder()

Output only. The risk analysis result for the event being assessed.

` .google.cloud.recaptchaenterprise.v1.RiskAnalysis risk_analysis = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[RiskAnalysisOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysisOrBuilder)` |   
  
### getTokenProperties()
    
    
    public abstract TokenProperties getTokenProperties()

Output only. Properties of the provided event token.

` .google.cloud.recaptchaenterprise.v1.TokenProperties token_properties = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties)` | The tokenProperties.  
  
### getTokenPropertiesOrBuilder()
    
    
    public abstract TokenPropertiesOrBuilder getTokenPropertiesOrBuilder()

Output only. Properties of the provided event token.

` .google.cloud.recaptchaenterprise.v1.TokenProperties token_properties = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TokenPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenPropertiesOrBuilder)` |   
  
### hasAccountDefenderAssessment()
    
    
    public abstract boolean hasAccountDefenderAssessment()

Output only. Assessment returned by Account defense when an account identifier is provided.

` .google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment account_defender_assessment = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accountDefenderAssessment field is set.  
  
### hasAccountVerification()
    
    
    public abstract boolean hasAccountVerification()

Optional. Account verification information for identity verification. The assessment event must include a token and site key to use this feature.

` .google.cloud.recaptchaenterprise.v1.AccountVerificationInfo account_verification = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accountVerification field is set.  
  
### hasAssessmentEnvironment()
    
    
    public abstract boolean hasAssessmentEnvironment()

Optional. The environment creating the assessment. This describes your environment (the system invoking CreateAssessment), NOT the environment of your user.

` .google.cloud.recaptchaenterprise.v1.AssessmentEnvironment assessment_environment = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assessmentEnvironment field is set.  
  
### hasEvent()
    
    
    public abstract boolean hasEvent()

Optional. The event being assessed.

` .google.cloud.recaptchaenterprise.v1.Event event = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the event field is set.  
  
### hasFirewallPolicyAssessment()
    
    
    public abstract boolean hasFirewallPolicyAssessment()

Output only. Assessment returned when firewall policies belonging to the project are evaluated using the field firewall_policy_evaluation.

` .google.cloud.recaptchaenterprise.v1.FirewallPolicyAssessment firewall_policy_assessment = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the firewallPolicyAssessment field is set.  
  
### hasFraudPreventionAssessment()
    
    
    public abstract boolean hasFraudPreventionAssessment()

Output only. Assessment returned by Fraud Prevention when TransactionData is provided.

` .google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment fraud_prevention_assessment = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fraudPreventionAssessment field is set.  
  
### hasFraudSignals()
    
    
    public abstract boolean hasFraudSignals()

Output only. Fraud Signals specific to the users involved in a payment transaction.

` .google.cloud.recaptchaenterprise.v1.FraudSignals fraud_signals = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fraudSignals field is set.  
  
### hasPhoneFraudAssessment()
    
    
    public abstract boolean hasPhoneFraudAssessment()

Output only. Assessment returned when a site key, a token, and a phone number as `user_id` are provided. SMS defense needs to be enabled.

` .google.cloud.recaptchaenterprise.v1.PhoneFraudAssessment phone_fraud_assessment = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the phoneFraudAssessment field is set.  
  
### hasPolicyEvaluation()
    
    
    public abstract boolean hasPolicyEvaluation()

Output only. Provides information about the policy evaluation for this assessment.

` .google.cloud.recaptchaenterprise.v1.PolicyEvaluation policy_evaluation = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policyEvaluation field is set.  
  
### hasPrivatePasswordLeakVerification()
    
    
    public abstract boolean hasPrivatePasswordLeakVerification()

Optional. The private password leak verification field contains the parameters that are used to to check for leaks privately without sharing user credentials.

` .google.cloud.recaptchaenterprise.v1.PrivatePasswordLeakVerification private_password_leak_verification = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privatePasswordLeakVerification field is set.  
  
### hasRiskAnalysis()
    
    
    public abstract boolean hasRiskAnalysis()

Output only. The risk analysis result for the event being assessed.

` .google.cloud.recaptchaenterprise.v1.RiskAnalysis risk_analysis = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the riskAnalysis field is set.  
  
### hasTokenProperties()
    
    
    public abstract boolean hasTokenProperties()

Output only. Properties of the provided event token.

` .google.cloud.recaptchaenterprise.v1.TokenProperties token_properties = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokenProperties field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
