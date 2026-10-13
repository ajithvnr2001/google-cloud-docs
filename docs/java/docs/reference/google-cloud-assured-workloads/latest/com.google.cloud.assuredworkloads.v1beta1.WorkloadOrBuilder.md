---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.WorkloadOrBuilder
title: Interface WorkloadOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:48.422643+00:00
---

# Interface WorkloadOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.WorkloadOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WorkloadOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 
    
    
    public interface WorkloadOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels applied to the workload.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBillingAccount()
    
    
    public abstract String getBillingAccount()

Output only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.

`string billing_account = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The billingAccount.  
  
### getBillingAccountBytes()
    
    
    public abstract ByteString getBillingAccountBytes()

Output only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.

`string billing_account = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for billingAccount.  
  
### getCjisSettings() (deprecated)
    
    
    public abstract Workload.CJISSettings getCjisSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.cjis_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=475_

Input only. Immutable. Settings specific to resources needed for CJIS.

` .google.cloud.assuredworkloads.v1beta1.Workload.CJISSettings cjis_settings = 8 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.CJISSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.CJISSettings)` | The cjisSettings.  
  
### getCjisSettingsOrBuilder() (deprecated)
    
    
    public abstract Workload.CJISSettingsOrBuilder getCjisSettingsOrBuilder()

Input only. Immutable. Settings specific to resources needed for CJIS.

` .google.cloud.assuredworkloads.v1beta1.Workload.CJISSettings cjis_settings = 8 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.CJISSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.CJISSettingsOrBuilder)` |   
  
### getComplianceRegime()
    
    
    public abstract Workload.ComplianceRegime getComplianceRegime()

Required. Immutable. Compliance Regime associated with this workload.

` .google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime compliance_regime = 4 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.ComplianceRegime](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime)` | The complianceRegime.  
  
### getComplianceRegimeSettingsCase()
    
    
    public abstract Workload.ComplianceRegimeSettingsCase getComplianceRegimeSettingsCase()

**Returns**  
---  
**Type** | **Description**  
`[Workload.ComplianceRegimeSettingsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegimeSettingsCase)` |   
  
### getComplianceRegimeValue()
    
    
    public abstract int getComplianceRegimeValue()

Required. Immutable. Compliance Regime associated with this workload.

` .google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime compliance_regime = 4 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for complianceRegime.  
  
### getCompliantButDisallowedServices(int index)
    
    
    public abstract String getCompliantButDisallowedServices(int index)

Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment."

` repeated string compliant_but_disallowed_services = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The compliantButDisallowedServices at the given index.  
  
### getCompliantButDisallowedServicesBytes(int index)
    
    
    public abstract ByteString getCompliantButDisallowedServicesBytes(int index)

Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment."

` repeated string compliant_but_disallowed_services = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the compliantButDisallowedServices at the given index.  
  
### getCompliantButDisallowedServicesCount()
    
    
    public abstract int getCompliantButDisallowedServicesCount()

Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment."

` repeated string compliant_but_disallowed_services = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of compliantButDisallowedServices.  
  
### getCompliantButDisallowedServicesList()
    
    
    public abstract List<String> getCompliantButDisallowedServicesList()

Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment."

` repeated string compliant_but_disallowed_services = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the compliantButDisallowedServices.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Immutable. The Workload creation timestamp.

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Immutable. The Workload creation timestamp.

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces.

Example: My Workload

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces.

Example: My Workload

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnableSovereignControls()
    
    
    public abstract boolean getEnableSovereignControls()

Optional. Indicates the sovereignty status of the given workload. Currently meant to be used by Europe/Canada customers.

`bool enable_sovereign_controls = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableSovereignControls.  
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getFedrampHighSettings() (deprecated)
    
    
    public abstract Workload.FedrampHighSettings getFedrampHighSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.fedramp_high_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=482_

Input only. Immutable. Settings specific to resources needed for FedRAMP High.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampHighSettings fedramp_high_settings = 11 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.FedrampHighSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.FedrampHighSettings)` | The fedrampHighSettings.  
  
### getFedrampHighSettingsOrBuilder() (deprecated)
    
    
    public abstract Workload.FedrampHighSettingsOrBuilder getFedrampHighSettingsOrBuilder()

Input only. Immutable. Settings specific to resources needed for FedRAMP High.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampHighSettings fedramp_high_settings = 11 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.FedrampHighSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.FedrampHighSettingsOrBuilder)` |   
  
