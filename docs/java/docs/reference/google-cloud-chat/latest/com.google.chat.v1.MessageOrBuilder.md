---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageOrBuilder
title: Interface MessageOrBuilder (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:42.706298+00:00
---

# Interface MessageOrBuilder (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MessageOrBuilder (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface MessageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessoryWidgets(int index)
    
    
    public abstract AccessoryWidget getAccessoryWidgets(int index)

Optional. One or more interactive widgets that appear at the bottom of a message. You can add accessory widgets to messages that contain text, cards, or both text and cards. Not supported for messages that contain dialogs. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

Creating a message with accessory widgets requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).

` repeated .google.chat.v1.AccessoryWidget accessory_widgets = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessoryWidget](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidget)` |   
  
### getAccessoryWidgetsCount()
    
    
    public abstract int getAccessoryWidgetsCount()

Optional. One or more interactive widgets that appear at the bottom of a message. You can add accessory widgets to messages that contain text, cards, or both text and cards. Not supported for messages that contain dialogs. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

Creating a message with accessory widgets requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).

` repeated .google.chat.v1.AccessoryWidget accessory_widgets = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessoryWidgetsList()
    
    
    public abstract List<AccessoryWidget> getAccessoryWidgetsList()

Optional. One or more interactive widgets that appear at the bottom of a message. You can add accessory widgets to messages that contain text, cards, or both text and cards. Not supported for messages that contain dialogs. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

Creating a message with accessory widgets requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).

` repeated .google.chat.v1.AccessoryWidget accessory_widgets = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AccessoryWidget](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidget)>` |   
  
### getAccessoryWidgetsOrBuilder(int index)
    
    
    public abstract AccessoryWidgetOrBuilder getAccessoryWidgetsOrBuilder(int index)

Optional. One or more interactive widgets that appear at the bottom of a message. You can add accessory widgets to messages that contain text, cards, or both text and cards. Not supported for messages that contain dialogs. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

Creating a message with accessory widgets requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).

` repeated .google.chat.v1.AccessoryWidget accessory_widgets = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessoryWidgetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidgetOrBuilder)` |   
  
### getAccessoryWidgetsOrBuilderList()
    
    
    public abstract List<? extends AccessoryWidgetOrBuilder> getAccessoryWidgetsOrBuilderList()

Optional. One or more interactive widgets that appear at the bottom of a message. You can add accessory widgets to messages that contain text, cards, or both text and cards. Not supported for messages that contain dialogs. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

Creating a message with accessory widgets requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).

` repeated .google.chat.v1.AccessoryWidget accessory_widgets = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.AccessoryWidgetOrBuilder>` |   
  
### getActionResponse()
    
    
    public abstract ActionResponse getActionResponse()

Input only. Parameters that a Chat app can use to configure how its response is posted.

` .google.chat.v1.ActionResponse action_response = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse)` | The actionResponse.  
  
### getActionResponseOrBuilder()
    
    
    public abstract ActionResponseOrBuilder getActionResponseOrBuilder()

Input only. Parameters that a Chat app can use to configure how its response is posted.

` .google.chat.v1.ActionResponse action_response = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ActionResponseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponseOrBuilder)` |   
  
### getAnnotations(int index)
    
    
    public abstract Annotation getAnnotations(int index)

Output only. Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

` repeated .google.chat.v1.Annotation annotations = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Output only. Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

` repeated .google.chat.v1.Annotation annotations = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsList()
    
    
    public abstract List<Annotation> getAnnotationsList()

Output only. Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

` repeated .google.chat.v1.Annotation annotations = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)>` |   
  
### getAnnotationsOrBuilder(int index)
    
    
    public abstract AnnotationOrBuilder getAnnotationsOrBuilder(int index)

Output only. Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

` repeated .google.chat.v1.Annotation annotations = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationOrBuilder)` |   
  
### getAnnotationsOrBuilderList()
    
    
    public abstract List<? extends AnnotationOrBuilder> getAnnotationsOrBuilderList()

Output only. Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

` repeated .google.chat.v1.Annotation annotations = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.AnnotationOrBuilder>` |   
  
### getArgumentText()
    
    
    public abstract String getArgumentText()

Output only. Plain-text body of the message with all Chat app mentions stripped out.

`string argument_text = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The argumentText.  
  
