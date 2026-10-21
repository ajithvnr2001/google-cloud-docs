---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/Testbed/
title: google.appengine.ext.testbed.Testbed \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:40:45.200631+00:00
---

# google.appengine.ext.testbed.Testbed  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/Testbed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.testbed.Testbed Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L337-L984) Class providing APIs to manipulate stubs for testing. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.testbed.Testbed()
    

This class allows you to replace App Engine services with fake stub implementations. These stubs act like the actual APIs but do not invoke the replaced services. In order to use a fake service stub or disable a real service, invoke the corresponding `init_*_stub` methods of this class.

## Methods

### `activate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L356-L402)
    
    
    activate(
        use_datastore_emulator=False
    )
    

Activates the testbed. Invoking this method will also assign default values to environment variables that are required by App Engine services, such as the application ID. You can set custom values with `setup_env()`. | Args  
---  
  
`use_datastore_emulator` |  `True` if user specifies testbed to use the Cloud Datastore Emulator.   
  
### `deactivate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L404-L449)
    
    
    deactivate()
    

Deactivates the testbed.

This method will restore the API proxy and environment variables to the state they were in before `activate()` was called.

Raises  
---  
  
`NotActivatedError` |  If called before `activate()` was called.   
  
### `get_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L617-L638)
    
    
    get_stub(
        service_name
    )
    

Gets the stub for a service.

Args  
---  
  
`service_name` |  The name of the service.   
  
Returns  
---  
The stub for `service_name`.   
  
Raises  
---  
  
`NotActivatedError` |  The testbed is not activated.   
`StubNotSupportedError` |  The service is not supported by testbed.   
`StubNotEnabledError` |  The service stub has not been enabled.   
  
### `init_all_stubs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L976-L984)
    
    
    init_all_stubs(
        enable=True
    )
    

Enables all known testbed stubs.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_app_identity_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L640-L652)
    
    
    init_app_identity_stub(
        enable=True
    )
    

Enables the app identity stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_blobstore_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L660-L672)
    
    
    init_blobstore_stub(
        enable=True
    )
    

Enables the blobstore stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_capability_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L674-L685)
    
    
    init_capability_stub(
        enable=True
    )
    

Enables the capability stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_channel_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L687-L698)
    
    
    init_channel_stub(
        enable=True
    )
    

Enables the channel stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
Raises  
---  
  
`StubNotSupportedError` |  If called.   
  
### `init_datastore_v3_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L700-L796)
    
    
    init_datastore_v3_stub(
        enable=True,
        datastore_file=None,
        use_sqlite=False,
        auto_id_policy=AUTO_ID_POLICY_SEQUENTIAL,
        **stub_kw_args
    )
    

Enables the datastore stub.

The `datastore_file` argument can be set to the path of an existing datastore file, or `None` (default) to use an in-memory datastore that is initially empty. If you use the sqlite stub and have defined `datastore_file`, the changes that you apply in a test will be written to the file. If you use the default datastore stub, changes are _not_ saved to disk unless you set `save_changes=True`.

#### Note:

You can only access those entities of the datastore file that use the same application ID as the test run. You can change the application ID for a test with `setup_env()`.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`datastore_file` |  File name of a `dev_appserver` datastore file.   
`use_sqlite` |  `True` to use the Sqlite stub, or `False` (default) to use the file stub.   
`auto_id_policy` |  How datastore stub assigns auto IDs. This value can be either `AUTO_ID_POLICY_SEQUENTIAL` or `AUTO_ID_POLICY_SCATTERED`.   
`**stub_kw_args` |  Keyword arguments passed on to the service stub.   
  
Raises  
---  
  
`StubNotSupportedError` |  If `datastore_sqlite_stub` is `None`.   
  
### `init_files_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L801-L811)
    
    
    init_files_stub(
        enable=True
    )
    

Enables the Files API stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
Raises  
---  
  
`StubNotSupportedError` |  If called.   
  
### `init_images_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L813-L828)
    
    
    init_images_stub(
        enable=True, **stub_kwargs
    )
    

Enables the images stub.

The images service stub is only available in `dev_appserver` because it uses the PIL library.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`**stub_kwargs` |  Keyword arguments passed on to the service stub.   
  
