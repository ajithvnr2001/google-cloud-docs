---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-flutter/
title: Flutter for iOS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:07.730343+00:00
---

# Flutter for iOS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-flutter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Flutter for iOS Stay organized with collections  Save and categorize content based on your preferences. 

You can set up mobile apps to work with Contact Center AI Platform (CCAI Platform) in a number of ways, including with Flutter. This page shows you how to integrate the iOS SDK into an iOS app using Flutter.

## Before you begin

Before you following the instructions on this page, you must first follow the instruction in [Integrate using Flutter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview#integrate-using-flutter).

## Integrate the SDK using CocoaPods

To integrate the SDK using CocoaPods, follow these steps:

  1. Open `Podfile` and add dependencies to the target, as in the following code sample:
         
         UJETPodspec = { :podspec => 'https://sdk.ujet.co/ios/UJET.podspec' }
         
         pod 'UJET', UJETPodspec
         pod 'UJET/Cobrowse', UJETPodspec
         

  2. In the terminal, go to the `example/ios` directory and run the `pod install` command to install dependencies.




## Set up iOS push notifications

To set up iOS push notifications, follow these steps:

  1. In XCode, open `example/ios/Runner.xcodeproj`.

  2. Add the following code to your `AppDelegate.swift` file:
         
         import PushKit
         import UJETKit
         
         @UIApplicationMain
         @objc class AppDelegate: FlutterAppDelegate {
         override func application(
             _ application: UIApplication,
             didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
         ) -> Bool {
             // Register Flutter Plugins
             GeneratedPluginRegistrant.register(with: self)
             UJETModule.register(with: self.registrar(forPlugin: "UjetModule")!)
             UJETModule.onInitDone = {
                 // setup push notification
                 let voipRegistry = PKPushRegistry(queue: DispatchQueue.main)
                 voipRegistry.desiredPushTypes = Set([PKPushType.voIP])
                 voipRegistry.delegate = self
                 UNUserNotificationCenter.current().delegate = self
             }
             return super.application(application, didFinishLaunchingWithOptions: launchOptions)
         }
         }
         
         // Extension for Push Notification
         
         extension AppDelegate {
             func tokenFromData(data: Data) -> String {
                 return data.map { String(format: "%02x", $0) }.joined()
             }
         
             override func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
                 print("apns token: ", tokenFromData(data: deviceToken))
         
                 UJET.updatePushToken(deviceToken, type: .APN)
             }
         
             override func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
                 UJET.updatePushToken(nil, type: .APN)
             }
         
             override func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
                 handleNotification(userInfo: userInfo, completion: nil)
             }
         }
         
         // MARK: PushKit
         
         extension AppDelegate: PKPushRegistryDelegate {
             func pushRegistry(_ registry: PKPushRegistry, didUpdate credentials: PKPushCredentials, for type: PKPushType) {
                 print("voip token: ", tokenFromData(data: credentials.token))
         
                 if type == .voIP {
                     UJET.updatePushToken(credentials.token, type: .voIP)
                 }
             }
         
             func pushRegistry(_ registry: PKPushRegistry, didInvalidatePushTokenFor type: PKPushType) {
                 if type == .voIP {
                     UJET.updatePushToken(nil, type: .voIP)
                 }
             }
         
             func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType, completion: @escaping () -> Void) {
                 if type == .voIP {
                     handleNotification(userInfo: payload.dictionaryPayload, completion: completion)
                 }
             }
         }
         
         extension AppDelegate {
         // handle push received in foreground state
         override func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
             let userInfo = notification.request.content.userInfo
             handleNotification(userInfo: userInfo, completion: nil)
         }
         
         // handle push received and tapped in background state
         override func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
             let userInfo = response.notification.request.content.userInfo
             handleNotification(userInfo: userInfo, completion: nil)
         }
         }
         
         private func handleNotification(userInfo: [AnyHashable: Any], completion: (() -> Void)?) {
             if userInfo["ujet"] != nil {
                 UJET.receivedNotification(userInfo, completion: completion)
             } else {
                 // Handle your notification here
                 completion?()
             }
         }
         

  3. Select your `.xcodeproj` and then your app target. Add `PushKit.framework` in the `Frameworks, Libraries, and Embedded Content` section.




## Set up deep linking

To set up deep linking, add the following code:
    
    
    // Extension for deep linking
    
    extension AppDelegate {
        override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
            print("Open app with url: \(url.absoluteString)")
    
            return self.handleRouting(url)
        }
    
        override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
            // Universal links
            if NSUserActivityTypeBrowsingWeb == userActivity.activityType {
                return self.handleRouting(userActivity.webpageURL!)
            } else if userActivity.activityType == "INStartAudioCallIntent" {
                // Open app from Call history
                UJET.start(with: UJETStartOptions())
    
                return true
            }
            return false
        }
    
        func handleRouting(_ url: URL) -> Bool {
            let availableSchema = [
                "ujetrn", // TODO: Change to your custom URL scheme. Config from Portal > Developer Settings > Mobile App > Enable Send SMS to Download App > iOS App > URL
                "https" // universal link
            ]
            let availableHostAndPath = [
                "call",         // custom URL scheme
                "ujet.cx/app"  // universal link,
            ]
    
            if !(availableSchema.contains(url.scheme ?? "")) {
                return false
            }
    
            let hostAndPath = String.init(format: "%@%@", url.host ?? "", url.path)
            if !(availableHostAndPath.contains(hostAndPath)) {
                return false
            }
    
            // ujet://call?call_id={call_id}&nonce={nonce}
            // https://ujet.co/app?call_id={call_id}&nonce={nonce}
            let urlComponents: URLComponents? = URLComponents(url: url, resolvingAgainstBaseURL: false)
            let queryItems = urlComponents?.queryItems
            let callId = value(forKey: "call_id", fromQueryItems: queryItems)
    
            // validate call ID
            if !isValidCallId(callId) {
                return false
            }
    
            guard let nonce = value(forKey: "nonce", fromQueryItems: queryItems) else {
                return false
            }
    
            let options = UJETStartOptions.init(callId: callId!, nonce: nonce)
    
            UJET.start(with: options)
    
            return true
        }
    
        func value(forKey key: String?, fromQueryItems queryItems: [URLQueryItem]?) -> String? {
            let predicate = NSPredicate(format: "name=%@", key ?? "")
            let filtered = (queryItems as NSArray?)?.filtered(using: predicate) as? [URLQueryItem]
            let queryItem: URLQueryItem? = filtered?.first
    
            return queryItem?.value
        }
    
        func isValidCallId(_ callId: String?) -> Bool {
            if (callId ?? "").isEmpty {
                return false
            }
    
            let nonNumbers = CharacterSet.decimalDigits.inverted
            let r = callId?.rangeOfCharacter(from: nonNumbers)
    
            return r == nil
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
