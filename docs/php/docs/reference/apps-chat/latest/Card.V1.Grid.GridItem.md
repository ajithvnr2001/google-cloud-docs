---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Grid.GridItem
title: Google Apps Chat V1 Client - Class GridItem (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:06.478683+00:00
---

# Google Apps Chat V1 Client - Class GridItem (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Grid.GridItem

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class GridItem (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class GridItem.

Represents an item in a grid layout. Items can contain text, an image, or both text and an image.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

Generated from protobuf message `google.apps.card.v1.Grid.GridItem`

## Namespace

Google \ Apps \ Card \ V1 \ Grid

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ id` |  `string`   
A user-specified identifier for this grid item. This identifier is returned in the parent grid's `onClick` callback parameters.  
`↳ image` |  `[Google\Apps\Card\V1\ImageComponent](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.ImageComponent)`   
The image that displays in the grid item.  
`↳ title` |  `string`   
The grid item's title.  
`↳ subtitle` |  `string`   
The grid item's subtitle.  
`↳ layout` |  `int`   
The layout to use for the grid item.  
  
### getId

A user-specified identifier for this grid item. This identifier is returned in the parent grid's `onClick` callback parameters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setId

A user-specified identifier for this grid item. This identifier is returned in the parent grid's `onClick` callback parameters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getImage

The image that displays in the grid item.

**Returns**  
---  
**Type** | **Description**  
`[Google\Apps\Card\V1\ImageComponent](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.ImageComponent)|null` |   
  
### hasImage

### clearImage

### setImage

The image that displays in the grid item.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Apps\Card\V1\ImageComponent](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.ImageComponent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTitle

The grid item's title.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTitle

The grid item's title.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubtitle

The grid item's subtitle.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSubtitle

The grid item's subtitle.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLayout

The layout to use for the grid item.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [GridItemLayout](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Grid.GridItem.GridItemLayout).  
  
### setLayout

The layout to use for the grid item.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [GridItemLayout](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Grid.GridItem.GridItemLayout).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
