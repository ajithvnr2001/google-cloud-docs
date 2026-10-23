---
url: https://docs.cloud.google.com/model-armor/model-armor-vertex-integration/
title: Integrate Model Armor with Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:10.978049+00:00
---

# Integrate Model Armor with Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/model-armor-vertex-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate Model Armor with Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Model Armor to protect Gemini models on Gemini Enterprise Agent Platform by screening prompts and responses. When integrated with Gemini Enterprise Agent Platform, Model Armor intercepts prompts before they reach Gemini models, and intercepts responses before your application receives them. Based on your configuration, Gemini Enterprise Agent Platform calls the Model Armor service, which inspects or blocks traffic that violates your defined policies—enforcing security measures like prompt injection and jailbreak detection, responsible AI filters, and Sensitive Data Protection. You can configure this integration either by using floor settings for project-level protection or by using templates for per-request protection.

Model Armor provides prompt and response protection within Gemini API in Vertex AI for the `generateContent` method. You need to enable Cloud Logging to view the sanitization results of prompts and responses.

In addition to protecting direct REST calls to the Gemini Enterprise Agent Platform service, you can also use Model Armor to protect other interfaces that provide access to the Gemini API in Vertex AI, like the [Google Generative AI SDKs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview) or [Firebase AI Logic SDKs](https://firebase.google.com/docs/ai-logic).

## Limitations

Consider the following limitations when integrating Model Armor with Gemini Enterprise Agent Platform:

  * When Model Armor uses a Sensitive Data Protection template for scanning prompts or responses, Model Armor checks if the content matches the filter criteria defined in the template. If it finds a match, Model Armor flags that the content triggered the Sensitive Data Protection filter. Although Sensitive Data Protection de-identifies the data based on the template configuration, Model Armor doesn't pass the de-identified data—such as masked, redacted, or hashed content—back to Gemini Enterprise Agent Platform for further processing. Instead, if the enforcement type is `INSPECT_AND_BLOCK`, Model Armor issues a block verdict to ensure that sensitive data doesn't proceed for further processing.
  * Sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported in this integration. To screen documents, call the [Model Armor REST API](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#file-prompts) directly.
  * If Gemini Enterprise Agent Platform routes a request to a region where the specified Model Armor template doesn't exist, the request fails with a `Template not found` error.
  * Gemini Enterprise Agent Platform skips the Model Armor sanitization step and continues processing the request under the following conditions:

    * Model Armor isn't available in a region where Gemini Enterprise Agent Platform is present.
    * Model Armor is temporarily unreachable.
    * An error occurs within Model Armor.

All these instances can occasionally expose unscreened prompts or responses because the request continues without prompt and response sanitization.

Although the integration is built for high availability during connection failures, `INSPECT_AND_BLOCK` mode will still report configuration errors, such as permission or quota issues.




## Before you begin

  * Grant the [Model Armor User role](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) to the Gemini Enterprise Agent Platform service account.
        
        gcloud projects add-iam-policy-binding PROJECT_ID --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com' --role='roles/modelarmor.user'

Replace the following:

    * `PROJECT_ID`: your Google Cloud project ID.
    * `PROJECT_NUMBER`: your Google Cloud project number.
  * Enable the [Model Armor API](https://docs.cloud.google.com/model-armor/manage-templates#enable-apis).

  * [Set the API endpoint override using the gcloud CLI](https://docs.cloud.google.com/model-armor/manage-templates#gcloud-override).




## Configure how Model Armor helps protect Gemini Enterprise Agent Platform

You can configure how Model Armor protects Gemini Enterprise Agent Platform in one of two ways:

  * **Use templates for per-request protection** : This approach provides granular control by letting you apply a specific template to each `generateContent` API call to Gemini models on Gemini Enterprise Agent Platform.
  * **Use floor settings for project-level protection** : This approach enforces a baseline protection by applying floor settings to all `generateContent` API calls to Gemini models on Gemini Enterprise Agent Platform within your project.



Define the [enforcement type](https://docs.cloud.google.com/model-armor/overview#define-enforcement-type) to determine whether violations are only inspected or also blocked.

### Per-request configuration using templates

Templates let you configure how Model Armor screens prompts and responses and define security filter configurations. You must create templates first, and then use these templates with the `generateContent` method of Gemini. For more information about templates, see [Create and manage Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates).

After configuring the Model Armor template, pass the template ID as a parameter when making a call to the Gemini API using the `generateContent` method. Gemini Enterprise Agent Platform routes the request to Model Armor for processing.

To apply specific templates to an individual `generateContent` call, include the `modelArmorConfig` object in your request.

  * `promptTemplateName`: The resource name of the Model Armor template to sanitize the prompt.
  * `responseTemplateName`: The resource name of the Model Armor template to sanitize the response.



The following code sample shows the request to the `generateContent` method.
    
    
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/gemini-2.0-flash-001:generateContent" -d '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "[YOUR PROMPT HERE]"
                }
            ]
        }
    ]
    , "generationConfig": {
        "responseModalities": ["TEXT"]
        ,"temperature": 0.2
        ,"maxOutputTokens": 1024
        ,"topP": 0.8
    },
     "model_armor_config": {
            "prompt_template_name": "projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID",
            "response_template_name": "projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID"
            }
    }'

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the Google Cloud location of the Gemini endpoint. The supported locations are `europe-west1`, `europe-west2`, `europe-west3`, `asia-southeast1`, and `asia-south1`.
  * `TEMPLATE_ID`: Model Armor template ID.



