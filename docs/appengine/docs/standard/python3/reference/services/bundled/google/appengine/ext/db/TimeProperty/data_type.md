---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/data_type/
title: google.appengine.ext.db.TimeProperty.data_type \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:10:28.495441+00:00
---

# google.appengine.ext.db.TimeProperty.data_type  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/data_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.TimeProperty.data_type Stay organized with collections  Save and categorize content based on your preferences. 

time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object

Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.TimeProperty.data_type(
        *args, **kwargs
    )
    

All arguments are optional. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

## Attributes  
  
---  
  
`fold` |   
`hour` |   
`microsecond` |   
`minute` |   
`second` |   
`tzinfo` |   
  
## Methods

### `dst`
    
    
    dst()
    

Return self.tzinfo.dst(self).

### `fromisoformat`
    
    
    fromisoformat()
    

string -> time from time.isoformat() output

### `isoformat`
    
    
    isoformat()
    

Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].

The optional argument timespec specifies the number of additional terms of the time to include. Valid options are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds' and 'microseconds'.

### `replace`
    
    
    replace()
    

Return time with new specified fields.

### `strftime`
    
    
    strftime()
    

format -> strftime() style string.

### `tzname`
    
    
    tzname()
    

Return self.tzinfo.tzname(self).

### `utcoffset`
    
    
    utcoffset()
    

Return self.tzinfo.utcoffset(self).

### `__eq__`
    
    
    __eq__(
        value, /
    )
    

Return self==value.

### `__ge__`
    
    
    __ge__(
        value, /
    )
    

Return self>=value.

### `__gt__`
    
    
    __gt__(
        value, /
    )
    

Return self>value.

### `__le__`
    
    
    __le__(
        value, /
    )
    

Return self<=value.

### `__lt__`
    
    
    __lt__(
        value, /
    )
    

Return self<value.

### `__ne__`
    
    
    __ne__(
        value, /
    )
    

Return self!=value.

## Class Variables  
  
---  
  
max |  Instance of [`google.appengine.ext.db.TimeProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/data_type)  
min |  Instance of [`google.appengine.ext.db.TimeProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/TimeProperty/data_type)  
resolution |  Instance of `datetime.timedelta`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
