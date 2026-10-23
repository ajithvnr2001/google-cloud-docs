---
url: https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest/
title: Validate PAL interoperability with SAS \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:27.300403+00:00
---

# Validate PAL interoperability with SAS  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Validate PAL interoperability with SAS Stay organized with collections  Save and categorize content based on your preferences. 

You can test [Priority Access License (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) functionality within Spectrum Access System (SAS) by using the following interoperability test cases. The current version of the PAL interoperability test suite is v2. The equipment vendors are assigned specific zones for testing purposes. For more information, see [PAL testing zones](https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities#pal-testingzone).

To pass the PAL interoperability test with SAS, your Citizens Broadband Radio Service Device (CBSD) needs the spectrum inquiry function. The CBSDs that can't make or process spectrum inquiry won't pass the test. Make sure that you validate the test results in the _Test Result_ spreadsheet provided by Google.

## Requirements for SAS interoperability testing

To test SAS interoperability with a SAS model and its software version, you need the following:

  * **Test[Federal Communications Commission (FCC) IDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc)**

The test ID must be valid as per [Part 96 FCC ID](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96). For devices awaiting FCC certification, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).

  * **Test user IDs**

If you're a Google SAS customer, use your existing [user ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid). If you're not a customer and want to test your device, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) to approve a custom user ID to use with the SAS test environment.

  * **Device test certificates**

Any CBRS device certificate works with the test SAS environment. If you don't have a test certificate for your CBSD or [Domain Proxy (DP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dp) device, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). The test certificates work for _only_ the SAS test environment.


**Tip:** In all regions, we encourage free-form testing. However, in the SAS test environment, we recommend that you test your device virtually in Alaska. Other than the [entities used for device testing](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#simulated-entities), there are no protected entities in Alaska. Testing outside Alaska might not produce the expected results for the interoperability testing test plan.

## PAL test case 1: New PAL-qualified CBSD that operates inside its protected area (normal PAL operation)

This test case verifies that a CBSD requests a grant on a PAL channel when a new CBSD is registered and begins operation in an area where its operator has a PAL.

### Prerequisites

Make sure that the new CBSD is registered as follows:

  * Within the borders of the county of your assigned PAL.
  * With the [user ID](https://docs.cloud.google.com/spectrum-access-system/key-terms#userid) associated with the assigned PAL.



### Steps

Verify the following steps:

  1. The CBSD sends a spectrum inquiry request. 

#####  Example 
         
         {
         "spectrumInquiryRequest":[
           {
              "cbsdId":"SAS-assigned CBSD ID",
              "inquiredSpectrum":[
                 {
                    "lowFrequency":3550000000,
                    "highFrequency":3700000000
                 }
              ]}]}
         

* * *

  2. The spectrum inquiry response from SAS shows that channel five is a PAL channel. 

#####  Example 
         
         {
           "spectrumInquiryResponse": [
             {
               "cbsdId": "SAS-assigned CBSD ID",
               "availableChannel": [
                 {
                   "frequencyRange": {
                     "lowFrequency": 3550000000,
                     "highFrequency": 3560000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3560000000,
                     "highFrequency": 3570000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3570000000,
                     "highFrequency": 3580000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3580000000,
                     "highFrequency": 3590000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                  {
                   "frequencyRange": {
                     "lowFrequency": 3590000000,
                     "highFrequency": 3600000000
                   },
                   "channelType": "PAL",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3600000000,
                     "highFrequency": 3610000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3610000000,
                     "highFrequency": 3620000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3620000000,
                     "highFrequency": 3630000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3630000000,
                     "highFrequency": 3640000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3640000000,
                     "highFrequency": 3650000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3650000000,
                     "highFrequency": 3660000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3660000000,
                     "highFrequency": 3670000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3670000000,
                     "highFrequency": 3680000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3680000000,
                     "highFrequency": 3690000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3690000000,
                     "highFrequency": 3700000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 }
         
         
         ],
           "response": {
             "responseCode": 0
           }
         }
         

] } 

* * *

  3. The CBSD requests a grant for any PAL channel. 

#####  Example 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3590000000,
                        "highFrequency":3600000000
                     }}}]}
         

