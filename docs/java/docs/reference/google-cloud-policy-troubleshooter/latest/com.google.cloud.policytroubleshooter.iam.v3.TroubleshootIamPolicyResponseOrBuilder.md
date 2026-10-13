---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponseOrBuilder
title: Interface TroubleshootIamPolicyResponseOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:33.180961+00:00
---

# Interface TroubleshootIamPolicyResponseOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TroubleshootIamPolicyResponseOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6  1.1.0  1.0.4  0.4.4 
    
    
    public interface TroubleshootIamPolicyResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessTuple()
    
    
    public abstract AccessTuple getAccessTuple()

The access tuple from the request, including any provided context used to evaluate the condition.

`.google.cloud.policytroubleshooter.iam.v3.AccessTuple access_tuple = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AccessTuple](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AccessTuple)` | The accessTuple.  
  
### getAccessTupleOrBuilder()
    
    
    public abstract AccessTupleOrBuilder getAccessTupleOrBuilder()

The access tuple from the request, including any provided context used to evaluate the condition.

`.google.cloud.policytroubleshooter.iam.v3.AccessTuple access_tuple = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AccessTupleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AccessTupleOrBuilder)` |   
  
### getAllowPolicyExplanation()
    
    
    public abstract AllowPolicyExplanation getAllowPolicyExplanation()

An explanation of how the applicable IAM allow policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanation allow_policy_explanation = 3; `

**Returns**  
---  
**Type** | **Description**  
`[AllowPolicyExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanation)` | The allowPolicyExplanation.  
  
### getAllowPolicyExplanationOrBuilder()
    
    
    public abstract AllowPolicyExplanationOrBuilder getAllowPolicyExplanationOrBuilder()

An explanation of how the applicable IAM allow policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanation allow_policy_explanation = 3; `

**Returns**  
---  
**Type** | **Description**  
`[AllowPolicyExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanationOrBuilder)` |   
  
### getDenyPolicyExplanation()
    
    
    public abstract DenyPolicyExplanation getDenyPolicyExplanation()

An explanation of how the applicable IAM deny policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanation deny_policy_explanation = 4; `

**Returns**  
---  
**Type** | **Description**  
`[DenyPolicyExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanation)` | The denyPolicyExplanation.  
  
### getDenyPolicyExplanationOrBuilder()
    
    
    public abstract DenyPolicyExplanationOrBuilder getDenyPolicyExplanationOrBuilder()

An explanation of how the applicable IAM deny policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanation deny_policy_explanation = 4; `

**Returns**  
---  
**Type** | **Description**  
`[DenyPolicyExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanationOrBuilder)` |   
  
### getOverallAccessState()
    
    
    public abstract TroubleshootIamPolicyResponse.OverallAccessState getOverallAccessState()

Indicates whether the principal has the specified permission for the specified resource, based on evaluating all types of the applicable IAM policies.

` .google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse.OverallAccessState overall_access_state = 1; `

**Returns**  
---  
**Type** | **Description**  
`[TroubleshootIamPolicyResponse.OverallAccessState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse.OverallAccessState)` | The overallAccessState.  
  
### getOverallAccessStateValue()
    
    
    public abstract int getOverallAccessStateValue()

Indicates whether the principal has the specified permission for the specified resource, based on evaluating all types of the applicable IAM policies.

` .google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse.OverallAccessState overall_access_state = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for overallAccessState.  
  
### hasAccessTuple()
    
    
    public abstract boolean hasAccessTuple()

The access tuple from the request, including any provided context used to evaluate the condition.

`.google.cloud.policytroubleshooter.iam.v3.AccessTuple access_tuple = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessTuple field is set.  
  
### hasAllowPolicyExplanation()
    
    
    public abstract boolean hasAllowPolicyExplanation()

An explanation of how the applicable IAM allow policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanation allow_policy_explanation = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowPolicyExplanation field is set.  
  
### hasDenyPolicyExplanation()
    
    
    public abstract boolean hasDenyPolicyExplanation()

An explanation of how the applicable IAM deny policies affect the final access state.

` .google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanation deny_policy_explanation = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the denyPolicyExplanation field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
