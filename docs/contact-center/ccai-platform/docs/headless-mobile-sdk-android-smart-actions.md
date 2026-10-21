---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions/
title: Headless Mobile SDK for Android: Smart actions, attachments, and deflection \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:51:31.062106+00:00
---

# Headless Mobile SDK for Android: Smart actions, attachments, and deflection  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-smart-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for Android: Smart actions, attachments, and deflection Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to integrate and customize the Headless Mobile SDK in your Android application. It covers the smart actions, attachments, and deflection.

**Note:** This document assumes you have a working chat session as covered in [Headless Mobile SDK for Android: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat). Some smart actions can also occur during voice calls. For more information, see [Headless Mobile SDK for Android: Voice, screen share, scheduled call, and email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice).

## Configure smart actions and attachments

Smart actions allow agents and consumers to exchange rich, structured information such as photos, videos, text snippets, and biometric verification.

In the headless architecture, the SDK acts strictly as the secure transport layer. It tells you when an action is required or requested, and it securely transports the data to the CCAI Platform platform. Because you own the user interface, your app is completely responsible for building the camera screens, photo pickers, text boxes, and triggering Android's built-in biometric prompts.

### Pre-session smart actions

Pre-session actions gather context (such as an account number or a video of a broken product) before the user joins the queue, significantly reducing agent handle time.

**Note:** You must collect this media before the user joins the queue, but defer the actual upload until the in-session chat pipeline officially connects. Don't hold large assets (such as 20 MB videos or high-res photos) in memory as `ByteArray` objects while the user waits in the queue. This will cause excessive memory consumption and Android may kill your process. Instead, save the asset to the app's cache directory and hold onto the file `Uri`.

**What the SDK provides** : The rules and requirements for a specific queue (for example, whether biometric verification, photo upload, or text input is optional or mandatory before joining).

**What you build** : The pre-session UI screens (camera, text input, and biometric prompts) that appear between the user tapping a queue and entering the waiting room, as well as the disk-caching logic to safely hold media until the session connects.

#### Implementation example

This code checks the SDK's configuration to see if the chosen queue has pre-session requirements. It demonstrates how to handle a video requirement by keeping a file `Uri` reference on disk rather than holding the video in memory.
    
    
    // 1. Check requirements and collect data BEFORE joining the queue
    fun checkPreSessionRequirements(queueMenu: QueueMenu) {
        val smartActions = queueMenu.settings
        if (smartActions.isNullOrEmpty()) {
            startChat(queueMenu)
            return
        }
    
        // Example: handle a video requirement
        presentVideoPicker { localFileUri ->
            // IMPORTANT: localFileUri should point to context.cacheDir
            MySessionStateManager.pendingPreSessionVideo = localFileUri
            startChat(queueMenu)
        }
    }
    
    // 2. Upload and clean up AFTER the session officially connects
    fun handleSessionConnected() {
        val pendingVideoUri = MySessionStateManager.pendingPreSessionVideo ?: return
    
        // Upload using the standard in-session pipeline
        // then clean up the temporary file
        val file = File(pendingVideoUri.path ?: return)
        file.delete()
        MySessionStateManager.pendingPreSessionVideo = null
    }
    

#### Read pre-session smart action configuration

The SDK exposes pre-session smart action configuration through **two complementary paths**. Check both to determine whether pre-session capture is required for a given queue and channel.

#### Path A - Queue-level (`QueueMenu.settings[].sdk.preSessionSmartAction`)
    
    
    // `QueueMenuSetting` and `QueueMenuSDKSetting` (simplified)
    data class QueueMenuSetting(
        val sdk: QueueMenuSDKSetting?
        // ... other fields ...
    )
    
    data class QueueMenuSDKSetting(
        val preSessionSmartAction: Boolean?
        // ... other fields ...
    )
    
    // Usage - "does any queue-level setting require a pre-session smart action?"
    fun queueRequiresPreSession(menu: QueueMenu): Boolean {
        return menu.settings?.any { it.sdk?.preSessionSmartAction == true } ?: false
    }
    

#### Path B - Channel-level (`VoiceCallChannel.preSessionSmartAction`)
    
    
    // Usage - "does the voice channel specifically require pre-session capture?"
    val requiresPreSessionOnVoice =
        menu.channels.voiceCall?.preSessionSmartAction == true
    

