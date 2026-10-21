---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started/
title: Headless Mobile SDK for Android: Get started \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:22:32.952705+00:00
---

# Headless Mobile SDK for Android: Get started  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless Mobile SDK for Android: Get started Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate and customize the SDK in your Android application.

## Get started

The Headless Mobile SDK for Android lets you integrate CCAI Platform's contact center capabilities into your own built-in Android UI.

Instead of presenting a CCAI Platform-branded widget, you:

  * Add the CCAI Android SDK modules as dependencies.

  * Build your own screens, flows, and visual design in Kotlin (recommended) or Java.

  * Use the SDK to:

    * Start and manage chat and voice sessions.

    * Offer email, voice call, and deflection options.

    * Support smart actions, attachments, and post-session flows (CSAT, surveys, virtual agent).




CCAI Platform handles the contact center logic (routing, queues, channels, configuration, reporting). You own the entire app experience (UI, flows, and branding).

If you'd prefer a prebuilt UI with configurable theming, use the standard mobile SDK.

## Requirements and supported environments

This section describes requirements and supported environments for Headless Mobile SDK for Android.

### Android platform requirements

The following platform requirements apply to Android:

  * **Minimum Android version** : Android 6.0 (API level 23) or later

  * **Compile SDK** : 36 (recommended)

  * **Supported languages** : Kotlin (recommended) or Java

  * **Java compatibility** : Java 17+

  * **Gradle / Android Studio** : a recent Android Gradle Plugin and Android Studio version compatible with your app and the SDK release you're using

  * **Kotlin version** : 1.6.0 or higher




### CCAI Platform instance requirements

You will need access to your CCAI Platform instance's **Developer settings** to obtain:

  * **Company key**

  * **Company secret code**

  * **Host URL** — the hostname for the CCAI platform (for example, your_subdomain.ccaiplatform.com)




These values are used for:

  * **Company key** and **Host URL** — in your Android app to initialize the SDK.

  * **Company secret code** — in your backend to sign JSON Web Tokens (JWT) used to authenticate users.




### Networking and permissions

Your app must allow outbound traffic to CCAI Platform endpoints and any voice provider endpoints you have configured.

Typical Android permissions include (the actual list may vary by SDK version and your feature set):

  * **Internet / network state** : for all SDK communications.

  * **Microphone** : for voice calls.

  * **Notifications** : for Firebase Cloud Messaging (FCM) push notifications.

  * **Storage / media** : for attachments.

  * **Camera** : for photo or video capture in smart actions.

  * **Screen capture** : for screen share (`MediaProjection`).




Declare and request runtime permissions according to Android OS guidelines.

### Push notifications

The Headless Android SDK uses FCM to deliver:

  * Incoming call notifications.

  * Certain smart-action and call-related messages.

  * Updates to help maintain state when the app is backgrounded.




You will need:

  * A Firebase project.

  * A valid google-services.json in your app module.

  * FCM token handling and registration in your app.

  * Custom notification and in-call UI in your app.




## How the headless Android SDK fits into your app

The Headless Mobile SDK for Android can be viewed as three layers:

### CCAI Platform platform and SDK (handled by CCAI Platform)

The SDK securely interacts with the CCAI Platform platform and provides:

  * Authentication using JSON Web Tokens (JWT).

  * Queue and channel routing metadata (chat, voice call, email, external deflection links).

  * Real-time session state management using service objects (`chatService`, `queueMenuService`, and more).

  * The secure transport pipeline for smart actions, file attachments, and screen share.

  * Deflection logic and post-session hierarchy evaluation.




### Your Android app (UI and logic - handled by you)

You control the entire visual and navigational experience:

  * **Entry points** : for example, a **Help** tab or **Contact us** button.

  * **Menus** : how you surface queues (for example, **Billing** , **Tech support**).

  * **In-session UI** : your custom chat bubbles, call screens, and controls.

  * **What your app does** : calls SDK service APIs to start and end sessions, observes SDK events using Kotlin Coroutines and Flow, and drives component navigation.




### CCAI Platform Admin Portal configuration

