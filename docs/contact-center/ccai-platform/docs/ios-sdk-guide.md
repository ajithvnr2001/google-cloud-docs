---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide/
title: iOS SDK guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:32:37.764233+00:00
---

# iOS SDK guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  iOS SDK guide Stay organized with collections  Save and categorize content based on your preferences. 

The Contact Center AI Platform (CCAI Platform) mobile SDK for the Apple iOS operating system provides the ability to embed the CCAI Platform mobile experience within iOS mobile applications.

## Requirements

The iOS mobile SDK has the following requirements:

  * iOS 12.0+



### Retrieve company credentials

  1. Sign into the Contact Center AI Platform (CCAI Platform) portal using Admin credentials.

  2. Go to **Settings > Developer Settings**.

  3. Under **Company Key** and **Secret Code** , note Company Key and Company Secret Code.




## Getting started

The following provides a guide on how to get started with the CCAI Platform iOS mobile SDK.

## Installation

To start get started you need to install the iOS SDK.

### Download the example app

  1. Download the [iOS Example App](https://externals.ujet.co/packages/ujet-ios-sdk-example.zip).

  2. Navigate to the folder and install dependencies using CocoaPods:
         
         $ pod install --project-directory=ExampleApp
         

  3. To quickly configure project settings, run a shell script:
         
         $ ./setup.sh
         

Alternatively, you can manually edit project settings by following these steps:

     1. Open `ExampleApp.xcworkspace`.

     2. Replace the `UJETCompanyKey` and `UJETCompanySecret` values in `Info.plist` with the **Company Key** and **Company Secret Code** values from the **Settings > Developer Settings** page in the CCAI Platform portal.

     3. Replace the `UJETSubdomain` value in `Info.plist` with the subdomain in the URL for your CCAI Platform portal. The subdomain directly precedes `.ujet.com` in the URL— for example, `your-subdomain` in `https://your-subdomain.ujet.com/settings/developer-setting`.




### Integrate to your project

Integration of the iOS SDK with your application depends on your development environment.

#### Swift package manager

  1. Add the [Swift Package for iOS SDK](https://github.com/ujet/ujet-ios-sdk-sp.git).

  2. In your build settings, put -ObjC on Other Linker Flags.

  3. As of the latest release of Xcode (currently 13.2), there is a [known issue](https://bugs.swift.org/browse/SR-13343) with consuming binary frameworks distributed using the Swift Package Manager. The current workaround to this issue is to add a Run Script Phase to the Build Phases of your Xcode project. This Run Script Phase should come after the Embed Frameworks build phase. This new Run Script Phase should contain the following code:
         
         find "${CODESIGNING_FOLDER_PATH}" -name '*.framework' -print0 | while read -d $'0' framework
         do
         codesign --force --deep --sign "${EXPANDED_CODE_SIGN_IDENTITY}" --preserve-metadata=identifier,entitlements --timestamp=none "${framework}"
         done
         




#### CocoaPods

  1. Add the following line to the Podfile:
         
         pod 'UJET', :podspec =>
         'https://sdk.ujet.co/ios/x.y.z/ujet.podspec' #specific version
         x.y.z
         

  2. Run pod install. If the iOS SDK has been integrated previously, run pod update CCAI Platform instead.




#### Carthage

Google Cloud recommends using a dependency manager or manual integration because a CCAI Platform dependency doesn't support Carthage. 

To use a different dependency manager, follow these steps:

  1. Add the following lines:
         
         binary "https://sdk.ujet.co/ios/UJETKit.json"
         binary "https://sdk.ujet.co/ios/UJETFoundationKit.json"
         binary "https://sdk.ujet.co/ios/UJETCallRedKit.json"
         binary "https://sdk.ujet.co/ios/UJETChatRedKit.json"
         # optional
         # binary "https://sdk.ujet.co/ios/UJETChatBlueKit.json"
         binary "https://raw.githubusercontent.com/twilio/twilio-voice-ios/Releases/twilio-voice-ios.json"
         # this is not supported: https://github.com/twilio/conversations-ios/issues/12
         # binary "https://raw.githubusercontent.com/twilio/conversations-ios/master/twilio-convo-ios.json"
         

  2. Run `carthage bootstrap --use-xcframeworks` (or `carthage update --use-xcframeworks` if you're updating dependencies).




##### Manual integration

  1. Download `UJETKit.xcframework`, `UJETFoundationKit.xcframework`, `UJETChatRedKit.xcframework`, `UJETChatBlueKit.xcframework`, `UJETTwilioCallKit.xcframework`, and all dependencies `TwilioVoice.xcframework` and `TwilioConversationsClient.xcframework`.

  2. Add the UJETKit.xcframework to your target by dragging it into the Frameworks, Libraries, and Embedded Content section.

  3. Repeat Steps 2 and 3 on all dependencies from Step 1.

  4. In your _Build Settings_ , put `-ObjC` on `Other Linker Flags`.

  5. Add `libc++.tbd` as a dependency in `Linked Frameworks` section of target.




If you are going to build the SDK manually with the example project use the steps in the following section.

##### Build the SDK manually with the example project

Follow these steps in order:

  1. Download all frameworks including `UJETKit.xcframework` and other dependencies.

  2. Create folder CCAI Platform on the project root and extract all frameworks.

  3. Select `Objc-Manual` or `Swift-Manual` target and build.




### Import framework

The following sections provide instructions on how to import the framework.

#### Objective-C Project
    
    
    @import UJETKit;
    

#### Swift Project
    
    
    swiftimport
    UJETimport UJETKit
    

### Initialize SDK

Initialize CCAI Platform with `UJET_COMPANY_KEY` and `UJET_SUBDOMAIN`.
    
    
    In application:didFinishLaunchingWithOptions: method:
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
        // Initialize CCAI Platform
        [UJET.initialize:UJET_COMPANY_KEY subdomain:UJET_SUBDOMAIN delegate:self];
    
        // YOUR CODE
    
        return YES;
    }
    

You can change log level from `verbose` to `error`. The default log level is `UjetLogLevelInfo`.
    
    
    [UJET.setLogLevel:UjetLogLevelVerbose];
    

### End-user authentication

Access the iOS SDK through the iOS app.

In order to make sure that the end user is authenticated, we are introducing the JWT signing mechanism.

The iOS SDK will ask to sign the payload when authentication is needed. If the signing is successful, the application exchanges the signed JWT to the end user auth token. The success or failure block must be called before the delegate returns.

For anonymous user (identifier = nil), the application will create a UUID for the user. If at a later time the user is authenticated with an identifier, the application will attempt to merge the two users based on the UUID.

In `UJETObject.h` from example project:
    
    
    @import UJETKit;
    
    @interface UJETObject : NSObject <UJETDelegate>
    

Implement `signPayload`: `payloadType`: success: failure: delegate method.
    
    
    - (void)signPayload:(NSDictionary *)payload payloadType:(UjetPayloadType)payloadType success:(void (^)(NSString *))success failure:(void (^)(NSError *))failure {
      if (payloadType == UjetPayloadAuthToken) {
        [self signAuthTokenInLocal:payload success:success failure:failure];
      }
    }
    
    - (void)signAuthTokenInLocal:(NSDictionary *)payload success:(void (^)(NSString *))success failure:(void (^)(NSError *))failure {
        NSMutableDictionary *payloadData = [payload mutableCopy];
    
        NSDictionary *userData = [[NSUserDefaults standardUserDefaults] objectForKey:@"user-data"];
        [payloadData addEntriesFromDictionary:userData];
        payloadData[@"iat"] = [NSNumber numberWithDouble:[[NSDate date] timeIntervalSince1970]]; // required
        payloadData[@"exp"] = [NSNumber numberWithDouble:([[NSDate date] timeIntervalSince1970] + 600)]; // required
    
        NSString *signedToken = [self encodeJWT:payloadData];
    
        if (signedToken.length > 0) {
            success(signedToken);
    
        } else {
            NSDictionary *userInfo = @{ NSLocalizedDescriptionKey: @"Failed to sign token" };
            NSError *error = [NSError errorWithDomain:@"ExampleApp" code:0 userInfo:userInfo];
            failure(error);
        }
    }
    
    - (NSString *)encodeJWT:(NSDictionary *)payload {
        id<JWTAlgorithm> algorithm = [JWTAlgorithmHSBase algorithm384];
        NSString *secret = NSBundle.mainBundle.infoDictionary[@"UJETCompanySecret"];
        return [JWTBuilder encodePayload:payload].secret().algorithm(algorithm).encode;
    }
    

We strongly recommend signing the payload from your application server, not in the client.

This example uses local signing for testing purposes. See `signDataInRemote: success: failure:` in the `UJETObject.m` file.

For more information, see [SDK End user authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth).

### Set up push notifications

The application sends push notifications to request Smart Actions like verification and photo, as well as reporting an incoming call. The application requires two different types of certificates (VoIP and APNs) to be saved in the Admin Portal.

#### Prepare VoIP services certificate

Reference documentation is available for [Apple's VoIP push notification](https://developer.apple.com/library/ios/documentation/Performance/Conceptual/EnergyGuide-iOS/OptimizeVoIP.html).

  1. Create and download the VoIP certificate from the Apple developer site.

  2. Double-click the certificate to add it to Keychain.

  3. Start the Keychain Access application on your Mac.

  4. Pick the My Certificates category in the left hand sidebar.

  5. Right-click VoIP Services: your.app.id certificate.

  6. In the popup menu choose **Export**.

  7. Save it as cert.p12 without protecting it with a password by leaving the password blank.

  8. Run the following command in terminal.
         
         openssl s_client -connect gateway.push.apple.com:2195 -cert cert.pem -debug -showcert
         

  9. The upper part of cert.pem is the certificate and the lower part is the private key.

  10. Check that your certificate is working with Apple's push notification server.
         
         openssl s_client -connect gateway.push.apple.com:2195 -cert cert.pem -debug -showcerts
         

When successful, it should return:
         
         ---
         New, TLSv1/SSLv3, Cipher is AES256-SHA
         Server public key is 2048 bit
         Secure Renegotiation IS supported
         Compression: NONE
         Expansion: NONE
         SSL-Session:
             Protocol  : TLSv1
             Cipher    : AES256-SHA
             Session-ID:
             Session-ID-ctx:
             Master-Key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
             Key-Arg   : None
             Start Time: 1475785489
             Timeout   : 300 (sec)
             Verify return code: 0 (ok)
         ---
         

  11. Sign in to the CCAI Platform portal with administrator credentials, and go to **Settings > Developer Settings > Mobile App**.

  12. Fill the certificate in the 'VoIP Services Certificate' section, and save. Be sure to contain boundaries (`-----BEGIN-----` and `-----END-----`) for both certificate and private key.

  13. Check the Sandbox checkbox if you are running an app with a development provisioning profile such as debugging in Xcode. If your app is archived for Ad hoc or App store and is using a distribution provisioning profile, then clear the Sandbox checkbox.




#### Prepare Apple push notification service SSL

The process for this is similar to that for VOIP service certificates. In this case Apple push notification service SSL (Sandbox & Production) certificate is used. You can refer to the [Apple remote notification server documentation](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns) for guidance on how to create the certificate.

#### Integrating push notification

In `AppDelegate.m`:
    
    
    @import PushKit;
    
    @interface AppDelegate() <PKPushRegistryDelegate>
    In application:didFinishLaunchingWithOptions: method:
    // Initialize CCAI Platform
    [UJET initialize:UJET_COMPANY_KEY subdomain:UJET_SUBDOMAIN delegate:self];
    
    //  Register for VoIP notifications on launch.
    PKPushRegistry *voipRegistry = [[PKPushRegistry alloc] initWithQueue: dispatch_get_main_queue()];
    voipRegistry.delegate = self;
    voipRegistry.desiredPushTypes = [NSSet setWithObject:PKPushTypeVoIP];
    

Add the following delegate methods in implementing `UIApplicationDelegate` protocol file:

Please print your device token to test push notifications.
    
    
    // PKPushRegistryDelegate
    
    - (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(NSString *)type {
      [UJET updatePushToken:credentials.token type:UjetPushTypeVoIP];
    }
    
    - (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(PKPushType)type withCompletionHandler:(void (^)(void))completion {
      if (payload.dictionaryPayload[@"ujet"]) {
        [UJET receivedNotification:payload.dictionaryPayload completion:completion];
      } else {
        completion();
      }
    }
    
    // UIApplicationDelegate
    
    - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      [UJET updatePushToken:deviceToken type:UjetPushTypeAPN];
    }
    
    - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
      if (userInfo[@"ujet"]) {
        [UJET receivedNotification:userInfo completion:nil];
      }
    }
    
    // UserNotificationsDelegate overrides [UIApplicationDelegate didReceiveRemoteNotification:]
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler {
        NSDictionary *userInfo = notification.request.content.userInfo;
    
        if (userInfo[@"ujet"] != nil) {
            [UJET receivedNotification:userInfo completion:nil];
        }
    }
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler {
        NSDictionary *userInfo = response.notification.request.content.userInfo;
    
        if (userInfo[@"ujet"] != nil) {
            [UJET receivedNotification:userInfo completion:nil];
        }
    }
    

### Enable push notifications

  1. Select your target and open **Capabilities** tab.

  2. Turn on the switch of **Push Notifications**.




### Test push notifications

The following sections provide guidance on how to test the push notifications.

#### Push notification debug section

In the administrator portal, navigate to Settings > Developer Settings. On this page, find the section titled **Push Notification Debug** :

Copy and paste the device token in the right text area and select the right Mobile App.

**Note:** Simulators don't support push notification tests.

#### Get the device token

An example device token string looks like this:

`7db0bc0044c8a203ed87cdab86a597a2c43bf16d82dae70e8d560e88253364b7`

Push notifications are usually set in the class which conforms to UIApplicationDelegate or PKPushRegistryDelegate protocol. At some point, the device token is available to you. You can print it out before passing it to the iOS SDK. To get your device token, use the code snippet.

##### Swift
    
    
    func tokenFromData(data: Data) -> String {
      return data.map { String(format: "%02x", $0) }.joined()
    }
    
    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
      print("apns token: ", tokenFromData(data: deviceToken))
      ...
    }
    
    func pushRegistry(_ registry: PKPushRegistry, didUpdate credentials: PKPushCredentials, for type: PKPushType) {
      print("voip token: ", tokenFromData(data: credentials.token))
      ...
    }
    

##### Obj-C
    
    
    - (NSString *)tokenFromData:(NSData *)data {
      const char *d = data.bytes;
      NSMutableString *token = [NSMutableString string];
    
      for (NSUInteger i = 0; i < data.length; i++) {
        [token appendFormat:@"%02.2hhX", d[i]];
      }
    
      return [[token copy] lowercaseString];
    }
    
    - (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(PKPushType)type {
      NSLog(@"voip token: %@", [self tokenFromData:credentials.token]);
      ...
    }
    
    - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      NSLog(@"apns token: %@", [self tokenFromData:deviceToken]);
    }
    

##### Result

Once you have entered the certificate PEM file and the device token, click the button.

The result will show a message _Push notification successfully configured_ if the test push notification was successfully delivered.

Push notification is not 100% guaranteed to be delivered, depending on the device's network connection.

### Project configurations

The following sections outline the changes needed to configure the project.

#### Capabilities

In target settings, turn on the following capabilities:

  * Push Notifications

  * Background Modes (check these items)

  * Audio and AirPlay

  * Voice over IP




#### Info.plist

To protect user privacy, any iOS app linked on or after iOS 10.0 which accesses any of the device's microphones, photo library, and camera, must declare the intent to do so. Include the following keys with a string value in your app's Info.plist file and provide a purpose string for this key. If your app attempts to access any of the device's microphones, photo library and camera without a corresponding purpose string, the app exits.

  * NSMicrophoneUsageDescription: Allows access to the microphone for calling and talking to support or troubleshooting teams, and for sending videos with sound related to product inquiries.

  * NSCameraUsageDescription: Allows access to the camera for customer to take and send photos related to their customer support inquiry.

  * NSPhotoLibraryUsageDescription: Allows access for customer to send photos related to their customer support inquiry.

  * NSFaceIDUsageDescription: Allows access to verification using Face ID.




### Start the iOS SDK

Add the following line where you want to start the iOS SDK:
    
    
    [UJET startWithOptions:nil];
    

You can also start the iOS SDK from a specific point in the menu with this key using a Direct Access Point:
    
    
    UJETStartOptions *option = [[UJETStartOptions alloc] initWithMenuKey:@"MENU_KEY"];
    [UJET startWithOptions:option];
    

The `menuKey` can be created by creating a **Direct Access Point** (DAP). The Following steps provide direction on how to create a DAP:

  1. Sign in to the CCAI Platform portal with in with administrator credentials.

  2. Go to **Settings > Queue**.

  3. Select any queue from the menu structure.

  4. Select **Create direct access point**

  5. Enter key in the text form.

  6. Click **Save**.




#### Clear cache from local if user data has been updated

We're caching auth token in the Keychain to re-use and make less frequent requests to sign payload from the host app. The SDK will use it until expired or revoked through clearUserData call. The host app is in charge of revoking this cache whenever user related data has changed or updated such as a sign out event.
    
    
    [UJET clearUserData];
    

#### Check for existing session before starting Contact Center AI Platform

Before starting a session, check to see if there isn't a current session. This is especially important when the userId has changed.
    
    
    [UJET getStatus];
    

If there is an existing session, we should prompt the user to resume the session or cancel the action:
    
    
    if ([UJET getStatus] != UjetStatusNone) {
      // Display alert to cancel login or resume existing session
    }
    

### Customize

There are several options for the SDK theme listed in `UJETGlobalTheme.h`.

Set your theme after `[UJET initialize]`—for example:
    
    
    UJETGlobalTheme *theme = [UJETGlobalTheme new];
    
    theme.font = [UIFont fontWithName:@"OpenSans" size: 16.0f];
    theme.lightFont = [UIFont fontWithName:@"OpenSans-Light" size: 16.0f];
    theme.boldFont = [UIFont fontWithName:@"OpenSans-Bold" size: 16.0f];
    theme.tintColor = [UIColor colorWithRed:0.243 green:0.663 blue:0.965 alpha:1.00];
    
    [Ujet setGlobalTheme:theme];
    

The company name is retrieved from **Admin Portal > Settings > Support Center Details > Display Name**.

You can set the logo image instead of the company name like this:
    
    
    theme.companyImage = [UIImage imageNamed:@"logo"];
    

The image will be resized to fit on the area if it is too large.

#### Strings

You can also customize strings by overriding the value. For example, put this key - value on your Localizable.strings:
    
    
    "ujet_greeting_title" = "Title";
    
    "ujet_greeting_description" = "Description";
    

Available customizable strings are listed in ujet.strings file.

#### Dark mode

You can specify a tint of the color you want for dark mode to better legibility of fonts.
    
    
    @property (nonatomic, strong) UIColor \*tintColorForDarkMode;
    

If you don't set the property then UJETGlobalTheme.tintColor will be used for dark mode. We recommend setting this property if your app supports dark mode. Refer to the following Apple articles on how to pick the right tint color for dark mode:

  * [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/dark-mode/)

  * [Color](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/)




#### Chat theme

To customize the chat screen, you have the option to use a JSON string or each theme class.

For reference, see the example app and uncomment the `customizeChatTheme` method.
    
    
    func customizeChatTheme() throws {
      guard let file = Bundle.main.path(forResource: "chat-theme-custom", ofType: "json") else { return }
      let json = try String.init(contentsOfFile: file, encoding: .utf8)
    
      let chatTheme = UJETChatTheme.init(jsonString: json)
    
      let quickReplyTheme = UJETChatQuickReplyButtonTheme()
      quickReplyTheme.style = .individual
      quickReplyTheme.alignment = .right
      quickReplyTheme.backgroundColor = UJETColorRef(assetName: "white_color")
      quickReplyTheme.backgroundColorForHighlightedState = UJETColorRef(assetName: "quick_reply_color")
      quickReplyTheme.textColor = UJETColorRef(assetName: "quick_reply_color")
      quickReplyTheme.textColorForHighlightedState = UJETColorRef(assetName: "white_color")
    
      let fontTheme = UJETFontTheme()
      fontTheme.family = "Arial Rounded MT Bold"
      fontTheme.size = 14
      quickReplyTheme.font = fontTheme
    
      chatTheme?.quickReplyButtonTheme = quickReplyTheme
    
      let globalTheme = UJETGlobalTheme()
      globalTheme.chatTheme = chatTheme
      globalTheme.defaultAgentImage = UIImage(named: "agent_avatar_image")
      globalTheme.font = UIFont(name: "Arial Rounded MT Bold", size: 14)
    
      UJET.setGlobalTheme(globalTheme)
    }
    

#### Content cards theme

You can add customization for content cards together with chat customization. You can do this either using the json file (see `content_card` property) or by using the `UJETChatContentCardTheme` class.
    
    
    func customizeChatTheme() throws {
      guard let file = Bundle.main.path(forResource: "chat-theme-custom", ofType: "json") else { return }
      let json = try String.init(contentsOfFile: file, encoding: .utf8)
    
      let chatTheme = UJETChatTheme.init(jsonString: json)
    
      let contentCardTheme = UJETChatContentCardTheme()
      contentCardTheme.backgroundColor = UJETColorRef(assetName: "agent_message_background_color")
      contentCardTheme.cornerRadius = 16
    
      let contentCardFontTheme = UJETFontTheme()
      contentCardFontTheme.family = "Arial Rounded MT Bold"
      contentCardFontTheme.size = 18
      contentCardTheme.font = contentCardFontTheme
    
      let contentCardBorder = UJETBorderTheme()
      contentCardBorder.width =  1
      contentCardBorder.color = UJETColorRef(assetName: "agent_message_border_color")
      contentCardTheme.border = contentCardBorder
    
      let contentCardFontTheme = UJETFontTheme()
      contentCardFontTheme.family = "Arial Rounded MT Bold"
      contentCardFontTheme.size = 18
      contentCardTheme.font = contentCardFontTheme
    
      // The font family is inherited from the contentCardFontTheme
      let subtitle = UJETFontTheme()
      subtitle.size = 12
      contentCardTheme.subtitle = subtitle
    
      // The font family is inherited from the contentCardFontTheme
      let bodyFont = UJETFontTheme()
      bodyFont.size = 10
      contentCardTheme.body = bodyFont
    
      theme.chatTheme?.contentCard = contentCardTheme
    
      let globalTheme = UJETGlobalTheme()
      globalTheme.chatTheme = chatTheme
      globalTheme.defaultAgentImage = UIImage(named: "agent_avatar_image")
      globalTheme.font = UIFont(name: "Arial Rounded MT Bold", size: 14)
    
      UJET.setGlobalTheme(globalTheme)
    }
    

#### Form card theme

You can add customization for form cards together with chat customization. Do this by either using the json file (see the `form_card property`) or by using the `UJETChatFormCardTheme` class.
    
    
    func customizeChatTheme() throws {
        guard let file = Bundle.main.path(forResource: "chat-theme-custom", ofType: "json") else { return }
        let json = try String.init(contentsOfFile: file, encoding: .utf8)
    
        let chatTheme = UJETChatTheme.init(jsonString: json)
    
        let formCardTheme = UJETChatFormCardTheme()
        formCardTheme.backgroundColor = UJETColorRef(assetName: "agent_message_background_color")
        formCardTheme.cornerRadius = 16
    
        let formCardFontTheme = UJETFontTheme()
        formCardFontTheme.family = "Arial Rounded MT Bold"
        formCardFontTheme.size = 18
        formCardTheme.font = formCardFontTheme
    
        let formCardBorder = UJETBorderTheme()
        formCardBorder.width =  1
        formCardBorder.color = UJETColorRef(assetName: "agent_message_border_color")
        formCardTheme.border = formCardBorder
    
        let titleFontTheme = UJETFontTheme()
        titleFontTheme.family = "Arial Rounded MT Bold"
        titleFontTheme.size = 18
        formCardTheme.title = titleFontTheme
    
        // The font family is inherited from the formCardFontTheme
        let subtitleFontTheme = UJETFontTheme()
        subtitleFontTheme.size = 12
        formCardTheme.subtitle = subtitleFontTheme
    
        chatTheme?.formCard = formCardTheme
    
        let globalTheme = UJETGlobalTheme()
        globalTheme.chatTheme = chatTheme
        globalTheme.defaultAgentImage = UIImage(named: "agent_avatar_image")
        globalTheme.font = UIFont(name: "Arial Rounded MT Bold", size: 14)
    
        UJET.setGlobalTheme(globalTheme)
    }
    

#### Web form configuration

To configure the web form capability, implement the `ujetWebFormDidReceive` method of the `UJETDelegate` protocol. This method receives an event (a `FormMessageReceivedEvent` dictionary) as a parameter, containing form-related information. The event (`FormMessageReceivedEvent`) dictionary includes the following JSON structure:
    
    
      {
        "type": "form_message_received",
        "smart_action_id": 1,
        "external_form_id": "external_foobar"
        "signature": "4868a7e1dcb5..."
      }
    

To handle the event, do the following:

  1. Extract the relevant information from the event dictionary (`smart_action_id`, `external_form_id`, and `signature`).

  2. Generate a form URI and a signature for the form data.

  3. Pass the form data to the SDK as a `FormDataEvent` dictionary using `completion closure`.

  4. If any error occurs during URI/signature generation, invoke the callback using `callback.onError()` with the `Error`.




The dictionary (`FormDataEvent`) passed to the SDK should have the following structure:
    
    
     {
        "type": "form_data",
        "signature": "4868a7e1dcb5...",
        "data": {
           "smart_action_id":1,
           "external_form_id": "form_id",
           "uri":"foobar"
        }
      }
    

The signature (HMAC-SHA:256) must be generated using the `data`, signed with the shared secret key. The object keys of data must be alphabetically ordered prior to generating signatures and the same `data` should be sent to the SDK.

#### Post session transfer

You can add customization for post session va together with chat customization. This can be accomplished either using the JSON file (see `post_session` property) or by using the `UJETChatPostSessionVaTheme` class. Border width can be only 0 or 1 and if you don't want to differentiate the post session VA experience then you could set `containerColor` white and border to 0.
    
    
    func customizeChatTheme() throws {
        guard let file = Bundle.main.path(forResource: "chat-theme-custom", ofType: "json") else { return }
        let json = try String.init(contentsOfFile: file, encoding: .utf8)
    
        let chatTheme = UJETChatTheme.init(jsonString: json)
    
        let postSessionVaTheme = UJETChatPostSessionVaTheme()
        postSessionVaTheme.containerColor = UJETColorRef(assetName: "white_color")
    
        let postSessionVaBorder = UJETBorderTheme()
        postSessionVaBorder.width =  0
        postSessionVaBorder.color = UJETColorRef(assetName: "white_color")
        containerColor.border = postSessionVaBorder
    
        chatTheme?.postSessionVaTheme = postSessionVaTheme
    
        let globalTheme = UJETGlobalTheme()
        globalTheme.chatTheme = chatTheme
    
        UJET.setGlobalTheme(globalTheme)
    }
    

#### Chat actions menu

You can add customization for chat actions menu together with chat customization. This can be accomplished either by using the JSON file (see `form_card` property) or by using the UJETChatActionMenuTheme class.
    
    
    func customizeChatTheme() throws {
        guard let file = Bundle.main.path(forResource: "chat-theme-custom", ofType: "json") else { return }
        let json = try String.init(contentsOfFile: file, encoding: .utf8)
    
        let chatTheme = UJETChatTheme.init(jsonString: json)
    
        let actionMenuTheme = UJETChatActionMenuTheme()
    
        let photoLibraryIcon = UJETChatUserInputIconTheme()
        photoLibraryIcon.visible = true
        photoLibraryIcon.image = UJETImageRef(assetName: "library_button_asset")
    
        let cameraIcon = UJETChatUserInputIconTheme()
        cameraIcon.visible = true
        cameraIcon.image = UJETImageRef(assetName: "camera_button_asset")
    
        let cobrowseIcon = UJETChatUserInputIconTheme()
        cobrowseIcon.visible = true
        cobrowseIcon.image = UJETImageRef(assetName: "cobrowse_button_asset")
    
        actionMenuTheme.libraryIcon = photoLibraryIcon
        actionMenuTheme.cameraIcon = cameraIcon
        actionMenuTheme.cobrowseIcon = cobrowseIcon
    
        chatTheme?.actionMenu = actionMenuTheme
    
        let globalTheme = UJETGlobalTheme()
        globalTheme.chatTheme = chatTheme
    
        UJET.setGlobalTheme(globalTheme)
    }
    

#### Other appearances

You can customize other appearances such as font size and background color.
    
    
    theme.supportTitleLabelFontSize = 30;
    theme.supportDescriptionLabelFontSize = 20;
    theme.supportPickerViewFontSize = 30;
    theme.staticFontSizeInSupportPickerView = YES;
    
    theme.backgroundColor = UIColor.darkGrayColor;
    theme.backgroundColorForDarkMode = UIColor.lightGrayColor;
    

### CallKit

On iOS 10.0 and greater, CallKit is enabled for all calls.

With CallKit, it shows an in-app call coming in with the call screen and shows the call in the phone's call history.

To start a new CCAI Platform support session from call history, add the following block to your AppDelegate.m:
    
    
    AppDelegate.m:
    - (BOOL)application:(UIApplication *)app continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray * _Nullable))restorationHandler {
        if ([userActivity.activityType isEqualToString:@"INStartAudioCallIntent"]) {
            // Open app from Call history
            [UJET startWithOptions:nil];
        }
    
        return YES;
    }
    

CallKit allows a 40x40 icon to be displayed on the lock screen when receiving a call while the device is locked. Place an image in your Xcassets named 'icon-call-kit'.

### Configure the SDK

You can set several options before starting the SDK.

Please take a look at the UJETGlobalOptions class for details.
    
    
    UJETGlobalOptions *options = [UJETGlobalOptions new];
    options.fallbackPhoneNumber = @"+18001112222";
    options.preferredLanguage = @"en";
    
    [UJET setGlobalOptions:options];
    

#### Show or hide the download transcript button

You can configure the SDK to show or hide the download transcript button in the chat options menu and in the post-chat screen.

The following code shows how to configure the download transcript button:
    
    
    typedef NS_OPTIONS(NSUInteger, UJETChatDownloadTranscriptVisibilityOptions) {
        UJETChatDownloadTranscriptVisibilityOptionsShowAll = 0,
        UJETChatDownloadTranscriptVisibilityOptionsHideFromOptionsMenu = 1 << 0,
        UJETChatDownloadTranscriptVisibilityOptionsHideFromPostChatScreen = 1 << 1,
        UJETChatDownloadTranscriptVisibilityOptionsHideAll = UJETChatDownloadTranscriptVisibilityOptionsHideFromOptionsMenu | UJETChatDownloadTranscriptVisibilityOptionsHideFromPostChatScreen
    };
    
    @property (nonatomic, assign) UJETChatDownloadTranscriptVisibilityOptions transcriptVisibilityOptions;
    

#### PSTN Fallback

We provide PSTN fallback for several situations:

  * Mobile network is offline.

  * The application backend is not reachable.

  * VoIP is not available

    * The network condition is not good enough to connect. See UJETGlobalOptions.pstnFallbackSensitivity property for details.

    * A failure has occurred during connection due to firewall configuration or provider issue.




We recommend setting your company IVR number in UJETGlobalOptions.fallbackPhoneNumber. The recommended format is + followed by country code and phone number. eg. +18001112222.

##### PSTN Fallback Sensitivity

You can adjust the sensitivity level of checking network condition to PSTN fallback.

@property (nonatomic, assign) float pstnFallbackSensitivity;

The value must be in the range of 0.0 to 1.0. If set to 1, the call will always connect through the PSTN rather than VoIP. The maximum latency and the minimum bandwidth threshold are 10000ms and 10KB/s respectively for the value of 0. For example, a value of 0.5 means a minimum latency and bandwidth is 5000 ms and 15KB/s, respectively.

This value can be configured by following these steps:

  1. Sign in to the CCAI Platform portal as an administrator.

  2. Go to **Settings > Developer Settings > Mobile Apps**.

  3. Find the section **Fallback phone number threshold**. The default value is 0.85.

  4. Specify the new threshold value.

  5. Click **save**.




#### Turn off push notifications at the global level

You can turn off push notifications at the global level. Setting the following property to `false` bypasses all push notification dependencies and prevents push notifications from reaching end-users:
    
    
    @property (nonatomic, assign) BOOL allowsPushNotifications;
    

#### Ignore dark mode

You can ignore the dark mode in CCAI Platform SDK specifically with this property:
    
    
    @property (nonatomic, assign) BOOL ignoreDarkMode;
    

#### Hide Status Bar

You can control the visibility of the status bar with this property:
    
    
      @property (nonatomic, assign) BOOL hideStatusBar;
    

By default, the `hideStatusBar` is set to `false` and `visible`.

#### Skip the CSAT survey

You can add a button that lets the user skip the CSAT survey. The following code sample shows how to add the button:
    
    
    let options = UJETGlobalOptions()
    options.skipCsat = true
    

#### Chat check-in after-hours options

If your chat queues use [chat check-in](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-check-in), you can control what appears on the after-hours chat check-in screen. Both options are properties of `UJETGlobalOptions`.
    
    
    // YES to hide the "Next availability" message on the after-hours
    // chat check-in screen. Default is NO.
    @property (nonatomic, assign) BOOL hideNextAvailability;
    
    // YES to hide the "Start over" button on the after-hours chat
    // check-in screen. Default is NO.
    @property (nonatomic, assign) BOOL hideStartOver;
    

#### Customize the activity indicator

You can add your own loader animation (inside a `UIView`) to the SDK and override the default `UIActivityIndicatorView`. Implement the `ujet_activityIndicator` method from the `UJETDelegate` and return the customized view.
    
    
    public func ujet_activityIndicator() -> UIView! {
        let loader = UIView.init()
        let animation = CABasicAnimation()
        loader.backgroundColor = .blue
        loader.layer.cornerRadius = 15
        animation.timingFunction = CAMediaTimingFunction.init(name: CAMediaTimingFunctionName.easeOut)
        animation.keyPath = "transform.scale"
        animation.duration = 1.0
        animation.fromValue = 0.0
        animation.toValue = 1.0
        animation.repeatCount = Float.infinity
        animation.isRemovedOnCompletion = false
        loader.layer.add(animation, forKey: "Load")
    
        return loader
    }
    

If you've already set UIUserInterfaceStyle as Light on your app's Info.plist to opt out of dark mode entirely, then you can ignore this property.

#### Preferred language

The CCAI Platform SDK will use the following priority order to determine the preferred language.

  1. Language selected from the splash screen within the app.

  2. Default language selected from `UJETGlobalOptions`. You can set the default language with `preferredLanguage` property. The supported language codes can be found in the `UJETGlobalOptions.h` file.

  3. Device language selected in the device (from **Settings > General > Language & Region**) will be used, when it is supported by the app.

  4. Closest dialect of device language will be used when the application does not support the device language but supports its closest parent dialect. For example, if the user selected Spanish Cuba as the language in the device and the app does not support Spanish Cuba but supports parent dialect Spanish, then Spanish language will be used.

  5. English will be used if the device language is not supported by the app.




#### Configure external deflection link icons

You can customize the icon in the external deflection link channel by uploading icon into asset catalog of your app and ensure to use the same icon name while creating external deflection link in Settings > Chat > External Deflection Links > View links > Add Deflection Link in the Admin Portal. If the icon name in the Admin Portal does not match with the icon uploaded into the app then the SDK will use the default icon. You can refer to this [link on how](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AddingImages.html) to add images on asset catalog.

### Send custom data to your CRM

You can send custom data to the CRM ticket.

There are two methods to send custom data:

  1. Secure method: predefined data signing with JWT.

  2. Non-secure method: predefined data with plain JSON (Not recommended).




#### Using the secure method to send custom data

You have to implement signing method. First, you can put your custom data on client side, and send to your server to sign it. On your server you can add additional data by defined form and sign with your company.secret and return it by JWT.
    
    
    - (void)signPayload:(NSDictionary *)payload payloadType:(UjetPayloadType)payloadType success:(void (^)(NSString *))success failure:(void (^)(NSError *))failure
    {
        if (payloadType == UjetPayloadCustomData) {
          // sign custom data using UJET_COMPANY_SECRET on your server.
    
          NSURLSessionConfiguration *sessionConfiguration = [NSURLSessionConfiguration defaultSessionConfiguration];
          NSURLSession *session = [NSURLSession sessionWithConfiguration:sessionConfiguration];
    
          NSMutableURLRequest *mutableRequest = [[NSMutableURLRequest alloc] init];
          mutableRequest.URL = [NSURL URLWithString:@"https://your.company.com/api/ujet/sign/custom_data"];
          mutableRequest.HTTPMethod = @"POST";
          NSError *error;
    
          // Make client's custom data
          UJETCustomData *customData = [[UJETCustomData alloc] init];
          [customData set:@"name" label:@"Name" stringValue:@"USER_NAME"];
          [customData set:@"os_version" label:@"OS Version" stringValue:[[UIDevice currentDevice] systemVersion]];
          [customData set:@"model" label:@"Model number" numberValue:[NSNumber numberWithInteger:1234]];
          [customData set:@"temperature" label:@"Temperature" numberValue:[NSNumber numberWithFloat:70.5]];
          [customData set:@"purchase_date" label:@"Purchase Date" dateValue:[NSDate date]];
          [customData set:@"dashboard_url" label:@"Dashboard" urlValue:[NSURL URLWithString:@"http://internal.dashboard.com/1234"]];
    
          NSDictionary *data = @{@"custom_data": [customData getData]};
          mutableRequest.HTTPBody = [NSJSONSerialization dataWithJSONObject:data options:0 error:&error];
          NSURLSessionDataTask *task = [session dataTaskWithRequest:mutableRequest completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
              if(error) {
                  failure(error);
              }
              else {
                  NSDictionary *json = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
                  success(json[@"jwt"]);
              }
          }];
    
          [task resume];
        }
    }
    

