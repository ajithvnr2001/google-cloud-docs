---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy/
title: Measure and improve speech accuracy \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:05.836936+00:00
---

# Measure and improve speech accuracy  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Measure and improve speech accuracy Stay organized with collections  Save and categorize content based on your preferences. 

[Automated Speech Recognition (ASR)](https://en.wikipedia.org/wiki/Speech_recognition), also known as machine transcription or Speech-to-Text (STT), uses machine learning to turn audio containing speech into text. ASR has many applications from subtitling, to virtual assistants, to [Interactive Voice Responses (IVRs)](https://en.wikipedia.org/wiki/Interactive_voice_response), to dictation, and more. However, machine learning systems are rarely 100% accurate, and ASR is no exception. If you plan to rely on ASR for critical systems, it's very important to measure its accuracy or overall quality to understand how it performs in your broader system that integrates it.

Once you measure your accuracy, it's possible to tune the systems to provide even greater accuracy for your specific situation. In Google's [Cloud Speech-to-Text API](https://docs.cloud.google.com/speech-to-text), accuracy tuning can be done by choosing the most appropriate recognition model and by using our Speech Adaptation API. We offer a wide variety of models tailored for different use cases, such as long-form audio, medical or over-the-phone conversations.

## Defining speech accuracy

Speech accuracy can be measured in a variety of ways. It might be useful for you to use multiple metrics, depending on your needs. However, the industry standard method for comparison is [Word Error Rate (WER)](https://en.wikipedia.org/wiki/Word_error_rate), often abbreviated as WER. WER measures the percentage of incorrect word transcriptions in the entire set. A lower WER means that the system is more accurate.

You might also see the term, _ground truth_ , used in the context of ASR accuracy. Ground truth is the 100% accurate transcription, typically human-provided, that you use to compare and measure accuracy.

### Word Error Rate (WER)

WER is the combination of three types of transcription errors, which can occur:

  * **Insertion Error (I):** Words present in the hypothesis transcript that aren't present in the ground truth.
  * **Substitution errors (S):** Words that are present in both the hypothesis and ground truth but aren't transcribed correctly.
  * **Deletion errors (D):** Words that are missing from the hypothesis but present in the ground truth.



\\[WER = {S+R+Q \over N}\\]

To find the WER, add the total number of each one of these errors, and divide by the total number of words (N) in the ground truth transcript. The WER can be greater than 100% in situations with very low accuracy, for example, when a large amount of new text is inserted. Note: Substitution is essentially deletion followed by insertion, and some substitutions are less severe than others. For example, there might be a difference in substituting a single letter as opposed to a word.

### Relation of WER to a confidence score

The WER metric is independent from a [confidence score](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#confidence-values), and they usually don't correlate with each other. A confidence score is based on likelihood, while the WER is based on whether the word is correctly identified or not. If the word isn't correctly identified, this means that even minor grammatical errors can cause a high WER. A word that is correctly identified leads to a low WER, which can still lead to a low likelihood, which drives the confidence low if the word isn't that frequent or the audio is very noisy.

Similarly, a word that is frequently used can have a high likelihood to get transcribed by the ASR correctly, which drives the confidence score high. For example, when a difference is identified between "I" and "eye", a high confidence might occur, because "I" is a more popular word, but the WER metric is lowered by it.

In summary, the confidence and WER metrics are independent and shouldn't be expected to correlate.

### Normalization

When computing the WER metric, the machine transcription is compared to a human-provided ground truth transcription. The text from both transcriptions is normalized before comparison is done. Punctuation is removed, and capitalization is ignored when comparing the machine transcription with the human-provided ground-truth transcription.

### Ground-truth conventions

It is important to recognize that there isn't a single human-agreed transcription format for any given audio. There are many aspects to consider. For example, audio might have other non-speech vocalizations, like "huh", "yep", "umm". Some Cloud STT models, like ["medical_conversation"](https://docs.cloud.google.com/speech-to-text/docs/v1/medical-models), do include these vocalizations, while others don't. Therefore, it is important that ground-truth conventions match the conventions of the model being evaluated. The following high-level guidelines are used to prepare a ground-truth text transcription for a given audio.

  * In addition to standard letters, you can use the digits 0-9.
  * Don't use symbols like "@", "#", "$", ".". Use words like "at", "hash", "dollar", "dot".
  * Use "%" but only when preceded by a number; otherwise, use the word "percent".
  * Use "\$" only when followed by a number, like "Milk is \$3.99".

  * Use words for numbers less than 10.

    * For example, "I have four cats and 12 hats."
  * Use numbers for measures, currency, and large factors like million, billion, or trillion. For example, "7.5 million" instead of "seven and a half million."

  * Don't use abbreviations in the following cases:

Do's | Don'ts  
---|---  
Warriors versus Lakers | Warriors versus Lakers  
I live at 123 Main Street | I live at 123 Main St  



## Measuring speech accuracy

The following steps get you started with determining accuracy using your audio:

### Gather test audio files

Gather a representative sample of audio files to measure their quality. This sample should be random and should be as close to the target environment as possible. For example, if you want to transcribe conversations from a call center to aid in quality assurance, you should randomly select a few actual calls recorded on the same equipment that your production audio comes through. If your audio is recorded on your mobile phone or computer microphone and isn't representative of your use case, then don't use the recorded audio.

Record at least 30 minutes of audio to get a statistically significant accuracy metric. We recommend using between 30 minutes and 3 hours of audio. In this lab, the audio is provided for you.

### Get ground truth transcriptions

Get accurate transcriptions of the audio. This usually involves a single or a double-pass human transcription of the target audio. Your goal is to have a 100% accurate transcription to measure the automated results against.

It's important when getting ground truth transcriptions to match the transcription conventions of your target ASR system as closely as possible. For example, ensure that punctuation, numbers, and capitalization are consistent.

Obtain a machine transcription, and fix any issues in the text that you notice.

### Get the machine transcription

Send the audio to the Cloud Speech-to-Text API, and get your hypothesis transcription by using the [Cloud Speech-to-Text UI](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-console).

### Pair ground truth to the audio

In the UI tool, click **Attach ground truth** to associate a given audio file with the provided ground truth. After finishing the attachment, you can see your WER metric and the visualization of all the differences.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
