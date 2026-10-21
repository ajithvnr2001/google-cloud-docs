---
url: https://docs.cloud.google.com/data-studio/operators/
title: Operators \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:29.169812+00:00
---

# Operators  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/operators/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Operators Stay organized with collections  Save and categorize content based on your preferences. 

Operators are represented by special characters or keywords; they do not use function call syntax. An operator manipulates any number of data inputs, also called operands, and returns a result.

## Arithmetic operators

  * Addition: +
  * Subtraction: -
  * Division: /
  * Multiplication: *



## String operators

  * Concatenation: ||



## Comparison operators

  * =
  * !=
  * >
  * >=
  * <
  * <=



The operands on both sides of the comparison operators must of the same type: text, number or boolean.

## Logical operators

Logical operators return `true`, `false`, or `null`. Data Studio supports the `AND`, `OR`, `IN`, `IS NULL`, and `NOT` operators.

### AND / OR

Use `AND` and `OR` to create expressions with multiple input values. Use parentheses to group conditions and force order of precedence, if needed.

`Boolean expression A AND ( Boolean expression B OR Boolean expression C )`

###  IS NULL 

Returns true if the input field is empty or null.

#### Syntax

`field``IS NULL```

#### Parameters

> `field` —the dimension or metric to evaluate.

#### Examples

**Field contains** |  **Formula** |  **Results**  
---|---|---  
a  |  Field  IS NULL  |  false   
|  Field  IS NULL  |  true   
  
> #### More on NULL
> 
> Unless otherwise specified, all operators return `NULL` when one of the operands is `NULL`.
> 
> ```NULL``` is different from the empty string (""). Whereas trying to use the empty string in arithmetic generally produces an error, using  NULL  returns the null value:
> 
> `1+``NULL``=``NULL```
> 
> `1*``NULL``=``NULL```
> 
> `1/``NULL``=``NULL```
> 
> etc.
> 
> On the other hand, while you can concatenate values with the empty string, the result of concatenating any value with NULL is the null value:
> 
> ```CONCAT``("A", "", "B") = "AB"`
> 
> ```CONCAT``("A",``NULL``, "B") = null`

###  IN 

Returns true if the input field contains any of the the listed values. Both the field and list values must be of the same type. IN matches complete values and is case-sensitive. For partial value or case insensitive matching, use REGEXP_MATCH.

#### Syntax

`field``IN``(value1, value2,... valueN)`

#### Parameters

> `field` —the dimension or metric to evaluate.

> `value1,value2,...valueN` —the values to look for.

#### Examples

Field contains  |  Field type  |  Formula  |  Results   
---|---|---|---  
Bob  |  Text  |  _Field_ IN  ('Bob', 'Alice')  |  true   
Alice  |  Text  |  _Field_ IN  ('Bob', 'Alice')  |  true   
Jorge  |  Text  |  _Field_ IN  ('Bob', 'Alice')  |  false   
20  |  Number  |  _Field_ IN  (10, 20)  |  true   
10  |  Number  |  _Field_ IN  (10, 20)  |  true   
100  |  Number  |  _Field_ IN  (10, 20)  |  false   
Bob  |  Text  |  _Field_ IN  ('Bob', 20)  |  error (because Field is text but 20 is a number. To fix this, put "20" in quotes.)   
  
###  NOT 

Negates input expressions.

#### Examples

Formula  |  Results   
---|---  
` IF(2+2=4,"YES","NO") ` |  YES   
` IF(NOT 2+2=4,"YES","NO") ` |  NO   
` "abc" IN ("abc") ` |  true   
` "abc" NOT IN ("abc") ` |  false   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
