---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-events-documentation/
title: UI module events \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:56.357237+00:00
---

# UI module events  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-events-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  UI module events Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API documentation for all custom UI module events.

## Event details

Event name | Payload | Description  
---|---|---  
active-conversation-selected | ActiveConversationSelectedPayload | Dispatched when a conversation is selected.  
smart-reply-selected | SmartReplySelection | Dispatched when a Smart Reply chip is selected.  
smart-reply-follow-up-suggestions-received | SmartReplyFollowUpSuggestionsReceivedPayload | Dispatched when Smart Reply follow-up suggestions have been received.  
conversation-details-received | ConversationDetailsReceivedPayload | Dispatched when conversation details are received from the SDK (including agent and customer info).  
conversation-initialization-requested | ConversationInitializationRequestedPayload | Dispatched when the Dialogflow conversation should be initialized.  
conversation-initialized | ConversationInitializedPayload | Dispatched when the Dialogflow conversation has been initialized.  
conversation-started | ConversationStartedPayload | Dispatched when the Dialogflow conversation has started.  
conversation-completed | ConversationCompletedPayload | Dispatched downstream to notify UI components and subscribers that the Dialogflow conversation has successfully been completed on the backend.  
complete-conversation-requested | CompleteConversationRequestedPayload | Dispatched by a connector or integration to request that the Dialogflow conversation is marked as complete.  
conversation-profile-requested | ConversationProfileRequestedPayload | Dispatched when the Dialogflow conversation profile is being fetched.  
conversation-profile-received | ConversationProfileReceivedPayload | Dispatched when the Dialogflow conversation profile has been received.  
conversation-model-requested | ConversationModelRequestedPayload | Dispatched when the Dialogflow conversation model is being fetched.  
conversation-model-received | ConversationModelReceivedPayload | Dispatched when the Dialogflow conversation model has been received.  
new-message-received | NewMessageReceivedPayload | Dispatched when a new transcript message has been received.  
analyze-content-requested | AnalyzeContentRequestDetails | Dispatched when an AnalyzeContent request should be made.  
analyze-content-response-received | AnalyzeContentResponseReceivedPayload | Dispatched when a new AnalyzeContentResponse has been received.  
conversation-summarization-requested | ConversationSummarizationRequestedEventPayload | Conversation summarization requested.  
stateless-conversation-summarization-requested | StatelessConversationSummarizationRequestedPayload | Stateless conversation summarization requested.  
stateless-conversation-summarization-response-received | StatelessConversationSummarizationResponseReceivedPayload | Stateless conversation summarization response received.  
conversation-summarization-received | ConversationSummarizationReceivedPayload | Conversation summarization received.  
dialogflow-api-error | DialogflowApiErrorPayload | Dialogflow API error encountered.  
dialogflow-api-authentication-error | void | Dialogflow API authentication (401) error encountered.  
answer-record-requested | AnswerRecordRequestedPayload | Answer record requested.  
answer-record-received | AnswerRecordReceivedPayload | Answer record received.  
patch-answer-record-requested | PatchAnswerRecordRequestedPayload | Patch answer record requested.  
patch-answer-record-received | PatchAnswerRecordReceivedPayload | Patch answer record request received.  
article-search-requested | ArticleSearchRequestedPayload | Article search requested.  
article-search-response-received | ArticleSearchResponseReceivedPayload | Article search results received.  
dark-mode-toggled | DarkModeToggledPayload | Dark mode toggled in Agent desktop.  
snackbar-notification-requested | SnackbarNotificationPayload | Snackbar notification requested.  
live-person-connector-initialized | void | LivePerson connector initialized.  
genesys-cloud-connector-initialized | void | Genesys Cloud connector initialized.  
api-connector-initialized | void | API connector initialized.  
event-based-connector-initialized | void | Event-based connector initialized.  
live-person-connector-initialization-failed | void | LivePerson connector initialization failed.  
genesys-cloud-connector-initialization-failed | void | Genesys Cloud connector initialization failed.  
genesys-cloud-connector-access-token-received | GenesysCloudConnectorAccessTokenReceivedPayload | Genesys Cloud connector access token received.  
api-connector-initialization-failed | void | API connector initialization failed.  
event-based-connector-initialization-failed | void | Event-based connector initialization failed.  
event-based-connection-established | void | Dispatched when Websocket connection is established.  
list-messages-requested | ListMessagesRequestedPayload | Request to list messages for a given conversation.  
list-messages-response-received | ListMessagesResponseReceivedPayload | Dispatched when a list messages response is received.  
virtual-agent-assist-response-message-selected | VirtualAgentAssistResponseMessageSelectedPayload | Dispatched when a Virtual Agent Assist response message is selected. This will be used to populate the agent input box with the selected message.  
human-agent-transfer-initiated | HumanAgentTransferInitiatedPayload | Dispatched when a call is transferred from a virtual agent to a human agent.  
search-knowledge-requested | SearchKnowledgeRequestedPayload | Search knowledge requested.  
search-knowledge-response-received | SearchKnowledgeResponseReceivedPayload | Search knowledge response received.  
knowledge-assist-v2-answer-pasted | string | A Knowledge Assist v2 answer to be pasted into the chat.  
batch-create-messages-requested | BatchCreateMessagesRequestedPayload | Batch create messages in a conversation. This will add the messages to the conversation without generating Agent Assist suggestions for the messages.  
batch-create-messages-response-received | BatchCreateMessagesResponseReceivedPayload | Batch create messages response received.  
  
