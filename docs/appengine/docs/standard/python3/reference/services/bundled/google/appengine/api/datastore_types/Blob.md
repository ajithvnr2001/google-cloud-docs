---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/Blob/
title: google.appengine.api.datastore_types.Blob \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:48:57.408742+00:00
---

# google.appengine.api.datastore_types.Blob  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/Blob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.Blob Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L1230-L1248) A blob type, appropriate for storing binary data of any length. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.Blob`, `google.appengine.ext.db.BlobProperty.data_type`
    
    
    google.appengine.api.datastore_types.Blob(
        *args, **kwargs
    )
    

This behaves identically to the Python bytes type, except for the constructor, which only accepts bytes arguments. | 

## Args  
  
---  
  
`arg` |  optional bytes instance (default b'')   
  
## Attributes  
  
---  
  
`meaning_uri` |   
  
## Methods

### `ToXml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L1214-L1221)
    
    
    ToXml()
    

Output bytes as XML.

Returns  
---  
Base64 encoded version of itself for safe insertion in to an XML document.   
  
### `capitalize`
    
    
    capitalize()
    

B.capitalize() -> copy of B

Return a copy of B with only its first character capitalized (ASCII) and the rest lower-cased.

### `center`
    
    
    center(
        width, fillchar, /
    )
    

Return a centered string of length width.

Padding is done using the specified fill character.

### `count`
    
    
    count()
    

B.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of subsection sub in bytes B[start:end]. Optional arguments start and end are interpreted as in slice notation.

### `decode`
    
    
    decode(
        encoding='utf-8', errors='strict'
    )
    

Decode the bytes using the codec registered for encoding.

encoding The encoding with which to decode the bytes. errors The error handling scheme to use for the handling of decoding errors. The default is 'strict' meaning that decoding errors raise a UnicodeDecodeError. Other possible values are 'ignore' and 'replace' as well as any other name registered with codecs.register_error that can handle UnicodeDecodeErrors.

### `endswith`
    
    
    endswith()
    

B.endswith(suffix[, start[, end]]) -> bool

Return True if B ends with the specified suffix, False otherwise. With optional start, test B beginning at that position. With optional end, stop comparing B at that position. suffix can also be a tuple of bytes to try.

### `expandtabs`
    
    
    expandtabs(
        tabsize=8
    )
    

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

### `find`
    
    
    find()
    

B.find(sub[, start[, end]]) -> int

