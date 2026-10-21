---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type/
title: google.appengine.ext.db.DateProperty.data_type \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:46:17.368151+00:00
---

# google.appengine.ext.db.DateProperty.data_type  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.DateProperty.data_type Stay organized with collections  Save and categorize content based on your preferences. 

date(year, month, day) --> date object

Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.DateProperty.data_type(
        *args, **kwargs
    )
    

## Attributes  
  
---  
  
`day` |   
`month` |   
`year` |   
  
## Methods

### `ctime`
    
    
    ctime()
    

Return ctime() style string.

### `fromisocalendar`
    
    
    fromisocalendar()
    

int, int, int -> Construct a date from the ISO year, week number and weekday.

This is the inverse of the date.isocalendar() function

### `fromisoformat`
    
    
    fromisoformat()
    

str -> Construct a date from the output of date.isoformat()

### `fromordinal`
    
    
    fromordinal()
    

int -> date corresponding to a proleptic Gregorian ordinal.

### `fromtimestamp`
    
    
    fromtimestamp()
    

Create a date from a POSIX timestamp.

The timestamp is a number, e.g. created via time.time(), that is interpreted as local time.

### `isocalendar`
    
    
    isocalendar()
    

Return a named tuple containing ISO year, week number, and weekday.

### `isoformat`
    
    
    isoformat()
    

Return string in ISO 8601 format, YYYY-MM-DD.

### `isoweekday`
    
    
    isoweekday()
    

Return the day of the week represented by the date. Monday == 1 ... Sunday == 7

### `replace`
    
    
    replace()
    

Return date with new specified fields.

### `strftime`
    
    
    strftime()
    

format -> strftime() style string.

### `timetuple`
    
    
    timetuple()
    

Return time tuple, compatible with time.localtime().

### `today`
    
    
    today()
    

Current date or datetime: same as self.**class**.fromtimestamp(time.time()).

### `toordinal`
    
    
    toordinal()
    

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

### `weekday`
    
    
    weekday()
    

Return the day of the week represented by the date. Monday == 0 ... Sunday == 6

### `__add__`
    
    
    __add__(
        value, /
    )
    

Return self+value.

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

### `__radd__`
    
    
    __radd__(
        value, /
    )
    

Return value+self.

### `__rsub__`
    
    
    __rsub__(
        value, /
    )
    

Return value-self.

### `__sub__`
    
    
    __sub__(
        value, /
    )
    

Return self-value.

## Class Variables  
  
---  
  
max |  Instance of [`google.appengine.ext.db.DateProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type)  
min |  Instance of [`google.appengine.ext.db.DateProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type)  
resolution |  Instance of `datetime.timedelta`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