## Event payloads

See all custom event payloads.

### ActiveConversationSelectedPayload
    
    
    interface ActiveConversationSelectedPayload {
      conversationName: string;
    }
    

### AnalyzeContentRequestDetails
    
    
    interface AnalyzeContentRequestDetails {
      type?: string;
      conversationId: string;
      participantRole:
        | "ROLE_UNSPECIFIED"
        | "HUMAN_AGENT"
        | "AUTOMATED_AGENT"
        | "END_USER";
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.participants/analyzeContent#request-body
       */
      request: AnalyzeContentRequest;
    }
    

### AnalyzeContentResponseReceivedPayload
    
    
    interface AnalyzeContentResponseReceivedPayload {
      conversationName: string;
      payload: {
        type?: string;
    
        /**
         * @link
         * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.participants#Participant
         */
        participant?: Participant;
    
        /**
         * @link
         * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.participants/analyzeContent#request-body
         */
        request?: AnalyzeContentRequest;
    
        /**
         * @link
         * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/AnalyzeContentResponse
         */
        response: AnalyzeContentResponse;
      };
    }
    

### ArticleSearchRequestedPayload
    
    
    interface ArticleSearchRequestedPayload {
      queryText: string;
    }
    

### ArticleSearchResponseReceivedPayload
    
    
    interface ArticleSearchResponseReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/priv/docs/reference/rest/v2beta1/projects.locations.conversations.suggestions/searchArticles#response-body
       */
      payload: SearchArticlesResponse;
    }
    

### ConversationDetailsReceivedPayload
    
    
    interface ConversationDetailsReceivedPayload {
      conversationName: string;
      payload: {
        chatInfo: {
          rtSessionId: string;
          accountId: string;
          chatRequestedTime: number;
          chatStartTime: number;
          sessionStartTime: number;
          chatStartUrl: string;
          spectatedEngagement: boolean;
          chatSkill: string;
        };
        chattingAgentInfo: {
          agentName: string;
          agentNickname: string;
          agentGroupName: string;
          agentId: number;
        };
        agentInfo: {
          accountId: string;
          agentName: string;
          agentNickname: string;
          agentId: number;
          agentEmail: string;
          employeeId: string;
          maxChats: number;
          agentGroupName: string;
        };
        chatTranscript: { lines: TranscriptMessage[] };
        surveyQuestions: {
          preChat: {
            email: { value: string; displayName: string };
            phone: { value: string; displayName: string };
            name: { value: string; displayName: string };
            customizedQuestions: [];
          };
          postChat: [];
          agentSurvey: [];
        };
        visitorInfo: {
          visitorId: string;
          visitorName: string;
          visitorSso: boolean;
          device: string;
          browser: string;
          operatingSystem: string;
          country: string;
          countryCode: string;
          state: string;
          city: string;
          isp: string;
          organization: string;
          IpAddress: string;
          visitStartTime: string;
          chattingVisitorState: string;
          chatRequestedTime: string;
          chatStartUrl: string;
          visitorTimezone: string;
          visitorTyping: boolean;
        };
        campaignInfo: {
          campaignName: string;
          campaignId: string;
          campaignDescription: string;
          targetAudience: [];
          goalName: string;
          goalId: string;
          goalDescription: string;
        };
        engagementInfo: {
          VisitorBehavior: [];
          skill: string;
          engagementType: string;
          engagementId: string;
          engagementName: string;
          agentNote: string;
          engagementSkill: string;
        };
        visitorJourney: {
          pages: [];
          searchEngine: { searchProvider: string; searchKeywords: string };
        };
        SDE: {
          customerDetails: [];
          personalInfo: [];
          marketingSource: [];
          leadGeneration: [];
          transaction: [];
          viewedProducts: [];
          shoppingCart: [];
          serviceActivity: [];
          error: [];
        };
        authenticatedData: { customerDetails: []; personalInfo: [] };
        claimsAndAuthType: { claims: {}; acr: string };
        applicationInfo: { theme: "light" | "dark" };
        customVariables: [];
        splitSession: { customVariables: [] };
      };
    }
    

