---
url: https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group/
title: Creating security groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:45.617190+00:00
---

# Creating security groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating security groups

This page explains how to create [security groups](https://docs.cloud.google.com/identity/docs/groups#group-types). You can create a new security group or update a Google group to a security group.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).




## Security group requirements

Security groups can only contain the following:

  * Users inside or outside of your domain (while associated with a Google service)
  * Service accounts inside or outside of your domain
  * Security groups inside of your domain



You can't apply the security group label to a Google Group that doesn't meet these conditions.

Only [predefined Super Admins or Groups Admins](https://support.google.com/a/answer/2405986) have the permissions to update security groups.

## Creating a new security group

###  REST 

To create a security group, call [`groups.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create) with an instance of the new group. The group instance must include a `groupKey`, `Parent`, and `labels` set to `cloudidentity.googleapis.com/groups.security` and `cloudidentity.googleapis.com/groups.discussion_forum`

###  Python 

The following example shows a helper function to create a Google Group using the Python client library:
    
    
    def create_google_group(service, customer_id, group_id, group_display_name, group_description):
      group_key = {"id": group_id}
      group = {
        "parent": "customers/" + customer_id,
        "description": group_description,
        "displayName": group_display_name,
        "groupKey": group_key,
        # Set the label to specify creation of a Google Group.
        "labels": {
          "cloudidentity.googleapis.com/groups.security": "",
          "cloudidentity.googleapis.com/groups.discussion_forum": ""
        }
      }
    
      try:
        request = service.groups().create(body=group)
        request.uri += "&initialGroupConfig=WITH_INITIAL_OWNER"
        response = request.execute()
        print(response)
      except Exception as e:
        print(e)
    

## Updating a Google Group to a security group

**Warning:** A security group cannot be changed back to a Google Group.

###  REST 

To update a Google Group to a security group, call [`groups.patch()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/patch) with `updateMask` set to `cloudidentity.googleapis.com/groups.security` and `cloudidentity.googleapis.com/groups.discussion_forum`.

**Sample request body**
    
    
    {
      "labels": {
        "cloudidentity.googleapis.com/groups.security": "",
        "cloudidentity.googleapis.com/groups.discussion_forum": ""
      }
    }
    

###  Python 

The following example shows a helper function to update a Google Group to a security group using the Python client library:
    
    
    def add_security_label_to_group(service, group_name):
      group = {
        "labels": {
          "cloudidentity.googleapis.com/groups.security": "",
          "cloudidentity.googleapis.com/groups.discussion_forum": ""
        }
      }
      try:
        request = service.groups().patch(name=group_name, body=group)
        request.uri = request.uri + '&updateMask=labels'
        response = request.execute()
        print(response)
      except Exception as e:
        print(e)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


