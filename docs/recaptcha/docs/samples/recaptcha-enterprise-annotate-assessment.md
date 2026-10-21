---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-annotate-assessment/
title: Annotate an assessment \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:14.808509+00:00
---

# Annotate an assessment  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-annotate-assessment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Annotate an assessment Stay organized with collections  Save and categorize content based on your preferences. 

Annotate an assessment to provide feedback on the correctness of the analysis made by reCAPTCHA Enterprise. 

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Annotation.html);
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).Reason;
    import com.google.recaptchaenterprise.v1.[AnnotateAssessmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentResponse.html);
    import com.google.recaptchaenterprise.v1.[AssessmentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentName.html);
    import java.io.IOException;
    
    public class AnnotateAssessment {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "project-id";
        String assessmentId = "assessment-id";
        annotateAssessment(projectID, assessmentId);
      }
    
      /**
       * Pre-requisite: Create an assessment before annotating.
       *
       * <p>Annotate an assessment to provide feedback on the correctness of recaptcha prediction.
       *
       * @param projectID: GCloud Project id
       * @param assessmentId: Value of the 'name' field returned from the CreateAssessment call.
       */
      public static void annotateAssessment(String projectID, String assessmentId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
          // Build the annotation request.
          // For more info on when/how to annotate, see:
          // https://cloud.google.com/recaptcha-enterprise/docs/annotate-assessment#when_to_annotate
          [AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html) annotateAssessmentRequest =
              [AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.html).newBuilder()
                  .setName([AssessmentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AssessmentName.html).of(projectID, assessmentId).toString())
                  .[setAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Builder.html#com_google_recaptchaenterprise_v1_AnnotateAssessmentRequest_Builder_setAnnotation_com_google_recaptchaenterprise_v1_AnnotateAssessmentRequest_Annotation_)([Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Annotation.html).FRAUDULENT)
                  .addReasons(Reason.FAILED_TWO_FACTOR)
                  .build();
    
          // Empty response is sent back.
          [AnnotateAssessmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentResponse.html) response = client.annotateAssessment(annotateAssessmentRequest);
          System.out.println("Annotated response sent successfully ! " + response);
        }
      }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def annotate_assessment(project_id: str, assessment_id: str) -> None:
        """Pre-requisite: Create an assessment before annotating.
            Annotate an assessment to provide feedback on the correctness of recaptcha prediction.
        Args:
            project_id: Google Cloud Project ID
            assessment_id: Value of the 'name' field returned from the create_assessment() call.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        assessment_name = f"projects/{project_id}/assessments/{assessment_id}"
        # Build the annotation request.
        # For more info on when/how to annotate, see:
        # https://cloud.google.com/recaptcha-enterprise/docs/annotate-assessment#when_to_annotate
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[AnnotateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.html)()
        request.name = assessment_name
        request.annotation = request.[Annotation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation.html).FRAUDULENT
        request.reasons = [request.Reason.FAILED_TWO_FACTOR]
    
        # Empty response is sent back.
        client.[annotate_assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_annotate_assessment)(request)
        print("Annotated response sent successfully ! ")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