### getArgumentTextBytes()
    
    
    public abstract ByteString getArgumentTextBytes()

Output only. Plain-text body of the message with all Chat app mentions stripped out.

`string argument_text = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for argumentText.  
  
### getAttachedGifs(int index)
    
    
    public abstract AttachedGif getAttachedGifs(int index)

Output only. GIF images that are attached to the message.

` repeated .google.chat.v1.AttachedGif attached_gifs = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedGif](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGif)` |   
  
### getAttachedGifsCount()
    
    
    public abstract int getAttachedGifsCount()

Output only. GIF images that are attached to the message.

` repeated .google.chat.v1.AttachedGif attached_gifs = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttachedGifsList()
    
    
    public abstract List<AttachedGif> getAttachedGifsList()

Output only. GIF images that are attached to the message.

` repeated .google.chat.v1.AttachedGif attached_gifs = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AttachedGif](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGif)>` |   
  
### getAttachedGifsOrBuilder(int index)
    
    
    public abstract AttachedGifOrBuilder getAttachedGifsOrBuilder(int index)

Output only. GIF images that are attached to the message.

` repeated .google.chat.v1.AttachedGif attached_gifs = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedGifOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGifOrBuilder)` |   
  
### getAttachedGifsOrBuilderList()
    
    
    public abstract List<? extends AttachedGifOrBuilder> getAttachedGifsOrBuilderList()

Output only. GIF images that are attached to the message.

` repeated .google.chat.v1.AttachedGif attached_gifs = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.AttachedGifOrBuilder>` |   
  
### getAttachment(int index)
    
    
    public abstract Attachment getAttachment(int index)

Optional. User-uploaded attachment.

` repeated .google.chat.v1.Attachment attachment = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)` |   
  
### getAttachmentCount()
    
    
    public abstract int getAttachmentCount()

Optional. User-uploaded attachment.

` repeated .google.chat.v1.Attachment attachment = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttachmentList()
    
    
    public abstract List<Attachment> getAttachmentList()

Optional. User-uploaded attachment.

` repeated .google.chat.v1.Attachment attachment = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)>` |   
  
### getAttachmentOrBuilder(int index)
    
    
    public abstract AttachmentOrBuilder getAttachmentOrBuilder(int index)

Optional. User-uploaded attachment.

` repeated .google.chat.v1.Attachment attachment = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentOrBuilder)` |   
  
### getAttachmentOrBuilderList()
    
    
    public abstract List<? extends AttachmentOrBuilder> getAttachmentOrBuilderList()

Optional. User-uploaded attachment.

` repeated .google.chat.v1.Attachment attachment = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.AttachmentOrBuilder>` |   
  
### getCards(int index) (deprecated)
    
    
    public abstract ContextualAddOnMarkup.Card getCards(int index)

Deprecated: Use `cards_v2` instead.

Rich, formatted, and interactive cards that you can use to display UI elements such as: formatted texts, buttons, and clickable images. Cards are normally displayed below the plain-text body of the message. `cards` and `cards_v2` can have a maximum size of 32 KB.

`repeated .google.chat.v1.ContextualAddOnMarkup.Card cards = 5 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContextualAddOnMarkup.Card](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card)` |   
  
### getCardsCount() (deprecated)
    
    
    public abstract int getCardsCount()

Deprecated: Use `cards_v2` instead.

Rich, formatted, and interactive cards that you can use to display UI elements such as: formatted texts, buttons, and clickable images. Cards are normally displayed below the plain-text body of the message. `cards` and `cards_v2` can have a maximum size of 32 KB.

`repeated .google.chat.v1.ContextualAddOnMarkup.Card cards = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCardsList() (deprecated)
    
    
    public abstract List<ContextualAddOnMarkup.Card> getCardsList()

Deprecated: Use `cards_v2` instead.

Rich, formatted, and interactive cards that you can use to display UI elements such as: formatted texts, buttons, and clickable images. Cards are normally displayed below the plain-text body of the message. `cards` and `cards_v2` can have a maximum size of 32 KB.

