---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions/
title: Headless Mobile SDK for iOS: Smart actions, attachments, and deflection \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:49.592970+00:00
---

# Headless Mobile SDK for iOS: Smart actions, attachments, and deflection  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for iOS: Smart actions, attachments, and deflection Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the Headless Mobile SDK in your Android application. It covers everything that adds rich, structured information to your support sessions: pre-session smart actions for context capture, in-session smart actions triggered by agents (including biometric verification with `LocalAuthentication`), web and custom forms, consumer- and agent-initiated attachments, and deflection handling for after-hours and over-capacity scenarios.

**Note:** This document assumes you have a working chat session as covered in [Headless Mobile SDK for iOS: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat). Some smart actions can also occur during voice calls (covered in [Headless Mobile SDK for iOS: Voice, screen share, scheduled call, and email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice)).

## Configure smart actions and attachments

Smart actions allow agents and consumers to exchange rich, structured information such as photos, videos, text snippets, and biometric verification (Face ID and Touch ID).

In the Headless architecture, the SDK acts strictly as the secure transport layer. It tells you when an action is required or requested, and it securely transports the data to the Google Cloud project platform. Because you own the user interface, your app is completely responsible for drawing the camera screens, photo pickers, text boxes, and triggering Apple's Face ID prompts.

### Pre-session smart actions

Pre-session actions gather context (such as an account number or a video of a broken product) before the user joins the queue, significantly reducing agent handle time.

**Note:** In the current release, you must collect this media before the user joins the queue, but defer the actual upload until the in-session chat pipeline officially connects. Don't hold large assets (such as 20 MB videos or high-res photos) in memory as `Data` objects while the user waits in the queue. This will cause excessive memory consumption and iOS may terminate your app in the background. Instead, save the asset to the device's temporary disk directory and hold onto the file `URL`.

**What the SDK provides** : The rules and requirements for a specific queue (for example, whether biometric verification, photo upload, or text input is optional or mandatory before joining).

**What you build** : The pre-session UI screens (camera, text input, and Face ID prompts) that appear between the user tapping a queue and entering the waiting room, as well as the disk-caching logic to safely hold media until the session connects.

#### Implementation example

This code checks the SDK's configuration to see if the chosen queue has pre-session requirements. It demonstrates how to handle a video requirement by keeping a file URL reference on disk rather than holding the video in memory.
    
    
    // 1. Check requirements and collect data BEFORE joining the queue
    func checkPreSessionRequirements(for menu: QueueMenu) {
        guard let smartActions = menu.settings else {
            startChat(for: menu)
            return
        }
    
        // Example: handle a video requirement
        presentVideoPicker { (localFileURL) in
            // IMPORTANT: localFileURL should point to NSTemporaryDirectory()
            MySessionStateManager.shared.pendingPreSessionVideo = localFileURL
            self.startChat(for: menu)
        }
    }
    
    // 2. Upload and clean up AFTER the session officially connects
    func handleSessionConnected() {
        guard let pendingVideoURL = MySessionStateManager.shared.pendingPreSessionVideo else { return }
    
        // Upload using the standard in-session pipeline
        // then clean up the temporary file
        try? FileManager.default.removeItem(at: pendingVideoURL)
        MySessionStateManager.shared.pendingPreSessionVideo = nil
    }
    

#### Reading pre-session smart action configuration

The SDK exposes pre-session smart action configuration through **two complementary paths**. Check both to determine whether pre-session capture is required for a given queue and channel.

**Path A - queue-level (`QueueMenu.settings[].sdk.preSessionSmartAction`)**:
    
    
    public struct QueueMenuSetting: Decodable {
        public let sdk: QueueMenuSDKSetting?
        // ... other fields ...
    }
    
    public struct QueueMenuSDKSetting: Decodable {
        public let preSessionSmartAction: Bool?
        // ... other fields ...
    }
    
    // Usage - "does any queue-level setting require a pre-session smart action?"
    func queueRequiresPreSession(_ menu: QueueMenu) -> Bool {
        return menu.settings?.contains { $0.sdk?.preSessionSmartAction == true } ?? false
    }
    

**Path B - channel-level (`VoiceCallChannel.preSessionSmartAction`)**:
    
    
    // Usage - "does the voice channel specifically require pre-session capture?"
    let requiresPreSessionOnVoice =
        menu.channels?.voiceCall?.preSessionSmartAction == true
    

