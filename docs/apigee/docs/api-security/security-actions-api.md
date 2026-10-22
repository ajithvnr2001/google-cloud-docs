---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api/
title: Security Actions API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:53.984666+00:00
---

# Security Actions API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security Actions API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Advanced API Security Actions**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Actions is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum. 

This page describes how to manage security actions using the Apigee Management APIs. For an overview of the security actions functionality, including limitations and latencies, see the [Security actions overview and UI](https://docs.cloud.google.com/apigee/docs/api-security/security-actions).

You can access all of the security actions features through the [Apigee Management APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). See the [ Security Actions API reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions) for information on all of the available commands. This page shows examples of some of the available commands.

## Variables used in examples

The examples on this page can include these variables:

  * `ORG` is the organization.
  * `ENV` is the environment for the security action.
  * `ACTION_NAME` is the name of the security action.



## Configure multiple condition types

You can include one or two condition types (such as IP address lists and ASN numbers) in a single security action.

**Note:** Configuring two condition types in a security action is available when configuring the security action via the API, not via the UI, at this time.**Important:** This feature is available in Apigee hybrid starting with version 1.16.0.

To configure a security action with two condition types, include multiple condition keys within the `conditionConfig` object. For example:
    
    
    "conditionConfig": {"ipAddressRanges": ["100.0.225.0"], "asns": ["10578"]}

This example shows two condition types in a deny action:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions?security_action_id=ACTION_NAME" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"state": "ENABLED", "deny": {"responseCode": 404}, "conditionConfig": {"ipAddressRanges": ["100.0.225.0"], "asns": ["10578"]}}'
    

## Create security actions

This section provides examples for how to create security actions with different action types.

### Create a deny action

To create a deny action, enter a command similar to the following:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions?security_action_id=ACTION_NAME" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"state": "ENABLED", "deny": {"responseCode": 404}, "conditionConfig": {"ipAddressRanges": ["100.0.225.0"]}}'

This creates a security action that denies access to requests to the IP addresses listed in `ipAddressRanges` and returns a response code `404`.

### Create a flag action

To create a flag action, enter a command similar to the following:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions?security_action_id=ACTION_NAME" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"state": "ENABLED", "flag": {"headers": [{"name": "senseflag", "value": "flagvalue"}]}, "conditionConfig": {"ipAddressRanges": ["100.0.230.0"]}}'

This creates a security action that flags requests from the IP addresses listed in `ipAddressRanges` and adds a header `senseflag` with value `flagvalue`.

### Create an allow action

To create an allow action, enter a command similar to the following:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions?security_action_id=ACTION_NAME" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"state": "ENABLED", "allow": {}, "conditionConfig": {"ipAddressRanges": ["100.0.220.0", "200.0.0.0"]}}'

This creates a security action that allows requests from the IP addresses listed in `ipAddressRanges`.

## Edit security actions

This section provides an example for how to edit an existing security action configuration. See Enable or disable a security action or Delete a security action to see examples for those types of changes.

### Edit a deny action

This section shows an example for editing a deny action. The APIs also support editing the other [action types](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#security-actions).

`update_mask` can include any of these options: `description,condition_config, api_proxies,expire_time,ttl,flag,allow,deny,*` (everything), or omitted (defaults to everything).

See the [ Security Actions API reference documentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions#SecurityActions) for more information about potential values when editing actions.
    
    
      curl -X PATCH "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions/ACTION_NAME?update_mask=deny,conditionConfig" \
             -H "Authorization: Bearer $TOKEN" \
             -d '{"deny": {"responseCode": 404}, "conditionConfig": {"ipAddressRanges": ["100.0.230.0"]}}' \
             -H "Content-Type: application/json"
             {
               "name": "ACTION_NAME",
               "state": "ENABLED",
               "createTime": "2022-12-29T18:28:50Z",
               "updateTime": "2022-12-29T18:28:50Z",
               "conditionConfig": {
                 "ipAddressRanges": [
                   "100.0.230.0"
                 ]
               },
               "deny": {
                 "responseCode": 404
               }
             }

## Enable or disable a security action

The following examples show API calls to enable or disable security actions.

### Enable a security action

To enable a security action, enter a command similar to the following:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions/ACTION_NAME:enable"
           -H "Authorization: Bearer $TOKEN"

This returns a response like the following:
    
    
    {
          "name": "ACTION_NAME",
          "state": "ENABLED",
          "createTime": "2022-12-29T18:27:31Z",
          "updateTime": "2023-01-03T23:19:26.650965481Z",
          "conditionConfig": {
            "ipAddressRanges": [
              "100.0.220.0",
              "200.0.0.0"
            ]
          },
          "allow": {},
          "expireTime": "2028-01-01T00:00:00Z"
    }

### Disable a security action

To disable a security action, enter a command similar to the following:
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions/ACTION_NAME:disable"
           -H "Authorization: Bearer $TOKEN"

This returns a response like the following:
    
    
    {
          "name": "actionallow",
          "state": "DISABLED",
          "createTime": "2022-12-29T18:27:31Z",
          "updateTime": "2023-01-03T23:13:04.874540001Z",
          "conditionConfig": {
            "ipAddressRanges": [
              "100.0.220.0",
              "200.0.0.0"
            ]
          },
          "allow": {},
          "expireTime": "2028-01-01T00:00:00Z"
    }

## Get or list security actions

The following examples show how to get or list security actions

### Get a security action

To get a security action, enter a command similar to the following:
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions/ACTION_NAME"
           -H "Authorization: Bearer $TOKEN"

This returns a response like the following:
    
    
    {
          "name": "ACTION_NAME",
          "state": "DISABLED",
          "createTime": "2022-12-29T18:27:31Z",
          "updateTime": "2023-01-03T23:13:04Z",
          "conditionConfig": {
            "ipAddressRanges": [
              "100.0.220.0",
              "200.0.0.0"
            ]
          },
          "allow": {},
          "expireTime": "2028-01-01T00:00:00Z"
    }

### List security actions

To list all security actions, enter a command similar to the following:
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions"
           -H "Authorization: Bearer $TOKEN"

## Pause or resume security actions

The following examples show how to pause or resume security actions

### Pause all security actions

To Pause all security actions, enter a command similar to the following:
    
    
    curl -X PATCH "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActionsConfig" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"enabled": "false", "name": "organizations/ORG/environments/ENV/securityActionsConfig"}'

This returns a response like the following:
    
    
    {
          "name": "organizations/ORG/environments/ENV/securityActionsConfig",
          "enabled": false,
          "updateTime": "2023-01-23T21:44:58.063807Z"
    }

### Resume paused security actions

To resume paused security actions, enter a command similar to the following:
    
    
    curl -X PATCH "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActionsConfig" \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"enabled": "true", "name": "organizations/ORG/environments/ENV/securityActionsConfig"}'

This returns a response like the following:
    
    
    {
          "name": "organizations/ORG/environments/ENV/securityActionsConfig",
          "enabled": true,
          "updateTime": "2023-01-23T21:44:58.063807Z"
    }

## Delete security actions

To delete a security action, enter a command similar to the following:
    
    
    curl -X DELETE "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityActions/ACTION_NAME"
           -H "Authorization: Bearer $TOKEN"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
