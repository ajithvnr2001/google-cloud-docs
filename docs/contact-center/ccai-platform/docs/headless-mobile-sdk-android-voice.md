---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice/
title: Headless Mobile SDK for Android: Voice, screen share, scheduled calls, and email \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:11:59.159856+00:00
---

# Headless Mobile SDK for Android: Voice, screen share, scheduled calls, and email  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for Android: Voice, screen share, scheduled calls, and email Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the Headless Mobile SDK in your Android application. It covers the voice, Screen Share, scheduled calls, and email.

**Note:** Inspecting available channels on a queue is covered in [Headless Mobile SDK for Android: Queues, channels, and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-queues-channels-chat). The patterns outlined in the this document assume you've already fetched a `QueueMenu` and are inspecting its `Channels` data class.

## Voice call

The Headless Mobile SDK for Android provides voice-call support through the `CCAICall` and `CCAICallRed` modules. Your app owns the custom call UI, while the SDK handles call creation, incoming-call handling, provider integration, and call lifecycle state.

**What the SDK provides** : Call-service APIs for starting instant calls, starting voicemail, handling incoming calls, and observing call state.

**What you build** : The visual call experience, including the pre-call entry point, recording-consent prompt, ringing or waiting states, in-call controls, foreground-service UI, and any post-call navigation.

### Initialize the call module

Initialize the call module after initializing the core SDK:
    
    
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaicall.CallOptions
    import com.ccaiplatform.ccaicall.initializeCall
    
    CCAI.initialize(context = applicationContext, options = initOptions)
    
    CCAI.initializeCall(
        context = applicationContext,
        options = CallOptions()
    )
    

### Inspect `VoiceCallChannel` capabilities

Before offering an instant call, inspect the queue's `VoiceCallChannel` to decide which entry points are exposed (instant call, voicemail fallback, channel-level deflection) and whether recording consent is required.

#### Key `VoiceCallChannel` fields

  * **`instantEnabled`** : `Boolean` — whether a live (instant) voice call is permitted for this queue. Treat `false` as "don't offer an instant call button". Distinct from `voiceCall != null`, which only tells you the queue has a voice channel at all.

  * **`preSessionSmartAction`** : `Boolean` — whether pre-session smart actions are required on this specific channel before starting a call. See [Pre-session smart actions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice/) in [Headless Mobile SDK for Android: Smart Actions, Attachments, and Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-voice/) for the complementary queue-level path.

  * **`scheduleEnabled`** : `Boolean` — whether scheduled calls are supported. See the Scheduled calls section.

  * **`recordingOption`** : `RecordingOption?` — the call recording consent model. See Record consent. Distinct from `RecordingPermission.NOT_ASKED`, which is used only with scheduled calls.

  * **`voicemailReason`** : `String?` — populated when the channel is configured to route to voicemail.

  * **`phoneNumber`** : `String?` — PSTN fallback number configured for deflection or voicemail.

  * **`scheduleDeflectionType`** : `String?` / **`deflected`** : `Boolean?` / **`deflectedReason`** : `String?` — channel-level deflection metadata. When `deflected == true`, show the admin-configured `deflectedReason` message and offer the configured fallback (for example, a phone number to dial or a scheduled-call entry point) instead of attempting an instant call. See the Wait-time deflection section. in Headless Mobile SDK for Android: Smart Actions, Attachments, and Deflection for queue-level deflection handling.



    
    
    fun voiceEntryPoints(menu: QueueMenu) {
        val voice = menu.channels.voiceCall
        if (voice == null) {
            callNowButton.isVisible = false
            voicemailButton.isVisible = false
            return
        }
    
        // Instant call - only when explicitly enabled and not deflected
        callNowButton.isVisible = voice.instantEnabled && voice.deflected != true
    
        // Voicemail fallback
        val number = voice.phoneNumber
        if (voice.voicemailReason != null && number != null) {
            voicemailButton.isVisible = true
            voicemailButton.text = "Leave a voicemail"
            voicemailButton.setOnClickListener {
                dialVoicemail(number, reason = voice.voicemailReason)
            }
        }
    
        // Channel-level deflection
        if (voice.deflected == true) {
            showChannelDeflection(reason = voice.deflectedReason)
        }
    }
    

### Record consent

**What the SDK provides** : A `recordingOption`: `RecordingOption?` field on `VoiceCallChannel` that describes the call recording consent model admins configured in the portal.