Your CCAI Platform admins configure the rules of engagement (operating hours, available channels, wait time thresholds, and surveys). The SDK reads this configuration and exposes it to your app as raw data and events. You decide how to draw that configuration on the screen.

## Retrieve company credentials

Before you integrate the SDK, obtain the credentials from your CCAI Platform instance:

  1. Sign in to the CCAI Platform Admin Portal with an administrator account.

  2. Navigate to **Settings > Developer settings**.

  3. Under **Company key & secret code**, copy:

     * **Company key**

     * **Company secret code**

  4. Note your **Host URL** — the hostname for the CCAI platform (for example, `your_subdomain.ccaiplatform.com`).




You will use:

  * **In your Android app** : **Company key** and **Host URL**.

  * **In your backend server** : **Company secret code** to sign JWTs for end-user authentication and optional custom data and context used by CCAI Platform.




## Add the SDK to your Android app

The Headless SDK uses a modular architecture. You install the core `CCAIKit` alongside the specific feature modules your app requires (for example, `CCAIChat` or `CCAIScreenShare`).

### Add the CCAI Maven repository

Add the CCAI Maven repository to your project's `settings.gradle.kts` (or root `build.gradle`):
    
    
    // settings.gradle.kts
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            maven { url = uri("https://sdk.ujet.co/ccaip/android/") }
        }
    }
    

### Configure the Gradle version catalog (recommended)

Google Cloud recommends using a Gradle version catalog for managing SDK dependencies. Add the following to your `gradle/libs.versions.toml`:
    
    
    [versions]
    ccaiVersion = "3.3.1"
    
    [libraries]
    ccai-kit       = { group = "com.ccaiplatform.android", name = "CCAIKit",        version.ref = "ccaiVersion" }
    ccai-chat      = { group = "com.ccaiplatform.android", name = "CCAIChat",       version.ref = "ccaiVersion" }
    ccai-chat-red  = { group = "com.ccaiplatform.android", name = "CCAIChatRed",    version.ref = "ccaiVersion" }
    ccai-call      = { group = "com.ccaiplatform.android", name = "CCAICall",       version.ref = "ccaiVersion" }
    ccai-call-red  = { group = "com.ccaiplatform.android", name = "CCAICallRed",    version.ref = "ccaiVersion" }
    ccai-screenshare = { group = "com.ccaiplatform.android", name = "CCAIScreenShare", version.ref = "ccaiVersion" }
    

### Add dependencies

In your app-level `build.gradle.kts`, add the core SDK and the specific feature modules:
    
    
    // app/build.gradle.kts
    android {
        compileSdk = 36
    
        compileOptions {
            sourceCompatibility = JavaVersion.VERSION_17
            targetCompatibility = JavaVersion.VERSION_17
        }
    
        kotlinOptions {
            jvmTarget = "17"
        }
    }
    
    dependencies {
        // 1. Core (always required)
        implementation(libs.ccai.kit)
    
        // 2. Chat (required for chat sessions)
        implementation(libs.ccai.chat)
        implementation(libs.ccai.chat.red)   // media layer paired with CCAIChat
    
        // 3. Voice (required for instant calls, voicemail, and scheduled calls)
        implementation(libs.ccai.call)
        implementation(libs.ccai.call.red)   // media/transport layer paired with CCAICall
    
        // 4. Screen Share (optional)
        // implementation(libs.ccai.screenshare)
    }
    

If you aren't using the version catalog, you can declare dependencies directly:
    
    
    val ccaiVersion = "3.3.1"
    
    dependencies {
        implementation("com.ccaiplatform.android:CCAIKit:$ccaiVersion")
        implementation("com.ccaiplatform.android:CCAIChat:$ccaiVersion")
        implementation("com.ccaiplatform.android:CCAIChatRed:$ccaiVersion")
        implementation("com.ccaiplatform.android:CCAICall:$ccaiVersion")        // Voice calls
        implementation("com.ccaiplatform.android:CCAICallRed:$ccaiVersion")     // Twilio VoIP backend
        implementation("com.ccaiplatform.android:CCAIScreenShare:$ccaiVersion") // Optional, for screen share
    }
    