#### Using insecure method to send custom data

This method is not recommended as it creates a potential vulnerability which could open your application to a man-in-the-middle attack. If you choose to use this method, we are not responsible for the security exposure and potential damage which may occur. We encourage you to use the secure method previously described to send custom data in your application. Or you can just start the iOS SDK with `UJETCustomData` instance. In this case, `signPayload` delegate for `UJETPayloadCustomData` should just call success(nil);.
    
    
    - (void)signPayload:(NSDictionary *)payload payloadType:(UjetPayloadType)payloadType success:(void (^)(NSString *))success failure:(void (^)(NSError *))failure {
        if (payloadType == UjetPayloadCustomData) {
          success(nil);
        }
    }
    UJETStartOptions *options = [UJETStartOptions new];
    options.unsignedCustomData = customData;
    
    [UJET startWithOptions:options];
    

#### Using unsigned custom data to send external chat transcript

You can send the chat transcript to the SDK when it's started with unsigned custom data by calling setExternalChatTransfer: or setExternalChatTransferWithDictionary: method to set JSON data with NSString or NSDictionary, respectively.
    
    
    UJETCustomData *customData = [UJETCustomData new];
    [customData setExternalChatTransfer:jsonString];
    
    UJETStartOptions *options = [UJETStartOptions new];
    options.unsignedCustomData = customData;
    
    [UJET startWithOptions:options];
    