Use **Path A** to decide whether to show a pre-session gate _before_ the user picks a channel. Use **Path B** for channel-specific refinements after a channel is selected (for example, only prompting before an instant voice call).

### In-session smart actions (agent-initiated)

During an active chat or voice call, an agent can select a button on their dashboard to request data from the user (for example, "Send a photo of your ID" or "Authenticate with Face ID").

**What the SDK provides** : Real-time events alerting your app that the agent has requested a specific type of smart action.

**What you build** : An in-chat or in-call alert notifying the user of the request, launching the appropriate built-in tool (camera, photo library, text field, or Face ID), and passing the result back to the SDK.

#### Implementation example

Here, your app listens for SDK events. When it detects an agent request, it displays an alert and then opens the appropriate iOS tool.
    
    
    // Listen for Smart Action requests from the active SDK session.
    //
    // `SmartActionType` exposes the following cases: `.photo`, `.video`,
    // `.screenshot`, `.text`, `.verification`, `.screenShare`, `.unknown`.
    // Use `.verification` (not `.biometric`) for Face ID / Touch ID flows -
    // there is no `.biometric` case on the enum.
    func handleSmartActionRequest(_ request: SmartActionRequest) {
        switch request.type {
        case .photo:
            promptUserForPhoto(message: "The agent requested a photo.") { capturedImage in
                // Send the image back to the agent using the SDK
                self.sendAttachment(image: capturedImage)
            }
    
        case .video:
            // Agent-requested video capture. Reuse the same disk-caching pattern
            // recommended for pre-session media - keep the recording on disk and
            // pass the file URL to the SDK rather than holding the raw `Data` in
            // memory.
            promptUserForVideo(message: "The agent requested a video.") { capturedVideoURL in
                self.sendAttachment(videoURL: capturedVideoURL)
            }
    
        case .screenshot:
            // The SDK exposes `.screenshot` as a distinct request type - the user
            // captures (or selects) a single still image of the current screen.
            // This is **not** the same as the following `.screenShare` case, which starts a
            // live co-browse session.
            promptUserForScreenshot(message: "The agent requested a screenshot.") { capturedImage in
                self.sendAttachment(image: capturedImage)
            }
    
        case .verification:
            // Use Face ID / Touch ID using LocalAuthentication. The SDK exposes
            // this case as `.verification`; there is no `.biometric` case on
            // `SmartActionType`.
            performAppleBiometricAuth { success in
                self.sendBiometricResult(success: success)
            }
    
        case .text:
            presentTextInputPrompt(message: "The agent requested text input.") { text in
                self.sendSmartActionText(text)
            }
    
        case .screenShare:
            // Hand off to the full screen share flow (see Headless Mobile SDK for iOS: Voice, Screen Share, Scheduled Call, and Email).
            // Don't confuse this with `.screenshot` described earlier - `.screenShare` starts a
            // live co-browse session using `CCAIScreenShare`, while `.screenshot`
            // captures a single still frame.
            startScreenShareFlow()
    
        case .unknown:
            // Future-proof: a smart action type the SDK doesn't recognize.
            // Log and continue - don't block the user.
            print("CCAI: received unknown smart action type")
    
        @unknown default:
            // Defensive: handle any cases added to `SmartActionType` in future
            // SDK releases.
            break
        }
    }
    

#### Notifying and tracking smart actions

Use `smartActionService` to acknowledge and update smart actions as the user progresses through them.
    
    
    let router = CommunicationRouter(id: chatId, type: .chat)
    
    // Notify the server that a smart action has been received
    do {
        try await CCAI.shared.smartActionService?.notifySmartActionReceived(
            router: router,
            smartActionId: smartActionId
        )
        print("Smart action notification sent successfully")
    } catch {
        print("Failed to notify smart action: \(error)")
    }
    
    // Update the smart action status as the user completes it
    do {
        try await CCAI.shared.smartActionService?.updateSmartActionStatus(
            router: router,
            smartActionId: smartActionId,
            status: .finished
        )
        print("Smart action status updated successfully")
    } catch {
        print("Failed to update smart action status: \(error)")
    }
    

If the action asks for text input, collect the text in your UI and send it through the smart action service before marking the action as finished.

### Web forms

**What the SDK provides** : APIs to fetch, display, and validate web forms triggered by agents during a chat session.

**What you build** : The web form rendering UI and the submission flow that packages the user's responses.