* * *

  4. SAS sends a grant response that shows that it's a PAL grant. You can find the following in the test SAS Portal:

     * Results
     * PAL grant on the CBSD's **Status** tab.
     * Associated [PPA](https://docs.cloud.google.com/spectrum-access-system/key-terms#ppa) on the CBSD's **Coex** tab. 

#####  Example 
           
           {
           "grantResponse":[
             {
                "cbsdId":"SAS-assigned CBSD ID",
                "grantId":"SAS-assigned grant ID",
                "grantExpireTime":"YYYY-MM-DDThh:mm:ssZ",
                "heartbeatInterval":60,
                "channelType": PAL,
                "response":{
                   "responseCode":0
                }}]}
           

* * *

  5. The CBSD sends heartbeat requests to SAS periodically based on `heartbeatInterval` and receives heartbeat responses from SAS. The first heartbeat request must have `operationState` set to **Granted**. Google SAS recommends a 60-second `heartbeatInterval`. 

#####  Example 
         
         {
                "heartbeatRequest":[
                   {
                      "cbsdId":"SAS-assigned CBSD ID",
                      "grantId":"SAS-assigned grant ID",
                      "operationState": "GRANTED"
                   }]}
         

* * *

  6. SAS responds with approval of the heartbeat request. 

#####  Example 
         
         {
              "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "grantId":"SAS-assigned grant ID",
               "transmitExpireTime": "YYYY-MM-DDThh:mm:ssZ",
               "heartbeatInterval":60,
         
         
         "response":{
                 "responseCode":0
              },
              }]}
         

* * *

  7. If the previous heartbeat request is approved, the CBSD sends subsequent heartbeat requests to the CBSD periodically based on `heartbeatInterval` with the field `operationState` set to **Authorized**. 

#####  Example 
         
         {
                "heartbeatRequest":[
                   {
                      "cbsdId":"SAS-assigned CBSD ID",
                      "grantId":"SAS-assigned grant ID",
                      "operationState":"AUTHORIZED"
                   }]}
          

* * *

  8. The SAS responds with approval of the heartbeat request. 

#####  Example 
         
         {
                "heartbeatResponse":[
                   {
                      "cbsdId":"SAS-assigned CBSD ID",
                      "grantId":"SAS-assigned grant ID",
                       "transmitExpireTime":"YYYY-MM-DDThh:mm:ssZ",
                        "heartbeatInterval":60,
                      "response":{
                         "responseCode":0
                      }}]}
           

* * *




### Result

The expected results from the test are listed in the following table.

**Table 1.** Test case 1 | Receives | Sends  
---|---|---  
SAS | 

  * Spectrum inquiry request
  * Valid grant request for the PAL channel
  * Heartbeat requests

| 

  * Spectrum inquiry response
  * Successful grant response after the CBSD requests a grant on the PAL channel

  
CBSD | 

  * Spectrum inquiry response
  * Successful grant response
  * Successful heartbeat responses

| 

  * Spectrum inquiry request
  * Valid grant request with the operational parameters for the PAL channel
  * Heartbeat requests

  
  
## PAL test case 2a: Pre-existing PAL-qualified CBSD that moves from a GAA grant to a PAL grant on a different channel

This test case verifies how a [PAL-qualified CBSD](https://docs.cloud.google.com/spectrum-access-system/key-terms#palcbsd) with a [General Authorized Access (GAA)](https://docs.cloud.google.com/spectrum-access-system/key-terms#gaa) behaves when a valid [PAL](https://docs.cloud.google.com/spectrum-access-system/key-terms#pal) channel becomes available for another channel.

### Prerequisites

Make sure that the following is true:

  * The CBSD is registered with the intermittent PAL [user ID](https://docs.cloud.google.com/spectrum-access-system/key-terms#userid) `test_pal_user_id` within the borders of the county of your assigned PAL. For more information, see [PAL testing zones](https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities#pal-testingzone).
  * The CBSD holds a GAA grant that spans any channel except channel three (3570 MHz to 3580 MHz).
  * The CBSD is heartbeating on the GAA grant.



### Steps

Verify the following steps:

  1. The test began when the CBSD automatically deactivated the intermittent PAL user ID [according to the time schedule](https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities#pal-testingzone).
  2. The CBSD requests a GAA grant that spans any channel except channel three (3570 MHz to 3580 MHz).
  3. The CBSD heartbeats on the GAA grant.
  4. SAS automatically activates the intermittent PAL user ID according to the time schedule.
  5. Optional: The CBSD relinquishes its GAA grant.
  6. The CBSD sends a spectrum inquiry request. 

#####  Example 
         
         {
            "spectrumInquiryRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":3550000000,
                        "highFrequency":3700000000
                     }]}]}
         

