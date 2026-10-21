---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-create-assessment/
title: Create an assessment \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:14.899961+00:00
---

# Create an assessment  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-create-assessment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Create an assessment Stay organized with collections  Save and categorize content based on your preferences. 

Create an assessment to analyze the risk of a user interaction. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create assessments for mobile applications](https://docs.cloud.google.com/recaptcha/docs/create-assessment-mobile)
  * [Create assessments for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)



## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html);
    import com.google.recaptchaenterprise.v1.[CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html);
    import com.google.recaptchaenterprise.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html);
    import com.google.recaptchaenterprise.v1.[RiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.html).[ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html);
    import java.io.IOException;
    
    public class CreateAssessment {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
        String token = "action-token";
        String recaptchaAction = "action-name";
        String userIpAddress = "user-ip-address";
        String userAgent = "user-agent";
        String ja3 = "ja3";
        String ja4 = "ja4";
    
        createAssessment(projectID, recaptchaSiteKey, token, recaptchaAction, userIpAddress, userAgent, ja3, ja4);
      }
    
      /**
       * Create an assessment to analyze the risk of an UI action. Assessment approach is the same for
       * both 'score' and 'checkbox' type recaptcha site keys.
       *
       * @param projectID : GCloud Project ID
       * @param recaptchaSiteKey : Site key obtained by registering a domain/app to use recaptcha
       *     services. (score/ checkbox type)
       * @param token : The token obtained from the client on passing the recaptchaSiteKey.
       * @param recaptchaAction : Action name corresponding to the token.
       * @param userIpAddress: IP address of the user sending a request.
       * @param userAgent: User agent is included in the HTTP request in the request header. 
       * @param ja3: JA3 associated with the request.
       * @param ja4: JA4 associated with the request.
       */
      public static void createAssessment(
          String projectID, String recaptchaSiteKey, String token, String recaptchaAction, String userIpAddress, String userAgent, String ja3, String ja4)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the properties of the event to be tracked.
          [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html) event = [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html).newBuilder()
              .[setSiteKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setSiteKey_java_lang_String_)(recaptchaSiteKey)
              .[setToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setToken_java_lang_String_)(token)
              .[setUserIpAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setUserIpAddress_java_lang_String_)(userIpAddress)
              .[setJa3](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setJa3_java_lang_String_)(ja3)
              .[setJa4](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setJa4_java_lang_String_)(ja4)
              .[setUserAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setUserAgent_java_lang_String_)(userAgent)
              .build();
    
          // Build the assessment request.
          [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html) createAssessmentRequest =
              [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html).newBuilder()
                  .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html).of(projectID).toString())
                  .setAssessment([Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html).newBuilder().[setEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.Builder.html#com_google_recaptchaenterprise_v1_Assessment_Builder_setEvent_com_google_recaptchaenterprise_v1_Event_)(event).build())
                  .build();
    
          [Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html) response = client.createAssessment(createAssessmentRequest);
    
          // Check if the token is valid.
          if (!response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getValid()) {
            System.out.println(
                "The CreateAssessment call failed because the token was: "
                    + response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getInvalidReason().name());
            return;
          }
    
          // Check if the expected action was executed.
          // (If the key is checkbox type and 'action' attribute wasn't set, skip this check.)
          if (!response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getAction().equals(recaptchaAction)) {
            System.out.println(
                "The action attribute in reCAPTCHA tag is: "
                    + response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getAction());
            System.out.println(
                "The action attribute in the reCAPTCHA tag "
                    + "does not match the action ("
                    + recaptchaAction
                    + ") you are expecting to score");
            return;
          }
    
          // Get the reason(s) and the risk score.
          // For more information on interpreting the assessment,
          // see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
          for ([ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html) reason : response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getReasonsList()) {
            System.out.println(reason);
          }
    
          float recaptchaScore = response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getScore();
          System.out.println("The reCAPTCHA score is: " + recaptchaScore);
    
          // Get the assessment name (id). Use this to annotate the assessment.
          String assessmentName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getName__)();
          System.out.println(
              "Assessment name: " + assessmentName.substring(assessmentName.lastIndexOf("/") + 1));
        }
      }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    from google.cloud.recaptchaenterprise_v1 import [Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment.html)
    
    
    def create_assessment(
        project_id: str,
        recaptcha_site_key: str,
        token: str,
        recaptcha_action: str,
        user_ip_address: str,
        user_agent: str,
        ja3: str,
    ) -> Assessment:
        """Create an assessment to analyze the risk of a UI action.
        Args:
            project_id: GCloud Project ID
            recaptcha_site_key: Site key obtained by registering a domain/app to use recaptcha services.
            token: The token obtained from the client on passing the recaptchaSiteKey.
            recaptcha_action: Action name corresponding to the token.
            user_ip_address: IP address of the user sending a request.
            user_agent: User agent is included in the HTTP request in the request header.
            ja3: JA3 associated with the request.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Set the properties of the event to be tracked.
        event = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Event](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event.html)()
        event.site_key = recaptcha_site_key
        event.token = token
        event.user_ip_address = user_ip_address
        event.user_agent = user_agent
        event.ja3 = ja3
    
        assessment = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment.html)()
        assessment.event = event
    
        project_name = f"projects/{project_id}"
    
        # Build the assessment request.
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest.html)()
        request.assessment = assessment
        request.parent = project_name
    
        response = client.[create_assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_assessment)(request)
    
        # Check if the token is valid.
        if not response.token_properties.valid:
            print(
                "The CreateAssessment call failed because the token was "
                + "invalid for for the following reasons: "
                + str(response.token_properties.invalid_reason)
            )
            return
    
        # Check if the expected action was executed.
        if response.token_properties.action != recaptcha_action:
            print(
                "The action attribute in your reCAPTCHA tag does"
                + "not match the action you are expecting to score"
            )
            return
        else:
            # Get the risk score and the reason(s)
            # For more information on interpreting the assessment,
            # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
            for reason in response.risk_analysis.reasons:
                print(reason)
            print(
                "The reCAPTCHA score for this token is: "
                + str(response.risk_analysis.score)
            )
            # Get the assessment name (id). Use this to annotate the assessment.
            assessment_name = client.[parse_assessment_path](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_assessment_path)(response.name).get("assessment")
            print(f"Assessment name: {assessment_name}")
        return response
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Create an assessment to analyze the risk of a UI action.
    #
    # @param site_key [String] Site key obtained by registering a domain/app to use recaptcha services.
    # @param token [String] The token obtained from the client on passing the recaptcha site_key.
    # @param project_id [String] GCloud Project ID.
    # @param recaptcha_action [String] Action name corresponding to the token.
    # @return [void]
    def create_assessment site_key:, token:, project_id:, recaptcha_action:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      request = { parent: "projects/#{project_id}",
                  assessment: {
                    event: {
                      site_key: site_key,
                      token: token
                    }
                  } }
    
      response = client.create_assessment request
    
      # Check if the token is valid.
      if !response.token_properties.valid
        puts "The create_assessment() call failed because the token was invalid with the following reason:" \
             "#{response.token_properties.invalid_reason}"
      # Check if the expected action was executed.
      elsif response.token_properties.action == recaptcha_action
        # Get the risk score and the reason(s).
        # For more information on interpreting the assessment,
        # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
        puts "The reCAPTCHA score for this token is: #{response.risk_analysis.score}"
        response.risk_analysis.reasons.each { |reason| puts reason }
      else
        puts "The action attribute in your reCAPTCHA tag does not match the action you are expecting to score"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