Return the lowest index in B where subsection sub is found, such that sub is contained within B[start,end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

### `fromhex`
    
    
    fromhex()
    

Create a bytes object from a string of hexadecimal numbers.

Spaces between two numbers are accepted. Example: bytes.fromhex('B9 01EF') -> b'\xb9\x01\xef'.

### `hex`
    
    
    hex()
    

Create a string of hexadecimal numbers from a bytes object.

sep An optional single character or byte to separate hex bytes. bytes_per_sep How many bytes between separators. Positive values count from the right, negative values count from the left.

#### Example:
    
    
    >>> value = b'\xb9\x01\xef'
    >>> value.hex()
    'b901ef'
    >>> value.hex(':')
    'b9:01:ef'
    >>> value.hex(':', 2)
    'b9:01ef'
    >>> value.hex(':', -2)
    'b901:ef'
    

### `index`
    
    
    index()
    

B.index(sub[, start[, end]]) -> int

Return the lowest index in B where subsection sub is found, such that sub is contained within B[start,end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the subsection is not found.

### `isalnum`
    
    
    isalnum()
    

B.isalnum() -> bool

Return True if all characters in B are alphanumeric and there is at least one character in B, False otherwise.

### `isalpha`
    
    
    isalpha()
    

B.isalpha() -> bool

Return True if all characters in B are alphabetic and there is at least one character in B, False otherwise.

### `isascii`
    
    
    isascii()
    

B.isascii() -> bool

Return True if B is empty or all characters in B are ASCII, False otherwise.

### `isdigit`
    
    
    isdigit()
    

B.isdigit() -> bool

Return True if all characters in B are digits and there is at least one character in B, False otherwise.

### `islower`
    
    
    islower()
    

B.islower() -> bool

Return True if all cased characters in B are lowercase and there is at least one cased character in B, False otherwise.

### `isspace`
    
    
    isspace()
    

B.isspace() -> bool

Return True if all characters in B are whitespace and there is at least one character in B, False otherwise.

### `istitle`
    
    
    istitle()
    

B.istitle() -> bool

Return True if B is a titlecased string and there is at least one character in B, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

### `isupper`
    
    
    isupper()
    

B.isupper() -> bool

Return True if all cased characters in B are uppercase and there is at least one cased character in B, False otherwise.

### `join`
    
    
    join(
        iterable_of_bytes, /
    )
    

Concatenate any number of bytes objects.

The bytes whose method is called is inserted in between each pair.

The result is returned as a new bytes object.

Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.

### `ljust`
    
    
    ljust(
        width, fillchar, /
    )
    

Return a left-justified string of length width.

Padding is done using the specified fill character.

### `lower`
    
    
    lower()
    

B.lower() -> copy of B

Return a copy of B with all ASCII characters converted to lowercase.

### `lstrip`
    
    
    lstrip(
        bytes, /
    )
    

Strip leading bytes contained in the argument.

If the argument is omitted or None, strip leading ASCII whitespace.

### `maketrans`
    
    
    maketrans(
        frm, to, /
    )
    

Return a translation table useable for the bytes or bytearray translate method.

The returned table will be one where each byte in frm is mapped to the byte at the same position in to.

The bytes objects frm and to must be of the same length.

### `partition`
    
    
    partition(
        sep, /
    )
    

Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original bytes object and two empty bytes objects.

### `removeprefix`
    
    
    removeprefix(
        prefix, /
    )
    

Return a bytes object with the given prefix string removed if present.

If the bytes starts with the prefix string, return bytes[len(prefix):]. Otherwise, return a copy of the original bytes.

### `removesuffix`
    
    
    removesuffix(
        suffix, /
    )
    

Return a bytes object with the given suffix string removed if present.

If the bytes ends with the suffix string and that suffix is not empty, return bytes[:-len(prefix)]. Otherwise, return a copy of the original bytes.

### `replace`
    
    
    replace(
        old, new, count, /
    )
    

Return a copy with all occurrences of substring old replaced by new.

count Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

### `rfind`
    
    
    rfind()
    

B.rfind(sub[, start[, end]]) -> int

Return the highest index in B where subsection sub is found, such that sub is contained within B[start,end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

### `rindex`
    
    
    rindex()
    

B.rindex(sub[, start[, end]]) -> int

Return the highest index in B where subsection sub is found, such that sub is contained within B[start,end]. Optional arguments start and end are interpreted as in slice notation.

Raise ValueError when the subsection is not found.

### `rjust`
    
    
    rjust(
        width, fillchar, /
    )
    

Return a right-justified string of length width.

Padding is done using the specified fill character.

### `rpartition`
    
    
    rpartition(
        sep, /
    )
    

Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty bytes objects and the original bytes object.

### `rsplit`
    
    
    rsplit(
        sep=None, maxsplit=-1
    )
    

Return a list of the sections in the bytes, using sep as the delimiter.

sep The delimiter according which to split the bytes. None (the default value) means split on ASCII whitespace characters (space, tab, return, newline, formfeed, vertical tab). maxsplit Maximum number of splits to do. -1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to the front.

### `rstrip`
    
    
    rstrip(
        bytes, /
    )
    

Strip trailing bytes contained in the argument.

If the argument is omitted or None, strip trailing ASCII whitespace.

### `split`
    
    
    split(
        sep=None, maxsplit=-1
    )
    

Return a list of the sections in the bytes, using sep as the delimiter.

sep The delimiter according which to split the bytes. None (the default value) means split on ASCII whitespace characters (space, tab, return, newline, formfeed, vertical tab). maxsplit Maximum number of splits to do. -1 (the default value) means no limit.

### `splitlines`
    
    
    splitlines(
        keepends=False
    )
    

Return a list of the lines in the bytes, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

### `startswith`
    
    
    startswith()
    

B.startswith(prefix[, start[, end]]) -> bool

Return True if B starts with the specified prefix, False otherwise. With optional start, test B beginning at that position. With optional end, stop comparing B at that position. prefix can also be a tuple of bytes to try.

### `strip`
    
    
    strip(
        bytes, /
    )
    

Strip leading and trailing bytes contained in the argument.

If the argument is omitted or None, strip leading and trailing ASCII whitespace.

### `swapcase`
    
    
    swapcase()
    

B.swapcase() -> copy of B

Return a copy of B with uppercase ASCII characters converted to lowercase ASCII and vice versa.

### `title`
    
    
    title()
    

B.title() -> copy of B

Return a titlecased version of B, i.e. ASCII words start with uppercase characters, all remaining cased characters have lowercase.

### `translate`
    
    
    translate(
        table, /, delete=b''
    )
    

Return a copy with each character mapped by the given translation table.

table Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are removed. The remaining characters are mapped through the given translation table.

### `upper`
    
    
    upper()
    

B.upper() -> copy of B

Return a copy of B with all ASCII characters converted to uppercase.

### `zfill`
    
    
    zfill(
        width, /
    )
    

Pad a numeric string with zeros on the left, to fill a field of the given width.

The original string is never truncated.

### `__add__`
    
    
    __add__(
        value, /
    )
    

Return self+value.

### `__contains__`
    
    
    __contains__(
        key, /
    )
    

Return key in self.

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

### `__getitem__`
    
    
    __getitem__(
        key, /
    )
    

Return self[key].

### `__gt__`
    
    
    __gt__(
        value, /
    )
    

Return self>value.

### `__iter__`
    
    
    __iter__()
    

Implement iter(self).

### `__le__`
    
    
    __le__(
        value, /
    )
    

Return self<=value.

### `__len__`
    
    
    __len__()
    

Return len(self).

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
