---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-advanced-topics/
title: Headless mobile SDK for Android: Advanced topics, localization, and post-session flows \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:12.968661+00:00
---

# Headless mobile SDK for Android: Advanced topics, localization, and post-session flows  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-advanced-topics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless mobile SDK for Android: Advanced topics, localization, and post-session flows Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to integrate and customize the Headless Mobile SDK in your Android application. It covers localization, post-session flows, and other advanced topics.

**Note:** This document assumes you have completed the integration steps in [Headless Mobile SDK for Android: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started) through [Headless Mobile SDK for Android: Smart actions, attachments, and deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions). Many of the patterns here apply to all sessions - chat, voice, and scheduled - regardless of which channel(s) you implemented.

## Post-session flows (post-session VA, surveys, and CSAT)

When a live chat or voice call ends, contact centers often want to collect feedback or offer automated follow-ups. CCAI Platform supports three types of post-session experiences:

  1. **Post-session virtual agent (VA)** : An automated chatbot that continues the conversation after the human agent disconnects.

  2. **Surveys** : A multi-question form tailored to the specific queue.

  3. **CSAT (customer satisfaction)** : A rating (for example, 1–5 stars) and optional text feedback.




### Enforcing the hierarchy

It is common for admins to configure overlapping rules in the portal (for example, turning on CSAT globally, but also turning on a post-session VA for the Billing queue).

**What the SDK provides** : A strict conflict-resolution engine. The SDK evaluates the portal rules and ensures that only **one** post-session flow triggers per session, strictly adhering to the following hierarchy:

  * The post-session priority: Post-session VA > Surveys > CSAT

    * _Example: If both CSAT and post-session VA are enabled for a queue, the user will ONLY see the post-session VA._



**What you build** : A listener that waits for the session to end, asks the SDK which flow won the hierarchy evaluation, and draws the corresponding screen. You don't need to write complex if-else logic to figure out which experience wins; the SDK does that math for you.

#### Implementation example

This snippet demonstrates how your app should listen to the end of a session and ask the SDK what to do next.
    
    
    // Called when the active chat or call ends
    fun handleSessionEnded(postSessionFlow: PostSessionFlow?) {
        // 1. Check if there is a required post-session flow.
        //    The SDK has already calculated the hierarchy (VA > Survey > CSAT).
        val flow = postSessionFlow
        if (flow == null) {
            // No feedback required. Safely close the support UI.
            closeSupportExperience()
            return
        }
    
        // 2. Route to the winning flow returned by the SDK.
        when (flow.type) {
            PostSessionType.VIRTUAL_AGENT -> transitionToPostSessionVA()
            PostSessionType.SURVEY -> showSurveyScreen(flow)
            PostSessionType.CSAT -> showCSATScreen(flow)
        }
    }
    

### Transitioning into the post-session phase

Regardless of which flow wins the hierarchy, you must call two shared lifecycle methods on the `chatService` to signal the CCAI Platform platform that the post-session phase has begun.

**What the SDK provides** : Lifecycle methods to transition the session into and through the post-session phase (`startPostSession`, `readyPostSession`).

**What you build** : The orchestration logic that calls these methods at the correct points in your post-session UI flow.

#### Implementation example

