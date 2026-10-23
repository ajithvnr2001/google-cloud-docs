---
url: https://docs.cloud.google.com/monitoring/api/v3/sorting-and-filtering/
title: Reference: Sorting and filtering \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:52.532119+00:00
---

# Reference: Sorting and filtering  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/sorting-and-filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Reference: Sorting and filtering Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can sort and filter the results of applicable Cloud Monitoring API commands. Sorting lets you specify the order of the elements in the list of results. Filtering lets you define the properties of the elements that are included in the list of results. You use the `orderBy` and `filter` fields to sort and filter the API response.

The following table lists Cloud Monitoring API methods that support sorting or filtering:

Method | Supports sorting | Supports filtering  
---|---|---  
[`projects.alertPolicies.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list) | Yes | Yes  
[`projects.notificationChannels.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list) | Yes | Yes  
[`projects.snoozes.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/list) | No | Yes  
[`projects.uptimeCheckConfig.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) | No | Yes  
  
## Sorting and filtering basics

The presence of `orderBy` and `filter` string fields in the list request body indicates support for sorting and filtering in a `list` operation. Refer to the API reference documentation to determine whether the request body includes these fields.

## Sort-order syntax

The `orderBy` field consists of a comma-separated list of field paths that are optionally prefixed with a minus sign to reverse the order.

For example, `user_label.team,display_name` orders by team name in ascending order, and then -- for entries with the same team -- orders by the display name, also in ascending order. If you add a minus sign in front of one of the comma-separated fields, then that field is sorted in descending order; for example, if you are trying to cut down on the verbosity of your titles, you could use `-display_name.size` to sort by the title length, with objects ordered from the most wordy title to the briefest title.

To provide a more realistic example, `user_label.team,display_name` groups results first by team (in lexicographic order) and then, within each team grouping, organizes results by the title (also in lexicographic order).

Formally, the syntax can be described as:
    
    
       ORDER_BY_SPEC :=
          # Comma-separated list of fields.
          ORDERED_FIELD_LIST
    
       ORDERED_FIELD_LIST :=
          # Single field on which to sort.
          ORDERED_FIELD
    
          # Sort by the first field and then by the remaining fields.
          | ORDERED_FIELD "," ORDERED_FIELD_LIST
    
       ORDERED_FIELD :=
          # Sort by the field in ascending order.
          FIELD_REFERENCE
    
          # Sort by the field in descending order.
          | "-" FIELD_REFERENCE
    
       FIELD_REFERENCE :=
          # Simple field reference
          FIELD_NAME
    
          # Map value or list index lookup. For string-valued keys, the
          # supplied key in this notation must be quoted.
          | FIELD_NAME "[" LITERAL "]"
    
       FIELD_NAME :=
          # Immediate element
          IDENTIFIER
    
          # Subfield dereference or map element dereference. Note that,
          # in the case of maps, the IDENTIFIER on the left can also
          # be the singular form of the name of the map. That is, it is
          # permitted to use `user_label.mykey` and not just
          # `user_labels.mykey`. This is done for consistency with the
          # metric filters which permit `resource.label.` and `metric.label.`
          # which are in the singular form even though the map is `labels`.
          | IDENTIFIER "." FIELD_NAME
    
       LITERAL :=
           # Whole or real number.
           [0-9]+(.[0.9]+)?
    
           # String literal using single quotes. Note that strings must
           # always be quoted. This is to avoid ambiguity with attempting
           # to refer to the value of a field.
           |  '[^']*'
    
           # String literal using double quotes. Note that strings must
           # always be quoted. This is to avoid ambiguity with attempting
           # to refer to the value of a field.
           |  "[^"]*"
    
           # Literal boolean true.
           |  true
    
           # Literal boolean false.
           |  false
    
       IDENTIFIER :=
           # Non-digit followed by any number of letters or digits.
           [a-zA-Z_]+[a-zA-Z0-9_]*
    

## Filter syntax