JSON format:

  * `greeting_override`: string

  * `agent`: dictionary

    * `name`: string

    * `avatar`: string [URL of agent avatar, optional]

  * `transcript`: array

    * `sender`: string [`end_user` or `agent`]

    * `timestamp`: string [for example, `2021-03-15 12:00:00Z`]

    * `content`: array

      * `type`: string [one of `text`, `media`]

      * `text`: string [required for text type]

      * `media`: dictionary [required for media type]

        * `type`: string [one of image, video]

        * `url`: string [public URL pointing at media file]




JSON example:
    
    
    {
      "greeting_override": "Please hold while we connect you with a human agent.",
      "agent": {
        "name": "Name",
        "avatar": "avatar url"
      },
      "transcript": [
        {
          "sender": "agent",
          "timestamp": "2021-03-15 12:00:15Z",
          "content": [
            {
              "type": "text",
              "text": "**Suggestions shown:**\n\n* Help with batch or delivery\n* Help with metrics or order feedback\n* Help with Instant Cashout"
            }
          ]
        },
        {
          "sender": "end_user",
          "timestamp": "2021-03-15 12:00:16Z",
          "content": [
            {
              "type": "text",
              "text": "Help with batch or delivery"
            }
          ]
        }
      ]
    }
    

You can use Markdown on the text type. Supported syntax include italic, bold, bullet list, hyperlink, and underline (`--text--`).

