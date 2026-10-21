---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming/
title: Transcribe a streaming feed on a local file \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:54.833771+00:00
---

# Transcribe a streaming feed on a local file  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a streaming feed on a local file Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a streaming audio feed from a microphone on a local file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe audio from streaming input](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-streaming-audio)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"path/filepath"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    func main() {
    	flag.Usage = func() {
    		fmt.Fprintf(os.Stderr, "Usage: %s <AUDIOFILE>\n", filepath.Base(os.Args[0]))
    		fmt.Fprintf(os.Stderr, "<AUDIOFILE> must be a path to a local audio file. Audio file must be a 16-bit signed little-endian encoded with a sample rate of 16000.\n")
    
    	}
    	flag.Parse()
    	if len(flag.Args()) != 1 {
    		log.Fatal("Please pass path to your local audio file as a command line argument")
    	}
    	audioFile := flag.Arg(0)
    
    	ctx := context.Background()
    
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatal(err)
    	}
    	stream, err := client.StreamingRecognize(ctx)
    	if err != nil {
    		log.Fatal(err)
    	}
    	// Send the initial configuration message.
    	if err := stream.Send(&speechpb.StreamingRecognizeRequest{
    		StreamingRequest: &speechpb.StreamingRecognizeRequest_StreamingConfig{
    			StreamingConfig: &speechpb.StreamingRecognitionConfig{
    				Config: &speechpb.RecognitionConfig{
    					Encoding:        speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    					SampleRateHertz: 16000,
    					LanguageCode:    "en-US",
    				},
    			},
    		},
    	}); err != nil {
    		log.Fatal(err)
    	}
    
    	f, err := os.Open(audioFile)
    	if err != nil {
    		log.Fatal(err)
    	}
    	defer f.Close()
    
    	go func() {
    		buf := make([]byte, 1024)
    		for {
    			n, err := f.Read(buf)
    			if n > 0 {
    				if err := stream.Send(&speechpb.StreamingRecognizeRequest{
    					StreamingRequest: &speechpb.StreamingRecognizeRequest_AudioContent{
    						AudioContent: buf[:n],
    					},
    				}); err != nil {
    					log.Printf("Could not send audio: %v", err)
    				}
    			}
    			if err == io.EOF {
    				// Nothing else to pipe, close the stream.
    				if err := stream.CloseSend(); err != nil {
    					log.Fatalf("Could not close stream: %v", err)
    				}
    				return
    			}
    			if err != nil {
    				log.Printf("Could not read from %s: %v", audioFile, err)
    				continue
    			}
    		}
    	}()
    
    	for {
    		resp, err := stream.Recv()
    		if err == io.EOF {
    			break
    		}
    		if err != nil {
    			log.Fatalf("Cannot stream results: %v", err)
    		}
    		if err := resp.Error; err != nil {
    			log.Fatalf("Could not recognize: %v", err)
    		}
    		for _, result := range resp.Results {
    			fmt.Printf("Result: %+v\n", result)
    		}
    	}
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs streaming speech recognition on raw PCM audio data.
     *
     * @param fileName the path to a PCM audio file to transcribe.
     */
    public static void streamingRecognizeFile(String fileName) throws Exception, IOException {
      Path path = Paths.get(fileName);
      byte[] data = Files.readAllBytes(path);
    
      // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
      try (SpeechClient speech = SpeechClient.create()) {
    
        // Configure request with local raw PCM audio
        RecognitionConfig recConfig =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .setModel("default")
                .build();
        StreamingRecognitionConfig config =
            StreamingRecognitionConfig.newBuilder().setConfig(recConfig).build();
    
        class ResponseApiStreamingObserver<T> implements ApiStreamObserver<T> {
          private final SettableFuture<List<T>> future = SettableFuture.create();
          private final List<T> messages = new java.util.ArrayList<T>();
    
          @Override
          public void onNext(T message) {
            messages.add(message);
          }
    
          @Override
          public void onError(Throwable t) {
            future.setException(t);
          }
    
          @Override
          public void onCompleted() {
            future.set(messages);
          }
    
          // Returns the SettableFuture object to get received messages / exceptions.
          public SettableFuture<List<T>> future() {
            return future;
          }
        }
    
        ResponseApiStreamingObserver<StreamingRecognizeResponse> responseObserver =
            new ResponseApiStreamingObserver<>();
    
        BidiStreamingCallable<StreamingRecognizeRequest, StreamingRecognizeResponse> callable =
            speech.streamingRecognizeCallable();
    
        ApiStreamObserver<StreamingRecognizeRequest> requestObserver =
            callable.bidiStreamingCall(responseObserver);
    
        // The first request must **only** contain the audio configuration:
        requestObserver.onNext(
            StreamingRecognizeRequest.newBuilder().setStreamingConfig(config).build());
    
        // Subsequent requests must **only** contain the audio data.
        requestObserver.onNext(
            StreamingRecognizeRequest.newBuilder()
                .setAudioContent(ByteString.copyFrom(data))
                .build());
    
        // Mark transmission as completed after sending the data.
        requestObserver.onCompleted();
    
        List<StreamingRecognizeResponse> responses = responseObserver.future().get();
    
        for (StreamingRecognizeResponse response : responses) {
          // For streaming recognize, the results list has one is_final result (if available) followed
          // by a number of in-progress results (if iterim_results is true) for subsequent utterances.
          // Just print the first result here.
          StreamingRecognitionResult result = response.getResultsList().get(0);
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
          System.out.printf("Transcript : %s\n", alternative.getTranscript());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const request = {
      config: {
        encoding: encoding,
        sampleRateHertz: sampleRateHertz,
        languageCode: languageCode,
      },
      interimResults: false, // If you want interim results, set this to true
    };
    
    // Stream the audio to the Google Cloud Speech API
    const recognizeStream = client
      .streamingRecognize(request)
      .on('error', console.error)
      .on('data', data => {
        console.log(
          `Transcription: ${data.results[0].alternatives[0].transcript}`
        );
      });
    
    // Stream an audio file from disk to the Speech API, e.g. "./resources/audio.raw"
    fs.createReadStream(filename).pipe(recognizeStream);

### PHP

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Speech\V2\Client\SpeechClient;
    use Google\Cloud\Speech\V2\StreamingRecognizeRequest;
    use Google\Cloud\Speech\V2\RecognitionFeatures;
    use Google\Cloud\Speech\V2\AutoDetectDecodingConfig;
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\StreamingRecognitionConfig;
    
    /**
     * @param string $projectId The Google Cloud project ID.
     * @param string $location The location of the recognizer.
     * @param string $recognizerId The ID of the recognizer to use.
     * @param string $audioFile path to an audio file.
     */
    function streaming_recognize(string $projectId, string $location, string $recognizerId, string $audioFile)
    {
        // create the speech client
        $apiEndpoint = $location === 'global' ? null : sprintf('%s-speech.googleapis.com', $location);
        $speech = new SpeechClient(['apiEndpoint' => $apiEndpoint]);
    
        $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    
        // set streaming config
        $features = new RecognitionFeatures([
            'enable_automatic_punctuation' => true
        ]);
        $streamingConfig = (new StreamingRecognitionConfig())
            ->setConfig(new RecognitionConfig([
                // Can also use {@see Google\Cloud\Speech\V2\ExplicitDecodingConfig}
                'auto_decoding_config' => new AutoDetectDecodingConfig(),
                'features' => $features
            ]));
        $streamingRequest = (new StreamingRecognizeRequest())
            ->setRecognizer($recognizerName)
            ->setStreamingConfig($streamingConfig);
    
        // set the streaming request
        $stream = $speech->streamingRecognize();
        $stream->write($streamingRequest);
    
        // stream the audio file
        $handle = fopen($audioFile, 'r');
        while (!feof($handle)) {
            $chunk = fread($handle, 4096);
            $streamingRequest = (new StreamingRecognizeRequest())
                ->setAudio($chunk);
            $stream->write($streamingRequest);
        }
        fclose($handle);
    
        // read the responses
        foreach ($stream->closeWriteAndReadAll() as $response) {
            // an empty response indicates the end of the stream
            if (!$response->getResults()) {
                continue;
            }
    
            // process the results
            foreach ($response->getResults() as $result) {
                printf(
                    'Transcript: "%s"' . PHP_EOL,
                    $result->getAlternatives()[0]->getTranscript()
                );
            }
        }
    }

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def transcribe_streaming(stream_file: str) -> speech.RecognitionConfig:
        """Streams transcription of the given audio file using Google Cloud Speech-to-Text API.
        Args:
            stream_file (str): Path to the local audio file to be transcribed.
                Example: "resources/audio.raw"
        """
        client = speech.SpeechClient()
    
        with open(stream_file, "rb") as audio_file:
            audio_content = audio_file.read()
    
        # In practice, stream should be a generator yielding chunks of audio data.
        stream = [audio_content]
    
        requests = (
            speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
        )
    
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
    
        streaming_config = speech.StreamingRecognitionConfig(config=config)
    
        # streaming_recognize returns a generator.
        responses = client.streaming_recognize(
            config=streaming_config,
            requests=requests,
        )
    
        for response in responses:
            # Once the transcription has settled, the first result will contain the
            # is_final result. The other results will be for subsequent portions of
            # the audio.
            for result in response.results:
                print(f"Finished: {result.is_final}")
                print(f"Stability: {result.stability}")
                alternatives = result.alternatives
                # The alternatives are ordered from most likely to least.
                for alternative in alternatives:
                    print(f"Confidence: {alternative.confidence}")
                    print(f"Transcript: {alternative.transcript}")
    
    
    

### Ruby

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # audio_file_path = "Path to file on which to perform speech recognition"
    
    require "google/cloud/speech"
    
    speech = Google::Cloud::[Speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html).[speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html) version: :v1
    
    audio_content = File.binread audio_file_path
    bytes_total   = audio_content.size
    bytes_sent    = 0
    chunk_size    = 32_000
    
    input_stream = Gapic::StreamInput.new
    output_stream = speech.streaming_recognize input_stream
    
    config = {
      config: {
        encoding:                 :LINEAR16,
        sample_rate_hertz:        16_000,
        language_code:            "en-US",
        enable_word_time_offsets: true
      }
    }
    input_stream.push streaming_config: config
    
    # Simulated streaming from a microphone
    # Stream bytes...
    while bytes_sent < bytes_total
      input_stream.push audio_content: audio_content[bytes_sent, chunk_size]
      bytes_sent += chunk_size
      sleep 1
    end
    
    puts "Stopped passing"
    input_stream.close
    
    results = output_stream
    
    results.each do |result|
      puts "Transcript: #{result}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
