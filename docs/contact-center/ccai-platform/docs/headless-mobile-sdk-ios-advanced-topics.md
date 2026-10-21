---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-advanced-topics/
title: Headless mobile SDK for iOS: Advanced topics, localization, and post-session flows \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:35:30.461814+00:00
---

# Headless mobile SDK for iOS: Advanced topics, localization, and post-session flows  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-advanced-topics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless mobile SDK for iOS: Advanced topics, localization, and post-session flows Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the Headless Mobile SDK in your Android application. It covers everything that happens after a session ends, including localization, error handling and session management, end-user services, custom data, external chat transfer, reactive Combine patterns, threading considerations, memory management, and troubleshooting.

**Note:** Make sure you have completed initialization, authentication, queue and channel setup, and chat (see [Headless Mobile SDK for iOS: Getting Started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started), [Headless Mobile SDK for iOS: Queues, Channels, and Chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat), and [Headless Mobile SDK for iOS: Voice, Screen Share, Scheduled Call, and Email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice)).

## Post-session flows (post-session VA, surveys, and CSAT)

When a live chat or voice call ends, contact centers often want to collect feedback or offer automated follow-ups. Contact Center AI Platform supports three types of post-session experiences:

  1. Post-session virtual agent (virtual agent): An automated chatbot that continues the conversation after the human agent disconnects.

  2. Surveys: A multi-question form tailored to the specific queue.

  3. CSAT (customer satisfaction): A rating (for example, 1–5 stars) and optional text feedback.




### Enforcing the hierarchy

It is common for admins to configure overlapping rules in the portal (for example, turning on CSAT globally, but also turning on a post-session virtual agent for the "Billing" queue).

**What the SDK provides:** A strict conflict-resolution engine. The SDK evaluates the portal rules and ensures that only **one** post-session flow triggers per session, strictly adhering to the following hierarchy:

  * The post-session priority: post-session virtual agent > surveys > CSAT.

    * _Example: If both CSAT and post-session virtual agent are enabled for a queue, the user only sees the post-session virtual agent._



**What you build:** A listener that waits for the session to end, asks the SDK which flow won the hierarchy evaluation, and draws the corresponding screen. You don't need to write complex if, else logic to figure out which experience wins; the SDK does that math for you.

**Implementation example:** This snippet demonstrates how your app should listen to the end of a session and ask the SDK what to do next.
    
    
    // Called when the active chat or call ends
    func handleSessionEnded(postSessionFlow: PostSessionFlow?) {
        // 1. Check if there is a required post-session flow.
        //    The SDK has already calculated the hierarchy (virtual agent > Survey > CSAT).
        guard let flow = postSessionFlow else {
            // No feedback required. Safely close the support UI.
            closeSupportExperience()
            return
        }
        // 2. Route to the winning flow returned by the SDK.
        switch flow.type {
        case .virtualAgent:
            transitionToPostSessionVA()
        case .survey:
            showSurveyScreen(flow)
        case .csat:
            showCSATScreen(flow)
        }
    }
    

### Transitioning into the post-session phase

Regardless of which flow wins the hierarchy, you must call two shared lifecycle methods on `chatService` to signal the CCAI Platform platform that the post-session phase has begun.

**What the SDK provides:** Lifecycle methods to transition the session into and through the post-session phase (`startPostSession`, `readyPostSession`).

**What you build:** The orchestration logic that calls these methods at the correct points in your post-session UI flow.

**Implementation example:** This code transitions the session through the two post-session lifecycle stages.
    
    
    // Step 1: Start the post-session process (updates status to "in_progress")
    do {
        let postSessionResponse = try await CCAI.shared.chatService?.startPostSession()
        if let response = postSessionResponse {
            print("Post-session started successfully: \\(response.id)")
        }
    } catch {
        print("Failed to start post-session: \\(error)")
    }
    
    // Step 2: Signal that post-session is ready (updates status to "ready")
    do {
        let readyResponse = try await CCAI.shared.chatService?.readyPostSession()
        if let response = readyResponse {
            print("Post-session ready: \\(response.id)")
        }
    } catch {
        print("Failed to prepare post-session: \\(error)")
    }
    

After the platform acknowledges the transition, proceed to the specific flow.

### Post-session state fields on ChatResponse

Two post-session orchestration fields on `ChatResponse` drive the transition logic:

  * `postSessionTransferStatus: String?` \- The current state of the post-session transfer (for example, `"in_progress"`, `"ready"`, `"completed"`). The platform keys the orchestration state machine off this field: `startPostSession()` moves it to `"in_progress"`, `readyPostSession()` moves it to `"ready"`, and you observe this value on subsequent `ChatResponse` payloads (via `chatReceived`) to confirm the platform-side transition.

  * `postSessionOptInRequired: Bool?` \- Whether the user must explicitly opt in to the post-session flow before it runs. When `true`, surface an opt-in prompt in your UI and only call `startPostSession()` after the user consents. When `false` or `nil`, the opt-in check isn't required and you can transition straight into the post-session flow.



    
    
    func orchestratePostSession(from chat: ChatResponse) async {
        // 1. Honor opt-in gating if required
        if chat.postSessionOptInRequired == true {
            let consented = await presentPostSessionOptIn()
            guard consented else {
                closeSupportExperience()
                return
            }
        }
        // 2. Drive the state machine
        _ = try? await CCAI.shared.chatService?.startPostSession()   // → "in_progress"
        _ = try? await CCAI.shared.chatService?.readyPostSession()   // → "ready"
        // 3. Observe postSessionTransferStatus on subsequent chatReceived
        //    emissions to confirm the transfer completed before rendering the
        //    winning flow.
    }
    

  * `postSessionRequired` tells you whether _any_ post-session flow is configured for the session.

  * `postSessionOptInRequired` tells you whether explicit user consent is required before running it.

  * `postSessionTransferStatus` tells you where the platform is in the transition lifecycle.




