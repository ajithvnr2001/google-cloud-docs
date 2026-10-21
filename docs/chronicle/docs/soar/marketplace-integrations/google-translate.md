---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-translate/
title: Integrate Google Translate with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:37:36.059630+00:00
---

# Integrate Google Translate with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-translate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Translate with Google SecOps

This document explains how to configure and integrate Google Translate with Google Security Operations (Google SecOps).

## Before you begin

To use the integration, you need to create and configure an API key.

### Create the API key

To create the API key, complete the following steps:

  1. In the Google Cloud console, go to **APIs & Services > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **add Create credentials**.

  3. Select **API key** to generate a new API key. A dialog appears with a generated API key.

  4. To copy the API key, click **content_copy Copy**.




### Configure the API key restrictions

To configure the API restriction for the API key, complete the following steps:

  1. Click **Restrict key**.

  2. Under **API restrictions** , select **Restrict key**.

  3. Select **Cloud Translation API** from the API list.

  4. Configure the applicable restrictions.

  5. Click **Save** to save the API key configuration.




## Integration parameters

The Google Translate integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required.The API root of the Google Translate instance.The default value is `https://translation.googleapis.com`.For more information about Cloud Translation API, see [ Cloud Translation API](https://docs.cloud.google.com/translate/docs/reference/rest).  
`API Key` | Required.The API key of the Google Translate account.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the Google Translate server. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### List Languages

Use the **List Languages** action to list available languages in Google Translate.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Languages** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | Optional.A key to filter languages.The possible values are as follows:

  * `Select One`
  * `Name`

The default value is `Select One`.  
`Filter Logic` | Optional.A filter logic to apply.The filtering logic uses the value that you set in the `Filter Key` parameter. The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | Optional.A value to use in the filter.The filtering logic uses the value that you set in the `Filter Key` parameter.If `Equal` is selected, the action searches for the exact match among results. If `Contains` is selected, the action searches for results that contain the specified substring. If you don't select a value, the action ignores the filter. Filtering logic is working based on the value provided in the `Filter Key` parameter.  
`Max Records To Return` | Optional.The maximum number of records to return.The maximum value is `50`.If you don't set a value, the action returns 50 records by default.  
  
#### Action outputs

The **List Languages** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Languages** action can generate the following table:

Table name: **Available Languages**

Table column: **Language Key**

##### JSON result

The following example shows the JSON result output received when using the **List Languages** action:
    
    
    {
        "data": {
            "languages": [
                {
                    "language": "af"
                },
                {
                    "language": "am"
                },
                {
                    "language": "ar"
                }
    
            ]
        }
    }
    

##### Output messages

The **List Languages** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found language for the provided criteria in Google Translate.` `No languages were found for the provided criteria in Google Translate.` `The filter was not applied, because parameter "Filter Value" has an empty value.` | The action succeeded.  
`Error executing action "List Languages". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Languages** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Google Translate.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Translate server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Translate server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Translate Text

Use the **Translate Text** action to translate text with Google Translate.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Translate Text** action requires the following parameters:

Parameter | Description  
---|---  
`Source Language` | Optional.A source language of the text.If you don't configure this parameter, the action detects the language automatically.  
`Target Language` | Required.A target language.The default value is `en`.  
`Text` | Required.A text to translate.  
  
#### Action outputs

The **Translate Text** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Translate Text** action:
    
    
    {
        "data": {
            "translations": [
                {
                    "translatedText": "TRANSLATED_TEXT"
                }
            ]
        }
    }
    

##### Output messages

The **Translate Text** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully translated the provided text in Google Translate.` | The action succeeded.  
`Error executing action "Translate Text". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Translate Text** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
