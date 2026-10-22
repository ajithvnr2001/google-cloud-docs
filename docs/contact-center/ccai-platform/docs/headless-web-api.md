---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api/
title: Headless web SDK API methods \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:01.532533+00:00
---

# Headless web SDK API methods  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless web SDK API methods Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the API methods available for the headless web SDK.

## Company and menus

Methods for handling company values and menus.

### getTrigger

This method detects the current page's proactive triggers. It returns either the current matched trigger or `null`.
    
    
    const trigger = await client.getTrigger()
    

### getCompany

This method retrieves the company information.

**Method signature**
    
    
    getCompany(): Promise<CompanyResponse>
    

**Return value**

Returns a `CompanyResponse` object.

**Interfaces**
    
    
    interface CompanyResponse {
      name: string;
      subdomain: string;
      support_email: string;
      languages: LanguageOption[];
      action_tracking: boolean;
      email_transcripts: boolean;
      message_preview: boolean;
      email_enhancement: boolean;
      cobrowse_domain?: string;
    }
    

**Example usage**
    
    
    try {
      const company = await client.getCompany()
    } catch (error) {
      // handle error
    }
    

### getMenus

This method lists all menu items available for the tenant.

**Method signature**
    
    
    getMenus(key?: string, lang?: string): Promise<MenuResponse>
    

**Return value**

Returns a `MenuResponse` object.

**Interfaces**
    
    
    interface MenuResponse {
      menus: MenuItem[];
      direct: {
        key: boolean;
        user: boolean;
      };
    }
    
    interface MenuItem {
      id: number;
      name?: string;
      enabled: boolean;
      redirection?: {
        option: string;
        data: string;
      };
      children?: MenuItem[];
      channels: MenuChannel[];
      deflection?: {
        enabled: boolean;
        type: string;
      };
    }
    

**Example usage**
    
    
    try {
      const data: MenuResponse = await client.getMenus("direct_menu_key")
      console.log(data.menus)
      console.log(data.direct)
    } catch (error) {
      // handle error
    }
    

### getWaitTimes

This method gets the wait time for the chat channel or the call channel of a menu.

**Method signature**
    
    
    getWaitTimes(menuId: number | string, lang?: string): Promise<WaitTimeResponse>
    

**Return value**

Returns a `WaitTimeResponse` object.

**Interfaces**
    
    
    interface WaitTimeResponse {
      chat: number;
      voice_call: number;
    }
    

**Example usage**
    
    
    try {
      const data: WaitTimeResponse = await client.getWaitTimes(123)
    } catch (error) {
      // handle error
    }
    

## Calls

Methods for handling scheduled calls through the SDK.

### createCall

This method creates an instant or scheduled call.

**Method signature**
    
    
    createCall(menuId: number | string, data: CallRequest): Promise<CallResponse>
    

**Return value**

Returns a `CallResponse` object.

**Interfaces**
    
    
    interface CallRequest {
      phone_number: string;
      lang?: string;
      scheduled_at?: string;
      ticket_id?: string;
      email?: string;
      recording_permission?: "recording_permission_not_asked" | "recording_permission_granted" | "recording_permission_denied";
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
      reschedule_call_id?: number;
      use_advanced_call_scheduling?: boolean;
    }
    

**Example Usage**
    
    
    try {
      const call = await client.createCall(123, { phone_number: '+12345678' })
    } catch (error) {
      // handle error
    }
    

### loadCall

This method retrieves the call information for a specified call ID.

**Method Signature**
    
    
    loadCall(callId: number | string): Promise<CallResponse>
    

**Return value**

Returns a `CallResponse` object.

**Interfaces**
    
    
    interface CallResponse {
      id: number;
      lang: string;
      menu_id: number;
      status: string;
      type: string;
      scheduled_at?: string;
      recording_permitted: boolean;
      survey_enabled: boolean;
      created_at: string;
      menus: {
        id: number;
        name: string;
      }[];
    }
    

**Example usage**
    
    
    try {
      const call = await client.loadCall(1234)
    } catch (error) {
      // handle error
    }
    

### cancelCall

This method cancels a call.

**Method signature**
    
    
    cancelCall(callId: number | string): Promise<CallResponse>
    

**Return value**

Returns a `CallResponse` object.

