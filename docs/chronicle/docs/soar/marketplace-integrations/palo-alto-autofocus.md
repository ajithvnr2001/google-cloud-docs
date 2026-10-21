---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-autofocus/
title: Palo Alto AutoFocus \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:34:34.748978+00:00
---

# Palo Alto AutoFocus  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-autofocus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Palo Alto AutoFocus

**Important:** This integration refers to Palo Alto Networks AutoFocus.

This document provides guidance on how to integrate Palo Alto AutoFocus with Google SecOps.

## Configure Palo Alto AutoFocus to work with Google Security Operations

### Credentials

  1. In order to obtain your personal API Key, please sign in to your [Palo Alto AutoFocus Account](https://login.paloaltonetworks.com/?resume=/idp/WLW6x/resumeSAML20/idp/startSSO.ping&spentity=supportCSP).

  2. Fill the required fields, and the authorization code in, and then select **submit**.

  3. Select the **Enable** action in **Site Licenses** , then Select the **API Key** link. Please **copy** API key to the clipboard, which will be later used in this integration configuration with Google SecOps.




### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Palo Alto AutoFocus integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Hunt Domain

#### Description

Hunt a domain and retrieve a list of associated tags.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed the limit. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
AutoFocus_Status | the state of the scan. 0 - running, 1 - completed  
AutoFocus_Percentage | If scan is completed then list of hits, otherwise, the percentage of the scan.  
AutoFocus_Cookie | Hunt's cookie (to fetch info about a running scan).  
visible | Returns if it exists in JSON result.  
id | Returns if it exists in JSON result.  
source | Returns if it exists in JSON result.  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched entity. The insight will be created when the number of detected engines equals or exceeds the limit set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult": [{
            "visible": true,
            "_id": "8002b33fdf1caec503a25ee39297005e84c6af169df65d8be82e2465baa9b2b0",
            "_source": {
                "malware": 1,
                "sha1": "d2884e3655ce4ba167f0083054d2a9ed02669241",
                "create_date": "2019-09-20T01:57:15",
                "finish_date": "2019-09-20T02:03:48",
                "imphash": "ca6f8d49909b618c106e9274d41caec8",
                "filetype": "DLL64",
                "ispublic": 1,
                "tag": [],
                "tag_groups": [],
                "tasks": [{
                    "metadata_compilation_ts": "2019-09-20T07:31:06"
                }],
                "ssdeep": "3072:656zgKIvACBkQTQzhH6ejYF9aIRQkfGRLe0oaf:JtIvNTKhakYF9lRQKPaf",
                "sha256":
                "8002b33fdf1caec503a25ee39297005e84c6af169df65d8be82e2465baa9b2b0",
                "region": ["us"],
                "md5": "0e1e960c1de792f71b70eb8c8ab47a00",
                "size": 131072
            }}],
        "Entity": "example.com"
    }]
    

### Hunt File

#### Description

Hunt a file and retrieve a list of associated tags.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * Filehash
  * Filename



#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed the limit. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
AutoFocus_Status | the state of the scan. 0 - running, 1 - completed  
AutoFocus_Percentage | If scan is completed then list of hits, otherwise, the percentage of the scan.  
AutoFocus_Cookie | Hunt's cookie (to fetch info about a running scan).  
visible | Returns if it exists in JSON result.  
id | Returns if it exists in JSON result.  
source | Returns if it exists in JSON result.  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched entity. The insight will be created when the number of detected engines equals or exceeds the limit set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult": [{
            "visible": true,
            "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
            "_source": {
                "size": 165888,
                "malware": 0,
                "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26",
                "create_date": "2019-08-14T23:01:24",
                "finish_date": "2019-08-14T23:07:40",
                "imphash": "0a38e850afb4bc720ee47a34e25f5b35",
                "filetype": "DLL64",
                "ispublic": 1,
                "tasks": [{
                    "metadata_compilation_ts": "2019-07-30T14:47:02"
                }],
                "region": ["us"],
                "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e",
                "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
                "tag_groups": [],
                "tag": [],
                "md5": "385eab250b3164ef84bb71efca8e305d"
            }}],
        "Entity": "81bb895a833594013bc74b429fb1f24f9ec9df26"
    }]
    

### Hunt IP

#### Description

Hunt an IP address and retrieve a list of associated tags.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed the limit. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
AutoFocus_Status | the state of the scan. 0 - running, 1 - completed  
AutoFocus_Percentage | if scan is completed then list of hits, otherwise, the percentage of the scan  
AutoFocus_Cookie | Hunt's cookie (to fetch info about a running scan).  
visible | Returns if it exists in JSON result.  
id | Returns if it exists in JSON result.  
source | Returns if it exists in JSON result.  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched entity. The insight will be created when the number of detected engines equals or exceeds the limit set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult": [{
            "visible": true,
            "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
            "_source": {
                "size": 165888,
                "malware": 0,
                "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26",
                "create_date": "2019-08-14T23:01:24",
                "finish_date": "2019-08-14T23:07:40",
                "imphash": "0a38e850afb4bc720ee47a34e25f5b35",
                "filetype": "DLL64",
                "ispublic": 1,
                "tasks": [{
                    "metadata_compilation_ts": "2019-07-30T14:47:02"
                }],
                "region": ["us"],
                "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e",
                "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
                "tag_groups": [],
                "tag": [],
                "md5": "385eab250b3164ef84bb71efca8e305d"
            }}],
        "Entity": "95.179.168.51"
    }]
    

### Hunt URL

#### Description

Hunt a URL and retrieve a list of associated tags.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed the limit. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
AutoFocus_Status | the state of the scan. 0 - running, 1 - completed  
AutoFocus_Percentage | If scan is completed then list of hits, otherwise, the percentage of the scan.  
AutoFocus_Cookie | Hunt's cookie (to fetch info about a running scan).  
visible | Returns if it exists in JSON result.  
id | Returns if it exists in JSON result.  
source | Returns if it exists in JSON result.  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched entity. The insight will be created when the number of detected engines equals or exceeds the limit set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult": [{
            "visible": true,
            "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
            "_source": {
                "size": 165888,
                "malware": 0,
                "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26",
                "create_date": "2019-08-14T23:01:24",
                "finish_date": "2019-08-14T23:07:40",
                "imphash": "0a38e850afb4bc720ee47a34e25f5b35",
                "filetype": "DLL64",
                "ispublic": 1,
                "tasks": [{
                    "metadata_compilation_ts": "2019-07-30T14:47:02"
                }],
                "region": ["us"],
                "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e",
                "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd",
                "tag_groups": [],
                "tag": [],
                "md5": "385eab250b3164ef84bb71efca8e305d"
            }}],
        "Entity": "http://example.com"
    }]
    

### Ping

#### Description

Test connectivity to AutoFocus.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
