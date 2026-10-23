---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-annotate-account-defender-assessment/
title: Annotate assessment with account-related metadata \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:15.669334+00:00
---

# Annotate assessment with account-related metadata  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-annotate-account-defender-assessment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Annotate assessment with account-related metadata Stay organized with collections  Save and categorize content based on your preferences. 

Annotate assessment with account-related metadata to provide feedback on the accuracy of the reCAPTCHA Enterprise's analysis. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect and prevent account-related fraudulent activities on mobile applications](https://docs.cloud.google.com/recaptcha/docs/account-defender-mobile)
  * [Detect and prevent account-related fraudulent activities on websites](https://docs.cloud.google.com/recaptcha/docs/account-defender)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