This code transitions the session through the two post-session lifecycle stages.
    
    
    lifecycleScope.launch {
        // Step 1: Start the post-session process (updates status to "in_progress")
        try {
            val postSessionResponse = CCAI.chatService?.startPostSession()
            if (postSessionResponse != null) {
                Log.d("CCAI", "Post-session started successfully: ${postSessionResponse.id}")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to start post-session: ${e.message}")
        }
    
        // Step 2: Signal that post-session is ready (updates status to "ready")
        try {
            val readyResponse = CCAI.chatService?.readyPostSession()
            if (readyResponse != null) {
                Log.d("CCAI", "Post-session ready: ${readyResponse.id}")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to prepare post-session: ${e.message}")
        }
    }
    

After the platform acknowledges the transition, proceed to this specific flow.

### Post-session state fields on `ChatResponse`

Two post-session orchestration fields on `ChatResponse` drive the transition logic:

  * `postSessionTransferStatus: String?` \- The current state of the post-session transfer (for example, `"in_progress"`, `"ready"`, `"completed"`). The platform keys the orchestration state machine off this field: `startPostSession()` moves it to `"in_progress"`, `readyPostSession()` moves it to `"ready"`, and you observe this value on subsequent `ChatResponse` emissions (from the chat service chat flow) to confirm the platform-side transition.

  * `postSessionOptInRequired: Boolean?` \- Whether the user must explicitly opt in to the post-session flow before it runs. When `true`, surface an opt-in prompt in your UI and only call `startPostSession()` after the user consents. When `false` or `null`, the opt-in check isn't required and you can transition straight into the post-session flow.



    
    
    suspend fun orchestratePostSession(chat: ChatResponse) {
        // 1. Honor opt-in gating if required
        if (chat.postSessionOptInRequired == true) {
            val consented = presentPostSessionOptIn()
            if (!consented) {
                closeSupportExperience()
                return
            }
        }
    
        // 2. Drive the state machine
        CCAI.chatService?.startPostSession()   // → "in_progress"
        CCAI.chatService?.readyPostSession()   // → "ready"
    
        // 3. Observe postSessionTransferStatus on subsequent chat updates
        //    to confirm the transfer completed before rendering the winning flow.
    }
    

  * `postSessionRequired` tells you whether _any_ post-session flow is configured for the session.

  * `postSessionOptInRequired` tells you whether explicit user consent is required before running it.

  * `postSessionTransferStatus` tells you where the platform is in the transition lifecycle.




All three are independent - always check each one.

### Post-session virtual agent (highest priority)

**What the SDK provides** : The transition state to shift the session from a human agent back to an automated bot, and the routing of the bot's messages.

**What you build** : Nothing entirely new. Because the post-session VA operates as a chat, you keep your existing custom chat UI open and let it handle the incoming automated messages just like it handled the human agent's messages.

#### Implementation example

If the SDK signals a transition to a post-session VA, you update your chat UI to reflect the change.
    
    
    fun transitionToPostSessionVA() {
        // Keep your chat UI open, but update the visual context
        myChatAdapter.addSystemMessage(
            "You are now speaking with our Virtual Assistant"
        )
        agentNameTextView.text = "Virtual Assistant"
        agentAvatarImageView.setImageResource(R.drawable.ic_bot_avatar)
    
        // The SDK will automatically start piping the VA's messages into
        // your standard chat message observer (messagesReceived).
    }
    

### Surveys (medium priority)

**What the SDK provides** : The `rateService` exposes methods to retrieve survey questions and submit answers for a communication session. Survey questions are configured by the administrator for each queue and can include multiple question types (CSAT, star rating, free-form text, enumeration, numeric scale).

**What you build** : A dynamic form that fetches the survey, loops through the questions, renders the appropriate UI (such as radio buttons, star ratings, or text fields) for each, validates that required fields are filled out, and packages the answers to send back.

#### Key types
    
    
    // Survey response from getSurvey()
    data class Survey(
        val id: Int?,
        val lang: String?,
        val questions: List<SurveyQuestion>?,
        val signOffText: String?  // "Thank you" message to show after submission
    )
    
    // Request payload for sendSurvey()
    data class SurveyRequest(
        val answers: Map<Int, String>  // Maps question IDs to answer values
    )
    

#### Implementation example

This code fetches survey questions from the `rateService`, renders them in a custom fragment, and submits the answers.
    
    
    fun showSurveyScreen(communicationId: Long) {
        val rateService = CCAI.rateService ?: return
    
        lifecycleScope.launch {
            try {
                // 1. Fetch the survey questions for this session
                val survey = rateService.getSurvey(
                    communicationId = communicationId,
                    communicationType = "chats"
                ).getOrThrow()
    
                // 2. Present your custom survey UI
                val surveyFragment = MyCustomSurveyFragment.newInstance(
                    survey.questions.orEmpty()
                )
                surveyFragment.onSubmit = { answersMap ->
                    lifecycleScope.launch {
                        try {
                            // 3. Submit the answers
                            val request = SurveyRequest(answers = answersMap)
                            rateService.sendSurvey(
                                communicationId = communicationId,
                                communicationType = "chats",
                                answers = request
                            ).getOrThrow()
                            rateService.clear()
                            closeSupportExperience()
                        } catch (e: Exception) {
                            Log.e("CCAI", "Failed to submit survey: ${e.message}")
                        }
                    }
                }
                supportFragmentManager.beginTransaction()
                    .replace(R.id.container, surveyFragment)
                    .addToBackStack(null)
                    .commit()
            } catch (e: Exception) {
                Log.e("CCAI", "Failed to load survey: ${e.message}")
                closeSupportExperience()
            }
        }
    }
    

### CSAT - customer satisfaction (lowest priority)

**What the SDK provides:** The `rateService` exposes a `rate()` method to submit a CSAT score and optional feedback for a communication session. The rating is typically a 1–5 integer value.

**What you build:** The visual rating screen (such as a row of tappable stars or a 1–5 number scale), a text field if feedback is allowed, and a **Submit** button.

#### Key types
    
    
    // Request payload for rate()
    data class RatingRequest(
        val rating: Int? = null,      // Typically 1-5
        val feedback: String? = null  // Optional qualitative feedback
    )
    

#### Implementation example

After the user taps a star rating and writes their feedback, you pass those values to the `rateService`.
    
    
    fun submitCSATFeedback(communicationId: Long, rating: Int, comment: String?) {
        val rateService = CCAI.rateService ?: return
        submitButton.isEnabled = false
        progressBar.isVisible = true
    
        lifecycleScope.launch {
            try {
                val request = RatingRequest(
                    rating = rating,
                    feedback = comment?.trim()?.takeIf { it.isNotEmpty() }
                )
                rateService.rate(
                    communicationId = communicationId,
                    communicationType = "chats",
                    request = request
                ).getOrThrow()
                rateService.clear()
                showThankYouScreen()
            } catch (e: Exception) {
                showErrorToast("Failed to submit feedback. Please try again.")
            } finally {
                submitButton.isEnabled = true
                progressBar.isVisible = false
            }
        }
    }
    

### Downloading chat transcripts

**What the SDK provides:** A method to download the chat transcript as a PDF file.

**What you build** : The download button in your UI and the file-handling logic (save, share, or preview).

#### Implementation example

This code demonstrates the Android transcript download approach - retrieving the PDF as a file and then saving, sharing, or previewing it in your app.
    
    
    // Download to a file destination
    val documentsDir = getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS)
    val transcriptFile = File(documentsDir, "chat_transcript.pdf")
    
    lifecycleScope.launch {
        try {
            val transcriptFile = CCAI.chatService?.downloadChatTranscript()
            if (transcriptFile != null) {
                Log.d("CCAI", "Transcript downloaded to: ${transcriptFile.absolutePath}")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to download transcript: ${e.message}")
        }
    }
    

The Android `downloadChatTranscript()` method takes no parameters and returns a `File?` pointing to the downloaded PDF. The `downloadChatTranscriptData()` method (which returns raw PDF data directly in memory without saving to disk) is available on iOS only. Ensure your app has the appropriate file storage permissions if saving to shared storage.

## Languages and localization

Because you are building a custom built-in UI using the Headless Mobile SDK, you own the translation of your app's buttons, menus, and custom alerts.

So, why does the SDK need to know the user's language?

  1. **Queue routing** : CCAI Platform uses the language code to route the user to an agent who speaks that language.

  2. **System messages** : Automated messages generated by the CCAI Platform backend (for example, "An agent will be with you shortly") are delivered in the active language.




### Language service APIs

**What the SDK provides** : A read and write `languageCode` property for the active SDK language.

**What you build** : A language picker UI (if you want users to choose manually) and the logic to set the language before a session starts.
    
    
    // Read the active language
    val currentLanguage = CCAI.languageService?.languageCode
    
    // Set the active language before the user starts a support session
    CCAI.languageService?.languageCode = "es"
    

The SDK doesn't expose a fixed SDK-supported language list. If your app shows a language picker, maintain the app's display list yourself or use instance or enterprise configuration returned by the SDK to determine which languages to offer.

### Setting the SDK language (the pre-session rule)

**Warning:** Based on the SDK's architecture, language switching is strictly pre-session only. Changing the language while a user is actively waiting in a queue or talking to an agent will break the routing logic and isn't supported.

**What the SDK provides** : A `LanguageService` that compares the language you request against the languages your admins have actually enabled in the CCAI Platform portal.

**What you build** : If you want to allow users to manually override the language (rather than just relying on their device's default settings), you must build the selection UI (such as a drop-down menu) and ensure it is only accessible _before_ they tap a support channel.

#### Implementation example

This code demonstrates how to explicitly override the SDK's language using standard ISO 639 language codes (for example, `"es"` for Spanish, `"fr"` for French). The preferred language is set using the `languageCode` parameter during SDK initialization in the `InitOptions` data class. You can also set it when re-initializing the SDK:
    
    
    // Set language during initialization
    val initOptions = InitOptions(
        key = "YOUR_COMPANY_KEY",
        urlHost = "your_subdomain.ccaiplatform.com",
        languageCode = "es"  // for example, "es" for Spanish, "fr" for French
    )
    
    try {
        CCAI.initialize(context = this, options = initOptions)
    } catch (e: Exception) {
        Log.e("CCAI", "Failed to initialize CCAI: ${e.message}")
    }
    

#### Chat module initialization (Android)

If you are initializing the chat module using the overload that accepts a language code, you can also supply the language there:
    
    
    val chatOptions = ChatOptions(
        webFormInterface = WebFormManager(),
        downloadTranscriptVisibility = DownloadTranscriptVisibility.SHOW_ALL,
        greeting = "Hello! How can I help you?"
    )
    CCAI.initializeChat(context = this, options = chatOptions)
    

You can also pass the language when fetching queue menus:
    
    
    val menuResult = CCAI.queueMenuService?.get(key = null)
    

Override per-session using the `ChatRequest`:
    
    
    val chatRequest = ChatRequest(
        chat = Chat(
            menuId = menuId,
            languageCode = "fr"  // This session will use French
        )
    )
    

### How CCAI Platform resolves the final language

If you don't explicitly set a language, the SDK still needs a language code for **routing** and **system messages**. To keep behavior predictable, it is best to set it yourself before the user starts a support session.

Use this priority order:

  1. **Explicit language (recommended)** : If you set a language in `InitOptions.languageCode`, the SDK uses that language.

  2. **Pre-session language update (still explicit)** : If you set `CCAI.languageService?.languageCode = "es"` before the user enters a queue, the SDK uses that updated language.

  3. **Per-session override (chat-only)** : If you provide `ChatRequest(chat = Chat(..., languageCode = "fr"))`, that chat session uses the requested language code.

  4. **If you don't set anything** : Behavior falls back to whatever the SDK determines is the best available option on the device and instance configuration. For consistent results, avoid relying on this and always set a language explicitly (Steps 1–3).




## Error handling, fallback, and session management

Even the most robust apps encounter dropped connections, missing dependencies, or authentication hiccups. The Headless Mobile SDK is designed to catch these underlying platform issues and surface them to your app, allowing you to handle them gracefully within your custom UI or rely on CCAI Platform's automated fallbacks.

### Handling SDK errors

**What the SDK provides** : Two categories of typed exceptions, alongside standard Kotlin exceptions:

  * `HttpExceptionWithCode` \- Thrown by any async service method when an HTTP request to the CCAI platform fails. Exposes an `Int code` property so you can branch on status codes (for example, `401` for expired authentication, `429` for rate limiting, `5xx` for server errors).

  * `CallCreationError.AfterHours` \- A sealed error thrown by the scheduled-call API (`callService.createScheduledCall`) when a slot conflict occurs or the scheduling window has closed. Carries a server-localized `displayMessage` intended for direct display to the user.

  * Standard Kotlin or Java exceptions - Network failures surface as `java.io.IOException`, coroutine cancellation as `kotlinx.coroutines.CancellationException`, and anything unanticipated as the base `Exception` class.




**What you build** : A layered try or catch around every SDK service call. Catch the most specific exception first (domain-specific sealed errors like `CallCreationError.AfterHours` where applicable, then `HttpExceptionWithCode` for HTTP status branching), and fall back to a generic `Exception` handler for network, system, and unanticipated failures.

#### Implementation example

This code wraps an SDK call in a layered try or catch pattern, catching `HttpExceptionWithCode` first to branch on the HTTP status code, then falling back to a generic handler for everything else.
    
    
    import kotlinx.coroutines.launch
    import androidx.lifecycle.lifecycleScope
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.start(chatRequest)
            // Handle success - observe chat state using chatReceived
        } catch (e: HttpExceptionWithCode) {
            // Handle HTTP-level failures from CCAI endpoints - inspect e.code for status code
            Log.e("CCAI", "HTTP ${e.code}: ${e.message}")
            showErrorToast("Something went wrong. Please try again.")
        } catch (e: Exception) {
            // Handle other errors (examples: network and system)
            Log.e("CCAI", "Error: ${e.message}")
            showErrorToast("An unexpected error occurred.")
        }
    }
    

#### Best practices

  * Wrap every SDK service call in a layered try/catch. Use `HttpExceptionWithCode` to branch on HTTP status codes - for example, re-trigger `ccaiShouldAuthenticate()` on `401` (expired auth token), apply a backoff on `429` (rate limiting), or surface a generic error on `5xx` responses.

  * For scheduled-call APIs, catch `CallCreationError.AfterHours` _before_ `HttpExceptionWithCode` so that 409 slot conflicts are handled with the server-localized message.

  * Finally, catch generic `Exception` as a safety net for `IOException`, `CancellationException`, and any unanticipated failures. Logging the exception details during development helps pinpoint root causes quickly.




### Check and clear sessions

Because your app's lifecycle is separate from the CCAI Platform support lifecycle, you need to manage session state - especially around user logouts.

**What the SDK provides** : Utility APIs to check if a support session is still in progress (including after app restarts or force-quits), and methods to clear cached SDK authentication state tied to a specific end user - preventing the next signed-in user from inheriting the previous user's session.

**What you build** : Pre-flight checks before trying to start new sessions, and cleanup routines that fire when a user logs out of your main app.

#### Implementation example (logout cleanup)

Ends any active session, clears the cached auth token from the SDK, wipes local app data, and navigates to the login screen - the minimum required cleanup to prevent session inheritance on user sign-out.
    
    
    fun handleUserLogout() {
        lifecycleScope.launch {
            // 1. Check for an in-progress session and end it cleanly
            try {
                val activeChat = CCAI.chatService?.getLastChatInProgress()
                if (activeChat != null) {
                    CCAI.chatService?.endChat()
                    Log.d("CCAI", "Ended active chat before logout.")
                }
            } catch (e: Exception) {
                // Session may not exist - that's fine
                Log.w("CCAI", "No active session to end: ${e.message}")
            }
    
            // 2. Clear the cached auth token
            //    (prevents the next user from inheriting the previous session)
            CCAI.authService?.updateAuthToken(null)
    
            // 3. Wipe your own app's user data
            MyAuthManager.clearLocalData()
    
            // 4. Navigate back to the login screen
            navigateToLoginScreen()
        }
    }
    

**Warning:** All cleanup steps (1–2) are required on logout. Skipping `updateAuthToken(null)` leaves a stale token that will silently authenticate the previous user on the next launch. Skipping the session check can leave an orphaned chat that blocks future sessions.

## Kotlin coroutines and Flow integration

The Headless Mobile SDK for Android is designed around **Kotlin coroutines** and **Flow** as its primary reactive patterns. This is the Android equivalent of the iOS SDK's Combine integration.

**What the SDK provides** : Kotlin Flow streams and suspend functions that emit real-time SDK events (incoming messages, screen share state changes) as observable reactive streams.

**What you build** : Coroutine-based integrations that collect these Flows and update your Android UI accordingly.

### Suspend functions

Many SDK service methods are Kotlin **suspend functions** , meaning they can be called from within a coroutine scope and will suspend (not block) while waiting for a result.
    
    
    import kotlinx.coroutines.launch
    import androidx.lifecycle.lifecycleScope
    
    // In an Activity or Fragment
    lifecycleScope.launch {
        try {
            // These are suspend functions - they suspend, not block
            val menuResult = CCAI.queueMenuService?.get()
            CCAI.chatService?.start(chatRequest)
            val company = CCAI.companyService?.get()
        } catch (e: Exception) {
            handleError(e)
        }
    }
    

**Note:** Use `lifecycleScope.launch {}` in Activities and Fragments and `viewModelScope.launch {}` in ViewModels. Both are lifecycle-aware and will automatically cancel when the lifecycle owner is destroyed.

### Chat service flows

The `chatService` exposes Kotlin `SharedFlow` properties for observing real-time chat events. Collect them within a lifecycle-aware coroutine scope (`lifecycleScope` or `viewModelScope`).

Flow | Emits  
---|---  
`messagesReceived` | Lists of incoming chat messages (from agents, VAs, or system).  
`typingEvent` | When a user or an agent is typing.  
`memberEvent` | When a user or an agent joins or leaves the chat (including agent transfers and disconnects).  
`stateChanged` | State changes of the chat provider (connecting, connected, disconnected, error).  
`chatReceived` | Chat response data when a chat is received or updated (including status changes, agent assignment, and post-session state).  
  
The `chatService` exposes additional Flows for transfer events (`transferEventSubject`), status check results (`checkStatusSubject`), and message send outcomes (`messageSendResultSubject`).

#### Implementation example
    
    
    import kotlinx.coroutines.flow.collect
    import kotlinx.coroutines.flow.distinctUntilChanged
    
    // 1. Incoming messages
    lifecycleScope.launch {
        CCAI.chatService?.messagesReceived?.collect { messages ->
            for (message in messages) {
                renderIncomingMessage(message)
            }
        }
    }
    
    // 2. Typing indicators
    lifecycleScope.launch {
        CCAI.chatService?.typingEvent?.collect { event ->
            when (event) {
                is ChatTypingEvent.Started -> showTypingIndicator()
                is ChatTypingEvent.Ended -> hideTypingIndicator()
            }
        }
    }
    
    // 3. Member join/leave
    lifecycleScope.launch {
        CCAI.chatService?.memberEvent?.collect { event ->
            when (event) {
                is MemberEvent.Joined -> Log.d("Chat", "Member joined")
                is MemberEvent.Left -> Log.d("Chat", "Member left")
            }
            // Refresh chat status after member changes
            try { CCAI.chatService?.checkStatus() } catch (_: Exception) {}
        }
    }
    
    // 4. Chat provider state changes
    lifecycleScope.launch {
        CCAI.chatService?.stateChanged?.distinctUntilChanged()?.collect { state ->
            // Update UI based on connection state (examples: connecting, connected)
            updateConnectionStatus(state)
        }
    }
    
    // 5. Chat metadata updates (agent assignment, status changes)
    lifecycleScope.launch {
        CCAI.chatService?.chatReceived?.collect { chat ->
            Log.d("Chat", "Received chat update: ${chat.id}")
            updateAgentInfo(chat)
            handlePostSessionIfNeeded(chat)
        }
    }
    

### Screen share state

**What the SDK provides** : Screen share session state is delivered through the `onSessionStateChanged` callback on `ScreenShareCallbacks`, which you pass to `ScreenShareManager.startSession()` — see [Headless Mobile SDK for Android: Voice, screen share, scheduled call, and email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice). The callback fires whenever the session transitions between `INACTIVE`, `PENDING`, and `ACTIVE`.

**What you build** : A handler wired into `ScreenShareCallbacks.onSessionStateChanged` that updates your UI as the session transitions between states, plus a local property (for example, `currentScreenShareSessionState`) if you need to read the current state outside the callback.

#### Implementation example

In addition to the `ScreenShareCallbacks` path, `ScreenShareManager` also exposes standalone `addStateChangeListener` / `removeStateChangeListener` APIs and a synchronous `getSessionState()` accessor. Use these when you need to observe state from a component other than the one that called `startSession()`, or to do a one-off non-reactive read. Unlike the `ScreenShareCallbacks` path - where the callback is released automatically when the session ends - standalone listeners aren't auto-released. Call `removeStateChangeListener(...)` in your lifecycle owner's teardown to avoid leaks.
    
    
    // Register a state change listener
    val listener: (ScreenShareSessionState) -> Unit = { state ->
        when (state) {
            ScreenShareSessionState.INACTIVE -> Log.d("ScreenShare", "No active session")
            ScreenShareSessionState.PENDING -> Log.d("ScreenShare", "Session pending")
            ScreenShareSessionState.ACTIVE -> Log.d("ScreenShare", "Session active")
        }
    }
    ScreenShareManager.addStateChangeListener(listener)
    
    // Get the current state directly (not reactive)
    val currentState = ScreenShareManager.getSessionState()
    
    // Clean up when done
    ScreenShareManager.removeStateChangeListener(listener)
    

## Custom data

**What the SDK provides** : A mechanism to attach structured metadata to chat sessions, either as **signed** JWTs (verified by your backend) or as **unsigned** payloads (set directly in the client).

**What you build** : The data collection logic in your app and, for signed data, the JWT-signing endpoint on your backend server (see [Headless Mobile SDK for Android: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started) for the full authentication and JWT payload schema).

### Signed custom data

Signed custom data uses a JWT token signed with your company secret on your backend server. This is the secure approach for passing sensitive or trusted data.

#### Implementation example

Create a signed custom data object from a JWT generated on your backend.
    
    
    // JWT signed with company secret (signing must happen on your backend)
    val customData = CustomData(signed = "header.payload.signature")
    

### Unsigned custom data

Unsigned custom data is set directly in the client using `CustomDataPayload` and `CustomDataItem`.

#### Implementation example

Build an unsigned payload with visible and agent-hidden data items. `CustomDataPayload` takes a `MutableMap<String, CustomDataItem?>`, so use subscript assignment (or `mutableMapOf`) to add each item by key. The key you choose (for example, `"user_name"` or `"account_tier"`) becomes the field name surfaced to the agent and to routing/analytics.
    
    
    val items = mutableMapOf<String, CustomDataItem?>()
    items["user_name"] = CustomDataItem(
        label = "Name",
        value = "John"
    )
    items["user_age"] = CustomDataItem(
        label = "Age",
        value = 30,
        type = CustomDataType.NUMBER,
        invisibleToAgent = true
    )
    val payload = CustomDataPayload(items = items)
    val customData = CustomData(unsigned = payload)
    

Custom data items support the following properties:

  * `label`: Display label shown to the agent.

  * `value`: The data value (examples: `String`, `Int`, `Bool`).

  * `type`: Data type (`STRING`, `NUMBER`, `DATE`, `URL`, `BOOLEAN`).

  * `invisibleToAgent`: When `true`, the data is hidden from agents but available for routing and analytics.




### Using custom data in chat requests

Attach custom data when starting a chat session.

#### Implementation example
    
    
    val chatRequest = ChatRequest(
        chat = Chat(
            menuId = 123,
            languageCode = "en",
            customData = customData
        )
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.start(chatRequest)
            // Chat started - observe chat state using chatReceived
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to start chat: ${e.message}")
        }
    }
    

