---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-mic/
title: Transcribe streaming audio from a microphone \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:51.480998+00:00
---

# Transcribe streaming audio from a microphone  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-mic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe streaming audio from a microphone Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe streaming audio from a microphone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe audio from streaming input](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-streaming-audio)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"os"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    func main() {
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
    
    	go func() {
    		// Pipe stdin to the API.
    		buf := make([]byte, 1024)
    		for {
    			n, err := os.Stdin.Read(buf)
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
    				log.Printf("Could not read from stdin: %v", err)
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
    			// Workaround while the API doesn't give a more informative error.
    			if err.Code == 3 || err.Code == 11 {
    				log.Print("WARNING: Speech recognition request exceeded limit of 60 seconds.")
    			}
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
    
    
    /** Performs microphone streaming speech recognition with a duration of 1 minute. */
    public static void streamingMicRecognize() throws Exception {
    
      ResponseObserver<StreamingRecognizeResponse> responseObserver = null;
      try (SpeechClient client = SpeechClient.create()) {
    
        responseObserver =
            new ResponseObserver<StreamingRecognizeResponse>() {
              ArrayList<StreamingRecognizeResponse> responses = new ArrayList<>();
    
              public void onStart(StreamController controller) {}
    
              public void onResponse(StreamingRecognizeResponse response) {
                responses.add(response);
              }
    
              public void onComplete() {
                for (StreamingRecognizeResponse response : responses) {
                  StreamingRecognitionResult result = response.getResultsList().get(0);
                  SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
                  System.out.printf("Transcript : %s\n", alternative.getTranscript());
                }
              }
    
              public void onError(Throwable t) {
                System.out.println(t);
              }
            };
    
        ClientStream<StreamingRecognizeRequest> clientStream =
            client.streamingRecognizeCallable().splitCall(responseObserver);
    
        RecognitionConfig recognitionConfig =
            RecognitionConfig.newBuilder()
                .setEncoding(RecognitionConfig.AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .build();
        StreamingRecognitionConfig streamingRecognitionConfig =
            StreamingRecognitionConfig.newBuilder().setConfig(recognitionConfig).build();
    
        StreamingRecognizeRequest request =
            StreamingRecognizeRequest.newBuilder()
                .setStreamingConfig(streamingRecognitionConfig)
                .build(); // The first request in a streaming call has to be a config
    
        clientStream.send(request);
        // SampleRate:16000Hz, SampleSizeInBits: 16, Number of channels: 1, Signed: true,
        // bigEndian: false
        AudioFormat audioFormat = new AudioFormat(16000, 16, 1, true, false);
        DataLine.Info targetInfo =
            new Info(
                TargetDataLine.class,
                audioFormat); // Set the system information to read from the microphone audio stream
    
        if (!AudioSystem.isLineSupported(targetInfo)) {
          System.out.println("Microphone not supported");
          System.exit(0);
        }
        // Target data line captures the audio stream the microphone produces.
        TargetDataLine targetDataLine = (TargetDataLine) AudioSystem.getLine(targetInfo);
        targetDataLine.open(audioFormat);
        targetDataLine.start();
        System.out.println("Start speaking");
        long startTime = System.currentTimeMillis();
        // Audio Input Stream
        AudioInputStream audio = new AudioInputStream(targetDataLine);
        while (true) {
          long estimatedTime = System.currentTimeMillis() - startTime;
          byte[] data = new byte[6400];
          audio.read(data);
          if (estimatedTime > 60000) { // 60 seconds
            System.out.println("Stop speaking.");
            targetDataLine.stop();
            targetDataLine.close();
            break;
          }
          request =
              StreamingRecognizeRequest.newBuilder()
                  .setAudioContent(ByteString.copyFrom(data))
                  .build();
          clientStream.send(request);
        }
      } catch (Exception e) {
        System.out.println(e);
      }
      responseObserver.onComplete();
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const recorder = require('node-record-lpcm16');
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
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
    
    // Create a recognize stream
    const recognizeStream = client
      .streamingRecognize(request)
      .on('error', console.error)
      .on('data', data =>
        process.stdout.write(
          data.results[0] && data.results[0].alternatives[0]
            ? `Transcription: ${data.results[0].alternatives[0].transcript}\n`
            : '\n\nReached transcription time limit, press Ctrl+C\n'
        )
      );
    
    // Start recording and send the microphone input to the Speech API.
    // Ensure SoX is installed, see https://www.npmjs.com/package/node-record-lpcm16#dependencies
    recorder
      .record({
        sampleRateHertz: sampleRateHertz,
        threshold: 0,
        // Other options, see https://www.npmjs.com/package/node-record-lpcm16#options
        verbose: false,
        recordProgram: 'rec', // Try also "arecord" or "sox"
        silence: '10.0',
      })
      .stream()
      .on('error', console.error)
      .pipe(recognizeStream);
    
    console.log('Listening, press Ctrl+C to stop.');

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import queue
    import re
    import sys
    
    from google.cloud import speech
    
    import pyaudio
    
    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms
    
    
    class MicrophoneStream:
        """Opens a recording stream as a generator yielding the audio chunks."""
    
        def __init__(self: object, rate: int = RATE, chunk: int = CHUNK) -> None:
            """The audio -- and generator -- is guaranteed to be on the main thread."""
            self._rate = rate
            self._chunk = chunk
    
            # Create a thread-safe buffer of audio data
            self._buff = queue.Queue()
            self.closed = True
    
        def __enter__(self: object) -> object:
            self._audio_interface = pyaudio.PyAudio()
            self._audio_stream = self._audio_interface.open(
                format=pyaudio.paInt16,
                # The API currently only supports 1-channel (mono) audio
                # https://goo.gl/z757pE
                channels=1,
                rate=self._rate,
                input=True,
                frames_per_buffer=self._chunk,
                # Run the audio stream asynchronously to fill the buffer object.
                # This is necessary so that the input device's buffer doesn't
                # overflow while the calling thread makes network requests, etc.
                stream_callback=self._fill_buffer,
            )
    
            self.closed = False
    
            return self
    
        def __exit__(
            self: object,
            type: object,
            value: object,
            traceback: object,
        ) -> None:
            """Closes the stream, regardless of whether the connection was lost or not."""
            self._audio_stream.stop_stream()
            self._audio_stream.close()
            self.closed = True
            # Signal the generator to terminate so that the client's
            # streaming_recognize method will not block the process termination.
            self._buff.put(None)
            self._audio_interface.terminate()
    
        def _fill_buffer(
            self: object,
            in_data: object,
            frame_count: int,
            time_info: object,
            status_flags: object,
        ) -> object:
            """Continuously collect data from the audio stream, into the buffer.
    
            Args:
                in_data: The audio data as a bytes object
                frame_count: The number of frames captured
                time_info: The time information
                status_flags: The status flags
    
            Returns:
                The audio data as a bytes object
            """
            self._buff.put(in_data)
            return None, pyaudio.paContinue
    
        def generator(self: object) -> object:
            """Generates audio chunks from the stream of audio data in chunks.
    
            Args:
                self: The MicrophoneStream object
    
            Returns:
                A generator that outputs audio chunks.
            """
            while not self.closed:
                # Use a blocking get() to ensure there's at least one chunk of
                # data, and stop iteration if the chunk is None, indicating the
                # end of the audio stream.
                chunk = self._buff.get()
                if chunk is None:
                    return
                data = [chunk]
    
                # Now consume whatever other data's still buffered.
                while True:
                    try:
                        chunk = self._buff.get(block=False)
                        if chunk is None:
                            return
                        data.append(chunk)
                    except queue.Empty:
                        break
    
                yield b"".join(data)
    
    
    def listen_print_loop(responses: object) -> str:
        """Iterates through server responses and prints them.
    
        The responses passed is a generator that will block until a response
        is provided by the server.
    
        Each response may contain multiple results, and each result may contain
        multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
        print only the transcription for the top alternative of the top result.
    
        In this case, responses are provided for interim results as well. If the
        response is an interim one, print a line feed at the end of it, to allow
        the next result to overwrite it, until the response is a final one. For the
        final one, print a newline to preserve the finalized transcription.
    
        Args:
            responses: List of server responses
    
        Returns:
            The transcribed text.
        """
        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue
    
            # The `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue
    
            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript
    
            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.
            #
            # If the previous result was longer than this one, we need to print
            # some extra spaces to overwrite the previous result
            overwrite_chars = " " * (num_chars_printed - len(transcript))
    
            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + "\r")
                sys.stdout.flush()
    
                num_chars_printed = len(transcript)
    
            else:
                print(transcript + overwrite_chars)
    
                # Exit recognition if any of the transcribed phrases could be
                # one of our keywords.
                if re.search(r"\b(exit|quit)\b", transcript, re.I):
                    print("Exiting..")
                    break
    
                num_chars_printed = 0
    
        return transcript
    
    
    def main() -> None:
        """Transcribe speech from audio file."""
        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code = "en-US"  # a BCP-47 language tag
    
        client = speech.SpeechClient()
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code,
        )
    
        streaming_config = speech.[StreamingRecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognitionConfig.html)(
            config=config, interim_results=True
        )
    
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (
                speech.[StreamingRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognizeRequest.html)(audio_content=content)
                for content in audio_generator
            )
    
            responses = client.[streaming_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_streaming_recognize)(streaming_config, requests)
    
            # Now, put the transcription responses to use.
            listen_print_loop(responses)
    
    
    if __name__ == "__main__":
        main()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