All three are independent - always check each one.

### Post-session virtual agent (highest priority)

**What the SDK provides:** The transition state to shift the session from a human agent back to an automated bot, and the routing of the bot's messages.

**What you build:** Nothing entirely new. Because the post-session virtual agent operates as a chat, you keep your existing custom chat UI open and let it handle the incoming automated messages the same way it handled the human agent's messages.

**Implementation example:** If the SDK signals a transition to a post-session VA, you update your chat UI to reflect the change.
    
    
    func transitionToPostSessionVA() {
        // Keep your Chat UI open, but update the visual context
        myChatUI.insertSystemDivider("You are now speaking with our Virtual Assistant")
        myChatUI.updateAgentAvatar(to: .botIcon)
        // The SDK will automatically start piping the VA's messages into
        // your standard chat message listeners.
    }
    

### Surveys (medium priority)

**What the SDK provides:** The `rateService` exposes methods to retrieve survey questions and submit answers for a communication session. Survey questions are configured by the administrator for each queue and can include multiple question types (CSAT, star rating, free-form text, enumeration, numeric scale).

**What you build:** A dynamic form that fetches the survey, loops through the questions, renders the appropriate UI (such as radio buttons, star ratings, or text fields) for each, validates that required fields are filled out, and packages the answers to send back.

**Key types:**
    
    
    // Survey response from getSurvey()
    public struct Survey {
        public let id: Int?
        public let lang: String?
        public let questions: [SurveyQuestion]
        public let signOffDisplayText: String?  // "Thank you" message to show after submission
    }
    
    // Request payload for submitSurvey()
    public struct SurveyRequest {
        public let answers: [Int: String]  // Maps question IDs to answer values
    }
    

**Implementation example:** This code fetches survey questions from the `rateService`, renders them in a custom view controller, and submits the answers.
    
    
    func showSurveyScreen(communicationId: Int64) async {
        guard let rateService = CCAI.shared.rateService else { return }
        do {
            // 1. Fetch the survey questions for this session
            let survey = try await rateService.getSurvey(
                communicationId: communicationId,
                communicationType: "chats"
            )
            // 2. Present your custom survey UI
            //    Note: survey.questions is non-optional ([SurveyQuestion]) on iOS -
            //    no need to use .orEmpty() / ?? [] safeguards.
            let surveyVC = MyCustomSurveyViewController(questions: survey.questions)
            surveyVC.onSubmit = { answersDict in
                Task {
                    do {
                        // 3. Submit the answers
                        let request = SurveyRequest(answers: answersDict)
                        try await rateService.submitSurvey(
                            communicationId: communicationId,
                            communicationType: "chats",
                            answers: request
                        )
                        rateService.clearRateTarget()
                        self.closeSupportExperience()
                    } catch {
                        print("Failed to submit survey: \\(error)")
                    }
                }
            }
            present(surveyVC, animated: true)
        } catch {
            print("Failed to load survey: \\(error)")
            closeSupportExperience()
        }
    }
    

### CSAT - customer satisfaction (lowest priority)

**What the SDK provides:** The `rateService` exposes a `rate()` method to submit a CSAT score and optional feedback for a communication session. The rating is typically a 1–5 integer value.

**What you build:** The visual rating screen (such as a row of tappable stars or a 1–5 number scale), a field if feedback is allowed, and a **Submit** button.

**Key types:**
    
    
    // Request payload for rate()
    public struct RatingRequest {
        public let rating: Int?       // Typically 1-5
        public let feedback: String?  // Optional qualitative feedback
    }
    

**Implementation example:** After the user taps a star rating and writes their feedback, you pass those values to the `rateService`.
    
    
    func submitCSATFeedback(communicationId: Int64, rating: Int, comment: String?) {
        guard let rateService = CCAI.shared.rateService else { return }
        submitButton.startLoading()
        Task {
            do {
                let request = RatingRequest(rating: rating, feedback: comment)
                try await rateService.rate(
                    communicationId: communicationId,
                    communicationType: "chats",
                    request: request
                )
                rateService.clearRateTarget()
                showThankYouScreen()
            } catch {
                showError("Failed to submit feedback. Please try again.")
            }
        }
    }
    

### Downloading chat transcripts

**What the SDK provides:** Methods to download the chat transcript as a PDF - either to a file URL or as raw `Data` in memory (iOS only).

**What you build:** The download button in your UI and the file-handling logic (save, share, or preview).

