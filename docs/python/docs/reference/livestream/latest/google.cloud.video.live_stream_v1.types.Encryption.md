---
url: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption
title: Class Encryption (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:49.242385+00:00
---

# Class Encryption (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Encryption (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.1  1.7.4  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.4  0.2.0  0.1.5 
    
    
    Encryption(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Encryption settings.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
Required. Identifier for this set of encryption options. The ID must be 1-63 characters in length. The ID must begin and end with a letter (regardless of case) or a number, but can contain dashes or underscores in between.   
`secret_manager_key_source` |  `[google.cloud.video.live_stream_v1.types.Encryption.SecretManagerSource](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption.SecretManagerSource)`   
For keys stored in Google Secret Manager. This field is a member of `oneof`_ `secret_source`.   
`drm_systems` |  `[google.cloud.video.live_stream_v1.types.Encryption.DrmSystems](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption.DrmSystems)`   
Required. Configuration for DRM systems.   
`aes128` |  `[google.cloud.video.live_stream_v1.types.Encryption.Aes128Encryption](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption.Aes128Encryption)`   
Configuration for HLS AES-128 encryption. This field is a member of `oneof`_ `encryption_mode`.   
`sample_aes` |  `[google.cloud.video.live_stream_v1.types.Encryption.SampleAesEncryption](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption.SampleAesEncryption)`   
Configuration for HLS SAMPLE-AES encryption. This field is a member of `oneof`_ `encryption_mode`.   
`mpeg_cenc` |  `[google.cloud.video.live_stream_v1.types.Encryption.MpegCommonEncryption](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Encryption.MpegCommonEncryption)`   
Configuration for MPEG-Dash Common Encryption (MPEG-CENC). This field is a member of `oneof`_ `encryption_mode`.   
  
## Classes 

### Aes128Encryption
    
    
    Aes128Encryption(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for HLS AES-128 encryption.

### Clearkey
    
    
    Clearkey(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Clearkey configuration.

### DrmSystems
    
    
    DrmSystems(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines configuration for DRM systems in use. If a field is omitted, that DRM system will be considered to be disabled.

### Fairplay
    
    
    Fairplay(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Fairplay configuration.

### MpegCommonEncryption
    
    
    MpegCommonEncryption(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for MPEG-Dash Common Encryption (MPEG-CENC).

### Playready
    
    
    Playready(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Playready configuration.

### SampleAesEncryption
    
    
    SampleAesEncryption(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for HLS SAMPLE-AES encryption.

### SecretManagerSource
    
    
    SecretManagerSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for secrets stored in Google Secret Manager.

### Widevine
    
    
    Widevine(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Widevine configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
