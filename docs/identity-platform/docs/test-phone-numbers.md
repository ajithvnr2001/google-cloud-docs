---
url: https://docs.cloud.google.com/identity-platform/docs/test-phone-numbers/
title: Registering test phone numbers \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:24.409950+00:00
---

# Registering test phone numbers  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/test-phone-numbers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Registering test phone numbers 

This document shows you how to register phone numbers with Identity Platform for development purposes. This allows you to test authentication methods that involve sending an SMS message, such as phone sign-in and multi-factor authentication.

Using a test number (rather than a real number you own) has several benefits:

  * It integrates seamlessly with the iOS and Android emulators.
  * It eliminates the overhead of sending an actual SMS.
  * You can execute consecutive tests with the same phone number without being throttled.
  * You can write integration tests without being blocked by security checks.
  * It doesn't consume your usage quota.



You can register up to 10 phone numbers for development.

## Registering a test phone number

To register a test phone number:

  1. Go to the **Identity Providers** page in the Google Cloud console.  
[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)  


  2. If you are testing phone authentication, locate it in the list of providers, then click the **Edit** icon. If you are testing multi-factor authentication, select the **Multi-factor SMS** tab, then click **Edit**.

  3. Under **Phone numbers for testing** , enter a phone number and verification code to register.

The phone number should use [ E.164 format](https://wikipedia.org/wiki/E.164), and cannot already be assigned to an existing Identity Platform user. The verification code should be six digits. For security purposes, choose numbers that are difficult to guess, and avoid obvious patterns like `+1 123-456-7890`.

  4. Click **Save**.




Testing phone numbers are treated like real phone numbers by Identity Platform, so store them securely and rotate them at regular intervals.

## Manual testing

You can immediately begin using test phone numbers in your app, either directly or using the iOS and Android emulators. When signing in with a test phone number, no SMS verification code is sent; instead, enter the code you registered when creating the test number.

After signing in, an Identity Platform user is created using the test phone number. This user has the same behavior and properties as a real user, including a valid ID token, meaning it can access all your apps and services.

To restrict access from your test users, consider creating a test role with limited permissions and assigning it using [custom claims](https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims).

## Integration testing

In addition to manual testing, the client SDK contains APIs that can help write integration tests. These APIs disable the reCAPTCHA and app verification requirements, making them easier bypass with automation.

The following example shows how to test signing in a user with a phone number:

###  JavaScript 
    
    
    // Turn off phone app verification.
    firebase.auth().settings.appVerificationDisabledForTesting = true;
    
    var phoneNumber = "+16505554567";
    var testVerificationCode = "123456";
    
    // Render a fake reCAPTCHA and resolve without app verification.
    var appVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container');
    // signInWithPhoneNumber will call appVerifier.verify(), which will resolve
    // with a fake reCAPTCHA response.
    firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
      .then(function (confirmationResult) {
        // confirmationResult can resolve using testVerificationCode.
        return confirmationResult.confirm(testVerificationCode)
      }).catch(function (error) {
        // Error; SMS not sent
        // ...
      });
    

Visible and invisible mock reCAPTCHA verifiers behave differently when app verification is disabled:

  * **Visible reCAPTCHA:** To simulate a user click, the reCAPTCHA will resolve itself automatically after a brief delay.

  * **Invisible reCAPTCHA** : To simulate app verification, the reCAPTCHA will resolve automatically when `appVerifier.verify()` is called.




Mock reCAPTCHAs will still trigger their callbacks when they resolve or expire.

## What's next

  * Add multi-factor authentication to your [web](https://docs.cloud.google.com/identity-platform/docs/web/mfa), [iOS](https://docs.cloud.google.com/identity-platform/docs/ios/mfa), or [Android](https://docs.cloud.google.com/identity-platform/docs/android/mfa) app.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