* * *

  7. The spectrum inquiry response from SAS shows that channel three is a PAL channel. 

#####  Example 
         
         {
           "spectrumInquiryResponse": [
             {
               "cbsdId": "SAS-assigned CBSD ID",
               "availableChannel": [
                 {
                   "frequencyRange": {
                     "lowFrequency": 3550000000,
                     "highFrequency": 3560000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3560000000,
                     "highFrequency": 3570000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3570000000,
                     "highFrequency": 3580000000
                   },
                   "channelType": "PAL",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3580000000,
                     "highFrequency": 3590000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                  {
                   "frequencyRange": {
                     "lowFrequency": 3590000000,
                     "highFrequency": 3600000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3600000000,
                     "highFrequency": 3610000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3610000000,
                     "highFrequency": 3620000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3620000000,
                     "highFrequency": 3630000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3630000000,
                     "highFrequency": 3640000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3640000000,
                     "highFrequency": 3650000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3650000000,
                     "highFrequency": 3660000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3660000000,
                     "highFrequency": 3670000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3670000000,
                     "highFrequency": 3680000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3680000000,
                     "highFrequency": 3690000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3690000000,
                     "highFrequency": 3700000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 }
         
         
         ],
           "response": {
             "responseCode": 0
           }}]}
         

* * *

  8. The CBSD requests a grant for PAL channel three (3570 MHz to 3580 MHz). 

#####  Example 
         
         {
             "grantRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3570000000,
                        "highFrequency":3580000000
                     }}}]}
            

* * *

  9. The CBSD receives a grant response from SAS.

**Note:** CBSDs and PPAs associated with the intermittent PAL user ID aren't visible in the test SAS Portal.

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "grantId":"SAS-assigned grant ID",
                  "grantExpireTime":"YYYY-MM-DDThh:mm:ssZ",
                  "heartbeatInterval":60,
                  "channelType": PAL,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
            

* * *

  10. The CBSD sends heartbeat requests to SAS periodically based on `heartbeatInterval` and receives heartbeat responses from SAS. The first heartbeat request must have `operationState` set to **Granted**. 

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState": "GRANTED"
               }]}
            

* * *

  11. SAS responds with approval of the heartbeat request. 

#####  Example 
         
         {
         "heartbeatResponse":[
           {
              "cbsdId":"SAS-assigned CBSD ID",
              "grantId":"SAS-assigned grant ID",
           "transmitExpireTime": "YYYY-MM-DDThh:mm:ssZ",
           "heartbeatInterval":60,
              "response":{
                 "responseCode":0
              },      }]}
            

* * *

  12. If the previous heartbeat request was approved, the CBSD sends subsequent heartbeat requests to SAS periodically based on `heartbeatInterval` with the field `operationState` set to **Authorized**. 

#####  Example 
         
         {
                  "heartbeatRequest":[
                     {
                        "cbsdId":"SAS-assigned CBSD ID",
                        "grantId":"SAS-assigned grant ID",
                        "operationState":"AUTHORIZED"
                     }
                  ]
               }
         
         

* * *

  13. SAS responds with approval of the heartbeat request. 

#####  Example 
         
         {
              "heartbeatResponse":[
                 {
                    "cbsdId":"SAS-assigned CBSD ID",
                    "grantId":"SAS-assigned grant ID",
                     "transmitExpireTime":"YYYY-MM-DDThh:mm:ssZ",
                      "heartbeatInterval":60,
                    "response":{
                       "responseCode":0
                    }
                 }
              ]
           }
            

* * *




### Result

The expected results from the test are listed in the following table.

**Table 2.** Test case 2 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Spectrum inquiry request
  * Valid grant request with the new operational parameters
  * Heartbeat requests
  * Optional: Relinquishment and registration requests

| 

  * Spectrum inquiry response
  * Successful grant response after the CBSD requests a grant on the PAL channel
  * Optional: Relinquishment and registration responses

|   
CBSD | 

  * Spectrum inquiry response
  * Successful grant response
  * Successful heartbeat responses