#### Example of custom data

##### JSON encoded to JWT

The JSON file should validate JWT. And the object of custom data is value of custom_data key.
    
    
    {
      "iat" : 1537399656,
      "exp" : 1537400256,
      "custom_data" : {
        "location" : {
          "label" : "Location",
          "value" : "1000 Stockton St, San Francisco, CA, United States",
          "type" : "string"
        },
        "dashboard_url" : {
          "label" : "Dashboard URL",
          "value" : "http://(company_name)/dashboard/device_user_ID",
          "type" : "url"
        },
        "contact_date" : {
          "label" : "Contact Date",
          "value" : 1537399655992,
          "type" : "date"
        },
        "membership_number" : {
          "label" : "Membership Number",
          "value" : 62303,
          "type" : "number"
        },
        "model" : {
          "label" : "Model",
          "value" : "iPhone",
          "type" : "string"
        },
        "os_version" : {
          "label" : "OS Version",
          "value" : "12.0",
          "type" : "string"
        },
        "last_transaction_id" : {
          "label" : "Last Transaction ID",
          "value" : "243324DE-01A1-4F71-BABC-3572B77AC487",
          "type" : "string"
        },
        "battery" : {
          "label" : "Battery",
          "value" : "-100%",
          "type" : "string"
        },
        "bluetooth" : {
          "label" : "Bluetooth",
          "value" : "Bluetooth not supported",
          "type" : "string"
        },
        "wifi" : {
          "label" : "Wi-Fi",
          "value" : "Wi-Fi not connected",
          "type" : "string"
        },
        "ssn" : {
          "invisible_to_agent" : true,
          "label" : "Social Security Number",
          "value" : "102-186-1837",
          "type" : "string"
        }
      }
    }
    

