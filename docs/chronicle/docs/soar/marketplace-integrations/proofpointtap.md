---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpointtap/
title: Integrate Proofpoint TAP with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:48.116206+00:00
---

# Integrate Proofpoint TAP with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpointtap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Proofpoint TAP with Google SecOps

This document explains how to integrate Proofpoint TAP with Google Security Operations (Google SecOps).

### Integration parameters

The Proofpoint TAP integration requires the following parameters:

Parameter | Description  
---|---  
API Root | Required. The API root of the Proofpoint Targeted Attack Protection (TAP) instance.  
Username | Required. The username of the Proofpoint TAP instance. Important: In the Proofpoint TAP account, Username is the **Service Principal Name**.   
Password | Required. The API Key of the Proofpoint TAP instance. Important: In the Proofpoint TAP account, Password is the **API Key**.   
Verify SSL | Optional. If enabled, that action verifies the validity of the SSL certificate.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### DecodeURL

Use the **DecodeURL** action to decode Proofpoint's encoded URLs.

This action runs on the following Google SecOps entity:

  * `URL`



#### Action inputs

Parameter | Description  
---|---  
Encoded URLs | Optional. A comma-separated list of URLs to decode. Note: URL entities in the scope of the alert will be decoded together.  
Create URL Entities | Optional. If selected, the action creates a URL entity from the URL after it has been successfully decoded. The default value is `Checked`.  
  
#### Action outputs

The **DecodeURL** action provides the following outputs.

##### Entity Enrichment

The **DecodeURL** action supports the following entity enrichment logic:

Enrichment Field Name | Logic - When to apply  
---|---  
Encoded Urls | A comma-separated list of URLs to decode. Note: URL entities in the scope of the alert will be decoded together.  
Create URL Entities | If selected, the action creates a successfully-decoded URL entity from the URL after it has been successfully decoded. The default value is `Checked`.  
  
##### Script Result

The following table describes the values for the script result output when using the **DecodeURL** action:

Script Result Name | Value Options | Example  
---|---|---  
decoded_urls | N/A | N/A  
  
### GetCampaign

Use the **GetCampaign** action to get campaign information by the campaign ID.

This action runs on all entities.

#### Action inputs

The **GetCampaign** action requires the following parameter:

Parameter | Description  
---|---  
Campaign ID | Required. The ID of the campaign to get information about.  
Create Insight | Optional. If selected, the action creates an insight with the campaign information. Selected by default  
Create Threat Campaign Entity | Optional. If selected, the action creates a threat campaign entity from the campaign information. Selected by default  
Fetch Forensics Info | Optional. If selected, the action fetches forensics information from the campaign. Selected by default  
Forensic Evidence Type Filter | Optional. A comma-separated list of evidence types to return when fetching forensic info. Possible values: `attachment`, `cookie`, `dns`, `dropper`, `file`, `ids`, `mutex`, `network`, `process`, `registry`, `screenshot`, `url`, `redirect_chain`, `behavior`.  
Max Forensics Evidence To Return | Optional. The amount of evidence to return per campaign. The default value is `50`. The maximum value is `1000`.  
  
#### Action outputs

The **GetCampaign** action provides the following outputs.

##### Script Result

The following table describes the values for the script result output when using the **GetCampaign** action:

Script Result Name | Value Options | Example  
---|---|---  
campaign_info | N/A | N/A  
  
### Ping

Use the **Ping** action to test Proofpoint TAP connectivity.

This action runs on all entities.

#### Action inputs

The **Ping** action doesn't require any parameters.

#### Action outputs

The **Ping** action provides the following outputs.

##### Script Result

The following table describes the values for the script result output when using the **Ping** action:

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