#### Implementation example

This code fetches a web form by its smart action ID and external form ID, then validates the response before submission.
    
    
    // Fetch a web form - WebFormRequest has no `signature` parameter on iOS
    let webFormRequest = WebFormRequest(
        smartActionId: 123,
        externalFormId: "form123"
    )
    
    do {
        let webFormResponse = try await CCAI.shared.chatService?.fetchWebForm(webFormRequest)
        if let response = webFormResponse {
            print("Web form received: \(response)")
        }
    } catch {
        print("Failed to fetch web form: \(error)")
    }
    
    // Validate a web form response
    do {
        let isValid = try await CCAI.shared.chatService?.validateWebForm(webFormResponse)
        if isValid == true {
            print("Web form is valid")
        } else {
            print("Web form validation failed")
        }
    } catch {
        print("Failed to validate web form: \(error)")
    }
    

For the full `WebFormResponse`, `FormPayload`, and `WebFormData` struct definitions, see the **Headless Mobile SDK - iOS API reference**.

### Custom forms

**What the SDK provides** : APIs to retrieve configurable form definitions (with multiple question types) and submit the user's answers.

**What you build** : A dynamic form UI that renders each question type (such as text fields and dropdowns), validates input, and collects responses for submission.

#### Implementation example

This code retrieves a custom form's question definitions, then packages and submits the user's answers.
    
    
    // Retrieve custom form details
    do {
        let form = CustomForm(
            id: 123,
            name: nil,
            title: nil,
            subtitle: nil,
            smartActionId: nil,
            image: nil,
            header: nil,
            footer: nil
        )
        let formDetails = try await CCAI.shared.chatService?.getCustomFormDetails(form)
        if let details = formDetails {
            print("Form Title: \(details.title ?? "No title")")
            print("Questions: \(details.questions.count)")
        }
    } catch {
        print("Failed to get custom form details: \(error)")
    }
    
    // Submit a custom form
    let request = SubmitCustomFormRequest(
        smartActionId: 123,
        formResponse: [
            SubmitCustomFormRequest.Answer(questionId: 1, value: "John Doe"),
            SubmitCustomFormRequest.Answer(questionId: 2, value: "john@example.com")
        ]
    )
    
    do {
        try await CCAI.shared.chatService?.submitCustomForm(request: request)
        print("Form submitted successfully")
    } catch {
        print("Failed to submit form: \(error)")
    }
    

For the full `CustomFormDetailsResponse`, `CustomFormQuestion`, `CustomFormQuestionOption`, and `CustomFormQuestionType` enum definitions, see the **Headless Mobile SDK - iOS API reference**.

### Consumer-initiated attachments (chat)

Users don't have to wait for an agent to ask; they can proactively send images and videos during a chat. The SDK enforces strict file size limits and automatically attempts compression before transmission.

#### Attachment size limits

  * Images: ≤ 2 MB

  * Videos: ≤ 20 MB




**What the SDK provides** : A secure upload pipeline that handles network transmission and automatically compresses files to meet Google Cloud project's limits.

**What you build** : The paperclip / attachment button in your chat UI, the photo / video picker, and the visual chat bubble showing the upload state (loading, sent, or failed).

#### Implementation example

When a user selects a photo or video from their camera roll, convert it to `Data` (for images) or get the local file URL (for videos), then pass it to the SDK using the same `sendMessage` API used for all outgoing messages (see the _Sending messages_ section in [Headless Mobile SDK for iOS: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat)). The SDK handles compression and upload.
    
    
    import PhotosUI
    
    // Called when the user picks an image from their photo library
    func userDidSelectImage(_ image: UIImage) {
        guard let imageData = image.jpegData(compressionQuality: 0.8) else { return }
    
        // Show a loading bubble in your custom chat UI
        let messageBubble = myChatUI.addLoadingImageBubble()
    
        Task {
            do {
                // Wrap the raw data in an UploadableImage
                let uploadableImage = UploadableImage(data: imageData, mimeType: "image/jpeg")
    
                // Pass to the SDK - compression and upload are handled automatically
                try await CCAI.shared.chatService?.sendMessage(
                    .images(images: [uploadableImage], smartAction: nil)
                )
                messageBubble.markAsSent()
            } catch {
                // The SDK returns an error if the file exceeds limits even after compression
                messageBubble.showError("Failed to send: \(error.localizedDescription)")
            }
        }
    }
    
    // Called when the user picks a video from their photo library
    func userDidSelectVideo(at localURL: URL) {
        let messageBubble = myChatUI.addLoadingVideoBubble()
    
        Task {
            do {
                let uploadableVideo = UploadableVideo(url: localURL, mimeType: "video/mp4")
                try await CCAI.shared.chatService?.sendMessage(
                    .videos(videos: [uploadableVideo], smartAction: nil)
                )
                messageBubble.markAsSent()
            } catch {
                messageBubble.showError("Failed to send: \(error.localizedDescription)")
            }
        }
    }
    

