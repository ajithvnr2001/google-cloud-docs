---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/chat/latest/apiv1/chatpb/
title: Google Chat API v1 - Package cloud.google.com/go/chat/apiv1/chatpb (v1.9.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:02.864118+00:00
---

# Google Chat API v1 - Package cloud.google.com/go/chat/apiv1/chatpb (v1.9.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/chat/latest/apiv1/chatpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Google Chat API v1 - Package cloud.google.com/go/chat/apiv1/chatpb (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.2  0.11.0  0.10.1  0.9.1  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.3 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/chat/apiv1/chatpb). 

##  Constants 

### ChatService_CreateMessage_FullMethodName, ChatService_ListMessages_FullMethodName, ChatService_ListMemberships_FullMethodName, ChatService_GetMembership_FullMethodName, ChatService_GetMessage_FullMethodName, ChatService_UpdateMessage_FullMethodName, ChatService_DeleteMessage_FullMethodName, ChatService_SearchMessages_FullMethodName, ChatService_GetAttachment_FullMethodName, ChatService_UploadAttachment_FullMethodName, ChatService_ListSpaces_FullMethodName, ChatService_SearchSpaces_FullMethodName, ChatService_GetSpace_FullMethodName, ChatService_CreateSpace_FullMethodName, ChatService_SetUpSpace_FullMethodName, ChatService_UpdateSpace_FullMethodName, ChatService_DeleteSpace_FullMethodName, ChatService_CompleteImportSpace_FullMethodName, ChatService_FindDirectMessage_FullMethodName, ChatService_FindGroupChats_FullMethodName, ChatService_CreateMembership_FullMethodName, ChatService_UpdateMembership_FullMethodName, ChatService_DeleteMembership_FullMethodName, ChatService_CreateReaction_FullMethodName, ChatService_ListReactions_FullMethodName, ChatService_DeleteReaction_FullMethodName, ChatService_ListMessagePins_FullMethodName, ChatService_CreateMessagePin_FullMethodName, ChatService_DeleteMessagePin_FullMethodName, ChatService_CreateCustomEmoji_FullMethodName, ChatService_GetCustomEmoji_FullMethodName, ChatService_ListCustomEmojis_FullMethodName, ChatService_DeleteCustomEmoji_FullMethodName, ChatService_GetSpaceReadState_FullMethodName, ChatService_UpdateSpaceReadState_FullMethodName, ChatService_GetThreadReadState_FullMethodName, ChatService_GetAvailability_FullMethodName, ChatService_MarkAsActive_FullMethodName, ChatService_MarkAsAway_FullMethodName, ChatService_MarkAsDoNotDisturb_FullMethodName, ChatService_UpdateAvailability_FullMethodName, ChatService_GetSpaceEvent_FullMethodName, ChatService_ListSpaceEvents_FullMethodName, ChatService_GetSpaceNotificationSetting_FullMethodName, ChatService_UpdateSpaceNotificationSetting_FullMethodName, ChatService_CreateSection_FullMethodName, ChatService_DeleteSection_FullMethodName, ChatService_UpdateSection_FullMethodName, ChatService_ListSections_FullMethodName, ChatService_PositionSection_FullMethodName, ChatService_ListSectionItems_FullMethodName, ChatService_MoveSectionItem_FullMethodName
    
    
    const (
    	ChatService_CreateMessage_FullMethodName                  = "/google.chat.v1.ChatService/CreateMessage"
    	ChatService_ListMessages_FullMethodName                   = "/google.chat.v1.ChatService/ListMessages"
    	ChatService_ListMemberships_FullMethodName                = "/google.chat.v1.ChatService/ListMemberships"
    	ChatService_GetMembership_FullMethodName                  = "/google.chat.v1.ChatService/GetMembership"
    	ChatService_GetMessage_FullMethodName                     = "/google.chat.v1.ChatService/GetMessage"
    	ChatService_UpdateMessage_FullMethodName                  = "/google.chat.v1.ChatService/UpdateMessage"
    	ChatService_DeleteMessage_FullMethodName                  = "/google.chat.v1.ChatService/DeleteMessage"
    	ChatService_SearchMessages_FullMethodName                 = "/google.chat.v1.ChatService/SearchMessages"
    	ChatService_GetAttachment_FullMethodName                  = "/google.chat.v1.ChatService/GetAttachment"
    	ChatService_UploadAttachment_FullMethodName               = "/google.chat.v1.ChatService/UploadAttachment"
    	ChatService_ListSpaces_FullMethodName                     = "/google.chat.v1.ChatService/ListSpaces"
    	ChatService_SearchSpaces_FullMethodName                   = "/google.chat.v1.ChatService/SearchSpaces"
    	ChatService_GetSpace_FullMethodName                       = "/google.chat.v1.ChatService/GetSpace"
    	ChatService_CreateSpace_FullMethodName                    = "/google.chat.v1.ChatService/CreateSpace"
    	ChatService_SetUpSpace_FullMethodName                     = "/google.chat.v1.ChatService/SetUpSpace"
    	ChatService_UpdateSpace_FullMethodName                    = "/google.chat.v1.ChatService/UpdateSpace"
    	ChatService_DeleteSpace_FullMethodName                    = "/google.chat.v1.ChatService/DeleteSpace"
    	ChatService_CompleteImportSpace_FullMethodName            = "/google.chat.v1.ChatService/CompleteImportSpace"
    	ChatService_FindDirectMessage_FullMethodName              = "/google.chat.v1.ChatService/FindDirectMessage"
    	ChatService_FindGroupChats_FullMethodName                 = "/google.chat.v1.ChatService/FindGroupChats"
    	ChatService_CreateMembership_FullMethodName               = "/google.chat.v1.ChatService/CreateMembership"
    	ChatService_UpdateMembership_FullMethodName               = "/google.chat.v1.ChatService/UpdateMembership"
    	ChatService_DeleteMembership_FullMethodName               = "/google.chat.v1.ChatService/DeleteMembership"
    	ChatService_CreateReaction_FullMethodName                 = "/google.chat.v1.ChatService/CreateReaction"
    	ChatService_ListReactions_FullMethodName                  = "/google.chat.v1.ChatService/ListReactions"
    	ChatService_DeleteReaction_FullMethodName                 = "/google.chat.v1.ChatService/DeleteReaction"
    	ChatService_ListMessagePins_FullMethodName                = "/google.chat.v1.ChatService/ListMessagePins"
    	ChatService_CreateMessagePin_FullMethodName               = "/google.chat.v1.ChatService/CreateMessagePin"
    	ChatService_DeleteMessagePin_FullMethodName               = "/google.chat.v1.ChatService/DeleteMessagePin"
    	ChatService_CreateCustomEmoji_FullMethodName              = "/google.chat.v1.ChatService/CreateCustomEmoji"
    	ChatService_GetCustomEmoji_FullMethodName                 = "/google.chat.v1.ChatService/GetCustomEmoji"
    	ChatService_ListCustomEmojis_FullMethodName               = "/google.chat.v1.ChatService/ListCustomEmojis"
    	ChatService_DeleteCustomEmoji_FullMethodName              = "/google.chat.v1.ChatService/DeleteCustomEmoji"
    	ChatService_GetSpaceReadState_FullMethodName              = "/google.chat.v1.ChatService/GetSpaceReadState"
    	ChatService_UpdateSpaceReadState_FullMethodName           = "/google.chat.v1.ChatService/UpdateSpaceReadState"
    	ChatService_GetThreadReadState_FullMethodName             = "/google.chat.v1.ChatService/GetThreadReadState"
    	ChatService_GetAvailability_FullMethodName                = "/google.chat.v1.ChatService/GetAvailability"
    	ChatService_MarkAsActive_FullMethodName                   = "/google.chat.v1.ChatService/MarkAsActive"
    	ChatService_MarkAsAway_FullMethodName                     = "/google.chat.v1.ChatService/MarkAsAway"
    	ChatService_MarkAsDoNotDisturb_FullMethodName             = "/google.chat.v1.ChatService/MarkAsDoNotDisturb"
    	ChatService_UpdateAvailability_FullMethodName             = "/google.chat.v1.ChatService/UpdateAvailability"
    	ChatService_GetSpaceEvent_FullMethodName                  = "/google.chat.v1.ChatService/GetSpaceEvent"
    	ChatService_ListSpaceEvents_FullMethodName                = "/google.chat.v1.ChatService/ListSpaceEvents"
    	ChatService_GetSpaceNotificationSetting_FullMethodName    = "/google.chat.v1.ChatService/GetSpaceNotificationSetting"
    	ChatService_UpdateSpaceNotificationSetting_FullMethodName = "/google.chat.v1.ChatService/UpdateSpaceNotificationSetting"
    	ChatService_CreateSection_FullMethodName                  = "/google.chat.v1.ChatService/CreateSection"
    	ChatService_DeleteSection_FullMethodName                  = "/google.chat.v1.ChatService/DeleteSection"
    	ChatService_UpdateSection_FullMethodName                  = "/google.chat.v1.ChatService/UpdateSection"
    	ChatService_ListSections_FullMethodName                   = "/google.chat.v1.ChatService/ListSections"
    	ChatService_PositionSection_FullMethodName                = "/google.chat.v1.ChatService/PositionSection"
    	ChatService_ListSectionItems_FullMethodName               = "/google.chat.v1.ChatService/ListSectionItems"
    	ChatService_MoveSectionItem_FullMethodName                = "/google.chat.v1.ChatService/MoveSectionItem"
    )

## Variables 

### AnnotationType_name, AnnotationType_value
    
    
    var (
    	AnnotationType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ANNOTATION_TYPE_UNSPECIFIED",
    		1: "USER_MENTION",
    		2: "SLASH_COMMAND",
    		3: "RICH_LINK",
    		4: "CUSTOM_EMOJI",
    	}
    	AnnotationType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ANNOTATION_TYPE_UNSPECIFIED": 0,
    		"USER_MENTION":                1,
    		"SLASH_COMMAND":               2,
    		"RICH_LINK":                   3,
    		"CUSTOM_EMOJI":                4,
    	}
    )

Enum value maps for AnnotationType.

### UserMentionMetadata_Type_name, UserMentionMetadata_Type_value
    
    
    var (
    	UserMentionMetadata_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "ADD",
    		2: "MENTION",
    	}
    	UserMentionMetadata_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"ADD":              1,
    		"MENTION":          2,
    	}
    )

Enum value maps for UserMentionMetadata_Type.

### SlashCommandMetadata_Type_name, SlashCommandMetadata_Type_value
    
    
    var (
    	SlashCommandMetadata_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "ADD",
    		2: "INVOKE",
    	}
    	SlashCommandMetadata_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"ADD":              1,
    		"INVOKE":           2,
    	}
    )

Enum value maps for SlashCommandMetadata_Type.

### RichLinkMetadata_RichLinkType_name, RichLinkMetadata_RichLinkType_value
    
    
    var (
    	RichLinkMetadata_RichLinkType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RICH_LINK_TYPE_UNSPECIFIED",
    		1: "DRIVE_FILE",
    		2: "CHAT_SPACE",
    		3: "GMAIL_MESSAGE",
    		4: "MEET_SPACE",
    		5: "CALENDAR_EVENT",
    	}
    	RichLinkMetadata_RichLinkType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RICH_LINK_TYPE_UNSPECIFIED": 0,
    		"DRIVE_FILE":                 1,
    		"CHAT_SPACE":                 2,
    		"GMAIL_MESSAGE":              3,
    		"MEET_SPACE":                 4,
    		"CALENDAR_EVENT":             5,
    	}
    )

Enum value maps for RichLinkMetadata_RichLinkType.

### MeetSpaceLinkData_Type_name, MeetSpaceLinkData_Type_value
    
    
    var (
    	MeetSpaceLinkData_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "MEETING",
    		2: "HUDDLE",
    	}
    	MeetSpaceLinkData_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"MEETING":          1,
    		"HUDDLE":           2,
    	}
    )

Enum value maps for MeetSpaceLinkData_Type.

### MeetSpaceLinkData_HuddleStatus_name, MeetSpaceLinkData_HuddleStatus_value
    
    
    var (
    	MeetSpaceLinkData_HuddleStatus_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HUDDLE_STATUS_UNSPECIFIED",
    		1: "STARTED",
    		2: "ENDED",
    		3: "MISSED",
    	}
    	MeetSpaceLinkData_HuddleStatus_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HUDDLE_STATUS_UNSPECIFIED": 0,
    		"STARTED":                   1,
    		"ENDED":                     2,
    		"MISSED":                    3,
    	}
    )

Enum value maps for MeetSpaceLinkData_HuddleStatus.

### AppCommandMetadata_AppCommandType_name, AppCommandMetadata_AppCommandType_value
    
    
    var (
    	AppCommandMetadata_AppCommandType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "APP_COMMAND_TYPE_UNSPECIFIED",
    		1: "SLASH_COMMAND",
    		3: "QUICK_COMMAND",
    		4: "MESSAGE_ACTION",
    	}
    	AppCommandMetadata_AppCommandType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"APP_COMMAND_TYPE_UNSPECIFIED": 0,
    		"SLASH_COMMAND":                1,
    		"QUICK_COMMAND":                3,
    		"MESSAGE_ACTION":               4,
    	}
    )

Enum value maps for AppCommandMetadata_AppCommandType.

### Attachment_Source_name, Attachment_Source_value
    
    
    var (
    	Attachment_Source_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SOURCE_UNSPECIFIED",
    		1: "DRIVE_FILE",
    		2: "UPLOADED_CONTENT",
    	}
    	Attachment_Source_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SOURCE_UNSPECIFIED": 0,
    		"DRIVE_FILE":         1,
    		"UPLOADED_CONTENT":   2,
    	}
    )

Enum value maps for Attachment_Source.

### Availability_State_name, Availability_State_value
    
    
    var (
    	Availability_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "IDLE",
    		3: "AWAY",
    		4: "DO_NOT_DISTURB",
    	}
    	Availability_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"IDLE":              2,
    		"AWAY":              3,
    		"DO_NOT_DISTURB":    4,
    	}
    )

Enum value maps for Availability_State.

### ContextualAddOnMarkup_Card_CardHeader_ImageStyle_name, ContextualAddOnMarkup_Card_CardHeader_ImageStyle_value
    
    
    var (
    	ContextualAddOnMarkup_Card_CardHeader_ImageStyle_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IMAGE_STYLE_UNSPECIFIED",
    		1: "IMAGE",
    		2: "AVATAR",
    	}
    	ContextualAddOnMarkup_Card_CardHeader_ImageStyle_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IMAGE_STYLE_UNSPECIFIED": 0,
    		"IMAGE":                   1,
    		"AVATAR":                  2,
    	}
    )

Enum value maps for ContextualAddOnMarkup_Card_CardHeader_ImageStyle.

### DeletionMetadata_DeletionType_name, DeletionMetadata_DeletionType_value
    
    
    var (
    	DeletionMetadata_DeletionType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "DELETION_TYPE_UNSPECIFIED",
    		1: "CREATOR",
    		2: "SPACE_OWNER",
    		3: "ADMIN",
    		4: "APP_MESSAGE_EXPIRY",
    		5: "CREATOR_VIA_APP",
    		6: "SPACE_OWNER_VIA_APP",
    		7: "SPACE_MEMBER",
    	}
    	DeletionMetadata_DeletionType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"DELETION_TYPE_UNSPECIFIED": 0,
    		"CREATOR":                   1,
    		"SPACE_OWNER":               2,
    		"ADMIN":                     3,
    		"APP_MESSAGE_EXPIRY":        4,
    		"CREATOR_VIA_APP":           5,
    		"SPACE_OWNER_VIA_APP":       6,
    		"SPACE_MEMBER":              7,
    	}
    )

Enum value maps for DeletionMetadata_DeletionType.

### HistoryState_name, HistoryState_value
    
    
    var (
    	HistoryState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HISTORY_STATE_UNSPECIFIED",
    		1: "HISTORY_OFF",
    		2: "HISTORY_ON",
    	}
    	HistoryState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HISTORY_STATE_UNSPECIFIED": 0,
    		"HISTORY_OFF":               1,
    		"HISTORY_ON":                2,
    	}
    )

Enum value maps for HistoryState.

### MarkupSyntax_name, MarkupSyntax_value
    
    
    var (
    	MarkupSyntax_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MARKUP_SYNTAX_UNSPECIFIED",
    		1: "MARKUP_SYNTAX_CHAT",
    		2: "MARKUP_SYNTAX_MARKDOWN",
    	}
    	MarkupSyntax_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MARKUP_SYNTAX_UNSPECIFIED": 0,
    		"MARKUP_SYNTAX_CHAT":        1,
    		"MARKUP_SYNTAX_MARKDOWN":    2,
    	}
    )

Enum value maps for MarkupSyntax.

### Membership_MembershipState_name, Membership_MembershipState_value
    
    
    var (
    	Membership_MembershipState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MEMBERSHIP_STATE_UNSPECIFIED",
    		1: "JOINED",
    		2: "INVITED",
    		3: "NOT_A_MEMBER",
    	}
    	Membership_MembershipState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MEMBERSHIP_STATE_UNSPECIFIED": 0,
    		"JOINED":                       1,
    		"INVITED":                      2,
    		"NOT_A_MEMBER":                 3,
    	}
    )

Enum value maps for Membership_MembershipState.

### Membership_MembershipRole_name, Membership_MembershipRole_value
    
    
    var (
    	Membership_MembershipRole_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MEMBERSHIP_ROLE_UNSPECIFIED",
    		1: "ROLE_MEMBER",
    		2: "ROLE_MANAGER",
    		4: "ROLE_ASSISTANT_MANAGER",
    	}
    	Membership_MembershipRole_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MEMBERSHIP_ROLE_UNSPECIFIED": 0,
    		"ROLE_MEMBER":                 1,
    		"ROLE_MANAGER":                2,
    		"ROLE_ASSISTANT_MANAGER":      4,
    	}
    )

Enum value maps for Membership_MembershipRole.

### Membership_Affiliation_name, Membership_Affiliation_value
    
    
    var (
    	Membership_Affiliation_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "AFFILIATION_UNSPECIFIED",
    		1: "INTERNAL",
    		2: "EXTERNAL",
    		3: "MANAGED_EXTERNAL",
    	}
    	Membership_Affiliation_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"AFFILIATION_UNSPECIFIED": 0,
    		"INTERNAL":                1,
    		"EXTERNAL":                2,
    		"MANAGED_EXTERNAL":        3,
    	}
    )

Enum value maps for Membership_Affiliation.

### QuotedMessageMetadata_QuoteType_name, QuotedMessageMetadata_QuoteType_value
    
    
    var (
    	QuotedMessageMetadata_QuoteType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "QUOTE_TYPE_UNSPECIFIED",
    		1: "REPLY",
    		2: "FORWARD",
    	}
    	QuotedMessageMetadata_QuoteType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"QUOTE_TYPE_UNSPECIFIED": 0,
    		"REPLY":                  1,
    		"FORWARD":                2,
    	}
    )

Enum value maps for QuotedMessageMetadata_QuoteType.

### ActionResponse_ResponseType_name, ActionResponse_ResponseType_value
    
    
    var (
    	ActionResponse_ResponseType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "NEW_MESSAGE",
    		2: "UPDATE_MESSAGE",
    		6: "UPDATE_USER_MESSAGE_CARDS",
    		3: "REQUEST_CONFIG",
    		4: "DIALOG",
    		7: "UPDATE_WIDGET",
    	}
    	ActionResponse_ResponseType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED":          0,
    		"NEW_MESSAGE":               1,
    		"UPDATE_MESSAGE":            2,
    		"UPDATE_USER_MESSAGE_CARDS": 6,
    		"REQUEST_CONFIG":            3,
    		"DIALOG":                    4,
    		"UPDATE_WIDGET":             7,
    	}
    )

Enum value maps for ActionResponse_ResponseType.

### CreateMessageRequest_MessageReplyOption_name, CreateMessageRequest_MessageReplyOption_value
    
    
    var (
    	CreateMessageRequest_MessageReplyOption_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MESSAGE_REPLY_OPTION_UNSPECIFIED",
    		1: "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
    		2: "REPLY_MESSAGE_OR_FAIL",
    	}
    	CreateMessageRequest_MessageReplyOption_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MESSAGE_REPLY_OPTION_UNSPECIFIED":     0,
    		"REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD": 1,
    		"REPLY_MESSAGE_OR_FAIL":                2,
    	}
    )

Enum value maps for CreateMessageRequest_MessageReplyOption.

### CreateMessageNotificationOptions_NotificationType_name, CreateMessageNotificationOptions_NotificationType_value
    
    
    var (
    	CreateMessageNotificationOptions_NotificationType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "NOTIFICATION_TYPE_NONE",
    		2: "NOTIFICATION_TYPE_FORCE_NOTIFY",
    		3: "NOTIFICATION_TYPE_SILENT",
    	}
    	CreateMessageNotificationOptions_NotificationType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"NOTIFICATION_TYPE_NONE":         0,
    		"NOTIFICATION_TYPE_FORCE_NOTIFY": 2,
    		"NOTIFICATION_TYPE_SILENT":       3,
    	}
    )

Enum value maps for CreateMessageNotificationOptions_NotificationType.

### SearchMessagesRequest_SearchMessagesView_name, SearchMessagesRequest_SearchMessagesView_value
    
    
    var (
    	SearchMessagesRequest_SearchMessagesView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SEARCH_MESSAGES_VIEW_UNSPECIFIED",
    		1: "SEARCH_MESSAGES_VIEW_BASIC",
    		2: "SEARCH_MESSAGES_VIEW_FULL",
    	}
    	SearchMessagesRequest_SearchMessagesView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SEARCH_MESSAGES_VIEW_UNSPECIFIED": 0,
    		"SEARCH_MESSAGES_VIEW_BASIC":       1,
    		"SEARCH_MESSAGES_VIEW_FULL":        2,
    	}
    )

Enum value maps for SearchMessagesRequest_SearchMessagesView.

### Section_SectionType_name, Section_SectionType_value
    
    
    var (
    	Section_SectionType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SECTION_TYPE_UNSPECIFIED",
    		1: "CUSTOM_SECTION",
    		2: "DEFAULT_DIRECT_MESSAGES",
    		3: "DEFAULT_SPACES",
    		6: "DEFAULT_APPS",
    	}
    	Section_SectionType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SECTION_TYPE_UNSPECIFIED": 0,
    		"CUSTOM_SECTION":           1,
    		"DEFAULT_DIRECT_MESSAGES":  2,
    		"DEFAULT_SPACES":           3,
    		"DEFAULT_APPS":             6,
    	}
    )

Enum value maps for Section_SectionType.

### PositionSectionRequest_Position_name, PositionSectionRequest_Position_value
    
    
    var (
    	PositionSectionRequest_Position_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "POSITION_UNSPECIFIED",
    		1: "START",
    		2: "END",
    	}
    	PositionSectionRequest_Position_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"POSITION_UNSPECIFIED": 0,
    		"START":                1,
    		"END":                  2,
    	}
    )

Enum value maps for PositionSectionRequest_Position.

### SpaceView_name, SpaceView_value
    
    
    var (
    	SpaceView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SPACE_VIEW_UNSPECIFIED",
    		3: "SPACE_VIEW_RESOURCE_NAME_ONLY",
    		4: "SPACE_VIEW_EXPANDED",
    	}
    	SpaceView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SPACE_VIEW_UNSPECIFIED":        0,
    		"SPACE_VIEW_RESOURCE_NAME_ONLY": 3,
    		"SPACE_VIEW_EXPANDED":           4,
    	}
    )

Enum value maps for SpaceView.

### Space_Type_name, Space_Type_value
    
    
    var (
    	Space_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "ROOM",
    		2: "DM",
    	}
    	Space_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"ROOM":             1,
    		"DM":               2,
    	}
    )

Enum value maps for Space_Type.

### Space_SpaceType_name, Space_SpaceType_value
    
    
    var (
    	Space_SpaceType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SPACE_TYPE_UNSPECIFIED",
    		1: "SPACE",
    		2: "GROUP_CHAT",
    		3: "DIRECT_MESSAGE",
    	}
    	Space_SpaceType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SPACE_TYPE_UNSPECIFIED": 0,
    		"SPACE":                  1,
    		"GROUP_CHAT":             2,
    		"DIRECT_MESSAGE":         3,
    	}
    )

Enum value maps for Space_SpaceType.

### Space_SpaceThreadingState_name, Space_SpaceThreadingState_value
    
    
    var (
    	Space_SpaceThreadingState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SPACE_THREADING_STATE_UNSPECIFIED",
    		2: "THREADED_MESSAGES",
    		3: "GROUPED_MESSAGES",
    		4: "UNTHREADED_MESSAGES",
    	}
    	Space_SpaceThreadingState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SPACE_THREADING_STATE_UNSPECIFIED": 0,
    		"THREADED_MESSAGES":                 2,
    		"GROUPED_MESSAGES":                  3,
    		"UNTHREADED_MESSAGES":               4,
    	}
    )

Enum value maps for Space_SpaceThreadingState.

### Space_PredefinedPermissionSettings_name, Space_PredefinedPermissionSettings_value
    
    
    var (
    	Space_PredefinedPermissionSettings_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED",
    		1: "COLLABORATION_SPACE",
    		2: "ANNOUNCEMENT_SPACE",
    	}
    	Space_PredefinedPermissionSettings_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED": 0,
    		"COLLABORATION_SPACE":                        1,
    		"ANNOUNCEMENT_SPACE":                         2,
    	}
    )

Enum value maps for Space_PredefinedPermissionSettings.

### Space_AccessSettings_AccessState_name, Space_AccessSettings_AccessState_value
    
    
    var (
    	Space_AccessSettings_AccessState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ACCESS_STATE_UNSPECIFIED",
    		1: "PRIVATE",
    		2: "DISCOVERABLE",
    	}
    	Space_AccessSettings_AccessState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ACCESS_STATE_UNSPECIFIED": 0,
    		"PRIVATE":                  1,
    		"DISCOVERABLE":             2,
    	}
    )

Enum value maps for Space_AccessSettings_AccessState.

### SpaceNotificationSetting_NotificationSetting_name, SpaceNotificationSetting_NotificationSetting_value
    
    
    var (
    	SpaceNotificationSetting_NotificationSetting_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "NOTIFICATION_SETTING_UNSPECIFIED",
    		1: "ALL",
    		2: "MAIN_CONVERSATIONS",
    		3: "FOR_YOU",
    		4: "OFF",
    	}
    	SpaceNotificationSetting_NotificationSetting_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"NOTIFICATION_SETTING_UNSPECIFIED": 0,
    		"ALL":                              1,
    		"MAIN_CONVERSATIONS":               2,
    		"FOR_YOU":                          3,
    		"OFF":                              4,
    	}
    )

Enum value maps for SpaceNotificationSetting_NotificationSetting.

### SpaceNotificationSetting_MuteSetting_name, SpaceNotificationSetting_MuteSetting_value
    
    
    var (
    	SpaceNotificationSetting_MuteSetting_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MUTE_SETTING_UNSPECIFIED",
    		1: "UNMUTED",
    		2: "MUTED",
    	}
    	SpaceNotificationSetting_MuteSetting_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MUTE_SETTING_UNSPECIFIED": 0,
    		"UNMUTED":                  1,
    		"MUTED":                    2,
    	}
    )

Enum value maps for SpaceNotificationSetting_MuteSetting.

### User_Type_name, User_Type_value
    
    
    var (
    	User_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "HUMAN",
    		2: "BOT",
    	}
    	User_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"HUMAN":            1,
    		"BOT":              2,
    	}
    )

Enum value maps for User_Type.

### WidgetMarkup_Icon_name, WidgetMarkup_Icon_value
    
    
    var (
    	WidgetMarkup_Icon_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "ICON_UNSPECIFIED",
    		1:  "AIRPLANE",
    		26: "BOOKMARK",
    		25: "BUS",
    		9:  "CAR",
    		2:  "CLOCK",
    		12: "CONFIRMATION_NUMBER_ICON",
    		14: "DOLLAR",
    		27: "DESCRIPTION",
    		10: "EMAIL",
    		20: "EVENT_PERFORMER",
    		21: "EVENT_SEAT",
    		16: "FLIGHT_ARRIVAL",
    		15: "FLIGHT_DEPARTURE",
    		6:  "HOTEL",
    		17: "HOTEL_ROOM_TYPE",
    		19: "INVITE",
    		3:  "MAP_PIN",
    		24: "MEMBERSHIP",
    		18: "MULTIPLE_PEOPLE",
    		30: "OFFER",
    		11: "PERSON",
    		13: "PHONE",
    		7:  "RESTAURANT_ICON",
    		8:  "SHOPPING_CART",
    		5:  "STAR",
    		22: "STORE",
    		4:  "TICKET",
    		23: "TRAIN",
    		28: "VIDEO_CAMERA",
    		29: "VIDEO_PLAY",
    	}
    	WidgetMarkup_Icon_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ICON_UNSPECIFIED":         0,
    		"AIRPLANE":                 1,
    		"BOOKMARK":                 26,
    		"BUS":                      25,
    		"CAR":                      9,
    		"CLOCK":                    2,
    		"CONFIRMATION_NUMBER_ICON": 12,
    		"DOLLAR":                   14,
    		"DESCRIPTION":              27,
    		"EMAIL":                    10,
    		"EVENT_PERFORMER":          20,
    		"EVENT_SEAT":               21,
    		"FLIGHT_ARRIVAL":           16,
    		"FLIGHT_DEPARTURE":         15,
    		"HOTEL":                    6,
    		"HOTEL_ROOM_TYPE":          17,
    		"INVITE":                   19,
    		"MAP_PIN":                  3,
    		"MEMBERSHIP":               24,
    		"MULTIPLE_PEOPLE":          18,
    		"OFFER":                    30,
    		"PERSON":                   11,
    		"PHONE":                    13,
    		"RESTAURANT_ICON":          7,
    		"SHOPPING_CART":            8,
    		"STAR":                     5,
    		"STORE":                    22,
    		"TICKET":                   4,
    		"TRAIN":                    23,
    		"VIDEO_CAMERA":             28,
    		"VIDEO_PLAY":               29,
    	}
    )

Enum value maps for WidgetMarkup_Icon.

### ChatService_ServiceDesc
    
    
    var ChatService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.chat.v1.ChatService",
    	HandlerType: (*ChatServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateMessage",
    			Handler:    _ChatService_CreateMessage_Handler,
    		},
    		{
    			MethodName: "ListMessages",
    			Handler:    _ChatService_ListMessages_Handler,
    		},
    		{
    			MethodName: "ListMemberships",
    			Handler:    _ChatService_ListMemberships_Handler,
    		},
    		{
    			MethodName: "GetMembership",
    			Handler:    _ChatService_GetMembership_Handler,
    		},
    		{
    			MethodName: "GetMessage",
    			Handler:    _ChatService_GetMessage_Handler,
    		},
    		{
    			MethodName: "UpdateMessage",
    			Handler:    _ChatService_UpdateMessage_Handler,
    		},
    		{
    			MethodName: "DeleteMessage",
    			Handler:    _ChatService_DeleteMessage_Handler,
    		},
    		{
    			MethodName: "SearchMessages",
    			Handler:    _ChatService_SearchMessages_Handler,
    		},
    		{
    			MethodName: "GetAttachment",
    			Handler:    _ChatService_GetAttachment_Handler,
    		},
    		{
    			MethodName: "UploadAttachment",
    			Handler:    _ChatService_UploadAttachment_Handler,
    		},
    		{
    			MethodName: "ListSpaces",
    			Handler:    _ChatService_ListSpaces_Handler,
    		},
    		{
    			MethodName: "SearchSpaces",
    			Handler:    _ChatService_SearchSpaces_Handler,
    		},
    		{
    			MethodName: "GetSpace",
    			Handler:    _ChatService_GetSpace_Handler,
    		},
    		{
    			MethodName: "CreateSpace",
    			Handler:    _ChatService_CreateSpace_Handler,
    		},
    		{
    			MethodName: "SetUpSpace",
    			Handler:    _ChatService_SetUpSpace_Handler,
    		},
    		{
    			MethodName: "UpdateSpace",
    			Handler:    _ChatService_UpdateSpace_Handler,
    		},
    		{
    			MethodName: "DeleteSpace",
    			Handler:    _ChatService_DeleteSpace_Handler,
    		},
    		{
    			MethodName: "CompleteImportSpace",
    			Handler:    _ChatService_CompleteImportSpace_Handler,
    		},
    		{
    			MethodName: "FindDirectMessage",
    			Handler:    _ChatService_FindDirectMessage_Handler,
    		},
    		{
    			MethodName: "FindGroupChats",
    			Handler:    _ChatService_FindGroupChats_Handler,
    		},
    		{
    			MethodName: "CreateMembership",
    			Handler:    _ChatService_CreateMembership_Handler,
    		},
    		{
    			MethodName: "UpdateMembership",
    			Handler:    _ChatService_UpdateMembership_Handler,
    		},
    		{
    			MethodName: "DeleteMembership",
    			Handler:    _ChatService_DeleteMembership_Handler,
    		},
    		{
    			MethodName: "CreateReaction",
    			Handler:    _ChatService_CreateReaction_Handler,
    		},
    		{
    			MethodName: "ListReactions",
    			Handler:    _ChatService_ListReactions_Handler,
    		},
    		{
    			MethodName: "DeleteReaction",
    			Handler:    _ChatService_DeleteReaction_Handler,
    		},
    		{
    			MethodName: "ListMessagePins",
    			Handler:    _ChatService_ListMessagePins_Handler,
    		},
    		{
    			MethodName: "CreateMessagePin",
    			Handler:    _ChatService_CreateMessagePin_Handler,
    		},
    		{
    			MethodName: "DeleteMessagePin",
    			Handler:    _ChatService_DeleteMessagePin_Handler,
    		},
    		{
    			MethodName: "CreateCustomEmoji",
    			Handler:    _ChatService_CreateCustomEmoji_Handler,
    		},
    		{
    			MethodName: "GetCustomEmoji",
    			Handler:    _ChatService_GetCustomEmoji_Handler,
    		},
    		{
    			MethodName: "ListCustomEmojis",
    			Handler:    _ChatService_ListCustomEmojis_Handler,
    		},
    		{
    			MethodName: "DeleteCustomEmoji",
    			Handler:    _ChatService_DeleteCustomEmoji_Handler,
    		},
    		{
    			MethodName: "GetSpaceReadState",
    			Handler:    _ChatService_GetSpaceReadState_Handler,
    		},
    		{
    			MethodName: "UpdateSpaceReadState",
    			Handler:    _ChatService_UpdateSpaceReadState_Handler,
    		},
    		{
    			MethodName: "GetThreadReadState",
    			Handler:    _ChatService_GetThreadReadState_Handler,
    		},
    		{
    			MethodName: "GetAvailability",
    			Handler:    _ChatService_GetAvailability_Handler,
    		},
    		{
    			MethodName: "MarkAsActive",
    			Handler:    _ChatService_MarkAsActive_Handler,
    		},
    		{
    			MethodName: "MarkAsAway",
    			Handler:    _ChatService_MarkAsAway_Handler,
    		},
    		{
    			MethodName: "MarkAsDoNotDisturb",
    			Handler:    _ChatService_MarkAsDoNotDisturb_Handler,
    		},
    		{
    			MethodName: "UpdateAvailability",
    			Handler:    _ChatService_UpdateAvailability_Handler,
    		},
    		{
    			MethodName: "GetSpaceEvent",
    			Handler:    _ChatService_GetSpaceEvent_Handler,
    		},
    		{
    			MethodName: "ListSpaceEvents",
    			Handler:    _ChatService_ListSpaceEvents_Handler,
    		},
    		{
    			MethodName: "GetSpaceNotificationSetting",
    			Handler:    _ChatService_GetSpaceNotificationSetting_Handler,
    		},
    		{
    			MethodName: "UpdateSpaceNotificationSetting",
    			Handler:    _ChatService_UpdateSpaceNotificationSetting_Handler,
    		},
    		{
    			MethodName: "CreateSection",
    			Handler:    _ChatService_CreateSection_Handler,
    		},
    		{
    			MethodName: "DeleteSection",
    			Handler:    _ChatService_DeleteSection_Handler,
    		},
    		{
    			MethodName: "UpdateSection",
    			Handler:    _ChatService_UpdateSection_Handler,
    		},
    		{
    			MethodName: "ListSections",
    			Handler:    _ChatService_ListSections_Handler,
    		},
    		{
    			MethodName: "PositionSection",
    			Handler:    _ChatService_PositionSection_Handler,
    		},
    		{
    			MethodName: "ListSectionItems",
    			Handler:    _ChatService_ListSectionItems_Handler,
    		},
    		{
    			MethodName: "MoveSectionItem",
    			Handler:    _ChatService_MoveSectionItem_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/chat/v1/chat_service.proto",
    }

ChatService_ServiceDesc is the grpc.ServiceDesc for ChatService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_chat_v1_action_status_proto
    
    
    var File_google_chat_v1_action_status_proto protoreflect.FileDescriptor

### File_google_chat_v1_annotation_proto
    
    
    var File_google_chat_v1_annotation_proto protoreflect.FileDescriptor

### File_google_chat_v1_app_command_metadata_proto
    
    
    var File_google_chat_v1_app_command_metadata_proto protoreflect.FileDescriptor

### File_google_chat_v1_attachment_proto
    
    
    var File_google_chat_v1_attachment_proto protoreflect.FileDescriptor

### File_google_chat_v1_audience_proto
    
    
    var File_google_chat_v1_audience_proto protoreflect.FileDescriptor

### File_google_chat_v1_availability_proto
    
    
    var File_google_chat_v1_availability_proto protoreflect.FileDescriptor

### File_google_chat_v1_chat_service_proto
    
    
    var File_google_chat_v1_chat_service_proto protoreflect.FileDescriptor

### File_google_chat_v1_contextual_addon_proto
    
    
    var File_google_chat_v1_contextual_addon_proto protoreflect.FileDescriptor

### File_google_chat_v1_deletion_metadata_proto
    
    
    var File_google_chat_v1_deletion_metadata_proto protoreflect.FileDescriptor

### File_google_chat_v1_event_payload_proto
    
    
    var File_google_chat_v1_event_payload_proto protoreflect.FileDescriptor

### File_google_chat_v1_group_proto
    
    
    var File_google_chat_v1_group_proto protoreflect.FileDescriptor

### File_google_chat_v1_history_state_proto
    
    
    var File_google_chat_v1_history_state_proto protoreflect.FileDescriptor

### File_google_chat_v1_markup_syntax_proto
    
    
    var File_google_chat_v1_markup_syntax_proto protoreflect.FileDescriptor

### File_google_chat_v1_matched_url_proto
    
    
    var File_google_chat_v1_matched_url_proto protoreflect.FileDescriptor

### File_google_chat_v1_membership_proto
    
    
    var File_google_chat_v1_membership_proto protoreflect.FileDescriptor

### File_google_chat_v1_message_pin_proto
    
    
    var File_google_chat_v1_message_pin_proto protoreflect.FileDescriptor

### File_google_chat_v1_message_proto
    
    
    var File_google_chat_v1_message_proto protoreflect.FileDescriptor

### File_google_chat_v1_reaction_proto
    
    
    var File_google_chat_v1_reaction_proto protoreflect.FileDescriptor

### File_google_chat_v1_section_proto
    
    
    var File_google_chat_v1_section_proto protoreflect.FileDescriptor

### File_google_chat_v1_slash_command_proto
    
    
    var File_google_chat_v1_slash_command_proto protoreflect.FileDescriptor

### File_google_chat_v1_space_event_proto
    
    
    var File_google_chat_v1_space_event_proto protoreflect.FileDescriptor

### File_google_chat_v1_space_notification_setting_proto
    
    
    var File_google_chat_v1_space_notification_setting_proto protoreflect.FileDescriptor

### File_google_chat_v1_space_proto
    
    
    var File_google_chat_v1_space_proto protoreflect.FileDescriptor

### File_google_chat_v1_space_read_state_proto
    
    
    var File_google_chat_v1_space_read_state_proto protoreflect.FileDescriptor

### File_google_chat_v1_space_setup_proto
    
    
    var File_google_chat_v1_space_setup_proto protoreflect.FileDescriptor

### File_google_chat_v1_thread_read_state_proto
    
    
    var File_google_chat_v1_thread_read_state_proto protoreflect.FileDescriptor

### File_google_chat_v1_user_proto
    
    
    var File_google_chat_v1_user_proto protoreflect.FileDescriptor

### File_google_chat_v1_widgets_proto
    
    
    var File_google_chat_v1_widgets_proto protoreflect.FileDescriptor

## Functions 

### func RegisterChatServiceServer 
    
    
    func RegisterChatServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv ChatServiceServer)

## AccessoryWidget
    
    
    type AccessoryWidget struct {
    
    	// The type of action.
    	//
    	// Types that are valid to be assigned to Action:
    	//
    	//	*AccessoryWidget_ButtonList
    	Action isAccessoryWidget_Action `protobuf_oneof:"action"`
    	// contains filtered or unexported fields
    }

One or more interactive widgets that appear at the bottom of a message. For details, see [Add interactive widgets at the bottom of a message](https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets).

### func (*AccessoryWidget) Descriptor 
    
    
    func (*AccessoryWidget) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccessoryWidget.ProtoReflect.Descriptor instead.

### func (*AccessoryWidget) GetAction 
    
    
    func (x *AccessoryWidget) GetAction() isAccessoryWidget_Action

### func (*AccessoryWidget) GetButtonList 
    
    
    func (x *AccessoryWidget) GetButtonList() *[v1](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1).[ButtonList](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1#ButtonList)

### func (*AccessoryWidget) ProtoMessage 
    
    
    func (*AccessoryWidget) ProtoMessage()

### func (*AccessoryWidget) ProtoReflect 
    
    
    func (x *AccessoryWidget) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccessoryWidget) Reset 
    
    
    func (x *AccessoryWidget) Reset()

### func (*AccessoryWidget) String 
    
    
    func (x *AccessoryWidget) String() [string](https://pkg.go.dev/builtin#string)

## AccessoryWidget_ButtonList
    
    
    type AccessoryWidget_ButtonList struct {
    	// A list of buttons.
    	ButtonList *v1.ButtonList `protobuf:"bytes,1,opt,name=button_list,json=buttonList,proto3,oneof"`
    }

## ActionResponse
    
    
    type ActionResponse struct {
    
    	// Input only. The type of Chat app response.
    	Type ActionResponse_ResponseType `protobuf:"varint,1,opt,name=type,proto3,enum=google.chat.v1.ActionResponse_ResponseType" json:"type,omitempty"`
    	// Input only. URL for users to authenticate or configure. (Only for
    	// `REQUEST_CONFIG` response types.)
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=url,proto3" json:"url,omitempty"`
    	// Input only. A response to an interaction event related to a
    	// [dialog](https://developers.google.com/workspace/chat/dialogs). Must be
    	// accompanied by `ResponseType.Dialog`.
    	DialogAction *DialogAction `protobuf:"bytes,3,opt,name=dialog_action,json=dialogAction,proto3" json:"dialog_action,omitempty"`
    	// Input only. The response of the updated widget.
    	UpdatedWidget *ActionResponse_UpdatedWidget `protobuf:"bytes,4,opt,name=updated_widget,json=updatedWidget,proto3" json:"updated_widget,omitempty"`
    	// contains filtered or unexported fields
    }

Parameters that a Chat app can use to configure how its response is posted.

### func (*ActionResponse) Descriptor 
    
    
    func (*ActionResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ActionResponse.ProtoReflect.Descriptor instead.

### func (*ActionResponse) GetDialogAction 
    
    
    func (x *ActionResponse) GetDialogAction() *DialogAction

### func (*ActionResponse) GetType 
    
    
    func (x *ActionResponse) GetType() ActionResponse_ResponseType

### func (*ActionResponse) GetUpdatedWidget 
    
    
    func (x *ActionResponse) GetUpdatedWidget() *ActionResponse_UpdatedWidget

### func (*ActionResponse) GetUrl 
    
    
    func (x *ActionResponse) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*ActionResponse) ProtoMessage 
    
    
    func (*ActionResponse) ProtoMessage()

### func (*ActionResponse) ProtoReflect 
    
    
    func (x *ActionResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ActionResponse) Reset 
    
    
    func (x *ActionResponse) Reset()

### func (*ActionResponse) String 
    
    
    func (x *ActionResponse) String() [string](https://pkg.go.dev/builtin#string)

## ActionResponse_ResponseType
    
    
    type ActionResponse_ResponseType [int32](https://pkg.go.dev/builtin#int32)

The type of Chat app response.

### ActionResponse_TYPE_UNSPECIFIED, ActionResponse_NEW_MESSAGE, ActionResponse_UPDATE_MESSAGE, ActionResponse_UPDATE_USER_MESSAGE_CARDS, ActionResponse_REQUEST_CONFIG, ActionResponse_DIALOG, ActionResponse_UPDATE_WIDGET
    
    
    const (
    	// Default type that's handled as `NEW_MESSAGE`.
    	ActionResponse_TYPE_UNSPECIFIED ActionResponse_ResponseType = 0
    	// Post as a new message in the topic.
    	ActionResponse_NEW_MESSAGE ActionResponse_ResponseType = 1
    	// Update the Chat app's message. This is only permitted on a `CARD_CLICKED`
    	// event where the message sender type is `BOT`.
    	ActionResponse_UPDATE_MESSAGE ActionResponse_ResponseType = 2
    	// Update the cards on a user's message. This is only permitted as a
    	// response to a `MESSAGE` event with a matched url, or a `CARD_CLICKED`
    	// event where the message sender type is `HUMAN`. Text is ignored.
    	ActionResponse_UPDATE_USER_MESSAGE_CARDS ActionResponse_ResponseType = 6
    	// Privately ask the user for additional authentication or configuration.
    	ActionResponse_REQUEST_CONFIG ActionResponse_ResponseType = 3
    	// Presents a
    	// [dialog](https://developers.google.com/workspace/chat/dialogs).
    	ActionResponse_DIALOG ActionResponse_ResponseType = 4
    	// Widget text autocomplete options query.
    	ActionResponse_UPDATE_WIDGET ActionResponse_ResponseType = 7
    )

### func (ActionResponse_ResponseType) Descriptor 
    
    
    func (ActionResponse_ResponseType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ActionResponse_ResponseType) Enum 
    
    
    func (x ActionResponse_ResponseType) Enum() *ActionResponse_ResponseType

### func (ActionResponse_ResponseType) EnumDescriptor 
    
    
    func (ActionResponse_ResponseType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ActionResponse_ResponseType.Descriptor instead.

### func (ActionResponse_ResponseType) Number 
    
    
    func (x ActionResponse_ResponseType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ActionResponse_ResponseType) String 
    
    
    func (x ActionResponse_ResponseType) String() [string](https://pkg.go.dev/builtin#string)

### func (ActionResponse_ResponseType) Type 
    
    
    func (ActionResponse_ResponseType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ActionResponse_SelectionItems
    
    
    type ActionResponse_SelectionItems struct {
    
    	// An array of the SelectionItem objects.
    	Items []*v1.SelectionInput_SelectionItem `protobuf:"bytes,1,rep,name=items,proto3" json:"items,omitempty"`
    	// contains filtered or unexported fields
    }

List of widget autocomplete results.

### func (*ActionResponse_SelectionItems) Descriptor 
    
    
    func (*ActionResponse_SelectionItems) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ActionResponse_SelectionItems.ProtoReflect.Descriptor instead.

### func (*ActionResponse_SelectionItems) GetItems 
    
    
    func (x *ActionResponse_SelectionItems) GetItems() []*[v1](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1).[SelectionInput_SelectionItem](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1#SelectionInput_SelectionItem)

### func (*ActionResponse_SelectionItems) ProtoMessage 
    
    
    func (*ActionResponse_SelectionItems) ProtoMessage()

### func (*ActionResponse_SelectionItems) ProtoReflect 
    
    
    func (x *ActionResponse_SelectionItems) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ActionResponse_SelectionItems) Reset 
    
    
    func (x *ActionResponse_SelectionItems) Reset()

### func (*ActionResponse_SelectionItems) String 
    
    
    func (x *ActionResponse_SelectionItems) String() [string](https://pkg.go.dev/builtin#string)

## ActionResponse_UpdatedWidget
    
    
    type ActionResponse_UpdatedWidget struct {
    
    	// The widget updated in response to a user action.
    	//
    	// Types that are valid to be assigned to UpdatedWidget:
    	//
    	//	*ActionResponse_UpdatedWidget_Suggestions
    	UpdatedWidget isActionResponse_UpdatedWidget_UpdatedWidget `protobuf_oneof:"updated_widget"`
    	// The ID of the updated widget. The ID must match the one for the
    	// widget that triggered the update request.
    	Widget [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=widget,proto3" json:"widget,omitempty"`
    	// contains filtered or unexported fields
    }

For `selectionInput` widgets, returns autocomplete suggestions for a multiselect menu.

### func (*ActionResponse_UpdatedWidget) Descriptor 
    
    
    func (*ActionResponse_UpdatedWidget) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ActionResponse_UpdatedWidget.ProtoReflect.Descriptor instead.

### func (*ActionResponse_UpdatedWidget) GetSuggestions 
    
    
    func (x *ActionResponse_UpdatedWidget) GetSuggestions() *ActionResponse_SelectionItems

### func (*ActionResponse_UpdatedWidget) GetUpdatedWidget 
    
    
    func (x *ActionResponse_UpdatedWidget) GetUpdatedWidget() isActionResponse_UpdatedWidget_UpdatedWidget

### func (*ActionResponse_UpdatedWidget) GetWidget 
    
    
    func (x *ActionResponse_UpdatedWidget) GetWidget() [string](https://pkg.go.dev/builtin#string)

### func (*ActionResponse_UpdatedWidget) ProtoMessage 
    
    
    func (*ActionResponse_UpdatedWidget) ProtoMessage()

### func (*ActionResponse_UpdatedWidget) ProtoReflect 
    
    
    func (x *ActionResponse_UpdatedWidget) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ActionResponse_UpdatedWidget) Reset 
    
    
    func (x *ActionResponse_UpdatedWidget) Reset()

### func (*ActionResponse_UpdatedWidget) String 
    
    
    func (x *ActionResponse_UpdatedWidget) String() [string](https://pkg.go.dev/builtin#string)

## ActionResponse_UpdatedWidget_Suggestions
    
    
    type ActionResponse_UpdatedWidget_Suggestions struct {
    	// List of widget autocomplete results
    	Suggestions *ActionResponse_SelectionItems `protobuf:"bytes,1,opt,name=suggestions,proto3,oneof"`
    }

## ActionStatus
    
    
    type ActionStatus struct {
    
    	// The status code.
    	StatusCode code.Code `protobuf:"varint,1,opt,name=status_code,json=statusCode,proto3,enum=google.rpc.Code" json:"status_code,omitempty"`
    	// The message to send users about the status of their request.
    	// If unset, a generic message based on the `status_code` is sent.
    	UserFacingMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=user_facing_message,json=userFacingMessage,proto3" json:"user_facing_message,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the status for a request to either invoke or submit a [dialog](https://developers.google.com/workspace/chat/dialogs).

### func (*ActionStatus) Descriptor 
    
    
    func (*ActionStatus) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ActionStatus.ProtoReflect.Descriptor instead.

### func (*ActionStatus) GetStatusCode 
    
    
    func (x *ActionStatus) GetStatusCode() [code](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/code).[Code](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/code#Code)

### func (*ActionStatus) GetUserFacingMessage 
    
    
    func (x *ActionStatus) GetUserFacingMessage() [string](https://pkg.go.dev/builtin#string)

### func (*ActionStatus) ProtoMessage 
    
    
    func (*ActionStatus) ProtoMessage()

### func (*ActionStatus) ProtoReflect 
    
    
    func (x *ActionStatus) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ActionStatus) Reset 
    
    
    func (x *ActionStatus) Reset()

### func (*ActionStatus) String 
    
    
    func (x *ActionStatus) String() [string](https://pkg.go.dev/builtin#string)

## Annotation
    
    
    type Annotation struct {
    
    	// The type of this annotation.
    	Type AnnotationType `protobuf:"varint,1,opt,name=type,proto3,enum=google.chat.v1.AnnotationType" json:"type,omitempty"`
    	// Start index (0-based, inclusive) in the plain-text message body this
    	// annotation corresponds to.
    	StartIndex *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=start_index,json=startIndex,proto3,oneof" json:"start_index,omitempty"`
    	// Length of the substring in the plain-text message body this annotation
    	// corresponds to. If not present, indicates a length of 0.
    	Length [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=length,proto3" json:"length,omitempty"`
    	// Additional metadata about the annotation.
    	//
    	// Types that are valid to be assigned to Metadata:
    	//
    	//	*Annotation_UserMention
    	//	*Annotation_SlashCommand
    	//	*Annotation_RichLinkMetadata
    	//	*Annotation_CustomEmojiMetadata
    	Metadata isAnnotation_Metadata `protobuf_oneof:"metadata"`
    	// contains filtered or unexported fields
    }

Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0. To add basic formatting to a text message, see [Format text messages](https://developers.google.com/workspace/chat/format-messages).

Example plain-text message body:
    
    
    Hello @FooBot how are you!"
    

The corresponding annotations metadata:
    
    
        "annotations":[{
          "type":"USER_MENTION",
          "startIndex":6,
          "length":7,
          "userMention": {
            "user": {
              "name":"users/{user}",
              "displayName":"FooBot",
              "avatarUrl":"https://goo.gl/aeDtrS",
              "type":"BOT"
            },
            "type":"MENTION"
           }
        }]
    

### func (*Annotation) Descriptor 
    
    
    func (*Annotation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Annotation.ProtoReflect.Descriptor instead.

### func (*Annotation) GetCustomEmojiMetadata 
    
    
    func (x *Annotation) GetCustomEmojiMetadata() *CustomEmojiMetadata

### func (*Annotation) GetLength 
    
    
    func (x *Annotation) GetLength() [int32](https://pkg.go.dev/builtin#int32)

### func (*Annotation) GetMetadata 
    
    
    func (x *Annotation) GetMetadata() isAnnotation_Metadata

### func (*Annotation) GetRichLinkMetadata 
    
    
    func (x *Annotation) GetRichLinkMetadata() *RichLinkMetadata

### func (*Annotation) GetSlashCommand 
    
    
    func (x *Annotation) GetSlashCommand() *SlashCommandMetadata

### func (*Annotation) GetStartIndex 
    
    
    func (x *Annotation) GetStartIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*Annotation) GetType 
    
    
    func (x *Annotation) GetType() AnnotationType

### func (*Annotation) GetUserMention 
    
    
    func (x *Annotation) GetUserMention() *UserMentionMetadata

### func (*Annotation) ProtoMessage 
    
    
    func (*Annotation) ProtoMessage()

### func (*Annotation) ProtoReflect 
    
    
    func (x *Annotation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Annotation) Reset 
    
    
    func (x *Annotation) Reset()

### func (*Annotation) String 
    
    
    func (x *Annotation) String() [string](https://pkg.go.dev/builtin#string)

## AnnotationType
    
    
    type AnnotationType [int32](https://pkg.go.dev/builtin#int32)

Type of the annotation.

### AnnotationType_ANNOTATION_TYPE_UNSPECIFIED, AnnotationType_USER_MENTION, AnnotationType_SLASH_COMMAND, AnnotationType_RICH_LINK, AnnotationType_CUSTOM_EMOJI
    
    
    const (
    	// Default value for the enum. Don't use.
    	AnnotationType_ANNOTATION_TYPE_UNSPECIFIED AnnotationType = 0
    	// A user is mentioned.
    	AnnotationType_USER_MENTION AnnotationType = 1
    	// A slash command is invoked.
    	AnnotationType_SLASH_COMMAND AnnotationType = 2
    	// A rich link annotation.
    	AnnotationType_RICH_LINK AnnotationType = 3
    	// A custom emoji annotation.
    	AnnotationType_CUSTOM_EMOJI AnnotationType = 4
    )

### func (AnnotationType) Descriptor 
    
    
    func (AnnotationType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AnnotationType) Enum 
    
    
    func (x AnnotationType) Enum() *AnnotationType

### func (AnnotationType) EnumDescriptor 
    
    
    func (AnnotationType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotationType.Descriptor instead.

### func (AnnotationType) Number 
    
    
    func (x AnnotationType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AnnotationType) String 
    
    
    func (x AnnotationType) String() [string](https://pkg.go.dev/builtin#string)

### func (AnnotationType) Type 
    
    
    func (AnnotationType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Annotation_CustomEmojiMetadata
    
    
    type Annotation_CustomEmojiMetadata struct {
    	// The metadata for a custom emoji.
    	CustomEmojiMetadata *CustomEmojiMetadata `protobuf:"bytes,7,opt,name=custom_emoji_metadata,json=customEmojiMetadata,proto3,oneof"`
    }

## Annotation_RichLinkMetadata
    
    
    type Annotation_RichLinkMetadata struct {
    	// The metadata for a rich link.
    	RichLinkMetadata *RichLinkMetadata `protobuf:"bytes,6,opt,name=rich_link_metadata,json=richLinkMetadata,proto3,oneof"`
    }

## Annotation_SlashCommand
    
    
    type Annotation_SlashCommand struct {
    	// The metadata for a slash command.
    	SlashCommand *SlashCommandMetadata `protobuf:"bytes,5,opt,name=slash_command,json=slashCommand,proto3,oneof"`
    }

## Annotation_UserMention
    
    
    type Annotation_UserMention struct {
    	// The metadata of user mention.
    	UserMention *UserMentionMetadata `protobuf:"bytes,4,opt,name=user_mention,json=userMention,proto3,oneof"`
    }

## AppCommandMetadata
    
    
    type AppCommandMetadata struct {
    
    	// The ID for the command specified in the Chat API configuration.
    	AppCommandId [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=app_command_id,json=appCommandId,proto3" json:"app_command_id,omitempty"`
    	// The type of Chat app command.
    	AppCommandType AppCommandMetadata_AppCommandType `protobuf:"varint,2,opt,name=app_command_type,json=appCommandType,proto3,enum=google.chat.v1.AppCommandMetadata_AppCommandType" json:"app_command_type,omitempty"`
    	// contains filtered or unexported fields
    }

Metadata about a [Chat app command](https://developers.google.com/workspace/chat/commands).

### func (*AppCommandMetadata) Descriptor 
    
    
    func (*AppCommandMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppCommandMetadata.ProtoReflect.Descriptor instead.

### func (*AppCommandMetadata) GetAppCommandId 
    
    
    func (x *AppCommandMetadata) GetAppCommandId() [int32](https://pkg.go.dev/builtin#int32)

### func (*AppCommandMetadata) GetAppCommandType 
    
    
    func (x *AppCommandMetadata) GetAppCommandType() AppCommandMetadata_AppCommandType

### func (*AppCommandMetadata) ProtoMessage 
    
    
    func (*AppCommandMetadata) ProtoMessage()

### func (*AppCommandMetadata) ProtoReflect 
    
    
    func (x *AppCommandMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AppCommandMetadata) Reset 
    
    
    func (x *AppCommandMetadata) Reset()

### func (*AppCommandMetadata) String 
    
    
    func (x *AppCommandMetadata) String() [string](https://pkg.go.dev/builtin#string)

## AppCommandMetadata_AppCommandType
    
    
    type AppCommandMetadata_AppCommandType [int32](https://pkg.go.dev/builtin#int32)

The type of Chat app command. For details, see [Types of Chat app commands](https://developers.google.com/workspace/chat/commands#types).

### AppCommandMetadata_APP_COMMAND_TYPE_UNSPECIFIED, AppCommandMetadata_SLASH_COMMAND, AppCommandMetadata_QUICK_COMMAND, AppCommandMetadata_MESSAGE_ACTION
    
    
    const (
    	// Default value. Unspecified.
    	AppCommandMetadata_APP_COMMAND_TYPE_UNSPECIFIED AppCommandMetadata_AppCommandType = 0
    	// A slash command. The user sends the command in a Chat message.
    	AppCommandMetadata_SLASH_COMMAND AppCommandMetadata_AppCommandType = 1
    	// A quick command. The user selects the command from the Chat menu
    	// in the message reply area.
    	AppCommandMetadata_QUICK_COMMAND AppCommandMetadata_AppCommandType = 3
    	// A message action. The user selects the command from the message context
    	// menu in Chat.
    	AppCommandMetadata_MESSAGE_ACTION AppCommandMetadata_AppCommandType = 4
    )

### func (AppCommandMetadata_AppCommandType) Descriptor 
    
    
    func (AppCommandMetadata_AppCommandType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AppCommandMetadata_AppCommandType) Enum 
    
    
    func (x AppCommandMetadata_AppCommandType) Enum() *AppCommandMetadata_AppCommandType

### func (AppCommandMetadata_AppCommandType) EnumDescriptor 
    
    
    func (AppCommandMetadata_AppCommandType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppCommandMetadata_AppCommandType.Descriptor instead.

### func (AppCommandMetadata_AppCommandType) Number 
    
    
    func (x AppCommandMetadata_AppCommandType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AppCommandMetadata_AppCommandType) String 
    
    
    func (x AppCommandMetadata_AppCommandType) String() [string](https://pkg.go.dev/builtin#string)

### func (AppCommandMetadata_AppCommandType) Type 
    
    
    func (AppCommandMetadata_AppCommandType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AttachedGif
    
    
    type AttachedGif struct {
    
    	// Output only. The URL that hosts the GIF image.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// contains filtered or unexported fields
    }

A GIF image that's specified by a URL.

### func (*AttachedGif) Descriptor 
    
    
    func (*AttachedGif) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AttachedGif.ProtoReflect.Descriptor instead.

### func (*AttachedGif) GetUri 
    
    
    func (x *AttachedGif) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*AttachedGif) ProtoMessage 
    
    
    func (*AttachedGif) ProtoMessage()

### func (*AttachedGif) ProtoReflect 
    
    
    func (x *AttachedGif) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AttachedGif) Reset 
    
    
    func (x *AttachedGif) Reset()

### func (*AttachedGif) String 
    
    
    func (x *AttachedGif) String() [string](https://pkg.go.dev/builtin#string)

## Attachment
    
    
    type Attachment struct {
    
    	// Identifier. Resource name of the attachment.
    	//
    	// Format: `spaces/{space}/messages/{message}/attachments/{attachment}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The original file name for the content, not the full path.
    	ContentName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=content_name,json=contentName,proto3" json:"content_name,omitempty"`
    	// Output only. The content type (MIME type) of the file.
    	ContentType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=content_type,json=contentType,proto3" json:"content_type,omitempty"`
    	// The data reference to the attachment.
    	//
    	// Types that are valid to be assigned to DataRef:
    	//
    	//	*Attachment_AttachmentDataRef
    	//	*Attachment_DriveDataRef
    	DataRef isAttachment_DataRef `protobuf_oneof:"data_ref"`
    	// Output only. The thumbnail URL which should be used to preview the
    	// attachment to a human user. Chat apps shouldn't use this URL to download
    	// attachment content.
    	ThumbnailUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=thumbnail_uri,json=thumbnailUri,proto3" json:"thumbnail_uri,omitempty"`
    	// Output only. The download URL which should be used to allow a human user to
    	// download the attachment. Chat apps shouldn't use this URL to download
    	// attachment content.
    	DownloadUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=download_uri,json=downloadUri,proto3" json:"download_uri,omitempty"`
    	// Output only. The source of the attachment.
    	Source Attachment_Source `protobuf:"varint,9,opt,name=source,proto3,enum=google.chat.v1.Attachment_Source" json:"source,omitempty"`
    	// contains filtered or unexported fields
    }

An attachment in Google Chat.

### func (*Attachment) Descriptor 
    
    
    func (*Attachment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Attachment.ProtoReflect.Descriptor instead.

### func (*Attachment) GetAttachmentDataRef 
    
    
    func (x *Attachment) GetAttachmentDataRef() *AttachmentDataRef

### func (*Attachment) GetContentName 
    
    
    func (x *Attachment) GetContentName() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetContentType 
    
    
    func (x *Attachment) GetContentType() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetDataRef 
    
    
    func (x *Attachment) GetDataRef() isAttachment_DataRef

### func (*Attachment) GetDownloadUri 
    
    
    func (x *Attachment) GetDownloadUri() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetDriveDataRef 
    
    
    func (x *Attachment) GetDriveDataRef() *DriveDataRef

### func (*Attachment) GetName 
    
    
    func (x *Attachment) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetSource 
    
    
    func (x *Attachment) GetSource() Attachment_Source

### func (*Attachment) GetThumbnailUri 
    
    
    func (x *Attachment) GetThumbnailUri() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) ProtoMessage 
    
    
    func (*Attachment) ProtoMessage()

### func (*Attachment) ProtoReflect 
    
    
    func (x *Attachment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Attachment) Reset 
    
    
    func (x *Attachment) Reset()

### func (*Attachment) String 
    
    
    func (x *Attachment) String() [string](https://pkg.go.dev/builtin#string)

## AttachmentDataRef
    
    
    type AttachmentDataRef struct {
    
    	// Optional. The resource name of the attachment data. This field is used with
    	// the media API to download the attachment data.
    	ResourceName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=resource_name,json=resourceName,proto3" json:"resource_name,omitempty"`
    	// Optional. Opaque token containing a reference to an uploaded attachment.
    	// Treated by clients as an opaque string and used to create or update Chat
    	// messages with attachments.
    	AttachmentUploadToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=attachment_upload_token,json=attachmentUploadToken,proto3" json:"attachment_upload_token,omitempty"`
    	// contains filtered or unexported fields
    }

A reference to the attachment data.

### func (*AttachmentDataRef) Descriptor 
    
    
    func (*AttachmentDataRef) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AttachmentDataRef.ProtoReflect.Descriptor instead.

### func (*AttachmentDataRef) GetAttachmentUploadToken 
    
    
    func (x *AttachmentDataRef) GetAttachmentUploadToken() [string](https://pkg.go.dev/builtin#string)

### func (*AttachmentDataRef) GetResourceName 
    
    
    func (x *AttachmentDataRef) GetResourceName() [string](https://pkg.go.dev/builtin#string)

### func (*AttachmentDataRef) ProtoMessage 
    
    
    func (*AttachmentDataRef) ProtoMessage()

### func (*AttachmentDataRef) ProtoReflect 
    
    
    func (x *AttachmentDataRef) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AttachmentDataRef) Reset 
    
    
    func (x *AttachmentDataRef) Reset()

### func (*AttachmentDataRef) String 
    
    
    func (x *AttachmentDataRef) String() [string](https://pkg.go.dev/builtin#string)

## Attachment_AttachmentDataRef
    
    
    type Attachment_AttachmentDataRef struct {
    	// Optional. A reference to the attachment data. This field is used to
    	// create or update messages with attachments, or with the media API to
    	// download the attachment data.
    	AttachmentDataRef *AttachmentDataRef `protobuf:"bytes,4,opt,name=attachment_data_ref,json=attachmentDataRef,proto3,oneof"`
    }

## Attachment_DriveDataRef
    
    
    type Attachment_DriveDataRef struct {
    	// Output only. A reference to the Google Drive attachment. This field is
    	// used with the Google Drive API.
    	DriveDataRef *DriveDataRef `protobuf:"bytes,7,opt,name=drive_data_ref,json=driveDataRef,proto3,oneof"`
    }

## Attachment_Source
    
    
    type Attachment_Source [int32](https://pkg.go.dev/builtin#int32)

The source of the attachment.

### Attachment_SOURCE_UNSPECIFIED, Attachment_DRIVE_FILE, Attachment_UPLOADED_CONTENT
    
    
    const (
    	// Reserved.
    	Attachment_SOURCE_UNSPECIFIED Attachment_Source = 0
    	// The file is a Google Drive file.
    	Attachment_DRIVE_FILE Attachment_Source = 1
    	// The file is uploaded to Chat.
    	Attachment_UPLOADED_CONTENT Attachment_Source = 2
    )

### func (Attachment_Source) Descriptor 
    
    
    func (Attachment_Source) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Attachment_Source) Enum 
    
    
    func (x Attachment_Source) Enum() *Attachment_Source

### func (Attachment_Source) EnumDescriptor 
    
    
    func (Attachment_Source) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Attachment_Source.Descriptor instead.

### func (Attachment_Source) Number 
    
    
    func (x Attachment_Source) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Attachment_Source) String 
    
    
    func (x Attachment_Source) String() [string](https://pkg.go.dev/builtin#string)

### func (Attachment_Source) Type 
    
    
    func (Attachment_Source) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Audience
    
    
    type Audience struct {
    
    	// The resource name of the [target
    	// audience](https://support.google.com/a/answer/9934697) who can discover
    	// or join the space. For details, see [Make a space
    	// discoverable to a target
    	// audience](https://developers.google.com/workspace/chat/space-target-audience).
    	// Format: `audiences/{audience}`
    	//
    	// To use the default target audience for the Google Workspace organization,
    	// set to `audiences/default`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A target audience in Google Chat. A target audience represents a group of users within a Google Workspace organization, defined by an administrator. Target audiences are used to configure access and visibility settings for resources, such as making a space discoverable to a specific group of users.

For more details, see [Target audiences](https://support.google.com/a/answer/9934697) and [Make a space discoverable to a target audience](https://developers.google.com/workspace/chat/space-target-audience).

### func (*Audience) Descriptor 
    
    
    func (*Audience) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Audience.ProtoReflect.Descriptor instead.

### func (*Audience) GetName 
    
    
    func (x *Audience) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Audience) ProtoMessage 
    
    
    func (*Audience) ProtoMessage()

### func (*Audience) ProtoReflect 
    
    
    func (x *Audience) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Audience) Reset 
    
    
    func (x *Audience) Reset()

### func (*Audience) String 
    
    
    func (x *Audience) String() [string](https://pkg.go.dev/builtin#string)

## Availability
    
    
    type Availability struct {
    
    	// Identifier. Resource name of the user's availability.
    	//
    	// Format: `users/{user}/availability`
    	//
    	// `{user}` is the id for the Person in the People API or Admin SDK directory
    	// API. For example, `users/123456789`.
    	//
    	// The user's email address or `me` can also be used as an alias to refer to
    	// the caller.  For example, `users/user@example.com` or `users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The user's current availability state.
    	State Availability_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.chat.v1.Availability_State" json:"state,omitempty"`
    	// Additional metadata associated with the user's availability state.
    	//
    	// Types that are valid to be assigned to StateMetadata:
    	//
    	//	*Availability_DoNotDisturbMetadata
    	StateMetadata isAvailability_StateMetadata `protobuf_oneof:"state_metadata"`
    	// Optional. The user's custom status.
    	CustomStatus *CustomStatus `protobuf:"bytes,4,opt,name=custom_status,json=customStatus,proto3" json:"custom_status,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a user's current availability information in Google Chat, including their state (for example, Active, Away, Do Not Disturb) and any custom status.

### func (*Availability) Descriptor 
    
    
    func (*Availability) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Availability.ProtoReflect.Descriptor instead.

### func (*Availability) GetCustomStatus 
    
    
    func (x *Availability) GetCustomStatus() *CustomStatus

### func (*Availability) GetDoNotDisturbMetadata 
    
    
    func (x *Availability) GetDoNotDisturbMetadata() *DoNotDisturbMetadata

### func (*Availability) GetName 
    
    
    func (x *Availability) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Availability) GetState 
    
    
    func (x *Availability) GetState() Availability_State

### func (*Availability) GetStateMetadata 
    
    
    func (x *Availability) GetStateMetadata() isAvailability_StateMetadata

### func (*Availability) ProtoMessage 
    
    
    func (*Availability) ProtoMessage()

### func (*Availability) ProtoReflect 
    
    
    func (x *Availability) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Availability) Reset 
    
    
    func (x *Availability) Reset()

### func (*Availability) String 
    
    
    func (x *Availability) String() [string](https://pkg.go.dev/builtin#string)

## Availability_DoNotDisturbMetadata
    
    
    type Availability_DoNotDisturbMetadata struct {
    	// Output only. Metadata if the user state is set to DO_NOT_DISTURB.
    	DoNotDisturbMetadata *DoNotDisturbMetadata `protobuf:"bytes,3,opt,name=do_not_disturb_metadata,json=doNotDisturbMetadata,proto3,oneof"`
    }

## Availability_State
    
    
    type Availability_State [int32](https://pkg.go.dev/builtin#int32)

Represents the current availability state of the user.

### Availability_STATE_UNSPECIFIED, Availability_ACTIVE, Availability_IDLE, Availability_AWAY, Availability_DO_NOT_DISTURB
    
    
    const (
    	// Default value. The state is unspecified.
    	Availability_STATE_UNSPECIFIED Availability_State = 0
    	// The user is currently active, based on recent activity.
    	Availability_ACTIVE Availability_State = 1
    	// The user is currently idle. This state indicates a period of inactivity
    	// after being ACTIVE, before potentially transitioning to AWAY.
    	Availability_IDLE Availability_State = 2
    	// The user is currently away. This can be either automatically set after
    	// a period of inactivity in ACTIVE or IDLE state, or it can be manually set
    	// by the user. When manually set via `MarkAsAway`, this state persists
    	// regardless of user activity.
    	Availability_AWAY Availability_State = 3
    	// The user is in Do Not Disturb state, which is manually set.
    	Availability_DO_NOT_DISTURB Availability_State = 4
    )

### func (Availability_State) Descriptor 
    
    
    func (Availability_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Availability_State) Enum 
    
    
    func (x Availability_State) Enum() *Availability_State

### func (Availability_State) EnumDescriptor 
    
    
    func (Availability_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Availability_State.Descriptor instead.

### func (Availability_State) Number 
    
    
    func (x Availability_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Availability_State) String 
    
    
    func (x Availability_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Availability_State) Type 
    
    
    func (Availability_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CalendarEventLinkData
    
    
    type CalendarEventLinkData struct {
    
    	// The [Calendar
    	// identifier](https://developers.google.com/workspace/calendar/api/v3/reference/calendars)
    	// of the linked Calendar.
    	CalendarId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=calendar_id,json=calendarId,proto3" json:"calendar_id,omitempty"`
    	// The [Event
    	// identifier](https://developers.google.com/workspace/calendar/api/v3/reference/events)
    	// of the linked Calendar event.
    	EventId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
    	// contains filtered or unexported fields
    }

Data for Calendar event links.

### func (*CalendarEventLinkData) Descriptor 
    
    
    func (*CalendarEventLinkData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CalendarEventLinkData.ProtoReflect.Descriptor instead.

### func (*CalendarEventLinkData) GetCalendarId 
    
    
    func (x *CalendarEventLinkData) GetCalendarId() [string](https://pkg.go.dev/builtin#string)

### func (*CalendarEventLinkData) GetEventId 
    
    
    func (x *CalendarEventLinkData) GetEventId() [string](https://pkg.go.dev/builtin#string)

### func (*CalendarEventLinkData) ProtoMessage 
    
    
    func (*CalendarEventLinkData) ProtoMessage()

### func (*CalendarEventLinkData) ProtoReflect 
    
    
    func (x *CalendarEventLinkData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CalendarEventLinkData) Reset 
    
    
    func (x *CalendarEventLinkData) Reset()

### func (*CalendarEventLinkData) String 
    
    
    func (x *CalendarEventLinkData) String() [string](https://pkg.go.dev/builtin#string)

## CardWithId
    
    
    type CardWithId struct {
    
    	// Required if the message contains multiple cards. A unique identifier for
    	// a card in a message.
    	CardId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=card_id,json=cardId,proto3" json:"card_id,omitempty"`
    	// A card. Maximum size is 32 KB.
    	Card *v1.Card `protobuf:"bytes,2,opt,name=card,proto3" json:"card,omitempty"`
    	// contains filtered or unexported fields
    }

A [card](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards) in a Google Chat message.

Chat apps can create cards with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). As part of the [Developer Preview Program](https://developers.google.com/workspace/preview), if your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), it can create card messages. If your Chat app is not part of Developer Preview Program, it can't create cards with user authentication.

To learn how to create a message that contains cards, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

[Card builder](https://addons.gsuite.google.com/uikit/builder)

### func (*CardWithId) Descriptor 
    
    
    func (*CardWithId) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CardWithId.ProtoReflect.Descriptor instead.

### func (*CardWithId) GetCard 
    
    
    func (x *CardWithId) GetCard() *[v1](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1).[Card](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1#Card)

### func (*CardWithId) GetCardId 
    
    
    func (x *CardWithId) GetCardId() [string](https://pkg.go.dev/builtin#string)

### func (*CardWithId) ProtoMessage 
    
    
    func (*CardWithId) ProtoMessage()

### func (*CardWithId) ProtoReflect 
    
    
    func (x *CardWithId) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CardWithId) Reset 
    
    
    func (x *CardWithId) Reset()

### func (*CardWithId) String 
    
    
    func (x *CardWithId) String() [string](https://pkg.go.dev/builtin#string)

## ChatServiceClient
    
    
    type ChatServiceClient interface {
    	// Creates a message in a Google Chat space. For an example, see [Send a
    	// message](https://developers.google.com/workspace/chat/create-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.create`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// Chat attributes the message sender differently depending on the type of
    	// authentication that you use in your request.
    	//
    	// The following image shows how Chat attributes a message when you use app
    	// authentication. Chat displays the Chat app as the message
    	// sender. The content of the message can contain text (`text`), cards
    	// (`cardsV2`), and accessory widgets (`accessoryWidgets`).
    	//
    	// ![Message sent with app
    	// authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)
    	//
    	// The following image shows how Chat attributes a message when you use user
    	// authentication. Chat displays the user as the message sender and attributes
    	// the Chat app to the message by displaying its name. The content of message
    	// can only contain text (`text`).
    	//
    	// ![Message sent with user
    	// authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)
    	//
    	// The maximum message size, including the message contents, is 32,000 bytes.
    	//
    	// For
    	// [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks)
    	// requests, the response doesn't contain the full message. The response only
    	// populates the `name` and `thread.name` fields in addition to the
    	// information that was in the request.
    	CreateMessage(ctx context.Context, in *CreateMessageRequest, opts ...grpc.CallOption) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Lists messages in a space that the caller is a member of, including
    	// messages from blocked members and spaces. System messages, like those
    	// announcing new space members, aren't included. If you list messages from a
    	// space with no messages, the response is an empty object. When using a
    	// REST/HTTP interface, the response contains an empty JSON object, `{}`.
    	// For an example, see
    	// [List
    	// messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`. When
    	//     using this authentication scope, this method only returns public
    	//     messages in a space. It doesn't include private messages.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	ListMessages(ctx context.Context, in *ListMessagesRequest, opts ...grpc.CallOption) (*ListMessagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists memberships in a space. For an example, see [List users and Google
    	// Chat apps in a
    	// space](https://developers.google.com/workspace/chat/list-members). Listing
    	// memberships with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// lists memberships in spaces that the Chat app has
    	// access to, but excludes Chat app memberships,
    	// including its own. Listing memberships with
    	// [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// lists memberships in spaces that the authenticated user has access to.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (requires
    	//     [administrator approval](https://support.google.com/a?p=chat-app-auth))
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	ListMemberships(ctx context.Context, in *ListMembershipsRequest, opts ...grpc.CallOption) (*ListMembershipsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a membership. For an example, see
    	// [Get details about a user's or Google Chat app's
    	// membership](https://developers.google.com/workspace/chat/get-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (requires
    	//     [administrator approval](https://support.google.com/a?p=chat-app-auth))
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	GetMembership(ctx context.Context, in *GetMembershipRequest, opts ...grpc.CallOption) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a message.
    	// For an example, see [Get details about a
    	// message](https://developers.google.com/workspace/chat/get-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`: When using this
    	//     authorization scope, this method returns details about a message the
    	//     Chat app has access to, like direct messages and [slash
    	//     commands](https://developers.google.com/workspace/chat/slash-commands)
    	//     that invoke the Chat app.
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//     with [administrator
    	//     approval](https://support.google.com/a?p=chat-app-auth).
    	//     When using this authentication scope,
    	//     this method returns details about a public message in a space.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//
    	// Note: Might return a message from a blocked member or space.
    	GetMessage(ctx context.Context, in *GetMessageRequest, opts ...grpc.CallOption) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Updates a message. There's a difference between the `patch` and `update`
    	// methods. The `patch`
    	// method uses a `patch` request while the `update` method uses a `put`
    	// request. We recommend using the `patch` method. For an example, see
    	// [Update a
    	// message](https://developers.google.com/workspace/chat/update-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When using app authentication, requests can only update messages
    	// created by the calling Chat app.
    	UpdateMessage(ctx context.Context, in *UpdateMessageRequest, opts ...grpc.CallOption) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a message.
    	// For an example, see [Delete a
    	// message](https://developers.google.com/workspace/chat/delete-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When using app authentication, requests can only delete messages
    	// created by the calling Chat app.
    	DeleteMessage(ctx context.Context, in *DeleteMessageRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Searches for messages in Google Chat that the calling user has access to.
    	// Returns a list of messages matching the search criteria.
    	//
    	// To search across all spaces the user has access to, set `parent` to
    	// `spaces/-`. Using any other value for `parent` results in an
    	// `INVALID_ARGUMENT` error. The returned messages have their `name` field
    	// populated with the full resource name, which includes the specific `space`
    	// in which the message resides.
    	//
    	// This API doesn't return all message types. The types of messages listed
    	// below aren't included in the response. Use
    	// [ListMessages][google.chat.v1.ChatService.ListMessages] to list all
    	// messages.
    	//
    	// - Private Messages that are visible to the authenticated user.
    	// - Messages posted by Chat apps in spaces or group chats.
    	// - Messages in a Chat app DM.
    	// - Messages from blocked users.
    	// - Messages in spaces that the caller has muted.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	SearchMessages(ctx context.Context, in *SearchMessagesRequest, opts ...grpc.CallOption) (*SearchMessagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of a message attachment. The attachment data is fetched
    	// using the [media
    	// API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download).
    	// For an example, see
    	// [Get metadata about a message
    	// attachment](https://developers.google.com/workspace/chat/get-media-attachments).
    	//
    	// Requires [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	GetAttachment(ctx context.Context, in *GetAttachmentRequest, opts ...grpc.CallOption) (*Attachment, [error](https://pkg.go.dev/builtin#error))
    	// Uploads an attachment. For an example, see
    	// [Upload media as a file
    	// attachment](https://developers.google.com/workspace/chat/upload-media-attachments).
    	//
    	// Requires user
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.create`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	//
    	// You can upload attachments up to 200 MB. Certain file types aren't
    	// supported. For details, see [File types blocked by Google
    	// Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat).
    	UploadAttachment(ctx context.Context, in *UploadAttachmentRequest, opts ...grpc.CallOption) (*UploadAttachmentResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists spaces the caller is a member of. Group chats and DMs aren't listed
    	// until the first message is sent. For an example, see
    	// [List
    	// spaces](https://developers.google.com/workspace/chat/list-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//
    	// To list all named spaces by Google Workspace organization, use the
    	// [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search)
    	// method using Workspace administrator privileges instead.
    	ListSpaces(ctx context.Context, in *ListSpacesRequest, opts ...grpc.CallOption) (*ListSpacesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of spaces in a Google Workspace organization. For an
    	// example, see [Search for and manage
    	// spaces](https://developers.google.com/workspace/chat/search-manage-admin).
    	//
    	// When `use_admin_access` is set to `false`, the results are limited to
    	// spaces where the calling user is a joined member. To search with
    	// administrator privileges, set `use_admin_access` to `true`.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//
    	// - [User
    	// authentication with administrator
    	// privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges)
    	// and one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	SearchSpaces(ctx context.Context, in *SearchSpacesRequest, opts ...grpc.CallOption) (*SearchSpacesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a space. For an example, see
    	// [Get details about a
    	// space](https://developers.google.com/workspace/chat/get-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces` with [administrator
    	//     approval](https://support.google.com/a?p=chat-app-auth)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	//
    	// App authentication has the following limitations:
    	//
    	// - `space.access_settings` is only populated when using the
    	// `chat.app.spaces` scope.
    	// - `space.predefind_permission_settings` and `space.permission_settings` are
    	// only populated when using the `chat.app.spaces` scope, and only for
    	// spaces the app created.
    	GetSpace(ctx context.Context, in *GetSpaceRequest, opts ...grpc.CallOption) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Creates a space. Can be used to create a named space, or a
    	// group chat in `Import mode`. For an example, see [Create a
    	// space](https://developers.google.com/workspace/chat/create-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When authenticating as an app, the `space.customer` field must be set in
    	// the request.
    	//
    	// When authenticating as an app, the Chat app is added as a member of the
    	// space. However, unlike human authentication, the Chat app is not added as a
    	// space manager. By default, the Chat app can be removed from the space by
    	// all space members. To allow only space managers to remove the app from a
    	// space, set `space.permission_settings.manage_apps` to `managers_allowed`.
    	//
    	// Space membership upon creation depends on whether the space is created in
    	// `Import mode`:
    	//
    	// * **Import mode:** No members are created.
    	// * **All other modes:**  The calling user is added as a member. This is:
    	//
    	//   - The app itself when using app authentication.
    	//
    	//   - The human user when using user authentication.
    	//
    	//     If you receive the error message `ALREADY_EXISTS` when creating
    	//     a space, try a different `displayName`. An existing space within
    	//     the Google Workspace organization might already use this display name.
    	CreateSpace(ctx context.Context, in *CreateSpaceRequest, opts ...grpc.CallOption) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Creates a space and adds specified users to it. The calling user is
    	// automatically added to the space, and shouldn't be specified as a
    	// membership in the request. For an example, see
    	// [Set up a space with initial
    	// members](https://developers.google.com/workspace/chat/set-up-spaces).
    	//
    	// To specify the human members to add, add memberships with the appropriate
    	// `membership.member.name`. To add a human user, use `users/{user}`, where
    	// `{user}` can be the email address for the user. For users in the same
    	// Workspace organization `{user}` can also be the `id` for the person from
    	// the People API, or the `id` for the user in the Directory API. For example,
    	// if the People API Person profile ID for `user@example.com` is `123456789`,
    	// you can add the user to the space by setting the `membership.member.name`
    	// to `users/user@example.com` or `users/123456789`.
    	//
    	// To specify the Google groups to add, add memberships with the
    	// appropriate `membership.group_member.name`. To add or invite a Google
    	// group, use `groups/{group}`, where `{group}` is the `id` for the group from
    	// the Cloud Identity Groups API. For example, you can use [Cloud Identity
    	// Groups lookup
    	// API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup)
    	// to retrieve the ID `123456789` for group email `group@example.com`, then
    	// you can add the group to the space by setting the
    	// `membership.group_member.name` to `groups/123456789`. Group email is not
    	// supported, and Google groups can only be added as members in named spaces.
    	//
    	// For a named space or group chat, if the caller blocks, or is blocked
    	// by some members, or doesn't have permission to add some members, then
    	// those members aren't added to the created space.
    	//
    	// To create a direct message (DM) between the calling user and another human
    	// user, specify exactly one membership to represent the human user. If
    	// one user blocks the other, the request fails and the DM isn't created.
    	//
    	// To create a DM between the calling user and the calling app, set
    	// `Space.singleUserBotDm` to `true` and don't specify any memberships. You
    	// can only use this method to set up a DM with the calling app. To add the
    	// calling app as a member of a space or an existing DM between two human
    	// users, see
    	// [Invite or add a user or app to a
    	// space](https://developers.google.com/workspace/chat/create-members).
    	//
    	// If a DM already exists between two users, even when one user blocks the
    	// other at the time a request is made, then the existing DM is returned.
    	//
    	// Spaces with threaded replies aren't supported. If you receive the error
    	// message `ALREADY_EXISTS` when setting up a space, try a different
    	// `displayName`. An existing space within the Google Workspace organization
    	// might already use this display name.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	SetUpSpace(ctx context.Context, in *SetUpSpaceRequest, opts ...grpc.CallOption) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Updates a space. For an example, see
    	// [Update a
    	// space](https://developers.google.com/workspace/chat/update-spaces).
    	//
    	// If you're updating the `displayName` field and receive the error message
    	// `ALREADY_EXISTS`, try a different display name.. An existing space within
    	// the Google Workspace organization might already use this display name.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	//
    	// App authentication has the following limitations:
    	//
    	// - To update either `space.predefined_permission_settings` or
    	// `space.permission_settings`, the app must be the space creator.
    	// - Updating the `space.access_settings.audience` is not supported for app
    	// authentication.
    	UpdateSpace(ctx context.Context, in *UpdateSpaceRequest, opts ...grpc.CallOption) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a named space. Always performs a cascading delete, which means
    	// that the space's child resources—like messages posted in the space and
    	// memberships in the space—are also deleted. For an example, see
    	// [Delete a
    	// space](https://developers.google.com/workspace/chat/delete-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) and the
    	// authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.delete` (only in
    	//     spaces the app created)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.delete`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.delete`
    	DeleteSpace(ctx context.Context, in *DeleteSpaceRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Completes the
    	// [import process](https://developers.google.com/workspace/chat/import-data)
    	// for the specified space and makes it visible to users.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// and domain-wide delegation with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.import`
    	//
    	// For more information, see [Authorize Google
    	// Chat apps to import
    	// data](https://developers.google.com/workspace/chat/authorize-import).
    	CompleteImportSpace(ctx context.Context, in *CompleteImportSpaceRequest, opts ...grpc.CallOption) (*CompleteImportSpaceResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the existing direct message with the specified user. If no direct
    	// message space is found, returns a `404 NOT_FOUND` error. For an example,
    	// see
    	// [Find a direct message](/chat/api/guides/v1/spaces/find-direct-message).
    	//
    	// With [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app),
    	// returns the direct message space between the specified user and the calling
    	// Chat app.
    	//
    	// With [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// returns the direct message space between the specified user and the
    	// authenticated user.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	FindDirectMessage(ctx context.Context, in *FindDirectMessageRequest, opts ...grpc.CallOption) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Returns all spaces with `spaceType == GROUP_CHAT`, whose
    	// human memberships contain exactly the calling user, and the users specified
    	// in `FindGroupChatsRequest.users`. Only members that have joined the
    	// conversation are supported. For an example, see [Find group
    	// chats](https://developers.google.com/workspace/chat/find-group-chats).
    	//
    	// If the calling user blocks, or is blocked by, some users, and no spaces
    	// with the entire specified set of users are found, this method returns
    	// spaces that don't include the blocked or blocking users.
    	//
    	// The specified set of users must contain only human (non-app) memberships.
    	// A request that contains non-human users doesn't return any spaces.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	FindGroupChats(ctx context.Context, in *FindGroupChatsRequest, opts ...grpc.CallOption) (*FindGroupChatsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a membership for the calling Chat app, a user, or a Google Group.
    	// Creating memberships for other Chat apps isn't supported.
    	// When creating a membership, if the specified member has their auto-accept
    	// policy turned off, then they're invited, and must accept the space
    	// invitation before joining. Otherwise, creating a membership adds the member
    	// directly to the specified space.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.memberships.app` (to add the
    	//     calling app to the space)
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	//
    	// App authentication is not supported for the following use cases:
    	//
    	// - Inviting users external to the Workspace organization that owns the
    	// space.
    	// - Adding a Google Group to a space.
    	// - Adding a Chat app to a space.
    	//
    	// For example usage, see:
    	//
    	// - [Invite or add a user to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-user-membership).
    	// - [Invite or add a Google Group to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-group-membership).
    	// - [Add the Chat app to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).
    	CreateMembership(ctx context.Context, in *CreateMembershipRequest, opts ...grpc.CallOption) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Updates a membership. For an example, see [Update a user's membership in
    	// a space](https://developers.google.com/workspace/chat/update-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) and the
    	// authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (only in
    	//     spaces the app created)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	UpdateMembership(ctx context.Context, in *UpdateMembershipRequest, opts ...grpc.CallOption) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a membership. For an example, see
    	// [Remove a user or a Google Chat app from a
    	// space](https://developers.google.com/workspace/chat/delete-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.memberships.app` (to remove
    	//     the calling app from the space)
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	//
    	// App authentication is not supported for the following use cases:
    	//
    	// - Removing a Google Group from a space.
    	// - Removing a Chat app from a space.
    	//
    	// To delete memberships for space managers, the requester
    	// must be a space manager. If you're using [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// the Chat app must be the space creator.
    	DeleteMembership(ctx context.Context, in *DeleteMembershipRequest, opts ...grpc.CallOption) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Creates a reaction and adds it to a message. For an example, see
    	// [Add a reaction to a
    	// message](https://developers.google.com/workspace/chat/create-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.create`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	CreateReaction(ctx context.Context, in *CreateReactionRequest, opts ...grpc.CallOption) (*Reaction, [error](https://pkg.go.dev/builtin#error))
    	// Lists reactions to a message. For an example, see
    	// [List reactions for a
    	// message](https://developers.google.com/workspace/chat/list-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	ListReactions(ctx context.Context, in *ListReactionsRequest, opts ...grpc.CallOption) (*ListReactionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a reaction to a message. For an example, see
    	// [Delete a
    	// reaction](https://developers.google.com/workspace/chat/delete-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	DeleteReaction(ctx context.Context, in *DeleteReactionRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists message pins in a space. Users can pin important messages in spaces
    	// for easy access. For more information, see [Pin or unpin a conversation in
    	// Google Chat](https://support.google.com/chat/answer/15622437).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	ListMessagePins(ctx context.Context, in *ListMessagePinsRequest, opts ...grpc.CallOption) (*ListMessagePinsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a message pin.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	CreateMessagePin(ctx context.Context, in *CreateMessagePinRequest, opts ...grpc.CallOption) (*MessagePin, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a message pin.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	DeleteMessagePin(ctx context.Context, in *DeleteMessagePinRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Creates a custom emoji.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	CreateCustomEmoji(ctx context.Context, in *CreateCustomEmojiRequest, opts ...grpc.CallOption) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a custom emoji.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis.readonly`
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	GetCustomEmoji(ctx context.Context, in *GetCustomEmojiRequest, opts ...grpc.CallOption) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))
    	// Lists custom emojis visible to the authenticated user.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis.readonly`
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	ListCustomEmojis(ctx context.Context, in *ListCustomEmojisRequest, opts ...grpc.CallOption) (*ListCustomEmojisResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a custom emoji. By default, users can only delete custom emoji they
    	// created. [Emoji managers](https://support.google.com/a/answer/12850085)
    	// assigned by the administrator can delete any custom emoji in the
    	// organization. See [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149).
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	DeleteCustomEmoji(ctx context.Context, in *DeleteCustomEmojiRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a user's read state within a space, used to identify
    	// read and unread messages. For an example, see [Get details about a user's
    	// space read
    	// state](https://developers.google.com/workspace/chat/get-space-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	GetSpaceReadState(ctx context.Context, in *GetSpaceReadStateRequest, opts ...grpc.CallOption) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))
    	// Updates a user's read state within a space, used to identify read and
    	// unread messages. For an example, see [Update a user's space read
    	// state](https://developers.google.com/workspace/chat/update-space-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	UpdateSpaceReadState(ctx context.Context, in *UpdateSpaceReadStateRequest, opts ...grpc.CallOption) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a user's read state within a thread, used to identify
    	// read and unread messages. For an example, see [Get details about a user's
    	// thread read
    	// state](https://developers.google.com/workspace/chat/get-thread-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	GetThreadReadState(ctx context.Context, in *GetThreadReadStateRequest, opts ...grpc.CallOption) (*ThreadReadState, [error](https://pkg.go.dev/builtin#error))
    	// Returns availability information for a human user in Google Chat. For
    	// example, this can be used to check if a user is online or away, or to
    	// retrieve their custom status message.
    	//
    	// This method only retrieves the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	GetAvailability(ctx context.Context, in *GetAvailabilityRequest, opts ...grpc.CallOption) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `ACTIVE` in Google Chat.
    	//
    	// Sets the user's availability state to `ACTIVE`. The `ACTIVE` state
    	// lasts until the specified expiration, at which point the user's state
    	// becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE`
    	// state duration may extend beyond the provided expiration.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsActive(ctx context.Context, in *MarkAsActiveRequest, opts ...grpc.CallOption) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `AWAY` in Google Chat.
    	//
    	// Sets the user's state to away and is not affected by the user's
    	// activity.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsAway(ctx context.Context, in *MarkAsAwayRequest, opts ...grpc.CallOption) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `DO_NOT_DISTURB` in Google Chat.
    	//
    	// Sets a user's availability state to `DO_NOT_DISTURB` until a specified
    	// expiration time.
    	// When in `DO_NOT_DISTURB`, users typically won't receive notifications.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsDoNotDisturb(ctx context.Context, in *MarkAsDoNotDisturbRequest, opts ...grpc.CallOption) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Updates availability information for a human user. Only the `custom_status`
    	// field can be updated through this method.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	UpdateAvailability(ctx context.Context, in *UpdateAvailabilityRequest, opts ...grpc.CallOption) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Returns an event from a Google Chat space. The [event
    	// payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload)
    	// contains the most recent version of the resource that changed. For example,
    	// if you request an event about a new message but the message was later
    	// updated, the server returns the updated `Message` resource in the event
    	// payload.
    	//
    	// Note: The `permissionSettings` field is not returned in the Space
    	// object of the Space event data for this request.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize)
    	// with an
    	// [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes)
    	// appropriate for reading the requested data:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships.readonly`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//
    	// To get an event, the authenticated caller must be a member of the space.
    	//
    	// For an example, see [Get details about an
    	// event from a Google Chat
    	// space](https://developers.google.com/workspace/chat/get-space-event).
    	GetSpaceEvent(ctx context.Context, in *GetSpaceEventRequest, opts ...grpc.CallOption) (*SpaceEvent, [error](https://pkg.go.dev/builtin#error))
    	// Lists events from a Google Chat space. For each event, the
    	// [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload)
    	// contains the most recent version of the Chat resource. For example, if you
    	// list events about new space members, the server returns `Membership`
    	// resources that contain the latest membership details. If new members were
    	// removed during the requested period, the event payload contains an empty
    	// `Membership` resource.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize)
    	// with an
    	// [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes)
    	// appropriate for reading the requested data:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships.readonly`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//
    	// To list events, the authenticated caller must be a member of the space.
    	//
    	// For an example, see [List events from a Google Chat
    	// space](https://developers.google.com/workspace/chat/list-space-events).
    	ListSpaceEvents(ctx context.Context, in *ListSpaceEventsRequest, opts ...grpc.CallOption) (*ListSpaceEventsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the space notification setting. For an example, see [Get the
    	// caller's space notification
    	// setting](https://developers.google.com/workspace/chat/get-space-notification-setting).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.spacesettings`
    	GetSpaceNotificationSetting(ctx context.Context, in *GetSpaceNotificationSettingRequest, opts ...grpc.CallOption) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))
    	// Updates the space notification setting. For an example, see [Update
    	// the caller's space notification
    	// setting](https://developers.google.com/workspace/chat/update-space-notification-setting).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.spacesettings`
    	UpdateSpaceNotificationSetting(ctx context.Context, in *UpdateSpaceNotificationSettingRequest, opts ...grpc.CallOption) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))
    	// Creates a section in Google Chat. Sections help users group conversations
    	// and customize the list of spaces displayed in Chat navigation panel. Only
    	// sections of type `CUSTOM_SECTION` can be created. For details, see [Create
    	// and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	CreateSection(ctx context.Context, in *CreateSectionRequest, opts ...grpc.CallOption) (*Section, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a section of type `CUSTOM_SECTION`.
    	//
    	// If the section contains items, such as spaces, the items are moved to
    	// Google Chat's default sections and are not deleted.
    	//
    	// For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	DeleteSection(ctx context.Context, in *DeleteSectionRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates a section. Only sections of type `CUSTOM_SECTION` can be updated.
    	// For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	UpdateSection(ctx context.Context, in *UpdateSectionRequest, opts ...grpc.CallOption) (*Section, [error](https://pkg.go.dev/builtin#error))
    	// Lists sections available to the Chat user. Sections help users group their
    	// conversations and customize the list of spaces displayed in Chat
    	// navigation panel. For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	//   - `https://www.googleapis.com/auth/chat.users.sections.readonly`
    	ListSections(ctx context.Context, in *ListSectionsRequest, opts ...grpc.CallOption) (*ListSectionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Changes the sort order of a section. For details, see [Create and organize
    	// sections in Google Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	PositionSection(ctx context.Context, in *PositionSectionRequest, opts ...grpc.CallOption) (*PositionSectionResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists items in a section.
    	//
    	// Only spaces can be section items. For details, see [Create and organize
    	// sections in Google Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	//   - `https://www.googleapis.com/auth/chat.users.sections.readonly`
    	ListSectionItems(ctx context.Context, in *ListSectionItemsRequest, opts ...grpc.CallOption) (*ListSectionItemsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Moves an item from one section to another. For example, if a section
    	// contains spaces, this method can be used to move a space to a different
    	// section. For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	MoveSectionItem(ctx context.Context, in *MoveSectionItemRequest, opts ...grpc.CallOption) (*MoveSectionItemResponse, [error](https://pkg.go.dev/builtin#error))
    }

ChatServiceClient is the client API for ChatService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewChatServiceClient 
    
    
    func NewChatServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) ChatServiceClient

## ChatServiceServer
    
    
    type ChatServiceServer interface {
    	// Creates a message in a Google Chat space. For an example, see [Send a
    	// message](https://developers.google.com/workspace/chat/create-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.create`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// Chat attributes the message sender differently depending on the type of
    	// authentication that you use in your request.
    	//
    	// The following image shows how Chat attributes a message when you use app
    	// authentication. Chat displays the Chat app as the message
    	// sender. The content of the message can contain text (`text`), cards
    	// (`cardsV2`), and accessory widgets (`accessoryWidgets`).
    	//
    	// ![Message sent with app
    	// authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)
    	//
    	// The following image shows how Chat attributes a message when you use user
    	// authentication. Chat displays the user as the message sender and attributes
    	// the Chat app to the message by displaying its name. The content of message
    	// can only contain text (`text`).
    	//
    	// ![Message sent with user
    	// authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)
    	//
    	// The maximum message size, including the message contents, is 32,000 bytes.
    	//
    	// For
    	// [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks)
    	// requests, the response doesn't contain the full message. The response only
    	// populates the `name` and `thread.name` fields in addition to the
    	// information that was in the request.
    	CreateMessage(context.Context, *CreateMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Lists messages in a space that the caller is a member of, including
    	// messages from blocked members and spaces. System messages, like those
    	// announcing new space members, aren't included. If you list messages from a
    	// space with no messages, the response is an empty object. When using a
    	// REST/HTTP interface, the response contains an empty JSON object, `{}`.
    	// For an example, see
    	// [List
    	// messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`. When
    	//     using this authentication scope, this method only returns public
    	//     messages in a space. It doesn't include private messages.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	ListMessages(context.Context, *ListMessagesRequest) (*ListMessagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists memberships in a space. For an example, see [List users and Google
    	// Chat apps in a
    	// space](https://developers.google.com/workspace/chat/list-members). Listing
    	// memberships with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// lists memberships in spaces that the Chat app has
    	// access to, but excludes Chat app memberships,
    	// including its own. Listing memberships with
    	// [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// lists memberships in spaces that the authenticated user has access to.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (requires
    	//     [administrator approval](https://support.google.com/a?p=chat-app-auth))
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	ListMemberships(context.Context, *ListMembershipsRequest) (*ListMembershipsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a membership. For an example, see
    	// [Get details about a user's or Google Chat app's
    	// membership](https://developers.google.com/workspace/chat/get-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (requires
    	//     [administrator approval](https://support.google.com/a?p=chat-app-auth))
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	GetMembership(context.Context, *GetMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a message.
    	// For an example, see [Get details about a
    	// message](https://developers.google.com/workspace/chat/get-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`: When using this
    	//     authorization scope, this method returns details about a message the
    	//     Chat app has access to, like direct messages and [slash
    	//     commands](https://developers.google.com/workspace/chat/slash-commands)
    	//     that invoke the Chat app.
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//     with [administrator
    	//     approval](https://support.google.com/a?p=chat-app-auth).
    	//     When using this authentication scope,
    	//     this method returns details about a public message in a space.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//
    	// Note: Might return a message from a blocked member or space.
    	GetMessage(context.Context, *GetMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Updates a message. There's a difference between the `patch` and `update`
    	// methods. The `patch`
    	// method uses a `patch` request while the `update` method uses a `put`
    	// request. We recommend using the `patch` method. For an example, see
    	// [Update a
    	// message](https://developers.google.com/workspace/chat/update-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When using app authentication, requests can only update messages
    	// created by the calling Chat app.
    	UpdateMessage(context.Context, *UpdateMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a message.
    	// For an example, see [Delete a
    	// message](https://developers.google.com/workspace/chat/delete-messages).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When using app authentication, requests can only delete messages
    	// created by the calling Chat app.
    	DeleteMessage(context.Context, *DeleteMessageRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Searches for messages in Google Chat that the calling user has access to.
    	// Returns a list of messages matching the search criteria.
    	//
    	// To search across all spaces the user has access to, set `parent` to
    	// `spaces/-`. Using any other value for `parent` results in an
    	// `INVALID_ARGUMENT` error. The returned messages have their `name` field
    	// populated with the full resource name, which includes the specific `space`
    	// in which the message resides.
    	//
    	// This API doesn't return all message types. The types of messages listed
    	// below aren't included in the response. Use
    	// [ListMessages][google.chat.v1.ChatService.ListMessages] to list all
    	// messages.
    	//
    	// - Private Messages that are visible to the authenticated user.
    	// - Messages posted by Chat apps in spaces or group chats.
    	// - Messages in a Chat app DM.
    	// - Messages from blocked users.
    	// - Messages in spaces that the caller has muted.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	SearchMessages(context.Context, *SearchMessagesRequest) (*SearchMessagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of a message attachment. The attachment data is fetched
    	// using the [media
    	// API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download).
    	// For an example, see
    	// [Get metadata about a message
    	// attachment](https://developers.google.com/workspace/chat/get-media-attachments).
    	//
    	// Requires [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	GetAttachment(context.Context, *GetAttachmentRequest) (*Attachment, [error](https://pkg.go.dev/builtin#error))
    	// Uploads an attachment. For an example, see
    	// [Upload media as a file
    	// attachment](https://developers.google.com/workspace/chat/upload-media-attachments).
    	//
    	// Requires user
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.create`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	//
    	// You can upload attachments up to 200 MB. Certain file types aren't
    	// supported. For details, see [File types blocked by Google
    	// Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat).
    	UploadAttachment(context.Context, *UploadAttachmentRequest) (*UploadAttachmentResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists spaces the caller is a member of. Group chats and DMs aren't listed
    	// until the first message is sent. For an example, see
    	// [List
    	// spaces](https://developers.google.com/workspace/chat/list-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//
    	// To list all named spaces by Google Workspace organization, use the
    	// [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search)
    	// method using Workspace administrator privileges instead.
    	ListSpaces(context.Context, *ListSpacesRequest) (*ListSpacesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of spaces in a Google Workspace organization. For an
    	// example, see [Search for and manage
    	// spaces](https://developers.google.com/workspace/chat/search-manage-admin).
    	//
    	// When `use_admin_access` is set to `false`, the results are limited to
    	// spaces where the calling user is a joined member. To search with
    	// administrator privileges, set `use_admin_access` to `true`.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//
    	// - [User
    	// authentication with administrator
    	// privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges)
    	// and one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	SearchSpaces(context.Context, *SearchSpacesRequest) (*SearchSpacesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a space. For an example, see
    	// [Get details about a
    	// space](https://developers.google.com/workspace/chat/get-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces` with [administrator
    	//     approval](https://support.google.com/a?p=chat-app-auth)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     one of the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	//
    	// App authentication has the following limitations:
    	//
    	// - `space.access_settings` is only populated when using the
    	// `chat.app.spaces` scope.
    	// - `space.predefind_permission_settings` and `space.permission_settings` are
    	// only populated when using the `chat.app.spaces` scope, and only for
    	// spaces the app created.
    	GetSpace(context.Context, *GetSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Creates a space. Can be used to create a named space, or a
    	// group chat in `Import mode`. For an example, see [Create a
    	// space](https://developers.google.com/workspace/chat/create-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//
    	// When authenticating as an app, the `space.customer` field must be set in
    	// the request.
    	//
    	// When authenticating as an app, the Chat app is added as a member of the
    	// space. However, unlike human authentication, the Chat app is not added as a
    	// space manager. By default, the Chat app can be removed from the space by
    	// all space members. To allow only space managers to remove the app from a
    	// space, set `space.permission_settings.manage_apps` to `managers_allowed`.
    	//
    	// Space membership upon creation depends on whether the space is created in
    	// `Import mode`:
    	//
    	// * **Import mode:** No members are created.
    	// * **All other modes:**  The calling user is added as a member. This is:
    	//
    	//   - The app itself when using app authentication.
    	//
    	//   - The human user when using user authentication.
    	//
    	//     If you receive the error message `ALREADY_EXISTS` when creating
    	//     a space, try a different `displayName`. An existing space within
    	//     the Google Workspace organization might already use this display name.
    	CreateSpace(context.Context, *CreateSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Creates a space and adds specified users to it. The calling user is
    	// automatically added to the space, and shouldn't be specified as a
    	// membership in the request. For an example, see
    	// [Set up a space with initial
    	// members](https://developers.google.com/workspace/chat/set-up-spaces).
    	//
    	// To specify the human members to add, add memberships with the appropriate
    	// `membership.member.name`. To add a human user, use `users/{user}`, where
    	// `{user}` can be the email address for the user. For users in the same
    	// Workspace organization `{user}` can also be the `id` for the person from
    	// the People API, or the `id` for the user in the Directory API. For example,
    	// if the People API Person profile ID for `user@example.com` is `123456789`,
    	// you can add the user to the space by setting the `membership.member.name`
    	// to `users/user@example.com` or `users/123456789`.
    	//
    	// To specify the Google groups to add, add memberships with the
    	// appropriate `membership.group_member.name`. To add or invite a Google
    	// group, use `groups/{group}`, where `{group}` is the `id` for the group from
    	// the Cloud Identity Groups API. For example, you can use [Cloud Identity
    	// Groups lookup
    	// API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup)
    	// to retrieve the ID `123456789` for group email `group@example.com`, then
    	// you can add the group to the space by setting the
    	// `membership.group_member.name` to `groups/123456789`. Group email is not
    	// supported, and Google groups can only be added as members in named spaces.
    	//
    	// For a named space or group chat, if the caller blocks, or is blocked
    	// by some members, or doesn't have permission to add some members, then
    	// those members aren't added to the created space.
    	//
    	// To create a direct message (DM) between the calling user and another human
    	// user, specify exactly one membership to represent the human user. If
    	// one user blocks the other, the request fails and the DM isn't created.
    	//
    	// To create a DM between the calling user and the calling app, set
    	// `Space.singleUserBotDm` to `true` and don't specify any memberships. You
    	// can only use this method to set up a DM with the calling app. To add the
    	// calling app as a member of a space or an existing DM between two human
    	// users, see
    	// [Invite or add a user or app to a
    	// space](https://developers.google.com/workspace/chat/create-members).
    	//
    	// If a DM already exists between two users, even when one user blocks the
    	// other at the time a request is made, then the existing DM is returned.
    	//
    	// Spaces with threaded replies aren't supported. If you receive the error
    	// message `ALREADY_EXISTS` when setting up a space, try a different
    	// `displayName`. An existing space within the Google Workspace organization
    	// might already use this display name.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.create`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	SetUpSpace(context.Context, *SetUpSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Updates a space. For an example, see
    	// [Update a
    	// space](https://developers.google.com/workspace/chat/update-spaces).
    	//
    	// If you're updating the `displayName` field and receive the error message
    	// `ALREADY_EXISTS`, try a different display name.. An existing space within
    	// the Google Workspace organization might already use this display name.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scopes is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.spaces`
    	//
    	// App authentication has the following limitations:
    	//
    	// - To update either `space.predefined_permission_settings` or
    	// `space.permission_settings`, the app must be the space creator.
    	// - Updating the `space.access_settings.audience` is not supported for app
    	// authentication.
    	UpdateSpace(context.Context, *UpdateSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a named space. Always performs a cascading delete, which means
    	// that the space's child resources—like messages posted in the space and
    	// memberships in the space—are also deleted. For an example, see
    	// [Delete a
    	// space](https://developers.google.com/workspace/chat/delete-spaces).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) and the
    	// authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.delete` (only in
    	//     spaces the app created)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.delete`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.delete`
    	DeleteSpace(context.Context, *DeleteSpaceRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Completes the
    	// [import process](https://developers.google.com/workspace/chat/import-data)
    	// for the specified space and makes it visible to users.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// and domain-wide delegation with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.import`
    	//
    	// For more information, see [Authorize Google
    	// Chat apps to import
    	// data](https://developers.google.com/workspace/chat/authorize-import).
    	CompleteImportSpace(context.Context, *CompleteImportSpaceRequest) (*CompleteImportSpaceResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the existing direct message with the specified user. If no direct
    	// message space is found, returns a `404 NOT_FOUND` error. For an example,
    	// see
    	// [Find a direct message](/chat/api/guides/v1/spaces/find-direct-message).
    	//
    	// With [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app),
    	// returns the direct message space between the specified user and the calling
    	// Chat app.
    	//
    	// With [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// returns the direct message space between the specified user and the
    	// authenticated user.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.bot`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	FindDirectMessage(context.Context, *FindDirectMessageRequest) (*Space, [error](https://pkg.go.dev/builtin#error))
    	// Returns all spaces with `spaceType == GROUP_CHAT`, whose
    	// human memberships contain exactly the calling user, and the users specified
    	// in `FindGroupChatsRequest.users`. Only members that have joined the
    	// conversation are supported. For an example, see [Find group
    	// chats](https://developers.google.com/workspace/chat/find-group-chats).
    	//
    	// If the calling user blocks, or is blocked by, some users, and no spaces
    	// with the entire specified set of users are found, this method returns
    	// spaces that don't include the blocked or blocking users.
    	//
    	// The specified set of users must contain only human (non-app) memberships.
    	// A request that contains non-human users doesn't return any spaces.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	FindGroupChats(context.Context, *FindGroupChatsRequest) (*FindGroupChatsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a membership for the calling Chat app, a user, or a Google Group.
    	// Creating memberships for other Chat apps isn't supported.
    	// When creating a membership, if the specified member has their auto-accept
    	// policy turned off, then they're invited, and must accept the space
    	// invitation before joining. Otherwise, creating a membership adds the member
    	// directly to the specified space.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.memberships.app` (to add the
    	//     calling app to the space)
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	//
    	// App authentication is not supported for the following use cases:
    	//
    	// - Inviting users external to the Workspace organization that owns the
    	// space.
    	// - Adding a Google Group to a space.
    	// - Adding a Chat app to a space.
    	//
    	// For example usage, see:
    	//
    	// - [Invite or add a user to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-user-membership).
    	// - [Invite or add a Google Group to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-group-membership).
    	// - [Add the Chat app to a
    	// space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).
    	CreateMembership(context.Context, *CreateMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Updates a membership. For an example, see [Update a user's membership in
    	// a space](https://developers.google.com/workspace/chat/update-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) and the
    	// authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships` (only in
    	//     spaces the app created)
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	UpdateMembership(context.Context, *UpdateMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a membership. For an example, see
    	// [Remove a user or a Google Chat app from a
    	// space](https://developers.google.com/workspace/chat/delete-members).
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator approval](https://support.google.com/a?p=chat-app-auth)
    	// and the authorization scope:
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//   - `https://www.googleapis.com/auth/chat.memberships.app` (to remove
    	//     the calling app from the space)
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces
    	//     only)
    	//   - User authentication grants administrator privileges when an
    	//     administrator account authenticates, `use_admin_access` is `true`, and
    	//     the following authorization scope is used:
    	//   - `https://www.googleapis.com/auth/chat.admin.memberships`
    	//
    	// App authentication is not supported for the following use cases:
    	//
    	// - Removing a Google Group from a space.
    	// - Removing a Chat app from a space.
    	//
    	// To delete memberships for space managers, the requester
    	// must be a space manager. If you're using [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// the Chat app must be the space creator.
    	DeleteMembership(context.Context, *DeleteMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))
    	// Creates a reaction and adds it to a message. For an example, see
    	// [Add a reaction to a
    	// message](https://developers.google.com/workspace/chat/create-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.create`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	CreateReaction(context.Context, *CreateReactionRequest) (*Reaction, [error](https://pkg.go.dev/builtin#error))
    	// Lists reactions to a message. For an example, see
    	// [List reactions for a
    	// message](https://developers.google.com/workspace/chat/list-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	ListReactions(context.Context, *ListReactionsRequest) (*ListReactionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a reaction to a message. For an example, see
    	// [Delete a
    	// reaction](https://developers.google.com/workspace/chat/delete-reactions).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.import` (import mode spaces only)
    	DeleteReaction(context.Context, *DeleteReactionRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists message pins in a space. Users can pin important messages in spaces
    	// for easy access. For more information, see [Pin or unpin a conversation in
    	// Google Chat](https://support.google.com/chat/answer/15622437).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	ListMessagePins(context.Context, *ListMessagePinsRequest) (*ListMessagePinsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a message pin.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	CreateMessagePin(context.Context, *CreateMessagePinRequest) (*MessagePin, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a message pin.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.spaces.pins`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	DeleteMessagePin(context.Context, *DeleteMessagePinRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Creates a custom emoji.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	CreateCustomEmoji(context.Context, *CreateCustomEmojiRequest) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a custom emoji.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis.readonly`
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	GetCustomEmoji(context.Context, *GetCustomEmojiRequest) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))
    	// Lists custom emojis visible to the authenticated user.
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis.readonly`
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	ListCustomEmojis(context.Context, *ListCustomEmojisRequest) (*ListCustomEmojisResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a custom emoji. By default, users can only delete custom emoji they
    	// created. [Emoji managers](https://support.google.com/a/answer/12850085)
    	// assigned by the administrator can delete any custom emoji in the
    	// organization. See [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149).
    	//
    	// Custom emojis are only available for Google Workspace accounts, and the
    	// administrator must turn custom emojis on for the organization. For more
    	// information, see [Learn about custom emojis in Google
    	// Chat](https://support.google.com/chat/answer/12800149) and
    	// [Manage custom emoji
    	// permissions](https://support.google.com/a/answer/12850085).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.customemojis`
    	DeleteCustomEmoji(context.Context, *DeleteCustomEmojiRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a user's read state within a space, used to identify
    	// read and unread messages. For an example, see [Get details about a user's
    	// space read
    	// state](https://developers.google.com/workspace/chat/get-space-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	GetSpaceReadState(context.Context, *GetSpaceReadStateRequest) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))
    	// Updates a user's read state within a space, used to identify read and
    	// unread messages. For an example, see [Update a user's space read
    	// state](https://developers.google.com/workspace/chat/update-space-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	UpdateSpaceReadState(context.Context, *UpdateSpaceReadStateRequest) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))
    	// Returns details about a user's read state within a thread, used to identify
    	// read and unread messages. For an example, see [Get details about a user's
    	// thread read
    	// state](https://developers.google.com/workspace/chat/get-thread-read-state).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	GetThreadReadState(context.Context, *GetThreadReadStateRequest) (*ThreadReadState, [error](https://pkg.go.dev/builtin#error))
    	// Returns availability information for a human user in Google Chat. For
    	// example, this can be used to check if a user is online or away, or to
    	// retrieve their custom status message.
    	//
    	// This method only retrieves the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	GetAvailability(context.Context, *GetAvailabilityRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `ACTIVE` in Google Chat.
    	//
    	// Sets the user's availability state to `ACTIVE`. The `ACTIVE` state
    	// lasts until the specified expiration, at which point the user's state
    	// becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE`
    	// state duration may extend beyond the provided expiration.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsActive(context.Context, *MarkAsActiveRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `AWAY` in Google Chat.
    	//
    	// Sets the user's state to away and is not affected by the user's
    	// activity.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsAway(context.Context, *MarkAsAwayRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Marks user as `DO_NOT_DISTURB` in Google Chat.
    	//
    	// Sets a user's availability state to `DO_NOT_DISTURB` until a specified
    	// expiration time.
    	// When in `DO_NOT_DISTURB`, users typically won't receive notifications.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	MarkAsDoNotDisturb(context.Context, *MarkAsDoNotDisturbRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Updates availability information for a human user. Only the `custom_status`
    	// field can be updated through this method.
    	//
    	// This method only updates the authenticated user's availability.
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.availability`
    	UpdateAvailability(context.Context, *UpdateAvailabilityRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))
    	// Returns an event from a Google Chat space. The [event
    	// payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload)
    	// contains the most recent version of the resource that changed. For example,
    	// if you request an event about a new message but the message was later
    	// updated, the server returns the updated `Message` resource in the event
    	// payload.
    	//
    	// Note: The `permissionSettings` field is not returned in the Space
    	// object of the Space event data for this request.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize)
    	// with an
    	// [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes)
    	// appropriate for reading the requested data:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships.readonly`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//
    	// To get an event, the authenticated caller must be a member of the space.
    	//
    	// For an example, see [Get details about an
    	// event from a Google Chat
    	// space](https://developers.google.com/workspace/chat/get-space-event).
    	GetSpaceEvent(context.Context, *GetSpaceEventRequest) (*SpaceEvent, [error](https://pkg.go.dev/builtin#error))
    	// Lists events from a Google Chat space. For each event, the
    	// [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload)
    	// contains the most recent version of the Chat resource. For example, if you
    	// list events about new space members, the server returns `Membership`
    	// resources that contain the latest membership details. If new members were
    	// removed during the requested period, the event payload contains an empty
    	// `Membership` resource.
    	//
    	// Supports the following types of
    	// [authentication](https://developers.google.com/workspace/chat/authenticate-authorize)
    	// with an
    	// [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes)
    	// appropriate for reading the requested data:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.app.spaces`
    	//   - `https://www.googleapis.com/auth/chat.app.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships`
    	//   - `https://www.googleapis.com/auth/chat.app.memberships.readonly`
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with one of the following authorization scopes:
    	//   - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	//   - `https://www.googleapis.com/auth/chat.spaces`
    	//   - `https://www.googleapis.com/auth/chat.messages.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions.readonly`
    	//   - `https://www.googleapis.com/auth/chat.messages.reactions`
    	//   - `https://www.googleapis.com/auth/chat.memberships.readonly`
    	//   - `https://www.googleapis.com/auth/chat.memberships`
    	//
    	// To list events, the authenticated caller must be a member of the space.
    	//
    	// For an example, see [List events from a Google Chat
    	// space](https://developers.google.com/workspace/chat/list-space-events).
    	ListSpaceEvents(context.Context, *ListSpaceEventsRequest) (*ListSpaceEventsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the space notification setting. For an example, see [Get the
    	// caller's space notification
    	// setting](https://developers.google.com/workspace/chat/get-space-notification-setting).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.spacesettings`
    	GetSpaceNotificationSetting(context.Context, *GetSpaceNotificationSettingRequest) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))
    	// Updates the space notification setting. For an example, see [Update
    	// the caller's space notification
    	// setting](https://developers.google.com/workspace/chat/update-space-notification-setting).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.spacesettings`
    	UpdateSpaceNotificationSetting(context.Context, *UpdateSpaceNotificationSettingRequest) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))
    	// Creates a section in Google Chat. Sections help users group conversations
    	// and customize the list of spaces displayed in Chat navigation panel. Only
    	// sections of type `CUSTOM_SECTION` can be created. For details, see [Create
    	// and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	CreateSection(context.Context, *CreateSectionRequest) (*Section, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a section of type `CUSTOM_SECTION`.
    	//
    	// If the section contains items, such as spaces, the items are moved to
    	// Google Chat's default sections and are not deleted.
    	//
    	// For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	DeleteSection(context.Context, *DeleteSectionRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Updates a section. Only sections of type `CUSTOM_SECTION` can be updated.
    	// For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	UpdateSection(context.Context, *UpdateSectionRequest) (*Section, [error](https://pkg.go.dev/builtin#error))
    	// Lists sections available to the Chat user. Sections help users group their
    	// conversations and customize the list of spaces displayed in Chat
    	// navigation panel. For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	//   - `https://www.googleapis.com/auth/chat.users.sections.readonly`
    	ListSections(context.Context, *ListSectionsRequest) (*ListSectionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Changes the sort order of a section. For details, see [Create and organize
    	// sections in Google Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	PositionSection(context.Context, *PositionSectionRequest) (*PositionSectionResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists items in a section.
    	//
    	// Only spaces can be section items. For details, see [Create and organize
    	// sections in Google Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	//   - `https://www.googleapis.com/auth/chat.users.sections.readonly`
    	ListSectionItems(context.Context, *ListSectionItemsRequest) (*ListSectionItemsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Moves an item from one section to another. For example, if a section
    	// contains spaces, this method can be used to move a space to a different
    	// section. For details, see [Create and organize sections in Google
    	// Chat](https://support.google.com/chat/answer/16059854).
    	//
    	// Requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// with the [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.sections`
    	MoveSectionItem(context.Context, *MoveSectionItemRequest) (*MoveSectionItemResponse, [error](https://pkg.go.dev/builtin#error))
    }

ChatServiceServer is the server API for ChatService service. All implementations should embed UnimplementedChatServiceServer for forward compatibility

## ChatSpaceLinkData
    
    
    type ChatSpaceLinkData struct {
    
    	// The space of the linked Chat space resource.
    	//
    	// Format: `spaces/{space}`
    	Space [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// The thread of the linked Chat space resource.
    	//
    	// Format: `spaces/{space}/threads/{thread}`
    	Thread [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=thread,proto3" json:"thread,omitempty"`
    	// The message of the linked Chat space resource.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	Message [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=message,proto3" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

Data for Chat space links.

### func (*ChatSpaceLinkData) Descriptor 
    
    
    func (*ChatSpaceLinkData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ChatSpaceLinkData.ProtoReflect.Descriptor instead.

### func (*ChatSpaceLinkData) GetMessage 
    
    
    func (x *ChatSpaceLinkData) GetMessage() [string](https://pkg.go.dev/builtin#string)

### func (*ChatSpaceLinkData) GetSpace 
    
    
    func (x *ChatSpaceLinkData) GetSpace() [string](https://pkg.go.dev/builtin#string)

### func (*ChatSpaceLinkData) GetThread 
    
    
    func (x *ChatSpaceLinkData) GetThread() [string](https://pkg.go.dev/builtin#string)

### func (*ChatSpaceLinkData) ProtoMessage 
    
    
    func (*ChatSpaceLinkData) ProtoMessage()

### func (*ChatSpaceLinkData) ProtoReflect 
    
    
    func (x *ChatSpaceLinkData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ChatSpaceLinkData) Reset 
    
    
    func (x *ChatSpaceLinkData) Reset()

### func (*ChatSpaceLinkData) String 
    
    
    func (x *ChatSpaceLinkData) String() [string](https://pkg.go.dev/builtin#string)

## CompleteImportSpaceRequest
    
    
    type CompleteImportSpaceRequest struct {
    
    	// Required. Resource name of the import mode space.
    	//
    	// Format: `spaces/{space}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for completing the import process for a space.

### func (*CompleteImportSpaceRequest) Descriptor 
    
    
    func (*CompleteImportSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CompleteImportSpaceRequest.ProtoReflect.Descriptor instead.

### func (*CompleteImportSpaceRequest) GetName 
    
    
    func (x *CompleteImportSpaceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CompleteImportSpaceRequest) ProtoMessage 
    
    
    func (*CompleteImportSpaceRequest) ProtoMessage()

### func (*CompleteImportSpaceRequest) ProtoReflect 
    
    
    func (x *CompleteImportSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CompleteImportSpaceRequest) Reset 
    
    
    func (x *CompleteImportSpaceRequest) Reset()

### func (*CompleteImportSpaceRequest) String 
    
    
    func (x *CompleteImportSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## CompleteImportSpaceResponse
    
    
    type CompleteImportSpaceResponse struct {
    
    	// The import mode space.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for completing the import process for a space.

### func (*CompleteImportSpaceResponse) Descriptor 
    
    
    func (*CompleteImportSpaceResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CompleteImportSpaceResponse.ProtoReflect.Descriptor instead.

### func (*CompleteImportSpaceResponse) GetSpace 
    
    
    func (x *CompleteImportSpaceResponse) GetSpace() *Space

### func (*CompleteImportSpaceResponse) ProtoMessage 
    
    
    func (*CompleteImportSpaceResponse) ProtoMessage()

### func (*CompleteImportSpaceResponse) ProtoReflect 
    
    
    func (x *CompleteImportSpaceResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CompleteImportSpaceResponse) Reset 
    
    
    func (x *CompleteImportSpaceResponse) Reset()

### func (*CompleteImportSpaceResponse) String 
    
    
    func (x *CompleteImportSpaceResponse) String() [string](https://pkg.go.dev/builtin#string)

## ContextualAddOnMarkup
    
    
    type ContextualAddOnMarkup struct {
    	// contains filtered or unexported fields
    }

The markup for developers to specify the contents of a contextual AddOn.

### func (*ContextualAddOnMarkup) Descriptor 
    
    
    func (*ContextualAddOnMarkup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup.ProtoReflect.Descriptor instead.

### func (*ContextualAddOnMarkup) ProtoMessage 
    
    
    func (*ContextualAddOnMarkup) ProtoMessage()

### func (*ContextualAddOnMarkup) ProtoReflect 
    
    
    func (x *ContextualAddOnMarkup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualAddOnMarkup) Reset 
    
    
    func (x *ContextualAddOnMarkup) Reset()

### func (*ContextualAddOnMarkup) String 
    
    
    func (x *ContextualAddOnMarkup) String() [string](https://pkg.go.dev/builtin#string)

## ContextualAddOnMarkup_Card
    
    
    type ContextualAddOnMarkup_Card struct {
    
    	// The header of the card. A header usually contains a title and an image.
    	Header *ContextualAddOnMarkup_Card_CardHeader `protobuf:"bytes,1,opt,name=header,proto3" json:"header,omitempty"`
    	// Sections are separated by a line divider.
    	Sections []*ContextualAddOnMarkup_Card_Section `protobuf:"bytes,2,rep,name=sections,proto3" json:"sections,omitempty"`
    	// The actions of this card.
    	CardActions []*ContextualAddOnMarkup_Card_CardAction `protobuf:"bytes,3,rep,name=card_actions,json=cardActions,proto3" json:"card_actions,omitempty"`
    	// Name of the card.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A card is a UI element that can contain UI widgets such as text and images.

### func (*ContextualAddOnMarkup_Card) Descriptor 
    
    
    func (*ContextualAddOnMarkup_Card) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup_Card.ProtoReflect.Descriptor instead.

### func (*ContextualAddOnMarkup_Card) GetCardActions 
    
    
    func (x *ContextualAddOnMarkup_Card) GetCardActions() []*ContextualAddOnMarkup_Card_CardAction

### func (*ContextualAddOnMarkup_Card) GetHeader 
    
    
    func (x *ContextualAddOnMarkup_Card) GetHeader() *ContextualAddOnMarkup_Card_CardHeader

### func (*ContextualAddOnMarkup_Card) GetName 
    
    
    func (x *ContextualAddOnMarkup_Card) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card) GetSections 
    
    
    func (x *ContextualAddOnMarkup_Card) GetSections() []*ContextualAddOnMarkup_Card_Section

### func (*ContextualAddOnMarkup_Card) ProtoMessage 
    
    
    func (*ContextualAddOnMarkup_Card) ProtoMessage()

### func (*ContextualAddOnMarkup_Card) ProtoReflect 
    
    
    func (x *ContextualAddOnMarkup_Card) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualAddOnMarkup_Card) Reset 
    
    
    func (x *ContextualAddOnMarkup_Card) Reset()

### func (*ContextualAddOnMarkup_Card) String 
    
    
    func (x *ContextualAddOnMarkup_Card) String() [string](https://pkg.go.dev/builtin#string)

## ContextualAddOnMarkup_Card_CardAction
    
    
    type ContextualAddOnMarkup_Card_CardAction struct {
    
    	// The label used to be displayed in the action menu item.
    	ActionLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=action_label,json=actionLabel,proto3" json:"action_label,omitempty"`
    	// The onclick action for this action item.
    	OnClick *WidgetMarkup_OnClick `protobuf:"bytes,2,opt,name=on_click,json=onClick,proto3" json:"on_click,omitempty"`
    	// contains filtered or unexported fields
    }

A card action is the action associated with the card. For an invoice card, a typical action would be: delete invoice, email invoice or open the invoice in browser.

Not supported by Google Chat apps.

### func (*ContextualAddOnMarkup_Card_CardAction) Descriptor 
    
    
    func (*ContextualAddOnMarkup_Card_CardAction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup_Card_CardAction.ProtoReflect.Descriptor instead.

### func (*ContextualAddOnMarkup_Card_CardAction) GetActionLabel 
    
    
    func (x *ContextualAddOnMarkup_Card_CardAction) GetActionLabel() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card_CardAction) GetOnClick 
    
    
    func (x *ContextualAddOnMarkup_Card_CardAction) GetOnClick() *WidgetMarkup_OnClick

### func (*ContextualAddOnMarkup_Card_CardAction) ProtoMessage 
    
    
    func (*ContextualAddOnMarkup_Card_CardAction) ProtoMessage()

### func (*ContextualAddOnMarkup_Card_CardAction) ProtoReflect 
    
    
    func (x *ContextualAddOnMarkup_Card_CardAction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualAddOnMarkup_Card_CardAction) Reset 
    
    
    func (x *ContextualAddOnMarkup_Card_CardAction) Reset()

### func (*ContextualAddOnMarkup_Card_CardAction) String 
    
    
    func (x *ContextualAddOnMarkup_Card_CardAction) String() [string](https://pkg.go.dev/builtin#string)

## ContextualAddOnMarkup_Card_CardHeader
    
    
    type ContextualAddOnMarkup_Card_CardHeader struct {
    
    	// The title must be specified. The header has a fixed height: if both a
    	// title and subtitle is specified, each takes up one line. If only the
    	// title is specified, it takes up both lines.
    	Title [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=title,proto3" json:"title,omitempty"`
    	// The subtitle of the card header.
    	Subtitle [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=subtitle,proto3" json:"subtitle,omitempty"`
    	// The image's type (for example, square border or circular border).
    	ImageStyle ContextualAddOnMarkup_Card_CardHeader_ImageStyle `protobuf:"varint,3,opt,name=image_style,json=imageStyle,proto3,enum=google.chat.v1.ContextualAddOnMarkup_Card_CardHeader_ImageStyle" json:"image_style,omitempty"`
    	// The URL of the image in the card header.
    	ImageUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=image_url,json=imageUrl,proto3" json:"image_url,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*ContextualAddOnMarkup_Card_CardHeader) Descriptor 
    
    
    func (*ContextualAddOnMarkup_Card_CardHeader) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup_Card_CardHeader.ProtoReflect.Descriptor instead.

### func (*ContextualAddOnMarkup_Card_CardHeader) GetImageStyle 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) GetImageStyle() ContextualAddOnMarkup_Card_CardHeader_ImageStyle

### func (*ContextualAddOnMarkup_Card_CardHeader) GetImageUrl 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) GetImageUrl() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card_CardHeader) GetSubtitle 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) GetSubtitle() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card_CardHeader) GetTitle 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) GetTitle() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card_CardHeader) ProtoMessage 
    
    
    func (*ContextualAddOnMarkup_Card_CardHeader) ProtoMessage()

### func (*ContextualAddOnMarkup_Card_CardHeader) ProtoReflect 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualAddOnMarkup_Card_CardHeader) Reset 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) Reset()

### func (*ContextualAddOnMarkup_Card_CardHeader) String 
    
    
    func (x *ContextualAddOnMarkup_Card_CardHeader) String() [string](https://pkg.go.dev/builtin#string)

## ContextualAddOnMarkup_Card_CardHeader_ImageStyle
    
    
    type ContextualAddOnMarkup_Card_CardHeader_ImageStyle [int32](https://pkg.go.dev/builtin#int32)

### ContextualAddOnMarkup_Card_CardHeader_IMAGE_STYLE_UNSPECIFIED, ContextualAddOnMarkup_Card_CardHeader_IMAGE, ContextualAddOnMarkup_Card_CardHeader_AVATAR
    
    
    const (
    	ContextualAddOnMarkup_Card_CardHeader_IMAGE_STYLE_UNSPECIFIED ContextualAddOnMarkup_Card_CardHeader_ImageStyle = 0
    	// Square border.
    	ContextualAddOnMarkup_Card_CardHeader_IMAGE ContextualAddOnMarkup_Card_CardHeader_ImageStyle = 1
    	// Circular border.
    	ContextualAddOnMarkup_Card_CardHeader_AVATAR ContextualAddOnMarkup_Card_CardHeader_ImageStyle = 2
    )

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Descriptor 
    
    
    func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Enum 
    
    
    func (x ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Enum() *ContextualAddOnMarkup_Card_CardHeader_ImageStyle

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) EnumDescriptor 
    
    
    func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup_Card_CardHeader_ImageStyle.Descriptor instead.

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Number 
    
    
    func (x ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) String 
    
    
    func (x ContextualAddOnMarkup_Card_CardHeader_ImageStyle) String() [string](https://pkg.go.dev/builtin#string)

### func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Type 
    
    
    func (ContextualAddOnMarkup_Card_CardHeader_ImageStyle) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ContextualAddOnMarkup_Card_Section
    
    
    type ContextualAddOnMarkup_Card_Section struct {
    
    	// The header of the section. Formatted text is
    	// supported. For more information
    	// about formatting text, see
    	// [Formatting text in Google Chat
    	// apps](https://developers.google.com/workspace/chat/format-messages#card-formatting)
    	// and
    	// [Formatting
    	// text in Google Workspace
    	// Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting).
    	Header [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=header,proto3" json:"header,omitempty"`
    	// A section must contain at least one widget.
    	Widgets []*WidgetMarkup `protobuf:"bytes,2,rep,name=widgets,proto3" json:"widgets,omitempty"`
    	// contains filtered or unexported fields
    }

A section contains a collection of widgets that are rendered (vertically) in the order that they are specified. Across all platforms, cards have a narrow fixed width, so there's currently no need for layout properties (for example, float).

### func (*ContextualAddOnMarkup_Card_Section) Descriptor 
    
    
    func (*ContextualAddOnMarkup_Card_Section) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualAddOnMarkup_Card_Section.ProtoReflect.Descriptor instead.

### func (*ContextualAddOnMarkup_Card_Section) GetHeader 
    
    
    func (x *ContextualAddOnMarkup_Card_Section) GetHeader() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualAddOnMarkup_Card_Section) GetWidgets 
    
    
    func (x *ContextualAddOnMarkup_Card_Section) GetWidgets() []*WidgetMarkup

### func (*ContextualAddOnMarkup_Card_Section) ProtoMessage 
    
    
    func (*ContextualAddOnMarkup_Card_Section) ProtoMessage()

### func (*ContextualAddOnMarkup_Card_Section) ProtoReflect 
    
    
    func (x *ContextualAddOnMarkup_Card_Section) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualAddOnMarkup_Card_Section) Reset 
    
    
    func (x *ContextualAddOnMarkup_Card_Section) Reset()

### func (*ContextualAddOnMarkup_Card_Section) String 
    
    
    func (x *ContextualAddOnMarkup_Card_Section) String() [string](https://pkg.go.dev/builtin#string)

## CreateCustomEmojiRequest
    
    
    type CreateCustomEmojiRequest struct {
    
    	// Required. The custom emoji to create.
    	CustomEmoji *CustomEmoji `protobuf:"bytes,1,opt,name=custom_emoji,json=customEmoji,proto3" json:"custom_emoji,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a custom emoji.

### func (*CreateCustomEmojiRequest) Descriptor 
    
    
    func (*CreateCustomEmojiRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateCustomEmojiRequest.ProtoReflect.Descriptor instead.

### func (*CreateCustomEmojiRequest) GetCustomEmoji 
    
    
    func (x *CreateCustomEmojiRequest) GetCustomEmoji() *CustomEmoji

### func (*CreateCustomEmojiRequest) ProtoMessage 
    
    
    func (*CreateCustomEmojiRequest) ProtoMessage()

### func (*CreateCustomEmojiRequest) ProtoReflect 
    
    
    func (x *CreateCustomEmojiRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateCustomEmojiRequest) Reset 
    
    
    func (x *CreateCustomEmojiRequest) Reset()

### func (*CreateCustomEmojiRequest) String 
    
    
    func (x *CreateCustomEmojiRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateMembershipRequest
    
    
    type CreateMembershipRequest struct {
    
    	// Required. The resource name of the space for which to create the
    	// membership.
    	//
    	// Format: spaces/{space}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The membership relation to create.
    	//
    	// The `memberType` field must contain a user with the `user.name` and
    	// `user.type` fields populated. The server will assign a resource name
    	// and overwrite anything specified.
    	//
    	// When a Chat app creates a membership relation for a human user, it must use
    	// certain authorization scopes and set specific values for certain fields:
    	//
    	// - When [authenticating as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// the `chat.memberships` authorization scope is required.
    	//
    	// - When [authenticating as an
    	// app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app),
    	// the `chat.app.memberships` authorization scope is required.
    	//
    	// - Set `user.type` to `HUMAN`, and set `user.name` with format
    	// `users/{user}`, where `{user}` can be the email address for the user. For
    	// users in the same Workspace organization `{user}` can also be the `id` of
    	// the [person](https://developers.google.com/people/api/rest/v1/people) from
    	// the People API, or the `id` for the user in the Directory API. For example,
    	// if the People API Person profile ID for `user@example.com` is `123456789`,
    	// you can add the user to the space by setting the `membership.member.name`
    	// to `users/user@example.com` or `users/123456789`.
    	//
    	// Inviting users external to the Workspace organization that owns the space
    	// requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	//
    	// When a Chat app creates a membership relation for itself, it must
    	// [authenticate as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set
    	// `user.name` to `users/app`.
    	Membership *Membership `protobuf:"bytes,2,opt,name=membership,proto3" json:"membership,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.memberships` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	//
    	// Creating app memberships or creating memberships for users outside the
    	// administrator's Google Workspace organization isn't supported using admin
    	// access.
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for creating a membership.

### func (*CreateMembershipRequest) Descriptor 
    
    
    func (*CreateMembershipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMembershipRequest.ProtoReflect.Descriptor instead.

### func (*CreateMembershipRequest) GetMembership 
    
    
    func (x *CreateMembershipRequest) GetMembership() *Membership

### func (*CreateMembershipRequest) GetParent 
    
    
    func (x *CreateMembershipRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateMembershipRequest) GetUseAdminAccess 
    
    
    func (x *CreateMembershipRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*CreateMembershipRequest) ProtoMessage 
    
    
    func (*CreateMembershipRequest) ProtoMessage()

### func (*CreateMembershipRequest) ProtoReflect 
    
    
    func (x *CreateMembershipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateMembershipRequest) Reset 
    
    
    func (x *CreateMembershipRequest) Reset()

### func (*CreateMembershipRequest) String 
    
    
    func (x *CreateMembershipRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateMessageNotificationOptions
    
    
    type CreateMessageNotificationOptions struct {
    
    	// The notification type for the message.
    	NotificationType CreateMessageNotificationOptions_NotificationType `protobuf:"varint,1,opt,name=notification_type,json=notificationType,proto3,enum=google.chat.v1.CreateMessageNotificationOptions_NotificationType" json:"notification_type,omitempty"`
    	// contains filtered or unexported fields
    }

Options for the notification behavior when the message is posted.

### func (*CreateMessageNotificationOptions) Descriptor 
    
    
    func (*CreateMessageNotificationOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMessageNotificationOptions.ProtoReflect.Descriptor instead.

### func (*CreateMessageNotificationOptions) GetNotificationType 
    
    
    func (x *CreateMessageNotificationOptions) GetNotificationType() CreateMessageNotificationOptions_NotificationType

### func (*CreateMessageNotificationOptions) ProtoMessage 
    
    
    func (*CreateMessageNotificationOptions) ProtoMessage()

### func (*CreateMessageNotificationOptions) ProtoReflect 
    
    
    func (x *CreateMessageNotificationOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateMessageNotificationOptions) Reset 
    
    
    func (x *CreateMessageNotificationOptions) Reset()

### func (*CreateMessageNotificationOptions) String 
    
    
    func (x *CreateMessageNotificationOptions) String() [string](https://pkg.go.dev/builtin#string)

## CreateMessageNotificationOptions_NotificationType
    
    
    type CreateMessageNotificationOptions_NotificationType [int32](https://pkg.go.dev/builtin#int32)

The notification types options for the message.

### CreateMessageNotificationOptions_NOTIFICATION_TYPE_NONE, CreateMessageNotificationOptions_NOTIFICATION_TYPE_FORCE_NOTIFY, CreateMessageNotificationOptions_NOTIFICATION_TYPE_SILENT
    
    
    const (
    	// Default behavior. Notification behavior is similar to when the human user
    	// sends the message using the Chat UI: no notification is sent to the
    	// human sender.
    	CreateMessageNotificationOptions_NOTIFICATION_TYPE_NONE CreateMessageNotificationOptions_NotificationType = 0
    	// Force notify recipients. This bypasses users' space notification settings
    	// and [Chat Do Not Disturb
    	// settings](https://support.google.com/chat/answer/9093489). This option
    	// does not bypass device-level Do Not Disturb settings.
    	//
    	// Requires [app authentication]
    	// (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    	CreateMessageNotificationOptions_NOTIFICATION_TYPE_FORCE_NOTIFY CreateMessageNotificationOptions_NotificationType = 2
    	// Do not notify recipients, and do not mark the message as unread.
    	// This behaves similarly to the user muting the conversation or enabling
    	// [Chat Do Not Disturb](https://support.google.com/chat/answer/9093489).
    	//
    	// Requires [app authentication]
    	// (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    	CreateMessageNotificationOptions_NOTIFICATION_TYPE_SILENT CreateMessageNotificationOptions_NotificationType = 3
    )

### func (CreateMessageNotificationOptions_NotificationType) Descriptor 
    
    
    func (CreateMessageNotificationOptions_NotificationType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CreateMessageNotificationOptions_NotificationType) Enum 
    
    
    func (x CreateMessageNotificationOptions_NotificationType) Enum() *CreateMessageNotificationOptions_NotificationType

### func (CreateMessageNotificationOptions_NotificationType) EnumDescriptor 
    
    
    func (CreateMessageNotificationOptions_NotificationType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMessageNotificationOptions_NotificationType.Descriptor instead.

### func (CreateMessageNotificationOptions_NotificationType) Number 
    
    
    func (x CreateMessageNotificationOptions_NotificationType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CreateMessageNotificationOptions_NotificationType) String 
    
    
    func (x CreateMessageNotificationOptions_NotificationType) String() [string](https://pkg.go.dev/builtin#string)

### func (CreateMessageNotificationOptions_NotificationType) Type 
    
    
    func (CreateMessageNotificationOptions_NotificationType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CreateMessagePinRequest
    
    
    type CreateMessagePinRequest struct {
    
    	// Required. The parent space in which to create the message pin.
    	// Format: spaces/{space}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The MessagePin to create.
    	MessagePin *MessagePin `protobuf:"bytes,2,opt,name=message_pin,json=messagePin,proto3" json:"message_pin,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for creating a message pin.

### func (*CreateMessagePinRequest) Descriptor 
    
    
    func (*CreateMessagePinRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMessagePinRequest.ProtoReflect.Descriptor instead.

### func (*CreateMessagePinRequest) GetMessagePin 
    
    
    func (x *CreateMessagePinRequest) GetMessagePin() *MessagePin

### func (*CreateMessagePinRequest) GetParent 
    
    
    func (x *CreateMessagePinRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateMessagePinRequest) ProtoMessage 
    
    
    func (*CreateMessagePinRequest) ProtoMessage()

### func (*CreateMessagePinRequest) ProtoReflect 
    
    
    func (x *CreateMessagePinRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateMessagePinRequest) Reset 
    
    
    func (x *CreateMessagePinRequest) Reset()

### func (*CreateMessagePinRequest) String 
    
    
    func (x *CreateMessagePinRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateMessageRequest
    
    
    type CreateMessageRequest struct {
    
    	// Required. The resource name of the space in which to create a message.
    	//
    	// Format: `spaces/{space}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Message body.
    	Message *Message `protobuf:"bytes,4,opt,name=message,proto3" json:"message,omitempty"`
    	// Optional. Deprecated: Use
    	// [thread.thread_key][google.chat.v1.Thread.thread_key] instead. ID for the
    	// thread. Supports up to 4000 characters. To start or add to a thread, create
    	// a message and specify a `threadKey` or the
    	// [thread.name][google.chat.v1.Thread.name]. For example usage, see [Start or
    	// reply to a message
    	// thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).
    	//
    	// Deprecated: Marked as deprecated in google/chat/v1/message.proto.
    	ThreadKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=thread_key,json=threadKey,proto3" json:"thread_key,omitempty"`
    	// Optional. A unique ID for this request. A random UUID is recommended.
    	// Specifying a request ID makes the request idempotent, which ensures that
    	// multiple identical requests with the same request ID result in only a
    	// single message being created. Subsequent requests with the same request
    	// ID return the existing message and do not update the message, even if the
    	// requested details differ from the current state.
    	//
    	// To use this field effectively:
    	//
    	// - Ensure that subsequent requests are identical and use the same
    	// authentication credentials as the original request.
    	// - If a message was already created with the provided request ID, the
    	// request returns that message. Note that the returned message might not be
    	// fully populated; the API echoes the message in your request with the
    	// system-assigned resource names populated. To retrieve the latest metadata
    	// for the message, call `GetMessage`.
    	// - Reusing an existing request ID with a different authenticated user
    	// results in an error.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. Specifies whether a message starts a thread or replies to one.
    	// Only supported in named spaces.
    	//
    	// When [responding to user
    	// interactions](https://developers.google.com/workspace/chat/receive-respond-interactions),
    	// this field is ignored. For interactions within a thread, the reply is
    	// created in the same thread. Otherwise, the reply is created as a new
    	// thread.
    	MessageReplyOption CreateMessageRequest_MessageReplyOption `protobuf:"varint,8,opt,name=message_reply_option,json=messageReplyOption,proto3,enum=google.chat.v1.CreateMessageRequest_MessageReplyOption" json:"message_reply_option,omitempty"`
    	// Optional. A custom ID for a message. Lets Chat apps get, update, or delete
    	// a message without needing to store the system-assigned ID in the message's
    	// resource name (represented in the message `name` field).
    	//
    	// The value for this field must meet the following requirements:
    	//
    	//   - Begins with `client-`. For example, `client-custom-name` is a valid
    	//     custom ID, but `custom-name` is not.
    	//   - Contains up to 63 characters and only lowercase letters, numbers, and
    	//     hyphens.
    	//   - Is unique within a space. A Chat app can't use the same custom ID for
    	//
    	// different messages.
    	//
    	// For details, see [Name a
    	// message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
    	MessageId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=message_id,json=messageId,proto3" json:"message_id,omitempty"`
    	// Optional. Controls the notification behavior when the message is posted.
    	// To learn more, see [Force notifications or send silent
    	// messages](https://developer.google.com/workspace/chat/create-messages#force-notify-silent).
    	CreateMessageNotificationOptions *CreateMessageNotificationOptions `protobuf:"bytes,10,opt,name=create_message_notification_options,json=createMessageNotificationOptions,proto3" json:"create_message_notification_options,omitempty"`
    	// contains filtered or unexported fields
    }

Creates a message.

### func (*CreateMessageRequest) Descriptor 
    
    
    func (*CreateMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMessageRequest.ProtoReflect.Descriptor instead.

### func (*CreateMessageRequest) GetCreateMessageNotificationOptions 
    
    
    func (x *CreateMessageRequest) GetCreateMessageNotificationOptions() *CreateMessageNotificationOptions

### func (*CreateMessageRequest) GetMessage 
    
    
    func (x *CreateMessageRequest) GetMessage() *Message

### func (*CreateMessageRequest) GetMessageId 
    
    
    func (x *CreateMessageRequest) GetMessageId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateMessageRequest) GetMessageReplyOption 
    
    
    func (x *CreateMessageRequest) GetMessageReplyOption() CreateMessageRequest_MessageReplyOption

### func (*CreateMessageRequest) GetParent 
    
    
    func (x *CreateMessageRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateMessageRequest) GetRequestId 
    
    
    func (x *CreateMessageRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateMessageRequest) GetThreadKey 
    
    
    func (x *CreateMessageRequest) GetThreadKey() [string](https://pkg.go.dev/builtin#string)

Deprecated: Marked as deprecated in google/chat/v1/message.proto.

### func (*CreateMessageRequest) ProtoMessage 
    
    
    func (*CreateMessageRequest) ProtoMessage()

### func (*CreateMessageRequest) ProtoReflect 
    
    
    func (x *CreateMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateMessageRequest) Reset 
    
    
    func (x *CreateMessageRequest) Reset()

### func (*CreateMessageRequest) String 
    
    
    func (x *CreateMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateMessageRequest_MessageReplyOption
    
    
    type CreateMessageRequest_MessageReplyOption [int32](https://pkg.go.dev/builtin#int32)

Specifies how to reply to a message. More states might be added in the future.

### CreateMessageRequest_MESSAGE_REPLY_OPTION_UNSPECIFIED, CreateMessageRequest_REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD, CreateMessageRequest_REPLY_MESSAGE_OR_FAIL
    
    
    const (
    	// Default. Starts a new thread. Using this option ignores any [thread
    	// ID][google.chat.v1.Thread.name] or
    	// [`thread_key`][google.chat.v1.Thread.thread_key] that's included.
    	CreateMessageRequest_MESSAGE_REPLY_OPTION_UNSPECIFIED CreateMessageRequest_MessageReplyOption = 0
    	// Creates the message as a reply to the thread specified by [thread
    	// ID][google.chat.v1.Thread.name] or
    	// [`thread_key`][google.chat.v1.Thread.thread_key]. If it fails, the
    	// message starts a new thread instead.
    	CreateMessageRequest_REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD CreateMessageRequest_MessageReplyOption = 1
    	// Creates the message as a reply to the thread specified by [thread
    	// ID][google.chat.v1.Thread.name] or
    	// [`thread_key`][google.chat.v1.Thread.thread_key]. If a new `thread_key`
    	// is used, a new thread is created. If the message creation fails, a
    	// `NOT_FOUND` error is returned instead.
    	CreateMessageRequest_REPLY_MESSAGE_OR_FAIL CreateMessageRequest_MessageReplyOption = 2
    )

### func (CreateMessageRequest_MessageReplyOption) Descriptor 
    
    
    func (CreateMessageRequest_MessageReplyOption) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CreateMessageRequest_MessageReplyOption) Enum 
    
    
    func (x CreateMessageRequest_MessageReplyOption) Enum() *CreateMessageRequest_MessageReplyOption

### func (CreateMessageRequest_MessageReplyOption) EnumDescriptor 
    
    
    func (CreateMessageRequest_MessageReplyOption) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateMessageRequest_MessageReplyOption.Descriptor instead.

### func (CreateMessageRequest_MessageReplyOption) Number 
    
    
    func (x CreateMessageRequest_MessageReplyOption) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CreateMessageRequest_MessageReplyOption) String 
    
    
    func (x CreateMessageRequest_MessageReplyOption) String() [string](https://pkg.go.dev/builtin#string)

### func (CreateMessageRequest_MessageReplyOption) Type 
    
    
    func (CreateMessageRequest_MessageReplyOption) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CreateReactionRequest
    
    
    type CreateReactionRequest struct {
    
    	// Required. The message where the reaction is created.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The reaction to create.
    	Reaction *Reaction `protobuf:"bytes,2,opt,name=reaction,proto3" json:"reaction,omitempty"`
    	// contains filtered or unexported fields
    }

Creates a reaction to a message.

### func (*CreateReactionRequest) Descriptor 
    
    
    func (*CreateReactionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateReactionRequest.ProtoReflect.Descriptor instead.

### func (*CreateReactionRequest) GetParent 
    
    
    func (x *CreateReactionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReactionRequest) GetReaction 
    
    
    func (x *CreateReactionRequest) GetReaction() *Reaction

### func (*CreateReactionRequest) ProtoMessage 
    
    
    func (*CreateReactionRequest) ProtoMessage()

### func (*CreateReactionRequest) ProtoReflect 
    
    
    func (x *CreateReactionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateReactionRequest) Reset 
    
    
    func (x *CreateReactionRequest) Reset()

### func (*CreateReactionRequest) String 
    
    
    func (x *CreateReactionRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateSectionRequest
    
    
    type CreateSectionRequest struct {
    
    	// Required. The parent resource name where the section is created.
    	//
    	// Format: `users/{user}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The section to create.
    	Section *Section `protobuf:"bytes,2,opt,name=section,proto3" json:"section,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for creating a section.

### func (*CreateSectionRequest) Descriptor 
    
    
    func (*CreateSectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateSectionRequest.ProtoReflect.Descriptor instead.

### func (*CreateSectionRequest) GetParent 
    
    
    func (x *CreateSectionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSectionRequest) GetSection 
    
    
    func (x *CreateSectionRequest) GetSection() *Section

### func (*CreateSectionRequest) ProtoMessage 
    
    
    func (*CreateSectionRequest) ProtoMessage()

### func (*CreateSectionRequest) ProtoReflect 
    
    
    func (x *CreateSectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateSectionRequest) Reset 
    
    
    func (x *CreateSectionRequest) Reset()

### func (*CreateSectionRequest) String 
    
    
    func (x *CreateSectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateSpaceRequest
    
    
    type CreateSpaceRequest struct {
    
    	// Required. The `displayName` and `spaceType` fields must be populated.  Only
    	// `SpaceType.SPACE`  and `SpaceType.GROUP_CHAT` are supported.
    	// `SpaceType.GROUP_CHAT` can only be used if `importMode` is set to true.
    	//
    	// If you receive the error message `ALREADY_EXISTS`,
    	// try a different `displayName`. An existing space within the Google
    	// Workspace organization might already use this display name.
    	//
    	// The space `name` is assigned on the server so anything specified in this
    	// field will be ignored.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// Optional. A unique ID for this request. A random UUID is recommended.
    	// Specifying a request ID makes the request idempotent, which ensures that
    	// multiple identical requests with the same request ID result in only a
    	// single space being created. Subsequent requests with the same request ID
    	// return the existing space and do not update the space, even if the
    	// requested details differ from the current state.
    	//
    	// To use this field effectively:
    	//
    	// - Ensure that subsequent requests are identical and use the same
    	// authentication credentials as the original request.
    	// - If a space was already created with the provided request ID, the request
    	// returns that space. Note that the returned space might not be fully
    	// populated; the API echoes the space in your request with the
    	// system-assigned resource name populated. To retrieve the latest metadata
    	// for the space, call `GetSpace`.
    	// - Reusing an existing request ID with a different authenticated user
    	// results in an error.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a named space with no members.

### func (*CreateSpaceRequest) Descriptor 
    
    
    func (*CreateSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateSpaceRequest.ProtoReflect.Descriptor instead.

### func (*CreateSpaceRequest) GetRequestId 
    
    
    func (x *CreateSpaceRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSpaceRequest) GetSpace 
    
    
    func (x *CreateSpaceRequest) GetSpace() *Space

### func (*CreateSpaceRequest) ProtoMessage 
    
    
    func (*CreateSpaceRequest) ProtoMessage()

### func (*CreateSpaceRequest) ProtoReflect 
    
    
    func (x *CreateSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateSpaceRequest) Reset 
    
    
    func (x *CreateSpaceRequest) Reset()

### func (*CreateSpaceRequest) String 
    
    
    func (x *CreateSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## CustomEmoji
    
    
    type CustomEmoji struct {
    
    	// Identifier. The resource name of the custom emoji, assigned by the server.
    	//
    	// Format: `customEmojis/{customEmoji}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Unique key for the custom emoji resource.
    	Uid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
    	// Optional. Immutable. User-provided name for the custom emoji, which is
    	// unique within the organization.
    	//
    	// Required when the custom emoji is created, output only otherwise.
    	//
    	// Emoji names must start and end with colons, must be lowercase and can only
    	// contain alphanumeric characters, hyphens, and underscores.
    	// Hyphens and underscores should be used to separate words and cannot be used
    	// consecutively.
    	//
    	// Example: `:valid-emoji-name:`
    	EmojiName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=emoji_name,json=emojiName,proto3" json:"emoji_name,omitempty"`
    	// Output only. A temporary image URL for the custom emoji, valid for at least
    	// 10 minutes. Note that this is not populated in the response when the custom
    	// emoji is created.
    	TemporaryImageUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=temporary_image_uri,json=temporaryImageUri,proto3" json:"temporary_image_uri,omitempty"`
    	// Optional. Input only. Payload data.
    	// Required when the custom emoji is created.
    	Payload *CustomEmoji_CustomEmojiPayload `protobuf:"bytes,5,opt,name=payload,proto3" json:"payload,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a [custom emoji](https://support.google.com/chat/answer/12800149).

### func (*CustomEmoji) Descriptor 
    
    
    func (*CustomEmoji) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CustomEmoji.ProtoReflect.Descriptor instead.

### func (*CustomEmoji) GetEmojiName 
    
    
    func (x *CustomEmoji) GetEmojiName() [string](https://pkg.go.dev/builtin#string)

### func (*CustomEmoji) GetName 
    
    
    func (x *CustomEmoji) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CustomEmoji) GetPayload 
    
    
    func (x *CustomEmoji) GetPayload() *CustomEmoji_CustomEmojiPayload

### func (*CustomEmoji) GetTemporaryImageUri 
    
    
    func (x *CustomEmoji) GetTemporaryImageUri() [string](https://pkg.go.dev/builtin#string)

### func (*CustomEmoji) GetUid 
    
    
    func (x *CustomEmoji) GetUid() [string](https://pkg.go.dev/builtin#string)

### func (*CustomEmoji) ProtoMessage 
    
    
    func (*CustomEmoji) ProtoMessage()

### func (*CustomEmoji) ProtoReflect 
    
    
    func (x *CustomEmoji) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CustomEmoji) Reset 
    
    
    func (x *CustomEmoji) Reset()

### func (*CustomEmoji) String 
    
    
    func (x *CustomEmoji) String() [string](https://pkg.go.dev/builtin#string)

## CustomEmojiMetadata
    
    
    type CustomEmojiMetadata struct {
    
    	// The custom emoji.
    	CustomEmoji *CustomEmoji `protobuf:"bytes,1,opt,name=custom_emoji,json=customEmoji,proto3" json:"custom_emoji,omitempty"`
    	// contains filtered or unexported fields
    }

Annotation metadata for custom emoji.

### func (*CustomEmojiMetadata) Descriptor 
    
    
    func (*CustomEmojiMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CustomEmojiMetadata.ProtoReflect.Descriptor instead.

### func (*CustomEmojiMetadata) GetCustomEmoji 
    
    
    func (x *CustomEmojiMetadata) GetCustomEmoji() *CustomEmoji

### func (*CustomEmojiMetadata) ProtoMessage 
    
    
    func (*CustomEmojiMetadata) ProtoMessage()

### func (*CustomEmojiMetadata) ProtoReflect 
    
    
    func (x *CustomEmojiMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CustomEmojiMetadata) Reset 
    
    
    func (x *CustomEmojiMetadata) Reset()

### func (*CustomEmojiMetadata) String 
    
    
    func (x *CustomEmojiMetadata) String() [string](https://pkg.go.dev/builtin#string)

## CustomEmoji_CustomEmojiPayload
    
    
    type CustomEmoji_CustomEmojiPayload struct {
    
    	// Required. Input only. The image used for the custom emoji.
    	//
    	// The payload must be under 256 KB and the dimension of
    	// the image must be square and between 64 and 500 pixels. The
    	// restrictions are subject to change.
    	FileContent [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=file_content,json=fileContent,proto3" json:"file_content,omitempty"`
    	// Required. Input only. The image file name.
    	//
    	// Supported file extensions: `.png`, `.jpg`, `.gif`.
    	Filename [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=filename,proto3" json:"filename,omitempty"`
    	// contains filtered or unexported fields
    }

Payload data for the custom emoji.

### func (*CustomEmoji_CustomEmojiPayload) Descriptor 
    
    
    func (*CustomEmoji_CustomEmojiPayload) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CustomEmoji_CustomEmojiPayload.ProtoReflect.Descriptor instead.

### func (*CustomEmoji_CustomEmojiPayload) GetFileContent 
    
    
    func (x *CustomEmoji_CustomEmojiPayload) GetFileContent() [][byte](https://pkg.go.dev/builtin#byte)

### func (*CustomEmoji_CustomEmojiPayload) GetFilename 
    
    
    func (x *CustomEmoji_CustomEmojiPayload) GetFilename() [string](https://pkg.go.dev/builtin#string)

### func (*CustomEmoji_CustomEmojiPayload) ProtoMessage 
    
    
    func (*CustomEmoji_CustomEmojiPayload) ProtoMessage()

### func (*CustomEmoji_CustomEmojiPayload) ProtoReflect 
    
    
    func (x *CustomEmoji_CustomEmojiPayload) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CustomEmoji_CustomEmojiPayload) Reset 
    
    
    func (x *CustomEmoji_CustomEmojiPayload) Reset()

### func (*CustomEmoji_CustomEmojiPayload) String 
    
    
    func (x *CustomEmoji_CustomEmojiPayload) String() [string](https://pkg.go.dev/builtin#string)

## CustomStatus
    
    
    type CustomStatus struct {
    
    	// Required. The text of the custom status. This will be a string with maximum
    	// length of 64.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// Required. The emoji of the custom status. Only Unicode emojis are
    	// supported; custom emojis are not supported.
    	Emoji *Emoji `protobuf:"bytes,2,opt,name=emoji,proto3" json:"emoji,omitempty"`
    	// The expiration time of the custom status. It can be specified as either
    	// an absolute timestamp or a time-to-live duration.
    	//
    	// Types that are valid to be assigned to Expiration:
    	//
    	//	*CustomStatus_ExpireTime
    	//	*CustomStatus_Ttl
    	Expiration isCustomStatus_Expiration `protobuf_oneof:"expiration"`
    	// contains filtered or unexported fields
    }

Represents a user's custom status in Google Chat. This includes a short text message with an optional emoji that a user sets to give more context about their availability.

### func (*CustomStatus) Descriptor 
    
    
    func (*CustomStatus) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CustomStatus.ProtoReflect.Descriptor instead.

### func (*CustomStatus) GetEmoji 
    
    
    func (x *CustomStatus) GetEmoji() *Emoji

### func (*CustomStatus) GetExpiration 
    
    
    func (x *CustomStatus) GetExpiration() isCustomStatus_Expiration

### func (*CustomStatus) GetExpireTime 
    
    
    func (x *CustomStatus) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*CustomStatus) GetText 
    
    
    func (x *CustomStatus) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*CustomStatus) GetTtl 
    
    
    func (x *CustomStatus) GetTtl() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*CustomStatus) ProtoMessage 
    
    
    func (*CustomStatus) ProtoMessage()

### func (*CustomStatus) ProtoReflect 
    
    
    func (x *CustomStatus) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CustomStatus) Reset 
    
    
    func (x *CustomStatus) Reset()

### func (*CustomStatus) String 
    
    
    func (x *CustomStatus) String() [string](https://pkg.go.dev/builtin#string)

## CustomStatus_ExpireTime
    
    
    type CustomStatus_ExpireTime struct {
    	// The timestamp when the custom status expires.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=expire_time,json=expireTime,proto3,oneof"`
    }

## CustomStatus_Ttl
    
    
    type CustomStatus_Ttl struct {
    	// Input only. The time-to-live duration after which the custom status
    	// expires.
    	Ttl *durationpb.Duration `protobuf:"bytes,4,opt,name=ttl,proto3,oneof"`
    }

## DeleteCustomEmojiRequest
    
    
    type DeleteCustomEmojiRequest struct {
    
    	// Required. Resource name of the custom emoji to delete.
    	//
    	// Format: `customEmojis/{customEmoji}`
    	//
    	// You can use the emoji name as an alias for `{customEmoji}`. For example,
    	// `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name
    	// for a custom emoji.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for deleting a custom emoji.

### func (*DeleteCustomEmojiRequest) Descriptor 
    
    
    func (*DeleteCustomEmojiRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteCustomEmojiRequest.ProtoReflect.Descriptor instead.

### func (*DeleteCustomEmojiRequest) GetName 
    
    
    func (x *DeleteCustomEmojiRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteCustomEmojiRequest) ProtoMessage 
    
    
    func (*DeleteCustomEmojiRequest) ProtoMessage()

### func (*DeleteCustomEmojiRequest) ProtoReflect 
    
    
    func (x *DeleteCustomEmojiRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteCustomEmojiRequest) Reset 
    
    
    func (x *DeleteCustomEmojiRequest) Reset()

### func (*DeleteCustomEmojiRequest) String 
    
    
    func (x *DeleteCustomEmojiRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteMembershipRequest
    
    
    type DeleteMembershipRequest struct {
    
    	// Required. Resource name of the membership to delete. Chat apps can delete
    	// human users' or their own memberships. Chat apps can't delete other apps'
    	// memberships.
    	//
    	// When deleting a human membership, requires the `chat.memberships` scope
    	// with [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	// or the `chat.memberships.app` scope with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// and the `spaces/{space}/members/{member}` format.
    	// You can use the email as an alias for `{member}`. For example,
    	// `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the
    	// email of the Google Chat user.
    	//
    	// When deleting an app membership, requires the `chat.memberships.app` scope
    	// and `spaces/{space}/members/app` format.
    	//
    	// Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.memberships` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	//
    	// Deleting app memberships in a space isn't supported using admin access.
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request to delete a membership in a space.

### func (*DeleteMembershipRequest) Descriptor 
    
    
    func (*DeleteMembershipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteMembershipRequest.ProtoReflect.Descriptor instead.

### func (*DeleteMembershipRequest) GetName 
    
    
    func (x *DeleteMembershipRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteMembershipRequest) GetUseAdminAccess 
    
    
    func (x *DeleteMembershipRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteMembershipRequest) ProtoMessage 
    
    
    func (*DeleteMembershipRequest) ProtoMessage()

### func (*DeleteMembershipRequest) ProtoReflect 
    
    
    func (x *DeleteMembershipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteMembershipRequest) Reset 
    
    
    func (x *DeleteMembershipRequest) Reset()

### func (*DeleteMembershipRequest) String 
    
    
    func (x *DeleteMembershipRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteMessagePinRequest
    
    
    type DeleteMessagePinRequest struct {
    
    	// Required. The resource name of the message pin to remove.
    	// Format: spaces/{space}/messagePins/{message_pin}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for deleting a message pin.

### func (*DeleteMessagePinRequest) Descriptor 
    
    
    func (*DeleteMessagePinRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteMessagePinRequest.ProtoReflect.Descriptor instead.

### func (*DeleteMessagePinRequest) GetName 
    
    
    func (x *DeleteMessagePinRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteMessagePinRequest) ProtoMessage 
    
    
    func (*DeleteMessagePinRequest) ProtoMessage()

### func (*DeleteMessagePinRequest) ProtoReflect 
    
    
    func (x *DeleteMessagePinRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteMessagePinRequest) Reset 
    
    
    func (x *DeleteMessagePinRequest) Reset()

### func (*DeleteMessagePinRequest) String 
    
    
    func (x *DeleteMessagePinRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteMessageRequest
    
    
    type DeleteMessageRequest struct {
    
    	// Required. Resource name of the message.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	//
    	// If you've set a custom ID for your message, you can use the value from the
    	// `clientAssignedMessageId` field for `{message}`. For details, see [Name a
    	// message]
    	// (https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. When `true`, deleting a message also deletes its threaded
    	// replies. When `false`, if a message has threaded replies, deletion fails.
    	//
    	// Only applies when [authenticating as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	// Has no effect when [authenticating as a Chat app]
    	// (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

Request to delete a message.

### func (*DeleteMessageRequest) Descriptor 
    
    
    func (*DeleteMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteMessageRequest.ProtoReflect.Descriptor instead.

### func (*DeleteMessageRequest) GetForce 
    
    
    func (x *DeleteMessageRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteMessageRequest) GetName 
    
    
    func (x *DeleteMessageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteMessageRequest) ProtoMessage 
    
    
    func (*DeleteMessageRequest) ProtoMessage()

### func (*DeleteMessageRequest) ProtoReflect 
    
    
    func (x *DeleteMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteMessageRequest) Reset 
    
    
    func (x *DeleteMessageRequest) Reset()

### func (*DeleteMessageRequest) String 
    
    
    func (x *DeleteMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteReactionRequest
    
    
    type DeleteReactionRequest struct {
    
    	// Required. Name of the reaction to delete.
    	//
    	// Format: `spaces/{space}/messages/{message}/reactions/{reaction}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Deletes a reaction to a message.

### func (*DeleteReactionRequest) Descriptor 
    
    
    func (*DeleteReactionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteReactionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteReactionRequest) GetName 
    
    
    func (x *DeleteReactionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReactionRequest) ProtoMessage 
    
    
    func (*DeleteReactionRequest) ProtoMessage()

### func (*DeleteReactionRequest) ProtoReflect 
    
    
    func (x *DeleteReactionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteReactionRequest) Reset 
    
    
    func (x *DeleteReactionRequest) Reset()

### func (*DeleteReactionRequest) String 
    
    
    func (x *DeleteReactionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteSectionRequest
    
    
    type DeleteSectionRequest struct {
    
    	// Required. The name of the section to delete.
    	//
    	// Format: `users/{user}/sections/{section}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for deleting a section. [Developer Preview](https://developers.google.com/workspace/preview).

### func (*DeleteSectionRequest) Descriptor 
    
    
    func (*DeleteSectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteSectionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteSectionRequest) GetName 
    
    
    func (x *DeleteSectionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteSectionRequest) ProtoMessage 
    
    
    func (*DeleteSectionRequest) ProtoMessage()

### func (*DeleteSectionRequest) ProtoReflect 
    
    
    func (x *DeleteSectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteSectionRequest) Reset 
    
    
    func (x *DeleteSectionRequest) Reset()

### func (*DeleteSectionRequest) String 
    
    
    func (x *DeleteSectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteSpaceRequest
    
    
    type DeleteSpaceRequest struct {
    
    	// Required. Resource name of the space to delete.
    	//
    	// Format: `spaces/{space}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.delete` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request for deleting a space.

### func (*DeleteSpaceRequest) Descriptor 
    
    
    func (*DeleteSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteSpaceRequest.ProtoReflect.Descriptor instead.

### func (*DeleteSpaceRequest) GetName 
    
    
    func (x *DeleteSpaceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteSpaceRequest) GetUseAdminAccess 
    
    
    func (x *DeleteSpaceRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteSpaceRequest) ProtoMessage 
    
    
    func (*DeleteSpaceRequest) ProtoMessage()

### func (*DeleteSpaceRequest) ProtoReflect 
    
    
    func (x *DeleteSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteSpaceRequest) Reset 
    
    
    func (x *DeleteSpaceRequest) Reset()

### func (*DeleteSpaceRequest) String 
    
    
    func (x *DeleteSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeletionMetadata
    
    
    type DeletionMetadata struct {
    
    	// Indicates who deleted the message.
    	DeletionType DeletionMetadata_DeletionType `protobuf:"varint,1,opt,name=deletion_type,json=deletionType,proto3,enum=google.chat.v1.DeletionMetadata_DeletionType" json:"deletion_type,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a deleted message. A message is deleted when `delete_time` is set.

### func (*DeletionMetadata) Descriptor 
    
    
    func (*DeletionMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletionMetadata.ProtoReflect.Descriptor instead.

### func (*DeletionMetadata) GetDeletionType 
    
    
    func (x *DeletionMetadata) GetDeletionType() DeletionMetadata_DeletionType

### func (*DeletionMetadata) ProtoMessage 
    
    
    func (*DeletionMetadata) ProtoMessage()

### func (*DeletionMetadata) ProtoReflect 
    
    
    func (x *DeletionMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeletionMetadata) Reset 
    
    
    func (x *DeletionMetadata) Reset()

### func (*DeletionMetadata) String 
    
    
    func (x *DeletionMetadata) String() [string](https://pkg.go.dev/builtin#string)

## DeletionMetadata_DeletionType
    
    
    type DeletionMetadata_DeletionType [int32](https://pkg.go.dev/builtin#int32)

Who deleted the message and how it was deleted. More values may be added in the future. See [Edit or delete a message in Google Chat](https://support.google.com/chat/answer/7653281) for details on when messages can be deleted.

### DeletionMetadata_DELETION_TYPE_UNSPECIFIED, DeletionMetadata_CREATOR, DeletionMetadata_SPACE_OWNER, DeletionMetadata_ADMIN, DeletionMetadata_APP_MESSAGE_EXPIRY, DeletionMetadata_CREATOR_VIA_APP, DeletionMetadata_SPACE_OWNER_VIA_APP, DeletionMetadata_SPACE_MEMBER
    
    
    const (
    	// This value is unused.
    	DeletionMetadata_DELETION_TYPE_UNSPECIFIED DeletionMetadata_DeletionType = 0
    	// User deleted their own message.
    	DeletionMetadata_CREATOR DeletionMetadata_DeletionType = 1
    	// An owner or manager deleted the message.
    	DeletionMetadata_SPACE_OWNER DeletionMetadata_DeletionType = 2
    	// A Google Workspace administrator deleted the message. Administrators can
    	// delete any message in the space, including messages sent by any space
    	// member or Chat app.
    	DeletionMetadata_ADMIN DeletionMetadata_DeletionType = 3
    	// A Chat app deleted its own message when it expired.
    	DeletionMetadata_APP_MESSAGE_EXPIRY DeletionMetadata_DeletionType = 4
    	// A Chat app deleted the message on behalf of the creator (using user
    	// authentication).
    	DeletionMetadata_CREATOR_VIA_APP DeletionMetadata_DeletionType = 5
    	// A Chat app deleted the message on behalf of a space manager (using user
    	// authentication).
    	DeletionMetadata_SPACE_OWNER_VIA_APP DeletionMetadata_DeletionType = 6
    	// A member of the space deleted the message. Users can delete messages sent
    	// by apps.
    	DeletionMetadata_SPACE_MEMBER DeletionMetadata_DeletionType = 7
    )

### func (DeletionMetadata_DeletionType) Descriptor 
    
    
    func (DeletionMetadata_DeletionType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (DeletionMetadata_DeletionType) Enum 
    
    
    func (x DeletionMetadata_DeletionType) Enum() *DeletionMetadata_DeletionType

### func (DeletionMetadata_DeletionType) EnumDescriptor 
    
    
    func (DeletionMetadata_DeletionType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletionMetadata_DeletionType.Descriptor instead.

### func (DeletionMetadata_DeletionType) Number 
    
    
    func (x DeletionMetadata_DeletionType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (DeletionMetadata_DeletionType) String 
    
    
    func (x DeletionMetadata_DeletionType) String() [string](https://pkg.go.dev/builtin#string)

### func (DeletionMetadata_DeletionType) Type 
    
    
    func (DeletionMetadata_DeletionType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Dialog
    
    
    type Dialog struct {
    
    	// Input only. Body of the dialog, which is rendered in a modal.
    	// Google Chat apps don't support the following card entities:
    	// `DateTimePicker`, `OnChangeAction`.
    	Body *v1.Card `protobuf:"bytes,1,opt,name=body,proto3" json:"body,omitempty"`
    	// contains filtered or unexported fields
    }

Wrapper around the card body of the dialog.

### func (*Dialog) Descriptor 
    
    
    func (*Dialog) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Dialog.ProtoReflect.Descriptor instead.

### func (*Dialog) GetBody 
    
    
    func (x *Dialog) GetBody() *[v1](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1).[Card](https://pkg.go.dev/google.golang.org/genproto/googleapis/apps/card/v1#Card)

### func (*Dialog) ProtoMessage 
    
    
    func (*Dialog) ProtoMessage()

### func (*Dialog) ProtoReflect 
    
    
    func (x *Dialog) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Dialog) Reset 
    
    
    func (x *Dialog) Reset()

### func (*Dialog) String 
    
    
    func (x *Dialog) String() [string](https://pkg.go.dev/builtin#string)

## DialogAction
    
    
    type DialogAction struct {
    
    	// Action to perform.
    	//
    	// Types that are valid to be assigned to Action:
    	//
    	//	*DialogAction_Dialog
    	Action isDialogAction_Action `protobuf_oneof:"action"`
    	// Input only. Status for a request to either invoke or submit a
    	// [dialog](https://developers.google.com/workspace/chat/dialogs). Displays
    	// a status and message to users, if necessary.
    	// For example, in case of an error or success.
    	ActionStatus *ActionStatus `protobuf:"bytes,2,opt,name=action_status,json=actionStatus,proto3" json:"action_status,omitempty"`
    	// contains filtered or unexported fields
    }

Contains a [dialog](https://developers.google.com/workspace/chat/dialogs) and request status code.

### func (*DialogAction) Descriptor 
    
    
    func (*DialogAction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DialogAction.ProtoReflect.Descriptor instead.

### func (*DialogAction) GetAction 
    
    
    func (x *DialogAction) GetAction() isDialogAction_Action

### func (*DialogAction) GetActionStatus 
    
    
    func (x *DialogAction) GetActionStatus() *ActionStatus

### func (*DialogAction) GetDialog 
    
    
    func (x *DialogAction) GetDialog() *Dialog

### func (*DialogAction) ProtoMessage 
    
    
    func (*DialogAction) ProtoMessage()

### func (*DialogAction) ProtoReflect 
    
    
    func (x *DialogAction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DialogAction) Reset 
    
    
    func (x *DialogAction) Reset()

### func (*DialogAction) String 
    
    
    func (x *DialogAction) String() [string](https://pkg.go.dev/builtin#string)

## DialogAction_Dialog
    
    
    type DialogAction_Dialog struct {
    	// Input only.
    	// [Dialog](https://developers.google.com/workspace/chat/dialogs) for the
    	// request.
    	Dialog *Dialog `protobuf:"bytes,1,opt,name=dialog,proto3,oneof"`
    }

## DoNotDisturbMetadata
    
    
    type DoNotDisturbMetadata struct {
    
    	// Output only. Timestamp until which the user should be marked as
    	// DO_NOT_DISTURB. This can be maximum of 1 year in the future.
    	ExpirationTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=expiration_time,json=expirationTime,proto3" json:"expiration_time,omitempty"`
    	// contains filtered or unexported fields
    }

Metadata associated with the `DO_NOT_DISTURB` availability state, specifying when the state is set to expire.

### func (*DoNotDisturbMetadata) Descriptor 
    
    
    func (*DoNotDisturbMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DoNotDisturbMetadata.ProtoReflect.Descriptor instead.

### func (*DoNotDisturbMetadata) GetExpirationTime 
    
    
    func (x *DoNotDisturbMetadata) GetExpirationTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*DoNotDisturbMetadata) ProtoMessage 
    
    
    func (*DoNotDisturbMetadata) ProtoMessage()

### func (*DoNotDisturbMetadata) ProtoReflect 
    
    
    func (x *DoNotDisturbMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DoNotDisturbMetadata) Reset 
    
    
    func (x *DoNotDisturbMetadata) Reset()

### func (*DoNotDisturbMetadata) String 
    
    
    func (x *DoNotDisturbMetadata) String() [string](https://pkg.go.dev/builtin#string)

## DriveDataRef
    
    
    type DriveDataRef struct {
    
    	// The ID for the drive file. Use with the Drive API.
    	DriveFileId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=drive_file_id,json=driveFileId,proto3" json:"drive_file_id,omitempty"`
    	// contains filtered or unexported fields
    }

A reference to the data of a drive attachment.

### func (*DriveDataRef) Descriptor 
    
    
    func (*DriveDataRef) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DriveDataRef.ProtoReflect.Descriptor instead.

### func (*DriveDataRef) GetDriveFileId 
    
    
    func (x *DriveDataRef) GetDriveFileId() [string](https://pkg.go.dev/builtin#string)

### func (*DriveDataRef) ProtoMessage 
    
    
    func (*DriveDataRef) ProtoMessage()

### func (*DriveDataRef) ProtoReflect 
    
    
    func (x *DriveDataRef) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DriveDataRef) Reset 
    
    
    func (x *DriveDataRef) Reset()

### func (*DriveDataRef) String 
    
    
    func (x *DriveDataRef) String() [string](https://pkg.go.dev/builtin#string)

## DriveLinkData
    
    
    type DriveLinkData struct {
    
    	// A
    	// [DriveDataRef](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments#drivedataref)
    	// which references a Google Drive file.
    	DriveDataRef *DriveDataRef `protobuf:"bytes,1,opt,name=drive_data_ref,json=driveDataRef,proto3" json:"drive_data_ref,omitempty"`
    	// The mime type of the linked Google Drive resource.
    	MimeType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=mime_type,json=mimeType,proto3" json:"mime_type,omitempty"`
    	// contains filtered or unexported fields
    }

Data for Google Drive links.

### func (*DriveLinkData) Descriptor 
    
    
    func (*DriveLinkData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DriveLinkData.ProtoReflect.Descriptor instead.

### func (*DriveLinkData) GetDriveDataRef 
    
    
    func (x *DriveLinkData) GetDriveDataRef() *DriveDataRef

### func (*DriveLinkData) GetMimeType 
    
    
    func (x *DriveLinkData) GetMimeType() [string](https://pkg.go.dev/builtin#string)

### func (*DriveLinkData) ProtoMessage 
    
    
    func (*DriveLinkData) ProtoMessage()

### func (*DriveLinkData) ProtoReflect 
    
    
    func (x *DriveLinkData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DriveLinkData) Reset 
    
    
    func (x *DriveLinkData) Reset()

### func (*DriveLinkData) String 
    
    
    func (x *DriveLinkData) String() [string](https://pkg.go.dev/builtin#string)

## Emoji
    
    
    type Emoji struct {
    
    	// Required. The content of the emoji.
    	//
    	// Types that are valid to be assigned to Content:
    	//
    	//	*Emoji_Unicode
    	//	*Emoji_CustomEmoji
    	Content isEmoji_Content `protobuf_oneof:"content"`
    	// contains filtered or unexported fields
    }

An emoji that is used as a reaction to a message.

### func (*Emoji) Descriptor 
    
    
    func (*Emoji) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Emoji.ProtoReflect.Descriptor instead.

### func (*Emoji) GetContent 
    
    
    func (x *Emoji) GetContent() isEmoji_Content

### func (*Emoji) GetCustomEmoji 
    
    
    func (x *Emoji) GetCustomEmoji() *CustomEmoji

### func (*Emoji) GetUnicode 
    
    
    func (x *Emoji) GetUnicode() [string](https://pkg.go.dev/builtin#string)

### func (*Emoji) ProtoMessage 
    
    
    func (*Emoji) ProtoMessage()

### func (*Emoji) ProtoReflect 
    
    
    func (x *Emoji) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Emoji) Reset 
    
    
    func (x *Emoji) Reset()

### func (*Emoji) String 
    
    
    func (x *Emoji) String() [string](https://pkg.go.dev/builtin#string)

## EmojiReactionSummary
    
    
    type EmojiReactionSummary struct {
    
    	// Output only. Emoji associated with the reactions.
    	Emoji *Emoji `protobuf:"bytes,1,opt,name=emoji,proto3" json:"emoji,omitempty"`
    	// Output only. The total number of reactions using the associated emoji.
    	ReactionCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=reaction_count,json=reactionCount,proto3,oneof" json:"reaction_count,omitempty"`
    	// contains filtered or unexported fields
    }

The number of people who reacted to a message with a specific emoji.

### func (*EmojiReactionSummary) Descriptor 
    
    
    func (*EmojiReactionSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EmojiReactionSummary.ProtoReflect.Descriptor instead.

### func (*EmojiReactionSummary) GetEmoji 
    
    
    func (x *EmojiReactionSummary) GetEmoji() *Emoji

### func (*EmojiReactionSummary) GetReactionCount 
    
    
    func (x *EmojiReactionSummary) GetReactionCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*EmojiReactionSummary) ProtoMessage 
    
    
    func (*EmojiReactionSummary) ProtoMessage()

### func (*EmojiReactionSummary) ProtoReflect 
    
    
    func (x *EmojiReactionSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EmojiReactionSummary) Reset 
    
    
    func (x *EmojiReactionSummary) Reset()

### func (*EmojiReactionSummary) String 
    
    
    func (x *EmojiReactionSummary) String() [string](https://pkg.go.dev/builtin#string)

## Emoji_CustomEmoji
    
    
    type Emoji_CustomEmoji struct {
    	// A custom emoji.
    	CustomEmoji *CustomEmoji `protobuf:"bytes,2,opt,name=custom_emoji,json=customEmoji,proto3,oneof"`
    }

## Emoji_Unicode
    
    
    type Emoji_Unicode struct {
    	// Optional. A basic emoji represented by a unicode string.
    	Unicode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=unicode,proto3,oneof"`
    }

## FindDirectMessageRequest
    
    
    type FindDirectMessageRequest struct {
    
    	// Required. Resource name of the user to find direct message with.
    	//
    	// Format: `users/{user}`, where `{user}` is either the `id` for the
    	// [person](https://developers.google.com/people/api/rest/v1/people) from the
    	// People API, or the `id` for the
    	// [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
    	// in the Directory API. For example, if the People API profile ID is
    	// `123456789`, you can find a direct message with that person by using
    	// `users/123456789` as the `name`. When [authenticated as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// you can use the email as an alias for `{user}`. For example,
    	// `users/example@gmail.com` where `example@gmail.com` is the email of the
    	// Google Chat user.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get direct message space based on the user resource.

### func (*FindDirectMessageRequest) Descriptor 
    
    
    func (*FindDirectMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FindDirectMessageRequest.ProtoReflect.Descriptor instead.

### func (*FindDirectMessageRequest) GetName 
    
    
    func (x *FindDirectMessageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*FindDirectMessageRequest) ProtoMessage 
    
    
    func (*FindDirectMessageRequest) ProtoMessage()

### func (*FindDirectMessageRequest) ProtoReflect 
    
    
    func (x *FindDirectMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FindDirectMessageRequest) Reset 
    
    
    func (x *FindDirectMessageRequest) Reset()

### func (*FindDirectMessageRequest) String 
    
    
    func (x *FindDirectMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## FindGroupChatsRequest
    
    
    type FindGroupChatsRequest struct {
    
    	// Optional. Resource names of all human users in group chat with the calling
    	// user. Chat apps can't be included in the request.
    	//
    	// The maximum number of users that can be specified in a single request is
    	// `49`.
    	//
    	// Format: `users/{user}`, where `{user}` is either the `id` for the
    	// [person](https://developers.google.com/people/api/rest/v1/people) from the
    	// People API, or the `id` for the
    	// [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
    	// in the Directory API. For example, to find all group chats with the calling
    	// user and two other users, with People API profile IDs `123456789` and
    	// `987654321`, you can use `users/123456789` and `users/987654321`.
    	// You can also use the email as an alias for `{user}`. For example,
    	// `users/example@gmail.com` where `example@gmail.com` is the email of the
    	// Google Chat user.
    	Users [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=users,proto3" json:"users,omitempty"`
    	// Optional. The maximum number of spaces to return. The service might return
    	// fewer than this value.
    	//
    	// If unspecified, at most 10 spaces are returned.
    	//
    	// The maximum value is 30. If you use a value more than 30, it's
    	// automatically changed to 30.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous call to find group chats.
    	// Provide this parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the token. Passing different values may lead to unexpected
    	// results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Requested space view type. If unset, defaults to
    	// `SPACE_VIEW_RESOURCE_NAME_ONLY`. Requests that specify
    	// `SPACE_VIEW_EXPANDED` must include scopes that allow reading space data,
    	// for example,
    	// https://www.googleapis.com/auth/chat.spaces or
    	// https://www.googleapis.com/auth/chat.spaces.readonly.
    	SpaceView SpaceView `protobuf:"varint,4,opt,name=space_view,json=spaceView,proto3,enum=google.chat.v1.SpaceView" json:"space_view,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get group chat spaces based on user resources.

### func (*FindGroupChatsRequest) Descriptor 
    
    
    func (*FindGroupChatsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FindGroupChatsRequest.ProtoReflect.Descriptor instead.

### func (*FindGroupChatsRequest) GetPageSize 
    
    
    func (x *FindGroupChatsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*FindGroupChatsRequest) GetPageToken 
    
    
    func (x *FindGroupChatsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*FindGroupChatsRequest) GetSpaceView 
    
    
    func (x *FindGroupChatsRequest) GetSpaceView() SpaceView

### func (*FindGroupChatsRequest) GetUsers 
    
    
    func (x *FindGroupChatsRequest) GetUsers() [][string](https://pkg.go.dev/builtin#string)

### func (*FindGroupChatsRequest) ProtoMessage 
    
    
    func (*FindGroupChatsRequest) ProtoMessage()

### func (*FindGroupChatsRequest) ProtoReflect 
    
    
    func (x *FindGroupChatsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FindGroupChatsRequest) Reset 
    
    
    func (x *FindGroupChatsRequest) Reset()

### func (*FindGroupChatsRequest) String 
    
    
    func (x *FindGroupChatsRequest) String() [string](https://pkg.go.dev/builtin#string)

## FindGroupChatsResponse
    
    
    type FindGroupChatsResponse struct {
    
    	// List of spaces in the requested (or first) page.
    	Spaces []*Space `protobuf:"bytes,1,rep,name=spaces,proto3" json:"spaces,omitempty"`
    	// A token that you can send as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

A response containing group chat spaces with exactly the calling user and the requested users.

### func (*FindGroupChatsResponse) Descriptor 
    
    
    func (*FindGroupChatsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FindGroupChatsResponse.ProtoReflect.Descriptor instead.

### func (*FindGroupChatsResponse) GetNextPageToken 
    
    
    func (x *FindGroupChatsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*FindGroupChatsResponse) GetSpaces 
    
    
    func (x *FindGroupChatsResponse) GetSpaces() []*Space

### func (*FindGroupChatsResponse) ProtoMessage 
    
    
    func (*FindGroupChatsResponse) ProtoMessage()

### func (*FindGroupChatsResponse) ProtoReflect 
    
    
    func (x *FindGroupChatsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FindGroupChatsResponse) Reset 
    
    
    func (x *FindGroupChatsResponse) Reset()

### func (*FindGroupChatsResponse) String 
    
    
    func (x *FindGroupChatsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ForwardedMetadata
    
    
    type ForwardedMetadata struct {
    
    	// Output only. The resource name of the source space.
    	// Format: spaces/{space}
    	Space [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// Output only. The display name of the source space or DM at the time of
    	// forwarding. For `SPACE`, this is the space name. For `DIRECT_MESSAGE`, this
    	// is the other participant's name (e.g., "User A"). For `GROUP_CHAT`, this is
    	// a generated name based on members' first names, limited to 5 including the
    	// creator (e.g., "User A, User B").
    	SpaceDisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=space_display_name,json=spaceDisplayName,proto3" json:"space_display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Metadata about the source space from which a message was forwarded.

### func (*ForwardedMetadata) Descriptor 
    
    
    func (*ForwardedMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ForwardedMetadata.ProtoReflect.Descriptor instead.

### func (*ForwardedMetadata) GetSpace 
    
    
    func (x *ForwardedMetadata) GetSpace() [string](https://pkg.go.dev/builtin#string)

### func (*ForwardedMetadata) GetSpaceDisplayName 
    
    
    func (x *ForwardedMetadata) GetSpaceDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ForwardedMetadata) ProtoMessage 
    
    
    func (*ForwardedMetadata) ProtoMessage()

### func (*ForwardedMetadata) ProtoReflect 
    
    
    func (x *ForwardedMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ForwardedMetadata) Reset 
    
    
    func (x *ForwardedMetadata) Reset()

### func (*ForwardedMetadata) String 
    
    
    func (x *ForwardedMetadata) String() [string](https://pkg.go.dev/builtin#string)

## GetAttachmentRequest
    
    
    type GetAttachmentRequest struct {
    
    	// Required. Resource name of the attachment, in the form
    	// `spaces/{space}/messages/{message}/attachments/{attachment}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get an attachment.

### func (*GetAttachmentRequest) Descriptor 
    
    
    func (*GetAttachmentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAttachmentRequest.ProtoReflect.Descriptor instead.

### func (*GetAttachmentRequest) GetName 
    
    
    func (x *GetAttachmentRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAttachmentRequest) ProtoMessage 
    
    
    func (*GetAttachmentRequest) ProtoMessage()

### func (*GetAttachmentRequest) ProtoReflect 
    
    
    func (x *GetAttachmentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAttachmentRequest) Reset 
    
    
    func (x *GetAttachmentRequest) Reset()

### func (*GetAttachmentRequest) String 
    
    
    func (x *GetAttachmentRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAvailabilityRequest
    
    
    type GetAvailabilityRequest struct {
    
    	// Required. The resource name of the availability to retrieve.
    	//
    	// Format: users/{user}/availability
    	//
    	// `{user}` is the id for the Person in the People API or Admin SDK directory
    	// API. For example, `users/123456789`.
    	//
    	// The user's email address or `me` can also be used as an alias to refer to
    	// the caller.  For example, `users/user@example.com` or `users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `GetAvailability` method.

### func (*GetAvailabilityRequest) Descriptor 
    
    
    func (*GetAvailabilityRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAvailabilityRequest.ProtoReflect.Descriptor instead.

### func (*GetAvailabilityRequest) GetName 
    
    
    func (x *GetAvailabilityRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAvailabilityRequest) ProtoMessage 
    
    
    func (*GetAvailabilityRequest) ProtoMessage()

### func (*GetAvailabilityRequest) ProtoReflect 
    
    
    func (x *GetAvailabilityRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAvailabilityRequest) Reset 
    
    
    func (x *GetAvailabilityRequest) Reset()

### func (*GetAvailabilityRequest) String 
    
    
    func (x *GetAvailabilityRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetCustomEmojiRequest
    
    
    type GetCustomEmojiRequest struct {
    
    	// Required. Resource name of the custom emoji.
    	//
    	// Format: `customEmojis/{customEmoji}`
    	//
    	// You can use the emoji name as an alias for `{customEmoji}`. For example,
    	// `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name
    	// for a custom emoji.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to return a single custom emoji.

### func (*GetCustomEmojiRequest) Descriptor 
    
    
    func (*GetCustomEmojiRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCustomEmojiRequest.ProtoReflect.Descriptor instead.

### func (*GetCustomEmojiRequest) GetName 
    
    
    func (x *GetCustomEmojiRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCustomEmojiRequest) ProtoMessage 
    
    
    func (*GetCustomEmojiRequest) ProtoMessage()

### func (*GetCustomEmojiRequest) ProtoReflect 
    
    
    func (x *GetCustomEmojiRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCustomEmojiRequest) Reset 
    
    
    func (x *GetCustomEmojiRequest) Reset()

### func (*GetCustomEmojiRequest) String 
    
    
    func (x *GetCustomEmojiRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetMembershipRequest
    
    
    type GetMembershipRequest struct {
    
    	// Required. Resource name of the membership to retrieve.
    	//
    	// To get the app's own membership [by using user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// you can optionally use `spaces/{space}/members/app`.
    	//
    	// Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app`
    	//
    	// You can use the user's email as an alias for `{member}`. For example,
    	// `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the
    	// email of the Google Chat user.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.memberships` or `chat.admin.memberships.readonly`
    	// [OAuth 2.0
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	//
    	// Getting app memberships in a space isn't supported when using admin access.
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get a membership of a space.

### func (*GetMembershipRequest) Descriptor 
    
    
    func (*GetMembershipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetMembershipRequest.ProtoReflect.Descriptor instead.

### func (*GetMembershipRequest) GetName 
    
    
    func (x *GetMembershipRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetMembershipRequest) GetUseAdminAccess 
    
    
    func (x *GetMembershipRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*GetMembershipRequest) ProtoMessage 
    
    
    func (*GetMembershipRequest) ProtoMessage()

### func (*GetMembershipRequest) ProtoReflect 
    
    
    func (x *GetMembershipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetMembershipRequest) Reset 
    
    
    func (x *GetMembershipRequest) Reset()

### func (*GetMembershipRequest) String 
    
    
    func (x *GetMembershipRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetMessageRequest
    
    
    type GetMessageRequest struct {
    
    	// Required. Resource name of the message.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	//
    	// If you've set a custom ID for your message, you can use the value from the
    	// `clientAssignedMessageId` field for `{message}`. For details, see [Name a
    	// message]
    	// (https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Specifies the desired output syntax for the Chat message
    	// `formatted_text` field.
    	MarkupSyntax MarkupSyntax `protobuf:"varint,3,opt,name=markup_syntax,json=markupSyntax,proto3,enum=google.chat.v1.MarkupSyntax" json:"markup_syntax,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get a message.

### func (*GetMessageRequest) Descriptor 
    
    
    func (*GetMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetMessageRequest.ProtoReflect.Descriptor instead.

### func (*GetMessageRequest) GetMarkupSyntax 
    
    
    func (x *GetMessageRequest) GetMarkupSyntax() MarkupSyntax

### func (*GetMessageRequest) GetName 
    
    
    func (x *GetMessageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetMessageRequest) ProtoMessage 
    
    
    func (*GetMessageRequest) ProtoMessage()

### func (*GetMessageRequest) ProtoReflect 
    
    
    func (x *GetMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetMessageRequest) Reset 
    
    
    func (x *GetMessageRequest) Reset()

### func (*GetMessageRequest) String 
    
    
    func (x *GetMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSpaceEventRequest
    
    
    type GetSpaceEventRequest struct {
    
    	// Required. The resource name of the space event.
    	//
    	// Format: `spaces/{space}/spaceEvents/{spaceEvent}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for getting a space event.

### func (*GetSpaceEventRequest) Descriptor 
    
    
    func (*GetSpaceEventRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSpaceEventRequest.ProtoReflect.Descriptor instead.

### func (*GetSpaceEventRequest) GetName 
    
    
    func (x *GetSpaceEventRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSpaceEventRequest) ProtoMessage 
    
    
    func (*GetSpaceEventRequest) ProtoMessage()

### func (*GetSpaceEventRequest) ProtoReflect 
    
    
    func (x *GetSpaceEventRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSpaceEventRequest) Reset 
    
    
    func (x *GetSpaceEventRequest) Reset()

### func (*GetSpaceEventRequest) String 
    
    
    func (x *GetSpaceEventRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSpaceNotificationSettingRequest
    
    
    type GetSpaceNotificationSettingRequest struct {
    
    	// Required. Format: users/{user}/spaces/{space}/spaceNotificationSetting
    	//
    	// - `users/me/spaces/{space}/spaceNotificationSetting`, OR
    	// - `users/user@example.com/spaces/{space}/spaceNotificationSetting`, OR
    	// - `users/123456789/spaces/{space}/spaceNotificationSetting`.
    	// Note: Only the caller's user id or email is allowed in the path.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message to get space notification setting. Only supports getting notification setting for the calling user.

### func (*GetSpaceNotificationSettingRequest) Descriptor 
    
    
    func (*GetSpaceNotificationSettingRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSpaceNotificationSettingRequest.ProtoReflect.Descriptor instead.

### func (*GetSpaceNotificationSettingRequest) GetName 
    
    
    func (x *GetSpaceNotificationSettingRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSpaceNotificationSettingRequest) ProtoMessage 
    
    
    func (*GetSpaceNotificationSettingRequest) ProtoMessage()

### func (*GetSpaceNotificationSettingRequest) ProtoReflect 
    
    
    func (x *GetSpaceNotificationSettingRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSpaceNotificationSettingRequest) Reset 
    
    
    func (x *GetSpaceNotificationSettingRequest) Reset()

### func (*GetSpaceNotificationSettingRequest) String 
    
    
    func (x *GetSpaceNotificationSettingRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSpaceReadStateRequest
    
    
    type GetSpaceReadStateRequest struct {
    
    	// Required. Resource name of the space read state to retrieve.
    	//
    	// Only supports getting read state for the calling user.
    	//
    	// To refer to the calling user, set one of the following:
    	//
    	// - The `me` alias. For example, `users/me/spaces/{space}/spaceReadState`.
    	//
    	// - Their Workspace email address. For example,
    	// `users/user@example.com/spaces/{space}/spaceReadState`.
    	//
    	// - Their user id. For example,
    	// `users/123456789/spaces/{space}/spaceReadState`.
    	//
    	// Format: users/{user}/spaces/{space}/spaceReadState
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for GetSpaceReadState API.

### func (*GetSpaceReadStateRequest) Descriptor 
    
    
    func (*GetSpaceReadStateRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSpaceReadStateRequest.ProtoReflect.Descriptor instead.

### func (*GetSpaceReadStateRequest) GetName 
    
    
    func (x *GetSpaceReadStateRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSpaceReadStateRequest) ProtoMessage 
    
    
    func (*GetSpaceReadStateRequest) ProtoMessage()

### func (*GetSpaceReadStateRequest) ProtoReflect 
    
    
    func (x *GetSpaceReadStateRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSpaceReadStateRequest) Reset 
    
    
    func (x *GetSpaceReadStateRequest) Reset()

### func (*GetSpaceReadStateRequest) String 
    
    
    func (x *GetSpaceReadStateRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSpaceRequest
    
    
    type GetSpaceRequest struct {
    
    	// Required. Resource name of the space, in the form `spaces/{space}`.
    	//
    	// Format: `spaces/{space}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.spaces` or `chat.admin.spaces.readonly` [OAuth 2.0
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

A request to return a single space.

### func (*GetSpaceRequest) Descriptor 
    
    
    func (*GetSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSpaceRequest.ProtoReflect.Descriptor instead.

### func (*GetSpaceRequest) GetName 
    
    
    func (x *GetSpaceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSpaceRequest) GetUseAdminAccess 
    
    
    func (x *GetSpaceRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*GetSpaceRequest) ProtoMessage 
    
    
    func (*GetSpaceRequest) ProtoMessage()

### func (*GetSpaceRequest) ProtoReflect 
    
    
    func (x *GetSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSpaceRequest) Reset 
    
    
    func (x *GetSpaceRequest) Reset()

### func (*GetSpaceRequest) String 
    
    
    func (x *GetSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetThreadReadStateRequest
    
    
    type GetThreadReadStateRequest struct {
    
    	// Required. Resource name of the thread read state to retrieve.
    	//
    	// Only supports getting read state for the calling user.
    	//
    	// To refer to the calling user, set one of the following:
    	//
    	// - The `me` alias. For example,
    	// `users/me/spaces/{space}/threads/{thread}/threadReadState`.
    	//
    	// - Their Workspace email address. For example,
    	// `users/user@example.com/spaces/{space}/threads/{thread}/threadReadState`.
    	//
    	// - Their user id. For example,
    	// `users/123456789/spaces/{space}/threads/{thread}/threadReadState`.
    	//
    	// Format: users/{user}/spaces/{space}/threads/{thread}/threadReadState
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for GetThreadReadStateRequest API.

### func (*GetThreadReadStateRequest) Descriptor 
    
    
    func (*GetThreadReadStateRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetThreadReadStateRequest.ProtoReflect.Descriptor instead.

### func (*GetThreadReadStateRequest) GetName 
    
    
    func (x *GetThreadReadStateRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetThreadReadStateRequest) ProtoMessage 
    
    
    func (*GetThreadReadStateRequest) ProtoMessage()

### func (*GetThreadReadStateRequest) ProtoReflect 
    
    
    func (x *GetThreadReadStateRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetThreadReadStateRequest) Reset 
    
    
    func (x *GetThreadReadStateRequest) Reset()

### func (*GetThreadReadStateRequest) String 
    
    
    func (x *GetThreadReadStateRequest) String() [string](https://pkg.go.dev/builtin#string)

## Group
    
    
    type Group struct {
    
    	// Resource name for a Google Group.
    	//
    	// Represents a
    	// [group](https://cloud.google.com/identity/docs/reference/rest/v1/groups) in
    	// Cloud Identity Groups API.
    	//
    	// Format: groups/{group}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A Google Group in Google Chat.

### func (*Group) Descriptor 
    
    
    func (*Group) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Group.ProtoReflect.Descriptor instead.

### func (*Group) GetName 
    
    
    func (x *Group) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Group) ProtoMessage 
    
    
    func (*Group) ProtoMessage()

### func (*Group) ProtoReflect 
    
    
    func (x *Group) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Group) Reset 
    
    
    func (x *Group) Reset()

### func (*Group) String 
    
    
    func (x *Group) String() [string](https://pkg.go.dev/builtin#string)

## HistoryState
    
    
    type HistoryState [int32](https://pkg.go.dev/builtin#int32)

The history state for messages and spaces. Specifies how long messages and conversation threads are kept after creation.

### HistoryState_HISTORY_STATE_UNSPECIFIED, HistoryState_HISTORY_OFF, HistoryState_HISTORY_ON
    
    
    const (
    	// Default value. Do not use.
    	HistoryState_HISTORY_STATE_UNSPECIFIED HistoryState = 0
    	// History off. [Messages and threads are kept for 24
    	// hours](https://support.google.com/chat/answer/7664687).
    	HistoryState_HISTORY_OFF HistoryState = 1
    	// History on. The organization's [Vault retention
    	// rules](https://support.google.com/vault/answer/7657597) specify for
    	// how long messages and threads are kept.
    	HistoryState_HISTORY_ON HistoryState = 2
    )

### func (HistoryState) Descriptor 
    
    
    func (HistoryState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (HistoryState) Enum 
    
    
    func (x HistoryState) Enum() *HistoryState

### func (HistoryState) EnumDescriptor 
    
    
    func (HistoryState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HistoryState.Descriptor instead.

### func (HistoryState) Number 
    
    
    func (x HistoryState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (HistoryState) String 
    
    
    func (x HistoryState) String() [string](https://pkg.go.dev/builtin#string)

### func (HistoryState) Type 
    
    
    func (HistoryState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListCustomEmojisRequest
    
    
    type ListCustomEmojisRequest struct {
    
    	// Optional. The maximum number of custom emojis returned. The service can
    	// return fewer custom emojis than this value. If unspecified, the default
    	// value is 25. The maximum value is 200; values above 200 are changed to 200.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. (If resuming from a previous query.)
    	//
    	// A page token received from a previous list custom emoji call. Provide this
    	// to retrieve the subsequent page.
    	//
    	// When paginating, the filter value should match the call that provided the
    	// page token. Passing a different value might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// Supports filtering by creator.
    	//
    	// To filter by creator, you must specify a valid value. Currently only
    	// `creator("users/me")` and `NOT creator("users/me")` are accepted to filter
    	// custom emojis by whether they were created by the calling user or not.
    	//
    	// For example, the following query returns custom emojis created by the
    	// caller:
    	// ```
    	// creator("users/me")
    	// ```
    	//
    	// Invalid queries are rejected with an `INVALID_ARGUMENT` error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

A request to return a list of custom emojis.

### func (*ListCustomEmojisRequest) Descriptor 
    
    
    func (*ListCustomEmojisRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCustomEmojisRequest.ProtoReflect.Descriptor instead.

### func (*ListCustomEmojisRequest) GetFilter 
    
    
    func (x *ListCustomEmojisRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListCustomEmojisRequest) GetPageSize 
    
    
    func (x *ListCustomEmojisRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListCustomEmojisRequest) GetPageToken 
    
    
    func (x *ListCustomEmojisRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCustomEmojisRequest) ProtoMessage 
    
    
    func (*ListCustomEmojisRequest) ProtoMessage()

### func (*ListCustomEmojisRequest) ProtoReflect 
    
    
    func (x *ListCustomEmojisRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCustomEmojisRequest) Reset 
    
    
    func (x *ListCustomEmojisRequest) Reset()

### func (*ListCustomEmojisRequest) String 
    
    
    func (x *ListCustomEmojisRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCustomEmojisResponse
    
    
    type ListCustomEmojisResponse struct {
    
    	// Unordered list. List of custom emojis.
    	CustomEmojis []*CustomEmoji `protobuf:"bytes,1,rep,name=custom_emojis,json=customEmojis,proto3" json:"custom_emojis,omitempty"`
    	// A token that you can send as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

A response to list custom emojis.

### func (*ListCustomEmojisResponse) Descriptor 
    
    
    func (*ListCustomEmojisResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCustomEmojisResponse.ProtoReflect.Descriptor instead.

### func (*ListCustomEmojisResponse) GetCustomEmojis 
    
    
    func (x *ListCustomEmojisResponse) GetCustomEmojis() []*CustomEmoji

### func (*ListCustomEmojisResponse) GetNextPageToken 
    
    
    func (x *ListCustomEmojisResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCustomEmojisResponse) ProtoMessage 
    
    
    func (*ListCustomEmojisResponse) ProtoMessage()

### func (*ListCustomEmojisResponse) ProtoReflect 
    
    
    func (x *ListCustomEmojisResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCustomEmojisResponse) Reset 
    
    
    func (x *ListCustomEmojisResponse) Reset()

### func (*ListCustomEmojisResponse) String 
    
    
    func (x *ListCustomEmojisResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListMembershipsRequest
    
    
    type ListMembershipsRequest struct {
    
    	// Required. The resource name of the space for which to fetch a membership
    	// list.
    	//
    	// Format: spaces/{space}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of memberships to return. The service might
    	// return fewer than this value.
    	//
    	// If unspecified, at most 100 memberships are returned.
    	//
    	// The maximum value is 1000. If you use a value more than 1000, it's
    	// automatically changed to 1000.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous call to list memberships.
    	// Provide this parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// You can filter memberships by a member's role
    	// ([`role`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.members#membershiprole))
    	// and type
    	// ([`member.type`](https://developers.google.com/workspace/chat/api/reference/rest/v1/User#type)).
    	//
    	// To filter by role, set `role` to `ROLE_MEMBER` or `ROLE_MANAGER`.
    	//
    	// To filter by type, set `member.type` to `HUMAN` or `BOT`. You can also
    	// filter for `member.type` using the `!=` operator.
    	//
    	// To filter by both role and type, use the `AND` operator. To filter by
    	// either role or type, use the `OR` operator.
    	//
    	// Either `member.type = "HUMAN"` or `member.type != "BOT"` is required
    	// when `use_admin_access` is set to true. Other member type filters will be
    	// rejected.
    	//
    	// For example, the following queries are valid:
    	//
    	// ```
    	// role = "ROLE_MANAGER" OR role = "ROLE_MEMBER"
    	// member.type = "HUMAN" AND role = "ROLE_MANAGER"
    	//
    	// member.type != "BOT"
    	// ```
    	//
    	// The following queries are invalid:
    	//
    	// ```
    	// member.type = "HUMAN" AND member.type = "BOT"
    	// role = "ROLE_MANAGER" AND role = "ROLE_MEMBER"
    	// ```
    	//
    	// Invalid queries are rejected by the server with an `INVALID_ARGUMENT`
    	// error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. When `true`, also returns memberships associated with a
    	// [Google Group][google.chat.v1.Membership.group_member], in
    	// addition to other types of memberships. If a
    	// [filter][google.chat.v1.ListMembershipsRequest.filter] is set,
    	// [Google Group][google.chat.v1.Membership.group_member]
    	// memberships that don't match the filter criteria aren't returned.
    	ShowGroups [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=show_groups,json=showGroups,proto3" json:"show_groups,omitempty"`
    	// Optional. When `true`, also returns memberships associated with
    	// [invited][google.chat.v1.Membership.MembershipState.INVITED] members, in
    	// addition to other types of memberships. If a
    	// filter is set,
    	// [invited][google.chat.v1.Membership.MembershipState.INVITED] memberships
    	// that don't match the filter criteria aren't returned.
    	//
    	// Currently requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	ShowInvited [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=show_invited,json=showInvited,proto3" json:"show_invited,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires either the `chat.admin.memberships.readonly` or
    	// `chat.admin.memberships` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	//
    	// Listing app memberships in a space isn't supported when using admin access.
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,8,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for listing memberships.

### func (*ListMembershipsRequest) Descriptor 
    
    
    func (*ListMembershipsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMembershipsRequest.ProtoReflect.Descriptor instead.

### func (*ListMembershipsRequest) GetFilter 
    
    
    func (x *ListMembershipsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListMembershipsRequest) GetPageSize 
    
    
    func (x *ListMembershipsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListMembershipsRequest) GetPageToken 
    
    
    func (x *ListMembershipsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMembershipsRequest) GetParent 
    
    
    func (x *ListMembershipsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListMembershipsRequest) GetShowGroups 
    
    
    func (x *ListMembershipsRequest) GetShowGroups() [bool](https://pkg.go.dev/builtin#bool)

### func (*ListMembershipsRequest) GetShowInvited 
    
    
    func (x *ListMembershipsRequest) GetShowInvited() [bool](https://pkg.go.dev/builtin#bool)

### func (*ListMembershipsRequest) GetUseAdminAccess 
    
    
    func (x *ListMembershipsRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*ListMembershipsRequest) ProtoMessage 
    
    
    func (*ListMembershipsRequest) ProtoMessage()

### func (*ListMembershipsRequest) ProtoReflect 
    
    
    func (x *ListMembershipsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMembershipsRequest) Reset 
    
    
    func (x *ListMembershipsRequest) Reset()

### func (*ListMembershipsRequest) String 
    
    
    func (x *ListMembershipsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMembershipsResponse
    
    
    type ListMembershipsResponse struct {
    
    	// Unordered list. List of memberships in the requested (or first) page.
    	Memberships []*Membership `protobuf:"bytes,1,rep,name=memberships,proto3" json:"memberships,omitempty"`
    	// A token that you can send as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to list memberships of the space.

### func (*ListMembershipsResponse) Descriptor 
    
    
    func (*ListMembershipsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMembershipsResponse.ProtoReflect.Descriptor instead.

### func (*ListMembershipsResponse) GetMemberships 
    
    
    func (x *ListMembershipsResponse) GetMemberships() []*Membership

### func (*ListMembershipsResponse) GetNextPageToken 
    
    
    func (x *ListMembershipsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMembershipsResponse) ProtoMessage 
    
    
    func (*ListMembershipsResponse) ProtoMessage()

### func (*ListMembershipsResponse) ProtoReflect 
    
    
    func (x *ListMembershipsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMembershipsResponse) Reset 
    
    
    func (x *ListMembershipsResponse) Reset()

### func (*ListMembershipsResponse) String 
    
    
    func (x *ListMembershipsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListMessagePinsRequest
    
    
    type ListMessagePinsRequest struct {
    
    	// Required. The parent space which owns the collection of pinned items
    	// Format: `spaces/{space}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of message pins returned. The service might
    	// return fewer messages than this value. The maximum value is 100. If you use
    	// a value more than 100, it's automatically changed to 100. If unspecified,
    	// at most 100 message pins will be returned. Negative values return an
    	// `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token received from a previous list message pins call.
    	// Provide this parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for listing message pins.

### func (*ListMessagePinsRequest) Descriptor 
    
    
    func (*ListMessagePinsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMessagePinsRequest.ProtoReflect.Descriptor instead.

### func (*ListMessagePinsRequest) GetPageSize 
    
    
    func (x *ListMessagePinsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListMessagePinsRequest) GetPageToken 
    
    
    func (x *ListMessagePinsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagePinsRequest) GetParent 
    
    
    func (x *ListMessagePinsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagePinsRequest) ProtoMessage 
    
    
    func (*ListMessagePinsRequest) ProtoMessage()

### func (*ListMessagePinsRequest) ProtoReflect 
    
    
    func (x *ListMessagePinsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMessagePinsRequest) Reset 
    
    
    func (x *ListMessagePinsRequest) Reset()

### func (*ListMessagePinsRequest) String 
    
    
    func (x *ListMessagePinsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMessagePinsResponse
    
    
    type ListMessagePinsResponse struct {
    
    	// The pinned messages from the specified space.
    	MessagePins []*MessagePin `protobuf:"bytes,1,rep,name=message_pins,json=messagePins,proto3" json:"message_pins,omitempty"`
    	// You can send a token as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing message pins.

### func (*ListMessagePinsResponse) Descriptor 
    
    
    func (*ListMessagePinsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMessagePinsResponse.ProtoReflect.Descriptor instead.

### func (*ListMessagePinsResponse) GetMessagePins 
    
    
    func (x *ListMessagePinsResponse) GetMessagePins() []*MessagePin

### func (*ListMessagePinsResponse) GetNextPageToken 
    
    
    func (x *ListMessagePinsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagePinsResponse) ProtoMessage 
    
    
    func (*ListMessagePinsResponse) ProtoMessage()

### func (*ListMessagePinsResponse) ProtoReflect 
    
    
    func (x *ListMessagePinsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMessagePinsResponse) Reset 
    
    
    func (x *ListMessagePinsResponse) Reset()

### func (*ListMessagePinsResponse) String 
    
    
    func (x *ListMessagePinsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListMessagesRequest
    
    
    type ListMessagesRequest struct {
    
    	// Required. The resource name of the space to list messages from.
    	//
    	// Format: `spaces/{space}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of messages returned. The service might return
    	// fewer messages than this value.
    	//
    	// If unspecified, at most 25 are returned.
    	//
    	// The maximum value is 1000. If you use a value more than 1000, it's
    	// automatically changed to 1000.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token received from a previous list messages call. Provide
    	// this parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// You can filter messages by date (`create_time`) and thread (`thread.name`).
    	//
    	// To filter messages by the date they were created, specify the `create_time`
    	// with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339)
    	// format and double quotation marks. For example,
    	// `"2023-04-21T11:30:00-04:00"`. You can use the greater than operator `>` to
    	// list messages that were created after a timestamp, or the less than
    	// operator `<` to="" list="" messages="" that="" were="" created="" before="" a="" timestamp.="" to="" filter="" messages="" within="" a="" time="" interval,="" use="" the="" `and`="" operator="" between="" two="" timestamps.="" to="" filter="" by="" thread,="" specify="" the="" `thread.name`,="" formatted="" as="" `spaces/{space}/threads/{thread}`.="" you="" can="" only="" specify="" one="" `thread.name`="" per="" query.="" to="" filter="" by="" both="" thread="" and="" date,="" use="" the="" `and`="" operator="" in="" your="" query.="" for="" example,="" the="" following="" queries="" are="" valid:="" ```="" create_time=""> "2012-04-21T11:30:00-04:00"
    	//
    	// create_time > "2012-04-21T11:30:00-04:00" AND
    	//
    	//	thread.name = spaces/AAAAAAAAAAA/threads/123
    	//
    	// create_time > "2012-04-21T11:30:00+00:00" AND
    	//
    	// create_time < "2013-01-01t00:00:00+00:00"="" and="" thread.name="spaces/AAAAAAAAAAA/threads/123" thread.name="spaces/AAAAAAAAAAA/threads/123" ```="" invalid="" queries="" are="" rejected="" by="" the="" server="" with="" an="" `invalid_argument`="" error.="" filter="">[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. How the list of messages is ordered. Specify a value to order by
    	// an ordering operation. Valid ordering operation values are as follows:
    	//
    	// - `ASC` for ascending.
    	//
    	// - `DESC` for descending.
    	//
    	// The default ordering is `create_time ASC`.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// Optional. Whether to include deleted messages. Deleted messages include
    	// deleted time and metadata about their deletion, but message content is
    	// unavailable.
    	ShowDeleted [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=show_deleted,json=showDeleted,proto3" json:"show_deleted,omitempty"`
    	// Optional. Specifies the desired output syntax for the Chat message
    	// `formatted_text` field.
    	MarkupSyntax MarkupSyntax `protobuf:"varint,9,opt,name=markup_syntax,json=markupSyntax,proto3,enum=google.chat.v1.MarkupSyntax" json:"markup_syntax,omitempty"`
    	// contains filtered or unexported fields
    }

Lists messages in the specified space, that the user is a member of.

### func (*ListMessagesRequest) Descriptor 
    
    
    func (*ListMessagesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMessagesRequest.ProtoReflect.Descriptor instead.

### func (*ListMessagesRequest) GetFilter 
    
    
    func (x *ListMessagesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagesRequest) GetMarkupSyntax 
    
    
    func (x *ListMessagesRequest) GetMarkupSyntax() MarkupSyntax

### func (*ListMessagesRequest) GetOrderBy 
    
    
    func (x *ListMessagesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagesRequest) GetPageSize 
    
    
    func (x *ListMessagesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListMessagesRequest) GetPageToken 
    
    
    func (x *ListMessagesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagesRequest) GetParent 
    
    
    func (x *ListMessagesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagesRequest) GetShowDeleted 
    
    
    func (x *ListMessagesRequest) GetShowDeleted() [bool](https://pkg.go.dev/builtin#bool)

### func (*ListMessagesRequest) ProtoMessage 
    
    
    func (*ListMessagesRequest) ProtoMessage()

### func (*ListMessagesRequest) ProtoReflect 
    
    
    func (x *ListMessagesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMessagesRequest) Reset 
    
    
    func (x *ListMessagesRequest) Reset()

### func (*ListMessagesRequest) String 
    
    
    func (x *ListMessagesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMessagesResponse
    
    
    type ListMessagesResponse struct {
    
    	// List of messages.
    	Messages []*Message `protobuf:"bytes,1,rep,name=messages,proto3" json:"messages,omitempty"`
    	// You can send a token as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing messages.

### func (*ListMessagesResponse) Descriptor 
    
    
    func (*ListMessagesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMessagesResponse.ProtoReflect.Descriptor instead.

### func (*ListMessagesResponse) GetMessages 
    
    
    func (x *ListMessagesResponse) GetMessages() []*Message

### func (*ListMessagesResponse) GetNextPageToken 
    
    
    func (x *ListMessagesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMessagesResponse) ProtoMessage 
    
    
    func (*ListMessagesResponse) ProtoMessage()

### func (*ListMessagesResponse) ProtoReflect 
    
    
    func (x *ListMessagesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMessagesResponse) Reset 
    
    
    func (x *ListMessagesResponse) Reset()

### func (*ListMessagesResponse) String 
    
    
    func (x *ListMessagesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReactionsRequest
    
    
    type ListReactionsRequest struct {
    
    	// Required. The message users reacted to.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of reactions returned. The service can return
    	// fewer reactions than this value. If unspecified, the default value is 25.
    	// The maximum value is 200; values above 200 are changed to 200.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. (If resuming from a previous query.)
    	//
    	// A page token received from a previous list reactions call. Provide this
    	// to retrieve the subsequent page.
    	//
    	// When paginating, the filter value should match the call that provided the
    	// page token. Passing a different value might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// You can filter reactions by
    	// [emoji](https://developers.google.com/workspace/chat/api/reference/rest/v1/Emoji)
    	// (either `emoji.unicode` or `emoji.custom_emoji.uid`) and
    	// [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User)
    	// (`user.name`).
    	//
    	// To filter reactions for multiple emojis or users, join similar fields
    	// with the `OR` operator, such as `emoji.unicode = "🙂" OR emoji.unicode =
    	// "👍"` and `user.name = "users/AAAAAA" OR user.name = "users/BBBBBB"`.
    	//
    	// To filter reactions by emoji and user, use the `AND` operator, such as
    	// `emoji.unicode = "🙂" AND user.name = "users/AAAAAA"`.
    	//
    	// If your query uses both `AND` and `OR`, group them with parentheses.
    	//
    	// For example, the following queries are valid:
    	//
    	// ```
    	// user.name = "users/{user}"
    	// emoji.unicode = "🙂"
    	// emoji.custom_emoji.uid = "{uid}"
    	// emoji.unicode = "🙂" OR emoji.unicode = "👍"
    	// emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}"
    	// emoji.unicode = "🙂" AND user.name = "users/{user}"
    	// (emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}")
    	// AND user.name = "users/{user}"
    	// ```
    	//
    	// The following queries are invalid:
    	//
    	// ```
    	// emoji.unicode = "🙂" AND emoji.unicode = "👍"
    	// emoji.unicode = "🙂" AND emoji.custom_emoji.uid = "{uid}"
    	// emoji.unicode = "🙂" OR user.name = "users/{user}"
    	// emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}" OR
    	// user.name = "users/{user}"
    	// emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}"
    	// AND user.name = "users/{user}"
    	// ```
    	//
    	// Invalid queries are rejected with an `INVALID_ARGUMENT` error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Lists reactions to a message.

### func (*ListReactionsRequest) Descriptor 
    
    
    func (*ListReactionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReactionsRequest.ProtoReflect.Descriptor instead.

### func (*ListReactionsRequest) GetFilter 
    
    
    func (x *ListReactionsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReactionsRequest) GetPageSize 
    
    
    func (x *ListReactionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReactionsRequest) GetPageToken 
    
    
    func (x *ListReactionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReactionsRequest) GetParent 
    
    
    func (x *ListReactionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReactionsRequest) ProtoMessage 
    
    
    func (*ListReactionsRequest) ProtoMessage()

### func (*ListReactionsRequest) ProtoReflect 
    
    
    func (x *ListReactionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReactionsRequest) Reset 
    
    
    func (x *ListReactionsRequest) Reset()

### func (*ListReactionsRequest) String 
    
    
    func (x *ListReactionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReactionsResponse
    
    
    type ListReactionsResponse struct {
    
    	// List of reactions in the requested (or first) page.
    	Reactions []*Reaction `protobuf:"bytes,1,rep,name=reactions,proto3" json:"reactions,omitempty"`
    	// Continuation token to retrieve the next page of results. It's empty
    	// for the last page of results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to a list reactions request.

### func (*ListReactionsResponse) Descriptor 
    
    
    func (*ListReactionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReactionsResponse.ProtoReflect.Descriptor instead.

### func (*ListReactionsResponse) GetNextPageToken 
    
    
    func (x *ListReactionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReactionsResponse) GetReactions 
    
    
    func (x *ListReactionsResponse) GetReactions() []*Reaction

### func (*ListReactionsResponse) ProtoMessage 
    
    
    func (*ListReactionsResponse) ProtoMessage()

### func (*ListReactionsResponse) ProtoReflect 
    
    
    func (x *ListReactionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReactionsResponse) Reset 
    
    
    func (x *ListReactionsResponse) Reset()

### func (*ListReactionsResponse) String 
    
    
    func (x *ListReactionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSectionItemsRequest
    
    
    type ListSectionItemsRequest struct {
    
    	// Required. The parent, which is the section resource name that owns this
    	// collection of section items. Only supports listing section items for the
    	// calling user.
    	//
    	// When you're filtering by space, use the wildcard `-` to search across all
    	// sections. For example, `users/{user}/sections/-`.
    	//
    	// Format: `users/{user}/sections/{section}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of section items to return. The service may
    	// return fewer than this value.
    	//
    	// If unspecified, at most 10 section items will be returned.
    	//
    	// The maximum value is 100. If you use a value more than 100, it's
    	// automatically changed to 100.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous list section items call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// Currently only supports filtering by space.
    	//
    	// For example, `space = spaces/{space}`.
    	//
    	// Invalid queries are rejected with an `INVALID_ARGUMENT` error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for listing section items.

### func (*ListSectionItemsRequest) Descriptor 
    
    
    func (*ListSectionItemsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSectionItemsRequest.ProtoReflect.Descriptor instead.

### func (*ListSectionItemsRequest) GetFilter 
    
    
    func (x *ListSectionItemsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionItemsRequest) GetPageSize 
    
    
    func (x *ListSectionItemsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSectionItemsRequest) GetPageToken 
    
    
    func (x *ListSectionItemsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionItemsRequest) GetParent 
    
    
    func (x *ListSectionItemsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionItemsRequest) ProtoMessage 
    
    
    func (*ListSectionItemsRequest) ProtoMessage()

### func (*ListSectionItemsRequest) ProtoReflect 
    
    
    func (x *ListSectionItemsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSectionItemsRequest) Reset 
    
    
    func (x *ListSectionItemsRequest) Reset()

### func (*ListSectionItemsRequest) String 
    
    
    func (x *ListSectionItemsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSectionItemsResponse
    
    
    type ListSectionItemsResponse struct {
    
    	// The section items from the specified section.
    	SectionItems []*SectionItem `protobuf:"bytes,1,rep,name=section_items,json=sectionItems,proto3" json:"section_items,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page. If
    	// this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing section items.

### func (*ListSectionItemsResponse) Descriptor 
    
    
    func (*ListSectionItemsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSectionItemsResponse.ProtoReflect.Descriptor instead.

### func (*ListSectionItemsResponse) GetNextPageToken 
    
    
    func (x *ListSectionItemsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionItemsResponse) GetSectionItems 
    
    
    func (x *ListSectionItemsResponse) GetSectionItems() []*SectionItem

### func (*ListSectionItemsResponse) ProtoMessage 
    
    
    func (*ListSectionItemsResponse) ProtoMessage()

### func (*ListSectionItemsResponse) ProtoReflect 
    
    
    func (x *ListSectionItemsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSectionItemsResponse) Reset 
    
    
    func (x *ListSectionItemsResponse) Reset()

### func (*ListSectionItemsResponse) String 
    
    
    func (x *ListSectionItemsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSectionsRequest
    
    
    type ListSectionsRequest struct {
    
    	// Required. The parent, which is the user resource name that owns this
    	// collection of sections. Only supports listing sections for the calling
    	// user. To refer to the calling user, set one of the following:
    	//
    	// - The `me` alias. For example, `users/me`.
    	//
    	// - Their Workspace email address. For example, `users/user@example.com`.
    	//
    	// - Their user id. For example, `users/123456789`.
    	//
    	// Format: `users/{user}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of sections to return. The service may return
    	// fewer than this value.
    	//
    	// If unspecified, at most 10 sections will be returned.
    	//
    	// The maximum value is 100. If you use a value more than 100, it's
    	// automatically changed to 100.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous list sections call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for listing sections.

### func (*ListSectionsRequest) Descriptor 
    
    
    func (*ListSectionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSectionsRequest.ProtoReflect.Descriptor instead.

### func (*ListSectionsRequest) GetPageSize 
    
    
    func (x *ListSectionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSectionsRequest) GetPageToken 
    
    
    func (x *ListSectionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionsRequest) GetParent 
    
    
    func (x *ListSectionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionsRequest) ProtoMessage 
    
    
    func (*ListSectionsRequest) ProtoMessage()

### func (*ListSectionsRequest) ProtoReflect 
    
    
    func (x *ListSectionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSectionsRequest) Reset 
    
    
    func (x *ListSectionsRequest) Reset()

### func (*ListSectionsRequest) String 
    
    
    func (x *ListSectionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSectionsResponse
    
    
    type ListSectionsResponse struct {
    
    	// The sections from the specified user.
    	Sections []*Section `protobuf:"bytes,1,rep,name=sections,proto3" json:"sections,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing sections.

### func (*ListSectionsResponse) Descriptor 
    
    
    func (*ListSectionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSectionsResponse.ProtoReflect.Descriptor instead.

### func (*ListSectionsResponse) GetNextPageToken 
    
    
    func (x *ListSectionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSectionsResponse) GetSections 
    
    
    func (x *ListSectionsResponse) GetSections() []*Section

### func (*ListSectionsResponse) ProtoMessage 
    
    
    func (*ListSectionsResponse) ProtoMessage()

### func (*ListSectionsResponse) ProtoReflect 
    
    
    func (x *ListSectionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSectionsResponse) Reset 
    
    
    func (x *ListSectionsResponse) Reset()

### func (*ListSectionsResponse) String 
    
    
    func (x *ListSectionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSpaceEventsRequest
    
    
    type ListSpaceEventsRequest struct {
    
    	// Required. Resource name of the [Google Chat
    	// space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces)
    	// where the events occurred.
    	//
    	// Format: `spaces/{space}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of space events returned. The service might
    	// return fewer than this value.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous list space events call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to list space events must
    	// match the call that provided the page token. Passing different values to
    	// the other parameters might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Required. A query filter.
    	//
    	// You must specify at least one event type (`event_type`)
    	// using the has `:` operator. To filter by multiple event types, use the `OR`
    	// operator. Omit batch event types in your filter. The request automatically
    	// returns any related batch events. For example, if you filter by new
    	// reactions
    	// (`google.workspace.chat.reaction.v1.created`), the server also returns
    	// batch new reactions events
    	// (`google.workspace.chat.reaction.v1.batchCreated`). For a list of supported
    	// event types, see the [`SpaceEvents` reference
    	// documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.event_type).
    	//
    	// Optionally, you can also filter by start time (`start_time`) and
    	// end time (`end_time`):
    	//
    	// * `start_time`: Exclusive timestamp from which to start listing space
    	// events.
    	//
    	//	You can list events that occurred up to 28 days ago. If unspecified, lists
    	//	space events from the past 28 days.
    	//   - `end_time`: Inclusive timestamp until which space events are listed.
    	//     If unspecified, lists events up to the time of the request.
    	//
    	// To specify a start or end time, use the equals `=` operator and format in
    	// [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339). To filter by both
    	// `start_time` and `end_time`, use the `AND` operator.
    	//
    	// For example, the following queries are valid:
    	//
    	// ```
    	// start_time="2023-08-23T19:20:33+00:00" AND
    	// end_time="2023-08-23T19:21:54+00:00"
    	// ```
    	// ```
    	// start_time="2023-08-23T19:20:33+00:00" AND
    	// (event_types:"google.workspace.chat.space.v1.updated" OR
    	// event_types:"google.workspace.chat.message.v1.created")
    	// ```
    	//
    	// The following queries are invalid:
    	//
    	// ```
    	// start_time="2023-08-23T19:20:33+00:00" OR
    	// end_time="2023-08-23T19:21:54+00:00"
    	// ```
    	// ```
    	// event_types:"google.workspace.chat.space.v1.updated" AND
    	// event_types:"google.workspace.chat.message.v1.created"
    	// ```
    	//
    	// Invalid queries are rejected by the server with an `INVALID_ARGUMENT`
    	// error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for listing space events.

### func (*ListSpaceEventsRequest) Descriptor 
    
    
    func (*ListSpaceEventsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSpaceEventsRequest.ProtoReflect.Descriptor instead.

### func (*ListSpaceEventsRequest) GetFilter 
    
    
    func (x *ListSpaceEventsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpaceEventsRequest) GetPageSize 
    
    
    func (x *ListSpaceEventsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSpaceEventsRequest) GetPageToken 
    
    
    func (x *ListSpaceEventsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpaceEventsRequest) GetParent 
    
    
    func (x *ListSpaceEventsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpaceEventsRequest) ProtoMessage 
    
    
    func (*ListSpaceEventsRequest) ProtoMessage()

### func (*ListSpaceEventsRequest) ProtoReflect 
    
    
    func (x *ListSpaceEventsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSpaceEventsRequest) Reset 
    
    
    func (x *ListSpaceEventsRequest) Reset()

### func (*ListSpaceEventsRequest) String 
    
    
    func (x *ListSpaceEventsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSpaceEventsResponse
    
    
    type ListSpaceEventsResponse struct {
    
    	// Results are returned in chronological order (oldest event first).
    	// Note: The `permissionSettings` field is not returned in the Space
    	// object for list requests.
    	SpaceEvents []*SpaceEvent `protobuf:"bytes,1,rep,name=space_events,json=spaceEvents,proto3" json:"space_events,omitempty"`
    	// Continuation token used to fetch more events.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing space events.

### func (*ListSpaceEventsResponse) Descriptor 
    
    
    func (*ListSpaceEventsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSpaceEventsResponse.ProtoReflect.Descriptor instead.

### func (*ListSpaceEventsResponse) GetNextPageToken 
    
    
    func (x *ListSpaceEventsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpaceEventsResponse) GetSpaceEvents 
    
    
    func (x *ListSpaceEventsResponse) GetSpaceEvents() []*SpaceEvent

### func (*ListSpaceEventsResponse) ProtoMessage 
    
    
    func (*ListSpaceEventsResponse) ProtoMessage()

### func (*ListSpaceEventsResponse) ProtoReflect 
    
    
    func (x *ListSpaceEventsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSpaceEventsResponse) Reset 
    
    
    func (x *ListSpaceEventsResponse) Reset()

### func (*ListSpaceEventsResponse) String 
    
    
    func (x *ListSpaceEventsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSpacesRequest
    
    
    type ListSpacesRequest struct {
    
    	// Optional. The maximum number of spaces to return. The service might return
    	// fewer than this value.
    	//
    	// If unspecified, at most 100 spaces are returned.
    	//
    	// The maximum value is 1000. If you use a value more than 1000, it's
    	// automatically changed to 1000.
    	//
    	// Negative values return an `INVALID_ARGUMENT` error.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A page token, received from a previous list spaces call.
    	// Provide this parameter to retrieve the subsequent page.
    	//
    	// When paginating, the filter value should match the call that provided the
    	// page token. Passing a different value may lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A query filter.
    	//
    	// You can filter spaces by the space type
    	// ([`space_type`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#spacetype)).
    	//
    	// To filter by space type, you must specify valid enum value, such as
    	// `SPACE` or `GROUP_CHAT` (the `space_type` can't be
    	// `SPACE_TYPE_UNSPECIFIED`). To query for multiple space types, use the `OR`
    	// operator.
    	//
    	// For example, the following queries are valid:
    	//
    	// ```
    	// space_type = "SPACE"
    	// spaceType = "GROUP_CHAT" OR spaceType = "DIRECT_MESSAGE"
    	// ```
    	//
    	// Invalid queries are rejected by the server with an `INVALID_ARGUMENT`
    	// error.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

A request to list the spaces the caller is a member of.

### func (*ListSpacesRequest) Descriptor 
    
    
    func (*ListSpacesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSpacesRequest.ProtoReflect.Descriptor instead.

### func (*ListSpacesRequest) GetFilter 
    
    
    func (x *ListSpacesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpacesRequest) GetPageSize 
    
    
    func (x *ListSpacesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSpacesRequest) GetPageToken 
    
    
    func (x *ListSpacesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpacesRequest) ProtoMessage 
    
    
    func (*ListSpacesRequest) ProtoMessage()

### func (*ListSpacesRequest) ProtoReflect 
    
    
    func (x *ListSpacesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSpacesRequest) Reset 
    
    
    func (x *ListSpacesRequest) Reset()

### func (*ListSpacesRequest) String 
    
    
    func (x *ListSpacesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSpacesResponse
    
    
    type ListSpacesResponse struct {
    
    	// List of spaces in the requested (or first) page.
    	// Note: The `permissionSettings` field is not returned in the Space
    	// object for list requests.
    	Spaces []*Space `protobuf:"bytes,1,rep,name=spaces,proto3" json:"spaces,omitempty"`
    	// You can send a token as `pageToken` to retrieve the next page of
    	// results. If empty, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response for a list spaces request.

### func (*ListSpacesResponse) Descriptor 
    
    
    func (*ListSpacesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSpacesResponse.ProtoReflect.Descriptor instead.

### func (*ListSpacesResponse) GetNextPageToken 
    
    
    func (x *ListSpacesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSpacesResponse) GetSpaces 
    
    
    func (x *ListSpacesResponse) GetSpaces() []*Space

### func (*ListSpacesResponse) ProtoMessage 
    
    
    func (*ListSpacesResponse) ProtoMessage()

### func (*ListSpacesResponse) ProtoReflect 
    
    
    func (x *ListSpacesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSpacesResponse) Reset 
    
    
    func (x *ListSpacesResponse) Reset()

### func (*ListSpacesResponse) String 
    
    
    func (x *ListSpacesResponse) String() [string](https://pkg.go.dev/builtin#string)

## MarkAsActiveRequest
    
    
    type MarkAsActiveRequest struct {
    
    	// Required. The resource name of the availability to mark as active.
    	// Format: users/{user}/availability
    	//
    	// `{user}` is the id for the Person in the People API or Admin SDK directory
    	// API. For example, `users/123456789`.
    	//
    	// The user's email address or `me` can also be used as an alias to refer to
    	// the caller.  For example, `users/user@example.com` or `users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The expiration for the ACTIVE availability state. The user will
    	// be marked as Away after expiration. If no expiration is provided, the
    	// ACTIVE state will expire 30 minutes from the current time.
    	//
    	// Types that are valid to be assigned to Expiration:
    	//
    	//	*MarkAsActiveRequest_ExpireTime
    	//	*MarkAsActiveRequest_Ttl
    	Expiration isMarkAsActiveRequest_Expiration `protobuf_oneof:"expiration"`
    	// contains filtered or unexported fields
    }

Request message for the `MarkAsActive` method.

### func (*MarkAsActiveRequest) Descriptor 
    
    
    func (*MarkAsActiveRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkAsActiveRequest.ProtoReflect.Descriptor instead.

### func (*MarkAsActiveRequest) GetExpiration 
    
    
    func (x *MarkAsActiveRequest) GetExpiration() isMarkAsActiveRequest_Expiration

### func (*MarkAsActiveRequest) GetExpireTime 
    
    
    func (x *MarkAsActiveRequest) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*MarkAsActiveRequest) GetName 
    
    
    func (x *MarkAsActiveRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkAsActiveRequest) GetTtl 
    
    
    func (x *MarkAsActiveRequest) GetTtl() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*MarkAsActiveRequest) ProtoMessage 
    
    
    func (*MarkAsActiveRequest) ProtoMessage()

### func (*MarkAsActiveRequest) ProtoReflect 
    
    
    func (x *MarkAsActiveRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkAsActiveRequest) Reset 
    
    
    func (x *MarkAsActiveRequest) Reset()

### func (*MarkAsActiveRequest) String 
    
    
    func (x *MarkAsActiveRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkAsActiveRequest_ExpireTime
    
    
    type MarkAsActiveRequest_ExpireTime struct {
    	// The absolute timestamp when the ACTIVE state expires.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=expire_time,json=expireTime,proto3,oneof"`
    }

## MarkAsActiveRequest_Ttl
    
    
    type MarkAsActiveRequest_Ttl struct {
    	// The duration from the current time until the ACTIVE state expires.
    	// Using a short TTL can effectively reset the user's state to be based
    	// on activity after this brief duration.
    	Ttl *durationpb.Duration `protobuf:"bytes,3,opt,name=ttl,proto3,oneof"`
    }

## MarkAsAwayRequest
    
    
    type MarkAsAwayRequest struct {
    
    	// Required. The resource name of the availability to mark as away.
    	// Format: users/{user}/availability
    	//
    	// `{user}` is the id for the Person in the People API or Admin SDK directory
    	// API. For example, `users/123456789`.
    	//
    	// The user's email address or `me` can also be used as an alias to refer to
    	// the caller.  For example, `users/user@example.com` or `users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `MarkAsAway` method.

### func (*MarkAsAwayRequest) Descriptor 
    
    
    func (*MarkAsAwayRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkAsAwayRequest.ProtoReflect.Descriptor instead.

### func (*MarkAsAwayRequest) GetName 
    
    
    func (x *MarkAsAwayRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkAsAwayRequest) ProtoMessage 
    
    
    func (*MarkAsAwayRequest) ProtoMessage()

### func (*MarkAsAwayRequest) ProtoReflect 
    
    
    func (x *MarkAsAwayRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkAsAwayRequest) Reset 
    
    
    func (x *MarkAsAwayRequest) Reset()

### func (*MarkAsAwayRequest) String 
    
    
    func (x *MarkAsAwayRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkAsDoNotDisturbRequest
    
    
    type MarkAsDoNotDisturbRequest struct {
    
    	// Required. The resource name of the availability to mark as Do Not Disturb.
    	// Format: users/{user}/availability
    	//
    	// `{user}` is the id for the Person in the People API or Admin SDK directory
    	// API. For example, `users/123456789`.
    	//
    	// The user's email address or `me` can also be used as an alias to refer to
    	// the caller.  For example, `users/user@example.com` or `users/me`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The expiration for the DND availability state. The user will be
    	// marked as Away after expiration. This can be at most 1 year from the
    	// current time.
    	//
    	// Types that are valid to be assigned to Expiration:
    	//
    	//	*MarkAsDoNotDisturbRequest_ExpireTime
    	//	*MarkAsDoNotDisturbRequest_Ttl
    	Expiration isMarkAsDoNotDisturbRequest_Expiration `protobuf_oneof:"expiration"`
    	// contains filtered or unexported fields
    }

Request message for the `MarkAsDoNotDisturb` method.

### func (*MarkAsDoNotDisturbRequest) Descriptor 
    
    
    func (*MarkAsDoNotDisturbRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkAsDoNotDisturbRequest.ProtoReflect.Descriptor instead.

### func (*MarkAsDoNotDisturbRequest) GetExpiration 
    
    
    func (x *MarkAsDoNotDisturbRequest) GetExpiration() isMarkAsDoNotDisturbRequest_Expiration

### func (*MarkAsDoNotDisturbRequest) GetExpireTime 
    
    
    func (x *MarkAsDoNotDisturbRequest) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*MarkAsDoNotDisturbRequest) GetName 
    
    
    func (x *MarkAsDoNotDisturbRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkAsDoNotDisturbRequest) GetTtl 
    
    
    func (x *MarkAsDoNotDisturbRequest) GetTtl() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*MarkAsDoNotDisturbRequest) ProtoMessage 
    
    
    func (*MarkAsDoNotDisturbRequest) ProtoMessage()

### func (*MarkAsDoNotDisturbRequest) ProtoReflect 
    
    
    func (x *MarkAsDoNotDisturbRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkAsDoNotDisturbRequest) Reset 
    
    
    func (x *MarkAsDoNotDisturbRequest) Reset()

### func (*MarkAsDoNotDisturbRequest) String 
    
    
    func (x *MarkAsDoNotDisturbRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkAsDoNotDisturbRequest_ExpireTime
    
    
    type MarkAsDoNotDisturbRequest_ExpireTime struct {
    	// The absolute timestamp when the DND state expires.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=expire_time,json=expireTime,proto3,oneof"`
    }

## MarkAsDoNotDisturbRequest_Ttl
    
    
    type MarkAsDoNotDisturbRequest_Ttl struct {
    	// The duration from the current time until the DND state expires.
    	Ttl *durationpb.Duration `protobuf:"bytes,3,opt,name=ttl,proto3,oneof"`
    }

## MarkupSyntax
    
    
    type MarkupSyntax [int32](https://pkg.go.dev/builtin#int32)

Specifies the markup syntax used to format the Chat message text. Applies to the `text` field of the `Message` resource.

### MarkupSyntax_MARKUP_SYNTAX_UNSPECIFIED, MarkupSyntax_MARKUP_SYNTAX_CHAT, MarkupSyntax_MARKUP_SYNTAX_MARKDOWN
    
    
    const (
    	// Represents the unspecified value.
    	MarkupSyntax_MARKUP_SYNTAX_UNSPECIFIED MarkupSyntax = 0
    	// Uses Google Chat's markup syntax.
    	// See
    	// https://developers.google.com/workspace/chat/format-messages#format-texts
    	// for more information.
    	MarkupSyntax_MARKUP_SYNTAX_CHAT MarkupSyntax = 1
    	// Uses Markdown syntax. This syntax is based on the
    	// [CommonMark](https://commonmark.org/help/) specification, with additional
    	// extensions.
    	// See
    	// https://developers.google.com/workspace/chat/format-messages#format-texts
    	// for more information.
    	MarkupSyntax_MARKUP_SYNTAX_MARKDOWN MarkupSyntax = 2
    )

### func (MarkupSyntax) Descriptor 
    
    
    func (MarkupSyntax) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MarkupSyntax) Enum 
    
    
    func (x MarkupSyntax) Enum() *MarkupSyntax

### func (MarkupSyntax) EnumDescriptor 
    
    
    func (MarkupSyntax) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkupSyntax.Descriptor instead.

### func (MarkupSyntax) Number 
    
    
    func (x MarkupSyntax) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MarkupSyntax) String 
    
    
    func (x MarkupSyntax) String() [string](https://pkg.go.dev/builtin#string)

### func (MarkupSyntax) Type 
    
    
    func (MarkupSyntax) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MatchedUrl
    
    
    type MatchedUrl struct {
    
    	// Output only. The URL that was matched.
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=url,proto3" json:"url,omitempty"`
    	// contains filtered or unexported fields
    }

A matched URL in a Chat message. Chat apps can preview matched URLs. For more information, see [Preview links](https://developers.google.com/chat/how-tos/preview-links).

### func (*MatchedUrl) Descriptor 
    
    
    func (*MatchedUrl) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MatchedUrl.ProtoReflect.Descriptor instead.

### func (*MatchedUrl) GetUrl 
    
    
    func (x *MatchedUrl) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*MatchedUrl) ProtoMessage 
    
    
    func (*MatchedUrl) ProtoMessage()

### func (*MatchedUrl) ProtoReflect 
    
    
    func (x *MatchedUrl) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MatchedUrl) Reset 
    
    
    func (x *MatchedUrl) Reset()

### func (*MatchedUrl) String 
    
    
    func (x *MatchedUrl) String() [string](https://pkg.go.dev/builtin#string)

## MeetSpaceLinkData
    
    
    type MeetSpaceLinkData struct {
    
    	// Meeting code of the linked Meet space.
    	MeetingCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=meeting_code,json=meetingCode,proto3" json:"meeting_code,omitempty"`
    	// Indicates the type of the Meet space.
    	Type MeetSpaceLinkData_Type `protobuf:"varint,2,opt,name=type,proto3,enum=google.chat.v1.MeetSpaceLinkData_Type" json:"type,omitempty"`
    	// Optional. Output only. If the Meet is a Huddle, indicates the status of the
    	// huddle. Otherwise, this is unset.
    	HuddleStatus MeetSpaceLinkData_HuddleStatus `protobuf:"varint,3,opt,name=huddle_status,json=huddleStatus,proto3,enum=google.chat.v1.MeetSpaceLinkData_HuddleStatus" json:"huddle_status,omitempty"`
    	// contains filtered or unexported fields
    }

Data for Meet space links.

### func (*MeetSpaceLinkData) Descriptor 
    
    
    func (*MeetSpaceLinkData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MeetSpaceLinkData.ProtoReflect.Descriptor instead.

### func (*MeetSpaceLinkData) GetHuddleStatus 
    
    
    func (x *MeetSpaceLinkData) GetHuddleStatus() MeetSpaceLinkData_HuddleStatus

### func (*MeetSpaceLinkData) GetMeetingCode 
    
    
    func (x *MeetSpaceLinkData) GetMeetingCode() [string](https://pkg.go.dev/builtin#string)

### func (*MeetSpaceLinkData) GetType 
    
    
    func (x *MeetSpaceLinkData) GetType() MeetSpaceLinkData_Type

### func (*MeetSpaceLinkData) ProtoMessage 
    
    
    func (*MeetSpaceLinkData) ProtoMessage()

### func (*MeetSpaceLinkData) ProtoReflect 
    
    
    func (x *MeetSpaceLinkData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MeetSpaceLinkData) Reset 
    
    
    func (x *MeetSpaceLinkData) Reset()

### func (*MeetSpaceLinkData) String 
    
    
    func (x *MeetSpaceLinkData) String() [string](https://pkg.go.dev/builtin#string)

## MeetSpaceLinkData_HuddleStatus
    
    
    type MeetSpaceLinkData_HuddleStatus [int32](https://pkg.go.dev/builtin#int32)

The status of the huddle

### MeetSpaceLinkData_HUDDLE_STATUS_UNSPECIFIED, MeetSpaceLinkData_STARTED, MeetSpaceLinkData_ENDED, MeetSpaceLinkData_MISSED
    
    
    const (
    	// Default value for the enum. Don't use.
    	MeetSpaceLinkData_HUDDLE_STATUS_UNSPECIFIED MeetSpaceLinkData_HuddleStatus = 0
    	// The huddle has started.
    	MeetSpaceLinkData_STARTED MeetSpaceLinkData_HuddleStatus = 1
    	// The huddle has ended. In this case the Meet space URI and identifiers
    	// will no longer be valid.
    	MeetSpaceLinkData_ENDED MeetSpaceLinkData_HuddleStatus = 2
    	// The huddle has been missed. In this case the Meet space URI and
    	// identifiers will no longer be valid.
    	MeetSpaceLinkData_MISSED MeetSpaceLinkData_HuddleStatus = 3
    )

### func (MeetSpaceLinkData_HuddleStatus) Descriptor 
    
    
    func (MeetSpaceLinkData_HuddleStatus) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MeetSpaceLinkData_HuddleStatus) Enum 
    
    
    func (x MeetSpaceLinkData_HuddleStatus) Enum() *MeetSpaceLinkData_HuddleStatus

### func (MeetSpaceLinkData_HuddleStatus) EnumDescriptor 
    
    
    func (MeetSpaceLinkData_HuddleStatus) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MeetSpaceLinkData_HuddleStatus.Descriptor instead.

### func (MeetSpaceLinkData_HuddleStatus) Number 
    
    
    func (x MeetSpaceLinkData_HuddleStatus) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MeetSpaceLinkData_HuddleStatus) String 
    
    
    func (x MeetSpaceLinkData_HuddleStatus) String() [string](https://pkg.go.dev/builtin#string)

### func (MeetSpaceLinkData_HuddleStatus) Type 
    
    
    func (MeetSpaceLinkData_HuddleStatus) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MeetSpaceLinkData_Type
    
    
    type MeetSpaceLinkData_Type [int32](https://pkg.go.dev/builtin#int32)

The type of the Meet space.

### MeetSpaceLinkData_TYPE_UNSPECIFIED, MeetSpaceLinkData_MEETING, MeetSpaceLinkData_HUDDLE
    
    
    const (
    	// Default value for the enum. Don't use.
    	MeetSpaceLinkData_TYPE_UNSPECIFIED MeetSpaceLinkData_Type = 0
    	// The Meet space is a meeting.
    	MeetSpaceLinkData_MEETING MeetSpaceLinkData_Type = 1
    	// The Meet space is a huddle.
    	MeetSpaceLinkData_HUDDLE MeetSpaceLinkData_Type = 2
    )

### func (MeetSpaceLinkData_Type) Descriptor 
    
    
    func (MeetSpaceLinkData_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MeetSpaceLinkData_Type) Enum 
    
    
    func (x MeetSpaceLinkData_Type) Enum() *MeetSpaceLinkData_Type

### func (MeetSpaceLinkData_Type) EnumDescriptor 
    
    
    func (MeetSpaceLinkData_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MeetSpaceLinkData_Type.Descriptor instead.

### func (MeetSpaceLinkData_Type) Number 
    
    
    func (x MeetSpaceLinkData_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MeetSpaceLinkData_Type) String 
    
    
    func (x MeetSpaceLinkData_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (MeetSpaceLinkData_Type) Type 
    
    
    func (MeetSpaceLinkData_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Membership
    
    
    type Membership struct {
    
    	// Identifier. Resource name of the membership, assigned by the server.
    	//
    	// Format: `spaces/{space}/members/{member}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. State of the membership.
    	State Membership_MembershipState `protobuf:"varint,2,opt,name=state,proto3,enum=google.chat.v1.Membership_MembershipState" json:"state,omitempty"`
    	// Optional. User's role within a Chat space, which determines their permitted
    	// actions in the space.
    	//
    	// This field can only be used as input in `UpdateMembership`.
    	Role Membership_MembershipRole `protobuf:"varint,7,opt,name=role,proto3,enum=google.chat.v1.Membership_MembershipRole" json:"role,omitempty"`
    	// Member associated with this membership. Other member types might be
    	// supported in the future.
    	//
    	// Types that are valid to be assigned to MemberType:
    	//
    	//	*Membership_Member
    	//	*Membership_GroupMember
    	MemberType isMembership_MemberType `protobuf_oneof:"memberType"`
    	// Optional. Immutable. The creation time of the membership, such as when a
    	// member joined or was invited to join a space. This field is output only,
    	// except when used to import historical memberships in import mode spaces.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Optional. Immutable. The deletion time of the membership, such as when a
    	// member left or was removed from a space. This field is output only, except
    	// when used to import historical memberships in import mode spaces.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Output only. A user's relationship to the Workspace organization that owns
    	// the space. In spaces owned by consumer accounts, the affiliation of all
    	// members is `EXTERNAL`.
    	Affiliation Membership_Affiliation `protobuf:"varint,9,opt,name=affiliation,proto3,enum=google.chat.v1.Membership_Affiliation" json:"affiliation,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a membership relation in Google Chat, such as whether a user or Chat app is invited to, part of, or absent from a space.

### func (*Membership) Descriptor 
    
    
    func (*Membership) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Membership.ProtoReflect.Descriptor instead.

### func (*Membership) GetAffiliation 
    
    
    func (x *Membership) GetAffiliation() Membership_Affiliation

### func (*Membership) GetCreateTime 
    
    
    func (x *Membership) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Membership) GetDeleteTime 
    
    
    func (x *Membership) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Membership) GetGroupMember 
    
    
    func (x *Membership) GetGroupMember() *Group

### func (*Membership) GetMember 
    
    
    func (x *Membership) GetMember() *User

### func (*Membership) GetMemberType 
    
    
    func (x *Membership) GetMemberType() isMembership_MemberType

### func (*Membership) GetName 
    
    
    func (x *Membership) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Membership) GetRole 
    
    
    func (x *Membership) GetRole() Membership_MembershipRole

### func (*Membership) GetState 
    
    
    func (x *Membership) GetState() Membership_MembershipState

### func (*Membership) ProtoMessage 
    
    
    func (*Membership) ProtoMessage()

### func (*Membership) ProtoReflect 
    
    
    func (x *Membership) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Membership) Reset 
    
    
    func (x *Membership) Reset()

### func (*Membership) String 
    
    
    func (x *Membership) String() [string](https://pkg.go.dev/builtin#string)

## MembershipBatchCreatedEventData
    
    
    type MembershipBatchCreatedEventData struct {
    
    	// A list of new memberships.
    	Memberships []*MembershipCreatedEventData `protobuf:"bytes,1,rep,name=memberships,proto3" json:"memberships,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple new memberships.

Event type: `google.workspace.chat.membership.v1.batchCreated`

### func (*MembershipBatchCreatedEventData) Descriptor 
    
    
    func (*MembershipBatchCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipBatchCreatedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipBatchCreatedEventData) GetMemberships 
    
    
    func (x *MembershipBatchCreatedEventData) GetMemberships() []*MembershipCreatedEventData

### func (*MembershipBatchCreatedEventData) ProtoMessage 
    
    
    func (*MembershipBatchCreatedEventData) ProtoMessage()

### func (*MembershipBatchCreatedEventData) ProtoReflect 
    
    
    func (x *MembershipBatchCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipBatchCreatedEventData) Reset 
    
    
    func (x *MembershipBatchCreatedEventData) Reset()

### func (*MembershipBatchCreatedEventData) String 
    
    
    func (x *MembershipBatchCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MembershipBatchDeletedEventData
    
    
    type MembershipBatchDeletedEventData struct {
    
    	// A list of deleted memberships.
    	Memberships []*MembershipDeletedEventData `protobuf:"bytes,1,rep,name=memberships,proto3" json:"memberships,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple deleted memberships.

Event type: `google.workspace.chat.membership.v1.batchDeleted`

### func (*MembershipBatchDeletedEventData) Descriptor 
    
    
    func (*MembershipBatchDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipBatchDeletedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipBatchDeletedEventData) GetMemberships 
    
    
    func (x *MembershipBatchDeletedEventData) GetMemberships() []*MembershipDeletedEventData

### func (*MembershipBatchDeletedEventData) ProtoMessage 
    
    
    func (*MembershipBatchDeletedEventData) ProtoMessage()

### func (*MembershipBatchDeletedEventData) ProtoReflect 
    
    
    func (x *MembershipBatchDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipBatchDeletedEventData) Reset 
    
    
    func (x *MembershipBatchDeletedEventData) Reset()

### func (*MembershipBatchDeletedEventData) String 
    
    
    func (x *MembershipBatchDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MembershipBatchUpdatedEventData
    
    
    type MembershipBatchUpdatedEventData struct {
    
    	// A list of updated memberships.
    	Memberships []*MembershipUpdatedEventData `protobuf:"bytes,1,rep,name=memberships,proto3" json:"memberships,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple updated memberships.

Event type: `google.workspace.chat.membership.v1.batchUpdated`

### func (*MembershipBatchUpdatedEventData) Descriptor 
    
    
    func (*MembershipBatchUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipBatchUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipBatchUpdatedEventData) GetMemberships 
    
    
    func (x *MembershipBatchUpdatedEventData) GetMemberships() []*MembershipUpdatedEventData

### func (*MembershipBatchUpdatedEventData) ProtoMessage 
    
    
    func (*MembershipBatchUpdatedEventData) ProtoMessage()

### func (*MembershipBatchUpdatedEventData) ProtoReflect 
    
    
    func (x *MembershipBatchUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipBatchUpdatedEventData) Reset 
    
    
    func (x *MembershipBatchUpdatedEventData) Reset()

### func (*MembershipBatchUpdatedEventData) String 
    
    
    func (x *MembershipBatchUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MembershipCreatedEventData
    
    
    type MembershipCreatedEventData struct {
    
    	// The new membership.
    	Membership *Membership `protobuf:"bytes,1,opt,name=membership,proto3" json:"membership,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a new membership.

Event type: `google.workspace.chat.membership.v1.created`.

### func (*MembershipCreatedEventData) Descriptor 
    
    
    func (*MembershipCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipCreatedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipCreatedEventData) GetMembership 
    
    
    func (x *MembershipCreatedEventData) GetMembership() *Membership

### func (*MembershipCreatedEventData) ProtoMessage 
    
    
    func (*MembershipCreatedEventData) ProtoMessage()

### func (*MembershipCreatedEventData) ProtoReflect 
    
    
    func (x *MembershipCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipCreatedEventData) Reset 
    
    
    func (x *MembershipCreatedEventData) Reset()

### func (*MembershipCreatedEventData) String 
    
    
    func (x *MembershipCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MembershipDeletedEventData
    
    
    type MembershipDeletedEventData struct {
    
    	// The deleted membership. Only the `name` and `state` fields are populated.
    	Membership *Membership `protobuf:"bytes,1,opt,name=membership,proto3" json:"membership,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a deleted membership.

Event type: `google.workspace.chat.membership.v1.deleted`

### func (*MembershipDeletedEventData) Descriptor 
    
    
    func (*MembershipDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipDeletedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipDeletedEventData) GetMembership 
    
    
    func (x *MembershipDeletedEventData) GetMembership() *Membership

### func (*MembershipDeletedEventData) ProtoMessage 
    
    
    func (*MembershipDeletedEventData) ProtoMessage()

### func (*MembershipDeletedEventData) ProtoReflect 
    
    
    func (x *MembershipDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipDeletedEventData) Reset 
    
    
    func (x *MembershipDeletedEventData) Reset()

### func (*MembershipDeletedEventData) String 
    
    
    func (x *MembershipDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MembershipUpdatedEventData
    
    
    type MembershipUpdatedEventData struct {
    
    	// The updated membership.
    	Membership *Membership `protobuf:"bytes,1,opt,name=membership,proto3" json:"membership,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for an updated membership.

Event type: `google.workspace.chat.membership.v1.updated`

### func (*MembershipUpdatedEventData) Descriptor 
    
    
    func (*MembershipUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MembershipUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*MembershipUpdatedEventData) GetMembership 
    
    
    func (x *MembershipUpdatedEventData) GetMembership() *Membership

### func (*MembershipUpdatedEventData) ProtoMessage 
    
    
    func (*MembershipUpdatedEventData) ProtoMessage()

### func (*MembershipUpdatedEventData) ProtoReflect 
    
    
    func (x *MembershipUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MembershipUpdatedEventData) Reset 
    
    
    func (x *MembershipUpdatedEventData) Reset()

### func (*MembershipUpdatedEventData) String 
    
    
    func (x *MembershipUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## Membership_Affiliation
    
    
    type Membership_Affiliation [int32](https://pkg.go.dev/builtin#int32)

Represents the affiliation of a user to the Google Workspace organization that owns the space. This enum may have more values added in the future.

### Membership_AFFILIATION_UNSPECIFIED, Membership_INTERNAL, Membership_EXTERNAL, Membership_MANAGED_EXTERNAL
    
    
    const (
    	// Default value. This value is unused.
    	Membership_AFFILIATION_UNSPECIFIED Membership_Affiliation = 0
    	// An account managed by the same Google Workspace organization that owns
    	// the space.
    	Membership_INTERNAL Membership_Affiliation = 1
    	// An account external to the Google Workspace organization that owns the
    	// space (e.g., a consumer account, or an account managed by a different
    	// Workspace organization).
    	Membership_EXTERNAL Membership_Affiliation = 2
    	// An account managed by the Workspace organization that owns the space,
    	// but provisioned for a user who is external to the organization (e.g., a
    	// Guest user). To learn more about guests, see
    	// https://support.google.com/chat/answer/16997417.
    	Membership_MANAGED_EXTERNAL Membership_Affiliation = 3
    )

### func (Membership_Affiliation) Descriptor 
    
    
    func (Membership_Affiliation) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Membership_Affiliation) Enum 
    
    
    func (x Membership_Affiliation) Enum() *Membership_Affiliation

### func (Membership_Affiliation) EnumDescriptor 
    
    
    func (Membership_Affiliation) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Membership_Affiliation.Descriptor instead.

### func (Membership_Affiliation) Number 
    
    
    func (x Membership_Affiliation) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Membership_Affiliation) String 
    
    
    func (x Membership_Affiliation) String() [string](https://pkg.go.dev/builtin#string)

### func (Membership_Affiliation) Type 
    
    
    func (Membership_Affiliation) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Membership_GroupMember
    
    
    type Membership_GroupMember struct {
    	// Optional. The Google Group the membership corresponds to.
    	//
    	// Reading or mutating memberships for Google Groups requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	GroupMember *Group `protobuf:"bytes,5,opt,name=group_member,json=groupMember,proto3,oneof"`
    }

## Membership_Member
    
    
    type Membership_Member struct {
    	// Optional. The Google Chat user or app the membership corresponds to.
    	// If your Chat app [authenticates as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// the output only populates the
    	// [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User)
    	// `name` and `type` fields for both internal and external users, unless
    	// they are members of the space or have a prior affinity, like a direct
    	// message (DM) conversation, with the calling user.
    	Member *User `protobuf:"bytes,3,opt,name=member,proto3,oneof"`
    }

## Membership_MembershipRole
    
    
    type Membership_MembershipRole [int32](https://pkg.go.dev/builtin#int32)

Represents a user's permitted actions in a Chat space. More enum values might be added in the future.

### Membership_MEMBERSHIP_ROLE_UNSPECIFIED, Membership_ROLE_MEMBER, Membership_ROLE_MANAGER, Membership_ROLE_ASSISTANT_MANAGER
    
    
    const (
    	// Default value. For [users][google.chat.v1.Membership.member]: they
    	// aren't a member of the space, but can be invited. For
    	// [Google Groups][google.chat.v1.Membership.group_member]: they're always
    	//
    	//	assigned this role (other enum values might be used in the future).
    	Membership_MEMBERSHIP_ROLE_UNSPECIFIED Membership_MembershipRole = 0
    	// A member of the space. In the Chat UI, this role is called Member.
    	//
    	// The user has basic permissions, like sending
    	// messages to the space.
    	// Managers and owners can grant members additional permissions in a space,
    	// including:
    	//
    	// - Add or remove members.
    	// - Modify space details.
    	// - Turn history on or off.
    	// - Mention everyone in the space with `@all`.
    	// - Manage Chat apps and webhooks installed in the space.
    	//
    	// In direct messages and unnamed group conversations, everyone
    	// has this role.
    	Membership_ROLE_MEMBER Membership_MembershipRole = 1
    	// A space owner. In the Chat UI, this role is called Owner.
    	//
    	// The user has the complete set of space permissions to manage the space,
    	// including:
    	//
    	// - Change the role of other members in the space to member, manager, or
    	// owner.
    	// - Delete the space.
    	//
    	// Only supported in
    	// [SpaceType.SPACE][google.chat.v1.Space.SpaceType] (named spaces).
    	//
    	// To learn more, see
    	// [Learn more about your role as a space
    	// owner or manager](https://support.google.com/chat/answer/11833441).
    	Membership_ROLE_MANAGER Membership_MembershipRole = 2
    	// A space manager. In the Chat UI, this role is called Manager.
    	//
    	// The user has all basic permissions of `ROLE_MEMBER`,
    	// and can be granted a subset of administrative permissions by an owner.
    	// By default, managers have all the permissions of an owner except for the
    	// ability to:
    	//
    	// - Delete the space.
    	// - Make another space member an owner.
    	// - Change an owner's role.
    	//
    	// By default, managers permissions include but aren't limited to:
    	//
    	//   - Make another member a manager.
    	//   - Delete messages in the space.
    	//   - Manage space permissions.
    	//   - Receive notifications for requests to join the space if the manager
    	//     has the "manage members" permission in the space settings.
    	//   - Make a space discoverable.
    	//
    	// Only supported in
    	// [SpaceType.SPACE][google.chat.v1.Space.SpaceType] (named spaces).
    	//
    	// To learn more, see
    	// [Manage space settings](https://support.google.com/chat/answer/13340792).
    	Membership_ROLE_ASSISTANT_MANAGER Membership_MembershipRole = 4
    )

### func (Membership_MembershipRole) Descriptor 
    
    
    func (Membership_MembershipRole) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Membership_MembershipRole) Enum 
    
    
    func (x Membership_MembershipRole) Enum() *Membership_MembershipRole

### func (Membership_MembershipRole) EnumDescriptor 
    
    
    func (Membership_MembershipRole) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Membership_MembershipRole.Descriptor instead.

### func (Membership_MembershipRole) Number 
    
    
    func (x Membership_MembershipRole) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Membership_MembershipRole) String 
    
    
    func (x Membership_MembershipRole) String() [string](https://pkg.go.dev/builtin#string)

### func (Membership_MembershipRole) Type 
    
    
    func (Membership_MembershipRole) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Membership_MembershipState
    
    
    type Membership_MembershipState [int32](https://pkg.go.dev/builtin#int32)

Specifies the member's relationship with a space. Other membership states might be supported in the future.

### Membership_MEMBERSHIP_STATE_UNSPECIFIED, Membership_JOINED, Membership_INVITED, Membership_NOT_A_MEMBER
    
    
    const (
    	// Default value. Don't use.
    	Membership_MEMBERSHIP_STATE_UNSPECIFIED Membership_MembershipState = 0
    	// The user is added to the space, and can participate in the space.
    	Membership_JOINED Membership_MembershipState = 1
    	// The user is invited to join the space, but hasn't joined it.
    	Membership_INVITED Membership_MembershipState = 2
    	// The user doesn't belong to the space and doesn't have a pending
    	// invitation to join the space.
    	Membership_NOT_A_MEMBER Membership_MembershipState = 3
    )

### func (Membership_MembershipState) Descriptor 
    
    
    func (Membership_MembershipState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Membership_MembershipState) Enum 
    
    
    func (x Membership_MembershipState) Enum() *Membership_MembershipState

### func (Membership_MembershipState) EnumDescriptor 
    
    
    func (Membership_MembershipState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Membership_MembershipState.Descriptor instead.

### func (Membership_MembershipState) Number 
    
    
    func (x Membership_MembershipState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Membership_MembershipState) String 
    
    
    func (x Membership_MembershipState) String() [string](https://pkg.go.dev/builtin#string)

### func (Membership_MembershipState) Type 
    
    
    func (Membership_MembershipState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Message
    
    
    type Message struct {
    
    	// Identifier. Resource name of the message.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	//
    	// Where `{space}` is the ID of the space where the message is posted and
    	// `{message}` is a system-assigned ID for the message. For example,
    	// `spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB`.
    	//
    	// If you set a custom ID when you create a message, you can use this ID to
    	// specify the message in a request by replacing `{message}` with the value
    	// from the `clientAssignedMessageId` field. For example,
    	// `spaces/AAAAAAAAAAA/messages/client-custom-name`. For details, see [Name
    	// a
    	// message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The user who created the message.
    	// If your Chat app [authenticates as a
    	// user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// the output only populates the
    	// [user](https://developers.google.com/workspace/chat/api/reference/rest/v1/User)
    	// `name` and `type` fields for both internal and external users, unless they
    	// are members of the space or have a prior affinity, like a direct message
    	// (DM) conversation, with the calling user.
    	Sender *User `protobuf:"bytes,2,opt,name=sender,proto3" json:"sender,omitempty"`
    	// Optional. Immutable. For spaces created in Chat, the time at which the
    	// message was created. This field is output only, except when used in import
    	// mode spaces.
    	//
    	// For import mode spaces, set this field to the historical timestamp at which
    	// the message was created in the source in order to preserve the original
    	// creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time at which the message was last edited by a user. If
    	// the message has never been edited, this field is empty.
    	LastUpdateTime *timestamppb.Timestamp `protobuf:"bytes,23,opt,name=last_update_time,json=lastUpdateTime,proto3" json:"last_update_time,omitempty"`
    	// Output only. The time at which the message was deleted in
    	// Google Chat. If the message is never deleted, this field is empty.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,26,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Optional. Plain-text body of the message. The first link to an image,
    	// video, or web page generates a [preview
    	// chip](https://developers.google.com/workspace/chat/preview-links). You can
    	// also [@mention a Google Chat
    	// user](https://developers.google.com/workspace/chat/format-messages#messages-@mention),
    	// or everyone in the space.
    	//
    	// To learn about creating text messages, see [Send a
    	// message](https://developers.google.com/workspace/chat/create-messages).
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=text,proto3" json:"text,omitempty"`
    	// Output only. Contains the message `text` with markups added to communicate
    	// formatting. This field might not capture all formatting visible in the UI,
    	// but includes the following:
    	//
    	// * [Markup
    	// syntax](https://developers.google.com/workspace/chat/format-messages)
    	// for bold, italic, strikethrough, monospace, monospace block, bulleted
    	// list, and block quote.
    	//
    	// * [User
    	// mentions](https://developers.google.com/workspace/chat/format-messages#messages-@mention)
    	// using the format `

A message in a Google Chat space.

### func (*Message) Descriptor 
    
    
    func (*Message) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Message.ProtoReflect.Descriptor instead.

### func (*Message) GetAccessoryWidgets 
    
    
    func (x *Message) GetAccessoryWidgets() []*AccessoryWidget

### func (*Message) GetActionResponse 
    
    
    func (x *Message) GetActionResponse() *ActionResponse

### func (*Message) GetAnnotations 
    
    
    func (x *Message) GetAnnotations() []*Annotation

### func (*Message) GetArgumentText 
    
    
    func (x *Message) GetArgumentText() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetAttachedGifs 
    
    
    func (x *Message) GetAttachedGifs() []*AttachedGif

### func (*Message) GetAttachment 
    
    
    func (x *Message) GetAttachment() []*Attachment

### func (*Message) GetCards 
    
    
    func (x *Message) GetCards() []*ContextualAddOnMarkup_Card

Deprecated: Marked as deprecated in google/chat/v1/message.proto.

### func (*Message) GetCardsV2 
    
    
    func (x *Message) GetCardsV2() []*CardWithId

### func (*Message) GetClientAssignedMessageId 
    
    
    func (x *Message) GetClientAssignedMessageId() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetCreateTime 
    
    
    func (x *Message) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Message) GetDeleteTime 
    
    
    func (x *Message) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Message) GetDeletionMetadata 
    
    
    func (x *Message) GetDeletionMetadata() *DeletionMetadata

### func (*Message) GetEmojiReactionSummaries 
    
    
    func (x *Message) GetEmojiReactionSummaries() []*EmojiReactionSummary

### func (*Message) GetFallbackText 
    
    
    func (x *Message) GetFallbackText() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetFormattedText 
    
    
    func (x *Message) GetFormattedText() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetLastUpdateTime 
    
    
    func (x *Message) GetLastUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Message) GetMarkupSyntax 
    
    
    func (x *Message) GetMarkupSyntax() MarkupSyntax

### func (*Message) GetMatchedUrl 
    
    
    func (x *Message) GetMatchedUrl() *MatchedUrl

### func (*Message) GetName 
    
    
    func (x *Message) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetPrivateMessageViewer 
    
    
    func (x *Message) GetPrivateMessageViewer() *User

### func (*Message) GetQuotedMessageMetadata 
    
    
    func (x *Message) GetQuotedMessageMetadata() *QuotedMessageMetadata

### func (*Message) GetSender 
    
    
    func (x *Message) GetSender() *User

### func (*Message) GetSilent 
    
    
    func (x *Message) GetSilent() [bool](https://pkg.go.dev/builtin#bool)

### func (*Message) GetSlashCommand 
    
    
    func (x *Message) GetSlashCommand() *SlashCommand

### func (*Message) GetSpace 
    
    
    func (x *Message) GetSpace() *Space

### func (*Message) GetText 
    
    
    func (x *Message) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetThread 
    
    
    func (x *Message) GetThread() *Thread

### func (*Message) GetThreadReply 
    
    
    func (x *Message) GetThreadReply() [bool](https://pkg.go.dev/builtin#bool)

### func (*Message) ProtoMessage 
    
    
    func (*Message) ProtoMessage()

### func (*Message) ProtoReflect 
    
    
    func (x *Message) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Message) Reset 
    
    
    func (x *Message) Reset()

### func (*Message) String 
    
    
    func (x *Message) String() [string](https://pkg.go.dev/builtin#string)

## MessageBatchCreatedEventData
    
    
    type MessageBatchCreatedEventData struct {
    
    	// A list of new messages.
    	Messages []*MessageCreatedEventData `protobuf:"bytes,1,rep,name=messages,proto3" json:"messages,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple new messages.

Event type: `google.workspace.chat.message.v1.batchCreated`

### func (*MessageBatchCreatedEventData) Descriptor 
    
    
    func (*MessageBatchCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageBatchCreatedEventData.ProtoReflect.Descriptor instead.

### func (*MessageBatchCreatedEventData) GetMessages 
    
    
    func (x *MessageBatchCreatedEventData) GetMessages() []*MessageCreatedEventData

### func (*MessageBatchCreatedEventData) ProtoMessage 
    
    
    func (*MessageBatchCreatedEventData) ProtoMessage()

### func (*MessageBatchCreatedEventData) ProtoReflect 
    
    
    func (x *MessageBatchCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageBatchCreatedEventData) Reset 
    
    
    func (x *MessageBatchCreatedEventData) Reset()

### func (*MessageBatchCreatedEventData) String 
    
    
    func (x *MessageBatchCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MessageBatchDeletedEventData
    
    
    type MessageBatchDeletedEventData struct {
    
    	// A list of deleted messages.
    	Messages []*MessageDeletedEventData `protobuf:"bytes,1,rep,name=messages,proto3" json:"messages,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple deleted messages.

Event type: `google.workspace.chat.message.v1.batchDeleted`

### func (*MessageBatchDeletedEventData) Descriptor 
    
    
    func (*MessageBatchDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageBatchDeletedEventData.ProtoReflect.Descriptor instead.

### func (*MessageBatchDeletedEventData) GetMessages 
    
    
    func (x *MessageBatchDeletedEventData) GetMessages() []*MessageDeletedEventData

### func (*MessageBatchDeletedEventData) ProtoMessage 
    
    
    func (*MessageBatchDeletedEventData) ProtoMessage()

### func (*MessageBatchDeletedEventData) ProtoReflect 
    
    
    func (x *MessageBatchDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageBatchDeletedEventData) Reset 
    
    
    func (x *MessageBatchDeletedEventData) Reset()

### func (*MessageBatchDeletedEventData) String 
    
    
    func (x *MessageBatchDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MessageBatchUpdatedEventData
    
    
    type MessageBatchUpdatedEventData struct {
    
    	// A list of updated messages.
    	Messages []*MessageUpdatedEventData `protobuf:"bytes,1,rep,name=messages,proto3" json:"messages,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple updated messages.

Event type: `google.workspace.chat.message.v1.batchUpdated`

### func (*MessageBatchUpdatedEventData) Descriptor 
    
    
    func (*MessageBatchUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageBatchUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*MessageBatchUpdatedEventData) GetMessages 
    
    
    func (x *MessageBatchUpdatedEventData) GetMessages() []*MessageUpdatedEventData

### func (*MessageBatchUpdatedEventData) ProtoMessage 
    
    
    func (*MessageBatchUpdatedEventData) ProtoMessage()

### func (*MessageBatchUpdatedEventData) ProtoReflect 
    
    
    func (x *MessageBatchUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageBatchUpdatedEventData) Reset 
    
    
    func (x *MessageBatchUpdatedEventData) Reset()

### func (*MessageBatchUpdatedEventData) String 
    
    
    func (x *MessageBatchUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MessageCreatedEventData
    
    
    type MessageCreatedEventData struct {
    
    	// The new message.
    	Message *Message `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a new message.

Event type: `google.workspace.chat.message.v1.created`

### func (*MessageCreatedEventData) Descriptor 
    
    
    func (*MessageCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageCreatedEventData.ProtoReflect.Descriptor instead.

### func (*MessageCreatedEventData) GetMessage 
    
    
    func (x *MessageCreatedEventData) GetMessage() *Message

### func (*MessageCreatedEventData) ProtoMessage 
    
    
    func (*MessageCreatedEventData) ProtoMessage()

### func (*MessageCreatedEventData) ProtoReflect 
    
    
    func (x *MessageCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageCreatedEventData) Reset 
    
    
    func (x *MessageCreatedEventData) Reset()

### func (*MessageCreatedEventData) String 
    
    
    func (x *MessageCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MessageDeletedEventData
    
    
    type MessageDeletedEventData struct {
    
    	// The deleted message. Only the `name`, `createTime`, and
    	// `deletionMetadata` fields are populated.
    	Message *Message `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a deleted message.

Event type: `google.workspace.chat.message.v1.deleted`

### func (*MessageDeletedEventData) Descriptor 
    
    
    func (*MessageDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageDeletedEventData.ProtoReflect.Descriptor instead.

### func (*MessageDeletedEventData) GetMessage 
    
    
    func (x *MessageDeletedEventData) GetMessage() *Message

### func (*MessageDeletedEventData) ProtoMessage 
    
    
    func (*MessageDeletedEventData) ProtoMessage()

### func (*MessageDeletedEventData) ProtoReflect 
    
    
    func (x *MessageDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageDeletedEventData) Reset 
    
    
    func (x *MessageDeletedEventData) Reset()

### func (*MessageDeletedEventData) String 
    
    
    func (x *MessageDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MessagePin
    
    
    type MessagePin struct {
    
    	// Identifier. The resource name of the message pin.
    	// Format: `spaces/{space}/messagePins/{message_pin}`
    	// The resource ID component matches the resource ID component of the
    	// message. For example, a message with `spaces/AAA/messages/bbb.ccc`
    	// corresponds to the message pin with the resource name
    	// `spaces/AAA/messagePins/bbb.ccc`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Immutable. The resource name of the message that is pinned.
    	// Format: `spaces/{space}/messages/{message}`
    	Message [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

A pin on a Chat message. For more information see [Pin a message](https://support.google.com/chat?p=chat-board-hc).

### func (*MessagePin) Descriptor 
    
    
    func (*MessagePin) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessagePin.ProtoReflect.Descriptor instead.

### func (*MessagePin) GetMessage 
    
    
    func (x *MessagePin) GetMessage() [string](https://pkg.go.dev/builtin#string)

### func (*MessagePin) GetName 
    
    
    func (x *MessagePin) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MessagePin) ProtoMessage 
    
    
    func (*MessagePin) ProtoMessage()

### func (*MessagePin) ProtoReflect 
    
    
    func (x *MessagePin) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessagePin) Reset 
    
    
    func (x *MessagePin) Reset()

### func (*MessagePin) String 
    
    
    func (x *MessagePin) String() [string](https://pkg.go.dev/builtin#string)

## MessageUpdatedEventData
    
    
    type MessageUpdatedEventData struct {
    
    	// The updated message.
    	Message *Message `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for an updated message.

Event type: `google.workspace.chat.message.v1.updated`

### func (*MessageUpdatedEventData) Descriptor 
    
    
    func (*MessageUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessageUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*MessageUpdatedEventData) GetMessage 
    
    
    func (x *MessageUpdatedEventData) GetMessage() *Message

### func (*MessageUpdatedEventData) ProtoMessage 
    
    
    func (*MessageUpdatedEventData) ProtoMessage()

### func (*MessageUpdatedEventData) ProtoReflect 
    
    
    func (x *MessageUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessageUpdatedEventData) Reset 
    
    
    func (x *MessageUpdatedEventData) Reset()

### func (*MessageUpdatedEventData) String 
    
    
    func (x *MessageUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## MoveSectionItemRequest
    
    
    type MoveSectionItemRequest struct {
    
    	// Required. The resource name of the section item to move.
    	//
    	// Format: `users/{user}/sections/{section}/items/{item}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The resource name of the section to move the section item to.
    	//
    	// Format: `users/{user}/sections/{section}`
    	TargetSection [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=target_section,json=targetSection,proto3" json:"target_section,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for moving a section item across sections.

### func (*MoveSectionItemRequest) Descriptor 
    
    
    func (*MoveSectionItemRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MoveSectionItemRequest.ProtoReflect.Descriptor instead.

### func (*MoveSectionItemRequest) GetName 
    
    
    func (x *MoveSectionItemRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MoveSectionItemRequest) GetTargetSection 
    
    
    func (x *MoveSectionItemRequest) GetTargetSection() [string](https://pkg.go.dev/builtin#string)

### func (*MoveSectionItemRequest) ProtoMessage 
    
    
    func (*MoveSectionItemRequest) ProtoMessage()

### func (*MoveSectionItemRequest) ProtoReflect 
    
    
    func (x *MoveSectionItemRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MoveSectionItemRequest) Reset 
    
    
    func (x *MoveSectionItemRequest) Reset()

### func (*MoveSectionItemRequest) String 
    
    
    func (x *MoveSectionItemRequest) String() [string](https://pkg.go.dev/builtin#string)

## MoveSectionItemResponse
    
    
    type MoveSectionItemResponse struct {
    
    	// The updated section item.
    	SectionItem *SectionItem `protobuf:"bytes,1,opt,name=section_item,json=sectionItem,proto3" json:"section_item,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for moving a section item.

### func (*MoveSectionItemResponse) Descriptor 
    
    
    func (*MoveSectionItemResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MoveSectionItemResponse.ProtoReflect.Descriptor instead.

### func (*MoveSectionItemResponse) GetSectionItem 
    
    
    func (x *MoveSectionItemResponse) GetSectionItem() *SectionItem

### func (*MoveSectionItemResponse) ProtoMessage 
    
    
    func (*MoveSectionItemResponse) ProtoMessage()

### func (*MoveSectionItemResponse) ProtoReflect 
    
    
    func (x *MoveSectionItemResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MoveSectionItemResponse) Reset 
    
    
    func (x *MoveSectionItemResponse) Reset()

### func (*MoveSectionItemResponse) String 
    
    
    func (x *MoveSectionItemResponse) String() [string](https://pkg.go.dev/builtin#string)

## PositionSectionRequest
    
    
    type PositionSectionRequest struct {
    
    	// Required. The resource name of the section to position.
    	//
    	// Format: `users/{user}/sections/{section}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The new position of the section.
    	//
    	// Types that are valid to be assigned to Position:
    	//
    	//	*PositionSectionRequest_SortOrder
    	//	*PositionSectionRequest_RelativePosition
    	Position isPositionSectionRequest_Position `protobuf_oneof:"position"`
    	// contains filtered or unexported fields
    }

Request message for positioning a section.

### func (*PositionSectionRequest) Descriptor 
    
    
    func (*PositionSectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PositionSectionRequest.ProtoReflect.Descriptor instead.

### func (*PositionSectionRequest) GetName 
    
    
    func (x *PositionSectionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*PositionSectionRequest) GetPosition 
    
    
    func (x *PositionSectionRequest) GetPosition() isPositionSectionRequest_Position

### func (*PositionSectionRequest) GetRelativePosition 
    
    
    func (x *PositionSectionRequest) GetRelativePosition() PositionSectionRequest_Position

### func (*PositionSectionRequest) GetSortOrder 
    
    
    func (x *PositionSectionRequest) GetSortOrder() [int32](https://pkg.go.dev/builtin#int32)

### func (*PositionSectionRequest) ProtoMessage 
    
    
    func (*PositionSectionRequest) ProtoMessage()

### func (*PositionSectionRequest) ProtoReflect 
    
    
    func (x *PositionSectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PositionSectionRequest) Reset 
    
    
    func (x *PositionSectionRequest) Reset()

### func (*PositionSectionRequest) String 
    
    
    func (x *PositionSectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## PositionSectionRequest_Position
    
    
    type PositionSectionRequest_Position [int32](https://pkg.go.dev/builtin#int32)

The position of the section.

### PositionSectionRequest_POSITION_UNSPECIFIED, PositionSectionRequest_START, PositionSectionRequest_END
    
    
    const (
    	// Unspecified position.
    	PositionSectionRequest_POSITION_UNSPECIFIED PositionSectionRequest_Position = 0
    	// Start of the list of sections.
    	PositionSectionRequest_START PositionSectionRequest_Position = 1
    	// End of the list of sections.
    	PositionSectionRequest_END PositionSectionRequest_Position = 2
    )

### func (PositionSectionRequest_Position) Descriptor 
    
    
    func (PositionSectionRequest_Position) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PositionSectionRequest_Position) Enum 
    
    
    func (x PositionSectionRequest_Position) Enum() *PositionSectionRequest_Position

### func (PositionSectionRequest_Position) EnumDescriptor 
    
    
    func (PositionSectionRequest_Position) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PositionSectionRequest_Position.Descriptor instead.

### func (PositionSectionRequest_Position) Number 
    
    
    func (x PositionSectionRequest_Position) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PositionSectionRequest_Position) String 
    
    
    func (x PositionSectionRequest_Position) String() [string](https://pkg.go.dev/builtin#string)

### func (PositionSectionRequest_Position) Type 
    
    
    func (PositionSectionRequest_Position) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## PositionSectionRequest_RelativePosition
    
    
    type PositionSectionRequest_RelativePosition struct {
    	// Optional. The relative position of the section in the list of sections.
    	RelativePosition PositionSectionRequest_Position `protobuf:"varint,3,opt,name=relative_position,json=relativePosition,proto3,enum=google.chat.v1.PositionSectionRequest_Position,oneof"`
    }

## PositionSectionRequest_SortOrder
    
    
    type PositionSectionRequest_SortOrder struct {
    	// Optional. The absolute position of the section in the list of sections.
    	// The position must be greater than 0. If the position is greater than the
    	// number of sections, the section will be appended to the end of the list.
    	// This operation inserts the section at the given position and shifts the
    	// original section at that position, and those below it, to the next
    	// position.
    	SortOrder [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=sort_order,json=sortOrder,proto3,oneof"`
    }

## PositionSectionResponse
    
    
    type PositionSectionResponse struct {
    
    	// The updated section.
    	Section *Section `protobuf:"bytes,1,opt,name=section,proto3" json:"section,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for positioning a section.

### func (*PositionSectionResponse) Descriptor 
    
    
    func (*PositionSectionResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PositionSectionResponse.ProtoReflect.Descriptor instead.

### func (*PositionSectionResponse) GetSection 
    
    
    func (x *PositionSectionResponse) GetSection() *Section

### func (*PositionSectionResponse) ProtoMessage 
    
    
    func (*PositionSectionResponse) ProtoMessage()

### func (*PositionSectionResponse) ProtoReflect 
    
    
    func (x *PositionSectionResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PositionSectionResponse) Reset 
    
    
    func (x *PositionSectionResponse) Reset()

### func (*PositionSectionResponse) String 
    
    
    func (x *PositionSectionResponse) String() [string](https://pkg.go.dev/builtin#string)

## QuotedMessageMetadata
    
    
    type QuotedMessageMetadata struct {
    
    	// Required. Resource name of the message that is quoted.
    	//
    	// Format: `spaces/{space}/messages/{message}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The timestamp when the quoted message was created or when the
    	// quoted message was last updated.
    	//
    	// If the message was edited, use this field, `last_update_time`.
    	// If the message was never edited, use `create_time`.
    	//
    	// If `last_update_time` doesn't match the latest version of the quoted
    	// message, the request fails.
    	LastUpdateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=last_update_time,json=lastUpdateTime,proto3" json:"last_update_time,omitempty"`
    	// Optional. Specifies the quote type. If not set, defaults to REPLY in the
    	// message read/write path for backward compatibility.
    	QuoteType QuotedMessageMetadata_QuoteType `protobuf:"varint,4,opt,name=quote_type,json=quoteType,proto3,enum=google.chat.v1.QuotedMessageMetadata_QuoteType" json:"quote_type,omitempty"`
    	// Output only. A snapshot of the quoted message's content.
    	QuotedMessageSnapshot *QuotedMessageSnapshot `protobuf:"bytes,5,opt,name=quoted_message_snapshot,json=quotedMessageSnapshot,proto3" json:"quoted_message_snapshot,omitempty"`
    	// Output only. Metadata about the source space of the quoted message.
    	// Populated only for FORWARD quote type.
    	ForwardedMetadata *ForwardedMetadata `protobuf:"bytes,6,opt,name=forwarded_metadata,json=forwardedMetadata,proto3" json:"forwarded_metadata,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a message that another message quotes.

When you update a message, you can't add or replace the `quotedMessageMetadata` field, but you can remove it.

For example usage, see [Quote another message](https://developers.google.com/workspace/chat/create-messages#quote-a-message).

### func (*QuotedMessageMetadata) Descriptor 
    
    
    func (*QuotedMessageMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use QuotedMessageMetadata.ProtoReflect.Descriptor instead.

### func (*QuotedMessageMetadata) GetForwardedMetadata 
    
    
    func (x *QuotedMessageMetadata) GetForwardedMetadata() *ForwardedMetadata

### func (*QuotedMessageMetadata) GetLastUpdateTime 
    
    
    func (x *QuotedMessageMetadata) GetLastUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*QuotedMessageMetadata) GetName 
    
    
    func (x *QuotedMessageMetadata) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*QuotedMessageMetadata) GetQuoteType 
    
    
    func (x *QuotedMessageMetadata) GetQuoteType() QuotedMessageMetadata_QuoteType

### func (*QuotedMessageMetadata) GetQuotedMessageSnapshot 
    
    
    func (x *QuotedMessageMetadata) GetQuotedMessageSnapshot() *QuotedMessageSnapshot

### func (*QuotedMessageMetadata) ProtoMessage 
    
    
    func (*QuotedMessageMetadata) ProtoMessage()

### func (*QuotedMessageMetadata) ProtoReflect 
    
    
    func (x *QuotedMessageMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*QuotedMessageMetadata) Reset 
    
    
    func (x *QuotedMessageMetadata) Reset()

### func (*QuotedMessageMetadata) String 
    
    
    func (x *QuotedMessageMetadata) String() [string](https://pkg.go.dev/builtin#string)

## QuotedMessageMetadata_QuoteType
    
    
    type QuotedMessageMetadata_QuoteType [int32](https://pkg.go.dev/builtin#int32)

The quote type of the quoted message.

### QuotedMessageMetadata_QUOTE_TYPE_UNSPECIFIED, QuotedMessageMetadata_REPLY, QuotedMessageMetadata_FORWARD
    
    
    const (
    	// Reserved. This value is unused.
    	QuotedMessageMetadata_QUOTE_TYPE_UNSPECIFIED QuotedMessageMetadata_QuoteType = 0
    	// When `quote_type` is `REPLY`, you can do the following:
    	//
    	// * If you're replying in a thread, you can quote another message in that
    	// thread.
    	//
    	// * If you're creating a root message, you can quote another root message
    	// in that space.
    	QuotedMessageMetadata_REPLY QuotedMessageMetadata_QuoteType = 1
    	// When `quote_type` is `FORWARD`, you can quote a:
    	//
    	// * Message from a different space.
    	//
    	// * Message reply from a different thread in the same space.
    	QuotedMessageMetadata_FORWARD QuotedMessageMetadata_QuoteType = 2
    )

### func (QuotedMessageMetadata_QuoteType) Descriptor 
    
    
    func (QuotedMessageMetadata_QuoteType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (QuotedMessageMetadata_QuoteType) Enum 
    
    
    func (x QuotedMessageMetadata_QuoteType) Enum() *QuotedMessageMetadata_QuoteType

### func (QuotedMessageMetadata_QuoteType) EnumDescriptor 
    
    
    func (QuotedMessageMetadata_QuoteType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use QuotedMessageMetadata_QuoteType.Descriptor instead.

### func (QuotedMessageMetadata_QuoteType) Number 
    
    
    func (x QuotedMessageMetadata_QuoteType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (QuotedMessageMetadata_QuoteType) String 
    
    
    func (x QuotedMessageMetadata_QuoteType) String() [string](https://pkg.go.dev/builtin#string)

### func (QuotedMessageMetadata_QuoteType) Type 
    
    
    func (QuotedMessageMetadata_QuoteType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## QuotedMessageSnapshot
    
    
    type QuotedMessageSnapshot struct {
    
    	// Output only. The quoted message's author name.
    	// Populated for both REPLY & FORWARD quote types.
    	Sender [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=sender,proto3" json:"sender,omitempty"`
    	// Output only. Snapshot of the quoted message's text content.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=text,proto3" json:"text,omitempty"`
    	// Output only. Contains the quoted message `text` with markups added to
    	// support rich formatting like hyperlinks,custom emojis, markup, etc.
    	// Populated only for FORWARD quote type.
    	FormattedText [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=formatted_text,json=formattedText,proto3" json:"formatted_text,omitempty"`
    	// Output only. Annotations parsed from the text body of the quoted message.
    	// Populated only for FORWARD quote type.
    	Annotations []*Annotation `protobuf:"bytes,4,rep,name=annotations,proto3" json:"annotations,omitempty"`
    	// Output only. Attachments that were part of the quoted message. These are
    	// copies of the quoted message's attachment metadata. Populated only for
    	// FORWARD quote type.
    	Attachments []*Attachment `protobuf:"bytes,5,rep,name=attachments,proto3" json:"attachments,omitempty"`
    	// contains filtered or unexported fields
    }

Provides a snapshot of the content of the quoted message at the time of quoting or forwarding

### func (*QuotedMessageSnapshot) Descriptor 
    
    
    func (*QuotedMessageSnapshot) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use QuotedMessageSnapshot.ProtoReflect.Descriptor instead.

### func (*QuotedMessageSnapshot) GetAnnotations 
    
    
    func (x *QuotedMessageSnapshot) GetAnnotations() []*Annotation

### func (*QuotedMessageSnapshot) GetAttachments 
    
    
    func (x *QuotedMessageSnapshot) GetAttachments() []*Attachment

### func (*QuotedMessageSnapshot) GetFormattedText 
    
    
    func (x *QuotedMessageSnapshot) GetFormattedText() [string](https://pkg.go.dev/builtin#string)

### func (*QuotedMessageSnapshot) GetSender 
    
    
    func (x *QuotedMessageSnapshot) GetSender() [string](https://pkg.go.dev/builtin#string)

### func (*QuotedMessageSnapshot) GetText 
    
    
    func (x *QuotedMessageSnapshot) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*QuotedMessageSnapshot) ProtoMessage 
    
    
    func (*QuotedMessageSnapshot) ProtoMessage()

### func (*QuotedMessageSnapshot) ProtoReflect 
    
    
    func (x *QuotedMessageSnapshot) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*QuotedMessageSnapshot) Reset 
    
    
    func (x *QuotedMessageSnapshot) Reset()

### func (*QuotedMessageSnapshot) String 
    
    
    func (x *QuotedMessageSnapshot) String() [string](https://pkg.go.dev/builtin#string)

## Reaction
    
    
    type Reaction struct {
    
    	// Identifier. The resource name of the reaction.
    	//
    	// Format: `spaces/{space}/messages/{message}/reactions/{reaction}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The user who created the reaction.
    	User *User `protobuf:"bytes,2,opt,name=user,proto3" json:"user,omitempty"`
    	// Required. The emoji used in the reaction.
    	Emoji *Emoji `protobuf:"bytes,3,opt,name=emoji,proto3" json:"emoji,omitempty"`
    	// contains filtered or unexported fields
    }

A reaction to a message.

### func (*Reaction) Descriptor 
    
    
    func (*Reaction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Reaction.ProtoReflect.Descriptor instead.

### func (*Reaction) GetEmoji 
    
    
    func (x *Reaction) GetEmoji() *Emoji

### func (*Reaction) GetName 
    
    
    func (x *Reaction) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Reaction) GetUser 
    
    
    func (x *Reaction) GetUser() *User

### func (*Reaction) ProtoMessage 
    
    
    func (*Reaction) ProtoMessage()

### func (*Reaction) ProtoReflect 
    
    
    func (x *Reaction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Reaction) Reset 
    
    
    func (x *Reaction) Reset()

### func (*Reaction) String 
    
    
    func (x *Reaction) String() [string](https://pkg.go.dev/builtin#string)

## ReactionBatchCreatedEventData
    
    
    type ReactionBatchCreatedEventData struct {
    
    	// A list of new reactions.
    	Reactions []*ReactionCreatedEventData `protobuf:"bytes,1,rep,name=reactions,proto3" json:"reactions,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple new reactions.

Event type: `google.workspace.chat.reaction.v1.batchCreated`

### func (*ReactionBatchCreatedEventData) Descriptor 
    
    
    func (*ReactionBatchCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReactionBatchCreatedEventData.ProtoReflect.Descriptor instead.

### func (*ReactionBatchCreatedEventData) GetReactions 
    
    
    func (x *ReactionBatchCreatedEventData) GetReactions() []*ReactionCreatedEventData

### func (*ReactionBatchCreatedEventData) ProtoMessage 
    
    
    func (*ReactionBatchCreatedEventData) ProtoMessage()

### func (*ReactionBatchCreatedEventData) ProtoReflect 
    
    
    func (x *ReactionBatchCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReactionBatchCreatedEventData) Reset 
    
    
    func (x *ReactionBatchCreatedEventData) Reset()

### func (*ReactionBatchCreatedEventData) String 
    
    
    func (x *ReactionBatchCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## ReactionBatchDeletedEventData
    
    
    type ReactionBatchDeletedEventData struct {
    
    	// A list of deleted reactions.
    	Reactions []*ReactionDeletedEventData `protobuf:"bytes,1,rep,name=reactions,proto3" json:"reactions,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple deleted reactions.

Event type: `google.workspace.chat.reaction.v1.batchDeleted`

### func (*ReactionBatchDeletedEventData) Descriptor 
    
    
    func (*ReactionBatchDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReactionBatchDeletedEventData.ProtoReflect.Descriptor instead.

### func (*ReactionBatchDeletedEventData) GetReactions 
    
    
    func (x *ReactionBatchDeletedEventData) GetReactions() []*ReactionDeletedEventData

### func (*ReactionBatchDeletedEventData) ProtoMessage 
    
    
    func (*ReactionBatchDeletedEventData) ProtoMessage()

### func (*ReactionBatchDeletedEventData) ProtoReflect 
    
    
    func (x *ReactionBatchDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReactionBatchDeletedEventData) Reset 
    
    
    func (x *ReactionBatchDeletedEventData) Reset()

### func (*ReactionBatchDeletedEventData) String 
    
    
    func (x *ReactionBatchDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## ReactionCreatedEventData
    
    
    type ReactionCreatedEventData struct {
    
    	// The new reaction.
    	Reaction *Reaction `protobuf:"bytes,1,opt,name=reaction,proto3" json:"reaction,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a new reaction.

Event type: `google.workspace.chat.reaction.v1.created`

### func (*ReactionCreatedEventData) Descriptor 
    
    
    func (*ReactionCreatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReactionCreatedEventData.ProtoReflect.Descriptor instead.

### func (*ReactionCreatedEventData) GetReaction 
    
    
    func (x *ReactionCreatedEventData) GetReaction() *Reaction

### func (*ReactionCreatedEventData) ProtoMessage 
    
    
    func (*ReactionCreatedEventData) ProtoMessage()

### func (*ReactionCreatedEventData) ProtoReflect 
    
    
    func (x *ReactionCreatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReactionCreatedEventData) Reset 
    
    
    func (x *ReactionCreatedEventData) Reset()

### func (*ReactionCreatedEventData) String 
    
    
    func (x *ReactionCreatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## ReactionDeletedEventData
    
    
    type ReactionDeletedEventData struct {
    
    	// The deleted reaction.
    	Reaction *Reaction `protobuf:"bytes,1,opt,name=reaction,proto3" json:"reaction,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for a deleted reaction.

Type: `google.workspace.chat.reaction.v1.deleted`

### func (*ReactionDeletedEventData) Descriptor 
    
    
    func (*ReactionDeletedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReactionDeletedEventData.ProtoReflect.Descriptor instead.

### func (*ReactionDeletedEventData) GetReaction 
    
    
    func (x *ReactionDeletedEventData) GetReaction() *Reaction

### func (*ReactionDeletedEventData) ProtoMessage 
    
    
    func (*ReactionDeletedEventData) ProtoMessage()

### func (*ReactionDeletedEventData) ProtoReflect 
    
    
    func (x *ReactionDeletedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReactionDeletedEventData) Reset 
    
    
    func (x *ReactionDeletedEventData) Reset()

### func (*ReactionDeletedEventData) String 
    
    
    func (x *ReactionDeletedEventData) String() [string](https://pkg.go.dev/builtin#string)

## RichLinkMetadata
    
    
    type RichLinkMetadata struct {
    
    	// The URI of this link.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// The rich link type.
    	RichLinkType RichLinkMetadata_RichLinkType `protobuf:"varint,2,opt,name=rich_link_type,json=richLinkType,proto3,enum=google.chat.v1.RichLinkMetadata_RichLinkType" json:"rich_link_type,omitempty"`
    	// Data for the linked resource.
    	//
    	// Types that are valid to be assigned to Data:
    	//
    	//	*RichLinkMetadata_DriveLinkData
    	//	*RichLinkMetadata_ChatSpaceLinkData
    	//	*RichLinkMetadata_MeetSpaceLinkData
    	//	*RichLinkMetadata_CalendarEventLinkData
    	Data isRichLinkMetadata_Data `protobuf_oneof:"data"`
    	// contains filtered or unexported fields
    }

A rich link to a resource. Rich links can be associated with the plain-text body of the message or represent chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0.

### func (*RichLinkMetadata) Descriptor 
    
    
    func (*RichLinkMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RichLinkMetadata.ProtoReflect.Descriptor instead.

### func (*RichLinkMetadata) GetCalendarEventLinkData 
    
    
    func (x *RichLinkMetadata) GetCalendarEventLinkData() *CalendarEventLinkData

### func (*RichLinkMetadata) GetChatSpaceLinkData 
    
    
    func (x *RichLinkMetadata) GetChatSpaceLinkData() *ChatSpaceLinkData

### func (*RichLinkMetadata) GetData 
    
    
    func (x *RichLinkMetadata) GetData() isRichLinkMetadata_Data

### func (*RichLinkMetadata) GetDriveLinkData 
    
    
    func (x *RichLinkMetadata) GetDriveLinkData() *DriveLinkData

### func (*RichLinkMetadata) GetMeetSpaceLinkData 
    
    
    func (x *RichLinkMetadata) GetMeetSpaceLinkData() *MeetSpaceLinkData

### func (*RichLinkMetadata) GetRichLinkType 
    
    
    func (x *RichLinkMetadata) GetRichLinkType() RichLinkMetadata_RichLinkType

### func (*RichLinkMetadata) GetUri 
    
    
    func (x *RichLinkMetadata) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*RichLinkMetadata) ProtoMessage 
    
    
    func (*RichLinkMetadata) ProtoMessage()

### func (*RichLinkMetadata) ProtoReflect 
    
    
    func (x *RichLinkMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RichLinkMetadata) Reset 
    
    
    func (x *RichLinkMetadata) Reset()

### func (*RichLinkMetadata) String 
    
    
    func (x *RichLinkMetadata) String() [string](https://pkg.go.dev/builtin#string)

## RichLinkMetadata_CalendarEventLinkData
    
    
    type RichLinkMetadata_CalendarEventLinkData struct {
    	// Data for a Calendar event link.
    	CalendarEventLinkData *CalendarEventLinkData `protobuf:"bytes,6,opt,name=calendar_event_link_data,json=calendarEventLinkData,proto3,oneof"`
    }

## RichLinkMetadata_ChatSpaceLinkData
    
    
    type RichLinkMetadata_ChatSpaceLinkData struct {
    	// Data for a chat space link.
    	ChatSpaceLinkData *ChatSpaceLinkData `protobuf:"bytes,4,opt,name=chat_space_link_data,json=chatSpaceLinkData,proto3,oneof"`
    }

## RichLinkMetadata_DriveLinkData
    
    
    type RichLinkMetadata_DriveLinkData struct {
    	// Data for a drive link.
    	DriveLinkData *DriveLinkData `protobuf:"bytes,3,opt,name=drive_link_data,json=driveLinkData,proto3,oneof"`
    }

## RichLinkMetadata_MeetSpaceLinkData
    
    
    type RichLinkMetadata_MeetSpaceLinkData struct {
    	// Data for a Meet space link.
    	MeetSpaceLinkData *MeetSpaceLinkData `protobuf:"bytes,5,opt,name=meet_space_link_data,json=meetSpaceLinkData,proto3,oneof"`
    }

## RichLinkMetadata_RichLinkType
    
    
    type RichLinkMetadata_RichLinkType [int32](https://pkg.go.dev/builtin#int32)

The rich link type. More types might be added in the future.

### RichLinkMetadata_RICH_LINK_TYPE_UNSPECIFIED, RichLinkMetadata_DRIVE_FILE, RichLinkMetadata_CHAT_SPACE, RichLinkMetadata_GMAIL_MESSAGE, RichLinkMetadata_MEET_SPACE, RichLinkMetadata_CALENDAR_EVENT
    
    
    const (
    	// Default value for the enum. Don't use.
    	RichLinkMetadata_RICH_LINK_TYPE_UNSPECIFIED RichLinkMetadata_RichLinkType = 0
    	// A Google Drive rich link type.
    	RichLinkMetadata_DRIVE_FILE RichLinkMetadata_RichLinkType = 1
    	// A Chat space rich link type. For example, a space smart chip.
    	RichLinkMetadata_CHAT_SPACE RichLinkMetadata_RichLinkType = 2
    	// A Gmail message rich link type. Specifically, a Gmail chip from [Share to
    	// Chat](https://support.google.com/chat?p=chat_gmail). The API only
    	// supports reading messages with GMAIL_MESSAGE rich links.
    	RichLinkMetadata_GMAIL_MESSAGE RichLinkMetadata_RichLinkType = 3
    	// A Meet message rich link type. For example, a Meet chip.
    	RichLinkMetadata_MEET_SPACE RichLinkMetadata_RichLinkType = 4
    	// A Calendar message rich link type. For example, a Calendar chip.
    	RichLinkMetadata_CALENDAR_EVENT RichLinkMetadata_RichLinkType = 5
    )

### func (RichLinkMetadata_RichLinkType) Descriptor 
    
    
    func (RichLinkMetadata_RichLinkType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RichLinkMetadata_RichLinkType) Enum 
    
    
    func (x RichLinkMetadata_RichLinkType) Enum() *RichLinkMetadata_RichLinkType

### func (RichLinkMetadata_RichLinkType) EnumDescriptor 
    
    
    func (RichLinkMetadata_RichLinkType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RichLinkMetadata_RichLinkType.Descriptor instead.

### func (RichLinkMetadata_RichLinkType) Number 
    
    
    func (x RichLinkMetadata_RichLinkType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RichLinkMetadata_RichLinkType) String 
    
    
    func (x RichLinkMetadata_RichLinkType) String() [string](https://pkg.go.dev/builtin#string)

### func (RichLinkMetadata_RichLinkType) Type 
    
    
    func (RichLinkMetadata_RichLinkType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SearchMessageResult
    
    
    type SearchMessageResult struct {
    
    	// The matched message.
    	Message *Message `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// Indicates if the matched message is read by the calling user.
    	//
    	// Only returned if the request view is `SEARCH_MESSAGES_VIEW_FULL` and the
    	// calling credentials include one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	//   - `https://www.googleapis.com/auth/chat.users.readstate`
    	Read *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=read,proto3,oneof" json:"read,omitempty"`
    	// The mute setting of the calling user for the space where the message is
    	// posted. The caller app can use this information to decide how to process
    	// the message depending on whether the space is muted for the user or not.
    	//
    	// Only returned if the request view is `SEARCH_MESSAGES_VIEW_FULL` and the
    	// calling credentials include the following [authorization
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	//   - `https://www.googleapis.com/auth/chat.users.spacesettings`
    	SpaceMuteSetting SpaceNotificationSetting_MuteSetting `protobuf:"varint,4,opt,name=space_mute_setting,json=spaceMuteSetting,proto3,enum=google.chat.v1.SpaceNotificationSetting_MuteSetting" json:"space_mute_setting,omitempty"`
    	// contains filtered or unexported fields
    }

A single result item from a message search.

### func (*SearchMessageResult) Descriptor 
    
    
    func (*SearchMessageResult) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchMessageResult.ProtoReflect.Descriptor instead.

### func (*SearchMessageResult) GetMessage 
    
    
    func (x *SearchMessageResult) GetMessage() *Message

### func (*SearchMessageResult) GetRead 
    
    
    func (x *SearchMessageResult) GetRead() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchMessageResult) GetSpaceMuteSetting 
    
    
    func (x *SearchMessageResult) GetSpaceMuteSetting() SpaceNotificationSetting_MuteSetting

### func (*SearchMessageResult) ProtoMessage 
    
    
    func (*SearchMessageResult) ProtoMessage()

### func (*SearchMessageResult) ProtoReflect 
    
    
    func (x *SearchMessageResult) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchMessageResult) Reset 
    
    
    func (x *SearchMessageResult) Reset()

### func (*SearchMessageResult) String 
    
    
    func (x *SearchMessageResult) String() [string](https://pkg.go.dev/builtin#string)

## SearchMessagesRequest
    
    
    type SearchMessagesRequest struct {
    
    	// Required. The resource name of the space to search within.
    	//
    	// To search across all spaces the user has access to, set this field to
    	// `spaces/-`. Using any other value for `parent` results in an
    	// `INVALID_ARGUMENT` error.
    	//
    	// To limit the search to one or more spaces, use `space.name` or
    	// `space.display_name` in the `filter`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. A search query.
    	//
    	// The query can specify one or more search keywords, which are used to filter
    	// the results,
    	//
    	// You can also filter the results using the following message fields:
    	//
    	//   - `create_time`: Accepts a timestamp in
    	//     [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the
    	//     supported comparison operators are: `<` and="" `="">=`.
    	//   - `sender.name`: The resource name of the sender (`users/{user}`). Only
    	//     supports `=`. You can use the e-mail as an alias for `{user}`. For
    	//     example, `users/example@gmail.com`, where `example@gmail.com` is the
    	//     e-mail of the Google Chat user.
    	//   - `space.name`: The resource name of the space where the message is posted.
    	//     (`spaces/{space}`). Only supports `=`. If this filter is not set, the
    	//     search is performed across all direct messages and spaces the user has
    	//     access to as a space member.
    	//   - `space.display_name`: Supports the operator `:` (has) and filters spaces
    	//     based on a partial match of their display name. Results are limited to
    	//     the top five space matches. For example, `space.display_name:Project`
    	//     searches for messages in the top five spaces that contain the word
    	//     "Project" in their display names.
    	//   - `space.space_type`: The type of the space. Only supports `=`. For
    	//     example, `space.space_type="DIRECT_MESSAGE"` returns only messages from
    	//     direct messages. The possible values are `DIRECT_MESSAGE`, `GROUP_CHAT`,
    	//     and `SPACE`.
    	//   - `attachment`: Supports the operator `:*` (has any) to check for the
    	//     presence of attachments. If `attachment:*` is specified, only messages
    	//     that have at least one attachment are returned.
    	//   - `annotations.user_mentions.user.name`: The resource name of the mentioned
    	//     user (`users/{user}`). Only supports `:` (has). For example:
    	//     `annotations.user_mentions.user.name:"users/1234567890"` returns only
    	//     messages that contain a mention to the specified user. Alternatively, the
    	//     alias `me` can be used to filter for messages that mention the caller
    	//     user, for example: `annotations.user_mentions.user.name:users/me`. You
    	//     can also use the e-mail as an alias for `{user}`, for example,
    	//     `users/example@gmail.com`.
    	//
    	// For advanced filtering, the following functions are also available:
    	//
    	//   - `has_link()`: Returns only messages that have at least one hyperlink in
    	//     the message text.
    	//   - `is_unread()`: Filters out messages that have been read by the calling
    	//     user.
    	//
    	// Using the `space.display_name` or the `space.space_type` filters requires
    	// that the calling credentials include one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	// - `https://www.googleapis.com/auth/chat.spaces.readonly`
    	// - `https://www.googleapis.com/auth/chat.spaces`
    	//
    	// Using the `is_unread()` filter requires that the calling credentials
    	// include one of the following [authorization
    	// scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    	//
    	// - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
    	// - `https://www.googleapis.com/auth/chat.users.readstate`
    	//
    	// Across different fields, only `AND` operators are supported. A valid
    	// example is `sender.name = "users/1234567890" AND is_unread()`. The word
    	// `AND` is optional and is implied if omitted. For example, `sender.name =
    	// "users/1234567890" is_unread()` is valid and is equivalent to the previous
    	// example. An invalid example is `sender.name = "users/1234567890" OR
    	// is_unread()` because `OR` is not supported between different fields.
    	//
    	// Among the same field:
    	//
    	//   - `create_time` supports only `AND`, and can only be used to represent
    	//     an interval, such as `create_time >= "2022-01-01T00:00:00+00:00" AND
    	//     create_time < "2023-01-01t00:00:00+00:00"`.="" -="" `sender.name`="" supports="" only="" the="" `or`="" operator,="" for="" example:="" `sender.name="users/1234567890" or="" sender.name="users/0987654321" `.="" -="" `space.name`="" supports="" only="" the="" `or`="" operator,="" for="" example:="" `space.name="spaces/ABCDEFGH" or="" space.name="spaces/QWERTYUI" `.="" -="" `space.display_name`="" supports="" the="" operators="" `and`="" and="" `or`,="" but="" not="" a="" mix="" of="" both.="" for="" example:="" `space.display_name:project="" and="" space.display_name:tasks`="" returns="" messages="" that="" are="" in="" spaces="" with="" display="" names="" containing="" both="" `project`="" and="" `tasks`,="" whereas="" `space.display_name:project="" or="" space.display_name:tasks`="" returns="" messages="" that="" are="" in="" spaces="" with="" display="" names="" containing="" either="" `project`="" or="" `tasks`="" or="" both.="" -="" `space.space_type`="" supports="" only="" the="" `or`="" operator,="" for="" example:="" `space.space_type="DIRECT_MESSAGE" or="" space.space_type="GROUP_CHAT" `.="" -="" `annotations.user_mentions.user.name`="" supports="" the="" operators="" `and`="" and="" `or`,="" but="" not="" a="" mix="" of="" both.="" for="" example:="" `annotations.user_mentions.user.name:"users/1234567890"="" and="" annotations.user_mentions.user.name:"users/0987654321"`="" returns="" only="" messages="" that="" mentions="" both="" users,="" whereas="" `annotations.user_mentions.user.name:"users/1234567890"="" or="" annotations.user_mentions.user.name:"users/0987654321"`="" returns="" messages="" that="" mention="" either="" user="" or="" both.="" parentheses="" are="" required="" to="" disambiguate="" operator="" precedence="" when="" combining="" `and`="" and="" `or`="" operators="" in="" the="" same="" query.="" for="" example:="" `(sender.name="users/me" or="" sender.name="users/123456" )="" and="" is_unread()`.="" otherwise,="" parentheses="" are="" optional.="" the="" following="" example="" queries="" are="" valid:="" ```="" "pending="" reports"="" and="" create_time="">= "2023-01-01T00:00:00Z"
    	//
    	// sender.name = "users/example@gmail.com"
    	//
    	// annotations.user_mentions.user.name:"users/0987654321"
    	//
    	// attachment:* AND space.name = "spaces/ABCDEFGH"
    	//
    	// tasks AND is_unread() AND sender.name = "users/1234567890"
    	//
    	// "things to do" "urgent"
    	//
    	// (sender.name = "users/1234567890")
    	// AND (create_time < "2023-05-01t00:00:00z")="" tasks="" and="" space.name="spaces/ABCDEFGH" and="" has_link()="" "project="" one"="" is_unread()="" space.display_name:project="" tasks="" ```="" the="" maximum="" query="" length="" is="" 1,000="" characters.="" invalid="" queries="" are="" rejected="" by="" the="" server="" with="" an="" `invalid_argument`="" error.="" filter="">[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. The maximum number of results to return. The service may return
    	// fewer than this value.
    	//
    	// If unspecified, at most 25 are returned.
    	//
    	// The maximum value is 100. If you use a value more than 100, it's
    	// automatically changed to 100.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token, received from the previous search messages call. Provide
    	// this parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. How the results list is ordered.
    	//
    	// Supported attributes to order by are:
    	//
    	//   - `create_time`: Sorts the results by the time of the message creation.
    	//     Default value.
    	//   - `relevance`: Sorts the results by relevance.
    	//     [Developer Preview](https://developers.google.com/workspace/preview).
    	//
    	// The default ordering is `create_time desc`. Only a single order per query
    	// (`create_time` or `relevance`) is supported. Only descending order (`desc`)
    	// is supported, and it must be specified after the order attribute.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// Optional. Specifies the desired output syntax for the Chat message
    	// `formatted_text` field.
    	MarkupSyntax MarkupSyntax `protobuf:"varint,6,opt,name=markup_syntax,json=markupSyntax,proto3,enum=google.chat.v1.MarkupSyntax" json:"markup_syntax,omitempty"`
    	// Optional. Specifies what kind of search results view to return. The default
    	// is `SEARCH_MESSAGES_VIEW_BASIC`.
    	View SearchMessagesRequest_SearchMessagesView `protobuf:"varint,7,opt,name=view,proto3,enum=google.chat.v1.SearchMessagesRequest_SearchMessagesView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for searching messages.

### func (*SearchMessagesRequest) Descriptor 
    
    
    func (*SearchMessagesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchMessagesRequest.ProtoReflect.Descriptor instead.

### func (*SearchMessagesRequest) GetFilter 
    
    
    func (x *SearchMessagesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*SearchMessagesRequest) GetMarkupSyntax 
    
    
    func (x *SearchMessagesRequest) GetMarkupSyntax() MarkupSyntax

### func (*SearchMessagesRequest) GetOrderBy 
    
    
    func (x *SearchMessagesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*SearchMessagesRequest) GetPageSize 
    
    
    func (x *SearchMessagesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchMessagesRequest) GetPageToken 
    
    
    func (x *SearchMessagesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchMessagesRequest) GetParent 
    
    
    func (x *SearchMessagesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*SearchMessagesRequest) GetView 
    
    
    func (x *SearchMessagesRequest) GetView() SearchMessagesRequest_SearchMessagesView

### func (*SearchMessagesRequest) ProtoMessage 
    
    
    func (*SearchMessagesRequest) ProtoMessage()

### func (*SearchMessagesRequest) ProtoReflect 
    
    
    func (x *SearchMessagesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchMessagesRequest) Reset 
    
    
    func (x *SearchMessagesRequest) Reset()

### func (*SearchMessagesRequest) String 
    
    
    func (x *SearchMessagesRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchMessagesRequest_SearchMessagesView
    
    
    type SearchMessagesRequest_SearchMessagesView [int32](https://pkg.go.dev/builtin#int32)

The kinds of view that are supported for partial search results.

### SearchMessagesRequest_SEARCH_MESSAGES_VIEW_UNSPECIFIED, SearchMessagesRequest_SEARCH_MESSAGES_VIEW_BASIC, SearchMessagesRequest_SEARCH_MESSAGES_VIEW_FULL
    
    
    const (
    	// The default / unset value.
    	// The API will default to the BASIC view.
    	SearchMessagesRequest_SEARCH_MESSAGES_VIEW_UNSPECIFIED SearchMessagesRequest_SearchMessagesView = 0
    	// Includes only the matched messages in the results, but no additional
    	// metadata. This is the default value.
    	SearchMessagesRequest_SEARCH_MESSAGES_VIEW_BASIC SearchMessagesRequest_SearchMessagesView = 1
    	// Includes everything in the results: the matched messages and additional
    	// metadata.
    	SearchMessagesRequest_SEARCH_MESSAGES_VIEW_FULL SearchMessagesRequest_SearchMessagesView = 2
    )

### func (SearchMessagesRequest_SearchMessagesView) Descriptor 
    
    
    func (SearchMessagesRequest_SearchMessagesView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SearchMessagesRequest_SearchMessagesView) Enum 
    
    
    func (x SearchMessagesRequest_SearchMessagesView) Enum() *SearchMessagesRequest_SearchMessagesView

### func (SearchMessagesRequest_SearchMessagesView) EnumDescriptor 
    
    
    func (SearchMessagesRequest_SearchMessagesView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchMessagesRequest_SearchMessagesView.Descriptor instead.

### func (SearchMessagesRequest_SearchMessagesView) Number 
    
    
    func (x SearchMessagesRequest_SearchMessagesView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SearchMessagesRequest_SearchMessagesView) String 
    
    
    func (x SearchMessagesRequest_SearchMessagesView) String() [string](https://pkg.go.dev/builtin#string)

### func (SearchMessagesRequest_SearchMessagesView) Type 
    
    
    func (SearchMessagesRequest_SearchMessagesView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SearchMessagesResponse
    
    
    type SearchMessagesResponse struct {
    
    	// The list of search results that matched the query.
    	Results []*SearchMessageResult `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
    	// A token that can be used to retrieve the next page. If this field is empty,
    	// there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for searching messages.

### func (*SearchMessagesResponse) Descriptor 
    
    
    func (*SearchMessagesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchMessagesResponse.ProtoReflect.Descriptor instead.

### func (*SearchMessagesResponse) GetNextPageToken 
    
    
    func (x *SearchMessagesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchMessagesResponse) GetResults 
    
    
    func (x *SearchMessagesResponse) GetResults() []*SearchMessageResult

### func (*SearchMessagesResponse) ProtoMessage 
    
    
    func (*SearchMessagesResponse) ProtoMessage()

### func (*SearchMessagesResponse) ProtoReflect 
    
    
    func (x *SearchMessagesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchMessagesResponse) Reset 
    
    
    func (x *SearchMessagesResponse) Reset()

### func (*SearchMessagesResponse) String 
    
    
    func (x *SearchMessagesResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchSpacesRequest
    
    
    type SearchSpacesRequest struct {
    
    	// When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires either the `chat.admin.spaces.readonly` or `chat.admin.spaces`
    	// [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// The maximum number of spaces to return. The service may return fewer than
    	// this value.
    	//
    	// If unspecified, at most 100 spaces are returned.
    	//
    	// The maximum value is 1000 when `useAdminAccess` is set to `true`.
    	// Otherwise, the maximum value is 100. If you use a value more than the
    	// maximum value, it's automatically changed to the maximum value.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token, received from the previous search spaces call. Provide this
    	// parameter to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided should match the call that
    	// provided the page token. Passing different values to the other parameters
    	// might lead to unexpected results.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Required. A search query.
    	//
    	// You can search by using the following parameters when `useAdminAccess`
    	// is set to `true`:
    	//
    	// - `create_time`
    	// - `customer`
    	// - `display_name`
    	// - `external_user_allowed`
    	// - `last_active_time`
    	// - `space_history_state`
    	// - `space_type`
    	//
    	// When `useAdminAccess` is set to `false`:
    	//
    	// - `display_name`
    	// - `external_user_allowed`
    	// - `space_type`
    	//
    	// `create_time` and `last_active_time` accept a timestamp in
    	// [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported
    	// comparison operators are: `=`, `<`, `="">`, `<=`, `="">=`.
    	//
    	// `customer` is required when `useAdminAccess` is set to `true`, and is
    	// used to indicate which customer to fetch spaces from.
    	// `customers/my_customer` is the only supported value.
    	//
    	// `display_name` only accepts the `HAS` (`:`) operator. The text to
    	// match is first tokenized into tokens and each token is prefix-matched
    	// case-insensitively and independently as a substring anywhere in the space's
    	// `display_name`. For example, `Fun Eve` matches `Fun event` or `The
    	// evening was fun`, but not `notFun event` or `even`. When `useAdminAccess`
    	// is set to `false`, `display_name` is required to retrieve meaningful
    	// results. Otherwise, the default behavior is to return an empty response.
    	//
    	// `external_user_allowed` accepts either `true` or `false`.
    	//
    	// `space_history_state` only accepts values from the [`historyState`]
    	// (https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState)
    	// field of a `space` resource.
    	//
    	// `space_type` is required and the only valid value is `SPACE`.
    	//
    	// Across different fields, only `AND` operators are supported. A valid
    	// example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid
    	// example is `space_type = "SPACE" OR display_name:"Hello"`.
    	//
    	// Among the same field,
    	// `space_type` doesn't support `AND` or `OR` operators.
    	// `display_name`, 'space_history_state', and 'external_user_allowed' only
    	// support `OR` operators.
    	// `last_active_time` and `create_time` support both `AND` and `OR` operators.
    	// `AND` can only be used to represent an interval, such as `last_active_time
    	// < "2022-01-01t00:00:00+00:00"="" and="" last_active_time="">
    	// "2023-01-01T00:00:00+00:00"`.
    	//
    	// The following example queries are valid when `useAdminAccess` is set to
    	// `true`:
    	//
    	// ```
    	// customer = "customers/my_customer" AND space_type = "SPACE"
    	//
    	// customer = "customers/my_customer" AND space_type = "SPACE" AND
    	// display_name:"Hello World"
    	//
    	// customer = "customers/my_customer" AND space_type = "SPACE" AND
    	// (last_active_time < "2020-01-01t00:00:00+00:00"="" or="" last_active_time="">
    	// "2022-01-01T00:00:00+00:00")
    	//
    	// customer = "customers/my_customer" AND space_type = "SPACE" AND
    	// (display_name:"Hello World" OR display_name:"Fun event") AND
    	// (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01t00:00:00+00:00")="" customer="customers/my_customer" and="" space_type="SPACE" and="" (create_time=""> "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01t00:00:00+00:00")="" and="" (external_user_allowed="true" )="" and="" (space_history_state="HISTORY_ON" or="" space_history_state="HISTORY_OFF" )="" ```="" the="" following="" example="" queries="" are="" valid="" when="" `useadminaccess`="" is="" set="" to="" `false`:="" ```="" display_name:"hello="" world"="" and="" space_type="SPACE" (display_name:"hello"="" or="" display_name:"fun")="" and="" space_type="SPACE" (external_user_allowed="true" and="" space_type="SPACE" )="" returns="" an="" empty="" response.="" (external_user_allowed="true" and="" display_name:"hello"="" and="" space_type="//" "space")="" ```="" the="" maximum="" query="" length="" is="" 1,000="" characters.="" invalid="" queries="" are="" rejected="" by="" the="" server="" with="" an="" `invalid_argument`="" error.="" query="">[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=query,proto3" json:"query,omitempty"`
    	// Optional. How the list of spaces is ordered.
    	//
    	// Supported attributes to order by are:
    	//
    	// - `membership_count.joined_direct_human_user_count` — Denotes the count of
    	// human users that have directly joined a space.
    	// - `last_active_time` — Denotes the time when last eligible item is added to
    	// any topic of this space.
    	// - `create_time` — Denotes the time of the space creation.
    	//
    	// When `useAdminAccess` is `false`, only `create_time` and `relevance` are
    	// supported for ordering. Only `DESC` is supported for these fields in
    	// non-admin searches.
    	//
    	// Valid ordering operation values are:
    	//
    	// - `ASC` for ascending. Default value.
    	//
    	// - `DESC` for descending.
    	//
    	// The supported syntax are when `useAdminAccess` is set to `true`:
    	//
    	// - `membership_count.joined_direct_human_user_count DESC`
    	// - `membership_count.joined_direct_human_user_count ASC`
    	// - `last_active_time DESC`
    	// - `last_active_time ASC`
    	// - `create_time DESC`
    	// - `create_time ASC`
    	//
    	// When `useAdminAccess` is set to `false`:
    	//
    	//   - `create_time DESC`
    	//   - `relevance DESC`
    	//     [Developer Preview](https://developers.google.com/workspace/preview).
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request to search for a list of spaces based on a query.

### func (*SearchSpacesRequest) Descriptor 
    
    
    func (*SearchSpacesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchSpacesRequest.ProtoReflect.Descriptor instead.

### func (*SearchSpacesRequest) GetOrderBy 
    
    
    func (x *SearchSpacesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*SearchSpacesRequest) GetPageSize 
    
    
    func (x *SearchSpacesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchSpacesRequest) GetPageToken 
    
    
    func (x *SearchSpacesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchSpacesRequest) GetQuery 
    
    
    func (x *SearchSpacesRequest) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SearchSpacesRequest) GetUseAdminAccess 
    
    
    func (x *SearchSpacesRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchSpacesRequest) ProtoMessage 
    
    
    func (*SearchSpacesRequest) ProtoMessage()

### func (*SearchSpacesRequest) ProtoReflect 
    
    
    func (x *SearchSpacesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchSpacesRequest) Reset 
    
    
    func (x *SearchSpacesRequest) Reset()

### func (*SearchSpacesRequest) String 
    
    
    func (x *SearchSpacesRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchSpacesResponse
    
    
    type SearchSpacesResponse struct {
    
    	// Deprecated: Please use the new `results` field instead.
    	// A page of the requested spaces. This field will be populated only when
    	// `useAdminAccess` is set to `true` and deprecated in favor of the new
    	// `results` field.
    	//
    	// Deprecated: Marked as deprecated in google/chat/v1/space.proto.
    	Spaces []*Space `protobuf:"bytes,1,rep,name=spaces,proto3" json:"spaces,omitempty"`
    	// A token that can be used to retrieve the next page. If this field is empty,
    	// there are no subsequent pages.
    	//
    	// Only populated when `useAdminAccess` is set to `true`.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// The total number of spaces that match the query, across all pages. If the
    	// result is over 10,000 spaces, this value is an estimate.
    	//
    	// Only populated when `useAdminAccess` is set to `true`.
    	TotalSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=total_size,json=totalSize,proto3" json:"total_size,omitempty"`
    	// Output only. The list of search results that matched the query.
    	Results []*SearchSpacesResponse_SearchSpaceResult `protobuf:"bytes,4,rep,name=results,proto3" json:"results,omitempty"`
    	// contains filtered or unexported fields
    }

Response with a list of spaces corresponding to the search spaces request.

### func (*SearchSpacesResponse) Descriptor 
    
    
    func (*SearchSpacesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchSpacesResponse.ProtoReflect.Descriptor instead.

### func (*SearchSpacesResponse) GetNextPageToken 
    
    
    func (x *SearchSpacesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchSpacesResponse) GetResults 
    
    
    func (x *SearchSpacesResponse) GetResults() []*SearchSpacesResponse_SearchSpaceResult

### func (*SearchSpacesResponse) GetSpaces 
    
    
    func (x *SearchSpacesResponse) GetSpaces() []*Space

Deprecated: Marked as deprecated in google/chat/v1/space.proto.

### func (*SearchSpacesResponse) GetTotalSize 
    
    
    func (x *SearchSpacesResponse) GetTotalSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchSpacesResponse) ProtoMessage 
    
    
    func (*SearchSpacesResponse) ProtoMessage()

### func (*SearchSpacesResponse) ProtoReflect 
    
    
    func (x *SearchSpacesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchSpacesResponse) Reset 
    
    
    func (x *SearchSpacesResponse) Reset()

### func (*SearchSpacesResponse) String 
    
    
    func (x *SearchSpacesResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchSpacesResponse_SearchSpaceResult
    
    
    type SearchSpacesResponse_SearchSpaceResult struct {
    
    	// Output only. The matched space.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// contains filtered or unexported fields
    }

A single result item from a space search.

### func (*SearchSpacesResponse_SearchSpaceResult) Descriptor 
    
    
    func (*SearchSpacesResponse_SearchSpaceResult) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchSpacesResponse_SearchSpaceResult.ProtoReflect.Descriptor instead.

### func (*SearchSpacesResponse_SearchSpaceResult) GetSpace 
    
    
    func (x *SearchSpacesResponse_SearchSpaceResult) GetSpace() *Space

### func (*SearchSpacesResponse_SearchSpaceResult) ProtoMessage 
    
    
    func (*SearchSpacesResponse_SearchSpaceResult) ProtoMessage()

### func (*SearchSpacesResponse_SearchSpaceResult) ProtoReflect 
    
    
    func (x *SearchSpacesResponse_SearchSpaceResult) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchSpacesResponse_SearchSpaceResult) Reset 
    
    
    func (x *SearchSpacesResponse_SearchSpaceResult) Reset()

### func (*SearchSpacesResponse_SearchSpaceResult) String 
    
    
    func (x *SearchSpacesResponse_SearchSpaceResult) String() [string](https://pkg.go.dev/builtin#string)

## Section
    
    
    type Section struct {
    
    	// Identifier. Resource name of the section.
    	//
    	// For system sections, the section ID is a constant string:
    	//
    	// - DEFAULT_DIRECT_MESSAGES: `users/{user}/sections/default-direct-messages`
    	// - DEFAULT_SPACES: `users/{user}/sections/default-spaces`
    	// - DEFAULT_APPS: `users/{user}/sections/default-apps`
    	//
    	// Format: `users/{user}/sections/{section}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The section's display name. Only populated for sections of type
    	// `CUSTOM_SECTION`. Supports up to 80 characters. Required when creating a
    	// `CUSTOM_SECTION`.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. The order of the section in relation to other sections.
    	// Sections with a lower `sort_order` value appear before sections with a
    	// higher value.
    	SortOrder [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=sort_order,json=sortOrder,proto3" json:"sort_order,omitempty"`
    	// Required. The type of the section.
    	Type Section_SectionType `protobuf:"varint,4,opt,name=type,proto3,enum=google.chat.v1.Section_SectionType" json:"type,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a [section](https://support.google.com/chat/answer/16059854) in Google Chat. Sections help users organize their spaces. There are two types of sections:

  1. **System Sections:** These are predefined sections managed by Google Chat.
         
         Their resource names are fixed, and they cannot be created, deleted, or
         have their `display_name` modified. Examples include:
         *   `users/{user}/sections/default-direct-messages`
         *   `users/{user}/sections/default-spaces`
         *   `users/{user}/sections/default-apps`
         

     1. **Custom Sections:** These are sections created and managed by the user. Creating a custom section using `CreateSection` **requires** a `display_name`. Custom sections can be updated using `UpdateSection` and deleted using `DeleteSection`.



### func (*Section) Descriptor 
    
    
    func (*Section) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Section.ProtoReflect.Descriptor instead.

### func (*Section) GetDisplayName 
    
    
    func (x *Section) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Section) GetName 
    
    
    func (x *Section) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Section) GetSortOrder 
    
    
    func (x *Section) GetSortOrder() [int32](https://pkg.go.dev/builtin#int32)

### func (*Section) GetType 
    
    
    func (x *Section) GetType() Section_SectionType

### func (*Section) ProtoMessage 
    
    
    func (*Section) ProtoMessage()

### func (*Section) ProtoReflect 
    
    
    func (x *Section) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Section) Reset 
    
    
    func (x *Section) Reset()

### func (*Section) String 
    
    
    func (x *Section) String() [string](https://pkg.go.dev/builtin#string)

## SectionItem
    
    
    type SectionItem struct {
    
    	// Identifier. The resource name of the section item.
    	//
    	// Format: `users/{user}/sections/{section}/items/{item}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The section item.
    	//
    	// Types that are valid to be assigned to Item:
    	//
    	//	*SectionItem_Space
    	Item isSectionItem_Item `protobuf_oneof:"item"`
    	// contains filtered or unexported fields
    }

A user's defined section item. This is used to represent section items, such as spaces, grouped under a section.

### func (*SectionItem) Descriptor 
    
    
    func (*SectionItem) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SectionItem.ProtoReflect.Descriptor instead.

### func (*SectionItem) GetItem 
    
    
    func (x *SectionItem) GetItem() isSectionItem_Item

### func (*SectionItem) GetName 
    
    
    func (x *SectionItem) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SectionItem) GetSpace 
    
    
    func (x *SectionItem) GetSpace() [string](https://pkg.go.dev/builtin#string)

### func (*SectionItem) ProtoMessage 
    
    
    func (*SectionItem) ProtoMessage()

### func (*SectionItem) ProtoReflect 
    
    
    func (x *SectionItem) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SectionItem) Reset 
    
    
    func (x *SectionItem) Reset()

### func (*SectionItem) String 
    
    
    func (x *SectionItem) String() [string](https://pkg.go.dev/builtin#string)

## SectionItem_Space
    
    
    type SectionItem_Space struct {
    	// Optional. The space resource name.
    	//
    	// Format: `spaces/{space}`
    	Space [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=space,proto3,oneof"`
    }

## Section_SectionType
    
    
    type Section_SectionType [int32](https://pkg.go.dev/builtin#int32)

Section types.

### Section_SECTION_TYPE_UNSPECIFIED, Section_CUSTOM_SECTION, Section_DEFAULT_DIRECT_MESSAGES, Section_DEFAULT_SPACES, Section_DEFAULT_APPS
    
    
    const (
    	// Unspecified section type.
    	Section_SECTION_TYPE_UNSPECIFIED Section_SectionType = 0
    	// Custom section.
    	Section_CUSTOM_SECTION Section_SectionType = 1
    	// Default section containing
    	// [DIRECT_MESSAGE](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#spacetype)
    	// between two human users or
    	// [GROUP_CHAT](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#spacetype)
    	// spaces that don't belong to any custom section.
    	Section_DEFAULT_DIRECT_MESSAGES Section_SectionType = 2
    	// Default spaces that don't belong to any custom section.
    	Section_DEFAULT_SPACES Section_SectionType = 3
    	// Default section containing a user's installed apps.
    	Section_DEFAULT_APPS Section_SectionType = 6
    )

### func (Section_SectionType) Descriptor 
    
    
    func (Section_SectionType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Section_SectionType) Enum 
    
    
    func (x Section_SectionType) Enum() *Section_SectionType

### func (Section_SectionType) EnumDescriptor 
    
    
    func (Section_SectionType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Section_SectionType.Descriptor instead.

### func (Section_SectionType) Number 
    
    
    func (x Section_SectionType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Section_SectionType) String 
    
    
    func (x Section_SectionType) String() [string](https://pkg.go.dev/builtin#string)

### func (Section_SectionType) Type 
    
    
    func (Section_SectionType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SetUpSpaceRequest
    
    
    type SetUpSpaceRequest struct {
    
    	// Required. The `Space.spaceType` field is required.
    	//
    	// To create a space, set `Space.spaceType` to `SPACE` and set
    	// `Space.displayName`. If you receive the error message `ALREADY_EXISTS` when
    	// setting up a space, try a different `displayName`. An existing space
    	// within the Google Workspace organization might already use this display
    	// name.
    	//
    	// To create a group chat, set `Space.spaceType` to
    	// `GROUP_CHAT`. Don't set `Space.displayName`.
    	//
    	// To create a 1:1 conversation between humans,
    	// set `Space.spaceType` to `DIRECT_MESSAGE` and set
    	// `Space.singleUserBotDm` to `false`. Don't set `Space.displayName` or
    	// `Space.spaceDetails`.
    	//
    	// To create an 1:1 conversation between a human and the calling Chat app, set
    	// `Space.spaceType` to `DIRECT_MESSAGE` and
    	// `Space.singleUserBotDm` to `true`. Don't set `Space.displayName` or
    	// `Space.spaceDetails`.
    	//
    	// If a `DIRECT_MESSAGE` space already exists, that space is returned instead
    	// of creating a new space.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// Optional. A unique ID for this request. A random UUID is recommended.
    	// Specifying a request ID makes the request idempotent, which ensures that
    	// multiple identical requests with the same request ID result in only a
    	// single space being created. Subsequent requests with the same request ID
    	// return the existing space and do not update the space, even if the
    	// requested details differ from the current state.
    	//
    	// To use this field effectively:
    	//
    	// - Ensure that subsequent requests are identical and use the same
    	// authentication credentials as the original request.
    	// - If a space was already created with the provided request ID, the request
    	// returns that space. Note that the returned space might not be fully
    	// populated; the API echoes the space in your request with the
    	// system-assigned resource name populated. To retrieve the latest metadata
    	// for the space, call `GetSpace`.
    	// - Reusing an existing request ID with a different authenticated user
    	// results in an error.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. The Google Chat users or groups to invite to join the space. Omit
    	// the calling user, as they are added automatically.
    	//
    	// The set currently allows up to 49 memberships (in addition to the caller).
    	//
    	// For human membership, the `Membership.member` field must contain a `user`
    	// with `name` populated (format: `users/{user}`) and `type` set to
    	// `User.Type.HUMAN`. You can only add human users when setting up a space
    	// (adding Chat apps is only supported for direct message setup with the
    	// calling app). You can also add members using the user's email as an alias
    	// for {user}. For example, the `user.name` can be `users/example@gmail.com`.
    	// To invite Gmail users or users from external Google Workspace domains,
    	// user's email must be used for `{user}`.
    	//
    	// For Google group membership, the `Membership.group_member` field must
    	// contain a `group` with `name` populated (format `groups/{group}`). You
    	// can only add Google groups when setting `Space.spaceType` to `SPACE`.
    	//
    	// Optional when setting `Space.spaceType` to `SPACE`.
    	//
    	// Required when setting `Space.spaceType` to `GROUP_CHAT`, along with at
    	// least two memberships.
    	//
    	// Required when setting `Space.spaceType` to `DIRECT_MESSAGE` with a human
    	// user, along with exactly one membership.
    	//
    	// Must be empty when creating a 1:1 conversation between a human and the
    	// calling Chat app (when setting `Space.spaceType` to
    	// `DIRECT_MESSAGE` and `Space.singleUserBotDm` to `true`).
    	Memberships []*Membership `protobuf:"bytes,4,rep,name=memberships,proto3" json:"memberships,omitempty"`
    	// contains filtered or unexported fields
    }

Request to create a space and add specified users to it.

### func (*SetUpSpaceRequest) Descriptor 
    
    
    func (*SetUpSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SetUpSpaceRequest.ProtoReflect.Descriptor instead.

### func (*SetUpSpaceRequest) GetMemberships 
    
    
    func (x *SetUpSpaceRequest) GetMemberships() []*Membership

### func (*SetUpSpaceRequest) GetRequestId 
    
    
    func (x *SetUpSpaceRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*SetUpSpaceRequest) GetSpace 
    
    
    func (x *SetUpSpaceRequest) GetSpace() *Space

### func (*SetUpSpaceRequest) ProtoMessage 
    
    
    func (*SetUpSpaceRequest) ProtoMessage()

### func (*SetUpSpaceRequest) ProtoReflect 
    
    
    func (x *SetUpSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SetUpSpaceRequest) Reset 
    
    
    func (x *SetUpSpaceRequest) Reset()

### func (*SetUpSpaceRequest) String 
    
    
    func (x *SetUpSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## SlashCommand
    
    
    type SlashCommand struct {
    
    	// The ID of the slash command.
    	CommandId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
    	// contains filtered or unexported fields
    }

Metadata about a [slash command](https://developers.google.com/workspace/chat/commands) in Google Chat.

### func (*SlashCommand) Descriptor 
    
    
    func (*SlashCommand) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SlashCommand.ProtoReflect.Descriptor instead.

### func (*SlashCommand) GetCommandId 
    
    
    func (x *SlashCommand) GetCommandId() [int64](https://pkg.go.dev/builtin#int64)

### func (*SlashCommand) ProtoMessage 
    
    
    func (*SlashCommand) ProtoMessage()

### func (*SlashCommand) ProtoReflect 
    
    
    func (x *SlashCommand) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SlashCommand) Reset 
    
    
    func (x *SlashCommand) Reset()

### func (*SlashCommand) String 
    
    
    func (x *SlashCommand) String() [string](https://pkg.go.dev/builtin#string)

## SlashCommandMetadata
    
    
    type SlashCommandMetadata struct {
    
    	// The Chat app whose command was invoked.
    	Bot *User `protobuf:"bytes,1,opt,name=bot,proto3" json:"bot,omitempty"`
    	// The type of slash command.
    	Type SlashCommandMetadata_Type `protobuf:"varint,2,opt,name=type,proto3,enum=google.chat.v1.SlashCommandMetadata_Type" json:"type,omitempty"`
    	// The name of the invoked slash command.
    	CommandName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=command_name,json=commandName,proto3" json:"command_name,omitempty"`
    	// The command ID of the invoked slash command.
    	CommandId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
    	// Indicates whether the slash command is for a dialog.
    	TriggersDialog [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=triggers_dialog,json=triggersDialog,proto3" json:"triggers_dialog,omitempty"`
    	// contains filtered or unexported fields
    }

Annotation metadata for slash commands (/).

### func (*SlashCommandMetadata) Descriptor 
    
    
    func (*SlashCommandMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SlashCommandMetadata.ProtoReflect.Descriptor instead.

### func (*SlashCommandMetadata) GetBot 
    
    
    func (x *SlashCommandMetadata) GetBot() *User

### func (*SlashCommandMetadata) GetCommandId 
    
    
    func (x *SlashCommandMetadata) GetCommandId() [int64](https://pkg.go.dev/builtin#int64)

### func (*SlashCommandMetadata) GetCommandName 
    
    
    func (x *SlashCommandMetadata) GetCommandName() [string](https://pkg.go.dev/builtin#string)

### func (*SlashCommandMetadata) GetTriggersDialog 
    
    
    func (x *SlashCommandMetadata) GetTriggersDialog() [bool](https://pkg.go.dev/builtin#bool)

### func (*SlashCommandMetadata) GetType 
    
    
    func (x *SlashCommandMetadata) GetType() SlashCommandMetadata_Type

### func (*SlashCommandMetadata) ProtoMessage 
    
    
    func (*SlashCommandMetadata) ProtoMessage()

### func (*SlashCommandMetadata) ProtoReflect 
    
    
    func (x *SlashCommandMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SlashCommandMetadata) Reset 
    
    
    func (x *SlashCommandMetadata) Reset()

### func (*SlashCommandMetadata) String 
    
    
    func (x *SlashCommandMetadata) String() [string](https://pkg.go.dev/builtin#string)

## SlashCommandMetadata_Type
    
    
    type SlashCommandMetadata_Type [int32](https://pkg.go.dev/builtin#int32)

### SlashCommandMetadata_TYPE_UNSPECIFIED, SlashCommandMetadata_ADD, SlashCommandMetadata_INVOKE
    
    
    const (
    	// Default value for the enum. Don't use.
    	SlashCommandMetadata_TYPE_UNSPECIFIED SlashCommandMetadata_Type = 0
    	// Add Chat app to space.
    	SlashCommandMetadata_ADD SlashCommandMetadata_Type = 1
    	// Invoke slash command in space.
    	SlashCommandMetadata_INVOKE SlashCommandMetadata_Type = 2
    )

### func (SlashCommandMetadata_Type) Descriptor 
    
    
    func (SlashCommandMetadata_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SlashCommandMetadata_Type) Enum 
    
    
    func (x SlashCommandMetadata_Type) Enum() *SlashCommandMetadata_Type

### func (SlashCommandMetadata_Type) EnumDescriptor 
    
    
    func (SlashCommandMetadata_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SlashCommandMetadata_Type.Descriptor instead.

### func (SlashCommandMetadata_Type) Number 
    
    
    func (x SlashCommandMetadata_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SlashCommandMetadata_Type) String 
    
    
    func (x SlashCommandMetadata_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (SlashCommandMetadata_Type) Type 
    
    
    func (SlashCommandMetadata_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space
    
    
    type Space struct {
    
    	// Identifier. Resource name of the space.
    	//
    	// Format: `spaces/{space}`
    	//
    	// Where `{space}` represents the system-assigned ID for the space. You can
    	// obtain the space ID by calling the
    	// [`spaces.list()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/list)
    	// method or from the space URL. For example, if the space URL
    	// is `https://mail.google.com/mail/u/0/#chat/space/AAAAAAAAA`, the space ID
    	// is `AAAAAAAAA`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Deprecated: Use `space_type` instead.
    	// The type of a space.
    	//
    	// Deprecated: Marked as deprecated in google/chat/v1/space.proto.
    	Type Space_Type `protobuf:"varint,2,opt,name=type,proto3,enum=google.chat.v1.Space_Type" json:"type,omitempty"`
    	// Optional. The type of space. Required when creating a space or updating the
    	// space type of a space. Output only for other usage.
    	SpaceType Space_SpaceType `protobuf:"varint,10,opt,name=space_type,json=spaceType,proto3,enum=google.chat.v1.Space_SpaceType" json:"space_type,omitempty"`
    	// Optional. Whether the space is a DM between a Chat app and a single
    	// human.
    	SingleUserBotDm [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=single_user_bot_dm,json=singleUserBotDm,proto3" json:"single_user_bot_dm,omitempty"`
    	// Output only. Deprecated: Use `spaceThreadingState` instead.
    	// Whether messages are threaded in this space.
    	//
    	// Deprecated: Marked as deprecated in google/chat/v1/space.proto.
    	Threaded [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=threaded,proto3" json:"threaded,omitempty"`
    	// Optional. The space's display name. Required when [creating a
    	// space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/create)
    	// with a `spaceType` of `SPACE`. If you receive the error message
    	// `ALREADY_EXISTS` when creating a space or updating the `displayName`, try a
    	// different `displayName`. An existing space within the Google Workspace
    	// organization might already use this display name.
    	//
    	// For direct messages, this field might be empty.
    	//
    	// Supports up to 128 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Optional. Immutable. Whether this space permits any Google Chat user as a
    	// member. Input when creating a space in a Google Workspace organization.
    	// Omit this field when creating spaces in the following conditions:
    	//
    	//   - The authenticated user uses a consumer account (unmanaged user
    	//     account). By default, a space created by a consumer account permits any
    	//     Google Chat user.
    	//
    	// For existing spaces, this field is output only.
    	ExternalUserAllowed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,8,opt,name=external_user_allowed,json=externalUserAllowed,proto3" json:"external_user_allowed,omitempty"`
    	// Output only. The threading state in the Chat space.
    	SpaceThreadingState Space_SpaceThreadingState `protobuf:"varint,9,opt,name=space_threading_state,json=spaceThreadingState,proto3,enum=google.chat.v1.Space_SpaceThreadingState" json:"space_threading_state,omitempty"`
    	// Optional. Details about the space including description and rules.
    	SpaceDetails *Space_SpaceDetails `protobuf:"bytes,11,opt,name=space_details,json=spaceDetails,proto3" json:"space_details,omitempty"`
    	// Optional. The message history state for messages and threads in this space.
    	SpaceHistoryState HistoryState `protobuf:"varint,13,opt,name=space_history_state,json=spaceHistoryState,proto3,enum=google.chat.v1.HistoryState" json:"space_history_state,omitempty"`
    	// Optional. Whether this space is created in `Import Mode` as part of a data
    	// migration into Google Workspace. While spaces are being imported, they
    	// aren't visible to users until the import is complete.
    	//
    	// Creating a space in `Import Mode`requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	ImportMode [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,16,opt,name=import_mode,json=importMode,proto3" json:"import_mode,omitempty"`
    	// Optional. Immutable. For spaces created in Chat, the time the space was
    	// created. This field is output only, except when used in import mode spaces.
    	//
    	// For import mode spaces, set this field to the historical timestamp at which
    	// the space was created in the source in order to preserve the original
    	// creation time.
    	//
    	// Only populated in the output when `spaceType` is `GROUP_CHAT` or `SPACE`.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,17,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Timestamp of the last message in the space.
    	LastActiveTime *timestamppb.Timestamp `protobuf:"bytes,18,opt,name=last_active_time,json=lastActiveTime,proto3" json:"last_active_time,omitempty"`
    	// Output only. For direct message (DM) spaces with a Chat app, whether the
    	// space was created by a Google Workspace administrator. Administrators can
    	// install and set up a direct message with a Chat app on behalf of users in
    	// their organization.
    	//
    	// To support admin install, your Chat app must feature direct messaging.
    	AdminInstalled [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,19,opt,name=admin_installed,json=adminInstalled,proto3" json:"admin_installed,omitempty"`
    	// Output only. The count of joined memberships grouped by member type.
    	// Populated when the `space_type` is `SPACE`, `DIRECT_MESSAGE` or
    	// `GROUP_CHAT`.
    	MembershipCount *Space_MembershipCount `protobuf:"bytes,20,opt,name=membership_count,json=membershipCount,proto3" json:"membership_count,omitempty"`
    	// Optional. Specifies the [access
    	// setting](https://support.google.com/chat/answer/11971020) of the space.
    	// Only populated when the `space_type` is `SPACE`.
    	AccessSettings *Space_AccessSettings `protobuf:"bytes,23,opt,name=access_settings,json=accessSettings,proto3" json:"access_settings,omitempty"`
    	// Optional. Immutable. The customer id of the domain of the space.
    	// Required only when creating a space with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// and `SpaceType` is `SPACE`, otherwise should not be set.
    	//
    	// In the format `customers/{customer}`, where `customer` is the `id` from the
    	// [Admin SDK customer
    	// resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers).
    	// Private apps can also use the `customers/my_customer` alias to create
    	// the space in the same Google Workspace organization as the app.
    	//
    	// This field isn't populated for direct messages (DMs) or when the space is
    	// created by non-Google Workspace users.
    	Customer *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,24,opt,name=customer,proto3,oneof" json:"customer,omitempty"`
    	// Output only. The URI for a user to access the space.
    	SpaceUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,25,opt,name=space_uri,json=spaceUri,proto3" json:"space_uri,omitempty"`
    	// Represents the [permission settings]
    	// (https://support.google.com/chat/answer/13340792) of a space. Only
    	// populated when the `space_type` is `SPACE`.
    	//
    	// Types that are valid to be assigned to SpacePermissionSettings:
    	//
    	//	*Space_PredefinedPermissionSettings_
    	//	*Space_PermissionSettings_
    	SpacePermissionSettings isSpace_SpacePermissionSettings `protobuf_oneof:"space_permission_settings"`
    	// Output only. The time when the space will be automatically deleted by the
    	// system if it remains in import mode.
    	//
    	// Each space created in import mode must exit this mode before this expire
    	// time using `spaces.completeImport`.
    	//
    	// This field is only populated for spaces that were created with import mode.
    	ImportModeExpireTime *timestamppb.Timestamp `protobuf:"bytes,28,opt,name=import_mode_expire_time,json=importModeExpireTime,proto3" json:"import_mode_expire_time,omitempty"`
    	// contains filtered or unexported fields
    }

A space in Google Chat. Spaces are conversations between two or more users or 1:1 messages between a user and a Chat app.

### func (*Space) Descriptor 
    
    
    func (*Space) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space.ProtoReflect.Descriptor instead.

### func (*Space) GetAccessSettings 
    
    
    func (x *Space) GetAccessSettings() *Space_AccessSettings

### func (*Space) GetAdminInstalled 
    
    
    func (x *Space) GetAdminInstalled() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space) GetCreateTime 
    
    
    func (x *Space) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Space) GetCustomer 
    
    
    func (x *Space) GetCustomer() [string](https://pkg.go.dev/builtin#string)

### func (*Space) GetDisplayName 
    
    
    func (x *Space) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Space) GetExternalUserAllowed 
    
    
    func (x *Space) GetExternalUserAllowed() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space) GetImportMode 
    
    
    func (x *Space) GetImportMode() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space) GetImportModeExpireTime 
    
    
    func (x *Space) GetImportModeExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Space) GetLastActiveTime 
    
    
    func (x *Space) GetLastActiveTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Space) GetMembershipCount 
    
    
    func (x *Space) GetMembershipCount() *Space_MembershipCount

### func (*Space) GetName 
    
    
    func (x *Space) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Space) GetPermissionSettings 
    
    
    func (x *Space) GetPermissionSettings() *Space_PermissionSettings

### func (*Space) GetPredefinedPermissionSettings 
    
    
    func (x *Space) GetPredefinedPermissionSettings() Space_PredefinedPermissionSettings

### func (*Space) GetSingleUserBotDm 
    
    
    func (x *Space) GetSingleUserBotDm() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space) GetSpaceDetails 
    
    
    func (x *Space) GetSpaceDetails() *Space_SpaceDetails

### func (*Space) GetSpaceHistoryState 
    
    
    func (x *Space) GetSpaceHistoryState() HistoryState

### func (*Space) GetSpacePermissionSettings 
    
    
    func (x *Space) GetSpacePermissionSettings() isSpace_SpacePermissionSettings

### func (*Space) GetSpaceThreadingState 
    
    
    func (x *Space) GetSpaceThreadingState() Space_SpaceThreadingState

### func (*Space) GetSpaceType 
    
    
    func (x *Space) GetSpaceType() Space_SpaceType

### func (*Space) GetSpaceUri 
    
    
    func (x *Space) GetSpaceUri() [string](https://pkg.go.dev/builtin#string)

### func (*Space) GetThreaded 
    
    
    func (x *Space) GetThreaded() [bool](https://pkg.go.dev/builtin#bool)

Deprecated: Marked as deprecated in google/chat/v1/space.proto.

### func (*Space) GetType 
    
    
    func (x *Space) GetType() Space_Type

Deprecated: Marked as deprecated in google/chat/v1/space.proto.

### func (*Space) ProtoMessage 
    
    
    func (*Space) ProtoMessage()

### func (*Space) ProtoReflect 
    
    
    func (x *Space) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space) Reset 
    
    
    func (x *Space) Reset()

### func (*Space) String 
    
    
    func (x *Space) String() [string](https://pkg.go.dev/builtin#string)

## SpaceBatchUpdatedEventData
    
    
    type SpaceBatchUpdatedEventData struct {
    
    	// A list of updated spaces.
    	Spaces []*SpaceUpdatedEventData `protobuf:"bytes,1,rep,name=spaces,proto3" json:"spaces,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for multiple updates to a space.

Event type: `google.workspace.chat.space.v1.batchUpdated`

### func (*SpaceBatchUpdatedEventData) Descriptor 
    
    
    func (*SpaceBatchUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceBatchUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*SpaceBatchUpdatedEventData) GetSpaces 
    
    
    func (x *SpaceBatchUpdatedEventData) GetSpaces() []*SpaceUpdatedEventData

### func (*SpaceBatchUpdatedEventData) ProtoMessage 
    
    
    func (*SpaceBatchUpdatedEventData) ProtoMessage()

### func (*SpaceBatchUpdatedEventData) ProtoReflect 
    
    
    func (x *SpaceBatchUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpaceBatchUpdatedEventData) Reset 
    
    
    func (x *SpaceBatchUpdatedEventData) Reset()

### func (*SpaceBatchUpdatedEventData) String 
    
    
    func (x *SpaceBatchUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## SpaceEvent
    
    
    type SpaceEvent struct {
    
    	// Resource name of the space event.
    	//
    	// Format: `spaces/{space}/spaceEvents/{spaceEvent}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Time when the event occurred.
    	EventTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=event_time,json=eventTime,proto3" json:"event_time,omitempty"`
    	// Type of space event. Each event type has a batch version, which
    	// represents multiple instances of the event type that occur in a short
    	// period of time. For `spaceEvents.list()` requests, omit batch event types
    	// in your query filter. By default, the server returns both event type and
    	// its batch version.
    	//
    	// Supported event types for
    	// [messages](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages):
    	//
    	//   - New message: `google.workspace.chat.message.v1.created`
    	//   - Updated message: `google.workspace.chat.message.v1.updated`
    	//   - Deleted message: `google.workspace.chat.message.v1.deleted`
    	//   - Multiple new messages: `google.workspace.chat.message.v1.batchCreated`
    	//   - Multiple updated messages:
    	//     `google.workspace.chat.message.v1.batchUpdated`
    	//   - Multiple deleted messages:
    	//     `google.workspace.chat.message.v1.batchDeleted`
    	//
    	// Supported event types for
    	// [memberships](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.members):
    	//
    	//   - New membership: `google.workspace.chat.membership.v1.created`
    	//   - Updated membership: `google.workspace.chat.membership.v1.updated`
    	//   - Deleted membership: `google.workspace.chat.membership.v1.deleted`
    	//   - Multiple new memberships:
    	//     `google.workspace.chat.membership.v1.batchCreated`
    	//   - Multiple updated memberships:
    	//     `google.workspace.chat.membership.v1.batchUpdated`
    	//   - Multiple deleted memberships:
    	//     `google.workspace.chat.membership.v1.batchDeleted`
    	//
    	// Supported event types for
    	// [reactions](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.reactions):
    	//
    	//   - New reaction: `google.workspace.chat.reaction.v1.created`
    	//   - Deleted reaction: `google.workspace.chat.reaction.v1.deleted`
    	//   - Multiple new reactions:
    	//     `google.workspace.chat.reaction.v1.batchCreated`
    	//   - Multiple deleted reactions:
    	//     `google.workspace.chat.reaction.v1.batchDeleted`
    	//
    	// Supported event types about the
    	// [space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces):
    	//
    	//   - Updated space: `google.workspace.chat.space.v1.updated`
    	//   - Multiple space updates: `google.workspace.chat.space.v1.batchUpdated`
    	EventType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=event_type,json=eventType,proto3" json:"event_type,omitempty"`
    	// Types that are valid to be assigned to Payload:
    	//
    	//	*SpaceEvent_MessageCreatedEventData
    	//	*SpaceEvent_MessageUpdatedEventData
    	//	*SpaceEvent_MessageDeletedEventData
    	//	*SpaceEvent_MessageBatchCreatedEventData
    	//	*SpaceEvent_MessageBatchUpdatedEventData
    	//	*SpaceEvent_MessageBatchDeletedEventData
    	//	*SpaceEvent_SpaceUpdatedEventData
    	//	*SpaceEvent_SpaceBatchUpdatedEventData
    	//	*SpaceEvent_MembershipCreatedEventData
    	//	*SpaceEvent_MembershipUpdatedEventData
    	//	*SpaceEvent_MembershipDeletedEventData
    	//	*SpaceEvent_MembershipBatchCreatedEventData
    	//	*SpaceEvent_MembershipBatchUpdatedEventData
    	//	*SpaceEvent_MembershipBatchDeletedEventData
    	//	*SpaceEvent_ReactionCreatedEventData
    	//	*SpaceEvent_ReactionDeletedEventData
    	//	*SpaceEvent_ReactionBatchCreatedEventData
    	//	*SpaceEvent_ReactionBatchDeletedEventData
    	Payload isSpaceEvent_Payload `protobuf_oneof:"payload"`
    	// contains filtered or unexported fields
    }

An event that represents a change or activity in a Google Chat space. To learn more, see [Work with events from Google Chat](https://developers.google.com/workspace/chat/events-overview).

### func (*SpaceEvent) Descriptor 
    
    
    func (*SpaceEvent) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceEvent.ProtoReflect.Descriptor instead.

### func (*SpaceEvent) GetEventTime 
    
    
    func (x *SpaceEvent) GetEventTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SpaceEvent) GetEventType 
    
    
    func (x *SpaceEvent) GetEventType() [string](https://pkg.go.dev/builtin#string)

### func (*SpaceEvent) GetMembershipBatchCreatedEventData 
    
    
    func (x *SpaceEvent) GetMembershipBatchCreatedEventData() *MembershipBatchCreatedEventData

### func (*SpaceEvent) GetMembershipBatchDeletedEventData 
    
    
    func (x *SpaceEvent) GetMembershipBatchDeletedEventData() *MembershipBatchDeletedEventData

### func (*SpaceEvent) GetMembershipBatchUpdatedEventData 
    
    
    func (x *SpaceEvent) GetMembershipBatchUpdatedEventData() *MembershipBatchUpdatedEventData

### func (*SpaceEvent) GetMembershipCreatedEventData 
    
    
    func (x *SpaceEvent) GetMembershipCreatedEventData() *MembershipCreatedEventData

### func (*SpaceEvent) GetMembershipDeletedEventData 
    
    
    func (x *SpaceEvent) GetMembershipDeletedEventData() *MembershipDeletedEventData

### func (*SpaceEvent) GetMembershipUpdatedEventData 
    
    
    func (x *SpaceEvent) GetMembershipUpdatedEventData() *MembershipUpdatedEventData

### func (*SpaceEvent) GetMessageBatchCreatedEventData 
    
    
    func (x *SpaceEvent) GetMessageBatchCreatedEventData() *MessageBatchCreatedEventData

### func (*SpaceEvent) GetMessageBatchDeletedEventData 
    
    
    func (x *SpaceEvent) GetMessageBatchDeletedEventData() *MessageBatchDeletedEventData

### func (*SpaceEvent) GetMessageBatchUpdatedEventData 
    
    
    func (x *SpaceEvent) GetMessageBatchUpdatedEventData() *MessageBatchUpdatedEventData

### func (*SpaceEvent) GetMessageCreatedEventData 
    
    
    func (x *SpaceEvent) GetMessageCreatedEventData() *MessageCreatedEventData

### func (*SpaceEvent) GetMessageDeletedEventData 
    
    
    func (x *SpaceEvent) GetMessageDeletedEventData() *MessageDeletedEventData

### func (*SpaceEvent) GetMessageUpdatedEventData 
    
    
    func (x *SpaceEvent) GetMessageUpdatedEventData() *MessageUpdatedEventData

### func (*SpaceEvent) GetName 
    
    
    func (x *SpaceEvent) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SpaceEvent) GetPayload 
    
    
    func (x *SpaceEvent) GetPayload() isSpaceEvent_Payload

### func (*SpaceEvent) GetReactionBatchCreatedEventData 
    
    
    func (x *SpaceEvent) GetReactionBatchCreatedEventData() *ReactionBatchCreatedEventData

### func (*SpaceEvent) GetReactionBatchDeletedEventData 
    
    
    func (x *SpaceEvent) GetReactionBatchDeletedEventData() *ReactionBatchDeletedEventData

### func (*SpaceEvent) GetReactionCreatedEventData 
    
    
    func (x *SpaceEvent) GetReactionCreatedEventData() *ReactionCreatedEventData

### func (*SpaceEvent) GetReactionDeletedEventData 
    
    
    func (x *SpaceEvent) GetReactionDeletedEventData() *ReactionDeletedEventData

### func (*SpaceEvent) GetSpaceBatchUpdatedEventData 
    
    
    func (x *SpaceEvent) GetSpaceBatchUpdatedEventData() *SpaceBatchUpdatedEventData

### func (*SpaceEvent) GetSpaceUpdatedEventData 
    
    
    func (x *SpaceEvent) GetSpaceUpdatedEventData() *SpaceUpdatedEventData

### func (*SpaceEvent) ProtoMessage 
    
    
    func (*SpaceEvent) ProtoMessage()

### func (*SpaceEvent) ProtoReflect 
    
    
    func (x *SpaceEvent) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpaceEvent) Reset 
    
    
    func (x *SpaceEvent) Reset()

### func (*SpaceEvent) String 
    
    
    func (x *SpaceEvent) String() [string](https://pkg.go.dev/builtin#string)

## SpaceEvent_MembershipBatchCreatedEventData
    
    
    type SpaceEvent_MembershipBatchCreatedEventData struct {
    	// Event payload for multiple new memberships.
    	//
    	// Event type: `google.workspace.chat.membership.v1.batchCreated`
    	MembershipBatchCreatedEventData *MembershipBatchCreatedEventData `protobuf:"bytes,31,opt,name=membership_batch_created_event_data,json=membershipBatchCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_MembershipBatchDeletedEventData
    
    
    type SpaceEvent_MembershipBatchDeletedEventData struct {
    	// Event payload for multiple deleted memberships.
    	//
    	// Event type: `google.workspace.chat.membership.v1.batchDeleted`
    	MembershipBatchDeletedEventData *MembershipBatchDeletedEventData `protobuf:"bytes,33,opt,name=membership_batch_deleted_event_data,json=membershipBatchDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_MembershipBatchUpdatedEventData
    
    
    type SpaceEvent_MembershipBatchUpdatedEventData struct {
    	// Event payload for multiple updated memberships.
    	//
    	// Event type: `google.workspace.chat.membership.v1.batchUpdated`
    	MembershipBatchUpdatedEventData *MembershipBatchUpdatedEventData `protobuf:"bytes,32,opt,name=membership_batch_updated_event_data,json=membershipBatchUpdatedEventData,proto3,oneof"`
    }

## SpaceEvent_MembershipCreatedEventData
    
    
    type SpaceEvent_MembershipCreatedEventData struct {
    	// Event payload for a new membership.
    	//
    	// Event type: `google.workspace.chat.membership.v1.created`
    	MembershipCreatedEventData *MembershipCreatedEventData `protobuf:"bytes,17,opt,name=membership_created_event_data,json=membershipCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_MembershipDeletedEventData
    
    
    type SpaceEvent_MembershipDeletedEventData struct {
    	// Event payload for a deleted membership.
    	//
    	// Event type: `google.workspace.chat.membership.v1.deleted`
    	MembershipDeletedEventData *MembershipDeletedEventData `protobuf:"bytes,219,opt,name=membership_deleted_event_data,json=membershipDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_MembershipUpdatedEventData
    
    
    type SpaceEvent_MembershipUpdatedEventData struct {
    	// Event payload for an updated membership.
    	//
    	// Event type: `google.workspace.chat.membership.v1.updated`
    	MembershipUpdatedEventData *MembershipUpdatedEventData `protobuf:"bytes,18,opt,name=membership_updated_event_data,json=membershipUpdatedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageBatchCreatedEventData
    
    
    type SpaceEvent_MessageBatchCreatedEventData struct {
    	// Event payload for multiple new messages.
    	//
    	// Event type: `google.workspace.chat.message.v1.batchCreated`
    	MessageBatchCreatedEventData *MessageBatchCreatedEventData `protobuf:"bytes,26,opt,name=message_batch_created_event_data,json=messageBatchCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageBatchDeletedEventData
    
    
    type SpaceEvent_MessageBatchDeletedEventData struct {
    	// Event payload for multiple deleted messages.
    	//
    	// Event type: `google.workspace.chat.message.v1.batchDeleted`
    	MessageBatchDeletedEventData *MessageBatchDeletedEventData `protobuf:"bytes,28,opt,name=message_batch_deleted_event_data,json=messageBatchDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageBatchUpdatedEventData
    
    
    type SpaceEvent_MessageBatchUpdatedEventData struct {
    	// Event payload for multiple updated messages.
    	//
    	// Event type: `google.workspace.chat.message.v1.batchUpdated`
    	MessageBatchUpdatedEventData *MessageBatchUpdatedEventData `protobuf:"bytes,27,opt,name=message_batch_updated_event_data,json=messageBatchUpdatedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageCreatedEventData
    
    
    type SpaceEvent_MessageCreatedEventData struct {
    	// Event payload for a new message.
    	//
    	// Event type: `google.workspace.chat.message.v1.created`
    	MessageCreatedEventData *MessageCreatedEventData `protobuf:"bytes,12,opt,name=message_created_event_data,json=messageCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageDeletedEventData
    
    
    type SpaceEvent_MessageDeletedEventData struct {
    	// Event payload for a deleted message.
    	//
    	// Event type: `google.workspace.chat.message.v1.deleted`
    	MessageDeletedEventData *MessageDeletedEventData `protobuf:"bytes,14,opt,name=message_deleted_event_data,json=messageDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_MessageUpdatedEventData
    
    
    type SpaceEvent_MessageUpdatedEventData struct {
    	// Event payload for an updated message.
    	//
    	// Event type: `google.workspace.chat.message.v1.updated`
    	MessageUpdatedEventData *MessageUpdatedEventData `protobuf:"bytes,13,opt,name=message_updated_event_data,json=messageUpdatedEventData,proto3,oneof"`
    }

## SpaceEvent_ReactionBatchCreatedEventData
    
    
    type SpaceEvent_ReactionBatchCreatedEventData struct {
    	// Event payload for multiple new reactions.
    	//
    	// Event type: `google.workspace.chat.reaction.v1.batchCreated`
    	ReactionBatchCreatedEventData *ReactionBatchCreatedEventData `protobuf:"bytes,34,opt,name=reaction_batch_created_event_data,json=reactionBatchCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_ReactionBatchDeletedEventData
    
    
    type SpaceEvent_ReactionBatchDeletedEventData struct {
    	// Event payload for multiple deleted reactions.
    	//
    	// Event type: `google.workspace.chat.reaction.v1.batchDeleted`
    	ReactionBatchDeletedEventData *ReactionBatchDeletedEventData `protobuf:"bytes,35,opt,name=reaction_batch_deleted_event_data,json=reactionBatchDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_ReactionCreatedEventData
    
    
    type SpaceEvent_ReactionCreatedEventData struct {
    	// Event payload for a new reaction.
    	//
    	// Event type: `google.workspace.chat.reaction.v1.created`
    	ReactionCreatedEventData *ReactionCreatedEventData `protobuf:"bytes,21,opt,name=reaction_created_event_data,json=reactionCreatedEventData,proto3,oneof"`
    }

## SpaceEvent_ReactionDeletedEventData
    
    
    type SpaceEvent_ReactionDeletedEventData struct {
    	// Event payload for a deleted reaction.
    	//
    	// Event type: `google.workspace.chat.reaction.v1.deleted`
    	ReactionDeletedEventData *ReactionDeletedEventData `protobuf:"bytes,22,opt,name=reaction_deleted_event_data,json=reactionDeletedEventData,proto3,oneof"`
    }

## SpaceEvent_SpaceBatchUpdatedEventData
    
    
    type SpaceEvent_SpaceBatchUpdatedEventData struct {
    	// Event payload for multiple updates to a space.
    	//
    	// Event type: `google.workspace.chat.space.v1.batchUpdated`
    	SpaceBatchUpdatedEventData *SpaceBatchUpdatedEventData `protobuf:"bytes,29,opt,name=space_batch_updated_event_data,json=spaceBatchUpdatedEventData,proto3,oneof"`
    }

## SpaceEvent_SpaceUpdatedEventData
    
    
    type SpaceEvent_SpaceUpdatedEventData struct {
    	// Event payload for a space update.
    	//
    	// Event type: `google.workspace.chat.space.v1.updated`
    	SpaceUpdatedEventData *SpaceUpdatedEventData `protobuf:"bytes,15,opt,name=space_updated_event_data,json=spaceUpdatedEventData,proto3,oneof"`
    }

## SpaceNotificationSetting
    
    
    type SpaceNotificationSetting struct {
    
    	// Identifier. The resource name of the space notification setting.
    	// Format: `users/{user}/spaces/{space}/spaceNotificationSetting`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The notification setting.
    	NotificationSetting *SpaceNotificationSetting_NotificationSetting `protobuf:"varint,2,opt,name=notification_setting,json=notificationSetting,proto3,enum=google.chat.v1.SpaceNotificationSetting_NotificationSetting,oneof" json:"notification_setting,omitempty"`
    	// The space notification mute setting.
    	MuteSetting *SpaceNotificationSetting_MuteSetting `protobuf:"varint,3,opt,name=mute_setting,json=muteSetting,proto3,enum=google.chat.v1.SpaceNotificationSetting_MuteSetting,oneof" json:"mute_setting,omitempty"`
    	// contains filtered or unexported fields
    }

The notification setting of a user in a space.

### func (*SpaceNotificationSetting) Descriptor 
    
    
    func (*SpaceNotificationSetting) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceNotificationSetting.ProtoReflect.Descriptor instead.

### func (*SpaceNotificationSetting) GetMuteSetting 
    
    
    func (x *SpaceNotificationSetting) GetMuteSetting() SpaceNotificationSetting_MuteSetting

### func (*SpaceNotificationSetting) GetName 
    
    
    func (x *SpaceNotificationSetting) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SpaceNotificationSetting) GetNotificationSetting 
    
    
    func (x *SpaceNotificationSetting) GetNotificationSetting() SpaceNotificationSetting_NotificationSetting

### func (*SpaceNotificationSetting) ProtoMessage 
    
    
    func (*SpaceNotificationSetting) ProtoMessage()

### func (*SpaceNotificationSetting) ProtoReflect 
    
    
    func (x *SpaceNotificationSetting) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpaceNotificationSetting) Reset 
    
    
    func (x *SpaceNotificationSetting) Reset()

### func (*SpaceNotificationSetting) String 
    
    
    func (x *SpaceNotificationSetting) String() [string](https://pkg.go.dev/builtin#string)

## SpaceNotificationSetting_MuteSetting
    
    
    type SpaceNotificationSetting_MuteSetting [int32](https://pkg.go.dev/builtin#int32)

The space notification mute setting types.

### SpaceNotificationSetting_MUTE_SETTING_UNSPECIFIED, SpaceNotificationSetting_UNMUTED, SpaceNotificationSetting_MUTED
    
    
    const (
    	// Reserved.
    	SpaceNotificationSetting_MUTE_SETTING_UNSPECIFIED SpaceNotificationSetting_MuteSetting = 0
    	// The user will receive notifications for the space based on the
    	// notification setting.
    	SpaceNotificationSetting_UNMUTED SpaceNotificationSetting_MuteSetting = 1
    	// The user will not receive any notifications for the space, regardless of
    	// the notification setting.
    	SpaceNotificationSetting_MUTED SpaceNotificationSetting_MuteSetting = 2
    )

### func (SpaceNotificationSetting_MuteSetting) Descriptor 
    
    
    func (SpaceNotificationSetting_MuteSetting) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SpaceNotificationSetting_MuteSetting) Enum 
    
    
    func (x SpaceNotificationSetting_MuteSetting) Enum() *SpaceNotificationSetting_MuteSetting

### func (SpaceNotificationSetting_MuteSetting) EnumDescriptor 
    
    
    func (SpaceNotificationSetting_MuteSetting) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceNotificationSetting_MuteSetting.Descriptor instead.

### func (SpaceNotificationSetting_MuteSetting) Number 
    
    
    func (x SpaceNotificationSetting_MuteSetting) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SpaceNotificationSetting_MuteSetting) String 
    
    
    func (x SpaceNotificationSetting_MuteSetting) String() [string](https://pkg.go.dev/builtin#string)

### func (SpaceNotificationSetting_MuteSetting) Type 
    
    
    func (SpaceNotificationSetting_MuteSetting) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SpaceNotificationSetting_NotificationSetting
    
    
    type SpaceNotificationSetting_NotificationSetting [int32](https://pkg.go.dev/builtin#int32)

The notification setting types. Other types might be supported in the future.

### SpaceNotificationSetting_NOTIFICATION_SETTING_UNSPECIFIED, SpaceNotificationSetting_ALL, SpaceNotificationSetting_MAIN_CONVERSATIONS, SpaceNotificationSetting_FOR_YOU, SpaceNotificationSetting_OFF
    
    
    const (
    	// Reserved.
    	SpaceNotificationSetting_NOTIFICATION_SETTING_UNSPECIFIED SpaceNotificationSetting_NotificationSetting = 0
    	// Notifications are triggered by @mentions, followed threads, first
    	// message of new threads. All new threads are automatically followed,
    	// unless manually unfollowed by the user.
    	SpaceNotificationSetting_ALL SpaceNotificationSetting_NotificationSetting = 1
    	// The notification is triggered by @mentions, followed threads, first
    	// message of new threads. Not available for 1:1 direct messages.
    	SpaceNotificationSetting_MAIN_CONVERSATIONS SpaceNotificationSetting_NotificationSetting = 2
    	// The notification is triggered by @mentions, followed threads. Not
    	// available for 1:1 direct messages.
    	SpaceNotificationSetting_FOR_YOU SpaceNotificationSetting_NotificationSetting = 3
    	// Notification is off.
    	SpaceNotificationSetting_OFF SpaceNotificationSetting_NotificationSetting = 4
    )

### func (SpaceNotificationSetting_NotificationSetting) Descriptor 
    
    
    func (SpaceNotificationSetting_NotificationSetting) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SpaceNotificationSetting_NotificationSetting) Enum 
    
    
    func (x SpaceNotificationSetting_NotificationSetting) Enum() *SpaceNotificationSetting_NotificationSetting

### func (SpaceNotificationSetting_NotificationSetting) EnumDescriptor 
    
    
    func (SpaceNotificationSetting_NotificationSetting) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceNotificationSetting_NotificationSetting.Descriptor instead.

### func (SpaceNotificationSetting_NotificationSetting) Number 
    
    
    func (x SpaceNotificationSetting_NotificationSetting) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SpaceNotificationSetting_NotificationSetting) String 
    
    
    func (x SpaceNotificationSetting_NotificationSetting) String() [string](https://pkg.go.dev/builtin#string)

### func (SpaceNotificationSetting_NotificationSetting) Type 
    
    
    func (SpaceNotificationSetting_NotificationSetting) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SpaceReadState
    
    
    type SpaceReadState struct {
    
    	// Resource name of the space read state.
    	//
    	// Format: `users/{user}/spaces/{space}/spaceReadState`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The time when the user's space read state was updated. Usually
    	// this corresponds with either the timestamp of the last read message, or a
    	// timestamp specified by the user to mark the last read position in a space.
    	LastReadTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=last_read_time,json=lastReadTime,proto3" json:"last_read_time,omitempty"`
    	// contains filtered or unexported fields
    }

A user's read state within a space, used to identify read and unread messages.

### func (*SpaceReadState) Descriptor 
    
    
    func (*SpaceReadState) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceReadState.ProtoReflect.Descriptor instead.

### func (*SpaceReadState) GetLastReadTime 
    
    
    func (x *SpaceReadState) GetLastReadTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SpaceReadState) GetName 
    
    
    func (x *SpaceReadState) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SpaceReadState) ProtoMessage 
    
    
    func (*SpaceReadState) ProtoMessage()

### func (*SpaceReadState) ProtoReflect 
    
    
    func (x *SpaceReadState) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpaceReadState) Reset 
    
    
    func (x *SpaceReadState) Reset()

### func (*SpaceReadState) String 
    
    
    func (x *SpaceReadState) String() [string](https://pkg.go.dev/builtin#string)

## SpaceUpdatedEventData
    
    
    type SpaceUpdatedEventData struct {
    
    	// The updated space.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// contains filtered or unexported fields
    }

Event payload for an updated space.

Event type: `google.workspace.chat.space.v1.updated`

### func (*SpaceUpdatedEventData) Descriptor 
    
    
    func (*SpaceUpdatedEventData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceUpdatedEventData.ProtoReflect.Descriptor instead.

### func (*SpaceUpdatedEventData) GetSpace 
    
    
    func (x *SpaceUpdatedEventData) GetSpace() *Space

### func (*SpaceUpdatedEventData) ProtoMessage 
    
    
    func (*SpaceUpdatedEventData) ProtoMessage()

### func (*SpaceUpdatedEventData) ProtoReflect 
    
    
    func (x *SpaceUpdatedEventData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpaceUpdatedEventData) Reset 
    
    
    func (x *SpaceUpdatedEventData) Reset()

### func (*SpaceUpdatedEventData) String 
    
    
    func (x *SpaceUpdatedEventData) String() [string](https://pkg.go.dev/builtin#string)

## SpaceView
    
    
    type SpaceView [int32](https://pkg.go.dev/builtin#int32)

A view that specifies which fields should be populated on the [`Space`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) resource. To ensure compatibility with future releases, we recommend that your code account for additional values.

### SpaceView_SPACE_VIEW_UNSPECIFIED, SpaceView_SPACE_VIEW_RESOURCE_NAME_ONLY, SpaceView_SPACE_VIEW_EXPANDED
    
    
    const (
    	// The default / unset value.
    	SpaceView_SPACE_VIEW_UNSPECIFIED SpaceView = 0
    	// Populates only the Space resource name.
    	SpaceView_SPACE_VIEW_RESOURCE_NAME_ONLY SpaceView = 3
    	// Populates Space resource fields.  Note: the `permissionSettings` field
    	// will not be populated.
    	// Requests that specify SPACE_VIEW_EXPANDED must include scopes that allow
    	// reading space data, for example,
    	// https://www.googleapis.com/auth/chat.spaces or
    	// https://www.googleapis.com/auth/chat.spaces.readonly.
    	SpaceView_SPACE_VIEW_EXPANDED SpaceView = 4
    )

### func (SpaceView) Descriptor 
    
    
    func (SpaceView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SpaceView) Enum 
    
    
    func (x SpaceView) Enum() *SpaceView

### func (SpaceView) EnumDescriptor 
    
    
    func (SpaceView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpaceView.Descriptor instead.

### func (SpaceView) Number 
    
    
    func (x SpaceView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SpaceView) String 
    
    
    func (x SpaceView) String() [string](https://pkg.go.dev/builtin#string)

### func (SpaceView) Type 
    
    
    func (SpaceView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space_AccessPermissionSetting
    
    
    type Space_AccessPermissionSetting struct {
    
    	// Optional. Unordered list. Allowed principals for this permission.
    	Principals []*Space_Principal `protobuf:"bytes,1,rep,name=principals,proto3" json:"principals,omitempty"`
    	// contains filtered or unexported fields
    }

An access permission setting.

### func (*Space_AccessPermissionSetting) Descriptor 
    
    
    func (*Space_AccessPermissionSetting) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_AccessPermissionSetting.ProtoReflect.Descriptor instead.

### func (*Space_AccessPermissionSetting) GetPrincipals 
    
    
    func (x *Space_AccessPermissionSetting) GetPrincipals() []*Space_Principal

### func (*Space_AccessPermissionSetting) ProtoMessage 
    
    
    func (*Space_AccessPermissionSetting) ProtoMessage()

### func (*Space_AccessPermissionSetting) ProtoReflect 
    
    
    func (x *Space_AccessPermissionSetting) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_AccessPermissionSetting) Reset 
    
    
    func (x *Space_AccessPermissionSetting) Reset()

### func (*Space_AccessPermissionSetting) String 
    
    
    func (x *Space_AccessPermissionSetting) String() [string](https://pkg.go.dev/builtin#string)

## Space_AccessPermissionSettings
    
    
    type Space_AccessPermissionSettings struct {
    
    	// Optional. Access permission setting for discovering the space.
    	DiscoverSpaceSetting *Space_AccessPermissionSetting `protobuf:"bytes,1,opt,name=discover_space_setting,json=discoverSpaceSetting,proto3" json:"discover_space_setting,omitempty"`
    	// Optional. Access permission setting for joining the space.
    	JoinSpaceSetting *Space_AccessPermissionSetting `protobuf:"bytes,2,opt,name=join_space_setting,json=joinSpaceSetting,proto3" json:"join_space_setting,omitempty"`
    	// Optional. Access permission setting for viewing space membership.
    	// Must be specified together with
    	// `PermissionSettings.view_space_membership` in the update mask and request
    	// body when updating who can view space membership. When granting view
    	// access to a target audience, you must also grant
    	// `PermissionSettings.view_space_membership` to all members in the same
    	// request. To remove an existing target audience (for example, to restrict
    	// view access to space managers or assistant managers only), specify an
    	// empty `AccessPermissionSetting` (with no `principals`).
    	ViewSpaceMembershipSetting *Space_AccessPermissionSetting `protobuf:"bytes,3,opt,name=view_space_membership_setting,json=viewSpaceMembershipSetting,proto3" json:"view_space_membership_setting,omitempty"`
    	// contains filtered or unexported fields
    }

Access permission settings for a space.

### func (*Space_AccessPermissionSettings) Descriptor 
    
    
    func (*Space_AccessPermissionSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_AccessPermissionSettings.ProtoReflect.Descriptor instead.

### func (*Space_AccessPermissionSettings) GetDiscoverSpaceSetting 
    
    
    func (x *Space_AccessPermissionSettings) GetDiscoverSpaceSetting() *Space_AccessPermissionSetting

### func (*Space_AccessPermissionSettings) GetJoinSpaceSetting 
    
    
    func (x *Space_AccessPermissionSettings) GetJoinSpaceSetting() *Space_AccessPermissionSetting

### func (*Space_AccessPermissionSettings) GetViewSpaceMembershipSetting 
    
    
    func (x *Space_AccessPermissionSettings) GetViewSpaceMembershipSetting() *Space_AccessPermissionSetting

### func (*Space_AccessPermissionSettings) ProtoMessage 
    
    
    func (*Space_AccessPermissionSettings) ProtoMessage()

### func (*Space_AccessPermissionSettings) ProtoReflect 
    
    
    func (x *Space_AccessPermissionSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_AccessPermissionSettings) Reset 
    
    
    func (x *Space_AccessPermissionSettings) Reset()

### func (*Space_AccessPermissionSettings) String 
    
    
    func (x *Space_AccessPermissionSettings) String() [string](https://pkg.go.dev/builtin#string)

## Space_AccessSettings
    
    
    type Space_AccessSettings struct {
    
    	// Output only. Indicates the access state of the space.
    	AccessState Space_AccessSettings_AccessState `protobuf:"varint,1,opt,name=access_state,json=accessState,proto3,enum=google.chat.v1.Space_AccessSettings_AccessState" json:"access_state,omitempty"`
    	// Optional. The resource name of the [target
    	// audience](https://support.google.com/a/answer/9934697) who can discover
    	// the space, join the space, and preview the messages in the space. If
    	// unset, only users or Google Groups who have been individually invited or
    	// added to the space can access it. For details, see [Make a space
    	// discoverable to a target
    	// audience](https://developers.google.com/workspace/chat/space-target-audience).
    	//
    	// Format: `audiences/{audience}`
    	//
    	// To use the default target audience for the Google Workspace organization,
    	// set to `audiences/default`.
    	//
    	// Reading the target audience supports:
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth)
    	// with the `chat.app.spaces` scope.
    	//
    	// This field is not populated when using the `chat.bot` scope with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    	//
    	// Setting the target audience requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	Audience [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=audience,proto3" json:"audience,omitempty"`
    	// Optional. Access permission settings for the space.
    	//
    	// To set the target audience when creating a space, specify the
    	// `accessSettings.audience` field in your request.
    	AccessPermissionSettings *Space_AccessPermissionSettings `protobuf:"bytes,5,opt,name=access_permission_settings,json=accessPermissionSettings,proto3" json:"access_permission_settings,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the [access setting](https://support.google.com/chat/answer/11971020) of the space.

### func (*Space_AccessSettings) Descriptor 
    
    
    func (*Space_AccessSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_AccessSettings.ProtoReflect.Descriptor instead.

### func (*Space_AccessSettings) GetAccessPermissionSettings 
    
    
    func (x *Space_AccessSettings) GetAccessPermissionSettings() *Space_AccessPermissionSettings

### func (*Space_AccessSettings) GetAccessState 
    
    
    func (x *Space_AccessSettings) GetAccessState() Space_AccessSettings_AccessState

### func (*Space_AccessSettings) GetAudience 
    
    
    func (x *Space_AccessSettings) GetAudience() [string](https://pkg.go.dev/builtin#string)

### func (*Space_AccessSettings) ProtoMessage 
    
    
    func (*Space_AccessSettings) ProtoMessage()

### func (*Space_AccessSettings) ProtoReflect 
    
    
    func (x *Space_AccessSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_AccessSettings) Reset 
    
    
    func (x *Space_AccessSettings) Reset()

### func (*Space_AccessSettings) String 
    
    
    func (x *Space_AccessSettings) String() [string](https://pkg.go.dev/builtin#string)

## Space_AccessSettings_AccessState
    
    
    type Space_AccessSettings_AccessState [int32](https://pkg.go.dev/builtin#int32)

Represents the access state of the space.

### Space_AccessSettings_ACCESS_STATE_UNSPECIFIED, Space_AccessSettings_PRIVATE, Space_AccessSettings_DISCOVERABLE
    
    
    const (
    	// Access state is unknown or not supported in this API.
    	Space_AccessSettings_ACCESS_STATE_UNSPECIFIED Space_AccessSettings_AccessState = 0
    	// Only users or Google Groups that have been individually added or
    	// invited by other users or Google Workspace administrators can discover
    	// and access the space.
    	Space_AccessSettings_PRIVATE Space_AccessSettings_AccessState = 1
    	// A space manager has granted a target audience access to
    	// the space. Users or Google Groups that have been individually added or
    	// invited to the space can also discover and access the space. To learn
    	// more, see [Make a space discoverable to specific
    	// users](https://developers.google.com/workspace/chat/space-target-audience).
    	//
    	// Creating discoverable spaces requires [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).
    	Space_AccessSettings_DISCOVERABLE Space_AccessSettings_AccessState = 2
    )

### func (Space_AccessSettings_AccessState) Descriptor 
    
    
    func (Space_AccessSettings_AccessState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Space_AccessSettings_AccessState) Enum 
    
    
    func (x Space_AccessSettings_AccessState) Enum() *Space_AccessSettings_AccessState

### func (Space_AccessSettings_AccessState) EnumDescriptor 
    
    
    func (Space_AccessSettings_AccessState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_AccessSettings_AccessState.Descriptor instead.

### func (Space_AccessSettings_AccessState) Number 
    
    
    func (x Space_AccessSettings_AccessState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Space_AccessSettings_AccessState) String 
    
    
    func (x Space_AccessSettings_AccessState) String() [string](https://pkg.go.dev/builtin#string)

### func (Space_AccessSettings_AccessState) Type 
    
    
    func (Space_AccessSettings_AccessState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space_MembershipCount
    
    
    type Space_MembershipCount struct {
    
    	// Output only. Count of human users that have directly joined the space,
    	// not counting users joined by having membership in a joined group.
    	JoinedDirectHumanUserCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=joined_direct_human_user_count,json=joinedDirectHumanUserCount,proto3" json:"joined_direct_human_user_count,omitempty"`
    	// Output only. Count of all groups that have directly joined the space.
    	JoinedGroupCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=joined_group_count,json=joinedGroupCount,proto3" json:"joined_group_count,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the count of memberships of a space, grouped into categories.

### func (*Space_MembershipCount) Descriptor 
    
    
    func (*Space_MembershipCount) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_MembershipCount.ProtoReflect.Descriptor instead.

### func (*Space_MembershipCount) GetJoinedDirectHumanUserCount 
    
    
    func (x *Space_MembershipCount) GetJoinedDirectHumanUserCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Space_MembershipCount) GetJoinedGroupCount 
    
    
    func (x *Space_MembershipCount) GetJoinedGroupCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Space_MembershipCount) ProtoMessage 
    
    
    func (*Space_MembershipCount) ProtoMessage()

### func (*Space_MembershipCount) ProtoReflect 
    
    
    func (x *Space_MembershipCount) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_MembershipCount) Reset 
    
    
    func (x *Space_MembershipCount) Reset()

### func (*Space_MembershipCount) String 
    
    
    func (x *Space_MembershipCount) String() [string](https://pkg.go.dev/builtin#string)

## Space_PermissionSetting
    
    
    type Space_PermissionSetting struct {
    
    	// Optional. Whether space owners
    	// ([`ROLE_MANAGER`][google.chat.v1.Membership.MembershipRole.ROLE_MANAGER])
    	// have this permission.
    	ManagersAllowed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=managers_allowed,json=managersAllowed,proto3" json:"managers_allowed,omitempty"`
    	// Optional. Whether space managers
    	// [`ROLE_ASSISTANT_MANAGER`][google.chat.v1.Membership.MembershipRole.ROLE_ASSISTANT_MANAGER])
    	// have this permission.
    	AssistantManagersAllowed *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=assistant_managers_allowed,json=assistantManagersAllowed,proto3,oneof" json:"assistant_managers_allowed,omitempty"`
    	// Optional. Whether basic space members
    	// ([`ROLE_MEMBER`][google.chat.v1.Membership.MembershipRole.ROLE_MEMBER])
    	// have this permission.
    	MembersAllowed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=members_allowed,json=membersAllowed,proto3" json:"members_allowed,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a space permission setting.

### func (*Space_PermissionSetting) Descriptor 
    
    
    func (*Space_PermissionSetting) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_PermissionSetting.ProtoReflect.Descriptor instead.

### func (*Space_PermissionSetting) GetAssistantManagersAllowed 
    
    
    func (x *Space_PermissionSetting) GetAssistantManagersAllowed() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space_PermissionSetting) GetManagersAllowed 
    
    
    func (x *Space_PermissionSetting) GetManagersAllowed() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space_PermissionSetting) GetMembersAllowed 
    
    
    func (x *Space_PermissionSetting) GetMembersAllowed() [bool](https://pkg.go.dev/builtin#bool)

### func (*Space_PermissionSetting) ProtoMessage 
    
    
    func (*Space_PermissionSetting) ProtoMessage()

### func (*Space_PermissionSetting) ProtoReflect 
    
    
    func (x *Space_PermissionSetting) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_PermissionSetting) Reset 
    
    
    func (x *Space_PermissionSetting) Reset()

### func (*Space_PermissionSetting) String 
    
    
    func (x *Space_PermissionSetting) String() [string](https://pkg.go.dev/builtin#string)

## Space_PermissionSettings
    
    
    type Space_PermissionSettings struct {
    
    	// Optional. Setting for managing members and groups in a space.
    	ManageMembersAndGroups *Space_PermissionSetting `protobuf:"bytes,1,opt,name=manage_members_and_groups,json=manageMembersAndGroups,proto3,oneof" json:"manage_members_and_groups,omitempty"`
    	// Optional. Setting for updating space name, avatar, description and
    	// guidelines.
    	ModifySpaceDetails *Space_PermissionSetting `protobuf:"bytes,2,opt,name=modify_space_details,json=modifySpaceDetails,proto3,oneof" json:"modify_space_details,omitempty"`
    	// Optional. Setting for toggling space history on and off.
    	ToggleHistory *Space_PermissionSetting `protobuf:"bytes,3,opt,name=toggle_history,json=toggleHistory,proto3,oneof" json:"toggle_history,omitempty"`
    	// Optional. Setting for using @all in a space.
    	UseAtMentionAll *Space_PermissionSetting `protobuf:"bytes,4,opt,name=use_at_mention_all,json=useAtMentionAll,proto3,oneof" json:"use_at_mention_all,omitempty"`
    	// Optional. Setting for managing apps in a space.
    	ManageApps *Space_PermissionSetting `protobuf:"bytes,5,opt,name=manage_apps,json=manageApps,proto3,oneof" json:"manage_apps,omitempty"`
    	// Optional. Setting for managing webhooks in a space.
    	ManageWebhooks *Space_PermissionSetting `protobuf:"bytes,6,opt,name=manage_webhooks,json=manageWebhooks,proto3,oneof" json:"manage_webhooks,omitempty"`
    	// Output only. Setting for posting messages in a space.
    	PostMessages *Space_PermissionSetting `protobuf:"bytes,7,opt,name=post_messages,json=postMessages,proto3,oneof" json:"post_messages,omitempty"`
    	// Optional. Setting for replying to messages in a space.
    	ReplyMessages *Space_PermissionSetting `protobuf:"bytes,8,opt,name=reply_messages,json=replyMessages,proto3,oneof" json:"reply_messages,omitempty"`
    	// Optional. Setting for viewing space membership.
    	// Must be specified together with
    	// `AccessPermissionSettings.view_space_membership_setting` in the update
    	// mask and request body when updating who can view space membership.
    	// When restricting view access to specific roles (for example, space
    	// managers or assistant managers only), specify the desired role
    	// permissions here and provide an empty
    	// `AccessPermissionSettings.view_space_membership_setting` in the same
    	// request. If a target audience is configured in
    	// `AccessPermissionSettings.view_space_membership_setting`, this setting
    	// must be granted to all members.
    	ViewSpaceMembership *Space_PermissionSetting `protobuf:"bytes,9,opt,name=view_space_membership,json=viewSpaceMembership,proto3,oneof" json:"view_space_membership,omitempty"`
    	// contains filtered or unexported fields
    }

[Permission settings](https://support.google.com/chat/answer/13340792) that you can specify when updating an existing named space.

To set permission settings when creating a space, specify the `PredefinedPermissionSettings` field in your request.

### func (*Space_PermissionSettings) Descriptor 
    
    
    func (*Space_PermissionSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_PermissionSettings.ProtoReflect.Descriptor instead.

### func (*Space_PermissionSettings) GetManageApps 
    
    
    func (x *Space_PermissionSettings) GetManageApps() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetManageMembersAndGroups 
    
    
    func (x *Space_PermissionSettings) GetManageMembersAndGroups() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetManageWebhooks 
    
    
    func (x *Space_PermissionSettings) GetManageWebhooks() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetModifySpaceDetails 
    
    
    func (x *Space_PermissionSettings) GetModifySpaceDetails() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetPostMessages 
    
    
    func (x *Space_PermissionSettings) GetPostMessages() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetReplyMessages 
    
    
    func (x *Space_PermissionSettings) GetReplyMessages() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetToggleHistory 
    
    
    func (x *Space_PermissionSettings) GetToggleHistory() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetUseAtMentionAll 
    
    
    func (x *Space_PermissionSettings) GetUseAtMentionAll() *Space_PermissionSetting

### func (*Space_PermissionSettings) GetViewSpaceMembership 
    
    
    func (x *Space_PermissionSettings) GetViewSpaceMembership() *Space_PermissionSetting

### func (*Space_PermissionSettings) ProtoMessage 
    
    
    func (*Space_PermissionSettings) ProtoMessage()

### func (*Space_PermissionSettings) ProtoReflect 
    
    
    func (x *Space_PermissionSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_PermissionSettings) Reset 
    
    
    func (x *Space_PermissionSettings) Reset()

### func (*Space_PermissionSettings) String 
    
    
    func (x *Space_PermissionSettings) String() [string](https://pkg.go.dev/builtin#string)

## Space_PermissionSettings_
    
    
    type Space_PermissionSettings_ struct {
    	// Optional. Space permission settings for existing spaces. Input for
    	// updating exact space permission settings, where existing permission
    	// settings are replaced. Output lists current permission settings.
    	//
    	// Reading and updating permission settings supports:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) with the
    	// `chat.app.spaces` scope. Only populated and settable when the Chat app
    	// created the space.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	PermissionSettings *Space_PermissionSettings `protobuf:"bytes,27,opt,name=permission_settings,json=permissionSettings,proto3,oneof"`
    }

## Space_PredefinedPermissionSettings
    
    
    type Space_PredefinedPermissionSettings [int32](https://pkg.go.dev/builtin#int32)

Predefined permission settings that you can only specify when creating a named space. More settings might be added in the future. For details about permission settings for named spaces, see [Learn about spaces](https://support.google.com/chat/answer/7659784).

### Space_PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED, Space_COLLABORATION_SPACE, Space_ANNOUNCEMENT_SPACE
    
    
    const (
    	// Unspecified. Don't use.
    	Space_PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED Space_PredefinedPermissionSettings = 0
    	// Setting to make the space a collaboration space where all members can
    	// post messages.
    	Space_COLLABORATION_SPACE Space_PredefinedPermissionSettings = 1
    	// Setting to make the space an announcement space where only space managers
    	// can post messages.
    	Space_ANNOUNCEMENT_SPACE Space_PredefinedPermissionSettings = 2
    )

### func (Space_PredefinedPermissionSettings) Descriptor 
    
    
    func (Space_PredefinedPermissionSettings) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Space_PredefinedPermissionSettings) Enum 
    
    
    func (x Space_PredefinedPermissionSettings) Enum() *Space_PredefinedPermissionSettings

### func (Space_PredefinedPermissionSettings) EnumDescriptor 
    
    
    func (Space_PredefinedPermissionSettings) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_PredefinedPermissionSettings.Descriptor instead.

### func (Space_PredefinedPermissionSettings) Number 
    
    
    func (x Space_PredefinedPermissionSettings) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Space_PredefinedPermissionSettings) String 
    
    
    func (x Space_PredefinedPermissionSettings) String() [string](https://pkg.go.dev/builtin#string)

### func (Space_PredefinedPermissionSettings) Type 
    
    
    func (Space_PredefinedPermissionSettings) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space_PredefinedPermissionSettings_
    
    
    type Space_PredefinedPermissionSettings_ struct {
    	// Optional. Input only. Predefined space permission settings, input only
    	// when creating a space. If the field is not set, a collaboration space is
    	// created. After you create the space, settings are populated in the
    	// `PermissionSettings` field.
    	//
    	// Setting predefined permission settings supports:
    	//
    	// - [App
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app)
    	// with [administrator
    	// approval](https://support.google.com/a?p=chat-app-auth) with the
    	// `chat.app.spaces` or `chat.app.spaces.create` scopes.
    	//
    	// - [User
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
    	PredefinedPermissionSettings Space_PredefinedPermissionSettings `protobuf:"varint,26,opt,name=predefined_permission_settings,json=predefinedPermissionSettings,proto3,enum=google.chat.v1.Space_PredefinedPermissionSettings,oneof"`
    }

## Space_Principal
    
    
    type Space_Principal struct {
    
    	// The type of principal.
    	//
    	// Types that are valid to be assigned to PrincipalType:
    	//
    	//	*Space_Principal_Audience
    	PrincipalType isSpace_Principal_PrincipalType `protobuf_oneof:"principal_type"`
    	// contains filtered or unexported fields
    }

A principal representing an entity granted access.

### func (*Space_Principal) Descriptor 
    
    
    func (*Space_Principal) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_Principal.ProtoReflect.Descriptor instead.

### func (*Space_Principal) GetAudience 
    
    
    func (x *Space_Principal) GetAudience() *Audience

### func (*Space_Principal) GetPrincipalType 
    
    
    func (x *Space_Principal) GetPrincipalType() isSpace_Principal_PrincipalType

### func (*Space_Principal) ProtoMessage 
    
    
    func (*Space_Principal) ProtoMessage()

### func (*Space_Principal) ProtoReflect 
    
    
    func (x *Space_Principal) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_Principal) Reset 
    
    
    func (x *Space_Principal) Reset()

### func (*Space_Principal) String 
    
    
    func (x *Space_Principal) String() [string](https://pkg.go.dev/builtin#string)

## Space_Principal_Audience
    
    
    type Space_Principal_Audience struct {
    	// An audience.
    	Audience *Audience `protobuf:"bytes,1,opt,name=audience,proto3,oneof"`
    }

## Space_SpaceDetails
    
    
    type Space_SpaceDetails struct {
    
    	// Optional. A description of the space. For example, describe the space's
    	// discussion topic, functional purpose, or participants.
    	//
    	// Supports up to 150 characters.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=description,proto3" json:"description,omitempty"`
    	// Optional. The space's rules, expectations, and etiquette.
    	//
    	// Supports up to 5,000 characters.
    	Guidelines [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=guidelines,proto3" json:"guidelines,omitempty"`
    	// contains filtered or unexported fields
    }

Details about the space including description and rules.

### func (*Space_SpaceDetails) Descriptor 
    
    
    func (*Space_SpaceDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_SpaceDetails.ProtoReflect.Descriptor instead.

### func (*Space_SpaceDetails) GetDescription 
    
    
    func (x *Space_SpaceDetails) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Space_SpaceDetails) GetGuidelines 
    
    
    func (x *Space_SpaceDetails) GetGuidelines() [string](https://pkg.go.dev/builtin#string)

### func (*Space_SpaceDetails) ProtoMessage 
    
    
    func (*Space_SpaceDetails) ProtoMessage()

### func (*Space_SpaceDetails) ProtoReflect 
    
    
    func (x *Space_SpaceDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Space_SpaceDetails) Reset 
    
    
    func (x *Space_SpaceDetails) Reset()

### func (*Space_SpaceDetails) String 
    
    
    func (x *Space_SpaceDetails) String() [string](https://pkg.go.dev/builtin#string)

## Space_SpaceThreadingState
    
    
    type Space_SpaceThreadingState [int32](https://pkg.go.dev/builtin#int32)

Specifies the type of threading state in the Chat space.

### Space_SPACE_THREADING_STATE_UNSPECIFIED, Space_THREADED_MESSAGES, Space_GROUPED_MESSAGES, Space_UNTHREADED_MESSAGES
    
    
    const (
    	// Reserved.
    	Space_SPACE_THREADING_STATE_UNSPECIFIED Space_SpaceThreadingState = 0
    	// Spaces that support message threads. When users respond to a message,
    	// they can reply in-thread, which keeps their response in the context of
    	// the original message.
    	Space_THREADED_MESSAGES Space_SpaceThreadingState = 2
    	// Named spaces where the conversation is organized by topic. Topics and
    	// their replies are grouped together.
    	Space_GROUPED_MESSAGES Space_SpaceThreadingState = 3
    	// Spaces that don't support message threading. This space threading state
    	// is only used for special cases including:
    	//
    	// * Continuous meeting chat where threading is intentionally turned off.
    	// * Legacy group conversations that were created prior to 2022.
    	Space_UNTHREADED_MESSAGES Space_SpaceThreadingState = 4
    )

### func (Space_SpaceThreadingState) Descriptor 
    
    
    func (Space_SpaceThreadingState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Space_SpaceThreadingState) Enum 
    
    
    func (x Space_SpaceThreadingState) Enum() *Space_SpaceThreadingState

### func (Space_SpaceThreadingState) EnumDescriptor 
    
    
    func (Space_SpaceThreadingState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_SpaceThreadingState.Descriptor instead.

### func (Space_SpaceThreadingState) Number 
    
    
    func (x Space_SpaceThreadingState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Space_SpaceThreadingState) String 
    
    
    func (x Space_SpaceThreadingState) String() [string](https://pkg.go.dev/builtin#string)

### func (Space_SpaceThreadingState) Type 
    
    
    func (Space_SpaceThreadingState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space_SpaceType
    
    
    type Space_SpaceType [int32](https://pkg.go.dev/builtin#int32)

The type of space. Required when creating or updating a space. Output only for other usage.

### Space_SPACE_TYPE_UNSPECIFIED, Space_SPACE, Space_GROUP_CHAT, Space_DIRECT_MESSAGE
    
    
    const (
    	// Reserved.
    	Space_SPACE_TYPE_UNSPECIFIED Space_SpaceType = 0
    	// A place where people send messages, share files, and collaborate.
    	// A `SPACE` can include Chat apps.
    	Space_SPACE Space_SpaceType = 1
    	// Group conversations between 3 or more people.
    	// A `GROUP_CHAT` can include Chat apps.
    	Space_GROUP_CHAT Space_SpaceType = 2
    	// 1:1 messages between two humans or a human and a Chat app.
    	Space_DIRECT_MESSAGE Space_SpaceType = 3
    )

### func (Space_SpaceType) Descriptor 
    
    
    func (Space_SpaceType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Space_SpaceType) Enum 
    
    
    func (x Space_SpaceType) Enum() *Space_SpaceType

### func (Space_SpaceType) EnumDescriptor 
    
    
    func (Space_SpaceType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_SpaceType.Descriptor instead.

### func (Space_SpaceType) Number 
    
    
    func (x Space_SpaceType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Space_SpaceType) String 
    
    
    func (x Space_SpaceType) String() [string](https://pkg.go.dev/builtin#string)

### func (Space_SpaceType) Type 
    
    
    func (Space_SpaceType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Space_Type
    
    
    type Space_Type [int32](https://pkg.go.dev/builtin#int32)

Deprecated: Use `SpaceType` instead.

### Space_TYPE_UNSPECIFIED, Space_ROOM, Space_DM
    
    
    const (
    	// Reserved.
    	Space_TYPE_UNSPECIFIED Space_Type = 0
    	// Conversations between two or more humans.
    	Space_ROOM Space_Type = 1
    	// 1:1 Direct Message between a human and a Chat app, where all messages are
    	// flat. Note that this doesn't include direct messages between two humans.
    	Space_DM Space_Type = 2
    )

### func (Space_Type) Descriptor 
    
    
    func (Space_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Space_Type) Enum 
    
    
    func (x Space_Type) Enum() *Space_Type

### func (Space_Type) EnumDescriptor 
    
    
    func (Space_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Space_Type.Descriptor instead.

### func (Space_Type) Number 
    
    
    func (x Space_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Space_Type) String 
    
    
    func (x Space_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (Space_Type) Type 
    
    
    func (Space_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Thread
    
    
    type Thread struct {
    
    	// Identifier. Resource name of the thread.
    	//
    	// Example: `spaces/{space}/threads/{thread}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Input for creating or updating a thread. Otherwise, output only.
    	// ID for the thread. Supports up to 4000 characters.
    	//
    	// This ID is unique to the Chat app that sets it. For example, if
    	// multiple Chat apps create a message using the same thread key,
    	// the messages are posted in different threads. To reply in a
    	// thread created by a person or another Chat app, specify the thread `name`
    	// field instead.
    	ThreadKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=thread_key,json=threadKey,proto3" json:"thread_key,omitempty"`
    	// contains filtered or unexported fields
    }

A thread in a Google Chat space. For example usage, see [Start or reply to a message thread](https://developers.google.com/workspace/chat/create-messages#create-message-thread).

If you specify a thread when creating a message, you can set the [`messageReplyOption`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create#messagereplyoption) field to determine what happens if no matching thread is found.

### func (*Thread) Descriptor 
    
    
    func (*Thread) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Thread.ProtoReflect.Descriptor instead.

### func (*Thread) GetName 
    
    
    func (x *Thread) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Thread) GetThreadKey 
    
    
    func (x *Thread) GetThreadKey() [string](https://pkg.go.dev/builtin#string)

### func (*Thread) ProtoMessage 
    
    
    func (*Thread) ProtoMessage()

### func (*Thread) ProtoReflect 
    
    
    func (x *Thread) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Thread) Reset 
    
    
    func (x *Thread) Reset()

### func (*Thread) String 
    
    
    func (x *Thread) String() [string](https://pkg.go.dev/builtin#string)

## ThreadReadState
    
    
    type ThreadReadState struct {
    
    	// Resource name of the thread read state.
    	//
    	// Format: `users/{user}/spaces/{space}/threads/{thread}/threadReadState`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The time when the user's thread read state was updated. Usually this
    	// corresponds with the timestamp of the last read message in a thread.
    	LastReadTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=last_read_time,json=lastReadTime,proto3" json:"last_read_time,omitempty"`
    	// contains filtered or unexported fields
    }

A user's read state within a thread, used to identify read and unread messages.

### func (*ThreadReadState) Descriptor 
    
    
    func (*ThreadReadState) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ThreadReadState.ProtoReflect.Descriptor instead.

### func (*ThreadReadState) GetLastReadTime 
    
    
    func (x *ThreadReadState) GetLastReadTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ThreadReadState) GetName 
    
    
    func (x *ThreadReadState) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ThreadReadState) ProtoMessage 
    
    
    func (*ThreadReadState) ProtoMessage()

### func (*ThreadReadState) ProtoReflect 
    
    
    func (x *ThreadReadState) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ThreadReadState) Reset 
    
    
    func (x *ThreadReadState) Reset()

### func (*ThreadReadState) String 
    
    
    func (x *ThreadReadState) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedChatServiceServer
    
    
    type UnimplementedChatServiceServer struct {
    }

UnimplementedChatServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedChatServiceServer) CompleteImportSpace 
    
    
    func (UnimplementedChatServiceServer) CompleteImportSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CompleteImportSpaceRequest) (*CompleteImportSpaceResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateCustomEmoji 
    
    
    func (UnimplementedChatServiceServer) CreateCustomEmoji([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateCustomEmojiRequest) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateMembership 
    
    
    func (UnimplementedChatServiceServer) CreateMembership([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateMessage 
    
    
    func (UnimplementedChatServiceServer) CreateMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateMessagePin 
    
    
    func (UnimplementedChatServiceServer) CreateMessagePin([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateMessagePinRequest) (*MessagePin, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateReaction 
    
    
    func (UnimplementedChatServiceServer) CreateReaction([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateReactionRequest) (*Reaction, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateSection 
    
    
    func (UnimplementedChatServiceServer) CreateSection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateSectionRequest) (*Section, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) CreateSpace 
    
    
    func (UnimplementedChatServiceServer) CreateSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteCustomEmoji 
    
    
    func (UnimplementedChatServiceServer) DeleteCustomEmoji([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteCustomEmojiRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteMembership 
    
    
    func (UnimplementedChatServiceServer) DeleteMembership([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteMessage 
    
    
    func (UnimplementedChatServiceServer) DeleteMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteMessageRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteMessagePin 
    
    
    func (UnimplementedChatServiceServer) DeleteMessagePin([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteMessagePinRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteReaction 
    
    
    func (UnimplementedChatServiceServer) DeleteReaction([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteReactionRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteSection 
    
    
    func (UnimplementedChatServiceServer) DeleteSection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteSectionRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) DeleteSpace 
    
    
    func (UnimplementedChatServiceServer) DeleteSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteSpaceRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) FindDirectMessage 
    
    
    func (UnimplementedChatServiceServer) FindDirectMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *FindDirectMessageRequest) (*Space, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) FindGroupChats 
    
    
    func (UnimplementedChatServiceServer) FindGroupChats([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *FindGroupChatsRequest) (*FindGroupChatsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetAttachment 
    
    
    func (UnimplementedChatServiceServer) GetAttachment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAttachmentRequest) (*Attachment, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetAvailability 
    
    
    func (UnimplementedChatServiceServer) GetAvailability([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAvailabilityRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetCustomEmoji 
    
    
    func (UnimplementedChatServiceServer) GetCustomEmoji([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCustomEmojiRequest) (*CustomEmoji, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetMembership 
    
    
    func (UnimplementedChatServiceServer) GetMembership([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetMessage 
    
    
    func (UnimplementedChatServiceServer) GetMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetSpace 
    
    
    func (UnimplementedChatServiceServer) GetSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetSpaceEvent 
    
    
    func (UnimplementedChatServiceServer) GetSpaceEvent([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSpaceEventRequest) (*SpaceEvent, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetSpaceNotificationSetting 
    
    
    func (UnimplementedChatServiceServer) GetSpaceNotificationSetting([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSpaceNotificationSettingRequest) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetSpaceReadState 
    
    
    func (UnimplementedChatServiceServer) GetSpaceReadState([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSpaceReadStateRequest) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) GetThreadReadState 
    
    
    func (UnimplementedChatServiceServer) GetThreadReadState([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetThreadReadStateRequest) (*ThreadReadState, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListCustomEmojis 
    
    
    func (UnimplementedChatServiceServer) ListCustomEmojis([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListCustomEmojisRequest) (*ListCustomEmojisResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListMemberships 
    
    
    func (UnimplementedChatServiceServer) ListMemberships([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListMembershipsRequest) (*ListMembershipsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListMessagePins 
    
    
    func (UnimplementedChatServiceServer) ListMessagePins([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListMessagePinsRequest) (*ListMessagePinsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListMessages 
    
    
    func (UnimplementedChatServiceServer) ListMessages([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListMessagesRequest) (*ListMessagesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListReactions 
    
    
    func (UnimplementedChatServiceServer) ListReactions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReactionsRequest) (*ListReactionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListSectionItems 
    
    
    func (UnimplementedChatServiceServer) ListSectionItems([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSectionItemsRequest) (*ListSectionItemsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListSections 
    
    
    func (UnimplementedChatServiceServer) ListSections([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSectionsRequest) (*ListSectionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListSpaceEvents 
    
    
    func (UnimplementedChatServiceServer) ListSpaceEvents([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSpaceEventsRequest) (*ListSpaceEventsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) ListSpaces 
    
    
    func (UnimplementedChatServiceServer) ListSpaces([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSpacesRequest) (*ListSpacesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) MarkAsActive 
    
    
    func (UnimplementedChatServiceServer) MarkAsActive([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkAsActiveRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) MarkAsAway 
    
    
    func (UnimplementedChatServiceServer) MarkAsAway([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkAsAwayRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) MarkAsDoNotDisturb 
    
    
    func (UnimplementedChatServiceServer) MarkAsDoNotDisturb([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkAsDoNotDisturbRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) MoveSectionItem 
    
    
    func (UnimplementedChatServiceServer) MoveSectionItem([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MoveSectionItemRequest) (*MoveSectionItemResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) PositionSection 
    
    
    func (UnimplementedChatServiceServer) PositionSection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *PositionSectionRequest) (*PositionSectionResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) SearchMessages 
    
    
    func (UnimplementedChatServiceServer) SearchMessages([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchMessagesRequest) (*SearchMessagesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) SearchSpaces 
    
    
    func (UnimplementedChatServiceServer) SearchSpaces([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchSpacesRequest) (*SearchSpacesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) SetUpSpace 
    
    
    func (UnimplementedChatServiceServer) SetUpSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SetUpSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateAvailability 
    
    
    func (UnimplementedChatServiceServer) UpdateAvailability([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAvailabilityRequest) (*Availability, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateMembership 
    
    
    func (UnimplementedChatServiceServer) UpdateMembership([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateMembershipRequest) (*Membership, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateMessage 
    
    
    func (UnimplementedChatServiceServer) UpdateMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateMessageRequest) (*Message, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateSection 
    
    
    func (UnimplementedChatServiceServer) UpdateSection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSectionRequest) (*Section, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateSpace 
    
    
    func (UnimplementedChatServiceServer) UpdateSpace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSpaceRequest) (*Space, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateSpaceNotificationSetting 
    
    
    func (UnimplementedChatServiceServer) UpdateSpaceNotificationSetting([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSpaceNotificationSettingRequest) (*SpaceNotificationSetting, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UpdateSpaceReadState 
    
    
    func (UnimplementedChatServiceServer) UpdateSpaceReadState([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSpaceReadStateRequest) (*SpaceReadState, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedChatServiceServer) UploadAttachment 
    
    
    func (UnimplementedChatServiceServer) UploadAttachment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UploadAttachmentRequest) (*UploadAttachmentResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeChatServiceServer
    
    
    type UnsafeChatServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeChatServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ChatServiceServer will result in compilation errors.

## UpdateAvailabilityRequest
    
    
    type UpdateAvailabilityRequest struct {
    
    	// Required. The availability to update.
    	Availability *Availability `protobuf:"bytes,1,opt,name=availability,proto3" json:"availability,omitempty"`
    	// Required. The list of fields to update.
    	// The only field that can be updated is `custom_status`.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the `UpdateAvailability` method.

### func (*UpdateAvailabilityRequest) Descriptor 
    
    
    func (*UpdateAvailabilityRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAvailabilityRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAvailabilityRequest) GetAvailability 
    
    
    func (x *UpdateAvailabilityRequest) GetAvailability() *Availability

### func (*UpdateAvailabilityRequest) GetUpdateMask 
    
    
    func (x *UpdateAvailabilityRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAvailabilityRequest) ProtoMessage 
    
    
    func (*UpdateAvailabilityRequest) ProtoMessage()

### func (*UpdateAvailabilityRequest) ProtoReflect 
    
    
    func (x *UpdateAvailabilityRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAvailabilityRequest) Reset 
    
    
    func (x *UpdateAvailabilityRequest) Reset()

### func (*UpdateAvailabilityRequest) String 
    
    
    func (x *UpdateAvailabilityRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateMembershipRequest
    
    
    type UpdateMembershipRequest struct {
    
    	// Required. The membership to update. Only fields specified by `update_mask`
    	// are updated.
    	Membership *Membership `protobuf:"bytes,1,opt,name=membership,proto3" json:"membership,omitempty"`
    	// Required. The field paths to update. Separate multiple values with commas
    	// or use `*` to update all field paths.
    	//
    	// Currently supported field paths:
    	//
    	// - `role`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.memberships` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for updating a membership.

### func (*UpdateMembershipRequest) Descriptor 
    
    
    func (*UpdateMembershipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateMembershipRequest.ProtoReflect.Descriptor instead.

### func (*UpdateMembershipRequest) GetMembership 
    
    
    func (x *UpdateMembershipRequest) GetMembership() *Membership

### func (*UpdateMembershipRequest) GetUpdateMask 
    
    
    func (x *UpdateMembershipRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateMembershipRequest) GetUseAdminAccess 
    
    
    func (x *UpdateMembershipRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateMembershipRequest) ProtoMessage 
    
    
    func (*UpdateMembershipRequest) ProtoMessage()

### func (*UpdateMembershipRequest) ProtoReflect 
    
    
    func (x *UpdateMembershipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateMembershipRequest) Reset 
    
    
    func (x *UpdateMembershipRequest) Reset()

### func (*UpdateMembershipRequest) String 
    
    
    func (x *UpdateMembershipRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateMessageRequest
    
    
    type UpdateMessageRequest struct {
    
    	// Required. Message with fields updated.
    	Message *Message `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// Required. The field paths to update. Separate multiple values with commas
    	// or use `*` to update all field paths.
    	//
    	// Currently supported field paths:
    	//
    	// - `text`
    	//
    	// - `attachment`
    	//
    	// - `cards` (Requires [app
    	// authentication](/chat/api/guides/auth/service-accounts).)
    	//
    	// - `cards_v2`  (Requires [app
    	// authentication](/chat/api/guides/auth/service-accounts).)
    	//
    	// - `accessory_widgets`  (Requires [app
    	// authentication](/chat/api/guides/auth/service-accounts).)
    	//
    	// - `quoted_message_metadata` (Only allows removal of the quoted message.)
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Optional. If `true` and the message isn't found, a new message is created
    	// and `updateMask` is ignored. The specified message ID must be
    	// [client-assigned](https://developers.google.com/workspace/chat/create-messages#name_a_created_message)
    	// or the request fails.
    	AllowMissing [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=allow_missing,json=allowMissing,proto3" json:"allow_missing,omitempty"`
    	// contains filtered or unexported fields
    }

Request to update a message.

### func (*UpdateMessageRequest) Descriptor 
    
    
    func (*UpdateMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateMessageRequest.ProtoReflect.Descriptor instead.

### func (*UpdateMessageRequest) GetAllowMissing 
    
    
    func (x *UpdateMessageRequest) GetAllowMissing() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateMessageRequest) GetMessage 
    
    
    func (x *UpdateMessageRequest) GetMessage() *Message

### func (*UpdateMessageRequest) GetUpdateMask 
    
    
    func (x *UpdateMessageRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateMessageRequest) ProtoMessage 
    
    
    func (*UpdateMessageRequest) ProtoMessage()

### func (*UpdateMessageRequest) ProtoReflect 
    
    
    func (x *UpdateMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateMessageRequest) Reset 
    
    
    func (x *UpdateMessageRequest) Reset()

### func (*UpdateMessageRequest) String 
    
    
    func (x *UpdateMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSectionRequest
    
    
    type UpdateSectionRequest struct {
    
    	// Required. The section to update.
    	Section *Section `protobuf:"bytes,1,opt,name=section,proto3" json:"section,omitempty"`
    	// Required. The mask to specify which fields to update.
    	//
    	// Currently supported field paths:
    	//
    	// - `display_name`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for updating a section.

### func (*UpdateSectionRequest) Descriptor 
    
    
    func (*UpdateSectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSectionRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSectionRequest) GetSection 
    
    
    func (x *UpdateSectionRequest) GetSection() *Section

### func (*UpdateSectionRequest) GetUpdateMask 
    
    
    func (x *UpdateSectionRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSectionRequest) ProtoMessage 
    
    
    func (*UpdateSectionRequest) ProtoMessage()

### func (*UpdateSectionRequest) ProtoReflect 
    
    
    func (x *UpdateSectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSectionRequest) Reset 
    
    
    func (x *UpdateSectionRequest) Reset()

### func (*UpdateSectionRequest) String 
    
    
    func (x *UpdateSectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSpaceNotificationSettingRequest
    
    
    type UpdateSpaceNotificationSettingRequest struct {
    
    	// Required. The resource name for the space notification settings must be
    	// populated in the form of
    	// `users/{user}/spaces/{space}/spaceNotificationSetting`. Only fields
    	// specified by `update_mask` are updated.
    	SpaceNotificationSetting *SpaceNotificationSetting `protobuf:"bytes,1,opt,name=space_notification_setting,json=spaceNotificationSetting,proto3" json:"space_notification_setting,omitempty"`
    	// Required. Supported field paths:
    	//
    	// - `notification_setting`
    	//
    	// - `mute_setting`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request to update the space notification settings. Only supports updating notification setting for the calling user.

### func (*UpdateSpaceNotificationSettingRequest) Descriptor 
    
    
    func (*UpdateSpaceNotificationSettingRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSpaceNotificationSettingRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSpaceNotificationSettingRequest) GetSpaceNotificationSetting 
    
    
    func (x *UpdateSpaceNotificationSettingRequest) GetSpaceNotificationSetting() *SpaceNotificationSetting

### func (*UpdateSpaceNotificationSettingRequest) GetUpdateMask 
    
    
    func (x *UpdateSpaceNotificationSettingRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSpaceNotificationSettingRequest) ProtoMessage 
    
    
    func (*UpdateSpaceNotificationSettingRequest) ProtoMessage()

### func (*UpdateSpaceNotificationSettingRequest) ProtoReflect 
    
    
    func (x *UpdateSpaceNotificationSettingRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSpaceNotificationSettingRequest) Reset 
    
    
    func (x *UpdateSpaceNotificationSettingRequest) Reset()

### func (*UpdateSpaceNotificationSettingRequest) String 
    
    
    func (x *UpdateSpaceNotificationSettingRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSpaceReadStateRequest
    
    
    type UpdateSpaceReadStateRequest struct {
    
    	// Required. The space read state and fields to update.
    	//
    	// Only supports updating read state for the calling user.
    	//
    	// To refer to the calling user, set one of the following:
    	//
    	// - The `me` alias. For example, `users/me/spaces/{space}/spaceReadState`.
    	//
    	// - Their Workspace email address. For example,
    	// `users/user@example.com/spaces/{space}/spaceReadState`.
    	//
    	// - Their user id. For example,
    	// `users/123456789/spaces/{space}/spaceReadState`.
    	//
    	// Format: users/{user}/spaces/{space}/spaceReadState
    	SpaceReadState *SpaceReadState `protobuf:"bytes,1,opt,name=space_read_state,json=spaceReadState,proto3" json:"space_read_state,omitempty"`
    	// Required. The field paths to update. Currently supported field paths:
    	//
    	// - `last_read_time`
    	//
    	// When the `last_read_time` is before the latest message create time, the
    	// space appears as unread in the UI.
    	//
    	// To mark the space as read, set `last_read_time` to any value later (larger)
    	// than the latest message create time. The `last_read_time` is coerced to
    	// match the latest message create time. Note that the space read state only
    	// affects the read state of messages that are visible in the space's
    	// top-level conversation. Replies in threads are unaffected by this
    	// timestamp, and instead rely on the thread read state.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for UpdateSpaceReadState API.

### func (*UpdateSpaceReadStateRequest) Descriptor 
    
    
    func (*UpdateSpaceReadStateRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSpaceReadStateRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSpaceReadStateRequest) GetSpaceReadState 
    
    
    func (x *UpdateSpaceReadStateRequest) GetSpaceReadState() *SpaceReadState

### func (*UpdateSpaceReadStateRequest) GetUpdateMask 
    
    
    func (x *UpdateSpaceReadStateRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSpaceReadStateRequest) ProtoMessage 
    
    
    func (*UpdateSpaceReadStateRequest) ProtoMessage()

### func (*UpdateSpaceReadStateRequest) ProtoReflect 
    
    
    func (x *UpdateSpaceReadStateRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSpaceReadStateRequest) Reset 
    
    
    func (x *UpdateSpaceReadStateRequest) Reset()

### func (*UpdateSpaceReadStateRequest) String 
    
    
    func (x *UpdateSpaceReadStateRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSpaceRequest
    
    
    type UpdateSpaceRequest struct {
    
    	// Required. Space with fields to be updated. `Space.name` must be
    	// populated in the form of `spaces/{space}`. Only fields
    	// specified by `update_mask` are updated.
    	Space *Space `protobuf:"bytes,1,opt,name=space,proto3" json:"space,omitempty"`
    	// Required. The updated field paths, comma separated if there are
    	// multiple.
    	//
    	// You can update the following fields for a space:
    	//
    	// `space_details`: Updates the space's description and guidelines. You must
    	// pass both description and guidelines in the update request as
    	// [`SpaceDetails`][google.chat.v1.Space.SpaceDetails]. If you only want to
    	// update one of the fields, pass the existing value for the other field.
    	//
    	// `display_name`: Only supports updating the display name for spaces where
    	// `spaceType` field is `SPACE`.
    	//
    	//	If you receive the error message `ALREADY_EXISTS`, try a different
    	//	value. An existing space within the
    	//
    	// Google Workspace organization might already use this display name.
    	//
    	// `space_type`: Only supports changing a `GROUP_CHAT` space type to
    	// `SPACE`. Include `display_name` together
    	// with `space_type` in the update mask and ensure that the specified space
    	// has a non-empty display name and the `SPACE` space type. Including the
    	// `space_type` mask and the `SPACE` type in the specified space when updating
    	// the display name is optional if the existing space already has the `SPACE`
    	// type. Trying to update the space type in other ways results in an invalid
    	// argument error.
    	// `space_type` is not supported with `useAdminAccess`.
    	//
    	// `space_history_state`: Updates [space history
    	// settings](https://support.google.com/chat/answer/7664687) by turning
    	// history on or off for the space. Only supported if history settings are
    	// enabled for the Google Workspace organization. To update the
    	// space history state, you must omit all other field masks in your request.
    	// `space_history_state` is not supported with `useAdminAccess`.
    	//
    	// `access_settings.audience`: Updates the [access
    	// setting](https://support.google.com/chat/answer/11971020) of who can
    	// discover the space, join the space, and preview the messages in named space
    	// where `spaceType` field is `SPACE`. If the existing space has a
    	// target audience, you can remove the audience and restrict space access by
    	// omitting a value for this field mask. To update access settings for a
    	// space, the authenticating user must be a space manager and omit all other
    	// field masks in your request. You can't update this field if the space is in
    	// [import
    	// mode](https://developers.google.com/workspace/chat/import-data-overview).
    	// To learn more, see [Make a space discoverable to specific
    	// users](https://developers.google.com/workspace/chat/space-target-audience).
    	// `access_settings.audience` is not supported with `useAdminAccess`.
    	//
    	// `access_settings.access_permission_settings`: Updates the [access
    	// permission
    	// settings](https://support.google.com/chat/answer/11971020) of who can
    	// discover and join the space where `spaceType` field is `SPACE`. Principals
    	// allowed to join the space must also be allowed to discover it. To update
    	// access permission settings for a space, the authenticating user must be a
    	// space manager or assistant manager and omit all other field masks in the
    	// request. You can't update this field if the space is in [import
    	// mode](https://developers.google.com/workspace/chat/import-data-overview).
    	// To learn more, see [Make a space discoverable to specific
    	// users](https://developers.google.com/workspace/chat/space-target-audience).
    	// `access_settings.access_permission_settings` is not supported with
    	// `useAdminAccess`.
    	// The supported field masks include:
    	//
    	// - `access_settings.access_permission_settings.discoverSpaceSetting`
    	// - `access_settings.access_permission_settings.joinSpaceSetting`
    	// - `access_settings.access_permission_settings.viewSpaceMembershipSetting`
    	//
    	// `permission_settings`: Supports changing the
    	// [permission settings](https://support.google.com/chat/answer/13340792)
    	// of a space.
    	// When updating permission settings, you can only specify
    	// `permissionSettings` field masks; you cannot update other field masks
    	// at the same time.
    	// The supported field masks include:
    	//
    	// - `permission_settings.manageMembersAndGroups`
    	// - `permission_settings.modifySpaceDetails`
    	// - `permission_settings.toggleHistory`
    	// - `permission_settings.useAtMentionAll`
    	// - `permission_settings.manageApps`
    	// - `permission_settings.manageWebhooks`
    	// - `permission_settings.replyMessages`
    	// - `permission_settings.viewSpaceMembership`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Optional. When `true`, the method runs using the user's Google Workspace
    	// administrator privileges.
    	//
    	// The calling user must be a Google Workspace administrator with the
    	// [manage chat and spaces conversations
    	// privilege](https://support.google.com/a/answer/13369245).
    	//
    	// Requires the `chat.admin.spaces` [OAuth 2.0
    	// scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).
    	//
    	// Some `FieldMask` values are not supported using admin access. For details,
    	// see the description of `update_mask`.
    	UseAdminAccess [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=use_admin_access,json=useAdminAccess,proto3" json:"use_admin_access,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update a single space.

### func (*UpdateSpaceRequest) Descriptor 
    
    
    func (*UpdateSpaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSpaceRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSpaceRequest) GetSpace 
    
    
    func (x *UpdateSpaceRequest) GetSpace() *Space

### func (*UpdateSpaceRequest) GetUpdateMask 
    
    
    func (x *UpdateSpaceRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSpaceRequest) GetUseAdminAccess 
    
    
    func (x *UpdateSpaceRequest) GetUseAdminAccess() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateSpaceRequest) ProtoMessage 
    
    
    func (*UpdateSpaceRequest) ProtoMessage()

### func (*UpdateSpaceRequest) ProtoReflect 
    
    
    func (x *UpdateSpaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSpaceRequest) Reset 
    
    
    func (x *UpdateSpaceRequest) Reset()

### func (*UpdateSpaceRequest) String 
    
    
    func (x *UpdateSpaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## UploadAttachmentRequest
    
    
    type UploadAttachmentRequest struct {
    
    	// Required. Resource name of the Chat space in which the attachment is
    	// uploaded. Format "spaces/{space}".
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The filename of the attachment, including the file extension.
    	Filename [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filename,proto3" json:"filename,omitempty"`
    	// contains filtered or unexported fields
    }

Request to upload an attachment.

### func (*UploadAttachmentRequest) Descriptor 
    
    
    func (*UploadAttachmentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UploadAttachmentRequest.ProtoReflect.Descriptor instead.

### func (*UploadAttachmentRequest) GetFilename 
    
    
    func (x *UploadAttachmentRequest) GetFilename() [string](https://pkg.go.dev/builtin#string)

### func (*UploadAttachmentRequest) GetParent 
    
    
    func (x *UploadAttachmentRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*UploadAttachmentRequest) ProtoMessage 
    
    
    func (*UploadAttachmentRequest) ProtoMessage()

### func (*UploadAttachmentRequest) ProtoReflect 
    
    
    func (x *UploadAttachmentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UploadAttachmentRequest) Reset 
    
    
    func (x *UploadAttachmentRequest) Reset()

### func (*UploadAttachmentRequest) String 
    
    
    func (x *UploadAttachmentRequest) String() [string](https://pkg.go.dev/builtin#string)

## UploadAttachmentResponse
    
    
    type UploadAttachmentResponse struct {
    
    	// Reference to the uploaded attachment.
    	AttachmentDataRef *AttachmentDataRef `protobuf:"bytes,1,opt,name=attachment_data_ref,json=attachmentDataRef,proto3" json:"attachment_data_ref,omitempty"`
    	// contains filtered or unexported fields
    }

Response of uploading an attachment.

### func (*UploadAttachmentResponse) Descriptor 
    
    
    func (*UploadAttachmentResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UploadAttachmentResponse.ProtoReflect.Descriptor instead.

### func (*UploadAttachmentResponse) GetAttachmentDataRef 
    
    
    func (x *UploadAttachmentResponse) GetAttachmentDataRef() *AttachmentDataRef

### func (*UploadAttachmentResponse) ProtoMessage 
    
    
    func (*UploadAttachmentResponse) ProtoMessage()

### func (*UploadAttachmentResponse) ProtoReflect 
    
    
    func (x *UploadAttachmentResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UploadAttachmentResponse) Reset 
    
    
    func (x *UploadAttachmentResponse) Reset()

### func (*UploadAttachmentResponse) String 
    
    
    func (x *UploadAttachmentResponse) String() [string](https://pkg.go.dev/builtin#string)

## User
    
    
    type User struct {
    
    	// Resource name for a Google Chat [user][google.chat.v1.User].
    	//
    	// Format: `users/{user}`. `users/app` can be used as an alias for the calling
    	// app [bot][google.chat.v1.User.Type.BOT] user.
    	//
    	// For [human users][google.chat.v1.User.Type.HUMAN], `{user}` is the same
    	// user identifier as:
    	//
    	// - the `id` for the
    	// [Person](https://developers.google.com/people/api/rest/v1/people) in the
    	// People API. For example, `users/123456789` in Chat API represents the same
    	// person as the `123456789` Person profile ID in People API.
    	//
    	// - the `id` for a
    	// [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
    	// in the Admin SDK Directory API.
    	//
    	// - the user's email address can be used as an alias for `{user}` in API
    	// requests. For example, if the People API Person profile ID for
    	// `user@example.com` is `123456789`, you can use `users/user@example.com` as
    	// an alias to reference `users/123456789`. Only the canonical resource name
    	// (for example `users/123456789`) will be returned from the API.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The user's display name.
    	//
    	// Populated for both app authentication and user authentication.
    	// This field is always populated for requests made with [app
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    	// When calling the Messages and Memberships APIs with [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// this field is populated for both internal and external users for the
    	// `sender` of a message, users within `annotations` (such as user
    	// mentions), and within `Membership` resources, provided the user is a
    	// member of the space or has prior affinity with the calling user.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. The user's avatar image URL.
    	//
    	// When calling the Messages and Memberships APIs with [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// this field is populated for both internal and external users for the
    	// `sender` of a message, users within `annotations` (such as user
    	// mentions), and within `Membership` resources, provided the user is a
    	// member of the space or has prior affinity with the calling user.
    	AvatarUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=avatar_url,json=avatarUrl,proto3" json:"avatar_url,omitempty"`
    	// Output only. The user's email address.
    	//
    	// When calling the Messages and Memberships APIs with [user
    	// authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user),
    	// this field is populated for both internal and external users for the
    	// `sender` of a message, users within `annotations` (such as user
    	// mentions), and within `Membership` resources, provided the user is a
    	// member of the space or has prior affinity with the calling user.
    	Email [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=email,proto3" json:"email,omitempty"`
    	// Unique identifier of the user's Google Workspace domain.
    	DomainId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
    	// User type.
    	Type User_Type `protobuf:"varint,5,opt,name=type,proto3,enum=google.chat.v1.User_Type" json:"type,omitempty"`
    	// Output only. When `true`, the user is deleted or their profile is not
    	// visible, such as when a user is mentioned in a space without being a member
    	// and without prior affinity with the calling user.
    	IsAnonymous [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=is_anonymous,json=isAnonymous,proto3" json:"is_anonymous,omitempty"`
    	// contains filtered or unexported fields
    }

If your Chat app [authenticates as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the output for a `User` resource (such as in the Messages and Memberships APIs) only populates the `name` and `type` fields for both internal and external users, unless they are members of the space or have prior affinity with the calling user.

### func (*User) Descriptor 
    
    
    func (*User) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use User.ProtoReflect.Descriptor instead.

### func (*User) GetAvatarUrl 
    
    
    func (x *User) GetAvatarUrl() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetDisplayName 
    
    
    func (x *User) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetDomainId 
    
    
    func (x *User) GetDomainId() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetEmail 
    
    
    func (x *User) GetEmail() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetIsAnonymous 
    
    
    func (x *User) GetIsAnonymous() [bool](https://pkg.go.dev/builtin#bool)

### func (*User) GetName 
    
    
    func (x *User) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*User) GetType 
    
    
    func (x *User) GetType() User_Type

### func (*User) ProtoMessage 
    
    
    func (*User) ProtoMessage()

### func (*User) ProtoReflect 
    
    
    func (x *User) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*User) Reset 
    
    
    func (x *User) Reset()

### func (*User) String 
    
    
    func (x *User) String() [string](https://pkg.go.dev/builtin#string)

## UserMentionMetadata
    
    
    type UserMentionMetadata struct {
    
    	// The user mentioned.
    	User *User `protobuf:"bytes,1,opt,name=user,proto3" json:"user,omitempty"`
    	// The type of user mention.
    	Type UserMentionMetadata_Type `protobuf:"varint,2,opt,name=type,proto3,enum=google.chat.v1.UserMentionMetadata_Type" json:"type,omitempty"`
    	// contains filtered or unexported fields
    }

Annotation metadata for user mentions (@).

### func (*UserMentionMetadata) Descriptor 
    
    
    func (*UserMentionMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UserMentionMetadata.ProtoReflect.Descriptor instead.

### func (*UserMentionMetadata) GetType 
    
    
    func (x *UserMentionMetadata) GetType() UserMentionMetadata_Type

### func (*UserMentionMetadata) GetUser 
    
    
    func (x *UserMentionMetadata) GetUser() *User

### func (*UserMentionMetadata) ProtoMessage 
    
    
    func (*UserMentionMetadata) ProtoMessage()

### func (*UserMentionMetadata) ProtoReflect 
    
    
    func (x *UserMentionMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UserMentionMetadata) Reset 
    
    
    func (x *UserMentionMetadata) Reset()

### func (*UserMentionMetadata) String 
    
    
    func (x *UserMentionMetadata) String() [string](https://pkg.go.dev/builtin#string)

## UserMentionMetadata_Type
    
    
    type UserMentionMetadata_Type [int32](https://pkg.go.dev/builtin#int32)

### UserMentionMetadata_TYPE_UNSPECIFIED, UserMentionMetadata_ADD, UserMentionMetadata_MENTION
    
    
    const (
    	// Default value for the enum. Don't use.
    	UserMentionMetadata_TYPE_UNSPECIFIED UserMentionMetadata_Type = 0
    	// Add user to space.
    	UserMentionMetadata_ADD UserMentionMetadata_Type = 1
    	// Mention user in space.
    	UserMentionMetadata_MENTION UserMentionMetadata_Type = 2
    )

### func (UserMentionMetadata_Type) Descriptor 
    
    
    func (UserMentionMetadata_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (UserMentionMetadata_Type) Enum 
    
    
    func (x UserMentionMetadata_Type) Enum() *UserMentionMetadata_Type

### func (UserMentionMetadata_Type) EnumDescriptor 
    
    
    func (UserMentionMetadata_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UserMentionMetadata_Type.Descriptor instead.

### func (UserMentionMetadata_Type) Number 
    
    
    func (x UserMentionMetadata_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (UserMentionMetadata_Type) String 
    
    
    func (x UserMentionMetadata_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (UserMentionMetadata_Type) Type 
    
    
    func (UserMentionMetadata_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## User_Type
    
    
    type User_Type [int32](https://pkg.go.dev/builtin#int32)

### User_TYPE_UNSPECIFIED, User_HUMAN, User_BOT
    
    
    const (
    	// Default value for the enum. DO NOT USE.
    	User_TYPE_UNSPECIFIED User_Type = 0
    	// Human user.
    	User_HUMAN User_Type = 1
    	// Chat app user.
    	User_BOT User_Type = 2
    )

### func (User_Type) Descriptor 
    
    
    func (User_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (User_Type) Enum 
    
    
    func (x User_Type) Enum() *User_Type

### func (User_Type) EnumDescriptor 
    
    
    func (User_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use User_Type.Descriptor instead.

### func (User_Type) Number 
    
    
    func (x User_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (User_Type) String 
    
    
    func (x User_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (User_Type) Type 
    
    
    func (User_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## WidgetMarkup
    
    
    type WidgetMarkup struct {
    
    	// A `WidgetMarkup` can only have one of the following items. You can use
    	// multiple `WidgetMarkup` fields to display more items.
    	//
    	// Types that are valid to be assigned to Data:
    	//
    	//	*WidgetMarkup_TextParagraph_
    	//	*WidgetMarkup_Image_
    	//	*WidgetMarkup_KeyValue_
    	Data isWidgetMarkup_Data `protobuf_oneof:"data"`
    	// A list of buttons. Buttons is also `oneof data` and only one of these
    	// fields should be set.
    	Buttons []*WidgetMarkup_Button `protobuf:"bytes,6,rep,name=buttons,proto3" json:"buttons,omitempty"`
    	// contains filtered or unexported fields
    }

A widget is a UI element that presents text and images.

### func (*WidgetMarkup) Descriptor 
    
    
    func (*WidgetMarkup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup) GetButtons 
    
    
    func (x *WidgetMarkup) GetButtons() []*WidgetMarkup_Button

### func (*WidgetMarkup) GetData 
    
    
    func (x *WidgetMarkup) GetData() isWidgetMarkup_Data

### func (*WidgetMarkup) GetImage 
    
    
    func (x *WidgetMarkup) GetImage() *WidgetMarkup_Image

### func (*WidgetMarkup) GetKeyValue 
    
    
    func (x *WidgetMarkup) GetKeyValue() *WidgetMarkup_KeyValue

### func (*WidgetMarkup) GetTextParagraph 
    
    
    func (x *WidgetMarkup) GetTextParagraph() *WidgetMarkup_TextParagraph

### func (*WidgetMarkup) ProtoMessage 
    
    
    func (*WidgetMarkup) ProtoMessage()

### func (*WidgetMarkup) ProtoReflect 
    
    
    func (x *WidgetMarkup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup) Reset 
    
    
    func (x *WidgetMarkup) Reset()

### func (*WidgetMarkup) String 
    
    
    func (x *WidgetMarkup) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_Button
    
    
    type WidgetMarkup_Button struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*WidgetMarkup_Button_TextButton
    	//	*WidgetMarkup_Button_ImageButton
    	Type isWidgetMarkup_Button_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

A button. Can be a text button or an image button.

### func (*WidgetMarkup_Button) Descriptor 
    
    
    func (*WidgetMarkup_Button) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_Button.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_Button) GetImageButton 
    
    
    func (x *WidgetMarkup_Button) GetImageButton() *WidgetMarkup_ImageButton

### func (*WidgetMarkup_Button) GetTextButton 
    
    
    func (x *WidgetMarkup_Button) GetTextButton() *WidgetMarkup_TextButton

### func (*WidgetMarkup_Button) GetType 
    
    
    func (x *WidgetMarkup_Button) GetType() isWidgetMarkup_Button_Type

### func (*WidgetMarkup_Button) ProtoMessage 
    
    
    func (*WidgetMarkup_Button) ProtoMessage()

### func (*WidgetMarkup_Button) ProtoReflect 
    
    
    func (x *WidgetMarkup_Button) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_Button) Reset 
    
    
    func (x *WidgetMarkup_Button) Reset()

### func (*WidgetMarkup_Button) String 
    
    
    func (x *WidgetMarkup_Button) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_Button_ImageButton
    
    
    type WidgetMarkup_Button_ImageButton struct {
    	// A button with image and `onclick` action.
    	ImageButton *WidgetMarkup_ImageButton `protobuf:"bytes,2,opt,name=image_button,json=imageButton,proto3,oneof"`
    }

## WidgetMarkup_Button_TextButton
    
    
    type WidgetMarkup_Button_TextButton struct {
    	// A button with text and `onclick` action.
    	TextButton *WidgetMarkup_TextButton `protobuf:"bytes,1,opt,name=text_button,json=textButton,proto3,oneof"`
    }

## WidgetMarkup_FormAction
    
    
    type WidgetMarkup_FormAction struct {
    
    	// The method name is used to identify which part of the form triggered the
    	// form submission. This information is echoed back to the Chat app as part
    	// of the card click event. You can use the same method name for several
    	// elements that trigger a common behavior.
    	ActionMethodName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=action_method_name,json=actionMethodName,proto3" json:"action_method_name,omitempty"`
    	// List of action parameters.
    	Parameters []*WidgetMarkup_FormAction_ActionParameter `protobuf:"bytes,2,rep,name=parameters,proto3" json:"parameters,omitempty"`
    	// contains filtered or unexported fields
    }

A form action describes the behavior when the form is submitted. For example, you can invoke Apps Script to handle the form.

### func (*WidgetMarkup_FormAction) Descriptor 
    
    
    func (*WidgetMarkup_FormAction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_FormAction.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_FormAction) GetActionMethodName 
    
    
    func (x *WidgetMarkup_FormAction) GetActionMethodName() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_FormAction) GetParameters 
    
    
    func (x *WidgetMarkup_FormAction) GetParameters() []*WidgetMarkup_FormAction_ActionParameter

### func (*WidgetMarkup_FormAction) ProtoMessage 
    
    
    func (*WidgetMarkup_FormAction) ProtoMessage()

### func (*WidgetMarkup_FormAction) ProtoReflect 
    
    
    func (x *WidgetMarkup_FormAction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_FormAction) Reset 
    
    
    func (x *WidgetMarkup_FormAction) Reset()

### func (*WidgetMarkup_FormAction) String 
    
    
    func (x *WidgetMarkup_FormAction) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_FormAction_ActionParameter
    
    
    type WidgetMarkup_FormAction_ActionParameter struct {
    
    	// The name of the parameter for the action script.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
    	// The value of the parameter.
    	Value [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

List of string parameters to supply when the action method is invoked. For example, consider three snooze buttons: snooze now, snooze one day, snooze next week. You might use `action method = snooze()`, passing the snooze type and snooze time in the list of string parameters.

### func (*WidgetMarkup_FormAction_ActionParameter) Descriptor 
    
    
    func (*WidgetMarkup_FormAction_ActionParameter) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_FormAction_ActionParameter.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_FormAction_ActionParameter) GetKey 
    
    
    func (x *WidgetMarkup_FormAction_ActionParameter) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_FormAction_ActionParameter) GetValue 
    
    
    func (x *WidgetMarkup_FormAction_ActionParameter) GetValue() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_FormAction_ActionParameter) ProtoMessage 
    
    
    func (*WidgetMarkup_FormAction_ActionParameter) ProtoMessage()

### func (*WidgetMarkup_FormAction_ActionParameter) ProtoReflect 
    
    
    func (x *WidgetMarkup_FormAction_ActionParameter) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_FormAction_ActionParameter) Reset 
    
    
    func (x *WidgetMarkup_FormAction_ActionParameter) Reset()

### func (*WidgetMarkup_FormAction_ActionParameter) String 
    
    
    func (x *WidgetMarkup_FormAction_ActionParameter) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_Icon
    
    
    type WidgetMarkup_Icon [int32](https://pkg.go.dev/builtin#int32)

The set of supported icons.

### WidgetMarkup_ICON_UNSPECIFIED, WidgetMarkup_AIRPLANE, WidgetMarkup_BOOKMARK, WidgetMarkup_BUS, WidgetMarkup_CAR, WidgetMarkup_CLOCK, WidgetMarkup_CONFIRMATION_NUMBER_ICON, WidgetMarkup_DOLLAR, WidgetMarkup_DESCRIPTION, WidgetMarkup_EMAIL, WidgetMarkup_EVENT_PERFORMER, WidgetMarkup_EVENT_SEAT, WidgetMarkup_FLIGHT_ARRIVAL, WidgetMarkup_FLIGHT_DEPARTURE, WidgetMarkup_HOTEL, WidgetMarkup_HOTEL_ROOM_TYPE, WidgetMarkup_INVITE, WidgetMarkup_MAP_PIN, WidgetMarkup_MEMBERSHIP, WidgetMarkup_MULTIPLE_PEOPLE, WidgetMarkup_OFFER, WidgetMarkup_PERSON, WidgetMarkup_PHONE, WidgetMarkup_RESTAURANT_ICON, WidgetMarkup_SHOPPING_CART, WidgetMarkup_STAR, WidgetMarkup_STORE, WidgetMarkup_TICKET, WidgetMarkup_TRAIN, WidgetMarkup_VIDEO_CAMERA, WidgetMarkup_VIDEO_PLAY
    
    
    const (
    	WidgetMarkup_ICON_UNSPECIFIED         WidgetMarkup_Icon = 0
    	WidgetMarkup_AIRPLANE                 WidgetMarkup_Icon = 1
    	WidgetMarkup_BOOKMARK                 WidgetMarkup_Icon = 26
    	WidgetMarkup_BUS                      WidgetMarkup_Icon = 25
    	WidgetMarkup_CAR                      WidgetMarkup_Icon = 9
    	WidgetMarkup_CLOCK                    WidgetMarkup_Icon = 2
    	WidgetMarkup_CONFIRMATION_NUMBER_ICON WidgetMarkup_Icon = 12
    	WidgetMarkup_DOLLAR                   WidgetMarkup_Icon = 14
    	WidgetMarkup_DESCRIPTION              WidgetMarkup_Icon = 27
    	WidgetMarkup_EMAIL                    WidgetMarkup_Icon = 10
    	WidgetMarkup_EVENT_PERFORMER          WidgetMarkup_Icon = 20
    	WidgetMarkup_EVENT_SEAT               WidgetMarkup_Icon = 21
    	WidgetMarkup_FLIGHT_ARRIVAL           WidgetMarkup_Icon = 16
    	WidgetMarkup_FLIGHT_DEPARTURE         WidgetMarkup_Icon = 15
    	WidgetMarkup_HOTEL                    WidgetMarkup_Icon = 6
    	WidgetMarkup_HOTEL_ROOM_TYPE          WidgetMarkup_Icon = 17
    	WidgetMarkup_INVITE                   WidgetMarkup_Icon = 19
    	WidgetMarkup_MAP_PIN                  WidgetMarkup_Icon = 3
    	WidgetMarkup_MEMBERSHIP               WidgetMarkup_Icon = 24
    	WidgetMarkup_MULTIPLE_PEOPLE          WidgetMarkup_Icon = 18
    	WidgetMarkup_OFFER                    WidgetMarkup_Icon = 30
    	WidgetMarkup_PERSON                   WidgetMarkup_Icon = 11
    	WidgetMarkup_PHONE                    WidgetMarkup_Icon = 13
    	WidgetMarkup_RESTAURANT_ICON          WidgetMarkup_Icon = 7
    	WidgetMarkup_SHOPPING_CART            WidgetMarkup_Icon = 8
    	WidgetMarkup_STAR                     WidgetMarkup_Icon = 5
    	WidgetMarkup_STORE                    WidgetMarkup_Icon = 22
    	WidgetMarkup_TICKET                   WidgetMarkup_Icon = 4
    	WidgetMarkup_TRAIN                    WidgetMarkup_Icon = 23
    	WidgetMarkup_VIDEO_CAMERA             WidgetMarkup_Icon = 28
    	WidgetMarkup_VIDEO_PLAY               WidgetMarkup_Icon = 29
    )

### func (WidgetMarkup_Icon) Descriptor 
    
    
    func (WidgetMarkup_Icon) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (WidgetMarkup_Icon) Enum 
    
    
    func (x WidgetMarkup_Icon) Enum() *WidgetMarkup_Icon

### func (WidgetMarkup_Icon) EnumDescriptor 
    
    
    func (WidgetMarkup_Icon) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_Icon.Descriptor instead.

### func (WidgetMarkup_Icon) Number 
    
    
    func (x WidgetMarkup_Icon) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (WidgetMarkup_Icon) String 
    
    
    func (x WidgetMarkup_Icon) String() [string](https://pkg.go.dev/builtin#string)

### func (WidgetMarkup_Icon) Type 
    
    
    func (WidgetMarkup_Icon) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## WidgetMarkup_Image
    
    
    type WidgetMarkup_Image struct {
    
    	// The URL of the image.
    	ImageUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=image_url,json=imageUrl,proto3" json:"image_url,omitempty"`
    	// The `onclick` action.
    	OnClick *WidgetMarkup_OnClick `protobuf:"bytes,2,opt,name=on_click,json=onClick,proto3" json:"on_click,omitempty"`
    	// The aspect ratio of this image (width and height). This field lets you
    	// reserve the right height for the image while waiting for it to load.
    	// It's not meant to override the built-in aspect ratio of the image.
    	// If unset, the server fills it by prefetching the image.
    	AspectRatio [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=aspect_ratio,json=aspectRatio,proto3" json:"aspect_ratio,omitempty"`
    	// contains filtered or unexported fields
    }

An image that's specified by a URL and can have an `onclick` action.

### func (*WidgetMarkup_Image) Descriptor 
    
    
    func (*WidgetMarkup_Image) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_Image.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_Image) GetAspectRatio 
    
    
    func (x *WidgetMarkup_Image) GetAspectRatio() [float64](https://pkg.go.dev/builtin#float64)

### func (*WidgetMarkup_Image) GetImageUrl 
    
    
    func (x *WidgetMarkup_Image) GetImageUrl() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_Image) GetOnClick 
    
    
    func (x *WidgetMarkup_Image) GetOnClick() *WidgetMarkup_OnClick

### func (*WidgetMarkup_Image) ProtoMessage 
    
    
    func (*WidgetMarkup_Image) ProtoMessage()

### func (*WidgetMarkup_Image) ProtoReflect 
    
    
    func (x *WidgetMarkup_Image) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_Image) Reset 
    
    
    func (x *WidgetMarkup_Image) Reset()

### func (*WidgetMarkup_Image) String 
    
    
    func (x *WidgetMarkup_Image) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_ImageButton
    
    
    type WidgetMarkup_ImageButton struct {
    
    	// The icon can be specified by an `Icon` `enum` or a URL.
    	//
    	// Types that are valid to be assigned to Icons:
    	//
    	//	*WidgetMarkup_ImageButton_Icon
    	//	*WidgetMarkup_ImageButton_IconUrl
    	Icons isWidgetMarkup_ImageButton_Icons `protobuf_oneof:"icons"`
    	// The `onclick` action.
    	OnClick *WidgetMarkup_OnClick `protobuf:"bytes,2,opt,name=on_click,json=onClick,proto3" json:"on_click,omitempty"`
    	// The name of this `image_button` that's used for accessibility.
    	// Default value is provided if this name isn't specified.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

An image button with an `onclick` action.

### func (*WidgetMarkup_ImageButton) Descriptor 
    
    
    func (*WidgetMarkup_ImageButton) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_ImageButton.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_ImageButton) GetIcon 
    
    
    func (x *WidgetMarkup_ImageButton) GetIcon() WidgetMarkup_Icon

### func (*WidgetMarkup_ImageButton) GetIconUrl 
    
    
    func (x *WidgetMarkup_ImageButton) GetIconUrl() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_ImageButton) GetIcons 
    
    
    func (x *WidgetMarkup_ImageButton) GetIcons() isWidgetMarkup_ImageButton_Icons

### func (*WidgetMarkup_ImageButton) GetName 
    
    
    func (x *WidgetMarkup_ImageButton) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_ImageButton) GetOnClick 
    
    
    func (x *WidgetMarkup_ImageButton) GetOnClick() *WidgetMarkup_OnClick

### func (*WidgetMarkup_ImageButton) ProtoMessage 
    
    
    func (*WidgetMarkup_ImageButton) ProtoMessage()

### func (*WidgetMarkup_ImageButton) ProtoReflect 
    
    
    func (x *WidgetMarkup_ImageButton) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_ImageButton) Reset 
    
    
    func (x *WidgetMarkup_ImageButton) Reset()

### func (*WidgetMarkup_ImageButton) String 
    
    
    func (x *WidgetMarkup_ImageButton) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_ImageButton_Icon
    
    
    type WidgetMarkup_ImageButton_Icon struct {
    	// The icon specified by an `enum` that indices to an icon provided by
    	// Chat API.
    	Icon WidgetMarkup_Icon `protobuf:"varint,1,opt,name=icon,proto3,enum=google.chat.v1.WidgetMarkup_Icon,oneof"`
    }

## WidgetMarkup_ImageButton_IconUrl
    
    
    type WidgetMarkup_ImageButton_IconUrl struct {
    	// The icon specified by a URL.
    	IconUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=icon_url,json=iconUrl,proto3,oneof"`
    }

## WidgetMarkup_Image_
    
    
    type WidgetMarkup_Image_ struct {
    	// Display an image in this widget.
    	Image *WidgetMarkup_Image `protobuf:"bytes,2,opt,name=image,proto3,oneof"`
    }

## WidgetMarkup_KeyValue
    
    
    type WidgetMarkup_KeyValue struct {
    
    	// At least one of icons, `top_label` and `bottom_label` must be defined.
    	//
    	// Types that are valid to be assigned to Icons:
    	//
    	//	*WidgetMarkup_KeyValue_Icon
    	//	*WidgetMarkup_KeyValue_IconUrl
    	Icons isWidgetMarkup_KeyValue_Icons `protobuf_oneof:"icons"`
    	// The text of the top label. Formatted text supported. For more information
    	// about formatting text, see
    	// [Formatting text in Google Chat
    	// apps](https://developers.google.com/workspace/chat/format-messages#card-formatting)
    	// and
    	// [Formatting
    	// text in Google Workspace
    	// Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting).
    	TopLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=top_label,json=topLabel,proto3" json:"top_label,omitempty"`
    	// The text of the content. Formatted text supported and always required.
    	// For more information
    	// about formatting text, see
    	// [Formatting text in Google Chat
    	// apps](https://developers.google.com/workspace/chat/format-messages#card-formatting)
    	// and
    	// [Formatting
    	// text in Google Workspace
    	// Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting).
    	Content [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=content,proto3" json:"content,omitempty"`
    	// If the content should be multiline.
    	ContentMultiline [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,9,opt,name=content_multiline,json=contentMultiline,proto3" json:"content_multiline,omitempty"`
    	// The text of the bottom label. Formatted text supported. For more
    	// information about formatting text, see [Formatting text in Google Chat
    	// apps](https://developers.google.com/workspace/chat/format-messages#card-formatting)
    	// and
    	// [Formatting
    	// text in Google Workspace
    	// Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting).
    	BottomLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=bottom_label,json=bottomLabel,proto3" json:"bottom_label,omitempty"`
    	// The `onclick` action. Only the top label, bottom label, and content
    	// region are clickable.
    	OnClick *WidgetMarkup_OnClick `protobuf:"bytes,6,opt,name=on_click,json=onClick,proto3" json:"on_click,omitempty"`
    	// A control widget. You can set either `button` or `switch_widget`,
    	// but not both.
    	//
    	// Types that are valid to be assigned to Control:
    	//
    	//	*WidgetMarkup_KeyValue_Button
    	Control isWidgetMarkup_KeyValue_Control `protobuf_oneof:"control"`
    	// contains filtered or unexported fields
    }

A UI element contains a key (label) and a value (content). This element can also contain some actions such as `onclick` button.

### func (*WidgetMarkup_KeyValue) Descriptor 
    
    
    func (*WidgetMarkup_KeyValue) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_KeyValue.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_KeyValue) GetBottomLabel 
    
    
    func (x *WidgetMarkup_KeyValue) GetBottomLabel() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_KeyValue) GetButton 
    
    
    func (x *WidgetMarkup_KeyValue) GetButton() *WidgetMarkup_Button

### func (*WidgetMarkup_KeyValue) GetContent 
    
    
    func (x *WidgetMarkup_KeyValue) GetContent() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_KeyValue) GetContentMultiline 
    
    
    func (x *WidgetMarkup_KeyValue) GetContentMultiline() [bool](https://pkg.go.dev/builtin#bool)

### func (*WidgetMarkup_KeyValue) GetControl 
    
    
    func (x *WidgetMarkup_KeyValue) GetControl() isWidgetMarkup_KeyValue_Control

### func (*WidgetMarkup_KeyValue) GetIcon 
    
    
    func (x *WidgetMarkup_KeyValue) GetIcon() WidgetMarkup_Icon

### func (*WidgetMarkup_KeyValue) GetIconUrl 
    
    
    func (x *WidgetMarkup_KeyValue) GetIconUrl() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_KeyValue) GetIcons 
    
    
    func (x *WidgetMarkup_KeyValue) GetIcons() isWidgetMarkup_KeyValue_Icons

### func (*WidgetMarkup_KeyValue) GetOnClick 
    
    
    func (x *WidgetMarkup_KeyValue) GetOnClick() *WidgetMarkup_OnClick

### func (*WidgetMarkup_KeyValue) GetTopLabel 
    
    
    func (x *WidgetMarkup_KeyValue) GetTopLabel() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_KeyValue) ProtoMessage 
    
    
    func (*WidgetMarkup_KeyValue) ProtoMessage()

### func (*WidgetMarkup_KeyValue) ProtoReflect 
    
    
    func (x *WidgetMarkup_KeyValue) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_KeyValue) Reset 
    
    
    func (x *WidgetMarkup_KeyValue) Reset()

### func (*WidgetMarkup_KeyValue) String 
    
    
    func (x *WidgetMarkup_KeyValue) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_KeyValue_
    
    
    type WidgetMarkup_KeyValue_ struct {
    	// Display a key value item in this widget.
    	KeyValue *WidgetMarkup_KeyValue `protobuf:"bytes,3,opt,name=key_value,json=keyValue,proto3,oneof"`
    }

## WidgetMarkup_KeyValue_Button
    
    
    type WidgetMarkup_KeyValue_Button struct {
    	// A button that can be clicked to trigger an action.
    	Button *WidgetMarkup_Button `protobuf:"bytes,7,opt,name=button,proto3,oneof"`
    }

## WidgetMarkup_KeyValue_Icon
    
    
    type WidgetMarkup_KeyValue_Icon struct {
    	// An enum value that's replaced by the Chat API with the
    	// corresponding icon image.
    	Icon WidgetMarkup_Icon `protobuf:"varint,1,opt,name=icon,proto3,enum=google.chat.v1.WidgetMarkup_Icon,oneof"`
    }

## WidgetMarkup_KeyValue_IconUrl
    
    
    type WidgetMarkup_KeyValue_IconUrl struct {
    	// The icon specified by a URL.
    	IconUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=icon_url,json=iconUrl,proto3,oneof"`
    }

## WidgetMarkup_OnClick
    
    
    type WidgetMarkup_OnClick struct {
    
    	// Types that are valid to be assigned to Data:
    	//
    	//	*WidgetMarkup_OnClick_Action
    	//	*WidgetMarkup_OnClick_OpenLink
    	Data isWidgetMarkup_OnClick_Data `protobuf_oneof:"data"`
    	// contains filtered or unexported fields
    }

An `onclick` action (for example, open a link).

### func (*WidgetMarkup_OnClick) Descriptor 
    
    
    func (*WidgetMarkup_OnClick) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_OnClick.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_OnClick) GetAction 
    
    
    func (x *WidgetMarkup_OnClick) GetAction() *WidgetMarkup_FormAction

### func (*WidgetMarkup_OnClick) GetData 
    
    
    func (x *WidgetMarkup_OnClick) GetData() isWidgetMarkup_OnClick_Data

### func (*WidgetMarkup_OnClick) GetOpenLink 
    
    
    func (x *WidgetMarkup_OnClick) GetOpenLink() *WidgetMarkup_OpenLink

### func (*WidgetMarkup_OnClick) ProtoMessage 
    
    
    func (*WidgetMarkup_OnClick) ProtoMessage()

### func (*WidgetMarkup_OnClick) ProtoReflect 
    
    
    func (x *WidgetMarkup_OnClick) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_OnClick) Reset 
    
    
    func (x *WidgetMarkup_OnClick) Reset()

### func (*WidgetMarkup_OnClick) String 
    
    
    func (x *WidgetMarkup_OnClick) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_OnClick_Action
    
    
    type WidgetMarkup_OnClick_Action struct {
    	// A form action is triggered by this `onclick` action if specified.
    	Action *WidgetMarkup_FormAction `protobuf:"bytes,1,opt,name=action,proto3,oneof"`
    }

## WidgetMarkup_OnClick_OpenLink
    
    
    type WidgetMarkup_OnClick_OpenLink struct {
    	// This `onclick` action triggers an open link action if specified.
    	OpenLink *WidgetMarkup_OpenLink `protobuf:"bytes,2,opt,name=open_link,json=openLink,proto3,oneof"`
    }

## WidgetMarkup_OpenLink
    
    
    type WidgetMarkup_OpenLink struct {
    
    	// The URL to open.
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=url,proto3" json:"url,omitempty"`
    	// contains filtered or unexported fields
    }

A link that opens a new window.

### func (*WidgetMarkup_OpenLink) Descriptor 
    
    
    func (*WidgetMarkup_OpenLink) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_OpenLink.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_OpenLink) GetUrl 
    
    
    func (x *WidgetMarkup_OpenLink) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_OpenLink) ProtoMessage 
    
    
    func (*WidgetMarkup_OpenLink) ProtoMessage()

### func (*WidgetMarkup_OpenLink) ProtoReflect 
    
    
    func (x *WidgetMarkup_OpenLink) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_OpenLink) Reset 
    
    
    func (x *WidgetMarkup_OpenLink) Reset()

### func (*WidgetMarkup_OpenLink) String 
    
    
    func (x *WidgetMarkup_OpenLink) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_TextButton
    
    
    type WidgetMarkup_TextButton struct {
    
    	// The text of the button.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// The `onclick` action of the button.
    	OnClick *WidgetMarkup_OnClick `protobuf:"bytes,2,opt,name=on_click,json=onClick,proto3" json:"on_click,omitempty"`
    	// contains filtered or unexported fields
    }

A button with text and `onclick` action.

### func (*WidgetMarkup_TextButton) Descriptor 
    
    
    func (*WidgetMarkup_TextButton) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_TextButton.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_TextButton) GetOnClick 
    
    
    func (x *WidgetMarkup_TextButton) GetOnClick() *WidgetMarkup_OnClick

### func (*WidgetMarkup_TextButton) GetText 
    
    
    func (x *WidgetMarkup_TextButton) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_TextButton) ProtoMessage 
    
    
    func (*WidgetMarkup_TextButton) ProtoMessage()

### func (*WidgetMarkup_TextButton) ProtoReflect 
    
    
    func (x *WidgetMarkup_TextButton) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_TextButton) Reset 
    
    
    func (x *WidgetMarkup_TextButton) Reset()

### func (*WidgetMarkup_TextButton) String 
    
    
    func (x *WidgetMarkup_TextButton) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_TextParagraph
    
    
    type WidgetMarkup_TextParagraph struct {
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// contains filtered or unexported fields
    }

A paragraph of text. Formatted text supported. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/workspace/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting).

### func (*WidgetMarkup_TextParagraph) Descriptor 
    
    
    func (*WidgetMarkup_TextParagraph) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use WidgetMarkup_TextParagraph.ProtoReflect.Descriptor instead.

### func (*WidgetMarkup_TextParagraph) GetText 
    
    
    func (x *WidgetMarkup_TextParagraph) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*WidgetMarkup_TextParagraph) ProtoMessage 
    
    
    func (*WidgetMarkup_TextParagraph) ProtoMessage()

### func (*WidgetMarkup_TextParagraph) ProtoReflect 
    
    
    func (x *WidgetMarkup_TextParagraph) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*WidgetMarkup_TextParagraph) Reset 
    
    
    func (x *WidgetMarkup_TextParagraph) Reset()

### func (*WidgetMarkup_TextParagraph) String 
    
    
    func (x *WidgetMarkup_TextParagraph) String() [string](https://pkg.go.dev/builtin#string)

## WidgetMarkup_TextParagraph_
    
    
    type WidgetMarkup_TextParagraph_ struct {
    	// Display a text paragraph in this widget.
    	TextParagraph *WidgetMarkup_TextParagraph `protobuf:"bytes,1,opt,name=text_paragraph,json=textParagraph,proto3,oneof"`
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
