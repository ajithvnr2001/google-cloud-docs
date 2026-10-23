---
url: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-submit-uri/
title: Submit a URI \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:17.278208+00:00
---

# Submit a URI  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-submit-uri/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Samples ](https://docs.cloud.google.com/web-risk/docs/samples)



#  Submit a URI Stay organized with collections  Save and categorize content based on your preferences. 

Create a Webrisk client and submit a URI.

## Code sample

### Java

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.webrisk.v1.[WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.webrisk.v1.[Submission](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.Submission.html);
    import com.google.webrisk.v1.[SubmitUriRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SubmitUriRequest.html);
    import com.google.webrisk.v1.[ThreatDiscovery](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.html);
    import com.google.webrisk.v1.[ThreatDiscovery](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.html).[Platform](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.Platform.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).[AbuseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.AbuseType.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).[Confidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).[Confidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.html).[ConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.ConfidenceLevel.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).[ThreatJustification](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.html);
    import com.google.webrisk.v1.[ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).[ThreatJustification](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.html).[JustificationLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.JustificationLabel.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubmitUri {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The name of the project that is making the submission.
        String projectId = "GOOGLE_CLOUD_PROJECT";
        // The URI that is being reported for malicious content to be analyzed.
        String uri = "http://testsafebrowsing.appspot.com/s/malware.html";
    
        submitUri(projectId, uri);
      }
    
      // Submits a URI suspected of containing malicious content to be reviewed. Returns a
      // google.longrunning.Operation which, once the review is complete, is updated with its result.
      // You can use the [Pub/Sub API] (https://cloud.google.com/pubsub) to receive notifications for
      // the returned Operation.
      // If the result verifies the existence of malicious content, the site will be added to the
      // Google's Social Engineering lists in order to protect users that could get exposed to this
      // threat in the future. Only allow-listed projects can use this method during Early Access.
      public static void submitUri(String projectId, String uri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html) webRiskServiceClient = [WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html).create()) {
    
          // Set the URI to be submitted.
          [Submission](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.Submission.html) submission = [Submission](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.Submission.html).newBuilder()
              .setUri(uri)
              .build();
    
          // Set the context about the submission including the type of abuse found on the URI and
          // supporting details.
          [ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html) threatInfo = [ThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.html).newBuilder()
              // The abuse type found on the URI.
              .[setAbuseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Builder.html#com_google_webrisk_v1_ThreatInfo_Builder_setAbuseType_com_google_webrisk_v1_ThreatInfo_AbuseType_)([AbuseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.AbuseType.html).SOCIAL_ENGINEERING)
              // Confidence that a URI is unsafe.
              .[setThreatConfidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Builder.html#com_google_webrisk_v1_ThreatInfo_Builder_setThreatConfidence_com_google_webrisk_v1_ThreatInfo_Confidence_)([Confidence](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.html).newBuilder()
                  .[setLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.Builder.html#com_google_webrisk_v1_ThreatInfo_Confidence_Builder_setLevel_com_google_webrisk_v1_ThreatInfo_Confidence_ConfidenceLevel_)([ConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Confidence.ConfidenceLevel.html).MEDIUM)
                  .build())
              // Context about why the URI is unsafe.
              .[setThreatJustification](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.Builder.html#com_google_webrisk_v1_ThreatInfo_Builder_setThreatJustification_com_google_webrisk_v1_ThreatInfo_ThreatJustification_)([ThreatJustification](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.html).newBuilder()
                  // Labels that explain how the URI was classified.
                  .[addLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.Builder.html#com_google_webrisk_v1_ThreatInfo_ThreatJustification_Builder_addLabels_com_google_webrisk_v1_ThreatInfo_ThreatJustification_JustificationLabel_)([JustificationLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.JustificationLabel.html).AUTOMATED_REPORT)
                  // Free-form context on why this URI is unsafe.
                  .[addComments](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatInfo.ThreatJustification.Builder.html#com_google_webrisk_v1_ThreatInfo_ThreatJustification_Builder_addComments_java_lang_String_)("Testing Submission")
                  .build())
              .build();
    
          // Set the details about how the threat was discovered.
          [ThreatDiscovery](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.html) threatDiscovery = [ThreatDiscovery](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.html).newBuilder()
              // Platform on which the threat was discovered.
              .[setPlatform](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.Builder.html#com_google_webrisk_v1_ThreatDiscovery_Builder_setPlatform_com_google_webrisk_v1_ThreatDiscovery_Platform_)([Platform](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.Platform.html).MACOS)
              // CLDR region code of the countries/regions the URI poses a threat ordered
              // from most impact to least impact. Example: "US" for United States.
              .[addRegionCodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatDiscovery.Builder.html#com_google_webrisk_v1_ThreatDiscovery_Builder_addRegionCodes_java_lang_String_)("US")
              .build();
    
          [SubmitUriRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SubmitUriRequest.html) submitUriRequest = [SubmitUriRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SubmitUriRequest.html).newBuilder()
              .setParent(String.[format](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ProjectName.html#com_google_webrisk_v1_ProjectName_format_java_lang_String_)("projects/%s", projectId))
              .setSubmission(submission)
              .[setThreatInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SubmitUriRequest.Builder.html#com_google_webrisk_v1_SubmitUriRequest_Builder_setThreatInfo_com_google_webrisk_v1_ThreatInfo_)(threatInfo)
              .[setThreatDiscovery](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SubmitUriRequest.Builder.html#com_google_webrisk_v1_SubmitUriRequest_Builder_setThreatDiscovery_com_google_webrisk_v1_ThreatDiscovery_)(threatDiscovery)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) submissionResponse = webRiskServiceClient.[submitUriCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html#com_google_cloud_webrisk_v1_WebRiskServiceClient_submitUriCallable__)()
              .futureCall(submitUriRequest)
              .get(30, TimeUnit.SECONDS);
    
          System.out.println("Submission response: " + submissionResponse);
        }
      }
    }

### Python

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.operation import Operation
    from google.cloud import [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest)
    
    
    def submit_uri(project_id: str, uri: str) -> Operation:
        """Submits a URI suspected of containing malicious content to be reviewed.
    
        Returns a google.longrunning.Operation which, once the review is complete, is updated with its result.
        You can use the [Pub/Sub API] (https://cloud.google.com/pubsub) to receive notifications for the
        returned Operation.
        If the result verifies the existence of malicious content, the site will be added to the
        Google's Social Engineering lists in order to protect users that could get exposed to this
        threat in the future. Only allow-listed projects can use this method during Early Access.
    
         Args:
             project_id: The name of the project that is making the submission.
             uri: The URI that is being reported for malicious content to be analyzed.
                 uri = "http://testsafebrowsing.appspot.com/s/malware.html"
    
        Returns:
            A Long Running Operation ID similar to `projects/1234/operations/5678`.
        """
        webrisk_client = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[WebRiskServiceClient](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html)()
    
        # Set the URI to be submitted.
        submission = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[Submission](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.Submission.html)()
        submission.uri = uri
    
        # Confidence that a URI is unsafe.
        threat_confidence = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatInfo](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.html).[Confidence](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.Confidence.html)(
            level=[webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatInfo](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.html).[Confidence](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.Confidence.html).[ConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.Confidence.ConfidenceLevel.html).MEDIUM
        )
    
        # Context about why the URI is unsafe.
        threat_justification = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatInfo](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.html).[ThreatJustification](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.ThreatJustification.html)(
            # Labels that explain how the URI was classified.
            labels=[
                [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatInfo](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.html).[ThreatJustification](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.ThreatJustification.html).[JustificationLabel](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.ThreatJustification.JustificationLabel.html).AUTOMATED_REPORT
            ],
            # Free-form context on why this URI is unsafe.
            comments=["Testing submission"],
        )
    
        # Set the context about the submission including the type of abuse found on the URI and
        # supporting details.
        threat_info = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatInfo](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatInfo.html)(
            # The abuse type found on the URI.
            abuse_type=[webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[types](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.html).[ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatType.html).SOCIAL_ENGINEERING,
            threat_confidence=threat_confidence,
            threat_justification=threat_justification,
        )
    
        # Set the details about how the threat was discovered.
        threat_discovery = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatDiscovery](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatDiscovery.html)(
            # Platform on which the threat was discovered.
            platform=[webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatDiscovery](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatDiscovery.html).[Platform](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatDiscovery.Platform.html).MACOS,
            # CLDR region code of the countries/regions the URI poses a threat ordered
            # from most impact to least impact. Example: "US" for United States.
            region_codes=["US"],
        )
    
        request = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[SubmitUriRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.SubmitUriRequest.html)(
            parent=f"projects/{project_id}",
            submission=submission,
            threat_info=threat_info,
            threat_discovery=threat_discovery,
        )
    
        response = webrisk_client.[submit_uri](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html#google_cloud_webrisk_v1_services_web_risk_service_WebRiskServiceClient_submit_uri)(request)
        return response.operation
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=webrisk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