`repeated .google.chat.v1.ContextualAddOnMarkup.Card cards = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Card](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card)>` |   
  
### getCardsOrBuilder(int index) (deprecated)
    
    
    public abstract ContextualAddOnMarkup.CardOrBuilder getCardsOrBuilder(int index)

Deprecated: Use `cards_v2` instead.

Rich, formatted, and interactive cards that you can use to display UI elements such as: formatted texts, buttons, and clickable images. Cards are normally displayed below the plain-text body of the message. `cards` and `cards_v2` can have a maximum size of 32 KB.

`repeated .google.chat.v1.ContextualAddOnMarkup.Card cards = 5 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContextualAddOnMarkup.CardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.CardOrBuilder)` |   
  
### getCardsOrBuilderList() (deprecated)
    
    
    public abstract List<? extends ContextualAddOnMarkup.CardOrBuilder> getCardsOrBuilderList()

Deprecated: Use `cards_v2` instead.

Rich, formatted, and interactive cards that you can use to display UI elements such as: formatted texts, buttons, and clickable images. Cards are normally displayed below the plain-text body of the message. `cards` and `cards_v2` can have a maximum size of 32 KB.

`repeated .google.chat.v1.ContextualAddOnMarkup.Card cards = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.ContextualAddOnMarkup.CardOrBuilder>` |   
  
### getCardsV2(int index)
    
    
    public abstract CardWithId getCardsV2(int index)

Optional. An array of [cards](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards).

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

` repeated .google.chat.v1.CardWithId cards_v2 = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CardWithId](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithId)` |   
  
### getCardsV2Count()
    
    
    public abstract int getCardsV2Count()

Optional. An array of [cards](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards).

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

` repeated .google.chat.v1.CardWithId cards_v2 = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCardsV2List()
    
    
    public abstract List<CardWithId> getCardsV2List()

Optional. An array of [cards](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards).

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

` repeated .google.chat.v1.CardWithId cards_v2 = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CardWithId](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithId)>` |   
  
### getCardsV2OrBuilder(int index)
    
    
    public abstract CardWithIdOrBuilder getCardsV2OrBuilder(int index)

Optional. An array of [cards](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards).

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

` repeated .google.chat.v1.CardWithId cards_v2 = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CardWithIdOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithIdOrBuilder)` |   
  
### getCardsV2OrBuilderList()
    
    
    public abstract List<? extends CardWithIdOrBuilder> getCardsV2OrBuilderList()

Optional. An array of [cards](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards).

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

` repeated .google.chat.v1.CardWithId cards_v2 = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.CardWithIdOrBuilder>` |   
  
### getClientAssignedMessageId()
    
    
    public abstract String getClientAssignedMessageId()

Optional. A custom ID for the message. You can use field to identify a message, or to get, delete, or update a message. To set a custom ID, specify the [`messageId`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create#body.QUERY_PARAMETERS.message_id) field when you create the message. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).

`string client_assigned_message_id = 32 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientAssignedMessageId.  
  
### getClientAssignedMessageIdBytes()
    
    
    public abstract ByteString getClientAssignedMessageIdBytes()

