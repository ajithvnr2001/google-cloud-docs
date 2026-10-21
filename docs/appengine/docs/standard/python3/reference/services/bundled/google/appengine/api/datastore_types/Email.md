---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/Email/
title: google.appengine.api.datastore_types.Email \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:13:00.632584+00:00
---

# google.appengine.api.datastore_types.Email  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/Email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.Email Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L878-L892) An RFC2822 email address. Makes no attempt at validation. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.Email`, `google.appengine.ext.db.EmailProperty.data_type`
    
    
    google.appengine.api.datastore_types.Email(
        email
    )
    

This is the `gd:email` element. In XML output, the email address is provided as the address attribute. See: https://developers.google.com/gdata/docs/1.0/elements#gdEmail Raises `BadValueError` if email is not a valid email address.

## Methods

### `ToXml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L891-L892)
    
    
    ToXml()
    

### `capitalize`
    
    
    capitalize()
    

Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.

### `casefold`
    
    
    casefold()
    

Return a version of the string suitable for caseless comparisons.

### `center`
    
    
    center(
        width, fillchar, /
    )
    

Return a centered string of length width. Padding is done using the specified fill character (default is a space).

### `count`
    
    
    count()
    

S.count(sub[, start[, end]]) -> int Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

### `encode`
    
    
    encode(
        encoding='utf-8', errors='strict'
    )
    

Encode the string using the codec registered for encoding. encoding The encoding in which to encode the string. errors The error handling scheme to use for encoding errors. The default is 'strict' meaning that encoding errors raise a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

### `endswith`
    
    
    endswith()
    

S.endswith(suffix[, start[, end]]) -> bool Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

### `expandtabs`
    
    
    expandtabs(
        tabsize=8
    )
    

Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

### `find`
    
    
    find()
    

S.find(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### `format`
    
    
    format()
    

S.format(*args, **kwargs) -> str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

### `format_map`
    
    
    format_map()
    

S.format_map(mapping) -> str Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces ('{' and '}').

### `index`
    
    
    index()
    

S.index(sub[, start[, end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### `isalnum`
    
    
    isalnum()
    

Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

### `isalpha`
    
    
    isalpha()
    

Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

### `isascii`
    
    
    isascii()
    

Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

### `isdecimal`
    
    
    isdecimal()
    

Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

### `isdigit`
    
    
    isdigit()
    

Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are digits and there is at least one character in the string.

### `isidentifier`
    
    
    isidentifier()
    

Return True if the string is a valid Python identifier, False otherwise. Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as "def" or "class".

### `islower`
    
    
    islower()
    

Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

### `isnumeric`
    
    
    isnumeric()
    

Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and there is at least one character in the string.

### `isprintable`
    
    
    isprintable()
    

Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in repr() or if it is empty.

### `isspace`
    
    
    isspace()
    

Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

### `istitle`
    
    
    istitle()
    

Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

### `isupper`
    
    
    isupper()
    

Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

### `join`
    
    
    join(
        iterable, /
    )
    

Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string. Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

### `ljust`
    
    
    ljust(
        width, fillchar, /
    )
    

Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).

### `lower`
    
    
    lower()
    

Return a copy of the string converted to lowercase.

### `lstrip`
    
    
    lstrip(
        chars, /
    )
    

Return a copy of the string with leading whitespace removed. If chars is given and not None, remove characters in chars instead.

### `maketrans`
    
    
    maketrans()
    

Return a translation table usable for str.translate(). If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

### `partition`
    
    
    partition(
        sep, /
    )
    

Partition the string into three parts using the given separator. This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it. If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

### `removeprefix`
    
    
    removeprefix(
        prefix, /
    )
    

Return a str with the given prefix string removed if present. If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

### `removesuffix`
    
    
    removesuffix(
        suffix, /
    )
    

Return a str with the given suffix string removed if present. If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

### `replace`
    
    
    replace(
        old, new, count, /
    )
    

Return a copy with all occurrences of substring old replaced by new. count Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences. If the optional argument count is given, only the first count occurrences are replaced.

### `rfind`
    
    
    rfind()
    

S.rfind(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

### `rindex`
    
    
    rindex()
    

S.rindex(sub[, start[, end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

### `rjust`
    
    
    rjust(
        width, fillchar, /
    )
    

Return a right-justified string of length width. Padding is done using the specified fill character (default is a space).

### `rpartition`
    
    
    rpartition(
        sep, /
    )
    

Partition the string into three parts using the given separator. This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it. If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

### `rsplit`
    
    
    rsplit(
        sep=None, maxsplit=-1
    )
    

Return a list of the substrings in the string, using sep as the separator string. sep The separator used to split the string.
    
    
    When set to None (the default value), will split on any whitespace
    character (including \\n \\r \\t \\f and spaces) and will discard
    empty strings from the result.
    

maxsplit Maximum number of splits (starting from the left). -1 (the default value) means no limit. Splitting starts at the end of the string and works to the front.

### `rstrip`
    
    
    rstrip(
        chars, /
    )
    

Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### `split`
    
    
    split(
        sep=None, maxsplit=-1
    )
    

Return a list of the substrings in the string, using sep as the separator string. sep The separator used to split the string.
    
    
    When set to None (the default value), will split on any whitespace
    character (including \\n \\r \\t \\f and spaces) and will discard
    empty strings from the result.
    

maxsplit Maximum number of splits (starting from the left). -1 (the default value) means no limit. Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

### `splitlines`
    
    
    splitlines(
        keepends=False
    )
    

Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

### `startswith`
    
    
    startswith()
    

S.startswith(prefix[, start[, end]]) -> bool Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

### `strip`
    
    
    strip(
        chars, /
    )
    

Return a copy of the string with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

### `swapcase`
    
    
    swapcase()
    

Convert uppercase characters to lowercase and lowercase characters to uppercase.

### `title`
    
    
    title()
    

Return a version of the string where each word is titlecased. More specifically, words start with uppercased characters and all remaining cased characters have lower case.

### `translate`
    
    
    translate(
        table, /
    )
    

Replace each character in the string using the given translation table. table Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None. The table must implement lookup/indexing via **getitem** , for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

### `upper`
    
    
    upper()
    

Return a copy of the string converted to uppercase.

### `zfill`
    
    
    zfill(
        width, /
    )
    

Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.

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
    

Return value*self. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