| 

  * Spectrum inquiry request
  * Valid grant request with the operational parameters for the PAL channel
  * Relinquishment and registration requests, acceptable but not recommended

| 

  * Continues to heartbeat on the previous GAA grant
  * If the CBSD has both a GAA grant and a PAL grant, it's [partially PAL-protected](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#partialpal)

  
  
## PAL test case 2b: Pre-existing PAL-qualified CBSD that moves from a GAA grant to a PAL grant on the same channel

A new [PPA](https://docs.cloud.google.com/spectrum-access-system/key-terms#ppa) is created in an area where the [CBSD](https://docs.cloud.google.com/spectrum-access-system/key-terms#cbsd) is already registered and operating. This test case verifies how a PAL-qualified CBSD with a GAA grant on its PAL channel behaves when a valid PAL channel becomes available.

[SAS](https://docs.cloud.google.com/spectrum-access-system/key-terms#sas) automatically converts GAA grants into PAL grants on that same channel for PAL-qualified CBSDs. In this case, the CBSD isn't expected to take actions when it converts from [GAA-only](https://docs.cloud.google.com/spectrum-access-system/key-terms#gaaonly) to PAL-protected.

### Prerequisites

Make sure that the following is true:

  * The CBSD is registered within the borders of the county of your assigned PAL.
  * The CBSD is configured with the intermittent PAL user ID `test_pal_user_id`.



### Steps

Verify the following steps:

  1. The test begins when SAS automatically deactivates the intermittent PAL user ID [according to the time schedule](https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities#pal-testingzone).
  2. The CBSD requests a GAA grant that spans channel three (3570 MHz to 3580 MHz).
  3. The CBSD begins heartbeating on the GAA grant.

**Note:** CBSDs and PPAs associated with the intermittent PAL user ID aren't visible in the [SAS Test Portal](https://wirelessconnectivity.google.com/test-sas).
  4. SAS automatically activates the intermittent PAL user ID according to the time schedule.

  5. Optional: The CBSD makes a spectrum inquiry request after the intermittent PAL user ID becomes active. 

#####  Example 
         
         {
         "spectrumInquiryRequest":[
             {
                "cbsdId":"SAS-assigned CBSD ID",
                "inquiredSpectrum":[
                   {
                      "lowFrequency":3550000000,
                      "highFrequency":3700000000
                   }]}]}
         

* * *

  6. The SAS response to the spectrum inquiry request includes PAL channel three.

**Note:** The CBSD should not experience any service interruptions or request a new grant.

#####  Example 
         
         {
         "spectrumInquiryResponse": [
         {
           "cbsdId": "SAS-assigned CBSD ID",
           "availableChannel": [
             {
               "frequencyRange": {
                 "lowFrequency": 3550000000,
                 "highFrequency": 3560000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3560000000,
                 "highFrequency": 3570000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3570000000,
                 "highFrequency": 3580000000
               },
               "channelType": "PAL",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3580000000,
                 "highFrequency": 3590000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
              {
               "frequencyRange": {
                 "lowFrequency": 3590000000,
                 "highFrequency": 3600000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3600000000,
                 "highFrequency": 3610000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3610000000,
                 "highFrequency": 3620000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3620000000,
                 "highFrequency": 3630000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3630000000,
                 "highFrequency": 3640000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3640000000,
                 "highFrequency": 3650000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3650000000,
                 "highFrequency": 3660000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3660000000,
                 "highFrequency": 3670000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3670000000,
                 "highFrequency": 3680000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3680000000,
                 "highFrequency": 3690000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3690000000,
                 "highFrequency": 3700000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             }
           ],
           "response": {
             "responseCode": 0
           }
         }
         ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 2b.** Test case 2b | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Spectrum inquiry request
  * Valid grant request with the new operational parameters
  * Heartbeat requests
  * Optional: Relinquishment and registration requests

| 

  * Spectrum inquiry response
  * Successful grant response after the CBSD requests a grant on the PAL channel
  * Optional: Relinquishment and registration responses

|   
CBSD | 

  * Spectrum inquiry response
  * Successful grant response
  * Successful heartbeat responses

| 

  * Spectrum inquiry request
  * Valid grant request with the operational parameters for the PAL channel

| Continues to heartbeat on a previous grant  
  
## PAL test case 3a: Pre-existing GAA-only CBSD that has an authorized grant on a channel that becomes a PAL channel

This test case verifies that the [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) can successfully migrate to another channel when a [PPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#ppa) is created in an area and on a channel where the GAA-only CBSD operates.

### Prerequisites

Make sure that you have two CBSDs as follows:

  * CBSD 1 is registered with the intermittent PAL user ID `test_pal_user_id` and is within the borders of the county of your assigned PAL.
  * CBSD 2 is configured with a user ID associated with your assigned PAL but hasn't been registered yet.



### Steps

Verify the following steps:

  1. CBSD 1 successfully requests a GAA grant on channel five from 3590 MHz to 3600 MHz. 

#####  Example 
         
         {
         "grantRequest":[
             . . .
             {
                 "operationFrequencyRange":{
                     "lowFrequency":3590000000,
                    "highFrequency":3600000000
                     . . .
                 }}]}
         

* * *

  2. CBSD 2 registers within 10 meters of CBSD 1 and also successfully receives a grant on channel five, which is a PAL channel.
  3. CBSD 1 sends a heartbeat request after [CPAS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas) is completed.
  4. SAS sends a heartbeat response to CBSD 1 with `responseCode 500` (`Terminated_Grant`). The grant is terminated because the CBSD uses a GAA grant that overlaps with the PAL channel associated with the PPA where CBSD 2 is located. 

#####  Example: Heartbeat response when the dynamic PPA zone is active 
         
         {
         "heartbeatResponse":[
           {
              "cbsdId":"SAS-assigned CBSD ID",
              "grantId":"SAS-assigned grant ID",
               "transmitExpireTime": "YYYY-MM-DDThh:mm:ssZ",
               "response": {
                   "responseCode": 500,
                   "responseMessage": "TERMINATED_GRANT"
              }
           }
         ]
         }
         

* * *

  5. CBSD 1 sends a spectrum inquiry request after the grant is terminated.
  6. SAS sends a spectrum inquiry response that no longer shows the PAL channel. 

#####  Example: Spectrum inquiry response when channel one is excluded 
         
         {
         "spectrumInquiryResponse": [
         {
           "cbsdId": "SAS-assigned CBSD ID",
           "availableChannel": [
             {
               "frequencyRange": {
                 "lowFrequency": 3550000000,
                 "highFrequency": 3560000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3560000000,
                 "highFrequency": 3570000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3570000000,
                 "highFrequency": 3580000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3580000000,
                 "highFrequency": 3590000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3600000000,
                 "highFrequency": 3610000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3610000000,
                 "highFrequency": 3620000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3620000000,
                 "highFrequency": 3630000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3630000000,
                 "highFrequency": 3640000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3640000000,
                 "highFrequency": 3650000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3650000000,
                 "highFrequency": 3660000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3660000000,
                 "highFrequency": 3670000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3670000000,
                 "highFrequency": 3680000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3680000000,
                 "highFrequency": 3690000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             },
             {
               "frequencyRange": {
                 "lowFrequency": 3690000000,
                 "highFrequency": 3700000000
               },
               "channelType": "GAA",
               "ruleApplied": "FCC_PART_96",
               "maxEirp": 37
             }
           ],
           "response": {
             "responseCode": 0
           }
         }
         ]
         }
         

* * *

  7. The CBSD requests a new grant on an available channel.



### Result

The expected results from the test are listed in the following table.

**Table 3a.** Test case 3a | Receives  | Sends  | Acceptable   
---|---|---|---  
SAS  | 

  * Heartbeat requests
  * Spectrum inquiry response
  * Grant request for a new GAA channel from CBSD 1 and grant request for a PAL channel from CBSD 2

| 

  * Heartbeat responses
  * Spectrum inquiry response that excludes channel five after CPAS is completed

|   
CBSD  | CBSD 1  | 

  * Heartbeat responses with `responseCode 0` (`Success`) before CPAS
  * Heartbeat responses with `responseCode 500` (`Terminated_Grant`) after CPAS

| 

  * Grant request for a GAA grant on channel five
  * Heartbeat requests
  * Spectrum inquiry requests to determine which channels are available
  * Grant requests for any available GAA channel

| Stops transmission on the PAL channel before `transmitExpireTime` +60 seconds  
CBSD 2  | 

  * Registration response with `responseCode 0` (`Success`)
  * Grant response for the requested PAL channel

| 

  * Registration request
  * Grant request for any available PAL channel

|   
  
## PAL test case 3b: New GAA-only CBSD within an existing PPA that requests a GAA grant on a GAA channel

This test case verifies that the [CBSD](https://docs.cloud.google.com/spectrum-access-system/key-terms#cbsd) correctly responds to PAL channel guidance from SAS.

### Prerequisites

Make sure that you have two CBSDs as follows:

  * CBSD 1 is configured with the intermittent PAL user ID `test_pal_user_id`.
  * CBSD 2 is configured with your PAL-assigned user ID and is registered within the borders of the county of your assigned PAL. It has a valid PAL grant on channel five.



### Steps

Verify the following steps:

  1. CBSD 1 registers at a location within 10 meters of CBSD 2.
  2. CBSD 1 sends a spectrum inquiry to SAS. 

#####  Example 
         
         {
            "spectrumInquiryRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":3550000000,
                        "highFrequency":3700000000
                     }
                  ]
               }
            ]
         }
         

* * *

  3. SAS responds with a spectrum inquiry that excludes PAL channel five from 3590 MHz to 3600 MHz. 

#####  Example: Spectrum inquiry response when channel five is excluded 
         
         {
             "spectrumInquiryResponse": [
               {
                 "cbsdId": "SAS-assigned CBSD ID",
                 "availableChannel": [
                   {
                     "frequencyRange": {
                       "lowFrequency": 3550000000,
                       "highFrequency": 3560000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3560000000,
                       "highFrequency": 3570000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3570000000,
                       "highFrequency": 3580000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3580000000,
                       "highFrequency": 3590000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3600000000,
                       "highFrequency": 3610000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3610000000,
                       "highFrequency": 3620000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3620000000,
                       "highFrequency": 3630000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3630000000,
                       "highFrequency": 3640000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3640000000,
                       "highFrequency": 3650000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3650000000,
                       "highFrequency": 3660000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3660000000,
                       "highFrequency": 3670000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3670000000,
                       "highFrequency": 3680000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3680000000,
                       "highFrequency": 3690000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   },
                   {
                     "frequencyRange": {
                       "lowFrequency": 3690000000,
                       "highFrequency": 3700000000
                     },
                     "channelType": "GAA",
                     "ruleApplied": "FCC_PART_96",
                     "maxEirp": 37
                   }
                 ],
                 "response": {
                   "responseCode": 0
                 }
               }
             ]
           }
         

* * *

  4. The CBSD sends a grant request that isn't on channel five, in accordance with the spectrum inquiry response. 

#####  Example 
         
         {
             "grantRequest":[
                 . . .
                 {
                     "operationFrequencyRange":{
                         "lowFrequency":3580000000,
                        "highFrequency":3590000000
                         . . .
                     }
                 }
             ]
         }
         

* * *

  5. The CBSD receives the grant response and begins heartbeating on the grant. 

#####  Example 
         
         {
             "grantResponse": [
               {
                 "cbsdId": "SAS-assigned CBSD ID",
                 "grantId": "SAS-assigned grant ID",
                 "grantExpireTime": "YYY-MM-DDThh-mm-ssZ",
                 "heartbeatInterval": 60,
                 "channelType": "GAA",
                 "response": {
                   "responseCode": 0
                 }
               }
             ]
           }
         

* * *

  6. After the first successful heartbeat, the CBSD starts transmission on the corresponding channel and power.



### Result

The expected results from the test are listed in the following table.

**Table 3b.** Test case 3b | Receives | Sends  
---|---|---  
SAS | 

  * Spectrum inquiry request
  * Valid GAA grant request
  * Valid periodic heartbeat requests at least every `heartbeatInterval` seconds

| 

  * Spectrum inquiry response with PAL channels omitted
  * Successful responses for all requests, with `transmitExpireTime` in the heartbeat responses set to a value for the duration of four minutes

  
CBSD 1 | Successful responses for all requests | 

  * Spectrum inquiry request
  * Grant request on channels other than channel five
  * Periodic heartbeat requests at least every `heartbeatInterval` seconds

  
  
## PAL test case 3c: (Optional) New GAA-only CBSD within an existing PPA that requests a GAA grant on a PAL-protected channel

This optional test case verifies that a GAA-only CBSD correctly responds when a request is granted on a PAL channel.

### Prerequisites

Make sure that you have two CBSDs as follows:

  * CBSD 1 is configured with the intermittent PAL user ID `test_pal_user_id`.
  * CBSD 2 is configured with your PAL-assigned user ID and is registered within the borders of the county of your assigned PAL. It has a valid PAL grant on channel five.



### Steps

Verify the following steps:

  1. CBSD 1 sends a GAA grant request to SAS for channel five, which is a PAL channel for CBSD 2. 

#####  Example 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3590000000,
                        "highFrequency":3600000000
                     }
                  }
               }
            ]
         }
         

* * *

  2. SAS responds and rejects the grant request with `responseCode 400` (`Inside exclusion zone`). 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "response":{
                     "responseCode":400,
                     "responseMessage":"Inside exclusion zone"
                  }
               }
            ]
         }
         