Optional. A custom ID for the message. You can use field to identify a message, or to get, delete, or update a message. To set a custom ID, specify the [`messageId`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create#body.QUERY_PARAMETERS.message_id) field when you create the message. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).

`string client_assigned_message_id = 32 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientAssignedMessageId.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Optional. Immutable. For spaces created in Chat, the time at which the message was created. This field is output only, except when used in import mode spaces.

For import mode spaces, set this field to the historical timestamp at which the message was created in the source in order to preserve the original creation time.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Optional. Immutable. For spaces created in Chat, the time at which the message was created. This field is output only, except when used in import mode spaces.

For import mode spaces, set this field to the historical timestamp at which the message was created in the source in order to preserve the original creation time.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDeleteTime()
    
    
    public abstract Timestamp getDeleteTime()

Output only. The time at which the message was deleted in Google Chat. If the message is never deleted, this field is empty.

`.google.protobuf.Timestamp delete_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. The time at which the message was deleted in Google Chat. If the message is never deleted, this field is empty.

`.google.protobuf.Timestamp delete_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDeletionMetadata()
    
    
    public abstract DeletionMetadata getDeletionMetadata()

Output only. Information about a deleted message. A message is deleted when `delete_time` is set.

` .google.chat.v1.DeletionMetadata deletion_metadata = 38 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DeletionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadata)` | The deletionMetadata.  
  
### getDeletionMetadataOrBuilder()
    
    
    public abstract DeletionMetadataOrBuilder getDeletionMetadataOrBuilder()

Output only. Information about a deleted message. A message is deleted when `delete_time` is set.

` .google.chat.v1.DeletionMetadata deletion_metadata = 38 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DeletionMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadataOrBuilder)` |   
  
### getEmojiReactionSummaries(int index)
    
    
    public abstract EmojiReactionSummary getEmojiReactionSummaries(int index)

Output only. The list of emoji reaction summaries on the message.

` repeated .google.chat.v1.EmojiReactionSummary emoji_reaction_summaries = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EmojiReactionSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummary)` |   
  
### getEmojiReactionSummariesCount()
    
    
    public abstract int getEmojiReactionSummariesCount()

Output only. The list of emoji reaction summaries on the message.

` repeated .google.chat.v1.EmojiReactionSummary emoji_reaction_summaries = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEmojiReactionSummariesList()
    
    
    public abstract List<EmojiReactionSummary> getEmojiReactionSummariesList()

Output only. The list of emoji reaction summaries on the message.

` repeated .google.chat.v1.EmojiReactionSummary emoji_reaction_summaries = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EmojiReactionSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummary)>` |   
  
### getEmojiReactionSummariesOrBuilder(int index)
    
    
    public abstract EmojiReactionSummaryOrBuilder getEmojiReactionSummariesOrBuilder(int index)

Output only. The list of emoji reaction summaries on the message.

` repeated .google.chat.v1.EmojiReactionSummary emoji_reaction_summaries = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EmojiReactionSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummaryOrBuilder)` |   
  
### getEmojiReactionSummariesOrBuilderList()
    
    
    public abstract List<? extends EmojiReactionSummaryOrBuilder> getEmojiReactionSummariesOrBuilderList()

Output only. The list of emoji reaction summaries on the message.

` repeated .google.chat.v1.EmojiReactionSummary emoji_reaction_summaries = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.chat.v1.EmojiReactionSummaryOrBuilder>` |   
  
### getFallbackText()
    
    
    public abstract String getFallbackText()

Optional. A plain-text description of the message's cards, used when the actual cards can't be displayed—for example, mobile notifications.

`string fallback_text = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fallbackText.  
  
### getFallbackTextBytes()
    
    
    public abstract ByteString getFallbackTextBytes()

Optional. A plain-text description of the message's cards, used when the actual cards can't be displayed—for example, mobile notifications.

`string fallback_text = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fallbackText.  
  
### getFormattedText()
    
    
    public abstract String getFormattedText()

