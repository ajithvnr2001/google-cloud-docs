---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PasswordValidationPolicyOrBuilder
title: Interface PasswordValidationPolicyOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:24.339362+00:00
---

# Interface PasswordValidationPolicyOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PasswordValidationPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PasswordValidationPolicyOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface PasswordValidationPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComplexity()
    
    
    public abstract PasswordValidationPolicy.Complexity getComplexity()

The complexity of the password.

`.google.cloud.sql.v1.PasswordValidationPolicy.Complexity complexity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PasswordValidationPolicy.Complexity](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PasswordValidationPolicy.Complexity)` | The complexity.  
  
### getComplexityValue()
    
    
    public abstract int getComplexityValue()

The complexity of the password.

`.google.cloud.sql.v1.PasswordValidationPolicy.Complexity complexity = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for complexity.  
  
### getDisallowCompromisedCredentials() (deprecated)
    
    
    public abstract BoolValue getDisallowCompromisedCredentials()

**Deprecated.** _google.cloud.sql.v1.PasswordValidationPolicy.disallow_compromised_credentials is deprecated. See google/cloud/sql/v1/cloud_sql_resources.proto;l=1569_

This field is deprecated and will be removed in a future version of the API.

`.google.protobuf.BoolValue disallow_compromised_credentials = 7 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The disallowCompromisedCredentials.  
  
### getDisallowCompromisedCredentialsOrBuilder() (deprecated)
    
    
    public abstract BoolValueOrBuilder getDisallowCompromisedCredentialsOrBuilder()

This field is deprecated and will be removed in a future version of the API.

`.google.protobuf.BoolValue disallow_compromised_credentials = 7 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getDisallowUsernameSubstring()
    
    
    public abstract BoolValue getDisallowUsernameSubstring()

Disallow username as a part of the password.

`.google.protobuf.BoolValue disallow_username_substring = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The disallowUsernameSubstring.  
  
### getDisallowUsernameSubstringOrBuilder()
    
    
    public abstract BoolValueOrBuilder getDisallowUsernameSubstringOrBuilder()

Disallow username as a part of the password.

`.google.protobuf.BoolValue disallow_username_substring = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getEnablePasswordPolicy()
    
    
    public abstract BoolValue getEnablePasswordPolicy()

Whether to enable the password policy or not. When enabled, passwords must meet complexity requirements. Keep this policy enabled to help prevent unauthorized access. Disabling this policy allows weak passwords.

`.google.protobuf.BoolValue enable_password_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The enablePasswordPolicy.  
  
### getEnablePasswordPolicyOrBuilder()
    
    
    public abstract BoolValueOrBuilder getEnablePasswordPolicyOrBuilder()

Whether to enable the password policy or not. When enabled, passwords must meet complexity requirements. Keep this policy enabled to help prevent unauthorized access. Disabling this policy allows weak passwords.

`.google.protobuf.BoolValue enable_password_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getMinLength()
    
    
    public abstract Int32Value getMinLength()

Minimum number of characters allowed.

`.google.protobuf.Int32Value min_length = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32Value.html)` | The minLength.  
  
### getMinLengthOrBuilder()
    
    
    public abstract Int32ValueOrBuilder getMinLengthOrBuilder()

Minimum number of characters allowed.

`.google.protobuf.Int32Value min_length = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Int32ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32ValueOrBuilder.html)` |   
  
### getPasswordChangeInterval()
    
    
    public abstract Duration getPasswordChangeInterval()

Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL.

`.google.protobuf.Duration password_change_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The passwordChangeInterval.  
  
### getPasswordChangeIntervalOrBuilder()
    
    
    public abstract DurationOrBuilder getPasswordChangeIntervalOrBuilder()

Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL.

`.google.protobuf.Duration password_change_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getReuseInterval()
    
    
    public abstract Int32Value getReuseInterval()

Number of previous passwords that cannot be reused.

`.google.protobuf.Int32Value reuse_interval = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32Value.html)` | The reuseInterval.  
  
### getReuseIntervalOrBuilder()
    
    
    public abstract Int32ValueOrBuilder getReuseIntervalOrBuilder()

Number of previous passwords that cannot be reused.

`.google.protobuf.Int32Value reuse_interval = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Int32ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32ValueOrBuilder.html)` |   
  
### hasDisallowCompromisedCredentials() (deprecated)
    
    
    public abstract boolean hasDisallowCompromisedCredentials()

**Deprecated.** _google.cloud.sql.v1.PasswordValidationPolicy.disallow_compromised_credentials is deprecated. See google/cloud/sql/v1/cloud_sql_resources.proto;l=1569_

This field is deprecated and will be removed in a future version of the API.

`.google.protobuf.BoolValue disallow_compromised_credentials = 7 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disallowCompromisedCredentials field is set.  
  
### hasDisallowUsernameSubstring()
    
    
    public abstract boolean hasDisallowUsernameSubstring()

Disallow username as a part of the password.

`.google.protobuf.BoolValue disallow_username_substring = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disallowUsernameSubstring field is set.  
  
### hasEnablePasswordPolicy()
    
    
    public abstract boolean hasEnablePasswordPolicy()

Whether to enable the password policy or not. When enabled, passwords must meet complexity requirements. Keep this policy enabled to help prevent unauthorized access. Disabling this policy allows weak passwords.

`.google.protobuf.BoolValue enable_password_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enablePasswordPolicy field is set.  
  
### hasMinLength()
    
    
    public abstract boolean hasMinLength()

Minimum number of characters allowed.

`.google.protobuf.Int32Value min_length = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minLength field is set.  
  
### hasPasswordChangeInterval()
    
    
    public abstract boolean hasPasswordChangeInterval()

Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL.

`.google.protobuf.Duration password_change_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the passwordChangeInterval field is set.  
  
### hasReuseInterval()
    
    
    public abstract boolean hasReuseInterval()

Number of previous passwords that cannot be reused.

`.google.protobuf.Int32Value reuse_interval = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reuseInterval field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