The following code sample shows the response from the `generateContent` method.
    
    
    {
      "promptFeedback": {
        "blockReason": "MODEL_ARMOR",
        "blockReasonMessage": "Blocked by Floor Setting. The prompt violated Responsible AI Safety settings (Harassment, Dangerous), Prompt Injection and Jailbreak filters."
      },
      "usageMetadata": {
        "trafficType": "ON_DEMAND"
      },
      "modelVersion": "gemini-2.0-flash-001",
      "createTime": "2025-03-26T13:14:36.961184Z",
      "responseId": "vP3jZ6DVOqLKnvgPqZL-8Ao"
    }

#### Define the enforcement type for templates

To configure how Model Armor handles detections, set the [enforcement type](https://docs.cloud.google.com/model-armor/overview#define-enforcement-type).

The following example shows the Model Armor template configuration with the `Inspect only` enforcement type.
    
    
    export TEMPLATE_CONFIG='{
       "filter_config": {
        "rai_settings": {
         "rai_filters": [{
           "filter_type": "HATE_SPEECH",
           "confidence_level": "MEDIUM_AND_ABOVE"
          }, {
          "filter_type": "HARASSMENT",
          "confidence_level": "MEDIUM_AND_ABOVE"
        }, {
          "filter_type": "DANGEROUS",
          "confidence_level": "MEDIUM_AND_ABOVE"
        },{
          "filter_type": "SEXUALLY_EXPLICIT",
          "confidence_level": "MEDIUM_AND_ABOVE"
        }]
      },
      "pi_and_jailbreak_filter_settings": {
        "filter_enforcement": "ENABLED",
        "confidence_level": "LOW_AND_ABOVE"
      },
      "malicious_uri_filter_settings": {
        "filter_enforcement": "ENABLED"
      }
     },
     "template_metadata": {
        "enforcement_type": "INSPECT_ONLY",
        "multi_language_detection": {
          "enable_multi_language_detection": true
        }
      }
    }'
    
    curl -X POST \
        -d "$TEMPLATE_CONFIG"  \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates?template_id=TEMPLATE_ID"