* * *

  3. The CBSD performs a spectrum inquiry. 

#####  Example 
         
         {
            "spectrumInquiryRequest":[
               {
                  "cbsdId":"SAS-assigned CBSD ID",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":3550000000,
                        "highFrequency":3700000000
                     }
                  ]
               }
            ]
         }
         

* * *

  4. SAS responds with a spectrum inquiry that excludes PAL channel five from 3590 MHz to 3600 MHz. 

#####  Example 
         
         {
           "spectrumInquiryResponse": [
             {
               "cbsdId": "SAS-assigned CBSD ID",
               "availableChannel": [
                 {
                   "frequencyRange": {
                     "lowFrequency": 3560000000,
                     "highFrequency": 3570000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3570000000,
                     "highFrequency": 3580000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3580000000,
                     "highFrequency": 3590000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3590000000,
                     "highFrequency": 3600000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3600000000,
                     "highFrequency": 3610000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3610000000,
                     "highFrequency": 3620000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3620000000,
                     "highFrequency": 3630000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3630000000,
                     "highFrequency": 3640000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3640000000,
                     "highFrequency": 3650000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3650000000,
                     "highFrequency": 3660000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3660000000,
                     "highFrequency": 3670000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3670000000,
                     "highFrequency": 3680000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3680000000,
                     "highFrequency": 3690000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 },
                 {
                   "frequencyRange": {
                     "lowFrequency": 3690000000,
                     "highFrequency": 3700000000
                   },
                   "channelType": "GAA",
                   "ruleApplied": "FCC_PART_96",
                   "maxEirp": 37
                 }
               ],
               "response": {
                 "responseCode": 0
               }
             }
           ]
         }
         

* * *

  5. The CBSD sends a grant request that isn't on a PAL channel, in accordance with the spectrum inquiry response. 

#####  Example 
         
         {
             "grantRequest":[
                 . . .
                 {
                     "operationFrequencyRange":{
                         "lowFrequency":3580000000,
                        "highFrequency":3590000000
                         . . .
                     }
                 }
             ]
         }
         

* * *

  6. The CBSD receives the grant response and begins heartbeating on the grant. 

#####  Example 
         
         {
           "grantResponse": [
             {
               "cbsdId": "SAS-assigned CBSD ID",
               "grantId": "SAS-assigned grant ID",
               "grantExpireTime": "YYY-MM-DDThh-mm-ssZ",
               "heartbeatInterval": 60,
               "channelType": "GAA",
               "response": {
                 "responseCode": 0
               }
             }
           ]
         }
         

* * *

  7. After the first successful heartbeat, the CBSD starts transmission on the corresponding channel and power.



### Result

The expected results from the test are listed in the following table.

**Table 3c.** Test case 3c | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Spectrum inquiry request
  * Grant requests

| 

  * Spectrum inquiry response
  * Grant response with `responseCode 400` (`Interface`). In this case, the CBSD is inside the PPA and requests a grant on a protected frequency.

|   
CBSD 1 | Grant response with `responseCode 400` (`Interface`) | Grant request | 

  * CBSD 1 shouldn't start heartbeating or transmitting.
  * Optional: CBSD 1 performs a spectrum inquiry or requests a grant on a different frequency.

  
  
## What's next

  * [Validate your test results with Google](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#validate-test-result).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).
  * Learn about [CBSD interoperability with Google SAS](https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
