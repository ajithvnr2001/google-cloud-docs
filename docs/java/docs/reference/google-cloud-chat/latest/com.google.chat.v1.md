---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1
title: Package com.google.chat.v1 (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:54.193009+00:00
---

# Package com.google.chat.v1 (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.chat.v1 (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-chat/google-cloud-chat/src/main/java/com/google/chat/v1) | [REST Documentation](https://developers.google.com/chat/api/reference/rest)  
---|---  
  
## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.chat.v1.ChatServiceClient](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient) |  Service Description: Enables developers to build Chat apps and integrations on Google Chat Platform. This class provides the ability to make remote calls to the backing service through method  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.chat.v1.ChatServiceSettings](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceSettings) |  Settings class to configure an instance of ChatServiceClient. The default instance has everything set to sensible defaults:   
[com.google.chat.v1.Space.AccessPermissionSettings](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSettings) |  Access permission settings for a space.  
[com.google.chat.v1.Space.AccessSettings](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessSettings) |  Represents the [access setting](https://support.google.com/chat/answer/11971020) of the space.   
[com.google.chat.v1.Space.PermissionSettings](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings) |  [Permission settings](https://support.google.com/chat/answer/13340792) that you can specify when updating an existing named space.   
[com.google.chat.v1.Space.PredefinedPermissionSettings](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PredefinedPermissionSettings) |  Predefined permission settings that you can only specify when creating a named space. More settings might be added in the future. For details about permission settings for named spaces, see [Learn about](https://support.google.com/chat/answer/7659784)  
  
## Classes

Class |  Description  
---|---  
[com.google.chat.v1.AccessoryWidget](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidget) |  One or more interactive widgets that appear at the bottom of a message. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).  
[com.google.chat.v1.AccessoryWidget.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidget.Builder) |  One or more interactive widgets that appear at the bottom of a message. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).  
[com.google.chat.v1.ActionResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse) |  Parameters that a Chat app can use to configure how its response is posted.   
[com.google.chat.v1.ActionResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.Builder) |  Parameters that a Chat app can use to configure how its response is posted.   
[com.google.chat.v1.ActionResponse.SelectionItems](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.SelectionItems) |  List of widget autocomplete results.   
[com.google.chat.v1.ActionResponse.SelectionItems.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.SelectionItems.Builder) |  List of widget autocomplete results.   
[com.google.chat.v1.ActionResponse.UpdatedWidget](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.UpdatedWidget) |  For `selectionInput` widgets, returns autocomplete suggestions for a multiselect menu.   
[com.google.chat.v1.ActionResponse.UpdatedWidget.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.UpdatedWidget.Builder) |  For `selectionInput` widgets, returns autocomplete suggestions for a multiselect menu.   
[com.google.chat.v1.ActionStatus](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionStatus) |  Represents the status for a request to either invoke or submit a [dialog](https://developers.google.com/workspace/chat/dialogs).   
[com.google.chat.v1.ActionStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionStatus.Builder) |  Represents the status for a request to either invoke or submit a [dialog](https://developers.google.com/workspace/chat/dialogs).   
[com.google.chat.v1.ActionStatusProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionStatusProto) |   
[com.google.chat.v1.Annotation](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation) |  Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0. To add basic formatting to a text  
[com.google.chat.v1.Annotation.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder) |  Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0. To add basic formatting to a text  
[com.google.chat.v1.AnnotationProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationProto) |   
[com.google.chat.v1.AppCommandMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AppCommandMetadata) |  Metadata about a [Chat app command](https://developers.google.com/workspace/chat/commands).   
[com.google.chat.v1.AppCommandMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AppCommandMetadata.Builder) |  Metadata about a [Chat app command](https://developers.google.com/workspace/chat/commands).   
[com.google.chat.v1.AppCommandMetadataProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AppCommandMetadataProto) |   
[com.google.chat.v1.AttachedGif](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGif) |  A GIF image that's specified by a URL.   
[com.google.chat.v1.AttachedGif.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGif.Builder) |  A GIF image that's specified by a URL.   
[com.google.chat.v1.Attachment](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment) |  An attachment in Google Chat.   
[com.google.chat.v1.Attachment.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment.Builder) |  An attachment in Google Chat.   
[com.google.chat.v1.AttachmentDataRef](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentDataRef) |  A reference to the attachment data.   
[com.google.chat.v1.AttachmentDataRef.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentDataRef.Builder) |  A reference to the attachment data.   
[com.google.chat.v1.AttachmentName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentName) |   
[com.google.chat.v1.AttachmentName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentName.Builder) |  Builder for spaces/{space}/messages/{message}/attachments/{attachment}.  
[com.google.chat.v1.AttachmentProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentProto) |   
[com.google.chat.v1.Audience](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Audience) |  A target audience in Google Chat. A target audience represents a group of users within a Google Workspace organization, defined by an administrator. Target audiences are used to configure access and visibility settings for  
[com.google.chat.v1.Audience.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Audience.Builder) |  A target audience in Google Chat. A target audience represents a group of users within a Google Workspace organization, defined by an administrator. Target audiences are used to configure access and visibility settings for  
[com.google.chat.v1.AudienceProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AudienceProto) |   
[com.google.chat.v1.Availability](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability) |  Represents a user's current availability information in Google Chat, including their state (for example, Active, Away, Do Not Disturb) and any custom status.  
[com.google.chat.v1.Availability.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability.Builder) |  Represents a user's current availability information in Google Chat, including their state (for example, Active, Away, Do Not Disturb) and any custom status.  
[com.google.chat.v1.AvailabilityName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AvailabilityName) |   
[com.google.chat.v1.AvailabilityName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AvailabilityName.Builder) |  Builder for users/{user}/availability.  
[com.google.chat.v1.AvailabilityProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AvailabilityProto) |   
[com.google.chat.v1.CalendarEventLinkData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CalendarEventLinkData) |  Data for Calendar event links.   
[com.google.chat.v1.CalendarEventLinkData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CalendarEventLinkData.Builder) |  Data for Calendar event links.   
[com.google.chat.v1.CardWithId](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithId) |  A [card](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards) in a Google Chat message.  
[com.google.chat.v1.CardWithId.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithId.Builder) |  A [card](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards) in a Google Chat message.  
[com.google.chat.v1.ChatServiceClient.FindGroupChatsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.FindGroupChatsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsPage) |   
[com.google.chat.v1.ChatServiceClient.FindGroupChatsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListCustomEmojisFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListCustomEmojisPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPage) |   
[com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListMembershipsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListMembershipsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPage) |   
[com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListMessagePinsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListMessagePinsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPage) |   
[com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListMessagesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListMessagesPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPage) |   
[com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListReactionsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListReactionsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPage) |   
[com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListSectionItemsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListSectionItemsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPage) |   
[com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListSectionsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListSectionsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPage) |   
[com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListSpaceEventsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListSpaceEventsPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPage) |   
[com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.ListSpacesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.ListSpacesPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPage) |   
[com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.SearchMessagesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.SearchMessagesPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPage) |   
[com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse) |   
[com.google.chat.v1.ChatServiceClient.SearchSpacesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesFixedSizeCollection) |   
[com.google.chat.v1.ChatServiceClient.SearchSpacesPage](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPage) |   
[com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse) |   
[com.google.chat.v1.ChatServiceGrpc](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc) |  Enables developers to build Chat apps and integrations on Google Chat Platform.   
[com.google.chat.v1.ChatServiceGrpc.ChatServiceImplBase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc.ChatServiceImplBase) |  Base class for the server implementation of the service ChatService. Enables developers to build Chat apps and  
[com.google.chat.v1.ChatServiceProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceProto) |   
[com.google.chat.v1.ChatServiceSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceSettings.Builder) |  Builder for ChatServiceSettings.  
[com.google.chat.v1.ChatSpaceLinkData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatSpaceLinkData) |  Data for Chat space links.   
[com.google.chat.v1.ChatSpaceLinkData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatSpaceLinkData.Builder) |  Data for Chat space links.   
[com.google.chat.v1.CompleteImportSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest) |  Request message for completing the import process for a space.   
[com.google.chat.v1.CompleteImportSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest.Builder) |  Request message for completing the import process for a space.   
[com.google.chat.v1.CompleteImportSpaceResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse) |  Response message for completing the import process for a space.   
[com.google.chat.v1.CompleteImportSpaceResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse.Builder) |  Response message for completing the import process for a space.   
[com.google.chat.v1.ContextualAddOnMarkup](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup) |  The markup for developers to specify the contents of a contextual AddOn.   
[com.google.chat.v1.ContextualAddOnMarkup.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Builder) |  The markup for developers to specify the contents of a contextual AddOn.   
[com.google.chat.v1.ContextualAddOnMarkup.Card](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card) |  A card is a UI element that can contain UI widgets such as text and images.   
[com.google.chat.v1.ContextualAddOnMarkup.Card.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.Builder) |  A card is a UI element that can contain UI widgets such as text and images.   
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardAction](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardAction) |  A card action is the action associated with the card. For an invoice card, a typical action would be: delete invoice, email invoice or open the  
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardAction.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardAction.Builder) |  A card action is the action associated with the card. For an invoice card, a typical action would be: delete invoice, email invoice or open the  
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader) |  Protobuf type `google.chat.v1.ContextualAddOnMarkup.Card.CardHeader`  
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.Builder) |  Protobuf type `google.chat.v1.ContextualAddOnMarkup.Card.CardHeader`  
[com.google.chat.v1.ContextualAddOnMarkup.Card.Section](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.Section) |  A section contains a collection of widgets that are rendered (vertically) in the order that they are specified. Across all platforms, cards have a narrow fixed width, so  
[com.google.chat.v1.ContextualAddOnMarkup.Card.Section.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.Section.Builder) |  A section contains a collection of widgets that are rendered (vertically) in the order that they are specified. Across all platforms, cards have a narrow fixed width, so  
[com.google.chat.v1.ContextualAddOnProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnProto) |   
[com.google.chat.v1.CreateCustomEmojiRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest) |  A request to create a custom emoji.   
[com.google.chat.v1.CreateCustomEmojiRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest.Builder) |  A request to create a custom emoji.   
[com.google.chat.v1.CreateMembershipRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest) |  Request message for creating a membership.   
[com.google.chat.v1.CreateMembershipRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest.Builder) |  Request message for creating a membership.   
[com.google.chat.v1.CreateMessageNotificationOptions](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageNotificationOptions) |  Options for the notification behavior when the message is posted.   
[com.google.chat.v1.CreateMessageNotificationOptions.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageNotificationOptions.Builder) |  Options for the notification behavior when the message is posted.   
[com.google.chat.v1.CreateMessagePinRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest) |  Request message for creating a message pin.   
[com.google.chat.v1.CreateMessagePinRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest.Builder) |  Request message for creating a message pin.   
[com.google.chat.v1.CreateMessageRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest) |  Creates a message.   
[com.google.chat.v1.CreateMessageRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest.Builder) |  Creates a message.   
[com.google.chat.v1.CreateReactionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest) |  Creates a reaction to a message.   
[com.google.chat.v1.CreateReactionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest.Builder) |  Creates a reaction to a message.   
[com.google.chat.v1.CreateSectionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest) |  Request message for creating a section.   
[com.google.chat.v1.CreateSectionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest.Builder) |  Request message for creating a section.   
[com.google.chat.v1.CreateSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest) |  A request to create a named space with no members.   
[com.google.chat.v1.CreateSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest.Builder) |  A request to create a named space with no members.   
[com.google.chat.v1.CustomEmoji](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji) |  Represents a [custom emoji](https://support.google.com/chat/answer/12800149).   
[com.google.chat.v1.CustomEmoji.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji.Builder) |  Represents a [custom emoji](https://support.google.com/chat/answer/12800149).   
[com.google.chat.v1.CustomEmoji.CustomEmojiPayload](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji.CustomEmojiPayload) |  Payload data for the custom emoji.   
[com.google.chat.v1.CustomEmoji.CustomEmojiPayload.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji.CustomEmojiPayload.Builder) |  Payload data for the custom emoji.   
[com.google.chat.v1.CustomEmojiMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata) |  Annotation metadata for custom emoji.   
[com.google.chat.v1.CustomEmojiMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata.Builder) |  Annotation metadata for custom emoji.   
[com.google.chat.v1.CustomEmojiName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiName) |   
[com.google.chat.v1.CustomEmojiName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiName.Builder) |  Builder for customEmojis/{custom_emoji}.  
[com.google.chat.v1.CustomStatus](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomStatus) |  Represents a user's custom status in Google Chat. This includes a short text message with an optional emoji that a user sets to give more context about their availability.  
[com.google.chat.v1.CustomStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomStatus.Builder) |  Represents a user's custom status in Google Chat. This includes a short text message with an optional emoji that a user sets to give more context about their availability.  
[com.google.chat.v1.DeleteCustomEmojiRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest) |  Request for deleting a custom emoji.   
[com.google.chat.v1.DeleteCustomEmojiRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest.Builder) |  Request for deleting a custom emoji.   
[com.google.chat.v1.DeleteMembershipRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest) |  Request to delete a membership in a space.   
[com.google.chat.v1.DeleteMembershipRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest.Builder) |  Request to delete a membership in a space.   
[com.google.chat.v1.DeleteMessagePinRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest) |  Request message for deleting a message pin.   
[com.google.chat.v1.DeleteMessagePinRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest.Builder) |  Request message for deleting a message pin.   
[com.google.chat.v1.DeleteMessageRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest) |  Request to delete a message.   
[com.google.chat.v1.DeleteMessageRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest.Builder) |  Request to delete a message.   
[com.google.chat.v1.DeleteReactionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest) |  Deletes a reaction to a message.   
[com.google.chat.v1.DeleteReactionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest.Builder) |  Deletes a reaction to a message.   
[com.google.chat.v1.DeleteSectionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest) |  Request message for deleting a section. [Developer Preview](https://developers.google.com/workspace/preview).   
[com.google.chat.v1.DeleteSectionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest.Builder) |  Request message for deleting a section. [Developer Preview](https://developers.google.com/workspace/preview).   
[com.google.chat.v1.DeleteSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest) |  Request for deleting a space.   
[com.google.chat.v1.DeleteSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest.Builder) |  Request for deleting a space.   
[com.google.chat.v1.DeletionMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadata) |  Information about a deleted message. A message is deleted when `delete_time` is set.   
[com.google.chat.v1.DeletionMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadata.Builder) |  Information about a deleted message. A message is deleted when `delete_time` is set.   
[com.google.chat.v1.DeletionMetadataProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadataProto) |   
[com.google.chat.v1.Dialog](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Dialog) |  Wrapper around the card body of the dialog.   
[com.google.chat.v1.Dialog.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Dialog.Builder) |  Wrapper around the card body of the dialog.   
[com.google.chat.v1.DialogAction](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DialogAction) |  Contains a [dialog](https://developers.google.com/workspace/chat/dialogs) and request status code.  
[com.google.chat.v1.DialogAction.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DialogAction.Builder) |  Contains a [dialog](https://developers.google.com/workspace/chat/dialogs) and request status code.  
[com.google.chat.v1.DoNotDisturbMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DoNotDisturbMetadata) |  Metadata associated with the `DO_NOT_DISTURB` availability state, specifying when the state is set to expire.   
[com.google.chat.v1.DoNotDisturbMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DoNotDisturbMetadata.Builder) |  Metadata associated with the `DO_NOT_DISTURB` availability state, specifying when the state is set to expire.   
[com.google.chat.v1.DriveDataRef](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveDataRef) |  A reference to the data of a drive attachment.   
[com.google.chat.v1.DriveDataRef.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveDataRef.Builder) |  A reference to the data of a drive attachment.   
[com.google.chat.v1.DriveLinkData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveLinkData) |  Data for Google Drive links.   
[com.google.chat.v1.DriveLinkData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveLinkData.Builder) |  Data for Google Drive links.   
[com.google.chat.v1.Emoji](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Emoji) |  An emoji that is used as a reaction to a message.   
[com.google.chat.v1.Emoji.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Emoji.Builder) |  An emoji that is used as a reaction to a message.   
[com.google.chat.v1.EmojiReactionSummary](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummary) |  The number of people who reacted to a message with a specific emoji.   
[com.google.chat.v1.EmojiReactionSummary.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummary.Builder) |  The number of people who reacted to a message with a specific emoji.   
[com.google.chat.v1.EventPayloadProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EventPayloadProto) |   
[com.google.chat.v1.FindDirectMessageRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest) |  A request to get direct message space based on the user resource.   
[com.google.chat.v1.FindDirectMessageRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest.Builder) |  A request to get direct message space based on the user resource.   
[com.google.chat.v1.FindGroupChatsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest) |  A request to get group chat spaces based on user resources.   
[com.google.chat.v1.FindGroupChatsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest.Builder) |  A request to get group chat spaces based on user resources.   
[com.google.chat.v1.FindGroupChatsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponse) |  A response containing group chat spaces with exactly the calling user and the requested users.   
[com.google.chat.v1.FindGroupChatsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponse.Builder) |  A response containing group chat spaces with exactly the calling user and the requested users.   
[com.google.chat.v1.ForwardedMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ForwardedMetadata) |  Metadata about the source space from which a message was forwarded.   
[com.google.chat.v1.ForwardedMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ForwardedMetadata.Builder) |  Metadata about the source space from which a message was forwarded.   
[com.google.chat.v1.GetAttachmentRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest) |  Request to get an attachment.   
[com.google.chat.v1.GetAttachmentRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest.Builder) |  Request to get an attachment.   
[com.google.chat.v1.GetAvailabilityRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest) |  Request message for the `GetAvailability` method.   
[com.google.chat.v1.GetAvailabilityRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest.Builder) |  Request message for the `GetAvailability` method.   
[com.google.chat.v1.GetCustomEmojiRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest) |  A request to return a single custom emoji.   
[com.google.chat.v1.GetCustomEmojiRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest.Builder) |  A request to return a single custom emoji.   
[com.google.chat.v1.GetMembershipRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest) |  Request to get a membership of a space.   
[com.google.chat.v1.GetMembershipRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest.Builder) |  Request to get a membership of a space.   
[com.google.chat.v1.GetMessageRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest) |  Request to get a message.   
[com.google.chat.v1.GetMessageRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest.Builder) |  Request to get a message.   
[com.google.chat.v1.GetSpaceEventRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest) |  Request message for getting a space event.   
[com.google.chat.v1.GetSpaceEventRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest.Builder) |  Request message for getting a space event.   
[com.google.chat.v1.GetSpaceNotificationSettingRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest) |  Request message to get space notification setting. Only supports getting notification setting for the calling user.   
[com.google.chat.v1.GetSpaceNotificationSettingRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest.Builder) |  Request message to get space notification setting. Only supports getting notification setting for the calling user.   
[com.google.chat.v1.GetSpaceReadStateRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest) |  Request message for GetSpaceReadState API.   
[com.google.chat.v1.GetSpaceReadStateRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest.Builder) |  Request message for GetSpaceReadState API.   
[com.google.chat.v1.GetSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest) |  A request to return a single space.   
[com.google.chat.v1.GetSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest.Builder) |  A request to return a single space.   
[com.google.chat.v1.GetThreadReadStateRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest) |  Request message for GetThreadReadStateRequest API.   
[com.google.chat.v1.GetThreadReadStateRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest.Builder) |  Request message for GetThreadReadStateRequest API.   
[com.google.chat.v1.Group](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Group) |  A Google Group in Google Chat.   
[com.google.chat.v1.Group.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Group.Builder) |  A Google Group in Google Chat.   
[com.google.chat.v1.GroupProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GroupProto) |   
[com.google.chat.v1.HistoryStateProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.HistoryStateProto) |   
[com.google.chat.v1.ListCustomEmojisRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest) |  A request to return a list of custom emojis.   
[com.google.chat.v1.ListCustomEmojisRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest.Builder) |  A request to return a list of custom emojis.   
[com.google.chat.v1.ListCustomEmojisResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponse) |  A response to list custom emojis.   
[com.google.chat.v1.ListCustomEmojisResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponse.Builder) |  A response to list custom emojis.   
[com.google.chat.v1.ListMembershipsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest) |  Request message for listing memberships.   
[com.google.chat.v1.ListMembershipsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest.Builder) |  Request message for listing memberships.   
[com.google.chat.v1.ListMembershipsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponse) |  Response to list memberships of the space.   
[com.google.chat.v1.ListMembershipsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponse.Builder) |  Response to list memberships of the space.   
[com.google.chat.v1.ListMessagePinsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest) |  Request message for listing message pins.   
[com.google.chat.v1.ListMessagePinsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest.Builder) |  Request message for listing message pins.   
[com.google.chat.v1.ListMessagePinsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponse) |  Response message for listing message pins.   
[com.google.chat.v1.ListMessagePinsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponse.Builder) |  Response message for listing message pins.   
[com.google.chat.v1.ListMessagesRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest) |  Lists messages in the specified space, that the user is a member of.   
[com.google.chat.v1.ListMessagesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest.Builder) |  Lists messages in the specified space, that the user is a member of.   
[com.google.chat.v1.ListMessagesResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponse) |  Response message for listing messages.   
[com.google.chat.v1.ListMessagesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponse.Builder) |  Response message for listing messages.   
[com.google.chat.v1.ListReactionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest) |  Lists reactions to a message.   
[com.google.chat.v1.ListReactionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest.Builder) |  Lists reactions to a message.   
[com.google.chat.v1.ListReactionsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponse) |  Response to a list reactions request.   
[com.google.chat.v1.ListReactionsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponse.Builder) |  Response to a list reactions request.   
[com.google.chat.v1.ListSectionItemsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest) |  Request message for listing section items.   
[com.google.chat.v1.ListSectionItemsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest.Builder) |  Request message for listing section items.   
[com.google.chat.v1.ListSectionItemsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponse) |  Response message for listing section items.   
[com.google.chat.v1.ListSectionItemsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponse.Builder) |  Response message for listing section items.   
[com.google.chat.v1.ListSectionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest) |  Request message for listing sections.   
[com.google.chat.v1.ListSectionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest.Builder) |  Request message for listing sections.   
[com.google.chat.v1.ListSectionsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponse) |  Response message for listing sections.   
[com.google.chat.v1.ListSectionsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponse.Builder) |  Response message for listing sections.   
[com.google.chat.v1.ListSpaceEventsRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest) |  Request message for listing space events.   
[com.google.chat.v1.ListSpaceEventsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest.Builder) |  Request message for listing space events.   
[com.google.chat.v1.ListSpaceEventsResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponse) |  Response message for listing space events.   
[com.google.chat.v1.ListSpaceEventsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponse.Builder) |  Response message for listing space events.   
[com.google.chat.v1.ListSpacesRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest) |  A request to list the spaces the caller is a member of.   
[com.google.chat.v1.ListSpacesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest.Builder) |  A request to list the spaces the caller is a member of.   
[com.google.chat.v1.ListSpacesResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponse) |  The response for a list spaces request.   
[com.google.chat.v1.ListSpacesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponse.Builder) |  The response for a list spaces request.   
[com.google.chat.v1.MarkAsActiveRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest) |  Request message for the `MarkAsActive` method.   
[com.google.chat.v1.MarkAsActiveRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest.Builder) |  Request message for the `MarkAsActive` method.   
[com.google.chat.v1.MarkAsAwayRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest) |  Request message for the `MarkAsAway` method.   
[com.google.chat.v1.MarkAsAwayRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest.Builder) |  Request message for the `MarkAsAway` method.   
[com.google.chat.v1.MarkAsDoNotDisturbRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest) |  Request message for the `MarkAsDoNotDisturb` method.   
[com.google.chat.v1.MarkAsDoNotDisturbRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest.Builder) |  Request message for the `MarkAsDoNotDisturb` method.   
[com.google.chat.v1.MarkupSyntaxProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkupSyntaxProto) |   
[com.google.chat.v1.MatchedUrl](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrl) |  A matched URL in a Chat message. Chat apps can preview matched URLs. For more information, see [Preview links](https://developers.google.com/chat/how-tos/preview-links).  
[com.google.chat.v1.MatchedUrl.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrl.Builder) |  A matched URL in a Chat message. Chat apps can preview matched URLs. For more information, see [Preview links](https://developers.google.com/chat/how-tos/preview-links).  
[com.google.chat.v1.MatchedUrlProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrlProto) |   
[com.google.chat.v1.MeetSpaceLinkData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MeetSpaceLinkData) |  Data for Meet space links.   
[com.google.chat.v1.MeetSpaceLinkData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MeetSpaceLinkData.Builder) |  Data for Meet space links.   
[com.google.chat.v1.Membership](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership) |  Represents a membership relation in Google Chat, such as whether a user or Chat app is invited to, part of, or absent from a space.   
[com.google.chat.v1.Membership.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership.Builder) |  Represents a membership relation in Google Chat, such as whether a user or Chat app is invited to, part of, or absent from a space.   
[com.google.chat.v1.MembershipBatchCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchCreatedEventData) |  Event payload for multiple new memberships. Event type: `google.workspace.chat.membership.v1.batchCreated`  
[com.google.chat.v1.MembershipBatchCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchCreatedEventData.Builder) |  Event payload for multiple new memberships. Event type: `google.workspace.chat.membership.v1.batchCreated`  
[com.google.chat.v1.MembershipBatchDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchDeletedEventData) |  Event payload for multiple deleted memberships. Event type: `google.workspace.chat.membership.v1.batchDeleted`  
[com.google.chat.v1.MembershipBatchDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchDeletedEventData.Builder) |  Event payload for multiple deleted memberships. Event type: `google.workspace.chat.membership.v1.batchDeleted`  
[com.google.chat.v1.MembershipBatchUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchUpdatedEventData) |  Event payload for multiple updated memberships. Event type: `google.workspace.chat.membership.v1.batchUpdated`  
[com.google.chat.v1.MembershipBatchUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchUpdatedEventData.Builder) |  Event payload for multiple updated memberships. Event type: `google.workspace.chat.membership.v1.batchUpdated`  
[com.google.chat.v1.MembershipCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipCreatedEventData) |  Event payload for a new membership. Event type: `google.workspace.chat.membership.v1.created`.  
[com.google.chat.v1.MembershipCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipCreatedEventData.Builder) |  Event payload for a new membership. Event type: `google.workspace.chat.membership.v1.created`.  
[com.google.chat.v1.MembershipDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipDeletedEventData) |  Event payload for a deleted membership. Event type: `google.workspace.chat.membership.v1.deleted`  
[com.google.chat.v1.MembershipDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipDeletedEventData.Builder) |  Event payload for a deleted membership. Event type: `google.workspace.chat.membership.v1.deleted`  
[com.google.chat.v1.MembershipName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipName) |   
[com.google.chat.v1.MembershipName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipName.Builder) |  Builder for spaces/{space}/members/{member}.  
[com.google.chat.v1.MembershipProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipProto) |   
[com.google.chat.v1.MembershipUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipUpdatedEventData) |  Event payload for an updated membership. Event type: `google.workspace.chat.membership.v1.updated`  
[com.google.chat.v1.MembershipUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipUpdatedEventData.Builder) |  Event payload for an updated membership. Event type: `google.workspace.chat.membership.v1.updated`  
[com.google.chat.v1.Message](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message) |  A message in a Google Chat space.   
[com.google.chat.v1.Message.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message.Builder) |  A message in a Google Chat space.   
[com.google.chat.v1.MessageBatchCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchCreatedEventData) |  Event payload for multiple new messages. Event type: `google.workspace.chat.message.v1.batchCreated`  
[com.google.chat.v1.MessageBatchCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchCreatedEventData.Builder) |  Event payload for multiple new messages. Event type: `google.workspace.chat.message.v1.batchCreated`  
[com.google.chat.v1.MessageBatchDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchDeletedEventData) |  Event payload for multiple deleted messages. Event type: `google.workspace.chat.message.v1.batchDeleted`  
[com.google.chat.v1.MessageBatchDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchDeletedEventData.Builder) |  Event payload for multiple deleted messages. Event type: `google.workspace.chat.message.v1.batchDeleted`  
[com.google.chat.v1.MessageBatchUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchUpdatedEventData) |  Event payload for multiple updated messages. Event type: `google.workspace.chat.message.v1.batchUpdated`  
[com.google.chat.v1.MessageBatchUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchUpdatedEventData.Builder) |  Event payload for multiple updated messages. Event type: `google.workspace.chat.message.v1.batchUpdated`  
[com.google.chat.v1.MessageCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageCreatedEventData) |  Event payload for a new message. Event type: `google.workspace.chat.message.v1.created`  
[com.google.chat.v1.MessageCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageCreatedEventData.Builder) |  Event payload for a new message. Event type: `google.workspace.chat.message.v1.created`  
[com.google.chat.v1.MessageDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageDeletedEventData) |  Event payload for a deleted message. Event type: `google.workspace.chat.message.v1.deleted`  
[com.google.chat.v1.MessageDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageDeletedEventData.Builder) |  Event payload for a deleted message. Event type: `google.workspace.chat.message.v1.deleted`  
[com.google.chat.v1.MessageName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageName) |   
[com.google.chat.v1.MessageName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageName.Builder) |  Builder for spaces/{space}/messages/{message}.  
[com.google.chat.v1.MessagePin](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin) |  A pin on a Chat message. For more information see [Pin a message](https://support.google.com/chat?p=chat-board-hc).   
[com.google.chat.v1.MessagePin.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin.Builder) |  A pin on a Chat message. For more information see [Pin a message](https://support.google.com/chat?p=chat-board-hc).   
[com.google.chat.v1.MessagePinName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePinName) |   
[com.google.chat.v1.MessagePinName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePinName.Builder) |  Builder for spaces/{space}/messagePins/{message_pin}.  
[com.google.chat.v1.MessagePinProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePinProto) |   
[com.google.chat.v1.MessageProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageProto) |   
[com.google.chat.v1.MessageUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageUpdatedEventData) |  Event payload for an updated message. Event type: `google.workspace.chat.message.v1.updated`  
[com.google.chat.v1.MessageUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageUpdatedEventData.Builder) |  Event payload for an updated message. Event type: `google.workspace.chat.message.v1.updated`  
[com.google.chat.v1.MoveSectionItemRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest) |  Request message for moving a section item across sections.   
[com.google.chat.v1.MoveSectionItemRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest.Builder) |  Request message for moving a section item across sections.   
[com.google.chat.v1.MoveSectionItemResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse) |  Response message for moving a section item.   
[com.google.chat.v1.MoveSectionItemResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse.Builder) |  Response message for moving a section item.   
[com.google.chat.v1.PositionSectionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest) |  Request message for positioning a section.   
[com.google.chat.v1.PositionSectionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest.Builder) |  Request message for positioning a section.   
[com.google.chat.v1.PositionSectionResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse) |  Response message for positioning a section.   
[com.google.chat.v1.PositionSectionResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse.Builder) |  Response message for positioning a section.   
[com.google.chat.v1.QuotedMessageMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadata) |  Information about a message that another message quotes. When you update a message, you can't add or replace the  
[com.google.chat.v1.QuotedMessageMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadata.Builder) |  Information about a message that another message quotes. When you update a message, you can't add or replace the  
[com.google.chat.v1.QuotedMessageSnapshot](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageSnapshot) |  Provides a snapshot of the content of the quoted message at the time of quoting or forwarding   
[com.google.chat.v1.QuotedMessageSnapshot.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageSnapshot.Builder) |  Provides a snapshot of the content of the quoted message at the time of quoting or forwarding   
[com.google.chat.v1.Reaction](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction) |  A reaction to a message.   
[com.google.chat.v1.Reaction.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction.Builder) |  A reaction to a message.   
[com.google.chat.v1.ReactionBatchCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchCreatedEventData) |  Event payload for multiple new reactions. Event type: `google.workspace.chat.reaction.v1.batchCreated`  
[com.google.chat.v1.ReactionBatchCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchCreatedEventData.Builder) |  Event payload for multiple new reactions. Event type: `google.workspace.chat.reaction.v1.batchCreated`  
[com.google.chat.v1.ReactionBatchDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchDeletedEventData) |  Event payload for multiple deleted reactions. Event type: `google.workspace.chat.reaction.v1.batchDeleted`  
[com.google.chat.v1.ReactionBatchDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchDeletedEventData.Builder) |  Event payload for multiple deleted reactions. Event type: `google.workspace.chat.reaction.v1.batchDeleted`  
[com.google.chat.v1.ReactionCreatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionCreatedEventData) |  Event payload for a new reaction. Event type: `google.workspace.chat.reaction.v1.created`  
[com.google.chat.v1.ReactionCreatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionCreatedEventData.Builder) |  Event payload for a new reaction. Event type: `google.workspace.chat.reaction.v1.created`  
[com.google.chat.v1.ReactionDeletedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionDeletedEventData) |  Event payload for a deleted reaction. Type: `google.workspace.chat.reaction.v1.deleted`  
[com.google.chat.v1.ReactionDeletedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionDeletedEventData.Builder) |  Event payload for a deleted reaction. Type: `google.workspace.chat.reaction.v1.deleted`  
[com.google.chat.v1.ReactionName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionName) |   
[com.google.chat.v1.ReactionName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionName.Builder) |  Builder for spaces/{space}/messages/{message}/reactions/{reaction}.  
[com.google.chat.v1.ReactionProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionProto) |   
[com.google.chat.v1.RichLinkMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata) |  A rich link to a resource. Rich links can be associated with the plain-text body of the message or represent chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length`  
[com.google.chat.v1.RichLinkMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata.Builder) |  A rich link to a resource. Rich links can be associated with the plain-text body of the message or represent chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length`  
[com.google.chat.v1.SearchMessageResult](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessageResult) |  A single result item from a message search.   
[com.google.chat.v1.SearchMessageResult.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessageResult.Builder) |  A single result item from a message search.   
[com.google.chat.v1.SearchMessagesRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest) |  Request message for searching messages.   
[com.google.chat.v1.SearchMessagesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest.Builder) |  Request message for searching messages.   
[com.google.chat.v1.SearchMessagesResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponse) |  Response message for searching messages.   
[com.google.chat.v1.SearchMessagesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponse.Builder) |  Response message for searching messages.   
[com.google.chat.v1.SearchSpacesRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest) |  Request to search for a list of spaces based on a query.   
[com.google.chat.v1.SearchSpacesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder) |  Request to search for a list of spaces based on a query.   
[com.google.chat.v1.SearchSpacesResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse) |  Response with a list of spaces corresponding to the search spaces request.   
[com.google.chat.v1.SearchSpacesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse.Builder) |  Response with a list of spaces corresponding to the search spaces request.   
[com.google.chat.v1.SearchSpacesResponse.SearchSpaceResult](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse.SearchSpaceResult) |  A single result item from a space search.   
[com.google.chat.v1.SearchSpacesResponse.SearchSpaceResult.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse.SearchSpaceResult.Builder) |  A single result item from a space search.   
[com.google.chat.v1.Section](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section) |  Represents a [section](https://support.google.com/chat/answer/16059854) in Google Chat. Sections help users organize their spaces. There are two types of sections:  
[com.google.chat.v1.Section.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section.Builder) |  Represents a [section](https://support.google.com/chat/answer/16059854) in Google Chat. Sections help users organize their spaces. There are two types of sections:  
[com.google.chat.v1.SectionItem](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItem) |  A user's defined section item. This is used to represent section items, such as spaces, grouped under a section.   
[com.google.chat.v1.SectionItem.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItem.Builder) |  A user's defined section item. This is used to represent section items, such as spaces, grouped under a section.   
[com.google.chat.v1.SectionItemName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItemName) |   
[com.google.chat.v1.SectionItemName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItemName.Builder) |  Builder for users/{user}/sections/{section}/items/{item}.  
[com.google.chat.v1.SectionName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionName) |   
[com.google.chat.v1.SectionName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionName.Builder) |  Builder for users/{user}/sections/{section}.  
[com.google.chat.v1.SectionProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionProto) |   
[com.google.chat.v1.SetUpSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest) |  Request to create a space and add specified users to it.   
[com.google.chat.v1.SetUpSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest.Builder) |  Request to create a space and add specified users to it.   
[com.google.chat.v1.SlashCommand](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommand) |  Metadata about a [slash command](https://developers.google.com/workspace/chat/commands) in Google Chat.  
[com.google.chat.v1.SlashCommand.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommand.Builder) |  Metadata about a [slash command](https://developers.google.com/workspace/chat/commands) in Google Chat.  
[com.google.chat.v1.SlashCommandMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata) |  Annotation metadata for slash commands (/).   
[com.google.chat.v1.SlashCommandMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata.Builder) |  Annotation metadata for slash commands (/).   
[com.google.chat.v1.SlashCommandProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandProto) |   
[com.google.chat.v1.Space](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space) |  A space in Google Chat. Spaces are conversations between two or more users or 1:1 messages between a user and a Chat app.   
[com.google.chat.v1.Space.AccessPermissionSetting](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSetting) |  An access permission setting.   
[com.google.chat.v1.Space.AccessPermissionSetting.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSetting.Builder) |  An access permission setting.   
[com.google.chat.v1.Space.AccessPermissionSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSettings.Builder) |  Access permission settings for a space.   
[com.google.chat.v1.Space.AccessSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessSettings.Builder) |  Represents the [access setting](https://support.google.com/chat/answer/11971020) of the space.   
[com.google.chat.v1.Space.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.Builder) |  A space in Google Chat. Spaces are conversations between two or more users or 1:1 messages between a user and a Chat app.   
[com.google.chat.v1.Space.MembershipCount](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.MembershipCount) |  Represents the count of memberships of a space, grouped into categories.   
[com.google.chat.v1.Space.MembershipCount.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.MembershipCount.Builder) |  Represents the count of memberships of a space, grouped into categories.   
[com.google.chat.v1.Space.PermissionSetting](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting) |  Represents a space permission setting.   
[com.google.chat.v1.Space.PermissionSetting.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting.Builder) |  Represents a space permission setting.   
[com.google.chat.v1.Space.PermissionSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder) |  [Permission settings](https://support.google.com/chat/answer/13340792) that you can specify when updating an existing named space.   
[com.google.chat.v1.Space.Principal](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.Principal) |  A principal representing an entity granted access.   
[com.google.chat.v1.Space.Principal.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.Principal.Builder) |  A principal representing an entity granted access.   
[com.google.chat.v1.Space.SpaceDetails](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpaceDetails) |  Details about the space including description and rules.   
[com.google.chat.v1.Space.SpaceDetails.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpaceDetails.Builder) |  Details about the space including description and rules.   
[com.google.chat.v1.SpaceBatchUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceBatchUpdatedEventData) |  Event payload for multiple updates to a space. Event type: `google.workspace.chat.space.v1.batchUpdated`  
[com.google.chat.v1.SpaceBatchUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceBatchUpdatedEventData.Builder) |  Event payload for multiple updates to a space. Event type: `google.workspace.chat.space.v1.batchUpdated`  
[com.google.chat.v1.SpaceEvent](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent) |  An event that represents a change or activity in a Google Chat space. To learn more, see [Work with events from Google Chat](https://developers.google.com/workspace/chat/events-overview).  
[com.google.chat.v1.SpaceEvent.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent.Builder) |  An event that represents a change or activity in a Google Chat space. To learn more, see [Work with events from Google Chat](https://developers.google.com/workspace/chat/events-overview).  
[com.google.chat.v1.SpaceEventName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEventName) |   
[com.google.chat.v1.SpaceEventName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEventName.Builder) |  Builder for spaces/{space}/spaceEvents/{space_event}.  
[com.google.chat.v1.SpaceEventProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEventProto) |   
[com.google.chat.v1.SpaceName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceName) |   
[com.google.chat.v1.SpaceName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceName.Builder) |  Builder for spaces/{space}.  
[com.google.chat.v1.SpaceNotificationSetting](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting) |  The notification setting of a user in a space.   
[com.google.chat.v1.SpaceNotificationSetting.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting.Builder) |  The notification setting of a user in a space.   
[com.google.chat.v1.SpaceNotificationSettingName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSettingName) |   
[com.google.chat.v1.SpaceNotificationSettingName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSettingName.Builder) |  Builder for users/{user}/spaces/{space}/spaceNotificationSetting.  
[com.google.chat.v1.SpaceNotificationSettingProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSettingProto) |   
[com.google.chat.v1.SpaceProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceProto) |   
[com.google.chat.v1.SpaceReadState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState) |  A user's read state within a space, used to identify read and unread messages.   
[com.google.chat.v1.SpaceReadState.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState.Builder) |  A user's read state within a space, used to identify read and unread messages.   
[com.google.chat.v1.SpaceReadStateName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadStateName) |   
[com.google.chat.v1.SpaceReadStateName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadStateName.Builder) |  Builder for users/{user}/spaces/{space}/spaceReadState.  
[com.google.chat.v1.SpaceReadStateProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadStateProto) |   
[com.google.chat.v1.SpaceSetupProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceSetupProto) |   
[com.google.chat.v1.SpaceUpdatedEventData](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceUpdatedEventData) |  Event payload for an updated space. Event type: `google.workspace.chat.space.v1.updated`  
[com.google.chat.v1.SpaceUpdatedEventData.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceUpdatedEventData.Builder) |  Event payload for an updated space. Event type: `google.workspace.chat.space.v1.updated`  
[com.google.chat.v1.Thread](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Thread) |  A thread in a Google Chat space. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).  
[com.google.chat.v1.Thread.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Thread.Builder) |  A thread in a Google Chat space. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).  
[com.google.chat.v1.ThreadReadState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState) |  A user's read state within a thread, used to identify read and unread messages.   
[com.google.chat.v1.ThreadReadState.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState.Builder) |  A user's read state within a thread, used to identify read and unread messages.   
[com.google.chat.v1.ThreadReadStateName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadStateName) |   
[com.google.chat.v1.ThreadReadStateName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadStateName.Builder) |  Builder for users/{user}/spaces/{space}/threads/{thread}/threadReadState.  
[com.google.chat.v1.ThreadReadStateProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadStateProto) |   
[com.google.chat.v1.UpdateAvailabilityRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest) |  Request message for the `UpdateAvailability` method.   
[com.google.chat.v1.UpdateAvailabilityRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest.Builder) |  Request message for the `UpdateAvailability` method.   
[com.google.chat.v1.UpdateMembershipRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest) |  Request message for updating a membership.   
[com.google.chat.v1.UpdateMembershipRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest.Builder) |  Request message for updating a membership.   
[com.google.chat.v1.UpdateMessageRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest) |  Request to update a message.   
[com.google.chat.v1.UpdateMessageRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest.Builder) |  Request to update a message.   
[com.google.chat.v1.UpdateSectionRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest) |  Request message for updating a section.   
[com.google.chat.v1.UpdateSectionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest.Builder) |  Request message for updating a section.   
[com.google.chat.v1.UpdateSpaceNotificationSettingRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest) |  Request to update the space notification settings. Only supports updating notification setting for the calling user.   
[com.google.chat.v1.UpdateSpaceNotificationSettingRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest.Builder) |  Request to update the space notification settings. Only supports updating notification setting for the calling user.   
[com.google.chat.v1.UpdateSpaceReadStateRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest) |  Request message for UpdateSpaceReadState API.   
[com.google.chat.v1.UpdateSpaceReadStateRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest.Builder) |  Request message for UpdateSpaceReadState API.   
[com.google.chat.v1.UpdateSpaceRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest) |  A request to update a single space.   
[com.google.chat.v1.UpdateSpaceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest.Builder) |  A request to update a single space.   
[com.google.chat.v1.UploadAttachmentRequest](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest) |  Request to upload an attachment.   
[com.google.chat.v1.UploadAttachmentRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest.Builder) |  Request to upload an attachment.   
[com.google.chat.v1.UploadAttachmentResponse](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse) |  Response of uploading an attachment.   
[com.google.chat.v1.UploadAttachmentResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse.Builder) |  Response of uploading an attachment.   
[com.google.chat.v1.User](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.User) |  If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output for a `User` resource (such as in the Messages and Memberships  
[com.google.chat.v1.User.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.User.Builder) |  If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output for a `User` resource (such as in the Messages and Memberships  
[com.google.chat.v1.UserMentionMetadata](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata) |  Annotation metadata for user mentions (@).   
[com.google.chat.v1.UserMentionMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata.Builder) |  Annotation metadata for user mentions (@).   
[com.google.chat.v1.UserName](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserName) |   
[com.google.chat.v1.UserName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserName.Builder) |  Builder for users/{user}.  
[com.google.chat.v1.UserProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserProto) |   
[com.google.chat.v1.WidgetMarkup](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup) |  A widget is a UI element that presents text and images.   
[com.google.chat.v1.WidgetMarkup.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Builder) |  A widget is a UI element that presents text and images.   
[com.google.chat.v1.WidgetMarkup.Button](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Button) |  A button. Can be a text button or an image button.   
[com.google.chat.v1.WidgetMarkup.Button.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Button.Builder) |  A button. Can be a text button or an image button.   
[com.google.chat.v1.WidgetMarkup.FormAction](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormAction) |  A form action describes the behavior when the form is submitted. For example, you can invoke Apps Script to handle the form.   
[com.google.chat.v1.WidgetMarkup.FormAction.ActionParameter](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormAction.ActionParameter) |  List of string parameters to supply when the action method is invoked. For example, consider three snooze buttons: snooze now, snooze one day, snooze next week. You might use `action method = snooze()`, passing the  
[com.google.chat.v1.WidgetMarkup.FormAction.ActionParameter.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormAction.ActionParameter.Builder) |  List of string parameters to supply when the action method is invoked. For example, consider three snooze buttons: snooze now, snooze one day, snooze next week. You might use `action method = snooze()`, passing the  
[com.google.chat.v1.WidgetMarkup.FormAction.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormAction.Builder) |  A form action describes the behavior when the form is submitted. For example, you can invoke Apps Script to handle the form.   
[com.google.chat.v1.WidgetMarkup.Image](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Image) |  An image that's specified by a URL and can have an `onclick` action.   
[com.google.chat.v1.WidgetMarkup.Image.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Image.Builder) |  An image that's specified by a URL and can have an `onclick` action.   
[com.google.chat.v1.WidgetMarkup.ImageButton](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ImageButton) |  An image button with an `onclick` action.   
[com.google.chat.v1.WidgetMarkup.ImageButton.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ImageButton.Builder) |  An image button with an `onclick` action.   
[com.google.chat.v1.WidgetMarkup.KeyValue](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.KeyValue) |  A UI element contains a key (label) and a value (content). This element can also contain some actions such as `onclick` button.   
[com.google.chat.v1.WidgetMarkup.KeyValue.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.KeyValue.Builder) |  A UI element contains a key (label) and a value (content). This element can also contain some actions such as `onclick` button.   
[com.google.chat.v1.WidgetMarkup.OnClick](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OnClick) |  An `onclick` action (for example, open a link).   
[com.google.chat.v1.WidgetMarkup.OnClick.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OnClick.Builder) |  An `onclick` action (for example, open a link).   
[com.google.chat.v1.WidgetMarkup.OpenLink](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OpenLink) |  A link that opens a new window.   
[com.google.chat.v1.WidgetMarkup.OpenLink.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OpenLink.Builder) |  A link that opens a new window.   
[com.google.chat.v1.WidgetMarkup.TextButton](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextButton) |  A button with text and `onclick` action.   
[com.google.chat.v1.WidgetMarkup.TextButton.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextButton.Builder) |  A button with text and `onclick` action.   
[com.google.chat.v1.WidgetMarkup.TextParagraph](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextParagraph) |  A paragraph of text. Formatted text supported. For more information about formatting text, see [Formatting text in Google Chat](https://developers.google.com/workspace/chat/format-messages#card-formatting)  
[com.google.chat.v1.WidgetMarkup.TextParagraph.Builder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextParagraph.Builder) |  A paragraph of text. Formatted text supported. For more information about formatting text, see [Formatting text in Google Chat](https://developers.google.com/workspace/chat/format-messages#card-formatting)  
[com.google.chat.v1.WidgetsProto](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetsProto) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.chat.v1.AccessoryWidgetOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidgetOrBuilder) |   
[com.google.chat.v1.ActionResponse.SelectionItemsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.SelectionItemsOrBuilder) |   
[com.google.chat.v1.ActionResponse.UpdatedWidgetOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.UpdatedWidgetOrBuilder) |   
[com.google.chat.v1.ActionResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponseOrBuilder) |   
[com.google.chat.v1.ActionStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionStatusOrBuilder) |   
[com.google.chat.v1.AnnotationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationOrBuilder) |   
[com.google.chat.v1.AppCommandMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AppCommandMetadataOrBuilder) |   
[com.google.chat.v1.AttachedGifOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachedGifOrBuilder) |   
[com.google.chat.v1.AttachmentDataRefOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentDataRefOrBuilder) |   
[com.google.chat.v1.AttachmentOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AttachmentOrBuilder) |   
[com.google.chat.v1.AudienceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AudienceOrBuilder) |   
[com.google.chat.v1.AvailabilityOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AvailabilityOrBuilder) |   
[com.google.chat.v1.CalendarEventLinkDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CalendarEventLinkDataOrBuilder) |   
[com.google.chat.v1.CardWithIdOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CardWithIdOrBuilder) |   
[com.google.chat.v1.ChatServiceGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc.AsyncService) |  Enables developers to build Chat apps and integrations on Google Chat Platform.   
[com.google.chat.v1.ChatSpaceLinkDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatSpaceLinkDataOrBuilder) |   
[com.google.chat.v1.CompleteImportSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequestOrBuilder) |   
[com.google.chat.v1.CompleteImportSpaceResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponseOrBuilder) |   
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardActionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardActionOrBuilder) |   
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeaderOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeaderOrBuilder) |   
[com.google.chat.v1.ContextualAddOnMarkup.Card.SectionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.SectionOrBuilder) |   
[com.google.chat.v1.ContextualAddOnMarkup.CardOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.CardOrBuilder) |   
[com.google.chat.v1.ContextualAddOnMarkupOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkupOrBuilder) |   
[com.google.chat.v1.CreateCustomEmojiRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequestOrBuilder) |   
[com.google.chat.v1.CreateMembershipRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequestOrBuilder) |   
[com.google.chat.v1.CreateMessageNotificationOptionsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageNotificationOptionsOrBuilder) |   
[com.google.chat.v1.CreateMessagePinRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequestOrBuilder) |   
[com.google.chat.v1.CreateMessageRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequestOrBuilder) |   
[com.google.chat.v1.CreateReactionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequestOrBuilder) |   
[com.google.chat.v1.CreateSectionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequestOrBuilder) |   
[com.google.chat.v1.CreateSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequestOrBuilder) |   
[com.google.chat.v1.CustomEmoji.CustomEmojiPayloadOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji.CustomEmojiPayloadOrBuilder) |   
[com.google.chat.v1.CustomEmojiMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadataOrBuilder) |   
[com.google.chat.v1.CustomEmojiOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiOrBuilder) |   
[com.google.chat.v1.CustomStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomStatusOrBuilder) |   
[com.google.chat.v1.DeleteCustomEmojiRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequestOrBuilder) |   
[com.google.chat.v1.DeleteMembershipRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequestOrBuilder) |   
[com.google.chat.v1.DeleteMessagePinRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequestOrBuilder) |   
[com.google.chat.v1.DeleteMessageRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequestOrBuilder) |   
[com.google.chat.v1.DeleteReactionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequestOrBuilder) |   
[com.google.chat.v1.DeleteSectionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequestOrBuilder) |   
[com.google.chat.v1.DeleteSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequestOrBuilder) |   
[com.google.chat.v1.DeletionMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadataOrBuilder) |   
[com.google.chat.v1.DialogActionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DialogActionOrBuilder) |   
[com.google.chat.v1.DialogOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DialogOrBuilder) |   
[com.google.chat.v1.DoNotDisturbMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DoNotDisturbMetadataOrBuilder) |   
[com.google.chat.v1.DriveDataRefOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveDataRefOrBuilder) |   
[com.google.chat.v1.DriveLinkDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DriveLinkDataOrBuilder) |   
[com.google.chat.v1.EmojiOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiOrBuilder) |   
[com.google.chat.v1.EmojiReactionSummaryOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.EmojiReactionSummaryOrBuilder) |   
[com.google.chat.v1.FindDirectMessageRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequestOrBuilder) |   
[com.google.chat.v1.FindGroupChatsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequestOrBuilder) |   
[com.google.chat.v1.FindGroupChatsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponseOrBuilder) |   
[com.google.chat.v1.ForwardedMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ForwardedMetadataOrBuilder) |   
[com.google.chat.v1.GetAttachmentRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequestOrBuilder) |   
[com.google.chat.v1.GetAvailabilityRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequestOrBuilder) |   
[com.google.chat.v1.GetCustomEmojiRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequestOrBuilder) |   
[com.google.chat.v1.GetMembershipRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequestOrBuilder) |   
[com.google.chat.v1.GetMessageRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequestOrBuilder) |   
[com.google.chat.v1.GetSpaceEventRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequestOrBuilder) |   
[com.google.chat.v1.GetSpaceNotificationSettingRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequestOrBuilder) |   
[com.google.chat.v1.GetSpaceReadStateRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequestOrBuilder) |   
[com.google.chat.v1.GetSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequestOrBuilder) |   
[com.google.chat.v1.GetThreadReadStateRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequestOrBuilder) |   
[com.google.chat.v1.GroupOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GroupOrBuilder) |   
[com.google.chat.v1.ListCustomEmojisRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequestOrBuilder) |   
[com.google.chat.v1.ListCustomEmojisResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponseOrBuilder) |   
[com.google.chat.v1.ListMembershipsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequestOrBuilder) |   
[com.google.chat.v1.ListMembershipsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponseOrBuilder) |   
[com.google.chat.v1.ListMessagePinsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequestOrBuilder) |   
[com.google.chat.v1.ListMessagePinsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponseOrBuilder) |   
[com.google.chat.v1.ListMessagesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequestOrBuilder) |   
[com.google.chat.v1.ListMessagesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponseOrBuilder) |   
[com.google.chat.v1.ListReactionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequestOrBuilder) |   
[com.google.chat.v1.ListReactionsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponseOrBuilder) |   
[com.google.chat.v1.ListSectionItemsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequestOrBuilder) |   
[com.google.chat.v1.ListSectionItemsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponseOrBuilder) |   
[com.google.chat.v1.ListSectionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequestOrBuilder) |   
[com.google.chat.v1.ListSectionsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponseOrBuilder) |   
[com.google.chat.v1.ListSpaceEventsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequestOrBuilder) |   
[com.google.chat.v1.ListSpaceEventsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponseOrBuilder) |   
[com.google.chat.v1.ListSpacesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequestOrBuilder) |   
[com.google.chat.v1.ListSpacesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponseOrBuilder) |   
[com.google.chat.v1.MarkAsActiveRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequestOrBuilder) |   
[com.google.chat.v1.MarkAsAwayRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequestOrBuilder) |   
[com.google.chat.v1.MarkAsDoNotDisturbRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequestOrBuilder) |   
[com.google.chat.v1.MatchedUrlOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MatchedUrlOrBuilder) |   
[com.google.chat.v1.MeetSpaceLinkDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MeetSpaceLinkDataOrBuilder) |   
[com.google.chat.v1.MembershipBatchCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchCreatedEventDataOrBuilder) |   
[com.google.chat.v1.MembershipBatchDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchDeletedEventDataOrBuilder) |   
[com.google.chat.v1.MembershipBatchUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipBatchUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.MembershipCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipCreatedEventDataOrBuilder) |   
[com.google.chat.v1.MembershipDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipDeletedEventDataOrBuilder) |   
[com.google.chat.v1.MembershipOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipOrBuilder) |   
[com.google.chat.v1.MembershipUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MembershipUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.MessageBatchCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchCreatedEventDataOrBuilder) |   
[com.google.chat.v1.MessageBatchDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchDeletedEventDataOrBuilder) |   
[com.google.chat.v1.MessageBatchUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageBatchUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.MessageCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageCreatedEventDataOrBuilder) |   
[com.google.chat.v1.MessageDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageDeletedEventDataOrBuilder) |   
[com.google.chat.v1.MessageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageOrBuilder) |   
[com.google.chat.v1.MessagePinOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePinOrBuilder) |   
[com.google.chat.v1.MessageUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessageUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.MoveSectionItemRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequestOrBuilder) |   
[com.google.chat.v1.MoveSectionItemResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponseOrBuilder) |   
[com.google.chat.v1.PositionSectionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequestOrBuilder) |   
[com.google.chat.v1.PositionSectionResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponseOrBuilder) |   
[com.google.chat.v1.QuotedMessageMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadataOrBuilder) |   
[com.google.chat.v1.QuotedMessageSnapshotOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageSnapshotOrBuilder) |   
[com.google.chat.v1.ReactionBatchCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchCreatedEventDataOrBuilder) |   
[com.google.chat.v1.ReactionBatchDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionBatchDeletedEventDataOrBuilder) |   
[com.google.chat.v1.ReactionCreatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionCreatedEventDataOrBuilder) |   
[com.google.chat.v1.ReactionDeletedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionDeletedEventDataOrBuilder) |   
[com.google.chat.v1.ReactionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ReactionOrBuilder) |   
[com.google.chat.v1.RichLinkMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadataOrBuilder) |   
[com.google.chat.v1.SearchMessageResultOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessageResultOrBuilder) |   
[com.google.chat.v1.SearchMessagesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequestOrBuilder) |   
[com.google.chat.v1.SearchMessagesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponseOrBuilder) |   
[com.google.chat.v1.SearchSpacesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequestOrBuilder) |   
[com.google.chat.v1.SearchSpacesResponse.SearchSpaceResultOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse.SearchSpaceResultOrBuilder) |   
[com.google.chat.v1.SearchSpacesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponseOrBuilder) |   
[com.google.chat.v1.SectionItemOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItemOrBuilder) |   
[com.google.chat.v1.SectionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionOrBuilder) |   
[com.google.chat.v1.SetUpSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequestOrBuilder) |   
[com.google.chat.v1.SlashCommandMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadataOrBuilder) |   
[com.google.chat.v1.SlashCommandOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandOrBuilder) |   
[com.google.chat.v1.Space.AccessPermissionSettingOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSettingOrBuilder) |   
[com.google.chat.v1.Space.AccessPermissionSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessPermissionSettingsOrBuilder) |   
[com.google.chat.v1.Space.AccessSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessSettingsOrBuilder) |   
[com.google.chat.v1.Space.MembershipCountOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.MembershipCountOrBuilder) |   
[com.google.chat.v1.Space.PermissionSettingOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder) |   
[com.google.chat.v1.Space.PermissionSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingsOrBuilder) |   
[com.google.chat.v1.Space.PrincipalOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PrincipalOrBuilder) |   
[com.google.chat.v1.Space.SpaceDetailsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpaceDetailsOrBuilder) |   
[com.google.chat.v1.SpaceBatchUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceBatchUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.SpaceEventOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEventOrBuilder) |   
[com.google.chat.v1.SpaceNotificationSettingOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSettingOrBuilder) |   
[com.google.chat.v1.SpaceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceOrBuilder) |   
[com.google.chat.v1.SpaceReadStateOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadStateOrBuilder) |   
[com.google.chat.v1.SpaceUpdatedEventDataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceUpdatedEventDataOrBuilder) |   
[com.google.chat.v1.ThreadOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadOrBuilder) |   
[com.google.chat.v1.ThreadReadStateOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadStateOrBuilder) |   
[com.google.chat.v1.UpdateAvailabilityRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequestOrBuilder) |   
[com.google.chat.v1.UpdateMembershipRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequestOrBuilder) |   
[com.google.chat.v1.UpdateMessageRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequestOrBuilder) |   
[com.google.chat.v1.UpdateSectionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequestOrBuilder) |   
[com.google.chat.v1.UpdateSpaceNotificationSettingRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequestOrBuilder) |   
[com.google.chat.v1.UpdateSpaceReadStateRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequestOrBuilder) |   
[com.google.chat.v1.UpdateSpaceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequestOrBuilder) |   
[com.google.chat.v1.UploadAttachmentRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequestOrBuilder) |   
[com.google.chat.v1.UploadAttachmentResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponseOrBuilder) |   
[com.google.chat.v1.UserMentionMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadataOrBuilder) |   
[com.google.chat.v1.UserOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.ButtonOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ButtonOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.FormAction.ActionParameterOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormAction.ActionParameterOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.FormActionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.FormActionOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.ImageButtonOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ImageButtonOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.ImageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ImageOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.KeyValueOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.KeyValueOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.OnClickOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OnClickOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.OpenLinkOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OpenLinkOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.TextButtonOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextButtonOrBuilder) |   
[com.google.chat.v1.WidgetMarkup.TextParagraphOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.TextParagraphOrBuilder) |   
[com.google.chat.v1.WidgetMarkupOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkupOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.chat.v1.AccessoryWidget.ActionCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AccessoryWidget.ActionCase) |   
[com.google.chat.v1.ActionResponse.ResponseType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.ResponseType) |  The type of Chat app response.   
[com.google.chat.v1.ActionResponse.UpdatedWidget.UpdatedWidgetCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ActionResponse.UpdatedWidget.UpdatedWidgetCase) |   
[com.google.chat.v1.Annotation.MetadataCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.MetadataCase) |   
[com.google.chat.v1.AnnotationType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationType) |  Type of the annotation.   
[com.google.chat.v1.AppCommandMetadata.AppCommandType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AppCommandMetadata.AppCommandType) |  The type of Chat app command. For details, see [Types of Chat app commands](https://developers.google.com/workspace/chat/commands#types).   
[com.google.chat.v1.Attachment.DataRefCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment.DataRefCase) |   
[com.google.chat.v1.Attachment.Source](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment.Source) |  The source of the attachment.   
[com.google.chat.v1.Availability.State](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability.State) |  Represents the current availability state of the user.   
[com.google.chat.v1.Availability.StateMetadataCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability.StateMetadataCase) |   
[com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.ImageStyle](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.ImageStyle) |  Protobuf enum `google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.ImageStyle`  
[com.google.chat.v1.CreateMessageNotificationOptions.NotificationType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageNotificationOptions.NotificationType) |  The notification types options for the message.   
[com.google.chat.v1.CreateMessageRequest.MessageReplyOption](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest.MessageReplyOption) |  Specifies how to reply to a message. More states might be added in the future.   
[com.google.chat.v1.CustomStatus.ExpirationCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomStatus.ExpirationCase) |   
[com.google.chat.v1.DeletionMetadata.DeletionType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeletionMetadata.DeletionType) |  Who deleted the message and how it was deleted. More values may be added in the future. See [Edit or delete a message in Google Chat](https://support.google.com/chat/answer/7653281) for details on when  
[com.google.chat.v1.DialogAction.ActionCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DialogAction.ActionCase) |   
[com.google.chat.v1.Emoji.ContentCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Emoji.ContentCase) |   
[com.google.chat.v1.HistoryState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.HistoryState) |  The history state for messages and spaces. Specifies how long messages and conversation threads are kept after creation.   
[com.google.chat.v1.MarkAsActiveRequest.ExpirationCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest.ExpirationCase) |   
[com.google.chat.v1.MarkAsDoNotDisturbRequest.ExpirationCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest.ExpirationCase) |   
[com.google.chat.v1.MarkupSyntax](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkupSyntax) |  Specifies the markup syntax used to format the Chat message text. Applies to the `text` field of the `Message` resource.   
[com.google.chat.v1.MeetSpaceLinkData.HuddleStatus](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MeetSpaceLinkData.HuddleStatus) |  The status of the huddle   
[com.google.chat.v1.MeetSpaceLinkData.Type](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MeetSpaceLinkData.Type) |  The type of the Meet space.   
[com.google.chat.v1.Membership.Affiliation](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership.Affiliation) |  Represents the affiliation of a user to the Google Workspace organization that owns the space. This enum may have more values added in the future.   
[com.google.chat.v1.Membership.MemberTypeCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership.MemberTypeCase) |   
[com.google.chat.v1.Membership.MembershipRole](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership.MembershipRole) |  Represents a user's permitted actions in a Chat space. More enum values might be added in the future.   
[com.google.chat.v1.Membership.MembershipState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership.MembershipState) |  Specifies the member's relationship with a space. Other membership states might be supported in the future.   
[com.google.chat.v1.PositionSectionRequest.Position](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest.Position) |  The position of the section.   
[com.google.chat.v1.PositionSectionRequest.PositionCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest.PositionCase) |   
[com.google.chat.v1.QuotedMessageMetadata.QuoteType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.QuotedMessageMetadata.QuoteType) |  The quote type of the quoted message.   
[com.google.chat.v1.RichLinkMetadata.DataCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata.DataCase) |   
[com.google.chat.v1.RichLinkMetadata.RichLinkType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata.RichLinkType) |  The rich link type. More types might be added in the future.   
[com.google.chat.v1.SearchMessagesRequest.SearchMessagesView](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest.SearchMessagesView) |  The kinds of view that are supported for partial search results.   
[com.google.chat.v1.Section.SectionType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section.SectionType) |  Section types.   
[com.google.chat.v1.SectionItem.ItemCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SectionItem.ItemCase) |   
[com.google.chat.v1.SlashCommandMetadata.Type](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata.Type) |  Protobuf enum `google.chat.v1.SlashCommandMetadata.Type`  
[com.google.chat.v1.Space.AccessSettings.AccessState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.AccessSettings.AccessState) |  Represents the access state of the space.   
[com.google.chat.v1.Space.Principal.PrincipalTypeCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.Principal.PrincipalTypeCase) |   
[com.google.chat.v1.Space.SpacePermissionSettingsCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpacePermissionSettingsCase) |   
[com.google.chat.v1.Space.SpaceThreadingState](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpaceThreadingState) |  Specifies the type of threading state in the Chat space.   
[com.google.chat.v1.Space.SpaceType](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.SpaceType) |  The type of space. Required when creating or updating a space. Output only for other usage.   
[com.google.chat.v1.Space.Type](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.Type) |  Deprecated: Use `SpaceType` instead.   
[com.google.chat.v1.SpaceEvent.PayloadCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent.PayloadCase) |   
[com.google.chat.v1.SpaceNotificationSetting.MuteSetting](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting.MuteSetting) |  The space notification mute setting types.   
[com.google.chat.v1.SpaceNotificationSetting.NotificationSetting](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting.NotificationSetting) |  The notification setting types. Other types might be supported in the future.   
[com.google.chat.v1.SpaceView](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceView) |  A view that specifies which fields should be populated on the [`Space`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) resource.  
[com.google.chat.v1.User.Type](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.User.Type) |  Protobuf enum `google.chat.v1.User.Type`  
[com.google.chat.v1.UserMentionMetadata.Type](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata.Type) |  Protobuf enum `google.chat.v1.UserMentionMetadata.Type`  
[com.google.chat.v1.WidgetMarkup.Button.TypeCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Button.TypeCase) |   
[com.google.chat.v1.WidgetMarkup.DataCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.DataCase) |   
[com.google.chat.v1.WidgetMarkup.Icon](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.Icon) |  The set of supported icons.   
[com.google.chat.v1.WidgetMarkup.ImageButton.IconsCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.ImageButton.IconsCase) |   
[com.google.chat.v1.WidgetMarkup.KeyValue.ControlCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.KeyValue.ControlCase) |   
[com.google.chat.v1.WidgetMarkup.KeyValue.IconsCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.KeyValue.IconsCase) |   
[com.google.chat.v1.WidgetMarkup.OnClick.DataCase](https://cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.WidgetMarkup.OnClick.DataCase) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
