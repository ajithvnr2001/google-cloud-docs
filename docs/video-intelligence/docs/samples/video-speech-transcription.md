---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-speech-transcription/
title: Transcribe speech in a local video file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:03.743502+00:00
---

# Transcribe speech in a local video file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-speech-transcription/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Transcribe speech in a local video file Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe speech in a video stored locally.

## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func speechTranscription(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	fileBytes, err := os.ReadFile(file)
    	if err != nil {
    		return err
    	}
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_SPEECH_TRANSCRIPTION,
    		},
    		VideoContext: &videopb.VideoContext{
    			SpeechTranscriptionConfig: &videopb.SpeechTranscriptionConfig{
    				LanguageCode:               "en-US",
    				EnableAutomaticPunctuation: true,
    			},
    		},
    		InputContent: fileBytes,
    	})
    	if err != nil {
    		return err
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	// A single video was processed. Get the first result.
    	result := resp.AnnotationResults[0]
    
    	for _, transcription := range result.SpeechTranscriptions {
    		// The number of alternatives for each transcription is limited by
    		// SpeechTranscriptionConfig.MaxAlternatives.
    		// Each alternative is a different possible transcription
    		// and has its own confidence score.
    		for _, alternative := range transcription.GetAlternatives() {
    			fmt.Fprintf(w, "Alternative level information:\n")
    			fmt.Fprintf(w, "\tTranscript: %v\n", alternative.GetTranscript())
    			fmt.Fprintf(w, "\tConfidence: %v\n", alternative.GetConfidence())
    
    			fmt.Fprintf(w, "Word level information:\n")
    			for _, wordInfo := range alternative.GetWords() {
    				startTime := wordInfo.GetStartTime()
    				endTime := wordInfo.GetEndTime()
    				fmt.Fprintf(w, "\t%4.1f - %4.1f: %v (speaker %v)\n",
    					float64(startTime.GetSeconds())+float64(startTime.GetNanos())*1e-9, // start as seconds
    					float64(endTime.GetSeconds())+float64(endTime.GetNanos())*1e-9,     // end as seconds
    					wordInfo.GetWord(),
    					wordInfo.GetSpeakerTag())
    			}
    		}
    	}
    
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
