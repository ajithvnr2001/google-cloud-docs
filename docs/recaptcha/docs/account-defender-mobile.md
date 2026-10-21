---
url: https://docs.cloud.google.com/recaptcha/docs/account-defender-mobile/
title: Detect and prevent account-related fraudulent activities on mobile applications \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:28.791453+00:00
---

# Detect and prevent account-related fraudulent activities on mobile applications  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/account-defender-mobile/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Detect and prevent account-related fraudulent activities on mobile applications Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use Account defense to detect and prevent account-related fraudulent activities on mobile applications.

Fraud Defense helps you protect critical actions, such as login and checkout. However, there are many subtle forms of account abuse that can be detected by observing a specific user's behavior on a mobile application over a period of time. Account defense, a feature of Fraud Defense, helps in identifying these kinds of subtle abuse by creating a site-specific model for your mobile application to detect a trend of suspicious behavior or a change in activity. By using the site-specific model, Account defense helps you detect the following:

  * Suspicious activities
  * Accounts with similar behaviors
  * Requests coming from devices that were marked as trusted for specific users



Based on the analysis of Account defense and the site-specific model, you can take the following actions:

  * Restrict or disable fraudulent accounts.
  * Prevent account takeover attempts.
  * Mitigate the successful account takeovers.
  * Grant access only to the requests coming from legitimate user accounts.
  * Reduce friction for users logging in from one of their trusted devices.



