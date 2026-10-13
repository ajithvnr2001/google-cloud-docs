---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.SpaceOrBuilder
title: Interface SpaceOrBuilder (0.66.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:06.616659+00:00
---

# Interface SpaceOrBuilder (0.66.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.SpaceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SpaceOrBuilder (0.66.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.66.0 (latest)  0.62.0  0.61.0  0.60.0  0.58.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.47.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface SpaceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActiveConference()
    
    
    public abstract ActiveConference getActiveConference()

Active conference, if it exists.

`.google.apps.meet.v2.ActiveConference active_conference = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ActiveConference](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.ActiveConference)` | The activeConference.  
  
### getActiveConferenceOrBuilder()
    
    
    public abstract ActiveConferenceOrBuilder getActiveConferenceOrBuilder()

Active conference, if it exists.

`.google.apps.meet.v2.ActiveConference active_conference = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ActiveConferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.ActiveConferenceOrBuilder)` |   
  
### getConfig()
    
    
    public abstract SpaceConfig getConfig()

Configuration pertaining to the meeting space.

`.google.apps.meet.v2.SpaceConfig config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SpaceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.SpaceConfig)` | The config.  
  
### getConfigOrBuilder()
    
    
    public abstract SpaceConfigOrBuilder getConfigOrBuilder()

Configuration pertaining to the meeting space.

`.google.apps.meet.v2.SpaceConfig config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SpaceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.SpaceConfigOrBuilder)` |   
  
### getGatewaySipAccess(int index)
    
    
    public abstract Space.GatewaySipAccess getGatewaySipAccess(int index)

Output only. The SIP-based access methods that can be used to join the conference. Can be empty.

` repeated .google.apps.meet.v2.Space.GatewaySipAccess gateway_sip_access = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.GatewaySipAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.GatewaySipAccess)` |   
  
### getGatewaySipAccessCount()
    
    
    public abstract int getGatewaySipAccessCount()

Output only. The SIP-based access methods that can be used to join the conference. Can be empty.

` repeated .google.apps.meet.v2.Space.GatewaySipAccess gateway_sip_access = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGatewaySipAccessList()
    
    
    public abstract List<Space.GatewaySipAccess> getGatewaySipAccessList()

Output only. The SIP-based access methods that can be used to join the conference. Can be empty.

` repeated .google.apps.meet.v2.Space.GatewaySipAccess gateway_sip_access = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GatewaySipAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.GatewaySipAccess)>` |   
  
### getGatewaySipAccessOrBuilder(int index)
    
    
    public abstract Space.GatewaySipAccessOrBuilder getGatewaySipAccessOrBuilder(int index)

Output only. The SIP-based access methods that can be used to join the conference. Can be empty.

` repeated .google.apps.meet.v2.Space.GatewaySipAccess gateway_sip_access = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.GatewaySipAccessOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.GatewaySipAccessOrBuilder)` |   
  
### getGatewaySipAccessOrBuilderList()
    
    
    public abstract List<? extends Space.GatewaySipAccessOrBuilder> getGatewaySipAccessOrBuilderList()

Output only. The SIP-based access methods that can be used to join the conference. Can be empty.

` repeated .google.apps.meet.v2.Space.GatewaySipAccess gateway_sip_access = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.meet.v2.Space.GatewaySipAccessOrBuilder>` |   
  
### getMeetingCode()
    
    
    public abstract String getMeetingCode()

Output only. Type friendly unique string used to join the meeting.

Format: `[a-z]+-[a-z]+-[a-z]+`. For example, `abc-mnop-xyz`.

The maximum length is 128 characters.

Can only be used as an alias of the space name to get the space.

`string meeting_code = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The meetingCode.  
  
### getMeetingCodeBytes()
    
    
    public abstract ByteString getMeetingCodeBytes()

Output only. Type friendly unique string used to join the meeting.

Format: `[a-z]+-[a-z]+-[a-z]+`. For example, `abc-mnop-xyz`.

The maximum length is 128 characters.

Can only be used as an alias of the space name to get the space.

`string meeting_code = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for meetingCode.  
  
### getMeetingUri()
    
    
    public abstract String getMeetingUri()

Output only. URI used to join meetings consisting of `<https://meet.google.com/>` followed by the `meeting_code`. For example, `<https://meet.google.com/abc-mnop-xyz>`.

`string meeting_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The meetingUri.  
  
### getMeetingUriBytes()
    
    
    public abstract ByteString getMeetingUriBytes()

Output only. URI used to join meetings consisting of `<https://meet.google.com/>` followed by the `meeting_code`. For example, `<https://meet.google.com/abc-mnop-xyz>`.

`string meeting_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for meetingUri.  
  
### getName()
    
    
    public abstract String getName()

Immutable. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space).

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space).

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPhoneAccess(int index)
    
    
    public abstract Space.PhoneAccess getPhoneAccess(int index)

Output only. All regional phone access methods for this meeting space. Can be empty.

` repeated .google.apps.meet.v2.Space.PhoneAccess phone_access = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PhoneAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.PhoneAccess)` |   
  
### getPhoneAccessCount()
    
    
    public abstract int getPhoneAccessCount()

Output only. All regional phone access methods for this meeting space. Can be empty.

` repeated .google.apps.meet.v2.Space.PhoneAccess phone_access = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPhoneAccessList()
    
    
    public abstract List<Space.PhoneAccess> getPhoneAccessList()

Output only. All regional phone access methods for this meeting space. Can be empty.

` repeated .google.apps.meet.v2.Space.PhoneAccess phone_access = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PhoneAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.PhoneAccess)>` |   
  
### getPhoneAccessOrBuilder(int index)
    
    
    public abstract Space.PhoneAccessOrBuilder getPhoneAccessOrBuilder(int index)

Output only. All regional phone access methods for this meeting space. Can be empty.

` repeated .google.apps.meet.v2.Space.PhoneAccess phone_access = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PhoneAccessOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Space.PhoneAccessOrBuilder)` |   
  
### getPhoneAccessOrBuilderList()
    
    
    public abstract List<? extends Space.PhoneAccessOrBuilder> getPhoneAccessOrBuilderList()

Output only. All regional phone access methods for this meeting space. Can be empty.

` repeated .google.apps.meet.v2.Space.PhoneAccess phone_access = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.meet.v2.Space.PhoneAccessOrBuilder>` |   
  
### hasActiveConference()
    
    
    public abstract boolean hasActiveConference()

Active conference, if it exists.

`.google.apps.meet.v2.ActiveConference active_conference = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeConference field is set.  
  
### hasConfig()
    
    
    public abstract boolean hasConfig()

Configuration pertaining to the meeting space.

`.google.apps.meet.v2.SpaceConfig config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the config field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
