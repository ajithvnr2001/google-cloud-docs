---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-audio-files-hold-music/
title: Custom Audio Files & Hold Music Details \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:49.293817+00:00
---

# Custom Audio Files & Hold Music Details  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-audio-files-hold-music/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Custom Audio Files & Hold Music Details Stay organized with collections  Save and categorize content based on your preferences. 

Almost all messages that are played to callers can be customized with your audio recordings. Following are recommendations and best practices when using custom audio messages.

### File types

Supports WAV and MP3 audio formats.

Note that changing the extension of the audio file does not change the format of the file, so it is not possible to rename the file. A converter must be used to do so and can be either downloaded or found online.

### Best practices

  * The telephony standard is 8-bit PCM mono with a sampling rate of 8 Khz. That means a 64 kbit per second bitrate (8 kHz sampling frequency × 8 bits per sample).

  * Voice files can have file size reduced, which also affects quality. The minimum recommended levels are 32 kb per second or 16 kb per second.

  * That standard is bandwidth-limited to the 300 Hz - 8Khz audio range and is designed for voice and provides acceptable voice-quality results.

  * CCAI Platform utilizes the OPUS codec where applicable and supports a constant or variable bitrate of 6 kb per second to 510 kb per second, but it is still recommended to keep to the 64 kb per second bitrate for telephony purposes.


**Note:** your audio will sound different on a landline versus a mobile device. It's best to check your audio once uploaded to the platform.

### Recording

For any audio prompts, it's best to start with the highest-quality possible source recording. This means a voice in a room with good acoustics, recorded carefully with a professional quality microphone and preamp.

You can achieve the best results with careful mic placement. For voice, place the microphone adjacent to the speaker's mouth in order to avoid distortion due to plosives (like "P" and "T" sounds). You can also use a pop filter or shield on your microphone to avoid this distortion.

Record your source at a 48Khz sample rate to a 16-bit or 24-bit mono uncompressed WAV file. Instead of mono, you can record in stereo. If you convert in stereo, you'll need to convert the file to mono before uploading to CCAI Platform.

### Post-processing

After recording, archive your recordings in that source format. This can be done either by compressing it into a ZIP or RAR file and storing it to an external drive or by uploading it to a cloud service. Keep in mind that uncompressed audio files will be large. Transcoding to audio that is telephony standard will degrade the quality to a large degree.

It's a good idea to keep an archive copy of the initial high-quality audio so that you have the option of reusing the source material or correcting any sound artifacts from post-processing.

Use an audio software editing program such as [_Audacity_](https://www.audacityteam.org/) (a free, multi-platform audio editing application) to:

  * Trim leading and trailing silence from the recording.

  * Normalize the volume.

  * Remove background noise.

  * Apply equalization to a copy of the source file.




When exporting from Audacity or another program, make sure the export settings are correct.

You may need to download an MP3 encoder for exporting to the MP3 format. Follow the directions in your audio editor for more information.

If you have stereo sources, convert these to mono prior to your upload. This ensures that you won't encounter any stereo-to-mono phase artifacts.

**Make sure your files do not exceed 15 MB in size.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
