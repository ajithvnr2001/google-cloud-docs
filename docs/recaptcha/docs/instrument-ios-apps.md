---
url: https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps/
title: Integrate Google Cloud Fraud Defense with iOS apps \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:02:11.426666+00:00
---

# Integrate Google Cloud Fraud Defense with iOS apps  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Integrate Google Cloud Fraud Defense with iOS apps Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to integrate Google Cloud Fraud Defense in your iOS app.

Due to the variation in mobile devices in terms of screen size, performance, and UIs of the apps, the visual checkbox reCAPTCHA challenge (**I'm not a robot**) is not available for iOS mobile apps. You can instead implement your own tiered enforcement strategy, such as an MFA flow to provide an alternative redemption path for suspicious traffic.

The SDK makes use of reflection and dynamic code to allow for the update and refinement of the detection system in already deployed applications or SDKs. To avoid interference with the application, the classes available in the system are restricted to a carefully controlled list.

**Warning:** Upgrade your Fraud Defense iOS Mobile SDK to prevent potential app crashes. We have identified a technical issue affecting SDK versions prior to v18.9.0 that causes crashes for users on iOS 27 Beta. To ensure continuous application stability and protect your end-users, upgrade your application dependency to Fraud Defense iOS Mobile SDK version 18.9.0 or later. **Important:** Take note of the [deprecation and decommissioning policy](https://docs.cloud.google.com/recaptcha/docs/deprecation-policy-mobile) and plan to upgrade the SDK on a regular basis.

## Before you begin

  1. Set the minimum SDK of your app to **iOS 15** or create a new mobile app.

**Note:** reCAPTCHA supports both iPhone and iPad devices.
  2. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  3. [Create a reCAPTCHA key](https://cloud.google.com/recaptcha/docs/create-key-mobile) for the iOS app platform.

Alternatively, you can copy the ID of an existing reCAPTCHA key for iOS by performing one of the following steps:

     * To copy the ID of an existing key from the **Google Cloud console** , do the following:

       1. Go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. Select the **Keys** tab.
       3. In the reCAPTCHA keys list, find the key you want to copy, and then click  content_copy . 
     * To copy the ID of an existing key using the **REST API** , use the [projects.keys.list](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method. 
     * To copy the ID of an existing key using the **gcloud CLI** , use the [gcloud recaptcha keys list](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command. 
  4. Have a GitHub account.

  5. Read the [Apple privacy details](https://docs.cloud.google.com/recaptcha/docs/apple-privacy-details).




## Prepare your iOS environment

To prepare your development environment, do the following:

  1. Download and install the [latest version of Xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12) and [create a new blank iOS single view application](https://developer.apple.com/documentation/xcode/creating-an-xcode-project-for-an-app).

  2. Download the SDK by using one of the following:

### CocoaPods

     1. [Download and install CocoaPods](https://cocoapods.org/).
     2. Create a Podfile and add the following lines to your Podfile:
            
            source "https://github.com/CocoaPods/Specs.git"
            
            target 'AppTarget' do
            
              # Podfiles must include use_frameworks! or
              # use_frameworks! :linkage => :static
              use_frameworks!
            
              pod "RecaptchaEnterprise", "18.10.0-beta01"
              ...
            
            end
            

     3. Install the required dependencies by running `pod update`.

**Note:** Running `pod clone` doesn't install the required dependencies.

### Swift Package Manager

     1. In Xcode, select **File > Add Packages**, and enter the following URL in the **Search** or **Enter Package URL** field:
            
            https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk
            

     2. In the **Xcode** dialog, enter the following details:

        * GitHub username.
        * A personal access token that you created using [GitHub's instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). The **Personal Access Token** must have the scopes listed in the **Xcode Sign In** dialog.

Xcode installs the SDK and its required dependencies.

### Flutter

For detailed instructions about using reCAPTCHA through Flutter, see the [Flutter documentation](https://pub.dev/packages/recaptcha_enterprise_flutter).

### React Native

For detailed instructions about using reCAPTCHA through React Native, see the [React Native documentation](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-react-native).

### Direct download

     1. If you want to download the SDK and its dependencies as xcframeworks, download the [client](https://dl.google.com/recaptchaenterprise/v18.10.0-beta01/RecaptchaEnterprise_iOS_xcframework/recaptcha-xcframework.xcframework.zip).

**Note:** Add all binaries as static xcframeworks.




## Integrate Fraud Defense with your iOS app

To integrate Fraud Defense with your iOS app, follow these steps in Xcode:

  1. To instantiate the SDK with the reCAPTCHA key (KEY_ID) that you created, update the app with the following code:

### Swift with Storyboard

     1. Update `ViewController.swift`.
            
            import RecaptchaEnterprise
            
            class ViewController: UIViewController {
              var recaptchaClient: RecaptchaClient?
            
              override func viewDidLoad() {
                super.viewDidLoad()
                Task {
                  do {
                    self.recaptchaClient = try await Recaptcha.fetchClient(withSiteKey: "KEY_ID")
                  } catch let error as RecaptchaError {
                     print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
                  }
                }
              }
            }
            

If your application's minimum OS version is less than 13, use a trailing closure instead:
            
            import RecaptchaEnterprise
            
            class ViewController: UIViewController {
              var recaptchaClient: RecaptchaClient?
            
              override func viewDidLoad() {
                super.viewDidLoad()
                Recaptcha.fetchClient(withSiteKey: "KEY_ID") { client, error in
                  guard let client = client else {
                      print("RecaptchaClient creation error: \(error).")
                    return
                  }
                  self.recaptchaClient = client
                }
              }
            }
            

### Swift with SwiftUI

     1. Create a `ViewModel` class.
            
            import RecaptchaEnterprise
            
            @MainActor class ViewModel: ObservableObject {
              private var recaptchaClient: RecaptchaClient?
            
              init() {
                 Task {
                  do {
                    self.recaptchaClient = try await Recaptcha.fetchClient(withSiteKey: "KEY_ID")
                  } catch let error as RecaptchaError {
                     print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
                  }
                }
              }
            }
            

If your application's minimum OS version is less than 13, use a trailing closure instead:
            
            import RecaptchaEnterprise
            
            class ViewController: UIViewController {
              var recaptchaClient: RecaptchaClient?
            
              override func viewDidLoad() {
                super.viewDidLoad()
                Recaptcha.fetchClient(withSiteKey: "KEY_ID") { client, error in
                  guard let client = client else {
                      print("RecaptchaClient creation error: \(error).")
                    return
                  }
                  self.recaptchaClient = client
                }
              }
            }
            

     2. Instantiate `ViewModel` in `ContentView.swift`.
            
            import SwiftUI
            import RecaptchaEnterprise
            
            struct ContentView: View {
              @StateObject private var viewModel = ViewModel()
            
              var body: some View {
              }
            }
            
            struct ContentView_Previews: PreviewProvider {
              static var previews: some View {
                ContentView()
              }
            }
            

### Objective-C

     1. If your app is written in Objective-C, create a dummy Swift file and include the following import to make sure Xcode can find and link the Swift libraries.
            
            import Foundation
            

     2. To ensure that the `Swift` code is linked correctly, navigate to **Target > Build Settings > Always Embed Swift Standard Libraries** and verify that the option is set to `Yes`.

     3. Update `ViewController.h`.
            
            #import <RecaptchaEnterprise/RecaptchaEnterprise.h>
            
            @interface ViewController : UIViewController
            @property (strong, atomic) RecaptchaClient *recaptchaClient;
            @end
            

     4. Update `ViewController.m`.
            
            @implementation ViewController
            [Recaptcha fetchClientWithSiteKey:@"KEY_ID"
                  completion:^void(RecaptchaClient* recaptchaClient, NSError* error) {
                    if (!recaptchaClient) {
                      NSLog(@"%@", (RecaptchaError *)error.errorMessage);
                      return;
                    }
                    self->_recaptchaClient = recaptchaClient;
                  }
            ];
            @end
            

Initialization of the SDK can take several seconds to complete. To mitigate this latency, initialize the client as early as possible, such as during the `onCreate()` call of a custom `Application` class. You shouldn't make UI elements block on the reCAPTCHA SDK.

  2. Create a button to call reCAPTCHA and trigger `execute()`.

### Swift with Storyboard

     1. In the storyboard, create a button.
     2. Create an action in `ViewController` linked to the button that you created.
     3. Call the `execute()` method passing a `Login` action to return a reCAPTCHA token by using the following code snippet:
            
            guard let recaptchaClient = recaptchaClient else {
              print("RecaptchaClient creation failed.")
              return
            }
            Task {
              do {
                let token = try await recaptchaClient.execute(withAction: RecaptchaAction.login)
                print(token)
              } catch let error as RecaptchaError {
                print(error.errorMessage)
              }
            }
            

If your application's minimum OS version is less than 13, use a trailing closure instead:
            
            guard let recaptchaClient = recaptchaClient else {
              print("RecaptchaClient creation failed.")
              return
            }
            recaptchaClient.execute(withAction: RecaptchaAction.login) { token, error in
              if let token = token {
                print(token)
              } else {
                print(error)
              }
            }
            

### Swift with SwiftUI

     1. Update ViewModel.swift with the execute code:
            
            import RecaptchaEnterprise
            
            @MainActor class ViewModel: ObservableObject {
            
              func execute() {
                guard let recaptchaClient = self.recaptchaClient else {
                  print("Client not initialized correctly.")
                  return
                }
            
                Task {
                  do {
                    let token = try await recaptchaClient.execute(withAction: RecaptchaAction.login)
                    print(token)
                  } catch let error as RecaptchaError {
                    print(error.errorMessage)
                  }
                }
              }
            }
            

If your application's minimum OS version is less than 13, use a trailing closure instead:
            
            guard let recaptchaClient = recaptchaClient else {
              print("RecaptchaClient creation failed.")
              return
            }
            recaptchaClient.execute(withAction: RecaptchaAction.login) { token, error in
              if let token = token {
                print(token)
              } else {
                print(error)
              }
            }
            

     2. Update ContentView.swift.
            
            import SwiftUI
            import RecaptchaEnterprise
            
            struct ContentView: View {
              @StateObject private var viewModel = ViewModel()
            
              var body: some View {
            
                Button {
                  viewModel.execute()
                } label: {
                  Text("Execute")
                }.padding()
            
                Spacer()
              }
            }
            
            struct ContentView_Previews: PreviewProvider {
              static var previews: some View {
                ContentView()
              }
            }
            

### Objective-C

     1. In the **storyboard** , create a button.
     2. Create an action in `ViewController` linked to the button that you created.
     3. Call the `execute()` method passing a `Login` action to return a reCAPTCHA token:
            
            if (!self->_recaptchaClient) {
              return;
            }
            
            [recaptchaClient execute:RecaptchaAction.login
                completion:^void(NSString* _Nullable  token, NSError* _Nullable error) {
              if (!token) {
                NSLog (@"%@", (RecaptchaError *)error.errorMessage);
                return;
              }
              NSLog (@"%@", token);
            }];
            

The `execute` API of the client can take several seconds to complete, such as in slow networking conditions or if it is waiting for background initialization to complete. Ensure that the `execute()` calls do not block a UI event, such as pressing a button.

  3. Test your application:

     1. reCAPTCHA uses [Apple's App Attest](https://developer.apple.com/documentation/devicecheck/establishing_your_app_s_integrity) as part of its detection engine. If you don't plan to use a testing key with a fixed score for local development, do the following:

        1. In Xcode, add the **App Attest** capability to your app.

        2. In your project's `.entitlements` file, set the App Attest environment to `production`.

     2. To clean your Xcode build environment, in the **Product** menu, click **Clean Build Folder**.

     3. To run the application, in the **Product** menu, click **Run**.

     4. In your loaded application, click the button that you created earlier.

     5. Observe your debug output window for a reCAPTCHA token (alphanumeric string), which is returned if the integration is successful.




## Migrate from getClient method to fetchClient method

The `fetchClient` method returns a [RecaptchaClient](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaClient) that retries initialization over network failures. If the app doesn't have network access when the client is created, the client keeps retrying and successfully initializes when a network is acquired.

If you call `execute(timeout)` and the client is not yet ready, it tries to initialize before returning a token or a [RecaptchaError](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaError).

The following example shows how to migrate from `getClient` to `fetchClient`.

### Swift with Storyboard
    
    
    // Migrate from getClient
    func initializeWithGetClient() {
      Task {
        do {
          self.recaptchaClient = try await Recaptcha.getClient(withSiteKey: "KEY_ID")
        } catch let error as RecaptchaError {
            print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
        }
      }
    }
    
    // Migrate to fetchClient
    func initializeWithFetchClient() {
      Task {
        do {
          self.recaptchaClient = try await Recaptcha.fetchClient(withSiteKey: "KEY_ID")
        } catch let error as RecaptchaError {
            print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
        }
      }
    }
    

If your application's minimum OS version is less than 13, use a trailing closure instead:
    
    
    // Migrate from getClient
    override func initializeWithGetClient() {
      Recaptcha.getClient(withSiteKey: "KEY_ID") { client, error in
        guard let client = client else {
            print("RecaptchaClient creation error: \(error).")
          return
        }
        self.recaptchaClient = client
      }
    }
    
    // Migrate to fetchClient
    override func initializeWithFetchClient() {
      Recaptcha.fetchClient(withSiteKey: "KEY_ID") { client, error in
        guard let client = client else {
            print("RecaptchaClient creation error: \(error).")
          return
        }
        self.recaptchaClient = client
      }
    }
    

### Swift with SwiftUI
    
    
    // Migrate from getClient
    func initializeWithGetClient() {
        Task {
        do {
          self.recaptchaClient = try await Recaptcha.getClient(withSiteKey: "KEY_ID")
        } catch let error as RecaptchaError {
            print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
        }
      }
    }
    
    // Migrate to fetchClient
    func initializeWithFetchClient() {
        Task {
        do {
          self.recaptchaClient = try await Recaptcha.fetchClient(withSiteKey: "KEY_ID")
        } catch let error as RecaptchaError {
            print("RecaptchaClient creation error: \(String(describing: error.errorMessage)).")
        }
      }
    }
    

If your application's minimum OS version is less than 13, use a trailing closure instead:
    
    
    // Migrate from getClient
    func initializeWithGetClient() {
      super.viewDidLoad()
      Recaptcha.getClient(withSiteKey: "KEY_ID") { client, error in
        guard let client = client else {
            print("RecaptchaClient creation error: \(error).")
          return
        }
        self.recaptchaClient = client
      }
    }
    
    // Migrate to fetchClient
    func initializeWithFetchClient() {
      super.viewDidLoad()
      Recaptcha.fetchClient(withSiteKey: "KEY_ID") { client, error in
        guard let client = client else {
            print("RecaptchaClient creation error: \(error).")
          return
        }
        self.recaptchaClient = client
      }
    }
    

### Objective-C
    
    
    // Migrate from getClient
    @implementation ViewController
    [Recaptcha getClientWithSiteKey:@"KEY_ID"
          completion:^void(RecaptchaClient* recaptchaClient, NSError* error) {
            if (!recaptchaClient) {
              NSLog(@"%@", (RecaptchaError *)error.errorMessage);
              return;
            }
            self->_recaptchaClient = recaptchaClient;
          }
    ];
    @end
    
    // Migrate to fetchClient
    @implementation ViewController
    [Recaptcha fetchClientWithSiteKey:@"KEY_ID"
          completion:^void(RecaptchaClient* recaptchaClient, NSError* error) {
            if (!recaptchaClient) {
              NSLog(@"%@", (RecaptchaError *)error.errorMessage);
              return;
            }
            self->_recaptchaClient = recaptchaClient;
          }
    ];
    @end
    

## Set a timeout for API calls

You can specify a timeout value for the `execute` APIs by using the `withTimeout` property.

**Note:** A default timeout of 10 seconds is used for consistency.

### Swift

  1. Set timeout when calling `execute`.
         
         Task {
             do {
               let token = try await recaptchaClient.execute(
                 withAction: RecaptchaAction.login,
                 withTimeout: 10000)
               print(token)
             } catch let error as RecaptchaError {
               print(error.errorMessage)
             }
           }
         

If your application's minimum OS version is less than 13, use a trailing closure instead:
         
         recaptchaClient.execute(
             withAction: RecaptchaAction.login,
             withTimeout: 10000
           ) { token, error in
             if let token = token {
               print(token)
             } else {
               print(error)
             }
           }
         




### Objective-C

  1. Set timeout when calling `execute`.
         
         [recaptchaClient execute:RecaptchaAction.login
               withTimeout:10000.0
               completion:^void(NSString* _Nullable  token, NSError* _Nullable error) {
             if (!token) {
               NSLog (@"%@", (RecaptchaError *)error.errorMessage);
               return;
             }
             NSLog (@"%@", token);
           }];
         




## Handle errors

If your app cannot communicate with the reCAPTCHA service successfully, it might be because the API encountered an error. You must add logic in your app to gracefully handle such errors.

For more details about mitigations for common API errors, see [RecaptchaErrorCode](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaError).

## API reference

For a complete reference of the reCAPTCHA API for iOS, see [`RecaptchaEnterprise`](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes).

## What's next

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-mobile).

**Note:** reCAPTCHA response tokens are assessed and annotated from your backend server, not from the mobile device.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
