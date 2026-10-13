---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SettingsOrBuilder
title: Interface SettingsOrBuilder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:21.488392+00:00
---

# Interface SettingsOrBuilder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SettingsOrBuilder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public interface SettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutoStrideEnabled()
    
    
    public abstract boolean getAutoStrideEnabled()

Optional. True if the user's stride length is determined automatically.

Updates to this field are currently not supported.

`bool auto_stride_enabled = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The autoStrideEnabled.  
  
### getDistanceUnit()
    
    
    public abstract Settings.DistanceUnit getDistanceUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.DistanceUnit distance_unit = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.DistanceUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.DistanceUnit)` | The distanceUnit.  
  
### getDistanceUnitValue()
    
    
    public abstract int getDistanceUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.DistanceUnit distance_unit = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for distanceUnit.  
  
### getFoodLanguageCode()
    
    
    public abstract String getFoodLanguageCode()

Output only. The food language code derived from the user's food database. Possible values: `'en-US'`, `'en-GB'`, `'de-DE'`, `'es-ES'`, `'fr-FR'`, `'zh-CN'`, `'zh-TW'`, `'ja-JP'`, `'en-AU'`, `'en-CA'`, `'it-IT'`, `'ko-KR'`, `'es-MX'`, `'en-IN'`, `'en-SG'`, `'en-PH'`, `'en-IE'`, `'fr-CA'`.

Updates to this field are currently not supported.

`string food_language_code = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The foodLanguageCode.  
  
### getFoodLanguageCodeBytes()
    
    
    public abstract ByteString getFoodLanguageCodeBytes()

Output only. The food language code derived from the user's food database. Possible values: `'en-US'`, `'en-GB'`, `'de-DE'`, `'es-ES'`, `'fr-FR'`, `'zh-CN'`, `'zh-TW'`, `'ja-JP'`, `'en-AU'`, `'en-CA'`, `'it-IT'`, `'ko-KR'`, `'es-MX'`, `'en-IN'`, `'en-SG'`, `'en-PH'`, `'en-IE'`, `'fr-CA'`.

Updates to this field are currently not supported.

`string food_language_code = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for foodLanguageCode.  
  
### getGlucoseUnit()
    
    
    public abstract Settings.GlucoseUnit getGlucoseUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.GlucoseUnit glucose_unit = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.GlucoseUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.GlucoseUnit)` | The glucoseUnit.  
  
### getGlucoseUnitValue()
    
    
    public abstract int getGlucoseUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.GlucoseUnit glucose_unit = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for glucoseUnit.  
  
### getHeightUnit()
    
    
    public abstract Settings.HeightUnit getHeightUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.HeightUnit height_unit = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.HeightUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.HeightUnit)` | The heightUnit.  
  
### getHeightUnitValue()
    
    
    public abstract int getHeightUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.HeightUnit height_unit = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for heightUnit.  
  
### getLanguageLocale()
    
    
    public abstract String getLanguageLocale()

Optional. The locale defined in the user's account settings.

Updates to this field are currently not supported.

`string language_locale = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageLocale.  
  
### getLanguageLocaleBytes()
    
    
    public abstract ByteString getLanguageLocaleBytes()

Optional. The locale defined in the user's account settings.

Updates to this field are currently not supported.

`string language_locale = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageLocale.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of this Settings resource.

Format: `users/{user}/settings` Example: `users/1234567890/settings` or `users/me/settings` The {user} ID is a system-generated Google Health API user ID, a string of 1-63 characters consisting of lowercase and uppercase letters, numbers, and hyphens. The literal `me` can also be used to refer to the authenticated user.

This field is read-only.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of this Settings resource.

Format: `users/{user}/settings` Example: `users/1234567890/settings` or `users/me/settings` The {user} ID is a system-generated Google Health API user ID, a string of 1-63 characters consisting of lowercase and uppercase letters, numbers, and hyphens. The literal `me` can also be used to refer to the authenticated user.

This field is read-only.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getStrideLengthRunningType()
    
    
    public abstract Settings.StrideLengthType getStrideLengthRunningType()

Optional. The stride length type defined in the user's account settings for running.