## External chat transfer

**What the SDK provides** : A data structure (`ExternalChatTransfer`) to pass a previous agent's name and conversation transcript into a new CCAI Platform session.

**What you build** : The migration flow that extracts context from your external chat system and packages it for the SDK.

#### Implementation example

This code creates an external chat transfer object with the previous agent's name and attaches it to the session's custom data.
    
    
    // ExternalChatAgent also accepts an optional `avatar: String? = null` parameter
    // for displaying the previous agent's avatar, for example:
    //     ExternalChatAgent(name = "John Smith", avatar = "https://cdn.example.com/avatars/jsmith.png")
    val transfer = ExternalChatTransfer(
        agent = ExternalChatAgent(name = "John Smith"),
        transcript = emptyList()
    )
    
    // Attach to your custom data payload
    val payload = CustomDataPayload()
    payload.externalChatTransfer = transfer
    
    val customData = CustomData(unsigned = payload)
    

This is useful when migrating a user from a third-party chat system into a CCAI Platform-powered session, preserving the conversation context for the receiving agent.

## Threading considerations

The Headless Mobile SDK for Android is designed to work with Kotlin coroutines and is largely main-safe. However, there are important threading considerations for headless integrations.

### Main thread safety

All SDK methods are **thread-safe** and can be called from any thread. Most SDK service calls (for example, `chatService?.start()`, `queueMenuService?.get()`) are **suspend functions** that handle their own threading internally - they suspend the calling coroutine without blocking the thread. You can safely call them from the main thread within a coroutine scope:
    
    
    // Safe to call from the main thread
    lifecycleScope.launch {
        val menu = CCAI.queueMenuService?.get()  // Suspends, does not block
        updateUi(menu)  // Back on main thread
    }
    