The filter syntax consists of an expression language for constructing a predicate from one or more fields of the objects being filtered. Negation, conjunction, and disjunction are written using `NOT`, `AND`, and `OR` keywords. Fields can be compared with literal values by use of `:` (containment), `=` (equality), `>` (greater), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to), and `!=` (inequality) operators. The built-in functions `starts_with`, `ends_with`, `monitoring.regex.full_match` ([RE2](https://github.com/google/re2/wiki/Syntax) syntax) as well as the built-in properties `empty` and `size` provide support for more advanced comparisons.

### Examples

To return all entries with a non-empty display name or description where the `user_labels` field has the `active` key set (with any value):
    
    
    (NOT display_name.empty OR NOT description.empty) AND user_labels='active'
    

To return all entries whose description contains 'cloud':
    
    
    description:'cloud'
    

To return all entries whose title matches "Temp XYZ":
    
    
    display_name=monitoring.regex.full_match('Temp \\d{3}')
    

### Formal specification

The filter expression syntax can be summarized as follows:
    
    
       FILTER_EXPRESSION :=
             # Negation
             "NOT" FILTER_EXPRESSION
    
             # Short-circuiting AND
             | FILTER_EXPRESSION "AND" FILTER_EXPRESSION
    
             # Short-circuiting OR
             | FILTER_EXPRESSION "OR" FILTER_EXPRESSION
    
             # Implicit short-circuiting AND
             | FILTER_EXPRESSION FILTER_EXPRESSION
    
             # Parenthesized sub-expression
             | "(" FILTER_EXPRESSION ")"
    
             # Basic expression
             | SIMPLE_EXPRESSION
    
       SIMPLE_EXPRESSION :=
             # Field implicitly converted to boolean
             FIELD_REFERENCE
    
             # Field binary comparison. Note that the right-hand side must
             # be compatible with the type on the left-hand side; one cannot
             # compare a number with a string. Sensible implicit conversions
             # are permitted, however; comparing an integer and double will
             # succeed with appropriate conversion/widening taking place.
             | FIELD_REFERENCE OP LITERAL
    
             # Function invocation
             | FIELD_REFERENCE "=" FUNCTION_EXPRESSION
    
    
       FIELD_REFERENCE :=
             # Simple field reference
             FIELD_NAME
    
             # Map value or list index lookup. For string-valued keys, the
             # supplied key in this notation must be quoted.
             | FIELD_NAME "[" LITERAL "]"
    
       FIELD_NAME :=
             # Immediate element
             IDENTIFIER
    
             # Subfield dereference or map element dereference. Note that,
             # in the case of maps, the IDENTIFIER on the left can also
             # be the singular form of the name of the map. That is, it is
             # permitted to use `user_label.mykey` and not just
             # `user_labels.mykey`. This is done for consistency with the
             # metric filters which permit `resource.label.` and `metric.label.`
             # which are in the singular form even though the map is `labels`.
             | IDENTIFIER "." FIELD_NAME
    
       OP :=
             # Equality comparison. Should be avoided for double-valued fields.
             "="
    
             # Less than.
             | "<"
    
             # Greater than.
             | ">"
    
             # Less than or equal.
             | "<="
    
             # Greater than or equal.
             | ">="
    
             # Containment. This is equivalent to '=' for numeric types.
             | ":"
    
             # Not equal.
             | "!="
    
       LITERAL :=
           # Whole or real number.
           [0-9]+(.[0.9]+)?
    
           # String literal using single quotes. Note that strings must
           # always be quoted. This is to avoid ambiguity with attempting
           # to refer to the value of a field.
           |  '[^']*'
    
           # String literal using double quotes. Note that strings must
           # always be quoted. This is to avoid ambiguity with attempting
           # to refer to the value of a field.
           |  "[^"]*"
    
           # Literal boolean true.
           |  true
    
           # Literal boolean false.
           |  false
    
           # Date and Time formatted as per RFC-3339 standards using
           # double quotes.
           |  "YYYY-MM-DDT00:00:00-00:00"
    
       FUNCTION_EXPRESSION :=
           # Starts with.
           "starts_with" "(" LITERAL ")"
    
           # Ends with.
           |  "ends_with" "(" LITERAL ")"
    
           # Has substring. Takes an optional second argument that indicates whether
           # the substring matching is case-sensitive (true) or not (false).
           # The default is false, providing case-insensitive matches.
           |  "has_substring" "(" LITERAL [, [true|false]] ")"
    
           # Regular expression match.
           |  "monitoring.regex.full_match" "(" LITERAL ")"
    
       IDENTIFIER :=
           # Non-digit followed by any number of letters or digits.
           [a-zA-Z_]+[a-zA-Z0-9_]*
    

## Supported fields

The fields which can be referenced in `filter` or `orderBy` fields depends on the type of object that is being listed.

### `AlertPolicy`

The following fields can be referenced in `filter` and `orderBy` when enumerating [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) objects:

  * name
  * display_name
  * documentation.content
  * documentation.mime_type
  * user_labels
  * conditions.size
  * combiner
  * enabled
  * notification_channels



### `NotificationChannel`

