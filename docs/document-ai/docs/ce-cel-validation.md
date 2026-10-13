---
url: https://docs.cloud.google.com/document-ai/docs/ce-cel-validation/
title: CEL dialect for document validation \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:17.523817+00:00
---

# CEL dialect for document validation  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/ce-cel-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  CEL dialect for document validation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Document AI validation and correction leverages the [Common Expression Language (CEL)](https://cel.dev/overview/cel-overview) to allow for flexible data validation and manipulation within your document processing workflows. Document AI offers a set of custom functions, macros, and behavioral modifications tailored for document entity data.

## Access entities in CEL expression

All expressions are evaluated against a root variable named `doc`, which consists of [entities](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#entity) that are phrases or properties belonging to the document. These entities closely follow the structure of the entities of your extracted document.

While an extracted entity contains many properties, only three of them are available for CEL evaluation.

  * **`mention_text`** : Raw extracted text as present in an extracted entity. It defaults to an empty string.
  * **`normalized_value`** : Normalized mention text as present in an extracted entity. It defaults to null. Read more on [Normalization](https://docs.cloud.google.com/document-ai/docs/normalization).
  * **`bounding_poly`** : A special object containing a representation of the extracted entity's placement in the document and used for alignment checks. It defaults to null.



## Data model

The exact structure of an extracted entity within the `doc` map depends on two factors. The first is whether its structure is a concrete value, such as a number or plain text, or if it's a complex object. The second factor is whether its occurrence type is single or multiple. For more information, see [`OccurrenceType`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/DocumentSchema#occurrencetype).

A key feature of the validation data model is that any entity defined in the schema but not extracted from the document is automatically populated with default values. This design lets you skip most of the explicit null checks in your CEL expressions, significantly simplifying your validation expressions. You only need to explicitly write null checks to ensure a selected entity was indeed extracted.

## Leaf entities example cases

The following sections describe how to access the entities in a leaf entity, which is one without nested child entities. Leaf entities directly hold a value.

### Leaf entity with a single occurrence

This is the most basic case, using `OccurrenceType` of `OPTIONAL_ONCE` or `REQUIRED_ONCE`. The entity is represented as an **object** containing the three standard properties.

An example of how to access these values is `doc.invoice_date.normalized_value`.

It has the structure:
    
    
      "invoice_date": {
        "mention_text": "1",
        "normalized_value": 1.0,
        "bounding_poly": bounding_poly_object
      }
    

And default value:
    
    
      "invoice_date": {
        "mention_text": "",
        "normalized_value": null,
        "bounding_poly": null
      }
    

### Leaf entity with multiple occurrences

This case applies to leaf entities which can occur multiple times and have an `OccurrenceType` of `OPTIONAL_MULTIPLE` or `REQUIRED_MULTIPLE`. For example, in a list of payment due dates, it's represented as an **object** where each property holds a **list** of the corresponding values from all occurrences. So properties like `mention_text`, `normalized_value`, and `bounding_poly` might have multiple entities.

An example of how to access these values is `doc.payment_due_dates.normalized_value[0]`.

It has the structure:
    
    
      "payment_due_dates": {
        "mention_text": ["Mar 1, 2024", "Apr 1, 2024"],
        "normalized_value": [null, proto.timestamp(2024-04-01)],
        // Note: If a value is not normalized, it is stored as a null.
        "bounding_poly": [bounding_poly_object,bounding_poly_object]
      }
    

And default value:
    
    
      "payment_due_dates": {
        "mention_text": [],
        "normalized_value": []
        "bounding_poly": []
      }
    

## Nested entities

A nested entity is a container for other entities, which are its "children."

### Nested entity with one occurrence

If a nested entity occurs only once, for example a single `receiver_address`, it's represented as an **object** where the keys are the names of its child entities.

An example of how to access these values is `doc.receiver_address.city.mention_text`.

It has the structure:
    
    
      "receiver_address": {
        "street": {
          "mention_text": "123 Main St",
          "normalized_value": "123 Main St",
          "bounding_poly": bounding_poly_object
        }
        }
    

And default value:

**Note:** The default value isn't `"receiver_address"`: `null`. This is a direct result of populating all unextracted schema entities with their respective defaults.
    
    
      "receiver_address": {
        "street": {
          "mention_text": "",
          "normalized_value": null,
          "bounding_poly": null
        }
        }
    

### Nested entity with multiple occurrences

When a nested entity can occur multiple times, it's represented as a **list of objects**. Each object in the list represents one full instance of the nested entity and contains its children.

An example of how to access these values is `doc.line_items[1].description.normalized_value`.

It has the structure:
    
    
      "line_items": [
        {
          "description": { "mention_text": "Product A", ... },
          "quantity": { "mention_text": "2", ... }
        },
        {
          "description": { "mention_text": "Service B", ... },
          "quantity": { "mention_text": "5", ... }
        }
      ]
    

And default value:
    
    
      "line_items": []
    

### Conversion table of normalized value

This table shows how the selected schema entity data type translates to the CEL `normalized_value` data type.

Schema data type | CEL data type  
---|---  
Currency, Address | `string`  
Number, Money | `double`  
Datetime | `proto.Timestamp`  
Checkbox, Signature | `bool`  
Plain Text | N/A  
  
## Example expressions

Here are some example CEL expressions.
    
    
    // Leaf entity with a single occurrence: Get the invoice ID string
    doc.invoice_id.normalized_value == "INV-12345"
    
    // Leaf entity with multiple occurrences: Get the first payment term from the list
    doc.payments.mention_text[0].matches('^\d+$')
    
    // Nested entity with one occurrence: Access a child entity of a single nested entity
    doc.receiver_address.name.normalized_value.star
    tsWith("John")
    // Nested entity with multiple occurrences: Access a child of a specific item in a list of nested entities
    doc.line_items[1].description.normalized_value == "Premium Gadget"
    
    // Advanced: Sum the total of all line items
    doc.line_items.map(item, item.total.normalized_value).sum() == 275.0
    
    // Advanced: Check if any line item has a quantity greater than 1
    doc.line_items.exists(item, item.quantity.normalized_value > 1.0)
    

Here are other examples of CEL logic you can use.
    
    
    // Ensure due date is after invoice date
    doc.due_date.normalized_value > doc.invoice_date.normalized_value
    
    // Cross list validation: ensure that each employer_contribution 
    // has a corresponding employee deduction
     doc.employer_contribution.size() == doc.employee_deduction.size() && lists.range(doc.employer_contribution.size()).all(i,doc.employee_deduction[i].current_amount.mention_text != "" && doc.employer_contribution[i].current_amount.mention_text != "")
    

## Behavioral changes

Document AI's CEL dialect modifies some standard behaviors to better suit document processing use cases.

### Epsilon-based equality

To address the lack of decimal type in CEL and account for common floating-point inaccuracies in financial and numerical data, the equality (`==`) and inequality (`!=`) operators are modified for numeric types (`double`, `int`). Instead of exact equality, they use an epsilon-based comparison with a tolerance of `1e-2` (0.01).

For example, consider a `total_amount` with a normalized value of `100.005`.

With the expression `doc.total_amount.normalized_value == 100.0`, the result is `true`. This is because `abs(100.005 - 100.0)` is less than `0.01`. Standard CEL would return `false`.

For the expression `doc.total_amount.normalized_value == 100.02` the result is `false`. This is because `abs(100.005 - 100.02)` is greater than `0.01`.

### String function restrictions

The standard CEL string manipulation functions are restricted to operate only on an entity's `mention_text` property. This restriction ensures that validation rules are consistently applied to the literal text string as it appears in the document.

The affected functions are:

  * `contains()`
  * `endsWith()`
  * `startsWith()`
  * `matches()`



Here is a valid example:
    
    
    // Checks if the extracted currency symbol is a dollar sign.
    doc.total_amount.mention_text.startsWith("$")
    

Here is an example of an invalid command:
    
    
    // This will produce a validation error upon save because contains() is not
    // being used on a .mention_text field.
    doc.supplier_name.normalized_value.contains("Inc.")
    

## Additional functions

This section describes non-standard global and member functions available in the Document AI CEL evaluation environment.

### Sum function
    
    
    ### sum()
    

Calculates the sum of a list of numeric elements. It can be called on lists of integers or doubles. Not that null values in the list are ignored. If the list contains any non-numeric elements, the function will trigger an error.

**Signature:** `<list>.sum()`

Here's an example summing up the normalized value of several line items.
    
    
    // Calculates the sum of all line item amounts.
    doc.line_item_amounts.normalized_value.sum()
    

### Or function
    
    
    ### or()
    

Returns the original value if it is not null; otherwise, it returns the second (default) argument.

**Signature:** `<value>.or(<;default_value>)`

As an example, you can use it to provide a default value when an optional field might be missing.
    
    
    // If the tax amount is not found, use a default of 0.0 for calculation.
    doc.tax_amount.normalized_value.or(0.0) > 5.0
    

### Check list vertical alignment function
    
    
    ### checkVerticalAlignment()
    

Returns `true` if all the `bounding_poly` objects are vertically aligned to a degree specified by the tolerance. Otherwise, returns an error describing which entities are misaligned. 

The tolerance is an optional argument that specifies the overlap of a bounding poly with the automatically selected best aligned bounding poly, 0 meaning bounding polys are non-intersecting, 1 meaning that the bounding polys are identical.

**Signature:** `checkVerticalAlignment([<;bounding_poly>,...],tolerance=0.8)`

As an example, you can use this to help keep all extracted entities within a single column.
    
    
    // Make sure that all extracted quantities are in the same column
    checkVerticalAlignment(doc.line_items.map(li,li.quantity.bounding_poly))
    

### Check horizontal alignment function
    
    
    ### checkHorizontalAlignment()
    

Returns `true` if all the `bounding_poly` objects are horizontally aligned to a degree specified by the tolerance. Otherwise, returns an error describing which entities are misaligned. 

The tolerance is an optional argument that specifies the overlap of a bounding poly with the automatically selected best aligned bounding poly. The meaning of 0 is that the bounding polys are non-intersecting, and 1 means bounding polys are identical.

**Signature:** `checkHorizontalAlignment([<;bounding_poly>,...],tolerance=0.6)`

As an example, you can use this to help keep all extracted entities within a single row.
    
    
    // For all line items make sure that each extracted line item's
    // children are in the same row. For example, if line item has
    // quantity and description properties, it makes sure they are in 
    // a single row for each respective line item.
    doc.line_items.all(li, checkHorizontalAlignment(li.map(col,li[col].bounding_poly)))
    

## Additional macros

This section describes non-standard macros available in the Document AI CEL evaluation environment.

For more information about macros, see [Language definition: Macros](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros).

### Reduce macro
    
    
    ### reduce()
    

Use the `reduce` macro to perform cumulative operations over a list.

**Signature:** `<list>.reduce(<;iterator_name>, <;accumulator_name>, <;initial_value>, <;loop_expression>)`

  * **`iterator_name`** : A variable name for the element being processed in each iteration.
  * **`accumulator_name`** : A variable name for the value that accumulates the result.
  * **`initial_value`** : The initial value of the accumulator.
  * **`loop_expression`** : An expression that defines how the accumulator is updated in each step.



Here is an example of macro use:
    
    
    // Use reduce to sum up the quantities from all line items.
    doc.line_items.reduce(item, running_total, 0.0, running_total + item.quantity.normalized_value)
    
    // Result: 3.0
    // Tip: this could also be done by concatenating map and sum:
    doc.line_items.map(item,item.quantity.normalized_value).sum()
    

## CEL extension libraries

In addition to the custom features, the following standard CEL extension libraries are available.

  * **Lists** : Provides functions for list manipulation: `range, distinct, flatten, reverse, sort, slice`. For more information, see [Lists](https://pkg.go.dev/github.com/google/cel-go/ext#readme-lists). 
  * **Math** : Provides extended mathematical functions like `math.greatest, math.least, math.abs`. For more information, see [Math](https://pkg.go.dev/github.com/google/cel-go/ext#readme-math).



## What's next

Learn about [pretrained processors](https://docs.cloud.google.com/document-ai/docs/pretrained-overview).

[ Previous arrow_back  Derived field and signature detection  ](https://docs.cloud.google.com/document-ai/docs/ce-derived-signature)

[ Next Pretrained overview  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/pretrained-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
