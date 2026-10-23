---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription/
title: Voice transcription \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:26.541537+00:00
---

# Voice transcription  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Voice transcription Stay organized with collections  Save and categorize content based on your preferences. 

Voice transcription lets you convert your streaming audio data to transcripted text in real time. Agent Assist makes suggestions based on text, so audio data must be converted before it can be used. You can also use transcripted streaming audio with Customer Experience Insights to gather real-time data about agent conversations (for example, [Topic Modeling](https://docs.cloud.google.com/contact-center/insights/docs/topic-modeling-overview)).

There are two ways to transcribe streaming audio for use with Agent Assist: By using the [SIPREC feature](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/siprec), or by making gRPC calls with audio data as payload. This page describes the process of transcribing streaming audio data using gRPC calls.

Voice transcription works using Speech-to-Text [streaming speech recognition](https://docs.cloud.google.com/speech-to-text/docs/transcribe-streaming-audio). Speech-to-Text offers multiple [recognition models](https://docs.cloud.google.com/speech-to-text/docs/basics#select-model), standard and [enhanced](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models). Agent Assist does not restrict which models you can use with voice transcription, but voice transcription is supported at the GA level **only** when used with the telephony or [Chirp 3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3) model. For optimal transcription quality, the [Chirp 3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3) model is recommended, subject to regional availability.

**Note:** To see if transcription feature is available for your language, see the [language support page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/languages).

## Prerequisites

  * [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in Google Cloud.
  * [Enable the Dialogflow API](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup).
  * Contact your Google representative to make sure that your account has access to [Speech-to-Text **enhanced models**](https://docs.cloud.google.com/speech-to-text/docs/enhanced-models).



## Create a conversation profile

To [create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile), use the [Agent Assist console](https://agentassist.cloud.google.com) or call the `create` method on the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) resource directly.

For voice transcription, we recommend that you configure `ConversationProfile.stt_config` as the default `InputAudioConfig` when sending audio data in a conversation.

**Note:** To enable long form models (e.g. telephony model, Chirp 3 model) for telephony integration, select **Use Long Form Model for AA Telephony SipRec Integration** at the conversation profile. The following image shows the recommended configuration.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/transcription-stt-config.png)

## Get transcriptions at conversation runtime

To get transcriptions at conversation runtime, you need to create participants for the conversation, and send audio data for each participant.

### Create participants

There are three types of [participant](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants). See the [reference documentation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#role) for more details about their roles. Call the `create` method on the `participant` and specify the `role`. Only an `END_USER` or a `HUMAN_AGENT` participant can call `StreamingAnalyzeContent`, which is required to get a transcription.

### Send audio data and get a transcript

You can use [`StreamingAnalyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#streaminganalyzecontentrequest) to send a participant's audio to Google and get transcription, with the following parameters:

  * The first request in the stream must be [`InputAudioConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig). (The fields configured here override the corresponding settings at `ConversationProfile.stt_config`.) Don't send any audio input until the second request.

    * **`audioEncoding`** needs to be set to `AUDIO_ENCODING_LINEAR_16` or `AUDIO_ENCODING_MULAW`.
    * **`model`** : This is the [Speech-to-Text model](https://docs.cloud.google.com/speech-to-text/docs/basics#select-model) that you want to use to transcribe your audio. Set this field to `chirp_3`. The variant doesn't impact transcription quality so, you can leave **Speech model variant** unspecified or choose **Use best available**.
    * **`singleUtterance`** should be set to `false` for best transcription quality. You should not expect `END_OF_SINGLE_UTTERANCE` if `singleUtterance` is `false`, but you can depend on `isFinal==true` inside `StreamingAnalyzeContentResponse.recognition_result` to half-close the stream.
    * **Optional additional parameters** : The following parameters are optional. To gain access to these parameters, contact your Google representative. 
      * **`languageCode`** : `language_code` of the audio. The default value is `en-US`.
      * **`alternativeLanguageCodes`** : This feature is only at GA level readiness for Chirp 3 model. Additional languages that might be detected in the audio. Agent Assist uses the `language_code` field to automatically detect the language at the beginning of the audio and defaults to it in all following conversation turns. The `alternativeLanguageCodes` field lets you specify more options for Agent Assist to choose from.
      * **`phraseSets`** : The [Speech-to-Text model adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model) `phraseSet` resource name. 
        * To configure adaptation for Chirp 3 model, add inline phrases separated by newlines, with no commas.
        * To use model adaptation with other models like `telephony` for voice transcription, you must first create the `phraseSet` using the Speech-to-Text API and specify the resource name here.
  * After you send the second request with audio payload, you should start receiving some `StreamingAnalyzeContentResponses` from the stream.

    * You can half close the stream (or stop sending in some languages like Python) when you see `is_final` set to `true` in `StreamingAnalyzeContentResponse.recognition_result`.
    * After you half-close the stream, the server will send back the response containing final transcript, along with potential Dialogflow suggestions or Agent Assist suggestions.
  * You can find the final transcription in the following locations:

    * `StreamingAnalyzeContentResponse.message.content`.
    * If you [enable Pub/Sub notifications](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub), you can also see the transcription in Pub/Sub.
  * Start a new stream after the previous stream is closed.

    * Audio re-send: Audio data generated after last `speech_end_offset` of the response with `is_final=true` to the new stream start time needs to be re-sent to `StreamingAnalyzeContent` for best transcription quality.
  * Here is the diagram illustrate how stream works.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/transcription-stream.png)


**Note:** you can also use [extended_streaming](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/extended-streaming) feature or [BidiStreamingAnalyzeContent API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/bidi-stream-api) for the integration.

### Streaming recognition request code sample

The following code sample illustrates how to send a streaming transcription request.

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Copyright 2023 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Google Cloud Dialogflow API sample code using the StreamingAnalyzeContent
    API.
    
    Also please contact Google to get credentials of this project and set up the
    credential file json locations by running:
    export GOOGLE_APPLICATION_CREDENTIALS=<cred_json_file_location>
    
    Example usage:
        export GOOGLE_CLOUD_PROJECT='cloud-contact-center-ext-demo'
        export CONVERSATION_PROFILE='FnuBYO8eTBWM8ep1i-eOng'
        export GOOGLE_APPLICATION_CREDENTIALS='/Users/ruogu/Desktop/keys/cloud-contact-center-ext-demo-78798f9f9254.json'
        python streaming_transcription.py
    
    Then started to talk in English, you should see transcription shows up as you speak.
    
    Say "Quit" or "Exit" to stop.
    """
    
    import os
    import re
    import sys
    
    from google.api_core.exceptions import DeadlineExceeded, OutOfRange
    
    import pyaudio
    
    from six.moves import queue
    
    import conversation_management
    import participant_management
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    CONVERSATION_PROFILE_ID = os.getenv("CONVERSATION_PROFILE")
    
    # Audio recording parameters
    SAMPLE_RATE = 16000
    CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms
    RESTART_TIMEOUT = 160  # seconds
    MAX_LOOKBACK = 3  # seconds
    HALF_CLOSE_DURATION_MS = 90 * 1000  # milliseconds
    
    YELLOW = "\033[0;33m"
    
    
    class ResumableMicrophoneStream:
        """Opens a recording stream as a generator yielding the audio chunks."""
    
        def __init__(self, rate, chunk_size):
            self._rate = rate
            self.chunk_size = chunk_size
            self._num_channels = 1
            self._buff = queue.Queue()
            self.is_final = False
            self.closed = True
            # Count the number of times the stream analyze content restarts.
            self.restart_counter = 0
            self.last_start_time = 0
            # Time end of the last is_final in millisec since last_start_time.
            self.is_final_offset = 0
            # Save the audio chunks generated from the start of the audio stream for
            # replay after restart.
            self.audio_input_chunks = []
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
    
        def __enter__(self):
            self.closed = False
            return self
    
        def __exit__(self, type, value, traceback):
            self._audio_stream.stop_stream()
            self._audio_stream.close()
            self.closed = True
            # Signal the generator to terminate so that the client's
            # streaming_recognize method will not block the process termination.
            self._buff.put(None)
            self._audio_interface.terminate()
    
        def _fill_buffer(self, in_data, *args, **kwargs):
            """Continuously collect data from the audio stream, into the buffer in
            chunksize."""
    
            self._buff.put(in_data)
            return None, pyaudio.paContinue
    
        def generator(self):
            """Stream Audio from microphone to API and to local buffer"""
            try:
                # Handle restart.
                print("restart generator")
                # Flip the bit of is_final so it can continue stream.
                self.is_final = False
                total_processed_time = self.last_start_time + self.is_final_offset
                processed_bytes_length = (
                    int(total_processed_time * SAMPLE_RATE * 16 / 8) / 1000
                )
                self.last_start_time = total_processed_time
                # Send out bytes stored in self.audio_input_chunks that is after the
                # processed_bytes_length.
                if processed_bytes_length != 0:
                    audio_bytes = b"".join(self.audio_input_chunks)
                    # Lookback for unprocessed audio data.
                    need_to_process_length = min(
                        int(len(audio_bytes) - processed_bytes_length),
                        int(MAX_LOOKBACK * SAMPLE_RATE * 16 / 8),
                    )
                    # Note that you need to explicitly use `int` type for substring.
                    need_to_process_bytes = audio_bytes[(-1) * need_to_process_length :]
                    yield need_to_process_bytes
    
                while not self.closed and not self.is_final:
                    data = []
                    # Use a blocking get() to ensure there's at least one chunk of
                    # data, and stop iteration if the chunk is None, indicating the
                    # end of the audio stream.
                    chunk = self._buff.get()
    
                    if chunk is None:
                        return
                    data.append(chunk)
                    # Now try to the rest of chunks if there are any left in the _buff.
                    while True:
                        try:
                            chunk = self._buff.get(block=False)
    
                            if chunk is None:
                                return
                            data.append(chunk)
    
                        except queue.Empty:
                            break
                    self.audio_input_chunks.extend(data)
                    if data:
                        yield b"".join(data)
            finally:
                print("Stop generator")
    
    
    def main():
        """start bidirectional streaming from microphone input to Dialogflow API"""
        # Create conversation.
        conversation = conversation_management.create_conversation(
            project_id=PROJECT_ID, conversation_profile_id=CONVERSATION_PROFILE_ID
        )
    
        conversation_id = conversation.name.split("conversations/")[1].rstrip()
    
        # Create end user participant.
        end_user = participant_management.create_participant(
            project_id=PROJECT_ID, conversation_id=conversation_id, role="END_USER"
        )
        participant_id = end_user.name.split("participants/")[1].rstrip()
    
        mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
        print(mic_manager.chunk_size)
        sys.stdout.write(YELLOW)
        sys.stdout.write('\nListening, say "Quit" or "Exit" to stop.\n\n')
        sys.stdout.write("End (ms)       Transcript Results/Status\n")
        sys.stdout.write("=====================================================\n")
    
        with mic_manager as stream:
            while not stream.closed:
                terminate = False
                while not terminate:
                    try:
                        print(f"New Streaming Analyze Request: {stream.restart_counter}")
                        stream.restart_counter += 1
                        # Send request to streaming and get response.
                        responses = participant_management.analyze_content_audio_stream(
                            conversation_id=conversation_id,
                            participant_id=participant_id,
                            sample_rate_herz=SAMPLE_RATE,
                            stream=stream,
                            timeout=RESTART_TIMEOUT,
                            language_code="en-US",
                            single_utterance=False,
                            # Uncomment to process multiple utterances detected in the audio stream
                            # individually instead of stitching together to form a single utterance.
                            # output_multiple_utterances=True,
                        )
    
                        # Now, print the final transcription responses to user.
                        for response in responses:
                            if response.message:
                                print(response)
                            if response.recognition_result.is_final:
                                print(response)
                                # offset return from recognition_result is relative
                                # to the beginning of audio stream.
                                offset = response.recognition_result.speech_end_offset
                                stream.is_final_offset = int(
                                    offset.seconds * 1000 + offset.microseconds / 1000
                                )
                                transcript = response.recognition_result.transcript
                                # Half-close upon final results for better streaming experiences
                                # (in Python just stop yielding requests)
                                if stream.is_final_offset > HALF_CLOSE_DURATION_MS:
                                    stream.is_final = True
                                # Exit recognition if any of the transcribed phrase could be
                                # one of our keywords.
                                if re.search(r"\b(exit|quit)\b", transcript, re.I):
                                    sys.stdout.write(YELLOW)
                                    sys.stdout.write("Exiting...\n")
                                    terminate = True
                                    stream.closed = True
                                    break
                    except OutOfRange:
                        print("Maximum audio duration exceeded in the stream, restarting.")
                    except DeadlineExceeded:
                        print("Deadline Exceeded, restarting.")
    
                if terminate:
                    conversation_management.complete_conversation(
                        project_id=PROJECT_ID, conversation_id=conversation_id
                    )
                    break
    
    
    if __name__ == "__main__":
        main()
    

Follow these steps to view the python files for `conversation_management` and `participant_management`.

  1. Navigate to the GitHub repository for Python documents.

[Go to GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dialogflow)

  2. Click **Go to file** and enter the filename: `conversation_management` or `participant_management`.

  3. Click **Enter**.




## Best practices

Message send time is when an utterance begins. Use message send time to determine the order in which your contact center displays or analyzes voice [messages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Message).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