Each data is similar to JSON object format and should contain the key, value, type, and label.

The key is unique identifier for the data. label is display name on CRM's page type is type of the value.

  * string

    * JSON string
  * number

    * integer, float
  * date

    * UTC Unix timestamp format with 13 digits. (contains milliseconds)
  * URL

    * HTTP URL format



##### CRM example

Here's a CRM example.

##### Location

Use CoreLocation framework. For more details please refer to `AppDelegate.m`.

##### Device OS Version
    
    
    [customData set:@"os_version" label:@"OS Version" stringValue:[[UIDevice currentDevice] systemVersion]];
    

#### Prevent the display of custom data

You can use the `invisible_to_agent` property with a custom data object to prevent signed or unsigned custom data from being displayed in the agent adapter. In the previous example, the end-user's social security number is not shown in the agent adapter because `"invisible_to_agent" : true` is included in the `ssn` object.

**Note:** The `invisible_to_agent` property does not prevent [reserved data properties](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#reserved-data-properties-ios-sdk) from displaying in the agent adapter. 

When you include the `"invisible_to_agent" : true` property with a custom data object, you can expect the following behavior:

  * The custom data is included in the [session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata).
  * The custom data is not included in CRM records.



For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter).

### Reserved data properties

You can send reserved data properties to Contact Center AI Platform (CCAI Platform) as signed custom data when a session begins. For more information, see [Send reserved data properties](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties).

