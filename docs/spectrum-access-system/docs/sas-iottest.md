---
url: https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest/
title: Validate CBSD interoperability with SAS \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:43.751368+00:00
---

# Validate CBSD interoperability with SAS  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Validate CBSD interoperability with SAS Stay organized with collections  Save and categorize content based on your preferences. 

The current version of the Spectrum Access System (SAS) test suite is v5.5. You can test the interoperability between a Citizens Broadband Radio Service Device (CBSD) and SAS by using the following test cases. Make sure that you validate the test result in the _Test Result_ spreadsheet provided by Google.

## Requirements for SAS interoperability testing

To test SAS interoperability with a SAS model and its software version, you need the following:

  * **Test[Federal Communications Commission (FCC) IDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc)**

The test ID must be valid as per [Part 96 FCC ID](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96). For devices awaiting FCC certification, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).

  * **Test user IDs**

If you're a Google SAS customer, use your existing [user ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid). If you're not a customer and want to test your device, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) to approve a custom user ID to use with the SAS test environment.

  * **Device test certificates**

Any CBRS device certificate works with the test SAS environment. If you don't have a test certificate for your CBSD or [Domain Proxy (DP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dp) device, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). The test certificates work for _only_ the SAS test environment.


**Tip:** In all regions, we encourage free-form testing. However, in the SAS test environment, we recommend that you test your device virtually in Alaska. Other than the [entities used for device testing](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#simulated-entities), there are no protected entities in Alaska. Testing outside Alaska might not produce the expected results for the interoperability testing test plan.

## Test case 1: CBSD registration, spectrum inquiry, grant, and heartbeat (normal operation)

This test case verifies the following:

  * CBSD registration procedure, grant procedure, and the first successful heartbeat to turn on the radio.
  * Optionally, if CBSD sends a spectrum inquiry request, then the CBSD uses the available channels in the spectrum inquiry response for the following grant request.



### WInnForum recognized CBRS grouping parameters

**The`groupingParam` object array is optional and is used by Google SAS only for General Authorized Access (GAA) coexistence purposes.**

We recommend that the CBSD sends `groupingParam` in the registration request whenever possible. Because SAS accepts the `groupingParam` array in the spectrum inquiry request, grant request, and heartbeat request, the subsequent information provided by the CBSD overrides the previous values.

**A list of valid`groupType` values has been published in [WINNF-SSC-0010](https://winnf.memberclicks.net/assets/CBRS/WINNF-SSC-0010.pdf).**

If the CBSD sends an invalid `groupType`, the SAS responds with `responseCode 103` (`Invalid_value`). Currently, SAS supports the `groupType` values **Principal_Subordinate_SFG** and **Spectrum_Reuse**. It stores and uploads grouping parameters to the [SAS Portal](https://docs.cloud.google.com/spectrum-access-system/key-terms#sas-portal). SAS ignores any other valid `groupType` values with `responseCode 0` (`Success`).

### Prerequisites

Make sure that the CBSD is not registered in the SAS Portal and is not set to request a subset of the spectrum that is available.

### Steps

Verify the following steps:

  1. The CBSD sends a registration request to SAS with the FCC ID and the user ID. You can use any certified FCC ID or one that has been confirmed along with the user ID and added to the allowlist by [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). Learn how to [connect to the test SAS environment](https://docs.cloud.google.com/spectrum-access-system/docs/connect-sastest). 

#####  Example 1: Category A CBSD single-step registration request 
         
         {
            "registrationRequest":[
               {
                  "fccId":"allowed FCC ID",
                  "userId":"allowed user ID",
                  "cbsdSerialNumber":"unique device ID",
                  "cbsdCategory":"A",
                  "airInterface":{
                     "radioTechnology":"E_UTRA",
                  },
                  "installationParam":{
                     "latitude":latitude within US,
                     "longitude":longitude within US,
                          "height":6,
                          "heightType":"AGL",
                     "antennaGain":6
                     "indoorDeployment":true
                  },
                  "cbsdInfo":{
                     "vendor": "CBSD Vendor 1",
                     "model": "CBSD Model 1",
                     "softwareVersion": "2.0",
                     "hardwareVersion": "2.0",
                     "firmwareVersion": "2.0"
                  },
                  "groupingParam":[
                     {
                        "groupType": "PRINCIPAL_SUBORDINATE_SFG",
                        "groupId": "string, e.g. CCG_1"
                     },
                     {
                        "groupType": "SPECTRUM_REUSE",
                        "groupId": "string, e.g. ICG_1"
                     }
                  ]
               }
            ]
         }
         

* * *

#####  Example 2: Category B CBSD multistep registration request 

These CPI-provided parameters have been pre-loaded into SAS through the SAS Portal.
         
         {
            "registrationRequest":[
               {
                  "fccId":"allowed FCC ID",
                  "userId":"allowed user ID",
                  "cbsdSerialNumber":"unique device ID",
                  "cbsdCategory":"B",
                  "airInterface":{
                     "radioTechnology":"E_UTRA"
                  },
                  "cbsdInfo":{
                     "vendor": "CBSD Vendor 1",
                     "model": "CBSD Model 1",
                     "softwareVersion": "2.0",
                     "hardwareVersion": "2.0",
                     "firmwareVersion": "2.0"
                  },
                  "groupingParam":[
                     {
                        "groupType": "PRINCIPAL_SUBORDINATE_SFG",
                        "groupId": "string, e.g. CCG_1"
                     },
                     {
                        "groupType": "SPECTRUM_REUSE",
                        "groupId": "string, e.g. ICG_1"
                     }
                  ]
               }
            ]
         }
         

* * *

  2. The CBSD receives a registration response from SAS. 

#####  Example 
         
         {
            "registrationResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  3. Optional: The CBSD sends a spectrum inquiry request to query available spectrum. 

#####  Example 
         
         {
            "spectrumInquiryRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":within 3550 - 3700 MHz range (e.g. 3550000000),
                        "highFrequency":within 3550 - 3700 MHz range (e.g. 3650000000)
                     }
                  ]
               }
            ]
         }
         

* * *

  4. If the CBSD sends the spectrum inquiry request, it receives a list of available channels from SAS. 

#####  Example 
         
         {
         
         
         
         "spectrumInquiryResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "availableChannel":[
                     {
                        "frequencyRange":{
                           "lowFrequency":3550 - 3700 MHz (e.g. 3600000000),
                           "highFrequency":3550 - 3700 MHz
                        },
                        "channelType":"GAA",
                        "ruleApplied":"FCC_PART_96",
                        "maxEirp": 37
                     }
                  ],
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  5. The CBSD sends a grant request to SAS. If a spectrum inquiry was carried out, then the CBSD requests a frequency range that SAS indicated is available. 

#####  Example 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz (e.g. 3600000000),
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               }
            ]
         }
         

* * *

  6. The CBSD receives a grant response from SAS. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  7. The CBSD sends heartbeat requests to SAS periodically based on `heartbeatInterval` and receives heartbeat responses from SAS.

**Important:** The first heartbeat request must have `operationState` set to **granted**.

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState":"GRANTED"
               }
            ]
         }
         

* * *

  8. SAS responds by approving the heartbeat request. 

#####  Example 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
                  "heartbeatInterval": 60,
                  "response":{
                     "responseCode":0
                  },
               }
            ]
         }
         

* * *

  9. If the previous heartbeat request was approved, the CBSD sends subsequent heartbeat requests to SAS periodically based on `heartbeatInterval` with the `operationState` field set to **Authorized**. 

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState":"AUTHORIZED"
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 1.** Test case 1 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Valid registration request
  * Valid grant request
  * Valid periodic heartbeat requests at least every `heartbeatInterval` seconds

| Successful responses for all requests, with `transmitExpireTime` included in the heartbeat responses. |   
CBSD | Successful responses for all requests | 

  * Valid registration request
  * Valid grant request
  * Valid periodic heartbeat requests at every `heartbeatInterval` seconds, including requests where `operationState` is set to **Authorized**

| After the first successful heartbeat, the CBSD starts transmission on the corresponding channel and power.  
SAS Portal | Grouping parameters sent by CBSD in either of the request messages, when the `groupType` value is **Principal_Subordinate_SFG** or **Spectrum_Reuse** The grouping parameters appear on the **Config** tab of the **Coex groups** section.  |  |   
  
## Test case 2: Grant relinquishment and deregistration (normal operation)

This test case verifies the deregistration of the CBSD from SAS.

### Prerequisites

Make sure that the CBSD is registered, holds a grant, and is heartbeating.

### Steps

Verify the following steps:

  1. The CBSD operator uses the management tool to release the spectrum. 

#####  Example 1: Optionally, the CBSD sends a relinquishment request to SAS 
         
         {
            "relinquishmentRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID"
               }
            ]
         }
         

* * *

#####  Example 2: If the relinquishment request is sent, the CBSD receives a relinquishment response from SAS 
         
         {
            "relinquishmentResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId" : "SAS-assigned grant ID",
                  "response":{
                     "responseCode":0,
                  }
               }
            ]
         }
         

* * *

  2. The CBSD sends a deregistration request to SAS. 

#####  Example 
         
         {
            "deregistrationRequest":[
               {
                  "cbsdId":"SAS-assigned device ID"
               }
            ]
         }
         

* * *

  3. The CBSD receives a deregistration response from SAS. 