### CCAIDelegate and background threads

The `ccaiShouldAuthenticate()` method in your `CCAIDelegate` is a suspend function, so you can safely perform network calls within it:
    
    
    override suspend fun ccaiShouldAuthenticate(): String? {
        // This runs in a coroutine context - safe to call suspend functions
        return withContext(Dispatchers.IO) {
            MyBackendApi.getSignedJwt()  // Network call on IO dispatcher
        }
    }
    

### UI updates from SDK callbacks

When observing SDK events using Flow, ensure UI updates happen on the main thread. If you use `lifecycleScope`, this is handled automatically:
    
    
    // lifecycleScope dispatches to Main by default
    lifecycleScope.launch {
        chatMessagesFlow.collect { messages ->
            // Already on Main - safe to update UI
            chatAdapter.submitList(messages)
        }
    }
    

If you collect from a non-main dispatcher, switch back explicitly:
    
    
    lifecycleScope.launch(Dispatchers.IO) {
        // Processing on IO thread
        val processed = heavyProcessing()
        withContext(Dispatchers.Main) {
            // Update UI on Main thread
            updateChatUi(processed)
        }
    }
    

### Initialization threading

`CCAI.initialize()` and related module initialization calls, such as `initializeChat()`, `initializeCall()`, and `initializeScreenShare()`, must be called on the **main thread** in your `Application.onCreate()`. These are synchronous calls that set up the SDK's internal state.
    
    
    class MainApplication : Application() {
        override fun onCreate() {
            super.onCreate()  // Always on main thread
    
            // All initialization must happen on main thread
            CCAI.initialize(context = this, options = initOptions)
            CCAI.initializeChat(context = this, options = ChatOptions())
            CCAI.initializeCall(context = this)
        }
    }
    

