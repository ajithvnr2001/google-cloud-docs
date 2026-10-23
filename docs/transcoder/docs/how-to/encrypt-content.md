---
url: https://docs.cloud.google.com/transcoder/docs/how-to/encrypt-content/
title: Encrypt transcoded content \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:12.898116+00:00
---

# Encrypt transcoded content  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/encrypt-content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Encrypt transcoded content Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to encrypt transcoded content. The Transcoder API does not create or manage encryption keys or licenses directly. Instead, you must use a third-party digital rights management (DRM) provider for these features. Once encryption keys have been created for your media, pass those keys to the Transcoder API using [Secret Manager](https://docs.cloud.google.com/secret-manager).

Encryption settings are specified in the [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) settings. The Transcoder API transcodes the content with the provided encryption settings. The output manifest includes the information required to decrypt the content within your media player of choice.

## Supported configurations

Streaming protocol | Container | DRM system | Encryption scheme  
---|---|---|---  
HLS | TS | ClearKey | aes128  
HLS | TS | FairPlay | sampleAes  
HLS | fMP4 | FairPlay | mpegCenc cbcs only  
MPEG-DASH | fMP4 | Widevine | mpegCenc cenc or cbcs  
MPEG-DASH | fMP4 | PlayReady | mpegCenc cenc or cbcs  
  
## Add the encryption key to Secret Manager

Before you begin, create your encryption keys using your third-party DRM provider of choice.

The Transcoder API requires your secret to contain the encryption key in the following JSON format, along with other necessary information.

