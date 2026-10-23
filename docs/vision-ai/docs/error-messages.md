---
url: https://docs.cloud.google.com/vision-ai/docs/error-messages/
title: Error messages \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:56.254366+00:00
---

# Error messages  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/error-messages/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to resolve some errors raised by Agent Platform Vision. This topic discusses errors whose resolutions require more steps than can be easily described in an error message.

See the [Cloud API documentation](https://docs.cloud.google.com/apis/design/errors#handling_errors) for recommended practices of error handling.

## Permissions

### Application default credentials are not available

If you receive this message:
    
    
    The Application Default Credentials are not available. They are
    available if running in Google Compute Engine. Otherwise, the
    environment variable GOOGLE_APPLICATION_CREDENTIALS must be defined
    pointing to a file defining the credentials.
    See https://developers.google.com/accounts/docs/application-default-credentials
    for more information.
    

### Permission denied

If you receive this message:
    
    
    ERROR: (gcloud.auth.application-default.print-access-token) File /path/to/key.json
    (pointed by GOOGLE_APPLICATION_CREDENTIALS environment variable) does not exist!
    {
      "error": {
        "code": 403,
        "message": "The request is missing a valid API key.",
        "status": "PERMISSION_DENIED"
      }
    }
    

Verify that you have a valid service account key JSON file in the location stored in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable and that the variable points to the correct place.

To diagnose this error, try opening the service account key file from the folder from which you're attempting to call the Gemini Enterprise Agent Platform Vision API.
    
    
    cat $GOOGLE_APPLICATION_CREDENTIALS
    

### Forbidden: 403 POST API has not been used or is disabled

If you receive the message: 
    
    
    Forbidden: 403 POST Gemini Enterprise Agent Platform Vision API has not been used in
    project # before or it is disabled.
    Enable it by visitng [url] then retry.
    If you enabled this API recently, wait a few minutes for the action to
    propagate and retry.
    

  1. Visit the link specified in the error message and enable the Agent Platform Vision API. Wait several minutes and then retry.
  2. Verify that you have a valid service account key JSON file stored in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. To diagnose this error, try opening the service account key file from the folder from which you're attempting to call the Gemini Enterprise Agent Platform Vision API. 
         
         cat $GOOGLE_APPLICATION_CREDENTIALS
         




## Invalid arguments

### API version unsupported

Example: when a request is made to an API version which does not support the operation.
    
    
    message: "The requested operation is unsupported for the API version."
    

### Bad Request

When an API request is made but the request fields have one or more violations. Each violation is captured as a `field_violations` in the `google.rpc.BadRequest` details.
    
    
    message: "Request contains an invalid argument."
    details {
      [type.googleapis.com/google.rpc.BadRequest] {
        field_violations { field: "foo" description: "bar" }
      }
    }
    

### Invalid Project Number

When an invalid project number is provided. Example project number: 848757893952147483648.
    
    
    message: "Invalid project number used: 848757893952147483648."
    details {
        [type.googleapis.com/google.rpc.ErrorInfo] {
          reason: "INVALID_PROJECT_NUMBER"
          domain: "visionai.googleapis.com"
        }
    }
    

### Invalid Resource Format

When a resource format is invalid. Example project number: 1234 and Example location ID: us-central1.
    
    
    message: "Invalid Resource Used: project/1234/location/us-central1. Valid format should be "
    "projects/{project_number}/locations/{location_id}."
    details {
        [type.googleapis.com/google.rpc.ErrorInfo] {
          reason: "INVALID_RESOURCE_FORMAT"
          domain: "visionai.googleapis.com"
        }
    }
    

## Failed Precondition

### Missing Video Data

Some APIs (such as CreateAnnotation for a partition level annotation), it is required for the asset to already have video data streamed in to infer the asset's start time. Otherwise the following error will be triggered.
    
    
    message: "Asset doesn't have start time inferred yet. Should ingest asset and retry."
    details {
        [type.googleapis.com/google.rpc.ErrorInfo] {
          reason: "FAILED_PRECONDITION"
          domain: "visionai.googleapis.com"
        }
    }
    

## Quotas and limits

### Quota exceeded

If you receive this message:
    
    
    RESOURCE_EXHAUSTED: Quota exceeded.
    

You have reached the limit of your per-minute or daily quota. Review the [quotas & limits](https://docs.cloud.google.com/vision-ai/quotas) for using Agent Platform Vision.

You can request an increase to your quotas from the [Google Cloud console](https://console.cloud.google.com/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
