---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type/
title: google.appengine.ext.db.DateTimeProperty.data_type \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:15:31.218734+00:00
---

# google.appengine.ext.db.DateTimeProperty.data_type  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.DateTimeProperty.data_type Stay organized with collections  Save and categorize content based on your preferences. 

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

Inherits From: [`data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateProperty/data_type), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.DateTimeProperty.data_type(
        *args, **kwargs
    )
    

The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

## Attributes  
  
---  
  
`day` |   
`fold` |   
`hour` |   
`microsecond` |   
`minute` |   
`month` |   
`second` |   
`tzinfo` |   
`year` |   
  
## Methods

### `astimezone`
    
    
    astimezone()
    

tz -> convert to local time in new timezone tz

### `combine`
    
    
    combine()
    

date, time -> datetime with same date and time fields

### `ctime`
    
    
    ctime()
    

Return ctime() style string.

### `date`
    
    
    date()
    

Return date object with same year, month and day.

### `dst`
    
    
    dst()
    

Return self.tzinfo.dst(self).

### `fromisocalendar`
    
    
    fromisocalendar()
    

int, int, int -> Construct a date from the ISO year, week number and weekday.

This is the inverse of the date.isocalendar() function

### `fromisoformat`
    
    
    fromisoformat()
    

string -> datetime from datetime.isoformat() output

### `fromordinal`
    
    
    fromordinal()
    

int -> date corresponding to a proleptic Gregorian ordinal.

### `fromtimestamp`
    
    
    fromtimestamp()
    

timestamp[, tz] -> tz's local time from POSIX timestamp.

### `isocalendar`
    
    
    isocalendar()
    

Return a named tuple containing ISO year, week number, and weekday.

### `isoformat`
    
    
    isoformat()
    

[sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM]. sep is used to separate the year from the time, and defaults to 'T'. The optional argument timespec specifies the number of additional terms of the time to include. Valid options are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds' and 'microseconds'.

### `isoweekday`
    
    
    isoweekday()
    

Return the day of the week represented by the date. Monday == 1 ... Sunday == 7

### `now`
    
    
    now()
    

Returns new datetime object representing current time local to tz.

tz Timezone object.

If no tz is specified, uses local timezone.

### `replace`
    
    
    replace()
    

Return datetime with new specified fields.

### `strftime`
    
    
    strftime()
    

format -> strftime() style string.

### `strptime`
    
    
    strptime()
    

string, format -> new datetime parsed from a string (like time.strptime()).

### `time`
    
    
    time()
    

Return time object with same time but with tzinfo=None.

### `timestamp`
    
    
    timestamp()
    

Return POSIX timestamp as float.

### `timetuple`
    
    
    timetuple()
    

Return time tuple, compatible with time.localtime().

### `timetz`
    
    
    timetz()
    

Return time object with same time and tzinfo.

### `today`
    
    
    today()
    

Current date or datetime: same as self.**class**.fromtimestamp(time.time()).

### `toordinal`
    
    
    toordinal()
    

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

### `tzname`
    
    
    tzname()
    

Return self.tzinfo.tzname(self).

### `utcfromtimestamp`
    
    
    utcfromtimestamp()
    

Construct a naive UTC datetime from a POSIX timestamp.

### `utcnow`
    
    
    utcnow()
    

Return a new datetime representing UTC day and time.

### `utcoffset`
    
    
    utcoffset()
    

Return self.tzinfo.utcoffset(self).

### `utctimetuple`
    
    
    utctimetuple()
    

Return UTC time tuple, compatible with time.localtime().

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
  
max |  Instance of [`google.appengine.ext.db.DateTimeProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type)  
min |  Instance of [`google.appengine.ext.db.DateTimeProperty.data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/DateTimeProperty/data_type)  
resolution |  Instance of `datetime.timedelta`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