See the [DRM protocol documentation](https://docs.cloud.google.com/transcoder/docs/reference/drm) for a description of each field. Note that you need to convert from snake case to camel case for JSON format.

### Example JSON
    
    
    {
      "encryptionKeys": [
        {
          // Key for FairPlay configuration.
          "keyId": "d569cb35bd0548c7a99d92feb381df13",
          "key": "f1967daca83e81f38d80aa741e7b32c2",
          "iv": "8d80aa741e7b32c2f1967daca83e81f3",
          "keyUri": "skd://d569cb35bd0548c7a99d92feb381df13",
          "matchers": [
            {
              "muxStreams": ["ts_fairplay"]
            }
          ]
        },
        {
          // Key for Widevine configurations.
          "keyId": "44ec248b048c43a6a6ee58a752c6f9f8",
          "key": "f1967daca83e81f38d80aa741e7b32c2",
          "keyUri": "skd://44ec248b048c43a6a6ee58a752c6f9f8",
          "matchers": [
            {
              "muxStreams": [
                "fmp4_widevine_cenc_video",
                "fmp4_widevine_cenc_audio",
                "fmp4_widevine_cbcs_video",
                "fmp4_widevine_cbcs_audio"
              ]
            }
          ]
        },
        {
          // Key for PlayReady configurations.
          "keyId": "8beed229709f480bb6004ec0f33e82d1",
          "key": "ad20cd838f354dcc8a77c443d08ff09f",
          "keyUri": "skd://8beed229709f480bb6004ec0f33e82d1",
          "matchers": [
            {
              "muxStreams": [
                "fmp4_playready_cenc_video",
                "fmp4_playready_cenc_audio",
                "fmp4_playready_cbcs_video",
                "fmp4_playready_cbcs_audio"
              ]
            }
          ]
        },
        {
          // Key for all ClearKey configurations.
          "keyId": "3d9dccb479c64adbb6e514790caa7822",
          "key": "my-key",
           // A URI that the media player can access
          "keyUri": "https://example.com/keys/my-key.bin",
          "iv": "8d80aa741e7b32c2f1967daca83e81f3"
          // No `matchers` field. This is the default key to use when none of the keys above match.
        }
      ]
    }
    

If your encryption configuration (for example, FairPlay) requires an explicit initialization vector (IV) but it is not included, the API will use the value of `keyId` for the value of `iv`.

To add and configure your encryption key, do the following:

  1. Using the preceding JSON data, add your encryption key to Secret Manager following the steps at [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

**Note:** Implementing Secret Manager might incur some [additional costs](https://cloud.google.com/secret-manager/pricing).
  2. Configure IAM permissions on your secret so that the Transcoder API can access the secret content. To do this, grant the `secretmanager.secretAccessor` role to the `service-PROJECT_NUMBER@gcp-sa-transcoder.iam.gserviceaccount.com` service account (this is similar to how the [service account has access to your Cloud Storage buckets](https://docs.cloud.google.com/transcoder/docs/access-control#access_to_gcs_pubsub)).

  3. Find the resource name of the secret version you created (for example, `projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/VERSION_ID`). You need this name to configure the Transcoder API job.

  4. For a ClearKey configuration, the `keyUri` field must reference a URI which the media player has access to. Do the following:

     1. Create a binary file from the key by running the following command:
            
            echo "my-key" | xxd -r -p > my-key.bin
            

     2. Upload the file to a public URI. To use Cloud Storage, see [Discover object storage with the Google Cloud console](https://docs.cloud.google.com/storage/docs/discover-object-storage-console).




## Create a job

Encryption settings are specified using objects in the [`encryptions`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.encryptions) array at the `JobConfig` level. A unique identifier ([`id`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#Encryption)) is assigned to each different configuration. Each `muxStream` uses an identifier to indicate which encryption configuration to use, or omits that field to remain unencrypted.

### JSON format
    
    
    {
      // Other JobConfig settings.
    
      "encryptions": [
        {
          // Identifier for this encryption configuration, to be specified in muxStream(s).
          "id": string,
          // Configuration for secrets stored in Google Secret Manager.
          "secretManagerKeySource": {
            // The name of the Secret Version containing the encryption key.
            // `projects/{project}/secrets/{secret_id}/versions/{version_number}`
            // Using {version_number} of `latest` is not supported.
            "secretVersion": string
          },
          // DRM system(s) that will be used. At least one must be specified. If a DRM system
          // is omitted, it will be considered disabled.
          "drmSystems": {
            // Widevine configuration.
            "widevine": {},
            // FairPlay configuration.
            "fairplay": {},
            // PlayReady configuration.
            "playready": {},
            // ClearKey configuration.
            "clearkey": {}
          },
          // Union field encryption_mode can be only one of the following:
          // Configuration for HLS AES-128 encryption.
          "aes128": {},
          // Configuration for HLS SAMPLE-AES encryption.
          "sampleAes": {},
          // Configuration for MPEG-DASH Common Encryption (MPEG-CENC).
          "mpegCenc": {
            // Specify the encryption scheme. Supported schemes:
            // - `cenc` - AES-CTR subsample
            // - `cbcs`- AES-CBC subsample pattern
            "scheme": string
          }
          // End of list of possible types for union field encryption_mode.
        }
        // Any other encryption configurations.
      ],
      "muxStreams": [
        {
          // Unique identifier for the muxStream.
          "key": string,
          // Identifier of the encryption configuration for the muxStream.
          "encryptionId": string
          // … other muxStream settings.
        }
        // Other muxStreams.
      ],
    
      // Other JobConfig settings.
    }
    

### Example (ClearKey)

The following example configures AES-128 muxStreams in HLS manifests, and MPEG-CENC muxStreams (cenc and cbcs) in DASH manifests:
    
    
    "elementaryStreams": [
      {
        "key": "es_video",
        "videoStream": {
          "h264": {
            "profile": "main",
            "heightPixels": 600,
            "widthPixels": 800,
            "bitrateBps": 1000000,
            "frameRate": 60,
          },
        },
      },
      {
        "key": "es_audio",
        "audioStream": {
          "codec": "aac",
          "channelCount": 2,
          "bitrateBps": 160000
        }
      }
    ],
    "encryptions": [
      {
        "id": "aes-128",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"clearkey": {}},
        "aes128": {}
      },
      {
        "id": "cenc",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"clearkey": {}},
        "mpegCenc": {
          "scheme": "cenc"
        }
      },
      {
        "id": "cbcs",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"clearkey": {}},
        "mpegCenc": {
          "scheme": "cbcs"
        }
      }
    ],
    "muxStreams": [
      {
        "key": "ts_aes128",
        "container": "ts",
        "elementaryStreams": ["es_video", "es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "aes-128"
      },
      {
        "key": "fmp4_cenc_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "cenc"
      },
      {
        "key": "fmp4_cenc_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "cenc"
      },
      {
        "key": "fmp4_cbcs_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "cbcs"
      },
      {
        "key": "fmp4_cbcs_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "cbcs"
      }
    ],
    "manifests": [
      {
        "fileName": "manifest_aes128.m3u8",
        "type": "HLS",
        "muxStreams": ["ts_aes128"]
      },
      {
        "fileName": "manifest_cenc.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_cenc_video", "fmp4_cenc_audio"]
      },
      {
        "fileName": "manifest_cbcs.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_cbcs_video", "fmp4_cbcs_audio"]
      }
    ]
    

### Example (FP/PR/Widevine)

The following example configures FairPlay/SAMPLE-AES, Widevine/MPEG-CENC (cenc and cbcs), and PlayReady/MPEG-CENC (cenc and cbcs) muxStreams. Widevine and PlayReady muxStreams are included in both HLS and DASH manifests.
    
    
    "elementaryStreams": [
      {
        "key": "es_video",
        "videoStream": {
          "h264": {
            "profile": "main",
            "heightPixels": 600,
            "widthPixels": 800,
            "bitrateBps": 1000000,
            "frameRate": 60,
          },
        },
      },
      {
        "key": "es_audio",
        "audioStream": {
          "codec": "aac",
          "channelCount": 2,
          "bitrateBps": 160000
        }
      }
    ],
    "encryptions": [
      {
        "id": "fairplay",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"fairplay": {}},
        "sampleAes": {}
      },
      {
        "id": "widevine-cenc",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"widevine": {}},
        "mpegCenc": {
          "scheme": "cenc"
        }
      },
      {
        "id": "widevine-cbcs",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"widevine": {}},
        "mpegCenc": {
          "scheme": "cbcs"
        }
      },
      {
        "id": "playready-cenc",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"playready": {}},
        "mpegCenc": {
          "scheme": "cenc"
        }
      },
      {
        "id": "playready-cbcs",
        "secretManagerKeySource": {
          "secretVersion": "projects/12345/secrets/key-1/versions/1"
        },
        "drmSystems": {"playready": {}},
        "mpegCenc": {
          "scheme": "cbcs"
        }
      }
    ],
    "muxStreams": [
      {
        "key": "ts_fairplay",
        "container": "ts",
        "elementaryStreams": ["es_video", "es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "fairplay"
      },
      {
        "key": "fmp4_widevine_cenc_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "widevine-cenc"
      },
      {
        "key": "fmp4_widevine_cenc_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "widevine-cenc"
      },
      {
        "key": "fmp4_widevine_cbcs_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "widevine-cbcs"
      },
      {
        "key": "fmp4_widevine_cbcs_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "widevine-cbcs"
      },
      {
        "key": "fmp4_playready_cenc_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "playready-cenc"
      },
      {
        "key": "fmp4_playready_cenc_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "playready-cenc"
      },
      {
        "key": "fmp4_playready_cbcs_video",
        "container": "fmp4",
        "elementaryStreams": ["es_video"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "playready-cbcs"
      },
      {
        "key": "fmp4_playready_cbcs_audio",
        "container": "fmp4",
        "elementaryStreams": ["es_audio"],
        "segmentSettings": {"segmentDuration": "2s"},
        "encryptionId": "playready-cbcs"
      }
    ],
    "manifests": [
      {
        "fileName": "manifest_fairplay.m3u8",
        "type": "HLS",
        "muxStreams": ["ts_fairplay"]
      },
      {
        "fileName": "manifest_widevine_cenc.m3u8",
        "type": "HLS",
        "muxStreams": ["fmp4_widevine_cenc_video", "fmp4_widevine_cenc_audio"]
      },
      {
        "fileName": "manifest_widevine_cbcs.m3u8",
        "type": "HLS",
        "muxStreams": ["fmp4_widevine_cbcs_video", "fmp4_widevine_cbcs_audio"]
      },
      {
        "fileName": "manifest_widevine_cenc.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_widevine_cenc_video", "fmp4_widevine_cenc_audio"]
      },
      {
        "fileName": "manifest_widevine_cbcs.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_widevine_cbcs_video", "fmp4_widevine_cbcs_audio"]
      },
      {
        "fileName": "manifest_playready_cenc.m3u8",
        "type": "HLS",
        "muxStreams": ["fmp4_playready_cenc_video", "fmp4_playready_cenc_audio"]
      },
      {
        "fileName": "manifest_playready_cbcs.m3u8",
        "type": "HLS",
        "muxStreams": ["fmp4_playready_cbcs_video", "fmp4_playready_cbcs_audio"]
      },
      {
        "fileName": "manifest_playready_cenc.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_playready_cenc_video", "fmp4_playready_cenc_audio"]
      },
      {
        "fileName": "manifest_playready_cbcs.mpd",
        "type": "DASH",
        "muxStreams": ["fmp4_playready_cbcs_video", "fmp4_playready_cbcs_audio"]
      }
    ]
    

