---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-account-defender-assessment/
title: Create an assessment using hashedAccountId \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:18.260849+00:00
---

# Create an assessment using hashedAccountId  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-account-defender-assessment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Create an assessment using hashedAccountId Stay organized with collections  Save and categorize content based on your preferences. 

Create an assessment using hashedAccountId to detect account takeovers. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect and prevent account-related fraudulent activities on mobile applications](https://docs.cloud.google.com/recaptcha/docs/account-defender-mobile)
  * [Detect and prevent account-related fraudulent activities on websites](https://docs.cloud.google.com/recaptcha/docs/account-defender)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
