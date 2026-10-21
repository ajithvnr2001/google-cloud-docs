---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/FloatProperty/data_type/
title: google.appengine.ext.db.FloatProperty.data_type \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:59:03.628460+00:00
---

# google.appengine.ext.db.FloatProperty.data_type  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/FloatProperty/data_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.FloatProperty.data_type Stay organized with collections  Save and categorize content based on your preferences. 

Convert a string or number to a floating point number, if possible.

Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.FloatProperty.data_type(
        *args, **kwargs
    )
    

## Attributes  
  
---  
  
`imag` |  the imaginary part of a complex number   
`real` |  the real part of a complex number   
  
## Methods

### `as_integer_ratio`
    
    
    as_integer_ratio()
    

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original float and with a positive denominator.

Raise OverflowError on infinities and a ValueError on NaNs.
    
    
    >>> (10.0).as_integer_ratio()
    (10, 1)
    >>> (0.0).as_integer_ratio()
    (0, 1)
    >>> (-.25).as_integer_ratio()
    (-1, 4)
    

### `conjugate`
    
    
    conjugate()
    

Return self, the complex conjugate of any float.

### `fromhex`
    
    
    fromhex()
    

Create a floating-point number from a hexadecimal string.
    
    
    >>> float.fromhex('0x1.ffffp10')
    2047.984375
    >>> float.fromhex('-0x1p-1074')
    -5e-324
    

### `hex`
    
    
    hex()
    

Return a hexadecimal representation of a floating-point number.
    
    
    >>> (-0.1).hex()
    '-0x1.999999999999ap-4'
    >>> 3.14159.hex()
    '0x1.921f9f01b866ep+1'
    

### `is_integer`
    
    
    is_integer()
    

Return True if the float is an integer.

### `__abs__`
    
    
    __abs__()
    

abs(self)

### `__add__`
    
    
    __add__(
        value, /
    )
    

Return self+value.

### `__bool__`
    
    
    __bool__()
    

True if self else False

### `__eq__`
    
    
    __eq__(
        value, /
    )
    

Return self==value.

### `__floordiv__`
    
    
    __floordiv__(
        value, /
    )
    

Return self//value.

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

### `__mod__`
    
    
    __mod__(
        value, /
    )
    

Return self%value.

### `__mul__`
    
    
    __mul__(
        value, /
    )
    

Return self*value.

### `__ne__`
    
    
    __ne__(
        value, /
    )
    

Return self!=value.

### `__neg__`
    
    
    __neg__()
    

-self

### `__pos__`
    
    
    __pos__()
    

+self

### `__pow__`
    
    
    __pow__(
        value, mod, /
    )
    

Return pow(self, value, mod).

### `__radd__`
    
    
    __radd__(
        value, /
    )
    

Return value+self.

### `__rfloordiv__`
    
    
    __rfloordiv__(
        value, /
    )
    

Return value//self.

### `__rmod__`
    
    
    __rmod__(
        value, /
    )
    

Return value%self.

### `__rmul__`
    
    
    __rmul__(
        value, /
    )
    

Return value*self.

### `__rpow__`
    
    
    __rpow__(
        value, mod, /
    )
    

Return pow(value, self, mod).

### `__rsub__`
    
    
    __rsub__(
        value, /
    )
    

Return value-self.

### `__rtruediv__`
    
    
    __rtruediv__(
        value, /
    )
    

Return value/self.

### `__sub__`
    
    
    __sub__(
        value, /
    )
    

Return self-value.

### `__truediv__`
    
    
    __truediv__(
        value, /
    )
    

Return self/value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
