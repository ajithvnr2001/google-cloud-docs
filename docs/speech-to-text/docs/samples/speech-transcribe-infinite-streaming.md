---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-infinite-streaming/
title: Transcribe a streaming audio feed \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:11.473506+00:00
---

# Transcribe a streaming audio feed  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-infinite-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a streaming audio feed Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a streaming audio feed from a microphone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe audio from streaming input](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-streaming-audio)



## Code sample

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ClientStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientStream.html);
    import com.google.api.gax.rpc.[ResponseObserver](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResponseObserver.html);
    import com.google.api.gax.rpc.[StreamController](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController.html);
    import com.google.cloud.speech.v1p1beta1.RecognitionConfig;
    import com.google.cloud.speech.v1p1beta1.SpeechClient;
    import com.google.cloud.speech.v1p1beta1.SpeechRecognitionAlternative;
    import com.google.cloud.speech.v1p1beta1.StreamingRecognitionConfig;
    import com.google.cloud.speech.v1p1beta1.StreamingRecognitionResult;
    import com.google.cloud.speech.v1p1beta1.StreamingRecognizeRequest;
    import com.google.cloud.speech.v1p1beta1.StreamingRecognizeResponse;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.text.DecimalFormat;
    import java.util.ArrayList;
    import java.util.concurrent.BlockingQueue;
    import java.util.concurrent.LinkedBlockingQueue;
    import java.util.concurrent.TimeUnit;
    import javax.sound.sampled.AudioFormat;
    import javax.sound.sampled.AudioSystem;
    import javax.sound.sampled.DataLine;
    import javax.sound.sampled.DataLine.Info;
    import javax.sound.sampled.TargetDataLine;
    
    public class InfiniteStreamRecognize {
    
      private static final int STREAMING_LIMIT = 290000; // ~5 minutes
    
      public static final String RED = "\033[0;31m";
      public static final String GREEN = "\033[0;32m";
      public static final String YELLOW = "\033[0;33m";
    
      // Creating shared object
      private static volatile BlockingQueue<byte[]> sharedQueue = new LinkedBlockingQueue<byte[]>();
      private static TargetDataLine targetDataLine;
      private static int BYTES_PER_BUFFER = 6400; // buffer size in bytes
    
      private static int restartCounter = 0;
      private static ArrayList<ByteString> audioInput = new ArrayList<ByteString>();
      private static ArrayList<ByteString> lastAudioInput = new ArrayList<ByteString>();
      private static int resultEndTimeInMS = 0;
      private static int isFinalEndTime = 0;
      private static int finalRequestEndTime = 0;
      private static boolean newStream = true;
      private static double bridgingOffset = 0;
      private static boolean lastTranscriptWasFinal = false;
      private static [StreamController](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController.html) referenceToStreamController;
      private static [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) tempByteString;
    
      public static void main(String... args) {
        InfiniteStreamRecognizeOptions options = InfiniteStreamRecognizeOptions.fromFlags(args);
        if (options == null) {
          // Could not parse.
          System.out.println("Failed to parse options.");
          System.exit(1);
        }
    
        try {
          infiniteStreamingRecognize(options.langCode);
        } catch (Exception e) {
          System.out.println("Exception caught: " + e);
        }
      }
    
      public static String convertMillisToDate(double milliSeconds) {
        long millis = (long) milliSeconds;
        DecimalFormat format = new DecimalFormat();
        format.setMinimumIntegerDigits(2);
        return String.format(
            "%s:%s /",
            format.format(TimeUnit.MILLISECONDS.[toMinutes](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html#com_google_protobuf_util_Durations_toMinutes_com_google_protobuf_Duration_)(millis)),
            format.format(
                TimeUnit.MILLISECONDS.toSeconds(millis)
                    - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.[toMinutes](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Durations.html#com_google_protobuf_util_Durations_toMinutes_com_google_protobuf_Duration_)(millis))));
      }
    
      /** Performs infinite streaming speech recognition */
      public static void infiniteStreamingRecognize(String languageCode) throws Exception {
    
        // Microphone Input buffering
        class MicBuffer implements Runnable {
    
          @Override
          public void run() {
            System.out.println(YELLOW);
            System.out.println("Start speaking...Press Ctrl-C to stop");
            targetDataLine.start();
            byte[] data = new byte[BYTES_PER_BUFFER];
            while (targetDataLine.isOpen()) {
              try {
                int numBytesRead = targetDataLine.read(data, 0, data.length);
                if ((numBytesRead <= 0) && (targetDataLine.isOpen())) {
                  continue;
                }
                sharedQueue.put(data.clone());
              } catch (InterruptedException e) {
                System.out.println("Microphone input buffering interrupted : " + e.getMessage());
              }
            }
          }
        }
    
        // Creating microphone input buffer thread
        MicBuffer micrunnable = new MicBuffer();
        Thread micThread = new Thread(micrunnable);
        ResponseObserver<StreamingRecognizeResponse> responseObserver = null;
        try (SpeechClient client = SpeechClient.create()) {
          ClientStream<StreamingRecognizeRequest> clientStream;
          responseObserver =
              new ResponseObserver<StreamingRecognizeResponse>() {
    
                ArrayList<StreamingRecognizeResponse> responses = new ArrayList<>();
    
                public void onStart([StreamController](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController.html) controller) {
                  referenceToStreamController = controller;
                }
    
                public void onResponse(StreamingRecognizeResponse response) {
                  responses.add(response);
                  StreamingRecognitionResult result = response.getResultsList().get(0);
                  [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) resultEndTime = result.getResultEndTime();
                  resultEndTimeInMS =
                      (int)
                          ((resultEndTime.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getSeconds__)() * 1000) + (resultEndTime.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getNanos__)() / 1000000));
                  double correctedTime =
                      resultEndTimeInMS - bridgingOffset + (STREAMING_LIMIT * restartCounter);
    
                  SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
                  if (result.getIsFinal()) {
                    System.out.print(GREEN);
                    System.out.print("\033[2K\r");
                    System.out.printf(
                        "%s: %s [confidence: %.2f]\n",
                        convertMillisToDate(correctedTime),
                        alternative.getTranscript(),
                        alternative.getConfidence());
                    isFinalEndTime = resultEndTimeInMS;
                    lastTranscriptWasFinal = true;
                  } else {
                    System.out.print(RED);
                    System.out.print("\033[2K\r");
                    System.out.printf(
                        "%s: %s", convertMillisToDate(correctedTime), alternative.getTranscript());
                    lastTranscriptWasFinal = false;
                  }
                }
    
                public void onComplete() {}
    
                public void onError(Throwable t) {}
              };
          clientStream = client.streamingRecognizeCallable().[splitCall](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html#com_google_api_gax_rpc_BidiStreamingCallable_splitCall_com_google_api_gax_rpc_ResponseObserver_ResponseT__)(responseObserver);
    
          RecognitionConfig recognitionConfig =
              RecognitionConfig.newBuilder()
                  .setEncoding(RecognitionConfig.AudioEncoding.LINEAR16)
                  .setLanguageCode(languageCode)
                  .setSampleRateHertz(16000)
                  .build();
    
          StreamingRecognitionConfig streamingRecognitionConfig =
              StreamingRecognitionConfig.newBuilder()
                  .setConfig(recognitionConfig)
                  .setInterimResults(true)
                  .build();
    
          StreamingRecognizeRequest request =
              StreamingRecognizeRequest.newBuilder()
                  .setStreamingConfig(streamingRecognitionConfig)
                  .build(); // The first request in a streaming call has to be a config
    
          clientStream.send(request);
    
          try {
            // SampleRate:16000Hz, SampleSizeInBits: 16, Number of channels: 1, Signed: true,
            // bigEndian: false
            AudioFormat audioFormat = new AudioFormat(16000, 16, 1, true, false);
            DataLine.Info targetInfo =
                new Info(
                    TargetDataLine.class,
                    audioFormat); // Set the system information to read from the microphone audio
            // stream
    
            if (!AudioSystem.isLineSupported(targetInfo)) {
              System.out.println("Microphone not supported");
              System.exit(0);
            }
            // Target data line captures the audio stream the microphone produces.
            targetDataLine = (TargetDataLine) AudioSystem.getLine(targetInfo);
            targetDataLine.open(audioFormat);
            micThread.start();
    
            long startTime = System.currentTimeMillis();
    
            while (true) {
    
              long estimatedTime = System.currentTimeMillis() - startTime;
    
              if (estimatedTime >= STREAMING_LIMIT) {
    
                clientStream.closeSend();
                referenceToStreamController.[cancel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController.html#com_google_api_gax_rpc_StreamController_cancel__)(); // remove Observer
    
                if (resultEndTimeInMS > 0) {
                  finalRequestEndTime = isFinalEndTime;
                }
                resultEndTimeInMS = 0;
    
                lastAudioInput = null;
                lastAudioInput = audioInput;
                audioInput = new ArrayList<ByteString>();
    
                restartCounter++;
    
                if (!lastTranscriptWasFinal) {
                  System.out.print('\n');
                }
    
                newStream = true;
    
                clientStream = client.streamingRecognizeCallable().[splitCall](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html#com_google_api_gax_rpc_BidiStreamingCallable_splitCall_com_google_api_gax_rpc_ResponseObserver_ResponseT__)(responseObserver);
    
                request =
                    StreamingRecognizeRequest.newBuilder()
                        .setStreamingConfig(streamingRecognitionConfig)
                        .build();
    
                System.out.println(YELLOW);
                System.out.printf("%d: RESTARTING REQUEST\n", restartCounter * STREAMING_LIMIT);
    
                startTime = System.currentTimeMillis();
    
              } else {
    
                if ((newStream) && (lastAudioInput.size() > 0)) {
                  // if this is the first audio from a new request
                  // calculate amount of unfinalized audio from last request
                  // resend the audio to the speech client before incoming audio
                  double chunkTime = STREAMING_LIMIT / lastAudioInput.size();
                  // ms length of each chunk in previous request audio arrayList
                  if (chunkTime != 0) {
                    if (bridgingOffset < 0) {
                      // bridging Offset accounts for time of resent audio
                      // calculated from last request
                      bridgingOffset = 0;
                    }
                    if (bridgingOffset > finalRequestEndTime) {
                      bridgingOffset = finalRequestEndTime;
                    }
                    int chunksFromMs =
                        (int) Math.floor((finalRequestEndTime - bridgingOffset) / chunkTime);
                    // chunks from MS is number of chunks to resend
                    bridgingOffset =
                        (int) Math.floor((lastAudioInput.size() - chunksFromMs) * chunkTime);
                    // set bridging offset for next request
                    for (int i = chunksFromMs; i < lastAudioInput.size(); i++) {
                      request =
                          StreamingRecognizeRequest.newBuilder()
                              .setAudioContent(lastAudioInput.get(i))
                              .build();
                      clientStream.send(request);
                    }
                  }
                  newStream = false;
                }
    
                tempByteString = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(sharedQueue.take());
    
                request =
                    StreamingRecognizeRequest.newBuilder().setAudioContent(tempByteString).build();
    
                audioInput.add(tempByteString);
              }
    
              clientStream.send(request);
            }
          } catch (Exception e) {
            System.out.println(e);
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // const encoding = 'LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'en-US';
    // const streamingLimit = 10000; // ms - set to low number for demo purposes
    
    const chalk = require('chalk');
    const {Writable} = require('stream');
    const recorder = require('node-record-lpcm16');
    
    // Imports the Google Cloud client library
    // Currently, only v1p1beta1 contains result-end-time
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    const config = {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
    };
    
    const request = {
      config,
      interimResults: true,
    };
    
    let recognizeStream = null;
    let restartCounter = 0;
    let audioInput = [];
    let lastAudioInput = [];
    let resultEndTime = 0;
    let isFinalEndTime = 0;
    let finalRequestEndTime = 0;
    let newStream = true;
    let bridgingOffset = 0;
    let lastTranscriptWasFinal = false;
    
    function startStream() {
      // Clear current audioInput
      audioInput = [];
      // Initiate (Reinitiate) a recognize stream
      recognizeStream = client
        .streamingRecognize(request)
        .on('error', err => {
          if (err.code === 11) {
            // restartStream();
          } else {
            console.error('API request error ' + err);
          }
        })
        .on('data', speechCallback);
    
      // Restart stream when streamingLimit expires
      setTimeout(restartStream, streamingLimit);
    }
    
    const speechCallback = stream => {
      // Convert API result end time from seconds + nanoseconds to milliseconds
      resultEndTime =
        stream.results[0].resultEndTime.seconds * 1000 +
        Math.round(stream.results[0].resultEndTime.nanos / 1000000);
    
      // Calculate correct time based on offset from audio sent twice
      const correctedTime =
        resultEndTime - bridgingOffset + streamingLimit * restartCounter;
    
      process.stdout.clearLine();
      process.stdout.cursorTo(0);
      let stdoutText = '';
      if (stream.results[0] && stream.results[0].alternatives[0]) {
        stdoutText =
          correctedTime + ': ' + stream.results[0].alternatives[0].transcript;
      }
    
      if (stream.results[0].isFinal) {
        process.stdout.write(chalk.green(`${stdoutText}\n`));
    
        isFinalEndTime = resultEndTime;
        lastTranscriptWasFinal = true;
      } else {
        // Make sure transcript does not exceed console character length
        if (stdoutText.length > process.stdout.columns) {
          stdoutText =
            stdoutText.substring(0, process.stdout.columns - 4) + '...';
        }
        process.stdout.write(chalk.red(`${stdoutText}`));
    
        lastTranscriptWasFinal = false;
      }
    };
    
    const audioInputStreamTransform = new Writable({
      write(chunk, encoding, next) {
        if (newStream && lastAudioInput.length !== 0) {
          // Approximate math to calculate time of chunks
          const chunkTime = streamingLimit / lastAudioInput.length;
          if (chunkTime !== 0) {
            if (bridgingOffset < 0) {
              bridgingOffset = 0;
            }
            if (bridgingOffset > finalRequestEndTime) {
              bridgingOffset = finalRequestEndTime;
            }
            const chunksFromMS = Math.floor(
              (finalRequestEndTime - bridgingOffset) / chunkTime
            );
            bridgingOffset = Math.floor(
              (lastAudioInput.length - chunksFromMS) * chunkTime
            );
    
            for (let i = chunksFromMS; i < lastAudioInput.length; i++) {
              recognizeStream.write(lastAudioInput[i]);
            }
          }
          newStream = false;
        }
    
        audioInput.push(chunk);
    
        if (recognizeStream) {
          recognizeStream.write(chunk);
        }
    
        next();
      },
    
      final() {
        if (recognizeStream) {
          recognizeStream.end();
        }
      },
    });
    
    function restartStream() {
      if (recognizeStream) {
        recognizeStream.end();
        recognizeStream.removeListener('data', speechCallback);
        recognizeStream = null;
      }
      if (resultEndTime > 0) {
        finalRequestEndTime = isFinalEndTime;
      }
      resultEndTime = 0;
    
      lastAudioInput = [];
      lastAudioInput = audioInput;
    
      restartCounter++;
    
      if (!lastTranscriptWasFinal) {
        process.stdout.write('\n');
      }
      process.stdout.write(
        chalk.yellow(`${streamingLimit * restartCounter}: RESTARTING REQUEST\n`)
      );
    
      newStream = true;
    
      startStream();
    }
    // Start recording and send the microphone input to the Speech API
    recorder
      .record({
        sampleRateHertz: sampleRateHertz,
        threshold: 0, // Silence threshold
        silence: 1000,
        keepSilence: true,
        recordProgram: 'rec', // Try also "arecord" or "sox"
      })
      .stream()
      .on('error', err => {
        console.error('Audio recording error ' + err);
      })
      .pipe(audioInputStreamTransform);
    
    console.log('');
    console.log('Listening, press Ctrl+C to stop.');
    console.log('');
    console.log('End (ms)       Transcript Results/Status');
    console.log('=========================================================');
    
    startStream();

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import queue
    import re
    import sys
    import time
    
    from google.cloud import speech
    import pyaudio
    
    # Audio recording parameters
    STREAMING_LIMIT = 240000  # 4 minutes
    SAMPLE_RATE = 16000
    CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms
    
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    
    
    def get_current_time() -> int:
        """Return Current Time in MS.
    
        Returns:
            int: Current Time in MS.
        """
    
        return int(round(time.time() * 1000))
    
    
    class ResumableMicrophoneStream:
        """Opens a recording stream as a generator yielding the audio chunks."""
    
        def __init__(
            self: object,
            rate: int,
            chunk_size: int,
        ) -> None:
            """Creates a resumable microphone stream.
    
            Args:
            self: The class instance.
            rate: The audio file's sampling rate.
            chunk_size: The audio file's chunk size.
    
            returns: None
            """
            self._rate = rate
            self.chunk_size = chunk_size
            self._num_channels = 1
            self._buff = queue.Queue()
            self.closed = True
            self.start_time = get_current_time()
            self.restart_counter = 0
            self.audio_input = []
            self.last_audio_input = []
            self.result_end_time = 0
            self.is_final_end_time = 0
            self.final_request_end_time = 0
            self.bridging_offset = 0
            self.last_transcript_was_final = False
            self.new_stream = True
            self._audio_interface = pyaudio.PyAudio()
            self._audio_stream = self._audio_interface.open(
                format=pyaudio.paInt16,
                channels=self._num_channels,
                rate=self._rate,
                input=True,
                frames_per_buffer=self.chunk_size,
                # Run the audio stream asynchronously to fill the buffer object.
                # This is necessary so that the input device's buffer doesn't
                # overflow while the calling thread makes network requests, etc.
                stream_callback=self._fill_buffer,
            )
    
        def __enter__(self: object) -> object:
            """Opens the stream.
    
            Args:
            self: The class instance.
    
            returns: None
            """
            self.closed = False
            return self
    
        def __exit__(
            self: object,
            type: object,
            value: object,
            traceback: object,
        ) -> object:
            """Closes the stream and releases resources.
    
            Args:
            self: The class instance.
            type: The exception type.
            value: The exception value.
            traceback: The exception traceback.
    
            returns: None
            """
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
            *args: object,
            **kwargs: object,
        ) -> object:
            """Continuously collect data from the audio stream, into the buffer.
    
            Args:
            self: The class instance.
            in_data: The audio data as a bytes object.
            args: Additional arguments.
            kwargs: Additional arguments.
    
            returns: None
            """
            self._buff.put(in_data)
            return None, pyaudio.paContinue
    
        def generator(self: object) -> object:
            """Stream Audio from microphone to API and to local buffer
    
            Args:
                self: The class instance.
    
            returns:
                The data from the audio stream.
            """
            while not self.closed:
                data = []
    
                if self.new_stream and self.last_audio_input:
                    chunk_time = STREAMING_LIMIT / len(self.last_audio_input)
    
                    if chunk_time != 0:
                        if self.bridging_offset < 0:
                            self.bridging_offset = 0
    
                        if self.bridging_offset > self.final_request_end_time:
                            self.bridging_offset = self.final_request_end_time
    
                        chunks_from_ms = round(
                            (self.final_request_end_time - self.bridging_offset)
                            / chunk_time
                        )
    
                        self.bridging_offset = round(
                            (len(self.last_audio_input) - chunks_from_ms) * chunk_time
                        )
    
                        for i in range(chunks_from_ms, len(self.last_audio_input)):
                            data.append(self.last_audio_input[i])
    
                    self.new_stream = False
    
                # Use a blocking get() to ensure there's at least one chunk of
                # data, and stop iteration if the chunk is None, indicating the
                # end of the audio stream.
                chunk = self._buff.get()
                self.audio_input.append(chunk)
    
                if chunk is None:
                    return
                data.append(chunk)
                # Now consume whatever other data's still buffered.
                while True:
                    try:
                        chunk = self._buff.get(block=False)
    
                        if chunk is None:
                            return
                        data.append(chunk)
                        self.audio_input.append(chunk)
    
                    except queue.Empty:
                        break
    
                yield b"".join(data)
    
    
    def listen_print_loop(responses: object, stream: object) -> None:
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
    
        Arg:
            responses: The responses returned from the API.
            stream: The audio stream to be processed.
        """
        for response in responses:
            if get_current_time() - stream.start_time > STREAMING_LIMIT:
                stream.start_time = get_current_time()
                break
    
            if not response.results:
                continue
    
            result = response.results[0]
    
            if not result.alternatives:
                continue
    
            transcript = result.alternatives[0].transcript
    
            result_seconds = 0
            result_micros = 0
    
            if result.result_end_time.seconds:
                result_seconds = result.result_end_time.seconds
    
            if result.result_end_time.microseconds:
                result_micros = result.result_end_time.microseconds
    
            stream.result_end_time = int((result_seconds * 1000) + (result_micros / 1000))
    
            corrected_time = (
                stream.result_end_time
                - stream.bridging_offset
                + (STREAMING_LIMIT * stream.restart_counter)
            )
            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.
    
            if result.is_final:
                sys.stdout.write(GREEN)
                sys.stdout.write("\033[K")
                sys.stdout.write(str(corrected_time) + ": " + transcript + "\n")
    
                stream.is_final_end_time = stream.result_end_time
                stream.last_transcript_was_final = True
    
                # Exit recognition if any of the transcribed phrases could be
                # one of our keywords.
                if re.search(r"\b(exit|quit)\b", transcript, re.I):
                    sys.stdout.write(YELLOW)
                    sys.stdout.write("Exiting...\n")
                    stream.closed = True
                    break
            else:
                sys.stdout.write(RED)
                sys.stdout.write("\033[K")
                sys.stdout.write(str(corrected_time) + ": " + transcript + "\r")
    
                stream.last_transcript_was_final = False
    
    
    def main() -> None:
        """start bidirectional streaming from microphone input to speech API"""
        client = speech.SpeechClient()
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=SAMPLE_RATE,
            language_code="en-US",
            max_alternatives=1,
        )
    
        streaming_config = speech.[StreamingRecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognitionConfig.html)(
            config=config, interim_results=True
        )
    
        mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
        print(mic_manager.chunk_size)
        sys.stdout.write(YELLOW)
        sys.stdout.write('\nListening, say "Quit" or "Exit" to stop.\n\n')
        sys.stdout.write("End (ms)       Transcript Results/Status\n")
        sys.stdout.write("=====================================================\n")
    
        with mic_manager as stream:
            while not stream.closed:
                sys.stdout.write(YELLOW)
                sys.stdout.write(
                    "\n" + str(STREAMING_LIMIT * stream.restart_counter) + ": NEW REQUEST\n"
                )
    
                stream.audio_input = []
                audio_generator = stream.generator()
    
                requests = (
                    speech.[StreamingRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognizeRequest.html)(audio_content=content)
                    for content in audio_generator
                )
    
                responses = client.[streaming_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_streaming_recognize)(streaming_config, requests)
    
                # Now, put the transcription responses to use.
                listen_print_loop(responses, stream)
    
                if stream.result_end_time > 0:
                    stream.final_request_end_time = stream.is_final_end_time
                stream.result_end_time = 0
                stream.last_audio_input = []
                stream.last_audio_input = stream.audio_input
                stream.audio_input = []
                stream.restart_counter = stream.restart_counter + 1
    
                if not stream.last_transcript_was_final:
                    sys.stdout.write("\n")
                stream.new_stream = True
    
    
    if __name__ == "__main__":
        main()
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