## Memory management

Proper memory management is essential to prevent leaks and ensure clean teardown of SDK resources.

### Coroutine and Flow lifecycle

Always cancel coroutine `Job` references and Flow collectors in Android lifecycle methods (`onDestroy()` for Activities, `onCleared()` for ViewModels). Failing to do so can keep references alive longer than intended, causing memory leaks.
    
    
    import kotlinx.coroutines.Job
    
    class ChatViewModel : ViewModel() {
        private var chatJob: Job? = null
    
        fun observeChatMessages() {
            chatJob = viewModelScope.launch {
                CCAI.chatService?.messagesReceived?.collect { messages ->
                    // Handle new messages
                }
            }
        }
    
        override fun onCleared() {
            super.onCleared()
            chatJob?.cancel()
        }
    }
    

### Listener and callback references

Use weak references for listeners and callbacks to prevent retain cycles. Clear any registered callbacks when your Activity or ViewModel is destroyed.
    
    
    class ChatActivity : AppCompatActivity() {
        private var chatJob: Job? = null
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            chatJob = lifecycleScope.launch {
                CCAI.chatService?.messagesReceived?.collect { messages ->
                    updateChatUI(messages)
                }
            }
        }
    
        override fun onDestroy() {
            super.onDestroy()
            chatJob?.cancel()
        }
    }
    

