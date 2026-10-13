---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/URLMap/
title: google.appengine.api.appinfo.URLMap \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:15.550189+00:00
---

# google.appengine.api.appinfo.URLMap  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/URLMap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.URLMap Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1091-L1397) Maps from URLs to handlers. Inherits From: [`HandlerBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/HandlerBase), [`Validated`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated), [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.appinfo.URLMap(
        **attributes
    )
    

This class acts similar to a union type. Its purpose is to describe a mapping between a set of URLs and their handlers. The handler type of a given instance is determined by which `handler-id` attribute is used. Every mapping can have one and only one handler type. Attempting to use more than one `handler-id` attribute will cause an `UnknownHandlerType` to be raised during validation. Failure to provide any `handler-id` attributes will cause `MissingHandlerType` to be raised during validation. The regular expression used by the `url` field will be used to match against the entire URL path and query string of the request; therefore, partial maps will not be matched. Specifying a `url`, such as `/admin`, is the same as matching against the regular expression `^/admin$`. Don't start your matching `url` with `^` or end them with `$`. These regular expressions won't be accepted and will raise `ValueError`.

#### Special cases:

When defining a `static_dir` handler, do not use a regular expression in the `url` attribute. Both the `url` and `static_dir` attributes are automatically mapped to these equivalents::
    
    
    <url>/(.*)
    <static_dir>/\1
    

For example, this declaration...::
    
    
    url: /images
    static_dir: images_folder
    

...is equivalent to this `static_files` declaration::
    
    
    url: /images/(.*)
    static_files: images_folder/\1
    upload: images_folder/(.*)
    

| 

## Raises  
  
---  
  
`AttributeDefinitionError` |  When class instance is missing `ATTRIBUTE` definition or when `ATTRIBUTE` is of the wrong type.   
  
## Attributes  
  
---  
  
`login` |  Specifies whether a user should be logged in to access a URL. The default value of this argument is `optional`.   
`secure` |  Sets the restriction on the protocol that can be used to serve this URL or handler. This value can be set to `HTTP`, `HTTPS` or `either`.   
`url` |  Specifies a regular expression that is used to fully match against the request URLs path. See the "Special cases" section of this document to learn more.   
`static_files` |  Specifies the handler ID attribute that maps `url` to the appropriate file. You can specify regular expression backreferences to the string matched to `url`.   
`upload` |  Specifies the regular expression that is used by the application configuration program to determine which files are uploaded as blobs. Because it is difficult to determine this information using just the `url` and `static_files` arguments, this attribute must be included. This attribute is required when you define a `static_files` mapping. A matching file name must fully match against the `upload` regular expression, similar to how `url` is matched against the request path. Do not begin the `upload` argument with the `^` character or end it with the `$` character.   
`static_dir` |  Specifies the handler ID that maps the provided `url` to a sub-directory within the application directory. See "Special cases."   
`mime_type` |  When used with `static_files` and `static_dir`, this argument specifies that the MIME type of the files that are served from those directories must be overridden with this value.   
`script` |  Specifies the handler ID that maps URLs to a script handler within the application directory that will run using CGI.   
`position` |  Used in `AppInclude` objects to specify whether a handler should be inserted at the beginning of the primary handler list or at the end. If `tail` is specified, the handler is inserted at the end; otherwise, the handler is inserted at the beginning. This behavior implies that `head` is the effective default.   
`expiration` |  When used with static files and directories, this argument specifies the time delta to use for cache expiration. This argument should use the following format: `4d 5h 30m 15s`, where each letter signifies days, hours, minutes, and seconds, respectively. The `s` for "seconds" can be omitted. Only one amount must be specified, though combining multiple amounts is optional. The following list contains examples of values that are acceptable: `10`, `1d 6h`, `1h 30m`, `7d 7d 7d`, `5m 30`.   
`api_endpoint` |  Specifies the handler ID that identifies an endpoint as an API endpoint. Calls that terminate here will be handled by the API serving framework.   
  
## Methods

### `AssertUniqueContentType`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1310-L1341)
    
    
    AssertUniqueContentType()
    

Makes sure that `self.http_headers` is consistent with `self.mime_type`.

This method assumes that `self` is a static handler, either `self.static_dir` or `self.static_files`. You cannot specify `None`.

Raises  
---  
  
`appinfo_errors.ContentTypeSpecifiedMultipleTimes` |  If `self.http_headers` contains a `Content-Type` header, and `self.mime_type` is set. For example, the following configuration would be rejected:: 
    
    
      handlers:
    
      - url: /static
        static_dir: static
        mime_type: text/html
        http_headers:
          content-type: text/html
    

As this example shows, a configuration will be rejected when `http_headers` and `mime_type` specify a content type, even when they specify the same content type.   
  
### `CheckInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1280-L1308)
    
    
    CheckInitialized()
    

Adds additional checking to make sure a handler has correct fields.

In addition to normal `ValidatedCheck`, this method calls `GetHandlerType`, which validates whether all of the handler fields are configured properly.

Raises  
---  
  
`UnknownHandlerType` |  If none of the handler ID attributes are set.   
`UnexpectedHandlerAttribute` |  If an unexpected attribute is set for the discovered handler type.   
`HandlerTypeMissingAttribute` |  If the handler is missing a required attribute for its handler type.   
`ContentTypeSpecifiedMultipleTimes` |  If `mime_type` is inconsistent with `http_headers`.   
  
### `ErrorOnPositionForAppInfo`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1364-L1375)
    
    
    ErrorOnPositionForAppInfo()
    

Raises an error if position is specified outside of AppInclude objects.

Raises  
---  
  
`PositionUsedInAppYamlHandler` |  If the `position` attribute is specified for an `app.yaml` file instead of an `include.yaml` file.   
  