**Interfaces**
    
    
    interface CallResponse {
      id: number;
      lang: string;
      menu_id: number;
      status: string;
      type: string;
      scheduled_at?: string;
      recording_permitted: boolean;
      survey_enabled: boolean;
      created_at: string;
      menus: {
        id: number;
        name: string;
      }[];
    }
    

**Example usage**
    
    
    try {
      const response = await client.cancelCall(1234)
    } catch (error) {
      // handle error
    }
    

### getTimeSlots

Retrieves available time slots for scheduled calls on a given menu.

When called with a `GetTimeSlotsRequest` options object, this method supports the following:

  * [Advanced call scheduling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#advanced-call-scheduling): `useAdvancedCallScheduling: true`

  * Rescheduling an existing call: `rescheduleCallId`




The deprecated `lang` string signature is still supported and routes to the same endpoint, with only `lang` populated.

**Method signature**
    
    
    getTimeSlots(menuId: number | string, options?: GetTimeSlotsRequest): Promise<string[]>
    

**Warning:** The previous signature, `getTimeSlots(menuId, lang?)`, is deprecated. Google recommends migrating to the new options-based signature, as documented here. The old signature continues to work but might be shut off in a later release.

**Return value**

Returns an array of time slot strings.

**Interfaces**
    
    
    interface GetTimeSlotsRequest {
      lang?: string;
      rescheduleCallId?: number;          // ID of an existing call being rescheduled
      useAdvancedCallScheduling?: boolean; // Enable advanced call scheduling behavior
    }
    

**Example usage**
    
    
    // New options-based signature (recommended)
    try {
      const slots = await client.getTimeSlots(123, {
        lang: 'en',
        useAdvancedCallScheduling: true,
      })
    } catch (error) {
      // handle error
    }
    
    // Deprecated signature (still supported)
    try {
      const slots = await client.getTimeSlots(123, 'en')
    } catch (error) {
      // handle error
    }
    

### fetchTimeSlotAvailability

This method checks whether time slots are available for a given menu without fetching the full list of time slots. You can use it to conditionally show scheduling options from the UI.

**Method signature**
    
    
    fetchTimeSlotAvailability(menuId: number | string, lang?: string): Promise<boolean>
    

**Return value**

Returns `true` if time slots are available. Otherwise, `false`.

**Example usage**
    
    
    try {
      const isAvailable = await client.fetchTimeSlotAvailability(123, 'en')
      if (isAvailable) {
        // Show scheduling UI
      }
    } catch (error) {
      // handle error
    }
    

## Chats

Methods for handling chats with the SDK.

### createChat

This method creates a new chat.

**Method Signature**
    
    
    createChat(menuId: number | string, data: ChatRequest): Promise<Chat>
    

**Return Value**

Returns a `Chat` instance.

**Interfaces**
    
    
    interface ChatRequest {
      lang?: string;
      trigger_id?: string;
      ticket_id?: string;
      email?: string;
      greeting?: string;
      cobrowsable?: boolean;
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
    }
    

**Example Usage**
    
    
    try {
      const chat = client.createChat(123, { lang: 'en' })
    } catch (error) {
      // handle error
    }
    

### loadChat

This method retrieves the chat information for a given chat ID.

**Method signature**
    
    
    loadChat(chatId: number | string): Promise<Chat>
    

**Return value**

Returns a `Chat` instance.

**Example Usage**
    
    
    try {
      const chat = await client.loadChat(1234)
    } catch (error) {
      // handle error
    }
    

### loadOngoingChat

This method is used to get the ongoing chat instance.

**Method Signature**
    
    
    loadOngoingChat(): Promise<Chat | null>
    

**Return Value**

Returns a `Chat` instance if found, or null if no ongoing chat exists. Cleans storage values if chat is not ongoing.

**Example usage**
    
    
    try {
      const chat = await client.loadOngoingChat()
    } catch (error) {
      // handle error
    }
    

### resumeChat

This method resumes a dismissed chat.

**Method signature**
    
    
    resumeChat(chatId: number | string): Promise<Chat>
    

**Return value**

Returns a chat instance.

**Example usage**
    
    
    client.resumeChat(1234)
    

### finishChat

This method changes the chat status to `finished`.

**Method signature**
    
    
    finishChat(): Promise<void>
    

**Example usage**
    
    
    try {
      await client.finishChat()
    } catch (error) {
      // handle error
    }
    

### destroyChat

This method destroys the current ongoing chat.

**Method signature**
    
    
    destroyChat(): Promise<void>
    

**Example usage**
    
    
    try {
      await client.destroyChat()
    } catch (error) {
      // handle error
    }
    

### fetchMessages

This method is used to get all the previous messages. If a failure occurs, it will return an empty array. You would use this method after the chat is connected.

**Method signature**
    
    
    fetchMessages(): Promise<MessageResponse[]>
    

**Return Value**

Returns an array of `MessageResponse`. Returns empty array on failure.

**Interfaces**
    
    
    interface MessageResponse {
      $index: number;
      $sid: string;
      $timestamp: Date;
      $userType: string;
      $userId: number;
      type: string;
      content?: string;
      event?: string;
      file?: File;
      media_id?: number;
      groupMessageId?: number;
      document?: {
        url: string;
      };
      unredacted?: string;
      buttons?: {
        title: string;
      }[];
      message?: {
        messages: string[];
        type: string;
      };
      signature: string;
      form?: {
        id: number;
        form_type: string;
        name: string;
        title: string;
        subtitle: string;
        external_form_id: string;
        smart_action_id: number;
        image: string;
      };
    }
    

**Example usage**
    
    
    const messages = client.fetchMessages()
    

### sendTextMessage

This method sends a text message.

**Method signature**
    
    
    sendTextMessage(rawContent: string): Promise<void>
    

**Example usage**
    
    
    try {
      client.sendTextMessage("hello world")
    } catch (error) {
      // handle error
    }
    

### sendFileMessage

This method sends a file message.

**Method signature**
    
    
    sendFileMessage(file: File): Promise<number>
    

**Return value**

Returns the message ID or -1 on failure.

**Example usage**
    
    
    const input = document.querySelector('input[type="file"]')
    const file = input.files[0]
    const id = client.sendFileMessage(file)
    

### sendPreviewMessage

Used to send a message preview to the agent adapter. The preview message is only displayed in the agent adapter if the `startTyping` method is called. The preview message is only displayed until either the final message is sent or the `stopTyping` method is called. For more information, see [Agent Experience - Message Preview](https://docs.cloud.google.com/contact-center/ccai-platform/docs/message-preview#message-preview).

**Method signature**
    
    
    sendPreviewMessage(content: string): Promise<void>
    

**Example usage**
    
    
    client.chat.startTyping();
    clearTimeout(stopTimer);
    stopTimer = setTimeout(() => {
        if (client.chat) {
            client.chat.stopTyping();
        }
    }, 5000);
    
    clearTimeout(previewTimer);
    const currentTime = Date.now();
    
    if (currentTime - lastPreviewTime >= 2000) {
        lastPreviewTime = currentTime;
        try {
            const response = await client.sendPreviewMessage("chat message");
        } catch (error) {
            console.error("Error sending preview message:", error);
        }
    } else {
        previewTimer = setTimeout(async () => {
            lastPreviewTime = Date.now();
            try {
                const response = await client.sendPreviewMessage("chat message");
            } catch (error) {
                console.error("Error sending debounced preview message:", error);
            }
        }, 1000);
    }
    

### startTyping

**Method signature**
    
    
    startTyping()
    

**Example usage**
    
    
    try {
      client.startTyping()
    } catch (error) {
      // handle error
    }
    

### stopTyping

**Method signature**
    
    
    stopTyping()
    

**Example usage**
    
    
    try {
      client.stopTyping()
    } catch (error) {
      // handle error
    }
    

### getChatDeflection

This method gets the chat deflection configuration.

**Method signature**
    
    
    getChatDeflection(): Promise<ChatDeflectionResponse>
    

**Return value**

Returns a `ChatDeflectionResponse` object.

**Interfaces**
    
    
    interface ChatDeflectionResponse {
      enabled: boolean;
      threshold: number;
      email: boolean;
      keep_waiting: boolean;
      external_deflection_links: {
        enabled: boolean;
        ids: number[];
      };
    }
    

**Example usage**
    
    
    try {
      const deflection = await client.getChatDeflection()
    } catch (error) {
      // handle error
    }
    

### sendChatTranscripts

Send current chat transcripts to the specified emails.

**Method signature**
    
    
    sendChatTranscripts (emails: string[]): Promise<void>
    

**Example usage**
    
    
    try {
      client.sendChatTranscripts([
        "name1@example.com",
        "name2@example.com",
      ])
    } catch (error) {
      // handle error
    }
    

### downloadChatTranscript

**Method signature**
    
    
    downloadChatTranscript(): Promise<GenerateTranscriptResponse>
    

**Return value**

Returns the transcript object.
    
    
    interface GenerateTranscriptResponse {
      status: string;
      chat_transcript_id: number;
    }
    

**Example usage**
    
    
    try {
      const resp = await client.downloadChatTranscript()
    } catch (error) {
      // handle error
    }
    

### getPdfStatus

**Method signature**
    
    
    getPdfStatus(id: number): Promise<RequestReturn>
    

**Return value**

Returns the PDF status object.

**Interfaces**
    
    
     interface RequestReturn {
        //...
        headers,
        data: PdfStatusResponse,
      }
    
      interface PdfStatusResponse {
        status: string;
        body?: File;
        failed_reason?: string;
      }
    

**Example usage**
    
    
    const response = await client.getPdfStatus(pdfId)
    // check header for status
    const status = resp.headers['x-transcript-status'];
    
    // otherwise use status on data
    const data: PdfStatusResponse = resp.data
    console.log(data.status)
    

### getChatSurvey

This method is used to get the chat survey questions.

**Method signature**
    
    
    getChatSurvey(): Promise<ChatSurveyResponse>
    

**Return value**

Returns a `ChatSurveyResponse` object.

**Interfaces**
    
    
    interface QuestionItem {
      id: number;
      type: "csat" | "star" | "free-form" | "scale" | "enumeration";
      display_text: string;
      name?: string;
      is_csat?: boolean;
      position?: number;
      valid_answers?: {
        key: string;
        value: string;
      }[]
    }
    
    interface ChatSurveyResponse {
      id?: number;
      lang?: string;
      sign_off_display_text: string;
      questions: QuestionItem[];
    }
    

**Example usage**
    
    
    try {
      const data = await client.getChatSurvey()
      console.log(data.questions)
    } catch (error) {
      // handle error
    }
    

### sendChatSurvey

This method sends a survey to the consumer.

**Method signature**
    
    
    sendChatSurvey(answers: SurveyAnswers): void
    

**Interfaces**
    
    
    interface SurveyAnswers {
      [question_id: string]: number | string;
    }
    

**Example Usage**
    
    
    try {
      await client.sendChatSurvey({
        123: "a",
        231: "b",
      })
    } catch (error) {
      // handle error
    }
    

### sendChatRate

This method sends the end-user feedback for the current chat when the chat is finished.

**Method signature**
    
    
    sendChatRate(data: RateRequest): Promise<void>
    

**Interfaces**
    
    
    interface RateRequest {
      rating: number;
      feedback?: string;
    }
    

**Example usage**
    
    
    try {
      await client.sendChatRate({
        rating: 5,
        feedback: "Very good service",
      })
    } catch (error) {
      // handle error
    }
    

### escalateChat

**Method signature**
    
    
    escalateChat(data?: EscalateRequest): Promise<void>
    

**Interfaces**
    
    
    interface EscalateRequest {
      reason?: string;
      // ...other escalation fields
    }
    

**Example usage**
    
    
    try {
      await client.escalateChat()
    } catch (error) {
      // handle error
    }
    

### trackChatEscalation

**Method signature**
    
    
    trackChatEscalation(escalationId: number, channel: string): Promise<void>
    

**Example usage**
    
    
    try {
      await client.trackChatEscalation(escalationId, channel)
    } catch (error) {
      // handle error
    }
    

### trackChatEndUserEvent

**Method signature**
    
    
    trackChatEndUserEvent(data: ChatEndUserEventRequest): Promise<void>
    

**Return Value**

Returns void.

**Interfaces**
    
    
    interface ChatEndUserEventRequest {
      end_user_name?: string;
      // ...other event fields
    }
    

**Example usage**
    
    
    try {
      await client.trackChatEndUserEvent(eventData)
    } catch (error) {
      // handle error
    }
    

### getChatHistory

**Method signature**
    
    
    getChatHistory(page?: number): Promise<ChatHistoryResponse>
    

**Return value**

Returns a `ChatHistoryResponse` object.

**Interfaces**
    
    
    interface ChatHistoryItem {
      comm_id: number;
      assigned_at: string;
      comm_type: string;
      timezone: string;
      entries: MessageResponse[];
      [key: string]: unknown;
    }
    interface ChatHistoryResponse {
      chats: ChatHistoryItem[];
      missing_chat_ids: number[];
      pagination: {
        next_page: number;
        per_page: number;
      }
    }
    

**Example usage**
    
    
    try {
      const data = client.getChatHistory(page: number)
      console.log(data)
    } catch (error) {
      console.log(error)
    }
    

## Emails

Methods for handling support emails.

### createEmails

**Method signature**
    
    
    createEmail(menuId: number | string, data: EmailRequest): Promise<EmailResponse>
    

**Return value**

Returns an `EmailResponse` object on failure or success.

**Interfaces**
    
    
    interface EmailRequest {
      name?: string;
      email: string;
      content: string;
      lang?: string;
      files?: File[];
      recaptcha?: string;
    }
    
    interface EmailResponse {
      id: number;
      type: string;
      status: string;
      fail_reason: string;
      attachment_count: number;
    }
    

**Example usage**
    
    
    try {
      await client.createEmail(123, {
        lang: "en",
        name: "User name",
        email: "name@example.com",
        content: "description of the question",
        files: input.files,
      })
    } catch (error) {
      console.log(error.message)
    }
    

### getProhibitedFileTypes

**Method Signature**
    
    
    getProhibitedFileTypes(): Promise<FileTypeItem[]>
    

**Return value**

Returns an array of `FileTypeItem`.

**Interfaces**
    
    
    interface FileTypeItem {
      extension: string;
      description: string;
    }
    

**Example usage**
    
    
    try {
      const types = await client.getProhibitedFileTypes()
    } catch (error) {
      // handle error
    }
    

## Screen Share

Methods for handling the Screen Share capability.

### createCobrowseCode

This method creates a Screen Share code.

**Method signature**
    
    
    createCobrowseCode(lang?: string, customData?: Record<string, string>): Promise<string>
    

**Return value**

Returns a Screen Share code string or empty string on failure.

**Example usage**
    
    
    const code = await client.createCobrowseCode()
    // 123456
    

### startCobrowse

**Method signature**
    
    
    startCobrowse(from?: string): Promise<void>
    

**Example usage**
    
    
    try {
      await client.startCobrowse()
    } catch (error) {
      // handle error
    }
    

### restoreCobrowseSession

This method attempts to restore a previously active Screen Share session after the browser window is reopened or the widget is reloaded.

**Method signature**
    
    
    restoreCobrowseSession(): Promise<void>
    

**Return value**

Returns `Promise<void>`. This method is a no-op (it returns immediately without error) if Screen Share isn't enabled for your instance or if no previous Screen Share session exists in storage.

**Note:** This method doesn't throw an error. If an error occurs during Screen Share session restoration, the method logs the error internally, clears the stored Screen Share session, then returns cleanly. You don't need to handle errors with `try` and `catch`.

**Example usage**
    
    
    // Safe to call unconditionally. Will no-op if cobrowse is not enabled
    // or if no previous session exists
    await client.restoreCobrowseSession()
    

### getMessageAttachment

**Method signature**
    
    
    getMessageAttachment(message: MessageResponse): Promise<File | null>
    

**Return value**

Returns a `File` object if found, or null if not applicable.

**Example usage**
    
    
    try {
      const file = await client.getMessageAttachment(message);
    } catch (error) {
      // handle error
    }
    

## Post session virtual agents

Methods for handling post session virtual agents.

### updatePostSession

Updates the post-session virtual agent status for the ongoing chat. Use this to signal readiness, progress, or completion of a post-session virtual agent flow. This method returns immediately as a no-op if `postSessionStatus` is `FINISHED` or `WAITING` because those transitions are handled internally. This method has internal retry logic specifically for the `IN_PROGRESS` status on a 400 response, so callers don't need to implement their own retry for that case.

**Method signature**
    
    
    updatePostSession(postSessionStatus: PostSessionStatus, optInSelection?: boolean): Promise<void>
    

**Interfaces**
    
    
    enum PostSessionStatus {
      READY = 'ready',
      IN_PROGRESS = 'in_progress',
      WAITING = 'waiting',
      FINISHED = 'finished',
    }
    

**Example usage**
    
    
    try {
      // Without opt-in selection
      await client.updatePostSession(PostSessionStatus.READY)
    
      // With opt-in selection
      await client.updatePostSession(PostSessionStatus.READY, true)
    } catch (error) {
      // handle error (e.g., show a notification to the user)
    }
    

**Related interface**
    
    
    interface ChatResponse {
      //...
      post_session_required?: boolean;
      post_session_opt_in_required?: boolean;
      post_session_transfer_status?: string;
    }
    

  * `post_session_required`: Post session required after a chat.
  * `post_session_opt_in_required`: If opt-in is enabled.
  * `post_session_transfer_status`: A `PostSessionStatus` enumeration.



## Debugging

Methods for debugging the SDK.

### getLogs

Gets the internal debug logs collected by the SDK, including bridge-level and root-level logs. This is useful for troubleshooting integration issues.

**Method signature**
    
    
    getLogs(): Promise<{ bridgeLogs: LogHistoryData[], rootLogs: LogHistoryData[] }>
    

**Return value**

Returns an object containing two arrays of `LogHistoryData`.

**Interfaces**
    
    
    interface LogHistoryData {
      date: string;
      channel: string;
      level: string;
      args: any[];
    }
    

**Note:** The system fetches bridge logs first, because the fetch produces a root log entry. As a result, rootLogs intentionally captures that final log.

**Granularity**

Each `LogHistoryData` entry captures a single log event with the following fields:

  * `date`. The ISO 8601 timestamp of the event.

  * `channel`. The SDK module that emitted it—for example, the top-level client, the chat layer, the Screen Share layer, or the real-time provider.

  * `level`. The log severity. Values include `debug`, `info`, `warn`, and `error`.

  * `args`. The raw arguments that the log call captured.




The following code example shows a log entry:
    
    
    {
      "date": "2026-05-08T14:02:13.412Z",
      "channel": "Provider",
      "level": "info",
      "args": ["chat connected", { "chatId": 4421 }]
    }
    

The set of channels and message contents might change between SDK releases. Treat the logs as a debugging aid, not a stable parsing target. Don't build production logic that depends on specific channel names or message strings.

**Scope and recommended use**

The `getLogs` method returns SDK-internal records that can help diagnose integration issues with the headless web SDK itself. Its primary use case is support diagnostics. When an end-user reports an issue, your application can capture the result of `getLogs` and attach it to the support ticket sent to Contact Center AI Platform (CCAI Platform).

The returned logs don't include the following:

  * Your host page's application telemetry, business events, or user navigation.

  * Network failures that the browser doesn't surface to the SDK—for example, CORS, mixed-content, or certificate errors.

  * Server-side request traces or backend details beyond the HTTP status returned to the SDK.




The `getLogs` method isn't a replacement for your own observability tooling. Google recommends pairing the SDK with the following:

  * A browser-side error or RUM tracker—for example, Sentry, Datadog Browser RUM, New Relic Browser, or equivalent.

  * Server-side logging on your authentication endpoint, which is the `authenticate` callback that the SDK calls.

  * Application-level listeners on `chat.disconnected`, `chat.timeout`, and `chat.ended` if you need to forward chat lifecycle signals to your own telemetry pipeline.




**Example usage**
    
    
    try {
      const { bridgeLogs, rootLogs } = await client.getLogs()
      console.log('Bridge logs:', bridgeLogs)
      console.log('Root logs:', rootLogs)
    } catch (error) {
      // handle error
    }
    

### printLogs

Prints all internal debug logs directly to the browser console. This is a convenience method that calls `getLogs()` internally and formats the output.

**Method signature**
    
    
    printLogs(): Promise<void>
    

**Example usage**
    
    
    try {
      await client.printLogs()
    } catch (error) {
      // handle error
    }
    

## Miscellaneous

Miscellaneous SDK methods.

### runTrigger

**Method signature**
    
    
    runTrigger(cb: (trigger: TriggerItem) => void): Promise<void>
    

**Example usage**
    
    
    client.runTrigger((trigger: TriggerItem) => {
      // code to run for given trigger
    })
    

### getAfterHourMessage

**Method signature**
    
    
    getAfterHourMessage(lang?: string): Promise<string>
    

**Return value**

Returns a string containing a configured message.

**Example usage**
    
    
    try {
      const message: string = await client.getAfterHourMessage()
    } catch (error) {
      // handle error
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