#####  Example 
         
         {
            "deregistrationResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
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

  * Optional: Relinquishment request
  * Deregistration request

| 

  * Optional: Relinquishment response
  * Deregistration request

|   
CBSD | 

  * Optional: Relinquishment response
  * Deregistration request

| 

  * Optional: Relinquishment request
  * Deregistration request

| Stops transmitting before sending a deregistration or a relinquishment request  
  
## Test case 3a: Grant suspension: IAP pending

This test case verifies the following:

  * The CBSD radio turns off when SAS suspends the CBSD's grant.
  * The CBSD reports the correct operation state in subsequent heartbeat requests.



### Prerequisites

A CBSD in the US has channels with limited power availability. Some locations like Tampa, Florida and Los Angeles, California have power budgets that are less than 37 dBm/MHz. To make it easier to simulate the test scenario for locations along the coast, _turn on_ the **Spectrum availability overlay** for the CBRS.

Make sure that the following is true:

  * The CBSD sends a grant request with a _maxEirp_ value less than the channel's available power in dBm/MHz. 

#####  Example 
        
        {
            "grantRequest":[
              . . .
              {
                 "operationParam":{
                      "maxEirp":25, (e.g. Assume Partial power available for
                              2670-2680=28dBm/MHz)
                      "operationFrequencyRange":{
                     "lowFrequency":3670000000,
                     "highFrequency":3680000000
                     . . .
                 }
              }
           ]
        }
        

* * *

  * The CBSD sends heartbeat requests. If the requested _maxEirp_ is less than or equal to partial power, SAS approves the grant. 

#####  Example 1: The first heartbeat request after a grant is approved 
        
        {
           "heartbeatRequest":[
              {
                 "cbsdId":"SAS-assigned device ID",
                 "grantId":"SAS-assigned grant ID",
                 "operationState": "GRANTED"
              }
           ]
        }
        

* * *

#####  Example 2: Heartbeat response when the grant is assigned 
        
        {
           "heartbeatResponse":[
              {
                 "cbsdId":"SAS-assigned device ID",
                 "grantId":"SAS-assigned grant ID",
                 "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
                 "heartbeatInterval": 60,
                 "response":{
                   "responseCode":0
                 },
              }
           ]
        }
        

* * *

#####  Example 3: Subsequent heartbeat requests when the grant is authorized 
        
        {
           "heartbeatRequest":[
              {
               "cbsdId":"SAS-assigned device ID",
               "grantId":"SAS-assigned grant ID",
               "operationState": "AUTHORIZED"
              }
           ]
        }
        

* * *




### Steps

Verify the following steps:

  1. The CBSD sends a spectrum inquiry for the channels with partial power. In the spectrum inquiry response, CBSD finds the available _maxEirp_ value in dBm on the relevant channels.
  2. The CBSD sends a grant request with _maxEirp_ greater than the available power for the channels in the spectrum inquiry response.
  3. The CBSD sends a heartbeat request.
  4. SAS sends the heartbeat response with `responseCode 501` (`Suspended_Grant: IAP Pending`).

**Note:** If you get an error such as `Error code 106 NOT_PROCESSED` during CPAS, pause your test and continue the test after the nightly CPAS cycle concludes. For more information about CPAS cycles, see [When CPAS runs](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync#cpas-run).

#####  Example 1: Spectrum inquiry response for an available channel with partial power 
         
         {
            "spectrumInquiryResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "availableChannel":{
                    {
                    "frequencyRange": {
                    "lowFrequency":3670000000,
                    "highFrequency":3680000000
                  },
                    "channelType": "GAA",
                    "ruleApplied": "FCC_PART_96",
                    "maxEirp": 26.73
               }
            ],
               "Response" {
               "responseCode": 0
               }
            }
            ]
         }
         

* * *

#####  Example 2: Heartbeat response when the grant request exceeds available power 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "response":{
                    "responseCode":501, {
                    "responseMessage":"SUSPENDED_GRANT : IAP Pending"
                    responseData = ["IAP Pending"]
                  }
               }
            ]
         }
         

* * *

#####  Example 3: Heartbeat request when the grant is suspended 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState": "GRANTED"
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 3a.** Test case 3a | Receives | Sends  
---|---|---  
SAS | 

  * Heartbeat requests with `operationState` set to **Granted** after CBSD is notified that the grant has been suspended through the heartbeat response
  * Heartbeat requests with `operationState` set to **Authorized** after the CBSD is notified through the heartbeat response that the grant has been authorized

| 

  * Heartbeat responses with `responseCode 0` (`Success`) when the grant is not suspended
  * Heartbeat responses with `responseCode 501` (`Suspended_Grant:IAP Pending`) when the grant is suspended

  
CBSD | 

  * Heartbeat responses with `responseCode 0` (`Success`), as long as the suspension zone isn't active
  * Heartbeat responses with `responseCode 501` (`Suspended_Grant`), until the current grant expires and a new grant is requested, or until additional power is available after a CPAS cycle
  * The CBSD stops the transmission (turns off the radio) less than 60 seconds after the `transmitExpireTime`

| 

  * Heartbeat requests with `operationState` set to **Authorized** after the CBSD is notified that the grant has been authorized through the heartbeat response
  * Subsequent heartbeat requests that have `operationState` set to **Granted** after the CBSD is notified that the grant has been suspended through the heartbeat response
  * Optional: Spectrum Inquiry request to determine which channels are available **Important:** Limitations due to an [Environmental Sensing Capability (ESC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#esc) event can't be reflected in the SAS response to a spectrum inquiry request. 

  
  
The interference calculations are complete, but SAS can't authorize transmission with the grant because after CPAS, the CBSD's grant is terminated and the use of low power is suggested. The CBSD requests a grant after it receives the operation parameters from the terminating heartbeat response.

We strongly recommend that the CBSD requests a new grant. If the grant request is for a frequency range outside of the suspension zone's frequency range , CBSD receives authorization to transmit in the heartbeat response. If authorized, the CBSD resumes transmission with a new grant. After the suspension is lifted, the CBSD resumes transmission on the original grant and ends the interim grant. For more information , see [Troubleshoot issues with interoperability testing](https://docs.cloud.google.com/spectrum-access-system/docs/iot-troubleshoot).

## Test case 3b: Grant suspension: DPA move list activated

This test case verifies the following:

  * The CBSD radio turns off when SAS suspends the CBSD's grant.
  * The CBSD reports the correct operation state in subsequent heartbeat requests.



### Prerequisites

Make sure that the following is true:

  * The CBSD is registered at a location inside the simulated suspension zone. 

#####  Example 

Learn about the [suspension zone in the SAS testing instance](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#simulated-entities).
        
        {
            "registrationRequest":[
              {
                 . . .
                 . . .
                 "installationParam":{
                    "latitude":62.5,
                    "longitude":-155.5,
                    . . .
                    . . .
                 }
              }
           ]
        }
        

* * *

  * The CBSD holds a grant that partially or fully overlaps the frequency range of the suspension zone. 

#####  Example 
        
        {
           "grantRequest":[
             . . .
             {
                 "operationFrequencyRange":{
                     "lowFrequency":3550 - 3615 MHz (e.g. 3550000000),
                     "highFrequency":3555 - 3700 MHz
                     . . .
                 }
              }
           ]
        }
        

* * *

  * The CBSD sends a heartbeat request. The grant is authorized by SAS as long as the suspension zone isn't active. 

#####  Example 1: The first heartbeat request after a grant is approved 
        
        {
           "heartbeatRequest":[
              {
                 "cbsdId":"SAS-assigned device ID",
                 "grantId":"SAS-assigned grant ID",
                 "operationState":"GRANTED"
              }
           ]
        }
        

* * *

#####  Example 2: Heartbeat response when the suspension zone isn't active 
        
        {
           "heartbeatResponse":[
              {
                 "cbsdId":"SAS-assigned device ID",
                 "grantId":"SAS-assigned grant ID",
                 "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
                 "heartbeatInterval": 60,
                 "response":{
                    "responseCode":0
                 },
              }
           ]
        }
        

* * *

#####  Example 3: Subsequent heartbeat requests when the suspension zone isn't active 
        
        {
           "heartbeatRequest":[
              {
                 "cbsdId":"SAS-assigned device ID",
                 "grantId":"SAS-assigned grant ID",
                 "operationState":"AUTHORIZED"
              }
           ]
        }
        

* * *




### Steps

Verify the following steps:

  1. Wait until the suspension zone is deactivated. For more information, see [Check the suspension zone schedule](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#protected-entities).
  2. SAS suspends the grant when the suspension zone is active, as specified in the suspension zone schedule.
  3. The CBSD sends a heartbeat request.
  4. SAS sends the heartbeat response with `responseCode 501` (Suspended_Grant : IAP Pending, "The grant is suspended because it is in the move list of a DPA that has been activated").
  5. Optional: The CBSD sends a spectrum inquiry request after the grant is suspended. 

#####  Example 1: Heartbeat response when the suspension zone is active 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "response":{
                     "responseCode":501,
                     "responseMessage":"SUSPENDED_GRANT : The grant is suspended because it is in the move list of a DPA that has been activated."
                     responseData = ["The grant is suspended because it is in the move list of a DPA that has been activated."]
                  }
               }
            ]
         }
         

* * *

#####  Example 2: Heartbeat request when the grant is suspended 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState":"GRANTED"
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 3b.** Test case 3b | Receives | Sends  
---|---|---  
SAS | 

  * Heartbeat requests with `operationState` set to **Granted** after CBSD is notified that the grant has been suspended through the heartbeat response
  * Heartbeat requests with `operationState` set to **Authorized** after the CBSD is notified through the heartbeat response that the grant has been authorized

| 

  * Heartbeat responses with `responseCode 0` (`Success`) when the suspension zone is not active
  * Heartbeat responses with `responseCode 501` (`Suspended_Grant: The grant is suspended because it is in the move list of a DPA that has been activated."`) when the suspension zone is active

  
CBSD | 

  * Heartbeat responses with `responseCode 0` (`Success`) for as long as the suspension zone isn't active
  * Heartbeat responses with `responseCode 501` (`Suspended_Grant: The grant is suspended because it is in the move list of a DPA that has been activated.`) for as long as the suspension zone is active
  * The CBSD stops the transmission, (turns off the radio) less than 60 seconds after the `transmitExpireTime`

| 

  * Heartbeat requests with `operationState` set to **Authorized** after the CBSD is notified through the heartbeat response that the grant has been authorized
  * Subsequent heartbeat requests that have `operationState` set to **Granted** after the CBSD has been notified through the heartbeat response that the grant has been suspended
  * Optional: Spectrum inquiry request to determine which channels are available.
**Important:** Limitations due to an ESC event can't be reflected in the SAS response to a spectrum inquiry request.
  
  
We strongly recommend that the CBSD requests a new grant. If the grant request is for a frequency range outside of the suspension zone's frequency range, CBSD receives authorization to transmit in the heartbeat response. If authorized, the CBSD resumes transmission with a new grant. Throughout the transmission, CBSD continues to heartbeat on the original (suspended) grant. After the suspension is lifted, CBSD resumes transmission on the original grant and terminates the interim grant.

