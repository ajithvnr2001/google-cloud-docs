---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-sync-recognize/
title: Recognize a synchronization request \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:30.821198+00:00
---

# Recognize a synchronization request  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-sync-recognize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Recognize a synchronization request Stay organized with collections  Save and categorize content based on your preferences. 

Loads the audio file from the disk into the request.

## Code sample

### C++

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a Speech client with the default configuration
    auto client = speech::SpeechClient(speech::MakeSpeechConnection());
    // Parse command line arguments.
    auto const args = ParseArguments(argc, argv);
    speech::v1::RecognizeRequest request;
    *request.mutable_config() = args.config;
      // Load the audio file from disk into the request.
      auto content =
          std::string{std::istreambuf_iterator<char>(
                          std::ifstream(args.path, std::ios::binary).rdbuf()),
                      {}};
      request.mutable_audio()->mutable_content()->assign(std::move(content));
    // Send audio content using Recognize().
    auto response = client.Recognize(request);
    if (!response) throw std::move(response).status();
    // Dump the transcript of all the results.
    for (auto const& result : response->results()) {
      for (auto const& alternative : result.alternatives()) {
        std::cout << alternative.confidence() << "\t" << alternative.transcript()
                  << "\n";
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