Output only. Contains the message `text` with markups added to communicate formatting. This field might not capture all formatting visible in the UI, but includes the following:

  * [Markup syntax](https://developers.google.com/workspace/chat/format-messages) for bold, italic, strikethrough, monospace, monospace block, bulleted list, and block quote.

  * [User mentions](https://developers.google.com/workspace/chat/format-messages#messages-@mention) using the format `<users/{user}>`.

  * Custom hyperlinks using the format `<{url}|{rendered_text}>` where the first string is the URL and the second is the rendered text—for example, `<http://example.com|custom text>`.

  * Custom emoji using the format `:{emoji_name}:`—for example, `😄`. This doesn't apply to Unicode emoji, such as `U+1F600` for a grinning face emoji.

  * Bullet list items using asterisks (`__`)—for example,` item`.

For more information, see [View text formatting sent in a message](https://developers.google.com/workspace/chat/format-messages#view_text_formatting_sent_in_a_message)




`string formatted_text = 43 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The formattedText.  
  
### getFormattedTextBytes()
    
    
    public abstract ByteString getFormattedTextBytes()

Output only. Contains the message `text` with markups added to communicate formatting. This field might not capture all formatting visible in the UI, but includes the following:

  * [Markup syntax](https://developers.google.com/workspace/chat/format-messages) for bold, italic, strikethrough, monospace, monospace block, bulleted list, and block quote.

  * [User mentions](https://developers.google.com/workspace/chat/format-messages#messages-@mention) using the format `<users/{user}>`.

  * Custom hyperlinks using the format `<{url}|{rendered_text}>` where the first string is the URL and the second is the rendered text—for example, `<http://example.com|custom text>`.

  * Custom emoji using the format `:{emoji_name}:`—for example, `😄`. This doesn't apply to Unicode emoji, such as `U+1F600` for a grinning face emoji.

  * Bullet list items using asterisks (`__`)—for example,` item`.

For more information, see [View text formatting sent in a message](https://developers.google.com/workspace/chat/format-messages#view_text_formatting_sent_in_a_message)




`string formatted_text = 43 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for formattedText.  
  
### getLastUpdateTime()
    
    
    public abstract Timestamp getLastUpdateTime()

Output only. The time at which the message was last edited by a user. If the message has never been edited, this field is empty.

` .google.protobuf.Timestamp last_update_time = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastUpdateTime.  
  
### getLastUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastUpdateTimeOrBuilder()

Output only. The time at which the message was last edited by a user. If the message has never been edited, this field is empty.

` .google.protobuf.Timestamp last_update_time = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMarkupSyntax()
    
    
    public abstract MarkupSyntax getMarkupSyntax()

Optional. Specifies how the server interprets the message `text` field content.

` .google.chat.v1.MarkupSyntax markup_syntax = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MarkupSyntax](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkupSyntax)` | The markupSyntax.  
  
### getMarkupSyntaxValue()
    
    
    public abstract int getMarkupSyntaxValue()

Optional. Specifies how the server interprets the message `text` field content.

` .google.chat.v1.MarkupSyntax markup_syntax = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for markupSyntax.  
  
### getMatchedUrl()
    
    
    public abstract MatchedUrl getMatchedUrl()

Output only. A URL in the Chat message `text` field that matches a link preview pattern. For more information, see [Preview links](https://developers.google.com/workspace/chat/preview-links).

`.google.chat.v1.MatchedUrl matched_url = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MatchedUrl](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrl)` | The matchedUrl.  
  
### getMatchedUrlOrBuilder()
    
    
    public abstract MatchedUrlOrBuilder getMatchedUrlOrBuilder()

Output only. A URL in the Chat message `text` field that matches a link preview pattern. For more information, see [Preview links](https://developers.google.com/workspace/chat/preview-links).

`.google.chat.v1.MatchedUrl matched_url = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MatchedUrlOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrlOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. Resource name of the message.

Format: `spaces/{space}/messages/{message}`

Where `{space}` is the ID of the space where the message is posted and `{message}` is a system-assigned ID for the message. For example, `spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB`.

If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing `{message}` with the value from the `clientAssignedMessageId` field. For example, `spaces/AAAAAAAAAAA/messages/client-custom-name`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Resource name of the message.

Format: `spaces/{space}/messages/{message}`

Where `{space}` is the ID of the space where the message is posted and `{message}` is a system-assigned ID for the message. For example, `spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB`.

If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing `{message}` with the value from the `clientAssignedMessageId` field. For example, `spaces/AAAAAAAAAAA/messages/client-custom-name`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrivateMessageViewer()
    
    
    public abstract User getPrivateMessageViewer()

Optional. Immutable. Input for creating a message, otherwise output only. The user that can view the message. When set, the message is private and only visible to the specified user and the Chat app. To include this field in your request, you must call the Chat API using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) and omit the following:

  * [Attachments](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments)

For details, see [Send a message privately](https://developers.google.com/workspace/chat/create-messages#private).




` .google.chat.v1.User private_message_viewer = 36 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.User)` | The privateMessageViewer.  
  
### getPrivateMessageViewerOrBuilder()
    
    
    public abstract UserOrBuilder getPrivateMessageViewerOrBuilder()

Optional. Immutable. Input for creating a message, otherwise output only. The user that can view the message. When set, the message is private and only visible to the specified user and the Chat app. To include this field in your request, you must call the Chat API using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) and omit the following:

  * [Attachments](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments)

For details, see [Send a message privately](https://developers.google.com/workspace/chat/create-messages#private).




` .google.chat.v1.User private_message_viewer = 36 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[UserOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserOrBuilder)` |   
  
### getQuotedMessageMetadata()
    
    
    public abstract QuotedMessageMetadata getQuotedMessageMetadata()

Optional. Information about a message that another message quotes.

When you create a message, you can quote messages within the same thread, or quote a root message to create a new root message. However, you can't quote a message reply from a different thread.

When you update a message, you can't add or replace the `quotedMessageMetadata` field, but you can remove it.

For example usage, see [Quote another message](https://developers.google.com/workspace/chat/create-messages#quote-a-message).

` .google.chat.v1.QuotedMessageMetadata quoted_message_metadata = 39 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotedMessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadata)` | The quotedMessageMetadata.  
  
### getQuotedMessageMetadataOrBuilder()
    
    
    public abstract QuotedMessageMetadataOrBuilder getQuotedMessageMetadataOrBuilder()

Optional. Information about a message that another message quotes.

When you create a message, you can quote messages within the same thread, or quote a root message to create a new root message. However, you can't quote a message reply from a different thread.

When you update a message, you can't add or replace the `quotedMessageMetadata` field, but you can remove it.

For example usage, see [Quote another message](https://developers.google.com/workspace/chat/create-messages#quote-a-message).

` .google.chat.v1.QuotedMessageMetadata quoted_message_metadata = 39 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotedMessageMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadataOrBuilder)` |   
  
### getSender()
    
    
    public abstract User getSender()

Output only. The user who created the message. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User) `name` and `type` fields for both internal and external users, unless they are members of the space or have a prior affinity, like a direct message (DM) conversation, with the calling user.

`.google.chat.v1.User sender = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.User)` | The sender.  
  
### getSenderOrBuilder()
    
    
    public abstract UserOrBuilder getSenderOrBuilder()

Output only. The user who created the message. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User) `name` and `type` fields for both internal and external users, unless they are members of the space or have a prior affinity, like a direct message (DM) conversation, with the calling user.

`.google.chat.v1.User sender = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[UserOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserOrBuilder)` |   
  
### getSilent()
    
    
    public abstract boolean getSilent()

Output only. Whether this is a silent message. Silent messages are messages where Chat suppresses push notifications for recipients.

`bool silent = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The silent.  
  
### getSlashCommand()
    
    
    public abstract SlashCommand getSlashCommand()

Output only. Slash command information, if applicable.

` .google.chat.v1.SlashCommand slash_command = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SlashCommand](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommand)` | The slashCommand.  
  
### getSlashCommandOrBuilder()
    
    
    public abstract SlashCommandOrBuilder getSlashCommandOrBuilder()

Output only. Slash command information, if applicable.

` .google.chat.v1.SlashCommand slash_command = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SlashCommandOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandOrBuilder)` |   
  
### getSpace()
    
    
    public abstract Space getSpace()

Output only. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) `name`.