### getFedrampModerateSettings() (deprecated)
    
    
    public abstract Workload.FedrampModerateSettings getFedrampModerateSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.fedramp_moderate_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=489_

Input only. Immutable. Settings specific to resources needed for FedRAMP Moderate.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampModerateSettings fedramp_moderate_settings = 12 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.FedrampModerateSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.FedrampModerateSettings)` | The fedrampModerateSettings.  
  
### getFedrampModerateSettingsOrBuilder() (deprecated)
    
    
    public abstract Workload.FedrampModerateSettingsOrBuilder getFedrampModerateSettingsOrBuilder()

Input only. Immutable. Settings specific to resources needed for FedRAMP Moderate.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampModerateSettings fedramp_moderate_settings = 12 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.FedrampModerateSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.FedrampModerateSettingsOrBuilder)` |   
  
### getIl4Settings() (deprecated)
    
    
    public abstract Workload.IL4Settings getIl4Settings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.il4_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=468_

Input only. Immutable. Settings specific to resources needed for IL4.

` .google.cloud.assuredworkloads.v1beta1.Workload.IL4Settings il4_settings = 7 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.IL4Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.IL4Settings)` | The il4Settings.  
  
### getIl4SettingsOrBuilder() (deprecated)
    
    
    public abstract Workload.IL4SettingsOrBuilder getIl4SettingsOrBuilder()

Input only. Immutable. Settings specific to resources needed for IL4.

` .google.cloud.assuredworkloads.v1beta1.Workload.IL4Settings il4_settings = 7 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.IL4SettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.IL4SettingsOrBuilder)` |   
  
### getKajEnrollmentState()
    
    
    public abstract Workload.KajEnrollmentState getKajEnrollmentState()

Output only. Represents the KAJ enrollment state of the given workload.

` .google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState kaj_enrollment_state = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.KajEnrollmentState](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState)` | The kajEnrollmentState.  
  
### getKajEnrollmentStateValue()
    
    
    public abstract int getKajEnrollmentStateValue()

Output only. Represents the KAJ enrollment state of the given workload.

` .google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState kaj_enrollment_state = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for kajEnrollmentState.  
  
### getKmsSettings() (deprecated)
    
    
    public abstract Workload.KMSSettings getKmsSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.kms_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=516_

Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS CMEK key is provisioned. This field is deprecated as of Feb 28, 2022. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.

` .google.cloud.assuredworkloads.v1beta1.Workload.KMSSettings kms_settings = 14 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.KMSSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.KMSSettings)` | The kmsSettings.  
  
### getKmsSettingsOrBuilder() (deprecated)
    
    
    public abstract Workload.KMSSettingsOrBuilder getKmsSettingsOrBuilder()

Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS CMEK key is provisioned. This field is deprecated as of Feb 28, 2022. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.

` .google.cloud.assuredworkloads.v1beta1.Workload.KMSSettings kms_settings = 14 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.KMSSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.KMSSettingsOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.WorkloadOrBuilder#com_google_cloud_assuredworkloads_v1beta1_WorkloadOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels applied to the workload.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels applied to the workload.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels applied to the workload.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Labels applied to the workload.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload}

Read-only.

`string name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload}

Read-only.

`string name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProvisionedResourcesParent()
    
    
    public abstract String getProvisionedResourcesParent()

Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/{folder_id}

`string provisioned_resources_parent = 13 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The provisionedResourcesParent.  
  
### getProvisionedResourcesParentBytes()
    
    
    public abstract ByteString getProvisionedResourcesParentBytes()

Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/{folder_id}

`string provisioned_resources_parent = 13 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for provisionedResourcesParent.  
  
### getResourceSettings(int index)
    
    
    public abstract Workload.ResourceSettings getResourceSettings(int index)

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings resource_settings = 15 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload.ResourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings)` |   
  
### getResourceSettingsCount()
    
    
    public abstract int getResourceSettingsCount()

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings resource_settings = 15 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceSettingsList()
    
    
    public abstract List<Workload.ResourceSettings> getResourceSettingsList()

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings resource_settings = 15 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings)>` |   
  