### `FixSecureDefaults`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1343-L1350)
    
    
    FixSecureDefaults()
    

Forces omitted `secure` handler fields to be set to 'secure: optional'.

The effect is that `handler.secure` is never equal to the nominal default.

### `Get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L366-L378)
    
    
    Get(
        key
    )
    

Get a single value on Validated instance.

This method can only be used to retrieve validated attributes.

Args  
---  
  
`key` |  The name of the attributes   
  
Raises  
---  
`ValidationError` when no validated attribute exists on class.   
  
### `GetHandler`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1219-L1225)
    
    
    GetHandler()
    

Gets the handler for a mapping.

Returns  
---  
The value of the handler, as determined by the handler ID attribute.   
  
### `GetHandlerType`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1227-L1278)
    
    
    GetHandlerType()
    

Gets the handler type of a mapping.

Returns  
---  
The handler type as determined by which handler ID attribute is set.   
  
Raises  
---  
  
`UnknownHandlerType` |  If none of the handler ID attributes are set.   
`UnexpectedHandlerAttribute` |  If an unexpected attribute is set for the discovered handler type.   
`HandlerTypeMissingAttribute` |  If the handler is missing a required attribute for its handler type.   
`MissingHandlerAttribute` |  If a URL handler is missing an attribute.   
  
### `GetUnnormalized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L358-L364)
    
    
    GetUnnormalized(
        key
    )
    

Get a single value on the `Validated` instance, without normalizing.

### `GetValidator`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L317-L335)
    
    
    @classmethod
    GetValidator(
        key
    )
    

Safely get the underlying attribute definition as a `Validator`.

Args  
---  
  
`key` |  Name of attribute to get.   
  
Returns  
---  
Validator associated with key or attribute value wrapped in a validator.   
  
Raises  
---  
  
`ValidationError` |  if no such attribute exists.   
  
### `GetWarnings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L337-L342)
    
    
    GetWarnings()
    

Return all the warnings we've got, along with their associated fields.

Returns  
---  
A list of tuples of (dotted_field, warning), both strings.   
  
### `PrettyRepr`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1377-L1397)
    
    
    PrettyRepr()
    

Short human-readable representation.

### `Set`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L344-L356)
    
    
    Set(
        key, value
    )
    

Set a single value on `Validated` instance.

This method can only be used to assign validated attributes.

Args  
---  
  
`key` |  The name of the attributes   
`value` |  The value to set   
  
Raises  
---  
`ValidationError` when no validated attribute exists on class.   
  
### `SetMultiple`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L197-L209)
    
    
    SetMultiple(
        attributes
    )
    

Set multiple values on Validated instance.

All attributes will be validated before being set.

Args  
---  
  
`attributes` |  A dict of attributes/items to set.   
  
Raises  
---  
  
`ValidationError` |  When no validated attribute exists on class.   
  
### `ToDict`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L476-L494)
    
    
    ToDict()
    

Convert Validated object to a dictionary.

Recursively traverses all of its elements and converts everything to simplified collections.

Returns  
---  
A dict of all attributes defined in this classes `ATTRIBUTES` mapped to its value. This structure is recursive in that Validated objects that are referenced by this object and in lists are also converted to dicts.   
  
### `ToYAML`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L251-L260)
    
    
    ToYAML()
    

Print validated object as simplified YAML.

Returns  
---  
Object as a simplified YAML string compatible with parsing using the `SafeLoader`.   
  
### `WarnReservedURLs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L1352-L1362)
    
    
    WarnReservedURLs()
    

Generates a warning for reserved URLs.

See the `version element documentation`_ to learn which URLs are reserved.

.. _`version element documentation`: https://cloud.google.com/appengine/docs/python/config/appref#syntax

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L437-L454)
    
    
    __eq__(
        other
    )
    

Equality operator.

Comparison is done by comparing all attribute values to those in the other instance. Objects which are not of the same type are not equal.

Args  
---  
  
`other` |  Other object to compare against.   
  
Returns  
---  
`True` if validated objects are equal, else `False`.   
  
### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L456-L458)
    
    
    __ne__(
        other
    )
    

Inequality operator.

## Class Variables  
  
---  
  
ALLOWED_FIELDS | 
    
    
    {
     'api_endpoint': ('position', 'script'),
     'script': 'position',
     'static_dir': ('mime_type', 'expiration', 'require_matching_file', 'http_headers', 'application_readable'),
     'static_files': ('mime_type', 'upload', 'expiration', 'require_matching_file', 'http_headers', 'application_readable')
    }
      
  
ATTRIBUTES | 
    
    
    {
     'api_endpoint': <google.appengine.api.validation.Optional object>,
     'application_readable': <google.appengine.api.validation.Optional object>,
     'auth_fail_action': <google.appengine.api.validation.Options object>,
     'expiration': <google.appengine.api.validation.Optional object>,
     'http_headers': <google.appengine.api.validation.Optional object>,
     'login': <google.appengine.api.validation.Options object>,
     'mime_type': <google.appengine.api.validation.Optional object>,
     'position': <google.appengine.api.validation.Optional object>,
     'redirect_http_response_code': <google.appengine.api.validation.Optional object>,
     'require_matching_file': <google.appengine.api.validation.Optional object>,
     'script': <google.appengine.api.validation.Optional object>,
     'secure': <google.appengine.api.validation.Options object>,
     'static_dir': <google.appengine.api.validation.Optional object>,
     'static_files': <google.appengine.api.validation.Optional object>,
     'upload': <google.appengine.api.validation.Optional object>,
     'url': <google.appengine.api.validation.Optional object>
    }
      
  
COMMON_FIELDS | 
    
    
    {
     'auth_fail_action',
     'login',
     'redirect_http_response_code',
     'secure',
     'url'
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
