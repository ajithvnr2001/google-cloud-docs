---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/optimizing-audio-files-for-speech-to-text/
title: Optimize audio files for Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:06.436642+00:00
---

# Optimize audio files for Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/optimizing-audio-files-for-speech-to-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Optimize audio files for Cloud Speech-to-Text Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to perform a preflight check on audio files that you're preparing for use with [Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text). It provides background on audio file formats, describes how to optimize audio files for use with Cloud STT, and how to diagnose errors. The tutorial is designed for non-technical media and entertainment professionals and post-production professionals. It doesn't require in-depth knowledge of Google Cloud; it requires only basic knowledge of how to use the `gcloud` command-line tool with files that are stored both locally and in a [ Cloud Storage](https://docs.cloud.google.com/storage) bucket.

## Objectives

  * Install the [FFMPEG](https://ffmpeg.org/) tool.
  * Download the sample media files.
  * Play audio and video files using FFMPEG.
  * Extract, transcode, and convert audio file properties using FFMPEG.
  * Run Cloud STT on a variety of sample files that contain dialog.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Cloud STT](https://docs.cloud.google.com/speech-to-text)



You can use the [pricing calculator](https://cloud.google.com/products/calculator/#id=34aca7d4-2a34-4313-b46c-ae020143a834) to generate a cost estimate based on your projected usage.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




In this tutorial, you use Cloud Shell to perform the procedures, such as copying data from a Cloud Storage bucket to the Cloud Shell session. Cloud Shell is a shell environment with the Google Cloud CLI already installed. You use gcloud CLI use for many steps in this tutorial. You also install software and sample audio files on your local machine and run these same exercises from your terminal, as described in the Running tutorial examples in a local terminal section later.

**Note:** During this tutorial, you listen to several audio files. We recommend that you use headphones or wide-dynamic-range loudspeakers so that you're able to hear the differences in the audio quality of the files.

## Overview

In this tutorial, you use [FFMPEG](https://ffmpeg.org/) , an open source tool for recording, converting, and streaming audio and video. The tutorial provides more information about this tool later.

## Understand sound file attributes

This section describes typical audio file types, sample rates, bit depths, and recording media found in media production and post-production workflows.

To get the best results from Cloud STT, you must make sure that the files used for transcription are monaural (mono) files that meet certain minimum specifications as described later. If the files don't meet the specifications, you might need to generate modified files. For example, you might need to do the following:

  * Extract the audio data from a video file.
  * Extract a single monaural track from a multi-track audio file.
  * Transcode from one audio [codec](https://wikipedia.org/wiki/Codec) to another codec that's better suited for Cloud STT.



### Sample rate (frequency range)

The sample rate determines the frequency range of the audio file. It's based on the number of samples per second that constitute the audio file. Typically the highest reproducible frequency of a digital audio file is equivalent to half of the sample rate. For example, the highest frequency that can be reproduced from a 44.1 kHz audio file is roughly 22 kHz, which is at the top end of or beyond the frequency response range of a typical listener's hearing.

Sample rates in telephony and telecommunications tend to be in the 8 kHz to 16 kHz range. This tutorial focuses on formats specific to the media and entertainment industry, which are typically higher than 16 kHz. For more information about telephony and other sound applications, see [Transcribing phone audio with enhanced models](https://docs.cloud.google.com/speech-to-text/docs/v1/phone-model) .

We recommend a sample rate of at least 16 kHz in the audio files that you use for transcription with Cloud STT. Sample rates found in audio files are typically 16 kHz, 32 kHz, 44.1 kHz, and 48 kHz. Because intelligibility is greatly affected by the frequency range, especially in the higher frequencies, a sample rate of less than 16 kHz results in an audio file that has little or no information above 8 kHz. This can prevent Cloud STT from correctly transcribing spoken audio. Speech intelligibility requires information throughout the 2 kHz to 4 kHz range, although the harmonics (multiples) of those frequencies in the higher range are also important for preserving speech intelligibility. Therefore, keeping the sample rate to a minimum of 16 kHz is a good practice.

It's possible to convert from one sample rate to another. However, there's no benefit to up-sampling the audio, because the frequency range information is limited by the lower sample rate and can't be recovered by converting to a higher sample rate. This means that up-sampling from 8 kHz to 44.1 kHz would limit the reproducible frequency range to half of the lower sample rate, or roughly 4 kHz. In this tutorial, you listen to audio files recorded at various sample rates and bit depths so that you can hear the difference for yourself.

### Bit depth (dynamic range)

The bit depth of the audio file determines the range from the quietest sounds to the loudest sounds, as well as the signal-to-noise ratio of the file. Dynamic range has less of an effect on the quality of the transcription than the frequency response does, but bit depths at or below 8 bits can cause excessive quantization noise in the audio track, making accurate transcription difficult. (_Quantization errors_ are rounding errors between the analog input signal and the mapping of the digital output value of that signal. The errors cause audible distortion that directly affects the fidelity of the sound.) The recommended bit depth of the files for analysis with Cloud STT is 16 bits or greater. As with sampling frequency, there's no advantage to up-converting the bit depth from 8 to 16 bits, because the dynamic range information is limited to the original 8-bit format.

### Recording medium

The original recording medium can also affect the quality of the audio file. For example, audio content that was originally recorded on magnetic tape might have background hiss embedded in the file. In some cases, you might need to preprocess noisy audio in order to get better results in the transcription process when you use Cloud STT. Treatment of noisy recordings and background noise interference are beyond the scope of this tutorial. For more information, see [Best practices](https://docs.cloud.google.com/speech-to-text/docs/v1/best-practices-provide-speech-data) in the Cloud STT documentation.

## Introduction to FFMPEG

In this tutorial, you use FFMPEG to work with audio files. The FFMPEG toolset offers a wide variety of functions that include the following:

  * Playing an audio or video file.
  * Converting audio files into one of the recognized codecs by Cloud STT.
  * Converting audio file sample rates and bit rates to optimal configurations for analysis by Cloud STT.
  * Extracting individual audio tracks or streams from a transport stream file or video file.
  * Splitting stereo files into two monaural files.
  * Splitting 5.1 audio files into six monaural files.
  * Applying equalization and filtering to improve audio clarity.



You can also use the [ffprobe](https://ffmpeg.org/ffprobe.html) function of FFMPEG to reveal metadata that's associated with a media file. This is important when you want to diagnose problems that are related to file types and formats for machine learning analysis.

## Codecs recognized by Cloud STT

Although Cloud STT recognizes a number of audio file formats, it might not read or analyze certain codecs properly. The tutorial shows you how you can check that your content is in one of the supported file formats.

In the tutorial, you read the metadata information to reveal and correct potential problems before you use Cloud STT. The same tools allow you to convert the file to a supported format if you discover an incompatibility.

Cloud STT recognizes the following codecs:

  * FLAC: [Free Lossless Audio Codec](https://wikipedia.org/wiki/FLAC)
  * LINEAR16: An [uncompressed pulse code modulation (PCM) format](https://wikipedia.org/wiki/Audio_file_format#Uncompressed_audio_format) used in WAV, AIFF, AU, and RAW containers
  * MULAW: a PCM codec designed for telecommunications in the US and Japan
  * AMR: An adaptive multi-rate codec designed for speech
  * AMR_WB: A wide-band variation of AMR with twice the bandwidth of AMR
  * OGG_OPUS: A lossy codec designed for low-latency applications
  * SPEEX_WITH_HEADER_BYTE: A codex designed for [voice over IP](https://wikipedia.org/wiki/Voice_over_IP) (VOIP) applications



It's important to understand that codecs and file formats are not the same. The filename extension doesn't necessarily indicate that the codec used in creating the file can be read by Cloud STT.

This tutorial focuses on FLAC and LINEAR16 codecs, because they're frequently found in media workflow environments. Both are lossless formats.

If you use WAV files (which are in uncompressed linear PCM format) with Cloud STT, the files must be a maximum of 16-bit depth and encoded in a non–floating-point format. The `.wav` filename extension doesn't guarantee that the file can be read by Cloud STT. The Optimize audio files for analysis section of this tutorial provides an example of how to convert the file from floating point to integer (signed) bit depth in order to transcribe the file within Cloud STT.

## Initialize your environment

Before you perform the tasks for this tutorial, you must initialize your environment by installing FFMPEG, setting some environment variables, and downloading audio files. You use media files that are stored both in a Cloud Shell instance and stored in a Cloud Storage bucket. Using different sources lets you work with different capabilities of Cloud STT.

In this section, you install FFMPEG and set up environment variables that point to the sample data storage locations in your Cloud Shell instance storage and in a Cloud Storage bucket. The media files are the same in both locations, and some of the examples in this tutorial access files both from Cloud Shell and from the Cloud Storage bucket. You can install FFMPEG on your local machine and run these same exercises, as described later in the Running tutorial examples in a local terminal section.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In Cloud Shell, install the current version of FFMPEG:
         
         sudo apt update
         sudo apt install ffmpeg
         

  3. Verify that FFMPEG is installed:
         
         ffmpeg -version
         

If a version number is displayed, the installation was successful.

  4. Create a directory for the project files:
         
         mkdir project_files
         

  5. Create a directory for the output files that you'll create in a later step:
         
         mkdir output
         

  6. Download the sample audio files:
         
         gcloud storage cp gs://cloud-samples-data/speech/project_files/*.* ~/project_files/
         

  7. Create an environment variable for the Cloud Storage bucket name:
         
         export GCS_BUCKET_PATH=gs://cloud-samples-data/speech/project_files
         

  8. Create an environment variable for the Cloud Shell instance directory path that points to the downloaded sample audio files:
         
         export PROJECT_FILES=~/project_files
         




## Examine metadata in media files

When you analyze audio or video files with Cloud STT, you need to know the details of the file's metadata. This helps you identify inconsistencies or incompatible parameters that might cause problems.

**Note:** A FLAC file must contain the sample rate in the FLAC header in order to be submitted to the Cloud Speech-to-Text API.

In this section, you use the `ffprobe` command in FFMPEG to examine the metadata from multiple media files to understand a file's specifications.

  1. In Cloud Shell, reveal metadata for the `HumptyDumptySample4416.flac` file:
         
         ffprobe $PROJECT_FILES/HumptyDumptySample4416.flac
         

The output is the following:
         
         Input #0, flac, from '_project_files_ /HumptyDumptySample4416.flac':
           Duration: 00:00:26.28, start: 0.000000, bitrate: 283 kb/s
             Stream #0:0: Audio: flac, 44100 Hz, mono, s16
         

This output indicates the following metadata about the file:

     * The duration of the audio file is 26.28 seconds.
     * The bitrate is 283 KB per second.
     * The codec format is FLAC.
     * The sample rate is 44.1kHz.
     * The file is a single-channel mono file.
     * The bit depth is 16 bits (signed integer).
  2. Reveal metadata for the `HumptyDumptySampleStereo.flac` file:
         
         ffprobe $PROJECT_FILES/HumptyDumptySampleStereo.flac
         

The output is the following:
         
         Input #0, flac, from '_project_files_ /HumptyDumptySampleStereo.flac':
           Duration: 00:00:26.28, start: 0.000000, bitrate: 378 kb/s
             Stream #0:0: Audio: flac, 44100 Hz, stereo, s16
         

The differences between this file and the previous one is that this is a stereo file that has a higher bitrate (378 KB/second instead of 283 KB/second) because it contains two-channel playback instead of one mono track. All of the other values are the same.

You should check the number of channels in an audio file that you want to process using Cloud STT; the audio files should have only one audio channel. To transcribe multiple audio channels within the same file, we recommend that you script the commands as outlined in the Optimize audio files for analysis section later.

  3. Reveal metadata for a 5.1 audio mix file:
         
         ffprobe $PROJECT_FILES/Alice_51_sample_mix.aif
         

The output is the following:
         
         Duration: 00:00:58.27, bitrate: 4610 kb/s
             Stream #0:0: Audio: pcm_s16be, 48000 Hz, 5.1, s16, 4608 kb/s
         

Because this file is in a different format than either the mono or stereo file, you see additional information. In this case, the audio is in a linear PCM format, recorded at a 44.1 kHz sample rate and a 16-bit bit rate (signed integer, little-endian).

Notice the `5.1` designation. The data rate of 4608 Kbits per second in this file is significantly higher than the rate for either of the previous examples, because the audio file contains 6 audio tracks.

Later in this tutorial, you see how this file causes errors when you try to transcribe it using Cloud STT. More importantly, you'll see how to optimize the file in order to use it with Cloud STT without errors.




## Optimize audio files for analysis

As mentioned earlier, when you use Cloud STT, the audio files need to be single-channel mono files so that you avoid errors in the transcription process. The following table shows common audio formats and the conversion process for converting mono files for processing.

Current audio format | Conversion process | Output audio format  
---|---|---  
Mono | No extraction necessary | FLAC or LINEAR16  
Stereo | Split into 2 mono files or downmix to a mono file | FLAC or LINEAR16  
Multitrack (5.1) | Split into 6 mono files | FLAC or LINEAR16  
Multi-stream audio/video | Split into separate mono files | FLAC or LINEAR16  
  
To process files with multiple audio tracks, you extract mono tracks from the stereo file using FFMPEG or other audio editing tools. Alternatively, you can automate the process as described in [Transcribing audio with multiple channels](https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel#speech-multi-channel-protocol) section of the Cloud STT documentation. For this tutorial, you explore the option of using FFMPEG to extract individual mono tracks from the stereo file.

As shown in the previous section, you can use the `ffprobe` command to determine how many audio channels a file contains and then use the `ffmpeg` command to extract or convert the file to a mono format if necessary.

### Preview an error based on an invalid format

To see how an incorrect format affects transcription, you can try running Cloud STT on a file that is _not_ in the mono format.

  1. In Cloud Shell, run Cloud STT on the `HumptyDumptySampleStereo.flac` file:
         
         gcloud ml speech recognize $PROJECT_FILES/HumptyDumptySampleStereo.flac \
             --language-code='en-US'
         

The output is the following:
         
         ERROR: (gcloud.ml.speech.recognize) INVALID_ARGUMENT: Invalid audio channel count
         

Although the codec format, sample rate, and bit depth of the file are correct, the stereo descriptor means that there are two tracks in the audio file. Therefore, running Cloud STT causes an `Invalid audio channel count` error.

  2. Run the `ffprobe` command on the file:
         
         ffprobe $PROJECT_FILES/HumptyDumptySampleStereo.flac
         

The output is the following:
         
         Stream #0:0: Audio: flac, 44100 Hz, stereo, s16
         

This reveals that the Cloud STT error is caused by attempting to process a stereo file




For information about how to manage stereo files through scripting, see [Transcribing audio with multiple channels](https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel) in the Cloud STT documentation.

### Split a stereo file into multiple FLAC mono files

One example of how to avoid the multiple-tracks error is to extract two mono tracks from a stereo audio file. The resulting tracks are in FLAC format and are written to the output directory. When you extract two mono files from a stereo file, it's a good idea to create names for the extracted files that indicate the original file channel location. For example, in the following procedure, you designate the left channel by using the suffix `FL` and you designate the right channel by using the suffix `FR`.

If the audio sample to transcribe is in both channels, only one channel is used for the transcription. However, if different speakers are recorded on different channels, we recommend that you transcribe the channels separately. Cloud STT can recognize multiple voices within a single recording. However, isolating each voice onto separate channels results in higher confidence levels in the transcription. (The confidence value is also referred to as [_word error rate_](https://wikipedia.org/wiki/Word_error_rate) , or WER, in speech recognition.) For more information about working with multiple voices in the same recording, see [Separating different speakers in an audio recording](https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices) in the Cloud STT documentation.

  * In Cloud Shell, split the `HumptyDumptySampleStereo.flac` stereo file into 2 mono files:
        
        ffmpeg -i $PROJECT_FILES/HumptyDumptySampleStereo.flac -filter_complex "[0:a]channelsplit=channel_layout=stereo[left][right]" -map "[left]" output/HumptyDumptySample_FL.flac -map "[right]" output/HumptyDumptySample_FR.flac
        

The output is the following, which shows the `HumptyDumptySample_FL.flac` (front left channel) and`HumptyDumptySample_FR.flac` (front right channel) mono files.
        
        Output #0, flac, to 'HumptyDumptySample_FL.flac':
          Input #0, flac, from '_project_files_ /HumptyDumptySampleStereo.flac':
          Duration: 00:00:26.28, start: 0.000000, bitrate: 378 kb/s
            Stream #0:0: Audio: flac, 44100 Hz, stereo, s16
        Stream mapping:
          Stream #0:0 (flac) -> channelsplit
          channelsplit:FL -> Stream #0:0 (flac)
          channelsplit:FR -> Stream #1:0 (flac)
        (...)
        Output #0, flac, to 'HumptyDumptySample_FL.flac':
        (...)
        Stream #0:0: Audio: flac, 44100 Hz, 1 channels (FL), s16, 128 kb/s
        (...)
        Output #1, flac, to 'HumptyDumptySample_FR.flac':
        (...)
        Stream #1:0: Audio: flac, 44100 Hz, 1 channels (FR), s16, 128 kb/s
        (...)
        size=918kB time=00:00:26.27 bitrate= 286.2kbits/s speed= 357x
        video:0kB audio:1820kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
        

This file is now optimized for Cloud STT.




### Split a 5.1 audio file into multiple mono files

Another example of how to optimize audio files is to split 5.1 audio files into individual FLAC mono files. When referring to channels in a multichannel mix such as a 5.1 mix, the filename designations are typically different than in stereo or mono files. The left channel file is typically designated as `FL` for front left, and the right channel is designated as `FR` for front right. The remaining channels of a 5.1 mix are referred to here as `FC` for front center, `LFE` for low frequency effects, `BL` for back left (also known as surround left), and `BR` for back right (also known as surround right). These aren't standard designations, but they're a conventional practice for identifying the origin of a sound file.

Typically, in multi-channel audio files for motion pictures and television, the primary dialog is carried by the front center channel. This is usually the file to choose when you use Cloud STT, because it typically contains most of the dialog in the mix.

In a post-production environment, the primary elements of dialog, music, and effects are split into groups called _stems_ so that all dialog for a mix is kept separate from the music and effects until the final mix is done. Because the dialog stem consists only of dialog, Cloud STT gives better results when transcribing the stems rather than trying to pull the center channel from a final mix. This is because an extracted center channel might be mixed with non-dialog sounds, causing intelligibility to suffer.

  1. In Cloud Shell, split the `Alice_51_sample_mix.aif` file into FLAC files, specifying the output file names for each channel:
         
         ffmpeg -i $PROJECT_FILES/Alice_51_sample_mix.aif -filter_complex "channelsplit=channel_layout=5.1[FL][FR][FC][LFE][BL][BR]" -map "[FL]" output/Alice_FL.flac -map "[FR]" output/Alice_FR.flac -map "[FC]" output/Alice_FC.flac -map "[LFE]" output/Alice_LFE.flac -map "[BL]" output/Alice_BL.flac -map "[BR]" output/Alice_BR.flac
         

The output is the following:
         
         Duration: 00:00:55.00, bitrate: 4235 kb/s
           Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, 5.1, s16, 4233 kb/s
         Stream mapping:
           Stream #0:0 (pcm_s16le) -> channelsplit
           channelsplit:FL -> Stream #0:0 (flac)
           channelsplit:FR -> Stream #1:0 (flac)
           channelsplit:FC -> Stream #2:0 (flac)
           channelsplit:LFE -> Stream #3:0 (flac)
           channelsplit:BL -> Stream #4:0 (flac)
           channelsplit:BR -> Stream #5:0 (flac)
         Press [q] to stop, [?] for help
         Output #0, flac, to 'Alice_FL.flac':
         (...)
             Stream #0:0: Audio: flac, 44100 Hz, 1 channels (FL), s16, 128 kb/s
         (...)
         Output #1, flac, to 'output/Alice_FR.flac':
         (...)
             Stream #1:0: Audio: flac, 44100 Hz, 1 channels (FR), s16, 128 kb/s
         (...)
         Output #2, flac, to 'output/Alice_FC.flac':
         (...)
             Stream #2:0: Audio: flac, 44100 Hz, mono, s16, 128 kb/s
         (...)
         Output #3, flac, to 'output/Alice_LFE.flac':
         (...)
             Stream #3:0: Audio: flac, 44100 Hz, 1 channels (LFE), s16, 128 kb/s
         (...)
         Output #4, flac, to 'output/Alice_BL.flac':
         (...)
             Stream #4:0: Audio: flac, 44100 Hz, 1 channels (BL), s16, 128 kb/s
         (...)
         Output #5, flac, to 'output/Alice_BR.flac':
         (...)
             Stream #5:0: Audio: flac, 44100 Hz, 1 channels (BR), s16, 128 kb/s
         (...)
         

  2. Click the following file to listen to it. This file is in the Cloud Storage bucket, and when you click the name, the file plays in a new tab in the browser.
         
         [Alice_mono_downmix.flac](https://storage.googleapis.com/cloud-samples-data/speech/listen/Alice_mono_downmix.flac)
         

  3. Listen to the FC (center-only channel file) that you just created. (The dialog starts after a few seconds of silence.)
         
         [Alice_FC.flac](https://storage.googleapis.com/cloud-samples-data/speech/listen/Alice_FC.flac)
         

Notice the difference in clarity from the previous file. This track is based on only the dialog portion of the mix.




## Test audio file quality

Before you convert the media files using Cloud STT, it's a good idea to listen to the files to determine whether they have anomalies in the sound quality that might prevent the ML tools from providing accurate results. In this section, you play the files in your browser by clicking the file names. (We recommend that you use headphones or wide-dynamic-range loudspeakers.)

### Listen to audio from a video file

  1. Click the following file to play it:
         
         [HumptyDumptySample4416.flac](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample4416.flac?_ga=2.212195793.-415293760.1529942435)
         

This file has a frequency of 44.1 kHz and a bit depth of 16 bits. Notice the clear, undistorted fidelity and the intelligibility of this file. This is a good candidate for transcription using Cloud STT.

  2. Play the following sample 5.1 format video file to hear a surround mix with non-dialog in all channels except for the center channel:
         
         [sample_51_mix_movie.mp4](https://storage.cloud.google.com/cloud-samples-data/speech/project_files/sample_51_mix_movie.mp4)
         

The file is designed for playback on a 5.1 audio system; if you're using only headphones or a two-channel system, not all of the channels might be audible during playback. (In order to hear all six of the channels, playback would need to be decoded on a 5.1 system or you would need to create a two-channel stereo downmix.)

Ideally, you use the dialog-only channel for Cloud STT. The sample file has non-dialog audio in five channels and dialog in one channel. In the Optimize audio files for analysis section later, you learn how to extract the six individual mono audio channels that are encoded in the 5.1 file in order to listen to each track. This lets you isolate the dialog-only channel (typically the center or front-center channel) from the non-dialog channels in order to improve the ability of Cloud STT to transcribe the file.




### Test the same file at different sample rates

The following table lists multiple versions of the same audio file for you to listen to, each with a different bit depth and sample rate.

Audio file | Sample rate/bit depth  
---|---  
[`HumptyDumptySample4416.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample4416.flac?_ga=2.15063283.-415293760.1529942435) | 44.1 kHz/16-bit Linear PCM  
[`HumptyDumptySample2216.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample2216.flac?_ga=2.14504562.-415293760.1529942435) | 22 kHz/16-bit Linear PCM  
[`HumptyDumptySample1616.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample1616.flac?_ga=2.14504562.-415293760.1529942435) | 16 kHz/16-bit Linear PCM  
[`HumptyDumptySample1116.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample1116.flac?_ga=2.14504562.-415293760.1529942435) | 11 kHz/16-bit Linear PCM  
[`HumptyDumptySample0808.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample0808.flac?_ga=2.241138886.-415293760.1529942435) | 8 kHz/8-bit Linear PCM  
[`HumptyDumptyUpSample4416.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptyUpSample4416.flac?_ga=2.241138886.-415293760.1529942435) | 44.1 kHz (upsampled)/16-bit Linear PCM   
[`HumptyDumptySample4408.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample4408.flac?_ga=2.252655180.-415293760.1529942435) | 44.1 kHz/8-bit Linear PCM  
[`HumptyDumptySample4408to16.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/HumptyDumptySample4408to16.flac?_ga=2.252655180.-415293760.1529942435) | 44.1 kHz/16-bit Linear PCM (up-converted)  
  
  1. For each file in the preceding table, click the filename to listen to the file. (The audio player opens in a new tab of the browser.) Notice the difference in quality when the sample rate is decreased.

The fidelity of the 16-bit files is reduced at the lower sample rates and the signal-to-noise ratio is drastically reduced in the 8-bit file versions due to the quantization errors. The last file in the table is an original 8kHz 8-bit file that's been upsampled to 44.1 kHz/16-bit. Notice that the sound quality is the same as the 8 kHz/8-bit file.

  2. In Cloud Shell, examine the metadata for the `HumptyDumptySampleStereo.flac` file:
         
         ffprobe $PROJECT_FILES/HumptyDumptySampleStereo.flac
         

The output is the following:
         
         Input #0, flac, from '_project_files_ /HumptyDumptySampleStereo.flac':
             Duration: 00:00:26.28, start: 0.000000, bitrate: 378 kb/s
             Stream #0:0: Audio: flac, 44100 Hz, stereo, s16
         

The output shows the following:

     * The file duration is 26 seconds and 28 frames. This information is useful for advanced use cases, for example, if you want to process files longer than 1 minute by using the `gcloud speech recognize-long-running` command.
     * The bitrate of the file is 378 kb/s.
     * The number of streams in the file is 1. (This is different than the number of channels.)
     * The sample rate of the file is 44.1kHz.
     * The number of channels of audio is 2 (stereo).
     * The bit depth of the file is 16 bits.

A transport stream can contain a number of streams, including audio, video, and metadata. Each of these has different characteristics, such as the number of audio channels per stream, the codec of the video streams, and the number of frames-per-second of the video streams.

Notice that the metadata reveals that this is a stereo file. This is important, because the default number of audio channels recommended for analysis with Cloud STT is one mono channel.




## Transcribe files using Cloud STT

Now that you've extracted mono files, you can use Cloud STT to transcribe the audio tracks. You use the `gcloud ml speech` command, which invokes the Cloud STT API.

  * Transcribe the clean `Alice_FC.flac` dialog file:
        
        gcloud ml speech recognize ~/output/Alice_FC.flac \
            --language-code='en-US' --format=text
        

Allow a few seconds to complete the transcription. The output is the following:
        
        results[0].alternatives[0].confidence: 0.952115
        results[0].alternatives[0].transcript: the walrus and the carpenter were walking close at hand they whip like anything to see such quantities of sand if this were only cleared away they said it would be grand
        results[1].alternatives[0].confidence: 0.968585
        results[1].alternatives[0].transcript: " if 7 Maids with seven mops swept it for half a year do you suppose the walrus said that they could get it clear I doubt it said the Carpenter and shed a bitter tear"
        results[2].alternatives[0].confidence: 0.960146
        results[2].alternatives[0].transcript: " oysters come and walk with us the walrus did beseech a pleasant walk a pleasant talk along the Briny Beach we cannot do with more than four to give a hand to each the eldest oyster look at him but never a word he said the eldest oyster winked his eye and shook his heavy head"
        




### Transcribe a "dirty" track

You might have audio files of people speaking that have other sound elements mixed into the dialog. These are often referred to as "dirty" tracks as opposed to the "clean" dialog-only track that have no other elements mixed in. Although Cloud STT can recognize speech in noisy environments, the results might be less accurate than for clean tracks. Additional [audio filtering and processing](https://docs.cloud.google.com/speech-to-text/docs/v1/best-practices-provide-speech-data) might be necessary to improve the intelligibility of the dialog before you analyze the file with Cloud STT.

In this section, you transcribe a mono downmix of the 5.1 audio file that you analyzed in the previous example.

  1. In Cloud Shell, transcribe the `Alice_mono_downmix.flac` file:
         
         gcloud ml speech recognize $PROJECT_FILES/Alice_mono_downmix.flac \
             --language-code='en-US' --format=text
         

The output is the following:
         
         results[0].alternatives[0].confidence: 0.891331
         results[0].alternatives[0].transcript: the walrus and the carpenter Milwaukee Corsicana they reflect anything to see such quantity if this were only
         results[1].alternatives[0].confidence: 0.846227
         results[1].alternatives[0].transcript: " it's Sunday 7th March 23rd happy few supposed former said that they could get it clear I doubt it to the doctor and she said it did it to just come and walk with us"
         results[2].alternatives[0].confidence: 0.917319
         results[2].alternatives[0].transcript: " along the Briny Beach it cannot do with more than four to give a hand to each the eldest oyster look at him but he said it was poised to Rich's eye and shook his head"
         

The results of this analysis are inaccurate because of the additional sounds that mask the dialog. The transcript confidence level is below 85%. And as you can see by the output, the text doesn't match the dialog in the recording as closely as it should.




### Transcribe audio files of different sample rates and bit depths

To understand more about how the sample rate and bit depth affect the transcription, in this section you transcribe the same audio file recorded in a variety of sample rates and bit depths. This lets you see the confidence level of Cloud STT and its relationship to the overall sound quality.

  1. Click the file names in the following table to listen to the sample, and notice the difference in quality. Each time you click the name of a file, the audio file plays in a new tab in the browser.

Audio filename | File specifications  
---|---  
[`Speech_11k8b.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/Speech_11k8b.flac?_ga=2.249960643.-415293760.1529942435) | 11025Hz sample rate, 8-bit depth  
[`Speech_16k8b.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/Speech_16k8b.flac?_ga=2.249960643.-415293760.1529942435) | 16kHz sample rate, 8-bit depth  
[`Speech_16k16b.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/Speech_16k8b.flac?_ga=2.249893059.-415293760.1529942435) | 16kHz sample rate, 16-bit depth  
[`Speech_441k8b.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/Speech_441k8b.flac?_ga=2.249893059.-415293760.1529942435) | 44100Hz sample rate, 8-bit depth  
[`Speech_441k16b.flac`](https://storage.cloud.google.com/cloud-samples-data/speech/listen/Speech_441k16b.flac?_ga=2.249893059.-415293760.1529942435) | 44100Hz sample rate, 16-bit depth  
  2. In Cloud Shell, transcribe the `Speech_11k8b.flac` file, which represents the lowest audio quality in this example:
         
         gcloud ml speech recognize $PROJECT_FILES/Speech_11k8b.flac \
             --language-code='en-US' --format=text
         

The output is the following:
         
         results[0].alternatives[0].confidence: 0.77032
         results[0].alternatives[0].transcript: number of Pentacle represent
         results[1].alternatives[0].confidence: 0.819939
         results[1].alternatives[0].transcript: " what people can get in trouble if we take a look at the X again"
         

  3. Transcribe the `Speech_441k16b.flac` file, which is recorded at significantly higher fidelity:
         
         gcloud ml speech recognize $PROJECT_FILES/Speech_441k16b.flac \
             --language-code='en-US' --format=text
         

The output is the following:
         
         results[0].alternatives[0].confidence: 0.934018
         results[0].alternatives[0].transcript: that gives us the number of pixels per inch when magnified to a 40-foot screen size now we take that number and multiply it by the distance between our eyes the interocular distance of 2 and 1/2 inch number of 10 pixels in other words on a 40-foot screen 10 pixels of information represents 2 and 1/2 in anything farther apart than that and positive Parallax is going to start to force the eyes to rotate that word in order to use the image
         results[1].alternatives[0].confidence: 0.956892
         results[1].alternatives[0].transcript: " where people tend to get in trouble is by looking at these images on a small monitor now if we take a look at the same math using a smaller monitor in this case 60 in the screen size in the resolution to multiply It Again by the distance between our eyes we end up with eighty pixels of Divergence on a monitor which equals two and a half inches so on the monitor things might look fine but when magnified up to the larger screen in this case for defeat we've created a situation that's eight times what we can stand to look at its very painful and should be avoided"
         

Notice the difference in confidence in the output of the two examples. The first file (`Speech_11k8b.flac`), which was recorded at 11kHz with an 8-bit depth, has a confidence level below 78%. The second file has a confidence level of about 94%.

  4. Optionally, transcribe the other files listed in the table in step 1 to make further comparisons between audio file sample rate and bit-depth accuracy.




The following table shows a summary of the output of Cloud STT for each of the files listed in the table in step 1 of the preceding procedure. Notice the difference in confidence value results for each file type. (Your results might vary slightly.) The transcriptions of the audio files that have the lower sample and bit rates tend to have lower confidence results due to the poorer sound quality.

Audio filename | Confidence (section one) | Confidence (section two)  
---|---|---  
`Speech_11k8b.flac` | 0.770318 | 0.81994  
`Speech_16k8b.flac` | 0.935356 | 0.959684  
`Speech_16k16b.flac` | 0.945423 | 0.964689  
`Speech_44.1k8b.flac` | 0.934017 | 0.956892  
`Speech_44.1k16b.flac` | 0.949069 | 0.961777  
  
## Optimize video files for analysis

This section of the tutorial takes you through the steps that are required in order to extract 5.1 audio from a movie file.

  1. In Cloud Shell, extract 6 mono channels from a 5.1 movie file and convert the individual files to FLAC format:
         
         ffmpeg -i $PROJECT_FILES/sample_51_mix_movie.mp4 -filter_complex "channelsplit=channel_layout=5.1[FL][FR][FC][LFE][BL][BR]" -map "[FL]" output/sample_FL.flac -map "[FR]" output/sample_FR.flac -map "[FC]" output/sample_FC.flac -map "[LFE]" output/sample_LFE.flac -map "[BL]" output/sample_BL.flac -map "[BR]" output/sample_BR.flac
         

This command extracts the following files into the output directory:
         
         sample_BL.flac
         sample_BR.flac
         sample_FC.flac
         sample_FL.flac
         sample_FR.flac
         sample_LFE.flac
         

  2. Check the metadata of the sample file:
         
         ffprobe $PROJECT_FILES/Speech_48kFloat.wav
         

The output is the following:
         
         Duration: 00:00:05.12, bitrate: 1536 kb/s
         Stream #0:0: Audio: pcm_f32le ([3][0][0][0] / 0x0003), 48000 Hz, mono, flt, 1536 kb/s
         

The `pcm_f32le` and `flt` metadata values indicate that this file has a floating-point bitrate. You need to convert a floating-point bit rate WAV file to a signed-integer format.

  3. Convert the file's bitrate to a signed-integer format:
         
         ffmpeg -i $PROJECT_FILES/Speech_48kFloat.wav -c:a pcm_s16le output/Speech_48k16bNonFloatingPoint.wav
         

This command creates a new WAV file whose bitrate is in signed-integer format.

  4. Examine the metadata of the newly created file:
         
         ffprobe ~/output/Speech_48k16bNonFloatingPoint.wav
         

The output is the following:
         
         Duration: 00:00:05.12, bitrate: 768 kb/s
         Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 48000 Hz, 1 channels, s16, 768 kb/s
         

The metadata now shows that the bitrate in the converted file is in a signed-integer (little-endian) format, as shown by the `pcm_s16le` and `s16` designations.




## Run tutorial examples in a local terminal

You can run all of the examples in this tutorial from a terminal on your local computer. Running the examples locally provides an important capability to play audio and video files directly by using the `ffplay` command (instead of listening to them in the browser).

  1. In a terminal on your local computer, install the FFMPEG tool:
         
         sudo apt update
         sudo apt install ffmpeg
         

  2. Download the sample files to your local machine:
         
         gcloud storage cp gs://cloud-samples-data/speech/project_files/*.* local_destination_path
         

Replace local_destination_path with the location to put the sample files.

  3. Set the `LOCAL_PATH` environment variable to the location on your computer where you downloaded the sample files:
         
         export LOCAL_PATH=local_destination_path
         

Replace local_destination_path with the path from the previous step.

  4. In the terminal, use the `ffplay` command in the terminal to listen to a sample audio file:

     * Audio file: `ffplay` `$LOCAL_PATH/HumptyDumpty4416.flac`
     * Video file: `ffplay $LOCAL_PATH/sample_51_mix_movie.mp4`
     * Cloud Storage bucket playback: `ffplay` `$GCS_BUCKET_PATH/HumptyDumpty4416.flac`

Experiment in your local terminal with the examples that you worked with earlier in this tutorial. This helps you to better understand how to best use Cloud STT.




## Troubleshooting

Errors can be caused by a number of factors, so it's worth examining some common errors and learning how to correct them. You might experience multiple errors on a given audio file that prevent the transcription process from completing.

### Audio is too long

The `gcloud speech recognize` command can process files that are up to 1 minute long. For example, try the following example:
    
    
    gcloud ml speech recognize $PROJECT_FILES/HumptyDumpty4416.flac \
        --language-code='en-US' --format=text
    

The output is the following:
    
    
    ERROR: (gcloud.ml.speech.recognize) INVALID_ARGUMENT: Request payload size exceeds the limit: 10485760 bytes.
    

The error is caused by trying to use the `speech recognize` command to process a file that's longer than 1 minute.

For files that are longer than 1 minute and shorter than 80 minutes, you can use the `speech recognize-long-running` command. To see how long the file is, you can use the `ffprobe` command, as in the following example:
    
    
    ffprobe $PROJECT_FILES/HumptyDumpty4416.flac
    

The output is similar to the following:
    
    
    Duration: 00:04:07.91, start: 0.000000, bitrate: 280 kb/s
    Stream #0:0: Audio: flac, 44100 Hz, mono, s16
    

Notice that the running time of the audio file is approximately 4 minutes and 8 seconds.

### Read large files from your local computer

The `speech recognize-long-running` command can process files only up to 1 minute in length from the local computer. To see where you might run into an error, try using the `speech recognize-long-running` command in Cloud Shell for a longer file:
    
    
    gcloud ml speech recognize-long-running $PROJECT_FILES/HumptyDumpty4416.flac \
        --language-code='en-US' --format=text
    

The output is the following:
    
    
    ERROR: (gcloud.ml.speech.recognize-long-running) INVALID_ARGUMENT: Request payload size exceeds the limit: 10485760 bytes.
    

This error isn't the result of the length of the audio, but because of the size of the file on the local machine. When you use the `recognize-long-running` command, the file must be in a Cloud Storage bucket.

To read files longer than 1 minute, use the `recognize-long-running` to read a file from a Cloud Storage bucket, as in the following command:
    
    
    gcloud ml speech recognize-long-running $GCS_BUCKET_PATH/HumptyDumpty4416.flac \
        --language-code='en-US' --format=text
    

This process takes a few minutes to complete.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Read the [Cloud STT documentation](https://docs.cloud.google.com/speech-to-text/docs) .
  * Read the documentation for the [speech recognize](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize) command and the [speech recognize-long-running](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running) command.
  * Work through the [Speech to text transcription with the Cloud Speech-to-Text API](https://developers.google.com/codelabs/cloud-speech-intro) codelab.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
