---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:36.919201+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.8.0/)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.7.0/)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.6.0/)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.5.0/)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.4.0/)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.3.0/)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.2.0/)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.1.0/)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.0.0/)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.9.0/)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.8.0/)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.7.0/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.6.0/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.5.0/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.4.0/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.3.0/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.2.0/)



# Google.Cloud.Speech.V1

`Google.Cloud.Speech.V1` is a.NET client library for the [Google Cloud Speech API](https://cloud.google.com/speech).

Note: This documentation is for version `3.9.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Speech.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

The simplest option is to use the synchronous, one-shot API as shown below in the sample code. More complex scenarios are considered further down this page.

Note that the audio data should be mono rather than stereo, and the format needs to be explicitly specified in the request.

## Sample code

## Constructing a RecognitionAudio object

There are various factory methods on the [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) class to allow instances to be constructed from files, streams, byte arrays and URIs.
    
    
    RecognitionAudio audio1 = RecognitionAudio.FromFile("Sound/SpeechSample.flac");
    RecognitionAudio audio2 = RecognitionAudio.FetchFromUri("https://.../HostedSpeech.flac");
    RecognitionAudio audio3 = RecognitionAudio.FromStorageUri("gs://my-bucket/my-file");
    
    byte[] bytes = ReadAudioData(); // For example, from a database
    RecognitionAudio audio4 = RecognitionAudio.FromBytes(bytes);
    
    using (Stream stream = OpenAudioStream()) // Any regular .NET stream
    {
        RecognitionAudio audio5 = RecognitionAudio.FromStream(stream);
    }
    

## Detect speech in a single file
    
    
    SpeechClient client = SpeechClient.Create();
    RecognitionConfig config = new RecognitionConfig
    {
        Encoding = AudioEncoding.Linear16,
        SampleRateHertz = 16000,
        LanguageCode = LanguageCodes.English.UnitedStates
    };
    RecognizeResponse response = client.Recognize(config, audio);
    Console.WriteLine(response);
    

## Immediate, long-running and streaming operations

The underlying RPC API contains three modes of operation.

The simplest is via the Recognize method. You make a single request, and get a single response with the result of the analysis.

The LongRunningRecognize method still requires all of the audio data to be passed in a single request, but the response from the RPC is a Google.LongRunning.Operation, representing an operation which could take some time to complete. It contains a token which can be used to retrieve the results later - you can think of it as a more persistent and remote `Task<T>` to a first approximation.

Finally, the RPC API supports StreamingRecognize, which is a bidirectional streaming API: the client makes a number of requests, and the server emits a number of responses. This enables a conversation to be transcribed in near real time, for example, without the client needing to split it into chunks for single operations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
