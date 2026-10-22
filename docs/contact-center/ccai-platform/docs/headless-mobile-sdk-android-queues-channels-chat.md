---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat/
title: Headless mobile SDK for Android: Queues, channels, and chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:32.452203+00:00
---

# Headless mobile SDK for Android: Queues, channels, and chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless mobile SDK for Android: Queues, channels, and chat Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to make support entry points (queues and channels) available in your app, and how to drive the full chat lifecycle: starting, resuming, sending messages and attachments, indicating typing, redacting sensitive data, escalating to human agents, and ending the session.

## Before you begin

Set up the SDK. For more information, see [Headless mobile SDK for Android: getting started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk).

## Select queues and channels

  * A queue usually represents a support entry point, such as "Billing", "Technical Support", or "VIP Support".

  * Each queue can offer one or more of the following channels:

    * Chat

    * Instant call (voice)

    * Scheduled call

    * Email

    * External deflection links (links to your self-service pages or other channels)




Queues and channel availability are configured by administrators in the **Contact Center AI Platform Admin Portal**.

### How it looks in your app

In your app, a typical flow is:

  1. You add a support entry point in your app (for example, a **Help** tab or a **Contact Us** button).

  2. When the user taps it, you fetch the queue menu using the SDK and render your own menu UI.

  3. When the user chooses a queue, you inspect its available channels.

  4. Your app shows those channels to the user (for example, **Chat now** , **Call now** , **Schedule a call** , **Email us** , **Visit Help Center**).

  5. When the user selects a channel, you call the corresponding SDK API.




**Fetching queue menus from the SDK:**

The SDK provides `queueMenuService` to fetch queue menus. The `get` method returns a `MenuResult` containing a `List<QueueMenu>` and a `Boolean` indicating direct access. You can either fetch the full menu tree or use a direct access key to jump directly to a specific queue:
    
    
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaikit.MenuResult
    import com.ccaiplatform.ccaikit.QueueMenu
    
    // Fetch the full queue menu tree
    val menuResult: MenuResult? = CCAI.queueMenuService?.get()
    
    // Or fetch a specific queue using a Direct Access Key
    val menuResult: MenuResult? = CCAI.queueMenuService?.get(key = "billing_vip")
    

The optional `key` parameter lets you bypass the full queue menu and jump the user directly to a specific queue. In the CCAI Platform platform, this is achieved with a direct access point (DAP).

A DAP can be configured by administrators in the CCAI Platform portal in the following way:

  1. Go to **Settings** > **Queue** > Select any queue from the menu structure.

  2. From the **Access Point** section, click + **Create direct access point**.

  3. Enter the key in the text form.

  4. Click **Save**.




**`QueueMenu` data structure:**

Each `QueueMenu` contains:

Property | Type | Description  
---|---|---  
`id` | Int | The unique identifier for this queue.  
`name` | String? | The display name (for example, "Billing Support").  
`children` | List<QueueMenu> | Sub-menus (empty list if this is a leaf node).  
`channels` | Channels | Available channels for this queue.  
`hidden` | Boolean | Whether this queue should be hidden from consumers (administrator configured).  
`position` | Int? | Server-defined display position - preserves administrator portal ordering.  
`settings` | List<QueueMenuSetting>? | Queue-level settings configured in the administrator portal.  
`redirectionExtra` | QueueMenuRedirection? | Automatic redirection metadata when configured (see [Redirect and deflection](https://support.ujet.co/hc/en-us/articles/57485702631961-Headless-Mobile-SDK-v3-for-Android-Queues-Channels-and-Chat#redirectanddeflection)).  
`deflectionFrom` | List<QueueMenuDeflection>? | Deflection configuration for this queue (see [Deflection](https://support.ujet.co/hc/en-us/articles/57489070509721-Headless-Mobile-SDK-v3-for-Android-Smart-Actions-Attachments-and-Deflection#deflectionafterhoursandovercapacity\)%20in%20\[Headless%20Mobile%20SDK%20for%20Android:%20Smart%20Actions,%20Attachments,%20and%20Deflection\]\(https://support.ujet.co/hc/en-us/articles/57489070509721-Headless-Mobile-SDK-v3-for-Android-Smart-Actions-Attachments-and-Deflection)).  
  
The `Channels` data class has these properties:

Property | Type | Description  
---|---|---  
`chat` | ChatChannel? | Chat channel configuration (`null` if chat isn't available for this queue).  
`voiceCall` | VoiceCallChannel? | Voice call channel configuration (`null` if voice isn't available). Contains flags such as `scheduleEnabled` and recording preferences.  
`email` | EmailChannel? | Email channel configuration (`null` if email isn't available). Access the address using `channels.email?.email`.  
`externalDeflectionLink` | ExternalDeflectionLink? | External deflection link configuration (`null` if not available). Access the URL using the structured type's properties.  
  
**`VoiceCallChannel` fields (capability and deflection metadata):**
    
    
    // VoiceCallChannel.kt (simplified)
    data class VoiceCallChannel(
        val instantEnabled: Boolean,            // Live voice call allowed now
        val preSessionSmartAction: Boolean,     // Per-channel pre-session smart action flag
        val scheduleEnabled: Boolean,           // Scheduled calls supported
        val recordingOption: RecordingOption?,  // ALWAYS / NEVER / ASK_USER
        val voicemailReason: String?,
        val phoneNumber: String?,
        val scheduleDeflectionType: String?,
        val deflected: Boolean?,
        val deflectedReason: String?
    )
    

**Implementation example:**
    
    
    fun showAvailableChannels(queueMenu: QueueMenu) {
        val channels = queueMenu.channels
    
        // Update your custom UI based on what the SDK says is active
        chatButton.isVisible = channels.chat != null
        callButton.isVisible = channels.voiceCall != null
        emailButton.isVisible = channels.email != null
    
        // External deflection link
        if (channels.externalDeflectionLink != null) {
            deflectionLinkButton.isVisible = true
            deflectionLinkButton.setOnClickListener {
                openAndroidBrowser(channels.externalDeflectionLink!!)
            }
        }
    }
    

**Fetching wait times:**

You can also retrieve estimated wait times for a specific queue:
    
    
    // Fetch wait time for a specific queue
    val waitTime = CCAI.queueMenuService?.getWaitTimes(menuId = queueMenu.id)
    
    // waitTime contains:
    // - chat: estimated wait time for chat (in seconds)
    // - voiceCall: estimated wait time for voice call (in seconds)
    

**Note:** The `getWaitTimes` method returns a `QueueMenuWaitTimeResponse`. The exact structure and property names may vary; verify against the SDK's actual response when testing.

### Single-channel queues

If a queue offers only one channel (for example, email only), you can:

  * Skip the channel selection step and go straight to the appropriate UI.

  * Or you can still show the available channel explicitly if that makes more sense in your UX.




The SDK's configuration and metadata tells you which channels are allowed; your app decides **how** to show them.

### Redirect and deflection

Queues can be configured to **redirect** or **deflect** users to alternate destinations:

  * Redirect to a different queue.

  * Open a phone number or URL.

  * Present a message and alternate options.




When the SDK indicates a redirect or deflection for the selected queue (using the `redirectionExtra` and `deflectionFrom` properties on `QueueMenu`), your app should:

  * Show any message text configured in CCAI Platform.

  * Present any options that are configured (for example, **Call this number** or **Visit our help center**).

  * Perform the selected action.




For deeper handling of after-hours and over-capacity deflection, see [Headless Mobile SDK for Android: Smart Actions, Attachments, and Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions)

## Channels

In the Headless Mobile SDK, your CCAI Platform administrator portal acts as the source of truth for your support operations. Administrators configure which support channels (such as chat, voice, email, or helpful links) are available for different support queues (such as "Billing" or "Tech Support").

The SDK's job is to securely fetch this configuration and hand it to your app. Your app's job is to read that configuration and draw the appropriate user interface.

**Tip:** For several channels in a headless architecture, the SDK tells you what is allowed and provides the routing metadata (for example, enabled flags, email addresses, and deflection URLs). Your app is responsible for building the UI and calling the corresponding SDK service APIs for the selected channel.

### Inspecting available channels

**What the SDK provides:** A real-time snapshot of which support channels are active and available for the specific queue the user selected, respecting your portal's business hours and capacity limits.

**What you build:** The UI menu (buttons, lists, or cards) that displays these available options to the user.

**Implementation example:** The following Kotlin code takes the queue the user just tapped and inspects the `Channels` data class to see which channels are enabled. It then decides which buttons to show on the screen.
    
    
    // Assuming 'selectedMenu' is a QueueMenu returned by the SDK
    fun setupChannelMenu(selectedMenu: QueueMenu) {
        val channels = selectedMenu.channels
    
        if (channels.chat != null) {
            showChatNowButton()
        }
    
        if (channels.voiceCall != null) {
            showCallNowButton()
        }
    
        if (channels.email != null) {
            showEmailUsButton()
        }
    
        if (channels.externalDeflectionLink != null) {
            showHelpCenterLinks()
        }
    }
    

The following sections cover chat in detail. For voice, screen share, scheduled call, email, and external deflection links, see [Headless Mobile SDK for Android: Voice, Screen Share, Scheduled Call, and Email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice)

## Chat service API

The `chatService` manages the full chat lifecycle. The core methods you use most frequently are:

Method | Description  
---|---  
`start` | Starts a new chat session with a `ChatRequest`.  
`sendMessage` | Sends a message (text, image, video, or form event).  
`typing` | Updates the typing indicator.  
`endChat` | Ends the current chat session.  
`resumeChat` | Resumes a previously established chat session.  
`escalateToHumanAgent` | Transfers from a virtual agent to a human agent.  
`checkStatus` | Refreshes the current chat status from the server.  
**Note:** The `chatService` exposes 23 methods in total; this includes smart action tracking (`notifySmartActionReceived`, `updateSmartActionStatus`), form handling (`fetchWebForm`, `getCustomFormDetails`, `submitCustomForm`), post-session management (`startPostSession`, `readyPostSession`), transcript download (`downloadChatTranscript`), and attachment download (`downloadMedia`). For complete method signatures and parameters, see the Headless Mobile SDK - Android API Reference.

### Chat Request and Chat Response data structures

The `ChatRequest` data class contains the configuration for starting a new chat:
    
    
    data class ChatRequest(
        val chat: Chat,                     // Required: session configuration
        val isScreenShareable: Boolean?     // Optional: enable screen share for this session
    )
    
    data class Chat(
        val menuId: Int,                    // Required: queue menu ID
        val languageCode: String? = "en",   // Optional: language code override (serialized as "lang"; defaults to "en")
        val ticketId: String? = null,       // Optional: associate with existing ticket
        val greeting: String? = null,       // Optional: custom greeting message
        val customData: CustomData? = null, // Optional: structured custom data
        val displayOrderInAdapter: List<String>? = null
    )
    

The `ChatResponse` is returned when you start or resume a chat. The properties you reference most in this document include:

  * `id` \- the unique chat session identifier.

  * `status` \- the current chat status (queued, active, ended, etc.).

  * `agent` / `virtualAgent` \- the assigned human or virtual agent.

  * `postSessionRequired` \- whether a post-session flow (CSAT, survey, VA) should be triggered.

  * `redactionEnabled` \- whether automatic PII redaction is active for this session.


**Note:** `ChatResponse` contains 20 properties in total (including `providerType`, `region`, `allAgents`, `allVirtualAgents`, `menus`, `features`, `timeoutAt`, `statusText`, `providerChannelId`, `postSessionOptInRequired`, `postSessionTransferStatus`, `csatSetting`, `surveyEnabled`, and more). For the full data class definition, see the Headless Mobile SDK - Android API Reference.

### Starting a chat session

**Warning:** Always call `getLastChatInProgress()` before starting a new chat. If an earlier session is still active (for example, the app was force-quit mid-conversation, or the user switched accounts), starting a second chat fails or produces undefined behavior. This check is especially critical when `userId` changes between sessions.
    
    
    // Before every call to chatService.start()
    lifecycleScope.launch {
        val existing = CCAI.chatService?.getLastChatInProgress()
        if (existing != null) {
            // An active session already exists - resume or end it first
            CCAI.chatService?.resumeChat(existing)
            return@launch
        }
    }
    

To start a chat session, use the `chatService` with a `ChatRequest` specifying the queue's menu ID.

**Minimal:**
    
    
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaichat.ChatRequest
    import com.ccaiplatform.ccaichat.Chat
    
    // If screen share is initialized, pass isScreenShareable for agent visibility
    val chatRequest = ChatRequest(
        chat = Chat(menuId = 123),
        isScreenShareable = CCAI.screenShareService != null
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.start(chatRequest)
            // Chat started, navigate to your custom chat screen
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to start chat: ${e.message}")
        }
    }
    

**With explicit language and custom data:**
    
    
    val chatRequest = ChatRequest(
        chat = Chat(menuId = 123, languageCode = "en")
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.start(chatRequest)
            // Chat started - navigate to your custom chat screen
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to start chat: ${e.message}")
        }
    }
    

### Resuming a chat session

Resume a previously established chat session using a `ChatResponse` object:
    
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.resumeChat(chat)
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to resume chat: ${e.message}")
        }
    }
    

### Chat queue management

You can enqueue the current chat for later retrieval or check for existing in-progress chats:
    
    
    // Enqueue the current chat (automatically calls checkStatus() after enqueuing)
    lifecycleScope.launch {
        try {
            CCAI.chatService?.enqueueCurrentChat()
            Log.d("CCAI", "Chat enqueued successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to enqueue chat: ${e.message}")
        }
    }
    
    // Check for an existing in-progress chat
    lifecycleScope.launch {
        try {
            val chat = CCAI.chatService?.getLastChatInProgress()
            if (chat != null) {
                Log.d("CCAI", "Found ongoing chat: ${chat.id}")
            } else {
                Log.d("CCAI", "No ongoing chat found")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to get last chat: ${e.message}")
        }
    }
    
    // Retrieve previous chat history with pagination
    lifecycleScope.launch {
        try {
            val previousChats = CCAI.chatService?.getPreviousChats(currentPage = 1)
            if (previousChats != null) {
                Log.d("CCAI", "Found ${previousChats.messages.size} previous messages")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to get previous chats: ${e.message}")
        }
    }
    

### Sending messages

The `sendMessage` method supports multiple message types through the `OutgoingMessageContent` sealed class:
    
    
    sealed class OutgoingMessageContent {
        data class Text(val content: String) : OutgoingMessageContent()
        data class Photos(
            val images: List<Uri>,
            val smartAction: SmartAction? = null
        ) : OutgoingMessageContent()
        data class Videos(
            val videos: List<Uri>,
            val smartAction: SmartAction? = null
        ) : OutgoingMessageContent()
        data class FormComplete(
            val type: String? = null,
            val signature: String? = null,
            val data: FormCompleteEventData
        ) : OutgoingMessageContent()
        data class ScreenShare(
            val event: String,
            val detail: ScreenShareResponse? = null
        ) : OutgoingMessageContent()
    }
    

For photos and videos, pass local `Uri` values for files selected or captured by your app. Avoid holding large media assets in memory while the user is waiting in queue or while an upload is pending.

**Usage examples:**
    
    
    // Send text message
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(OutgoingMessageContent.Text("Hello world"))
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message: ${e.message}")
        }
    }
    
    // Send image message
    val imageUris: List<Uri> = listOf(selectedImageUri)
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Photos(
                    images = imageUris,
                    smartAction = null
                )
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send image: ${e.message}")
        }
    }
    
    // Send video message
    val videoUris: List<Uri> = listOf(selectedVideoUri)
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Videos(
                    videos = videoUris,
                    smartAction = null
                )
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send video: ${e.message}")
        }
    }
    
    // Send form completion event
    // Note: status is a nullable String (for example, "success" or "failure").
    val formCompleteData = FormCompleteEventData(
        smartActionId = 123,
        status = "success",
        timestamp = "2024-01-01T12:00:00Z",
        details = FormCompleteDataDetails(message = "Form submitted successfully")
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.FormComplete(data = formCompleteData)
            )
            Log.d("CCAI", "Form completion event sent")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send form completion: ${e.message}")
        }
    }
    