### Best practices

  * **Store coroutine`Job` references**: Always store `Job` references returned by `launch {}` to prevent runaway coroutines that outlive their scope.

  * **Clean up in lifecycle methods** : Cancel all jobs and clear callbacks in `onDestroy()` (Activities) or `onCleared()` (ViewModels).

  * **Use weak references for listeners** : Be cautious with lambdas that implicitly capture `this` (the enclosing Activity or Fragment context), as this can prevent garbage collection.

  * **Services are SDK-managed** : You don't need to manually release SDK services - they are managed by the `CCAI` singleton object.




## Troubleshooting

This section covers common integration issues and their resolutions.

### Build and dependency issues

This section covers common build and dependency issues.

#### Problem

Gradle can't resolve `com.ccaiplatform.android:CCAIKit`.

  * **Cause** : The CCAI Maven repository is missing or uses the wrong URL.

  * **Fix** : Ensure your `settings.gradle.kts` includes:
        
        maven { url = uri("https://sdk.ujet.co/ccaip/android/") }
        

Note the `/ccaip/` path segment. The legacy URL (`https://sdk.ujet.co/android/`) won't resolve artifacts.




#### Problem

Java 17 required compilation errors.

  * **Cause** : This SDK requires Java 17 compatibility.

  * **Fix** : Update your `build.gradle.kts`:
        
        compileOptions {
            sourceCompatibility = JavaVersion.VERSION_17
            targetCompatibility = JavaVersion.VERSION_17
        }
        kotlinOptions {
            jvmTarget = "17"
        }
        




