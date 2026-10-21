---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-streaming-recognize/
title: Streaming speech recognition \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:55.303803+00:00
---

# Streaming speech recognition  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-streaming-recognize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Streaming speech recognition Stay organized with collections  Save and categorize content based on your preferences. 

Reads and writes audio from a file.

## Code sample

### C++

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace speech = ::google::cloud::speech;
    using RecognizeStream = ::google::cloud::AsyncStreamingReadWriteRpc<
        speech::v1::StreamingRecognizeRequest,
        speech::v1::StreamingRecognizeResponse>;
    
    auto constexpr kUsage = R"""(Usage:
      streaming_transcribe [--bitrate N] audio.(raw|ulaw|flac|amr|awb)
    )""";
    
    // Write the audio in 64k chunks at a time, simulating audio content arriving
    // from a microphone.
    void MicrophoneThreadMain(RecognizeStream& stream,
                              std::string const& file_path) {
      speech::v1::StreamingRecognizeRequest request;
      std::ifstream file_stream(file_path, std::ios::binary);
      auto constexpr kChunkSize = 64 * 1024;
      std::vector<char> chunk(kChunkSize);
      while (true) {
        // Read another chunk from the file.
        file_stream.read(chunk.data(), chunk.size());
        auto const bytes_read = file_stream.gcount();
        // And write the chunk to the stream.
        if (bytes_read > 0) {
          request.set_audio_content(chunk.data(), bytes_read);
          std::cout << "Sending " << bytes_read / 1024 << "k bytes." << std::endl;
          if (!stream.Write(request, grpc::WriteOptions()).get()) break;
        }
        if (!file_stream) {
          // Done reading everything from the file, so done writing to the stream.
          stream.WritesDone().get();
          break;
        }
        // Wait a second before writing the next chunk.
        std::this_thread::sleep_for(std::chrono::seconds(1));
      }
    }
    
    int main(int argc, char** argv) try {
      // Create a Speech client with the default configuration
      auto client = speech::SpeechClient(speech::MakeSpeechConnection());
    
      // Parse command line arguments.
      auto args = ParseArguments(argc, argv);
      auto const file_path = args.path;
    
      speech::v1::StreamingRecognizeRequest request;
      auto& streaming_config = *request.mutable_streaming_config();
      *streaming_config.mutable_config() = args.config;
    
      // Begin a stream.
      auto stream = client.AsyncStreamingRecognize();
      // The stream can fail to start, and `.get()` returns an error in this case.
      if (!stream->Start().get()) throw stream->Finish().get();
      // Write the first request, containing the config only.
      if (!stream->Write(request, grpc::WriteOptions{}).get()) {
        // Write().get() returns false if the stream is closed.
        throw stream->Finish().get();
      }
    
      // Simulate a microphone thread using the file as input.
      auto microphone =
          std::thread(MicrophoneThreadMain, std::ref(*stream), file_path);
      // Read responses.
      auto read = [&stream] { return stream->Read().get(); };
      for (auto response = read(); response.has_value(); response = read()) {
        // Dump the transcript of all the results.
        for (auto const& result : response->results()) {
          std::cout << "Result stability: " << result.stability() << "\n";
          for (auto const& alternative : result.alternatives()) {
            std::cout << alternative.confidence() << "\t"
                      << alternative.transcript() << "\n";
          }
        }
      }
      auto status = stream->Finish().get();
      microphone.join();
      if (!status.ok()) throw status;
      return 0;
    } catch (google::cloud::Status const& s) {
      std::cerr << "Recognize stream finished with an error: " << s << "\n";
      return 1;
    } catch (std::exception const& ex) {
      std::cerr << "Standard C++ exception thrown: " << ex.what() << "\n"
                << kUsage << "\n";
      return 1;
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
