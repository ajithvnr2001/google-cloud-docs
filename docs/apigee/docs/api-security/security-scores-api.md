---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-scores-api/
title: Security scores and profiles API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:52.058467+00:00
---

# Security scores and profiles API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-scores-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security scores and profiles API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Overview

This page describes how to manage Risk Assessment security scores and security profiles (also referred to simply as "profiles") using APIs. This page presents example API requests.

**Note** : The APIs for Risk Assessment v1 and v2 have separate data and APIs. The APIs from one cannot be used to query the other. For example, Risk Assessment v1 APIs cannot be used to query Risk Assessment v2 data.

For an overview of the Risk Assessment functionality, including limitations, and instructions for using the UI, see [Risk assessment overview and UI](https://docs.cloud.google.com/apigee/docs/api-security/security-scores).

## Risk Assessment v2 API Examples

**Preview — Risk Assessment v2**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

### Parameters for v2 API examples

The examples in this section can use these parameters:

  * ORG is your organization.
  * ENV is the environment in which you want scores to be calculated.
  * PROFILE_ID is the name of the profile. PROFILE_ID can be `google-default` or the name of a custom profile that you create.
  * PROFILE_DESC (optional) is the description for the profile. This should be a human-readable description of the profile that provides enough information to differentiate it from other profiles.
  * PROXY_NAME: The name of the proxy.
  * RESOURCES can be: 
    * `"include_all_resources":{}` to monitor all resources within the scope.
    * `"include": { "resources": [{"type": "API_PROXY", "name": "PROXY_NAME"}]}` to monitor one or more specified proxies. For example, `"include": { "resources": [{"type": "API_PROXY", "name": "my-proxy-1"}]}` to monitor the proxy called `my-proxy-1`.
  * SECURITY_MONITORING_CONDITION_ID: The unique ID of the security monitoring condition. If no ID is provided, a UUID is generated automatically.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). 



### Retrieve batch security assessment results

Users with the `Security Admin` or `Security Viewer` roles have permissions to perform an ad hoc risk assessment computation. You'll need to specify the security profile, scope (the Apigee environment), and resources to be assessed. Resources could be `include_all_resources: true` to compute on all resources within the scope, or only a handful. See [securityAssessmentResults.batchCompute](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityAssessmentResults/batchCompute) in the Apigee Management API reference documentation for more information on this functionality.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityAssessmentResults:batchCompute" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-type: application/json' \
           -d '{
               "profile": "PROFILE_ID",
               "scope": "ENV",
               RESOURCES
      }'

This is a potential response for the request:
    
    
    {
      "securityAssessmentResults": [
        {
          "resource": {
            "type": "API_PROXY",
            "name": "my-proxy-1",
            "resourceRevisionId": "1"
          },
          "createTime": "2023-11-22T04:49:29.418166Z",
          "scoringResult": {
            "severity": "HIGH",
            "failedAssessmentPerWeight": {
              "MINOR": 1
            },
            "assessmentRecommendations": {
              "cors-policies-check": {
                "displayName": "CORS policies check",
                "weight": "MAJOR",
                "recommendations": [
                  {
                    "description": "Check whether a CORS policy or CORS header in AssignMessage policy are present.",
                    "link": {
                      "text": "Learn more",
                      "uri": "https://cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy"
                    }
                  }
                ],
                "verdict": "FAIL",
                "scoreImpact": 100
              }
            },
            "dataUpdateTime": "2023-11-22T04:49:29.418166Z"
          }
        }
      ],
      "assessmentTime": "2023-11-22T04:49:29.418166Z"
    }

### Manage security profiles

This section provides examples for managing security profiles using the APIs and is not exhaustive. See the [securityProfilesV2 API reference docs](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2) for more information.

#### Get existing custom security profiles

This command retrieves the information for all security profiles for your project:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfilesV2" \
          -H "Authorization: Bearer $TOKEN"

This command retrieves the metadata for a specific security profile and can be used to retrieve information on the `google-default` profile as well as custom profiles:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfilesV2/PROFILE_ID" \
          -H "Authorization: Bearer $TOKEN"

#### Create a new custom security profile

