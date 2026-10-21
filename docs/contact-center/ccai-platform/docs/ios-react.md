---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-react/
title: React Native for iOS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:32:17.661439+00:00
---

# React Native for iOS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-react/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  React Native for iOS Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides integration with mobile applications using a number of methods including React. This document explains how to integrate React Native for iOS.

Before following these Android-specific instructions, complete the instructions at [React Native for Mobile SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview#mobile-sdk-react).

## Integrate SDK using CocoaPods

  1. To integrate the mobile SD using CocoaPods, open Podfile and add the following dependencies to the target:
         
         UJETPodspec = { :podspec => 'https://sdk.ujet.co/ios/UJET.podspec' }
         
         pod 'UJET', UJETPodspec
         pod 'UJET/Cobrowse', UJETPodspec
         

  2. Install dependencies by running the command `pod-install`from the ios folder or npx pod-install from the app folder.




## Set up push notifications

To set up push notifications to the mobile SDK, follow these steps:

  1. Open Xcode project.

  2. Open the file which conforms to `RCTAppDelegate` and add the following code:
         
         #import <UJETKit/UJETKit.h>
         #import <PushKit/PushKit.h>
         
         @interface AppDelegate() <PKPushRegistryDelegate>
         @end
         
         - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
         {
           PKPushRegistry *voipRegistry = [[PKPushRegistry alloc] initWithQueue: dispatch_get_main_queue()];
           voipRegistry.delegate = self;
           voipRegistry.desiredPushTypes = [NSSet setWithObject:PKPushTypeVoIP];
         }
         
         #pragma mark PushKit
         
         - (NSString *)tokenFromData:(NSData *)data {
             const void *bytes = [data bytes];
             const unsigned char *d = (const unsigned char *)bytes;
             NSMutableString *token = [NSMutableString string];
         
             for (NSUInteger i = 0; i < [data length]; ++i) {
                 [token appendFormat:@"%02X", d[i]];
             }
         
             return [token lowercaseString];
         }
         
         - (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(PKPushType)type {
           NSLog(@"voip token: %@", [self tokenFromData:credentials.token]);
         
           if ([type isEqual:PKPushTypeVoIP]) {
             [UJET updatePushToken:credentials.token type:UjetPushTypeVoIP];
         
           }
         }
         
         - (void)pushRegistry:(PKPushRegistry *)registry didInvalidatePushTokenForType:(PKPushType)type {
           if ([type isEqual:PKPushTypeVoIP]) {
             [UJET updatePushToken:nil type:UjetPushTypeVoIP];
           }
         }
         
         - (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(PKPushType)type withCompletionHandler:(void (^)(void))completion {
           if ([type isEqual:PKPushTypeVoIP] && payload.dictionaryPayload[@"ujet"]) {
             [UJET receivedNotification:payload.dictionaryPayload completion:completion];
           } else {
             completion();
           }
         }
         
         #pragma mark APNS
         
         - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
           NSLog(@"apns token: %@", [self tokenFromData:deviceToken]);
         
           [UJET updatePushToken:deviceToken type:UjetPushTypeAPN];
         }
         
         - (void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(nonnull NSError *)error {
           [UJET updatePushToken:nil type:UjetPushTypeAPN];
         }
         
         - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
           if (userInfo[@"ujet"]) {
             [UJET receivedNotification:userInfo completion:nil];
           } else {
             // handle your notifications
           }
         }
         

For Swift:
         
         import UJETKit
         import PushKit
         
         func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
             let voipRegistry = PKPushRegistry(queue: DispatchQueue.main)
             voipRegistry.desiredPushTypes = Set([PKPushType.voIP])
             voipRegistry.delegate = self
         }
         
         // MARK: Push Notifications
         
         extension AppDelegate {
             func tokenFromData(data: Data) -> String {
                 return data.map { String(format: "%02x", $0) }.joined()
             }
         
             func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
                 print("apns token: ", tokenFromData(data: deviceToken))
         
                 UJET.updatePushToken(deviceToken, type: .APN)
             }
         
             func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
                 UJET.updatePushToken(nil, type: .APN)
             }
         
             func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
                 if userInfo["ujet"] != nil {
                     UJET.receivedNotification(userInfo, completion: nil)
                 } else {
                     // handle your notifications
                 }
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
                 if type == .voIP && payload.dictionaryPayload["ujet"] != nil {
                     UJET.receivedNotification(payload.dictionaryPayload, completion: completion)
                 } else {
                     completion()
                 }
             }
         }
         

  3. Select your .xcodeproj and then your app target. Add PushKit.framework on the Frameworks, Libraries, and Embedded Content section.