The `ScreenShare` message type is used to send screen sharing events and responses to the server. Available screen share events include:

  * `screenShareRequestedFromAgent` \- agent requested screen sharing

  * `screenShareRequestedFromEndUser` \- end user requested screen sharing

  * `screenShareCodeGenerated` \- screen share code was generated

  * `screenShareFailed` \- screen sharing failed

  * `screenShareStarted` \- screen sharing session started

  * `screenShareEnded` \- screen sharing session ended


**Note:** If redaction is enabled (via the `redactionEnabled` property in `ChatResponse`), sensitive information in plain text messages is automatically redacted before being sent to the agent. See [_Message redaction_](https://support.ujet.co/hc/en-us/articles/57485702631961-Headless-Mobile-SDK-v3-for-Android-Queues-Channels-and-Chat#messageredaction) for details.

### Typing indicators and message previews

Update the typing status and send message previews while the user is typing:
    
    
    // Update typing indicator
    CCAI.chatService?.typing(true)   // Start typing
    CCAI.chatService?.typing(false)  // Stop typing
    
    // Send message preview
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessagePreview("Typing...")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message preview: ${e.message}")
        }
    }
    
    // Example: Send preview as user types
    fun onTextChanged(text: String) {
        lifecycleScope.launch {
            try {
                CCAI.chatService?.sendMessagePreview(text)
            } catch (e: Exception) {
                Log.e("CCAI", "Failed to send preview: ${e.message}")
            }
        }
    }
    