`.google.chat.v1.Space space = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` | The space.  
  
### getSpaceOrBuilder()
    
    
    public abstract SpaceOrBuilder getSpaceOrBuilder()

Output only. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) `name`.

`.google.chat.v1.Space space = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[SpaceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceOrBuilder)` |   
  
### getText()
    
    
    public abstract String getText()

Optional. Plain-text body of the message. The first link to an image, video, or web page generates a [preview chip](https://developers.google.com/workspace/chat/preview-links). You can also [@mention a Google Chat user](https://developers.google.com/workspace/chat/format-messages#messages-@mention), or everyone in the space.

To learn about creating text messages, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

`string text = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public abstract ByteString getTextBytes()

Optional. Plain-text body of the message. The first link to an image, video, or web page generates a [preview chip](https://developers.google.com/workspace/chat/preview-links). You can also [@mention a Google Chat user](https://developers.google.com/workspace/chat/format-messages#messages-@mention), or everyone in the space.

To learn about creating text messages, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

`string text = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getThread()
    
    
    public abstract Thread getThread()

The thread the message belongs to. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).

`.google.chat.v1.Thread thread = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Thread](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Thread)` | The thread.  
  
### getThreadOrBuilder()
    
    
    public abstract ThreadOrBuilder getThreadOrBuilder()