## Test case 4: Grant reauthorization

This test case verifies that the CBSD can resume transmission after the suspension zone is deactivated. The CBSD behavior verified in this test is similar to what happens when the CBSD grant is suspended due to DPA protection and then reauthorized after the DPA is deactivated.

### Prerequisites

Make sure that the following is true:

  * The CBSD is registered at a location inside the suspension zone. For more information, see [suspension zone](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#protected-entities). 

#####  Example 
        
        {
        "registrationRequest":[
          {
             . . .
             . . .
             "installationParam":{
                "latitude":62.5,
                "longitude":-155.5,
                . . .
                . . .
             }
          }
        ]
        }
        

* * *

  * The CBSD is heartbeating and holds a grant that partially or completely overlaps the frequency range of the suspension zone.
  * The suspension zone is active and the CBSD discovers that the grant has been suspended.



### Steps

Verify the following steps:

  1. The CBSD continues heartbeating while the grant is suspended.
  2. SAS sends heartbeat responses with `responseCode 501` (`Suspended_Grant`).
  3. After the suspension zone is deactivated, SAS approves the heartbeat requests with `responseCode` (`Success`).
  4. The CBSD resumes transmission after receiving approval from SAS.
  5. The CBSD sends subsequent heartbeat requests with `operationState` set to **Authorized**.



### Result

The expected results from the test are listed in the following table.

**Table 4.** Test case 4 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | Heartbeat requests with `operationState` set to **Granted** | 

  * Heartbeat responses with `responseCode 501` (`Suspended_Grant`) while the suspension zone is active
  * Heartbeat responses with `responseCode 0` (`Success`) after the suspension zone is deactivated

|   
CBSD | 

  * Heartbeat responses with `responseCode 501` (`Suspended_Grant`) when the suspension zone is active
  * Heartbeat responses with `responseCode 0` (`Success`) after the suspension zone is deactivated

| Heartbeat responses with `operationState` set to **Granted** or **Authorized** | The CBSD resumes transmission (turns on the radio) after it has received `responseCode 0.`  
  
## Test case 5a: Termination of an authorized grant with suggested operational parameters

This test case verifies the following:

  * The CBSD stops its heartbeat and stop the transmission associated with the grant that was terminated by SAS.
  * The CBSD requests a new grant by using the operational parameters recommended by SAS in the heartbeat response.



### Prerequisites

Make sure that the following is true:

  * The CBSD is registered at a location inside the termination zone. [Learn more about the termination zone](https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities#termination-zone).
  * The CBSD is registered at a location inside the test SAS simulated suspension zone. 

#####  Example 
        
        {
           "registrationRequest":[
              {
        . . .
        . . .
                 "installationParam":{
                    "latitude":66.5,
                    "longitude":-158.5,
        . . .
        . . .
                 }
              }
           ]
        }
        

* * *

  * The CBSD holds a grant and is heartbeating.
  * The `operationFrequencyRange` of the grant partially or fully overlaps with 3550 MHz to 3620 MHz.



### Steps

Verify the following steps:

  1. SAS automatically terminates the grant according to the time schedule in the termination zone.
  2. The CBSD sends a heartbeat request.
  3. SAS sends the heartbeat response with `responseCode 500` (`Terminated_Grant`).

**Important:** In this test case, SAS suggests a new `operationFrequencyRange` between 3620 MHz and 3700 MHz. When the spectrum is available, SAS tries to match the bandwidth of the suggested frequency range to the bandwidth of the terminated grant. The suggested [EIRP](https://docs.cloud.google.com/spectrum-access-system/key-terms#eirp) is smaller than or equal to the EIRP of the terminated grant.

#####  Example 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "operationParam":{
                     "maxEirp":"New max EIRP",
                     "operationFrequencyRange":{
                        "lowFrequency":"New low frequency",
                        "highFrequency":"New high frequency"
                     }
                  },
                  "response":{
                     "responseCode":500,
                     "responseMessage":"TERMINATED_GRANT"
                  }
               }
            ]
         }
         

* * *

  4. The CBSD submits a grant request to SAS that includes the new recommended operational parameters. 

#####  Example 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "operationParam":{
                     "maxEirp":New max EIRP,
                     "operationFrequencyRange":{
                        "lowFrequency":New low frequency,
                        "highFrequency":New high frequency
                     }
                  }
               }
            ]
         }
         

* * *

  5. The CBSD receives a grant response from SAS. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 5a.** Test case 5a | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Heartbeat request
  * Valid grant request with the new operational parameters

| 

  * Heartbeat responses with `responseCode 500` (`Terminated_Grant`) for the first heartbeat request after the grant has been terminated
  * Successful grant response after the CBSD requests a grant with the new operational parameters

|   
CBSD | 

  * Heartbeat responses with `responseCode 500` (`Terminated_Grant`)
  * Successful grant response

| 

  * Heartbeat request
  * Valid grant request with the operational parameters that SAS suggests in the termination heartbeat response

| 

  * Stops sending heartbeat requests to SAS for the terminated grant
  * The CBSD stops the transmission less than 60 seconds after the `transmitExpireTime`.

  
  
## Test case 5b: Termination of an authorized grant from a channel mask in the SAS Portal

This test case verifies the following:

  * The CBSD stops heartbeating and ends transmission on a terminated grant.
  * The CBSD requests a new grant for one of the available channels from a spectrum inquiry without requiring user intervention.



### Prerequisites

Make sure that the following is true:

  * The CBSD holds a grant and is heartbeating.
  * The CBSD continues to send heartbeats until SAS terminates the grant.



### Steps

Verify the following steps:

  1. In the [SAS Portal](https://wirelessconnectivity.google.com/sas), [set a channel mask](https://docs.cloud.google.com/spectrum-access-system/docs/channel-masks) that restricts at least one currently granted channel.
  2. SAS terminates the grant at the time specified for this CBSD in the SAS Portal.
  3. The CBSD sends a heartbeat request.
  4. SAS sends the heartbeat response with `responseCode 500` (`Terminated_Grant`). 

#####  Example 
         
         {
            "heartbeatResponse":[
               {
              "cbsdId":"SAS-assigned device ID",
              "grantId":"SAS-assigned grant ID",
              "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
              "response":{
                 "responseCode":500,
                 "responseMessage":"TERMINATED_GRANT"
                 }
              }
           ]
         }
         

* * *

  5. The CBSD sends a spectrum inquiry request to SAS. For an example, see Test Case 1.
  6. SAS sends a spectrum inquiry response with a list of available channels.
  7. The CBSD sends a grant request to SAS for one of the channels listed in the spectrum inquiry response. 

#####  Example 
         
         {
          "grantRequest":[
             {
                "cbsdId":"SAS-assigned device ID",
                "operationParam":{
                   "maxEirp":New max EIRP
                   ""operationFrequencyRange":{
                      "lowFrequency":"New low frequency",
                      "highFrequency":New high frequency
                   }
                }
             }
          ]
         }
         

* * *

  8. The CBSD receives a grant response from SAS. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  9. The CBSD sends a heartbeat request for the new grant.



### Result

The expected results from the test are listed in the following table.

**Table 5b.** Test case 5b | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Heartbeat request
  * Spectrum inquiry request
  * Valid grant request for an available channel

| 

  * Heartbeat responses with `responseCode 500` (`Terminated_Grant`) for the first heartbeat request after CPAS has ended
  * Successful grant response after the CBSD requests a grant with the new operational parameters
  * Spectrum inquiry response with a list of available channels
  * Successful grant response after the CBSD requests a grant for an available channel

|   
CBSD | 

  * Heartbeat responses with `responseCode 500` (`Terminated_Grant`)
  * Spectrum inquiry response
  * Successful grant response

| 

  * Heartbeat request
  * Spectrum inquiry request
  * Valid grant request for one of the available channels

| 

  * Stops sending heartbeat requests to SAS for the terminated grant
  * The CBSD stops the transmission less than 60 seconds after the `transmitExpireTime`

  
  
## Test case 6: Grant request failure

This test case verifies that the CBSD does not start the heartbeat process or transmission if a grant request does not succeed.

### Prerequisites

Make sure that the CBSD is registered at a location inside the Grandfathered Wireless Protection Zone (GWPZ). 

#####  Example: Registration inside the GWPZ 
    
    
      {
        "registrationRequest":[
         {
           . . .
           . . .
           "installationParam":{
           "latitude":70,
           "longitude":-162,
            . . .
            . . .
          }
         }
       ]
      }
    

* * *

### Steps

Verify the following steps:

  1. The CBSD sends a grant request to SAS. 

#####  Example: Grant request for frequencies precluded by the GWPZ 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3650 - 3695 MHz (e.g. 3650000000),
                        "highFrequency":3655 - 3700 MHz
                     }
                  }
               }
            ]
         }
         

* * *

  2. SAS responds by rejecting the grant request with `responseCode 400` (`Interference`). 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "response":{
                     "responseCode":400,
                     "responseMessage":"Inside GWPZ"
                  }
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 6.** Test case 6 | Receives | Sends  
---|---|---  
SAS | Grant request | Grant response with `responseCode 400` (`Interference`) In this case, the CBSD is inside the GWPZ and is requesting a grant on a protected frequency, but it can be for any other reason.  
CBSD |  Grant response with `responseCode 400` (`Interference`) The CBSD should not start heartbeating or transmitting. | Grant request  
  
## Test case 7: CBSD deregistration and re-registration

This test case verifies that the CBSD deregisters itself from SAS and re-registers when it is moved from one location to another location more than 50 meters away.

### Prerequisites

Make sure that the CBSD is registered, has a grant, and is heartbeating. 

#####  Example: CBSD coordinates in the initial registration request 
    
    
        {
           "registrationRequest":[
              {
                 . . .
                 . . .
    
    
    
             "installationParam":{
                "latitude":37.4,
                "longitude":-122.0,
             . . .
             . . .
    
             }
          }
       ]
    }
    

* * *

### Steps

Verify the following steps:

  1. Set the CBSD position to another location selected more than 50 meters away. This can be done by either physically moving it or by setting its location manually.
  2. The CBSD optionally sends a deregistration request due to the change in location. 

#####  Example 
         
         {
            "deregistrationRequest":{
               "cbsdId":"SAS-assigned device ID"
            }
         }
         