### `init_mail_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L830-L846)
    
    
    init_mail_stub(
        enable=True, **stub_kw_args
    )
    

Enables the mail stub.

The email service stub is only available in `dev_appserver` because it uses the `subprocess` module.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`**stub_kw_args` |  Keyword arguments that are passed on to the service stub.   
  
### `init_memcache_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L848-L859)
    
    
    init_memcache_stub(
        enable=True
    )
    

Enables the memcache stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_modules_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L936-L948)
    
    
    init_modules_stub(
        enable=True
    )
    

Enables the modules stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
### `init_taskqueue_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L861-L882)
    
    
    init_taskqueue_stub(
        enable=True, **stub_kw_args
    )
    

Enables the taskqueue stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`**stub_kw_args` |  Keyword arguments passed on to the service stub.   
  
### `init_urlfetch_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L884-L907)
    
    
    init_urlfetch_stub(
        enable=True, urlmatchers=None
    )
    

Enables the `urlfetch` stub.

The `urlfetch` service stub uses the `urllib` module to make requests. On appserver, `urllib` also relies the `urlfetch` infrastructure, so using this stub will have no effect.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`urlmatchers` |  optional initial sequence of `(matcher, fetcher)` pairs to populate `urlmatchers_to_fetch_functions`; matchers passed here, if any, take precedence over default matchers dispatching GCS access.   
  
### `init_user_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L909-L922)
    
    
    init_user_stub(
        enable=True, **stub_kw_args
    )
    

Enables the users stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
`**stub_kw_args` |  Keyword arguments that are passed on to the service stub.   
  
### `init_xmpp_stub`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L924-L934)
    
    
    init_xmpp_stub(
        enable=True
    )
    

Enables the xmpp stub.

Args  
---  
  
`enable` |  `True` if the fake service should be enabled, or `False` if the real service should be disabled.   
  
Raises  
---  
  
`StubNotSupportedError` |  If called.   
  
### `setup_env`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L451-L542)
    
    
    setup_env(
        overwrite=False, **kwargs
    )
    

Sets default and custom environment variables.

By default, all of the items in `DEFAULT_ENVIRONMENT` will be created without being specified. To set a value other than the default, or to pass a custom environment variable, pass a corresponding keyword argument.

#### Example:

# All defaults

testbed_instance.setup_env()

# All defaults, overriding AUTH_DOMAIN in both context modes

testbed_instance.setup_env(auth_domain='custom')

# All defaults; adds a custom os.environ['CUSTOM'] = 'foo'

testbed_instance.setup_env(custom='foo')

To overwrite the values set by a previous invocation, pass `overwrite=True`. Passing this value will not result in an `OVERWRITE` entry in `os.environ`.

If the variable corresponds to a WSGI environ variable, it will be set in the gen2 request context as contextvars as well as `os.environ`. To only set the gen2 context, switch to `setup_wsgi_env()`.

Args  
---  
  
`overwrite` |  Boolean. Specifies whether to overwrite items with corresponding entries in `os.environ`.   
`**kwargs` |  Environment variables to set. The name of the argument will be uppercased and used as a key in `os.environ`.   
  
### `setup_wsgi_env`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/testbed/__init__.py#L547-L575)
    
    
    setup_wsgi_env(
        **kwargs
    )
    

Sets the gen2 request context with the WSGI vars provided in kwargs.

Valid values can be found in [`google.appengine.runtime.context.gae_headers`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/context/gae_headers) and [`google.appengine.runtime.context.wsgi`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/context/wsgi).

setup_wsgi_env does not also set the "legacy context mode" aka `os.environ`. If you still rely on the legacy context, use setup_env instead.

#### Example:

# Sets context.gae_headers.AUTH_DOMAIN

**Note:** that all as per PEP 3333, all headers have the HTTP_ prefix.

# GAE headers headers share an additional x _appengine_ prefix.

testbed_instance.setup_wsgi_env(http_x_appengine_auth_domain='custom')

# Sets context.wsgi.SERVER_NAME

testbed_instance.setup_wsgi_env(server_name='custom')

Args  
---  
  
`**kwargs` |  WSGI variables to set in the SDK's request context.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
