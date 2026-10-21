---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview/
title: Mobile SDKs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:50:54.731804+00:00
---

# Mobile SDKs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Mobile SDKs Stay organized with collections  Save and categorize content based on your preferences. 

The Contact Center AI Platform (CCAI Platform) mobile SDKs include the Android SDK and the iOS SDK. With these SDKs, you can provide voice and chat support for your customers directly inside your iOS or Android mobile app.

You can set up mobile apps to work with CCAI Platform in a number of ways, including integrating the mobile SDKs into your mobile apps as directed in the [Android SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide) or the [iOS SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide). You can also integrate the mobile SDKs into your mobile apps using Flutter or React Native.

## Integrate using Flutter

This section provides the initial steps for using Flutter to integrate the mobile SDKs into your mobile apps. The steps in this section are the same for both the Android SDK and the iOS SDK. After completing these steps, you can continue by using instructions specific to the Android SDK or the iOS SDK, depending on your mobile platform.

Flutter is not required for integrating the mobile SDKs into your mobile apps. You can also integrate as directed in the following:

  * The [Android SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide)

  * The [iOS SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide)

  * Integrate using React Native




### Run the sample app locally

Running a sample app requires the following:

  * Flutter: A framework for building cross-platform apps.

  * Android Studio: An integrated development environment for Flutter and Android app development.

  * Xcode: An integrated development environment for iOS app development.

  * Cocoapods: A dependency manager for iOS projects.