* * *

  3. The CBSD then sends a new registration request with the new location.

**Note:** The new coordinates and other fields are the same as before.

#####  Example 
         
         {
            "registrationRequest":[
               {
                  . . .
                  . . .
         
                  "installationParam":{
                     "latitude":37.5,
                     "longitude":-122.1,
                  . . .
                  . . .
                  }
               }
            ]
         }
         

* * *

  4. SAS sends a registration response with `responseCode 0`. 

#####  Example 
         
         {
            "registrationResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 7.** Test case 7 | Receives | Sends  
---|---|---  
SAS | 

  * Registration request with start location information
  * Optional: Deregistration request
  * Registration request with new location information

| 

  * Registration response with `responseCode 0`
  * Optional: Deregistration response with `responseCode 0`
  * Registration response with `responseCode 0`

  
CBSD | 

  * Registration response with `responseCode 0`
  * Optional: Deregistration response with `responseCode 0`
  * Registration response with `responseCode 0`

| 

  * Registration request with start location information
  * Optional: Deregistration request
  * Registration request with the new location

  
  
## Test case 8: Grant expiration and renewal

This test case verifies the CBSD behavior when a grant is about to expire.

### Prerequisites

Make sure that the CBSD is registered, holds a grant, and is heartbeating.

### Steps

Verify the following steps:

  1. The CBSD sends a heartbeat request to SAS with `grantRenew` set to **true** before the grant expires. 

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "operationState": "AUTHORIZED",
                  "grantRenew":"true"
               }
            ]
         }
         

* * *

  2. SAS sends a new `grantExpireTime` in the heartbeat response if the CBSD requests grant renewal. 

#####  Example 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID",
                  "grantId":"SAS-assigned grant ID",
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
                  "heartbeatInterval": 60,
                  "response":{
                     "responseCode":0
                  },
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 8.** Test case 8 | Receives | Sends  
---|---|---  
SAS | Heartbeat request that also requests grant renewal | Heartbeat response that contains a new `grantExpireTime` value  
CBSD | Heartbeat response that contains a new `grantExpireTime` value | Heartbeat request with `grantRenew` set to **true** before the grant expires  
  
## Test case 9: CBSD handling of invalid or missing values

This test case shows examples of invalid requests. The CBSD does not need to follow the instructions step-by-step, but the tester should verify that after the CBSD receives a response code indicating that there is an error in the request, it does not retry the same (invalid) request.

### Prerequisites

Make sure that the CBSD is not registered in SAS.

### Steps

  1. The CBSD sends a registration request to SAS. 

#####  Example 1: Requests with errors 

The FCC ID field in strike-through text is omitted in the request, even though it's required for CBSD registration. 
         
         {
            "registrationRequest":[
               {
                  ~~"fccId":" whitelisted FCC ID"~~,
                  "userId":"whitelisted user ID",
                  "cbsdSerialNumber":"<unique device ID>",
                  "cbsdCategory":"A",
                  "airInterface":{
                     "radioTechnology":"E_UTRA"
                  },
                  "installationParam":{
                     "latitude": latitude within US,
                     "longitude": longitude within US,
                     "height":9,
                     "heightType":"AGL",
                     "indoorDeployment":false,
                     "antennaGain":16
                  },
                  "cbsdInfo":{
                     "vendor": "CBSD Vendor 1",
                     "model": "CBSD Model 1",
                     "softwareVersion": "2.0",
                     "hardwareVersion": "2.0",
                     "firmwareVersion": "2.0"
                  }
               }
           ]
         }
         

* * *

#####  Example 2: A second registration request with latitude and longitude values set to 0 (zero) 

This is to test CBSD handling of invalid data. The CBSD is expected to correct the fields before resending the request. 
         
         {
            "registrationRequest":[
               {
                  "fccId":"whitelisted FCC ID",
                  "userId":"whitelisted user ID",
                  "cbsdSerialNumber":"unique device ID",
                  "cbsdCategory":"A",
                  "airInterface":{
                     "radioTechnology":"E_UTRA"
                  },
                  "installationParam":{
                     "latitude": 0,
                     "longitude": 0,
                     "height":12,
                     "heightType":"AGL",
                     "indoorDeployment":false,
                     "antennaGain":20
                  },
                  "cbsdInfo":{
                     "vendor": "CBSD Vendor 1",
                     "model": "CBSD Model 1",
                     "softwareVersion": "2.0",
                     "hardwareVersion": "2.0",
                     "firmwareVersion": "2.0"
                  }
               }
         
            ]
         }
         

* * *

  2. SAS rejects the registration request with one of the following:

     * `responseCode 102` (`Missing_Param`). Enter the missing parameters in the `responseData` field. 

#####  Example 
           
           {
            "registrationResponse":[
               {
                  "response":{
                     "responseCode":102,
                     "responseData":["fccId"],
                     "responseMessage":"Missing field: fccId"
                  }
               }
           ]
           }
           

* * *

     * `responseCode 103` (`Invalid_Value`). Enter the parameters with invalid values in the `responseData` field. 

#####  Example 
           
           {
           "registrationResponse":[
               {
                  "response":{
                     "responseCode":103,
                     "responseData":["latitude", "longitude"],
                     "responseMessage":"Invalid field: latitude, longitude"
                  }
               }
            ]
           }
           

* * *




### Result

The expected results from the test are listed in the following table.

**Table 9.** Test case 9 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | Registration request without the necessary fields specified or with invalid values | One of the following: 

  * Registration response with `responseCode 102` (`Missing_Param`) and missing parameters in the `responseData` field
  * Registration response with `responseCode 103` (`Invalid_Value`) and the parameters with invalid values in the `responseData` field

|   
CBSD | Registration response with non-zero response code | Incomplete or invalid registration request | The CBSD must not try the same request until the error is fixed.  
  
## Test case 10: CBSD measurement reporting for RECEIVED_POWER_WITHOUT_GRANT

This test verifies that the CBSDs that support the `Received_Power_Without_Grant` measurement capability send measurement reports as prescribed in [WINNF-17-SSC-0002](https://cbrs.wirelessinnovation.org/policies-and-procedures).

### Prerequisites

Make sure that the CBSD is not registered.

### Steps

Verify the following steps:

  1. The CBSD sends a registration request to SAS that includes `Received_Power_Without_Grant` as one of its measurement capabilities.
  2. SAS replies with a registration response that includes `Received_Power_Without_Grant` in the measurement report configuration.
  3. Optional: The CBSD sends a spectrum inquiry request that contains a valid measurement.
  4. If the spectrum inquiry request is sent, SAS sends a spectrum inquiry response with `responseCode 0`.
  5. The CBSD sends a grant request that contains a valid measurement.
  6. SAS sends a grant response with `responseCode 0`.



### Result

The expected results from the test are listed in the following table.

**Table 10.** Test case 10 | Receives | Sends  
---|---|---  
SAS | 

  * Registration request that includes `Received_Power_Without_Grant` as one of the measurement capabilities
  * Optional: Spectrum inquiry request that contains a valid measurement
  * Grant request that contains a valid measurement

| 

  * Registration response
  * Optional: Spectrum inquiry response
  * Grant response

  
CBSD | 

  * Registration response
  * Optional: Spectrum inquiry request
  * Grant request that contains a valid measurement
  * Grant response

| 

  * Registration request
  * Optional: Spectrum inquiry request that contains a valid measurement
  * Grant request that contains a valid measurement

  
  
## Test case 11: CBSD measurement reporting for RECEIVED_POWER_WITH_GRANT

This test verifies that the CBSDs that support the `Received_Power_With_Grant` measurement capability send measurement reports as prescribed in [WINNF-17-SSC-0002](https://cbrs.wirelessinnovation.org/policies-and-procedures).

### Prerequisites

Make sure that the CBSD is not registered.

### Steps

Verify the following steps:

  1. The CBSD sends a registration request to SAS that includes `Received_Power_With_Grant` as one of its measurement capabilities.
  2. SAS replies with a registration response with `responseCode 0`.
  3. Optional: The CBSD sends a spectrum inquiry request.
  4. SAS sends a spectrum inquiry response with `responseCode 0`.
  5. The CBSD sends a valid grant request.
  6. SAS sends a grant response that includes `Received_Power_With_Grant` in the measurement report configuration.
  7. Within the first five heartbeat requests, the CBSD sends at least one request that contains a valid measurement.
  8. SAS sends heartbeat responses with `responseCode 0`.



### Result

The expected results from the test are listed in the following table.

**Table 11.** Test case 11 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Registration request from the CBSD that includes `Received_Power_With_Grant` as one of the measurement capabilities
  * Optional: A spectrum inquiry request
  * Valid grant request from the CBSD
  * Any number of heartbeat requests, with at least one of the first five containing a valid measurement

| 

  * Registration response
  * Optional: Spectrum inquiry response
  * Grant response that includes `Received_Power_With_Grant` in the measurement report configuration
  * Heartbeat response(s) with `responseCode 0`

|   
CBSD | 

  * Registration response
  * Optional: Spectrum inquiry request
  * Grant response

| 

  * Registration request that includes `Received_Power_With_Grant` as one of the measurement capabilities
  * Optional: Spectrum inquiry request
  * Grant request
  * Any number of heartbeat requests, with at least one of the first five containing a valid measurement

| After the first successful heartbeat, the CBSD starts transmission on the corresponding channel and power.  
  
## Test case 12: Batch requests

This test case verifies that a Domain Proxy (DP) is capable of sending batch requests and receiving batch responses for multiple CBSDs.

In particular, this test case focuses on the following:

  * The batch spectrum query for multiple CBSDs
  * The batch grant procedure for multiple CBSDs
  * The first batch heartbeat to turn the radios on for multiple CBSDs

**Important:** Registration batch messages are not tested because they are used less frequently in a typical deployment.

### Prerequisites

**Important:** This test case requires 2 to 20 CBSDs and a DP that relays SAS messages for each CBSD. The largest batch size for the test environment is 20. This is different from the production environment, where the largest batch size is 120.

Make sure that the following is true:

  * The CBSDs are registered with SAS.
  * The DP is set to request a subset of the spectrum that is available.



### Steps

Verify the following steps:

  1. The DP sends a batch spectrum query request to check available spectrum for each CBSD. 

#####  Example 
         
         {
              "spectrumInquiryRequest":[
                 {
                    "cbsdId":"SAS-assigned device ID #1",
                    "inquiredSpectrum":[
                       {
                          "lowFrequency":within 3550 - 3700 MHz range,
                          "highFrequency":within 3550 - 3700 MHz range
                       }
                    ]
                 },
                 {
                    "cbsdId":"SAS-assigned device ID #2",
                    "inquiredSpectrum":[
                       {
                          "lowFrequency":within 3550 - 3700 MHz range,
                          "highFrequency":within 3550 - 3700 MHz range
                       }
                    ]
                 },
                 ...
                 {
                    "cbsdId":"SAS-assigned device ID #N",
                    "inquiredSpectrum":[
                       {
                          "lowFrequency":within 3550 - 3700 MHz range,
                          "highFrequency":within 3550 - 3700 MHz range
                       }
                    ]
                 }
              ]
           }
           

* * *

  2. For each CBSD, the DP receives a list of available channels from SAS. 

#####  Example 
         
         {
            "spectrumInquiryResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "availableChannel":[
                     {
                        "frequencyRange":{
                           "lowFrequency":3550 - 3700 MHz,
                           "highFrequency":3550 - 3700 MHz
                        },
                        "channelType":"GAA",
                        "ruleApplied":"FCC_PART_96",
                        "maxEirp": 37
                     },
                     ...
                  ],
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "availableChannel":[
                     {
                        "frequencyRange":{
                           "lowFrequency":3550 - 3700 MHz,
                           "highFrequency":3550 - 3700 MHz
                        },
                        "channelType":"GAA",
                        "ruleApplied":"FCC_PART_96",
                        "maxEirp": 37
                     },
                     ...
                  ],
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "availableChannel":[
                     {
                        "frequencyRange":{
                           "lowFrequency":3550 - 3700 MHz,
                           "highFrequency":3550 - 3700 MHz
                        },
                        "channelType":"GAA",
                        "ruleApplied":"FCC_PART_96",
                        "maxEirp": 37
                     },
                     ...
                  ],
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  3. The DP sends a batch grant request to SAS. For each CBSD, the DP requests a frequency range that SAS specified was available. 

#####  Example 
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               }
            ]
         }
         

