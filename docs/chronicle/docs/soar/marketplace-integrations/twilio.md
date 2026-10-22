---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/twilio/
title: Twilio \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:40.557608+00:00
---

# Twilio  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/twilio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Twilio

This document provides guidance on how to integrate Twilio with Google SecOps.

## Configure Twilio to work with Google Security Operations

  1. Log into your [Twilio account](https://www.twilio.com/login).

  2. In the Twilio Console, navigate to the **Settings** > **API Keys.**

  3. Select **Create new API Key** and choose to create either Standard or Master API Key.

  4. You will find your Account SID and API Credentials containing _Auth Token_ in the **Settings** > **General**.


**Note:** For more information about API Credentials, see [API Key](https://www.twilio.com/docs/glossary/what-is-an-api-key).

## Configure Twilio integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Account sid | String | N/A | Yes | The ID of your Twilio Account.  
Authentication token | String | N/A | Yes | Twilio token used for authentication.  
SMS phone number | String | N/A | Yes | Your Twilio phone number that can be generated in the Twilio console.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please refer [here](https://www.manula.com/manuals/siemplify/how-to/5.5.0/en/topic/supporting-multiple-instances).

## Actions

### Ping

#### Description

Verify that the user has a connection to Twilio via the user's device.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

If the connection is established, Script result will be True. Else: False.

##### JSON Result
    
    
    N/A
    

### Send SMS

#### Description

By using Twilio's REST API, outgoing SMS messages can be sent from specific Twilio phone numbers to mobile phones worldwide. If multiple messages are sent at once from a single Twilio sender (number or Alphanumeric Sender ID), Twilio will queue them up for delivery.

#### Parameters

Parameter Display Name | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Phone Number | String | N/A | Yes | Target phone number.The phone number must include a dial code.  
Message | String | Testing | Yes | Message content.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Send SMS and Wait

#### Description

The message will be sent with a generated Google SecOps ID: `<code>`. The action will wait for a response containing Google SecOps ID: `<code>`. This action has the role of sending SMS and waiting for a response to a previously sent SMS message. This action also enables multiple send/wait for reply actions within a single trigger allowing constructing automated SMS text conversations and performing different actions based on the reply results.

#### Parameters

Parameter Display Name | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Phone Number | String | N/A | Yes | Target phone number. The phone number must include a dial code.  
Message | String | N/A | Yes | Message content.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