The following is an example of reserved data properties in custom data:
    
    
      {
        "custom_data": {
          "reserved_verified_customer": {
            "label": "Verified Customer",
            "value": "VERIFIED_CUSTOMER_BOOLEAN": ,
            "type": "boolean"
          },
          "reserved_bad_actor": {
            "label": "Bad Actor",
            "value": "VERIFIED_BAD_ACTOR_BOOLEAN": ,
            "type": "boolean"
          },
          "reserved_repeat_customer": {
            "label": "Repeat Customer",
            "value": "REPEAT_CUSTOMER_BOOLEAN": ,
            "type": "boolean"
          }
        }
      }
      

Replace the following:

  * `VERIFIED_CUSTOMER_BOOLEAN`: True if you consider this end-user to be a legitimate customer.
  * `VERIFIED_BAD_ACTOR_BOOLEAN`: True if you consider this end-user to potentially be a bad actor.
  * `REPEAT_CUSTOMER_BOOLEAN`: True if you have determined that this end-user has contacted your contact center before.



### Customize Flow

#### Disconnect CCAI Platform for handling Host app events
    
    
    // CCAI Platform is connected
    ...
    // An event has come
    [UJET disconnect:^{
      // Handle an event
    }];
    

#### Postpone CCAI Platform incoming call or chat

##### Implement a delegate method for handling incoming events
    
    
    - (BOOL)shouldConnectUjetIncoming:(NSString *)identifier forType:(UjetIncomingType)type {
      if (weDoingSomething) {
        // save identifier and type
        return NO; // postpone
      } else {
        return YES;
      }
    }
    

##### Connect postponed event
    
    
    [UJET connect:identifier forType:UjetIncomingTypeCall];
    

### Setup Deep link

This enables agents on PSTN calls to use smart actions by SMS for both when an end user has or does not have the app.

Go to **Settings > Operation Management > Enable Send SMS to Download App** in the CCAI Platform portal.