**Implementation example:** This code demonstrates both transcript download approaches - saving to a file URL and retrieving raw PDF data in memory.
    
    
    // Option 1: Download to a file destination
    let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
    let transcriptURL = documentsPath.appendingPathComponent("chat_transcript.pdf")
    do {
        try await CCAI.shared.chatService?.downloadChatTranscript(to: transcriptURL)
        print("Transcript downloaded to: \\(transcriptURL.path)")
    } catch {
        print("Failed to download transcript: \\(error)")
    }
    
    // Option 2: Get the PDF data directly (iOS only)
    do {
        let transcriptData = try await CCAI.shared.chatService?.downloadChatTranscriptData()
        if let data = transcriptData {
            // Use the PDF data directly (for example, display in a preview, email it)
            print("Transcript data size: \\(data.count) bytes")
        }
    } catch {
        print("Failed to download transcript data: \\(error)")
    }
    

The `downloadChatTranscriptData()` method is iOS only and returns the raw PDF `Data` directly, allowing you to use it without saving to disk first. The `downloadChatTranscript(to:)` method downloads to a specified file URL with built-in retry logic.

## Languages and localization

Because you are building a custom UI using the Headless Mobile SDK, you own the translation of your app's buttons, menus, and custom alerts.

So, why does the CCAI Platform SDK need to know the user's language?

  1. Queue routing: CCAI Platform uses the language code to route the user to an agent who speaks that language.

  2. System messages: Automated messages generated by the CCAI Platform backend (for example, "An agent will be with you shortly") are delivered in the active language.




### Language service APIs

**What the SDK provides:** A read and write `languageCode` property for the active SDK language.

**What you build:** A language picker UI (if you want users to choose manually) and the logic to set the language before a session starts.
    
    
    // Read the active language
    let currentLanguage = CCAI.shared.languageService?.languageCode
    
    // Set the active language before the user starts a support session
    CCAI.shared.languageService?.languageCode = "es"
    

The SDK doesn't expose a fixed SDK-supported language list. If your app shows a language picker, maintain the app's display list yourself or use instance or company configuration returned by the SDK to determine which languages to offer.

### Setting the SDK language (the pre-session rule)

**Warning:** Based on the SDK's architecture, language switching is strictly pre-session only. Changing the language while a user is actively waiting in a queue or talking to an agent will break the routing logic and isn't supported.

**What the SDK provides:** A `languageService` that compares the language you request against the languages your admins have actually enabled in the CCAI Platform portal.

