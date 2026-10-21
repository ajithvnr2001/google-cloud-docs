---
url: https://docs.cloud.google.com/identity/docs/how-to/approve-device/
title: Approving a device \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:53.209587+00:00
---

# Approving a device  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/approve-device/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Approving a device

The following examples shows you how to update the approval state for a user.

###  REST 

To update the approval state, call [`devices.deviceUsers.approve()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/approve) with a device name and customer object.

###  Python HTTP 

The following example shows a helper function to update the approval state using the Python HTTP library:
    
    
    """Example script to use the approve method of the Devices API."""
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
    
    if not SA_FILE:
      print('Please specify the location of the service account key file')
    if not ADMIN_EMAIL:
      print('Please specify the email of the administrator to call as')
    if not RESOURCE_NAME:
      print('Please specify the Device User Resource Name to be approved')
    
    if not SA_FILE or not ADMIN_EMAIL or not RESOURCE_NAME:
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
    # Approve the DeviceUser
    header = {
        'authorization': 'Bearer ' + dc.token,
        'Content-Type': 'application/json'
    }
    
    action_url = BASE_URL + RESOURCE_NAME + ':approve'
    request = urllib.request.Request(action_url, None, headers=header)
    request.get_method = lambda: 'POST'
    
    try:
      approve_response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
      if e.code == 400:
        print('The request was invalid. Perhaps the device is already approved?')
      else:
        print('Unknown error occurred')
      exit(-1)
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(approve_response)
    

Note that `RESOURCE_NAME` would be set to the name of the resource retrieved from a device resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