You can set App URL with your web page (i.e, <https://your-company.com/support>) after configuring [Universal Link](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html) or [custom URL scheme](https://developer.apple.com/documentation/uikit/core_app/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app?language=objc). You can select either way.

#### Implement delegate method to handle deep link

The universal link and custom URL look like `https://your-company.com/support?call_id=x&nonce=y` and `your-company://support?call_id=x&nonce=y` respectively. Put one of your links without query parameters under App URL in Admin Portal. For example, put `your-company://support` if using a custom URL scheme.

In the delegate method, make sure to only call `[UJET start]` when the URL paths and parameters in the universal link or custom URL are specific for CCAI Platform.
    
    
    - (BOOL)application:(UIApplication *)app continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray * _Nullable))restorationHandler {
      ...
      if ([NSUserActivityTypeBrowsingWeb isEqualToString:userActivity.activityType]) {
        NSURL *url = userActivity.webpageURL;
    
        NSArray *availableSchema = @[
                                      @"your-company",   // custom URL scheme
                                      @"https"           // universal link
                                      ];
    
        NSArray *availableHostAndPath = @[
                                          @"ujet",                  // custom URL scheme
                                          @"your-comany.com/ujet"   // universal link
                                          ];
    
        if (![availableSchema containsObject:url.scheme]) {
          return NO;
        }
    
        NSString *hostAndPath = [NSString stringWithFormat:@"%@%@", url.host, url.path];
        if (![availableHostAndPath containsObject:hostAndPath]) {
          return NO;
        }
    
        // your-company://ujet?call_id={call_id}&nonce={nonce}
        // https://your-company.com/ujet?call_id={call_id}&nonce={nonce}
        NSURLComponents *urlComponents = [NSURLComponents componentsWithURL:url
                                                    resolvingAgainstBaseURL:NO];
        NSArray *queryItems = urlComponents.queryItems;
        NSString *callId = [self valueForKey:@"call_id" fromQueryItems:queryItems];
        // validate call id
        if (![self isValidCallId:callId]) {
          return NO;
        }
        NSString *nonce = [self valueForKey:@"nonce" fromQueryItems:queryItems];
    
        UJETStartOptions *options = [[UJETStartOptions alloc] initWithCallId:callId nonce:nonce];
    
        [UJET startWithOptions:options];
      }
      ...
    }
    

If your app adopts `UIWindowSceneDelegate`, then add this code snippet:
    
    
    class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
        var window: UIWindow?
    
        func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    
            //if app is called with universal Link and started from cold
            if connectionOptions.urlContexts.first != nil  {
                self.scene(scene, openURLContexts: connectionOptions.urlContexts)
            }
    
            guard let _ = (scene as? UIWindowScene) else { return }
        }
    
        func scene(_ scene: UIScene, willContinueUserActivityWithType userActivityType: String) {
            guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else { return }
            let _ = appDelegate.application(UIApplication.shared,
                                            continue: NSUserActivity(activityType: userActivityType)) { _ in
    
            }
        }
    
        func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
            guard let url = URLContexts.first?.url else {
                return
            }
    
            guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else { return }
            let _ = appDelegate.application(UIApplication.shared,
                                            open: url,
                                            options: [:])
        }
    }
    

For more information, see the example codes from `UJETObject+DeepLink` file.

### Observe CCAI Platform event

We post the following events through NSNotificationCenter.defaultCenter. You can listen to them and customize your flow depending on your use case, e.g., custom keyboard layout.

  * UJETEventEmailDidClick

    * _Queue Menu Data_
  * UJETEventEmailDidSubmit

    * _Queue Menu Data_

    * has_attachment: (NSNumber) @YES, @NO

  * UJETEventSessionViewDidAppear

    * type: @"call", @"chat"

    * timestamp: (NSString) ISO 8601

  * UJETEventSessionViewDidDisappear

    * type: @"call", @"chat"

    * timestamp: (NSString) ISO 8601

  * UJETEventSessionDidCreate

    * _Session Data_
  * UJETEventSessionDidEnd

    * _Session Data_

    * agent_name: (NSString) null if agent didn't join

    * duration: (NSNumber) only for call

    * ended_by: (NSString)

      * type=call: @"agent", @"end_user"

      * type=chat: @"agent", @"end_user", @"timeout", @"dismissed"

  * UJETEventSdkDidTerminate

  * UJETEventPostSessionOptInDidSelected

    * opt_in_selected: (NSString) @"Yes", @"No"



#### Event Data

**Metadata**

  * application: @"iOS"

  * app_id: (NSString) bundle identifier

  * app_version: (NSString)

  * company: (NSString) subdomain

  * device_model: (NSString)

  * device_version: (NSString)

  * sdk_version: (NSString)

  * timestamp: (NSString) ISO 8601




#### Queue Menu Data

**Metadata**

  * menu_id: NSString

  * menu_key: NSString, nullable

  * menu_name: NSString

  * menu_path : NSString




#### Session Data

**Metadata**

  * session_id: NSString

  * type: @"call", @"chat"

  * end_user_identifier: NSString




### Setup Screen Share

If you want to use Screen Share feature, then integrate `UJETCobrowseKit.xcframework`.

**CocoaPods:** Add the following subspec to your app target.
    
    
        ruby
    target 'MyApp' do
      pod 'UJET'
      pod 'UJET/Cobrowse'
    end
    

**Carthage:** Add the following line on the Cartfile:
    
    
    binary "https://sdk.ujet.co/ios/UJETKit.json"
    

**SwiftPM:** Select `UJET` and `UJETCobrowse` products and add to your app target.

And set `UJETGlobalOptions.cobrowseKey` property.
    
    
    swift
    let options = UJETGlobalOptions()
    options.cobrowseKey = cobrowseKey
    
    UJET.setGlobalOptions(options)
    

#### Full device Screen Sharing (optional)

Full device screen sharing allows your support agents to view screens from applications outside of your own. This is often useful where support agents need to check the state of system settings, or need to see the user navigate between multiple applications. If you don't want this feature, you may skip this section.

#### Customize the Screen Share consent dialog

To customize the Screen Share consent dialog, you need to implement the `UJETCobrowseAlertProvider` protocol in your provider class. In this implementation, return a custom `UIViewController` or any other object inherited `UIViewController` through the respective protocol method. `UIViewController` should have two buttons, one is for accept, the other is for deny.

After getting the consent, pass into our SDK by calling the closure `consentStatus`. `UIViewController` from `cobrowseFullDeviceRequestAlert`. The delegate should contain the `RPSystemBroadcastPickerView` with title (see in sample code below) and should have another deny button. Invoke the dismissed closure on click of the deny button.
    
    
    class CobrowseAlertProvider: NSObject, UJETCobrowseAlertProvider {
        func cobrowseSessionInitializationAlert(consentStatus: @escaping (Bool) -> Void) -> UIViewController? {
            let customAlertViewController = CustomAlertViewController()
            customAlertViewController.consentStatus = consentStatus
            return customAlertViewController
        }
    
        func cobrowseSessionRequestAlert(consentStatus: @escaping (Bool) -> Void) -> UIViewController? {
            // Same as cobrowseSessionInitializationAlert
        }
    
        func cobrowseRemoteRequestAlert(consentStatus: @escaping (Bool) -> Void) -> UIViewController? {
            // Same as cobrowseSessionInitializationAlert
        }
    
        func cobrowseFullDeviceRequestAlert(dismissed: @escaping () -> Void) -> UIViewController? {
            let customAlertViewController = CustomFullDeviceAlertViewController()
            cobrowseSessionAlertViewController.dismissed = dismissed
            return customAlertViewController
        }
    
        func cobrowseSessionEndAlert(consentStatus: @escaping (Bool) -> Void) -> UIViewController? {
            // Same as cobrowseSessionInitializationAlert
        }
    }
    

The custom view controller should have a closure to pass the consent status to the SDK.
    
    
    class CustomAlertViewController: UIViewController {
        var consentStatus: ((Bool) -> Void)?
    
        @IBAction func allowButtonClicked(_ sender: Any) {
            dismiss(animated: true) {[weak self] in
                self?.consentStatus?(true)
            }
        }
    
        @IBAction func denyButtonClicked(_ sender: Any) {
            dismiss(animated: true) {[weak self] in
                self?.consentStatus?(false)
            }
        }
    }
    