### ConversationInitializationRequestedPayload
    
    
    interface ConversationInitializationRequestedPayload {
      conversationName: string;
    }
    

### ConversationInitializedPayload
    
    
    interface ConversationInitializedPayload {
      conversation: Conversation;
      participants: ParticipantsMap<Participant_ | null>;
    }
    

### ConversationProfileRequestedPayload
    
    
    interface ConversationProfileRequestedPayload {
      conversationProfileName: string;
    }
    

### ConversationProfileReceivedPayload
    
    
    type ConversationProfileReceivedPayload =
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversationProfiles#ConversationProfile
       */
      ConversationProfile | null;
    

### ConversationModelRequestedPayload
    
    
    interface ConversationModelRequestedPayload {
      modelName: string | null;
    }
    

### ConversationModelReceivedPayload
    
    
    type ConversationModelReceivedPayload =
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversationModels#ConversationModel
       */
      ConversationModel | null;
    

### ConversationSummarizationReceivedPayload
    
    
    interface ConversationSummarizationReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestConversationSummaryResponse
       */
      payload: SuggestConversationSummaryResponse;
    }
    

### ConversationSummarizationRequestedEventPayload
    
    
    type ConversationSummarizationRequestedEventPayload = {
      conversationName?: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.suggestions/suggestConversationSummary#request-body
       */
      request?: SuggestConversationSummaryRequest;
    } | void;
    

### DarkModeToggledPayload
    
    
    interface DarkModeToggledPayload {
      on: boolean;
    }
    

### DialogflowApiErrorPayload
    
    
    type DialogflowApiErrorPayload = {
      conversationName: string;
      source:
        | "TYPE_UNSPECIFIED"
        | "ARTICLE_SUGGESTION"
        | "FAQ"
        | "SMART_REPLY"
        | "DIALOGFLOW_ASSIST"
        | "SMART_COMPOSE"
        | "ISSUE_SMART_COMPOSE"
        | "SPELL_GRAMMAR_CORRECTION"
        | "CONVERSATION_SUMMARIZATION"
        | "KEY_MOMENT"
        | "ARTICLE_SEARCH"
        | "CONVERSATION_GUIDANCE"
        | "ARTICLE_SUGGESTION_VOICE"
        | "CONVERSATION_SUMMARIZATION_VOICE"
        | "KNOWLEDGE_SEARCH"
        | "KNOWLEDGE_ASSIST"
        | "ENTITY_EXTRACTION"
        | "ANALYZE_CONTENT"
        | "INITIALIZATION"
        | "AUTHORIZATION"
        | "LIST_MESSAGES"
        | "BATCH_CREATE_MESSAGES"
        | "GET_CONVERSATION_PROFILE"
        | "GET_CONVERSATION_MODEL"
        | "SEARCH_KNOWLEDGE"
        | "GENERATE_STATELESS_SUMMARY";
      data?: Dictionary;
      error: GoogleRpcStatus | null;
    } | null;
    