To create a new custom security profile, use a command like this:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfilesV2?security_profile_v2_id=PROFILE_ID" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-type: application/json' \
           -d '{
               "description": "PROFILE_DESC",
               "risk_assessment_type": "APIGEE",
               "profile_assessment_configs": {
                   "auth-policies-check": {"weight": "MINOR"},
                   "threat-policies-check": {"weight": "MODERATE"}
               }
            }'

#### Update an existing custom security profile

To update an existing profile, use a command like:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfilesV2/PROFILE_ID?update_mask=UPDATE_MASK" \
           -X PATCH \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-type: application/json' \
           -d '{"description": "PROFILE_DESC"}'

where UPDATE_MASK can be one of these values, if present: `description`, `profile_assessment_configs`, `description,profile_assessment_configs`, or `*` (everything). If specifying the `*` update mask, the request updates all fields, which could remove values if they are not included in the request.  
  
Omitting `update_mask` updates only the fields provided in the update request.

#### Delete a custom security profile

The delete a custom security profile:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfilesV2/PROFILE_ID" \
           -X DELETE \
           -H "Authorization: Bearer $TOKEN"

### Manage monitoring conditions

This section provides examples for managing monitoring conditions using the APIs and is not exhaustive. See the [monitoring conditions API reference docs](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2.securityMonitoringConditions) for more information on managing monitoring conditions through the APIs.

#### Create a new monitoring condition

To create a new monitoring condition, use a command like this:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions?security_monitoring_condition_id=MONITORING_CONDITION_ID" \
           -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{
               "profile": "PROFILE_ID",
               "scope": "ENV",
               RESOURCES
           }'

The response could look like:
    
    
    {
      "name": "organizations/my-org/securityMonitoringConditions/my-condition",
      "createTime": "2025-11-22T05:02:16.089469Z",
      "updateTime": "2023-11-22T05:02:16.089469Z",
      "profile": "google-default",
      "scope": "test",
      "totalMonitoredResources": 4,
      "totalDeployedResources": 4,
      "includeAllResources": {}
    }

#### List monitoring conditions

To get a list of monitoring conditions in your organization, use a command like this:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions"

The response is in this form:
    
    
    {
      "securityMonitoringConditions": [
        {
          "name": "organizations/my-org/securityMonitoringConditions/my-condition",
          "createTime": "2023-11-22T05:02:16.089469Z",
          "updateTime": "2025-11-22T05:02:16.089469Z",
          "profile": "google-default",
          "scope": "test",
          "totalMonitoredResources": 4,
          "totalDeployedResources": 4,
          "includeAllResources": {}
        }
      ]
    }

You could also use this syntax to limit the returned results by scope or security profile:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions?filter=scope=ENV%20AND%20profile=PROFILE_ID"

#### Get an existing monitoring condition

To get the information for an existing monitoring condition, use a command like this:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions/MONITORING_CONDITION_ID"

The response is in this form:
    
    
    {
      "name": "organizations/my-org/securityMonitoringConditions/my-condition",
      "createTime": "2023-11-22T05:02:16.089469Z",
      "updateTime": "2025-11-22T05:02:16.089469Z",
      "profile": "google-default",
      "scope": "test",
      "totalMonitoredResources": 4,
      "totalDeployedResources": 4,
      "includeAllResources": {}
    }

#### Update an existing monitoring condition

This command updates the profile for an existing monitoring condition:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions/MONITORING_CONDITION_ID?update_mask=CONDITION_UPDATE_MASK" -X PATCH -H "Content-Type: application/json" \
           -d  '{
           RESOURCES
      }'

where `update_mask` is optional. If included, CONDITION_UPDATE_MASK can be `include` or `include_all_resources`. Omitting `update_mask` updates only the fields provided in the update request.

The response might look like:
    
    
    {
      "name": "test-condition",
      "createTime": "2023-11-22T03:04:05Z",
      "updateTime": "2023-11-22T03:04:05Z",
      "profile": "google-default",
      "scope": "test",
      "include": {
        "resources": [{
          "type": "API_PROXY", "name": "PROXY_NAME"
        }]
      }
    }

#### Delete a monitoring condition

This command deletes an existing monitoring condition:

**Important:** Deleting a monitoring condition in Apigee does not delete the metrics tracking for that monitoring condition in Cloud Monitoring. See [Disable collection of metrics](https://docs.cloud.google.com/monitoring/settings/disable) for instructions on deleting the Cloud Monitoring metrics.
    
    
    curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG/securityMonitoringConditions/MONITORING_CONDITION_ID" \
           -X DELETE

## Risk Assessment v1

This section shows information and examples for Risk Assessment v1 APIs.

### Limitations on security scores when using the APIs

Security scores have the following limitations when used from the security scores and profiles APIs:

  * Supported input fields in JSON: 
    * `timeRange`: Values are limited by the criteria described in the [computEnvironmentScores API reference](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/computeEnvironmentScores). 
    * `filters`: See Filters supported in the API.
    * `pageSize`: Maximum number of subcomponents to be returned in a single page: 100.
  * Multiple input filters are not supported.
  * Impact field in response is not supported. (Impact field is the potential impact of this recommendation on the overall score. This denotes how important this recommendation is to improve the score.)



For general security score limitations not specific to use from the APIs, see [Limitations on security scores v1](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#limitations-on-security-scores-v1).

### Parameters in example API calls

The following sections provide example API calls and can use the following parameters:

  * ORG is your organization.
  * ENV is the environment in which you want scores to be calculated.
  * ENVGROUP is an environment group containing the environment.
  * PROFILE_ID is the name of the profile. PROFILE_ID can be `default` or the name of a custom profile that you create. 

PROFILE_ID must contain from 1 to 63 characters, which can be lower case letters, numbers 0-9, or hyphens. The first character must be a lower case letter. The last character must be a lower case letter or number.

  * PROXY_NAME: The name of the proxy.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). 
  * `timeRange` is the [time range](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/computeEnvironmentScores#request-body) for the scores.



### Risk Assessment v1 API Examples

#### Filters supported in the API

The following table lists the filters that are supported in the API, and their component paths.

Filter | Component path | Environment scores | `/org@ORG/envgroup@ENVGROUP/env@ENV`  
---|---  
Source scores all underlying components | `/org@ORG/envgroup@ENVGROUP/env@ENV/source`  
Abuse scores | `/org@ORG/envgroup@ENVGROUP/env@ENV/source/abuse`  
Scores for all proxies | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies`  
Scores for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME`  
Policy scores for specific proxy | 

  * `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies`
  * `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual`

  
Mediation policy scores for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual/mediation`  
Security policy scores for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual/security`  
Auth policy scores for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual/security/auth`  
CORS policy score for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual/security/cors`  
Threat policy scores for specific proxy | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY_NAME/policies/individual/security/threat`  
Policy scores for all proxies in the env | 

  * `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies`
  * `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual`

  
Mediation policy scores for all proxies in the env | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/mediation`  
Security policy scores for all proxies in the env | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security`  
Auth policy scores for all proxies in the env | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/auth`  
CORS policy scores for all proxies in the env | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/cors`  
Threat policy scores for all proxies in the env | `/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/threat`  
  
#### Use the default security profile

The following examples show how to use the [default security profile](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#default-security-profile-v1). See Parameters in example API calls for the parameters used in the examples.

##### Attach the default security profile to an environment

To view security scores, you need to attach a profile to the environment whose security you want to evaluate. To attach the default [security profile](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#default-security-profile-v1) to an environment, use the following command:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/default/environments" \
           -X POST \
           -d '{"name": "ENV"}' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

**Note:** The parameter `securityProfileRevisionId` has been deprecated. If you include this parameter in an API call, Advanced API Security will use the latest revision of the profile, regardless of the value of the parameter.

##### Get the default security profile definition

To get the definition of the default security profile, enter the following command:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/default" \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

#### Detach the default security profile from an environment

If you need to detach the default profile from an environment, you can do so as follows:
    
    
      curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/default/environments/ENV" \
             -X DELETE
             -H 'Content-type: application/json' \
             -H "Authorization: Bearer $TOKEN"

#### Use a custom security profile

**Preview — Advanced API Security Custom Profiles**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Custom Profiles is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum. 

You can create a [ custom security profile](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#custom-security-profile) with an API call in either of the following ways:

  * Explicitly define the profile in the body of the call.
  * Attach a JSON file that contains the profile definition to the call.



The following sections give examples of both methods. See Parameters in example API calls for the parameters used in the examples.

The following fields in the example API calls specify the custom profile:

  * `description`: A description of the custom profile.
  * `profileConfig`: A list of the categories to include in the custom profile. This can be any subset of the following [security categories](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#security-categories): 
    * `abuse`
    * `authorization`
    * `cors`
    * `mtls`
    * `mediation`
    * `threat`



##### Define the profile in the body of an API call

To define a custom profile in the body of an API call, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles?security_profile_id=PROFILE_ID" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{
             "description":"test custom profile",
             "profileConfig" : {
               "categories":[
                 {"cors":{}},
                 {"threat":{}}
               ]
             }
           }'

This creates a custom profile that includes the categories cors and threat, and returns a response like this:
    
    
    {
      "name": "PROFILE_ID",
      "revisionId": "1",
      "revisionCreateTime": "2023-07-17T18:47:08Z",
      "revisionUpdateTime": "2023-07-17T18:47:08Z",
      "scoringConfigs": [
        {
          "title": "json",
          "scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/threat/json",
          "description": "Check if JSONThreatProtection policy is configured."
        },
        {
          "title": "xml",
          "scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/threat/xml",
          "description": "Check if XMLThreatProtection policy is configured."
        },
        {
          "title": "cors",
          "scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@$proxy/policies/individual/security/cors",
          "description": "Check if CORS policy is configured."
        }
      ],
      "maxScore": 1200,
      "minScore": 200,
      "profileConfig": {
        "categories": [
          {
            "cors": {}
          },
          {
            "threat": {}
          }
        ]
      },
      "description": "test custom profile"
      }

##### Define the profile by attaching a JSON file to an API call

You can also define a custom security profile by attaching a JSON file that defines the profile to an API call. As an example, first create the following JSON file:
    
    
    {
      "description": "test custom profile",
      "profileConfig" : {
        "categories":[
          {"cors":{}},
          {"threat" :{}},
        ]
      }
    }

This defines a profile with categories cors and threat. You can then create a profile based on these categories as follows:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles?security_profile_id=PROFILE_ID" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d @create_profile.json

where `create_profile.json` is the name of the JSON file described above.

##### Get a custom security profile definition

To get the definition of a custom security profile, enter a command similar to the following:
    
    
      curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID" \
             -X GET \
             -H "Authorization: Bearer $TOKEN" \
             -H "Content-Type: application/json"

##### Detach a custom security profile from an environment

To detach a custom security profile from an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV" \
           -X DELETE \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json"

##### Delete a custom security profile

To delete a custom security profile, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID" \
           -X DELETE \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json"

**Note:** If you delete a custom security profile, you will lose all scores related to the profile, and all environments attached to the profile will be automatically detached.

#### Get scores for an environment

The following sections present examples of getting scores for an environment. See Parameters in example API calls for the parameters used in the examples. 

##### Get all scores for an environment

To get all scores for an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  }
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

See the [ `computeEnvironmentScores`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/computeEnvironmentScores) reference page for a description of the request and response.

##### Get source scores for an environment

To get source scores for an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  },
                "filters": [{"scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/source"}]
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

##### Get abuse score in source for an environment

To get the abuse score in source for an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  },
                "filters": [{"scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/source/abuse"}]
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

##### Get scores for all proxies in an environment

To get scores for all proxies in an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  },
                "filters": [{"scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/proxies"}]
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

##### Get scores for a specific proxy in an environment

To get scores for a specific proxy in an environment, enter command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  },
                "filters": [{"scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/proxies/proxy@PROXY"}]
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

where PROXY is the proxy whose scores you want to get.

##### Get scores for a specific target in an environment

To get scores for a specific target in an environment, enter a command similar to the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityProfiles/PROFILE_ID/environments/ENV:computeEnvironmentScores" \
           -X POST \
           -d '{"timeRange":
                  {
                    "startTime": "YYYY-MM-DDT00:00:00Z",
                    "endTime": "YYYY-MM-DDT00:00:00Z"
                  },
                "filters": [{"scorePath": "/org@ORG/envgroup@ENVGROUP/env@ENV/target@TARGET"}]
               }' \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
