---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated/
title: google.appengine.api.validation.Validated \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:55:57.531546+00:00
---

# google.appengine.api.validation.Validated  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.Validated Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L272-L494) Base class for classes that require validation. Inherits From: [`ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.validation.Validated(
        **attributes
    )
    

A class which intends to use validated fields should sub-class itself from this class. Each class should define an 'ATTRIBUTES' class variable which should be a map from attribute name to its validator. For example:
    
    
      class Story(Validated):
        ATTRIBUTES = {'title': Type(str),
                      'authors': Repeated(Type(str)),
                      'isbn': Optional(Type(str)),
                      'pages': Type(int),
                      }
        ```
    
    Attributes that are not listed under `ATTRIBUTES` work like normal and are
    not validated upon assignment.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
    
    <tr>
    <td>
    `AttributeDefinitionError`
    </td>
    <td>
    When class instance is missing `ATTRIBUTE`
    definition or when `ATTRIBUTE` is of the wrong type.
    </td>
    </tr>
    </table>
    
    
    
    ## Methods
    
    <h3 id="CheckInitialized"><code>CheckInitialized</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L395-L398">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>CheckInitialized()
    </code></pre>
    
    Checks for missing or conflicting attributes.
    
    Subclasses should override this function and raise an exception for
    any errors. Always run this method when all assignments are complete.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Raises</th></tr>
    
    <tr>
    <td>
    `ValidationError`
    </td>
    <td>
    When there are missing or conflicting attributes.
    </td>
    </tr>
    </table>
    
    
    
    <h3 id="Get"><code>Get</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L366-L378">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>Get(
        key
    )
    </code></pre>
    
    Get a single value on Validated instance.
    
    This method can only be used to retrieve validated attributes.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Args</th></tr>
    
    <tr>
    <td>
    `key`
    </td>
    <td>
    The name of the attributes
    </td>
    </tr>
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Raises</th></tr>
    <tr class="alt">
    <td colspan="2">
    `ValidationError` when no validated attribute exists on class.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="GetUnnormalized"><code>GetUnnormalized</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L358-L364">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>GetUnnormalized(
        key
    )
    </code></pre>
    
    Get a single value on the `Validated` instance, without normalizing.
    
    
    <h3 id="GetValidator"><code>GetValidator</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L317-L335">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>@classmethod</code>
    <code>GetValidator(
        key
    )
    </code></pre>
    
    Safely get the underlying attribute definition as a `Validator`.
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Args</th></tr>
    
    <tr>
    <td>
    `key`
    </td>
    <td>
    Name of attribute to get.
    </td>
    </tr>
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Returns</th></tr>
    <tr class="alt">
    <td colspan="2">
    Validator associated with key or attribute value wrapped in a
    validator.
    </td>
    </tr>
    
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Raises</th></tr>
    
    <tr>
    <td>
    `ValidationError`
    </td>
    <td>
    if no such attribute exists.
    </td>
    </tr>
    </table>
    
    
    
    <h3 id="GetWarnings"><code>GetWarnings</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L337-L342">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>GetWarnings()
    </code></pre>
    
    Return all the warnings we've got, along with their associated fields.
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Returns</th></tr>
    <tr class="alt">
    <td colspan="2">
    A list of tuples of (dotted_field, warning), both strings.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="Set"><code>Set</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L344-L356">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>Set(
        key, value
    )
    </code></pre>
    
    Set a single value on `Validated` instance.
    
    This method can only be used to assign validated attributes.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Args</th></tr>
    
    <tr>
    <td>
    `key`
    </td>
    <td>
    The name of the attributes
    </td>
    </tr><tr>
    <td>
    `value`
    </td>
    <td>
    The value to set
    </td>
    </tr>
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Raises</th></tr>
    <tr class="alt">
    <td colspan="2">
    `ValidationError` when no validated attribute exists on class.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="SetMultiple"><code>SetMultiple</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L197-L209">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>SetMultiple(
        attributes
    )
    </code></pre>
    
    Set multiple values on Validated instance.
    
    All attributes will be validated before being set.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Args</th></tr>
    
    <tr>
    <td>
    `attributes`
    </td>
    <td>
    A dict of attributes/items to set.
    </td>
    </tr>
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Raises</th></tr>
    
    <tr>
    <td>
    `ValidationError`
    </td>
    <td>
    When no validated attribute exists on class.
    </td>
    </tr>
    </table>
    
    
    
    <h3 id="ToDict"><code>ToDict</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L476-L494">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>ToDict()
    </code></pre>
    
    Convert Validated object to a dictionary.
    
    Recursively traverses all of its elements and converts everything to
    simplified collections.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Returns</th></tr>
    <tr class="alt">
    <td colspan="2">
    A dict of all attributes defined in this classes `ATTRIBUTES` mapped
    to its value. This structure is recursive in that Validated objects
    that are referenced by this object and in lists are also converted to
    dicts.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="ToYAML"><code>ToYAML</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L251-L260">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>ToYAML()
    </code></pre>
    
    Print validated object as simplified YAML.
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Returns</th></tr>
    <tr class="alt">
    <td colspan="2">
    Object as a simplified YAML string compatible with parsing using the
    `SafeLoader`.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="__eq__"><code>__eq__</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L437-L454">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>__eq__(
        other
    )
    </code></pre>
    
    Equality operator.
    
    Comparison is done by comparing all attribute values to those in the other
    instance. Objects which are not of the same type are not equal.
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Args</th></tr>
    
    <tr>
    <td>
    `other`
    </td>
    <td>
    Other object to compare against.
    </td>
    </tr>
    </table>
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2">Returns</th></tr>
    <tr class="alt">
    <td colspan="2">
    `True` if validated objects are equal, else `False`.
    </td>
    </tr>
    
    </table>
    
    
    
    <h3 id="__ne__"><code>__ne__</code></h3>
    
    <a target="_blank" href="https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L456-L458">View source</a>
    
    <pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link devsite-disable-click-to-copy" suppresswarning>
    <code>__ne__(
        other
    )
    </code></pre>
    
    Inequality operator.
    
    
    
    
    
    
    <!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>
    
    <tr>
    <td>
    ATTRIBUTES<a id="ATTRIBUTES"></a>
    </td>
    <td>
    `None`
    </td>
    </tr>
    </table>
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