## Set up deep links

To provide support for deep links within your mobile application, use the following code:
    
    
      #pragma mark Deep Link
    
      - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
        if ([url.scheme isEqualToString:@"ujet"]) {
          return [self handleRouting:url];
        }
    
        return NO;
      }
    
      - (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void(^)(NSArray<id<UIUserActivityRestoring>> * __nullable restorableObjects))restorationHandler {
        // Universal links
        if ([NSUserActivityTypeBrowsingWeb isEqualToString:userActivity.activityType]) {
          return [self handleRouting:userActivity.webpageURL];
    
        } else if ([userActivity.activityType isEqualToString:@"INStartAudioCallIntent"]) {
          // Open app from Call history
          [UJET startWithOptions:nil];
    
          return YES;
        }
    
        return NO;
      }
    
      - (BOOL)handleRouting:(NSURL *)url {
        NSArray *availableSchema = @[
          @"ujetrn", // TODO: Change to your custom URL scheme. Config from Portal > Developer Settings > Mobile App > Enable Send SMS to Download App > iOS App > URL
          @"https"   // TODO: or your universal link
        ];
        NSArray *availableHostAndPath = @[
          @"call",          // custom URL scheme
          @"ujet.cx/app"    // universal link
        ];
    
        if (![availableSchema containsObject:url.scheme]) {
          return NO;
        }
    
        NSString *hostAndPath = [NSString stringWithFormat:@"%@%@", url.host, url.path];
        if (![availableHostAndPath containsObject:hostAndPath]) {
          return NO;
        }
    
        // ujetrn://call?call_id={call_id}&nonce={nonce}
        // https://ujet.co/app?call_id={call_id}&nonce={nonce}
        NSURLComponents *urlComponents = [NSURLComponents componentsWithURL:url
                                                    resolvingAgainstBaseURL:NO];
        NSArray *queryItems = urlComponents.queryItems;
        NSString *callId = [self valueForKey:@"call_id" fromQueryItems:queryItems];
        // validate call ID
        if (![self isValidCallId:callId]) {
          return NO;
        }
        NSString *nonce = [self valueForKey:@"nonce" fromQueryItems:queryItems];
    
        UJETStartOptions *options = [[UJETStartOptions alloc] initWithCallId:callId nonce:nonce];
    
        [UJET startWithOptions:options];
    
        return YES;
      }
    
      - (NSString *)valueForKey:(NSString *)key fromQueryItems:(NSArray *)queryItems {
        NSPredicate *predicate = [NSPredicate predicateWithFormat:@"name=%@", key];
        NSURLQueryItem *queryItem = [[queryItems
                                      filteredArrayUsingPredicate:predicate]
                                    firstObject];
        return queryItem.value;
      }
    
      - (BOOL)isValidCallId:(NSString *)callId {
        if (callId.length == 0) {
          return NO;
        }
    
        NSCharacterSet *nonNumbers = [[NSCharacterSet decimalDigitCharacterSet] invertedSet];
        NSRange r = [callId rangeOfCharacterFromSet: nonNumbers];
        return r.location == NSNotFound;
      }
    

For Swift:
    
    
      // MARK: Deep Link
    
      extension AppDelegate {
          func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
              print("Open app with url: \(url.absoluteString)")
    
              return self.handleRouting(url)
          }
    
          func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
              // Universal links
              if NSUserActivityTypeBrowsingWeb == userActivity.activityType {
                  return self.handleRouting(userActivity.webpageURL!)
              } else if userActivity.activityType == "INStartAudioCallIntent" {
                  // Open app from Call history
                  let model = DataController.shared.startOptions()
                  let startOptions = StartOptionsController().convert(model)
                  UJET.start(with: startOptions)
    
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
                  "ujet.cx/app",  // universal link,
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
    

## Target configurations

This section shows the capabilities and additional information needed for the target configuration.

### Capabilities

  * Push Notifications

  * Background Modes (check items below):

    * Audio and AirPlay

    * Voice over IP (VoIP)




### Information

Add the following keys with description:

  * NSMicrophoneUsageDescription

  * NSCameraUsageDescription

  * NSPhotoLibraryUsageDescription

  * NSFaceIDUsageDescription




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
