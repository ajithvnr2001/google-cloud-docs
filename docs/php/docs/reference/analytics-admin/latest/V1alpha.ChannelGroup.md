---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup
title: Google Analytics Admin V1alpha Client - Class ChannelGroup (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:53.708830+00:00
---

# Google Analytics Admin V1alpha Client - Class ChannelGroup (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ChannelGroup (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ChannelGroup.

A resource message representing a Channel Group.

Generated from protobuf message `google.analytics.admin.v1alpha.ChannelGroup`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. The resource name for this Channel Group resource. Format: properties/{property}/channelGroups/{channel_group}  
`↳ display_name` |  `string`   
Required. The display name of the Channel Group. Max length of 80 characters.  
`↳ description` |  `string`   
The description of the Channel Group. Max length of 256 characters.  
`↳ grouping_rule` |  `array<[GroupingRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GroupingRule)>`   
Required. The grouping rules of channels. Maximum number of rules is 50.  
`↳ system_defined` |  `bool`   
Output only. If true, then this channel group is the Default Channel Group predefined by Google Analytics. Display name and grouping rules cannot be updated for this channel group.  
`↳ primary` |  `bool`   
Optional. If true, this channel group will be used as the default channel group for reports. Only one channel group can be set as `primary` at any time. If the `primary` field gets set on a channel group, it will get unset on the previous primary channel group. The Google Analytics predefined channel group is the primary by default.  
  
### getName

Output only. The resource name for this Channel Group resource.

Format: properties/{property}/channelGroups/{channel_group}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name for this Channel Group resource.

Format: properties/{property}/channelGroups/{channel_group}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The display name of the Channel Group. Max length of 80 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The display name of the Channel Group. Max length of 80 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

The description of the Channel Group. Max length of 256 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

The description of the Channel Group. Max length of 256 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGroupingRule

Required. The grouping rules of channels. Maximum number of rules is 50.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[GroupingRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GroupingRule)>` |   
  
### setGroupingRule

Required. The grouping rules of channels. Maximum number of rules is 50.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[GroupingRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GroupingRule)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSystemDefined

Output only. If true, then this channel group is the Default Channel Group predefined by Google Analytics. Display name and grouping rules cannot be updated for this channel group.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSystemDefined

Output only. If true, then this channel group is the Default Channel Group predefined by Google Analytics. Display name and grouping rules cannot be updated for this channel group.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPrimary

Optional. If true, this channel group will be used as the default channel group for reports. Only one channel group can be set as `primary` at any time. If the `primary` field gets set on a channel group, it will get unset on the previous primary channel group.

The Google Analytics predefined channel group is the primary by default.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setPrimary

Optional. If true, this channel group will be used as the default channel group for reports. Only one channel group can be set as `primary` at any time. If the `primary` field gets set on a channel group, it will get unset on the previous primary channel group.

The Google Analytics predefined channel group is the primary by default.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
