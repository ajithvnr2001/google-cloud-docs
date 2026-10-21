---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/BooleanProperty/data_type/
title: google.appengine.ext.db.BooleanProperty.data_type \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:46:19.552139+00:00
---

# google.appengine.ext.db.BooleanProperty.data_type  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/BooleanProperty/data_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.BooleanProperty.data_type Stay organized with collections  Save and categorize content based on your preferences. 

bool(x) -> bool

Inherits From: [`data_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/IntegerProperty/data_type), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.db.BooleanProperty.data_type(
        *args, **kwargs
    )
    

Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

## Attributes  
  
---  
  
`denominator` |  the denominator of a rational number in lowest terms   
`imag` |  the imaginary part of a complex number   
`numerator` |  the numerator of a rational number in lowest terms   
`real` |  the real part of a complex number   
  
## Methods

### `as_integer_ratio`
    
    
    as_integer_ratio()
    

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.
    
    
    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)
    

### `bit_count`
    
    
    bit_count()
    

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.
    
    
    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3
    

### `bit_length`
    
    
    bit_length()
    

Number of bits necessary to represent self in binary.
    
    
    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6
    

### `conjugate`
    
    
    conjugate()
    

Returns self, the complex conjugate of any int.

### `from_bytes`
    
    
    from_bytes(
        byteorder, *, signed=False
    )
    

Return the integer represented by the given array of bytes.

bytes Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer. If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the most significant byte is at the end of the byte array. To request the native byte order of the host system, use `sys.byteorder' as the byte order value. signed Indicates whether two's complement is used to represent the integer.

### `to_bytes`
    
    
    to_bytes(
        length, byteorder, *, signed=False
    )
    

Return an array of bytes representing an integer.

length Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes. byteorder The byte order used to represent the integer. If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the most significant byte is at the end of the byte array. To request the native byte order of the host system, use `sys.byteorder' as the byte order value. signed Determines whether two's complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

### `__abs__`
    
    
    __abs__()
    

abs(self)

### `__add__`
    
    
    __add__(
        value, /
    )
    

Return self+value.

### `__and__`
    
    
    __and__(
        value, /
    )
    

Return self&value.

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

### `__invert__`
    
    
    __invert__()
    

~self

### `__le__`
    
    
    __le__(
        value, /
    )
    

Return self<=value.

### `__lshift__`
    
    
    __lshift__(
        value, /
    )
    

Return self<<value.

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

### `__or__`
    
    
    __or__(
        value, /
    )
    

Return self|value.

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

### `__rand__`
    
    
    __rand__(
        value, /
    )
    

Return value&self.

### `__rfloordiv__`
    
    
    __rfloordiv__(
        value, /
    )
    

Return value//self.

### `__rlshift__`
    
    
    __rlshift__(
        value, /
    )
    

Return value<<self.

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

### `__ror__`
    
    
    __ror__(
        value, /
    )
    

Return value|self.

### `__rpow__`
    
    
    __rpow__(
        value, mod, /
    )
    

Return pow(value, self, mod).

### `__rrshift__`
    
    
    __rrshift__(
        value, /
    )
    

Return value>>self.

### `__rshift__`
    
    
    __rshift__(
        value, /
    )
    

Return self>>value.

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

### `__rxor__`
    
    
    __rxor__(
        value, /
    )
    

Return value^self.

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

### `__xor__`
    
    
    __xor__(
        value, /
    )
    

Return self^value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