* * *

  4. The DP receives a batch grant response from SAS. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  5. The DP sends batch heartbeat requests to SAS periodically based on the `heartbeatInterval` and receives batch heartbeat responses from SAS.

**Important:** The first heartbeat request for each CBSD must have `operationState` set to **Granted**.

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "operationState":"GRANTED"
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "operationState":"GRANTED"
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "operationState":"GRANTED"
               }
            ]
         }
         

* * *

  6. SAS responds by approving the heartbeat requests. 

#####  Example 
         
         {
            "heartbeatResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "response":{
                     "responseCode":0
                  },
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "response":{
                     "responseCode":0
                  },
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "response":{
                     "responseCode":0
                  },
                  "transmitExpireTime":"YYYY-MM-DDTHH:MM:SSZ"
               }
         

* * *

  7. The DP sends subsequent batch heartbeat requests to SAS periodically based on the `heartbeatInterval` with the field `operationState`, which belongs to any particular CBSD set to **Authorized** if the previous heartbeat request was approved. 

#####  Example 
         
         {
            "heartbeatRequest":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "operationState":"AUTHORIZED"
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "operationState":"AUTHORIZED"
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "operationState":"AUTHORIZED"
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 12.** Test case 12 | Receives | Sends  
---|---|---  
SAS | 

  * Valid batch spectrum inquiry request, including one request for each CBSD
  * Valid batch grant request, including one request for each CBSD
  * Valid periodic batch heartbeat requests, including one request for each CBSD at least every `heartbeatInterval` seconds

| Successful batch responses to all batch requests. The `transmitExpire` time in the heartbeat responses is set to a value during four minutes.  
DP | 

  * Successful batch responses to all batch requests
  * After the first successful heartbeat response, each CBSD starts transmission on the corresponding channel and power

| 

  * Valid batch spectrum inquiry request, including one request for each CBSD
  * Valid batch grant request, including one request for each CBSD
  * Valid periodic batch heartbeat requests at least every `heartbeatInterval` second, including one request for each CBSD. The field `operationState` that belongs to any particular CBSD should be set to **Authorized** in at least one heartbeat request.

  
  
## Test case 13: Oversized batch requests

This test case verifies that a [Domain Proxy (DP)](https://docs.cloud.google.com/spectrum-access-system/key-terms#dp) is capable of handling a situation where the size of a batch request exceeds the maximum batch size that is processed by SAS.

When the batch size is larger than `maxBatchSize`, SAS sends a valid response to the first `maxBatchSize` requests with the `responseCode` field set to `0` (`Success`). For the remainder of the requests, SAS sends `responseCode 106` (`Not_Processed`).

The default value of `maxBatchSize` in the production SAS environment is `120`. To support easy testing, the `maxBatchSize` in the test SAS environment is `20`.

In particular, this test case focuses on the grant request process to demonstrate how to handle oversized batch requests.

We recommend that you extend this test case to include other message types, such as registration requests, spectrum inquiry, heartbeat procedure, grant relinquishment procedure, and deregistration.

### Prerequisites

**Important:** The test case requires 2 to 20 CBSDs, and a DP that relays SAS messages for each CBSD.

Make sure that the following is true:

  * The CBSDs are registered with SAS.
  * The DP is set to request a subset of the spectrum that is available.



### Steps

Verify the following steps:

  1. The DP sends an oversized batch grant request to SAS. The size of the batch is N, where N is from 20 to 40. For each CBSD, the DP requests a frequency range that SAS specified was available. 

#####  Example 
         
         {
                "grantRequest":[
                   {
                      "cbsdId":"SAS-assigned device ID #1",
                      "operationParam":{
                         "maxEirp":20,
                         "operationFrequencyRange":{
                            "lowFrequency":3550 - 3700 MHz,
                            "highFrequency":3550 - 3700 MHz
                         }
                      }
                   },
                   {
                      "cbsdId":"SAS-assigned device ID #2",
                      "operationParam":{
                         "maxEirp":20,
                         "operationFrequencyRange":{
                            "lowFrequency":3550 - 3700 MHz,
                            "highFrequency":3550 - 3700 MHz
                         }
                      }
                   },
                   ...
                   {
                      "cbsdId":"SAS-assigned device ID #N",
                      "operationParam":{
                         "maxEirp":20,
                         "operationFrequencyRange":{
                            "lowFrequency":3550 - 3700 MHz,
                            "highFrequency":3550 - 3700 MHz
                         }
                      }
                   }
                ]
             }
           

* * *

  2. The DP receives a batch grant response from SAS. SAS sends a valid response to the first 20 requests with the `responseCode` field set to `0` (`Success`). SAS sets the `responseCode` field to `106` (`Not_Processed`) for the last N to 20 items in the batch. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #20",
                  "grantId":"SAS-assigned grant ID #20",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #21",
                  "response":{
                     "responseCode":106,
                     "responseMessage":"The Google SAS requires that each request batch size be less than or equal to 20"
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #22",
                  "response":{
                     "responseCode":106,
                     "responseMessage":"The Google SAS requires that each request batch size be less than or equal to 20"
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "response":{
                     "responseCode":106,
                     "responseMessage":"The Google SAS requires that each request batch size be less than or equal to 20"
                  }
               }
            ]
         }
         

* * *

  3. The DP sends the grant requests that have not yet been processed. 

#####  Example 

The size of this batch request is less than 20 by design.
         
         {
            "grantRequest":[
               {
                  "cbsdId":"SAS-assigned device ID #21",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #22",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "operationParam":{
                     "maxEirp":20,
                     "operationFrequencyRange":{
                        "lowFrequency":3550 - 3700 MHz,
                        "highFrequency":3550 - 3700 MHz
                     }
                  }
               }
            ]
         }
         

* * *

  4. The DP receives a batch grant response from SAS. SAS sends a valid response to all requests with the `responseCode` field set to `0` (`Success`). 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #21",
                  "grantId":"SAS-assigned grant ID #21",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #22",
                  "grantId":"SAS-assigned grant ID #22",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *




### Result

The expected results from the test are listed in the following table.

**Table 13.** Test case 13 | Receives | Sends  
---|---|---  
SAS | 

  * Valid batch grant request, including one request for each CBSD for a batch size of 20 to 40 in the first attempt
  * Valid batch grant requests for the second part to the batch in the second attempt where the batch size is more than 20

| 

  * Successful batch responses to the first 20 grant requests, and `responseCode 106` for the rest of the batch in the first attempt
  * Successful batch responses to all grant requests in the second attempt

  
DP | 

  * Successful batch responses to the first 20 requests, and `responseCode 106` for the rest of the batch in the first attempt
  * Successful batch responses to all grant requests in the second attempt

| 

  * Valid batch grant request, including one request for each CBSD for a batch size of 20 to 40 in the first attempt
  * Valid batch grant requests for the second part to the batch in the second attempt where the batch size is more than 20

  
  
## Test case 14: Passive DAS registration and grant procedure

