---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.CardOrBuilder
title: Interface CardOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:14.627932+00:00
---

# Interface CardOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.CardOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CardOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public interface CardOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCardActions(int index)
    
    
    public abstract Card.CardAction getCardActions(int index)

The card's actions. Actions are added to the card's toolbar menu.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

For example, the following JSON constructs a card action menu with `Settings` and `Send Feedback` options:

`<code><code> "card_actions": [ { "actionLabel": "Settings", "onClick": { "action": { "functionName": "goToView", "parameters": [ { "key": "viewType", "value": "SETTING" } ], "loadIndicator": "LoadIndicator.SPINNER" } } }, { "actionLabel": "Send Feedback", "onClick": { "openLink": { "url": "https://example.com/feedback" } } } ] </code></code>`

`repeated .google.apps.card.v1.Card.CardAction card_actions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Card.CardAction](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardAction)` |   
  
### getCardActionsCount()
    
    
    public abstract int getCardActionsCount()

The card's actions. Actions are added to the card's toolbar menu.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

For example, the following JSON constructs a card action menu with `Settings` and `Send Feedback` options:

`<code><code> "card_actions": [ { "actionLabel": "Settings", "onClick": { "action": { "functionName": "goToView", "parameters": [ { "key": "viewType", "value": "SETTING" } ], "loadIndicator": "LoadIndicator.SPINNER" } } }, { "actionLabel": "Send Feedback", "onClick": { "openLink": { "url": "https://example.com/feedback" } } } ] </code></code>`

`repeated .google.apps.card.v1.Card.CardAction card_actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCardActionsList()
    
    
    public abstract List<Card.CardAction> getCardActionsList()

The card's actions. Actions are added to the card's toolbar menu.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

For example, the following JSON constructs a card action menu with `Settings` and `Send Feedback` options:

`<code><code> "card_actions": [ { "actionLabel": "Settings", "onClick": { "action": { "functionName": "goToView", "parameters": [ { "key": "viewType", "value": "SETTING" } ], "loadIndicator": "LoadIndicator.SPINNER" } } }, { "actionLabel": "Send Feedback", "onClick": { "openLink": { "url": "https://example.com/feedback" } } } ] </code></code>`

`repeated .google.apps.card.v1.Card.CardAction card_actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CardAction](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardAction)>` |   
  
### getCardActionsOrBuilder(int index)
    
    
    public abstract Card.CardActionOrBuilder getCardActionsOrBuilder(int index)

The card's actions. Actions are added to the card's toolbar menu.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

For example, the following JSON constructs a card action menu with `Settings` and `Send Feedback` options:

`<code><code> "card_actions": [ { "actionLabel": "Settings", "onClick": { "action": { "functionName": "goToView", "parameters": [ { "key": "viewType", "value": "SETTING" } ], "loadIndicator": "LoadIndicator.SPINNER" } } }, { "actionLabel": "Send Feedback", "onClick": { "openLink": { "url": "https://example.com/feedback" } } } ] </code></code>`

`repeated .google.apps.card.v1.Card.CardAction card_actions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Card.CardActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardActionOrBuilder)` |   
  
### getCardActionsOrBuilderList()
    
    
    public abstract List<? extends Card.CardActionOrBuilder> getCardActionsOrBuilderList()

The card's actions. Actions are added to the card's toolbar menu.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

For example, the following JSON constructs a card action menu with `Settings` and `Send Feedback` options:

`<code><code> "card_actions": [ { "actionLabel": "Settings", "onClick": { "action": { "functionName": "goToView", "parameters": [ { "key": "viewType", "value": "SETTING" } ], "loadIndicator": "LoadIndicator.SPINNER" } } }, { "actionLabel": "Send Feedback", "onClick": { "openLink": { "url": "https://example.com/feedback" } } } ] </code></code>`

`repeated .google.apps.card.v1.Card.CardAction card_actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.card.v1.Card.CardActionOrBuilder>` |   
  
### getDisplayStyle()
    
    
    public abstract Card.DisplayStyle getDisplayStyle()

In Google Workspace add-ons, sets the display properties of the `peekCardHeader`.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`.google.apps.card.v1.Card.DisplayStyle display_style = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Card.DisplayStyle](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.DisplayStyle)` | The displayStyle.  
  
### getDisplayStyleValue()
    
    
    public abstract int getDisplayStyleValue()

In Google Workspace add-ons, sets the display properties of the `peekCardHeader`.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`.google.apps.card.v1.Card.DisplayStyle display_style = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for displayStyle.  
  
### getFixedFooter()
    
    
    public abstract Card.CardFixedFooter getFixedFooter()

The fixed footer shown at the bottom of this card.

