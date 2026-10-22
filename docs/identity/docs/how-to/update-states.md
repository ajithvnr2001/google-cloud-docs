---
url: https://docs.cloud.google.com/identity/docs/how-to/update-states/
title: Updating the client state \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:43.313182+00:00
---

# Updating the client state  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/update-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Updating the client state

The following examples shows you how to update the client state for the API client calling the Devices API.

###  REST 

To update the client state, call [`devices.clientStates.patch()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/patch) with a customer name and [ClientState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates#ClientState) object.

###  Python HTTP 

The following example shows a helper function to update the client state using the Python HTTP library:
    
    
    """Sample script to demonstrate the use of the Update method in the Devices API."""
    import json
    import pprint
    
    from six.moves import urllib
    
    import google.auth.transport.requests
    from google.oauth2 import service_account
    
    SCOPES = ['https://www.googleapis.com/auth/cloud-identity.devices']
    BASE_URL = 'https://cloudidentity.googleapis.com/v1/'
    
    # Change this to the location of the service account key
    SA_FILE = ''
    
    # Enter the administrator to call as here.
    ADMIN_EMAIL = ''
    
    # Enter the Device User Resource Name. You can get this from the value
    # of the name field in the results of a List method call
    RESOURCE_NAME = ''
    
    # Enter the Client ID, which is in the format <customer-id>-<somestring>
    # Where 'customer-id' is your customer id.
    CLIENT_ID = ''
    
    if not SA_FILE:
      print('Please specify the location of the service account key file')
    if not ADMIN_EMAIL:
      print('Please specify the email of the administrator to call as')
    if not RESOURCE_NAME:
      print('Please specify the Device User Resource Name to be approved')
    if not CLIENT_ID:
      print('Please specify your client id, which is your customer-id, followed by'
            ' a hyphen, folowed by any string')
    
    if not SA_FILE or not ADMIN_EMAIL or not RESOURCE_NAME or not CLIENT_ID:
      exit(-1)
    
    def create_delegated_credentials(user_email):
      credentials = service_account.Credentials.from_service_account_file(
          SA_FILE,
          scopes=['https://www.googleapis.com/auth/cloud-identity.devices'])
    
      delegated_credentials = credentials.with_subject(user_email)
    
      return delegated_credentials
    
    ######################################################################
    # AUTHENTICATE the service account and retrieve an oauth2 access token
    
    request = google.auth.transport.requests.Request()
    dc = create_delegated_credentials(ADMIN_EMAIL)
    dc.refresh(request)
    print('Access token: ' + dc.token + '\n')
    
    ###############################
    # Update the client state
    header = {
        'authorization': 'Bearer ' + dc.token,
        'Content-Type': 'application/json'
    }
    body = {
        'customId': 'abcd',
        'assetTags': ['efgh', 'ijkl'],
        'healthScore': 'GOOD',
        'scoreReason': 'all ok',
        'managed': 'MANAGED',
        'complianceState': 'COMPLIANT'
    }
    
    update_clientstate_url = BASE_URL + RESOURCE_NAME + '/clientStates/' + CLIENT_ID + '?updateMask=' +
    'customId,assetTags,healthScore,scoreReason,managed,complianceState'
    
    serialized_body = json.dumps(body, separators=(',', ':'))
    request = urllib.request.Request(
        update_clientstate_url, serialized_body, headers=header)
    request.get_method = lambda: 'PATCH'
    
    try:
      contents = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
      if e.code == 404:
        print('The resource was not found')
      else:
        print('Permission denied. Did you provide the correct client id?')
      exit(-1)
    
    update_response = json.loads(contents.read())
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(update_response['response'])
    

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