### getResourceSettingsOrBuilder(int index)
    
    
    public abstract Workload.ResourceSettingsOrBuilder getResourceSettingsOrBuilder(int index)

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings resource_settings = 15 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload.ResourceSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettingsOrBuilder)` |   
  
### getResourceSettingsOrBuilderList()
    
    
    public abstract List<? extends Workload.ResourceSettingsOrBuilder> getResourceSettingsOrBuilderList()

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettings resource_settings = 15 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceSettingsOrBuilder>` |   
  
### getResources(int index)
    
    
    public abstract Workload.ResourceInfo getResources(int index)

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo resources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload.ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo)` |   
  
### getResourcesCount()
    
    
    public abstract int getResourcesCount()

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo resources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourcesList()
    
    
    public abstract List<Workload.ResourceInfo> getResourcesList()

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo resources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo)>` |   
  
### getResourcesOrBuilder(int index)
    
    
    public abstract Workload.ResourceInfoOrBuilder getResourcesOrBuilder(int index)

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo resources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload.ResourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfoOrBuilder)` |   
  
### getResourcesOrBuilderList()
    
    
    public abstract List<? extends Workload.ResourceInfoOrBuilder> getResourcesOrBuilderList()

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

` repeated .google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfo resources = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.assuredworkloads.v1beta1.Workload.ResourceInfoOrBuilder>` |   
  
### getSaaEnrollmentResponse()
    
    
    public abstract Workload.SaaEnrollmentResponse getSaaEnrollmentResponse()

Output only. Represents the SAA enrollment response of the given workload. SAA enrollment response is queried during GetWorkload call. In failure cases, user friendly error message is shown in SAA details page.

` .google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponse saa_enrollment_response = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.SaaEnrollmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponse)` | The saaEnrollmentResponse.  
  
### getSaaEnrollmentResponseOrBuilder()
    
    
    public abstract Workload.SaaEnrollmentResponseOrBuilder getSaaEnrollmentResponseOrBuilder()

Output only. Represents the SAA enrollment response of the given workload. SAA enrollment response is queried during GetWorkload call. In failure cases, user friendly error message is shown in SAA details page.

` .google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponse saa_enrollment_response = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Workload.SaaEnrollmentResponseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponseOrBuilder)` |   
  
### hasCjisSettings() (deprecated)
    
    
    public abstract boolean hasCjisSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.cjis_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=475_

Input only. Immutable. Settings specific to resources needed for CJIS.

` .google.cloud.assuredworkloads.v1beta1.Workload.CJISSettings cjis_settings = 8 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cjisSettings field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Immutable. The Workload creation timestamp.

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasFedrampHighSettings() (deprecated)
    
    
    public abstract boolean hasFedrampHighSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.fedramp_high_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=482_

Input only. Immutable. Settings specific to resources needed for FedRAMP High.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampHighSettings fedramp_high_settings = 11 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fedrampHighSettings field is set.  
  
### hasFedrampModerateSettings() (deprecated)
    
    
    public abstract boolean hasFedrampModerateSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.fedramp_moderate_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=489_

Input only. Immutable. Settings specific to resources needed for FedRAMP Moderate.

` .google.cloud.assuredworkloads.v1beta1.Workload.FedrampModerateSettings fedramp_moderate_settings = 12 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fedrampModerateSettings field is set.  
  
### hasIl4Settings() (deprecated)
    
    
    public abstract boolean hasIl4Settings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.il4_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=468_

Input only. Immutable. Settings specific to resources needed for IL4.

` .google.cloud.assuredworkloads.v1beta1.Workload.IL4Settings il4_settings = 7 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the il4Settings field is set.  
  
### hasKmsSettings() (deprecated)
    
    
    public abstract boolean hasKmsSettings()

**Deprecated.** _google.cloud.assuredworkloads.v1beta1.Workload.kms_settings is deprecated. See google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto;l=516_

Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS CMEK key is provisioned. This field is deprecated as of Feb 28, 2022. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.

` .google.cloud.assuredworkloads.v1beta1.Workload.KMSSettings kms_settings = 14 [deprecated = true, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kmsSettings field is set.  
  
### hasSaaEnrollmentResponse()
    
    
    public abstract boolean hasSaaEnrollmentResponse()

Output only. Represents the SAA enrollment response of the given workload. SAA enrollment response is queried during GetWorkload call. In failure cases, user friendly error message is shown in SAA details page.

` .google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponse saa_enrollment_response = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the saaEnrollmentResponse field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
