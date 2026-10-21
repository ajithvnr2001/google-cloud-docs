---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/error-messages/
title: Error messages \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:02.111213+00:00
---

# Error messages  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/error-messages/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses Cloud Speech-to-Text errors whose resolutions require more steps than can be described in an error message.

## "The Application Default Credentials are not available"

If you receive this message:
    
    
    The Application Default Credentials are not available. They are
    available if running in Google Compute Engine. Otherwise, the
    environment variable GOOGLE_APPLICATION_CREDENTIALS must be defined
    pointing to a file defining the credentials.
    See https://developers.google.com/accounts/docs/application-default-credentials
    for more information.
    

Cloud STT uses [_Application Default Credentials_](https://docs.cloud.google.com/accounts/docs/application-default-credentials) (ADC) for authentication. 

The credentials for ADC must be available within the context that you call the Cloud Speech-to-Text API. For example, if you set up ADC in your terminal but run your code in the debugger of your IDE, the execution context of your code might not have access to the credentials. In that case, your request to Cloud STT might fail. 

To learn how to provide credentials to ADC, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc). 

## "File ... (pointed by GOOGLE_APPLICATION_CREDENTIALS environment variable) does not exist!"

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

To diagnose this error, try opening the service account key file from the folder from which you're attempting to call the Cloud Speech-to-Text API.
    
    
    cat $GOOGLE_APPLICATION_CREDENTIALS
    

## Forbidden: 403 POST API has not been used or is disabled

If you receive the message: 
    
    
    Forbidden: 403 POST Cloud Speech-to-Text API has not been used in
    project # before or it is disabled.
    Enable it by visiting [url] then retry.
    If you enabled this API recently, wait a few minutes for the action to
    propagate to our systems and retry.
    

  1. Visit the link specified in the error message and enable the Cloud STT API. Wait several minutes and then retry.
  2. Verify that you have a valid service account key JSON file stored in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. To diagnose this error, try opening the service account key file from the folder from which you're attempting to call the Cloud Speech-to-Text API.


    
    
    cat $GOOGLE_APPLICATION_CREDENTIALS
    

## "Must use single channel (mono) audio"

If you receive this message:
    
    
    Must use single channel (mono) audio, but WAV header indicates 2
    channels.
    

Your audio file contains more than one channel. To transcribe this audio file, you must declare that your audio has [multiple channels](https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel).

## "Must use 16 bit samples for LINEAR_PCM"

If you receive this message:
    
    
    INVALID_ARGUMENT: Must use 16 bit samples for LINEAR_PCM, but the WAV
    header indicates 8 bits per sample
    

You might need to change the encoding that you've specified in your [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig#AudioEncoding). To read about supported encodings in Cloud STT, see the [encodings](https://docs.cloud.google.com/speech-to-text/docs/v1/encoding) guide.

## "Sync input too long"

If you receive this message:
    
    
    Sync input too long. For audio longer than 1 min use
    LongRunningRecognize with a 'uri' parameter.
    

The [synchronous recognize](https://docs.cloud.google.com/speech-to-text/docs/v1/sync-recognize) method for Cloud STT only supports transcribing audio data up to 1 minute in length. For longer audio data, use [asynchronous recognize](https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize) instead.

## "Invalid recognition 'config': bad encoding"

If you receive this message:
    
    
    Invalid recognition 'config': bad encoding.
    

Your audio data might not be encoded correctly or is encoded with a codec different than what you've declared in the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig). Check the audio input and make sure that you've set the `encoding` field correctly.

## "Request payload size exceeds the limit"

If you receive either of these messages:
    
    
    Request payload size exceeds the limit.
    
    
    
    Inline audio exceeds duration limit. Please use a GCS URI.
    

You have exceeded the 10 MB size limit for a single request sent to the API using a local file. You can move your audio file to a Cloud Storage bucket to avoid the 10 MB limit. See the [quotas & limits](https://docs.cloud.google.com/speech-to-text/docs/v1/quotas) page for more information.

## "Quota exceeded"

If you receive this message:
    
    
    RESOURCE_EXHAUSTED: Quota exceeded.
    

You have reached the limit of your per-minute or daily quota. Review the [quotas & limits](https://docs.cloud.google.com/speech-to-text/docs/v1/quotas) for using Cloud STT.

You can request an increase to your quotas from the [Google Cloud console](https://console.cloud.google.com/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