### Agent-initiated attachments (chat)

Agents can send files back to the user, including images, videos, audio clips, and documents (PDFs, CSVs, etc.).

#### Supported file types

The Google Cloud project platform accepts 19 file types across four categories. Your custom UI should handle each category gracefully (image preview, video player, audio player, document download).

Category | Supported types  
---|---  
Images | JPEG, PNG, GIF, and WebP.  
Video | MP4, MOV, AVI, WMV, and WebM.  
Audio | MP3, WAV, M4A, and WEBA.  
Documents | PDF, DOC, XLS, PPT, CSV, and TXT.  
**Note:** Agents are restricted to this list when uploading from the agent dashboard. The SDK doesn't enforce this list client-side - it exposes whatever the platform delivered - but planning your UI around these 19 types covers every file the agent can send.

**What the SDK provides** : Incoming chat message payloads (delivered using the `messagesReceived` Combine publisher - see the _Reactive patterns with Combine_ section in [Headless Mobile SDK for iOS: Post-session and advanced topics](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-advanced-topics) that include attachment metadata. The chat service also provides `downloadMedia` for retrieving agent-sent media securely.)

**What you build** : The UI to render these attachments in the chat feed. Your app decides whether to show image previews, video thumbnails, audio playback controls, or document download buttons.

#### Implementation example

Subscribe to incoming messages using `messagesReceived`. When a new message includes media metadata, call `downloadMedia` before rendering or opening the file.

`downloadMedia` returns `DownloadMediaResponse { data: Data, fileName: String? }` — the fully-downloaded bytes plus an optional display filename. The SDK doesn't cache downloads. If your UI scrolls back to an older bubble or re-enters the chat view, your app is responsible for caching the decoded image or persisting the bytes; calling `downloadMedia` again triggers another network fetch.
    
    
    import Combine
    
    private var cancellables = Set<AnyCancellable>()
    
    CCAI.shared.chatService?.messagesReceived
        .receive(on: DispatchQueue.main)
        .sink { [weak self] messages in
            for message in messages {
                self?.renderIncomingMessage(message)
            }
        }
        .store(in: &cancellables)
    
    func renderIncomingMessage(_ message: ChatMessage) {
        guard let media = message.media else {
            myChatUI.insertTextBubble(text: message.text)
            return
        }
    
        Task {
            do {
                // `downloadMedia` returns the raw bytes plus an optional filename.
                // First arg is unlabeled.
                let response = try await CCAI.shared.chatService?.downloadMedia(
                    media.id,
                    mediaType: media.type
                )
                guard let response else { return }
    
                await MainActor.run {
                    switch media.type {
                    case .photo:
                        // Decode in-memory - no disk write needed.
                        if let image = UIImage(data: response.data) {
                            myChatUI.insertImageBubble(
                                image: image,
                                fileName: response.fileName
                            )
                        }
                    case .video, .audio, .document:
                        // Larger media usually needs an on-disk URL for AVPlayer
                        // or QLPreviewController. Write to the temp directory
                        // yourself and hand the resulting URL to your UI helper.
                        let url = FileManager.default
                            .temporaryDirectory
                            .appendingPathComponent(response.fileName ?? "attachment")
                        try? response.data.write(to: url)
                        myChatUI.insertAttachmentBubble(
                            fileURL: url,
                            mediaType: media.type
                        )
                    }
                }
            } catch {
                await MainActor.run {
                    myChatUI.insertAttachmentErrorBubble(fileName: message.media?.name)
                }
            }
        }
    }
    

For the exact chat message and media metadata types, see the **Headless Mobile SDK — iOS API reference.**

## Deflection (after-hours and over-capacity)