Replace the following:

  * `PROJECT_ID`: the ID of the project that the template belongs to.
  * `TEMPLATE_ID`: the ID of the template to be created.
  * `LOCATION`: the [location](https://docs.cloud.google.com/model-armor/locations) of the template.



### Project-level configuration using floor settings

Floor settings define a minimum baseline of protection that applies to all Gemini Enterprise Agent Platform `generateContent` calls within a project even if the `modelArmorConfig` parameter is omitted from the API request. For instructions on how to set up floor settings, see [Configure floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

Floor settings use the `Stable` [filter version](https://docs.cloud.google.com/model-armor/set-filter-version) by default. If you want to override this setting, specify a template in the `generateContent` call to the Gemini model. For more information, see [Override the default filter version for floor settings](https://docs.cloud.google.com/model-armor/set-filter-version#floor-settings-behavior).

To enable Model Armor and Gemini Enterprise Agent Platform integration, set floor settings only at the project level using the API or the Google Cloud console.

To configure floor settings with Gemini Enterprise Agent Platform integration, run the following command:

### gcloud
    
    
    gcloud model-armor floorsettings update \
      --full-uri=projects/PROJECT_ID/locations/global/floorSetting \
      --add-integrated-services=VERTEX_AI

This command enables the `INSPECT_ONLY` enforcement mode by default. To change the mode to `INSPECT_AND_BLOCK`, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri=projects/PROJECT_ID/locations/global/floorSetting \
      --vertex-ai-enforcement-type=INSPECT_AND_BLOCK

To remove Gemini Enterprise Agent Platform from the integrated services, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri=projects/PROJECT_ID/locations/global/floorSetting \
      --remove-integrated-services=VERTEX_AI

To remove all configured integrated services from the floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri=projects/PROJECT_ID/locations/global/floorSetting \
      --clear-integrated-services

Replace `PROJECT_ID` with the ID of the project for the floor settings.

### REST
    
    
    curl -X PATCH \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -d '{"filterConfig" : {"piAndJailbreakFilterSettings": { "filterEnforcement": "ENABLED"}}, "integratedServices": ["AI_PLATFORM"], "aiPlatformFloorSetting":{"inspectOnly":true, "enableCloudLogging":true}, "enableFloorSettingEnforcement":true}' \
      "https://modelarmor.googleapis.com/v1/projects/PROJECT_ID/locations/global/floorSetting"

Replace `PROJECT_ID` with the ID of the project that contains the floor settings.

After configuring the floor settings to enable Gemini Enterprise Agent Platform sanitization, Model Armor sanitizes all `generateContent` API calls to the project's Gemini endpoints using the filter settings specified.

The following code sample shows how to use the `generateContent` method.
    
    
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/gemini-2.5-flash:generateContent" -d '{
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/gemini-2.5-flash:generateContent" -d '{
    "contents": [
      {
          "role": "user",
          "parts": [
              {
                  "text": ""
              }
          ]
      }
    ]
    , "generationConfig": {
      "responseModalities": ["TEXT"]
      ,"temperature": 0.2
      ,"maxOutputTokens": 1024
      ,"topP": 0.8
    }
    }'

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the Google Cloud location of the Gemini endpoint. For supported locations, see [Locations for the Model Armor API](https://docs.cloud.google.com/model-armor/locations).



The following code sample shows the response from the `generateContent` method.
    
    
    {
    "promptFeedback": {
      "blockReason": "MODEL_ARMOR",
      "blockReasonMessage": "Blocked by Floor Setting. The prompt violated
      Responsible AI Safety settings (Harassment, Dangerous), Prompt Injection
      and Jailbreak filters."
    },
    "usageMetadata": {
      "trafficType": "ON_DEMAND"
    },
    "modelVersion": "gemini-2.5-flash",
    "createTime": "2025-03-26T13:14:36.961184Z",
    "responseId": "vP3jZ6DVOqLKnvgPqZL-8Ao"
    }

#### Define the enforcement type for floor settings

To configure how Model Armor handles detections, set the [enforcement type](https://docs.cloud.google.com/model-armor/overview#define-enforcement-type) to either `INSPECT` or `INSPECT_AND_BLOCK`. The following example shows the floor settings configuration with the `INSPECT_AND_BLOCK` enforcement type.

### gcloud
    
    
    gcloud model-armor floorsettings update \
      --full-uri=projects/modelarmor-api-test/locations/global/floorSetting \
      --vertex-ai-enforcement-type=INSPECT_AND_BLOCK

### REST
    
    
    export FLOOR_SETTING='{
      "filterConfig": {
        "raiSettings": {
          "raiFilters": [
            { "filterType": "HATE_SPEECH", "confidenceLevel": "LOW_AND_ABOVE" },
            { "filterType": "DANGEROUS", "confidenceLevel": "LOW_AND_ABOVE" },
            { "filterType": "SEXUALLY_EXPLICIT", "confidenceLevel": "LOW_AND_ABOVE" },
            { "filterType": "HARASSMENT", "confidenceLevel": "LOW_AND_ABOVE" }
          ]
        },
        "sdpSettings": {
          "basicConfig": { "filterEnforcement": "ENABLED" }
        },
        "piAndJailbreakFilterSettings": {
          "filterEnforcement": "ENABLED",
          "confidenceLevel": "LOW_AND_ABOVE"
        },
        "maliciousUriFilterSettings": { "filterEnforcement": "ENABLED" }
      },
      "integratedServices": ["AI_PLATFORM"],
      "aiPlatformFloorSetting": {
        "inspectAndBlock": true,
        "enableCloudLogging": true
      },
      "enableFloorSettingEnforcement": true
    }'
    
    curl -X PATCH \
        -d "$FLOOR_SETTING" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://modelarmor.googleapis.com/v1/projects/PROJECT_ID/locations/global/floorSetting"

Replace the following:

  * `PROJECT_ID`: the ID of the project for the floor settings.
  * `LOCATION`: the [location](https://docs.cloud.google.com/model-armor/locations) of the floor settings.



#### Test inline enforcement with an API call

Test the integration to call the Gemini Enterprise Agent Platform API's `generateContent` method. Use a prompt that is designed to violate the configured floor settings.
    
    
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://${VERTEX_AI_LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${VERTEX_AI_LOCATION}/publishers/google/models/gemini-2.5-flash:generateContent" -d '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": ""
                }
            ]
        }
    ]
    , "generationConfig": {
        "responseModalities": ["TEXT"]
        ,"temperature": 0.2
        ,"maxOutputTokens": 1024
        ,"topP": 0.8
    }
    }'