Use **Path A** to decide whether to show a pre-session gate _before_ the user picks a channel. Use **Path B** for channel-specific refinements after a channel is selected (for example, only prompting before an instant voice call).

### In-session smart actions (agent-initiated)

During an active chat or voice call, an agent can click a button on their dashboard to request data from the user (for example, _Send a photo of your ID_ or _Authenticate with biometrics)._

**What the SDK provides** : Real-time events alerting your app that the agent has requested a specific type of smart action.

**What you build** : An in-chat or in-call alert notifying the user of the request, launching the appropriate built-in tool (camera, photo library, text field, or Android `BiometricPrompt`), and passing the result back to the SDK.

#### Implementation example

Here, your app listens for SDK events. When it detects an agent request, it displays an alert and then opens the appropriate Android tool.
    
    
    import androidx.biometric.BiometricPrompt
    import androidx.core.content.ContextCompat
    
    // Listen for Smart Action requests from the active SDK session.
    //
    // `SmartActionRequest` exposes a nested `smartAction: SmartAction`, and the
    // switchable type lives at `request.smartAction.type`. The `SmartActionType`
    // enum is `PascalCase: Unknown`, `Verification`, `Screenshot`, `Photo`, `Video`,
    // `TextInput`, `ScreenShare`. Use `Verification` for Face ID / fingerprint flows.
    fun handleSmartActionRequest(request: SmartActionRequest) {
        when (request.smartAction.type) {
            SmartActionType.Photo -> {
                promptUserForPhoto(message = "The agent requested a photo.") { capturedBitmap ->
                    // Send the image back to the agent using the SDK.
                    sendAttachment(image = capturedBitmap)
                }
            }
    
            SmartActionType.Verification -> {
                val executor = ContextCompat.getMainExecutor(this)
                val biometricPrompt = BiometricPrompt(this, executor,
                    object : BiometricPrompt.AuthenticationCallback() {
                        override fun onAuthenticationSucceeded(
                            result: BiometricPrompt.AuthenticationResult
                        ) {
                            sendBiometricResult(success = true)
                        }
    
                        override fun onAuthenticationFailed() {
                            sendBiometricResult(success = false)
                        }
    
                        override fun onAuthenticationError(
                            errorCode: Int, errString: CharSequence
                        ) {
                            sendBiometricResult(success = false)
                        }
                    }
                )
    
                val promptInfo = BiometricPrompt.PromptInfo.Builder()
                    .setTitle("Identity Verification")
                    .setSubtitle("Verify your identity to continue")
                    .setNegativeBtnText("Cancel")
                    .build()
    
                biometricPrompt.authenticate(promptInfo)
            }
    
            SmartActionType.TextInput -> {
                presentTextInputPrompt(message = "The agent requested text input.") { text ->
                    sendSmartActionText(text)
                }
            }
    
            SmartActionType.Video -> {
                // Agent-requested video capture. Reuse the same disk-cached file
                // pattern recommended for pre-session media keep the recording on
                // disk and pass the local Uri to the SDK rather than holding a
                // large `ByteArray` in memory.
                promptUserForVideo(message = "The agent requested a video.") { capturedVideoUri ->
                    sendAttachment(videoUri = capturedVideoUri)
                }
            }
    
            SmartActionType.Screenshot -> {
                // The SDK exposes `Screenshot` as a distinct request type the
                // user captures (or selects), a single still image of the current
                // screen. This is **not** the same as `ScreenShare`, which
                // starts a live co-browse session.
                promptUserForScreenshot(message = "The agent requested a screenshot.") { capturedBitmap ->
                    sendAttachment(image = capturedBitmap)
                }
            }
    
            SmartActionType.ScreenShare -> {
                // Hand off to the full screen share flow (see Headless Mobile SDK for Android: Voice, screen share, scheduled call, and email).
                // Don't confuse with `Screenshot`;  `ScreenShare` starts a
                // live co-browse session using `CCAIScreenShare`, while `Screenshot`
                // captures a single still frame.
                startScreenShareFlow()
            }
    
            SmartActionType.Unknown -> {
                // Future-proof: a smart action type the SDK does not recognize.
                // Log and continue; don't block the user.
                Log.w("CCAI", "Received unknown smart action type")
            }
        }
    }
    

Agent-initiated smart actions arrive through the active session's SDK events. Subscribe to the relevant chat or call events before starting the session so your app can present the appropriate customer-facing prompt as soon as a request arrives.