## Initialization and setup

Initialize the SDK during app launch. Because of the SDK's modular architecture, initialize the core CCAI Platform system first, then register the specific channel providers (such as `chat` or `screen share`).

### Implement the `CCAIDelegate` interface

The SDK uses a `CCAIDelegate` interface for authentication callbacks. The key method is a Kotlin suspend function `ccaiShouldAuthenticate()` that the SDK calls when it needs a JWT.
    
    
    import com.ccaiplatform.ccaikit.CCAIDelegate
    
    class MyCCAIDelegate : CCAIDelegate {
    
        /**
         *   Called by the SDK when it needs a signed JWT for authentication.
         *   This is a suspend function - you can make network calls here.
         *
         *   @return The auth token returned by `authService.authenticate(jwt)`,
    
    *   or null on failure. This is what the SDK expects - not the raw JWT.
         */
        override suspend fun ccaiShouldAuthenticate(): String? {
            return try {
                // 1. Call your backend server to get a signed JWT
                val jwt = MyBackendApi.getSignedJwt() ?: return null
    
                // 2. Exchange the JWT for an auth token using authService - this is
                //    what the SDK expects to be returned (not the raw JWT).
                CCAI.authService?.authenticate(jwt)
            } catch (e: Exception) {
                null // Return null to signal authentication failure
            }
        }
    }
    

The preceding snippet shows the minimal two-step flow (**sign → authenticate → return**).

See Authenticate end users and pass custom data for the full authentication contract, including:

  * how to sign the JWT on your backend,
  * how `authenticate(jwt)` exchanges it for an auth token,
  * token caching and invalidation, and
  * worked examples with error handling.



### Initialize the SDK in your application class

Initialize the SDK in your custom application class using the `CCAI` singleton object:
    
    
    import android.app.Application
    import com.ccaiplatform.ccaikit.CCAI
    import com.ccaiplatform.ccaikit.InitOptions
    import com.ccaiplatform.ccaichat.initializeChat
    import com.ccaiplatform.ccaichat.model.ChatOptions
    import com.ccaiplatform.ccaicall.initializeCall
    import com.ccaiplatform.ccaikit.initializeScreenShare
    import com.ccaiplatform.ccaikit.models.screenShare.ScreenShareOptions
    
    class MainApplication : Application() {
    
        private val delegate = MyCCAIDelegate()
    
        override fun onCreate() {
            super.onCreate()
    
            // 1. Build InitOptions
            val initOptions = InitOptions(
                key = "YOUR_COMPANY_KEY",
                urlHost = "your_subdomain.ccaiplatform.com",
                languageCode = "en",       // Optional: ISO 639 code
                delegate = delegate        // Your delegate implementation
            )
    
            // 2. Initialize the core SDK
            CCAI.initialize(
                context = this,
                options = initOptions
            )
    
            // 3. Initialize chat (minimal)
            CCAI.initializeChat(context = this)
    
            // Initialize chat (with optional configuration)
            // val chatOptions = ChatOptions(
            //     webFormInterface = null,              // Implement to intercept and render custom web forms within your own UI
            //     downloadTranscriptVisibility = DownloadTranscriptVisibility.SHOW_ALL,
            //     greeting = "Hello! How can I help you?"
            // )
            // CCAI.initializeChat(
            //     context = this,
            //     options = chatOptions
            // )
    
            // 4. Initialize call (required whenever your app uses voice or scheduled calls)
            CCAI.initializeCall(context = this)
    
            // 5. Initialize screen share (optional)
            // CCAI.initializeScreenShare(
            //     context = this,
            //     options = ScreenShareOptions(
            //         key = "YOUR_COMPANY_KEY",
            //         domain = "your_subdomain.ccaiplatform.com"
            //     )
            // )
        }
    }
    