Updates to this field are currently not supported.

` .google.devicesandservices.health.v4.Settings.StrideLengthType stride_length_running_type = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.StrideLengthType](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.StrideLengthType)` | The strideLengthRunningType.  
  
### getStrideLengthRunningTypeValue()
    
    
    public abstract int getStrideLengthRunningTypeValue()

Optional. The stride length type defined in the user's account settings for running.

Updates to this field are currently not supported.

` .google.devicesandservices.health.v4.Settings.StrideLengthType stride_length_running_type = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for strideLengthRunningType.  
  
### getStrideLengthWalkingType()
    
    
    public abstract Settings.StrideLengthType getStrideLengthWalkingType()

Optional. The stride length type defined in the user's account settings for walking.

Updates to this field are currently not supported.

` .google.devicesandservices.health.v4.Settings.StrideLengthType stride_length_walking_type = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.StrideLengthType](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.StrideLengthType)` | The strideLengthWalkingType.  
  
### getStrideLengthWalkingTypeValue()
    
    
    public abstract int getStrideLengthWalkingTypeValue()

Optional. The stride length type defined in the user's account settings for walking.

Updates to this field are currently not supported.

` .google.devicesandservices.health.v4.Settings.StrideLengthType stride_length_walking_type = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for strideLengthWalkingType.  
  
### getSwimUnit()
    
    
    public abstract Settings.SwimUnit getSwimUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.SwimUnit swim_unit = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.SwimUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.SwimUnit)` | The swimUnit.  
  
### getSwimUnitValue()
    
    
    public abstract int getSwimUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.SwimUnit swim_unit = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for swimUnit.  
  
### getTemperatureUnit()
    
    
    public abstract Settings.TemperatureUnit getTemperatureUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.TemperatureUnit temperature_unit = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.TemperatureUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.TemperatureUnit)` | The temperatureUnit.  
  
### getTemperatureUnitValue()
    
    
    public abstract int getTemperatureUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.TemperatureUnit temperature_unit = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for temperatureUnit.  
  
### getTimeZone()
    
    
    public abstract String getTimeZone()

Optional. The timezone defined in the user's account settings. This follows the IANA [Time Zone Database](https://www.iana.org/time-zones).

Updates to this field are currently not supported.

`string time_zone = 17 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The timeZone.  
  
### getTimeZoneBytes()
    
    
    public abstract ByteString getTimeZoneBytes()

Optional. The timezone defined in the user's account settings. This follows the IANA [Time Zone Database](https://www.iana.org/time-zones).

Updates to this field are currently not supported.

`string time_zone = 17 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for timeZone.  
  
### getUtcOffset()
    
    
    public abstract Duration getUtcOffset()

Optional. The user's timezone offset relative to UTC.

Updates to this field are currently not supported.

`.google.protobuf.Duration utc_offset = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The utcOffset.  
  
### getUtcOffsetOrBuilder()
    
    
    public abstract DurationOrBuilder getUtcOffsetOrBuilder()

Optional. The user's timezone offset relative to UTC.

Updates to this field are currently not supported.

`.google.protobuf.Duration utc_offset = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getWaterUnit()
    
    
    public abstract Settings.WaterUnit getWaterUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.WaterUnit water_unit = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.WaterUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.WaterUnit)` | The waterUnit.  
  
### getWaterUnitValue()
    
    
    public abstract int getWaterUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.WaterUnit water_unit = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for waterUnit.  
  
### getWeightUnit()
    
    
    public abstract Settings.WeightUnit getWeightUnit()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.WeightUnit weight_unit = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Settings.WeightUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings.WeightUnit)` | The weightUnit.  
  
### getWeightUnitValue()
    
    
    public abstract int getWeightUnitValue()

Optional. The measurement unit defined in the user's account settings.

` .google.devicesandservices.health.v4.Settings.WeightUnit weight_unit = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for weightUnit.  
  
### hasUtcOffset()
    
    
    public abstract boolean hasUtcOffset()

Optional. The user's timezone offset relative to UTC.

Updates to this field are currently not supported.

`.google.protobuf.Duration utc_offset = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the utcOffset field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