#### Problem

`chatLibraryNotFound` (error code 1100) at runtime.

  * **Cause** : The `CCAIChatRed` module is missing from dependencies.

  * **Fix** : Both `CCAIChat` and `CCAIChatRed` are required for chat. Add:
        
        implementation("com.ccaiplatform.android:CCAIChat:ccaiVersion")
        implementation("com.ccaiplatform.android:CCAIChatRed:ccaiVersion")
        




### Initialization issues

This section covers common initialization issues.

#### Problem

`NullPointerException` when accessing `CCAI.chatService`.

  * **Cause** : `CCAI.initializeChat()` wasn't called, or was called before `CCAI.initialize()`.

  * **Fix** : Ensure initialization order in `Application.onCreate()`:

    1. `CCAI.initialize(context, options = initOptions)`

    2. `CCAI.initializeChat(context, options = chatOptions)`

    3. `CCAI.initializeCall(context)` (if using voice or scheduled calls)

    4. `CCAI.initializeScreenShare(context, options)` (if using screen share)




#### Problem

SDK services return `null` after initialization.

  * **Cause** : `CCAI.initialize()` wasn't called on the main thread, or the `Application` class isn't registered in the manifest.

  * **Fix** : Verify that the line `android:name=".MainApplication"` is present in your `AndroidManifest.xml` file and that all init calls are in `onCreate()`.