### `InitOptions` configuration reference
    
    
    data class InitOptions(
        /// The company key used for authentication
        var key: String,
    
        /// The host URL for CCAI platform (for example, "my-unique-instance.uc1.ccaiplatform.com")
        var urlHost: String,
    
        /// The preferred language code for localization (defaults to "en")
        var languageCode: String? = "en",
    
        /// Listener that handles authentication
        var delegate: CCAIDelegate? = null,
    
        /// Whether to cache the authentication token (defaults to true)
        var cacheAuthToken: Boolean = true
    )
    

### Update `AndroidManifest.xml`

Ensure your custom application class is registered:
    
    
    <application
        android:name=".MainApplication"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.YourApp">
    </application>
    

### Available SDK services

After initialization, you can access various services through the `CCAI` singleton object:
    
    
    val authService = CCAI.authService
    val companyService = CCAI.companyService
    val queueMenuService = CCAI.queueMenuService
    val optionsService = CCAI.optionsService
    val languageService = CCAI.languageService
    val pushNotificationService = CCAI.pushNotificationService
    val chatService = CCAI.chatService              // Only available after initializeChat()
    val screenShareService = CCAI.screenShareService // Only available after initializeScreenShare()
    val rateService = CCAI.rateService              // For CSAT ratings and survey submission
    val callService = CCAI.callService              // Only available after initializeCall()
    

**Note:** `CCAI` is an object (singleton) in Kotlin, so you access properties directly using `CCAI.propertyName` — no need to call `getInstance()` or use a shared accessor.**Warning:** `callService` requires its own initialization step. Unlike the other core services, `CCAI.callService` lives in the `CCAICall` module and is registered as an extension property on `CCAI` only after you call `CCAI.initializeCall(context)`. If you skip that step, `CCAI.callService` will be `null` at runtime and the scheduling APIs in Headless Mobile SDK for Android: voice, screen share, scheduled call, and email will be unreachable.

### Fetching company configuration

After initialization, you can fetch company-level configuration using the `companyService`. This is useful for populating language pickers, displaying the company name, or reading support contact details before the user enters a queue.
    
    
    // Fetch company details
    val company = CCAI.companyService?.get()
    
    // CompanyResponse contains:
    // - displayName: String
    // - supportEmail: String?
    // - languages: List<String>
    // - phoneNumber: String?
    // ...
    

**Note:** The `languages` list returned by `companyService` reflects what your admins have enabled in the CCAI Platform Portal. Use it to build a language picker in your app's settings.

## Authenticate end users and pass custom data

The Headless Mobile SDK for Android uses JSON web tokens (JWT) to authenticate users and securely pass contextual information to the agent's CRM.

### How it works