The following fields can be referenced in `filter` and `orderBy` when enumerating [`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels) objects:

  * name
  * type
  * display_name
  * description
  * labels
  * user_labels



### `UptimeCheckConfig`

The following fields can be referenced in `filter` when enumerating [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig) objects:

  * display_name
  * user_labels
  * selected_regions
  * http_check.path
  * http_check.headers
  * http_check.port
  * tcp_check.port
  * monitored_resource.type
  * monitored_resource.labels



### `Snoozes`

The following fields can be referenced in `filter` when enumerating [`Snoozes`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes) objects:

  * interval.start_time
  * interval.end_time



## Advanced topics

This section provides more information about sorting and filtering API results.

### Field casing

Field names can be expressed in both `lower_case_with_underscores` and in `camelCase` forms. That is, both `display_name` and `displayName` are supported.

### Strings

**Built-in properties**

String-valued fields automatically have a `size` property generated that computes the number of Unicode characters in the string. This enables, for examples, a filter such as `display_name.size > 3 AND display_name.size < 10`. In addition to `size`, strings also have a bool `empty` property.

**Sort order**

When listing a string in `orderBy`, the strings are compared using byte-wise lexicographic ordering in the UTF-8 representation of the string; the strings are not sorted according to Unicode collation order.

**Implicit bool conversion**

It is possible to implicitly convert a string to bool in a filter as in `user_label.enabled`. Note that this conversion is not identical to testing that the string is non-empty; under this conversion, the contents of the string are parsed to a bool and strings that unambiguously parse to a boolean take on that boolean value; if the string is not obviously boolean-valued, then non-empty strings are interpreted as true and empty strings are interpreted as false.

Strings that case-insensitively match "false", "f", "no", "n", or "0" are considered to be unambiguously false; strings that case-insensitively match "true", "t", "yes", "y", or "1" are considered to be unambiguously true.

### Lists

**Built-in properties**

List-valued fields automatically have a `size` property generated that computes the number of elements in that list. For example, you can use `notification_channels.size` in `orderBy` to sort alert policies by the number of channels that they notify.

**Use in binary comparisons**

When comparing a list-valued field to a literal with one of the various binary operators, the comparison is interpreted as applying an element-wise comparison and then computing the OR of the results. For example, the filter `notification_channels:"123"` will evaluate to true if any of the notification channels has "123" as a substring. For the `!=` operator, specifically, the element-wise comparison is ANDed rather than ORed; in other words, for `!=`, none of the elements are permitted to match. Or, to restate, `x!=y` is logically equivalent to the pseudo-code `x[0]!=y AND x[1]!=y AND ... AND x[x.size-1]!=y` whereas `x=y` is logically equivalent to the pseudo-code `x[0]=y OR x[1]=y OR ... OR x[x.size-1]=y`. This inconsistency is designed to address the likely intent of `x!=y` and prevent confusion with such an expression returning results that contain the filtered value.

In addition to restricting on the list as a whole, it is also possible to refer to specific list entries by using the indexing (`[]`) operator. For example, you can use `notification_channels[0]:"123"` to test just the first element. A default (empty, zero, etc.) is generated in the case of out-of-bounds indexes.

**Implicit conversion to bool**

When specified in a filter without a binary comparison, a list will be implicitly converted to boolean. This conversion is distinct from testing that the list is non-empty; `a_list` and `NOT a_list.empty` return different results for `{false, false, false}` or any other non-empty list whose values all are or implicitly convert to the boolean value `false`.

### Maps

**Built-in properties**

Map-valued fields automatically have a `size` property generated that computes the number of elements in that map. For example, you can use `user_labels.size` in `orderBy` to sort by number of user labels defined. Similarly, a boolean-valued `empty` property is also auto-generated.

**Note:** if your map contains a key named `size`, then use `user_labels.size` to refer to the number of elements in the map and use `user_labels['size']` to refer to the value of the user label key `size`. The same applies to the `empty` property.

**Testing for key existence**

Maps can be compared with literal values with the various supported binary operators. The interpretation is logically equivalent to projecting the map into a list by extracting the map's keys and then executing the comparison. For example, you can use `user_labels="phase"` to determine whether the `user_labels` map contains a key whose value is equal to "phase".

**Referencing values by key**

Map entries can be referenced using one of two notations: dot (`.`) notation and index (`[]`) notation. For example, you can use `user_labels.team` or `user_labels['team']` to refer to the value corresponding to the key "team" in the `user_labels` field. For consistency with the metrics API which uses `metric.label.` and `resource.label.` prefixes rather than `metric.labels.` and `resource.labels.`, map fields can also be referenced using the singular form of the name (for example, `user_label.team` is also permitted). Note that, for keys named `size` or `empty`, you must use index notation; using dot notation will refer to the built-in map properties.

**Implicit conversion to bool**

In implicit conversions to bool, a map is considered to be true if it is non-empty and at least one map *value - implicitly converts to true. This is not the same as testing that the map is non-empty.

### Ordering by compound types

All fields that can be referenced in a filter can be referenced in `order_by`, as well. This also applies to complex and compound types. The sort order for these types is stable and well-defined, though not necessarily intuitive; therefore, this usage is discouraged but allowed.

**Lists**

Lists are compared using an element-wise, lexicographic comparison, with the smaller list coming first in the case of their common elements being equal. To give an example, `{0, 1}` is less than `{0, 2}` but greater than `{0}`.

**Maps**

Maps are compared by performing an element-wise comparison of the map values corresponding to the union of their keys. For keys defined in one map but not the other, a default (empty, zero, etc.) value is used for the comparison. To give an example, `{"x":0, "y":0}` is less than `{"x":1, "y":1}` but greater than `{"a":-1}` and equal to `{}`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