Deflection is a critical contact center feature that redirects users when your support team is unavailable. This usually happens in two scenarios:

  * After hours: the user tries to contact support outside of your configured operating hours.

  * Over-capacity: the queue is open, but the wait time exceeds the maximum threshold set by your admins.




In a headless architecture, the SDK doesn't automatically block the user or pop up an error screen. Instead, it quietly passes the deflection status and the admin-configured fallback options to your app. Your app must check this status before attempting to start a session.

### Handle deflection states

**What the SDK provides** : A `deflectionFrom: [QueueMenuDeflection]?` on `QueueMenu` that lists the **incoming deflection rules** routing other queues into this one. Each `QueueMenuDeflection` carries only two fields:

  * `deflectionType: DeflectionType?` \- the category of deflection (for example, after-hours or over-capacity).

  * `menuId: Int?` \- the ID of the source queue that deflects into this one.




`QueueMenuDeflection` doesn't carry a display message or a human-readable label. For user-facing copy, walk the `settings` array yourself (or fall back to your own admin-configured strings). For the resolved source queue's display name, use the `findMenu(byId:)` extension on `[QueueMenu]` to look it up in your already-fetched menu tree.

**What you build** : The logic to check for these deflection states before putting a user in a queue, and the custom UI (such as a full-screen alert or a banner) that displays the appropriate message and alternative routing buttons.

#### Implementation example

The following code intercepts a user's attempt to start a chat. It checks the SDK's deflection metadata on the `QueueMenu` and, if a rule is active, resolves the after-hours message from the queue's settings and presents a deflection screen.
    
    
    // Helper - pull the first after-hours message text out of the queue's settings
    func afterHoursMessageText(for menu: QueueMenu) -> String? {
        return menu.settings?
            .compactMap { $0.afterHours?.message?.text }
            .first
    }
    
    // Called when the user taps "Start Chat" in your app
    func attemptToStartChat(for menu: QueueMenu) {
        // 1. Check if any deflection rules route into this queue
        if let deflections = menu.deflectionFrom, !deflections.isEmpty {
            let message = afterHoursMessageText(for: menu)
                ?? "Support is currently unavailable."
            showDeflectionScreen(message: message, deflections: deflections)
        } else {
            // No deflection rules apply. Safe to start the chat.
            Task {
                await startChat(for: menu)
            }
        }
    }
    

### Render deflection options

When a deflection rule is active, your admins will likely configure alternative ways for the user to get help - typically by pointing at another queue (which you can resolve using `menuId`) or by displaying the current queue's after-hours text.

**What the SDK provides** : The list of `QueueMenuDeflection` entries on `deflectionFrom`, each with a `deflectionType` and `menuId`.

**What you build** : A dynamic menu that loops through these entries, resolves each `menuId` against your already-fetched menu tree to get a display name, and generates the appropriate buttons.

#### Implementation example

This code takes the deflection entries and dynamically builds a screen. It resolves the source queue's name using the SDK-provided `findMenu(byId:)` extension on `[QueueMenu]`, falling back to the `deflectionType` name when a queue name is unavailable.
    
    
    func showDeflectionScreen(
        message: String,
        deflections: [QueueMenuDeflection],
        cachedRootMenus: [QueueMenu]
    ) {
        // 1. Update your UI with the resolved message (or your fallback)
        deflectionTitleLabel.text = message
    
        // 2. Loop through the incoming deflection rules and generate buttons
        for deflection in deflections {
            let sourceMenu = deflection.menuId.flatMap { cachedRootMenus.findMenu(byId: $0) }
            let label = sourceMenu?.name
                ?? deflection.deflectionType.map { String(describing: $0) }
                ?? "Alternative option"
    
            let button = createButton(title: label) {
                self.handleDeflectionAction(deflection)
            }
            menuStackView.addArrangedSubview(button)
        }
    
        // 3. Present the compiled screen to the user
        present(deflectionViewController, animated: true)
    }
    

`deflectionFrom` is the list of deflection rules that **route into** this menu - each entry's `menuId` identifies a **source** queue that deflects into the current one. Your app decides how to present these: some integrations present the destination queue as "here's where we'll send you instead," while others use the presence of any rule as a gate to show a generic "try again later" screen.

**Tip:** The iOS SDK ships a recursive-search extension on `[QueueMenu]` \- `func findMenu(byId id: Int) -> QueueMenu?` \- that walks the menu tree (roots and all descendants) and returns the first match. Use it instead of implementing your own traversal.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