The SDK uses a simplified two-step async authentication flow:

  1. The SDK determines it needs to authenticate the user.

  2. It calls your `CCAIDelegate` method - `ccaiShouldAuthenticate()` \- which is a suspend function.

  3. Your app signs a JWT remotely on your backend server using your `Company

  4. Your app signs a JWT remotely on your backend server using your `Company Secret Code`.

  5. Your app then passes the signed JWT to `CCAI.authService?.authenticate(jwt)` to exchange it for an auth token.

  6. The auth token is returned to the SDK to complete the connection.


**Warning:** JWT signing must always be performed on your backend server. Never embed the `Company Secret Code` inside your compiled Android app - doing so creates a severe security vulnerability.

### Implement the `CCAIDelegate` for authentication

Your app must implement the `CCAIDelegate` interface. The SDK calls the first suspend method when it needs authentication.

#### `CCAIDelegate` interface
    
    
    interface CCAIDelegate {
        suspend fun ccaiShouldAuthenticate(): String?
    }
    

#### Implementation example (Kotlin)
    
    
    class CCAIDelegate : CCAIDelegate {
        override suspend fun ccaiShouldAuthenticate(): String? {
            // 1. Sign JWT remotely on your backend server
            val jwt = signJWTRemotely() ?: return null
    
            // 2. Authenticate JWT using authService to get an auth token
            return try {
                CCAI.authService?.authenticate(jwt)
            } catch (e: Exception) {
                null
            }
        }
    }
    

#### Full example with JWT signing (for reference and testing only)
    
    
    class AuthController : CCAIDelegate {
        override suspend fun ccaiShouldAuthenticate(): String? {
            // First, sign JWT with company secret (do this on your backend in production)
            val jwt = Jwts.builder()
                .setClaims(claims)
                .signWith(SignatureAlgorithm.HS384, companySecret?.encodeToByteArray())
                .compact()
    
            // Then authenticate JWT using authService to get an auth token
            return try {
                CCAI.authService?.authenticate(jwt)
            } catch (e: Exception) {
                null
            }
        }
    }
    

### Pass custom data to the CRM

If you want to pass contextual data to the agent (for example, the user's current device OS, location, or account tier), your backend must inject a `custom_data` object into the JWT payload before signing it.

Each piece of custom data must be formatted as a `JSON` object containing a label (what the agent sees), a value, and a type.

#### Supported data types

  * `string`: standard text (for example, "Pixel 8 Pro").

  * `number`: integers or floats (for example, 1234 or 99.99).

  * `date`: a 13-digit UTC Unix timestamp including milliseconds (for example, 1537399655992).

  * `url`: standard HTTP/HTTPS URL format.

  * `boolean`: standard true or false value.




**Agent visibility** : You can optionally pass data to the CCAI Platform platform that is hidden from the human agent but available for routing or backend analytics. To do this, include `"invisible_to_agent": true` in the data object.

### Reserved CRM keys

CCAI Platform supports specific reserved keys that trigger built-in behaviors in the platform, such as flagging a user as a VIP or warning an agent about a bad actor. These must be formatted as `boolean` types and will only be accepted if the payload is signed using the secure `JWT` method.

  * `reserved_verified_customer`: indicates whether a customer has been successfully authenticated by your internal systems.

  * `reserved_bad_actor`: flags the user to the agent as a potential spammer or fraudulent account.

  * `reserved_repeat_customer`: indicates whether this customer has frequently contacted support recently.




#### Example payload with reserved keys
    
    
    {
      "iat": 1537399656,
      "exp": 1537400256,
      "custom_data": {
        "reserved_verified_customer": {
          "label": "Verified Customer",
          "value": true,
          "type": "boolean"
        },
        "reserved_bad_actor": {
          "label": "Bad Actor",
          "value": false,
          "type": "boolean"
        },
        "reserved_repeat_customer": {
          "label": "Repeat Customer",
          "value": false,
          "type": "boolean"
        }
      }
    }
    

### Manage auth tokens

The SDK provides methods to manually update or clear the cached authentication token:
    
    
    // Set a new auth token
    CCAI.authService?.updateAuthToken("new_auth_token")
    
    // Clear the current token (for example, on user logout)
    CCAI.authService?.updateAuthToken(null)
    

**Warning:** When `cacheAuthToken` is `true` (the default in `InitOptions`), the SDK caches the auth token so it can be reused across app launches without re-signing. The cached token is used until it expires or is explicitly cleared. You must clear the cached token whenever user-related data changes — most importantly on sign-out events, user switching, or profile updates. Failing to do so can cause the SDK to authenticate the _previous_ user's session. Call `updateAuthToken(null)` as part of your logout routine.

### Custom data JWT payload schema

When your backend constructs the final payload to be signed with your `Company Secret Code`, it must strictly follow this schema. Note the mandatory `iat` (issued at) and `exp` (expiration) timestamps.
    
    
    {
      "iat": 1537399656,
      "exp": 1537400256,
      "custom_data": {
        "os_version": {
          "label": "OS Version",
          "value": "14.0",
          "type": "string"
        },
        "membership_tier": {
          "label": "Membership Tier",
          "value": "Platinum",
          "type": "string"
        },
        "ssn_last_four": {
          "label": "SSN",
          "value": "1234",
          "type": "string",
          "invisible_to_agent": true
        },
        "reserved_verified_customer": {
          "label": "Verified Customer",
          "value": true,
          "type": "boolean"
        }
      }
    }
    

## Enable push notifications

The SDK uses push notifications for:

  * Incoming calls.

  * Certain smart actions and call-related events.

  * Maintaining state when the app is in the background.




### Firebase setup

  1. Create or use an existing Firebase project.

  2. Register your Android app and download the `google-services.json` file.

  3. Place `google-services.json` in your app module directory.

  4. In your root-level `build.gradle.kts`, add the Google services plugin:
         
         // build.gradle.kts (Project)
         plugins {
             id("com.google.gms.google-services") version "4.4.2" apply false
         }
         

  5. In your app-level `build.gradle.kts`, apply the plugin and add `Firebase` dependencies:
         
         // app/build.gradle.kts
         plugins {
             id("com.google.gms.google-services")
         }
         
         dependencies {
             // Firebase BoM for version management
             implementation(platform("com.google.firebase:firebase-bom:33.5.1"))
             implementation("com.google.firebase:firebase-messaging")
         }
         

  6. Sync the project.




### Register the FCM token with the SDK

Register the FCM push token through `pushNotificationService` and forward incoming FCM data payloads to the SDK. Your app is responsible for rendering any customer-facing notification or in-call UI.

#### Implement `onMessageReceived`

If you are using FCM, implement a listener in your `FirebaseMessagingService` class for push notifications. **If these aren't implemented, the service won't work properly.**
    
    
    import com.google.firebase.messaging.FirebaseMessagingService
    import com.google.firebase.messaging.RemoteMessage
    import com.ccaiplatform.ccaikit.CCAI
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.Dispatchers
    import kotlinx.coroutines.launch
    
    class MyFirebaseMessagingService : FirebaseMessagingService() {
    
        private val scope = CoroutineScope(Dispatchers.IO)
    
        override fun onMessageReceived(remoteMessage: RemoteMessage) {
            scope.launch {
                // Forward CCAI platform push notifications to the SDK.
                CCAI.pushNotificationService?.handlePushNotification(remoteMessage.data)
    
                // Render any customer-facing notification UI in your own app code.
                MyNotificationRenderer.showIfNeeded(application, remoteMessage.data)
            }
        }
    }
    

**Note:** `CCAI.pushNotificationService?.handlePushNotification()` processes the notification at the platform level. Build your own notification renderer for visible notifications, incoming-call screens, and any app-specific notification behavior.

#### Implement `onNewToken`

Also implement the `onNewToken` method to handle token updates. This ensures that the Headless Mobile SDK for Android receives the latest push notification token:
    
    
    class MyFirebaseMessagingService : FirebaseMessagingService() {
        // ...
        override fun onNewToken(token: String) {
            // Fetch the updated token from Firebase and update it in CCAI
            CCAI.pushNotificationService?.updatePushToken(token)
        }
    }
    

#### Register the service in `AndroidManifest.xml`

Add the Firebase Messaging Service to your `AndroidManifest.xml` so the system can deliver push messages to your service:
    
    
    <application>
        <service
            android:name=".firebase.MyFirebaseMessagingService"
            android:exported="true">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT" />
            </intent-filter>
        </service>
    </application>
    

### Initial token registration

At app startup (after SDK initialization), proactively register the current FCM token:
    
    
    import com.google.firebase.messaging.FirebaseMessaging
    
    // In your Application.onCreate(), after CCAI.initialize()
    FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
        if (task.isSuccessful) {
            val token = task.result
            CCAI.pushNotificationService?.updatePushToken(token)
        }
    }
    

### Notification permission handling (Android 13+)

On Android 13 (API level 33) and the aforementioned apps must request the `POST_NOTIFICATIONS` runtime permission. The SDK provides a built-in utility for this:
    
    
    import com.ccaiplatform.ccaikit.util.PermissionUtil
    
    // Request notification permissions from the user
    PermissionUtil.requestPermissionsForNotifications(activity)
    
    // Check if permissions have been granted
    val isGranted = PermissionUtil.isPermissionsForNotificationsGranted(context)
    if (isGranted) {
        Log.d("CCAI", "Push notifications permitted")
    }
    

Call this early in your app lifecycle (for example, during onboarding or first launch) before registering the FCM token, so push notifications can be delivered.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
