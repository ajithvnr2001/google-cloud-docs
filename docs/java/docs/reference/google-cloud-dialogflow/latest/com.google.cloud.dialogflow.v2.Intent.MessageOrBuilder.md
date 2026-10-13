---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.MessageOrBuilder
title: Interface Intent.MessageOrBuilder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:34.341821+00:00
---

# Interface Intent.MessageOrBuilder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.MessageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Intent.MessageOrBuilder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public static interface Intent.MessageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBasicCard()
    
    
    public abstract Intent.Message.BasicCard getBasicCard()

The basic card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.BasicCard basic_card = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.BasicCard](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.BasicCard)` | The basicCard.  
  
### getBasicCardOrBuilder()
    
    
    public abstract Intent.Message.BasicCardOrBuilder getBasicCardOrBuilder()

The basic card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.BasicCard basic_card = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.BasicCardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.BasicCardOrBuilder)` |   
  
### getBrowseCarouselCard()
    
    
    public abstract Intent.Message.BrowseCarouselCard getBrowseCarouselCard()

Browse carousel card for Actions on Google.

` .google.cloud.dialogflow.v2.Intent.Message.BrowseCarouselCard browse_carousel_card = 22; `

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.BrowseCarouselCard](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.BrowseCarouselCard)` | The browseCarouselCard.  
  
### getBrowseCarouselCardOrBuilder()
    
    
    public abstract Intent.Message.BrowseCarouselCardOrBuilder getBrowseCarouselCardOrBuilder()

Browse carousel card for Actions on Google.

` .google.cloud.dialogflow.v2.Intent.Message.BrowseCarouselCard browse_carousel_card = 22; `

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.BrowseCarouselCardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.BrowseCarouselCardOrBuilder)` |   
  
### getCard()
    
    
    public abstract Intent.Message.Card getCard()

The card response.

`.google.cloud.dialogflow.v2.Intent.Message.Card card = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.Card](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.Card)` | The card.  
  
### getCardOrBuilder()
    
    
    public abstract Intent.Message.CardOrBuilder getCardOrBuilder()

The card response.

`.google.cloud.dialogflow.v2.Intent.Message.Card card = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.CardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.CardOrBuilder)` |   
  
### getCarouselSelect()
    
    
    public abstract Intent.Message.CarouselSelect getCarouselSelect()

The carousel card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.CarouselSelect carousel_select = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.CarouselSelect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.CarouselSelect)` | The carouselSelect.  
  
### getCarouselSelectOrBuilder()
    
    
    public abstract Intent.Message.CarouselSelectOrBuilder getCarouselSelectOrBuilder()

The carousel card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.CarouselSelect carousel_select = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.CarouselSelectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.CarouselSelectOrBuilder)` |   
  
### getImage()
    
    
    public abstract Intent.Message.Image getImage()

The image response.

`.google.cloud.dialogflow.v2.Intent.Message.Image image = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.Image)` | The image.  
  
### getImageOrBuilder()
    
    
    public abstract Intent.Message.ImageOrBuilder getImageOrBuilder()

The image response.

`.google.cloud.dialogflow.v2.Intent.Message.Image image = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.ImageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.ImageOrBuilder)` |   
  
### getLinkOutSuggestion()
    
    
    public abstract Intent.Message.LinkOutSuggestion getLinkOutSuggestion()

The link out suggestion chip for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.LinkOutSuggestion link_out_suggestion = 10; `

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.LinkOutSuggestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.LinkOutSuggestion)` | The linkOutSuggestion.  
  
### getLinkOutSuggestionOrBuilder()
    
    
    public abstract Intent.Message.LinkOutSuggestionOrBuilder getLinkOutSuggestionOrBuilder()

The link out suggestion chip for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.LinkOutSuggestion link_out_suggestion = 10; `

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.LinkOutSuggestionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.LinkOutSuggestionOrBuilder)` |   
  
### getListSelect()
    
    
    public abstract Intent.Message.ListSelect getListSelect()

The list card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.ListSelect list_select = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.ListSelect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.ListSelect)` | The listSelect.  
  
### getListSelectOrBuilder()
    
    
    public abstract Intent.Message.ListSelectOrBuilder getListSelectOrBuilder()

The list card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.ListSelect list_select = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.ListSelectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.ListSelectOrBuilder)` |   
  
### getMediaContent()
    
    
    public abstract Intent.Message.MediaContent getMediaContent()

The media content card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.MediaContent media_content = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.MediaContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.MediaContent)` | The mediaContent.  
  
### getMediaContentOrBuilder()
    
    
    public abstract Intent.Message.MediaContentOrBuilder getMediaContentOrBuilder()

The media content card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.MediaContent media_content = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.MediaContentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.MediaContentOrBuilder)` |   
  
### getMessageCase()
    
    
    public abstract Intent.Message.MessageCase getMessageCase()

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.MessageCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.MessageCase)` |   
  
### getPayload()
    
    
    public abstract Struct getPayload()

A custom platform-specific response.

`.google.protobuf.Struct payload = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The payload.  
  
### getPayloadOrBuilder()
    
    
    public abstract StructOrBuilder getPayloadOrBuilder()

A custom platform-specific response.

`.google.protobuf.Struct payload = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getPlatform()
    
    
    public abstract Intent.Message.Platform getPlatform()

Optional. The platform that this message is intended for.

` .google.cloud.dialogflow.v2.Intent.Message.Platform platform = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.Platform](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.Platform)` | The platform.  
  
### getPlatformValue()
    
    
    public abstract int getPlatformValue()

Optional. The platform that this message is intended for.

` .google.cloud.dialogflow.v2.Intent.Message.Platform platform = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for platform.  
  
