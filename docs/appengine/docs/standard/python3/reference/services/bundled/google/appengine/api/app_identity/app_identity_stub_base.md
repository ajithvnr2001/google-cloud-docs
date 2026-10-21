---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub_base/
title: Module: google.appengine.api.app_identity.app_identity_stub_base \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:56:50.257962+00:00
---

# Module: google.appengine.api.app_identity.app_identity_stub_base  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub_base/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.app_identity.app_identity_stub_base Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub_base.py) Base class and constants for app identity stubs.

#### View aliases

**Main aliases** `google.appengine.api.app_identity.app_identity_stub.app_identity_stub_base` The module offers following objects available for app identity stubs:

#### Constants:

  * **`RSA_LIB_INSTALLED`** : boolean, pure-Python crypto enabled/disabled.
  * **`CRYPTO_LIB_INSTALLED`** : boolean, C crypto enabled/disabled.
  * **`APP_SERVICE_ACCOUNT_NAME`** : service account hardcoded in the stubs.
  * **`APP_DEFAULT_GCS_BUCKET_NAME`** : GCS bucket hardcoded in the stubs.
  * **`X509_PUBLIC_CERT`** : public certificate hardcoded in the stubs.



#### Classes:

  * **`AppIdentityServiceStubBase`** : base for app identity stub.



## Classes

[`class AppIdentityServiceStubBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub_base/AppIdentityServiceStubBase): A base class for the AppIdentityService API stub. | 

## Other Members  
  
---  
  
APP_DEFAULT_GCS_BUCKET_NAME |  `'app_default_bucket'`  
APP_SERVICE_ACCOUNT_NAME |  `'test@localhost'`  
D |  `16986504444572720056487621821047100642841595850137583213470349776864799280835251113078612103869013355016302383270733509621770011190160658118800356360958694229960556902751935956316359959542321272425222634888969943798180994410031448370776358545990991384123912313866752051562052322103544805811361355593091450379904792608637886965065110019212136239200637553477192566763015004249754677600683846556806159369233241157779976231822757855748068765507787598014034587835400718727569389998321277712761796543890788269130617890866139616903097422259980026836628018133574943835504630997228592718738382001678104796538128020421537193913`  
E |  `65537`  
HEADER1 |  `'0001'`  
HEADER2 |  `'00'`  
LENGTH_OF_SHA256_HASH |  `32`  
LEN_OF_PREFIX |  `19`  
MODULUS_BYTES |  `256`  
N |  `19119371788959611760073322421014045870056498252163411380847152703712917776733759011400972099255719579701566470175077491500050513917658074590935646529525468755348555932670175295728802986097707368373781743941167574738113348515272061138933984990014969297930973127363812200790406743271047572192133912023914306041356562363557723417403707408838823620411045628159183655215061768071407845537324145892973481372872161981015237572556138317222082306397041309823528068650373958169977675424007883635551170458356632131122901683151395297447872184074888239102348331222079943386530179883880518236689216575776729057173406091195993394637`  
PADDING |  `'ff'`  
PREFIX |  `'3031300d060960864801650304020105000420'`  
SIGNING_KEY_NAME |  `'key'`  
X509_PUBLIC_CERT |  `('\n' '-----BEGIN CERTIFICATE-----\n' 'MIIC/jCCAeagAwIBAgIIQTBFcRw3moMwDQYJKoZIhvcNAQEFBQAwIjEgMB4GA1UE\n' 'AxMXcm9ib3RqYXZhLmEuYXBwc3BvdC5jb20wHhcNMTEwMjIzMTUwNzQ5WhcNMTEw\n' 'MjI0MTYwNzQ5WjAiMSAwHgYDVQQDExdyb2JvdGphdmEuYS5hcHBzcG90LmNvbTCC\n' 'ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJd0YJCQWvQMa+7L/orCt3D0\n' 'hVtkdAkeGSikuT4U7mNrxBuOaAbxCIGhRbUe2p+uvRF6MZtLvoU1h9qEFo/wAVDO\n' 'HN4WHhw3VLl/OVuredRfe8bBTi0KqdgUBrKr8V61n26N3B4Ma9dkTMbcODC/XCfP\n' 'IRJnTIf4Z1vnoEfWQEJDfW9QLJFyJF17hpp9l5S1uuMJBxjYMsZ3ExLqSFhM7IbN\n' '1PDBAb6zGtI7b9AVP+gxS1hjXiJoZA32IWINAZiPV+0k925ecsV0BkI0zV4Ta06F\n' 'JexNx040y5ivr4C214GRUM3UKihirTcEOBS1a7SRi5wCPh/wT0A8gN6NNbTNjc0C\n' 'AwEAAaM4MDYwDAYDVR0TAQH/BAIwADAOBgNVHQ8BAf8EBAMCB4AwFgYDVR0lAQH/\n' 'BAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQEFBQADggEBAD+h2D+XGIHWMwPCA2DN\n' 'JgMhN1yTTJ8dtwbiQIhfy8xjOJbrzZaSEX8g2gDm50qaEl5TYHHr2zvAI1UMWdR4\n' 'nx9TN7I9u3GoOcQsmn9TaOKkBDpMv8sPtFBal3AR5PwR5Sq8/4L/M22LX/TN0eIF\n' 'Y4LnkW+X/h442N8a1oXn05UYtFo+p/6emZb1S84WZAnONGtF5D1Z6HuX4ikDI5m+\n' 'iZbwm47mLkV8yuTZGKI1gJsWmAsElPkoWVy2X0t69ecBOYyn3wMmQhkLk2+7lLlD\n' '/c4kygP/941fe1Wb/T9yGeBXFwEvJ4jWbX93Q4Xhk9UgHlso9xkCu9QeWFvJqufR\n' '5Cc=\n' '-----END CERTIFICATE-----\n')`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
