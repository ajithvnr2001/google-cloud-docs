---
url: https://docs.cloud.google.com/identity/docs/how-to/list-get-devices/
title: Listing device users \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:24.195418+00:00
---

# Listing device users  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/list-get-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Listing device users

This page explains how to list device users.

## Listing specific device users

The following examples show you how to list specific devices users in your organization.

###  REST 

To list specific device users, call [`devices.deviceUsers.list()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/list) with the name of the `customer` (organization).

###  Python HTTP 

The following example shows how to list specific device users using the Python HTTP library:
    
    
    """Sample script to demonstrate the use of the List method in the Devices API."""
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
    # LIST deviceUsers with filter.
    
    # Change this filter according to the options here:
    # https://support.google.com/a/answer/7549103
    FILTER = urllib.parse.quote_plus('status:approved os:IOS')
    list_url = BASE_URL + 'devices/-/deviceUsers?filter=' + FILTER
    auth_header = {'Authorization': 'Bearer ' + dc.token}
    content = urllib.request.urlopen(
        urllib.request.Request(list_url, headers=auth_header)).read()
    response = json.loads(content)
    pp = pprint.PrettyPrinter(indent=4)
    
    if 'deviceUsers' in response:
      print('Listed: ' + str(len(response['deviceUsers'])) + ' deviceUsers\n')
    
      for element in response['deviceUsers']:
        pp.pprint(element)
      print('Next page token: ' + response['nextPageToken'])
    else:
      print('Empty response')
    

Notice that `FILTER` is set to filter device users to those users whose status is "approved" (`status:approved`) and operating system is "IOS" (`os:IOS`).

## Getting a specific device user

The following examples show you how to retrieve a specific device user.

###  REST 

To get a specific device user, call [`devices.deviceUsers.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/get) with the `name` of the device and the `customer` (organization).

###  Python HTTP 

The following example shows how to retrieve a specific customer using the Python HTTP library:
    
    
    """Sample script to demonstrate the use of the get method in the Devices API."""
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
    
    # Enter the Resource Name. You can get this from the value of the name
    # field in the results of a List method call
    RESOURCE_NAME = ''
    
    if not SA_FILE:
      print('Please specify the location of the service account key file')
    if not ADMIN_EMAIL:
      print('Please specify the email of the administrator to call as')
    if not RESOURCE_NAME:
      print('Please specify the Resource Name to be retrieved')
    
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
    # Get the resource
    get_url = BASE_URL + RESOURCE_NAME
    auth_header = {'Authorization': 'Bearer ' + dc.token}
    content = urllib.request.urlopen(
        urllib.request.Request(get_url, headers=auth_header)).read()
    response = json.loads(content)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