The thread the message belongs to. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).

`.google.chat.v1.Thread thread = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ThreadOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadOrBuilder)` |   
  
### getThreadReply()
    
    
    public abstract boolean getThreadReply()

Output only. When `true`, the message is a response in a reply thread. When `false`, the message is visible in the space's top-level conversation as either the first message of a thread or a message with no threaded replies.

If the space doesn't support reply in threads, this field is always `false`.

`bool thread_reply = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The threadReply.  
  
### hasActionResponse()
    
    
    public abstract boolean hasActionResponse()

Input only. Parameters that a Chat app can use to configure how its response is posted.

` .google.chat.v1.ActionResponse action_response = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the actionResponse field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Optional. Immutable. For spaces created in Chat, the time at which the message was created. This field is output only, except when used in import mode spaces.

For import mode spaces, set this field to the historical timestamp at which the message was created in the source in order to preserve the original creation time.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeleteTime()
    
    
    public abstract boolean hasDeleteTime()

Output only. The time at which the message was deleted in Google Chat. If the message is never deleted, this field is empty.

`.google.protobuf.Timestamp delete_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasDeletionMetadata()
    
    
    public abstract boolean hasDeletionMetadata()

Output only. Information about a deleted message. A message is deleted when `delete_time` is set.

` .google.chat.v1.DeletionMetadata deletion_metadata = 38 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deletionMetadata field is set.  
  
### hasLastUpdateTime()
    
    
    public abstract boolean hasLastUpdateTime()

Output only. The time at which the message was last edited by a user. If the message has never been edited, this field is empty.

` .google.protobuf.Timestamp last_update_time = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastUpdateTime field is set.  
  
### hasMatchedUrl()
    
    
    public abstract boolean hasMatchedUrl()

Output only. A URL in the Chat message `text` field that matches a link preview pattern. For more information, see [Preview links](https://developers.google.com/workspace/chat/preview-links).

`.google.chat.v1.MatchedUrl matched_url = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the matchedUrl field is set.  
  
### hasPrivateMessageViewer()
    
    
    public abstract boolean hasPrivateMessageViewer()

Optional. Immutable. Input for creating a message, otherwise output only. The user that can view the message. When set, the message is private and only visible to the specified user and the Chat app. To include this field in your request, you must call the Chat API using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) and omit the following:

  * [Attachments](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments)

For details, see [Send a message privately](https://developers.google.com/workspace/chat/create-messages#private).




` .google.chat.v1.User private_message_viewer = 36 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateMessageViewer field is set.  
  
### hasQuotedMessageMetadata()
    
    
    public abstract boolean hasQuotedMessageMetadata()

Optional. Information about a message that another message quotes.

When you create a message, you can quote messages within the same thread, or quote a root message to create a new root message. However, you can't quote a message reply from a different thread.

When you update a message, you can't add or replace the `quotedMessageMetadata` field, but you can remove it.

For example usage, see [Quote another message](https://developers.google.com/workspace/chat/create-messages#quote-a-message).

` .google.chat.v1.QuotedMessageMetadata quoted_message_metadata = 39 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quotedMessageMetadata field is set.  
  
### hasSender()
    
    
    public abstract boolean hasSender()

Output only. The user who created the message. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User) `name` and `type` fields for both internal and external users, unless they are members of the space or have a prior affinity, like a direct message (DM) conversation, with the calling user.

`.google.chat.v1.User sender = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sender field is set.  
  
### hasSlashCommand()
    
    
    public abstract boolean hasSlashCommand()

Output only. Slash command information, if applicable.

` .google.chat.v1.SlashCommand slash_command = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the slashCommand field is set.  
  
### hasSpace()
    
    
    public abstract boolean hasSpace()

Output only. If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output only populates the [space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) `name`.

`.google.chat.v1.Space space = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the space field is set.  
  
### hasThread()
    
    
    public abstract boolean hasThread()

The thread the message belongs to. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).

`.google.chat.v1.Thread thread = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the thread field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