**What you build:** If you want to allow users to manually override the language (rather than relying on their device's default settings), you must build the selection UI (such as a drop-down menu) and ensure it is only accessible _before_ they tap a support channel.

**Implementation example:** This code demonstrates how to explicitly override the SDK's language using standard ISO 639 language codes (for example, `"es"` for Spanish, `"fr"` for French). The preferred language is set using the `languageCode` parameter during SDK initialization in the `InitOptions` struct. You can also set it when re-initializing the SDK:
    
    
    // Set language during initialization
    let options = InitOptions(
        key: "YOUR_COMPANY_KEY",
        urlHost: "your_subdomain.ccaiplatform.com",
        delegate: self,
        languageCode: "es"  // for example, "es" for Spanish, "fr" for French
    )
    do {
        try CCAI.shared.initialize(options: options)
    } catch {
        print("Failed to initialize CCAI: \\(error)")
    }
    

You can also pass the language when fetching queue menus:
    
    
    let (menus, isDirectAccess) = try await CCAI.shared.queueMenuService?.get(
        key: nil,
        language: "es"  // Request menus in Spanish
    )
    

### How CCAI Platform resolves the final language

If you don't explicitly set a language, the SDK still needs a language code for **routing** and **system messages**. For the most predictable behavior, set it yourself before the user starts a support session.

Use this priority order:

  1. Explicit language (recommended): If you set a language in `InitOptions.languageCode`, the SDK uses that language.

  2. Device language (when available): If you don't set a language explicitly, the SDK uses the language selected in the user's iOS Settings (**Settings > General > Language & Region**), as long as that language is enabled for your instance in the CCAI Platform portal.

  3. Parent dialect fallback: If the device is set to a regional dialect that isn't enabled (for example, `es-CU`), but the base language is enabled (`es`), the SDK falls back to the parent language.

  4. English fallback: If none of the previous options are available, the SDK falls back to English.




## Error handling, fallback, and session management

Even the most robust apps encounter dropped connections, missing dependencies, or authentication hiccups. The Headless Mobile SDK is designed to catch these underlying platform issues and surface them to your app, allowing you to handle them gracefully within your custom UI or rely on CCAI Platform automated fallbacks.

### Handling SDK errors

All async methods in the Headless Mobile SDK for iOS can throw errors.

**What the SDK provides:** Async service methods such as `chatService`, `queueMenuService`, and `authService` that throw Swift `Error` values when an operation fails. The iOS SDK doesn't define a single unifying `CCAIError` type. Specific failure modes are expressed through focused error types (for example, `NetworkError`, `ScreenShareError`, `ChatProviderError`) alongside standard Foundation errors. For most integrations, catching the generic `Error` and reading `error.localizedDescription` is sufficient.

**What you build:** `do/catch` error handling around every SDK service call, surfacing a user-facing message and - where appropriate - triggering recovery logic (for example, re-requesting authentication on `authService` failures).

**Implementation example:** This code wraps an SDK call in a standard Swift `do/catch`, reading the error's localized description for display and logging.
    
    
    do {
        let result = try await someAsyncMethod()
        // Handle success
    } catch {
        // Handle any error thrown by the SDK (examples: auth failure, network, invalid config)
        print("SDK error: \\(error.localizedDescription)")
        showErrorToUser(error.localizedDescription)
    }
    

**Best practices:**

  * Wrap every SDK service call in `do/catch`. Common failure modes include expired authentication tokens (re-trigger `ccaiShouldAuthenticate()`), invalid `menuId` values, missing module dependencies (for example, calling `chatService` before `initializeChat()`), and network or system-level issues.

  * If you need to branch on specific error types, pattern-match against the concrete types thrown by the relevant subsystem (for example, `ScreenShareError` from the screen share service).

  * Logging the error details during development helps pinpoint root causes quickly.




### Check and clear sessions

Because your app's lifecycle is separate from the CCAI Platform support lifecycle, you need to manage session state - especially around user logouts.

**What the SDK provides:** Utility APIs to check if a support session is still in progress (including after app restarts or force-quits), and a secure method to clear all cached SDK state tied to a specific end user - most importantly the cached authentication token stored in the iOS Keychain.

**What you build:** Pre-flight checks before trying to start new sessions, and cleanup routines that fire when a user logs out of your main app.

**Implementation example (logout cleanup):** Ends any active session, clears the cached auth token and end-user record from the SDK, wipes local app data, and navigates to the login screen - preventing the next signed-in user from inheriting the previous user's SDK session.
    
    
    func handleUserLogout() {
        Task {
            // 1. Check for an in-progress session and end it cleanly
            if let activeChat = try? await CCAI.shared.chatService?.getLastChatInProgress() {
                try? await CCAI.shared.chatService?.endChat()
                print("Ended active chat \\(activeChat.id) before logout.")
            }
            // 2. Clear the cached auth token from the iOS Keychain
            //    (prevents the next user from inheriting the previous session)
            CCAI.shared.authService?.updateAuthToken(nil)
            // 3. Clear the end user record
            CCAI.shared.endUserService?.updateEndUser(nil)
            // 4. Wipe your own app's user data
            MyAuthManager.shared.clearLocalData()
            // 5. Navigate back to the login screen
            await MainActor.run {
                transitionToLoginScreen()
            }
        }
    }
    

**Warning:** All three SDK cleanup steps (1–3) are required on logout. Skipping `updateAuthToken(nil)` leaves a stale token in the Keychain that will silently authenticate the previous user on the next launch. Skipping `updateEndUser(nil)` can cause the SDK to report incorrect end-user metadata. Skipping the session check can leave an orphaned chat that blocks future sessions.

## End user services (iOS only)

**What the SDK provides:** A read and write service (`endUserService`) for accessing and updating the authenticated end user's profile information (name, email, phone, identifier). This service is iOS-only.

**What you build:** The integration between your app's user and authentication system and the SDK's end user record, including updates on login and cleanup on logout (see [_Check and clear sessions_](https://support.ujet.co/hc/en-us/articles/57490933873689-Headless-Mobile-SDK-v3-for-iOS-Post-Session-and-Advanced-Topics#checkandclearsessions) earlier in this article).

### EndUser data structure
    
    
    public struct EndUser: Codable {
        public let id: Int?
        public let name: String?
        public let identifier: String?
        public let email: String?
        public let phone: String?
    
        public var displayName: String { name ?? email ?? identifier ?? "Customer" }
    }
    

### Accessing end user information

**Implementation example:** Retrieve the current end user's profile using the read-only `endUser` property.
    
    
    if let user = CCAI.shared.endUserService?.endUser {
        print("Current user: \\(user.displayName)")
        print("Email: \\(user.email ?? "N/A")")
        print("Phone: \\(user.phone ?? "N/A")")
    }
    

### Updating end user information

**Implementation example:** Update the end user record with new profile data, or clear it on logout.
    
    
    // Update end user information
    let newUser = EndUser(
        id: 123,
        name: "John Doe",
        identifier: "user123",
        email: "john@example.com",
        phone: "+1234567890"
    )
    CCAI.shared.endUserService?.updateEndUser(newUser)
    
    // Clear end user information
    CCAI.shared.endUserService?.updateEndUser(nil)
    

## Custom data

**What the SDK provides:** A mechanism to attach structured metadata to chat sessions, either as **signed** JWTs (verified by your backend) or as **unsigned** payloads (set directly in the client).

**What you build:** The data collection logic in your app and, for signed data, the JWT-signing endpoint on your backend server (see [Authenticate end users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#authenticate_end_users) for the full authentication and JWT payload schema).

### Signed custom data

Signed custom data uses a JWT token signed with your company secret on your backend server. This is the secure approach for passing sensitive or trusted data.

**Implementation example:** Create a signed custom data object from a JWT generated on your backend.
    
    
    // JWT signed with company secret (signing must happen on your backend)
    let customData = CustomData(signed: "header.payload.signature")
    

### Unsigned custom data

Unsigned custom data is set directly in the client using `CustomDataPayload` and `CustomDataItem`.

**Implementation example:** Build an unsigned payload with visible and agent-hidden data items.
    
    
    var payload = CustomDataPayload()
    payload["user_name"] = CustomDataItem(
        label: "Name",
        value: "John"
    )
    payload["user_age"] = CustomDataItem(
        label: "Age",
        value: 30,
        type: .number,
        invisibleToAgent: true
    )
    let customData = CustomData(unsigned: payload)
    

Custom data items support the following properties:

  * `label`: Display label shown to the agent.

  * `value`: The data value (examples: `String`, `Int`, `Bool`).

  * `type`: Data type (`.string`, `.number`, `.date`, `.url`, `.boolean`).

  * `invisibleToAgent`: When `true`, the data is hidden from agents but available for routing and analytics.




### Using custom data in chat requests

**Implementation example:** Attach custom data when starting a chat session.
    
    
    let chatRequest = ChatRequest(
        menuId: 123,
        lang: "en",
        customData: customData
    )
    do {
        try await CCAI.shared.chatService?.start(request: chatRequest)
    } catch {
        print("Failed to start chat: \(error)")
    }
    

## External chat transfer

**What the SDK provides:** A data structure (`ExternalChatTransfer`) to pass a previous agent's name and conversation transcript into a new CCAI Platform session.

**What you build:** The migration flow that extracts context from your external chat system and packages it for the SDK.

**Implementation example:** This code creates an external chat transfer object with the previous agent's name and attaches it to the session's custom data.
    
    
    let transfer = ExternalChatTransfer(
        agent: ExternalChatAgent(name: "John Smith"),
        transcript: []
    )
    
    // Attach to your custom data payload
    var payload = CustomDataPayload()
    payload.externalChatTransfer = transfer
    let customData = CustomData(unsigned: payload)
    

This is useful when migrating a user from a third-party chat system into a CCAI Platform session, preserving the conversation context for the receiving agent.

## Combine integration (reactive programming)

**What the SDK provides:** Combine publishers that emit real-time SDK events (incoming messages, screen share state changes) as observable streams.

**What you build:** Reactive UI bindings that subscribe to these publishers and update your SwiftUI or UIKit views accordingly.

### Chat messages

The `chatService` exposes Combine publishers for observing real-time chat events.

**Warning:** The chat service publishers are raw `PassthroughSubject` / `CurrentValueSubject` values - they don't apply `.receive(on: DispatchQueue.main)` internally. Depending on where the SDK emits from, `sink` closures may run on a background thread. If you update UIKit or SwiftUI from `sink`, add `.receive(on: DispatchQueue.main)` before `.sink` (or hop to `MainActor` inside the closure) to avoid crashes.Publisher | Emits  
---|---  
`messagesReceived` | Lists of incoming chat messages (from agents, virtual agents, or system).  
`typingEvent` | When a user or an agent is typing.  
`memberEvent` | When a user or an agent joins or leaves the chat (including agent transfers and disconnects).  
`stateChanged` | State changes of the chat provider (connecting, connected, disconnected, error).  
`chatReceived` | Chat response data when a chat is received or updated (including status changes, agent assignment, and post-session state).  
  
The `chatService` exposes additional publishers for transfer events (`coldTransferSubject`) and other internal state changes. For complete type signatures and all available publishers, see the **Headless Mobile SDK - iOS API Reference**.

**Implementation example:**
    
    
    import Combine
    
    private var cancellables = Set<AnyCancellable>()
    
    // 1. Incoming messages
    CCAI.shared.chatService?.messagesReceived
        .receive(on: DispatchQueue.main)
        .sink { messages in
            for message in messages {
                updateChatUI(with: message)
            }
        }
        .store(in: &cancellables)
    
    // 2. Typing indicators
    CCAI.shared.chatService?.typingEvent
        .receive(on: DispatchQueue.main)
        .sink { event in
            switch event {
            case .started:
                showTypingIndicator()
            case .ended:
                hideTypingIndicator()
            default:
                break
            }
        }
        .store(in: &cancellables)
    
    // 3. Member join/leave
    // Note: the associated value on .joined / .left is `identity: String?` (the
    // member's identity, not a full Member struct).
    CCAI.shared.chatService?.memberEvent
        .receive(on: DispatchQueue.main)
        .sink { event in
            switch event {
            case .joined(let identity):
                print("Member joined: \\(identity ?? "Unknown")")
            case .left(let identity):
                print("Member left: \\(identity ?? "Unknown")")
            default:
                break
            }
            // Refresh chat status after member changes
            Task { try? await CCAI.shared.chatService?.checkStatus() }
        }
        .store(in: &cancellables)
    
    // 4. Chat provider state changes
    CCAI.shared.chatService?.stateChanged
         .receive(on: DispatchQueue.main)
        .sink { state in
            // Update UI based on connection state (connecting, connected, etc.)
            updateConnectionStatus(state)
            Task { try? await CCAI.shared.chatService?.checkStatus() }
        }
        .store(in: &cancellables)
    
    // 5. Chat metadata updates (agent assignment, status changes)
    CCAI.shared.chatService?.chatReceived
        .receive(on: DispatchQueue.main)
        .sink { chat in
            guard let chat = chat else { return }
            updateAgentInfo(chat.agent)
            handlePostSessionIfNeeded(chat)
        }
        .store(in: &cancellables)
    

### Screen share state

**Implementation example:** Monitor screen share state changes reactively and respond to each session phase.
    
    
    CCAI.shared.screenShareService?.statePublisher
        .receive(on: DispatchQueue.main)  // Ensure UI updates run on the main thread
        .sink { state in
            switch state {
            case .none:
                print("No screen share session")
            case .pending:
                print("Screen share pending")
            case .authorizing:
                print("Screen share authorizing")
            case .active:
                print("Screen share active")
            case .ended:
                print("Screen share ended")
            }
        }
        .store(in: &cancellables)
    

**Note:** The SDK doesn't apply `.receive(on: DispatchQueue.main)` internally on its Combine publishers. Add it explicitly (as shown above) before any `sink` that touches UIKit or SwiftUI views, or hop to the main actor inside the closure.

## Threading considerations

The Headless Mobile SDK for iOS is designed to work with Swift's structured concurrency (async/await) and is largely main-safe. However, there are important threading considerations for headless integrations.

### Thread safety

All SDK methods are **thread-safe** and can be called from any thread. Network operations are performed asynchronously using Swift's async and await pattern - they suspend the calling task without blocking the thread.
    
    
    // Safe to call from the main thread - suspends, does not block
    Task {
        let result = try await CCAI.shared.queueMenuService?.get(
            key: nil,
            language: "en"
        )
        // Back on the calling context after suspension
        displayQueueMenu(result)
    }
    

### CCAIDelegate and async authentication

The `ccaiShouldAuthenticate()` method in your `CCAIDelegate` is an async function, so you can safely perform network calls within it:
    
    
    func ccaiShouldAuthenticate() async -> String? {
        // This runs in an async context - safe to call async functions
        guard let jwt = await signJWTRemotely() else { return nil }
        return try? await CCAI.shared.authService?.authenticate(jwt)
    }
    

### UI updates from SDK callbacks

When observing SDK events using Combine publishers, ensure UI updates happen on the main thread. The chat service and screen share publishers are raw subjects that **don't** apply a main-thread scheduler internally, so always insert `.receive(on: DispatchQueue.main)` before a `sink` that updates the UI:
    
    
    // Explicitly hop to the main thread before updating UI
    CCAI.shared.chatService?.messagesReceived
        .receive(on: DispatchQueue.main)
        .sink { [weak self] messages in
            // Safe to update UI here
            self?.chatTableView.reloadData()
        }
        .store(in: &cancellables)
    

For async SDK calls, use `@MainActor` (in Swift concurrency / async and await code) or `DispatchQueue.main.async` (in Grand Central Dispatch / closure-based code) to switch back to the main thread before updating the UI:
    
    
    // Async SDK calls - use @MainActor to update UI
    func refreshChatStatus() {
        Task {
            do {
                try await CCAI.shared.chatService?.checkStatus()
                await MainActor.run {
                    updateStatusIndicator()
                }
            } catch {
                await MainActor.run {
                    showError(error.localizedDescription)
                }
            }
        }
    }
    

If you collect from a background context, switch back explicitly:
    
    
    Task.detached(priority: .userInitiated) {
        // Processing off main thread
        let processed = heavyProcessing()
        await MainActor.run {
            // Update UI on Main thread
            updateChatUI(processed)
        }
    }
    

### Initialization threading

SDK initialization (`CCAI.shared.initialize(options:)`) must be called during app launch in your AppDelegate's `application(_:didFinishLaunchingWithOptions:)` method. Feature module initialization (`initializeChat()`, `initializeScreenShare()`) should also be performed at this time, before any service calls are made.
    
    
    // Always initialize on the main thread during app launch
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let options = InitOptions(
            key: "YOUR_COMPANY_KEY",
            urlHost: "your_subdomain.ccaiplatform.com",
            delegate: self,
            languageCode: "en"
        )
        do {
            try CCAI.shared.initialize(options: options)
            CCAI.shared.initializeChat()
        } catch {
            print("Failed to initialize CCAI: \\(error.localizedDescription)")
        }
        return true
    }
    

## Memory management

Proper memory management is essential to prevent leaks and ensure clean teardown of SDK resources.

### Delegate references

The Headless Mobile SDK for iOS uses **weak references** for all delegates to prevent retain cycles. You don't need to manually nil out delegates in most cases, but it is good practice to do so in `deinit`.

### Combine cancellables

Always store Combine subscriptions in a `Set<AnyCancellable>` and clean them up when your view controller or view model is deallocated:
    
    
    import Combine
    
    class ChatViewModel {
        private var cancellables = Set<AnyCancellable>()
    
        init() {
            // Subscribe to chat messages
            CCAI.shared.chatService?.messagesReceived
                .sink { messages in
                    // Handle new messages
                }
                .store(in: &cancellables)
    
            // Subscribe to screen share state
            CCAI.shared.screenShareService?.statePublisher
                .sink { state in
                    // Handle state changes
                }
                .store(in: &cancellables)
        }
    
        deinit {
            // Clean up all subscriptions
            cancellables.removeAll()
    
            // Nil out delegates
            CCAI.shared.screenShareService?.delegate = nil
        }
    }
    

### Best practices

  * Store cancellables: Always store `AnyCancellable` references to prevent subscriptions from being immediately deallocated.

  * Clean up in `deinit`: Remove all cancellables and nil out delegates when your object is deallocated.

  * Avoid retain cycles: Use `[weak self]` in closures that capture `self`. This creates a non-owning reference, so the closure doesn't keep your object alive longer than it should - preventing memory leaks when the object is deallocated before the closure runs:
        
        CCAI.shared.chatService?.messagesReceived
            .sink { [weak self] messages in
                self?.handleMessages(messages)
            }
            .store(in: &cancellables)
        

  * Services are SDK-managed: You don't need to manually release SDK services - they are managed by the `CCAI.shared` singleton.




## Troubleshooting

Follow these suggestions to resolve common issues.

### App Store submission - VoIP entitlement

When you submit your app to Apple for review, the App Store will ask:

> _"Does this app use the VoIP Background Mode or PushKit VoIP push notifications?"_

**Answer Yes.** Because the SDK uses PushKit for incoming calls and PSTN-based smart actions (see [Registering for VoIP push notifications (PushKit)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#register_for_voip_push_notifications)), the VoIP entitlement is required. Answering "No" - or omitting the entitlement - will result in rejection or broken call and push functionality.

**Warning:** Apple enforces strict rules for VoIP push usage. Forward VoIP payloads to the SDK through the PushKit handling path shown in [Headless Mobile SDK for iOS: Getting Started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started), so incoming-call payloads can be processed correctly.

### Build and dependency issues

**Problem:** Swift Package Manager can't resolve `CCAIKit`.

  * Cause: The package URL or branch is incorrect in your `Package.swift` or Xcode SPM settings.

  * Fix: Ensure your SPM dependency uses the correct repository URL and branch:
        
        dependencies: [
            .package(url: "<https://github.com/UJET/ccai-ios-sdk.git>", branch: "3.3.1")
        ]
        




Verify the branch matches the SDK version you intend to use. If Xcode can't resolve the package, try **File > Packages > Reset Package Caches** and then **Resolve Package Versions**.

**Problem:** Build errors in a SwiftUI project related to AppDelegate.

  * Cause: The SDK requires an AppDelegate for initialization and push notification delegates, but pure SwiftUI apps don't have one by default.

  * Fix: Declare `@UIApplicationDelegateAdaptor` in your `App` struct:
        
        @main
        struct YourAppName: App {
            @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
            // ...
        }
        




Then implement your `AppDelegate` class with `CCAIDelegate` conformance and push notification delegates as shown in [Implement the CCAIDelegate for authentication and Registering for remote notifications](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#implement_the_ccaidelegate_for_authentication).

### Initialization issues

**Problem:** `chatService` returns `nil`.

  * Cause: `CCAI.shared.initializeChat()` wasn't called, or was called before `CCAI.shared.initialize(options:)`.

  * Fix: Ensure initialization order in your `AppDelegate.application(_:didFinishLaunchingWithOptions:)`:
        
        // 1. Initialize the Core SDK
        try CCAI.shared.initialize(options: options)
        // 2. Initialize Chat
        CCAI.shared.initializeChat()
        // 3. Initialize Screen Share (optional)
        // CCAI.shared.initializeScreenShare(screenShareOptions)
        




The `chatService` property on `CCAI.shared` only has a value after `initializeChat()` is called.

**Problem:** `screenShareService` returns `nil`.

  * Cause: `CCAI.shared.initializeScreenShare()` wasn't called, or was called with invalid `ScreenShareOptions`.

  * Fix: Ensure you call `initializeScreenShare()` with a valid screen share key:
        
        CCAI.shared.initializeScreenShare(ScreenShareOptions(key: "YOUR_SCREEN_SHARE_KEY"))
        




### Authentication issues

**Problem:** Authentication fails silently or `ccaiShouldAuthenticate()` is never called.

  * Cause: The delegate wasn't set in `InitOptions`.

  * Fix: Ensure `delegate` is passed to `InitOptions`:
        
        let options = InitOptions(
            key: "YOUR_KEY",
            urlHost: "your_subdomain.ccaiplatform.com",
            delegate: self  // Must conform to CCAIDelegate
        )
        




The `delegate` property on `InitOptions` is declared as `weak`, so the object you pass must be retained elsewhere (for example, your `AppDelegate` or a long-lived coordinator).

**Problem:** JWT validation errors or `authService?.authenticate()` throws.

  * Cause: The JWT is expired, malformed, or signed with the wrong secret.

  * Fix: Verify that your backend:

    * Uses the correct company secret code.

    * Sets valid `iat` and `exp` timestamps.

    * Signs the JWT with the HS384 algorithm.

    * Returns a properly formatted JWT string.




### Push notification issues

**Problem:** Push notifications aren't received or aren't handled.

  * Cause: Push notification delegates aren't implemented, or APNs/VoIP tokens aren't being forwarded to the SDK.

  * Fix:

    * Implement the required `UIApplicationDelegate` methods and forward tokens to the SDK:
          
          func application(
              _ application: UIApplication,
              didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
          ) {
              CCAI.shared.pushNotificationService?.updatePushToken(
                  data: deviceToken,
                  type: .apns
              )
          }
          

    * For VoIP pushes, implement `PKPushRegistryDelegate` and forward the VoIP token with `type: .voip` (see [Registering for VoIP push notifications (PushKit)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#register_for_voip_push_notifications)).

    * Verify both APNs and VoIP certificates are uploaded in the CCAI Platform portal (see [Configuring certificates](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#configure_certificates)).

    * Ensure Push Notifications and Background Modes (**Voice over IP** , **Remote notifications**) are enabled in your target's **Signing & Capabilities**.




**Problem:** VoIP pushes don't wake the app from terminated state.

  * Cause: `PKPushRegistry` isn't configured, or voice over IP background mode isn't enabled.

  * Fix:

    * Create a `PKPushRegistry` in `didFinishLaunchingWithOptions` with `desiredPushTypes = [.voIP]` (see [Registering for VoIP push notifications (PushKit)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started#register_for_voip_push_notifications)).

    * Ensure the Voice over IP background mode is checked in **Target** > **Signing & Capabilities** > **Background Modes**.

    * VoIP push notifications only work on physical devices - they aren't supported in the iOS Simulator.




### Chat session issues

**Problem:** `chatService?.start()` throws an error.

  * Cause: Invalid `menuId`, authentication failure, network issue, or an existing session conflict.

  * Fix:

    * Verify the `menuId` matches a valid queue in your administrator portal.

    * Check that `ccaiShouldAuthenticate()` returns a valid auth token.

    * Ensure the device has network connectivity.

    * Always call `getLastChatInProgress()` before starting a new chat - if an earlier session is still active (for example, the app was force-quit mid-conversation), starting a second chat will fail. Resume or end the existing session first (see [Starting a chat session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat#start-chat)).

    * Wrap the call in a `do/catch` and log the error details.




**Problem:** Chat messages aren't appearing in your UI.

  * Cause: Not subscribing to the chat service's Combine publisher.

  * Fix: Ensure you are subscribing to `messagesReceived` and storing the cancellable (see _Chat messages_ earlier in this article):
        
        CCAI.shared.chatService?.messagesReceived
            .sink { [weak self] messages in
                for message in messages {
                    self?.updateChatUI(with: message)
                }
            }
            .store(in: &cancellables)
        




### Screen share issues

**Problem:** Screen share doesn't start after the session is created.

  * Cause: `CCAIScreenShare` module not initialized, or screen share key not configured.

  * Fix:

    * Ensure `CCAI.shared.initializeScreenShare()` is called with valid `ScreenShareOptions` containing your screen share key.

    * Verify that the current chat supports screen share by checking `chat?.isSupportingScreenShare == true`.

    * Subscribe to `statePublisher` and `requestPublisher` (see [_Screen share_](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice#screen_share)).




**Problem:** Full-device screen sharing isn't working.

  * Cause: Broadcast extension not configured correctly.

  * Fix:

    * Verify you added a broadcast upload extension target (not a broadcast UI extension) - clear **Include UI Extension** when creating it.

    * Both your app target and extension target must share the `io.cobrowse` Keychain Sharing entitlement.

    * Add the extension bundle ID to your app's `Info.plist` (not the extension's):
          
          <key>CBIOBroadcastExtension</key>
          <string>your.app.extension.bundle.ID.here</string>
          

    * Add `CobrowseSDK` to your broadcast extension target under Frameworks and Libraries.

    * Replace the generated `SampleHandler.swift` with:
          
          import CobrowseSDK
          class SampleHandler: CobrowseIOReplayKitExtension { }
          

    * Full-device screen sharing is only available on physical devices - it won't work in the iOS Simulator.




### General debugging tips

  1. Enable verbose logging during development to see SDK internal state.

  2. Check the CCAI Platform administrator portal to verify queue configuration, channel enablement, and operating hours.

  3. Monitor network traffic with tools like Charles Proxy or Instruments to verify API calls to `*.ccaiplatform.com`.

  4. Verify SPM package versions match - all CCAI modules should use the same SPM branch to avoid compatibility issues.




## Wrapping up

Across this five-part series, you have:

  * Set up the Headless Mobile SDK for iOS, authenticated end users, and configured push notifications (see [Headless Mobile SDK for iOS: Getting Started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started)).

  * Surfaced queues and channels, and built the full chat lifecycle including smart messages, attachments, and redaction (see [Headless Mobile SDK for iOS: Queues, Channels, and Chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat)).

  * Added voice, screen share, scheduled call, email, and external deflection links (see [Headless Mobile SDK for iOS: Voice, Screen Share, Scheduled Call, and Email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice)).

  * Layered in smart actions, web and custom forms, and after-hours and overcapacity deflection (see [Headless Mobile SDK for iOS: Smart Actions, Attachments, and Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions)).

  * Handled post-session flows, localization, error handling, end-user services, custom data, external chat transfer, reactive Combine patterns, threading, memory management, and troubleshooting (this article).




For exhaustive method signatures, complete struct definitions, and full enum listings, see the companion **Headless Mobile SDK - iOS API Reference**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
