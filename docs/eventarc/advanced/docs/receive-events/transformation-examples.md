---
url: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transformation-examples/
title: Transformation examples \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:05.762520+00:00
---

# Transformation examples  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transformation-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Transformation examples Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

You can transform your [CloudEvents data](https://docs.cloud.google.com/eventarc/advanced/docs/event-format) by writing transformation expressions [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel). For more information, see [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events).

**Caution:** Don't include sensitive information such as passwords, secrets, or personally identifiable information (PII) in CEL transformation expressions. These expressions are treated as service configuration data by Eventarc Advanced and don't have the same level of [data security](https://cloud.google.com/trust-center/security) as event payloads.

The following are some common use cases and examples that show you how to write CEL expressions to transform your event data.

## Standard use cases

The following are some standard use cases when transforming event data.

**Note:** To simplify the examples, required CloudEvents context attributes have been omitted.

### Data normalization

You need to flatten a nested data structure in your event message to allow for easier processing by a downstream service.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "orderId": "12345",
        "customer": {
          "firstName": "Alex",
          "lastName": "Taylor",
          "address": {
            "street": "1800 Amphibious Blvd.",
            "city": "Mountain View"
          }
        }
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "orderId": "12345",
        "customerFirstName": "Alex",
        "customerLastName": "Taylor",
        "customerStreet": "1800 Amphibious Blvd.",
        "customerCity": "Mountain View"
      }
    }

Solution 1:
    

Format the output data manually. This lets you list the field names and pick only the elements needed in the output. This is a reasonable approach when the input is predictable and when the number of fields is low. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. For example:
    
    
    message.setField("data",
    {
      "orderId": message.data.orderId,
      "customerFirstName": message.data.customer.firstName,
      "customerLastName": message.data.customer.lastName,
      "customerStreet": message.data.customer.address.street,
      "customerCity": message.data.customer.address.city,
    })

Solution 2:
    

Use a function in your expression. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. The [`denormalize`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function flattens deep structures to a list of key and value pairs. Field names are delimited using a period (`.`) to segment the structure hierarchy. For example:
    
    
    message.setField("data", message.data.denormalize())

This results in the following output which differs slightly from the expected payload. However, the advantages include a shorter CEL expression which operates on any input, and which automatically includes any number of incoming fields.
    
    
    {
      "data": {
        "orderId": "12345",
        "customer.firstName": "Alex",
        "customer.lastName": "Taylor",
        "customer.address.street": "1800 Amphibious Blvd.",
        "customer.address.city": "Mountain View"
      }
    }

### Data masking

You need to mask sensitive data in an event payload before it's sent on to a less secure environment.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "userId": "user123",
        "email": "alex@example.com",
        "creditCardNumber": "1234-5678-9012-3456"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "userId": "user123",
        "email": "a***@example.com",
        "creditCardNumber": "xxxx-xxxx-xxxx-3456"
      }
    }

Solution:
    

Use an expression to mask any sensitive information such as the email address and credit card number. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. The [`extract`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#regex-functions) regular expression function follows the [RE2 syntax](https://github.com/google/re2/wiki/Syntax). For example:
    
    
    message
          .setField("data.email",
              re.extract(message.data.email,
                        "(^.).*@(.*)",
                        "\\1***@\\2"))
    
          .setField("data.creditCardNumber",
              re.extract(message.data.creditCardNumber,
                        "(\\d{4})\\D*$",
                        "xxxx-xxxx-xxxx-\\1"))

### Data redaction

You need to remove specific fields from an event payload based upon certain conditions.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "orderId": "12345",
        "customerType": "gold",
        "discountCode": "VIP"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      {
      "orderId": "12345",
      "customerType": "gold"
      }
    }

Solution:
    

Use an expression that redacts the `discountCode` field if the `customerType` is "gold". The [`removeFields`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function removes specific fields from an event. For example:
    
    
    message.data.customerType == "gold" ?
          message.removeFields(["data.discountCode"]) :
          message

### Data conversion

You need to convert data from one format or type to another.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "orderDate": "2024-10-31T12:00:00Z",
        "totalAmount": "1500"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "orderDate": 1704086400,
        "totalAmount": 1500.00
      }
    }

Solution:
    

Use an expression which converts `orderDate` to a UNIX timestamp, and the `totalAmount` type from a `string` to a `double` (floating-point number). The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. You can use [string manipulation functions](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#string-manipulation-operators) to convert the string results. For example:
    
    
    message
          .setField("data.orderDate", int(timestamp(message.data.orderDate)))
          .setField("data.totalAmount", double(message.data.totalAmount))

### Conditional routing

You need to route events to different destinations based on the event data.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "eventType": "order.created",
        "orderValue": 200
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "eventType": "order.created",
        "orderValue": 200,
        "routingKey": "highValue"
      }
    }

Solution:
    

Use an expression that adds a `routingKey` field with a "highValue" if the `orderValue` is greater than 100; otherwise, `"normal"`. The `routingKey` field can be used to determine the routing path. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. For example:
    
    
    message.data.orderValue > 100 ?
          message.setField("data.routingKey", "highValue") :
          message.setField("data.routingKey", "normal")

### Default value handling

You need to ensure that certain fields in the event payload have default values if they are not present.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "itemName": "Product A"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "itemName": "Product A",
        "quantity": 1
      }
    }

Solution:
    

