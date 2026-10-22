---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses/
title: Field Classes \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:40.317378+00:00
---

# Field Classes  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldclasses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Field Classes Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `Field` is an abstract base class representing a field of a document. This class should not be directly instantiated; instead, use one of the subclasses representing specific data types.

`Field` is defined in the module `google.appengine.api.search`.

## Properties

An instance of class `Field` has the following properties:

name
    

Name of the field. Must begin with a letter, contain only letters, digits, and underscores (`_`), and be no longer than 500 characters.

language
    

Two-letter [ISO 693-1](http://www.sil.org/iso639-3/codes.asp?order=639_1&letter=%25) language code for the field's content, to assist in tokenization. For example, `en` signifies that the field is English. If `None`, the language code of the document will be used.

value
    

Value of the field. Data type varies depending on the specific subclass.

## Subclasses

Class `Field` has the following subclasses:

class TextField
    

A field containing text.

The field's value must be a string or Unicode string. The following example shows a text field named `signature` with Polish language content:
    
    
    TextField(name='signature', value='brzydka pogoda', language='pl')

    

Exceptions

TypeError
    

Value supplied is not a text string.

ValueError
    

Value exceeds maximum allowable length.

class HtmlField
    

A field containing HTML content.

The field's value must be a string or Unicode string containing the searchable content of the field. The following example shows an HTML field named `content`:
    
    
    HtmlField(name='content', value='<html>herbata, kawa</html>', language='pl')

    

Exceptions

TypeError
    

Value supplied is not a text string.

ValueError
    

Value exceeds maximum allowable length.

class AtomField
    

A field containing text to be treated as an indivisible (atomic) token for indexing purposes.

The field's value must be a string or Unicode object to be treated as an atomic token. The following example shows an atom field named `contributor`:
    
    
    AtomField(name='contributor', value='foo@bar.com')

    

Exceptions

TypeError
    

Value supplied is not a text string.

ValueError
    

Value exceeds maximum allowable length.

class NumberField
    

A field containing a numeric value.

The field's value must be numeric. The following example shows a number field named `size` with integer value 10:
    
    
    NumberField(name='size', value=10)

    

**Exception**

TypeError
    

Value supplied is not numeric.

class DateField
    

A field containing a date or datetime value.

The field's value must be of type `datetime.date`, or `datetime.datetime`. Only Python ["naive"](https://docs.python.org/2/library/datetime.html) date and time objects can be used. "Aware" objects are not allowed. The following example shows a date field named `creation_date` representing the date 21 March 2011:
    
    
    DateField(name='creation_date', value=datetime.date(2011, 03, 21))

    

**Exception**

TypeError
    

Value supplied is not a `datetime.date` or a `datetime.datetime`.

class GeoField
    

A field containing a [GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/geopointclass) value.

The following example shows a GeoField named `place` representing a location at -33.84 degrees latitude and 151.26 degrees longitude:
    
    
    GeoField(name='place', value=GeoPoint(latitude=-33.84, longitude=151.26))

    

**Exception**

TypeError
    

Value supplied is not a `[GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/geopointclass)`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
