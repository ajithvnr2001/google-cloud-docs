---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path
title: Module field_path (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:37.071410+00:00
---

# Module field_path (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module field_path (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Utilities for managing / converting field paths to / from strings.

## Classes 

### [FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)
    
    
    FieldPath(*parts: str)

Field Path object for client use.

A field path is a sequence of element keys, separated by periods. Each element key can be either a simple identifier, or a full unicode string.

In the string representation of a field path, non-identifier elements must be quoted using backticks, with internal backticks and backslashes escaped with a backslash.

## Modules Functions 

### get_field_path
    
    
    get_field_path(field_names: typing.Iterable[str])

Create a **field path** from a list of nested field names.

A **field path** is a `.`-delimited concatenation of the field names. It is used to represent a nested field. For example, in the data
    
    
    data = {
       'aa': {
           'bb': {
               'cc': 10,
           },
       },
    }
    

the field path `'aa.bb.cc'` represents that data stored in `data['aa']['bb']['cc']`.

**Returns**  
---  
**Type** | **Description**  
`str` | The `.`-delimited field path.  
  
### get_nested_value
    
    
    get_nested_value(field_path: str, data: typing.MutableMapping[str, typing.Any])

Get a (potentially nested) value from a dictionary.

If the data is nested, for example:
    
    
    >>> data
    {
        'top1': {
            'middle2': {
                'bottom3': 20,
                'bottom4': 22,
            },
            'middle5': True,
        },
        'top6': b' foo',
    }
    

a **field path** can be used to access the nested data. For example:
    
    
    >>> get_nested_value('top1', data)
    {
        'middle2': {
            'bottom3': 20,
            'bottom4': 22,
        },
        'middle5': True,
    }
    >>> get_nested_value('top1.middle2', data)
    {
        'bottom3': 20,
        'bottom4': 22,
    }
    >>> get_nested_value('top1.middle2.bottom3', data)
    20
    

See xref_field_path for more information on **field paths**.

**Parameters**  
---  
**Name** | **Description**  
`field_path` |  `str`   
A field path (`.`-delimited list of field names).  
`data` |  `Dict[str, Any]`   
The (possibly nested) data.  
**Exceptions**  
---  
**Type** | **Description**  
`KeyError` | If the `field_path` does not match nested data.  
**Returns**  
---  
**Type** | **Description**  
`Any` | (A copy of) the value stored for the `field_path`.  
  
### parse_field_path
    
    
    parse_field_path(api_repr: str)

Parse a **field path** from into a list of nested field names.

See `field_path` for more on **field paths**.

**Parameter**  
---  
**Name** | **Description**  
`api_repr` |  `str`   
The unique Firestore api representation which consists of either simple or UTF-8 field names. It cannot exceed 1500 bytes, and cannot be empty. Simple field names match `'^`_a-zA-Z][_a-zA-Z0-9]`*$'`. All other field names are escaped by surrounding them with backticks.  
**Returns**  
---  
**Type** | **Description**  
`List[str, ...]` | The list of field names in the field path.  
  
### render_field_path
    
    
    render_field_path(field_names: typing.Iterable[str])

Create a **field path** from a list of nested field names.

A **field path** is a `.`-delimited concatenation of the field names. It is used to represent a nested field. For example, in the data
    
    
    data = {
       'aa': {
           'bb': {
               'cc': 10,
           },
       },
    }
    

the field path `'aa.bb.cc'` represents that data stored in `data['aa']['bb']['cc']`.

**Returns**  
---  
**Type** | **Description**  
`str` | The `.`-delimited field path.  
  
### split_field_path
    
    
    split_field_path(path: str | None)

Split a field path into valid elements (without dots).

**Parameter**  
---  
**Name** | **Description**  
`path` |  `str`   
field path to be lexed.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if the path does not match the elements-interspersed- with-dots pattern.  
**Returns**  
---  
**Type** | **Description**  
`List(str)` | tokens  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
