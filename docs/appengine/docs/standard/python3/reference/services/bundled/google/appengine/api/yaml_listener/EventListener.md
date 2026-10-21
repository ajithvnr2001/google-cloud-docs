---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_listener/EventListener/
title: google.appengine.api.yaml_listener.EventListener \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:38:04.114623+00:00
---

# google.appengine.api.yaml_listener.EventListener  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_listener/EventListener/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.yaml_listener.EventListener Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L84-L241) Helper class to re-map PyYAML events to method calls. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.yaml_listener.EventListener(
        event_handler
    )
    

By default, PyYAML generates its events via a Python generator. This class is a helper that iterates over the events from the PyYAML parser and forwards them to a handle class in the form of method calls. For simplicity, the underlying event is forwarded to the handler as a parameter to the call. This object does not produce iterable objects itself, but is instead a mapping to a given handler instance. Example use:
    
    
    ```python
    class PrintDocumentHandler(object):
      def DocumentStart(event):
        print "A new document has been started"
    
    EventListener(PrintDocumentHandler()).Parse('''
      key1: value1
      ---
      key2: value2
      '''
    
    ```
    >>> A new document has been started
        A new document has been started
    
    ```
    
    ```
    

In the example above, the implemented handler class (`PrintDocumentHandler`) has a single method that reports each time a new document is started within a YAML file. It is not necessary to subclass the `EventListener`, since only it receives a `PrintDocumentHandler` instance. Every time a new document begins, `PrintDocumentHandler.DocumentStart` is called with the PyYAML event passed in as its parameter. The constructor initializes the PyYAML event listener and constructs internal mapping directly from event type to method on the actual handler. This prevents reflection being used during the actual parse time. | 

## Args  
  
---  
  
`event_handler` |  Event handler that will receive mapped events. Must implement at least one appropriate handler method named from the values of the `_EVENT_METHOD_MAP`.   
  
## Raises  
  
---  
`ListenerConfigurationError` if `event_handler` is not an `EventHandler`.   
  
## Methods

### `HandleEvent`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L144-L159)
    
    
    HandleEvent(
        event, loader=None
    )
    

Handles individual PyYAML event.

Args  
---  
  
`event` |  Event to forward to method call in method call.   
  
Raises  
---  
`IllegalEvent` when receives an unrecognized or unsupported event type.   
  
### `Parse`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L220-L241)
    
    
    Parse(
        stream, loader_class=yaml.loader.SafeLoader, **loader_args
    )
    

Calls YAML parser to generate and handle all events.

Calls PyYAML parser and sends resulting generator to `handle_event` method for processing.

Args  
---  
  
`stream` |  String document or open file object to process as per the `yaml.parse` method. Any object that implements a `read()` method which returns a string document will work with the YAML parser.   
`loader_class` |  Used for dependency injection.   
`**loader_args` |  Pass to the loader on construction.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
