---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice/
title: Headless Mobile SDK for iOS: Voice, screen share, scheduled call, and email \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:44.226323+00:00
---

# Headless Mobile SDK for iOS: Voice, screen share, scheduled call, and email  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-voice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for iOS: Voice, screen share, scheduled call, and email Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the Headless Mobile SDK in your Android application. It covers voice calls through the `CCAICall`

**Note:** Inspecting available channels on a queue is covered in [Headless Mobile SDK for iOS: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-queues-channels-chat). These patterns assume you've already fetched a `QueueMenu` and are inspecting its `Channels` struct.

## Voice calls

The Headless Mobile SDK for iOS provides voice-call support through the `CCAICall` module. Your app owns the custom call UI, while the SDK handles the call connection, CallKit integration, VoIP push handling, and call lifecycle events.

**What the SDK provides** : Call-service APIs for starting instant calls, starting voicemail, handling incoming calls, and observing call state.

**What you build** : The visual call experience, including the pre-call entry point, recording-consent prompt, ringing or waiting states, in-call controls, and any post-call navigation.

### Initialize the call module

Initialize the call module after initializing the core SDK:
    
    
    import CCAIKit
    import CCAICall
    
    try CCAI.shared.initialize(options: options)
    CCAI.shared.initializeCall(CallOptions())
    

### Inspecting `VoiceCallChannel` capabilities

Before offering an instant call, inspect the queue's `VoiceCallChannel` struct to decide which entry points to expose (instant call, voicemail fallback, channel-level deflection) and whether recording consent is required.

