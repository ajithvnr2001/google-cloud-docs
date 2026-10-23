---
url: https://docs.cloud.google.com/vision-ai/docs/use-cloud-functions/
title: Add processing logic using Cloud Run functions \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:35.165059+00:00
---

# Add processing logic using Cloud Run functions  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/use-cloud-functions/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Add processing logic using Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Run functions you can further process output data from Vertex AI custom-trained model and BigQuery app nodes. You can use these integrations with app nodes in the following ways:

  * **Vertex AI custom model** node: Use Cloud Run functions to post-process prediction results from the original Vertex AI custom model.
  * **BigQuery** node: Use Cloud Run functions to generate customized BigQuery rows with the original annotations.



All the Cloud Run functions you use with App Platform must meet the following requirements:

  * Cloud Run functions must provide the [Http trigger](https://docs.cloud.google.com/functions/docs/calling/http).
  * Cloud Run functions must receive a [`AppPlatformCloudFunctionRequest`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#appplatformcloudfunctionrequest) JSON string, and must return a [`AppPlatformCloudFunctionResponse`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#appplatformcloudfunctionresponse) JSON string back.
  * The annotation payload schema stored in the request _and_ the response must follow the specification of the target model.



#### API definitions: `AppPlatformMetadata`, `AppPlatformCloudFunctionRequest`, `AppPlatformCloudFunctionResponse`
    
    
    // Message of essential metadata of App Platform.
    // This message is usually attached to a certain model output annotation for
    // customer to identify the source of the data.
    message AppPlatformMetadata {
      // The application resource name.
      string application = 1;
      // The instance resource id. Instance is the nested resource of application
      // under collection 'instances'.
      string instance_id = 2;
      // The node name of the application graph.
      string node = 3;
      // The referred model resource name of the application node.
      string processor = 4;
    }
    
    // For any Cloud Run function based customer processing logic, customer's cloud
    // function is expected to receive AppPlatformCloudFunctionRequest as request
    // and send back AppPlatformCloudFunctionResponse as response.
    // Message of request from AppPlatform to Cloud Run functions.
    message AppPlatformCloudFunctionRequest {
      // The metadata of the AppPlatform for customer to identify the source of the
      // payload.
      AppPlatformMetadata app_platform_metadata = 1;
      // A general annotation message that uses struct format to represent different
      // concrete annotation protobufs.
      message StructedInputAnnotation {
        // The ingestion time of the current annotation.
        int64 ingestion_time_micros = 1;
        // The struct format of the actual annotation.
        protobuf.Struct annotation = 2;
      }
      // The actual annotations to be processed by the customized Cloud Run function.
      repeated StructedInputAnnotation annotations = 2;
    }
    
    // Message of the response from customer's Cloud Run function to AppPlatform.
    message AppPlatformCloudFunctionResponse {
      // A general annotation message that uses struct format to represent different
      // concrete annotation protobufs.
      message StructedOutputAnnotation {
        // The struct format of the actual annotation.
        protobuf.Struct annotation = 1;
      }
    
      // The modified annotations that is returned back to AppPlatform.
      // If the annotations fields are empty, then those annotations will be dropped
      // by AppPlatform.
      repeated StructedOutputAnnotation annotations = 2;
    }

### Sample usage

Use the following code to post-process Vertex AI custom-trained model annotations and replace annotations with a constant key-value pair.

### Python
    
    
    import functions_framework
    from flask import jsonify
    
    @functions_framework.http
    def hello_http(request):
       request_json = request.get_json(silent=True)
       request_args = request.args
    
       if request_json and 'annotations' in request_json:
           annotations = []
           for ele in request_json['annotations']:
               for k, v in ele.items():
                   if k == "annotation":
                    if "predictions" in v:
                        # Replace the annotation.
                        v["predictions"][0] = {"user": "googler"}
                        annotations.append({"annotation" : v})
       else:
           annotations = 'Failure'
       return jsonify(annotations=annotations)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