**Warning:** Android `BiometricPrompt` requires the AndroidX Biometric library. Add `implementation("androidx.biometric:biometric:1.2.0-alpha05")` to your `build.gradle.kts` dependencies.

#### Notify and track smart actions

Use `smartActionService` to acknowledge and update smart actions as the user progresses through them.
    
    
    val router = CommunicationRouter(
        id = chatId,
        type = CommunicationType.Chat
    )
    
    // Notify the server that a smart action has been received.
    lifecycleScope.launch {
        try {
            CCAI.smartActionService?.notifySmartActionReceived(
                router = router,
                smartActionId = smartActionId
            )
            Log.d("CCAI", "Smart action notification sent successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to notify smart action: ${e.message}")
        }
    }
    
    // Update the smart action status as the user completes it.
    lifecycleScope.launch {
        try {
            CCAI.smartActionService?.updateSmartActionStatus(
                router = router,
                smartActionId = smartActionId,
                status = SmartActionStatus.Finished
            )
            Log.d("CCAI", "Smart action status updated successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to update smart action status: ${e.message}")
        }
    }
    

If the action asks for text input, collect the text in your UI and send it through the smart action service before marking the action as finished.

### Web forms

**What the SDK provides** : APIs to fetch, display, and validate web forms triggered by agents during a chat session.

**What you build** : The web form rendering UI and the submission flow that packages the user's responses.

#### Implementation example