## Before you begin

  1. Account defense for mobile applications is accessible after triggering an automatic security review by adding a billing account to your project. [ Add a billing account ](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) to your project to onboard your mobile application to this feature.
  2. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 
  3. [Create a score-based key](https://docs.cloud.google.com/recaptcha/docs/create-key-mobile).



## Configure your mobile application for Account defense

Account defense requires a comprehensive understanding of account activities to enable effective detection. To start feeding account-related activities to Account defense, and to create and improve your site-specific model, do the following:

  1. Integrate Fraud Defense with your mobile application.

     * For Android apps, see [Integrate Fraud Defense with Android apps](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps).
     * For iOS apps, see [Integrate Fraud Defense with iOS apps](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps).
  2. Report on critical user actions.
  3. Assess critical user events.
  4. Annotate user events to tune your site-specific model.



### Report on critical user actions

To detect suspicious activity patterns and build a better model of typical activity patterns on your site, Account defense needs the information about critical user actions. For each action of your app that is protected using Fraud Defense, call the `execute()` method with `RecaptchaAction`. For more information about `execute()` and `RecaptchaAction`, see the following: 

  * Android: [`execute()`](https://docs.cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaClient) and [`RecaptchaAction`](https://docs.cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaAction).
  * iOS: [`execute()`](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaClient) and [`RecaptchaAction`](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaAction).



The reCAPTCHA library provides a built-in set of actions, and if necessary you can create custom actions.

The following table lists the action names that you can use when reporting the critical user actions.

**Note:** Action names need not be confined to the following list. You can add action names that are meaningful and describe the user action such as `PASSWORD_RESET` or `ACCOUNT_UPDATE` by using [`custom() for Android`](https://docs.cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaAction#custom\(kotlin.String\)) or [`custom() for iOS`](https://docs.cloud.google.com/recaptcha/docs/reference/ios/client/api/Classes/RecaptchaAction#customaction). Action name | User initiated event or user action  
---|---  
`LOGIN` | Login to the mobile application.  
`SIGNUP` | Sign up on the mobile application.  
  
### Assess critical user events

When you call `execute()` on a user action, it generates a token. For the critical user events, such as successful and failed logins, registrations, and actions of the logged-in users, create an assessment to assess the results of the `execute()` call. The assessment provides you a risk verdict, which you can use to make a decision about how to handle potentially fraudulent activities. Some of the actions you can take are blocking suspicious requests, challenging risky logins, and investigating accounts of interest.

Account defense requires you to provide a stable account identifier to make the assessment and to attribute user activity–such as login requests, logged-in requests, and signup requests–to a specific account. This helps Account defense process user activity patterns to build an activity model for each account to better detect anomalous and abusive traffic.

Choose a stable account identifier `accountId` that is not often changed by the user and provide it to the assessment in the [ `projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method. This stable account identifier should have the same value for all the events related to the same user. You can provide the following as the account identifier:

### User identifiers

If every account can be uniquely associated with a stable username, email address, or phone number, you can use it as the `accountId`. When you provide such cross-site identifiers (identifiers that can be reused across sites), Fraud Defense uses this information to improve protection for your user accounts based on cross-site models by flagging abusive account identifiers and using knowledge of cross-site abuse patterns related to these identifiers.

Alternatively, if you have an internal user ID uniquely associated with each account, you can provide it as the `accountId`.

### Hashed or encrypted

If you do not have an internal user ID uniquely associated with each account, you can turn any stable identifier into an opaque, site-specific account identifier. This identifier is still needed for Fraud Defense account defender to understand user activity patterns and detect anomalous behaviour, but it is not shared across other sites.

Pick any stable account identifier and make it opaque before sending to Fraud Defense by using encryption or hashing:

  * encryption (recommended): encrypt the account identifier using a deterministic encryption method that produces a stable ciphertext. For detailed instructions, see [encrypt data deterministically](https://developers.google.com/tink/deterministic-encryption). When you choose symmetric encryption over hashing, you don't need to keep a mapping between your user identifiers and the corresponding opaque user identifiers. Decrypt the opaque identifiers that are returned by Fraud Defense to turn them into the user identifier.

  * hashing: we recommend hashing the account identifier using the SHA256-HMAC method with a custom salt of your choice. Because hashes are one-way only, you need to keep a mapping between the generated hashes and your user identifiers so that you can map the hashed account identifier that are returned back to the original accounts.




In addition to providing a stable account identifier for all the account-related requests, you can provide additional account identifiers, potentially non-stable, for some specific requests. Context-specific account identifiers provided in addition to the `accountId` help Account defense better analyze user activity and detect account takeover attempts to keep your user accounts safe. When you provide additional identifiers, Google Cloud Fraud Defense uses this information to improve protection for your user accounts based on cross-site models by flagging abusive account identifiers and using knowledge of cross-site abuse patterns related to these identifiers. For example, you can provide the following:

  * The username, email address, or phone number that was used as a login handle for login requests

  * The email address or phone number that was verified for a multi-factor authentication request

  * An email address or phone number (primary or secondary) that was provided by the user during an account update request

  * The email addresses and phone numbers that are provided by the user during a registration request




Append the chosen stable account identifier to the `accountId` parameter in the [` projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method for all the account-related requests. Optionally, provide additional account identifiers for the relevant requests by using the `userIds` field in the assessment.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * TOKEN: token returned from the `execute()` call
  * KEY_ID: reCAPTCHA key associated with the app
  * ACCOUNT_ID: the identifier that is uniquely associated with the user account for a user account to your app
  * EMAIL_ADDRESS: Optional. An email address that is associated with this request, if any
  * PHONE_NUMBER: Optional. A phone number that is associated with this request, if any
  * USERNAME: Optional. A username that is associated with this request, if any



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments

Request JSON body: 
    
    
    {
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userInfo": {
          "accountId": "ACCOUNT_ID",
          "userIds": [
            {
              "email": "EMAIL_ADDRESS"
            },
            {
              "phoneNumber": "PHONE_NUMBER"
            },
            {
              "username": "USERNAME"
            }
          ]
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "tokenProperties": {
        "valid": true,
        "androidPackageName": "com.example.app" or "iosBundleId": "com.example.app",
        "action": "login",
        "createTime": "2019-03-28T12:24:17.894Z"
      },
      "riskAnalysis": {
        "score": 0.6,
      },
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY",
        "userInfo": {
          "accountId": "ACCOUNT_ID"
        }
      },
      "name": "projects/PROJECT_NUMBER/assessments/b6ac310000000000",
      "accountDefenderAssessment": {
        "labels": ["SUSPICIOUS_LOGIN_ACTIVITY"]
      }
    }
    
    

**Note:** If you are already using the legacy `hashedAccountId` parameter to provide a stable account identifier to the [ `projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method, you can keep doing so. However, new integrations should use the `accountId` parameter instead, because the `hashedAccountId` is deprecated. 

#### Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.recaptchaenterprise.v1.[AccountDefenderAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountDefenderAssessment.html).[AccountDefenderLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountDefenderAssessment.AccountDefenderLabel.html);
    import com.google.recaptchaenterprise.v1.[Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html);
    import com.google.recaptchaenterprise.v1.[CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html);
    import com.google.recaptchaenterprise.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html);
    import com.google.recaptchaenterprise.v1.[RiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.html).[ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html);
    import com.google.recaptchaenterprise.v1.[TokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html);
    import com.google.recaptchaenterprise.v1.[UserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserId.html);
    import com.google.recaptchaenterprise.v1.[UserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfo.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.security.InvalidKeyException;
    import java.security.NoSuchAlgorithmException;
    import java.util.List;
    import java.util.UUID;
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    
    public class AccountDefenderAssessment {
    
      public static void main(String[] args)
          throws IOException, NoSuchAlgorithmException, InvalidKeyException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: Google Cloud Project ID
        String projectId = "project-id";
    
        // recaptchaSiteKey: Site key obtained by registering a domain/app to use recaptcha
        // services.
        String recaptchaSiteKey = "recaptcha-site-key";
    
        // token: The token obtained from the client on passing the recaptchaSiteKey.
        // To get the token, integrate the recaptchaSiteKey with frontend. See,
        // https://cloud.google.com/recaptcha-enterprise/docs/instrument-web-pages#frontend_integration_score
        String token = "recaptcha-token";
    
        // recaptchaAction: The action name corresponding to the token.
        String recaptchaAction = "recaptcha-action";
    
        // Unique ID of the user, such as email, customer ID, etc.
        String accountId = "default" + UUID.randomUUID().toString().split("-")[0];
    
        // User phone number
        String phoneNumber = "555-987-XXXX";
    
        // User email address
        String emailAddress = "john.doe@example.com";
    
        accountDefenderAssessment(projectId, recaptchaSiteKey, token, recaptchaAction, accountId, phoneNumber, emailAddress);
      }
    
      /**
       * This assessment detects account takeovers. See,
       * https://cloud.google.com/recaptcha-enterprise/docs/account-takeovers The input is the hashed
       * account id. Result tells if the action represents an account takeover. You can optionally
       * trigger a Multi-Factor Authentication based on the result.
       */
      public static void accountDefenderAssessment(
          String projectId,
          String recaptchaSiteKey,
          String token,
          String recaptchaAction,
          String accountId,
          String phoneNumber,
          String emailAddress)
          throws IOException {
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the properties of the event to be tracked.
          [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html).Builder eventBuilder =
              [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html).newBuilder()
                  .[setSiteKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setSiteKey_java_lang_String_)(recaptchaSiteKey)
                  .[setToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setToken_java_lang_String_)(token);
    
          // Set the account id, email address and phone number (of the user).
          eventBuilder.[setUserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setUserInfo_com_google_recaptchaenterprise_v1_UserInfo_)(
            [UserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfo.html).newBuilder()
              .setAccountId(accountId)
              .[addUserIds](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfo.Builder.html#com_google_recaptchaenterprise_v1_UserInfo_Builder_addUserIds_com_google_recaptchaenterprise_v1_UserId_)([UserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserId.html).newBuilder().setEmail(emailAddress))
              .[addUserIds](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfo.Builder.html#com_google_recaptchaenterprise_v1_UserInfo_Builder_addUserIds_com_google_recaptchaenterprise_v1_UserId_)([UserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserId.html).newBuilder().setPhoneNumber(phoneNumber)));
    
          [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html) event = eventBuilder.build();
    
          // Build the assessment request.
          [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html) createAssessmentRequest =
              [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html).newBuilder()
                  .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html).of(projectId).toString())
                  .setAssessment([Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html).newBuilder().[setEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.Builder.html#com_google_recaptchaenterprise_v1_Assessment_Builder_setEvent_com_google_recaptchaenterprise_v1_Event_)(event).build())
                  .build();
    
          [Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html) response = client.createAssessment(createAssessmentRequest);
    
          // Check integrity of the response token.
          if (!checkTokenIntegrity(response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)(), recaptchaAction)) {
            return;
          }
    
          // Get the reason(s) and the reCAPTCHA risk score.
          // For more information on interpreting the assessment,
          // see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
          for ([ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html) reason : response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getReasonsList()) {
            System.out.println(reason);
          }
          float recaptchaScore = response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getScore();
          System.out.println("The reCAPTCHA score is: " + recaptchaScore);
          String assessmentName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getName__)();
          System.out.println(
              "Assessment name: " + assessmentName.[substring](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_substring_int_)(assessmentName.lastIndexOf("/") + 1));
    
          // Get the Account Defender result.
          com.google.recaptchaenterprise.v1.[AccountDefenderAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountDefenderAssessment.html) accountDefenderAssessment =
              response.[getAccountDefenderAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getAccountDefenderAssessment__)();
          System.out.println(accountDefenderAssessment);
    
          // Get Account Defender label.
          List<AccountDefenderLabel> defenderResult =
              response.[getAccountDefenderAssessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getAccountDefenderAssessment__)().getLabelsList();
          // Based on the result, can you choose next steps.
          // If the 'defenderResult' field is empty, it indicates that Account Defender did not have
          // anything to add to the score.
          // Few result labels: ACCOUNT_DEFENDER_LABEL_UNSPECIFIED, PROFILE_MATCH,
          // SUSPICIOUS_LOGIN_ACTIVITY, SUSPICIOUS_ACCOUNT_CREATION, RELATED_ACCOUNTS_NUMBER_HIGH.
          // For more information on interpreting the assessment, see:
          // https://cloud.google.com/recaptcha-enterprise/docs/account-defender#interpret-assessment-details
          System.out.println("Account Defender Assessment Result: " + defenderResult);
        }
      }
    
      private static boolean checkTokenIntegrity(
          [TokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html) tokenProperties, String recaptchaAction) {
        // Check if the token is valid.
        if (!tokenProperties.[getValid](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html#com_google_recaptchaenterprise_v1_TokenProperties_getValid__)()) {
          System.out.println(
              "The Account Defender Assessment call failed because the token was: "
                  + tokenProperties.[getInvalidReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html#com_google_recaptchaenterprise_v1_TokenProperties_getInvalidReason__)().name());
          return false;
        }
    
        // Check if the expected action was executed.
        if (!tokenProperties.[getAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html#com_google_recaptchaenterprise_v1_TokenProperties_getAction__)().equals(recaptchaAction)) {
          System.out.printf(
              "The action attribute in the reCAPTCHA tag '%s' does not match "
                  + "the action '%s' you are expecting to score",
              tokenProperties.[getAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TokenProperties.html#com_google_recaptchaenterprise_v1_TokenProperties_getAction__)(), recaptchaAction);
          return false;
        }
        return true;
      }
    }

### Interpret the risk verdict of the critical user events

When you create an assessment with Account defense enabled, Account defense returns `accountDefenderAssessment` as part of the assessment response. The value of `accountDefenderAssessment` helps you assess whether the user activity is legitimate or fraudulent. It also returns an assessment ID that you need to use when annotating user events.

The following example is a sample JSON response:
    
    
    {
      "tokenProperties": {
        "valid": true,
        "androidPackageName": "com.example.app" or "iosBundleId": "com.example.app",
        "action": "login",
        "createTime": "2019-03-28T12:24:17.894Z"
       },
      "riskAnalysis": {
        "score": 0.6,
      },
     "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "expectedAction": "USER_ACTION"
      },
      "**name"** : "projects/PROJECT_ID/assessments/b6ac310000000000X",
      "accountDefenderAssessment": {
        labels: ["SUSPICIOUS_LOGIN_ACTIVITY"]
      }
    }

The `accountDefenderAssessment` field can have any of the following values:

Value | Description  
---|---  
`SUSPICIOUS_LOGIN_ACTIVITY` | Indicates that the request represents a high risk of credential stuffing or account takeover.  
`SUSPICIOUS_ACCOUNT_CREATION` | Indicates that the request represents a high risk of abusive account creation.  
`PROFILE_MATCH` | Indicates that the attributes of the user match the attributes that have been seen earlier for this particular user. This value is an indicator that this user is on a trusted device that was used before to access your mobile application. `PROFILE_MATCH` is returned only in the following scenarios:

  * You use [Multi-factor (MFA) or Two-factor authentication (2FA)](https://docs.cloud.google.com/recaptcha/docs/integrate-account-verification) and Account defense marks user profiles as trusted after users pass the MFA or 2FA challenge.
  * You annotate assessments as `LEGITIMATE` or `PASSED_TWO_FACTOR` and Account defense marks the corresponding user profile as trusted.

  
**Note:** If the `accountDefenderAssessment` field is empty, it indicates that Account defense did not have anything to add to the score. 

### Annotate events to tune your site-specific model

To provide more information to Account defense and improve your site-specific detection model, you must annotate the events that you assessed by creating assessments.

You annotate an assessment by sending a request to the [`projects.assessments.annotate`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate) method with the assessment ID. In the body of that request, you include labels providing additional information about an event described in the assessment.

To annotate an assessment, do the following:

  1. Determine the information and labels to add in the request JSON body depending on your use case.

The following table lists the labels and values that you can use to annotate events:

Label | Description | Request example  
---|---|---  
`reasons` | Required. A label to support your assessments. Provide real-time event details in the `reasons` label in a few seconds or minutes after the event because they influence real-time detection. For the list of possible values, see [reasons values](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason). Example: To detect account takeovers, annotate if the entered password was correct with `CORRECT_PASSWORD` or `INCORRECT_PASSWORD` values. If you deployed your own MFA, you can add the following values: `INITIATED_TWO_FACTOR`, and `PASSED_TWO_FACTOR` or `FAILED_TWO_FACTOR`.  | 
         
         {
               "reasons": ["INCORRECT_PASSWORD"]
               }
               
  
`annotation` | Optional. A label to indicate the legitimacy of assessments. Provide facts about login and registration events to validate or correct your risk assessments in the `annotation` label. Possible values: `LEGITIMATE` or `FRAUDULENT`. You can send this information at any time or as part of a batch job. However, we recommend sending this information in a few seconds or minutes after the event because they influence real-time detection. | 
         
         {
                "annotation": "LEGITIMATE"
               }
         
             
  
`accountId` | Optional. A label to associate an [account ID](https://docs.cloud.google.com/recaptcha/docs/recaptcha/docs/account-defender#provide-account-id) with an event. If you created an assessment without an account ID, use this label to provide the account ID of an event whenever it is available. | 
         
         {
            "accountId": "ACCOUNT_ID"
           }  
  
  2. Create an annotate request with the appropriate labels.

Before using any of the request data, make the following replacements: 

     * ASSESSMENT_ID: Value of the `name` field returned from the `projects.assessments.create` call.
     * ANNOTATION: Optional. A label to indicate whether the assessment is legitimate or fraudulent.
     * REASONS: Optional. Reasons that support your annotation. For the list of possible values, see [reasons values](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason).
     * ACCOUNT_ID: Optional. the identifier that is uniquely associated with the user account on your app.

For more information, see [labels for annotations.](https://docs.cloud.google.com/recaptcha/docs/account-defender#sample-request)

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate

Request JSON body: 
    
    {
      "annotation": ANNOTATION,
      "reasons": REASONS,
      "accountId": ACCOUNT_ID
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




#### Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).Annotation;
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).Reason;
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentResponse.html);
    import com.google.recaptchaenterprise.v1.[AssessmentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentName.html);
    import java.io.IOException;
    import java.security.NoSuchAlgorithmException;
    import java.util.UUID;
    
    public class AnnotateAccountDefenderAssessment {
    
      public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        // TODO(developer): Replace these variables before running the sample.
        // projectID: GCloud Project id.
        String projectID = "project-id";
    
        // assessmentId: Value of the 'name' field returned from the CreateAssessment call.
        String assessmentId = "account-defender-assessment-id";
    
        // accountId: Set the accountId corresponding to the assessment id.
        String accountId = "default" + UUID.randomUUID().toString().split("-")[0];
    
        annotateAssessment(projectID, assessmentId, accountId);
      }
    
      /**
       * Pre-requisite: Create an assessment before annotating. Annotate an assessment to provide
       * feedback on the correctness of recaptcha prediction.
       */
      public static void annotateAssessment(
          String projectID, String assessmentId, String accountId) throws IOException {
    
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
          // Build the annotation request.
          // For more info on when/how to annotate, see:
          // https://cloud.google.com/recaptcha-enterprise/docs/annotate-assessment#when_to_annotate
          [AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html) annotateAssessmentRequest =
              [AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).newBuilder()
                  .setName([AssessmentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentName.html).of(projectID, assessmentId).toString())
                  .setAnnotation(Annotation.LEGITIMATE)
                  .addReasons(Reason.PASSED_TWO_FACTOR)
                  .setAccountId(accountId)
                  .build();
    
          // Empty response is sent back.
          [AnnotateAssessmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentResponse.html) response = client.annotateAssessment(annotateAssessmentRequest);
          System.out.println("Annotated response sent successfully ! " + response);
        }
      }
    }

## Use and interpret the account takeover risk score

The Account Takeover (ATO) risk score feature adds a numerical risk score and human-readable explanations to the Account defense assessment. These insights help you understand the assessment and inform your subsequent actions or decisions.

**Note:** You must have an Enterprise subscription to use the ATO risk score feature. For more information, see [Compare features between Fraud Defense tiers](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). 

### Get the risk score

To receive the risk score and explainability reasons, send a `CreateAssessment` request and include `event.userInfo.accountId` in your request.

### Read the risk score and details

The risk score and explainability reasons are in the `accountDefenderAssessment.accountTakeoverVerdict` object in the assessment response.

  * **Risk score** : `accountDefenderAssessment.accountTakeoverVerdict.risk`
  * **Risk reasons** : `accountDefenderAssessment.accountTakeoverVerdict.riskReasons`
  * **Trust reasons** : `accountDefenderAssessment.accountTakeoverVerdict.trustReasons`



The following snippet shows an example of the fields in an assessment response:
    
    
      "accountDefenderAssessment": {
        "labels": ["PROFILE_MATCH"],
        "accountTakeoverVerdict": {
          "risk": 0.249,
          "riskReasons": [{"reason": "CLIENT_ACCESSED_MANY_ACCOUNTS"}],
          "trustReasons": [{"reason": "PROFILE_MATCH"}, {"reason": "ACCOUNT_HISTORY_REPUTABLE"}]
        }
      }

### Interpret the ATO risk score

When you use the risk score, establish a threshold to determine when to take protective actions.

Use the ATO risk score as an alternative to the `SUSPICIOUS_LOGIN_ACTIVITY` label. Do not use both the risk score and the label to trigger enforcement on the same assessment. You can configure your enforcement logic either based on the risk score exceeding your threshold or based on the label's presence. Generally, the risk score offers a more granular assessment.

We recommend that you evaluate the risk score's performance with an appropriate threshold on your platform's traffic before you use it for enforcement.

To act on the risk score, implement a check in your backend as shown in the following snippet:
    
    
    if (assessment.accountDefenderAssessment.accountTakeoverVerdict.risk > YOUR_CHOSEN_THRESHOLD) {
      // Treat as suspicious
      // Implement protective actions
    }
    

### Standard risk score thresholds

The following table provides standard risk score thresholds and their expected False Positive Rates (FPR). Choose a threshold based on your acceptable FPR. Performance can vary, so you might need to adjust your threshold based on observed performance.

Risk tolerance | Recommended threshold | Maximum false positive rate  
---|---|---  
Low | 0.5 | 4%  
Medium | 0.7 | 1%  
High | 0.9 | 0.25%  
  
### Interpret explainability reasons

Explainability reasons provide insights into factors that influence the risk score. Use these reasons to refine your decision-making.

  * **Risk reasons** : indicate factors associated with a higher risk of account takeover.
  * **Trust reasons** : indicate factors that suggest legitimacy.



Both risk and trust reasons can appear for any given risk score.

Reason | Type | Interpretation  
---|---|---  
`PROFILE_MATCH` | Trust | The request matches a trusted profile associated with this account. This is equivalent to the `AccountDefenderLabel.PROFILE_MATCH` label.  
`ACCOUNT_HISTORY_REPUTABLE` | Trust | The account's historical activity is reputable. It is unlikely that the account has been compromised in the past.  
`CLIENT_HISTORICAL_BOT_ACTIVITY` | Risk | The client has been observed sending bot-like traffic to this site in the past. This reason incorporates historical reputation and indicates that the client is known to use bots, even if the current request is being made by a human.  
`ACCOUNT_IN_LARGE_RELATED_GROUP` | Risk | The account is part of a large group of related accounts, indicating that it may be part of a fraudulent network. Related accounts are identified based on having similar traffic patterns and request characteristics.  
`CLIENT_ACCESSED_MANY_ACCOUNTS` | Risk | The client has been observed accessing many accounts on this site.  
`DISPOSABLE_EMAIL_DOMAIN` | Risk | The provided email address belongs to a known or suspected provider of temporary, disposable (one-time use) email domains.  
  
## Adjust the account takeover risk threshold

After you evaluate the performance of the account takeover risk score on your traffic, you might need to adjust your threshold to achieve your acceptable False Positive Rate (FPR) and recall. You can tune your threshold based on observed performance or calculate intermediate values to target a specific FPR.

### Adjust your threshold

If the observed FPR is too high, increase the threshold. If the observed recall is too low and you can tolerate a higher FPR, decrease the threshold.

### Calculate intermediate values

To estimate the FPR for a threshold between the standard values, use linear interpolation. The following example shows how to calculate the FPR for a threshold of 0.85:
    
    
    _FPR_(_T_ : 0.85) = (_FPR_(_T_ : 0.8) +  _FPR_(_T_ : 0.9)) / 2 = (0.5% + 0.25%) / 2 = 0.375%
    

To find a threshold for a specific _FPR_ , interpolate between the standard values. The following example shows how to find the threshold for an _FPR_ of 5%:
    
    
    _Threshold_ = 0.4 + (0.5 − 0.4) × (8% − 5%) / (8% − 4%)
    _Threshold_ = 0.4 + 0.1 × (3 / 4)
    _Threshold_ = 0.4 + 0.075 = 0.475
    

A threshold of 0.475 is estimated to yield a 5% _FPR_.

## What's next

  * To learn about other account protection features, see [User accounts protection features](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