#### Key `VoiceCallChannel` fields

  * `instantEnabled: Bool?` \- whether a live (instant) voice call is permitted for this queue. Treat `nil` or `false` as a `"don't offer an instant call button"` state. Distinct from `voiceCall != nil`, which only tells you the queue has a voice channel at all.

  * `preSessionSmartAction: Bool?` \- whether pre-session smart actions are required on this specific channel before starting a call. See [Headless Mobile SDK for iOS: Smart actions, attachments, and deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions) for the complementary queue-level path.

  * `scheduleEnabled: Bool?` \- whether scheduled calls are supported. See Scheduled calls for the complementary queue-level path.

  * `recordingOption: RecordingOption?` \- the call recording consent model (see Recording consent). Distinct from `RecordingPermission.notAsked`, which is scheduling-specific.

  * `voicemailReason: String?` \- populated when the channel is configured to route to voicemail.

  * `phoneNumber: String?` \- PSTN fallback number configured for deflection or voicemail.

  * `scheduleDeflectionType: String?` / `deflected: Bool?` / `deflectedReason: String?` \- channel-level deflection metadata. When `deflected == true`, show the admin-configured `deflectedReason` message and offer the configured fallback (for example, a phone number to dial or a scheduled-call entry point) instead of attempting an instant call. See [Deflection (after-hours and over-capacity)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-smart-actions#deflection) for queue-level deflection handling.



    
    
    func voiceEntryPoints(for menu: QueueMenu) {
        guard let voice = menu.channels?.voiceCall else {
            hideCallNowButton()
            hideVoicemailButton()
            return
        }
    
        // Instant call - only when explicitly enabled and not deflected
        callNowButton.isHidden = (voice.instantEnabled != true) || (voice.deflected == true)
    
        // Voicemail fallback
        if let number = voice.phoneNumber, voice.voicemailReason != nil {
            showVoicemailButton(number: number, reason: voice.voicemailReason)
        }
    
        // Channel-level deflection
        if voice.deflected == true {
            showChannelDeflection(reason: voice.deflectedReason)
        }
    }
    

### Recording consent

**What the SDK provides** : A `recordingOption: RecordingOption?` field on `VoiceCallChannel` that describes the call recording consent model admins configured in the portal.

**What you build** : The consent prompt (when `.askUser`) and the branching logic that honors the admin's choice.
    
    
    public enum RecordingOption: String, Decodable {
        case always   // Calls are always recorded - surface a disclosure before connecting
        case never    // Calls are never recorded - no disclosure needed
        case askUser  // Prompt the user for consent before the call connects
    }
    
    func handleRecordingConsent(
        for voice: VoiceCallChannel,
        completion: @escaping (Bool) -> Void
    ) {
        switch voice.recordingOption {
        case .always:
            showRecordingDisclosure(message: "This call will be recorded.")
            completion(true)
        case .never, .none:
            completion(true)
        case .askUser:
            presentConsentPrompt { granted in
                completion(granted)
            }
        }
    }
    

### Start an instant call

Before starting an instant call:

  1. Inspect the selected queue's `VoiceCallChannel`.

  2. Check that instant calls are enabled and not deflected.

  3. Handle recording consent according to the queue's `recordingOption`.

  4. Request microphone permission.

  5. Call `startInstantCall`.



    
    
    func initiateInstantCall(for menu: QueueMenu) async {
        guard let voice = menu.channels?.voiceCall,
              voice.instantEnabled == true,
              voice.deflected != true else {
            return
        }
    
        let recordingPermission = await resolveRecordingPermission(for: voice)
        guard await requestMicrophonePermission() else { return }
    
        do {
            try await CCAI.shared.callService?.startInstantCall(
                InstantCallRequest(
                    menuId: menu.id,
                    recordingPermission: recordingPermission
                )
            )
        } catch {
            showCallStartError(error)
        }
    }
    

### Observe call state

Subscribe to call-service events before starting or accepting a call:
    
    
    CCAI.shared.callService?.stateChanged
        .receive(on: DispatchQueue.main)
        .sink { state in
            updateCallConnectionState(state)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.callReceived
        .receive(on: DispatchQueue.main)
        .sink { call in
            updateCallDetails(call)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.incomingCallEvent
        .receive(on: DispatchQueue.main)
        .sink { event in
            handleIncomingCallEvent(event)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.waitTimeUpdated
        .receive(on: DispatchQueue.main)
        .sink { waitTime in
            // The platform pushed a new estimated wait time for the active call.
            updateEstimatedWaitTime(waitTime)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.participantUpdated
        .receive(on: DispatchQueue.main)
        .sink { participant in
            // Agent assignment, transfer, or participant metadata changed.
            updateParticipantInfo(participant)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.interruptionDetected
        .receive(on: DispatchQueue.main)
        .sink { interruption in
            // A PSTN interruption (for example, an incoming cellular call)
            // has paused the active CCAI call. Surface a "call interrupted"
            // banner and offer a Resume action after the interruption ends.
            showInterruptionBanner(reason: interruption)
        }
        .store(in: &cancellables)
    
    CCAI.shared.callService?.deflectionOffered
        .receive(on: DispatchQueue.main)
        .sink { deflection in
            // The platform offered a wait-time deflection (for example, a
            // scheduled callback or PSTN fallback). Render the prompt and
            // honor the user's choice.
            presentWaitTimeDeflection(deflection)
        }
        .store(in: &cancellables)
    

### Provider state versus server status

`stateChanged` and `callReceived.status` are independent signals — read them as columns, not rows. The provider's `stateChanged` reports the local VoIP handshake; the server-side `callReceived.status` reports the call's lifecycle on the platform. Drive the **Connected** flip and the call-timer start from `callReceived.status` — not from `stateChanged` reaching `.connected`.

Signal | What it reports | What to drive from it  
---|---|---  
`stateChanged` (provider) | Local VoIP handshake — `.connecting`, `.connected` (local), `.disconnected`, `.error(...)`. | Optional pre-status spinner before the server status arrives, error surfaces, and end-of-call cleanup.  
`callReceived.status` (server) | Server-side lifecycle — `.waiting`, `.connecting`, `.connected`, `.onHold`, `.interrupted`, `.ended`. | **Connected** flip, call-timer start, agent-assigned UI, transfer or escalation overlays, and the end-call flow.  
  
### Call status and server-side states

**What the SDK provides** : A server-driven `CallStatus` enum on each `Call` payload that describes where the call is in its lifecycle (for example, `connecting`, `waiting`, `connected`, `onHold`, `interrupted`, `ended`).

**What you build** : The mapping from `CallStatus` to the customer-facing states in your call screen (ringing, waiting in queue, connected, on hold, interrupted, ended).

#### Implementation example

Switch on `call.status` from each `callReceived` emission and render the matching UI state.
    
    
    func updateCallDetails(_ call: Call) {
        switch call.status {
        case .connecting:
            renderConnectingState()
        case .waiting:
            renderWaitingInQueueState(estimatedWait: call.estimatedWait)
        case .connected:
            renderConnectedState(agent: call.agent)
        case .onHold:
            renderOnHoldState()
        case .interrupted:
            renderInterruptedState()
        case .ended, .failed:
            renderEndedState(reason: call.endReason)
        @unknown default:
            break
        }
    }
    

### In-call controls (mute, speaker, hold)

**What the SDK provides** : Read-only properties on `callService` — `isMuted`, `isSpeakerEnabled`, `isOnHold` — alongside the actions to toggle each state (`setMuted`, `setSpeakerEnabled`, `setOnHold`).

**What you build** : The mute, speaker, and hold buttons in your in-call UI, wired to the SDK's actions and reflecting the current state.

#### Implementation example

Read the current state from `callService` to initialize your buttons, then toggle and update on tap.
    
    
    // Read current state
    muteButton.isSelected = CCAI.shared.callService?.isMuted ?? false
    speakerButton.isSelected = CCAI.shared.callService?.isSpeakerEnabled ?? false
    holdButton.isSelected = CCAI.shared.callService?.isOnHold ?? false
    
    // Toggle from your UI handlers
    func onMuteTapped() {
        let next = !(CCAI.shared.callService?.isMuted ?? false)
        CCAI.shared.callService?.setMuted(next)
        muteButton.isSelected = next
    }
    
    func onSpeakerTapped() {
        let next = !(CCAI.shared.callService?.isSpeakerEnabled ?? false)
        CCAI.shared.callService?.setSpeakerEnabled(next)
        speakerButton.isSelected = next
    }
    
    func onHoldTapped() {
        let next = !(CCAI.shared.callService?.isOnHold ?? false)
        CCAI.shared.callService?.setOnHold(next)
        holdButton.isSelected = next
    }
    

### Resume an in-progress call after interruption

When a PSTN interruption (such as an incoming cellular call) pauses the active CCAI call, the SDK keeps the session alive and emits `interruptionDetected`. After the interruption ends, your app can resume the call.

**What the SDK provides** : `getLastCallInProgress()` to look up an in-progress call (including across app restarts) and `resumeCall(_:)` to bring it back to the foreground.

**What you build** : The resume affordance in your UI (typically a banner or an automatic resume after the interruption ends) and the navigation back to your call screen.

#### Implementation example

Look up the in-progress call with `getLastCallInProgress`, resume it, and navigate back to your call screen.
    
    
    func resumeIfInterrupted() async {
        guard let call = try? await CCAI.shared.callService?.getLastCallInProgress() else {
            return
        }
        do {
            try await CCAI.shared.callService?.resumeCall(call)
            navigateToCallScreen(call)
        } catch {
            showCallResumeError(error)
        }
    }
    

### Escalation from a virtual agent

**What the SDK provides** : `canEscalate(allowSkipVirtualAgent:)` is a method on `CallResponse` (the model emitted by `callService.callReceived`), not on `callService` itself. It reports whether the current call is eligible for escalation to a human agent based on the call's current virtual-agent status.

**What you build** : Hold onto the most recent `callReceived` emission as your `"current call"` state, then bind the visibility of your **Talk to a person** button to `currentCall?.canEscalate(...)`. The `allowSkipVirtualAgent` argument is a menu-configuration value that you fetch separately from the call response itself — don't hard-code `true` in production.

#### Implementation example

Keep the latest `Call` in a stored property, then invoke `canEscalate` on it. Resolve `allowSkipVirtualAgent` from your menu configuration.
    
    
    // Held from the most recent `callReceived` emission
    private var currentCall: Call?
    
    // `allowSkipVirtualAgent` is fetched separately from menu configuration
    // it is not derived from the CallResponse.
    let allowSkip = menuConfiguration.allowSkipVirtualAgent
    let allowed = currentCall?.canEscalate(allowSkipVirtualAgent: allowSkip) ?? false
    talkToAgentButton.isHidden = !allowed
    

### Voicemail

**What the SDK provides** : `startVoicemail(_ request: VoicemailRequest)` on `callService`, plus a `VoicemailReason` enum that describes why the platform offered voicemail in the first place (for example, after-hours fallback, over-capacity fallback, or temporary redirection).

**What you build** : The voicemail entry point in your UI (typically shown when `VoiceCallChannel.voicemailReason` is populated, or when the call lifecycle resolves to a voicemail outcome) and the recording UI itself.

#### Implementation example

Surface the voicemail button when `voicemailReason` is set, then call `startVoicemail` with a `VoicemailRequest`.
    
    
    public enum VoicemailReason: String, Decodable {
        case afterHourDeflection
        case overCapacityDeflection
        case temporaryRedirection
    }
    
    func offerVoicemail(for menu: QueueMenu) async {
        guard let voice = menu.channels?.voiceCall,
              voice.voicemailReason != nil else {
            return
        }
        do {
            try await CCAI.shared.callService?.startVoicemail(
                VoicemailRequest(menuId: menu.id)
            )
        } catch {
            showVoicemailError(error)
        }
    }
    

### Wait-time deflection

When the queue is open but the wait time exceeds the admin-configured threshold, the platform can offer an alternative path — typically a scheduled callback or a PSTN deflection.

**What the SDK provides** : A `CallDeflection` payload describing the offered alternative, retrievable using `getCallDeflection(callId:)` on `callService` for the active call. The platform also emits the same payload through the `deflectionOffered` publisher when a deflection becomes available mid-wait. A separate `CompanyResponse.preventDirectPstnCall` flag indicates whether direct PSTN dialing should be hidden in your fallback UI.

**What you build** : The deflection prompt (for example, _Estimated wait is 12 minutes — schedule a callback instead?)_ and the branching logic that honors the user's choice.

#### Implementation example

Look up the active call with `getLastCallInProgress`, fetch the offered deflection with `getCallDeflection(callId:)`, combine it with `CompanyResponse.preventDirectPstnCall`, and present the prompt.
    
    
    func evaluateWaitTimeDeflection() async {
        guard let currentCall = try? await CCAI.shared.callService?.getLastCallInProgress() else {
            return
        }
        let deflection = try? await CCAI.shared.callService?.getCallDeflection(
            callId: currentCall.id
        )
        guard let offer = deflection else { return }
        let company = try? await CCAI.shared.companyService?.get()
        let allowDirectPstn = company?.preventDirectPstnCall != true
        presentWaitTimeDeflection(offer, allowDirectPstn: allowDirectPstn)
    }
    

### Audible messages (system announcements)

**What the SDK provides** : An `audibleMessageService` that resolves the admin-configured audible messages for a queue (for example, **All agents are busy**). By default, the SDK plays these messages automatically when the call enters the corresponding state.

**What you build** : Nothing, in the default mode. If you prefer to render the announcement yourself (for example, as caption text plus your own audio player), initialize the call module with `playAudibleMessages = false` and call `resolveMessages(menuId:)` directly.

#### Implementation example

Use the default initializer for the SDK-played path, or set `playAudibleMessages = false` and resolve messages yourself to render captions and play audio in your own UI.
    
    
    // Option A default: SDK plays audible messages automatically.
    CCAI.shared.initializeCall(CallOptions())
    
    // Option B your app renders the announcements manually.
    CCAI.shared.initializeCall(CallOptions(playAudibleMessages: false))
    let messages = try await CCAI.shared.audibleMessageService?.resolveMessages(
        menuId: menu.id
    )
    for message in messages ?? [] {
        renderCaption(message.text)
        playAudio(message.audioURL)
    }
    

### Advanced `CallOptions`

`CallOptions` exposes a small set of toggles for apps that need to opt out of the default call experience.

  * `playAudibleMessages: Bool` — when `false`, the SDK doesn't play system announcements; render them yourself using `audibleMessageService`.

  * `callKitEnabled: Bool` — when `false`, the SDK doesn't present the built-in CallKit screen for incoming or outgoing calls. Use this when your app needs to render its own in-app incoming-call UI instead of relying on the iOS system UI.




#### Implementation example

Pass the toggles into `CallOptions` when initializing the call module.
    
    
    // Fully custom in-app call experience
    CCAI.shared.initializeCall(
        CallOptions(
            playAudibleMessages: false,
            callKitEnabled: false
        )
    )
    

**Note:** When `callKitEnabled` is `true` (the default), iOS handles the lock-screen and ringer experience for you. When `false`, your app is responsible for presenting an incoming-call UI while in the foreground; iOS won't surface a system-level incoming-call screen.

## Screen share

Screen sharing allows support agents to view the user's screen to help troubleshoot issues. Google Cloud project supports two modes of screen sharing:

  * In-app sharing: the agent can only see what is happening inside your specific app.

  * Full-device sharing (optional): the agent can see the user's entire device, including the iOS home screen and other apps. This requires advanced iOS configuration using Apple's ReplayKit.




**What the SDK provides** : The screen share service that creates and manages sessions, handles state changes, and processes consent requests.

**What you build** : The initialization configuration, the UI prompts for user consent, and (if supporting full-device) the built-in iOS Broadcast Extension.

The screen share service provides methods for the full session lifecycle - `create`, `activate`, `end`, `clear` (iOS only) - plus configuration methods `updateOptions`, `enableRemoteControl`, and `enableFullDeviceSharing`. The next subsections walk through the core integration flow.

For complete method signatures and parameter details for all screen share methods, see the **Headless Mobile SDK - iOS API Reference**.

### Initialize and configure screen share

Before an agent can request a screen share, you must initialize and configure the service with your specific screen share license key.
    
    
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaikit.initializeScreenShare
    import com.ccaiplatform.ccaikit.models.screenShare.ScreenShareOptions
    
    // Minimal domain defaults to your instance's configured provider
    CCAI.initializeScreenShare(
        context = this,
        options = ScreenShareOptions(
            key = "YOUR_COMPANY_KEY"
        )
    )
    
    // If your instance or provider requires an explicit domain:
    // CCAI.initializeScreenShare(
    //     context = this,
    //     options = ScreenShareOptions(
    //         key = "YOUR_COMPANY_KEY",
    //         domain = "your_subdomain.ccaiplatform.com"
    //     )
    // )
    

### Check screen share eligibility

Before enabling screen share functionality, check if it's available for the current chat:
    
    
    let isChatSupportingScreenShare = CCAI.shared.screenShareService != nil
        && chat?.isSupportingScreenShare == true
    

### Handle screen share requests

Implement screen share request handling using the `screenShareService`. You create a `ScreenShareRequest` and handle the async response:
    
    
    func requestScreenShare(isFromRemote: Bool) async {
        guard let chatId = currentChatId else { return }
        guard let screenShareService = CCAI.shared.screenShareService else {
            handleError(ScreenShareError.serviceNotAvailable, message: "Request Screen Share")
            return
        }
    
        // Track whether this session is agent-initiated
        screenShareInitiatedFrom = isFromRemote ? .agent : .endUser
    
        if !isFromRemote {
            await sendScreenShareMessage(event: .screenShareRequestedFromEndUser)
        }
    
        do {
            let response = try await screenShareService.create(
                request: ScreenShareRequest(
                    communicationId: chatId,
                    communicationType: .chat,
                    initiatedFrom: isFromRemote ? .agent : .endUser
                )
            )
            await sendScreenShareMessage(event: .screenShareCodeGenerated, response: response)
        } catch {
            await sendScreenShareMessage(event: .screenShareFailed)
            handleError(error, message: "Request screen share error")
        }
    }
    

### Handle screen share state changes

Observe screen share state and requests through the service publishers. Subscribe before creating or activating a session so your UI can respond to every transition.
    
    
    CCAI.shared.screenShareService?.statePublisher
        .receive(on: DispatchQueue.main)
        .sink { state in
            currentScreenShareSessionState = state
            if state == .authorizing, screenShareInitiatedFrom == .agent {
                Task {
                    do {
                        try await handleStartSession(isAccepted: true)
                    } catch {
                        handleError(error, message: "Failed to start screen share")
                    }
                }
            }
        }
        .store(in: &cancellables)
    
    CCAI.shared.screenShareService?.requestPublisher
        .receive(on: DispatchQueue.main)
        .sink { request in
            switch request {
            case .session:
                if screenShareInitiatedFrom == .endUser {
                    showScreenSharePrompt(.startSession)
                }
            case .remoteControl:
                showScreenSharePrompt(.remoteControl)
            @unknown default:
                break
            }
        }
        .store(in: &cancellables)
    

The `ScreenShareServiceState` enum tracks session progress through `.none`, `.pending`, `.authorizing`, `.active`, and `.ended`. The request publisher emits session and remote-control requests that your app should translate into customer-facing consent prompts.

### Full-device screen sharing (advanced)

To allow agents to see screens from applications outside of your own, you must implement an Apple Broadcast Upload Extension. This allows iOS to capture the screen system-wide and hand the video frames securely to the Google Cloud project SDK.

**Warning:** Full-device screen sharing requires additional setup and is only available on physical devices (not iOS Simulator).

#### Add a broadcast extension target

  * Open your Xcode project.

  * Navigate to **File** > **New** > **Target** …

  * Select **Broadcast Upload Extension**.

  * Enter a name for the target.

  * Clear **Include UI Extension**.

  * Create the target, noting its bundle ID.

  * Change the target SDK of your broadcast extension to iOS 12.0 or higher.


**Warning:** Full-device screen sharing is delivered using the Cobrowse third-party SDK. The CCAI iOS SDK package includes Cobrowse in the package graph, but Broadcast Upload Extension targets don't automatically inherit the main app target's linked frameworks. Add CobrowseSDK manually to the Broadcast Upload Extension target under **Frameworks and Libraries**.

#### Set up keychain sharing

Your app and the app extension need to share secrets using the iOS Keychain using their own Keychain group.

  * In Xcode, go to the **Signing & Capabilities** tab for both targets.

  * Add the **Keychain Sharing** capability.

  * Add `io.cobrowse` to the **Keychain Groups** for both targets.




#### Update your main app's Info.plist

Add the extension bundle ID to your app's `Info.plist` (not the extension's `Info.plist`):
    
    
    <key>CBIOBroadcastExtension</key>
    <string>your.app.extension.bundle.ID.here</string>
    

#### Add CobrowseSDK to your broadcast extension target

In Xcode, with your broadcast extension target selected, select the **+** button under **Frameworks and Libraries** and add `CobrowseSDK` to your extension target.

#### Implement the extension handler

Xcode adds a `SampleHandler.swift` file to the target you created earlier. Replace the file's contents with the following so that it inherits from the ReplayKit extension class of the SDK:
    
    
    import CobrowseSDK
    
    class SampleHandler: CobrowseIOReplayKitExtension {
        // The Google Cloud project module automatically handles ReplayKit lifecycle methods
    }
    

#### Build and run

You're now ready to build and run your app. The full-device capability is only available on physical devices - it doesn't work in the iOS Simulator.

If you've set everything up properly, after selecting the blue circular icon you should see a screen to select your broadcast extension.

### iOS SwiftUI limitations for screen share

**Warning:** Remote control in Cobrowse iOS isn't fully supported for SwiftUI-based components, which can cause certain buttons or interactions to be non-clickable. UIKit-based components work as expected under remote control.

#### Recommended approaches for remote interaction in SwiftUI

  * Wrap key interactive elements with UIKit - for areas that need to be remotely clickable, wrap them as UIKit controls (for example, `UIButton`) using `UIViewRepresentable` or `UIViewControllerRepresentable`. This ensures remote clicks work reliably using Cobrowse's UIKit path.

  * Forward remote touches with custom touch handling - for SwiftUI areas that can't be replaced with UIKit, use Cobrowse's custom touch callbacks to forward remote touch events to your SwiftUI logic. Implementation involves using a custom `UIView` or gesture recognizer to handle callbacks, then bridging events to SwiftUI (using `UIViewRepresentable` plus a `Coordinator`, notifications, or closures).

  * Provide product-level guidance or fallback - clearly indicate on SwiftUI screens that **Agents can only view; user must tap locally** , or automatically restrict remote-control permissions on these pages while maintaining view-only access.




#### Example UIKit wrapper implementation
    
    
    struct RemoteControlButton: UIViewRepresentable {
        let title: String
        let action: () -> Void
    
        func makeUIView(context: Context) -> UIButton {
            let button = UIButton(type: .system)
            button.setTitle(title, for: .normal)
            button.addTarget(
                context.coordinator,
                action: #selector(Coordinator.buttonTapped),
                for: .touchUpInside
            )
            return button
        }
    
        func updateUIView(_ uiView: UIButton, context: Context) {
            uiView.setTitle(title, for: .normal)
        }
    
        func makeCoordinator() -> Coordinator {
            Coordinator(action: action)
        }
    
        class Coordinator: NSObject {
            let action: () -> Void
    
            init(action: @escaping () -> Void) {
                self.action = action
            }
    
            @objc func buttonTapped() {
                action()
            }
        }
    }
    
    // Usage in SwiftUI
    struct ContentView: View {
        var body: some View {
            VStack {
                Text("This screen supports remote control")
                RemoteControlButton(title: "Clickable Button") {
                    print("Button tapped remotely or locally")
                }
            }
        }
    }
    

## Scheduled calls

Scheduled calls let end users book a future voice call instead of waiting in queue for an instant call. In the iOS headless SDK, use queue and channel metadata to decide whether to show a scheduling entry point in your app.

### Capability detection

**What the SDK provides** : A `scheduleEnabled` flag on `VoiceCallChannel` that tells you whether the selected queue supports booking future calls — independent of whether instant (live) voice calls are available.

**What you build** : The logic to check this flag before showing your scheduling entry point.

#### Implementation example

Check `scheduleEnabled` on the queue's voice call channel. **Don't** use `voiceCall != nil` as a proxy — a queue can support instant voice calls without supporting scheduled calls, and the other way around.
    
    
    func setupScheduledCallEntryPoint(for menu: QueueMenu) {
        guard let voiceChannel = menu.channels?.voiceCall else {
            // No voice channel at all hide both instant and scheduled call buttons
            hideCallNowButton()
            hideScheduleCallButton()
            return
        }
    
        // Instant voice call always show if voiceCall channel exists
        showCallNowButton()
    
        // Scheduled call check scheduleEnabled explicitly
        if voiceChannel.scheduleEnabled == true {
            showScheduleCallButton()
        } else {
            hideScheduleCallButton()
        }
    }
    

**Warning:** `scheduleEnabled` and instant call availability are independent. A voice-enabled queue can support one without the other. Always check `scheduleEnabled` explicitly for scheduling support - don't assume that a queue with voice calls also supports scheduling.

#### Data model reference
    
    
    // VoiceCallChannel.swift
    public struct VoiceCallChannel: Decodable {
        // ...
        public let scheduleEnabled: Bool?  // true if scheduled calls are supported
        // ...
    }
    
    // ChannelType.swift
    public enum ChannelType {
        case scheduleCall(deflectionType: DeflectionType?)
        // ...
    }
    

You can also check for `.scheduleCall` in the enabled channels list returned by `QueueMenu.getEnabledChannels()`.

### Fetch available time slots

The headless call service can fetch available appointment times for the selected queue. Your app owns the calendar or time-picker UI.

**What the SDK provides** : Available slot timestamps for the selected queue, with optional support for rescheduling an existing scheduled call.

**What you build** : The calendar, time picker, timezone presentation, empty-state handling, and retry behavior.

#### Implementation example

Call `getScheduledTimeSlots` with the queue menu ID. When rescheduling, pass the existing scheduled-call ID so the service can return the appropriate availability.
    
    
    let slots = try await CCAI.shared.callService?.getScheduledTimeSlots(
        menuId: menu.id,
        callIdForRescheduling: nil
    ) ?? []
    

When rescheduling an existing scheduled call, pass the existing call ID so the service can return the appropriate availability:
    
    
    let slots = try await CCAI.shared.callService?.getScheduledTimeSlots(
        menuId: menu.id,
        callIdForRescheduling: existingCallId
    ) ?? []
    

### Create a scheduled call

After the user selects a time slot, create the scheduled call through `callService`.

**What the SDK provides** : A `createScheduledCall` API that books the selected slot and returns the scheduled-call record.

**What you build** : E.164 phone-number validation, confirmation UI, local persistence of the scheduled-call ID, and recovery for scheduling errors.

#### Implementation example

Pass the selected slot, phone number, queue ID, and `RecordingPermission.notAsked` in a `ScheduledCallRequest`.
    
    
    let response = try await CCAI.shared.callService?.createScheduledCall(
        ScheduledCallRequest(
            menuId: menu.id,
            phoneNumber: userPhoneNumber,
            scheduleTime: selectedSlot,
            recordingPermission: .notAsked,
            callIdForRescheduling: nil,
            customData: nil,
            ticketId: nil
        )
    )
    saveScheduledCallId(response?.id)
    

The phone number must be in E.164 format, such as `+14155551234`.

### Reschedule a scheduled call

To reschedule, pass the existing scheduled-call ID as `callIdForRescheduling`.

**What the SDK provides** : The same time-slot and creation APIs, with `callIdForRescheduling` used to identify the existing booking.

**What you build** : The `"change time"` UI, local lookup of the stored scheduled-call ID, and updated confirmation state after the new booking is created.

#### Implementation example

Pass the existing call ID to `createScheduledCall` after the user selects a new slot.
    
    
    let response = try await CCAI.shared.callService?.createScheduledCall(
        ScheduledCallRequest(
            menuId: menu.id,
            phoneNumber: userPhoneNumber,
            scheduleTime: newSelectedSlot,
            recordingPermission: .notAsked,
            callIdForRescheduling: existingCallId,
            customData: nil,
            ticketId: nil
        )
    )
    saveScheduledCallId(response?.id)
    

### Cancel a scheduled call

When the user cancels an upcoming call, call `cancelScheduledCall` and clear the locally stored call ID.

**What the SDK provides** : A cancellation API for a scheduled-call ID.

**What you build** : The confirmation prompt, cancellation success or error UI, and cleanup of any locally stored upcoming-call state.

#### Implementation example

Call `cancelScheduledCall(callId:)` with the stored ID, then remove the ID from your app's storage.
    
    
    try await CCAI.shared.callService?.cancelScheduledCall(callId: existingCallId)
    clearScheduledCallId()
    

Persist the scheduled-call ID in your app if you want to offer an upcoming call state, reschedule, or cancel experiences after the app restarts.

## Email

**Important:** Email composition and submission are entirely handed off to your built-in app. Because the Google Cloud project SDK doesn't built-inly send the email payload, it can't automatically track if an email was successfully sent. You must use Apple's built-in delegates to track the submission and log it to your own analytics platform.

**What the SDK provides** : The destination email address configured for that specific queue, alongside any instructions the administrator wants the user to see (for example, **Include your account number**).

**What you build** : The email composer screen and the delegate to track its completion. You can build your own custom form, or use Apple's built-in `MFMailComposeViewController`.

#### Implementation example

This code pulls the support email address and instructions from the SDK. It opens the built-in iOS mail composer and uses the `MFMailComposeViewControllerDelegate` to listen for the exact moment the user selects **Send** or **Cancel**.
    
    
    import UIKit
    import MessageUI
    
    class SupportViewController: UIViewController, MFMailComposeViewControllerDelegate {
        // 1. Trigger the email flow
        func openEmailComposer(for menu: QueueMenu) {
            guard let emailChannel = menu.channels?.email else { return }
    
            if MFMailComposeViewController.canSendMail() {
                let mail = MFMailComposeViewController()
                mail.mailComposeDelegate = self
    
                // Use the metadata provided by the SDK
                mail.setToRecipients([emailChannel.email].compactMap { $0 })
                mail.setMessageBody(emailChannel.instructionMessage ?? "", isHTML: false)
                present(mail, animated: true)
            } else {
                showError("Mail services are not configured on this device.")
            }
        }
    
        // 2. Track the outcome using Apple's delegate
        func mailComposeController(
            _ controller: MFMailComposeViewController,
            didFinishWith result: MFMailComposeResult,
            error: Error?
        ) {
            controller.dismiss(animated: true)
    
            switch result {
            case .sent:
                print("Email successfully sent!")
            case .cancelled:
                print("User cancelled the email.")
            case .saved:
                print("Email saved as draft.")
            case .failed:
                print("Email failed to send: \(error?.localizedDescription ?? "Unknown error")")
            @unknown default:
                break
            }
        }
    }
    

## External deflection links

**What the SDK provides** : A list of URLs (such as your company's Help Center, refund policy, or a partner app) and their display titles, exactly as configured in the administrator portal.

**What you build** : The logic to execute those links when a user selects them - either by opening them in a built-in in-app browser or sending them out to the Safari app.

#### Implementation example

This helper takes a URL string and presents it in Apple's in-app browser.
    
    
    import SafariServices
    
    func openHelpCenterLink(_ urlString: String) {
        guard let url = URL(string: urlString) else { return }
        let safariViewController = SFSafariViewController(url: url)
        present(safariViewController, animated: true)
    }
    

#### Full integration example (iterate all enabled links)

On iOS, `ExternalDeflectionLink` doesn't carry a top-level `url` \- the links live inside an inner `links: [ExternalDeflection]?` array, and each enabled entry contributes one button to the channel menu. Iterate the array and skip any entries whose `enabled` flag isn't `true`.
    
    
    func setupDeflectionLinks(for queueMenu: QueueMenu) {
        // Clear any previously-rendered buttons
        helpCenterStackView.arrangedSubviews.forEach { $0.removeFromSuperview() }
    
        guard let links = queueMenu.channels?.externalDeflectionLink?.links,
              !links.isEmpty else {
            helpCenterStackView.isHidden = true
            return
        }
    
        helpCenterStackView.isHidden = false
    
        for link in links where link.enabled == true {
            let button = UIButton(type: .system)
            button.setTitle(link.displayName, for: .normal)
            button.addAction(UIAction { [weak self] _ in
                self?.openHelpCenterLink(link.url)
            }, for: .touchUpInside)
            helpCenterStackView.addArrangedSubview(button)
        }
    }
    

`ExternalDeflectionLink` exposes `enabled: Bool?` and `links: [ExternalDeflection]?`. Each `ExternalDeflection` carries its own `url` and `displayName`. If `QueueMenu.getEnabledChannels()` is used, the SDK emits one `.externalDeflection(url:displayName:)` entry per enabled link - so iterating `links` directly and iterating the enabled-channels output produce the same set of buttons.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