### SmartReplySelection
    
    
    SuggestionFeatureSelection<SmartReplyAnswer>
    

### SmartReplyFollowUpSuggestionsReceivedPayload
    
    
    interface SmartReplyFollowUpSuggestionsReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestSmartRepliesResponse#smartreplyanswer
       */
      payload: SmartReplyAnswer_[];
    }
    

### PatchAnswerRecordRequestedPayload
    
    
    type PatchAnswerRecordRequestedPayload = PatchPayload<{
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord
       */
      answerRecord: AnswerRecord;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord
       */
      previousAnswerRecord?: AnswerRecord | undefined;
    }>;
    

### PatchAnswerRecordReceivedPayload
    
    
    interface PatchAnswerRecordReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord
       */
      payload: AnswerRecord;
    }
    

### SnackbarNotificationPayload
    
    
    interface SnackbarNotificationPayload {
      message: string;
      actionMessage?: string | undefined;
      actionHandler?: () => void;
    }
    

### AnswerRecordRequestedPayload
    
    
    interface AnswerRecordRequestedPayload {
      answerRecordName: string;
    }
    

### AnswerRecordReceivedPayload
    
    
    interface AnswerRecordReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord
       */
      payload: AnswerRecord;
    }
    

### ConversationStartedPayload
    
    
    interface ConversationStartedPayload {
      conversationName: string;
    }
    

### ConversationCompletedPayload
    
    
    interface ConversationCompletedPayload {
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations/complete
       */
      conversationName: string;
    }
    

### CompleteConversationRequestedPayload
    
    
    interface CompleteConversationRequestedPayload {
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations/complete
       */
      conversationName: string;
    }
    

### NewMessageReceivedPayload
    
    
    type NewMessageReceivedPayload =
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Message
       */
      Message;
    

### GenesysCloudConnectorAccessTokenReceivedPayload
    
    
    export declare interface GenesysCloudConnectorAccessTokenReceivedPayload {
      accessToken: string;
    }
    

### ListMessagesRequestedPayload
    
    
    interface ListMessagesRequestedPayload {
      conversationName: string;
    }
    

### ListMessagesResponseReceivedPayload
    
    
    interface ListMessagesResponseReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ListMessagesResponse
       */
      payload: ListMessagesResponse;
    }
    

### VirtualAgentAssistResponseMessageSelectedPayload
    
    
    interface VirtualAgentAssistResponseMessageSelectedPayload {
      responseMessage: string;
    }
    

### HumanAgentTransferInitiatedPayload
    
    
    interface HumanAgentTransferInitiatedPayload {
      conversationName: string;
    }
    

### SearchKnowledgeRequestedPayload
    
    
    interface SearchKnowledgeRequestedPayload {
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.suggestions/searchKnowledge
       */
      request: SearchKnowledgeRequest;
    }
    

### SearchKnowledgeResponseReceivedPayload
    
    
    interface SearchKnowledgeResponseReceivedPayload {
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.suggestions/searchKnowledge
       */
      request: SearchKnowledgeRequest;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SearchKnowledgeResponse
       */
      response: SearchKnowledgeResponse;
    }
    

### BatchCreateMessagesRequestedPayload
    
    
    interface BatchCreateMessagesRequestedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.messages/batchCreate#request-body
       */
      request: BatchCreateMessagesRequest;
    }
    

### BatchCreateMessagesResponseReceivedPayload
    
    
    interface BatchCreateMessagesResponseReceivedPayload {
      conversationName: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/BatchCreateMessagesResponse
       */
      response: BatchCreateMessagesResponse;
    }
    

### StatelessConversationSummarizationRequestedPayload
    
    
    interface StatelessConversationSummarizationRequestedPayload {
      conversationName?: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.suggestions/generateStatelessSummary#request-body
       */
      request?: GenerateStatelessSummaryRequest;
    }
    

### StatelessConversationSummarizationResponseReceivedPayload
    
    
    interface StatelessConversationSummarizationResponseReceivedPayload {
      conversationName?: string;
    
      /**
       * @link
       * https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GenerateStatelessSummaryResponse
       */
      response?: GenerateStatelessSummaryResponse;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