### Message redaction

Automatic redaction of sensitive information (PII, credit card numbers, etc.) is supported for plain text chat messages and message previews.

**Redaction configuration:**

  * Controlled by the `redactionEnabled` property in `ChatResponse`.

  * Configured in the portal under **Settings** > **Chat Settings** > **Automatic Redaction**.

  * When enabled, sensitive data is automatically replaced with placeholders before being sent to agents.



    
    
    // Redaction is automatically handled, use sendMessage as usual
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendMessage(
                OutgoingMessageContent.Text("My phone number is 4155553423")
            )
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send message: ${e.message}")
        }
    }
    

**Note:** Redaction only applies to plain text messages. Redaction is automatically enabled or disabled based on portal configuration. The redaction status is available in `ChatResponse` after starting or resuming a chat. Message previews with timestamps older than the last sent preview are automatically skipped.

### Ending and escalating chats
    
    
    // End the current chat session
    lifecycleScope.launch {
        try {
            CCAI.chatService?.endChat()
            Log.d("CCAI", "Chat ended successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to end chat: ${e.message}")
        }
    }
    
    // Escalate to a human agent
    lifecycleScope.launch {
        try {
            CCAI.chatService?.escalateToHumanAgent()
            Log.d("CCAI", "Chat escalated to human agent")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to escalate chat: ${e.message}")
        }
    }
    
    // Escalate with deflection options
    val escalationOption = ChatEscalationOption(
        escalationId = 123,
        deflectionChannel = "email"
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.escalate(option = escalationOption)
            Log.d("CCAI", "Chat escalated successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to escalate chat: ${e.message}")
        }
    }
    
    // Check the current chat status
    lifecycleScope.launch {
        try {
            CCAI.chatService?.checkStatus()
            Log.d("CCAI", "Status check completed successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to check status: ${e.message}")
        }
    }
    

### Chat events

Send chat events to the server for tracking user interactions. `ChatEvent.payload` is a non-nullable `Map<String, String>` — both keys and values must be strings.
    
    
    val event = ChatEvent(
        name = "form_received",
        payload = mapOf("name" to "contact_form")
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.sendEvent(event)
            Log.d("CCAI", "Event sent successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to send event: ${e.message}")
        }
    }
    

Common event use cases include form interactions ("form_received", "form_clicked"), smart action events ("smart_action_received", "smart_action_clicked"), and custom user interactions for analytics.

## Module-specific build considerations

Consider the following for a module-specific build.

### Minimum Sdk level

The `CCAIChatRed` and `CCAICallRed` media-layer modules require **min Sdk = 23** (Android 6.0). If your app declares a lower `minSdkVersion`, Gradle will fail to merge manifests. Raise your `min Sdk` to at least 23 in `app/build.gradle.kts`:
    
    
    android {
        defaultConfig {
            minSdk = 23
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
