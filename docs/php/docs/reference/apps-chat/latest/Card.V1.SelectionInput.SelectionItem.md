---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.SelectionInput.SelectionItem
title: Google Apps Chat V1 Client - Class SelectionItem (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:12.994664+00:00
---

# Google Apps Chat V1 Client - Class SelectionItem (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.SelectionInput.SelectionItem

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class SelectionItem (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class SelectionItem.

An item that users can select in a selection input, such as a checkbox or switch. Supports up to 100 items.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

Generated from protobuf message `google.apps.card.v1.SelectionInput.SelectionItem`

## Namespace

Google \ Apps \ Card \ V1 \ SelectionInput

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ text` |  `string`   
The text that identifies or describes the item to users.  
`↳ value` |  `string`   
The value associated with this item. The client should use this as a form input value. For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data).  
`↳ selected` |  `bool`   
Whether the item is selected by default. If the selection input only accepts one value (such as for radio buttons or a dropdown menu), only set this field for one item.  
`↳ start_icon_uri` |  `string`   
  
`↳ bottom_text` |  `string`   
For multiselect menus, a text description or label that's displayed below the item's `text` field.  
  
### getText

The text that identifies or describes the item to users.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setText

The text that identifies or describes the item to users.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValue

The value associated with this item. The client should use this as a form input value.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setValue

The value associated with this item. The client should use this as a form input value.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSelected

Whether the item is selected by default. If the selection input only accepts one value (such as for radio buttons or a dropdown menu), only set this field for one item.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSelected

Whether the item is selected by default. If the selection input only accepts one value (such as for radio buttons or a dropdown menu), only set this field for one item.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartIconUri

Generated from protobuf field `string start_icon_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasStartIconUri

### setStartIconUri

Generated from protobuf field `string start_icon_uri = 4;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBottomText

For multiselect menus, a text description or label that's displayed below the item's `text` field.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBottomText

For multiselect menus, a text description or label that's displayed below the item's `text` field.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartIcon

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