Setting `fixedFooter` without specifying a `primaryButton` or a `secondaryButton` causes an error. For Chat apps, you can use fixed footers in [dialogs](https://developers.google.com/workspace/chat/dialogs), but not [card messages](https://developers.google.com/workspace/chat/create-messages#create).

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`.google.apps.card.v1.Card.CardFixedFooter fixed_footer = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardFixedFooter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardFixedFooter)` | The fixedFooter.  
  
### getFixedFooterOrBuilder()
    
    
    public abstract Card.CardFixedFooterOrBuilder getFixedFooterOrBuilder()

The fixed footer shown at the bottom of this card.

Setting `fixedFooter` without specifying a `primaryButton` or a `secondaryButton` causes an error. For Chat apps, you can use fixed footers in [dialogs](https://developers.google.com/workspace/chat/dialogs), but not [card messages](https://developers.google.com/workspace/chat/create-messages#create).

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`.google.apps.card.v1.Card.CardFixedFooter fixed_footer = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardFixedFooterOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardFixedFooterOrBuilder)` |   
  
### getHeader()
    
    
    public abstract Card.CardHeader getHeader()

The header of the card. A header usually contains a leading image and a title. Headers always appear at the top of a card.

`.google.apps.card.v1.Card.CardHeader header = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardHeader](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardHeader)` | The header.  
  
### getHeaderOrBuilder()
    
    
    public abstract Card.CardHeaderOrBuilder getHeaderOrBuilder()

The header of the card. A header usually contains a leading image and a title. Headers always appear at the top of a card.

`.google.apps.card.v1.Card.CardHeader header = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardHeaderOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardHeaderOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Name of the card. Used as a card identifier in card navigation.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`string name = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the card. Used as a card identifier in card navigation.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`string name = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPeekCardHeader()
    
    
    public abstract Card.CardHeader getPeekCardHeader()

When displaying contextual content, the peek card header acts as a placeholder so that the user can navigate forward between the homepage cards and the contextual cards.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`.google.apps.card.v1.Card.CardHeader peek_card_header = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardHeader](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardHeader)` | The peekCardHeader.  
  
### getPeekCardHeaderOrBuilder()
    
    
    public abstract Card.CardHeaderOrBuilder getPeekCardHeaderOrBuilder()

When displaying contextual content, the peek card header acts as a placeholder so that the user can navigate forward between the homepage cards and the contextual cards.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`.google.apps.card.v1.Card.CardHeader peek_card_header = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Card.CardHeaderOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.CardHeaderOrBuilder)` |   
  
### getSectionDividerStyle()
    
    
    public abstract Card.DividerStyle getSectionDividerStyle()

The divider style between the header, sections and footer.

`.google.apps.card.v1.Card.DividerStyle section_divider_style = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Card.DividerStyle](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.DividerStyle)` | The sectionDividerStyle.  
  
### getSectionDividerStyleValue()
    
    
    public abstract int getSectionDividerStyleValue()

The divider style between the header, sections and footer.

`.google.apps.card.v1.Card.DividerStyle section_divider_style = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sectionDividerStyle.  
  
### getSections(int index)
    
    
    public abstract Card.Section getSections(int index)

Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Define a section of a card](https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card).

`repeated .google.apps.card.v1.Card.Section sections = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Card.Section](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.Section)` |   
  
### getSectionsCount()
    
    
    public abstract int getSectionsCount()

Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Define a section of a card](https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card).

`repeated .google.apps.card.v1.Card.Section sections = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSectionsList()
    
    
    public abstract List<Card.Section> getSectionsList()

Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Define a section of a card](https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card).

`repeated .google.apps.card.v1.Card.Section sections = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Section](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.Section)>` |   
  
### getSectionsOrBuilder(int index)
    
    
    public abstract Card.SectionOrBuilder getSectionsOrBuilder(int index)

Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Define a section of a card](https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card).

`repeated .google.apps.card.v1.Card.Section sections = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Card.SectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Card.SectionOrBuilder)` |   
  
### getSectionsOrBuilderList()
    
    
    public abstract List<? extends Card.SectionOrBuilder> getSectionsOrBuilderList()

Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Define a section of a card](https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card).

`repeated .google.apps.card.v1.Card.Section sections = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.card.v1.Card.SectionOrBuilder>` |   
  
### hasFixedFooter()
    
    
    public abstract boolean hasFixedFooter()

The fixed footer shown at the bottom of this card.

Setting `fixedFooter` without specifying a `primaryButton` or a `secondaryButton` causes an error. For Chat apps, you can use fixed footers in [dialogs](https://developers.google.com/workspace/chat/dialogs), but not [card messages](https://developers.google.com/workspace/chat/create-messages#create).

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`.google.apps.card.v1.Card.CardFixedFooter fixed_footer = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fixedFooter field is set.  
  
### hasHeader()
    
    
    public abstract boolean hasHeader()

The header of the card. A header usually contains a leading image and a title. Headers always appear at the top of a card.

`.google.apps.card.v1.Card.CardHeader header = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the header field is set.  
  
### hasPeekCardHeader()
    
    
    public abstract boolean hasPeekCardHeader()

When displaying contextual content, the peek card header acts as a placeholder so that the user can navigate forward between the homepage cards and the contextual cards.

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons):

`.google.apps.card.v1.Card.CardHeader peek_card_header = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the peekCardHeader field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
