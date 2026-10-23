---
url: https://docs.cloud.google.com/recaptcha/docs/check-passwords/
title: Detect password leaks and breached credentials \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:12.885127+00:00
---

# Detect password leaks and breached credentials  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/check-passwords/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Detect password leaks and breached credentials Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Password defense feature of Fraud Defense to detect password leaks and breached credentials to prevent account takeovers (ATOs) and credential stuffing attacks. With Fraud Defense, you can conduct regular audits of user credentials (passwords) as part of any assessment to ensure that they have not been leaked or breached. To perform these assessments, Google uses the [Password Checkup](https://security.googleblog.com/2019/08/new-research-lessons-from-password.html) feature.

**Important:** Password defense uses [secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation) (MPC) to protect user data. Requesting password checks might cause extra latency when creating an assessment. Although the response time is much faster, we recommend using a `500ms` timeout when creating an assessment with Password defense.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Set up Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow).

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Fraud Defense requires billing to be linked and enabled on the project to use the Password defense feature. You can enable billing by using either a credit card or an existing Google Cloud project billing ID. If you require assistance with billing, contact the [Cloud Billing support](https://cloud.google.com/support/billing).




## Check for breached and leaked credentials

You can check if a set of credentials has been compromised by using cryptographic functions or by using the Docker container.

The Docker container is an open-source client that implements the [secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation) that is needed to preserve end-user privacy and securely look up password leaks. For more information, see the [GitHub Repo](https://github.com/GoogleCloudPlatform/reCAPTCHA-PLD). The Docker container abstracts the complexity of implementing the cryptographic algorithms and simplifies the installation process. It also lets you host the container app in your infrastructure.

### Cryptographic function

To check if a set of credentials has been compromised, use Password defense when creating assessments for actions such as logins, password changes, and password resets.

To check for password leaks and breached credentials, complete the following steps:

  1. Generate request parameters.
  2. Create an assessment to detect password leaks.
  3. Verify leaked credentials from an assessment.
  4. Interpret verdict and take actions.



### Generate request parameters

  1. Calculate the necessary request parameters by using the cryptographic functions required by the high-privacy protocol. Password defense provides Java and TypeScript libraries to assist with generating these fields:

     * [java-recaptcha-password-check-helpers](https://github.com/GoogleCloudPlatform/java-recaptcha-password-check-helpers)
     * [typescript-recaptcha-password-check-helpers](https://github.com/GoogleCloudPlatform/typescript-recaptcha-password-check-helpers)
  2. To create password check verifications, create a `PasswordCheckVerifier` object.
         
         PasswordCheckVerifier verifier = new PasswordCheckVerifier();
         

  3. To initiate a verification, call `PasswordCheckVerifier#createVerification`. This method uses the username and password to calculate the parameters to perform the password check.
         
         PasswordCheckVerification verification = verifier.createVerification("username", "password").get();
         

  4. Create an [assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website#java) by using the verification parameters.
         
         byte[] lookupHashPrefix = verification.getLookupHashPrefix();
         byte[] encryptedUserCredentialsHash = verification.getEncryptedUserCredentialsHash();
         

The byte arrays `lookupHashPrefix` and `encryptedUserCredentialsHash` contain the parameters that are required to initiate a password check `Assessment`.




### Create an assessment to detect password leaks

Use the [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOOKUP_HASH_PREFIX: prefix of the username SHA-256 hash prefix
  * ENCRYPTED_USER_CREDENTIALS_HASH: encrypted user credentials Scrypt hash



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments

Request JSON body: 
    
    
    {
      "private_password_leak_verification": {
        "lookup_hash_prefix": "LOOKUP_HASH_PREFIX",
        "encrypted_user_credentials_hash": "ENCRYPTED_USER_CREDENTIALS_HASH"
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
      "name": "projects/698047609967/assessments/fb22000000000000",
      "score": 0,
      "reasons": [],
      "privatePasswordLeakVerification": {
        "lookupHashPrefix": "zoxZwA==",
        "encryptedUserCredentialsHash": "AyRihRcKaGLj/FA/r2uqQY/fzfTaDb/nEcIUMeD3Tygp",
        "reencryptedUserCredentialsHash": "Aw65yEbLM39ww1ridDEfx5VhkWo11tzn/R1B88Qqwr/+"
        "encryptedLeakMatchPrefixes": [
          "n/n5fvPD6rmQPFyb4xk=", "IVQqzXsbZenaibID6OI=", ..., "INeMMndrfnlf6osCVvs=",
          "MkIpxt2x4mtyBnRODu0=", "AqUyAUWzi+v7Kx03e6o="]
      }
    }
    

### Verify leaked credentials from an assessment

From the assessment response extract the fields `reEncryptedUserCredentials` and `encryptedLeakMatchPrefixes`, and pass them to the verifier object to determine if the credentials are leaked or not.
    
    
    PasswordCheckResult result = verifier.verify(verification,
    result.getReEncryptedUserCredentials(),
    result.getEncryptedLeakMatchPrefixes()
    ).get();
    
    System.out.println("Credentials leaked: " + result.areCredentialsLeaked());
    

#### Code sample

###  Node.js (TypeScript) 

To learn about how to implement Password defense by using Node.js (TypeScript), see the [TypeScript code sample on GitHub](https://github.com/GoogleCloudPlatform/typescript-recaptcha-password-check-helpers/tree/main).

###  Java 

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptcha.passwordcheck.PasswordCheckResult;
    import com.google.cloud.recaptcha.passwordcheck.PasswordCheckVerification;
    import com.google.cloud.recaptcha.passwordcheck.PasswordCheckVerifier;
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.recaptchaenterprise.v1.[Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html);
    import com.google.recaptchaenterprise.v1.[CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.stream.Collectors;
    
    public class CreatePasswordLeakAssessment {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Google Cloud Project ID.
        String projectID = "project-id";
    
        // Username and password to be checked for credential breach.
        String username = "username";
        String password = "password";
    
        checkPasswordLeak(projectID, username, password);
      }
    
      /*
       * Detect password leaks and breached credentials to prevent account takeovers
       * (ATOs) and credential stuffing attacks.
       * For more information, see:
       * https://cloud.google.com/recaptcha-enterprise/docs/check-passwords and
       * https://security.googleblog.com/2019/02/protect-your-accounts-from-data.html
    
       * Steps:
       * 1. Use the 'create' method to hash and Encrypt the hashed username and
       * password.
       * 2. Send the hash prefix (26-bit) and the encrypted credentials to create
       * the assessment.(Hash prefix is used to partition the database.)
       * 3. Password leak assessment returns a list of encrypted credential hashes to
       * be compared with the decryption of the returned re-encrypted credentials.
       * Create Assessment also sends back re-encrypted credentials.
       * 4. The re-encrypted credential is then locally verified to see if there is
       * a match in the database.
       *
       * To perform hashing, encryption and verification (steps 1, 2 and 4),
       * reCAPTCHA Enterprise provides a helper library in Java.
       * See, https://github.com/GoogleCloudPlatform/java-recaptcha-password-check-helpers
    
       * If you want to extend this behavior to your own implementation/ languages,
       * make sure to perform the following steps:
       * 1. Hash the credentials (First 26 bits of the result is the
       * 'lookupHashPrefix')
       * 2. Encrypt the hash (result = 'encryptedUserCredentialsHash')
       * 3. Get back the PasswordLeak information from
       * reCAPTCHA Enterprise Create Assessment.
       * 4. Decrypt the obtained 'credentials.getReencryptedUserCredentialsHash()'
       * with the same key you used for encryption.
       * 5. Check if the decrypted credentials are present in
       * 'credentials.getEncryptedLeakMatchPrefixesList()'.
       * 6. If there is a match, that indicates a credential breach.
       */
      public static void checkPasswordLeak(
          String projectID, String username, String password)
          throws ExecutionException, InterruptedException, IOException {
    
        // Instantiate the java-password-leak-helper library to perform the cryptographic functions.
        PasswordCheckVerifier passwordLeak = new PasswordCheckVerifier();
    
        // Create the request to obtain the hash prefix and encrypted credentials.
        PasswordCheckVerification verification =
            passwordLeak.createVerification(username, password).get();
    
        byte[] lookupHashPrefix = verification.getLookupHashPrefix();
        byte[] encryptedUserCredentialsHash = verification.getEncryptedUserCredentialsHash();
    
        // Pass the credentials to the createPasswordLeakAssessment() to get back
        // the matching database entry for the hash prefix.
        [PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html) credentials =
            createPasswordLeakAssessment(
                projectID,
                lookupHashPrefix,
                encryptedUserCredentialsHash);
    
        // Convert to appropriate input format.
        List<byte[]> leakMatchPrefixes =
            credentials.[getEncryptedLeakMatchPrefixesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html#com_google_recaptchaenterprise_v1_PrivatePasswordLeakVerification_getEncryptedLeakMatchPrefixesList__)().stream()
                .map(x -> x.toByteArray())
                .collect(Collectors.toList());
    
        // Verify if the encrypted credentials are present in the obtained match list.
        PasswordCheckResult result =
            passwordLeak
                .verify(
                    verification,
                    credentials.[getReencryptedUserCredentialsHash](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html#com_google_recaptchaenterprise_v1_PrivatePasswordLeakVerification_getReencryptedUserCredentialsHash__)().toByteArray(),
                    leakMatchPrefixes)
                .get();
    
        // Check if the credential is leaked.
        boolean isLeaked = result.areCredentialsLeaked();
        System.out.printf("Is Credential leaked: %s", isLeaked);
      }
    
      // Create a reCAPTCHA Enterprise assessment.
      // Returns:  PrivatePasswordLeakVerification which contains
      // reencryptedUserCredentialsHash and credential breach database
      // whose prefix matches the lookupHashPrefix.
      private static [PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html) createPasswordLeakAssessment(
          String projectID,
          byte[] lookupHashPrefix,
          byte[] encryptedUserCredentialsHash)
          throws IOException {
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the hashprefix and credentials hash.
          // Setting this will trigger the Password leak protection.
          [PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html) passwordLeakVerification =
              [PrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.html).newBuilder()
                  .[setLookupHashPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.Builder.html#com_google_recaptchaenterprise_v1_PrivatePasswordLeakVerification_Builder_setLookupHashPrefix_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(lookupHashPrefix))
                  .[setEncryptedUserCredentialsHash](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PrivatePasswordLeakVerification.Builder.html#com_google_recaptchaenterprise_v1_PrivatePasswordLeakVerification_Builder_setEncryptedUserCredentialsHash_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(encryptedUserCredentialsHash))
                  .build();
    
          // Build the assessment request.
          [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html) createAssessmentRequest =
              [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html).newBuilder()
                  .setParent(String.format("projects/%s", projectID))
                  .setAssessment(
                      [Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html).newBuilder()
                          // Set request for Password leak verification.
                          .[setPrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.Builder.html#com_google_recaptchaenterprise_v1_Assessment_Builder_setPrivatePasswordLeakVerification_com_google_recaptchaenterprise_v1_PrivatePasswordLeakVerification_)(passwordLeakVerification)
                          .build())
                  .build();
    
          // Send the create assessment request.
          [Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html) response = client.createAssessment(createAssessmentRequest);
    
          // Get the reCAPTCHA Enterprise score.
          float recaptchaScore = response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getScore();
          System.out.println("The reCAPTCHA score is: " + recaptchaScore);
    
          // Get the assessment name (id). Use this to annotate the assessment.
          String assessmentName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getName__)();
          System.out.println(
              "Assessment name: " + assessmentName.[substring](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_substring_int_)(assessmentName.lastIndexOf("/") + 1));
    
          return response.[getPrivatePasswordLeakVerification](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getPrivatePasswordLeakVerification__)();
        }
      }
    }

###  Docker container 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To check if credentials are leaked, securely send the username and password credential pair to the container by using a localhost connection or by setting up HTTPS on the container. The container then encrypts these credentials before making an API request, and verifies the re-encrypted result locally.

**Note:** Credentials that are shared in this way are never read or decrypted by Google, and the verification is performed by the container itself.

To send requests to the Docker container, complete the following steps:

  1. [Set up Docker](https://www.docker.com/get-started/).
  2. Prepare an environment for the Docker container.
  3. Build and run the container.
  4. Send HTTP requests to the container.
  5. Interpret verdict and take actions.



### Prepare to run the Docker container

  1. Choose an authentication strategy.

The container supports setting [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) or can accept an [API Key](https://docs.cloud.google.com/docs/authentication/api-keys) for authentication.

  2. Configure the PLD container to run with HTTPS or in a localhost-only demo mode.

Because the container accepts sensitive end-user credentials (usernames and passwords), it must be run either with HTTPS or in a localhost-only demo mode. For guidance on HTTPS configuration, see [README on GitHub](https://github.com/GoogleCloudPlatform/reCAPTCHA-PLD).




The following steps use API key authentication and run the client in the localhost-only demo mode.

### Build and run the Docker container

  1. Clone the repository:
         
         git clone github.com/GoogleCloudPlatform/reCAPTCHA-PLD
         

  2. Build the container:
         
         docker build . -t pld-local
         

  3. Start the container:
         
         docker run --network host \
         -e RECAPTCHA_PROJECT_ID=PROJECT_ID \
         -e GOOGLE_CLOUD_API_KEY=API_KEY \
         pld-local
         




The container starts and begins to serve requests on port 8080 of localhost.

### Send Localhost Requests

**Important:** Although this example shows the container running in HTTP, we recommend that you use HTTPS certificates when running the Docker container in a production environment. For details about setting up HTTPS and provide certificates to the container, see [README](https://github.com/GoogleCloudPlatform/reCAPTCHA-PLD).

Before using any of the request data, make the following replacements: 

  * LEAKED_USERNAME: username of the leaked credentials pair.
  * LEAKED_PASSWORD: password of the leaked credentials pair.



HTTP method and URL: 
    
    
    POST http://localhost:8080/createAssessment/

Request JSON body: 
    
    
    {
        "username":"LEAKED_USERNAME",
        "password":"LEAKED_PASSWORD"
    }
    
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "http://localhost:8080/createAssessment/"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "http://localhost:8080/createAssessment/" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
      { "leakedStatus":"LEAKED" }
    
    
     OR
    
    
      { "leakedStatus":"NO_STATUS" }
    
    

## Interpret verdict and take actions

The assessment response shows if the credentials were leaked and provides you with information that you can use to take appropriate actions to protect your users.

The following table lists the recommended actions that you can take when a leaked password is detected:

Leaked password detected | Actions to protect your user  
---|---  
During sign-in  | 

  * Reject and require that the customer choose a different password, and trigger an MFA challenge, if possible. 
  * Remind the user to use unique passwords across accounts.
  * Require strong passwords on your site.
  * Prompt the user to enable multi-factor authentication (MFA) if they are not using it.

  
During account creation or password reset  | 

  * Require the user change their password.
  * Trigger a multi-factor authentication (MFA) flow.

  
  
If you aren't using an MFA provider on your site already, you can use the [MFA capability](https://docs.cloud.google.com/recaptcha/docs/integrate-account-verification) of Fraud Defense.

## What's next

  * Learn about how to use [multi-factor authentication (MFA)](https://docs.cloud.google.com/recaptcha/docs/integrate-account-verification)
  * Learn about how to protect user accounts by using Fraud Defense [Account defense](https://docs.cloud.google.com/recaptcha/docs/account-defender)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