**What you build** : The consent prompt (when `ASK_USER`) and the branching logic that honors the admin's choice.
    
    
    enum class RecordingOption {
        ALWAYS,   // Calls are always recorded - surface a disclosure before connecting
        NEVER,    // Calls are never recorded - no disclosure needed
        ASK_USER  // Prompt the user for consent before the call connects
    }
    
    fun handleRecordingConsent(voice: VoiceCallChannel, onResult: (Boolean) -> Unit) {
        when (voice.recordingOption) {
            RecordingOption.ALWAYS -> {
                showRecordingDisclosure("This call will be recorded.")
                onResult(true)
            }
            RecordingOption.NEVER, null -> onResult(true)
            RecordingOption.ASK_USER -> presentConsentPrompt { granted ->
                onResult(granted)
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



    
    
    suspend fun initiateInstantCall(queueMenu: QueueMenu) {
        val voice = queueMenu.channels.voiceCall ?: return
    
        if (!voice.instantEnabled || voice.deflected == true) {
            return
        }
    
        val recordingPermission = resolveRecordingPermission(voice)
        requestMicrophonePermissionIfNeeded()
    
        try {
            CCAI.callService?.startInstantCall(
                menuId = queueMenu.id,
                recordingPermission = recordingPermission
            )
        } catch (e: Exception) {
            showCallStartError(e)
        }
    }
    

### Observe call state

**Warning:** `CCAI.callService` may briefly be null after app launch — `CCAI.initializeCall(...)` returns early if the core SDK hasn't finished registering its network and smart-action services. If you wrap the service in a long-lived controller and start collecting flows at app launch, don't capture `callService?.stateChanged ?: emptyFlow()` into a stored property — that snapshots an empty flow that never emits. Re-read `CCAI.callService` from each intent method, or route flows through your own relay so late-bound subscribers receive events after the service appears.

Collect call-service events before starting or accepting a call:
    
    
    val service = CCAI.callService ?: return
    
    lifecycleScope.launch {
        service.stateChanged.collect { state ->
            updateCallConnectionState(state)
        }
    }
    
    lifecycleScope.launch {
        service.callReceived.collect { call ->
            updateCallDetails(call)
        }
    }
    
    lifecycleScope.launch {
        service.incomingCallEvent.collect { event ->
            handleIncomingCallEvent(event)
        }
    }
    
    lifecycleScope.launch {
        service.waitTimeUpdated.collect { waitTime ->
            updateEstimatedWaitTime(waitTime)
        }
    }
    
    lifecycleScope.launch {
        service.participantUpdated.collect { participant ->
            updateParticipantInfo(participant)
        }
    }
    
    lifecycleScope.launch {
        service.interruptionDetected.collect { interruption ->
            // A PSTN interruption (for example, an incoming cellular call)
            // has paused the active CCAI call. Surface a "call interrupted"
            // banner and offer a Resume action after the interruption ends.
            showInterruptionBanner(interruption)
        }
    }
    
    lifecycleScope.launch {
        service.deflectionOffered.collect { deflection ->
            // The platform offered a wait-time deflection (for example, a
            // scheduled callback or PSTN fallback). Render the prompt and
            // honor the user's choice.
            presentWaitTimeDeflection(deflection)
        }
    }
    

### Provider state versus server status

`stateChanged` and `callReceived.status` are independent signals — read them as columns, not rows. The provider's `stateChanged` reports the local VoIP handshake; the server-side `callReceived.status` reports the call's lifecycle on the platform. Drive the "Connected" flip and the call-timer start from `callReceived.status` — not from `stateChanged` reaching the connected state.

Signal | What it reports | What to drive from it  
---|---|---  
`stateChanged` (provider) | Local VoIP handshake — `Connecting, Connected (local), Disconnected, Error(...).` | Optional pre-status spinner before the server status arrives, error surfaces, and end-of-call cleanup.  
`callReceived.status` (server) | Server-side lifecycle — `WAITING`, `CONNECTING`, `CONNECTED`, `ON_HOLD`, `INTERRUPTED`, `ENDED`. | Connected flip, call-timer start, agent-assigned UI, transfer or escalation overlays, and the end-call flow.  
  
### Incoming calls

Incoming voice calls are delivered to the device using FCM. Because incoming calls can arrive while your app is backgrounded or fully terminated, your integration needs to be ready to receive them from any process state.

**Warning:** Initialize the SDK (`CCAI.initialize`, `CCAI.initializeChat`, `CCAI.initializeCall`) inside `Application.onCreate()`. FCM delivery for incoming calls fires the application class before any `Activity` is created, so any initialization that lives only in an `Activity` will miss cold-start incoming calls.

**What the SDK provides** : An `IncomingCallEvent` Flow on `callService` that emits the lifecycle of an incoming call: `Arrived`, `Accepted`, `Rejected`. The call service also exposes `acceptIncomingCall()` and `rejectIncomingCall()` to act on the offer.

**What you build** : Your incoming-call UI (full-screen ringing screen, lock-screen presentation, or in-app banner) and the handlers that accept or reject the offer.

#### Implementation example

Collect `incomingCallEvent` and render or dismiss your UI on each lifecycle event, then accept or reject from a long-lived scope. Define `applicationScope` once in your `Application` class so accept or reject coroutines survive any short-lived `Activity` teardown during the handshake.
    
    
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.Dispatchers
    import kotlinx.coroutines.SupervisorJob
    import kotlinx.coroutines.flow.first
    import kotlinx.coroutines.withTimeoutOrNull
    
    // Define this in your Application class (or another long-lived singleton).
    // Expose it however your app prefers as top-level property, dependency
    // injection, or a static field on the Application subclass.
    val applicationScope = CoroutineScope(SupervisorJob() + Dispatchers.Main)
    
    lifecycleScope.launch {
        CCAI.callService?.incomingCallEvent?.collect { event ->
            when (event) {
                is IncomingCallEvent.Arrived -> showIncomingCallUi(event.call)
                is IncomingCallEvent.Accepted -> navigateToCallScreen(event.call)
                is IncomingCallEvent.Rejected -> dismissIncomingCallUi()
            }
        }
    }
    
    // User taps "Accept" in your custom UI.
    fun onAcceptTapped() {
        // Important: accept/reject helpers suspend internally. Launch them on
        // `applicationScope` (defined above) so the call survives if the
        // ringing Activity is dismissed during the handshake.
        applicationScope.launch {
            CCAI.callService?.acceptIncomingCall()
        }
    }
    
    fun onRejectTapped() {
        applicationScope.launch {
            CCAI.callService?.rejectIncomingCall()
        }
    }
    

#### _Bridging FCM to your incoming-call UI_

FCM-delivered incoming calls arrive on a background thread, often before any `Activity` exists. Use a short timeout to bridge the FCM payload to the first `IncomingCallEvent.Arrived` emission, then start your UI.

#### Implementation example

Suspend on the next `IncomingCallEvent.Arrived` with `withTimeoutOrNull`, then hand off to your navigator.
    
    
    suspend fun handleIncomingCallPush() {
        val arrived = withTimeoutOrNull(60_000L) {
            CCAI.callService?.incomingCallEvent
                ?.filterIsInstance<IncomingCallEvent.Arrived>()
                ?.first()
        } ?: return
        // `myNavigator` is the `IncomingCallUiNavigator` implementation you wire
        // up during app initialization (see "Alternative: full-screen ringing
        // Activity" below). Hold the reference somewhere long-lived (for
        // example, on your `Application` subclass) so it can be reused here.
        myNavigator.showRingingUi(applicationContext, arrived.call.id)
    }
    

#### Telecom framework integration (recommended)

For a built-in Android incoming-call experience — full-screen ringer, lock-screen presentation, and integration with the system call log — register a `PhoneAccount` and let the Telecom framework own the ringing UX.

**What the SDK provides** : A `TelecomCallService` helper that registers a `PhoneAccount` for your app (`registerPhoneAccount(context)`), a `TelecomConnectionService` to bridge incoming CCAI calls into Android Telecom, and a `TelecomConnectionCallback` interface for connection state callbacks.

**What you build** : The one-time `PhoneAccount` registration during app initialization and a manifest declaration for the connection service.

#### Implementation example

Register the phone account at app startup, then declare the connection service and permission in your manifest.
    
    
    // In Application.onCreate(), after CCAI.initializeCall(...)
    TelecomCallService.registerPhoneAccount(context = this)
    
    
    
    <!-- AndroidManifest.xml -->
    <uses-permission android:name="android.permission.MANAGE_OWN_CALLS" />
    
    <service
        android:name="com.ccaiplatform.android.call.TelecomConnectionService"
        android:permission="android.permission.BIND_TELECOM_CONNECTION_SERVICE"
        android:exported="true">
        <intent-filter>
            <action android:name="android.telecom.ConnectionService" />
        </intent-filter>
    </service>
    

**Note:** Telecom requires API level 26 (Android 8.0) or higher for `PhoneAccount` registration. 

#### Alternative: full-screen ringing activity

If you prefer to render your own ringing screen instead of using the Telecom framework, the SDK exposes `IncomingCallService` along with the `IncomingCallUiNavigator` interface. Implement the interface, then hand your implementation to `IncomingCallService` during app initialization.

#### Implementation example

Implement `IncomingCallUiNavigator` and pass it into `IncomingCallService` once during `Application.onCreate()`.
    
    
    // 1. Implement the navigator. Override the three interface methods to
    //    declare the ringing Activity intent and to show/hide your UI as the
    //    call lifecycle changes.
    class MyNavigator : IncomingCallUiNavigator {
        override fun ringingActivityIntent(
            context: Context,
            callId: Long,
            callerName: String?
        ): Intent = Intent(context, RingingActivity::class.java).apply {
            putExtra("callId", callId)
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        }
    
        override fun showRingingUi(context: Context, callId: Long) {
            // Optional: surface an in-app banner or push your ringing UI.
        }
    
        override fun hideRingingUi(context: Context, callId: Long) {
            // Optional: dismiss whatever you surfaced in showRingingUi.
        }
    }
    
    // 2. Wire it up during app initialization (typically in Application.onCreate()).
    val incomingCallService = IncomingCallService(
        applicationContext,
        MyNavigator()
    )
    

**Warning:** To show your ringing `Activity` over the keyguard, set `setShowWhenLocked(true)` and `setTurnScreenOn(true)` on the `Activity`. On API 34 (Android 14) and newer, full-screen-intent presentation requires the user to grant the `USE_FULL_SCREEN_INTENT` permission. Check and request it before relying on this UX:
    
    
    if (!CCAI.canShowIncomingCallFullScreen(context)) {
        CCAI.openFullScreenIntentSettings(context)
    }
    

#### Foreground service for active ringing

While a call is ringing, Android may kill background processes. The SDK ships an `IncomingRingingService` that keeps the ringing flow alive as a foreground service. Declare it in your manifest and the SDK starts and stops it automatically as incoming calls arrive.
    
    
    <service
        android:name="com.ccaiplatform.android.call.IncomingRingingService"
        android:foregroundServiceType="phoneCall"
        android:exported="false" />
    
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_PHONE_CALL" />
    

### Call status and server-side states

**What the SDK provides** : A server-driven `CallStatus` enum on each `Call` payload that describes where the call is in its lifecycle (for example, `CONNECTING`, `WAITING`, `CONNECTED`, `ON_HOLD`, `INTERRUPTED`, `ENDED`, `FAILED`).

**What you build** : The mapping from `CallStatus` to the customer-facing states in your call screen.

#### Implementation example

`when`-branch on `call.status` from each `callReceived` emission and render the matching UI state:
    
    
    fun updateCallDetails(call: Call) {
        when (call.status) {
            CallStatus.CONNECTING -> renderConnectingState()
            CallStatus.WAITING -> renderWaitingInQueueState(call.estimatedWait)
            CallStatus.CONNECTED -> renderConnectedState(call.agent)
            CallStatus.ON_HOLD -> renderOnHoldState()
            CallStatus.INTERRUPTED -> renderInterruptedState()
            CallStatus.ENDED, CallStatus.FAILED -> renderEndedState(call.endReason)
        }
    }
    

### In-call controls (mute, speaker, hold)

**What the SDK provides** : Read-only properties on `callService` — `isMuted`, `isSpeakerEnabled`, `isOnHold` — alongside the actions to toggle each state (`setMuted`, `setSpeakerEnabled`, `setOnHold`).

**What you build** : The mute, speaker, and hold buttons in your in-call UI, wired to the SDK's actions and reflecting the current state.

#### Implementation example

Read the current state from `callService` to initialize your buttons, then toggle and update on tap.
    
    
    muteButton.isSelected = CCAI.callService?.isMuted == true
    speakerButton.isSelected = CCAI.callService?.isSpeakerEnabled == true
    holdButton.isSelected = CCAI.callService?.isOnHold == true
    
    fun onMuteTapped() {
        val next = CCAI.callService?.isMuted != true
        CCAI.callService?.setMuted(next)
        muteButton.isSelected = next
    }
    
    fun onSpeakerTapped() {
        val next = CCAI.callService?.isSpeakerEnabled != true
        CCAI.callService?.setSpeakerEnabled(next)
        speakerButton.isSelected = next
    }
    
    fun onHoldTapped() {
        val next = CCAI.callService?.isOnHold != true
        CCAI.callService?.setOnHold(next)
        holdButton.isSelected = next
    }
    

### Resume an in-progress call after interruption

When a PSTN interruption (such as an incoming cellular call) pauses the active CCAI call, the SDK keeps the session alive and emits `interruptionDetected`. After the interruption ends, your app can resume the call.

**What the SDK provides** : `getLastCallInProgress()` to look up an in-progress call (including across app restarts) and `resumeCall(call)` to bring it back to the foreground.

**What you build** : The resume affordance in your UI (typically a banner or an automatic resume after the interruption ends) and the navigation back to your call screen.

#### Implementation example

Look up the in-progress call with `getLastCallInProgress`, resume it, and navigate back to your call screen.
    
    
    lifecycleScope.launch {
        val call = CCAI.callService?.getLastCallInProgress() ?: return@launch
        try {
            CCAI.callService?.resumeCall(call)
            navigateToCallScreen(call)
        } catch (e: Exception) {
            showCallResumeError(e)
        }
    }
    

### Escalation from a virtual agent

**What the SDK provides** : `canEscalate(allowSkipVirtualAgent: Boolean)` is a method on `CallResponse` (the model emitted by `callService.callReceived`), not on `callService` itself. It reports whether the current call is eligible for escalation to a human agent based on the call's current virtual-agent status.

**What you build** : Hold onto the most recent `callReceived` emission as your "current call", then bind the visibility of your "Talk to a person" button to `currentCall?.canEscalate(...)`. The `allowSkipVirtualAgent` argument is a menu-configuration value that you fetch separately from the call response itself — don't hard-code `true` in production.

#### Implementation example

Keep the latest `Call` in a property, then invoke `canEscalate` on it. Resolve `allowSkipVirtualAgent` from your menu configuration.
    
    
    // Held from the most recent `callReceived` emission
    private var currentCall: Call? = null
    
    // `allowSkipVirtualAgent` is fetched separately from menu configuration
    // it is not derived from the CallResponse.
    val allowSkip = menuConfiguration.allowSkipVirtualAgent
    val allowed = currentCall?.canEscalate(allowSkipVirtualAgent = allowSkip) == true
    talkToAgentButton.isVisible = allowed
    

## Voicemail

**What the SDK provides** : `startVoicemail(VoicemailRequest)` on `callService`, plus a `VoicemailReason` enum that describes why the platform offered voicemail (for example, after-hours fallback, over-capacity fallback, or temporary redirection).

**What you build** : The voicemail entry point in your UI (typically shown when `VoiceCallChannel.voicemailReason` is populated, or when the call lifecycle resolves to a voicemail outcome) and the recording UI itself.

#### Implementation example

Surface the voicemail button when `voicemailReason` is set, then call `startVoicemail` with a `VoicemailRequest`.
    
    
    enum class VoicemailReason {
        AFTER_HOUR_DEFLECTION,
        OVER_CAPACITY_DEFLECTION,
        TEMPORARY_REDIRECTION
    }
    
    suspend fun offerVoicemail(menu: QueueMenu) {
        val voice = menu.channels.voiceCall ?: return
        if (voice.voicemailReason == null) return
        try {
            CCAI.callService?.startVoicemail(
                VoicemailRequest(menuId = menu.id)
            )
        } catch (e: Exception) {
            showVoicemailError(e)
        }
    }
    

## Wait-time deflection

When the queue is open but the wait time exceeds the admin-configured threshold, the platform can offer an alternative path — typically a scheduled callback or a PSTN deflection.

**What the SDK provides** : A `CallDeflection` payload describing the offered alternative, retrievable using `getCallDeflection(callId)` on `callService`. The platform also emits the same payload through the `deflectionOffered` Flow when a deflection becomes available mid-wait. A separate `CompanyResponse.preventDirectPstnCall` flag indicates whether direct PSTN dialing should be hidden in your fallback UI.

**What you build** : The deflection prompt (for example, "Estimated wait is 12 minutes — schedule a callback instead?") and the branching logic that honors the user's choice.

#### Implementation example

Fetch the offered deflection with the active call's ID, combine it with `CompanyResponse.preventDirectPstnCall`, and present the prompt.
    
    
    lifecycleScope.launch {
        val currentCall = CCAI.callService?.getLastCallInProgress()
            ?: return@launch
        val deflection = CCAI.callService?.getCallDeflection(callId = currentCall.id)
            ?: return@launch
        val company = CCAI.companyService?.get()
        val allowDirectPstn = company?.preventDirectPstnCall != true
        presentWaitTimeDeflection(deflection, allowDirectPstn)
    }
    

## Advanced `CallOptions`

`CallOptions` exposes a small set of toggles for apps that need to tune the default call experience.

  * **`connectingPollIntervalMs`** : `Long` — how often the SDK polls the platform while the call is in the connecting state.

  * **`connectedPollIntervalMs`** : `Long` — how often the SDK polls the platform while the call is connected.

  * **`endCallMaxRetries`** : `Int` — how many times the SDK retries the end-call request before surfacing an error.

  * **`endCallRetryDelayMs`** : `Long` — delay between end-call retries.




#### Implementation example

Pass the tuned values into `CallOptions` when initializing the call module:
    
    
    CCAI.initializeCall(
        context = this,
        options = CallOptions(
            connectingPollIntervalMs = 2_000L,
            connectedPollIntervalMs = 5_000L,
            endCallMaxRetries = 3,
            endCallRetryDelayMs = 1_000L
        )
    )
    

## Screen share

Screen sharing allows support agents to view the user's screen to help troubleshoot issues. CCAI Platform supports two modes of screen sharing:

  1. **In-app sharing** : the agent can only see what is happening inside your specific app.

  2. **Full-device sharing (optional)** : the agent can see the user's entire device, including the Android home screen and other apps. This requires advanced Android configuration using `MediaProjection` and a foreground service.




**What the SDK provides** : The `CCAIScreenShare` module that creates and manages sessions, handles state changes, and processes consent requests.

**What you build** : The initialization configuration, the UI prompts for user consent, and (if supporting full-device) the built-in Android `MediaProjection` integration with a foreground service.

The screen share service provides methods for the full session lifecycle — `startSession`, `activateSession`, `stopSession` — plus configuration methods for remote control and full-device sharing. The next subsections walk through the core integration flow.

For complete method signatures and parameter details for all screen share methods, see the **Headless Mobile SDK - Android API Reference**.

### Initialize and configure screen share

Initialize the screen share service during app setup by providing your screen share key:
    
    
    import com.ccaiplatform.android.CCAI
    import com.ccaiplatform.android.ScreenShareOptions
    
    // Minimal - domain defaults to your instance's configured provider
    CCAI.initializeScreenShare(
        context = this,
        screenShareOptions = ScreenShareOptions(
            key = "YOUR_SCREEN_SHARE_KEY"
        )
    )
    
    // If your instance or provider requires an explicit domain:
    // CCAI.initializeScreenShare(
    //     context = this,
    //     screenShareOptions = ScreenShareOptions(
    //         key = "YOUR_SCREEN_SHARE_KEY",
    //         domain = "your_subdomain.ccaiplatform.com"
    //     )
    // )
    

### Check screen share eligibility

Before enabling screen share functionality, check if it's available for the current chat:
    
    
    import com.ccaiplatform.ccaiscreenshare.ScreenShareManager
    
    fun isScreenShareEnabled(chat: ChatResponse): Boolean {
        return CCAI.screenShareService != null
            && chat.supportScreenShare == true
    }
    

### Handle screen share requests

Implement screen share request handling using `ScreenShareManager`. You create a session and handle the async response using `ScreenShareCallbacks`:
    
    
    import com.ccaiplatform.ccaiscreenshare.ScreenShareManager
    import com.ccaiplatform.ccaiscreenshare.ScreenShareCallbacks
    
    fun requestScreenShare(chatId: String, isFromRemote: Boolean) {
        val screenShareService = CCAI.screenShareService
        if (screenShareService == null) {
            Log.e("ScreenShare", "Screen share service not available")
            return
        }
    
        // Track whether this session is agent-initiated
        screenShareInitiatedFrom = if (isFromRemote) "agent" else "endUser"
    
        if (!isFromRemote) {
            sendScreenShareMessage(event = "screenShareRequestedFromEndUser")
        }
    
        val callbacks = ScreenShareCallbacks(
            onSessionStateChanged = { state ->
                Log.d("ScreenShare", "State changed: $state")
                handleScreenShareStateChange(state)
            },
            onSessionCreationError = { error ->
                Log.e("ScreenShare", "Session creation failed: ${error.message}")
                sendScreenShareMessage(event = "screenShareFailed")
                showErrorToast("Screen share failed to start.")
            },
            onSessionActivationRequest = {
                Log.d("ScreenShare", "Activation request received")
                // For agent-initiated sessions, activate immediately
                // For user-initiated sessions, show a confirmation dialog first
                if (screenShareInitiatedFrom == "agent") {
                    ScreenShareManager.activateSession()
                } else {
                    showScreenShareConsentDialog {
                        ScreenShareManager.activateSession()
                    }
                }
            }
        )
    
        ScreenShareManager.startSession(
            request = ScreenShareRequest(
                communicationId = chatId,
                communicationType = CommunicationType.Chat,
                initiatedFrom = if (isFromRemote) ScreenShareFrom.AGENT else ScreenShareFrom.END_USER
            ),
            callbacks = callbacks
        )
    }
    

### Handle screen share state changes

Listen to screen share session state changes through the `onSessionStateChanged` callback provided to `ScreenShareCallbacks`:
    
    
    fun handleScreenShareStateChange(state: ScreenShareSessionState) {
        currentScreenShareSessionState = state
    
        when (state) {
            ScreenShareSessionState.INACTIVE -> {
                Log.d("ScreenShare", "No active session")
            }
            ScreenShareSessionState.PENDING -> {
                Log.d("ScreenShare", "Session pending - waiting for activation")
                // For agent-initiated sessions, activate immediately
                if (screenShareInitiatedFrom == "agent") {
                    ScreenShareManager.activateSession()
                }
            }
            ScreenShareSessionState.ACTIVE -> {
                Log.d("ScreenShare", "Screen share active")
                sendScreenShareMessage(event = "screenShareStarted")
                updateUiForActiveScreenShare()
            }
        }
    }
    

#### `ScreenShareCallbacks` reference

Callback | Description  
---|---  
`onSessionStateChanged` | Called when the screen share session state changes (`INACTIVE`, `PENDING`, `ACTIVE`).  
`onSessionCreationError` | Called when session creation fails (network issue, service unavailable, etc.).  
`onSessionActivationRequest` | Called when the session is ready to activate — call `ScreenShareManager.activateSession()` to begin sharing. For user-initiated sessions, show a consent prompt first; for agent-initiated sessions, activate immediately.  
`onSessionRemoteControlRequest` | Called when the agent requests remote control of the user's screen. Show a consent prompt before granting remote control.  
`onSessionFullDeviceRequest` | Called when the agent requests full-device sharing (see Full-device screen sharing below). Trigger your `MediaProjection` consent flow in response.  
`onSessionDidSucceed` | Called after a session successfully activates and begins streaming. Use this to update your UI to the "screen share active" state.  
  
For the full state enum definitions and all associated types, see the **Headless Mobile SDK - Android API Reference**.

### Full-device screen sharing (advanced)

Full-device screen sharing enables agents to view screens from applications outside of your own, including system settings and inter-application navigation. This requires integrating Android's `MediaProjection` API and running a foreground service.

**Warning:** Full-device screen sharing requires additional setup and is only available on physical devices. On Android 14 (API level 34) and newer, your foreground service must declare the `mediaProjection` type.

#### Declare permissions and foreground service

Add the required permissions and foreground service declaration to your `AndroidManifest.xml`:
    
    
    <manifest>
        <!-- Required for screen capture -->
        <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
        <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" />
    
        <application>
            <service
                android:name=".screenshare.ScreenShareForegroundService"
                android:foregroundServiceType="mediaProjection"
                android:exported="false" />
        </application>
    </manifest>
    

#### Request MediaProjection consent

Before capturing the screen, you must prompt the user for consent using `MediaProjectionManager`:
    
    
    import android.media.projection.MediaProjectionManager
    import android.content.Context
    
    private val mediaProjectionManager by lazy {
        getSystemService(Context.MEDIA_PROJECTION_SERVICE) as MediaProjectionManager
    }
    
    fun requestScreenCapturePermission() {
        val captureIntent = mediaProjectionManager.createScreenCaptureIntent()
        screenCaptureResultLauncher.launch(captureIntent)
    }
    
    // Handle the result in your Activity
    private val screenCaptureResultLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == Activity.RESULT_OK && result.data != null) {
            // User granted screen capture permission
            startScreenShareForegroundService(result.resultCode, result.data!!)
        } else {
            Log.d("ScreenShare", "User denied screen capture permission")
        }
    }
    

#### Implement the foreground service

Create a foreground service that holds the `MediaProjection` session:
    
    
    import android.app.Service
    import android.app.Notification
    import android.app.NotificationChannel
    import android.app.NotificationManager
    import android.content.Intent
    import android.os.IBinder
    
    class ScreenShareForegroundService : Service() {
    
        override fun onCreate() {
            super.onCreate()
            createNotificationChannel()
        }
    
        override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
            val notification = buildNotification()
            startForeground(NOTIFICATION_ID, notification)
            return START_NOT_STICKY
        }
    
        override fun onBind(intent: Intent?): IBinder? = null
    
        private fun createNotificationChannel() {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "Screen Share",
                NotificationManager.IMPORTANCE_LOW
            ).apply {
                description = "Active screen share session"
            }
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(channel)
        }
    
        private fun buildNotification(): Notification {
            return Notification.Builder(this, CHANNEL_ID)
                .setContentTitle("Screen Sharing")
                .setContentText("An agent is viewing your screen.")
                .setSmallIcon(R.drawable.ic_screen_share)
                .build()
        }
    
        companion object {
            private const val CHANNEL_ID = "screen_share_channel"
            private const val NOTIFICATION_ID = 1001
        }
    }
    

