---
url: https://docs.cloud.google.com/identity/docs/how-to/create-devices/
title: Creating devices \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:19.201048+00:00
---

# Creating devices  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating devices

This page explains how to create devices.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [Devices API overview](https://docs.cloud.google.com/identity/docs/concepts/overview-devices).

  * [Set up the Devices API](https://docs.cloud.google.com/identity/docs/how-to/setup).




## Creating a device

The following examples shows you how to create a device.

###  REST 

To create a device, call [`devices.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/create) with the name of the `customer` (organization) and a [Device object](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices).

###  Python HTTP 

The following example shows a helper function to create a device using the Python HTTP library:
    
    
    """Example script to use the create method of the Devices API."""
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
    
    if not SA_FILE:
      print('Please specify the location of the service account key file')
    if not ADMIN_EMAIL:
      print('Please specify the email of the administrator to call as')
    
    if not SA_FILE or not ADMIN_EMAIL:
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
    # Create the Device
    header = {
        'authorization': 'Bearer ' + dc.token,
        'Content-Type': 'application/json'
    }
    body = {
        'serialNumber': 'someSerial',  # the serial number of your device.
    
        # see values in
        # https://cloud.google.com/identity/docs/reference/rest/v1/devices#DeviceType
        'deviceType': 'LINUX'
    }
    
    serialized_body = json.dumps(body, separators=(',', ':'))
    
    request_url = BASE_URL + 'devices'
    print('Request URL: ' + request_url)
    print('Request body: ' + serialized_body)
    
    serialized_body = json.dumps(body, separators=(',', ':'))
    request = urllib.request.Request(request_url, serialized_body, headers=header)
    request.get_method = lambda: 'POST'
    
    try:
      contents = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
      if e.code == 409:
        print('The request was invalid. Perhaps the device is already present?')
      else:
        print('Unknown error occurred: {}', e.code)
      exit(-1)
    
    create_response = json.loads(contents.read())
    inner_response = create_response['response']
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(inner_response)
    

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
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

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