Use an expression that adds a `quantity` field with a default value of `1` if the field doesn't already exist. The [`has`](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros) macro tests whether a field is available. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. For example:
    
    
    has(message.data.quantity)  ?
        message :
        message.setField("data.quantity", 1)

### String manipulation

You need to extract or modify parts of a string field in the event data.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "customerEmail": "alex@example.com"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "customerEmail": "alex@example.com",
        "emailDomain": "example.com"
      }
    }

Solution:
    

Use an expression that extracts the domain name ("example.com") from the `customerEmail` field and stores it in a new `emailDomain` field. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. The [`extract`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#regex-functions) regular expression function follows the [RE2 syntax](https://github.com/google/re2/wiki/Syntax). For example:
    
    
    message
      .setField("data.emailDomain",
    re.extract(message.data.customerEmail, "(^.*@)(.*)", "\\2"))

### List and map operations

You need to work with lists or maps in the event data.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "productIds": [
          "product123",
          "product456"
        ]
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "productIds": [
          "product123",
          "product456"
        ],
        "productFound": true
      }
    }

Solution:
    

Use an expression that checks if "product456" exists in the `productIds` list and stores the result (`true` or `false`) in a new `productFound` field. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. The [`exists`](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros) macro tests whether a predicate holds for all elements of a list and combines the results with the "or" operator. For example:
    
    
    message.setField("data.productFound",
            message.data.productIds.exists(id, id == "product123"))

### Error handling

You need to gracefully handle potential errors or unexpected data in the event payload.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "quantity": "abc"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "quantity": 0,
        "error": "Invalid quantity"
      }
    }

Solution:
    

Use an expression that attempts to convert the `quantity` field to an integer. If the conversion fails, set the `quantity` field to `0`, and add a new `error` field with the value "Invalid quantity".

  * The [`has`](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros) macro tests whether a field is available.
  * The [`type`](https://github.com/google/cel-spec/blob/master/doc/langdef.md#type-values) function returns the type of a value.
  * The [`matches`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#regex-functions) regular expression function follows the [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
  * The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key.



For example:
    
    
    // Check if data.quantity exists
    has(message.data.quantity) &&
    // Check if data.quantity is a string
    type(message.data.quantity) == string &&
    // Check if string consists of digits
    message.data.quantity.matches(r'^-?[0-9]+$') ?
      // If data.quantity is valid, use message
      message :
      // If data.quantity is invalid, set to 0 and generate error
      message
        .setField("data.quantity", 0)
        .setField("data.error", "Invalid quantity")

## Complex use cases

The following are some complex use cases when transforming event data.

**Note:** To simplify the examples, required CloudEvents context attributes have been omitted.

### Data transformation

You need to perform multiple transformations on nested event data.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "orderId": "12345",
        "customer": {
          "firstName": "Alex",
          "lastName": "Taylor",
          "email": "alex@example.com",
          "address": {
            "street": "1800 Amphibious Blvd.",
            "city": "Mountain View",
            "state": "CA"
          }
        },
        "items": [
          {
            "itemId": "item1",
            "price": 10.00,
            "quantity": 2
          },
          {
            "itemId": "item2",
            "price": 5.00,
            "quantity": 1
          }
        ]
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "orderId": "12345",
        "customer.firstName": "Alex",
        "customer.lastName": "Taylor",
        "customer.email": "a***@example.com",
        "customer.address.city": "Mountain View",
        "customer.address.state": "CA"
      }
    }

Solution:
    

Use an expression that extracts the city and state from the address, and that masks the email address.

  * The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key.
  * The [`toMap`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#bind-functions) function converts a CEL list of CEL maps to a single CEL map.
  * The [`extract`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#regex-functions) regular expression function follows the [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
  * The [`removeFields`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function removes specific fields from an event.
  * The [`denormalize`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function flattens deep structures to a list of key and value pairs. Field names are delimited using a period (`.`) to segment the structure hierarchy.



For example:
    
    
    message
    .setField("data",
      message.data.setField("customer.address",
        message.data.customer.address.map(key, key == "city" || key == "state",
              { key: message.data.customer.address[key] }).toMap())
      .setField("customer.email",
            re.extract(message.data.customer.email, "(^..?).*@(.*)", "\\1***@\\2"))
      .removeFields(["items"])
      .denormalize()
    )

### Data formatting and routing

You need to format event data, add product information, and then route the event message.

Scenario:
    

Given the following CloudEvents data:
    
    
    {
      "data": {
        "productId": "p123",
        "productName": "Example Product",
        "category": "electronics"
      }
    }

You want to write a CEL expression that results in the following output:
    
    
    {
      "data": {
        "productId": "electronics-p123",
        "productName": "EXAMPLE PRODUCT",
        "category": "electronics",
        "routingKey": "electronics"
      }
    }

Solution:
    

Use an expression that formats the product name to uppercase, adds a prefix to the product ID based on its category, and includes a routing key for downstream processing. The [`setField`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions) function adds or replaces a field of the event with a given key. The [`upperAscii`](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#string-manipulation-operators) function returns a string with all ASCII characters converted to their corresponding uppercase characters. For example:
    
    
    message
    .setField("data.productId",
    message.data.category + "-" + message.data.productId)
    .setField("data.productName", message.data.productName.upperAscii())
    .setField("data.routingKey", message.data.category)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