This code fetches a web form by its external ID and smart action ID, then validates the response before submission.
    
    
    // Fetch a web form - `fetchWebForm` takes two positional parameters on Android.
    lifecycleScope.launch {
        try {
            val webFormResponse = CCAI.chatService?.fetchWebForm(
                externalFormId = "form123",
                smartActionId = 123
            )
            if (webFormResponse != null) {
                Log.d("CCAI", "Web form received: $webFormResponse")
                // Render the web form in your custom UI.
                renderWebForm(webFormResponse)
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to fetch web form: ${e.message}")
        }
    }
    
    // Validate a web form response.
    lifecycleScope.launch {
        try {
            val isValid = CCAI.chatService?.validateWebForm(webFormResponse)
            if (isValid == true) {
                Log.d("CCAI", "Web form is valid")
            } else {
                Log.d("CCAI", "Web form validation failed")
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to validate web form: ${e.message}")
        }
    }
    

### Custom forms

**What the SDK provides** : APIs to retrieve configurable form definitions (with multiple question types) and submit the user's answers.

**What you build** : A dynamic form UI that renders each question type (text fields, dropdowns, etc.), validates input, and collects responses for submission.

#### Implementation example

This code retrieves a custom form's question definitions, then packages and submits the user's answers.
    
    
    // Retrieve custom form details
    lifecycleScope.launch {
        try {
            val formDetails = CCAI.chatService?.getCustomFormDetails(formId = 123)
            if (formDetails != null) {
                Log.d("CCAI", "Form Title: ${formDetails.title ?: "No title"}")
                Log.d("CCAI", "Questions: ${formDetails.questions.size}")
                // Render the form dynamically based on question types
                renderCustomForm(formDetails)
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to get custom form details: ${e.message}")
        }
    }
    
    // Submit a custom form
    val request = SubmitCustomFormRequest(
        smartActionId = 123,
        formResponse = listOf(
            SubmitCustomFormRequest.Answer(questionId = 1, value = "John Doe"),
            SubmitCustomFormRequest.Answer(questionId = 2, value = "john@example.com")
        )
    )
    
    lifecycleScope.launch {
        try {
            CCAI.chatService?.submitCustomForm(request = request)
            Log.d("CCAI", "Form submitted successfully")
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to submit form: ${e.message}")
        }
    }
    

For the full `CustomFormDetailsResponse`, `CustomFormQuestion`, `CustomFormQuestionOption`, and `CustomFormQuestionType` enum definitions, see the **Headless Mobile SDK — Android API Reference**.

### Consumer-initiated attachments (chat)

Users don't have to wait for an agent to ask; they can proactively send images and videos during a chat. The SDK enforces strict file size limits and automatically attempts compression before transmission.

#### Attachment size limits

  * **Images** : ≤ 2 MB

  * **Videos** : ≤ 20 MB




**What the SDK provides** : A secure upload pipeline that handles network transmission and automatically compresses files to meet CCAI Platform's limits.

**What you build** : The paperclip / attachment button in your chat UI, the photo / video picker, and the visual chat bubble showing the upload state (loading, sent, or failed).

#### Implementation example

When a user selects a photo or video from their gallery, pass the local file `Uri` to the SDK using the same `sendMessage` API used for all outgoing messages. For more information, see [Sending messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-channels-chat#sending-messages).

The SDK handles compression and upload.
    
    
    // Called when the user picks an image from their photo gallery
    fun userDidSelectImage(imageUri: Uri) {
        val messageBubble = myChatAdapter.addLoadingImageBubble()
    
        lifecycleScope.launch {
            try {
                CCAI.chatService?.sendMessage(
                    OutgoingMessageContent.Photos(
                        images = listOf(imageUri),
                        smartAction = null
                    )
                )
                messageBubble.markAsSent()
            } catch (e: Exception) {
                messageBubble.showError("Failed to send: ${e.message}")
            }
        }
    }
    

### Agent-initiated attachments (chat)

Agents can send files back to the user, including images, videos, audio clips, and documents (PDFs, CSVs, etc.).

#### Supported file types

The CCAI Platform platform accepts 19 file types across four categories. Your custom UI should handle each category gracefully (image preview, video player, audio player, document download).

Category | Supported types  
---|---  
Images | JPEG, PNG, GIF, and WebP.  
Video | MP4, MOV, AVI, WMV, and WebM.  
Audio | MP3, WAV, M4A, and WEBA.  
Documents | PDF, DOC, XLS, PPT, CSV, and TXT.  
**Note:** Agents are restricted to this list when uploading from the agent dashboard. The SDK doesn't enforce this list client-side — it surfaces whatever the platform delivered. However, planning your UI around these 19 types covers every file the agent can send.

**What the SDK provides** : Incoming chat message payloads delivered using the chat service's message `Flow` that include attachment metadata — see [Headless Mobile SDK for Android: Advanced topics, localization, and post-session flows](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-advanced-topics). The chat service also provides `downloadMedia` for retrieving agent-sent media securely.

**What you build** : The UI to render these attachments in the chat feed. Your app decides whether to show image previews, video thumbnails, audio playback controls, or document download buttons.

#### Implementation example

Observe incoming messages using the chat service's message `Flow`. When a new message includes media metadata, call `downloadMedia` before rendering or opening the file.

`downloadMedia` returns `DownloadMediaResponse { data: ByteArray, fileName: String? }` — the fully-downloaded bytes plus an optional display filename. The SDK doesn't cache downloads. If your UI scrolls back to an older bubble or re-enters the chat view, your app is responsible for caching the decoded image or persisting the bytes; calling `downloadMedia` again triggers another network fetch.
    
    
    import android.graphics.BitmapFactory
    import java.io.File
    
    lifecycleScope.launch {
        CCAI.chatService?.messagesReceived?.collect { messages ->
            for (message in messages) {
                renderIncomingMessage(message)
            }
        }
    }
    
    fun renderIncomingMessage(message: ChatMessage) {
        val media = message.media
    
        if (media == null) {
            myChatAdapter.insertTextBubble(text = message.text)
            return
        }
    
        lifecycleScope.launch {
            try {
                // `downloadMedia` returns the raw bytes plus an optional filename.
                val response = CCAI.chatService?.downloadMedia(
                    mediaId = media.id,
                    mediaType = media.type
                ) ?: return@launch
    
                when (media.type) {
                    DownloadableMediaType.Photo -> {
                        // Decode in-memory; no disk write needed.
                        val bitmap = BitmapFactory.decodeByteArray(
                            response.data, 0, response.data.size
                        )
                        myChatAdapter.insertImageBubble(
                            bitmap = bitmap,
                            fileName = response.fileName
                        )
                    }
                    DownloadableMediaType.Video,
                    DownloadableMediaType.Audio,
                    DownloadableMediaType.Document -> {
                        // Larger media usually needs an on-disk file for a player
                        // or document viewer. Write to the app's cache directory
                        // yourself and hand the resulting File/Uri to your UI.
                        val file = File(
                            applicationContext.cacheDir,
                            response.fileName ?: "attachment"
                        )
                        file.writeBytes(response.data)
                        myChatAdapter.insertAttachmentBubble(
                            file = file,
                            mediaType = media.type
                        )
                    }
                }
            } catch (e: Exception) {
                myChatAdapter.insertAttachmentErrorBubble(fileName = message.media?.name)
            }
        }
    }
    

## Deflection (after hours and over-capacity)

Deflection redirects users when your support team is unavailable. This usually happens in two scenarios:

  * **After hours** : the user tries to contact support outside of configured operating hours.

  * **Over-capacity** : the queue is open, but wait time exceeds the admin-configured threshold.




In a headless architecture, the SDK doesn't automatically block the user or pop up an error screen. Instead, it quietly passes the deflection status and the admin-configured fallback options to your app. Your app must check this status before attempting to start a session.

### Handle deflection states

**What the SDK provides** : A `deflectionFrom: List<QueueMenuDeflection>?` on `QueueMenu` that lists the **incoming deflection rules** routing other queues into this one. Each `QueueMenuDeflection` carries only two fields:

  * **`deflectionType: DeflectionType?`** : the category of deflection (for example, after-hours or over-capacity).

  * **`menuId: Int?`** : the ID of the source queue that deflects into this one.




`QueueMenuDeflection` doesn't carry a display message or a human-readable label. For the user-facing copy (for example, _Our office is closed),_ use `afterHoursMessage` of the queue (derived from `QueueMenu.settings[].afterHours`) or your own admin-configured strings. For the resolved destination queue's display name, look it up from your already-fetched menu tree by `menuId`.

**What you build** : The logic to check for these deflection states before putting a user in a queue, and the custom UI (such as a full-screen alert or a banner) that displays the appropriate message and alternative routing buttons.

#### Implementation example

The following code intercepts a user's attempt to start a chat. It checks the SDK's deflection metadata on the `QueueMenu` and, if a rule is active, presents a deflection screen using the queue's `afterHoursMessage` (or a fallback).
    
    
    fun onSupportMenuTapped(queueMenu: QueueMenu) {
        // 1. Check if any deflection rules route into this queue.
        val deflections = queueMenu.deflectionFrom
        if (!deflections.isNullOrEmpty()) {
            // Deflection is active - stop routing. Show the custom deflection screen instead.
            val message = queueMenu.afterHoursMessage?.text
                ?: "Support is currently unavailable."
            showDeflectionScreen(
                message = message,
                deflections = deflections
            )
        } else {
            // No deflection rules apply. Safe to proceed to channel selection or directly to chat/call.
            startSupportFlow(queueMenu)
        }
    }
    

### Render deflection options

When a deflection rule is active, your admins will likely configure alternative ways for the user to get help — typically by pointing at another queue (which you can resolve using `menuId`) or by surfacing the current queue's configured `afterHoursMessage`.

**What the SDK provides** : The list of `QueueMenuDeflection` entries on `deflectionFrom`, each with a `deflectionType` and `menuId`.

**What you build** : A dynamic menu that loops through these entries, resolves each `menuId` against your already-fetched menu tree to get a display name, and generates the appropriate buttons.

#### Implementation example

This code takes the deflection entries and dynamically builds a screen. It uses the source queue's name (resolved from `menuId`) as the button label, falling back to the `deflectionType` when a name isn't available.
    
    
    fun showDeflectionScreen(message: String, deflections: List<QueueMenuDeflection>) {
        // 1. Update your UI with the admin's configured message (or your fallback).
        deflectionTitleTextView.text = message
    
        // 2. Loop through the incoming deflection rules and generate buttons.
        for (deflection in deflections) {
            val sourceMenu = deflection.menuId?.let { findMenuById(it) }
            val label = sourceMenu?.name
                ?: deflection.deflectionType?.name
                ?: "Alternative option"
    
            val button = MaterialButton(this).apply {
                text = label
                setOnClickListener {
                    handleDeflectionAction(deflection)
                }
            }
            menuLinearLayout.addView(button)
        }
    
        // 3. Present the compiled screen to the user.
        deflectionContainer.isVisible = true
    }
    
    // Walk your previously fetched menu tree (for example, by using `QueueMenu.flatten()`) to resolve a `menuId`.
    private fun findMenuById(id: Int): QueueMenu? =
        cachedRootMenus.flatMap { it.flatten() }.firstOrNull { it.id == id }
    

`deflectionFrom` is the list of deflection rules that **route into** this menu — each entry's `menuId` identifies a **source** queue that deflects into the current one. Your app decides how to expose these. Some integrations present the destination queue as **here's where we'll send you instead** , while others just use the presence of any rule as a gate to show a generic **try again later** screen.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