If the integration is working as expected, the API returns a response with the `blockReason` field set to `MODEL_ARMOR` when Model Armor identifies the prompt as a violation.

A sample response is as follows:
    
    
        {
        "promptFeedback": {
          "blockReason": "MODEL_ARMOR",
          "blockReasonMessage": "Blocked by Floor Setting. The prompt violated Responsible AI Safety settings..."
        },
        "usageMetadata": { "trafficType": "ON_DEMAND" },
        "modelVersion": "gemini-2.5-flash"
        }
    

## Interaction and precedence rules

When using Model Armor with Gemini Enterprise Agent Platform, you can define safety configurations at multiple levels. In such cases, Model Armor and Gemini Enterprise Agent Platform follow a specific order of precedence:

  1. **Model Armor templates** : Any configuration explicitly provided in the API request configuration have the highest precedence. These settings override any other conflicting configurations for that specific request.

  2. **Model Armor floor settings** : If no overriding configuration is provided in the API request, Model Armor floor settings apply.

  3. **Gemini Enterprise Agent Platform safety filters** : The default safety filters built into Gemini Enterprise Agent Platform have the lowest precedence. They apply only if you don't define specific Model Armor templates or floor settings.




This hierarchical approach provides a combination of broad, organization-wide minimum standards (using floor settings) and per-request control (using templates), while still using Gemini Enterprise Agent Platform's inherent safety features as a baseline.

The behavior of Model Armor and Gemini Enterprise Agent Platform safety features depends on how you provide the configuration.

Template configured? | Gemini Enterprise Agent Platform safety filters configured? | Floor settings configured? | Behavior  
---|---|---|---  
Yes | Yes | Any | You get an error. You cannot specify both template configuration and Gemini Enterprise Agent Platform safety filters in the same request.  
Yes | No | Any | Model Armor runs, using the templates specified in `modelArmorConfig`. Gemini Enterprise Agent Platform safety filters are ignored. Request templates override floor settings.  
No | Yes | Yes | Both run. Model Armor scans using the floor setting policy, and Gemini Enterprise Agent Platform evaluates its safety filters. The most restrictive outcome is applied.  
No | No | Yes | Model Armor runs, using the active floor setting policy.  
No | Yes | No | Only Gemini Enterprise Agent Platform safety filters are evaluated. Model Armor isn't called.  
No | No | No | Neither per-request Model Armor nor Gemini Enterprise Agent Platform safety filters are applied. Only baseline model behaviors are active.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
