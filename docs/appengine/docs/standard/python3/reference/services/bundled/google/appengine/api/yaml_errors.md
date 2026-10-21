---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/
title: Module: google.appengine.api.yaml_errors \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:25:12.445511+00:00
---

# Module: google.appengine.api.yaml_errors  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.yaml_errors Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_errors.py) Errors used in the YAML API.

## Classes

[`class AmbiguousConfigurationFiles`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/AmbiguousConfigurationFiles): Both YAML and XML files exist for the same configuration information. [`class DuplicateAttribute`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/DuplicateAttribute): Generated when an attribute is assigned twice. [`class EmptyConfigurationFile`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/EmptyConfigurationFile): Tried to load an empty configuration file. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/Error): Base datastore yaml error type. [`class EventError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/EventError): Generated specifically when an error occurs in the event handler. [`class EventListenerError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/EventListenerError): Top level exception raised by the YAML listener. [`class EventListenerYAMLError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/EventListenerYAMLError): Generated specifically for `yaml.error.YAMLError`. [`class IllegalEvent`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/IllegalEvent): Raised when an unexpected event type is received by the listener. [`class InternalError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/InternalError): Raised when an internal implementation error is detected. [`class ListenerConfigurationError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/ListenerConfigurationError): Generated when there is a parsing problem due to configuration. [`class MultipleConfigurationFile`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/MultipleConfigurationFile): Tried to load configuration file with multiple objects. [`class ProtocolBufferParseError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/ProtocolBufferParseError): Error in protocol buffer parsing. [`class UnexpectedAttribute`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_errors/UnexpectedAttribute): Raised when an unexpected attribute is encounted. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