### Authentication issues

This section covers common authentication issues.

#### Problem

Authentication fails silently or `ccaiShouldAuthenticate()` is never called.

  * **Cause** : `CCAIDelegate` wasn't set in `InitOptions`.

  * **Fix** : Ensure `delegate` is passed to `InitOptions`:
        
        val initOptions = InitOptions(
            key = "YOUR_KEY",
            urlHost = "your_subdomain.ccaiplatform.com",
            delegate = MyCCAIDelegate()  // Must not be null
        )
        




#### Problem

JWT validation errors (error code 101).

  * **Cause** : The JWT is expired, malformed, or signed with the wrong secret.

  * **Fix** : Verify that your backend:

    * Uses the correct Company Secret Code.

    * Sets valid `iat` and `exp` timestamps.

    * Returns a properly formatted JWT string.




### Push notification issues

This section covers common push notification issues.

#### Problem

Push notifications aren't being received or handled.

  * **Cause** : The FCM token isn't registered with the SDK, the Firebase messaging service isn't registered, or incoming data payloads aren't being forwarded to the SDK.

  * **Fix** :

    * Call `CCAI.pushNotificationService?.updatePushToken(token)` in both `onNewToken()` and at startup.

    * Forward `remoteMessage.data` to `CCAI.pushNotificationService?.handlePushNotification(remoteMessage.data)` from your Firebase messaging service.

    * Verify `google-services.json` is in your app module.

    * Check that the Firebase Service Account Key is configured in the CCAI Platform administrator portal.

    * Render any visible notification or incoming-call UI in your own app code.




#### Problem

The SDK doesn't react to incoming push notifications (messages are ignored).

  * **Cause** : Passing the wrong data type to the `handlePushNotification()` method.

  * **Fix** : Ensure you pass `remoteMessage.data` (which is a `Map<String, String>`), not the entire `RemoteMessage` object.




### Chat session issues

This section covers common chat session issues.

#### Problem

`chatService?.start()` throws an exception or returns `null`.

  * **Cause** : Invalid `menuId`, authentication failure, or network issue.

  * **Fix** :

    * Verify the `menuId` matches a valid queue in your administrator portal.

    * Check that `ccaiShouldAuthenticate()` exchanges a valid signed JWT through `CCAI.authService?.authenticate(jwt)` and returns the resulting auth token.

    * Ensure the device has network connectivity.

    * Wrap the call in a try or catch, then log the exception details.




#### Problem

Chat messages not appearing in your UI.

  * **Cause** : Not observing the chat service's message stream.

  * **Fix** : Ensure you are collecting from the chat service's Flow in a lifecycle-aware scope (see the Chat service flows section above).




### Screen share issues

This section covers common screen share issues.

#### Problem

Screen share doesn't start after the user grants consent.

  * **Cause** : `CCAIScreenShare` module not initialized or Android `MediaProjection` not started.

  * **Fix** :

    * Ensure `CCAI.initializeScreenShare()` is called with valid `ScreenShareOptions`.

    * Verify you are correctly starting Android's `MediaProjectionManager` and foreground service after consent.

    * On Android 14+, ensure your foreground service type includes `mediaProjection`.




### General debugging tips

  * Enable verbose logging during development to see SDK internal state.

  * Check the CCAI Platform administrator portal to verify queue configuration, channel enablement, and operating hours.

  * Monitor network traffic with tools like Charles Proxy or Android Studio's Network Inspector to verify API calls to `*.ccaiplatform.com`.

  * Verify module versions match - all `com.ccaiplatform.android` modules should use the same version number to avoid compatibility issues.




## Series wrap-up

Congratulations - you've completed the five-part Headless Mobile SDK for Android series. Your integration now covers:

  * Setup and initialization ([Headless Mobile SDK for Android: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started))

  * Queues, channels, and chat ([Headless Mobile SDK for Android: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat))

  * Voice, screen share, scheduled call, and email ([Headless Mobile SDK for Android: Voice, screen share, scheduled call, and email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice))

  * Smart actions, attachments, and deflection ([Headless Mobile SDK for Android: Smart actions, attachments, and deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions))

  * Post-session flows, localization, error handling, and advanced topics (this article)




For ongoing reference, bookmark the **Headless Mobile SDK - Android API Reference** and keep an eye on the CCAI Platform release notes for SDK updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