### getQuickReplies()
    
    
    public abstract Intent.Message.QuickReplies getQuickReplies()

The quick replies response.

`.google.cloud.dialogflow.v2.Intent.Message.QuickReplies quick_replies = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.QuickReplies](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.QuickReplies)` | The quickReplies.  
  
### getQuickRepliesOrBuilder()
    
    
    public abstract Intent.Message.QuickRepliesOrBuilder getQuickRepliesOrBuilder()

The quick replies response.

`.google.cloud.dialogflow.v2.Intent.Message.QuickReplies quick_replies = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.QuickRepliesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.QuickRepliesOrBuilder)` |   
  
### getSimpleResponses()
    
    
    public abstract Intent.Message.SimpleResponses getSimpleResponses()

The voice and text-only responses for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.SimpleResponses simple_responses = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.SimpleResponses](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.SimpleResponses)` | The simpleResponses.  
  
### getSimpleResponsesOrBuilder()
    
    
    public abstract Intent.Message.SimpleResponsesOrBuilder getSimpleResponsesOrBuilder()

The voice and text-only responses for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.SimpleResponses simple_responses = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.SimpleResponsesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.SimpleResponsesOrBuilder)` |   
  
### getSuggestions()
    
    
    public abstract Intent.Message.Suggestions getSuggestions()

The suggestion chips for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.Suggestions suggestions = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.Suggestions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.Suggestions)` | The suggestions.  
  
### getSuggestionsOrBuilder()
    
    
    public abstract Intent.Message.SuggestionsOrBuilder getSuggestionsOrBuilder()

The suggestion chips for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.Suggestions suggestions = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.SuggestionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.SuggestionsOrBuilder)` |   
  
### getTableCard()
    
    
    public abstract Intent.Message.TableCard getTableCard()

Table card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.TableCard table_card = 23;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.TableCard](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.TableCard)` | The tableCard.  
  
### getTableCardOrBuilder()
    
    
    public abstract Intent.Message.TableCardOrBuilder getTableCardOrBuilder()

Table card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.TableCard table_card = 23;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.TableCardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.TableCardOrBuilder)` |   
  
### getText()
    
    
    public abstract Intent.Message.Text getText()

The text response.

`.google.cloud.dialogflow.v2.Intent.Message.Text text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.Text](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.Text)` | The text.  
  
### getTextOrBuilder()
    
    
    public abstract Intent.Message.TextOrBuilder getTextOrBuilder()

The text response.

`.google.cloud.dialogflow.v2.Intent.Message.Text text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Intent.Message.TextOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message.TextOrBuilder)` |   
  
### hasBasicCard()
    
    
    public abstract boolean hasBasicCard()

The basic card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.BasicCard basic_card = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the basicCard field is set.  
  
### hasBrowseCarouselCard()
    
    
    public abstract boolean hasBrowseCarouselCard()

Browse carousel card for Actions on Google.

` .google.cloud.dialogflow.v2.Intent.Message.BrowseCarouselCard browse_carousel_card = 22; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the browseCarouselCard field is set.  
  
### hasCard()
    
    
    public abstract boolean hasCard()

The card response.

`.google.cloud.dialogflow.v2.Intent.Message.Card card = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the card field is set.  
  
### hasCarouselSelect()
    
    
    public abstract boolean hasCarouselSelect()

The carousel card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.CarouselSelect carousel_select = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the carouselSelect field is set.  
  
### hasImage()
    
    
    public abstract boolean hasImage()

The image response.

`.google.cloud.dialogflow.v2.Intent.Message.Image image = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the image field is set.  
  
### hasLinkOutSuggestion()
    
    
    public abstract boolean hasLinkOutSuggestion()

The link out suggestion chip for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.LinkOutSuggestion link_out_suggestion = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the linkOutSuggestion field is set.  
  
### hasListSelect()
    
    
    public abstract boolean hasListSelect()

The list card response for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.ListSelect list_select = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the listSelect field is set.  
  
### hasMediaContent()
    
    
    public abstract boolean hasMediaContent()

The media content card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.MediaContent media_content = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mediaContent field is set.  
  
### hasPayload()
    
    
    public abstract boolean hasPayload()

A custom platform-specific response.

`.google.protobuf.Struct payload = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the payload field is set.  
  
### hasQuickReplies()
    
    
    public abstract boolean hasQuickReplies()

The quick replies response.

`.google.cloud.dialogflow.v2.Intent.Message.QuickReplies quick_replies = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quickReplies field is set.  
  
### hasSimpleResponses()
    
    
    public abstract boolean hasSimpleResponses()

The voice and text-only responses for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.SimpleResponses simple_responses = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the simpleResponses field is set.  
  
### hasSuggestions()
    
    
    public abstract boolean hasSuggestions()

The suggestion chips for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.Suggestions suggestions = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the suggestions field is set.  
  
### hasTableCard()
    
    
    public abstract boolean hasTableCard()

Table card for Actions on Google.

`.google.cloud.dialogflow.v2.Intent.Message.TableCard table_card = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tableCard field is set.  
  
### hasText()
    
    
    public abstract boolean hasText()

The text response.

`.google.cloud.dialogflow.v2.Intent.Message.Text text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