#### Enable full-device sharing

After `MediaProjection` is active, enable full-device sharing through the screen share service:
    
    
    // After MediaProjection consent is granted and foreground service is started
    ScreenShareManager.enableFullDeviceSharing(true)
    

### Jetpack Compose considerations for screen share

**Warning:** Remote control in the Cobrowse-based screen share integration may not fully support Jetpack Compose-based UI components, which can cause certain interactive elements to be non-clickable under remote control. legacy Android view-based components work as expected.

#### Recommended approaches for remote interaction in Jetpack Compose

  1. **Wrap key interactive elements with Android views** — for areas that need to be remotely clickable, wrap them as standard Android view controls (for example, `android.widget.Button`) using the `AndroidView` composable. This ensures remote clicks work reliably through the Android view-based path.

  2. **Forward remote touches with custom touch handling** — for Compose areas that can't be replaced with Views, use custom touch callbacks to forward remote touch events to your Compose logic.

  3. **Provide product-level guidance or fallback** — clearly indicate on Compose screens that "Agents can only view; user must tap locally," or automatically restrict remote-control permissions on these pages while maintaining view-only access.




#### Example Android view wrapper implementation
    
    
    import androidx.compose.runtime.Composable
    import androidx.compose.ui.viewinterop.AndroidView
    import android.widget.Button
    
    @Composable
    fun RemoteControlButton(
        title: String,
        onClick: () -> Unit
    ) {
        AndroidView(
            factory = { context ->
                Button(context).apply {
                    text = title
                    setOnClickListener { onClick() }
                }
            },
            update = { button ->
                button.text = title
            }
        )
    }
    
    // Usage in a Composable
    @Composable
    fun ScreenShareSupportScreen() {
        Column {
            Text("This screen supports remote control")
            RemoteControlButton(title = "Clickable Button") {
                println("Button tapped remotely or locally")
            }
        }
    }
    