After you know the JSON configuration you want to use, [create a job](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs) as normal.

## Monitor the output

Encrypted output streams contain modified manifests with the information needed to decrypt the content for playback.

### Manifest examples

The following manifests show the information needed to decrypt the associated content.

### HLS AES-128/ClearKey
    
    
    #EXTM3U
    #EXT-X-VERSION:7
    #EXT-X-TARGETDURATION:4
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-DISCONTINUITY-SEQUENCE:0
    #EXT-X-KEY:METHOD=AES-128,URI="https://example.com/keys/3d9dccb479c64adbb6e514790caa7822.bin",IV=0x8d80aa741e7b32c2f1967daca83e81f3
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:22.870Z
    #EXTINF:2.576778
    segment-0000000000.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:25.447Z
    #EXTINF:2.000000
    segment-0000000001.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:27.447Z
    #EXTINF:2.000000
    segment-0000000002.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:29.447Z
    #EXTINF:2.000000
    segment-0000000003.ts
    

### HLS SAMPLE-AES/FairPlay
    
    
    #EXTM3U
    #EXT-X-VERSION:7
    #EXT-X-TARGETDURATION:4
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-DISCONTINUITY-SEQUENCE:0
    #EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://d569cb35bd0548c7a99d92feb381df13",KEYFORMAT="com.apple.streamingkeydelivery",KEYFORMATVERSIONS="1"
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:22.870Z
    #EXTINF:2.576778
    segment-0000000000.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:25.447Z
    #EXTINF:2.000000
    segment-0000000001.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:27.447Z
    #EXTINF:2.000000
    segment-0000000002.ts
    #EXT-X-PROGRAM-DATE-TIME:2022-10-12T20:08:29.447Z
    #EXTINF:2.000000
    segment-0000000003.ts
    

