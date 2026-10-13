---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Columns.Column.HorizontalSizeStyle
title: Google Apps Chat V1 Client - Class HorizontalSizeStyle (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:04.736498+00:00
---

# Google Apps Chat V1 Client - Class HorizontalSizeStyle (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Card.V1.Columns.Column.HorizontalSizeStyle

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class HorizontalSizeStyle (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class HorizontalSizeStyle.

Specifies how a column fills the width of the card. The width of each column depends on both the `HorizontalSizeStyle` and the width of the widgets within the column.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend)

Protobuf type `google.apps.card.v1.Columns.Column.HorizontalSizeStyle`

## Namespace

Google \ Apps \ Card \ V1 \ Columns \ Column

## Methods 

### static::name

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
  
  
### static::value

**Parameter**  
---  
**Name** | **Description**  
`name` |  `mixed`   
  
  
## Constants 

### HORIZONTAL_SIZE_STYLE_UNSPECIFIED
    
    
    Value: 0

Don't use. Unspecified.

Generated from protobuf enum `HORIZONTAL_SIZE_STYLE_UNSPECIFIED = 0;`

### FILL_AVAILABLE_SPACE
    
    
    Value: 1

Default value. Column fills the available space, up to 70% of the card's width. If both columns are set to `FILL_AVAILABLE_SPACE`, each column fills 50% of the space.

Generated from protobuf enum `FILL_AVAILABLE_SPACE = 1;`

### FILL_MINIMUM_SPACE
    
    
    Value: 2

Column fills the least amount of space possible and no more than 30% of the card's width.

Generated from protobuf enum `FILL_MINIMUM_SPACE = 2;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