## Scheduled calls

Scheduled calls let users book a future voice call instead of waiting in queue for an instant call. On Android, the SDK exposes call-service methods for checking availability, fetching time slots, booking calls, rescheduling calls, canceling calls, and handling scheduling errors.

### Capability detection

**What the SDK provides** : A `scheduleEnabled` flag on `VoiceCallChannel` that tells you whether the selected queue supports booking future calls.

**What you build** : The logic to check this flag before showing your scheduling entry point.

#### Implementation example

Check `scheduleEnabled` on the queue voice call channel. Don't use voiceCall != null as a proxy — a queue can support instant voice calls without supporting scheduled calls, and the other way around.
    
    
    fun setupScheduledCallEntryPoint(queueMenu: QueueMenu) {
        val voiceChannel = queueMenu.channels.voiceCall
    
        if (voiceChannel == null) {
            callNowButton.isVisible = false
            scheduleCallButton.isVisible = false
            return
        }
    
        callNowButton.isVisible = voiceChannel.instantEnabled && voiceChannel.deflected != true
        scheduleCallButton.isVisible = voiceChannel.scheduleEnabled == true
    }
    

**Warning:** `scheduleEnabled` and instant call availability are independent booleans. A voice-enabled queue can have one and not the other. Always check `scheduleEnabled` explicitly for scheduling support.