This test case verifies the following:

  * The registration and grant procedure for [Passive DAS](https://docs.cloud.google.com/spectrum-access-system/key-terms#p-das) radio equipment.
  * Optional: The spectrum inquiry process for Passive [DAS](https://docs.cloud.google.com/spectrum-access-system/key-terms#das) radio equipment.

**Important:** Registration batch messages are not tested because they are used less frequently in a typical deployment.

### Assumptions

  * **Deployment scenario**

In this test case, we assume a Category 3 deployment scenario as defined in [WINNF-TR-5001](https://winnf.memberclicks.net/assets/CBRS/WINNF-TR-5001.pdf): A single-sector Radio Unit (RU) deployed as a Passive DAS with multiple transmission points (TPs). [ ![{Category 3 deployment \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/category3-deployment.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/category3-deployment.svg) Category 3 deployment (click to enlarge)

  * **Unique CBSD identification**

In this case, each TP is registered as a single CBSD with the FCC ID and the manufacturer's serial number (MSN). The FCC ID and MSN of the RU is combined with an extra TP ID to uniquely identify each TP. The TP ID can be provided to SAS with suffixes in the `cbsdSerialNumber`. The TP ID must be appended to the MSN of the RU with a delimiter character (:) before the TP ID. For more information, see [WINNF-TR-5001](https://winnf.memberclicks.net/assets/CBRS/WINNF-TR-5001.pdf).

**Important:** Do not register an RU as a CBSD. When you register all TPs, it correctly account for the total radiated power created by the Passive DAS system.
  * **Indoor or outdoor determination**

In this test case, we assume an indoor deployment scenario. In general, you can deploy Passive DAS equipment either indoors or outdoors. To find the complete list of guidelines, see [WINNF-TR-5001](https://winnf.memberclicks.net/assets/CBRS/WINNF-TR-5001.pdf).

  * **EIRP capability**

For an indoor deployment, the max EIRP of each TP must be less than or equal to 30 dBm or 10 MHz. To find examples of how to calculate the EIRP capability for each TP, see [WINNF-TR-5001](https://winnf.memberclicks.net/assets/CBRS/WINNF-TR-5001.pdf).

  * **CBSD category**

For an indoor deployment, each TP must be registered as a Category A CBSD. This can be done even if the RU is originally certified by the FCC as a high-power Category B device. You cannot install Category B CBSDs indoors.

  * **CPI-assisted installation**

Current FCC guidance suggests that a Certified Professional Installer (CPI) must always install Passive DAS equipment. The reasons are as follows:

    * The FCC recommends CPI installation whenever you deploy a high-power Category B RU in an indoor environment with reduced power as a Category A CBSD.
    * Even if the RU is certified as a low-power Category A device, a typical TP doesn't have automatic geolocation capability. Therefore, a CPI must always install a Passive DAS.
  * **Multistep registration**

In this test case, we assume multistep registration. This means that before executing the test, a CPI must pre-load installation parameters for each TP into SAS through the SAS Portal. It's important that the CPI specifies the `eirpCapability` parameter in the `InstallationParam` object.

For this test case, `eirpCapability` must be set to no greater than 30 dBm or 10 MHz for each TP. If not included, in accordance with the [Release 1 WInnForum specification WINNF- TS-0016](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf), SAS sets `eirpCapability` as the rounded up FCC certified maximum EIRP of the RU. For a high-power RU, this can be greater than 30 dBm or 10 MHz, which isn't allowed for an indoor Category A installation.

**Important:** The URL for the SAS Portal in the test environment is different from the URL for the SAS Portal in the production environment. For more information, see [Get started with the test SAS environment](https://docs.cloud.google.com/spectrum-access-system/docs/connect-sastest) and [Understand the differences between the test and production SAS environments](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors#diff-sas).
  * **Domain Proxy (DP)**

In this test case, we assume the presence of a DP that can send and receive batch requests from SAS.




### Prerequisites

Make sure that the following is true:

  * The CBSDs (TPs) are not registered in the SAS Portal.
  * The CBSDs (TPs) are set to request a subset of the spectrum that is available.
  * The CPI provided registration parameters, including `eirpCapability` for each TP, which are preloaded into SAS through the SAS Portal.



### Steps

Verify the following steps:

  1. To register multiple TPs, the DP sends a batch registration request to SAS.

**Important:** The maximum batch size in the test environment is 20. Many TPs require multiple batch requests.

#####  Example 
         
         {
              "registrationRequest":[
                 {
                    "fccId":"allowed FCC ID of RU",
                    "userId":"allowed user ID",
                    "cbsdSerialNumber":"MSN of RU:TP ID #1",
                    "cbsdCategory":"A",
                    "airInterface":{
                       "radioTechnology":"E_UTRA",
                    },
                    "cbsdInfo":{
                      "vendor": "CBSD Vendor of RU",
                      "model": "CBSD Model of RU",
                      "softwareVersion": "2.0",
                      "hardwareVersion": "2.0",
                      "firmwareVersion": "2.0"
                    }
                 },
                 {
                    "fccId":"allowed FCC ID of RU",
                    "userId":"allowed user ID",
                    "cbsdSerialNumber":"MSN of RU:TP ID #2",
                    "cbsdCategory":"A",
                    "airInterface":{
                       "radioTechnology":"E_UTRA",
                    },
                    "cbsdInfo":{
                      "vendor": "CBSD Vendor of RU",
                      "model": "CBSD Model of RU",
                      "softwareVersion": "2.0",
                      "hardwareVersion": "2.0",
                      "firmwareVersion": "2.0"
                    }
                 },
                 ...
                 {
                    "fccId":"allowed FCC ID of RU",
                    "userId":"allowed user ID",
                    "cbsdSerialNumber":"MSN of RU:TP ID #N",
                    "cbsdCategory":"A",
                    "airInterface":{
                       "radioTechnology":"E_UTRA",
                    },
                    "cbsdInfo":{
                      "vendor": "CBSD Vendor of RU",
                      "model": "CBSD Model of RU",
                      "softwareVersion": "2.0",
                      "hardwareVersion": "2.0",
                      "firmwareVersion": "2.0"
                    }
                 }
              ]
           }
         

* * *

  2. The CBSD receives a batch registration response from SAS. 

#####  Example 
         
         {
            "registrationResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  3. To check available spectrum for each TP, the DP sends a batch spectrum inquiry request.

**Important:** The `inquiredSpectrum` field should be the same for each TP. In a single-sector Passive DAS deployment, all TPs must use the same RF channels.

#####  Example 
         
         {
            "spectrumInquiryRequest":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":F1 (within 3550 - 3700 MHz range),
                        "highFrequency":F2 (within 3550 - 3700 MHz range)
                     }
                  ]
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":F1 (within 3550 - 3700 MHz range),
                        "highFrequency":F2 (within 3550 - 3700 MHz range)
                     }
                  ]
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "inquiredSpectrum":[
                     {
                        "lowFrequency":F1 (within 3550 - 3700 MHz range),
                        "highFrequency":F2 (within 3550 - 3700 MHz range)
                     }
                  ]
               }
            ]
         }
         

* * *

  4. For each TP, the DP receives a list of available channels from SAS.

**Note:** The `availableChannel` field in the spectrum inquiry response from SAS doesn't need to be the same for all TPs because the list of available channels might vary based on the location of the TP.

#####  Example 
         
         {
          "spectrumInquiryResponse":[
             {
                "cbsdId":"SAS-assigned device ID #1",
                "availableChannel":[
                   {
                      "frequencyRange":{
                         "lowFrequency":3550 - 3700 MHz,
                         "highFrequency":3550 - 3700 MHz
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
                      "maxEirp": 37
                   },
                   ...
                ],
                "response":{
                   "responseCode":0
                }
             },
             {
                "cbsdId":"SAS-assigned device ID #2",
                "availableChannel":[
                   {
                      "frequencyRange":{
                         "lowFrequency":3550 - 3700 MHz,
                         "highFrequency":3550 - 3700 MHz
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
                      "maxEirp": 37
                   },
                   ...
                ],
                "response":{
                   "responseCode":0
                }
             },
             ...
             {
                "cbsdId":"SAS-assigned device ID #N",
                "availableChannel":[
                   {
                      "frequencyRange":{
                         "lowFrequency":3550 - 3700 MHz,
                         "highFrequency":3550 - 3700 MHz
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
                      "maxEirp": 37
                   },
                   ...
                ],
                "response":{
                   "responseCode":0
                }
             }
          ]
         }
         

* * *

  5. The DP sends a batch grant request to SAS. For each TP, the DP requests a frequency range that SAS specified as available.

     * The `maxEirp` value for each TP should not be more than 30 dBm or 10 MHz for an indoor deployment.
     * The `operationFrequencyRange` field should be the same for each TP. In a single-sector Passive DAS deployment, all TPs must use the same RF channels.

#####  Example 
    
    {
       "grantRequest":[
          {
             "cbsdId":"SAS-assigned device ID #1",
             "operationParam":{
                "maxEirp":value less than or equal to 30,
                "operationFrequencyRange":{
                   "lowFrequency":F1 (within 3550 - 3700 MHz),
                   "highFrequency":F2 (within 3550 - 3700 MHz)
                }
             }
          },
          {
             "cbsdId":"SAS-assigned device ID #2",
             "operationParam":{
                "maxEirp":value less than or equal to 30,
                "operationFrequencyRange":{
                   "lowFrequency":F1 (within 3550 - 3700 MHz),
                   "highFrequency":F2 (within 3550 - 3700 MHz)
                }
             }
          },
          ...
          {
             "cbsdId":"SAS-assigned device ID #N",
             "operationParam":{
                "maxEirp":value less than or equal to 30,
                "operationFrequencyRange":{
                   "lowFrequency":F1 (within 3550 - 3700 MHz),
                   "highFrequency":F2 (within 3550 - 3700 MHz)
                }
             }
          }
       ]
    }
    

* * *

  6. The DP receives a batch grant response from SAS. 

#####  Example 
         
         {
            "grantResponse":[
               {
                  "cbsdId":"SAS-assigned device ID #1",
                  "grantId":"SAS-assigned grant ID #1",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               {
                  "cbsdId":"SAS-assigned device ID #2",
                  "grantId":"SAS-assigned grant ID #2",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               },
               ...
               {
                  "cbsdId":"SAS-assigned device ID #N",
                  "grantId":"SAS-assigned grant ID #N",
                  "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                  "heartbeatInterval":60,
                  "channelType": GAA,
                  "response":{
                     "responseCode":0
                  }
               }
            ]
         }
         

* * *

  7. The DP sends batch heartbeat requests to SAS periodically based on the `heartbeatInterval` and receives batch heartbeat responses from SAS.

**Important:** The first heartbeat request for each CBSD must have `operationState` set to **Granted**. If the previous heartbeat request was approved, the field `operationState` that belongs to any particular TP must be set to **Authorized**. Find a more detailed example in Test Case 12.



### Result

The expected results from the test are listed in the following table.

**Table 14.** Test case 14 | Receives | Sends  
---|---|---  
SAS | 

  * Valid batch registration request, including one request for each TP
  * Valid batch spectrum inquiry request, including one request for each TP
  * Valid batch grant request, including one request for each TP
  * Valid periodic batch heartbeat requests, including one request for each TP at least every `heartbeatInterval` seconds

| Successful batch responses to all batch requests. The `transmitExpire` time in the heartbeat responses is set to a value during four minutes.  
DP | 

  * Successful batch responses to all batch requests
  * After the first successful heartbeat response, each TP starts transmission on the corresponding channel and power

| 

  * Valid batch registration request, including one request for each TP
  * Valid batch spectrum inquiry request, including one request for each TP
  * Valid batch grant request, including one request for each TP
  * Valid periodic batch heartbeat requests at least every `heartbeatInterval` second, including one request for each TP. The field `operationState` that belongs to any particular TP should be set to **Authorized** in at least one heartbeat request.

  
  
## Test case 15: Sorted spectrum inquiry response

This test case verifies that the CBSD can select the highest quality channels from a sorted spectrum inquiry response. [Learn how SAS calculates channel quality](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels#channel-quality).

### Assumptions

The CBSD tries to transmit on a single 10-MHz wide channel.

### Prerequisites

Make sure that the CBSD has been registered with SAS for at least four hours before the test. After the CBSD registers, SAS can take up to four hours to calculate channel quality and ranking.

**Tip:** On the SAS Portal, you can check the spectrum availability, channel quality, and channel ranking on the **Coex** tab of the CBSD.

For more accurate results, give frequency management grouping information for the CBSD either in the registration request or in the SAS Portal. Use Test Case 1 as an example.

### Steps

Verify the following steps:

  1. The CBSD sends a spectrum inquiry request to SAS for the entire CBRS frequency range 3550 MHz to 3700 MHz. 

#####  Example 
         
         {
              "spectrumInquiryRequest":[
                 {
                    "cbsdId":"SAS-assigned device ID #1",
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

  2. The CBSD receives a spectrum inquiry response from SAS. The spectrum inquiry response returns a list of available channels sorted from best channel quality to worst. The first object in the `availableChannel` array has the best quality. 

#####  Example 

In this example, the first `frequencyRange` object has the highest quality and will be reused in Step 3.
         
         {
          "spectrumInquiryResponse":[
             {
                "cbsdId":"SAS-assigned device ID",
                "availableChannel":[
                   {
                      "frequencyRange":{
                         "lowFrequency":3560000000,
                         "highFrequency":3570000000
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
                      "maxEirp": 37
                   },
                   {
                      "frequencyRange":{
                         "lowFrequency":3600000000,
                         "highFrequency":3610000000
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
                      "maxEirp": 37
                   },
                   {
                      "frequencyRange":{
                         "lowFrequency":3630000000,
                         "highFrequency":3640000000
                      },
                      "channelType":"GAA",
                      "ruleApplied":"FCC_PART_96",
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
                         "lowFrequency": 3570000000,
                         "highFrequency": 3580000000
                      },
                      "channelType": "GAA",
                      "ruleApplied": "FCC_PART_96",
                      "maxEirp": 37
                   },
                   {
                      "frequencyRange": {
                         "lowFrequency": 3550000000,
                         "highFrequency": 3560000000
                      },
                      "channelType": "GAA",
                      "ruleApplied": "FCC_PART_96",
                      "maxEirp": 37
                   }
                ],
                "response":{
                   "responseCode":0
                }
             }
          ]
         }
         

* * *

  3. The CBSD sends a grant request to SAS. The CBSD requests the channel with the highest ranking. This is the first element in the `availableChannel` array of the sorted spectrum inquiry response. 

#####  Example 
         
         {
          "grantRequest":[
             {
                "cbsdId":"SAS-assigned device ID",
                "operationParam":{
                   "maxEirp":27,
                   "operationFrequencyRange":{
                      "lowFrequency":3560000000,
                      "highFrequency":3570000000
                   }
                }
             }
          ]
         }
         

* * *

  4. The CBSD receives a grant response from SAS. 

#####  Example 
         
         {
          "grantResponse":[
             {
                "cbsdId":"SAS-assigned device ID",
                "grantId":"SAS-assigned grant ID",
                "grantExpireTime":"YYYY-MM-DDTHH:MM:SSZ",
                "heartbeatInterval":60,
                "channelType": GAA,
                "response":{
                   "responseCode":0
                }
             }
          ]
         }
         

* * *

  5. The CBSD sends heartbeat requests to SAS periodically based on `heartbeatInterval` and receives heartbeat responses from SAS. Review the requirements to send heartbeat requests in Test Case 1.



### Result

The expected results from the test are listed in the following table.

**Table 15.** Test case 15 | Receives | Sends | Acceptable  
---|---|---|---  
SAS | 

  * Valid spectrum inquiry request
  * Valid grant request for the highest ranking channel based on the spectrum inquiry response
  * Valid periodic heartbeat requests at least every `heartbeatInterval` second

| 

  * Successful sorted spectrum inquiry response
  * Successful grant response
  * Successful responses for all heartbeat requests, with `transmitExpireTime` included in the heartbeat responses.

|   
CBSD | 

  * Successful sorted spectrum inquiry response
  * Successful grant response
  * Successful heartbeat responses for all heartbeat requests

| After the first successful heartbeat, the CBSD starts transmission on the corresponding channel and power. | 

  * Valid spectrum inquiry request
  * Valid grant request for the highest-ranking channel based on the spectrum inquiry response
  * Valid periodic heartbeat requests at least every `heartbeatInterval` seconds, including at least one request in which the `operationState` is set to **Authorized**

  
SAS Portal |  |  | You can find spectrum availability, channel quality, and channel ranking on the **Coex** tab of the CBSD in the SAS Portal. [Find the URL of the test SAS environment](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors).  
  
## Test case 16: Same frequency

This test case verifies the following:

  * The CBSD or DP equipment sends the Same Frequency identifier to SAS each time the device registers.
  * The Same Frequency value can be set or edited in the SAS Portal for each device.



### Prerequisites

Make sure that the following is true:

  * The CBSD is not registered with SAS.
  * The CBSD or DP doesn't share the Same Frequency ID with SAS.



### Steps

Verify the following steps:

  1. Configure the WInnForum Same Frequency value info in the CBSD registration message. 

#####  Example 
         
         {
            "registrationRequest": [
            {
            "fccId": "abc123",
            "cbsdCategory": "A",
            "callSign": "CB987",
            "userId": "John Doe",
            "airInterface": {
            "radioTechnology": "E_UTRA"
            },
            "cbsdSerialNumber": "abcd1234",
            "measCapability": [
            "RECEIVED_POWER_WITHOUT_GRANT"
            ],
            "installationParam": {
            "latitude": 37.419735,
            "longitude": -122.072205,
            "height": 6,
            "heightType": "AGL",
            "indoorDeployment": true
            },
            "groupingParam": [
            { "groupId": "example-group-1",
            "groupType": "PRINCIPAL_SUBORDINATE_SFG" },
            ]
            },
           

* * *

  2. Register the device with SAS.
  3. If there's a change in the Same Frequency value, you can set up a new value in the heartbeat request message and send it to SAS.
  4. Optional: Use the SAS Portal to set or edit the Same Frequency value for the CBSD.

**Note:** You can document values that are set with the SAS Portal in the _Test Result_ sheet provided by Google.



### Result

The expected results from the test are listed in the following table.

**Table 16.** Test case 16 | Receives | Sends  
---|---|---  
SAS | 

  * Registration request or heartbeat message from the CBSD or DP, which includes the configured Same Frequency value
  * Optional: Same Frequency configuration for a CBSD in the SAS Portal

| Successful registration response to the CBSD or DP  
CBSD or DP | Successful registration response or heartbeat response | The Common Channel Group label for each CBSD during registration or by heartbeat when the Same Frequency value changes  
  
## Test case 17: Frequency reuse

This test case verifies the following:

  * The CBSD or DP equipment sends the Same Frequency reuse identifier to Google SAS each time the device registers.
  * The Frequency Reuse value can be set or edited in the SAS Portal for each device.



### Prerequisites

Make sure that the following is true:

  * The CBSD is not registered with SAS.
  * The CBSD or DP doesn't share the Same Frequency ID with SAS.



### Steps

Verify the following steps:

  1. Configure the WInnForum Same Frequency value info in the CBSD registration message. 

#####  Example 
         
         {
            "registrationRequest": [
            {
            "fccId": "abc123",
            "cbsdCategory": "A",
            "callSign": "CB987",
            "userId": "John Doe",
            "airInterface": {
            "radioTechnology": "E_UTRA"
            },
            "cbsdSerialNumber": "abcd1234",
            "measCapability": [
            "RECEIVED_POWER_WITHOUT_GRANT"
            ],
            "installationParam": {
            "latitude": 37.419735,
            "longitude": -122.072205,
            "height": 6,
            "heightType": "AGL",
            "indoorDeployment": true
            },
            "groupingParam": [
            { "groupId": "example-group-1",
            "groupType": "PRINCIPAL_SUBORDINATE_SFG" },
            ]
            },
           

* * *

  2. Register the device with SAS.
  3. If there's a change in the Same Frequency value, you can set up a new value in the heartbeat request message and send it to SAS.
  4. Optional: Use the SAS Portal to set or edit the Same Frequency value for the CBSD.

**Note:** You can document values that are set with the SAS Portal in the _Test Result_ sheet provided by Google.



### Result

The expected results from the test are listed in the following table.

**Table 17.** Test case 17 | Receives | Sends  
---|---|---  
SAS | 

  * Registration request or heartbeat message from the CBSD or DP, which includes the configured Frequency Reuse value
  * Optional: Frequency Reuse configuration for a CBSD in the SAS Portal

| Successful registration response to the CBSD or DP  
CBSD or DP | Successful registration response or heartbeat response | The Common Channel Group (CCG) label per CBSD during registration or by heartbeat when the Frequency Reuse value changes  
  
## Test case 18: Preference for multiple 10-MHz grant requests

This test case verifies that the CBSD or DP chooses to request multiple 10-MHz grants when multiple channels that are greater than 10 MHz are used for operation.

### Prerequisites

Make sure that the following is true:

  * The CBSD or DP is registered with SAS.
  * The CBSD is configured to utilize more than 10 MHz to operate.



### Steps

Verify the following steps:

  1. The CBSD or DP sends a grant request to SAS.
  2. The CBSD sends a spectrum inquiry request to query available spectrum. If SAS indicates availability, then the CBSD requests a 10-MHz channel. 

#####  Example 
         
         {
              "grantRequest":[
                {
                  "cbsdId":"SAS-assigned device ID",
                  "operationParam":{
                    "maxEirp":20,
                    "operationFrequencyRange":{
                      "lowFrequency":3550 - 3700 MHz (e.g. 3600000000),
                      "highFrequency":3550 - 3700 MHz
                    }
                  }
                }
              ]
           }
           

* * *

  3. The parameters `lowFrequency` and `highFrequency` are set for the selected 10-MHz channel.
  4. Multiple grants are requested for the number of channels determined necessary by the device.



### Result

The expected results from the test are listed in the following table.

**Table 18.** Test case 18 | Receives | Sends  
---|---|---  
SAS | Valid grant requests for the number of channels determined necessary by the device | Successful grant response for all valid requests  
CBSD or DP | A successful grant response for the number of requests possible, based on the device location and incumbent protection zones | One valid grant request per 10-MHz channel  
  
## Test case 19: Support for grants on non-contiguous channels

This test case verifies the following:

  * The CBSD or DP supports and requests grants for multiple non-contiguous 10-MHz channels for the same CBSD.
  * The CBSD or DP requests and accepts grants on separated channels that have been granted.



### Prerequisites

Make sure that the following is true:

  * The CBSD or DP is registered with SAS.
  * The CBSD is set to request a subset of the spectrum that's available per the spectrum inquiry response from SAS.



### Steps

Verify the following steps:

  1. The device is registered with SAS.
  2. The CBSD sends a spectrum inquiry request to query available spectrum. 

#####  Example 
         
         {
            "spectrumInquiryRequest":[
              {
                "cbsdId":"SAS-assigned device ID",
                "inquiredSpectrum":[
                  {
                    "lowFrequency":within 3550 - 3700 MHz range (e.g. 3550000000),
                    "highFrequency":within 3550 - 3700 MHz range (e.g. 3650000000)
                  }
                ]
              }
            ]
          }
           

* * *

  3. The CBSD receives a list of available channels from SAS. 

#####  Example 
         
         {
            "spectrumInquiryResponse":[
              {
                "cbsdId":"SAS-assigned device ID",
                "availableChannel":[
                  {
                    "frequencyRange":{
                      "lowFrequency":3550 - 3700 MHz (e.g. 3600000000)
                      "highFrequency":3550 - 3700 MHz
                    },
                    "channelType":"GAA",
                    "ruleApplied":"FCC_PART_96",
                    "maxEirp": 37
                  }
                ],
                "response":{
                  "responseCode":0
                }
              }
            ]
          }
           

* * *

  4. The CBSD sends a grant request to SAS.
  5. The CBSD sends a grant request for the available frequency range indicated by SAS.
  6. If desired bandwidth is available but not in a contiguous range, the CBSD sends more than one grant request for each corresponding channel.

**Important:** The CBSD sends multiple grant requests for each channel even when the bandwidth is available in a contiguous range, like 3550 MHz to 3600 MHz. Learn more about Frequency Reuse.



### Result

The expected results from the test are listed in the following table.

**Table 19.** Test case 19 | Receives | Sends  
---|---|---  
SAS | Valid grant request | Successful responses for all valid grant requests from the CBSD  
CBSD or DP | Successful grant response for all requests | Valid grant requests  
  
## Test case 20: Support for automated EIRP increase

This test case verifies the following:

  * The CBSD identifies conditions favorable for EIRP increase.
  * The CBSD is notified that an EIRP increase is available.



For more information, see [Automated EIRP increase](https://docs.cloud.google.com/spectrum-access-system/docs/operator-tips#auto-increase-eirp).

### Prerequisites

Make sure that the following is true:

  * The CBSD is registered with the `Test` SAS within a 5 kilometer radius of [68, -164.5]. The protection entity is simulated in the `Test` SAS to ensure that the EIRP available on day 1 is 6dB or more below the `eirpCapability` value of the device.
  * The CBSD is not located near the Canadian border, a Federal Communications Commission field office, Table Mountain, or in a National Radio Quiet Zone.



### Steps

Verify the following steps:

  1. The CBSD sends a spectrum inquiry to the `Test` SAS. The spectrum inquiry response shows one or more 10 MHz channels with EIRP 6dB or more below the `eirpCapability` value of the device.

  2. The CBSD requests a grant outside of the CPAS window on a frequency according to the EIRP shown in Spectrum Inquiry, which is 6dB or more below the `eirpCapability` value of the device. SAS approves the grant.

  3. The CBSD commences heartbeat and receives authorization for transmission.

  4. The CBSD heartbeat continues until CPAS occurs, as configured in the `Test` SAS.

  5. After CPAS occurs, the CBSD receives an `operationalParam` payload that denotes EIRP that's higher than the EIRP in the existing grant and with a successful response code.

#####  Example payload 
         
         {
           "heartbeatResponse": [
             {
               "cbsdId": "xy123uzt",
               "grantId": "SAS-assigned grant ID #1",
               "transmitExpireTime": "2023-08-01T17:16:51Z",
               "heartbeatInterval": 60,
               "operationParam": {
                 "maxEirp": 37,
                 "operationFrequencyRange": {
                   "lowFrequency": 3550000000,
                   "highFrequency": 3560000000} },
               "response": {
                 "responseCode": 0}
                     }
                 ]
             }
         

* * *

  6. If the CBSD decides to claim the new grant with the new EIRP value, it sends a grant relinquishment request. The `Test` SAS sends a response indicating successful relinquishment.

  7. (Optional) The CBSD sends a spectrum inquiry to check the new EIRP value. The `maxEirp` value in the spectrum inquiry response will match the `maxEirp` value in the heartbeat response from the previous step for the granted channel as long as the grant is a multiple of 10MHz. For example, 3550MHz to 3560MHz.

#####  Example response 
         
         {
           "spectrumInquiryResponse": [
             {
               "availableChannel": [
                 {
                   "channelType": "GAA",
                   "frequencyRange": {
                     "lowFrequency": 3550000000,           
                     "highFrequency": 3560000000},
                   "maxEirp": 37,
                   "ruleApplied": "FCC_PART_96"
                   }
                 ],
               "cbsdId": "xy123uzt",
               "response": {
                 "responseCode": 0
                 }
             }
           ]
         }
         

* * *

  8. The CBSD sends a grant request with the EIRP value from the heartbeat response. The `Test` SAS approves the request and sends an approval response.

#####  Example grant response 
         
         {
           "grantResponse": [
             {
               "cbsdId": "xy123uzt",
               "grantId": "SAS-assigned grant ID #1",
               "grantExpireTime": "2024-07-31T18:06:39Z",
               "heartbeatInterval": 60,
               "channelType": "GAA",
               "response": {
                 "responseCode": 0
                 }
                }
             ]
         }
         

* * *

  9. The CBSD sends a heartbeat response for the new grant and receives a successful grant response from the `Test` SAS.

#####  Example grant response 
         
         {
         "heartbeatResponse": [
           {
             "cbsdId": "xy123uzt",
             "grantId": "SAS-assigned grant ID #1",
             "transmitExpireTime": "2023-08-01T18:23:16Z",
             "heartbeatInterval": 60,
             "response": {
               "responseCode": 0
                  }
               }
              ]
            }
           

* * *




## Test case 21: Heartbeat extension outside of DPA areas

SAS suggests different heartbeat interval and `transmitExpireTime` values depending on frequencies granted and the CBSD's location. For more information on heartbeat operation, see [Send heartbeat requests for authorization to transmit](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#heartbeat).

This test case verifies the following:

  * The CBSD reads the heartbeat interval and `transmitExpireTime` values from the heartbeat response.
  * The CBSD heartbeats according to the heartbeat interval returned by SAS.
  * The CBSD continues to transmit until the `transmitExpireTime` value is reached.



### Prerequisites

To complete the steps in this test case, you must register your CBSD both inside and outside of the suspension zone in the test SAS deployment.

### Outside the suspension zone

Verify the following steps:

  1. Register the CBSD outside the suspension zone.
  2. The CBSD requests a grant.
  3. The test SAS deployment sends a heartbeat response. For example:

#####  Example payload 
         
         {
           "heartbeatResponse":[
               {
                 "cbsdId":"",
                 "grantId":"",
                 "transmitExpireTime":"current time+6 hours
                 "heartbeatInterval": 1800,
                 "response":{
                     "responseCode":0
                 },
               }
           ]
         }
         

* * *

  4. The CBSD sends the next heartbeat 1800 seconds later.




### Inside the suspension zone (grants in the 3550 MHz - 3650 MHz range)

Verify the following steps:

  1. Register the CBSD inside the suspension zone.
  2. The CBSD requests a grant within the 3550 MHz - 3650 MHz range.
  3. The test SAS deployment sends a heartbeat response. For example:

#####  Example payload 
         
         {
           "heartbeatResponse":[
               {
                 "cbsdId":"",
                 "grantId":"",
                 "transmitExpireTime":"current time+ 200 sec
                 "heartbeatInterval": 60,
                 "response":{
                     "responseCode":0
                 },
               }
           ]
         }
         

* * *

  4. The CBSD sends the next heartbeat 60 seconds later.

  5. The CBSD stops transmitting 200 seconds later unless it receives a new heartbeat response with a new `transmitExpireTime` value.




### Inside the suspension zone (grants in the 3650 MHz - 3700 MHz range)

Verify the following steps:

  1. Register the CBSD inside the suspension zone.
  2. The CBSD requests a grant within the 3650 MHz - 3700 MHz range.
  3. The test SAS deployment sends a heartbeat response. For example:

#####  Example payload 
         
         {
           "heartbeatResponse":[
         
               {
                 "cbsdId":"",
                 "grantId":"",
                 "transmitExpireTime":"current time+ 6 hours
                 "heartbeatInterval": 60,
                 "response":{
                     "responseCode":0
                 },
               }
           ]
         }
         

* * *

  4. The CBSD sends the next heartbeat 60 seconds later.

  5. The CBSD stops transmitting 6 hours later unless it receives a new heartbeat response with a new `transmitExpireTime` value.




## What's next

  * [Validate your test results with Google](https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).
  * Learn about the [PAL interoperability test suite](https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms)..



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