The custom view controller for full device request alert should have `RPSystemBroadcastPickerView` and a closure to pass the `dismiss` status to the SDK.
    
    
    class CustomFullDeviceAlertViewController: UIViewController {
        var broadcastPickerView: RPSystemBroadcastPickerView!
        var dismissed: (() -> Void)?
    
        override func viewDidLoad() {
            super.viewDidLoad()
    
            let frame = CGRect(x: x, y: y, width: 50, height: 50) // Set your own value
            broadcastPickerView = RPSystemBroadcastPickerView(frame: frame)
            broadcastPickerView.preferredExtension = Bundle.main.object(forInfoDictionaryKey: "CBIOBroadcastExtension") as? String // Should have this value as it is
            view.addSubview(broadcastPickerView)
        }
    
        @IBAction func denyButtonClicked(_ sender: Any) {
            dismiss(animated: true) {[weak self] in
                self?.dismissed?()
            }
        }
    }
    

Don't forget to pass this provider to our SDK through the following API:
    
    
    let provider = CobrowseAlertProvider()
    UJET.setCobrowseAlertProvider(provider)
    

#### Broadcast Extension

The feature requires adding a Broadcast Extension.

  1. Open your Xcode project.

  2. Navigate to **File > Target**.

  3. Pick **Broadcast Upload Extension**.

  4. Enter a **Name** for the target.

  5. Uncheck **Include UI Extension**.

  6. Create the target, noting its **bundle ID**.

  7. Change the target SDK of your Broadcast Extension to _iOS 12.0_ or higher.




#### Integrate the SDK

**CocoaPods:** Add the following subspec to your extension target:
    
    
    target 'MyApp' do
      pod 'UJET'
      pod 'UJET/Cobrowse'
    end
    target 'MyAppExtension' do
      pod 'UJET/CobrowseExtension'
    end
    

If you're using SwiftPM, select `UJETCobrowseExtension` product and add to your extension target.

#### Set up keychain sharing

Your app and the app extension that you previously created need to share some secrets through the iOS Keychain. They do this using their own Keychain group so they are isolated from the rest of your apps Keychain.

In **both** your **app target** and your **extension target** add a Keychain Sharing entitlement for the `io.cobrowse` keychain group.

#### Add the bundle ID to your plist

Take the **bundle ID** of the **extension** you previously created and add the following entry in your apps Info.plist (Note: **not** in the extensions Info.plist), replacing the following **bundle ID** with your own:
    
    
    xml
    <key>CBIOBroadcastExtension</key>
    <string>your.app.extension.bundle.ID.here</string>
    

#### Implement the extension

Xcode will have added `SampleHandler.m` and `SampleHandler.h` (or `SampleHander.swift`) files as part of the target you created earlier. Replace the content of the files with the following:

**Swift:** Select `UJETCobrowseExtension` product and add to your extension target:
    
    
    import CobrowseIOAppExtension
    class SampleHandler: CobrowseIOReplayKitExtension {
    }
    

**ObjC**
    
    
    objc// SampleHandler.h
    @import CobrowseIOAppExtension;
    @interface SampleHandler : CobrowseIOReplayKitExtension
    @end// SampleHandler.m
    #import "SampleHandler.h"
    @implementation SampleHandler
    @end
    

#### Build and run your app

You're now ready to build and run your app. The full device capability is only available on physical devices, it won't work in the iOS Simulator.

### Minimize the SDK

The Contact Center AI Platform SDK can be minimized when a chat session or a call is ongoing. This can be useful when you want to drive the user back to your app after an SDK event has been received such as a content card clicked. To minimize the SDK and drive user back to your app you can use:
    
    
    UJET.minimize(nil)
     // Or if you want to take some action once the SDK has been minimized:
    
    UJET.minimize {
      // Add the code you want to run once the SDK has been minimized here
    }
    

### Fallback

You can use the `didHandleUjetError` function for the fallback of unexpected errors. If you don't use this function or it returns `false`, the iOS SDK handles the error.

The following table shows the errors that the `didHandleUjetError` function listens for:

Error type | Error code | Description  
---|---|---  
`networkError` | 1 | The network isn't available.**Note:** This error isn't triggered when the network isn't available during a chat or call session or a rate screen.  
`authenticationError` | 100 | An unexpected error occurred during authentication.  
`authenticationJwtError` | 101 | An unexpected error occurred during JWT validation—for example, a parsing error.  
`voipConnectionError` | 1000 | Failed to establish a connection to the VoIP provider. A VoIP SDK callback handles this.  
`voipLibraryNotFound` | 1001 | The system expects a call to connect through a VoIP provider but cannot find one. This can happen if you integrate the wrong SDK or don't add a VoIP provider library to your dependencies.  
`chatLibraryNotFound` | 1100 | Occurs when the system can't find the chat library. This can happen when you integrate the wrong SDK or didn't add a Twilio chat library to your dependencies.  
  
The following code sample shows how to use the `didHandleUjetError` function:
    
    
    public func didHandleUjetError(_ errorCode: Int32) -> Bool {
        guard let ujetError = UjetErrorCode(rawValue: Int(errorCode)) else {
            return false // Let the SDK handle unknown integer codes.
        }
    
        switch ujetError {
        case .networkError:
            // Example for if you have a custom UI for network errors. You can
            // handle the error and prevent the SDK from showing its own alert.
            showCustomNetworkAlert() // Your custom UI for this type of error.
            return true
    
        case .authenticationError, .voipConnectionError:
            // For all other errors, use the default SDK behavior.
            return false
    
        @unknown default:
            // Let the SDK handle future errors.
            return false
        }
    }
    

## Troubleshooting

### App submission rejection

App submission is rejected due to the inclusion of CallKit framework in China territory.

If your app is rejected by Apple for this reason, then just leave a comment as the system is designed to deactivate the CallKit framework for China region on VoIP call. This is effective as of SDK version 0.31.1.

### SDK size is too large

**When SDK size is too large and hard to track on GitHub**

In this [article](https://help.github.com/articles/distributing-large-binaries/), they offer two choices. It is recommended to use Git lfs.

If you are not using [Bitcode](https://help.apple.com/xcode/mac/current/#/devbbdc5ce4f) then stripping bitcode from binary can be an another option. Run this command under UJETKit.xcframework folder.
    
    
    xcrun bitcode_strip -r UJET -o UJET
    

### dyld: Library not loaded error

Add @executable_path/Frameworks on the Runpath Search Paths from **Target > Build Settings > Linking**.

### App submission on iTunes Connect

Apple might ask the following question while in review process because of enabled Voice over IP background mode:

Can users receive VoIP calls in your app?

Respond **Yes** to the question.

### Alert Notification is _unavailable_ when starting SDK

Check the following:

  * Use real device not simulator.

  * Enable Push notifications and **Background Modes > Voice over IP capability**.




If those things don't help, then try to build with distribution provisioning profile (Ad-hoc or Apple Store).

### Test push notification against your test app

Prepare your VoIP certificate and device's device token.

On CCAI Platform portal, refer to the **Push Notification Debug** section in **Settings > Developer Settings** menu.

If you have already set the certificate for APNS, you don't have to put your certificate again.

Input your certificate (optional) and check whether sandbox or not (optional) and input your test app push notification device token.

### Starting a new chat took longer than 30 seconds

Check if you are responding to a delegate method of custom data. You should return a valid custom data upon request or just return nil on the success block.

Use this code snippet as an example configuration:
    
    
    public func signPayload(_ payload: [AnyHashable: Any]?, payloadType: UjetPayloadType, success: (String?) -> Void, failure: (Error?) -> Void)
    {
        if payloadType == .customData {
            success(nil)
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