To run the sample app locally, follow these steps:

  1. Download and expand the [Flutter example](https://externals.ujet.co/packages/ujet-flutter-example.zip) ZIP file.

  2. In the terminal, go to the Flutter example directory.

  3. Enter the following code in the terminal:
         
         cd example
         cp .env.example .env
         

  4. Enter the environment variable values in the `.env` file—for example, `API_KEY=your_api_key`. Quotation marks are not required.

  5. To install dependencies, enter `flutter pub get` in the terminal.

  6. To update the company information, go to `android/app/src/main/res/values/strings.xml` and update `ujet_company_key`, `ujet_subdomain`, and `ujet_company_url`.

  7. Depending on your platform, run either an Android emulator or an iOS simulator.

  8. Enter `flutter run` in the terminal.




### Import the CCAI Platform module into your project

Importing the CCAI Platform module into your project requires the following:

  * A JWT signing API endpoint. For more information, see [SDK end user authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth).

  * For Android, your project's deployment target must be iOS 13.0 or later.

  * For iOS, your project's `minSdkVersion` must be 21 or later.




To import the CCAI Platform module into your project, follow these steps:

  1. Copy the contents of the `example/lib/ujet` directory and paste it into your Flutter project in the `lib` directory.

  2. Go to `example/android/app/src/main/kotlin/co/ujet/flutter_example_app` and copy the following files into your Flutter project where the `MainActivity` class is located:

     * `UJETModule.kt`

     * `Application.kt`

     * `firebase\MyFirebaseMessagingService.kt`

     * `firebase\FirebaseTokenManager.kt`

**Important:** Be sure to change the package declaration at the top of these files according to your project's package structure.
  3. Open XCode, and then drag `example/ios/Runner/UJETModule.swift` into your project.

  4. Open `example/lib/ujet/ujet_module.dart` and edit the `_getUserData` method so that it returns appropriate end-user information. See the following code sample:
         
         static Future<Map<String, String?>> _getUserData() async {
         
         String? name = "John Doe"; // end-user name
         String? identifier = "id1234"; // end user identifier
         String? email = "jdoe@example.com"; // end user email
         String? phone = "+12223334444"; // end user phone
         
         return {
           "name": name,
           "identifier": identifier,
           "email": email,
           "phone": phone
           };
         }
         

  5. Implement `signPayload` in `server_api.dart` to get the signed JWT token from your server API. For more information, see [SDK end user authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth).




### Initialize and start

To initialize and start, enter the following code in the terminal:
    
    
     await UJET.init(key: 'your_ujet_key', baseUrl: 'your_ujet_base_url');
     await UJET.start(UjetStartOptions(skipSplashScreen: true));
    

### Known issues

Here known issues for using Flutter to integrate the mobile SDKs into your mobile apps:

  * **Issue** : Screenshots are not captured using the screenshot SmartActions.

    * **Action** : Google is working to fix this issue.
  * **Issue** : The Co-browse screen is not projected from the agent side during a co-browse session (iOS only).

    * **Action** : Google recommends disabling the impeller engine on iOS devices. To disable the impeller engine, follow these steps:

      1. Open the `info.plist` file.

      2. Set the `FLTEnableImpeller` key to `false`, as in the following code sample:
             
             <key>FLTEnableImpeller</key>
             <false/>
             




### Continue your integration

To continue integrating using Flutter, see one of the following pages, depending on your mobile platform:

  * [Flutter for Android](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-flutter)

  * [Flutter for iOS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-flutter)




## Integrate using React Native

This section provides the initial steps for using React Native to integrate the mobile SDKs into your mobile apps. The steps in this section are the same for both the Android SDK and the iOS SDK. After completing these steps, you can continue by using instructions specific to the Android SDK or the iOS SDK, depending on your mobile platform.

React Native is not required for integrating the mobile SDKs into your mobile apps. You can also integrate as directed in the following:

  * The [Android SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide)

  * The [iOS SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide)

  * Integrate using Flutter




### Run the sample app locally

To run the sample app locally, do the following:

  1. Download and extract the [ujet-react-native-example.zip](https://externals.ujet.co/packages/ujet-react-native-example.zip) sample app.

  2. Open the README.md file in the extracted folder, and follow the instructions.




### Run the sample app from a local server

The sample app that you downloaded in the previous procedure can also be run from a local server. To do this, follow these steps:

  1. Download and expand the [React Native example](https://externals.ujet.co/packages/ujet-react-native-example.zip) ZIP file.

  2. Access the directory where the server sample is deployed.

  3. Enter the following commands:
         
         cd server
         cp .env.example .env
         Edit .env
         nvm use
         npm install
         npm start```
         




### Run React Native

To run React Native, follow these steps:

  1. Change the application directory.

  2. Enter the following commands:
         
         cd app
         nvm use
         npm install
         bundle install
         npx pod-install
         

  3. Update the company information:

     1. **src/screens/Home.tsx:** Update the parameters in `UJET.initialize({})`

     2. **android/app/src/main/res/values/strings.xml:** Update `ujet_company_key`, `ujet_subdomain`, and `ujet_company_url`.

  4. Enter the command `npm start`.

  5. Run the iOS or Android mobile app using either the Meteor interactive CLI or an IDE of your choice.

**Note:** If the command fails, specify the simulator—for example, `npm run ios -- --simulator="iPhone 15 Pro"`.



### Import the CCAI Platform module to your project

This section shows you how to import the CCAI Platform module to your project.

#### Requirements

You need to use a JWT signing API endpoint. Refer to the `server/app.js` file in the sample app, or see [End User Authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth) for more details.

#### Procedure

To import the CCAI Platform module into your project, follow these steps:

  1. Copy the following files from the sample app and paste them into your project where appropriate:

     1. `app/src/native_modules/UJETInterfaces.ts`
     2. `app/src/native_modules/UJETNativeModule.ts`
     3. `app/ios/UJETModule.h`
     4. `app/ios/UJETModule.m`
     5. `app/android/src/main/java/com/sampleapp/UJETModule.kt`
  2. Open `UJETNativeModule.ts`

     1. Remove the following line:

`import AsyncStorage from '@react-native-async-storage/async-storage';`

     2. Edit the `getUserData` function to return accurate end user information:
            
            async function getUserData({ name: anonymousName }: SignPayloadData): Promise<Object> {
              // fetch the end user information from your application
              return {
                name: 'John Doe',
                identifier: 'id1234',
                email: 'jdoe@example.com',
                phone: '+12223334444'
              }
            }
            

     3. Update SIGNING_BASE_URL to point to your signing endpoint.

  3. Initialize and start, using the following code sample:
         
         import { UJET } from '../path/UJETNativeModule';
         
         UJET.initialize({
           key: 'your-key',
           baseUrl: 'your-base-url'
         });
         
         const startUJET = () => {
           UJET.start({
             skipSplashScreen: true
           });
         };
         

     * Replace `your-key` with the company ID.
     * Replace `your-base-url` with the API endpoint for the CCAI Platform host—for example, `https://ccaas-host.uc1.ccaiplatform.com/api/v2/`.



### Continue your integration

To continue integrating using React Native, see one of the following pages, depending on your mobile platform:

  * [React Native for Android](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-react)

  * [React Native for iOS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-react)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