### DASH MPEG-CENC/Widevine
    
    
    <AdaptationSet segmentAlignment="true" maxWidth="800" maxHeight="600">
      <Representation mimeType="video/mp4" id="fmp4_widevine_cenc_video" codecs="avc1.4d001f">
        <ContentProtection value="cenc" schemeIdUri="urn:mpeg:dash:mp4protection:2011" cenc:default_KID="44ec248b-048c-43a6-a6ee-58a752c6f9f8"/>
        <ContentProtection schemeIdUri="urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed" value="Widevine">
          <cenc:pssh>AAAAOHBzc2gAAAAA7e+LqXnWSs6jCfc1R0h7QAAABgSEAB3Gcrj/8kFklokiVbJMh9VmwY=</cenc:pssh>
        </ContentProtection>
      </Representation>
    </AdaptationSet>
    <AdaptationSet segmentAlignment="true" mimeType="audio/mp4" id="1" label="fmp4_widevine_cenc_audio">
      <Representation id="fmp4_widevine_cenc_audio" codecs="mp4a.40.2">
        <ContentProtection value="cenc" schemeIdUri="urn:mpeg:dash:mp4protection:2011" cenc:default_KID="44ec248b-048c-43a6-a6ee-58a752c6f9f8"/>
        <ContentProtection schemeIdUri="urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed" value="Widevine">
          <cenc:pssh>AAAAOHBzc2gAAAAA7e+LqXnWSs6jCfc1R0h7QAAABgSEAB3Gcrj/8kFklokiVbJMh9VmwY=</cenc:pssh>
        </ContentProtection>
      </Representation>
    </AdaptationSet>
    

### Recommended players

Players based on [`HLS.js`](https://github.com/video-dev/hls.js) are recommended for HLS/TS decryption. Players based on [Shaka Player](https://github.com/shaka-project/shaka-player) are recommended for DASH/fMP4 decryption.

The PlayReady 'cenc' scheme is supported on physical machines running Windows 10 with the Microsoft Edge browser, Xbox One (version 1703 or lower), and some non-Windows devices (for example, smart TVs). The PlayReady 'cbcs' scheme is only supported on Xbox One version 1709 or higher. See [PlayReady Content Encryption Modes](https://learn.microsoft.com/en-us/playready/packaging/content-encryption-modes) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
