---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Chip
title: Google Apps Chat V1 Client - Class Chip (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:53.453884+00:00
---

# Google Apps Chat V1 Client - Class Chip (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Chip

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class Chip (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class Chip.

A text, icon, or text and icon chip that users can click.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

Generated from protobuf message `google.apps.card.v1.Chip`

## Namespace

Google \ Apps \ Card \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ icon` |  `[Icon](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Icon)`   
The icon image. If both `icon` and `text` are set, then the icon appears before the text.  
`↳ label` |  `string`   
The text displayed inside the chip.  
`↳ on_click` |  `[OnClick](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.OnClick)`   
Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function.  
`↳ enabled` |  `bool`   
Whether the chip is in an active state and responds to user actions. Defaults to `true`. Deprecated. Use `disabled` instead.  
`↳ disabled` |  `bool`   
Whether the chip is in an inactive state and ignores user actions. Defaults to `false`.  
`↳ alt_text` |  `string`   
The alternative text that's used for accessibility. Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at <https://developers.google.com/workspace/chat>".  
  
### getIcon

The icon image. If both `icon` and `text` are set, then the icon appears before the text.

**Returns**  
---  
**Type** | **Description**  
`[Icon](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Icon)|null` |   
  
### hasIcon

### clearIcon

### setIcon

The icon image. If both `icon` and `text` are set, then the icon appears before the text.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Icon](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Icon)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabel

The text displayed inside the chip.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLabel

The text displayed inside the chip.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOnClick

Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function.

**Returns**  
---  
**Type** | **Description**  
`[OnClick](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.OnClick)|null` |   
  
### hasOnClick

### clearOnClick

### setOnClick

Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[OnClick](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.OnClick)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEnabled

Whether the chip is in an active state and responds to user actions.

Defaults to `true`. Deprecated. Use `disabled` instead.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEnabled

Whether the chip is in an active state and responds to user actions.

Defaults to `true`. Deprecated. Use `disabled` instead.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisabled

Whether the chip is in an inactive state and ignores user actions.

Defaults to `false`.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDisabled

Whether the chip is in an inactive state and ignores user actions.

Defaults to `false`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAltText

The alternative text that's used for accessibility.

Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at <https://developers.google.com/workspace/chat>".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAltText

The alternative text that's used for accessibility.

Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at <https://developers.google.com/workspace/chat>".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
