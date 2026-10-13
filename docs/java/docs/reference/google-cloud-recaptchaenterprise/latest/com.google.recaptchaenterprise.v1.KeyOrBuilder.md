---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyOrBuilder
title: Interface KeyOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:33.585412+00:00
---

# Interface KeyOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface KeyOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface KeyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. See [Creating and managing labels](https://cloud.google.com/recaptcha/docs/labels).

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAndroidSettings()
    
    
    public abstract AndroidKeySettings getAndroidSettings()

Settings for keys that can be used by Android apps.

`.google.cloud.recaptchaenterprise.v1.AndroidKeySettings android_settings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AndroidKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AndroidKeySettings)` | The androidSettings.  
  
### getAndroidSettingsOrBuilder()
    
    
    public abstract AndroidKeySettingsOrBuilder getAndroidSettingsOrBuilder()

Settings for keys that can be used by Android apps.

`.google.cloud.recaptchaenterprise.v1.AndroidKeySettings android_settings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AndroidKeySettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AndroidKeySettingsOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp corresponding to the creation of this key.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp corresponding to the creation of this key.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Human-readable display name of this key. Modifiable by user.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Human-readable display name of this key. Modifiable by user.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getExpressSettings()
    
    
    public abstract ExpressKeySettings getExpressSettings()

Settings for keys that can be used by reCAPTCHA Express.

`.google.cloud.recaptchaenterprise.v1.ExpressKeySettings express_settings = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ExpressKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ExpressKeySettings)` | The expressSettings.  
  
### getExpressSettingsOrBuilder()
    
    
    public abstract ExpressKeySettingsOrBuilder getExpressSettingsOrBuilder()

Settings for keys that can be used by reCAPTCHA Express.

`.google.cloud.recaptchaenterprise.v1.ExpressKeySettings express_settings = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ExpressKeySettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ExpressKeySettingsOrBuilder)` |   
  
### getIosSettings()
    
    
    public abstract IOSKeySettings getIosSettings()

Settings for keys that can be used by iOS apps.

`.google.cloud.recaptchaenterprise.v1.IOSKeySettings ios_settings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[IOSKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.IOSKeySettings)` | The iosSettings.  
  
### getIosSettingsOrBuilder()
    
    
    public abstract IOSKeySettingsOrBuilder getIosSettingsOrBuilder()

Settings for keys that can be used by iOS apps.

`.google.cloud.recaptchaenterprise.v1.IOSKeySettings ios_settings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[IOSKeySettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.IOSKeySettingsOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyOrBuilder#com_google_recaptchaenterprise_v1_KeyOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. See [Creating and managing labels](https://cloud.google.com/recaptcha/docs/labels).

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. See [Creating and managing labels](https://cloud.google.com/recaptcha/docs/labels).

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. See [Creating and managing labels](https://cloud.google.com/recaptcha/docs/labels).

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. See [Creating and managing labels](https://cloud.google.com/recaptcha/docs/labels).

`map<string, string> labels = 6 [(.google.api.field_behavior) = OPTIONAL];`

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

Identifier. The resource name for the Key in the format `projects/{project}/keys/{key}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name for the Key in the format `projects/{project}/keys/{key}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPlatformSettingsCase()
    
    
    public abstract Key.PlatformSettingsCase getPlatformSettingsCase()

**Returns**  
---  
**Type** | **Description**  
`[Key.PlatformSettingsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.PlatformSettingsCase)` |   
  
### getTestingOptions()
    
    
    public abstract TestingOptions getTestingOptions()

Optional. Options for user acceptance testing.

` .google.cloud.recaptchaenterprise.v1.TestingOptions testing_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TestingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TestingOptions)` | The testingOptions.  
  
### getTestingOptionsOrBuilder()
    
    
    public abstract TestingOptionsOrBuilder getTestingOptionsOrBuilder()

Optional. Options for user acceptance testing.

` .google.cloud.recaptchaenterprise.v1.TestingOptions testing_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TestingOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TestingOptionsOrBuilder)` |   
  
### getUniversalSettings()
    
    
    public abstract UniversalKeySettings getUniversalSettings()

Settings for keys that are configured through their Policy.

`.google.cloud.recaptchaenterprise.v1.UniversalKeySettings universal_settings = 13;`

**Returns**  
---  
**Type** | **Description**  
`[UniversalKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UniversalKeySettings)` | The universalSettings.  
  
### getUniversalSettingsOrBuilder()
    
    
    public abstract UniversalKeySettingsOrBuilder getUniversalSettingsOrBuilder()

Settings for keys that are configured through their Policy.

`.google.cloud.recaptchaenterprise.v1.UniversalKeySettings universal_settings = 13;`

**Returns**  
---  
**Type** | **Description**  
`[UniversalKeySettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UniversalKeySettingsOrBuilder)` |   
  
### getWafSettings()
    
    
    public abstract WafSettings getWafSettings()

Optional. Settings for Web Application Firewall (WAF).

` .google.cloud.recaptchaenterprise.v1.WafSettings waf_settings = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WafSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WafSettings)` | The wafSettings.  
  
### getWafSettingsOrBuilder()
    
    
    public abstract WafSettingsOrBuilder getWafSettingsOrBuilder()

Optional. Settings for Web Application Firewall (WAF).

` .google.cloud.recaptchaenterprise.v1.WafSettings waf_settings = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WafSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WafSettingsOrBuilder)` |   
  
### getWebSettings()
    
    
    public abstract WebKeySettings getWebSettings()

Settings for keys that can be used by websites.

`.google.cloud.recaptchaenterprise.v1.WebKeySettings web_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings)` | The webSettings.  
  
### getWebSettingsOrBuilder()
    
    
    public abstract WebKeySettingsOrBuilder getWebSettingsOrBuilder()

Settings for keys that can be used by websites.

`.google.cloud.recaptchaenterprise.v1.WebKeySettings web_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[WebKeySettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettingsOrBuilder)` |   
  
### hasAndroidSettings()
    
    
    public abstract boolean hasAndroidSettings()

Settings for keys that can be used by Android apps.

`.google.cloud.recaptchaenterprise.v1.AndroidKeySettings android_settings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the androidSettings field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp corresponding to the creation of this key.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasExpressSettings()
    
    
    public abstract boolean hasExpressSettings()

Settings for keys that can be used by reCAPTCHA Express.

`.google.cloud.recaptchaenterprise.v1.ExpressKeySettings express_settings = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expressSettings field is set.  
  
### hasIosSettings()
    
    
    public abstract boolean hasIosSettings()

Settings for keys that can be used by iOS apps.

`.google.cloud.recaptchaenterprise.v1.IOSKeySettings ios_settings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iosSettings field is set.  
  
### hasTestingOptions()
    
    
    public abstract boolean hasTestingOptions()

Optional. Options for user acceptance testing.

` .google.cloud.recaptchaenterprise.v1.TestingOptions testing_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the testingOptions field is set.  
  
### hasUniversalSettings()
    
    
    public abstract boolean hasUniversalSettings()

Settings for keys that are configured through their Policy.

`.google.cloud.recaptchaenterprise.v1.UniversalKeySettings universal_settings = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the universalSettings field is set.  
  
### hasWafSettings()
    
    
    public abstract boolean hasWafSettings()

Optional. Settings for Web Application Firewall (WAF).

` .google.cloud.recaptchaenterprise.v1.WafSettings waf_settings = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the wafSettings field is set.  
  
### hasWebSettings()
    
    
    public abstract boolean hasWebSettings()

Settings for keys that can be used by websites.

`.google.cloud.recaptchaenterprise.v1.WebKeySettings web_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the webSettings field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