### Optional availability check

Before showing your time-slot picker, you can check whether the selected queue has available scheduling slots.

#### Implementation example

Use `hasScheduledTimeSlots(menuId:)` as a lightweight pre-check. If it returns `false`, show an empty-state or fallback option instead of opening the picker.
    
    
    lifecycleScope.launch {
        try {
            val available = CCAI.callService?.hasScheduledTimeSlots(menuId = menu.id) == true
            if (available) {
                showScheduleCallUI()
            } else {
                showNoSlotsMessage()
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Availability check failed: ${e.message}")
            showNoSlotsMessage()
        }
    }
    

### Fetch time slots

Retrieve available appointment times for the selected queue. The SDK returns Date values that your app can display in the user's local timezone.

**What the SDK provides** : Available slot timestamps for the selected queue, with optional support for rescheduling an existing scheduled call.

**What you build** : The calendar, time picker, timezone presentation, empty-state handling, and retry behavior.

#### Implementation example

Call `getScheduledTimeSlots` with the queue menu ID. When rescheduling, pass the existing scheduled-call ID so the service can return the appropriate availability.
    
    
    lifecycleScope.launch {
        try {
            val slots: List<Date> = CCAI.callService?.getScheduledTimeSlots(
                menuId = menu.id,
                callIdForRescheduling = null
            ) ?: emptyList()
    
            if (slots.isEmpty()) {
                showNoSlotsMessage()
            } else {
                displayTimeSlotPicker(slots)
            }
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to fetch time slots: ${e.message}")
        }
    }
    

When rescheduling, pass the existing scheduled-call ID:
    
    
    val slots = CCAI.callService?.getScheduledTimeSlots(
        menuId = menu.id,
        callIdForRescheduling = existingCallId
    ) ?: emptyList()
    

### Create a scheduled call

After the user selects a time slot, create the scheduled call through `callService`.

**What the SDK provides** : A `createScheduledCall` API that books the selected slot and returns the scheduled-call record.

**What you build** : E.164 phone-number validation, confirmation UI, local persistence of the scheduled-call ID, and recovery for slot conflicts or after-hours responses.

#### Implementation example

Pass the selected slot, phone number, queue ID, and `RecordingPermission.NOT_ASKED` in a `ScheduledCallRequest`.
    
    
    lifecycleScope.launch {
        try {
            val response = CCAI.callService?.createScheduledCall(
                ScheduledCallRequest(
                    menuId = menu.id,
                    phoneNumber = userPhoneNumber,
                    scheduleTime = selectedSlot,
                    recordingPermission = RecordingPermission.NOT_ASKED,
                    callIdForRescheduling = null,
                    customData = null,
                    ticketId = null
                )
            )
    
            saveScheduledCallId(response?.id)
            showConfirmation(scheduledAt = response?.scheduledAt)
        } catch (e: CallCreationError.AfterHours) {
            showMessage(e.displayMessage)
            refreshTimeSlots()
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to schedule call: ${e.message}")
        }
    }
    

The phone number must be in **E.164** format, such as `+14155551234`.

### Reschedule an existing call

To reschedule, fetch slots and create the new scheduled call with the existing scheduled-call ID.

**What the SDK provides** : The same time-slot and creation APIs, with `callIdForRescheduling` used to identify the existing booking.

**What you build** : The "change time" UI, local lookup of the stored scheduled-call ID, and updated confirmation state after the new booking is created.

#### Implementation example

Pass the existing call ID to both `getScheduledTimeSlots` and `createScheduledCall`.
    
    
    lifecycleScope.launch {
        try {
            val slots = CCAI.callService?.getScheduledTimeSlots(
                menuId = menu.id,
                callIdForRescheduling = existingCallId
            ) ?: emptyList()
    
            val response = CCAI.callService?.createScheduledCall(
                ScheduledCallRequest(
                    menuId = menu.id,
                    phoneNumber = userPhoneNumber,
                    scheduleTime = newSelectedSlot,
                    recordingPermission = RecordingPermission.NOT_ASKED,
                    callIdForRescheduling = existingCallId,
                    customData = null,
                    ticketId = null
                )
            )
    
            saveScheduledCallId(response?.id)
            showConfirmation(scheduledAt = response?.scheduledAt)
        } catch (e: CallCreationError.AfterHours) {
            showMessage(e.displayMessage)
            refreshTimeSlots()
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to reschedule: ${e.message}")
        }
    }
    

### Cancel a scheduled call

When the user cancels an upcoming call, call `cancelScheduledCall` and clear the locally stored call ID.

**What the SDK provides** : A cancellation API for a scheduled-call ID.

**What you build** : The confirmation prompt, cancellation success or error UI, and cleanup of any locally stored upcoming-call state.

#### Implementation example

Call `cancelScheduledCall(callId:)` with the stored ID, then remove the ID from your app's storage.
    
    
    lifecycleScope.launch {
        try {
            CCAI.callService?.cancelScheduledCall(callId = existingCallId)
            clearScheduledCallId()
            showCancellationConfirmation()
        } catch (e: Exception) {
            Log.e("CCAI", "Failed to cancel call: ${e.message}")
        }
    }
    

## Email

**Important BYO composer dependency** : Email composition and submission are entirely handed off to your built-in app. Because the CCAI Platform SDK doesn't natively send the email payload, it can't automatically track whether an email was successfully sent. You must use Android `ActivityResultContract` or `startActivityForResult` patterns to track the submission and log it to your own analytics platform. 

**What the SDK provides** : The destination email address configured for that specific queue, alongside any instructions the administrator wants the user to see (for example, _include your account number)._

**What you build** : The email composer screen and the logic to track its completion. You can build your own custom form, or use Android's built-in `Intent.ACTION_SENDTO` to launch the user's preferred email client.

#### Implementation example

This code pulls the support email address from the SDK's `Channels` object on the `QueueMenu`. It opens the built-in Android email client and handles the case where no email client is installed.
    
    
    import android.content.Intent
    import android.net.Uri
    import android.widget.Toast
    
    class SupportActivity : AppCompatActivity() {
    
        // 1. Trigger the email flow
        fun openEmailComposer(queueMenu: QueueMenu) {
            val emailChannel = queueMenu.channels.email ?: return
            val emailAddress = emailChannel.email ?: return
    
            val emailIntent = Intent(Intent.ACTION_SENDTO).apply {
                data = Uri.parse("mailto:")
                putExtra(Intent.EXTRA_EMAIL, arrayOf(emailAddress))
                putExtra(Intent.EXTRA_SUBJECT, "Support Request: ${queueMenu.name ?: ""}")
                // If the queue provides an instruction message, include it in the body
                // putExtra(Intent.EXTRA_TEXT, emailChannel.instructionMessage ?: "")
            }
    
            if (emailIntent.resolveActivity(packageManager) != null) {
                emailResultLauncher.launch(emailIntent)
            } else {
                Toast.makeText(
                    this,
                    "No email client installed on this device.",
                    Toast.LENGTH_LONG
                ).show()
            }
        }
    
        // 2. Track the outcome using ActivityResultContract
        private val emailResultLauncher = registerForActivityResult(
            ActivityResultContracts.StartActivityForResult()
        ) { result ->
            // Note: Most Android email clients don't return a meaningful
            // result code. Unlike iOS's MFMailComposeViewControllerDelegate,
            // Android's email intent doesn't reliably report whether the
            // email was sent, saved as draft, or cancelled.
            // Log this event to your analytics and assume the user
            // interacted with the email composer.
            Log.d("CCAI", "Email composer closed. Result code: ${result.resultCode}")
            MyAnalytics.logEvent("email_composer_closed")
        }
    }
    

**Note:** Unlike iOS's `MFMailComposeViewControllerDelegate`, which reports exact outcomes (sent, cancelled, saved, failed), Android's `ACTION_SENDTO` intent doesn't provide reliable result codes from third-party email apps. Most email clients return `RESULT_CANCELED` regardless of whether the user sent the email or dismissed the composer. If precise send-tracking is critical, consider building a custom in-app email form that submits using your own backend API. 

## External deflection links

**What the SDK provides** : A list of URLs (such as your company's Help Center, refund policy, or a partner app) and their display titles, exactly as configured in the Admin Portal.

**What you build** : The logic to execute those links when a user taps them - either by opening them in an in-app browser (using Android's [custom tabs](https://developer.chrome.com/docs/android/custom-tabs/)) or launching the default system browser.

#### Implementation example (custom tabs — recommended)

When the user taps an external link from your menu, this code extracts the URL string provided by the SDK and uses Chrome Custom Tabs to display the webpage in an in-app browser experience. Custom tabs provide a faster, more seamless experience than launching the full browser app, while still showing the address bar so the user knows they are viewing external content.
    
    
    import androidx.browser.customtabs.CustomTabsIntent
    import android.net.Uri
    
    fun openHelpCenterLink(urlString: String) {
        val uri = Uri.parse(urlString) ?: return
    
        val customTabsIntent = CustomTabsIntent.Builder()
            .setShowTitle(true)
            .build()
    
        customTabsIntent.launchUrl(this, uri)
    }
    

**Warning:** Custom tabs require the AndroidX Browser library. Add `implementation("androidx.browser:browser:1.8.0")` to your `build.gradle.kts` dependencies. If you prefer not to add this dependency, use the fallback approach outlined next.

**Fallback implementation (system browser)** : If Custom Tabs are not available or you prefer a simpler approach, you can open the link in the user's default browser:
    
    
    import android.content.Intent
    import android.net.Uri
    
    fun openHelpCenterLink(urlString: String) {
        val uri = Uri.parse(urlString) ?: return
    
        val intent = Intent(Intent.ACTION_VIEW, uri)
        if (intent.resolveActivity(packageManager) != null) {
            startActivity(intent)
        } else {
            showErrorToast("No browser available to open this link.")
        }
    }
    

#### Full integration example

This code reads the deflection link from the SDK's `Channels` object and presents it to the user as a tappable button in your channel menu.
    
    
    fun setupDeflectionLinks(queueMenu: QueueMenu) {
        val deflectionLink = queueMenu.channels.externalDeflectionLink
    
        if (deflectionLink != null) {
            helpCenterButton.isVisible = true
            helpCenterButton.setOnClickListener {
                // Read the URL from the structured ExternalDeflectionLink type
                val url = deflectionLink.url ?: return@setOnClickListener
                openHelpCenterLink(url)
            }
        } else {
            helpCenterButton.isVisible = false
        }
    }
    

`ExternalDeflectionLink` exposes both top-level `url` / `displayName` fields and an inner `links: List<ExternalDeflection>?` array. The preceding example only renders the top-level entry, which is sufficient for single-link queues. If your admins configure multiple external links on a single queue, iterate `deflectionLink.links` and render one button per enabled entry - each `ExternalDeflection` carries its own `url` and `displayName`:
    
    
    deflectionLink.links
        ?.filter { it.enabled == true }
        ?.forEach { link ->
            val button = MaterialButton(this).apply {
                text = link.displayName
                setOnClickListener { openHelpCenterLink(link.url) }
            }
            helpCenterContainer.addView(button)
        }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
