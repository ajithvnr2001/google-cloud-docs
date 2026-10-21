---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-password-leak-verification/
title: Password leak verification \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:15.519488+00:00
---

# Password leak verification  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-password-leak-verification/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Password leak verification Stay organized with collections  Save and categorize content based on your preferences. 

Detect password leaks and breached credentials to prevent account takeovers (ATOs) and credential stuffing attacks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect password leaks and breached credentials](https://docs.cloud.google.com/recaptcha/docs/check-passwords)



## Code sample

### Java

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

### Node.js

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {RecaptchaEnterpriseServiceClient} from '@google-cloud/recaptcha-enterprise';
    import {PasswordCheckVerification} from 'recaptcha-password-check-helpers';
    
    // TODO(developer): Uncomment and set the following variables
    // Google Cloud Project ID.
    // const projectId: string = "PROJECT_ID"
    
    // Username and password to be checked for credential breach.
    // const username: string = "user123";
    // const password: string = "1234@abcd";
    
    // Create a client.
    const client = new RecaptchaEnterpriseServiceClient();
    
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
    * reCAPTCHA Enterprise provides a helper library in Typescript.
    * See, https://github.com/GoogleCloudPlatform/typescript-recaptcha-password-check-helpers
    
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
    async function checkPasswordLeak(projectId, username, password) {
      // Instantiate the recaptcha-password-check-helpers library to perform the
      // cryptographic functions.
      // Create the request to obtain the hash prefix and encrypted credentials.
      const verification = await PasswordCheckVerification.create(
        username,
        password
      );
    
      const lookupHashPrefix = Buffer.from(
        verification.getLookupHashPrefix()
      ).toString('base64');
      const encryptedUserCredentialsHash = Buffer.from(
        verification.getEncryptedUserCredentialsHash()
      ).toString('base64');
      console.log('Hashes created.');
    
      // Pass the credentials to the createPasswordLeakAssessment() to get back
      // the matching database entry for the hash prefix.
      const credentials = await createPasswordLeakAssessment(
        projectId,
        lookupHashPrefix,
        encryptedUserCredentialsHash
      );
    
      // Convert to appropriate input format.
      const reencryptedUserCredentialsHash = Buffer.from(
        credentials.reencryptedUserCredentialsHash.toString(),
        'base64'
      );
    
      const encryptedLeakMatchPrefixes = credentials.encryptedLeakMatchPrefixes.map(
        prefix => {
          return Buffer.from(prefix.toString(), 'base64');
        }
      );
    
      // Verify if the encrypted credentials are present in the obtained
      // match list to check if the credential is leaked.
      const isLeaked = verification
        .verify(reencryptedUserCredentialsHash, encryptedLeakMatchPrefixes)
        .areCredentialsLeaked();
    
      console.log(`Is Credential leaked: ${isLeaked}`);
    }
    
    // Create a reCAPTCHA Enterprise assessment.
    // Returns: PrivatePasswordLeakVerification which contains
    // reencryptedUserCredentialsHash and credential breach database whose prefix
    // matches the lookupHashPrefix.
    async function createPasswordLeakAssessment(
      projectId,
      lookupHashPrefix,
      encryptedUserCredentialsHash
    ) {
      // Build the assessment request.
      const createAssessmentRequest = {
        parent: `projects/${projectId}`,
        assessment: {
          // Set the hashprefix and credentials hash.
          // Setting this will trigger the Password leak protection.
          privatePasswordLeakVerification: {
            lookupHashPrefix: lookupHashPrefix,
            encryptedUserCredentialsHash: encryptedUserCredentialsHash,
          },
        },
      };
    
      // Send the create assessment request.
      const [response] = await client.createAssessment(createAssessmentRequest);
    
      // Get the reCAPTCHA Enterprise score.
      console.log(`The reCAPTCHA score is: ${response.riskAnalysis.score}`);
      // Get the assessment name (id). Use this to annotate the assessment.
      console.log(`Assessment name: ${response.name}`);
    
      if (!response.privatePasswordLeakVerification) {
        throw `Error in obtaining response from Private Password Leak Verification ${response}`;
      }
    
      return response.privatePasswordLeakVerification;
    }
    
    checkPasswordLeak(projectId, username, password).catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### Node.js

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {google} from '@google-cloud/recaptcha-enterprise/build/protos/protos';
    import {RecaptchaEnterpriseServiceClient} from '@google-cloud/recaptcha-enterprise';
    import {PasswordCheckVerification} from 'recaptcha-password-check-helpers';
    
    // TODO(developer): Uncomment and set the following variables
    // Google Cloud Project ID.
    // const projectId: string = "PROJECT_ID"
    
    // Username and password to be checked for credential breach.
    // const username: string = "user123";
    // const password: string = "1234@abcd";
    
    // Create a client.
    const client: RecaptchaEnterpriseServiceClient =
      new RecaptchaEnterpriseServiceClient();
    
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
    * reCAPTCHA Enterprise provides a helper library in Typescript.
    * See, https://github.com/GoogleCloudPlatform/typescript-recaptcha-password-check-helpers
    
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
    async function checkPasswordLeak(
      projectId: string,
      username: string,
      password: string
    ) {
      // Instantiate the recaptcha-password-check-helpers library to perform the
      // cryptographic functions.
      // Create the request to obtain the hash prefix and encrypted credentials.
      const verification: PasswordCheckVerification =
        await PasswordCheckVerification.create(username, password);
    
      const lookupHashPrefix: string = Buffer.from(
        verification.getLookupHashPrefix()
      ).toString('base64');
      const encryptedUserCredentialsHash: string = Buffer.from(
        verification.getEncryptedUserCredentialsHash()
      ).toString('base64');
      console.log('Hashes created.');
    
      // Pass the credentials to the createPasswordLeakAssessment() to get back
      // the matching database entry for the hash prefix.
      const credentials: google.cloud.recaptchaenterprise.v1.IPrivatePasswordLeakVerification =
        await createPasswordLeakAssessment(
          projectId,
          lookupHashPrefix,
          encryptedUserCredentialsHash
        );
    
      // Convert to appropriate input format.
      const reencryptedUserCredentialsHash: Uint8Array = Buffer.from(
        credentials.reencryptedUserCredentialsHash!.toString(),
        'base64'
      );
      const encryptedLeakMatchPrefixes: Uint8Array[] =
        credentials.encryptedLeakMatchPrefixes!.map(prefix => {
          return Buffer.from(prefix.toString(), 'base64');
        });
    
      // Verify if the encrypted credentials are present in the obtained
      // match list to check if the credential is leaked.
      const isLeaked: boolean = verification
        .verify(reencryptedUserCredentialsHash, encryptedLeakMatchPrefixes)
        .areCredentialsLeaked();
    
      console.log(`Is Credential leaked: ${isLeaked}`);
    }
    
    // Create a reCAPTCHA Enterprise assessment.
    // Returns: PrivatePasswordLeakVerification which contains
    // reencryptedUserCredentialsHash and credential breach database whose prefix
    // matches the lookupHashPrefix.
    async function createPasswordLeakAssessment(
      projectId: string,
      lookupHashPrefix: string,
      encryptedUserCredentialsHash: string
    ): Promise<google.cloud.recaptchaenterprise.v1.IPrivatePasswordLeakVerification> {
      // Build the assessment request.
      const createAssessmentRequest: google.cloud.recaptchaenterprise.v1.ICreateAssessmentRequest =
        {
          parent: `projects/${projectId}`,
          assessment: {
            // Set the hashprefix and credentials hash.
            // Setting this will trigger the Password leak protection.
            privatePasswordLeakVerification: {
              lookupHashPrefix: lookupHashPrefix,
              encryptedUserCredentialsHash: encryptedUserCredentialsHash,
            },
          },
        };
    
      // Send the create assessment request.
      const [response] = await client.createAssessment(createAssessmentRequest);
    
      // Get the reCAPTCHA Enterprise score.
      console.log(`The reCAPTCHA score is: ${response.riskAnalysis?.score}`);
      // Get the assessment name (id). Use this to annotate the assessment.
      console.log(`Assessment name: ${response.name}`);
    
      if (!response?.privatePasswordLeakVerification) {
        throw `Error in obtaining response from Private Password Leak Verification ${response}`;
      }
    
      return response.privatePasswordLeakVerification;
    }
    
    checkPasswordLeak(projectId, username, password).catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
