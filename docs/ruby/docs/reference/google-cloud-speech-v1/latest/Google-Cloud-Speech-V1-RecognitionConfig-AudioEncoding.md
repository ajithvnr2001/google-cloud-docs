---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-RecognitionConfig-AudioEncoding/
title: Cloud Speech-to-Text V1 API - Module Google::Cloud::Speech::V1::RecognitionConfig::AudioEncoding (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:04.916448+00:00
---

# Cloud Speech-to-Text V1 API - Module Google::Cloud::Speech::V1::RecognitionConfig::AudioEncoding (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-RecognitionConfig-AudioEncoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V1 API - Module Google::Cloud::Speech::V1::RecognitionConfig::AudioEncoding (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.17.0  0.16.2  0.15.0  0.14.0  0.13.1  0.12.1  0.11.0  0.10.2  0.9.0  0.8.0  0.7.3 

Reference documentation and code samples for the Cloud Speech-to-Text V1 API module Google::Cloud::Speech::V1::RecognitionConfig::AudioEncoding.

The encoding of the audio data sent in the request.

All encodings support only 1 channel (mono) audio, unless the `audio_channel_count` and `enable_separate_recognition_per_channel` fields are set.

For best results, the audio source should be captured and transmitted using a lossless encoding (`FLAC` or `LINEAR16`). The accuracy of the speech recognition can be reduced if lossy codecs are used to capture or transmit audio, particularly if background noise is present. Lossy codecs include `MULAW`, `AMR`, `AMR_WB`, `OGG_OPUS`, `SPEEX_WITH_HEADER_BYTE`, `MP3`, and `WEBM_OPUS`.

The `FLAC` and `WAV` audio file formats include a header that describes the included audio content. You can request recognition for `WAV` files that contain either `LINEAR16` or `MULAW` encoded audio. If you send `FLAC` or `WAV` audio file format in your request, you do not need to specify an `AudioEncoding`; the audio encoding format is determined from the file header. If you specify an `AudioEncoding` when you send send `FLAC` or `WAV` audio, the encoding configuration must match the encoding described in the audio header; otherwise the request returns an [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] error code.

## Constants 

### ENCODING_UNSPECIFIED

**value:** 0  
Not specified.

### LINEAR16

**value:** 1  
Uncompressed 16-bit signed little-endian samples (Linear PCM).

### FLAC

**value:** 2  
`FLAC` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.

### MULAW

**value:** 3  
8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.

### AMR

**value:** 4  
Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be 8000.

### AMR_WB

**value:** 5  
Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be 16000.

### OGG_OPUS

**value:** 6  
Opus encoded audio frames in Ogg container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.

### SPEEX_WITH_HEADER_BYTE

**value:** 7  
Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The [Speex](https://speex.org/) encoding supported by Cloud Speech API has a header byte in each block, as in MIME type `audio/x-speex-with-header-byte`. It is a variant of the RTP Speex encoding defined in [RFC 5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence of blocks, one block per RTP packet. Each block starts with a byte containing the length of the block, in bytes, followed by one or more frames of Speex data, padded to an integral number of bytes (octets) as specified in RFC 5574. In other words, each RTP header is replaced with a single byte containing the block length. Only Speex wideband is supported. `sample_rate_hertz` must be 16000.

### MP3

**value:** 8  
MP3 audio. MP3 encoding is a Beta feature and only available in v1p1beta1. Support all standard MP3 bitrates (which range from 32-320 kbps). When using this encoding, `sample_rate_hertz` has to match the sample rate of the file being used.

### WEBM_OPUS

**value:** 9  
Opus encoded audio frames in WebM container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
