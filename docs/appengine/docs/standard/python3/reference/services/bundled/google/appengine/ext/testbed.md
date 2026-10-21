---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/
title: Module: google.appengine.ext.testbed \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:30:12.371483+00:00
---

# Module: google.appengine.ext.testbed  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.ext.testbed Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py) A module to use service stubs for testing. To test applications that use App Engine services, such as datastore, developers can use the available stub implementations. Service stubs behave like the original service without causing permanent side effects. The datastore stub, for example, allows you to write entities into memory without storing them to the actual datastore. The `testbed` module makes using those stubs for testing easier.

#### Example:

import unittest from google.appengine.ext import ndb from google.appengine.ext import testbed class TestModel(ndb.Model): number = ndb.IntegerProperty(default=42) class MyTestCase(unittest.TestCase): def setUp(self): # First, create an instance of the Testbed class. self.testbed = testbed.Testbed() # Then activate the testbed, which will allow you to use # service stubs. self.testbed.activate() # Next, declare which service stubs you want to use. self.testbed.init_datastore_v3_stub() self.testbed.init_memcache_stub() def tearDown(self): # Don't forget to deactivate the testbed after the tests are # completed. If the testbed is not deactivated, the original # stubs will not be restored. self.testbed.deactivate() def testInsertEntity(self): # Because we use the datastore stub, this put() does not have # permanent side effects. TestModel().put() fetched_entities = TestModel.query().fetch(2) self.assertEqual(1, len(fetched_entities)) self.assertEqual(42, fetched_entities[0].number)

## Enable stubs and disable services

The `testbed` module allows you to use stubs for the following services:
    
    
    - capability_service
    - channel
    - datastore_v3 (aka datastore)
    - images (only for dev_appserver)
    - mail (only for dev_appserver)
    - memcache
    - taskqueue
    - urlfetch
    - user
    - xmpp
    

To use a particular service stub, call `self.init_SERVICENAME_stub()`. Using this call will replace calls to the service with calls to the service stub. If you want to disable any calls to a particular service, call `self.init_SERVICENAME_stub(enable=False)`. This call can be useful if you want to test code that must not use a certain service.

## Environment variables

App Engine service stubs often depend on environment variables. For example, the datastore stub uses an environment variable to store entities linked to a particular app. `testbed` will use default values if nothing else is provided, but you can change those values with `self.setup_env()`.

## Classes

[`class ActiveStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/ActiveStub) [`class EmulatorSupportChecker`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/EmulatorSupportChecker): A static class. Checks whether datastore emulator is supported. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/Error): Base testbed error type. [`class NotActivatedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/NotActivatedError): Raised if the used testbed instance is not activated. [`class StubNotSupportedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/StubNotSupportedError): Raised if an unsupported service stub is accessed. [`class Testbed`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/Testbed): Class providing APIs to manipulate stubs for testing.

## Functions

[`validate_project_id(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/validate_project_id): Ensure that a GCP project ID is valid. | 

## Other Members  
  
---  
  
APP_IDENTITY_SERVICE_NAME |  `'app_identity_service'`  
AUTO_ID_POLICY_SCATTERED |  `'scattered'`  
AUTO_ID_POLICY_SEQUENTIAL |  `'sequential'`  
BLOBSTORE_SERVICE_NAME |  `'blobstore'`  
CAPABILITY_SERVICE_NAME |  `'capability_service'`  
CHANNEL_SERVICE_NAME |  `'channel'`  
DATASTORE_SERVICE_NAME |  `'datastore_v3'`  
DEFAULT_APP_ID |  `'testbed-test'`  
DEFAULT_AUTH_DOMAIN |  `'gmail.com'`  
DEFAULT_ENVIRONMENT | 
    
    
    {
     'AUTH_DOMAIN': 'gmail.com',
     'CURRENT_MODULE_ID': 'default',
     'CURRENT_VERSION_ID': 'testbed-version',
     'GAE_APPLICATION': 'testbed-test',
     'GAE_RUNTIME': 'python310',
     'GOOGLE_CLOUD_PROJECT': 'testbed-test',
     'HTTP_HOST': 'testbed.example.com',
     'REQUEST_ID_HASH': 'testbed-request-id-hash',
     'REQUEST_LOG_ID': '7357B3D7091D',
     'SERVER_NAME': 'testbed.example.com',
     'SERVER_PORT': '80',
     'SERVER_SOFTWARE': 'Development/1.0 (testbed)',
     'USER_EMAIL': '',
     'USER_ID': ''
    }
      
  
DEFAULT_SERVER_NAME |  `'testbed.example.com'`  
DEFAULT_SERVER_PORT |  `'80'`  
DEFAULT_SERVER_SOFTWARE |  `'Development/1.0 (testbed)'`  
FILES_SERVICE_NAME |  `'file'`  
IMAGES_SERVICE_NAME |  `'images'`  
INIT_STUB_METHOD_NAMES | 
    
    
    {
     'app_identity_service': 'init_app_identity_stub',
     'blobstore': 'init_blobstore_stub',
     'capability_service': 'init_capability_stub',
     'datastore_v3': 'init_datastore_v3_stub',
     'images': 'init_images_stub',
     'mail': 'init_mail_stub',
     'memcache': 'init_memcache_stub',
     'modules': 'init_modules_stub',
     'taskqueue': 'init_taskqueue_stub',
     'urlfetch': 'init_urlfetch_stub',
     'user': 'init_user_stub'
    }
      
  
MAIL_SERVICE_NAME |  `'mail'`  
MEMCACHE_SERVICE_NAME |  `'memcache'`  
MODULES_SERVICE_NAME |  `'modules'`  
SUPPORTED_SERVICES |  `['app_identity_service', 'blobstore', 'capability_service', 'datastore_v3', 'images', 'mail', 'memcache', 'modules', 'taskqueue', 'urlfetch', 'user']`  
TASKQUEUE_SERVICE_NAME |  `'taskqueue'`  
URLFETCH_SERVICE_NAME |  `'urlfetch'`  
URLMATCHERS_TO_FETCH_FUNCTIONS |  `[]`  
USER_SERVICE_NAME |  `'user'`  
XMPP_SERVICE_NAME |  `'xmpp'`  
apiserver_util |  `None`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
